BOOK_META = {
    "title": "Medical Devices",
    "subtitle": "A Comprehensive Textbook for Pharmacy and Allied Health Sciences",
    "edition": "First Edition",
    "author": "Author Name",
    "affiliation": "Department of Pharmaceutics, Institution Name",
    "publisher": "Emergent Academic Press",
    "year": "2026",
    "isbn": "ISBN 978-X-XXXXX-XXX-X (placeholder — assigned on registration)",
    "syllabus_anchor": "PCI NEP 2020 B.Pharm — BP708T (Medical Devices, Elective)",
    "series": "Medical Devices Academic Ecosystem · Core Textbook",
}

PARTS = [
    {"num": "I", "title": "Foundations", "chapters": [1, 2]},
    {"num": "II", "title": "Design, Biomaterials & Biocompatibility", "chapters": [3, 4, 5]},
    {"num": "III", "title": "Manufacturing, Quality & Safety", "chapters": [6, 7, 8, 9, 10]},
    {"num": "IV", "title": "Regulatory & Post-Market", "chapters": [11, 12]},
    {"num": "V", "title": "Practice & Careers", "chapters": [13, 14]},
]

CHAPTERS = [
    {"num": 1, "id": "ch01", "title": "Introduction to Medical Devices", "status": "complete", "phase": 2,
     "sections": ["What is a medical device?", "A brief history of medical devices", "The global medical device industry", "The Indian medical device sector", "National Medical Device Policy 2023", "Government of India initiatives"]},
    {"num": 2, "id": "ch02", "title": "Definitions & Classification of Medical Devices", "status": "complete", "phase": 2,
     "sections": ["Legal definitions across jurisdictions", "Risk-based classification: the universal logic", "India — CDSCO MDR 2017 (Class A–D)", "United States — US FDA (Class I–III)", "European Union — EU MDR & CE marking", "IMDRF and global harmonization"]},
    {"num": 3, "id": "ch03", "title": "Medical Device Design & Development Process", "status": "planned", "phase": 3,
     "sections": ["The device lifecycle", "Design controls (21 CFR 820.30)", "User needs & design inputs", "Verification vs validation", "Safety analysis & human factors"]},
    {"num": 4, "id": "ch04", "title": "Biomaterials", "status": "planned", "phase": 3,
     "sections": ["Classes of biomaterials", "Structure–property relationships", "Material selection for devices", "Tissue engineering & regenerative medicine"]},
    {"num": 5, "id": "ch05", "title": "Biocompatibility", "status": "planned", "phase": 3,
     "sections": ["Host response to materials", "ISO 10993 family overview", "Biological evaluation planning", "Test selection by contact & duration"]},
    {"num": 6, "id": "ch06", "title": "Manufacturing Technologies & Workflows", "status": "planned", "phase": 4,
     "sections": ["Cleanroom manufacturing", "Molding, machining, additive manufacturing", "Process validation (IQ/OQ/PQ)", "Industry 4.0 in medtech"]},
    {"num": 7, "id": "ch07", "title": "Quality Management Systems — ISO 13485", "status": "planned", "phase": 4,
     "sections": ["QMS principles", "ISO 13485:2016 clause map", "Document & record control", "CAPA and internal audit"]},
    {"num": 8, "id": "ch08", "title": "Risk Management — ISO 14971", "status": "planned", "phase": 4,
     "sections": ["Risk management process", "Hazard identification & risk analysis", "Risk evaluation & control", "Production and post-production feedback"]},
    {"num": 9, "id": "ch09", "title": "Electrical Safety & Essential Performance — IEC 60601", "status": "planned", "phase": 4,
     "sections": ["The IEC 60601 series", "Basic safety & essential performance", "Applied parts and leakage currents", "EMC and collateral standards"]},
    {"num": 10, "id": "ch10", "title": "Sterilization, Packaging & Labeling", "status": "planned", "phase": 4,
     "sections": ["Sterilization modalities (EO, steam, radiation)", "Sterility assurance level", "Sterile barrier systems (ISO 11607)", "Labeling & UDI"]},
    {"num": 11, "id": "ch11", "title": "Licensing & Conformity Assessment Pathways", "status": "planned", "phase": 5,
     "sections": ["India — MDR 2017 licence forms & authorities", "US FDA 510(k), De Novo, PMA", "EU CE marking & notified bodies", "Pathway comparison"]},
    {"num": 12, "id": "ch12", "title": "Clinical Evaluation, PMS & Materiovigilance (MvPI)", "status": "planned", "phase": 5,
     "sections": ["Clinical investigation & evaluation", "Post-market surveillance systems", "Materiovigilance Programme of India", "Adverse event reporting & recalls"]},
    {"num": 13, "id": "ch13", "title": "Major Device Categories", "status": "planned", "phase": 5,
     "sections": ["In vitro diagnostics", "Implants & prosthetics", "Drug–device combinations", "Wearables & SaMD"]},
    {"num": 14, "id": "ch14", "title": "The Pharmacist's Role, Entrepreneurship, IP & Careers", "status": "planned", "phase": 5,
     "sections": ["Pharmacists across the device lifecycle", "Entrepreneurship & start-up pathways", "Intellectual property basics", "Career maps & NSQF/LSSSDC touchpoints"]},
]

PHASES = [
    {"num": 1, "title": "Design system + book skeleton", "detail": "Cover, front matter, TOC, chapter template, A4 PDF pipeline", "status": "complete"},
    {"num": 2, "title": "Part I authored (Ch 1–2)", "detail": "Reviewed against Quality Gate", "status": "complete"},
    {"num": 3, "title": "Part II (Ch 3–5)", "detail": "Design, biomaterials, biocompatibility", "status": "pending"},
    {"num": 4, "title": "Part III (Ch 6–10)", "detail": "Manufacturing, quality & safety", "status": "pending"},
    {"num": 5, "title": "Part IV–V (Ch 11–14)", "detail": "Regulatory, post-market, practice & careers", "status": "pending"},
    {"num": 6, "title": "Back matter & final typeset", "detail": "Glossary, references, consistency pass, final A4 PDF", "status": "pending"},
]

FIGURES = [
    ("1.1", "Milestones in the history of medical devices (1816–present)"),
    ("1.2", "Structure of the global medical device market by major segment"),
    ("1.3", "The Indian medical device ecosystem: actors and flows"),
    ("1.4", "The six strategy pillars of the National Medical Device Policy, 2023"),
    ("2.1", "The risk-based classification pyramid under CDSCO MDR 2017 (Class A–D)"),
    ("2.2", "US FDA device classification and pathway decision flow"),
    ("2.3", "EU CE marking conformity assessment route by device class"),
    ("2.4", "From GHTF to IMDRF: the harmonization timeline"),
]

TABLES = [
    ("1.1", "Selected landmark medical devices and their public health impact"),
    ("1.2", "Leading global medical device markets and characteristics"),
    ("1.3", "Segment profile of the Indian medical device industry"),
    ("1.4", "Key Government of India initiatives for the medical device sector"),
    ("2.1", "Definitional elements of a medical device across jurisdictions"),
    ("2.2", "CDSCO MDR 2017 device classes with examples and licensing authority"),
    ("2.3", "US FDA device classes, controls and typical pathways"),
    ("2.4", "EU MDR classes and conformity assessment requirements"),
    ("2.5", "Side-by-side comparison: India vs USA vs EU classification"),
]


def part_divider_html(part):
    chapters = [c for c in CHAPTERS if c["num"] in part["chapters"]]
    ch_rows = "".join(
        '<div class="pd-ch"><span class="n">%02d</span> %s</div>' % (c["num"], c["title"])
        for c in chapters
    )
    return """
<section class="part-divider" id="part%s">
  <div class="pd-inner">
    <div class="pd-num">%s</div>
    <div class="pd-label">Part %s</div>
    <div class="pd-title">%s</div>
    <div class="pd-chapters">%s</div>
  </div>
</section>""" % (part["num"], part["num"], part["num"], part["title"], ch_rows)


def stub_chapter_html(ch):
    secs = "".join("<li>%s</li>" % s for s in ch["sections"])
    return """
<section class="chapter stub-page" id="%s" data-running="Chapter %d · %s">
  <div class="ch-opener">
    <div class="ch-kicker">Chapter %d</div>
    <div class="ch-band">
      <div class="ch-num-cell"><div class="ch-num">%02d</div></div>
      <div class="ch-title-cell">
        <h1 class="ch-title">%s</h1>
        <div class="ch-tagline">Scheduled for authoring in Phase %d of the production plan.</div>
      </div>
    </div>
  </div>
  <span class="status-pill">In Development — Phase %d</span>
  <p>This chapter is part of the approved book architecture and will be authored to the full
  Master Prompt v5.4 chapter template: learning objectives with CO/Bloom's mapping, the
  What–Why–How–Where–When content framework, figures and comparison tables, callout boxes,
  case studies, a complete assessment battery, Vancouver-style references, and a Quality Gate
  completion dashboard.</p>
  <div class="stub-scope">
    <h3>Planned Scope</h3>
    <ul>%s</ul>
  </div>
</section>""" % (ch["id"], ch["num"], ch["title"], ch["num"], ch["num"], ch["title"], ch["phase"], ch["phase"], secs)
