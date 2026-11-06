"""价值分析页：用同一套公开规则给最新一期主榜打分，先给「现在最值得看」的结论，再给逐项证据，最后才是按个人情况匹配。

五项分数（总分最高 11）：
  需求 0–3   周增不少于 3,000 / 1,000 / 300。优先用升星榜的近 7 天新增，其次较上期变化，都没有时按采集日折算
  采用 0–3   fork 占星数不少于 10% / 6% / 3%
  维护 0–3   近 30 天提交不少于 50（且提交者不少于 3）/ 10 / 1；超过 14 天没推送最高 1 分（data/activity/ 没有数据时只看推送日期）
  可用 0–2   有一条命令就能装上得 2；要源码构建、Docker 或只给了仓库得 1；原型、模板或功能未完成得 0
  风险 −0–2  提示里涉及账号条款、隐私、版权授权、法规的条数：两条以上扣 2，一条扣 1；许可证未声明再扣 1（最多扣 2）
判断：≥9 现在值得看；7–8 值得跟踪；风险扣 2 且 ≥6 为有价值先看风险；5–6 按需了解；其余、疑似刷星作者、高风险分类为暂不优先。

可用、风险两项和个人匹配用的方向、宿主、门槛以 data/analysis_labels.yml 的人工标注为准；
没有标注的项目（通常是本期新上榜的）按介绍文字的关键词推断，是近似值，页面上标为「自动推断」。
"""
import datetime as dt
import re
from pathlib import Path

import yaml

import activity
import charts

LABELS = Path(__file__).resolve().parent.parent / "data" / "analysis_labels.yml"

DIRS = {"code": "编码工作流", "model": "模型接入与额度", "design": "设计与视觉", "video": "视频与内容创作", "web": "网页自动化",
        "device": "手机与设备操作", "platform": "自托管 Agent 平台", "infra": "Agent 基础设施", "growth": "SEO 与资讯运营",
        "career": "求职准备", "local": "本地推理与硬件", "niche": "专项工具"}
ORDER = ["code", "career", "design", "local", "platform", "growth", "video", "model", "infra", "web", "device", "niche"]
DIR_ICONS = {"code": "code", "model": "plugs-connected", "design": "paint-brush", "video": "film-strip", "web": "globe", "device": "device-mobile",
             "platform": "hard-drives", "infra": "graph", "growth": "newspaper", "career": "briefcase", "local": "cpu", "niche": "toolbox"}
# 主方向按顺序匹配，先到先得；都不中按周报分类兜底
DIR_RULES = [
    ("career", r"求职|简历|面试|招聘"),
    ("local", r"显卡|Tensor Core|内核模块|本地推理|量化"),
    ("model", r"免费模型|模型网关|本地网关|订阅账号|额度|转发.*模型|模型.*转发"),
    ("growth", r"SEO|GEO|日报|热点站|可见度"),
    ("video", r"视频|短剧|漫剧|剪辑|绘画|ComfyUI|短片|分镜"),
    ("design", r"界面|UI|标志|Logo|吉祥物|插图|图解|SVG|视觉"),
    ("device", r"Android|安卓|adb|手机|桌面宠物|聊天"),
    ("web", r"浏览器|网页|抓取|无头"),
    ("platform", r"自托管.{0,12}(Agent|AI)|Agent 平台|AI 同事|个人 Agent|Agent 工作台"),
    ("infra", r"知识图谱|知识底座|工具 API|持续学习|强化学习|评测|运行时|世界模型"),
    ("code", r"编码|编程|代码|规格|上下文|Codex|Claude Code|终端"),
]
CAT_DIR = {"编程 Agent 与运行框架": "code", "Agent 平台与基础设施": "infra", "AI 应用产品": "niche", "本地推理与模型": "local",
           "Skills 与写作/设计": "design", "开发者工具与集成": "code"}
HOSTS = {"cc": ("Claude Code", r"Claude Code|claude plugin|/plugin marketplace"), "codex": ("Codex", r"Codex"),
         "cursor": ("Cursor", r"Cursor"), "gemini": ("Gemini CLI", r"Gemini CLI"),
         "dsh": ("DeepSeek Harness", r"\bdsh\b|DeepSeek Harness|DSH"), "chatgpt": ("ChatGPT 网页版", r"ChatGPT")}
HABITS = {"parallel": ("同时跑多个 Agent", r"多个.{0,6}Agent|并行|多 Worker|会话状态"),
          "mobile": ("离开电脑也要盯进度", r"手机|iPhone|锁屏|遥控"),
          "spec": ("先写规格再实现", r"规格|评审|规划与审查"),
          "context": ("常被上下文压缩坑", r"上下文压缩|压缩摘要|上下文"),
          "models": ("经常切换模型或账号", r"切换模型|多个模型|模型供应商|免费模型|订阅账号|网关"),
          "docs": ("要 Agent 产出可读的说明", r"HTML|图解|插图|解释")}
# 经历关键词：页面和这里共用，项目文字里出现就算这个领域
TAGS = {
    "video": ["视频", "剪辑", "短视频", "video", "ffmpeg"], "drama": ["短剧", "漫剧", "小说", "剧本", "分镜"],
    "painting": ["绘画", "插画", "comfyui", "stable diffusion", "角色图"],
    "scrape": ["爬虫", "抓取", "采集", "playwright", "selenium", "puppeteer", "浏览器自动化", "scrap"],
    "testing": ["测试", "qa", "appium", "测开"], "android": ["android", "安卓", "adb", "kotlin"], "ios": ["ios", "swift"],
    "frontend": ["前端", "react", "vue", "frontend", "css", "tailwind", "静态站", "静态页"], "ui": ["ui", "界面", "交互设计", "产品设计"],
    "brand": ["品牌", "logo", "标志", "吉祥物"], "writing": ["技术写作", "博客", "文档", "写作", "教程"],
    "news": ["资讯", "聚合", "日报", "周报", "rss", "热点"], "seo": ["seo", "geo", "增长", "投放", "流量", "广告"],
    "kg": ["知识图谱", "知识库", "rag", "graphrag", "向量"], "training": ["训练", "推理", "gpu", "cuda", "pytorch", "微调", "强化学习"],
    "docker": ["docker", "k8s", "kubernetes", "运维", "devops", "部署"],
    "agentdev": ["agent 开发", "智能体", "langchain", "多 agent", "multi-agent", "agent 框架", "可观测", "opentelemetry", "harness"],
    "mcp": ["mcp"], "llm": ["llm", "大模型", "deepseek", "提示词", "prompt"], "reverse": ["逆向", "反编译", "reverse"],
    "game": ["游戏", "mod", "unity", "unreal"], "osint": ["osint", "地理定位", "开源情报"], "pm": ["项目管理", "甘特", "排期"],
    "career": ["求职", "简历", "面试", "校招", "秋招"]}
TAGNAME = {"video": "视频", "drama": "短剧与小说改编", "painting": "AI 绘画", "scrape": "网页抓取", "testing": "测试", "android": "Android",
           "ios": "iOS", "frontend": "前端", "ui": "界面设计", "brand": "品牌设计", "writing": "写作与文档", "news": "资讯聚合",
           "seo": "SEO 与增长", "kg": "知识库", "training": "模型训练与推理", "docker": "部署运维", "agentdev": "Agent 开发", "mcp": "MCP",
           "llm": "大模型应用", "reverse": "逆向", "game": "游戏", "osint": "开源情报", "pm": "项目管理", "career": "求职"}
TIERS = {"top": "现在值得看", "track": "值得跟踪", "risk": "有价值，先看风险", "need": "按需了解", "hold": "暂不优先"}
SEVERE = re.compile(r"服务条款|用户协议|封号|封禁|账号.{0,4}(风险|限制)|隐私|肖像|侵权|版权|知识产权|商标|法规|违法|溯源|水印")
UNFINISHED = re.compile(r"研究原型|并非成品|尚未完成|仍在开发|开发中|alpha", re.I)
EASY_CMD = re.compile(r"^\s*(npx|/plugin|claude (plugin|mcp)|codex plugin|agy plugin|dsh plugin|npm (i|install)|pip3? install|brew install|curl [^\n]*install)")
SELF_HOST = re.compile(r"自托管|Docker|docker compose|部署在自己")


def _tag_hits(text):
    t = text.lower()
    hits = []
    for k, words in TAGS.items():
        for w in words:
            if re.fullmatch(r"[a-z0-9 .+-]+", w):
                if re.search(rf"(^|[^a-z0-9]){re.escape(w)}($|[^a-z0-9])", t):
                    hits.append(k)
                    break
            elif w in t:
                hits.append(k)
                break
    return hits


def _labels(e, v):
    text = " ".join([v["tagline"], v["positioning"], v["audience"], " ".join(v["features"]), v["cmd"], " ".join(e.get("topics") or [])])
    head = v["tagline"] + " " + v["positioning"]
    d = [k for k, rx in DIR_RULES if re.search(rx, v["tagline"], re.I)] or [k for k, rx in DIR_RULES if re.search(rx, head, re.I)]
    d = d or [CAT_DIR.get(v["category"], "niche")]
    hosts = [k for k, (_, rx) in HOSTS.items() if re.search(rx, text)]
    req = ["dsh"] if (v["cmd"].lstrip().startswith("dsh ") or re.match(r"^(dsh|DeepSeek Harness)", v["tagline"])) else []
    any_skill = bool(re.search(r"Agent Skill|SKILL\.md|skills add|技能包", text))
    os_ = [o for o in ("Windows", "macOS", "Linux") if re.search(o, v["positioning"] + v["audience"])]
    level = 3 if (SELF_HOST.search(head) or re.search(r"docker", v["cmd"], re.I)) else 1 if (EASY_CMD.search(v["cmd"]) or any_skill) else 2
    paid = bool(re.search(r"API Key|密钥|订阅|Plus|Pro\b|付费|按量", v["audience"] + v["positioning"] + " ".join(v["risks"])))
    habits = [k for k, (_, rx) in HABITS.items() if re.search(rx, text)]
    return dict(d=d[:2], hosts=hosts, req=req, any=any_skill, os=os_, l=level, paid=paid, h=habits, t=_tag_hits(text))


def _form(v, level, any_skill):
    if any_skill:
        return "Agent Skill"
    if level == 3:
        return "自托管"
    return "一条命令安装" if EASY_CMD.search(v["cmd"]) else "源码或脚本"


def load_labels():
    return yaml.safe_load(LABELS.read_text(encoding="utf-8")) if LABELS.exists() else {}


def score_entry(e, rising_x, act, collected, spam, warn, manual=None):
    v = e["v"]
    n = e["full_name"]
    if rising_x is not None:
        wk, src, prev7 = rising_x["last7"], "近 7 天新增", rising_x["prev7"]
    elif e.get("delta") is not None:
        wk, src, prev7 = e["delta"], "较上期", None
    elif act:
        days = max(1, (dt.date.fromisoformat(collected["at"]) - dt.date.fromisoformat(collected["snap"])).days)
        wk, src, prev7 = round((act["stars"] - e["stars"]) * 7 / days), f"按 {days} 天折算", None
    else:
        wk, src, prev7 = 0, "无数据", None
    M = 3 if wk >= 3000 else 2 if wk >= 1000 else 1 if wk >= 300 else 0
    ratio = e["forks"] / e["stars"] if e["stars"] else 0
    A = 3 if ratio >= .10 else 2 if ratio >= .06 else 1 if ratio >= .03 else 0
    pushed = (act or {}).get("pushed_at") or e["pushed_at"]
    ref = dt.date.fromisoformat(collected["at"] if act else collected["snap"])
    idle = (ref - dt.date.fromisoformat(pushed)).days
    if act:
        c, au = act["commits30"], act["authors30"]
        K = 3 if c >= 50 and au >= 3 else 2 if c >= 10 else 1 if c >= 1 else 0
    else:
        c = au = None
        K = 2 if idle <= 7 else 1 if idle <= 30 else 0
    if idle > 14:
        K = min(K, 1)
    labels = _labels(e, v)
    unfinished = UNFINISHED.search(v["positioning"] + " ".join(v["risks"]) + " ".join(v["highlights"]))
    form = _form(v, labels["l"], labels["any"])
    if manual:
        U, R, form = manual["U"], manual["R"], manual.get("form", form)
        labels.update({k: manual.get(k, [] if k in ("req", "hosts", "os", "h", "t") else False if k == "any" else labels[k])
                       for k in ("d", "req", "hosts", "any", "os", "l", "h", "t")})
        if manual.get("need"):
            labels["paid"] = bool(re.search(r"Key|密钥|订阅|账号|付费|模型|fal", manual["need"]))
    else:
        U = 0 if unfinished else 2 if (EASY_CMD.search(v["cmd"]) or labels["any"]) and labels["l"] < 3 else 1
        severe = sum(1 for r in v["risks"] if SEVERE.search(r))
        R = 2 if severe >= 2 else 1 if severe == 1 else 0
        if any("许可证" in f for f in e["flags"]):
            R = min(2, R + 1)
    total = M + A + K + U - R
    owner = n.split("/")[0]
    if v["category"] in warn or owner in spam:
        tier = "hold"
    elif R >= 2:
        tier = "risk" if total >= 6 else "hold"
    else:
        tier = "top" if total >= 9 else "track" if total >= 7 else "need" if total >= 5 else "hold"
    return dict(n=n, id="p-" + re.sub(r"[^A-Za-z0-9-]", "-", n), u=e["html_url"], owner=owner, tag=v["tagline"], pos=v["positioning"],
                feat=v["features"], hi=v["highlights"], aud=v["audience"], cmd=v["cmd"], note=v["note"], risks=e["notes"],
                stars=e["stars"], live=(act or {}).get("stars", e["stars"]), forks=e["forks"], ratio=round(ratio * 100, 1),
                wk=wk, src=src, prev7=prev7, accel=bool(rising_x and rising_x.get("accel")), commits=c, authors=au, pushed=pushed, idle=idle,
                issues=(act["open_issues"] + act["open_prs"]) if act else None, og=(act or {}).get("og_image"),
                license=e.get("license") or "未声明", lang=(e.get("language") or "").lower(), new=e.get("delta") is None,
                M=M, A=A, K=K, U=U, R=R, total=total, tier=tier, spam=owner in spam, unfinished=bool(unfinished),
                form=form, auto=not manual, need=(manual or {}).get("need", ""), excl=v["category"] in warn, **labels)


def _verdict(x):
    """一句客观短评，只用数字和提示原文拼，不加评价词。"""
    parts = []
    if x["prev7"] is not None:
        trend = "在加速" if x["accel"] else "放缓" if x["wk"] < x["prev7"] else "持平或上升"
        parts.append(f"周增 {x['prev7']:,} → {x['wk']:,}，{trend}")
    else:
        parts.append(f"{x['src']} {x['wk']:+,}")
    parts.append(f"fork 比例 {x['ratio']}%")
    if x["commits"] is not None:
        parts.append(f"近 30 天 {x['commits']:,} 次提交、{x['authors']} 位提交者")
    if x["idle"] > 14:
        parts.append(f"最后推送 {x['pushed']}")
    s = "；".join(parts) + "。"
    if x["spam"]:
        s += "作者账号被短期榜标记为疑似刷星，星数参考价值低。"
    elif x["unfinished"]:
        s += "项目自述仍是原型、模板或未完成。"
    if x["risks"]:
        s += "提示：" + x["risks"][0].rstrip("。") + "。"
    return s


def _signals(x, rank_ratio):
    """把需求、采用、维护三项按得分分成长处（≥2 分）和短板（≤1 分），各配一句带数字的说明。"""
    demand = (f"近 7 天新增 {x['wk']:,} 星，前 7 天 {x['prev7']:,}" + ("，在加速" if x["accel"] else "")) if x["prev7"] is not None         else f"{x['src']} {x['wk']:+,} 星"
    adopt = f"fork 比例 {x['ratio']}%，在本期 {rank_ratio[1]} 个项目里排第 {rank_ratio[0]}"
    upkeep = (f"近 30 天 {x['commits']:,} 次提交、{x['authors']} 位提交者，最后推送 {x['pushed']}" if x["commits"] is not None
              else f"最后推送 {x['pushed']}")
    good, weak = [], []
    for score, name, text in ((x["M"], "需求", demand), (x["A"], "采用", adopt), (x["K"], "维护", upkeep)):
        (good if score >= 2 else weak).append(f"{name}：{text}。")
    if x["U"] == 2:
        good.append(f"上手：{x['form']}，门槛低。")
    return good, weak


def _why(x, rank_ratio):
    return _signals(x, rank_ratio)[0]


def _but(x, rank_ratio):
    out = _signals(x, rank_ratio)[1] + list(x["risks"][:3])
    if x["issues"] and x["issues"] >= 300:
        out.append(f"未关闭的 issue 和 PR 有 {x['issues']:,} 个。")
    if not x["risks"]:
        out.append("周报没有给出风险提示；性能数字多为项目方自报，用前回 README 核对。")
    return out


def build(ctx, cfg, icons):
    s = ctx["s"]
    act_data = activity.load(s["date"])
    collected = {"at": act_data["collected_at"] if act_data else s["date"], "snap": s["date"]}
    rising = s.get("rising") or {}
    surge = {x["full_name"]: x for x in rising.get("surge", [])}
    spam = set((rising.get("stats") or {}).get("spam_owners", []))
    warn = cfg.get("warn_categories") or {}
    manual = load_labels()
    items = [score_entry(e, surge.get(e["full_name"]), (act_data or {}).get("repos", {}).get(e["full_name"]), collected, spam, warn,
                         manual.get(e["full_name"])) for e in ctx["ranked"]]
    items.sort(key=lambda x: (-x["total"], -x["wk"]))
    by_ratio = sorted(items, key=lambda x: -x["ratio"])
    for x in items:
        x["v"] = _verdict(x)
        rr = (by_ratio.index(x) + 1, len(items))
        x["why"] = _why(x, rr)
        x["but"] = _but(x, rr)
    counts = {k: sum(1 for x in items if x["tier"] == k) for k in TIERS}
    dir_icons = {k: icons[DIR_ICONS[k]] for k in DIRS}
    used = [k for k in ORDER if any(x["d"][0] == k for x in items)]
    return dict(
        items=items, tops=[x for x in items if x["tier"] == "top"], counts=counts, tiers=TIERS, dirs=DIRS, order=used,
        dir_icons=dir_icons, radar=charts.radar(items, ORDER, DIRS, dir_icons),
        collected=collected, has_activity=bool(act_data),
        js=dict(items=[{k: x[k] for k in ("n", "id", "u", "owner", "tag", "d", "hosts", "req", "any", "os", "l", "paid", "h", "t", "lang", "accel",
                                           "prev7", "wk", "risks", "spam", "tier", "total", "cmd", "stars", "form", "auto", "need", "excl")} for x in items],
                dirs=DIRS, tiers=TIERS, hosts={k: v[0] for k, v in HOSTS.items()}, habits={k: v[0] for k, v in HABITS.items()},
                tags=TAGS, tagname=TAGNAME, dirIcons=dir_icons),
    )


def summary(an):
    """周报首页用：本期最值得看的项目名单。"""
    return [{"n": x["n"], "id": x["id"], "total": x["total"]} for x in an["tops"]]
