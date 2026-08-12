#!/usr/bin/env python3
"""
RECEIPT -- P16: ** ITEM 55 WORKED.  N_eff WAS LOAD-BEARING AT BOTH ENDS AND NAMED NOWHERE.  AND THE
CORPUS'S OWN WALL SETTLES THE QUESTION IT INVITES: CR FIXES THE nu_R's PLACE IN A GRADING AND NOT ITS
COUPLINGS, SO IT MAKES NO N_eff PREDICTION -- AND THE STANDARD VALUE IS CONSISTENT WITH THE FOURTH
GRADING RATHER THAN IN TENSION WITH IT. **

Built r2545+c54.205, lead `L-527`.  VEIN: `L-221` (PO-5, what may exist and why these).

===================================================================================================
** cc54 RAISED IT AS AN OPEN FORK AND ROUTED IT RATHER THAN ATTEMPTING IT.  THAT WAS RIGHT. **
===================================================================================================

The fork as posed -- *"does CR adopt the standard value, or does its nu_R structure predict a
departure?"* -- is a research programme, and the literature does not settle it.  ** The corpus's own
wall does, and the result is a paragraph. **

  * ** su(3) is not a subalgebra of the substrate's isometry algebra ** -- stated repeatedly -- and
    the geometric core ** declines a geometric origin for the gauge content ** outright.
    ⇒ *** So CR assigns a right-handed neutrino a PLACE IN A GRADING and NO INTERACTIONS, and says
        so. ***
  * ** And N_eff counts species that THERMALIZE ** -- a statement about interaction rates.  *This
    paper's own network computes the neutrino term from a DECOUPLING TEMPERATURE, which is exactly
    such a rate.*
  ⇒ ** The Standard Model already admits a gauge-singlet right-handed neutrino and keeps 3.046, for
    precisely that reason.  ** *** The existence of the state has never by itself moved the count. ***

===================================================================================================
** WHAT WAS MEASURED, AND WHAT IS NOW WRITTEN **
===================================================================================================

  PART 1  ** THE ABSENCE, re-measured here rather than taken from the routing slip: ** N_eff, Neff,
          3.046 and "effective number of" across the seventeen papers.  *A missing NAME, not a
          missing sector -- the lithium problem is named and worked, and D/H and Y_p are everywhere.*
  PART 2  ** AND THE COMMITMENT, in this paper's own network: ** `r_nu = (4.0/11.0)**(1.0/3.0)` and
          three species, read out of `bbn_network.py` itself.  ** The value was being used and not
          named. **
  PART 3  ** THE WALL, checked in the corpus's own text ** -- the su(3) exclusion and p0's declining
          of a geometric origin for the gauge content.  *Without both, the paragraph would be a new
          claim rather than an application of a standing one.*
  PART 4  ** AND THE WRITTEN PARAGRAPH ** -- the name, the value with its provenance, Planck's
          2.99 +- 0.17 for comparison, and the stance.

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that CR predicts N_eff = 3.046 ** -- it predicts nothing about it; the value is ADOPTED, and
the claim is consistency rather than derivation.  ** Not that a fourth grading is a fourth
thermalized species ** -- that is the inference the paragraph exists to block.  ** Not that the nu_R
is a Standard Model singlet as a CR result **: what CR supplies is the absence of an assigned gauge
status, which is weaker than singlethood and is all the wall gives.

⚠ ** AND THE TRIP-WIRE IS AN EXISTING ONE, WHICH IS THE POINT. **  `F1` fires if the gauge group is
ever promoted from described to forced.  ** If it were, the nu_R would acquire couplings and this
consistency argument would have to be re-run ** -- so the stance sits under a falsifier the framework
already carries rather than under a new one.

SETTINGS: none -- no instrument, no spectra.  Source counts over the corpus's .tex, a read of this
paper's own BBN network source, and source checks.

rc=0 on success.  Run: python3 P16_CR_makes_no_Neff_prediction_because_it_fixes_a_place_and_not_a_coupling.py
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
P16 = TEX['cosmogenesis_paper.tex']
OTHERS = '\n'.join(v for k, v in TEX.items() if k != 'cosmogenesis_paper.tex')

# =====================================================================
print("=" * 78)
print("PART 1 — THE ABSENCE, RE-MEASURED HERE RATHER THAN TAKEN FROM THE ROUTING SLIP")
print("=" * 78)
TERMS = [('N_eff (any spelling)', r'N_\{?\\?mathrm\{eff\}\}?|N_\{\\rm eff\}|\bN_eff\b|\bNeff\b'),
         ('3.046', r'3\.046'),
         ('"effective number of"', r'effective number of')]
print(f"  {'term':>24s} {'in P16 now':>11s} {'elsewhere':>10s}")
_before_elsewhere = {}
for what, pat in TERMS:
    a = len(re.findall(pat, P16))
    b = len(re.findall(pat, OTHERS))
    _before_elsewhere[what] = b
    print(f"  {what:>24s} {a:>11d} {b:>10d}")
print()
print("  *The routed measurement was zero everywhere before this revision; P16's counts above are")
print("   this revision's own paragraph, and the 'elsewhere' column shows the other sixteen papers")
print("   are untouched by it.*")
_neff_in_p16 = len(re.findall(TERMS[0][1], P16))
if _neff_in_p16 == 0:
    fail.append("N_eff is still unnamed in P16 — the revision's whole point is that it is named")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE COMMITMENT, READ OUT OF THIS PAPER'S OWN NETWORK SOURCE")
print("=" * 78)
_bbn = None
for cand in (os.path.join(ROOT, 'computations', 'p16_bbn', 'bbn_network.py'),
             os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper', 'bbn_network.py')):
    if os.path.exists(cand):
        _bbn = cand
        break
assert _bbn, 'bbn_network.py not found'
src = open(_bbn, encoding='utf-8', errors='replace').read()
COMMIT = [("the post-annihilation temperature ratio is hard-coded", r'r_nu\s*=\s*\(4\.0/11\.0\)\*\*\(1\.0/3\.0\)'),
          ("and three species enter the entropy count", r'3\.0\s*\*\s*\(7\.0/8\.0\)')]
for what, pat in COMMIT:
    ok = re.search(pat, src) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the network no longer shows: {what}")
print(f"\n  source: {os.path.relpath(_bbn, ROOT)}")
print("  ** So the value was being USED and not named — which is the finding, and it is a missing")
print("     NAME rather than a missing sector. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE WALL, IN THE CORPUS'S OWN TEXT, WITHOUT WHICH THIS WOULD BE A NEW CLAIM")
print("=" * 78)
WALL = [("the corpus states su(3) is not a subalgebra of the substrate's isometry algebra",
         OTHERS + P16, r'\\su\(3\)\\not\\subset|\\mathfrak\{su\}\(3\)\\not\\subset|not a subalgebra of'),
        ("and p0 declines a geometric origin for the gauge content",
         OTHERS, r'geometric origin for the gauge')]
for what, hay, pat in WALL:
    ok = re.search(pat, hay, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the standing wall is not in the corpus: {what}")
print()
print("  ⇒ *CR assigns the nu_R a PLACE and NO COUPLINGS.  N_eff counts what THERMALIZES.  The two")
print("     do not meet, which is why the paragraph is a consistency statement and not a prediction.*")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND WHAT THE PARAGRAPH NOW SAYS")
print("=" * 78)
WRITTEN = [("names N_eff and gives the adopted value with its provenance", r'N_\{\\mathrm\{eff\}\}=3\.046'),
           ("states that what is fixed is a place and not a coupling", r'place in a grading, and not a coupling'),
           ("states plainly that no prediction is made", r'makes no \$N_\{\\mathrm\{eff\}\}\$\s*\n?prediction'),
           ("gives Planck's value for comparison", r'2\.99\\pm0\.17'),
           ("and puts the stance under F1 rather than a new trip-wire",
            r'\\textup\{\(F1\)\} fires if the gauge group is ever promoted')]
for what, pat in WRITTEN:
    ok = re.search(pat, P16, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the written paragraph does not carry: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — N_eff is named where the network commits to it; the network's commitment is")
print("read out of its own source; the wall that settles the question is the corpus's own standing")
print("one; and the paragraph states a consistency rather than a prediction, under F1.")
print("=" * 78)

# ============================================================================================
# GATE — r2545+c54.205, `L-527`.  A consistency paragraph is the easiest kind of writing to
# over-read as a result, so the pins are on it being an APPLICATION of a standing wall and on the
# stance staying a non-prediction:
#   (1) N_eff asserted PRESENT in P16 -- the revision exists to name it, and if the name is gone
#       the revision did nothing;
#   (2) the network's own two commitments read out of source -- ** if the code did not commit to
#       three thermalized species at (4/11)^(1/3), the "load-bearing and unnamed" finding would be
#       about nothing **;
#   (3) the standing wall asserted present in the corpus -- ** without it, "CR fixes a place and
#       not a coupling" would be a NEW claim this paper is not entitled to make, and the paragraph
#       would be doing physics instead of applying a result **;
#   (4) and five elements of the written paragraph, including that no prediction is made and that
#       the dependency sits under F1 rather than a new trip-wire.
#   NOT gated: any value of N_eff as a CR output.  ** There is none; the value is adopted. **
# ============================================================================================
assert _neff_in_p16 > 0, "N_eff is still unnamed in P16"
for what, pat in COMMIT:
    assert re.search(pat, src), f"the network no longer shows: {what}"
for what, hay, pat in WALL:
    assert re.search(pat, hay, re.I | re.S), f"the standing wall is missing: {what}"
for what, pat in WRITTEN:
    assert re.search(pat, P16, re.I | re.S), f"the paragraph lacks: {what}"
print(f"GATE c54.205 (r2545), `L-527`: N_eff now appears {_neff_in_p16} time(s) in P16 where the "
      f"network commits to three thermalized species at (4/11)^(1/3) and named none; the wall that "
      f"settles it is the corpus's standing su(3) exclusion plus p0's declining of a geometric gauge "
      f"origin; and the paragraph states a consistency under F1, not a prediction — pinned against "
      f"`FOR_54` item 55 (r2545) and cc54's station 9.")
