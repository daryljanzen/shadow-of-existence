import sympy as sp
r, M, al = sp.symbols('r M alpha', positive=True)
A = 2*M*al**2 - al**2*r + r**3          # cubic arg = -alpha^2 r f ; in static region f>0 => A<0
cond = 3*M*(2*M*al**2*r**3 + M*al**2*sp.Abs(A) - al**2*r**4 + r**6 + r**3*sp.Abs(A))/(al**2*r**6*A)
# static region: f>0 => A<0 => |A| = -A
cond_static = sp.simplify(cond.subs(sp.Abs(A), -A))
print("Gauss decomposability in the static region (f>0):")
print("   cond =", cond_static)
print("   factored:", sp.factor(cond_static))
