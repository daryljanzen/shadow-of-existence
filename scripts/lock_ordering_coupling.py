import sympy as sp

a, x, s, E = sp.symbols('a x s E', positive=True)
f = sp.Function('f'); psi = sp.Function('psi')

# Ordering family for (2pi/3) p_a^2 / a, leading symbol a^{-1} p^2, dropping 2pi/3:
#   T_s f = -a^{-s} D a^{2s-1} D a^{-s} f       (D = d/da);  one ordering per s.
def Ts(expr):
    inner = a**(2*s-1) * sp.diff(a**(-s)*expr, a)
    return -a**(-s) * sp.diff(inner, a)
Tf = sp.simplify(Ts(f(a)).doit())
# collect coefficients of f'', f', f
f2 = sp.Symbol('f2'); f1 = sp.Symbol('f1'); f0 = sp.Symbol('f0')
sub = {sp.Derivative(f(a),a,a):f2, sp.Derivative(f(a),a):f1, f(a):f0}
Tf_c = sp.expand(Tf).subs(sub)
c2 = sp.simplify(Tf_c.coeff(f2)); c1 = sp.simplify(Tf_c.coeff(f1)); c0 = sp.simplify(Tf_c.coeff(f0))
print("T_s f  =  (%s) f''  +  (%s) f'  +  (%s) f" % (c2, c1, c0))

# Geodesic coordinate from leading symbol a^{-1}∂^2:  G_aa = a,  x = ∫sqrt(a)da = (2/3)a^{3/2}
ax = (sp.Rational(3,2)*x)**sp.Rational(2,3)     # a(x)
# Put -c2 f'' - c1 f' - c0 f = E f into standard Schrodinger form -ψ'' + Veff ψ = e ψ
# via a=a(x) and f = J(x) ψ(x), J chosen to kill the ψ' term, kinetic coeff normalized to 1.
# Build the operator coefficients in x:
da_dx = sp.diff(ax, x)
# f'(a) = (1/a'(x)) d/dx,  f''(a) = (1/a'^2) d2/dx2 - (a''/a'^3) d/dx
# Operator  L = -c2 d2/da2 - c1 d/da - c0  (so L f = E f).  Map to x:
A2 = sp.simplify((-c2).subs(a,ax) / da_dx**2)                                  # coeff of ψ_xx
A1 = sp.simplify((-c2).subs(a,ax) * (-sp.diff(ax,x,2)/da_dx**3) + (-c1).subs(a,ax)/da_dx)  # coeff of ψ_x
A0 = sp.simplify((-c0).subs(a,ax))                                              # coeff of ψ
A2 = sp.simplify(A2)
# normalize kinetic to 1: divide through by (-A2_over_-1)... A2 should be const (=-? ) check:
print("kinetic coeff in x (coeff of ψ_xx, want constant):", sp.simplify(A2))
# remove first-derivative term by f=J ψ:  standard Veff = (A1 form) ; do it via Liouville:
# write L = A2 d2/dx2 + A1 d/dx + A0 ; with A2 const. Liouville: ψ=exp(-∫A1/(2A2)dx) χ
J = sp.exp(-sp.integrate(A1/(2*A2), x))
# effective potential for χ:  Veff = A0/A2 ... minus quantum terms; compute directly:
chi = sp.Function('chi')
expr = A2*sp.diff(J*chi(x),x,2) + A1*sp.diff(J*chi(x),x) + A0*(J*chi(x))
expr = sp.simplify(sp.expand(sp.simplify(expr/ (A2*J))))   # divide so leading is chi''
# expr = chi'' + (Veff/?) chi ; collect coeff of chi (the -Veff) 
ch2=sp.Symbol('ch2'); ch1=sp.Symbol('ch1'); ch0=sp.Symbol('ch0')
expr_c = sp.expand(expr).subs({sp.Derivative(chi(x),x,x):ch2, sp.Derivative(chi(x),x):ch1, chi(x):ch0})
pot = sp.simplify(expr_c.coeff(ch0))      # this is -(E-Veff)/.. ; the x-dependent piece is the ordering potential
print("coeff of chi (the inverse-square ordering potential, x->0):", sp.simplify(pot))
# extract gamma in gamma/x^2
gamma = sp.simplify(pot * x**2)
gamma = sp.simplify(sp.limit(pot*x**2, x, 0))
print("\ngamma(s) in  Veff ~ gamma/x^2  near x=0 :", sp.simplify(gamma))
print("gamma = 0  (one-parameter family / BC needed) at s =", sp.solve(sp.Eq(gamma,0), s))
print("gamma = 3/4 (essential self-adjointness threshold) at s =", sp.solve(sp.Eq(gamma,sp.Rational(3,4)), s))
