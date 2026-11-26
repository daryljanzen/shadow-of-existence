# -*- coding: utf-8 -*-
"""⛭⛭⛭ `r7879+cc66` ** ⑮ ALL **TWENTY** FITS ON `60`'s FIVE BANKED LEGS CONFIRM THEIR FIGURES TO
`1.039197e-05`, AND **EVERY LEG PAIR IS RESOLVABLE** -- SO UNLIKE `r7877`'s `EE` THESE AGREEMENTS ARE
ABOUT THE LEGS. ⛔ **NO LEG PASSES `69`'s JOINT `0.03` BAR**; THE NEAREST IS `W` AT `0.059605`.
⑯ AND CAMB's OWN HIERARCHY AND ITS FLUID APPROXIMATION ARE **NOT MEASURABLY DIFFERENT OBJECTS**:
`Nu_trunc`, `Nu_approx` AND `Nu_best` ARE **BIT-IDENTICAL**, AND `A` MOVES BY `7.993606e-15` **

COMPUTES: nothing.  Every figure is read out of the two JSON records this revision's drivers wrote
(`legs_five.json`, `hierarchy_ref.json`).  No parameter is pinned here.

⌗ `69`'s order names SIX newly banked legs; `60`'s `parts/` and `60`'s own `refit_parts.json` and
`leverage.json` name FIVE (`W`, `C`, `E`, `CE`, `A1`): four decomposition legs plus ONE `c_a²` arm.
The five that exist are run, and `Ⓐ①` pins the count.

⌗ AND ⑯'s ANSWER RESTS ON A DISTINCTION THIS SEAT CANNOT RESOLVE, SO IT CLAIMS ONLY THE WEAKER HALF:
the two treatments are not measurably different **as the setting is exposed**, which is consistent
both with genuine agreement to machine precision and with the switch being inert here.  `Ⓘ⑨` says so
rather than asserting the stronger reading.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7879_cc66_the_decomposition_legs_and_cambs_own_hierarchy_reference')

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

L = load(os.path.join(MINE, 'legs_five.json'))
H = load(os.path.join(MINE, 'hierarchy_ref.json'))
F = L['fits']

# ───────────────────────────────────────────── Ⓐ① five legs, not six, and the same instrument
check("⛭⛔⛭ `r7879` ** ⑮ Ⓐ① **FIVE LEGS ARE BANKED, NOT THE SIX `69`'s ORDER NAMES** -- AND THE "
      "HARNESS RE-DERIVES `r7875`'s FOUR LANDED AMPLITUDES AT **EXACTLY ZERO** BEFORE ANY LEG IS "
      "READ ** ⇒ *** `60`'s `parts/` holds `W`, `C`, `E`, `CE` and `A1`, and `60`'s own "
      "`refit_parts.json` and `leverage.json` both record `arms = ['A1', 'C', 'CE', 'E', 'W']`: four "
      "decomposition legs plus ONE `c_a²` arm, not two. ** The five that exist are run and named; "
      "the count is pinned here so the record does not carry a sixth leg that never existed. ** And "
      "the regression control is `0.0`, so this is the same instrument as `r7875` and `r7877`. *** "
      "⌗ *The same class as the `shear_on`/`shear_off` ambiguity at `r7877`, which `69` then used to "
      "correct their own merge paragraph: a count in prose against the directory*",
      (sorted(L['legs']) == ['A1', 'C', 'CE', 'E', 'W']
       and len(L['legs']) == 5
       and L['regression_worst'] == 0.0
       and L['legs_read'] is True
       and L['legs_in_order_but_absent'] == []
       and len(F) == 20
       and all(v['n'] == 41 for v in F.values())),
      '%d legs (%s), %d fits, all on 41 multipoles; regression worst %.1e'
      % (len(L['legs']), ', '.join(sorted(L['legs'])), len(F), L['regression_worst']))

# ───────────────────────────────────────────── Ⓑ② the twenty fits
check("⛭⛭⛭ `r7879` ** ⑮ Ⓑ② **ALL TWENTY FITS CONFIRM `60`'s FIGURES, WORST `1.039197e-05`** ** ⇒ "
      "*** my own CAMB leg, my own fitter, `60`'s `41` multipoles, the LANDED zero leg as `60` "
      "choose it. `W` reads `0.995110` and `1.056210` in TT against `60`'s `0.995103` and "
      "`1.056207`; `C` reads `1.263947` at `Σ = 0.60` against `1.263943`; `CE` carries the worst "
      "disagreement at `1.039197e-05` on `EE` at `0.30`; `A1` reads `0.907858` against `0.907865`. "
      "** Twenty of twenty inside `0.005`, and the worst is four hundred times tighter than that. "
      "*** ⌗ *`W`'s TT at `Σ = 0.30` reads `0.995110` -- BELOW unity -- which independently confirms "
      "`60`'s finding that the weight change alone already crosses one*",
      (L['n_hits'] == 20 and all(v['hits'] for v in F.values())
       and abs(L['worst_diff'] - 1.0391969696099679e-05) < 1e-15
       and abs(F['W|TT|0.30']['A'] - 0.995110131467115) < 1e-13
       and abs(F['W|EE|0.60']['A'] - 0.9403953982410259) < 1e-13
       and abs(F['C|TT|0.60']['A'] - 1.263946697413109) < 1e-13
       and abs(F['CE|EE|0.30']['A'] - 1.0076975299696962) < 1e-13
       and abs(F['A1|TT|0.60']['A'] - 0.9078582831316561) < 1e-13
       and F['W|TT|0.30']['A'] < 1.0),
      '%d of %d within 0.005; worst %.6e; W TT 0.30 at %.6f is below unity'
      % (L['n_hits'], len(F), L['worst_diff'], F['W|TT|0.30']['A']))

# ───────────────────────────────────────────── Ⓒ③ every pair resolvable, unlike r7877
check("⛭⛭⛭ `r7879` ** ⑮ Ⓒ③ **ALL `40` LEG-PAIR COMPARISONS ARE RESOLVABLE, SO NONE OF THESE TWENTY "
      "AGREEMENTS IS THE DEGENERATE KIND `r7877`'s `EE` WAS** ** ⇒ *** at `r7877` the `EE` "
      "`shear_on`-minus-`shear_off` separation fell eighty times BELOW my own interpolation floor, "
      "so those four `EE` agreements confirmed the BANK READING and not the leg -- which I "
      "registered in advance and reported. ** Here every one of the `40` pairwise comparisons "
      "separates ABOVE the floors (`3.515264e-06` for TT, `5.307333e-05` for EE): `0` fall below. "
      "So these legs differ enough that agreeing with `60` on them is a statement about the legs. "
      "*** ⌗ *The caveat that applied at `r7877` does NOT apply here, and saying which is as much "
      "part of the answer as the numbers -- an agreement's worth depends on whether the fitter can "
      "tell the alternatives apart*",
      (L['n_pairs'] == 40 and L['n_unresolvable'] == 0
       and abs(L['floors']['TT'] - 3.515263913511646e-06) < 1e-18
       and abs(L['floors']['EE'] - 5.307332502169082e-05) < 1e-18
       and all(v['resolvable'] for v in L['separation'].values())),
      '%d pair comparisons, %d below the floors (TT %.6e, EE %.6e)'
      % (L['n_pairs'], L['n_unresolvable'], L['floors']['TT'], L['floors']['EE']))

# ───────────────────────────────────────────── Ⓓ④ no leg passes the joint bar
check("⛭⛔⛭ `r7879` ** ⑮ Ⓓ④ **NO LEG PASSES `69`'s REFINED JOINT BAR OF `0.03`, ON A SECOND "
      "FITTER** -- THE NEAREST IS `W`, WHOSE WORST IS `EE` AT `Σ = 0.60` WITH `|A − 1| = 0.059605`, "
      "TWICE THE BAR ** ⇒ *** `69` refined the criterion to *TT and EE both within `0.03` of unity "
      "on both fitters*. Measured against it: `W` fails on `EE` at `0.059605`; every other leg fails "
      "on TT at `Σ = 0.60`, from `A1`'s `0.092142` out to `C`'s `0.263947`. ** So the fluid family "
      "is refuted on the joint bar by the second fitter `69` asked for, and the failure is not "
      "marginal on any member. *** ⌗ *`W` is nearest and still misses by a factor of two, which is "
      "the useful form of the answer: the gap is not a tuning distance*",
      (L['any_passes_bar'] is False
       and abs(L['bar'] - 0.03) < 1e-12
       and L['nearest_leg'] == 'W'
       and abs(L['nearest_worst_dist'] - 0.059604601758974085) < 1e-15
       and abs(F['W|EE|0.60']['dist_from_unity'] - 0.059604601758974085) < 1e-15
       and abs(F['W|EE|0.60']['dist_from_unity'] - L['nearest_worst_dist']) < 1e-15
       and L['nearest_worst_dist'] > L['bar'] * 1.9
       and abs(F['C|TT|0.60']['dist_from_unity'] - 0.26394669741310905) < 1e-15
       and abs(F['A1|TT|0.60']['dist_from_unity'] - 0.09214171686834394) < 1e-15
       and not any(v['passes'] for v in L['against_bar'].values())),
      'no leg passes the %.2f bar; nearest %s at %.6f; C at 0.60 is %.6f out'
      % (L['bar'], L['nearest_leg'], L['nearest_worst_dist'],
         F['C|TT|0.60']['dist_from_unity']))

# ───────────────────────────────────────────── Ⓔ⑤ the liveness control on the methods
_liv = H['liveness']
check("⛭⛔⛭ `r7879` ** ⑯ Ⓔ⑤ **THE LIVENESS CONTROL IS THE WHOLE ANSWER: `Nu_trunc`, `Nu_approx` AND "
      "`Nu_best` ARE **BIT-IDENTICAL**, AND `Nu_int` DIFFERS BY `3.141247e-15` AT `Σ = 0.30` AND BY "
      "**EXACTLY ZERO** AT `0.60` ** ⇒ *** all four settings are accepted and echoed back by CAMB, "
      "so the knob is settable, not refused. But the spectra it produces are not different objects: "
      "`Nu_trunc == Nu_approx == Nu_best` exactly, at every sum and both blocks, and the hierarchy "
      "differs from them by `3.141247e-15` at `Σ = 0.30` and is IDENTICAL at `0.60`. ** This had to "
      "be measured BEFORE any amplitude: an `A` difference of zero between two settings that "
      "produce the same spectrum says nothing about hierarchies, only that the knob is inert. *** "
      "⌗ *The same positive control the `MassiveNuMethod` knob needed at `r7871`, the custom-source "
      "path at `r7873` and the fitter at `r7875` -- and here it is not a precaution, it IS the "
      "finding*",
      (all(_liv[k]['trunc_vs_approx_identical'] for k in _liv)
       and all(_liv[k]['approx_vs_best_identical'] for k in _liv)
       and _liv['TT|0.60']['Nu_trunc']['identical'] is True
       and _liv['EE|0.60']['Nu_approx']['identical'] is True
       and _liv['TT|0.60']['Nu_trunc']['max_abs_rel'] == 0.0
       and abs(_liv['TT|0.30']['Nu_trunc']['max_abs_rel'] - 3.1412471746919506e-15) < 1e-27
       and abs(H['worst_spectrum_difference'] - 3.1412471746919506e-15) < 1e-27
       and sorted(H['settings_survive']) == ['Nu_approx', 'Nu_best', 'Nu_int', 'Nu_trunc']
       and all(H['settings_survive'][k] == k for k in H['settings_survive'])),
      'all four settings survive and echo back; trunc==approx==best everywhere; worst '
      'hierarchy-vs-truncated spectrum difference %.6e' % H['worst_spectrum_difference'])

# ───────────────────────────────────────────── Ⓕ⑥ the amplitudes, and 69's question answered
check("⛭⛭⛭ `r7879` ** ⑯ Ⓕ⑥ **`A` MOVES BY `7.993606e-15` BETWEEN HIERARCHY AND FLUID "
      "APPROXIMATION, AND `ε` BY EXACTLY ZERO -- `2.665e-13` OF `69`'s `0.03` BAR** ** ⇒ *** eight "
      "comparisons, TT and EE at both sums against both truncated arms. Worst `|ΔA|` is "
      "`7.993606e-15`; `|Δε|` is `0.0` throughout; `0` of `8` clear my own interpolation floors. ** "
      "`69` asked how much of `60`'s leverage gap a full hierarchy can be expected to close. **NONE "
      "THAT CAN BE MEASURED** -- the gap `60` need is `10.8` in TT:EE leverage at `Σ = 0.30`, and "
      "the difference between CAMB's two treatments is thirteen orders of magnitude below the bar "
      "that judges it. *** ⌗ *`69` asked specifically 'whether that difference is as small in `A` "
      "and `ε`, and where it is not'. It is as small, and there is nowhere it is not*",
      (abs(H['worst_dA'] - 7.993605777301127e-15) < 1e-27
       and H['n_above_floor'] == 0
       and len(H['differences']) == 8
       and all(v['deps'] == 0.0 for v in H['differences'].values())
       and abs(H['bar'] - 0.03) < 1e-12
       and H['worst_dA'] / H['bar'] < 1e-12),
      'worst |dA| %.6e over %d comparisons, all |deps| zero, %d above my floors; %.3e of the '
      '%.2f bar' % (H['worst_dA'], len(H['differences']), H['n_above_floor'],
                    H['worst_dA'] / H['bar'], H['bar']))

# ───────────────────────────────────────────── Ⓖ⑦ the distinction not claimed
check("⛭⛔⛭ `r7879` ** ⑯ Ⓖ⑦ **WHAT THIS DOES **NOT** ESTABLISH: WHETHER THE TWO TREATMENTS AGREE TO "
      "MACHINE PRECISION OR WHETHER THE SWITCH IS **INERT** HERE -- I CANNOT SEPARATE THOSE FROM "
      "OUTSIDE CAMB ** ⇒ *** `Nu_trunc`, `Nu_approx` and `Nu_best` being BIT-IDENTICAL is the "
      "signature of three settings taking the same code path, not of three treatments converging. "
      "** So the supported claim is the weaker one: the treatments are not measurably different **as "
      "the setting is exposed at these parameters**. `69`'s practical answer is the same either way "
      "-- no measurable leverage from a hierarchy -- but the two readings are different claims and "
      "only one is evidenced. *** ⌗ *Stated because the stronger reading would license a conclusion "
      "about hierarchy physics that this measurement cannot carry: it would say CAMB's integrator "
      "and its fluid approximation agree, when what was shown is that CAMB returned the same array*",
      (H['any_identical_to_hierarchy'] is True
       and all(_liv[k]['trunc_vs_approx_identical'] for k in _liv)
       and H['worst_dA'] < min(H['floors'].values())),
      'at least one truncated arm is bit-identical to the hierarchy, and all three truncated '
      'settings are bit-identical to each other -- the signature of a shared code path')

# ───────────────────────────────────────────── Ⓗ⑧ the r7871 figure, reconciled not overwritten
check("⛭⛔⛭ `r7879` ** ⑯ Ⓗ⑧ **MY `r7871` FIGURE OF `7.305730e-08` IS NOT CORRECTED BY THIS "
      "REVISION'S `3.141247e-15`: THE TWO MEASURE DIFFERENT CONFIGURATIONS ** ⇒ *** `69`'s order "
      "cites my `r7871` result as *about `6e-6`*; my record says `7.305730e-08`, two orders of "
      "magnitude smaller, and this revision measures `3.141247e-15`. ** `r7871` compared the four "
      "methods on **LENSED** spectra over `ℓ = 100`--`1996`, where the lensing is reconstructed per "
      "method; this item uses **UNLENSED** spectra over `ℓ = 100`--`420`, as `60` do. Both are mine, "
      "both are negligible, and the configurations differ. *** ⌗ *Recorded so the smaller number "
      "does not read as a correction of the larger. A figure superseded by a measurement in a "
      "different configuration has not been found wrong, and saying so costs nothing while the "
      "alternative quietly discredits a record that stands*",
      (abs(H['r7871_spread'] - 7.305729821105444e-08) < 1e-20
       and H['worst_spectrum_difference'] < H['r7871_spread']
       and H['window'] == [100, 420]),
      'r7871 measured %.6e on lensed spectra to l=1996; this item measures %.6e unlensed over '
      'l=%d-%d' % (H['r7871_spread'], H['worst_spectrum_difference'],
                   H['window'][0], H['window'][1]))

# ───────────────────────────────────────────── the count arm
check("⛭ `r7879` ** Ⓘ⑨ THE ARMS ABOVE ARE **ALL OF THEM** ** ⇒ *** eight arms precede this one: "
      "four on item ⑮ and four on item ⑯. *** ⌗ *A receipt that loses an arm to an editing slip "
      "reports fewer failures than it has*",
      _n[0] == 8,
      '%d arm(s) before this one' % _n[0])

print('\n' + '=' * 100)
print('  %d arm(s), %d failed' % (_n[0], _fail[0]))
print('=' * 100)
sys.exit(1 if _fail[0] else 0)
