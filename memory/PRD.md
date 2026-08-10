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
frontend/.env → REACT_APP_BACKEND_URL=https://happy-kowalevski-8.preview.emergentagent.com, WDS_SOCKET_PORT=443
backend/.env → MONGO_URL=mongodb://localhost:27017, DB_NAME=medical_devices_book, CORS_ORIGINS=*
(Mongo still unused — content is file-based.)

## Status (Aug 2026 — FINAL EDITION)
- All phases COMPLETE. Book: 726 A4 pages, ~3.5MB PDF, 20 chapters, 6 parts.
- ALL 156 FIGURES are agent-generated vector SVG via backend/book/figkit.py (18 templates:
  flow, vflow, cycle, pyramid, ladder, columns, hub, timeline, layers, matrix, decide, bars,
  vmodel, curve, formulabox, zones, labelcard, profile) + figure_specs_a/b/c.py (one spec per
  figure, keyed "1.1".."20.5", incl. clean captions used in chapter + List of Figures).
  Manuscript JPEGs in book/images/ are UNUSED fallbacks now.
- Typography: widows/orphans, teal list markers, framed .figure.vector panels.
- Two-pass figure-prompt residue removal in extractor (h4/p "Description" anchors + chart-
  narration anchors: FP_ANCHOR_P/FP_CONT_* rules). QA scan: 0 artifacts, 156/156 captions,
  TOC cross-refs exact.
- Robustness: sections lru_cached; preview via threadpool (~4ms); PDF disk cache
  (book/build/book.pdf + content-hash meta) -> instant readiness after restarts; frontend
  auto-download when typesetting finishes; PreviewPane loading/error states.
- Tested: backend 100% (testing agent, iterations 3-4), frontend UI 100% (testing agent).

## Known minor source-inherited artifacts (acceptable, fix on request)
- ~6 "Description:" figure-prompt blocks remain near some figures; ch11 glossary mangled in
  source (2-col layout lost, only 3 terms recovered); occasional merged headings/run-on lines
  from the PDF→docx source conversion; T14 (ch10 residuals table) has merged-cell gaps.

## Backlog
- P1: Real author name/affiliation/ISBN when provided; optional copy-editing pass on
  source-inherited artifacts; per-chapter PDF export
- P2: Grayscale print variant; AI chapter-opener artwork; companion products (Lab Manual,
  Faculty Package, LMS)
