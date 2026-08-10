CH08_HTML = """
<section class="chapter" id="ch08" data-running="Chapter 8 · Risk Management — ISO 14971">

<div class="ch-opener">
  <div class="ch-kicker">Part III &middot; Manufacturing, Quality &amp; Safety &middot; Chapter 8</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">08</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Risk Management &mdash; ISO 14971</h1>
      <div class="ch-tagline">The risk management process &middot; hazard, hazardous situation, harm &middot; risk analysis, evaluation and control &middot; production and post-production feedback</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Define risk, hazard, hazardous situation and harm per ISO 14971:2019. <span class="lo-tag">CO1 &middot; Remember</span></li>
    <li>Describe the complete risk management process from plan to post-production. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Perform a risk analysis: intended use, hazard identification, risk estimation (P &times; S). <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Apply the risk-control option hierarchy and evaluate residual risk. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Construct and defend a risk acceptability matrix. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Evaluate benefit&ndash;risk determinations and the &ldquo;as far as possible&rdquo; demand of the EU MDR. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Explain risk vocabulary and process architecture</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Apply analysis, control and acceptability tools</td><td>L3</td><td>3, 4, 5</td></tr>
    <tr><td>CO3</td><td>Evaluate benefit&ndash;risk and regulatory variants</td><td>L5</td><td>6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">8.1</span>The Vocabulary of Risk</h2>
<span class="wframe">What</span>
<p class="lead">No medical device is risk-free; a scalpel cuts, an X-ray irradiates, an implant occupies living
tissue. The mature question is never &ldquo;is it safe?&rdquo; but &ldquo;are the risks acceptable in relation to the
benefit, and have they been reduced appropriately?&rdquo; <strong>ISO 14971:2019</strong> supplies the discipline and
the dictionary:</p>
<ul>
  <li><strong>Harm</strong> &mdash; injury or damage to health of people, or damage to property or environment;</li>
  <li><strong>Hazard</strong> &mdash; a potential source of harm (electrical energy, sharp edge, wrong software output, biological contamination);</li>
  <li><strong>Hazardous situation</strong> &mdash; the circumstance in which people are actually exposed to the hazard;</li>
  <li><strong>Risk</strong> &mdash; the combination of the <strong>probability of occurrence of harm (P)</strong> and its <strong>severity (S)</strong>;</li>
  <li><strong>Residual risk</strong> &mdash; what remains after controls;</li>
  <li><strong>Benefit&ndash;risk analysis</strong> &mdash; the judgement weighing residual risk against clinical benefit.</li>
</ul>
<p>The hazard&ndash;situation&ndash;harm chain matters in practice. Mains electricity inside a monitor is a hazard;
it becomes a hazardous situation only when insulation fails <em>and</em> someone touches an energised part;
harm follows with some probability. Controls can break the chain at any link &mdash; and the analysis must record
which link each control addresses (the foreseeable-event sequences of the standard's Annex C reasoning).</p>

<h2 class="sec"><span class="secnum">8.2</span>The Process, End to End</h2>
<span class="wframe">How &middot; When</span>
<div class="figure">
<svg viewBox="0 0 700 252" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <defs><marker id="a8" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0F4C5C"/></marker></defs>
  <g font-size="8.8" text-anchor="middle">
    <rect x="20" y="12" width="150" height="36" fill="#0F4C5C"/><text x="95" y="27" fill="#fff" font-weight="bold">Risk management plan</text><text x="95" y="40" fill="#BCD9E1">scope &middot; criteria &middot; responsibilities</text>
    <rect x="20" y="66" width="150" height="52" fill="#14537D"/><text x="95" y="82" fill="#fff" font-weight="bold">Risk analysis</text><text x="95" y="95" fill="#CFE3F0">intended use &amp; misuse &middot; hazard</text><text x="95" y="106" fill="#CFE3F0">identification &middot; estimate P &times; S</text>
    <rect x="20" y="136" width="150" height="36" fill="#2E7D96"/><text x="95" y="151" fill="#fff" font-weight="bold">Risk evaluation</text><text x="95" y="164" fill="#E2F1F5">against plan criteria</text>
    <rect x="240" y="66" width="190" height="106" fill="#E4EFF1" stroke="#0F4C5C"/>
    <text x="335" y="84" font-weight="bold" fill="#0F4C5C">Risk control (option hierarchy)</text>
    <text x="335" y="100" fill="#333">1. Inherently safe design &amp; manufacture</text>
    <text x="335" y="114" fill="#333">2. Protective measures (alarms, guards,</text>
    <text x="335" y="125" fill="#333">interlocks) in device or process</text>
    <text x="335" y="139" fill="#333">3. Information for safety (warnings,</text>
    <text x="335" y="150" fill="#333">labeling, training)</text>
    <text x="335" y="165" fill="#B4690E" font-weight="bold">verify implementation &amp; effectiveness</text>
    <rect x="480" y="12" width="200" height="52" fill="#1E6E4A"/><text x="580" y="30" fill="#fff" font-weight="bold">Overall residual risk &amp;</text><text x="580" y="43" fill="#fff" font-weight="bold">benefit&ndash;risk evaluation</text><text x="580" y="56" fill="#D9F0E4">disclose residual risks to users</text>
    <rect x="480" y="86" width="200" height="36" fill="#5C3A6E"/><text x="580" y="101" fill="#fff" font-weight="bold">Risk management review &amp; report</text><text x="580" y="114" fill="#E4D8EC">before release</text>
    <rect x="480" y="144" width="200" height="52" fill="#B4690E"/><text x="580" y="162" fill="#fff" font-weight="bold">Production &amp; post-production</text><text x="580" y="175" fill="#FBEFD9">complaints &middot; vigilance &middot; PMS &middot; trends</text><text x="580" y="188" fill="#FBEFD9">feed back into the file</text>
  </g>
  <g stroke="#0F4C5C" stroke-width="1.1" fill="none" marker-end="url(#a8)">
    <line x1="95" y1="48" x2="95" y2="62"/><line x1="95" y1="118" x2="95" y2="132"/>
    <line x1="170" y1="154" x2="236" y2="130"/><line x1="430" y1="100" x2="476" y2="50"/>
    <line x1="580" y1="64" x2="580" y2="82"/><line x1="580" y1="122" x2="580" y2="140"/>
  </g>
  <path d="M 480 180 C 300 235 120 210 90 176" stroke="#B4690E" stroke-width="1" fill="none" stroke-dasharray="4 3" marker-end="url(#a8)"/>
  <text x="280" y="225" font-size="8.4" fill="#B4690E" text-anchor="middle" font-weight="bold">the loop: field experience re-enters risk analysis for the device's whole life</text>
</svg>
<div class="figcaption"><b>Figure 8.1</b> &nbsp;The ISO 14971:2019 risk management process. Risk management is a lifetime activity: the file stays open as long as the device is on the market.</div>
</div>
<p>Everything is anchored by the <strong>risk management plan</strong> (which fixes, in advance, the criteria for
risk acceptability &mdash; so that acceptability cannot be re-negotiated after the results arrive) and archived
in the <strong>risk management file</strong>, the single traceable home of analyses, controls, verifications and
reviews. The concluding <strong>risk management report</strong> confirms the plan was executed, overall residual
risk is acceptable against clinical benefit, and production/post-production mechanisms are in place.</p>

<h2 class="sec"><span class="secnum">8.3</span>Risk Analysis and the Acceptability Matrix</h2>
<span class="wframe">How</span>
<p>Analysis begins with the device's <strong>intended use and reasonably foreseeable misuse</strong> &mdash; a syringe
will be recapped, a home nebuliser will be shared, a monitor's alarm will be silenced. Hazard identification
then sweeps systematic categories (energy, biological/chemical, operational/use, informational), typically
powered by the FMEA/FTA tools of Chapter 3 plus checklists from ISO/TR 24971, the standard's guidance
companion. For each hazardous situation, the team estimates <strong>P</strong> (often on a 5-level ordinal scale
anchored to quantitative ranges where data exist) and <strong>S</strong> (negligible &rarr; catastrophic), and plots
the pair on the pre-agreed matrix:</p>

<div class="tablewrap">
<div class="tabcaption"><b>Table 8.1</b> &nbsp;An illustrative 5&times;5 risk acceptability matrix (defined in the risk management plan)</div>
<table class="data">
  <tr><th>Probability &darr; / Severity &rarr;</th><th>Negligible</th><th>Minor</th><th>Serious</th><th>Critical</th><th>Catastrophic</th></tr>
  <tr><td class="rowhead">Frequent</td><td>R2</td><td>R3</td><td>R3</td><td>R3</td><td>R3</td></tr>
  <tr><td class="rowhead">Probable</td><td>R1</td><td>R2</td><td>R3</td><td>R3</td><td>R3</td></tr>
  <tr><td class="rowhead">Occasional</td><td>R1</td><td>R2</td><td>R2</td><td>R3</td><td>R3</td></tr>
  <tr><td class="rowhead">Remote</td><td>R1</td><td>R1</td><td>R2</td><td>R2</td><td>R3</td></tr>
  <tr><td class="rowhead">Improbable</td><td>R1</td><td>R1</td><td>R1</td><td>R2</td><td>R2</td></tr>
</table>
</div>
<p style="font-size:9pt;color:#5B6770;">R1 = acceptable; R2 = reduce as far as possible, justify residual; R3 = unacceptable without further control. The
matrix shape, scales and region boundaries are the manufacturer's documented policy decision &mdash; auditors check
that decisions follow the declared matrix, and that the matrix itself is clinically defensible.</p>

<h2 class="sec"><span class="secnum">8.4</span>Risk Control and Its Hierarchy</h2>
<span class="wframe">How &middot; Why</span>
<p>ISO 14971 imposes a strict <strong>order of preference</strong>: (1) <strong>inherently safe design</strong> &mdash; remove
the hazard or the exposure (a luer connector that physically cannot join an enteral line; limiting a
laser's maximum output below injury threshold); (2) <strong>protective measures</strong> &mdash; guards, interlocks,
alarms, redundancy that intervene when things go wrong; (3) <strong>information for safety</strong> &mdash; warnings,
contraindications, training. The hierarchy encodes hard experience: labels are the weakest control because
they depend on human attention at the worst moment. A control is not credited until its implementation
<em>and</em> effectiveness are verified &mdash; and each control is checked for the new risks it introduces (an
alarm added is an alarm-fatigue contribution made: the analysis iterates).</p>
<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight &middot; ALARP vs AFAP</div>
  <p>Older practice reduced risks &ldquo;as low as reasonably practicable&rdquo; (ALARP), admitting economic
  practicability. The <strong>EU MDR</strong> (Annex I, GSPR 2&ndash;4) demands reduction <strong>as far as possible</strong>
  (AFAP) &ldquo;without adversely affecting the benefit&ndash;risk ratio&rdquo; &mdash; cost alone cannot justify leaving a
  feasible control unimplemented. ISO 14971:2019 was drafted to be compatible with this stricter reading;
  manufacturers serving Europe write their plans accordingly.</p>
</div>

<h2 class="sec"><span class="secnum">8.5</span>Living With Risk: Production and Post-Production</h2>
<span class="wframe">When &middot; Where</span>
<p>Clause 10 of the standard is where many systems fail in practice: the manufacturer must actively collect
and review production data (SPC drifts, nonconformities) and post-production information (complaints,
vigilance reports, literature, registry signals &mdash; Chapter 12), ask whether any information changes the
risk estimates or reveals new hazards, and re-enter the process if it does. The metal-on-metal hip story
(Chapters 4&ndash;5) is the canonical example of post-production information overturning premarket estimates:
revision-registry data rewrote the probability column, and with it the acceptability of the entire product
category.</p>
<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Every adverse event a hospital pharmacist reports into MvPI (Chapter 12) lands, by design, in some
  manufacturer's clause-10 review. Under-reporting starves the loop: risk files remain confident because
  the data that would humble them was never filed. Reporting is not bureaucracy; it is the P in someone's
  P &times; S.</p>
</div>
<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>ISO 14971's separation of <em>hazard</em> from <em>hazardous situation</em> was borrowed from system-safety
  engineering in aviation and process industries. The same P &times; S logic that certifies an autopilot
  certifies an infusion pump &mdash; medicine imported half a century of other industries' accident lessons in
  one standard.</p>
</div>
<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>&ldquo;Risk file remediation&rdquo; became a small industry when the EU MDR raised the bar: thousands of legacy
  devices needed their MDD-era files rebuilt to 14971:2019 + AFAP logic. Consultancies still hire
  scientifically trained staff who can read a clinical literature base and defend a benefit&ndash;risk
  conclusion in front of a notified body.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 8.1 &middot; Infusion Pump Alarm Strategy &mdash; Controls That Create Risks</div>
  <div class="cs-body">
    <p>A pump maker, responding to over-infusion risk, layers protective measures: occlusion alarms, air-in-line
    alarms, drug-library soft and hard limits, and near-continuous audible alerts. Nurses in a 40-bed ICU now
    face hundreds of pump alarms per shift; alarm fatigue sets in, and a genuinely critical alarm is silenced
    with the reflexive keystroke used on the previous fifty nuisance alarms. A patient is harmed. The
    subsequent analysis reclassifies &ldquo;excessive alarm burden&rdquo; as a hazard in its own right, retunes
    thresholds, introduces alarm escalation and prioritisation per IEC 60601-1-8, and validates the strategy
    in simulated use.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Where in the ISO 14971 process should alarm-fatigue risk have first appeared?</li>
      <li>Why does the option hierarchy not simply mean &ldquo;add more protective measures&rdquo;?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) At risk-control verification: every control must be analysed for the risks it introduces; use-related
      hazard analysis (Chapter 3) should have modelled the ward-level alarm ecology, not the single pump.
      (2) Because controls interact and saturate the user; the hierarchy prefers inherent safety (better
      occlusion physics, smarter defaults) precisely because it does not tax human attention.</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 8.2 &middot; Building the Risk File for a Blood Glucose Meter</div>
  <div class="cs-body">
    <p>An Indian IVD firm builds the 14971 file for a home glucometer. Intended use: lay users, self-monitoring.
    Foreseeable misuse: expired strips, coded strips from other lots, testing with contaminated fingers.
    Hazards include erroneous high/low results (informational hazard) whose harm pathway runs through wrong
    insulin dosing. P is estimated from human-factors studies and literature; S from clinical consultation
    (severe hypoglycaemia = critical). Controls follow the hierarchy: strip auto-coding and expiry lockout
    (inherent), control-solution check prompts and implausible-value flags (protective), and only then label
    warnings. Residual risk is weighed against the overwhelming benefit of self-monitoring, disclosed in the
    IFU, and the file is wired to complaint trending &mdash; strip lot complaints trigger clause-10 review.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Why is an erroneous reading a hazard even though the meter &ldquo;works&rdquo; electrically?</li>
      <li>Trace one complete hazard &rarr; situation &rarr; harm chain and its control at each link.</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) ISO 14971 explicitly covers informational/output hazards: for a diagnostic, the dangerous output
      IS the wrong number. (2) Hazard: falsely low reading (degraded strip) &rarr; situation: user doses less
      insulin &rarr; harm: hyperglycaemia/DKA. Controls: expiry lockout (breaks hazard), implausible-value
      flag (breaks situation), IFU instruction to confirm symptoms vs reading (mitigates harm).</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>Risk = P &times; S; the chain hazard &rarr; hazardous situation &rarr; harm structures every analysis, and controls are credited against specific links.</li>
    <li>The process: plan (criteria fixed in advance) &rarr; analysis (intended use &amp; foreseeable misuse, hazard identification, estimation) &rarr; evaluation &rarr; control &rarr; overall residual risk &amp; benefit&ndash;risk &rarr; review/report &rarr; production &amp; post-production feedback &mdash; a whole-lifetime loop archived in the risk management file.</li>
    <li>The control hierarchy is mandatory in order: inherent safety, protective measures, information for safety; each control is verified for implementation, effectiveness and newly introduced risks.</li>
    <li>Acceptability matrices are the manufacturer's declared policy; the EU MDR's &ldquo;as far as possible&rdquo; standard forbids resting on cost-based ALARP arguments.</li>
    <li>Clause 10 makes surveillance data a formal input: registries, complaints and vigilance can &mdash; and do &mdash; overturn premarket risk estimates (metal-on-metal hips).</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Hazard / hazardous situation / harm</dt> <dd>&mdash; source of harm / exposure circumstance / the injury itself.</dd></div>
    <div class="kt-row"><dt>Risk (P &times; S)</dt> <dd>&mdash; probability of occurrence of harm combined with its severity.</dd></div>
    <div class="kt-row"><dt>Risk management plan / file / report</dt> <dd>&mdash; the criteria-setting, archival and concluding documents.</dd></div>
    <div class="kt-row"><dt>Foreseeable misuse</dt> <dd>&mdash; predictable use outside the intended use, in scope of analysis.</dd></div>
    <div class="kt-row"><dt>Inherent safety by design</dt> <dd>&mdash; first-preference control removing hazard or exposure.</dd></div>
    <div class="kt-row"><dt>Residual risk</dt> <dd>&mdash; risk remaining after controls, disclosed and weighed against benefit.</dd></div>
    <div class="kt-row"><dt>ALARP / AFAP</dt> <dd>&mdash; &ldquo;reasonably practicable&rdquo; vs the EU's stricter &ldquo;as far as possible&rdquo;.</dd></div>
    <div class="kt-row"><dt>ISO/TR 24971</dt> <dd>&mdash; guidance companion to ISO 14971.</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 8 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>Per ISO 14971, risk is the combination of:
    <ul class="mcq-opts"><li><span class="ol">a)</span> cost and benefit</li><li><span class="ol">b)</span> hazard and label</li><li><span class="ol">c)</span> detectability and severity</li><li><span class="ol">d)</span> probability of occurrence of harm and severity of that harm</li></ul>
    <div class="rationale"><b>Answer: d.</b> P &times; S is the definition; detectability belongs to FMEA's RPN, not to the ISO 14971 definition of risk.</div></li>
  <li>Mains voltage inside an ECG monitor is, in 14971 vocabulary, a:
    <ul class="mcq-opts"><li><span class="ol">a)</span> harm</li><li><span class="ol">b)</span> hazard</li><li><span class="ol">c)</span> hazardous situation</li><li><span class="ol">d)</span> residual risk</li></ul>
    <div class="rationale"><b>Answer: b.</b> It is a potential source of harm; exposure (touching an energised part after insulation failure) is the hazardous situation; electrocution is the harm.</div></li>
  <li>Risk acceptability criteria must be defined:
    <ul class="mcq-opts"><li><span class="ol">a)</span> in the risk management plan, before analysis</li><li><span class="ol">b)</span> after testing, when data are known</li><li><span class="ol">c)</span> by the notified body</li><li><span class="ol">d)</span> only for Class III devices</li></ul>
    <div class="rationale"><b>Answer: a.</b> Fixing criteria in advance prevents retro-fitting acceptability to whatever results emerge.</div></li>
  <li>The first-preference risk control option is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> warnings in the IFU</li><li><span class="ol">b)</span> user training</li><li><span class="ol">c)</span> inherently safe design and manufacture</li><li><span class="ol">d)</span> alarms</li></ul>
    <div class="rationale"><b>Answer: c.</b> The hierarchy runs design &rarr; protective measures &rarr; information for safety; labels are last because they depend on human attention.</div></li>
  <li>Reasonably foreseeable misuse:
    <ul class="mcq-opts"><li><span class="ol">a)</span> is excluded from analysis</li><li><span class="ol">b)</span> must be identified and analysed</li><li><span class="ol">c)</span> voids the warranty and the file</li><li><span class="ol">d)</span> applies only to home-use devices</li></ul>
    <div class="rationale"><b>Answer: b.</b> The standard requires analysis of intended use AND reasonably foreseeable misuse &mdash; recapping needles and alarm silencing are design inputs, not excuses.</div></li>
  <li>Under the EU MDR, risks must be reduced:
    <ul class="mcq-opts"><li><span class="ol">a)</span> as far as possible without adversely affecting the benefit&ndash;risk ratio</li><li><span class="ol">b)</span> as low as commercially convenient</li><li><span class="ol">c)</span> only below the R3 region</li><li><span class="ol">d)</span> until insurance approves</li></ul>
    <div class="rationale"><b>Answer: a.</b> GSPR 2 codifies AFAP; economic practicability alone cannot justify omitting a feasible control.</div></li>
  <li>A newly added alarm must itself be:
    <ul class="mcq-opts"><li><span class="ol">a)</span> exempt from analysis</li><li><span class="ol">b)</span> considered only at PMS</li><li><span class="ol">c)</span> analysed for the new risks it introduces (e.g., alarm fatigue)</li><li><span class="ol">d)</span> validated only electrically</li></ul>
    <div class="rationale"><b>Answer: c.</b> Every control is checked for introduced risks &mdash; the iterative core of the standard, dramatised by Case Study 8.1.</div></li>
  <li>The document confirming the plan was executed and overall residual risk is acceptable is the:
    <ul class="mcq-opts"><li><span class="ol">a)</span> quality manual</li><li><span class="ol">b)</span> DHF</li><li><span class="ol">c)</span> BER</li><li><span class="ol">d)</span> risk management report</li></ul>
    <div class="rationale"><b>Answer: d.</b> The report closes the premarket phase; the file remains open through clause 10 for the market life.</div></li>
  <li>Clause 10 of ISO 14971:2019 requires:
    <ul class="mcq-opts"><li><span class="ol">a)</span> annual recertification</li><li><span class="ol">b)</span> active collection and review of production and post-production information</li><li><span class="ol">c)</span> destruction of superseded analyses</li><li><span class="ol">d)</span> notarised matrices</li></ul>
    <div class="rationale"><b>Answer: b.</b> Field data must be evaluated for impact on risk estimates and new hazards &mdash; the mechanism that caught metal-on-metal hips.</div></li>
  <li>Which is an informational hazard?
    <ul class="mcq-opts"><li><span class="ol">a)</span> a falsely low glucometer reading</li><li><span class="ol">b)</span> a sharp housing edge</li><li><span class="ol">c)</span> leakage current</li><li><span class="ol">d)</span> EO residue</li></ul>
    <div class="rationale"><b>Answer: a.</b> For diagnostics, erroneous output is the hazard; its harm pathway runs through wrong clinical decisions.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>No medical device is entirely free of risk. <span class="marks">(T)</span></li>
  <li>The risk management file must remain active for the device's entire market life. <span class="marks">(T)</span></li>
  <li>Detectability is part of ISO 14971's definition of risk. <span class="marks">(F &mdash; that is FMEA's RPN; 14971 risk is P &times; S)</span></li>
  <li>A control is credited only after verification of implementation and effectiveness. <span class="marks">(T)</span></li>
  <li>Warnings in labeling are the most reliable class of risk control. <span class="marks">(F &mdash; they are the last resort)</span></li>
  <li>Users must be informed of significant residual risks. <span class="marks">(T)</span></li>
  <li>The acceptability matrix is prescribed identically for all manufacturers by ISO. <span class="marks">(F &mdash; it is the manufacturer's documented, defensible policy)</span></li>
  <li>Registry data can legitimately overturn premarket probability estimates. <span class="marks">(T)</span></li>
  <li>Benefit&ndash;risk analysis weighs overall residual risk against clinical benefit. <span class="marks">(T)</span></li>
  <li>ISO/TR 24971 is a sterilization standard. <span class="marks">(F &mdash; it is the guidance companion to ISO 14971)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>Risk is defined as the combination of __________ and __________.</li>
  <li>A potential source of harm is a __________.</li>
  <li>The circumstance exposing people to a hazard is a __________.</li>
  <li>Acceptability criteria are fixed in advance in the risk management __________.</li>
  <li>The first-preference control option is inherently safe __________.</li>
  <li>Risk remaining after controls is __________ risk.</li>
  <li>The EU MDR requires reduction of risks as far as __________.</li>
  <li>Guidance on applying ISO 14971 is given in ISO/TR __________.</li>
  <li>Production and post-production activities are clause __________ of ISO 14971:2019.</li>
  <li>Predictable use outside the intended use is called reasonably foreseeable __________.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> Labels are the weakest risk control. <strong>R:</strong> Information for safety depends on human attention at the moment of hazard. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Acceptability criteria may be revised after results if targets are missed. <strong>R:</strong> The plan is written before analysis begins. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> Adding protective measures can increase total system risk. <strong>R:</strong> Controls can introduce new hazards such as alarm fatigue. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> The risk management report ends the manufacturer's risk obligations. <strong>R:</strong> Clause 10 mandates lifetime production and post-production feedback. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> A diagnostic device that always powers on may still be hazardous. <strong>R:</strong> Erroneous output is itself a hazard with a clinical harm pathway. <span class="marks">(a)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>Define harm, hazard, hazardous situation and risk with one device example threading all four.</li>
  <li>List the stages of the ISO 14971 process in order.</li>
  <li>State the risk-control option hierarchy and why its order is mandatory.</li>
  <li>Distinguish ALARP from the EU MDR's AFAP requirement.</li>
  <li>What belongs in a risk management file?</li>
  <li>Give three post-production information sources feeding clause 10.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Describe the complete ISO 14971:2019 process with a diagram, explaining the role of the plan, file and report, and the lifetime feedback loop, illustrated on a home glucometer.</li>
  <li>Construct a 5&times;5 risk matrix for an infusion pump, populate it with five analysed hazardous situations, apply the control hierarchy to each, and present the residual-risk and benefit&ndash;risk conclusions.</li>
  <li>Using metal-on-metal hips and the alarm-fatigue case, analyse how post-production data and control side-effects challenge premarket risk files, and what organisational practices keep files honest.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>Your matrix rates a catastrophic-but-improbable failure R2 (acceptable with justification). A board member asks: &ldquo;would you sign if the patient were your child?&rdquo; Write the disciplined answer &mdash; defending or revising the matrix &mdash; using benefit&ndash;risk and AFAP reasoning.</li>
  <li>Design the clause-10 surveillance plan for a novel Class C ventilator in the Indian market: data sources, review cadence, trigger thresholds, and the pathway from signal to file revision to field action.</li>
  <li>An AI-based SaMD updates its model quarterly. Propose how the risk management file should handle a moving intended-performance baseline &mdash; what is re-analysed, what is re-verified, and what governance gate releases each update.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>International Organization for Standardization. ISO 14971:2019 &mdash; Medical devices &mdash; Application of risk management to medical devices. Geneva: ISO; 2019.</li>
  <li>International Organization for Standardization. ISO/TR 24971:2020 &mdash; Guidance on the application of ISO 14971. Geneva: ISO; 2020.</li>
  <li>European Parliament and Council. Regulation (EU) 2017/745, Annex I, GSPR 1&ndash;9. OJEU. 2017;L117.</li>
  <li>International Electrotechnical Commission. IEC 60601-1-8 &mdash; Alarm systems in medical electrical equipment. Geneva: IEC.</li>
  <li>US Food and Drug Administration. Factors to Consider Regarding Benefit-Risk in Medical Device Product Availability, Compliance, and Enforcement Decisions &mdash; Guidance. Silver Spring (MD): FDA; 2016.</li>
  <li>Association for the Advancement of Medical Instrumentation. AAMI TIR57/related risk guidance. Arlington (VA): AAMI.</li>
  <li>Leveson NG. Engineering a Safer World: Systems Thinking Applied to Safety. Cambridge (MA): MIT Press; 2011.</li>
  <li>Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 &mdash; essential principles (risk reduction requirements). New Delhi: MoHFW; 2017.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 8 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 8.1&ndash;8.5</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figure 8.1; Table 8.1</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 8.1 (alarm fatigue), 8.2 (glucometer risk file)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>ISO 14971:2019, ISO/TR 24971:2020, EU MDR Annex I &mdash; cited</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>8 references</td></tr>
</table>
</div>

</section>
"""
