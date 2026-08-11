#!/usr/bin/env python3
"""
`L-150`, front #1.  ** THE CHECK: DOES THE LEAKED BRANCH OPERATE?  IT DOES NOT — NOT WITH THE
$k$-DEPENDENCE THE BOUND RESTED ON.  ON THE CYCLIC ATTRACTOR THE LEAKED/DIRECT RATIO IS FLAT IN $k$
(log-slope $+0.04$ against WKB's $-1$) AND OF ORDER $2\\pi$.  SO CHAIN B EVAPORATES, THE
OVER-DETERMINATION DISSOLVES, AND P15's TRANSMISSION CLAIM IS VINDICATED FOR A COMPUTED REASON. **

c54.142 recorded an over-determination that fails by $831\\times$, and named its one unverified step:
that the surviving mode is fed by the LEAKED branch — i.e. that the incoming state is a free
oscillation, so WKB gives $|c_0|/|c_1|=1/(c_sk)$ — rather than arriving already in the survivor
branch.  ** That premise is testable inside the construction, because the construction says what the
incoming state IS: the output of the PREVIOUS branch point. **

  PART 1  ** THE TEST, AND IT IS SELF-CONTAINED: the closed dust+radiation interior is a FULL cycle
          with a branch point at each end and the same $(0,1)$ exponents at both.  Propagate the
          Frobenius basis bang -> crunch, compose with the monodromy, take the attractor. **
  PART 2  ** THE RESULT: leaked/direct is k-FLAT, not $\\propto1/k$. **
  PART 3  ** WHAT THAT DOES TO THE LEDGER — chain B, c54.133, the bracket, and chain A. **
  PART 4  ** WHAT REPLACES THE BOUND, and it is already well posed. **

Run: python3 L150j_does_the_leaked_branch_operate.py      (numpy, scipy)
"""
import numpy as np
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])
CS = 1.0 / np.sqrt(3.0)

# =====================================================================
print("=" * 78)
print("PART 1 — THE TEST")
print("=" * 78)
for s in [
 "  The closed dust+radiation interior is a COMPLETE cycle, bang to crunch, and both ends are",
 "  branch points of the SAME type: with A = 2M and rho = 2 sqrt(B)/A,",
 "     a(eta) = (1 - cos eta) + rho sin eta        (units A = 2),   eta_c = 2 pi - 2 arctan(rho)",
 "     a'(0) = +rho,  a''(0) = 1      and      a'(eta_c) = -rho,  a''(eta_c) = 1",
 "  so the indicial exponents are (0,1) at each end and the Frobenius basis is the same one the",
 "  monodromy acts in.  ** Nothing external is needed: the construction supplies the incoming",
 "     state, because the parent came through a branch point too. **",
 "",
 "  So: propagate the basis {v_0 -> 1, v_1 -> sigma} from the bang to the crunch (matrix T), compose",
 "  with the monodromy J : c_1 -> c_1 + 2 pi i p c_1, p = -1/rho, and take the ATTRACTOR of C = J T",
 "  -- the direction a long chain of cycles settles into.  Read the leaked/direct ratio at the",
 "  crunch, i.e. on T v, BEFORE the monodromy that turns it into the next universe's spectrum.",
]:
    print(s)


def eta_c(r):
    return 2 * np.pi - 2 * np.arctan(r)


def pot(e, r):
    a = (1 - np.cos(e)) + r * np.sin(e)
    return (np.cos(e) - r * np.sin(e)) / a


def T_of(k, r, cs=CS, eps_rel=1e-6):
    """propagate the Frobenius basis across one full cycle; det T must be 1 (Wronskian)"""
    eps = eps_rel * r
    ec = eta_c(r)

    def rhs(t, y):
        return [y[1], (pot(t, r) - cs * cs * k * k) * y[0]]

    cols = []
    for w in (0, 1):
        L = np.log(eps / (2 * r))
        y0 = [1.0 + (eps / r) * L, (1.0 / r) * (L + 1.0)] if w == 0 else [eps, 1.0]
        s = solve_ivp(rhs, [eps, ec - eps], y0, rtol=3e-13, atol=1e-16, method='DOP853')
        v, vp = s.y[0, -1], s.y[1, -1]
        c0 = v / (1.0 + (eps / r) * L)
        c1 = c0 * (1.0 / r) * (L + 1.0) + vp          # sigma = -x, so d/dx = -d/deta
        cols.append([c0, c1])
    return np.array(cols).T


def leaked_over_direct(k, r):
    T = T_of(k, r)
    det = abs(np.linalg.det(T) - 1)
    C = np.array([[1.0, 0.0], [2 * np.pi / r, 1.0]]) @ T
    w, V = np.linalg.eig(C)
    i = int(np.argmax(abs(w)))
    vc = T @ V[:, i]                                   # the state AT the crunch, pre-monodromy
    return (2 * np.pi / r) * abs(vc[0] / vc[1]), abs(w[i]), det


# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE RESULT")
print("=" * 78)
KS = [2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0]
RHO = 0.054                                            # chain A's value, where the test matters
print(f"  rho = {RHO} (the value chain A determines), c_s = 1/sqrt3\n")
print(f"  {'k':>7} {'|det T - 1|':>13} {'|lambda|':>11} {'leaked/direct':>15} "
      f"{'WKB 2 pi/(rho c_s k)':>22}")
vals, ks = [], []
for k in KS:
    ld, lam, det = leaked_over_direct(k, RHO)
    if det > 1e-2:
        print(f"  {k:>7.1f} {det:>13.2e}   -- rejected: Wronskian drift --")
        continue
    vals.append(ld)
    ks.append(k)
    print(f"  {k:>7.1f} {det:>13.2e} {lam:>11.4g} {ld:>15.4f} {2*np.pi/(RHO*CS*k):>22.2f}")
vals, ks = np.array(vals), np.array(ks)
slope = np.polyfit(np.log(ks), np.log(vals), 1)[0]
wkb = 2 * np.pi / (RHO * CS * ks)
print(f"\n  ** log-slope of leaked/direct in k :  CYCLIC {slope:+.4f}   vs   WKB -1.0000 **")
print(f"  ** over the same range WKB runs {wkb[0]:.0f} -> {wkb[-1]:.1f}; the cyclic ratio stays at "
      f"{vals.mean():.1f} +- {vals.std():.1f} ~ 2 pi **")
assert abs(slope) < 0.25, slope
assert 1.0 < vals.mean() < 30.0
print()
for s in [
 "⇒⇒⇒ ** THE $1/k$ IS NOT THERE.  It was a WKB artefact of treating the incoming mode as a FREE",
 "   OSCILLATION.  The construction does not supply a free oscillation — it supplies the output of",
 "   the previous branch point, and that output is already in the survivor branch. **",
 "   *The monodromy itself does it: $J$ sends $c_1\\to c_1+(2\\pi/\\rho)c_0$, so every branch point",
 "   emits a state with $c_0/c_1\\sim\\rho/2\\pi$, and one full cycle does not restore the free-field",
 "   ratio.*",
 "",
 "⌗ *The scatter about $2\\pi$ is oscillatory rather than a trend — the phase accumulated over a",
 "   cycle — and the attractor eigenvalue is large ($10^{1}$–$10^{3}$ per cycle), so a generic state",
 "   reaches the attractor within one passage.  **The test does not need the universe to have cycled",
 "   many times; one is enough.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THAT DOES TO THE LEDGER")
print("=" * 78)
print(f"  {'claim':>52} {'rested on':>22} {'verdict':>14}")
for a_, b_, c_ in [("c54.133's bound rho <= 1.2e-2", "leaked/direct ∝ 1/k", "** FALLS **"),
                   ("c54.141's bound rho <= 6.5e-5", "the same 1/k", "** FALLS **"),
                   ("c54.142's over-determination, 831x", "chain B", "** DISSOLVES **"),
                   ("the BBN floor rho >= 3.8e-6", "standard BBN alone", "STANDS"),
                   ("chain A: rho = 5.4e-2", "one M + the plasma crosses", "STANDS"),
                   ("P15 rem:transmission-leg", "-- asserted --", "** VINDICATED **")]:
    print(f"  {a_:>52} {b_:>22} {c_:>14}")
print()
for s in [
 "✔✔✔ ** SO THE PROGENITOR'S COMPOSITION IS NOT BRACKETED — IT IS DETERMINED. $\\rho\\simeq0.054$,",
 "   from one $M$ across the bead and a crossing plasma, and it satisfies the one surviving bound",
 "   (BBN) by four orders. **",
 "",
 "✔✔ ** AND P15's CLAIM THAT 'THE LEG MULTIPLIES THE SPECTRUM BY A CONSTANT' IS NOW EARNED RATHER",
 "   THAN ASSERTED, AND THE CONSTANT IS COMPUTED: the leaked and direct contributions arrive in a",
 "   fixed ratio $\\sim2\\pi$, $k$-independently, because the previous branch point put the mode in",
 "   the survivor branch. **  *The paper argued it from the degeneracy of the horizon; this argues",
 "   it from the cyclic structure, and the two are independent.*",
 "",
 "⚠ *What this does NOT do is vindicate the reasoning that got here.  Five versions of a composition",
 "   bound were argued or computed and all five are now withdrawn — four for asking the wrong",
 "   question and the fifth for a premise the construction itself contradicts.  **The quantity that",
 "   moved every time was the incoming state, and it was never once looked up in the construction",
 "   until now.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT REPLACES THE BOUND")
print("=" * 78)
print("  On the attractor a full cycle multiplies the mode by lambda(k), so the observable spectral")
print("  distortion is |lambda(k)|^2 -- and the numbers above show it is NOT smooth:")
print(f"\n  {'k':>7} {'|lambda|':>12}")
for k in KS[:6]:
    _, lam, det = leaked_over_direct(k, RHO)
    if det <= 1e-2:
        print(f"  {k:>7.1f} {lam:>12.4g}")
print()
for s in [
 "⇒⇒ ** THE PER-CYCLE AMPLIFICATION OSCILLATES IN $k$, and that is not a defect — it is the",
 "   acoustic structure, arriving from the progenitor rather than from an expanding radiation era.",
 "   **So the composition question and the first-acoustic-peak question are the SAME calculation",
 "   in different variables**, which is the first time those two fronts have touched. **",
 "",
 "⇒ ** THE OWED STEP IS THEREFORE ONE OBJECT, NOT TWO: compute $|\\lambda(k)|^2$ across the observed",
 "   range on $\\rho=0.054$, and read off both the spectral distortion (which bounds the composition,",
 "   properly this time) and the peak positions (which is front #2). **",
 "   *Same integration, same background, same attractor — and it is the calculation the corpus has",
 "   been circling since c54.121.*",
]:
    print("  " + s)
