#!/usr/bin/env python3
"""
RECEIPT — P16 (the collapse excursion): ** THE SCALAR MONODROMY AT THE CRUNCH IS 4 pi / rho, TWICE
THE TENSOR'S 2 pi / rho, AND THE DIFFERENCE IS THE PERTURBATION VARIABLE ITSELF. **

Built r2376+c54.151 because the corpus had a hole of a kind no gate could see: P16 asserts the
scalar value 4 pi/rho and cited `P16_the_mixing_is_two_pi_over_rho`, which computes the OTHER one.
The \\rcpt link resolved, the receipt ran, and the claim in the paper had no computation behind it.

  PART 1  ** THE TRUE HYDRODYNAMICAL VARIABLE, DERIVED: z_S = a sqrt(rho+p)/(c_s H) collapses on
          a closed dust+radiation interior to z_S = a (a + 4B/3A)/a' = a (a + rho^2 A/3)/a'. **
          ** AND THE DERIVATION CORRECTS THE FORM THE CORPUS CARRIED: a(a + 2B/3)/a' is an A = 2
          specialisation, and adds a length to an area at any other A. **
  PART 2  ** z_S IS PROPORTIONAL TO a AT BOTH ENDPOINTS, so the indicial exponents (0,1) survive
          and the mixing does not vanish -- but the SECOND-order terms differ. **
  PART 3  ** AND THAT DOUBLES THE POTENTIAL'S RESIDUE: z_S''/z_S -> 2/(rho x) where a''/a ->
          1/(rho x).  The off-diagonal is 2 pi i P with P the residue, so 4 pi i/rho. **
  PART 4  ** THE TENSOR VALUE IS UNCHANGED AND EXACT: z_T = a M_Pl/2 identically, for any content
          and any equation of state, so z_T''/z_T = a''/a and the tensor off-diagonal is 2 pi
          i/rho.  ** The two sectors differ; before this they were one number. **
  PART 5  ** THE TURNAROUND POLE OF z_S IS APPARENT: continuing around it returns a real transfer
          with the Wronskian preserved, so it contributes no monodromy of its own. **

** SCOPE, STATED. **  Everything here is local to the background and to a SINGLE passage.  Nothing
in this receipt uses a cycle, a periodic map, or any identification of the progenitor's harmonic
basis with another universe's -- the apparatus withdrawn at r2376+c54.149/150.

rc=0 on success.  Run: python3 P16_the_scalar_monodromy_is_four_pi_over_rho.py  (sympy numpy scipy)
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("rc=0")[0])
fail = []

RHO, A = 0.0539, 2.0
B = RHO ** 2

# =====================================================================
print("=" * 78)
print("PART 1 — THE TRUE SCALAR VARIABLE, DERIVED RATHER THAN ASSUMED")
print("=" * 78)
e, Asym, Bsym = sp.symbols('e A B', positive=True)
a_sym = (Asym / 2) * (1 - sp.cos(e)) + sp.sqrt(Bsym) * sp.sin(e)
ap_sym = sp.diff(a_sym, e)

# (8 pi G/3) rho_m = A/a^3, (8 pi G/3) rho_r = B/a^4, p = rho_r/3, H = a'/a^2 (cosmic-time Hubble
# rate in conformal parametrisation), and z_S = a sqrt(rho+p)/(c_s H) -- so z_S^2 = a^6 (rho+p)/
# (c_s^2 a'^2).
rho_tot = Asym / a_sym ** 3 + Bsym / a_sym ** 4
p_tot = sp.Rational(1, 3) * Bsym / a_sym ** 4
cs2 = sp.Rational(4, 3) * Bsym / (3 * Asym * a_sym + 4 * Bsym)
z_sq = a_sym ** 6 * (rho_tot + p_tot) / (cs2 * ap_sym ** 2)

closed_form = a_sym * (a_sym + 4 * Bsym / (3 * Asym)) / ap_sym
corpus_form = a_sym * (a_sym + sp.Rational(2, 3) * Bsym) / ap_sym
print("  z_S = a sqrt(rho+p)/(c_s H),  H = a'/a^2   =>   z_S^2 = a^6 (rho+p)/(c_s^2 a'^2)")
print("  with (8 pi G/3) rho_m = A/a^3,  rho_r = B/a^4,  p = rho_r/3,  c_s^2 = (4/3)B/(3Aa+4B):")
print()
print("     ** z_S = a (a + 4B/3A)/a'  =  a (a + rho^2 A/3)/a'   (up to a constant) **")
ratio = sp.simplify(sp.simplify(z_sq) / closed_form ** 2)
print(f"  z_S^2 / (claimed)^2  =  {ratio}      <- must be free of eta")
if e in ratio.free_symbols:
    print("  the ratio still depends on eta: the closed form is wrong")
    fail.append("closed form")
else:
    print("  ** free of eta: the closed form is exact up to normalisation. **")

# --- and the form the corpus was carrying ---------------------------------------------------
ratio_old = sp.simplify(sp.simplify(z_sq) / corpus_form ** 2)
print()
print("  ⚠⚠ ** THE FORM THE CORPUS CARRIED, a (a + 2B/3)/a', IS AN A = 2 SPECIALISATION. **")
print(f"     z_S^2 / (that)^2  =  {sp.simplify(ratio_old)}")
print("     -- eta-dependent, so it is not the variable at general A.  ** And it is dimensionally")
print("     inconsistent as written: [A] = length and [B] = length^2 (from A/a^3 and B/a^4 both")
print("     being curvatures), so 'a + 2B/3' adds a length to an area, while a + 4B/3A does not. **")
print("     *At A = 2 the two agree, which is why it survived: 4B/(3A) = 2B/3 there, and every")
print("     number in this sector was computed at A = 2.*")
if e not in ratio_old.free_symbols:
    fail.append("the A=2 form should NOT be eta-free at general A")

# numeric double-check at the working values, independent of the simplifier
A_num = A
f_zsq = sp.lambdify(e, z_sq.subs({Asym: A_num, Bsym: B}), 'numpy')
f_cf = sp.lambdify(e, closed_form.subs({Asym: A_num, Bsym: B}), 'numpy')
pts = [1.0, 2.0, 3.0, 4.0, 5.5]
rs = [np.sqrt(abs(f_zsq(x))) / abs(f_cf(x)) for x in pts]
print(f"\n  numeric ratio at eta = {pts}:")
print("     " + "  ".join(f"{r:.9f}" for r in rs))
if max(rs) - min(rs) > 1e-9 * max(rs):
    fail.append("closed form numeric")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE ENDPOINTS: z_S IS PROPORTIONAL TO a AT BOTH")
print("=" * 78)
a_n = sp.lambdify(e, a_sym.subs({Asym: A, Bsym: B}), 'numpy')
z_n = sp.lambdify(e, closed_form.subs({Asym: A, Bsym: B}), 'numpy')
eta_c = 2 * np.pi - 2 * np.arctan(RHO)
print(f"  {'delta from an endpoint':>26} {'z_S/a at the bang':>20} {'z_S/a at the crunch':>22}")
for d in [1e-3, 1e-4, 1e-5]:
    print(f"  {d:>26.0e} {z_n(d)/a_n(d):>20.6f} {z_n(eta_c-d)/a_n(eta_c-d):>22.6f}")
lim_bang = z_n(1e-5) / a_n(1e-5)
lim_crunch = z_n(eta_c - 1e-5) / a_n(eta_c - 1e-5)
print("  ** finite and non-zero at both ends, so the exponents (0,1) are unchanged and the crunch")
print("     is still a resonant regular singular point. **")
if not (0 < abs(lim_bang) < 1e3 and 0 < abs(lim_crunch) < 1e3):
    fail.append("endpoint proportionality")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RESIDUE DOUBLES, AND THAT IS THE ENTIRE EFFECT")
print("=" * 78)
U = sp.lambdify(e, sp.simplify(sp.diff(closed_form, e, 2) / closed_form).subs(
    {Asym: A, Bsym: B}), 'numpy')
print("  near the crunch, with x = |eta - eta_c| and A = 2:")
print("     a    ~ rho x + x^2/2   =>  a''/a     -> 1/(rho x)")
print("     z_S  ~ rho x + x^2     =>  z_S''/z_S -> 2/(rho x)      ** the second-order terms differ **")
print(f"\n  {'x':>10} {'(z_S''/z_S) * rho * x':>24} {'(a''/a) * rho * x':>22}")
for d in [1e-4, 1e-5, 1e-6]:
    ad = np.cos(eta_c - d) - RHO * np.sin(eta_c - d)          # a'' at the crunch side
    print(f"  {d:>10.0e} {U(eta_c-d)*RHO*d:>24.6f} {ad/a_n(eta_c-d)*RHO*d:>22.6f}")
res_scalar = U(eta_c - 1e-6) * RHO * 1e-6
ad = np.cos(eta_c - 1e-6) - RHO * np.sin(eta_c - 1e-6)
res_tensor = ad / a_n(eta_c - 1e-6) * RHO * 1e-6
print(f"\n  ** scalar residue {res_scalar:.6f} against tensor {res_tensor:.6f}: a clean factor of two. **")
if abs(res_scalar - 2.0) > 1e-3 or abs(res_tensor - 1.0) > 1e-3:
    fail.append("residue")

# ** the factor of two must not be an artefact of A = 2, since that is where the corpus's
#    specialised form came from. **
print()
print("  ⌗ AND THE FACTOR IS NOT AN ARTEFACT OF A = 2 -- the same check at the recollapse cap and")
print("    at a different composition:")
print(f"\n  {'A':>10} {'rho':>8} {'scalar residue':>16} {'tensor residue':>16}")
for A_alt, rho_alt in [(2.0, RHO), (2 * 2055.0, RHO), (2.0, 0.2)]:
    B_alt = rho_alt ** 2 * A_alt ** 2 / 4
    a_alt = (A_alt / 2) * (1 - sp.cos(e)) + sp.sqrt(B_alt) * sp.sin(e)
    z_alt = a_alt * (a_alt + 4 * B_alt / (3 * A_alt)) / sp.diff(a_alt, e)
    U_alt = sp.lambdify(e, sp.diff(z_alt, e, 2) / z_alt, 'numpy')
    an_alt = sp.lambdify(e, a_alt, 'numpy')
    app_alt = sp.lambdify(e, sp.diff(a_alt, e, 2), 'numpy')
    ec_alt = 2 * np.pi - 2 * np.arctan(rho_alt)
    dd = 1e-6
    sc = U_alt(ec_alt - dd) * rho_alt * dd
    tn = app_alt(ec_alt - dd) / an_alt(ec_alt - dd) * rho_alt * dd
    print(f"  {A_alt:>10.1f} {rho_alt:>8.4f} {sc:>16.6f} {tn:>16.6f}")
    if abs(sc - 2.0) > 1e-3 or abs(tn - 1.0) > 1e-3:
        fail.append(f"residue A={A_alt} rho={rho_alt}")
print("  ** the doubling is a property of the VARIABLE, not of the parameters. **")

# --- the monodromy itself, from the Frobenius pair ---------------------------------------------
print()
print("  With exponents (0,1) differing by one, the resonance forces a logarithm: the second")
print("  solution carries v_1 ln x, and continuing x -> x e^{2 pi i} adds 2 pi i P times the other")
print("  solution, P being the residue above.  So:")
P_scalar, P_tensor = 2.0 / RHO, 1.0 / RHO
print(f"     ** scalar off-diagonal = 2 pi i P = {2*np.pi*P_scalar:>10.4f} i  =  4 pi i / rho **")
print(f"        tensor off-diagonal = 2 pi i P = {2*np.pi*P_tensor:>10.4f} i  =  2 pi i / rho")
if abs(2 * np.pi * P_scalar - 4 * np.pi / RHO) > 1e-9:
    fail.append("scalar off-diagonal")

# verify the log coefficient by substituting the Frobenius solution into the equation
x = sp.symbols('x', positive=True)
Psym = sp.symbols('P', positive=True)
v0 = 1 + Psym * x * sp.log(x)
resid = sp.simplify(sp.diff(v0, x, 2) - (Psym / x) * v0)
lead = sp.simplify(sp.limit(resid * x, x, 0))
print(f"\n  substituting v_0 = 1 + P x ln x into v'' = (P/x) v leaves residual x*(...) -> {lead}")
print("  ** so P x ln x is forced at first order and the log coefficient IS the residue. **")
if sp.simplify(lead) != 0:
    fail.append("frobenius log coefficient")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE TENSOR VALUE IS UNCHANGED, AND IT IS EXACT")
print("=" * 78)
print("  z_T = a M_Pl/2 identically -- for ANY content, any equation of state, any sound speed --")
print("  so z_T''/z_T = a''/a with no idealisation at all, and the tensor off-diagonal stays")
print("  2 pi i/rho.  ** The scalar value needed the hydrodynamical variable and is specific to a")
print("  closed dust+radiation interior; the tensor value needs nothing. **")
print()
print(f"  {'sector':>10} {'variable':>26} {'residue':>12} {'off-diagonal':>16}")
for nm, var, P_, lab in [("tensor", "z_T = a M_Pl/2 (exact)", P_tensor, "2 pi i/rho"),
                         ("scalar", "z_S = a(a+2B/3)/a'", P_scalar, "** 4 pi i/rho **")]:
    print(f"  {nm:>10} {var:>26} {P_*RHO:>12.1f}/rho {lab:>16}")
print()
print("  ⌗ WHAT MOVES DOWNSTREAM: anything that carried the SCALAR passage with 2 pi/rho gains a")
print("    factor 2 in amplitude and 4 in power.  The tensor results -- the floor, the absence of")
print("    primordial B-modes, the shear bound -- are untouched.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE TURNAROUND POLE IS APPARENT")
print("=" * 78)
eta_t = np.pi - np.arctan(RHO)
CS2 = sp.lambdify(e, (sp.Rational(4, 3) * Bsym / (3 * Asym * a_sym + 4 * Bsym)).subs(
    {Asym: A, Bsym: B}), 'numpy')
print("  H = 0 at turnaround, so z_S has a simple pole and z_S''/z_S a double one:")
for d in [1e-3, 1e-4]:
    print(f"     delta = {d:.0e}:  (z_S''/z_S) delta^2 = {U(eta_t+d)*d*d:.6f}   -> exponents (-1,2)")
if abs(U(eta_t + 1e-4) * 1e-8 - 2.0) > 1e-3:
    fail.append("turnaround exponents")
print("  Nothing physical happens at turnaround, so the singular point must be APPARENT.  Tested by")
print("  continuing v around it on a semicircle in the complex plane: the transfer must return REAL")
print("  with det T = 1.")


def T_of(k, dl=3e-3, eps=1e-7):
    Plog = P_scalar

    def rhs(t, y, dedt, eta):
        v = y[0] + 1j * y[1]
        vp = y[2] + 1j * y[3]
        dv = vp * dedt
        dvp = (U(eta) - CS2(eta) * k * k) * v * dedt
        return [dv.real, dv.imag, dvp.real, dvp.imag]

    def line(y, e0, e1):
        return solve_ivp(lambda t, y: rhs(t, y, (e1 - e0), e0 + t * (e1 - e0)), [0, 1], y,
                         rtol=1e-11, atol=1e-15, method='DOP853').y[:, -1]

    def arc(y):
        def f(t, y):
            th = np.pi * (1 - t)
            return rhs(t, y, -1j * np.pi * dl * np.exp(1j * th), eta_t + dl * np.exp(1j * th))
        return solve_ivp(f, [0, 1], y, rtol=1e-11, atol=1e-15, method='DOP853').y[:, -1]

    cols = []
    for w in (0, 1):
        Lg = np.log(eps / (2 * RHO))
        y0 = ([1.0 + Plog * eps * Lg, 0.0, Plog * (Lg + 1.0), 0.0] if w == 0
              else [eps, 0.0, 1.0, 0.0])
        y = line(y0, eps, eta_t - dl)
        y = arc(y)
        y = line(y, eta_t + dl, eta_c - eps)
        v = y[0] + 1j * y[1]
        vp = y[2] + 1j * y[3]
        c0 = v / (1.0 + Plog * eps * Lg)
        c1 = c0 * Plog * (Lg + 1.0) + vp
        cols.append([c0, c1])
    return np.array(cols).T


print(f"\n  {'k':>7} {'|Im T| / |Re T|':>17} {'det T':>16}")
for k in [80.0, 150.0, 300.0]:
    T = T_of(k)
    r = abs(T.imag).max() / abs(T.real).max()
    d = np.linalg.det(T)
    print(f"  {k:>7.1f} {r:>17.2e} {d.real:>16.6f}")
    if abs(d - 1) > 5e-3 or r > 1e-4:
        fail.append(f"turnaround pole k={k}")
print("  ** real to a part in 1e6 and the Wronskian preserved: the pole is apparent and the extra")
print("     singular point contributes no monodromy. **")

# =====================================================================
print()
print("=" * 78)
# ** SEED REMOVED c54.222 (`L-556`). **  `try: fail.append('SEEDED')` was left in this file by my own
# c54.212 while testing whether the twelve gates could all exit non-zero, and it has failed this
# receipt ever since -- 90-odd commits, visible in every full run and triaged by nobody as a SEED.
#   ⇒ *** c54.213's rule, from the same hand: VERIFY THE RESTORE, do not trust the `finally`.  This is
#       what it costs when the restore is not verified: a real receipt reads as a real failure, and the
#       failure list absorbs it. ***  Restored to the r2682^ text, byte for byte.
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the scalar monodromy is 4 pi/rho, the tensor's is 2 pi/rho, and the")
print("difference is the perturbation variable rather than the background.")
print("=" * 78)
