#!/usr/bin/env python3
"""Builds the SDVsolution website pages into the repo folder given as argv[1]."""
import sys, os
OUT = sys.argv[1]
NEW = 'target="_blank" rel="noopener"'

LOGO = '<svg width="26" height="26" viewBox="0 0 26 26" aria-hidden="true"><rect width="26" height="26" fill="#9CFF3A"/><g fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="square"><circle cx="18.5" cy="7" r="2.6"/><circle cx="7.5" cy="13" r="2.6"/><circle cx="18.5" cy="19" r="2.6"/><path d="M9.8 11.8l6.4-3.6M9.8 14.2l6.4 3.6"/></g></svg>'

PAGES = [("platform.html", "Platform"), ("software-factory.html", "Software factory"), ("nvidia-drive.html", "NVIDIA DRIVE"), ("solutions.html", "Solutions and plans")]

def header(cur):
    links = "".join('<a href="%s" %s%s>%s</a>' % (f, NEW, ' aria-current="page"' if f == cur else "", t) for f, t in PAGES)
    home = '#top' if cur == "index.html" else 'index.html'
    return f'''<header class="top"><div class="wrap nav">
  <a class="brand" href="{home}" {"" if cur == "index.html" else NEW}>{LOGO}SDVsolution</a>
  <nav class="navlinks" aria-label="Main">{links}</nav>
  <div class="nav-cta"><a class="login" href="https://app.sdvsolution.com" {NEW}>Log in</a><a class="btn btn-lime" href="#demo">Request a demo</a></div>
</div></header>'''

def contact(title="See it on a real vehicle feature.", lead="Request a demo, ask about an NVIDIA DRIVE integration, or get a quote for your scope. We reply by email."):
    return f'''<section class="band band-ink" id="demo"><div class="wrap contact">
  <div>
    <h2>{title}</h2>
    <p class="lead">{lead}</p>
    <ul class="pts">
      <li>A walkthrough with our team, on a sample feature from requirement to test</li>
      <li>Then access for your team, by email</li>
      <li>A quote scoped to a feature, a sub-system, a domain or the full stack</li>
    </ul>
  </div>
  <form class="demo" id="demoForm" action="https://formspree.io/f/xljrqwaw" method="POST">
    <div class="ttl">Request a demo or contact us</div>
    <label for="df-name">Name</label><input id="df-name" name="name" required autocomplete="name" />
    <label for="df-email">Work email</label><input id="df-email" type="email" name="email" required autocomplete="email" placeholder="you@company.com" />
    <label for="df-company">Company</label><input id="df-company" name="company" autocomplete="organization" />
    <label for="df-team">Team size</label><select id="df-team" name="team_size"><option>1–5</option><option>6–20</option><option>21–100</option><option>100+</option></select>
    <label for="df-interest">I'm interested in</label><select id="df-interest" name="interest"><option>A demo</option><option>NVIDIA DRIVE AGX Thor integration</option><option>Generated software for a feature</option><option>Generated software for an ECU</option><option>The complete vehicle software</option><option>A license for a sub-system or domain</option><option>A tool license</option><option>Something else</option></select>
    <label for="df-msg">What would you like to see?</label><textarea id="df-msg" name="message"></textarea>
    <input type="hidden" name="_subject" value="SDVsolution contact request" />
    <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off" />
    <button class="btn btn-lime" type="submit">Send request</button>
    <div class="status" id="demoStatus" role="status" aria-live="polite"></div>
  </form>
</div></section>'''

def footer():
    return f'''<footer><div class="wrap">
  <div class="fgrid">
    <div><div class="brand" style="margin-bottom:12px">{LOGO}SDVsolution</div><p style="max-width:34ch">One engineering system for the software-defined vehicle, from the first requirement to the integrated vehicle software.</p></div>
    <div><h4>Product</h4><a href="platform.html" {NEW}>Platform</a><a href="software-factory.html" {NEW}>Software factory</a><a href="nvidia-drive.html" {NEW}>NVIDIA DRIVE</a><a href="solutions.html" {NEW}>Solutions and plans</a></div>
    <div><h4>Company</h4><a href="#demo">Contact</a><a href="https://www.linkedin.com/company/sdvsolution/" {NEW}>LinkedIn</a><a href="https://app.sdvsolution.com" {NEW}>Log in</a></div>
    <div><h4>Legal</h4><a href="terms.html" {NEW}>Terms of Service</a><a href="privacy.html" {NEW}>Privacy Policy</a></div>
  </div>
  <div class="fbot"><span>© 2026 SDVsolution. All rights reserved.</span><span>NVIDIA and NVIDIA DRIVE are trademarks of NVIDIA Corporation. SDVsolution is not affiliated with, sponsored by or endorsed by NVIDIA.</span></div>
</div></footer>
<script src="assets/site.js"></script>'''

def page(fname, title, desc, body):
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="preload" href="assets/fonts/barlow-condensed-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin />
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
<link rel="stylesheet" href="assets/site.css" />
</head>
<body>
{header(fname)}
<a id="top"></a>
{body}
{footer()}
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)

# ------------------------------------------------------------------ drawings
def box(x, y, w, h, t, s=None, core=False):
    o = f'<rect class="{"d-core" if core else "d-box"}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
    o += f'<text class="d-t" x="{x + w / 2}" y="{y + (h / 2 + (-2 if s else 5))}" text-anchor="middle">{t}</text>'
    if s: o += f'<text class="d-s" x="{x + w / 2}" y="{y + h / 2 + 14}" text-anchor="middle">{s}</text>'
    return o

TOPO = f'''<svg class="topo" viewBox="0 0 640 470" role="img" aria-label="Vehicle topology: a central computer connected by Ethernet to front, center and rear zone controllers, which reach door, seat, lighting and climate units over CAN and LIN.">
  <path class="bus d-eth" d="M320 92V150M320 150H110V196M320 150V196M320 150H530V196"/>
  <path class="bus b2 d-can" d="M110 252V300M60 300H160M60 300V336M160 300V336M320 252V300M250 300H390M250 300V336M320 300V336M390 300V336M530 252V300M480 300H580M480 300V336M580 300V336"/>
  <path class="bus b3 d-lin" d="M60 384V420M160 384V420M250 384V420M390 384V420M480 384V420M580 384V420"/>
  {box(230, 34, 180, 58, "Central computer", "driver assistance + cockpit", True)}
  {box(40, 196, 140, 56, "Front zone", "climate, chassis")}
  {box(250, 196, 140, 56, "Center zone", "body, access, power")}
  {box(460, 196, 140, 56, "Rear zone", "tailgate, trailer")}
  {box(20, 336, 80, 48, "Wiper")}{box(120, 336, 80, 48, "Brake")}
  {box(212, 336, 76, 48, "Doors")}{box(292, 336, 56, 48, "Seats")}{box(352, 336, 76, 48, "Roof")}
  {box(440, 336, 80, 48, "Lighting")}{box(540, 336, 80, 48, "Tires")}
  <g class="d-s" text-anchor="middle"><text x="60" y="438">rain sensor</text><text x="160" y="438">wear sensor</text><text x="250" y="438">switch pack</text><text x="390" y="438">mirror</text><text x="480" y="438">ambient light</text><text x="580" y="438">parking lock</text></g>
</svg>
<div class="legend"><span><i style="background:var(--lime)"></i>Ethernet</span><span><i style="background:var(--can)"></i>CAN</span><span><i style="background:var(--lin)"></i>LIN</span></div>'''

ART_V = f'''<svg viewBox="0 0 520 300" role="img" aria-label="The V-model: stakeholder needs, system, software and hardware requirements going down the left side, and unit, integration and system tests coming up the right, each level traced across.">
  <path class="d-thin" d="M150 62H370M190 122H330M230 182H290" stroke-dasharray="4 5"/>
  <path class="d-wire d-eth" d="M40 40L250 262L470 40" opacity=".35"/>
  {box(20, 44, 130, 36, "System requirements")}{box(370, 44, 130, 36, "System test")}
  {box(60, 104, 130, 36, "Architecture")}{box(330, 104, 130, 36, "Integration test")}
  {box(100, 164, 130, 36, "Software, hardware")}{box(290, 164, 130, 36, "Unit test")}
  {box(195, 236, 130, 36, "Code", None, True)}
  <g class="d-s" text-anchor="middle"><text x="260" y="58">traced</text><text x="260" y="118">traced</text><text x="260" y="178">traced</text></g>
</svg>'''

def trow(y, a, b, c, ok=True):
    mark = f'<rect class="d-ok" x="456" y="{y - 10}" width="10" height="10"/>' if ok else f'<rect x="456" y="{y - 10}" width="10" height="10" fill="#FFB020"/>'
    return f'<text class="d-t" x="24" y="{y}">{a}</text><text class="d-s" x="92" y="{y}" style="font-size:13px">{b}</text><text class="d-s" x="290" y="{y}" style="font-size:13px">{c}</text>{mark}<path class="d-thin" d="M24 {y + 12}H496"/>'

ART_WIRE = f'''<svg viewBox="0 0 520 300" role="img" aria-label="A pin table comparing the I/O list with the wiring drawing, pin by pin. One pin is flagged because the drawing puts the signal on a different pin.">
  <text class="d-s" x="24" y="30">Pin</text><text class="d-s" x="92" y="30">I/O list</text><text class="d-s" x="290" y="30">Wiring drawing</text><text class="d-s" x="440" y="30">Match</text>
  <path d="M24 40H496" stroke="#55636f" fill="none"/>
  {trow(68, "B19", "Glove box switch", "Glove box switch")}
  {trow(108, "B21", "Start button, contact 4", "Start button, contact 4")}
  {trow(148, "D8", "Steering-wheel supply", "Dashboard supply", False)}
  {trow(188, "D14", "Rear lighting CAN high", "Rear lighting CAN high")}
  {trow(228, "E9", "Handle touch sensor", "Handle touch sensor")}
  <text class="d-s" x="24" y="274">1 of 5 pins differs. The drawing wins, and the list is corrected.</text>
</svg>'''

ART_SPEC = f'''<svg viewBox="0 0 520 300" role="img" aria-label="An ECU specification sheet with numbered requirements, each with a verification method, next to the ECU's connectors and buses.">
  <rect class="d-box" x="20" y="20" width="290" height="260"/>
  <text class="d-t" x="36" y="48">Door module, front left</text><text class="d-s" x="36" y="66">Requirement specification</text>
  <path class="d-thin" d="M36 78H294"/>
  <g class="d-s" style="font-size:12.5px"><text x="36" y="102">REQ-014  Door CAN, 500 kbit/s nominal</text><text x="36" y="128">REQ-027  Window anti-pinch reversal</text><text x="36" y="154">REQ-031  Latch status debounce</text><text x="36" y="180">REQ-044  Diagnostic session control</text><text x="36" y="206">REQ-052  Secure software update</text><text x="36" y="232">REQ-060  Quiescent current limit</text></g>
  <g class="d-s"><text x="36" y="262">Each with an ID and a verification method</text></g>
  {box(350, 30, 150, 44, "Connector A", "window motor")}{box(350, 92, 150, 44, "Connector B", "latch, CAN, supply")}{box(350, 154, 150, 44, "Connector C", "mirror")}{box(350, 216, 150, 44, "Connector D", "switches")}
  <path class="d-wire d-can" d="M310 114H350"/><path class="d-thin" d="M310 52H350M310 176H350M310 238H350"/>
</svg>'''

ART_CODE = f'''<svg viewBox="0 0 520 300" role="img" aria-label="A behavior model becomes C code and unit tests for one feature. The features deployed on one ECU are integrated into that ECU's software, and the ECUs into the vehicle package.">
  {box(20, 30, 130, 50, "Behavior model", "states, signals")}
  <path class="d-wire d-eth" d="M150 55H190"/>
  <rect class="d-core" x="190" y="20" width="310" height="110"/>
  <g class="d-code" xml:space="preserve"><text x="204" y="44">void MirrorFold_Step(void) {{</text><text x="204" y="62">  switch (state) {{</text><text x="204" y="80">    case FOLDING:</text><text x="204" y="98">      if (t_ms &gt;= CAL_FOLD_MS)</text><text x="204" y="116">        state = FOLDED;</text></g>
  <path class="d-wire d-eth" d="M345 130V166"/>
  {box(40, 166, 130, 46, "Feature", "code + unit tests")}{box(195, 166, 130, 46, "Feature", "code + unit tests")}{box(350, 166, 130, 46, "Feature", "code + unit tests")}
  <path class="d-wire d-can" d="M105 212V236H415V212M260 212V236M260 236V250"/>
  {box(170, 250, 180, 40, "ECU software, integrated", None, True)}
</svg>'''

def rel(y, n, w, t):
    return f'<text class="d-t" x="24" y="{y}">{n}</text><rect x="170" y="{y - 12}" width="250" height="12" fill="#26323D"/><rect class="d-ok" x="170" y="{y - 12}" width="{w}" height="12"/><text class="d-s" x="434" y="{y}" style="font-size:13px">{t}</text>'

ART_REL = f'''<svg viewBox="0 0 520 300" role="img" aria-label="A release board listing each ECU with how much of its software delivery is signed off for the vehicle release.">
  <text class="d-s" x="24" y="30">Vehicle release, ECU by ECU</text><path d="M24 40H496" stroke="#55636f" fill="none"/>
  {rel(76, "Center zone", 250, "signed off")}{rel(116, "Front zone", 250, "signed off")}{rel(156, "Door modules", 205, "2 open")}{rel(196, "Seat modules", 150, "4 open")}{rel(236, "Brake control", 95, "evidence due")}
  <text class="d-s" x="24" y="274">What blocks the release is on one screen.</text>
</svg>'''

ART_PKG = f'''<svg viewBox="0 0 520 320" role="img" aria-label="The contents of a generated ECU package: one folder per software component, the integration layer, the test, the AUTOSAR description, a makefile and a manifest.">
  <rect class="d-box" x="20" y="16" width="480" height="288"/>
  <g class="d-code" xml:space="preserve" style="font-size:13.5px">
   <text x="40" y="46">ecu/CZM/</text>
   <text x="40" y="72">  swc/MirrorFold/        MirrorFold.c  .h  test</text>
   <text x="40" y="96">  swc/WindowLifter/      WindowLifter.c  .h  test</text>
   <text x="40" y="120">  swc/CentralLocking/    CentralLocking.c  .h  test</text>
   <text x="40" y="148">  integration/Ecu_CZM.h</text>
   <text x="40" y="172">  integration/Ecu_CZM_Rte.c       signal routing</text>
   <text x="40" y="196">  integration/Ecu_CZM_Schedule.c  task schedule</text>
   <text x="40" y="220">  integration/test/test_Ecu_CZM.c</text>
   <text x="40" y="248">  arxml/CZM_Composition.arxml</text>
   <text x="40" y="272">  Makefile   README.txt   manifest.json</text>
  </g>
</svg>'''

# ------------------------------------------------------------------ home
def row(h, p, items, art, link, linktext, flip=False):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'''<div class="row{" flip" if flip else ""}"><figure class="art">{art}</figure><div><h3>{h}</h3><p>{p}</p><ul>{lis}</ul><a class="more" href="{link}" {NEW}>{linktext}</a></div></div>'''

home = f'''<section class="hero"><div class="wrap">
  <div>
    <h1>The whole vehicle, in one engineering system.</h1>
    <p class="lead">SDVsolution takes a vehicle program from stakeholder need to integrated ECU software: requirements written to the standard, the architecture and wiring checked against each other, a specification for every ECU, and code generated feature by feature.</p>
    <div class="cta"><a class="btn btn-lime" href="#demo">Request a demo</a><a class="btn btn-line" href="platform.html" {NEW}>See the platform</a></div>
    <p class="fine">We walk you through the demo, then give your team access by email.</p>
  </div>
  <div>{TOPO}</div>
</div></section>

<div class="strip"><div class="wrap"><span>Aligned to the standards your customers ask for</span><b>Automotive SPICE</b><b>ISO/IEC/IEEE 29148</b><b>ISO 26262</b><b>ISO/SAE 21434</b></div></div>

<section class="band band-black" id="work"><div class="wrap">
  <div class="head"><h2>What your team does in it</h2><p class="lead">Five jobs that usually live in five tools and a shared drive. Here they share one model, so a change in one shows up in the others.</p></div>
  {row("Write requirements that pass an assessment", "System, software and hardware requirements in one connected model, with architecture, detailed design and state machines beside them.", ["Every requirement checked as you type: one statement, verifiable, unambiguous", "Trace from stakeholder need to test, in both directions", "Reviews, approvals and versioned baselines with diff and restore"], ART_V, "platform.html#requirements", "How requirements work")}
  {row("Check the wiring against the I/O list", "Import the communication matrix and the wiring drawings. The platform traces every wire and compares it, pin by pin, with what each ECU says it provides.", ["CAN, LIN, Ethernet and FlexRay from DBC, LDF and ARXML", "Wiring drawings read from PDF, net by net", "Wrong pins, unwired outputs and missing signals listed for you"], ART_WIRE, "platform.html#architecture", "How the cross-check works", True)}
  {row("Hand each supplier a complete ECU specification", "A specification for every ECU, built from its own buses, connectors and safety level, so the supplier gets requirements that match the vehicle it goes into.", ["Hardware, software, diagnostics, update, cybersecurity and verification", "Connector pin-outs and I/O lists per ECU", "Every requirement with an ID and a verification method"], ART_SPEC, "platform.html#ecu", "What an ECU specification holds")}
  {row("Generate the software, feature by feature", "Describe a feature as a behavior model. The software factory writes its C code and unit tests, then integrates the features deployed on each ECU into that ECU's software.", ["C code and unit tests per feature", "ECU integration: signal routing, schedule, integration test", "The complete vehicle as one package, ECU by ECU"], ART_CODE, "software-factory.html", "How the software factory works", True)}
  {row("Know which ECUs are ready for the release", "Every ECU delivers against a common vehicle release. Track each deliverable with its evidence and sign off ECU by ECU.", ["Deliverables and evidence per ECU", "Sign-off per ECU and per release", "Safety, cybersecurity and review status on one dashboard"], ART_REL, "platform.html#release", "How release tracking works")}
</div></section>

<section class="band on-paper" id="parts"><div class="wrap">
  <div class="head"><h2>Six parts, one system</h2><p class="lead">Each part does one job. They share the same vehicle model, which is what lets the software factory generate code from the requirements your engineers approved.</p></div>
  <div class="blocks">
    <div class="block"><h3>AI platform</h3><p>The assistant your engineers talk to. Drop in a PDF, a spreadsheet or a bus file and ask in plain language.</p></div>
    <div class="block"><h3>Engineering knowledge graph</h3><p>Features, requirements, signals, pins, ECUs and tests as one connected model. Click anything to see what it depends on.</p></div>
    <div class="block"><h3>AI agents</h3><p>They draft requirements, propose behavior models and review them against the standard. Your engineers approve every result.</p></div>
    <div class="block"><h3>AI software factory</h3><p>Turns an approved behavior model into C code and unit tests, one feature at a time.</p></div>
    <div class="block"><h3>ECU platform</h3><p>The specification, the I/O list and the integrated software for each ECU in the vehicle.</p></div>
    <div class="block"><h3>AI system integration</h3><p>Checks the signals between ECUs and assembles the complete vehicle software, ready for the bench.</p></div>
  </div>
</div></section>

<section class="band band-ink" id="nvidia"><div class="wrap">
  <div class="head"><p class="kicker">Built for NVIDIA DRIVE AGX Thor</p><h2>Bring the NVIDIA DRIVE hardware. Integrate the complete vehicle faster.</h2><p class="lead">You choose NVIDIA DRIVE AGX Thor for central compute. SDVsolution brings the vehicle around it: the architecture, the communication, the ECU specifications and the release tracking that connect the computer to every other ECU.</p></div>
  <div class="gens">
    <div class="gen"><div class="tag">Generation 1</div><h3>Driver assistance on NVIDIA DRIVE AGX Thor</h3><p>The driver-assistance ECU is built on Thor. The cockpit keeps its own computer and the zone controllers stay as they are.</p></div>
    <div class="gen"><div class="tag">Generation 2</div><h3>Driver assistance and cockpit on one Thor</h3><p>Both run on a single Thor-based central computer, with the zone controllers around it.</p></div>
  </div>
  <p style="margin-top:34px"><a class="more" href="nvidia-drive.html" {NEW}>See both architectures in detail</a></p>
  <p class="legal">NVIDIA and NVIDIA DRIVE are trademarks of NVIDIA Corporation. SDVsolution is an independent company and is not affiliated with, sponsored by or endorsed by NVIDIA.</p>
</div></section>

<section class="band band-black" id="flow"><div class="wrap">
  <div class="head"><h2>From a need to running software</h2></div>
  <div class="steps five">
    <div class="step"><h3>Capture</h3><p>Turn stakeholder needs into system requirements with a guided template.</p></div>
    <div class="step"><h3>Derive</h3><p>Roll them down to software and hardware, and allocate each feature to its ECUs.</p></div>
    <div class="step"><h3>Model</h3><p>Describe each feature's behavior: states, signals, timing and calibration.</p></div>
    <div class="step"><h3>Generate</h3><p>Produce the code and tests for each feature and integrate them per ECU.</p></div>
    <div class="step"><h3>Release</h3><p>Review, baseline, and sign off each ECU against the vehicle release.</p></div>
  </div>
</div></section>

<section class="band on-paper" id="solutions"><div class="wrap">
  <div class="head"><h2>License one feature, one ECU or the whole vehicle</h2><p class="lead">Take the generated software at the size your program needs, or license the platform and keep the engineering in house.</p></div>
  <div class="scopes">
    <div class="scope"><div class="bar" style="width:25%"></div><h3>Feature</h3><p>One vehicle feature: its requirements, behavior model, code and tests.</p></div>
    <div class="scope"><div class="bar" style="width:50%"></div><h3>ECU</h3><p>Every feature deployed on one ECU, integrated into that ECU's software.</p></div>
    <div class="scope"><div class="bar" style="width:75%"></div><h3>Domain</h3><p>A complete domain, such as body, energy, cockpit or driver assistance.</p></div>
    <div class="scope"><div class="bar" style="width:100%"></div><h3>Complete vehicle</h3><p>Every ECU and the integration between them, with bench, HIL and lab-car support.</p></div>
  </div>
  <p style="margin-top:34px"><a class="more" href="solutions.html" {NEW}>Compare the ways to work with us, and the plans</a></p>
</div></section>
{contact()}'''

page("index.html", "SDVsolution: one engineering system for the software-defined vehicle",
     "SDVsolution takes a vehicle program from stakeholder need to integrated ECU software: requirements to Automotive SPICE, architecture and wiring cross-checks, ECU specifications, and code generated per feature, per ECU or for the complete vehicle.", home)

# ------------------------------------------------------------------ platform
def phero(crumb, h1, lead):
    return f'''<section class="phero"><div class="wrap"><p class="crumb"><a href="index.html" {NEW}>SDVsolution</a> / {crumb}</p><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'''

platform = phero("Platform", "One model for requirements, architecture and every ECU.", "The platform holds the vehicle as a single connected model. Requirements, signals, connector pins, ECUs and tests are all in it, so the tool can check them against each other instead of leaving that to a review meeting.") + f'''
<section class="band band-black" id="requirements"><div class="wrap">
  <div class="row"><figure class="art">{ART_V}</figure><div><h3>Requirements across the V</h3><p>System, software and hardware requirements sit in one model with the architecture, the detailed design and the state machines they lead to.</p><ul><li>A guided template for the requirement sentence, so each one has a trigger, a condition and a response</li><li>A live check on every requirement: one statement, verifiable, unambiguous</li><li>Trace in both directions, from stakeholder need to the test that proves it</li><li>Impact view: click a requirement or a signal and see everything a change would touch</li></ul></div></div>
  <div class="row flip" id="reviews"><figure class="art">{ART_REL}</figure><div><h3>Reviews, baselines and readiness</h3><p>Approvals and configuration management are part of the model, not a separate process on paper.</p><ul><li>Joint review with comments, decisions and approvals recorded</li><li>Versioned baselines with a diff between any two, and restore</li><li>A readiness dashboard across safety, cybersecurity, review status and the quality check</li><li id="release">Release tracking: deliverables, evidence and sign-off for every ECU</li></ul></div></div>
</div></section>

<section class="band band-ink" id="architecture"><div class="wrap">
  <div class="row"><figure class="art">{ART_WIRE}</figure><div><h3>Vehicle architecture and communication</h3><p>The topology, the communication matrix and the wiring are imported and then compared with each other.</p><ul><li>Buses, frames and signals from DBC, LDF and ARXML</li><li>Wiring drawings read from PDF: every wire traced from pin to pin</li><li>I/O list against drawing: wrong pins, outputs with no wire, wired pins missing from the list</li><li>Bus membership against the drawings: nodes that have signals but no wiring, and the reverse</li></ul></div></div>
  <div class="row flip" id="ecu"><figure class="art">{ART_SPEC}</figure><div><h3>A specification for every ECU</h3><p>Each ECU gets its own requirement specification, generated from the buses it is on, the connectors it has and the safety level it carries.</p><ul><li>Hardware constraints, software, diagnostics, update, cybersecurity and verification</li><li>Connector pin-outs and an I/O list per ECU</li><li>Features deployed to the ECUs that host them, including features that span several ECUs</li><li>Ready to hand to the ECU supplier</li></ul></div></div>
</div></section>

<section class="band on-paper"><div class="wrap">
  <div class="head"><h2>The assistant reads what you already have</h2><p class="lead">Drop a file into the assistant and ask in plain language. It answers from your live model and drafts requirements and updates for your engineers to review. It supports your team; it does not replace engineering judgment.</p></div>
  <div class="scroll"><table class="tbl">
    <tr><th>File</th><th>What the platform does with it</th></tr>
    <tr><td>PDF, Word</td><td>Reads specifications and standards, and drafts requirements from them</td></tr>
    <tr><td>Excel</td><td>Imports requirement lists, I/O lists and release plans</td></tr>
    <tr><td>DBC, LDF</td><td>Imports CAN and LIN buses with their frames and signals</td></tr>
    <tr><td>ARXML</td><td>Imports the system description: clusters, ECUs, signals and software components</td></tr>
    <tr><td>Wiring drawings (PDF)</td><td>Traces every net and builds the pin-to-pin connection list</td></tr>
  </table></div>
</div></section>

<section class="band band-black"><div class="wrap">
  <div class="head"><h2>Where it sits in Automotive SPICE</h2><p class="lead">The platform is organised around the process areas an assessor will ask about.</p></div>
  <div class="scroll"><table class="tbl">
    <tr><th>Process area</th><th>In the platform</th></tr>
    <tr><td>System engineering</td><td>System requirements, system architecture, integration and qualification test (SYS.2 to SYS.5)</td></tr>
    <tr><td>Software engineering</td><td>Software requirements, architecture, detailed design and unit construction, with unit, integration and qualification test (SWE.1 to SWE.6)</td></tr>
    <tr><td>Hardware engineering</td><td>Hardware requirements, design and verification (HWE.1 to HWE.4)</td></tr>
    <tr><td>Supporting processes</td><td>Joint review, configuration management and change request management (SUP.4, SUP.8, SUP.10)</td></tr>
    <tr><td>Safety and cybersecurity</td><td>Safety level and cybersecurity attributes on each requirement, in line with ISO 26262 and ISO/SAE 21434</td></tr>
  </table></div>
  <p style="margin-top:34px"><a class="more" href="software-factory.html" {NEW}>Next: how the software factory turns the model into code</a></p>
</div></section>
{contact()}'''
page("platform.html", "Platform | SDVsolution", "Requirements across the Automotive SPICE V, vehicle architecture and wiring cross-checks, a specification for every ECU, reviews, baselines and release tracking, in one connected model.", platform)

# ------------------------------------------------------------------ software factory
factory = phero("Software factory", "Code for each feature. Software for each ECU. One package for the vehicle.", "A behavior model describes what a feature does. The software factory turns each approved model into C code and unit tests, then integrates the features deployed on an ECU into the software for that ECU.") + f'''
<section class="band band-black"><div class="wrap">
  <div class="head"><h2>How a feature becomes software</h2></div>
  <div class="steps">
    <div class="step"><h3>Model the behavior</h3><p>States, transitions, inputs, outputs, timing and calibration values. An agent can propose the model from the feature's requirements; an engineer approves it.</p></div>
    <div class="step"><h3>Generate the feature</h3><p>C source and header for the feature, with unit tests that drive it through its scenarios and check outputs, states and timing.</p></div>
    <div class="step"><h3>Integrate the ECU</h3><p>Every feature deployed on the ECU is wired together: signals routed between features, a schedule, and an integration test for the whole ECU.</p></div>
    <div class="step"><h3>Assemble the vehicle</h3><p>One package with every ECU, plus a list of the signals that cross between ECUs so the buses can be checked.</p></div>
  </div>
</div></section>

<section class="band band-ink"><div class="wrap">
  <div class="row"><figure class="art">{ART_CODE}</figure><div><h3>The target ECU comes from the deployment</h3><p>You decide once where each feature runs. A window feature runs on the door modules, a seat feature on the seat modules, climate on the front zone. The factory reads that deployment and builds each ECU from the features it hosts.</p><ul><li>A feature can run on several ECUs, such as all four door modules</li><li>Two features that write the same signal are caught before code is generated</li><li>Calibration values stay separate per feature</li></ul></div></div>
  <div class="row flip"><figure class="art">{ART_PKG}</figure><div><h3>What is in an ECU package</h3><p>A folder you can build. The makefile compiles the package and runs the integration test.</p><ul><li>One software component per feature, with its own unit test</li><li>The integration layer: ECU header, signal routing and task schedule</li><li>An integration test that replays each feature's scenarios through the ECU's inputs</li><li>An AUTOSAR composition description (ARXML) and a manifest of what was built</li></ul></div></div>
</div></section>

<section class="band on-paper"><div class="wrap">
  <div class="head"><h2>How it is checked</h2><p class="lead">Generated code is only useful if you can trust it, so the factory tests what it writes.</p></div>
  <div class="cols">
    <div><h3>Compiled with strict warnings</h3><p>Generated packages are compiled with the compiler's warnings turned on and treated as errors.</p></div>
    <div><h3>Tested at two levels</h3><p>Each feature has unit tests. Each ECU has an integration test that runs every feature's scenarios again once the features are wired together.</p></div>
    <div><h3>The tests are tested</h3><p>We plant deliberate faults in the integration layer and check that the integration test catches them.</p></div>
    <div><h3>Your engineers stay in charge</h3><p>Models are proposed, then reviewed and approved by an engineer. Only approved models go into a release package.</p></div>
  </div>
</div></section>

<section class="band band-black"><div class="wrap">
  <div class="head"><h2>Take the software at the size you need</h2></div>
  <div class="scroll"><table class="tbl">
    <tr><th>License</th><th>What you receive</th></tr>
    <tr><td>Per feature</td><td>The code and unit tests for one feature, with its requirements and behavior model</td></tr>
    <tr><td>Per ECU</td><td>The integrated software for one ECU: every feature deployed on it, the integration layer and the integration test</td></tr>
    <tr><td>Complete vehicle</td><td>Every ECU package and the signals between them, with support on the integration bench, hardware-in-the-loop and the lab car</td></tr>
  </table></div>
  <p style="margin-top:34px"><a class="more" href="solutions.html" {NEW}>See the ways to work with us, and the plans</a></p>
</div></section>
{contact("See a feature go from model to code.", "We generate a sample feature in the demo and show you the package it produces. We reply by email.")}'''
page("software-factory.html", "Software factory | SDVsolution", "The SDVsolution software factory generates C code and unit tests for each vehicle feature from its behavior model, integrates the features deployed on each ECU, and assembles the complete vehicle software package.", factory)

# ------------------------------------------------------------------ NVIDIA DRIVE
def gen_svg(two):
    cc = box(210, 30, 220, 56, "NVIDIA DRIVE AGX Thor", "driver assistance + cockpit" if two else "driver assistance", True)
    cockpit = "" if two else box(470, 30, 150, 56, "Cockpit computer", "its own unit")
    link = "" if two else '<path class="d-wire d-eth" d="M430 58H470"/>'
    return f'''<svg viewBox="0 0 640 300" role="img" aria-label="{"One Thor-based central computer for driver assistance and cockpit" if two else "A Thor-based driver-assistance computer beside a separate cockpit computer"}, connected by Ethernet to three zone controllers, with cameras, radars and displays.">
  <path class="d-wire d-eth" d="M320 86V130M320 130H110V170M320 130V170M320 130H530V170"/>{link}
  <path class="d-wire d-can" d="M110 222V250M320 222V250M530 222V250"/>
  {cc}{cockpit}
  {box(20, 30, 150, 56, "Cameras, radars", "ultrasonic sensors")}<path class="d-wire d-eth" d="M170 58H210"/>
  {box(40, 170, 140, 52, "Front zone")}{box(250, 170, 140, 52, "Center zone")}{box(460, 170, 140, 52, "Rear zone")}
  <g class="d-s" text-anchor="middle"><text x="110" y="268">climate, chassis</text><text x="320" y="268">body, doors, seats</text><text x="530" y="268">tailgate, trailer</text></g>
</svg>'''

nvidia = phero("NVIDIA DRIVE", "The vehicle around NVIDIA DRIVE AGX Thor.", "Choosing the central computer is one decision. Connecting it to the dozens of other ECUs in the vehicle is the larger job. SDVsolution models that vehicle for you, in two ready-made architectures.") + f'''
<section class="band band-black"><div class="wrap">
  <div class="row"><figure class="art">{gen_svg(False)}<figcaption>Generation 1</figcaption></figure><div><h3>Generation 1: driver assistance on Thor</h3><p>The driver-assistance ECU is built on NVIDIA DRIVE AGX Thor. The cockpit keeps its own computer and the zone controllers stay as they are.</p><ul><li>The lowest-change path onto NVIDIA DRIVE</li><li>Driver-assistance interfaces, cameras, radars and ultrasonic sensors modeled</li><li>Available as a ready-made project in SDVsolution</li></ul></div></div>
  <div class="row flip"><figure class="art">{gen_svg(True)}<figcaption>Generation 2</figcaption></figure><div><h3>Generation 2: driver assistance and cockpit on one Thor</h3><p>Both functions run on a single Thor-based central computer, with the zone controllers around it.</p><ul><li>One central computer in place of two</li><li>Driver-assistance and cockpit interfaces on one ECU specification</li><li>Cockpit audio, displays and cameras brought onto the central computer's interfaces</li><li>Available as a ready-made project in SDVsolution</li></ul></div></div>
</div></section>

<section class="band on-paper"><div class="wrap">
  <div class="head"><h2>What we bring to a Thor-based program</h2></div>
  <div class="four">
    <div><b>Vehicle architecture</b><span>The topology around the central computer: zone controllers, sensors, actuators and power distribution.</span></div>
    <div><b>Communication matrix</b><span>CAN, LIN and Ethernet frames and signals for every ECU, with the interface requirements derived from them.</span></div>
    <div><b>ECU specifications</b><span>A requirement specification for each ECU in the vehicle, ready to hand to its supplier.</span></div>
    <div><b>Release tracking</b><span>Software delivery, evidence and sign-off for every ECU against each vehicle release.</span></div>
  </div>
</div></section>

<section class="band band-ink"><div class="wrap">
  <div class="head"><h2>Does the hardware cover the vehicle?</h2><p class="lead">Before you commit to an architecture, the platform compares what the vehicle needs from its central computer with the interfaces the hardware provides, line by line.</p></div>
  <div class="scroll"><table class="tbl">
    <tr><th>What is compared</th><th>Why it matters</th></tr>
    <tr><td>Camera and display links</td><td>Whether every camera and display in the vehicle has a port, in both generations</td></tr>
    <tr><td>Ethernet, CAN and LIN</td><td>Whether the vehicle's buses can all reach the central computer, directly or through a zone controller</td></tr>
    <tr><td>Audio</td><td>Whether the cockpit's audio buses move onto the central computer in Generation 2</td></tr>
    <tr><td>Supply and environment</td><td>Whether voltage range and temperature limits fit where the unit is mounted</td></tr>
    <tr><td>Open gaps</td><td>Each gap becomes a requirement with an owner, so it is closed on purpose and not found on the bench</td></tr>
  </table></div>
  <p class="legal">NVIDIA and NVIDIA DRIVE are trademarks of NVIDIA Corporation. SDVsolution is an independent company and is not affiliated with, sponsored by or endorsed by NVIDIA. Hardware capabilities are those published by NVIDIA; check the current NVIDIA documentation for your hardware revision.</p>
</div></section>
{contact("Walk through a Thor-based vehicle with us.", "We open the Generation 1 and Generation 2 projects and show you the architecture, the communication and the ECU specifications. We reply by email.")}'''
page("nvidia-drive.html", "Built for NVIDIA DRIVE AGX Thor | SDVsolution", "SDVsolution models the vehicle around NVIDIA DRIVE AGX Thor in two ready-made architectures: driver assistance on Thor, and driver assistance and cockpit on one Thor. Architecture, communication, ECU specifications and release tracking.", nvidia)

# ------------------------------------------------------------------ solutions
solutions = phero("Solutions and plans", "Two ways to work with us, at four sizes.", "Hand us the vehicle side and receive the software, or license the platform and keep the engineering in your own team. Either way, you choose how much of the vehicle it covers.") + f'''
<section class="band band-black"><div class="wrap">
  <div class="cols">
    <div><h3 style="color:#fff;font-size:34px">Full-stack integration</h3><p>SDVsolution takes the vehicle side end to end: requirements, generated software and ECU integration across the complete vehicle, delivered against your vehicle releases.</p></div>
    <div><h3 style="color:#fff;font-size:34px">Tool license</h3><p>Your engineering stays in house. Your teams work in the SDVsolution platform under a license, with support from us when you need it.</p></div>
  </div>
</div></section>

<section class="band on-paper"><div class="wrap">
  <div class="head"><h2>Choose the size</h2></div>
  <div class="scopes">
    <div class="scope"><div class="bar" style="width:25%"></div><h3>Feature</h3><p>One vehicle feature, end to end: its requirements, behavior model, code and tests.</p></div>
    <div class="scope"><div class="bar" style="width:50%"></div><h3>ECU or sub-system</h3><p>The features on one ECU, or a group of related features and the ECUs that deliver them, such as exterior lighting.</p></div>
    <div class="scope"><div class="bar" style="width:75%"></div><h3>Domain</h3><p>A complete vehicle domain, such as body, energy, cockpit or driver assistance.</p></div>
    <div class="scope"><div class="bar" style="width:100%"></div><h3>Complete vehicle</h3><p>Every domain, every ECU and the integration between them, with integration bench, HIL and lab-car support.</p></div>
  </div>
</div></section>

<section class="band band-ink" id="plans"><div class="wrap">
  <div class="head"><h2>Start with the demo. License what you need.</h2><p class="lead">We show you the demo and give your team access by email. When you are ready, we scope a license to your program and price it by quote.</p></div>
  <div class="plans">
    <div class="plan"><h3>Demo</h3><div class="amt">Free</div><div class="per">by request, access by email</div><ul><li>A walkthrough with our team</li><li>Then access for your team, by email</li><li>A sample feature from system requirement to software and hardware</li><li>Four door modules to explore</li></ul><a class="btn btn-line" href="#demo">Request a demo</a></div>
    <div class="plan"><h3>Custom</h3><div class="amt">By quote</div><div class="per">scoped to your program</div><ul><li>Feature, ECU, domain or complete-vehicle scope</li><li>Full-stack integration or a tool license</li><li>NVIDIA DRIVE AGX Thor architectures, Generation 1 and 2</li><li>Communication matrix, ARXML, DBC, LDF and connector pin-outs</li><li>Integrations with the requirements tools you already use</li><li>Single sign-on, access controls, audit trail and assessment support</li></ul><a class="btn btn-lime" href="#demo">Get a quote</a></div>
  </div>
</div></section>

<section class="band band-black"><div class="wrap">
  <div class="head"><h2>Questions we are asked</h2></div>
  <details><summary>Who can sign up?</summary><p>Access is by invitation. Request a demo, and after the walkthrough we enable the email addresses of your team.</p></details>
  <details><summary>Do we need training?</summary><p>No. If you have used a requirements tool, the tree, the document view and the import and export will be familiar. The assistant answers questions inside the app.</p></details>
  <details><summary>Does the AI replace our engineers?</summary><p>No. Agents draft requirements and propose behavior models. An engineer reviews and approves each one, and only approved work goes into a baseline or a release package.</p></details>
  <details><summary>Can we keep using our current requirements tool?</summary><p>Yes. Requirements can be imported and exported, and the Custom plan includes integrations with the tools your program already uses.</p></details>
  <details><summary>What do we receive when we license generated software?</summary><p>Source code, tests and a build file, for a feature, an ECU or the complete vehicle. The software factory page lists the contents of a package.</p></details>
</div></section>
{contact("Tell us the size of your program.", "Name the feature, the ECU or the vehicle, and we will come back with a scope and a quote. We reply by email.")}'''
page("solutions.html", "Solutions and plans | SDVsolution", "Work with SDVsolution through full-stack integration or a tool license, at the size of one feature, one ECU, one domain or the complete vehicle. Start with a free demo; licenses are priced by quote.", solutions)

open(os.path.join(OUT, "assets", "site.js"), "w").write('''(function(){
  var f=document.getElementById('demoForm'), s=document.getElementById('demoStatus');
  if(!f) return;
  f.addEventListener('submit', function(e){
    e.preventDefault();
    s.style.color='#9AA8B4'; s.textContent='Sending your request.';
    fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}}).then(function(r){
      if(r.ok){ f.reset(); s.style.color='#9CFF3A'; s.textContent='Request sent. We will reply by email.'; }
      else { s.style.color='#FFB020'; s.textContent='The request was not sent. Check the email address and send it again.'; }
    }).catch(function(){ s.style.color='#FFB020'; s.textContent='The request was not sent because the connection dropped. Send it again.'; });
  });
})();
''')
print("built")
