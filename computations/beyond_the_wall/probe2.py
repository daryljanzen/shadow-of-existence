"""PROBE 2 — the Killing algebra: dimension, structure, orbits."""
import sympy as sp
u,v,x,y = sp.symbols('u v x y', real=True)
hp, hc = sp.cos(u), sp.sin(u)
H = hp*(x**2-y**2) + 2*hc*x*y
X=[u,v,x,y]
g = sp.zeros(4,4); g[0,1]=g[1,0]=1; g[0,0]=H; g[2,2]=1; g[3,3]=1

def killing_residual(xi):
    """Lie_xi g, lowered — must vanish identically."""
    res = sp.zeros(4,4)
    for a in range(4):
        for b in range(4):
            e = sum(xi[c]*sp.diff(g[a,b],X[c]) for c in range(4))
            e += sum(g[c,b]*sp.diff(xi[c],X[a]) for c in range(4))
            e += sum(g[a,c]*sp.diff(xi[c],X[b]) for c in range(4))
            res[a,b] = sp.simplify(sp.expand_trig(sp.simplify(e)))
    return res

# candidate: xi_f = f^a(u) d_a - (fdot_a x^a) d_v, with f satisfying fdd = A f
f1 = sp.Function('f1'); f2 = sp.Function('f2')
xi = [0, -(sp.diff(f1(u),u)*x + sp.diff(f2(u),u)*y), f1(u), f2(u)]
res = killing_residual(xi)
print("Killing residual for the ansatz (before imposing the ODE):")
sp.pprint(sp.simplify(res))
# the surviving component should be exactly the oscillator equation
cond = sp.simplify(res[0,0])
print("\nthe one surviving condition:  ", sp.simplify(cond))
A = sp.Matrix([[hp, hc],[hc, -hp]])
ode = sp.Matrix([sp.diff(f1(u),u,2), sp.diff(f2(u),u,2)]) - A*sp.Matrix([f1(u), f2(u)])
print("the geodesic-deviation ODE  fdd = A f, A = "); sp.pprint(A)
print("condition == -2 * (x,y).(fdd - A f) ? ",
      sp.simplify(cond + 2*(x*ode[0] + y*ode[1])) == 0)

# d_v is Killing
print("\nd_v is Killing:", killing_residual([0,1,0,0]) == sp.zeros(4,4))
