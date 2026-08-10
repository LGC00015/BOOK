CH06_HTML = """
<section class="chapter" id="ch06" data-running="Chapter 6 · Manufacturing Technologies">

<div class="ch-opener">
  <div class="ch-kicker">Part III &middot; Manufacturing, Quality &amp; Safety &middot; Chapter 6</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">06</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Manufacturing Technologies &amp; Workflows</h1>
      <div class="ch-tagline">Cleanroom production &middot; molding, machining and additive manufacturing &middot; process validation (IQ/OQ/PQ) &middot; Industry 4.0</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Describe cleanroom classification (ISO 14644-1) and contamination control in device manufacturing. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Explain the principal forming technologies: injection molding, extrusion, machining, additive manufacturing. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Distinguish process verification from process validation and state when validation is mandatory. <span class="lo-tag">CO2 &middot; Understand</span></li>
    <li>Apply the IQ&ndash;OQ&ndash;PQ framework to a device manufacturing process. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Illustrate Industry 4.0 elements (IoT, digital twins, analytics) in medtech production. <span class="lo-tag">CO3 &middot; Understand</span></li>
    <li>Evaluate manufacturing strategy choices for an Indian device start-up. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Describe cleanroom and forming technologies</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Apply process validation methodology</td><td>L2&ndash;L3</td><td>3, 4</td></tr>
    <tr><td>CO3</td><td>Assess modern and strategic manufacturing options</td><td>L2&ndash;L5</td><td>5, 6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">6.1</span>What Makes Device Manufacturing Different</h2>
<span class="wframe">What &middot; Why</span>
<p class="lead">Device manufacturing spans injection-molded syringes made by the billion, hand-finished heart
valves made by the thousand, and patient-specific 3-D-printed implants made one at a time. What unifies
them is not technology but <strong>discipline</strong>: every process step that can affect safety or performance is
specified, controlled, monitored and &mdash; where its output cannot be fully verified &mdash; validated.</p>
<p>Three features distinguish medtech from general manufacturing: <strong>traceability</strong> (lot and unit-level
records, the DHR of Chapter 3, UDI of Chapter 10); <strong>contamination control</strong> (bioburden, particulates,
endotoxin); and <strong>change control</strong> &mdash; a resin substitution that would be routine in consumer goods is a
regulated event in a device plant (Chapter 5's case study made the point biologically).</p>

<h2 class="sec"><span class="secnum">6.2</span>Cleanroom Manufacturing</h2>
<span class="wframe">Where &middot; How</span>
<p>Products that will be sterilised &mdash; and especially those that cannot tolerate high bioburden &mdash; are made
in <strong>cleanrooms</strong>, classified by airborne particle concentration under <strong>ISO 14644-1</strong>. The class
number is the decadic exponent of permitted particles &ge;0.1 &micro;m per m&sup3;; practically, device assembly
commonly runs in <strong>ISO Class 7</strong> (&le;352,000 particles &ge;0.5 &micro;m/m&sup3;) or <strong>Class 8</strong>, with
Class 5 laminar-flow zones for critical operations. Control rests on HEPA-filtered air with defined air
changes and pressure cascades (cleanest room most positive), gowning discipline, material airlocks,
cleaning/disinfection programmes, and <strong>environmental monitoring</strong> &mdash; particle counts, settle and
contact plates for viable organisms, personnel monitoring &mdash; trended against alert and action limits.
Bioburden of product before sterilization (ISO 11737-1) is itself a monitored quality attribute, because
sterilization validation (Chapter 10) assumes it.</p>

<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Hospital-acquired infections from intrinsically contaminated devices are rare precisely because of
  this architecture &mdash; when it fails, the consequences are outbreaks traced to single plants, which is why
  regulators inspect environmental-monitoring trend data, not just certificates.</p>
</div>

<h2 class="sec"><span class="secnum">6.3</span>Forming and Assembly Technologies</h2>
<span class="wframe">How</span>
<div class="tablewrap">
<div class="tabcaption"><b>Table 6.1</b> &nbsp;Principal manufacturing technologies in medtech</div>
<table class="data">
  <tr><th style="width:40mm;">Technology</th><th>Essence</th><th>Typical device outputs</th></tr>
  <tr><td class="rowhead">Injection molding</td><td>Molten polymer forced into precision molds; multi-cavity tooling; validated cycle parameters</td><td>Syringes, IV components, housings, labware</td></tr>
  <tr><td class="rowhead">Extrusion</td><td>Continuous profile through a die; multi-lumen and co-extrusion capability</td><td>Catheter tubing, drainage tubes, guidewire jackets</td></tr>
  <tr><td class="rowhead">CNC machining</td><td>Subtractive precision from implant alloys and PEEK</td><td>Bone plates, screws, hip/knee components, surgical instruments</td></tr>
  <tr><td class="rowhead">Additive manufacturing (3-D printing)</td><td>Layer-wise builds: SLS/SLM/EBM for Ti, SLA/FDM for polymers; enables lattices and patient-specific geometry</td><td>Cranial plates, acetabular cups with porous lattice, surgical guides, anatomical models</td></tr>
  <tr><td class="rowhead">Micro-fabrication &amp; electronics</td><td>SMT assembly, wire bonding, hermetic sealing, conformal coating</td><td>Pacemakers, sensors, diagnostic instruments</td></tr>
  <tr><td class="rowhead">Textile &amp; braiding</td><td>Weaving/braiding/knitting of fibres</td><td>Vascular grafts, stent braids, meshes, sutures</td></tr>
  <tr><td class="rowhead">Joining &amp; finishing</td><td>Ultrasonic/laser welding, adhesive bonding (UV-cure), solvent bonding; passivation, electropolishing</td><td>Fluid-path assemblies, needle hubs, implant surfaces</td></tr>
</table>
</div>
<p>Additive manufacturing deserves its own note: it collapses tooling cost and enables porous structures no
mold can make, but it moves the quality burden onto <strong>powder control, build-parameter validation and
post-processing</strong> (HIP, heat treatment, powder removal from lattices) &mdash; the subjects of dedicated FDA
guidance on 3-D-printed devices and of rapidly growing ISO/ASTM 52900-series standards.</p>

<h2 class="sec"><span class="secnum">6.4</span>Process Verification vs Process Validation &mdash; and IQ/OQ/PQ</h2>
<span class="wframe">How &middot; Why</span>
<p>If a process output can be <strong>fully verified</strong> by subsequent inspection or test (a machined
dimension, measured 100%), verification may suffice. Where it cannot &mdash; sterilization, welding, sealing,
molding of internal structures, lyophilisation, software builds &mdash; the process must be <strong>validated</strong>:
objective evidence that it consistently produces conforming output. ISO 13485 (clause 7.5.6) and the QMSR
both mandate this; the classic methodology, from GHTF process-validation guidance, is the
<strong>IQ&ndash;OQ&ndash;PQ</strong> ladder:</p>

<div class="figure">
<svg viewBox="0 0 700 150" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <defs><marker id="a6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0F4C5C"/></marker></defs>
  <g font-size="9" text-anchor="middle">
    <rect x="20" y="30" width="190" height="62" fill="#E4EFF1" stroke="#0F4C5C"/>
    <text x="115" y="48" font-weight="bold" fill="#0F4C5C">IQ &middot; Installation Qualification</text>
    <text x="115" y="62" fill="#333">Equipment installed correctly:</text>
    <text x="115" y="74" fill="#333">utilities, calibration, software,</text>
    <text x="115" y="86" fill="#333">documentation, safety features</text>
    <rect x="255" y="30" width="190" height="62" fill="#E4EFF1" stroke="#0F4C5C"/>
    <text x="350" y="48" font-weight="bold" fill="#0F4C5C">OQ &middot; Operational Qualification</text>
    <text x="350" y="62" fill="#333">Process works across worst-case</text>
    <text x="350" y="74" fill="#333">parameter windows; challenge</text>
    <text x="350" y="86" fill="#333">limits define the operating space</text>
    <rect x="490" y="30" width="190" height="62" fill="#E4EFF1" stroke="#0F4C5C"/>
    <text x="585" y="48" font-weight="bold" fill="#0F4C5C">PQ &middot; Performance Qualification</text>
    <text x="585" y="62" fill="#333">Consistency under real production:</text>
    <text x="585" y="74" fill="#333">typically &ge;3 consecutive successful</text>
    <text x="585" y="86" fill="#333">runs with routine staff &amp; materials</text>
  </g>
  <g stroke="#0F4C5C" stroke-width="1.2" fill="none" marker-end="url(#a6)">
    <line x1="210" y1="61" x2="251" y2="61"/><line x1="445" y1="61" x2="486" y2="61"/>
  </g>
  <text x="350" y="122" font-size="8.6" fill="#5B6770" text-anchor="middle">Maintained by change control, revalidation triggers, and continued process monitoring (SPC)</text>
</svg>
<div class="figcaption"><b>Figure 6.1</b> &nbsp;The IQ&ndash;OQ&ndash;PQ process validation ladder (GHTF/SG3 methodology). Validation is a lifecycle: change control and statistical monitoring keep the validated state alive.</div>
</div>

<p>Statistical thinking pervades the workflow: sampling plans (ISO 2859/ANSI Z1.4), <strong>statistical process
control</strong> charts on critical parameters, and capability indices (C<sub>p</sub>, C<sub>pk</sub>) demonstrating that
the process spread fits the specification. A C<sub>pk</sub> &ge; 1.33 is a common minimum expectation for
critical characteristics.</p>

<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight</div>
  <p>India's MDR 2017 ties manufacturing licences to site-specific QMS compliance audited against the
  <strong>Fifth Schedule</strong>; notified bodies under the EU MDR and FDA investigators under the QMSR audit the
  same substance &mdash; validation master plans, IQ/OQ/PQ protocols and reports, and the change-control trail.
  &ldquo;We have always run it this way&rdquo; is not evidence; a signed PQ report is.</p>
</div>

<h2 class="sec"><span class="secnum">6.5</span>Industry 4.0 in Medtech</h2>
<span class="wframe">When &middot; Where</span>
<p>The fourth industrial revolution reaches device plants as connected, data-rich production:</p>
<ul>
  <li><strong>IoT-instrumented equipment</strong> streaming molding pressures, torque curves and environmental data
  into historians &mdash; every unit's process fingerprint attached to its DHR;</li>
  <li><strong>Digital twins</strong> &mdash; simulation models of processes or products used to explore parameter windows
  before physical OQ, and to predict maintenance;</li>
  <li><strong>Machine vision and AI inspection</strong> replacing fatigue-prone human visual checks on needles,
  ampoules and printed labels;</li>
  <li><strong>Predictive analytics</strong> on trend data catching drifts before specification breach &mdash; SPC at
  machine speed;</li>
  <li><strong>Flexible automation</strong> &mdash; cobots for assembly and packing, e-batch records replacing paper.</li>
</ul>
<p>The regulatory frame keeps pace: computerised systems used in production and quality must themselves be
validated (software validation expectations under ISO 13485 and FDA's computer software assurance
thinking), and data integrity principles (ALCOA+) apply to machine-generated records as much as human ones.</p>

<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>India's PLI-supported plants (Chapter 1) were built straight into the Industry 4.0 era &mdash; new imaging
  and stent lines with e-batch records and analytics from day one. For pharmacy graduates, this multiplies
  roles at the manufacturing&ndash;quality&ndash;data interface: validation engineer, QMS data analyst, e-QMS
  administrator.</p>
</div>
<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>A modern multi-cavity syringe mold can produce over a hundred barrels per cycle at cycles under ten
  seconds &mdash; a single machine making several hundred million units a year. At that scale, a process drift
  of hours before detection is a recall of millions; hence sensors, SPC and automated rejection.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 6.1 &middot; Validating the Seal &mdash; A Pouch Sealing Line</div>
  <div class="cs-body">
    <p>A manufacturer of sterile dressing kits installs a new rotary heat-sealer for Tyvek pouches. Seal
    strength cannot be 100% verified &mdash; testing is destructive &mdash; so the process must be validated. IQ
    documents installation, utilities and calibrated instrumentation. OQ maps the parameter space:
    temperature, pressure and dwell are challenged at worst-case corners; seal strength (peel testing per
    ASTM F88) and integrity (dye penetration per ASTM F1929) define the window. PQ runs three full
    production shifts with routine operators and materials, sampling seals across the run. The validated
    window enters the DMR; sealer parameters are alarmed; any excursion triggers nonconformance review.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Why is destructive-only testability the trigger for validation here?</li>
      <li>The purchasing team proposes a cheaper pouch supplier. What must happen before first use?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Full verification would destroy every unit; only process evidence can assure the unsampled
      majority. (2) Change control: supplier qualification, material equivalence review, and at minimum a
      bracketing revalidation (OQ challenge/PQ runs) with the new material &mdash; sterile-barrier integrity is a
      patient-safety characteristic (Chapter 10).</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 6.2 &middot; 3-D-Printed Titanium Implants at AMTZ</div>
  <div class="cs-body">
    <p>An Indian start-up uses shared electron-beam-melting capacity at a medtech park to print
    patient-specific titanium cranial plates from CT scans. The workflow chains design (segmentation &rarr;
    CAD), build (validated parameter sets, powder lot control, witness coupons per build), post-processing
    (powder removal, heat treatment, surface finish), and verification (dimensional scan against the design,
    coupon mechanical tests). Because each device is unique, validation attaches to the <em>process
    envelope</em> &mdash; a defined geometry family and parameter set &mdash; rather than to a single design, mirroring
    the logic of FDA's additive manufacturing guidance.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>What does &ldquo;worst case&rdquo; mean in OQ for a patient-specific product family?</li>
      <li>Which shared-infrastructure risks must the start-up's quality agreement with the park cover?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Envelope extremes: thinnest walls, largest spans, most complex lattices the family permits &mdash;
      validated once, checked per build by coupons. (2) Powder cross-contamination between users, machine
      maintenance/calibration records, environmental control and data ownership of build logs &mdash; supplier
      controls under ISO 13485 clause 7.4.</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>Device manufacturing is defined by traceability, contamination control and change control, whatever the forming technology.</li>
    <li>Cleanrooms are classified under ISO 14644-1; device assembly typically runs at ISO 7&ndash;8 with monitored particles, viables and pressure cascades; pre-sterilization bioburden is a controlled attribute.</li>
    <li>Core technologies: injection molding, extrusion, CNC machining, additive manufacturing, electronics assembly, braiding/textiles, welding and bonding &mdash; each with characteristic critical parameters.</li>
    <li>Processes whose output cannot be fully verified must be validated: IQ (installed right) &rarr; OQ (works across worst-case windows) &rarr; PQ (consistent in real production), maintained by change control and SPC.</li>
    <li>Industry 4.0 brings IoT process fingerprints, digital twins, AI inspection and e-records &mdash; with computerised-system validation and ALCOA+ data integrity as the regulatory counterpart.</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Cleanroom class (ISO 14644-1)</dt> <dd>&mdash; airborne particulate classification of controlled environments.</dd></div>
    <div class="kt-row"><dt>Bioburden</dt> <dd>&mdash; viable microbial load on product before sterilization (ISO 11737-1).</dd></div>
    <div class="kt-row"><dt>Process validation</dt> <dd>&mdash; documented evidence a process consistently yields conforming output.</dd></div>
    <div class="kt-row"><dt>IQ / OQ / PQ</dt> <dd>&mdash; installation, operational and performance qualification.</dd></div>
    <div class="kt-row"><dt>SPC / C<sub>pk</sub></dt> <dd>&mdash; statistical process control; capability index of process spread vs specification.</dd></div>
    <div class="kt-row"><dt>Additive manufacturing</dt> <dd>&mdash; layer-wise fabrication (SLM/EBM/SLA/FDM) enabling patient-specific devices.</dd></div>
    <div class="kt-row"><dt>Digital twin</dt> <dd>&mdash; simulation counterpart of a process or product used for prediction.</dd></div>
    <div class="kt-row"><dt>ALCOA+</dt> <dd>&mdash; data integrity attributes (attributable, legible, contemporaneous, original, accurate, plus complete/consistent/enduring/available).</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 6 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>Cleanrooms for device manufacturing are classified under:
    <ul class="mcq-opts"><li><span class="ol">a)</span> ISO 13485</li><li><span class="ol">b)</span> ISO 11607</li><li><span class="ol">c)</span> ISO 14644-1</li><li><span class="ol">d)</span> IEC 60601</li></ul>
    <div class="rationale"><b>Answer: c.</b> ISO 14644-1 classifies air cleanliness by particle concentration; 13485 is the QMS, 11607 packaging, 60601 electrical safety.</div></li>
  <li>Process validation is mandatory when:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the output cannot be fully verified by subsequent inspection or test</li><li><span class="ol">b)</span> the process is automated</li><li><span class="ol">c)</span> the device is Class A</li><li><span class="ol">d)</span> production exceeds one million units</li></ul>
    <div class="rationale"><b>Answer: a.</b> The verifiability criterion (ISO 13485 7.5.6) decides &mdash; sealing, welding and sterilization are classic validated processes regardless of volume or class.</div></li>
  <li>OQ primarily establishes:
    <ul class="mcq-opts"><li><span class="ol">a)</span> that equipment is installed to specification</li><li><span class="ol">b)</span> that the process performs across worst-case parameter windows</li><li><span class="ol">c)</span> long-term consistency with routine staff</li><li><span class="ol">d)</span> supplier pricing</li></ul>
    <div class="rationale"><b>Answer: b.</b> IQ covers installation; OQ challenges the limits of the operating window; PQ proves consistency under real production conditions.</div></li>
  <li>A C<sub>pk</sub> of 1.33 for a critical dimension indicates:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the process is out of control</li><li><span class="ol">b)</span> 33% defect rate</li><li><span class="ol">c)</span> calibration is overdue</li><li><span class="ol">d)</span> the process spread fits the specification with a commonly accepted capability margin</li></ul>
    <div class="rationale"><b>Answer: d.</b> C<sub>pk</sub> &ge;1.33 (&asymp;4&sigma; to nearest limit) is a customary minimum for critical characteristics.</div></li>
  <li>Which technology most naturally produces porous ingrowth lattices in titanium implants?
    <ul class="mcq-opts"><li><span class="ol">a)</span> injection molding</li><li><span class="ol">b)</span> extrusion</li><li><span class="ol">c)</span> additive manufacturing (SLM/EBM)</li><li><span class="ol">d)</span> braiding</li></ul>
    <div class="rationale"><b>Answer: c.</b> Powder-bed fusion builds internal lattice geometries no subtractive or molding process can form.</div></li>
  <li>Pre-sterilization microbial load on product is called:
    <ul class="mcq-opts"><li><span class="ol">a)</span> endotoxin</li><li><span class="ol">b)</span> bioburden</li><li><span class="ol">c)</span> particulate matter</li><li><span class="ol">d)</span> pyrogen</li></ul>
    <div class="rationale"><b>Answer: b.</b> Bioburden (ISO 11737-1) is the input assumption of every sterilization validation; endotoxin/pyrogen are distinct attributes.</div></li>
  <li>Catheter tubing with multiple lumens is characteristically produced by:
    <ul class="mcq-opts"><li><span class="ol">a)</span> (co-)extrusion</li><li><span class="ol">b)</span> CNC machining</li><li><span class="ol">c)</span> compression molding</li><li><span class="ol">d)</span> casting</li></ul>
    <div class="rationale"><b>Answer: a.</b> Multi-lumen dies in continuous extrusion define catheter cross-sections; machining polymers to such geometry is impractical.</div></li>
  <li>ALCOA+ principles govern:
    <ul class="mcq-opts"><li><span class="ol">a)</span> cleanroom gowning</li><li><span class="ol">b)</span> alloy composition</li><li><span class="ol">c)</span> shipping conditions</li><li><span class="ol">d)</span> data integrity of records, including machine-generated ones</li></ul>
    <div class="rationale"><b>Answer: d.</b> Attributable, legible, contemporaneous, original, accurate (+complete, consistent, enduring, available) applies to e-batch records and sensor data alike.</div></li>
  <li>The pressure cascade in a cleanroom suite ensures:
    <ul class="mcq-opts"><li><span class="ol">a)</span> faster molding cycles</li><li><span class="ol">b)</span> lower energy use</li><li><span class="ol">c)</span> air flows from cleaner to less clean spaces</li><li><span class="ol">d)</span> higher humidity</li></ul>
    <div class="rationale"><b>Answer: c.</b> Positive differential pressure in cleaner rooms prevents ingress of contaminated air at doorways and hatches.</div></li>
  <li>For a patient-specific 3-D-printed implant family, validation attaches to:
    <ul class="mcq-opts"><li><span class="ol">a)</span> each individual device design</li><li><span class="ol">b)</span> a defined process envelope (geometry family + parameter set)</li><li><span class="ol">c)</span> the CT scanner</li><li><span class="ol">d)</span> nothing &mdash; custom devices are exempt</li></ul>
    <div class="rationale"><b>Answer: b.</b> The envelope approach, reflected in FDA's additive manufacturing guidance, validates worst-case geometry/parameters once, with per-build coupons as ongoing evidence.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>Device assembly commonly occurs in ISO Class 7 or 8 cleanrooms with Class 5 zones for critical steps. <span class="marks">(T)</span></li>
  <li>A process whose output is 100% verifiable must still always be validated. <span class="marks">(F &mdash; verification may suffice)</span></li>
  <li>PQ typically includes at least three consecutive successful production runs. <span class="marks">(T)</span></li>
  <li>Seal-strength testing of pouches is destructive, which is why sealing is a validated process. <span class="marks">(T)</span></li>
  <li>Environmental monitoring measures only non-viable particles. <span class="marks">(F &mdash; viable monitoring by settle/contact plates is integral)</span></li>
  <li>Digital twins can be used to explore parameter windows before physical OQ. <span class="marks">(T)</span></li>
  <li>Computerised systems used in production must themselves be validated. <span class="marks">(T)</span></li>
  <li>Additive manufacturing eliminates the need for post-processing of titanium implants. <span class="marks">(F &mdash; powder removal, heat treatment and finishing are critical)</span></li>
  <li>SPC charts on critical parameters help detect drift before specification breach. <span class="marks">(T)</span></li>
  <li>Change control applies to suppliers' material changes only if the supplier agrees. <span class="marks">(F &mdash; the manufacturer's QMS must capture and control such changes)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>Cleanroom air cleanliness is classified under ISO __________.</li>
  <li>Viable microbial load on product before sterilization is called __________.</li>
  <li>The three-step process validation ladder is IQ, OQ and __________.</li>
  <li>A common minimum capability index for critical characteristics is C<sub>pk</sub> &ge; __________.</li>
  <li>Powder-bed fusion of titanium implants uses SLM or __________ technology.</li>
  <li>Continuous multi-lumen catheter tubing is produced by __________.</li>
  <li>The data integrity acronym for regulated records is __________.</li>
  <li>The GHTF study group that authored process validation guidance is SG__________.</li>
  <li>Air moves from cleaner to less clean rooms because of the pressure __________.</li>
  <li>Pouch seal integrity by dye penetration is tested per ASTM __________.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> Sterilization is always treated as a validated process. <strong>R:</strong> Sterility of each unit cannot be verified without destroying it. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> OQ challenges worst-case corners of the parameter window. <strong>R:</strong> PQ uses routine operators and materials. <span class="marks">(b)</span></li>
  <li><strong>A:</strong> A validated process may drift out of its validated state over time. <strong>R:</strong> SPC monitoring and revalidation triggers exist for exactly this reason. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Machine-generated data are exempt from data-integrity expectations. <strong>R:</strong> ALCOA+ applies to all GxP records regardless of origin. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> Patient-specific implants can never be manufactured under a validated process. <strong>R:</strong> Validation can attach to a process envelope covering a geometry family. <span class="marks">(d)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>List four elements of cleanroom contamination control.</li>
  <li>State the verifiability rule deciding between process verification and validation, with two examples each.</li>
  <li>Define IQ, OQ and PQ in one sentence each.</li>
  <li>Name three quality risks specific to additive manufacturing and their controls.</li>
  <li>What is a pressure cascade and why is it used?</li>
  <li>Give three Industry 4.0 applications in device production with their regulatory counterpart.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Describe the manufacturing workflow of a sterile disposable syringe from resin to packed product: technologies, cleanroom environment, in-process controls, and the validated processes involved.</li>
  <li>Explain process validation methodology (IQ/OQ/PQ) in detail using a pouch-sealing example, including worst-case rationale, sampling, acceptance criteria, and lifecycle maintenance of the validated state.</li>
  <li>Assess how Industry 4.0 changes device manufacturing quality &mdash; opportunities, new risks (data integrity, software validation), and the skills it demands of quality professionals.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>Your molding line's C<sub>pk</sub> for a critical flange dimension fell from 1.8 to 1.1 over three months without alarms triggering. Design the investigation and the interim product-disposition strategy.</li>
  <li>An Indian start-up must choose between building an in-house ISO 7 cleanroom and contracting a park-based manufacturer for its Class B catheter. Construct the decision matrix: cost, control, regulatory responsibility, scale-up.</li>
  <li>Propose the validation strategy for an AI vision system replacing human inspectors on needle-tip defects: dataset governance, acceptance criteria versus human baseline, and change control for model updates.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>International Organization for Standardization. ISO 14644-1:2015 &mdash; Cleanrooms and associated controlled environments &mdash; Part 1: Classification of air cleanliness by particle concentration. Geneva: ISO; 2015.</li>
  <li>International Organization for Standardization. ISO 13485:2016, clauses 6.4, 7.5 &mdash; production and service provision. Geneva: ISO; 2016.</li>
  <li>Global Harmonization Task Force. Quality Management Systems &mdash; Process Validation Guidance (GHTF/SG3/N99-10:2004, Edition 2). GHTF; 2004.</li>
  <li>International Organization for Standardization. ISO 11737-1:2018 &mdash; Sterilization of health care products &mdash; Microbiological methods &mdash; Part 1: Determination of bioburden. Geneva: ISO; 2018.</li>
  <li>US Food and Drug Administration. Technical Considerations for Additive Manufactured Medical Devices &mdash; Guidance. Silver Spring (MD): FDA; 2017.</li>
  <li>ISO/ASTM 52900 series &mdash; Additive manufacturing &mdash; General principles and vocabulary. Geneva/West Conshohocken: ISO/ASTM.</li>
  <li>ASTM International. F88/F88M &mdash; Seal strength of flexible barrier materials; F1929 &mdash; Detecting seal leaks by dye penetration. West Conshohocken (PA): ASTM.</li>
  <li>Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 &mdash; Fifth Schedule (QMS). New Delhi: MoHFW; 2017.</li>
  <li>US Food and Drug Administration. Computer Software Assurance for Production and Quality System Software &mdash; Draft Guidance. Silver Spring (MD): FDA; 2022.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 6 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 6.1&ndash;6.5</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figure 6.1; Table 6.1</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 6.1 (pouch sealing), 6.2 (3-D printed implants)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>ISO 14644-1, GHTF/SG3/N99-10, ISO 11737-1, ASTM F88/F1929 &mdash; cited</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>9 references</td></tr>
</table>
</div>

</section>
"""
