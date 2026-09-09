#!/usr/bin/env python3
"""为已完成的 PostCollection 文章生成分类、月份和总索引。"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
INDEX_ROOT = OUTPUT / "indexes"


@dataclass(frozen=True)
class Article:
    path: Path
    title: str
    category: str
    month: str
    published: str
    summary: str
    depth: str


def parse_frontmatter(text: str) -> dict[str, object]:
    """解析本项目使用的简单 YAML frontmatter，不依赖第三方库。"""
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, object] = {}
    current_list: str | None = None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        list_item = re.match(r"^\s*-\s+(.+)$", line)
        if current_list and list_item:
            value = str(list_item.group(1)).strip().strip("'\"")
            cast = result.setdefault(current_list, [])
            if isinstance(cast, list):
                cast.append(value)
            continue
        match = re.match(r"^([\w-]+):\s*(.*)$", line)
        if not match:
            current_list = None
            continue
        key, raw = match.groups()
        raw = raw.strip()
        if not raw:
            result[key] = []
            current_list = key
        elif raw.startswith("[") and raw.endswith("]"):
            result[key] = [part.strip().strip("'\"") for part in raw[1:-1].split(",") if part.strip()]
            current_list = None
        else:
            result[key] = raw.strip("'\"")
            current_list = None
    return result


def first(meta: dict[str, object], *keys: str, default: str = "") -> str:
    """返回首个有值的字段，并把列表压缩为逗号分隔文本。"""
    for key in keys:
        value = meta.get(key)
        if isinstance(value, list) and value:
            return "、".join(str(item) for item in value)
        if value not in (None, ""):
            return str(value)
    return default


def is_complete(path: Path) -> bool:
    """文章仅在存在 `<文章>.md.done` 或 `<文章>.done` 时进入索引。"""
    return Path(f"{path}.done").is_file() or path.with_suffix(".done").is_file()


def load_articles() -> list[Article]:
    """扫描 output/YYYY-MM/*.md 并读取索引所需元数据。"""
    articles: list[Article] = []
    if not OUTPUT.exists():
        return articles
    for path in sorted(OUTPUT.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]/*.md")):
        if path.name.startswith("_") or not is_complete(path):
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        published = first(meta, "date", "published", "published_at", default=path.parent.name)
        month_match = re.search(r"\d{4}-\d{2}", published)
        month = month_match.group(0) if month_match else path.parent.name
        articles.append(Article(
            path=path,
            title=first(meta, "title", default=path.stem),
            category=first(meta, "category", "categories", default="未分类"),
            month=month,
            published=published,
            summary=first(meta, "summary", "description", "abstract", default="暂无摘要"),
            depth=first(meta, "depth", "level", default="未标注"),
        ))
    return articles


def safe_name(value: str) -> str:
    """生成可跨平台使用且仍可辨认的索引文件名。"""
    clean = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", "-", value).strip(" .")
    return clean or "未分类"


def article_link(article: Article, base: Path) -> str:
    relative = Path(os.path.relpath(article.path, base)).as_posix()
    return quote(relative, safe="/()[]-_.~")


def article_lines(articles: Iterable[Article], base: Path) -> list[str]:
    lines: list[str] = []
    for item in sorted(articles, key=lambda article: (article.published, article.title), reverse=True):
        lines.append(f"- [{item.title}]({article_link(item, base)}) · {item.published} · {item.depth}")
        lines.append(f"  - {item.summary}")
    return lines or ["- 暂无文章"]


def write_index(path: Path, title: str, articles: list[Article]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = [f"# {title}", "", f"> 共 {len(articles)} 篇，生成于 {date.today().isoformat()}。", ""]
    content.extend(article_lines(articles, path.parent))
    path.write_text("\n".join(content) + "\n", encoding="utf-8")


def build_indexes(rebuild: bool = False) -> list[Article]:
    """生成全部索引；--rebuild 仅清理由本脚本维护的索引目录。"""
    if rebuild:
        if INDEX_ROOT.exists():
            shutil.rmtree(INDEX_ROOT)
        root_index = OUTPUT / "_index.md"
        if root_index.exists():
            root_index.unlink()

    articles = load_articles()
    categories: dict[str, list[Article]] = defaultdict(list)
    months: dict[str, list[Article]] = defaultdict(list)
    for article in articles:
        categories[article.category].append(article)
        months[article.month].append(article)

    category_dir = INDEX_ROOT / "categories"
    month_dir = INDEX_ROOT / "months"
    for category, items in sorted(categories.items()):
        write_index(category_dir / f"{safe_name(category)}.md", f"分类：{category}", items)
    for month, items in sorted(months.items(), reverse=True):
        write_index(month_dir / f"{safe_name(month)}.md", f"月份：{month}", items)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    root_lines = [
        "# PostCollection 索引", "",
        f"> 共 {len(articles)} 篇，{len(categories)} 个分类，{len(months)} 个月份。", "",
        "## 按分类", "",
    ]
    root_lines.extend(
        f"- [{category}](indexes/categories/{quote(safe_name(category))}.md)（{len(items)}）"
        for category, items in sorted(categories.items())
    )
    if not categories:
        root_lines.append("- 暂无文章")
    root_lines.extend(["", "## 按月份", ""])
    root_lines.extend(
        f"- [{month}](indexes/months/{quote(safe_name(month))}.md)（{len(items)}）"
        for month, items in sorted(months.items(), reverse=True)
    )
    if not months:
        root_lines.append("- 暂无文章")
    (OUTPUT / "_index.md").write_text("\n".join(root_lines) + "\n", encoding="utf-8")
    return articles


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 PostCollection Markdown 索引")
    parser.add_argument("--rebuild", action="store_true", help="重建全部索引")
    args = parser.parse_args()
    articles = build_indexes(args.rebuild)
    print(f"已索引 {len(articles)} 篇文章：{OUTPUT / '_index.md'}")


if __name__ == "__main__":
    main()
