# -*- coding: utf-8 -*-
"""⛭⛔⛭ `r7873+cc66` ** ⑪ THE TWO-START SCAN FINDS **ONE BASIN ON BOTH RULERS** AT `Σ = 0.400` --
BUT **AT THAT SUM ONLY**, SO `r7869`'s "ONE BRANCH TO `0.60` eV" IS STILL UNESTABLISHED AND `60`'s
OBJECTION STANDS. ⑫ CAMB's SUM RESPONSE **BY SOURCE TERM** CLOSES EXACTLY AND IS **NOT UNIFORM**:
`ISW` CARRIES `0.2918` OF THE RESPONSE ON `0.1361` OF THE SPECTRUM -- `×2.14` ITS WEIGHT -- AND
`0.945356` OF THAT IS THE **EARLY** `ISW`, NOT THE LATE ONE **

COMPUTES: nothing.  Every figure is read out of the three JSON records this revision's drivers
wrote (`two_start.json`, `basin_detail.json`, `source_terms.json`).  No parameter is pinned here.

⌗ THREE REGISTRATION DEFECTS OF MY OWN ARE RECORDED BELOW RATHER THAN REPAIRED QUIETLY, because a
criterion rewritten after it fires has measured nothing:

  `Ⓒ③` of ⑪ -- the registered `χ²` bound sat between the minimiser's stopping rule and its actual
  run-to-run scatter, so it was guaranteed to fire on the noisier ruler and not the quieter one.

  `Ⓔ⑤` of ⑪ -- the midpoint discriminator I added to settle the matter had **no scale**, and so
  called a barrier a hundredth of `fatol` a second basin.

  `Ⓒ③` of ⑫ -- the registered closure arithmetic summed four AUTO spectra, which cannot close
  because `C_ℓ` is quadratic in the source; it would have closed the item on an error of mine.

⌗ `Ⓔ⑤` of ⑫ declares a DEPARTURE from the registration: `Ⓘ⑨` says read no term if the path control
fails, the path control DOES fail at `1.976630e-03`, and the terms are read anyway on a measured
ground stated there.  `69` should judge that departure rather than discover it.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7873_cc66_the_two_start_basin_test_and_cambs_response_by_source_term')

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

TS = load(os.path.join(MINE, 'two_start.json'))
BD = load(os.path.join(MINE, 'basin_detail.json'))
ST = load(os.path.join(MINE, 'source_terms.json'))
_rc, _rm = BD['modes']['rd_camb'], BD['modes']['rd_min']
_tc, _tm = TS['modes']['rd_camb'], TS['modes']['rd_min']

# ───────────────────────────────────────────── Ⓐ① the starts and the banked points are 60's, read
check("⛭ `r7873` ** ⑪ Ⓐ① THE TWO STARTS ARE **60's OWN BASIN FIGURES** AND THE OTHER FOUR "
      "PARAMETERS ARE **READ FROM THE BANKED RECORD, NOT RETYPED** -- AND BOTH RUNS ON BOTH RULERS "
      "CONVERGE **INTERIOR** TO THE BOX ** ⇒ *** `H0` is started at `65.29` and `68.59`, 60's own "
      "figures for the two basins they reported, with `Ω_m`, `ω_b`, `n_s` and `τ` each set to the "
      "banked `Σ = 0.400` best fit **for that ruler** -- `rd_camb` at `H0 = 66.80438680` with "
      "`χ² = 690.59935803`, `rd_min` at `H0 = 64.97100670` with `χ² = 650.26603753`. ** Both runs "
      "on both rulers land strictly inside `BOX`, so no verdict below is a boundary artefact, and "
      "both re-score to their banked `χ²` with **zero drift**. *** ⌗ *A start read from the record "
      "cannot drift from the instrument's; a retyped one can*",
      (abs(TS['h0_starts'][0] - 65.29) < 1e-12 and abs(TS['h0_starts'][1] - 68.59) < 1e-12
       and abs(_tc['banked']['H0'] - 66.80438680) < 1e-7
       and abs(_tc['banked_chi2'] - 690.59935803) < 1e-7
       and abs(_tm['banked']['H0'] - 64.97100670) < 1e-7
       and abs(_tm['banked_chi2'] - 650.26603753) < 1e-7
       and _tc['both_interior'] is True and _tm['both_interior'] is True
       and max(_rc['rescore_drift']) == 0.0 and max(_rm['rescore_drift']) == 0.0),
      'rd_camb banked H0 %.8f chi2 %.8f; rd_min banked H0 %.8f chi2 %.8f; both interior; '
      'rescore drift %s and %s'
      % (_tc['banked']['H0'], _tc['banked_chi2'], _tm['banked']['H0'], _tm['banked_chi2'],
         _rc['rescore_drift'], _rm['rescore_drift']))

# ───────────────────────────────────────────── Ⓑ② the registered criterion gave TWO verdicts
check("⛭⛔⛭ `r7873` ** ⑪ Ⓑ② **THE REGISTERED CRITERION RETURNS A DIFFERENT VERDICT ON EACH RULER -- "
      "`rd_min` **ONE BRANCH**, `rd_camb` **THE THIRD OUTCOME** -- AND THE DISAGREEMENT IS NOT ABOUT "
      "`H0`, WHICH BOTH RULERS PUT IN THE SAME PLACE TO UNDER FOUR THOUSANDTHS ** ⇒ *** applied "
      "exactly as registered. `rd_min`: `|ΔH0| = 0.00058711` and `|Δχ²| = 0.00000658`, both inside "
      "the same-branch bounds, so **ONE BRANCH**. `rd_camb`: `|ΔH0| = 0.00387394`, well inside the "
      "`0.5` bound, but `|Δχ²| = 0.08595087`, outside the `0.01` bound -- so it fails the "
      "same-branch test, fails the two-branch test (`|ΔH0|` is nowhere near `2.0`), and lands in "
      "60's third outcome. ** THE TWO RULERS DIFFER BY A FACTOR `13057` IN `|Δχ²|` AND BY ONLY "
      "`6.6×` IN `|ΔH0|`: the registered disagreement is about how well `χ²` CONVERGED, not about "
      "where the basin is. *** ⌗ *Reported as registered before being superseded, because a "
      "criterion that is rewritten after it fires has measured nothing*",
      (abs(TS['criterion']['same_dh0'] - 0.5) < 1e-12
       and abs(TS['criterion']['same_dchi2'] - 0.01) < 1e-12
       and abs(TS['criterion']['two_dh0'] - 2.0) < 1e-12
       and abs(TS['criterion']['two_dchi2'] - 0.01) < 1e-12
       and _tc['verdict'] == 'THE THIRD OUTCOME' and _tm['verdict'] == 'ONE BRANCH'
       and abs(_tc['dh0'] - 0.00387394) < 1e-7 and abs(_tc['dchi2'] - 0.08595087) < 1e-7
       and abs(_tm['dh0'] - 0.00058711) < 1e-7 and abs(_tm['dchi2'] - 0.00000658) < 4e-9
       and _tc['dh0'] < 0.5 and _tc['dchi2'] > 0.01
       and _tm['dh0'] < 0.5 and _tm['dchi2'] < 0.01
       and abs(_tc['dchi2'] / _tm['dchi2'] - 13057.0) < 20.0
       and abs(_tc['dh0'] / _tm['dh0'] - 6.598) < 0.02),
      'rd_camb |dH0| %.8f < 0.5 but |dchi2| %.8f > 0.01 -> %s; rd_min |dH0| %.8f |dchi2| %.8f '
      '-> %s; chi2 ratio %.0f, H0 ratio %.3f'
      % (_tc['dh0'], _tc['dchi2'], _tc['verdict'], _tm['dh0'], _tm['dchi2'], _tm['verdict'],
         _tc['dchi2'] / _tm['dchi2'], _tc['dh0'] / _tm['dh0']))

# ───────────────────────────────────────────── Ⓒ③ what the registered threshold actually was
check("⛭⛔⛭ `r7873` ** ⑪ Ⓒ③ **THE REGISTERED `χ²` THRESHOLD SAT BETWEEN THE MINIMISER'S STOPPING "
      "RULE AND ITS ACTUAL RUN-TO-RUN SCATTER, WHICH IS WHY IT FIRED** -- `fatol` IS A STOPPING RULE "
      "ON THE SIMPLEX SPREAD, **NOT A BOUND ON THE ACHIEVED MINIMUM** ** ⇒ *** "
      "`profile_likeforlike.profile` minimises five free parameters with Nelder-Mead at "
      "`fatol = 5e-3`, `xatol = 1e-3`. The registered same-branch bound is `0.01`, which is `2×` "
      "`fatol` -- so it is NOT tighter than the tolerance, and saying so would be wrong. What it IS "
      "tighter than is the measured reproducibility: `rd_camb`'s two independent runs differ by "
      "`0.08595087`, **`17.190174×` `fatol`**, because a simplex that has stopped shrinking is not a "
      "simplex that has found the floor. ** My threshold sat between `5e-3` and `0.086`, so it was "
      "guaranteed to fire on the noisier ruler and not on the quieter one. *** ⌗ *A registration "
      "defect of mine. Stated precisely rather than approximately: an earlier commit message of "
      "mine called `0.01` 'tighter than the convergence tolerance', and that was imprecise*",
      (abs(_tc['dchi2'] / 5e-3 - 17.190174) < 1e-4
       and _tc['dchi2'] > 5e-3 and 0.01 > 5e-3
       and abs(0.01 / 5e-3 - 2.0) < 1e-12
       and _tm['dchi2'] < 5e-3),
      'fatol 5e-3; registered bound 0.01 = 2x fatol; rd_camb scatter %.8f = %.6fx fatol; '
      'rd_min scatter %.8f is BELOW fatol'
      % (_tc['dchi2'], _tc['dchi2'] / 5e-3, _tm['dchi2']))

# ───────────────────────────────────────────── Ⓓ④ the midpoint discriminator on rd_camb
check("⛭⛭⛭ `r7873` ** ⑪ Ⓓ④ **THE MIDPOINT DISCRIMINATOR SETTLES `rd_camb` WITHOUT DEPENDING ON "
      "CONVERGENCE PRECISION AT ALL: THE MIDPOINT SCORES `0.05522985` **BELOW** THE WORSE ENDPOINT, "
      "SO THE TWO CONVERGED POINTS SIT IN **ONE CONVEX BASIN** ** ⇒ *** a basin is convex near its "
      "floor, so the midpoint of two points inside one basin scores at or below the worse of them, "
      "and a midpoint ABOVE both is a barrier. Scoring the midpoint of `rd_camb`'s two converged "
      "`5`-parameter points gives `690.60965364` against endpoints `690.66488348` and "
      "`690.57893261`: **below the worse by `0.05522985`**, which is `11.045970×` `fatol` below, not "
      "a marginal call. ** This is a GEOMETRIC statement about the surface and is immune to the "
      "`Ⓒ③` problem entirely -- it does not ask the minimiser for any precision. *** ⌗ *`rd_camb`'s "
      "`χ²` gap lives in `τ`, whose separation `0.00146063` is the largest of the four non-`H0` "
      "parameters by more than an order of magnitude. The two runs found the same `H0` "
      "and stopped at different `τ` on one floor*",
      (_rc['midpoint_minus_worse'] < 0.0
       and abs(_rc['midpoint_minus_worse'] - (-0.055229848417639005)) < 1e-12
       and abs(_rc['excess_over_fatol'] - (-11.045969683527801)) < 1e-9
       and abs(_rc['midpoint_chi2'] - 690.6096536363771) < 1e-9
       and abs(_rc['chi2'][0] - 690.5789326140299) < 1e-9
       and abs(_rc['chi2'][1] - 690.6648834847947) < 1e-9
       and _rc['one_basin'] is True and _rc['ridge_that_matters'] is False
       and abs(_rc['separations']['tau'] - 0.0014606347258273034) < 1e-15
       and _rc['separations']['tau'] == max(v for k, v in _rc['separations'].items()
                                           if k != 'H0')),
      'midpoint %.8f is %.8f BELOW the worse endpoint %.8f (%.6fx fatol); tau separation '
      '%.8f is the largest non-H0 one'
      % (_rc['midpoint_chi2'], -_rc['midpoint_minus_worse'], max(_rc['chi2']),
         -_rc['excess_over_fatol'], _rc['separations']['tau']))

# ───────────────────────────────────────────── Ⓔ⑤ the discriminator's OWN defect, recorded
check("⛭⛔⛭ `r7873` ** ⑪ Ⓔ⑤ **THE FIRST VERSION OF THAT DISCRIMINATOR HAD **NO SCALE** AND SO "
      "REPORTED `rd_min` AS *TWO BASINS* ON A BARRIER OF `4.833800e-05` -- A HUNDREDTH OF THE "
      "MINIMISER'S OWN `fatol`, BETWEEN TWO POINTS AGREEING TO `1e-5` IN EVERY PARAMETER ** ⇒ *** "
      "it tested `midpoint > worse` against **ZERO**. `rd_min`'s midpoint does exceed its worse "
      "endpoint, by `+0.00004834`, so the unscaled test fired: `TWO BASINS` on a ruler whose two "
      "starts had just converged to the same point in all five parameters. That verdict would have "
      "been **false and physically absurd**, and it was mine, not the likelihood's. ** Scaled, the "
      "excess is `0.009668` of `fatol` and `4.833800e-05` of the one-parameter unit `Δχ² = 1`. A "
      "barrier under either scale is **not a basin boundary**. *** ⌗ *The `Ⓗ⑧` lesson of item ⑫ in "
      "a second costume: a comparison is readable only against a scale that matters. Recorded as a "
      "defect rather than silently widened, because a test whose threshold is chosen after seeing "
      "the answer has measured nothing*",
      (_rm['midpoint_above_both'] is True
       and abs(_rm['midpoint_minus_worse'] - 4.8338003807657515e-05) < 1e-18
       and abs(_rm['excess_over_fatol'] - 0.009667600761531503) < 1e-12
       and _rm['excess_over_fatol'] < 1.0
       and _rm['ridge_that_matters'] is False and _rm['one_basin'] is True
       and max(v for k, v in _rm['separations'].items() if k != 'H0') < 1e-4),
      'rd_min midpoint exceeds the worse endpoint by %+.8e, which is %.6f of fatol and %.3e of '
      'dchi2=1; its non-H0 separations are all below %.1e'
      % (_rm['midpoint_minus_worse'], _rm['excess_over_fatol'],
         _rm['midpoint_minus_worse'], 1e-4))

# ───────────────────────────────────────────── Ⓕ⑥ the answer, and its scope
check("⛭⛭⛭ `r7873` ** ⑪ Ⓕ⑥ **THE ANSWER TO 60: **ONE BASIN ON BOTH RULERS AT `Σ = 0.400`** -- BUT "
      "**AT `Σ = 0.400` ONLY**, SO `r7869`'s 'ONE BRANCH TO `0.60` eV' IS **STILL NOT ESTABLISHED** "
      "AND 60's OBJECTION STANDS ** ⇒ *** on the geometric test both rulers read one basin: "
      "`rd_camb` because its midpoint is `0.055230` below the worse endpoint, `rd_min` because its "
      "two starts converged to the same point to `0.00058711` in `H0` and under `1e-5` in every "
      "other parameter -- which is a stronger statement than any midpoint test, since the starts "
      "did not merely share a basin, they found the same point. ** THE SCOPE IS ONE SUM. 60's "
      "objection was that `r7869` held each ruler's best fit and **no branch scan**, so 'one branch "
      "to `0.60` eV' claimed more than the record showed. This revision scans `Σ = 0.400` and "
      "nothing else: it removes the two-basin worry **at that sum** and leaves the claim to "
      "`0.60` eV exactly as unestablished as 60 found it. *** ⌗ *The order asked for `0.400` and "
      "that is what was run. Saying so is the difference between answering 60 and appearing to*",
      (_rc['one_basin'] is True and _rm['one_basin'] is True
       and abs(TS['sum'] - 0.400) < 1e-12
       and len(TS['modes']) == 2
       and all(len(TS['modes'][m]['runs']) == 2 for m in TS['modes'])),
      'both rulers one basin at Sigma = %.3f; %d ruler(s), %d start(s) each; NO sum above 0.400 '
      'was scanned' % (TS['sum'], len(TS['modes']),
                       min(len(TS['modes'][m]['runs']) for m in TS['modes'])))
# ───────────────────────────────────────────── Ⓑ② the registered path control FAILS, and it stands
_pc = ST['path_control']
check("⛭⛔⛭ `r7873` ** ⑫ Ⓑ② **THE REGISTERED PATH CONTROL `Ⓘ⑨` FAILS AT `1.976630e-03` AGAINST ITS "
      "OWN `1e-3` BAND, AND THE FAILURE STANDS AS WRITTEN** -- IT IS **NEITHER A DEAD MECHANISM NOR "
      "AN ACCURACY PROBLEM**, AND IT IS **NOT** THE TROUGH ARTEFACT THAT MADE `r7871`'s `Ⓔ⑤` PASS "
      "ON A QUANTITY THAT DID NOT EXIST ** ⇒ *** the sources returned UNMODIFIED by "
      "`get_scalar_temperature_sources()` and pushed back through `set_custom_scalar_sources` give "
      "CAMB's own unlensed TT to a worst pointwise relative `1.976630e-03` over `ℓ = 100`--`420`, "
      "twice the band this seat registered. ** THREE DIAGNOSTICS SEPARATE A SETUP ERROR FROM THE "
      "MECHANISM. ⑴ It is INVARIANT to accuracy: identical to four digits across "
      "`lens_potential_accuracy` `1`..`4` and `lmax` `1200`/`2600`, so no accuracy setting moves it. "
      "⑵ The trough reading is REFUTED, not assumed: at the worst multipole `ℓ = 376` the spectrum "
      "is `0.342941` of the band maximum -- not a trough -- and the residual at TT's DEEPEST points "
      "`2.241564e-04` is **SMALLER** than at its peaks `8.106748e-04`, which is the opposite of what "
      "a zero-crossing artefact does. ⑶ CAMB's own docstring names the cause: the symbolic sources "
      "are derived *after integration by parts so that only integrated against a Bessel function*, "
      "a DIFFERENT EQUIVALENT ARRANGEMENT of the line-of-sight integral from the one CAMB's code "
      "evaluates -- two arrangements agree analytically and differ numerically. *** ⌗ *Reported as "
      "a FAILURE of my own registered band, not retrofitted to pass. The first attempt at this "
      "control failed on `gfortran: not found` -- an ENVIRONMENT gap, since the custom-source path "
      "compiles generated Fortran at run time -- and calling THAT 'CAMB cannot give it' would have "
      "invoked the order's escape clause on a missing compiler*",
      (abs(_pc['rel'] - 0.001976630289126075) < 1e-15 and _pc['ok'] is False
       and abs(_pc['band'] - 0.001) < 1e-12 and _pc['rel'] > _pc['band']
       and _pc['worst_l'] == 376
       and abs(_pc['TT_at_worst_over_max'] - 0.3429412483262532) < 1e-15
       and abs(_pc['rel_at_deepest_TT'] - 0.0002241563751519108) < 1e-18
       and abs(_pc['rel_at_highest_TT'] - 0.0008106748135913251) < 1e-18
       and _pc['rel_at_deepest_TT'] < _pc['rel_at_highest_TT']),
      'registered band %.0e; measured %.6e at l=%d where |TT| is %.6f of the band max; '
      'deepest %.6e < peaks %.6e, so NOT a trough artefact'
      % (_pc['band'], _pc['rel'], _pc['worst_l'], _pc['TT_at_worst_over_max'],
         _pc['rel_at_deepest_TT'], _pc['rel_at_highest_TT']))

# ───────────────────────────────────────────── Ⓒ③ the registered closure ARITHMETIC could not close
_c0 = ST['closure']['0']
check("⛭⛔⛭ `r7873` ** ⑫ Ⓒ③ **THE CLOSURE ARITHMETIC THIS SEAT REGISTERED COULD NOT HAVE CLOSED, "
      "BY CONSTRUCTION** -- `C_ℓ` IS **QUADRATIC** IN THE SOURCE, SO A SPLIT OF THE SOURCE INTO FOUR "
      "TERMS IS **NOT** A SPLIT OF `C_ℓ` INTO FOUR SPECTRA, AND SUMMING THE FOUR AUTO-SPECTRA MISSES "
      "**`26.683487` PER CENT** OF CAMB'S TOTAL ** ⇒ *** the driver as registered ran each term "
      "ALONE and summed the four resulting spectra. That drops every interference term. Measured "
      "against CAMB's own TT it is wrong by a worst relative `3.381711e-01` and a median "
      "`0.2668348729` at `Σ = 0`, and by the same amount at both sums -- so the registered arm would "
      "have printed `DOES NOT CLOSE` and closed item ⑫ **on an error of mine**, reporting that CAMB "
      "could not give the split when CAMB gives it exactly. *** ⌗ *The honest closure sums all "
      "SIXTEEN pairs, auto and cross, which CAMB returns in ONE run when the four terms are passed "
      "as four NAMED sources. This is recorded as a defect of the registration rather than silently "
      "repaired: `Ⓕ⑥` as written was the wrong instrument*",
      (abs(_c0['autos_vs_own'] - 0.3381710752565494) < 1e-15
       and abs(_c0['autos_median_shortfall'] - 0.2668348728775738) < 1e-15
       and _c0['autos_vs_own'] > 0.1
       and all(abs(ST['closure'][k]['autos_median_shortfall'] - 0.2668348728775738) < 2e-3
               for k in ST['closure'])),
      'four autos vs CAMB own TT: worst %.6e, median shortfall %.10f, at every sum'
      % (_c0['autos_vs_own'], _c0['autos_median_shortfall']))

# ───────────────────────────────────────────── Ⓓ④ the honest closure, and the split adds nothing
check("⛭⛭⛭ `r7873` ** ⑫ Ⓓ④ **THE SIXTEEN-PAIR CLOSURE RESIDUAL **EQUALS THE PATH CONTROL'S OWN**, "
      "SO THE SPLIT ITSELF CONTRIBUTES **NOTHING** AND THE WHOLE RESIDUAL IS THE PATH ARRANGEMENT -- "
      "AND THE FOUR ASSIGNED CONTRIBUTIONS SUM TO THE SIXTEEN-PAIR TOTAL **EXACTLY**, AT "
      "`2.728484e-12` ** ⇒ *** summing all sixteen pairs against CAMB's own unlensed TT gives "
      "`1.976630e-03` at `Σ = 0`, which is the SAME NUMBER as `Ⓑ②`'s path control to twelve "
      "significant figures. That is the arm that makes the split trustworthy despite `Ⓑ②`'s failure: "
      "if the decomposition were introducing error, the closure residual would EXCEED the path "
      "residual, and it does not. ** The four half-assigned contributions sum to the sixteen-pair "
      "total to `2.728484e-12` in `μK²` -- machine zero, exact by construction rather than by "
      "tolerance. *** ⌗ *Two independent statements: the split is internally exact, and it closes on "
      "CAMB to the path's own systematic and no worse*",
      (abs(_c0['sixteen_vs_own'] - 0.00197663028912839) < 1e-15
       and abs(_c0['sixteen_vs_own'] - _pc['rel']) < 1e-14
       and _c0['contributions_vs_sixteen'] < 1e-10
       and abs(_c0['contributions_vs_sixteen'] - 2.7284841053187847e-12) < 1e-20
       and ST['closes'] is True),
      'sixteen pairs vs own %.6e == path control %.6e (differ by %.2e); contributions vs '
      'sixteen pairs %.6e muK^2'
      % (_c0['sixteen_vs_own'], _pc['rel'], abs(_c0['sixteen_vs_own'] - _pc['rel']),
         _c0['contributions_vs_sixteen']))

# ───────────────────────────────────────────── Ⓔ⑤ the ratio control, and the declared departure
_r3, _r6 = ST['ratio_control']['0.3'], ST['ratio_control']['0.6']
check("⛭⛭⛭ `r7873` ** ⑫ Ⓔ⑤ **THE DEPARTURE IS DECLARED, NOT DISCOVERED: `Ⓘ⑨` GATES ON *ABSOLUTE* "
      "AGREEMENT WHILE EVERY NUMBER THIS ITEM REPORTS IS A *RATIO WITHIN THE PATH*, WHERE THE COMMON "
      "SYSTEMATIC CANCELS BY A FACTOR `~75` -- **MEASURED, NOT ASSUMED** ** ⇒ *** the added ratio "
      "control compares the path's own `D_ℓ(Σ)/D_ℓ(0) − 1` against CAMB's own over the same band. "
      "The `1.976630e-03` absolute systematic falls to `1.263571e-05` at `Σ = 0.30` and "
      "`2.640837e-05` at `Σ = 0.60`: `5.724463e-04` and `5.858855e-04` **OF THE RESPONSE BEING "
      "MEASURED**, inside the same `1e-3` band ON THE QUANTITY ACTUALLY REPORTED, with the two "
      "response envelopes agreeing to six digits (`0.022073` against `0.022073`). ** `Ⓘ⑨` as "
      "registered says read no term if it fails. **THE TERMS ARE READ BELOW ANYWAY, AND THAT IS A "
      "DEPARTURE FROM MY OWN REGISTRATION**, put on the record here so `69` judges it rather than "
      "finds it. *** ⌗ *`Ⓘ⑨`'s PURPOSE was to catch a mechanism that silently does nothing. That "
      "purpose is served more directly, and by three measurements a dead mechanism could not "
      "produce: this cancellation, `Ⓕ⑥`'s `26.683487`% interference, and `Ⓖ⑦`'s terms differing from "
      "one another by a factor of two*",
      (abs(_r3['frac_of_signal'] - 0.000572446297790576) < 1e-18
       and abs(_r6['frac_of_signal'] - 0.000585885534901546) < 1e-18
       and _r3['frac_of_signal'] < 0.001 and _r6['frac_of_signal'] < 0.001
       and abs(_r3['worst'] - 1.2635712655306719e-05) < 1e-20
       and abs(_r6['worst'] - 2.640836920497769e-05) < 1e-20
       and ST['ratio_control_ok'] is True
       and _pc['rel'] / _r3['frac_of_signal'] > 3.0),
      'Sigma 0.30 %.6e of signal; Sigma 0.60 %.6e of signal; the absolute systematic is %.1fx '
      'the ratio one at Sigma=0.30' % (_r3['frac_of_signal'], _r6['frac_of_signal'],
                                       _pc['rel'] / _r3['frac_of_signal']))

# ───────────────────────────────────────────── Ⓕ⑥ the interference: a share needs a convention
_int, _as = ST['interference'], ST['auto_share']
check("⛭⛭⛭ `r7873` ** ⑫ Ⓕ⑥ **THE FOUR TERMS INTERFERE, SO NO TERM OWNS A SHARE UNTIL THE CROSS "
      "TERMS ARE *ASSIGNED* -- `monopole × ISW` ALONE IS `+0.209044` OF THE TOTAL, AND THE FOUR "
      "AUTOS TOGETHER ARE ONLY `0.696144` OF IT ** ⇒ *** the six cross terms run from "
      "`monopole × ISW` at `+0.209044` down to `ISW × quadrupole` at `+0.000927`, and "
      "`ISW × doppler` is **NEGATIVE** at `-0.029673`. The autos are `monopole` `+0.486364`, "
      "`doppler` `+0.173659`, `ISW` `+0.035867`, `quadrupole` `+0.000254`. ** This revision assigns "
      "each cross HALF-AND-HALF to its two partners, which makes the four contributions sum to the "
      "total exactly; **that choice is stated, not hidden**, and a different convention gives "
      "different per-term shares. *** ⌗ *Same class as `r7869`'s finding that the per-bin share was "
      "not a readable number: a 'term's share' is not a property of CAMB until a convention is "
      "named*",
      (abs(_int['mono_x_isw'] - 0.2090435304402678) < 1e-15
       and abs(_int['isw_x_dopp'] - (-0.029672624291969117)) < 1e-15
       and _int['isw_x_dopp'] < 0.0
       and abs(_int['isw_x_quad'] - 0.0009268251263345788) < 1e-18
       and abs(_as['mono'] - 0.4863636064011011) < 1e-15
       and abs(_as['dopp'] - 0.17365948464529757) < 1e-15
       and abs(_as['isw'] - 0.03586701819327717) < 1e-15
       and abs(_as['quad'] - 0.0002535116682349531) < 1e-18
       and abs(sum(_as.values()) - 0.6961436209079108) < 1e-12),
      'crosses: mono x isw %+.6f, isw x dopp %+.6f (negative); four autos sum to %.6f'
      % (_int['mono_x_isw'], _int['isw_x_dopp'], sum(_as.values())))
# ───────────────────────────────────────────── Ⓖ⑦ THE ANSWER: the response by source term
_a3, _a6 = ST['answer']['0.3'], ST['answer']['0.6']
check("⛭⛭⛭ `r7873` ** ⑫ Ⓖ⑦ **THE ANSWER -- CAMB'S SUM RESPONSE *BY SOURCE TERM*, WITH THE SIGNED "
      "SHARES **ADDITIVE TO `1.00000000`** AND THE TERMS **NOT MOVING TOGETHER**: `ISW` RESPONDS AT "
      "`×2.14` ITS WEIGHT WHILE THE `monopole` RESPONDS AT `×0.74` OF ITS OWN ** ⇒ *** over "
      "`ℓ = 100`--`420` at `Σ = 0.60`, as median ratio / signed share of the total response / share "
      "of the `Σ = 0` spectrum: `monopole` `+0.020737` / `0.465652` / `0.627097`; `ISW` `+0.041584` "
      "/ `0.291812` / `0.136091`; `doppler` `+0.030356` / `0.236597` / `0.204474`; `quadrupole` "
      "`+0.034127` / `0.005940` / `0.005001`. At `Σ = 0.30` the shares are `0.472167`, `0.283102`, "
      "`0.238726`, `0.006005` -- **nearly unchanged**, so the decomposition is a STRUCTURAL property "
      "and not an artefact of one amplitude. ** The `ISW` ratio is `2.01×` the `monopole`'s at "
      "`Σ = 0.60`, which is the whole content of the item: the sum does not scale the spectrum, it "
      "reweights the terms that build it. *** ⌗ *Massive neutrinos change the expansion and growth "
      "history, which is what the `ISW` term integrates; the `monopole` is set at last scattering "
      "and moves least*",
      (abs(ST['sums'][0] - 0.30) < 1e-12 and abs(ST['sums'][1] - 0.60) < 1e-12
       and abs(ST['tau'] - 0.054) < 1e-12
       and abs(_a6['monopole']['median_ratio'] - 0.020737177842161447) < 1e-15
       and abs(_a6['ISW']['median_ratio'] - 0.04158438902065953) < 1e-15
       and abs(_a6['doppler']['median_ratio'] - 0.030355695191326415) < 1e-15
       and abs(_a6['quadrupole']['median_ratio'] - 0.03412653874135563) < 1e-15
       and abs(_a6['monopole']['signed_share_of_response'] - 0.4656517774746315) < 1e-15
       and abs(_a6['ISW']['signed_share_of_response'] - 0.29181155084269805) < 1e-15
       and abs(_a6['doppler']['signed_share_of_response'] - 0.2365965934999594) < 1e-15
       and abs(_a6['quadrupole']['signed_share_of_response'] - 0.005940078182710659) < 1e-18
       and abs(_a6['ISW']['share_of_spectrum'] - 0.136090552656873) < 1e-12
       and abs(_a6['monopole']['share_of_spectrum'] - 0.627097077262210) < 1e-12
       and abs(_a6['ISW']['responds_above_its_weight'] - 2.1442454685186507) < 1e-13
       and abs(_a6['monopole']['responds_above_its_weight'] - 0.7425513438965157) < 1e-13
       and abs(_a3['monopole']['signed_share_of_response'] - 0.472166685465957) < 1e-12
       and abs(_a3['ISW']['signed_share_of_response'] - 0.283102474649709) < 1e-12
       and abs(_a3['doppler']['signed_share_of_response'] - 0.238725749095979) < 1e-12
       and abs(_a3['quadrupole']['signed_share_of_response'] - 0.006005090788355) < 1e-12
       and abs(_a6['_shares_sum'] - 1.0) < 1e-12 and abs(_a3['_shares_sum'] - 1.0) < 1e-12
       and abs(_a6['ISW']['median_ratio'] / _a6['monopole']['median_ratio'] - 2.005) < 0.02),
      'Sigma 0.60 shares sum to %.8f; ISW %+.6f at x%.4f its weight vs monopole %+.6f at x%.4f; '
      'ISW/monopole ratio %.3f'
      % (_a6['_shares_sum'], _a6['ISW']['median_ratio'],
         _a6['ISW']['responds_above_its_weight'], _a6['monopole']['median_ratio'],
         _a6['monopole']['responds_above_its_weight'],
         _a6['ISW']['median_ratio'] / _a6['monopole']['median_ratio']))

# ───────────────────────────────────────────── Ⓗ⑧ the per-term ratio ENVELOPE is not readable
check("⛭⛔⛭ `r7873` ** ⑫ Ⓗ⑧ **THE PER-TERM RATIO *ENVELOPE* IS NOT A READABLE NUMBER FOR `ISW` OR "
      "`quadrupole` -- IT REACHES `19.354451` AND `10.823707` -- **BECAUSE THEIR ASSIGNED "
      "CONTRIBUTIONS CROSS ZERO INSIDE THE BAND**, WHICH IS WHY `Ⓖ⑦` REPORTS THE *MEDIAN* AND THE "
      "*SIGNED SHARE* ** ⇒ *** a ratio taken across a zero of its denominator is arithmetic without "
      "a referent. The `monopole` and `doppler` envelopes are ordinary (`0.062162` and `0.057182`) "
      "because their contributions keep one sign; `ISW` reaches `19.354451` and `quadrupole` "
      "`10.823707`, and the `quadrupole`'s value at `ℓ = 100` is NEGATIVE at `-0.227892` while its "
      "median is `+0.034127`. ** Those two envelopes are recorded here as **UNREADABLE AND NOT "
      "USED**, not quietly dropped. *** ⌗ *The THIRD instance of this class in this corpus: "
      "`r7871`'s `Ⓔ⑤` passed arithmetically on a quantity that did not exist near a zero crossing, "
      "and `r7871`'s `TE` needed an envelope for the same reason. The lesson has now cost three "
      "arms, so it is stated as a rule: **a ratio is readable only where its denominator keeps its "
      "sign***",
      (_a6['ISW']['envelope'] > 10.0 and _a6['quadrupole']['envelope'] > 10.0
       and abs(_a6['ISW']['envelope'] - 19.354451151845645) < 1e-12
       and abs(_a6['quadrupole']['envelope'] - 10.82370692659627) < 1e-12
       and abs(_a6['monopole']['envelope'] - 0.06216220731461797) < 1e-15
       and abs(_a6['doppler']['envelope'] - 0.05718161999443039) < 1e-15
       and _a6['monopole']['envelope'] < 0.1 and _a6['doppler']['envelope'] < 0.1
       and _a6['quadrupole']['l100'] < 0.0
       and abs(_a6['quadrupole']['l100'] - (-0.22789223985714957)) < 1e-15),
      'ISW envelope %.6f and quadrupole %.6f are unreadable; monopole %.6f and doppler %.6f are '
      'ordinary; quadrupole at l=100 is %+.6f against a %+.6f median'
      % (_a6['ISW']['envelope'], _a6['quadrupole']['envelope'], _a6['monopole']['envelope'],
         _a6['doppler']['envelope'], _a6['quadrupole']['l100'],
         _a6['quadrupole']['median_ratio']))

# ───────────────────────────────────────────── Ⓘ⑨ the ISW window was registered AT RISK and survived
_w = ST['isw_window']
_h6 = _w['halves']['0.6']
check("⛭⛭⛭ `r7873` ** ⑫ Ⓘ⑨ **THE EARLY/LATE `ISW` WINDOW WAS REGISTERED *AT RISK* AND **SURVIVED**: "
      "IT COMPILED AND CLOSES ON THE UNDIVIDED TERM AT `1.049911e-14` -- AND ITS ANSWER **REFUTES "
      "THE OBVIOUS READING OF `Ⓖ⑦`** ** ⇒ *** `Ⓗ⑧` of the registration expected the time window to "
      "fail, since early against late `ISW` is one integrand over different stretches of TIME and "
      "not a source term. A logistic window in the scale factor at `a = 0.032258` (`z = 30.0`) "
      "compiled, and its windowed pair-sum reproduces the undivided `ISW` auto-spectrum to "
      "`1.049911e-14` -- machine zero. ** THE ANSWER IS A NEGATIVE. The `late ISW` is "
      "intrinsically the MORE responsive half, `+0.093606` against the early half's `+0.074700` at "
      "`Σ = 0.60`, a factor `1.25`; but it is only `0.044190` of the `ISW` term in this band and so "
      "carries just `0.054644` of the `ISW` response. **`0.945356` of `ISW`'s response is the EARLY "
      "`ISW`.** *** ⌗ *So `Ⓖ⑦`'s `×2.14` is a RECOMBINATION-ERA effect, not the dark-energy one it "
      "looks like. Had the window failed, the natural reading of `Ⓖ⑦` -- massive neutrinos acting "
      "through the late-time growth the `ISW` integrates -- would have gone unchallenged and been "
      "WRONG*",
      (_w['built'] is True and _w['closes'] is True
       and abs(_w['rel_to_undivided_isw'] - 1.0499111214358652e-14) < 1e-22
       and _w['rel_to_undivided_isw'] < 1e-12
       and abs(_w['a_split'] - 0.03225806451612903) < 1e-15
       and abs(_w['z_split'] - 30.0) < 1e-9
       and abs(_h6['late']['median_ratio'] - 0.09360621709711792) < 1e-15
       and abs(_h6['early']['median_ratio'] - 0.07470033775680007) < 1e-15
       and _h6['late']['median_ratio'] > _h6['early']['median_ratio']
       and abs(_h6['late']['share_of_ISW'] - 0.044189967058373573) < 1e-15
       and abs(_h6['late']['signed_share_of_ISW_response'] - 0.054644312238706076) < 1e-15
       and abs(_h6['early']['signed_share_of_ISW_response'] - 0.9453556877612938) < 1e-15
       and _h6['early']['signed_share_of_ISW_response'] > 0.9),
      'window closes at %.6e; late ratio %+.6f > early %+.6f, yet late is %.6f of ISW and '
      'carries %.6f of its response, so early carries %.6f'
      % (_w['rel_to_undivided_isw'], _h6['late']['median_ratio'],
         _h6['early']['median_ratio'], _h6['late']['share_of_ISW'],
         _h6['late']['signed_share_of_ISW_response'],
         _h6['early']['signed_share_of_ISW_response']))

# ───────────────────────────────────────────── Ⓙ⑩ the band is the order's, and it excludes late ISW
check("⛭⛔⛭ `r7873` ** ⑫ Ⓙ⑩ **THE EARLY-`ISW` DOMINANCE IS A STATEMENT ABOUT **THIS BAND**, NOT "
      "ABOUT `ISW`: `ℓ = 100`--`420` IS THE ORDER'S OWN WINDOW AND IT EXCLUDES THE LATE `ISW` "
      "ALMOST ENTIRELY ** ⇒ *** the late `ISW` is a large-angle effect living at `ℓ ≲ 10`, so over "
      "`321` multipoles from `ℓ = 100` to `ℓ = 420` it holds `0.044190` of the `ISW` term. `Ⓘ⑨`'s "
      "`0.945356` is therefore NOT a claim that the late `ISW` is unresponsive to `Σ` -- `Ⓘ⑨` "
      "measures the opposite, that per unit it responds `1.25×` as strongly -- but a claim that it "
      "has almost no WEIGHT here. ** A reader who wants the late `ISW`'s own response needs a band "
      "that contains it, and this revision does not provide one: the order fixed `ℓ = 100`--`420` "
      "and that is what was measured. *** ⌗ *Stated so the figure is not carried out of this band "
      "by someone else. The same caution `r7869` needed and did not get*",
      (ST['l_lo'] == 100 and ST['l_hi'] == 420 and ST['n_ell'] == 321
       and abs(_h6['late']['share_of_ISW'] - 0.044189967058373573) < 1e-15
       and _h6['late']['share_of_ISW'] < 0.05
       and abs(_h6['late']['median_ratio'] / _h6['early']['median_ratio'] - 1.253) < 0.01),
      'band l=%d..%d, %d multipoles; late ISW is %.6f of the term though %.3fx as responsive'
      % (ST['l_lo'], ST['l_hi'], ST['n_ell'], _h6['late']['share_of_ISW'],
         _h6['late']['median_ratio'] / _h6['early']['median_ratio']))

# ───────────────────────────────────────────── the count arm
check("⛭ `r7873` ** Ⓝ⑭ THE ARMS ABOVE ARE **ALL OF THEM**, AND THE COUNT IS ASSERTED SO A SILENTLY "
      "DROPPED ARM CANNOT PASS AS A CLEAN RUN ** ⇒ *** fifteen arms precede this one: six on item "
      "⑪ and nine on item ⑫. *** ⌗ *A receipt that loses an arm to an editing slip reports fewer "
      "failures than it has*",
      _n[0] == 15,
      '%d arm(s) before this one' % _n[0])

print('\n' + '=' * 100)
print('  %d arm(s), %d failed' % (_n[0], _fail[0]))
print('=' * 100)
sys.exit(1 if _fail[0] else 0)
