#!/usr/bin/env python3
"""
GitHub Trending AI/ML 项目采集脚本
功能：
1. 使用 playwright 抓取 https://github.com/trending?since=weekly
2. 解析页面提取项目名、作者、Star 数、本周新增 Star、语言、URL、描述
3. 按关键词筛选 AI/ML 相关项目
4. 读取 trending_data.json，检查当前周期是否已有数据，已存在则跳过
5. 对筛选出的项目调用 OpenAI API 生成中文解读（有 API Key 时），或使用降级模板
6. 追加新周期数据并写入 JSON
7. 输出采集汇总到 stdout
"""

import asyncio
import json
import os
import re
import sys
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# 脚本所在目录
SCRIPT_DIR = Path(__file__).resolve().parent

# 数据文件路径
DATA_FILE = SCRIPT_DIR / "trending_data.json"

# AI/ML 筛选关键词
AI_KEYWORDS = [
    "ai", "llm", "machine-learning", "deep-learning", "gpt", "agent",
    "skill", "nlp", "cv", "transformer", "diffusion", "embedding",
    "rag", "mcp"
]

# 北京时间时区
TZ_BEIJING = timezone(timedelta(hours=8))


def get_current_period() -> dict:
    """计算当前周周期信息（ISO 周）"""
    now = datetime.now(TZ_BEIJING)
    # 取上一周（本周可能尚未结束）
    last_week = now - timedelta(days=7)
    iso_year, iso_week, _ = last_week.isocalendar()

    # 计算该周的起止日期
    monday = last_week - timedelta(days=last_week.weekday())
    sunday = monday + timedelta(days=6)

    return {
        "period": f"{iso_year}-W{iso_week:02d}",
        "date_range": f"{monday.strftime('%Y-%m-%d')} ~ {sunday.strftime('%Y-%m-%d')}",
        "fetch_time": now.strftime("%Y-%m-%dT%H:%M:%S+08:00"),
    }


def load_existing_data() -> dict:
    """加载已有的数据文件，不存在则返回空结构"""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                logger.info(f"已加载现有数据：{len(data.get('weeks', []))} 个周期")
                return data
        except (json.JSONDecodeError, OSError) as e:
            logger.warning(f"数据文件读取失败：{e}，将创建新文件")
    return {"weeks": []}


def save_data(data: dict):
    """保存数据到 JSON 文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info(f"数据已保存到 {DATA_FILE}")


def is_ai_project(name: str, summary: str, language: str, topics: list) -> bool:
    """判断项目是否属于 AI/ML 领域"""
    combined = f"{name.lower()} {summary.lower()} {' '.join(topics).lower()}"
    for keyword in AI_KEYWORDS:
        if keyword in combined:
            return True
    return False


def extract_star_number(text: str) -> int:
    """从文本中提取数字，处理逗号和 k 后缀"""
    text = text.strip().lower().replace(",", "")
    if text.endswith("k"):
        try:
            return int(float(text[:-1]) * 1000)
        except ValueError:
            return 0
    try:
        return int(text)
    except ValueError:
        return 0


def generate_fallback_interpretation(name: str, language: str, description: str) -> dict:
    """没有 API Key 时的降级模板生成"""
    desc_snippet = description[:60] if description else "开源"
    return {
        "summary": f"该项目是一个基于{language}的{desc_snippet}相关工具",
        "features": [
            f"基于{language}开发，充分利用语言生态优势",
            "开源社区活跃，持续迭代更新",
            "文档完善，上手成本低",
        ],
        "scenarios": ["开发者", "技术团队", "开源贡献者", "学习者"],
    }


def generate_ai_interpretation(repo_name: str, language: str, stars: int, description: str) -> dict:
    """调用 OpenAI API 生成项目中文解读，失败时回退到降级模板"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logger.info(f"  [降级] {repo_name} — 未检测到 OPENAI_API_KEY，使用模板生成")
        return generate_fallback_interpretation(repo_name, language, description)

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "你是GitHub开源项目分析师。为给定项目生成中文解读。"
                        "严格输出JSON格式："
                        '{"summary":"一句话概述","features":["功能1","功能2","功能3"],'
                        '"scenarios":["场景1","场景2","场景3","场景4"]}'
                    ),
                },
                {
                    "role": "user",
                    "content": f"项目：{repo_name}\n语言：{language}\nStar数：{stars}\n描述：{description}",
                },
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
        result = json.loads(response.choices[0].message.content)
        logger.info(f"  [AI] {repo_name} — 解读生成成功")
        return result
    except Exception as e:
        logger.warning(f"  [AI失败] {repo_name} — {e}，回退到模板生成")
        return generate_fallback_interpretation(repo_name, language, description)


async def fetch_trending() -> list:
    """
    使用 playwright 抓取 GitHub Trending Weekly 页面
    返回项目列表
    """
    logger.info("正在启动浏览器...")
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        logger.error("未安装 playwright，请运行: pip install playwright && playwright install chromium")
        sys.exit(1)

    projects = []

    async with async_playwright() as p:
        logger.info("启动 Chromium...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        try:
            url = "https://github.com/trending?since=weekly"
            logger.info(f"正在请求 {url} ...")
            await page.goto(url, wait_until="networkidle", timeout=30000)
            logger.info("页面加载完成，开始解析...")

            # 等待仓库列表渲染
            await page.wait_for_selector("article.Box-row", timeout=15000)

            # 提取所有仓库行
            repos = await page.query_selector_all("article.Box-row")
            logger.info(f"找到 {len(repos)} 个 trending 项目")

            for repo in repos:
                try:
                    # 提取项目名和作者
                    h2 = await repo.query_selector("h2")
                    if not h2:
                        continue
                    name_text = await h2.inner_text()
                    name_text = name_text.strip().replace("\n", " ").replace("  ", " ")
                    # 格式: "author / name" 或 "author/name"
                    parts = [p.strip() for p in re.split(r"\s*/\s*", name_text) if p.strip()]
                    if len(parts) < 2:
                        parts = name_text.split("/")
                    if len(parts) < 2:
                        continue
                    author, name = parts[0], parts[1]

                    # 提取 URL
                    link_el = await h2.query_selector("a")
                    href = ""
                    if link_el:
                        href = await link_el.get_attribute("href") or ""
                    full_url = f"https://github.com{href}" if href else f"https://github.com/{author}/{name}"

                    # 提取语言
                    lang_el = await repo.query_selector("[itemprop='programmingLanguage']")
                    language = await lang_el.inner_text() if lang_el else "Unknown"
                    language = language.strip()

                    # 提取总 Star 数
                    star_els = await repo.query_selector_all("a[href*='/stargazers']")
                    total_stars = 0
                    for se in star_els:
                        text = (await se.inner_text()).strip()
                        num = extract_star_number(text)
                        if num > 0 and num > total_stars:
                            total_stars = num

                    # 提取本周新增 Star
                    forks_els = await repo.query_selector_all("span.d-inline-block.float-sm-right")
                    weekly_stars = 0
                    for fe in forks_els:
                        text = (await fe.inner_text()).strip()
                        if "stars" in text.lower():
                            num_text = (
                                text.lower()
                                .replace("stars", "")
                                .replace("star", "")
                                .replace("this week", "")
                                .replace("today", "")
                                .strip()
                            )
                            weekly_stars = extract_star_number(num_text)
                            break

                    # 提取描述
                    desc_el = await repo.query_selector("p.col-9")
                    summary = ""
                    if desc_el:
                        summary = (await desc_el.inner_text()).strip()

                    # 提取 topics
                    topic_els = await repo.query_selector_all("a.topic-tag")
                    topics = []
                    for te in topic_els:
                        t = (await te.inner_text()).strip()
                        if t:
                            topics.append(t)

                    # 判断是否 AI 相关
                    if not is_ai_project(name, summary, language, topics):
                        continue

                    project = {
                        "name": name,
                        "author": author,
                        "full_name": f"{author}/{name}",
                        "url": full_url,
                        "stars": total_stars,
                        "stars_weekly": weekly_stars,
                        "language": language,
                        "summary": summary,     # 来自页面的原始描述
                        "features": [],
                        "scenarios": [],
                    }
                    projects.append(project)
                    logger.info(f"  ✓ {author}/{name} | ★{total_stars} +{weekly_stars}/周 | {language}")

                except Exception as e:
                    logger.warning(f"解析项目时出错: {e}")
                    continue

        except Exception as e:
            logger.error(f"页面抓取失败: {e}")
        finally:
            await browser.close()

    logger.info(f"筛选出 {len(projects)} 个 AI/ML 项目")
    return projects


async def main():
    logger.info("===== GitHub Trending AI/ML 采集器 =====")

    # 1. 计算当前周期
    period_info = get_current_period()
    logger.info(f"当前周期: {period_info['period']} ({period_info['date_range']})")
    logger.info(f"抓取时间: {period_info['fetch_time']}")

    # 2. 加载已有数据
    data = load_existing_data()

    # 3. 检查当前周期是否已存在
    for week in data["weeks"]:
        if week["period"] == period_info["period"]:
            logger.info(f"周期 {period_info['period']} 已存在数据，跳过采集。")
            return

    # 4. 抓取数据
    try:
        projects = await fetch_trending()
    except Exception as e:
        logger.error(f"抓取失败: {e}")
        sys.exit(1)

    if not projects:
        logger.warning("未抓取到任何 AI/ML 项目。")
        return

    # 5. 为每个项目生成 AI 解读
    logger.info(f"正在为 {len(projects)} 个项目生成解读...")
    for project in projects:
        interpretation = await asyncio.to_thread(
            generate_ai_interpretation,
            repo_name=project["full_name"],
            language=project["language"],
            stars=project["stars"],
            description=project.get("summary", ""),
        )
        # 注意：summary 字段在项目中是原始描述，解读里的 summary 是一句话概述
        # 这里把解读结果存到 interpretation 键下，同时保留原始 summary
        project["interpretation_summary"] = interpretation.get("summary", "")
        project["features"] = interpretation.get("features", [])
        project["scenarios"] = interpretation.get("scenarios", [])

    # 6. 构建新周期数据
    new_week = {
        "period": period_info["period"],
        "date_range": period_info["date_range"],
        "fetch_time": period_info["fetch_time"],
        "projects": projects,
    }

    # 7. 追加并保存
    data["weeks"].append(new_week)
    save_data(data)

    # 8. 输出汇总
    logger.info(f"===== 采集完成 =====")
    logger.info(f"周期: {period_info['period']}")
    logger.info(f"日期范围: {period_info['date_range']}")
    logger.info(f"AI/ML 项目数: {len(projects)}")
    logger.info(f"数据已写入: {DATA_FILE}")
    for i, p in enumerate(projects, 1):
        logger.info(
            f"  {i}. {p['full_name']} | ★{p['stars']} (+{p['stars_weekly']}/周) "
            f"| {p['language']} | {p.get('interpretation_summary', '')[:40]}..."
        )

    # 输出 JSON 汇总到 stdout
    summary_output = {
        "period": period_info["period"],
        "date_range": period_info["date_range"],
        "project_count": len(projects),
        "projects": [
            {
                "full_name": p["full_name"],
                "stars": p["stars"],
                "stars_weekly": p["stars_weekly"],
                "language": p["language"],
                "interpretation_summary": p.get("interpretation_summary", ""),
            }
            for p in projects
        ],
    }
    print(json.dumps(summary_output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
