# PRD — Medical Devices: The Complete Textbook (A4 PDF Edition)

## Original Problem Statement
A single, publication-quality book — professionally designed, A4 format, ISBN-ready — authored
under Master Prompt v5.4 as the Core Textbook of the Medical Devices Academic Ecosystem.
Aligned to PCI NEP 2020 B.Pharm syllabus (BP708T – Medical Devices elective). 14 chapters in 5 parts,
full chapter architecture (LO/CO/Bloom mapping, What–Why–How–Where–When, figures, callouts, case
studies, full assessment battery, Vancouver references, Quality Gate dashboard). Production pipeline:
print-optimized HTML/CSS compiled to A4 PDF (Python/WeasyPrint via FastAPI). Book only for now;
5 companion products later. Anti-fabrication guardrail: verified regulatory citations only.

## User Choices (defaults applied — user skipped clarification)
- Author: placeholder "Author Name, Institution Name" (swap on request)
- Figures: styled vector SVG/CSS diagrams (print-crisp), no AI image generation
- Title: "Medical Devices: A Comprehensive Textbook for Pharmacy and Allied Health Sciences"
- Content authored directly by agent (deterministic, in-codebase)
- Scope of first build: Phase 1 + Phase 2 (Part I, Ch 1–2 fully authored)

## Architecture
- Backend FastAPI (port 8001, /api prefix). WeasyPrint 69 A4 pipeline; fonts: Spectral (body serif),
  Manrope (headings) in /app/backend/book/fonts (downloaded TTF, fonttools-instanced Manrope weights).
- /app/backend/book/: styles.py (full print CSS system: @page masters cover/front/main/divider,
  running headers, roman/arabic folios, TOC leader dots + target-counter live page numbers,
  callouts, case studies, assessments, quality gate), outline.py (book metadata, 14-chapter TOC,
  6 phases, figure/table lists, stub-page generator), front_matter.py, ch01.py, ch02.py,
  back_matter.py, assembler.py (section assembly, preview HTML w/ fit-to-width zoom, PDF cache +
  startup warm build in daemon thread).
- Endpoints: GET /api/book/meta, /api/book/toc, /api/book/preview/{section_id} (HTML),
  /api/book/pdf/status, /api/book/pdf (attachment, X-Page-Count header).
  Static mount /api/book/preview/fonts for browser preview typography.
- Frontend React dashboard (Swiss/high-contrast, Cabinet Grotesk + IBM Plex Sans, Phosphor icons):
  Sidebar (phases), KPI strip, CoverCard, TocPanel (status badges), PreviewPane (A4 iframe),
  PhaseTracker, PDF download with status polling. Mongo not used (content is code-authored).

## Known technical notes
- WeasyPrint ignores counter-reset/counter-set on the `page` counter → book uses continuous page
  numbering (front matter shows roman format of same counter; main matter continues arabic ~p21).
- PDF: 93 A4 pages, ~345KB, ~30s cold build, pre-warmed at startup and cached in memory.

## What's Implemented (June 2026)
- Phase 1 COMPLETE: design system, cover, full front matter (half title, title, copyright w/ ISBN
  placeholder, preface, how-to-use, BP708T syllabus mapping, TOC with live page numbers, lists of
  figures/tables/abbreviations), chapter template, part dividers, stub pages for Ch 3–14,
  back matter skeleton (glossary 28 terms, standards index, answer keys Ch1–2, consolidated refs),
  A4 PDF pipeline, production dashboard.
- Phase 2 COMPLETE: Ch 1 (Introduction) & Ch 2 (Definitions & Classification) fully authored to
  Quality Gate: 6 LOs + CO/Bloom map, W5 framework tags, 4 SVG figures + 4–5 tables each, all 4
  callout types, 2 case studies each (AMTZ, COVID ventilators; PIP, pulse oximeter), 10 MCQ w/
  rationales + 10 T/F + 10 FIB + 5 A-R + 6 SAQ + 3 LAQ + 3 HOTS each, Vancouver refs, QG dashboard.
- Testing: iteration_1 — backend 100% (17 pytest), frontend 100%. Font-404 preview fix applied after.

## Backlog (prioritized)
- P0: Phase 3 — author Ch 3–5 (design controls, biomaterials, biocompatibility/ISO 10993)
- P0: Phase 4 — Ch 6–10 (manufacturing, ISO 13485, ISO 14971, IEC 60601, sterilization/packaging)
- P0: Phase 5 — Ch 11–14 (licensing pathways, PMS/MvPI, device categories, pharmacist careers)
- P1: Phase 6 — grow glossary/standards index/answer keys with each chapter; consistency pass; final export
- P1: Real author name/affiliation + ISBN when provided; optional AI chapter-opener artwork (Nano Banana)
- P2: Grayscale print variant; per-chapter PDF export; companion products (Lab Manual, Faculty Package, LMS)
