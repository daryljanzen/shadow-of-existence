"""
P08_matter_functional.py -- verifies P8's matter functional, vacuum kernel, and density-is-the-bend, by
  DERIVING the Einstein tensor of the construction gauge ds^2=-f dt^2+dr^2/f+r^2 dOmega^2 from scratch:
    (i)  8pi T^t_t = 8pi T^r_r = (r f' + f - 1)/r^2 + Lambda   [eq:Ttt] and 8pi T^th_th=f''/2+f'/r+Lambda [eq:Ttheta]
    (ii) the lock g_tt g_rr=-1 forces T^t_t = T^r_r identically (p_r=-rho) for EVERY f;
    (iii)[thm:kernel] T_munu=0  <=>  r f'+f-1+Lambda r^2=0, whose GENERAL solution is SdS f=1-2M/r-Lambda r^2/3;
    (iv) [prop:bend] with a mass function f=1-2m(r)/r-Lambda r^2/3, 8pi T^t_t=-2m'/r^2, i.e. rho=m'/(4 pi r^2).
  [P8 slicing_operator sec:gauge/sec:kernel/sec:bend]
STATUS: ✔✔   RUN: python3 P08_matter_functional.py   RUNTIME: ~8s
CONTROL: a straight cut (m'=0) is vacuum; a bent cut (m'!=0) has rho=m'/(4 pi r^2) != 0 (density IS the bend).
ORIGIN: built new r1359 (P8 cited no receipts).
LEVEL: PRE-LEVEL -- this receipt PRODUCES the level distinction rather than computing on one.
  Einstein's equations applied to the construction gauge; no rate, no density parameter, no scale
  factor enters. G=8piT -> the vacuum kernel is the SdS family, two constants and no more.
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
t,r,th,ph,Lam = sp.symbols('t r theta phi Lambda', real=True)
f = sp.Function('f')(r)
x=[t,r,th,ph]
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
gi = g.inv()
n=4
# Christoffel
Gamma=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],x[c])+sp.diff(g[d,c],x[b])-sp.diff(g[b,c],x[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
# Ricci
def ricci(b,c):
    return sp.simplify(sum(sp.diff(Gamma[a][b][c],x[a]) for a in range(n))
                       - sum(sp.diff(Gamma[a][b][a],x[c]) for a in range(n))
                       + sum(Gamma[a][a][d]*Gamma[d][b][c] for a in range(n) for d in range(n))
                       - sum(Gamma[a][c][d]*Gamma[d][b][a] for a in range(n) for d in range(n)))
Ric=sp.Matrix(n,n, lambda i,j: ricci(i,j))
Rs=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
G_dn=sp.simplify(Ric - Rs*g/2)                       # G_{mu nu}
Gud=sp.simplify(gi*G_dn)                              # G^mu_nu
print("="*70); print("P08 matter functional (Einstein tensor of the construction gauge, DERIVED)"); print("="*70)
fp=sp.diff(f,r); fpp=sp.diff(f,r,2)
# (i) 8pi T^t_t and 8pi T^theta_theta
Ttt = sp.simplify(Gud[0,0] + Lam)                    # 8pi T^t_t = G^t_t + Lambda
Tthth = sp.simplify(Gud[2,2] + Lam)
ok&=check("8pi T^t_t = (r f' + f - 1)/r^2 + Lambda   (eq:Ttt, DERIVED)",
          sp.simplify(Ttt - ((r*fp+f-1)/r**2 + Lam))==0)
ok&=check("8pi T^theta_theta = f''/2 + f'/r + Lambda   (eq:Ttheta, DERIVED)",
          sp.simplify(Tthth - (fpp/2 + fp/r + Lam))==0)
# (ii) the lock: T^t_t = T^r_r identically (p_r = -rho)
ok&=check("lock g_tt g_rr=-1 => T^t_t = T^r_r identically (p_r=-rho) for every f",
          sp.simplify(Gud[0,0]-Gud[1,1])==0)
# (iii) thm:kernel -- vacuum ODE + SdS general solution
vac_ode = sp.simplify((Ttt*r**2))                    # =0 gives r f'+f-1+Lambda r^2 ... check equals r f'+f-1+Lam r^2
ok&=check("thm:kernel: T^t_t=0  <=>  r f' + f - 1 + Lambda r^2 = 0  (eq:vacode)",
          sp.simplify(vac_ode - (r*fp+f-1+Lam*r**2))==0)
M=sp.symbols('M'); f_sds=1-2*M/r-Lam*r**2/3
ok&=check("SdS f=1-2M/r-Lambda r^2/3 solves the vacuum ODE", sp.simplify((r*sp.diff(f_sds,r)+f_sds-1+Lam*r**2))==0)
gen=sp.dsolve(sp.Eq(r*fp+f-1+Lam*r**2,0), f)         # general solution
ok&=check("vacuum ODE GENERAL solution is the SdS family (one constant -2M)",
          "C1" in str(gen.rhs) and sp.simplify(gen.rhs - (1 - Lam*r**2/3 + sp.Symbol('C1')/r))==0)
# (iv) prop:bend -- density is the bend
m=sp.Function('m')(r); f_m=1-2*m/r-Lam*r**2/3
Ttt_m=sp.simplify(((r*sp.diff(f_m,r)+f_m-1)/r**2 + Lam))
ok&=check("prop:bend: f=1-2m(r)/r-Lambda r^2/3 => 8pi T^t_t = -2 m'(r)/r^2",
          sp.simplify(Ttt_m - (-2*sp.diff(m,r)/r**2))==0)
rho=sp.simplify(-Ttt_m/(8*sp.pi))
ok&=check("=> rho(r) = m'(r)/(4 pi r^2)", sp.simplify(rho - sp.diff(m,r)/(4*sp.pi*r**2))==0)
# CONTROL: straight cut m'=0 -> vacuum; bent cut m'!=0 -> nonzero density
ok&=check("CONTROL: straight cut m'=0 -> T^t_t=0 (vacuum); bent cut m'!=0 -> rho!=0 (density IS the bend)",
          sp.simplify(Ttt_m.subs(sp.diff(m,r),0))==0 and sp.simplify(rho.subs(sp.diff(m,r),1))!=0)
print("="*70)
print("RESULT:", "ALL PASS -- matter functional derived from the Einstein tensor; the lock gives p_r=-rho;\n         vacuum kernel = SdS (general solution); density = m'/(4 pi r^2) is the bend of the cut." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   AND prop:bend EVALUATED ON A CONCRETE BEND, which turns 'density is the bend' into a number.
#   A uniform-density cut is m(r) = r^3: then m' = 3 r^2, so 8 pi T^t_t = -2m'/r^2 = -6 at EVERY
#   radius and rho = m'/(4 pi r^2) = 3/(4 pi) = 0.238732414637843, constant -- the interior
#   Schwarzschild ball, and the bend is uniform because the density is.
_Ttt_ball = sp.simplify(Ttt_m.subs(m, r**3).doit())
assert sp.simplify(_Ttt_ball + 6) == 0, _Ttt_ball
assert abs(float(_Ttt_ball) - (-6.0)) < 1e-12, float(_Ttt_ball)
_rho_ball = sp.simplify(rho.subs(m, r**3).doit())
assert sp.simplify(_rho_ball - 3/(4*sp.pi)) == 0, _rho_ball
assert abs(float(_rho_ball) - 0.238732414637843) < 1e-12, float(_rho_ball)
#   and the vacuum kernel's one constant IS -2M: dsolve's C1 in f = 1 - Lambda r^2/3 + C1/r
#   matches SdS at C1 = -2M, so a STRAIGHT cut carries mass and no density.
assert sp.simplify(gen.rhs.subs(sp.Symbol('C1'), -2*M) - f_sds) == 0, gen.rhs
assert sp.simplify(Ttt_m.subs(m, M).doit()) == 0        # m constant -> vacuum, the straight cut
