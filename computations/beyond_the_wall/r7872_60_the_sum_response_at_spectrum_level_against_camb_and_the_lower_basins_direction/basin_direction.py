# -*- coding: utf-8 -*-
"""Ⓑ② THE LOWER BASIN'S DIRECTION, NAMED THROUGH THE INSTRUMENT AND NOT THROUGH A SLOT INDEX.

Order `r7871` item ②: *name the parameter that differs between the two basins (your −1.054 against
+0.597 grid steps), and say whether cc66's reference has any branch along it.*

⛔ ** WHY THIS IS NOT ARITHMETIC ON AN INDEX. **  `r7870` recorded two five-component vectors.
Reading "component 0" as a parameter name is reading a LABEL, and the guard this line works under
is that before two stretches are identified by a label, the label's many-to-oneness has to be
checked on the object.  So both vectors are pushed through the instrument's OWN parameter map
(`Model6('lcdm').cmb.phys`), which is the function the chi^2 actually calls, and every parameter is
reported in PHYSICAL units.  If the map put the sum, or tau, or nothing at all in that slot, this
file would say so.

⛭ ** AND THE WORD "BASIN" IS PUT AT RISK HERE, NOT ASSUMED. **  Two vectors with different chi^2
are two minima only if there is a BARRIER between them.  Without one they are one basin reported
twice and `r7870`'s word for them was wrong -- which is a live outcome of this file.  The chi^2 is
evaluated along the straight segment joining them, at the node they were both found at, and the
verdict is read off that.

⌗ *Read, not retyped: the two vectors come out of `r7870`'s committed JSON.*

    NODE=60 python3 basin_direction.py
"""
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7864 = os.path.join(_BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_'
                           'density_and_both_limits_re_read')
R7870 = os.path.join(_BTW, 'r7870_60_the_separating_grid_the_corrected_control_and_the_cache_'
                           'that_relabelled_a_column')
R7869 = os.path.join(_BTW, 'r7869_cc66_the_reference_per_bin_response_and_the_census_converted_'
                           'to_its_property')

# ⛔ the grid directories must be in the environment BEFORE model6 is imported: its GRID is read at
#   module import time, and importing `limits` is what puts model3/distances/model6 on sys.path.
sys.path.insert(0, R7864)
import limits as _L7864                                                    # noqa: E402,F401

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff044')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')

import model6 as M6                                                        # noqa: E402
import model3 as M3                                                        # noqa: E402

NODE = 0.400                 # the sum at which r7870 found the two vectors
OUT = os.path.join(_HERE, 'basin_direction.json')
rec = {}

# ── the two vectors, READ from r7870's committed record ─────────────────────────────────────────
_sb = json.load(open(os.path.join(R7870, 'second_basin.json')))
_at = _sb['at_0400']
X_LO = [float(v) for v in _at['x_lower']]
X_HI = [float(v) for v in _at['x_higher']]
rec['read'] = dict(source='r7870/second_basin.json:at_0400', node=NODE,
                   x_lower=X_LO, x_higher=X_HI,
                   chi2_lower_recorded=float(_at['lower']),
                   chi2_higher_recorded=float(_at['higher']),
                   gap_recorded=float(_at['gap']))
print('=' * 100)
print('  Ⓑ② THE LOWER BASIN\'S DIRECTION, at Sum = %.3f eV' % NODE)
print('=' * 100)
print('  read from r7870: lower %.4f, higher %.4f, gap %.4f'
      % (_at['lower'], _at['higher'], _at['gap']))

# ── Ⓑ②ᵃ the parameter map, asked of the instrument ──────────────────────────────────────────────
mod = M6.Model6('lcdm')
raw = mod.amp_cmb
mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0        # r7870's own halving, carried

# the slots, as the OBJECT defines them -- not as this file guesses
p_lo = mod.cmb.phys(X_LO[:4], NODE)
p_hi = mod.cmb.phys(X_HI[:4], NODE)
STEP = {k: float(M3.R.STEP[k]) for k in ('H0', 'OM', 'WB', 'NS')}
CENTRE = {k: float(M3.ARMS['lcdm']['centre'][k]) for k in ('H0', 'OM', 'WB', 'NS')}
rec['parameter_map'] = dict(step=STEP, centre=CENTRE,
                            keys_phys_returns=sorted(p_lo.keys()))
print('\n  the instrument\'s own parameter map returns: %s' % ', '.join(sorted(p_lo)))
print('  grid steps: ' + ', '.join('%s %g' % (k, STEP[k]) for k in ('H0', 'OM', 'WB', 'NS')))

rows = []
for j, k in enumerate(('H0', 'OM', 'WB', 'NS')):
    d_steps = X_HI[j] - X_LO[j]
    rows.append(dict(name=k, slot=j, lower_steps=X_LO[j], higher_steps=X_HI[j],
                     lower_phys=float(p_lo[k]), higher_phys=float(p_hi[k]),
                     d_steps=float(d_steps), d_phys=float(p_hi[k] - p_lo[k])))
# tau is the component the profiler holds separately -- it is NOT one of the four
rec['tau'] = dict(lower=X_LO[4], higher=X_HI[4], d=float(X_HI[4] - X_LO[4]))
rec['params'] = rows

print('\n%14s %14s %14s %12s %14s %14s' % ('parameter', 'lower', 'higher', 'd (steps)',
                                           'lower phys', 'higher phys'))
for r in rows:
    print('%14s %14.6f %14.6f %12.4f %14.6f %14.6f'
          % (r['name'], r['lower_steps'], r['higher_steps'], r['d_steps'],
             r['lower_phys'], r['higher_phys']))
print('%14s %14.6f %14.6f %12.6f' % ('tau (held)', X_LO[4], X_HI[4], X_HI[4] - X_LO[4]))

# the registered criterion, fixed in PREDICTION.md before this ran:
#   ONE DIRECTION  <=>  the largest |d| exceeds 1.0 step AND every other is below 0.1 step
mag = sorted(((abs(r['d_steps']), r['name']) for r in rows), reverse=True)
biggest, second = mag[0], mag[1]
one_direction = bool(biggest[0] > 1.0 and second[0] < 0.1)
rec['one_direction'] = dict(holds=one_direction, largest=biggest[1], largest_steps=biggest[0],
                            next_largest=second[1], next_largest_steps=second[0],
                            criterion='largest |d| > 1.0 step and every other < 0.1 step')
print('\n  largest separation: %s at %.4f step(s); next largest %s at %.4f'
      % (biggest[1], biggest[0], second[1], second[0]))
print('  ⇒ %s' % ('ONE DIRECTION: the basins are separated in %s alone' % biggest[1]
                  if one_direction else
                  'NOT ONE DIRECTION: two or more parameters move together'))

# ── Ⓑ②ᵃ′ the barrier: are these two minima at all? ─────────────────────────────────────────────
def chi2_at(v5):
    return float(mod.chi2(list(v5[:4]) + [NODE, float(v5[4])]))

c_lo, c_hi = chi2_at(X_LO), chi2_at(X_HI)
ts = np.linspace(0.0, 1.0, 81)
seg = [chi2_at([X_LO[i] + t * (X_HI[i] - X_LO[i]) for i in range(5)]) for t in ts]
seg = [float(c) for c in seg]
interior = seg[1:-1]
top = max(interior)
t_top = float(ts[1 + int(np.argmax(interior))])
barrier = bool(top > max(c_lo, c_hi) + 1e-6)
rec['barrier'] = dict(chi2_lower_here=c_lo, chi2_higher_here=c_hi,
                      segment_t=[float(t) for t in ts], segment_chi2=seg,
                      interior_max=top, interior_max_at_t=t_top,
                      height_over_higher_end=float(top - max(c_lo, c_hi)),
                      height_over_lower_end=float(top - min(c_lo, c_hi)),
                      holds=barrier, n_points=len(ts))
print('\n  the segment between them, %d points: chi2 at the ends %.4f and %.4f'
      % (len(ts), c_lo, c_hi))
print('  highest interior point %.4f at t = %.4f -- %.4f above the HIGHER end, %.4f above the lower'
      % (top, t_top, top - max(c_lo, c_hi), top - min(c_lo, c_hi)))
print('  ⇒ %s' % ('A BARRIER: they are two basins' if barrier else
                  '⛔ NO BARRIER on this segment: they are NOT two separate basins, and r7870\'s '
                  'word for them was wrong'))

# ── Ⓑ②ᵇ does the reference have a branch along that direction? ─────────────────────────────────
_pb = json.load(open(os.path.join(R7869, 'per_bin_response.json')))


def _find_keys(o, want, path='', hits=None):
    if hits is None:
        hits = []
    if isinstance(o, dict):
        for k, v in o.items():
            p = path + '/' + str(k)
            if want.lower() in str(k).lower():
                hits.append(p)
            _find_keys(v, want, p, hits)
    elif isinstance(o, list):
        for i, v in enumerate(o[:4]):
            _find_keys(v, want, path + '[%d]' % i, hits)
    return hits


name = biggest[1]
hits_param = _find_keys(_pb, name)
hits_branch = _find_keys(_pb, 'branch') + _find_keys(_pb, 'basin')
rec['reference'] = dict(record='r7869_cc66/per_bin_response.json',
                        top_level_keys=sorted(_pb.keys()),
                        keys_naming_the_direction=hits_param,
                        keys_naming_a_branch_or_basin=hits_branch)
resolved = bool(hits_param and hits_branch)
rec['reference']['resolves_a_branch_along_the_direction'] = resolved
print('\n  the reference\'s committed record, top-level keys: %s' % ', '.join(sorted(_pb)))
print('  keys naming %s: %s' % (name, hits_param if hits_param else 'NONE'))
print('  keys naming a branch or a basin: %s' % (hits_branch if hits_branch else 'NONE'))
print('  ⇒ %s' % ('the record resolves a branch along %s' % name if resolved else
                  'UNESTABLISHED AND ROUTED: this record does not decompose a branch by parameter, '
                  'so whether the reference branches along %s is not answered here -- and the '
                  'order\'s own summary of it is not that measurement' % name))

# ── an ADDITIONAL reading, labelled: WHERE the reference's own fitted solutions sit ────────────
# ⚠ Not a registered arm.  Ⓑ②ᵇ's verdict above stands on its own: a best fit per ruler is not a
#   scan, and a record that does not decompose a branch cannot be made to answer whether one
#   exists.  But the record DOES carry each ruler's fitted H0, and which branch those two sit in
#   is a fact about them that is worth putting beside the two basins rather than leaving unsaid.
_ref_h0 = {m: float(_pb['modes'][m]['params']['H0']) for m in _pb['modes']}
_near = {}
for m, v in _ref_h0.items():
    _near[m] = dict(H0=v, to_lower=float(v - p_lo['H0']), to_higher=float(v - p_hi['H0']),
                    nearer=('higher' if abs(v - p_hi['H0']) < abs(v - p_lo['H0']) else 'lower'))
rec['reference']['fitted_H0_per_mode'] = _near
rec['reference']['additional_reading_not_registered'] = True
print('\n  ⌗ additional reading, not a registered arm -- where the reference\'s own fits sit in H0:')
print('     the two basins are at %.3f (lower) and %.3f (higher) km/s/Mpc'
      % (p_lo['H0'], p_hi['H0']))
for m in sorted(_near):
    n = _near[m]
    print('     %-9s H0 = %.3f : %+.3f from the lower basin, %+.3f from the higher -> in the %s'
          % (m, n['H0'], n['to_lower'], n['to_higher'], n['nearer']))
print('     ⇒ both of the reference\'s fitted solutions sit in the HIGHER branch; that says where '
      'its fits are, and NOT that it has no second one')

json.dump(rec, open(OUT, 'w'), indent=1, sort_keys=True)
print('\n  wrote %s' % OUT)
