#!/usr/bin/env python3
"""
P15 receipt -- `r7041` ⓒ AT FULL COVERAGE: THE BAND-RMS RATIO DOES NOT MOVE WITH ANY NUMERICAL
SETTING AT THE 0.6% FLOOR -- AND ELEVEN OF THE TWELVE AXIS READINGS ARE STILL NOT "CONVERGED",
WHICH IS THE HALF OF THE RESULT THAT HAS TO BE SAID FIRST.

** WHAT WAS RUN. **  `r7041`'s convergence sweep, finished at 10:53 on 2026-10-01: 158,885 modes over
66 queued configurations, each a projection of a KNOWN analytic oscillation (`SRCINJ`) on the two arms,
tiled on `KSLICE` and folded by `computations/beyond_the_wall/r7041_directions/fold.py`.  Two injection
schemes (`fixed`, `sweepown`) x two arms (`cr`, `lcdm`) x twelve settings = 48 runs, all on disk.

** THE QUANTITY IS THE BAND-RMS RATIO, NOT "THE RETENTION" ** (`r7057`/`r7059`/`r7061`).  About a THIRD
of the reported `+0.0139` per acoustic period is a phase drift between the two arms' SOURCE combs, which
a band root-mean-square reads as retention.  *That fraction is irrelevant to the convergence question --
whether the number stops moving with the numerical settings -- and decisive for the sentence written
about it afterwards, so the name is kept exact here.*

** THE FINDING, BOTH HALVES. **
  (1) ** NOTHING MOVES IT. **  `fixed` sits at 1.0587 and `sweepown` at 1.0659-1.0660 across every
      refinement of every axis.  The worst last step over all twelve axis readings is 0.008%, against a
      pre-registered floor of 0.6% -- a factor of 75 inside it -- and the base points reproduce
      `r6919`'s banked 1.0587/+0.01189 and 1.0659/+0.02260 exactly.
  (2) ⛔ ** AND ONLY ONE OF THE TWELVE IS REPORTABLE AS CONVERGED. **  The pre-registration says a
      sequence that has not TURNED OVER is not converged whatever its last step, and that monotonicity is
      undefined on two points.  SEVEN readings therefore read *"step under the floor but the sequence has
      NOT turned over"*, four read *"TWO POINTS ONLY"*, and exactly one -- `sweepown`'s eta half-width
      NLOSW -- reads *"converged at the floor"*.  ⌗ *A small last step is the cheapest way to look
      converged without being it; the sweep bought stability, not convergence, and says so.*

⛭ ** AND THERE ARE NOT TWELVE AXES. FIVE MOVED IT ON THE ARM, SIX ON THE CONTROL. **  `NK` is inert on
the arm BY CONSTRUCTION -- the arm's k ladder is `sqrt(L(L+2))*stretch` out to `KMAXL` and `NK` is a
decimation cap never reached, so `nk15` and `nk20` are the same computation as `base` (byte-identical `k`
and `eta` from `GRIDSAVE`, `max|Dl| = 0.0` on the banked slices), and the six arm-NK configurations were
never queued at all.  On the control `NK` carries 2547 -> 3822 -> 5094 modes and the spectra differ
outright.  `LSTEP` is the mirror case: a REAL axis for the sweep (238 -> 475 reported ell points) and
inert for the ACCEPTANCE on both arms.
  ⇒ *** So the sentence the verdict is gated against is "five axes moved it on the arm, six on the
  control", not "twelve". ***  ⌗ *The run log is the evidence and not the argument: the sweep's last two
  configurations to finish were `real_lcdm_nk15` and `real_lcdm_nk20` -- NK on the CONTROL -- while all
  six arm-NK rows never started.  The asymmetry is in what the launcher queued.*

⚠ ** WHAT THIS RECEIPT CAN AND CANNOT READ, STATED RATHER THAN BLURRED. **  The folded spectra live in
`/tmp/n66/r7041/` and are NOT in the repository, so in CI the projection integrals cannot be recomputed
here.  ⇒ This receipt therefore does BOTH, and says which it did: when the bank is present it folds the
48 runs through `fold.load` and computes the twelve sequences from the spectra; when it is absent it
reads the table banked below from the full-coverage run.  ** The pre-registered verdict rule is
re-implemented from its statement either way and the verdict labels are asserted, not quoted ** -- so the
claim under test is the rule applied to the numbers, which is what the convergence claim rests on.
  ⛔ *A receipt that recomputed nothing and printed the sweep's own conclusion back would be asserting
  the persistence of a symptom. `r7061`'s class: a gate must assert THE FINDING, read from the state the
  finding is a claim about -- and where it cannot reach that state it says so in the cell, as the
  resolution-table receipt did for this same bank.*
"""
import os
import sys

import numpy as np

FLOOR = 0.006          # `r6911`'s, on a KNOWN injected contrast
LO, HI, NG = 0.85, 5.75, 1200
BANK = '/tmp/n66/r7041/inj'
INJ = ('fixed', 'sweepown')

# the sequences, each one axis refined in one direction; `base` is every sequence's first point
SEQ = {
    'KFAC':  ['base', 'kfac26', 'kfac32', 'kfac40'],
    'NK':    ['base', 'nk15', 'nk20'],
    'NLOS':  ['base', 'nlos1120', 'nlos2240'],
    'NLOSW': ['base', 'nlosw9', 'nlosw12'],
    'NLOSF': ['base', 'nlosf90'],
    'LSTEP': ['base', 'lstep4'],
}
# ⛭ the one substitution, and it is an identity rather than an approximation -- see the header
INERT_ON_ARM = {'nk15', 'nk20'}

# ** THE TABLE BANKED FROM THE FULL-COVERAGE RUN of 2026-10-01 10:53 ** -- used when the bank of folded
# spectra is absent, which is CI.
# ⛔ ** AND IT IS BANKED AT FULL PRECISION, BECAUSE A ROUNDED TABLE CANNOT CARRY THE RULE. **  The first
# version of this receipt banked the ratios at the 4 dp its reader prints, and the fallback path then
# reported EIGHT of twelve readings converged against the live path's ONE.  *The pre-registration's test is
# whether a sequence has TURNED OVER -- the SIGNS of its steps -- and rounding four identical-to-4-dp
# points to `1.0587` destroys exactly that, leaving differences of zero that read as a turn.*
#   ⇒ A table precise enough to quote is not a table precise enough to apply the rule to, and the honest
#   remedy is the precision, not a looser rule.  ⌗ *The same defect in miniature as the reader that could
#   not see the sweep: an instrument given less state than its question needs will still answer.*
BANKED = {
    ('fixed', 'KFAC'): [1.058685304866, 1.058685375771, 1.058685376190, 1.058685376297],
    ('fixed', 'NK'): [1.058685304866, 1.058685304748, 1.058685304690],
    ('fixed', 'NLOS'): [1.058685304866, 1.058685042345, 1.058684975020],
    ('fixed', 'NLOSW'): [1.058685304866, 1.058684929568, 1.058684858006],
    ('fixed', 'NLOSF'): [1.058685304866, 1.058687068324],
    ('fixed', 'LSTEP'): [1.058685304866, 1.058598582178],
    ('sweepown', 'KFAC'): [1.065942504021, 1.065991974081, 1.065994035591, 1.065994125397],
    ('sweepown', 'NK'): [1.065942504021, 1.065942429208, 1.065942395573],
    ('sweepown', 'NLOS'): [1.065942504021, 1.065939468052, 1.065938716482],
    ('sweepown', 'NLOSW'): [1.065942504021, 1.065937681365, 1.065938456689],
    ('sweepown', 'NLOSF'): [1.065942504021, 1.065964763488],
    ('sweepown', 'LSTEP'): [1.065942504021, 1.065873307190],
}
R6919 = {'fixed': 1.0587, 'sweepown': 1.0659}        # the banked base points this must reproduce


def env_a(x, y, win=1.0):
    e = np.empty_like(y, dtype=float)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    y = np.asarray(y, float)
    e = env_a(x, y, win)
    return (y - e) / e


def from_bank():
    """the twelve sequences computed from the folded spectra, or None when the bank is absent"""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     '..', '..', 'computations', 'beyond_the_wall', 'r7041_directions')
    if not os.path.isdir(BANK) or not os.path.isdir(d):
        return None
    sys.path.insert(0, os.path.normpath(d))
    try:
        import fold
    except Exception:
        return None

    def load(inj, arm, s):
        if arm == 'cr' and s in INERT_ON_ARM:
            s = 'base'                 # the identity, warranted in the header and gated in report_c
        r = fold.load(BANK, f'inj_{inj}_{arm}_{s}')
        if r is None:
            return None
        ls, Dl, l_A, _form = r
        return ls / l_A, Dl

    def ratio(inj, s):
        a, b = load(inj, 'cr', s), load(inj, 'lcdm', s)
        if a is None or b is None:
            return None
        x = np.linspace(LO, HI, NG)
        A, B = np.interp(x, a[0], osc(*a)), np.interp(x, b[0], osc(*b))
        return float(np.sum(A * B) / np.sum(B * B))

    out = {}
    for inj in INJ:
        for name, seq in SEQ.items():
            vals = [ratio(inj, s) for s in seq]
            if any(v is None for v in vals):
                return None            # an incomplete bank is not a partial result here: fall back
            out[(inj, name)] = vals
    return out


def verdict(vals, step_frac):
    """THE PRE-REGISTERED RULE, re-implemented from its statement and not copied from the reader.

    `a sequence that has not turned over is not converged whatever its last step`, and monotonicity is
    UNDEFINED on two points -- so a two-point axis cannot be reported converged however small its step.
    """
    if step_frac > FLOOR:
        return 'unconverged'
    if len(vals) < 3:
        return 'two-points-only'
    mono = all((vals[j + 1] - vals[j]) * (vals[1] - vals[0]) > 0 for j in range(len(vals) - 1))
    return 'not-turned-over' if mono else 'converged'


live = from_bank()
SOURCE = ('the folded spectra in %s' % BANK) if live else \
         'the table banked from the 2026-10-01 10:53 run (the spectra are not in the repository)'
seqs = live if live else {k: list(v) for k, v in BANKED.items()}
# ⌗ ONE definition of the step, so the two paths cannot disagree about what they measured
steps = {k: 100.0 * abs(v[-1] - v[-2]) / abs(v[-2]) for k, v in seqs.items()}
if live:
    # ⛔ and when it DID reach the spectra, the recomputed ratios must reproduce the banked table
    for k, v in seqs.items():
        for got, want in zip(v, BANKED[k]):
            assert abs(got - want) < 1e-8, f'{k}: {got:.12f} is not the banked {want:.12f}'

assert len(seqs) == 12, f'twelve axis readings, not {len(seqs)}'

# --- (1) nothing moves it: every last step is inside the floor, worst 0.008% ------------------------
worst = max(steps.values())
for k, s in steps.items():
    assert s <= 100 * FLOOR, f'{k}: last step {s}% is ABOVE the {100*FLOOR}% floor'
# ⌗ the worst reading is `fixed`/LSTEP at 0.0082%, which is the 0.008% the sweep's reader prints;
#   the assertion is on the ROUNDED figure because that is the figure the claim quotes.
assert round(worst, 3) == 0.008, f'the worst last step must round to 0.008%, not {worst}%'

# --- the base points reproduce r6919 ---------------------------------------------------------------
for inj in INJ:
    for name in SEQ:
        assert abs(seqs[(inj, name)][0] - R6919[inj]) < 5e-5, f'{inj}/{name}: base is not r6919\'s'

# --- (2) exactly ONE of the twelve is reportable as converged ---------------------------------------
verds = {k: verdict(v, steps[k] / 100.0) for k, v in seqs.items()}
conv = sorted(k for k, v in verds.items() if v == 'converged')
assert not [k for k, v in verds.items() if v == 'unconverged'], 'nothing may read unconverged here'
assert len(conv) == 1, f'exactly one reading may read converged, not {len(conv)}: {conv}'
assert conv[0] == ('sweepown', 'NLOSW'), f"the one converged reading is sweepown/NLOSW, not {conv[0]}"
assert sum(1 for v in verds.values() if v == 'two-points-only') == 4
assert sum(1 for v in verds.values() if v == 'not-turned-over') == 7

# --- and the counting the verdict is gated against: five axes on the arm, six on the control --------
arm_axes = [n for n in SEQ if not set(SEQ[n][1:]) <= INERT_ON_ARM]
ctl_axes = list(SEQ)
assert len(arm_axes) == 5 and len(ctl_axes) == 6, 'five on the arm, six on the control'
assert 'NK' not in arm_axes and 'NK' in ctl_axes, 'NK is the axis the arm does not carry'
assert 'LSTEP' in arm_axes, 'LSTEP is real for the sweep on both arms, inert for the ACCEPTANCE'

print('P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting -- PASS')
print(f'  read from   : {SOURCE}')
print(f'  worst step  : {worst:.3f}% against the {100*FLOOR:.1f}% floor -- a factor of {100*FLOOR/worst:.0f} inside it')
print(f'  ratios      : fixed = 1.0587 flat; sweepown = 1.0659-1.0660  (r6919 base points reproduced)')
print(f'  converged   : {len(conv)} of 12 readings -- {conv[0][0]}/{conv[0][1]} only')
print( '                7 read `not turned over`, 4 read `two points only`')
print( '  the axes    : FIVE moved it on the arm, SIX on the control -- NK inert on the arm by construction')
