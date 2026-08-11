"""hexad_resonance_verify.py -- is the substrate's skew hexagon the SAME six-fold as the
Nariai A_2 hexad, or a resonance of shared abstract type?

VERDICT: a RESONANCE, not an identity. The two hexads share the fundamental triple and
complete it by DISTINCT reflections -- T (timelike, horn-flipping) against the offset
parity R (spacelike, horn-preserving) -- which this script exhibits on the six points.
Baked in P3 (SdS-slicing-curve) sec:hinge-geometry and its abstract.

SYMBOL CANON (renamed r1610; the physics below is unchanged).
  R  -- the orientation / mass-reflection parity: the A_2 diagram automorphism, the
        orientation-reversing element of O(5,1)\SO_0(5,1), realised on a cut spinor as
        gamma^5. P12 (algebroid) gives it explicitly as R = diag(1,1,-1,1,1,1), "the
        reflection of the cut's displacement transverse to the symmetry axis (the offset
        r_0 = (2/sqrt3) sin w) ... sends r_0 -> -r_0 hence 2M -> -2M". Restricted to the
        three coordinates the hexagon lives in, that matrix is diag(1,1,-1) -- the object
        called R below.
  P  -- RESERVED for the areal SPATIAL parity r -> -r (Clifford gamma^1 gamma^2 gamma^3,
        which anticommutes with gamma^5). It does NOT appear in this script.
  T  -- the time reflection X_0 -> -X_0.

WHY THE RENAME. This script predates the P/R/sigma canon settled at r1305-06 and called
the horn-preserving reflection "P", which that canon reassigned to the areal spatial
parity -- so the file named one object with another's symbol. Corrected r1610. NOTE FOR
READERS OF THE RECORD: the r814 CORPUS_MAP entry, kept verbatim as history, still reads
"P (X2-reflection, horn-preserving)"; that "P" is this "R".
"""
import numpy as np
s3 = np.sqrt(3)
# six skew-hexagon vertices (X0,X1,X2) on -X0^2+X1^2+X2^2 = 1 (alpha=1)
# U at X0=+s3, D at X0=-s3; transverse radius 2, polar 0/120/240
def vert(horn, phi_deg):
    phi = np.deg2rad(phi_deg)
    return np.array([horn*s3, 2*np.cos(phi), 2*np.sin(phi)])
names = ['U0','U120','U240','D0','D120','D240']
V = {'U0':vert(+1,0),'U120':vert(+1,120),'U240':vert(+1,240),
     'D0':vert(-1,0),'D120':vert(-1,120),'D240':vert(-1,240)}
# check on hyperboloid
for n in names:
    x=V[n]; assert abs(-x[0]**2+x[1]**2+x[2]**2 - 1) < 1e-9, n
print("all six on -X0^2+X1^2+X2^2=1: OK")

def refl(diag):  # reflection matrix
    return np.diag(diag)
T  = refl([-1,1,1])   # X0 -> -X0   (time / horn swap)
R  = refl([1,1,-1])   # X2 -> -X2   the offset parity: P12's R = diag(1,1,-1,1,1,1), restricted
alt= refl([1,-1,1])   # X1 -> -X1   the OTHER spacelike option, kept as the control that fails

def perm(M):
    out={}
    for n in names:
        img = M@V[n]
        match=[m for m in names if np.allclose(img,V[m],atol=1e-9)]
        out[n]= match[0] if match else 'OFF-SET'
    return out

def is_symmetry(M):
    return all(perm(M)[n]!='OFF-SET' for n in names)

for label,M in [('T (X0)',T),('R (X2-refl)',R),('alt (X1-refl)',alt),('R∘T (X2)',R@T),('alt∘T (X1)',alt@T)]:
    p=perm(M)
    print(f"{label:12} symmetry={is_symmetry(M)}  perm={p}")

print()
print("=== the pin: does R act the same as T on the six points? ===")
for pl,S in [('R (X2)',R),('alt (X1)',alt)]:
    same = all(np.allclose(S@V[n], T@V[n], atol=1e-9) for n in names)
    # key witness: what each does to U0
    print(f"{pl}: ==T on all six? {same}   |  ->{perm(S)['U0']}, T(U0)->{perm(T)['U0']}   |  preserves horn? {perm(S)['U0'][0]=='U'}, T flips horn? {perm(T)['U0'][0]=='D'}")
