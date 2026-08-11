"""
B-4 / C4: charge as the bend. The slicing operator reads matter as the bend of the cut off the
SdS vacuum kernel; charge is the instance where the bend is the Maxwell electromagnetic field.
Confirm symbolically that RN-dS (Reissner-Nordstrom-de Sitter) has, off the SdS kernel, exactly
the Maxwell stress-energy of a radial electric field -- i.e. the charge Q enters as the EM bend,
not as a vacuum parameter. (Rotation-as-shift, J=Ma, is already P9 prop:kerr; this closes the
charge half of C4, extending the C9 matter-functional collection to the charged class.)
Convention: G_{mu nu} + Lambda g_{mu nu} = 8 pi T_{mu nu}.  rho = -T^t_t, p_i = T^i_i.
"""
import sympy as sp

def ricci_einstein(g, coords):
    n=len(coords); gi=g.inv()
    Gam=[[[sp.simplify(sum(gi[l,m]*(sp.diff(g[m,i],coords[j])+sp.diff(g[m,j],coords[i])
        -sp.diff(g[i,j],coords[m])) for m in range(n))/2) for j in range(n)] for i in range(n)] for l in range(n)]
    Ric=sp.zeros(n)
    for i in range(n):
        for j in range(n):
            Ric[i,j]=sp.simplify(sum(sp.diff(Gam[l][i][j],coords[l]) for l in range(n))
              -sum(sp.diff(Gam[l][i][l],coords[j]) for l in range(n))
              +sum(Gam[l][i][j]*Gam[m][l][m] for l in range(n) for m in range(n))
              -sum(Gam[l][i][m]*Gam[m][j][l] for l in range(n) for m in range(n)))
    R=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
    Ein=sp.Matrix(n,n,lambda i,j: sp.simplify(Ric[i,j]-g[i,j]*R/2))
    return Ein, gi

t,r,th,ph = sp.symbols('t r theta phi', real=True)
M,Q,Lam = sp.symbols('M Q Lambda', positive=True)
pi=sp.pi
f = 1 - 2*M/r + Q**2/r**2 - Lam*r**2/3         # RN-dS metric function
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
Ein, gi = ricci_einstein(g, [t,r,th,ph])

# 8 pi T^mu_nu = (Ein + Lam g) raised
def Tmix(a,b): return sp.simplify(sum(gi[a,c]*(Ein[c,b]+Lam*g[c,b]) for c in range(4)))
rho   = sp.simplify(-Tmix(0,0))     # 8 pi rho
p_r   = sp.simplify( Tmix(1,1))     # 8 pi p_r
p_th  = sp.simplify( Tmix(2,2))     # 8 pi p_theta
print("="*70); print("B-4/C4 :: charge as the bend -- RN-dS stress-energy off the SdS kernel"); print("="*70)
print(f"  8 pi rho     = {rho}")
print(f"  8 pi p_r     = {p_r}")
print(f"  8 pi p_theta = {p_th}")

# Maxwell stress-energy of a radial electric field E_r = Q/r^2 (Gaussian units, G=c=1):
#   rho_EM = Q^2/(8 pi r^4);  T^t_t = T^r_r = -rho_EM ;  T^theta_theta = T^phi_phi = +rho_EM
rho_EM = Q**2/(8*pi*r**4)
print("-"*70)
print("  Maxwell radial-E-field target (E=Q/r^2):")
print(f"    8 pi rho_EM = {sp.simplify(8*pi*rho_EM)}   (= Q^2/r^4)")
print(f"    check  rho (geom)  == +Q^2/r^4 : {sp.simplify(rho - Q**2/r**4)==0}")
print(f"    check  p_r (geom)  == -Q^2/r^4 : {sp.simplify(p_r + Q**2/r**4)==0}   (T^t_t=T^r_r)")
print(f"    check  p_th(geom)  == +Q^2/r^4 : {sp.simplify(p_th - Q**2/r**4)==0}   (transverse +)")
# trace-free check (EM is traceless): -rho + p_r + 2 p_th = 0
print(f"    traceless (-rho+p_r+2p_th=0)   : {sp.simplify(-rho+p_r+2*p_th)==0}")
# vacuum kernel: Q=0 -> T=0
print(f"    vacuum kernel (Q=0) T=0        : {sp.simplify(rho.subs(Q,0))==0 and sp.simplify(p_r.subs(Q,0))==0}")
print("="*70)
print("""VERDICT (B-4/C4 charge closed): RN-dS's departure from the SdS vacuum kernel is EXACTLY the
Maxwell stress-energy of a radial electric field E=Q/r^2 -- the charge is the bend of the cut
(the EM field), traceless, vanishing with Q, off the same SdS kernel C9 read the neutral matter
off. So charge folds into the slicing-curve picture as the electromagnetic instance of matter =
the bend; rotation is the shift (frame-dragging g_{t phi}, J=Ma) already established in P9
prop:kerr. C4 is collected. No new physics -- the P8/P9 bend reading applied to the charged class.""")
