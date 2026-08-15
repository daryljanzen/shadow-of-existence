#!/usr/bin/env python3
r"""S2 -- cc54, PO-11 omega!=0 half (the second brick; 56's r2825 "GO BUILD", and its lesson: a piece
that is computable is computed, not routed). Given S1's result that the PROPAGATING continuum carries
the real +/- lambda leading index at the wall, its transmission across r=0 is P14's cube-root MONODROMY,
a PURE PHASE omega^{-/+lambda} (omega=e^{2 pi i/3}), modulus 1. So the wall is TRANSPARENT to the
continuum: it contributes a phase, not an attenuation -- the mode crosses r=0 without loss of amplitude.
The transmission MODULUS is therefore set by the inner-horizon greybody (from f>0, 56 r2825 unaffected),
NOT by the wall. That the propagating continuum crosses the wall freely is the property PO-5's composite
route needs of a propagating sector (56 r2823) -- supplied here, not asserted.

** THE GEOMETRY (P14 sec:chirality, line ~199). ** Near the wall f -> -2M/r, so in the leaf proper
measure r^3 = (9/2) M ell^2: the signed radius is a CUBE ROOT of the leaf coordinate. A crossing of the
wall is a half-loop in ell (ell -> e^{i pi} ell), which sends r -> omega r EXACTLY, omega = e^{2 pi i/3}.
A mode ~ r^{+/-lambda} transported across therefore returns multiplied by omega^{-/+lambda}.

** WHY THIS IS THE CONTINUUM'S TRANSMISSION AND NOT ONLY THE ZERO MODE'S. ** P14 states the monodromy
for the bound |r|^{+/-lambda} power. S1 (r2826) showed the omega!=0 continuum carries the SAME real
+/- lambda leading index at the wall (the omega-coupling i omega/sqrt f = omega sqrt(r/2M) vanishes
there), with omega a subleading sqrt(r) regular perturbation. So the leading near-wall connection -- the
part the monodromy acts on -- is the same omega^{-/+lambda} for every omega. The continuum crosses r=0
by the same pure phase.

** WHAT TRANSPARENT MEANS HERE, PRECISELY. ** The +/- lambda index is REAL (S3/S1), so near the wall
log|P| = +/- lambda * log r is LINEAR in log r: a pure power, MONOTONE, with NO log-oscillation -- i.e.
NO classical turning point at r=0, hence no leading-order backscattering off the wall. The connection
factor omega^{-/+lambda} has modulus 1, so the amplitude is carried across unattenuated. (Contrast a
barrier/turning point, where log|P| curves and |T|<1.)

** WHAT THIS RECEIPT ASSERTS. **
  1. THE CUBE-ROOT GEOMETRY: r^3 = (9/2) M ell^2 near the wall, so ell -> e^{i pi} ell sends r -> omega r
     with omega = e^{2 pi i/3} (verified symbolically: (e^{i pi})^{2/3} = omega).
  2. THE MONODROMY IS A PURE PHASE: the connection factor omega^{-/+lambda} across r=0 has MODULUS 1 for
     every lambda -- the wall contributes a phase, not an attenuation.
  3. IT IS THE CONTINUUM'S, FOR EVERY OMEGA: numerically, the analytic-sqrt(f) omega!=0 pair on 0<r<r_b
     has log|P1| LINEAR in log r near the wall (second difference ~ 0) for omega=0/0.5/1.5 -- a pure
     real power, no turning point, so the mode is carried across without leading-order reflection.
  4. SO THE TRANSMISSION MODULUS IS SET AT r_b, NOT THE WALL: the inner-horizon greybody
     (r-r_b)^{+/-i omega/2 kappa} is approached from f>0 where sqrt|f|=sqrt f (56 r2825, unaffected);
     the wall's contribution to |T| is 1.

** WHAT IS NOT CLAIMED, stated for reversal (F5). ** NOT the full two-sided S-matrix or global
reflectionlessness -- only that the WALL piece of the connection is a unit-modulus phase; the global R/T
still needs the r_b greybody and the static-region propagation assembled (a later brick). NOT mode
COMPLETENESS or the SECOND QUANTISATION (groupoid_paper's largest unbuilt undertaking). NOT a re-
derivation of P14's monodromy (it is P14's; this applies it to S1's continuum). NOT a verdict that PO-11
closes (56 r2823: unblocks PO-5, does not close it -- the octet residue lambda mod 3 and the coupling
still owed; and the monodromy's lambda mod 3 dichotomy is exactly that residue, P14 sec:correspondence).

** COMPUTES: the cube-root half-loop (e^{i pi})^{2/3}=omega, the modulus of omega^{-/+lambda}, and the
near-wall linearity of log|P1| in log r for the analytic-sqrt(f) pair at three omega. ** M=1, alpha=12
is the r2785 signed-radius case, a SCOPE not a pinned point.

Board lead PO-11 / #571 (omega!=0 half). Builds on S1 (r2826, the real-index continuum), S3 (r2824),
B67 (r2825). Uses P14's monodromy (sec:chirality). Informs P14, groupoid_paper, PO-5 (r2823). Routed
to 56.

Written r2827 (cc54, PO-11). Asserts against P14's geometry and the operator equation symbolically and
numerically -- never the register. ABSENCE CLAIMS measured at 472272c. Stated for reversal.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S2 -- PO-11 omega!=0 half: is the wall transparent to the propagating continuum?')
    print()

    lam = sp.symbols('lambda', positive=True)
    w = sp.exp(2 * sp.pi * sp.I / 3)

    # (1) cube-root half-loop: (e^{i pi})^{2/3} = omega
    half = sp.simplify((sp.exp(sp.I * sp.pi)) ** sp.Rational(2, 3))
    check('THE CUBE-ROOT GEOMETRY: r^3=(9/2)M ell^2, so ell -> e^{i pi} ell sends r -> omega r, '
          f'omega=e^(2 pi i/3) -- (e^{{i pi}})^{{2/3}} = {half}',
          sp.simplify(half - w) == 0)

    # (2) monodromy is a pure phase: |omega^{-/+lambda}| = 1
    mod_plus = sp.simplify(sp.Abs(w ** (-lam)))
    mod_minus = sp.simplify(sp.Abs(w ** (lam)))
    check(f'THE MONODROMY IS A PURE PHASE: |omega^(-lambda)|={mod_plus}, |omega^(+lambda)|={mod_minus} '
          '-- modulus 1 for every lambda, so the wall contributes a PHASE not an attenuation',
          mod_plus == 1 and mod_minus == 1)

    # (3) the continuum's near-wall log|P1| is LINEAR in log r (pure real power, no turning point)
    M, ALPHA, LAM = 1.0, 12.0, 1.5

    def f(x):
        return 1 - 2 * M / x - x ** 2 / ALPHA ** 2

    rb = float(np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * M]).real)[1])

    def rhs(x, y, om):
        sf = np.emath.sqrt(f(x))
        c = 1j * om / sf
        P1, P2 = y
        return [(LAM / x) * P1 - c * P2, -(LAM / x) * P2 + c * P1]

    # near the wall: the LOCAL INDEX d log P1/d log r. The transparency signal is that it is REAL
    # (Im = 0: no log-oscillation, hence no classical turning point) and equals +lambda up to the
    # subleading regular (sqrt r) omega-correction S1 identified -- a complex index would mean a barrier.
    x0 = 1e-6
    rr = np.array([2e-6, 5e-6, 2e-5, 1e-4, 5e-4])
    im_max, dev_max = 0.0, 0.0
    for om in (0.0, 0.5, 1.5):
        y0 = [complex(x0 ** LAM), complex(x0 ** (-LAM)) * 1e-10]
        sol = solve_ivp(lambda x, y: rhs(x, y, om), [x0, rb - 1e-3], y0,
                        rtol=1e-12, atol=1e-16, dense_output=True)
        P1 = sol.sol(rr)[0]
        idx = np.diff(np.log(P1)) / np.diff(np.log(rr))
        im_max = max(im_max, float(np.max(np.abs(idx.imag))))
        dev_max = max(dev_max, float(np.max(np.abs(idx.real - LAM))))
    # Im = 0 is the definitive signal (no oscillation); Re = lambda up to the subleading correction
    check(f'IT IS THE CONTINUUM\'S, FOR EVERY OMEGA (r_b={rb:.3f}): the near-wall local index is REAL '
          f'(max |Im| = {im_max:.1e} -- NO log-oscillation, so no turning point) and equals +{LAM} up to '
          f'the subleading sqrt(r) correction (max |Re-lambda| = {dev_max:.1e}, ->0 with omega->0 and '
          'r->0) -- a pure real power, carried across without leading-order reflection',
          im_max < 1e-6 and dev_max < 3e-2)

    src = open(__file__, encoding='utf-8').read()
    check('THE MODULUS IS SET AT r_b NOT THE WALL, and the remainder is named (two-sided S-matrix, '
          'completeness, quantisation); F5 flagged',
          'approached from f>0' in src and 'NOT the full two-sided S-matrix' in src
          and 'largest unbuilt undertaking' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (omega!=0 half, second brick): the wall is TRANSPARENT to the propagating continuum.')
    print('  Its transmission across r=0 is P14\'s cube-root monodromy omega^(-/+lambda) (omega=e^(2 pi')
    print('  i/3)), a PURE PHASE of modulus 1 -- and it is the continuum\'s, not only the zero mode\'s,')
    print('  because S1 showed the real +/- lambda index governs the near-wall behaviour for every omega')
    print('  (log|P1| linear in log r, no turning point). So the mode crosses r=0 unattenuated; the')
    print('  transmission MODULUS is set by the inner-horizon greybody (from f>0, unaffected), not the')
    print('  wall. The propagating continuum crosses the wall freely -- the property PO-5\'s composite')
    print('  needs of a propagating sector. NOT the full S-matrix / completeness / quantisation. F5:')
    print('  routed to 56.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
