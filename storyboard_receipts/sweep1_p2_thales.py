"""
THE FULL-CORPUS SWEEP, question 1: IS P2's CYCLOID CIRCLE THE THALES CIRCLE?  (r1115)

WHY THIS RECEIPT EXISTS. At r1115 I baked the geometric upgrade into five downstream papers
and wrote, of the other ten: "no locus the material bears on -- adding to them would be
decoration." ** I had not looked at one of them. ** That is an absence declared from a search
never run (CODA_FIELD_NOTE face 18's worst form; face 35's cousin), with the restraint dressed
up as a result. Daryl caught it. This is the sweep, done properly, and P2 is first because
there is something checkable in it.

THE QUESTION. P3's construction (alpha_alone.py, tab1) has the ** THALES CIRCLE **:
    the hole translated onto its own edge -- centre (alpha, 0), radius alpha,
    passing through the hole's CENTRE (0,0) and ending at the HINGE (2 alpha, 0).
P2's construction has the ** CYCLOID CIRCLE **:
    r(z) = M(1 + cos z), "the trajectory traced by a point on the rim of a circle of radius M
    as the circle rolls along a straight line" -- with r = 2M at z = 0 (the horizon) and
    r = 0 at z = pi (the standard singularity), the two endpoints being P2's two critical
    points of identical analytic character.

    ** Both are a circle of radius X centred at (X, 0), through 0 and 2X. **

Is that the same construction at two scales -- alpha for the substrate's throat, M for the
hole -- or two circles that happen to share a description?

** THE PREDICTION, NAMED BEFORE COMPUTING. ** If it IS the same construction, then P2's two
critical points (r=0 and r=2M) must be the SAME PAIR as the Thales circle's two distinguished
points (the hole's centre and the hinge), under alpha -> M. And P2's central claim is that its
two endpoints are ** critical points of identical analytic character on a smooth manifold **.
The Thales circle's two points are the CENTRE and the HINGE -- which are not obviously "of
identical character" at all. ** So I expect a real correspondence at the level of the circle
and a MISMATCH at the level of what the two endpoints ARE. If so, the mismatch is the finding,
not the match. **

COULD THIS RETURN OTHERWISE? Yes: the parametrisations are explicit, the two-point structure
is explicit, and either they map onto each other or they do not.
"""
import numpy as np

print("="*80)
print("1. THE TWO CIRCLES, WRITTEN OUT")
print("="*80)
M, alpha = 1.0, 1.0

# P2's cycloid circle:  x = r(z) = M(1+cos z),  y = M sin z.
# ANALYTIC, not sampled: (x - M)^2 + y^2 = M^2 cos^2 z + M^2 sin^2 z = M^2, identically.
# So centre (M, 0), radius M -- exact, for every z. (An earlier version took max/min over a
# 400-point linspace and the assert refused: linspace(0, 2pi, 400) never lands on pi, so the
# minimum was not 0. Face 37 on this receipt's own hand -- do not sample an identity.)
import sympy as sp
zs, Ms = sp.symbols('z M', real=True, positive=True)
lhs = sp.simplify((Ms*(1+sp.cos(zs)) - Ms)**2 + (Ms*sp.sin(zs))**2)
print(f"  P2's cycloid circle:  x = M(1+cos z),  y = M sin z")
print(f"      identity: (x-M)^2 + y^2 = {lhs}   ->  centre (M, 0), radius M, for ALL z")
assert sp.simplify(lhs - Ms**2) == 0
print(f"      its diameter runs r = 0 (z=pi, the 'singularity') to r = 2M (z=0, the horizon)")
print(f"  P3's Thales circle:   centre ({alpha:.4f}, 0), radius {alpha:.4f}")
print(f"      its diameter runs 0 (the hole's centre) to {2*alpha:.4f} (the hinge)")
print(f"\n  ** SAME CONSTRUCTION under alpha <-> M: a circle of radius X centred at (X,0),")
print(f"     through 0 and 2X. Established as an identity, not a fit. **")
print("""
  ** So P2's rolling circle and P3's Thales circle are ONE CONSTRUCTION at two scales:
     a circle of radius X centred at (X,0), through 0 and 2X. **
  P2 rolls it to make the cycloid; P3 uses it to place the hinge. Neither paper says so.""")

print("\n" + "="*80)
print("2. AND THALES' THEOREM IS WHY P2's CIRCLE IS THE ONE IT IS")
print("="*80)
print("""  A circle on the diameter from 0 to 2X has the defining property (Thales): every point P
  on it sees that diameter at a RIGHT ANGLE. Check it on P2's own circle:""")
A0, B0 = np.array([0.0, 0.0]), np.array([2*M, 0.0])
worst = 0.0
for zz in np.linspace(0.15, 2*np.pi-0.15, 500):
    P = np.array([M*(1+np.cos(zz)), M*np.sin(zz)])
    d = abs(np.dot(A0-P, B0-P))
    worst = max(worst, d)
print(f"  max |(0-P)·(2M-P)| over 500 points of P2's circle: {worst:.2e}   -> right angle, every one")
assert worst < 1e-9
print("""
  ** P2's circle IS a Thales circle on the diameter [0, 2M]. ** That is not a coincidence of
  shape: it is why r(z) = M(1+cos z) has its two critical points where it does. The endpoints
  of the diameter ARE the two critical points, and Thales' theorem is the statement that the
  circle is exactly the locus seeing them orthogonally.""")

print("\n" + "="*80)
print("3. ** THE MISMATCH, WHICH IS THE FINDING -- what the two endpoints ARE **")
print("="*80)
print("""  P2's two endpoints:  r = 2M (the horizon) and r = 0 (the 'singularity').
      P2's central claim: they are ** non-degenerate critical points of IDENTICAL analytic
      character ** on a smooth manifold -- that is the paper's whole result.
  P3's two points:     the hole's CENTRE (0) and the HINGE (2 alpha).
      These are NOT of identical character: the centre is on the throat's axis, the hinge is a
      vantage 2 alpha out. One is a point of the geometry; the other is where an observer's
      pivot sits.""")
print(f"\n  {'point':>26} {'P2 reads it as':>26} {'P3 reads it as':>26}")
print(f"  {'x = 0':>26} {'the r=0 critical point':>26} {'the hole''s centre':>26}")
print(f"  {'x = 2X':>26} {'the horizon r=2M':>26} {'the hinge':>26}")
print("""
  ** SO THE SCALES DO NOT MATCH BY ACCIDENT AND THEY DO NOT MATCH BY IDENTITY EITHER. **
  P2's circle is drawn on the diameter [0, 2M] -- 2M is the HORIZON, a locus of the geometry.
  P3's Thales circle is drawn on the diameter [0, 2alpha] -- 2alpha is the HINGE, the vantage.
  Same construction, different diameters: one spans a geometry's own two critical points, the
  other spans the throat's centre and an observer's pivot.

  ** AND THAT IS EXACTLY THE CORPUS'S OWN GEOMETRY/VANTAGE PARTITION, DRAWN TWICE. **
  P2's is intrinsic (2M is where the geometry turns); P3's is perspectival (2alpha is where a
  vantage stands, and alpha is the invariant). The one construction appears once on each side
  of the partition the whole programme runs on.""")

print("\n" + "="*80)
print("4. WHAT WOULD MAKE IT MORE THAN A SHARED CONSTRUCTION -- named, and TESTED")
print("="*80)
print("""  The tempting move: 2M and 2alpha are 'the same 2', so the two circles are one object.
  ** TEST IT. ** In P3 the mass is not free: 2M = alpha(r0/alpha - (r0/alpha)^3). Is there a
  slicing at which P2's circle (diameter 2M) IS P3's Thales circle (diameter 2 alpha)?""")
print(f"\n  need 2M = 2 alpha, i.e. r0 - r0^3 = 1 (in units alpha=1):")
rts = np.roots([-1.0, 0.0, 1.0, -1.0])
real = rts[abs(rts.imag) < 1e-9].real
print(f"    roots of r0 - r0^3 = 1 : {np.round(rts,4)}")
print(f"    real roots             : {np.round(real,4) if len(real) else 'NONE in range'}")
mx = 2/(3*np.sqrt(3))
print(f"    and |2M| is BOUNDED: max over all slicings = 2/(3 sqrt3) = {mx:.6f} << 2")
assert mx < 2
print(f"""
  ** NO SLICING HAS 2M = 2 alpha. ** The mass is capped at 2/(3 sqrt3) alpha ~ {mx:.4f} alpha
  (the Nariai value -- P3's own maximum of sin 3w), so P2's circle is ALWAYS smaller than P3's
  Thales circle, by at least a factor {2/mx:.2f}. ** The two circles never coincide, for the
  construction's own reason: the mass is bounded and the throat is not. **
  The shared construction is real; the identification is refuted by P3's own mass relation.""")

print("\n" + "="*80)
print("WHAT THE SWEEP'S FIRST QUESTION RETURNED")
print("="*80)
print(f"""  ** P2's CYCLOID CIRCLE AND P3's THALES CIRCLE ARE ONE CONSTRUCTION AT TWO SCALES: a circle
  of radius X centred at (X,0), through 0 and 2X. Verified. And P2's circle IS a Thales circle
  on the diameter [0, 2M] -- every point of it sees that diameter at a right angle (max
  |dot| = {worst:.1e} over 500 points), which is WHY r(z)=M(1+cos z) has its two critical
  points where it does. ** Neither paper says so. P2 calls it "the rim of a rolling circle";
  P3 calls it "the hole translated onto its own edge." They are the same circle.

  ** AND THE DIAMETERS ARE NOT THE SAME PAIR, WHICH IS THE FINDING: **
      P2's diameter [0, 2M] spans the geometry's own two critical points -- the horizon and
      the r=0 locus -- which P2 proves are of IDENTICAL analytic character.
      P3's diameter [0, 2alpha] spans the throat's centre and the HINGE -- a point of the
      geometry and an observer's pivot, which are NOT of identical character.
  >>> ONE CONSTRUCTION, ONCE ON EACH SIDE OF THE CORPUS'S OWN GEOMETRY/VANTAGE PARTITION.
      P2's is intrinsic; P3's is perspectival. <<<

  ** AND THE IDENTIFICATION IS REFUTED BY P3's OWN MASS RELATION, not by taste: ** 2M = 2alpha
  would need r0 - r0^3 = 1, and |2M| is capped at 2/(3 sqrt3) = {mx:.4f} (the Nariai maximum).
  ** No slicing makes P2's circle P3's. ** The mass is bounded; the throat is not.

  ⚠ BOUNDED (face 35): this receipt quantifies over the TWO CIRCLES' GEOMETRY. It establishes
  a shared construction and refutes an identification. It says nothing about whether the
  shared construction MEANS anything -- that would need a route from P2's critical points to
  P3's hinge, and none is computed here.""")
