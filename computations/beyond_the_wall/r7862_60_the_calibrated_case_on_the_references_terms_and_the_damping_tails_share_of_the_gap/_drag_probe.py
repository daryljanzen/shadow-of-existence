# -*- coding: utf-8 -*-
"""ONE drag-epoch probe, run as its own process so the instrument's switches are the process's.

⛭ *The instrument fixes its cosmology AT IMPORT from the environment, so a ruler that moves with the
cosmology cannot be had from one import.  This file is the inner worker: it imports the instrument
once at the switches it is given, derives the drag epoch from the instrument's OWN ionisation
history and accumulates the sound horizon to it on the clock `rs_from` is on, and writes the answer
as JSON to `$OUTJSON`.*

⌗ *Nothing here edits the instrument.  `taup_of`, `Rb_of`, `a_of_eta`, `RB_REC`, `A_REC`, `Hleaf`,
`Hgeom` and `R_S` are read from it as it stands, which is why this revision does not move its blob.*
"""
import importlib.util
import io
import json
import os

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)


def main():
    spec = importlib.util.spec_from_file_location(
        'inst', os.path.join(BTW, 'ACOUSTIC_two_arm.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    # ── the drag optical depth, on the instrument's own dtau/deta and its own R(eta) ────────────
    #   tau_d(eta) = INT_eta^eta_end (dtau/deta')/R(eta') deta'.  *R is the baryon-to-photon
    #   momentum ratio: the drag depth is the Compton depth WEIGHTED DOWN by it, which is why the
    #   drag epoch falls LATER than last scattering and r_d exceeds r_s.*
    e_end = float(m._ea[-1])
    e_lo = float(m._ea[0])

    def taud(e):
        return quad(lambda x: float(m.taup_of(x)) / float(m.Rb_of(x)),
                    e, e_end, limit=400)[0]

    # ⌗ the root is BRACKETED and the bracket is reported, so a run whose history never reaches
    #   unity fails loudly instead of returning an endpoint.
    t_lo, t_hi = taud(e_lo), taud(e_end * (1 - 1e-12))
    bracketed = bool((t_lo - 1.0) * (t_hi - 1.0) < 0.0)
    out = dict(switches=dict((k, os.environ.get(k)) for k in
                             ('ARM', 'LH0', 'LOM', 'WBH2', 'MNU', 'LMAXL', 'LEAFREC',
                              'LEAFSCALES', 'LEAFGEOM')),
               H0=float(m.H0), OM=float(m.OM), OMBH2=float(m.OMBH2), MNU=float(m.MNU),
               omega_m=float(m.OM) * (float(m.H0) / 100.0) ** 2,
               omega_b=float(m.OMBH2),
               A_REC=float(m.A_REC), Z_REC=float(m.Z_REC), R_S=float(m.R_S),
               RB_REC=float(m.RB_REC),
               taud_at_eta_rec=float(taud(float(m.eta_rec))),
               taud_bracket=[float(t_lo), float(t_hi)], bracketed=bracketed)
    if not bracketed:
        out['error'] = 'the drag depth does not cross unity inside the ionisation grid'
        with io.open(os.environ['OUTJSON'], 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(out, indent=1, sort_keys=True))
        return 1

    e_d = brentq(lambda e: taud(e) - 1.0, e_lo, e_end * (1 - 1e-12), xtol=1e-9, rtol=1e-12)
    a_d = float(m.a_of_eta(e_d))

    # ── the ruler: the sound horizon accumulated to the DRAG epoch, on the clock `rs_from` is on ──
    #   *`rs_from` integrates the same integrand to `A_REC`; the only change is the upper limit, and
    #   the clock is taken from the instrument's own `LEAFSCALES` branch rather than chosen here, so
    #   a run on the leaf clock and a run on the stacking clock each get their own ruler.*
    H = m.Hleaf if m.LEAFSCALES else m.Hgeom

    def _rs_to(a_hi):
        return quad(lambda a: m.C / (a ** 2 * H(a) * np.sqrt(3 * (1 + m.RB_REC * a / m.A_REC))),
                    0.0, a_hi, limit=400)[0]

    out.update(eta_drag=float(e_d), a_drag=a_d, z_drag=1.0 / a_d - 1.0,
               r_drag=float(_rs_to(a_d)),
               # ⌗ the SAME integral stopped at recombination, so the one number this instrument
               #   already reports is reproduced by this file's own quadrature rather than trusted:
               #   a ruler that could not reproduce `R_S` is not measuring what `R_S` measures.
               r_rec_reproduced=float(_rs_to(float(m.A_REC))),
               clock=('leaf' if m.LEAFSCALES else ('leaf' if m.LEAFGEOM else 'stack')))
    out['r_rec_error'] = abs(out['r_rec_reproduced'] / out['R_S'] - 1.0)
    with io.open(os.environ['OUTJSON'], 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
