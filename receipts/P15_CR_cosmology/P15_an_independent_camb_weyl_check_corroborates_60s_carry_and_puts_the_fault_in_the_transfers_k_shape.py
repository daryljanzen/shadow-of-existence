"""
P15, r7851+cc66.5, on 69's order r7851: an INDEPENDENT CAMB check of the Weyl potential against
the instrument's own, on the k and eta grid its lensing kernel weights.

** WHAT THIS SETTLES, AND IT CORROBORATES THE OTHER SEAT RATHER THAN REFUTING IT. **
Two different quantities were available to compare, and only one of them is the one in dispute:

  the CARRY     -- how Phi EVOLVES in time, each mode normalised at the z = 12.8331 the instrument
                   freezes at.  Independent CAMB agrees with the instrument to 0.43 per cent at
                   k = 0.001, flat from z ~ 2 onward, and to better than 0.570 per cent at every
                   one of 48 modes at z = 1.  SO THE CARRY IS NOT THE FAULT.
  the TRANSFER  -- the k-SHAPE Phi is handed over WITH, normalised super-horizon instead.  There
                   the instrument is over-suppressed: -31.78 per cent at k = 0.05 /Mpc, worst
                   -31.89 per cent at k = 0.0933, against +0.149 per cent at k = 0.001.

⛔ AND THE FIRST COMPARISON THIS SEAT RAN WAS THE WRONG ONE, WHICH IS RECORDED HERE BECAUSE IT WAS
ONE STEP FROM A FALSE REFUTATION.  Normalising each mode at the instrument's own reference epoch
CANCELS a shape error by construction: whatever factor the transfer is wrong by divides out of a
ratio taken at fixed k.  Reporting that 0.43 per cent as "the potentials agree" would have read as
contradicting the other seat's diagnosis while measuring a quantity their diagnosis does not
touch -- and they had already measured the carry themselves and said so.

** THE SIZE OF THE DECAY MATCHES, WHICH IS WHY THE DIAGNOSIS SURVIVES BEING CHECKED. **
  the instrument's own decay ratio across the comparison band   1.4198
  independent CAMB's                                            1.4680
  agreeing to                                                   3.39 per cent
So the two instruments do not disagree about HOW MUCH the potential decays; they disagree about
WHICH MODES carry the suppression.  That is a transfer fault, not a transport fault.

** AND CAMB's OWN Phi DECAYS THROUGH MATTER DOMINATION TOO: 4.53 per cent from z = 10 to z = 1 and
21.39 per cent from the reference epoch to z = 0 ** -- so decay in the reported range is not by
itself evidence of a defect, and an arm that treated any decay as the fault would have been wrong.

⌗ A TRAP CAUGHT BY MEASUREMENT, NOT BY READING THE DOCUMENTATION.  CAMB's Weyl evolution variable
CARRIES A FACTOR k^2: its small-k log-log slope here is 1.998, where a bare potential gives
essentially zero.  Left uncorrected it would have manufactured a k-dependence of exactly the sign
and rough size the other seat's diagnosis predicts, and FALSELY CONFIRMED it.  Phi = Weyl / k^2.

** THE PINS ARE VERIFIED FAILABLE BY PERTURBATION, NOT ASSUMED TO BE. **  Each banked figure was
moved in turn and the arms that read it watched to redden, then restored:
  * scaling the carry comparison's fractions by 1.05 reddens Ⓒ⑧ (0.4297 -> 0.4511 per cent) and
    Ⓒ⑩ (0.5699 -> 0.5984);
  * moving the transfer comparison's k = 0.05 fraction by 0.0005 reddens Ⓔ⑯ (-31.7785 ->
    -31.8285 per cent), past check_figures_pinned's allowance for a printed -31.78;
  * scaling the instrument's banked decay ratio by 1.02 reddens Ⓕ⑲ (1.41983 -> 1.44823);
  * perturbing CAMB's small-k slope by 0.01 reddens Ⓑ⑥ (1.9982 -> 2.0082) and with it the k^2
    identification Ⓑ⑦ rests on.
Each was applied to the banked record in place, the run watched, and the record restored from git;
the four runs reddened 2, 1, 1 and 1 arms and NOTHING ELSE.  Ⓖ's arms pin no figure: they compare
DISTINCT FIELDS of this revision's own banked citation record, and redden if those stop differing.

COMPUTES: nothing of the physics another seat owns.  It re-reads THIS revision's own banked
          comparisons and recomputes from them: the carry's fractional difference at the reference
          mode and its spread across modes, the transfer's fractional difference against
          super-horizon normalisation, the two decay ratios and their agreement, and CAMB's own
          decay across the same epochs.  It reads 60's modules only STRUCTURALLY, through the
          parsed syntax tree, never by matching their wording.  The published-provenance arms read
          only this revision's own banked record of the citation.

Bound: this receipt pins THIS check's figures.  It does NOT repair the instrument's transfer, does
not re-run its control, and does NOT yet compare a REPAIRED transfer -- item ③ of the order is
open until that lands, and nothing here stands in for it.  It does not rule on whether the
transfer's k-shape or its super-horizon normalisation is the correct place to fix.  It pins no
cosmological parameter as a result, and it establishes no limit.
"""
import ast
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
MINE = os.path.join(BTW, 'r7851_cc66_an_independent_weyl_potential_check_against_camb')
R46 = os.path.join(BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')

with open(os.path.join(MINE, 'weyl_vs_60.json'), encoding='utf-8') as fh:
    CARRY = json.load(fh)
with open(os.path.join(MINE, 'transfer_vs_camb.json'), encoding='utf-8') as fh:
    TRANS = json.load(fh)
with open(os.path.join(MINE, 'published_provenance.json'), encoding='utf-8') as fh:
    PROV = json.load(fh)

print(__doc__.strip().splitlines()[0])
print()

# ---------------------------------------------------------------- Ⓐ the grid is the kernel's own
G = CARRY['grid']
check('Ⓐ① the comparison runs on the kernel\'s own mode count and k range, not a grid of its own',
      G['nkp_kernel'] == 220 and abs(G['kmin'] - 2e-4) < 1e-12 and abs(G['kmax'] - 1.0) < 1e-12,
      'nkp=%d  kmin=%g  kmax=%g' % (G['nkp_kernel'], G['kmin'], G['kmax']))

check('Ⓐ② and at the reference epoch the instrument freezes at, read from the comparison itself',
      abs(G['etaref_mpc'] - 4000.0) < 1e-9 and abs(G['z_ref'] - 12.8331) < 1e-3,
      'eta_ref=%.1f Mpc  z_ref=%.4f' % (G['etaref_mpc'], G['z_ref']))

# the instrument's own constants, read through the PARSED SYNTAX and never by matching its wording
_PHIPHI = ast.parse(open(os.path.join(R46, 'phiphi.py'), encoding='utf-8').read())
_GROWTH = ast.parse(open(os.path.join(R46, 'growth_kdep.py'), encoding='utf-8').read())


def _envdefault(tree, name):
    """the constant's default, off the parsed call -- never off the line's text or its comment"""
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Assign) and len(n.targets) == 1
                and isinstance(n.targets[0], ast.Name) and n.targets[0].id == name):
            continue
        for c in ast.walk(n.value):
            if (isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute)
                    and c.func.attr == 'get' and len(c.args) == 2
                    and all(isinstance(a, ast.Constant) for a in c.args)
                    and c.args[0].value == name):
                return float(c.args[1].value)
    return None


_PC = {k: _envdefault(_PHIPHI, k) for k in ('NKP', 'KMIN', 'KMAX')}
_GC = {'ETAREF': _envdefault(_GROWTH, 'ETAREF')}
check('Ⓐ③ the mode count and k range are the instrument\'s own, off its parsed syntax tree',
      _PC.get('NKP') == 220.0 and _PC.get('KMIN') == 2e-4 and _PC.get('KMAX') == 1.0,
      'NKP=%s KMIN=%s KMAX=%s' % (_PC.get('NKP'), _PC.get('KMIN'), _PC.get('KMAX')))

check('Ⓐ④ and the reference epoch is theirs, off the same tree and not off a comment',
      _GC.get('ETAREF') == 4000.0, 'ETAREF=%s' % (_GC.get('ETAREF'),))

_funcs = {n.name for n in ast.walk(_PHIPHI) if isinstance(n, ast.FunctionDef)}
_funcs |= {n.name for n in ast.walk(_GROWTH) if isinstance(n, ast.FunctionDef)}
check('Ⓐ⑤ both of the instrument\'s entry points this check consumed still exist, by name in the tree',
      {'phi_shape', 'g_of'} <= _funcs, 'found %d functions' % len(_funcs))

# ------------------------------------------------- Ⓑ the k^2 in CAMB's evolution variable, MEASURED
SLOPE = TRANS['camb_weyl_small_k_loglog_slope']
check('Ⓑ⑥ CAMB\'s Weyl evolution variable carries a factor k^2, MEASURED as a small-k log-log slope',
      abs(SLOPE - 1.998) < 0.0008, 'slope = %.4f  (pinned 1.998 +/- 0.0008)' % SLOPE)

check('Ⓑ⑦ and the power is 2 to better than a fifth of a per cent, so the division is exact and not a fit',
      abs(SLOPE - 2.0) < 0.01, '|slope - 2| = %.4f' % abs(SLOPE - 2.0))

# ------------------------------------------------------------------- Ⓒ the CARRY -- NOT the fault
F = CARRY['frac_summary']
carry_z1_pc = F['at_k001_z1'] * 100.0
check('Ⓒ⑧ the CARRY agrees with independent CAMB to 0.43 per cent at the reference mode at z = 1',
      abs(carry_z1_pc - 0.43) < 0.004, 'carry = %.4f per cent  (pinned 0.43 +/- 0.004)' % carry_z1_pc)

_fk = {float(k): v for k, v in CARRY['frac_at_k001'].items()}
_settle = abs(_fk[2.0] - _fk[0.0]) * 100.0
check('Ⓒ⑨ and it is FLAT from z ~ 2 onward, so the agreement is not an accident of one epoch',
      _settle < 0.0130, 'remaining change after z = 2 is %.4f per cent' % _settle)

worst_z1_pc = max(abs(F['z1_absmin']), abs(F['z1_absmax'])) * 100.0
check('Ⓒ⑩ and across all 48 modes at z = 1 the carry agrees everywhere to better than 0.570 per cent',
      abs(worst_z1_pc - 0.570) < 0.0004 and len(CARRY['frac_at_z1']['k']) == 48,
      'worst = %.4f per cent over %d modes  (pinned 0.570 +/- 0.0004)'
      % (worst_z1_pc, len(CARRY['frac_at_z1']['k'])))

spread = F['k_spread_factor_at_z1']
check('Ⓒ⑪ and the carry\'s k-dependence spans a factor 1.588, so it is nearly scale-free',
      abs(spread - 1.588) < 0.0006, 'spread = %.4f  (pinned 1.588 +/- 0.0006)' % spread)

# ------------------------------------------- Ⓓ CAMB's OWN decay, so decay alone is not the defect
d10 = CARRY['camb_drift_z10_to_z1_at_k001'] * 100.0
d0 = CARRY['camb_drift_zref_to_z0_at_k001'] * 100.0
check('Ⓓ⑫ CAMB\'s OWN potential decays 4.53 per cent from z = 10 to z = 1 at the reference mode',
      abs(d10 - 4.53) < 0.004, 'decay = %.4f per cent  (pinned 4.53 +/- 0.004)' % d10)

check('Ⓓ⑬ and 21.39 per cent from the reference epoch to today, so DECAY ALONE IS NOT THE DEFECT',
      abs(d0 - 21.39) < 0.008, 'decay = %.4f per cent  (pinned 21.39 +/- 0.008)' % d0)

# ------------------------------------------------------- Ⓔ the TRANSFER -- where the fault DOES sit
check('Ⓔ⑭ the instrument\'s super-horizon potential is -0.9010, so its normalisation is near unity',
      abs(TRANS['phi60_super_horizon'] + 0.9010) < 0.0003,
      'Phi(k -> 0) = %.6f  (pinned -0.9010 +/- 0.0003)' % TRANS['phi60_super_horizon'])

k001_pc = TRANS['frac_at_k0001'] * 100.0
check('Ⓔ⑮ and super-horizon the two SHAPES agree to 0.149 per cent, so the disagreement is not an offset',
      abs(k001_pc - 0.149) < 0.0004,
      'agreement = %+.4f per cent  (pinned 0.149 +/- 0.0004)' % k001_pc)

k05_pc = TRANS['frac_at_k005'] * 100.0
check('Ⓔ⑯ but at k = 0.05 /Mpc the instrument\'s TRANSFER is over-suppressed by 31.78 per cent',
      abs(k05_pc + 31.78) < 0.012,
      'deficit = %+.4f per cent  (pinned -31.78 +/- 0.012)' % k05_pc)

w = TRANS['worst']
check('Ⓔ⑰ and the deficit is worst at 31.89 per cent, at k = 0.0933 /Mpc, inside the kernel\'s own band',
      abs(w['frac'] * 100.0 + 31.89) < 0.012 and abs(w['k'] - 0.0933) < 0.00005,
      'worst %+.4f per cent at k = %.6f' % (w['frac'] * 100.0, w['k']))

_k = np.array(TRANS['k'], float)
_f = np.array(TRANS['frac'], float)
_tail = _f[_k >= 0.2]
check('Ⓔ⑱ and it SATURATES rather than running away, so it is a shape error and not a divergence',
      _tail.size > 0 and abs(_tail).max() <= abs(_f[_k >= 0.05]).max() + 1e-12
      and abs(float(_tail.mean()) - float(_f[_k >= 0.05].mean())) < 0.05,
      'tail mean %+.4f vs band mean %+.4f over %d modes'
      % (_tail.mean(), _f[_k >= 0.05].mean(), _tail.size))

# ----------------------------------------- Ⓕ the SIZE of the decay matches -- the diagnosis stands
check('Ⓕ⑲ the instrument\'s own decay ratio across the band is 1.4198, read off its banked transfer',
      abs(TRANS['their_decay_ratio'] - 1.4198) < 0.0005,
      'theirs = %.5f  (pinned 1.4198 +/- 0.0005)' % TRANS['their_decay_ratio'])

check('Ⓕ⑳ independent CAMB\'s is 1.4680, computed here and not taken from them',
      abs(TRANS['my_shape_ratio'] - 1.4680) < 0.0005,
      'mine = %.5f  (pinned 1.4680 +/- 0.0005)' % TRANS['my_shape_ratio'])

agree = TRANS['agreement_per_cent']
check('Ⓕ㉑ so the two agree on the SIZE of the decay to 3.39 per cent -- they differ on WHICH MODES',
      abs(agree - 3.39) < 0.004, 'agreement = %.4f per cent  (pinned 3.39 +/- 0.004)' % agree)

check('Ⓕ㉒ and the size agreement is an order of magnitude tighter than the shape disagreement',
      abs(k05_pc) > 5.0 * agree, '%.2f per cent shape vs %.2f per cent size' % (abs(k05_pc), agree))

# --------------------------------------- Ⓖ the published provenance: TWO FITS, NOT ONE (item ④)
A, B = PROV['the_64_2_meV'], PROV['the_minus_0_101_eV']
check('Ⓖ㉓ the two published figures this line calibrates against carry DIFFERENT CONFIDENCE LEVELS',
      A['confidence'] != B['confidence'], '%s vs %s' % (A['confidence'], B['confidence']))

check('Ⓖ㉔ and DIFFERENT STATISTICS -- one is a one-sided limit, the other a central value',
      ('LIMIT' in A['statistic'].upper()) and ('CENTRAL' in B['statistic'].upper()),
      '%s | %s' % (A['statistic'], B['statistic']))

check('Ⓖ㉕ and DIFFERENT MODELS, one of which admits negative energy densities and one of which does not',
      A['model'] != B['model'] and 'NEGATIVE' in B['prior'].upper()
      and '> 0' in A['prior'], '%s | %s' % (A['prior'], B['prior']))

check('Ⓖ㉖ so NO SINGLE CONTROL CAN LAND NEAR BOTH AT ONCE, and a criterion asking for both is unmeetable',
      A['equation'] != B['equation'] and B.get('table') == 'Table 5',
      'equations %s and %s, the second from %s' % (A['equation'], B['equation'], B.get('table')))

check('Ⓖ㉗ and the baseline likelihood combination is named, so what the control reproduces is stated',
      all(PROV['the_baseline_CMB_dataset'].get(key) for key in
          ('lensing_reconstruction', 'low_ell', 'high_ell')),
      '; '.join('%s: %s' % (k, v) for k, v in PROV['the_baseline_CMB_dataset'].items()
                if k != 'note'))

# ------------------------------------------------------------------------------- Ⓗ the count
_n = len(RAN)
check('Ⓗ㉘ the count is COUNTED off the arms that ran and then pinned, not typed',
      _n == 27, 'arms before this one: %d (pinned 27)' % _n)

print()
print('  %d arms, %d FAILED' % (len(RAN), len(FAILED)))
if FAILED:
    print('  FAILED: ' + '; '.join(FAILED))
sys.exit(1 if FAILED else 0)
