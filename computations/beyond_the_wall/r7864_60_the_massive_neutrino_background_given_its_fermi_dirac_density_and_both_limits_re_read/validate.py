# -*- coding: utf-8 -*-
"""Ⓐ① THE REGISTERED ARMS of the massive-neutrino background, measured.

⛭ `r7863` (69) item ①.  Each leg is one of the arms `PREDICTION.md` fixed before any of this ran,
and the two it is expected to FAIL are run and reported as failures rather than quietly rebanded.

    python3 validate.py
"""
import io
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BTW))
PROBE = os.path.join(BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_the_damping_'
                          'tails_share_of_the_gap', '_drag_probe.py')
sys.path.insert(0, HERE)
import nu_fd as N                                                           # noqa: E402

#: the reference's own figures at the control cosmology, READ at r7862 and carried as a read
REF_RDRAG = {0.00: 146.89300, 0.06: 147.05547, 0.30: 147.59023, 0.60: 148.07882}
TOL_REF_RD = 5.0e-03            # ⛭ registered
TOL_REF_H = 2.0e-03             # ⛭ registered
TOL_REF_RHO = 5.0e-03           # ⛭ registered
TOL_LIMITS = (1.0e-04, 1.0e-03)  # ⛭ registered: early limit, late limit
RULER_SPREAD_MIN = 5.0e-03      # ⛭ registered
FLAT_TOL = 1.0e-12              # ⛭ registered


def inst(env_extra, want):
    """read named module-level values out of one import of the instrument, in its own process"""
    code = ('import importlib.util, json, sys\n'
            'spec = importlib.util.spec_from_file_location("inst", %r)\n'
            'm = importlib.util.module_from_spec(spec)\n'
            'spec.loader.exec_module(m)\n'
            'out = {}\n'
            'for k in %r:\n'
            '    v = getattr(m, k)\n'
            '    out[k] = (float(v) if not callable(v) else None)\n'
            'out["Hleaf"] = [float(m.Hleaf(a)) for a in (1.0, 0.5, 1.0/1101.0, 1e-4)]\n'
            'out["Hphys"] = [float(m.Hphys(a)) for a in (1.0, 0.5, 1.0/1101.0, 1e-4)]\n'
            'out["Onu"] = [float(m.Onu_of(a)) for a in (1.0, 1e-2, 1e-5, 1e-8)]\n'
            'out["rt_head"] = [float(x) for x in m._rt[:3]]\n'
            'out["rt_tail"] = [float(x) for x in m._rt[-3:]]\n'
            'sys.stderr.write("__JSON__" + json.dumps(out))\n'
            % (os.path.join(BTW, 'ACOUSTIC_two_arm.py'), list(want)))
    env = dict(os.environ)
    env.update(ARM='lcdm', LMAXL='2')
    env.update(env_extra)
    r = subprocess.run([sys.executable, '-c', code], env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    txt = r.stderr.decode()
    if '__JSON__' not in txt:
        raise RuntimeError(txt[-2500:])
    return json.loads(txt.split('__JSON__', 1)[1])


WANT = ('R_S', 'OM', 'OL', 'OR', 'FNU', 'ONU_EARLY', 'ONU_FD', 'A_REC', 'H0', 'eta_rec', 'D_M')


def drag(env_extra):
    """the drag epoch and r_d through r7862's own probe, which reads whatever background is live"""
    import tempfile
    env = dict(os.environ)
    env.update(ARM='lcdm', LMAXL='2')
    env.update(env_extra)
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    env['OUTJSON'] = path
    try:
        r = subprocess.run([sys.executable, PROBE], env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        if not os.path.getsize(path):
            raise RuntimeError(r.stderr.decode()[-2000:])
        return json.load(io.open(path, encoding='utf-8'))
    finally:
        os.unlink(path)


def camb_at(sum_ev):
    import camb
    h = 0.674
    onu = sum_ev / 93.14 / h ** 2
    p = camb.set_params(H0=67.40, ombh2=0.0224,
                        omch2=(0.3150 - 0.0224 / h ** 2 - onu) * h ** 2,
                        mnu=sum_ev, tau=0.054, ns=0.965, As=2.1e-9)
    b = camb.get_background(p)
    d = b.get_derived_params()
    return dict(rdrag=float(d['rdrag']), zdrag=float(d['zdrag']),
                H=[float(b.hubble_parameter(z)) for z in (0.0, 1.0, 1100.0)],
                omnuh2=float(p.omnuh2), Omega_nu=float(p.omnuh2) / h ** 2)


def main():
    print(__doc__)
    print('=' * 104)
    out = {}

    # ── Ⓐ①ᵃ / Ⓐ①ᵃᵃ the two inertness claims, which are two different claims ────────────────────
    print('\n  Ⓐ①ᵃ AND Ⓐ①ᵃᵃ THE TWO INERTNESS CLAIMS')
    print('  ' + '-' * 104)
    off = inst({}, WANT)
    on0 = inst(dict(NUFD='1', MNU='0.0'), WANT)
    keys = ['R_S', 'Hleaf', 'Hphys', 'Onu', 'rt_head', 'rt_tail']
    same = {k: (off[k] == on0[k]) for k in keys}
    out['inert'] = dict(off=off, on_zero=on0, identical=same,
                        holds=bool(all(same.values())))
    for k in keys:
        print('    %-9s %s' % (k, 'bit-identical' if same[k] else '⛔ DIFFERS'))
    print('    ⇒ the switch is inert off and inert ON AT ZERO SUM: %s' % out['inert']['holds'])

    # ── Ⓐ①ᵉ the one-count bookkeeping, and the registered flatness band ────────────────────────
    print('\n  Ⓐ①ᵉ THE BOOKKEEPING -- is the species counted ONCE?')
    print('  ' + '-' * 104)
    rows = []
    for s in (0.0, 0.06, 0.30, 0.60):
        d = inst(dict(NUFD='1', MNU=repr(s)), WANT)
        tot_on = (d['OM'] - d['ONU_EARLY']) + d['OL'] + (1 - d['FNU']) * d['OR'] + d['Onu'][0]
        tot_off = off['OM'] + off['OL'] + off['OR']
        rows.append(dict(sum=s, total_on=tot_on, total_off=tot_off, diff=tot_on - tot_off,
                         minus_fnu_or=-d['FNU'] * d['OR'], R_S=d['R_S'],
                         ONU=d['ONU_EARLY'], ONU_FD=d['ONU_FD']))
        print('    Sum %.2f eV  total(a=1) %.13f  landed %.13f  diff %+.6e  (-FNU*OR %+.6e)'
              % (s, tot_on, tot_off, rows[-1]['diff'], rows[-1]['minus_fnu_or']))
    one_count = all(abs(r['diff'] - r['minus_fnu_or']) < FLAT_TOL for r in rows)
    flat_as_registered = all(abs(r['total_on'] - 1.0) < FLAT_TOL for r in rows)
    out['bookkeeping'] = dict(rows=rows, one_count=bool(one_count),
                              flatness_as_registered=bool(flat_as_registered), tol=FLAT_TOL)
    print('    ⇒ the difference from the landed total is EXACTLY -FNU*OR at every sum, to %.0e: %s'
          % (FLAT_TOL, one_count))
    print('    ⛔ and the REGISTERED band -- that the densities at a = 1 sum to 1 to %.0e -- is %s:'
          % (FLAT_TOL, 'HELD' if flat_as_registered else 'FAILED'))
    print('       the landed convention does NOT subtract the radiation from the vacuum term, so '
          'the total is 1 + Omega_r both before and after.')
    print('       *The claim that matters is the DIFFERENCE, and it is the one measured above.  The '
          'criterion is reported as written and not moved.*')

    # ── Ⓐ①ᵇ the two limits of the new term ─────────────────────────────────────────────────────
    print('\n  Ⓐ①ᵇ THE TWO LIMITS OF THE NEW TERM')
    print('  ' + '-' * 104)
    lim = {}
    for s in (0.06, 0.60):
        early = N.omega_factor(1e-8, s)
        late = N.omega_factor(1.0, s) / N.omega_factor(0.5, s) / 2.0
        lim[str(s)] = dict(early_factor=early, early_err=abs(early - 1.0),
                           late_ratio=late, late_err=abs(late - 1.0))
        print('    Sum %.2f eV  factor(a=1e-8) %.12f (err %.2e)   '
              'Omega_nu a^3 constancy between a=0.5 and 1: %.9f (err %.2e)'
              % (s, early, lim[str(s)]['early_err'], late, lim[str(s)]['late_err']))
    out['limits'] = dict(rows=lim, tol=list(TOL_LIMITS),
                         holds=bool(all(v['early_err'] < TOL_LIMITS[0]
                                        and v['late_err'] < TOL_LIMITS[1]
                                        for v in lim.values())))
    print('    ⇒ early limit inside %.0e and late limit inside %.0e: %s'
          % (TOL_LIMITS[0], TOL_LIMITS[1], out['limits']['holds']))

    # ── Ⓐ①ᶜ against the reference, before use ──────────────────────────────────────────────────
    print('\n  Ⓐ①ᶜ AGAINST THE REFERENCE AT THE CONTROL POINT')
    print('  ' + '-' * 104)
    ref, mine = {}, {}
    for s in (0.0, 0.06, 0.30, 0.60):
        ref[s] = camb_at(s)
        mine[s] = drag(dict(NUFD='1', MNU=repr(s)))
    rd_rows = []
    for s in (0.0, 0.06, 0.30, 0.60):
        rel = abs(mine[s]['r_drag'] / ref[s]['rdrag'] - 1.0)
        rd_rows.append(dict(sum=s, r_drag=mine[s]['r_drag'], rdrag_ref=ref[s]['rdrag'],
                            rdrag_read=REF_RDRAG[s], rel=rel, within=bool(rel < TOL_REF_RD)))
        print('    Sum %.2f eV   r_d %10.4f vs %10.4f   %.3e   %s'
              % (s, mine[s]['r_drag'], ref[s]['rdrag'], rel,
                 'within' if rd_rows[-1]['within'] else '⛔ OUTSIDE'))
    h_on = inst(dict(NUFD='1', MNU='0.06'), WANT)
    h_rel = [abs(h_on['Hleaf'][i] / ref[0.06]['H'][i] - 1.0) for i in range(3)]
    print('    H(z) at z = 0, 1, 1100 at Sum = 0.06 eV: %s against %s   rel %s'
          % (['%.4f' % v for v in h_on['Hleaf'][:3]],
             ['%.4f' % v for v in ref[0.06]['H']], ['%.2e' % v for v in h_rel]))
    rho_rel = abs(h_on['Onu'][0] / ref[0.06]['Omega_nu'] - 1.0)
    print('    rho_nu/rho_crit at a = 1, Sum = 0.06 eV: %.6e against %.6e   rel %.3e   %s'
          % (h_on['Onu'][0], ref[0.06]['Omega_nu'], rho_rel,
             'within' if rho_rel < TOL_REF_RHO else '⛔ OUTSIDE'))
    out['reference'] = dict(rdrag=rd_rows, H_rel=h_rel, H_within=bool(all(v < TOL_REF_H
                                                                         for v in h_rel)),
                            rho_rel=rho_rel, rho_within=bool(rho_rel < TOL_REF_RHO),
                            rdrag_within=bool(all(r['within'] for r in rd_rows)),
                            tol=dict(rdrag=TOL_REF_RD, H=TOL_REF_H, rho=TOL_REF_RHO))

    # ── the N_eff diagnosis, which this leg can refute ─────────────────────────────────────────
    print('\n  Ⓐ①ᶜᵃ THE DIAGNOSIS FOR THAT GAP, PUT TO A TEST THAT COULD REFUTE IT')
    print('  ' + '-' * 104)
    dn = inst(dict(NUFD='1', MNU='0.06', DNEFF='0.0293'), WANT)
    dn_rel = abs(dn['Onu'][0] / ref[0.06]['Omega_nu'] - 1.0)
    print('    at DNEFF = +0.0293 the density is %.6e against the reference\'s %.6e   rel %.3e'
          % (dn['Onu'][0], ref[0.06]['Omega_nu'], dn_rel))
    out['neff'] = dict(rho=dn['Onu'][0], ref=ref[0.06]['Omega_nu'], rel=dn_rel,
                       rel_without=rho_rel,
                       diagnosis_holds=bool(dn_rel < rho_rel / 3.0))
    print('    ⇒ the gap goes from %.3e to %.3e: the diagnosis %s'
          % (rho_rel, dn_rel, 'HOLDS' if out['neff']['diagnosis_holds'] else '** IS REFUTED **'))

    # ── Ⓐ①ᵈ the ruler moves with the sum now ───────────────────────────────────────────────────
    print('\n  Ⓐ①ᵈ THE RULER ACROSS THE SUM -- it was EXACTLY FLAT at r7862')
    print('  ' + '-' * 104)
    rds = [mine[s]['r_drag'] for s in (0.0, 0.06, 0.30, 0.60)]
    spread = max(rds) / min(rds) - 1.0
    for s, v in zip((0.0, 0.06, 0.30, 0.60), rds):
        print('    Sum %.2f eV   r_d %10.5f Mpc' % (s, v))
    out['ruler'] = dict(sums=[0.0, 0.06, 0.30, 0.60], r_drag=rds, spread=spread,
                        min_spread=RULER_SPREAD_MIN, holds=bool(spread >= RULER_SPREAD_MIN))
    print('    ⇒ spread %.4f per cent against the %.1f per cent registered and r7862\'s exactly '
          'zero: %s' % (100 * spread, 100 * RULER_SPREAD_MIN,
                        'HOLDS' if out['ruler']['holds'] else '** FAILS **'))

    # ── the two implementations, measured against each other ───────────────────────────────────
    print('\n  Ⓐ①ᶠ THE TWO IMPLEMENTATIONS -- the instrument\'s inline factor against this '
          'revision\'s independent module')
    print('  ' + '-' * 104)
    worst = 0.0
    for s in (0.06, 0.60):
        d = inst(dict(NUFD='1', MNU=repr(s)), WANT)
        for i, a in enumerate((1.0, 1e-2, 1e-5, 1e-8)):
            want = d['FNU'] * d['OR'] / a ** 4 * N.omega_factor(a, s)
            worst = max(worst, abs(d['Onu'][i] / want - 1.0))
    out['two_impls'] = dict(worst_rel=worst, holds=bool(worst < 1.0e-06))
    print('    worst relative difference over eight points: %.3e  ⇒ %s'
          % (worst, 'they agree' if out['two_impls']['holds'] else '⛔ THEY DO NOT'))

    with io.open(os.path.join(HERE, 'validate.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))
    print('')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
