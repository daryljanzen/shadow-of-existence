"""D3 — SEGRE.  The Segre symbol classifies a PENCIL of quadrics by the elementary divisors of
lambda A + mu B.  So the probe needs an honest answer to: DOES THE CORPUS HAVE TWO QUADRICS IN ONE
SPACE?  Confirmation 4, before anything runs.  Candidates, each checked:"""
import numpy as np, sympy as sp
print("="*78); print("D3 — SEGRE: IS THERE A SECOND QUADRIC?"); print("="*78)
print("""
  CANDIDATE 1 — the substrate eta(X,X)=alpha^2 and the absolute eta(X,X)=0.
    Homogenised in P^5 with X6:  Q_sub = eta(X,X) - alpha^2 X6^2 ,  Q_abs = eta(X,X).
    The pencil they span is  a.eta + b.X6^2  -- so its second generator is X6^2, a DOUBLE HYPERPLANE
    of RANK ONE.  A pencil containing a rank-1 member is the degenerate end of the Segre table, and
    the pair is not two quadrics in general position: it is one quadric and the hyperplane at infinity.
    *** That is not a Segre problem. It is the CAYLEY-KLEIN setup, which Q3 already identified. ***

  CANDIDATE 2 — the horizon locus, prop:locus:  (r - r_0)(r^2 + r.r_0 + r_0^2 - 1) = 0.
    A LINE times a CONIC is a REDUCIBLE CUBIC, not a pencil of conics.  Q5 already read its singular
    points (the two Nariai).  *** Not a Segre problem either. ***

  CANDIDATE 3 — the two concentric circles of the hinge figure: the THROAT |x|^2 = alpha^2 and the
    hinge triangle's CIRCUMCIRCLE |x|^2 = 4.alpha^2.  Two genuine conics in one plane.  THIS is a pencil.
""")
x,y,z,lam=sp.symbols('x y z lambda')
A=sp.Matrix([[1,0,0],[0,1,0],[0,0,-1]])          # x^2+y^2-z^2  (throat, alpha=1, homogeneous)
B=sp.Matrix([[1,0,0],[0,1,0],[0,0,-4]])          # x^2+y^2-4z^2 (circumcircle)
print("STEP 1 — the pencil A + lambda B, and its degenerate members:")
M=A+lam*B
det=sp.factor(sp.det(M))
print("   det(A + lambda B) =", det)
roots=sp.solve(sp.Eq(det,0), lam)
print("   degenerate at lambda =", roots)
for r in roots:
    Mr=sp.Matrix(M.subs(lam,r))
    print(f"     lambda={r}:  rank = {Mr.rank()},  matrix diag = {[sp.simplify(Mr[i,i]) for i in range(3)]}")
print("""
STEP 2 — READ IT, from the computation and not past it.  det(A + lambda B) = -(lambda+1)^2 (4 lambda + 1),
  so the pencil has TWO degenerate members, not one:
    lambda = -1   (a DOUBLE root):  rank 1, the form 3.z^2  --  THE LINE AT INFINITY, DOUBLED.
    lambda = -1/4 (a simple root):  rank 2, the form (3/4)(x^2+y^2)  --  the two isotropic lines
                                    through the common centre.
  A pencil whose most degenerate member is the doubled line at infinity is the classical signature of
  CONCENTRIC circles: the two conics are bitangent there, at the circular points.
""")
print("STEP 3 — DOES THAT SAY ANYTHING THE CORPUS DOES NOT HAVE?")
print("   [(1,1),1] says: the two circles touch at the circular points, i.e. they are CONCENTRIC.")
print("   The corpus already says they are concentric -- the throat is the incircle of the hinge")
print("   triangle and the circumradius is 2.alpha, both about the same axis (prop:twoalpha).")
print("   *** SO SEGRE RETURNS THE CONCENTRICITY THE CONSTRUCTION STARTED FROM. NO BITE. ***")

print("""
STEP 4 — AND THE BOUNCE HAS A REASON, which is the result.
  Every conic the construction owns is built FROM THE ONE THROAT: the throat itself (radius alpha),
  the hinge circumcircle (2.alpha, an OUTPUT of the throat -- 'the circle on its own edge through its
  own centre'), the contact triangle's circumcircle (the throat again), its incircle (alpha/2).
  All concentric, all coaxial with the substrate's own axis.
  *** SO THE CORPUS HAS NO PENCIL IN GENERAL POSITION, AND CANNOT: a second quadric independent of
      the first would be a second scale, and the construction has ONE. ***
  Segre classifies the relative position of two quadrics.  Where the second is manufactured from the
  first, the classification returns the manufacture.  THAT is why it does not bite -- and it is the
  same fact as Q3's 'the scale is the only free constant a Cayley-Klein construction carries', met
  from the pencil side.
""")
print("="*78)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  STEP 1's determinant, its two degenerate members and their ranks
# were printed and read by eye; STEP 2's Segre reading [(1,1),1] was then asserted in prose.
# Pinned here: the determinant itself, the root multiplicities (2 and 1 -- the DOUBLE root is the
# whole content), the ranks 1 and 2, the rank-1 member's form 3.z^2 (the doubled line at
# infinity), and the elementary-divisor structure that IS the symbol [(1,1),1].  Plus a control:
# a NON-concentric second circle breaks the double root, so the symbol is not an artefact.
assert sp.simplify(det - (-(lam + 1)**2*(4*lam + 1))) == 0
mult = sp.roots(sp.Poly(det, lam))
assert mult == {sp.Integer(-1): 2, sp.Rational(-1, 4): 1}
M_double = sp.Matrix(M.subs(lam, -1))
M_simple = sp.Matrix(M.subs(lam, sp.Rational(-1, 4)))
assert M_double.rank() == 1 and M_simple.rank() == 2
assert sp.simplify(M_double - sp.diag(0, 0, 3)) == sp.zeros(3, 3)          # the form 3.z^2
assert sp.simplify(M_simple - sp.diag(sp.Rational(3, 4), sp.Rational(3, 4), 0)) == sp.zeros(3, 3)
# [(1,1),1]: at the double root the rank drops by TWO (a 2-dimensional kernel -> two elementary
# divisors of degree 1 in one bracket), at the simple root by one.
assert M_double.nullspace().__len__() == 2 and M_simple.nullspace().__len__() == 1
# CONTROL: displace the second circle off the common centre -- (x-1/2)^2 + y^2 = 4 -- and the
# double root must disappear, i.e. the [(1,1),1] symbol is the CONCENTRICITY and not the pencil.
B_off = sp.Matrix([[1, 0, sp.Rational(-1, 2)], [0, 1, 0], [sp.Rational(-1, 2), 0, sp.Rational(-15, 4)]])
mult_off = sp.roots(sp.Poly(sp.det(A + lam*B_off), lam))
assert max(mult_off.values()) == 1 and len(mult_off) == 3
print("  [r2376+c54.161] det(A+lam B) = -(lam+1)^2(4 lam+1) asserted, with multiplicities {-1:2,")
print("  -1/4:1}, ranks 1 and 2, the doubled line at infinity 3.z^2, and an off-centre control")
print("  whose double root disappears -- so [(1,1),1] IS the concentricity.")
