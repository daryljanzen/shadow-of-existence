import sympy as sp

print("="*78)
print("ANCHOR — stress/evolution sector (ij). Completes the matter functional:")
print("  energy (perp-perp)  rho   = leaf bend          [Hamiltonian constraint, done]")
print("  momentum (perp-i)   j_i   = shift departure     [momentum constraint, r148]")
print("  stress (ij)         S_ij  = stacking departure  [this: G_ij = ADM evolution]")
print("Grounding the ij sector by recovering the operator paper's lapse split from scratch.")
print("="*78)

r, th, A, f, M, al = sp.symbols('r theta A f M alpha', positive=True)
A = sp.Function('A')(r); f = sp.Function('f')(r)
coords=[sp.Symbol('t'), r, th, sp.Symbol('phi')]
g = sp.diag(-A, 1/f, r**2, r**2*sp.sin(th)**2)
ginv=g.inv()
def einstein_mixed(g,ginv,X):
    n=4
    Ga=[[[sp.simplify(sum(ginv[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric=sp.zeros(n,n)
    for b in range(n):
        for c in range(n):
            s=0
            for a in range(n):
                s+=sp.diff(Ga[a][b][c],X[a])-sp.diff(Ga[a][b][a],X[c])
                for d in range(n):
                    s+=Ga[a][a][d]*Ga[d][b][c]-Ga[a][c][d]*Ga[d][b][a]
            Ric[b,c]=sp.simplify(s)
    Rs=sp.simplify(sum(ginv[a,b]*Ric[a,b] for a in range(n) for b in range(n)))
    Gmix=sp.simplify(ginv*(Ric-sp.Rational(1,2)*g*Rs))
    return Gmix
Gm=einstein_mixed(g,ginv,coords)
Lam=3/al**2
# G^mu_nu + Lam delta = 8pi T^mu_nu ; T^t_t=-rho, T^r_r=p_r, T^th_th=p_t
rho = sp.simplify(-(Gm[0,0]+Lam)/(8*sp.pi))
p_r = sp.simplify((Gm[1,1]+Lam)/(8*sp.pi))
p_t = sp.simplify((Gm[2,2]+Lam)/(8*sp.pi))
print("\n[1] energy density   8pi rho  =", sp.simplify(8*sp.pi*rho))
print("[2] radial pressure  8pi p_r  =", sp.simplify(8*sp.pi*p_r))

print("\n[3] operator-paper lapse split: verify 8pi(p_r+rho) = (f/r) d_r ln(A/f).")
lhs = sp.simplify(8*sp.pi*(p_r+rho))
rhs = sp.simplify(f/r*sp.diff(sp.log(A/f), r))
print("    8pi(p_r+rho) - (f/r)d_r ln(A/f) =", sp.simplify(lhs-rhs), " (0 => matches operator paper)")

print("\n[4] locked construction gauge A=f: p_r = -rho ?")
lock = sp.simplify((p_r+rho).subs(sp.Function('A')(r), f).doit())
print("    (p_r+rho)|_{A=f} =", lock, " (0 => p_r=-rho, the locked equation of state)")

print("\n[5] tangential pressure 8pi p_t (free lapse) =")
print("   ", sp.simplify(8*sp.pi*p_t))

print("\n" + "="*78)
print("READING (stress sector; completes the anchor):")
print("="*78)
print("""
 - The anchor's ij sector is G_ij = 8pi S_ij, the spatial Einstein tensor = the ADM
   evolution of the leaf's extrinsic curvature. Read by the corpus for the spherical
   class (operator sec:lapse) and recovered here from scratch: energy density rho is the
   LEAF's bend (spatial profile f alone); radial pressure is the STACKING's departure
   from the leaf, 8pi(p_r+rho)=(f/r)d_r ln(A/f), zero exactly when the lapse is locked to
   the leaf (A=f -> p_r=-rho, vacuum-Lambda its kernel) and general when the lapse is
   freed. So matter STRESS = the stacking's (lapse's) departure -- the third operator
   datum, the time-spacing of the leaves -- exactly as energy = leaf bend and momentum =
   shift departure.
 - THE ANCHOR CLOSES. The full matter functional of the cut, T^a_b as a functional of the
   four data, is now assembled sector by sector and each verified against the corpus:
       leaf   (spatial cut)   -> energy   rho   (the bend; Hamiltonian constraint)
       shift  (frame-drag)    -> momentum j_i   (the shift's departure; r148)
       lapse  (time-stacking) -> stress   S_ij  (the stacking's departure; here)
       vantage(radial sig.)   -> signature       (hole vs cosmos; operator sec:dictionary)
   Energy and momentum are the constraints (initial data); stress is the evolution. The
   spherical instance is the operator paper's leaf/lapse/vantage split with the shift
   turned off; the general anchor adds the shift (momentum) and states all four as one
   functional of the cut. HONEST SCOPE: the general ij sector is the ADM evolution with
   the CR reading; verified here on the static spherical class (recovering operator
   sec:lapse exactly) and consistent with the cosmology (E=1 dust: p=0, the pressureless
   bend, operator eq:friedmann). The non-spherical explicit stress functionals
   (range sec:open item 2) and the dS5-slicing restriction remain.
""")
