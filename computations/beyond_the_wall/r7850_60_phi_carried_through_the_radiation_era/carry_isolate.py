"""** Ⓐ① FAILED. THIS ISOLATES THE CAUSE INSTEAD OF GUESSING IT, WHICH IS WHAT r7848's Ⓐ① DID. **

`phi_carry.py` reports a residual spread of `0.63`, `0.49` and `0.32` at handovers `eta = 500`,
`914` and `1400` against a registered criterion of `0.023` -- and `r7848`'s matter-only carry, the
thing this revision replaces, scored `0.2276`.  ** So on that test the repair is WORSE than what it
replaces, and the trend runs the wrong way: the LATER the handover, the better it does. **  A result
like that is either a finding against the order's design or a defect in the test, and the way to
tell is to measure which.

Two candidate causes, both named before they are measured, and both reachable:

  ⒜ ** THE TEST'S OWN IDENTITY MAY NOT RANGE OVER THE WHOLE BAND. **  `phi_carry` compares
     `Phi(a2)/Phi(a1)` against `[d_cb(a2)/a2]/[d_cb(a1)/a1]`, which is the Poisson relation.
     Poisson is a SUB-HORIZON statement.  At `k = 2e-4` and `eta = 500` the mode has `k eta = 0.1`,
     so it is OUTSIDE the horizon and `Phi` there is not `-(3/2)(H0^2 Om/a) d_cb/k^2` at all --
     super-horizon `Phi` is nearly constant while `d_cb` grows.  *That would be a category error in
     the test, exactly the one `r7848`'s first growth attempt made by comparing two formulas in a
     regime where neither was valid.*

  ⒝ ** THE BARYONS MAY NOT HAVE CAUGHT UP AT THE HANDOVER. **  `d_cb` is one fluid here, and at
     `z = 482` the baryons have only recently left the photons.  If `d_b` is still far below `d_c`
     at high `k`, then what follows is `d_b` catching up, and a single-fluid `d_cb` equation does
     not describe that.  *That would be a real deficiency of the carry and not of the test.*

So this file measures three things and lets them decide:

  ① the Poisson relation's own accuracy per `k`, with its ONE constant fitted on the modes where it
     must hold and then held fixed -- which establishes WHAT THE IDENTITY RANGES OVER rather than
     assuming it ranges over everything;
  ② `d_b / d_c` per `k` at each handover, which is ⒝ measured directly;
  ③ Ⓐ①'s residual re-read on the modes where ① holds, reported as a RESTRICTED READING and never
     as the registered arm passing.  ** Ⓐ① is reported FAILED with its criterion exactly as
     written, whatever ③ says. **

Run: python3 carry_isolate.py          (writes carry_isolate.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import phi_carry as PC                                                     # noqa: E402
A = PC.A

POISSON_OK = float(os.environ.get('POISSON_OK', '0.01'))   # the identity holds to this, per k


def one(eta_h):
    c = PC.PhiCarry(eta_h)
    a_h, a_j = c.a_of[c.i_h], c.a_of[c.i_j]
    kk = c.kk

    # ① the Poisson relation, with ONE constant fitted where it must hold and then held
    # Phi = -C * d_cb / (a k^2); the constant is the same at both times and for every k
    def resid(i_t, a_t):
        pred = -c.d_cb[i_t] / (a_t * kk ** 2)
        C = float(np.median((c.phi[i_t] / pred)[kk >= 0.3]))
        return C, np.abs(c.phi[i_t] / (C * pred) - 1.0)

    C_h, r_h = resid(c.i_h, a_h)
    C_j, r_j = resid(c.i_j, a_j)
    ok = (r_h <= POISSON_OK) & (r_j <= POISSON_OK)
    k_eta_h = kk * c.eta_h

    # ② the baryons against the cold matter, read off the SAME solve rather than a second one
    dc = c.dc[c.i_h]
    db = c.db[c.i_h]
    ratio_bc = db / dc

    # ③ the restricted reading
    chk = c.check()
    rel = np.asarray(chk['rel'], float)
    out = dict(eta_h=float(eta_h), z_h=chk['z_h'],
               radiation_over_matter=chk['radiation_over_matter_at_handover'],
               poisson=dict(constant_at_handover=C_h, constant_at_judge=C_j,
                            threshold=POISSON_OK,
                            n_ok=int(ok.sum()), n_total=int(len(kk)),
                            k_min_ok=float(kk[ok].min()) if ok.any() else None,
                            k_eta_min_ok=float(k_eta_h[ok].min()) if ok.any() else None,
                            worst_at_low_k=float(r_h[0]), worst_at_high_k=float(r_h[-1]),
                            resid_handover=[float(v) for v in r_h],
                            resid_judge=[float(v) for v in r_j]),
               baryons=dict(ratio_db_over_dc=[float(v) for v in ratio_bc],
                            at_k_min=float(ratio_bc[0]), at_k_max=float(ratio_bc[-1]),
                            worst_shortfall=float(np.min(ratio_bc))),
               full_band=dict(spread=chk['spread'], worst_abs=chk['worst_abs'],
                              holds=chk['holds']),
               restricted=dict(
                   n=int(ok.sum()),
                   spread=float(rel[ok].max() - rel[ok].min()) if ok.sum() > 1 else None,
                   worst_abs=float(np.max(np.abs(rel[ok]))) if ok.any() else None,
                   is_not_the_registered_arm=True),
               k=[float(v) for v in kk], k_eta_at_handover=[float(v) for v in k_eta_h],
               rel=[float(v) for v in rel])
    return out


def main():
    print('\n  Ⓐ① failed; this isolates the cause rather than guessing it\n')
    rows = []
    for eh in PC.HANDOVERS:
        r = one(eh)
        rows.append(r)
        p, b = r['poisson'], r['baryons']
        print('  handover eta = %-6g (z = %7.2f)' % (r['eta_h'], r['z_h']))
        print('     ① Poisson holds to %.0e on %d of %d modes; the lowest is k = %s (k*eta = %s)'
              % (p['threshold'], p['n_ok'], p['n_total'],
                 ('%.3e' % p['k_min_ok']) if p['k_min_ok'] else 'none',
                 ('%.2f' % p['k_eta_min_ok']) if p['k_eta_min_ok'] else 'none'))
        print('        its residual is %.3e at the lowest k and %.3e at the highest'
              % (p['worst_at_low_k'], p['worst_at_high_k']))
        print('     ② d_b/d_c runs %.4f at k = %.1e to %.4f at k = %.1e; worst shortfall %.4f'
              % (b['at_k_min'], r['k'][0], b['at_k_max'], r['k'][-1], b['worst_shortfall']))
        print('     ③ the residual spread is %.4e on the full band and %s on the %d modes where '
              '① holds'
              % (r['full_band']['spread'],
                 ('%.4e' % r['restricted']['spread']) if r['restricted']['spread'] is not None
                 else 'undefined', r['restricted']['n']), flush=True)
    best = min((r for r in rows if r['restricted']['spread'] is not None),
               key=lambda r: r['restricted']['spread'], default=None)
    out = dict(handovers=rows, poisson_threshold=POISSON_OK,
               criterion=PC.CRITERION, r7848_matter_only_spread=PC.R7848_SPREAD,
               best_restricted=(None if best is None else
                                dict(eta_h=best['eta_h'], spread=best['restricted']['spread'])),
               registered_arm_verdict='FAILED on the full band, with the criterion as registered')
    print('\n  ⇒ Ⓐ① is FAILED with its criterion exactly as registered, on the full band.')
    if best is not None:
        print('     The restricted reading, which is NOT the arm, gives %.4e at eta = %g.'
              % (best['restricted']['spread'], best['eta_h']))
    with io.open(os.path.join(_HERE, 'carry_isolate.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote carry_isolate.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
