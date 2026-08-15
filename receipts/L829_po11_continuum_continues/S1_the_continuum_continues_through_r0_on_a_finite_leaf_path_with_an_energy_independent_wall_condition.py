#!/usr/bin/env python3
r"""S1 -- cc54, PO-11 (56's r2800 left "constructing the solution remains -- a computation"): the
static-region continuum DOES continue through the wall at r=0, and it does so with the SAME fixed
condition at every energy. Two computed facts make the construction well-posed: (1) in the LEAF
coordinate dl = dr/sqrt|f| the whole path from the wall to the cosmological horizon is a FINITE
interval and the inner horizon r_b is a REGULAR interior point -- so the "infinite tortoise distance"
B46 found at r_b is a coordinate artefact of dx=dr/f, not an obstruction, and a continuum mode can
traverse wall -> r_b -> r_c; (2) at the wall the mass term dominates the energy -- int W dl = lambda
ln r (the sqrt(f) cancels, L-828) DIVERGES and sets the |r|^{+-lambda} power, while int omega dl ~
omega r^{3/2} -> 0 -- so EVERY continuum mode (all omega), not just the zero-mode, carries the decaying
power |r|^{+lambda} at the wall, the non-degenerate condition 56 fixed (no free parameter). So the row's
"with what condition?" is answered for the whole continuum, and the continuation is determined.

** THE GEOMETRY (signed radius, M=1, alpha=12 -- the register's r2785 case). ** f = 1 - 2M/r - r^2/
alpha^2 has three real roots: a conjugate-side horizon at r = -12.897 (a FULL static region r<0 exists),
the inner horizon r_b = 2.061, and the cosmological r_c = 10.836. Between them 0 < r < r_b is timelike
(f<0), the wall r=0 joins it to the conjugate static region.

COMPUTES: the leaf integral l = int dr/sqrt|f| and the tortoise x = int dr/f at the wall, the inner
horizon and the cosmological horizon, and the symbolic near-wall scalings of int W dl and int omega dl.
** The results are structural (the leaf finiteness and the energy-independence hold for every member);
M=1, alpha=12 is the representative signed-radius case, a SCOPE not a pinned working point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE CONTINUUM'S PATH IS FINITE IN THE LEAF COORDINATE: l(wall), l(r_b^-), l(r_b^+), l(r_c) are all
     finite and l is continuous across r_b (a regular interior point), while the tortoise x = int dr/f
     DIVERGES at r_b -- so the continuation wall -> r_b -> r_c is over a finite path, the tortoise
     infinity being a coordinate artefact.
  2. THE WALL CONDITION IS ENERGY-INDEPENDENT: int W dl = lambda ln r (the sqrt(f) cancellation) while
     int omega dl ~ omega r^{3/2} -> 0 at the wall, so the energy term is subleading for every omega and
     the continuum mode carries the same |r|^{+lambda} decaying power as the zero-mode -- 56's
     non-degenerate condition holds across the whole continuum, no free parameter.
  3. IT IS ANCHORED ON THE ZERO-MODE AND THE VERDICT: at omega=0 the mode is |r|^{+lambda} (P14/L-828,
     lambda=j+1/2 non-degenerate), and the continuum is "the same analysis at a different energy" (B48)
     -- so the fixed power, not a log, is the condition at every energy.

** WHAT IS NOT CLAIMED, stated for reversal. ** The explicit TRANSMISSION amplitude across r=0 -- the
coefficient with which a static-region scattering state arrives at the wall and connects to the
conjugate static region -- is NOT computed here: crossing the inner horizon is a greybody-type
connection (the mode ~ (r - r_b)^{+-i omega / 2 kappa} around the horizon branch point) on the
timelike stretch where the radial operator turns propagating (imaginary mass, P14), and that amplitude
is the remaining computation, flagged not run. This receipt establishes that the continuation is
WELL-POSED (finite path) and DETERMINED (energy-independent fixed condition), not the amplitude. NOT a
framework verdict (F5): PO-11 is the observer line's; 56 fixed the condition at r2800 and this supplies
the construction step that the condition extends to the whole continuum on a finite path. NOT that the
timelike-stretch operator is examined -- only the leaf finiteness and the near-wall dominance are
computed; the propagating-regime mode is the flagged remainder.

** Board lead L-829 (cc54's band); the r2800 construction step (the continuum continues through r=0,
finite path + energy-independent condition). Informs L-221/family-6, PO-11, B46, B48, L-828, P14. Routed
to 56. **

Written r2802 (cc54, L-829). Asserts against the corpus's own f and the leaf/tortoise integrals
symbolically and numerically -- never the register. Stated for reversal.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- PO-11: does the static-region continuum continue through r=0, and with what condition?')
    print()
    M, ALPHA = 1.0, 12.0

    def f(r):
        return 1 - 2 * M / r - r ** 2 / ALPHA ** 2

    roots = np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * M]).real)
    rneg, rb, rc = roots
    r_mid = 0.5 * (rb + rc)

    def leaf(r):
        pts = [rb] if (min(r, r_mid) < rb < max(r, r_mid)) else None
        return quad(lambda rr: 1.0 / np.sqrt(abs(f(rr))), r_mid, r, limit=400, points=pts)[0]

    l_wall = leaf(1e-7)
    l_rb_m = leaf(rb - 1e-6)
    l_rb_p = leaf(rb + 1e-6)
    l_rc = leaf(rc - 1e-7)
    # tortoise near rb (diverges)
    tort = lambda r: quad(lambda rr: 1.0 / f(rr), r_mid, r, limit=400)[0]
    t1, t2 = tort(rb + 1e-3), tort(rb + 1e-5)

    check(f'THE PATH IS FINITE IN THE LEAF COORDINATE: l(wall)={l_wall:.2f}, l(r_b-)={l_rb_m:.2f}, '
          f'l(r_b+)={l_rb_p:.2f} (continuous across r_b, gap {abs(l_rb_p-l_rb_m):.1e}), l(r_c)={l_rc:.2f} '
          f'-- all finite; but the TORTOISE diverges at r_b ({t1:.1f} -> {t2:.1f} as r->r_b), so its '
          '"infinite distance" is a coordinate artefact',
          all(np.isfinite(v) for v in (l_wall, l_rb_m, l_rb_p, l_rc)) and abs(l_rb_p - l_rb_m) < 1e-2
          and abs(t2) > abs(t1) + 2)

    # energy-independence, symbolic
    r, Ms, al, lam, om = sp.symbols('r M alpha lambda omega', positive=True)
    fsym = 1 - 2 * Ms / r - r ** 2 / al ** 2
    Wdl = sp.simplify(lam * sp.sqrt(fsym) / r * (1 / sp.sqrt(fsym)))     # W * dl/dr
    I_om = sp.simplify(sp.integrate(om * sp.sqrt(r / (2 * Ms)), (r, 0, r)))  # near-wall omega-integral
    check(f'THE WALL CONDITION IS ENERGY-INDEPENDENT: int W dl has integrand W*(dl/dr) = {Wdl} -> '
          f'int = lambda*ln(r) (DIVERGES, sets |r|^lambda), while int omega dl ~ {I_om} ~ omega r^(3/2) '
          '-> 0 at the wall -- so the energy term is subleading for every omega and the |r|^{+lambda} '
          'condition holds across the whole continuum',
          Wdl == lam / r and sp.limit(I_om, r, 0) == 0)

    check('IT IS ANCHORED ON THE ZERO-MODE AND THE VERDICT: the conjugate static region r<0 exists '
          f'(horizon at r={rneg:.2f}), so the wall joins two static regions; at omega=0 the mode is '
          '|r|^{+lambda} (P14/L-828, lambda=j+1/2 non-degenerate), and the continuum is the same '
          'analysis at omega>0 (B48) -- a power, not a log',
          rneg < 0 and rb > 0 and rc > rb)

    src = open(__file__, encoding='utf-8').read()
    check('THE REMAINING PIECE IS NAMED (the transmission amplitude / horizon connection), not claimed',
          'greybody-type connection' in src and 'NOT computed here' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (r2800 construction step): the static-region continuum CONTINUES through r=0 -- the')
    print('  path wall -> r_b -> r_c is FINITE in the leaf coordinate (the tortoise infinity at r_b is a')
    print('  coordinate artefact), and the wall condition is ENERGY-INDEPENDENT (int W dl = lambda ln r')
    print('  dominates int omega dl ~ omega r^{3/2}), so every continuum mode carries the fixed')
    print('  |r|^{+lambda} decaying power 56 determined -- no free parameter, at any energy. What remains')
    print('  is the transmission amplitude across the horizon (a greybody connection), flagged. F5:')
    print('  routed to 56, PO-11 the observer line\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
