"""figkit — vector figure engine for the Medical Devices textbook.

Every figure in the book is generated from a compact spec through one of the
templates below. All output is print-crisp SVG in the book palette, sized to
the text column (720 units wide ≈ 170 mm).
"""
import math

TEAL = "#0F4C5C"
TEAL_DEEP = "#093542"
TEAL_SOFT = "#E4EFF1"
BLUE = "#14537D"
BLUE_SOFT = "#EAF2F8"
AMBER = "#B4690E"
AMBER_SOFT = "#FBF3E6"
GREEN = "#1E6E4A"
GREEN_SOFT = "#EDF6F1"
PLUM = "#5C3A6E"
PLUM_SOFT = "#F3EDF6"
RED = "#A33B3B"
RED_SOFT = "#F9EEEE"
INK = "#1A1A1A"
MUTED = "#5B6770"
RULE = "#C9D6DA"

SERIES = [TEAL, BLUE, GREEN, AMBER, PLUM, RED]
SERIES_SOFT = [TEAL_SOFT, BLUE_SOFT, GREEN_SOFT, AMBER_SOFT, PLUM_SOFT, RED_SOFT]
RISK = [GREEN, "#7B8F1E", AMBER, RED]  # low -> high


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(text, width):
    words = str(text).split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width or not cur:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def T(x, y, text, size=11, fill=INK, anchor="middle", weight="normal", width=None, lh=None, style=""):
    """Text element, word-wrapped to `width` chars if given. Returns (svg, lines)."""
    lh = lh or size + 3
    lines = wrap(text, width) if width else [str(text)]
    tsp = "".join('<tspan x="%g" dy="%s">%s</tspan>' % (x, (0 if i == 0 else lh), esc(l))
                  for i, l in enumerate(lines))
    s = ('<text x="%g" y="%g" font-size="%g" fill="%s" text-anchor="%s" font-weight="%s" %s>%s</text>'
         % (x, y, size, fill, anchor, weight, style, tsp))
    return s, len(lines)


def _arrowdefs(idsuffix=""):
    return ('<defs><marker id="ah%s" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
            '<path d="M0,0 L8,4 L0,8 z" fill="%s"/></marker></defs>' % (idsuffix, MUTED))


def _svg(height, body, w=720):
    return ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">%s%s</svg>'
            % (w, height, _arrowdefs(), body))


def _arrow(x1, y1, x2, y2, dash=""):
    d = 'stroke-dasharray="4 3"' if dash else ""
    return ('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.4" %s marker-end="url(#ah)"/>'
            % (x1, y1, x2, y2, MUTED, d))


def _box(x, y, w, h, fill, stroke, rx=3, sw=1):
    return ('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" stroke-width="%g"/>'
            % (x, y, w, h, rx, fill, stroke, sw))


# ---------------------------------------------------------------- templates

def flow(spec):
    """Horizontal flowchart. steps: [(title, sub)] — wraps to rows of `cols`."""
    steps = spec["steps"]
    cols = spec.get("cols") or min(4, len(steps))
    gap = 26
    bw = (720 - gap * (cols - 1) - 4) / cols
    bh = spec.get("bh", 66)
    rows = math.ceil(len(steps) / cols)
    H = rows * bh + (rows - 1) * 34 + 8
    out = []
    for i, st in enumerate(steps):
        title, sub = (st if isinstance(st, (tuple, list)) else (st, ""))
        r, c = divmod(i, cols)
        if r % 2 == 1:  # serpentine
            c = cols - 1 - c
        x = 2 + c * (bw + gap)
        y = 4 + r * (bh + 34)
        color = SERIES[min(r, len(SERIES) - 1)] if spec.get("rowcolor") else TEAL
        soft = SERIES_SOFT[min(r, len(SERIES) - 1)] if spec.get("rowcolor") else TEAL_SOFT
        out.append(_box(x, y, bw, bh, soft, color))
        t1, n1 = T(x + bw / 2, y + 18, title, 11.5, color, weight="bold", width=int(bw / 6.2))
        out.append(t1)
        if sub:
            t2, _ = T(x + bw / 2, y + 18 + n1 * 13 + 3, sub, 9, MUTED, width=int(bw / 4.9), lh=11)
            out.append(t2)
        nxt = i + 1
        if nxt < len(steps):
            r2, c2 = divmod(nxt, cols)
            if r2 == r:
                if r % 2 == 0:
                    out.append(_arrow(x + bw + 3, y + bh / 2, x + bw + gap - 3, y + bh / 2))
                else:
                    out.append(_arrow(x - 3, y + bh / 2, x - gap + 3, y + bh / 2))
            else:
                out.append(_arrow(x + bw / 2, y + bh + 3, x + bw / 2, y + bh + 31))
    return _svg(H, "".join(out))


def vflow(spec):
    """Vertical flowchart. steps: [(title, sub)]; title starting '?' -> diamond."""
    steps = spec["steps"]
    bw = spec.get("bw", 430)
    x0 = 360 - bw / 2
    y = 6
    out = []
    for i, st in enumerate(steps):
        title, sub = (st if isinstance(st, (tuple, list)) else (st, ""))
        is_q = str(title).startswith("?")
        title = str(title).lstrip("? ")
        subl = len(wrap(sub, 78)) if sub else 0
        bh = 34 + (12 if subl else 0) + subl * 11 + (14 if is_q else 0)
        if is_q:
            cx, cy = 360, y + bh / 2
            out.append('<polygon points="%g,%g %g,%g %g,%g %g,%g" fill="%s" stroke="%s" stroke-width="1"/>'
                       % (cx - bw / 2 - 20, cy, cx, y - 4, cx + bw / 2 + 20, cy, cx, y + bh + 4, AMBER_SOFT, AMBER))
            t1, _ = T(cx, cy - 2, title, 11.5, AMBER, weight="bold", width=52)
            out.append(t1)
            if sub:
                t2, _ = T(cx, cy + 12, sub, 9, MUTED, width=60, lh=11)
                out.append(t2)
        else:
            out.append(_box(x0, y, bw, bh, TEAL_SOFT, TEAL))
            t1, n1 = T(360, y + 20, title, 11.5, TEAL, weight="bold", width=64)
            out.append(t1)
            if sub:
                t2, _ = T(360, y + 20 + n1 * 13 + 1, sub, 9, MUTED, width=78, lh=11)
                out.append(t2)
        y += bh + (12 if is_q else 0)
        if i < len(steps) - 1:
            lbl = spec.get("edge_labels", {}).get(i)
            out.append(_arrow(360, y + 2, 360, y + 24))
            if lbl:
                t, _ = T(372, y + 16, lbl, 9, GREEN, anchor="start", weight="bold")
                out.append(t)
            y += 28
    return _svg(y + 4, "".join(out))


def cycle(spec):
    """Circular process. steps: [str] (≤8)."""
    steps = spec["steps"]
    n = len(steps)
    cx, cy, R = 360, 170, 118
    H = 340
    out = ['<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="3 4"/>' % (cx, cy, R, RULE)]
    if spec.get("center"):
        t, _ = T(cx, cy - 4, spec["center"], 12.5, TEAL, weight="bold", width=18)
        out.append(t)
    for i, st in enumerate(steps):
        a = -math.pi / 2 + 2 * math.pi * i / n
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        bw, bh = 150, 40
        color = SERIES[i % len(SERIES)]
        soft = SERIES_SOFT[i % len(SERIES)]
        bx = x - bw / 2 + 178 * math.cos(a) * 0.32
        by = y - bh / 2 + 52 * math.sin(a) * 0.55
        bx = max(2, min(720 - bw - 2, bx))
        out.append(_box(bx, by, bw, bh, soft, color))
        t1, _ = T(bx + bw / 2, by + 18, st, 10.5, color, weight="bold", width=26, lh=12)
        out.append(t1)
        a2 = a + 2 * math.pi / n * 0.42
        ax1, ay1 = cx + R * math.cos(a + 0.32), cy + R * math.sin(a + 0.32)
        ax2, ay2 = cx + R * math.cos(a2 + 0.18), cy + R * math.sin(a2 + 0.18)
        out.append('<path d="M %g %g A %g %g 0 0 1 %g %g" fill="none" stroke="%s" stroke-width="1.4" marker-end="url(#ah)"/>'
                   % (ax1, ay1, R, R, ax2, ay2, MUTED))
    return _svg(H, "".join(out))


def pyramid(spec):
    """levels: bottom-first [(label, sub)]; colors low->high risk upward."""
    levels = spec["levels"]
    n = len(levels)
    lh_px = 52
    H = n * lh_px + 30
    out = []
    top_w, bot_w = 130, 560
    for i, (label, sub) in enumerate(levels):  # i=0 bottom
        yb = H - 22 - i * lh_px
        yt = yb - lh_px + 6
        frac_b = (n - i) / n
        frac_t = (n - i - 1) / n
        w_bot = top_w + (bot_w - top_w) * frac_b
        w_top = max(top_w + (bot_w - top_w) * frac_t, top_w * 0.9)
        color = RISK[min(int(i * len(RISK) / n), len(RISK) - 1)] if not spec.get("mono") else TEAL
        cx = 300
        out.append('<polygon points="%g,%g %g,%g %g,%g %g,%g" fill="%s" opacity="0.88"/>'
                   % (cx - w_bot / 2, yb, cx + w_bot / 2, yb, cx + w_top / 2, yt, cx - w_top / 2, yt, color))
        t1, _ = T(cx, (yb + yt) / 2 + 4, label, 11.5, "#fff", weight="bold")
        out.append(t1)
        if sub:
            t2, _ = T(596, (yb + yt) / 2 - 2, sub, 9.2, MUTED, anchor="start", width=22, lh=11)
            out.append(t2)
            out.append('<line x1="%g" y1="%g" x2="588" y2="%g" stroke="%s" stroke-width="0.8"/>'
                       % (cx + w_bot / 2 + 4, (yb + yt) / 2, (yb + yt) / 2, RULE))
    lo = spec.get("axis", ("LOWER RISK", "HIGHER RISK"))
    if lo:
        out.append('<line x1="28" y1="%g" x2="28" y2="18" stroke="%s" stroke-width="1.4" marker-end="url(#ah)"/>' % (H - 24, MUTED))
        t, _ = T(16, H / 2, lo[1] + " →", 8.5, MUTED, style='transform="rotate(-90 16 %g)"' % (H / 2))
        out.append('<text x="16" y="%g" font-size="8.5" fill="%s" text-anchor="middle" transform="rotate(-90 16 %g)">%s → %s</text>'
                   % (H / 2, MUTED, H / 2, esc(lo[0]), esc(lo[1])))
    return _svg(H, "".join(out))


def ladder(spec):
    """Ascending steps left->right. steps: [(title, sub)] low risk first."""
    steps = spec["steps"]
    n = len(steps)
    bw = min(168, (720 - 20) / n - 10)
    rise = spec.get("rise", 46)
    bh = 58
    H = bh + rise * (n - 1) + 46
    out = []
    for i, (title, sub) in enumerate(steps):
        x = 8 + i * (bw + 10)
        y = H - 40 - bh - i * rise
        color = RISK[min(int(i * len(RISK) / n), len(RISK) - 1)]
        out.append(_box(x, y, bw, bh, "#fff", color, sw=1.4))
        out.append('<rect x="%g" y="%g" width="%g" height="6" fill="%s"/>' % (x, y, bw, color))
        t1, n1 = T(x + bw / 2, y + 22, title, 11, color, weight="bold", width=int(bw / 6.4))
        out.append(t1)
        if sub:
            t2, _ = T(x + bw / 2, y + 22 + n1 * 12 + 2, sub, 8.6, MUTED, width=int(bw / 4.7), lh=10)
            out.append(t2)
    out.append(_arrow(30, H - 16, 690, H - 16))
    t, _ = T(360, H - 24, spec.get("axis", "Increasing risk · increasing regulatory control"), 9.5, MUTED, weight="bold")
    out.append(t)
    return _svg(H, "".join(out))


def columns(spec):
    """Comparison panels. cols: [(header, [items])]."""
    cols = spec["cols"]
    n = len(cols)
    gap = 18
    cw = (720 - gap * (n - 1) - 4) / n
    maxit = max(sum(len(wrap(i, int(cw / 5.4))) for i in items) + len(items) for _, items in cols)
    H = 46 + maxit * 13 + 18
    out = []
    for ci, (header, items) in enumerate(cols):
        x = 2 + ci * (cw + gap)
        color = SERIES[ci % len(SERIES)]
        out.append(_box(x, 2, cw, H - 6, "#fff", color, sw=1.2))
        out.append('<rect x="%g" y="2" width="%g" height="30" rx="3" fill="%s"/>' % (x, cw, color))
        t, _ = T(x + cw / 2, 21, header, 11, "#fff", weight="bold", width=int(cw / 6))
        out.append(t)
        y = 50
        for it in items:
            lines = wrap(it, int(cw / 5.4))
            out.append('<circle cx="%g" cy="%g" r="2" fill="%s"/>' % (x + 12, y - 3.5, color))
            for li, l in enumerate(lines):
                t, _ = T(x + 22, y, l, 9.4, INK, anchor="start")
                out.append(t)
                y += 13
            y += 4
    return _svg(H, "".join(out))


def hub(spec):
    """Hub-and-spoke ecosystem. center: str, spokes: [(label, sub)]."""
    spokes = spec["spokes"]
    n = len(spokes)
    cx, cy = 360, 190
    H = 380
    Rr = 150
    out = []
    for i, sp in enumerate(spokes):
        label, sub = (sp if isinstance(sp, (tuple, list)) else (sp, ""))
        a = -math.pi / 2 + 2 * math.pi * i / n
        x, y = cx + Rr * 1.55 * math.cos(a), cy + Rr * 0.82 * math.sin(a)
        x = max(80, min(640, x))
        bw, bh = 158, 46 if sub else 34
        color = SERIES[i % len(SERIES)]
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1"/>'
                   % (cx, cy, x, y, RULE))
        out.append(_box(x - bw / 2, y - bh / 2, bw, bh, SERIES_SOFT[i % len(SERIES)], color))
        t1, _ = T(x, y - (6 if sub else -4), label, 10.5, color, weight="bold", width=27, lh=11)
        out.append(t1)
        if sub:
            t2, _ = T(x, y + 10, sub, 8.4, MUTED, width=32, lh=9.6)
            out.append(t2)
    out.append('<circle cx="%g" cy="%g" r="66" fill="%s"/>' % (cx, cy, TEAL))
    t, _ = T(cx, cy + 2, spec["center"], 12, "#fff", weight="bold", width=13, lh=13)
    out.append(t)
    return _svg(H, "".join(out))


def timeline(spec):
    """events: [(label, text)] on a horizontal line, alternating."""
    events = spec["events"]
    n = len(events)
    H = 200
    y0 = H / 2
    out = ['<line x1="24" y1="%g" x2="696" y2="%g" stroke="%s" stroke-width="2"/>' % (y0, y0, TEAL)]
    for i, (label, text) in enumerate(events):
        x = 40 + i * (640 / max(n - 1, 1))
        up = i % 2 == 0
        out.append('<circle cx="%g" cy="%g" r="5" fill="%s"/>' % (x, y0, SERIES[i % len(SERIES)]))
        ty = y0 - 24 if up else y0 + 30
        t1, _ = T(x, ty, label, 11, SERIES[i % len(SERIES)], weight="bold")
        out.append(t1)
        t2, n2 = T(x, ty + (12 if not up else 12), "", 8.6, MUTED)
        lines = wrap(text, 18)
        step = 10.5
        base = (ty + 12) if not up else (ty - 12 - (len(lines) - 1) * step)
        for li, l in enumerate(lines):
            t, _ = T(x, base + li * step, l, 8.6, MUTED)
            out.append(t)
    return _svg(H, "".join(out))


def layers(spec):
    """Stacked bands. bands: top-first [(label, sub)]."""
    bands = spec["bands"]
    out = []
    y = 4
    for i, (label, sub) in enumerate(bands):
        subl = len(wrap(sub, 74)) if sub else 0
        bh = 34 + subl * 11 + (6 if subl else 0)
        color = SERIES[i % len(SERIES)]
        out.append(_box(60, y, 600, bh, SERIES_SOFT[i % len(SERIES)], color, sw=1.2))
        t1, _ = T(360, y + 20, label, 11.5, color, weight="bold", width=68)
        out.append(t1)
        if sub:
            t2, _ = T(360, y + 33, sub, 9, MUTED, width=74, lh=11)
            out.append(t2)
        y += bh + 8
    return _svg(y, "".join(out))


def matrix(spec):
    """Grid. headers: [str], rows: [[str,...]] (first cell = row head)."""
    headers = spec["headers"]
    rows = spec["rows"]
    nc = len(headers)
    cw = [180] + [(720 - 184) / (nc - 1)] * (nc - 1) if spec.get("wide_first", True) else [720 / nc] * nc
    rh = spec.get("rh", 34)
    H = 30 + len(rows) * rh + 6
    out = []
    x = 2
    for ci, h in enumerate(headers):
        out.append(_box(x, 2, cw[ci] - 4, 26, TEAL, TEAL, rx=2))
        t, _ = T(x + (cw[ci] - 4) / 2, 19, h, 9.6, "#fff", weight="bold", width=int(cw[ci] / 6))
        out.append(t)
        x += cw[ci]
    for ri, row in enumerate(rows):
        y = 30 + ri * rh
        x = 2
        for ci, cell in enumerate(row):
            fill = "#F3F8F9" if ri % 2 == 0 else "#fff"
            out.append(_box(x, y, cw[ci] - 4, rh - 4, fill, RULE, rx=2, sw=0.6))
            cell = str(cell)
            color = INK
            wgt = "bold" if ci == 0 else "normal"
            if cell in ("✓", "●"):
                color, wgt = GREEN, "bold"
            elif cell in ("✗", "—"):
                color = MUTED
            t, _ = T(x + (cw[ci] - 4) / 2, y + rh / 2 - 2 + 3, cell, 9.2, color if ci else TEAL,
                     weight=wgt, width=int(cw[ci] / 5.4), lh=10)
            out.append(t)
            x += cw[ci]
    return _svg(H, "".join(out))


def decide(spec):
    """Vertical decision chain. qs: [(question, yes_result)], final: str."""
    qs = spec["qs"]
    out = []
    y = 8
    for q, yes in qs:
        cx = 300
        bh = 56
        out.append('<polygon points="%g,%g %g,%g %g,%g %g,%g" fill="%s" stroke="%s"/>'
                   % (cx - 190, y + bh / 2, cx, y, cx + 190, y + bh / 2, cx, y + bh, AMBER_SOFT, AMBER))
        t1, _ = T(cx, y + bh / 2 + 3, q, 10, AMBER, weight="bold", width=40, lh=11)
        out.append(t1)
        out.append(_arrow(cx + 192, y + bh / 2, 548, y + bh / 2))
        ty, _ = T(524, y + bh / 2 - 8, "YES", 8.5, GREEN, weight="bold")
        out.append(ty)
        out.append(_box(552, y + bh / 2 - 20, 162, 40, GREEN_SOFT, GREEN))
        t2, _ = T(633, y + bh / 2 - 4, yes, 9.4, GREEN, weight="bold", width=28, lh=10.5)
        out.append(t2)
        out.append(_arrow(cx, y + bh + 2, cx, y + bh + 26))
        tn, _ = T(cx + 12, y + bh + 18, "NO", 8.5, MUTED, anchor="start", weight="bold")
        out.append(tn)
        y += bh + 30
    out.append(_box(300 - 140, y, 280, 40, TEAL, TEAL))
    tf, _ = T(300, y + 24, spec["final"], 11, "#fff", weight="bold", width=44)
    out.append(tf)
    return _svg(y + 48, "".join(out))


def bars(spec):
    """Horizontal bars. items: [(label, value, note)] value 0-100 relative."""
    items = spec["items"]
    mx = max(v for _, v, *_ in items) or 1
    H = len(items) * 40 + 26
    out = []
    for i, it in enumerate(items):
        label, v = it[0], it[1]
        note = it[2] if len(it) > 2 else ""
        y = 10 + i * 40
        t1, _ = T(190, y + 15, label, 9.8, INK, anchor="end", weight="bold", width=36, lh=10.5)
        out.append(t1)
        w = 20 + (460 - 20) * (v / mx)
        out.append('<rect x="200" y="%g" width="%g" height="20" rx="2" fill="%s" opacity="0.9"/>'
                   % (y, w, SERIES[i % len(SERIES)]))
        t2, _ = T(206 + w, y + 14, note or str(v), 9.2, MUTED, anchor="start")
        out.append(t2)
    out.append('<line x1="200" y1="%g" x2="200" y2="6" stroke="%s" stroke-width="1"/>' % (H - 12, RULE))
    return _svg(H, "".join(out))


def vmodel(spec):
    """V-model. left: [str] top-down, right: [str] bottom-up, bottom: str."""
    left, right, bottom = spec["left"], spec["right"], spec["bottom"]
    n = len(left)
    H = n * 62 + 96
    bw, bh = 218, 44
    out = []
    for i in range(n):
        lx = 20 + i * 34
        y = 10 + i * 62
        out.append(_box(lx, y, bw, bh, TEAL_SOFT, TEAL))
        t, _ = T(lx + bw / 2, y + bh / 2 + 3.5, left[i], 9.6, TEAL, weight="bold", width=38, lh=10.5)
        out.append(t)
        rx = 700 - bw - 20 - i * 34
        out.append(_box(rx, y, bw, bh, GREEN_SOFT, GREEN))
        t, _ = T(rx + bw / 2, y + bh / 2 + 3.5, right[n - 1 - i], 9.6, GREEN, weight="bold", width=38, lh=10.5)
        out.append(t)
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>'
                   % (lx + bw + 4, y + bh / 2, rx - 4, y + bh / 2, RULE))
        if i < n - 1:
            out.append(_arrow(20 + i * 34 + bw / 2 + 20, y + bh + 2, 20 + (i + 1) * 34 + bw / 2, y + 60))
            out.append(_arrow(700 - 20 - (i + 1) * 34 - bw / 2, y + 62 + bh - 2, 700 - 20 - i * 34 - bw / 2 + 18, y + bh + 3))
    y = 10 + n * 62 + 6
    out.append(_box(360 - 130, y, 260, 42, AMBER_SOFT, AMBER))
    t, _ = T(360, y + 25, bottom, 10.5, AMBER, weight="bold", width=42)
    out.append(t)
    return _svg(H, "".join(out))


def curve(spec):
    """Stress–strain curve with labeled regions (materials chapter)."""
    H = 300
    out = []
    out.append('<line x1="60" y1="260" x2="690" y2="260" stroke="%s" stroke-width="1.6" marker-end="url(#ah)"/>' % INK)
    out.append('<line x1="60" y1="260" x2="60" y2="20" stroke="%s" stroke-width="1.6" marker-end="url(#ah)"/>' % INK)
    t, _ = T(375, 288, spec.get("x", "Strain (deformation)"), 10.5, INK, weight="bold")
    out.append(t)
    out.append('<text x="20" y="140" font-size="10.5" font-weight="bold" fill="%s" text-anchor="middle" transform="rotate(-90 20 140)">%s</text>'
               % (INK, esc(spec.get("y", "Stress (force / area)"))))
    out.append('<path d="M60,260 L200,90 C240,45 300,38 360,44 C450,54 560,70 640,120" fill="none" stroke="%s" stroke-width="3"/>' % TEAL)
    pts = [(200, 90, "Proportional limit / yield point", AMBER),
           (360, 44, "Ultimate tensile strength", RED),
           (640, 120, "Fracture point", PLUM)]
    for x, y, lbl, c in pts:
        out.append('<circle cx="%g" cy="%g" r="5" fill="%s"/>' % (x, y, c))
        t, _ = T(x + 6, y - 12, lbl, 9.4, c, anchor="start", weight="bold", width=26, lh=10.5)
        out.append(t)
    out.append('<rect x="60" y="20" width="140" height="240" fill="%s" opacity="0.25"/>' % GREEN_SOFT)
    t, _ = T(130, 240, "Elastic region (recoverable)", 9, GREEN, width=16, lh=10)
    out.append(t)
    t, _ = T(430, 240, "Plastic region (permanent deformation)", 9, MUTED, width=28, lh=10)
    out.append(t)
    return _svg(H, "".join(out))


def formulabox(spec):
    """Formula panel. lines: [(formula, note)]."""
    lines = spec["lines"]
    H = 30 + len(lines) * 56 + 6
    out = [_box(60, 4, 600, H - 10, "#FBFDFD", RULE, sw=1)]
    y = 40
    for f, note in lines:
        out.append('<text x="360" y="%g" font-size="17" fill="%s" text-anchor="middle" font-family="Spectral" font-style="italic">%s</text>'
                   % (y, TEAL_DEEP, esc(f)))
        if note:
            t, _ = T(360, y + 18, note, 9.4, MUTED, width=90, lh=11)
            out.append(t)
        y += 56
    return _svg(H, "".join(out))


def zones(spec):
    """Room/zone sequence (cleanroom, warehouse). rooms: [(name, sub, badge)]."""
    rooms = spec["rooms"]
    n = len(rooms)
    gap = 16
    bw = (720 - gap * (n - 1) - 8) / n
    H = 150
    out = []
    for i, (name, sub, badge) in enumerate(rooms):
        x = 4 + i * (bw + gap)
        color = SERIES[i % len(SERIES)]
        out.append(_box(x, 26, bw, 86, SERIES_SOFT[i % len(SERIES)], color, sw=1.3))
        if badge:
            out.append(_box(x + bw / 2 - 34, 12, 68, 20, color, color, rx=9))
            t, _ = T(x + bw / 2, 26, badge, 8.6, "#fff", weight="bold")
            out.append(t)
        t1, n1 = T(x + bw / 2, 56, name, 10.5, color, weight="bold", width=int(bw / 6))
        out.append(t1)
        if sub:
            t2, _ = T(x + bw / 2, 56 + n1 * 12 + 2, sub, 8.6, MUTED, width=int(bw / 4.8), lh=10)
            out.append(t2)
        if i < n - 1:
            out.append(_arrow(x + bw + 2, 69, x + bw + gap - 2, 69))
    if spec.get("legend"):
        t, _ = T(360, 136, spec["legend"], 9, MUTED, width=110)
        out.append(t)
    return _svg(H, "".join(out))


def labelcard(spec):
    """Mock device label / UDI label. fields: [(key, value)], title: str."""
    fields = spec["fields"]
    H = 66 + len(fields) * 24 + (46 if spec.get("barcode", True) else 8)
    out = [_box(90, 6, 540, H - 12, "#fff", INK, rx=2, sw=1.4)]
    t, _ = T(360, 30, spec.get("title", "STERILE MEDICAL DEVICE — SINGLE USE"), 12, INK, weight="bold")
    out.append(t)
    out.append('<line x1="106" y1="40" x2="614" y2="40" stroke="%s" stroke-width="0.8"/>' % RULE)
    y = 62
    for k, v in fields:
        t1, _ = T(116, y, k, 9.6, TEAL, anchor="start", weight="bold")
        out.append(t1)
        t2, _ = T(280, y, v, 9.6, INK, anchor="start")
        out.append(t2)
        y += 24
    if spec.get("barcode", True):
        x = 150
        import random
        rnd = random.Random(7)
        while x < 480:
            w = rnd.choice([2, 2, 3, 4])
            out.append('<rect x="%g" y="%g" width="%g" height="30" fill="%s"/>' % (x, y - 6, w, INK))
            x += w + rnd.choice([2, 3, 4])
        t, _ = T(320, y + 36, "(01) 08901234567894 (11) 260101 (17) 290101 (10) LOT4521", 8.6, MUTED)
        out.append(t)
    return _svg(H, "".join(out))


def profile(spec):
    """Step profile chart (e.g., sterilization cycle). phases: [(name, level, dur)]."""
    phases = spec["phases"]
    H = 240
    total = sum(p[2] for p in phases)
    out = []
    out.append('<line x1="50" y1="200" x2="700" y2="200" stroke="%s" stroke-width="1.4" marker-end="url(#ah)"/>' % INK)
    out.append('<line x1="50" y1="200" x2="50" y2="16" stroke="%s" stroke-width="1.4" marker-end="url(#ah)"/>' % INK)
    t, _ = T(375, 226, spec.get("x", "Cycle time →"), 9.6, MUTED, weight="bold")
    out.append(t)
    out.append('<text x="18" y="110" font-size="9.6" font-weight="bold" fill="%s" text-anchor="middle" transform="rotate(-90 18 110)">%s</text>'
               % (MUTED, esc(spec.get("y", "Parameter level"))))
    x = 50
    lasty = 200
    for i, (name, level, dur) in enumerate(phases):
        w = 630 * dur / total
        y = 196 - level * 1.6
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.4"/>' % (x, lasty, x, y, TEAL))
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.4"/>' % (x, y, x + w, y, TEAL))
        out.append('<rect x="%g" y="200" width="%g" height="6" fill="%s" opacity="0.85"/>' % (x, w, SERIES[i % len(SERIES)]))
        t, _ = T(x + w / 2, y - 10, name, 8.8, SERIES[i % len(SERIES)], weight="bold", width=int(max(w, 60) / 4.6), lh=9.6)
        out.append(t)
        x += w
        lasty = y
    out.append('<line x1="%g" y1="%g" x2="%g" y2="200" stroke="%s" stroke-width="2.4"/>' % (x, lasty, x, TEAL))
    return _svg(H, "".join(out))


TEMPLATES = {
    "flow": flow, "vflow": vflow, "cycle": cycle, "pyramid": pyramid,
    "ladder": ladder, "columns": columns, "hub": hub, "timeline": timeline,
    "layers": layers, "matrix": matrix, "decide": decide, "bars": bars,
    "vmodel": vmodel, "curve": curve, "formulabox": formulabox,
    "zones": zones, "labelcard": labelcard, "profile": profile,
}


def render(spec):
    return TEMPLATES[spec["t"]](spec)
