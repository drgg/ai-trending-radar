# AI Trending Radar

每周一期的刊物：整理 GitHub 近 90 天新建、星数超过 5000 的 AI 项目，用 Claude 为每个项目写中文介绍，**先报本期变化（新上榜 / 涨星 / 移出），完整名录放在后面**。

- 网页：<https://drgg.github.io/ai-trending-radar/>
- 订阅：[RSS](https://drgg.github.io/ai-trending-radar/feed.xml)，或 Watch 本仓库——每期发布时会开一个带「周报」标签的 Issue，上一期的自动关闭
- 给 AI Agent：[llms.txt](https://drgg.github.io/ai-trending-radar/llms.txt) 列出最新一期、往期和原始数据的地址；[latest.md](https://drgg.github.io/ai-trending-radar/latest.md) 是最新一期的纯文本版。两者都在 render 时从快照生成

## 流程
`fetch`（GitHub Search API）→ `summarize`（Claude，按 README sha 缓存）→ `diff`（对比上一个正式期）→ `render`（整站 HTML + RSS + Markdown）→ 部署 Pages → 开 Issue 通知

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
1. 本机运行 `claude setup-token`，复制生成的令牌
2. Settings → Secrets and variables → Actions → 新建 `CLAUDE_CODE_OAUTH_TOKEN`，粘贴令牌
   （如改用 API 计费：`config.yml` 中设 `backend: api`，并新建 `ANTHROPIC_API_KEY`）
3. Settings → Pages → Source 选 **GitHub Actions**
4. Actions → weekly-report → Run workflow 验证

令牌有效期一年，到期后重新生成并更新 Secret。

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
python scripts/main.py --limit 3      # 需要本机 claude 已登录或设置 CLAUDE_CODE_OAUTH_TOKEN
```

## 目录
- `config.yml`：关键词、时间窗口、星数门槛、模型、风险阈值、分类、网址
- `data/snapshots/`：每期快照；`data/intros/`：介绍缓存
- `templates/index.html.j2`：页面模板，设计规格见 `design/issue/DESIGN.md`
- `site/`：生成的网页（`archive/` 为每期存档，`feed.xml` 为 RSS，`assets/fonts/` 为自托管的标题字体子集）
- `report.md`：最新一期 Markdown
- 标题文字改动后运行 `python scripts/fetch_font.py` 重新生成字体子集（Noto Serif SC，OFL 协议）
