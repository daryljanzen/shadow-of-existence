"""
P09_typeD_quartics.py -- verifies thm:pd (the Type-D vacuum kernel = Kerr-NUT-(A)dS): the separable Carter
  cut ds^2=(Sig/Dr)dr^2+(Sig/Dp)dp^2+(1/Sig)[Dr(dtau-p^2 dsig)^2 - Dp(dtau+r^2 dsig)^2], Sig=r^2+p^2, is
  vacuum-Lambda (R_munu=Lambda g_munu) IF AND ONLY IF the structure functions are the quartics
    Dr = -(Lambda/3) r^4 + c2 r^2 + c1 r + c0,   Dp = -(Lambda/3) p^4 - c2 p^2 + d1 p + c0
  -- leading coeff -Lambda/3 (both), SHARED c0, OPPOSITE c2. [P9 range_paper sec:pd / thm:pd]
STATUS: ✔✔   RUN: python3 P09_typeD_quartics.py   RUNTIME: ~12s
COMPUTES: numeric R^mu_nu at several (r,p): =Lambda delta for the quartics (vacuum-Lambda, ~1e-5); and the
  ONLY-IF direction -- three perturbations that break the quartic structure each break vacuum:
  (a) an extra r^3 term, (b) mismatched constants (c0 -> c0+delta in Dp), (c) flipped c2 sign in Dp.
ORIGIN: built new r1367 (P9 cited no receipts).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r,p=sp.symbols('r p', real=True)
Lam=sp.Rational(12,100); L=float(Lam)
c2,c1,c0,d1=sp.Rational(1),sp.Rational(-6,10),sp.Rational(1,2),sp.Rational(3,10)
def metricf(Dr,Dp):
    Sig=r**2+p**2; g=sp.zeros(4,4)
    g[0,0]=(Dr-Dp)/Sig; g[1,1]=Sig/Dr; g[2,2]=Sig/Dp
    g[3,3]=(Dr*p**4-Dp*r**4)/Sig; g[0,3]=g[3,0]=(-Dr*p**2-Dp*r**2)/Sig
    return sp.lambdify((r,p), g,'numpy')
def christ(gf,rr,pp,h=1e-6):
    g0=np.array(gf(rr,pp),float); gi=np.linalg.inv(g0); dg=np.zeros((4,4,4))
    dg[1]=(np.array(gf(rr+h,pp),float)-np.array(gf(rr-h,pp),float))/(2*h)
    dg[2]=(np.array(gf(rr,pp+h),float)-np.array(gf(rr,pp-h),float))/(2*h)
    Ga=np.zeros((4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
        Ga[A,b,c]=0.5*sum(gi[A,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c]) for d in range(4))
    return Ga
def resid(gf,rr,pp,h=1e-5):
    Ga=christ(gf,rr,pp); dGa=np.zeros((4,4,4,4))
    dGa[1]=(christ(gf,rr+h,pp)-christ(gf,rr-h,pp))/(2*h); dGa[2]=(christ(gf,rr,pp+h)-christ(gf,rr,pp-h))/(2*h)
    R=np.zeros((4,4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        R[A,b,c,d]=dGa[c][A,b,d]-dGa[d][A,b,c]+sum(Ga[A,e,c]*Ga[e,b,d]-Ga[A,e,d]*Ga[e,b,c] for e in range(4))
    Ric=np.einsum('abad->bd',R); gi=np.linalg.inv(np.array(gf(rr,pp),float))
    return np.max(np.abs(gi@Ric - L*np.eye(4)))
pts=[(2.0,0.5),(3.0,0.8),(2.5,1.1)]
print("="*70); print("P09 Type-D vacuum kernel: Carter cut is vacuum-Lambda IFF structure functions are quartics"); print("="*70)
# forward: the quartics -> vacuum-Lambda
Dr=-Lam/3*r**4+c2*r**2+c1*r+c0; Dp=-Lam/3*p**4-c2*p**2+d1*p+c0
gf=metricf(Dr,Dp); res=[resid(gf,*pt) for pt in pts]
ok&=check(f"quartic Dr,Dp -> vacuum-Lambda R^mu_nu=Lambda delta (Lambda=0.12) at 3 (r,p), max resid {max(res):.1e}", max(res)<1e-4)
# only-if (a): extra r^3 term breaks vacuum
gf_a=metricf(Dr+sp.Rational(2,10)*r**3, Dp); ra=resid(gf_a,*pts[0])
ok&=check(f"ONLY-IF (a): an extra r^3 term in Dr breaks vacuum (resid {ra:.3f} >> 0)", ra>1e-2)
# only-if (b): mismatched constant (c0 -> c0+0.3 in Dp) breaks vacuum
gf_b=metricf(Dr, -Lam/3*p**4-c2*p**2+d1*p+(c0+sp.Rational(3,10))); rb=resid(gf_b,*pts[0])
ok&=check(f"ONLY-IF (b): mismatched constant (c0 not shared) breaks vacuum (resid {rb:.3f} >> 0)", rb>1e-2)
# only-if (c): flipped c2 sign in Dp breaks vacuum
gf_c=metricf(Dr, -Lam/3*p**4+c2*p**2+d1*p+c0); rc=resid(gf_c,*pts[0])
ok&=check(f"ONLY-IF (c): flipped c2 sign in Dp (must be OPPOSITE) breaks vacuum (resid {rc:.3f} >> 0)", rc>1e-2)
print("="*70)
print("RESULT:", "ALL PASS -- the separable Carter cut is vacuum-Lambda IFF Dr,Dp are the quartics with leading\n         -Lambda/3, shared c0, opposite c2: the Type-D (Kerr-NUT-(A)dS) vacuum kernel. Breaking any of these breaks vacuum." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   THE THREE STRUCTURAL CONDITIONS OF thm:pd, PINNED ON THE POLYNOMIALS THEMSELVES at
#   Lambda = 12/100, c2 = 1, c1 = -6/10, c0 = 1/2, d1 = 3/10:
#     leading coefficient -Lambda/3 = -0.04 in BOTH quartics,
#     c2 OPPOSITE:  +1 in Dr and -1 in Dp,
#     c0 SHARED:    0.5 in both.
assert abs(L - 0.12) < 1e-12, L
_Pr, _Pp = sp.Poly(Dr, r), sp.Poly(Dp, p)
assert _Pr.degree() == 4 and _Pp.degree() == 4
assert abs(float(_Pr.coeff_monomial(r**4)) - (-0.04)) < 1e-12
assert abs(float(_Pp.coeff_monomial(p**4)) - (-0.04)) < 1e-12
assert abs(float(_Pr.coeff_monomial(r**2)) - 1.0) < 1e-12
assert abs(float(_Pp.coeff_monomial(p**2)) - (-1.0)) < 1e-12
assert float(_Pr.coeff_monomial(r**2)) == -float(_Pp.coeff_monomial(p**2))       # OPPOSITE
assert abs(float(_Pr.coeff_monomial(1)) - 0.5) < 1e-12
assert float(_Pr.coeff_monomial(1)) == float(_Pp.coeff_monomial(1))              # SHARED
#   AND THE IFF IS TWO-SIDED WITH ROOM TO SPARE: the quartics sit below 1e-4 and all three
#   only-if breakages sit above 1e-2, more than two orders of magnitude apart.
assert max(res) < 1e-4, max(res)
assert min(ra, rb, rc) > 1e-2, (ra, rb, rc)
assert min(ra, rb, rc)/max(res) > 100.0
