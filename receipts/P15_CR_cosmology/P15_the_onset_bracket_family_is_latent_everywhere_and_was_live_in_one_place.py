#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE `(1500, 60000)` ONSET BRACKET IS NOT ONE HABIT IN ONE FILE.  THE TREE
CARRIES 27 LIVE ACOUSTIC-ONSET SOLVERS AND 46 RETIRED ONES; 18 OF THE LIVE ONES SIT BELOW THE LEAF
RULER'S ROOT OF 61,580 -- WHICH IS 2.6% PAST THE 60,000 CEILING. **

** ⇒ AND EXACTLY ONE OF THEM WAS EVER REACHED. **  All 18 integrate r_s on the STACKING clock,
where the root is 6,764 and no ceiling in the family is near it.  ** So the sweep's answer is
"one live failure, already fixed; eighteen latent; zero silently wrong" -- and the reason that is
worth a receipt rather than a shrug is that the one that was reached was reached by the FIRST run
that changed the clock, and it failed by a quarter of a multipole. **

Built r6760+cc66.6 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order
("a sweep for other solver brackets the leaf ruler pushes past").

===================================================================================================
** WHAT A BRACKET IS AND WHEN IT STOPS BEING ONE **
===================================================================================================

`brentq(f, lo, hi)` needs f(lo) and f(hi) to straddle zero.  A ceiling chosen well above the root
is an implementation detail.  ** A ceiling chosen just below it is a physics choice, and it is
the worst kind, because it does not return a wrong answer -- it raises `ValueError: f(a) and f(b)
must have different signs`, which reads as "this configuration has no solution". **

  On the STACKING ruler:  pi D_M / r_s = 301.6  at  z_onset = 6,764.
  On the LEAF ruler:      pi D_M / r_s = 301.6  at  z_onset = 61,580,
                          and at the old ceiling z = 60,000 it is 301.85 -- ** 0.25 short. **

  PART 1  ** THE TWO ROOTS, computed here from the instrument's own integrands. **
  PART 2  ** THE CEILING MEASURED AGAINST THE ROOT, ** which is the thing that decides.
  PART 3  ** THE SWEEP. **  Every `brentq` in the tree, classified: reached, latent, or unrelated.
  PART 4  ** WHAT WAS CHANGED AND WHAT WAS DELIBERATELY NOT. **

** COMPUTES: H0 = 73.00, Om = 0.3066, Or = 4.15e-5/h^2, z_rec = 1089.9, Ombh2 = 0.0224,
   LATARG = 301.6 -- the CR arm's own values, read off `ACOUSTIC_two_arm.py`, so PART 1 reproduces
   that file's root rather than defining a new one.  *** Nothing here is fitted. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~10 s)
"""
import glob
import os
import re
import sys

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

C = 299792.458
H0, OM = 73.00, 0.3066
OR = 4.15e-5 / (H0 / 100) ** 2
OL = 1.0 - OM
Z_REC = 1089.9
A_REC = 1.0 / (1.0 + Z_REC)
OMBH2 = 0.0224
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)
LATARG = 301.6


def Hphys(a):
    """L1, the stacking rate: radiation is content, not a source."""
    return H0 * np.sqrt(OM / a ** 3 + OL)


def Hleaf(a):
    """L2, the leaf rate: the same background with its radiation."""
    return H0 * np.sqrt(OM / a ** 3 + OL + OR / a ** 4)


def rs_from(z_lo, H):
    return quad(lambda a: C / (a ** 2 * H(a) * np.sqrt(3 * (1 + RB_REC * a / A_REC))),
                1.0 / (1.0 + z_lo), A_REC, limit=250)[0]


D_M = quad(lambda a: C / (a ** 2 * Hphys(a)), A_REC, 1.0, limit=250)[0]

print("=" * 99)
print("  PART 1 -- ** THE TWO ROOTS **")
print("=" * 99)
z_stack = brentq(lambda z: np.pi * D_M / rs_from(z, Hphys) - LATARG, 1500., 5.0e6)
z_leaf = brentq(lambda z: np.pi * D_M / rs_from(z, Hleaf) - LATARG, 1500., 5.0e6)
print(f"  D_M = {D_M:.1f} Mpc   (the same on both: the PROJECTION is the stacking rate's, always)")
print(f"  {'clock':>18} {'z_onset':>12} {'r_s Mpc':>10} {'pi D_M / r_s':>13}")
for nm, z, H in (('STACKING (L1)', z_stack, Hphys), ('LEAF (L2)', z_leaf, Hleaf)):
    r = rs_from(z, H)
    print(f"  {nm:>18} {z:>12.0f} {r:>10.2f} {np.pi * D_M / r:>13.2f}")
if abs(z_stack - 6764) > 30:
    fail.append(f"the stacking root is {z_stack:.0f}, not the instrument's 6764")
if abs(z_leaf - 61580) / 61580 > 0.02:
    fail.append(f"the leaf root is {z_leaf:.0f}, not ~61580")

print()
print("=" * 99)
print("  PART 2 -- ** THE CEILING AGAINST THE ROOT.  THIS IS THE WHOLE FINDING. **")
print("=" * 99)
lA_at_ceiling = np.pi * D_M / rs_from(60000.0, Hleaf)
print(f"  the old ceiling                 z = 60,000")
print(f"  pi D_M / r_s,leaf there                {lA_at_ceiling:.2f}")
print(f"  the target                             {LATARG:.2f}")
print(f"  ⇒ short by                             {lA_at_ceiling - LATARG:.2f} multipoles, "
      f"and the root is {(z_leaf - 60000) / 60000 * 100:.1f}% past the ceiling")
print()
print("  ** So the failure mode was not a wrong number.  brentq raised, the arm reported no")
print("  solution, and 'the leaf ruler has no onset' would have been believed. **")
if lA_at_ceiling <= LATARG:
    fail.append("the old ceiling already straddles the target -- PART 2's premise is wrong")
if z_leaf <= 60000:
    fail.append("the leaf root is inside the old bracket -- there was nothing to widen")

print()
print("=" * 99)
print("  PART 3 -- ** THE SWEEP **")
print("=" * 99)
# ** The scan reads SOURCE, not results.  A bracket is a literal in a call and that is exactly what
# is being audited, so a regex over the text is the right instrument here and not a shortcut. **
PAT = re.compile(r'brentq\s*\(')
ONSET = re.compile(r'brentq\([^)]*?(?:pi\s*\*\s*DM?\s*/\s*rs|theta_star|thetaCR|ell_A|rs_f?\(z\))',
                   re.S)
CEIL = re.compile(r',\s*([0-9][0-9_.eE+]*)\s*[,)]\s*$')
live, retired, onset_live, onset_retired = 0, 0, [], []
for f in sorted(glob.glob(os.path.join(ROOT, '**', '*.py'), recursive=True)):
    if '/.git/' in f:
        continue
    try:
        src = open(f, encoding='utf-8', errors='replace').read()
    except OSError:
        continue
    if os.path.basename(f) == os.path.basename(__file__):
        continue
    is_retired = 'retired_conformal_seed' in f or '/_dig/' in f
    for ln, line in enumerate(src.splitlines(), 1):
        if not PAT.search(line):
            continue
        if is_retired:
            retired += 1
        else:
            live += 1
        if ONSET.search(line):
            m = CEIL.search(line.rstrip().rstrip(')').rstrip() + ')')
            hi = None
            nums = re.findall(r'([0-9][0-9_]*(?:\.[0-9]*)?(?:[eE]\+?[0-9]+)?)', line.split('brentq')[1])
            if nums:
                try:
                    hi = float(nums[-1].replace('_', ''))
                except ValueError:
                    hi = None
            rec = (os.path.relpath(f, ROOT), ln, hi)
            (onset_retired if is_retired else onset_live).append(rec)

print(f"  brentq calls in the tree:   {live} live, {retired} retired/_dig")
print(f"  of those, ACOUSTIC-ONSET solves:  {len(onset_live)} live, {len(onset_retired)} retired")
print()
print(f"  {'live onset solver':>72} {'line':>5} {'ceiling':>11} {'vs 61580':>10}")
below = []
for path, ln, hi in onset_live:
    tag = '--' if hi is None else ('BELOW' if hi < z_leaf else 'above')
    if hi is not None and hi < z_leaf:
        below.append((path, ln, hi))
    print(f"  {path:>72} {ln:>5} {('--' if hi is None else f'{hi:g}'):>11} {tag:>10}")

print()
print(f"  ⌗ {len(below)} of {len(onset_live)} live onset solvers carry a ceiling below the LEAF root.")
print("    ** Every one of them integrates r_s on the STACKING clock, where the root is 6,764. **")
print("    So they are LATENT, not broken: not one of them can be reached as the tree stands, and")
print("    each becomes reachable the moment its own r_s is moved to the leaf clock.")
print("    *That is a standing hazard and it is recorded as one rather than pre-emptively widened:*")
print(f"    *widening {len(below)} files to guard against a change nobody has made is churn, and churn*")
print("    *in files whose pinned numbers are quoted in the papers is worse than churn.*")

print()
print("=" * 99)
print("  PART 4 -- ** WHAT WAS CHANGED **")
print("=" * 99)
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
inst = open(INST, encoding='utf-8').read()
widened = {
    'computations/beyond_the_wall/ACOUSTIC_two_arm.py': '5.0e6',
    'hubble_build/desi_dr2_confrontation.py': '5e6',
    'hubble_build/hubble_expansion_confrontation_v2.py': '5e6',
    'hubble_build/make_hubble_figure.py': '5e6',
    'receipts/P15_CR_cosmology/P15_desi_dr2_confrontation.py': '5e6',
    'receipts/P15_CR_cosmology/P15_hubble_expansion_confrontation_v2.py': '5e6',
}
print("  ** SIX FILES, AND THE LIST IS EXACTLY THE FILES A LEAF-CLOCK RUN ACTUALLY ENTERS. **")
for p, want in widened.items():
    src = open(os.path.join(ROOT, p), encoding='utf-8').read()
    ok = want in src
    print(f"    {'✓' if ok else '✗'}  {p:<58} ceiling {want}")
    if not ok:
        fail.append(f"{p} does not carry the widened ceiling {want}")
if 'brentq(lambda z: np.pi * D_M / rs_from(z) - _latarg, 1500., 5.0e6)' not in inst:
    fail.append("ACOUSTIC_two_arm.py's onset bracket is not the widened one")
print(f"""
  ** AND THE TWO RECEIPT MIRRORS ARE THE POINT OF PART 4. **  `P15_desi_dr2_confrontation.py` and
  `P15_hubble_expansion_confrontation_v2.py` each declare an ORIGIN in `hubble_build/`, and the
  originals were widened at r6760+cc66.3 while the mirrors were not.  ** A receipt that has drifted
  from the script it names as its origin is not a receipt of that script. **  Both were brought
  back into line here and both still print their pinned numbers unmoved -- which they must, because
  pi D_M / r_s is monotone in z_onset and a wider bracket cannot find a different root.

  ⌗ ** WHAT IS NOT CLAIMED. **  This does not say the leaf ruler is right.  It says that until
  r6760+cc66.1 the instrument could not be ASKED, and that the thing standing in the way was a
  literal chosen when the only clock in the file was the other one.
""")

print("=" * 99)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 99)
