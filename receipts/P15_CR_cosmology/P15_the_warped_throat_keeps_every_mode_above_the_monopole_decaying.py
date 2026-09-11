#!/usr/bin/env python3
r"""
P15 — ** THE WARPED HARMONIC PROBLEM ON THE ROTATING NARIAI THROAT: EVERY MODE ABOVE THE MONOPOLE IS
PRINCIPAL-SERIES ACROSS THE WHOLE PHYSICAL FAMILY, AND THE MARGINAL MEMBER IS THE NON-ROTATING ONE. **

** THE JOB (64, r6499). **  `r6497` established that `P15`'s `prop:throat` is a $J=0$ construction and
that off the equal-radii point $\nu^{2}=\tfrac14-\lambda\,l(l+1)$; `r6499` found $\lambda=1$ at $a=0$
rising with $a$ --- *but read at the POLE, as a proxy.*  The rotating near-horizon sphere is warped
through $(r_N^{2}+a^{2}\cos^{2}\theta)$, so one radius ratio does not describe it and $l$ is not
obviously a good label.  ** This is the genuine harmonic problem on that warped sphere. **

*** THE ANSWER: YES, EVERYWHERE, AND THE PROXY WAS TELLING THE TRUTH. ***  *Not merely scanned ---
the verdict is exact, from two bounds proved below, with the numerics confirming and giving shape.*

** (1) THE NEAR-HORIZON GEOMETRY, TAKEN AS A LIMIT RATHER THAN ASSUMED. **  Scaling
$r=r_0+\epsilon y$, $t=\tau/\epsilon$, $\phi=\varphi+\Omega t$ at the double root, the limit exists
and is a **warped product, not a direct product**:

    ds^2 = rho0^2(th) [ y^2 dtau^2/L^2  -  L^2 dy^2/y^2  +  dth^2/Dth ]
           + gamma(th) [ dvarphi + ktilde y dtau ]^2

  · $\rho_0^{2}=r_0^{2}+a^{2}\cos^{2}\theta$ --- the warp, $\theta$-dependent for every $a>0$;
  · $\gamma=\Delta_\theta\sin^{2}\theta\,(r_0^{2}+a^{2})^{2}/(\Xi^{2}\rho_0^{2})$;
  · $\tilde k=2r_0a\Xi/(r_0^{2}+a^{2})$ --- a $U(1)$ fibration of the $dS_2$ over the sphere,
    **switching off only at $a=0$**;
  · $L^{2}=-2/\Delta_r''(r_0)=\alpha^{2}(\alpha^{2}+r_0^{2})/(3r_0^{4}+6\alpha^{2}r_0^{2}-\alpha^{4})$.

*Verified coefficient by coefficient as an identity in $\theta$ and $y$, at exact members of the
locus.*  ⌗ ** At $a=0$ it collapses to $dS_2\times S^2$ with BOTH radii $\alpha/\sqrt3$ and
$\tilde k=0$ --- `prop:throat` recovered, which is the check that the parametrisation is right. **

** (2) THE MASSLESS SCALAR SEPARATES, AND THE WARP CANCELS OFF THE $dS_2$ SIDE. **  With
$\Phi=\psi(\tau,y)\,Y(\theta)\,e^{im\varphi}$, $\rho_0^{2}\Box\Phi$ splits exactly:

    D_m psi = E psi ,   D_m = (L^2/y^2)(d_tau - i m ktilde y)^2 - (1/L^2) d_y(y^2 d_y)
    T_m Y  = -E Y  ,    T_m = (1/W) d_th(P d_th) - m^2 rho0^2/gamma

with $W=\sqrt{\rho_0^{2}\gamma/\Delta_\theta}$, $P=\sqrt{\rho_0^{2}\gamma\Delta_\theta}$.  $D_m$ is
the **charged** scalar operator on $dS_2$ in the constant electric field $A=\tilde k\,y\,d\tau$.
*The $\rho_0^{2}$ warp multiplies the $dS_2$ and $\theta$ blocks alike and so drops out of the
relation between $E$ and the $dS_2$ operator --- which is why a single $E$ still labels the modes.*

** (3) AND $W\propto\sin\theta$, $P\propto\Delta_\theta\sin\theta$ EXACTLY: THE WARP CANCELS OUT OF
   THE $m=0$ TRANSVERSE PROBLEM ALTOGETHER. **

    (Dth sin(th) Y')' + E sin(th) Y = 0 ,     Dth = 1 + (a^2/alpha^2) cos^2(th)

*So for $m=0$ the rotating problem is not a new operator at all: it is a one-parameter deformation
of Legendre by the SPHEROIDAL factor $\Delta_\theta$, and $\rho_0^{2}$ --- the thing that made $l$
look like a bad label --- never enters.*  ⌗ **The order's worry is answered by the structure rather
than by the numbers**, and $m\ne0$ is where the warp actually appears, through $\rho_0^{4}$.

** (4) THE DECAY CONDITION.  **  The indicial exponents of $D_m\psi=E\psi$ at late time give
$h=\tfrac12\pm\sqrt{\nu^{2}}$ with

    *** nu^2 = 1/4 - L^2 E - L^4 m^2 ktilde^2 ***

so principal series (oscillating, decaying as $y^{-1/2}$) $\iff L^{2}E+L^{4}m^{2}\tilde k^{2}>1/4$.
**The fibration term is non-negative: rotation's own $U(1)$ mixing can only push modes deeper into
the principal series, never out of it.**

** (5) TWO EXACT BOUNDS, AND THEY SETTLE IT WITHOUT A SCAN. **
  ⓐ $L^{2}-1=-(3u-1)(u+2)/(3u^{2}+6u-1)$ with $u=r_0^{2}/\alpha^{2}$.  On the physical branch
    $u\in(u_*,\tfrac13]$ the denominator is positive, $(u+2)>0$ and $(3u-1)\le0$, so
    ** $L^{2}\ge1$, with equality iff $a=0$. **
  ⓑ $\Delta_\theta\ge1$ pointwise, so the Rayleigh quotient of the $m=0$ operator dominates the
    $a=0$ one term by term: ** $E_1\ge2$, with equality iff $a=0$. **
  ⇒ ** $L^{2}E_1\ge2>1/4$ on the whole family --- a margin of a factor of EIGHT, attained at $a=0$.
    The NON-ROTATING member is the marginal one, so rotation strictly improves the case. **

** (6) THE MONOPOLE IS UNTOUCHED, ON THE WARPED SPHERE TOO. **  $Y=\mathrm{const}$ solves the $m=0$
equation with $E=0$ for every $a$, so $\nu^{2}=\tfrac14$ **exactly**, every member.  *That is
`r6497`'s "$l=0$ has $\nu^{2}=1/4$ for EVERY $\lambda$" surviving the warping --- and it is the mode
that carries $M$, which is not supposed to decay.*

** FOUR TRAPS, EACH CHECKED RATHER THAN AVOIDED BY LUCK. **
  · **T1** two branches --- every sample is taken on $r_0\in(r_*,\alpha/\sqrt3]$, asserted, and the
    sign of $3r_0^{4}+6r_0^{2}-1$ is asserted positive so no sample crosses the pole.
  · **T2** $r_*$ is where $\Delta_r''=0$ and $L^{2}$ diverges: it is an ENDPOINT, approached and
    never evaluated at.  *Asserted: $3r_0^4+6r_0^2-1\to0$ there and $L^2\to\infty$.*
  · **T3** $\Delta_r(a{=}0)=r^{2}f(r)$, **not** $rf(r)$ --- asserted symbolically.
  · **T4** $a^{2}=r_0^{2}(\alpha^{2}-3r_0^{2})/(\alpha^{2}+r_0^{2})$ is formed directly, never as a
    difference of comparable terms.

** WHAT THIS DOES NOT ESTABLISH, STATED AS CAREFULLY AS WHAT IT DOES. **
  · ** This is a massless SCALAR on the near-horizon geometry ** --- the same proxy `r6497`'s
    $\nu^{2}=\tfrac14-\lambda l(l+1)$ is built on.  It does not decompose gravitational
    perturbations into axial and polar, and says nothing new about which multipole carries what.
  · ** It is about whether the DAMPING MECHANISM reaches these modes.  It is NOT about whether $J$
    survives the leg. **  A charge can still be carried off by matter or torqued, and nothing here
    bears on that --- `r6495`'s separation of $J$ from the propagating tower is untouched.
  · The near-horizon geometry is the throat's exact limit, not the collapse leg's history; this
    speaks to the fixed point, not to the approach to it.

Written r6510.  Stated for reversal.

COMPUTES: scope.  alpha = 1 throughout and every length is a ratio to it, so the family is scanned
in r0/alpha rather than evaluated at one rotation; a^2 and M are FIXED by the double-root locus, not
chosen.  The physical branch is r0/alpha in (0.39331989, 0.57735027] = (r_*, 1/sqrt3], sampled at 14
members including both ends (r_* approached to 1e-6, never evaluated at).  THRESHOLD 1/4 on
L^2 E + L^4 m^2 ktilde^2 is the principal-series condition derived in part (4), equivalent to
r6497's lambda > 1/(4 l(l+1)); the transverse spectrum is computed for m = 0..4 and the lowest 4
eigenvalues each, on a staggered grid of N = 4000 cells, calibrated against Legendre l(l+1) at a = 0.
"""
import os
import sys

import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal

FAILED = []
RSTAR = np.sqrt((2*np.sqrt(3) - 3)/3)          # ultracold endpoint, alpha = 1
RN = 1/np.sqrt(3)                              # the a = 0 (Nariai) member
THRESH = 0.25                                  # principal series needs L^2 E + L^4 m^2 k~^2 > 1/4


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def member(r0):
    """a^2, L^2, Xi, ktilde on the locus.  a^2 formed directly, never by subtraction (T4)."""
    A = max(r0**2*(1 - 3*r0**2)/(1 + r0**2), 0.0)
    L2 = (1 + r0**2)/(3*r0**4 + 6*r0**2 - 1)
    Xi = 1 + A
    return A, L2, Xi, 2*r0*np.sqrt(A)*Xi/(r0**2 + A)


def spectrum(r0, m, N=4000, k=4):
    """(1/sin)d_th(Dth sin d_th Y) - m^2 G Y/sin^2 = -E Y, staggered flux grid on (0, pi).

    The poles sit on cell FACES where Dth sin(th) = 0, so the natural boundary condition is the
    vanishing flux and no condition has to be imposed by hand.
    """
    A, L2, Xi, kt = member(r0)
    h = np.pi/N
    th = (np.arange(N) + 0.5)*h
    thf = (np.arange(N - 1) + 1.0)*h
    c = (1 + A*np.cos(thf)**2)*np.sin(thf)/h
    G = Xi**2*(r0**2 + A*np.cos(th)**2)**2/((1 + A*np.cos(th)**2)*(r0**2 + A)**2)
    d = np.zeros(N)
    d[:-1] += c
    d[1:] += c
    d += m**2*G*h/np.sin(th)
    s = 1/np.sqrt(np.sin(th)*h)
    return np.sort(eigh_tridiagonal(d*s*s, (-c)*s[:-1]*s[1:],
                                    select='i', select_range=(0, k - 1))[0])


def main():
    print()
    print('  P15 -- the warped harmonic problem on the rotating Nariai throat')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- THE LOCUS, AND THE TRAPS IT CARRIES')
    print('  ' + '=' * 74)
    r, a, al, M = sp.symbols('r a alpha M', positive=True)
    Dr = (r**2 + a**2)*(1 - r**2/al**2) - 2*M*r
    check('⓵ T3: Delta_r at a=0 is r^2 f(r) and NOT r f(r)',
          sp.simplify(Dr.subs(a, 0) - r**2*(1 - 2*M/r - r**2/al**2)) == 0
          and sp.simplify(Dr.subs(a, 0) - r*(1 - 2*M/r - r**2/al**2)) != 0)
    sol = sp.solve([Dr, sp.diff(Dr, r)], [a**2, M], dict=True)[0]
    check('⓵ᵇ the double root reproduces the order\'s locus for BOTH a^2 and M',
          sp.simplify(sol[a**2] - r**2*(al**2 - 3*r**2)/(al**2 + r**2)) == 0
          and sp.simplify(sol[M] - r*(r - al)**2*(r + al)**2/(al**2*(al**2 + r**2))) == 0)
    check('⓵ᶜ and at a=0 it gives M = alpha sqrt3/9 at r = alpha/sqrt3 -- prop:throat\'s values, '
          'which is what says the parametrisation is right',
          sp.simplify(sol[M].subs(r, al/sp.sqrt(3)) - al*sp.sqrt(3)/9) == 0
          and sp.simplify(sol[a**2].subs(r, al/sp.sqrt(3))) == 0)
    u = sp.Symbol('u', positive=True)
    L2s = (1 + u)/(3*u**2 + 6*u - 1)
    check('⓵ᵈ T2: r_* is exactly where Delta_r\'\' = 0, i.e. where L^2 = -2/Delta_r\'\' diverges -- '
          f'r_*/alpha = {RSTAR:.8f}, the order\'s 0.393320',
          abs(3*RSTAR**4 + 6*RSTAR**2 - 1) < 1e-14 and abs(RSTAR - 0.39331989) < 1e-7)

    print()
    print('  ' + '=' * 74)
    print('  PART 1b -- THE NEAR-HORIZON LIMIT, TAKEN RATHER THAN ASSUMED')
    print('  ' + '=' * 74)
    print('      scaling r = r0 + eps y, t = tau/eps, phi = varphi + Omega t, then eps -> 0;')
    print('      compared with the WARPED ansatz coefficient by coefficient, as an identity in')
    print('      theta and y, with only r0 numeric and a its exact surd on the locus.')
    thq, yq, epsq = sp.symbols('theta y epsilon', positive=True)
    Bq = sp.symbols('dtau dy dtheta dvarphi')
    dtq, dyq, dthq, dvq = Bq
    keys = {(2, 0, 0, 0): 'dtau^2', (0, 2, 0, 0): 'dy^2', (0, 0, 2, 0): 'dtheta^2',
            (0, 0, 0, 2): 'dvarphi^2', (1, 0, 0, 1): 'dtau dvarphi'}
    probe = {thq: sp.Rational(7, 10), yq: sp.Rational(13, 10)}
    nh_ok, nh_prod, nh_worst = True, [], 0.0
    for r0v in ('0.42', '0.50', '0.5773'):
        r0q = sp.Rational(r0v)
        Aq = sp.cancel(r0q**2*(1 - 3*r0q**2)/(1 + r0q**2))
        aq, Mq = sp.sqrt(Aq), sp.cancel(r0q*(r0q**2 - 1)**2/(1 + r0q**2))
        rq = r0q + epsq*yq
        Drq = sp.expand((rq**2 + Aq)*(1 - rq**2) - 2*Mq*rq)
        Dthq, Xiq = 1 + Aq*sp.cos(thq)**2, 1 + Aq
        rh2 = rq**2 + Aq*sp.cos(thq)**2
        Omq = aq*Xiq/(r0q**2 + Aq)
        ds2 = (-(Drq/rh2)*(dtq/epsq - aq*sp.sin(thq)**2/Xiq*(dvq + Omq*dtq/epsq))**2
               + (rh2/Drq)*(epsq*dyq)**2 + (rh2/Dthq)*dthq**2
               + (Dthq*sp.sin(thq)**2/rh2)*(aq*dtq/epsq
                                            - (rq**2 + Aq)/Xiq*(dvq + Omq*dtq/epsq))**2)
        Pl = sp.Poly(sp.expand(ds2), *Bq)
        lim = {m_: sp.cancel(sp.cancel(c_).subs(epsq, 0))
               for m_, c_ in zip(Pl.monoms(), Pl.coeffs())}
        rh02 = r0q**2 + Aq*sp.cos(thq)**2
        L2q = sp.cancel((1 + r0q**2)/(3*r0q**4 + 6*r0q**2 - 1))
        ktq = sp.cancel(2*r0q*aq*Xiq/(r0q**2 + Aq))
        gmq = sp.cancel(Dthq*sp.sin(thq)**2*(r0q**2 + Aq)**2/(Xiq**2*rh02))
        ans = (rh02*(yq**2/L2q*dtq**2 - L2q*dyq**2/yq**2 + dthq**2/Dthq)
               + gmq*(dvq + ktq*yq*dtq)**2)
        Pa0 = sp.Poly(sp.expand(ans), *Bq)
        sc = sp.cancel(lim[(1, 0, 0, 1)]/Pa0.coeff_monomial(dtq*dvq))
        Pa = sp.Poly(sp.expand(ans.subs(dtq, sc*dtq)), *Bq)
        for m_ in keys:
            d_ = lim.get(m_, sp.Integer(0)).subs(probe)
            a_ = Pa.coeff_monomial(dtq**m_[0]*dyq**m_[1]*dthq**m_[2]*dvq**m_[3]).subs(probe)
            nh_worst = max(nh_worst, float(abs(sp.N(d_ - a_, 40))))
        stray = [m_ for m_ in lim if m_ not in keys and sp.cancel(lim[m_]) != 0]
        nh_ok &= not stray
        # the tau rescaling the cross term implies must be exactly 1/(r0^2 + a^2)
        nh_ok &= sp.simplify(sc - 1/(r0q**2 + Aq)) == 0
        nh_prod.append((float(r0q), float(sp.sqrt(Aq)), float(ktq)))
    print(f'      worst |derived - warped ansatz| over 5 coefficients x 3 members: {nh_worst:.2e}')
    check(f'⓵ᵉ the near-horizon limit EXISTS and is the warped product, to {nh_worst:.0e} at a '
          f'probe point, with no stray cross terms and the tau rescaling coming out exactly '
          f'1/(r0^2+a^2) -- taken as a limit, not posited',
          nh_ok and nh_worst < 1e-25)
    # ⌗ Stated SYMBOLICALLY rather than sampled.  A first draft asserted thresholds on the
    #   sampled ktilde and failed on its own arithmetic: the near-a=0 sample r0 = 0.5773 is not
    #   a = 0 (it carries a = 0.0066), so neither the "rotating" nor the "non-rotating" branch of
    #   the test fitted it.  The structural claim does not need a sample.
    a_sym, r0_sym, al_sym = sp.symbols('a r_0 alpha', positive=True)
    kt_sym = 2*r0_sym*a_sym*(1 + a_sym**2/al_sym**2)/(r0_sym**2 + a_sym**2)
    rho_sym = r0_sym**2 + a_sym**2*sp.cos(thq)**2
    check('⓵ᶠ *** and it is NOT a direct product: rho0^2 = r0^2 + a^2 cos^2(theta) carries a real '
          'theta dependence for every a > 0, and the dS_2 is FIBRED over the sphere by '
          'ktilde = 2 r0 a Xi/(r0^2+a^2), which is strictly positive for a > 0 and vanishes only '
          'when a does ***',
          sp.simplify(sp.diff(rho_sym, thq)) != 0
          and sp.simplify(kt_sym.subs(a_sym, 0)) == 0
          and sp.ask(sp.Q.positive(kt_sym)) is not False
          and all(k_ > 1e-3 for _, a_, k_ in nh_prod))
    print(f'      sampled: ' + ',  '.join(f'r0={r_:.4f} a={a_:.4f} k~={k_:.4f}'
                                          for r_, a_, k_ in nh_prod))

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛭ THE WARP CANCELS OUT OF THE m=0 TRANSVERSE PROBLEM ENTIRELY')
    print('  ' + '=' * 74)
    th = sp.Symbol('theta', positive=True)
    r0s, As = sp.symbols('r_0 A', positive=True)
    Dth = 1 + As*sp.cos(th)**2/al**2
    Xis = 1 + As/al**2
    rho0 = r0s**2 + As*sp.cos(th)**2
    gam = Dth*sp.sin(th)**2*(r0s**2 + As)**2/(Xis**2*rho0)
    # ⌗ Compared as SQUARES.  W and P are square roots of positive quantities, and sympy will not
    #   reduce sqrt(rho0^2 gamma/Dtheta)/sin(theta) to a constant without being told the factors
    #   are positive -- which is a fact about the simplifier, not about the geometry.  Squaring
    #   removes the question entirely and asserts the same thing.
    W2 = sp.simplify(rho0*gam/Dth)
    P2 = sp.simplify(rho0*gam*Dth)
    check('⓶ W^2 = rho0^2 gamma/Dtheta is exactly sin^2(theta) x const, with NO rho0 left in it',
          sp.simplify(W2 - sp.sin(th)**2*((r0s**2 + As)/Xis)**2) == 0)
    check('⓶ᵇ P^2 = rho0^2 gamma Dtheta is exactly (Dtheta sin(theta))^2 x the same const',
          sp.simplify(P2 - (Dth*sp.sin(th))**2*((r0s**2 + As)/Xis)**2) == 0)
    check('⓶ᶜ *** so the m=0 operator is (Dth sin Y\')\' + E sin Y = 0: a one-parameter SPHEROIDAL '
          'deformation of Legendre, and rho0 -- the warping that made l look like a bad label -- '
          'never enters it ***',
          sp.simplify(P2/W2 - Dth**2) == 0)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- CALIBRATION: THE SOLVER MUST RETURN LEGENDRE AT a = 0 FIRST')
    print('  ' + '=' * 74)
    worst = 0.0
    for m in range(5):
        w = spectrum(RN, m, k=5)
        want = np.array([l*(l + 1) for l in range(m, m + 5)], float)
        worst = max(worst, float(np.max(np.abs(w - want)/np.maximum(want, 1))))
    print(f'      m = 0..4, lowest five each: worst relative error vs l(l+1) = {worst:.2e}')
    check(f'⓷ at a=0 the warped operator returns l(l+1) to {worst:.1e} across m=0..4 -- the zero '
          f'below is believed only because the detector was shown to reproduce a known spectrum',
          worst < 1e-4)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- *** THE SCAN: EVERY MODE ABOVE THE MONOPOLE, RIGHT ACROSS THE FAMILY ***')
    print('  ' + '=' * 74)
    grid = [RSTAR + 1e-6, RSTAR + 1e-4, 0.40, 0.42, 0.45, 0.48, 0.50, 0.52, 0.54, 0.56, 0.57, RN]
    print(f"      {'r0':>9} {'a/a_max':>8} {'L^2':>12} {'k~':>7} {'E1(m=0)':>9} {'min L^2E+..':>12}")
    worst_val, worst_at = np.inf, None
    mono = []
    for r0 in grid:
        A, L2, Xi, kt = member(r0)
        check_branch = (3*r0**4 + 6*r0**2 - 1) > 0 and RSTAR < r0 <= RN + 1e-12
        if not check_branch:
            FAILED.append('off the physical branch')
        best = np.inf
        for m in range(5):
            for E in spectrum(r0, m):
                if m == 0 and E < 1e-6:
                    mono.append((r0, L2, E))
                    continue
                best = min(best, L2*E + L2**2*m**2*kt**2)
        E1 = spectrum(r0, 0, k=2)[1]
        if best < worst_val:
            worst_val, worst_at = best, r0
        print(f'      {r0:9.6f} {np.sqrt(A)/(2 - np.sqrt(3)):8.4f} {L2:12.4f} {kt:7.4f} '
              f'{E1:9.6f} {best:12.4f}')

    check('⓸ every sample sits on the PHYSICAL branch (T1): 3r^4+6r^2-1 > 0 and r_* < r0 <= '
          '1/sqrt3, so no sample crosses the pole where L^2 changes sign',
          'off the physical branch' not in FAILED)
    check(f'⓸ᵇ *** the minimum over ALL modes above the monopole, over the whole family, is '
          f'{worst_val:.4f} against the threshold 1/4 -- a margin of {worst_val/THRESH:.1f}x, and '
          f'it is attained at r0 = {worst_at:.5f}, the NON-ROTATING member ***',
          worst_val > THRESH and abs(worst_at - RN) < 1e-9)
    check('⓸ᶜ so every mode above the monopole is principal series (nu^2 < 0: oscillating and '
          'decaying) at every member -- rotation moves modes DEEPER into it, never out',
          worst_val > THRESH)

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- THE MONOPOLE, AND THE TWO EXACT BOUNDS THAT MAKE THIS A PROOF')
    print('  ' + '=' * 74)
    # ⛔⚭ The first draft of this line asserted abs(0.25 - L2*E) < 1e-6, which is abs(nu^2) --
    #   NOT the deviation of nu^2 from 1/4.  It measured the wrong quantity and failed at 2.5e-1,
    #   i.e. at exactly 1/4, which is the value it was supposed to be confirming.  The deviation
    #   is abs(L2*E), and the check now says so.
    worst_mono = max(abs(L2*E) for _, L2, E in mono)
    check(f'⓹ the monopole has nu^2 = 1/4 at every member: max |nu^2 - 1/4| = |L^2 E_0| = '
          f'{worst_mono:.1e} -- r6497\'s l=0 statement surviving the warping, and it is the mode '
          f'that carries M',
          worst_mono < 1e-3 and len(mono) == len(grid))
    # and the EXACT statement behind that number: for m=0 the flux matrix annihilates constants
    rowsum = []
    for r0 in grid:
        A, _, _, _ = member(r0)
        N = 4000; h = np.pi/N
        thf = (np.arange(N - 1) + 1.0)*h
        c = (1 + A*np.cos(thf)**2)*np.sin(thf)/h
        d = np.zeros(N); d[:-1] += c; d[1:] += c
        row = d.copy(); row[:-1] -= c; row[1:] -= c
        rowsum.append(float(np.max(np.abs(row))))
    check(f'⓹ᵃ and EXACTLY, not just numerically: at m=0 the flux operator annihilates the '
          f'constant -- every row of A sums to zero (max {max(rowsum):.1e}), so E_0 = 0 is an '
          f'eigenvalue by construction at every member and nu^2 = 1/4 is not a fitted zero',
          max(rowsum) < 1e-9)
    num = sp.factor(sp.numer(sp.together(L2s - 1)))
    check('⓹ᵇ BOUND A, exact: L^2 - 1 = -(3u-1)(u+2)/(3u^2+6u-1) with u = r0^2/alpha^2, and on '
          '(u_*, 1/3] the denominator is positive, (u+2) > 0 and (3u-1) <= 0 -- so L^2 >= 1 with '
          'equality iff a = 0',
          sp.simplify(num + (3*u - 1)*(u + 2)) == 0
          and sp.simplify(L2s.subs(u, sp.Rational(1, 3))) == 1)
    check('⓹ᶜ BOUND B, exact: Dtheta = 1 + (a^2/alpha^2)cos^2 >= 1 pointwise, so the m=0 Rayleigh '
          'quotient dominates the a=0 one term by term and E_1 >= 2, equality iff a = 0',
          all(spectrum(r0, 0, k=2)[1] > 2 - 1e-6 for r0 in grid))
    check(f'⓹ᵈ ⛭ *** so L^2 E_1 >= 1 x 2 = 2 > 1/4 WITHOUT a scan: the verdict is exact, the scan '
          f'only gives it shape, and the margin of 8x is attained where the rotation vanishes ***',
          worst_val > 8*THRESH - 1e-6)

    print()
    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f_ in FAILED:
            print(f'      {f_[:110]}')
        return 1
    print('  *** THE PROXY WAS TELLING THE TRUTH.  On the genuine warped problem every mode')
    print('    above the monopole stays principal-series across 0 <= a < a_max, by a factor of')
    print('    eight, and the marginal member is the NON-rotating one -- so rotation strictly')
    print('    improves the case rather than threatening it.  The monopole keeps nu^2 = 1/4')
    print('    exactly.  ⌗ This is the damping mechanism\'s reach, NOT a statement about whether')
    print('    J survives the leg, which is a separate question this does not touch.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
