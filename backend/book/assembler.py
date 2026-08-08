import threading
from pathlib import Path

from .styles import PRINT_CSS, PREVIEW_EXTRA_CSS
from .outline import BOOK_META, PARTS, CHAPTERS, part_divider_html, stub_chapter_html
from . import front_matter as fm
from . import back_matter as bm
from .ch01 import CH01_HTML
from .ch02 import CH02_HTML

BOOK_DIR = Path(__file__).parent

AUTHORED = {"ch01": CH01_HTML, "ch02": CH02_HTML}


def _chapter_html(ch):
    return AUTHORED.get(ch["id"]) or stub_chapter_html(ch)


def build_sections():
    sections = [
        ("cover", "Cover", fm.cover_html()),
        ("halftitle", "Half Title", fm.halftitle_html()),
        ("titlepage", "Title Page", fm.titlepage_html()),
        ("copyright", "Copyright", fm.copyright_html()),
        ("preface", "Preface", fm.preface_html()),
        ("howto", "How to Use This Book", fm.howto_html()),
        ("syllabus", "Syllabus Mapping (BP708T)", fm.syllabus_html()),
        ("toc", "Table of Contents", fm.toc_html()),
        ("lists", "Figures, Tables & Abbreviations", fm.lists_html()),
    ]
    for part in PARTS:
        sections.append(("part%s" % part["num"], "Part %s — %s" % (part["num"], part["title"]), part_divider_html(part)))
        for ch in CHAPTERS:
            if ch["num"] in part["chapters"]:
                sections.append((ch["id"], "Chapter %d — %s" % (ch["num"], ch["title"]), _chapter_html(ch)))
    sections += [
        ("glossary", "Glossary", bm.glossary_html()),
        ("stdindex", "Standards & Regulations Index", bm.standards_index_html()),
        ("answerkeys", "Answer Keys", bm.answer_keys_html()),
        ("biblio", "Consolidated References", bm.consolidated_refs_html()),
    ]
    return sections


def full_html():
    body = "".join(html for _, _, html in build_sections())
    return """<!DOCTYPE html><html><head><meta charset="utf-8"><title>%s</title>
<style>%s</style></head>
<body style="string-set: booktitle '%s'">%s</body></html>""" % (
        BOOK_META["title"], PRINT_CSS, BOOK_META["title"].upper(), body)


def preview_html(section_id):
    for sid, label, html in build_sections():
        if sid == section_id:
            dark = ' dark' if sid in ("cover",) or sid.startswith("part") else ''
            wrapped = html if sid in ("cover",) or sid.startswith("part") else '<div class="sheet%s">%s</div>' % (dark, html)
            if sid == "cover" or sid.startswith("part"):
                wrapped = '<div class="sheet dark" style="padding:0">%s</div>' % html
            fit_js = ("<script>function fit(){var s=document.querySelector('.sheet');"
                      "if(s){document.body.style.zoom=Math.min(1,(window.innerWidth-16)/s.offsetWidth);}}"
                      "window.addEventListener('load',fit);window.addEventListener('resize',fit);</script>")
            return """<!DOCTYPE html><html><head><meta charset="utf-8"><title>%s</title>
<style>%s%s</style></head><body>%s%s</body></html>""" % (label, PRINT_CSS, PREVIEW_EXTRA_CSS, wrapped, fit_js)
    return None


_lock = threading.Lock()
_cache = {"pdf": None, "pages": 0, "building": False, "error": None}


def _render():
    from weasyprint import HTML
    doc = HTML(string=full_html(), base_url=str(BOOK_DIR)).render()
    return doc.write_pdf(), len(doc.pages)


def build_pdf_sync():
    with _lock:
        if _cache["pdf"] is not None:
            return _cache["pdf"], _cache["pages"]
        _cache["building"] = True
        try:
            pdf, pages = _render()
            _cache.update(pdf=pdf, pages=pages, error=None)
        except Exception as e:
            _cache["error"] = str(e)
            raise
        finally:
            _cache["building"] = False
        return _cache["pdf"], _cache["pages"]


def pdf_status():
    return {
        "ready": _cache["pdf"] is not None,
        "building": _cache["building"],
        "pages": _cache["pages"],
        "size_bytes": len(_cache["pdf"]) if _cache["pdf"] else 0,
        "error": _cache["error"],
    }


def warm_pdf_async():
    threading.Thread(target=lambda: _safe_build(), daemon=True).start()


def _safe_build():
    try:
        build_pdf_sync()
    except Exception:
        pass
