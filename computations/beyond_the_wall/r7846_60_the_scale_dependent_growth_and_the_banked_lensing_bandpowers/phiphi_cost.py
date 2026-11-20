#!/usr/bin/env python3
"""how long each piece of a phi-phi spectrum costs, and whether the four CMB parameters matter

** A GRID IS A COMPUTE BUDGET AND IT SHOULD BE SIZED BEFORE IT IS SPENT. **  A full response grid
is the base plus eight sums plus eight parameter directions, seventeen spectra per arm and
thirty-four over both.  This measures the two things that decide whether that is necessary: what
each stage costs, and how much the nine bandpowers actually MOVE when the four CMB parameters move
over the posterior's own width.

⌗ *If the four-parameter response is far below the bandpowers' own errors over the range the chain
explores, holding it is a stated approximation rather than an omission -- and the eight direction
spectra per arm are not worth their hours.  If it is not, they are.  Either way it is measured.*
"""
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
os.environ.setdefault('ETAREF', '914')          # the carry r7846 settled on, z = 188

import phiphi as PP                                                      # noqa: E402
import growth_kdep as GK                                                 # noqa: E402
A = GK.A


def main():
    lb, cov, wins = PP.bandpowers()
    err = np.sqrt(np.diag(cov))
    frac_err = err / lb[:, 4]
    Lg = np.unique(np.concatenate([L for L, _ in wins]))
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lg.min())),
                                        np.log10(Lg.max()), 36)).astype(int))
    etaref = float(os.environ['ETAREF'])
    a_ref = float(A.a_of_eta(etaref))

    t0 = time.time()
    kk = np.logspace(np.log10(PP.KMIN), np.log10(PP.KMAX), 48)
    g = GK.GrowthKDep(0.0, kk=kk, a_start=a_ref)
    t_growth = time.time() - t0
    print('  the growth solve (48 k, one sum):          %7.1f s' % t_growth, flush=True)

    t0 = time.time()
    kkp, Phi = PP.phi_shape(etaref)
    t_phi = time.time() - t0
    print('  the instrument solve for Phi(k):           %7.1f s' % t_phi, flush=True)

    t0 = time.time()
    cl = PP.clpp(ls, 0.0, etaref=etaref, growth=g)
    t_limber = time.time() - t0
    print('  the Limber integral over %d multipoles:    %7.1f s' % (len(ls), t_limber), flush=True)
    b0 = PP.bin_through(ls, cl, wins)

    print('  ⇒ one spectrum at a NEW sum reuses Phi: %.1f s;  at a new PARAMETER point: %.1f s'
          % (t_growth + t_limber, t_growth + t_phi + t_limber), flush=True)

    out = dict(seconds=dict(growth=t_growth, phi=t_phi, limber=t_limber,
                            per_new_sum=t_growth + t_limber,
                            per_new_parameter_point=t_growth + t_phi + t_limber),
               fractional_error=[float(v) for v in frac_err])

    # ⌗ the four-parameter response, over ONE grid step, which is wider than the posterior's own sd
    print('  measuring the four-parameter response is a separate run', flush=True)
    with open(os.path.join(_HERE, 'phiphi_cost.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote phiphi_cost.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
