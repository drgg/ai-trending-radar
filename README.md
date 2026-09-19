# AI Trending Radar

每周自动整理 GitHub 近 90 天新建、星数超过 5000 的 AI 项目，用 Claude 为每个项目写中文介绍，并发布到 GitHub Pages。

## 流程
`fetch`（GitHub Search API）→ `summarize`（Claude API，按 README sha 缓存）→ `diff`（与上期对比）→ `render`（HTML + Markdown）

## 首次配置
1. 本机运行 `claude setup-token`，复制生成的令牌
2. Settings → Secrets and variables → Actions → 新建 `CLAUDE_CODE_OAUTH_TOKEN`，粘贴令牌
   （如改用 API 计费：`config.yml` 中设 `backend: api`，并新建 `ANTHROPIC_API_KEY`）
3. Settings → Pages → Source 选 **GitHub Actions**
4. Actions → weekly-report → Run workflow（可先勾选 dry_run 验证）

令牌有效期一年，到期后重新生成并更新 Secret。

之后每周一北京时间 09:00 自动运行。

## 本地运行
```bash
pip install -r requirements.txt
python scripts/main.py --dry-run     # 不调用模型
python scripts/main.py --limit 3     # 需要本机 claude 已登录或设置 CLAUDE_CODE_OAUTH_TOKEN
```

## 目录
- `config.yml`：关键词、时间窗口、星数门槛、模型、风险阈值、分类
- `data/snapshots/`：每期快照；`data/intros/`：介绍缓存
- `site/`：生成的网页（`archive/` 为历史存档）；`report.md`：最新一期 Markdown
