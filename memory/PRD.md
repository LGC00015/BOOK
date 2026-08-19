# PRD — Medical Devices: The Complete Textbook (A4 PDF Edition)

## Original Problem Statement
A single, publication-quality book — professionally designed, A4 format, ISBN-ready.
UPDATE (Aug 2026 continuation): user uploaded their OWN complete 20-chapter manuscript
(.docx, 156 embedded figures, 19 tables, per-chapter CLOs/keywords/roadmap/case studies/
industry insights/glossary/quick recap/references). The whole book is now built from that
manuscript, replacing the earlier 14-chapter agent-drafted outline. Design system, dashboard
and PDF pipeline retained.

## User Choices
- Use embedded manuscript images as figures (no vector redraw)
- Replace old agent-drafted Ch1–2 entirely with manuscript content
- Title/author remain placeholders: "Medical Devices: A Comprehensive Textbook..." /
  "Author Name, Institution Name" (swap on request)

## Architecture
- Source manuscript: /app/source/book_source.docx
- Extraction (offline, rerunnable): /app/scripts/extract_docx.py →
  /app/backend/book/content/chNN.json + manifest.json + /app/backend/book/images/chNN_figMM.jpg
  (Pillow-compressed, max 1400px, q78). Heuristics: text-based special-section markers with
  tail-position guards, glossary separators (colon/dash/tab), roadmap-fuzzy h2 promotion,
  references segmentation, PUA-bullet stripping, box (case study/industry insight/example box)
  capture with ':'-heading containment.
- Renderer: /app/backend/book/docx_chapters.py (JSON → print HTML, design-system classes;
  also all_glossary_terms() and all_references() for back matter).
- outline.py: manifest-driven. 6 parts: I Foundations(1–3), II Lifecycle/QMS/Cleanrooms(4–6),
  III Materials/Biocompat/Design(7–9), IV Manufacturing/QC(10–11),
  V Regulation/Clinical/Post-market/Packaging/SupplyChain(12–17), VI Emerging/Data/Careers(18–20).
- front_matter.py: preface/howto/syllabus updated to 20-ch structure; TOC (no dev badges);
  lists of 156 figures + 17 tables from manifest.
- back_matter.py: consolidated glossary (merged chapter glossaries, chapter tags), curated
  standards index, chapter-by-chapter consolidated references. Answer keys REMOVED
  (manuscript has no MCQ battery; only ch10 has inline Review Questions).
- server.py: /api/book/meta, /toc, /preview/{id}, /preview/images/* (new static mount),
  /pdf/status, /pdf. Old chNN.py author files deleted.
- PDF: 754 A4 pages, ~5.1MB, ~36s build, pre-warmed at startup, cached in memory.
- Frontend dashboard unchanged except KpiStrip default (20) + footer text; fully data-driven.

## Environment note (fork gotcha)
.env files were MISSING in this fork — recreated:
frontend/.env → REACT_APP_BACKEND_URL=https://med-devices-layout.preview.emergentagent.com, WDS_SOCKET_PORT=443
backend/.env → MONGO_URL=mongodb://localhost:27017, DB_NAME=medical_devices_book, CORS_ORIGINS=*
(Mongo still unused — content is file-based.)

## Status (Aug 2026 — LAYOUT v2.0, Product 1 compliance pass)
- Book: 728 A4 pages (~3.7MB), 20 chapters, 6 parts. Manuscript frozen — layout-only pass.
- §5 margins 22/20/22/22 mirrored; §7 type scale (body 10.5/14.7, H1 22, H2 14, H3 12, caps 9)
  + lang="en" hyphenation; §9 alternating running heads (verso=chapter via data-running,
  recto=live H2 via string-set sectitle, reset at .ch-opener) + mirrored bottom-outer folios
  + "MEDICAL DEVICES" center identifier; §10 frontplain master (no folio on halftitle/title/
  copyright), roman front matter, ARABIC RESTART AT 1 via @page divider-first counter-reset
  (on .part-divider.first = partI; element-level counter-reset:page is IGNORED by WeasyPrint —
  must be inside @page rule); §15 thead/tbody in manuscript tables; §21 orphans/widows 3;
  §29 PDF metadata; §32 press variant GET /api/book/pdf?variant=press (3mm bleed + crop marks,
  TrimBox=A4, on-demand + disk cache book_press.pdf); frontend has secondary "Press PDF" button.
- §25 QA FLAG: "PCI BP708T" was hard-coded but absent from manuscript → genericized
  ("Medical Devices (B.Pharm Elective)"); restore only on Project-Lead confirmation.
- Preflight (all PASS): 156/156 figures, 20/20 TOC cross-refs exact (ch openers 3,29,49,...,647,
  all recto), 0 orphan headings, clean blanks, all fonts embedded, 0 BP708T residue.
  Full report: /app/PRODUCTION_NOTES.md.
- Known: symbol glyphs (→ ≥ ₂ ₹ ✓ …) use embedded fallback fonts; PDF/X-1a/CMYK conversion is
  printer-side (documented §33); ch03 "3.5 EU MDR" heading is an H3 source artifact (QA FLAG 2).

## Previous status (vector SVG edition)
- All 156 figures agent-generated vector SVG via figkit.py + figure_specs_a/b/c.py.
- QA corrections layer (qa_corrections.py, 51+3 fixes) — QMSR/510(k)/25kGy/ETO/market dates.

## Known minor source-inherited artifacts (acceptable, fix on request)
- ~6 "Description:" figure-prompt blocks remain near some figures; ch11 glossary mangled in
  source (2-col layout lost, only 3 terms recovered); occasional merged headings/run-on lines
  from the PDF→docx source conversion; T14 (ch10 residuals table) has merged-cell gaps.

## Backlog
- P1: Real author name/affiliation/ISBN when provided; optional copy-editing pass on
  source-inherited artifacts; per-chapter PDF export
- P2: Grayscale print variant; AI chapter-opener artwork; companion products (Lab Manual,
  Faculty Package, LMS)
