"""把公有领域的二战雷达屏幕照片转成 96×96 的亮度网格，存到 design/assets/radar-scope.json。

页面用它在 canvas 上以字符点阵画出刊头和分析页的雷达底纹（颜色跟随主题，体积约 9 KB）。
只在换底图时运行一次，结果随仓库提交；需要 Pillow（不在 requirements.txt 里，出刊不需要）：
    pip install pillow && python scripts/make_scope.py

底图：Night radar scope image of Potomac approach to Washington, WWII
National Museum of the U.S. Navy，Public Domain Mark 1.0
https://commons.wikimedia.org/wiki/File:Night_radar_scope_image_of_Potomac_approach_to_Washington,_WWII_(39543289985).jpg
"""
import io
import json
from pathlib import Path

import requests
from PIL import Image, ImageOps

URL = ("https://upload.wikimedia.org/wikipedia/commons/7/78/"
       "Night_radar_scope_image_of_Potomac_approach_to_Washington%2C_WWII_%2839543289985%29.jpg")
OUT = Path(__file__).resolve().parent.parent / "design" / "assets" / "radar-scope.json"
N = 96


def main():
    raw = requests.get(URL, headers={"User-Agent": "ai-trending-radar (make_scope.py)"}, timeout=60)
    raw.raise_for_status()
    src = Image.open(io.BytesIO(raw.content)).convert("L")
    k = src.size[0] / 900  # 裁切框按 900 宽的预览图量出：圆形屏幕略扁，拉成正圆
    sq = ImageOps.autocontrast(src.crop((int(70 * k), int(8 * k), int(800 * k), int(668 * k))), cutoff=2)
    px = sq.resize((N, N), Image.LANCZOS).load()
    rows = []
    for y in range(N):
        row = ""
        for x in range(N):
            dx, dy = (x + .5 - N / 2) / (N / 2), (y + .5 - N / 2) / (N / 2)
            row += str(min(9, px[x, y] * 10 // 256)) if dx * dx + dy * dy < .93 else "0"
        rows.append(row)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"source": URL, "license": "Public Domain Mark 1.0", "credit": "National Museum of the U.S. Navy",
                               "rows": rows}, ensure_ascii=False), encoding="utf-8")
    print(f"写入 {OUT}（{N}×{N}）")


if __name__ == "__main__":
    main()
