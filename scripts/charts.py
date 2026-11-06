"""页面里的两张 SVG 图：周报首屏的加速图、分析页的价值雷达。服务端直接出 SVG，关掉 JS 也能看。

标签位置自动选：依次试右、左、上、下四个位置，和已放下的标签或图边界相撞就换，四个都不行就不标。
"""
import math

from markupsafe import Markup, escape

CHAR_W = 7.4  # 12–13px 等宽字体的大致字宽，估标签宽度用


def _place(labels, x, y, text, bounds, gap=10):
    """返回 (x, y, anchor)，放不下返回 None。labels 记录已占用的矩形。"""
    w, h = len(text) * CHAR_W, 14
    x0, y0, x1, y1 = bounds
    for dx, dy, anchor in ((gap, 4, "start"), (-gap, 4, "end"), (0, -gap - 2, "middle"), (0, gap + 12, "middle")):
        tx, ty = x + dx, y + dy
        left = tx if anchor == "start" else tx - w if anchor == "end" else tx - w / 2
        box = (left - 2, ty - h + 3, left + w + 2, ty + 5)
        if box[0] < x0 or box[2] > x1 or box[1] < y0 or box[3] > y1:
            continue
        if any(not (box[2] < b[0] or box[0] > b[2] or box[3] < b[1] or box[1] > b[3]) for b in labels):
            continue
        labels.append(box)
        return tx, ty, anchor
    return None


# ---------- 周报：这一周谁在加速 ----------

def accel_chart(surge, href):
    """升星榜全部项目，横轴前 7 天、纵轴近 7 天新增星数，双对数坐标；持平线以上是在加速。"""
    if not surge:
        return ""
    W, H, R, T, B, L = 720, 600, 20, 20, 48, 56
    X0 = L + 36
    xmin, xmax, ymin = 10, 100000, 1000
    ymax = 10 ** math.ceil(math.log10(max(x["last7"] for x in surge) * 1.05))
    ymax = max(ymax, 10000)
    lg = math.log10
    sx = lambda v: X0 + (lg(max(v, xmin)) - lg(xmin)) / (lg(xmax) - lg(xmin)) * (W - R - X0)  # noqa: E731
    sy = lambda v: T + (lg(ymax) - lg(max(v, ymin))) / (lg(ymax) - lg(ymin)) * (H - T - B)  # noqa: E731
    fmt = {10: "10", 100: "100", 1000: "1,000", 10000: "1 万", 100000: "10 万", 1000000: "100 万"}
    g = []
    for v in (10, 100, 1000, 10000, 100000):
        g.append(f'<line class="grid" x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="{T}" y2="{H - B}"/>'
                 f'<text class="tick" x="{sx(v):.1f}" y="{H - B + 20}" text-anchor="middle">{fmt[v]}</text>')
    v = 1000
    while v <= ymax:
        g.append(f'<line class="grid" x1="{L}" x2="{W - R}" y1="{sy(v):.1f}" y2="{sy(v):.1f}"/>'
                 f'<text class="tick" x="{L - 8}" y="{sy(v) + 4:.1f}" text-anchor="end">{fmt[v]}</text>')
        v *= 10
    zero = L + 14
    g.append(f'<text class="tick" x="{zero}" y="{H - B + 20}" text-anchor="middle">0</text>')
    top = min(xmax, ymax)
    g.append(f'<line class="par" x1="{sx(ymin):.1f}" y1="{sy(ymin):.1f}" x2="{sx(top):.1f}" y2="{sy(top):.1f}"/>')
    g.append(f'<text class="zone" x="{X0 + 8}" y="{T + 20}">上方：比前一周涨得快</text>')
    g.append(f'<text class="zone" x="{W - R - 8}" y="{H - B - 12}" text-anchor="end">下方：比前一周涨得慢</text>')
    g.append(f'<text class="axis" x="{W - R}" y="{H - 8}" text-anchor="end">前 7 天新增星数 →</text>')
    pos = {}
    for x in sorted(surge, key=lambda x: x["accel"]):
        cx = sx(x["prev7"]) if x["prev7"] >= xmin else zero
        cy = sy(x["last7"])
        r = 4 + min(3, lg(max(x["last7"], 1000)) - 3) * 1.5
        pos[x["full_name"]] = (cx, cy, r)
        g.append(f'<a href="{escape(href(x))}" aria-label="{escape(x["full_name"])}"><circle class="dot{" hot" if x["accel"] else ""}" '
                 f'cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"><title>{escape(x["full_name"])}：前 7 天 {x["prev7"]:,}，近 7 天 {x["last7"]:,}</title></circle></a>')
    # 标签：加速里增量最大的 5 个 + 不加速里增量最大的 2 个
    hot = sorted((x for x in surge if x["accel"]), key=lambda x: -x["last7"])[:5]
    cold = sorted((x for x in surge if not x["accel"]), key=lambda x: -x["last7"])[:2]
    boxes = [(cx - r, cy - r, cx + r, cy + r) for cx, cy, r in (pos[x["full_name"]] for x in hot + cold)]
    for x in hot + cold:
        cx, cy, r = pos[x["full_name"]]
        name = x["full_name"].split("/")[1]
        p = _place(boxes, cx, cy, name, (L, T, W - R, H - B), gap=r + 6)
        if p:
            g.append(f'<text class="lab{" on" if x["accel"] else ""}" x="{p[0]:.1f}" y="{p[1]:.1f}" text-anchor="{p[2]}">{escape(name)}</text>')
    return Markup(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="升星榜 {len(surge)} 个项目的前 7 天与近 7 天新增星数散点图，双对数坐标">{"".join(g)}</svg>')


# ---------- 分析页：价值雷达 ----------

CX = CY = 360
RADIUS = 254


def _pol(a, r):
    return CX + r * math.cos(a), CY + r * math.sin(a)


def _rad(total, top_score):
    return 46 + (top_score - max(1, min(top_score, total))) / (top_score - 1) * (RADIUS - 58)


def _inner(svg):
    return svg[svg.index(">") + 1:svg.rindex("</svg>")]


def radar(items, order, dirs, icons, top_score=10):
    """价值分越高离中心越近；按主方向分扇区，扇区角度按项目数分；点越大周增越高。"""
    by = {k: [] for k in order}
    for x in items:
        by[x["d"][0]].append(x)
    share = sum(len(v) + 1 for v in by.values() if v)
    out = ['<svg viewBox="-60 0 840 720" role="img" aria-label="'
           f'{len(items)} 个项目的价值雷达：离中心越近价值分越高，按方向分扇区，点越大周增越高">']
    for s in (9, 7, 5):
        out.append(f'<circle class="ring" cx="{CX}" cy="{CY}" r="{_rad(s, top_score):.1f}"/>')
    out.append(f'<circle class="ring edge" cx="{CX}" cy="{CY}" r="{RADIUS}"/>')
    a = -math.pi / 2
    blips, pos = [], {}
    for k in order:
        if not by[k]:
            continue
        span = (len(by[k]) + 1) / share * 2 * math.pi
        x0, y0 = _pol(a, 20)
        x1, y1 = _pol(a, RADIUS)
        out.append(f'<line class="spoke" x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}"/>')
        mid = a + span / 2
        ix, iy = _pol(mid, RADIUS + 24)
        out.append(f'<svg class="rim-ic" x="{ix - 10:.1f}" y="{iy - 10:.1f}" width="20" height="20" viewBox="0 0 256 256" fill="currentColor">'
                   f'<title>{escape(dirs[k])}</title>{_inner(icons[k])}</svg>')
        tx, ty = _pol(mid, RADIUS + 42)
        c, s_ = math.cos(mid), math.sin(mid)
        anchor = "start" if c > .25 else "end" if c < -.25 else "middle"
        ty += 6 if abs(c) >= .25 else (12 if s_ > 0 else 0)
        out.append(f'<text class="rim" x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}">{escape(dirs[k])}</text>')
        members = sorted(by[k], key=lambda x: -x["total"])
        n = len(members)
        slots = [(i + 1) / (n + 1) for i in range(n)]
        for j, m in zip(sorted(range(n), key=lambda i: abs(slots[i] - .5)), members):
            bx, by_ = _pol(a + slots[j] * span, _rad(m["total"], top_score))
            size = 3.5 + min(9.5, math.sqrt(max(m["wk"], 0)) / 11)
            if m["tier"] == "hold":
                size = min(size, 5)
            pos[m["n"]] = (bx, by_, size)
            blips.append(f'<a href="{escape(m["u"])}" data-goto="{escape(m["id"])}" aria-label="{escape(m["n"])}"><g class="blip {m["tier"]}">'
                         f'<circle cx="{bx:.1f}" cy="{by_:.1f}" r="{size:.1f}"><title>{escape(m["n"])}：价值分 {m["total"]}，周增 {m["wk"]:,}</title></circle></g></a>')
        a += span
    sweep_end = _pol(-math.pi / 2 + math.pi / 5, RADIUS)
    out.append(f'<g class="sweep" aria-hidden="true"><path d="M{CX} {CY} L{CX} {CY - RADIUS} A{RADIUS} {RADIUS} 0 0 1 {sweep_end[0]:.1f} {sweep_end[1]:.1f} Z"/></g>')
    out += blips
    # 标签：全部「现在值得看」+ 有风险里周增最大的 2 个
    labeled = [x for x in items if x["tier"] == "top"] + sorted((x for x in items if x["tier"] == "risk"), key=lambda x: -x["wk"])[:2]
    boxes = [(cx - r, cy - r, cx + r, cy + r) for cx, cy, r in (pos[x["n"]] for x in labeled)]
    for x in labeled:
        cx, cy, r = pos[x["n"]]
        name = x["n"].split("/")[1]
        p = _place(boxes, cx, cy, name, (-60, 0, 780, 720), gap=r + 5)
        if p:
            out.append(f'<text class="b-l {"top" if x["tier"] == "top" else "minor"}" x="{p[0]:.1f}" y="{p[1]:.1f}" text-anchor="{p[2]}">{escape(name)}</text>')
    for s in (9, 7, 5):
        out.append(f'<text class="ring-l" x="{CX + 4}" y="{CY - _rad(s, top_score) - 4:.1f}">{s} 分</text>')
    out.append("</svg>")
    return Markup("".join(out))
