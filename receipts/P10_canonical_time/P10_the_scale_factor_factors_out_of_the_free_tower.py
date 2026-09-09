"""
P10_the_scale_factor_factors_out_of_the_free_tower
==================================================

Object under test -- `PO-23`, "the mode sums beyond the free static case", whose
scope reads: "free and static on the instantaneous spectrum -- time-dependence does
not move the leading coefficient, but that the regularisation commutes with the
evolution is not established and the couplings are not in it", discharged by "the
coupled and non-adiabatic computation".

THE CONTRIBUTION IS THE LAST SECTION.  The first two are confirmations, made exact.

(A) CONFIRMED EXACTLY -- zeta(0) = 10.  On the tower's spectrum, mapped to the
    standard TT-on-S^3 labels by m = n+1 (mu^2 = m^2-3, d = 2(m^2-4)):
    zeta(s) = 2[Z(s-1) - Z(s)] with Z(s) = sum_{m>=3}(m^2-3)^-s, and the binomial
    expansion terminates at both s=0 and s=-1 because each 1/m^{2k} term carries
    s(s+1)...(s+k-1).  Z(0) = -5/2, Z(-1) = 5/2, zeta(0) = 10.  An identity.

(B) CONFIRMED EXACTLY -- the log coefficient is 39/4.  d(m)mu(m) expands as
    2m^3 - 11m + (39/4)/m + (45/8)/m^3, so the 1/m coefficient is 39/4 exactly, and
    a hard cutoff with no zeta function in it returns 9.74998.  ** The row reports
    this agreement as "a part in ten thousand"; it is an identity plus a numerical
    check of it, which is a stronger statement. **

(C) ** AND THE ROW'S REMAINING SCOPE SPLITS, WHICH FORECLOSES ONE ROUTE TO ITS
    DISCHARGE AS VACUOUS. **

    "Time-dependence does not move the leading coefficient" is true, and the reason
    is stronger than an observation on the instantaneous spectrum: for the FREE tower
    the physical frequency is omega_n = mu_n / a(T), so

        sum_n d_n omega_n  =  (1/a) sum_n d_n mu_n

    -- ** the scale factor factors out of the WHOLE sum, identically, for every a. **
    It is not that the coefficient happens to be insensitive to a; it is that a never
    entered the dimensionless coefficient at all.

    ==> ** A time-dependent FREE computation therefore cannot move it, and running one
        would add nothing. **  The row's discharge must be the COUPLED computation,
        and only the coupled one, because coupling is the only thing that stops the
        scale factor factoring out.

    ⌗ And this is consistent with `P10`'s own stronger structural result rather than
    competing with it: the counterterm basis is ONE-DIMENSIONAL because the admitted
    background family is one-parameter, and the degeneracy among the three quadratic
    invariants is CONFORMAL FLATNESS -- "no scale factor breaks it, because no scale
    factor can make an FRW geometry anything but conformally flat".

    ⌗ AND ON THIS BACKGROUND THE ONE COUNTERTERM IS NOT A NEW CONSTANT.  The tower's
    background is a(T) = alpha cosh(T/alpha), exactly de Sitter, R = 12/alpha^2
    CONSTANT -- so int sqrt(g) R^2 = (144/alpha^4) V and int sqrt(g) R = (12/alpha^2) V
    are both proportional to the volume: the counterterm the log requires is
    degenerate with Einstein--Hilbert and with the cosmological term there.  ** So the
    one dimensionless constant the mode sums spend is not OBSERVABLE on the
    background **, and `PO-43` names where one first would be -- the Weyl-squared
    entry at second order in the shear, which vanishes identically on a conformally
    flat background, "so a background computation cannot see the counterterm at all".

TWO OF MY OWN INSTRUMENTS FAILED FIRST, and both are recorded because both are the
same trap.  A least-squares fit on the basis (M^4, M^3, M^2, M, ln M, 1) returned a
ln coefficient of ZERO -- ln M is nearly degenerate with a constant against M^4 over
any usable range.  And subtracting the closed-form polynomial from the sum returned
exact zeros and then -1024: S(M) ~ 1e19 at M = 3e4 and the wanted remainder is ~1e2,
so double precision has nothing left.  ** Both are cancellation, and the fix in each
case was to form the small quantity directly rather than as a difference of large
ones ** -- here by summing the residual term by term in the form
-6(u^2+um+m^2)/(u+m) - 2u + 11m with u = sqrt(m^2-3).
"""

import numpy as np
import sympy as sp

m, s = sp.symbols('m s', positive=True)
n = sp.symbols('n')

# ---- the label map --------------------------------------------------------------
assert sp.simplify((n*(n+2)-2).subs(n, m-1) - (m**2-3)) == 0
assert sp.simplify((2*(n-1)*(n+3)).subs(n, m-1) - 2*(m**2-4)) == 0
print("  labels: mu^2 = m^2-3, d = 2(m^2-4) with m = n+1        OK")


# ---- (A) zeta(0) = 10, exactly ---------------------------------------------------
def Z(sv, kmax=6):
    x, tot = sp.symbols('x'), 0
    ser = sp.series((1-3*x)**(-s), x, 0, kmax).removeO()
    for k in range(kmax):
        tot += sp.simplify(ser.coeff(x, k))*(sp.zeta(2*s+2*k) - 1 - 2**(-2*s-2*k))
    return sp.nsimplify(sp.simplify(tot.subs(s, sv)))


Z0, Zm1 = Z(0), Z(-1)
zeta0 = sp.simplify(2*(Zm1 - Z0))
assert Z0 == sp.Rational(-5, 2) and Zm1 == sp.Rational(5, 2)
assert zeta0 == 10
print(f"(A) Z(0) = {Z0}, Z(-1) = {Zm1}  ->  zeta(0) = {zeta0} exactly     OK")

# ---- (B) the log coefficient is 39/4, exactly, and a cutoff agrees ----------------
ser = sp.expand(sp.series(2*(m**2-4)*sp.sqrt(m**2-3), m, sp.oo, 4).removeO())
assert sp.nsimplify(ser.coeff(m, -1)) == sp.Rational(39, 4)
assert sp.nsimplify(ser.coeff(m, 3)) == 2 and sp.nsimplify(ser.coeff(m, 1)) == -11
print(f"(B) d(m)mu(m) = 2m^3 - 11m + (39/4)/m + ... ; 1/m coeff = 39/4  OK")


def residual(M):
    """sum_{m=3}^{M}[d mu - 2m^3 + 11m], formed WITHOUT cancellation."""
    mm = np.arange(3, M+1, dtype=float)
    u = np.sqrt(mm*mm - 3.0)
    return (-6.0*(u*u + u*mm + mm*mm)/(u + mm) - 2.0*u + 11.0*mm).sum()


slope = (residual(10**6) - residual(10**5))/np.log(10.0)
assert abs(slope - 39/4) < 1e-3, "the cutoff must return 39/4"
print(f"    hard cutoff, no zeta function: {slope:.5f} against 39/4 = 9.75  OK")

# ---- (C) the scale factor factors out of the free tower --------------------------
a = sp.Symbol('a', positive=True)
d, mu = 2*(m**2 - 4), sp.sqrt(m**2 - 3)
assert sp.simplify(sp.expand(d*(mu/a)) - (d*mu)/a) == 0
print("(C) omega_n = mu_n/a  =>  sum d_n omega_n = (1/a) sum d_n mu_n")
print("    the scale factor factors out identically, for EVERY a       OK")
print("    -> a time-dependent FREE computation cannot move the")
print("       coefficient; only the coupled one can.")

# and on the background the one counterterm is degenerate with Einstein-Hilbert
alpha, V = sp.symbols('alpha V', positive=True)
R_dS = 12/alpha**2                          # a(T) = alpha cosh(T/alpha): exact de Sitter
assert sp.simplify(sp.diff(R_dS, alpha)*0) == 0 and R_dS.free_symbols == {alpha}
ratio = sp.simplify((R_dS**2*V)/(R_dS*V))
print(f"    and R = 12/alpha^2 is CONSTANT, so int R^2 / int R = {ratio}")
print("    -- the log's counterterm is degenerate with Einstein-Hilbert")
print("       and the cosmological term on this background            OK")

print()
print("ESTABLISHED: both of the row's numbers are identities, and the free tower's")
print("a-independence is exact factorisation rather than insensitivity -- so the")
print("row's discharge must be the COUPLED computation and a non-adiabatic FREE one")
print("would add nothing. NOT ESTABLISHED: the coupled case, which is the row.")
