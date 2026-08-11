"""Receipt: verify range_paper (P9) L228 Type-D speciality claim.
Claim: SdS/KdS/axisym-Bianchi are Type D, with the speciality discriminant
I^3 - 27 J^2 = 0 and the speciality ratio I^3/J^2 CONSTANT (=27, not 4).
Method: standard curvature (Weyl) invariants I, J from the 5 Weyl scalars.
Type D => only Psi_2 != 0 in the transverse frame."""
import numpy as np
def IJ(Psi):
    p0,p1,p2,p3,p4 = Psi
    I = p0*p4 - 4*p1*p3 + 3*p2**2
    # J = det of the 3x3 symmetric Weyl matrix
    M = np.array([[p0,p1,p2],[p1,p2,p3],[p2,p3,p4]])
    J = np.linalg.det(M)
    return I, J
# Type D: only Psi_2 nonzero (Kerr/SdS/KdS transverse frame), test several values
for psi in [0.3, 1.0, -2.5, 3.7]:
    I,J = IJ([0,0,psi,0,0])
    disc = I**3 - 27*J**2
    ratio = I**3 / J**2
    print(f"Psi2={psi:+.2f}: I={I:.4f} J={J:.4f}  I^3-27J^2={disc:.2e}  I^3/J^2={ratio:.6f}")
# Type I (generic): three distinct eigenvalues -> discriminant != 0, ratio varies
print("--- Type I (generic Psi0..Psi4) : discriminant nonzero, ratio not 27 ---")
for seed in [1,2,3]:
    rng=np.random.default_rng(seed); Psi=rng.normal(size=5)
    I,J=IJ(Psi); print(f"  disc={ (I**3-27*J**2):.4f}  I^3/J^2={(I**3/J**2):.4f}")
print("\nCONCLUSION: Type D => I^3=27J^2 exactly, ratio I^3/J^2 == 27 (constant), NEVER 4.")
print("range_paper L228 'speciality ratio constant over the manifold' is CORRECT; old '==4' would be wrong.")

# --- r968 APPLIED FIX ---
# range_paper L231 defined "the speciality ratio 27J^2/I^3" and wrongly stated Kerr Type D has ratio ==4.
# For Type D: I^3 = 27 J^2  =>  27J^2/I^3 = 1 identically.  Fixed "\equiv4" -> "\equiv1" at r968.
import numpy as np
ps=1.3; I=3*ps**2; J=-ps**3
print(f"\n[r968 fix check] Type D 27J^2/I^3 = {27*J**2/I**3:.6f}  (paper now says \\equiv1  -- correct)")
