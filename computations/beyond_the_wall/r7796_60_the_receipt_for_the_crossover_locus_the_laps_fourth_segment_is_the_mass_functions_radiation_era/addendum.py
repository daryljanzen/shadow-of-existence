#!/usr/bin/env python3
"""r7796 (60) -- ADDENDUM, DECLARED POST HOC.

** WHAT THIS IS AND WHEN IT WAS WRITTEN. **  The thirteen arms of `PREDICTION.md` were pushed before
anything in this revision was measured.  The receipt was then built and run, and THREE of its checks
came back red.  This file is the diagnosis of those three, written AFTER seeing them, and it is kept
separate from the registration for exactly that reason.  Nothing here is a registered prediction.

** WHAT IT SEARCHES AND COMPUTES. **  Nothing textual: it reads no file.  It recomputes the bent
radicand's inner zero at six values of `alpha^2` from the same derived constants the receipt uses, fits
the two-term expansion `lambda * gap = e1 + e2/lambda` on the two STIFFEST points alone, and prints the
other four as predictions of a model fitted without them.  It then solves the first-order balance
symbolically and expands the result in the small parameter.

** THE THREE REDS, AND WHICH KIND EACH IS. **
  Ⓐ⑤ is a REAL FAILURE of the registered criterion.  The registration predicted the series would
     return exactly `s_0^3/(2M alpha^2)`.  It returns that divided by `(1 - 2 x share)`.  Reported
     FAILED; the finding is stronger than the prediction, and the receipt's gate carries the closed
     form.
  Ⓐ⑥ was MY IMPLEMENTATION, not the criterion.  It formed the residual as `gap(lambda) - gap(1)/lambda`
     -- using the measured gap at `lambda = 1` where the first-order COEFFICIENT belongs.  `gap(1)` is
     `e1 + e2`, so that residual is `e2(1/lambda^2 - 1/lambda)` and carries a spurious `(1 - lambda)`.
     Measured with the fitted `e1` the registered criterion is met with room to spare.
  Ⓒ⑨ was MY GRID, not the criterion.  The registration said four decades EITHER SIDE; the first
     implementation sampled two.  The share is exactly `s_0/s`, so two decades either side spans `1e2`
     to `1e-2` and cannot reach the registered `1e-3`.  On the grid the registration named it is met.

⌗ Two of the three reds were defects in reading my own registration, and the third was the registration
  claiming more than the argument needs.  None of the three was in the physics.
"""
import numpy as np, sympy as sp, mpmath as mp
CLIGHT=299792.458; H0,OM=68.6,0.2973
OMR=4.15e-5/(H0/100.0)**2; OL=1.0-OM; hub=H0/CLIGHT
X0=(2*OL/OM)**(1/3); ALPHA=1.0/(hub*np.sqrt(OL)); R0=ALPHA*X0/np.sqrt(3.0)
TWOM=2*R0**3/(ALPHA**2*X0**3); KRAD=hub**2*OMR*R0**4
mp.mp.dps=60
A_,M_,K_=mp.mpf(ALPHA),mp.mpf(TWOM),mp.mpf(KRAD); S0=K_/M_
def bal(s,a2=None):
    return -M_/s + K_/s**2 + (mp.mpf(0) if a2=='none' else s**2/(A_**2 if a2 is None else mp.mpf(a2)))
LAM=[mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(1),mp.mpf(2),mp.mpf(4),mp.mpf(16)]
gaps={}
for lam in LAM:
    s_l=mp.findroot(lambda s: bal(s,a2=lam*A_**2), S0); gaps[lam]=(s_l-S0)/S0
# lam*gap = e1 + e2/lam  -> linear in 1/lam.  fit from lam=4 and lam=16
l1,l2=mp.mpf(4),mp.mpf(16)
y1,y2=gaps[l1]*l1,gaps[l2]*l2
e2=(y1-y2)/(1/l1-1/l2); e1=y1-e2/l1
print("e1 =",mp.nstr(e1,20)); print("e2 =",mp.nstr(e2,12))
share=S0**3/(M_*A_**2)
print("share =",mp.nstr(share,20))
print("e1/share - 1 =",mp.nstr(e1/share-1,8))
print("e2/e1 =",mp.nstr(e2/e1,8), "  4*share =",mp.nstr(4*share,8))
# residual with the FITTED e1
print("\nresidual gap - e1/lam, scaled by lam^2:")
vals=[]
for lam in LAM:
    r=gaps[lam]-e1/lam; vals.append(r*lam**2)
    print(f"  lam={float(lam):>6.2f}  resid={mp.nstr(r,8):>16s}  x lam^2={mp.nstr(r*lam**2,10)}")
sp2=(max(vals)-min(vals))/abs(sum(vals)/len(vals))
print("spread of resid*lam^2 =",mp.nstr(sp2,6))
# linearity of lam*gap in 1/lam -- three-point second difference
print("\nlinearity of lam*gap against 1/lam:")
xs=[1/l for l in LAM]; ys=[gaps[l]*l for l in LAM]
pred=[e1+e2*x for x in xs]
worst=max(abs(ys[i]-pred[i])/abs(ys[i]) for i in range(len(xs)))
for i,l in enumerate(LAM):
    print(f"  lam={float(l):>6.2f}  lam*gap={mp.nstr(ys[i],16)}  model={mp.nstr(pred[i],16)}")
print("worst relative departure from the two-term model =",mp.nstr(worst,6))
# the symbolic exact first-order solve vs its leading asymptotic
Ks,Ms,als,eps=sp.symbols('K TwoM alpha epsilon',positive=True)
s0s=Ks/Ms; ssym=s0s*(1+eps)
B=-Ms/ssym+Ks/ssym**2+ssym**2/als**2
lead=sp.series(sp.simplify(B),eps,0,2).removeO()
sol=sp.solve(sp.Eq(lead,0),eps)[0]
pred_s=sp.simplify(s0s**3/(Ms*als**2))
print("\nexact first-order solve:",sp.simplify(sol))
print("the share            :",pred_s)
small=sp.symbols('delta',positive=True)
ratio=sp.simplify(sol/pred_s)
print("ratio sol/share      :",ratio)
# asymptotic: expand ratio in the small parameter u = K^3/(TwoM^4 alpha^2)
u=sp.symbols('u',positive=True)
ratio_u=sp.simplify(ratio.subs(als**2, Ks**3/(Ms**4*u)))
print("ratio in terms of u = K^3/(TwoM^4 alpha^2):",sp.simplify(ratio_u))
print("series about u=0:",sp.series(sp.simplify(ratio_u),u,0,3))
print("\nnumeric u =",mp.nstr(K_**3/(M_**4*A_**2),8),"  share =",mp.nstr(share,8))
