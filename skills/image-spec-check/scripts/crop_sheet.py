"""把一张图上要细看的几块区域按原分辨率裁出来，拼成一张带编号的核对图。

用法：
  python crop_sheet.py 原图 输出图 "A1=x,y,w,h" "A2=x,y,w,h" ... [--max 1500]

每块写成 编号=左上角x,左上角y,宽,高。四个数可以写像素，也可以全部写 0-1 的
比例（0.5 是画面一半）。编号用清单里的条目号，比如 A1、G2、手1。

裁出来的块不缩放，按原尺寸排进核对图；核对图长边不超过 --max（默认 1500，
看图时更大的图会被自动缩小，细节就丢了）。放不下就分成几张，依次存为
输出图_1.png、输出图_2.png……，终端会打印每张里有哪几块。只需要 Pillow。
"""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

GAP = 12
LABEL_H = 30
BG = (40, 40, 44)
FONTS = [
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/arialbd.ttf",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def load_font(size):
    for path in FONTS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def parse_region(text, width, height):
    if "=" not in text:
        sys.exit(f"区域要写成 编号=x,y,w,h：{text}")
    label, box = text.split("=", 1)
    try:
        x, y, w, h = (float(v) for v in box.replace("，", ",").split(","))
    except ValueError:
        sys.exit(f"区域要有四个数 x,y,w,h：{text}")
    if all(0 <= v <= 1 for v in (x, y, w, h)):
        x, y, w, h = x * width, y * height, w * width, h * height
    left, top = max(0, round(x)), max(0, round(y))
    right, bottom = min(width, round(x + w)), min(height, round(y + h))
    if right - left < 2 or bottom - top < 2:
        sys.exit(f"{label} 的区域在画面外或太小：{text}")
    return label.strip(), (left, top, right, bottom)


def pack(tiles, limit):
    """按行排；一行放不下就换行，一张放不下就另起一张。"""
    sheets, rows = [], []
    row, row_w, row_h, used_h = [], GAP, 0, GAP
    for label, img in tiles:
        tw, th = img.width, img.height + LABEL_H
        if tw + 2 * GAP > limit or th + 2 * GAP > limit:
            print(f"注意：{label} 有 {img.width}×{img.height}，超过 {limit}，看图时会被缩小，建议拆成两块",
                  file=sys.stderr)
            sheets.append([[(label, img)]])
            continue
        if row and row_w + tw + GAP > limit:
            rows.append(row)
            used_h += row_h + GAP
            row, row_w, row_h = [], GAP, 0
        if used_h + max(row_h, th) + GAP > limit:
            if row:
                rows.append(row)
            sheets.append(rows)
            rows, row, row_w, row_h, used_h = [], [], GAP, 0, GAP
        row.append((label, img))
        row_w += tw + GAP
        row_h = max(row_h, th)
    if row:
        rows.append(row)
    if rows:
        sheets.append(rows)
    return sheets


def render(rows, font):
    width = max(sum(img.width + GAP for _, img in row) + GAP for row in rows)
    height = sum(max(img.height for _, img in row) + LABEL_H + GAP for row in rows) + GAP
    sheet = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(sheet)
    y = GAP
    for row in rows:
        x = GAP
        for label, img in row:
            draw.rectangle([x, y, x + img.width - 1, y + LABEL_H - 1], fill=(20, 20, 22))
            draw.text((x + 6, y + 3), f"{label}  {img.width}×{img.height}", fill=(255, 220, 80), font=font)
            sheet.paste(img, (x, y + LABEL_H))
            x += img.width + GAP
        y += max(img.height for _, img in row) + LABEL_H + GAP
    return sheet


def main():
    ap = argparse.ArgumentParser(description="按原分辨率裁出几块区域，拼成一张核对图")
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("regions", nargs="+", help='编号=x,y,w,h，像素或 0-1 比例')
    ap.add_argument("--max", type=int, default=1500, help="核对图长边上限，默认 1500")
    args = ap.parse_args()

    src = Image.open(args.src).convert("RGB")
    tiles = []
    for text in args.regions:
        label, box = parse_region(text, src.width, src.height)
        tiles.append((label, src.crop(box)))
        print(f"{label}: 裁切 {box[0]},{box[1]} → {box[2]},{box[3]}")

    sheets = pack(tiles, args.max)
    font = load_font(20)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    for n, rows in enumerate(sheets, 1):
        path = out if len(sheets) == 1 else out.with_name(f"{out.stem}_{n}{out.suffix}")
        img = render(rows, font)
        img.save(path)
        labels = ", ".join(label for row in rows for label, _ in row)
        print(f"{path}（{img.width}×{img.height}）：{labels}")


if __name__ == "__main__":
    main()
