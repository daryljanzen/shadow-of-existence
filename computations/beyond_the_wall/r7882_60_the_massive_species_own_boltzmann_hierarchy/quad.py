#!/usr/bin/env python3
"""r7882+60 gate Ⓠ⓵ — THE QUADRATURE AGAINST THE BACKGROUND ALREADY BUILT.

`PREDICTION.md` registered this as the FIRST gate and as the cheap one: the `q`-grid the hierarchy
will be binned on must reproduce the instrument's own `NUF_of` and `NUW_of` -- its `rho_nu(a)/rho_nu0`
and `w_nu(a)` -- to `1e-04` relative, at every decade of `a` from `1e-10` to `1`.

⌗ *A grid that cannot reproduce the background the species is described by is not integrating that
  species, and nothing it says about a perturbation would mean anything.  This runs before any
  spectrum, and it decides `n_q` and `q_max` by the registered criterion rather than by what the
  validation would like them to be.*

⌗ NOT RETYPED.  The weight, the energy and pressure integrands, the momentum variable and the two
  splines are the INSTRUMENT's own: this script executes its prelude and reads them out, exactly as
  `r7876`'s `closure.py` and `r7880`'s `clock.py` do.

    NODE=60 python3 quad.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(_HERE)
SRC = os.path.join(BW, 'ACOUSTIC_two_arm.py')
_CUT = 645                                   # the `D_M = eta_0 - eta_rec` line, as r7876 pinned it
LC = dict(LH0='67.40', LOM='0.3150', WBH2='0.0224', NS='0.965')   # the control's environment
TOL = 1e-04                                  # PREDICTION.md, gate Ⓠ⓵
CANDIDATES = [(n, qm) for qm in (15.0, 20.0, 25.0, 30.0) for n in (8, 12, 16, 24, 32, 48, 64)]


def prelude(mnu):
    with io.open(SRC, encoding='utf-8') as fh:
        head = ''.join(fh.readlines()[:_CUT])
    keep = dict(os.environ)
    os.environ.update(LC)
    os.environ.update(ARM='lcdm', MNU=str(mnu), NUFD='1', BVEL='1', HIER='1')
    ns = {'__name__': '_prelude', '__file__': SRC}
    try:
        sys.path.insert(0, BW)
        exec(compile(head, SRC, 'exec'), ns)
    finally:
        sys.path.pop(0)
        os.environ.clear()
        os.environ.update(keep)
    return ns


def grid(n, qmax):
    """Gauss-Legendre nodes and weights on [0, qmax] -- deterministic, and its own convergence
    in `n` is what the gate reads.  ⌗ *No node is placed by hand and none is tuned.*"""
    x, w = np.polynomial.legendre.leggauss(int(n))
    return 0.5 * qmax * (x + 1.0), 0.5 * qmax * w


def main():
    print(__doc__)
    print('=' * 100)
    #: the instrument's own weight and its two splines, read out of its prelude at a NON-ZERO sum
    ns = prelude(0.30)
    f0, NUF, NUW, FD0 = ns['_fd_w'], ns['NUF_of'], ns['NUW_of'], ns['_FD0']
    T0, mnu = ns['_T_NU0_EV'], ns['MNU']
    las = np.log(np.array([10.0 ** k for k in range(-10, 1)]))     # every decade of `a`
    ys = (mnu / 3.0) * np.exp(las) / T0
    print('  the instrument\'s own weight and splines, read from its prelude at Sigma = 0.30 eV')
    print('  %d decade(s) of a, y from %.4g to %.4g' % (len(ys), ys.min(), ys.max()))

    rec = {'tol': TOL, 'decades': int(len(ys)), 'candidates': {}}
    best = None
    for n, qmax in CANDIDATES:
        q, w = grid(n, qmax)
        fw = f0(q) * w
        er, ew = [], []
        for la, y in zip(las, ys):
            rho = float((q ** 2 * np.sqrt(q ** 2 + y ** 2) * fw).sum())
            pre = float((q ** 4 / np.sqrt(q ** 2 + y ** 2) * fw).sum()) / 3.0
            er.append(abs(rho / FD0 - float(NUF(la))) / max(abs(float(NUF(la))), 1e-300))
            ew.append(abs(pre / rho - float(NUW(la))) / max(abs(float(NUW(la))), 1e-300))
        row = {'n': int(n), 'qmax': float(qmax), 'worst_rho': max(er), 'worst_w': max(ew)}
        row['passes'] = bool(row['worst_rho'] < TOL and row['worst_w'] < TOL)
        rec['candidates']['%d@%g' % (n, qmax)] = row
        if row['passes'] and (best is None or (n, qmax) < (best['n'], best['qmax'])):
            best = row
    print('\n  %6s %7s %14s %14s %8s' % ('n_q', 'q_max', 'worst |d rho|', 'worst |d w|', 'passes'))
    for k in sorted(rec['candidates'], key=lambda s: (rec['candidates'][s]['qmax'],
                                                      rec['candidates'][s]['n'])):
        r = rec['candidates'][k]
        print('  %6d %7g %14.3e %14.3e %8s'
              % (r['n'], r['qmax'], r['worst_rho'], r['worst_w'], 'YES' if r['passes'] else 'no'))

    #: ⛔⛭⛭ ** A THIRD WEIGHT THE REGISTERED GATE DOES NOT COVER, NAMED AND MEASURED HERE. **
    #:   *`PREDICTION.md` fixed gate Ⓚ⓵ as "reproduce `NUF_of` and `NUW_of`", and those two carry the
    #:   `q^2 eps` weight of the density and the `q^4/eps` weight of the pressure -- which is also
    #:   the shear's.  The perturbation needs a THIRD: the energy flux integrates `Psi_1` against
    #:   `q^3 f0`, and no spline of the background carries it, so the registered gate is silent on
    #:   it.*  ⇒ It is checked by SELF-CONVERGENCE against a far finer grid of the same rule, at
    #:   the same `1e-04`, and reported as an ADDITION to the gate rather than as part of it --
    #:   because a criterion met by a weight nobody checked is not met.
    _qf, _wf = grid(96, 40.0)
    _ref = float((_qf ** 3 * f0(_qf) * _wf).sum())
    rec['third_weight'] = {}
    for n, qmax in CANDIDATES:
        q, w = grid(n, qmax)
        got = float((q ** 3 * f0(q) * w).sum())
        rec['third_weight']['%d@%g' % (n, qmax)] = abs(got - _ref) / _ref
    _k = '%d@%g' % (best['n'], best['qmax']) if best else None
    rec['third_weight_at_chosen'] = rec['third_weight'].get(_k)
    rec['third_weight_passes'] = bool(_k and rec['third_weight'][_k] < TOL)
    print('\n  THE THIRD WEIGHT the registered gate is silent on -- the energy flux\'s `q^3 f0`,')
    print('  checked by self-convergence against a 96-node grid on [0, 40] of the same rule:')
    for k in sorted(rec['third_weight'], key=lambda s: (float(s.split('@')[1]),
                                                        int(s.split('@')[0]))):
        print('    %-9s %.3e%s' % (k, rec['third_weight'][k], '   <- the chosen grid'
                                   if k == _k else ''))
    print('  ⇒ at the chosen grid it is %.3e against the same %g: %s'
          % (rec['third_weight_at_chosen'] or float('nan'), TOL,
             'MET' if rec['third_weight_passes'] else '** NOT MET **'))

    rec['chosen'] = best
    print('\n  ⇒ %s' % ('GATE Ⓠ⓵ MET by n_q = %d on [0, %g]: worst %.3e in rho and %.3e in w, '
                        'against the registered %g'
                        % (best['n'], best['qmax'], best['worst_rho'], best['worst_w'], TOL)
                        if best else
                        '** GATE Ⓠ⓵ NOT MET by any candidate -- the hierarchy is not built on this '
                        'quadrature, and that is the finding **'))
    #: ⛔ *the choice is the SMALLEST grid that meets the registered criterion, taken in the
    #:   order the candidate list was written, so it is not the grid that flatters a later number.*
    json.dump(rec, io.open(os.path.join(_HERE, 'quad.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote quad.json')
    return 0 if best else 1


if __name__ == '__main__':
    sys.exit(main())
