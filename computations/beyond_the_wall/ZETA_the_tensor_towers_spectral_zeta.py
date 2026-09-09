#!/usr/bin/env python3
r"""ZETA_the_tensor_towers_spectral_zeta.py -- PO-23's one number, computed.

** THE QUESTION, AS THE CORPUS POSES IT. **  `P10` `sec:lock` fixes the deparametrized graviton
sector as a tower of time-dependent oscillators, one per tensor harmonic of the layer's $S^3$ --- a
countable degree-of-freedom system and NOT a field theory on a background.  So the obstruction usually
invoked for a graviton sector, the non-renormalizability of perturbative quantum gravity, has no
object here: it is a statement about counterterms for a field theory and the constraint is already
solved.  What remains is whether a divergent sum over a KNOWN DISCRETE SPECTRUM admits a definition.

`CR_synthesis` `sec:ledger` states the consequence and turns it into a prediction:

    "a divergent sum over a discrete spectrum on a compact section is fixed by its spectral zeta
     function --- which carries exactly one ambiguity, a log-scale whose coefficient is that function
     at zero.  So the claim above, read across the sector it names, makes a prediction about a
     computable number: that coefficient vanishes.  If it does not, the mode sums spend one
     dimensionless constant and the claim needs the scoping sec:frontier already applies locally."

** THE SPECTRUM IS THE CORPUS'S OWN, not this file's. **  `P10` `sec:lock`:
  * Laplace eigenvalues  $\mu_n^2 = n(n+2)-2$,  $n \ge 2$  (no zero mode, no soft region);
  * degeneracy $2(n-1)(n+3)$, ten at the floor --- derived there from Peter--Weyl on the
    parallelizable $S^3=SU(2)$, the transverse-traceless part being the two extreme summands, so the
    constant is "the propagating-component count rather than a universal";
  * frequency $\omega_n = \mu_n/a(T)$, shell contribution $2n^3$, the sum diverging quartically.

  ⌗ In $m=n+1\ge3$ this is $\mu^2=m^2-3$, $d=2(m^2-4)$ -- the standard transverse-traceless form on
    the unit three-sphere.  *Checked here rather than assumed: the corpus's Peter--Weyl derivation
    and the textbook harmonic analysis are the same numbers, which is what makes the literature's
    machinery usable on the corpus's object.*

** WHAT IS COMPUTED, AND THE ONE PLACE THE CORPUS'S OWN WORDING NEEDS CARE. **  Two spectral
quantities carry a log-scale, and they are NOT the same number:

  ⓵ $\zeta(0)$ -- the coefficient the corpus names.  It is the ambiguity of a functional
    DETERMINANT: under a rescaling of the operator, $\zeta'(0) \to \zeta'(0) + \zeta(0)\ln\lambda$.
  ⓶ $\operatorname{Res}_{s=-1}\zeta(s)$ -- the ambiguity of the zero-point SUM
    $E=\tfrac12\sum_n d_n\omega_n = \tfrac12\zeta(-1)$, which is the sum the corpus actually points
    at when it says the mode sums diverge quartically.

*Both are computed here, because the verdict should not turn on which object the sentence meant.*

Run:  python3 computations/beyond_the_wall/ZETA_the_tensor_towers_spectral_zeta.py

Written r4568 for PO-23.  Stated for reversal.
"""
import sympy as sp

M_, S_, X_ = sp.symbols('m s x', positive=True)


def spectrum():
    """(mu^2, degeneracy) in the corpus's n, and the same in m = n+1."""
    n = sp.Symbol('n', positive=True)
    mu2_n, deg_n = n * (n + 2) - 2, 2 * (n - 1) * (n + 3)
    mu2_m = sp.simplify(mu2_n.subs(n, M_ - 1))
    deg_m = sp.simplify(deg_n.subs(n, M_ - 1))
    return mu2_n, deg_n, mu2_m, deg_m


def coeffs(J=4):
    """c_j(s) in  (m^2-4)(m^2-3)^{-s/2} = m^{2-s} sum_j c_j(s) m^{-2j}."""
    f = (1 - 4 * X_) * (1 - 3 * X_) ** (-S_ / 2)
    ser = sp.expand(sp.series(f, X_, 0, J + 1).removeO())
    return [sp.simplify(ser.coeff(X_, j)) for j in range(J + 1)]


def zeta_at_zero():
    r"""zeta(0), EXACTLY -- the continuation has no remainder at s=0.

    ** The expansion TERMINATES at s=0: ** c_j(0) = 1, -4, 0, 0, ... because
    $(1-4x)(1-3x)^{0} = 1-4x$ is a polynomial.  So
        zeta(0) = 2[ (zeta_R(-2) - 1 - 2^2) - 4(zeta_R(0) - 1 - 1) ]
    is not an asymptotic estimate but a finite exact identity.  ⌗ *That is why no numerical
    continuation is needed for the headline number, and why it carries no truncation error.*
    """
    c = [sp.simplify(cj.subs(S_, 0)) for cj in coeffs()]
    tail = lambda z: sp.zeta(z) - 1 - sp.Integer(2) ** (-z)          # sum_{m>=3} m^{-z}
    val = 2 * (c[0] * tail(sp.Integer(-2)) + c[1] * tail(sp.Integer(0)))
    return sp.simplify(val), c


def residue_at_minus_one():
    r"""Res_{s=-1} zeta(s).

    A pole of zeta at s can only come from zeta_R(s+2j-2) at argument 1, i.e. s = 3-2j.  For s=-1
    that is j=2 and nothing else, so the residue is exactly 2 c_2(-1).
    """
    return sp.simplify(2 * coeffs()[2].subs(S_, -1))


def log_coefficient_from_the_summand():
    """The same number by a route with no zeta function in it: the 1/m term of d_m * mu_m."""
    asym = sp.expand(sp.series(2 * (M_ ** 2 - 4) * sp.sqrt(M_ ** 2 - 3), M_, sp.oo, 4).removeO())
    return sp.simplify(asym.coeff(M_, -1)), sp.nsimplify(asym)


def main():
    print()
    print('  THE TENSOR TOWER\'S SPECTRAL ZETA -- PO-23\'s one number')
    print('  ' + '=' * 74)
    mu2_n, deg_n, mu2_m, deg_m = spectrum()
    print(f'    corpus (P10 sec:lock):  mu_n^2 = {mu2_n}   degeneracy = {sp.factor(deg_n)}   n >= 2')
    print(f'    in m = n+1 >= 3      :  mu^2   = {mu2_m}   degeneracy = {sp.factor(deg_m)}')
    print(f'    floor  m=3           :  mu^2 = {mu2_m.subs(M_, 3)}   degeneracy = {deg_m.subs(M_, 3)}'
          '   (the corpus\'s "ten at the floor")')
    print(f'    structural relation  :  d = 2(mu^2 - 1)  ->  '
          f'{sp.simplify(deg_m - 2 * (mu2_m - 1)) == 0}')
    print()

    z0, c = zeta_at_zero()
    print('  ⓵ zeta(0) -- the coefficient the corpus names')
    print(f'      c_j(0) = {[sp.simplify(cj.subs(S_, 0)) for cj in coeffs()]}'
          '   -> the expansion TERMINATES, so this is exact')
    print(f'      zeta(0) = 2[(zeta_R(-2) - 5) - 4(zeta_R(0) - 2)]'
          f' = 2[(0 - 5) - 4(-1/2 - 2)] = {z0}')
    print()

    r1 = residue_at_minus_one()
    lg, asym = log_coefficient_from_the_summand()
    print('  ⓶ Res_{s=-1} zeta(s) -- the coefficient of the zero-point SUM\'s log-scale')
    print(f'      only j=2 can pole at s=-1, so Res = 2 c_2(-1) = {r1}')
    print(f'      independent route, large-m expansion of d*mu:  {asym}')
    print(f'      the 1/m coefficient is {lg}  -- the SAME number, with no zeta function in it')
    print()

    print('  ' + '=' * 74)
    print(f'    *** zeta(0) = {z0}, NOT ZERO.   Res_{{s=-1}} = {r1}, NOT ZERO. ***')
    print('    On either reading of which spectral quantity carries the log-scale, the free static')
    print('    tower spends one dimensionless constant.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
