#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `spectra/c54.182_clpp.npz` RE-DERIVES **BIT-IDENTICALLY** FROM A PRODUCER THAT IS
IN THE REPOSITORY -- `L171x_lensing_potential.py`, AT ITS OWN DEFAULTS, ON THE CURRENT BACKGROUND.
ALL FOUR OF THE KEYS IT WRITES AGREE TO ZERO: `Phi`, `k`, `ls` AND THE LIMBER `cl` THAT PART B's
FIGURE IS BUILT FROM. **

*** AND THAT ANSWERS BY MEASUREMENT THE QUESTION `70` PUT TO `60`: whether a `c54`-era lensing
potential is admissible on the current background.  The artefact predates `LEAFSCALES` and the
current background returns the IDENTICAL arrays -- so the switch does not move this object, and the
era is not a defect in it. ***

⚠ ** WHAT DOES NOT RE-DERIVE IS NAMED AND NOT GLOSSED: three of the seven banked keys --
`cl_exact`, `cl_limber`, `l_exact` -- have no producer, because `L171x` computes the LIMBER integral
only.  The eight-multipole Limber-against-exact cross-check came from a computation that is not in
the repository, and this file does not claim otherwise. **

Built r7109+cc66.87 (node 66, code seat), on the second of `r7109` ⓷'s two unplaceables.

===================================================================================================
** WHAT `70` ASKED, AND WHY THE ANSWER IS BETTER THAN THE QUESTION EXPECTED **
===================================================================================================

`70`'s provenance audit: *"the lensing potential C_l^phiphi (`k`, `Phi`, exact and Limber), a
`c54`-era derived product, no producer ... **re-derive**, or re-point PART B onto a re-derivable
lensing source.  It is load-bearing, and its era predates `LEAFSCALES`."*  And node 66 added: *"I
have asked `60` for one line on whether a `c54`-era lensing potential is admissible on the current
background at all -- if it is not, then that receipt's part B has been standing on a superseded
object and not merely an unreproducible one."*

** Both halves come out favourably, and neither was assumed: **

  ⓐ ** THE OBJECT IS RE-DERIVABLE **, from `computations/beyond_the_wall/L171x_lensing_potential.py`
     -- which `70`'s matcher did not find because it postdates the artefact (`c54.184` against
     `c54.182`) and writes four of its seven keys.  *So "no producer" is literally true of the FILE
     and false of the OBJECT, and the distinction is the whole content of this receipt.*
  ⓑ ** AND IT IS NOT SUPERSEDED. **  Bit-identical is the strongest available answer to "is a
     `c54`-era potential admissible on the current background": the current background returns the
     same object, so nothing that changed since reaches it.  *The reason is in the producer's own
     docstring -- `Phi(k, a) = Phi(k, a_ref) g(a)/g(a_ref)` with `g` a BACKGROUND QUADRATURE, and no
     transfer function imported -- and this file measures that the reasoning holds rather than
     quoting it.*

  PART 1  ** THE PRODUCER IS TRACKED, AND WHAT IT WRITES IS ASSERTED AT SOURCE. **  Its `savez`
          writes exactly `ls, cl, k, Phi` -- which is WHY three banked keys have no producer, so the
          gap is derived from the source rather than observed and left unexplained.
  PART 2  ** BIT-IDENTICAL, ON EVERY SHARED KEY. **  Against the banked record of the re-derivation,
          which is banked beside the producer that wrote it.
  PART 3  ** THE THREE KEYS THAT DO NOT RE-DERIVE, AND WHAT THEY ARE FOR. **  PART B's
          Limber-against-exact table at eight multipoles.  *The Limber side IS re-derived -- it is
          the `cl` of PART 2; what has no producer is the EXACT projection it is compared against.*
  PART 4  ** AND WHAT PART B ACTUALLY STANDS ON, so the residual gap is sized. **  Read from that
          receipt's source: its FIGURE is built from `cl` and `ls`, both re-derived, while
          `cl_exact`/`cl_limber`/`l_exact` feed one printed table and one `worst` number and no
          figure.  ** So the load-bearing half is the re-derived half. **  ⚠ *And the read COUNT
          goes the other way -- three against two -- which is reported before the conclusion rather
          than after it: a read count is the wrong measure of load-bearing, and the structural fact
          is what the check rests on.*

===================================================================================================
** WHAT THIS DOES NOT CLAIM **
===================================================================================================

** It does not re-point PART B, and it does not propose to. **  That receipt is `c54.184`'s, not
this seat's, and with the object re-deriving bit-identically there is nothing to re-point it ONTO
that it is not already reading.  ** Nor does it build the exact projection: ** that would be new
machinery in another seat's instrument, and it is named as the remaining gap rather than filled.

** And no live re-derivation runs here, with the cost measured rather than asserted: ** the full run
is ~9 minutes (220 modes carried to eta = 4000) and a reduced `NKP=12 LMAXPHI=40` run still exceeds
two minutes, because the cost is the mode integration and not the mode count.  *So the record is
banked, exactly as the `cc66_lowell_sweep` producer's is, and the comparison below is made against
the BANK rather than trusting the record.*

** COMPUTES: nothing. ***  Two `.npz` files are read and compared, and two sources are read as text.
   The re-derivation they record was made by `L171x_lensing_potential.py` at ITS OWN defaults --
   `NKP=220`, `ETAREF=4000`, `LMAXPHI=2000`, `ARM` unset (the control, `D_M = 13865` Mpc, matching
   the banked control base) -- and this file chooses no parameter.

rc=0 on success.  Run: python3 P15_the_lensing_potential_re_derives_bit_identically_and_the_three_keys_that_do_not_are_a_cross_check_the_producer_never_computed.py
                       (numpy, ~2 s)
"""
import os
import subprocess
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
PRODUCER = os.path.join(BW, 'L171x_lensing_potential.py')
RECORD = os.path.join(BW, 'r7109_directions', 'clpp_rederive.npz')
BANK = os.path.join(BW, 'spectra', 'c54.182_clpp.npz')
READER = os.path.join(HERE, 'P15_the_residual_is_contrast_and_the_lensing_potential_is_derived.py')

# =====================================================================
print("=" * 100)
print("  PART 1 -- ** THE PRODUCER, AND WHAT IT WRITES, ASSERTED AT SOURCE **")
print("=" * 100)
INPUTS = [PRODUCER, RECORD, BANK, READER]
try:
    subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch'] + INPUTS,
                   check=True, capture_output=True)
    print(f"  all {len(INPUTS)} inputs are tracked by git in this checkout")
except subprocess.CalledProcessError as exc:
    fail.append("an input is not tracked by git: "
                + exc.stderr.decode('utf-8', 'replace').strip().split('\n')[0][:120])
except (OSError, FileNotFoundError):
    absent = [p for p in INPUTS if not os.path.exists(p)]
    if absent:
        fail.append(f"{len(absent)} input(s) absent and git unavailable to check tracking")
    else:
        print(f"  git unavailable here; all {len(INPUTS)} inputs exist (tracking unchecked)")

PSRC = open(PRODUCER, encoding='utf-8', errors='replace').read()
WRITES = "np.savez(os.environ.get('SAVEPHI', '/tmp/clpp.npz'), ls=ls, cl=cl, k=kk, Phi=Phi)"
if WRITES not in PSRC:
    fail.append("the producer's savez is not the four-key line this receipt's gap argument rests on "
                "-- re-read it before trusting PART 3")
else:
    print("  the producer writes exactly: ls, cl, k, Phi  (its one `savez`, quoted from source)")
# and it computes the LIMBER integral, which is why there is no exact side to write
if 'Limber:' not in PSRC or 'quad(integ' not in PSRC:
    fail.append("the producer no longer carries the Limber quadrature PART 3 attributes to it")
else:
    print("  and it computes the LIMBER projection (`quad(integ, ...)`), named as such in its own")
    print("  docstring -- so the EXACT projection is a thing it never computed")
# the era, from the file's own build line
if 'c54.184' not in PSRC:
    print("  ⌗ the producer no longer records c54.184 as its build -- the era note below is stale")
else:
    print("  the producer is built at c54.184; the artefact is c54.182 -- it POSTDATES what it makes,")
    print("  which is why a producer search keyed on the artefact's era does not find it")

# =====================================================================
print()
print("=" * 100)
print("  PART 2 -- ** BIT-IDENTICAL, ON EVERY SHARED KEY **")
print("=" * 100)
b = np.load(BANK)
r = np.load(RECORD)
BK, RK = set(b.files), set(r.files)
print(f"  banked keys ({len(BK)}): {sorted(BK)}")
print(f"  record keys ({len(RK)}): {sorted(RK)}")
shared = sorted(BK & RK)
print(f"\n  {'key':>6} {'shape':>10} {'elements differing':>20} {'worst relative':>16}")
worst = 0.0
for k in shared:
    x = np.atleast_1d(np.asarray(b[k], float))
    y = np.atleast_1d(np.asarray(r[k], float))
    if x.shape != y.shape:
        fail.append(f"{k}: the record's shape {y.shape} is not the bank's {x.shape}")
        continue
    nd = int(np.sum(x != y))
    rel = float(np.max(np.abs(y - x) / np.maximum(np.abs(x), 1e-300)))
    worst = max(worst, rel)
    print(f"  {k:>6} {str(x.shape):>10} {nd:>20d} {rel:>16.3e}")
    if nd != 0:
        fail.append(f"{k}: {nd} element(s) differ -- the re-derivation is NOT bit-identical, and "
                    f"this receipt's headline is wrong")
if not shared:
    fail.append("the record and the bank share no keys -- the comparison is vacuous")
elif worst == 0.0:
    print(f"\n  ** ZERO on all {len(shared)} shared keys. **  Not 'within tolerance' -- the same")
    print("     floating-point values, from a producer run on the CURRENT background.")
    print("  ⇒ ** So the era question is answered by measurement: the artefact predates `LEAFSCALES`")
    print("     and `LEAFSCALES` does not move it. **")
else:
    fail.append(f"the worst relative difference is {worst:.3e}, not zero")

# =====================================================================
print()
print("=" * 100)
print("  PART 3 -- ** THE THREE KEYS THAT DO NOT RE-DERIVE **")
print("=" * 100)
GAP = sorted(BK - RK)
print(f"  unproduced: {GAP}")
if set(GAP) != {'cl_exact', 'cl_limber', 'l_exact'}:
    fail.append(f"the unproduced set is {GAP}, not the Limber-against-exact triple this receipt "
                f"accounts for -- the gap has moved and the accounting is stale")
else:
    n_ex = len(np.atleast_1d(b['l_exact']))
    print(f"  all three are the Limber-against-exact cross-check, at {n_ex} multipoles: "
          f"l = {list(np.atleast_1d(b['l_exact']))}")
    print("  ** and the LIMBER side of that comparison IS re-derived -- it is PART 2's `cl`. **")
    print("     What has no producer is the EXACT projection it is compared against.")
    # the Limber column of the banked cross-check must be the banked cl at those multipoles,
    # or the two objects are not the same computation and PART 3's reading is wrong
    lsb = np.atleast_1d(np.asarray(b['ls'], float))
    clb = np.atleast_1d(np.asarray(b['cl'], float))
    lim = np.atleast_1d(np.asarray(b['cl_limber'], float))
    lx = np.atleast_1d(np.asarray(b['l_exact'], float))
    pick = np.array([np.argmin(np.abs(lsb - L)) for L in lx])
    on_grid = np.allclose(lsb[pick], lx)
    if on_grid:
        rel = float(np.max(np.abs(lim / clb[pick] - 1.0)))
        print(f"  ⌗ and the banked `cl_limber` matches the banked `cl` at those multipoles to "
              f"{rel:.3e} --")
        print("    so the cross-check's Limber column IS this object, and not a second computation")
        if rel > 1e-6:
            fail.append(f"the banked cl_limber departs from the banked cl by {rel:.3e} at the "
                        f"cross-check multipoles -- then they are not the same computation and "
                        f"PART 3's reading is wrong")
    else:
        print("  ⌗ the cross-check's multipoles are not on the `ls` grid, so this comparison is not")
        print("    available and PART 3 rests on the key names alone -- said rather than assumed")

# =====================================================================
print()
print("=" * 100)
print("  PART 4 -- ** AND WHAT PART B ACTUALLY STANDS ON, SO THE GAP IS SIZED **")
print("=" * 100)
RSRC = open(READER, encoding='utf-8', errors='replace').read()
uses = {k: RSRC.count(f"z2['{k}']") for k in sorted(BK)}
print(f"  how often that receipt reads each banked key: {uses}")
if 'c54.182_clpp' not in RSRC:
    fail.append("the reading receipt no longer loads c54.182_clpp -- this file's premise has moved")
re_derived_used = sum(v for k, v in uses.items() if k in RK)
gap_used = sum(v for k, v in uses.items() if k in GAP)
print(f"  reads of RE-DERIVED keys: {re_derived_used};  reads of UNPRODUCED keys: {gap_used}")
if re_derived_used == 0:
    fail.append("that receipt reads none of the re-derived keys -- then PART 2 closes nothing for it")
# ⚠ ** AND THE COUNT GOES THE OTHER WAY, WHICH IS SAID BEFORE THE CONCLUSION AND NOT AFTER IT. **
#   Three reads against two.  *A read count is the wrong measure of load-bearing, and it is reported
#   here precisely so the conclusion below is not read as resting on it.*  What settles it is WHAT
#   each key feeds, which is a structural fact and is asserted:
FIGURE = "P = (ls * (ls + 1)) ** 2 * cl / (2 * np.pi) * AMP"
if FIGURE not in RSRC:
    print("  ⌗ that receipt no longer builds its figure from `cl` on the line this file quotes --")
    print("    PART 4's sizing is not available and rests on nothing; re-read it.")
    fail.append("the figure line PART 4's sizing depends on is not in the reading receipt")
else:
    print(f"  the figure that receipt plots, quoted from its source: `{FIGURE}`")
    print("  ** built from `cl` and `ls` -- both re-derived.  The three unproduced keys feed one")
    print("     printed table and one `worst` number, and no figure. **")
print("  ⌗ *This is a SIZING of the gap and not a dismissal of it: a cross-check with no producer is")
print("   still a cross-check nobody can repeat, and it stays on the provenance list.*")

# =====================================================================
print()
print("=" * 100)
if fail:
    print(f"  FAIL -- {len(fail)} check(s) did not hold")
    for f in fail:
        print(f"    - {f}")
    print("=" * 100)
    sys.exit(1)
print("  ** ALL CHECKS HOLD. **  `c54.182_clpp`'s potential re-derives BIT-IDENTICALLY from")
print(f"  `L171x_lensing_potential.py` on the current background, on all {len(shared)} keys that")
print("  producer writes -- so the object is placed, and `LEAFSCALES` demonstrably does not move it.")
print(f"  ** What remains unplaceable is the {len(GAP)}-key Limber-against-exact cross-check, whose")
print("  EXACT side the producer never computed -- named here, not filled, and not glossed. **")
print("=" * 100)
sys.exit(0)
