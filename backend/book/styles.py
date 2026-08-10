PRINT_CSS = """
@font-face { font-family: 'Spectral'; src: url('fonts/Spectral-Regular.ttf'); font-weight: 400; font-style: normal; }
@font-face { font-family: 'Spectral'; src: url('fonts/Spectral-Italic.ttf'); font-weight: 400; font-style: italic; }
@font-face { font-family: 'Spectral'; src: url('fonts/Spectral-SemiBold.ttf'); font-weight: 600; font-style: normal; }
@font-face { font-family: 'Spectral'; src: url('fonts/Spectral-Bold.ttf'); font-weight: 700; font-style: normal; }
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-Medium.ttf'); font-weight: 500; font-style: normal; }
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-SemiBold.ttf'); font-weight: 600; font-style: normal; }
@font-face { font-family: 'Manrope'; src: url('fonts/Manrope-ExtraBold.ttf'); font-weight: 800; font-style: normal; }

:root {
  --teal: #0F4C5C;
  --teal-deep: #093542;
  --teal-soft: #E4EFF1;
  --blue: #14537D;
  --ink: #1A1A1A;
  --muted: #5B6770;
  --rule: #C9D6DA;
  --amber: #B4690E;
  --green: #1E6E4A;
  --plum: #5C3A6E;
}

* { box-sizing: border-box; }

html { font-size: 10.2pt; }
body {
  font-family: 'Spectral', serif;
  color: var(--ink);
  line-height: 1.52;
  margin: 0;
  font-weight: 400;
  text-rendering: optimizeLegibility;
}

/* ---------- PAGE MASTERS ---------- */
@page {
  size: A4;
  margin: 20mm 16mm 20mm 20mm;
}
@page :left { margin: 20mm 20mm 20mm 16mm; }

@page cover { margin: 0; background: var(--teal-deep); }

@page front {
  margin: 22mm 18mm 22mm 20mm;
  @bottom-center { content: counter(page, lower-roman); font-family: 'Manrope'; font-size: 8pt; color: #5B6770; }
}

@page main {
  @top-left { content: string(booktitle); font-family: 'Manrope'; font-weight: 600; font-size: 7pt; letter-spacing: 0.14em; text-transform: uppercase; color: #0F4C5C; }
  @top-right { content: string(chaptertitle); font-family: 'Manrope'; font-size: 7pt; letter-spacing: 0.06em; color: #5B6770; }
  @bottom-center { content: counter(page); font-family: 'Manrope'; font-weight: 600; font-size: 8.5pt; color: #0F4C5C; }
  @top-center { content: ''; }
}
@page main:first { @top-left { content: ''; } @top-right { content: ''; } }

@page divider { background: var(--teal-deep); margin: 0;
  @bottom-center { content: ''; } @top-left { content: ''; } @top-right { content: ''; }
}

.cover-page { page: cover; }
.front-section { page: front; break-before: right; }
.part-divider { page: divider; break-before: right; }
.chapter, .backmatter-section { page: main; break-before: right; }

/* ---------- COVER ---------- */
.cover-page { width: 210mm; height: 296mm; background: var(--teal-deep); color: #fff; position: relative; overflow: hidden; }
.cover-grid-lines { position: absolute; top: 0; left: 0; width: 210mm; height: 297mm; }
.cover-inner { position: absolute; top: 0; left: 0; width: 210mm; height: 297mm; padding: 22mm 18mm; }
.cover-series { font-family: 'Manrope'; font-weight: 600; font-size: 8pt; letter-spacing: 0.32em; text-transform: uppercase; color: #7FB6C4; border: 1px solid #2C6B7C; display: inline-block; padding: 2.4mm 5mm; }
.cover-title { font-family: 'Manrope'; font-weight: 800; font-size: 34pt; line-height: 1.06; margin: 26mm 0 0 0; color: #FFFFFF; letter-spacing: -0.01em; }
.cover-title .accent { color: #8FD6E8; }
.cover-subtitle { font-family: 'Spectral'; font-style: italic; font-size: 12.5pt; color: #BCD9E1; margin-top: 8mm; line-height: 1.5; max-width: 150mm; }
.cover-badges { margin-top: 12mm; }
.cover-badge { display: inline-block; font-family: 'Manrope'; font-weight: 600; font-size: 7.5pt; letter-spacing: 0.1em; text-transform: uppercase; color: #DDEFF4; border-left: 2.5pt solid #8FD6E8; padding: 1mm 0 1mm 3.5mm; margin-right: 9mm; }
.cover-art { margin-top: 13mm; }
.cover-author-block { position: absolute; bottom: 22mm; left: 18mm; right: 18mm; border-top: 1px solid #2C6B7C; padding-top: 6mm; }
.cover-author { font-family: 'Manrope'; font-weight: 800; font-size: 13pt; color: #fff; }
.cover-affil { font-family: 'Manrope'; font-weight: 500; font-size: 9pt; color: #9CC3CE; margin-top: 1.5mm; }
.cover-pub { float: right; text-align: right; font-family: 'Manrope'; font-size: 8pt; color: #7FB6C4; letter-spacing: 0.18em; text-transform: uppercase; }

/* ---------- FRONT MATTER ---------- */
.halftitle { text-align: left; padding-top: 60mm; }
.halftitle h1 { font-family: 'Manrope'; font-weight: 800; font-size: 22pt; color: var(--teal); }

.titlepage { padding-top: 30mm; }
.titlepage .tp-rule { width: 32mm; height: 2.5pt; background: var(--teal); margin-bottom: 10mm; }
.titlepage h1 { font-family: 'Manrope'; font-weight: 800; font-size: 27pt; line-height: 1.1; color: var(--ink); margin: 0; }
.titlepage h2 { font-family: 'Spectral'; font-style: italic; font-weight: 400; font-size: 13pt; color: var(--muted); margin: 8mm 0 0 0; }
.titlepage .tp-meta { margin-top: 28mm; font-family: 'Manrope'; font-size: 10pt; }
.titlepage .tp-author { font-weight: 800; font-size: 14pt; color: var(--teal); }
.titlepage .tp-affil { color: var(--muted); margin-top: 2mm; }
.titlepage .tp-publisher { position: relative; margin-top: 55mm; border-top: 1px solid var(--rule); padding-top: 5mm; font-family: 'Manrope'; font-size: 8.5pt; letter-spacing: 0.16em; text-transform: uppercase; color: var(--muted); }

.copyrightpage { font-size: 8.6pt; color: #333; padding-top: 8mm; }
.copyrightpage p { margin: 0 0 3.2mm 0; }
.copyrightpage .isbn { font-family: 'Manrope'; font-weight: 600; font-size: 10pt; color: var(--ink); }

h1.fm-title { font-family: 'Manrope'; font-weight: 800; font-size: 19pt; color: var(--teal); margin: 0 0 8mm 0; letter-spacing: -0.01em; }
h1.fm-title::after { content: ''; display: block; width: 22mm; height: 2pt; background: var(--teal); margin-top: 3mm; }

/* ---------- TOC ---------- */
.toc a { color: var(--ink); text-decoration: none; }
.toc-part { font-family: 'Manrope'; font-weight: 800; font-size: 10.5pt; text-transform: uppercase; letter-spacing: 0.12em; color: var(--teal); margin: 7mm 0 2.5mm 0; }
.toc-entry { display: block; font-family: 'Spectral'; font-size: 10.3pt; margin: 0 0 2mm 0; }
.toc-entry a::after { content: leader('.') ' ' target-counter(attr(href), page); font-family: 'Manrope'; font-weight: 600; font-size: 8.6pt; color: var(--teal); }
.toc-entry .toc-chnum { display: inline-block; min-width: 9mm; font-family: 'Manrope'; font-weight: 800; font-size: 9pt; color: var(--muted); }
.toc-entry.frontm a::after { content: leader('.') ' ' target-counter(attr(href), page, lower-roman); }
.toc-sub { display: block; font-size: 9pt; color: var(--muted); margin: 0 0 1.4mm 12mm; }
.toc-status { font-family: 'Manrope'; font-weight: 600; font-size: 6.6pt; letter-spacing: 0.08em; text-transform: uppercase; padding: 0.5mm 2mm; border: 0.7pt solid var(--amber); color: var(--amber); margin-left: 2.5mm; }

/* ---------- LISTS OF FIGURES/TABLES/ABBREV ---------- */
.lof-entry { font-size: 9.4pt; margin-bottom: 1.8mm; }
.lof-entry .lof-num { font-family: 'Manrope'; font-weight: 600; color: var(--teal); display: inline-block; min-width: 16mm; }
table.abbr { width: 100%; border-collapse: collapse; font-size: 9.2pt; }
table.abbr td { padding: 1.3mm 2mm; border-bottom: 0.5pt solid #E3EBEE; vertical-align: top; }
table.abbr td:first-child { font-family: 'Manrope'; font-weight: 600; color: var(--teal); width: 30mm; }

/* ---------- PART DIVIDERS ---------- */
.part-divider { width: 210mm; height: 296mm; background: var(--teal-deep); color: #fff; position: relative; }
.pd-inner { position: absolute; top: 0; left: 0; padding: 30mm 24mm; width: 210mm; height: 297mm; }
.pd-num { font-family: 'Manrope'; font-weight: 800; font-size: 64pt; color: #1C5A6B; line-height: 1; }
.pd-label { font-family: 'Manrope'; font-weight: 600; font-size: 9pt; letter-spacing: 0.34em; text-transform: uppercase; color: #7FB6C4; margin-top: 4mm; }
.pd-title { font-family: 'Manrope'; font-weight: 800; font-size: 26pt; color: #fff; margin-top: 6mm; line-height: 1.15; max-width: 150mm; }
.pd-chapters { margin-top: 16mm; border-top: 1px solid #2C6B7C; padding-top: 8mm; }
.pd-ch { font-family: 'Spectral'; font-size: 11pt; color: #BCD9E1; margin-bottom: 4mm; }
.pd-ch .n { font-family: 'Manrope'; font-weight: 800; color: #8FD6E8; display: inline-block; min-width: 14mm; }

/* ---------- CHAPTER OPENER ---------- */
.chapter { string-set: chaptertitle attr(data-running); }
.ch-opener { border-bottom: 2.5pt solid var(--teal); padding-bottom: 7mm; margin-bottom: 8mm; }
.ch-kicker { font-family: 'Manrope'; font-weight: 600; font-size: 8pt; letter-spacing: 0.3em; text-transform: uppercase; color: var(--muted); }
.ch-band { display: table; width: 100%; margin-top: 4mm; }
.ch-num-cell { display: table-cell; width: 26mm; vertical-align: top; }
.ch-num { font-family: 'Manrope'; font-weight: 800; font-size: 46pt; color: var(--teal-soft); -weasy-text-stroke: 0; line-height: 0.9; color: #CFE1E6; }
.ch-title-cell { display: table-cell; vertical-align: middle; padding-left: 5mm; border-left: 1pt solid var(--rule); }
h1.ch-title { font-family: 'Manrope'; font-weight: 800; font-size: 21pt; line-height: 1.14; color: var(--ink); margin: 0; bookmark-level: 1; }
.ch-tagline { font-family: 'Spectral'; font-style: italic; font-size: 10.5pt; color: var(--muted); margin-top: 3mm; }

.objectives-box { background: var(--teal-soft); border-left: 3pt solid var(--teal); padding: 5mm 6mm; margin: 6mm 0 7mm 0; break-inside: avoid; }
.objectives-box h3 { font-family: 'Manrope'; font-weight: 800; font-size: 9.5pt; letter-spacing: 0.12em; text-transform: uppercase; color: var(--teal); margin: 0 0 3mm 0; }
.objectives-box ol { margin: 0; padding-left: 5.5mm; font-size: 9.4pt; }
.objectives-box li { margin-bottom: 1.6mm; }
.objectives-box .lo-tag { font-family: 'Manrope'; font-weight: 600; font-size: 7pt; color: #fff; background: var(--teal); padding: 0.3mm 1.8mm; margin-left: 2mm; white-space: nowrap; }

table.co-map { width: 100%; border-collapse: collapse; font-size: 8.4pt; margin: 4mm 0 2mm 0; }
table.co-map th { font-family: 'Manrope'; font-weight: 600; font-size: 7.6pt; text-transform: uppercase; letter-spacing: 0.06em; background: var(--teal); color: #fff; padding: 1.8mm 2.5mm; text-align: left; }
table.co-map td { padding: 1.6mm 2.5mm; border-bottom: 0.5pt solid var(--rule); vertical-align: top; }

/* ---------- BODY TYPOGRAPHY ---------- */
h2.sec { font-family: 'Manrope'; font-weight: 800; font-size: 13.5pt; color: var(--teal); margin: 8mm 0 3.5mm 0; bookmark-level: 2; break-after: avoid; }
h2.sec .secnum { color: #9BB6BE; margin-right: 2.5mm; }
h3.subsec { font-family: 'Manrope'; font-weight: 600; font-size: 10.8pt; color: var(--ink); margin: 5.5mm 0 2.5mm 0; bookmark-level: 3; break-after: avoid; }
h4.minisec { font-family: 'Manrope'; font-weight: 600; font-size: 9.6pt; color: var(--blue); margin: 4mm 0 2mm 0; break-after: avoid; }
p { margin: 0 0 3.2mm 0; text-align: justify; hyphens: auto; }
p.lead { font-size: 11pt; color: #2A363C; }
ul, ol { margin: 0 0 3.5mm 0; padding-left: 6mm; }
li { margin-bottom: 1.4mm; text-align: justify; }
strong { font-weight: 600; }
.wframe { font-family: 'Manrope'; font-weight: 800; font-size: 8pt; letter-spacing: 0.1em; text-transform: uppercase; color: #fff; background: var(--blue); display: inline-block; padding: 0.8mm 2.8mm; margin: 3mm 0 2mm 0; }

/* ---------- FIGURES ---------- */
.figure { margin: 5mm 0 6mm 0; break-inside: avoid; text-align: center; }
.figure svg { max-width: 100%; }
.figure img { max-width: 86%; height: auto; border: 0.5pt solid var(--rule); }
.figcaption { font-family: 'Manrope'; font-size: 8.4pt; color: var(--muted); text-align: left; margin-top: 2.5mm; border-top: 0.6pt solid var(--rule); padding-top: 1.8mm; }
.figcaption b { font-weight: 800; color: var(--teal); }

/* ---------- KEYWORDS & ROADMAP ---------- */
.kwline { font-family: 'Manrope'; font-size: 8.8pt; color: #2A363C; margin: 3mm 0; border-left: 2pt solid var(--amber); padding-left: 3.5mm; }
.kwlab { font-weight: 800; font-size: 7.6pt; letter-spacing: 0.14em; text-transform: uppercase; color: var(--amber); margin-right: 2.5mm; }
.roadmap { margin: 3mm 0 5mm 0; }
.roadmap .kwlab { color: var(--blue); display: block; margin-bottom: 1.6mm; }
.rm-chip { display: inline-block; font-family: 'Manrope'; font-size: 7.8pt; color: var(--blue); border: 0.6pt solid #C4D4E2; background: #F4F8FB; padding: 0.8mm 2.6mm; margin: 0 1.4mm 1.4mm 0; }
.gl-ch { font-family: 'Manrope'; font-size: 7.4pt; color: var(--muted); }
.callout table.data { font-size: 8pt; margin: 2mm 0; }
.case-study table.data { font-size: 8pt; margin: 2mm 0; }

/* ---------- TABLES ---------- */
.tablewrap { margin: 5mm 0 6mm 0; break-inside: avoid; }
.tabcaption { font-family: 'Manrope'; font-size: 8.4pt; color: var(--muted); margin-bottom: 2mm; }
.tabcaption b { font-weight: 800; color: var(--teal); }
table.data { width: 100%; border-collapse: collapse; font-size: 8.7pt; }
table.data th { font-family: 'Manrope'; font-weight: 600; font-size: 8pt; background: var(--teal); color: #fff; padding: 2mm 2.5mm; text-align: left; }
table.data td { padding: 1.8mm 2.5mm; border-bottom: 0.5pt solid var(--rule); vertical-align: top; }
table.data tr:nth-child(even) td { background: #F3F8F9; }
table.data td.rowhead { font-family: 'Manrope'; font-weight: 600; color: var(--teal); }

/* ---------- CALLOUT BOXES ---------- */
.callout { border: 0.8pt solid; padding: 4mm 5mm; margin: 5mm 0; break-inside: avoid; font-size: 9.3pt; }
.callout .co-head { font-family: 'Manrope'; font-weight: 800; font-size: 8.4pt; letter-spacing: 0.14em; text-transform: uppercase; margin: 0 0 2.2mm 0; }
.callout p:last-child { margin-bottom: 0; }
.callout.regulatory { border-color: var(--teal); background: #F0F7F8; }
.callout.regulatory .co-head { color: var(--teal); }
.callout.clinical { border-color: var(--green); background: #F0F7F2; }
.callout.clinical .co-head { color: var(--green); }
.callout.industry { border-color: var(--blue); background: #F0F5FA; }
.callout.industry .co-head { color: var(--blue); }
.callout.didyouknow { border-color: var(--amber); background: #FBF5EC; }
.callout.didyouknow .co-head { color: var(--amber); }

/* ---------- CASE STUDY ---------- */
.case-study { border: 1pt solid var(--plum); margin: 6mm 0; break-inside: avoid; }
.case-study .cs-head { background: var(--plum); color: #fff; font-family: 'Manrope'; font-weight: 800; font-size: 9pt; letter-spacing: 0.1em; text-transform: uppercase; padding: 2.4mm 5mm; }
.case-study .cs-body { padding: 4mm 5mm; font-size: 9.3pt; }
.case-study .cs-q { font-family: 'Manrope'; font-weight: 600; font-size: 8.6pt; color: var(--plum); margin-top: 3mm; }
.case-study .cs-analysis { border-top: 0.6pt dashed var(--plum); margin-top: 3mm; padding-top: 3mm; }

/* ---------- SUMMARY & KEY TERMS ---------- */
.summary-box { background: #F6F9FA; border-top: 2pt solid var(--teal); border-bottom: 2pt solid var(--teal); padding: 5mm 6mm; margin: 7mm 0; }
.summary-box h3 { font-family: 'Manrope'; font-weight: 800; font-size: 10.5pt; text-transform: uppercase; letter-spacing: 0.12em; color: var(--teal); margin: 0 0 3mm 0; }
.summary-box ul { font-size: 9.3pt; margin-bottom: 0; }
.keyterms { margin: 5mm 0; }
.keyterms h3 { font-family: 'Manrope'; font-weight: 800; font-size: 10.5pt; text-transform: uppercase; letter-spacing: 0.12em; color: var(--teal); margin: 0 0 3mm 0; }
.keyterms dl { font-size: 9.1pt; margin: 0; }
.keyterms dt { font-family: 'Manrope'; font-weight: 600; color: var(--ink); display: inline; }
.keyterms dd { display: inline; margin: 0; color: #333; }
.keyterms .kt-row { margin-bottom: 1.8mm; }

/* ---------- ASSESSMENTS ---------- */
.assessment { border-top: 2.5pt solid var(--teal); margin-top: 8mm; padding-top: 4mm; }
.assessment > h2 { font-family: 'Manrope'; font-weight: 800; font-size: 14pt; color: var(--teal); margin: 0 0 4mm 0; bookmark-level: 2; }
.ass-block { margin-bottom: 6mm; }
.ass-block h3 { font-family: 'Manrope'; font-weight: 800; font-size: 9.6pt; letter-spacing: 0.08em; text-transform: uppercase; color: #fff; background: var(--teal); display: inline-block; padding: 1.2mm 3.5mm; margin: 0 0 3mm 0; }
.ass-block ol { font-size: 9.2pt; }
.mcq-opts { list-style: none; padding-left: 2mm; margin: 1mm 0 1.5mm 0; }
.mcq-opts li { display: inline-block; margin-right: 6mm; margin-bottom: 0.6mm; }
.mcq-opts .ol { font-family: 'Manrope'; font-weight: 600; color: var(--teal); }
.rationale { font-size: 8.4pt; color: var(--muted); border-left: 1.5pt solid var(--rule); padding-left: 3mm; margin: 1mm 0 2.5mm 0; }
.rationale b { color: var(--green); font-family: 'Manrope'; }
.ar-key { font-size: 8.6pt; color: var(--muted); font-style: italic; margin-bottom: 3mm; }
.marks { font-family: 'Manrope'; font-size: 7.6pt; color: var(--muted); }

/* ---------- REFERENCES ---------- */
.references { margin-top: 7mm; border-top: 1pt solid var(--rule); padding-top: 4mm; }
.references h2 { font-family: 'Manrope'; font-weight: 800; font-size: 12pt; color: var(--teal); margin: 0 0 3mm 0; bookmark-level: 2; }
.references ol { font-size: 8.6pt; color: #333; padding-left: 6mm; }
.references li { margin-bottom: 1.8mm; text-align: left; }

/* ---------- QUALITY GATE DASHBOARD ---------- */
.qgate { margin-top: 7mm; break-inside: avoid; }
.qgate h2 { font-family: 'Manrope'; font-weight: 800; font-size: 11pt; color: var(--teal-deep); margin: 0 0 3mm 0; bookmark-level: 2; }
table.qgate-t { width: 100%; border-collapse: collapse; font-size: 8.4pt; }
table.qgate-t th { font-family: 'Manrope'; font-weight: 600; font-size: 7.6pt; text-transform: uppercase; background: var(--teal-deep); color: #fff; padding: 1.8mm 2.5mm; text-align: left; }
table.qgate-t td { padding: 1.5mm 2.5mm; border-bottom: 0.5pt solid var(--rule); }
.qg-pass { font-family: 'Manrope'; font-weight: 800; color: var(--green); }

/* ---------- STUB (IN DEVELOPMENT) PAGES ---------- */
.stub-page .status-pill { font-family: 'Manrope'; font-weight: 800; font-size: 8pt; letter-spacing: 0.14em; text-transform: uppercase; color: var(--amber); border: 1pt solid var(--amber); display: inline-block; padding: 1.5mm 4mm; margin: 4mm 0; }
.stub-scope { border: 0.8pt dashed var(--rule); padding: 4mm 5mm; margin-top: 4mm; }
.stub-scope h3 { font-family: 'Manrope'; font-weight: 800; font-size: 9pt; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); margin: 0 0 2.5mm 0; }
.stub-scope ul { font-size: 9.3pt; margin-bottom: 0; }

/* ---------- BACK MATTER ---------- */
.backmatter-section h1 { string-set: chaptertitle content(); }
.glossary dl { font-size: 9.1pt; }
.glossary dt { font-family: 'Manrope'; font-weight: 600; }
.glossary dd { margin: 0 0 2.2mm 0; }
table.stdindex { width: 100%; border-collapse: collapse; font-size: 8.8pt; }
table.stdindex th { font-family: 'Manrope'; font-weight: 600; font-size: 8pt; background: var(--teal); color: #fff; padding: 1.8mm 2.5mm; text-align: left; }
table.stdindex td { padding: 1.6mm 2.5mm; border-bottom: 0.5pt solid var(--rule); }
.akey { font-size: 9pt; }
.akey h3 { font-family: 'Manrope'; font-weight: 800; font-size: 10pt; color: var(--teal); margin: 4mm 0 2mm 0; }
.akey p { text-align: left; }
"""

PREVIEW_EXTRA_CSS = """
body { background: #47555C; padding: 24px 0; }
.sheet { width: 210mm; min-height: 297mm; margin: 0 auto 24px auto; background: #fff; box-shadow: 0 2px 14px rgba(0,0,0,0.35); padding: 20mm 18mm; }
.sheet.dark { background: #093542; }
.cover-page, .part-divider { width: 100%; height: 297mm; }
.cover-inner, .pd-inner { position: relative; width: auto; height: auto; padding: 22mm 18mm; }
.cover-author-block { position: relative; bottom: auto; left: auto; right: auto; margin-top: 30mm; }
@media screen { .toc-entry a::after { content: '  ·  p.—'; color: #9BB6BE; } }
"""
