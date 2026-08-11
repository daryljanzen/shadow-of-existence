"""
P07_eikonal_ratio_is_D_minus_three.py -- P7's eikonal-ringdown consistency, at general $D$.

** $\\lambda^{2}/\\Omega_c^{2} = D-3$ EXACTLY, for every $M$ and every $\\alpha$. **  So the
mass- and curvature-independence of the eikonal quality factor is NOT a four-dimensional fact --
it holds in every dimension.  What is four-dimensional is the ratio's VALUE being one.

WHAT PROMPTED IT.  The framework records the $D=4$ identity $2f-r^{2}f''\\equiv2$, hence
$\\lambda=\\Omega_c$ and a quality factor $\\ell/(n+\\tfrac12)$ independent of $M$ and $\\alpha$, and
marks it as a consistency of the reading rather than an independent prediction.  The
$D$-dependence was never computed, and the independence was tacitly attributed to the identity.

WHAT IS ESTABLISHED.
  1. ** THE IDENTITY AT GENERAL $D$, IN CLOSED FORM ** (asserted at $D=4\\ldots8$):
     $2f-r^{2}f'' = 2 + 2M\\,[(D-3)(D-2)-2]\\,r^{-(D-3)}$, and the bracket factors as
     $(D-1)(D-4)$, so it vanishes exactly at $D=4$ among dimensions above three.
  2. ** THE RATIO, COMPUTED RATHER THAN QUOTED ** (asserted at $D=4,\\ldots,9$): with the photon
     sphere at $rf'=2f$, $\\Omega_c^{2}=f_c/r_c^{2}$ and
     $\\lambda^{2}=-(r_c^{2}f_c/2)\\,(f/r^{2})''|_{r_c}$, the ratio $\\lambda^{2}/\\Omega_c^{2}$
     equals $D-3$ identically -- no $M$, no $\\alpha$, no residue.
  3. ** THE REASON, IN ONE LINE. **  The photon-sphere condition gives $M r_c^{-(D-3)}=1/(D-1)$,
     so the identity's excess becomes $2(D-1)(D-4)/(D-1)=2(D-4)$ and
     $\\lambda^{2}-\\Omega_c^{2}=(D-4)\\Omega_c^{2}$.
  4. ** HENCE THE CORRECTION TO THE READING: the eikonal quality factor is
     $\\ell/[\\sqrt{D-3}\\,(n+\\tfrac12)]$ in every dimension and is always $M$- and $\\alpha$-free.
     The four-dimensional content is $\\lambda=\\Omega_c$, not the independence. **  At $D=5$ and
     $D=6$ the ratios $\\Omega_c/\\lambda$ are $1/\\sqrt2$ and $1/\\sqrt3$.

** SCOPE.  Standard eikonal/geodesic correspondence for a static spherically symmetric metric,
applied to the $D$-dimensional Schwarzschild--de~Sitter function $f=1-2M/r^{D-3}-r^{2}/\\alpha^{2}$.
This is a statement about that function's photon sphere and Lyapunov exponent and inherits the
same altitude the framework already assigns the $D=4$ case: a consistency of the reading, not an
independent prediction. **

ORIGIN: computations/baryon_edge/L016w_the_dimension_cluster.py -- built r2376 (c54.83);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also disposes of four register items
about other structures at general $D$.  ** This copy carries the paper-facing subset: every
assertion here appears in the origin verbatim, and nothing here is absent from it. **"""
import sympy as sp

print(__doc__)
r, M, al = sp.symbols('r M alpha', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE IDENTITY AT GENERAL D")
print("=" * 78)
HDR = "2f - r^2 f''"
print(f"  {'D':>3} {HDR:>26} {'the coefficient':>26}")
for D in range(4, 9):
    f = 1 - 2*M/r**(D-3) - r**2/al**2
    idn = sp.simplify(sp.expand(2*f - r**2*sp.diff(f, r, 2)))
    coef = sp.expand((D-3)*(D-2) - 2)
    print(f"  {D:>3} {str(idn):>26} {f'(D-3)(D-2)-2 = {coef}':>26}")
    assert sp.simplify(idn - (2 + 2*M*((D-3)*(D-2)-2)*r**(-(D-3)))) == 0
Dd = sp.Symbol('D')
print()
print(f"  (D-3)(D-2)-2 = {sp.factor(sp.expand((Dd-3)*(Dd-2)-2))}   "
      f"** vanishing exactly at D = 4 above three **")
assert sp.expand((Dd-3)*(Dd-2)-2 - (Dd-1)*(Dd-4)) == 0

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE RATIO, COMPUTED")
print("=" * 78)
print("  photon sphere at r f' = 2f;  Omega_c^2 = f_c / r_c^2;")
print("  lambda^2 = -(r_c^2 f_c / 2) (f/r^2)''|_{r_c}")
print()
print(f"  {'D':>3} {'r_c':>22} {'lambda^2 / Omega_c^2':>22} {'lambda / Omega_c':>18}")
for D in range(4, 10):
    f = 1 - 2*M/r**(D-3) - r**2/al**2
    g = sp.simplify(f/r**2)
    rc = [x for x in sp.solve(sp.Eq(sp.simplify(r*sp.diff(f, r) - 2*f), 0), r)
          if x.is_real is not False][0]
    fc = sp.simplify(f.subs(r, rc))
    lam2 = sp.simplify(-(rc**2*fc/2)*sp.simplify(sp.diff(g, r, 2).subs(r, rc)))
    Om2 = sp.simplify(fc/rc**2)
    ratio = sp.simplify(sp.radsimp(lam2/Om2))
    print(f"  {D:>3} {str(sp.simplify(rc)):>22} {str(ratio):>22} {str(sp.sqrt(ratio)):>18}")
    assert sp.simplify(ratio - (D - 3)) == 0
print()
for s in [
 "⇒⇒ ** $\\lambda^2/\\Omega_c^2 = D-3$ EXACTLY, ASSERTED AT SIX DIMENSIONS, INDEPENDENT OF $M$ AND",
 "   $\\alpha$ AT EVERY $D$. **",
 "",
 "⌗ *The reason in one line: the photon-sphere condition gives $Mr_c^{-(D-3)}=1/(D-1)$, so the",
 "identity's excess $2M[(D-3)(D-2)-2]r_c^{-(D-3)}$ becomes $2(D-1)(D-4)/(D-1)=2(D-4)$, whence",
 "$\\lambda^2-\\Omega_c^2=(D-4)\\Omega_c^2$.*",
 "",
 "⚠⚠ ** SO THE READING NEEDS ONE WORD CHANGED: the eikonal quality factor is",
 "   $\\ell/[\\sqrt{D-3}(n+\\tfrac12)]$ in EVERY dimension and is always $M$- and $\\alpha$-free.  The",
 "   four-dimensional content is not the independence but the VALUE, $\\lambda=\\Omega_c$. **",
]:
    print("  " + s)
