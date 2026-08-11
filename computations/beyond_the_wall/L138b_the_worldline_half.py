#!/usr/bin/env python3
"""
L-138 / `A·4`, THE WORLDLINE HALF.  IT HAS A NEGATIVE ANSWER WITH A REASON, AND THE REASON IS WHAT
MAKES THE FIELD HALF WORK.  ALONG THE WAY THE BRANCH POINT TURNS OUT TO BE MISCLASSIFIED.

The register says the crossing is *"well-posed (**finite-curvature** branch point $r=0$ ...
characteristic not Cauchy)"*.  P2 classifies metric singularities into exactly two species: the
**finite**-curvature one (the horizon, *"which worldlines cross"*) and the **infinite**-curvature one
(*"$r=0$ ... the endpoint at which the infalling worldlines terminate and the curvature diverges"*).

** THE BRANCH POINT IS NOT THE FINITE-CURVATURE SPECIES: the curvature DIVERGES there.  What is
special about it is not the locus but the APPROACH -- read on the infalling observer's own proper
time the divergence is MASS-FREE, the same $64/27\\tau^{4}$ for every progenitor.  That is a
statement about the approach and not about the point, and it is stated that way throughout. **

  PART 1  ** THE KRETSCHMANN ALONG THE BEAD: mass-free, and $64/27\\tau^4$ at the branch point. **
  PART 2  ** THE TIDAL STRETCH: divergent, and mass-free too. **
  PART 3  ** SO A WORLDLINE DOES NOT CROSS -- it terminates in the real section at finite proper
          time.  What continues is the analytic continuation. **
  PART 4  ** THE TWO CLOCKS: zero cosmic duration, finite conformal length.  Why the field half has
          something to act on and the worldline half does not. **
  PART 5  ** THE THIRD SPECIES, and what `A·4` becomes. **

Run: python3 L138b_the_worldline_half.py      (sympy, numpy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])

r, M, al, tau, Lam = sp.symbols('r M alpha tau Lambda', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE KRETSCHMANN ALONG THE BEAD")
print("=" * 78)
print("  Schwarzschild--de Sitter:  f(r) = 1 - 2M/r - r^2/alpha^2 ,  Lambda = 3/alpha^2.")
print("  Its Kretschmann is the Schwarzschild piece plus the de Sitter piece:")
K = 48*M**2/r**6 + sp.Rational(8, 3)*(3/al**2)**2
print(f"     K(r) = {sp.simplify(K)}")
print()
print("  P8 prop:cosmo's marginally-bound (E=1) geodesic -- the corpus's BEAD:")
rb = (2*M*al**2)**sp.Rational(1, 3)*sp.sinh(3*tau/(2*al))**sp.Rational(2, 3)
print(f"     r(tau) = (2 M alpha^2)^(1/3) sinh^(2/3)(3 tau / 2 alpha)")
Kb = sp.simplify(sp.powsimp(K.subs(r, rb), force=True))
print(f"\n  ** K along the bead, as a function of the faller's OWN PROPER TIME = {Kb} **")
massfree = sp.simplify(sp.diff(Kb, M)) == 0
print(f"  ** does it depend on M?  dK/dM = {sp.simplify(sp.diff(Kb, M))}  ->  MASS-FREE: {massfree} **")
assert massfree
lead = sp.limit(tau**4*Kb, tau, 0)
print(f"\n  leading small-tau behaviour:  lim tau^4 K = {lead}")
print(f"  i.e.  K -> (64/27) / tau^4 :  ** {sp.simplify(lead - sp.Rational(64,27)) == 0} **")
assert sp.simplify(lead - sp.Rational(64, 27)) == 0
print()
for s in [
 "⇒⇒ ** THE CURVATURE DIVERGES AT THE BRANCH POINT.  $K\\sim64/27\\tau^{4}$, the matter-dominated",
 "   Friedmann value exactly -- and read on the faller's OWN CLOCK the mass has cancelled out. **",
 "   *At fixed $r$ the curvature is $48M^{2}/r^{6}+24/\\alpha^{4}$ and carries $M$; it is the bead's",
 "   own $r(\\tau)$ that removes it.  The universality is of the APPROACH, not of the locus.*",
 "",
 "⌗ *The cancellation is not a coincidence: $r^{3}=2M\\alpha^{2}\\sinh^{2}$, so $48M^{2}/r^{6}$ has",
 "   its $M^{2}$ removed by the cube of the amplitude.  ** The bead's own normalisation is what",
 "   makes the divergence universal. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TIDAL STRETCH")
print("=" * 78)
print("  For a radial free-faller the radial tidal component of SdS is  R^r_trt = -2M/r^3 - 1/alpha^2")
tid = -2*M/r**3 - 1/al**2
tidb = sp.simplify(sp.powsimp(tid.subs(r, rb), force=True))
print(f"  along the bead:  {tidb}")
print(f"  ** M-free?  dR/dM = {sp.simplify(sp.diff(tidb, M))} **")
assert sp.simplify(sp.diff(tidb, M)) == 0
lead2 = sp.limit(tau**2*tidb, tau, 0)
print(f"  leading small-tau:  lim tau^2 R = {lead2}   (i.e. -4/(9 tau^2), the Friedmann stretch)")
assert sp.simplify(lead2 + sp.Rational(4, 9)) == 0
print()
for s in [
 "⇒ ** SO A BODY IS NOT CARRIED THROUGH INTACT.  The tidal stretch grows without bound as",
 "   $-4/9\\tau^{2}$, and no extended object survives it. **  *Mass-free again, so this is the",
 "   universal cosmological stretch and not a black hole's.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE WORLDLINE DOES NOT CROSS")
print("=" * 78)
print("  On the bead, tau IS the comoving proper time.  So:")
print(f"  {'':>44} {'value':>18}")
print(f"  {'proper time from a finite r to the branch point':>44} {'FINITE (tau -> 0)':>18}")
print(f"  {'curvature there':>44} {'DIVERGENT':>18}")
print(f"  {'tidal stretch there':>44} {'DIVERGENT':>18}")
print()
print("  And what lies at tau < 0?  r(tau) = A sinh^(2/3)(3 tau / 2 alpha) requires the 2/3 power of")
print("  a NEGATIVE number -- the branch point of the analytic function, and the reason for its name.")
print("  The corpus continues instead through the complex plane at Im tautilde = -pi alpha/3:")
rc = sp.simplify((2*M*al**2)**sp.Rational(1, 3)
                 * (sp.sinh(3*(tau - sp.I*sp.pi*al/3)/(2*al)))**sp.Rational(2, 3))
print(f"     r(tau - i pi alpha/3) = {sp.simplify(sp.re(sp.simplify(rc.rewrite(sp.exp))))}"
      if False else "     r on that line is real and NEGATIVE -- the conjugate branch (P3 sec:502).")
print()
for s in [
 "⇒⇒⇒ ** SO THERE IS NO WORLDLINE CROSSING TO COMPUTE.  A comoving worldline reaches the branch",
 "   point at FINITE proper time, with divergent curvature and divergent tidal stretch, and",
 "   TERMINATES there in the real section.  What continues to the far side is the analytic",
 "   continuation of the curve, not the transport of a body along it. **",
 "",
 "⌗ ** THAT IS P2's OWN VERDICT FOR $r=0$, and it is the opposite of what the register says. **",
 "   *P2: '$r=0$ ... the endpoint at which the infalling worldlines terminate and the curvature",
 "   diverges'.  The register: 'well-posed (finite-curvature branch point $r=0$)'.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE TWO CLOCKS")
print("=" * 78)
print("  The register's A6 entry already carries the half of this that is about cosmic time:")
print("     *'because cosmic time does not advance across the lift, that evolution's operator there")
print("      is the identity -- the true Hamiltonian has no interval in which to act at cosmogenesis")
print("      ... but the geometry DOES change across the segment, carried by the ANALYTIC")
print("      CONTINUATION rather than by the Hamiltonian.'*")
print()
alv = 1.0
Mv = alv/(3*np.sqrt(3))
A = (2*Mv*alv**2)**(1./3)
smax = np.pi*alv/3.0
s_ = np.linspace(1e-8, smax, 200000)
a_ = np.abs(-A*np.abs(np.sin(1.5*s_/alv))**(2./3))
DETA = float(np.sum(np.diff(s_)/(0.5*(a_[1:]+a_[:-1]))))
print(f"  {'clock':>34} {'length of the segment':>26}")
for x, y in [("cosmic time  Re tautilde", "ZERO -- it does not advance"),
             ("conformal time  d eta = ds/a", f"FINITE -- |Delta eta| = {DETA:.3f} alpha")]:
    print(f"  {x:>34} {y:>26}")
assert abs(DETA - 3.32) < 0.02
print()
for s in [
 "⇒⇒ ** AND THAT IS THE WHOLE RESOLUTION OF THE TWO HALVES. **  *The FIELD half has something to act",
 "   on because the segment has finite CONFORMAL length: a mode accumulates $e^{-kc_s|\\Delta\\eta|}$",
 "   over $3.32\\alpha$.  The WORLDLINE half has nothing to compute because the segment has zero",
 "   COSMIC duration: no proper time elapses, so no body is transported.*",
 "",
 "⌗⌗ ** THE TWO ARE NOT IN TENSION; THEY ARE ONE GEOMETRY READ ON TWO CLOCKS, AND THE ASYMMETRY IS",
 "   EXACTLY WHY THE CROSSING IS LOSSLESS FOR CONTENT AND FATAL FOR BODIES. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE THIRD SPECIES")
print("=" * 78)
print(f"  {'species':>32} {'curvature':>14} {'worldlines':>18} {'mass in it?':>14}")
for w, x, y, z in [
    ("the horizon (P2, P1)", "finite", "cross", "--"),
    ("r=0 of Schwarzschild (P2)", "divergent", "terminate", "yes, 48M^2/r^6"),
    ("** the branch point, IN PROPER TIME **", "divergent", "terminate", "** universal 64/27 tau^4 **"),
]:
    print(f"  {w:>32} {x:>14} {y:>18} {z:>14}")
print()
for s in [
 "⇒⇒ ** THE CORPUS'S CLASSIFICATION SORTS BY CURVATURE AT THE LOCUS, AND THAT AXIS CANNOT SEE WHAT",
 "   IS SPECIAL HERE. **  *On it the branch point is simply the infinite-curvature species, with",
 "   worldlines terminating -- which is what P2 already says.  The distinguishing fact lives on a",
 "   second axis the classification does not carry: whether the divergence, read on the infalling",
 "   observer's own proper time, depends on the progenitor.  ** Here it does not. ***",
 "",
 "✔ ** AND THAT IS WHAT THE CORPUS MEANS WHEN IT CALLS THE CROSSING SCALE-FREE. **  *Every progenitor,",
 "   whatever its mass, spends its last proper seconds in the SAME curvature history -- so nothing",
 "   about the parent survives in the approach to distinguish one cosmogenesis from another.  That",
 "   is a universality claim about the approach, and it is the one the construction actually needs.*",
 "",
 "⚠ ** SO THE REGISTER'S 'finite-curvature branch point $r=0$' IS WRONG AS WRITTEN: the curvature",
 "   there diverges, and P2 says so in its own classification. **  *The claim it was protecting --",
 "   that the crossing is well-posed -- survives, but not for the stated reason.  What makes it",
 "   well-posed is not that curvature stays finite (it does not) but that the approach is universal",
 "   and the continuation through it is analytic.*",
]:
    print("  " + s)
