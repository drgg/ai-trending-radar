"""用 Claude API 为仓库生成中文介绍；按 README sha 缓存，避免重复调用。"""
import json
import os
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

INTRO_DIR = Path(__file__).resolve().parent.parent / "data" / "intros"
PROMPT_VERSION = 4  # 改动 schema 或提示词时加一，旧缓存会自动重新生成

SYSTEM = """你是一名技术编辑，为中文读者撰写 GitHub 热门 AI 项目的简介。读者会快速浏览，简短比全面更重要。
依据仓库元数据和 README 摘录写作，只陈述材料里有的事实，语言简洁具体，避免空话和营销腔。
- 项目方自报的性能、速度、基准数字都要注明"项目方数据"；如果 README 同时说明该结果没有达到项目自己设定的目标或门槛，要一并写出。
- 不写材料无法支撑的评价，例如"迅速走红""增长迅速""业界领先"。星数本身不算亮点。
- 元数据和 README 的数字冲突时，以 README 为准。
- 描述功能时照 README 的默认行为写；需要手动开启的，要说明"可选"或"需开启"。

各字段的长度上限（中文字符和英文单词各算 1 字，严格遵守）：
- tagline：一句话说清它是什么，不超过 40 字
- positioning：定位说明，不超过 100 字
- features：3–5 条，每条不超过 40 字
- highlights：1–3 条，每条不超过 50 字
- audience：不超过 60 字
- quickstart_cmd：最关键的一条安装或运行命令，原样照抄 README；README 里没有安装或运行命令（例如只提供下载安装包）就返回空字符串，不要用排查、调试类命令代替
- quickstart_note：上手的补充说明，不超过 60 字，必须和 quickstart_cmd 属于同一条安装路径；没有就返回空字符串
字段内部不要自己加 "-"、"•"、编号等列表符号，也不要换行。

风险提示（risks）只在确有依据时填写，每条一句话。属于风险的类型：
- 自动化操作第三方网页或账号，可能违反服务条款或有封号风险。项目的核心功能就是用浏览器自动化、Computer Use 等方式操作别人的服务（包括 ChatGPT 等 AI 服务的网页版）时，必须标注
- 越狱、绕过模型安全限制
- 攻击性安全工具：注明仅限授权测试
- 隐私、版权、肖像权或 AI 内容标识等法规问题，包括把用户或第三方的数据发送给外部服务、采集他人个人信息
- 许可证未声明或非标准（如仅限非商业使用）
- 默认配置不安全：README 明确警告默认设置不可直接暴露到公网
以下不算风险，不要写入 risks：需要联网、需要登录或注册账号、需要 API Key、不接受外部贡献、处于早期版本、效果有随机性、仅支持部分平台。
没有风险就返回空数组。

category 按项目的核心功能选择，分类名本身要让读者一眼看出项目性质：
- 核心功能是越狱、破甲、绕过模型或平台安全限制的，必须选“越狱与绕过模型限制”，即使项目自称用于安全研究
- 核心功能是渗透测试、漏洞利用、红队攻击的，必须选“攻击性安全（仅限授权测试）”
- 只有防御、检测、审计、合规类工具才选“安全防护与合规”
- 核心功能属于其他类别、只是附带服务条款风险的（例如浏览器自动化），按功能归类，风险写进 risks

is_ai_product：项目的核心是否与 AI/LLM/Agent 相关。仅因 README 顺带提到 AI 关键词、或本身是加密货币机器人、网络工具等无关项目时为 false。"""


LENGTH_LIMITS = {"tagline": 40, "positioning": 100, "audience": 60, "quickstart_note": 60,
                 "features": 40, "highlights": 50}
_WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9._\-/+]*")


def text_len(text):
    """中文字符和英文单词各算 1 字，和提示词里的口径一致。"""
    return len(_WORD.sub("W", text))


def length_violations(intro):
    over = []
    for field, limit in LENGTH_LIMITS.items():
        value = intro.get(field) or ""
        for i, item in enumerate(value if isinstance(value, list) else [value], 1):
            n = text_len(item)
            if n > limit:
                label = f"{field}[{i}]" if isinstance(value, list) else field
                over.append(f"{label} {n}/{limit} 字")
    return over


FIELDS = ["is_ai_product", "category", "tagline", "positioning", "features", "highlights",
          "audience", "quickstart_cmd", "quickstart_note", "risks"]


def _schema(categories):
    s = {"type": "string"}
    arr = {"type": "array", "items": s}
    props = {"is_ai_product": {"type": "boolean"},
             "category": {"type": "string", "enum": categories},
             "features": arr, "highlights": arr, "risks": arr}
    for f in FIELDS:
        props.setdefault(f, s)
    return {"type": "object", "properties": props, "required": FIELDS, "additionalProperties": False}


TREND_SCHEMA = {
    "type": "object",
    "properties": {"bullets": {"type": "array", "items": {"type": "string"}}},
    "required": ["bullets"],
    "additionalProperties": False,
}


class AuthError(RuntimeError):
    """认证失败：继续调用没有意义，整期中止。"""


_AUTH_MARKERS = ("Failed to authenticate", "401", "invalid x-api-key", "OAuth")


class Summarizer:
    def __init__(self, cfg, dry_run=False):
        self.cfg = cfg
        self.dry_run = dry_run
        self.calls = 0
        self._client = None
        INTRO_DIR.mkdir(parents=True, exist_ok=True)

    @property
    def client(self):
        if self._client is None:
            import anthropic
            self._client = anthropic.Anthropic()
        return self._client

    def _ask(self, system, user, schema, max_tokens=8000):
        if self.cfg.get("backend", "api") == "claude-cli":
            return self._ask_cli(system, user, schema)
        return self._ask_api(system, user, schema, max_tokens)

    def _ask_cli(self, system, user, schema):
        """通过 Claude Code 非交互模式调用，走订阅额度（CLAUDE_CODE_OAUTH_TOKEN）。"""
        cmd = [shutil.which("claude") or "claude", "-p",
               "--model", self.cfg["model"],
               "--output-format", "json",
               "--json-schema", json.dumps(schema, ensure_ascii=False),
               "--system-prompt", system,
               "--tools", ""]
        # API Key 在认证优先级上高于订阅令牌，这里去掉以免误走 API 计费
        env = {k: v for k, v in os.environ.items()
               if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}
        # 从终端复制的令牌常带折行或末尾换行；令牌本身不含空白，直接去掉
        if env.get("CLAUDE_CODE_OAUTH_TOKEN"):
            env["CLAUDE_CODE_OAUTH_TOKEN"] = "".join(env["CLAUDE_CODE_OAUTH_TOKEN"].split())
        proc = subprocess.run(cmd, input=user, capture_output=True, text=True,
                              encoding="utf-8", timeout=600, env=env)
        self.calls += 1
        try:
            out = json.loads(proc.stdout)
        except json.JSONDecodeError:
            raise RuntimeError(f"claude 输出无法解析（exit {proc.returncode}）：{(proc.stderr or proc.stdout)[:300]}")
        if out.get("is_error"):
            msg = str(out.get("result"))
            if any(m in msg for m in _AUTH_MARKERS):
                raise AuthError(f"Claude 认证失败：{msg}")
            raise RuntimeError(f"claude 调用失败（{out.get('subtype')}）：{msg}")
        data = out.get("structured_output")
        return data if data is not None else json.loads(out["result"])

    def _ask_api(self, system, user, schema, max_tokens):
        """调用 Claude API 并返回解析后的 JSON；Opus/Fable 开启服务端拒答回退。"""
        kwargs = dict(
            model=self.cfg["model"],
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"effort": self.cfg["effort"],
                           "format": {"type": "json_schema", "schema": schema}},
        )
        if self.cfg["model"].startswith(("claude-opus-5", "claude-fable")):
            resp = self.client.beta.messages.create(
                betas=["server-side-fallback-2026-07-01"],
                extra_body={"fallbacks": "default"}, **kwargs)
        else:
            resp = self.client.messages.create(**kwargs)
        self.calls += 1
        if resp.stop_reason == "refusal":
            raise RuntimeError("模型拒绝了该请求")
        if resp.stop_reason == "max_tokens":
            raise RuntimeError("输出被 max_tokens 截断")
        text = next(b.text for b in resp.content if b.type == "text")
        return json.loads(text)

    # ---------- 单个仓库 ----------
    @staticmethod
    def _path(full_name):
        return INTRO_DIR / (full_name.replace("/", "__") + ".json")

    def _stale(self, cached, repo, today):
        if self.dry_run:  # dry-run 不覆盖已有介绍
            return False
        if cached.get("placeholder") or cached.get("prompt_version", 1) != PROMPT_VERSION:
            return True
        if cached.get("readme_sha") == repo.get("readme_sha"):
            return False
        age = (today - date.fromisoformat(cached["generated_at"])).days
        return age >= self.cfg["refresh_after_days"]

    def intro(self, repo, today):
        path = self._path(repo["full_name"])
        if path.exists():
            cached = json.loads(path.read_text(encoding="utf-8"))
            if not self._stale(cached, repo, today):
                return cached
        if self.dry_run:
            intro = self._placeholder(repo)
        else:
            try:
                intro = self.generate(repo)
            except AuthError:
                raise
            except Exception as e:  # 单个失败不影响整期
                print(f"  ! {repo['full_name']} 介绍生成失败：{e}")
                if path.exists():
                    return json.loads(path.read_text(encoding="utf-8"))
                intro = self._placeholder(repo)
        intro.update(readme_sha=repo.get("readme_sha"), generated_at=today.isoformat(),
                     prompt_version=PROMPT_VERSION,
                     model=None if intro.get("placeholder") else self.cfg["model"])
        path.write_text(json.dumps(intro, ensure_ascii=False, indent=2), encoding="utf-8")
        return intro

    def generate(self, repo):
        """调用模型生成介绍；超出字数上限时带着超限清单重试一次，仍超限就保留第二次结果。"""
        schema = _schema(self.cfg["categories"])
        prompt = self._repo_prompt(repo)
        intro = self._ask(SYSTEM, prompt, schema)
        over = length_violations(intro)
        if over:
            retry = (prompt + "\n\n上一版介绍如下，其中这些字段超出了字数上限："
                     + "；".join(over) + "。请在不丢失关键信息的前提下压缩，重新输出完整介绍。\n"
                     + json.dumps(intro, ensure_ascii=False))
            intro = self._ask(SYSTEM, retry, schema)
        return intro

    @staticmethod
    def _repo_prompt(repo):
        meta = {k: repo[k] for k in ("full_name", "description", "stars", "forks", "language",
                                     "license", "topics", "homepage", "created_at", "pushed_at")}
        return (f"<metadata>\n{json.dumps(meta, ensure_ascii=False)}\n</metadata>\n"
                f"<readme_excerpt>\n{repo.get('readme', '')}\n</readme_excerpt>\n"
                "请为这个仓库写中文简介。")

    @staticmethod
    def _placeholder(repo):
        desc = repo["description"] or "（暂无描述）"
        return {"placeholder": True, "is_ai_product": True, "category": "其他",
                "tagline": desc, "positioning": desc, "features": [], "highlights": [],
                "audience": "", "quickstart_cmd": "", "quickstart_note": "", "risks": []}

    # ---------- 趋势小结 ----------
    def trends(self, entries):
        if self.dry_run or not entries:
            return ["（dry-run 模式，未生成趋势小结）"] if self.dry_run else []
        lines = [f"- {e['full_name']}（{e['stars']}★，{e['intro']['category']}）："
                 f"{e['intro'].get('tagline') or e['intro']['positioning']}"
                 for e in entries]
        try:
            return self._ask("你是一名技术编辑。", "以下是本期 GitHub 近三个月新建且星数最高的 AI 项目：\n"
                             + "\n".join(lines)
                             + "\n\n请用 3–5 条中文要点总结本期趋势。每条一句话、不超过 60 字，点名 1–3 个代表项目（只写仓库名，不带所有者）。",
                             TREND_SCHEMA, max_tokens=4000)["bullets"]
        except Exception as e:
            print(f"  ! 趋势小结生成失败：{e}")
            return []
