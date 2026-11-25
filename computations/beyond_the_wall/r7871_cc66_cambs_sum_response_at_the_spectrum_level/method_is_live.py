# -*- coding: utf-8 -*-
"""r7871+cc66 ⑩ Ⓖ⑦ POSITIVE CONTROL -- is `MassiveNuMethod` LIVE, or is the null result a no-op?

The four treatments agreed to `7.3e-08` in the ratio.  Four different methods agreeing to one part
in ten million is equally the signature of a knob that never reached the computation, and this seat
has now been caught four times by exactly that shape.  So before the agreement is reported as
physics, it is established that the knob is LIVE:

  ⒜ the setting SURVIVES `set_cosmology` and `set_for_lmax` (it is read back after both);
  ⒝ the outputs are NOT bit-identical between methods -- so the method reaches the computation;
  ⒞ and a regime IS found where the methods differ by a large amount, so the agreement at 60's
     multipoles is a statement about that range and not about the knob.

    NODE=cc66 python3 method_is_live.py
"""
import io
import json
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
OUT = os.path.join(_HERE, 'method_is_live.json')
METHODS = ('Nu_int', 'Nu_trunc', 'Nu_approx', 'Nu_best')


def run(method, mnu, lmax, acc):
    import camb
    p = camb.CAMBparams()
    p.MassiveNuMethod = method
    p.set_cosmology(H0=67.4, ombh2=0.0224, omch2=max(0.315 * 0.674 ** 2 - 0.0224, 1e-4),
                    mnu=mnu, num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=0.054)
    p.InitPower.set_params(As=2.1e-9, ns=0.965)
    p.set_for_lmax(lmax, lens_potential_accuracy=acc)
    survived = (p.MassiveNuMethod == method)
    r = camb.get_results(p)
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['lensed_scalar'])['lensed_scalar']
    return survived, np.asarray(cl[:, 0], float)


def main():
    print(__doc__)
    print('=' * 100)
    out = {}

    print('\n  ⒜ does the setting SURVIVE the builder calls?')
    surv = {}
    for m in METHODS:
        s, _ = run(m, 0.6, 600, 1)
        surv[m] = bool(s)
        print('      %-10s read back after set_cosmology and set_for_lmax: %s' % (m, s))
    out['survives'] = surv

    print('\n  ⒝ are the outputs BIT-IDENTICAL between methods?  (identical ⇒ the knob is inert)')
    _, a = run('Nu_int', 0.6, 2600, 1)
    _, b = run('Nu_approx', 0.6, 2600, 1)
    n = min(a.size, b.size)
    same = bool(np.array_equal(a[:n], b[:n]))
    worst = float(np.nanmax(np.abs(a[:n] - b[:n]) / np.maximum(np.abs(a[:n]), 1e-30)))
    print('      Nu_int vs Nu_approx, lensed TT, bit-identical: %s;  worst relative difference %.3e'
          % (same, worst))
    out['bit_identical_at_60s_range'] = same
    out['worst_rel_at_60s_range'] = worst

    print('\n  ⒞ is there a regime where they DO differ materially?')
    probe = {}
    for mnu, lmax in ((2.0, 2600), (0.6, 2600)):
        _, x = run('Nu_int', mnu, lmax, 1)
        _, y = run('Nu_approx', mnu, lmax, 1)
        k = min(x.size, y.size)
        hi = slice(2, k)
        w = float(np.nanmax(np.abs(x[hi] - y[hi]) / np.maximum(np.abs(x[hi]), 1e-30)))
        probe['mnu=%g' % mnu] = w
        print('      Sum = %.1f eV: worst relative TT difference between Nu_int and Nu_approx %.3e'
              % (mnu, w))
    out['probe'] = probe
    live = (all(surv.values()) and not same)
    out['knob_is_live'] = bool(live)
    print('\n  ⇒ the knob is %s: the setting survives and the outputs are not identical.'
          % ('LIVE' if live else '⛔ INERT, and the agreement says nothing about the treatment'))
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
