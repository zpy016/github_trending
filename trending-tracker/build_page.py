#!/usr/bin/env python3
"""
GitHub Trending AI/ML 追踪器 - HTML 页面构建脚本
读取 trending_data.json，生成自包含的单文件 HTML 页面。
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / "trending_data.json"
OUTPUT_FILE = SCRIPT_DIR / "github-trending-tracker.html"


def format_star(n: int) -> str:
    """格式化 Star 数字为人类可读格式"""
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def load_data() -> dict:
    """加载数据文件"""
    if not DATA_FILE.exists():
        print(f"错误: 数据文件不存在 {DATA_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_language_color(lang: str) -> str:
    """获取语言对应的颜色"""
    colors = {
        "Python": "#3776AB",
        "Shell": "#4EAA25",
        "Rust": "#DEA584",
        "TypeScript": "#3178C6",
        "JavaScript": "#F7DF1E",
        "Markdown": "#6d6d6d",
    }
    return colors.get(lang, "#8b8b8b")


def extract_all_projects(data: dict) -> list:
    """从所有周期中提取项目，去重保留最新周期数据"""
    all_projects = []
    seen = {}  # full_name -> index in all_projects
    for week in data.get("weeks", []):
        for proj in week.get("projects", []):
            key = proj.get("full_name", proj.get("url", ""))
            if key in seen:
                # 同一项目出现在多个周期，更新数据和周期标签
                idx = seen[key]
                existing = all_projects[idx]
                # 保留最新周期的数据
                existing["periods"].append(week["period"])
            else:
                p = dict(proj)
                p["periods"] = [week["period"]]
                all_projects.append(p)
                seen[key] = len(all_projects) - 1
    return all_projects


def extract_languages(projects: list) -> list:
    """提取所有出现的语言（去重排序）"""
    langs = set()
    for p in projects:
        langs.add(p.get("language", "Unknown"))
    return sorted(langs)


def extract_periods(data: dict) -> list:
    """提取所有周期标签"""
    return [w["period"] for w in data.get("weeks", [])]


def extract_trend_tags(projects: list) -> list:
    """从最近一周项目的场景标签中提取高频词作为趋势热词"""
    word_count = {}
    for p in projects:
        for scenario in p.get("scenarios", []):
            # 简单分词
            for word in scenario.replace("·", " ").replace("、", " ").replace("/", " ").split():
                word = word.strip()
                if len(word) >= 2:
                    word_count[word] = word_count.get(word, 0) + 1
    # 按频率排序取前 6
    sorted_words = sorted(word_count.items(), key=lambda x: -x[1])
    return [w for w, _ in sorted_words[:6]]


def build_html(data: dict) -> str:
    """构建完整 HTML 页面"""
    projects = extract_all_projects(data)
    languages = extract_languages(projects)
    periods = extract_periods(data)
    trend_tags = extract_trend_tags(projects)

    # 按本周新增 Star 降序排列
    projects_sorted = sorted(projects, key=lambda x: -x.get("stars_weekly", 0))

    # 统计
    total_projects = len(projects)
    total_periods = len(periods)

    # 最近一次抓取时间
    latest_fetch = ""
    if data.get("weeks"):
        latest_fetch = data["weeks"][-1].get("fetch_time", "")

    # 将数据转为 JSON 内嵌
    data_json = json.dumps(projects_sorted, ensure_ascii=False)
    languages_json = json.dumps(languages, ensure_ascii=False)
    periods_json = json.dumps(periods, ensure_ascii=False)

    # 趋势热词
    tags_html = " · ".join(trend_tags)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub Trending AI/ML 追踪器</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
  background: linear-gradient(135deg, #0f0d1e 0%, #1e1b4b 30%, #312e81 60%, #4338ca 100%);
  background-attachment: fixed;
  min-height: 100vh;
  color: #e8e6f0;
  line-height: 1.6;
}}

.container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 24px;
}}

/* ---------- Header ---------- */
.header {{
  text-align: center;
  margin-bottom: 40px;
}}

.header h1 {{
  font-size: 2.4rem;
  font-weight: 700;
  background: linear-gradient(135deg, #c7d2fe, #a5b4fc, #818cf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 8px;
}}

.header .subtitle {{
  font-size: 0.95rem;
  color: #a5a0c8;
  margin-bottom: 16px;
}}

.header .stats {{
  font-size: 0.85rem;
  color: #7c78a0;
}}

/* ---------- Trend Tags ---------- */
.trend-bar {{
  background: rgba(99, 102, 241, 0.12);
  border: 1px solid rgba(99, 102, 241, 0.2);
  border-radius: 12px;
  padding: 12px 20px;
  margin-bottom: 24px;
  font-size: 0.9rem;
  color: #a5b4fc;
}}

.trend-bar .label {{
  color: #c7d2fe;
  font-weight: 600;
  margin-right: 8px;
}}

/* ---------- Controls ---------- */
.controls {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 32px;
  align-items: center;
}}

.controls select,
.controls input {{
  background: rgba(30, 27, 75, 0.6);
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 10px;
  color: #e8e6f0;
  padding: 10px 16px;
  font-size: 0.9rem;
  font-family: inherit;
  outline: none;
  transition: border-color 0.2s;
}}

.controls select:focus,
.controls input:focus {{
  border-color: #6366f1;
}}

.controls input {{
  flex: 1;
  min-width: 200px;
}}

.controls input::placeholder {{
  color: #6b6890;
}}

.sort-btns {{
  display: flex;
  gap: 4px;
}}

.sort-btns button {{
  background: rgba(30, 27, 75, 0.6);
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 10px;
  color: #a5a0c8;
  padding: 10px 16px;
  font-size: 0.85rem;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
  white-space: nowrap;
}}

.sort-btns button:hover {{
  background: rgba(99, 102, 241, 0.2);
  border-color: #6366f1;
}}

.sort-btns button.active {{
  background: rgba(99, 102, 241, 0.3);
  border-color: #818cf8;
  color: #c7d2fe;
  font-weight: 600;
}}

/* ---------- Grid ---------- */
.card-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-bottom: 40px;
}}

@media (max-width: 1023px) {{
  .card-grid {{
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }}
}}

@media (max-width: 767px) {{
  .card-grid {{
    grid-template-columns: 1fr;
  }}
  .header h1 {{ font-size: 1.8rem; }}
  .controls {{ flex-direction: column; align-items: stretch; }}
  .sort-btns {{ width: 100%; }}
  .sort-btns button {{ flex: 1; }}
}}

/* ---------- Card ---------- */
.card {{
  background: rgba(30, 27, 75, 0.75);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(99, 102, 241, 0.15);
  border-radius: 16px;
  padding: 24px;
  transition: transform 0.3s ease, box-shadow 0.3s ease, opacity 0.3s ease;
  display: flex;
  flex-direction: column;
}}

.card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(99, 102, 241, 0.25);
}}

.card.hidden {{
  display: none;
}}

/* ---------- Card Top Row ---------- */
.card-top {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}}

.rank-badge {{
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #0f0d1e;
  font-weight: 800;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}

.project-name {{
  font-size: 1.05rem;
  font-weight: 700;
  color: #e8e6f0;
  text-decoration: none;
  transition: color 0.2s;
  word-break: break-all;
}}

.project-name:hover {{
  color: #a5b4fc;
}}

.lang-tag {{
  display: inline-block;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  flex-shrink: 0;
  margin-left: auto;
}}

/* ---------- Period Labels ---------- */
.period-labels {{
  display: flex;
  gap: 6px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}}

.period-label {{
  display: inline-block;
  padding: 2px 10px;
  border-radius: 8px;
  font-size: 0.72rem;
  font-weight: 500;
  background: rgba(99, 102, 241, 0.2);
  color: #a5b4fc;
}}

/* ---------- Star Row ---------- */
.star-row {{
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 14px;
}}

.star-total {{
  font-size: 1.2rem;
  font-weight: 700;
  color: #e8e6f0;
}}

.star-weekly {{
  font-size: 0.95rem;
  font-weight: 600;
  color: #34d399;
}}

/* ---------- Divider ---------- */
.divider {{
  border: none;
  border-top: 1px solid rgba(99, 102, 241, 0.15);
  margin: 0 0 14px 0;
}}

/* ---------- Summary ---------- */
.summary {{
  font-size: 0.9rem;
  color: #c7d2fe;
  font-weight: 600;
  margin-bottom: 12px;
  line-height: 1.5;
}}

/* ---------- Features ---------- */
.features {{
  list-style: none;
  padding: 0;
  margin: 0 0 14px 0;
}}

.features li {{
  position: relative;
  padding-left: 18px;
  font-size: 0.85rem;
  color: #a5a0c8;
  line-height: 1.6;
  margin-bottom: 4px;
}}

.features li::before {{
  content: "·";
  position: absolute;
  left: 4px;
  color: #6366f1;
  font-weight: 700;
}}

/* ---------- Scenarios ---------- */
.scenarios {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: auto;
}}

.scenario-tag {{
  display: inline-block;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.78rem;
  background: rgba(99, 102, 241, 0.18);
  color: #a5b4fc;
  white-space: nowrap;
}}

/* ---------- Empty State ---------- */
.empty-state {{
  grid-column: 1 / -1;
  text-align: center;
  padding: 60px 24px;
  color: #7c78a0;
}}

.empty-state .icon {{
  font-size: 3rem;
  margin-bottom: 16px;
}}

.empty-state p {{
  font-size: 1.1rem;
}}

/* ---------- Footer ---------- */
.footer {{
  text-align: center;
  padding: 32px 0 16px;
  font-size: 0.8rem;
  color: #6b6890;
  border-top: 1px solid rgba(99, 102, 241, 0.1);
  margin-top: 20px;
}}
</style>
</head>
<body>

<div class="container">

  <!-- Header -->
  <div class="header">
    <h1>GitHub Trending AI/ML 追踪器</h1>
    <div class="subtitle">持续追踪 GitHub 上 AI/ML 领域的热门开源项目，按周汇总 · 中文解读</div>
    <div class="stats">累计收录 <strong>{total_projects}</strong> 个项目 · 覆盖 <strong>{total_periods}</strong> 个周期</div>
  </div>

  <!-- Trend Tags -->
  <div class="trend-bar">
    <span class="label">本周热点：</span>{tags_html}
  </div>

  <!-- Controls -->
  <div class="controls">
    <select id="period-filter">
      <option value="all">全部周期</option>
    </select>
    <select id="language-filter">
      <option value="all">全部语言</option>
    </select>
    <input type="text" id="search-input" placeholder="搜索项目名或描述...">
    <div class="sort-btns">
      <button id="sort-weekly" class="active">本周新增 ↑</button>
      <button id="sort-stars">总 Star ↑</button>
    </div>
  </div>

  <!-- Card Grid -->
  <div class="card-grid" id="card-grid">
  </div>

  <!-- Footer -->
  <div class="footer">
    数据来源：GitHub Trending · 最近抓取时间：{latest_fetch}
  </div>

</div>

<script id="trending-data" type="application/json">{data_json}</script>

<script>
(function() {{
  'use strict';

  // 读取数据
  const dataEl = document.getElementById('trending-data');
  const allProjects = JSON.parse(dataEl.textContent);
  const languages = {languages_json};
  const periods = {periods_json};

  // ===== 动态填充下拉框 =====
  const periodFilter = document.getElementById('period-filter');
  periods.forEach(p => {{
    const opt = document.createElement('option');
    opt.value = p;
    opt.textContent = p;
    periodFilter.appendChild(opt);
  }});

  const langFilter = document.getElementById('language-filter');
  languages.forEach(l => {{
    const opt = document.createElement('option');
    opt.value = l;
    opt.textContent = l;
    langFilter.appendChild(opt);
  }});

  // ===== 语言颜色映射 =====
  const langColors = {{
    "Python": "#3776AB",
    "Shell": "#4EAA25",
    "Rust": "#DEA584",
    "TypeScript": "#3178C6",
    "JavaScript": "#F7DF1E",
    "Markdown": "#6d6d6d",
  }};

  function getLangColor(lang) {{
    return langColors[lang] || "#8b8b8b";
  }}

  // ===== 格式化 Star =====
  function formatStar(n) {{
    if (n >= 1000) return (n / 1000).toFixed(1) + 'k';
    return String(n);
  }}

  // ===== 获取语言标签 HTML =====
  function getLangTag(lang) {{
    const c = getLangColor(lang);
    return `<span class="lang-tag" style="background:${{c}}20;color:${{c}};border:1px solid ${{c}}44">${{lang}}</span>`;
  }}

  // ===== 过滤条件 =====
  let currentPeriod = 'all';
  let currentLang = 'all';
  let currentSearch = '';
  let currentSort = 'weekly'; // 'weekly' | 'stars'

  // ===== 渲染卡片 =====
  function render() {{
    const grid = document.getElementById('card-grid');

    // 过滤
    let filtered = allProjects;
    if (currentPeriod !== 'all') {{
      filtered = filtered.filter(p => (p.periods || []).includes(currentPeriod));
    }}
    if (currentLang !== 'all') {{
      filtered = filtered.filter(p => p.language === currentLang);
    }}
    if (currentSearch.trim()) {{
      const q = currentSearch.trim().toLowerCase();
      filtered = filtered.filter(p => {{
        const fields = [
          p.name, p.author, p.summary,
          ...(p.features || []),
          ...(p.scenarios || [])
        ].join(' ').toLowerCase();
        return fields.includes(q);
      }});
    }}

    // 排序
    if (currentSort === 'weekly') {{
      filtered.sort((a, b) => (b.stars_weekly || 0) - (a.stars_weekly || 0));
    }} else {{
      filtered.sort((a, b) => (b.stars || 0) - (a.stars || 0));
    }}

    // 无结果
    if (filtered.length === 0) {{
      grid.innerHTML = `<div class="empty-state"><div class="icon">&#128269;</div><p>没有匹配的项目</p><p style="font-size:0.85rem;margin-top:8px">试试调整筛选条件或搜索关键词</p></div>`;
      return;
    }}

    // 构建卡片
    grid.innerHTML = filtered.map((p, i) => {{
      const rank = i + 1;
      const features = (p.features || []).map(f => `<li>${{f}}</li>`).join('');
      const scenarios = (p.scenarios || []).map(s => `<span class="scenario-tag">${{s}}</span>`).join('');
      const periodsHtml = (p.periods || []).map(pd => `<span class="period-label">${{pd}}</span>`).join('');

      return `
      <div class="card">
        <div class="card-top">
          <span class="rank-badge">${{rank}}</span>
          <a class="project-name" href="${{p.url}}" target="_blank" rel="noopener">${{p.full_name}}</a>
          ${{getLangTag(p.language)}}
        </div>
        <div class="period-labels">${{periodsHtml}}</div>
        <div class="star-row">
          <span class="star-total">★ ${{formatStar(p.stars)}}</span>
          <span class="star-weekly">↑ ${{formatStar(p.stars_weekly)}} 本周</span>
        </div>
        <hr class="divider">
        <div class="summary">${{p.summary || '暂无描述'}}</div>
        <ul class="features">${{features}}</ul>
        <div class="scenarios">${{scenarios}}</div>
      </div>`;
    }}).join('');
  }}

  // ===== 事件绑定 =====
  periodFilter.addEventListener('change', function() {{
    currentPeriod = this.value;
    render();
  }});

  langFilter.addEventListener('change', function() {{
    currentLang = this.value;
    render();
  }});

  let searchTimer;
  document.getElementById('search-input').addEventListener('input', function() {{
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {{
      currentSearch = this.value;
      render();
    }}, 200);
  }});

  document.getElementById('sort-weekly').addEventListener('click', function() {{
    currentSort = 'weekly';
    this.classList.add('active');
    document.getElementById('sort-stars').classList.remove('active');
    render();
  }});

  document.getElementById('sort-stars').addEventListener('click', function() {{
    currentSort = 'stars';
    this.classList.add('active');
    document.getElementById('sort-weekly').classList.remove('active');
    render();
  }});

  // ===== 初始渲染 =====
  render();

}})();
</script>

</body>
</html>"""

    return html


def main():
    print("===== GitHub Trending AI/ML 页面构建器 =====")
    data = load_data()
    print(f"已加载 {len(data.get('weeks', []))} 个周期")

    html = build_html(data)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"HTML 页面已生成: {OUTPUT_FILE} ({size_kb:.1f} KB)")
    print("可直接在浏览器中打开。")


if __name__ == "__main__":
    main()
