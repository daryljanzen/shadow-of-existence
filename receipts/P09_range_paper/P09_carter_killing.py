"""
P09_carter_killing.py -- verifies cor:carter (the Carter constant is the substrate's symmetry): for the
  separable Carter cut, the vacuum condition splits of itself into eq:separated Dr''(r)+Dp''(p)=-4L(r^2+p^2),
  whose separation constant (the c2 that enters Dr as +c2 r^2 and Dp as -c2 p^2) is the CARTER CONSTANT --
  a genuine irreducible KILLING TENSOR K_ab = p^2 g^(r)_ab - r^2 g^(p)_ab with grad_(a K_bc)=0. So the hidden
  symmetry is not imposed: it is forced by vacuum on the maximally symmetric substrate. [P9 range_paper cor:carter]
STATUS: ✔✔   RUN: python3 P09_carter_killing.py   RUNTIME: ~8s
COMPUTES: symbolically, the quartics satisfy eq:separated and Dr''+4L r^2 = 2c2 = -(Dp''+4L p^2) (the
  separation constant); numerically, K=p^2 g^(r) - r^2 g^(p) satisfies the Killing-tensor equation
  grad_(a K_bc)=0 (~1e-8), is irreducible (K not proportional to g). CONTROL: the wrong-sign combination
  p^2 g^(r) + r^2 g^(p) FAILS the Killing equation.
ORIGIN: built new r1368 (P9 cited no receipts).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r,p=sp.symbols('r p', real=True)
Lam=sp.Rational(12,100); c2,c1,c0,d1=sp.Rational(1),sp.Rational(-6,10),sp.Rational(1,2),sp.Rational(3,10)
Dr=-Lam/3*r**4+c2*r**2+c1*r+c0; Dp=-Lam/3*p**4-c2*p**2+d1*p+c0
print("="*70); print("P09 Carter constant = a genuine Killing tensor (the substrate's hidden symmetry)"); print("="*70)
# (1) symbolic separation
ok&=check("quartics satisfy eq:separated: Dr''(r)+Dp''(p) = -4 Lambda (r^2+p^2)",
          sp.simplify(sp.diff(Dr,r,2)+sp.diff(Dp,p,2)-(-4*Lam*(r**2+p**2)))==0)
sr=sp.simplify(sp.diff(Dr,r,2)+4*Lam*r**2); spp=sp.simplify(sp.diff(Dp,p,2)+4*Lam*p**2)
ok&=check(f"separation constant: Dr''+4L r^2 = {sr} (=2c2) and Dp''+4L p^2 = {spp} (=-2c2), constant & opposite -> the CARTER constant",
          sr.free_symbols==set() and spp.free_symbols==set() and sp.simplify(sr+spp)==0 and sr!=0)
# (2) the Killing tensor K = p^2 g^(r) - r^2 g^(p), grad_(a K_bc)=0
Sig=r**2+p**2
er=[sp.Integer(1),0,0,-p**2]; ep=[sp.Integer(1),0,0,r**2]
gr=sp.zeros(4,4); gp=sp.zeros(4,4)
for i in range(4):
 for j in range(4): gr[i,j]=(Dr/Sig)*er[i]*er[j]
gr[1,1]+=Sig/Dr
for i in range(4):
 for j in range(4): gp[i,j]=-(Dp/Sig)*ep[i]*ep[j]
gp[2,2]+=Sig/Dp
g=gr+gp
g_f=sp.lambdify((r,p),g,'numpy')
def christ(rr,pp,h=1e-6):
    g0=np.array(g_f(rr,pp),float); gi=np.linalg.inv(g0); dg=np.zeros((4,4,4))
    dg[1]=(np.array(g_f(rr+h,pp),float)-np.array(g_f(rr-h,pp),float))/(2*h)
    dg[2]=(np.array(g_f(rr,pp+h),float)-np.array(g_f(rr,pp-h),float))/(2*h)
    Ga=np.zeros((4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4): Ga[A,b,c]=0.5*sum(gi[A,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c]) for d in range(4))
    return Ga
def killing_resid(Kexpr,rr,pp,h=1e-6):
    K_f=sp.lambdify((r,p),Kexpr,'numpy'); Ga=christ(rr,pp); K0=np.array(K_f(rr,pp),float); dK=np.zeros((4,4,4))
    dK[1]=(np.array(K_f(rr+h,pp),float)-np.array(K_f(rr-h,pp),float))/(2*h)
    dK[2]=(np.array(K_f(rr,pp+h),float)-np.array(K_f(rr,pp-h),float))/(2*h)
    nab=np.zeros((4,4,4))
    for a in range(4):
     for b in range(4):
      for c in range(4): nab[a,b,c]=dK[a][b,c]-sum(Ga[d,a,b]*K0[d,c]+Ga[d,a,c]*K0[b,d] for d in range(4))
    return max(abs((nab[a,b,c]+nab[b,c,a]+nab[c,a,b]+nab[a,c,b]+nab[b,a,c]+nab[c,b,a])/6) for a in range(4) for b in range(4) for c in range(4))
K = p**2*gr - r**2*gp
res=[killing_resid(K,rr,pp) for (rr,pp) in [(2.0,0.5),(3.0,0.8),(2.5,1.1)]]
ok&=check(f"KILLING TENSOR: K=p^2 g^(r)-r^2 g^(p) satisfies grad_(a K_bc)=0 at 3 points (max {max(res):.1e})", max(res)<1e-5)
# (3) irreducible: K is not proportional to g (a genuine hidden symmetry, not the trivial Killing tensor)
ratio=sp.simplify((K[1,1]/g[1,1]) - (K[0,0]/g[0,0]))
ok&=check("K is IRREDUCIBLE: K/g varies component-to-component (K not proportional to g) -> a genuine hidden symmetry",
          ratio!=0)
# (4) CONTROL: wrong-sign combination p^2 g^(r) + r^2 g^(p) FAILS the Killing equation
K2 = p**2*gr + r**2*gp
res2=killing_resid(K2, 2.0,0.5)
ok&=check(f"CONTROL: wrong-sign p^2 g^(r)+r^2 g^(p) FAILS grad_(a K_bc)=0 (resid {res2:.3f} >> 0)", res2>1e-2)
print("="*70)
print("RESULT:", "ALL PASS -- the separation constant of the vacuum condition IS a genuine irreducible Killing\n         tensor (grad_(a K_bc)=0): the Carter constant is the substrate's hidden symmetry, forced by vacuum." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   THE SEPARATION CONSTANT ITSELF, PINNED.  It is what the whole corollary is about: the vacuum
#   condition splits into two halves whose common value is 2 c2, and at c2 = 1 that is +2 on the
#   r side and -2 on the p side -- constant (no r, no p) and exactly opposite.
assert sr == 2 and spp == -2, (sr, spp)
assert sp.simplify(sr - 2*c2) == 0 and sp.simplify(spp + 2*c2) == 0
assert sr.free_symbols == set() and spp.free_symbols == set()
assert abs(float(Lam) - 0.12) < 1e-12                    # Lambda = 12/100, the substrate's own
#   THE KILLING EQUATION, PINNED AGAINST THE CONTROL.  The right-sign combination has residual
#   below 1e-5 at three points; the wrong-sign one is above 1 at the first of them -- five orders
#   of magnitude apart, so the check is not a tolerance artefact.
assert max(res) < 1e-5 and res2 > 1.0, (max(res), res2)
assert res2/max(res) > 1e4
#   and the tensor is IRREDUCIBLE: K/g takes different values in different blocks, so K is not a
#   multiple of the metric (which would carry no information beyond the norm).
assert sp.simplify(K[1, 1]/g[1, 1] - p**2) == 0
assert sp.simplify(K[2, 2]/g[2, 2] + r**2) == 0
assert sp.simplify(K[1, 1]/g[1, 1] - K[2, 2]/g[2, 2]) != 0
