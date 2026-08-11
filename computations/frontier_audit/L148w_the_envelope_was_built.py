#!/usr/bin/env python3
"""
L-148w — `E·3`, THE COHERENCE → PEAK-HEIGHTS TRANSFER. ITS OPEN CORE WAS BUILT, RECEIPTED ELEVEN
TIMES, AND THE MAP NEVER RECORDED IT.

`E·3`'s status, carried since r1408 and folded into the register verbatim at c54.90:

    *"the open core is NOT a stand-alone CMB transfer. It is the short-wavelength (high-$\\ell$)
    collapse-phase driving envelope — the peak heights above $\\ell\\approx800$ — which per
    §coherence lives on the CONTRACTING collapse leg (L2), radiation gravitating on the
    progenitor excursion, **UNCOMPUTED**."*

** IT IS COMPUTED.  P15 carries a `sec:envelope` and a `sec:envelope-consequence` built out of an
eleven-step chain, C1 through C11, each with its own receipt -- and one of them, `C7`, is named
in its own summary as *\"THE STEP THE TRAP WAS GUARDING\"*. **

  PART 1  The chain, step by step, checked against the receipt index.
  PART 2  ** THE TRAP `E·3` NAMES WAS NOT FALLEN INTO -- IT WAS GUARDED, AND THEN REMOVED. **
  PART 3  What actually remains, and it is another item on this same map.
  PART 4  `L-148` struck, and what the miss cost.

Run: python3 L148w_the_envelope_was_built.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# =====================================================================
print("=" * 78)
print("PART 1 — THE CHAIN, CHECKED AGAINST THE INDEX")
print("=" * 78)
rows = {}
for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8'):
    if not ln.startswith('| P'):
        continue
    c = [x.strip() for x in re.split(r'(?<!\\)\|', ln.rstrip('\n'))[1:-1]]
    if len(c) != 8:
        continue
    st = re.search(r'`([^`]+)`', c[3])
    if st:
        rows[os.path.splitext(os.path.basename(st.group(1)))[0]] = (c[0], c[1], c[2])

CHAIN = [
    ("C1_closure_of_the_driving", "does the acoustic oscillator close in elementary terms on the collapse leg"),
    ("C2_horizon_limits", "the comoving Hubble radius across the excursion, from the corpus's own geometry"),
    ("C3_conformal_map", "conformal time on the leg -- does the map from the limits close too"),
    ("C4_driving_envelope", "ASSEMBLE IT: integrand + limits + map, on the collapse leg"),
    ("C5b_baryon_term", "the baryon term, the first of the two C4 named as missing"),
    ("C6_neutrino_term", "the anisotropic-stress term, the second"),
    ("C7_equality_and_deficit", "** THE STEP THE TRAP WAS GUARDING **"),
    ("C8_diffusion_length", "r_D derived here from first principles, on the same footing"),
    ("C9_sound_horizon_and_ratio", "r_s and r_D with the correct lower limit: THE SEAM"),
    ("C10_highl_ratio", "the high-ell ratio, assembled from derived pieces only"),
    ("C11_early_isw", "the early ISW, the last named piece"),
]
print(f"  {'receipt':>28} {'registered?':>12} {'paper':>6} {'section':>26}")
missing = []
for stem, what in CHAIN:
    hit = rows.get(stem)
    print(f"  {stem:>28} {('** yes **' if hit else 'NO'):>12} "
          f"{(hit[0] if hit else '-'):>6} {(hit[1] if hit else '-'):>26}")
    if not hit:
        missing.append(stem)
print()
print(f"  ** {len(CHAIN) - len(missing)} of {len(CHAIN)} steps registered in the receipt index. **")
assert not missing, missing
print()
for s in [
 "⌗ ** AND THE SECTIONS EXIST IN THE PAPER, NOT ONLY THE RECEIPTS: P15 carries `sec:envelope`",
 "   and `sec:envelope-consequence`, and the framework paper's own frontier item already reports",
 "   the outcome -- *'the collapse-phase driving envelope is derived in closed form and is flat",
 "   above ten times the seam's horizon wavenumber, with its turnover at the equality the",
 "   inherited datum fixes, so the peak heights verified through the third peak continue to",
 "   track.'* **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TRAP WAS GUARDED, AND THEN REMOVED")
print("=" * 78)
for s in [
 "`E·3` carries a warning in capitals: ** *'★ THE TRAP (burned two nodes): taking $\\Lambda$CDM's",
 "$C_\\ell$ as the high-$\\ell$ envelope + applying the $+8\\%$ damping manufactures a spurious",
 "\"decisive deficit\" -- §coherence DISOWNS it (\"precisely the unbuilt part\")'* **",
 "",
 "⌗ ** `C7`'s OWN SUMMARY IS THE ANSWER TO THAT WARNING, IN THE SAME WORDS: ** *'full_transfer_",
 "   verdict.py ASSUMED the high-ell peaks equal LambdaCDM's and applied the extra damping,",
 "   getting a large deficit -- and P15 disowns it because \"that assumption IS the unbuilt part.\"",
 "   ** C4 built it. ** So the same calculation can now be done with a DERIVED envelope.'*",
 "",
 "⇒⇒ ** SO THE TRAP WAS NOT MERELY AVOIDED: THE THING THAT MADE IT A TRAP -- the envelope being",
 "   unbuilt -- WAS REMOVED, AND THE CALCULATION REDONE ON THE DERIVED ONE. **  *The warning is",
 "   still worth keeping as a record of how two nodes were burned; it is no longer a live hazard.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT ACTUALLY REMAINS, AND IT IS ANOTHER ITEM ON THIS MAP")
print("=" * 78)
print(f"  {'the framework paper says what is left':>44} {'where that already lives':>30}")
for a, b in [
    ("the full-spectrum likelihood-level comparison", "** `E·2` -- the map's own item **"),
    ("(a parameter refit, not a further calculation)", "registered as `L-147`"),
    ("the odd/even height pattern", "ordinary content physics on the"),
    ("(baryon loading on the expansion leg)", "expansion leg; not a transfer"),
]:
    print(f"  {a:>44} {b:>30}")
print()
for s in [
 "⇒ ** `E·3` HAS NO REMAINDER OF ITS OWN.  What is left of it is `E·2`, which the map already",
 "   carries as a separate item, and a height pattern the corpus classifies as ordinary content",
 "   physics rather than as this transfer's business. **",
 "",
 "⌗ *That is the cleanest kind of strike: the item does not need re-scoping or re-gating, because",
 "its residue is somewhere the register can already see.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — `L-148` STRUCK, AND WHAT THE MISS COST")
print("=" * 78)
for s in [
 "✔ ** `L-148` (the map's `E·3`) STRIKES: its open core is built, eleven receipts deep, its trap",
 "   is disarmed by the build, and its residue is `E·2`. **",
 "",
 "⚠⚠ ** AND THE MISS IS THE POINT, BECAUSE IT IS THE FOLD'S WHOLE ARGUMENT IN ONE ITEM. **  *The",
 "   map described this as UNCOMPUTED, in capitals, while the corpus carried a named section, a",
 "   named consequence section, eleven registered receipts, and a frontier-item summary reporting",
 "   the result.*  ** Nothing was hidden; the map simply had no mechanism for noticing, and the",
 "   register it has now been folded into does. **",
 "",
 "⌗ *The status text was written at r1408 and the build ran around r1927--r1975.  ** The item sat",
 "wrong for roughly five hundred revisions, and the first scan after the fold found it. ***",
]:
    print("  " + s)
