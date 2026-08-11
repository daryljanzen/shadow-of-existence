import sympy as sp

M, z, r, l, alpha = sp.symbols('M z r l alpha', positive=True)

print("="*70)
print("1. THE CURVE (Paper 2): r(z)=M(1+cos z). The two critical points.")
print("="*70)
rz = M*(1+sp.cos(z))
rp = sp.diff(rz,z); rpp = sp.diff(rz,z,2)
for name,zz in [("horizon z=0",0),("centre  z=pi",sp.pi)]:
    print(f"  {name}:  r={rz.subs(z,zz)},  r'={rp.subs(z,zz)},  r''={sp.simplify(rpp.subs(z,zz))}")
print("  -> 1st derivative r' = 0 at BOTH (identical).")
print("  -> 2nd derivative |r''| = M at BOTH (same magnitude, opposite sign).")
print("  -> the ONLY curve-level difference is the VALUE r: 2M vs 0.")

print()
print("="*70)
print("2. CURVATURE IS A FUNCTION OF THE VALUE r. K(z)=48M^2/r(z)^6.")
print("="*70)
Kz = 48*M**2/rz**6
print("  K at z=0 (r=2M):", sp.simplify(Kz.subs(z,0)), " (finite)")
# pole order at z=pi:
w = sp.symbols('w')
ser = sp.series(rz.subs(z, sp.pi+w), w, 0, 5).removeO()
print("  r(pi+w) =", ser, " -> vanishes to 2nd order in w")
Kser = sp.series(Kz.subs(z, sp.pi+w), w, 0, 2)
print("  K(pi+w) leading term:", Kser.as_leading_term(w), " -> 12th-order pole")
print("  pole order = (mult of crit pt = 2) x (power of r in K = 6) = 12  [Paper 2]")

print()
print("="*70)
print("3. SWEPT-LEAF GAUSSIAN CURVATURE  K_G = -f'/(2r),  f=1-2M/r-r^2/alpha^2")
print("   (the surface of revolution the slicing curve generates; r''(l)=f'/2)")
print("="*70)
f = 1 - 2*M/r - r**2/alpha**2
KG = sp.simplify(-sp.diff(f,r)/(2*r))
print("  K_G =", KG, "  = 1/alpha^2 - M/r^3")
print("  -> a function of r with a POLE at r=0, finite at any r=r_h != 0.")
print("  -> same structure as 4D Kretschmann: curvature = (function of r), pole at 0.")

print()
print("="*70)
print("4. THE FIRST DISTINGUISHING INVARIANT IS 2ND-ORDER (no 1st-order invariant)")
print("   Full Schwarzschild: lowest curvature scalars.")
print("="*70)
t,th,ph = sp.symbols('t theta phi')
fr = 1-2*M/r
g = sp.diag(-fr, 1/fr, r**2, r**2*sp.sin(th)**2)
X=[t,r,th,ph]; gi=g.inv()
Gam=[[[sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(4))/2
       for c in range(4)] for b in range(4)] for a in range(4)]
Gam=[[[sp.simplify(Gam[a][b][c]) for c in range(4)] for b in range(4)] for a in range(4)]
def Riem(a,b,c,d):
    t1=sp.diff(Gam[a][b][d],X[c])-sp.diff(Gam[a][b][c],X[d])
    t2=sum(Gam[a][c][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][b][c] for e in range(4))
    return sp.simplify(t1+t2)
Ric=sp.zeros(4)
for b in range(4):
    for d in range(4):
        Ric[b,d]=sp.simplify(sum(Riem(a,b,a,d) for a in range(4)))
Rs=sp.simplify(sum(gi[b,d]*Ric[b,d] for b in range(4) for d in range(4)))
print("  Ricci scalar  R =", Rs, "  (vacuum; 2nd order in g, identical at both pts)")
# Kretschmann
Rlow=[[[[sp.simplify(sum(g[a,e]*Riem(e,b,c,d) for e in range(4))) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
Rup=[[[[sp.simplify(sum(gi[a,e]*gi[b,f]*gi[c,h]*gi[d,k]*Rlow[e][f][h][k] for e in range(4) for f in range(4) for h in range(4) for k in range(4))) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
Kret=sp.simplify(sum(Rlow[a][b][c][d]*Rup[a][b][c][d] for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
print("  Kretschmann   K =", Kret, "  -> FIRST invariant that distinguishes the pts")
print("  K at r=2M:", sp.simplify(Kret.subs(r,2*M)), " finite ;  r->0: pole")
print()
print("  Lowest scalar curvature invariant = Ricci scalar, SECOND order in g.")
print("  There is NO first-order scalar invariant (Christoffels are non-tensorial).")
