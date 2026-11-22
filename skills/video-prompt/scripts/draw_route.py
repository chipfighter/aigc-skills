"""在场景图副本上画带编号的运镜路线，给视频模型作参考图。

用法：
  python draw_route.py 场景图 输出图 "x1,y1 x2,y2 x3,y3" [--color red]

路点按摄影机经过的先后排列，第一个是起点。坐标可以写像素，也可以全部写
0-1 的比例（0.5,0.5 是画面中心）。只需要 Pillow。
"""

import argparse
import math
import sys

from PIL import Image, ImageColor, ImageDraw, ImageFont

COLORS = {"red": "#eb1414", "cyan": "#00d2ff", "green": "#1ee650", "yellow": "#ffd200"}
STEPS = 40  # 每段曲线的采样数
FONTS = [
    "C:/Windows/Fonts/arialbd.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "DejaVuSans-Bold.ttf",
]


def parse_points(text, width, height):
    pts = []
    for item in text.replace("，", ",").split():
        x, y = (float(v) for v in item.split(","))
        pts.append((x, y))
    if len(pts) < 2:
        sys.exit("至少要两个路点")
    if all(0 <= x <= 1 and 0 <= y <= 1 for x, y in pts):
        pts = [(x * width, y * height) for x, y in pts]
    for n, (x, y) in enumerate(pts, 1):
        if not (0 <= x <= width and 0 <= y <= height):
            print(f"注意：第 {n} 个路点 ({x:.0f},{y:.0f}) 在画面外", file=sys.stderr)
    return pts


def smooth(points):
    """穿过所有路点的 Catmull-Rom 曲线。"""
    p = [points[0]] + points + [points[-1]]
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for s in range(STEPS):
            t = s / STEPS
            out.append(tuple(
                0.5 * (2 * p1[k] + (-p0[k] + p2[k]) * t
                       + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t * t
                       + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t ** 3)
                for k in (0, 1)))
    out.append(points[-1])
    return out


def arrowhead(draw, tip, before, size, color):
    ang = math.atan2(tip[1] - before[1], tip[0] - before[0])
    left = (tip[0] - size * math.cos(ang - 0.45), tip[1] - size * math.sin(ang - 0.45))
    right = (tip[0] - size * math.cos(ang + 0.45), tip[1] - size * math.sin(ang + 0.45))
    draw.polygon([tip, left, right], fill=color)


def load_font(size):
    for path in FONTS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow < 10.1
        return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser(description="在场景图副本上画带编号的运镜路线")
    ap.add_argument("src", help="干净的场景图")
    ap.add_argument("dst", help="输出的标注图，不要覆盖原图")
    ap.add_argument("points", help='路点，按经过顺序："x1,y1 x2,y2 ..."')
    ap.add_argument("--color", default="red",
                    help="线的颜色：red、cyan、green、yellow 或 #rrggbb；场景本身红色多时换掉红色")
    args = ap.parse_args()

    img = Image.open(args.src).convert("RGB")
    color = ImageColor.getrgb(COLORS.get(args.color, args.color))
    pts = parse_points(args.points, img.width, img.height)
    w = max(4, max(img.size) // 220)

    draw = ImageDraw.Draw(img)
    curve = smooth(pts)
    draw.line(curve, fill=color, width=w, joint="curve")
    for i in range(len(pts) - 1):  # 每段中间一个方向箭头
        m = i * STEPS + STEPS // 2
        arrowhead(draw, curve[m + 1], curve[m - 1], w * 4, color)
    arrowhead(draw, curve[-1], curve[-3], w * 6, color)  # 终点大箭头

    font = load_font(w * 5)
    r = w * 4
    for n, (x, y) in enumerate(pts, 1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=(255, 255, 255), width=2)
        draw.text((x, y), str(n), fill=(255, 255, 255), font=font, anchor="mm")

    img.save(args.dst)
    print(f"已保存 {args.dst}（{img.width}×{img.height}，{len(pts)} 个路点）")


if __name__ == "__main__":
    main()
