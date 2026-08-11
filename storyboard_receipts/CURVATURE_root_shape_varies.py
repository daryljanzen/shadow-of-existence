"""Does the ROOT configuration's form vary with the dial?  Constant permutation transport preserves a
CONSTANT form; a w-dependent form is not preserved by it, and that mismatch is curvature."""
import numpy as np
al=1.0
def roots_at(w,E):
    M2=(2/(3*np.sqrt(3)))*al*np.sin(3*w)          # 2M
    return np.roots([1,0,(E**2-1)*al**2, M2*al**2])
def shape(rts):
    """scale-invariant shape: normalise to unit RMS modulus, return sorted |r_i - r_j|"""
    r=np.array(rts); r=r-r.mean()
    s=np.sqrt((abs(r)**2).mean())
    if s<1e-14: return None
    r=r/s
    d=sorted(abs(r[i]-r[j]) for i in range(3) for j in range(i+1,3))
    return np.array(d)
for E,lab in ((1.0,'E=1 (flat leaf, turnaround cubic)'),(0.0,'E=0 (horizon cubic, the generations)')):
    print("   %s"%lab)
    print("      w      scale-invariant side lengths of the root triangle")
    prev=None
    for w in (0.10,0.30,0.50,0.70,0.90):
        sh=shape(roots_at(w,E))
        print("      %.2f   %s"%(w, '  '.join('%.5f'%x for x in sh)))
        prev=sh
    sh0=shape(roots_at(0.10,E)); sh1=shape(roots_at(0.90,E))
    print("      -> shape varies with w: %s   (max change %.2e)"%(not np.allclose(sh0,sh1,atol=1e-9), abs(sh1-sh0).max()))
    print()
print("   => at E=1 the shape is w-INDEPENDENT (equilateral always: the pure cube scales but does not deform).")
print("      at E=0 the shape DOES vary with w -- so a form built on the roots is w-dependent there,")
print("      and constant permutation transport does NOT preserve it.  That mismatch is the curvature.")
