#!/usr/bin/env python3
"""
RECEIPT -- P7: THE RESOLUTION RESEMBLES THE BABY-UNIVERSE ONE, ITS STANDARD OBJECTION HAS NO PREMISE
HERE, AND ON THE NEAR-PLANCKIAN FLUX P1 ESTABLISHES THE PAGE CURVE IS A CONSEQUENCE OF UNITARITY
RATHER THAN A TEST OF THIS READING.

PART 1 -- the objection to a baby-universe resolution is that information carried into a CAUSALLY
DISCONNECTED daughter is still lost to the exterior.  It presupposes two spacetimes joined at a neck.
P7 states the realised spacetime stays globally connected and globally hyperbolic with a global
Cauchy surface throughout, so there is no disconnected region and no sector to trace over.  The prior
literature that puts a daughter behind the parent's horizon (Frolov-Markov-Mukhanov, Smolin,
Poplawski, Pathria) is named, so the shape the objection answers is on the page.

PART 2 -- the flux.  P1 computes the Bogoliubov coefficients at finite retarded time on the realised
exterior: a flux close to Planckian at kappa/2pi arrives with no horizon formed anywhere
(Barcelo-Liberati-Sonego-Visser 2011).  What the realised exterior never contains is the exactly
thermal u -> infinity limit and evaporation carried to completion, both of which belong to the
completed horizon.  P7's Hawking subsection states the same.

PART 3 -- the diagnostic.  Radiation from a body still outside its horizon, into a globally hyperbolic
spacetime with nothing traced over, is entangled with that body as any radiating object is; a Page
curve is then what unitarity requires should the body radiate long enough, and a measured one agrees
with the reading rather than discriminating it.  What the readings dispute is the endpoint.

COMPUTES: no numbers -- source checks over corpus/*.tex (P1 and P7), and counts of the two names the
paragraph exists to carry.

WHAT IS NOT CLAIMED.  Not that the near-Planckian flux carries the body to complete evaporation on any
stated timescale; not a computation of the entanglement entropy; no new physics.  Every element is
already in P1 or P7 and this file checks that it is.

rc=0 on success.  Run: python3 P07_the_daughter_is_not_disconnected_and_the_page_curve_is_what_unitarity_requires.py
                        (stdlib only; ~2 s)
"""
import os
import re
import sys

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

TEX = {fn: open(os.path.join(CORPUS, fn), encoding='utf-8', errors='replace').read()
       for fn in sorted(os.listdir(CORPUS))
       if fn.endswith('.tex') and not fn.startswith('appendix_receipts')}
ALL = '\n'.join(TEX.values())
P7 = TEX['CR_framework.tex']
P1 = TEX['BH_causality_v2.tex']


def uses(pat, hay=None):
    return len(re.findall(pat, ALL if hay is None else hay, re.I))


def check(title, rows, hay):
    print("=" * 78)
    print(title)
    print("=" * 78)
    for what, pat in rows:
        ok = re.search(pat, hay, re.I | re.S) is not None
        print(f"  {'OK ' if ok else 'MISSING'}  {what}")
        if not ok:
            fail.append(f"{title.split(' --')[0]}: {what}")
    print()


check("PART 1 -- ONE SPACETIME, NOT TWO JOINED AT A NECK", [
    ("P7 states the spacetime stays globally connected and globally hyperbolic",
     r'stays globally connected and globally hyperbolic'),
    ("with a global Cauchy surface throughout", r'global Cauchy surface throughout'),
    ("and no hidden interior sector to trace the exterior state over",
     r'no hidden interior sector over which the exterior state must be traced'),
    ("the objection stated as an objection -- a causally disconnected daughter",
     r'causally disconnected\} daughter'),
    ("the difference that answers it", r'presupposes two spacetimes joined at a\s*\n?neck'),
    ("the prior daughter-universe literature named (Frolov-Markov-Mukhanov)",
     r'\\cite\{FrolovMarkovMukhanov1989\}'),
    ("and Smolin", r'\\cite\{Smolin1992\}'),
], P7)

check("PART 2a -- P1 CARRIES THE FINITE-u FLUX", [
    ("P1 computes the Bogoliubov coefficients at finite u on the realised exterior",
     r'Bogoliubov coefficients at finite \$u\$ are therefore computed on the realised exterior'),
    ("P1 cites Barcelo et al. for a flux with no horizon formed", r'no horizon need form anywhere for such a flux to arrive~\\cite\{Barcelo2011\}'),
    ("P1 places the exactly thermal state at the u -> infinity limit", r'exactly thermal state is its \$u\\to\\infty\$ end'),
], P1)

check("PART 2b -- P7 STATES THE SAME", [
    ("P7: a flux close to Planckian at kappa/2pi", r'flux close to Planckian at the temperature \$\\kappa/2\\pi\$'),
    ("P7 cites Barcelo et al.", r'\\cite\{Barcelo2011,JanzenBHcausality\}'),
    ("P7: the exactly thermal state and evaporation to completion belong to the completed horizon",
     r'exactly thermal state, with the permanent inequivalence'),
], P7)

check("PART 3 -- THE PAGE CURVE IS A CONSEQUENCE, AND THE DISPUTE IS THE ENDPOINT", [
    ("the Page curve named, with the 1993 reference", r'\\emph\{Page\s*\n?curve\}~\\cite\{Page1993\}'),
    ("the baby-universe scenario named", r'\\emph\{baby\s*\n?universe\}'),
    ("the curve stated as a consequence and not a test", r'the curve is a consequence and not a test'),
    ("a measured curve agrees rather than discriminates", r'would therefore agree with this reading'),
    ("the dispute located at the endpoint", r'dispute is the endpoint and not the curve'),
], P7)

_counts = {'Page curve': uses(r'Page\s*\n?curve'), 'baby universe': uses(r'baby\s*\n?universe')}
for k, v in _counts.items():
    print(f"     {k:>20s} : {v} use(s) corpus-wide")
assert _counts['Page curve'] > 0, "the Page curve is not named in the corpus"
assert _counts['baby universe'] > 0, "the baby-universe scenario is not named in the corpus"

print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS -- the daughter is the same globally hyperbolic spacetime, not one behind a neck;")
print("the near-Planckian flux at finite u is P1's and P7's alike; and on it the Page curve is what")
print("unitarity requires, the readings parting at the exactly thermal endpoint and not at the curve.")
print("=" * 78)
