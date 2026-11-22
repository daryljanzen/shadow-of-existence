#!/usr/bin/env python3
"""** Ⓔ⑤/Ⓕ⑥/Ⓖ⑦/Ⓗ⑧/Ⓘ⑨ banked as ONE record, so the receipt pins readings and not recomputations.

Three control runs, each with its treatment named:

  landed, minimised     the configuration on `main`, the ruler minimised as this harness does
  repaired, minimised   the same with `BVEL=1`, nothing else moved
  repaired, calibrated  and with `r_d` held at the reference pipeline's own drag-epoch horizon at
                        the control's cosmology, which is legitimate because the control IS that
                        pipeline's model -- and would not be for the arm of record

⌗ Ⓖ⑦'s figures come from the instrument's own spectrum run both ways; Ⓗ⑧ is checked by reading the
filesystem rather than asserted; Ⓘ⑨ collects the timings each file recorded with its switches.

Run: python3 summary.py          (writes summary.json)
"""
import io
import json
import os
import re
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7850 = os.path.join(_BTW, 'r7850_60_phi_carried_through_the_radiation_era')
ROOT = os.path.dirname(_BTW)
sys.path.insert(0, R7846)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import lensing_like as LL                                                    # noqa: E402

RDFIX = 147.055454          # the reference's own drag-epoch horizon at the control's cosmology
SPEC = {0: '/tmp/claude-0/spec2_bvel0.log', 1: '/tmp/claude-0/spec2_bvel1.log'}


def j(p):
    return json.load(io.open(p, encoding='utf-8'))


def score(path):
    d = j(path)
    b = np.array(d['bandpowers'], float)
    a = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
    r = LL.DATA - a * b
    c2 = float(r @ LL.FISHER @ r)
    return dict(chi2=c2, per_dof=c2 / 8.0, amplitude=a, etaref=d['etaref'])


def read_run(path, tag, ruler):
    d = j(path)
    b, u, p = d['lcdm_bounded'], d['lcdm_unbounded'], d['lcdm_proposal']
    return dict(which=tag, ruler=ruler,
                upper95_mev=b['upper95_mev'], upper95_mcse_mev=b['upper95_mcse_mev'],
                effective_mass_mev=1000.0 * u['sum_mean_ev'],
                effective_mass_sd_mev=1000.0 * u['sum_sd_ev'],
                chi2min=b['best_fit']['chi2'],
                worst_rhat=max(v['rhat'] for v in b['diagnostics'].values()),
                least_ess=min(v['ess'] for v in b['diagnostics'].values()),
                accept=b['accept'], minimum_on_a_bound=p['minimum_on_a_bound'],
                curvature_unmeasurable_in=p['curvature_unmeasurable_in'],
                per_chain_span_mev=(max(b['upper95_per_chain_mev'])
                                    - min(b['upper95_per_chain_mev'])),
                frac_below_59=b['frac_below_0.059'], frac_below_64=b['frac_below_0.064'])


def peaks(path):
    t = io.open(path, encoding='utf-8', errors='replace').read()
    pk = re.findall(r'peaks at l = \[([0-9, ]+)\]', t)
    rat = re.findall(r'l_1/l_A = ([0-9.]+)\s+P1/P2 = ([0-9.]+)\s+P1/P3 = ([0-9.]+)', t)
    return dict(peaks=[int(v) for v in pk[-1].split(',')] if pk else None,
                l1_over_lA=float(rat[-1][0]) if rat else None,
                P1_over_P2=float(rat[-1][1]) if rat else None,
                P1_over_P3=float(rat[-1][2]) if rat else None)


def main():
    out = {}
    print('\n  Ⓔ⑤ THE NINE BANDPOWERS, one amplitude fitted')
    bp = dict(landed=score(os.path.join(R7850, 'grid_ics_eta4000', 'lcdm_S000.json')),
              repaired=score(os.path.join(_HERE, 'grid_ics_eta4000_bvel1', 'lcdm_S000.json')))
    bp['camb_exactly_binned_per_dof'] = 1.066836
    for k in ('landed', 'repaired'):
        print('      %-10s chi^2 %9.4f   %.6f per dof   amplitude %.6e'
              % (k, bp[k]['chi2'], bp[k]['per_dof'], bp[k]['amplitude']))
    print('      %-10s                %.6f per dof' % ('reference', bp['camb_exactly_binned_per_dof']))
    out['bandpowers'] = bp

    print('\n  Ⓔ⑤/Ⓕ⑥ THE CONTROL, three runs, each treatment named')
    runs = [read_run(os.path.join(R7850, 'sampler6_lcdm_ics.json'), 'landed', 'minimised'),
            read_run(os.path.join(_HERE, 'sampler6_bvel1.json'), 'repaired', 'minimised'),
            read_run(os.path.join(_HERE, 'sampler6_bvel1_rdfix.json'), 'repaired',
                     'calibrated at r_d = %.6f Mpc' % RDFIX)]
    print('      which     ruler        limit (meV)        effective (meV)     joint chi^2min')
    for r in runs:
        print('      %-9s %-12s %9.4f +/- %.4f  %+9.3f +/- %6.3f  %10.4f'
              % (r['which'], r['ruler'].split()[0], r['upper95_mev'], r['upper95_mcse_mev'],
                 r['effective_mass_mev'], r['effective_mass_sd_mev'], r['chi2min']))
    out['control_runs'] = runs
    out['rdfix_mpc'] = RDFIX
    d_ruler = runs[2]['upper95_mev'] - runs[1]['upper95_mev']
    frac = abs(d_ruler) / runs[1]['upper95_mev']
    out['ruler_shift_mev'] = d_ruler
    out['ruler_shift_fraction'] = frac
    out['ruler_expectation_holds'] = bool(d_ruler < 0 and frac >= 0.10)
    print('    ⇒ the ruler moves the limit by %+.4f meV, %.4f of it -- registered as a TIGHTENING '
          'of at least a tenth, so the expectation %s'
          % (d_ruler, frac, 'HOLDS' if out['ruler_expectation_holds'] else 'FAILS'))

    print('\n  Ⓖ⑦ THE SIZE OF THE RECALIBRATION, before and after, from the spectrum run both ways')
    pk = {('bvel%d' % b): peaks(SPEC[b]) for b in (0, 1)}
    for k, v in sorted(pk.items()):
        print('      %-7s peaks %s   l_1/l_A %.4f   P1/P2 %.3f   P1/P3 %.3f'
              % (k, v['peaks'], v['l1_over_lA'], v['P1_over_P2'], v['P1_over_P3']))
    same = pk['bvel0'] == pk['bvel1']
    out['calibration'] = pk
    out['calibration_identical'] = bool(same)
    print('    ** THE RECALIBRATION IS %s **'
          % ('ZERO: every figure identical to its last printed digit' if same
             else 'NOT zero, and the figures above are the size of it'))

    print('\n  Ⓗ⑧ NOTHING DOWNSTREAM MOVED, read off the tree and not asserted')
    rng = subprocess.run(['git', 'diff', '--name-only', 'origin/main...HEAD'],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    p15 = [f for f in rng if f.startswith('corpus/P15') or f == 'corpus/CR_cosmology.tex']
    other_grids = [f for f in rng if 'grid_' in f and 'bvel1' not in f]
    out['downstream'] = dict(files_changed=len(rng), p15_sources_touched=p15,
                             other_grids_touched=other_grids,
                             p15_untouched=not p15, no_other_grid=not other_grids)
    print('      %d file(s) in this revision\'s range; P15 sources touched: %s; '
          'other grids touched: %s' % (len(rng), p15 or 'none', other_grids or 'none'))

    print('\n  Ⓘ⑨ THE TIMINGS, each with its own switches')
    timings = {}
    for f in ('locate.json', 'repair.json'):
        p = os.path.join(_HERE, f)
        if os.path.exists(p):
            d = j(p)
            if 'timings' in d:
                timings[f] = d['timings']
            elif 'solve_seconds' in d:
                timings[f] = dict(solve=dict(seconds=d['solve_seconds'],
                                             etas=len(d.get('etas', [])),
                                             modes=len(d.get('k', []))))
    out['timings'] = timings
    n = sum(len(v) for v in timings.values())
    print('      %d timing record(s) over %d file(s), each carrying its configuration'
          % (n, len(timings)))

    with io.open(os.path.join(_HERE, 'summary.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote summary.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
