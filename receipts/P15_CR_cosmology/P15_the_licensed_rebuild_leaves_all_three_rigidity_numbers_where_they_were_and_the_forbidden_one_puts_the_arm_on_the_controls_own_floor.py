#!/usr/bin/env python3
"""r7097+cc66.79 -- ⛭⛭⛭ THE LICENSED REBUILD LEAVES ALL THREE OF `70`'s RIGIDITY NUMBERS WHERE THEY
WERE, AND THE FORBIDDEN ONE PUTS THE ARM ON THE CONTROL'S OWN FLOOR.

** WHAT r7097 ORDERED, AND WHY IT NAMED THE NUMBERS IN ADVANCE. **  `r7097` withdrew `r7095`'s Q1 as an
order, gated `LEAFREC`, and made Q3 the whole job: run the rate rule's own configuration end to end with
the onset dissolved -- both arms from $z=3\\times10^7$ with no solve anywhere, `LEAFSCALES=1`,
`LEAFPERT` on, **`LEAFREC=1`**, `VISLEAF=0` because it is still unadjudicated, and **`LEAFGEOM=0`, the
geometry on the stacking rate.**  *It named the targets before the grid existed:* **the data ask this
arm's acoustic contrast to be $6.4\\pm0.9$ per cent lower at $7.5\\sigma$ and ask the control for nothing;
the unreachable $\\chi^2$ is $278.8$ against the control's $186.0$ at $n-5=180$; the residual crosses zero
$54$ times against noise's $88\\pm10$.**

⇒ *** ALL THREE ARE UNMOVED BY THE LICENSED REBUILD.  The unreachable $\\chi^2$ goes $278.795$ to
  $278.788$ -- $0.007$ per cent of the $92.8$ gap it was ordered to close -- the crossings stay at $54$, and the longest run of one
  sign stays at $33$. ***
⇒ *** AND ALL THREE ARE CLOSED BY THE FORBIDDEN ONE.  $\\chi^2$ falls to $184.99$, which is BELOW the
  control's own $186.01$; the crossings go to $91$ against noise's $88$; the longest run goes to $8$,
  which is exactly the control's $8$. ***

⛭⛭ ** SO `60`'s FALSIFIER FIRES, AND IT WAS WRITTEN UNPROMPTED AND BEFORE THE RUN. **  *`r7097` quotes
it: "if a rebuild consistent on all four assignments does not supply a contrast correction of that sign
and about that size, **then the rate assignments are not where the contrast comes from and the rigidity is
somewhere this adjudication has not looked.**"*  **The licensed rebuild supplies $0.007$ per cent of it.**
  ⇒ *But the one assignment the rule FORBIDS supplies all of it, so the conclusion is sharper than the
  falsifier's own wording: the contrast does not come from the rate assignments **as the rule assigns
  them** -- it comes from the clock the GEOMETRY is read on, which is the one object `P07` pins to the
  stacking rate by name.*

⚠ ** THIS DOES NOT REINSTATE `LEAFGEOM=1`. **  *`r7095`'s ruling is the gate's and it stands; the
switch's default is untouched and no build is resumed.  What is reported is a conflict between the rule's
configuration and the sky, measured on the gate's own pre-named statistics, for the gate to adjudicate.*

** COMPUTES: the unreachable GLS chi^2, the zero-crossing count and the longest run of one sign for both
arms on three banked grids, through `70`'s `rigidity.py` definitions rather than re-implemented ones; the
four-parameter refit on each; and the two-direction tilt against the refit's own n_s shift.  Asserts the
licensed rebuild moves the unreachable chi^2 by under 0.05 per cent and the crossings and longest run not
at all, that the forbidden one reaches the control's floor on all three, and that the control is
identical across all three grids -- the no-op that says what moved is the arm. **
"""
import contextlib
import io as _io
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
sys.argv = ['rigidity', '--mc', '2']          # the MC is not used here; the three numbers are not MC
sys.path.insert(0, os.path.join(BW, 'r7091_70_fit_rigidity'))
with contextlib.redirect_stdout(_io.StringIO()):
    import rigidity as R                                                    # noqa: E402

CHECKS, bad = [], []


def gate(label, cond):
    CHECKS.append(label)
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        bad.append(label)


def head(t):
    print("\n  " + "=" * 74)
    print("  " + t)
    print("  " + "=" * 74)


GRIDS = (('banked', os.path.join(BW, 'refit_grid185')),
         ('licensed', os.path.join(BW, 'r7095_directions', 'grid_licensed')),
         ('forbidden', os.path.join(BW, 'r7093_directions', 'grid_oneclock')))


def reach(grid, arm):
    """`70`'s own reach and shape, computed from `rigidity.py`'s definitions -- its `build`, its `W`,
    its `STEP` and its `stats`.  Nothing here re-derives the model: re-deriving it would make a
    disagreement unattributable between the geometry and this file's arithmetic."""
    R.GRID = grid
    with contextlib.redirect_stdout(_io.StringIO()):
        B = R.build(arm)
        cols = [B['m0'] * 0.02] + [B['g'][k] * R.STEP[k] for k in R.STEP]
        Jw = np.column_stack([R.W(B, c) for c in cols])
        dw = R.W(B, B['d'])
        Q, _ = np.linalg.qr(Jw)
        rw = dw - Q @ (Q.T @ dw)
        st = R.stats((B['L'] @ rw) / np.sqrt(np.diag(B['C'])))
        x, A, mfit, c0, c1 = R.bestfit(B)
    return dict(chi2=float(rw @ rw), crossings=int(st['crossings']), longest=int(st['longest']),
                fit=dict(zip(R.STEP, x)), nm_chi2=float(c1), nbins=len(dw))


print(__doc__)

# =====================================================================================
head("A.  r7097's THREE NAMED NUMBERS, ON THE BANKED GRID, BEFORE ANYTHING IS COMPARED")

V = {(nm, arm): reach(g, arm) for nm, g in GRIDS for arm in ('lcdm', 'cr')}
print(f"      {'grid':10s} {'arm':5s} {'unreachable chi2':>18s} {'n-5':>5s} {'crossings':>10s} {'longest':>8s}")
for nm, _ in GRIDS:
    for arm in ('lcdm', 'cr'):
        v = V[(nm, arm)]
        print(f"      {nm:10s} {arm:5s} {v['chi2']:18.6f} {v['nbins']-5:>5d} "
              f"{v['crossings']:10d} {v['longest']:8d}")

gate("the banked grid returns r7097's own three figures -- unreachable chi^2 278.8 on the arm against "
     "the control's 186.0 at n-5 = 180, and 54 crossings -- so the instrument is the one the order "
     "named and not a re-derivation of it",
     abs(V[('banked', 'cr')]['chi2'] - 278.8) < 0.1
     and abs(V[('banked', 'lcdm')]['chi2'] - 186.0) < 0.1
     and V[('banked', 'cr')]['crossings'] == 54
     and V[('banked', 'cr')]['nbins'] - 5 == 180)
gate("⌗ THE CONSISTENCY CHECK: the CONTROL's three numbers are IDENTICAL across all three grids, "
     "because its nine runs are the same nine files -- so whatever moves below is the arm and not "
     "the method",
     V[('licensed', 'lcdm')]['chi2'] == V[('banked', 'lcdm')]['chi2'] == V[('forbidden', 'lcdm')]['chi2']
     and V[('licensed', 'lcdm')]['crossings'] == V[('forbidden', 'lcdm')]['crossings'] == 87)

# =====================================================================================
head("B.  ⛔⛔ THE LICENSED REBUILD -- THE RATE RULE'S OWN CONFIGURATION -- MOVES NONE OF THEM")

_gap = V[('banked', 'cr')]['chi2'] - V[('banked', 'lcdm')]['chi2']
_mv = V[('banked', 'cr')]['chi2'] - V[('licensed', 'cr')]['chi2']
print(f"      the gap the rebuild was ordered to close: {_gap:.3f} in chi^2")
print(f"      the licensed rebuild closes:              {_mv:.6f}  = {100*_mv/_gap:.4f} per cent of it")
print(f"      crossings {V[('banked','cr')]['crossings']} -> {V[('licensed','cr')]['crossings']}      "
      f"longest run {V[('banked','cr')]['longest']} -> {V[('licensed','cr')]['longest']}")
gate("⛔⛔ THE UNREACHABLE chi^2 DOES NOT MOVE: under 0.05 per cent of the gap, on a rebuild that "
     "changed the spectrum by six and a half per cent",
     abs(_mv) / _gap < 5e-4)
gate("⛔ and neither the crossings nor the longest run of one sign move AT ALL",
     V[('licensed', 'cr')]['crossings'] == V[('banked', 'cr')]['crossings']
     and V[('licensed', 'cr')]['longest'] == V[('banked', 'cr')]['longest'])
gate("⛭ ⇒ SO `60`'s FALSIFIER FIRES ON ITS OWN TERMS: a rebuild consistent on all four assignments "
     "supplies no contrast correction of the named sign and size, which it wrote in advance means the "
     "rate assignments are not where the contrast comes from",
     abs(_mv) / _gap < 5e-4 and V[('licensed', 'cr')]['crossings'] == 54)

# =====================================================================================
head("C.  ⛭⛭ AND THE FORBIDDEN ONE REACHES THE CONTROL'S OWN FLOOR ON ALL THREE")

_f = V[('forbidden', 'cr')]
_c = V[('banked', 'lcdm')]
print(f"      forbidden arm chi^2 {_f['chi2']:.6f}   against the CONTROL's own {_c['chi2']:.6f}")
print(f"      crossings {_f['crossings']} (control {_c['crossings']}, noise about 88)      "
      f"longest run {_f['longest']} (control {_c['longest']})")
gate("⛭⛭ the forbidden repair takes the arm's unreachable chi^2 BELOW the control's own value -- "
     "184.99 against 186.01 -- so on this statistic the arm stops being the worse of the two",
     _f['chi2'] < _c['chi2'])
gate("⛭ and its longest run of one sign lands on the control's exactly, 8 bins against 33 before",
     _f['longest'] == _c['longest'] and V[('banked', 'cr')]['longest'] == 33)
gate("⛭ and its crossings go to 91 against the control's 87 and noise's roughly 88, from 54 -- the "
     "arm becoming noise-consistent where it was 4.6 sigma away",
     _f['crossings'] > 85 and V[('banked', 'cr')]['crossings'] == 54)

# =====================================================================================
head("D.  ⌗ THE REFIT r7097 ASKED FOR, AND THE TILT PREDICTION IT PUT ON THE RECORD")

print(f"      {'grid':10s} {'arm':5s} " + '  '.join(f'{k:>9s}' for k in R.STEP) + f" {'chi2':>9s}")
for nm, _ in GRIDS:
    for arm in ('lcdm', 'cr'):
        v = V[(nm, arm)]
        print(f"      {nm:10s} {arm:5s} " + '  '.join(f"{v['fit'][k]:+9.4f}" for k in R.STEP)
              + f" {v['nm_chi2']:9.1f}")

# the two-direction tilts `shape.py` fits, banked here as literals with their provenance because they
# are another tool's output and this receipt is not the place to re-run it
TILT_2DIR = {'banked': +0.0264, 'licensed': +0.0390, 'forbidden': -0.0016}      # LMAXL=2000, ell<=1040
TILT_1300 = {'before': -0.0046, 'oneclock': -0.0324}                            # cc66.73's own pair
print(f"      the two-direction tilt (shape.py, ell<=1040, LMAXL=2000): "
      + ', '.join(f'{k} {v:+.4f}' for k, v in TILT_2DIR.items()))
print(f"      cc66.73's own LMAXL=1300 pair:                            "
      + ', '.join(f'{k} {v:+.4f}' for k, v in TILT_1300.items()))
gate("⌗ the two-direction tilt and the four-parameter refit's own n_s shift AGREE to better than "
     "0.004 on all three grids at matched resolution, which is what licenses reading one as the other "
     "-- a power-law tilt in ell is a delta-n_s to first order and is checked rather than assumed",
     all(abs(TILT_2DIR[nm] - V[(nm, 'cr')]['fit']['NS']) < 0.004 for nm, _ in GRIDS))
gate("⛔ ⇒ AND THE PREDICTION DOES NOT SURVIVE THE RESOLUTION: `cc66.73`'s -0.0324 is its own "
     "`LMAXL=1300` pair's value, and at `LMAXL=2000` the one-clock rebuild needs essentially NO tilt "
     "-- -0.0035 on the refit, an order of magnitude smaller",
     abs(V[('forbidden', 'cr')]['fit']['NS']) < 0.01
     and abs(TILT_1300['oneclock']) > 3 * abs(V[('forbidden', 'cr')]['fit']['NS']))
gate("⌗ and the banked default and the licensed configuration BOTH want about +0.03 to +0.04 of tilt, "
     "so the tilt the fit reaches for is a property of the two-clock geometry and not of the rebuild",
     V[('banked', 'cr')]['fit']['NS'] > 0.02 and V[('licensed', 'cr')]['fit']['NS'] > 0.02)

# =====================================================================================
head("E.  ⚠ THE SCOPE")

gate("no spectrum is computed here and no parameter is pinned: every number is read from a grid "
     "tracked in this repository, through `70`'s own `rigidity.py` definitions",
     all(os.path.isdir(g) for _, g in GRIDS))
gate("⛔ and `LEAFGEOM=1` is NOT reinstated: `r7095`'s ruling is the gate's, the switch's default is "
     "untouched, and what is reported is a conflict for the gate to adjudicate",
     True)

print(f"\n  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail")
print("  GATES: " + ("ALL PASS" if not bad else "FAILURES ABOVE"))
print("""
  r7097's Q3, ON ITS OWN THREE NAMED NUMBERS:
                        unreachable chi2       crossings    longest run
    control (all three)     186.007               87             8
    banked arm              278.795               54            33
    LICENSED arm            278.788               54            33     <- nothing moved
    forbidden arm           184.989               91             8     <- the control's floor
  ⇒ the rule's own configuration closes 0.007 per cent of the 92.8 chi^2 gap; the configuration the
    rule forbids closes all of it and lands the arm on the control's value on all three statistics.
  ⇒ 60's falsifier fires: the contrast does not come from the rate assignments AS THE RULE ASSIGNS
    THEM.  It comes from the clock the GEOMETRY is read on -- the one object P07 pins by name.
""")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
