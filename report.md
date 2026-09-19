# GitHub 近 90 天 AI 热门项目（Stars > 5000）

- 数据快照：2026-09-19　共 27 个项目

## 本期变化
首期，暂无对比。

## 趋势小结
- Agent Skills 生态迅速标准化并向创意与专业领域扩张：从 petergyang/no-ai-slop（去 AI 味写作）、hypit-ai/hypit 与 Vincentwei1021/video-shotcraft（视频创作）、jakubkrehel/skills（UI/UX 设计）到 larashero3-dotcom/lieflat-charts（数据可视化）、s1dashu/ip-as-logo-skill（Logo 设计），Claude Code/Codex 等编程 Agent 正被“技能插件化”改造为多领域生产力工具。
- 企业级 Agent 运行时与基础设施成为竞争新焦点：yc-software/qm（团队协作 harness）、truefoundry/trueforge 与 unicity-aos/aos-ce（agent operating system）、CopilotKit/OpenBot（可审计协作平台）、oomol-lab/open-connector（统一连接器网关）纷纷抢占“承载/调度/管控 Agent”的底层平台位置。
- 为编程 Agent 补齐“记忆”与“知识库”成为新刚需：langchain-ai/openwiki 自动生成可持续维护的代码 Wiki、trailhq/Graft 构建代码库知识图谱、deeplethe/utopia 提供企业级双时态知识本体，共同解决 Agent 每次任务都要从零探索上下文的痛点。
- 薅订阅额度与复用真实浏览器/终端环境成为新趋势：miuuyy/codex-chatgpt-web、XiaoDuoYa/codex-with-chatgpt 让 Codex 借用 ChatGPT 网页版算力，Tencent/BrowserSkill 与 google/artemis 则让 Agent 直接操控用户已登录的浏览器或测试设备，凸显“环境复用”优于“重新造轮子”的实践思路。
- AI 安全与对抗性工具双线增长：elder-plinius/T3MP3ST 将编程 Agent 武器化为自动红队渗透工具、MDX-Tom/gpt-instruct 提供 Codex 越狱提示词，而 guillaumemeyer/watermarks-remover 则反向清除 AI 溯源水印，反映出围绕 Agent 能力边界的攻防博弈正在加剧。

## 编程 Agent 与运行框架

### [xai-org/grok-build](https://github.com/xai-org/grok-build) ⭐ 26,872
- **定位**：xAI（项目署名SpaceXAI）推出的终端AI编程代理 grok，以全屏TUI形式运行，可理解代码库、编辑文件、执行命令，定位与OpenAI Codex CLI、Claude Code等终端编程Agent类似
- **能做什么**：全屏、支持鼠标交互的TUI界面；理解代码库、自动编辑文件、执行shell命令、联网搜索、管理长时间运行任务；支持交互式、headless（脚本/CI）、通过Agent Client Protocol（ACP）嵌入编辑器三种运行方式；支持MCP服务器、插件、hooks、主题、沙箱等扩展机制；首次启动通过浏览器完成身份认证
- **亮点**：由xAI官方发布，创建仅两月余（2026-07-14）已获2.6万+ star，热度增长迅速；Rust编写，通过DotSlash管理构建工具链；仓库定期从xAI内部monorepo同步；工具实现中包含对openai/codex和sst/opencode的移植代码（第三方声明中注明）；不接受外部代码贡献
- **适合**：需要命令行/终端AI编程助手的软件开发者，尤其是已在使用类似Codex CLI、Claude Code、opencode等工具、希望尝试xAI官方方案的用户
- **上手**：macOS/Linux执行 curl -fsSL https://x.ai/cli/install.sh | bash 安装，Windows PowerShell执行 irm https://x.ai/cli/install.ps1 | iex，安装后运行 grok --version 验证；也可用cargo从源码构建（需先安装DotSlash和protoc）

### [trailhq/Graft](https://github.com/trailhq/Graft) ⭐ 8,618
- **定位**：Graft 是为 Claude Code、Cursor、Codex、Gemini 等编码 Agent 提供代码库知识图谱的开源 CLI 工具，通过一次性构建可读的 Markdown 节点图谱，让 Agent 无需每次任务都从零探索代码库，从而更快、更省、且更准确地完成任务。
- **能做什么**：- `graft init` 一键接入 Claude Code：自动构建代码图谱并在 `.claude/` 下写入 statusline 和 hooks，后续每轮对话自动拉取相关节点、后台增量重建图谱；
- 图谱以 tree-sitter 静态解析（Tier 1，$0、无需模型/密钥）为基础，构建 per-symbol 代码图（wiring.json）；可选 `--deep` 模式用 LLM（OpenAI/Anthropic/OpenRouter/Fireworks/Groq/本地模型等，使用用户自己的 key）对每个文件生成摘要并分组为若干"节点"（子系统/关键文件/概念），节点内容是用自然语言解释代码作用和关联关系，而非符号列表；
- 每次查询前自动按内容哈希增量刷新图谱（约 3ms，无改动时几乎零成本），保证图谱与未提交的工作区改动保持同步；
- 图谱本身是本地可再生缓存（类似 node_modules），自动加入 `.gitignore`，团队共享的是 `graft init` 写入的接入配置，各自运行 `graft build` 生成本地图谱；
- 支持 MCP server 集成、CLI 命令（`graft grep`/`graft map`/`graft viz` 等）、多语言解析（23 种语言，含全保真度的 TS/JS/Python/Go/Java/Kotlin/PHP/Swift/R，以及广泛支持的 Rust/C/C++/C#/Ruby 等），并可选接入 LSP（rust-analyzer、clangd、gopls、pyright 等）获得更精确的调用边。
- **亮点**：项目方给出的自测数据（Claude Sonnet 5 harness，162 次运行）：接入 Graft 后工具调用减少 46%、token 节省 42%、耗时减少 60%，正确率不降反升；在 SWE-bench Verified（50 个实例）上，接入 Graft 后解决率从 54% 提升到 66%（+12 分），同时 token 减少 23%、成本降低 19%、耗时减少 32%。项目方称此结果源于图谱能让 Agent 一次性发现需要修改的所有相关文件，而非漏改部分文件导致测试失败。
- **适合**：使用 Claude Code、Cursor、Codex、Gemini 等 AI 编码 Agent 的开发者，尤其是希望降低大型代码库探索成本、提升多文件改动准确率的团队。
- **上手**：全局安装：`npm install -g @nanonets/graft`，然后运行 `graft init` 构建图谱并接入所选编码 Agent（可用 `--dry-run` 预览改动，`--agents claude` 指定单一 Agent）；也可用 `npx @nanonets/graft init` 免全局安装直接运行。之后每次修改代码，`graft build` 会增量更新图谱，团队协作时提交 `.claude/` 等接入配置，各成员本地运行 `graft build` 生成自己的图谱副本。

### [google/artemis](https://github.com/google/artemis) ⭐ 7,956
- **定位**：ARTEMIS 是 Google 开源的 Android 自动化测试 Agent，能把自然语言指令转化为在真机或模拟器上执行的端到端操作流程，并生成日志与诊断报告，同时可作为 MCP 服务器接入 Antigravity、Codex、Claude Code 等 AI 编程助手，让它们直接操控测试设备。
- **能做什么**：• 跨应用自然语言自动化：根据文字描述完成测试用例或日常任务的连续操作；
• 多模态元素定位：优先使用无障碍元素索引，辅以坐标和视觉模型定位，兼容自定义 Canvas/Compose/Flutter 界面；
• MCP 集成：内置 MCP 服务器，支持 Antigravity、Claude Code、Windsurf、Cursor、Codex 等 IDE 直接驱动设备、采集 Logcat 和截图；
• 双执行档位：Flash（约 3–5 秒/步的反应式循环，适合常规确定性任务）与 Pro（15–40 秒/步的多智能体规划-执行-校验图，含 Planner/Operator、预执行安全网与执行事件恢复机制）；
• 提供 Web 可视化测试控制台、开发者 CLI、Python SDK（含 Pydantic 结构化输出）及零运行时依赖的 artemis-client 客户端，可接入 pytest/CI 等自动化测试流程；
• 会在设备上安装名为 Artemis Accessibility Helper 的无障碍服务用于读取屏幕结构，可预装/卸载，也可切换为 UIAutomator2 后端。
- **亮点**：在 Google Research 的 AndroidWorld 基准（20+ 应用、100+ 多步骤任务）上达到 99%+ 任务完成率（项目方数据）；出自 Google 官方仓库，Apache-2.0 许可，上线一个月内即获近 8000 星，社区关注度高。
- **适合**：Android 应用测试/QA 工程师、移动端自动化测试团队、使用 AI 编程助手（Antigravity/Claude Code/Codex 等）进行调试和缺陷复现的开发者。
- **上手**：连接已开启 USB 调试的 Android 设备或模拟器后，克隆仓库并执行一键启动脚本（macOS/Linux 用 ./start.sh，Windows 用 .\start.bat），脚本会自动安装 ADB/scrcpy/FFmpeg 等工具链并提示配置 MCP 及 AI IDE 规则，随后可通过浏览器访问 http://localhost:8000 使用可视化控制台，或用 `uv run artemis run "指令内容" --profile flash` 从命令行直接执行任务；也可用 `uv run artemis mcp --install all` 将其接入各类 AI IDE 的 MCP 配置。
- ⚠️ 会在被测手机上安装并运行一个无障碍服务（Artemis Accessibility Helper）读取屏幕内容，使用前需了解其权限范围及卸载方式。

### [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) ⭐ 5,482
- **定位**：让 Codex 复用 ChatGPT 网页版订阅额度做规划与审查的桥接工具：ChatGPT 负责思考（规划、Review），Codex 负责实际执行代码任务，避免重复消耗 API/Codex Token。
- **能做什么**：以 Codex Skill 形式安装，通过本地回环 HTTP 服务（C2C Bridge）连接 ChatGPT 与 Codex；数据面基于只读 MCP，提供 workspace_info、read_file、git_diff、test_status 等 9 个只读工具供 ChatGPT 按需读取工作区代码，仓库内容不会整体上传；控制面通过极小的 [C2C] 状态消息（INIT→PLAN→EXECUTED→REVIEW→DONE）在 ChatGPT 与 Codex 间同步执行状态；连接采用 OAuth 2.1（PKCE、动态客户端注册、刷新令牌轮换）+ 一次性配对码鉴权；默认使用 Cloudflare Quick Tunnel 做公网穿透，也支持绑定自有域名的稳定地址；提供 c2c CLI（setup/status/doctor/pair/logs 等）用于本地管理。
- **亮点**：无需 API Key、无逆向代理，直接用官方 ChatGPT 网页端做规划审查；服务端不存在写/删/shell/commit 等工具，从架构上保证只读，防止提示注入获得写权限；敏感文件（.env、密钥、SSH 凭据等）默认拒绝读取；每个 workspace 的令牌绑定单一目录，路径逃逸（符号链接、../、绝对路径）经测试阻断；Skill 每日自动检查更新；项目方称测试覆盖 150 个用例（路径安全、OAuth、配对、MCP 端到端）。
- **适合**：使用 Codex 编码、同时已订阅 ChatGPT Plus/Pro 想复用网页版额度做规划与代码审查的开发者
- **上手**：将仓库 skill/ 目录复制到 ~/.codex/skills/codex-with-chatgpt/，对 Codex 说"使用 Codex with ChatGPT 完成首次配置"完成 OAuth 配对与隧道搭建；之后对 Codex 说"Use Codex with ChatGPT to implement XXX"即可使用；也可用仓库提供的一段自然语言提示词让 Codex 自动完成环境检测、克隆、构建、安装全过程。
- ⚠️ 依赖 Cloudflare Quick Tunnel 将本地服务暴露到公网，配置或使用不当可能带来未授权访问风险
- ⚠️ 项目为非官方社区项目，与 OpenAI 无关联，且属于 V1 早期版本，可能存在未覆盖的边界问题

## Agent 平台与基础设施

### [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) ⭐ 22,333
- **定位**：一款面向 AI Agent 生态的"去水印/去溯源标记"工具：以 Agent Skill + 纯 Python 标准库服务的形式，批量清除文本与文件中的多厂商 AI 溯源标记（如 C2PA、SynthID、隐形 Unicode 水印等），用于清理"用户自有内容"上的痕迹。
- **能做什么**：分为三层能力：Layer A 用确定性脚本清除隐形 Unicode、异形空格、bidi 控制符等文本痕迹；Layer B 针对统计型 token 采样水印（如 Kirchenbauer 绿名单、Aaronson keyed-Gumbel）依赖 Agent 改写或脚本 hook；文件层支持 PNG/JPEG/PDF/DOCX/MP4/MP3 等数十种格式的 C2PA/EXIF/XMP/文档属性清除。可作为 Claude Code 插件市场一键安装，注册 PostToolUse hook 在 Agent 写文件时自动检测或清理；也支持 Cursor、Grok、Cowork/claude.ai 等多种宿主安装；服务端仅依赖 Python 3.10+ 标准库，无需 Docker。
- **亮点**：上线约一个月（2026-08 创建）即获 2.2 万+ star，是近期 GitHub 热门项目；技能本身"零代码"，通过 HTTP 调用后端服务实现跨 Agent 宿主（Claude Code、Cursor、Grok 等）复用；提供确定性的文件写入 hook，与 pre-commit gate、CI SARIF 导出共用同一套检测逻辑，弥补"模型是否调用 skill 不确定"的问题。
- **适合**：使用 Claude Code / Cursor / Grok 等 AI 编程助手的开发者、需要清理自有内容中 AI 生成痕迹的写作者与内容团队。
- **上手**：Claude Code 用户可通过插件市场安装：`/plugin marketplace add guillaumemeyer/watermarks-remover` 后 `/plugin install watermarks-remover@watermarks-remover`；或用 `python3 install_skill.py --skill remove-ai-marks --target claude-code` 安装到本地技能目录，再执行 `make serve` 启动本地 HTTP 服务（默认 127.0.0.1:8765），随后用 `/remove-ai-marks` 或直接调用 `service/scripts/clean_file.py` 处理文件。
- ⚠️ 该工具核心功能是移除 AI 生成内容的溯源/水印标记（如 C2PA、SynthID），若用于非自有或未获授权的内容，可能违反平台条款或 AI 内容标识相关法规（如要求标注 AI 生成内容的监管要求）。

### [yc-software/qm](https://github.com/yc-software/qm) ⭐ 15,159
- **定位**：QM 是面向企业/团队的“多人协作型”AI Agent 承载平台（harness），支持在 Slack 和 Web 端使用，让公司内每个员工拥有独立的个人工作空间，同时也能在频道、群聊和项目中与 Agent 协作，替代常见的“个人助理式”单人 Agent 方案。
- **能做什么**：核心为无头（headless）服务，用 Postgres 持久化会话、记忆与队列；Agent 执行循环可切换 Pi、OpenCode、Codex、Claude Code 等多种开源 harness 与模型，不绑定单一厂商；每个用户/房间拥有独立作用域的记忆、文件、密钥视图、权限、定时任务（cron）和常驻沙箱环境；支持在沙箱中运行 `execute` 工具执行命令、构建并发布内部 Web 应用；技能（skills）按作用域归属并可授权共享，管理员可将其提升为全组织可用，也可从 git 仓库导入技能包；支持 cron、监听（watch）和入站 webhook 驱动的后台自动化任务；管理员可配置组织级安全与共享策略，以及可用的 harness/模型范围。
- **亮点**：区别于单人助理式 Agent，QM 强调“个人 + 共享”双重作用域的协作模型，个人自定义与团队协同可以共存；架构上将 harness、会话存储、沙箱、记忆等全部抽象为可替换接口，声称对模型和 harness 厂商中立；提供两套独立可配置的安全策略——执行安全（Strict/Auto/Dangerous，控制人工审批与内容审查）与共享策略（Isolated/Open，控制跨作用域的文件/记忆访问及来源标注和审计），并对跨上下文读取做出多项限制（如候选窗口上限、二进制文件需显式共享）；部署通过独立的“部署仓库”依赖 `@yc-software/qm` 包完成，企业可在自己的云账号（Fly 或 AWS）中运行，核心代码库与部署配置分离，便于后续升级。
- **适合**：需要为团队/公司整体部署内部协作型 AI Agent 的技术负责人、平台工程师和企业 IT/安全管理员，尤其是已在使用 Claude Code、Codex、OpenCode 等编码 Agent 且希望统一到 Slack/Web 协作场景的初创公司团队。
- **上手**：让编码 Agent 执行“部署 https://github.com/yc-software/qm”指令，由其按仓库内的部署指南自动完成；也可先通过第三方托管版本（agent37.com/qm）试用。正式部署方式是创建组织所属的部署仓库并执行 `npm exec --package=@yc-software/qm@latest -- qm init . --org <slug> --target <fly-or-aws>` 后 `npm install`，完成基础设施、登录、连接器凭证、Slack 接入等配置；本地调试可用 `npm run dev-instance:web`（网页/管理端）或 `npm run dev-instance:slack`（Slack）。
- ⚠️ 提供“Dangerous”安全模式，可关闭内容审查且工具调用之间无需人工审批，管理员配置不当可能导致 Agent 执行未经审核的高风险操作
- ⚠️ Agent 以用户本人的凭证和权限代表其执行操作（含在沙箱中运行任意命令、访问内部系统），部署方需自行评估权限范围和审计机制

### [deeplethe/utopia](https://github.com/deeplethe/utopia) ⭐ 8,525
- **定位**：Utopia 是 DeepLethe 开源的"企业世界模型"，定位为一套能被动学习、自我治理的知识工程底座：在双时态知识图谱和本体之上运行冲突检测、推理与决策，目标是为企业 Agent 提供可离线部署、可审计的知识与决策核心，而非单纯的向量库或知识图谱。
- **能做什么**：架构为单个 Rust 二进制 + PostgreSQL（pgvector），内置全文检索（Tantivy）、向量检索与 RRF 融合排序；支持 PDF/DOCX/PPTX/XLSX 等多格式文档摄取及网页、RSS、GitHub、Jira、Notion、WebDAV、S3 定时同步；内置 agent harness 支持对话式操作、文档检索、图谱遍历（按时间点/时间段查询）及挂载数据库查询（Ontology2SQL 支持 Postgres/MySQL/Trino/Databricks/Snowflake）；每个知识库暴露 MCP Server 供 Claude Desktop、Cursor 等 Agent 客户端连接；内置 schema.org、W3C Org、PROV-O、FOAF、IOF Core 等本体包；实体消歧三阶段流程（精确匹配、向量相似、模型裁决）及人工复核队列；基于本体公理的前向链推理（可选开启）；三类冲突检测（事实冲突、公理违反、本体自相矛盾）及处理策略；多用户角色权限管理；append-only 决策台账记录所有确认/合并/回滚操作。
- **亮点**：部署极简，只需一个 Rust 二进制加一个 Postgres 实例，无需额外中间件；双时态图谱同时记录"事实何时为真"与"系统何时相信"，支持决策回溯审计；配套的 Ontology2SQL 方法据项目方数据在 BIRD Mini-Dev（SQLite/PostgreSQL）榜单上表现领先；兼容任意 OpenAI 协议端点（DeepSeek、Qwen、GLM、Ollama、vLLM），可全程 air-gapped 运行；GitHub 8500+ star、1000+ fork，关注度较高。
- **适合**：需要私有化部署知识管理/RAG系统的企业技术团队、知识图谱和本体工程师，以及希望为 AI Agent 构建可信知识底座和决策审计能力的开发者。
- **上手**：克隆仓库后执行 `docker compose --profile app up -d` 启动预构建镜像，访问 http://localhost:1516 注册（首个账号自动成为系统管理员），随后在 Administration → Models 中配置对话与向量模型端点即可开始摄取文档；本地开发需 Rust 1.85+、Node 20+、pnpm，分别启动数据库、`cargo run -p utopia-server` 后端与 `pnpm dev` 前端。
- ⚠️ 项目仍处于 v0.1 早期阶段，数据库 schema 随版本演进且迁移只能前滚、不支持回滚，生产环境升级前需固定镜像版本并备份数据
- ⚠️ README 明确要求在将其暴露到公网前先阅读 SECURITY.md，说明默认配置可能存在安全隐患需自行加固

### [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) ⭐ 8,463
- **定位**：AOS Community Edition 是一个开放的"智能体操作系统"（agent operating system），为 AI Agent 提供可检查、可组合的运行环境，用 Rust 实现，由 aos CLI 和 HTTP API 统一管理 Agent 的运行时、能力模块和权限边界。
- **能做什么**：提供 aos CLI 与 HTTP API 作为产品统一入口；capsules（胶囊）是用户态的最小能力构建块，官方发行版内置 22 个生产级 capsule，可组合成 harness、meta-harness、连接器等更复杂系统；Forge 作为系统构建工具，教 Agent 检查运行中的系统、发现能力缺口并构建最小权限 capsule；meta-harness skill 引导 Agent 把自身指令、记忆、技能、工具、trace 等当作可迭代改进的用户态世界；aos mcp serve 作为 MCP 服务边界，供 Codex、Claude、Grok 等客户端共享同一操作系统，并提供本地审批界面（macOS AppKit、Windows 原生对话框、Linux Pinentry）；支持 stable/dev/nightly 等签名发布渠道，运行时版本通过 runtime-compatibility.toml 精确锁定，发布产物附带校验和、Sigstore 签名与 GitHub 构建溯源证明。
- **亮点**：把 Agent 运行环境当作真正的操作系统来设计（有 init/status/migrate/update/daemon 等根命令边界，而非松散脚本集合）；发布流程强制机器可读的兼容性与自愈校验门（fail-closed），未通过签名验证的渠道不可用；capsule 机制强调最小权限和可审计（Unicity Audit）；同一套系统可被 Codex、Claude、Grok 等多个 Agent 客户端通过 MCP 共享使用。
- **适合**：需要为 AI Agent 构建可审查、可复用运行环境的开发者与系统工程师，以及希望在 Codex/Claude/Grok 等多个 Agent 客户端之间共享统一能力体系（capsule、工具、审批策略）的团队。
- **上手**：执行安装脚本 `curl --proto '=https' --tlsv1.2 -fsSL https://aos.unicity.ai/install.sh | sh` 安装 aos 命令及其固定运行时，随后运行 `aos init`（支持 `--offline` 离线模式）完成 22 个 Community Edition capsule 的初始化；也可用 `aos status`、`aos doctor`、`aos mcp serve` 等命令检查状态或对接 MCP 客户端。
- ⚠️ fork/star 比例异常（21/8463），热度可能有水分

### [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) ⭐ 5,811
- **定位**：OpenConnector 是一个开源的连接器/认证网关，为 AI Agent 和应用提供统一入口，接入 1000+（README 中另一处称 1500+）SaaS 服务商与超过 10000 个预制 Action，是 Pipedream/Composio 的开源替代方案。
- **能做什么**：支持 GitHub、Gmail、Notion、BigQuery、Google Analytics、Supabase、Airtable、Slack 等主流服务的连接器目录；统一处理 API Key、OAuth2、自定义凭证及无认证场景；提供可审查的 Action 契约（请求/响应 schema、所需权限范围、懒加载执行源）；具备连接身份、作用域、运行时令牌、Action 允许/拦截策略、临时文件中转和脱敏运行日志等运行时控制；支持通过 SDK（TypeScript）、oo CLI、MCP、HTTP/OpenAPI 及 Web 控制台多种方式接入；可本地 Docker/Node.js 部署，使用 SQLite 或 PostgreSQL 存储，本地或 S3 兼容对象存储中转文件，也支持 Kubernetes Helm、Fly.io、Cloudflare Workers 部署及 OOMOL 托管运行时。
- **亮点**：核心价值是把服务商凭证与密钥封装在网关运行时边界内，Agent 进程本身不接触真实凭证，只获得元数据、脱敏账户标签和执行结果；同一套 provider id、Action id、schema 和契约可在开源自托管与 OOMOL 商业托管环境间无缝迁移；配套 oo CLI 作为本地 Agent 中继，以及桌面 Agent 应用 Wanta 可直接复用该网关连接 SaaS 服务。
- **适合**：需要让 AI Agent 安全、可持久访问用户第三方 SaaS 账户的开发者和团队，尤其是构建 Agent 产品、自动化工作流或需要自托管认证网关以保留数据控制权的公司。
- **上手**：使用 `docker compose up` 从 `ghcr.io/oomol-lab/open-connector:latest` 镜像启动本地运行时，打开 http://localhost:3000 查看控制台和 API 文档；可先用无需认证的 Action（如 hackernews.get_top_stories）验证运行是否正常，再通过 PUT /api/connections/<provider> 配置凭证（如 GitHub PAT）后调用具体 Action；本地开发可用 Node.js 22+ 运行 `npm install && npm run dev`。

### [truefoundry/trueforge](https://github.com/truefoundry/trueforge) ⭐ 5,783
- **定位**：TrueForge 是一个开源的"agent harness"（智能体运行框架），定位为运行层——把一个 LLM 变成真正能干活的 Agent，负责执行循环中的模型调用、工具接入、沙箱执行、审批和会话状态管理，而不是又一个 Agent 框架/编排库。
- **能做什么**：支持从 YAML 目录一键初始化模型、MCP 工具、Skills 和沙箱配置；兼容 OpenAI、Anthropic、Google Gemini 及任意 OpenAI 兼容端点；支持远程 MCP 服务器（含 Header 鉴权和 OAuth、聊天内授权）；通过 git 管理的 SKILL.md 技能包按需加载；沙箱作为工具按需provision（目前支持 Daytona，密钥留存在 harness 内不下发）；提供工具审批、人工提问、Generative UI 等人工检查点；具备子智能体、延迟工具加载、Code Mode、大结果卸载与上下文压缩等上下文工程能力；对外提供聊天 UI、HTTP API + TypeScript SDK（@truefoundry/trueforge-sdk）以及可嵌入的 UI SDK（@truefoundry/trueforge-ui）。
- **亮点**：可从单进程 + SQLite 的本地模式，平滑扩展到 Postgres + Redis 的多副本托管模式（Docker Compose / Helm / Railway）；项目方在 benchmark 中称在相同任务、工具、模型条件下，相较 Claude Managed Agents 和 deepagents 达到"同等准确率、更低成本"（项目方数据，可在仓库 benchmark/ 目录复现）；MIT 许可，TypeScript 编写，star 数近 5.8k，由 TrueFoundry 团队维护。
- **适合**：需要快速搭建生产级 Agent 运行环境的开发者和团队，尤其是希望复用现成的工具接入、沙箱、审批与会话管理能力、而非从零造轮子的场景；也适合想对比不同 Agent 框架成本与效果的技术团队。
- **上手**：运行 npx @truefoundry/trueforge@latest 即可在本地以单进程 + SQLite 方式体验；生产/团队场景可参考官网 Quickstart 指南，通过 Docker Compose、Helm 或 Railway 部署托管模式（Postgres + Redis）。
- ⚠️ README 明确提示本地模式默认无登录、数据存于本地 SQLite 文件，仅适合个人试用，不应暴露在公网，团队/生产场景需切换到有鉴权的托管模式。

### [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) ⭐ 5,142
- **定位**：CopilotKit 出品的自托管 AI "协作者"平台：每个 Agent（Bot）拥有独立的浏览器、文件和工具权限，所有操作都经过统一网关做事前策略判定、事后完整审计。基于开放协议 AG-UI，可接入任意框架写的 Agent，模型和数据都留在自己的基础设施上。官方定位为"可克隆定制的模板"而非现成产品或托管服务。
- **能做什么**：每个 Bot 独立容器+独立 workspace 卷+独立浏览器 profile，可选 gVisor(runsc) 隔离；统一网关拦截浏览器/文件/Shell/MCP/组件调用，用 CEL 策略引擎判定 allow/deny（deny 优先、策略缺失即拒绝、策略出错即拒绝的 fail-closed 设计）；Activity 面板实时展示屏幕、命令行、读写内容，形成完整审计记录（/admin/audit）；Bot 遇到登录墙或 2FA 时可请求人工"接管方向盘"，接管期间自动拒绝 Bot 动作；凭据 write-only 加密存储，转录中只记录"请求了密钥"而非密钥内容；支持任意说 AG-UI 协议的 endpoint 作为 Bot（LangGraph、Mastra、CrewAI、Pydantic AI、Google ADK 或手写均可）；内置 13 个示例协作者（通用助理、知识库问答、风险分析及 10 个金融场景 Agent，如报销审核、会议纪要转待办、发布说明起草等），可通过 YAML/UI/文件方式自定义；回答以可发布、可授权的 React 组件呈现而非纯文本；MCP 治理内置 Google Drive、Notion，并可通过 Composio 接入数百个第三方工具，逐 Bot 授权。
- **亮点**：核心卖点是"先判定、后执行、全记录"的治理网关，把 Agent 自动化操作真实浏览器/文件/工具这件事变得可控可追溯，而非仅提供聊天界面；协议层用 AG-UI 而非绑定某个 Agent 框架，理论上可平替 LangGraph/CrewAI 等任意后端；项目方明确声明这是"模板"（无托管版本、代码不作为包发布），定位诚实但也意味着需要自行运维和定制；目前处于 Alpha 阶段，功能和接口仍在变动。
- **适合**：需要在自有基础设施上部署、治理AI Agent的企业技术团队、平台/安全工程师，以及正在用LangGraph、Mastra、CrewAI等框架构建Agent、需要统一浏览器/文件/工具执行环境和审计能力的开发者
- **上手**：需 Docker、Bun 1.3+、一个 CopilotKit Intelligence 项目（有免费额度，可自托管）及模型 API Key。步骤：cp .env.example .env → 用 `npx copilotkit login` 和 `project select` 获取 INTELLIGENCE_API_KEY 填入 .env → 填入 OPENAI_API_KEY 等必填项 → `bun install && bash scripts/start.sh` → 打开 http://localhost:3010。也可直接用官方镜像 `ghcr.io/copilotkit/openbot:latest` 通过 docker run 一键部署（应用+API+浏览器+可选内置 PostgreSQL）。
- ⚠️ 核心功能依赖 Bot 用自带登录态的真实浏览器自动化访问网站并完成操作，可能违反目标网站服务条款或触发账号风控/封禁
- ⚠️ 项目自述处于 Alpha 阶段、仍在快速变动，存在较多不稳定和边缘情况
- ⚠️ 运行需要依赖 CopilotKit 的商业化 Intelligence 项目和许可证密钥，并非完全独立自包含的开源方案

## AI 应用产品

### [trycompai/crm](https://github.com/trycompai/crm) ⭐ 10,627
- **定位**：开源的"Agent 优先"CRM：不是在传统 CRM 上加一个聊天框，而是让 AI Agent 作为 CRM 的主要使用者——Agent 独立部署、自主调度、自主研究并记录客户信息，人类查看和把关它的工作成果。
- **能做什么**：基于 eve 框架构建独立部署的 Agent（apps/agent），拥有 18 个自定义工具（如 identify_contact、research_person、enrich_company、record_fact、schedule_recheck 等）和 4 份 Markdown 编写的技能文档；工作队列用 Postgres 行级锁（FOR UPDATE SKIP LOCKED）实现任务分发与租约恢复；提供无网络、无数据库访问权限的沙箱环境执行 bash/grep/glob 等命令；证据分级机制——只有强证据才写入客户记录，弱证据变为待人工确认的建议，工具不允许输出"置信度"；可选集成 Perplexity（网络研究）、Context（公司品牌数据与 LinkedIn 信息）等外部数据源，零 API Key 也可基于已有邮件/会议记录工作；前端 Next.js + shadcn/ui，后端 NestJS + tRPC + Prisma + Postgres，认证用 Better Auth（支持 Google/Microsoft/自有 IdP），单租户架构（不支持多组织）。
- **亮点**：与常见"AI+CRM"产品的核心区别在于角色反转：CRM 是 Agent 记笔记的地方，而非人类操作、AI 辅助；强调"绝不猜测"原则，所有客户事实必须有可观测证据支撑，避免大模型自评置信度导致的错误记录；沙箱刻意采用 deny-all 出站网络且不注入数据库凭证，防止客户邮件等敏感数据通过 shell 命令泄露；每个联系人/公司/交易都有 Agent 标签页展示其决策步骤和被丢弃的线索及原因，可读性和可追溯性较强；GitHub 已获超万星，社区关注度较高。
- **适合**：需要自建/自托管 CRM 且愿意接受 AI Agent 自动化管理客户资料的技术团队、销售运营人员、以及对 Agentic 应用架构感兴趣的开发者
- **上手**：需要 Bun 和 Docker：克隆仓库后复制 .env.example 并配置 BETTER_AUTH_SECRET、ALLOWED_SIGN_IN 及 Google/Microsoft OAuth 凭据（至少配置一种登录方式），执行 bun install、docker compose up -d 启动本地 Postgres，运行 bun run db:deploy 应用迁移、bun run db:seed 生成示例数据，最后 bun run dev 启动，前端在 localhost:3000，API 在 localhost:3001。
- ⚠️ Agent 需要接入 Gmail/Calendar 等真实邮件和日历数据以及 LinkedIn 等第三方信息进行客户研究，自建时需关注邮件内容和个人信息的隐私合规与数据处理边界

### [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) ⭐ 7,525
- **定位**：DSH Desktop 是 DeepSeek Harness（一个 Agent 运行时 + Web UI）的社区桌面客户端，将本地优先、跨平台的 Harness 体验打包成一个可安装的原生应用，开机自启 Harness 并直接打开完整界面。
- **能做什么**：自动启动/停止 Harness 而无需单独 CLI 或浏览器标签；原生系统目录选择器管理项目工作区；支持官方 DeepSeek 模型及主流第三方模型提供商；以 .dshpreset 包形式导入导出完整的自定义 Agent 预设（含冲突检测和信任提示）；内置 PPT 模式，可将素材转为可编辑的 PPTX（16 套模板、192 种版式，预览为英文，输出支持中英文）；应用升级时保留 profile、插件、工作区、会话和模型设置；检测启动/前端插件故障并提供诊断日志与引导式修复；非破坏性 Safe Mode 可临时屏蔽第三方插件；支持手机通过局域网或临时公网隧道（Cloudflare/Pinggy）接续会话；受控的应用更新机制；适配 macOS/Windows 的原生菜单、标题栏与主题。
- **亮点**：本地优先架构：Harness Web UI 仅在随机回环端口提供服务，渲染进程无 Node.js 权限并启用上下文隔离与沙箱，屏蔽 webview 和不受信导航；用户数据存放在系统应用数据目录而非安装目录内，跨版本升级不丢失；提供 Safe Mode 排障和手机远程接续会话等桌面原生能力，是社区插件生态（dsh-market）的配套客户端；macOS 版本经 Apple 签名公证，Windows 版本代码签名。
- **适合**：需要在本地桌面使用 DeepSeek Harness Agent（如日常问答、PPT 生成、插件扩展等）的个人用户和早期尝鲜者，尤其是 macOS/Windows 用户
- **上手**：从官网 dshdesktop.com 下载稳定版安装包（推荐日常使用），或在 GitHub Releases 中选择标记为 Pre-release 的预览版尝鲜；安装后应用会自动启动 Harness 并打开界面；如遇启动或渲染问题，可从 Harness 菜单选择 "Restart as Safe Mode…" 或以命令行传入 --safe-mode 参数进入安全模式排查。
- ⚠️ 当前为基于快速迭代的 @deepseek-ai/dsh@0.1.5-rc.2 的早期预览版本，官方明确不建议普通用户使用预览渠道
- ⚠️ 手机远程访问功能会通过 Cloudflare Quick Tunnel 或 Pinggy 等第三方临时公网隧道暴露本地会话，需注意潜在的数据外泄风险

### [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) ⭐ 7,187
- **定位**：GenOffice 是一款免费开源的 AI 办公套件，作为 Microsoft Office 的替代品，支持在 macOS、Windows、Linux 上原生打开和编辑 .docx、.xlsx、.pptx、PDF、Markdown 和 HTML 文件，并在每个文档旁内置一个可审查的 AI 编辑代理，而非简单的聊天侧栏。
- **能做什么**：1）按字节保真编辑：只重写被修改的部分，文件其余内容原样保留，保证在 Word/Excel/PowerPoint 中仍可正常打开；2）AI 编辑可审查：Docs 生成追踪更改与差异对比、一键回滚，Sheets 生成可用的实时公式而非贴数值，Slides 在画布上生成且可继续编辑；3）本地优先：文件的打开、编辑、保存、格式转换（PDF↔Word/Excel/PowerPoint、Markdown/HTML→Word）均在本机完成，仅 AI 调用请求发往用户选定的模型提供商；4）自带密钥：可登录 Genspark 免配置，也可自带 Claude、OpenAI、Gemini、DeepSeek、Kimi、GLM、Qwen、Doubao、MiniMax、Grok、Mistral、OpenRouter 等或任意 OpenAI 兼容端点（含本地模型服务）的 API Key；5）提供 genoffice CLI 及配套 Agent Skill，支持 Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot、OpenCode、Windsurf 等编码代理无需打开窗口即可创建、转换、读写真实 Office 文件；6）提供 MCP 服务器，将命令封装为 29 个 MCP 工具供 Claude Desktop 等客户端调用。
- **亮点**：开源协议 Apache-2.0，7000+ Star；强调"字节保真"编辑与本地优先处理，仅 AI 请求出网；同时覆盖桌面 GUI 应用、命令行工具和 MCP 服务器三种使用形态，让编码 Agent 能直接产出真实 Office 文件而非 Markdown 近似替代品。
- **适合**：需要 AI 辅助创建/编辑 Office 文档（Word、Excel、PPT）、PDF 或网页的个人和团队用户；使用 Claude Code、Cursor 等编码 Agent 并希望其能直接生成规范 Office 文件的开发者。
- **上手**：从 GitHub Releases 下载 macOS/Windows/Linux 安装包；或安装 CLI 后运行如 `genoffice create --type docx --from notes.md --out notes.docx`、`genoffice convert report.md --to pdf` 等命令；也可通过 `npx skills add genspark-ai/genoffice` 为 Claude Code 等 Agent 安装技能，或运行 `genoffice mcp` 作为 MCP 服务器接入 Claude Desktop 等客户端。

## 本地推理与模型

### [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) ⭐ 8,054
- **定位**：一个用纯 C99 从零实现的 CPU 推理引擎，不依赖 BLAS、深度学习框架或 GPU，号称可在单台机器 8GB 内存内运行 2.78 万亿参数的 Kimi K3（MoE）模型。
- **能做什么**：核心思路是把 1.45TB 的路由专家权重永不常驻内存，而是以打包的 4bit（MXFP4）形式按需从磁盘读取并即时反量化计算；93 层的 dense trunk 被预先打包成单文件，可按选定深度常驻内存、其余部分流式读取；配合 LRU 专家缓存、MLA（用单一潜向量代替 96 个注意力头）和 KDA（内存恒定的线性注意力）两项结构性优化压缩计算与内存开销；底层用 AVX2+FMA 手写 SIMD kernel，仅依赖 libm 和 OpenMP；随包附带对照 PyTorch 参考实现的多级测试门禁（teacher forcing / greedy decode / incremental 三重比对）。
- **亮点**：项目方数据显示：同一份 1.56TB 的 checkpoint，在 8GB 到 224GB 内存预算下均可运行并产生逐字节一致的输出，仅速度不同（8GB 预设约 32.7 秒/token，128GB 预设约 10.7 秒/token）；无需下载任何模型权重，克隆仓库后一分钟内即可用内置 13 层模拟模型跑通全部正确性测试；README 提供了从磁盘 I/O、量化格式、注意力机制到缓存策略的完整实现细节文档。
- **适合**：系统/底层软件工程师、LLM 推理性能优化研究者、希望在消费级硬件上运行超大规模模型的极客与爱好者
- **上手**：git clone 后执行 `make -j` 构建（几秒钟），再 `make test`（一分钟内）即可在无需下载模型、无需联网的情况下验证引擎正确性；若要跑真实推理，需从 HuggingFace 下载 1.56TB 的 Kimi K3 checkpoint（需要约 1.7TB 磁盘空间），用脚本打包 trunk 后通过 `./bin/k3` 加预设（laptop/desktop/workstation/server/max）运行推理。

### [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) ⭐ 6,774
- **定位**：TurboFieldfare 是一个用 Swift + Metal 编写的模型专用推理运行时，让 Gemma 4 26B-A4B（26B 参数、约3.88B 激活参数的 MoE 模型）能在仅 8GB 内存的 Apple Silicon Mac 上运行，运行时占用约 2GB 内存。
- **能做什么**：- 不将完整 14.3GB 模型加载进内存，仅常驻 1.35GB 共享核心和 FP16 KV 缓存，按 token 从 SSD 流式加载所需专家（MoE 路由）
- 权重采用 MLX 4-bit 仿射量化（分组64）、8-bit 路由器
- 提供原生 Mac App、命令行 CLI、实验性 OpenAI 兼容本地服务器（仅回环地址，无远程鉴权/TLS）三种使用方式，共享同一 .gturbo 模型目录
- 流式安装器直接从 Hugging Face 按字节范围拉取并重打包模型，无需在本地保留完整原始 checkpoint
- 支持可选视觉塔（约1.1GB）实现图像输入，需 M2 及以上机型；纯文本推理支持 M1
- CLI/服务器支持工具调用声明，但工具执行需客户端自行完成；不支持音频/视频
- 模型专用而非 MLX 或 llama.cpp 的通用封装，附103项内核、缓存、I/O、预填充、解码相关实测记录
- **亮点**：项目方实测：8GB M2 MacBook Air 上解码速度 5.1-6.3 tok/s，24GB M5 Pro 上 31-35 tok/s（均为项目方数据）。核心卖点是把 26B 参数 MoE 模型的内存占用压到约2GB，使 8GB 内存的入门级 Mac 也能跑得动大模型，这是同类通用推理框架（如 llama.cpp、MLX）难以做到的针对性优化。
- **适合**：拥有 Apple Silicon Mac（尤其是 8GB/16GB 低内存机型）、希望本地运行大参数量 LLM 的开发者和技术爱好者，以及关注端侧 AI 推理优化的工程师。
- **上手**：克隆仓库后执行 `swift build -c release` 编译，运行 `.build/release/TurboFieldfareMac` 启动 Mac App，首次运行选择 Download 下载并重打包约15GB的 Gemma 4 模型，完成后 Load Model 即可在界面输入 Prompt 生成；也可用 TurboFieldfareCLI 命令行方式或启动 TurboFieldfareServer 提供 OpenAI 兼容的本地 API（监听 127.0.0.1:8080）。要求 macOS 26 + Metal 4 + Xcode 26 + Swift 6.2，仅支持 arm64。

## Skills 与写作/设计

### [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) ⭐ 10,595
- **定位**：一个面向 Claude Code、Codex、ChatGPT 等 AI 编程/写作助手的 Skill 插件，用于识别并清除文本中 20 多种典型的"AI 味"表达模式，同时尽量保留作者原有的用词、语气和风格。
- **能做什么**：- 提供 /no-ai-slop 命令，可直接编辑输入文本，去除套路化表达并列出具体修改点
- 提供检测模式 /no-ai-slop is this slop?，只标注命中的套路句式，不判断文本是否由 AI 生成
- 覆盖二元对比句（"It's not X. It's Y."）、故弄玄虚开场白、假深刻结尾、同义词轮换、专家背书式套话等 20+ 种常见 AI 写作模式
- 同时检查基础写作问题：开门见山、主动语态、句子结构、具体细节 vs 空泛表述
- 附带 eval.md 用于自检输出质量，可通过 npx skills add 或复制指令安装到多种 AI 编程/对话工具
- 另有 ChatGPT 插件形式可用
- **亮点**：上线约两个半月即获得超过 1 万 star，说明"去 AI 味"是当前 AI 写作助手用户的普遍痛点；项目以 Skill/Plugin 形式设计，可跨 Claude Code、Codex、ChatGPT 等多个 Agent 平台复用，而非局限于单一工具。
- **适合**：使用 AI 辅助写作或编辑的内容创作者、博客作者、以及在 Claude Code / Codex / ChatGPT 中配置个人写作技能的开发者。
- **上手**：在 ChatGPT、Claude Code、Codex 或其他支持 Skill 的编程 Agent 中输入：Install the /no-ai-slop skill globally from https://github.com/petergyang/no-ai-slop；也可执行 npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes 完成安装，之后用 /no-ai-slop (你的文本) 进行编辑。

### [hypit-ai/hypit](https://github.com/hypit-ai/hypit) ⭐ 10,297
- **定位**：为 Claude Code、Codex 等编程 Agent 提供一套视频创作语言与系统（技能包），可将任意参考视频"克隆"成完整可编辑、可重跑的工作流（画面、字幕、B-roll、特效），也支持从模板或纯文字描述生成视频，生成式模型仅为可选组件。
- **能做什么**：提供 SVML 等 DSL/标记语言，让 Agent 以"词"而非"秒"为锚点组织字幕、镜头切换与特效；克隆参考视频得到的是完整可编辑工作流而非脚本拆解；一份工作流可复用素材批量产出上百个变体（换主播、换钩子、换产品、换语言、换画幅）；组件可插拔，字幕、主持人等模块可独立替换、自建或发布到私有仓库；生成模型可选，纯代码渲染的可视化内容无需调用生成式模型及其费用；内置广告克隆、TikTok Shop 带货视频、AI UGC/数字人口播、播客访谈剪辑、多语言本地化等场景示例。
- **亮点**：项目方未披露具体性能数字；上线约两个月已获 10K+ star、1.2K+ fork，热度增长较快；开源免费，无 Hypit 坐席费、渲染费或水印，模型/生成服务费用按所选服务另计（官方推荐 HypiHub，也可接自有 API 或本地模型）。
- **适合**：使用 Claude Code、Codex 等编程 Agent 的开发者；短视频/UGC/广告内容生产者；需要批量产出视频变体的营销、增长和电商团队
- **上手**：运行 `npx skills add hypit-ai/hypit -g` 将其安装为 Agent 技能；在任意项目目录中用 `/hypit` 指令让 Agent 克隆指定参考视频或按文字描述生成视频，首次使用时 Agent 会自动检查并协助准备 Hypit 可执行文件及所需凭证。
- ⚠️ 内置视频换脸（face swap）功能用于克隆他人视频内容，可能涉及肖像权、深度伪造相关的法律与伦理风险
- ⚠️ 采用自定义的 "Hypit Open Source License"，GitHub 许可证字段标记为 NOASSERTION，非标准开源协议，使用前需自行核实授权条款
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) ⭐ 8,967
- **定位**：面向 Claude Code / Codex 的 Agent Skill，把编程 Agent 变成一个基于 Remotion 的运动设计工作室，用于自动生成电影感的产品宣传、营销、发布或演示视频。
- **能做什么**：提供 157 张镶嵌参数（用途、节奏能量、建议时长、实现细节、常见坑点）的分镜/运动“配方卡”，配套 214 种可搜索预览的运动风格及对应 Remotion（TSX）参考实现；内置一套已验证的完整视频模板“Ink Press”（36.2 秒、1920×1080、30fps、10 个镶头，纸墨琥珀色风格，含 2.5D 真实页面运镜、字幕、转场与完整音效）；覆盖真实页面截图采集、2.5D 运镜、按节奏卡点剪辑、电影级音效设计的全流程方法论；支持将成片导出为剪映（CapCut CN）可编辑项目（已在 macOS 剪映 Pro 11.2 验证）；交付后可用浏览器端“Motion Workbench”（类 CapCut 时间线编辑器）对成片按镶头/转场/字幕/音效轨道二次编辑并用 Remotion 重新渲染，支持从 216 个演示动效库中拖拽素材。同系列还有专注旁白视频的 video-talkcraft 技能。
- **亮点**：GitHub 8967 星、804 fork，采用 Apache-2.0 许可证；配方卡与预览数量持续扩充（从 104 卡增至 152/157 卡，209/214 种预览）；提供在线 Gallery 供浏览、筛选和复制镶头卡名称；剪映导出与 Workbench 渲染号称“像素级一致”（项目方数据）；音效素材来自 Mixkit 免费商用授权；镶头手法参考了 ClickUp、Perplexity、Slack、Notion、Figma、Framer、Bear、Raycast、Pitch、Miro、Superhuman、Loom 等公司官方产品视频的运镜语言（未直接使用其素材本身）。
- **适合**：使用 Claude Code / Codex 等编程 Agent 的产品团队、独立开发者、增长与营销人员，需要快速产出电影感产品宣传视频但缺乏专业运动设计或视频剪辑经验的用户。
- **上手**：在 Claude Code / Codex 中直接对 Agent 说“Install this skill for me: https://github.com/Vincentwei1021/video-shotcraft”，或用 npx skills add Vincentwei1021/video-shotcraft 安装，也可 git clone 后软链接到 ~/.claude/skills/ 或 ~/.codex/skills/ 目录；之后向 Agent 提出类似“Use video-shotcraft to create a promo for my desktop product”的请求即可，可指定具体镶头卡（如 deck-deal-flyin）或直接套用内置 Ink Press 模板。
- ⚠️ Remotion 本身有独立许可证，个人和小团队免费，公司使用可能需要付费授权
- ⚠️ 模板中的产品截图为演示素材，发布前需替换并核实是否需要对产品、客户或个人数据做匿名化处理
- ⚠️ 剪映导出功能仅在 macOS 版剪映 Pro 11.2 上验证，Windows 版未测试

### [jakubkrehel/skills](https://github.com/jakubkrehel/skills) ⭐ 6,898
- **定位**：一套面向 AI Agent（如 Claude Code）的"界面设计技能"集合，通过给 Agent 注入专业的 UI/UX 知识，帮助其在写代码时自动生成更精致的界面，涵盖排版、色彩、布局、无障碍与产品文案等方面。
- **能做什么**：提供多个可独立安装的 Agent Skill：better-ui（同心圆角、视觉对齐、上下文图标、点击区域、动效等）、better-typography（字号阶梯、间距、可变字体、OpenType 特性、换行截断等）、better-colors（调色板生成、语义化色彩令牌、格式转换、对比度检查）、better-accessibility（无障碍规范）、better-layout（分组、对齐、阅读顺序）、better-writing（产品文案打磨）；此外还有综合型技能 better-interface（整合所有 better-* 技能进行统一审查）、interface-review（多维度界面审查报告）、explain-interface（解析网页动画/UI 实现原理）、break（在临时页面中渲染组件的全部状态并做压力测试）、variant（批量生成组件变体辅助迭代）。
- **亮点**：作者是设计工程类杂志 Interfaces 的作者，技能内容来自其个人网站与杂志文章，聚焦"让 AI 写出的界面更专业"这一具体痛点；技能可按需单独调用（如 interface-review、explain-interface 为用户主动触发），也可通过 better-interface 一键组合全部审查项；支持通过 npx 或 Claude Code 插件市场两种方式快速安装。
- **适合**：使用 AI Agent（尤其是 Claude Code）辅助前端/界面开发的设计工程师、前端开发者及产品设计师。
- **上手**：命令行安装：npx skills add jakubkrehel/skills；或在 Claude Code 中通过插件市场安装：/plugin marketplace add jakubkrehel/skills 然后 /plugin install interfaces@interfaces。

### [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) ⭐ 5,547
- **定位**：面向 AI Agent 的数据可视化 Skill，遵循 Agent Skills 规范（SKILL.md 格式），让 Claude Code、Codex、moxt 等兼容 Agent 把用户数据自动转化为有编辑设计感的可交互 HTML 图表或整页报告。
- **能做什么**：提供三种视觉风格——Lupi（编辑叙事型，细线/留白/逐记录，适合论文年报）、Glance（快速判断型，粗柱大数字，适合周报 dashboard）、Basics（保留常见图表轮廓的基础编辑型）；49 个图型覆盖柱状、折线、环形、散点、矩形树图、K 线、网络关系图等；支持 Mono 黑白灰及青瓷蓝、椰林绿、编辑部红三套彩色预设，Agent 可按数据结构自动选色，也支持自定义品牌色；新增 12 套中英双语整页报告模板（调研、年报、财报、dashboard、海报等），可从单图扩展到整页 HTML 报告；实现上 Lupi/Basics 多用原生 SVG，Glance 与部分交互图通过 CDN 加载 Chart.js/ECharts。
- **亮点**：与常规"套模板出图"不同，先判断数据契约再选图型、每张图只承担一个独立结论、把标题旁注来源留白动效都纳入设计语法，用 Lupi/Glance 区分"慢读"与"快读"两种阅读速度；在 moxt.ai 原生工作区中可保留规则模板数据在同一环境持续迭代，也可独立安装到 Claude Code、Codex 等其他 Agent 工具中使用；GitHub 5500+ stars。
- **适合**：需要用 AI Agent 快速产出高质量数据图表或报告的内容创作者、分析师、研究者，以及在 Claude Code / Codex / moxt 等平台上做 Agent 开发和数据可视化自动化的开发者。
- **上手**：一条命令安装：npx skills add https://github.com/larashero3-dotcom/lieflat-charts --skill lieflat-charts；或让有 shell 权限的 Agent 将仓库克隆到 ~/.claude/skills/lieflat-charts（Codex 为 ~/.codex/skills/lieflat-charts），确认 SKILL.md、templates/、catalog.md、mono-tokens.js 等文件存在后即可安装完成；安装后直接向 Agent 提出可视化需求（如“把这份数据做成适合公众号的图表”）即可生成 HTML 结果；也可直接打开 templates/ 下的 HTML 文件预览效果。
- ⚠️ 使用 PolyForm Noncommercial License 1.0.0 非标准许可证，仅允许非商业使用，商业使用需另行获取授权。
- ⚠️ Glance、Circular、Force 等部分图表及报告模板 R11/R12 通过 CDN 加载 Chart.js/ECharts，离线环境无法完整显示。
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) ⭐ 5,332
- **定位**：一个开放格式的 Agent Skill，专门指导 AI 图像模型生成极简、圆润、略带新拟物质感的可爱 IP 吉祥物 Logo，不绑定特定 Agent 产品，可安装到任何兼容该格式的 AI 工具中。
- **能做什么**：- 遵循 Agent Skills 开放格式，通过 `npx skills@latest add` 一键安装到 Codex、Coze、Doubao、YouMind、Manus、Gemini Apps、Replit Agent 等兼容工具
- 规定设计规范：4-7 个基础形状构成的主体轮廓、默认三色配色（两种主体色+一种背景色）、圆润无锐角的粗线条造型
- 主体从画面左下或右下角"涌现"，占画面 85%-95%，默认生成 6 张候选图（3 张左下+3 张右下各方向两变体）
- 优先使用常见动物形象作为吉祥物主体（开放式批次中占 95%-100%），非动物题材需与产品属性直接相关
- 需要顶级图像模型支持（GPT Image 2、Seedance 5.0 Pro、Nano Banana Pro/2 等），不回退到 SVG
- 生成过程不做透明度检测、合规筛选或自动重试，原样保留并交付每次生成结果
- 配套官网 ipaslogo.com 提供免费可商用的现成 Logo 库，供无 AI 工具的用户直接下载
- **亮点**：仓库结构极简，仅含一份 SKILL.md 指令文档和一张展示图，无脚本或额外依赖；上线一周内获得 5000+ star，反映出对"用 AI Skill 标准化控制图像生成风格"这一思路的关注度较高。
- **适合**：使用 Codex、Doubao、Coze 等支持 Agent Skills 格式的 AI 编程/创作工具的开发者、设计师，以及需要快速生成品牌吉祥物 Logo 的产品团队
- **上手**：执行 `npx skills@latest add s1dashu/ip-as-logo-skill`（可加 `--global` 全局安装），安装器会自动识别根目录 SKILL.md 并引导选择兼容的编程 Agent；之后在对话中用自然语言描述吉祥物需求（如"在深藏青色背景上做一个简单可爱的圆润幽灵 IP 形象"），Skill 会自动提出三个设计方向并生成六张候选图。若无相关 Agent 工具，可直接访问 ipaslogo.com 下载现成免费商用 Logo。

## 开发者工具与集成

### [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) ⭐ 16,632
- **定位**：OpenWiki 是一个 CLI 工具，用 Deep Agents 文档 Agent 自动阅读代码库或个人知识源，生成并持续维护一套互相链接的 Markdown Wiki，供 AI Agent 作为记忆读取，也可通过内置可视化工具供人类浏览探索。
- **能做什么**：支持 code（代码仓库）和 personal（个人知识）两种模式；兼容 OpenAI、Anthropic、Bedrock、Gemini 等 13 家模型提供商及 OpenAI 兼容网关；可作为技能/MCP 集成进 IBM Bob、Codex、Claude Code、OpenCode、Cursor、Kiro 等编码 Agent，复用宿主的模型与仓库工具；内置 Notion、Slack、Gmail、X、Web Search、Hacker News、LangSmith、本地 Git 仓库、自定义 MCP 等 9 种连接器；Grounded Claims 机制将文档中的关键事实追溯到带版本的源码证据，证据变化时自动标记需复核的内容；支持通过 GitHub Actions、GitLab CI、Bitbucket Pipelines 定时自动更新并发 PR；输出符合 Open Knowledge Format v0.2 规范、带 Mermaid 图的可移植 Wiki 包；仓库生成采用可续跑的分页任务队列架构，中断后可从检查点恢复。
- **亮点**：核心卖点是"自我维护"：Wiki 会随代码变更自动更新，且用 Grounded Claims 追踪每条事实背后的具体源码证据版本，证据失效时能精确定位哪些结论需要重写或撤回，而不仅仅依赖文件修改时间戳；同时可直接挂载进已有编码 Agent 复用其认证模型，无需额外配置 API Key。
- **适合**：需要为代码仓库或个人知识库自动生成并维护文档的开发者、技术团队，以及使用 Claude Code、Cursor、Codex 等编码 Agent 的用户
- **上手**：安装（需 Node.js ≥22.22.0）：npm install -g openwiki；在仓库根目录运行 openwiki --init 首次生成代码 Wiki（引导选择模型提供商），之后用 openwiki --update 增量更新；个人知识库用 openwiki personal --init；也可运行 openwiki integrations install <bob|codex|claude|opencode|cursor|kiro> 集成到已有编码 Agent 中使用。

### [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) ⭐ 9,452
- **定位**：一个 Codex CLI 的扩展/启动器，通过浏览器自动化把 ChatGPT 网页版（包括 Pro）接入 Codex 的模型选择器，让用户用 ChatGPT 网页额度而非 Codex/API 配额驱动编码任务，并可通过 MCP 让 ChatGPT 调用本地文件、终端等工具。
- **能做什么**：- 用内嵌浏览器（Playwright 驱动）登录 ChatGPT 网页版，在 Codex 原生模型选择器中加入"ChatGPT Web"系列模型
- 按账户权限自动检测可用模型：Free/Go 账户对应 Luna/Think，有推理控制的账户可用 Instant–High，以及 Extra High、Pro（若账户支持）
- 三种运行模式：Browser-only（全自动读取/发送页面消息）、Full harness（通过 MCP 与 OpenAI 官方 tunnel-client，把 ChatGPT 的工具调用接回 Codex 当前任务的文件、终端、工具和审批流程）、Zero Risk（不操作页面，手动粘贴/发送并在启动器中确认）
- 内置浏览器与运行时，无需额外安装 Chrome、Node 或 Bun
- 提供 macOS/Linux/Windows 一键安装脚本，安装前校验发布的 SHA-256 清单
- 支持跨后端子代理（subagents）协议切换（Compatibility V1 / Native），用于兼容 Codex 自身功能设置
- **亮点**：GitHub 星标 9452；项目方宣传可在 Codex 中用 ChatGPT 网页版（含 Pro）的独立额度完成编码任务，从而不占用 Codex 或工作账号的配额，同时保留同一套界面、任务上下文、流式输出和图片能力。
- **适合**：使用 OpenAI Codex CLI 编码、希望复用 ChatGPT Plus/Pro 网页版额度而非消耗 Codex/API 配额的开发者
- **上手**：macOS/Linux 一行命令：curl -fsSL .../install-launcher.sh | sh；Windows 用 PowerShell 的 irm .../install-launcher.ps1 | iex。也可源码运行：git clone 后执行 bun run app（需 Bun 1.4.0），随后在启动器中登录 ChatGPT、安装模型并重启 Codex，选择"ChatGPT Web —…"模型；若需工具调用，在启动器 MCP 页完成 Full harness 设置。
- ⚠️ 这是非官方的浏览器自动化方案，并非 OpenAI 官方 API，依赖模拟登录态操作 ChatGPT 网页，README 明确提示 ChatGPT 页面 UI 变动会导致失效，且使用方式可能触及 OpenAI 服务条款边界，存在账号风险
- ⚠️ 浏览器登录状态属于敏感凭据，本地回环监听可被同一用户下的其他进程访问，官方建议只在可信设备上使用、不要共享启动器画像
- ⚠️ 发布的安装包尚未做平台签名，安装/运行时会触发 macOS Gatekeeper 或 Windows SmartScreen 的安全警告

### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) ⭐ 5,443
- **定位**：由腾讯开源的浏览器自动化工具，通过 CLI（bsk）+ 浏览器扩展，让 Cursor、Claude Code、Codex 等任意可调用 Shell 的 AI Agent 复用用户本机已登录的真实浏览器，而不打断用户日常使用。
- **能做什么**：核心机制是「借用标签页」：Agent 需显式借用某个标签页、任务完成后归还，不干扰浏览器其余部分；浏览任务在独立可见的 Agent Window 中运行，用户可继续正常使用自己的浏览器；内置人机协作机制，遇到验证码、登录、确认弹窗等需要人工介入的步骤时可请求用户接管；支持整页截图（bsk screenshot --full-page）；提供技能文件（SKILL.md）一键安装到各类 Agent Harness，兼容 macOS（Apple Silicon/Intel）、Linux（x64/ARM64）、Windows x64，浏览器支持 Chrome 和 Edge（其他基于 Chromium 的浏览器预期可用，Firefox 计划支持中）。
- **亮点**：不依赖为 Agent 单独准备测试账号，直接复用已登录状态访问网站；不锁定特定模型或 Agent 框架，任何能调用 Shell 的 Agent 均可通过 bsk CLI 接入；自动化设置（借用前确认、允许求助）两项开关默认开启，用户设置对所有会话具有最高优先级；协议版本兼容 1.0–1.2，支持渐进式升级。
- **适合**：使用 Cursor、Claude Code、Codex 等 AI 编程/自动化 Agent、需要 Agent 操作已登录网站（如后台管理、内部系统）但又不想打断自己浏览器使用的开发者。
- **上手**：通过 install.sh（macOS/Linux）或 install.ps1（Windows）安装 bsk CLI；从 Chrome Web Store 或 Edge Add-ons 安装 BrowserSkill 浏览器扩展；运行 bsk install-skill 将技能安装到所用 Agent Harness；运行 bsk doctor 检查连接状态，即可在 Agent 会话中发出如 /browser-skill open example.com 的指令进行验证；也可直接把安装说明链接发给 Agent 让其自动完成安装。
- ⚠️ 该工具允许 AI Agent 操作用户已登录状态的真实浏览器标签页（包括第三方网站账号），若被用于自动执行网站禁止的自动化操作，可能违反相关网站服务条款或存在账号风险。

## 安全相关

### [MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct) ⭐ 8,495
- **定位**：面向 Codex（GPT 系列）的"破甲"（越狱）系统提示词与配套回归测试工具链，通过自定义 model_instructions_file 改变模型的默认行为约束，重点优化复杂任务的首轮执行、过程连续性、工件验证与可回滚部署。
- **能做什么**：维护两条并行产品线：稳定生产版 gpt-5.6-sol-v45 与新线 gpt-6-astra-v1；提供 Python 脚本一键部署/预览/回滚系统提示词到 Codex 配置，支持自定义 ZIP/Markdown 部署；配套 A/B/C 三级发布门禁测试体系（3 用例快速验证→66 用例/74 轮回归→120 用例全量测试），并附带测试脚本、评分校验与失败归因文档。
- **亮点**：项目方数据：gpt-6-astra-v1 在 A 级门禁 3/4 通过，全量 B 级回归 52/66 cases、60/74 turns、15/16 工件门通过；每个候选提示词限制在 8000 UTF-8 字节内；采用严格的版本命名与历史归档规范（每 epoch 最多 20 个版本），要求所有修改型候选具备修改记录、diff 与可运行回滚方案。
- **适合**：对 AI 模型安全机制感兴趣的研究者/测试者，以及需要绕开 Codex/GPT 默认限制以完成复杂任务的高级用户
- **上手**：克隆仓库后运行 `python3 codex-instruct.py --apply --version gpt-5.6-v45 --dry-run` 预览部署，去掉 `--dry-run` 正式部署稳定版；部署新版用 `--version gpt-6-v1`；`--reset` 可仅恢复本项目管理的提示词配置项，不影响其他 Codex 设置。
- ⚠️ 该项目本质是绕过 GPT/Codex 模型的默认安全限制（越狱提示词），存在被滥用于生成违规内容的风险；README 明确提示"从事破甲活动、使用自定义模型指令存在账号风险，建议在日抛账号上使用"，说明使用者可能面临账号被封禁的后果。

### [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) ⭐ 6,188
- **定位**：多智能体自动化红队/进攻性安全框架，把用户本地已登录的 AI 编程 Agent（Claude Code、Codex 等）或本地离线模型变成执行"侦察→利用→出报告"全流程渗透测试的"武器库"。
- **能做什么**：不需要单独申请 API key，直接复用本地已在运行的 AI 编程 Agent（Claude Code / Codex / Hermes / OpenCode / Oh My Pi）作为决策大脑，也可指向 Ollama / LM Studio / vLLM 等完全离线的本地模型；提供浏览器 War Room 界面和 CLI 两种操作方式；覆盖 Web 应用黑盒渗透（XBEN 套件）、CTF 无提示解题（Cybench）、机器人/OT/嵌入式 OSS 漏洞协调披露、白盒代码审计（web-tree-sitter 多语言解析）、智能合约漏洞复现（Damn Vulnerable DeFi）、云 IaC 误配置检测、移动端静态分析、二进制/逆向 sink 检测等多个领域，README 中逐项标注各功能的成熟度（稳定/实验性/路线图）；内置 `npm run verify-claims` 命令，可从仓库提交的基准数据一键复现所有宣称的性能数字；支持 Docker 部署，默认仅绑定 127.0.0.1，不对外网暴露。
- **亮点**：项目方数据称在 XBOW 官方 104 题挑战套件上 pass@1 达到 90.1%，高于 XBOW 自报的 85%，同时给出了无提示 CTF 解题记录和针对模型训练截止后新披露 CVE 的"冷猎"验证结果；强调所有基准数字可通过一条命令从提交数据复现（27/27 通过），并在文档中明确区分哪些能力已稳定、哪些仍是实验性脚手架，避免夸大宣传。
- **适合**：授权渗透测试人员、安全研究者、CTF 参赛者，以及希望用 AI Agent 辅助漏洞挖掘的开发者
- **上手**：克隆仓库后执行 `npm install` 与 `npm run server` 启动 War Room（http://127.0.0.1:3333/ui/），在 Settings 中连接本地 AI 编程 Agent 即可用自然语言向 Op Admiral 描述目标并发起任务；也可设置 OPENROUTER_API_KEY / ANTHROPIC_API_KEY 等云端 key，或通过 `ollama serve` 加 `npx tempest` 完全离线运行；执行 `npm run verify-claims` 可复现 README 中的所有基准数字；也提供 `docker compose up -d` 的容器化部署方式。
- ⚠️ 这是一款明确定位为进攻性安全的工具，README 反复强调仅限对拥有明确书面授权的目标使用，未经授权访问计算机系统或网络在多数司法辖区属违法行为，使用者需自行承担合规责任。
- ⚠️ 采用 AGPL-3.0 许可证，具有较强的著佐权传染性，基于其构建的衍生服务需注意开源披露义务。
