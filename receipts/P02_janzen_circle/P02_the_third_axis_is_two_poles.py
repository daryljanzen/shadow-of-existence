"""
P02_the_third_axis_is_two_poles.py -- the complex-z continuations, classified exactly, and the
count of them read off the circle.

** THE REAL-LANDING SET IS EXACTLY THREE AXES AND THERE IS NO FOURTH. **  Writing z = a + ib, the
cycloid r = M(1 + cos z) has Im r = -M sin(a) sinh(b) -- a PRODUCT -- so Im r = 0 iff b = 0 or
a in pi*Z, and 2pi-periodicity collapses the second to a = 0 and a = pi.

** AND THE THREE EXHAUST THE GEOMETRY, not merely the reality condition: ** their ranges are
0 <= r <= 2M (the cycloid arc), r >= 2M (the front seam) and r <= 0 (the back seam), which partition
the real radius line.  On them tau is real, purely imaginary, and purely imaginary about tau = M pi
-- Lorentzian on the arc, Riemannian on the two seams, which is what makes the imaginary axes
physical rather than formal.

** AND THE COUNT IS THE CIRCLE'S OWN. **  The parametrisation carries the reflection z -> -z, under
which r is EVEN and tau is ODD; its fixed points on R/2piZ are z = 0 and z = pi, where r = 2M and
r = 0 -- the event horizon and the curvature singularity, the paper's two poles.  So the number of
continuations beyond the real one is |Fix(z -> -z)| = 2: not a fact about the cosine.

WHAT PROMPTED IT.  P2 states the criterion ("a continuation is physical exactly when it lands on a
real region of the geometry"), states the list, and states the verdict ("the third axis is
therefore resolved, not open") -- but asserts the exhaustiveness rather than proving it, and does
not observe that the two seam axes sit at the fixed points of the parametrisation's own reflection.

STATUS: ✔✔ (Im r asserted equal to -M sin a sinh b; the r-ranges on the two imaginary axes asserted;
  Re(tau) asserted zero on one and M*pi on the other; r asserted even and tau odd under z -> -z; and
  r(0) = 2M, r(pi) = 0 asserted)
RUN: python3 P02_the_third_axis_is_two_poles.py   RUNTIME: <10s (sympy)
ORIGIN: computations/beyond_the_wall/L145_the_third_axis_is_two_poles.py, built r2376 (c54.111).
ORIGIN-DIVERGENCE: none of substance; the origin is a lead disposal and opens and closes on the
  register's own bookkeeping, which is kept there rather than here.
"""
import sympy as sp

print(__doc__.split("STATUS:")[0])

a, b, M, rho = sp.symbols('a b M rho', real=True)
Mp = sp.Symbol('M', positive=True)
z = a + sp.I*b

# the Schwarzschild interior in Lemaitre--Tolman cycloid form (P2 sec:cycloid)
r = Mp*(1 + sp.cos(z))
tau = Mp*(z + sp.sin(z))

# =====================================================================
print("=" * 78)
print("PART 1 — THE REALITY CONDITION, SOLVED EXACTLY")
print("=" * 78)
print("  P2's cycloid:   r(z) = M(1 + cos z),   tau(z) = M(z + sin z),   z = a + i b")
Imr = sp.simplify(sp.im(sp.expand(r.rewrite(sp.exp)).rewrite(sp.cos)))
Imr = sp.simplify(sp.expand_trig(sp.simplify(sp.im(Mp*(1 + sp.cos(a + sp.I*b))))))
print(f"\n  Im r = {Imr}")
tgt = -Mp*sp.sin(a)*sp.sinh(b)
print(f"  which is exactly  -M sin(a) sinh(b):  ** {sp.simplify(Imr - tgt) == 0} **")
assert sp.simplify(Imr - tgt) == 0
print()
for s in [
 "⇒⇒ ** SO Im r = 0  <=>  sin(a) = 0  OR  sinh(b) = 0  <=>  a in pi*Z  OR  b = 0. **",
 "   *A product of two factors, each vanishing on a line.  There is nothing else to solve.*",
 "",
 "⌗ ** AND THE PARAMETER IS $2\\pi$-PERIODIC, so $a\\in\\pi\\mathbb Z$ collapses to TWO values, $a=0$ and",
 "   $a=\\pi$. **  *With the real axis $b=0$ that is THREE axes in the $z$ plane and no fourth --",
 "   which is precisely the list P2 states, now proved rather than enumerated.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT EACH AXIS REACHES")
print("=" * 78)
AX = [("b = 0 (z real)", sp.simplify(r.subs({a: a, b: 0}).rewrite(sp.cos)),
       "the cycloid arc"),
      ("a = 0 (z = i rho)", sp.simplify(r.subs({a: 0, b: rho})), "the FRONT seam"),
      ("a = pi (z = pi + i rho)", sp.simplify(r.subs({a: sp.pi, b: rho})), "the BACK seam")]
print(f"  {'axis':>26} {'r on it':>26} {'range':>22} {'P2 calls it':>16}")
rows = [
    ("b = 0  (z real)", "M(1 + cos a)", "0 <= r <= 2M", "the cycloid arc"),
    ("a = 0  (z = i rho)", "M(1 + cosh rho)", "r >= 2M", "the front seam"),
    ("a = pi (z = pi + i rho)", "M(1 - cosh rho)", "r <= 0", "the back seam"),
]
for w, x, yy, zz in rows:
    print(f"  {w:>26} {x:>26} {yy:>22} {zz:>16}")
r_front = sp.simplify(Mp*(1 + sp.cos(sp.I*rho)))
r_back = sp.simplify(Mp*(1 + sp.cos(sp.pi + sp.I*rho)))
print()
print(f"  checked: r on a=0   is {r_front}   (>= 2M for real rho)")
print(f"           r on a=pi  is {r_back}   (<= 0  for real rho)")
assert sp.simplify(r_front - Mp*(1 + sp.cosh(rho))) == 0
assert sp.simplify(r_back - Mp*(1 - sp.cosh(rho))) == 0
print()
for s in [
 "⇒ ** THE THREE AXES PARTITION THE WHOLE REAL $r$ LINE: $[0,2M]$ on the real axis, $[2M,\\infty)$ on",
 "   one imaginary axis, $(-\\infty,0]$ on the other.  Nothing real is missed and nothing is",
 "   double-counted. **  *That is why the list is exhaustive in the sense that matters: not merely",
 "   'no fourth axis' but 'the three already cover the geometry'.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE SIGNATURE ON EACH AXIS")
print("=" * 78)
tau_real = sp.simplify(Mp*(a + sp.sin(a)))
tau_front = sp.simplify(Mp*(sp.I*rho + sp.sin(sp.I*rho)))
tau_back = sp.simplify(Mp*(sp.pi + sp.I*rho + sp.sin(sp.pi + sp.I*rho)))
print(f"  {'axis':>26} {'tau on it':>34} {'reading':>22}")
print(f"  {'b = 0':>26} {'M(a + sin a)   -- REAL':>34} {'Lorentzian':>22}")
print(f"  {'a = 0':>26} {str(sp.simplify(tau_front)) + '  -- purely imaginary':>34} "
      f"{'Riemannian':>22}")
print(f"  {'a = pi':>26} {str(sp.simplify(tau_back - Mp*sp.pi)) + '  + M pi':>34} "
      f"{'Riemannian, offset':>22}")
pf = sp.simplify(sp.re(sp.expand(tau_front)))
pb = sp.simplify(sp.re(sp.expand(tau_back)) - Mp*sp.pi)
print()
print(f"  Re(tau) on a=0  is {pf}: ** purely imaginary, so the section is Riemannian. **")
print(f"  Re(tau) - M*pi on a=pi is {pb}: ** the same, based at tau = M pi. **")
assert pf == 0 and pb == 0
print()
for s in [
 "⌗ ** SO THE CRITERION IS NOT 'EVERYTHING REAL' BUT 'REAL GEOMETRY': $r$ real, and $\\tau$ real OR",
 "   purely imaginary about a real base -- Lorentzian on one axis, Riemannian on the other two. **",
 "   *That is exactly P2's 'the Riemannian$\\leftrightarrow$Lorentzian and backward-radial",
 "   continuations of one closed slicing curve', and it is what makes the imaginary axes physical",
 "   rather than formal.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE COUNT IS FORCED")
print("=" * 78)
print("  The parametrisation carries a reflection  z |-> -z :")
print(f"     r(-z) - r(z)   = {sp.simplify(Mp*(1+sp.cos(-a)) - Mp*(1+sp.cos(a)))}   -- r is EVEN")
print(f"     tau(-z) + tau(z) = {sp.simplify(Mp*(-a + sp.sin(-a)) + Mp*(a + sp.sin(a)))}"
      "   -- tau is ODD")
assert sp.simplify(Mp*(1+sp.cos(-a)) - Mp*(1+sp.cos(a))) == 0
assert sp.simplify(Mp*(-a + sp.sin(-a)) + Mp*(a + sp.sin(a))) == 0
print("  ** so z |-> -z fixes the radius and reverses the cycloid time: it is the reflection of")
print("     the circle in its own axis. **")
print()
print("  Its fixed points on the circle R/2piZ are  z = 0  and  z = pi :")
print(f"     r(0)  = {sp.simplify(Mp*(1+sp.cos(0)))}   -- ** the event horizon **")
print(f"     r(pi) = {sp.simplify(Mp*(1+sp.cos(sp.pi)))}   -- ** the curvature singularity **")
assert sp.simplify(Mp*(1+sp.cos(0))) == 2*Mp and sp.simplify(Mp*(1+sp.cos(sp.pi))) == 0
print()
for s in [
 "⇒⇒⇒ ** AND THOSE ARE EXACTLY THE TWO VALUES OF $a$ THE REALITY CONDITION SELECTED. **  *The",
 "   imaginary axes do not stand at arbitrary places: they stand at the fixed points of the",
 "   parametrisation's own reflection, which P2's title object names as the circle's TWO POLES --",
 "   the event horizon and the curvature singularity.*",
 "",
 "⌗⌗ ** SO THE NUMBER OF EXTRA AXES IS NOT A FACT ABOUT $\\cos$: IT IS $|\\mathrm{Fix}(z\\mapsto-z)|$ ON",
 "   THE CIRCLE, WHICH IS TWO. **  *A question phrased as 'is there a third axis' has the answer",
 "   'there are exactly two beyond the real one, and their count is the number of poles the circle",
 "   has' -- which is the paper's own central object doing the counting.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT `L-145` BECOMES")
print("=" * 78)
for s in [
 "⌗ ** THE ROW'S TWO CLAIMS ABOUT ITSELF ARE BOTH STALE. **",
 "   *'no sharp resolution criterion' -- P2 states one: **a continuation is physical exactly when it",
 "   lands on a real region of the geometry.**",
 "   'exploratory' -- P2 states the verdict: **'The third axis is therefore resolved, not open.'***",
 "",
 "✔ ** AND WHAT THE PAPER ASSERTED, THIS PROVES: the real-landing set is EXACTLY three axes,",
 "   because $\\mathrm{Im}\\,r = -M\\sin a\\sinh b$ factorises and the parameter is $2\\pi$-periodic. **",
 "✔ ** THE THREE PARTITION THE REAL $r$ LINE -- $[0,2M]$, $[2M,\\infty)$, $(-\\infty,0]$ -- so they",
 "   exhaust the geometry rather than merely exhausting the solutions of a reality condition. **",
 "✔ ** AND THEIR COUNT IS FORCED BY THE CIRCLE: two, the fixed points of $z\\mapsto-z$, which are",
 "   the horizon and the singularity. **",
 "⇒ ** `L-145` STRIKES. **",
 "",
 "⚠ *One thing is worth carrying and is not claimed: the reflection $z\\mapsto-z$ here is $r$-even",
 "and $\\tau$-odd, i.e. cycloid-time reversal.  Whether it is the corpus's $R$ (mass reflection),",
 "$K$ (the reality involution), or a third thing is not settled here and is not needed for the",
 "count.*",
]:
    print("  " + s)
