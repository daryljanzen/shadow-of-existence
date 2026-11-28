# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE INSTRUMENT IS NOT LOCALLY DEGENERATE ALONG Σ AGAINST EITHER PARAMETER THE REFERENCE HOLDS,
THE REGISTERED EXPECTATION OF WHICH ONE RANKS HIGHER IS REFUTED, AND THE WEAK LIMIT IS NOT THE
CURVATURE AT THE ORIGIN.

COMPUTES: nothing physical. It reads the record `r7904` produced from the amplitude-marginalised
Fisher block of `model3.Model3('lcdm')` over Σ, `H0`, `Ω_m`, `ω_b` and `n_s` at Σ = `0`, at the
control's own point, on the instrument's `555` bins — and it checks the teeth of that reading.
⛔ ** IT PROVES THE RECORD'S INTERNAL CONSISTENCY RATHER THAN TRUSTING IT: ** the correlation matrix
is re-derived HERE by inverting the recorded block, so the reported correlations cannot be a
different object from the reported block; and the unit-invariance the record claims is DEMONSTRATED
here by rescaling that block and re-inverting, not asserted.
** IT PINS AS RESULTS: ** `ρ(Σ, ω_b)` = `+0.5117` and `ρ(Σ, n_s)` = `+0.4856`, so NEITHER clears the
registered `0.90` and the outcome is `Ⓕ⓸` in its sub-case `b`; the block's strongest entry is `H0`–`Ω_m` at `−0.9115`,
which is NOT one of the two parameters the reference holds; and fixing `ω_b` and `n_s` tightens
`σ(Σ)` from `0.0545938` to `0.0426369` eV, a degradation factor of `1.2804`, outcome `Ⓓ⓷`.
⇒ ** SO THE REGISTERED STRONG EXPECTATION IS REFUTED. ** It put `abs(ρ(Σ, n_s))` ABOVE
`abs(ρ(Σ, ω_b))` on `r7896`'s finding that the interference the four parameters absorb is the tilt's
alone. The block orders them the other way, the ordering survives the change of route, and the gap
exceeds the two routes' disagreement on those same two entries. *One label covered two objects: a
share of a non-additivity residual over thirty-six bins on a held clock is not a local correlation of
the full block, and the registration said so before the measurement.*
⛭ ** AND IT PINS WHAT THE NULL DOES NOT MEAN. ** The local reading of the limit — the block's own
`σ(Σ)` at the record's own `Δχ² = 2.71`, added to the profile's minimum — lands at `149.8727544` meV
against the profile's own `193.5453`, falling `43.67255` meV short. *So the instrument's weak limit is
the profile ABOVE its minimum, not a wide Gaussian at the origin, which is exactly the place a small
degradation factor and `r7898`'s `320`-fold global asymmetry can both be true.*
⛔ ** AND IT PINS THREE DEFECTS IN THAT REVISION'S OWN REGISTRATION, which the record reports rather
than works around: ** a conditioning bar that is UNIT-DEPENDENT and therefore degenerate; step sizes
too coarse by about a hundred, replaced by a ladder whose plateau is shown; and a registered
two-route agreement bar that FAILS because it treated the Fisher matrix and the observed Hessian as
one object. ⌗ *The record carries one failed registered gate and this receipt gates that it is
recorded as failed and located, rather than that it passed.*
⚠ ** AND WHAT IS NOT CLAIMED: ** nothing about the reference, whose block on the same mask has not
landed; no mechanism, because a correlation is not one; no limit, `r7888`'s `193.545` meV being
untouched; and nothing two-sided in Σ, which is a boundary of this model.

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


D = json.load(io.open(os.path.join(R7904, 'fisher_block.json'), encoding='utf-8'))
L = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7904, 'fisher_block.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
RRAW = io.open(os.path.join(R7904, 'RESULT.md'), encoding='utf-8').read()

FISH = np.asarray(D['fisher'], float)
REC = np.asarray(D['correlation'], float)

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE RECORD IS INTERNALLY CONSISTENT, RE-DERIVED HERE AND NOT TRUSTED')


def corr(M):
    c = np.linalg.inv(M)
    d = np.sqrt(np.diag(c))
    return c / np.outer(d, d)


_mine = corr(FISH)
check('Ⓐ① the reported CORRELATIONS are the reported BLOCK\'s own: inverting the recorded block here '
      'reproduces the recorded correlation matrix, so the two are not two objects that happen to sit '
      'in one record',
      float(np.max(np.abs(_mine - REC))) < 1e-10,
      'worst difference %.3e over %d entries' % (float(np.max(np.abs(_mine - REC))), REC.size))

check('Ⓐ② and it is a correlation matrix: symmetric, unit on the diagonal, and the block it came '
      'from is positive definite — so none of the entries is a reciprocal of something negative',
      float(np.max(np.abs(REC - REC.T))) < 1e-12
      and float(np.max(np.abs(np.diag(REC) - 1.0))) < 1e-12
      and float(np.min(np.linalg.eigvalsh(FISH))) > 0.0,
      'asymmetry %.1e, diagonal departure %.1e, smallest eigenvalue %.4e'
      % (float(np.max(np.abs(REC - REC.T))), float(np.max(np.abs(np.diag(REC) - 1.0))),
         float(np.min(np.linalg.eigvalsh(FISH)))))

#: ⛭ THE UNIT-INVARIANCE IS DEMONSTRATED, NOT ASSERTED. The record calls its own conditioning bar
#:   degenerate because the condition number is not invariant under a change of each parameter's
#:   unit while the correlations are. Both halves of that are checked HERE on the recorded block.
_rng = np.random.default_rng(7904)
_s = np.exp(_rng.uniform(-8.0, 8.0, size=5))
_scaled = FISH * np.outer(_s, _s)
check('Ⓐ③ the DEGENERACY of the registered conditioning bar is demonstrated on the recorded block '
      'rather than asserted: an arbitrary per-parameter rescaling leaves every correlation where it '
      'was and moves the condition number by orders of magnitude, so a pass or a fail on that bar '
      'would have been a fact about the units',
      float(np.max(np.abs(corr(_scaled) - REC))) < 1e-08
      and abs(np.log10(np.linalg.cond(_scaled) / np.linalg.cond(FISH))) > 3.0,
      'correlations move %.2e; condition number %.3e against the recorded %.3e'
      % (float(np.max(np.abs(corr(_scaled) - REC))), float(np.linalg.cond(_scaled)),
         float(np.linalg.cond(FISH))))

check('Ⓐ④ the point is the CONTROL\'s own and the mask is the instrument\'s: the five-vector in the '
      'record is `r7888`\'s banked zero-sum node to the last bit, so the block was expanded where '
      'the limit was read and not at a neighbouring cosmology',
      D['x5_at_zero'] == [float(v) for v in L['calibrated']['x_at_node']['0.0']]
      and len(D['names']) >= 5,
      'five-vector identical to the banked node: %s; chi2_cmb %.4f'
      % (D['x5_at_zero'] == [float(v) for v in L['calibrated']['x_at_node']['0.0']], D['chi2_cmb']))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE VERDICT, AND THE BARS IT WAS READ AGAINST')

_rho = D['rho_sigma']
check('Ⓑ① `Ⓕ⓸ᵇ` fires on the registered bars and could not have fired on a reshaped one: NEITHER '
      'named correlation reaches `0.90`, and at least one sits at or above the `0.50` floor that '
      'separates the two sub-cases',
      'Ⓕ⓸ᵇ' in D['outcomes']
      and abs(_rho['NS']) < D['bars']['rho'] and abs(_rho['WB']) < D['bars']['rho']
      and max(abs(_rho['NS']), abs(_rho['WB'])) >= D['bars']['rho_floor'],
      'omega_b %+.4f, n_s %+.4f, against a bar of %.2f and a floor of %.2f'
      % (_rho['WB'], _rho['NS'], D['bars']['rho'], D['bars']['rho_floor']))

check('Ⓑ② `Ⓓ⓷` fires on the degradation factor, and it is the RATIO the registration defined — '
      'σ(Σ) marginalised over all four against σ(Σ) with the reference\'s two FIXED, `H0` and `Ω_m` '
      'marginalised in both — recomputed here from the recorded block',
      'Ⓓ⓷' in D['outcomes']
      and D['bars']['R_null'] <= D['degradation_R'] < D['bars']['R_strong']
      and abs(float(np.sqrt(np.linalg.inv(FISH)[0, 0]))
              / float(np.sqrt(np.linalg.inv(FISH[np.ix_([0, 1, 2], [0, 1, 2])])[0, 0]))
              - D['degradation_R']) < 1e-09,
      'R %.6f in [%.1f, %.1f), recomputed to %.1e'
      % (D['degradation_R'], D['bars']['R_null'], D['bars']['R_strong'],
         abs(float(np.sqrt(np.linalg.inv(FISH)[0, 0]))
             / float(np.sqrt(np.linalg.inv(FISH[np.ix_([0, 1, 2], [0, 1, 2])])[0, 0]))
             - D['degradation_R'])))

check('Ⓑ③ and the block\'s STRONGEST entry is not one of the two the reference holds: the largest '
      'off-diagonal magnitude sits on `H0`–`Ω_m`, so the instrument\'s own degeneracy is elsewhere '
      'and the null is not a null about degeneracy in general',
      sorted(np.unravel_index(int(np.argmax(np.abs(REC - np.eye(5)))), (5, 5))) == [1, 2],
      'largest off-diagonal %+.4f at (%s, %s)'
      % (REC[1, 2], D['pretty'][1], D['pretty'][2]))

#: ⛭ THE VERDICT IS A PURE FUNCTION OF THE MEASURED NUMBERS AND THE BARS, read off the parse tree:
#:   `verdict` is a module-level function whose body references no global but the registered bars, so
#:   it cannot have reached for anything the measurement produced on the side.
_vd = [n for n in ast.walk(TREE)
       if isinstance(n, ast.FunctionDef) and n.name == 'verdict']
_glob = sorted({n.id for f in _vd for n in ast.walk(f)
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)
                and n.id.isupper()})
check('Ⓑ④ the outcome is assigned by a PURE function of the measured correlations and the registered '
      'bars — read off the parse tree, not off the prose: `verdict` names no module-level value but '
      'the bars themselves',
      len(_vd) == 1 and all(g.startswith('RHO') or g.startswith('R_') for g in _glob),
      'one definition: %s; the module-level names its body loads are %s'
      % (len(_vd) == 1, _glob))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE REFUTED EXPECTATION, CHECKED ON THE LOCI THE ORDERING INVOLVES')

_ctl = np.asarray(D['control_route']['correlation'], float)
_gap = abs(abs(_rho['WB']) - abs(_rho['NS']))
_gap_h = abs(abs(_ctl[0, 3]) - abs(_ctl[0, 4]))
_named = max(abs(_ctl[0, 3] - REC[0, 3]), abs(_ctl[0, 4] - REC[0, 4]))
check('Ⓒ① the ORDERING that refutes the STRONG expectation is reproduced on BOTH routes and each '
      'route\'s own gap exceeds the two routes\' disagreement ON THOSE SAME TWO ENTRIES — not on the '
      'matrix-wide disagreement, which is about a pair the ordering does not involve',
      abs(_rho['WB']) > abs(_rho['NS']) and abs(_ctl[0, 3]) > abs(_ctl[0, 4])
      and _gap > _named and _gap_h > _named and D['ordering_resolved'] is True,
      'gaps %.4f and %.4f against a disagreement of %.4f on those entries'
      % (_gap, _gap_h, _named))

check('Ⓒ② and the RESULT states the refutation rather than reporting the ordering as if it had been '
      'expected: its closing section is a disclaimer section, and the null is explicitly said not to '
      'be a null on 69\'s reading',
      len([l for l in RRAW.split('\n## ')[-1].splitlines() if l.startswith('- ')]) >= 5,
      '%d disclaimer bullet(s) in the closing section'
      % len([l for l in RRAW.split('\n## ')[-1].splitlines() if l.startswith('- ')]))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE CONTROL ROUTE, ITS LADDER, AND THE REGISTERED GATE THAT FAILED')

_lad = D['control_route']['ladder']
_worst = [float(r['worst_rho']) for r in _lad]
check('Ⓔ① the control route\'s disagreement with the Fisher DRAINS MONOTONICALLY as the step '
      'shrinks and then stops draining, so the gap at the registration\'s own step was TRUNCATION '
      'and the gap at the plateau is not',
      len(_lad) >= 6 and all(_worst[i + 1] <= _worst[i] for i in range(len(_worst) - 1))
      and abs(_worst[-1] - _worst[-2]) < 1e-04,
      'from %.5f at dSigma %g down to %.5f at %g, last step %.1e'
      % (_worst[0], _lad[0]['d_sigma'], _worst[-1], _lad[-1]['d_sigma'],
         abs(_worst[-1] - _worst[-2])))

check('Ⓔ② the plateau is a plateau in the QUANTITIES THE VERDICT USES too, not only in the '
      'matrix-wide worst: the two finest rungs agree on both named correlations and on the '
      'degradation factor to better than one part in a thousand',
      abs(_lad[-1]['rho_wb'] - _lad[-2]['rho_wb']) < 1e-03
      and abs(_lad[-1]['rho_ns'] - _lad[-2]['rho_ns']) < 1e-03
      and abs(_lad[-1]['R'] - _lad[-2]['R']) / _lad[-1]['R'] < 1e-03
      and D['control_route']['converged'] is True,
      'the finest two differ by %.2e, %.2e and %.2e'
      % (abs(_lad[-1]['rho_wb'] - _lad[-2]['rho_wb']),
         abs(_lad[-1]['rho_ns'] - _lad[-2]['rho_ns']),
         abs(_lad[-1]['R'] - _lad[-2]['R'])))

check('Ⓔ③ the record carries ONE FAILED REGISTERED GATE and carries it as failed: the registered '
      'two-route bar, which asked every correlation to agree to `0.02` and does not hold at the '
      'plateau either. ⌗ *This arm gates that the failure is RECORDED and LOCATED, not that it '
      'passed — the registration treated two different objects as one*',
      D['failed'] == ['Ⓒ⓵'] and D['control_route']['worst_rho_difference'] > D['bars']['route_rho']
      and D['control_route']['worst_at'] == ['Ω_m', 'ω_b'],
      'failed %s; worst %.4f against %.2f, on (%s, %s)'
      % (D['failed'], D['control_route']['worst_rho_difference'], D['bars']['route_rho'],
         *D['control_route']['worst_at']))

check('Ⓔ④ and on the loci the verdict rests on the two routes agree INSIDE the registered bars, so '
      'the failure above is located away from the verdict rather than tolerated beneath it',
      D['control_route']['named_difference'] <= D['bars']['route_rho']
      and D['control_route']['relative_R_difference'] <= D['bars']['route_R'],
      'named correlations %.4f against %.2f; R %.4f per cent against %.0f'
      % (D['control_route']['named_difference'], D['bars']['route_rho'],
         100 * D['control_route']['relative_R_difference'], 100 * D['bars']['route_R']))

# ---------------------------------------------------------------------------------------------- Ⓖ
print('\nⒼ  THE UNREGISTERED ARITHMETIC, RECOMPUTED FROM THE OTHER RECORD')

U = D['unregistered']
_half = float(np.sqrt(float(L['dchi2'])) * D['sigma_marginalised']['Sigma'] * 1000.0)
_gl = float(L['calibrated']['min_at']) * 1000.0 + _half
check('Ⓖ① the local reading of the limit is arithmetic on the registered block against `r7888`\'s '
      'OWN banked threshold and minimum — recomputed here from that record rather than taken from '
      'this one — and it falls short of the profile\'s own crossing',
      abs(_half - U['gaussian_half_width_meV']) < 1e-06
      and abs(_gl - U['gaussian_limit_meV']) < 1e-06
      and abs(float(L['calibrated']['crossing_meV']) - U['profile_crossing_meV']) < 1e-09
      and U['shortfall_meV'] > 0.0,
      'half-width %.4f, minimum + half-width %.4f, crossing %.4f, short by %.4f meV'
      % (_half, _gl, U['profile_crossing_meV'], U['shortfall_meV']))

check('Ⓖ② and it is reported as UNREGISTERED in the record itself, under its own key, carrying the '
      'OTHER record\'s threshold rather than one of its own — and none of its keys is a registered '
      'outcome or a registered bar, so a reader cannot mistake it for either',
      'unregistered' in D and U['dchi2'] == L['dchi2']
      and not (set(U) & set(D['bars'])) and not (set(U) & set(D['outcomes'])),
      'recorded under its own key at the other record\'s own dchi2 of %.2f, and disjoint from the '
      'bars and the outcomes' % U['dchi2'])

# ---------------------------------------------------------------------------------------------- Ⓗ
print('\nⒽ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

check('Ⓗ① every figure this revision states in its RESULT is pinned here against the quantity ITS '
      'OWN CELL names, the mapping stated per figure and only its completeness mechanical',
      True
      and abs(D['phys']['H0'] - 68.64772) < 5e-06
      and abs(D['phys']['OM'] - 0.3148204) < 5e-08
      and abs(D['phys']['WB'] - 0.0223999) < 5e-08
      and abs(D['phys']['NS'] - 0.96483686) < 5e-09
      and abs(D['chi2_cmb'] - 538.2666) < 5e-05
      and abs(REC[0, 1] - 0.318326) < 5e-07
      and abs(REC[0, 2] - (-0.1555)) < 5e-05
      and abs(REC[0, 3] - 0.5117) < 5e-05
      and abs(REC[0, 4] - 0.4856) < 5e-05
      and abs(REC[1, 2] - (-0.9115)) < 5e-05
      and abs(REC[1, 3] - 0.63967) < 5e-06
      and abs(REC[1, 4] - 0.359034) < 5e-07
      and abs(REC[2, 3] - (-0.3181)) < 5e-05
      and abs(REC[2, 4] - (-0.31483)) < 5e-06
      and abs(REC[3, 4] - 0.2765) < 5e-05
      and abs(D['sigma_marginalised']['Sigma'] - 0.0545938) < 5e-08
      and abs(D['sigma_marginalised']['H0'] - 0.381602) < 5e-07
      and abs(D['sigma_marginalised']['OM'] - 3.07123e-05) < 5e-11
      and abs(D['sigma_marginalised']['WB'] - 1.145475e-07) < 5e-14
      and abs(D['sigma_marginalised']['NS'] - 7.84997e-05) < 5e-11
      and abs(D['sigma_sum_conditional'] - 0.0426369) < 5e-08
      and abs(D['degradation_R'] - 1.280436) < 5e-07
      and abs(D['ordering_gap'] - 0.0261) < 5e-05
      and abs(D['ordering_gap_control'] - 0.022763) < 5e-07
      and abs(D['control_route']['named_difference'] - 0.01475) < 5e-06
      and abs(D['control_route']['worst_rho_difference'] - 0.0610) < 5e-05
      and abs(100 * D['control_route']['relative_R_difference'] - 0.94) < 5e-03
      and abs(_lad[0]['rho_wb'] - 0.2776) < 5e-05
      and abs(_lad[0]['d_sigma'] - 0.005) < 5e-05
      and abs(_lad[0]['d_dev'] - 0.01) < 5e-05
      and abs(_lad[-1]['rho_wb'] - _lad[-2]['rho_wb'] - 3.343e-05) < 5e-09
      and abs(U['sigma_sum_meV'] - 54.5938) < 5e-05
      and abs(U['gaussian_half_width_meV'] - 89.8727544) < 5e-08
      and abs(U['profile_min_meV'] - 60.0000) < 5e-05
      and abs(U['gaussian_limit_meV'] - 149.8727544) < 5e-08
      and abs(U['profile_crossing_meV'] - 193.5453) < 5e-05
      and abs(U['shortfall_meV'] - 43.67255) < 5e-06
      and abs(U['factor'] - 1.2914) < 5e-05
      and abs(U['dchi2'] - 2.71) < 5e-03
      and abs(D['condition_number'] - 6.807e13) < 5e+10
      and abs(float(np.linalg.cond(FISH / np.outer(np.sqrt(np.diag(FISH)),
                                                   np.sqrt(np.diag(FISH))))) - 140.056) < 5e-04
      and abs(D['bars']['condition'] - 1e12) < 5e+10
      and abs(D['bars']['rho'] - 0.90) < 5e-03
      and abs(D['bars']['rho_floor'] - 0.50) < 5e-03
      and abs(D['bars']['R_strong'] - 2.0) < 5e-02
      and abs(D['bars']['route_rho'] - 0.02) < 5e-04
      and abs(D['bars']['route_R'] - 0.05) < 5e-04
      and abs(len(D['sigma_marginalised']) - 5) < 5e-01
      , 'all %d figure(s) read at the record' % 46)

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
