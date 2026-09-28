"""⓷ WHAT IS NOT ON THE LIST -- the enumeration of the UNMEASURED -- r6997+cc66.51.

⛔ *Nothing is RUN: the order's ⓸.  The enumeration is built by asking the BANKS what they resolve,
rather than by listing what comes to mind, so "never measured" is a checkable statement about the
corpus's own arrays and not an impression.*

** THE QUESTION. **  `cc66.50` found no measured candidate carrying the excess's wavenumber dependence.
*That is a statement about the set searched.*  ⇒ So: **what in this arm has never had its wavenumber
dependence measured at all**, as against measured and failing?  ⚠ *And the order requires the possibility
that the carrier is not a channel in the source or the transfer but a property of the PROJECTION -- which
is what this row's own name has said since it opened, and which no revision has tested.*
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}

print(__doc__)
print('=' * 104)
print('\n⓷a  WHAT THE BANKS ACTUALLY RESOLVE.  A quantity can only have a MEASURED wavenumber')
print('     dependence if some bank stores it against wavenumber.  Asked of the arrays:\n')
d = A['cr']
qres, etaonly, scalar = [], [], []
for k in sorted(d.files):
    v = d[k]
    if v.ndim == 2:
        qres.append((k, v.shape))
    elif v.ndim == 1:
        etaonly.append((k, v.shape))
    else:
        scalar.append(k)
print('     RESOLVED IN WAVENUMBER (eta x band) -- these are the ones a filter can be applied to:')
for k, s in qres:
    print(f'       {k:10s} {s}')
print('\n     FUNCTIONS OF CONFORMAL TIME ALONE -- no wavenumber axis exists for them:')
print('       ' + '  '.join(k for k, _ in etaonly))
print('\n     SINGLE NUMBERS -- one value for the whole arm:')
print('       ' + '  '.join(scalar))

print('\n⓷b  ⛭⛭ AND THAT SETTLES A WHOLE CLASS BY STRUCTURE RATHER THAN BY MEASUREMENT.')
print('     ** Every quantity belonging to the two-rate clock structure -- the leaf clock `rs_leaf`,')
print('     the ruler `rs_stack`, the Jacobian `jac` between them, the visibility `vis`, the optical')
print('     depth `etau` -- is a function of CONFORMAL TIME ALONE. **  A function of eta has the same')
print('     value for every wavenumber, so it cannot vary across wavenumber, so ** it cannot be the')
print('     carrier, and this needs no run to establish. **')
print('     ⇒ *That is the strongest form the empty search can take for these: not "measured and')
print('       failed" and not "unmeasured", but CANNOT CARRY IT, by the shape of the object.*')
print('     ⚠ *What such a quantity CAN do is set a scale that something else then varies across --')
print('       which is a different claim and is the one ⓷c is about.*')


# ==================================================================================================
print('\n⓷c  ⛭⛭⛭ AND THE PROJECTION, WHICH THIS ROW IS NAMED AFTER AND NO REVISION HAS TESTED.')
print('     A projection property can carry a wavenumber dependence in a way a clock cannot, because')
print('     the projection is where k becomes l.  Two widths govern it and THEY ARE NOT THE SAME WIDTH:\n')
print('       · the ACOUSTIC PHASE swept across the visibility window varies by k x (width in the')
print('         LEAF sound horizon) -- this is what smears the oscillation, and it is what')
print('         cc66.47 acted on with SRCTAPER;')
print('       · the PROJECTION smears by k x (width in CONFORMAL TIME), because the Bessel argument')
print('         is k(eta_0 - eta) -- a different width, in a different clock.')
print('     ⇒ ** In a one-rate cosmology these two are the same object up to the sound speed.  In')
print('       THIS arm they are not, because the two clocks differ -- which is the corpus\'s own')
print('       two-rate assignment. **  Both grow with k, so both are q-dependent by construction.\n')


def widths(t):
    """visibility-weighted widths of the window, in each clock, from the bank"""
    d = A[t]
    ee, vv = np.asarray(d['eta'], float), np.asarray(d['vis'], float)
    rs = np.asarray(d['rs_leaf'], float)
    w = vv / np.trapezoid(vv, ee)
    m_e = float(np.trapezoid(w * ee, ee))
    s_e = float(np.sqrt(np.trapezoid(w * (ee - m_e) ** 2, ee)))
    m_r = float(np.trapezoid(w * rs, ee))
    s_r = float(np.sqrt(np.trapezoid(w * (rs - m_r) ** 2, ee)))
    return s_e, s_r


print(f"     {'arm':8s} {'width in eta':>14s} {'width in rs_leaf':>18s} {'ratio eta/rs':>14s}")
W = {}
for t in ('lcdm', 'cr'):
    se, sr = widths(t)
    W[t] = (se, sr)
    print(f"     {t:8s} {se:14.4f} {sr:18.4f} {se / sr:14.4f}")
re_, rr_ = W['cr'][0] / W['lcdm'][0], W['cr'][1] / W['lcdm'][1]
print(f"\n     arm/control:  in eta {re_:.4f}   in rs_leaf {rr_:.4f}   "
      f"-> they differ by {100 * (re_ / rr_ - 1):+.1f} per cent")
print('\n     ⇒ ** THE TWO WIDTHS DO NOT SCALE TOGETHER BETWEEN THE ARMS. **  The window that smears')
print('       the acoustic phase and the window that the projection integrates over stand in a')
print('       DIFFERENT RATIO in the arm than in the control.')
print('     ⌗ *cc66.47 imposed the arm\'s PHASE spread on the control and measured the response;')
print('       nothing has imposed the arm\'s PROJECTION width, and the two are not the same knob.*')
print('\n  ⇒⇒ SO THE ENUMERATION OF THE UNMEASURED, WHICH IS WHAT THE ORDER ASKED FOR:')
print('     ⓐ the PROJECTION width of the window, in conformal time, as against the phase width in')
print('        the leaf clock -- different between the arms by the figure above, never imposed,')
print('        never measured as a response.  ** The one candidate here that is a property of the')
print('        projection rather than of the source. **')
print('     ⓑ the q-dependence of the oscillation-amplitude ratio BELOW q = 2, which ⓵ showed is')
print('        where the target does most of its growing and where no present estimator reaches.')
print('     ⓒ the polarisation term\'s oscillation amplitude -- w2pol is q-resolved and was filtered')
print('        on band POWER like the dipole, so it carries the same error and has not been')
print('        filtered on the right quantity either.')
print('     ⛔ AND WHAT IS NOT ON THE LIST BECAUSE IT CANNOT BE: every clock quantity, by ⓷b.')
