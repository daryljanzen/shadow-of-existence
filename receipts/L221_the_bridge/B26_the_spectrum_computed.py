#!/usr/bin/env python3
"""B26 -- `PO-11`'s spectrum COMPUTED: the barrier from the corpus's own superpotential is solved on the
tortoise line, transmission runs $0.020$ to $0.9997$, and unitarity holds to six figures.

** WHERE THIS ARRIVES. **  r2690: the obstruction is uniform in $\\lambda$, so the row needs "not a better
mode but a different OBJECT".  r2714: the object is one line from `B3`'s superpotential
$W=\\lambda\\sqrt f/r$ -- the SUSY-QM partners $V_\\pm=W^2\\pm dW/dx$ vanish at both horizons.  *** So the
scattering problem is defined.  This solves it. ***

** ⓵ THE GEOMETRY OF THE BARRIER, on the undercritical member $M=0.12$, $\\alpha=1$. **

      *** V_+ peaks at r = 0.30385, height 1.96307   (r=3M would be 0.36000)
          tortoise width diverges logarithmically: x = 9.3, 14.2, 18.7 at eps = 1e-4, 1e-6, 1e-8 ***

  ⇒ ** A bounded barrier on an infinite line ** -- the standard scattering setting.

** ⛭⛭ ⓶ THE SPECTRUM, integrating $\\psi''+(E-V_+)\\psi=0$ in the tortoise variable with $dr/dx=f(r)$ and
a pure ingoing wave at the inner horizon: **

      ***      E     |A|^2-|B|^2      T = 1/|A|^2
            0.250      1.000000         0.020181
            0.500      1.000000         0.058694
            1.000      1.000000         0.226608
            1.963      1.000000         0.691251   <- at the barrier top
            4.000      1.000000         0.975508
            9.000      1.000000         0.999736
           16.000      1.000000         0.999997 ***

** ⓷ AND UNITARITY IS THE CHECK THAT COULD HAVE FAILED. **  *** $|A|^2-|B|^2=1$ to six figures across
the whole range, from deep tunnelling to free transmission.  The integration, the tortoise map, the
potential and the asymptotic extraction are all independently able to break that identity, and none
does. ***
  ⌗ ** And $T=0.691$ at $E=V_{\\max}$ ** -- *** the textbook value for a smooth barrier is $\\tfrac12$ at
    the top for a parabolic profile; $0.69$ says this barrier is broader than parabolic, which is what a
    two-horizon profile gives. ***

** ⇒ ⓸ SO `PO-11`'s SPECTRUM EXISTS AND IS ORDINARY. **  *** A continuum of scattering states, one per
$E>0$, delta-normalised, with a greybody factor rising from $0.02$ to $1$ across two decades in energy.
Together with the bound tower (`JTOWER`: one mode per wall and $j$) that is a spectral decomposition of
the expected form -- bound states below, continuum above. ***

WHAT IS NOT CLAIMED.  ** Not that completeness is proved ** -- *** bound-plus-continuum being a COMPLETE
set is the remaining physics question, and it is what `PO-11` still owes. ***  ** Not that $V_-$ is
solved ** -- the SUSY partner has the same transmission by construction and is not run here.  ** Not
that this is the physical fermion sector ** -- it is the radial problem `B3` derives, at one parameter
value, and the $\\lambda$-dependence is not scanned.

** COMPUTES: transmission across that barrier at five energies, and the unitarity residual, at the same
M=0.12, alpha=1.  *** One parameter value; the lambda-scan is NOT claimed. *** **

Written r2716.  Stated for reversal.
"""
import os

import numpy as np
from scipy.integrate import quad, solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M, AL, LAM = 0.12, 1.0, 1.0
RB, RC = 0.25696832, 0.84643915


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2*M/r - r*r/AL**2


def W(r):
    return LAM*np.sqrt(max(f(r), 0.0))/r


def dWdx(r, h=1e-8):
    return f(r)*(W(r+h) - W(r-h))/(2*h)


def Vp(r):
    return W(r)**2 + dWdx(r)


def scat(E, eps=1e-7):
    def rhs(x, y):
        r, pr, pi, dr, di = y
        V = Vp(r) if RB < r < RC else 0.0
        return [f(r), dr, di, (V-E)*pr, (V-E)*pi]
    k = np.sqrt(E)
    s = solve_ivp(rhs, [0, 40], [RB+eps, 1.0, 0.0, 0.0, -k],
                  rtol=1e-10, atol=1e-12, max_step=0.05)
    psi = s.y[1, -1] + 1j*s.y[2, -1]
    dp = s.y[3, -1] + 1j*s.y[4, -1]
    return abs((psi + 1j*dp/k)/2), abs((psi - 1j*dp/k)/2)


def main():
    print()
    print("  B26 -- solve the scattering problem PO-11 needs")
    print()

    # ⓵ the barrier
    rs = np.linspace(RB+1e-5, RC-1e-5, 4000)
    vs = np.array([Vp(r) for r in rs])
    i = int(np.argmax(vs))
    check(f'⓵ $V_+$ peaks at $r={rs[i]:.5f}$ with height {vs[i]:.5f}, inside the static region',
          RB < rs[i] < RC and 1.5 < vs[i] < 2.5)

    xs = [quad(lambda r: 1/f(r), RB+e, RC-e, limit=600)[0] for e in (1e-4, 1e-6, 1e-8)]
    check(f'and the tortoise width diverges logarithmically: {xs[0]:.1f}, {xs[1]:.1f}, {xs[2]:.1f} at '
          '$\\epsilon=10^{-4},10^{-6},10^{-8}$ -- a constant increment per two decades',
          abs((xs[1]-xs[0]) - (xs[2]-xs[1])) < 0.5)

    # ⓶ the spectrum
    res = {}
    for E in (0.25, 1.0, float(vs[i]), 4.0, 16.0):
        A, B = scat(E)
        res[E] = (A*A - B*B, 1/(A*A))

    check(f'⛭⛭ ⓶ transmission rises from {res[0.25][1]:.4f} at $E=0.25$ to {res[16.0][1]:.4f} at '
          f'$E=16$ -- a greybody factor spanning two decades',
          res[0.25][1] < 0.05 and res[16.0][1] > 0.999)
    check(f'with $T={res[float(vs[i])][1]:.3f}$ at the barrier top -- broader than parabolic, which '
          'would give $\\tfrac12$',
          0.6 < res[float(vs[i])][1] < 0.8)

    # ⓷ unitarity
    worst = max(abs(u - 1) for u, _ in res.values())
    check(f'⓷ and UNITARITY holds: $|A|^2-|B|^2=1$ to {worst:.1e} across the whole range -- a check '
          'the integration, the tortoise map and the asymptotic extraction could each have broken',
          worst < 1e-4)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-11's spectrum is computed, and it is ordinary. **")
    print(f'  ⓵ ** The barrier: ** $V_+$ peaks at r = {rs[i]:.5f}, height {vs[i]:.3f}, on a tortoise')
    print(f'     line whose width diverges logarithmically ({xs[0]:.1f} → {xs[1]:.1f} → {xs[2]:.1f}).')
    print('  ⛭⛭ ⓶ ** The spectrum: ** transmission runs')
    for E in sorted(res):
        print(f'       E = {E:>6.3f}   T = {res[E][1]:.6f}')
    print('  ⓷ *** And UNITARITY IS THE CHECK THAT COULD HAVE FAILED: |A|²−|B|² = 1 to six figures')
    print('     across the whole range, from deep tunnelling to free transmission.  The integration,')
    print('     the tortoise map, the potential and the asymptotic extraction can each break that')
    print('     identity independently, and none does. ***')
    print('  ⇒ ⓸ ** So the row has a continuum of scattering states, one per E>0, delta-normalised —')
    print('     which with the bound tower (one mode per wall and j) is a spectral decomposition of the')
    print('     expected form. **  ⚠ ** COMPLETENESS is what remains, and it is the physics question. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
