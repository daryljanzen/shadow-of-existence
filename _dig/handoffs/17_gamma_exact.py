import sympy as sp
a = sp.symbols('a', positive=True)
u = sp.Function('u')

# The minisuperspace KINETIC operator is  T = (2*pi/3) * p_a^2 / a   (H_phys line 373).
# Quantize p_a^2/a with an ORDERING. The natural (s-)ordering family for p^2/a on the half-line:
#   T_s = (2pi/3) * a^{-s} p_a a^{2s-1} p_a a^{-s}   with p_a = -i d/da,  and the classical symbol
#   is p_a^2/a for every s (the a-powers sum: -s + (2s-1) - s = -1). This is the standard 1-parameter
#   ordering family for a momentum-squared term with an inverse power of a.
# So T_s u = -(2pi/3) a^{-s} d/da ( a^{2s-1} d/da ( a^{-s} u ) ).
s = sp.symbols('s', real=True)
def T_s(expr):
    return -a**(-s)*sp.diff(a**(2*s-1)*sp.diff(a**(-s)*expr, a), a)   # drop 2pi/3 prefactor; it scales, not shape

# geodesic coordinate: kinetic metric ds^2 ~ (1/a) da^2  => proper length x = int a^{-1/2} da = 2 a^{1/2}.
# Wait: the operator p_a^2/a corresponds to a 1D "metric" G(a) with Laplacian ~ (1/sqrt|G|) d(sqrt|G| G^{-1} d).
# For kinetic K = (1/2) G^{-1} p^2 with G^{-1} ~ 1/a, i.e. G ~ a. Geodesic (flat) coordinate x: dx = sqrt(G) da = sqrt(a) da
#  => x = (2/3) a^{3/2}, i.e. x ∝ a^{3/2}  (matches the paper's stated x ∝ a^{3/2}). Good.
x = sp.symbols('x', positive=True)
# a in terms of x:  x = (2/3) a^{3/2} => a = (3x/2)^{2/3}
a_of_x = (sp.Rational(3,2)*x)**sp.Rational(2,3)

# Transform T_s to the x-coordinate AND to the flat L^2(dx) measure (unitary map u = J * v with the
# Jacobian that flattens the measure). Standard result: an operator -(1/w) d/da (p(a) d/da) on L^2(w da)
# is unitarily equivalent, in the flat coordinate x with dx = sqrt(w/p) da and after the measure-flattening
# similarity, to -d^2/dx^2 + V(x). Let me just do the full reduction numerically/symbolically:
# Write T_s in Sturm-Liouville form -(1/W) (P u')' with:
#   T_s u = -a^{-s} ( a^{2s-1} (a^{-s} u)' )'.  Expand:
uu = sp.Function('u')(a)
Tu = -a**(-s)*sp.diff(a**(2*s-1)*sp.diff(a**(-s)*uu, a), a)
Tu = sp.expand(sp.simplify(Tu))
# collect as A(a) u'' + B(a) u' + C(a) u
upp = sp.diff(uu,a,2); up = sp.diff(uu,a)
A = sp.simplify(Tu.coeff(upp))
B = sp.simplify(Tu.coeff(up))
Ccoef = sp.simplify((Tu - A*upp - B*up)/uu)
print("T_s u = A u'' + B u' + C u   with")
print("  A(a) =", A)
print("  B(a) =", B)
print("  C(a) =", sp.simplify(Ccoef))

# The Schrodinger reduction: for -A u'' - B u' - C u  (note A here is negative: A = -a^{2s-1-2s}=-a^{-1})
# put in the form  T = -A ( u'' + (B/A) u' + (C/A) u ). Since A = -1/a:
print("\n  A simplifies to:", sp.simplify(A), " (= -1/a, so leading symbol p^2/a ✓)")

# Reduce -(1/w) (P u')' form: here P = a^{2s-1}, w = a^{s}*a^{s} = a^{2s}? Actually the measure making T_s
# symmetric is L^2(a^{... } da). For T_s = -a^{-s}(a^{2s-1}(a^{-s} u)')' the natural measure is da (flat in a)
# with the a^{-s} similarity folded in. Cleanest: T_s is unitarily equiv (via u=a^{-s} v ... ) let's just
# directly bring -A u'' - B u' to Liouville normal form and read gamma.
# Liouville normal form of  L = -(u'' + (B/A) u') : substitute u = mu(a) v, choose mu to kill first-deriv,
# then change variable to x. The resulting potential's inverse-square coefficient near a=0 (x->0) is gamma.
P = B/A   # coefficient of u' after dividing by A
P = sp.simplify(P)
print("\n  after dividing by A: u'' + p1 u' + p0 u = 0 form, p1 =", P)
# kill first derivative: u = exp(-1/2 ∫ p1 da) v
half_int = sp.simplify(sp.integrate(P/2, a))
print("  integrating factor exponent -1/2∫p1 =", sp.simplify(-half_int))
# potential shift from de-first-derivative:  Q = p0 - (1/2)p1' - (1/4)p1^2   (in the a-variable, then map to x)
p0 = sp.simplify(Ccoef/A)
Q_a = sp.simplify(p0 - sp.diff(P,a)/2 - P**2/4)
print("  Q(a) [potential in a-var, pre x-map] =", sp.simplify(Q_a))

# Now change to geodesic x with dx = sqrt(w/P_SL) da; for the p^2/a operator the flat coordinate is x∝a^{3/2}.
# Under a change of independent variable to x (where -d^2/dx^2 is the flat Laplacian), the inverse-square
# coefficient is read from the a->x map. The robust way: the geodesic coordinate makes the SECOND-order
# operator -d^2/dx^2, and the inverse-square coefficient gamma is a CONFORMAL INVARIANT computable as:
#    gamma = lim_{x->0} x^2 * V_eff(x)
# where V_eff is the full Schrodinger potential in x. Let me construct V_eff(x) directly by the standard
# formula for reducing -(1/m(a)) d/da(1/... ) ... Instead use the cleanest known route:
# For T = -a^{-s} d/da a^{2s-1} d/da a^{-s}, the substitution to x=(2/3)a^{3/2}, u = a^{-1/4} w (the
# a^{-1/4} flattens the a^{1/2} measure Jacobian) gives -d^2/dx^2 + gamma/x^2 with a computable gamma(s).
# Do it fully:
xx = sp.symbols('x', positive=True)
a_x = (sp.Rational(3,2)*xx)**sp.Rational(2,3)
w = sp.Function('w')(xx)
# u(a) with a=a(x); and u = a(x)^{-1/4} * w(x)? The measure: T_s symmetric on L^2(da) after the a^{-s}
# similarity means we want flat L^2(dx). da = ? dx: x=(2/3)a^{3/2} => dx = a^{1/2} da => da = a^{-1/2} dx.
# So L^2(da) = L^2(a^{-1/2} dx); flatten with u = a^{1/4} w. Compose everything:
u_expr = a_x**(sp.Rational(1,4)) * w
# Apply T_s (in a) to u_expr, then express in x, then divide by a_x^{1/4} to read operator on w.
# Build T_s as differential op in a acting on u_expr(a(x)): use chain rule via substitution a->a_x.
# Easier: compute T_s symbolically on a test u(a), then substitute u=a^{1/4}(x) w(x) with a=a_x and da->dx.
# Represent u(a) generic, get A u'' + B u' + C u, then substitute the x-forms.
da_dx = sp.diff(a_x, xx)  # = a^{-1/2}... check
u_of_x = a_x**sp.Rational(1,4)*w
u_a  = u_of_x
u_a1 = sp.diff(u_of_x, xx)/da_dx                  # du/da = (du/dx)/(da/dx)
u_a2 = sp.diff(u_a1, xx)/da_dx                     # d2u/da2
Top = (A.subs(a,a_x))*u_a2 + (B.subs(a,a_x))*u_a1 + (Ccoef.subs(a,a_x))*u_of_x
# operator on w: divide by the similarity factor a_x^{1/4}
Ow = sp.simplify(Top / a_x**sp.Rational(1,4))
Ow = sp.expand(sp.simplify(Ow))
# Ow should look like -(2pi/3 dropped) [ w'' *(-1) + gamma/x^2 w + (marginal from -Λ term absent here) ]
wpp = sp.diff(w,xx,2); wp=sp.diff(w,xx)
Aw = sp.simplify(Ow.coeff(wpp)); Bw=sp.simplify(Ow.coeff(wp))
Cw = sp.simplify((Ow - Aw*wpp - Bw*wp)/w)
print("\n  operator on w(x):  Aw w'' + Bw w' + Cw w")
print("   Aw =", Aw, "  (want const, = -1 up to overall scale => -d^2/dx^2)")
print("   Bw =", sp.simplify(Bw), "  (want 0 => no first derivative)")
print("   Cw =", sp.simplify(Cw))
gamma_s = sp.simplify(Cw * xx**2 / Aw)   # coefficient of 1/x^2 relative to the w'' term
print("\n  gamma(s) = (coeff of 1/x^2)/(coeff of -w'') =", sp.simplify(gamma_s))
# maximize over s
gs = sp.simplify(gamma_s)
dgs = sp.diff(gs, s)
crit = sp.solve(dgs, s)
print("  d gamma/ds = 0 at s =", crit, "-> gamma_max =", [sp.simplify(gs.subs(s,c)) for c in crit])
for sv in [0, sp.Rational(1,2), 1, sp.Rational(3,2), 2]:
    print(f"    s={sv}: gamma={sp.nsimplify(gs.subs(s,sv))}")
