# PRODUCTION NOTES — A4 PRINT EDITION
## Medical Devices: A Comprehensive Textbook for Pharmacy and Allied Health Sciences
### Product 1 — Typesetting, Layout & Visual Design · Layout v2.0

**Manuscript Version:** FINAL / FROZEN (post-QA, 51+3 corrections layer applied)
**Layout Version:** v2.0 — Product 1 Master Prompt compliance pass
**Output:** A4 Print Edition, 728 pages · Standard PDF + Press PDF (3 mm bleed, crop marks)
**Date:** August 2026

---

## 1. LAYOUT v2.0 CHANGELOG (design only — zero manuscript changes)

| # | Spec § | Change | Pages affected | Manuscript affected? |
|---|---|---|---|---|
| 1 | §5 | Page geometry set to gutter 22 mm / outer 20 mm / top+bottom 22 mm, fully mirrored on verso/recto (was 20/16/20) | all | NO |
| 2 | §7 | Type scale: body 10.5 pt / ≈14.7 pt leading; Chapter H1 22 pt; H2 14 pt; H3 12 pt; H4 10.5 pt; captions 9 pt / 11 pt; Part opener 28 pt | all | NO |
| 3 | §7 | True English hyphenation enabled (html lang="en" → Pyphen dictionary) for justified body text | all | NO |
| 4 | §9 | Alternating running heads: VERSO = chapter/part title (small caps, teal), RECTO = current section title (auto-tracked from every H2 via string-set; reset to chapter label at each chapter opener). Thin hairline rule under both. Suppressed on chapter openers and dividers | main text | NO |
| 5 | §9/§10 | Folios mirrored to bottom-outer corners; restrained "MEDICAL DEVICES" identifier bottom-center; folio suppressed on half-title, title page, copyright (new frontplain master); front matter roman (i, ii…), MAIN TEXT RESTARTS AT ARABIC 1 at Part I divider; back matter continues Arabic | all | NO |
| 6 | §15 | Manuscript tables now emit explicit thead/tbody → header row repeats automatically if a table ever breaks across pages; caption keep-with-table (`break-after: avoid`); tables keep-together where they fit | tables | NO (identical text) |
| 7 | §21 | Orphan/widow protection raised to 3 lines on paragraphs; keep-with-next retained on all heading levels; keep-together on callouts, case studies, figures, captions, objectives and recap boxes | all | NO |
| 8 | §29 | Full PDF metadata embedded: title, author, subject/description, keywords, generator. Bookmarks + clickable TOC retained | n/a | NO |
| 9 | §32 | NEW press-production variant `GET /api/book/pdf?variant=press`: 3 mm bleed + crop/registration marks; TrimBox = exact A4 (210 × 297 mm), MediaBox 216 × 303 mm. On-demand, disk-cached | all | NO |
| 10 | §25 | Unverified syllabus code removed (see QA FLAG 1) | cover, title, preface, syllabus page, TOC | front matter only (agent-authored, not manuscript) |

---

## 2. TEXTBOOK QA FLAGS (raised, NOT silently corrected — per §4/§20)

### QA FLAG 1 — Syllabus code "PCI BP708T" (§25) — RESOLVED BY GENERICIZATION, AWAITING PROJECT-LEAD CONFIRMATION
- **Location:** cover badges, title page, preface, syllabus-mapping page, TOC label (front matter — agent-authored, not part of the frozen manuscript)
- **Existing text:** "PCI NEP 2020 Aligned", "BP708T · Medical Devices", "Syllabus Mapping — PCI BP708T"
- **Issue:** The code "BP708T"/"PCI" appears NOWHERE in the frozen manuscript (verified against book_source.docx). Product 1 §25 forbids hard-coding a course code that is not in the approved manuscript.
- **Action applied:** genericized to "Medical Devices (B.Pharm Elective)" wording. The mapping table itself (units → chapters) is retained.
- **To restore:** Project Lead confirmation that the book targets PCI BP708T; then the exact code can be reinstated on request.

### QA FLAG 2 — Heading-level artifact in Chapter 3 (source-inherited)
- **Location:** Chapter 3, sub-heading "3.5 European Union MDR Classification System" (stored as H3 in extracted content; chapter-level H2 sections are 3.1–3.5 with different titles, e.g., H2 3.5 = "Practical Applications")
- **Issue:** Numbering/level inconsistency inherited from the PDF→DOCX source conversion. The recto running header correctly tracks H2 sections only, so this H3's number never appears in headers.
- **Recommended action:** author to confirm intended section hierarchy in a future revision. NOT corrected (manuscript frozen).

### QA FLAG 3 — Special-symbol glyph fallback (§8 note)
- The manuscript uses symbols outside the Spectral/Manrope glyph sets: → ↓ ≥ ≤ ≈ ● ✓ ✗ ₹ and scientific super/subscripts (⁻ ⁶ ₀ ₁ ₂ ⁴).
- These render through embedded fallback fonts (FreeSerif, FreeSans, WenQuanYi Zen Hei, IPA Gothic). All are embedded and print-safe; substitution is deterministic (symbols only, never body text). No content change.

---

## 3. PREFLIGHT REPORT (§34–§35) — Layout v2.0, 728-page build

| Check | Result |
|---|---|
| Page size | 210.0 × 297.0 mm exact A4, all 728 pages ✅ |
| Margins | 22/20/22/22 mirrored ✅ |
| Fonts | 15 subsets, ALL embedded (pdffonts audit) ✅ |
| Metadata | Title/Author/Keywords/Producer present ✅ |
| Figures | 156/156 captions present in PDF text layer (whitespace-tolerant audit) ✅ |
| Tables | 17/17 with caption-above, keep-together, thead repetition armed ✅ |
| TOC cross-refs | ALL 20 chapter page numbers exact vs printed folios (3, 29, 49, 91, 141, 165, 189, 219, 245, 275, 309, 353, 395, 433, 489, 515, 555, 583, 609, 647) ✅ |
| Chapter openers | all 20 start on recto (odd folio) ✅ |
| Running heads | verso = chapter (verified), recto = live H2 section title (verified on ch03 spread) ✅ |
| Folio system | cover/half-title/title/copyright folio-free; preface→lists roman ix–xxv; main restarts at Arabic 1 at Part I ✅ |
| Orphan headings | 0 pages end on a heading-like line (automated scan) ✅ |
| Blank pages | inserted blanks fully clean (no folio/header leak) ✅ |
| BP708T residue | 0 occurrences in PDF ✅ |
| QA-corrections layer | intact (QMSR, 510(k), 25 kGy, ETO, market-date wordings re-verified via API) ✅ |
| Press variant | TrimBox = A4, BleedBox present, MediaBox 216 × 303 mm with marks ✅ |

**Content-integrity statement (§35):** chapter JSONs (frozen manuscript extraction + QA corrections layer) are byte-identical to the previous edition; the renderer changes are purely structural (thead/tbody wrapper, data-running attribute). No paragraph, heading, value, table cell, caption, reference or glossary definition was altered.

---

## 4. HONEST PRE-PRESS LIMITATIONS (§31/§33)

- The WeasyPrint pipeline outputs PDF 1.7 with embedded fonts and vector artwork in RGB/device colour. **Certified PDF/X-1a / PDF/X-4 with CMYK ICC conversion is not produced by this pipeline** — that final normalization is the printer's standard prepress step (Acrobat Preflight or Ghostscript with an ICC output intent, e.g. `-dPDFX` + FOGRA39). The press variant supplies correct TrimBox/BleedBox/crop marks for that step.
- Tagged-PDF accessibility (PDF/UA) is partially supported by the engine; heading structure, bookmarks, searchable text and colour-safe design are in place.
- Table continuation labels ("Table X.X — Continued") cannot be generated by CSS paged media; instead all 17 manuscript tables are kept whole on a page (verified — none break), with thead repetition armed as a safety net.

---

## 5. STATUS

**LAYOUT-READY: YES** — all design and pagination requirements satisfied.
**PRESS-READY: YES, with the §33 note above** (PDF/X normalization at printer).
**PUBLISHER-READY: pending** — Project Lead approval + publication metadata (author name, affiliation, ISBN, publisher confirmation — see QA_REPORT.md Part F).
