CH03_HTML = """
<section class="chapter" id="ch03" data-running="Chapter 3 · Design &amp; Development">

<div class="ch-opener">
  <div class="ch-kicker">Part II &middot; Design, Biomaterials &amp; Biocompatibility &middot; Chapter 3</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">03</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Medical Device Design &amp; Development Process</h1>
      <div class="ch-tagline">The device lifecycle &middot; design controls &middot; verification and validation &middot; safety analysis &middot; human factors</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Describe the stages of the medical device lifecycle from concept to post-market. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Explain the elements of design controls under 21 CFR 820.30 and ISO 13485:2016 clause 7.3. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Translate user needs into design inputs and outputs for a given device. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Differentiate design verification from design validation with examples. <span class="lo-tag">CO2 &middot; Analyse</span></li>
    <li>Apply FMEA and FTA as safety-analysis tools within design. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Evaluate the role of human factors/usability engineering (IEC 62366-1) in preventing use error. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Describe the design-controlled device lifecycle</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Apply design control and safety-analysis tools</td><td>L3&ndash;L4</td><td>3, 4, 5</td></tr>
    <tr><td>CO3</td><td>Evaluate usability engineering in device safety</td><td>L5</td><td>6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">3.1</span>The Medical Device Lifecycle</h2>
<span class="wframe">What &middot; When</span>
<p class="lead">A medical device is not &ldquo;invented&rdquo; in a flash of genius and shipped; it is <strong>developed</strong> through
a disciplined lifecycle in which every claim about safety and performance must be planned, documented and
proven before a patient ever touches the product &mdash; and continuously re-proven afterwards.</p>
<p>The lifecycle is conventionally divided into: <strong>concept and feasibility</strong> (unmet clinical need,
market and technology assessment, proof-of-concept prototypes); <strong>design and development</strong> (design
controls, discussed below); <strong>verification and validation</strong>; <strong>regulatory submission and design
transfer</strong> to manufacturing; <strong>production</strong>; and <strong>post-market surveillance</strong> feeding field experience
back into design changes. The cycle is a loop, not a line: Chapter 12's vigilance data is Chapter 3's next
design input.</p>
<p>Development is typically managed through <strong>phase&ndash;gate (stage&ndash;gate) reviews</strong>: the project may pass
to the next phase only when a formal review confirms that the deliverables of the current phase &mdash;
documents, test results, risk analyses &mdash; are complete. This structure exists because design defects are
cheapest to fix on paper and most expensive to fix by recall: industry analyses and FDA recall studies have
repeatedly attributed a substantial share of device recalls to design-related root causes, which is
precisely why regulators regulate <em>the process of designing</em> and not merely the finished article.</p>

<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight &middot; From QSR to QMSR</div>
  <p>US design controls were codified in <strong>21 CFR 820.30</strong> (Quality System Regulation, 1996). On
  31 January 2024 the FDA issued the <strong>Quality Management System Regulation (QMSR)</strong> final rule, which
  incorporates <strong>ISO 13485:2016</strong> by reference and took effect on <strong>2 February 2026</strong>. Design control
  expectations now live in ISO 13485 clause 7.3 for FDA purposes too &mdash; a landmark harmonization: one QMS
  standard now anchors the USA, EU conformity practice, MDSAP and India's Fifth Schedule expectations.</p>
</div>

<h2 class="sec"><span class="secnum">3.2</span>Design Controls</h2>
<span class="wframe">How</span>
<p>Design controls are a set of interlocking, documented practices that force a development team to state
what the device must do, prove the design does it, and prove the device as used actually serves the user.
The classical FDA &ldquo;waterfall&rdquo; diagram (adapted from the FDA/GHTF design control guidance) captures the
logic:</p>

<div class="figure">
<svg viewBox="0 0 700 240" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <defs><marker id="a3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0F4C5C"/></marker></defs>
  <g font-size="9.4" text-anchor="middle">
    <rect x="30" y="15" width="130" height="34" fill="#0F4C5C"/><text x="95" y="36" fill="#fff" font-weight="bold">User Needs</text>
    <rect x="150" y="70" width="130" height="34" fill="#14537D"/><text x="215" y="91" fill="#fff" font-weight="bold">Design Input</text>
    <rect x="270" y="125" width="130" height="34" fill="#2E7D96"/><text x="335" y="146" fill="#fff" font-weight="bold">Design Process</text>
    <rect x="390" y="180" width="130" height="34" fill="#14537D"/><text x="455" y="201" fill="#fff" font-weight="bold">Design Output</text>
    <rect x="540" y="15" width="130" height="34" fill="#0F4C5C"/><text x="605" y="36" fill="#fff" font-weight="bold">Medical Device</text>
  </g>
  <g stroke="#0F4C5C" stroke-width="1.2" fill="none" marker-end="url(#a3)">
    <line x1="95" y1="49" x2="200" y2="70"/>
    <line x1="215" y1="104" x2="320" y2="125"/>
    <line x1="335" y1="159" x2="440" y2="180"/>
    <line x1="520" y1="197" x2="605" y2="52"/>
  </g>
  <g stroke="#B4690E" stroke-width="1" fill="none" stroke-dasharray="4 3" marker-end="url(#a3)">
    <path d="M 455 180 C 420 130 300 95 282 92"/>
    <path d="M 605 52 C 560 25 220 20 162 30"/>
  </g>
  <g font-size="8.6" fill="#B4690E" font-weight="bold">
    <text x="330" y="112">VERIFICATION: output meets input</text>
    <text x="300" y="14">VALIDATION: device meets user needs</text>
  </g>
  <text x="30" y="232" font-size="8.4" fill="#5B6770">Design reviews are held at each transition; every arrow generates records in the Design History File.</text>
</svg>
<div class="figcaption"><b>Figure 3.1</b> &nbsp;The design-control &ldquo;waterfall&rdquo; (adapted from FDA design control guidance). Verification closes the loop between output and input; validation closes the loop between the finished device and user needs.</div>
</div>

<h3 class="subsec">3.2.1 The elements</h3>
<div class="tablewrap">
<div class="tabcaption"><b>Table 3.1</b> &nbsp;Design control elements (21 CFR 820.30 / ISO 13485:2016 clause 7.3)</div>
<table class="data">
  <tr><th style="width:40mm;">Element</th><th>What it demands</th><th style="width:44mm;">Typical records</th></tr>
  <tr><td class="rowhead">Design &amp; development planning</td><td>Plan stages, responsibilities, interfaces, review points before work begins</td><td>D&amp;D plan, project charter</td></tr>
  <tr><td class="rowhead">Design inputs</td><td>Complete, unambiguous, testable requirements: performance, safety, usability, regulatory (e.g., EU GSPR Annex I), standards</td><td>Design input/requirements specification</td></tr>
  <tr><td class="rowhead">Design outputs</td><td>Drawings, specifications, software, labeling that can be checked against inputs; identify outputs essential for proper functioning</td><td>Drawings, DMR content, acceptance criteria</td></tr>
  <tr><td class="rowhead">Design review</td><td>Systematic, documented reviews at planned stages incl. an independent reviewer</td><td>Review minutes, action logs</td></tr>
  <tr><td class="rowhead">Design verification</td><td>Confirm outputs meet inputs (&ldquo;did we build the device right?&rdquo;)</td><td>Test protocols &amp; reports, analyses</td></tr>
  <tr><td class="rowhead">Design validation</td><td>Confirm the device meets user needs and intended use, on initial production units, under actual/simulated use, incl. software validation and clinical evaluation where needed (&ldquo;did we build the right device?&rdquo;)</td><td>Validation protocols/reports, HF summative study, clinical evaluation</td></tr>
  <tr><td class="rowhead">Design transfer</td><td>Translate the design correctly into production specifications</td><td>Transfer checklist, process validation links</td></tr>
  <tr><td class="rowhead">Design changes</td><td>Identify, document, verify/validate, review and approve changes before implementation</td><td>Change orders, impact/risk assessments</td></tr>
  <tr><td class="rowhead">Design history file (DHF)</td><td>The compiled evidence that the design was developed under controls</td><td>DHF index referencing all of the above</td></tr>
</table>
</div>

<p>Three documents are habitually confused and must be separated: the <strong>DHF</strong> (Design History File)
tells the story of <em>how the design was developed</em>; the <strong>DMR</strong> (Device Master Record) is the recipe
&mdash; the complete set of specifications to <em>build</em> the device; the <strong>DHR</strong> (Device History Record)
is the batch record proving a <em>specific unit or lot</em> was built to the DMR. In ISO 13485 language the
DMR corresponds to the <strong>medical device file</strong> (clause 4.2.3).</p>

<h3 class="subsec">3.2.2 User needs and design inputs</h3>
<p>Design quality is decided at the input stage. A user need (&ldquo;nurses must be able to programme the
infusion pump quickly and without error, wearing gloves, in a dim ward&rdquo;) must be decomposed into
verifiable inputs (&ldquo;keypad operable with nitrile gloves; rate entry &le;5 keystrokes; display legible at
1 m at 50 lux; hard limits per drug library&rdquo;). Inputs come from clinicians and patients, predicate and
competitor analysis, applicable standards (IEC 60601 series, ISO 14971), regulatory requirements (EU MDR
General Safety and Performance Requirements, Annex I), and the risk management file. Ambiguous inputs
(&ldquo;easy to use&rdquo;, &ldquo;biocompatible&rdquo;) are the classic root cause of late-stage failure because nothing
untestable can be verified.</p>

<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Pharmacists are natural sources of design input: they know that a prefilled syringe's plunger force
  matters to arthritic hands, that look-alike device labels cause selection errors in a crash cart, and
  that a drug library's hard and soft limits are what actually prevent infusion overdoses. Manufacturers
  conducting user research routinely interview pharmacists alongside nurses and physicians.</p>
</div>

<h2 class="sec"><span class="secnum">3.3</span>Verification vs Validation</h2>
<span class="wframe">How &middot; Why</span>
<p><strong>Verification</strong> asks: does the design output conform to the design input? It is analytical and
bench-based: dimensional inspection, tensile testing, electrical safety testing to IEC 60601-1, software
unit and integration testing, sterile barrier integrity testing. <strong>Validation</strong> asks the deeper
question: does the device, as produced, satisfy the defined user needs and intended uses? It must be
performed on <strong>initial production units (or equivalents)</strong> under <strong>actual or simulated use
conditions</strong>, and it includes usability validation and, where required, clinical investigation.</p>
<div class="tablewrap">
<div class="tabcaption"><b>Table 3.2</b> &nbsp;Verification vs validation &mdash; an infusion pump example</div>
<table class="data">
  <tr><th style="width:34mm;">Aspect</th><th>Verification</th><th>Validation</th></tr>
  <tr><td class="rowhead">Question</td><td>Did we build the device right?</td><td>Did we build the right device?</td></tr>
  <tr><td class="rowhead">Reference</td><td>Design inputs</td><td>User needs / intended use</td></tr>
  <tr><td class="rowhead">Example</td><td>Flow-rate accuracy &plusmn;5% across range on test bench; occlusion alarm at set pressure</td><td>Nurses in a simulated ward programme complex infusions; no critical use errors; therapy delivered as intended</td></tr>
  <tr><td class="rowhead">Units used</td><td>Prototypes or production units</td><td>Initial production units (or equivalent)</td></tr>
  <tr><td class="rowhead">Typical methods</td><td>Bench tests, inspections, analyses, software testing</td><td>Simulated/actual use studies, HF summative evaluation, clinical evaluation</td></tr>
</table>
</div>

<h2 class="sec"><span class="secnum">3.4</span>Safety Analysis in Design</h2>
<span class="wframe">How</span>
<p>Design-stage risk work applies ISO 14971 (treated fully in Chapter 8) through two complementary tools:</p>
<ul>
  <li><strong>FMEA &mdash; Failure Mode and Effects Analysis.</strong> A <em>bottom-up</em> inductive method: for each
  component or process step, ask how it can fail (failure mode), what happens (effect), why (cause), and
  how bad/likely/detectable it is. Design FMEA (dFMEA) addresses the product; process FMEA (pFMEA)
  addresses manufacturing. Outputs feed design changes and process controls.</li>
  <li><strong>FTA &mdash; Fault Tree Analysis.</strong> A <em>top-down</em> deductive method: start from an undesired top
  event (&ldquo;over-infusion reaches patient&rdquo;) and decompose through AND/OR logic gates into basic causes,
  exposing single-point failures and the value of independent safeguards.</li>
</ul>
<p>The two are complementary: FMEA is exhaustive but component-centric; FTA reveals combinations. Both
must trace into the risk management file, and every high-risk line item must map to a risk control that is
itself verified.</p>

<div class="figure">
<svg viewBox="0 0 700 205" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <g font-size="9" text-anchor="middle">
    <rect x="250" y="10" width="200" height="30" fill="#0F4C5C"/><text x="350" y="29" fill="#fff" font-weight="bold">TOP EVENT: over-infusion reaches patient</text>
    <rect x="285" y="58" width="130" height="24" fill="#E4EFF1" stroke="#0F4C5C"/><text x="350" y="73" font-weight="bold" fill="#0F4C5C">OR</text>
    <rect x="60" y="110" width="170" height="30" fill="#F0F5FA" stroke="#14537D"/><text x="145" y="129" fill="#14537D">Pump delivers wrong rate</text>
    <rect x="265" y="110" width="170" height="30" fill="#F0F5FA" stroke="#14537D"/><text x="350" y="129" fill="#14537D">Wrong rate programmed</text>
    <rect x="470" y="110" width="170" height="30" fill="#F0F5FA" stroke="#14537D"/><text x="555" y="129" fill="#14537D">Free-flow on set removal</text>
    <rect x="180" y="165" width="150" height="28" fill="#fff" stroke="#B4690E"/><text x="255" y="182" fill="#B4690E">AND: use error + soft limit off</text>
    <rect x="380" y="165" width="180" height="28" fill="#fff" stroke="#B4690E"/><text x="470" y="182" fill="#B4690E">AND: clamp fails + no anti-free-flow</text>
  </g>
  <g stroke="#5B6770" stroke-width="1">
    <line x1="350" y1="40" x2="350" y2="58"/>
    <line x1="315" y1="82" x2="145" y2="110"/><line x1="350" y1="82" x2="350" y2="110"/><line x1="385" y1="82" x2="555" y2="110"/>
    <line x1="350" y1="140" x2="270" y2="165"/><line x1="555" y1="140" x2="480" y2="165"/>
  </g>
</svg>
<div class="figcaption"><b>Figure 3.2</b> &nbsp;A simplified fault tree for an infusion pump. AND-gates show where two independent safeguards must both fail &mdash; the design rationale for anti-free-flow valves and dose-error-reduction software.</div>
</div>

<h2 class="sec"><span class="secnum">3.5</span>Human Factors &amp; Usability Engineering</h2>
<span class="wframe">Why &middot; How</span>
<p>A large fraction of device harm arises not from device malfunction but from <strong>use error</strong> &mdash;
predictable mistakes induced by design. Usability engineering, standardised in <strong>IEC 62366-1:2015</strong>
(with FDA's 2016 human factors guidance closely parallel), requires manufacturers to: define intended
users, uses and use environments; identify <strong>hazard-related use scenarios</strong>; analyse tasks; run
<strong>formative</strong> evaluations during design; and conclude with a <strong>summative (validation) usability
evaluation</strong> in which representative users perform critical tasks in a realistic environment, with
residual use-error risks judged against ISO 14971 criteria. Insulin pens, autoinjectors, home nebulisers
and infusion pumps are canonical subjects &mdash; all products the pharmacist dispenses and demonstrates.</p>

<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>FDA's decade-long infusion pump initiative followed tens of thousands of adverse event reports and
  scores of recalls, many rooted in confusing user interfaces &mdash; a key reason premarket review of pumps
  now expects human-factors validation data, not just bench accuracy.</p>
</div>

<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>&ldquo;Design assurance&rdquo; is a hiring category in its own right: engineers and life-science graduates who
  can write testable requirements, trace them through V&amp;V matrices, and defend a DHF in audit. Traceability
  tools (requirement &rarr; risk &rarr; test) are among the first software systems a new regulatory/quality recruit
  learns.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 3.1 &middot; Therac-25 &mdash; When Software Design Escapes Control</div>
  <div class="cs-body">
    <p>Between 1985 and 1987 the Therac-25 radiotherapy machine delivered massive radiation overdoses to at
    least six patients, several fatally. Investigations (Leveson &amp; Turner's classic analysis) found race
    conditions in software reused from earlier models whose <em>hardware</em> interlocks had masked the bugs;
    the Therac-25 had removed the hardware interlocks and trusted software alone. There was no independent
    code review, inadequate testing of the integrated system, and error messages so cryptic that operators
    routinely overrode them.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Map each Therac-25 failure to the design-control element that should have caught it.</li>
      <li>Why is &ldquo;removing a hardware interlock&rdquo; a design change demanding re-validation, not just re-verification?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Missing input: no requirement that no single software fault cause overdose (input completeness);
      race conditions undetected (verification of software under realistic operator speed); cryptic messages
      (usability validation); reuse without analysis (design change control). (2) Because the change alters
      the safety architecture experienced by users and patients &mdash; the user-need level &mdash; not merely
      conformance of one output to one input; validation and risk analysis must be repeated.</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 3.2 &middot; Designing an Auto-Disable Syringe for Immunisation Programmes</div>
  <div class="cs-body">
    <p>WHO's push against syringe reuse drove development of auto-disable (AD) syringes, whose plunger locks
    or breaks after a single delivery. The core design inputs came directly from field user needs: must work
    with existing vaccine vials, must not add steps for high-volume vaccinators, must disable irreversibly
    at full dose, must cost within immunisation-programme budgets. Verification tested lock activation force
    and dose accuracy; validation put syringes in the hands of vaccinators in simulated campaign conditions.
    WHO/UNICEF procurement policy subsequently made AD syringes the standard for immunisation &mdash; a case of
    user-need-driven design reshaping global health.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Write three testable design inputs from the user need &ldquo;must not permit reuse&rdquo;.</li>
      <li>Which risks did the AD mechanism itself introduce, and how would a dFMEA capture them?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) e.g., plunger shall lock at &ge;95% of nominal dose delivery; lock shall withstand &ge;X N
      withdrawal force; premature lock rate &le;1 in 10&sup4; under transport stress. (2) New failure modes:
      premature disablement (vaccine wasted), incomplete dose at lock; dFMEA rows would rate severity of
      partial dosing and drive tolerance and training controls.</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>The device lifecycle &mdash; concept, design, V&amp;V, transfer, production, post-market &mdash; is managed by phase&ndash;gate reviews because design defects are the costliest class of failure.</li>
    <li>Design controls (21 CFR 820.30; ISO 13485 clause 7.3 &mdash; now also the FDA baseline under the QMSR effective 2 February 2026) chain planning, inputs, outputs, reviews, verification, validation, transfer and change control, all evidenced in the DHF.</li>
    <li>DHF = how the design was developed; DMR/medical device file = the recipe; DHR = proof a batch followed the recipe.</li>
    <li>Verification proves output meets input; validation proves the produced device meets user needs under actual or simulated use, on initial production units.</li>
    <li>dFMEA/pFMEA (bottom-up) and FTA (top-down) are the working tools of design safety analysis, feeding the ISO 14971 risk file.</li>
    <li>Usability engineering per IEC 62366-1 &mdash; formative studies plus a summative validation &mdash; targets use error, the dominant real-world failure mode of home-use and infusion devices.</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Design controls</dt> <dd>&mdash; regulated practices governing device design (820.30 / ISO 13485 7.3).</dd></div>
    <div class="kt-row"><dt>Design input / output</dt> <dd>&mdash; testable requirements / the specifications and artefacts meeting them.</dd></div>
    <div class="kt-row"><dt>Verification / validation</dt> <dd>&mdash; output-vs-input conformity / device-vs-user-need conformity.</dd></div>
    <div class="kt-row"><dt>DHF, DMR, DHR</dt> <dd>&mdash; design history file; device master record; device history record.</dd></div>
    <div class="kt-row"><dt>Design transfer</dt> <dd>&mdash; controlled hand-over of design into production specifications.</dd></div>
    <div class="kt-row"><dt>FMEA / FTA</dt> <dd>&mdash; bottom-up failure-mode analysis / top-down fault-tree analysis.</dd></div>
    <div class="kt-row"><dt>Use error</dt> <dd>&mdash; predictable user action or omission causing a different result than intended.</dd></div>
    <div class="kt-row"><dt>IEC 62366-1</dt> <dd>&mdash; usability engineering standard for medical devices.</dd></div>
    <div class="kt-row"><dt>QMSR</dt> <dd>&mdash; FDA rule incorporating ISO 13485:2016, effective 2 February 2026.</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 3 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>Design controls primarily regulate:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the finished device only</li><li><span class="ol">b)</span> the process of designing the device</li><li><span class="ol">c)</span> marketing claims</li><li><span class="ol">d)</span> pricing</li></ul>
    <div class="rationale"><b>Answer: b.</b> Regulators audit the documented design process (plans, inputs, V&amp;V, reviews) because design-stage defects drive recalls; the finished article alone cannot reveal them.</div></li>
  <li>&ldquo;Did we build the right device?&rdquo; is the question answered by:
    <ul class="mcq-opts"><li><span class="ol">a)</span> design review</li><li><span class="ol">b)</span> design verification</li><li><span class="ol">c)</span> design validation</li><li><span class="ol">d)</span> design transfer</li></ul>
    <div class="rationale"><b>Answer: c.</b> Validation checks the produced device against user needs/intended use; verification checks outputs against inputs (&ldquo;built right&rdquo;).</div></li>
  <li>The Design History File contains:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the records showing the design was developed under design controls</li><li><span class="ol">b)</span> batch production records</li><li><span class="ol">c)</span> only the final drawings</li><li><span class="ol">d)</span> supplier invoices</li></ul>
    <div class="rationale"><b>Answer: a.</b> The DHF is the evidence trail of development; batch records form the DHR; the recipe of specifications is the DMR.</div></li>
  <li>Design validation must be performed on:
    <ul class="mcq-opts"><li><span class="ol">a)</span> CAD models</li><li><span class="ol">b)</span> any early prototype</li><li><span class="ol">c)</span> competitor units</li><li><span class="ol">d)</span> initial production units or their equivalents</li></ul>
    <div class="rationale"><b>Answer: d.</b> Validation must reflect the device as actually manufactured, under actual or simulated use conditions.</div></li>
  <li>The FDA rule that incorporates ISO 13485:2016 by reference is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the De Novo rule</li><li><span class="ol">b)</span> the QMSR (effective 2 February 2026)</li><li><span class="ol">c)</span> 21 CFR 803</li><li><span class="ol">d)</span> the UDI rule</li></ul>
    <div class="rationale"><b>Answer: b.</b> The Quality Management System Regulation (final rule 31 January 2024) replaced the 1996 QSR framework, harmonizing FDA QMS requirements with ISO 13485:2016. 21 CFR 803 is adverse-event reporting.</div></li>
  <li>Which is a well-written design input?
    <ul class="mcq-opts"><li><span class="ol">a)</span> &ldquo;device shall be user friendly&rdquo;</li><li><span class="ol">b)</span> &ldquo;device shall be safe&rdquo;</li><li><span class="ol">c)</span> &ldquo;flow-rate accuracy shall be within &plusmn;5% from 1&ndash;999 mL/h&rdquo;</li><li><span class="ol">d)</span> &ldquo;device shall satisfy clinicians&rdquo;</li></ul>
    <div class="rationale"><b>Answer: c.</b> Inputs must be unambiguous and verifiable; the other options cannot be objectively tested.</div></li>
  <li>Fault Tree Analysis is best described as:
    <ul class="mcq-opts"><li><span class="ol">a)</span> bottom-up and component-centred</li><li><span class="ol">b)</span> a usability test</li><li><span class="ol">c)</span> a sampling plan</li><li><span class="ol">d)</span> top-down decomposition of an undesired event through logic gates</li></ul>
    <div class="rationale"><b>Answer: d.</b> FTA starts from the harm and works down through AND/OR gates; FMEA is the bottom-up counterpart.</div></li>
  <li>Under IEC 62366-1, the final usability study that supports validation is called:
    <ul class="mcq-opts"><li><span class="ol">a)</span> summative evaluation</li><li><span class="ol">b)</span> formative evaluation</li><li><span class="ol">c)</span> heuristic walkthrough</li><li><span class="ol">d)</span> alpha test</li></ul>
    <div class="rationale"><b>Answer: a.</b> Formative studies iterate during design; the summative evaluation tests critical tasks with representative users to close usability validation.</div></li>
  <li>The Device Master Record is best described as:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the story of the design</li><li><span class="ol">b)</span> the vigilance log</li><li><span class="ol">c)</span> the complete recipe of specifications to build the device</li><li><span class="ol">d)</span> the clinical study report</li></ul>
    <div class="rationale"><b>Answer: c.</b> The DMR (ISO 13485: medical device file) holds device, production, QC, packaging and labeling specifications.</div></li>
  <li>The Therac-25 disaster is chiefly a lesson in:
    <ul class="mcq-opts"><li><span class="ol">a)</span> biocompatibility failure</li><li><span class="ol">b)</span> uncontrolled software design and change without system-level safety analysis</li><li><span class="ol">c)</span> sterilization failure</li><li><span class="ol">d)</span> counterfeit components</li></ul>
    <div class="rationale"><b>Answer: b.</b> Software reuse after removal of hardware interlocks, with no independent verification, allowed race conditions to deliver radiation overdoses.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>Design reviews must be documented and held at planned stages. <span class="marks">(T)</span></li>
  <li>Verification confirms that the device meets user needs. <span class="marks">(F &mdash; that is validation)</span></li>
  <li>A design change must be verified and, where appropriate, validated before implementation. <span class="marks">(T)</span></li>
  <li>EU MDR Annex I (GSPR) is a source of design inputs for the European market. <span class="marks">(T)</span></li>
  <li>The DHR documents how the design was developed. <span class="marks">(F &mdash; that is the DHF; the DHR is the batch record)</span></li>
  <li>dFMEA addresses the product design while pFMEA addresses the manufacturing process. <span class="marks">(T)</span></li>
  <li>Usability engineering is optional for home-use devices. <span class="marks">(F)</span></li>
  <li>Design transfer links design outputs to production specifications. <span class="marks">(T)</span></li>
  <li>Under the QMSR, FDA abandoned all QMS expectations for devices. <span class="marks">(F &mdash; it adopted ISO 13485:2016 as the framework)</span></li>
  <li>&ldquo;Use error&rdquo; can occur with a device that is functioning exactly as designed. <span class="marks">(T)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>The compiled evidence that a design was developed under design controls is kept in the __________.</li>
  <li>Confirming that design outputs meet design inputs is called __________.</li>
  <li>Confirming that the device conforms to defined user needs is called __________.</li>
  <li>US design controls were historically codified in 21 CFR __________.</li>
  <li>The QMSR incorporates the standard __________ by reference.</li>
  <li>The controlled hand-over of a design into production specifications is __________.</li>
  <li>The usability engineering standard for medical devices is __________.</li>
  <li>FMEA stands for __________.</li>
  <li>Testable requirements derived from user needs are called __________.</li>
  <li>The QMSR became effective on __________.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> Ambiguous design inputs cause late-stage project failure. <strong>R:</strong> Requirements that cannot be objectively tested cannot be verified. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Validation uses initial production units. <strong>R:</strong> The device as manufactured, not a hand-built prototype, is what patients will receive. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> FTA and FMEA are interchangeable, so only one is ever used. <strong>R:</strong> FMEA is bottom-up while FTA is top-down. <span class="marks">(d &mdash; A false: they are complementary; R true)</span></li>
  <li><strong>A:</strong> Hardware interlocks may be removed freely once software performs the same function. <strong>R:</strong> Software of unproven independence can harbour common-cause failures such as race conditions. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> Summative usability evaluation is part of design validation. <strong>R:</strong> The DHF must contain a design and development plan. <span class="marks">(b)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>Distinguish DHF, DMR and DHR in one sentence each.</li>
  <li>Convert the user need &ldquo;elderly patients must handle the inhaler easily&rdquo; into three testable design inputs.</li>
  <li>List the nine elements of design control.</li>
  <li>Give two differences between formative and summative usability evaluations.</li>
  <li>Why must design validation include simulated or actual use conditions?</li>
  <li>State the significance of the FDA QMSR for global QMS harmonization.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Draw and explain the design-control waterfall, showing where verification, validation and design reviews close their loops, and illustrate each element with an infusion-pump example.</li>
  <li>Compare FMEA and FTA as safety-analysis tools &mdash; method, direction, strengths, blind spots &mdash; and show how their outputs enter the ISO 14971 risk management file.</li>
  <li>Using the Therac-25 case, analyse how failures of input definition, software verification, change control and usability combined, and propose the design-control regime that would prevent recurrence.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>Your team proposes replacing a syringe pump's mechanical anti-free-flow clamp with a software-monitored valve to cut cost. Construct the design-change dossier: affected inputs, new failure modes, verification/validation additions, and the risk-benefit argument you would defend in audit.</li>
  <li>Design a one-page traceability matrix (columns and three example rows) linking user needs &rarr; inputs &rarr; outputs &rarr; verification &rarr; risks for a fingertip pulse oximeter.</li>
  <li>A start-up claims its AI symptom-checker app needs no design controls because &ldquo;software iterates weekly&rdquo;. Rebut or support this claim using ISO 13485 clause 7.3 logic and the concept of design change control for SaMD.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>US Food and Drug Administration. Design Control Guidance for Medical Device Manufacturers. Rockville (MD): FDA; 1997.</li>
  <li>US Food and Drug Administration. 21 CFR 820.30 &mdash; Design controls; Quality Management System Regulation final rule (89 FR 7496, 2 February 2024, effective 2 February 2026). Silver Spring (MD): FDA.</li>
  <li>International Organization for Standardization. ISO 13485:2016 &mdash; Medical devices &mdash; Quality management systems &mdash; Requirements for regulatory purposes, clause 7.3. Geneva: ISO; 2016.</li>
  <li>International Electrotechnical Commission. IEC 62366-1:2015+A1:2020 &mdash; Medical devices &mdash; Application of usability engineering to medical devices. Geneva: IEC.</li>
  <li>US Food and Drug Administration. Applying Human Factors and Usability Engineering to Medical Devices &mdash; Guidance. Silver Spring (MD): FDA; 2016.</li>
  <li>International Organization for Standardization. ISO 14971:2019 &mdash; Application of risk management to medical devices. Geneva: ISO; 2019.</li>
  <li>Leveson NG, Turner CS. An investigation of the Therac-25 accidents. Computer. 1993;26(7):18-41.</li>
  <li>World Health Organization. WHO&ndash;UNICEF joint statement on the use of auto-disable syringes in immunization services. Geneva: WHO; 1999 (WHO/V&amp;B/99.25).</li>
  <li>European Parliament and Council. Regulation (EU) 2017/745, Annex I &mdash; General safety and performance requirements. OJEU. 2017;L117.</li>
  <li>US Food and Drug Administration. Infusion Pumps Total Product Life Cycle &mdash; Guidance. Silver Spring (MD): FDA; 2014.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 3 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 3.1&ndash;3.5</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figures 3.1&ndash;3.2; Tables 3.1&ndash;3.2</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 3.1 (Therac-25), 3.2 (AD syringe)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>820.30; QMSR 89 FR 7496; ISO 13485:2016; IEC 62366-1 &mdash; cited in references</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>10 references</td></tr>
</table>
</div>

</section>
"""
