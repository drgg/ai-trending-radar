# GitHub 近 90 天 AI 热门项目（Stars > 5000）

- 数据快照：2026-10-05　共 33 个项目

## 本期变化
对比 2026-09-30：
- 新上榜：lexmount/moli、KKKKhazix/AIHOT、ApodexAI/FrontierAgent
- 移出：trailhq/Graft、elder-plinius/T3MP3ST、aipoch/open-science
- 涨幅榜：hypit-ai/hypit +1329、dataelement/dsh-desktop +810、TencentCloud/Octop +740、browser-use/jev-ultrafast +467、miuuyy/codex-chatgpt-web +452

## 趋势小结
- Agent基础设施类项目大量涌现，覆盖运行时、操作系统与协作平台：qm、aos-ce、reef。
- Claude/Codex技能包（Skills）生态持续走热，垂直场景不断细分：watermarks-remover、no-ai-slop、skills。
- 本地极致压缩推理成热点，普通硬件即可跑起千亿级大模型：kimi-k3-in-c、turbo-fieldfare。
- ChatGPT网页版与Codex互补桥接工具涌现，既省配额又能协同规划：codex-chatgpt-web、codex-with-chatgpt。
- 终端编程Agent赛道竞争升温，大厂与社区项目同台竞技：grok-build、ZCode、FrontierAgent。

## 编程 Agent 与运行框架

### [xai-org/grok-build](https://github.com/xai-org/grok-build) ⭐ 27,226

> xAI 推出的终端 AI 编程 Agent，全屏 TUI，可编辑代码、执行命令、搜索网页。

- **定位**：grok 是 xAI（SpaceXAI）推出的终端 AI 编程 Agent，以全屏 TUI 运行，理解代码库并执行文件编辑、命令、网页搜索等任务，支持交互模式、无头脚本/CI 及通过 ACP 的编辑器集成。
- **能做什么**：
  - 理解代码库并自动编辑文件
  - 执行 shell 命令、搜索网页
  - 管理长时间运行的任务
  - 支持交互式全屏 TUI、无头脚本/CI 模式
  - 可通过 Agent Client Protocol（ACP）嵌入编辑器
- **亮点**：
  - 由 xAI（SpaceXAI）官方开发并维护，代码定期从内部 monorepo 同步
  - README 未给出具体性能或基准数字
- **适合**：需要终端 AI 编程助手的开发者，尤其是希望在 CLI、CI 或编辑器中集成编码 Agent 的 Grok 用户
- **上手**：`curl -fsSL https://x.ai/cli/install.sh | bash` 适用于 macOS/Linux；Windows 用 PowerShell 命令安装。首次启动 grok 会打开浏览器完成身份验证。

### [zai-org/ZCode](https://github.com/zai-org/ZCode) ⭐ 7,412

> Z.ai 出品的编程 Agent 工作台，提供桌面、Web 与终端三种界面

- **定位**：ZCode 是 AI 编程工作台，整合桌面应用、浏览器界面和终端 Agent，仓库包含客户端、后端服务、共享 UI 以及 Agent CLI 与运行时源码。
- **能做什么**：
  - 提供桌面应用（Electron）、Web 界面和终端 TUI/CLI 三种使用形态，共用同一后端服务
  - 命令行发行包统一用 zcode 命令启动，无参数进入 TUI，加 --web 启动网页界面
  - 可选支持 SSH/WSL 远程开发，本地构建资源通过 SFTP 上传，不经 CDN
  - Web 服务默认只监听 127.0.0.1，局域网访问需显式开启 --host 0.0.0.0
  - 可通过环境变量自定义数据目录、后端工作区路径及内置 Provider 配置文件
- **亮点**：
  - 仓库同时开源客户端、后端服务、共享 UI 与 Agent CLI/运行时完整源码，采用 Apache-2.0 许可
  - README 标注已更新至 ZCode v3.14.3 版本（项目方数据）
- **适合**：需要本地部署或自定义编程 Agent 工作台的开发者和团队
- **上手**：`pnpm bootstrap` 安装 workspace 依赖并准备桌面本地运行资源，随后可用 pnpm dev:desktop 启动开发环境

### [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) ⭐ 7,392

> Claude Code插件，用外部模型逐条打分决定去留，替代摘要式上下文压缩

- **定位**：Claude Code 触发上下文压缩时，用名为Jev的外部模型逐条给工具调用和结果打分，决定保留、截断或删除，替代默认的LLM摘要压缩方式。
- **能做什么**：
  - 对每条工具调用和结果打分，决定保留、截断前300字符或整条删除
  - 保留内容均为原文，不做摘要式改写，用户与助手文本始终完整
  - 问题超出单次请求token上限时自动分批并发请求，再合并结果
  - 可作为Claude Code插件直接替换内置compaction，也可作npm库单独调用
  - 压缩失败或减幅不足时自动回退到Claude Code内置摘要
- **亮点**：
  - 用逐条保留概率代替摘要改写，声称可避免文件路径、报错等细节在压缩中丢失（项目方说法）
  - 完整对话状态会随每批请求重复发送给打分服务，接近状态上限时单次压缩需多次请求（项目方文档）
- **适合**：使用 Claude Code 处理长会话、希望上下文压缩保留原文细节而非摘要的开发者
- **上手**：`claude plugin marketplace add tamaratran/fast-jev-compaction` 需先在settings.json开启CLAUDE_CODE_ENABLE_FUNCTION_HOOKS并配置TYPESAFE_API_KEY，再执行plugin install完…
- ⚠️ 会将对话中的工具调用、输入参数和文本内容发送给第三方TypeSafe API用于打分，存在隐私或代码泄露风险。

### [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) ⭐ 5,104

> 开源终端智能体运行时，提供 ReAct 单智能体与 Agent Team 多智能体两种工作模式

- **定位**：面向长周期研究和文件类任务的开源智能体运行时，内置终端 TUI，提供 ReAct 单智能体与 Agent Team 多智能体两种工作流，同一引擎也用于 Apodex 模型的评测基准。
- **能做什么**：
  - ReAct 模式：单个有状态智能体在任务沙箱内研究、读写文件、执行命令并迭代
  - Agent Team 模式：协调器维护任务看板，调度并行子智能体并汇总报告合成结果
  - 任务沙箱分 /inputs 只读、/workspace 可写、/outputs 产出，校验失败默认拒绝
  - 支持运行中插话：输入新指令会在安全节点注入，不打断正在执行的任务
  - 写操作默认需审批确认，会话带检查点与本地追踪，支持 /revert 回滚和 --resume 续跑
- **亮点**：
  - 同一工作流引擎既驱动终端 TUI 产品，也用于跑 FrontierSearchBench/FrontierChallenge 等内置评测基…
  - macOS/Linux 一条命令即可安装运行，无需预装环境，Docker 为可选而非必需依赖
- **适合**：需要终端智能体处理长周期研究、文件分析或多智能体协作任务的开发者与研究者
- **上手**：`uv run frontier-agent --mode react --cwd /path/to/project` 需先 git clone 仓库、执行 uv sync 安装依赖，并在 .env 中配置 OpenAI 兼容模型端点

## Agent 平台与基础设施

### [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) ⭐ 22,014

> 用动态索引动作空间驱动浏览器执行单一自然语言目标的实验性网页Agent

- **定位**：browser-use团队发布的实验性网页Agent，用动态索引动作空间（而非截图或固定脚本）驱动浏览器完成单一自然语言目标，定位为可读性强的MVP示例而非通用生产工具
- **能做什么**：
  - 每次观察生成带编号的元素表，模型从CLICK/TYPE_TEXT/SELECT等有限操作中选择
  - 操作与目标预测合并为一次网络请求，仅TYPE_TEXT操作时才调用小模型生成文本
  - 默认不依赖截图，用结构化DOM快照驱动决策，截图仅用于本地调试界面
  - 执行前校验目标元素的页面新鲜度与是否被遮挡，拒绝对失效元素操作
  - 提供Python库调用方式（Agent类）和本地可视化调试页面（demo inspector）
- **亮点**：
  - 项目方数据：Google Flights单程航班查询任务7.1秒完成（含模型调用、生成文本、浏览器操作和等待）
  - 项目方数据：3/3通过，耗时中位数9.45→7.09秒，协议调用1092→101次；仅单任务测试，非通用基准
- **适合**：需要快速浏览器自动化/网页Agent方案的开发者，尤其是browser-use生态用户及关注Agent执行效率的工程师
- **上手**：`uv run jev` 先执行git clone、uv sync并在.env中配置TYPESAFE_API_KEY和TEXT_MODEL_API_KEY，再运行此命令打开本地调试页面
- ⚠️ 核心功能是自动化操作Google Flights、Wikipedia等第三方网页完成任务，可能违反对方服务条款，存在账号风险

### [yc-software/qm](https://github.com/yc-software/qm) ⭐ 15,337

> 面向团队的多人协作 Agent 工作平台，支持 Slack 与网页端

- **定位**：为初创公司设计的多人协作 Agent 系统，部署在自有云账户、使用自有模型和密钥，员工拥有独立工作区并可在频道中共同使用 Agent。
- **能做什么**：
  - 个人与共享作用域并存，可在 Slack 频道、群组、项目中协作
  - Slack 与网页端共享同一身份和配置
  - 支持 Pi、OpenCode、Codex、Claude Code 等多种 harness 和模型切换
  - 可创建内部 Web 应用并按权限发布给指定人员
  - 支持定时任务、监控和入站 webhook 等后台运行能力
- **亮点**：
  - 安全策略分 Strict（逐步需人工审批）、Auto（默认，阻断私网访问）、Dangerous 三档，可选内容审查功能
  - 共享策略默认 Isolated，资源默认不跨作用域共享，可选 Open 模式按授权共享
- **适合**：需要为团队搭建内部协作型 AI Agent 系统的初创公司技术团队或运维人员
- **上手**：`npm exec --yes --package=@yc-software/qm@latest -- qm init . --org <slug> --target <fly-or-aws>` 需先创建组织自有的部署仓库依赖 @yc-software/qm，init 后按引导完成基础设施、登录和连接器配置，部署在自己的云账户中

### [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) ⭐ 11,905

> 本地优先的跨平台桌面应用，封装 DeepSeek Harness 的 Agent 运行时与 Web 界面

- **定位**：将本地运行的 DeepSeek Harness 打包为安装版桌面应用，自动启动运行时，在本地就绪后打开完整 Harness 界面，用户数据保存在应用目录之外。
- **能做什么**：
  - 自动启动和停止 Harness，无需单独 CLI 或浏览器标签页
  - 支持官方 DeepSeek 模型及主流第三方模型提供商
  - 内置 PPT 模式，可将素材转为可编辑 PPTX（项目方称含16模板192布局）
  - 支持导入导出 .dshpreset 格式的完整自定义 Agent 预设包
  - 提供 Safe Mode 临时屏蔽第三方插件，并给出故障诊断与恢复指引
- **亮点**：
  - 基于快速演进中的 @deepseek-ai/dsh@0.2.0-rc.2 构建，项目方称为早期预览版
  - macOS 版经 Apple 签名并公证，Windows x64 安装包已代码签名
  - 内置离线 DOCX/PPTX/XLSX 技能，macOS 和 Windows 自带所需 Python 库
- **适合**：需要在本地运行 DeepSeek Harness、管理 Agent 插件与多工作区的 macOS 或 Windows 用户
- ⚠️ 可选的手机远程访问功能通过 Cloudflare Quick Tunnel 或 Pinggy 等第三方隧道转发本地数据

### [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) ⭐ 8,461

> 面向智能体的开源操作系统，提供CLI、HTTP API与能力胶囊体系

- **定位**：AOS Community Edition 是面向智能体的操作系统社区版，拥有 aos CLI、HTTP API、发行版、22个官方胶囊及审计体系，用于构建可组合、可审计的智能体环境。
- **能做什么**：
  - 提供 aos CLI 统一管理 init、status、update、mcp、daemon 等核心命令
  - 内置22个官方胶囊(capsule)，构成用户可组合的能力单元
  - 支持 MCP 协议，兼容 Codex、Claude、Grok 等客户端的审批流程
  - 提供 Forge 工具链，辅助智能体识别能力缺口并构建最小权限胶囊
  - 发布版本附带校验和、Sigstore签名与GitHub构建溯源证明
- **亮点**：
  - 每次发行均提供校验和、Sigstore签名与GitHub构建溯源证明，发布前需同时通过运行时兼容性与自愈校验
  - MCP本地审批桥仅接受固定布尔值或AOS审批枚举，不收集任意字符串、密码或URL
- **适合**：需要可审计、可组合智能体运行环境的开发者，以及构建智能体工具链和胶囊生态的团队
- **上手**：`curl --proto '=https' --tlsv1.2 -fsSL https://aos.unicity.ai/install.sh | sh` 安装脚本执行后需再运行 aos init 完成22个官方胶囊初始化，整个过程约需等待2分钟（限速批次）
- ⚠️ fork/star 比例异常（23/8461），热度可能有水分

### [deeplethe/utopia](https://github.com/deeplethe/utopia) ⭐ 8,072

> 开源企业级"世界模型"，基于双时态知识图谱的自治知识库系统

- **定位**：DeepLethe开源的企业知识管理系统，用双时态知识图谱记录知识随时间演化的全过程，结合本体推理与冲突检测，支持离线自部署，作为Agent可信赖的决策基座与审计轨迹。
- **能做什么**：
  - 支持PDF、Word、Excel等多格式摄取，可同步网页、GitHub等数据源
  - 全文检索与向量检索融合排序，回答附带可追溯的引用来源
  - 内置Agent可对话式查询知识图谱，支持MCP协议供外部Agent接入
  - 本体驱动的实体消歧、冲突检测，支持可选的正向链式推理
  - 决策台账记录每次确认、合并、回滚操作，且不可篡改
- **亮点**：
  - 双时态知识图谱同时记录事实的有效时间与系统发现时间，修正时保留历史版本而非覆盖
  - 单一Rust二进制加Postgres即可运行，无需额外组件，支持离线自部署
  - 配套方法Ontology2SQL在BIRD Mini-Dev基准上表现突出（项目方数据）
- **适合**：需要知识图谱、RAG与审计追溯能力的企业技术团队、法务合规人员，以及接入MCP开发Agent的工程师
- **上手**：`docker compose --profile app up -d` 先clone仓库并进入目录，再执行该命令，访问 http://localhost:1516 注册，首个账号自动成为管理员。

### [lexmount/moli](https://github.com/lexmount/moli) ⭐ 7,915

> 面向 AI Agent 的轻量无头浏览器，按需渲染，资源占用低，用 Rust 编写

- **定位**：Moli 是用 Rust 自研的生产级无头浏览器内核，非 Chromium 封装，默认只读取 DOM/样式状态，仅在截图等场景按需触发布局与绘制，供 AI Agent 抓取网页、搜索和执行浏览器自动化任务。
- **能做什么**：
  - 支持 CLI、CDP、WebDriver Classic、WebDriver BiDi 四种接口，Playwright 可直接通过 CDP…
  - 默认只读 DOM/样式不触发布局绘制，加 --layout 可选开启真实布局、坐标输入与截图
  - 可选 --resource、--image、--font 等参数按需加载图片、字体、音视频资源
  - CLI 可直接输出 HTML、Markdown、JSON、语义树等格式，适合抓取与检索场景
  - 基于 html5ever、V8、Servo/Stylo、Taffy+Parley 等组件自研内核，不依赖 Chromium
- **亮点**：
  - 项目方数据：192个公开网页抓取测试中，Moli成功率53.6%、内存占用73MiB，内存远低于Chrome Headless的773MiB
  - 项目方数据：Lexbench 1308项任务测试中，Moli 0.1.1通过率81.88%，低于作为参照的Chrome的99.85%
  - 项目方数据：同一任务集下，Moli中位CPU时间与峰值内存约为Chrome的15%和13%
- **适合**：需要网页抓取、构建爬虫或 Agent 浏览自动化的开发者，尤其是对资源占用和启动速度敏感的场景
- **上手**：`curl --proto '=https' --tlsv1.2 -fsSL https://github.com/lexmount/moli/releases/latest/download/moli-installer.sh | sh` Linux/macOS 下载并安装预编译二进制；Windows 需在 PowerShell 中运行对应的 .ps1 安装脚本

### [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) ⭐ 7,486

> 开源的持续自我改进 Agent 基础设施，衔接推理、反馈、训练与版本发布

- **定位**：Reef 是开源的持续自我改进 Agent 基础设施，连接 Agent 推理、反馈收集、训练与版本化发布，支持训练模型权重或优化 Agent 的提示词、规则与技能（Harness）。
- **能做什么**：
  - 提供 OpenAI/Anthropic 兼容的推理接口，接收请求并记录交互供反馈匹配
  - 支持两种学习路径：用 Slime、SGLang 训练模型权重，或优化 Agent harness（提示词、规则、技能）
  - 按 Serve-Observe-Grow-Commit 四步处理反馈并发布更新
  - 内置 Reefine，仅用模型 API 即可优化编码 harness，无需本地训练 GPU
  - 支持版本管理与热更新，服务不中断即可切换到新版本
- **亮点**：
  - 项目方称其为首个开源的持续自我改进 Agent 基础设施（项目方说法）
  - 同时覆盖模型权重训练与 Agent harness 优化两条自我改进路径，并提供多个任务示例配方
- **适合**：需要为 Agent 构建持续学习或自我改进系统的研究者和工程团队，熟悉强化学习训练框架或 Agent harness 开发
- **上手**：`uv pip install reef-infra` 需先用 uv 创建并激活虚拟环境；若需版本/检查点功能还要系统安装 git-lfs。
- ⚠️ Reefine 默认在本地无鉴权启动（需手动设 REEF_TOKEN 才要求认证），其编码会话默认不在沙箱中运行命令，README 提醒需自行隔离安装目录与运行环境。

### [TencentCloud/Octop](https://github.com/TencentCloud/Octop) ⭐ 6,789

> 腾讯云出品的自托管多用户多智能体 AI 助手

- **定位**：Octop 是腾讯云开源的自托管 AI 助手平台，面向家庭和小团队，单进程运行网页控制台、CLI、IM 接入与定时任务，数据和凭证全部留在本机。
- **能做什么**：
  - 多用户专家团队：按场景切换专家，支持专家库、专家市场与团队内专家共享
  - 支持飞书、钉钉、QQ、微信、Telegram、Discord、企业微信等多种 IM 渠道接入
  - 内置知识库（RAG）与插件系统，支持 OAuth/MCP 的 Connector 扩展
  - 支持 ACP 协议双向集成，可委托 OpenCode、Claude Code 等编码代理处理任务
  - 提供浏览器自动化（Browser AI+）与远程桌面功能，用于网页任务和桌面操作
- **亮点**：
  - 安全机制内置：JWT 多用户隔离、工具调用审批、Shell 命令防护与 PII 脱敏
  - 控制面数据库默认 SQLite，可选 PostgreSQL；所有数据保存在本机 ~/.octop/ 目录下
- **适合**：希望搭建私有、数据留在本地的多智能体 AI 助手的家庭用户、小团队与开发者。
- **上手**：`curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash` macOS/Linux 一键安装脚本，使用 uv 自动配置 Python 3.12 环境，安装后需重新加载终端。
- ⚠️ 内置浏览器自动化（Browser AI+）和远程桌面控制功能，用于操作网页和桌面时可能涉及第三方服务条款风险。

### [truefoundry/trueforge](https://github.com/truefoundry/trueforge) ⭐ 6,064

> 开源agent harness，为LLM提供执行循环、沙箱、审批等运行时能力

- **定位**：TrueForge是开源的agent harness（运行时层），负责模型调用、MCP工具、技能、沙箱、审批和会话状态管理，并通过对话UI、HTTP API/SDK和可嵌入UI SDK三种方式对外提供能力。
- **能做什么**：
  - 支持OpenAI、Anthropic、Google Gemini等模型提供商，或兼容OpenAI接口的任意端点
  - 支持远程MCP工具服务器，含header认证或OAuth，可在对话中完成授权
  - 基于git的SKILL.md技能包，按需加载到沙箱中执行
  - 沙箱作为工具：隔离代码/文件执行（目前支持Daytona），按需创建，密钥留存在harness内
  - 人工检查点：工具调用审批、向用户提问、对话内生成式UI
- **亮点**：
  - 项目方数据：相同任务、工具和模型下，与Claude Managed Agents、deepagents相比准确率相当但成本更低
  - 支持本地模式（单进程+SQLite）和托管模式（Postgres+Redis，可用Docker Compose/Helm/Railway部…
- **适合**：需要为LLM构建生产级运行环境的开发者和团队，关注会话持久化、工具审批与沙箱执行等场景。
- **上手**：`npx @truefoundry/trueforge@latest` 本地模式为单进程+SQLite，仅限本机试用；团队或生产环境需用Docker Compose、Helm或Railway的托管模式。
- ⚠️ 本地模式默认无登录认证，README明确警告仅限本机使用，不可直接暴露到公网作为生产部署

### [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) ⭐ 6,042

> 开源AI协作者平台，为每个Agent分配独立电脑并记录全部操作

- **定位**：自托管的AG-UI Agent治理平台，可接入任意框架构建的Agent，为每个"Bot"提供独立浏览器、文件和工具，所有操作需预先审批并留痕记录。
- **能做什么**：
  - 基于AG-UI协议，兼容LangGraph、CrewAI等任意Agent框架
  - 每个Bot拥有独立浏览器、文件系统和受限工具权限
  - 网关统一管控浏览器、文件、MCP和组件操作，执行前决策、执行后记录
  - 示例包含13个预置协作者，可通过配置文件或界面创建新协作者
  - 支持Slack、Teams、短信等渠道继续对话，并提供审批、边界策略等管理界面
- **亮点**：
  - README称项目是"模板而非产品"，需克隆后自行定制，不提供托管版本
  - 项目处于Alpha阶段，仍在积极开发中
- **适合**：需要在自有基础设施中部署可审计、可控AI Agent系统的企业技术团队
- **上手**：`cp .env.example .env && bun install` 需配置CopilotKit Intelligence密钥和模型Key后，执行bash scripts/start.sh启动服务
- ⚠️ 核心功能是让Agent使用自带登录态的浏览器自动化操作第三方网站，可能涉及违反目标网站服务条款的风险
- ⚠️ 默认.env.example开启OPENBOT_SINGLE_USER=true，将所有请求视为管理员身份，需手动开启登录后才能对外部署

## AI 应用产品

### [trycompai/crm](https://github.com/trycompai/crm) ⭐ 11,063

> 开源 agent 原生 CRM，AI agent 自主调研并记录客户信息，而非聊天侧边栏

- **定位**：为 AI agent 设计的开源 CRM：agent 独立部署运行，自主决定调研对象、记录证据、安排跟进，而非作为聊天框功能附加在传统 CRM 表单上。
- **能做什么**：
  - 18 个工具 4 个技能 1 个调度，agent 自主建队列决定下一步调研哪个联系人
  - 证据分级记录事实：强证据写入记录，弱证据只生成人工确认的建议，不接受自评置信度
  - 沙盒执行 shell 命令默认禁止出网且不接触数据库，防止客户信息经此泄露
  - 无需任何 API Key 即可运行，读取自身邮件和会议记录作为免费可靠的证据来源
  - 可选接入 Perplexity 做网络调研，接入 Context 获取 LinkedIn 资料和公司品牌数据
- **亮点**：
  - Agent 作为独立部署持续运行，关闭浏览器后仍按自身调度继续工作，非请求-响应式交互
  - UI 提供 Agent 标签页可查看调研步骤和决策过程，需配置 AGENT_BRIDGE_SECRET 才启用
- **适合**：需要 AI 自动调研、补全客户资料的销售/增长团队，以及希望自托管、具备工程能力的技术团队
- **上手**：`git clone https://github.com/trycompai/crm.git && cd crm` 需 Bun 和 Docker，克隆后配置 .env、docker compose 启动 Postgres、执行迁移后运行 bun run dev
- ⚠️ agent 的 research_person、enrich_company 等工具会调用第三方服务（如 LinkedIn 数据）调研联系人个人信息，涉及第三方隐私数据采集合规问题

### [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) ⭐ 8,634

> 开源免费的AI办公套件，本地编辑Word/Excel/PPT/PDF并内置AI代理

- **定位**：开源免费的本地优先Office替代品，原生读写.docx/.xlsx/.pptx并编辑PDF/Markdown/HTML，内置可审查的AI代理，提供CLI和Skill供Claude Code、Codex、Cursor等编程Agent创建与编辑真实办公文件。
- **能做什么**：
  - 原生读写.docx/.xlsx/.pptx，并编辑PDF/Markdown/HTML，未修改部分按字节保留
  - AI编辑以追踪变更和diff呈现，支持一键回滚；表格生成实时公式而非粘贴数值
  - 本机完成PDF转Word/Excel/PPT等格式转换，仅AI请求发送至所选模型服务商
  - 可登录Genspark免配置使用，或自带Claude/OpenAI/Gemini等多家模型密钥，含本地OpenAI兼容端点
  - 提供genoffice命令行、Agent Skill和MCP服务器，供Claude Code、Codex、Cursor等Agent创建编辑…
- **亮点**：
  - 本地SQLite全文搜索支持中日韩分词，可选开启TypeSafe Jev模型对前20条结果重新排序（项目方描述，默认关闭）
  - MCP服务器提供29个工具（项目方数据），Claude Desktop等客户端可直接调用在可见编辑器中生成文档
- **适合**：需要AI辅助处理Word/Excel/PPT/PDF文档，或希望让Claude Code、Cursor等编程Agent直接生成真实办公文件的个人与团队
- **上手**：`npx skills add genspark-ai/genoffice` 该命令将GenOffice的Agent Skill安装进支持Skill的编程Agent；配合随桌面应用安装的genoffice命令行使用。

### [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) ⭐ 7,346

> 读手机屏幕聊天内容，AI判断对方意图并生成回复候选，发送仍由你手动确认

- **定位**：面向普通用户的手机聊天回复辅助工具，通过无障碍服务读取QQ、X、飞书等App聊天界面内容，调用用户自配置的大模型判断对方意图并生成候选回复，由用户手动决定是否发送，不修改App本身。
- **能做什么**：
  - 无障碍服务读取QQ、X、飞书聊天界面，不hook、不改包、不读数据库
  - 判断模型给出对方意图、危险等级（1-9）与最佳动作，再生成3条候选回复
  - 候选回复一键填入输入框，发送始终由用户手动点击，不碰转账红包
  - 本地知识库与联系人档案，分析时按标签匹配自动带上笔记和历史（历史默认关闭，可选开启）
  - 判断、回复、视觉三路接口可分别配置，内置OpenRouter等多家预设
- **亮点**：
  - 先用判断模型给出意图和危险等级，再据此起草回复，而非直接让模型编回复（项目方设计思路）
  - 不hook、不改包、不走App接口或账号体系，只用系统无障碍服务读屏，截图仅本机OCR不上传
  - 微信Android版已全面下架，当前版本不采集、不分析、不处理微信内容
- **适合**：在QQ、X、飞书等App上聊天、希望AI辅助判断对方意图并起草回复的Android手机用户（仅支持Android 11+ ARM64机型）
- **上手**：`adb install -r apk/jev-assistant-v1.4-release.apk` 需先从仓库下载签名release APK，安装后在设置填入模型API Key，再按向导开启无障碍、悬浮窗等权限
- ⚠️ 触发分析时，聊天文字及你启用的背景信息会发送给你自行配置的第三方大模型服务商，涉及对方聊天内容外流的隐私问题。
- ⚠️ 核心功能靠无障碍服务读取QQ、X、飞书等App的聊天界面内容并自动填入回复文本框，可能涉及相关App服务条款限制。

### [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) ⭐ 5,846

> 自动找热点、写日报的自托管网站框架，换上信源和标准就是你的行业热点站

- **定位**：AIHOT 开源的网站引擎和框架，用大模型自动抓取信源、筛选打分、聚簇事件、生成日报周报月报；换上自己行业的信源和提示词，即可搭建专属行业热点站。
- **能做什么**：
  - 支持 RSS、网页、JSON、X、微信公众号等六种信源及自定义推送，分三级设门槛
  - 大模型先预筛，再独立打两次分，按信源分级门槛决定是否入选精选，提示词全公开可改
  - 同一事件的不同来源报道自动聚簇，按独立来源数量计算热度，48小时内重复来源不多算
  - 每天自动生成日报（默认08:00），每周周报、每月月报从日报汇编而成
  - 提供 RSS、公开 API、MCP、llms.txt 等多种接口，同一份内容同时给人看和给 Agent 用
- **亮点**：
  - 所有提示词原文和入选门槛均开源，可用自己标注的样本在 SelectBench 中校准评分标准
  - 仓库是 AIHOT 线上同款引擎代码，但不含其信源名单和运营数据，示范信源仅18个海外AI资讯源
- **适合**：想为自己所在行业（法律、HR、金融等）搭建热点聚合与日报网站的自托管用户和开发者
- **上手**：`git clone https://github.com/KKKKhazix/AIHOT.git myhot
cd myhot
node scripts/init-env.ts --llm-key <你的模型 API Key>
docker compose up -d --build` 需要 Docker、Node.js 24 和 OpenAI 兼容的模型 API Key，完成后访问 localhost:3000，后台在 /admin

## 本地推理与模型

### [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) ⭐ 8,884

> 用纯C99在单CPU上以8GB内存运行2.78万亿参数的Kimi K3模型

- **定位**：一个零依赖的C99推理引擎，通过4位专家量化、线性注意力和流式加载把2.78万亿参数的Kimi K3模型的内存需求从集群级降到消费级CPU可承受范围。
- **能做什么**：
  - 无BLAS、无框架、无GPU，纯C99实现，仅依赖libm和OpenMP
  - 专家权重打包为4位（MXFP4）格式，按需流式加载，不常驻内存
  - 密集trunk层预先打包为109GB文件，可按预设深度常驻内存
  - 支持AVX2+FMA（x86-64）和NEON（arm64），用LRU缓存管理专家权重
  - 提供laptop到max共5档内存预设，内存预算从8GB到224GB可选
- **亮点**：
  - 项目方数据：laptop预设下峰值内存8.24GB，生成8个token耗时261.5秒，平均32.69秒/token
  - 项目方数据：server预设下峰值内存127.92GB，生成28个token耗时299.3秒，平均10.69秒/token
  - 项目方称同一模型在8GB到224GB不同内存预算下产生字节级相同输出
- **适合**：需要在无GPU、低内存消费级硬件上运行超大规模MoE模型的研究者和工程爱好者
- **上手**：`git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git
cd kimi-k3-in-c
make -j
make test` 无需下载模型即可完成构建和测试，约一分钟；完整推理需下载1.56TB权重并打包trunk后运行

### [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) ⭐ 6,861

> 让260亿参数Gemma4模型在8GB内存Mac上用约2GB内存推理

- **定位**：面向Apple Silicon Mac（含8GB内存机型）的本地大模型推理工具，用专家流式加载技术让260亿参数的Gemma4 26B-A4B在约2GB内存预算下运行。
- **能做什么**：
  - 按token从SSD流式加载所需专家权重，无需把14.3GB完整模型载入内存
  - 自研Swift+Metal运行时，专为该模型定制，不是MLX或llama.cpp的封装
  - 提供Mac原生应用、命令行工具、本地OpenAI兼容服务器三种使用方式
  - 可选安装约1.1GB视觉塔组件支持图像输入，需M2及以上芯片
  - 本地服务器支持函数工具声明，但需客户端自行授权并执行调用
- **亮点**：
  - 项目方数据：8GB内存M2 MacBook Air上测得解码速度5.1-6.3 tok/s
  - 项目方数据：24GB内存M5 Pro上测得解码速度31-35 tok/s
- **适合**：拥有8GB内存等低配Apple Silicon Mac、希望本地运行大模型做推理实验的开发者和爱好者
- **上手**：`swift build -c release && .build/release/TurboFieldfareMac` 克隆仓库后构建运行，首次启动应用需在界面中选择Download下载安装约15GB模型，完成后方可加载生成。
- ⚠️ README明确提示本地OpenAI兼容服务器无远程认证和TLS，只应在loopback地址运行，不可直接暴露到公网

## Skills 与写作/设计

### [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) ⭐ 23,344

> Claude Agent Skill + 本地服务，去除文本和文件中的多厂商 AI 水印与溯源标记

- **定位**：面向拥有内容版权用户的隐私工具，提供 Agent Skill 与本地 Python 服务，检测并清除文本中的隐藏水印及文件的 C2PA/EXIF/XMP 等溯源信息，可装入 Claude Code、Cursor、Grok 等多种 Agent 宿主。
- **能做什么**：
  - 文本 Layer A：去除隐藏 Unicode、异形空格、双向控制符等标记，用确定性脚本处理
  - 文本 Layer B：针对统计型水印，依赖 Agent 改写或可选的 rewrite_text.py 钩子
  - 文件层支持 PNG/JPEG/PDF/DOCX/MP4 等数十种格式的 C2PA/EXIF/XMP/文档属性清理
  - 可选 PostToolUse 钩子：Claude Code 写文件后自动检测或清除水印（check/clean 模式）
  - 提供 Claude Code 插件市场、Cursor、Grok 等多宿主一键安装方式
- **亮点**：
  - 项目方称可识别 Claude、Gemini/SynthID-Text、OpenAI 及开源 LLM 的 Kirchenbauer/Gumb…
  - 核心脚本仅依赖 Python 3.10+ 标准库，无需额外依赖或 Docker
- **适合**：需要清理自有 AI 生成内容中隐藏水印或溯源元数据的开发者、写作者及 Claude Code/Cursor 用户
- **上手**：`python3 install_skill.py --skill remove-ai-marks --target claude-code` 安装 Claude Code 个人版 Skill，需额外启动本地服务（make serve）配合使用
- ⚠️ 去除 AI 内容的水印与溯源标记（如 C2PA、SynthID）可能涉及规避 AI 内容标识相关法规的风险

### [hypit-ai/hypit](https://github.com/hypit-ai/hypit) ⭐ 19,304

> 让 Claude Code 等编程 Agent 克隆任意视频，批量生成素材、字幕与特效的完整工作流

- **定位**：为 Claude Code、Codex 等编程 Agent 提供视频创作的语言和系统，输入参考视频或描述即可生成完整可编辑、可重跑的视频合成工作流
- **能做什么**：
  - 克隆任意参考视频，还原素材、字幕、B-roll、特效的完整可编辑工作流
  - 也可从模板或纯文字描述生成工作流，无需参考视频
  - 组件可插拔，可单独替换主播、字幕等模块或自行编写组件
  - 可选调用生成模型，也可用代码渲染本地完成视频合成，省去生成模型调用费用
  - 复用同一工作流和素材，一次命令产出多个变体
- **亮点**：
  - 项目方称该开源项目不收取座位费和渲染费、不加水印，模型服务费用由用户自选的服务商单独计费
  - 字幕和特效以文字而非秒数为时间锚点，改词后时间自动重新排布
- **适合**：使用 Claude Code、Codex 等编程 Agent 制作短视频、广告变体、UGC 内容的营销与内容团队
- **上手**：`npx skills add hypit-ai/hypit -g` 安装为 Agent 技能后，在项目目录中用 /hypit 指令配合编程 Agent 生成视频
- ⚠️ 仓库采用自定义的 Hypit Open Source License，非常见开源许可证，GitHub 元数据显示许可证未明确判定（NOASSERTION），使用前需自行核实条款
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) ⭐ 11,885

> 面向 AI 编码助手的技能包，清除写作中20多种常见的AI套话模式

- **定位**：为 Claude Code、ChatGPT、Codex 等编码或对话 agent 提供的 Skill，用于检测并移除 AI 生成文本中套路化的表达方式，同时尽量保留作者原有的语言风格。
- **能做什么**：
  - 编辑模式：移除文中AI套话，保留个人语言风格，并列出具体改动
  - 检测模式：只标出文中疑似套话的句子，不判断文本是否为AI生成
  - 覆盖20多种套话模式，如二元对比句、故弄玄虚开场、虚假顿悟式结尾等
  - 附带生成模式，可用于讽刺性制造夸张的AI腔调文案
  - 技能规则写在SKILL.md中，并附带eval.md供自我检查
- **亮点**：
  - 以具体的套话句式清单（如“It's not X. It's Y.”）作为判断依据，而非笼统的“更自然”标准
- **适合**：使用AI辅助写作或编辑、希望去除文本中套路化AI腔调并保留个人风格的写作者和内容创作者
- **上手**：`npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes` 全局安装后，在支持该技能的编码或对话agent中用 /no-ai-slop 命令编辑或检测文本
- ⚠️ 已 33 天未更新

### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) ⭐ 10,305

> 面向 Claude Code / Codex 的 Agent Skill，用 Remotion 制作电影感产品宣传片

- **定位**：这是一个 Agent Skill，内置分镜配方卡库、运动预览库和可运行的 Remotion 视频模板，让 Claude Code 或 Codex 直接把产品截图编排、动画化、配乐成成片宣传视频。
- **能做什么**：
  - 157 个分镜配方卡，含用途、时长、参数与实现注意事项
  - 214 个运动预览，可在在线 Gallery 搜索筛选及复制镜头名
  - 内置 Ink Press 完整模板：36.2 秒、1080p、30fps、10 个镜头
  - 交付后可用浏览器端 Motion Workbench 二次编辑并重新渲染
  - 支持真实网页截图、2.5D 镜头运动、节拍同步剪辑与电影级音效
- **亮点**：
  - 新增的 48 张分镜卡经过 8 轮逐帧比对参考素材筛选产出（项目方数据）
  - 剪映（CapCut CN）项目导出功能已在 macOS 剪映专业版 11.2 上验证，Windows 未测试
  - Motion Workbench 的预览与渲染结果达到像素级一致（项目方数据）
- **适合**：使用 Claude Code 或 Codex 的开发者和团队，需要为产品制作宣传、发布或演示视频
- **上手**：`npx skills add Vincentwei1021/video-shotcraft` 安装后需在 Claude Code 或 Codex 中对话式调用，也可 git clone 后手动软链到 skills 目录
- ⚠️ 渲染视频依赖的 Remotion 框架有独立许可证，个人与小团队免费，公司使用可能需付费许可（项目方说明）

### [jakubkrehel/skills](https://github.com/jakubkrehel/skills) ⭐ 7,463

> 面向 Claude 等 AI Agent 的界面设计技能合集，覆盖 UI、排版、配色、无障碍与布局

- **定位**：一组面向 Claude 等支持 Agent Skills 的 AI 工具的技能合集，用于在构建界面时改进 UI、排版、配色、无障碍、布局与产品文案，并提供综合审查能力。
- **能做什么**：
  - better-ui：优化圆角、对齐、图标、点击区域、动画等界面细节
  - better-typography：改进字号比例、间距、可变字体、OpenType 特性等排版问题
  - better-colors：生成调色板、使用语义化色彩标记、转换格式、检查对比度
  - better-accessibility：帮助项目符合无障碍标准与最佳实践
  - interface-review：对 UI、排版、布局、配色、文案、无障碍多维度给出审查报告
- **亮点**：
  - 包含 break、variant、explain-interface 等需用户手动调用的技能，分别用于组件压力测试、生成变体和解析网页动效…
  - 可通过 npx 命令或 Claude Code 插件市场两种方式安装
- **适合**：使用 Claude Code 等支持 Agent Skills 工具做界面与前端开发的开发者、设计工程师
- **上手**：`npx skills add jakubkrehel/skills` 也可用 Claude Code 插件市场安装：/plugin marketplace add jakubkrehel/skills 后 /plugin install inter…

### [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) ⭐ 5,929

> 面向 AI Agent 的数据可视化 Skill，把数据转化为精致可交互的 HTML 图表与报告

- **定位**：遵循 Agent Skills 格式的数据可视化与报告生成 skill，可供 moxt、Claude Code、Codex 等兼容 SKILL.md 的 AI agent 调用，默认生成单张图表，整页报告需用户明确要求。
- **能做什么**：
  - 提供 Lupi（编辑叙事）、Glance（快速判断）、Basics（基础图型）三种视觉风格，另有网络、路径、流向等独立交互大图
  - 支持 Mono 黑白灰及青瓷蓝、椰林绿、编辑部红三色预设，按场景自动选色
  - 共 49 个图型模板，catalog.md 提供数据契约索引
  - 需用户明确要求报告、年报、白皮书等才生成整页 HTML 报告，可选 12 套中英双语模板
  - 部分模板（Glance、Circular、Force 及报告模板 R11/R12）通过 CDN 加载 Chart.js 或 ECharts…
- **亮点**：
  - 项目方称该 skill 在 Moxt 工作区完成设计与验证，可在同一工作区持续预览和修改图表与数据
  - 用统一字体、留白、线条和明度体系区分“编辑叙事”与“快速判断”两种阅读速度，而非单一图表模板
- **适合**：使用 Claude Code、Codex、moxt 等 AI Agent 的用户，需要把数据快速转化为可发布 HTML 图表或报告
- **上手**：`npx skills add https://github.com/larashero3-dotcom/lieflat-charts --skill lieflat-charts` 安装后向 Agent 发送数据可视化需求即可生成 HTML 图表；也可手动克隆到 ~/.claude/skills 或 ~/.codex/skills 目录下。
- ⚠️ 许可证为 PolyForm Noncommercial License 1.0.0，仅允许学习、修改、分享和非商业使用，商业使用需另行取得许可。
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) ⭐ 5,794

> 面向AI Agent的技能包，指导生成极简可爱的IP吉祥物风格Logo图像

- **定位**：ip-as-logo是遵循Agent Skills开放格式的技能包，指导兼容的AI Agent按固定规则生成简化、圆润、带轻微拟物质感的IP吉祥物图像，可用作企业吉祥物或Logo素材，不绑定特定Agent产品。
- **能做什么**：
  - 指导生成由4-7个大色块构成的圆润极简吉祥物轮廓，去除多余细节
  - 默认采用三种语义色：两个IP主色加一个背景色，背景饱和度略调低
  - 用户确认方向后默认批量产出6张图，三张左下出场三张右下出场
  - 开放主题时默认以常见动物为吉祥物主体，物品、机械等需有明确产品理由
  - 兼容Codex、Coze、豆包、Manus、Gemini Apps等Agent，需配合GPT Image 2等顶级图像模型
- **亮点**：
  - 项目方称技能不回退使用SVG，若没有顶级图像模型，需用户明确同意才使用替代模型，且不保证效果等同
  - 官网提供预生成的IP吉祥物图片库，供没有兼容Agent的用户直接免费下载并商用
- **适合**：需要为产品设计简约吉祥物或Logo素材的设计师、产品团队，以及使用Codex、Coze、豆包等兼容AI Agent的用户
- **上手**：`npx skills@latest add s1dashu/ip-as-logo-skill` 安装后在支持的Agent中启用，并确保配置了顶级图像模型，再用自然语言描述所需吉祥物即可生成
- ⚠️ 已 44 天未更新

### [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) ⭐ 5,355

> 面向求职场景的 AI Skills 插件包，覆盖开源贡献、简历制作到投递跟进全流程

- **定位**：可安装进 Claude Code、Codex 等平台的插件包，提供九个面向求职场景的 Skill 入口，覆盖开源贡献、简历提升与制作、面试准备、岗位匹配与投递跟进。
- **能做什么**：
  - /contributor 寻找有证据支撑的开源问题，经用户逐项确认后才提交 PR
  - /make-resume 生成可编辑 HTML 简历，支持 PDF 导出和可选 LaTeX 源文件
  - /job-match 对照 JD 与简历输出证据矩阵、硬性门槛和投递建议
  - /job-apply 连接已登录浏览器填写招聘网站申请表，默认停在提交前供用户核对
  - /offer 整理招聘邮件和投递记录，生成本地求职进度表
- **亮点**：
  - 同时支持 Codex、Claude Code、TraeWork、Qoder，另提供 Cursor、OpenCode、WorkBuddy 轻…
  - 九个入口共享同一套 skills/assets/references 和证据账本，可按顺序组合成完整求职流程
- **适合**：正在求职、需要整理开源贡献证据、制作简历或跟进投递进度的开发者和求职者
- **上手**：`/plugin marketplace add Hisn00w/ASu-skills` Claude Code 下执行该命令后还需执行 /plugin install asu-skills@asu 并按提示 /reload-plugins
- ⚠️ /job-apply 需连接用户已登录的浏览器自动填写招聘网站申请表，自动化操作第三方网页存在违反网站服务条款的风险

## 开发者工具与集成

### [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) ⭐ 13,449

> 让 Codex 把 ChatGPT 网页版（含 Pro）当作模型使用，不消耗 Codex 配额

- **定位**：一款浏览器自动化桌面工具，通过内置浏览器登录 ChatGPT 网页版，让 Codex 的模型选择器中可用 ChatGPT Web 各档模型，使用网页版自己的用量限制而非 Codex 或 Work 配额。
- **能做什么**：
  - 在 Codex 原生模型选择器中接入 ChatGPT Web 模型，支持上下文、工具调用、流式输出和图片
  - 内置浏览器与运行时，无需单独安装 Chrome、Node 或 Bun
  - 可选 Full harness 模式，通过 MCP 把 ChatGPT 工具调用接回 Codex 任务的文件与终端
  - 提供 Zero Risk 模式，手动粘贴发送提示词，不读取或操作 ChatGPT 页面
  - 支持跨后端子代理协议切换（Compatibility V1 或 Native）
- **亮点**：
  - 项目方说明 Full harness 模式的隧道连接为单向出站，不开放公网入口或端口转发
  - Plus Medium/High 模式下测得的上下文窗口为 9万 tokens，开启实验性 3倍上下文后可达 27万 tokens（项目方…
- **适合**：希望用 ChatGPT 网页版（含 Pro）账号额度为 Codex 提供模型，又不想消耗 Codex 自身配额的开发者
- **上手**：`curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh | sh` 安装启动器后需在内置浏览器登录 ChatGPT 并完成安装模型步骤，再重启 Codex 一次
- ⚠️ README 明确说明这是非官方的浏览器自动化，通过模拟登录操作 ChatGPT 网页版，可能违反 OpenAI 服务条款并有账号风险
- ⚠️ 浏览器登录状态是敏感凭证，本地同用户进程可访问回环监听端口，需在可信设备使用

### [google/artemis](https://github.com/google/artemis) ⭐ 10,973

> 用自然语言驱动安卓自动化测试，集成主流AI编程助手的MCP工具

- **定位**：Google出品的安卓自动化工具，将自然语言指令转化为跨应用测试和日常任务执行，通过MCP与Antigravity、Codex、Claude Code等AI编程助手集成，支持日志采集与截图诊断。
- **能做什么**：
  - 跨应用自动化：根据自然语言指令执行安卓测试流程与日常任务
  - 多模态定位：元素索引为主，坐标与视觉识别作为自定义界面的后备方案
  - MCP集成：Antigravity、Claude Code、Windsurf等IDE可直接操控测试设备并采集Logcat与截图
  - 双执行模式：Flash快速响应约3-5秒/步，Pro模式支持规划、校验与长时间探索测试
  - 提供Web可视化控制台、MCP服务器、命令行与Python SDK四种使用方式
- **亮点**：
  - 在Google Research的AndroidWorld基准（20+应用、100+多步任务）上达到99%+任务完成率（项目方数据）
  - Apache-2.0许可，Google官方项目
- **适合**：需要为安卓应用做自动化测试，或希望用AI编程助手驱动设备操作与问题诊断的开发者和测试工程师
- **上手**：`git clone https://github.com/google/artemis.git && cd artemis && ./start.sh` 需已连接安卓设备（开启USB调试）或模拟器，脚本自动安装ADB等工具链并启动Web控制台

### [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) ⭐ 7,028

> 让 ChatGPT 网页版做规划审查，Codex 负责执行代码的 MCP 桥接工具

- **定位**：以 Codex Skill 形式接入，把闲置的 ChatGPT Plus/Pro 网页版额度用作编码任务的规划与审查大脑，Codex 保留全部执行权，不占用 API 额度，不用逆向代理。
- **能做什么**：
  - 通过只读 MCP 连接让 ChatGPT 按需读取工作区代码，仓库不整体上传
  - OAuth 2.1 加一次性配对码保护连接，无 token 访问返回 401，工作区不匹配返回 403
  - .env、密钥、SSH 凭据等敏感文件默认禁止读取，可用 .c2cignore 自定义规则
  - Codex 执行后，ChatGPT 通过 MCP 独立核查 git diff 和测试记录再给审查意见
  - 安装为 Codex Skill，可选配置 Cloudflare 固定域名，默认用临时隧道并自动重连
- **亮点**：
  - 服务端不存在写入、删除、shell、提交类工具，结构上保证只读，无法被提示注入绕过
  - 项目方称测试套件覆盖 150 个用例，涉及路径安全、OAuth、配对流程和 MCP 端到端场景
- **适合**：使用 Codex 编写代码、同时已订阅 ChatGPT Plus/Pro 网页版，希望用网页版额度做规划和代码审查的开发者
- **上手**：`pnpm install` 克隆仓库后执行 pnpm build 构建，再把 skill/ 安装为 Codex Skill 并运行 c2c setup 完成配对
- ⚠️ 核心流程通过 Computer Use 方式与 ChatGPT 网页版自动交换状态消息并驱动会话，可能涉及 ChatGPT 服务条款风险

## 越狱与绕过模型限制

> ⚠️ 核心功能是绕过 AI 模型或平台的安全限制，非官方支持、违反服务条款，使用可能导致封号。

### [MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct) ⭐ 9,179

> 针对 Codex/GPT 系列模型的破甲提示词与可复现评测工具链

- **定位**：为 Codex 系列模型提供越狱（破甲）提示词及配套的 A/B/C 分级回归测试、JailbreakBench 评测工具，用于绕过模型默认安全限制并验证提示词的稳定性与可复现性。
- **能做什么**：
  - 提供 gpt-5.6-sol-v45 稳定版及 gpt-6-astra、gpt-6.1-sol 两个预发布版破甲提示词
  - Python 脚本一键部署、预览（dry-run）与回滚 Codex 的 model_instructions_file 配置
  - A/B/C 三级发布门禁回归测试，含人工复核与工件（artifact）校验
  - 可选 JailbreakBench 模块化评测 JB-A/JB-B，覆盖 100 条 harmful behaviors
  - 部署前自动保存配置快照，支持显式还原
- **亮点**：
  - 项目方数据：两预发布版B门禁（42/50、34/50等）未达66/66、74/74硬门槛，C未运行
  - 项目方数据：两次 fresh A 测试均为 3/4
- **适合**：需要测试或绕过 Codex/GPT 安全限制的研究者，以及关注破甲提示词评测方法的开发者
- **上手**：`python3 codex-instruct.py --apply --version gpt-5.6-v45` 需先 git clone 本仓库并进入目录，该命令部署当前稳定版提示词到本地 Codex 配置中
- ⚠️ 项目核心功能是绕过/破解模型的安全限制（越狱），使用可能违反模型提供方的服务条款
- ⚠️ README 明确提示从事破甲活动、使用自定义模型指令存在账号被封风险，建议使用日抛账号
- ⚠️ README 声明项目不用于任何商业化行为，但仓库许可证标注为 MIT，二者存在表述上的不一致

## 其他

### [bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book) ⭐ 5,882

> 从硬件约束出发，量化推导 LLM 推理与训练系统设计的开源电子书

- **定位**：李博杰撰写的开源书稿，从硬件约束和模型架构出发，用量化估算推导 LLM 推理与训练系统设计，是《深入理解 AI Agent》姊妹篇，书稿仍为初稿。
- **能做什么**：
  - 全书十二章，覆盖模型架构、加速器、数据中心网络、推理优化与训练系统
  - 配套计算工具可复算书中数字，静态计算只需 Python 3.10+ 标准库，无需 GPU 或模型权重
  - 配套实验按章节组织，附运行方法、输入条件和结果说明，部分实验需 GPU
  - 提供简体中文原版及英文、繁体中文、俄语社区翻译，含 PDF、EPUB 与在线阅读网站
- **亮点**：
  - 是作者《深入理解 AI Agent》（项目方称获 50k+ Star）的姊妹篇，聚焦 AI 系统基础设施
  - 配套计算工具静态计算无需 GPU 或模型权重，可直接复算书中资源估算数字
- **适合**：已调用模型 API 或本地运行过模型、想弄清推理为何慢及如何降本的开发者，以及系统、网络、芯片方向的工程师、研究者和学生
- **上手**：`git clone https://github.com/bojieli/ai-infra-book.git` 克隆后可用 python3 calculations/calc.py 复算书中数字，静态计算无需 GPU 或模型权重

## 已排除（判定与 AI 无关）
- Mak5er/AirCard：一款 macOS 应用，通过 USB 连接 iPhone，利用名为 airlift 的系统漏洞为 Apple Wallet 卡片和锁屏密码键盘替换自定义图案，无需越狱设备。
