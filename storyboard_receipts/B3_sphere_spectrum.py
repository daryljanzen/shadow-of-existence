#!/usr/bin/env python3
"""B3_sphere_spectrum.py -- verify the angular eigenvalue lambda=j+1/2 in W=lambda*sqrt(f)/r (B3/L2).
Standard Dirac-on-S^2 spectrum, but WORKED here from the spin-weighted (edth) algebra, not cited.
The 2-sphere Dirac operator couples the spin-weight s=+/-1/2 spinor components via edth:
    edth  {}_sY_lm = -sqrt((l-s)(l+s+1)) {}_{s+1}Y_lm
    edthb {}_sY_lm = +sqrt((l+s)(l-s+1)) {}_{s-1}Y_lm
On (+1/2,-1/2) the Dirac operator is D=[[0,edthb],[edth,0]]; its eigenvalues are +/- the magnitude,
and we check that magnitude equals j+1/2 (j=l) for l=1/2,3/2,5/2,..., i.e. lambda in {1,2,3,...}.
"""
import numpy as np
def check(tag,c): print(f"  [{'PASS' if c else 'FAIL'}] {tag}"); return bool(c)
ok=True
print("="*66); print("Dirac operator on S^2: eigenvalue = j+1/2  (edth algebra)"); print("="*66)
for l in [0.5,1.5,2.5,3.5,4.5]:
    # coefficients coupling the two spin-1/2 components (m arbitrary; take m=1/2)
    s=-0.5; c_edth = np.sqrt((l-s)*(l+s+1))     # edth : -1/2 -> +1/2 ,  = sqrt((l+1/2)(l+1/2))
    s=+0.5; c_edthb= np.sqrt((l+s)*(l-s+1))     # edthb: +1/2 -> -1/2 ,  = sqrt((l+1/2)(l+1/2))
    D=np.array([[0.0, c_edthb],[c_edth,0.0]])    # 2x2 Dirac block on (+1/2,-1/2)
    ev=np.linalg.eigvals(D); mag=np.max(np.abs(ev.real))
    j=l; lam=j+0.5
    ok&=check(f"l=j={l}:  |Dirac eigenvalue|={mag:.4f}  ==  j+1/2={lam:.4f}", np.isclose(mag,lam))
print("-"*66)
print("  => the angular Dirac eigenvalue on S^2 is  lambda = j+1/2  in {1,2,3,...},")
print("     confirming W=lambda*sqrt(f)/r uses the standard sphere spectrum (Camporesi-Higuchi);")
print("     also = sqrt(D^2) with D^2 = -Delta_{1/2} + R/4 (Lichnerowicz, R=2 on unit S^2) = (l+1/2)^2.")
print("RESULT:", "ALL PASS -- lambda=j+1/2 verified from the edth algebra, not merely cited." if ok else "FAIL")
print("="*66)
