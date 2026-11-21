#!/usr/bin/env python3
"""** Ⓖ⑦, ANSWERED BY MEASUREMENT RATHER THAN BY WAITING: camb 2.0.4 IS INSTALLED HERE. **

Order `r7847` ③ says to compare this instrument's response against `cc66`'s independent CAMB
decomposition *when it lands*, and the registered arm Ⓖ⑦ says that if it has not landed the receipt
SAYS so and infers nothing from the silence.  It has not landed -- there is no `cc66` revision above
`r7843` in the tree.

⌗ ** BUT `FOR_66.md` STATES, REPEATEDLY, THAT `camb 2.0.4` WILL NOT INSTALL IN THIS CONTAINER, AND
IT IS INSTALLED. **  Probed rather than taken on the page's word:

    camb.__version__ == '2.0.4'   at /usr/local/lib/python3.11/dist-packages/camb/__init__.py

and it runs: `get_lens_potential_cls` returns a lensing-potential spectrum at a standard cosmology.
** That is the THIRD consecutive revision on this line in which a stated absence turned out to be
false on probing ** -- `r7844` found the lensing bandpowers banked, `r7848` found ACT DR6 banked, and
this finds the reference pipeline installed.  ⇒ So the independent reference the order wants exists
here, and this file builds it instead of waiting for it.

** WHAT MAKES THIS THE STRONGEST TEST IN THE REVISION. **  Everything else here compares this
instrument against ITSELF -- its own `Phi` at two times, its own growth with two initial conditions.
CAMB is a different pipeline with a different solver, so it can answer the question those cannot:
when the nine bandpowers come out at `chi^2/dof` about `2` against this instrument, is that the
instrument's shape or the data's?

Three readings, each with its own amplitude treatment stated:

  ① CAMB's spectrum binned through the SAME nine windows, scored against the data with NOTHING
     fitted, at a stated `A_s`.  If CAMB lands near the data with no amplitude freedom, the
     absolute normalisation is reachable and this instrument's `0.91` ratio is this instrument's.
  ② the same with ONE amplitude fitted, which isolates SHAPE from normalisation.
  ③ CAMB against this instrument's own bandpowers, on both of this line's growths, which says
     whether the `-6` per cent the initial-condition repair moved them went toward CAMB or away.

⚠ `A_s` is a PARAMETER here and not a measurement: it is set to the value stated below and the
absolute reading ① means nothing without it.  The shape reading ② does not depend on it.

Run: python3 camb_reference.py          (writes camb_reference.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
sys.path.insert(0, R7846)
sys.path.insert(0, _HERE)
import lensing_like as LL                                                  # noqa: E402

import camb                                                               # noqa: E402

# the control's own cosmology, as gen_phiphi.sh sets it for the lcdm arm
H0 = 67.40
OM = 0.3150
WB = 0.0224
NS = 0.965
TAU = 0.054
AS = float(os.environ.get('AS', '2.1e-9'))     # ⚠ a PARAMETER, not a measurement
MNU = float(os.environ.get('MNU', '0.06'))
LMAX = 600


def camb_bandpowers(mnu, As=AS):
    """CAMB's lensing potential through the nine banked windows, in the data's own convention

    `get_lens_potential_cls` returns `[L(L+1)]^2 C_L^phiphi / (2 pi)`, which is the convention
    `r7471`'s own scoring code uses and which `r7848` read off it rather than assuming.
    """
    omch2 = (OM - WB / (H0 / 100.0) ** 2) * (H0 / 100.0) ** 2 - mnu / 93.14
    p = camb.set_params(H0=H0, ombh2=WB, omch2=omch2, mnu=mnu, tau=TAU, ns=NS, As=As,
                        lmax=LMAX, WantTransfer=True)
    r = camb.get_results(p)
    cl = r.get_lens_potential_cls(lmax=LMAX)[:, 0]          # index is L
    out = []
    for L, w in LL.WINDOWS:
        out.append(float(np.sum(w * cl[L])))
    return np.array(out), dict(H0=H0, ombh2=WB, omch2=omch2, mnu=mnu, tau=TAU, ns=NS, As=As,
                               lmax=LMAX, camb_version=camb.__version__)


def score(b, amplitude=None):
    a = (float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b)) if amplitude is None
         else float(amplitude))
    r = LL.DATA - a * b
    return float(r @ LL.FISHER @ r), a


def main():
    print('\n  Ⓖ⑦: the independent reference, built here because camb %s IS installed\n'
          % camb.__version__, flush=True)
    b, cfg = camb_bandpowers(MNU)
    err = np.sqrt(np.diag(LL.COV))
    print('  CAMB at the control\'s cosmology, A_s = %.3e (a PARAMETER, stated not measured):'
          % AS)
    print('    bin  L_av      data            CAMB            CAMB/data   in bin sigma')
    for i in range(LL.NBP):
        print('     %d   %6.1f   %.6e   %.6e   %8.4f   %+8.3f'
              % (i + 1, LL.L_AV[i], LL.DATA[i], b[i], b[i] / LL.DATA[i],
                 (b[i] - LL.DATA[i]) / err[i]))
    c2_free, a_free = score(b)
    c2_fixed, _ = score(b, amplitude=1.0)
    print('\n  ① nothing fitted:        chi^2 %12.4f on 9 bins  (%.4f per bin)'
          % (c2_fixed, c2_fixed / 9.0))
    print('  ② one amplitude fitted:  chi^2 %12.4f on 8 dof   (%.4f per dof), amplitude %.6f'
          % (c2_free, c2_free / 8.0, a_free))

    # ③ against this instrument, on both growths, at zero sum
    inst = {}
    for tag, path in (('r7848_quadrature_ics',
                       os.path.join('/tmp/claude-0/phiphi_grid_eta4000', 'lcdm_S000.json')),
                      ('r7850_instrument_ics',
                       os.path.join(_HERE, 'grid_ics_eta4000', 'lcdm_S000.json'))):
        if not os.path.exists(path):
            inst[tag] = None
            continue
        d = json.load(io.open(path, encoding='utf-8'))
        bb = np.array(d['bandpowers'], float)
        # the instrument's bandpowers are in ITS OWN arbitrary units, so only the SHAPE compares:
        # each is normalised by its own best fit to the data before being compared with CAMB's
        _, ai = score(bb)
        _, ac = score(b)
        inst[tag] = dict(shape_vs_camb=[float(v) for v in (ai * bb) / (ac * b) - 1.0],
                         chi2_free=score(bb)[0], amplitude=ai)
    out = dict(camb_version=camb.__version__, config=cfg, mnu=MNU,
               data=[float(v) for v in LL.DATA], camb=[float(v) for v in b],
               ratio_camb_over_data=[float(v) for v in (b / LL.DATA)],
               in_bin_sigma=[float(v) for v in ((b - LL.DATA) / err)],
               chi2_nothing_fitted=c2_fixed, chi2_one_amplitude=c2_free,
               fitted_amplitude=a_free,
               instrument=inst,
               as_is_a_parameter=True,
               decomposition_from_cc66_has_landed=False,
               note=('cc66 has no revision above r7843 in the tree, so the ordered decomposition '
                     'has not landed; this is built here instead because camb is present, and the '
                     'absence FOR_66 states is false in this container'))
    for tag, v in inst.items():
        if v is None:
            print('  ③ %s: not present' % tag)
            continue
        s = np.array(v['shape_vs_camb'], float)
        print('  ③ %-22s shape against CAMB after each is self-normalised: %+.4f to %+.4f, '
              'chi^2 %.4f' % (tag, s.min(), s.max(), v['chi2_free']))
    with io.open(os.path.join(_HERE, 'camb_reference.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote camb_reference.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
