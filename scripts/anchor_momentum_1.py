import sympy as sp

print("="*78)
print("ANCHOR — momentum sector (CORRECTED: properly linearized in the twist).")
print("Momentum constraint = the perp-i Einstein component, companion of the energy")
print("sector's Hamiltonian constraint. Worked from scratch on a twisted cut.")
print("="*78)

t, r, th, ph, M, al, J, eps = sp.symbols('t r theta phi M alpha J epsilon', positive=True)
w = sp.Function('omega')(r)
f = 1 - 2*M/r - r**2/al**2

coords = [t, r, th, ph]
g = sp.zeros(4,4)
g[0,0] = -f
g[1,1] = 1/f
g[2,2] = r**2
g[3,3] = r**2*sp.sin(th)**2
g[0,3] = g[3,0] = -eps*w*r**2*sp.sin(th)**2     # eps = bookkeeping; linearize to O(eps)
ginv = g.inv()

def christoffel(g, ginv, coords):
    n=len(coords); Ga=[[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s=0
                for d in range(n):
                    s+=ginv[a,d]*(sp.diff(g[d,b],coords[c])+sp.diff(g[d,c],coords[b])-sp.diff(g[b,c],coords[d]))
                Ga[a][b][c]=sp.series(sp.simplify(s/2), eps, 0, 2).removeO()
    return Ga

def ricci(Ga, coords):
    n=len(coords); Ric=sp.zeros(n,n)
    for b in range(n):
        for c in range(n):
            s=0
            for a in range(n):
                s+=sp.diff(Ga[a][b][c],coords[a])-sp.diff(Ga[a][b][a],coords[c])
                for d in range(n):
                    s+=Ga[a][a][d]*Ga[d][b][c]-Ga[a][c][d]*Ga[d][b][a]
            Ric[b,c]=sp.series(sp.expand(s), eps, 0, 2).removeO()
    return Ric

print("\n[1] Einstein G_{t phi}, linearized to O(eps):")
Ga = christoffel(g, ginv, coords)
Ric = ricci(Ga, coords)
Rs = sp.series(sp.expand(sum(ginv[a,b]*Ric[a,b] for a in range(4) for b in range(4))), eps,0,2).removeO()
G_tph = sp.series(sp.expand(Ric[0,3] - sp.Rational(1,2)*g[0,3]*Rs), eps,0,2).removeO()
Lam = 3/al**2
EOM = sp.expand(G_tph + Lam*g[0,3])                       # = 8pi T_{t phi}
# coefficient of eps, strip angular factor
EOM = sp.simplify(sp.diff(EOM, eps).subs(eps,0) / (r**2*sp.sin(th)**2))
print("    (G_{tphi}+Lam g_{tphi})/eps / (r^2 sin^2th) =")
print("   ", sp.simplify(EOM))

print("\n[2] VACUUM frame-drag ODE (numerator = 0):")
ode = sp.simplify(sp.numer(sp.together(EOM)))
ode = sp.simplify(ode / sp.gcd(ode, r))
print("   ", sp.expand(ode), "= 0")

print("\n[3] Verify the general solution omega = C0 + 2J/r^3 on the FULL SdS ODE:")
C0 = sp.Symbol('C0')
for trial,label in [(2*J/r**3,"omega = 2J/r^3 (localized frame-drag, J the angular momentum)"),
                    (C0,"omega = C0 (rigid co-rotation, the homogeneous mode)"),
                    (C0+2*J/r**3,"omega = C0 + 2J/r^3 (general)")]:
    res = sp.simplify(ode.subs(w, trial).doit())
    print(f"    {label}:  residual = {res}")
print("    => exterior frame-drag omega=2J/r^3 holds on the SdS substrate (Lambda cancels");
print("       for the 1/r^3 profile); J is the angular momentum carried by the shift.")
