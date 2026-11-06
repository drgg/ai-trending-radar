# AI Trending Radar

每周一期的刊物：整理 GitHub 近 90 天新建、星数超过 5000 的 AI 项目，用 DeepSeek 为每个项目写中文介绍，**先报本期变化（新上榜 / 涨星 / 移出），完整名录放在后面**。

- 网页：<https://drgg.github.io/ai-trending-radar/>
- 价值分析：<https://drgg.github.io/ai-trending-radar/analysis.html>，用公开规则给最新一期打分，先给最值得看的项目，最后可按个人情况再筛
- 订阅：[RSS](https://drgg.github.io/ai-trending-radar/feed.xml)，或 Watch 本仓库——每期发布时会开一个带「周报」标签的 Issue，上一期的自动关闭
- 给 AI Agent：[llms.txt](https://drgg.github.io/ai-trending-radar/llms.txt) 列出最新一期、往期和原始数据的地址；[latest.md](https://drgg.github.io/ai-trending-radar/latest.md) 是最新一期的纯文本版。两者都在 render 时从快照生成

## 流程
`fetch`（GitHub Search API）→ `summarize`（DeepSeek，按模型和 README sha 缓存）→ `diff`（对比上一个正式期）→ `activity`（GraphQL 批量取维护信号）→ `render`（整站 HTML + 价值分析页 + RSS + Markdown）→ 部署 Pages → 开 Issue 通知

## 价值分析页（scripts/analysis.py，只为最新一期生成 site/analysis.html）
五项分数，总分最高 11：需求（周增）、采用（fork 占星数）、维护（近 30 天提交与提交者）、可用、风险。≥9 为「现在值得看」，周报首页列出这些项目并链接到分析页。
- 维护信号由 `scripts/activity.py` 用 GraphQL 一次批量查（不占短期榜的 REST 配额），写到 `data/activity/<快照日期>.json`；采集失败不影响出刊，分析页改按最后推送日期估算
- 可用、风险两项和方向、门槛、宿主以 `data/analysis_labels.yml` 的人工标注为准；本期新上榜、还没标注的项目按介绍文字的关键词推断，页面标「自动推断」。每期出刊后补标注再 `--render-only` 即可
- 补采某一期的维护信号：`python scripts/activity.py 2026-11-02`

## 近期趋势（页首）
模型综合本期主榜变化、短期榜和前 3 个正式期的趋势，写一段 150–250 字的分析和 3–5 条要点；前几期说过的结论只在有新证据时才写。原来的「编者按」并入这里。

## 短期榜（scripts/rising.py，参数在 config.yml 的 rising 段）
按 UTC 完整自然日切窗口，D = 运行当天：近 7 天 = D-7…D-1，前 7 天 = D-14…D-8。
- **升星榜**：近一年创建的 AI 项目里，近 7 天新增 ≥1000 星的列名字，≥2000 的前 20 个附一句话介绍；≥5000 标「暴涨」，达到前 7 天 2 倍标「加速」
- **新星**：近 7 天创建、≥500★，每个附一句话介绍（和两期之间的间隔相同，每个项目只会出现一次）
- **新锐**：创建 8–30 天、≥1000★ 列名字，≥2000★ 附一句话介绍
- 超过 5000★ 且 ≤90 天的进主榜，所以三段互不重叠
- 星数增量来自 `/stargazers/history`（2026-06-30 起 stargazers 名单不再公开）
- 疑似刷星：同一作者 ≥4 个项目同周各涨 ≥1000，整组不进榜，单独折叠列出
- 一句话介绍按批生成、缓存在 `data/taglines/`；测速约 850 次 API 请求，配额见底时会等到重置再继续

## 正式期和临时更新
- **正式期**：每周一的定时运行。编期号、开 Issue 通知、进 RSS
- **临时更新**：手动运行（例如改了提示词后重新生成介绍）。照常更新页面，但不编期号、不通知
- 两者都只和**上一个正式期**比较，所以正式期之间永远是周对周
- 早期快照没有 `issue` 字段，按「周一 = 定时运行」推断

## 首次配置
1. 在 DeepSeek 平台创建 API Key，确认账户有余额。
2. Settings → Secrets and variables → Actions → 新建 `DEEPSEEK_API_KEY`。
3. Settings → Pages → Source 选 **GitHub Actions**。
4. Actions → weekly-report → Run workflow，mode 选 `issue` 发布一期。

默认 `backend: deepseek`、`model: deepseek-flash`。每周一北京时间 9 点自动生成正式周报并部署 GitHub Pages，随后发布 Issue 通知。密钥仅保存在环境变量或 Actions Secret，不能提交到仓库。

DeepSeek 使用 JSON 输出并在本地校验 schema；网络或临时服务错误最多尝试三次。认证、余额或主榜/短期榜生成失败时中止，不用占位介绍覆盖线上内容。切换模型会刷新介绍缓存。原有 `claude-cli`（`CLAUDE_CODE_OAUTH_TOKEN`）与 `api`（`ANTHROPIC_API_KEY`）仍可选。

## 手动运行（Actions → weekly-report → Run workflow）
| mode | 做什么 |
|---|---|
| `update`（默认） | 临时更新：重新抓取、生成新介绍，不编期号、不通知 |
| `issue` | 作为正式一期发布（定时任务失败时补发） |
| `render` | 只用已有快照重渲染整站（改了模板时用），不抓取、不调模型 |
| `dry-run` | 不调用模型，验证流程 |

## 本地运行
```bash
pip install -r requirements.txt
python scripts/main.py --render-only  # 用已有快照重渲染整站，改模板后预览用
python scripts/main.py --dry-run      # 不调用模型
python scripts/main.py --limit 3      # 需要设置 DEEPSEEK_API_KEY；完整抓取同时需要 GITHUB_TOKEN 或 gh 登录态
```

## 目录
- `config.yml`：关键词、时间窗口、星数门槛、模型、风险阈值、分类、网址
- `data/snapshots/`：每期快照；`data/intros/`：介绍缓存
- `templates/index.html.j2`：周报模板；`templates/analysis.html.j2`：价值分析页；两页共用 `_base.css.j2`、`_scope.js.j2`，设计规格见 `design/issue/DESIGN.md`
- `templates/icons/`：Phosphor Icons 双色调图标（MIT，许可证同目录）
- `data/activity/`：每期的维护信号；`data/analysis_labels.yml`：分析页的人工标注
- `design/assets/radar-scope.json`：刊头雷达底纹的亮度网格，由 `scripts/make_scope.py` 从公有领域照片生成（需要 Pillow，只在换底图时运行）
- `site/`：生成的网页（`archive/` 为每期存档，`analysis.html` 为价值分析，`feed.xml` 为 RSS，`assets/fonts/` 为自托管的字体子集）
- `report.md`：最新一期 Markdown
- 标题文字改动后运行 `python scripts/fetch_font.py` 重新生成字体子集（标题 ZCOOL XiaoWei、数字 Geist Mono，均为 OFL）；渲染时发现标题用到子集外的字会提示

## 本地模型对比

设置 `DEEPSEEK_API_KEY` 后执行 `python scripts/compare_models.py --snapshot 2026-10-26`，生成主榜和趋势的历史同期对比稿，保存在忽略的 `build/` 下，不发布、不刷新星数；短期榜保留原稿。
