"""
P15, r7853+cc66.12, on 69's order r7853: the REPAIRED transfer checked against CAMB, and the
LIKE-FOR-LIKE reference built on 60's own subset AND 60's own freedoms.

** ③ THE REPAIR WORKS, AND THE K-SHAPE ERROR IS GONE. **
60's BVEL=1 drives the baryon continuity with a baryon velocity the solver's state had lacked.
Re-banking phi_shape(4000) under it and re-running r7851's comparison:

                        PRE-REPAIR      REPAIRED
  frac at k = 0.05       -31.779 %       +1.853 %
  worst frac             -31.888 %       +2.960 %
  residual shape ratio     1.46800        0.98410
  Phi(k -> 0)            -0.901020      -0.901021

So the fault r7852 diagnosed as the transfer's shape in WAVENUMBER, and which this seat
corroborated at r7851 by matching the decay SIZE under a different normalisation, is removed.
⌗ The sign FLIPS: the repaired transfer is slightly in EXCESS, not over-suppressed.
⌗ 60 report the shape "within 2.5 per cent".  At k = 0.05 that holds (1.85); at the WORST mode it
  is 2.96, outside the figure they quoted.  Their claim is right at the band they named.

** ⑤ AND THE HELD PARAMETERS EXPLAIN NONE OF THE GAP, WHICH REFUTES THIS SEAT'S OWN r7849 CLAIM
ON THE RULER 60 ACTUALLY USE. **

  arm          95% limit   vertex 4/5/6 meV        vs r7849 HELD    vs published 64.2
  calibrated    30.560 meV  -80.01/-67.50/-68.12    26.06  (+17.3%)   2.10 x tighter
  minimised     54.000 meV  -81.07/-72.81/-74.91    54.28  ( -0.5%)   1.19 x tighter
  ruler spread 43.4 per cent of the looser   (r7849, parameters HELD: 52.0)

r7849's receipt declared its factor against 60 an UPPER BOUND and not a measurement, because
holding omega_b and n_s tightens this reference for free.  60's model3.bao_direct MINIMISES r_d, so
the MINIMISED arm is the like-for-like one -- and there, freeing the two parameters moves the limit
by half a per cent, 54.28 to 54.000 against 60's 100.40.  ** The correction that caveat anticipated
is approximately ZERO where it counts. **  The factor 1.85 stands essentially unchanged and is now
a measurement rather than a bound.  The stance was right and the quantity it hedged against is
negligible; both halves are reported.

** AND THE OVER-CONSTRAINT AGAINST THE PUBLISHED FIGURE SURVIVES THE EXTRA FREEDOM. **  30.560 meV
is still 2.10 times tighter than 64.2, where the held arm was 2.46.  Consistent with this
revision's own registration, which said in advance that the published baseline likelihood is
CamSpec with SimAll and Commander, which NEITHER instrument scores -- so the residual is most
likely the likelihood and not the parameter count.

** FOUR OF THIS SEAT'S REGISTERED BANDS ARE REFUTED OR WITHDRAWN, AND EACH IS REPORTED AS SUCH. **
  Ⓓ "the baryon slot I_DB moves"            -> REFUTED.  NV grows 19 -> 20 but I_DB is 18 on both
     sides; the added slot is APPENDED at index 19.  The band was right that the layout moves and
     that a hardcoded index needs licensing, and wrong about which slot moves.
  Ⓒ "the decay-ratio agreement improves"    -> WITHDRAWN AS ILL-POSED.  Its comparator was 60's own
     PRE-REPAIR spurious decay 1.41983, the quantity the repair removes, so agreeing with it after
     the repair would have meant the repair FAILED.  A symptom is not a target.
  Ⓔ "BOTH limits loosen"                     -> HALF REFUTED.  Calibrated loosens into its band at
     the bottom edge; minimised does not loosen at all and lands BELOW its registered 60-120 band.
  and the warm-start check's own printed verdict -> MIS-THRESHOLDED, corrected below.

** THE WARM STARTS DID NOT DECIDE THE ANSWER, AND THE CHECK THAT SAID THEY DID WAS WRONG. **
Two points re-run cold from the control start: calibrated 614.7121 warm against 614.7120 cold,
minimised 608.4979 against 608.4998 -- agreement to about 2e-3 in chi^2, INSIDE the minimiser's own
fatol of 5e-3.  The comparison printed "the warm path GOT STUCK" on a difference of 1e-4 because
its threshold was written at 1e-6, five thousand times tighter than the convergence tolerance of
what it was checking.  ⇒ A verification threshold below the tolerance of what it verifies reports
NOISE AS FAILURE.  This line's usual defect is an assertion too weak to fail; this is its mirror,
too strong to pass, and it manufactures a retraction instead of hiding one.

** THE PINS ARE VERIFIED FAILABLE BY PERTURBATION, NOT ASSUMED TO BE. **  Each banked figure was
moved in turn and the arms that read it watched to redden, then restored from git:
  * scaling the repaired transfer's k = 0.05 fraction by 1.5 reddens Ⓒ⑧ (+1.853 -> +2.779 per cent);
  * moving the residual shape ratio by 0.01 reddens Ⓓ⑪ (0.98410 -> 0.99410);
  * adding 0.5 to the CALIBRATED arm's Sum = 0.05 total reddens FIVE arms -- Ⓔ⑭'s limit
    (30.560 -> 27.480 meV), Ⓕ⑯'s vertex, Ⓖ⑰'s spread, Ⓗ⑱'s loosening and Ⓘ㉑'s factor;
  * adding 0.5 to the MINIMISED arm's likewise reddens SIX -- Ⓕ⑮ (54.000 -> 45.760 meV), Ⓕ⑯, Ⓖ⑰,
    Ⓗ⑲, Ⓗ⑳ and Ⓘ㉑, so THE HEADLINE FINDING IS ITSELF FAILABLE and not merely stated.
Each was applied in place, the run watched, and the record restored from git; the four runs
reddened 1, 1, 5 and 6 arms and NOTHING ELSE.  ⌗ The counts are the MEASURED ones: this record
first said "1, 1, 2 and 2", written from expectation before the runs, and is corrected here.

COMPUTES: nothing of the physics another seat owns.  It re-reads THIS revision's own banked
          records -- the repaired transfer comparison, the state-layout probe, the sixteen profile
          points and the two cold re-runs -- and recomputes from them: each arm's minimum, 95 per
          cent limit by the first Delta chi^2 > 2.71 crossing ABOVE the minimum, the parabolic
          vertices, the ruler spread, the loosening against r7849 and the factors against the
          published figure.  It reads 60's modules only STRUCTURALLY, through the parsed syntax
          tree, never by matching their wording.

Bound: this receipt pins THIS revision's figures.  It does NOT re-run 60's control, does not rule
on whether the repaired transfer's slight EXCESS matters, and does NOT reproduce the published
64.2 meV -- the published baseline likelihood is one neither instrument scores, which is stated
rather than worked around.  The vertex is an EXTRAPOLATED parabolic vertex and NOT 60's estimator,
which is a posterior mean over a chain whose lower bound is negative; CAMB has no negative-sum
construction and none was invented.  It pins no cosmological parameter as a result.
"""
import ast
import glob
import json
import os
import sys

import numpy as np

FAILED = []
RAN = []


def check(label, ok, detail=''):
    RAN.append(label)
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
R51 = os.path.join(BTW, 'r7851_cc66_an_independent_weyl_potential_check_against_camb')
R46 = os.path.join(BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')

with open(os.path.join(MINE, 'transfer_repaired_vs_camb.json'), encoding='utf-8') as fh:
    T = json.load(fh)
with open(os.path.join(MINE, 'state_layout_probe.json'), encoding='utf-8') as fh:
    L = json.load(fh)

ROWS = {}
for _f in glob.glob(os.path.join(MINE, 'out5', '*.json')):
    with open(_f, encoding='utf-8') as fh:
        _d = json.load(fh)
    if _d.get('cold'):
        ROWS.setdefault('cold', []).append(_d)
    else:
        ROWS.setdefault(_d['mode'], []).append(_d)
for _m in ROWS:
    ROWS[_m].sort(key=lambda r: r['sum'])


def limit95(rows):
    """the first crossing ABOVE the minimum -- scanning from the grid's bottom is the r7847 bug"""
    s = np.array([r['sum'] for r in rows], float)
    t = np.array([r['total'] for r in rows], float)
    dc = t - t.min()
    i = int(np.argmin(t))
    hs, hd = s[i:], dc[i:]
    fine = np.linspace(float(hs[0]), float(hs[-1]), 20001)
    k = np.where(np.interp(fine, hs, hd) > 2.71)[0]
    return float(s[i]), (float(fine[k[0]]) * 1000.0 if k.size else None), dc


def vertices(rows, dc):
    s = np.array([r['sum'] for r in rows], float)
    out = []
    for n in (4, 5, 6):
        a, b, _c = np.polyfit(s[:n], dc[:n], 2)
        out.append(-b / (2 * a) * 1000.0)
    return out


print(__doc__.strip().splitlines()[1])
print()

# -------------------------------------------------- Ⓐ the grid is complete and the freedoms named
check('Ⓐ① the profile is COMPLETE on both rulers, eight sums each, so no limit is off a partial grid',
      len(ROWS.get('rd_camb', [])) == 8 and len(ROWS.get('rd_min', [])) == 8,
      'calibrated %d, minimised %d' % (len(ROWS.get('rd_camb', [])), len(ROWS.get('rd_min', []))))

check('Ⓐ② and FIVE parameters are free, which is what makes it like-for-like with 60\'s six',
      ROWS['rd_camb'][0]['free'] == ['H0', 'Om', 'ombh2', 'ns', 'tau'],
      'free = %s' % ','.join(ROWS['rd_camb'][0]['free']))

_M6 = ast.parse(open(os.path.join(R46, 'model6.py'), encoding='utf-8').read())
_names = {n.name for n in ast.walk(_M6) if isinstance(n, ast.FunctionDef)}
check('Ⓐ③ 60\'s scoring entry point still exists, read off their parsed syntax tree not their wording',
      'chi2' in _names, 'model6 defines %d functions' % len(_names))

# ------------------------------------------------ Ⓑ the state layout, and Ⓓ's refutation recorded
check('Ⓑ④ the state WIDENS across the repair, NV 19 to 20, so the layout did move',
      L['bvel0']['NV'] == 19 and L['bvel1']['NV'] == 20,
      'NV %d -> %d' % (L['bvel0']['NV'], L['bvel1']['NV']))

check('Ⓑ⑤ but the baryon slot does NOT move -- this REFUTES the half of Ⓓ that said it would',
      L['bvel0']['I_DB'] == L['bvel1']['I_DB'] == 18,
      'I_DB %d -> %d, so the added slot is APPENDED at 19'
      % (L['bvel0']['I_DB'], L['bvel1']['I_DB']))

check('Ⓑ⑥ and slot 6 is still the potential, LICENSED by the analytic -9/10 and not by the index',
      abs(L['bvel1']['slot6_super_horizon'] + 0.901) < 0.001
      and abs(L['bvel0']['slot6_super_horizon'] - L['bvel1']['slot6_super_horizon']) < 1e-5,
      '%.6f and %.6f across the repair'
      % (L['bvel0']['slot6_super_horizon'], L['bvel1']['slot6_super_horizon']))

# ------------------------------------------------------------- Ⓒ item ③, the repaired transfer
check('Ⓒ⑦ CAMB\'s Weyl variable still carries its factor k^2, MEASURED as a slope and divided out',
      abs(T['camb_weyl_small_k_loglog_slope'] - 1.998) < 0.0008,
      'slope %.4f  (pinned 1.998 +/- 0.0008)' % T['camb_weyl_small_k_loglog_slope'])

rep, pre = T['repaired'], T['pre_repair']
k05 = rep['frac_at_k005'] * 100.0
check('Ⓒ⑧ the deficit at k = 0.05 /Mpc COLLAPSES to 1.85 per cent, from 31.78 over-suppressed',
      abs(k05 - 1.85) < 0.004 and abs(pre['frac_at_k005'] * 100.0 + 31.78) < 0.012,
      'repaired %+.4f per cent, pre-repair %+.4f' % (k05, pre['frac_at_k005'] * 100.0))

check('Ⓒ⑨ and the SIGN FLIPS: the repaired transfer is in EXCESS, not over-suppressed',
      rep['frac_at_k005'] > 0 > pre['frac_at_k005'],
      'pre %+.4f, repaired %+.4f' % (pre['frac_at_k005'], rep['frac_at_k005']))

wf = rep['worst_frac'] * 100.0
check('Ⓒ⑩ the worst mode is 2.96 per cent, so 60\'s own "within 2.5 per cent" holds at the band '
      'they named and the TAIL is wider',
      abs(wf - 2.96) < 0.004 and wf > 2.5,
      'worst %+.4f per cent at k = %.5g' % (wf, rep['worst_k']))

check('Ⓓ⑪ the k-SHAPE ERROR IS GONE: the residual shape ratio is 0.9841 against 1.4680 before',
      abs(rep['residual_shape_ratio'] - 0.9841) < 0.0004
      and abs(pre['residual_shape_ratio'] - 1.4680) < 0.0005,
      '%.5f from %.5f, a perfect 1.0 being no residual shape'
      % (rep['residual_shape_ratio'], pre['residual_shape_ratio']))

check('Ⓓ⑫ and the super-horizon normalisation does not move, -0.90102 on both sides',
      abs(rep['super_horizon'] + 0.90102) < 0.0003
      and abs(rep['super_horizon'] - pre['super_horizon']) < 1e-5,
      'repaired %.6f, pre %.6f' % (rep['super_horizon'], pre['super_horizon']))

# --------------------------------------------------------------- Ⓔ/Ⓕ item ⑤, the two arms
sC, limC, dcC = limit95(ROWS['rd_camb'])
sM, limM, dcM = limit95(ROWS['rd_min'])
vC, vM = vertices(ROWS['rd_camb'], dcC), vertices(ROWS['rd_min'], dcM)

check('Ⓔ⑬ the calibrated arm\'s minimum is at a ZERO sum exactly, so the scan starts where it should',
      abs(sC) < 1e-12 and abs(sM) < 1e-12, 'minima at %.3f and %.3f eV' % (sC, sM))

check('Ⓔ⑭ the calibrated 95 per cent limit is 30.56 meV, by the first crossing ABOVE the minimum',
      abs(limC - 30.56) < 0.012, 'limit %.3f meV  (pinned 30.56 +/- 0.012)' % limC)

check('Ⓕ⑮ the minimised 95 per cent limit is 54.00 meV, on 60\'s own treatment of the ruler',
      abs(limM - 54.00) < 0.02, 'limit %.3f meV  (pinned 54.00 +/- 0.02)' % limM)

check('Ⓕ⑯ and both vertices are deep in the negative, -67.50 and -72.81 on the five-point fit',
      abs(vC[1] + 67.50) < 0.025 and abs(vM[1] + 72.81) < 0.025,
      'calibrated %s ; minimised %s' % ('/'.join('%+.2f' % v for v in vC),
                                        '/'.join('%+.2f' % v for v in vM)))

spread = 100.0 * (1.0 - limC / limM)
check('Ⓖ⑰ the ruler is still worth 43.4 per cent of the looser limit, down from 52.0 when HELD',
      abs(spread - 43.4) < 0.04, 'spread %.2f per cent  (pinned 43.4 +/- 0.04)' % spread)

# ------------------------------- Ⓗ the finding: the held parameters explain none of the gap
loosC = 100.0 * (limC / 26.06 - 1.0)
loosM = 100.0 * (limM / 54.28 - 1.0)
check('Ⓗ⑱ freeing the two parameters loosens the CALIBRATED limit by 17.3 per cent',
      abs(loosC - 17.3) < 0.04, 'calibrated %+.2f per cent against r7849\'s 26.06 meV' % loosC)

check('Ⓗ⑲ ⛔ and leaves the MINIMISED one UNCHANGED -- half a per cent, and slightly TIGHTER',
      abs(loosM) < 1.0 and loosM < 0.0,
      'minimised %+.2f per cent against r7849\'s 54.28 meV' % loosM)

check('Ⓗ⑳ ⇒ so on 60\'s OWN ruler the held parameters explain NONE of the gap, and r7849\'s '
      '"upper bound, not a measurement" caveat is refuted in magnitude',
      abs(limM - 54.28) < 1.0 and abs(loosM) < abs(loosC) / 10.0,
      '54.28 -> %.3f meV against 60\'s 100.40; the calibrated arm moved %.0f times further'
      % (limM, abs(loosC / loosM) if loosM else float('inf')))

check('Ⓘ㉑ and the over-constraint against the published figure SURVIVES the extra freedom',
      abs(64.2 / limC - 2.10) < 0.004 and abs(64.2 / limM - 1.19) < 0.004,
      '%.3f times tighter calibrated, %.3f minimised, where the HELD arm was 2.46'
      % (64.2 / limC, 64.2 / limM))

# --------------------------------------------------- Ⓙ the mechanism grades, Ⓚ the warm starts
runC = ROWS['rd_camb'][-1]['H0'] - ROWS['rd_camb'][0]['H0']
runM = ROWS['rd_min'][-1]['H0'] - ROWS['rd_min'][0]['H0']
check('Ⓙ㉒ the mechanism GRADES: H0 runs harder on the free ruler than the calibrated one',
      runM < runC < 0, 'H0 run %.3f calibrated against %.3f minimised' % (runC, runM))

_cold = {r['mode']: r for r in ROWS.get('cold', [])}
_ok, _det = True, []
for _m, _rows in (('rd_camb', ROWS['rd_camb']), ('rd_min', ROWS['rd_min'])):
    if _m not in _cold:
        _ok = False
        continue
    _w = next(r for r in _rows if abs(r['sum'] - 0.10) < 1e-9)
    _d = _w['total'] - _cold[_m]['total']
    _det.append('%s %+.4f' % (_m, _d))
    _ok = _ok and abs(_d) < 5e-3
check('Ⓚ㉓ the warm starts did NOT decide the answer: cold re-runs agree inside the minimiser\'s '
      'own fatol of 5e-3, and the printed "GOT STUCK" verdict was MIS-THRESHOLDED at 1e-6',
      _ok, 'warm minus cold: %s' % '; '.join(_det))

check('Ⓛ㉔ the count is COUNTED off the arms that ran and then pinned, not typed',
      len(RAN) == 23, 'arms before this one: %d (pinned 23)' % len(RAN))

print()
print('  %d arms, %d FAILED' % (len(RAN), len(FAILED)))
if FAILED:
    print('  FAILED: ' + '; '.join(FAILED))
sys.exit(1 if FAILED else 0)
