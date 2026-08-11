"""
P09_kerr_deSitter.py -- verifies prop:kerr: Kerr-de Sitter is vacuum-Lambda on the de Sitter substrate,
  R_munu = Lambda g_munu with Lambda=3/alpha^2 (shared throat alpha=sqrt(3/Lambda)); its radial structure
  function decomposes EXACTLY as Delta_r = r^2 f_SdS + a^2 f_dS (f_SdS=1-2M/r-r^2/a^2, f_dS=1-r^2/a^2), with
  Delta_theta=1+(a/alpha)^2 cos^2 theta, Xi=1+(a/alpha)^2, and J=Ma/Xi^2; it reduces to SdS as a->0 and to
  maximally-symmetric (Weyl-flat) de Sitter as M->0. The J=Ma/Xi^2 relation (Komar) is stated, not computed
  here. [P9 range_paper sec:rotation / prop:kerr]
STATUS: ✔✔   RUN: python3 P09_kerr_deSitter.py   RUNTIME: ~10s
COMPUTES: the numeric GR pipeline gives R^mu_nu=Lambda delta at several (r,theta) (vacuum-Lambda to ~1e-5);
  the Delta_r/Delta_theta/Xi decomposition symbolically; a->0 collapses Delta_r to r^2 f_SdS (SdS); M->0 gives
  vanishing Weyl (maximal symmetry). CONTROL: a nonzero M keeps Weyl!=0 (Type D, not maximally symmetric).
ORIGIN: built new r1366 (P9 cited no receipts).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r,th=sp.symbols('r theta', real=True)
# (1) symbolic structure-function decomposition
Ms,as_,als=sp.symbols('M a alpha', positive=True)
Dr_def=(r**2+as_**2)*(1-r**2/als**2)-2*Ms*r
f_SdS=1-2*Ms/r-r**2/als**2; f_dS=1-r**2/als**2
print("="*70); print("P09 Kerr-de Sitter: vacuum-Lambda on the substrate"); print("="*70)
ok&=check("Delta_r = r^2 f_SdS + a^2 f_dS  (exact decomposition, eq:deltadecomp)",
          sp.simplify(Dr_def-(r**2*f_SdS+as_**2*f_dS))==0)
ok&=check("a->0: Delta_r -> r^2 f_SdS = r^2-2Mr-r^4/a^2 (SdS reduction); Delta_theta->1, Xi->1",
          sp.simplify(Dr_def.subs(as_,0)-(r**2-2*Ms*r-r**4/als**2))==0
          and sp.simplify((1+(as_**2/als**2)*sp.cos(th)**2).subs(as_,0)-1)==0
          and sp.simplify((1+as_**2/als**2).subs(as_,0)-1)==0)
# metric builder (Boyer-Lindquist Kerr-dS), numeric pipeline
def metric_f(Mv,av,alv):
    rho2=r**2+av**2*sp.cos(th)**2; Xi=1+av**2/alv**2
    Dr=(r**2+av**2)*(1-r**2/alv**2)-2*Mv*r; Dth=1+(av**2/alv**2)*sp.cos(th)**2
    e1=[sp.Integer(1),0,0,-av*sp.sin(th)**2/Xi]; e2=[av,0,0,-(r**2+av**2)/Xi]
    g=sp.zeros(4,4)
    for i in range(4):
     for j in range(4):
        g[i,j]=-(Dr/rho2)*e1[i]*e1[j]+(Dth*sp.sin(th)**2/rho2)*e2[i]*e2[j]
    g[1,1]+=rho2/Dr; g[2,2]+=rho2/Dth
    return sp.lambdify((r,th), g,'numpy')
def christ(gf,rr,tt,h=1e-6):
    g0=np.array(gf(rr,tt),float); gi=np.linalg.inv(g0); dg=np.zeros((4,4,4))
    dg[1]=(np.array(gf(rr+h,tt),float)-np.array(gf(rr-h,tt),float))/(2*h)
    dg[2]=(np.array(gf(rr,tt+h),float)-np.array(gf(rr,tt-h),float))/(2*h)
    Ga=np.zeros((4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
        Ga[A,b,c]=0.5*sum(gi[A,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c]) for d in range(4))
    return Ga
def riemann(gf,rr,tt,h=1e-5):
    Ga=christ(gf,rr,tt); dGa=np.zeros((4,4,4,4))
    dGa[1]=(christ(gf,rr+h,tt)-christ(gf,rr-h,tt))/(2*h); dGa[2]=(christ(gf,rr,tt+h)-christ(gf,rr,tt-h))/(2*h)
    R=np.zeros((4,4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        R[A,b,c,d]=dGa[c][A,b,d]-dGa[d][A,b,c]+sum(Ga[A,e,c]*Ga[e,b,d]-Ga[A,e,d]*Ga[e,b,c] for e in range(4))
    return R
def ricci_mix(gf,rr,tt):
    R=riemann(gf,rr,tt); Ric=np.einsum('abad->bd',R); gi=np.linalg.inv(np.array(gf(rr,tt),float)); return gi@Ric
def weyl_max(gf,rr,tt):
    R=riemann(gf,rr,tt); g0=np.array(gf(rr,tt),float); gi=np.linalg.inv(g0)
    Rl=np.einsum('ae,ebcd->abcd',g0,R); Ric=np.einsum('abad->bd',R); Rs=float(np.einsum('bd,bd->',gi,Ric))
    Cw=np.zeros((4,4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        Cw[A,b,c,d]=Rl[A,b,c,d]-0.5*(g0[A,c]*Ric[b,d]-g0[A,d]*Ric[b,c]-g0[b,c]*Ric[A,d]+g0[b,d]*Ric[A,c])+Rs/6*(g0[A,c]*g0[b,d]-g0[A,d]*g0[b,c])
    return np.max(np.abs(Cw))
# (2) vacuum-Lambda numeric
gf=metric_f(0.3,0.5,5.0); Lam=3/5.0**2
res=[np.max(np.abs(ricci_mix(gf,rr,tt)-Lam*np.eye(4))) for (rr,tt) in [(3.0,np.pi/3),(4.0,1.0),(2.5,2.0)]]
ok&=check(f"vacuum-Lambda: R^mu_nu = Lambda delta (Lambda=0.12) at 3 points, max resid {max(res):.1e}", max(res)<1e-4)
# (3) M->0 maximally symmetric (Weyl-flat) vs M!=0 (Weyl!=0)
w0=weyl_max(metric_f(0.0,0.5,5.0),3.0,np.pi/3); wM=weyl_max(metric_f(0.3,0.5,5.0),3.0,np.pi/3)
ok&=check(f"M->0: Weyl -> 0 (maximally symmetric de Sitter), max|Weyl|={w0:.1e}; M=0.3 keeps Weyl!=0 ({wM:.3f})",
          w0<1e-4 and wM>1e-2)
# NOTE (honest scope): the angular momentum J=Ma/Xi^2 ("offset times twist") is a Komar/Ashtekar-Das
# surface integral -- a separate computation NOT performed here. This receipt verifies vacuum-Lambda + the
# Delta_r decomposition + the a->0 (SdS) and M->0 (maximally symmetric) limits, which are the checkable core.
print("  [NOTE] J=Ma/Xi^2 is stated (Komar/Ashtekar-Das integral) -- not independently computed in this receipt.")
print("="*70)
print("RESULT:", "ALL PASS -- Kerr-de Sitter is vacuum-Lambda on the substrate (R^mu_nu=Lambda delta); Delta_r=r^2 f_SdS\n         +a^2 f_dS; a->0 gives SdS, M->0 gives maximally-symmetric de Sitter. Rotation is reached." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   THE SUBSTRATE CONSTANT, PINNED: the throat alpha = 5 carries Lambda = 3/alpha^2 = 0.12, so the
#   Ricci scalar of the vacuum-Lambda solution is 4 Lambda = 0.48 -- and the numeric pipeline hits
#   both, at a point away from the axis and away from any horizon.
assert abs(Lam - 0.12) < 1e-12, Lam
_ric = ricci_mix(gf, 3.0, np.pi/3)
assert abs(float(np.trace(_ric)) - 0.48) < 1e-4, np.trace(_ric)
assert np.max(np.abs(_ric - 0.12*np.eye(4))) < 1e-4
assert max(res) < 1e-4, max(res)
#   THE STRUCTURE FUNCTIONS, PINNED at M = 3/10, a = 1/2, alpha = 5:
#     Delta_r(3) = (r^2+a^2)(1-r^2/alpha^2) - 2Mr = 9.25*0.64 - 1.8 = 4.12
#     Xi         = 1 + (a/alpha)^2                                  = 1.01
#     Delta_theta(pi/3) = 1 + (a/alpha)^2 cos^2 theta               = 1.0025
_sub = {Ms: sp.Rational(3, 10), as_: sp.Rational(1, 2), als: sp.Integer(5)}
assert abs(float(Dr_def.subs(_sub).subs(r, 3)) - 4.12) < 1e-12, float(Dr_def.subs(_sub).subs(r, 3))
assert abs(float((1 + as_**2/als**2).subs(_sub)) - 1.01) < 1e-12
assert abs(float((1 + (as_**2/als**2)*sp.cos(th)**2).subs(_sub).subs(th, sp.pi/3)) - 1.0025) < 1e-12
#   and the two limits are genuinely different geometries, not a tolerance: Weyl dies at M = 0 and
#   survives at M = 3/10, four orders of magnitude apart.
assert w0 < 1e-4 < 1e-2 < wM, (w0, wM)
assert wM/max(w0, 1e-300) > 1e4
