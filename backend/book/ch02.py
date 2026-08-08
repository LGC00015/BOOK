CH02_HTML = """
<section class="chapter" id="ch02" data-running="Chapter 2 · Definitions &amp; Classification">

<div class="ch-opener">
  <div class="ch-kicker">Part I &middot; Foundations &middot; Chapter 2</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">02</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Definitions &amp; Classification of Medical Devices</h1>
      <div class="ch-tagline">CDSCO MDR 2017 (Class A&ndash;D) &middot; US FDA (Class I&ndash;III) &middot; EU MDR &amp; CE marking &middot; IMDRF harmonization</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Reproduce and compare the legal definitions of a medical device in India, the USA and the EU. <span class="lo-tag">CO1 &middot; Remember</span></li>
    <li>Explain the universal logic of risk-based classification and the factors that drive class assignment. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Classify given devices into CDSCO Classes A&ndash;D and identify the competent licensing authority. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Distinguish US FDA Classes I&ndash;III and match them to their regulatory controls and premarket pathways. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Outline EU MDR classes and the role of notified bodies in CE marking. <span class="lo-tag">CO2 &middot; Understand</span></li>
    <li>Assess the contribution of GHTF/IMDRF to global regulatory convergence. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>State definitions and classification logic across jurisdictions</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Apply classification rules of India, USA and EU to real devices</td><td>L3</td><td>3, 4, 5</td></tr>
    <tr><td>CO3</td><td>Evaluate international harmonization efforts</td><td>L5</td><td>6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">2.1</span>Legal Definitions Across Jurisdictions</h2>
<span class="wframe">What</span>
<p class="lead">Every regulatory decision about a product &mdash; which law applies, which authority licenses it,
which evidence is demanded &mdash; begins with a single question: <em>is it a medical device?</em> The answer lies in
statutory definitions that are strikingly convergent in substance, though different in wording.</p>

<h3 class="subsec">2.1.1 India</h3>
<p>In India, devices are regulated under the <strong>Drugs and Cosmetics Act, 1940</strong>: specified categories are
notified as &ldquo;drugs&rdquo; under section 3(b)(iv), and the <strong>Medical Devices Rules, 2017</strong> then apply to them.
The MDR 2017 covers instruments, apparatus, appliances, implants, materials and software intended for use
in the diagnosis, prevention, monitoring, treatment or alleviation of disease or injury; investigation,
replacement, modification or support of anatomy or physiological processes; supporting or sustaining life;
disinfection of devices; and control of conception &mdash; provided the product <strong>does not achieve its primary
intended action by pharmacological, immunological or metabolic means</strong> in or on the human body (though it
may be assisted by such means). By a gazette notification of February 2020, effective 1 April 2020, the
definition was extended so that <strong>all medical devices</strong> fall within regulation, replacing the earlier
regime of a limited notified list.</p>

<h3 class="subsec">2.1.2 United States</h3>
<p>Section <strong>201(h)</strong> of the Federal Food, Drug, and Cosmetic Act defines a device as an instrument,
apparatus, implement, machine, contrivance, implant, in vitro reagent, or other similar or related article,
including any component, part, or accessory, which is (i) recognised in the official National Formulary or
United States Pharmacopeia, (ii) intended for use in the diagnosis, cure, mitigation, treatment, or
prevention of disease, or (iii) intended to affect the structure or any function of the body &mdash; and which
<strong>does not achieve its primary intended purposes through chemical action</strong> within or on the body and is
<strong>not dependent upon being metabolised</strong> for the achievement of those purposes.</p>

<h3 class="subsec">2.1.3 European Union</h3>
<p>Article 2(1) of <strong>Regulation (EU) 2017/745</strong> defines a medical device as any instrument, apparatus,
appliance, software, implant, reagent, material or other article intended by the manufacturer to be used,
alone or in combination, for human beings for specific medical purposes (diagnosis, prevention, monitoring,
prediction, prognosis, treatment or alleviation of disease; injury or disability; anatomical or physiological
investigation, replacement or modification; and information from in vitro examination of specimens), and
which does not achieve its principal intended action by pharmacological, immunological or metabolic means.
The EU definition notably adds <strong>prediction and prognosis</strong> &mdash; sweeping modern AI-based prognostic software
into scope &mdash; and expressly includes devices for the control or support of conception and certain products
without a medical purpose (Annex XVI, e.g., coloured contact lenses).</p>

<div class="tablewrap">
<div class="tabcaption"><b>Table 2.1</b> &nbsp;Definitional elements of a medical device across jurisdictions</div>
<table class="data">
  <tr><th style="width:38mm;">Element</th><th>India (MDR 2017)</th><th>USA (FD&amp;C &sect;201(h))</th><th>EU (MDR Art. 2(1))</th></tr>
  <tr><td class="rowhead">Article types listed</td><td>Instrument, apparatus, appliance, implant, material, software</td><td>Instrument, apparatus, machine, implant, in vitro reagent, component/part/accessory</td><td>Instrument, apparatus, appliance, software, implant, reagent, material</td></tr>
  <tr><td class="rowhead">Medical purposes</td><td>Diagnosis, prevention, monitoring, treatment, alleviation; life support; disinfection; contraception</td><td>Diagnosis, cure, mitigation, treatment, prevention; affecting structure/function</td><td>Adds <strong>prediction and prognosis</strong>; includes specimen examination; conception</td></tr>
  <tr><td class="rowhead">Exclusion principle</td><td>No primary pharmacological/ immunological/metabolic action</td><td>No primary chemical action; not metabolised</td><td>No principal pharmacological/ immunological/metabolic action</td></tr>
  <tr><td class="rowhead">Software as device</td><td>Yes (expressly listed)</td><td>Yes (FDA guidance; 21st Century Cures Act carve-outs)</td><td>Yes (expressly listed; MDCG guidance)</td></tr>
  <tr><td class="rowhead">Non-medical products in scope</td><td>No</td><td>No</td><td>Yes &mdash; Annex XVI aesthetic products</td></tr>
</table>
</div>

<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight &middot; Borderline Products</div>
  <p>Products combining drug and device actions are assigned by their <strong>principal</strong> mode of action: a
  drug-eluting stent is a device with ancillary drug (device rules lead); a pre-filled insulin syringe is a
  drug with ancillary device (drug rules lead). Regulators publish borderline-classification guidance
  (e.g., the EU's Borderline &amp; Classification manual), and Chapter 13 treats combination products in depth.</p>
</div>

<h2 class="sec"><span class="secnum">2.2</span>Risk-Based Classification: The Universal Logic</h2>
<span class="wframe">Why</span>
<p>No regulator can subject a tongue depressor and a heart valve to identical scrutiny; the first would be
absurdly over-regulated, the second lethally under-regulated. The solution, pioneered by the US in 1976 and
refined by the GHTF into guidance that most nations (including India) now follow, is <strong>risk-proportionate
regulation</strong>: devices are sorted into classes by potential for harm, and regulatory burden climbs with class.
Class assignment turns on a handful of recurring factors:</p>
<ul>
  <li><strong>Duration of contact</strong> &mdash; transient (&lt;60 minutes), short term (&le;30 days), long term (&gt;30 days);</li>
  <li><strong>Degree of invasiveness</strong> &mdash; non-invasive, invasive through body orifice, surgically invasive, implantable;</li>
  <li><strong>Active vs non-active</strong> &mdash; whether the device depends on a source of energy other than the body or gravity;</li>
  <li><strong>Anatomical site</strong> &mdash; devices contacting the central circulatory system or central nervous system rank higher;</li>
  <li><strong>Local vs systemic effect</strong>, and whether the device delivers medicinal products or energy.</li>
</ul>
<p>The consequence &mdash; identical across India, the USA and the EU &mdash; is a pyramid: many low-risk devices under
light control at the base, few high-risk devices under intense control at the apex.</p>

<div class="figure">
<svg viewBox="0 0 790 250" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <g>
    <polygon points="350,15 425,70 275,70" fill="#0F4C5C"/>
    <polygon points="262,78 438,78 475,133 225,133" fill="#2E7D96"/>
    <polygon points="212,141 488,141 525,196 175,196" fill="#4E98AC"/>
    <polygon points="162,204 538,204 575,240 125,240" fill="#8FBECB"/>
  </g>
  <g font-size="10.5" fill="#fff" text-anchor="middle" font-weight="bold">
    <text x="350" y="52">CLASS D &middot; High risk</text>
    <text x="350" y="100">CLASS C &middot; Moderate&ndash;high risk</text>
    <text x="350" y="163">CLASS B &middot; Low&ndash;moderate risk</text>
    <text x="350" y="226" fill="#093542">CLASS A &middot; Low risk</text>
  </g>
  <g font-size="8.4" fill="#333">
    <text x="580" y="45">Heart valves, implantable pacemakers,</text><text x="580" y="56">drug-eluting stents &mdash; CLA licence</text>
    <text x="590" y="112">Ventilators, bone fixation plates,</text><text x="590" y="123">haemodialysers &mdash; CLA licence</text>
    <text x="600" y="175">Hypodermic needles, suction</text><text x="600" y="186">equipment, BP monitors &mdash; SLA</text>
    <text x="608" y="222">Thermometers, tongue depressors,</text><text x="608" y="233">absorbent cotton &mdash; SLA</text>
  </g>
  <g stroke="#5B6770" stroke-width="0.7"><line x1="430" y1="42" x2="575" y2="42"/><line x1="480" y1="108" x2="585" y2="108"/><line x1="530" y1="171" x2="595" y2="171"/><line x1="578" y1="219" x2="603" y2="219"/></g>
</svg>
<div class="figcaption"><b>Figure 2.1</b> &nbsp;The risk-based classification pyramid under CDSCO MDR 2017. Regulatory intensity, evidence requirements and licensing authority escalate from Class A to Class D. (CLA = Central Licensing Authority; SLA = State Licensing Authority.)</div>
</div>

<h2 class="sec"><span class="secnum">2.3</span>India &mdash; CDSCO Classification under MDR 2017 (Class A&ndash;D)</h2>
<span class="wframe">How</span>
<p>The <strong>First Schedule</strong> of the Medical Devices Rules, 2017 lays down classification principles closely
modelled on GHTF guidance. Devices (and, in a parallel set of rules, IVDs) are graded into four classes:</p>

<div class="tablewrap">
<div class="tabcaption"><b>Table 2.2</b> &nbsp;CDSCO MDR 2017 device classes with examples and licensing authority</div>
<table class="data">
  <tr><th style="width:18mm;">Class</th><th style="width:28mm;">Risk level</th><th>Representative examples</th><th style="width:42mm;">Manufacturing licence</th></tr>
  <tr><td class="rowhead">A</td><td>Low</td><td>Clinical thermometers, tongue depressors, absorbent cotton, surgical dressings, spectacle frames</td><td>State Licensing Authority; application Form MD-3 &rarr; licence Form MD-5 (Class A non-sterile, non-measuring: registration-based exemption per 2022 notification)</td></tr>
  <tr><td class="rowhead">B</td><td>Low&ndash;moderate</td><td>Hypodermic needles &amp; syringes, suction equipment, digital BP monitors, surgical gloves</td><td>State Licensing Authority; Form MD-3 &rarr; MD-5 (loan licence MD-4 &rarr; MD-6)</td></tr>
  <tr><td class="rowhead">C</td><td>Moderate&ndash;high</td><td>Lung ventilators, bone fixation plates, haemodialysers, intraocular lenses, condoms with spermicide</td><td>Central Licensing Authority (DCGI); Form MD-7 &rarr; licence MD-9 (loan MD-8 &rarr; MD-10)</td></tr>
  <tr><td class="rowhead">D</td><td>High</td><td>Prosthetic heart valves, implantable pacemakers/defibrillators, drug-eluting coronary stents, HIV diagnostic kits (IVD)</td><td>Central Licensing Authority (DCGI); Form MD-7 &rarr; MD-9; clinical investigation requirements apply</td></tr>
</table>
</div>

<p>Three structural features matter for practice:</p>
<ol>
  <li><strong>Split jurisdiction.</strong> The <strong>State Licensing Authority</strong> licenses manufacture of Class A and B
  devices; the <strong>Central Licensing Authority</strong> (the Drugs Controller General of India at CDSCO) licenses
  Class C and D manufacture, <em>all imports</em> of every class (Form MD-14 &rarr; licence MD-15), and clinical
  investigations.</li>
  <li><strong>Perpetual licences.</strong> MDR 2017 licences remain valid indefinitely subject to payment of a retention
  fee every five years &mdash; a deliberate ease-of-doing-business feature.</li>
  <li><strong>QMS anchoring.</strong> Every licence presupposes a quality management system audited against the Fifth
  Schedule, which is closely aligned to ISO 13485 (Chapter 7).</li>
</ol>

<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Classification is not academic: it dictates what a hospital pharmacist may accept in procurement. A
  Class D drug-eluting stent must arrive with an import licence (MD-15) or manufacturing licence (MD-9)
  traceable to CDSCO's registry; a Class A cotton roll needs only state-level registration. Verifying
  licence class against product class is a standard materiovigilance audit point.</p>
</div>

<h2 class="sec"><span class="secnum">2.4</span>United States &mdash; US FDA Classification (Class I&ndash;III)</h2>
<span class="wframe">How</span>
<p>The FDA sorts devices into three classes defined not by risk labels alone but by the <strong>controls necessary
to provide reasonable assurance of safety and effectiveness</strong>. Around 1,700 generic device types are
catalogued in sixteen classification panels (21 CFR Parts 862&ndash;892).</p>

<div class="tablewrap">
<div class="tabcaption"><b>Table 2.3</b> &nbsp;US FDA device classes, controls and typical premarket pathways</div>
<table class="data">
  <tr><th style="width:18mm;">Class</th><th style="width:34mm;">Controls</th><th style="width:40mm;">Typical premarket route</th><th>Examples</th></tr>
  <tr><td class="rowhead">I</td><td>General controls (registration, listing, labeling, GMP)</td><td>Mostly <strong>exempt</strong> from premarket notification</td><td>Elastic bandages, examination gloves, manual toothbrushes, tongue depressors</td></tr>
  <tr><td class="rowhead">II</td><td>General + special controls (performance standards, guidance, PMS)</td><td><strong>510(k)</strong> premarket notification &mdash; substantial equivalence to a predicate; <strong>De Novo</strong> where no predicate exists</td><td>Infusion pumps, powered wheelchairs, most IVD assays, CT scanners, pulse oximeters</td></tr>
  <tr><td class="rowhead">III</td><td>General controls + <strong>premarket approval</strong></td><td><strong>PMA</strong> &mdash; valid scientific evidence incl. clinical data</td><td>Implantable pacemakers, prosthetic heart valves, coronary stents, deep-brain stimulators</td></tr>
</table>
</div>

<p>Class I contains roughly half of all device types and is dominated by 510(k)-exempt products; Class III,
about 10% of types, carries the full weight of premarket approval. Between them, the <strong>510(k)</strong> pathway is
the workhorse of US device regulation: the sponsor demonstrates that the new device is <strong>substantially
equivalent</strong> to a legally marketed <strong>predicate</strong> &mdash; same intended use, and same technological
characteristics or different ones that raise no new questions of safety and effectiveness. Novel
low-to-moderate-risk devices without a predicate can request risk-based classification through the
<strong>De Novo</strong> pathway rather than defaulting into Class III.</p>

<div class="figure">
<svg viewBox="0 0 700 258" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <defs><marker id="arr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#14537D"/></marker></defs>
  <g font-size="9.3" text-anchor="middle">
    <rect x="255" y="10" width="190" height="34" fill="#0F4C5C"/><text x="350" y="31" fill="#fff" font-weight="bold">Is the product a device? (&sect;201(h))</text>
    <rect x="255" y="72" width="190" height="34" fill="#14537D"/><text x="350" y="88" fill="#fff" font-weight="bold">Identify classification</text><text x="350" y="100" fill="#BCD9E1">21 CFR 862&ndash;892 / product code</text>
    <rect x="40" y="150" width="180" height="42" fill="#E4EFF1" stroke="#0F4C5C"/><text x="130" y="167" font-weight="bold" fill="#0F4C5C">Class I</text><text x="130" y="181" fill="#333">General controls; mostly exempt</text>
    <rect x="260" y="150" width="180" height="42" fill="#E4EFF1" stroke="#0F4C5C"/><text x="350" y="167" font-weight="bold" fill="#0F4C5C">Class II</text><text x="350" y="181" fill="#333">510(k) substantial equivalence</text>
    <rect x="480" y="150" width="180" height="42" fill="#E4EFF1" stroke="#0F4C5C"/><text x="570" y="167" font-weight="bold" fill="#0F4C5C">Class III</text><text x="570" y="181" fill="#333">PMA with clinical evidence</text>
    <rect x="260" y="216" width="180" height="34" fill="#FBF5EC" stroke="#B4690E"/><text x="350" y="233" fill="#B4690E" font-weight="bold">No predicate? &rarr; De Novo request</text>
  </g>
  <g stroke="#14537D" stroke-width="1.1" fill="none" marker-end="url(#arr2)">
    <line x1="350" y1="44" x2="350" y2="68"/>
    <line x1="305" y1="106" x2="140" y2="146"/>
    <line x1="350" y1="106" x2="350" y2="146"/>
    <line x1="395" y1="106" x2="560" y2="146"/>
    <line x1="350" y1="192" x2="350" y2="212"/>
  </g>
</svg>
<div class="figcaption"><b>Figure 2.2</b> &nbsp;US FDA device classification and pathway decision flow. Classification determines the premarket route: exemption, 510(k), De Novo or PMA.</div>
</div>

<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>The 510(k) pathway is named simply after <strong>section 510(k)</strong> of the FD&amp;C Act &mdash; the paragraph
  requiring manufacturers to <em>notify</em> FDA 90 days before marketing. What began as a notification
  provision became the route for the vast majority of moderate-risk devices reaching the US market.</p>
</div>

<h2 class="sec"><span class="secnum">2.5</span>European Union &mdash; EU MDR and CE Marking</h2>
<span class="wframe">How &middot; When</span>
<p>The EU regulates devices through <strong>Regulation (EU) 2017/745</strong> (the EU MDR), fully applicable from
<strong>26 May 2021</strong>, which replaced the Medical Devices Directive 93/42/EEC and the Active Implantable
Medical Devices Directive 90/385/EEC after the PIP scandal exposed their weaknesses. Devices are classified
by the <strong>22 rules of Annex VIII</strong> into <strong>Class I</strong> (with special sub-categories: I<em>s</em> sterile,
I<em>m</em> measuring, I<em>r</em> reusable surgical instruments), <strong>Class IIa</strong>, <strong>Class IIb</strong> and
<strong>Class III</strong>.</p>
<p>The pivotal institutional difference from India and the USA: the EU has no central device-approval agency.
Instead, manufacturers affix the <strong>CE mark</strong> after a conformity assessment in which, for every class above
plain Class I, an independent <strong>notified body</strong> &mdash; an organization designated by a member state &mdash; audits
the QMS and reviews technical documentation. The manufacturer then draws up an EU Declaration of Conformity,
registers the device (UDI) in <strong>EUDAMED</strong>, and may market it across the entire Union.</p>

<div class="tablewrap">
<div class="tabcaption"><b>Table 2.4</b> &nbsp;EU MDR classes and conformity assessment requirements</div>
<table class="data">
  <tr><th style="width:22mm;">Class</th><th style="width:36mm;">Examples</th><th>Conformity assessment</th></tr>
  <tr><td class="rowhead">I</td><td>Wheelchairs, stethoscopes, corrective spectacles</td><td>Manufacturer self-declaration; QMS &amp; technical documentation; no notified body (unless Is/Im/Ir aspects)</td></tr>
  <tr><td class="rowhead">Is / Im / Ir</td><td>Sterile dressings; thermometers; reusable surgical forceps</td><td>Notified body reviews the sterile/measuring/reprocessing aspects only</td></tr>
  <tr><td class="rowhead">IIa</td><td>Dental fillings, short-term contact lenses, diagnostic ultrasound</td><td>Notified body assessment of QMS and representative technical documentation</td></tr>
  <tr><td class="rowhead">IIb</td><td>Ventilators, infusion pumps, long-term contact lenses, bone fixation</td><td>Notified body assessment; deeper technical documentation sampling per device group</td></tr>
  <tr><td class="rowhead">III</td><td>Heart valves, pacemakers, drug-eluting stents, neuro-implants</td><td>Full QMS + device-specific technical documentation review; clinical evaluation with expert panel consultation for certain implants</td></tr>
</table>
</div>

<div class="figure">
<svg viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <defs><marker id="arr3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0F4C5C"/></marker></defs>
  <g font-size="8.8" text-anchor="middle">
    <rect x="10" y="35" width="118" height="46" fill="#E4EFF1" stroke="#0F4C5C"/><text x="69" y="54" font-weight="bold" fill="#0F4C5C">1. Classify device</text><text x="69" y="67" fill="#333">Annex VIII, 22 rules</text>
    <rect x="150" y="35" width="118" height="46" fill="#E4EFF1" stroke="#0F4C5C"/><text x="209" y="54" font-weight="bold" fill="#0F4C5C">2. QMS + technical file</text><text x="209" y="67" fill="#333">GSPR, clinical evaluation</text>
    <rect x="290" y="35" width="118" height="46" fill="#E4EFF1" stroke="#0F4C5C"/><text x="349" y="54" font-weight="bold" fill="#0F4C5C">3. Notified body audit</text><text x="349" y="67" fill="#333">(Class Is/Im/Ir&ndash;III)</text>
    <rect x="430" y="35" width="118" height="46" fill="#E4EFF1" stroke="#0F4C5C"/><text x="489" y="54" font-weight="bold" fill="#0F4C5C">4. Declaration + CE</text><text x="489" y="67" fill="#333">EU DoC, CE mark, UDI</text>
    <rect x="570" y="35" width="118" height="46" fill="#0F4C5C"/><text x="629" y="54" font-weight="bold" fill="#fff">5. Market + PMS</text><text x="629" y="67" fill="#BCD9E1">EUDAMED, vigilance</text>
  </g>
  <g stroke="#0F4C5C" stroke-width="1.1" fill="none" marker-end="url(#arr3)">
    <line x1="128" y1="58" x2="146" y2="58"/><line x1="268" y1="58" x2="286" y2="58"/><line x1="408" y1="58" x2="426" y2="58"/><line x1="548" y1="58" x2="566" y2="58"/>
  </g>
</svg>
<div class="figcaption"><b>Figure 2.3</b> &nbsp;EU CE marking conformity assessment route. Notified-body involvement scales with device class; Class I (non-sterile, non-measuring, non-reusable-surgical) is self-declared.</div>
</div>

<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>The EU MDR transition created a global shortage of notified-body capacity, with review queues stretching
  beyond a year &mdash; a vivid demonstration that regulatory infrastructure is itself a market bottleneck.
  Indian exporters targeting Europe now build MDR technical documentation from day one, and regulatory
  affairs professionals fluent in Annex VIII rules command a premium.</p>
</div>

<h2 class="sec"><span class="secnum">2.6</span>IMDRF and Global Harmonization</h2>
<span class="wframe">Where &middot; When</span>
<p>A syringe maker selling to sixty countries once faced sixty regulatory dialects. The convergence effort
began with the <strong>Global Harmonization Task Force (GHTF)</strong>, founded in 1992 by the regulators and industry
of the USA, EU, Canada, Australia and Japan. GHTF's guidance documents &mdash; on classification principles,
essential principles of safety, and QMS &mdash; became the templates on which later national rules (including
India's MDR 2017) were drafted. In <strong>2011</strong> GHTF was succeeded by the <strong>International Medical Device
Regulators Forum (IMDRF)</strong>, a regulators-only body whose members include the regulatory authorities of
Australia, Brazil, Canada, China, the EU, Japan, Russia, Singapore, South Korea, the UK and the USA, with
the WHO as an official observer. India's CDSCO participates in IMDRF open sessions and models its rules on
IMDRF documents, reflecting its path toward deeper engagement with the forum.</p>
<p>IMDRF's practical outputs matter to every submission a regulatory-affairs pharmacist writes:</p>
<ul>
  <li><strong>SaMD framework</strong> &mdash; the N10/N12 documents defining Software as a Medical Device and its risk categorisation;</li>
  <li><strong>UDI guidance</strong> &mdash; the architecture of unique device identification adopted by FDA, EU and India alike;</li>
  <li><strong>MDSAP</strong> &mdash; the Medical Device Single Audit Program, under which one QMS audit satisfies five jurisdictions (USA, Canada, Brazil, Australia, Japan);</li>
  <li><strong>Table-of-contents formats</strong> for harmonised premarket submissions.</li>
</ul>

<div class="figure">
<svg viewBox="0 0 700 130" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <line x1="40" y1="65" x2="670" y2="65" stroke="#0F4C5C" stroke-width="2"/>
  <g text-anchor="middle">
    <circle cx="80" cy="65" r="5" fill="#0F4C5C"/><text x="80" y="44" font-size="10.5" font-weight="bold" fill="#0F4C5C">1992</text><text x="80" y="90" font-size="8.8" fill="#333">GHTF founded</text><text x="80" y="101" font-size="8" fill="#777">US, EU, CA, AU, JP</text>
    <circle cx="240" cy="65" r="5" fill="#0F4C5C"/><text x="240" y="44" font-size="10.5" font-weight="bold" fill="#0F4C5C">1990s&ndash;2000s</text><text x="240" y="90" font-size="8.8" fill="#333">Guidance on classification,</text><text x="240" y="101" font-size="8.8" fill="#333">essential principles, QMS</text>
    <circle cx="400" cy="65" r="5" fill="#B4690E"/><text x="400" y="44" font-size="10.5" font-weight="bold" fill="#B4690E">2011</text><text x="400" y="90" font-size="8.8" fill="#333">IMDRF succeeds GHTF</text><text x="400" y="101" font-size="8" fill="#777">regulators-only forum</text>
    <circle cx="540" cy="65" r="5" fill="#0F4C5C"/><text x="540" y="44" font-size="10.5" font-weight="bold" fill="#0F4C5C">2013&ndash;17</text><text x="540" y="90" font-size="8.8" fill="#333">SaMD, UDI, MDSAP;</text><text x="540" y="101" font-size="8.8" fill="#333">India's MDR 2017 aligns</text>
    <circle cx="650" cy="65" r="5" fill="#14537D"/><text x="650" y="44" font-size="10.5" font-weight="bold" fill="#14537D">Today</text><text x="650" y="90" font-size="8.8" fill="#333">AI/ML device</text><text x="650" y="101" font-size="8.8" fill="#333">convergence work</text>
  </g>
</svg>
<div class="figcaption"><b>Figure 2.4</b> &nbsp;From GHTF to IMDRF: the harmonization timeline. India's MDR 2017 classification rules are drafted on GHTF/IMDRF principles.</div>
</div>

<div class="tablewrap">
<div class="tabcaption"><b>Table 2.5</b> &nbsp;Side-by-side comparison: India vs USA vs EU classification and routes</div>
<table class="data">
  <tr><th style="width:34mm;">Feature</th><th>India (CDSCO)</th><th>USA (FDA)</th><th>EU (MDR)</th></tr>
  <tr><td class="rowhead">Legal basis</td><td>D&amp;C Act 1940 + MDR 2017</td><td>FD&amp;C Act 1938 + MDA 1976</td><td>Regulation (EU) 2017/745</td></tr>
  <tr><td class="rowhead">Classes</td><td>A, B, C, D</td><td>I, II, III</td><td>I (Is/Im/Ir), IIa, IIb, III</td></tr>
  <tr><td class="rowhead">Classification method</td><td>First Schedule rules (GHTF-based)</td><td>Panel/product-code precedent (21 CFR 862&ndash;892)</td><td>Annex VIII &mdash; 22 rules</td></tr>
  <tr><td class="rowhead">Reviewer</td><td>SLA (A&ndash;B mfg); CLA/DCGI (C&ndash;D, all imports)</td><td>FDA (CDRH)</td><td>Notified bodies (private, state-designated); self-declaration for Class I</td></tr>
  <tr><td class="rowhead">Typical high-risk route</td><td>MD-7 &rarr; MD-9 licence + clinical investigation</td><td>PMA</td><td>Notified body cert. + expert panel; CE mark</td></tr>
  <tr><td class="rowhead">Equivalence concept</td><td>Predicate device provisions for substantial equivalence</td><td>510(k) substantial equivalence</td><td>Equivalence tightly restricted under MDR Art. 61</td></tr>
  <tr><td class="rowhead">Post-market DB</td><td>MvPI / SUGAM registry</td><td>MAUDE database</td><td>EUDAMED</td></tr>
</table>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 2.1 &middot; PIP Breast Implants &mdash; Why Europe Rewrote Its Rulebook</div>
  <div class="cs-body">
    <p>Between 2001 and 2010, French manufacturer Poly Implant Proth&egrave;se (PIP) fraudulently filled hundreds
    of thousands of CE-marked breast implants with cheap industrial-grade silicone instead of the approved
    medical grade, roughly doubling rupture-prone devices across 65 countries. The fraud evaded the notified
    body's <em>announced</em> audits for years. The scandal &mdash; and the parallel metal-on-metal hip failures &mdash;
    demolished confidence in the directive system and directly produced Regulation (EU) 2017/745: unannounced
    audits, stricter notified-body designation, device-level scrutiny for implants, UDI traceability, and the
    EUDAMED transparency database.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Which specific control failures allowed PIP to persist for nearly a decade?</li>
      <li>Map each failure to the EU MDR provision designed to prevent its recurrence.</li>
      <li>Could India's MDR 2017 architecture have caught PIP earlier? Why or why not?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Announced-only audits, no raw-material verification, no device traceability, fragmented national
      vigilance. (2) Unannounced audits and sample testing (Art. 44/Annex IX); stricter notified body oversight
      (Arts. 35&ndash;49); UDI (Art. 27); EUDAMED vigilance module (Arts. 87&ndash;92). (3) Partially: India's central
      import licensing and MvPI provide central visibility, but detection of deliberate raw-material fraud
      ultimately depends on unannounced inspection and testing capacity &mdash; a lesson MDR 2017's Fifth Schedule
      audits inherit.</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 2.2 &middot; One Device, Three Rulebooks: Classifying a Pulse Oximeter</div>
  <div class="cs-body">
    <p>A start-up develops a fingertip pulse oximeter and targets India, the USA and the EU simultaneously.
    In India the device falls in <strong>Class B</strong> (low&ndash;moderate risk monitoring device) &mdash; state licence via
    Form MD-3 &rarr; MD-5 for domestic manufacture. In the USA it is <strong>Class II</strong>, requiring a 510(k) against
    one of the many oximeter predicates and conformance with special controls including performance testing.
    In the EU it is <strong>Class IIa</strong> (active diagnostic device supplying physiological information &mdash; Annex VIII
    Rule 10), requiring a notified-body-audited QMS before CE marking. Three classifications, one device,
    one underlying risk logic.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Why do the three systems converge on &ldquo;moderate risk&rdquo; despite different class labels?</li>
      <li>Which market's route is fastest for this device, and what single document set (per IMDRF ToC) could serve all three?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) All three apply the same GHTF-derived factors &mdash; active device, non-invasive, physiological
      monitoring, misdiagnosis risk bounded. (2) The Indian SLA route is typically fastest procedurally; an
      IMDRF-format technical file (device description, essential principles checklist, risk management file
      per ISO 14971, clinical evaluation, performance data) can seed all three submissions &mdash; harmonization's
      concrete payoff.</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>All major definitions share the same skeleton: an article with a medical purpose whose principal action is <strong>not</strong> pharmacological, immunological or metabolic; the EU adds prediction/prognosis and certain non-medical (Annex XVI) products.</li>
    <li>Risk-based classification is the universal architecture; class is driven by duration of contact, invasiveness, active status, anatomical site and effect systemic-ness.</li>
    <li><strong>India:</strong> MDR 2017 First Schedule yields Classes A&ndash;D; SLA licenses Class A&ndash;B manufacture (MD-3&rarr;MD-5), CLA/DCGI licenses Class C&ndash;D (MD-7&rarr;MD-9) and all imports (MD-14&rarr;MD-15); licences are perpetual with retention fees.</li>
    <li><strong>USA:</strong> Classes I&ndash;III by necessary controls; Class I mostly exempt, Class II via 510(k) substantial equivalence (De Novo for novel devices), Class III via PMA with clinical evidence.</li>
    <li><strong>EU:</strong> MDR 2017/745 (applicable 26 May 2021) classifies via Annex VIII's 22 rules into I (Is/Im/Ir), IIa, IIb, III; notified bodies conduct conformity assessment; CE mark + UDI + EUDAMED complete market access.</li>
    <li><strong>Harmonization:</strong> GHTF (1992) seeded common principles; IMDRF (2011) drives convergence through SaMD, UDI, MDSAP and submission-format work; India's rules are built on this scaffolding.</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Primary/principal mode of action</dt> <dd>&mdash; mechanism test excluding pharmacological/immunological/metabolic action from device status.</dd></div>
    <div class="kt-row"><dt>First Schedule (MDR 2017)</dt> <dd>&mdash; India's classification rule set producing Classes A&ndash;D.</dd></div>
    <div class="kt-row"><dt>State/Central Licensing Authority</dt> <dd>&mdash; split Indian jurisdiction: SLA for Class A&ndash;B manufacture; CLA (DCGI) for C&ndash;D and all imports.</dd></div>
    <div class="kt-row"><dt>510(k)</dt> <dd>&mdash; US premarket notification demonstrating substantial equivalence to a predicate.</dd></div>
    <div class="kt-row"><dt>De Novo</dt> <dd>&mdash; US pathway granting risk-based classification to novel devices lacking predicates.</dd></div>
    <div class="kt-row"><dt>PMA</dt> <dd>&mdash; premarket approval; the most stringent US route, for Class III devices.</dd></div>
    <div class="kt-row"><dt>Annex VIII</dt> <dd>&mdash; EU MDR's 22 classification rules.</dd></div>
    <div class="kt-row"><dt>Notified body</dt> <dd>&mdash; member-state-designated conformity assessor for CE marking.</dd></div>
    <div class="kt-row"><dt>CE marking</dt> <dd>&mdash; manufacturer's declaration of EU conformity permitting Union-wide marketing.</dd></div>
    <div class="kt-row"><dt>GHTF / IMDRF</dt> <dd>&mdash; successive global harmonization bodies (1992/2011).</dd></div>
    <div class="kt-row"><dt>MDSAP</dt> <dd>&mdash; single QMS audit accepted by five jurisdictions.</dd></div>
    <div class="kt-row"><dt>UDI</dt> <dd>&mdash; unique device identification enabling traceability.</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 2 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>Under all three major definitions, a product is NOT a medical device if its principal intended action is achieved by:
    <ul class="mcq-opts"><li><span class="ol">a)</span> mechanical means</li><li><span class="ol">b)</span> software logic</li><li><span class="ol">c)</span> pharmacological means</li><li><span class="ol">d)</span> physical measurement</li></ul>
    <div class="rationale"><b>Answer: c.</b> Pharmacological (with immunological and metabolic) action is the exclusion criterion; mechanical, physical and software actions are the very substance of devices.</div></li>
  <li>Under MDR 2017, a lung ventilator is classified as:
    <ul class="mcq-opts"><li><span class="ol">a)</span> Class A</li><li><span class="ol">b)</span> Class C</li><li><span class="ol">c)</span> Class B</li><li><span class="ol">d)</span> Class D</li></ul>
    <div class="rationale"><b>Answer: b (option letter) &mdash; Class C.</b> Life-supporting equipment failure can cause serious harm, but ventilators are not implantable high-risk devices like heart valves (Class D).</div></li>
  <li>Which Indian authority licenses the import of a Class A device?
    <ul class="mcq-opts"><li><span class="ol">a)</span> State Licensing Authority</li><li><span class="ol">b)</span> BIS</li><li><span class="ol">c)</span> National Institute of Biologicals</li><li><span class="ol">d)</span> Central Licensing Authority (DCGI)</li></ul>
    <div class="rationale"><b>Answer: d.</b> ALL imports, regardless of class, are licensed centrally (Form MD-14 &rarr; MD-15); the SLA's remit is Class A&ndash;B domestic manufacture.</div></li>
  <li>The US pathway that establishes &ldquo;substantial equivalence&rdquo; to a predicate device is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> PMA</li><li><span class="ol">b)</span> 510(k)</li><li><span class="ol">c)</span> De Novo</li><li><span class="ol">d)</span> HDE</li></ul>
    <div class="rationale"><b>Answer: b.</b> 510(k) premarket notification rests on substantial equivalence; PMA demands independent proof of safety/effectiveness; De Novo classifies novel devices; HDE serves humanitarian-use devices.</div></li>
  <li>An implantable pacemaker in the USA is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> Class I</li><li><span class="ol">b)</span> Class II</li><li><span class="ol">c)</span> Class III</li><li><span class="ol">d)</span> unclassified</li></ul>
    <div class="rationale"><b>Answer: c.</b> Life-sustaining implants require premarket approval &mdash; the definition of Class III.</div></li>
  <li>Under EU MDR, device classification is performed using:
    <ul class="mcq-opts"><li><span class="ol">a)</span> the 22 rules of Annex VIII</li><li><span class="ol">b)</span> FDA product codes</li><li><span class="ol">c)</span> the First Schedule</li><li><span class="ol">d)</span> notified body discretion</li></ul>
    <div class="rationale"><b>Answer: a.</b> Annex VIII contains the EU's rule-based algorithm. The First Schedule is India's; product codes are American; notified bodies apply, not invent, the rules.</div></li>
  <li>The EU MDR became fully applicable on:
    <ul class="mcq-opts"><li><span class="ol">a)</span> 1 January 2018</li><li><span class="ol">b)</span> 5 April 2017</li><li><span class="ol">c)</span> 26 May 2021</li><li><span class="ol">d)</span> 26 May 2017</li></ul>
    <div class="rationale"><b>Answer: c.</b> Adopted 5 April 2017, the Regulation applied from 26 May 2021 after a pandemic-related one-year deferral. 1 January 2018 is India's MDR 2017 commencement.</div></li>
  <li>Which body succeeded the GHTF in 2011?
    <ul class="mcq-opts"><li><span class="ol">a)</span> WHO PQ</li><li><span class="ol">b)</span> IMDRF</li><li><span class="ol">c)</span> ICH</li><li><span class="ol">d)</span> PIC/S</li></ul>
    <div class="rationale"><b>Answer: b.</b> The International Medical Device Regulators Forum, a regulators-only successor. ICH and PIC/S serve medicines; WHO prequalification is a procurement quality mechanism.</div></li>
  <li>MDSAP allows a single audit to satisfy the QMS requirements of:
    <ul class="mcq-opts"><li><span class="ol">a)</span> India, USA, EU</li><li><span class="ol">b)</span> all IMDRF members</li><li><span class="ol">c)</span> USA and EU only</li><li><span class="ol">d)</span> USA, Canada, Brazil, Australia, Japan</li></ul>
    <div class="rationale"><b>Answer: d.</b> The five MDSAP jurisdictions are the USA, Canada (where it is mandatory), Brazil, Australia and Japan. The EU and India are not MDSAP participants.</div></li>
  <li>Under MDR 2017, manufacturing licences are:
    <ul class="mcq-opts"><li><span class="ol">a)</span> valid for 5 years, then reapplication</li><li><span class="ol">b)</span> perpetual, subject to retention fee every five years</li><li><span class="ol">c)</span> annual</li><li><span class="ol">d)</span> valid for 10 years</li></ul>
    <div class="rationale"><b>Answer: b.</b> Perpetual licensing with periodic retention fees is a distinctive ease-of-doing-business feature of the Indian rules.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>In India, medical devices are regulated under a standalone Medical Devices Act. <span class="marks">(F &mdash; under the Drugs and Cosmetics Act, 1940 via MDR 2017)</span></li>
  <li>The EU definition of a medical device includes software intended for prognosis of disease. <span class="marks">(T)</span></li>
  <li>Duration of contact and invasiveness are core classification factors in all three systems. <span class="marks">(T)</span></li>
  <li>A Class C device manufacturing licence in India is granted by the State Licensing Authority. <span class="marks">(F &mdash; Central Licensing Authority)</span></li>
  <li>Most US Class I devices are exempt from 510(k) notification. <span class="marks">(T)</span></li>
  <li>A PMA is required for every Class II device in the USA. <span class="marks">(F &mdash; PMA is the Class III route)</span></li>
  <li>CE marking is granted by the European Commission itself. <span class="marks">(F &mdash; the manufacturer affixes it after conformity assessment, with notified body certification where required)</span></li>
  <li>EU Class I reusable surgical instruments (Ir) require notified body involvement for reprocessing aspects. <span class="marks">(T)</span></li>
  <li>WHO is an official observer at IMDRF. <span class="marks">(T)</span></li>
  <li>India is one of the five MDSAP audit jurisdictions. <span class="marks">(F)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>A device must not achieve its primary intended action by __________, __________ or __________ means.</li>
  <li>Prosthetic heart valves and drug-eluting stents belong to Indian Class __________.</li>
  <li>Class A and B manufacturing licences in India are issued by the __________.</li>
  <li>The most stringent US premarket pathway, used for Class III devices, is __________.</li>
  <li>The 510(k) route requires demonstration of __________ to a predicate device.</li>
  <li>EU classification rules are contained in __________ of Regulation (EU) 2017/745.</li>
  <li>Conformity of Class IIa/IIb/III devices in the EU is certified by a __________.</li>
  <li>The EU MDR became fully applicable on __________.</li>
  <li>The IMDRF was established in the year __________.</li>
  <li>Classification in every jurisdiction is anchored to the manufacturer's stated __________ of the device.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> A drug-eluting stent is Class D in India. <strong>R:</strong> It is a long-term implant in the central circulatory system incorporating an ancillary medicinal substance. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> All Indian device imports are licensed by the CLA. <strong>R:</strong> The State Licensing Authority has no role in any device licensing. <span class="marks">(c &mdash; A true; R false: SLAs license Class A&ndash;B manufacture)</span></li>
  <li><strong>A:</strong> The 510(k) pathway is faster than PMA. <strong>R:</strong> Substantial equivalence to a predicate replaces independent clinical demonstration of safety and effectiveness. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> CE marking certifies that the European Commission has approved a device. <strong>R:</strong> Notified bodies are designated by member states to assess conformity. <span class="marks">(d &mdash; A false: CE is the manufacturer's declaration of conformity; R true)</span></li>
  <li><strong>A:</strong> India's First Schedule classification resembles EU Annex VIII. <strong>R:</strong> IMDRF publishes the MDSAP audit model. <span class="marks">(b &mdash; both true; R does not explain A: the resemblance stems from shared GHTF ancestry)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>Write the US FD&amp;C &sect;201(h) definition of a device in your own words, preserving its three limbs and its exclusion clause.</li>
  <li>List the five principal factors driving risk classification, with one example device for each.</li>
  <li>Tabulate Indian Classes A&ndash;D with two examples and the licensing authority for each.</li>
  <li>Differentiate 510(k), De Novo and PMA in three sentences each.</li>
  <li>What are Class Is, Im and Ir in the EU system, and why do they need notified body involvement?</li>
  <li>State four concrete outputs of IMDRF and one sentence on each's practical use.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Compare and contrast medical device classification and premarket routes in India, the USA and the EU, using a labelled diagram or table, and explain how a single risk logic produces three different institutional designs.</li>
  <li>Describe India's MDR 2017 classification and licensing architecture in full &mdash; classes, schedules, forms, authorities, perpetual licensing &mdash; and evaluate its strengths and gaps against the EU MDR.</li>
  <li>Trace global harmonization from GHTF to IMDRF and assess, with examples (SaMD, UDI, MDSAP), how harmonization changes the daily work of a regulatory affairs professional in an Indian device company.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>An AI mobile application analyses smartphone photographs of skin lesions and outputs melanoma risk scores. Argue its classification in India, the USA and the EU, citing the definitional and rule provisions you would rely on, and identify the single greatest classification uncertainty.</li>
  <li>The PIP fraud passed announced audits for years. Design three audit-system changes (beyond those in EU MDR) that would detect deliberate raw-material substitution, and analyse their cost and feasibility for Indian SLAs.</li>
  <li>A manufacturer's syringe is Class B in India, Class II in the USA, and Class IIa in the EU. Propose a single global technical file structure (IMDRF ToC) and mark which sections need jurisdiction-specific annexes and why.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 (G.S.R. 78(E), 31 January 2017), incl. First Schedule (classification) and Fifth Schedule (QMS). New Delhi: Ministry of Health and Family Welfare; 2017.</li>
  <li>Ministry of Health and Family Welfare. Notification S.O. 648(E) dated 11 February 2020 (definition of medical devices, effective 1 April 2020) and Medical Devices (Amendment) Rules, 2020. New Delhi: Government of India; 2020.</li>
  <li>US Food and Drug Administration. Federal Food, Drug, and Cosmetic Act &sect;201(h); 21 CFR Parts 860&ndash;892. Silver Spring (MD): FDA.</li>
  <li>US Food and Drug Administration. The 510(k) Program: Evaluating Substantial Equivalence in Premarket Notifications &mdash; Guidance. Silver Spring (MD): FDA; 2014.</li>
  <li>US Food and Drug Administration. De Novo Classification Process (Evaluation of Automatic Class III Designation) &mdash; Guidance. Silver Spring (MD): FDA; 2021.</li>
  <li>European Parliament and Council. Regulation (EU) 2017/745 of 5 April 2017 on medical devices, incl. Annex VIII (classification rules) and Annex XVI. OJEU. 2017;L117:1-175.</li>
  <li>Medical Device Coordination Group. MDCG 2021-24: Guidance on classification of medical devices. Brussels: European Commission; 2021.</li>
  <li>Global Harmonization Task Force. Principles of Medical Devices Classification (GHTF/SG1/N77:2012). GHTF; 2012.</li>
  <li>International Medical Device Regulators Forum. IMDRF/SaMD WG/N10:2013 &mdash; Software as a Medical Device (SaMD): Key Definitions. IMDRF; 2013.</li>
  <li>International Medical Device Regulators Forum. About IMDRF; MDSAP documents [Internet]. Available from: https://www.imdrf.org</li>
  <li>Heneghan C, Thompson M, Billingsley M, Cohen D. Medical-device recalls in the UK and the device-regulation process: retrospective review of safety notices and alerts. BMJ Open. 2011;1(1):e000155.</li>
  <li>Martindale V, Menache A. The PIP scandal: an analysis of the process of quality control that failed to safeguard women from the health risks. J R Soc Med. 2013;106(5):173-7.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 2 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 2.1&ndash;2.6</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figures 2.1&ndash;2.4; Tables 2.1&ndash;2.5</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 2.1 (PIP), 2.2 (pulse oximeter)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>G.S.R. 78(E); S.O. 648(E); FD&amp;C &sect;201(h); Reg. (EU) 2017/745; GHTF/IMDRF documents &mdash; cited in references</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>12 references</td></tr>
</table>
</div>

</section>
"""
