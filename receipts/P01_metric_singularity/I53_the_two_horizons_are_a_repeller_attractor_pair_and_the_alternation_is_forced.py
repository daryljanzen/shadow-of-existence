#!/usr/bin/env python3
r"""I53 -- P01 MAKES THE HORIZON A FIXED POINT WITH AN EIGENVALUE.  READ AT THE NEXT ORDER, THE TWO
     HORIZONS OF SdS ARE A REPELLER/ATTRACTOR PAIR WHOSE INDICES CANCEL -- AND THE ALTERNATION IS
     FORCED BY DEGREE, NOT BY THE METRIC.

** WHAT THE PAPER HAS.  ** `BH_causality_v2.tex` L191: *"the outgoing null rays obey the
one-dimensional flow $\dd r/\dd v=f(r)/2$, whose equilibria are precisely the zeros of $f$ ... Its
eigenvalue is the surface gravity ... the fixed point is hyperbolic exactly when $\kappa\neq0$."*
  ⌗ *That sentence carries `\ldg{integrable_systems}` -- 59 landed it from the dynamical side, and it
  is the reason this row was predicted at all.*  ** What is NOT there is the next order: a flow on a
  line has more than one equilibrium, and the relation BETWEEN them is a topological fact. **

*** THE FINDING.  Between two consecutive SIMPLE zeros of $f$ the sign of $f$ does not change, so the
    derivative at consecutive zeros must ALTERNATE.  ⇒ The black-hole and cosmological horizons of
    Schwarzschild--de Sitter are necessarily a REPELLER and an ATTRACTOR -- their surface gravities
    carry opposite signs and their fixed-point indices sum to ZERO -- and this is forced by the
    intermediate value theorem on ANY function with simple zeros, not by the SdS metric. ***

  ⛭ ** AND THE NARIAI MEMBER IS THE DEGENERATE MERGE. **  *At $3\sqrt3\,M=\alpha$ the two roots
  collide into a double zero: the alternation argument's hypothesis fails, both eigenvalues vanish
  together, and the pair annihilates -- which is a Poincare--Hopf statement about a vector field on a
  line and is exactly the configuration `P01` L400-406 discusses as $\kappa=0$, the $p=1$ against
  $p=2$ split.*  ** So "the two horizons coincide at Nariai" and "the surface gravity vanishes there"
  are one index statement, and the corpus reaches them separately. **

⛔ ** MEASURED ABSENT IN THE SOURCE, so the finding is not a re-statement: ** *`Poincare--Hopf` x0,
`index of a vector field` x0, `winding number` x0, `attractor`/`repeller`/`opposite sign` x0 across
every `corpus/*.tex`.  The corpus has both horizons, both surface gravities and the Nariai merge, and
never says the signs are forced.*

WHAT IS MEASURED, and each part has a control that can fail:
  (A) on SdS, over a sweep of masses: the two physical horizons' $\kappa$ have OPPOSITE signs and the
      signs sum to zero.
  (B) ** the alternation is TOPOLOGICAL, not SdS's: ** the same test on random polynomials with simple
      zeros must alternate too -- and a deliberately built DOUBLE zero must BREAK it, which is the
      control showing the "simple" hypothesis is load-bearing rather than decorative.
  (C) the Nariai limit: both $\kappa\to0$ together as $3\sqrt3 M\to\alpha$, at the measured rate.

COMPUTES: scope.
  * `ALPHA = 1` sets the length unit; the statement is scale-free and the mass sweep is in units of the
    Nariai mass, so no number here depends on it.
  * ** the mass sweep stops short of Nariai by design: ** AT Nariai the hypothesis of (A) is false, and
    that is the point of (C) rather than a gap in (A).
  * ** NOT CLAIMED: that this is the Poincare--Hopf theorem on a compact manifold. **  *The flow lives
    on an interval of the line with the zeros in its interior; the index sum being zero is the
    one-dimensional degree statement, and calling it Poincare--Hopf is an analogy that the compactness
    hypothesis does not license.  What IS claimed is the alternation and its forcing.*

Written r3662 by node 60, pass B on row 6 of the index-theory locator (`P01`).
"""
import numpy as np

np.random.seed(7)

ALPHA = 1.0
M_NARIAI = ALPHA / (3.0 * np.sqrt(3.0))


def f_sds(r, M, alpha=ALPHA):
    return 1.0 - 2.0 * M / r - r * r / (alpha * alpha)


def horizons(M, alpha=ALPHA):
    r"""the positive simple zeros of $f$, from the cubic $-r^3/\alpha^2 + r - 2M$"""
    rts = np.roots([-1.0 / (alpha * alpha), 0.0, 1.0, -2.0 * M])
    real = sorted(x.real for x in rts if abs(x.imag) < 1e-9 and x.real > 1e-9)
    return real


def kappa(r, M, alpha=ALPHA, h=1e-6):
    """surface gravity $\\kappa = f'(r)/2$, by central difference"""
    return (f_sds(r + h, M, alpha) - f_sds(r - h, M, alpha)) / (2 * h) / 2.0


def alternates(roots, fn, h=1e-7):
    """do the derivatives at consecutive simple zeros alternate in sign?"""
    d = [(fn(x + h) - fn(x - h)) / (2 * h) for x in roots]
    return all(d[i] * d[i + 1] < 0 for i in range(len(d) - 1)), [int(np.sign(x)) for x in d]


if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('(A) SdS — the two horizons, swept in mass')
    print('=' * 78)
    print(f"    {'M/M_Nariai':>11} {'r_h':>9} {'r_c':>9} {'kappa_h':>11} {'kappa_c':>11}  signs")
    sums = []
    for frac in (0.2, 0.4, 0.6, 0.8, 0.95, 0.999):
        M = frac * M_NARIAI
        rs = horizons(M)
        assert len(rs) == 2, (frac, rs)
        kh, kc = kappa(rs[0], M), kappa(rs[1], M)
        s = int(np.sign(kh)) + int(np.sign(kc))
        sums.append(s)
        print(f'    {frac:>11.3f} {rs[0]:>9.5f} {rs[1]:>9.5f} {kh:>+11.5f} {kc:>+11.5f}'
              f'  {int(np.sign(kh)):+d}{int(np.sign(kc)):+d} -> {s}')
    print()
    print('    ⇒ the black-hole horizon REPELS (kappa>0) and the cosmological horizon')
    print('      ATTRACTS (kappa<0), at every mass.  Their indices sum to zero.')

    print()
    print('=' * 78)
    print('(B) THE CONTROL — is the alternation SdS\'s, or topology\'s?')
    print('=' * 78)
    ok = 0
    for _ in range(300):
        rts = np.sort(np.random.uniform(0.5, 5.0, 4))
        if np.min(np.diff(rts)) < 0.15:
            continue
        g = lambda x, R=rts: float(np.prod([x - t for t in R]))
        good, signs = alternates(list(rts), g)
        ok += good
    print(f'    random quartics with 4 well-separated SIMPLE zeros: {ok} of 300 alternate')
    print('    *(the shortfall is only samples rejected for near-degenerate spacing)*')
    rts_dbl = [1.0, 2.0, 2.0, 3.5]
    gd = lambda x: float(np.prod([x - t for t in rts_dbl]))
    good_d, signs_d = alternates([1.0, 2.0, 3.5], gd)
    print(f'    a DOUBLE zero at r=2 :  alternates = {good_d}   derivative signs {signs_d}')
    print('    ⇒ the alternation holds for every simple-zero function and BREAKS at a double')
    print('      zero, so it is the topology of simple zeros and not the SdS metric.')

    print()
    print('=' * 78)
    print('(C) THE NARIAI MERGE — the pair annihilates, both indices to zero')
    print('=' * 78)
    for frac in (0.9, 0.99, 0.999, 0.9999):
        M = frac * M_NARIAI
        rs = horizons(M)
        kh, kc = kappa(rs[0], M), kappa(rs[1], M)
        print(f'    M/M_N = {frac:<7.4f}  gap r_c-r_h = {rs[1]-rs[0]:.6f}   '
              f'|kappa_h| = {abs(kh):.6f}   |kappa_c| = {abs(kc):.6f}')
    print()
    print('    ⇒ the two fixed points merge and BOTH eigenvalues vanish together: the')
    print('      degenerate zero has index 0, which is the pair cancelling.  P01 reaches')
    print('      the same configuration at L400-406 as "kappa = 0", the p=1 against p=2')
    print('      split — and does not say it is the two indices annihilating.')

    # ⛔⛭ pinned to measured values -- never `expr == True`
    assert sums == [0, 0, 0, 0, 0, 0], sums
    assert ok >= 200, ok
    assert good_d is False, good_d
    khn = abs(kappa(horizons(0.9999 * M_NARIAI)[0], 0.9999 * M_NARIAI))
    kh9 = abs(kappa(horizons(0.9 * M_NARIAI)[0], 0.9 * M_NARIAI))
    assert khn < 0.1 * kh9, (khn, kh9)
    print()
    print('  ALL PASS')
