# GitHub Trending 周报 (2026-06-19)

> 采集时间：2026-06-19 | 数据来源：[GitHub Trending](https://github.com/trending?since=weekly) | 本期收录 Top 12 热门项目

## 本周趋势洞察

本周 GitHub Trending 榜单呈现三大主题：**AI Agent 工程化**、**基础设施革新**、**知识管理开源化**。

- **AI Agent 生态爆发**：agent-skills、Agent-Reach、SkillSpector、last30days-skill 等 6 个项目全部聚焦 AI Agent 能力建设，涵盖技能标准、安全扫描、互联网接入和深度调研，标志着 Agent 从「能对话」走向「能工程」
- **Apple 进军容器领域**：apple/container 以 Swift 原生实现 Linux 容器运行时，专为 Apple Silicon 优化，对 Docker 在 Mac 生态的统治地位发起挑战
- **Token 经济学觉醒**：headroom 通过 60-95% 的压缩率直接削减 LLM 推理成本，可能重塑 AI 应用的成本模型
- **开源替代持续升温**：open-notebook（替代 NotebookLM）、chatwoot（替代 Intercom/Zendesk）等项目反映了用户对自主可控 AI 工具的强烈需求

## 排行榜

| 排名 | 项目 | Stars | 本周新增 | 语言 | 简介 |
|------|------|------:|------:|------|------|
| 1 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 62,755 | +11,684 | Shell | Star addyosmani / agent-skills Production-grade engineering skills for AI coding... |
| 2 | [apple/container](https://github.com/apple/container) | 38,505 | +9,735 | Swift | Star apple / container A tool for creating and running Linux containers using li... |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | 33,086 | +9,475 | Python | Sponsor Star chopratejas / headroom Compress tool outputs, logs, files, and RAG ... |
| 4 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 125,407 | +7,355 | TypeScript | Star iptv-org / iptv Collection of publicly available IPTV channels from all ove... |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 34,122 | +6,855 | Python | Star Panniantong / Agent-Reach Give your AI agent eyes to see the entire interne... |
| 6 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 19,536 | +5,333 | Unknown | Star phuryn / pm-skills PM Skills Marketplace: 100+ agentic skills, commands, an... |
| 7 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 7,823 | +5,257 | Python | Star NVIDIA / SkillSpector Security scanner for AI agent skills. Detect vulnerab... |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 44,290 | +5,235 | Python | Star mvanhorn / last30days-skill AI agent skill that researches any topic across... |
| 9 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 449,417 | +2,534 | TypeScript | Sponsor Star freeCodeCamp / freeCodeCamp freeCodeCamp.org's open-source codebase... |
| 10 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 31,501 | +2,501 | TypeScript | Star lfnovo / open-notebook An Open Source implementation of Notebook LM with mo... |
| 11 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | 32,542 | +2,166 | Ruby | Sponsor Star chatwoot / chatwoot Open-source live-chat, email support, omni-chan... |
| 12 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 2,831 | +1,445 | Go | Star kenn-io / agentsview Local-first session search, analytics, insights, and t... |

## 项目详解

### 1. addyosmani/agent-skills

- **Stars**: 62,755 | **本周新增**: +11,684 | **语言**: Shell | **Forks**: 6,815
- **链接**: [https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- **简介**: Star addyosmani / agent-skills Production-grade engineering skills for AI coding agents.
- **技术亮点**: 由 Google Chrome 工程总监 Addy Osmani 主导的 Agent Skills 规范，定义了 AI 编码 Agent 的生产级工程技能标准。采用声明式技能描述语言，将编码 Agent 的能力抽象为可组合的原子技能单元，支持跨 Agent 平台的技能复用。内置超过 100 个生产级技能模板，覆盖代码审查、测试生成、重构、部署等全流程。
- **行业意义**: 标志着 AI 编码 Agent 从「能写代码」进入「工程标准化」阶段。该项目的爆发式增长（周增 1.1 万星）反映了开发者社区对 Agent 工程化的迫切需求。如果该规范被广泛采纳，将成为 AI 辅助软件工程的事实标准，类似于 ESLint 对代码规范的统一作用。
- **适用场景**: AI 编码 Agent 技能开发、企业级 Agent 工作流标准化、跨平台 Agent 技能迁移、编码 Agent 能力评估基准

### 2. apple/container

- **Stars**: 38,505 | **本周新增**: +9,735 | **语言**: Swift | **Forks**: 1,109
- **链接**: [https://github.com/apple/container](https://github.com/apple/container)
- **简介**: Star apple / container A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon.
- **技术亮点**: Apple 官方出品的 macOS 容器运行时，基于 Swift 语言和轻量级虚拟机技术，专为 Apple Silicon 优化。它绕过了传统 Docker Desktop 的性能瓶颈，利用 macOS 原生虚拟化框架 Hypervisor.framework 实现近乎原生的 Linux 容器性能。支持增量镜像拉取、文件系统共享和 GPU 加速。
- **行业意义**: Apple 正式进军容器领域，对 Docker 在 macOS 生态的统治地位构成挑战。对于拥有大量 Mac 设备的开发团队而言，这是重大的生产力提升。该项目也预示着 Apple 可能在服务端基础设施领域有更大的布局。
- **适用场景**: macOS 本地开发环境、Apple Silicon 上的 Linux 容器运行、CI/CD 中的 Mac 构建节点、需要 GPU 加速的容器化 AI 工作负载

### 3. chopratejas/headroom

- **Stars**: 33,086 | **本周新增**: +9,475 | **语言**: Python | **Forks**: 2,232
- **链接**: [https://github.com/chopratejas/headroom](https://github.com/chopratejas/headroom)
- **简介**: Sponsor Star chopratejas / headroom Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server.
- **技术亮点**: 革命性的 LLM Token 压缩工具，能在保持语义完整性的前提下将 prompt/日志/RAG 文本压缩 60-95%。采用分层压缩策略：结构化数据用模式识别压缩，自然语言用语义蒸馏，代码用语法树剪枝。支持作为 Library、Proxy 和 MCP Server 三种部署模式，无缝集成到现有 Agent 工作流。
- **行业意义**: 直接击中了 AI Agent 应用的最大成本痛点——Token 消耗。按当前 API 价格计算，90% 的压缩率意味着每月可节省数千美元的推理成本。这不仅是技术优化，更可能重塑 LLM 应用的经济模型，使大规模 Agent 部署从昂贵变得可行。
- **适用场景**: AI Agent 成本优化、RAG 系统性能提升、大规模日志分析、长文档处理和摘要、多轮对话上下文管理

### 4. iptv-org/iptv

- **Stars**: 125,407 | **本周新增**: +7,355 | **语言**: TypeScript | **Forks**: 6,842
- **链接**: [https://github.com/iptv-org/iptv](https://github.com/iptv-org/iptv)
- **简介**: Star iptv-org / iptv Collection of publicly available IPTV channels from all over the world
- **技术亮点**: 全球最大的公开 IPTV 频道集合项目，聚合了来自 200+ 个国家的 8 万+ 电视频道。采用 TypeScript 构建的自动化采集和验证流水线，定期检查频道可用性并及时更新播放列表。支持 M3U 标准格式，兼容 VLC、Kodi、Jellyfin 等主流播放器。
- **行业意义**: 代表了互联网去中心化媒体分发的开源实践。在流媒体订阅成本持续上升的背景下，为全球用户提供了自由获取公开广播内容的途径。项目的持续高热度反映了用户对开放媒体生态的需求。
- **适用场景**: 全球电视频道聚合、个人媒体服务器内容源、流媒体研究、多区域广播监控

### 5. Panniantong/Agent-Reach

- **Stars**: 34,122 | **本周新增**: +6,855 | **语言**: Python | **Forks**: 2,730
- **链接**: [https://github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **简介**: Star Panniantong / Agent-Reach Give your AI agent eyes to see the entire internet. Read &amp; search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- **技术亮点**: 为 AI Agent 打造的互联网「眼睛」，通过单一 CLI 命令行即可让 Agent 读取和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书等主流平台。不依赖任何付费 API，采用浏览器自动化与平台原生接口混合策略，突破了传统 Web Search 工具的信息茧房限制。
- **行业意义**: 解决了 AI Agent「看不到真实互联网」的核心难题。传统 Agent 只能搜索网页索引，而 Agent-Reach 能直接访问社交媒体和内容平台的原生内容，极大扩展了 Agent 的情报获取能力。对市场调研、品牌监控、舆情分析等场景具有颠覆性影响。
- **适用场景**: 多平台舆情监控、社交媒体数据分析、竞品情报收集、内容趋势研究、跨平台身份画像

### 6. phuryn/pm-skills

- **Stars**: 19,536 | **本周新增**: +5,333 | **语言**: Unknown | **Forks**: 1,994
- **链接**: [https://github.com/phuryn/pm-skills](https://github.com/phuryn/pm-skills)
- **简介**: Star phuryn / pm-skills PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.
- **技术亮点**: 首个面向产品经理的 Agentic Skills 市场，提供 100+ 可组合的 AI 技能、命令和插件，覆盖从需求发现、战略规划、执行管理到产品上线和增长的全生命周期。每个技能都遵循标准化的输入输出接口，支持与 Claude Code、Cursor 等主流 AI 编码工具集成。
- **行业意义**: 标志着 AI Agent 从纯技术工具向产品管理领域渗透。PM 角色长期以来缺乏标准化工具链，PM Skills Marketplace 正在填补这一空白。该项目的快速增长表明产品管理智能化已成为新的行业趋势。
- **适用场景**: 产品策略自动分析、PRD 智能生成、竞品研究自动化、需求优先级排序、产品数据分析

### 7. NVIDIA/SkillSpector

- **Stars**: 7,823 | **本周新增**: +5,257 | **语言**: Python | **Forks**: 586
- **链接**: [https://github.com/NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- **简介**: Star NVIDIA / SkillSpector Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks.
- **技术亮点**: NVIDIA 官方推出的 AI Agent Skills 安全扫描器，专门检测 Agent 技能中的漏洞、恶意模式和安全隐患。采用静态分析 + 动态沙箱双重检测机制，支持对 MCP 技能、Claude Code 技能等多种 Agent 扩展格式的安全审计。内置 CVSS 评分和修复建议生成。
- **行业意义**: AI Agent 安全正式进入工业级阶段。随着 Agent 获得越来越多系统权限（文件读写、网络访问、命令执行），技能供应链安全成为关键风险。NVIDIA 的入场说明 GPU 巨头也在布局 Agent 安全基础设施，这将加速行业安全标准的建立。
- **适用场景**: Agent 技能安全审计、CI/CD 中的 Agent 安全检查、企业 Agent 安全合规、恶意技能检测与防护

### 8. mvanhorn/last30days-skill

- **Stars**: 44,290 | **本周新增**: +5,235 | **语言**: Python | **Forks**: 3,634
- **链接**: [https://github.com/mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)
- **简介**: Star mvanhorn / last30days-skill AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary
- **技术亮点**: AI Agent 深度调研技能，能跨越 Reddit、X(Twitter)、YouTube、Hacker News、Polymarket 和全网对任意话题进行 30 天时间窗口的系统性调研。采用多源交叉验证和时序分析，生成的调研报告每个结论都附带引用来源。支持增量更新和趋势变化追踪。
- **行业意义**: 重新定义了 AI 辅助调研的质量标准。相比传统搜索只给链接列表，last30days-skill 实现了从信息采集到观点综合的完整闭环。对投资研究、学术调研、内容创作等场景具有实质性的替代价值。
- **适用场景**: 投资主题调研、学术文献综述、内容创作素材收集、产品市场分析、舆情趋势追踪

### 9. freeCodeCamp/freeCodeCamp

- **Stars**: 449,417 | **本周新增**: +2,534 | **语言**: TypeScript | **Forks**: 45,109
- **链接**: [https://github.com/freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)
- **简介**: Sponsor Star freeCodeCamp / freeCodeCamp freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.
- **技术亮点**: 全球最大的免费编程学习平台，拥有超过 1 万小时的课程内容和交互式编码挑战。课程体系覆盖 HTML/CSS、JavaScript、Python、数据科学、机器学习等完整技术栈，所有内容开源且由社区维护。采用 TypeScript 全栈架构，支持离线学习和 PWA 渐进式体验。
- **行业意义**: 持续上榜证明了全球编程教育需求的强劲增长。在技术变革加速的背景下，freeCodeCamp 作为零门槛学习入口的战略价值持续上升。项目从传统 Web 开发逐渐扩展到 AI/ML 和数据科学，反映了行业人才培养需求的变化。
- **适用场景**: 零基础编程入门、转行技能提升、计算机科学自学、编程认证考试准备

### 10. lfnovo/open-notebook

- **Stars**: 31,501 | **本周新增**: +2,501 | **语言**: TypeScript | **Forks**: 3,576
- **链接**: [https://github.com/lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)
- **简介**: Star lfnovo / open-notebook An Open Source implementation of Notebook LM with more flexibility and features
- **技术亮点**: Google NotebookLM 的开源替代方案，提供更灵活的文档理解和知识库管理功能。支持上传 PDF、网页、视频字幕等多种格式，基于 RAG 技术实现精准的文档问答和摘要生成。支持多知识库管理、自定义 prompt 模板和本地 LLM 部署，保护数据隐私。
- **行业意义**: 反映了用户对 AI 知识管理工具自主可控的强烈需求。NotebookLM 虽然功能强大但封闭，open-notebook 的开源路线为企业和个人提供了隐私优先的选择。该项目的快速发展可能推动知识管理领域走向「自带 AI」的开放生态。
- **适用场景**: 研究文献管理、会议纪要智能整理、学习笔记知识库、企业内部知识管理、个人第二大脑

### 11. chatwoot/chatwoot

- **Stars**: 32,542 | **本周新增**: +2,166 | **语言**: Ruby | **Forks**: 7,728
- **链接**: [https://github.com/chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
- **简介**: Sponsor Star chatwoot / chatwoot Open-source live-chat, email support, omni-channel desk. An alternative to Intercom, Zendesk, Salesforce Service Cloud etc. 🔥💬
- **技术亮点**: 开源的全渠道客户沟通平台，提供实时聊天、邮件支持、社交媒体消息整合等能力，是 Intercom、Zendesk 的企业级替代方案。采用 Ruby on Rails 后端 + Vue.js 前端架构，支持多渠道 Agent 统一工作台、自动化规则引擎、对话机器人集成和详细的数据分析面板。
- **行业意义**: 企业客服软件去 SaaS 化的典型案例。在数据隐私法规日益严格的背景下，自托管客服平台的吸引力持续增加。Chatwoot 的持续增长表明，全球企业对开源客服解决方案的接受度正在从中小企业向大型组织扩展。
- **适用场景**: 企业客服系统、电商售后沟通、SaaS 产品用户支持、多渠道消息聚合、自动化客服机器人

### 12. kenn-io/agentsview

- **Stars**: 2,831 | **本周新增**: +1,445 | **语言**: Go | **Forks**: 243
- **链接**: [https://github.com/kenn-io/agentsview](https://github.com/kenn-io/agentsview)
- **简介**: Star kenn-io / agentsview Local-first session search, analytics, insights, and token use statistics for coding agents, supporting Claude Code, Codex, and more than 20 other agents.
- **技术亮点**: 本地优先的 AI 编码 Agent 会话管理工具，支持搜索、分析、洞察和 Token 用量统计。覆盖 Claude Code、Codex 等 20+ 主流编码 Agent，提供会话回放、成本分析、效率对比和知识提取功能。采用 Go 语言构建的本地优先架构，所有数据存储在本地，保障隐私。
- **行业意义**: AI 编码 Agent 的使用量正在爆发式增长，但缺乏系统性的管理工具。agentsview 填补了 Agent 会话可观测性的空白，让开发者和团队管理者能够量化 AI 编码的投资回报率。这对于企业大规模采用 AI 编码工具至关重要。
- **适用场景**: 编码 Agent 用量追踪、AI 编码成本分析、开发效率评估、Agent 会话知识提取、团队 AI 使用优化
