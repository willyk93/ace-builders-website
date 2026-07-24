#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates original flat-style SVG illustrations for the Ace Builders site,
using only the green/cream brand palette (no photography/stock assets needed).
Run: python3 gen_illustrations.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "assets", "img", "illustrations")
os.makedirs(OUT, exist_ok=True)

# Palette
F950 = "#06231a"
F900 = "#0b3a27"
F800 = "#0f4a30"
F700 = "#146c3a"
F600 = "#1c7f42"
F500 = "#24904c"
F400 = "#3faa62"
SAGE300 = "#a9cdb2"
SAGE200 = "#cfe4d5"
SAGE100 = "#eaf4ec"
CREAM100 = "#faf8f3"
CREAM200 = "#f2efe6"
TAN300 = "#e4ddc8"
SKIN = "#e9ddc4"  # neutral, abstract "peep"-style figure tone


def write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)


def person(cx, cy, scale=1.0, body=F700, hat=F500, arm="down", accessory=None, mirrored=False):
    """A simple flat 'peep'-style figure. Origin at top of head, feet ~260 below."""
    flip = -1 if mirrored else 1
    g = [f'<g transform="translate({cx} {cy}) scale({scale*flip} {scale})">']
    # legs
    g.append(f'<rect x="-25" y="120" width="20" height="78" rx="9" fill="{F950}" opacity="0.85"/>')
    g.append(f'<rect x="5" y="120" width="20" height="78" rx="9" fill="{F950}" opacity="0.85"/>')
    # torso
    g.append(f'<rect x="-35" y="35" width="70" height="92" rx="20" fill="{body}"/>')
    # arms
    if arm == "down":
        g.append(f'<rect x="-52" y="42" width="16" height="70" rx="8" fill="{body}"/>')
        g.append(f'<rect x="36" y="42" width="16" height="70" rx="8" fill="{body}"/>')
    elif arm == "wave":
        g.append(f'<rect x="-52" y="42" width="16" height="70" rx="8" fill="{body}"/>')
        g.append(f'<rect x="30" y="-6" width="16" height="60" rx="8" fill="{body}" transform="rotate(28 38 24)"/>')
    elif arm == "forward":
        g.append(f'<rect x="-52" y="42" width="16" height="70" rx="8" fill="{body}"/>')
        g.append(f'<rect x="20" y="48" width="55" height="16" rx="8" fill="{body}"/>')
    # neck + head
    g.append(f'<rect x="-10" y="18" width="20" height="20" fill="{SKIN}"/>')
    g.append(f'<circle cx="0" cy="-6" r="30" fill="{SKIN}"/>')
    # hard hat
    if hat:
        g.append(f'<path d="M-30 -8a30 26 0 0160 0z" fill="{hat}"/>')
        g.append(f'<rect x="-34" y="-8" width="68" height="8" rx="4" fill="{hat}"/>')
    if accessory == "clipboard":
        g.append(f'<rect x="20" y="60" width="34" height="44" rx="4" fill="{CREAM100}" stroke="{F900}" stroke-width="2"/>')
        g.append(f'<path d="M27 74h20M27 84h20M27 94h12" stroke="{F700}" stroke-width="3" stroke-linecap="round"/>')
    g.append("</g>")
    return "\n".join(g)


def wrap(inner, vb="0 0 800 560", extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none">
{extra_defs}
<rect width="{vb.split()[2]}" height="{vb.split()[3]}" fill="{SAGE100}"/>
{inner}
</svg>'''


# ---------------------------------------------------------------------------
# 1. About — "our story": two figures reviewing plans by a building outline
# ---------------------------------------------------------------------------
def illus_team():
    bg_pattern = f'''
<g opacity="0.5" stroke="{SAGE200}" stroke-width="2">
  <path d="M0 480h800M0 440h800"/>
</g>
<g opacity="0.55">
  <rect x="70" y="120" width="130" height="330" fill="{SAGE200}"/>
  <rect x="215" y="180" width="90" height="270" fill="{CREAM200}"/>
  {"".join(f'<rect x="{90+((i%2)*40)}" y="{150+((i//2)*46)}" width="24" height="28" fill="{CREAM100}"/>' for i in range(14))}
</g>
<circle cx="660" cy="120" r="110" fill="{SAGE200}" opacity="0.6"/>
'''
    figs = person(430, 190, scale=1.15, body=F700, hat=F500, arm="forward")
    figs += person(560, 200, scale=1.1, body=F800, hat=F400, arm="forward", mirrored=True, accessory="clipboard")
    ground = f'<rect x="0" y="480" width="800" height="80" fill="{TAN300}" opacity="0.5"/>'
    return wrap(bg_pattern + figs + ground)


# ---------------------------------------------------------------------------
# 2. Services — HSE Consulting & Training
# ---------------------------------------------------------------------------
def illus_hse():
    board = f'''
<rect x="470" y="90" width="260" height="190" rx="10" fill="{CREAM100}" stroke="{F800}" stroke-width="4"/>
<rect x="470" y="90" width="260" height="34" rx="10" fill="{F800}"/>
<g stroke="{F600}" stroke-width="4" stroke-linecap="round">
  <path d="M500 160h200"/>
  <path d="M500 190h200"/>
  <path d="M500 220h140"/>
</g>
<circle cx="700" cy="255" r="14" fill="{F500}"/>
<path d="M693 255l5 6 11-13" stroke="{CREAM100}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
<rect x="585" y="280" width="10" height="90" fill="{F800}"/>
'''
    stand_l = f'<rect x="520" y="365" width="12" height="70" fill="{F800}"/>'
    stand_r = f'<rect x="655" y="365" width="12" height="70" fill="{F800}"/>'
    figs = person(300, 210, scale=1.25, body=F700, hat=F500, arm="wave")
    listener = person(150, 260, scale=0.95, body=SAGE300, hat=None, arm="down")
    ground = f'<ellipse cx="400" cy="470" rx="360" ry="26" fill="{TAN300}" opacity="0.5"/>'
    badge = f'''
<g transform="translate(120 120)">
  <circle r="46" fill="{CREAM100}" stroke="{F600}" stroke-width="4"/>
  <path d="M-14 0l10 11 20-24" stroke="{F600}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</g>'''
    return wrap(board + stand_l + stand_r + figs + listener + ground + badge)


# ---------------------------------------------------------------------------
# 3. Services — Hazardous Abatement (PPE worker)
# ---------------------------------------------------------------------------
def illus_abatement():
    hazard_stripes = f'''
<g opacity="0.55">
<pattern id="stripes" width="26" height="26" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <rect width="26" height="26" fill="{SAGE100}"/>
  <rect width="13" height="26" fill="{SAGE200}"/>
</pattern>
<rect x="0" y="380" width="800" height="60" fill="url(#stripes)"/>
</g>'''
    # PPE figure: full coverall (sage), respirator mask on head instead of hard hat
    cx, cy, s = 400, 150, 1.6
    figure = f'''
<g transform="translate({cx} {cy}) scale({s})">
  <rect x="-25" y="120" width="20" height="78" rx="9" fill="{F950}"/>
  <rect x="5" y="120" width="20" height="78" rx="9" fill="{F950}"/>
  <rect x="-38" y="30" width="76" height="98" rx="22" fill="{SAGE300}"/>
  <rect x="-55" y="38" width="17" height="72" rx="8" fill="{SAGE300}"/>
  <rect x="38" y="38" width="17" height="72" rx="8" fill="{SAGE300}"/>
  <circle cx="0" cy="-8" r="32" fill="{SAGE200}"/>
  <circle cx="0" cy="-4" r="19" fill="{F900}"/>
  <circle cx="0" cy="-4" r="12" fill="{F700}"/>
  <path d="M-19 -20a19 15 0 0138 0z" fill="{SAGE300}"/>
</g>'''
    tool = f'<rect x="{cx+70}" y="{cy+150}" width="14" height="90" rx="6" fill="{F800}" transform="rotate(18 {cx+70} {cy+150})"/>'
    hazard_sign = f'''
<g transform="translate(620 140)">
  <circle r="52" fill="{CREAM100}" stroke="{F600}" stroke-width="5"/>
  <circle cx="0" cy="-16" r="9" fill="{F700}"/>
  <circle cx="-16" cy="12" r="9" fill="{F700}"/>
  <circle cx="16" cy="12" r="9" fill="{F700}"/>
  <circle r="8" fill="{F900}"/>
</g>'''
    ground = f'<ellipse cx="400" cy="470" rx="360" ry="26" fill="{TAN300}" opacity="0.5"/>'
    return wrap(hazard_stripes + figure + hazard_sign + ground)


# ---------------------------------------------------------------------------
# 4. Services — Asphalt & Concrete (roller on road)
# ---------------------------------------------------------------------------
def illus_asphalt():
    sky_accent = f'<circle cx="120" cy="110" r="70" fill="{SAGE200}" opacity="0.6"/>'
    road = f'''
<rect x="0" y="360" width="800" height="120" fill="{F900}"/>
<g stroke="{CREAM100}" stroke-width="10" stroke-dasharray="46 34" opacity="0.85">
  <path d="M0 420h800"/>
</g>
<rect x="0" y="470" width="800" height="90" fill="{TAN300}" opacity="0.5"/>
'''
    # roller machine (simplified)
    roller = f'''
<g transform="translate(430 230)">
  <rect x="-40" y="30" width="220" height="90" rx="14" fill="{F700}"/>
  <rect x="-40" y="10" width="90" height="50" rx="10" fill="{F800}"/>
  <rect x="-20" y="-40" width="34" height="50" rx="6" fill="{F900}"/>
  <circle cx="-60" cy="150" r="46" fill="{F950}"/>
  <circle cx="-60" cy="150" r="18" fill="{SAGE200}"/>
  <circle cx="150" cy="150" r="46" fill="{F950}"/>
  <circle cx="150" cy="150" r="18" fill="{SAGE200}"/>
  <rect x="90" y="60" width="70" height="20" rx="8" fill="{F600}"/>
</g>'''
    steam = f'''
<g stroke="{SAGE200}" stroke-width="6" stroke-linecap="round" opacity="0.7">
  <path d="M400 150c0-20 20-20 20-40s-20-20-20-40"/>
</g>'''
    return wrap(sky_accent + road + roller + steam)


# ---------------------------------------------------------------------------
# 5. Services — Waste Management & Recycling
# ---------------------------------------------------------------------------
def illus_waste():
    ground = f'<rect x="0" y="420" width="800" height="140" fill="{TAN300}" opacity="0.55"/>'
    bin_ = f'''
<g transform="translate(300 230)">
  <path d="M-90 40 L-70 220 L170 220 L190 40 Z" fill="{F700}"/>
  <rect x="-100" y="10" width="300" height="34" rx="8" fill="{F900}"/>
  <path d="M-60 40 L170 40" stroke="{F950}" stroke-width="4" opacity="0.4"/>
</g>'''
    arrows = f'''
<g transform="translate(560 160)" stroke="{F600}" stroke-width="10" stroke-linecap="round" fill="none">
  <path d="M0 60a60 60 0 01100-46"/>
  <path d="M85 0l20 18-18 20"/>
  <path d="M120 60a60 60 0 01-100 46"/>
  <path d="M35 120l-20-18 18-20"/>
</g>'''
    leaf = f'''
<g transform="translate(120 120) scale(1.1)">
  <path d="M0 0c-38 0-62 24-62 62 34 0 62-24 62-62z" fill="{F500}"/>
  <path d="M-52 52C-38 38-20 20 0 0" stroke="{SAGE100}" stroke-width="4" fill="none" stroke-linecap="round"/>
</g>'''
    scraps = f'''
<g opacity="0.9">
  <rect x="230" y="150" width="34" height="34" rx="6" fill="{SAGE300}" transform="rotate(12 247 167)"/>
  <rect x="350" y="140" width="30" height="30" rx="6" fill="{F400}" transform="rotate(-10 365 155)"/>
  <circle cx="410" cy="175" r="16" fill="{SAGE200}"/>
</g>'''
    return wrap(ground + bin_ + arrows + leaf + scraps)


# ---------------------------------------------------------------------------
# 6. Certifications — safety briefing huddle
# ---------------------------------------------------------------------------
def illus_safety():
    ground = f'<ellipse cx="400" cy="470" rx="360" ry="26" fill="{TAN300}" opacity="0.5"/>'
    ring = f'<circle cx="400" cy="260" r="150" fill="{SAGE200}" opacity="0.45"/>'
    p1 = person(300, 190, scale=1.05, body=F700, hat=F500, arm="down")
    p2 = person(430, 175, scale=1.15, body=F800, hat=F400, arm="wave")
    p3 = person(540, 210, scale=0.95, body=F600, hat=SAGE300, arm="down", mirrored=True)
    check = f'''
<g transform="translate(650 110)">
  <circle r="42" fill="{CREAM100}" stroke="{F600}" stroke-width="5"/>
  <path d="M-13 0l10 11 18-22" stroke="{F600}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</g>'''
    return wrap(ring + p1 + p2 + p3 + ground + check)


# ---------------------------------------------------------------------------
# 7. Hero skyline banner (wide)
# ---------------------------------------------------------------------------
def hero_skyline():
    bw = 1600
    buildings = []
    import random
    xs = [40, 170, 300, 460, 620, 800, 960, 1120, 1280, 1440]
    heights = [140, 210, 120, 260, 170, 230, 150, 200, 130, 180]
    widths = [90, 110, 80, 130, 100, 120, 90, 110, 90, 100]
    colors = [F800, F900, F800, F950, F900, F800, F950, F900, F800, F950]
    for x, h, w, c in zip(xs, heights, widths, colors):
        y = 300 - h
        buildings.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>')
        # windows
        rows = max(1, h // 34)
        cols = max(1, w // 26)
        for r in range(rows):
            for co in range(cols):
                wx = x + 10 + co * 26
                wy = y + 12 + r * 34
                if wx + 12 <= x + w - 6 and wy + 16 <= y + h - 8:
                    buildings.append(f'<rect x="{wx}" y="{wy}" width="12" height="16" fill="{CREAM100}" opacity="0.16"/>')
    crane = f'''
<g stroke="{SAGE300}" stroke-width="6" stroke-linecap="round" fill="none">
  <path d="M1220 300V70"/>
  <path d="M1220 90h230"/>
  <path d="M1220 90l-70 40"/>
  <path d="M1420 90v20"/>
  <path d="M1220 140l60-30"/>
</g>'''
    ground = f'<rect x="0" y="300" width="{bw}" height="60" fill="{F950}"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {bw} 360" fill="none" preserveAspectRatio="none">
{''.join(buildings)}
{crane}
{ground}
</svg>'''


def main():
    write("illus-team.svg", illus_team())
    write("illus-hse.svg", illus_hse())
    write("illus-abatement.svg", illus_abatement())
    write("illus-asphalt.svg", illus_asphalt())
    write("illus-waste.svg", illus_waste())
    write("illus-safety.svg", illus_safety())
    write("hero-skyline.svg", hero_skyline())


if __name__ == "__main__":
    main()
