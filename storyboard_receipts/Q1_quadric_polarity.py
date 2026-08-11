"""Q1, invariant form.  The first pass computed a EUCLIDEAN distance for the polar hyperplane in a
MINKOWSKI space and got 1/sqrt7 = 0.37796 -- a gauge artifact, not an invariant.  Redone with the only
quantity polarity actually depends on: eta(P,P) against alpha^2."""
import numpy as np
a=1.0; eta=np.diag([-1.,1.,1.])
ip=lambda P,Q: P@eta@Q
pts={"throat point":np.array([0,1,0.]), "hinge (X0=+sqrt3,|X|=2a)":np.array([np.sqrt(3),2,0.]),
     "hinge-axis foot (X0=0,|X|=2a)":np.array([0,2,0.]), "Nariai radius pt":np.array([0,1/np.sqrt(3),0.]),
     "r=0 origin":np.array([0,0,0.])}
print("="*76); print("Q1 (invariant) — classification by eta(P,P) vs alpha^2, the ONLY thing polarity depends on")
print("="*76)
print(f"{'point':32s} {'eta(P,P)':>10s} {'position':>10s}  {'polar':s}")
for l,P in pts.items():
    e=ip(P,P); pos = "ON" if abs(e-a*a)<1e-12 else ("OUTSIDE" if e>a*a else "INSIDE")
    pol = {"ON":"tangent hyperplane at P","OUTSIDE":"real chord of contact","INSIDE":"no real contact"}[pos]
    print(f"{l:32s} {e:10.5f} {pos:>10s}  {pol}")
print("\n"+"-"*76)
print("THE ONE STRUCTURAL FACT: the HINGES LIE ON THE QUADRIC.  -3 + 4 = 1.")
print("  eta(hinge,hinge) = -(sqrt3 a)^2 + (2a)^2 = -3a^2 + 4a^2 = a^2.  So each hinge is a substrate point,")
print("  and its polar is the TANGENT HYPERPLANE there -- not a new object.")
print("\nAND THE 'sqrt3' TEST -- is the tangent length from the hinge-axis foot a NEW relation?")
foot=pts["hinge-axis foot (X0=0,|X|=2a)"]
pw = foot[1:]@foot[1:] - a*a
print(f"  pow_throat(foot) = |X|^2 - a^2 = {pw:.5f};  tangent length = sqrt(pow) = {np.sqrt(pw):.6f} = sqrt3 a")
print(f"  the hinge's HEIGHT is X0 = {np.sqrt(3):.6f} = sqrt3 a  -- the same number.")
print("  MECHANISM? YES, and it is p0's: for a point ON the quadric, pow_throat = X0^2 (eq:powerisheight).")
print("  The hinge is on the quadric at transverse 2a, so X0^2 = 4a^2 - a^2 = 3a^2 forces X0 = sqrt3 a.")
print("  => NOT a new relation.  It is eq:powerisheight evaluated at the hinge.  CONFIRMS.")
print("\n"+"="*76)
print("VERDICT Q1: CONFIRMS.  Polarity w.r.t. the quadric returns, at every named point, what")
print("  eq:powerisheight already gives -- because that identity IS the quadric's equation, which")
print("  p0 states.  rho58's bound therefore EXTENDS from the plane to the projective setting:")
print("  the quadric's polarity carries no height the throat's power does not already carry.")
print("="*76)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS, and they CONSTRUCT the polar.  The table above reads "tangent
# hyperplane at P" out of a dict keyed on the sign of eta(P,P) - alpha^2; no polar hyperplane is
# ever built, so the word "tangent" is a label.  Here the polar { X : eta(P,X) = alpha^2 } is
# written down for the hinge and for the hinge-axis foot, and the tangency is COMPUTED: for the
# hinge (ON the quadric) the quadric restricted to any line inside the polar has a DOUBLE root
# at the hinge, and the section is a degenerate conic (rank 2 -- the two rulings through it);
# for the foot (OUTSIDE) the section is a nondegenerate REAL conic and its points are genuine
# contact points.  The classification eta-values are pinned too.
import sympy as sp
E = sp.diag(-1, 1, 1)
Xs = sp.Matrix(sp.symbols('Xa Xb Xc', real=True))
qf = lambda U, V: (U.T*E*V)[0, 0]
assert abs(ip(pts["throat point"], pts["throat point"]) - 1.0) < 1e-12
assert abs(ip(pts["hinge (X0=+sqrt3,|X|=2a)"], pts["hinge (X0=+sqrt3,|X|=2a)"]) - 1.0) < 1e-12
assert abs(ip(foot, foot) - 4.0) < 1e-12
assert abs(ip(pts["Nariai radius pt"], pts["Nariai radius pt"]) - 1.0/3.0) < 1e-12
assert abs(pw - 3.0) < 1e-12 and abs(np.sqrt(pw) - 1.732051) < 1e-6      # sqrt3 alpha
H = sp.Matrix([sp.sqrt(3), 2, 0])
assert sp.simplify(qf(H, H) - 1) == 0                                    # -3 + 4 = 1: ON
polar_H = sp.expand(qf(H, Xs) - 1)                                       # the hyperplane itself
assert sp.simplify(polar_H - (-sp.sqrt(3)*Xs[0] + 2*Xs[1] - 1)) == 0
assert sp.simplify(polar_H.subs(dict(zip(list(Xs), list(H))))) == 0      # P is on its own polar
tt = sp.Symbol('tt', real=True)
d_sym = sp.Matrix(sp.symbols('da db dc', real=True))
d_in = d_sym.subs(d_sym[0], sp.solve(sp.Eq(qf(H, d_sym), 0), d_sym[0])[0])   # d inside the polar
line_in = sp.Poly(sp.expand(qf(H + tt*d_in, H + tt*d_in) - 1), tt)
assert line_in.coeff_monomial(tt) == 0                                   # DOUBLE root -> tangency
line_off = sp.Poly(sp.expand(qf(H + tt*Xs.subs({Xs[0]: 1, Xs[1]: 0, Xs[2]: 0}),
                                H + tt*Xs.subs({Xs[0]: 1, Xs[1]: 0, Xs[2]: 0})) - 1), tt)
assert sp.simplify(line_off.coeff_monomial(tt)) != 0                     # a direction OFF it: not
def conic_of_section(base, b1, b2):
    """the quadric restricted to the plane base + s b1 + t b2, as a 3x3 conic matrix"""
    ss, uu = sp.symbols('ss uu', real=True)
    Y = base + ss*b1 + uu*b2
    g = sp.expand(qf(Y, Y) - 1)
    z = {ss: 0, uu: 0}
    return sp.Matrix([[sp.diff(g, ss, 2)/2, sp.diff(g, ss, uu)/2, sp.diff(g, ss).subs(z)/2],
                      [sp.diff(g, ss, uu)/2, sp.diff(g, uu, 2)/2, sp.diff(g, uu).subs(z)/2],
                      [sp.diff(g, ss).subs(z)/2, sp.diff(g, uu).subs(z)/2, g.subs(z)]])
C_H = conic_of_section(H, sp.Matrix([2, sp.sqrt(3), 0]), sp.Matrix([0, 0, 1]))
assert sp.simplify(C_H.det()) == 0 and C_H.rank() == 2      # DEGENERATE: the two rulings at H
F = sp.Matrix([0, 2, 0])                                    # the hinge-axis foot, OUTSIDE
C_F = conic_of_section(sp.Matrix([0, sp.Rational(1, 2), 0]), sp.Matrix([1, 0, 0]), sp.Matrix([0, 0, 1]))
assert sp.simplify(C_F.det() - sp.Rational(3, 4)) == 0 and C_F.rank() == 3   # a real conic
T = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2), 1])    # a REAL point of the chord of contact
assert sp.simplify(qf(T, T) - 1) == 0 and sp.simplify(qf(F, T) - 1) == 0
line_FT = sp.Poly(sp.expand(qf(T + tt*(F - T), T + tt*(F - T)) - 1), tt)
assert line_FT.coeff_monomial(tt) == 0                      # the line foot->T touches AT T
print("  [r2376+c54.161] the polar hyperplane is now BUILT, not labelled: eta(hinge,X) = alpha^2")
print("  touches the quadric doubly at the hinge and cuts it in a rank-2 (degenerate) section,")
print("  while the foot's polar cuts a real conic whose points are genuine contact points.")
