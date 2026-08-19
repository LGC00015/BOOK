"""Render the 20 extracted chapters (content/chNN.json) into print HTML
using the book's design system classes."""
import json
from functools import lru_cache
from pathlib import Path

from . import figkit
from .figure_specs import spec_for

CONTENT_DIR = Path(__file__).parent / "content"

# --- Production correction pass (layout-only, manuscript text untouched) ---
# Chapter running-header overrides for titles too long for the header band (§9).
RUNNING_OVERRIDES = {
    13: "SaMD, AI/ML & Digital Health Regulation",
}

# Pseudo-table keep-groups: source tables flattened to paragraphs during extraction.
# (start-anchor heading text prefix, end-anchor block text) — kept together on one page.
PSEUDO_TABLE_KEEPS = [
    ("Table 4.2 — Lifecycle Documentation Summary", "Ongoing per PMS data"),
]

# Case-study boxes taller than ~a page must be allowed to break internally,
# otherwise they strand their preceding heading on a near-empty page.
TALL_BOX_CHARS = 2000


def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


@lru_cache(maxsize=32)
def load_chapter(num):
    return json.loads((CONTENT_DIR / ("ch%02d.json" % num)).read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def load_manifest():
    return json.loads((CONTENT_DIR / "manifest.json").read_text(encoding="utf-8"))


def _fig_html(b):
    num = b.get("num") or ""
    spec = spec_for(num)
    if spec:
        cap = esc(spec.get("cap") or b.get("caption") or "")
        caption = "<b>Figure %s</b>" % num + ("&nbsp; %s" % cap if cap else "")
        return ('<div class="figure vector">%s<div class="figcaption">%s</div></div>'
                % (figkit.render(spec), caption))
    cap = esc(b.get("caption") or "")
    caption = "<b>Figure %s</b>" % num + ("&nbsp; %s" % cap if cap else "")
    ratio = (b.get("h") or 1) / max(b.get("w") or 1, 1)
    style = "max-height:110mm;" if ratio > 0.9 else ""
    return ('<div class="figure"><img src="%s" style="%s" alt="Figure %s"/>'
            '<div class="figcaption">%s</div></div>') % (b["src"], style, num, caption)


def _table_html(b):
    rows = b.get("rows") or []
    if not rows:
        return ""
    import re as _re
    cap_raw = b.get("caption") or ""
    # display-level dedupe: some source captions already begin with their own
    # "Table N.N —" label; strip it so the bold label is not printed twice.
    num = str(b.get("num") or "")
    cap_disp = _re.sub(r"^\s*Table\s*%s\s*[—–:-]*\s*" % _re.escape(num), "", cap_raw).strip() or cap_raw
    cap = esc(cap_disp)
    caption = "<b>Table %s</b>" % b["num"] + ("&nbsp; %s" % cap if cap else "")
    trs = []
    for i, row in enumerate(rows):
        tag = "th" if i == 0 and len(rows) > 1 else "td"
        trs.append("<tr>" + "".join("<%s>%s</%s>" % (tag, esc(c), tag) for c in row) + "</tr>")
    if len(rows) > 1:
        # explicit thead so the header row repeats when a long table breaks across pages
        body_html = "<thead>%s</thead><tbody>%s</tbody>" % (trs[0], "".join(trs[1:]))
    else:
        body_html = "".join(trs)
    return ('<div class="tablewrap"><div class="tabcaption">%s</div>'
            '<table class="data">%s</table></div>') % (caption, body_html)


def _inner_blocks_html(blocks):
    out = []
    for b in blocks:
        t = b["t"]
        if t == "p":
            out.append("<p>%s</p>" % b["html"])
        elif t == "ul":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in b["items"]))
        elif t == "h4":
            out.append('<h4 class="minisec">%s</h4>' % b["text"])
        elif t in ("h2", "h3"):
            out.append('<h4 class="minisec">%s</h4>' % b["text"])
        elif t == "table":
            out.append(_table_html(b))
        elif t == "fig":
            out.append(_fig_html(b))
    return "".join(out)


def _box_html(b):
    kind = b["kind"]
    label = esc(b.get("label") or "")
    title = esc(b.get("title") or "")
    inner = _inner_blocks_html(b.get("blocks") or [])
    if kind == "case":
        head = label + (" &mdash; %s" % title if title else "")
        # near-page-height case studies must be breakable, or they strand the
        # preceding heading on an almost-empty page (production correction)
        approx_len = sum(
            len(str(ib.get("html") or ib.get("text") or "")) + sum(len(i) for i in (ib.get("items") or []))
            for ib in (b.get("blocks") or [])
        )
        tall = " tall" if approx_len > TALL_BOX_CHARS else ""
        return ('<div class="case-study%s"><div class="cs-head">%s</div>'
                '<div class="cs-body">%s</div></div>') % (tall, head, inner)
    cls = "industry" if kind == "insight" else "didyouknow"
    title_html = "<p><strong>%s</strong></p>" % title if title else ""
    return ('<div class="callout %s"><div class="co-head">%s</div>%s%s</div>'
            ) % (cls, label, title_html, inner)


def _render_block(b):
    t = b["t"]
    if t == "h2":
        return '<h2 class="sec"><span class="secnum">%s</span>%s</h2>' % (b.get("num", ""), b["text"])
    if t == "h3":
        return '<h3 class="subsec">%s</h3>' % b["text"]
    if t == "h4":
        return '<h4 class="minisec">%s</h4>' % b["text"]
    if t == "p":
        return "<p>%s</p>" % b["html"]
    if t == "ul":
        return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in b["items"])
    if t == "fig":
        return _fig_html(b)
    if t == "table":
        return _table_html(b)
    if t == "box":
        return _box_html(b)
    return ""


def _blocks_html(blocks):
    out = []
    i, n = 0, len(blocks)
    while i < n:
        b = blocks[i]
        t = b["t"]
        text = str(b.get("text") or "")

        # (a) pseudo-table keep-group: heading anchor .. end-anchor paragraph kept on one page
        end_anchor = None
        if t in ("h2", "h3", "h4"):
            for start, end in PSEUDO_TABLE_KEEPS:
                if text.startswith(start):
                    end_anchor = end
                    break
        if end_anchor:
            grp = [_render_block(b)]
            i += 1
            while i < n:
                nb = blocks[i]
                if nb["t"] in ("box", "h2"):
                    break
                grp.append(_render_block(nb))
                plain = str(nb.get("html") or nb.get("text") or "")
                i += 1
                if plain.strip().endswith(end_anchor):
                    break
            out.append('<div class="keepwith">%s</div>' % "".join(grp))
            continue

        # (b) keep a heading (and at most one short intervening p/ul) with its table
        if t in ("h2", "h3", "h4"):
            j = i + 1
            mid = []
            if j < n and blocks[j]["t"] in ("p", "ul"):
                mid = [blocks[j]]
                j += 1
            if j < n and blocks[j]["t"] == "table":
                unit = [_render_block(b)] + [_render_block(m) for m in mid] + [_render_block(blocks[j])]
                out.append('<div class="keepwith">%s</div>' % "".join(unit))
                i = j + 1
                continue

        out.append(_render_block(b))
        i += 1
    return "".join(out)


def _glossary_html(ch):
    if not ch["glossary"]:
        return ""
    rows = "".join('<div class="kt-row"><dt>%s.</dt> <dd>%s</dd></div>'
                   % (esc(t), esc(d)) for t, d in ch["glossary"])
    return ('<div class="keyterms"><h3>Glossary &mdash; Chapter %d</h3><dl>%s</dl></div>'
            % (ch["num"], rows))


def _recap_html(ch):
    if not ch["recap_items"] and not ch["recap_intro"]:
        return ""
    intro = "<p>%s</p>" % ch["recap_intro"] if ch["recap_intro"] else ""
    items = "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in ch["recap_items"]) if ch["recap_items"] else ""
    return '<div class="summary-box"><h3>Quick Recap</h3>%s%s</div>' % (intro, items)


def _references_html(ch):
    refs = ch["references"]
    if not refs:
        return ""
    out = ['<div class="references"><h2>References</h2>']
    cur_group = object()
    open_ol = False
    for r in refs:
        g = r.get("group")
        if g != cur_group:
            if open_ol:
                out.append("</ol>")
                open_ol = False
            if g:
                out.append('<h4 class="minisec" style="margin-top:3mm;">%s</h4>' % esc(g))
            cur_group = g
        if not open_ol:
            out.append("<ol>")
            open_ol = True
        out.append("<li>%s</li>" % esc(r["text"]))
    if open_ol:
        out.append("</ol>")
    out.append("</div>")
    return "".join(out)


def chapter_html(num, part_label):
    ch = load_chapter(num)
    tagline = esc(ch["subtitle"]) if ch["subtitle"] else " &middot; ".join(ch["keywords"][:5])
    overview = "".join('<p class="lead">%s</p>' % p for p in ch["overview"])
    clos = "".join("<li>%s</li>" % c for c in ch["clos"])
    kw = " &middot; ".join(ch["keywords"])
    kw_html = ('<div class="kwline"><span class="kwlab">Keywords</span> %s</div>' % kw) if kw else ""
    roadmap = ""
    if ch["roadmap"]:
        chips = "".join('<span class="rm-chip">%s</span>' % r for r in ch["roadmap"][:12])
        roadmap = '<div class="roadmap"><span class="kwlab">Chapter Roadmap</span> %s</div>' % chips
    return """
<section class="chapter" id="%(id)s" data-running="Chapter %(num)d &middot; %(short)s">
<div class="ch-opener" data-running="Chapter %(num)d &middot; %(short)s">
  <div class="ch-kicker">%(part)s &middot; Chapter %(num)d</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">%(num02)s</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">%(title)s</h1>
      <div class="ch-tagline">%(tagline)s</div>
    </div>
  </div>
</div>
%(overview)s
<div class="objectives-box">
  <h3>Chapter Learning Outcomes</h3>
  <ol>%(clos)s</ol>
</div>
%(kw)s
%(roadmap)s
%(body)s
%(glossary)s
%(recap)s
%(references)s
</section>""" % {
        "id": ch["id"],
        "num": ch["num"],
        "num02": "%02d" % ch["num"],
        "short": esc(RUNNING_OVERRIDES.get(ch["num"]) or (ch["title"] if len(ch["title"]) <= 60 else ch["title"][:57] + "...")),
        "title": esc(ch["title"]),
        "tagline": tagline,
        "part": part_label,
        "overview": overview,
        "clos": clos,
        "kw": kw_html,
        "roadmap": roadmap,
        "body": _blocks_html(ch["blocks"]),
        "glossary": _glossary_html(ch),
        "recap": _recap_html(ch),
        "references": _references_html(ch),
    }


def all_glossary_terms():
    """Merged, sorted glossary across all chapters: [(term, definition, [ch_nums])]"""
    merged = {}
    for c in load_manifest()["chapters"]:
        ch = load_chapter(c["num"])
        for term, definition in ch["glossary"]:
            key = term.strip().lower()
            if key in merged:
                if c["num"] not in merged[key][2]:
                    merged[key][2].append(c["num"])
            else:
                merged[key] = [term.strip(), definition.strip(), [c["num"]]]
    return sorted(merged.values(), key=lambda x: x[0].lower())


def all_references():
    """[(ch_num, ch_title, [ref_texts])]"""
    out = []
    for c in load_manifest()["chapters"]:
        ch = load_chapter(c["num"])
        refs = [r["text"] for r in ch["references"]]
        if refs:
            out.append((c["num"], c["title"], refs))
    return out
