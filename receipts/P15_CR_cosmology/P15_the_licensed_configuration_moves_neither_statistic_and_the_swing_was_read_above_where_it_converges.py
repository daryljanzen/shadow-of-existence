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
import glob                  # r7655: composing the arm-of-record grids from two banked sources
import hashlib               # r7655: the control is the same nine files, asserted rather than assumed
import os
import re
import subprocess
import sys
import tempfile

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
# ⛭⛭ r7099 Q1: THE TWO RUN LOGS ARE NOW TRACKED, so this reads them DIRECTLY again.
# *`cc66.81` had transcribed their `projection reach:` lines into a `.txt` because `.gitignore` excluded
# `*.log` -- a rule that lives in the file's **LaTeX build-output** section and was never meant for a
# solver log.  `r7099` ordered the logs committed instead, which is better: **the instrument's own output
# is the evidence, and a transcription is a second place for one fact to drift.**  The `.txt` is removed
# and the exception is declared in `.gitignore` rather than force-added, so the next reader can see it.*
#   ⌗ *The tracking gate in section G covers these two paths, so if the ignore rule ever reclaims them
#   this receipt fails here instead of only on someone else's tree -- which is the whole lesson of
#   `cc66.80` and `cc66.81`.*
_reach = {}
for nm, p in (('1300', os.path.join(L1300, 'cr_before.log')),
              ('2000', os.path.join(LICENSED, 'cr_base.log'))):
    _m = re.search(r'k_max = (\d+)/D_M against a reported l_max = (\d+) -> ratio ([\d.]+)',
                   open(p, errors='replace').read())
    assert _m, f"the instrument's own reach line is not in {p}"
    _reach[nm] = (int(_m.group(1)), int(_m.group(2)), float(_m.group(3)))
    print(f"      LMAXL={nm}: k_max = {_reach[nm][0]}/D_M, reported l_max = {_reach[nm][1]}, "
          f"ratio {_reach[nm][2]}   [read from the run's own tracked log]")
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

# ⛭⛭ THIS GATE NOW CHECKS WHAT IT CLAIMS.  *It used to assert that every input was tracked in the
# repository without asking git, and that claim was FALSE for two `.log` files while the gate passed --
# `.gitignore` excludes `*.log`.  **A scope claim about provenance that does not consult the thing that
# decides provenance is the defect this corpus keeps finding, and it was in my own scope section.***
_INPUTS = [os.path.join(g, f'{a}_base.npz')
           for g in (BANKED, LICENSED, ONECLOCK) for a in ('lcdm', 'cr')] + [
    os.path.join(L1300, 'cr_before.npz'), os.path.join(L1300, 'cr_oneclock.npz'),
    os.path.join(L1300, 'cr_before.log'), os.path.join(LICENSED, 'cr_base.log')]
# ⌗ *And it degrades honestly rather than brittlely: inside a git checkout it asks about TRACKING,
# which is the question that matters and the one that would have caught the `.log` files.  Unpacked
# outside a checkout there is no tracking to ask about, so it falls back to EXISTENCE and SAYS which
# question it answered -- a gate that cannot run should report that, not fail or pretend.*
_isrepo = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip() == 'true'
if _isrepo:
    _t = subprocess.run(['git', 'ls-files', '--error-unmatch'] + _INPUTS,
                        cwd=ROOT, capture_output=True, text=True)
    _missing = [os.path.relpath(p, ROOT) for p in _INPUTS
                if os.path.relpath(p, ROOT) not in _t.stdout.split('\n')]
    print(f"      provenance asked of `git ls-files`: {len(_INPUTS)} input(s), "
          f"{len(_missing)} not tracked{'  ' + str(_missing) if _missing else ''}")
    gate("⛭ EVERY FILE THIS RECEIPT READS IS TRACKED IN THE REPOSITORY, asked of `git ls-files` "
         "rather than asserted -- so it cannot pass here on a file absent from CI's checkout",
         _t.returncode == 0 and not _missing)
else:
    print("      ⌗ not inside a git checkout, so TRACKING cannot be asked; existence checked instead")
    gate("⌗ every file this receipt reads is present (tracking not askable outside a checkout, and "
         "that is reported rather than passed over)",
         all(os.path.exists(p) for p in _INPUTS))
gate("no parameter is refitted and no onset pinned here, and the three grids' own `switches` stamps "
     "are quoted above",
     all('__SWITCHES__' in _sw[k] for k in _sw))
gate("⛔ and `LEAFGEOM=1` is NOT reinstated by this receipt -- `r7095`'s ruling is the gate's and it "
     "stands.  What is reported is a CONFLICT between the rule's configuration and the sky, for the "
     "gate to adjudicate, and not a build resumed",
     True)

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("H.  ⛭⛭⛭ r7655 (cc66), ORDERED BY 69 ITEMS 2 AND 3 -- THE SAME TWO ROUTES ON THE ARM OF "
     "RECORD, AND THE 'TWO ROUTES DISAGREE' REPORT WITHDRAWN")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
#
# ⛔ ** THIS SEAT REPORTED A ROUTE DISAGREEMENT AT r7653 AND THERE IS NONE.  THE WITHDRAWAL COMES
#   FIRST. **  `MEASURED_item4.md` routed to 69: *"the audit's contrast coefficients differ from
#   l.1941-1946's ... the two routes may simply differ"*, naming the audit's `-0.0670 +- 0.0086` and
#   `-0.0092 +- 0.0085` against the paper's `-0.0642` and `-0.0069 +- 0.0083`.  ** Run THIS receipt's
#   own route -- `contrast_on.c_on`, the one the paragraph cites -- on the ARM-OF-RECORD grid and it
#   returns the audit's two numbers to four decimals. **  ⇒ *The routes never differed.  The paper's
#   pair is the NAMESAKE grid's and the audit's pair is the ARM OF RECORD's, through the same
#   design matrix, and I compared two grids while calling it a comparison of two methods.*
#
# ⛭ ** AND THE ARM-OF-RECORD GRIDS CARRY NO CONTROL, SO THE CONTROL IS COMPOSED EXPLICITLY RATHER
#   THAN SILENTLY. **  Each `*_leafrec1` grid holds its nine `cr_*.npz` and no `lcdm_*`; `c_on` needs
#   both arms because the coefficient is a CONTRAST.  The control's nine files are byte-identical
#   across all three namesake grids (`H①` asserts it), and the arm of record refits the CR
#   parameters and leaves the control untouched -- so the control is linked in from `refit_grid185`
#   and the composition is stated here, in the file, instead of being a property of one scratch
#   directory nobody can see.
_AO_SETS = [('banked', 'refit_grid185_leafrec1'),
            ('licensed', os.path.join('r7095_directions', 'grid_licensed_leafrec1')),
            ('forbidden', os.path.join('r7093_directions', 'grid_oneclock_leafrec1'))]
_NS_DIRS = {'banked': BANKED, 'licensed': LICENSED, 'forbidden': ONECLOCK}
_ctl_md5 = {nm: hashlib.md5(open(os.path.join(d, 'lcdm_base.npz'), 'rb').read()).hexdigest()
            for nm, d in _NS_DIRS.items()}
print(f"    the control's base, md5 on each namesake grid: "
      f"{', '.join(f'{k} {v[:8]}' for k, v in _ctl_md5.items())}")
gate("H① the control's nine runs ARE the same nine files on all three namesake grids, which is what "
     "licenses linking them beside the arm-of-record `cr_*` to form a like-for-like contrast",
     bool(len(set(_ctl_md5.values())) == 1))

_tmp = tempfile.mkdtemp(prefix='r7655_aor_')
_AO_DIRS = {}
for _nm, _rel in _AO_SETS:
    _d = os.path.join(_tmp, _nm)
    os.makedirs(_d)
    for _f in glob.glob(os.path.join(BW, _rel, 'cr_*.npz')):
        os.symlink(_f, os.path.join(_d, os.path.basename(_f)))
    for _f in glob.glob(os.path.join(BANKED, 'lcdm_*.npz')):
        os.symlink(_f, os.path.join(_d, os.path.basename(_f)))
    _AO_DIRS[_nm] = _d

# ── ITEM 3: the coefficient, this route, both arms ──────────────────────────────────────────────
_AUDIT = {'licensed': (-0.0670, 0.0086), 'forbidden': (-0.0092, 0.0085)}
_CAO, _CAO_CTL = {}, {}      # the arm's and the CONTROL's coefficient, kept apart (r7657: I⑥)
print(f"\n    the contrast coefficient through THIS receipt's own `c_on`, both arms:")
for _nm, _d in _AO_DIRS.items():
    _o = CO.c_on(_d)
    _cc, _sc, _ = _o['cr']
    _cl, _sl, _ = _o['lcdm']
    _CAO[_nm] = (_cc, _sc)
    _CAO_CTL[_nm] = (_cl, _sl)
    print(f"      {_nm:9s} ARM OF RECORD  cr c = {_cc:+.4f} +- {_sc:.4f} ({_cc/_sc:+.1f} sigma)"
          f"   control {_cl:+.4f} +- {_sl:.4f}")
gate("⛭⛭⛭ ** H② ITEM 3 ANSWERED, AND IT WITHDRAWS THIS SEAT'S OWN REPORT: THE PARAGRAPH'S RECEIPT "
     "REPRODUCES THE AUDIT'S COEFFICIENTS ON THE ARM OF RECORD TO FOUR DECIMALS, SO THERE IS NO "
     "SECOND ROUTE. **  *l.1941's `-0.0642` and l.1944's `-0.0069 +- 0.0083` are the NAMESAKE "
     "grid's through this design matrix; the audit's `-0.0670 +- 0.0086` and `-0.0092 +- 0.0085` "
     "are the SAME design matrix on the ARM-OF-RECORD grid.  One statistic, two grids.*",
     bool(abs(_CAO['licensed'][0] - _AUDIT['licensed'][0]) < 1e-4
          and abs(_CAO['licensed'][1] - _AUDIT['licensed'][1]) < 1e-4
          and abs(_CAO['forbidden'][0] - _AUDIT['forbidden'][0]) < 1e-4
          and abs(_CAO['forbidden'][1] - _AUDIT['forbidden'][1]) < 1e-4))
_mv = (_CAO['forbidden'][0] - _CAO['licensed'][0]) / _CAO['licensed'][1]
_fall = 100.0 * (abs(_CAO['forbidden'][0]) / abs(_CAO['licensed'][0]) - 1.0)
print(f"      and the forbidden route moves c by {_mv:+.2f} of the licensed error, "
      f"|c| {_fall:+.0f} per cent  (the paper says 6.7 errors and -89 per cent on the namesake)")
gate("⛭⛭ H③ and the paragraph's two CLAIMS survive the move: the forbidden route still moves the "
     "coefficient by more than six errors and still takes |c| down by about nine tenths, so only "
     "the digits are the namesake's",
     bool(_mv > 6.0 and -92.0 < _fall < -82.0))

# ── ITEM 2: the four-ceiling run lengths, this reader, both arms ─────────────────────────────────
_PUB_SEQ = {'banked': [8, 8, 15, 18], 'licensed': [9, 9, 13, 22], 'forbidden': [9, 9, 9, 12]}
_SEQ_NS, _SEQ_AO = {}, {}
# ⛭ r7657: the WHOLE shape dict is kept per (ceiling, configuration), not just `longest`.  Item 1
#   needs the crossings and the chi^2 per bin from the same subprocess calls, and re-running
#   `shape.py` for each column would be twelve more subprocesses for numbers already measured.
_SH_AO = {}
print(f"\n    the longest run of one sign at this receipt's own four ceilings {CEILINGS}:")
for _nm in ('banked', 'licensed', 'forbidden'):
    for _L in CEILINGS:
        _SH_AO[(_L, _nm)] = shape(os.path.join(_AO_DIRS[_nm], 'cr_base.npz'), _L)
    _SEQ_NS[_nm] = [S[(L, _nm)]['longest'] for L in CEILINGS]
    _SEQ_AO[_nm] = [_SH_AO[(L, _nm)]['longest'] for L in CEILINGS]
    print(f"      {_nm:9s} namesake {str(_SEQ_NS[_nm]):18s} "
          f"ARM OF RECORD {str(_SEQ_AO[_nm]):18s}")
gate("H④ the namesake sequences are this receipt's own published ones, which calibrates the reader "
     "before the arm of record is read with it",
     bool(all(_SEQ_NS[k] == _PUB_SEQ[k] for k in _PUB_SEQ)))
gate("⛭⛭⛭ ** H⑤ ITEM 2 ANSWERED: l.1952-1954's `9, 9, 13, 22` AND `9, 9, 9, 12` ARE THIS RECEIPT'S, "
     "AT CEILINGS 700/800/900/1040 ON THE NAMESAKE GRID, AND THEY ARE NOT THE AUDIT'S STATISTIC AT "
     "ALL. **  *The audit's `longest` column -- specified 4, 5, 11, 20, 23, 23, 27, 33 and forbidden "
     "4, 4, 4, 5, 7, 8, 8, 8 -- is a different reader at eight different ceilings (850..1996), so "
     "the two were never comparable and the sentence should NOT be re-pointed onto the audit.  What "
     "is wrong is the CITATION: the sentence sits in a passage closed by the three-grid receipt, "
     "which gates none of it, while the receipt that computes all four numbers closes the paragraph "
     "eleven lines above.*",
     bool(_SEQ_NS['licensed'] == [9, 9, 13, 22] and _SEQ_NS['forbidden'] == [9, 9, 9, 12]))
_gap_ns = _SEQ_NS['licensed'][-1] - _SEQ_NS['forbidden'][-1]
_gap_ao = _SEQ_AO['licensed'][-1] - _SEQ_AO['forbidden'][-1]
print(f"      the discriminating gap at the top ceiling: namesake {_SEQ_NS['licensed'][-1]} vs "
      f"{_SEQ_NS['forbidden'][-1]} = {_gap_ns};  arm of record {_SEQ_AO['licensed'][-1]} vs "
      f"{_SEQ_AO['forbidden'][-1]} = {_gap_ao}")
gate("⛔⛭⛭ ** H⑥ AND ON THE ARM OF RECORD THE DISCRIMINATING FEATURE IS WEAKER, WHICH IS THE PART "
     "WORTH ROUTING RATHER THAN THE DIGITS. **  *The specified configuration's run reaches 16 "
     "instead of 22 while the forbidden one's still reaches 12, so the gap the sentence turns on "
     "falls from ten bins to four.  The DIRECTION survives -- specified grows, forbidden stays -- "
     "and `every one of them with a longest run of eight or nine bins` below the ceiling becomes "
     "SEVEN to nine, because the forbidden arm reads 7 at 700.*",
     bool(_gap_ao < _gap_ns and _gap_ao > 0 and min(min(v[:2]) for v in _SEQ_AO.values()) == 7))

# ── and why two of the three arm-of-record rows agree exactly ────────────────────────────────────
_zb = np.load(os.path.join(BW, 'refit_grid185_leafrec1', 'cr_base.npz'), allow_pickle=True)
_zl = np.load(os.path.join(BW, 'r7095_directions', 'grid_licensed_leafrec1', 'cr_base.npz'),
              allow_pickle=True)
_same = all(np.array_equal(_zb[k], _zl[k]) for k in ('Dl', 'ls', 'l_A', 'D_M', 'r_s'))
_md5_differ = (hashlib.md5(open(os.path.join(BW, 'refit_grid185_leafrec1',
                                             'cr_base.npz'), 'rb').read()).hexdigest()
               != hashlib.md5(open(os.path.join(BW, 'r7095_directions', 'grid_licensed_leafrec1',
                                                'cr_base.npz'), 'rb').read()).hexdigest())
print(f"\n    the banked and licensed arm-of-record grids: spectra bit-identical {_same}, "
      f"files differ {_md5_differ}")
gate("⛭ H⑦ the banked and licensed rows agree on the arm of record because their SPECTRA ARE "
     "BIT-IDENTICAL -- `Dl`, `ls`, `l_A`, `D_M` and `r_s` all equal -- while the FILES differ, in a "
     "`manifest` key alone.  *Stated because the md5 difference invites the opposite conclusion: "
     "two files, one spectrum, so the agreement is identity and not coincidence.*",
     bool(_same and _md5_differ))

# =====================================================================================
head("I.  ⛭⛭⛭ r7657 (cc66), ORDERED BY 69 ITEM 1 -- l.1938-1955 WHOLE ON THE ARM OF RECORD, "
     "IN ONE TABLE, WITH THE PARAGRAPH'S OWN FIGURES READ OUT OF THE PAPER BESIDE THEM")
# =====================================================================================
#
# ⌗ ** TWO OF 69's FIGURES ARE ELIDED FROM THE QUOTE BELOW AND FROM I④'s LABEL, and a GATE is
#   the reason: `check_marker_transposition` reads a receipt's own source for a paper figure's
#   digits and treats the receipt as CARRYING that number, so printing another site's figure in
#   PROSE makes this file a FALSE CARRIER for it.  That is exactly what happened at r7657: the
#   gate flagged l.1997's restatement of the namesake grid's acoustic scale as transposed away
#   from the optical-depth group that closes it, because THIS file's prose had started quoting
#   those digits -- and naming them AGAIN in this very comment would re-make the flag, so the
#   number is not written here either.  Its own `unquoted()` drops
#   lines carrying `$` or `TEX` for this reason, and a plain `#` comment is not dropped. **
#   ⇒ *So this file prints the figures it COMPUTES and reads the paper's out of the paper.
#   Nothing is hidden: the elision is marked here, and both figures are in I④'s own read.*
# ⛭ ** 69's ITEM 1, verbatim: "Give the rest of the paragraph on the same arm in one table:
#   `rising one per cent`, the longest run 18 -> 22 and 18 -> 12, chi^2 per bin 3.05, 3.20 and 1.47,
#   the sign changes 30 -> 44, ell_A <the namesake pair's own two figures, ELIDED here and read
#   out of l.1946 by I④ instead> against 301.375, and `indistinguishable below ell ~= 800`.  I land it whole, with the `\rcpt` you recommend on the run-length sentence.
#   On your figures the gap the sentence turns on falls from ten bins to four, so say whether
#   `separate only above it` still holds, or how it should read." **
#
# ⛔⛭⛭⛭ ** AND THE FIRST HALF OF THE PARAGRAPH HAS NO ARM-OF-RECORD COUNTERPART AT ALL, which
#   is the finding and not a gap in the table.  ON THE ARM OF RECORD THE BANKED GRID ALREADY
#   CARRIES `LEAFREC=1 LEAFSCALES=1` AND NO `LEAFGEOM` -- it IS the configuration the rate rule
#   specifies. **  The two grids' switches are printed below and are the same string; `H⑦` already
#   showed their spectra bit-identical.  ⇒ *So `the configuration the rate rule specifies moves
#   neither statistic` is EXACTLY true there, to the bit, and its four figures -- `0.08` of an
#   error, `rising` one per cent to `-0.0642`, `18` to `22`, `3.05` to `3.20` -- are the NAMESAKE
#   pair's and cannot be re-pointed onto this arm.  There is nothing to move, because the
#   re-point MADE the licensed configuration the baseline.*
_TOP = CEILINGS[-1]
_WORDNUM = {'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
_P15T = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                 encoding='utf-8', errors='replace').read())
_PP = {}


# ⛭⛭ r7661 (69's order, from 60's general point at r7660): A READER THAT MAY LEGITIMATELY FIND
#   NOTHING WANTS ITS TWO CASES SEPARATED.  One `None` serving both *the sentence is gone* and *the
#   pattern no longer sees it* is what let three of these seven reads go blind behind a green gate
#   between `r7657` and `r7661`: each `None` short-circuits its conjunction, so the gate passed
#   WITHOUT its paper-side check and nothing in the output invited a second look.
#   ⇒ `WITHDRAWN` is now a DECLARED list carrying its reason, and every other key MUST match.
#   `I⑧` is the gate that says so, which is what turns the next rewording into a red.
WITHDRAWN = {
    'coef, licensed': 'r7659 replaced the measured licensed null with `moves neither statistic by '
                      'construction`, so there is no licensed coefficient pair left to read -- '
                      'which is this receipt\'s own recommendation (1), taken',
    'shape, licensed': 'the same removal: the sentence no longer prints a licensed run or chi^2 pair',
}
_MISSED = []


def ppaper(key, pat, *cast):
    """read ONE of l.1938-1955's figures out of the .tex, and say WHICH KIND of absence it is."""
    m = re.search(pat, _P15T)
    _PP[key] = tuple(c(g) for c, g in zip(cast, m.groups())) if m else None
    if m:
        state = f"{_PP[key]}"
    elif key in WITHDRAWN:
        state = f"** WITHDRAWN, declared -- {WITHDRAWN[key]} **"
    else:
        state = "** NOT MATCHED -- not declared withdrawn, so this read has gone BLIND **"
        _MISSED.append(key)
    print(f"      {key:16s} {state}")
    return _PP[key]


print("    l.1938-1955's figures, each READ OUT OF corpus/CR_cosmology.tex:")
ppaper('coef, licensed', r'moves by \$([\d.]+)\$ of its own error, its magnitude \\emph\{rising\} '
                        r'one per cent to \$(-[\d.]+)\$', float, float)
ppaper('shape, licensed', r'the longest run of one sign goes from \$(\d+)\$ to \$(\d+)\$ bins, the '
                         r'wrong way; \$\\chi\^\{2\}\$ per bin goes from \$([\d.]+)\$ to '
                         r'\$([\d.]+)\$', int, int, float, float)
# ⛭ r7661: REPOINTED.  `the same coefficient ... to` became `the contrast coefficient ... from
#   ... to`, which adds the SPECIFIED pair the old pattern never read -- five groups, not three.
ppaper('coef, forbidden', r'by \$([\d.]+)\$ of its own error, from \$(-[\d.]+)\\pm([\d.]+)\$ '
                         r'to \$(-[\d.]+)\\pm([\d.]+)\$',
       float, float, float, float, float)
ppaper('the fall', r'its magnitude falling \$(\d+)\$ per cent onto the value the control itself '
                   r'returns', float)
# ⛭ r7661: REPOINTED.  `the longest run falls` became `the longest run OF ONE SIGN falls`, and
#   chi^2 per bin now prints BOTH ends -- six groups, not five.
ppaper('shape, forbidden', r'the sign changes rise from \$(\d+)\$ to \$(\d+)\$, the longest run '
                          r'of one sign falls from \$(\d+)\$ to \$(\d+)\$ and '
                          r'\$\\chi\^\{2\}\$ per bin falls from \$([\d.]+)\$ to \$([\d.]+)\$',
       int, int, int, int, float, float)
ppaper('the scale', r"\$\\ell_A\$ moves from \$([\d.]+)\$ to \$([\d.]+)\$ against the control's "
                    r"\$([\d.]+)\$", float, float, float)
ppaper('the ceiling', r"\\emph\{indistinguishable below \$\\ell\\simeq(\d+)\$\}---every one of them "
                      r"with a longest run of ([a-z]+) to ([a-z]+) bins---and separate only above "
                      # r7781 (69): P15 rewritten on one rate -- `the specified configuration` is now `the
                      #   radiation-free distance` and `the forbidden one` is `the one rate`; same figures
                      r"it, where the (?:specified configuration|radiation-free distance)'s run grows \$(\d+)\$, \$(\d+)\$, "
                      r"\$(\d+)\$, \$(\d+)\$ and the (?:forbidden one|one rate)'s stays \$(\d+)\$, \$(\d+)\$, "
                      r"\$(\d+)\$, \$(\d+)\$", int, str, str, int, int, int, int, int, int, int, int)

# -- the two tables, the arm of record first because that is what was ordered --------------------
_sw_ao = {}
print("\n    the arm-of-record grids' own switches, because the first half turns on them:")
for _nm, _rel in _AO_SETS:
    _zz = np.load(os.path.join(BW, _rel, 'cr_base.npz'), allow_pickle=True)
    _sw_ao[_nm] = re.sub(r'SAVE=\S+', 'SAVE=...', str(_zz['switches']))
    print(f"      {_nm:10s} {_sw_ao[_nm]}")


def _row(nm, cdict, shdict, lA, base):
    _c, _e = cdict[nm][:2]
    _b = cdict[base][0]
    _sh = shdict[nm]
    return (_c, _e, (_c - _b) / cdict[base][1], 100.0 * (abs(_c) / abs(_b) - 1.0),
            _sh['crossings'], _sh['longest'], _sh['chi2bin'], _sh['mean_ext'], lA)


_AO_C = {k: (v[0], v[1]) for k, v in _CAO.items()}
_NS_C = {k: (C[k]['cr'][0], C[k]['cr'][1]) for k in C}
_AO_LA = {k: float(np.load(os.path.join(_AO_DIRS[k], 'cr_base.npz'),
                           allow_pickle=True)['l_A']) for k in _AO_DIRS}
_NS_LA = {k: float(_z[k]['l_A']) for k in _z}
_LA_CTL = float(np.load(os.path.join(BANKED, 'lcdm_base.npz'), allow_pickle=True)['l_A'])
_AO = {k: _row(k, _AO_C, {n: _SH_AO[(_TOP, n)] for n in _AO_C}, _AO_LA[k], 'banked')
       for k in _AO_C}
_NS = {k: _row(k, _NS_C, {n: S[(_TOP, n)] for n in _NS_C}, _NS_LA[k], 'banked') for k in _NS_C}
_HDR = (f"      {'configuration':<11}{'c':>9}{'+-':>8}{'move/err':>10}{'|c| %':>8}{'cross':>7}"
        f"{'longest':>8}{'chi2/bin':>10}{'mean|ext|':>10}{'l_A':>11}")
for _ttl, _T in ((f"THE ARM OF RECORD, read to ell {_TOP}", _AO),
                 (f"the NAMESAKE pair at the same ceiling, which is what the paper prints", _NS)):
    print(f"\n    {_ttl}:")
    print(_HDR)
    for _nm in ('banked', 'licensed', 'forbidden'):
        _r = _T[_nm]
        print(f"      {_nm:<11}{_r[0]:+9.4f}{_r[1]:8.4f}{_r[2]:+10.2f}{_r[3]:+8.1f}{_r[4]:7d}"
              f"{_r[5]:8d}{_r[6]:10.2f}{_r[7]:10.3f}{_r[8]:11.3f}")
    print(f"      {'control':<11}{C['banked']['lcdm'][0]:+9.4f}{C['banked']['lcdm'][1]:8.4f}"
          f"{'':10}{'':8}{'':7}{'':8}{'':10}{'':10}{_LA_CTL:11.3f}")

gate("⛔⛭⛭⛭ ** I① THE PARAGRAPH'S FIRST HALF IS NAMESAKE-ONLY, BECAUSE THE RE-POINT MADE THE "
     "LICENSED CONFIGURATION THE BASELINE: the arm-of-record banked and licensed grids carry THE "
     "SAME SWITCHES, so c, the crossings, the longest run and chi^2 per bin are identical to the "
     "bit and `moves neither statistic` is exactly true. **  *l.1940-1942's four figures -- 0.08 "
     "of an error, |c| rising one per cent to -0.0642, the run 18 to 22, chi^2/bin 3.05 to 3.20 -- "
     "are the NAMESAKE pair's, where the banked grid has no `LEAFREC` and the licensed one does.  "
     "⇒ ** They cannot be re-pointed onto this arm: there is no second configuration to compare, "
     "and a table of zeroes would be a true table of the wrong comparison. ** *",
     bool(_sw_ao['banked'] == _sw_ao['licensed'] and 'LEAFGEOM' not in _sw_ao['banked']
          and 'LEAFREC=1' in _sw_ao['banked'] and 'LEAFSCALES=1' in _sw_ao['banked']
          and _AO_C['banked'] == _AO_C['licensed']
          and _SH_AO[(_TOP, 'banked')] == _SH_AO[(_TOP, 'licensed')]
          and abs(_AO['licensed'][3]) < 1e-9 and abs(_AO['licensed'][2]) < 1e-9
          # ⌗ `namesake-only` is a claim ABOUT THE PAPER, so the paper's own figure is READ and
          #   shown to match the namesake measurement and NOT this arm's.  Without this the label
          #   would attribute four figures to l.1940-1942 while depending on nothing read out of
          #   it -- which is what `check_unread_figure` caught here, and it was right.
          and (_PP['coef, licensed'] is None
               or (abs(_NS_C['licensed'][0] - _PP['coef, licensed'][1]) < 5e-5
                   and abs(_AO_C['licensed'][0] - _PP['coef, licensed'][1]) > 5e-4))
          and (_PP['shape, licensed'] is None
               or (_NS['licensed'][5] == _PP['shape, licensed'][1]
                   and _AO['licensed'][5] != _PP['shape, licensed'][1]
                   and abs(_NS['licensed'][6] - _PP['shape, licensed'][3]) < 5e-3
                   and abs(_AO['licensed'][6] - _PP['shape, licensed'][3]) > 5e-2))))
_pl, _ps = _PP['coef, licensed'], _PP['shape, licensed']
gate("⛭ I② and the reader is CALIBRATED on the paper's own first-half digits before the second "
     "half is read with it: the namesake pair returns 0.08 of an error, |c| rising 1 per cent to "
     "-0.0642, the run 18 to 22 and chi^2/bin 3.05 to 3.20, each read out of l.1940-1942 rather "
     "than typed here.  *A reader that cannot reproduce the figures the paragraph prints has no "
     "standing to report that the other half of it moved.*",
     bool((_pl is None or (abs(abs(_NS['licensed'][2]) - _pl[0]) < 5e-3
                           and abs(_NS_C['licensed'][0] - _pl[1]) < 5e-5))
          and (_ps is None or (_NS['banked'][5] == _ps[0] and _NS['licensed'][5] == _ps[1]
                               and abs(_NS['banked'][6] - _ps[2]) < 5e-3
                               and abs(_NS['licensed'][6] - _ps[3]) < 5e-3))
          and abs(_NS['licensed'][3] - 1.0) < 0.5))
_pf, _pfa, _pfs = _PP['coef, forbidden'], _PP['the fall'], _PP['shape, forbidden']
print(f"\n    the forbidden route's whole set, NAMESAKE then ARM OF RECORD:")
print(f"      c moves           {_NS['forbidden'][2]:+.2f} errors -> "
      f"{_AO['forbidden'][2]:+.2f} errors")
print(f"      |c| falls         {_NS['forbidden'][3]:+.1f} per cent -> "
      f"{_AO['forbidden'][3]:+.1f} per cent, onto the control's own "
      f"{C['banked']['lcdm'][0]:+.4f} "
      f"({abs(_AO_C['forbidden'][0] - C['banked']['lcdm'][0]) / C['banked']['lcdm'][1]:.1f} of an "
      f"error from it)")
print(f"      sign changes      {_NS['banked'][4]} -> {_NS['forbidden'][4]}   became   "
      f"{_AO['banked'][4]} -> {_AO['forbidden'][4]}")
print(f"      longest run       {_NS['banked'][5]} -> {_NS['forbidden'][5]}   became   "
      f"{_AO['banked'][5]} -> {_AO['forbidden'][5]}")
print(f"      chi^2 per bin     {_NS['banked'][6]:.2f} -> {_NS['forbidden'][6]:.2f}   became   "
      f"{_AO['banked'][6]:.2f} -> {_AO['forbidden'][6]:.2f}")
print(f"      mean |excursion|  {_NS['banked'][7]:.3f} -> {_NS['forbidden'][7]:.3f}   became   "
      f"{_AO['banked'][7]:.3f} -> {_AO['forbidden'][7]:.3f}")
gate("⛭⛭⛭ ** I③ ITEM 1's SECOND HALF, ON THE ARM OF RECORD: EVERY DIRECTION THE "
     "PRE-REGISTERED TEST NAMED HOLDS AND EVERY DIGIT MOVES. **  *c -0.0670 -> -0.0092, a move of "
     "6.7 of its error, |c| falling 86 per cent and landing 0.2 of an error from the control's "
     "own -0.0075; the sign changes 32 -> 38; the longest run 16 -> 12; chi^2 per bin 2.64 -> "
     "1.33; the mean excursion 1.327 -> 1.114.  ** More sign changes, shorter runs, smaller "
     "excursions and a lower chi^2 -- the four-part test fixed before either grid was read, met "
     "on all four. ** *  ⛭ r7661: this gate used to add `where the paper prints 30 -> 44` and its "
     "three companions, because the paragraph then carried the NAMESAKE pair.  It no longer does "
     "-- r7659 landed the re-point -- so the paper's digits and this receipt's are the same "
     "digits, and the read is now an AGREEMENT rather than a contrast.",
     # ⛭ r7659 (69): l.1938-1946 LANDED on the arm of record, so each paper read is held as a
     #   disjunction of the two states -- the namesake's printed figure or this arm's.
     # ⛭⛭ r7661: `coef, forbidden` and `shape, forbidden` are REPOINTED onto the landed wording,
     #   which reads the ARM's figures and the SPECIFIED end the old patterns never saw.  Both are
     #   now held across both states, as `the fall` and `the scale` already were -- and both reads
     #   FAILED on the namesake-only form the moment they came back, which is the blindness made
     #   visible: the gates had been passing on a `None`, not on an agreement.
     bool((_pf is None or any(abs(_X['forbidden'][2] - _pf[0]) < 5e-2
                              and abs(_XC['banked'][0] - _pf[1]) < 5e-5
                              and abs(_XC['banked'][1] - _pf[2]) < 5e-5
                              and abs(_XC['forbidden'][0] - _pf[3]) < 5e-5
                              and abs(_XC['forbidden'][1] - _pf[4]) < 5e-5
                              for _X, _XC in ((_NS, _NS_C), (_AO, _AO_C))))
          and (_pfa is None or any(abs(abs(_X['forbidden'][3]) - _pfa[0]) < 1.0 for _X in (_NS, _AO)))
          and (_pfs is None or any(_X['banked'][4] == _pfs[0] and _X['forbidden'][4] == _pfs[1]
                                   and _X['banked'][5] == _pfs[2] and _X['forbidden'][5] == _pfs[3]
                                   and abs(_X['banked'][6] - _pfs[4]) < 5e-3
                                   and abs(_X['forbidden'][6] - _pfs[5]) < 5e-3
                                   for _X in (_NS, _AO)))
          and _AO['forbidden'][2] > 6.0 and -88.0 < _AO['forbidden'][3] < -84.0
          and abs(_AO_C['forbidden'][0] - C['banked']['lcdm'][0]) < 0.3 * C['banked']['lcdm'][1]
          and _AO['forbidden'][4] > _AO['banked'][4] and _AO['forbidden'][5] < _AO['banked'][5]
          and _AO['forbidden'][6] < _AO['banked'][6]
          and _AO['forbidden'][7] < _AO['banked'][7]))
_pla = _PP['the scale']
print(f"\n    and the acoustic scale: {_AO['banked'][8]:.3f} -> {_AO['forbidden'][8]:.3f} against "
      f"the control's {_LA_CTL:.3f}   (the paper's namesake pair: {_NS['banked'][8]:.3f} -> "
      f"{_NS['forbidden'][8]:.3f} against the same {_LA_CTL:.3f})")
gate("⛭⛭ ** I④ AND THE SCALE FOLLOWS IT ON THIS ARM TOO, PAST THE CONTROL RATHER THAN ONTO IT: "
     "l_A moves 302.943 -> 301.400 against the control's 301.375, and since r7659 those are the "
     "paper's own three figures too -- READ out of l.1946 above and not repeated here. **  *The "
     "control's figure is UNMOVED because it is the "
     "same file on every grid, which is what makes this a statement about the arm.  ** The "
     "forbidden route overshoots: the namesake landed 0.005 above the control and this arm lands "
     "0.025 above it, five times as far, on a move twenty times that size. ** *",
     bool((_pla is None or (any(abs(_X['banked'][8] - _pla[0]) < 5e-4
                                and abs(_X['forbidden'][8] - _pla[1]) < 5e-4 for _X in (_NS, _AO))
                            and abs(_LA_CTL - _pla[2]) < 5e-4))
          and abs(_AO['banked'][8] - 302.943) < 5e-4
          and abs(_AO['forbidden'][8] - 301.400) < 5e-4
          and _AO['forbidden'][8] > _LA_CTL
          and _AO['banked'][8] - _AO['forbidden'][8] > 1.0))
_pc = _PP['the ceiling']
_GAPS_AO = [_SEQ_AO['licensed'][k] - _SEQ_AO['forbidden'][k] for k in range(len(CEILINGS))]
_GAPS_NS = [_SEQ_NS['licensed'][k] - _SEQ_NS['forbidden'][k] for k in range(len(CEILINGS))]
INDIST = 2          # bins; `indistinguishable` as this receipt already scores it below


def _state(seq, gaps):
    """(the ceiling the sentence can say they are indistinguishable BELOW, the run bounds there),
    DERIVED from one state's own gap profile rather than taken from the sentence: the last ceiling
    whose gap is still within `INDIST`, and the min and max longest run over every configuration
    at that ceiling and below.  ⛭ r7661: the paper's three figures are a reading of this triple,
    so the triple is what the read is checked against -- namesake (800, 8, 9), arm (900, 7, 9)."""
    k = -1
    for i, g in enumerate(gaps):
        if g > INDIST:
            break
        k = i
    if k < 0:
        return None
    win = [v[:k + 1] for v in seq.values()]
    return CEILINGS[k], min(min(w) for w in win), max(max(w) for w in win)


_ST_NS, _ST_AO = _state(_SEQ_NS, _GAPS_NS), _state(_SEQ_AO, _GAPS_AO)
print(f"      the ceiling each state can claim, derived from its own gaps (<= {INDIST} bins): "
      f"namesake {_ST_NS}, ARM OF RECORD {_ST_AO}")
print(f"\n    where the three SEPARATE, gap in the longest run at each ceiling {CEILINGS}:")
print(f"      namesake       specified {_SEQ_NS['licensed']}  forbidden {_SEQ_NS['forbidden']}"
      f"  gap {_GAPS_NS}")
print(f"      ARM OF RECORD  specified {_SEQ_AO['licensed']}  forbidden {_SEQ_AO['forbidden']}"
      f"  gap {_GAPS_AO}")
gate("⛭⛭⛭ ** I⑤ `separate only above it` STILL HOLDS AND THE CEILING MOVES UP: ON THE ARM OF "
     "RECORD THE THREE ARE INDISTINGUISHABLE BELOW ell ≃ 900, NOT 800. **  *At 700, 800 and 900 "
     "the specified configuration reads 9, 9, 9 and the forbidden one 7, 8, 8 -- gaps of two, one "
     "and one bin -- where the namesake pair had already opened to four bins at 900 (13 against "
     "9).  The separation appears only at the top ceiling, 16 against 12.  ⇒ ** So the sentence's "
     "STRUCTURE survives and two of its figures moved, and since r7659 the paragraph carries them: "
     "`indistinguishable below ell ≃ 900`, `a longest run of seven to nine bins`, and the gap it "
     "turns on falls from ten bins to four. ** *  ⛭ r7661: the ceiling and the two run bounds are "
     "DERIVED from each state's own gap profile rather than taken from the sentence -- namesake "
     "(800, 8, 9), arm of record (900, 7, 9) -- so the read is checked against a triple this "
     "receipt computes, and a wrong ceiling in the paper reddens here.",
     bool((_pc is None or any((_pc[0], _WORDNUM[_pc[1]], _WORDNUM[_pc[2]]) == _ST
                              and list(_pc[3:7]) == _S['licensed']
                              and list(_pc[7:11]) == _S['forbidden']
                              for _S, _ST in ((_SEQ_NS, _ST_NS), (_SEQ_AO, _ST_AO))))
          and max(_GAPS_AO[:3]) <= 2 and _GAPS_AO[3] == 4 and _GAPS_NS[3] == 10
          and _GAPS_NS[2] == 4
          and min(min(v[:3]) for v in _SEQ_AO.values()) == 7))
gate("⌗ I⑥ the control's coefficient is the SAME NUMBER on all six grids, and here that is an "
     "identity rather than a check: the arm-of-record sets carry no control of their own, so all "
     "three link the same nine `lcdm_*` files `H①` showed byte-identical across the namesake "
     "grids.  *Said plainly because `identical across all three grids` reads like a measurement, "
     "and on this arm it is a property of the composition -- the MEASUREMENT of it is the namesake "
     "row in F.*",
     bool(all(_CAO_CTL[k] == _CAO_CTL['banked'] for k in _CAO_CTL)
          and _CAO_CTL['banked'][0] == C['banked']['lcdm'][0]
          and all(C[k]['lcdm'][0] == C['banked']['lcdm'][0] for k in C)))
_still = [k for k in WITHDRAWN if _PP[k] is not None]
gate("⛭⛭⛭ ** I⑧ EVERY READ THAT IS NOT DECLARED WITHDRAWN MATCHED, AND EVERY ONE THAT IS "
     "DECLARED WITHDRAWN IS STILL ABSENT. **  *This is the gate `r7660` is owed and the one this "
     "receipt did not have: between `r7657` and `r7661` three of these seven reads stopped seeing "
     "figures the paper still printed -- `coef, forbidden`, `shape, forbidden` and `the ceiling` "
     "-- and because a missing read is tolerated by short-circuit, the three gates that consume "
     "them went on passing WITHOUT their paper-side check.  ** A guard that cannot fail on the "
     "data it is given is not a guard, and a green gate is the one thing that cannot tell you a "
     "check has stopped checking. **  ⇒ The tolerance stays, because a sentence may legitimately "
     "be withdrawn -- but it now costs a DECLARATION with a reason, and the undeclared case "
     "reddens.  ⌗ The second arm matters as much as the first: if a withdrawn sentence comes "
     "back, the declaration is false and this gate says so rather than letting the list rot.*",
     bool(not _MISSED and not _still
          # ⌗ and the three counts the INDEX row quotes are PINNED here, not merely printed, so a
          #   read added or withdrawn without restating the row reddens this receipt.
          and len(_PP) == 7 and len(WITHDRAWN) == 2
          and sum(v is not None for v in _PP.values()) == 5))
print(f"      reads {len(_PP)}, matched {sum(v is not None for v in _PP.values())}, "
      f"declared withdrawn {len(WITHDRAWN)}, blind {len(_MISSED)}"
      + (f" -- {_MISSED}" if _MISSED else "")
      + (f";  DECLARED WITHDRAWN BUT PRESENT: {_still}" if _still else ""))

# -- the INDEX row's own digits, pinned, because r7657 puts fourteen new ones in it ---------------
# ⌗ `check_figures_pinned`'s rule: a figure a citing sentence prints must FAIL its receipt when it
#   is wrong, and `pins()` only sees constants inside a comparison -- so a gate that MEASURES a
#   quantity does not pin the digits a row quotes it to.  The chain below is the pin; the tables
#   above print the measurements, so each literal lives in exactly one place.
_cf, _cc = _AO_C['forbidden'], _CAO_CTL['banked']
gate("⛭ I⑦ ** EVERY DIGIT r7657 PUTS IN THIS RECEIPT'S INDEX ROW IS A LITERAL TWIN HERE, so a "
     "stale row reddens the receipt instead of going quietly wrong. **  *The one-state rule cuts "
     "both ways: the row states what this receipt finds NOW, and this gate makes the row's own "
     "digits the receipt's responsibility.*",
     bool(abs(round(_AO_C['banked'][0], 4) - -0.0670) < 1e-9
          and abs(round(_AO_C['banked'][1], 4) - 0.0086) < 1e-9
          and abs(round(_cf[0], 4) - -0.0092) < 1e-9
          and abs(round(_cf[1], 4) - 0.0085) < 1e-9
          and abs(round(_AO['forbidden'][2], 2) - 6.71) < 1e-9
          and abs(round(_AO['forbidden'][3], 1) - -86.3) < 1e-9
          and abs(round(abs(_cf[0] - _cc[0]) / _cc[1], 1) - 0.2) < 1e-9
          and abs(round(_cc[0], 4) - -0.0075) < 1e-9
          and abs(round(_cc[1], 4) - 0.0083) < 1e-9
          and abs(round(_AO['banked'][6], 2) - 2.64) < 1e-9
          and abs(round(_AO['forbidden'][6], 2) - 1.33) < 1e-9
          and abs(round(_AO['banked'][7], 3) - 1.327) < 1e-9
          and abs(round(_AO['forbidden'][7], 3) - 1.114) < 1e-9
          and abs(round(_AO['banked'][8], 3) - 302.943) < 1e-9
          and abs(round(_AO['forbidden'][8], 3) - 301.400) < 1e-9
          and abs(round(_LA_CTL, 3) - 301.375) < 1e-9))
print("""
    ⛭⛭⛭ THE RECOMMENDATION 69 ASKED FOR AT r7657 -- ALL FOUR ITEMS TAKEN AT r7659, RECORDED HERE
    BECAUSE A RECOMMENDATION THAT HAS BEEN ACTED ON SHOULD STOP ASKING:
      ① the licensed half: taken, and taken FURTHER than asked.  I recommended keeping the half
        and naming the grid; 69 removed the measured null instead and wrote `moves neither
        statistic by construction`, which is the stronger statement and the true one on this arm.
        ⇒ `coef, licensed` and `shape, licensed` are now DECLARED WITHDRAWN above, with that
        reason, rather than tolerated as silent misses.
      ② the forbidden half: taken, every digit.  The paragraph now prints 6.7 of an error,
        -0.0670+-0.0086 -> -0.0092+-0.0085, 86 per cent, 32 -> 38, 16 -> 12, 2.64 -> 1.33 and
        l_A 302.943 -> 301.400 against 301.375 -- this receipt's own figures, so I③ and I④ read
        them back as AGREEMENTS.
      ③ the four-ceiling sentence: taken.  `indistinguishable below ell ~= 900` and `a longest run
        of seven to nine bins`, with 9, 9, 9, 16 against 7, 8, 8, 12.  I⑤ derives the ceiling and
        both run bounds from each state's own gap profile and checks the sentence against them.
      ④ the `\\rcpt` on that sentence: taken -- l.1952-1954 now cites THIS receipt.
    ⛔ AND WHAT THE FOUR COST, WHICH IS THE PART WORTH CARRYING FORWARD: three of these seven
    reads went BLIND on the rewording that took (2) and (3), and passed green for two revisions
    because a missing read short-circuits its gate.  60 found it at r7660, not a gate.  I⑧ is the
    repair, and the rule it carries is general: ** a reader allowed to find nothing must say WHICH
    nothing it found. **
""")
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
