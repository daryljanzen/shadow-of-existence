"""P15 -- THE NULL HARNESS, NOW LOAD-BEARING FOR `PO-56`'s EXIT, GIVEN ONE PASS OF ITS OWN (node 70, `r7035`).

`r7029` built the instrument-noise null: the control fit plus a draw from N(0, COV), the likelihood's own
covariance, pushed through the whole estimator.  `cc66.66` scored its three projections against it and reversed
`cc66.65` on it.  It assumes the likelihood's COV IS the noise.
** a) What does that assumption buy, and what would it cost if it were wrong?  b) Can the harness give an
uncertainty on a RATIO of two projected amplitudes and on a PHASE OFFSET -- what the accounting will quote? **

** a) IT BUYS EVERY CLEARANCE BUT ONE. **
  * Held design: the ESTIMATOR is fixed (F stays the likelihood's metric, as the paper defines the statistic); only
    the covariance the noise is DRAWN from varies.  Diagonal alone; every correlation at the flat 0.15 floor
    `cc66.62` measured; that floor at lags 1-7 only; COV rescaled.
  * The arm's a(1.00) and `cc66.66`'s projections a) and b) clear under EVERY variant, pooled or not, by margins
    the variants never approach.
  * ** The misplaced part c) does not.**  Pooled over 20,000 draws it clears the likelihood's COV (0 reach it) and
    fails the pre-registered bar under the lags-1-7 floor: 26 of 20,000 reach it, p = 1.3e-3.  Still below one
    per cent, but it is the ONE clearance the assumption decides.
  * ** And `cc66.66`'s 1.44x is the favourable end of its own seed spread. **  Its seed reproduces it exactly;
    ten other seeds of 2,000 give 1.10x to 1.37x, because the maximum of 2,000 draws is itself a noisy statistic.
    The pooled tail count is the stable number, and on it c) still clears the likelihood's COV.
  * RESCALING DOES NOT MATTER; STRUCTURE DOES.  The repository measures the noise scale -- its fitted LCDM control
    returns chi2 206.4 over 210 degrees of freedom, 0.98 +- 0.10 -- and the smallest variance inflation at which any
    draw reaches c) is 2.5, fifteen widths away.  (The harness's own control returns 3.3 per degree of freedom,
    but that is theory misfit -- the control is a theory spectrum, not fitted to the data -- and is not read as a
    rescale.)  The sqrt(s) law the pre-registration assumed FAILS: each draw is
    a FIXED part (the noise-free quadratic term) plus noise, and only the noise scales, so the margin is measured
    by a scan, not the formula.
  * ⇒ *** THE MARGIN: A CLEARANCE NEEDS ITS OBSERVED VALUE ABOVE ABOUT ONE AND A HALF TIMES THE LIKELIHOOD-COV
    NULL'S MAXIMUM BEFORE THE ASSUMPTION STOPS MATTERING -- the largest structural inflation of the null maximum
    is 1.46x.  The arm and a) and b) sit at 2.0x and above; c) sits at 1.1x to 1.4x. ***

** b) YES AT THE EXCESS, AND AT THE SPECTRUM THERE IS NOTHING TO FLOOR. **
  * The null CANNOT give them as a null: it is built with the signal absent.  Its cross-term phase is uniform
    (Rayleigh p = 0.20); its excess phase is not, and that is the fixed quadratic term (amplitude 1.06 in every
    draw), which `r7029` declared -- not a leak.  A ratio or a phase needs the same noise model used as a
    PERTURBATION about the observed data, and that is what is measured here.
  * AT THE SPECTRUM LEVEL -- `cc66.65`'s accounting instrument -- THE FLOORS ARE NEGLIGIBLE: phase offsets to
    4e-4 rad, ratios to 1e-3 relative.  The spectrum difference moves with the data only through two fitted
    scalars.  ⇒ *** The window's 0.264 and +0.27 rad are properties of the two THEORIES, with no statistical floor.
    A share built from them is exact up to the construction, and its honest uncertainty is SYSTEMATIC. ***
  * AT THE EXCESS LEVEL -- where the noise lives -- THE FLOORS ARE FINITE AND LINEAR: phase offsets to about
    0.05 rad and ratios to 0.015 (window) and 0.030 (term mix).  Half the noise doubled matches the full noise to
    one per cent, and the delta method from the joint covariance matches direct perturbation to one per cent.  So
    the floor on ANY residue `arm - k * channel` at fixed k follows from one 6x6 matrix, which is recorded.

⛔ NOT CLAIMED: no accounting is run.  No central value of the term mix's ratio, phase or share is printed -- that is
`cc66`'s, because it owns the instrument; spreads only.  No channel, no mechanism, no re-scoring, no physics, and no
verdict on `cc66`'s results: c)'s dependence on the assumption and the seed spread of its multiple are ROUTED, not
applied.  No `cc66` receipt, bank or transfer is touched.

Written r7035 by node 70.  Stated for reversal.
"""
import os
import runpy

import numpy as np

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7035_70_harness_audit')
HDR = ' '.join(__doc__.split())
PRE = ' '.join(open(os.path.join(WORK, 'PREDICTION.md'), encoding='utf-8').read().split())

print('=' * 100)
print('THE AUDIT, RUN IN-PROCESS FROM ITS COMMITTED SCRIPT (nothing written back)')
print('=' * 100)
os.environ['AUDIT_NOWRITE'] = '1'
os.environ.setdefault('NDRAW', '2000')
G = runpy.run_path(os.path.join(WORK, 'audit_harness.py'), run_name='__audit__')
OUT, OBS, QN = G['OUT'], G['OBS'], G['QN']
A = OUT['A']
ARM, QA, QB_, QC = QN

print('\n' + '=' * 100)
print('THE GATES')
print('=' * 100)
print('\nPART 0 -- THE PRE-REGISTRATION CAME FIRST, AND THE HARNESS IS THE ONE `cc66.66` SCORED ON.')
check("the pre-registration fixed the design (estimator held, DRAWING covariance varied) and the bars before the "
      "script existed",
      'estimator is held fixed' in PRE and 'covariance the noise is DRAWN from' in PRE
      and '0 of 2,000 draws reach the observed value' in PRE)
check("⛭ the harness reproduces the arm's a(1.00) and, on `cc66.66`'s own seed and draw order, its published "
      "multiples 2.26, 2.83 and 1.44 exactly",
      abs(OBS[0] - 7.304) < 0.002
      and np.allclose(OUT['repro_cc66_66']['obs_over_max'][1:], [2.26, 2.83, 1.44], atol=0.005),
      f"a(1.00) {OBS[0]:.4f}; multiples {np.round(OUT['repro_cc66_66']['obs_over_max'][1:], 3).tolist()}")

print('\nPART ⓐ -- THE ASSUMPTION, VARIED.')
V0, V1, V2, V3 = ('V0 likelihood COV', 'V1 diagonal alone', 'V2 flat 0.15, all pairs', 'V3 flat 0.15, lags 1-7')
check("on the likelihood's own COV all four clear: 0 of 2,000 reach any observed value",
      all(A[V0][q]['ge'] == 0 for q in QN), {q: A[V0][q]['ge'] for q in QN})
check("⛭ the arm, a) and b) SURVIVE THE ASSUMPTION: 0 of 2,000 reach them under the diagonal, the flat plateau "
      "AND the flat floor at lags 1-7",
      all(A[v][q]['ge'] == 0 for v in (V1, V2, V3) for q in (ARM, QA, QB_)),
      {v[:2]: [A[v][q]['obs_over_max'] for q in (ARM, QA, QB_)] for v in (V1, V2, V3)})
check("⛔⛭ AND c), THE MISPLACED PART, DOES NOT: it survives the diagonal and the plateau but draws reach it under "
      "the lags-1-7 floor -- the one clearance the assumption decides",
      A[V1][QC]['ge'] == 0 and A[V2][QC]['ge'] == 0 and A[V3][QC]['ge'] > 0,
      f"V1 {A[V1][QC]['ge']}, V2 {A[V2][QC]['ge']}, V3 {A[V3][QC]['ge']} of {OUT['ndraw']}")
PV0, PV3 = A['pooled'][V0], A['pooled'][V3]
check("⌗ pooled over 20,000 draws: c) clears the likelihood's COV outright and, under the lags-1-7 floor, lands "
      "between 1e-4 and 1e-2 -- below one per cent, not clear of it",
      PV0[QC]['ge'] == 0 and PV0[QC]['n'] == 20000 and 1e-4 < PV3[QC]['p'] < 1e-2,
      f"V0 {PV0[QC]['ge']} of {PV0[QC]['n']}; V3 {PV3[QC]['ge']} of {PV3[QC]['n']}, p {PV3[QC]['p']:.1e}")
check("and pooled, the arm, a) and b) are reached by NO draw under either",
      all(A['pooled'][v][q]['ge'] == 0 for v in (V0, V3) for q in (ARM, QA, QB_)))
SS = A['seed_spread_of_max'][V0][QC]['obs_over_max_range']
check("⛭ `cc66.66`'s 1.44x for c) is the FAVOURABLE END of its own seed spread: ten other seeds of 2,000 give "
      "multiples wholly below it, because the maximum of 2,000 draws is itself a noisy statistic",
      OUT['repro_cc66_66']['obs_over_max'][3] > SS[1] and SS[1] - SS[0] > 0.15,
      f"ten seeds {SS[0]:.2f}x - {SS[1]:.2f}x against 1.44x")
SQ = A['sqrt_law']
check("⚠ the sqrt(s) law the pre-registration assumed FAILS, so its s* formula is kept for the record and NOT used "
      "-- each draw is a fixed noise-free part plus noise, and only the noise scales",
      all(abs(r - 1.0) > 0.2 for r in SQ['0.5'] + SQ['2.0']),
      f"median ratio / sqrt(s): s=0.5 {np.round(SQ['0.5'], 2).tolist()}, s=2 {np.round(SQ['2.0'], 2).tolist()}")
SM = A['s_star_measured']
check("⛭ so the rescale margin is measured by a scan: c) is first reached at a variance inflation of at most 3, "
      "the other three at no less than 12",
      SM[QC]['first_s_any_draw_reaches'] is not None and SM[QC]['first_s_any_draw_reaches'] <= 3.0
      and all((SM[q]['first_s_any_draw_reaches'] or 99) >= 12.0 for q in (ARM, QA, QB_)),
      {q[:2]: SM[q]['first_s_any_draw_reaches'] for q in QN})
SH = A['s_hat']
check("⛭ AND RESCALING IS NOT WHERE THE RISK IS: the repository measures the noise scale -- the fitted LCDM control's "
      "chi2 per degree of freedom -- and c)'s threshold sits more than ten widths above it",
      SH['prov_states'] and abs(SH['s_hat'] - 0.983) < 0.01
      and (SM[QC]['first_s_any_draw_reaches'] - SH['s_hat']) / SH['width'] > 10,
      f"s_hat {SH['s_hat']:.3f} +- {SH['width']:.3f}; c) first reached at s = {SM[QC]['first_s_any_draw_reaches']}")
check("⛔ and the harness's own control is NOT a noise estimate -- its chi2/nu is theory misfit, and it is reported "
      "as that rather than read as a rescale",
      A['control_chi2_per_nu_NOT_a_noise_scale'] > 2.0 and 'theory misfit' in HDR,
      f"{A['control_chi2_per_nu_NOT_a_noise_scale']:.2f}")
ST = A['struct_max_ratio']
INFL = max(max(v) for v in ST.values())
check("⇒ *** THE MARGIN: the largest structural inflation of the null maximum is under 1.5x, so a clearance above "
      "about 1.5x the likelihood-COV maximum is safe from the assumption -- the arm, a) and b) are; c) is not ***",
      1.3 < INFL < 1.5 and all(A['seed_spread_of_max'][V0][q]['obs_over_max_range'][0] > 1.9 for q in (ARM, QA, QB_))
      and SS[1] < 1.5,
      f"largest inflation {INFL:.2f}x; lowest seed multiple: arm/a/b "
      f"{[round(A['seed_spread_of_max'][V0][q]['obs_over_max_range'][0], 2) for q in (ARM, QA, QB_)]}, c {SS[0]:.2f}")

print('\nPART ⓑ -- A RATIO AND A PHASE.')
NP = OUT['B_null_phase']
check("the null cannot supply them AS A NULL: the noise-carrying cross term's phase is uniform under it",
      NP['cross term alone']['rayleigh_p'] > 0.05, f"Rayleigh p {NP['cross term alone']['rayleigh_p']:.2f}")
check("⚠ and the excess's null phase is NOT uniform -- found running it and pre-registered as a leak -- because the "
      "quadratic term is FIXED in every draw, at about the null's own median; `r7029` declared that term noise-free",
      NP['excess (quad + cross)']['Rbar'] > 0.5 and abs(NP['quad_fixed_amp'] - 1.06) < 0.02
      and abs(NP['quad_fixed_amp'] - A[V0][ARM]['median']) < 0.1,
      f"mean resultant {NP['excess (quad + cross)']['Rbar']:.2f}; fixed quad {NP['quad_fixed_amp']:.3f} against "
      f"null median {A[V0][ARM]['median']:.3f}")
B = OUT['B']
check("⛭⛭ AT THE SPECTRUM LEVEL -- the accounting's own instrument -- THE FLOORS ARE NEGLIGIBLE by the "
      "pre-registered bar: phase below 0.01 rad, ratio below one per cent relative",
      all(B[f'd {c}/arm']['phase_sd'] < 0.01 for c in ('window', 'term mix'))
      and B['d window/arm']['ratio_rel_sd'] < 0.01 and B['d term mix/arm']['ratio_sd'] < 0.01,
      f"window phase {B['d window/arm']['phase_sd']:.1e} rad, ratio {B['d window/arm']['ratio_rel_sd']:.1e} rel; "
      f"term mix phase {B['d term mix/arm']['phase_sd']:.1e} rad, ratio {B['d term mix/arm']['ratio_sd']:.1e}")
check("⇒ *** and the window's published 0.264 and +0.27 rad are recovered as the perturbation's centres -- properties "
      "of the two theories, with no statistical floor ***",
      abs(B['d window/arm']['ratio_obs'] - 0.264) < 0.001 and abs(B['d window/arm']['phase_obs'] - 0.27) < 0.005
      and abs(B['d window/arm']['ratio_med'] - B['d window/arm']['ratio_obs']) < 3 * B['d window/arm']['ratio_sd'],
      f"ratio {B['d window/arm']['ratio_obs']:.4f}, phase {B['d window/arm']['phase_obs']:+.3f} rad")
check("⛭ AT THE EXCESS LEVEL THE FLOORS ARE FINITE: phase offsets to about 0.05 rad, ratios to a few hundredths",
      all(0.02 < B[f'ex {c}/arm']['phase_sd'] < 0.1 for c in ('window', 'term mix'))
      and all(0.005 < B[f'ex {c}/arm']['ratio_sd'] < 0.05 for c in ('window', 'term mix')),
      {c: (round(B[f'ex {c}/arm']['phase_sd'], 4), round(B[f'ex {c}/arm']['ratio_sd'], 4))
       for c in ('window', 'term mix')})
check("and LINEAR by the pre-registered bar: half the noise, doubled, is within ten per cent of the full spread",
      all(abs(B[k]['lin_ratio'] - 1) < 0.1 and abs(B[k]['lin_phase'] - 1) < 0.1 for k in B),
      {k: (round(B[k]['lin_ratio'], 3), round(B[k]['lin_phase'], 3)) for k in B})
DW = OUT['B_delta_window']
check("⛭ and the delta method from the joint 6x6 covariance matches direct perturbation within fifteen per cent, "
      "so the floor on ANY residue arm - k*channel follows from the recorded matrix",
      abs(DW['agree_ratio'] - 1) < 0.15 and abs(DW['agree_phase'] - 1) < 0.15 and len(OUT['B_cov6']) == 6,
      f"ratio {DW['agree_ratio']:.3f}, phase {DW['agree_phase']:.3f}")
RF = OUT['B_residue_sigma_component']
check("⌗ the residue floor is tabled on a grid of k, not at a fitted k -- per component it stays between 0.2 and 0.5",
      all(0.2 < v < 0.5 for c in RF.values() for v in c.values()), RF)

print('\nPART ⛔ -- THE LIMITS, AS WRITTEN.')
check("no central value of the term mix's ratio, phase or share is computed into the record -- spreads only",
      all('ratio_obs' not in B[f'{lv} term mix/arm'] and 'phase_obs' not in B[f'{lv} term mix/arm']
          and 'ratio_rel_sd' not in B[f'{lv} term mix/arm'] for lv in ('d', 'ex')))
check("and the header says no accounting is run, and routes c)'s dependence and the seed spread rather than applying "
      "them",
      'no accounting is run' in HDR and 'ROUTED, not applied' in HDR and 'No `cc66` receipt, bank or transfer' in HDR)

print('\n' + '=' * 100)
if FAILS:
    print(f"VERDICT: {len(FAILS)} CHECK(S) FAILED")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("VERDICT: ALL PASS -- the harness survives its one assumption for the arm, a) and b); c), the misplaced part,")
print("         is the one clearance the assumption decides, and its 1.44x is the favourable end of its seed spread.")
print("         A ratio or phase is floored at the excess (about 0.05 rad) and has no statistical floor at the")
print("         spectrum, where the accounting's own instrument lives.")
