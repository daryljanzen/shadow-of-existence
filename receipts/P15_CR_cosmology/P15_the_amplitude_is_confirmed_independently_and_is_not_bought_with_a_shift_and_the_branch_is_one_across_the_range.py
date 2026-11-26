# -*- coding: utf-8 -*-
"""⛭⛭⛭ `r7875+cc66` ** ⑬ `60`'s AMPLITUDE IS **CONFIRMED INDEPENDENTLY** -- MY OWN CAMB LEG AND MY
OWN FITTING CODE GIVE `1.1516214` AND `1.2959211` AGAINST `60`'s `1.1516250` AND `1.2959240`, AGREEING
TO `3.5e-06` -- AND IT IS **NOT BOUGHT WITH A SHIFT THE GEOMETRY DISALLOWS**: PINNING `ε` MOVES `A`
BY `0.000211`. ⑭ AND THE BRANCH IS **ONE BASIN ON BOTH RULERS AT EVERY SUM FROM `0.20` TO `0.60`**,
WITH NO BOX WALL ANYWHERE **

COMPUTES: nothing.  Every figure is read out of the two JSON records this revision's drivers wrote
(`amplitude_check.json`, `branch_scan.json`).  No parameter is pinned here.

⌗ TWO REGISTRATION DEFECTS OF MINE ARE RECORDED BELOW, and one registered expectation is REFUTED in
`60`'s favour.  The defects: `Ⓐ①` named `lmax = 1200` where `r7871` ran `2600`, and `Ⓑ②` asked my
fresh UNLENSED ratio to match my `r7871` record, which is LENSED.  The refutation is `Ⓗ⑧`'s: I
expected `A` to move once `ε` was pinned inside its allowance, and it does not.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7875_cc66_the_independent_check_of_the_amplitude_and_the_branch_scan_'
                    'across_the_sums')

_n, _fail = [0], [0]


def check(label, ok, detail=''):
    _n[0] += 1
    if not ok:
        _fail[0] += 1
    print('\n    [%s] %s' % ('PASS' if ok else 'FAIL', label))
    if detail:
        print('             %s' % detail)


def load(p):
    if not os.path.exists(p):
        sys.exit('FATAL: %s is not where this reads it from.' % p)
    return json.load(io.open(p, encoding='utf-8'))


print('=' * 100)
print(__doc__)
print('=' * 100)

AC = load(os.path.join(MINE, 'amplitude_check.json'))
BS = load(os.path.join(MINE, 'branch_scan.json'))
F = AC['fits']

# ───────────────────────────────────────────── Ⓐ① the control, and the lmax the amendment fixed
check("⛭ `r7875` ** ⑬ Ⓐ① THE CONTROL IS **READ FROM `60`'s MODULE AT RUN TIME**, AND `lmax` IS "
      "`2600` **BECAUSE THE REGISTRATION NAMED `1200` AND WAS WRONG** ** ⇒ *** `H0 = 67.40`, "
      "`Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965`, with `τ = 0.054` and `A_s = 2.1e-9` declared. "
      "`lmax = 2600` is `r7871`'s `lmax_calc`, which is where `60` took theirs; I registered `1200`, "
      "which is `r7873`'s, and amended it IN ITS OWN COMMIT BEFORE computing. ** A like-for-like "
      "check at the wrong `lmax` would not have been one. *** ⌗ *The amendment is on the record "
      "rather than silent, because a registration corrected after the answer is worthless*",
      (abs(AC['control']['H0'] - 67.40) < 1e-9 and abs(AC['control']['OM'] - 0.3150) < 1e-9
       and abs(AC['control']['WB'] - 0.0224) < 1e-9 and abs(AC['control']['NS'] - 0.965) < 1e-9
       and abs(AC['tau'] - 0.054) < 1e-12 and AC['lmax'] == 2600
       and AC['window'] == [100, 420]),
      'control %s; tau %.3f; lmax %d; window %s' % (AC['control'], AC['tau'], AC['lmax'],
                                                    AC['window']))

# ───────────────────────────────────────────── Ⓑ② the mis-specified control, and the corrected one
check("⛭⛔⛭ `r7875` ** ⑬ Ⓑ② **THE CONTROL I REGISTERED COMPARED TWO DIFFERENT QUANTITIES** -- MY "
      "FRESH **UNLENSED** RATIO AGAINST MY `r7871` RECORD, WHICH IS **LENSED** -- AND COMPARED LIKE "
      "WITH LIKE IT PASSES AT **EXACTLY ZERO** ** ⇒ *** as registered it failed at a worst relative "
      "`1.678e+02`. ** AND MY FIRST READING OF THAT FAILURE WAS ALSO WRONG: ** I suspected the "
      "near-zero-denominator trap this corpus has now met four times, but measuring ABSOLUTELY gave "
      "real differences up to `4.902e-02`, largest exactly where lensing bites. `r7871`'s driver "
      "takes `lensed_scalar`; `60`'s `shift.py` takes `unlensed_scalar`. ** My fresh LENSED leg "
      "reproduces the record's six banked multipoles at `0.0` absolute and `0.0` relative -- "
      "bit-identical. So my CAMB leg was never wrong; the control's specification was. *** ⌗ *The "
      "band is `1e-9` ABSOLUTE and not relative, because the ratio changes sign inside the record's "
      "own multipoles -- the `r7873` rule, applied to my own control this time*",
      (AC['b2_worst_abs'] == 0.0 and AC['b2_worst_rel'] == 0.0
       and AC['b2_worst_abs'] < 1e-9 and AC['A_reported'] is True),
      'worst absolute %.1e and worst relative %.1e over the 24 comparisons'
      % (AC['b2_worst_abs'], AC['b2_worst_rel']))

# ───────────────────────────────────────────── Ⓒ③ the allowance, reproduced exactly
check("⛭⛭⛭ `r7875` ** ⑬ Ⓒ③ **`ε`'s ALLOWANCE FROM `θ*` REPRODUCES `60`'s EXACTLY, AT RELATIVE "
      "ZERO** ** ⇒ *** `f_inst = l_A(Σ)/l_A(0) − 1` with `l_A` READ from the instrument bank, and "
      "`f_camb = −(θ*(Σ)/θ*(0) − 1)` because `ℓ` scales as `1/θ*`; the allowance is the difference. "
      "I get `2.563377e-04` at `Σ = 0.30` and `5.170089e-04` at `0.60`, against `60`'s same two "
      "figures at relative `0.0`. ** Only `θ*` is mine here, so this is an agreement about CAMB's "
      "`θ*` and not about the fit. *** ⌗ *It had to be checked separately: if `θ*` disagreed, every "
      "`ε` below would be measured against the wrong yardstick and `A` could still look right*",
      (abs(AC['allowance']['0.30']['allowed'] - 0.00025633773521949177) < 1e-18
       and abs(AC['allowance']['0.60']['allowed'] - 0.0005170088639169235) < 1e-18
       and AC['allowance']['0.30']['rel_to_60'] == 0.0
       and AC['allowance']['0.60']['rel_to_60'] == 0.0),
      'allowance %.6e at 0.30 and %.6e at 0.60, both at relative zero to 60\'s'
      % (AC['allowance']['0.30']['allowed'], AC['allowance']['0.60']['allowed']))

# ───────────────────────────────────────────── Ⓓ④ the fitter is not hard-wired
check("⛭⛭⛭ `r7875` ** ⑬ Ⓓ④ **THE FITTER RECOVERS A PLANTED `(A, ε)` TO `4.441e-16`, SO IT IS NOT "
      "HARD-WIRED TO `60`'s ANSWER** ** ⇒ *** three plants imposed on the CAMB ratio and refitted: "
      "`A = 1.40` at `ε = +0.0030`, `A = 0.80` at `−0.0045`, and `A = 1.00` at `0.0`. Worst "
      "recovery error in `A` is `4.440892e-16`. ** A fitter that returned about `1.15` on TT "
      "whatever it was given would agree with `60` for no reason at all, and `Ⓔ⑤` below would be "
      "worthless. *** ⌗ *The same positive control the `MassiveNuMethod` knob needed at `r7871` and "
      "the custom-source path at `r7873`: a mechanism that cannot fail cannot confirm*",
      (AC['planted_ok'] is True and len(AC['planted']) == 3
       and max(v['dA'] for v in AC['planted'].values()) < 1e-12
       and abs(max(v['dA'] for v in AC['planted'].values())
               - 4.440892098500626e-16) < 1e-24),
      '3 plants, worst |dA| %.6e' % max(v['dA'] for v in AC['planted'].values()))

# ───────────────────────────────────────────── Ⓔ⑤ THE ANSWER to 69's question
check("⛭⛭⛭ `r7875` ** ⑬ Ⓔ⑤ **THE ANSWER: YES. ALL FOUR AMPLITUDES REPRODUCE `60`'s, THE TWO `69` "
      "NAMED TO `3.5e-06` AND `2.8e-06`** ** ⇒ *** my own CAMB leg, my own fitting code, `60`'s `41` "
      "in-band multipoles: `TT` at `Σ = 0.30` gives `1.1516214` against `60`'s `1.1516250`; `TT` at "
      "`0.60` gives `1.2959211` against `1.2959240`; `EE` at `0.30` gives `1.0140592` against "
      "`1.0140521`; `EE` at `0.60` gives `1.0463072` against `1.0462960`. Worst disagreement over "
      "the four is `1.112883e-05`. ** `69` asked whether I get `1.152` and `1.296`. I do, to five "
      "and six decimals, on a registered tolerance of `0.005` that was three orders too loose. *** "
      "⌗ *So TT's sum response really is about `15` per cent above CAMB's at `0.30` and `30` at "
      "`0.60`, as `60` reported*",
      (abs(F['TT|0.30']['A_free'] - 1.151621417168135) < 1e-12
       and abs(F['TT|0.60']['A_free'] - 1.2959211454888449) < 1e-12
       and abs(F['EE|0.30']['A_free'] - 1.0140591924745146) < 1e-12
       and abs(F['EE|0.60']['A_free'] - 1.0463071504477712) < 1e-12
       and abs(F['TT|0.30']['abs_diff_from_60'] - 3.5380344298729938e-06) < 1e-15
       and abs(F['TT|0.60']['abs_diff_from_60'] - 2.8202029827006925e-06) < 1e-15
       and AC['n_hits'] == 4
       and all(F[k]['hits_target'] for k in F)
       and max(F[k]['abs_diff_from_60'] for k in F) < 1.2e-05),
      'TT %.7f vs %.7f and %.7f vs %.7f; worst |dA| over the four %.6e'
      % (F['TT|0.30']['A_free'], F['TT|0.30']['target_60'], F['TT|0.60']['A_free'],
         F['TT|0.60']['target_60'], max(F[k]['abs_diff_from_60'] for k in F)))

# ───────────────────────────────────────────── Ⓕ⑥ Ⓗ⑧'s expectation refuted, in 60's favour
check("⛭⛔⛭ `r7875` ** ⑬ Ⓕ⑥ **MY REGISTERED `Ⓗ⑧` IS REFUTED, AND IN `60`'s FAVOUR: THE AMPLITUDE IS "
      "**NOT BOUGHT WITH A SHIFT THE GEOMETRY DISALLOWS**. PINNING `ε` MOVES `A` BY `0.000211` ** ⇒ "
      "*** I registered that `A` would move once `ε` was pinned inside its allowance, because `60`'s "
      "own record shows `ε` running `2.77` to `6.57` times that allowance -- which my fit reproduces. "
      "** It barely moves. ** `TT` at `0.30` reads `1.1516214` at `ε` free, `1.1517591` at `ε` "
      "pinned to `+` the allowance, and `1.1518321` at `ε = 0`: a spread of `0.000211`, which is "
      "`60` times SMALLER than the `0.015` excess over unity that the claim rests on. ** So the "
      "shift and the amplitude are separable here, and the amplitude survives without the shift. *** "
      "⌗ *This was registered as the arm most likely to qualify `60`'s reading, and it strengthens "
      "it instead. Reported as refuted because that is what the registration said*",
      (all(F[k]['eps_within_allowed'] is False for k in F)
       and abs(F['TT|0.30']['eps_over_allowed'] - 2.7731968505975617) < 1e-12
       and abs(F['EE|0.30']['eps_over_allowed'] - 6.574236908807055) < 1e-12
       and abs(F['TT|0.30']['A_eps_zero'] - 1.1518321192349157) < 1e-12
       and abs(F['TT|0.30']['A_eps_pinned_plus'] - 1.1517590895636403) < 1e-12
       and abs(max(F['TT|0.30']['A_eps_zero'], F['TT|0.30']['A_eps_pinned_plus'],
                   F['TT|0.30']['A_free'])
               - min(F['TT|0.30']['A_eps_zero'], F['TT|0.30']['A_eps_pinned_plus'],
                     F['TT|0.30']['A_free']) - 0.000210702) < 1e-8),
      'eps is %.4f x its allowance at TT 0.30 yet A runs only %.7f (free) to %.7f (eps=0)'
      % (F['TT|0.30']['eps_over_allowed'], F['TT|0.30']['A_free'],
         F['TT|0.30']['A_eps_zero']))

# ───────────────────────────────────────────── Ⓖ⑦ the multipole set is load-bearing
check("⛭⛔⛭ `r7875` ** ⑬ Ⓖ⑦ **THE MULTIPOLE SET IS LOAD-BEARING AT A LEVEL `1000` TIMES THE "
      "AGREEMENT: `60`'s `41` IN-BAND MULTIPOLES GIVE `1.1516214`, ALL `321` GIVE `1.1473108`** ** ⇒ "
      "*** the instrument bank carries `238` multipoles of which `41` fall in `ℓ = 100`--`420`, and "
      "`60` fit on those. Interpolating the instrument ratio onto every integer `ℓ` instead moves "
      "`TT` at `0.30` by `0.004311` -- against the `3.538034e-06` that separates my `A` from `60`'s. "
      "** So matching `60`'s multipole set was not a detail; it is the difference between confirming "
      "their number and reporting a different one. Both are given. *** ⌗ *The interpolation scheme "
      "is my choice too, and it is worth `3.515264e-06` between linear and cubic -- about the size "
      "of the agreement itself, so a disagreement smaller than that would not have been one*",
      (F['TT|0.30']['n_multipoles'] == 41
       and abs(F['TT|0.30']['A_all_321'] - 1.1473107864101062) < 1e-12
       and abs(abs(F['TT|0.30']['A_all_321'] - F['TT|0.30']['A_free']) - 0.004310631) < 1e-8
       and abs(F['TT|0.30']['interp_sensitivity'] - 3.515263913511646e-06) < 1e-15
       and abs(F['TT|0.30']['A_all_321'] - F['TT|0.30']['A_free'])
       > F['TT|0.30']['abs_diff_from_60'] * 100),
      '41 multipoles -> %.7f, 321 -> %.7f, a gap of %.6f; interpolation worth %.6e'
      % (F['TT|0.30']['A_free'], F['TT|0.30']['A_all_321'],
         abs(F['TT|0.30']['A_all_321'] - F['TT|0.30']['A_free']),
         F['TT|0.30']['interp_sensitivity']))

# ───────────────────────────────────────────── Ⓗ⑧ the lensing leg, and what it does to EE
check("⛭⛔⛭ `r7875` ** ⑬ Ⓗ⑧ **THE LENSING LEG MOVES `TT`'s `A` BY `0.003516` BUT `EE`'s BY "
      "`0.036161` -- LARGER THAN `EE`'s WHOLE CLAIMED EXCESS. SO TT's RESULT IS ROBUST TO THAT "
      "CHOICE AND THE `EE` READING IS NOT ** ⇒ *** `60` fit against CAMB's UNLENSED spectra. "
      "Refitting the same instrument ratios against my LENSED leg gives `TT` at `0.30` "
      "`1.1551372` instead of `1.1516214`, a move of `0.003516` on an excess of `0.15`; but `EE` at "
      "`0.30` gives `1.0502204` instead of `1.0140592`, a move of `0.036161` on an excess of only "
      "`0.014`. ** `EE` would read a `5` per cent excess rather than a `1.4` per cent one. *** ⌗ "
      "*`60` compared the instrument against BOTH CAMB legs at `r7872`, with the stated reason that "
      "if the departure is the same on both then lensing is not what carries it -- so this is "
      "already theirs and is flagged, NOT offered as a correction. It bears only on `EE`, and `69`'s "
      "order routed the physics to `60` either way*",
      (abs(F['TT|0.30']['lensing_moves_A'] - 0.003515807347835187) < 1e-15
       and abs(F['EE|0.30']['lensing_moves_A'] - 0.036161218199312284) < 1e-15
       and abs(F['EE|0.30']['A_lensed_leg'] - 1.0502204106738269) < 1e-12
       and F['EE|0.30']['lensing_moves_A'] > abs(F['EE|0.30']['A_free'] - 1.0) * 2
       and F['TT|0.30']['lensing_moves_A'] < abs(F['TT|0.30']['A_free'] - 1.0) / 10),
      'lensing moves TT by %.6f on an excess of %.4f, and EE by %.6f on an excess of %.4f'
      % (F['TT|0.30']['lensing_moves_A'], F['TT|0.30']['A_free'] - 1.0,
         F['EE|0.30']['lensing_moves_A'], F['EE|0.30']['A_free'] - 1.0))

# ───────────────────────────────────────────── Ⓘ⑨ the scan: one basin everywhere
_S = BS['scan']
check("⛭⛭⛭ `r7875` ** ⑭ Ⓘ⑨ **ONE BASIN ON BOTH RULERS AT EVERY SUM FROM `0.20` TO `0.60`, WITH **NO "
      "BOX WALL ANYWHERE** ** ⇒ *** eight pairs, `28` minimisations: `Σ = 0.20`, `0.30`, `0.50` and "
      "`0.60` on `rd_camb` and `rd_min`, two `H0` starts each at `60`'s own `65.29` and `68.59`, "
      "plus the midpoint. Every pair reads ONE BASIN. ** Six have the midpoint strictly BELOW the "
      "worse endpoint -- no ridge at all -- the widest being `rd_camb` at `0.20` at `0.036365` "
      "below, which is `7.273` times `fatol` the right way. ** And no run on any pair sits on a box "
      "wall, so every verdict is about the likelihood and not about the box. *** ⌗ *With `r7873`'s "
      "`0.400` this covers five sums on both rulers*",
      (len(_S) == 8
       and all('ONE BASIN' in v['verdict'] for v in _S.values())
       and all(not v['walls'] for v in _S.values())
       and abs(_S['rd_camb|0.20']['midpoint_minus_worse'] - (-0.036364614948752205)) < 1e-15
       and abs(_S['rd_camb|0.20']['excess_over_fatol'] - (-7.272922989750441)) < 1e-12
       and sum(1 for v in _S.values() if v['midpoint_minus_worse'] <= 0.0) == 6),
      '%d pairs, all ONE BASIN, no walls; %d with the midpoint at or below the worse endpoint'
      % (len(_S), sum(1 for v in _S.values() if v['midpoint_minus_worse'] <= 0.0)))

# ───────────────────────────────────────────── Ⓙ⑩ the two ridges, and why the scale matters
check("⛭⛔⛭ `r7875` ** ⑭ Ⓙ⑩ **TWO PAIRS SHOW A RIDGE, AND THE UNSCALED TEST OF `r7873` WOULD HAVE "
      "CALLED THEM **TWO BASINS** -- SO THE SCALE ADDED AFTER THAT DEFECT DECIDES REAL CASES ** ⇒ "
      "*** `rd_camb` at `0.60` has a midpoint `0.000394` ABOVE its worse endpoint, and `rd_min` at "
      "`0.30` has `0.000415`. Both are positive, so a test comparing against ZERO -- which is what I "
      "wrote at `r7873` before the defect was caught -- would have returned TWO BASINS on both. ** "
      "Scaled, they are `0.0789` and `0.0831` of the profiler's own `fatol`, and `3.9e-04` and "
      "`4.2e-04` of the one-parameter unit `Δχ² = 1`: barriers under every scale that means "
      "anything. *** ⌗ *At `r7873` the unscaled form called a barrier a hundredth of `fatol` a "
      "second basin on `rd_min`, and I recorded it as my defect. This revision is where that repair "
      "earns itself: two of eight pairs turn on it*",
      (_S['rd_camb|0.60']['midpoint_minus_worse'] > 0.0
       and _S['rd_min|0.30']['midpoint_minus_worse'] > 0.0
       and abs(_S['rd_camb|0.60']['midpoint_minus_worse'] - 0.00039432276423667645) < 1e-18
       and abs(_S['rd_min|0.30']['midpoint_minus_worse'] - 0.00041541205746398188) < 1e-18
       and abs(_S['rd_camb|0.60']['excess_over_fatol'] - 0.07886455284733529) < 1e-14
       and abs(_S['rd_min|0.30']['excess_over_fatol'] - 0.08308241149279638) < 1e-14
       and _S['rd_camb|0.60']['excess_over_fatol'] < 1.0
       and _S['rd_min|0.30']['excess_over_fatol'] < 1.0),
      'rd_camb 0.60 excess %+.6f (%.4f x fatol); rd_min 0.30 excess %+.6f (%.4f x fatol)'
      % (_S['rd_camb|0.60']['midpoint_minus_worse'], _S['rd_camb|0.60']['excess_over_fatol'],
         _S['rd_min|0.30']['midpoint_minus_worse'], _S['rd_min|0.30']['excess_over_fatol']))

# ───────────────────────────────────────────── Ⓚ⑪ the four base points that had to be computed
check("⛭⛭⛭ `r7875` ** ⑭ Ⓚ⑪ **FOUR OF THE EIGHT BASE POINTS DID NOT EXIST AND WERE COMPUTED HERE, "
      "DECLARED IN THE REGISTRATION RATHER THAN SUBSTITUTED QUIETLY** ** ⇒ *** `r7853`'s bank holds "
      "`0.000`--`0.300` and `0.400`, so `Σ = 0.20` and `0.30` READ their banked best fit for that "
      "ruler, exactly as `r7873` did, while `Σ = 0.50` and `0.60` had NOTHING to read on either "
      "ruler. Each of those four got a COLD profile run from the box centre first, and the record "
      "says which of the eight was read and which was computed. ** The two-start test sets the other "
      "four parameters from that base point, so a base invented silently would have made four of the "
      "eight verdicts untraceable. *** ⌗ *Registered as `Ⓙ⑩` before any of it ran*",
      (sum(1 for v in _S.values() if 'COLD' in v['base_from']) == 4
       and sum(1 for v in _S.values() if 'READ' in v['base_from']) == 4
       and all('COLD' in _S['%s|%.2f' % (m, s)]['base_from']
               for m in ('rd_camb', 'rd_min') for s in (0.50, 0.60))
       and all('READ' in _S['%s|%.2f' % (m, s)]['base_from']
               for m in ('rd_camb', 'rd_min') for s in (0.20, 0.30))),
      '4 base points READ from the r7853 bank (0.20, 0.30 on both rulers) and 4 COLD here '
      '(0.50, 0.60 on both)')

# ───────────────────────────────────────────── Ⓛ⑫ the box risk did not materialise
check("⛭⛭⛭ `r7875` ** ⑭ Ⓛ⑫ **THE BOX RISK I REGISTERED DID **NOT** MATERIALISE: NOT ONE OF THE "
      "`16` CONVERGED POINTS SITS ON A WALL, SO NO VERDICT IS THE BOX's ** ⇒ *** `BOX` caps `Ω_m` at "
      "`0.40` and `τ` at `0.12`, and at `Σ = 0.400` the `rd_min` best fit already sat at "
      "`Ω_m = 0.34387`, so I registered that a fit at `0.50` or `0.60` might land ON a boundary and "
      "that a midpoint between two boundary points measures the box rather than the basin. ** Every "
      "one of the sixteen two-start points is interior, on both rulers at all four sums, and the "
      "`walls` list is empty for all eight pairs. *** ⌗ *Registered as the thing most likely to "
      "invalidate the outer sums, and it is clean -- which is worth saying explicitly, because an "
      "unmaterialised risk left unmentioned reads as a risk that was never checked*",
      (all(v['walls'] == [] for v in _S.values())
       and all(r['interior'] for v in _S.values() for r in v['runs'].values())
       and sum(len(v['runs']) for v in _S.values()) == 16
       and abs(BS['box'][1][1] - 0.40) < 1e-12 and abs(BS['box'][4][1] - 0.12) < 1e-12),
      '%d two-start points, all interior, no wall on any of the %d pairs'
      % (sum(len(v['runs']) for v in _S.values()), len(_S)))

# ───────────────────────────────────────────── Ⓜ⑬ the scope of the claim
check("⛭⛔⛭ `r7875` ** ⑭ Ⓜ⑬ **WHAT THIS ESTABLISHES AND WHAT IT DOES NOT: FIVE SAMPLED SUMS UNDER "
      "ONE GEOMETRIC CRITERION, NOT EVERY SUM IN THE INTERVAL ** ⇒ *** at `r7873` I held the scope "
      "to `Σ = 0.400` and said `r7869`'s 'one branch to `0.60` eV' was as unestablished as `60` "
      "found it. With `0.20`, `0.30`, `0.50` and `0.60` added on both rulers it IS established "
      "**at those five sums, by this test**. ** It remains a statement about five points and about a "
      "midpoint criterion: a barrier narrower than the segment between two converged points, or one "
      "at a sum not sampled, is not excluded by it. *** ⌗ *The honest form of the answer `60` asked "
      "for. Saying 'one branch across the range' without the sampling would claim a continuum from "
      "five points*",
      (sorted(BS['sums']) == [0.20, 0.30, 0.50, 0.60]
       and sorted(BS['modes']) == ['rd_camb', 'rd_min']
       and sorted(BS['h0_starts']) == [65.29, 68.59]
       and len(_S) == 8),
      'sums %s on rulers %s from starts %s -- five sums counting r7873\'s 0.400'
      % (BS['sums'], BS['modes'], BS['h0_starts']))

# ───────────────────────────────────────────── the count arm
check("⛭ `r7875` ** Ⓝ⑭ THE ARMS ABOVE ARE **ALL OF THEM** ** ⇒ *** thirteen arms precede this one: "
      "eight on item ⑬ and five on item ⑭. *** ⌗ *A receipt that loses an arm to an editing slip "
      "reports fewer failures than it has*",
      _n[0] == 13,
      '%d arm(s) before this one' % _n[0])

print('\n' + '=' * 100)
print('  %d arm(s), %d failed' % (_n[0], _fail[0]))
print('=' * 100)
sys.exit(1 if _fail[0] else 0)
