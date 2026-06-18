# GitHub Trending AI 周报 — 2026-06-08 ~ 2026-06-15

> 采集时间：2026-06-18T00:00:00+08:00

| # | 项目 | Stars | ⬆本周 | 语言 | 简介 |
|---|------|------:|------:|------|------|
| 1 | [last30days-skill](https://github.com/mvanhorn/last30days-skill) | 42,325 | +12,053 | Python | AI Agent 技能，跨 Reddit/X/YouTube/HN/Polymarket 全平台调研并生成有据可依的摘要 |
| 2 | [headroom](https://github.com/chopratejas/headroom) | 26,000 | +10,000 | Python | AI Agent 专用上下文压缩层，将 Token 消耗降低 60-95% |
| 3 | [taste-skill](https://github.com/Leonxlnx/taste-skill) | 43,000 | +8,700 | Shell | 为 AI Agent 打造的反模板化前端技能集，解决 AI 生成 UI 千篇一律的问题 |
| 4 | [agent-skills](https://github.com/addyosmani/agent-skills) | 58,000 | +8,300 | Shell | Addy Osmani 创建的生产级 AI 编程 Agent 技能库，将高级工程实践封装为可执行命令 |
| 5 | [markitdown](https://github.com/microsoft/markitdown) | 152,000 | +7,000 | Python | 微软开源的多格式文件转 Markdown 工具，专为 LLM 文本分析管道优化 |
| 6 | [agent-skills](https://github.com/anthropics/skills) | 27,000 | +5,400 | Python | Anthropic 官方公开的 Agent Skills 仓库，展示技能生态的标准范式与最佳实践 |
| 7 | [pm-skills](https://github.com/phuryn/pm-skills) | 12,480 | +4,800 | Markdown | 产品经理技能市场，将 12 位顶级 PM 方法论编码为 Agent 可执行的工作流 |
| 8 | [supervision](https://github.com/roboflow/supervision) | 44,000 | +4,000 | Python | Roboflow 出品的计算机视觉通用工具包，月下载量超百万 |
| 9 | [SkillSpector](https://github.com/NVIDIA/SkillSpector) | 4,000 | +2,600 | Python | NVIDIA 推出的 AI Agent 技能安全扫描器，为技能生态提供安全保障 |
| 10 | [goose](https://github.com/aaif-goose/goose) | 49,000 | +2,500 | Rust | 已移交 Linux Foundation AAIF 的开源通用 AI Agent，经 Block 12000 名员工验证 |
| 11 | [CopilotKit](https://github.com/CopilotKit/CopilotKit) | 35,000 | +2,500 | TypeScript | 构建 Agent 原生应用的开源框架，支持前端框架深度集成 AI Agent 能力 |
| 12 | [codex-plugins](https://github.com/openai/codex-plugins) | 2,900 | +1,400 | JavaScript | OpenAI 官方 Codex 插件示例集合，展示多场景 AI 开发插件的最佳实践 |

---

## 1. [last30days-skill](https://github.com/mvanhorn/last30days-skill)

- **作者**: mvanhorn
- **Stars**: 42,325 | **本周新增**: +12,053
- **语言**: Python
- **简介**: AI Agent 技能，跨 Reddit/X/YouTube/HN/Polymarket 全平台调研并生成有据可依的摘要
- **核心特性**:
  - 跨平台并行搜索与数据聚合，覆盖 Reddit/X/YouTube/HN/Polymarket 等社区
  - 基于社区投票、互动与押注的真实信号排序算法
  - AI 自动合成带引用源的综述报告，可直接验证每一条结论
- **适用场景**:
  - 内容创作者
  - 行业研究员
  - 技术趋势分析
  - 竞品情报收集

## 2. [headroom](https://github.com/chopratejas/headroom)

- **作者**: chopratejas
- **Stars**: 26,000 | **本周新增**: +10,000
- **语言**: Python
- **简介**: AI Agent 专用上下文压缩层，将 Token 消耗降低 60-95%
- **核心特性**:
  - 6 种可配置压缩算法，支持摘要/截断/结构化等多种策略
  - 支持库/代理/MCP Server 三种接入模式，灵活适配不同架构
  - 本地优先可逆压缩，保证信息不丢失且无需上传数据到第三方
- **适用场景**:
  - LLM 应用开发者
  - AI Agent 构建者
  - 推理成本敏感团队
  - 长文档处理

## 3. [taste-skill](https://github.com/Leonxlnx/taste-skill)

- **作者**: Leonxlnx
- **Stars**: 43,000 | **本周新增**: +8,700
- **语言**: Shell
- **简介**: 为 AI Agent 打造的反模板化前端技能集，解决 AI 生成 UI 千篇一律的问题
- **核心特性**:
  - 高质量布局/排版/动效/间距方案注入，彻底告别样板化界面
  - 图像生成技能配合视觉参考板，提供完整的设计方向指引
  - 多平台 UI 设计智能适配，支持 Web/Mobile/Desktop 不同终端
- **适用场景**:
  - 前端开发者
  - AI 编程助手用户
  - UI/UX 设计师
  - 快速原型构建

## 4. [agent-skills](https://github.com/addyosmani/agent-skills)

- **作者**: addyosmani
- **Stars**: 58,000 | **本周新增**: +8,300
- **语言**: Shell
- **简介**: Addy Osmani 创建的生产级 AI 编程 Agent 技能库，将高级工程实践封装为可执行命令
- **核心特性**:
  - 7 阶段开发生命周期命令：/spec→/plan→/build→/test→/review→/code-simplify→/ship
  - 斜杠命令自动激活对应技能集，Agent 无需额外配置即可遵循最佳实践
  - 一键自动构建覆盖从想法到上线的完整流程
- **适用场景**:
  - 软件工程师
  - AI 编程 Agent
  - 团队开发标准化
  - 全栈项目交付

## 5. [markitdown](https://github.com/microsoft/markitdown)

- **作者**: microsoft
- **Stars**: 152,000 | **本周新增**: +7,000
- **语言**: Python
- **简介**: 微软开源的多格式文件转 Markdown 工具，专为 LLM 文本分析管道优化
- **核心特性**:
  - 支持 PDF/Word/PPT/Excel/HTML/图片/音视频/YouTube 等十余种格式
  - 保留标题/列表/表格/链接等文档结构，转换质量业界领先
  - 内置 OCR 文字识别与语音转录，覆盖非文本文档场景
- **适用场景**:
  - RAG 应用开发者
  - 文档知识库构建
  - LLM 数据预处理
  - 非结构化数据转换

## 6. [agent-skills](https://github.com/anthropics/skills)

- **作者**: anthropics
- **Stars**: 27,000 | **本周新增**: +5,400
- **语言**: Python
- **简介**: Anthropic 官方公开的 Agent Skills 仓库，展示技能生态的标准范式与最佳实践
- **核心特性**:
  - 官方技能模板与开发规范，降低技能创建门槛
  - Claude 生态下的可复用技能集合，覆盖多种业务场景
  - 持续更新的技能示例代码与文档
- **适用场景**:
  - Claude 开发者
  - Agent 技能设计者
  - AI 工具链集成

## 7. [pm-skills](https://github.com/phuryn/pm-skills)

- **作者**: phuryn
- **Stars**: 12,480 | **本周新增**: +4,800
- **语言**: Markdown
- **简介**: 产品经理技能市场，将 12 位顶级 PM 方法论编码为 Agent 可执行的工作流
- **核心特性**:
  - 68 个 PM 技能 + 42 个链式命令覆盖从产品发现到增长的完整生命周期
  - 9 大领域插件涵盖市场调研/数据分析/Go-to-Market/PRD 编写等
  - 跨 Claude Code/Cursor/Codex/Gemini 等 7 大 AI 平台兼容
- **适用场景**:
  - 产品经理
  - 创业团队
  - 产品策略制定
  - 需求管理与发布

## 8. [supervision](https://github.com/roboflow/supervision)

- **作者**: roboflow
- **Stars**: 44,000 | **本周新增**: +4,000
- **语言**: Python
- **简介**: Roboflow 出品的计算机视觉通用工具包，月下载量超百万
- **核心特性**:
  - 数据集加载/标注可视化/目标检测/追踪全流程工具链
  - 兼容 YOLO/SAM 等主流 CV 模型，即插即用
  - 实时区域计数与视频流分析，支持产线级部署
- **适用场景**:
  - 计算机视觉工程师
  - 工业质检
  - 安防监控
  - 自动驾驶感知

## 9. [SkillSpector](https://github.com/NVIDIA/SkillSpector)

- **作者**: NVIDIA
- **Stars**: 4,000 | **本周新增**: +2,600
- **语言**: Python
- **简介**: NVIDIA 推出的 AI Agent 技能安全扫描器，为技能生态提供安全保障
- **核心特性**:
  - 检测 64 种漏洞模式，覆盖提示注入/数据窃取/权限提升等 16 类风险
  - 0-100 风险评分量化，支持企业级安全策略配置
  - 支持终端/JSON/SARIF 多格式输出，可直接集成 CI/CD 流水线
- **适用场景**:
  - AI Agent 安全审计
  - 企业 AI 合规部署
  - 技能市场内容审核
  - DevSecOps 集成

## 10. [goose](https://github.com/aaif-goose/goose)

- **作者**: aaif-goose
- **Stars**: 49,000 | **本周新增**: +2,500
- **语言**: Rust
- **简介**: 已移交 Linux Foundation AAIF 的开源通用 AI Agent，经 Block 12000 名员工验证
- **核心特性**:
  - 桌面应用/CLI/API 三形态统一，覆盖开发到生产的全场景
  - 支持 15+ LLM 提供商和 70+ MCP 扩展，生态极其丰富
  - 编码/研究/写作/自动化/数据分析全场景能力，非局限于编程助手
- **适用场景**:
  - 全栈开发者
  - 研究人员
  - 自动化运维
  - 企业 AI 助手部署

## 11. [CopilotKit](https://github.com/CopilotKit/CopilotKit)

- **作者**: CopilotKit
- **Stars**: 35,000 | **本周新增**: +2,500
- **语言**: TypeScript
- **简介**: 构建 Agent 原生应用的开源框架，支持前端框架深度集成 AI Agent 能力
- **核心特性**:
  - 生成式 UI 动态渲染 Agent 输出，告别纯文本交互
  - 共享状态实现人机实时协作，Human-in-the-Loop 开箱即用
  - React/Angular/Vue/React Native 全框架支持
- **适用场景**:
  - 前端开发者
  - Agent 应用产品化
  - 企业 SaaS AI 功能集成
  - 交互式 AI 产品

## 12. [codex-plugins](https://github.com/openai/codex-plugins)

- **作者**: openai
- **Stars**: 2,900 | **本周新增**: +1,400
- **语言**: JavaScript
- **简介**: OpenAI 官方 Codex 插件示例集合，展示多场景 AI 开发插件的最佳实践
- **核心特性**:
  - 覆盖 Figma 设计/Notion 知识管理/iOS 开发/Web 部署等多场景插件
  - 每个插件含 manifest + 技能文件，结构清晰便于二次开发
  - 官方维护的插件开发参考，持续随 Codex 更新而迭代
- **适用场景**:
  - Codex 用户
  - 插件开发者
  - AI 开发工具链定制
  - IDE 扩展开发
