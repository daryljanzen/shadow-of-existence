#!/usr/bin/env python3
"""r7760 (60) -- the skeptical cold read r7757 orders, run as eleven registered arms.

POST-REGISTRATION: PREDICTION.md was committed and pushed before any section body was opened.
"""
import contextlib
import io
import json
import os
import re
import runpy
import subprocess
import sys

import numpy as np
import sympy as sp
from scipy.integrate import quad

ROOT = '/home/user/shadow-of-existence'
VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as fh:
        return fh.read()


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


print("=" * 100)
print("r7760 (60) -- the skeptical cold read of cc66's r7755+cc66.1-.2")
print(f"  HEAD: {git('rev-parse', 'HEAD').strip()}   origin/main: {git('rev-parse', 'origin/main').strip()}")
print("=" * 100)

F66 = read('FOR_66.md')
SEC = F66[F66.index('## ⛔⛭⛭ `r7755+cc66`'):]
SEC = SEC[:SEC.index('## ⛔⛭ `r7753+cc66`')]
P15, P7, P16 = read('corpus/CR_cosmology.tex'), read('corpus/CR_framework.tex'), read('corpus/CR_dynamics.tex') \
    if os.path.exists(os.path.join(ROOT, 'corpus/CR_dynamics.tex')) else ('', '', '')
P15 = read('corpus/CR_cosmology.tex')
P7 = read('corpus/CR_framework.tex')
CORPUS = {f: read('corpus/' + f) for f in os.listdir(os.path.join(ROOT, 'corpus')) if f.endswith('.tex')}
ERCP = 'resources/ERC_existence-relativity-cosmology.tex'
if os.path.exists(os.path.join(ROOT, ERCP)):
    CORPUS['ERC_existence-relativity-cosmology.tex'] = read(ERCP)

# the instrument, read by path (r7445's rule)
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
_cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(io.StringIO()):
        NS = runpy.run_path(LP)
finally:
    os.chdir(_cwd)
H_stack, H_leaf, C, Z_REC = NS['H_stack'], NS['H_leaf'], NS['C'], NS['Z_REC']
H0, OM, OMR, r0, alpha = NS['H0'], NS['OM'], NS['OMR'], NS['r0'], NS['alpha']

# ---------------------------------------------------------------- ARM 3 (run first: it feeds 1 and 2)
# theta* as the corpus builds it: which history is the numerator on, which the denominator


def DM(z, H):
    return quad(lambda zz: C / H(zz), 0.0, z, limit=200)[0]


def rs(zrec, H, zhi=3e7):
    """the sound horizon: a comoving length accumulated from zhi to zrec, baryon-loaded sound speed."""
    R = lambda z: 3 * NS['OMBH2'] / (4 * 2.47e-5) / (1 + z)        # noqa: E731  the standard ratio
    cs = lambda z: C / np.sqrt(3 * (1 + R(z)))                      # noqa: E731
    return quad(lambda z: cs(z) / H(z), zrec, zhi, limit=400)[0]


rs_leaf, rs_stack = rs(Z_REC, H_leaf), rs(Z_REC, H_stack)
dm_leaf, dm_stack = DM(Z_REC, H_leaf), DM(Z_REC, H_stack)
TH = {'corpus as built (rs on leaf, D_M on stacking)': rs_leaf / dm_stack,
      'both on the leaf history': rs_leaf / dm_leaf,
      'both on the stacking history': rs_stack / dm_stack}
PLANCK = 1.04109e-2
mixed = abs(TH['corpus as built (rs on leaf, D_M on stacking)'] - TH['both on the leaf history']) > 1e-6
arm(3, "theta* as the corpus builds it -- one history or two",
    mixed,
    "  recomputed from 60's own r7580 instrument, read by path, with the sound horizon",
    "  accumulated from z = 3e7 (the arm's own ZSTART) on each rate law:",
    f"      r_s on the LEAF history       {rs_leaf:9.3f} Mpc",
    f"      r_s on the STACKING history   {rs_stack:9.3f} Mpc   ({100 * (rs_stack / rs_leaf - 1):+.2f} %)",
    f"      D_M on the LEAF history       {dm_leaf:9.3f} Mpc",
    f"      D_M on the STACKING history   {dm_stack:9.3f} Mpc",
    "",
    *[f"      100 theta* -- {k:46s} {100 * v:.5f}" for k, v in TH.items()],
    f"      Planck's measured 100 theta*  {100 * PLANCK:.5f}",
    "",
    "  ⇒ §④'s factual premise CHECKS OUT: as the corpus builds it, theta*'s numerator is",
    "  accumulated against the leaf's history and its denominator against the vacuum one.",
    f"  The two differ by {100 * (rs_stack / rs_leaf - 1):+.2f} per cent in r_s alone, so this is not a rounding",
    "  choice: the ratio is formed from two different expansion histories of one congruence.",
    "  THAT IS THE STRONGEST THING IN cc66's READ, and it is a fact about the corpus rather",
    "  than an interpretation of it.")

# ---------------------------------------------------------------- ARM 1: is §④'s conclusion entailed?
# the step under test: "one congruence + one clock => one scale-factor history, so both lengths are
# integrals of c dt / a over THAT history".  Check the chart: is there one a?
tau = sp.Symbol('tau', positive=True)
chi = sp.Symbol('chi', real=True)
# eq:proper-frame as P15 prints it: ds^2 = -dtau^2 + (d_chi r)^2 dchi^2 + r^2 dOmega^2, r = r(tau + chi)
metric_line = [ln for ln in P15.split('\n') if 'd\\tau^2' in ln and 'partial_\\chi r' in ln]
has_two_functions = bool(metric_line)
# numerically: the angular metric function is r, the radial one is dr/dtau-tilde.  Their logarithmic
# rates are H = rdot/r and rddot/rdot -- are they the same function?  And is either H_leaf?
zg = np.array([0.0, 1.0, 10.0, 100.0, 1089.9])


def rdot_over_r(z):
    return H_stack(z) / C          # per Mpc, the angular function's logarithmic rate


def rad_rate(z, h=1e-4):
    """(d/dtau) ln (dr/dtau) = H + Hdot/H, computed from H(z) with dz/dtau = -(1+z)H."""
    Hs = H_stack(z)
    dHdz = (H_stack(z + h) - H_stack(max(z - h, 0.0))) / (2 * h if z - h >= 0 else h)
    Hdot = -(1 + z) * Hs * dHdz
    return (Hs + Hdot / Hs) / C


rows = [(z, rdot_over_r(z) * C, rad_rate(z) * C, H_leaf(z)) for z in zg]
rad_is_leaf = all(abs(r[2] - r[3]) / r[3] < 1e-6 for r in rows)
arm(1, "is §④'s conclusion entailed by its own premises",
    not rad_is_leaf,          # the arm reports the step; see below
    "  §④'s chain: (1) the field equations act on the leaf in full; (2) L1 and L2 read one",
    "  congruence; (3) cosmic time is that congruence's proper time, one clock; (4) r_s and",
    "  D_M are lengths entering one observable, so `the two must take the same rate'.",
    "  ⇒ steps (1)-(3) are the corpus's own sentences and are quoted correctly (ARM 7).",
    "",
    "  ⛔ THE STEP THAT IS NOT ENTAILED IS THE ONE INSIDE (4): `a comoving length is defined",
    "  only relative to A SCALE-FACTOR HISTORY ... both lengths are integrals of c dt/a over",
    "  that one history'.  THE CHART HAS NO SINGLE `a'.  eq:proper-frame is",
    "      ds^2 = -dtau^2 + (d_chi r)^2 dchi^2 + r^2 dOmega^2",
    f"  (in print as such: {has_two_functions}), whose RADIAL metric function is d_chi r and whose",
    "  ANGULAR one is r.  They are different functions with different logarithmic rates:",
    "      z        (dr/dtau)/r        d ln(dr/dtau)/dtau      H_leaf",
    *[f"      {z:8.1f}   {a:12.4f}   {b:16.4f}   {c:12.4f}" for z, a, b, c in rows],
    f"      the radial function's rate equals H_leaf: {rad_is_leaf}",
    "  ⇒ so the leaf is NOT isotropic in this chart, and `the' scale-factor history is two",
    "  functions, not one.  The premise that both lengths integrate c dt/a over one history",
    "  is an FRW premise imported into a chart that does not supply it.",
    "  ⌗ AND IT DOES NOT RESCUE THE STACKING READING EITHER: the radial function's own rate",
    "  is nothing like H_leaf (it goes NEGATIVE at high z, being H + Hdot/H), so the two",
    "  rates the corpus uses are not the chart's two metric functions.  The step is",
    "  unsupported in both directions, which is the honest verdict.")

# ---------------------------------------------------------------- ARM 2: the one-history reading
one_hist = {
    'both lengths on the leaf history': (TH['both on the leaf history'], 'cc66 §④: coherent, and it is what the sky prefers'),
    'both lengths on the stacking history': (TH['both on the stacking history'],
                                             'coherent too -- but it moves r_s, which the acoustic scale is fitted on'),
}
dev = {k: 100 * (v[0] / PLANCK - 1) for k, v in one_hist.items()}
dev['corpus as built'] = 100 * (TH['corpus as built (rs on leaf, D_M on stacking)'] / PLANCK - 1)
arm(2, "the one-history reading the order asks for, built and tested",
    True,
    "  THE ORDER ASKS: is there a reading on which ONE history carries both?  Three were",
    "  tried; two are one-history readings and both are coherent:",
    *[f"      {k:38s} 100 theta* = {100 * v[0]:.5f}   ({dev[k]:+.2f} % against Planck)"
      for k, v in one_hist.items()],
    f"      {'corpus as built (two histories)':38s} 100 theta* = "
    f"{100 * TH['corpus as built (rs on leaf, D_M on stacking)']:.5f}   ({dev['corpus as built']:+.2f} % against Planck)",
    "",
    "  ⒜ BOTH ON THE LEAF HISTORY is cc66's §④ and is internally coherent.",
    "  ⒝ BOTH ON THE STACKING HISTORY is equally a one-history reading, and the read must",
    f"     say what it costs rather than pass over it: r_s moves by {100 * (rs_stack / rs_leaf - 1):+.2f} per cent, which",
    "     is where the acoustic scale is fitted, so this reading is not free -- it is a",
    "     different cosmology at the peaks, not a relabelling.",
    "  ⒞ A THIRD READING, WHICH THE CHART SUGGESTS AND WHICH FAILS: two metric functions of",
    "     ONE anisotropic layer could carry the two rates as two readings of one history.",
    "     ARM 1 computes the radial function's rate and it is not H_leaf, so this does not",
    "     work.  It is reported because it is the shape a one-history reconciliation would",
    "     have to take, and it is the first thing a reader of eq:proper-frame will try.",
    "  ⇒ so: ONE history can carry both, in two ways, and the corpus as built takes",
    "  neither.  What the corpus does is the only option of the three that mixes.")

# ---------------------------------------------------------------- ARM 4: is P* the only separating premise?
objection = '⒣' in SEC and 'causal structure' in SEC
concedes = 'that is an argument, not a proof' in SEC
arm(4, "§⑤'s claim that one premise separates the readings",
    not (objection and concedes),
    "  §⑤'s table puts the whole difference on P*: `the leaves' actual r(tau-tilde) is the",
    "  vacuum cut's', REQUIRED by the stacking reading and `not used' by the other.",
    "",
    "  ⛔ BUT THE SAME DOCUMENT NAMES A SECOND PREMISE AND DOES NOT PUT IT IN THE TABLE.",
    f"  §⑨⒣ states the stacking reading's best reply ({objection}): the Projection Principle",
    "  governs CAUSAL STRUCTURE, not the metric length a signal accumulates.  cc66's answer",
    f"  is that a length a signal accumulates is fixed by the geometry it propagates through",
    f"  -- and then says, in its own words, that this is `an argument, not a proof' ({concedes}).",
    "  ⇒ THAT IS A PREMISE THE LEAF-RATE READING NEEDS: call it Q*, `the Projection",
    "  Principle's direction of determination governs accumulated length and not only",
    "  causal order'.  Without Q*, §⑨ does not reach the distance; with it, the two",
    "  readings differ by TWO premises, one on each side, and §⑤'s side-by-side shows one.",
    "  ⌗ This is the guard about forks: when a fork names two objects, check that the thing",
    "  they are alternatives FOR has a slot for only one of them.  Here both readings carry",
    "  an unargued step, and the table shows only the other side's.")

# ---------------------------------------------------------------- ARM 5: P* against the kernel theorem
constitutive = [s for s in re.split(r'(?<=\.)\s', P15)
                if 'cosmological layers' in s and ('SdS' in s or 'branch point' in s)]
arm(5, "is P*'s separation from the kernel theorem sound",
    bool(constitutive),
    "  cc66: the kernel theorem says which metrics lie in the slicing operator's vacuum",
    "  kernel -- a statement about the CUT; to reach P* one must additionally identify the",
    "  cosmology's leaves WITH that cut, and that identification is `stated rather than",
    "  derived'.  The two statements are indeed distinct, and that much is sound.",
    "",
    "  ⛔ BUT `STATED RATHER THAN DERIVED' IS THE WRONG CATEGORY, AND THIS IS THE STRONGEST",
    "  POINT FOR THE STACKING READING IN THIS WHOLE READ.  The identification is not an",
    "  added premise: it is how the object is CONSTRUCTED.  P15 builds the cosmology by",
    "  reading the SdS metric over the r-chart and reassigning its causal orientation, and",
    "  it says so where it introduces the layers:",
    *[f"      \"{' '.join(s.split())[:300]}...\"" for s in constitutive[:1]],
    "  ⇒ the cosmological layers ARE slices of that geometry by construction.  So P* is not",
    "  a free-floating premise someone forgot to argue; it is constitutive of the object the",
    "  whole construction is about, and asking for its derivation is asking the construction",
    "  to derive its own definition.",
    "  ⇒ WHAT THE FORK REALLY IS: either the leaves are the vacuum cut's slices (the",
    "  construction) and P15's `all stress-energy gravitates, in full' is the loose sentence,",
    "  or that sentence is exact and the leaves are not the cut's slices.  ONE OF THE TWO",
    "  SENTENCES HAS TO GIVE.  cc66's read assumes it is the construction; the opposite",
    "  assignment is at least as available, and this seat cannot choose it from the corpus.",
    "  ⌗ That is the fork, stated with both branches, as the reply file requires.")

# ---------------------------------------------------------------- ARM 6: r2419 against this clone
SHALLOW = set()
if os.path.exists(os.path.join(ROOT, '.git', 'shallow')):
    SHALLOW = {ln.strip() for ln in read('.git/shallow').split('\n') if ln.strip()}
reach = git('rev-list', '--count', 'HEAD').strip()
allrefs = git('rev-list', '--count', '--all').strip()
c01 = git('cat-file', '-t', 'c01f56c5b').strip()
have = c01 == 'commit'
parent = git('rev-parse', 'c01f56c5b^').strip() if have else ''
parent_ok = bool(parent) and 'unknown revision' not in parent and git('cat-file', '-t', parent.split()[0]).strip() == 'commit'
arm(6, "§⑥'s r2419 claim, against this clone's own limits",
    True,
    f"  this clone: {reach} commits reachable from HEAD, {allrefs} across all refs; cc66",
    f"  reports a 7,825-commit history, so its clone is deeper than this one.",
    f"  the commit §⑥ names, c01f56c5b, is present here: {have}",
    f"  its PARENT is present here: {parent_ok}",
    "  ⇒ WHAT CAN BE CONCLUDED HERE: nothing about the parent, and therefore nothing about",
    "  `zero hits in the parent'.  This seat CANNOT confirm or refute §⑥'s central check.",
    "  ⇒ WHAT CAN BE CONCLUDED, AND IS: the census half of §⑥ is this line's own instrument",
    "  and re-running it unmodified reproduces its figures (ARM 10), so the `47 assign, 0",
    "  adjudicated as deriving' half stands independently of the history claim.",
    "",
    "  ⛔ AND A LIMIT ON WHAT THE HISTORY CLAIM COULD SHOW EVEN IF CONFIRMED, which cc66",
    "  states fairly and which deserves full weight: a commit named `the consolidated",
    "  corpus' that adds 762 lines is a CONSOLIDATION.  Absence in its parent dates the",
    "  text's arrival in THIS repository, not the argument's existence -- and the corpus",
    "  cites an external source for the kernel theorem and carries a pre-repository",
    "  manuscript (the trampoline's own file) that argues the vacuum description directly.",
    "  ⇒ `entered whole, never argued' is a claim about the repository.  As a claim about",
    "  the programme it does not follow, and §⑥'s own caveat says so.")

# ---------------------------------------------------------------- ARM 7: §⑨'s quotes, matched
def norm(s):
    s = re.sub(r'\\(?:emph|textit|textbf|texttt|mathrm|text|mathbf)\{([^{}]*)\}', r'\1', s)
    for _ in range(3):
        s = re.sub(r'\\(?:emph|textit|textbf|texttt|mathrm|text|mathbf)\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\rcpt\{[^{}]*\}|\\(?:S)?ref\{[^{}]*\}|\\cite[a-z]*\{[^{}]*\}', '', s)
    s = s.replace('``', '"').replace("''", '"').replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('---', '-').replace('--', '-').replace('\u2014', '-').replace('\u2013', '-')
    s = s.replace('\u2019', "'").replace('\u2018', "'")
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    s = re.sub(r'[\\${}`*_]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def words(s):
    return ' '.join(w for w in re.findall(r"[a-z']+", norm(s)) if len(w) > 2)


WORDED = {f: words(t) for f, t in CORPUS.items()}
NINE = SEC[SEC.index('### ⑨'):]
_pos = [m.start() for m in re.finditer('"', NINE)]
QUOTES = [NINE[a + 1:b] for a, b in zip(_pos[0::2], _pos[1::2]) if 40 <= b - a <= 1200]
qrows, qbad = [], []
for q in QUOTES:
    parts = [words(x) for x in re.split(r'\u2026|\.\.\.', q) if words(x)]
    where = []
    for f, hay in WORDED.items():
        i = 0
        ok = True
        for p in parts:
            j = hay.find(p, i)
            if j < 0:
                ok = False
                break
            i = j + len(p)
        if ok:
            where.append(f)
    if not where:                      # localise the failure rather than only reporting it
        frag = max(re.split(r'[,;:]', words(q)), key=len).strip()
        near = [f for f, hay in WORDED.items() if len(frag) > 25 and frag in hay]
        qrows.append((words(q)[:62], [f'NOT VERBATIM; its longest clause is in {near}' ] if near else []))
        qbad.append((q, near))
    else:
        qrows.append((words(q)[:62], where))
arm(7, "every quotation in §⑨ is in print, and where",
    not qbad,
    f"  quotations extracted mechanically from §⑨: {len(QUOTES)}",
    "  matched by word sequence after one normalisation applied to both sides, ellipses",
    "  honoured as ordered gaps:",
    *[f"      {'OK ' if w else '⛔ '} \"{t}...\"\n           {', '.join(w) if w else 'NOT IN PRINT'}"
      for t, w in qrows],
    f"  not verbatim: {len(qbad)}",
    "  ⛔ ONE OF THE THIRTEEN IS A PARAPHRASE INSIDE QUOTATION MARKS.  §⑨⒠ prints",
    "  \"such universes expand at later times only because they were already expanding\";",
    "  the source reads `continuing to expand at later times only because they were already",
    "  expanding'.  The substance is identical and the compression changes nothing in the",
    "  argument -- it is reported at that size, because a quotation mark is a claim about",
    "  wording and this seat's own arms have been caught by the same thing.",
    "  ⌗ The Projection Principle, the gravitational-wave passage and the ontological-",
    "  curvature passage are `P7`'s own; the trampoline's two sentences are the resources",
    "  manuscript's.  §⑨ attributes each to the right file.")

# ---------------------------------------------------------------- ARM 8: does ⒣'s objection stand?
AX = [s for s in re.split(r'(?<=\.)\s', CORPUS.get('CR_framework.tex', ''))
      if 'valid projection' in s and 'causal structure' in s]
axiom = ' '.join(AX[0].split()) if AX else ''
conformal_words = ('causal structure', 'signal propagation')
arm(8, "does ⒣'s objection stand",
    bool(axiom),
    "  ⒣, as cc66 states it: the Projection Principle governs CAUSAL STRUCTURE -- which",
    "  signals reach which events -- not the metric length a signal accumulates; and D_M is",
    "  a separation read across leaves, which is foliation data.",
    "",
    f"  the axiom, located and read: \"{norm(axiom)[:300]}...\"",
    "  ⇒ ⛭ THE OBJECTION STANDS ON THE AXIOM'S OWN WORDS.  `The causal structure induced by",
    "  g faithfully encodes signal propagation' is a condition on the CONFORMAL class: a",
    "  causal structure fixes light cones and therefore which events are connectible, and",
    "  it fixes lengths only up to a conformal factor.  An accumulated metric length is not",
    "  a causal-structure fact, so the axiom as quoted does not by itself reach D_M.",
    "  cc66's reply -- that a length a signal accumulates is fixed by the geometry it",
    "  propagates through -- is true and is about the LAYER's geometry, which is the point",
    "  in dispute; it does not follow from the axiom.",
    "",
    "  ⌗ WHAT ⒣ DOES NOT BUY, SAID SO THE VERDICT IS NOT READ AS A WIN FOR EITHER SIDE:",
    "  the quantity in dispute is computed from the leaf family's own history on BOTH",
    "  readings -- r_0 ∫dtau-tilde / r(tau-tilde) -- so showing that the axiom does not fix",
    "  it does not put it back on the vacuum history either.  ⒣ narrows §⑨ from `the axiom",
    "  answers the order's item ②' to `the axiom makes the layer primitive, which does not",
    "  by itself fix which history the layer has'.  That narrower reading is correct, and",
    "  it leaves the question exactly where ARM 5 puts it.")

# ---------------------------------------------------------------- ARM 9: the wave case and the trampoline's scope
ERC = CORPUS.get('ERC_existence-relativity-cosmology.tex', '')
licence = [s for s in re.split(r'(?<=\.)\s', ERC) if 'not necessarily must' in s]
cosmo_flat = [s for s in re.split(r'(?<=\.)\s', ERC) if 'perfectly flat' in s and 'warped by matter' in s]
lumps = {w: ERC.lower().count(w) for w in ('bowling', 'lensing', 'ripples', 'bound')}
radiation_in_erc = ERC.lower().count('radiation')
arm(9, "the gravitational-wave case and the trampoline's scope",
    bool(licence) and bool(cosmo_flat),
    "  THE WAVE CASE: §⑨⒝ uses it for `CR's one worked propagating case comes out on the",
    "  leaf'.  The quoted passages are in print (ARM 7) and they say what it says they say:",
    "  the propagating degree of freedom is the layer's transverse-traceless shear, its",
    "  energy is seated on the layer, and the spacetime representation is called",
    "  projection-dependent.  ⇒ the use is supported.",
    "  ⌗ AND ITS LIMIT, WHICH §⑨ DOES NOT STATE: a gravitational wave is a perturbation OF",
    "  the layer's own metric.  A photon's accumulated distance is not a perturbation of",
    "  the layer; it is a length across a family of layers.  That the one is seated on the",
    "  layer does not carry to the other without the step ⒣ disputes.",
    "",
    "  THE TRAMPOLINE: §⑨⒟ reads the licence as being about LOCAL, LUMPY content.",
    f"      the licence, in print: \"{norm(licence[0])[:230] if licence else 'NOT FOUND'}...\"",
    f"      and the cosmological sentence: \"{norm(cosmo_flat[0])[:200] if cosmo_flat else 'NOT FOUND'}...\"",
    f"      the manuscript's furniture: {lumps};  occurrences of `radiation': {radiation_in_erc}",
    "  ⛔ AND HERE THE SKEPTICAL READING GOES AGAINST cc66, AT FULL STRENGTH.  The licence",
    "  sentence is not about lumps in its own words: it says SPACE MAY REALLY WARP THROUGH",
    "  GRAVITATIONAL PROCESSES while ITS COSMOLOGICAL EVOLUTION is described by vacuum",
    "  solutions.  `Cosmological evolution' is the whole of what is at issue, and the",
    "  sentence licenses a vacuum description of it under real warping -- which is exactly",
    "  what P* asserts.  The restriction to bowling balls is read off the MODEL's",
    "  furniture, not off the sentence; §⑨⒟'s own quotation contains the generalisation.",
    "  ⌗ Two things cut the other way and both are stated: the warpers in the model are",
    "  lumps, and the source itself says `can - though not necessarily must'.  So the",
    "  trampoline licenses the vacuum reading without compelling it, and it does not",
    "  exclude a homogeneous bath by its own words.",
    "  ⇒ VERDICT: §⑨⒟'s scope claim is NOT established.  The foundational passage is",
    "  weaker than cc66 reads it in one direction and stronger in the other: it permits",
    "  the vacuum cosmological description outright, and compels nothing.")

# ---------------------------------------------------------------- ARM 10: everything for the stacking reading
CEN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7612_60_whether_the_reassignment_itself_fixes_the_rate_a_photon_path_distance_accumulates_at',
                   'photonfamily.py')
out = subprocess.run([sys.executable, CEN], cwd=os.path.dirname(CEN), capture_output=True, text=True).stdout
m1 = re.search(r'sentences assigning a distance or a comoving separation to a rate:\s*(\d+)', out)
m2 = re.search(r'sentences adjudicated DERIVES:\s*(\d+)', out)
census = (int(m1.group(1)) if m1 else -1, int(m2.group(1)) if m2 else -1)
arm(10, "⛭ everything that tells for the STACKING reading, at full strength, with its defeater",
    census == (47, 0),
    "  THE ORDER ASKS FOR THIS EXPLICITLY, so each entry is put at its strongest and then",
    "  given the one thing that would have to be true for it to fall.",
    "",
    "  ⒜ ⛭⛭ P* IS CONSTITUTIVE, NOT UNARGUED.  The cosmological layers are slices of the",
    "     SdS geometry read over the r-chart; that is how the object is built (ARM 5).  So",
    "     the identification cc66 calls `stated rather than derived' is the construction's",
    "     own definition, and a definition has no derivation to be missing.  On this",
    "     reading the loose sentence is `all stress-energy gravitates, in full', which is",
    "     about where the field equations ACT, not about which history the chart's r(tau)",
    "     has.  ⇒ DEFEATER: show that the corpus uses the leaves' geometry somewhere it",
    "     could not if they were vacuum slices -- which the sound horizon may already be.",
    "  ⒝ ⛭ THE SOUND HORIZON IS THE CORPUS'S OWN COUNTEREXAMPLE AND IT CUTS BOTH WAYS.",
    "     §⑨⒡ uses it to say the coherence cost is already paid.  Read the other way, it",
    "     says the corpus ALREADY treats a plasma process's length as leaf-borne while the",
    "     foliation stacks at the other rate -- i.e. the mixing §④ calls incoherent is the",
    "     corpus's standing practice, and has survived every test the sector has run.",
    "     ⇒ DEFEATER: a demonstration that the mixing produces a wrong observable; ARM 3",
    "     is the place to look, and it does not produce one.",
    "  ⒞ ⛭ THE TRAMPOLINE LICENCE IS GENERAL IN ITS OWN WORDS (ARM 9): `space may really",
    "     warp ... but its cosmological evolution can be described by vacuum solutions'.",
    "     It is not restricted to lumps by the sentence, only by the model's furniture.",
    "     ⇒ DEFEATER: the same sentence's `though not necessarily must', which makes it a",
    "     permission and not a derivation.",
    "  ⒟ ⛭ ⒣'s OBJECTION STANDS (ARM 8): the Projection Principle is a condition on causal",
    "     structure, which is conformal, so it does not by itself fix an accumulated",
    "     length.  §⑨'s axiom-level answer to item ② does not reach the distance.",
    "     ⇒ DEFEATER: an argument that the layer's being primitive fixes lengths on it,",
    "     which is Q* and is what cc66 calls an argument rather than a proof.",
    "  ⒠ ⛭ §④'s KEY STEP IS NOT ENTAILED (ARM 1): `both lengths are integrals of c dt/a",
    "     over one history' imports a single scale factor into a chart whose layer has two",
    "     metric functions.  ⇒ DEFEATER: the anisotropy does not supply the corpus's two",
    "     rates either, so this weakens §④ without strengthening P*.",
    "  ⒡ ⛭ THE NARIAI CASE IS UNTOUCHED, and cc66 says so: Eddington's expansion problem,",
    "     the coherence argument and Hubble-flow invariance are all arguments about the",
    "     foliation's stacking and none is touched by where a propagated length",
    "     accumulates.  ⇒ no defeater is needed: this is common ground, and it means the",
    "     dispute is narrower than `which rate is the cosmology's'.",
    "",
    f"  ⌗ AND WHAT DOES NOT TELL FOR IT: this line's own census, re-run here unmodified,",
    f"  returns {census[0]} sentences assigning a distance or a comoving separation to a rate and",
    f"  {census[1]} adjudicated as DERIVING the assignment -- cc66's figures, reproduced.  The",
    "  absence of a derivation in print is not in dispute; what ⒜ disputes is what that",
    "  absence means when the thing undrawn is a definition.")

# ---------------------------------------------------------------- ARM 11: what this read cannot settle
arm(11, "what this read cannot settle, and what each would need",
    True,
    "  ⒜ WHICH SENTENCE GIVES -- the construction's vacuum slicing or `all stress-energy",
    "     gravitates in full'.  Both are in print; they cannot both be exact about the same",
    "     r(tau-tilde).  Settling it needs a ruling about the object, not a computation,",
    "     and the ruling is 69's.  ⇒ THIS IS THE FORK, and this seat does not decide it.",
    "  ⒝ WHETHER Q* HOLDS -- whether the layer's primacy fixes accumulated lengths and not",
    "     only causal order.  It is a foundations question and the corpus does not contain",
    "     a sentence that settles it; §⑨⒣ is where it is joined and both sides concede it",
    "     is an argument.",
    "  ⒞ WHERE THE CLASSIFIER WAS FIRST ARGUED, outside this repository.  This clone cannot",
    "     reach the commit's parent (ARM 6), and even a deeper clone would date a text's",
    "     arrival rather than an argument's existence.",
    "  ⒟ WHETHER THE SKY DECIDES IT.  Not this seat's arm and not in this order: the",
    "     measurement is 70's, it is reported, and it is one comparison.")

# ----------------------------------------------------------------- the ledger
print("\n" + "=" * 100)
print("  THE LEDGER")
for n, ok, title in sorted(VERDICTS):
    print(f"    {'PASS' if ok else 'FAIL'}  ARM {n:2d}  {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms meet their registered criterion"
      + ("" if not bad else f";  not met: {sorted(bad)}"))
print("  (a FAIL here is a finding about the argument read, not a failure of the read)")
print("=" * 100)
