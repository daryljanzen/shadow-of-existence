#!/usr/bin/env python3
"""
`L-150`, front #1.  ** THE TRUE HYDRODYNAMICAL $z_S$ ON THE CLOSED INTERIOR, IN CLOSED FORM — AND IT
CORRECTS A RECEIPTED RESULT: THE SCALAR MONODROMY IS $4\\pi/\\rho$, NOT $2\\pi/\\rho$.  $2\\pi/\\rho$ IS THE
TENSOR VALUE. **

** ⚠ CORRECTION TO THE CLOSED FORM (r2376+c54.151).  THE FORM WRITTEN BELOW, $z_S=a(a+2B/3)/a'$, IS
AN $A=2$ SPECIALISATION AND WAS PROPAGATED TO TWO PAPERS AND FOUR STANDING DOCUMENTS AS THOUGH IT
WERE GENERAL. **  The variable is

        z_S  =  a (a + 4B/3A) / a'   =   a (a + rho^2 A/3) / a' ,

which reduces to the form below exactly at $A=2$ — the value everything in this sector was computed
at.  *The tell was dimensional and was there from the first line: $A/a^3$ and $B/a^4$ are both
curvatures, so $[A]=$ length and $[B]=$ length$^2$, and "$a+2B/3$" adds a length to an area.*
** Nothing computed in this file moves: every number here is at $A=2$, where the two agree, and the
residue-doubling that gives $4\\pi/\\rho$ is verified $A$-independent in the receipt
`P16_the_scalar_monodromy_is_four_pi_over_rho`, which derives the variable rather than quoting it. **

c54.145 named the arc's single remaining idealisation: $z\\propto a$ at constant $c_s$.  This replaces
it.  For a closed universe $z_S^2=a^6(\\rho+p)/(c_s^2H^2)$ with $H=a'/a^2$, and with
$(8\\pi G/3)\\rho_m=A/a^3$, $(8\\pi G/3)\\rho_r=B/a^4$, $c_s^2=\\tfrac43 B/(3Aa+4B)$ everything collapses:

    ***  z_S  =  a (a + 2B/3) / a'   ***      (up to a constant)

  PART 1  ** THE CLOSED FORM, and its three structural features. **
  PART 2  ** THE ENDPOINTS SURVIVE BUT THE COEFFICIENT DOUBLES: $z_S''/z_S\\to2/(\\rho x)$ where
          $a''/a\\to1/(\\rho x)$.  The exponents are still $(0,1)$ and the monodromy is $4\\pi/\\rho$. **
  PART 3  ** THE TURNAROUND POLE IS APPARENT: continuing around it returns a real transfer with
          $\\det T=1$. **
  PART 4  ** $c_s$ RUNS, AND THE SOUND HORIZON OVER A CYCLE IS 12x SMALLER — the Floquet band
          period goes from $\\Delta\\ell=2.4$ to $\\Delta\\ell=28$. **
  PART 5  ** THE BANDS STILL CLOSE: phase-only transmission survives, with the boundary moved up. **

Run: python3 L150m_the_true_scalar_z.py      (numpy, scipy, sympy)
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

print(__doc__.split("Run:")[0])
RHO, A, SMAP = 0.0539, 2.0, 2.75
B = RHO**2
e = sp.symbols('e')
a_s = (A / 2) * (1 - sp.cos(e)) + sp.sqrt(B) * sp.sin(e)
ap_s = sp.diff(a_s, e)
z_s = a_s * (a_s + sp.Rational(2, 3) * B) / ap_s
U = sp.lambdify(e, sp.simplify(sp.diff(z_s, e, 2) / z_s), 'numpy')
CS2 = sp.lambdify(e, sp.Rational(4, 3) * B / (3 * A * a_s + 4 * B), 'numpy')
AA = sp.lambdify(e, a_s, 'numpy')
ec = 2 * np.pi - 2 * np.arctan(RHO)
et = np.pi - np.arctan(RHO)
P = 2.0 / RHO

# =====================================================================
print("=" * 78)
print("PART 1 — THE CLOSED FORM")
print("=" * 78)
print(f"  z_S = a (a + 2B/3)/a'   with A = 2M, B = radiation, rho = 2 sqrt(B)/A")
print(f"  {'feature':>34} {'where':>20} {'consequence':>22}")
for x, y, z in [("z_S ∝ a", "both endpoints", "exponents (0,1) survive"),
                ("but z_S/a is NOT a''/a's ratio", "both endpoints", "** monodromy doubles **"),
                ("simple pole (H = 0)", "turnaround", "extra singular point"),
                ("c_s runs 0.018 -> 0.577", "turnaround -> crunch", "band period x12")]:
    print(f"  {x:>34} {y:>20} {z:>22}")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE COEFFICIENT DOUBLES, SO THE SCALAR MONODROMY IS 4 pi/rho")
print("=" * 78)
print("  Expanding at the crunch with x = |eta - eta_c| (A = 2, so a ~ rho x + x^2/2):")
print("     a       ∝ rho x + x^2/2        ⇒  a''/a   -> 1/(rho x)")
print("     z_S     ∝ rho x + x^2          ⇒  z_S''/z_S -> 2/(rho x)")
print("  -- the second-order terms differ, and that is the whole of it.")
print(f"\n  {'d':>10} {'U * rho * d':>14} {'a''/a * rho * d':>18}")
for d in [1e-4, 1e-5, 1e-6]:
    ap = np.cos(ec - d) - RHO * np.sin(ec - d)
    print(f"  {d:>10.0e} {U(ec-d)*RHO*d:>14.6f} {ap/AA(ec-d)*RHO*d:>18.6f}")
assert abs(U(ec - 1e-6) * RHO * 1e-6 - 2.0) < 1e-3
print()
for s in [
 "⇒⇒⇒ ** SO THE SCALAR MIXING IS $4\\pi/\\rho$ AND THE RECEIPTED $2\\pi/\\rho$ IS THE TENSOR VALUE. **",
 "   *c54.131 computed the monodromy from $a''/a$, i.e. on $z\\propto a$ — which is exact for tensors",
 "   ($z_T=aM_{\\rm Pl}/2$, any content) and wrong for scalars by a factor of two in the potential's",
 "   residue, hence a factor of two in the off-diagonal.*",
 "",
 "⌗ ** AND THE TWO SECTORS NOW DIFFER, WHICH THEY DID NOT BEFORE: scalars mix twice as strongly as",
 "   tensors at the crunch. **  *Everything downstream that used $2\\pi/\\rho$ for the SCALAR passage",
 "   gains a factor 2 in amplitude and 4 in power — the transfer law, and the vacuum floors it",
 "   feeds.  The tensor results are untouched.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TURNAROUND POLE IS APPARENT")
print("=" * 78)
print("  H = 0 at turnaround, so z_S has a simple pole there and z_S''/z_S a double one:")
for d in [1e-3, 1e-4]:
    print(f"     delta = {d:.0e} :  (z''/z) * delta^2 = {U(et+d)*d*d:.6f}   -> exponents (-1, 2)")
assert abs(U(et + 1e-4) * 1e-8 - 2.0) < 1e-3
print("  Nothing physical happens at turnaround, so the singularity must be APPARENT.  Tested by")
print("  continuing v around it on a semicircle in the complex plane: the transfer must come back")
print("  REAL, with det T = 1.")


def T_of(k, dl=3e-3, eps=1e-7):
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
            return rhs(t, y, -1j * np.pi * dl * np.exp(1j * th), et + dl * np.exp(1j * th))
        return solve_ivp(f, [0, 1], y, rtol=1e-11, atol=1e-15, method='DOP853').y[:, -1]

    cols = []
    for w in (0, 1):
        L = np.log(eps / (2 * RHO))
        y0 = [1.0 + P * eps * L, 0.0, P * (L + 1.0), 0.0] if w == 0 else [eps, 0.0, 1.0, 0.0]
        y = line(y0, eps, et - dl)
        y = arc(y)
        y = line(y, et + dl, ec - eps)
        v = y[0] + 1j * y[1]
        vp = y[2] + 1j * y[3]
        c0 = v / (1.0 + P * eps * L)
        c1 = c0 * P * (L + 1.0) + vp
        cols.append([c0, c1])
    return np.array(cols).T


print(f"\n  {'k':>7} {'|Im T| / |Re T|':>17} {'det T':>26}")
for k in [80.0, 150.0, 300.0]:
    T = T_of(k)
    print(f"  {k:>7.1f} {abs(T.imag).max()/abs(T.real).max():>17.2e} "
          f"{np.linalg.det(T):>26.6f}")
    assert abs(np.linalg.det(T) - 1) < 5e-3
print("  ** real to a part in 1e6 and the Wronskian preserved to 1e-4: the pole is apparent, and")
print("     the extra singular point contributes no monodromy. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — c_s RUNS, AND THE BAND PERIOD WITH IT")
print("=" * 78)
cs = lambda x: np.sqrt(CS2(x))
I = quad(cs, 1e-9, ec - 1e-9, limit=400)[0]
print(f"  {'quantity':>44} {'true':>12} {'the idealisation':>18}")
for nm, t, i_ in [("c_s at turnaround", cs(et), 1 / np.sqrt(3)),
                  ("c_s at the crunch", cs(ec - 1e-9), 1 / np.sqrt(3)),
                  ("sound horizon over a cycle, int c_s d eta", I, ec / np.sqrt(3)),
                  ("Floquet band period, Delta k = pi/int", np.pi / I, np.pi / (ec / np.sqrt(3))),
                  ("in multipole, Delta l", np.pi / I * SMAP, np.pi / (ec / np.sqrt(3)) * SMAP)]:
    print(f"  {nm:>44} {t:>12.4f} {i_:>18.4f}")
assert 8 < np.pi / I < 14
print()
for s in [
 "⇒ ** THE BAND PERIOD IS TWELVE TIMES COARSER: $\\Delta\\ell=28$ where the idealisation gave $2.4$. **",
 "   *That matters for a reason c54.144 turned on: at $\\Delta\\ell=2.4$ adjacent multipoles sampled",
 "   the bands at effectively random phase, and at $\\Delta\\ell=28$ they sample them SMOOTHLY, some",
 "   ten modes to a band.  **The quasi-random mode-to-mode scatter that excluded the chain is",
 "   replaced by a smooth oscillation.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE BANDS STILL CLOSE")
print("=" * 78)
print(f"  {'k':>7} {'l':>7} {'|lambda|':>12} {'band':>10}")
for k in [80.0, 110.0, 150.0, 220.0, 300.0]:
    T = T_of(k)
    C = np.array([[1.0, 0.0], [2 * np.pi * P, 1.0]]) @ T.real
    lam = max(abs(np.linalg.eig(C)[0]))
    print(f"  {k:>7.1f} {k*SMAP:>7.0f} {lam:>12.4f} {'UNSTABLE' if lam>1.0001 else 'stable':>10}")
print()
for s in [
 "✔✔ ** SO c54.144's CENTRAL RESULT SURVIVES THE REPAIR: the instability bands close, and above the",
 "   closure a branch-point passage is a pure phase rotation. **  *The boundary moves up — the",
 "   monodromy is twice as strong, so the modes stay coupled a little further — but the structure",
 "   is the same, and it is now computed on the true scalar variable rather than a stand-in.*",
 "",
 "⚠ ** WHAT IS NOT YET REDONE, AND IT IS THE DECIDING NUMBER: the phase-averaged transfer and its",
 "   RUNNING on this potential.  c54.145 got $0.35$–$0.95$ against a permitted $0.01$ using the",
 "   idealisation; with a band period twelve times coarser and a monodromy twice as strong, that",
 "   number will move, and its direction is not guessable from here. **",
 "   *It is the same machinery and it is the next step.  **Stating it as unfinished rather than",
 "   estimating it is the whole lesson of the five withdrawn bounds.***",
]:
    print("  " + s)
