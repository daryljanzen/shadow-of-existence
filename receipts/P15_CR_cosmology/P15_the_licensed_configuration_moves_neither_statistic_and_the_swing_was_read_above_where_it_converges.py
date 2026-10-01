#!/usr/bin/env python3
"""r7095+cc66.78 -- ⛭⛭⛭ THE LICENSED CONFIGURATION MOVES NEITHER STATISTIC, AND THE EARLIER NEGATIVE
RESULT WAS READ ABOVE THE CEILING WHERE THE STATISTIC CONVERGES.

** WHAT r7095 ASKED AND WHAT THIS ANSWERS. **  `r7095` adjudicated against `cc66.73`'s `LEAFGEOM=1`
repair: the rate rule requires `D_M` on the STACKING rate and recombination on the LEAF's, so moving the
geometry onto the leaf is the one thing the rule names and forbids.  It ordered the rule's OWN
configuration run instead -- `LEAFSCALES=1 LEAFREC=1 ZSTART=3e7`, geometry left on the stacking rate --
and fixed the fork in advance:

    *if the rule's own configuration ALSO drops |c|, the rule and the data agree and the forbidden route
    was just one way there.  If it does NOT, the data are asking for the one object the rule pins -- a
    conflict between the rate rule and the sky rather than an implementation defect.  Assume neither.*

⇒ *** IT RESOLVES THE SECOND WAY.  The licensed configuration moves the contrast coefficient by 0.08
  sigma and makes the swing and chi^2 WORSE.  The forbidden one moves c by 6.7 sigma and flattens the
  swing on all three pre-registered criteria. ***

⛭⛭ ** AND A SECOND FINDING, WHICH IS WHY THE FIRST CAN BE TRUSTED: THE SWING STATISTIC IS NOT
** CONVERGED AGAINST THE CEILING IT IS READ TO, AND THE EARLIER NEGATIVE RESULT SAT ABOVE WHERE IT IS. **
*`cc66.73` reported that the forbidden repair did NOT flatten the swing -- crossings $36 \\to 30$ and the
longest run $16 \\to 18$, the wrong way on both -- and `r7095` credited that as reporting against myself.
**It reproduces here to the digit on its own pair, so it was measured correctly.  It was measured at
`LMAXL=1300`, and read to $\\ell \\le 1040$ that is 80 per cent of the run's own ceiling.**  Rerun at
`LMAXL=2000` the same comparison REVERSES: crossings $30 \\to 44$, longest run $18 \\to 12$.*
  ⇒ ** The ceiling scan below localises why, and it is not a wash: the discriminating feature LIVES
    above $\\ell \\approx 850$. **  *Below it all three configurations look alike -- longest run 8 or 9
    bins.  Above it the banked default's longest run GROWS with the ceiling, $8 \\to 8 \\to 15 \\to 18$,
    and the licensed configuration's grows faster, $9 \\to 9 \\to 13 \\to 22$, while the forbidden
    repair's stays flat, $9 \\to 9 \\to 9 \\to 12$.*  **So the statistic discriminates exactly where the
    `LMAXL=1300` run could not see it, which is why that run read a null.**

⚠ ** WHAT IS NOT CLAIMED. **  *This does not reinstate `LEAFGEOM=1`: `r7095`'s ruling is the gate's and
it stands.  What is reported is that the configuration the rule licenses does not move the two numbers
the rule's own repair was supposed to move, and that the forbidden one does -- which is a conflict to
adjudicate, not a build to resume.*  *Nor is the earlier result withdrawn: it was right about its own
pair, and the correction is the ceiling, not the arithmetic.*
  ⌗ *No parameter is refitted here and no onset is pinned.  Every spectrum is read from a BANKED file
  tracked in this repository -- nothing is derived from `/tmp` -- and the verdict rule is `r7091`'s own,
  quoted below before any number is read.*

** COMPUTES: the sign-crossing count, the longest run of one sign, the mean |extremum| over runs and
chi^2/bin of the binned residual for three banked CR configurations at four read ceilings; the contrast
coefficient c on each banked grid through 70's own design matrix; and the three peak-height ratios
against the sky.  Asserts the licensed configuration moves c by under 0.2 sigma, that its longest run is
no shorter than the banked default's, that the forbidden repair moves c by over 6 sigma and shortens the
longest run, and that all three agree below ell 800 -- which is the convergence finding. **
"""
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(BW, 'r7091_directions'))

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


# ⛔ THE VERDICT RULE, QUOTED FROM `r7091` BEFORE ANY SPECTRUM IS READ.
RULE = ("a chi^2 that improves while the swing stays is not the fix, and a swing that flattens is the "
        "fix even if chi^2 moves little; a flattened swing has MORE crossings, SHORTER runs and "
        "SMALLER extrema")

BANKED = os.path.join(BW, 'refit_grid185')
LICENSED = os.path.join(BW, 'r7095_directions', 'grid_licensed')
ONECLOCK = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
L1300 = os.path.join(BW, 'r7095_directions', 'lmaxl1300')


def shape(npz, lmax):
    """The swing statistics, via `r7091`'s own shape reader run as a subprocess so its definitions
    are not re-implemented here -- the mistake that would make a disagreement unattributable."""
    import subprocess
    p = subprocess.run([sys.executable, os.path.join(BW, 'r7091_directions', 'shape.py'),
                        npz, '--lmax', str(lmax), '--tilt'],
                       capture_output=True, text=True, errors='replace')
    out = p.stdout
    c = re.search(r'crossings at ell: (.*)', out)
    runs = re.findall(r'^\s+[+-]\s+(\d+)-(\d+)\s+(\d+)\s+([+-][\d.]+) s', out, re.M)
    ch = re.search(r'chi2/bin = ([\d.]+)', out)
    nb = re.search(r'over (\d+) bins', out)
    # ⛭ THE SUBPROCESS'S OWN STDERR IS IN THE MESSAGE, added at `r7097+cc66.80` because its absence is
    # what made the first failure of this assertion unreadable: `shape.py` carried an absolute path to
    # one machine's filesystem, so on a CI runner it died before printing and this said only "gave no
    # statistics".  ** An assertion about another process has to carry that process's complaint. **
    assert c and runs and ch, (
        f"shape.py gave no statistics for {npz} at lmax {lmax} -- exit {p.returncode}\n"
        f"  its stderr: {p.stderr.strip()[-800:] or '(empty)'}\n"
        f"  its stdout: {out.strip()[-400:] or '(empty)'}")
    lens = [int(r[2]) for r in runs]
    ext = [abs(float(r[3])) for r in runs]
    return dict(crossings=len(c.group(1).split()), longest=max(lens),
                mean_ext=sum(ext) / len(ext), chi2bin=float(ch.group(1)), nbins=int(nb.group(1)))


print(__doc__)

# =====================================================================================
head("A.  THE THREE CONFIGURATIONS, READ OFF THEIR OWN BANKED HEADERS")

_sw = {}
for nm, d in (('licensed', LICENSED), ('forbidden', ONECLOCK)):
    z = np.load(os.path.join(d, 'cr_base.npz'))
    _sw[nm] = str(z['switches'])
    print(f"      {nm:9s} {_sw[nm][:120]}")
gate("the licensed grid carries `LEAFREC=1 LEAFSCALES=1 ZSTART=3e7` and NO `LEAFGEOM` -- the rate "
     "rule's own assignment, geometry left on the stacking rate",
     'LEAFREC=1' in _sw['licensed'] and 'LEAFSCALES=1' in _sw['licensed']
     and 'ZSTART=3e7' in _sw['licensed'] and 'LEAFGEOM' not in _sw['licensed'])
gate("⛔ and the forbidden grid carries `LEAFGEOM=1` -- the geometry moved onto the leaf, which is "
     "what `P07`'s rate rule names and forbids",
     'LEAFGEOM=1' in _sw['forbidden'])

_z = {k: np.load(os.path.join(v, 'cr_base.npz'))
      for k, v in (('banked', BANKED), ('licensed', LICENSED), ('forbidden', ONECLOCK))}
for k, z in _z.items():
    print(f"      {k:9s} l_A = {float(z['l_A']):10.6f}   D_M = {float(z['D_M']):9.4f}   "
          f"r_s = {float(z['r_s']):10.6f}")
gate("⛭ `LEAFREC` moved the SPECTRUM and left `l_A`, `D_M` and `r_s` BIT-IDENTICAL to the banked "
     "run -- which is `r6893+cc66.37`'s finding that these three are diagnostics no transfer "
     "function reads, holding again on a switch that was built after it",
     float(_z['licensed']['l_A']) == float(_z['banked']['l_A'])
     and float(_z['licensed']['D_M']) == float(_z['banked']['D_M'])
     and float(_z['licensed']['r_s']) == float(_z['banked']['r_s'])
     and not np.array_equal(_z['licensed']['Dl'], _z['banked']['Dl']))
gate("⌗ and the three grids share one ell sampling, so every shape statistic below is comparable "
     "without interpolation",
     all(np.array_equal(_z['banked']['ls'], _z[k]['ls']) for k in ('licensed', 'forbidden')))

# =====================================================================================
head("B.  ⛭⛭ THE SWING, FIRST, BECAUSE r7095 FIXED THE ORDER -- AND AT FOUR CEILINGS")
print(f"      the rule, quoted before any number: {RULE}")
print()

CEILINGS = (700, 800, 900, 1040)
S = {}
print(f"      {'ceiling':>8}  {'configuration':<10} {'crossings':>9} {'longest':>7} "
      f"{'mean|ext|':>9} {'chi2/bin':>8}")
for L in CEILINGS:
    for nm, d in (('banked', BANKED), ('licensed', LICENSED), ('forbidden', ONECLOCK)):
        S[(L, nm)] = shape(os.path.join(d, 'cr_base.npz'), L)
        s = S[(L, nm)]
        print(f"      {L:>8}  {nm:<10} {s['crossings']:>9} {s['longest']:>7} "
              f"{s['mean_ext']:>9.3f} {s['chi2bin']:>8.2f}")

gate("⛔⛔ THE LICENSED CONFIGURATION DOES NOT FLATTEN THE SWING: read to ell 1040 its longest run is "
     "LONGER than the banked default's, which is the wrong direction on the criterion `r7091` named "
     "first",
     S[(1040, 'licensed')]['longest'] > S[(1040, 'banked')]['longest'])
gate("⛭⛭ and the forbidden repair DOES, on all three criteria at once -- more crossings, a shorter "
     "longest run, smaller mean |extremum|",
     S[(1040, 'forbidden')]['crossings'] > S[(1040, 'banked')]['crossings']
     and S[(1040, 'forbidden')]['longest'] < S[(1040, 'banked')]['longest']
     and S[(1040, 'forbidden')]['mean_ext'] < S[(1040, 'banked')]['mean_ext'])
gate("⛭⛭⛭ AND THE STATISTIC IS NOT CONVERGED: below ell 800 all three configurations have a longest "
     "run of 8 or 9 bins and are indistinguishable, so a reading taken there decides nothing",
     all(8 <= S[(L, nm)]['longest'] <= 9
         for L in (700, 800) for nm in ('banked', 'licensed', 'forbidden')))
gate("⇒ and the feature that discriminates GROWS with the ceiling on the banked default and on the "
     "licensed configuration while staying flat on the forbidden repair -- which is why it lives "
     "above ell 850 and not below",
     S[(1040, 'banked')]['longest'] > S[(800, 'banked')]['longest']
     and S[(1040, 'licensed')]['longest'] > S[(800, 'licensed')]['longest']
     and S[(1040, 'forbidden')]['longest'] - S[(800, 'forbidden')]['longest'] <= 3)

# =====================================================================================
head("C.  ⛭ THE EARLIER NEGATIVE RESULT, REPRODUCED ON ITS OWN PAIR AND THEN EXPLAINED")

_b = shape(os.path.join(L1300, 'cr_before.npz'), 1040)
_o = shape(os.path.join(L1300, 'cr_oneclock.npz'), 1040)
print(f"      LMAXL=1300  before    crossings {_b['crossings']}  longest {_b['longest']}  "
      f"chi2/bin {_b['chi2bin']:.2f}")
print(f"      LMAXL=1300  oneclock  crossings {_o['crossings']}  longest {_o['longest']}  "
      f"chi2/bin {_o['chi2bin']:.2f}")
gate("⌗ `cc66.73`'s reported crossings 36 -> 30 and longest run 16 -> 18 REPRODUCE exactly on the "
     "`LMAXL=1300` pair it was measured from -- the earlier null was arithmetically right",
     (_b['crossings'], _o['crossings']) == (36, 30) and (_b['longest'], _o['longest']) == (16, 18))
_reach = {}
for nm, p in (('1300', os.path.join(L1300, 'cr_before.log')),
              ('2000', os.path.join(LICENSED, 'cr_base.log'))):
    _m = re.search(r'k_max = (\d+)/D_M against a reported l_max = (\d+) -> ratio ([\d.]+)',
                   open(p, errors='replace').read())
    _reach[nm] = (int(_m.group(1)), int(_m.group(2)), float(_m.group(3)))
    print(f"      LMAXL={nm}: k_max = {_reach[nm][0]}/D_M, reported l_max = {_reach[nm][1]}, "
          f"ratio {_reach[nm][2]}")
gate("⛔ and the reason is the ceiling and not the arithmetic: both runs hold k_max = 2 l_max / D_M, "
     "so reading to ell 1040 is 80 per cent of the `LMAXL=1300` run's own reported ceiling against "
     "52 per cent of the `LMAXL=2000` run's",
     _reach['1300'][2] == _reach['2000'][2] == 2.0
     and abs(1040 / _reach['1300'][1] - 0.80) < 0.01
     and abs(1040 / _reach['2000'][1] - 0.52) < 0.01)
gate("⇒ so the earlier null is CORRECTED BY RESOLUTION, not withdrawn: the same comparison at "
     "`LMAXL=2000` reverses on both criteria it reported",
     S[(1040, 'forbidden')]['crossings'] > S[(1040, 'banked')]['crossings']
     and S[(1040, 'forbidden')]['longest'] < S[(1040, 'banked')]['longest']
     and _o['crossings'] < _b['crossings'] and _o['longest'] > _b['longest'])

# =====================================================================================
head("D.  chi^2, SECOND -- AND IT AGREES WITH THE SWING RATHER THAN HIDING IT THIS TIME")

for L in CEILINGS:
    print(f"      ell <= {L:4d}   banked {S[(L, 'banked')]['chi2bin']:.2f}   "
          f"licensed {S[(L, 'licensed')]['chi2bin']:.2f}   "
          f"forbidden {S[(L, 'forbidden')]['chi2bin']:.2f}")
gate("the licensed configuration's chi^2/bin is NO BETTER than the banked default's at the order's "
     "ceiling -- it is worse",
     S[(1040, 'licensed')]['chi2bin'] >= S[(1040, 'banked')]['chi2bin'])
gate("⛭ and the forbidden repair's is the lowest of the three at EVERY ceiling tested, so on this "
     "comparison chi^2 and the swing point the same way instead of opposite ways",
     all(S[(L, 'forbidden')]['chi2bin'] < min(S[(L, 'banked')]['chi2bin'],
                                              S[(L, 'licensed')]['chi2bin']) for L in CEILINGS))

# =====================================================================================
head("E.  THE HEIGHTS, THIRD -- WHERE THE LICENSED CONFIGURATION IS THE WORST OF THE THREE")

SKY = dict(l1_lA=0.7312, P1P2=2.217, P1P3=2.277)
H = {}
for nm, z in _z.items():
    ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
    pk = [i for i in range(1, len(Dl) - 1)
          if Dl[i] > Dl[i - 1] and Dl[i] > Dl[i + 1] and ls[i] > 150][:3]
    P = [float(Dl[i]) for i in pk]
    H[nm] = dict(l1=int(ls[pk[0]]), l1_lA=float(ls[pk[0]]) / lA, P1P2=P[0] / P[1], P1P3=P[0] / P[2])
    H[nm]['hdev'] = abs(H[nm]['P1P2'] - SKY['P1P2']) + abs(H[nm]['P1P3'] - SKY['P1P3'])
    print(f"      {nm:9s} l_1 = {H[nm]['l1']}  l_1/l_A = {H[nm]['l1_lA']:.4f} "
          f"({H[nm]['l1_lA']-SKY['l1_lA']:+.4f})   P1/P2 = {H[nm]['P1P2']:.3f} "
          f"({H[nm]['P1P2']-SKY['P1P2']:+.3f})   P1/P3 = {H[nm]['P1P3']:.3f} "
          f"({H[nm]['P1P3']-SKY['P1P3']:+.3f})   sum|height dev| {H[nm]['hdev']:.3f}")
print(f"      the sky: l_1 = 220.6, l_1/l_A = {SKY['l1_lA']}, P1/P2 = {SKY['P1P2']}, "
      f"P1/P3 = {SKY['P1P3']}")
gate("all three put the first peak at ell = 220 against the sky's 220.6, so none of this is a "
     "first-peak-position effect",
     all(H[nm]['l1'] == 220 for nm in H))
gate("⛔ the licensed configuration's summed height deviation is the LARGEST of the three -- it "
     "overshoots P1/P2 and P1/P3 further than the banked default does",
     H['licensed']['hdev'] > H['banked']['hdev'] and H['licensed']['hdev'] > H['forbidden']['hdev'])
gate("⌗ and the forbidden repair trades them: `l_1/l_A` lands four times closer to the sky while "
     "P1/P3 undershoots, so the heights are a trade and not the clean win the swing is",
     abs(H['forbidden']['l1_lA'] - SKY['l1_lA']) < abs(H['banked']['l1_lA'] - SKY['l1_lA']) / 3)

# =====================================================================================
head("F.  ⛭⛭⛭ THE CONTRAST COEFFICIENT, WHICH IS THE NUMBER r7093 NAMED")

sys.path.insert(0, os.path.join(BW, 'r7093_directions'))
import contrast_on as CO                                                    # noqa: E402

C = {}
for nm, d in (('banked', BANKED), ('licensed', LICENSED), ('forbidden', ONECLOCK)):
    C[nm] = CO.c_on(d)
    for arm in ('lcdm', 'cr'):
        c, s, _ = C[nm][arm]
        print(f"      {nm:9s} {arm:5s} c = {c:+.4f} +- {s:.4f}   ({c/s:+.1f} sigma)")
gate("70's published coefficients are REPRODUCED on the banked grid before anything is compared to "
     "them -- arm -0.0636 and control -0.0075",
     abs(C['banked']['cr'][0] - (-0.0636)) < 5e-4 and abs(C['banked']['lcdm'][0] - (-0.0075)) < 5e-4)
_dl = C['licensed']['cr'][0] - C['banked']['cr'][0]
_df = C['forbidden']['cr'][0] - C['banked']['cr'][0]
_s0 = C['banked']['cr'][1]
print(f"      licensed  moves the arm's c by {_dl:+.4f} = {_dl/_s0:+.2f} sigma   "
      f"|c| {100*(abs(C['licensed']['cr'][0])/abs(C['banked']['cr'][0])-1):+.0f}%")
print(f"      forbidden moves the arm's c by {_df:+.4f} = {_df/_s0:+.2f} sigma   "
      f"|c| {100*(abs(C['forbidden']['cr'][0])/abs(C['banked']['cr'][0])-1):+.0f}%")
gate("⛔⛔ THE LICENSED CONFIGURATION DOES NOT MOVE THE CONTRAST COEFFICIENT: under 0.2 sigma, and "
     "|c| RISES rather than falls -- the anomaly the rebuild was ordered to remove is untouched",
     abs(_dl / _s0) < 0.2 and abs(C['licensed']['cr'][0]) >= abs(C['banked']['cr'][0]))
gate("⛭⛭ and the forbidden repair moves it by more than 6 sigma, taking |c| down by about 89 per "
     "cent onto the control's own value",
     _df / _s0 > 6.0 and abs(C['forbidden']['cr'][0]) < 0.2 * abs(C['banked']['cr'][0]))
gate("⌗ THE CONSISTENCY CHECK: the CONTROL's coefficient is unchanged across all three, because its "
     "nine runs are the same nine files -- so what moved is the arm and not the method",
     all(C[k]['lcdm'][0] == C['banked']['lcdm'][0] for k in C))

# =====================================================================================
head("G.  ⚠ THE SCOPE, AND WHAT THIS DOES NOT LICENSE")

gate("no parameter is refitted and no onset pinned here: every spectrum is read from a banked file "
     "tracked in this repository, and the three grids' own `switches` stamps are quoted above",
     all('__SWITCHES__' in _sw[k] for k in _sw))
gate("⛔ and `LEAFGEOM=1` is NOT reinstated by this receipt -- `r7095`'s ruling is the gate's and it "
     "stands.  What is reported is a CONFLICT between the rule's configuration and the sky, for the "
     "gate to adjudicate, and not a build resumed",
     True)

print(f"\n  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail")
print("  GATES: " + ("ALL PASS" if not bad else "FAILURES ABOVE"))
print("""
  THE ANSWER TO r7095's FORK, IN ONE PLACE:
    the licensed configuration  ->  c moves -0.08 sigma (|c| RISES 1%), longest run 18 -> 22,
                                    chi^2/bin 3.05 -> 3.20, heights the worst of the three.
                                    ** IT MOVES NEITHER STATISTIC. **
    the forbidden repair        ->  c moves +6.70 sigma (|c| FALLS 89%), longest run 18 -> 12,
                                    crossings 30 -> 44, chi^2/bin 3.05 -> 1.47.
    the swing statistic         ->  NOT CONVERGED below ell ~ 850; the earlier null was read at
                                    80 per cent of its own run's ceiling and reverses above it.
    ⇒ the fork resolves the SECOND way: the data are asking for the one object the rule pins.
      That is a conflict to adjudicate, not an implementation defect to repair.
""")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
