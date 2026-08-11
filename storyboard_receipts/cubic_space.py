import numpy as np
# Are the sheet-A2 and generation-A2 one structure? Test by DEFORMATION in cubic-space (p,q): r^3 + p r + q = 0.
# p=0 line = Z3-symmetric (equal-magnitude roots); p!=0 breaks Z3.
M=0.3
# SHEET family:  r^3 = 2M sinh^2(w)  =>  p=0, q=-2M sinh^2(w)          [the Z3-symmetric axis]
# GEN. family :  r^3 - a^2 r + 2M a^2 = 0 => p=-a^2, q=2M a^2 = -2M p   [line q=-2M p; a^2=curvature/Lambda]
for w in [0.3,0.7,1.2]:
    q=-2*M*np.sinh(1.5*w)**2; print("sheet  w=%.1f (p,q)=(0,%+.3f) |roots|=%s"%(w,q,[round(abs(z),3) for z in np.roots([1,0,0,q])]))
for a2 in [0.0,0.3,1.0,2.0]:
    p,q=-a2,2*M*a2; print("gen  a^2=%.1f (p,q)=(%+.2f,%+.3f) |roots|=%s"%(a2,p,q,[round(abs(z),3) for z in np.roots([1,0,p,q])]))
# both lines pass through origin (r^3=0, the r=0 triple point = charge-conj locus).
# charge conj r->-r acts as (p,q)->(p,-q): fixes sheet line p=0; sends gen line q=-2Mp to q=+2Mp (different line).
print("=> shared symmetric A2 center at r=0 + shared charge Z2; two distinct deformation rays; NO symmetry maps sheets<->generations.")
