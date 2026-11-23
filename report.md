# GitHub AI 热门项目周报 · 第 10 期 · 2026-11-23：新上榜 8 · 移出 5

- 收录：2026-08-25 至 2026-11-23 创建、Stars > 5,000 的 AI 项目，共 59 个

## 近期趋势

本期加速集中在安全测试与软件复刻：ARTEX 由 +2351 升至 +12542，Claude-BugHunter 由 +1300 升至 +11684，security-audit-skill 仍在数千增量，加上新星 sapper-v2，两个以上项目佐证，攻防测试成为方向。rust-anything 新入榜即 +8219，fast-anything 新星 2399，两者都以「Agent 改写为 Rust 并验证行为一致」为路径，延续编码 Agent 的能力边界扩张。编码 Agent 的远程统一控制延续升温：t3code 由 +9058 升至 +11024，orca 由 +6645 升至 +7669。前几期的视频与 3D 产出仍有新证据：openmotion 加速、phonebox 加速，但 rea 由 +18479 降至 +12476、modern-web-guidance 由 +15904 降至 +6671，热度回落一句带过。

- ARTEX 由 +2351 加速至 +12542，Claude-BugHunter 由 +1300 加速至 +11684，安全测试方向升温。
- rust-anything 新入榜 +8219，fast-anything 新星 2399，Agent 改写 Rust 并验证一致成为新路径。
- t3code 由 +9058 升至 +11024，orca 由 +6645 升至 +7669，编码 Agent 远程统一控制延续升温。
- openmotion 加速至 +5530、phonebox 加速至 +3747，视频与设备复用方向延续。
- rea 由 +18479 降至 +12476，modern-web-guidance 由 +15904 降至 +6671，前几期热点回落。

## 本期变化
较第 9 期（2026-11-16，7 天）：
- 新上榜：BaaRai/ARTEX、erkamyaman/rust-anything、mdiri-ai/SoduWork、haydenschmitty/floorplan、vAPI-Network/vapi-network、Leonxlnx/earshot、Likely7/Veyra-NRVideo、ersinkoc/phonebox
- 移出：larashero3-dotcom/lieflat-less-ai-tone（创建于 2026-08-20，已超出 90 天收录窗口）；s1dashu/ip-as-logo-skill（创建于 2026-08-18，已超出 90 天收录窗口）；ApodexAI/FrontierAgent（创建于 2026-08-22，已超出 90 天收录窗口）；totec448-spec/chat-on-steroids（创建于 2026-08-22，已超出 90 天收录窗口）；nateherkai/scroll-craft（创建于 2026-08-22，已超出 90 天收录窗口）
- 涨星：Ebony-Vinyl/dsh-our-free-model +8,024、ccch1mneyyy/dsh-Go +6,298、kajisho5/ffmpeg-skill +3,852、heydamir/unslop +3,564、lemomo-ai/lemo-opuscar +3,118

## 升星榜（近 7 天 11-16 至 11-22，对比前 7 天 11-09 至 11-15）

测了 868 个近一年创建的 AI 项目：近 7 天涨星 ≥1,000 的 115 个，≥2,000 的 54 个，≥5,000 的 17 个；18 个在加速，69 个创建已超过 90 天，26 个已在主榜。

### 暴涨（近 7 天 ≥5,000）
- [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX) **+12,542**（前 7 天 +2,351，现 16,686★）　加速　主榜：自托管、由 LLM 驱动、带证据留痕的自主渗透测试平台
- [morluto/rea](https://github.com/morluto/rea) **+12,476**（前 7 天 +18,479，现 474,644★）：面向 AI Agent 的逆向工程 MCP，覆盖二进制、应用与运行时行为
- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) **+11,684**（前 7 天 +1,300，现 18,502★）　加速：Claude Code 漏洞挖掘技能包，含 82 项技能与红队攻击矩阵
- [pingdotgg/t3code](https://github.com/pingdotgg/t3code) **+11,024**（前 7 天 +9,058，现 72,941★）：在任意电脑或手机上统一控制 Claude Code、Codex 等编码 Agent，支持远程与 Git。
- [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) **+8,755**（前 7 天 +10,318，现 84,432★）　主榜：dsh 插件：免登录、免 Key 接入免费模型并本地转发
- [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything) **+8,219**（前 7 天 +0，现 8,230★）　主榜：录制原应用行为，让编程 Agent 分块改写为 Rust 并逐块验证一致
- [stablyai/orca](https://github.com/stablyai/orca) **+7,669**（前 7 天 +6,645，现 133,574★）：在桌面、手机和远程运行环境中编排 Codex、Claude Code 等编码代理。
- [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) **+6,671**（前 7 天 +15,904，现 25,226★）：让编码 Agent 掌握最新 Web 最佳实践的技能包，由 Chrome 等浏览器团队维护。
- [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) **+6,338**（前 7 天 +7,457，现 30,439★）　主榜：DeepSeek Harness 的 Android 客户端，手机本机运行或远程遥控电脑上的 DSH
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork) **+5,895**（前 7 天 +964，现 6,880★）　加速　主榜：可自托管的团队 AI Agent 编排引擎，多 harness 协作并按验收标准交付
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) **+5,611**（前 7 天 +4,758，现 197,100★）：让 AI 编码代理像最懒的资深开发者那样，写刚好够用的代码。
- [mattpocock/skills](https://github.com/mattpocock/skills) **+5,602**（前 7 天 +6,765，现 330,830★）：Matt Pocock 的轻量可组合代理技能，帮助编码代理做真实工程而非氛围编程。
- [nexu-io/openmotion](https://github.com/nexu-io/openmotion) **+5,530**（前 7 天 +544，现 15,517★）　加速：开源代理式动效视频工作室，参考视频一键复刻并导出短视频。
- [affaan-m/ECC](https://github.com/affaan-m/ECC) **+5,479**（前 7 天 +4,454，现 309,186★）：为 Claude Code 等代理提供规划、测试、记忆与安全优化的工程化技能系统。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) **+5,326**（前 7 天 +6,354，现 116,738★）：本地开源 ElevenLabs 替代，支持克隆、配音、转录与有声书
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) **+5,286**（前 7 天 +806，现 73,005★）　加速：AI 代理技能：跨 Reddit、X、YouTube 等研究话题并生成有据总结。
- [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) **+5,076**（前 7 天 +768，现 6,029★）　加速：多代理框架，将研究素材自动写成可投稿的 LaTeX 论文。

### 猛涨（近 7 天 2,000–4,999）
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) **+4,336**（前 7 天 +340，现 63,065★）　加速：为各类软件生成 CLI，让 AI 代理直接操控现有软件。
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) **+4,093**（前 7 天 +4,548，现 59,721★）：让 Claude Code、Cursor 等编码代理生成不像 AI 模板的网页设计技能。
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) **+4,016**（前 7 天 +4,347，现 120,325★）：给编码代理艺术方向、真实图片和浏览器自检的网页设计技能。

其余 95 个：tashfeenahmed/freellmapi +3,929、cloudflare/security-audit-skill +3,921、kajisho5/ffmpeg-skill +3,849、Tencent/LoopForge +3,849、ersinkoc/phonebox +3,747、Graphify-Labs/graphify +3,728、heygen-com/hyperframes +3,709、simplexai-labs/linger +3,640、heydamir/unslop +3,575、alibaba/open-code-review +3,157、lemomo-ai/lemo-opuscar +3,135、cathrynlavery/diagram-design +3,125、yetone/magpie +3,061、JuneYaooo/rea-video +3,032、nextlevelbuilder/ui-ux-pro-max-skill +3,020、blader/humanizer +2,944、Immortal-Protocols/lastbook +2,890、GoogleChrome/modern-web-guidance-src +2,805、bookwjitchieni1986/blender-ai-mcp-addon +2,758、Likely7/Veyra-NRVideo +2,645、google-labs-code/stitch-skills +2,581、XinaTian/MROffice +2,490、backnotprop/plannotator +2,467、EL4CTEO/fast-anything +2,359、open-jarvis/OpenJarvis +2,353、google/elephant-goldfish-model +2,325、Alishahryar1/free-claude-code +2,231、iamajmeena/neonclipping +2,178、hugohe3/ppt-master +2,161、Panniantong/Agent-Reach +2,034、tt-a1i/archify +2,031、ifixai-ai/iFixAi +2,013、sybil-solutions/inference-optimisation-skill +2,006、Lee-xeo/Claude-Cage +2,002、paperclipai/paperclip +1,967、Vincentwei1021/video-shotcraft +1,939、AgriciDaniel/claude-seo +1,934、cheaper-inference/OmniRoute +1,931、vercel-labs/agent-desktop +1,915、shinyobjectz/raea +1,909、nightly-labs/openbot +1,896、addyosmani/agent-skills +1,882、xerj-org/xerj +1,818、JuliusBrussee/caveman +1,812、multica-ai/andrej-karpathy-skills +1,809、jub0t/Concat +1,793、OpenMontageInc/OpenMontage +1,793、vercel-labs/agent-browser +1,768、haydenschmitty/floorplan +1,752、Jakeschincariol/instagram-agent-skill +1,745、Tracer-Cloud/opensre +1,731、janestreet/agent_skills +1,727、atuizz/posewear +1,713、dataelement/dsh-desktop +1,644、amosblomqvist/learnharness +1,590、vercel-labs/ui +1,539、coreyhaines31/marketingskills +1,517、career-ops-hq/career-ops +1,485、EL4CTEO/blender-skills +1,484、ZiChuanLan/freebie-radar +1,427、gamedev-skills/awesome-gamedev-agent-skills +1,403、openfilm/openfilm +1,400、h4ckf0r0day/obscura +1,386、NVIDIA/auto-ontology +1,360、agent-substrate/substrate +1,353、n8n-io/nod +1,350、nexu-io/open-design +1,337、haziqahmedqasmi/PeakCut +1,307、ethanplusai/sellbird +1,299、FrigadeHQ/yogurt +1,289、wheresryan22/anatomy +1,252、RainBowLuoCS/Gamer +1,240、VaneAi888/vane-gpt-image-skills +1,233、ZhuLinsen/daily_stock_analysis +1,233、microsoft/TokenEconomizer +1,222、herdrdev/herdr +1,206、ai-job-search-dev/ai-job-search +1,189、Jakeschincariol/day-trader-skill +1,183、patch-gg/pixelfx +1,174、multica-ai/multica +1,165、hypit-ai/hypit +1,146、Imbad0202/academic-research-skills +1,136、huggingface/pybot +1,126、Zagitta/gpu-unlock +1,101、citrolabs/ego-lite +1,093、FailproofAI/failproofai +1,079、VoltAgent/awesome-design-md +1,068、NVIDIA/SkillSpector +1,067、kaomei/stickman-video-director +1,065、Donchitos/Claude-Code-Game-Studios +1,033、modelflare-ai/AnyModelBot +1,030、beenuar/AiSOC +1,027、mromidev/claude-animated-shorts +1,026、jiwoochris/artex-global +1,022、Egonex-AI/Understand-Anything +1,016

## 新星（创建于 11-16 至 11-22，≥500★）

**≥2,000★**
- [bookwjitchieni1986/blender-ai-mcp-addon](https://github.com/bookwjitchieni1986/blender-ai-mcp-addon) ★ 2,758：Blender 里的 AI 助手与 MCP 服务，让模型查看场景、建模、改材质并执行多步流程
- [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything) ★ 2,399：定位 Python/Node/Ruby 热点函数，让编码 Agent 用 Rust 重写并验证行为一致
- [iamajmeena/neonclipping](https://github.com/iamajmeena/neonclipping) ★ 2,187：本地开源剪辑工具，把长视频自动切成带字幕的竖屏片段，配本地 LLM 选题
- [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill) ★ 2,009：Agent skill for hill-climbing local LLM serving speed (decode, speculative decoding, prefill, KV, startup, TTFT) on any hardware and quantization

**500–999★**
- [pierridotite/mobile-agent-testers](https://github.com/pierridotite/mobile-agent-testers) ★ 954：在 GitHub 免费 runner 上并行跑多个 Claude Code Agent，探索式测试移动 App 并报 Bug
- [boringmarketer/boring-marketing-skills](https://github.com/boringmarketer/boring-marketing-skills) ★ 801：面向 AI Agent 的 32 个营销技能：调研、定位、文案、SEO、广告与内容
- [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast) ★ 642：给 Google Antigravity 用的本地 MCP 加速插件，批量合并检索与编辑以省 token 和延迟
- [danielwh2/sprite-stacking](https://github.com/danielwh2/sprite-stacking) ★ 542：Agent 技能：把四视图像素画堆叠成可旋转的伪 3D 精灵，用于游戏开发

## 新锐（创建于 10-24 至 11-15，≥1,000★）

- [modelflare-ai/AnyModelBot](https://github.com/modelflare-ai/AnyModelBot) ★ 4,980：本地优先的个人 AI Agent，跨模型并接入微信飞书
- [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) ★ 4,623：Claude 技能：用 three.js 与 Remotion 在本地渲染竖屏动画短片
- [t3dotgg/tstack](https://github.com/t3dotgg/tstack) ★ 4,309：作者日常使用的 Agent 技能集，覆盖提 PR、评审、合并与接管等开发流程。
- [elvarofficial/teardown](https://github.com/elvarofficial/teardown) ★ 4,051：Claude Code 技能：把任何机器做成可拆解的 3D 模拟器
- [benjitaylor/skills](https://github.com/benjitaylor/skills) ★ 4,022：面向 AI 编码 Agent 的设计与动效技能合集
- [simplexai-labs/linger](https://github.com/simplexai-labs/linger) ★ 4,018：完全跑在本机的开源个人 Agent，主动记忆办事，数据不出设备
- [FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt) ★ 3,007：本地运行、隐私优先的 AI 会议记录与摘要工具，Granola 的开源替代
- [Immortal-Protocols/lastbook](https://github.com/Immortal-Protocols/lastbook) ★ 2,978：离线生存知识库，整合手册、视频、百科、地图与本地问答，供断网时查用
- [paipiange/nvzhuang](https://github.com/paipiange/nvzhuang) ★ 2,971：1407 张 AI 女装图集网站，支持 AI 虚拟试穿换装
- [sarpstar/cinecode](https://github.com/sarpstar/cinecode) ★ 2,892：AI 编码 Agent 写脚本并用代码构建每一帧，输出成片 MP4
- [caru-ini/stack-diagram](https://github.com/caru-ini/stack-diagram) ★ 2,783：Agent 技能：一句话描述技术栈，生成带官方 logo 的架构图
- [DenisSergeevitch/ex-ussr-kinship-research](https://github.com/DenisSergeevitch/ex-ussr-kinship-research) ★ 2,738：面向 AI Agent 的前苏联家谱研究技能，检索教会簿册、民事与军事档案并标注证据。
- [DIYgod/pinky](https://github.com/DIYgod/pinky) ★ 2,695：让 AI Agent 通过 MCP 操作真实手机，并由你在环内审批
- [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2) ★ 2,567：自主渗透测试多智能体编排框架，指挥官加 Worker 集群协同作战
- [XinaTian/MROffice](https://github.com/XinaTian/MROffice) ★ 2,523：开源 Office 风格在线编辑器合集，内置 Copilot 与 MCP 服务，可让 AI 读写真实文档
- [wquguru/cicada](https://github.com/wquguru/cicada) ★ 2,471：跨平台实时字幕、同声传译与 AI 会议纪要工具
- [Motionsites-AI/claude-skill](https://github.com/Motionsites-AI/claude-skill) ★ 2,460：免费 Claude 技能：让 Claude 做出电影级落地页
- [ZiChuanLan/freebie-radar](https://github.com/ZiChuanLan/freebie-radar) ★ 2,367：聚合多源福利信息并用 AI 二次审核过滤的工具，通过 Telegram 推送
- [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) ★ 2,285：Claude Code 技能：逐帧逆向复刻网页动画并对齐验证
- [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d) ★ 2,236：面向 LLM 的 Python 建模库，用简短代码在 Blender 中构建 3D 对象
- [andyhuo520/digital-human-koubo](https://github.com/andyhuo520/digital-human-koubo) ★ 2,082：给 AI Agent 的一张照片生数字人口播视频技能包
- [ZiChuanLan/agent-purge](https://github.com/ZiChuanLan/agent-purge) ★ 2,064：为多种编码 Agent 统一替换或注入系统提示词，带本地 Web 控制台

1,000–1,999★ 的 29 个：agentes-chat/agentes-chat ★1,964、daveebbelaar/bama ★1,950、jacke-pp/open-yoki ★1,871、JosssphZhou/poki ★1,866、atuizz/posewear ★1,834、haziqahmedqasmi/PeakCut ★1,790、anonnerdfrenzy/survival-llm ★1,724、voyager-so/vork ★1,694、RunanywhereAI/trnrt ★1,659、VaneAi888/vane-gpt-image-skills ★1,457、XiaoyeCodes/code-animation-prompts ★1,436、RainBowLuoCS/Gamer ★1,378、emanuele-em/kanzo ★1,320、RikiyaT/lm_understand-logs ★1,288、konlu/story-studio ★1,232、Minglink/dsh-jailbreak-workflow ★1,218、JDhruv14/line-art-animation ★1,188、kubai087/kubai-icons ★1,174、alexeyw/lot-map ★1,132、rerun-build/rerun ★1,129、huggingface/pybot ★1,128、hyperionaidev/smolmaxxing ★1,111、artemnovitckii/claude-animation-skills ★1,108、Dodaios/ste80-humanizer ★1,092、anthropics/FlashProve ★1,090、jackwener/DSH-Android ★1,035、op7418/dsh-guizang-design ★1,031、wzc520pyfm/gen-ai-pose-image ★1,007、anomalyco/browse ★1,002

## 名录

### 编程 Agent 与运行框架

#### [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) ⭐ 24,306

> 监听 GitHub 的主动式编码 Agent 研究原型，以 DeepSeek Harness 插件包形式运行

- **定位**：项目方自述这是研究原型而非 DeepSeek 官方产品，代码不保证达到生产可用标准；它为单个 GitHub 仓库服务，收到授权成员的请求后自行建立工作项、在独立会话和目录中执行，并回到原对话中答复。
- **能做什么**：
  - 监听 GitHub，可选接入飞书，识别授权用户的任务请求
  - 为每个请求建立工作项，使用独立 Agent 会话与目录执行
  - 在原始对话中回复结果，例如提交拉取请求
  - 提供网页面板，展示需要人工处理的事项
  - 仅在被请求或团队规则允许时行动
- **亮点**：
  - 项目方称多数工程由编码 Agent 完成
  - 安装配置由编码 Agent 按 SETUP.md 逐步引导完成
  - 设计原则是占用尽量少的人工注意力
- **适合**：研究自主 Agent 架构的开发者，以及愿意用研究代码自建仓库级编码 Agent 的团队
- ⚠️ 项目方声明这是研究原型，可能存在缺陷，需自行审查和调整后再使用
- ⚠️ 该原型与同团队论文描述的实现并不一致，论文中部分设计尚未实现

#### [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) ⭐ 9,841

> 让 Claude 等编程 Agent 为任意 PC 游戏做 Mod 的技能包与工具集

- **定位**：以 Agent Skills 加 fal MCP 和 um CLI 的形式，把侦察、逆向、建 Mod、生成素材、游戏内验证、录视频、写经验笔记串成 Agent 可执行的固定流程，支持 Claude Code、Codex、Gemini CLI、Cursor 等。
- **能做什么**：
  - 固定十步流程：检索知识库、侦察选路、备份存档、读代码、做最小切片、生成素材、游戏内验证、录制、打包、写笔记
  - 用 fal 生成图像、3D、音频素材，也可接本地 ComfyUI
  - knowledge/ 收录各游戏实际 Mod 经验笔记，结束可提 PR 共享
  - 提供 um CLI，可搜索知识库、新建和检查笔记
  - 自带三个子 Agent 编排长周期 Mod，token 消耗为数倍
- **亮点**：
  - 示例含 Terraria 的 Fal Arsenal、帝国时代 II 新文明、GTA V 内跑 Minecraft
  - 拒绝注入带反作弊的在线游戏，不做对抗其他玩家的作弊
  - 不附带游戏文件或反编译产物，改动前备份存档
- **适合**：想用 AI Agent 给自有 PC 游戏做 Mod 的玩家与 Mod 作者，需熟悉命令行与游戏引擎概念。
- **上手**：`/plugin marketplace add rehan-remade/universal-modder` Claude Code 中先加市场，再执行 /plugin install universal-modder@universal-modder；其他 Agent 各有对应安装方式。
- ⚠️ 对游戏程序做注入与逆向改动，可能违反部分游戏的用户协议或服务条款
- ⚠️ 生成的素材来自 fal 等外部付费服务，需自行确认版权与商用授权

#### [zai-org/ZCode](https://github.com/zai-org/ZCode) ⭐ 8,851

> Z.ai 推出的 AI 编程工作台，含桌面端、Web 端和终端 Agent。

- **定位**：ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent；本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。
- **能做什么**：
  - 桌面版基于 Electron，另有 Web 客户端
  - 命令行版 zcode 统一启动 TUI、Web 与 Agent
  - 支持 SSH/WSL 远程项目，资源经 SFTP 上传
  - 提供 UI Plugin 机制与 Excalidraw 示例
  - workspace 拆分桌面、Web、服务端与共享 UI
- **亮点**：
  - 命令行版默认监听 127.0.0.1，可选 --web 启动浏览器界面
  - 监听非本机地址时默认生成访问令牌，可用 --no-token 关闭
  - Agent CLI 与运行时源码随仓库一并克隆，无需单独初始化
- **适合**：想本地开发和二次构建 AI 编程 Agent 客户端的开发者，需熟悉 Node.js、pnpm 与 Electron。
- **上手**：`pnpm bootstrap` 需先准备 Git、Node.js 24.14.0 和 pnpm 10.33.2，命令在仓库根目录执行。
- ⚠️ 命令行 Web 模式可用 --no-token 关闭认证，README 说明监听非本机地址时才默认生成令牌，局域网暴露前需自行确认访问控制。

#### [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything) ⭐ 8,230

> 录制原应用行为，让编程 Agent 分块改写为 Rust 并逐块验证一致

- **定位**：面向 TypeScript/JavaScript、Python、C、Go、Ruby、Java、Kotlin、PHP、C# 应用，先录制原程序行为，再由编码 Agent 或人逐块写 Rust，每块与录制结果比对通过后才切换，最终得到纯 Rust 应用。
- **能做什么**：
  - 录制原程序行为，逐块校验 Rust 改写结果
  - 支持 CLI、HTTP 服务和库，也可只移植慢的热点函数
  - 生成桥接层，保持原有 API 不变，可随时回退到原实现
  - 支持 Claude Code、Codex、Cursor 等 Agent 接入
  - 用 fuzz、bench、gate 检查未覆盖输入、性能与完成度
- **亮点**：
  - 项目方数据：Prettier 命令行 128.6s 降至 6.9s
  - 项目方数据：json-server 空闲内存 74MB 降至 3.5MB
  - 项目方数据：Fuse.js 每查询 91.2ms 降至 2.8ms
- **适合**：希望把现有应用或性能热点迁移到 Rust、并用编码 Agent 保证行为一致的开发者。
- **上手**：`cargo install rust-anything` 随后运行 rust-anything setup 注册到 Claude Code、Codex 等 Agent；也可用 npm 或预编译二进制安装。
- ⚠️ record 与 app record 会用大量生成输入反复执行原代码，涉及写文件、数据库和网络的代码会重复执行，README 要求先在项目副本、测试库上运行并移除生产凭据。

### Agent 平台与基础设施

#### [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) ⭐ 84,431

> dsh 插件：免登录、免 Key 接入免费模型并本地转发

- **定位**：为 dsh 宿主提供免账号的免费模型车道（OpenCode Zen、Kilo 公共网关），并把模型以 OpenAI 兼容和 Anthropic Messages 接口转发给本机工具。
- **能做什么**：
  - 免登录免 Key，装插件即用免费模型车道
  - 设置页可管理模型清单、思考强度与用量看板
  - 本机 OpenAI 兼容与 Anthropic Messages 转发端口
  - 支持降级链路由与工具输出压缩省 Token
  - 应用内升级，SHA-256 校验失败自动回滚
- **亮点**：
  - 清单随上游刷新，仅广播实测可路由的模型
  - 用量数据全部留在本机，不上传
  - 项目方数据：40 KB git diff 压缩可移除 90% 字节
- **适合**：使用 dsh / DeepSeek Harness 的开发者，以及想把免费模型接入本机工具的 AI 用户。
- **上手**：`dsh plugin --profile web add @ebony-vinyl/dsh-our-free-model@2.8.0` 装完重启一次；README 警告勿装 npm 上无 scope 的同名包，那是第三方打包。
- ⚠️ README 警告勿安装 npm 上无 scope 的 dsh-our-free-model，该包由第三方打包且内容与本仓库不一致。
- ⚠️ 免费车道经第三方公共网关直连上游，请求与数据发往何处需自行评估；Kilo 池上游声明 prompt 可能被记录用于改进服务，README 提示勿发敏感内容。
- ⚠️ 各账号渠道与 EAC 渠道涉及登录第三方服务账号及 GitHub 授权校验，可能受对应平台服务条款约束。
- ⚠️ 许可证未声明或非标准，商用前请确认授权

#### [yetone/magpie](https://github.com/yetone/magpie) ⭐ 40,244

> 本地网关，让任意编程 Agent 用上任意模型与订阅

- **定位**：magpie 在 127.0.0.1:3425 起一个本地网关，兼容 OpenAI Chat/Responses、Anthropic Messages 和 Gemini 协议并互相翻译；可在菜单栏或 CLI 中为每个 Agent 改写配置，切换模型、供应商和账号。
- **能做什么**：
  - 为每个 Agent 一键切换任意 provider/model，原子改写原配置并保留注释格式
  - 把已登录的 Claude、ChatGPT、Copilot、Gemini 等订阅当作供应商共享给其他 Agent
  - 配额用尽时按 routing group 在账号、模型、供应商间自动转移
  - 可选隐私遮蔽：请求离开本机前把密钥、密码、邮箱换成占位符，回复中还原
  - 支持插件与网关中间件，可改写请求或过滤内容
- **亮点**：
  - 单个网关同时说 OpenAI、Anthropic、Gemini 四种协议并互转，含流式、工具调用与推理
  - Profiles 可一次保存并切回所有 Agent 的配置组合
  - 项目方称配额转移后 Agent 不会看到报错；只有一个账号且无分组时错误仍会传给 Agent
- **适合**：同时使用多个编程 Agent、多个模型供应商或多个订阅账号的开发者，macOS/Windows/Linux 均可。
- **上手**：`curl -fsSL https://usemagpie.ai/install.sh | sh` 安装后打开 magpie，在 Providers → Add provider 选预设粘贴密钥，再到 Agents 页为各 Agent 选模型。
- ⚠️ 默认会读取 Claude Code、Codex 的登录文件与 Keychain 来发现订阅账号，需在 Settings → Privacy 关闭或运行 magpie accounts discovery off。
- ⚠️ 把订阅账号的额度共享给其他 Agent 使用，可能违反相应服务的条款。
- ⚠️ 隐私遮蔽默认关闭，开启后仍可能漏检或误判，且模型看不到被遮蔽的原值。
- ⚠️ 网关监听本地端口，README 未说明是否可安全暴露到公网。

#### [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) ⭐ 24,714

> 用动态索引动作空间操作网页的快速浏览器 Agent

- **定位**：TypeSafe 的 Jev 策略：把页面结构化为带编号的元素表，通过一次请求同时预测操作和点击/输入目标，只有输入文本时才调用小模型生成文字。
- **能做什么**：
  - 每次观察生成编号元素表，操作限于点击、输入、选择、滚动等
  - 操作与目标在同一个网络往返中一起预测
  - 默认循环不截屏，只消费结构化页面状态
  - 执行前校验目标节点、页面新鲜度和遮挡情况
  - 提供本地 Inspector 查看元素编号、概率与已执行动作
- **亮点**：
  - 项目方数据：苏黎世到伦敦航班搜索 7.1 秒，含模型调用与加载等待
  - 项目方数据：六次交替运行中任务耗时中位数从 9.450 秒降至 7.092 秒，降幅 25%
  - 仅限单个任务、单个浏览器配置上的三次重复，非通用可靠性基准
- **适合**：需要把自然语言目标自动落到网页操作上的开发者与研究者，熟悉 Python 与浏览器自动化。
- **上手**：`uv run jev` 先执行 uv sync 并从 .env.example 复制配置，填入 TYPESAFE_API_KEY 和 TEXT_MODEL_API_KEY，再打开 127.0.0.1:8…
- ⚠️ 通过浏览器自动化操作 Google Flights、维基百科等第三方网站，可能违反其服务条款
- ⚠️ 示例使用真实 Chrome 用户配置，共享已有登录状态与 Cookie
- ⚠️ 调用 TypeSafe 与 OpenRouter 等外部服务会把页面可见文本和输入内容发送出去

#### [Jakeschincariol/day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill) ⭐ 9,229

> 11 个 Claude 技能：扫描图表、追踪新闻、择时进出并回放交易结果

- **定位**：面向日内交易的 Claude 技能包，由标准库 Python 工具读取 Yahoo Finance、SEC EDGAR 等免费公开数据，串联扫描、择时、风控、下单到告警的完整流程，默认纸面交易。
- **能做什么**：
  - 扫描数千张图表，寻找开盘区间突破、旗形、超卖反弹等形态
  - 逐根 K 线盯盘，给出等待、触发或过期信号
  - 入场前设好止损止盈，按预算和单笔最大亏损计算仓位
  - 时间机器从个股近 60 天 5 分钟线模拟 1 万次后续走势，并回放历史触发记录
  - 读取财报、突发新闻与国会交易披露文件
- **亮点**：
  - 所有工具为纯 Python 3.8+ 标准库实现，无需安装依赖
  - 示例中 TSLA 模拟结果：目标先到 29.4%，止损先到 25.5%，收盘仍未了结 45.1%（项目方数据）
  - 默认纸面交易，任何订单都需用户在对话中确认后才提交
- **适合**：使用 Claude Code 或 Claude 桌面端、关注日内交易的个人交易者与开发者
- **上手**：`/plugin marketplace add Jakeschincariol/day-trader-skill` 在 Claude Code 中执行后，再运行 /plugin install day-trader-skill@day-trader-skill 安装；SEC 相关工具需在 co…
- ⚠️ 项目方明确警告：时间机器是模拟而非预测，止损只是计划而非保证，快速行情或跳空时可能大幅滑点
- ⚠️ 项目方说明 Yahoo Finance 图表接口非官方 API，可能延迟、变更或限流，且扫描基于 1 或 5 分钟 K 线而非逐笔
- ⚠️ 项目方提醒多数日内交易者亏损，本软件不构成投资建议
- ⚠️ 快照当日已 34 天未更新（最后推送 2026-10-20）

#### [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) ⭐ 8,014

> Claude Code 插件：用 Jev 打分删除过期工具调用，替代有损压缩摘要

- **定位**：一个 npm 库兼 Claude Code 插件，在上下文压缩时不让模型改写历史，只对每次工具调用和结果打分，删除或截断不再需要的部分，保留内容逐字不变。
- **能做什么**：
  - 每条 tool_use 与 tool_result 配对打分，保留或删除，不重写文本
  - 按阶段裁剪状态以塞进 25k token 上限，仍不合适则抛错
  - 问题分批并发请求，受 30k token 请求上限约束
  - 结果可保留、截断为前 300 字符，或整条删除
  - 可选替换 Claude Code 内置压缩，失败时回退摘要
- **亮点**：
  - 用户与助手文本逐字保留且顺序不变，只动工具调用和结果
  - 导出 JevAsker 接口和构建、解析、裁剪等底层函数，可自接传输
  - 删除有概率阈值，结果可被重新运行，但概率不等于可安全删除的证据
- **适合**：使用 Claude Code 且在意上下文压缩丢失文件路径、报错等细节的开发者，以及需要可嵌入压缩库的工程师。
- **上手**：`npm install fast-jev-compaction` 需先 export TYPESAFE_API_KEY；插件方式需 Claude Code 2.1.274+ 并开启函数钩子早期访问开关。
- ⚠️ 快照当日已 66 天未更新（最后推送 2026-09-18）

#### [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer) ⭐ 7,986

> 为编码 Agent 跨会话学习仓库经验、削减无效 token 成本的插件。

- **定位**：微软开源的编码 Agent 插件，不改动 Agent 本身的模型与代码，而是从同一仓库的历史会话中学习，削减重复成本。支持 Claude Code、Codex、Copilot CLI、Pi，另实验性支持 opencode、Cursor Agent 等。
- **能做什么**：
  - 微技能：跨会话记录仓库的构建步骤、命令拼写等事实，三次确认后写入会话开头
  - 工具裁剪：连续多轮多会话未使用的工具定义从后续会话中移除，可按需恢复
  - 失败循环干预：判定卡死时给 Agent 一条重试提示，每轮最多一次
  - 成本按缓存价格计算，包含插件自身模型调用的开销
  - 每个机制可单独开关，动作只输出一行提示，失败时不影响原会话
- **亮点**：
  - 项目方数据：SWE-Bench 上五种 Agent-模型组合平均成本降 18.4–30.9%，30 个仓库×组合单元全部更便宜，Pass@…
  - 项目方数据：Web-Bench 成本降 16–21%，两个安全审计基准降 6–20%
  - 学习结果存于本地 ~/.tokeneconomizer，无需自带 API Key，复用 Agent 自身登录
- **适合**：频繁在同一代码仓库使用 Claude Code、Codex、Copilot CLI 等编码 Agent，希望降低 token 开销的开发者。
- **上手**：`git clone https://github.com/microsoft/TokenEconomizer.git
claude plugin marketplace add "$PWD/TokenEconomizer"
claude plugin install tokeneconomizer@tokeneconomizer` 需 Python 3.10+ 与对应 Agent；启动后信任文件夹并运行 /tokeneconomizer:status，每台机器执行一次 refresh-catalog。

#### [Lee-xeo/Claude-Cage](https://github.com/Lee-xeo/Claude-Cage) ⭐ 7,883

> 为 Claude 定制的本地轻量虚拟机，隔离网络与浏览器指纹

- **定位**：一个桌面程序，用 macOS、Windows 或 Linux 客机隔离运行 Claude Code、Claude Desktop 和浏览器，由 Cage 接管代理与网络出口，统一管理多账号、远程服务器和手机接续。基于 agent-vm 二次开发。
- **能做什么**：
  - 客机系统可选 macOS、Windows、Debian 或 Ubuntu
  - 内置代理管理，导入 Clash/Mihomo 订阅并选节点
  - 隔离时区、语言等指纹，可选与代理 IP 自动同步
  - 多 Claude Code 账号查看额度、分配与切换
  - Android/iPhone 配对电脑接续对话与工具审批
- **亮点**：
  - 内置网络与隔离检查，关键检查失败时环境保持离线，代理不可用无直连回退
  - 项目方数据：环境检测结果见 README 截图，社区浏览器检测仅供参考
  - 主许可 MIT；Mihomo 按 GPL-3.0 独立分发，附 NOTICE 与第三方许可
- **适合**：需要在本地隔离环境中使用 Claude Code、Claude Desktop，并管理多账号或远程环境的开发者
- **上手**：从项目主页下载对应平台安装包，拖入应用程序后按引导配置自己的代理，再新建终端输入 claude 完成授权
- ⚠️ README 称网络检查无法保证账户不受平台限制，项目面向规避封号场景，可能违反 Anthropic 服务条款
- ⚠️ 共享项目中的修改和删除直接作用于本机原文件，包括 Git 操作
- ⚠️ 同一配置下各项目共用客机系统、工具、账户与文件系统，项目间无独立隔离
- ⚠️ 默认公网出站仅支持 IPv4 TCP，UDP、IPv6、ICMP 及局域网直连受限

#### [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) ⭐ 7,727

> 用 ChatGPT 网页版做规划与审查，Codex 负责执行

- **定位**：通过只读 MCP 连接把 ChatGPT 网页版接入 Codex 会话，充当规划与审查角色，代码执行权仍留在 Codex；不使用 API Key，也不做逆向代理。
- **能做什么**：
  - 控制面用 Computer Use 传递极小的 [C2C] 状态消息
  - 数据面经 OAuth 2.1 保护的只读 MCP 工具读取工作区
  - 默认拒绝 .env、密钥、SSH 等敏感文件，可用 .c2cignore 加规则
  - ChatGPT 执行后自查 git diff 与测试记录，独立审查
  - 提供 c2c setup/status/doctor/pair 等 CLI 命令
- **亮点**：
  - 服务端不提供写入和 shell 工具，只读是代码层面保证的
  - 公开地址默认是 Cloudflare 临时隧道 URL，重启即变，可选配置固定域名
  - Skill 每天自动检查 GitHub 并更新
- **适合**：已订阅 ChatGPT Plus/Pro、希望减少 API 额度消耗的 Codex 用户，包括不熟悉命令行的小白用户
- **上手**：`c2c setup` 需先 pnpm install && pnpm build；另需 Node.js ≥ 20、git 和 cloudflared，也可让 Codex 按整段话自动安装
- ⚠️ 核心机制是用 Computer Use 自动操作 ChatGPT 网页版，可能违反其服务条款或有账号风险
- ⚠️ 默认公网入口是临时隧道地址，配置不当或令牌泄露会把工作区读取能力暴露出去
- ⚠️ 快照当日已 53 天未更新（最后推送 2026-10-01）

#### [Human-Agent-Society/reef](https://github.com/Human-Agent-Society/reef) ⭐ 7,643

> 让 Agent 从交互反馈中持续自我改进的开源基础设施

- **定位**：把 Agent 推理、反馈、学习与带版本号的发布串成一个持续循环，既能训练模型权重，也能迭代 Agent 的提示词、规则与技能。
- **能做什么**：
  - 推理、记录、训练、评估发布四步闭环
  - 兼容 OpenAI 与 Anthropic 的推理接口，返回回执关联反馈
  - 支持训练模型权重，或用模型 API 演化 Agent harness
  - 基于 Git LFS 的产物版本历史与不中断更新交付
  - 内置 SFT，另有 TTT、SAO、GEPA 等配方与教程
- **亮点**：
  - 模型权重与 harness 两种学习面由配方决定
  - 更新经评估后由推理服务热加载，无需重启
  - harness 教程用模型 API 跑通完整小循环，无需本地 GPU
- **适合**：希望让 Agent 从真实使用反馈中持续变强的研发团队，以及做 Agent 强化学习与持续学习的研究者。
- **上手**：`uv venv && source .venv/bin/activate
uv pip install reef-infra` 产物与检查点功能需先安装 git-lfs 系统包；源码开发则用 git lfs install 后以 -e 方式安装。

#### [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth) ⭐ 7,433

> 给 Agent 用的照片定位技能，靠 OSM 几何、高程天际线与街景推断拍摄点。

- **定位**：一个标准 Agent Skill（SKILL.md 加 Python 脚本），可装进 Claude Code、Codex、Cursor、Gemini CLI、OpenCode、GitHub Copilot，接收一张照片后输出相机坐标±半径、朝向和一张卫星证据图。
- **能做什么**：
  - 无文字、无车牌、无地标时，靠 OSM 几何、高程、卫星瓦片和街景推断
  - 把桥墩间距当距离尺、影子当方位、山脊线当高程指纹
  - 二十余个单一用途脚本负责搜索、打分和排序，模型只在排名靠前的少量候选中做判断
  - 结论需指明本次会话中运行过的命令和产出的文件
  - 输出带误差半径的坐标、相机朝向、证据图和分级置信度
- **亮点**：
  - 项目方数据：铁路桥案例定位误差 ±2 m，荒漠案例盲跑距确认点位 87 m
  - 项目方数据：温哥华樱花案例盲跑 3 m，用时 53 分钟、154 次工具调用
  - 项目方数据：荒漠盲跑最佳站点 0.224°、次优 0.357°；手机 1° 横滚曾致拟合卡住，后纳入拟合
- **适合**：使用 Claude Code、Cursor、Codex 等 Agent 做图片地理定位或 OSINT 分析的调查者、记者与地理竞猜玩家。
- **上手**：`npx skills add Oldcircle/geo-sleuth` 按提示选择要装入的 Agent；首次使用先让 Agent 运行 scripts/ 下的 doctor.py 排查环境，再把照片交给它并说“找出这张照片的拍摄地”。
- ⚠️ 核心功能是用反向图片搜索、街景和卫星影像定位他人照片的拍摄地点，用于现实中的人或敏感设施时可能涉及隐私与个人信息合规问题

#### [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) ⭐ 7,405

> 在 Mac 刘海和手机端实时监控并审批 AI 编程 Agent 会话的桌面伴侣

- **定位**：把 Claude Code、Codex、Cursor、Gemini CLI 等 Agent 的会话状态、文件改动和权限请求收进 Mac 刘海（Windows/Linux 为屏幕顶部），并延伸到 iPhone、Android 的锁屏与小组件上，让你不离开当前工作就能批准或回答问题。
- **能做什么**：
  - 刘海内实时展示各 Agent 会话读取、编辑、执行的内容和完整 diff
  - 在刘海或锁屏直接 Allow / Deny / Always，并回答 AskUserQuestion 选项
  - 一键跳到会话对应的终端窗口（macOS）
  - 内置多供应商聊天，可用自己的 API Key 或已有订阅
  - 附带离线听写、通话转写、邮件、集成和加密货币行情等小组件
- **亮点**：
  - 开源 MIT 版本，对标只展示不开放的刘海伴侣应用
  - iPhone 端用 Live Activity、灵动岛和可操作通知接力审批，每次 Allow 需 Face ID
  - 无遥测无账号，密钥存系统钥匙串，数据仅发给用户接入的服务
- **适合**：同时运行多个 AI 编程 Agent、希望随时掌握进度并快速授权的 Mac 开发者，以及想在手机上继续盯会话的人。
- ⚠️ 通过终端 CLI 订阅登录方式聊天，属于对第三方 AI 服务账号的自动化调用，可能触及服务条款
- ⚠️ 通话录制需自行告知参与者，否则涉及隐私与当地录音法规
- ⚠️ 语音助手模式下仅说话内容和相关数据会发送给 Anthropic

#### [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork) ⭐ 6,879

> 可自托管的团队 AI Agent 编排引擎，多 harness 协作并按验收标准交付

- **定位**：把需求变成带验收标准的工单，分配给人或 Agent，由另一个 harness 用不同模型复核，最终由提出人签收，全程留痕；适合团队统一管理和沉淀 AI 工作方式。
- **能做什么**：
  - 一个 harness 执行、另一个模型 harness 按验收标准复核
  - 支持 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex 等运行时，会话中可切换
  - 成功的对话可保存为插件，供团队复用并持续改进
  - 插件需审核后授权给团队或个人，可撤销，含角色、用量、成本与审计日志
  - 支持 Docker 自托管部署，含 Hub、管理控制台与 PostgreSQL
- **亮点**：
  - 以验收标准先行、AI 复核、人工签收的流程保证交付可信
  - 项目方说明：当前为公开测试版，建议在生产使用前先评估
  - 程序和模型分离，支持 ACP 的程序可通过目录声明接入
- **适合**：需要统一管理多个 AI Agent 与模型的开发团队、技术负责人和企业内部平台团队
- **上手**：`sh start.sh --desktop` 需先克隆仓库；Windows 用 .\start.cmd --desktop。首次运行会安装依赖并启动 Hub、管理控制台和桌面客户端。
- ⚠️ 项目处于公开测试阶段，README 建议在生产使用前先评估
- ⚠️ 官方在线演示仅供评估，README 明确要求勿上传真实业务数据或敏感信息

#### [CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots) ⭐ 6,729

> 开源模板：持久在线的 AI 同事，可跨文本、通话和 Slack 工作

- **定位**：OpenDots 是 CopilotKit 推出的开源模板，用于搭建自托管的持久化 AI Agent 工作台。每个 Dot 有独立角色、工具和计算机，支持 Web 与移动端，需要自行配置 Intelligence、模型和渠道服务。
- **能做什么**：
  - Space 页面库支持嵌套子页、可视化编辑器与 Markdown 源模式
  - 每个 Dot 可配置名称、角色、指令、工具权限和独立计算机
  - 浏览器、文件和 Shell 操作可在聊天中实时查看并接管
  - 保存前弹人工审核卡，批准后才写入授权 Space
  - 接通 MCP 工具和 Composio 邮箱日历，写操作需审批
- **亮点**：
  - 电脑的浏览器配置与工作区文件在停止后仍保留
  - 通话将实时语音与独立计算 Agent 配对，共用上下文和权限
  - Slack 通过 Channels SDK 接入，带工作区与用户白名单
- **适合**：想自托管、定制 AI Agent 工作台的开发者与团队，需熟悉 Node.js、TypeScript 和服务配置
- **上手**：`git clone https://github.com/CopilotKit/OpenDots.git
cd OpenDots
npm ci
cp .env.example .env
npm run dev` 需 Node.js 24；未接服务前可建 Space 和配置 Dot，聊天需配置 Intelligence 项目和模型。勿运行 copilotkit onboard。
- ⚠️ 托管模式会把对话消息、工具调用和运行事件发送到 CopilotKit 云端
- ⚠️ 公共网页研究默认把查询和所选 URL 发给 Parallel，需设 WEB_SEARCH_PROVIDER=disabled 关闭
- ⚠️ 启用 Connected apps 后，工具参数与结果会经 Composio 和应用提供商处理，且会操作真实账号
- ⚠️ 项目会收集使用元数据和安装 ID，需用 COPILOTKIT_TELEMETRY_DISABLED 或 DO_NOT_TRACK 退出

#### [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop) ⭐ 6,342

> 让命令行 Agent 在后台自动接活、遇到拿不准的事再找你拍板的本地调度中台

- **定位**：一个零依赖的本地自动化中台，把定时任务、Webhook 等事件按规则派给 Claude Code、Codex 等命令行 Agent，任务跑完即退出；需要人工决策时通过飞书、桌面通知等推送卡片，你回答后它接回原会话继续。
- **能做什么**：
  - 用 rules.json 写清什么事、交给谁、在哪个目录干，不需要写胶水代码
  - 事件、Agent、通知通道、交付流水线四个方向都可替换，支持第三方插件
  - Agent 在最后一条回复里用代码块提问、通知或预约复查
  - 待决策时进程退出，不占后台进程也不消耗 Token，回答后接回原会话
  - 内置八套场景模板：早报、Issue 跟进、告警排查、收件箱分诊等
- **亮点**：
  - 内核零运行时依赖，状态从只追加日志事件溯源，可一条命令查清每轮来龙去脉
  - 外部文字只作资料放进文件、不拼进提示词，事件里带 cwd/agent 字段会被拒收
  - 项目方数据：冷启动 88.78 ms，空闲内存 59.94 MB，派活 p99 1.82 ms
- **适合**：使用 Claude Code、Codex 等命令行 Agent、想让它们在本机后台自动处理重复任务并保留人工确认环节的开发者。
- **上手**：`curl -fsSL https://raw.githubusercontent.com/KKKKhazix/agent-autoloop/main/install.sh | sh` Windows 用 README 中的 PowerShell 安装脚本；需 Node 24+、Git 和已登录的命令行 Agent，装好运行 agent-autoloop try…
- ⚠️ 直接调用本机已登录的模型订阅额度，README 建议高频自动化或对外提供服务时改用 API Key

#### [monid-ai/monid](https://github.com/monid-ai/monid) ⭐ 6,219

> 给 AI Agent 用的一站式工具 API 网关，一个入口接入 2000+ 工具。

- **定位**：Monid 定位为 Agent 工具领域的 OpenRouter：一个 base URL、一个密钥，Agent 即可调用 72+ 供应商的搜索、抓取、人物与公司信息、社交、市场数据、图像与语音生成等接口。本仓库是连接器层，用声明式定义描述每个接口的调用方式与计费模型。
- **能做什么**：
  - 连接器以声明式 TS 定义认证、输入 schema 与用量计费模型
  - discover 按任务跨全部供应商排序，返回价格、健康度与 p50/p95 延迟
  - 用量按调用结算并锚定原始响应，供应商报错计为零用量
  - 测试基于录制 fixture 回放，CI 无需网络和厂商密钥
  - 提供 AGENT.md 与 Apify scaffold，可由编码 Agent 生成连接器
- **亮点**：
  - 覆盖 2000+ 工具、72+ 供应商，统一 base URL 与密钥
  - 同一产物可在本地、CI 回放与托管平台三处运行
  - 新增供应商只需提交 PR，合并后即进入 discover 目录
- **适合**：需要为 Agent 接入多种外部工具 API 的开发者，以及希望把自家 API 上架到 Monid 的厂商。
- **上手**：`git clone https://github.com/monid-ai/monid.git
cd monid
deno task check && deno task test` 需要 Deno 2.x；默认跑类型检查和 188 个离线回放测试。

#### [kuafuai/andee](https://github.com/kuafuai/andee) ⭐ 6,182

> 住在 Android 手机或 Mac 上的 AI 助手，像你一样操作任意 App。

- **定位**：一个设备常驻型个人 Agent：在设备本地运行，读取无障碍树和截图来操作任意 App，无需集成或 Root，支持任意 OpenAI 兼容模型，记忆和密码只留在本机。
- **能做什么**：
  - 读无障碍树与带标注网格截图，按格子点按，不做坐标计算
  - 支持任意 OpenAI 兼容模型，英文界面默认 OpenAI、中文默认 DeepSeek
  - 记忆笔记本仅存本机且可逐条删除，不上传
  - 自带四种现成场景：盯消息、清订阅、记会议、抢预约
  - 两台设备扫码配对，可互相派活
- **亮点**：
  - 安卓与 macOS 共用同一套 Agent 循环，代码开源可查
  - 第三方 App 无需提供接口，凡能用手指完成的操作它都能做
  - 检测到微信首个注入点击会破坏窗口，调度器直接拒绝在微信内点按
- **适合**：希望拥有本地常驻、可审计的手机或 Mac 个人 Agent 的用户，需要自行准备模型与语音 Key。
- **上手**：README 只提供 CodeFlying 在线一键构建与 GitHub Release 安装包，无命令行安装步骤；装后需授予悬浮窗和无障碍权限。
- ⚠️ 核心功能是自动化操作第三方 App，可能违反其服务条款；README 明确说明在微信内注入点击会导致窗口保护、截图变黑
- ⚠️ README 警告它会代你点按、输入、发消息甚至完成支付，属实验性软件，后果自负
- ⚠️ 语音会发送给你选择的语音服务商，对话会发送给你配置的模型服务
- ⚠️ 仓库许可证为 NOASSERTION，未声明标准许可证
- ⚠️ 许可证未声明或非标准，商用前请确认授权

#### [vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network) ⭐ 5,593

> 让 AI Agent 用 USDC 按次付费调用 x402 API 的非托管客户端

- **定位**：开源的 TypeScript 客户端与 SDK，提供本地钱包、按次付费和消费上限，供终端、MCP 客户端或代码发现并支付 x402 API，默认在 Base 上用 USDC 结算。
- **能做什么**：
  - 同时搜索多个 x402 目录并合并结果，标注来源
  - 签名前应用消费上限，每次付款生成本地收据
  - 提供 CLI、stdio MCP 服务器和 SDK，共用同一钱包
  - 可为每个 Agent 分配独立且带上限的账户
  - 启用 Arc 网络后可跨账户转账，由 vAPI 支付 gas
- **亮点**：
  - 付款直接发往 API 端点，无支付代理、无服务端签名
  - MCP 服务器不提供暴露助记词或私钥的工具
  - 运行于本机的组件全部开源，采用 Apache-2.0 许可
- **适合**：需要让 Agent 按次付费调用 API 的开发者，以及使用 Claude Code、Cursor、Codex 等 MCP 客户端的用户。
- **上手**：`npm i -g vapi-network` 需 Node.js 22+；随后运行 vapi setup 创建或恢复钱包，再 vapi fund 充值。
- ⚠️ 恢复短语只能由用户自行备份，vAPI 无法代为恢复；钱包密钥丢失即无法找回
- ⚠️ 客户端会把搜索、充值、云备份等操作发送给托管服务，这些服务的源码不在本仓库，且付款标识会带上 vapi 客户端标记
- ⚠️ 实验性的 Railway 部署需要显式导出成员密钥

#### [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) ⭐ 5,250

> 用 7 美元的 ESP32 板让 AI 模型操控真实 iPhone

- **定位**：iPhone 通过 AirPlay 把屏幕投给 ESP32 板，板子再把画面转发给手机上的 App；App 调用任意 OpenAI 兼容视觉模型做规划，通过 USB HID 模拟鼠标键盘点击屏幕。无需 Mac、开发者账号或越狱。
- **能做什么**：
  - AirPlay 屏幕镜像传到板子，App 解码后送入视觉模型
  - 板子作标准 USB 鼠标键盘，配合 AssistiveTouch 点击滑动
  - 任务可在后台运行，中断后从同一步暂停恢复
  - 每次运行保存在手机，可逐步回放并导出操作轨迹
  - 可选：提供 MCP 服务器与 Claude Code 插件，供编码 Agent 调用
- **亮点**：
  - 整个方案只需一台 iPhone 和一块约 7 美元的 Seeed XIAO ESP32S3
  - 步骤主要耗时在模型，项目方称每步需数秒
  - 项目方称免费模型线路为共享资源，可能返回 HTTP 503 导致运行卡住
- **适合**：想让 AI 直接操作 iPhone、又没有 Mac 或开发者环境的人；以及想把手机接入编码 Agent 的开发者。
- **上手**：`arduino-cli lib install "NimBLE-Arduino@2.5.1"` 还须安装 ESP32 core 3.3.x，再运行 hardware/flash.sh 烧录；没有 Mac 可在 Chrome/Edge 浏览器中刷固件。
- ⚠️ App 通过 USB HID 模拟鼠标键盘自动操作第三方 App 和账号，可能违反其服务条款
- ⚠️ 使用免费共享模型线路时，截图和任务内容会发送给外部服务

### AI 应用产品

#### [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) ⭐ 30,437

> DeepSeek Harness 的 Android 客户端，手机本机运行或远程遥控电脑上的 DSH

- **定位**：基于 DeepSeek Harness 的第三方 Android 客户端，社区开发，非官方。手机上跑 DSH 引擎，也可通过 SSH 或 DSHarness Remote 连接电脑、服务器上的 DSH。
- **能做什么**：
  - App 内装 Ubuntu、Node.js 与 DSH 环境，免 Root 免 Termux
  - 通过 SSH 或 DSHarness Remote 连接远程 DSH
  - 聊天界面支持切换模型、图片、语音与工具审批
  - 支持适配 DSH Go 的原生工具卡、表单、面板插件
  - 开启权限后可由本机引擎读取屏幕、点按和输入
- **亮点**：
  - 本机运行需预留约 1 GB 空间，仅连远程可跳过安装
  - 分享链接端到端加密，密钥只在链接里
  - 可选手机操控遇付款、密码、验证码交还用户
- **适合**：需要在 Android 手机上运行或遥控 DeepSeek Harness 的用户；插件作者可用仓库内 SDK 与示例开发原生界面。
- **上手**：从 GitHub Releases 或官网下载对应架构 APK 侧载，需 Android 8.0 及以上，首次启动选择本机安装或连接远程主机。
- ⚠️ 开启手机操控后，任务所需的屏幕文字可能发送给模型，支持看图的模型还可能收到截图
- ⚠️ “发送匿名使用统计”默认开启，需在首次引导或设置中手动关闭
- ⚠️ 仅以 APK 侧载为目标，非 Google Play 发布配置，release 本地构建默认用 debug 签名
- ⚠️ 名称、标识与吉祥物不在 AGPL 授权范围内，另有 ASSETS.md 使用条款

#### [jub0t/Concat](https://github.com/jub0t/Concat) ⭐ 19,714

> 免费开源的本地视频编辑器，作为 CapCut 的替代品，带有内置 MCP。

- **定位**：面向短视频与教程剪辑的跨平台非线性编辑器，本地 Rust 引擎加 GPU 合成，剪辑、自动字幕、配音、抠像全在本机完成；同时提供 MCP 服务与 JSON-RPC API 供脚本和 AI Agent 调用。
- **能做什么**：
  - 本地 Whisper 自动字幕，可选模型大小并套用样式
  - 本地文本转语音与几秒录音克隆音色
  - 人物、物体抠像，也可手绘遮罩
  - 关键帧支持位置、缩放、旋转、不透明度、音量与曲线编辑
  - 100 种 GPU 特效、滤镜和转场，多轨多时间线合成
- **亮点**：
  - 无 watermark、无需账号、无订阅，素材不上传，可离线使用
  - 内置 MCP 服务，用 concat --mcp 让 Claude 等 Agent 直接剪辑
  - 支持 macOS、Windows、Linux、Android，界面 26 种语言
- **适合**：做 TikTok、Reels、Shorts、YouTube 与播客切片的内容创作者，以及想用脚本或 AI Agent 批量剪视频的开发者。
- **上手**：`cd src
cargo run -p concat` 从源码构建需 Rust 1.93+、FFmpeg 7+ 开发库、cmake 和 C++ 编译器；普通用户可直接下载各平台安装包。
- ⚠️ 项目自述处于 beta，功能可用但仍有粗糙之处
- ⚠️ Windows 与 macOS 安装包未签名，需手动绕过 SmartScreen 或 quarantine 限制
- ⚠️ 音色克隆功能涉及他人声音的授权与肖像、声音权合规问题

#### [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) ⭐ 12,390

> 逐镜头逆向拆解视频：拍的、AI 生成还是代码做的，以及怎么复刻

- **定位**：为 AI Agent 设计的视频拆解工具，输出面向人的 HTML/PDF 报告和供 Agent 分层读取的 VIDEO.md，覆盖实拍、AI 视频、数字人、3D、代码动效与混合剪辑。
- **能做什么**：
  - 逐镜头判断实拍、AI 生成或代码制作，并给出机位、提示词或代码复刻方案
  - 提取字幕与文字样式并导出 SRT/ASS，标注贴纸、剪辑点和音频构成
  - 双输出：给人看的 report.html/PDF，给 AI 读取的分层 VIDEO.md
  - 可选接入 Gemini 或豆包视觉模型，提升判断准确率并生成反推提示词
  - 可按目标视频模型的时长、多镜头能力批量规划复刻
- **亮点**：
  - 项目方数据：纯离线工具在原始文件上调参集 98.3%、留出集 99.6%/98.9%
  - 项目方数据：平台转码后的视频需加视觉模型或 Agent 复核才能回到 99% 以上
  - VIDEO.md 为开放格式，可 pip install videomd 后独立校验
- **适合**：需要拆解参考视频、学习拍摄与动效手法并计划复刻的创作者、短视频团队和 Agent 用户
- **上手**：`Install https://github.com/JuneYaooo/rea-video, then break down this video: /path/to/video.mp4` 在 Claude Code、Codex 等可执行命令的 Agent 中直接说出该指令，需预装 ffmpeg 和 Python 3.10+。
- ⚠️ README 提示不要复用他人素材、音乐、角色或肖像，发布时需遵守平台规则与当地 AI 内容标识要求。

#### [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) ⭐ 11,259

> 自托管行业热点站框架：大模型筛选信源、聚簇事件、生成中文日报

- **定位**：AIHOT 的引擎与框架，与线上站同一份代码；把信源、分类和精选提示词换成你自己的行业，即可搭一个自动出日报的热点站。
- **能做什么**：
  - 六种信源：RSS、网页列表、JSON、X 账号、微信公众号、脚本推送
  - 提示词预筛后独立打两次分，按信源分级门槛入选
  - 不同来源的同一事件聚为一条，按独立来源数算热度
  - 默认每天 08:00 出日报，周一、每月 1 日出周月报
  - 对外提供 RSS、公开 API、MCP 与 llms.txt 给 Agent 使用
- **亮点**：
  - 精选提示词与入选门槛原文公开，改标准不用改代码
  - 示范仓库带 18 个公开海外 AI 信源，不含运营数据
  - 评分标准可用自标注样本在 SelectBench 中校准
- **适合**：想把某一行业资讯做成自动日报站的开发者或团队，需有 Docker、Node.js 24 和 OpenAI 兼容模型 API Key。
- **上手**：`node scripts/init-env.ts --llm-key <你的模型 API Key>` 需先 clone 仓库并进入目录；随后 docker compose up -d --build，打开 localhost:3000，后台在 /admin。
- ⚠️ README 要求不要使用 AIHOT 的名字和 Logo，名称与 Logo 不在 MIT 许可范围内。

#### [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness) ⭐ 11,221

> 用 AI Agent 规划并讲授课程，带你从现有理解学到目标

- **定位**：先测出你在各知识点的理解边界，再生成依赖图并逐步讲授；学习记录以命题和推理链存成知识图谱，跨会话沿用。
- **能做什么**：
  - 先测量理解边界，再生成到目标的知识依赖图
  - 逐步教学：预测、解释、检验，修复混淆后再往下建
  - 单独练习会话，题目和提示按你的推理调整
  - 知识图谱以命题和推理链存储，可导入笔记
  - 桌面端可附 PDF、图片，支持后台调研与可视化讲解
- **亮点**：
  - 无订阅加价，可用自有 API Key、订阅连接或 OpenAI 兼容端点（含本地模型）
  - 对话、图谱、设置和 API Key 存本地，学习记录为可查看的纯文本文件
  - 系统提示词可见可编辑，AGPL-3.0 开源
- **适合**：想系统学会困难概念、愿意写出推理过程并自带模型 Key 或本地模型的学习者
- **上手**：`npm run dev` 开发运行前需先执行 npm ci；普通用户可从 learnharness.ai 或 GitHub Releases 下载安装包
- ⚠️ 模型请求、联网调研和听写会把任务所需内容发送给外部服务，本地存储不等于离线处理
- ⚠️ Windows 安装包目前未签名，可能触发未知发布者或 SmartScreen 警告

#### [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) ⭐ 9,921

> 给编码 Agent 用的本地 FFmpeg 剪辑技能，含 42 个工具和 MCP 服务。

- **定位**：把 FFmpeg 封装成 Agent 可读的结构化工具集：先 probe，再无损剪辑，最后校验和看图确认。全本地运行，不需要云端和 API Key。
- **能做什么**：
  - 42 个工具覆盖剪切、拼接、字幕、重构图、响度、平台导出
  - 以 SKILL.md 技能形式接入 Claude Code、Cursor、Codex
  - 全部工具可作为 MCP 工具调用，默认只暴露核心 12 个
  - contract --json 输出机器可读契约，MCP 接口由它派生
  - 可选本地语音引擎生成字幕，音频不上传
- **亮点**：
  - 执行后自动 probe、按平台规范 check，并生成联系表检查画面
  - 模板交付 TikTok、Reels、YouTube 等 7 个视频目的地并输出汇总表
  - CI 校验 input_schema 与 CLI 是否漂移（项目方说明）
- **适合**：用 Claude Code、Cursor、Codex 等编码 Agent 做本地视频剪辑、又不想把素材上传云端的用户。
- **上手**：`npx ffmpeg-skill` 先安装 ffmpeg；Cursor 加 --cursor，Codex 加 --codex，三者都要用 --all。可用 doctor 检查环境。

#### [wangzan101/Mika](https://github.com/wangzan101/Mika) ⭐ 9,704

> 安卓端 AI 助手，用一句话让它在后台操作手机应用和网页

- **定位**：运行在手机本地的 AI Agent，在独立的后台屏幕上打开应用、点击输入、滚动浏览，不占用用户当前屏幕；无 Mika 服务器，用户自备模型 API Key 或登录已有账号。
- **能做什么**：
  - 在后台屏幕操作任意 App，无需逐应用集成 API
  - 内置桌面级浏览器，可在当前网页直接下指令
  - 记住用户偏好，把完成的任务沉淀为技能
  - 支持定时与条件触发任务，可随时插话或停止
  - 每会话提供 Linux 沙箱运行 Python、Node 和 shell（arm64）
- **亮点**：
  - 模型与数据留在本机，Key 和记忆加密存储，对话与运行记录不出设备
  - 默认 Ask 模式：仅在花钱（下单、支付）前确认，可选切换 Autonomous 模式
  - 电脑端 AI 工具可通过 CLI + Skill 或 MCP 向 Mika 派发任务
- **适合**：需要用自然语言自动处理安卓应用操作、网页浏览与定时任务的安卓用户；操作手机应用需 Android 12+，建议 14+。
- **上手**：从 Releases 下载 APK 安装，在设置›模型中选择提供商并填 API Key，操作手机应用还需按向导配对一次无线调试。
- ⚠️ 自动操作第三方应用和网站可能违反其服务条款，README 明确提示需自行判断并建议重要操作使用 Ask 模式。

#### [openfilm/openfilm](https://github.com/openfilm/openfilm) ⭐ 9,051

> 让编码 Agent 编写 HTML 网页来制作视频，并可在浏览器编辑器里修改的 AI 视频工具

- **定位**：把 Codex、Claude Code 等编码 Agent 变成视频 Agent：影片就是一个 film.html，每个镜头是一个用 frame(t) 绘制任意时刻的网页，Studio 在本地浏览器中编辑，改动会写回文件供 Agent 读取。
- **能做什么**：
  - 影片是一个 film.html：像剪辑轨一样编排网页、视频、图片和声音，用 CSS 定样式
  - 每个镜头是一个网页，用 frame(t) 画出任意时刻，可使用 three.js、WebGL、canvas、SVG、GSAP 等
  - Studio 本地编辑器：可改文字、图层、片段位置、裁剪、音量、速度与字幕
  - 导出 MP4、GIF、音频、字幕、静帧及 Final Cut Pro、Premiere、达芬奇时间线
  - 影片的生成方式放在技能里，可安装社区技能或用 openfilm skill add 添加
- **亮点**：
  - 同一 t 必须画出同一画面；look 会把每帧画两次并打乱顺序比对，找出不一致
  - 制作、编辑、渲染无需账号；内置音乐、音效、配音、贴纸、转场、特效与模板可免费使用
  - 生成式配音、音乐、图像和视频需在设置中接入自己的服务密钥，或登录 OpenFilm 免密钥使用
- **适合**：已在使用 Codex、Claude Code 等编码 Agent，希望用网页技术制作并精修视频的开发者与创作者。
- **上手**：`npx skills add openfilm/openfilm` 需 Node 22.2+、ffmpeg、git；首次运行会下载约 100 MB 的无头 Chromium。然后让 Agent 制作影片，并提示词。
- ⚠️ 未接入自有服务时，可登录 OpenFilm 免密钥生成配音、音乐、图像和视频，相关素材与请求会发送到其服务。

#### [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) ⭐ 8,491

> 聊天辅助决策工具：先判断对方意图与风险，再生成可填入的回复

- **定位**：Jev 先判断对方意图和当下风险，再起草、核对并排序多条回复，点选后填入输入框，发送始终由用户自己按下。覆盖 Android、Windows、macOS、iOS。
- **能做什么**：
  - 先判断后写：先输出意图、风险与应对方式，再给草稿
  - 多条草稿按该判断核对并排序，最贴合的排在前
  - Android 以悬浮层读取 WhatsApp、QQ、飞书、X 聊天
  - 桌面端用截图配合本地 OCR 或系统文本接口读取聊天窗口
  - 只填入输入框，从不代用户发送
- **亮点**：
  - 使用自己配置的模型服务商和 API Key，项目方不运行服务器
  - MIT 许可，允许商用，分发时需保留 LICENSE 和 NOTICE 并署名
  - Android 版聊天文字和用户开启的背景信息只发给所配置的服务商
- **适合**：需要在 WhatsApp、QQ、飞书、X 等聊天场景中先判断对方意图、再选择回复的 Android 与桌面端用户。
- **上手**：README 仅提供各平台 APK 或安装包下载链接，安装后需按应用引导开启无障碍服务和悬浮窗权限。
- ⚠️ 在 QQ、飞书、X、WhatsApp 等第三方应用内使用可能违反其服务条款，账号可能被限制或封禁。
- ⚠️ Android 版会将聊天文字及用户开启的背景信息发送至用户配置的外部模型服务商。

#### [anhao/ai-pose-gallery-zh](https://github.com/anhao/ai-pose-gallery-zh) ⭐ 7,893

> 中文 AI 绘画参考图库，含姿势、服装、人像三库与角色合成台

- **定位**：把原作者ギア的三个日文 AI 绘画参考站合并并全量汉化，本地镜像 11,568 张图，另提供网页合成台和 ComfyUI 节点。
- **能做什么**：
  - 姿势库 1,439 条，每张素体白模对应一张深度图，可一键互换
  - 服装库 1,407 条、人像库 1,499 条，元数据全部为中文
  - 合成台可组合人像、服装、姿势，并支持拖拽、粘贴、URL 附加参考图
  - 可选直连 5 家图像接口，支持后台跨页生成和 IndexedDB 历史
  - ComfyUI 插件提供 4 个节点，内置 4,345 条中文弹窗选图器
- **亮点**：
  - 同时收录白模与深度图，可直接接入 ControlNet Depth
  - 无需 Python 依赖即可作为 ComfyUI custom_nodes 安装
  - 提供 8 个 SKILL.md 技能，让 Agent 通过相对路径检索图片
- **适合**：用 AI 绘画工具或 ComfyUI 制作角色图的创作者，以及需要姿势、服装、人像参考素材的插画与动画工作者
- **上手**：`cd /path/to/ComfyUI/custom_nodes
git clone --depth 1 https://github.com/anhao/ai-pose-gallery-zh.git` 重启 ComfyUI 后，右键新建节点，选择「AI角色三合一参考图集」，再点选图器；也可以访问在线演示。
- ⚠️ 图库包含 18+ 素体与内衣、性感穿搭内容，README 要求用户自行开启安全模式来屏蔽
- ⚠️ 图片版权归原作者ギア所有，README 禁止提取倒卖或付费分发
- ⚠️ README 声明许可证为 NOASSERTION，协议部分内容在摘录中也不完整
- ⚠️ 用于真人换脸或 Deepfake 可能涉及肖像权、隐私权等法律问题
- ⚠️ 许可证未声明或非标准，商用前请确认授权

#### [yi1108/printfilm](https://github.com/yi1108/printfilm) ⭐ 7,183

> 把文案做成带画面与配音的 AI 短视频与分集漫剧

- **定位**：自托管的 AI 视频创作平台，分步完成文案、分镜、生图、图生视频和合成，漫剧与短视频共用同一套生成能力。
- **能做什么**：
  - AI 短视频分步创作：文案、分镜、生图、镜头视频、合成预览
  - AI 漫剧从大纲到分集成片，角色与场景资产可复用
  - 默认 9:16 竖屏、约 60 秒，可选静图加 TTS 配音成片
  - 每阶段停下等待人工检查，支持单镜预览与重生
  - 管理后台配置模型路由，可选开启计费
- **亮点**：
  - 镜像托管在公开 ACR 命名空间，拉取无需登录
  - 进程内任务平台，无需单独部署 Celery Worker
  - 填 ARK_MOCK=true 可在无 Key 时先看界面
- **适合**：需要批量制作投放短片、漫剧分集的创作者和小团队，以及希望自托管视频生成平台的开发者。
- **上手**：`docker compose --env-file deploy/.env.docker up -d` 先克隆仓库并把 deploy/.env.docker.example 复制为 deploy/.env.docker，至少修改数据库密码、SECRET_KEY 和 API Key。
- ⚠️ README 提示生产环境须立刻更换默认密钥，并不要把示例密码直接用于部署。

#### [CopilotKit/openfuse](https://github.com/CopilotKit/openfuse) ⭐ 6,575

> 自带浏览器、终端和文件的跨端个人 Agent 应用

- **定位**：OpenFuse 是一个可自行部署的个人 Agent 应用，自带服务端、任务 worker 和浏览器 worker，支持 iOS、Android 和 Web（基于 CopilotKit React Native），可克隆后自行修改。目前处于 alpha 阶段。
- **能做什么**：
  - 聊天内联显示邮件、浏览器、PDF、计划与财务卡片
  - Agent 电脑：持久 Chromium 配置、接管控制台，可选隔离 Linux 终端
  - 任务活动：计划、审批、暂停/恢复/取消/重试，SQL 租约恢复中断任务
  - Goals 跟踪：定期检查公开页面变化、文本或美元价格阈值并去重告警
  - 邮件与日历：Google OAuth 接入 Gmail 与 Calendar，读写均需逐次审核
- **亮点**：
  - 内置浏览器 worker 可实时接管同一会话继续操作
  - README 提供 Render 三服务部署模板（API、静态站、私有浏览器）
  - Web 搜索默认开启，使用 Parallel 免费无 Key 的 Search MCP
- **适合**：想自托管个人 Agent、基于开源模板二次开发的开发者，需要 Node 24 与 CopilotKit Intelligence 项目密钥。
- **上手**：`pnpm dev` 需先克隆仓库、pnpm install、复制 .env.example 并完成 copilotkit CLI 登录与项目选择；另开终端运行 pnpm dev:web。
- ⚠️ 通过 Google OAuth 操作真实 Gmail 和日历账户，发送或变更仍需逐次审核，账号数据会经该服务处理
- ⚠️ 默认将模型生成的查询与对话上下文匿名会话 ID 发送给第三方 Parallel 搜索，可设 WEB_SEARCH_ENABLED=false 关闭
- ⚠️ 仅以共享访问密钥保护单一用户，不是多租户认证系统；README 要求远程部署使用 HTTPS 并限制网络访问

#### [AhmadHassan-BTed/Jantt](https://github.com/AhmadHassan-BTed/Jantt) ⭐ 6,237

> 把声明式 JSON 渲染成可交互甘特图的零依赖 TypeScript 引擎

- **定位**：面向 AI Agent 与人类协作者的时间线引擎：LLM 只输出符合 JSON Schema 的任务与依赖，Jantt 负责确定性渲染、拖拽编辑和回写状态。提供 React 组件、script 标签与 CLI 三种用法。
- **能做什么**：
  - 零运行时依赖的纯 TypeScript 核心，React、HTML、CLI 均可接入
  - 内置拓扑 DAG 求解与关键路径（CPM）计算，支持里程碑、基线与进度拖拽
  - 内置 EVM 挣值管理与 DCMA-14 进度健康审计
  - 提供 JSON Schema 与提示词速查表，供 LLM 生成任务数据
  - 可选：多用户 CRDT 协作房间与角色权限
- **亮点**：
  - 项目方数据：核心包 gzip 后小于 14 KB，模型生成 JSON 比生成 JSX 少 10 倍 token
  - 声明式 JSON 契约提供边拖拽编辑边回写，形成与 AI 的双向循环
  - MIT 许可，附带在线 Playground 与完整 Schema 规范文档
- **适合**：希望让 LLM 生成项目计划的前端与 AI 工程团队，以及需要轻量甘特图的项目管理者
- **上手**：`npm install @jantt/react @jantt/core` 引入 @jantt/react/dist/index.css 后以 data 传入 { tasks, categories } 即可渲染
- ⚠️ fork/star 比例异常（23/6237），热度可能有水分

#### [AienTech/dossier](https://github.com/AienTech/dossier) ⭐ 5,382

> 自托管的求职与简历工具，用 AI 按每个岗位生成定制简历和求职信。

- **定位**：Dossier 把职业经历集中到一份个人资料里，再据此为每个岗位生成只使用资料中事实的定制简历、求职信和配套邮件，并跟踪每份申请从草稿到拿到 offer 的全过程。它只面向单用户自托管。
- **能做什么**：
  - 个人档案涵盖经历、项目、证书、论文等，也可从已有简历导入
  - 内置 12 套简历主题和主题编辑器，可在服务器端渲染为 PDF
  - 从 JSearch、Adzuna、FreeHire 搜索岗位，并按个人资料打分匹配
  - AI 根据岗位描述匹配个人档案，缺失的要求只标为差距，不会编造
  - 可选 Job Agent 每天按需运行最多三个已保存的搜索，只准备草稿，不投递
- **亮点**：
  - 可接入 Ollama 或 LM Studio 的本地模型，资料可不出本机
  - 可选 MCP 连接器，在 Claude 各客户端或 n8n 中调用，只能存草稿
  - 项目方数据：2 vCPU / 1 GB 容器内单份简历 PDF 渲染约 0.25 秒
- **适合**：需要自托管、注重隐私、愿意自己准备模型和数据库的个人求职者。
- **上手**：`docker compose up -d` 需先下载 compose.production.yml，并在 .env 写入 POSTGRES_PASSWORD、DOSSIER_SECRET 和 argon2id: 密码哈希…
- ⚠️ 可选连接 Gmail 和 Google 日历，会把邮件内容和日历数据交给所配置的 AI 模型处理，README 建议先阅读隐私说明
- ⚠️ 用 SQLite 单容器部署时，如果不挂载 /data 卷，升级会删除数据，容器启动时会就此警告
- ⚠️ AGPL-3.0 许可证对修改后对外提供服务的版本有开源要求

#### [ersinkoc/phonebox](https://github.com/ersinkoc/phonebox) ⭐ 5,196

> 把旧安卓手机变成电脑桌面控制面板和触控面板。

- **定位**：配套安卓全屏应用与桌面代理，通过 USB 或 Wi-Fi 连接，在旧手机上显示电脑状态、AI 编程会话、媒体信息和触控操作，支持 Windows、Linux、macOS，无需 root、账号或云服务。
- **能做什么**：
  - 130 个小组件、30 个模板，浏览器可视化编辑器可拖拽布局
  - 显示 CPU、GPU、内存、磁盘、网络等电脑状态
  - 查看 Claude、Codex 等 AI 编程会话配额与本地会话详情
  - 触控宏、快捷键、媒体、麦克风、OBS 与系统控制
  - Webhook、Home Assistant 联动与通知自动化
- **亮点**：
  - 桌面代理监听 127.0.0.1:8765，可选 Wi-Fi 使用 HTTPS 端口 8766 并固定证书
  - 无遥测、分析或账号；可选组件会访问天气、配额、GitHub 等外部服务
  - 手机端可回应 Codex、Claude Code、OpenCode 的权限提示（需开启）
- **适合**：想把闲置安卓手机改造成桌面仪表盘、或想在手机上一键查看 AI 编程会话与电脑状态的 Windows、Linux、macOS 用户。
- **上手**：`irm https://raw.githubusercontent.com/ersinkoc/phonebox/main/setup.ps1 | iex` Windows PowerShell 命令；Linux/macOS 用 setup.sh。需 Android 5+ 手机，Wi-Fi 配对默认关闭需在设置中开启。
- ⚠️ Windows 发布代理尚未签名，SmartScreen 或杀毒软件可能警告或拦截
- ⚠️ USB 调试授权仅应在可信电脑上进行，否则可能被滥用
- ⚠️ 社区插件未经项目方审核，可修改 PhoneBox 设置

#### [omnirush-ai/omnirush-gui](https://github.com/omnirush-ai/omnirush-gui) ⭐ 5,095

> 桌面端编程 Agent 应用，默认使用 GPT 6 Astra 等前沿模型

- **定位**：面向在自己项目上使用编程 Agent 的开发者，提供 macOS 与 Linux 桌面客户端，按账号内可用模型选择，并集成 Skills、本地 MCP 与 Git 工作流。
- **能做什么**：
  - 按对话选择模型与推理强度（low 到 max）
  - 从设置里的 Library 添加 Skills，所有模型共享
  - 支持本地 MCP 服务器，如文件系统、git、SQLite、Playwright
  - Agent 可克隆、建分支、提交、推送并用 gh 创建和审查 PR
  - 全权限开关可切换逐次询问与放行全部工具调用
- **亮点**：
  - 只支持账号内模型，不支持自带第三方 provider 密钥
  - 写命令每会话询问一次，破坏性命令始终询问
  - macOS 与 Linux 多数安装包支持应用内自动更新
- **适合**：希望在本地桌面环境用前沿模型做编程的开发者，主要在 macOS 与 Linux 上工作。
- **上手**：从 releases 页面下载对应平台安装包；macOS 构建未公证，首次需在隐私与安全性中点“仍要打开”。
- ⚠️ 许可证为非标准：主仓库为 MIT，但 ee/ 目录另有许可
- ⚠️ 桌面端当前依赖 omnirush.ai 账号，且必须登录后才能运行提示
- ⚠️ macOS 构建尚未公证，README 指导用户绕过 Gatekeeper 打开
- ⚠️ 许可证未声明或非标准，商用前请确认授权

### 本地推理与模型

#### [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) ⭐ 20,821

> 在驱动加载前解锁 GeForce 显卡被限制的 Tensor Core 速率

- **定位**：Linux 内核模块，在 NVIDIA 原厂驱动绑定显卡前解除 GeForce 在 FP16/BF16/TF32 上的半速限制；不改驱动、不刷 VBIOS，驱动更新后无需重做。
- **能做什么**：
  - 支持 Ampere（RTX 30）稳定，Ada（RTX 40）、Turing（RTX 20）实验性
  - 通过内核命令行 gpu_unlock.targets 指定全部或指定 PCI 地址的显卡
  - 安装后写入 initramfs，在 nvidia 之前加载；默认不启用
  - 挂起到内存唤醒后自动重新解锁，可用 gpu_unlock.resume=0 关闭
  - 输出结果前后逐位一致，仅速度变化
- **亮点**：
  - 项目方数据：RTX 4090 BF16 稠密矩阵乘从 165 升至 329 TFLOPS（+100%）
  - 项目方数据：LLM prefill 提速 25–55%，LoRA/全参微调 25–50%
  - 项目方数据：4090 在默认功耗下受功耗限制，大 GEMM 增益远低于峰值速率
- **适合**：使用 RTX 20/30/40 系列显卡跑 AI 训练与推理的 Linux 用户
- **上手**：`make install` 需先克隆仓库并进入目录；安装后还要把 gpu_unlock.targets=all 加到内核命令行
- ⚠️ 仓库未声明许可证；README 只说明内核模块与本地打包为 GPL-2.0-only
- ⚠️ 解锁后显卡功耗与发热上升，笔记本可能因空闲断电而静默失效
- ⚠️ 许可证未声明或非标准，商用前请确认授权

#### [Likely7/Veyra-NRVideo](https://github.com/Likely7/Veyra-NRVideo) ⭐ 5,516

> Windows 上的实时 GPU 视频增强播放器，集超分、降噪、补帧与采集于一体

- **定位**：把本地视频、采集卡和主机串流统一接入同一套实时 GPU 处理管线，支持超分辨率、降噪、HDR、帧生成和导出。基于 GPL-3.0 开源，需 Windows 11 x64 与 DirectX 12。
- **能做什么**：
  - 最多四层独立降噪，各自可设内部分辨率与强度
  - 可选 SR、RTX Video HDR 与 DLSS/XeSS/FSR 帧生成
  - 实时预览视频、图片、采集卡、PS5、Xbox 与截屏
  - 节点模式可连线搭建自定义处理链，支持预设与会话
  - 导出队列支持剪辑、MP4/MKV 及多音轨和字幕轨
- **亮点**：
  - 项目方数据：RTX5070 下 4K 抗锯齿 FXAA 约 0.15ms、SMAA/MLAA 约 0.30ms
  - 项目方数据：最终单面网格美化 1080p 约 0.93ms、4K 约 1.42ms，称耗时随内容与硬件变化
  - 项目方数据：README 称降噪强度设为 5 时仅做单次推理外推，不能保证所有视频无伪影
- **适合**：需要为本地视频、采集卡或主机串流做实时画质增强的 Windows 用户，需具备兼容 GPU 与基本配置能力
- **上手**：从 Releases 下载 Setup EXE 或便携 ZIP，运行安装或解压到可写目录后启动 Veyra.exe，并另装对应 GPU 包
- ⚠️ Xbox 串流为官方未支持的实验功能，受账号、服务与主机限制
- ⚠️ PS5 串流需经第三方网站获取 Account ID，涉及账号凭据处理
- ⚠️ README 说明项目方从社区代币领取创作者手续费，该代币非官方发行，不构成投资建议

### Skills 与写作/设计

#### [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) ⭐ 28,780

> 让 Claude 把技术概念画成可交互的等距 SVG 图解。

- **定位**：一个 Agent Skill：根据你的描述，让 Claude 设计一台能把概念演出来的机器，再用几十个带明暗的等距零件画出带标题、提示和实时读数的卡片图。
- **能做什么**：
  - 输出独立 HTML、单个 SVG 或 React/Next.js 组件
  - 可选 WebGL 着色器，用来画火焰、水、光晕
  - 3D 效果为 beta，零件可旋转、弯曲、掉落
  - 图上的数字和零件运动由同一个模型驱动
  - 自带无头浏览器检查脚本，逐处检查各个关节
- **亮点**：
  - 使用 Node 内置模块，无需 API Key 或 npm install
  - 支持 Claude Code、Antigravity、OpenCode、Codex、MiniMax Code
  - examples/ 内已提交成品页面，可直接打开查看
- **适合**：需要为文档、博客或落地页制作技术解说插图的开发者，以及使用 Claude 等编码 Agent 的用户。
- **上手**：`npx skills add wheresryan22/anatomy -g` 安装时会询问要给哪些 Agent 装上，加 -a claude-code 可跳过；之后在 Claude Code 中输入 /anatomy。
- ⚠️ 快照当日已 36 天未更新（最后推送 2026-10-18）

#### [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) ⭐ 22,271

> 用 AI Agent 写规格、再由零上下文子代理评审的编码插件

- **定位**：EGM 是给编码 Agent 用的开源技能插件：Elephant 持有项目上下文起草设计规格，Goldfish 评审者在没有先前对话的情况下审查草稿，架构取舍仍由人决定。
- **能做什么**：
  - Elephant 代理结合项目上下文起草设计规格文档
  - Goldfish 子代理在零上下文下评审草稿，暴露未言明的假设
  - 流程分头脑风暴、起草、评审三步，每步可单独使用
  - 评审需要能新建子代理的会话，否则中止
  - 支持 Antigravity、Claude Code、Codex 等编码 Agent
- **亮点**：
  - 起草与评审由不同上下文承担，减少盲区
  - 每节草稿暂停等人反馈，架构决策由人批准
  - Apache 2.0 开源，非 Google 官方支持产品
- **适合**：需要对有设计取舍的功能先写规格再实现的开发者，以及使用 Claude Code、Codex、Antigravity 的编码 Agent 用户。
- **上手**：`claude plugin marketplace add google/elephant-goldfish-model` 安装后需另执行 claude plugin install egm@egm，并新开会话；Claude Code 中命令要加 /egm: 前缀。

#### [heydamir/unslop](https://github.com/heydamir/unslop) ⭐ 20,469

> 把 AI 味 UI 改造成有设计感的界面

- **定位**：Claude Code 与 Codex 的 Agent Skill，先找出紫色渐变、光晕、emoji 标签等 AI 风格元素，再从产品出发确定设计方向，按设计师逐轮审查的方式修改界面。
- **能做什么**：
  - 审计界面并列出每处 AI 风格元素的位置
  - 从产品推导性格、世界与标志性细节
  - 按间距、色彩、图标、文案、字体、布局等顺序逐轮修改
  - 支持 Next.js、React、Vue、Svelte、Tailwind 及原生 HTML/CSS
  - 仅凭链接即可处理线上页面，可选生成方形短视频
- **亮点**：
  - 先提出设计方向再动手，可提前调整
  - 界面已足够好时只给小幅优化建议，不推倒重来
- **适合**：使用 Claude Code 或 Codex 的开发者与设计者，用于整理用 AI 生成的仪表盘、应用和落地页。
- **上手**：`git clone https://github.com/heydamir/unslop
mkdir -p ~/.claude/skills && cp -r unslop/skills/unslop ~/.claude/skills/` 安装后在 Claude Code 输入 /unslop 加需求；Codex 用 $unslop，也可手动复制到 ~/.agents/skills/。

#### [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) ⭐ 20,036

> 面向 Claude 的代码短片风格工具箱：66 种现成风格，也可自建

- **定位**：Claude Code 技能包，把一种风格提示词交给编码 Agent，由它逐帧写代码完成画面、配乐和配音，不用视频生成模型，也不需要素材片。
- **能做什么**：
  - 66 种内置风格，按流派分类，每种附有 STYLE.md 和演示短片
  - 可修改内置风格，也可从零新建并保存为自己的风格
  - 可选先出故事板再出成片；默认 1920×1080、24fps
  - 由 DIRECTOR.md、TECHNIQUE.md 指导构图、配音、配乐和混音
  - 提供 Claude Code 插件安装，其他 Agent 可复制技能目录
- **亮点**：
  - 全部画面用 canvas/WebGL 逐帧渲染，音乐取自免费采样库，旁白用 TTS
  - 项目方说明：风格针对 Claude Opus 5.5 调校，其他模型可能难以复现
  - 项目方说明：一部片约需 30–60 分钟和较多 token
- **适合**：用 Claude Code 制作短片、动效或解说视频的创作者，需 Node 20+、ffmpeg 7+、Python 3.11+。
- **上手**：`claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab` 安装后首次使用会把指南、工具和风格提示词下载到 ~/lemo-opuscar；Ubuntu 24.04 自带 ffmpeg 6.1 版本过低。
- ⚠️ 演示中有三段配音不在 CC BY 4.0 范围内（macOS 系统语音、Edge TTS、豆包 TTS），README 要求不要复用
- ⚠️ 影片素材的版权和使用责任由使用者自行承担
- ⚠️ 许可证未声明或非标准，商用前请确认授权

#### [janestreet/agent_skills](https://github.com/janestreet/agent_skills) ⭐ 10,940

> Jane Street 的 AI Agent 技能集合，目前提供苏格拉底式导师技能

- **定位**：一组面向 AI Agent 和聊天机器人的技能，每个技能是一个含 SKILL.md 的目录；目前收录 socratic-tutor，把 LLM 变成用苏格拉底法教学的个人导师。
- **能做什么**：
  - 每个技能为含 SKILL.md 的目录，内有给 Agent 的指令
  - socratic-tutor 依次进行诊断、0-5 级技能地图评估
  - 每次只问一个问题，配合间隔复习
  - 教学结束时给出最终测评
  - 支持通用 SKILL.md 格式的编程 Agent，也支持纯聊天机器人
- **亮点**：
  - 基于 MIT 许可证开源
  - 编程 Agent 可复制技能目录后直接调用
  - 纯聊天机器人则粘贴 SKILL.md 正文到对话或系统提示
- **适合**：使用支持 SKILL.md 格式编程 Agent 或普通聊天机器人的用户，尤其是想用 LLM 自学的人
- **上手**：README 未提供安装或运行命令：把技能目录复制到 Agent 的 skills 文件夹，或把 SKILL.md 正文粘贴进聊天。

#### [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) ⭐ 10,368

> 11 个 Claude 技能，用于反向拆解并重建任意 App

- **定位**：一组按顺序执行的 Claude 技能，从公开页面和自有账号中反向工程目标 App 的界面、流程与数据模型，再用全新代码重建，并做品牌替换、评分和上线。MIT 协议，无需注册或 API Key。
- **能做什么**：
  - recon 技能从公开页面、截图、商店页和自有账号提取屏幕、流程与数据模型
  - architect、design、build、backend 技能规划技术栈、设计令牌并逐屏重建
  - test、diff 技能用 Playwright 跑流程测试，并给出对比原版的功能完成度评分
  - entrepreneur 技能把真实评论里的用户抱怨整理成改法和定位角度，每条带链接
  - brand、launch、deploy 技能负责改名换肤、写落地页与商店文案、部署上线
- **亮点**：
  - 11 个技能可串联执行，也可单独运行，产物统一写入项目的 replica/ 目录
  - 6 个纯标准库 Python 工具，README 称均不联网
  - sweep.py 检查代码中是否残留原 App 名称、域名与配色，不通过则阻止部署
- **适合**：想基于现有 App 的功能与流程做独立产品的开发者、独立创业者，需要已安装 Claude Code，Python 3.8 以上。
- **上手**：`/plugin marketplace add Jakeschincariol/replica-skill
/plugin install replica-skill@replica-skill` 以插件安装后技能带 replica-skill: 前缀；也可 git clone 后把 replica-*/ 目录复制到 ~/.claude/skills/。
- ⚠️ 重建他人 App 的功能与流程可能涉及知识产权或商标纠纷，README 要求先做商标核查并在上线前咨询律师
- ⚠️ recon 会读取自有账号内容，若账号条款禁止用于做竞品，README 称将只使用公开来源
- ⚠️ 项目只做清洁室式功能复刻，不复制源码、素材、商标与内容，但 README 也声明不保证得到完全一致的克隆结果
- ⚠️ 快照当日已 51 天未更新（最后推送 2026-10-03）

#### [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) ⭐ 8,809

> 244 个代码化像素特效，附一个 Claude Code 技能用于自制

- **定位**：一套纯代码实现的像素艺术特效库，按特效分目录存放，可直接在浏览器游戏里调用，也可导出精灵表；附带一个 Claude Code 技能，用于查找、导出和新建特效。
- **能做什么**：
  - 21 类共 244 个特效，每个都是一个 JS 文件
  - 61 个带角色特效和 12 个招式带蓄力、命中、硬直等演出数据
  - 无依赖，可配合 canvas、Phaser、PixiJS 等使用
  - 支持导出 PNG 精灵表与 Aseprite 风格 JSON
  - 特效接受 palette 参数，不改代码即可换色
- **亮点**：
  - 纯特效按时间参数出帧、循环无接缝，模拟类特效以 120Hz 步进
  - 所有随机数由 seed 决定，同一帧每次渲染一致
  - 与 Sprite Fusion 的 VFX 帧结构相同，可共用缓冲区
- **适合**：做像素风游戏或动画的开发者，以及用 Claude Code 制作特效的美术和独立开发者
- **上手**：`npm i github:patch-gg/pixelfx` 从 GitHub 安装；也可直接复制 src/core 和所需特效文件。

#### [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) ⭐ 8,411

> 13 个 Claude 技能，帮你运营 Instagram 账号

- **定位**：一套面向 Claude 的 Instagram 运营技能包，覆盖 Reels 脚本、爆款研究、文案检查、个人主页评分、一周排期等，并附带 5 个本地 Python 工具。免费、MIT 许可，无需注册或 API Key。
- **能做什么**：
  - 用 26 个钩子公式生成 Reels，生成前先给钩子打分
  - 按各账号自身中位数倍数找出对标领域内的爆款 Reels
  - 检查标题文案，预览信息流中可见的前 125 个字符
  - 按 100 分制评分个人主页并给出改写顺序
  - 去除草稿中的隐形字符、堆砌词汇和模板句式
- **亮点**：
  - 项目方数据：钩子评分器在故意写差的钩子上 AUC 为 0.83
  - 项目方数据：区分同一创作者的热门与冷门视频时 AUC 仅 0.56，即接近随机；README 承认无法挑出赢家
  - 项目方数据：公式分类器最初只识别 8% 的真实钩子，重写后达 49%
- **适合**：用 Claude 运营 Instagram 账号的创作者、内容团队和社媒运营者。
- **上手**：`git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/` 也可作为插件安装；之后花十分钟填写 templates/voice.md，所有技能都会读取这个文件。技能只负责写作，发帖仍由你自己操作。
- ⚠️ 快照当日已 71 天未更新（最后推送 2026-09-13）

#### [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) ⭐ 7,544

> 让 Claude 等 AI 代理做标志设计的 Agent Skill，从需求简报产出可用的 SVG 和品牌规范。

- **定位**：一个按开放 Agent Skills 格式（含 SKILL.md 的文件夹）编写的标志设计技能包，可装入 Claude Code、Gemini CLI、Codex CLI、Cursor、Copilot 等代理，把首份简报一路推进到生产级 SVG 与品牌指南。
- **能做什么**：
  - 覆盖从需求调研、概念发想、几何构建、光学修正到色彩、字体、锁定的完整流程
  - 1,400+ 真实 SVG 标志参考库，可按标志类型、行业、情绪等检索，命令行可查、本地画廊可浏览
  - 无依赖 Python 工具：审查 SVG、生成测试表、渲染 PNG、导出图标集
  - 流程固定在检查点停下：先给出概念总览与推荐，用户选定方向后才制作完整套件
- **亮点**：
  - 参考库只用于研究构造与行业惯例，README 明确声明不用于复制
  - 测试含 16px 像素测试、单色、反白、眯眼、镜像与竞品货架对比
  - README 说明技能在能看图的模型上效果最好，因为它会自行渲染 PNG 再检查
- **适合**：使用 Claude Code、Gemini CLI、Codex CLI、Cursor 等支持 Agent Skills 的代理，需要做品牌标志与视觉识别设计的开发者、设计师和独立…
- **上手**：`/plugin marketplace add kaankiziltug/logo-design-skill` 在 Claude Code 中执行后，再运行 /plugin install logo-design@logo-design-skill；其他代理需把 skills/logo-d…

#### [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) ⭐ 6,995

> 11 个 Claude 技能，覆盖 YouTube 频道从选题到剪辑的各个环节

- **定位**：面向 YouTube 创作者的 Claude 技能包，包含脚本、标题缩略图配对、剪辑决策、留存分析、Shorts 切分等 11 个命令，并配有 6 个零依赖 Python 工具；免费、MIT 许可、无需注册或 API Key。
- **能做什么**：
  - /yt-script 按 21 个钩子公式生成脚本并给钩子打分
  - /yt-package 把标题与缩略图作为一组配对做 lint
  - /yt-retention 读留存导出，定位观众流失的具体秒数
  - /yt-edit 从转录稿生成带时间码的剪辑决策表
  - /yt-shorts 从长视频中找出可切分的 Shorts
- **亮点**：
  - 6 个 Python 工具仅需纯净 Python 3，无第三方依赖
  - 不自动发布，所有技能都以人工确认收尾
  - hookscore.py 项目方数据：基于 74 个真实短视频钩子校准
- **适合**：希望用 Claude 辅助运营 YouTube 频道的创作者与内容团队，需要本地安装 Claude Code 以使用 Python 工具。
- **上手**：`git clone https://github.com/Jakeschincariol/youtube-agent-skill.git
cp -r youtube-agent-skill/skills/yt-* ~/.claude/skills/` 也可作为插件安装，或不装 Claude Code 直接粘贴单个 SKILL.md；建议先填写 templates/voice.md。
- ⚠️ /yt-viral 仅读取公开列表，但抓取第三方平台数据仍需留意平台服务条款。
- ⚠️ 快照当日已 68 天未更新（最后推送 2026-09-16）

#### [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) ⭐ 6,617

> 让 AI Agent 用一页 HTML 回答复杂问题的技能

- **定位**：一个面向 AI Agent 的技能：模型只写 Markdown 草稿，由随技能附带的 CLI 负责排版、配色和画图，输出单文件 HTML 页面。
- **能做什么**：
  - 模型只写 Markdown，CLI 生成版面、CSS 和 SVG 图
  - 按问题类型给出时序图、流程图、对比表、时间线等页面
  - 提供 blueprint、shadcn、paper 三种主题，均支持明暗模式
  - 每页为无外部依赖的单文件 HTML，可离线打开
  - 草稿出错时 CLI 返回行号和正确示例供修正
- **亮点**：
  - 项目方数据：模型输出 token 从 4893 降到 612，约为原来的 1/8
  - 项目方数据：同样问题耗时从 31 秒降到 12 秒
  - 项目方数据：账单只降约 15%，因为每轮仍需读取上下文
- **适合**：常用 Claude Code、Codex、Cursor 等 Agent 做技术解释、方案对比和代码梳理的开发者。
- **上手**：`npx skills add QingYunA/answer-me-with-html` 需 Node.js 20 以上，安装器会询问装进哪些 Agent；装完无需额外配置。

#### [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) ⭐ 5,581

> 给编码 Agent 用的音效生成工具，用一句话描述即可渲染出音效代码。

- **定位**：earshot 面向 Claude Code 等编码 Agent 及与之协作的人。它从 922 个音效设计中检索需求，并用代码渲染新版音效；目录中没有的，可用录制素材按配方拼出，再由听音模型评估。
- **能做什么**：
  - 922 个设计、384 个音效族，309 个由 692 段公共领域录音学习而来
  - 目录缺失时用 earshot build 按 JSON 配方拼装录音部件
  - 听音功能可描述音效、判断匹配度、检测录音还是合成
  - 提供 20 个工具的 MCP 服务、Claude Code 插件与两个 Agent skill
  - 内置 252 个影片音效银行的代码，以及 99 个配方手册
- **亮点**：
  - 纯 CPU 运行，基础安装不下载模型，生成音效时无需联网
  - 仓库不含音频文件，所有音效均由代码按需渲染
- **适合**：为游戏、界面、影片写代码的 AI Agent 用户及音效设计相关人员。
- **上手**：`pip install "earshot @ git+https://github.com/Leonxlnx/earshot"` 需 Python 3.10+，仅合入 CPU；写入 ogg/mp3 等格式需 ffmpeg；PyPI 上的 earshot 是别的项目。

### 开发者工具与集成

#### [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) ⭐ 10,644

> 面向 Claude 的开源 SEO 与 GEO 技能包，配免费 SEO MCP 服务

- **定位**：通过 Ryze MCP 连接器把 Claude 接到用户自己的 Search Console、GA4 和广告账号，用真实排名与流量数据执行 SEO 与 AI 可见性分析；技能以 MIT 协议开源。
- **能做什么**：
  - seo-audit：检查索引、CTR 异常、衰减页面与快速收益
  - keyword-research：从种子词到搜索量、意图和聚类关键词计划
  - rank-tracking：对比任意两个周期的排名变化，数据来自 GSC
  - competitor-gap / backlink-check：找竞品有而自己没有的关键词与外链
  - ai-visibility：从 GA4 的 AI 引荐流量看各 AI 引擎带来的访问与引用页面
- **亮点**：
  - 排名取自真实 Search Console 位置，流量取自真实 GA4，而非抓取估算
  - 插件已打包连接器，在 Claude Code 中可直接安装技能
  - 技能为 Markdown 文件，也可复制到任意支持 MCP 的客户端
- **适合**：用 Claude 或 Claude Code 做 SEO、内容与增长分析的人，以及想改写或扩展 SEO 技能的作者。
- **上手**：`claude mcp add ryze --transport http https://connector.get-ryze.ai/mcp` 安装插件时这一步可选；之后还需执行 claude plugin marketplace add Ryze-AI-Adgent/open-seo-mcp-skills 并安装插件。
- ⚠️ 数据经第三方托管的 get-ryze.ai 连接器转发，需信任其对 Search Console、GA4 与广告账号数据的处理

#### [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) ⭐ 8,804

> 通过 adb 关闭国产安卓系统广告的脚本与桌面客户端

- **定位**：用 adb 驱动手机，按机型脚本自动进入各厂商系统与 App 设置页，关闭个性化广告、热搜资讯、推广位和营销通知，无需 root，可以用一条命令还原。
- **能做什么**：
  - 只调用系统与 App 自带的设置开关，不卸载也不停用系统应用
  - 机型脚本按型号和系统版本存放，版本不匹配时会提示，找不到入口就跳过
  - 营销通知按渠道关闭，订单、快递、更新类通知保留
  - 广告组件用 pm suspend 挂起，这一步需要机主同意
  - 提供 AI 智能体执行、聊天 AI 引导、手动清单、桌面客户端四种用法
- **亮点**：
  - 不 root、不解锁、不刷机，系统更新不受影响
  - 广告跟踪（OAID）、搜索热榜、负一屏资讯、商店推广位都在处理范围内
  - README 列出的适配机型约 40 款，覆盖小米、OPPO、vivo、荣耀、魅族等品牌
- **适合**：使用小米、OPPO、vivo、荣耀、魅族等国产安卓手机，想清理系统广告但不想 root 的用户
- **上手**：`pip3 install -r requirements.txt` 先装依赖，再用 python3 tool/run.py devices 查看设备与机型脚本；首次需在手机上开启开发者模式和 USB 调试。
- ⚠️ 挂起广告组件和关闭系统开关可能影响部分系统功能，README 要求改动前先备份
- ⚠️ 机型与系统版本不匹配时脚本可能点错入口，README 声明使用后果由使用者自行承担

#### [vercel-labs/ui](https://github.com/vercel-labs/ui) ⭐ 6,602

> 供 AI Agent 构建无头 UI 组件的交互行为库

- **定位**：把键盘导航、焦点、选择、弹窗、拖拽和 ARIA 等交互行为抽象为 Agent 可组合的 primitives，再通过适配器在 React、Vue、Svelte、Solid、Web Components 中渲染。
- **能做什么**：
  - @ui-sdk/core 提供焦点、选择、弹窗、拖拽与 ARIA 行为
  - 提供 React、Vue、Svelte、Solid、Web Components 五个适配器
  - 用 definePrimitive 定义组件行为，用 createParts 在各框架渲染
  - 附带 UI SDK skill，可让 Agent 编写组件行为
- **亮点**：
  - 基于 behaviors 组合而非固定组件，一套行为跨五个框架复用
  - README 称无需手写行为代码，Agent 会完成编写
  - Apache-2.0 开源，项目仍处 beta，API 可能变化
- **适合**：使用 AI Agent 开发前端、需要跨框架无头交互组件的前端与设计系统团队
- **上手**：`npm install @ui-sdk/react @ui-sdk/core` 使用其他框架时把 @ui-sdk/react 换成 @ui-sdk/vue、@ui-sdk/svelte、@ui-sdk/solid 或 @ui-sdk/web

#### [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan) ⭐ 6,316

> 让 Claude 或 Codex 读取代码库，生成可交互的纯英文架构地图。

- **定位**：面向用 AI 构建应用但不读代码的人：Claude Code 或 Codex 扫描代码后，自动生成可缩放的地图，展示各部件、文件、端点、页面及前后端请求关系，并附带健康检查。
- **能做什么**：
  - 按层级缩放查看整体、部件、文件与端点
  - 用日常英语命名每个部分，悬停解释技术词
  - 跨仓库匹配前端请求与后端端点
  - 健康检查：代码内密钥、开放的表规则、可伪造的 webhook
  - 可选蓝图：从 PRD 规划尚未构建的应用
- **亮点**：
  - 脚本负责扫描与布局，模型只负责命名和描述
  - 全部在本机运行，不写依赖，地图可离线使用
  - 地图保存在 floorplan/ 目录并自我忽略，不入 git
- **适合**：用 Claude Code 或 Codex 构建应用、希望看懂代码结构与安全隐患的开发者与团队。
- **上手**：`claude plugin marketplace add haydenschmitty/floorplan` 需 Node.js 18+ 与 Claude Code；安装后新开会话，对项目说"Make me a floorplan of this app"。

### 安全防护与合规

#### [qybaihe/bla](https://github.com/qybaihe/bla) ⭐ 6,443

> 对抗 AI 逆向工程代理的软件加固 MCP 服务器与 CLI

- **定位**：BLA 面向软件作者，通过欺骗、耗尽分析预算、诱饵状态机等手段，让 AI 逆向工程代理难以还原发布产物的核心逻辑，覆盖 JS/TS、Electron、WASM、原生二进制、SQLite、GGUF 等格式。
- **能做什么**：
  - 一条命令自动发现构建产物并执行审计、保护、验证
  - 把可识别的分析预算上限设置得极低，触发逆向代理的资源上限
  - 植入格式合法诱饵与蜜罐 SourceMap，制造互相冲突的假设
  - 将 JS、WASM、原生附属文件通过运行时摘要互绑，防止剥离
  - 支持 Vite、Rollup、Webpack、esbuild 打包插件接入
- **亮点**：
  - 项目方数据：对真实 morluto/rea 实测 12 类格式触发预算或容量错误
  - 项目方数据：14/14 自带基准目标通过输入输出等价测试
  - 项目方数据：建模 token 放大 300×–2,800×
- **适合**：需要保护自有发布产物、防止 AI 逆向代理复刻逻辑的软件作者与安全团队
- **上手**：`npx bla-agents harden .` 需 Node.js ^22.23.4 或 >=24；自动发现 dist/、.asar、.wasm 等构建输出。
- ⚠️ 仅限保护自有软件；README 声明不得用于第三方产物

### 攻击性安全（仅限授权测试）

> ⚠️ 渗透测试、漏洞利用、红队等攻击性工具，只能用于自己拥有或获得书面授权的系统，未经授权使用可能违法。

#### [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX) ⭐ 16,684

> 自托管、由 LLM 驱动、带证据留痕的自主渗透测试平台

- **定位**：ARTEX 是一个自托管的 LLM 驱动渗透测试平台，由规划器将目标拆分为意图、Worker 调用真实工具执行，结果写入资产图与探索图两张关联图，每条发现都可绑定原始请求响应作证据。
- **能做什么**：
  - 规划器拆分目标、Worker 执行意图并写回，形成闭环
  - 双图架构：全局资产图与每任务探索图，用锚点关联
  - 记录型 MITM 代理与浏览器扩展采集真实流量作证据
  - 人工审批门、argv 前缀规则、范围门与 token/轮次预算
  - 支持自建 Anthropic/OpenAI 兼容端点或本地 Ollama
- **亮点**：
  - 发现需绑定证据响应与逐字引用才算 verified
  - retester 代理可复测漏洞并记录仍可复现/已修复/无法确认
  - 单 Go 二进制内嵌 Next.js UI，PostgreSQL 存储
- **适合**：授权范围内做渗透测试与红队评估的安全团队，会自行部署并配置 LLM 端点
- **上手**：`docker compose up -d --build` 先 git clone 并 cp .env.example .env 设置 POSTGRES_PASSWORD，启动后访问 http://localhost:8787，用日志中的…
- ⚠️ 攻击性安全工具，仅限在获得明确授权的目标上使用。
- ⚠️ 浏览器扩展会采集会话流量并发送到本地 ARTEX 服务。

### 其他

#### [Albert-Weasker/niubigeo](https://github.com/Albert-Weasker/niubigeo) ⭐ 10,087

> 开源自托管的 GEO 研究工具，追踪品牌和多模型在 AI 回答中的可见度

- **定位**：输入域名或关键词，调用多个模型进行测试，保存原始回答、引用来源和竞品信息，并支持重复运行与定时监测，数据存放在自己环境中。
- **能做什么**：
  - 输入域名后看各模型如何描述产品、点名哪些竞品
  - 用不含品牌名的关键词测试谁会被 AI 推荐
  - 保留原始回答、引用和普通链接，失败也记录
  - 支持多模型与 OpenRouter、直连 API、自定义端点混测
  - 关键词监测可定时运行并用 Diff View 对比变化（v0.3 Beta）
- **亮点**：
  - 答案到引用全链路可查，不输出单一黑盒分数
  - 自带 20 个真实案例，无需安装或 API Key 即可阅读
  - 每条结果保留端点、模型和搜索设置
- **适合**：关注 AI 搜索可见度（GEO）的品牌、市场与增长团队，以及希望自托管数据、自行验证结果的开发者。
- **上手**：`git clone --branch v0.3.2 --depth 1 https://github.com/Albert-Weasker/niubigeo.git
cd niubigeo
npm ci
cp .env.example .env
npm run server` 需 Node.js 22.13+，在 .env 填 OPENROUTER_API_KEY 后启动，访问 localhost:8787；模型和搜索 API 费用自付。
- ⚠️ 发送给外部模型 API 的提示词会离开自托管环境，README 明确说明自托管不等于零数据暴露
- ⚠️ 工作台默认显示视频顾问卡片，点击会跳转第三方外部服务
- ⚠️ 定时监测需额外运行 monitoring worker 容器

## 已排除（判定与 AI 无关）
- tangency-labs/solidcraft：一个早期但可用的参数化 CAD 应用，用草图约束和特征时间线建模，同一套命令可在桌面端、浏览器、无头 CLI 和 MCP 服务器上运行。
- yihui-dev/awesome-opus5-5-videos：收录创作者用 Claude Opus 5.5 让模型以代码形式绘制动画（HTML、Canvas、SVG、Three.js 等）做出的视频，并附上对应提示词或原始发布链接，方便读者复制 prompt 自行尝试。
- Mak5er/AirCard：基于 airlift AirTraffic 同步漏洞的 macOS 应用，可替换 Apple Wallet 卡片皮肤和锁屏密码键盘主题，无需越狱。
- omlahore/RemoveMacAI：一个原生 App 加同款 CLI，用来关掉 Apple Intelligence 及其模型，并关闭系统遥测、个性化广告、弹窗和其他应用的更新器；所有改动先预览，且都可撤销。
- shader-effects-inc/shaders：把 WebGPU 着色器效果封装成声明式组件，可嵌套、混合和遮罩，同一包内为各前端框架提供一致的 props；另配可视化设计编辑器，可导出代码。
