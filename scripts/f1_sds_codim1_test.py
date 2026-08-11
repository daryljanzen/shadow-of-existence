import sympy as sp
# ============================================================================
# Does SdS embed as a codim-1 slice of the substrate dS5?  (the tilt route to
# the F1 term-for-term step: would make the offset a literal so(5,1) motion.)
# Gauss test for a codim-1 hypersurface in a constant-curvature ambient K0=1/al^2:
#   R_abcd(SdS) - K0(g_ac g_bd - g_ad g_bc) = K_ac K_bd - K_ad K_bc   (single K)
# Correct Lorentzian signature in the K0 subtraction (eta=diag(-1,1,1,1));
# restricted to the static region f>0; with dS4 and Schwarzschild limit checks.
# (Supersedes the first run, whose timelike-pair signs were unreliable.)
# ============================================================================
r, th, M, al = sp.symbols('r theta M alpha', positive=True)
f  = 1 - 2*M/r - r**2/al**2
K0 = 1/al**2
g  = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)          # SdS, signature -+++
gi = g.inv(); co = [sp.Symbol('t'), r, th, sp.Symbol('phi')]; n = 4
Gam = [[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],co[c])+sp.diff(g[d,c],co[b])
        -sp.diff(g[b,c],co[d]))for d in range(n))/2)for c in range(n)]for b in range(n)]for a in range(n)]
def Rm(a,b,c,d):
    return sp.simplify(sp.diff(Gam[a][b][d],co[c])-sp.diff(Gam[a][b][c],co[d])
        +sum(Gam[a][c][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][b][c] for e in range(n)))
def Rlow(a,b,c,d): return sp.simplify(sum(g[a,e]*Rm(e,b,c,d) for e in range(n)))
absg = [sp.Abs(g[i,i]) for i in range(n)]                 # |g_aa|; static region f>0
eta  = [-1, 1, 1, 1]                                      # Lorentzian signature factors
def Mpair(a,b):
    # orthonormal (ab,ab) Riemann minus the constant-curvature ambient piece,
    # K0*(eta_a eta_b) -- the signature factor the first run omitted
    raw = Rlow(a,b,a,b)/(absg[a]*absg[b]) - K0*eta[a]*eta[b]
    return sp.simplify(raw.subs(sp.Abs(f), f))            # f>0 (static region)
Mtr, Mtth, Mrth, Mthph = Mpair(0,1), Mpair(0,2), Mpair(1,2), Mpair(2,3)
# decomposability for a diagonal K=diag(k_t,k_r,k_a,k_a):
#   M_tr=k_t k_r, M_tth=k_t k_a, M_rth=k_r k_a, M_thph=k_a^2
#   single K exists  <=>  M_tr*M_thph == M_tth*M_rth
cond = sp.simplify(Mtr*Mthph - Mtth*Mrth)
A = 2*M*al**2 - al**2*r + r**3                            # cubic arg = -al^2 r f < 0 (static)
cond_static = sp.factor(sp.simplify(cond.subs(sp.Abs(A), -A)))
print("Gauss decomposability  M_tr*M_thph - M_tth*M_rth :")
print("   raw          :", cond)
print("   static (f>0) :", cond_static, "   (=0 would mean SdS is codim-1 in dS5)")
print("\nlimit checks (on the raw cond):")
print("   dS4   (M=0)        :", sp.simplify(cond.subs(M,0)), " -> 0: de Sitter IS a codim-1 slice (totally geodesic)")
print("   Schwarzschild (a->oo):", sp.simplify(sp.limit(cond.subs(sp.Abs(A), -A), al, sp.oo)),
      " -> -3M^2/r^6: the known class-2 obstruction (sign check)")
print("""
RESULT.  cond = -3 M^2 / r^6 != 0 in the static region: SdS does NOT embed as a
codim-1 slice of dS5 -- it is embedding class 2 (needs two extra dimensions).
Lambda drops out entirely; the obstruction is the mass term alone, identical to
plain Schwarzschild (the a->oo limit). The vacuum (M=0) IS a clean codim-1 slice.
So the offset -> SdS is NOT a literal codim-1 tilt of a dS5 slice; the tilt route
to the F1 term-for-term step holds only for the vacuum. dS4 = {chi=pi/2} of dS5
(totally geodesic, lift=chi) is in scripts/f1_4d_in_5d_slice.py.
""")
