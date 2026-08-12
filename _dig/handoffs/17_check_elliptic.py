import sympy as sp
# D02 leaned on: the j=0 (equianharmonic) elliptic curve associated to the 3 roots + centre is a
# degree-2 cover of the line branched at 4 points, with CM by omega (order-3 automorphism).
# This is the rem:equianharmonic object. Let me sanity-check the STANDARD facts I invoked, so the
# draft doesn't assert something loosely.
# (1) An elliptic curve y^2 = quartic(x) is a double cover of the x-line branched at the 4 roots. STANDARD.
# (2) j=0 <=> the curve has an order-3 automorphism (CM by the Eisenstein integers Z[omega]). STANDARD.
# (3) equianharmonic cross-ratio of 4 pts = e^{i pi/3} <=> j=0. STANDARD.
# I am NOT re-deriving these (they are textbook). I just confirm the cross-ratio claim numerically:
# three cube roots of unity + center(0): are they equianharmonic (j=0)?
import numpy as np
w=np.exp(2j*np.pi/3)
pts=[1, w, w**2, 0]   # 3 roots of z^3=1 plus the centre
# cross-ratio (z1,z2;z3,z4)
def cr(a,b,c,d): return ((a-c)*(b-d))/((a-d)*(b-c))
lam=cr(*pts)
print("cross-ratio of {1,w,w^2,0} =", np.round(lam,6))
# j-invariant from lambda: j=256 (l^2-l+1)^3 / (l^2 (l-1)^2)
j=256*(lam**2-lam+1)**3/(lam**2*(lam-1)**2)
print("j =", np.round(j,6), " (j=0 is equianharmonic) ->", "EQUIANHARMONIC (j=0)" if abs(j)<1e-9 else "not")
# lambda equianharmonic values are the primitive 6th roots e^{±i pi/3}: check |lam^2-lam+1|
print("lam^2-lam+1 =", np.round(lam**2-lam+1,8), " -> vanishes iff equianharmonic:", abs(lam**2-lam+1)<1e-9)
print("\n=> D02's structural description (deg-2 cover, 4 branch pts, j=0/CM-by-omega) uses only textbook")
print("   facts + this cross-ratio check. The draft's math is safe; it asserts nothing nonstandard.")
