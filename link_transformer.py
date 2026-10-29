import re

IG_PATTERN = re.compile(
    r"https?://(?:www\.)?instagram\.com/([a-zA-Z0-9_./-]+)",
    re.IGNORECASE,
)

TIKTOK_STANDARD_PATTERN = re.compile(
    r"https?://(?:www\.)?tiktok\.com/([a-zA-Z0-9_./@-]+)",
    re.IGNORECASE,
)

TIKTOK_SHORT_PATTERN = re.compile(
    r"https?://(?:vm|vt)\.tiktok\.com/([a-zA-Z0-9_./-]+)",
    re.IGNORECASE,
)

PUNCTUATION_TO_STRIP = ".,!?:;)>"


def _clean_path(raw_path: str) -> str:
    path = raw_path.rstrip(PUNCTUATION_TO_STRIP).rstrip("/").lstrip("/")
    return path


def transform_urls(text: str) -> list[str]:
    """Extract Instagram and TikTok URLs from text and convert to kkclip embed domain."""
    results: list[str] = []

    for path in IG_PATTERN.findall(text):
        clean_path = _clean_path(path)
        if clean_path:
            results.append(f"https://www.kkclip.com/{clean_path}")

    for path in TIKTOK_STANDARD_PATTERN.findall(text):
        clean_path = _clean_path(path)
        if clean_path:
            results.append(f"https://www.kkclip.com/{clean_path}")

    for path in TIKTOK_SHORT_PATTERN.findall(text):
        clean_path = _clean_path(path)
        if clean_path:
            results.append(f"https://www.kkclip.com/{clean_path}")

    return list(dict.fromkeys(results))


def format_message(links: list[str]) -> str:
    """Format transformed URLs into Discord masked markdown links."""
    return "\n".join(f"[Fixed Embed]({link})" for link in links)

