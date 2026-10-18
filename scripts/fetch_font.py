"""下载标题用的衬线字体子集到 site/assets/fonts/，自托管，避免国内访问 Google Fonts 不稳定。

只取页面标题实际用到的字（render.HEADING_GLYPHS），文件只有几 KB。
标题文字有变动时重跑一次并提交：
    python scripts/fetch_font.py
字体：Noto Serif SC 700，SIL Open Font License 1.1（许可证随字体一起放在同目录）。
"""
import re
import sys
from pathlib import Path

import requests

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import HEADING_GLYPHS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "fonts"
CSS_API = "https://fonts.googleapis.com/css2"
OFL_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/OFL.txt"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    css = requests.get(CSS_API, params={"family": "Noto Serif SC:wght@700", "text": HEADING_GLYPHS,
                                        "display": "swap"}, headers={"User-Agent": UA}, timeout=30)
    css.raise_for_status()
    urls = re.findall(r"url\((https://[^)]+)\) format\('woff2'\)", css.text)
    if len(urls) != 1:
        sys.exit(f"预期 1 个 woff2，实际 {len(urls)} 个：\n{css.text[:500]}")
    font = requests.get(urls[0], timeout=30)
    font.raise_for_status()
    (OUT / "serif-heading.woff2").write_bytes(font.content)
    ofl = requests.get(OFL_URL, timeout=30)
    ofl.raise_for_status()
    (OUT / "OFL.txt").write_text(ofl.text, encoding="utf-8")
    print(f"写入 {OUT}：serif-heading.woff2（{len(font.content) / 1024:.1f} KB，{len(HEADING_GLYPHS)} 个字），OFL.txt")


if __name__ == "__main__":
    main()
