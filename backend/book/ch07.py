CH07_HTML = """
<section class="chapter" id="ch07" data-running="Chapter 7 · Quality Management Systems — ISO 13485">

<div class="ch-opener">
  <div class="ch-kicker">Part III &middot; Manufacturing, Quality &amp; Safety &middot; Chapter 7</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">07</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Quality Management Systems &mdash; ISO 13485</h1>
      <div class="ch-tagline">QMS principles &middot; the clause map of ISO 13485:2016 &middot; documentation &middot; CAPA and audits &middot; certification and global recognition</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Explain the purpose and principles of a quality management system for medical devices. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Map the clause structure (4&ndash;8) of ISO 13485:2016 to real organisational activities. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Differentiate ISO 13485 from ISO 9001 and state why devices need their own QMS standard. <span class="lo-tag">CO2 &middot; Analyse</span></li>
    <li>Describe the documentation hierarchy: quality manual, procedures, records, medical device file. <span class="lo-tag">CO2 &middot; Understand</span></li>
    <li>Apply CAPA methodology to a quality problem. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Evaluate how ISO 13485 certification anchors market access (EU, MDSAP, India, FDA QMSR). <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Explain QMS purpose and ISO 13485 structure</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Analyse and apply QMS mechanisms (documents, CAPA)</td><td>L3&ndash;L4</td><td>3, 4, 5</td></tr>
    <tr><td>CO3</td><td>Evaluate certification's regulatory leverage</td><td>L5</td><td>6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">7.1</span>Why a QMS &mdash; and Why a Device-Specific One</h2>
<span class="wframe">What &middot; Why</span>
<p class="lead">A quality management system is the organisation's documented nervous system: the structures,
processes, responsibilities and records through which it consistently produces devices that are safe,
effective and compliant. Regulators license <em>systems</em> as much as products, because a sound product from
an unsound system is an accident that has not happened yet.</p>
<p><strong>ISO 13485:2016</strong> &mdash; <em>Medical devices &mdash; Quality management systems &mdash; Requirements for
regulatory purposes</em> &mdash; is the world's device QMS standard. Built on the ISO 9001 architecture, it departs
deliberately: where ISO 9001 pursues customer satisfaction and continual improvement, ISO 13485 pursues
<strong>sustained regulatory compliance and device safety</strong> &mdash; the standard asks organisations to
<em>maintain the effectiveness</em> of the QMS, embeds <strong>risk-based thinking against ISO 14971</strong>, demands
far heavier <strong>documentation</strong>, and adds device-specific machinery: medical device files, sterile-device
clauses, implant traceability, advisory notices and regulatory reporting.</p>
<div class="tablewrap">
<div class="tabcaption"><b>Table 7.1</b> &nbsp;ISO 13485:2016 vs ISO 9001:2015 &mdash; the deliberate differences</div>
<table class="data">
  <tr><th style="width:42mm;">Dimension</th><th>ISO 9001:2015</th><th>ISO 13485:2016</th></tr>
  <tr><td class="rowhead">Primary goal</td><td>Customer satisfaction, continual improvement</td><td>Device safety &amp; sustained regulatory compliance; maintain QMS effectiveness</td></tr>
  <tr><td class="rowhead">Structure</td><td>Annex SL high-level structure</td><td>Retains 2008-style clauses 4&ndash;8 (regulatory stability)</td></tr>
  <tr><td class="rowhead">Documentation</td><td>&ldquo;Documented information&rdquo;, lean</td><td>Quality manual, defined procedures, medical device file &mdash; extensive and prescribed</td></tr>
  <tr><td class="rowhead">Risk</td><td>Risk-based thinking, broad</td><td>Risk management per ISO 14971 across product realization</td></tr>
  <tr><td class="rowhead">Special processes</td><td>Generic</td><td>Explicit validation demands (sterilization, sterile barrier, software)</td></tr>
  <tr><td class="rowhead">Regulatory interface</td><td>None specific</td><td>Reporting to authorities, advisory notices, UDI-ready records</td></tr>
</table>
</div>

<h2 class="sec"><span class="secnum">7.2</span>The Clause Map of ISO 13485:2016</h2>
<span class="wframe">How</span>
<div class="figure">
<svg viewBox="0 0 700 226" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <g font-size="8.8">
    <rect x="18" y="14" width="200" height="52" fill="#0F4C5C"/>
    <text x="118" y="32" text-anchor="middle" fill="#fff" font-weight="bold">Clause 4 &middot; QMS (general)</text>
    <text x="118" y="46" text-anchor="middle" fill="#BCD9E1">Documented QMS &middot; quality manual</text>
    <text x="118" y="58" text-anchor="middle" fill="#BCD9E1">medical device file &middot; control of documents/records</text>
    <rect x="250" y="14" width="200" height="52" fill="#14537D"/>
    <text x="350" y="32" text-anchor="middle" fill="#fff" font-weight="bold">Clause 5 &middot; Management</text>
    <text x="350" y="46" text-anchor="middle" fill="#CFE3F0">Policy &middot; objectives &middot; responsibility</text>
    <text x="350" y="58" text-anchor="middle" fill="#CFE3F0">management representative &middot; review</text>
    <rect x="482" y="14" width="200" height="52" fill="#14537D"/>
    <text x="582" y="32" text-anchor="middle" fill="#fff" font-weight="bold">Clause 6 &middot; Resources</text>
    <text x="582" y="46" text-anchor="middle" fill="#CFE3F0">Competence &amp; training &middot; infrastructure</text>
    <text x="582" y="58" text-anchor="middle" fill="#CFE3F0">work environment &amp; contamination control</text>
    <rect x="18" y="86" width="432" height="60" fill="#2E7D96"/>
    <text x="234" y="106" text-anchor="middle" fill="#fff" font-weight="bold">Clause 7 &middot; Product Realization</text>
    <text x="234" y="121" text-anchor="middle" fill="#E2F1F5">Planning &middot; customer/regulatory requirements &middot; design &amp; development (7.3)</text>
    <text x="234" y="134" text-anchor="middle" fill="#E2F1F5">purchasing &amp; supplier control (7.4) &middot; production, validation, identification,</text>
    <text x="234" y="145" text-anchor="middle" fill="#E2F1F5">traceability (7.5) &middot; monitoring &amp; measuring equipment (7.6)</text>
    <rect x="482" y="86" width="200" height="60" fill="#1E6E4A"/>
    <text x="582" y="106" text-anchor="middle" fill="#fff" font-weight="bold">Clause 8 &middot; Measurement,</text>
    <text x="582" y="119" text-anchor="middle" fill="#fff" font-weight="bold">Analysis &amp; Improvement</text>
    <text x="582" y="133" text-anchor="middle" fill="#D9F0E4">Feedback &amp; complaints &middot; internal audit &middot;</text>
    <text x="582" y="144" text-anchor="middle" fill="#D9F0E4">nonconformity &middot; CAPA &middot; reporting</text>
  </g>
  <g stroke="#5B6770" stroke-width="0.9" fill="none">
    <line x1="118" y1="66" x2="118" y2="86"/><line x1="350" y1="66" x2="300" y2="86"/><line x1="582" y1="66" x2="582" y2="86"/>
  </g>
  <text x="350" y="176" font-size="9.2" fill="#0F4C5C" text-anchor="middle" font-family="Manrope" font-weight="bold">Plan &rarr; Do &rarr; Check &rarr; Act: clause 7 does; clause 8 checks and corrects; clauses 4&ndash;6 plan and resource</text>
  <text x="350" y="196" font-size="8.4" fill="#5B6770" text-anchor="middle">Permitted exclusions: clause 7.3 (design) where regulations allow; non-applicabilities in 6&ndash;8 must be justified</text>
</svg>
<div class="figcaption"><b>Figure 7.1</b> &nbsp;The clause map of ISO 13485:2016 arranged as a PDCA system. India's Fifth Schedule (MDR 2017) and the FDA QMSR mirror this same substance.</div>
</div>
<p>Three clauses do the daily heavy lifting. <strong>7.4 purchasing</strong>: suppliers are qualified, risk-ranked
and monitored &mdash; quality agreements bind critical suppliers because the manufacturer, not the supplier,
owns final responsibility. <strong>7.5 production</strong>: work instructions, device identification and
traceability (unit-level for implants), cleanliness, servicing, and the validated processes of Chapter 6.
<strong>8.5 improvement</strong>: corrective and preventive action &mdash; the QMS's immune system.</p>

<h2 class="sec"><span class="secnum">7.3</span>Documentation: Say It, Do It, Prove It</h2>
<span class="wframe">How</span>
<p>The documentation pyramid descends from the <strong>quality manual</strong> (scope, exclusions, process map),
through <strong>procedures</strong> (SOPs answering who/what/when) and <strong>work instructions</strong> (task-level how),
to <strong>records</strong> &mdash; the objective evidence. Two compilations matter specially: the <strong>medical device
file</strong> (clause 4.2.3; the DMR of Chapter 3) for each device family, and quality records retained for at
least the device lifetime as defined by the organisation (and not less than regulation demands). Document
control &mdash; approval, revision status, availability at point of use, obsolete-document withdrawal &mdash; is the
most-cited audit finding category worldwide; a superseded drawing on a production floor is a recall
mechanism in waiting.</p>

<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>The auditor's folk theorem &mdash; <em>&ldquo;if it isn't documented, it didn't happen&rdquo;</em> &mdash; has a converse
  that trips organisations just as often: if it <em>is</em> documented, it must be happening. Writing
  aspirational SOPs the floor cannot follow manufactures nonconformities.</p>
</div>

<h2 class="sec"><span class="secnum">7.4</span>CAPA, Audits and Management Review</h2>
<span class="wframe">How &middot; Why</span>
<p><strong>CAPA</strong> distinguishes three reflexes: <strong>correction</strong> (fix this unit &mdash; rework, scrap),
<strong>corrective action</strong> (find and remove the root cause so it cannot recur), and <strong>preventive
action</strong> (act on a potential cause before any nonconformity occurs). The discipline lives or dies on
<strong>root cause analysis</strong> &mdash; 5-Why, fishbone (Ishikawa), fault trees &mdash; and on <strong>effectiveness
checks</strong>: a CAPA closed without evidence that the problem stopped recurring is paperwork, not quality.
Inputs stream in from complaints, nonconformities, audit findings, service reports and post-market data;
CAPA is the hinge that turns Chapter 12's surveillance into Chapter 3's design changes.</p>
<p><strong>Internal audits</strong> (clause 8.2.4) test the QMS against the standard, regulations and the
organisation's own documents &mdash; planned, independent (no one audits their own work), evidence-based, and
closed through CAPA. <strong>Management review</strong> (clause 5.6) is the board-level feedback loop with
mandated inputs (audit results, complaints, regulatory changes, CAPA status, new-product performance) and
outputs (resource and improvement decisions) &mdash; the meeting where quality either has a seat or does not.</p>

<h2 class="sec"><span class="secnum">7.5</span>Certification and Its Regulatory Leverage</h2>
<span class="wframe">Where &middot; When</span>
<p>ISO 13485 certification is issued after a two-stage initial audit by an accredited certification body,
maintained by annual surveillance and three-yearly recertification. Its leverage is global:</p>
<ul>
  <li><strong>European Union</strong> &mdash; notified bodies assess the manufacturer's QMS against EU MDR Annex IX; an
  ISO 13485-conformant system is the practical backbone of CE conformity.</li>
  <li><strong>MDSAP</strong> &mdash; one ISO 13485-based audit accepted by the USA, Canada (mandatory), Brazil, Australia
  and Japan (Chapter 2).</li>
  <li><strong>USA</strong> &mdash; the QMSR (effective 2 February 2026) incorporates ISO 13485:2016 as the substance of
  21 CFR 820 (Chapter 3).</li>
  <li><strong>India</strong> &mdash; MDR 2017 licences presuppose QMS compliance with the <strong>Fifth Schedule</strong>, drafted
  in close alignment with ISO 13485; CDSCO and notified auditors audit against it, and ICMED (the
  Quality Council of India's certification scheme) offers an Indian certification pathway built on the
  same base.</li>
</ul>

<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight</div>
  <p>Certification is <em>not</em> product approval: ISO 13485 certifies the system, while licences, 510(k)s
  and CE certificates authorise devices. A certified plant can still make an unapprovable product; an
  auditor's certificate never substitutes for a licence &mdash; a distinction examiners love to test.</p>
</div>
<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Hospital procurement teams increasingly demand ISO 13485 certificates from device suppliers &mdash; and
  pharmacists sitting on procurement committees should read them critically: check scope (does it cover
  the product category offered?), site addresses, validity dates and the issuing body's accreditation.</p>
</div>
<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>QMS roles are the largest single employment category for pharmacy graduates entering medtech: QMS
  engineers, document controllers, CAPA specialists, supplier quality auditors, management representatives.
  Lead-auditor certification (ISO 13485/19011) is a recognised career accelerator.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 7.1 &middot; The CAPA That Stopped at Correction</div>
  <div class="cs-body">
    <p>A catheter manufacturer receives complaints of kinking. Investigation finds an extrusion lot with
    wall thickness at the low specification edge; the firm scraps remaining stock and closes the file. Six
    months later the complaint recurs. A proper root cause analysis finally reveals that a die had been
    polished during maintenance, shifting the process mean, and that SPC limits had been set from the
    original validation and never alarmed. Corrective action: maintenance-triggered requalification of the
    die, recalculated control limits, and a preventive review of all maintenance activities that can alter
    validated parameters. The effectiveness check: twelve months of complaint and SPC data.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Classify each action taken (correction / corrective / preventive).</li>
      <li>Which clause linkages (7.5, 7.6, 8.2, 8.5) does this case thread together?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Scrapping stock = correction; die requalification and new limits = corrective action; the
      maintenance-programme review = preventive action extended to analogous processes. (2) Production
      control and validation maintenance (7.5), monitoring equipment/limits (7.6), complaint feedback
      (8.2.1&ndash;8.2.2), nonconformity and CAPA (8.3, 8.5) &mdash; the QMS working as one circuit.</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 7.2 &middot; An Indian SME Builds Its QMS for Export</div>
  <div class="cs-body">
    <p>A Coimbatore surgical instruments SME selling domestically under an SLA licence wins a European
    distributor's interest. Gap analysis against ISO 13485 finds: no design control records for legacy
    instruments, purchasing on price alone, and no CAPA system distinct from a complaints register. Over
    eighteen months the firm builds a documented QMS &mdash; medical device files for instrument families,
    supplier qualification, CAPA with root-cause training &mdash; achieves certification, and then engages a
    notified body for CE marking of its Class I reusable (Ir) instruments. The same system later shortens
    its MDSAP path when a Canadian buyer appears.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Why did certification precede rather than substitute for CE marking?</li>
      <li>Which QMS investments create the greatest cross-market leverage?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) The certificate evidences the system; Class Ir devices still require notified body conformity
      assessment of reprocessing aspects and a Declaration of Conformity (Chapter 2). (2) Documentation
      architecture, supplier control and CAPA &mdash; the clauses every jurisdiction audits &mdash; deliver leverage
      across EU, MDSAP and India's Fifth Schedule simultaneously.</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>A QMS is the documented system through which safe, compliant devices are produced consistently; regulators license systems as much as products.</li>
    <li>ISO 13485:2016 adapts ISO 9001 for devices: regulatory compliance and maintained effectiveness over continual-improvement rhetoric, ISO 14971 risk integration, prescribed documentation, device-specific clauses.</li>
    <li>Clause map: 4 QMS &amp; documents; 5 management; 6 resources; 7 product realization (design 7.3, purchasing 7.4, production/validation 7.5); 8 feedback, audit, nonconformity, CAPA.</li>
    <li>Documentation descends manual &rarr; procedures &rarr; work instructions &rarr; records, with the medical device file per family; document control failures are the world's most-cited findings.</li>
    <li>CAPA = correction vs corrective vs preventive action, powered by root-cause analysis and proven by effectiveness checks; audits and management review close the loop.</li>
    <li>Certification leverages market access &mdash; EU notified body assessment, MDSAP's five jurisdictions, FDA's QMSR, India's Fifth Schedule/ICMED &mdash; but never substitutes for product approval.</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Quality manual</dt> <dd>&mdash; top-level document defining QMS scope, exclusions and process interactions.</dd></div>
    <div class="kt-row"><dt>Medical device file</dt> <dd>&mdash; per-family compilation of specifications and QMS references (clause 4.2.3).</dd></div>
    <div class="kt-row"><dt>Correction / corrective / preventive action</dt> <dd>&mdash; fix the unit / remove the cause / pre-empt a potential cause.</dd></div>
    <div class="kt-row"><dt>Root cause analysis</dt> <dd>&mdash; systematic cause identification (5-Why, Ishikawa, FTA).</dd></div>
    <div class="kt-row"><dt>Effectiveness check</dt> <dd>&mdash; evidence that a CAPA actually stopped recurrence.</dd></div>
    <div class="kt-row"><dt>Internal audit</dt> <dd>&mdash; planned, independent conformity check of the QMS (clause 8.2.4).</dd></div>
    <div class="kt-row"><dt>Management review</dt> <dd>&mdash; top-management evaluation of QMS suitability with defined inputs/outputs (5.6).</dd></div>
    <div class="kt-row"><dt>Quality agreement</dt> <dd>&mdash; binding quality responsibilities between manufacturer and supplier.</dd></div>
    <div class="kt-row"><dt>ICMED</dt> <dd>&mdash; Indian Certification for Medical Devices (Quality Council of India scheme).</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 7 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>ISO 13485:2016 differs from ISO 9001:2015 chiefly in that it:
    <ul class="mcq-opts"><li><span class="ol">a)</span> abolishes documentation</li><li><span class="ol">b)</span> prioritises regulatory compliance and maintained effectiveness over continual improvement</li><li><span class="ol">c)</span> applies only to importers</li><li><span class="ol">d)</span> has no audit requirement</li></ul>
    <div class="rationale"><b>Answer: b.</b> The device standard trades 9001's improvement/customer-satisfaction emphasis for regulatory stability, ISO 14971 integration and heavier documentation.</div></li>
  <li>Design and development requirements sit in ISO 13485 clause:
    <ul class="mcq-opts"><li><span class="ol">a)</span> 4.2</li><li><span class="ol">b)</span> 5.6</li><li><span class="ol">c)</span> 7.3</li><li><span class="ol">d)</span> 8.5</li></ul>
    <div class="rationale"><b>Answer: c.</b> Clause 7.3 (within product realization) mirrors the design controls of Chapter 3; 4.2 is documentation, 5.6 management review, 8.5 improvement/CAPA.</div></li>
  <li>Reworking a defective unit found on the line is an example of:
    <ul class="mcq-opts"><li><span class="ol">a)</span> preventive action</li><li><span class="ol">b)</span> corrective action</li><li><span class="ol">c)</span> management review</li><li><span class="ol">d)</span> correction</li></ul>
    <div class="rationale"><b>Answer: d.</b> Correction fixes the nonconforming item; corrective action removes the root cause; preventive action pre-empts potential causes.</div></li>
  <li>The per-device-family compilation of specifications required by clause 4.2.3 is the:
    <ul class="mcq-opts"><li><span class="ol">a)</span> medical device file</li><li><span class="ol">b)</span> quality policy</li><li><span class="ol">c)</span> audit programme</li><li><span class="ol">d)</span> training matrix</li></ul>
    <div class="rationale"><b>Answer: a.</b> The medical device file (the DMR in US vocabulary) holds device, production, QC and labeling specifications.</div></li>
  <li>Internal audits must be:
    <ul class="mcq-opts"><li><span class="ol">a)</span> unplanned to surprise staff</li><li><span class="ol">b)</span> planned and independent of the work audited</li><li><span class="ol">c)</span> performed only by external bodies</li><li><span class="ol">d)</span> annual board meetings</li></ul>
    <div class="rationale"><b>Answer: b.</b> Clause 8.2.4 requires a planned programme with auditor objectivity &mdash; no one audits their own work.</div></li>
  <li>A CAPA is demonstrably complete only when:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the form is signed</li><li><span class="ol">b)</span> stock is scrapped</li><li><span class="ol">c)</span> a memo is circulated</li><li><span class="ol">d)</span> an effectiveness check shows the problem stopped recurring</li></ul>
    <div class="rationale"><b>Answer: d.</b> Without verification of effectiveness, a CAPA is administrative closure, not quality assurance.</div></li>
  <li>MDSAP audits are conducted against:
    <ul class="mcq-opts"><li><span class="ol">a)</span> ISO 14971 alone</li><li><span class="ol">b)</span> IEC 60601</li><li><span class="ol">c)</span> ISO 13485 plus participating countries' regulatory requirements</li><li><span class="ol">d)</span> ISO 9001</li></ul>
    <div class="rationale"><b>Answer: c.</b> The single audit combines ISO 13485 with the specific requirements of the USA, Canada, Brazil, Australia and Japan.</div></li>
  <li>India's QMS requirements for device manufacturers are set out in:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the Fifth Schedule of MDR 2017</li><li><span class="ol">b)</span> Schedule M</li><li><span class="ol">c)</span> the Second Schedule of the D&amp;C Act</li><li><span class="ol">d)</span> Form MD-14</li></ul>
    <div class="rationale"><b>Answer: a.</b> The Fifth Schedule, aligned to ISO 13485, is audited for licensing; Schedule M governs pharmaceuticals.</div></li>
  <li>ISO 13485 certification proves:
    <ul class="mcq-opts"><li><span class="ol">a)</span> every product is approved</li><li><span class="ol">b)</span> the quality management system conforms &mdash; not that any product is approved</li><li><span class="ol">c)</span> exemption from inspection</li><li><span class="ol">d)</span> clinical efficacy</li></ul>
    <div class="rationale"><b>Answer: b.</b> System certification and product authorisation are distinct legal acts; both are required for market access.</div></li>
  <li>Mandated inputs to management review include:
    <ul class="mcq-opts"><li><span class="ol">a)</span> only financial results</li><li><span class="ol">b)</span> marketing plans alone</li><li><span class="ol">c)</span> shareholder lists</li><li><span class="ol">d)</span> audit results, complaints, CAPA status and regulatory changes</li></ul>
    <div class="rationale"><b>Answer: d.</b> Clause 5.6.2 specifies quality-system inputs so that top management confronts the QMS's real condition.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>ISO 13485:2016 follows the Annex SL high-level structure of ISO 9001:2015. <span class="marks">(F &mdash; it retains the older clause 4&ndash;8 architecture)</span></li>
  <li>Design control (clause 7.3) may be excluded where regulations permit, with justification. <span class="marks">(T)</span></li>
  <li>Implantable devices demand unit-level traceability records. <span class="marks">(T)</span></li>
  <li>A supplier's quality failure transfers legal responsibility away from the manufacturer. <span class="marks">(F &mdash; the manufacturer retains responsibility)</span></li>
  <li>Document control failures are among the most-cited audit findings globally. <span class="marks">(T)</span></li>
  <li>Preventive action responds to a nonconformity that has already occurred. <span class="marks">(F &mdash; that is corrective action)</span></li>
  <li>Management review has mandated inputs and outputs under clause 5.6. <span class="marks">(T)</span></li>
  <li>The FDA QMSR made ISO 13485:2016 the substance of US device QMS law. <span class="marks">(T)</span></li>
  <li>An ISO 13485 certificate covers any product the company may later make. <span class="marks">(F &mdash; scope-limited by product category and site)</span></li>
  <li>ICMED is a Quality Council of India certification scheme for medical devices. <span class="marks">(T)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>The full title theme of ISO 13485 is quality management systems &mdash; requirements for __________ purposes.</li>
  <li>The top-level QMS document defining scope and process interactions is the __________.</li>
  <li>Purchasing and supplier control is ISO 13485 clause __________.</li>
  <li>Fixing the defective unit itself is called a __________.</li>
  <li>Removing the root cause so a nonconformity cannot recur is __________ action.</li>
  <li>The fishbone diagram used in root cause analysis is also called the __________ diagram.</li>
  <li>India's MDR 2017 QMS requirements are in the __________ Schedule.</li>
  <li>The single audit programme spanning five jurisdictions is __________.</li>
  <li>Internal audit requirements appear in clause __________.</li>
  <li>Proof that a CAPA worked is documented in the __________ check.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> ISO 13485 demands more prescribed documentation than ISO 9001. <strong>R:</strong> Regulatory audits require objective, retrievable evidence of every quality-relevant activity. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> A certified QMS guarantees product approval in the EU. <strong>R:</strong> Notified bodies also review device-specific technical documentation. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> CAPA effectiveness checks are optional refinements. <strong>R:</strong> Complaints are an input to CAPA. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> Suppliers of critical components are bound by quality agreements. <strong>R:</strong> The manufacturer retains final responsibility for purchased product. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Management review can be delegated entirely to the quality department. <strong>R:</strong> Clause 5.6 assigns the review to top management. <span class="marks">(d)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>State four deliberate differences between ISO 13485:2016 and ISO 9001:2015.</li>
  <li>Sketch the documentation pyramid with one example per level.</li>
  <li>Differentiate correction, corrective action and preventive action with a single running example.</li>
  <li>List five mandated inputs to management review.</li>
  <li>What must a procurement pharmacist verify on a supplier's ISO 13485 certificate?</li>
  <li>How does ISO 13485 certification shorten the path to MDSAP and EU market access?</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Map the clause structure of ISO 13485:2016 (4&ndash;8) to the departments and daily activities of a catheter manufacturer, and identify the records an auditor would sample in each clause.</li>
  <li>Describe the CAPA lifecycle from complaint signal to effectiveness check, embedding root-cause tools, and analyse why CAPAs fail in practice using Case Study 7.1.</li>
  <li>Evaluate the global regulatory leverage of ISO 13485 certification across the EU, MDSAP, the US QMSR and India's Fifth Schedule &mdash; and its limits (why certification is not approval).</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>You inherit a QMS with 240 open CAPAs, most overdue. Design a triage and reduction strategy that preserves compliance integrity while restoring the system's credibility.</li>
  <li>Draft the agenda and input pack (with example metrics) for a management review at a firm one year from its first MDSAP audit.</li>
  <li>A cost-cutting proposal outsources final inspection to the component supplier. Argue the QMS implications under clauses 7.4 and 8.2.6 and design the controls that would make it defensible &mdash; or show why it is not.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>International Organization for Standardization. ISO 13485:2016 &mdash; Medical devices &mdash; Quality management systems &mdash; Requirements for regulatory purposes. Geneva: ISO; 2016.</li>
  <li>International Organization for Standardization. ISO 9001:2015 &mdash; Quality management systems &mdash; Requirements. Geneva: ISO; 2015.</li>
  <li>US Food and Drug Administration. Quality Management System Regulation final rule (89 FR 7496, effective 2 February 2026). Silver Spring (MD): FDA; 2024.</li>
  <li>Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 &mdash; Fifth Schedule. New Delhi: MoHFW; 2017.</li>
  <li>International Medical Device Regulators Forum. MDSAP audit model and companion documents. IMDRF/MDSAP.</li>
  <li>European Parliament and Council. Regulation (EU) 2017/745, Annex IX &mdash; conformity assessment based on a QMS. OJEU. 2017;L117.</li>
  <li>International Organization for Standardization. ISO 19011:2018 &mdash; Guidelines for auditing management systems. Geneva: ISO; 2018.</li>
  <li>Quality Council of India. ICMED &mdash; Indian Certification for Medical Devices scheme documents. New Delhi: QCI.</li>
  <li>International Organization for Standardization. ISO 14971:2019. Geneva: ISO; 2019.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 7 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 7.1&ndash;7.5</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figure 7.1; Table 7.1</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 7.1 (CAPA failure), 7.2 (SME export QMS)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>ISO 13485:2016 clauses, QMSR 89 FR 7496, Fifth Schedule, MDSAP &mdash; cited</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>9 references</td></tr>
</table>
</div>

</section>
"""
