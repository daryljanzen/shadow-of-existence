# -*- coding: utf-8 -*-
"""Ⓑ② BOTH LIMITS ON THE SEPARATING GRID — the repair ON, no `N_eff` offset at all — AND READ BOTH
WAYS, because the way the profile is read is now part of what is under test.

Order `r7869` item ②. The order ruled this grid to decide which of two things carries the unreadable
minimised profile: the repaired background, or the `N_eff` ruling. **Since then this revision has
measured that the unreadability is the PROFILER mixing two basins** — the lower basin reaches five
nodes and the dip at the top node was the basin switch — so the fork may have no slot for its
answer. The grid is read anyway, for the two reasons that do not depend on the fork: it was ordered,
and it completes the four-rung decomposition.

⛭ ** SO THIS FILE READS THE MINIMISED LIMIT TWICE, AND THE COMPARISON BETWEEN THE TWO READINGS IS
THE POINT. **
  ⓵ **RAW** — the original profiler's own reading, a warm-start chain from one node to the next, the
    way `r7866` and item ① read their banks. *This is the reading the order's fork is about.*
  ⓶ **ENVELOPE** — every node also started from cold starts and from each basin's own solution, so
    no node can sit in a higher basin than its neighbour.
⇒ *** If the raw reading dips here too and the envelope does not, then basin mixing is GENERAL to
this score and not a property of any one bank — and the fork's two branches are both wrong about
what they were alternatives for. If the raw reading does NOT dip here, the mixing is particular to
the banks that carry an offset, and the fork's question survives. Both outcomes are stated here
before the run. ***

⚠ ** WHAT IS NOT CLAIMED. **  The envelope is a LOWER ENVELOPE of what has been found, not a proved
global minimum, exactly as in `one_basin.py`. A third basin deeper still would move it and nothing
here rules one out. *So no crossing read on an envelope is reported as a limit anywhere in this
revision.*

    NODE=60 python3 limits_separating.py
"""
import io
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7864 = os.path.join(_BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_'
                           'density_and_both_limits_re_read')
sys.path.insert(0, R7864)
import limits as L7864                                                      # noqa: E402

#: both keys, set BEFORE `model6` is imported anywhere -- it reads the lensing key at import time
NEWBANK = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')
NEWPP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_only')
OTHERPP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')
os.environ['POL_DIR'] = NEWBANK
os.environ['PPGRID'] = NEWPP

DCHI2 = 2.71
SUMS = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
REF_RULER, REF_CALIB = 54.00, 30.56

#: ⌗ THE FOUR RUNGS the order names, with each figure's PROVENANCE beside it rather than inlined as
#:   a bare number.  `None` for a minimised limit means NOT READABLE as that revision's profiler
#:   read it -- an absence, carried as an absence.
RUNGS = [
    ('the landed bank: no repair, no offset', 'r7864', 69.97, 81.94),
    ('repair ON, no offset  (THIS GRID)', 'r7870 item ②', 'measured below', 'measured below'),
    ('repair ON, offset +0.0293', 'r7866', None, 185.69),
    ('repair ON, offset +0.044', 'r7870 item ①', None, 185.92),
]


def precondition():
    """Ⓑ②ᵃ -- read off every point's own recorded config, not off the directory name"""
    pol = sorted(f for f in os.listdir(NEWBANK)
                 if f.endswith('.npz') and not f.endswith('_tt.npz'))
    cfgs = {}
    for f in pol:
        z = np.load(os.path.join(NEWBANK, f), allow_pickle=True)
        cfgs[f[:-4]] = json.loads(str(np.atleast_1d(z['config'])[0]))
    lc = {k: v for k, v in cfgs.items() if v.get('ARM') == 'lcdm'}
    cr = {k: v for k, v in cfgs.items() if v.get('ARM') == 'cr'}
    #: ⛔ THE WHOLE POINT OF THIS RUNG: no offset on EITHER arm.  A single point carrying one would
    #:   make this bank a different object from the one the order ruled.
    no_offset = all(v.get('DNEFF') is None for v in cfgs.values())
    nonzero_on = all(v.get('NUFD') is True for v in cfgs.values()
                     if float(v.get('MNU') or 0) != 0)
    zero_off = all(v.get('NUFD') is False for v in cfgs.values()
                   if float(v.get('MNU') or 0) == 0)
    pp_lc = [f for f in os.listdir(NEWPP) if f.endswith('.json') and f.startswith('lcdm_')]
    pp_cr = [f for f in os.listdir(NEWPP) if f.endswith('.json') and f.startswith('cr_')]
    ok = dict(cmb_points=len(pol), lcdm_points=len(lc), cr_points=len(cr),
              lensing_points_lcdm=len(pp_lc), lensing_points_cr=len(pp_cr),
              dneff_key_present=all('DNEFF' in v for v in cfgs.values()),
              no_offset_on_either_arm=bool(no_offset),
              nufd_true_at_every_nonzero_sum=bool(nonzero_on),
              nufd_false_at_zero_sum=bool(zero_off),
              nothing_carried='both arms are solved on this rung',
              blob=cfgs['lcdm_S000'].get('instrument_blob'))
    ok['holds'] = bool(len(pol) == 32 and len(lc) == 16 and len(cr) == 16
                       and len(pp_lc) == 16 and len(pp_cr) == 16
                       and ok['dneff_key_present'] and no_offset and nonzero_on and zero_off)
    return ok


def _starts(seed, n_x):
    rng = np.random.default_rng(seed)
    out = [[0.0, 0.0, 0.0, 0.0, t] for t in (0.030, 0.040, 0.054, 0.075, 0.100, 0.140)]
    for _ in range(n_x):
        for t in (0.054, 0.100):
            out.append(list(rng.normal(0.0, 1.0, 4)) + [t])
    return out


def _fit(mod, s, starts):
    def f(v):
        return float(mod.chi2(list(v[:4]) + [s, float(v[4])]))
    best, bestx = np.inf, None
    for x0 in starts:
        r = minimize(f, x0, method='Nelder-Mead',
                     options=dict(xatol=1e-8, fatol=1e-8, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    if bestx is not None:
        r = minimize(f, bestx, method='Nelder-Mead',
                     options=dict(xatol=1e-9, fatol=1e-9, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    return best, bestx


def _read(ss, tot):
    tot = np.asarray(tot, float)
    i0 = int(np.argmin(tot))
    d = tot - tot[i0]
    dips = [(float(ss[k]), float(tot[k] - tot[k - 1]))
            for k in range(i0 + 1, len(ss)) if tot[k] < tot[k - 1] - 1e-6]
    above = [k for k in range(i0 + 1, len(ss)) if d[k] >= DCHI2]
    lim = None
    if above:
        k = above[0]
        lim = float(ss[k - 1] + (DCHI2 - d[k - 1]) * (ss[k] - ss[k - 1])
                    / (d[k] - d[k - 1])) * 1000.0
    return dict(sums=[float(v) for v in ss], totals=[float(v) for v in tot],
                delta=[float(v) for v in d], min_at=float(ss[i0]),
                dips=[list(x) for x in dips], monotonic_above_min=not dips,
                crossing_meV=lim, limit_meV=(None if dips else lim))


def profile(mod, label, seeds=None, warm_only=False):
    ss = [s for s in SUMS if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
    tot, prev = [], None
    print('\n  %s' % label)
    print('  ' + '-' * 104)
    for s in ss:
        if warm_only:
            st = [[0.0, 0.0, 0.0, 0.0, t] for t in (0.040, 0.054, 0.075, 0.100)]
            if prev is not None:
                st.insert(0, list(prev))
        else:
            st = _starts(7870, 6)
            if prev is not None:
                st.insert(0, list(prev))
            for sd in (seeds or []):
                st.insert(0, list(sd))
        b, bx = _fit(mod, s, st)
        tot.append(b)
        prev = bx
        print('    Sum = %.3f eV   total chi2 %12.4f' % (s, b))
    out = _read(ss, tot)
    print('    minimum at Sum = %.3f eV;  dips above it: %s'
          % (out['min_at'], ', '.join('%.3f eV' % x[0] for x in out['dips'])
             if out['dips'] else 'NONE'))
    print('    the %.2f crossing: %s meV%s'
          % (DCHI2, ('%.2f' % out['crossing_meV']) if out['crossing_meV'] else 'not reached',
             '' if not out['dips'] else '   ⛔ the profile DIPS, so no limit is reported'))
    return out


def main():
    print(__doc__)
    print('=' * 104)
    out = {}

    print('\n  Ⓑ②ᵃ THE PRECONDITION -- is this bank the rung the order named?')
    print('  ' + '-' * 104)
    pre = precondition()
    print('    %d CMB point(s): %d control, %d arm of record;  lensing: %d control, %d arm'
          % (pre['cmb_points'], pre['lcdm_points'], pre['cr_points'],
             pre['lensing_points_lcdm'], pre['lensing_points_cr']))
    print('    the offset key is present everywhere and reads NONE on EITHER arm: %s'
          % pre['no_offset_on_either_arm'])
    print('    the repair reads TRUE at every nonzero sum: %s, FALSE at the zero-sum node: %s'
          % (pre['nufd_true_at_every_nonzero_sum'], pre['nufd_false_at_zero_sum']))
    print('    nothing is carried on this rung: %s' % pre['nothing_carried'])
    out['precondition'] = pre
    if not pre['holds']:
        print('\n  ⛔ the precondition FAILS -- no limit is reported.\n')
        _save(out)
        return 1

    import model3 as M3                                                     # noqa: E402
    import distances as DI                                                  # noqa: E402
    import model6 as M6                                                     # noqa: E402

    print('\n  THE PLUMBING, MEASURED IN THIS RUN')
    print('  ' + '-' * 104)
    def _base(grid, tag='S030', arm='lcdm'):
        p = os.path.join(grid, '%s_%s.json' % (arm, tag))
        return np.asarray(json.load(io.open(p, encoding='utf-8'))['bandpowers'], float)
    rel = float(np.max(np.abs(_base(NEWPP) / _base(OTHERPP) - 1.0)))
    print('    the CMB grid in use     : %s' % os.path.basename(os.environ['POL_DIR']))
    print('    the lensing grid in use : %s' % os.path.basename(M6.GRID))
    print('    it IS this rung\'s grid  : %s'
          % (os.path.basename(M6.GRID) == os.path.basename(NEWPP)))
    print('    and its bandpowers differ from the offset rung\'s by up to %.3e at Sum = 0.30' % rel)
    out['plumbing'] = dict(pol_dir=os.path.basename(os.environ['POL_DIR']),
                           pp_grid=os.path.basename(M6.GRID),
                           pp_grid_is_this_rungs=bool(os.path.basename(M6.GRID)
                                                      == os.path.basename(NEWPP)),
                           max_rel_change_vs_offset_rung=rel)

    def _mod():
        m = M6.Model6('lcdm')
        raw = m.amp_cmb
        m.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        return m

    r_inst = L7864.Ruler(os.path.join(R7864, 'rd_grid_nufd.npz'), 'r_drag',
                         "this instrument's own drag epoch ON THE REPAIRED BACKGROUND",
                         'instrument')

    #: ⓵ the RAW reading -- the profiler's own warm-start chain, the reading the fork is about
    out['raw_minimised'] = profile(
        _mod(), 'Ⓑ②ᵇ⓵ THE RULER MINIMISED, RAW -- the warm-start chain, as r7866 and item ① read '
                'their banks', warm_only=True)
    modc = _mod()
    L7864.attach(modc, r_inst, M3, DI)
    out['raw_calibrated'] = profile(
        modc, 'Ⓑ②ᶜ⓵ CALIBRATED, RAW', warm_only=True)

    #: ⓶ the ENVELOPE -- seeded from both known basins so no node can sit in the higher one
    seeds = []
    try:
        ob = json.load(io.open(os.path.join(_HERE, 'one_basin.json'), encoding='utf-8'))
        seeds = [ob['seeds']['lower'], ob['seeds']['higher']]
        print('\n  ⌗ the envelope is seeded from the two basins this revision already found')
    except Exception as exc:                                                # noqa: BLE001
        print('\n  ⌗ no stored basin seeds (%s) -- the envelope uses cold starts only' % exc)
    out['env_minimised'] = profile(
        _mod(), 'Ⓑ②ᵇ⓶ THE RULER MINIMISED, ENVELOPE -- cold starts, the node below, and every '
                'known basin', seeds=seeds)
    modc2 = _mod()
    L7864.attach(modc2, r_inst, M3, DI)
    out['env_calibrated'] = profile(modc2, 'Ⓑ②ᶜ⓶ CALIBRATED, ENVELOPE', seeds=seeds)

    rawm, envm = out['raw_minimised'], out['env_minimised']
    print('\n  Ⓑ②ᵇ THE FORK, AND WHAT THE TWO READINGS SAY ABOUT IT')
    print('  ' + '-' * 104)
    raw_dips, env_dips = bool(rawm['dips']), bool(envm['dips'])
    print('    RAW      : %s%s'
          % ('DIPS at ' + ', '.join('%.3f eV' % d[0] for d in rawm['dips']) if raw_dips
             else 'monotonic, limit %.2f meV' % rawm['limit_meV'],
             '' if not raw_dips else '  ⇒ no limit reported'))
    print('    ENVELOPE : %s'
          % ('DIPS at ' + ', '.join('%.3f eV' % d[0] for d in envm['dips']) if env_dips
             else 'monotonic, crossing %.2f meV (an ENVELOPE, not a limit)'
                  % envm['crossing_meV']))
    if raw_dips and not env_dips:
        verdict = ('** BASIN MIXING IS GENERAL TO THIS SCORE, NOT A PROPERTY OF ANY ONE BANK. **  '
                   'The raw reading dips on a bank with NO offset at all, and the envelope on the '
                   'same bank does not.  ⇒ *** The order\'s fork named the repaired background and '
                   'the N_eff ruling as the alternatives; the unreadability is NEITHER, so the '
                   'thing they were alternatives FOR does not exist.  The repaired background is '
                   'ruled out here on its own rung, exactly as item ① ruled out the ruling. ***')
    elif raw_dips and env_dips:
        verdict = ('** THE RAW READING DIPS AND SO DOES THE ENVELOPE. **  Basin mixing does not '
                   'account for this rung, so something else is carrying it here and it is NOT '
                   'named by this file -- reported as unseparated on this rung, with the earlier '
                   'rungs\' basin result standing on its own')
    elif not raw_dips:
        verdict = ('** THE RAW READING IS MONOTONIC ON THIS RUNG. **  So the mixing is NOT general: '
                   'it appears on the banks that carry an offset and not on the one that carries '
                   'none.  ⇒ the fork\'s question SURVIVES, and this rung is the branch that reads')
    else:
        verdict = 'NOT SEPARATED -- reported as unseparated rather than named'
    print('\n    %s' % verdict)
    out['fork'] = dict(raw_dips=raw_dips, envelope_dips=env_dips,
                       raw_limit_meV=rawm['limit_meV'],
                       envelope_crossing_meV=envm['crossing_meV'],
                       envelope_is_not_a_limit=True, verdict=verdict)

    print('\n  Ⓑ②ᵈ THE FOUR RUNGS, each figure with the revision that measured it')
    print('  ' + '-' * 104)
    rows = []
    for name, prov, mini, cal in RUNGS:
        if mini == 'measured below':
            mini = rawm['limit_meV']
            cal = out['raw_calibrated']['limit_meV']
        rows.append(dict(rung=name, provenance=prov, minimised_meV=mini, calibrated_meV=cal))
        print('    %-38s %-14s  minimised %-14s calibrated %s'
              % (name, prov,
                 ('%.2f' % mini) if isinstance(mini, float) else 'NOT READABLE',
                 ('%.2f' % cal) if isinstance(cal, float) else 'NOT READABLE'))
    print('    ⌗ every minimised entry reading NOT READABLE is the RAW reading of that rung, which '
          'is the only reading the earlier revisions took.  ⇒ *On this revision\'s envelope '
          'reading, the ones it could re-read are not unreadable at all -- which is the finding, '
          'and it is why the column is labelled by its READING and not left to look like a '
          'property of the bank.*')
    out['rungs'] = rows
    out['reference'] = dict(minimised=REF_RULER, calibrated=REF_CALIB)
    _save(out)
    print('')
    return 0


def _save(out):
    with io.open(os.path.join(_HERE, 'limits_separating.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    sys.exit(main())
