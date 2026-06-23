"""Dependency-free checks for the Cracktrader static site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if element_id := values.get("id"):
            if element_id in self.ids:
                raise ValueError(f"duplicate id: {element_id}")
            self.ids.add(element_id)
        if tag in {"a", "link"} and values.get("href"):
            self.links.append(values["href"])


def local_target(url: str) -> Path | None:
    parsed = urlparse(url)
    if parsed.scheme or url.startswith(("#", "//", "mailto:")):
        return None
    return ROOT / parsed.path.lstrip("/")


def main() -> None:
    errors: list[str] = []
    for page in ROOT.glob("*.html"):
        parser = Parser()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            target = local_target(link)
            if target and not target.exists():
                errors.append(f"{page.name}: missing local target {link}")
    for expected in ("styles.css", "robots.txt", "sitemap.xml", "assets/favicon.svg"):
        if not (ROOT / expected).exists():
            errors.append(f"missing required file: {expected}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Static site checks passed.")


if __name__ == "__main__":
    main()
