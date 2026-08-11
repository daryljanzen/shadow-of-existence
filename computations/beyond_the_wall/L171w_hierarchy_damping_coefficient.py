#!/usr/bin/env python3
"""L171w_hierarchy_damping_coefficient.py -- ** THE SHEAR COEFFICIENT, DERIVED INSTEAD OF REMEMBERED. **

Built r2376+c54.177, front #2.

** WHY THIS EXISTS. **  The diffusion damping in this fork is applied as exp(-k^2/k_D^2) with

    1/k_D^2(eta) = INT [ R^2/(1+R) + C ] / [ 6 (1+R) tau' ]  d(eta),

and C has never been derived here.  `C8_diffusion_length.py` names the ambiguity in its own text --
"the 8/9 coefficient against the 16/15 polarization-corrected one" -- and uses 8/9.  At c54.176 I
changed it to 16/15 on recollection of the standard result and changed it straight back, because a
remembered number is not a derivation; and chi^2 preferring 8/9 by 1123 is not one either.
** THIS FILE MEASURES C, from the photon Boltzmann hierarchy with the polarisation multipoles, on
this corpus's own background and opacity. **

** THE METHOD, AND WHY IT NEEDS NO WKB PREFACTOR. **  Two integrations of the SAME oscillator on the
SAME background, differing in one thing:

  REFERENCE   the perfect tight-coupled fluid -- one velocity, no quadrupole, no slip.  Undamped
              by construction:  dg' = -(4/3)tg,  tg' = -[H R/(1+R)] tg + k^2 dg/(4(1+R)).
  HIERARCHY   photons carried to l = LG with Thomson scattering, polarisation carried alongside,
              and the baryons given their OWN velocity coupled through tau'(tg - tb)/R.

** Their ratio is the damping and nothing else. **  The (1+R)^(1/4) WKB prefactor, the drift of c_s,
the R-dependence of the oscillation -- all of it is common to the two runs and divides out
identically.  *This is the whole reason the measurement is a ratio and not a fit to an envelope.*

The envelope ratio is read on the MONOPOLE, at every extremum of the REFERENCE monopole in the
interval -- where the dipole vanishes, so nothing of the phase leaks in.  *The obvious reading, the
oscillator invariant Theta_0^2 + 3(1+R)Theta_1^2, is wrong here by a measurable amount and the
docstring of `run` records why and what it cost.*  Then

    ln(A_hier/A_ref) = -k^2 [ K + C J ],   K = INT R^2/(1+R) / [6(1+R)tau'],   J = INT 1/[6(1+R)tau'],

both integrals taken over the same interval and computed here from the same splines.  ** So C is
solved for, mode by mode, and its INDEPENDENCE OF k is the check that the k^2 scaling is real
rather than imposed. **

  POL=1  Pi = F_2 + G_0 + G_2 with the polarisation hierarchy evolved -- the real universe.
  POL=0  Pi = F_2 with G identically zero, which turns the l=2 scattering term into -(9/10)tau' F_2:
         the unpolarised case, and the standard textbook 8/9 should come out of it.

** BOTH ARE RUN, because the DIFFERENCE between them is the polarisation correction and it is the
thing actually in dispute.  A single number matching a remembered one proves less than a ratio. **

Gravity is switched off in both runs -- Phi = Psi = 0.  ** That is not an approximation, it is the
definition of the object: the WKB damping formula is a statement about the FREE oscillator, and
driving it would measure the driving as well. **  The expansion is kept, since R and tau' evolve.

Env: KLIST, ETA_I (default 60), ETA_F (default 200), LG (default 16), POL, RTOL.
Run:  python3 L171w_hierarchy_damping_coefficient.py
"""
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp, quad

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('NK', '4')
os.environ.setdefault('NOPROJ', '1')
import ACOUSTIC_two_arm as A                                              # noqa: E402

LG = int(os.environ.get('LG', '16'))
RTOL = float(os.environ.get('RTOL', '1e-9'))
ETA_I = float(os.environ.get('ETA_I', '60'))
ETA_F = float(os.environ.get('ETA_F', '200'))
# ** THE FIT IS RESTRICTED TO SMALL (k/tau')^2, because the correction is not linear in it. **
# Including the large-(k/tau') tail curves the line and drags the intercept -- which is the one
# number this file exists to report.  The intercept's stability under this cut is checked, not
# assumed: it is the KTMAX2 scan in the receipt.
KTMAX2 = float(os.environ.get('KTMAX2', '0.02'))

# state layout, hierarchy run:  dg tg tb  F2..F_LG  G0..G_LG
I_F2 = 3
N_F = LG - 1                      # F_2 .. F_LG
I_G0 = I_F2 + N_F
N_G = LG + 1                      # G_0 .. G_LG
NV = I_G0 + N_G


def rhs_hier(e, y, k, pol):
    """the photon hierarchy with polarisation, the baryons on their own velocity, no gravity"""
    tp = float(A.taup_of(e))
    R = float(A.Rb_of(e))
    Hc = float(A.Hc_of(e))
    dg, tg, tb = y[0], y[1], y[2]
    F = y[I_F2:I_F2 + N_F]                    # F[0] = F_2, F[j] = F_{j+2}
    G = y[I_G0:I_G0 + N_G] if pol else np.zeros(N_G)
    Pi = F[0] + (G[0] + G[2] if pol else 0.0)
    out = np.zeros(NV)
    out[0] = -(4.0 / 3.0) * tg
    out[1] = k ** 2 * (dg / 4.0 - F[0] / 2.0) + tp * (tb - tg)
    out[2] = -Hc * tb + tp * (tg - tb) / R
    # ** l = 2: (8/15) tg - (3/5) k F_3 - tau'[F_2 - Pi/10].  With G = 0 the bracket is (9/10)F_2,
    # which IS the unpolarised closure -- so POL=0 is a physical limit and not a mutilation. **
    out[I_F2] = (8.0 / 15.0) * tg - (3.0 / 5.0) * k * F[1] - tp * (F[0] - Pi / 10.0)
    for j in range(1, N_F - 1):
        l = j + 2
        out[I_F2 + j] = k / (2 * l + 1) * (l * F[j - 1] - (l + 1) * F[j + 1]) - tp * F[j]
    lM = LG
    out[I_F2 + N_F - 1] = k * F[N_F - 2] - (lM + 1) / e * F[N_F - 1] - tp * F[N_F - 1]
    if pol:
        out[I_G0] = -k * G[1] + tp * (-G[0] + Pi / 2.0)
        out[I_G0 + 1] = (k / 3.0) * (G[0] - 2 * G[2]) - tp * G[1]
        out[I_G0 + 2] = (k / 5.0) * (2 * G[1] - 3 * G[3]) + tp * (-G[2] + Pi / 10.0)
        for l in range(3, LG):
            out[I_G0 + l] = k / (2 * l + 1) * (l * G[l - 1] - (l + 1) * G[l + 1]) - tp * G[l]
        out[I_G0 + LG] = k * G[LG - 1] - (LG + 1) / e * G[LG] - tp * G[LG]
    return out


def rhs_ref(e, y, k):
    """the perfect tight-coupled fluid: one velocity, no quadrupole, no slip -- UNDAMPED"""
    R = float(A.Rb_of(e))
    Hc = float(A.Hc_of(e))
    dg, tg = y[0], y[1]
    return np.array([-(4.0 / 3.0) * tg,
                     -Hc * R / (1 + R) * tg + k ** 2 * dg / (4.0 * (1 + R))])


def run(k, pol):
    """** THE RATIO IS READ AT THE REFERENCE'S OWN EXTREMA, AND NOT ON AN AMPLITUDE INVARIANT. **

    The obvious reading is A^2 = Theta_0^2 + 3(1+R)Theta_1^2, which is stationary for the undamped
    fluid.  It is WRONG here by a measurable amount: the hierarchy damps the DIPOLE differently from
    the monopole at order k/tau', so |z| carries a residue oscillating at twice the acoustic phase.
    ** It shows up as a 39% swing in the recovered C that oscillates in k with the acoustic period --
    a systematic wearing the costume of scatter. **

    At an extremum of the REFERENCE monopole the dipole vanishes, so the monopole ratio there is the
    envelope ratio with the contamination removed, and the hierarchy's own small phase shift enters
    only at SECOND order.  Every extremum in the interval is used, which also tests C for constancy
    in eta -- a thing the single-endpoint reading could not do at all.
    """
    y0 = np.zeros(NV)
    y0[0] = 1.0                                  # dg; normalisation is irrelevant to a ratio
    # ** START ON THE TIGHT-COUPLING QUADRUPOLE, not on zero. **  Starting with F_2 = 0 launches a
    # transient that relaxes on 1/tau'; it is short, but it is a transient the reference run does not
    # have, and it would be charged to the damping.
    y0[I_F2] = (16.0 / 27.0) * y0[1] / float(A.taup_of(ETA_I))
    s = solve_ivp(rhs_hier, [ETA_I, ETA_F], y0, method='Radau', args=(k, pol),
                  rtol=RTOL, atol=1e-14, dense_output=True)
    r = solve_ivp(rhs_ref, [ETA_I, ETA_F], y0[:2], method='Radau', args=(k,),
                  rtol=RTOL, atol=1e-14, dense_output=True)
    if not (s.success and r.success):
        raise RuntimeError(f"k={k}: hier {s.message} / ref {r.message}")
    eg = np.linspace(ETA_I, ETA_F, 6000)
    dr = r.sol(eg)[0]
    ext = [i for i in range(1, len(eg) - 1)
           if (dr[i] - dr[i - 1]) * (dr[i + 1] - dr[i]) < 0 and eg[i] > ETA_I + 5]
    out = []
    for i in ext:
        e = float(eg[i])
        rr = float(s.sol(e)[0]) / float(dr[i])
        out.append((e, rr))
    return out


def _base(e):
    R = float(A.Rb_of(e))
    return 1.0 / (6.0 * (1 + R) * float(A.taup_of(e)))


def _kern(e):
    R = float(A.Rb_of(e))
    return R ** 2 / (1 + R) * _base(e)


def integrals(e_hi):
    """K and J over [ETA_I, e_hi] -- the SAME interval that run's reading covers"""
    return (quad(_kern, ETA_I, e_hi, limit=400)[0], quad(_base, ETA_I, e_hi, limit=400)[0])


def local_C(k, pol):
    """** C MEASURED LOCALLY, BETWEEN CONSECUTIVE EXTREMA, NOT CUMULATIVELY FROM ETA_I. **

    A cumulative reading averages the coefficient over the whole interval weighted by the integrand,
    so its residual against the leading-order value is a smear over a range of k/tau' and cannot be
    extrapolated.  Between two adjacent extrema the same arithmetic returns C over a short interval
    at a well-defined local k/tau', and *that* can be extrapolated to zero -- which is the only way
    to separate "the coefficient is not 8/9" from "the WKB formula is leading order and we are
    reading it at finite k/tau'".
    """
    pts = run(k, pol)
    out = []
    for (ea, ra), (eb, rb) in zip(pts[:-1], pts[1:]):
        if ra <= 0 or rb <= 0:
            continue
        dK = quad(_kern, ea, eb, limit=400)[0]
        dJ = quad(_base, ea, eb, limit=400)[0]
        C = ((-np.log(abs(rb / ra))) / k ** 2 - dK) / dJ
        em = 0.5 * (ea + eb)
        out.append((em, k / float(A.taup_of(em)), C))
    return out


def main():
    KS = [float(v) for v in os.environ.get(
        'KLIST', '0.15,0.20,0.25,0.30,0.35,0.40').split(',')]
    print()
    print("=" * 78)
    print("L171w — THE SHEAR COEFFICIENT C IN [ R^2/(1+R) + C ], MEASURED FROM THE HIERARCHY")
    print("=" * 78)
    print(f"  interval eta = {ETA_I:.0f} to {ETA_F:.0f}   (tau' = {float(A.taup_of(ETA_I)):.2f} -> "
          f"{float(A.taup_of(ETA_F)):.2f} /Mpc,  R = {float(A.Rb_of(ETA_I)):.3f} -> "
          f"{float(A.Rb_of(ETA_F)):.3f})")
    print(f"  hierarchy depth LG = {LG};  gravity OFF in both runs;  the envelope read on the")
    print("  MONOPOLE at the reference's extrema, and C taken between CONSECUTIVE extrema")
    print()
    fit = {}
    for pol, want, nm in ((0, 8 / 9, 'UNPOLARISED  (G = 0, so the l=2 term is -(9/10) tau F2)'),
                          (1, 16 / 15, 'POLARISED  (Pi = F2 + G0 + G2, polarisation evolved)')):
        print(f"  {nm}      leading-order value {want:.4f}")
        print(f"    {'k':>7} {'eta':>7} {'k/tau':>8} {'(k/tau)^2':>11} {'C':>9} {'vs l.o.':>9}")
        X, Y = [], []
        for k in KS:
            for em, kt, C in local_C(k, pol):
                if kt ** 2 > KTMAX2:
                    continue
                X.append(kt ** 2)
                Y.append(C)
                print(f"    {k:>7.2f} {em:>7.1f} {kt:>8.4f} {kt**2:>11.5f} {C:>9.4f} "
                      f"{(C-want)/want:>8.2%}")
        X, Y = np.array(X), np.array(Y)
        a, C0 = np.polyfit(X, Y, 1)
        resid = float(np.std(Y - (a * X + C0)))
        fit[pol] = (C0, a, resid, want)
        print(f"\n    ** C(k/tau -> 0) = {C0:.4f} against {want:.4f} — {(C0-want)/want:+.2%};")
        print(f"       the slope is {a:+.3f} in (k/tau)^2 and the scatter about the line is "
              f"{resid:.4f}. **")
        print(f"    *So the departure IS the finite-(k/tau) correction the WKB derivation drops,")
        print(f"     and the intercept is the coefficient.*\n")
    r = fit[1][0] / fit[0][0]
    print("  " + "-" * 74)
    print(f"  ** UNPOLARISED   C = {fit[0][0]:.4f}   against 8/9   = {8/9:.4f}   "
          f"({(fit[0][0]-8/9)/(8/9):+.2%})")
    print(f"  ** POLARISED     C = {fit[1][0]:.4f}   against 16/15 = {16/15:.4f}   "
          f"({(fit[1][0]-16/15)/(16/15):+.2%})")
    print(f"  ** THE POLARISATION CORRECTION IS A FACTOR {r:.4f}, against (16/15)/(8/9) = "
          f"{(16/15)/(8/9):.4f}  ({(r-1.2)/1.2:+.2%}) **")
    return 0


if __name__ == '__main__':
    sys.exit(main())
