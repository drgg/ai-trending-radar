"""用 Claude API 为仓库生成中文介绍；按 README sha 缓存，避免重复调用。"""
import json
import os
import shutil
import subprocess
from datetime import date
from pathlib import Path

INTRO_DIR = Path(__file__).resolve().parent.parent / "data" / "intros"

SYSTEM = """你是一名技术编辑，为中文读者撰写 GitHub 热门 AI 项目的简介。
依据仓库元数据和 README 摘录写作，只陈述材料里有的事实；项目方自报的性能数字要注明"项目方数据"。
语言简洁具体，避免空话。

风险提示（risks）只在确有依据时填写，每条一句话，常见类型：
- 自动化操作第三方网页/账号、可能违反服务条款或有封号风险
- 越狱、绕过模型安全限制
- 攻击性安全工具：注明仅限授权测试
- 隐私、版权、肖像权或 AI 内容标识等法规问题
- 许可证未声明或非标准
没有风险就返回空数组。

is_ai_product：项目的核心是否与 AI/LLM/Agent 相关。仅因 README 顺带提到 AI 关键词、或本身是加密货币机器人、网络工具等无关项目时为 false。"""


def _schema(categories):
    s = {"type": "string"}
    return {
        "type": "object",
        "properties": {
            "is_ai_product": {"type": "boolean"},
            "category": {"type": "string", "enum": categories},
            "positioning": s,
            "features": s,
            "highlights": s,
            "audience": s,
            "quickstart": s,
            "risks": {"type": "array", "items": s},
        },
        "required": ["is_ai_product", "category", "positioning", "features",
                     "highlights", "audience", "quickstart", "risks"],
        "additionalProperties": False,
    }


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
            raise RuntimeError(f"claude 调用失败：{msg}")
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
        if cached.get("placeholder") and not self.dry_run:
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
                intro = self._ask(SYSTEM, self._repo_prompt(repo), _schema(self.cfg["categories"]))
            except AuthError:
                raise
            except Exception as e:  # 单个失败不影响整期
                print(f"  ! {repo['full_name']} 介绍生成失败：{e}")
                if path.exists():
                    return json.loads(path.read_text(encoding="utf-8"))
                intro = self._placeholder(repo)
        intro.update(readme_sha=repo.get("readme_sha"), generated_at=today.isoformat(),
                     model=None if intro.get("placeholder") else self.cfg["model"])
        path.write_text(json.dumps(intro, ensure_ascii=False, indent=2), encoding="utf-8")
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
        return {"placeholder": True, "is_ai_product": True, "category": "其他",
                "positioning": repo["description"] or "（暂无描述）",
                "features": "", "highlights": "", "audience": "", "quickstart": "", "risks": []}

    # ---------- 趋势小结 ----------
    def trends(self, entries):
        if self.dry_run or not entries:
            return ["（dry-run 模式，未生成趋势小结）"] if self.dry_run else []
        lines = [f"- {e['full_name']}（{e['stars']}★，{e['intro']['category']}）：{e['intro']['positioning']}"
                 for e in entries]
        try:
            return self._ask("你是一名技术编辑。", "以下是本期 GitHub 近三个月新建且星数最高的 AI 项目：\n"
                             + "\n".join(lines)
                             + "\n\n请用 3–5 条中文要点总结本期趋势，每条一句话，尽量点名代表项目。",
                             TREND_SCHEMA, max_tokens=4000)["bullets"]
        except Exception as e:
            print(f"  ! 趋势小结生成失败：{e}")
            return []
