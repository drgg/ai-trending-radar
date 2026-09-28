# GitHub 近 90 天 AI 热门项目（Stars > 5000）

- 数据快照：2026-09-28　共 33 个项目

## 本期变化
对比 2026-09-21：
- 新上榜：browser-use/jev-ultrafast、zai-org/ZCode、jev-chat/jev-chat-jarvis、Human-Agent-Society/reef、bojieli/ai-infra-book、TencentCloud/Octop、Hisn00w/ASu-skills、aipoch/open-science
- 移出：oomol-lab/open-connector
- 涨幅榜：hypit-ai/hypit +4816、miuuyy/codex-chatgpt-web +2166、google/artemis +2038、dataelement/dsh-desktop +1994、tamaratran/fast-jev-compaction +1600

## 趋势小结
- 面向AI Agent的垂直技能包大量涌现，覆盖设计、简历、可视化等场景，如no-ai-slop、ASu-skills、ip-as-logo-skill
- 开源Agent运行时/操作系统成基础设施热点，强调协作与自进化，如aos-ce、reef、utopia
- 编程Agent工具持续迭代，终端桌面一体化与上下文管理并进，如grok-build、ZCode、fast-jev-compaction
- 消费级硬件跑超大模型的极限推理引擎受关注，如kimi-k3-in-c、turbo-fieldfare
- AI安全与红队自动化工具浮现，越狱与渗透测试框架同步增长，如T3MP3ST、gpt-instruct

## 编程 Agent 与运行框架

### [xai-org/grok-build](https://github.com/xai-org/grok-build) ⭐ 27,132

> xAI 出品的终端 AI 编程助手，全屏 TUI 交互，可编辑代码、执行命令

- **定位**：Grok Build（grok）是 xAI（SpaceXAI）开发的终端 AI 编程 Agent，理解代码库、编辑文件、执行 shell 命令、搜索网页并管理长任务，可交互使用也可无头运行于 CI 或嵌入编辑器。
- **能做什么**：
  - 全屏、支持鼠标操作的终端 TUI 界面
  - 可编辑文件、执行 shell 命令、联网搜索
  - 支持交互式、无头脚本化（CI）和通过 ACP 协议嵌入编辑器三种运行模式
  - 支持 MCP 服务器、插件、Hooks、技能（skills）和沙箱运行
  - 官方提供 macOS/Linux/Windows 预编译二进制，源码从内部 monorepo 定期同步
- **亮点**：
  - 由 xAI 官方发布，Star 数已近 2.7 万，增长迅速
  - 部分工具实现移植自 openai/codex 与 sst/opencode 项目
- **适合**：使用命令行工作、希望借助 AI Agent 辅助编码、调试和自动化任务的开发者
- **上手**：`curl -fsSL https://x.ai/cli/install.sh | bash` 安装后运行 grok，首次启动会打开浏览器完成身份认证
- ⚠️ 不接受外部代码贡献，仓库为只读同步性质
- ⚠️ 首次启动需通过浏览器登录 xAI 账号完成认证，涉及账号授权

### [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) ⭐ 20,908

> 超快浏览器操作 Agent，用动态索引动作空间替代截图驱动方案

- **定位**：一个浏览器自动化 Agent 框架，通过结构化 DOM 快照生成动态索引动作空间，一次网络请求内同时选出操作和目标元素，仅在需要输入文本时调用小型 LLM 生成内容，以降低延迟。
- **能做什么**：
  - 每次观察生成带编号的可操作元素表，动态定义可执行动作空间
  - 操作预测与目标预测合并为一次 TypeSafe 网络请求，减少往返次数
  - 默认不依赖截图，直接消费结构化页面状态，本地调试界面才启用截图
  - 执行前校验目标元素页面新鲜度与遮挡情况，降低误操作风险
  - 代码库精简，核心循环、DOM 快照、浏览器执行等模块均可直接阅读
- **亮点**：
  - 项目方数据：Google Flights 单程航班搜索任务7.1秒完成，含模型调用与页面加载等待
  - 项目方数据：与对比版本相比，浏览器协议调用次数从1092次降至101次，任务耗时中位数下降25%
- **适合**：需要构建低延迟网页自动化/浏览器 Agent 的开发者，尤其关注减少模型调用和协议往返开销的团队
- **上手**：`git clone https://github.com/browser-use/jev-ultrafast.git && cd jev-ultrafast && uv sync && cp .env.example .env && uv run jev` 需自行配置 TYPESAFE_API_KEY 和 TEXT_MODEL_API_KEY（如 OpenRouter），并通过 Browser Harness 连接 Chrome
- ⚠️ 自动化操作 Google Flights、Wikipedia 等第三方网站，可能受目标网站服务条款限制
- ⚠️ 依赖 TypeSafe 商业 API 和第三方文本模型服务，实际使用会产生外部 API 调用成本

### [google/artemis](https://github.com/google/artemis) ⭐ 10,493

> Google 出品的自然语言驱动 Android 自动化测试与操作框架

- **定位**：将自然语言指令转化为可靠的 Android 端到端自动化操作，支持测试与日常任务执行，并通过 MCP 与 AI 编程助手集成
- **能做什么**：
  - 观察-行动的多模态定位，结合无障碍层级、OCR 与视觉模型识别界面元素
  - 原生 MCP 服务器，供 Antigravity、Claude Code、Codex 等 IDE 驱动真机执行任务
  - Flash 与 Pro 双执行模式，分别面向快速响应和深度规划验证场景
  - 自动采集 Logcat 日志与截图，支持长时间探索性与稳定性测试
  - 提供 Web 可视化控制台、CLI 和 Python SDK 多种使用方式
- **亮点**：
  - 项目方数据：在 Google Research 的 AndroidWorld 基准（20+ 应用、100+ 多步任务）上完成率超 99%
  - Flash 模式单步响应约 3-5 秒，采用历史压缩而非截断以支持长流程任务
- **适合**：移动应用测试工程师、需要 Android 自动化的开发者，以及使用 AI 编程助手做移动端调试的团队
- **上手**：`git clone https://github.com/google/artemis.git && cd artemis && ./start.sh` 需先通过 USB 调试连接 Android 设备或模拟器，一键脚本会自动安装 ADB、scrcpy 等依赖
- ⚠️ 会在测试设备上安装无障碍辅助服务并读取屏幕内容，需注意在授权设备上使用

### [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) ⭐ 7,042

> Claude Code 插件：逐条为工具调用打分，取代压缩摘要，保留内容全为原文

- **定位**：上下文压缩常用LLM生成摘要而丢失细节，本项目改用Jev模型对每次工具调用和结果打分，决定保留、截断或删除，保留部分始终逐字不变；可作Claude Code插件替换内置压缩，也可作npm库单独使用。
- **能做什么**：
  - 对每次工具调用和结果单独打分，只做保留/截断/删除决策，不做摘要改写
  - 保留的用户、助手文本及工具结果均逐字保留、绝不改写或概括
  - 通过TypeSafe的Jev模型API评分，可配置token上限、保留窗口、阈值等参数
  - 同时提供npm库和Claude Code插件两种形式，插件在压缩效果不足时自动回退内置摘要
  - 附带SwiftUI动画演示程序，用于录屏展示压缩决策过程
- **亮点**：
  - 与常见摘要式压缩不同，只删减不改写，避免文件路径、报错等细节因概括而丢失
  - 项目方数据：GitHub已获5442星、297 fork
- **适合**：使用Claude Code进行长会话开发、担心上下文压缩丢失关键细节的工程师
- **上手**：`npm install fast-jev-compaction` 需先设置TYPESAFE_API_KEY；作为Claude Code插件需添加marketplace并安装，且要求2.1.274+版本
- ⚠️ 需要将完整对话历史发送给第三方TypeSafe的Jev API进行打分，存在会话数据外传的隐私风险
- ⚠️ 依赖Claude Code尚处早期访问阶段的function hooks特性，需手动开启实验性开关才能使用
- ⚠️ 功能运行依赖外部API密钥和第三方服务可用性，非完全自托管方案

### [zai-org/ZCode](https://github.com/zai-org/ZCode) ⭐ 6,933

> Z.ai 出品的 AI 编程工作台，桌面、Web、终端三端合一的编码 Agent

- **定位**：面向开发者的编程 Agent 工具，统一 zcode 命令支持 TUI 终端、本地 Web 界面和 Electron 桌面应用，本仓库开源客户端、后端服务与 Agent CLI/运行时源码。
- **能做什么**：
  - 单一 zcode 命令切换 TUI 终端、Web 界面和桌面应用三种形态
  - 内置 HTTP/WebSocket 后端服务，支持本地和远程项目连接（SSH/WSL）
  - Web 模式支持局域网访问、端口自定义与访问令牌认证
  - 提供 Agent 客户端 SDK、共享 UI 组件和 Provider 扩展能力
  - 完整打包发布流程，含安装脚本、校验摘要和多平台桌面构建
- **亮点**：
  - 同一套 Agent 运行时同时驱动桌面、Web、终端三种交互形态，架构统一
  - 支持 SSH/WSL 远程开发场景，资源通过 SFTP 上传而非依赖公网 CDN
- **适合**：需要在终端、浏览器或桌面环境中使用 AI 编程 Agent 的开发者，以及希望自建或定制编码工具链的团队
- **上手**：`pnpm bootstrap` 初始化后可用 pnpm dev:desktop 跑桌面版，或用 zcode / zcode --web 启动命令行发行包

### [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) ⭐ 6,789

> 让付费ChatGPT网页版当规划审查大脑，Codex 负责执行编码任务

- **定位**：通过只读MCP桥接把ChatGPT网页版接入Codex编码会话：ChatGPT负责思考规划和代码审查，Codex保留全部执行权，仓库代码不上传，只按需读取所需的少量代码。
- **能做什么**：
  - 只读MCP桥接提供9个工具，供ChatGPT按需读取工作区文件、git状态与测试结果
  - OAuth 2.1加一次性配对码鉴权，无token访问公网端点直接401
  - 单工作区单边界，路径规范化处理防止符号链接与路径穿越攻击
  - .env、密钥、SSH凭证等敏感文件默认拒绝读取，可用.c2cignore自定义规则
  - Codex执行后ChatGPT查看真实git diff和测试记录做独立审查，不轻信测试通过的说法
- **亮点**：
  - 不需要API Key、不用逆向代理，直接组合官方ChatGPT网页版和Codex CLI使用
  - 项目方称已完成端到端验证，含150个测试覆盖路径安全、OAuth、配对和MCP流程
- **适合**：已订阅ChatGPT Plus/Pro并使用Codex CLI编码、希望用网页版闲置额度做规划审查以节省API用量的开发者
- **上手**：`pnpm install && pnpm build` 构建后运行c2c setup完成桥接、隧道和配对，也可让Codex按README提供的一段指令全自动安装配置

## Agent 平台与基础设施

### [yc-software/qm](https://github.com/yc-software/qm) ⭐ 15,268

> 面向团队的多人协作 Agent 框架，同时支持 Slack 与网页端

- **定位**：QM 是为创业公司打造的多人 Agent 协作框架，每位员工拥有独立作用域和沙箱，也能在频道、项目中与 Agent 协同工作，底层模型与 harness 可自由切换。
- **能做什么**：
  - 个人与共享作用域并存，可在 Slack 频道和项目中协同使用 Agent
  - 支持 Pi、OpenCode、Codex、Claude Code 等多种 harness 和模型切换
  - 内置定时任务、监控和 webhook，可在无人值守时自动执行后台工作
  - 可搭建内部 Web 应用并按权限发布给指定成员
  - Skills 按作用域共享，支持管理员提升权限及从 Git 仓库导入技能包
- **亮点**：
  - 安全策略分 Strict/Auto/Dangerous 三级，共享策略分 Isolated/Open，可按组织和作用域精细控制
  - 每个用户和房间拥有独立的持久化沙箱、记忆与权限，核心运行时与企业部署配置分离
- **适合**：需要为团队搭建协作式 AI Agent 工作环境的创业公司工程与运维团队
- **上手**：`npm exec --yes --package=@yc-software/qm@latest -- qm init . --org <slug> --target <fly-or-aws>` 需创建自有部署仓库并接入自己的云账号（Fly 或 AWS），非开箱即用的本地工具
- ⚠️ Agent 以用户自身身份和权限执行操作并被审计记录，组织需自行把控权限边界和数据共享范围

### [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) ⭐ 10,085

> 将 DeepSeek Harness 打包成本地优先的跨平台桌面应用

- **定位**：DSH Desktop 是 DeepSeek Harness（Agent 运行时 + Web UI）的桌面封装产品，自动启动本地运行环境并打开完整界面，统一管理配置文件、插件、工作区与模型设置。
- **能做什么**：
  - 自动启动/停止 Harness，无需单独 CLI 或浏览器标签页
  - 支持导入导出 .dshpreset 便携式 Agent 预设包，带冲突检查与信任提示
  - 内置 PPT 模式，提供 16 套模板 192 种版式，生成可编辑 PPTX
  - 安全模式可临时屏蔽第三方插件，识别故障插件并引导恢复
  - 支持手机通过局域网或临时隧道连接继续会话
- **亮点**：
  - macOS 版本经 Apple 签名与公证，Windows 版本经代码签名
  - 渲染进程无 Node.js 权限、启用上下文隔离与沙箱，会话数据存于应用目录之外
- **适合**：需要在本地运行 DeepSeek Harness、希望获得原生桌面体验、插件管理和跨设备续接会话的开发者与重度用户
- **上手**：`open -a "DSH Desktop" --args --safe-mode` 需先从官网或 GitHub Releases 下载安装包；该命令用于以安全模式启动以排查插件故障
- ⚠️ 当前为早期预览版本，基于快速迭代的 dsh@0.1.5-rc.2，稳定性和插件兼容性有限
- ⚠️ 手机远程访问依赖 Cloudflare Quick Tunnel 或 Pinggy 等第三方临时隧道服务

### [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) ⭐ 8,462

> 面向智能体的开放操作系统，提供CLI、能力胶囊与运行时管理

- **定位**：AOS Community Edition 是为智能体设计的可审查、可组合运行环境，提供 aos CLI、HTTP API、官方 capsule 集合及 MCP 接入，供开发者搭建和治理agent系统。
- **能做什么**：
  - aos CLI与HTTP API统一管理运行时、发行版与capsule
  - 内置22个官方生产级capsule作为可组合用户态构建块
  - aos mcp serve支持Codex、Claude、Grok等客户端接入
  - Forge工具辅助智能体检查系统、发现缺口并构建最小权限capsule
  - 发布物附带校验和、Sigstore签名与构建溯源证明
- **亮点**：
  - 项目方称安装全部22个capsule约需2分钟等待（受限流批次影响），为自报数据
  - 支持stable、dev、nightly等多签名发布渠道，元数据未签名时安装会失败关闭
- **适合**：需要为Codex、Claude、Grok等智能体提供可控本地运行环境、权限管理与可组合能力扩展的开发者
- **上手**：`curl --proto '=https' --tlsv1.2 -fsSL https://aos.unicity.ai/install.sh | sh` 安装后执行aos init完成初始化，可加--offline离线使用本地已打包的capsule资源。
- ⚠️ fork/star 比例异常（22/8462），热度可能有水分

### [deeplethe/utopia](https://github.com/deeplethe/utopia) ⭐ 7,903

> 开源企业级世界模型，双时态知识图谱驱动的知识治理与决策系统

- **定位**：DeepLethe打造的开源企业知识引擎，将时间感知与本体内置于底层，知识随材料自动演化，冲突检测、推理与决策均基于本体运行，可离线部署构建可信决策核心与合规审计链。
- **能做什么**：
  - 支持PDF/DOCX等多格式文档及网页、GitHub、Jira、Notion等数据源定时同步
  - 全文检索(Tantivy)与向量检索(pgvector)融合，答案流式输出并附来源引用
  - 内置Agent可搜索文档、遍历图谱、查询数据库，并通过MCP接入Claude Desktop等客户端
  - 双时态知识图谱：修正事实不覆盖旧版本，保留世界真实状态与系统认知两条时间线
  - 本体驱动的冲突检测与推理，实体合并可撤销，决策过程留痕形成审计日志
- **亮点**：
  - 单个Rust二进制加PostgreSQL即可运行，无需额外中间件，支持全离线部署
  - 自研Ontology2SQL方法在BIRD Mini-Dev文本转SQL基准上表现领先（项目方数据）
- **适合**：需要自建可信知识库、决策审计追踪的企业技术团队，以及关注知识图谱、GraphRAG与Agent记忆系统的开发者
- **上手**：`docker compose --profile app up -d` 先clone仓库并准备Docker环境，启动后访问 http://localhost:1516 注册即成为管理员
- ⚠️ 项目仍处于v0.1早期阶段，数据库schema随版本演进且迁移不可回滚，升级需谨慎备份
- ⚠️ 官方提示暴露到公网前需先阅读SECURITY.md，存在安全配置风险

### [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) ⭐ 6,638

> 开源的智能体持续自我进化基础设施，连接推理、反馈、训练与版本发布

- **定位**：Reef 是首个开源的持续自我进化智能体基础设施，把推理服务、反馈收集、训练学习、版本发布整合成闭环，支持训练模型权重或优化智能体harness两种进化路径。
- **能做什么**：
  - 四步闭环：提供推理服务、匹配用户反馈、生成候选更新、评估后发布新版本
  - 支持用Slime、SGLang训练模型权重，或优化harness的提示词、规则与技能
  - 推理接口兼容OpenAI与Anthropic格式，可直接接入/v1/chat/completions
  - 内置Reefine等多种recipe，覆盖科学发现、连续任务学习、真实使用反馈等场景
  - 更新期间保持服务在线，具备版本历史管理与回滚能力
- **亮点**：
  - 项目方数据：在AIME2025、Terminal-Bench、IMOAnswerBench等基准上验证了多个recipe的改进效果
  - 宣称是唯一兼具在线推理、权重训练、版本管理与harness进化四种能力的开源框架
- **适合**：需要让智能体从真实交互中持续学习的AI工程师，以及需要做RL训练或优化coding agent harness的团队
- **上手**：`uv pip install reef-infra` 需先用uv创建并激活虚拟环境；权重训练需配套GPU栈，harness进化只需一个模型API即可体验
- ⚠️ harness自我进化功能会让模型以coding agent身份自动修改并执行代码变更，需在沙箱或可信环境中运行

### [truefoundry/trueforge](https://github.com/truefoundry/trueforge) ⭐ 5,989

> 开源的 Agent 运行时，把 LLM 变成可用的智能体

- **定位**：TrueForge 承担 Agent 执行循环——模型调用、工具、沙箱、审批、上下文管理，并通过聊天界面、HTTP API/SDK、可嵌入 UI 三种方式对外提供，省去自建运行时的重复劳动。
- **能做什么**：
  - 支持 OpenAI、Anthropic、Gemini 等多模型及任意 OpenAI 兼容接口
  - 可接入远程 MCP 工具，支持 Header 认证和 OAuth
  - 支持 SKILL.md 技能包，按需在沙箱中加载
  - 沙箱作为工具按需提供隔离代码/文件执行环境，密钥留在运行时内
  - 内置工具审批、追问用户、生成式 UI 等人工检查点
- **亮点**：
  - 项目方数据：在相同任务和模型下，成本低于 Claude Managed Agents 和 deepagents，精度相当
- **适合**：需要快速搭建生产级 Agent 运行时的开发者和团队，尤其是已用 MCP/多模型但缺少统一执行框架的场景
- **上手**：`npx @truefoundry/trueforge@latest` 本地模式单进程+SQLite适合个人试用；团队或生产建议用 Docker Compose、Helm 或 Railway 的托管模式
- ⚠️ 本地模式默认无登录且数据存于本地 SQLite 文件，官方提示仅限本机使用，不适合暴露到公网

### [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) ⭐ 5,656

> 自托管AI协作者平台，每个Agent配专属浏览器、文件和操作审批网关

- **定位**：OpenBot是可部署在自有基础设施上的开源Agent平台模板，通过AG-UI协议接入任意Agent框架，每个Bot拥有独立电脑（浏览器、文件、工具），所有操作经统一网关审批并留痕。
- **能做什么**：
  - 每个Bot拥有独立容器、workspace卷和浏览器profile，可选gVisor沙箱隔离
  - 统一网关先鉴权记录再执行，CEL策略引擎默认拒绝未授权操作
  - 支持Google Drive、Notion等MCP服务器，工具按Bot逐一授权
  - Bot遇登录墙或2FA时可移交人工接管，全程操作可审计追溯
  - 内置13个示例协作者（费用审核、会议纪要、发布说明等），配置化定义
- **亮点**：
  - 基于AG-UI协议，可接入LangGraph、CrewAI、Mastra、Pydantic AI等任意Agent框架
  - Docker Compose一键部署，数据存于自有PostgreSQL，不绑定任何模型厂商
  - 官方明确定位为"模板而非产品"，需克隆源码后自行定制部署，无托管版本
- **适合**：需要在自有基础设施上部署可控AI协作者的企业技术团队，尤其关注操作审计、权限治理和多Agent框架接入的场景
- **上手**：`docker run -p 3001:3001 --env-file .env -e EMBEDDED_POSTGRES=on -v openbot-data:/var/lib/postgresql ghcr.io/copilotkit/openbot:latest` 需先获取CopilotKit Intelligence项目密钥和模型API Key并写入.env，再执行bun install和启动脚本
- ⚠️ Bot使用独立浏览器登录第三方网站执行自动化操作，可能违反目标站点的服务条款
- ⚠️ 处于Alpha早期开发阶段，官方提示存在较多不稳定问题

### [TencentCloud/Octop](https://github.com/TencentCloud/Octop) ⭐ 5,358

> 腾讯云出品的自托管多用户多智能体 AI 助手

- **定位**：面向家庭和小团队的自托管 AI 助手平台，单进程运行 Web 控制台、CLI、IM 渠道和定时任务，数据全部留在本地。
- **能做什么**：
  - 多用户专家团队，管理员统一分配，内置专家库和专家市场
  - 支持飞书、钉钉、QQ、微信、Telegram、Discord、企业微信等 IM 渠道接入
  - 可插拔工作区后端：本地磁盘、Docker 沙盒、PostgreSQL 或 COS/S3
  - ACP 双向集成，可调用或被 OpenCode、Claude Code 等外部编码 Agent 调用
  - 内置浏览器自动化、远程桌面、终端 AI 及 RAG 知识库
- **亮点**：
  - 单进程架构整合 Web、CLI、IM、定时任务，重启后从控制面数据库完整恢复状态
  - 记忆随工作区迁移，配合专家共享池和 MBTI 人格模板打造差异化 Agent
- **适合**：希望自建私有 AI 助手的开发者、注重数据隐私的家庭用户及需要跨 IM 协同的小团队
- **上手**：`curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash` 安装脚本自动用 uv 配置 Python 3.12 虚拟环境，也提供桌面客户端安装包和 FnOS NAS 版本。

## AI 应用产品

### [trycompai/crm](https://github.com/trycompai/crm) ⭐ 10,931

> 开源CRM，AI Agent是核心而非附加聊天框

- **定位**：Comp AI CRM 把自主研究型Agent作为CRM的运行主体，Agent独立部署、自定调度、调研客户信息并按证据强弱决定是否落库，而不是给传统CRM表单加个聊天框。
- **能做什么**：
  - Agent独立部署运行，拥有自己的任务队列、调度计划和研究预算
  - 18个内置工具加4个技能文件，按证据强度分级录入，杜绝置信度打分
  - 沙箱支持bash/grep/glob执行，默认deny-all出站，且不挂载数据库凭证
  - 无需任何外部API Key即可运行，靠已有邮件与会议记录做基础调研
  - 每个联系人/公司/交易都有Agent标签页，可查看执行步骤和决策理由
- **亮点**：
  - 设计理念强调工具只报告观测事实、拒绝AI自评置信度，弱证据仅生成待人工确认的建议
  - 沙箱环境无网络无数据库访问权限，从架构上防止客户数据经由Shell命令泄露
- **适合**：需要AI自动调研、维护和补全客户资料的销售/CRM团队，以及关注Agent系统架构设计的开发者
- **上手**：`git clone https://github.com/trycompai/crm.git && cd crm` 需先装好Bun和Docker，配置.env后依次执行bun install、docker compose up -d、数据库迁移与bun run dev
- ⚠️ 需接入Google/Microsoft账号授权读取Gmail、日历及LinkedIn数据，涉及第三方账号权限和隐私合规问题

### [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) ⭐ 8,017

> 开源 AI 办公套件，本地编辑真正的 Word/Excel/PPT/PDF 文件

- **定位**：GenOffice 是免费开源的 Office 替代品，内置 AI 编辑器直接读写 .docx/.xlsx/.pptx，并提供 CLI 与 Agent 技能，让 Claude Code、Codex、Cursor 等在本地创建和修改真实办公文件。
- **能做什么**：
  - 支持 docx/xlsx/pptx/PDF/Markdown/HTML 编辑，未修改部分逐字节保留原文件
  - AI 编辑以追踪修改和差异呈现，可一键回滚，表格生成活公式而非纯数字
  - 文件全部在本地打开、编辑、保存和转换，PDF 转 Word/Excel/PPT 也在设备端完成
  - 可自带 API Key，支持 Claude、OpenAI、Gemini、DeepSeek 等十余家模型及本地服务
  - 附带 genoffice CLI、Agent 技能和 MCP 服务器，支持编码 Agent 直接操作文件
- **亮点**：
  - 7190 星，Apache-2.0 协议，支持 macOS、Windows、Linux 三平台原生应用
  - MCP 服务器提供 29 个工具，可让 Claude Desktop 等客户端直接构建 Word 文档
- **适合**：需要用真实办公文件格式做 AI 协作的个人和团队，以及希望编码 Agent 生成正式文档的开发者
- **上手**：`npx skills add genspark-ai/genoffice` 安装 GenOffice 应用后即含 genoffice CLI，也可通过该命令为 Claude Code、Cursor 等安装 Agent 技能

### [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) ⭐ 6,810

> 装在手机上的AI对话副驾：读懂聊天、给出候选回复，发不发由你决定

- **定位**：Android无障碍服务读取QQ/X/飞书聊天界面，交给大模型判断意图并生成候选回复，一键填入输入框，发送与否由用户自己决定。
- **能做什么**：
  - 判断模型先分析对方意图、危险等级、是否该马上回，再起草3条候选回复
  - 无障碍服务只读屏幕内容，不hook、不改包、不碰App账号或数据库
  - 本地知识库与联系人档案，分析时自动带入命中的笔记和历史背景
  - 判断/回复/视觉三路接口可分别配置，支持OpenRouter等多家模型预设
  - 回复仅通过ACTION_SET_TEXT填入输入框，从不自动发送，不碰转账红包
- **亮点**：
  - 项目方称QQ、X真机全链路跑通，飞书靠离线OCR兜底；微信Android版已下架故不支持
  - 密钥、知识库与截图OCR均在本机完成不上传，但触发分析时聊天内容会发给用户自配的模型服务商
- **适合**：使用QQ、X、飞书聊天，希望AI辅助分析对方意图并起草回复、但仍要自己决定是否发送的Android用户
- **上手**：`adb install -r apk/jev-assistant-v1.4-release.apk` 安装后需在设置中填入判断接口API Key（如OpenRouter），并开启无障碍、悬浮窗、自启动权限
- ⚠️ 触发分析时聊天文字及启用的背景信息会发送给用户自行配置的第三方模型服务商，存在隐私数据外传
- ⚠️ 通过无障碍服务读取聊天App界面内容并辅助生成回复，可能涉及相关平台服务条款合规问题

### [aipoch/open-science](https://github.com/aipoch/open-science) ⭐ 5,159

> 本地优先、模型无关的开源 AI 科研工作台桌面应用

- **定位**：面向科研人员的桌面级研究工作台，用自然语言描述研究目标，由 AI 智能体调用工具、执行代码、查询科研数据，产出可追溯证据链的报告与图表。
- **能做什么**：
  - 内置23个科学技能，另有525个技能可从市场一键安装
  - 24个内置连接器，支持自定义本地/远程MCP连接器
  - 本地运行Python/R Notebook，支持SSH远程与Slurm提交
  - 产物版本不可变并附带溯源信息，可查看生成代码与执行证据
  - 可选Reviewer自动复核代理执行结果，给出通过/警告/失败判定
- **亮点**：
  - 项目方数据：在BiomniBench-DA Public 50对比中以79.05分排名第一
  - 文献库支持PDF管理、开放获取全文查找及图表提取
- **适合**：从事计算与数据密集型研究的科学家和研究者，涵盖生命科学、化学、材料、物理、环境科学等领域
- **上手**：`brew install --cask open-science` macOS可用Homebrew安装，其余平台从官网下载对应安装包，完成设置向导后即可创建项目开始研究

## 本地推理与模型

### [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) ⭐ 8,727

> 用纯C99在单CPU、8GB内存上运行2.78万亿参数Kimi K3模型的推理引擎

- **定位**：面向超大规模MoE模型的CPU推理引擎，通过流式加载1.45TB专家权重、LRU缓存和4bit量化，把1.56TB检查点压缩到8GB内存运行，不同内存预算下输出字节级一致。
- **能做什么**：
  - 无BLAS无框架无GPU依赖，纯C99代码可跨Linux/macOS/Windows移植
  - 密集主干层可流式读取，1.45TB路由专家权重不常驻内存按需读取
  - LRU缓存管理专家权重，配合4bit量化(MXFP4)和AVX2 SIMD内核
  - 提供laptop到server等多档内存预设，8GB到224GB均可运行
  - 内置测试套件，用PyTorch参考结果逐层验证推理正确性
- **亮点**：
  - 项目方数据：8GB内存下生成约32.69秒/token，127GB内存下约10.69秒/token
  - 不同内存预算（8GB~224GB）下生成结果字节级完全一致，仅速度不同
  - 完整检查点1.56TB，通过流式读取与打包主干把内存下限降到8GB
- **适合**：对底层推理引擎实现、CPU上运行超大MoE模型、系统编程感兴趣的工程师和研究者
- **上手**：`git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git && cd kimi-k3-in-c && make -j && make test` 该命令只构建并验证引擎，无需下载模型；实际生成文本需另外下载1.56TB检查点并打包主干层。

### [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) ⭐ 6,834

> 用Swift+Metal专为Gemma 4 26B打造的运行时，8GB内存Mac也能跑26B大模型

- **定位**：面向Apple Silicon Mac的模型专用推理引擎，通过流式加载专家权重把26B参数模型的内存占用压到约2GB，而非通用的MLX/llama.cpp包装器。
- **能做什么**：
  - 仅保留1.35GB共享核心与KV缓存常驻内存，按需从SSD流式加载专家权重
  - 提供原生Mac App、命令行CLI和本地OpenAI兼容Server三种使用方式
  - 支持视觉理解，需额外安装约1.1GB的图像模型包(M2及以上)
  - CLI和Server支持多轮对话、函数调用声明及采样参数自定义
  - 内置流式安装器，边下载边重打包为.gturbo格式，避免占用双份磁盘空间
- **亮点**：
  - 项目方数据：8GB M2 MacBook Air上解码速度5.1-6.3 tok/s，24GB M5 Pro上可达31-35 tok/s
  - 模型专用运行时而非通用推理框架包装器，针对Gemma 4 26B-A4B做了103项内核/缓存/IO优化实验
- **适合**：拥有Apple Silicon Mac(尤其8GB内存机型)、想在本地运行大模型又不想升级硬件的开发者和爱好者
- **上手**：`git clone https://github.com/drumih/turbo-fieldfare.git && cd turbo-fieldfare && swift build -c release && .build/release/TurboFieldfareMac` 首次运行需下载约15GB模型文件；仅支持macOS 26+Metal 4+Xcode 26的arm64 Apple Silicon Mac。

## Skills 与写作/设计

### [hypit-ai/hypit](https://github.com/hypit-ai/hypit) ⭐ 16,889

> 让 AI 智能体一键克隆爆款视频，批量产出可复用的完整制作工作流

- **定位**：Hypit 为 Claude Code、Codex 等编码智能体提供一套视频创作语言与系统，把参考视频克隆成可编辑、可重复运行的完整工作流，而非一次性成片。
- **能做什么**：
  - 克隆任意参考视频为完整工作流：镜头、字幕、B-roll、特效一并生成
  - 以词而非秒为时间锚点，修改文案后时间轴自动重排
  - 组件可插拔，可替换主播、字幕样式或自写自定义组件
  - 支持代码渲染视频，无需调用生成模型即可完成合成
  - 单次编排可衍生上百条变体，适配广告投放和多语言本地化
- **亮点**：
  - 开源免费，无席位费、渲染费或水印，仅模型服务按用量单独计费（项目方数据）
  - 自研 SVML 标记语言与编译器，把视频描述编译为可重跑的完整合成工程
- **适合**：需要批量制作短视频广告、UGC、社媒克隆视频的营销团队，以及使用 Claude Code、Codex 等编码智能体的开发者
- **上手**：`npx skills add hypit-ai/hypit -g` 安装为 Agent Skill 后在项目目录用 /hypit 指令让智能体克隆或新建视频，首次使用会自动检查并准备可执行程序
- ⚠️ 采用自定义的 Hypit Open Source License，非标准开源协议，使用前需自行确认条款
- ⚠️ 克隆他人短视频或广告素材制作衍生内容可能涉及版权或平台服务条款风险
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) ⭐ 11,451

> 一个 Claude/ChatGPT/Codex 技能，专门清除文字中 20 多种"AI 腔"套路

- **定位**：面向用 AI 辅助写作或编辑的用户，识别并去除"这不是X，而是Y"等 AI 套话模式，同时保留个人写作风格，可作为编辑器或检测器使用。
- **能做什么**：
  - 检测并清除二元对比、故作深刻等20多种AI套话模式
  - 支持纯编辑模式和仅检测不猜测模式
  - 保留原作者的词汇、语感和幽默风格
  - 可反向生成讽刺性AI套话文案娱乐用
  - 提供ChatGPT插件和Codex/Claude Code技能两种接入方式
- **亮点**：
  - GitHub星标超1万，上线两个月内迅速走红
- **适合**：用AI辅助写作、编辑文章或社交媒体内容，希望去除机械AI腔调、保留个人风格的写作者和内容创作者
- **上手**：`npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes` 安装后在Claude Code等工具中用 /no-ai-slop 加待编辑文字调用即可

### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) ⭐ 9,745

> 让 Claude Code / Codex 用 Remotion 自动产出电影感产品宣传视频的 Agent Skill

- **定位**：面向 Claude Code / Codex 的 Agent Skill，将模型变成动效设计工作室，用 Remotion 自动分镜、动画和音效设计出电影感产品宣传片
- **能做什么**：
  - 157 张分镜配方卡，含用途、时长、参数与实现要点
  - 214 种运镜风格与动效预览，可在在线 Gallery 搜索筛选
  - 内置 Ink Press 完整视频模板，36.2 秒 1920×1080 30fps
  - 交付后可用浏览器 Motion Workbench 继续剪辑并用 Remotion 导出
  - 支持导出为剪映（JianYing CN）工程，可二次编辑字幕与音轨
- **亮点**：
  - 提供 157 张结构化分镜配方卡和对应 Remotion 组件实现，而非单纯的提示词模板
  - 内置真实产品截图 2.5D 运镜、卡点音效和 149 条分类 SFX 素材
- **适合**：使用 Claude Code / Codex 制作产品宣传视频的开发者、独立开发者和营销/设计人员
- **上手**：`npx skills add Vincentwei1021/video-shotcraft` 也可直接把仓库链接发给 Agent 让其自动安装，或 clone 后软链到 ~/.claude/skills 目录
- ⚠️ Remotion 本身有独立许可证，个人和小团队免费，公司使用可能需付费授权
- ⚠️ 模板中的产品截图为演示素材，发布前需自行替换并核查是否含需匿名化的数据
- ⚠️ 音频素材来自 Mixkit 等来源，需遵守各自许可条款

### [jakubkrehel/skills](https://github.com/jakubkrehel/skills) ⭐ 7,277

> 一套面向 AI Agent 的界面设计技能集，帮助打造更好的 UI

- **定位**：为 Claude 等 Agent 提供可插拔的设计技能包，覆盖 UI、排版、色彩、无障碍、布局与文案，让 Agent 按专业标准审查和改进界面。
- **能做什么**：
  - better-ui 涵盖圆角、光学对齐、图标、点击区域、动画等界面细节
  - better-typography 处理字号、间距、可变字体、断行截断等排版问题
  - better-colors 生成调色板、语义化 token 并检查对比度
  - better-accessibility 帮助项目符合无障碍标准
  - interface-review、break、variant 支持界面审查与多方案迭代
- **亮点**：
  - 作者将个人设计工程博客 Interfaces 的内容整理成可复用技能
  - 可作为 Claude Code 插件直接安装使用
- **适合**：使用 Claude 等 Agent 工具进行前端/UI 开发的设计工程师和开发者
- **上手**：`npx skills add jakubkrehel/skills` 也可作为 Claude Code 插件安装：/plugin marketplace add jakubkrehel/skills

### [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) ⭐ 5,749

> 面向 AI Agent 的数据可视化 Skill，一键把数据变成精致可交互的 HTML 图表

- **定位**：面向 AI Agent 的数据可视化 Skill，遵循 Agent Skills 格式，让 Claude Code、Codex 等 Agent 把数据自动生成为有编辑设计感的可交互 HTML 图表或整页报告。
- **能做什么**：
  - 49 种图型：Lupi 编辑叙事型、Glance 快速判断型、Basics 基础型三套视觉体系
  - 提供 12 套中英双语整页报告模板，覆盖年报、周报、dashboard 等场景
  - 内置 Mono 及青瓷蓝、椰林绿、编辑部红三种彩色预设，Agent 可自动选色
  - 支持网络图、路径图等独立交互大图，基于 SVG/Chart.js/ECharts 实现
  - 遵循 Agent Skills 格式，可安装到 moxt、Claude Code、Codex 等兼容 SKILL.md 的工具
- **亮点**：
  - GitHub 5500+ star，专注把数据转成有编辑设计感的 HTML 图表而非通用图表库
  - 设计规则围绕数据契约展开：先判断数据结构再选图型，而非先选模板
- **适合**：需要用 AI Agent 快速生成图表和报告的内容创作者、分析师及 Claude Code/Codex 用户
- **上手**：`npx skills add https://github.com/larashero3-dotcom/lieflat-charts --skill lieflat-charts` 安装后直接对 Agent 描述数据和用途即可生成图表；推荐在 moxt.ai 中使用以获得完整工作区体验。
- ⚠️ 采用 PolyForm Noncommercial License，仅限学习和非商业使用，商业使用需另行取得许可
- ⚠️ 部分图表模板通过 CDN 加载 Chart.js/ECharts，离线环境无法完整显示
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) ⭐ 5,614

> 面向AI Agent的极简可爱IP吉祥物/Logo生成技能包

- **定位**：遵循开放Agent Skills格式的指令文档，指导兼容AI Agent（需搭载顶尖图像模型）生成极简、圆润、带轻微新拟物质感的公司吉祥物形象，不绑定特定Agent产品。
- **能做什么**：
  - 主体由4-7个大块基础形状构成，严格限制视觉复杂度
  - 默认三色方案：两个主体色加一个命名纯色背景
  - 主体固定从左下或右下角凸显，占比约85%-95%
  - 用户确认方向后自动生成三方向共六张独立候选图
  - 兼容Codex、Doubao、Coze、Manus、Gemini Apps等Agent
- **亮点**：
  - 官网ipaslogo.com提供免费商用Logo库，无需自备兼容Agent即可下载
  - 仓库仅含单个SKILL.md指令文档，无脚本或生成依赖，轻量易安装
- **适合**：需要快速产出品牌吉祥物或Logo草案的产品设计师、独立开发者，以及已在使用Codex等AI Agent的团队
- **上手**：`npx skills@latest add s1dashu/ip-as-logo-skill` 安装后需在兼容Agent中启用顶尖图像模型（如GPT Image 2、Nano Banana Pro）才能实际生成图像
- ⚠️ 生成效果依赖第三方图像模型且具随机性，项目方不做合规或质量自动校验
- ⚠️ 已 37 天未更新

### [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) ⭐ 5,182

> 面向求职场景的九个 AI Skill 插件包，覆盖简历、投递、面试全流程

- **定位**：面向 Claude Code、Codex 等 AI Agent 平台的求职技能插件包，提供从开源贡献积累经历、简历制作、岗位匹配到投递填表、面试演练、进度管理的九个可单独调用入口。
- **能做什么**：
  - /contributor 寻找开源问题、核对贡献规则后辅助提交 PR 积累经历
  - /great-resume 与 /make-resume 完成岗位定位改写并生成可编辑 HTML 简历
  - /job-match 对照 JD 生成要求-证据矩阵和投递建议
  - /job-apply 连接浏览器自动填写招聘申请表，停在提交前供用户核对
  - /interview 与 /offer 支持追问式面试演练和校招投递进度跟踪
- **亮点**：
  - 同时支持 Codex、Claude Code、TraeWork、Qoder、Cursor 等多平台安装
  - 强调事实边界，不编造经历数据，关键操作均需用户逐项确认后才提交
- **适合**：求职中的学生和开发者，尤其是需要系统整理项目经历、制作简历、准备面试的求职者
- **上手**：`/plugin marketplace add Hisn00w/ASu-skills` 适用于 Claude Code，安装后执行 /plugin install asu-skills@asu 并按提示 reload-plugins
- ⚠️ /job-apply 涉及自动化操作已登录浏览器填写招聘网站表单，需留意平台服务条款风险
- ⚠️ /contributor 会代为提交开源 PR，需确保符合目标仓库的贡献规范，避免滥用

## 开发者工具与集成

### [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) ⭐ 22,967

> 去除AI生成内容水印与溯源标记的Agent Skill及本地服务

- **定位**：面向Claude Code、Cursor、Grok等Agent主机的Skill/插件，配合纯Python本地服务，清除自有文本与文件中的多厂商AI水印和溯源标记。
- **能做什么**：
  - 支持Claude、Gemini/SynthID、OpenAI等多厂商水印检测与清除
  - 覆盖图片、文档、音视频等二十余种文件格式的C2PA/EXIF/XMP元数据清理
  - 提供PostToolUse钩子，在Agent写文件时自动检测或清理水印
  - 纯Python标准库实现无需额外依赖，一条命令即可启动本地服务
  - 支持Claude Code插件市场、Cursor、Grok等多种主机的安装方式
- **亮点**：
  - 同时处理不可见Unicode字符、统计型文本水印和文件元数据三类溯源标记
  - 提供确定性钩子而非仅依赖模型指令，保证Agent写文件时的清理可靠执行
- **适合**：使用AI生成工具创作、需要清理自有内容中溯源标记的开发者、创作者及Agent工具集成者
- **上手**：`python3 install_skill.py --skill remove-ai-marks --target claude-code` 安装Skill后还需运行make serve启动本地HTTP服务，Skill通过HTTP调用该服务完成实际清理
- ⚠️ 用于去除AI生成内容的溯源与水印标识，可能涉及AI内容标识相关法规合规问题

### [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) ⭐ 12,212

> 让Codex的模型选择器直接调用你的ChatGPT网页版账号（含Pro），不占用Codex额度

- **定位**：通过浏览器自动化和MCP，把ChatGPT网页版账号（含Pro）接入Codex原生模型选择器，使用网页版独立的用量额度，同时保留上下文、工具调用、流式与图片能力。
- **能做什么**：
  - 浏览器自动化登录ChatGPT网页版，作为Codex原生模型直接使用
  - Full harness模式通过MCP和OpenAI tunnel-client把ChatGPT工具调用接回Codex当前任务
  - 提供仅浏览器自动发送、完整harness带工具、零风险手动粘贴三种模式
  - 自带浏览器与运行环境，无需单独安装Chrome、Node或Bun
  - 按账号类型（Free/Go、Plus、Pro）自动识别可用的模型档位
- **亮点**：
  - 项目方称使用ChatGPT网页版独立用量额度，不消耗Codex或Work自身配额
  - 官方明确说明这是非官方浏览器自动化方案而非OpenAI API，界面变动可能导致功能失效
- **适合**：希望在Codex里用自己ChatGPT Plus/Pro账号能力、且能接受浏览器自动化方案的开发者
- **上手**：`git clone https://github.com/miuuyy/codex-chatgpt-web.git && cd codex-chatgpt-web && bun run app` 该路径需要Bun 1.4.0；也可用官方脚本一键安装启动器（提供macOS/Linux/Windows安装命令）
- ⚠️ 依赖浏览器自动化操作个人ChatGPT账号页面，可能违反OpenAI服务条款并存在封号风险
- ⚠️ 安装包尚未做平台签名，安装时macOS Gatekeeper或Windows SmartScreen会发出警告
- ⚠️ 浏览器登录状态是敏感凭证，本机同用户进程可访问，需在受信任设备使用

### [trailhq/Graft](https://github.com/trailhq/Graft) ⭐ 9,320

> 给 Claude Code、Cursor 等编码 Agent 装上代码知识图谱，减少重复探索代码库

- **定位**：Graft 为代码库构建一份可读的 Markdown 知识图谱，写入仓库供各类编码 Agent 直接读取，避免每次任务从零探索代码，从而更省钱、更快、更准确。
- **能做什么**：
  - graft init 自动为 Claude Code 等 Agent 接入统计栏、钩子和 MCP 配置
  - 两阶段构图：LLM 总结每个文件，再分组成带类型链接的节点
  - 结构层用 tree-sitter 解析，$0 成本、无需模型密钥，支持23种语言
  - 每次查询前自动增量刷新图谱，反映未提交的最新代码改动
  - graft/ 目录作为本地可再生缓存不提交，团队成员各自 build 生成
- **亮点**：
  - 项目方基准测试：工具调用减少46%，token节省42%，耗时减少60%
  - 项目方SWE-bench Verified测试：正确率从54%提升到66%（+12分）
  - 支持OpenAI、Anthropic、OpenRouter等多家模型提供商，可用自有API密钥
- **适合**：使用Claude Code、Cursor、Codex、Gemini等AI编码助手的开发者和团队
- **上手**：`npm install -g @nanonets/graft && graft init` 安装后运行graft init选择要接入的编码Agent，自动构建图谱并完成配置

## 安全相关

### [MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct) ⭐ 8,894

> 针对 Codex/GPT 的越狱提示词与配套自动化评测工具包

- **定位**：面向 Codex CLI 的破甲提示词项目，维护稳定版与新版两条产品线，配合部署脚本和 A/B/C 三级回归测试门禁验证提示词效果。
- **能做什么**：
  - 提供 gpt-5.6-sol-v45 稳定版与 gpt-6-astra-v1 正式版两条提示词产品线
  - codex-instruct.py 脚本支持一键部署、预览（--dry-run）和回滚（--reset）
  - A/B/C 三级发布门禁，含 66 例 Issue 回归测试与 120 例原始测试样例
  - 保留历史版本、SHA 校验值和测试证据，强调可复现的评测流程
- **亮点**：
  - 项目方数据：gpt-6-astra-v1 全量 B 测试通过 52/66 cases、60/74 turns
  - README 明确声明不用于商业化，定位为提升 AI 安全的研究项目
- **适合**：研究或使用 Codex/GPT 越狱提示词、关注 LLM 安全测试方法论的开发者和安全研究人员
- **上手**：`git clone https://github.com/MDX-Tom/gpt-instruct.git` clone 后运行 codex-instruct.py --apply 部署提示词到 Codex 配置，支持 --dry-run 预览
- ⚠️ 项目本质为绕过 AI 模型安全限制的越狱（破甲）提示词
- ⚠️ README 明确提示破甲活动存在账号封禁风险，建议使用日抛账号

### [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) ⭐ 6,267

> 多智能体自动化红队框架，把你的AI编程Agent变成渗透测试军火库

- **定位**：复用本地已在使用的AI编程Agent（Claude Code、Codex等）或离线本地模型作为决策大脑，驱动侦察-利用-报告全流程渗透测试，无需额外API密钥。
- **能做什么**：
  - 调用本地已登录的AI编程Agent或Ollama/LM Studio等离线模型作为大脑，无需新密钥
  - 覆盖Web应用、CTF、源码审计等成熟场景，云、移动、二进制等仍为脚手架阶段
  - 提供War Room浏览器界面和CLI两种操作方式
  - 内置verify-claims命令，一键从提交数据复现README中所有基准结果
  - 支持Docker部署，服务默认仅绑定127.0.0.1本地地址
- **亮点**：
  - 项目方数据：在XBOW官方104题挑战集上pass@1达90.1%，高于XBOW自评的85%
  - 所有基准数字可通过npm run verify-claims从公开提交的原始数据复现，27项全部通过
- **适合**：已获得授权的安全研究员、渗透测试人员和红队从业者
- **上手**：`npm install
npm run server` 启动后访问 http://127.0.0.1:3333/ui/ 打开War Room，在设置中连接本地Agent或配置模型密钥
- ⚠️ 这是进攻性安全工具，仅限对已获得明确书面授权的目标使用，未授权访问计算机系统在多数司法辖区属违法行为
- ⚠️ 使用第三方托管模型（如Novita）时会将目标数据和提示词发送至该服务商，需自行评估隐私和数据安全风险

## 其他

### [bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book) ⭐ 5,438

> 从硬件约束与模型架构出发，量化推导 LLM 推理训练系统设计的开源书稿

- **定位**：《深入理解 AI Agent》作者的姊妹篇，用量化估算方法系统讲解 LLM 推理与训练系统设计，覆盖加速器、算子、网络、调度等十二章内容，配套计算工具与实验代码。
- **能做什么**：
  - 十二章覆盖模型架构、加速器、算子运行时、数据中心网络、推理与训练系统等主题
  - 配套 Python 计算工具可复算书中数字，也可替换模型和硬件重新估算
  - 按章节组织实验代码与运行记录，需 GPU 的实验注明硬件与依赖
  - 提供简体中文、英文、繁体中文三语 PDF、EPUB 及在线阅读版本
  - 全书正文为 Markdown，持续开源修订，欢迎勘误与翻译贡献
- **亮点**：
  - 姊妹篇《深入理解 AI Agent》在 GitHub 获得 45k+ Star（项目方数据）
  - 方法论强调"从约束推导设计"：先算硬件理论上限，再对照实测找差距来源
- **适合**：已调用或部署过大模型、想弄清推理训练系统底层原理的应用工程师、系统/网络/芯片工程师及相关研究者
- **上手**：`git clone https://github.com/bojieli/ai-infra-book.git` 克隆后可用 calc.py 复算书中算例，静态计算仅需 Python 3.10+ 标准库，无需 GPU 或模型权重
