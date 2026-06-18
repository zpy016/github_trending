# GitHub Trending AI 周刊

## 项目概述

静态网页 + Python HTTP 服务器项目，生成 GitHub Trending AI 项目的周刊报告，提供 HTML 卡片、JSON、CSV、Markdown 四种格式的数据展示。

## 技术栈

- **语言**: Python 3.12（标准库，无外部依赖）
- **前端**: 纯静态 HTML/CSS
- **服务器**: Python `http.server` 模块
- **包管理**: 无（纯标准库）

## 目录结构

```
/workspace/projects/
├── .coze                    # Coze 项目配置
├── index.html               # 主入口页面
├── server.py                # HTTP 服务器入口（5000 端口）
├── requirements.txt         # 无外部依赖
├── scripts/
│   ├── coze-preview-build.sh
│   └── coze-preview-run.sh
└── trending-tracker/
    ├── github-trending-tracker.html  # 周刊卡片页面
    ├── trending_data.json            # 结构化数据
    ├── trending_data.csv             # CSV 表格
    └── trending_data.md              # Markdown 表格
```

## 关键入口 / 核心模块

| 文件 | 职责 |
|------|------|
| `server.py` | HTTP 服务器，监听 5000 端口，提供静态文件服务 |
| `index.html` | 主入口，展示周刊链接 |
| `trending-tracker/` | 周刊数据目录 |

## 运行与预览

- **预览端口**: 5000
- **预览命令**: `bash scripts/coze-preview-run.sh`
- **构建命令**: `bash scripts/coze-preview-build.sh`（无实际构建，输出 OK）
- **依赖安装**: 无（纯标准库）

## Coze 配置说明

- `project_type`: web（静态网页 + Python 服务器）
- `preview_enable`: enabled
- `requires`: python-3.12（白名单值）
- `entrypoint`: server.py
- `deploy.profile.kind`: service
- `deploy.profile.flavor`: web

## 用户偏好与长期约束

1. Python 脚本使用标准库，无需包管理器
2. 端口固定为 5000（HTTP 服务）
3. 预览脚本需具备幂等性（清理端口残留进程）

## 常见问题和预防

1. **端口冲突**: run 脚本已包含 `fuser -k 5000/tcp` 清理逻辑
2. **跨平台兼容**: 使用 Python 标准库，无外部依赖冲突
