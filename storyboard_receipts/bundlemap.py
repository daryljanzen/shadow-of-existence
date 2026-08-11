"""U-bundlemap: map panel A's two physical bundles to (branch=Im tau~ wing, sign Re tau~)
in the F chart, and identify the other two of the four cells. All at source.
Bead: r^3 = A^3 sinh^2(w), w=1.5 tau~ (alpha=1). r REAL is the physical condition."""
import numpy as np
A=(2/(3*np.sqrt(3)))**(1/3)

def r_real_check(Re,Im):
    w=1.5*(Re+1j*Im); S=np.sinh(w)**2               # = (r/A)^3
    # the three cube roots; pick the (near-)real one
    roots=[A*abs(S)**(1/3)*np.exp(1j*(np.angle(S)+2*np.pi*k)/3) for k in range(3)]
    real=[z.real for z in roots if abs(z.imag)<1e-7]
    return real, roots

# ---- Bundle 1 (ours, cosmological): antimatter collapse -> lap -> matter universe ----
def cosmo(r):
    if r>=0: return (2/3)*np.arcsinh((r/A)**1.5),0.0
    u=abs(r/A)**1.5
    return (0.0,-(2/3)*np.arcsin(u)) if u<=1 else (-(2/3)*np.arccosh(u),-np.pi/3)

print("BUNDLE 1 (ours): r , (Re tau~, Im tau~/[pi/3]) , r recovered real?")
for r in [-2.0,-1.155,-0.727,-0.3,0.3,1.0]:
    Re,Im=cosmo(r); real,_=r_real_check(Re,Im)
    hit=any(abs(z-r)<1e-3 for z in real)
    print(f"  r={r:+.3f}  Re={Re:+.3f}  Im={Im/(np.pi/3):+.2f}*pi/3  real r in {[f'{z:+.2f}' for z in real]}  match={hit}")

# ---- Bundle 2 (conjugate, r->-r reading): matter BH -> lap -> antimatter universe ----
# antimatter universe leg: signed r<0, EXPANDING. r->-r image of matter universe (r>0,Im=0).
# sinh^2(w')=-(|r|/A)^3 -> sinh(w')=i(|r|/A)^{3/2}=i sinh(x): w'=arccosh(sinh x)+i pi/2 for sinh x>=1.
print("\nBUNDLE 2 (conjugate) antimatter-universe leg (signed r<0, expanding):")
for x in [0.4,0.9,1.4]:                       # x = |Re tau~| of the matter-universe preimage
    sx=np.sinh(x)
    if sx>=1:
        a=np.arccosh(sx); Re,Im=a/1.5,(np.pi/2)/1.5
        real,_=r_real_check(Re,Im)
        rneg=[z for z in real if z<-1e-6]
        print(f"  Re={Re:+.3f}  Im={Im/(np.pi/3):+.2f}*pi/3  -> real r<0: {[f'{z:+.2f}' for z in rneg]}")
    else:
        print(f"  x={x}: |sinh|<1 (lap region, r in (-A,0))")

# ---- the FOUR cells of the r<0 (antimatter) region, s=|r/A|^{3/2}>1 (collapse/universe) ----
print("\nFOUR CELLS  (Im wing = sign of Im tau~) x (sign Re tau~), at |r|=1.5 (s>1):")
r0=-1.5; s=abs(r0/A)**1.5; x=np.arccosh(s)
for imwing in (-1,+1):
    for resign in (-1,+1):
        Re,Im=resign*x/1.5, imwing*(np.pi/2)/1.5
        real,_=r_real_check(Re,Im); rneg=[z for z in real if z<-1e-6]
        tag=""
        if imwing<0 and resign<0: tag="= BUNDLE 1 antimatter collapse (our progenitor, back in cosmic time)"
        if imwing>0 and resign>0: tag="= BUNDLE 2 antimatter universe (the conjugate, forward)"
        if imwing<0 and resign>0: tag="= T-image of B1 (same wing, arrow-reversed: the cosh's other arm)"
        if imwing>0 and resign<0: tag="= T-image of B2 (arrow-reversed)"
        print(f"  Im={imwing:+d}*pi/3, Re {'>' if resign>0 else '<'}0 : real r<0={[f'{z:+.2f}' for z in rneg]}  {tag}")

print("\nRELATIONS: bundle2 = E(bundle1), E=T.P: (Re,Im)->(-Re,-Im) on the antimatter legs.")
print("The two PHYSICAL bundles are the DIAGONAL {(-pi/3,Re<0),(+pi/3,Re>0)} = the E-pair.")
print("The other two cells are the T-images (arrow-reversed) of the bundles: same worldlines,")
print("cosmic-time-reversed -- the antimatter cosh-bounce arm that re-expands WITHOUT crossing r=0.")
