"""下载页面用的两款字体子集到 site/assets/fonts/，自托管，避免国内访问 Google Fonts 不稳定。

- heading.woff2：ZCOOL XiaoWei（站酷小薇），标题用。只取 render.HEADING_GLYPHS 里的字，外加全部 ASCII（分析页标题里有项目名）
- mono.woff2：Geist Mono，数字、日期和读数用。只取 ASCII 和几个常用符号
两款都是 SIL Open Font License 1.1，许可证随字体放在同目录。
标题文字有变动时重跑一次并提交（render 发现标题用到子集外的字会提示）：
    python scripts/fetch_font.py
"""
import re
import sys
from pathlib import Path

import requests

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import HEADING_GLYPHS, MONO_GLYPHS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "fonts"
CSS_API = "https://fonts.googleapis.com/css2"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
FONTS = [  # (输出文件, Google Fonts 家族参数, 子集文字, OFL 原文)
    ("heading.woff2", "ZCOOL XiaoWei", HEADING_GLYPHS, "https://raw.githubusercontent.com/google/fonts/main/ofl/zcoolxiaowei/OFL.txt"),
    ("mono.woff2", "Geist Mono:wght@400;500", MONO_GLYPHS, "https://raw.githubusercontent.com/google/fonts/main/ofl/geistmono/OFL.txt"),
]


def fetch(name, family, text, ofl_url):
    css = requests.get(CSS_API, params={"family": family, "text": text, "display": "swap"},
                       headers={"User-Agent": UA}, timeout=30)
    css.raise_for_status()
    urls = re.findall(r"url\((https://[^)]+)\) format\('woff2'\)", css.text)
    if not urls:
        sys.exit(f"{family}：没取到 woff2：\n{css.text[:500]}")
    # 可变字体按字重会返回同一个文件；取第一个即可
    font = requests.get(urls[0], timeout=30)
    font.raise_for_status()
    (OUT / name).write_bytes(font.content)
    ofl = requests.get(ofl_url, timeout=30)
    ofl.raise_for_status()
    (OUT / f"OFL-{name.split('.')[0]}.txt").write_text(ofl.text, encoding="utf-8")
    print(f"  {name}：{family}，{len(font.content) / 1024:.1f} KB，{len(text)} 个字")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for args in FONTS:
        fetch(*args)
    for old in ("serif-heading.woff2", "OFL.txt"):  # 旧版 Noto Serif SC 子集
        (OUT / old).unlink(missing_ok=True)
    print(f"写入 {OUT}")


if __name__ == "__main__":
    main()
