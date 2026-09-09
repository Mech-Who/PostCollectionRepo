#!/usr/bin/env python3
"""把已完成的 Markdown 文章渲染为可离线浏览的静态站点。"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
SITE = ROOT / "site"


@dataclass(frozen=True)
class Article:
    source: Path
    key: str
    page: Path
    title: str
    date: str
    category: str
    depth: str
    summary: str
    source_url: str
    body: str


def parse_document(text: str) -> tuple[dict[str, object], str]:
    """解析简单 YAML frontmatter，并保留正文。"""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    meta: dict[str, object] = {}
    current_list: str | None = None
    end = 0
    for index, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end = index + 1
            break
        item = re.match(r"^\s*-\s+(.+)$", line)
        if current_list and item:
            value = item.group(1).strip().strip("'\"")
            cast = meta.setdefault(current_list, [])
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
            meta[key] = []
            current_list = key
        elif raw.startswith("[") and raw.endswith("]"):
            meta[key] = [part.strip().strip("'\"") for part in raw[1:-1].split(",") if part.strip()]
            current_list = None
        else:
            meta[key] = raw.strip("'\"")
            current_list = None
    return meta, "\n".join(lines[end:])


def field(meta: dict[str, object], *keys: str, default: str = "") -> str:
    for key in keys:
        value = meta.get(key)
        if isinstance(value, list) and value:
            return "、".join(str(item) for item in value)
        if value not in (None, ""):
            return str(value)
    return default


def complete(path: Path) -> bool:
    return Path(f"{path}.done").is_file() or path.with_suffix(".done").is_file()


def inline(text: str) -> str:
    """转义文本后渲染常见行内 Markdown。"""
    escaped = html.escape(text, quote=False)
    placeholders: list[str] = []

    def hold(markup: str) -> str:
        placeholders.append(markup)
        return f"\x00{len(placeholders) - 1}\x00"

    escaped = re.sub(r"`([^`]+)`", lambda match: hold(f"<code>{match.group(1)}</code>"), escaped)
    escaped = re.sub(
        r"!\[([^]]*)\]\((https?://[^ )]+)(?:\s+&quot;.*?&quot;)?\)",
        lambda match: hold(f'<img src="{html.escape(match.group(2), quote=True)}" alt="{html.escape(match.group(1), quote=True)}" loading="lazy">'),
        escaped,
    )
    escaped = re.sub(
        r"\[([^]]+)\]\((https?://[^ )]+)\)",
        lambda match: hold(f'<a href="{html.escape(match.group(2), quote=True)}" target="_blank" rel="noreferrer">{match.group(1)}</a>'),
        escaped,
    )
    escaped = re.sub(r"(?<![\"'=])(https?://[^\s<]+)", lambda match: hold(f'<a href="{html.escape(match.group(1), quote=True)}" target="_blank" rel="noreferrer">{match.group(1)}</a>'), escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    for index, markup in enumerate(placeholders):
        escaped = escaped.replace(f"\x00{index}\x00", markup)
    return escaped


def markdown(text: str) -> str:
    """渲染阅读站点所需的 Markdown 子集。"""
    output: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{'<br>'.join(inline(line) for line in paragraph)}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            output.append(f"</{list_type}>")
            list_type = None

    for line in text.splitlines():
        if line.strip().startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines.clear()
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(line)
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        unordered = re.match(r"^\s*[-*+]\s+(.+)$", line)
        ordered = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        quote_line = re.match(r"^>\s?(.*)$", line)
        if heading:
            flush_paragraph(); close_list()
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif unordered or ordered:
            flush_paragraph()
            wanted = "ul" if unordered else "ol"
            if list_type != wanted:
                close_list(); output.append(f"<{wanted}>"); list_type = wanted
            match = unordered or ordered
            output.append(f"<li>{inline(match.group(1))}</li>")
        elif quote_line:
            flush_paragraph(); close_list()
            output.append(f"<blockquote>{inline(quote_line.group(1))}</blockquote>")
        elif line.strip() in {"---", "***", "___"}:
            flush_paragraph(); close_list(); output.append("<hr>")
        elif not line.strip():
            flush_paragraph(); close_list()
        else:
            close_list(); paragraph.append(line)
    if in_code:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    flush_paragraph(); close_list()
    return "\n".join(output)


def load_articles() -> list[Article]:
    articles: list[Article] = []
    if not OUTPUT.exists():
        return articles
    for source in sorted(OUTPUT.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]/*.md")):
        if source.name.startswith("_") or not complete(source):
            continue
        meta, body = parse_document(source.read_text(encoding="utf-8-sig"))
        relative = source.relative_to(OUTPUT)
        page = Path("articles") / relative.with_suffix(".html")
        key = relative.as_posix()
        articles.append(Article(
            source=source, key=key, page=page,
            title=field(meta, "title", default=source.stem),
            date=field(meta, "date", "published", "published_at", default=source.parent.name),
            category=field(meta, "category", "categories", default="未分类"),
            depth=field(meta, "depth", "level", default="未标注"),
            summary=field(meta, "summary", "description", "abstract", default="暂无摘要"),
            source_url=field(meta, "source_url", "url", "original_url"),
            body=body,
        ))
    return sorted(articles, key=lambda item: (item.date, item.title), reverse=True)


STYLE = """
:root{color-scheme:light;--ink:#18211d;--muted:#63706a;--paper:#f7f6f2;--panel:#fff;--line:#d9dedb;--accent:#176b52;--warm:#b7552a}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.75 system-ui,-apple-system,"Segoe UI","Microsoft YaHei",sans-serif}a{color:var(--accent);text-underline-offset:3px}.wrap{width:min(1120px,calc(100% - 32px));margin:auto}.top{padding:28px 0 22px;border-bottom:1px solid var(--line);background:var(--panel)}.top h1{margin:0;font-size:clamp(25px,4vw,38px);letter-spacing:0}.top p{margin:6px 0 0;color:var(--muted)}.progress{height:8px;margin-top:18px;background:#e5e8e5;overflow:hidden}.progress span{display:block;width:0;height:100%;background:var(--accent);transition:width .25s}.toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;padding:18px 0}.toolbar input,.toolbar select{min-height:42px;border:1px solid var(--line);background:#fff;padding:0 12px;font:inherit}.toolbar input{flex:1;min-width:220px}.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr));gap:14px;padding-bottom:48px}.card{display:flex;flex-direction:column;border:1px solid var(--line);border-left:4px solid var(--accent);background:var(--panel);padding:18px}.card.read{opacity:.63;border-left-color:#a3aaa6}.meta{display:flex;gap:7px;flex-wrap:wrap;color:var(--muted);font-size:13px}.tag{border:1px solid var(--line);padding:1px 7px}.card h2{margin:10px 0 6px;font-size:20px;line-height:1.4}.card p{margin:0 0 16px;color:#46504b}.actions{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:auto}.read-toggle{border:1px solid var(--line);background:#fff;color:var(--ink);min-height:36px;padding:0 10px;cursor:pointer}.empty{display:none;padding:40px 0;color:var(--muted)}article{width:min(780px,calc(100% - 32px));margin:36px auto 72px;background:var(--panel);border:1px solid var(--line);padding:clamp(22px,5vw,54px)}article h1{font-size:clamp(28px,5vw,42px);line-height:1.25;letter-spacing:0;margin:.35em 0}article h2{margin-top:1.8em;font-size:25px;letter-spacing:0}article h3{margin-top:1.5em;font-size:20px;letter-spacing:0}article img{display:block;max-width:100%;height:auto;margin:22px auto}article pre{overflow:auto;background:#17201c;color:#ecf3ef;padding:16px}article code{font-family:ui-monospace,Consolas,monospace}article :not(pre)>code{background:#edf0ed;padding:2px 5px}blockquote{margin:20px 0;padding:8px 16px;border-left:4px solid var(--warm);background:#faf4ef;color:#4e4a47}.article-nav{width:min(780px,calc(100% - 32px));margin:24px auto 0;display:flex;justify-content:space-between;gap:12px}.button{display:inline-flex;align-items:center;min-height:40px;padding:0 13px;border:1px solid var(--line);background:#fff;color:var(--ink);text-decoration:none;cursor:pointer}.article-summary{font-size:18px;color:#46504b;border-bottom:1px solid var(--line);padding-bottom:20px}@media(max-width:560px){.wrap{width:min(100% - 20px,1120px)}.top{padding-top:20px}.toolbar>*{width:100%}article{width:100%;margin:0;border-width:1px 0;padding:22px 18px}.article-nav{width:calc(100% - 24px)}}
"""


SCRIPT = """
const STORE='postcollection-read-v1';
const readSet=()=>new Set(JSON.parse(localStorage.getItem(STORE)||'[]'));
const save=s=>localStorage.setItem(STORE,JSON.stringify([...s]));
function updateProgress(){const cards=[...document.querySelectorAll('[data-key]')],read=readSet();cards.forEach(c=>{const yes=read.has(c.dataset.key);c.classList.toggle('read',yes);const b=c.querySelector('.read-toggle');if(b)b.textContent=yes?'标为未读':'标为已读'});const done=cards.filter(c=>read.has(c.dataset.key)).length,total=cards.length,pct=total?Math.round(done/total*100):0;const label=document.querySelector('#progress-label');const bar=document.querySelector('#progress-bar');if(label)label.textContent=`已读 ${done}/${total}（${pct}%）`;if(bar)bar.style.width=pct+'%'}
function toggle(key){const s=readSet();s.has(key)?s.delete(key):s.add(key);save(s);updateProgress()}
function filterCards(){const q=(document.querySelector('#search')?.value||'').toLowerCase(),cat=document.querySelector('#category')?.value||'';let shown=0;document.querySelectorAll('.card').forEach(c=>{const yes=(!q||c.textContent.toLowerCase().includes(q))&&(!cat||c.dataset.category===cat);c.hidden=!yes;if(yes)shown++});const empty=document.querySelector('#empty');if(empty)empty.style.display=shown?'none':'block'}
document.addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('.read-toggle').forEach(b=>b.addEventListener('click',()=>toggle(b.dataset.key)));document.querySelector('#search')?.addEventListener('input',filterCards);document.querySelector('#category')?.addEventListener('change',filterCards);updateProgress()});
"""


def layout(title: str, content: str, *, script: str = "") -> str:
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{STYLE}</style></head><body>{content}<script>{SCRIPT}{script}</script></body></html>"""


def render_index(articles: list[Article]) -> None:
    categories = sorted({item.category for item in articles})
    options = "".join(f'<option value="{html.escape(value, quote=True)}">{html.escape(value)}</option>' for value in categories)
    cards = []
    for item in articles:
        href = quote(item.page.as_posix(), safe="/()[]-_.~")
        cards.append(f'''<section class="card" data-key="{html.escape(item.key, quote=True)}" data-category="{html.escape(item.category, quote=True)}"><div class="meta"><span>{html.escape(item.date)}</span><span class="tag">{html.escape(item.category)}</span><span class="tag">{html.escape(item.depth)}</span></div><h2><a href="{href}">{html.escape(item.title)}</a></h2><p>{html.escape(item.summary)}</p><div class="actions"><a href="{href}">阅读文章</a><button class="read-toggle" data-key="{html.escape(item.key, quote=True)}" type="button">标为已读</button></div></section>''')
    body = f'''<header class="top"><div class="wrap"><h1>PostCollection</h1><p id="progress-label">已读 0/{len(articles)}（0%）</p><div class="progress" aria-hidden="true"><span id="progress-bar"></span></div></div></header><main class="wrap"><div class="toolbar"><input id="search" type="search" placeholder="搜索标题、摘要或标签" aria-label="搜索文章"><select id="category" aria-label="筛选分类"><option value="">全部分类</option>{options}</select></div><div class="cards">{''.join(cards)}</div><p id="empty" class="empty">没有匹配的文章。</p></main>'''
    (SITE / "index.html").write_text(layout("PostCollection", body), encoding="utf-8")


def render_article(item: Article) -> None:
    destination = SITE / item.page
    destination.parent.mkdir(parents=True, exist_ok=True)
    index_href = "../" * len(item.page.parent.parts) + "index.html"
    original = ""
    if item.source_url:
        original = f'<a class="button" href="{html.escape(item.source_url, quote=True)}" target="_blank" rel="noreferrer">阅读原文（weixin）</a>'
    body = f'''<nav class="article-nav"><a class="button" href="{index_href}">返回目录</a><button class="read-toggle button" data-key="{html.escape(item.key, quote=True)}" type="button">标为已读</button></nav><article data-key="{html.escape(item.key, quote=True)}"><div class="meta"><span>{html.escape(item.date)}</span><span class="tag">{html.escape(item.category)}</span><span class="tag">{html.escape(item.depth)}</span></div><h1>{html.escape(item.title)}</h1><p class="article-summary">{html.escape(item.summary)}</p>{markdown(item.body)}<hr>{original}</article>'''
    destination.write_text(layout(item.title, body), encoding="utf-8")


def main() -> None:
    articles = load_articles()
    SITE.mkdir(parents=True, exist_ok=True)
    render_index(articles)
    for article in articles:
        render_article(article)
    manifest = {"count": len(articles), "articles": [item.key for item in articles]}
    (SITE / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已渲染 {len(articles)} 篇文章：{SITE / 'index.html'}")


if __name__ == "__main__":
    main()
