"""Shared helpers: pull device symbols out of the device-plan SVGs and convert to feet.

Scales are derived from each drawing's own labeled dimensions (see SCALES below).
World frame used everywhere: origin = garage NW exterior corner at the garage slab,
x = east (ft), z = south (ft), y = up (ft).
"""
import re, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAW = ROOT / "drawings"

# name -> (file, origin_px (x,y), px/ft x, px/ft y, world offset (x,z) of that origin, label basis)
SCALES = {
    # Garage outline 66.6..558.6 px wide = 42'6" exterior (41'6" interior label + 2 x 6" walls, A.2)
    # and 79.1..372.0 px deep = 25'4" exterior (24'4" label + walls).
    "G": ("1-garage-and-hallway_v20.svg", (66.6, 79.1), 492.0 / 42.5, 292.9 / (25 + 4 / 12), (0.0, 0.0)),
    # Second floor outline 72.7..583.0 px = 42'6"; 50.0..353.8 px = 25'4" (A.3 overall dims; the
    # labeled rooms 17'1" media / 14'2" x 20'8" family agree within ~3%).
    "2": ("2-second-floor_v20.svg", (72.7, 50.0), 510.3 / 42.5, 303.8 / (25 + 4 / 12), (0.0, 0.0)),
    # Third floor: legend says "Overall 42'6\" wide" = 38.1..645.9 px; depth 53.9..415.6 px = 25'4" (A.4).
    "3": ("3-third-floor_v32.svg", (38.1, 53.9), 607.8 / 42.5, 361.7 / (25 + 4 / 12), (0.0, 0.0)),
    # Sauna/shed: title "12 ft x 24 ft"; building rect 60..360 px = 12 ft -> 25 px/ft both ways.
    # Site: 20 ft south of the garage SW corner (z = 22 + 20 = 42 is the porch edge, wall at 45),
    # east wall in line with the garage west wall (x = 0), so local x 0..12 maps to world -12..0.
    "S": ("4-sauna-shed_v6.svg", (60.0, 165.0), 25.0, 25.0, (-12.0, 45.0)),
}

def _tag(e): return e.tag.split('}')[-1]

def to_ft(level, px, py):
    _, (ox, oy), sx, sy, (wx, wz) = SCALES[level]
    return round((px - ox) / sx + wx, 2), round((py - oy) / sy + wz, 2)

def devices(level):
    """Return {label: {'cls':..., 'pts':[(x_px,y_px),...], 'shape':'circle'|'rect', 'size':(w,h)}} for plan symbols.
    Only symbols above the legend block are returned (legend swatches have no text in their group)."""
    root = ET.parse(DRAW / SCALES[level][0]).getroot()
    out = {}
    def add(label, cls, shapes):
        pts, shape, size = [], None, None
        for s in shapes:
            if _tag(s) == 'circle':
                pts.append((float(s.get('cx')), float(s.get('cy')))); shape = 'circle'
            else:
                x, y, w, h = (float(s.get(k)) for k in ('x', 'y', 'width', 'height'))
                pts.append((x + w / 2, y + h / 2)); shape = 'rect'; size = (w, h)
        if not pts: return
        key = label
        if key in out: key = label + "#dup"
        out[key] = dict(cls=cls, pts=pts, shape=shape, size=size)
    for g in root.iter():
        if _tag(g) != 'g': continue
        cls = g.get('class', '')
        kids = list(g)
        texts = [k for k in kids if _tag(k) == 'text']
        if not texts: continue
        shapes = [k for k in kids if _tag(k) in ('circle', 'rect')]
        labels = [''.join(t.itertext()).strip() for t in texts]
        if len(shapes) == len(texts) and len(texts) > 1 and labels[1] != 'fan':
            for s, l in zip(shapes, labels): add(l, cls, [s])       # 3rd-floor P#/H# rows
        else:
            add(labels[0], cls, shapes)
    # third floor draws some symbols as bare class'd rects followed by a labelled circle group; the
    # circle groups are picked up above, which is what we want for IDs.
    return out

if __name__ == "__main__":
    for lv in SCALES:
        print("==", lv, SCALES[lv][0])
        for k, d in devices(lv).items():
            x, z = to_ft(lv, *d['pts'][0])
            print(f"{k:6s} {d['cls']:9s} x={x:6.2f} z={z:6.2f} n={len(d['pts'])}")
