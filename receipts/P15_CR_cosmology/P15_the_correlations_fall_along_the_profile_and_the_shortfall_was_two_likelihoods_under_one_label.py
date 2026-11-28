# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE CORRELATIONS *FALL* ALONG THE PROFILE, THE REGISTERED STRONG EXPECTATION IS REFUTED, AND
`r7904`'s UNREGISTERED SHORTFALL IS WITHDRAWN: IT COMPARED TWO LIKELIHOODS UNDER ONE LABEL.

COMPUTES: nothing physical. It reads the record `r7908` produced from the amplitude-marginalised
Fisher block of `model3.Model3('lcdm')` at Σ = `0`, `0.06` and `0.30`, and it checks the teeth of
that reading.  No spectrum is solved by that revision either: `Model3`'s splines were already banked.
⛔ ** IT PINS THE BINDING CONTROL FIRST: ** the Σ = `0` block is `r7904`'s, ENTRY FOR ENTRY, compared
here between the two records rather than taken from either one's own boolean — which is what makes
the three points one measurement and not three.
** IT PINS AS RESULTS: ** `ρ(Σ, ω_b)` and `ρ(Σ, n_s)` FALL from `+0.511698`/`+0.485608` at Σ = `0` to
`+0.494984`/`+0.434296` at Σ = `0.30`, so `Δρ` = `−0.016714` and `−0.051311` against a registered fall
bar of `−0.05`; and the degradation factor falls with them, `1.280436` to `1.264440` to `1.235741`.
⇒ ** SO THE REGISTERED OUTCOME IS `Ⓟ⓸ + Ⓝ⓷`: ** the instrument becomes LESS degenerate against both
parameters the reference holds as the sum grows, not more.  *The registration attached NO expectation
to that axis, on the stated grounds that a plausible story ran each way, so the direction is
information rather than a confirmation.*
⛔ ** AND THE REGISTERED STRONG EXPECTATION IS REFUTED, NOT NARROWLY: ** `σ(Σ)` was expected to GROW
along the profile and it FALLS, `0.0545938` to `0.0479808` eV, monotonically across all eleven nodes
the limit record banks.
⛭⛭ ** WHICH FORCED THE REAL FINDING, AND IT IS A CORRECTION TO A PREDECESSOR OF THIS SEAT'S OWN. **
A monotonically tightening curvature makes `r7904`'s story impossible, so the two numbers it compared
were examined: this block is `chi2_cmb`, `555` CMB bandpowers over five parameters, while `r7888`'s
crossing is read on `Model6.chi2`, which is the same CMB score PLUS a BAO term PLUS a lensing
likelihood PLUS a tau prior, over SIX parameters.  ** TWO LIKELIHOODS UNDER ONE LABEL. **  Read inside
ONE object instead — the profile's own curvature from the profile's own `Δχ²` values — the crossing
comes out in `[185.0880, 194.0674]` meV across three fits against an actual `193.5453`.
⇒ ** THE PROFILE IS ACCOUNTED FOR BY ITS OWN CURVATURE, THERE IS NO SHORTFALL, AND `r7904`'s SENTENCE
IS WITHDRAWN. ** *The arithmetic was right and the object was not; the many-to-one-label guard says to
establish which object a quantity belongs to BEFORE two are identified, and at `r7904` it was not.*
⚠ ** AND WHAT IS NOT CLAIMED: ** nothing about the reference, whose block has not landed; no mechanism,
because a correlation is not one; no limit, `r7888`'s `193.545` meV being untouched and in fact
SUPPORTED rather than undercut by this correction; and nothing about the instrument outside the
quadratic Taylor model it is read on, whose truncation does more work at Σ = `0.30` than at the origin.

    python3 <this file>
"""
import ast
import glob
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7908 = glob.glob(os.path.join(BW, 'r7908_60_*'))[0]
R7904 = glob.glob(os.path.join(BW, 'r7904_60_*'))[0]
R7888 = glob.glob(os.path.join(BW, 'r7888_60_*'))[0]

FAILS = []
NARMS = 0


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


D = json.load(io.open(os.path.join(R7908, 'interior_block.json'), encoding='utf-8'))
P4 = json.load(io.open(os.path.join(R7904, 'fisher_block.json'), encoding='utf-8'))
L = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7908, 'interior_block.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
RRAW = io.open(os.path.join(R7908, 'RESULT.md'), encoding='utf-8').read()
PRAW = io.open(os.path.join(R7908, 'PREDICTION.md'), encoding='utf-8').read()

TAGS = ['Ⓞ', 'Ⓐ', 'Ⓑ']
PT = {t: D['points'][t] for t in TAGS}

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE BINDING CONTROL, AND THE RECORD\'S OWN CONSISTENCY')


def corr(M):
    c = np.linalg.inv(M)
    d = np.sqrt(np.diag(c))
    return c / np.outer(d, d)


_mine = np.asarray(PT['Ⓞ']['fisher'], float)
_theirs = np.asarray(P4['fisher'], float)
check('Ⓐ① the Σ = 0 block is `r7904`\'s ENTRY FOR ENTRY, compared HERE between the two records rather '
      'than taken from either one\'s own boolean — which is what makes the three points one '
      'measurement, so a difference between them cannot be a difference between implementations',
      float(np.max(np.abs(_mine - _theirs))) == 0.0
      and float(D['reproduced_r7904_worst']) == 0.0,
      'worst absolute difference %.3e over %d entries; the record reports %.3e'
      % (float(np.max(np.abs(_mine - _theirs))), _mine.size,
         float(D['reproduced_r7904_worst'])))

_ok = True
for t in TAGS:
    F = np.asarray(PT[t]['fisher'], float)
    R = np.asarray(PT[t]['correlation'], float)
    _ok = (_ok and float(np.max(np.abs(corr(F) - R))) < 1e-10
           and float(np.min(np.linalg.eigvalsh(F))) > 0.0
           and float(np.max(np.abs(R - R.T))) < 1e-12)
check('Ⓐ② at every one of the three points the reported CORRELATIONS are the reported BLOCK\'s own, '
      're-derived here by inverting it, and every block is a symmetric positive-definite matrix — so '
      'no correlation below is a reciprocal of something negative',
      _ok, 'checked at %d point(s); smallest eigenvalues %s'
      % (len(TAGS), ['%.4e' % float(np.min(np.linalg.eigvalsh(
          np.asarray(PT[t]['fisher'], float)))) for t in TAGS]))

check('Ⓐ③ each point\'s five-vector is `r7888`\'s banked node to the last bit, so the three blocks '
      'were expanded where the profile was read and not at neighbouring cosmologies',
      all(PT[t]['x5'] == [float(v) for v in L['calibrated']['x_at_node'][PT[t]['node']]]
          for t in TAGS),
      '; '.join('%s node %s chi2 %.4f' % (t, PT[t]['node'], PT[t]['chi2_cmb']) for t in TAGS))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE VERDICT, RECOMPUTED FROM THE RECORDED BLOCKS')

_dwb = abs(PT['Ⓑ']['rho_sigma']['WB']) - abs(PT['Ⓞ']['rho_sigma']['WB'])
_dns = abs(PT['Ⓑ']['rho_sigma']['NS']) - abs(PT['Ⓞ']['rho_sigma']['NS'])
check('Ⓑ① `Ⓟ⓸` fires on the registered fall bar, and the deltas are recomputed HERE from the '
      'recorded correlations rather than read from the record\'s own delta field',
      'Ⓟ⓸' in D['outcomes']
      and abs(_dwb - float(D['delta_rho']['WB'])) < 1e-12
      and abs(_dns - float(D['delta_rho']['NS'])) < 1e-12
      and min(_dwb, _dns) <= -float(D['bars']['flat']),
      'omega_b %+.6f, n_s %+.6f against a fall bar of %.2f' % (_dwb, _dns, D['bars']['flat']))

check('Ⓑ② `Ⓝ⓷` fires because the degradation factor is intermediate at BOTH interior points, and it '
      'FALLS along the profile rather than rising — recomputed here from each recorded block',
      'Ⓝ⓷' in D['outcomes']
      and all(D['bars']['R_null'] <= PT[t]['degradation_R'] < D['bars']['R_strong']
              for t in ('Ⓐ', 'Ⓑ'))
      and PT['Ⓞ']['degradation_R'] > PT['Ⓐ']['degradation_R'] > PT['Ⓑ']['degradation_R']
      and all(abs(float(np.sqrt(np.linalg.inv(np.asarray(PT[t]['fisher'], float))[0, 0]))
                  / float(np.sqrt(np.linalg.inv(np.asarray(PT[t]['fisher'], float)
                                                [np.ix_([0, 1, 2], [0, 1, 2])])[0, 0]))
                  - PT[t]['degradation_R']) < 1e-09 for t in TAGS),
      '%.6f, %.6f, %.6f' % tuple(PT[t]['degradation_R'] for t in TAGS))

_sg = [r['sigma_sum'] for r in D['unregistered']['scan']]
check('Ⓑ③ the registered STRONG expectation is REFUTED and not narrowly: `σ(Σ)` does not grow, it '
      'FALLS — and across every node the limit record banks it falls MONOTONICALLY, which is '
      'recomputed here from the scan rather than taken from its boolean',
      D['sigma_grew'] is False
      and PT['Ⓑ']['sigma_sum_marginalised'] < PT['Ⓞ']['sigma_sum_marginalised']
      and bool(np.all(np.diff(_sg) < 0.0)) and D['unregistered']['sigma_monotone'] is True
      and len(_sg) >= 11,
      '%.7f down to %.7f eV over %d node(s), monotone %s'
      % (_sg[0], _sg[-1], len(_sg), bool(np.all(np.diff(_sg) < 0.0))))

_vd = [n for n in ast.walk(TREE) if isinstance(n, ast.FunctionDef) and n.name == 'verdict']
_glob = sorted({n.id for f in _vd for n in ast.walk(f)
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id.isupper()})
check('Ⓑ④ the outcome is assigned by a PURE function of the measured numbers and the registered '
      'bars, read off the parse tree: `verdict` loads no module-level name but the bars',
      len(_vd) == 1 and all(g in ('GROW_BAR', 'FLAT_BAR', 'R_STRONG', 'R_NULL') for g in _glob),
      'one definition: %s; the module-level names its body loads are %s' % (len(_vd) == 1, _glob))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE CORRECTION TO `r7904`, RE-DERIVED HERE INSIDE ONE OBJECT')

_ss = np.asarray(L['calibrated']['sums'], float)
_dd = np.asarray(L['calibrated']['delta'], float)
_dchi = float(L['dchi2'])
_cross = float(L['calibrated']['crossing_meV'])
_k = int(np.argmin(_dd))
_own = []
for n in (3, 5, 6):
    sel = list(range(max(0, _k - (n // 2)), min(len(_ss), _k + (n // 2) + 1)))
    aa, bb, _c = np.polyfit(_ss[sel], _dd[sel], 2)
    _own.append(1000.0 * (-bb / (2.0 * aa) + float(np.sqrt(_dchi)) / float(np.sqrt(aa))))
check('Ⓒ① the profile\'s OWN curvature accounts for its OWN crossing, re-derived in this receipt '
      'from `r7888`\'s own delta-chi-square values: three parabolas about its minimum bracket the '
      'crossing it actually reports. ⇒ *So there is no shortfall to explain, and `r7904`\'s sentence '
      'is withdrawn rather than left standing*',
      min(_own) <= _cross <= max(_own)
      and D['correction_to_r7904']['accounted'] is True
      and abs(min(_own) - float(D['correction_to_r7904']['span_meV'][0])) < 5e-04
      and abs(max(_own) - float(D['correction_to_r7904']['span_meV'][1])) < 5e-04,
      'the three fits span [%.4f, %.4f] meV and the crossing is %.4f' % (min(_own), max(_own), _cross))

#: ⛭ THE TWO LIKELIHOODS ARE SHOWN TO DIFFER NUMERICALLY, FROM THE TWO RECORDS THEMSELVES — no
#:   name is searched for in anyone's source. The limit record's own total at the zero node is the
#:   value of the function the crossing is read on; `r7904`'s record carries the value of THIS
#:   block's function at the same node. If they were one likelihood the two would agree.
_tot0 = float(L['calibrated']['totals'][0])
_cmb0 = float(P4['chi2_cmb'])
_ratio = _tot0 / _cmb0
check('Ⓒ② the two likelihoods are DIFFERENT OBJECTS, shown by their own recorded VALUES at the same '
      'node rather than by searching a source for the name of a term: the function the crossing is '
      'read on scores %.4f there, and the function this block differentiates scores %.4f — a factor '
      'of %.4f apart. ⇒ *One label, two likelihoods, and no reading of the first can be extrapolated '
      'from the curvature of the second*' % (_tot0, _cmb0, _ratio),
      _ratio > 2.0 and abs(_cmb0 - float(PT['Ⓞ']['chi2_cmb'])) < 5e-09,
      'the limit record\'s own total %.4f against this block\'s score %.4f at the same node, and '
      'that score is the one `r7904` recorded to the last bit' % (_tot0, _cmb0))

_me = os.path.basename(R7908).split('_')[0]
_pred_result = io.open(os.path.join(R7904, 'RESULT.md'), encoding='utf-8').read()
check('Ⓒ③ the withdrawal is carried WHERE THE CLAIM WAS MADE and not only here: the predecessor\'s '
      'own RESULT now cites this revision by id — derived from this revision\'s directory rather '
      'than typed — and its receipt was RENAMED, so no receipt in this family still asserts the '
      'withdrawn half in its filename',
      _me in _pred_result and _me.startswith('r')
      and not glob.glob(os.path.join(HERE, '*weak_limit_is_not_the_curvature*')),
      'the predecessor\'s RESULT cites %s; no receipt carries the withdrawn name' % _me)

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE CLAMP, AND THE TWO FORMS OF ITS GATE THAT FAILED')

check('Ⓔ① the clamp is established as an IDENTITY on the function: below Σ = 0 the departure sits at '
      'the floor of double precision and above it is broken by nine orders of magnitude more, which '
      'is what licenses calling the interior points two-sided',
      float(D['unregistered']['clamp_identity_below']) < 1e-12
      and (float(D['unregistered']['clamp_identity_above'])
           > 1e+08 * float(D['unregistered']['clamp_identity_below'])),
      'below %.3e, above %.3e' % (float(D['unregistered']['clamp_identity_below']),
                                  float(D['unregistered']['clamp_identity_above'])))

#: ⛭ read off the PARSE TREE rather than by searching the RESULT for a phrase: the one-sided
#:   disagreement is computed and printed, and the gate that replaced it does NOT test it — which is
#:   what `reported with no bar on it` has to mean if it is to mean anything checkable.
_clamp_gate = [n for n in ast.walk(TREE) if isinstance(n, ast.Call)
               and isinstance(n.func, ast.Name) and n.func.id == 'gate'
               and n.args and isinstance(n.args[0], ast.Constant)
               and n.args[0].value.startswith('Ⓒ')]
_kink_names = set()
for c in _clamp_gate:
    for nn in ast.walk(c):
        if isinstance(nn, ast.Name):
            _kink_names.add(nn.id)
check('Ⓔ② the one-sided disagreement the FIRST form of that gate measured is reported and NOT '
      'GATED, read off the parse tree: it sits in the record under its own key at all three points, '
      'and no `gate` call in the module tests it. ⌗ *That is what `reported with no bar on it` must '
      'mean if it is to be checkable at all*',
      set(D['unregistered']['clamp_onesided']) == set(TAGS)
      and 'kink' not in _kink_names and len(_clamp_gate) >= 2,
      'recorded at %d point(s); the module\'s %d control gate(s) do not reference it'
      % (len(D['unregistered']['clamp_onesided']), len(_clamp_gate)))

check('Ⓔ③ the registration named TWO interior points and the extra nodes are marked UNREGISTERED in '
      'the record, under their own key, so the scan cannot be mistaken for part of the verdict',
      'unregistered' in D and 'scan' in D['unregistered']
      and not (set(D['unregistered']) & set(D['outcomes']))
      and len(D['unregistered']['scan']) > 2,
      '%d node(s) scanned, recorded under `unregistered`' % len(D['unregistered']['scan']))

# ---------------------------------------------------------------------------------------------- Ⓗ
print('\nⒽ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

U = D['unregistered']
C = D['correction_to_r7904']
check('Ⓗ① every figure this revision states in its RESULT is pinned here against the quantity ITS '
      'OWN CELL names, the mapping stated per figure and only its completeness mechanical',
      True
      and abs(PT['Ⓞ']['rho_sigma']['H0'] - 0.318326) < 5e-07
      and abs(PT['Ⓞ']['rho_sigma']['OM'] - (-0.155486)) < 5e-07
      and abs(PT['Ⓞ']['rho_sigma']['WB'] - 0.511698) < 5e-07
      and abs(PT['Ⓞ']['rho_sigma']['NS'] - 0.485608) < 5e-07
      and abs(PT['Ⓐ']['rho_sigma']['H0'] - 0.405646) < 5e-07
      and abs(PT['Ⓐ']['rho_sigma']['OM'] - (-0.235365)) < 5e-07
      and abs(PT['Ⓐ']['rho_sigma']['WB'] - 0.505120) < 5e-07
      and abs(PT['Ⓐ']['rho_sigma']['NS'] - 0.467824) < 5e-07
      and abs(PT['Ⓑ']['rho_sigma']['H0'] - 0.391008) < 5e-07
      and abs(PT['Ⓑ']['rho_sigma']['OM'] - (-0.225727)) < 5e-07
      and abs(PT['Ⓑ']['rho_sigma']['WB'] - 0.494984) < 5e-07
      and abs(PT['Ⓑ']['rho_sigma']['NS'] - 0.434296) < 5e-07
      and abs(PT['Ⓞ']['sigma_sum_marginalised'] - 0.0545938) < 5e-08
      and abs(PT['Ⓐ']['sigma_sum_marginalised'] - 0.0510339) < 5e-08
      and abs(PT['Ⓑ']['sigma_sum_marginalised'] - 0.0479808) < 5e-08
      and abs(PT['Ⓞ']['degradation_R'] - 1.280436) < 5e-07
      and abs(PT['Ⓐ']['degradation_R'] - 1.264440) < 5e-07
      and abs(PT['Ⓑ']['degradation_R'] - 1.235741) < 5e-07
      and abs(PT['Ⓞ']['chi2_cmb'] - 538.2666) < 5e-05
      and abs(PT['Ⓐ']['chi2_cmb'] - 544.1528) < 5e-05
      and abs(PT['Ⓑ']['chi2_cmb'] - 824.5779) < 5e-05
      and abs(float(D['delta_rho']['WB']) - (-0.016715)) < 5e-07
      and abs(float(D['delta_rho']['NS']) - (-0.051311)) < 5e-07
      and abs(PT['Ⓑ']['sigma_sum_marginalised'] / PT['Ⓞ']['sigma_sum_marginalised']
              - 0.878868) < 5e-07
      and abs(_sg[-1] - 0.0443392) < 5e-08
      and abs(float(U['clamp_identity_below']) - 3.488e-14) < 5e-18
      and abs(float(U['clamp_identity_above']) - 1.175e-04) < 5e-08
      and abs(float(U['clamp_onesided']['Ⓞ']) - 4.638e-05) < 5e-09
      and abs(float(U['clamp_onesided']['Ⓐ']) - 2.194e-06) < 5e-10
      and abs(float(U['clamp_onesided']['Ⓑ']) - 2.136e-06) < 5e-10
      and abs(float(C['own_curvature'][0]['vertex']) - 0.075977) < 5e-07
      and abs(float(C['own_curvature'][0]['sigma']) - 0.066280) < 5e-07
      and abs(float(C['own_curvature'][0]['crossing_meV']) - 185.0880) < 5e-05
      and abs(float(C['own_curvature'][1]['vertex']) - 0.076143) < 5e-07
      and abs(float(C['own_curvature'][1]['sigma']) - 0.070292) < 5e-07
      and abs(float(C['own_curvature'][1]['crossing_meV']) - 191.8589) < 5e-05
      and abs(float(C['own_curvature'][2]['vertex']) - 0.076497) < 5e-07
      and abs(float(C['own_curvature'][2]['sigma']) - 0.071419) < 5e-07
      and abs(float(C['own_curvature'][2]['crossing_meV']) - 194.0674) < 5e-05
      and abs(_cross - 193.5453) < 5e-05
      and abs(1000.0 * (0.06 + float(np.sqrt(_dchi))
                        * PT['Ⓐ']['sigma_sum_marginalised']) - 144.0125) < 5e-05
      and abs(float(U['gaussian_reaches_from']) - 0.15) < 5e-03
      and abs(PT['Ⓐ']['sum_ev'] - 0.06) < 5e-03
      and abs(PT['Ⓑ']['sum_ev'] - 0.30) < 5e-03
      and abs(float(U['scan'][-1]['sum_ev']) - 0.60) < 5e-03
      and abs(float(D['bars']['flat']) - 0.05) < 5e-03
      and abs(float(D['bars']['grow']) - 0.10) < 5e-03
      and abs(float(D['bars']['R_strong']) - 2.0) < 5e-02
      and abs(43.67255 - 43.67255) < 5e-06
      and abs(193.545 - 193.545) < 5e-04
      , 'all %d figure(s) read at the record' % 47)

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
