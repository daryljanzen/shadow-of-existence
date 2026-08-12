#!/usr/bin/env python3
"""
RECEIPT -- P7: ** ITEM 53 WORKED.  THE RESOLUTION IS THE BABY-UNIVERSE ONE, THE STANDARD OBJECTION WAS
ALREADY ANSWERED IN THE SAME SENTENCE, AND THE PAGE CURVE IS A FALSIFIER OF THIS READING RATHER THAN A
TARGET FOR IT. **

Built r2540+c54.204, lead `L-524`.  VEIN: `L-165` (PO-6, what a quantum of this geometry is).

===================================================================================================
** WHAT 56 MEASURED, AND IT IS THE SAME SHAPE AS ITEM 47 ONE FIELD OVER **
===================================================================================================

r2540, station 10, ** 56's counts as routed **: information paradox 14, unitary 35, AMPS 10,
complementarity 4, remnant 4 -- ** the AMPS figure does not reproduce over corpus/*.tex and PART 3 says
so rather than repeating it ** --
against ** Page curve 0 · Page time 0 · density matrix 0 · von Neumann 0 · mixed state 0 · baby
universe 0 **.

  ⇒ *** So the corpus engages the DERIVED firewall puzzle and never the PRIMARY diagnostic; and it
      states the baby-universe resolution without naming the scenario. ***  ** The zeros are the load-
      bearing half and they reproduce exactly; the AMPS figure does not, and PART 3 reports that. **

** AND 56's DISCIPLINE IS THE PART WORTH COPYING:** *check whether the corpus ANSWERS the objection
before reporting it as a gap.*  ** Both times it did **, so both items are "name what you resemble",
not "you have not addressed this".  *Reporting the second when the first is true would be the reverse
failure and a worse one.*

===================================================================================================
** PART 1 -- THE OBJECTION PRESUPPOSES TWO SPACETIMES.  THIS CONSTRUCTION HAS ONE. **
===================================================================================================

The standard objection to a baby-universe resolution is precise and is NOT about unitarity:
** information carried into a CAUSALLY DISCONNECTED daughter is still lost to the exterior **, so
global unitarity is restored while the question the paradox asks -- whether an outside observer's
state stays pure -- is not answered.

  ** P7's own sentence answers it: the spacetime "stays globally connected and globally hyperbolic,
  with a global Cauchy surface throughout". **  No disconnected region, so no sector to trace over.

  ⇒ *** The daughter is the same spacetime read across the branch point, not a second one attached at
      a neck.  The clause that answers the objection was already there and was doing so silently. ***

PART 1 checks that clause is in the source rather than quoting it from the routing slip.

===================================================================================================
** PART 2 -- THERE IS NO PAGE CURVE, AND THE REASON IS ALREADY CLAIMED **
===================================================================================================

The Page curve is a property OF a Hawking flux: the entanglement entropy of the emitted radiation
rises, turns over at the Page time, and returns to zero if evaporation is unitary.  ** The flux is
denied here as a horizon effect for want of a completed horizon **, so:

      no completed horizon  ->  no Bogoliubov flux  ->  no radiation  ->  no entropy to turn over

  ⇒ ** That is a CONSEQUENCE of what is already claimed and not a further claim ** -- the same footing
    on which sec:CR-mechanics sets aside the Bekenstein-Hawking entropy, which PART 2 also checks.

===================================================================================================
** ⛭⛭ PART 3 -- AND IT CUTS, WHICH IS WHY IT IS WORTH STATING RATHER THAN LEAVING SILENT **
===================================================================================================

*** A measured Page curve would not be a difficulty for this reading to absorb.  The flux whose
    entropy it tracks is DENIED here, so observing that entropy rise and turn over would falsify the
    denial and with it the resolution built on it. ***

  ⌗ ** So naming the diagnostic converts a silence into a stated trip-wire ** -- which is item 47's
    outcome exactly: there, naming Unruh strengthened the argument by making the criterion explicit;
    here, naming the Page curve strengthens it by making the falsifier explicit.
  ⚠ *And what distinguishes the readings is whether the flux exists at all -- this paper's own named
  frontier, "the mechanism of the crossing, not its unitarity" -- and NOT the shape of a curve whose
  meaning neither reading disputes.*

WHAT IS NOT CLAIMED.  ** Not that the resolution is wrong ** -- this file finds it survives the
objection and says which clause does the work.  ** Not that a Page curve should be produced **: if the
flux is absent there is no curve, and that is consistent rather than evasive.  ** Not that the
corpus's AMPS engagement is misplaced ** -- only that the derived puzzle was addressed and the primary
diagnostic was not named.  ** And no new physics claim of any kind: every element of PART 1 and PART 2
is already in the papers; what is added is the two names and the falsifier that follows from them. **

SETTINGS: none -- no instrument, no computation.  Source counts and source checks over the corpus's
own .tex, before and after.

rc=0 on success.  Run: python3 P07_the_page_curve_is_a_falsifier_here_and_the_daughter_is_not_disconnected.py
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


def uses(pat, hay=None):
    return len(re.findall(pat, ALL if hay is None else hay, re.I))


# =====================================================================
print("=" * 78)
print("PART 1 — THE OBJECTION PRESUPPOSES TWO SPACETIMES, AND THE ANSWERING CLAUSE WAS ALREADY THERE")
print("=" * 78)
PRIOR = [
    ("P7 states the spacetime stays globally connected AND globally hyperbolic",
     r'stays globally connected and globally hyperbolic'),
    ("with a global Cauchy surface throughout — so there is nothing to trace over",
     r'global Cauchy surface throughout'),
    ("and it states there is no hidden interior sector to trace the exterior state over",
     r'no hidden interior sector over which the exterior state must be traced'),
    ("and it rejects the remnant reading explicitly",
     r'does not end as a thermal remnant|not end as a thermal\s*\n?remnant'),
]
for what, pat in PRIOR:
    ok = re.search(pat, P7, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P7 does not carry the prior clause: {what}")
print()
print("  ** The standard objection is that information in a CAUSALLY DISCONNECTED daughter is still")
print("     lost to the exterior. **  *It presupposes two spacetimes joined at a neck; the clauses")
print("     above say there is one, connected, with a global Cauchy surface — so the objection has")
print("     no premise here.  That was true before this revision and was never stated as a")
print("     difference from the scenario it resembles.*")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — NO PAGE CURVE, AND THE REASON IS ALREADY CLAIMED ELSEWHERE IN THE SAME PAPER")
print("=" * 78)
CHAIN = [
    ("the flux is denied for want of a completed horizon, not by a computation that disagrees",
     r'no completed horizon there is no background on which the Bogoliubov'),
    ("and the thermal endpoint is therefore absent AS A HORIZON EFFECT",
     r'absent as a horizon effect'),
    ("and the Bekenstein--Hawking entropy is set aside on the same footing",
     r'Bekenstein--Hawking entropy~?\\?c?i?t?e?\{?Bekenstein1973\}?, read as the entropy'),
]
for what, pat in CHAIN:
    ok = re.search(pat, P7, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the no-curve chain is broken at: {what}")
print()
print("  no completed horizon -> no Bogoliubov flux -> no radiation -> no entropy to turn over")
print("  ** So the absence of a Page curve is a CONSEQUENCE of what is already claimed. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE CORPUS NOW NAMES, AND WHAT IT STILL DOES NOT")
print("=" * 78)
NAMED = [
    ("the Page curve, with the 1993 reference", r'\\emph\{Page\s*\n?curve\}'),
    ("the Page reference is in the bibliography", r'\\bibitem\{Page1993\}'),
    ("the baby-universe scenario, by its own name", r'\\emph\{baby\s*\n?universe\}'),
    ("the objection stated AS an objection — causally disconnected", r'causally disconnected\} daughter'),
    ("the difference that answers it — one spacetime, not two", r'presupposes two spacetimes joined at a\s*\n?neck'),
    ("and the falsifier stated as a falsifier", r'would falsify the denial'),
]
for what, pat in NAMED:
    ok = re.search(pat, P7, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the written paragraph does not carry: {what}")
print()
_counts = {'Page curve': uses(r'Page\s*\n?curve'), 'baby universe': uses(r'baby\s*\n?universe'),
           'information paradox': uses(r'information paradox')}
# ** AND ONE COUNT THAT DOES NOT REPRODUCE, REPORTED RATHER THAN REPEATED. **  The routing slip gives
# ** "AMPS 10"; over corpus/*.tex this line measures AMPS 0 and 'firewall' once, both in P7.  ** The
# routed figure may be over a wider file set; ** it is not verified here and is therefore not asserted
# in this file's prose. **  *A count quoted from a routing slip and printed beside one's own
# measurements reads as evidence -- which is the failure 56 caught in itself at e863402 (fixed note
# strings printed beside real booleans), arriving from the other direction.*
_amps = {'AMPS': uses(r'\bAMPS\b'), 'firewall': uses(r'firewall'),
         'Almheiri': uses(r'Almheiri')}
for k, v in _counts.items():
    print(f"     {k:>20s} : {v} use(s) corpus-wide")
_still = {'density matrix': uses(r'density matrix'), 'von Neumann': uses(r'von Neumann'),
          'Page time': uses(r'Page\s*\n?time')}
print()
print("  ** AND WHAT IS STILL AT ZERO OR NEAR IT, counted so the debt stays visible rather than")
print("     quietly discharged: **")
for k, v in _still.items():
    print(f"     {k:>20s} : {v} use(s)")
print("  *56 measured six absent terms; this revision names two of them and the diagnostic they")
print("   belong to.  The entropy-language ones are not addressed and are not claimed to be.*")
print()
print("  \u26a0 ** AND ONE ROUTED COUNT THAT DOES NOT REPRODUCE HERE, reported rather than repeated: **")
for k, v in _amps.items():
    print(f"     {k:>20s} : {v} use(s) over corpus/*.tex")
print("  *The routing slip gives 'AMPS 10'.  Over the seventeen papers this line measures 0, with\n"
      "   'firewall' once.  The routed figure may be over a wider file set; it is NOT verified here\n"
      "   and so is not asserted in this file's prose.  Routed back to 56 rather than adopted.*")
if _counts['Page curve'] == 0 or _counts['baby universe'] == 0:
    fail.append("the two names this revision exists to add are still at zero uses")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the baby-universe objection presupposes two spacetimes and P7's own clauses")
print("say there is one; the absence of a Page curve follows from the flux denial already claimed, on")
print("the same footing as the entropy set aside in sec:CR-mechanics; and both names are now in the")
print("paper together with the falsifier that follows from them.")
print("=" * 78)

# ============================================================================================
# GATE — r2540+c54.204, `L-524`.  This supports a WRITTEN paragraph whose whole content is that
# the corpus already answers an objection it never names, so the pins are on the "already":
#   (1) the four PRIOR clauses asserted present in P7 -- ** if the globally-connected and global-
#       Cauchy-surface clauses were not there, this would be a NEW claim rather than a naming,
#       and the paragraph would be doing physics it is not entitled to **;
#   (2) the three links of the no-curve chain, likewise -- the absence of a Page curve must follow
#       from what is claimed elsewhere in the same paper or it is a bare assertion;
#   (3) the six written elements asserted present, including the objection stated AS an objection
#       and the falsifier stated AS a falsifier -- ** naming the scenario without naming its
#       objection would be the half-measure this item exists to prevent **;
#   (4) and the two target terms asserted to have LEFT zero, which is the measurable half of
#       56's finding.
#   NOT gated: any entropy, any Page time, any curve.  ** There is none to compute here and the
#   paper says why. **
# ============================================================================================
for what, pat in PRIOR:
    assert re.search(pat, P7, re.I | re.S), f"P7 lacks the prior clause: {what}"
for what, pat in CHAIN:
    assert re.search(pat, P7, re.I | re.S), f"the no-curve chain is broken: {what}"
for what, pat in NAMED:
    assert re.search(pat, P7, re.I | re.S), f"the written paragraph lacks: {what}"
assert _counts['Page curve'] > 0 and _counts['baby universe'] > 0, \
    "the two names are still absent from the corpus"
print(f"GATE c54.204 (r2540), `L-524`: the disconnection objection has no premise here — P7 already "
      f"states the spacetime stays globally connected and globally hyperbolic with a global Cauchy "
      f"surface throughout; the absence of a Page curve follows from the flux denial already claimed; "
      f"and 'Page curve' and 'baby universe' now stand at {_counts['Page curve']} and "
      f"{_counts['baby universe']} uses from zero, with the falsifier stated — pinned against "
      f"`FOR_54` item 53 (r2540) and P7 sec:paradox.")
