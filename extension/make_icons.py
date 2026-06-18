#!/usr/bin/env python3
"""Generate the PolyArc extension icons (icons/icon{16,32,48,128}.png).

The mark: a three-segment traffic-light gauge — green / yellow / red,
left to right — sheltering a neutral figure. The thing watching over you
*is* the GO / BE CAREFUL / STOP grade. Colors match the site's card chips.

Reproducible: run `python make_icons.py` to regenerate the icon set.
Requires Pillow (`uv pip install pillow`).
"""
import math
from PIL import Image, ImageDraw

# Brand palette (matches the site / card chips)
BG      = (12, 15, 20, 255)     # #0c0f14 dark tile
BG2     = (18, 23, 32, 255)     # subtle inner ring
GREEN   = (95, 211, 154, 255)   # #5fd39a  GO
YELLOW  = (245, 196, 81, 255)   # #f5c451  BE CAREFUL
RED     = (255, 107, 90, 255)   # #ff6b5a  STOP
NEUTRAL = (205, 214, 224, 255)  # #cdd6e0  the person ("you")

SS = 8  # supersample factor, downscaled with LANCZOS for clean edges


def _tile(S):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(S * 0.22)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=r, fill=BG)
    d.rounded_rectangle(
        [int(S * 0.06), int(S * 0.06), int(S * 0.94), int(S * 0.94)],
        radius=int(r * 0.85), outline=BG2, width=max(1, S // 120))
    return img, d


def _person(d, S, cx, head_cy, col=NEUTRAL, scale=1.05):
    hr = int(S * 0.075 * scale)
    d.ellipse([cx - hr, head_cy - hr, cx + hr, head_cy + hr], fill=col)
    sw = int(S * 0.16 * scale)
    sy = head_cy + int(hr * 0.9)
    sh = int(S * 0.13 * scale)
    d.pieslice([cx - sw, sy, cx + sw, sy + sh * 2], start=180, end=360, fill=col)


def render(px):
    S = px * SS
    img, d = _tile(S)
    # Dome gauge: span clockwise 200deg (upper-left) -> 340deg (upper-right),
    # passing through 270 (top). Three equal segments, small dark gaps.
    box = [int(S * 0.16), int(S * 0.18), int(S * 0.84), int(S * 0.86)]
    w = int(S * 0.105)
    a0, a1, gap = 200, 340, 7
    span = (a1 - a0 - 2 * gap) / 3
    segs = [(a0, a0 + span),
            (a0 + span + gap, a0 + 2 * span + gap),
            (a0 + 2 * span + 2 * gap, a1)]
    for (s, e), c in zip(segs, (GREEN, YELLOW, RED)):  # left -> right
        d.arc(box, start=s, end=e, fill=c, width=w)
    _person(d, S, S // 2, int(S * 0.54))
    return img.resize((px, px), Image.LANCZOS)


def main():
    for px in (16, 32, 48, 128):
        render(px).save(f"icons/icon{px}.png")
        print(f"wrote icons/icon{px}.png")


if __name__ == "__main__":
    main()
