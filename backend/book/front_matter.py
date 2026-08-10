from .outline import BOOK_META, PARTS, CHAPTERS, FIGURES, TABLES


def cover_html():
    return """
<section class="cover-page" id="cover">
  <svg class="cover-grid-lines" viewBox="0 0 210 297" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="210" height="297" fill="#093542"/>
    <g stroke="#0F4C5C" stroke-width="0.25">
      <line x1="0" y1="74" x2="210" y2="74"/><line x1="0" y1="148" x2="210" y2="148"/>
      <line x1="0" y1="222" x2="210" y2="222"/><line x1="52" y1="0" x2="52" y2="297"/>
      <line x1="105" y1="0" x2="105" y2="297"/><line x1="158" y1="0" x2="158" y2="297"/>
    </g>
    <g transform="translate(118,168)">
      <circle cx="46" cy="46" r="42" fill="none" stroke="#1C5A6B" stroke-width="0.8"/>
      <polyline points="4,46 22,46 30,26 40,66 48,36 54,52 60,46 88,46" fill="none" stroke="#8FD6E8" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
      <circle cx="46" cy="46" r="52" fill="none" stroke="#1C5A6B" stroke-width="0.4" stroke-dasharray="2 3"/>
    </g>
  </svg>
  <div class="cover-inner">
    <span class="cover-series">Medical Devices Academic Ecosystem &middot; Core Textbook</span>
    <div class="cover-title">MEDICAL<br/>DEVICES<span class="accent">.</span></div>
    <div class="cover-subtitle">A Comprehensive Textbook for Pharmacy and Allied Health Sciences &mdash; from device history and classification to regulation, quality and practice.</div>
    <div class="cover-badges">
      <span class="cover-badge">PCI NEP 2020 Aligned</span>
      <span class="cover-badge">BP708T &middot; Medical Devices</span>
      <span class="cover-badge">A4 Print Edition</span>
    </div>
    <div class="cover-author-block">
      <div class="cover-pub">Emergent Academic Press<br/>First Edition &middot; 2026</div>
      <div class="cover-author">%(author)s</div>
      <div class="cover-affil">%(affiliation)s</div>
    </div>
  </div>
</section>""" % BOOK_META


def halftitle_html():
    return """
<section class="front-section halftitle" id="halftitle">
  <h1>Medical Devices</h1>
  <p style="font-family:'Spectral';font-style:italic;color:#5B6770;">A Comprehensive Textbook for Pharmacy and Allied Health Sciences</p>
</section>"""


def titlepage_html():
    return """
<section class="front-section titlepage" id="titlepage">
  <div class="tp-rule"></div>
  <h1>Medical Devices</h1>
  <h2>A Comprehensive Textbook for Pharmacy and Allied Health Sciences</h2>
  <div class="tp-meta">
    <div class="tp-author">%(author)s</div>
    <div class="tp-affil">%(affiliation)s</div>
  </div>
  <div class="tp-meta" style="margin-top:14mm;">
    <div style="font-weight:600;">%(edition)s</div>
    <div style="color:#5B6770;margin-top:1.5mm;">Aligned to %(syllabus_anchor)s</div>
  </div>
  <div class="tp-publisher">%(publisher)s &middot; %(year)s</div>
</section>""" % BOOK_META


def copyright_html():
    return """
<section class="front-section copyrightpage" id="copyright">
  <p><strong>Medical Devices: A Comprehensive Textbook for Pharmacy and Allied Health Sciences</strong><br/>%(edition)s, %(year)s</p>
  <p>&copy; %(year)s %(author)s. All rights reserved.</p>
  <p class="isbn">%(isbn)s</p>
  <p>No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any
  form or by any means &mdash; electronic, mechanical, photocopying, recording or otherwise &mdash; without the
  prior written permission of the publisher, except for brief quotations in reviews or scholarly analysis.</p>
  <p><strong>Notice.</strong> Medical device regulation, standards and clinical practice evolve continuously. The author
  and publisher have taken care to verify regulatory citations (CDSCO, US FDA, European Commission, ISO, IEC, WHO)
  against official sources current at the time of writing. Readers must consult the latest official texts of the
  Medical Devices Rules 2017, applicable FDA regulations, EU Regulation (EU) 2017/745, and referenced standards
  before acting on any regulatory matter. This book is an educational work and does not constitute regulatory or
  clinical advice.</p>
  <p><strong>Trademarks.</strong> All product names, standards designations and organizational marks referenced are the
  property of their respective owners and are used solely for identification and educational purposes.</p>
  <p>Typeset in Spectral and Manrope. Designed and typeset digitally for A4 print and digital distribution.<br/>
  Published by %(publisher)s.</p>
  <p style="margin-top:8mm;">10&nbsp;&nbsp;9&nbsp;&nbsp;8&nbsp;&nbsp;7&nbsp;&nbsp;6&nbsp;&nbsp;5&nbsp;&nbsp;4&nbsp;&nbsp;3&nbsp;&nbsp;2&nbsp;&nbsp;1</p>
</section>""" % BOOK_META


def preface_html():
    return """
<section class="front-section" id="preface">
  <h1 class="fm-title">Preface</h1>
  <p class="lead">Medical devices touch a patient's life at nearly every point of care &mdash; a thermometer at triage,
  a stent in the cath-lab, a glucose sensor worn on the arm, software that reads a retinal scan. Yet for
  decades, pharmacy education treated devices as a footnote to medicines. That era is over.</p>
  <p>With the Medical Devices Rules 2017, India brought devices under a modern, risk-based regulatory
  system; with the National Medical Device Policy 2023, it declared the sector a national priority; and with
  the NEP 2020-aligned PCI curriculum, <strong>Medical Devices (BP708T)</strong> entered the B.Pharm classroom as a
  dedicated elective. This textbook was written to serve that course &mdash; and to go beyond it.</p>
  <p>Three convictions shaped this book:</p>
  <ul>
    <li><strong>Devices deserve rigour.</strong> Every chapter follows a disciplined architecture &mdash; chapter learning
    outcomes, keywords and a roadmap up front; figures, tables, worked example boxes, case studies and
    industry insights through the body; and a chapter glossary, quick recap and references to close.</li>
    <li><strong>Regulation must be exact.</strong> Classifications, rule numbers, licence forms and standards cited here
    are drawn from official CDSCO, US FDA, European Commission, ISO, IEC and WHO sources. Where a fact
    could not be verified, it was omitted rather than invented.</li>
    <li><strong>Students learn from stories.</strong> Case studies and industry insights
    show why device law and practice look the way they do, and connect each concept to the clinic,
    the factory floor and the regulator's desk.</li>
  </ul>
  <p>The journey runs across six parts and twenty chapters. Part I builds the foundation &mdash; the device
  universe, the structure of the industry, and the classification logic that underpins every regulatory
  decision worldwide. Parts II and III follow the device from lifecycle and quality systems through
  cleanrooms, materials, biocompatibility and design. Part IV covers manufacturing and quality control;
  Part V the regulatory, clinical, post-market, labeling and supply-chain landscape &mdash; including Software
  as a Medical Device and AI/ML regulation. Part VI looks forward: emerging technologies, healthcare data
  and interoperability, and the career pathways that await you in this sector.</p>
  <p>I hope this book makes the device world as intellectually alive for you as it has become for the
  pharmacists, engineers and regulators who build it every day.</p>
  <p style="margin-top:8mm;text-align:left;"><strong>%(author)s</strong><br/><span style="color:#5B6770;">%(affiliation)s &middot; %(year)s</span></p>
</section>""" % BOOK_META


def howto_html():
    return """
<section class="front-section" id="howto">
  <h1 class="fm-title">How to Use This Book</h1>
  <p>Every chapter follows the same architecture, so you always know where you are and what comes next.</p>
  <div class="tablewrap">
  <table class="data">
    <tr><th style="width:38mm;">Element</th><th>What it gives you</th></tr>
    <tr><td class="rowhead">Chapter opener</td><td>Chapter Learning Outcomes (CLOs), keywords and a chapter roadmap, so you can see exactly what you should be able to do after studying and how the chapter unfolds.</td></tr>
    <tr><td class="rowhead">Figures &amp; tables</td><td>Numbered illustrations, flowcharts and comparison tables. Cite them in exams as &ldquo;Fig. 3.2&rdquo; style.</td></tr>
    <tr><td class="rowhead">Example boxes</td><td>Worked examples and applied comparisons that turn definitions into practice.</td></tr>
    <tr><td class="rowhead">Case studies</td><td>Real events and devices with regulatory analysis &mdash; ideal for tutorials and viva preparation.</td></tr>
    <tr><td class="rowhead">Industry insights</td><td>Market, policy and career context connecting each topic to the working world of medical devices.</td></tr>
    <tr><td class="rowhead">Chapter glossary</td><td>The chapter's key terms defined in place, consolidated again in the back-matter glossary.</td></tr>
    <tr><td class="rowhead">Quick recap</td><td>A closing summary of the chapter's essential takeaways for rapid revision.</td></tr>
    <tr><td class="rowhead">References</td><td>Regulatory documents, international standards and technical publications backing the chapter.</td></tr>
  </table></div>
  <h3 class="subsec">Suggested study workflow</h3>
  <ol>
    <li>Read the chapter learning outcomes first; they are your examination contract.</li>
    <li>Work through the narrative once without stopping, then a second time making margin notes on figures and tables.</li>
    <li>Close each chapter by writing your own recap before reading the Quick Recap &mdash; then compare.</li>
    <li>Use case studies and industry insights for group discussion and viva practice.</li>
  </ol>
  <div class="callout regulatory">
    <div class="co-head">Regulatory Spotlight</div>
    <p>Wherever a rule, form number or standard is cited (e.g., &ldquo;Form MD-5&rdquo;, &ldquo;ISO 13485:2016&rdquo;),
    it has been checked against the official source listed in the chapter references. Always verify the
    current version before professional use.</p>
  </div>
</section>"""


def syllabus_html():
    return """
<section class="front-section" id="syllabus">
  <h1 class="fm-title">Syllabus Mapping &mdash; PCI BP708T (Medical Devices)</h1>
  <p>The table maps the units of the PCI NEP 2020 B.Pharm elective <strong>BP708T &mdash; Medical Devices</strong> to the
  chapters of this book. Chapters marked &ldquo;beyond syllabus&rdquo; extend coverage to full textbook depth for
  honours study, M.Pharm preparation and industry readiness.</p>
  <div class="tablewrap">
  <table class="data">
    <tr><th style="width:20mm;">Unit</th><th>Syllabus topics</th><th style="width:34mm;">Covered in</th></tr>
    <tr><td class="rowhead">Unit I</td><td>Introduction to medical devices; history and evolution; global and Indian medical device industry; market trends; structure of the industry</td><td>Chapters 1&ndash;2</td></tr>
    <tr><td class="rowhead">Unit II</td><td>Definitions and classification of medical devices &mdash; CDSCO (MDR 2017, Class A&ndash;D), US FDA (Class I&ndash;III), EU MDR/CE marking; global harmonization</td><td>Chapter 3</td></tr>
    <tr><td class="rowhead">Unit III</td><td>Medical device lifecycle, design and development; materials and their selection; biomechanics and biocompatibility</td><td>Chapters 4, 7&ndash;9</td></tr>
    <tr><td class="rowhead">Unit IV</td><td>Quality management systems (ISO 13485); cleanrooms and sterile manufacturing; manufacturing technologies; quality control and testing; packaging, labeling and UDI</td><td>Chapters 5&ndash;6, 10&ndash;11, 16</td></tr>
    <tr><td class="rowhead">Unit V</td><td>Regulatory requirements and pathways; SaMD and digital health; clinical evaluation; post-market surveillance and vigilance; import-export and supply chain; emerging technologies; healthcare data; careers</td><td>Chapters 12&ndash;15, 17&ndash;20</td></tr>
  </table></div>
  <div class="callout industry">
    <div class="co-head">Industry Connect</div>
    <p>Chapters 13 and 18&ndash;20 add Software as a Medical Device and AI/ML regulation, emerging technologies,
    healthcare data and interoperability, and skill-mapped career pathways that exceed the syllabus
    minimum &mdash; the material recruiters and regulatory-affairs interview panels actually probe.</p>
  </div>
</section>"""


def toc_html():
    front_entries = [
        ("preface", "Preface"), ("howto", "How to Use This Book"),
        ("syllabus", "Syllabus Mapping (PCI BP708T)"), ("lists", "Figures, Tables &amp; Abbreviations"),
    ]
    rows = ['<div class="toc-part" style="margin-top:0;">Front Matter</div>']
    for sid, label in front_entries:
        rows.append('<span class="toc-entry frontm"><a href="#%s">%s</a></span>' % (sid, label))
    for part in PARTS:
        rows.append('<div class="toc-part">Part %s &mdash; %s</div>' % (part["num"], part["title"]))
        for ch in CHAPTERS:
            if ch["num"] in part["chapters"]:
                rows.append('<span class="toc-entry"><a href="#%s"><span class="toc-chnum">%d</span>%s</a></span>'
                            % (ch["id"], ch["num"], ch["title"]))
                if ch["sections"]:
                    rows.append('<span class="toc-sub">%s</span>' % " &middot; ".join(ch["sections"][:4]))
    rows.append('<div class="toc-part">Back Matter</div>')
    for sid, label in [("glossary", "Glossary of Key Terms"), ("stdindex", "Standards &amp; Regulations Index"),
                       ("biblio", "Consolidated References")]:
        rows.append('<span class="toc-entry"><a href="#%s">%s</a></span>' % (sid, label))
    return """
<section class="front-section toc" id="toc">
  <h1 class="fm-title">Contents</h1>
  %s
</section>""" % "\n".join(rows)


def lists_html():
    figs = "".join('<div class="lof-entry"><span class="lof-num">Fig. %s</span>%s</div>' % (n, t) for n, t in FIGURES)
    tabs = "".join('<div class="lof-entry"><span class="lof-num">Table %s</span>%s</div>' % (n, t) for n, t in TABLES)
    abbr = [
        ("AI", "Artificial Intelligence"), ("AERB", "Atomic Energy Regulatory Board"),
        ("BIS", "Bureau of Indian Standards"), ("CDSCO", "Central Drugs Standard Control Organisation"),
        ("CE", "Conformit&eacute; Europ&eacute;enne (European conformity marking)"),
        ("CFR", "Code of Federal Regulations (USA)"), ("CLA", "Central Licensing Authority"),
        ("DCGI", "Drugs Controller General of India"), ("EUDAMED", "European Database on Medical Devices"),
        ("FDA", "Food and Drug Administration (USA)"), ("FD&C Act", "Federal Food, Drug, and Cosmetic Act (USA)"),
        ("GHTF", "Global Harmonization Task Force"), ("GMP", "Good Manufacturing Practice"),
        ("IEC", "International Electrotechnical Commission"), ("IMDRF", "International Medical Device Regulators Forum"),
        ("IPC", "Indian Pharmacopoeia Commission"), ("ISO", "International Organization for Standardization"),
        ("IVD", "In Vitro Diagnostic (medical device)"), ("MDR 2017 (India)", "Medical Devices Rules, 2017"),
        ("EU MDR", "Regulation (EU) 2017/745 on medical devices"), ("MvPI", "Materiovigilance Programme of India"),
        ("NIB", "National Institute of Biologicals"), ("NMDP", "National Medical Device Policy, 2023"),
        ("NSQF", "National Skills Qualifications Framework"), ("LSSSDC", "Life Sciences Sector Skill Development Council"),
        ("PLI", "Production Linked Incentive (scheme)"), ("PMA", "Premarket Approval (US FDA)"),
        ("PMS", "Post-Market Surveillance"), ("QMS", "Quality Management System"),
        ("SaMD", "Software as a Medical Device"), ("SLA", "State Licensing Authority"),
        ("UDI", "Unique Device Identification"), ("WHO", "World Health Organization"),
    ]
    abbr_rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (a, b) for a, b in abbr)
    return """
<section class="front-section" id="lists">
  <h1 class="fm-title">List of Figures</h1>
  %s
  <h1 class="fm-title" style="margin-top:10mm;">List of Tables</h1>
  %s
  <h1 class="fm-title" style="margin-top:10mm;">Abbreviations</h1>
  <table class="abbr">%s</table>
</section>""" % (figs, tabs, abbr_rows)
