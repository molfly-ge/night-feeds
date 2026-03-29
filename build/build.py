#!/usr/bin/env python3
"""
build.py — генератор статического сайта night-feeds
Исходники: posts/, tools/, digests/, index.md
Выход: site/
"""

import re
import shutil
from pathlib import Path
import markdown

ROOT = Path(__file__).parent.parent
SITE = ROOT / "site"

md = markdown.Markdown(extensions=["tables"])


# ── Helpers ──────────────────────────────────────────────────────────────────

def strip_frontmatter(text: str) -> str:
    """Убирает YAML frontmatter (--- ... ---) из начала файла."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[end + 4:].lstrip("\n")


def strip_meta_line(text: str) -> str:
    """Убирает строку *Обработано: X твитов...*"""
    return re.sub(r'\n---\n\*Обработано:.*?\*\s*$', '', text, flags=re.DOTALL).rstrip()


def linkify_urls(html: str) -> str:
    """Превращает голые URL в <a href>. Не трогает уже существующие href/src."""
    # Защищаем уже существующие атрибуты href="..." и src="..."
    protected = {}
    def protect(m):
        key = f"\x00ATTR{len(protected)}\x00"
        protected[key] = m.group(0)
        return key
    html = re.sub(r'(?:href|src)="[^"]*"', protect, html)

    # Linkify голые https?://... не внутри тегов
    html = re.sub(
        r'(?<!["\'=>])(https?://[^\s<>"\']+)',
        lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>',
        html
    )

    for key, val in protected.items():
        html = html.replace(key, val)
    return html


def linkify_mentions(text: str) -> str:
    """@username → ссылка на X, не трогая уже существующие markdown-ссылки."""
    # Защищаем уже существующие ссылки: [text](url) и [@name](url)
    placeholders = {}
    def protect(m):
        key = f"\x00LINK{len(placeholders)}\x00"
        placeholders[key] = m.group(0)
        return key
    text = re.sub(r'\[([^\]]*)\]\([^)]+\)', protect, text)

    # Заменяем свободные @mentions
    text = re.sub(
        r'(?<![/\w])@([A-Za-z0-9_]+)',
        lambda m: f'[@{m.group(1)}](https://x.com/{m.group(1)}?s=11)',
        text
    )

    # Восстанавливаем защищённые ссылки
    for key, val in placeholders.items():
        text = text.replace(key, val)
    return text


def fix_links(html: str) -> str:
    """Перепиши .md-ссылки в чистые URL сайта."""
    # ../posts/post-{account}-{date}.md → /posts/{account}-{date}
    html = re.sub(
        r'href="\.\./posts/post-([^"]+)-(\d{2}-\d{2}-\d{4})\.md"',
        r'href="/posts/\1-\2"',
        html
    )
    # ../tools/{slug}.md → /tools/{slug}
    html = re.sub(
        r'href="\.\./tools/([^"]+)\.md"',
        r'href="/tools/\1"',
        html
    )
    # digests/digest-{date}.md → /digests/{date}  (из index.md)
    html = re.sub(
        r'href="digests/digest-([^"]+)\.md"',
        r'href="/digests/\1"',
        html
    )
    return html


def render_md(text: str) -> str:
    md.reset()
    text = strip_frontmatter(text)
    text = linkify_mentions(text)
    html = md.convert(text)
    html = fix_links(html)
    html = linkify_urls(html)
    return html


def write_page(path: Path, html: str):
    path.mkdir(parents=True, exist_ok=True)
    (path / "index.html").write_text(html, encoding="utf-8")


def page(title: str, body: str, back: str = None) -> str:
    back_link = f'<p class="back"><a href="{back}">← назад</a></p>' if back else ""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 17px;
      line-height: 1.6;
      color: #2D2D2D;
      background: #ffffff;
      padding: 48px 20px 80px;
      display: flex;
      justify-content: center;
    }}
    .container {{ width: 100%; max-width: 640px; }}
    h1 {{ font-size: 22px; font-weight: 600; margin-bottom: 24px; line-height: 1.3; }}
    h2 {{ font-size: 18px; font-weight: 600; margin: 32px 0 12px; }}
    h3 {{ font-size: 17px; font-weight: 600; margin: 24px 0 8px; }}
    p  {{ margin-bottom: 16px; }}
    ul, ol {{ margin: 0 0 16px 20px; }}
    li {{ margin-bottom: 4px; }}
    a  {{ color: #000; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    code {{ font-family: "Menlo", "SF Mono", monospace; font-size: 14px;
            background: #f5f5f5; padding: 1px 5px; border-radius: 3px; }}
    pre {{ background: #f5f5f5; padding: 16px; border-radius: 4px;
           overflow-x: auto; margin-bottom: 16px; }}
    pre code {{ background: none; padding: 0; }}
    hr {{ border: none; border-top: 1px solid #e5e5e5; margin: 32px 0; }}
    em {{ color: #666; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 16px; font-size: 15px; }}
    th, td {{ text-align: left; padding: 6px 12px 6px 0; border-bottom: 1px solid #e5e5e5; }}
    th {{ font-weight: 600; }}
    .back {{ margin-bottom: 32px; }}
    .back a {{ color: #666; font-size: 15px; }}
    .posts {{ display: flex; flex-direction: column; gap: 10px; }}
    .post {{ display: flex; justify-content: space-between; align-items: baseline; gap: 16px; }}
    .post a {{ color: #000; }}
    .post .date {{ color: #666; white-space: nowrap; font-size: 15px; }}
    .tool-cards {{ margin-top: 32px; display: flex; flex-direction: column; gap: 24px; }}
    .tool-cards img {{ width: 100%; height: auto; display: block; }}
  </style>
</head>
<body>
  <div class="container">
    {back_link}
    {body}
  </div>
</body>
</html>"""


def fmt_date(date_str: str) -> str:
    """29-03-2026 → Mar 29, 2026"""
    months = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]
    d, m, y = date_str.split("-")
    return f"{months[int(m)-1]} {int(d)}, {y}"


# ── Tool index: {slug} → {source_account, source_date, has_png, names} ───────

def build_tool_index() -> dict:
    index = {}
    for f in (ROOT / "tools").glob("*.md"):
        slug = f.stem
        text = f.read_text(encoding="utf-8")
        account, date = None, None
        m = re.search(r'\*\*Источник:\*\*.*?@(\w+).*?,\s*(\d{2}-\d{2}-\d{4})', text)
        if m:
            account, date = m.group(1), m.group(2)
        has_png = (ROOT / "tools" / f"{slug}.png").exists()

        # Собираем варианты имён для авто-линковки
        names = set()
        # из frontmatter: name: ...
        fm = re.search(r'^name:\s*(.+)$', text, re.MULTILINE)
        if fm:
            names.add(fm.group(1).strip())
        # из заголовка: # Title
        h1 = re.search(r'^# (.+)$', strip_frontmatter(text), re.MULTILINE)
        if h1:
            names.add(h1.group(1).strip())
        # slug как fallback (дефисы → пробелы)
        names.add(slug)
        names.add(slug.replace("-", " "))

        index[slug] = {"account": account, "date": date, "has_png": has_png, "names": names}
    return index


def autolink_github(html: str) -> str:
    """**repo** (github-user) → ссылка на github.com/user/repo.
    Не трогает уже залинкованные <strong><a ...>.
    """
    def replace(m):
        name = m.group(1)
        user = m.group(2)
        # slug для GitHub: lowercase, пробелы → дефисы
        repo = name.lower().replace(" ", "-")
        return (
            f'<strong><a href="https://github.com/{user}/{repo}">{name}</a></strong>'
            f' (<a href="https://github.com/{user}">{user}</a>)'
        )

    # Матчим только незалинкованный <strong>text</strong> (без <a> внутри)
    return re.sub(
        r'<strong>([^<]+)</strong>\s*\(([A-Za-z0-9_-]+)\)',
        replace,
        html
    )


def autolink_tools(html: str, tool_index: dict) -> str:
    """Оборачивает жирные названия инструментов в ссылки на их страницы."""
    # Строим обратный словарь: lowercase_name → slug
    name_to_slug = {}
    for slug, info in tool_index.items():
        for name in info["names"]:
            name_to_slug[name.lower()] = slug

    def replace(m):
        name = m.group(1)
        slug = name_to_slug.get(name.lower())
        if slug:
            return f'<strong><a href="/tools/{slug}">{name}</a></strong>'
        return m.group(0)

    return re.sub(r'<strong>([^<]+)</strong>', replace, html)


# ── Build index (/) ───────────────────────────────────────────────────────────

def build_index(tool_index: dict):
    index_md = (ROOT / "index.md").read_text(encoding="utf-8")
    rows = []
    for line in index_md.splitlines():
        m = re.match(r'-\s+\[([^\]]+)\]\(digests/digest-([^)]+)\.md\)\s*[—–-]\s*(.*)', line)
        if not m:
            continue
        label, date, desc = m.group(1), m.group(2), m.group(3)
        rows.append(f'''<div class="post">
          <a href="/digests/{date}">{desc}</a>
          <span class="date">{fmt_date(date)}</span>
        </div>''')

    body = f"""<section>
      <h2>дайджест</h2>
      <div class="posts">
        {''.join(rows)}
      </div>
    </section>"""

    write_page(SITE, page("Дайджест", body))


# ── Build digest pages ────────────────────────────────────────────────────────

def build_digests():
    for f in (ROOT / "digests").glob("*.md"):
        m = re.match(r'digest-(\d{2}-\d{2}-\d{4})', f.stem)
        if not m:
            continue
        date = m.group(1)
        text = f.read_text(encoding="utf-8")
        body = f"<article>{render_md(text)}</article>"
        write_page(SITE / "digests" / date, page(f"Дайджест {date}", body, back="/"))


# ── Build post pages ──────────────────────────────────────────────────────────

def build_posts(tool_index: dict):
    for f in (ROOT / "posts").glob("*.md"):
        m = re.match(r'post-(.+)-(\d{2}-\d{2}-\d{4})', f.stem)
        if not m:
            continue
        account, date = m.group(1), m.group(2)
        text = f.read_text(encoding="utf-8")
        text = strip_meta_line(text)
        content_html = autolink_github(autolink_tools(render_md(text), tool_index))
        body = f"<article>{content_html}</article>"

        # PNG карточки инструментов из этого поста
        cards = [
            slug for slug, info in tool_index.items()
            if info["account"] == account and info["date"] == date and info["has_png"]
        ]
        if cards:
            imgs = "\n".join(
                f'<img src="/tools/{slug}/{slug}.png" alt="{slug}">'
                for slug in cards
            )
            body += f'<div class="tool-cards">{imgs}</div>'

        slug_path = f"{account}-{date}"
        write_page(SITE / "posts" / slug_path, page(f"{account} — {date}", body, back="/"))


# ── Build tool pages ──────────────────────────────────────────────────────────

def build_tools(tool_index: dict):
    for f in (ROOT / "tools").glob("*.md"):
        slug = f.stem
        text = f.read_text(encoding="utf-8")
        info = tool_index.get(slug, {})

        img_html = ""
        if info.get("has_png"):
            img_html = f'<p><img src="{slug}.png" alt="{slug}" style="width:100%;height:auto;display:block;margin-bottom:24px;"></p>'

        body = f"<article>{img_html}{render_md(text)}</article>"
        dest = SITE / "tools" / slug
        write_page(dest, page(slug, body, back="/"))

        # Копируем PNG рядом с index.html
        src_png = ROOT / "tools" / f"{slug}.png"
        if src_png.exists():
            shutil.copy2(src_png, dest / f"{slug}.png")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    tool_index = build_tool_index()

    build_index(tool_index)
    build_digests()
    build_posts(tool_index)
    build_tools(tool_index)

    pages = list(SITE.rglob("index.html"))
    print(f"Собрано: {len(pages)} страниц → {SITE}")


if __name__ == "__main__":
    main()
