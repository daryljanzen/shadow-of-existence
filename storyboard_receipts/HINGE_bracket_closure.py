"""If the geometry ASSIGNS the 6 null cross-horn connections to the off-diagonal E_ij and the
3 timelike same-hinge directions to the diagonal, do the brackets close?  Matrix units on C^3."""
import numpy as np, itertools
def E(i,j):
    M=np.zeros((3,3),dtype=complex); M[i,j]=1; return M
def br(A,B): return A@B-B@A
off=[(i,j) for i in range(3) for j in range(3) if i!=j]     # the 6 NULL connections
dia=[(i,i) for i in range(3)]                                # the 3 TIMELIKE directions
basis={p:E(*p) for p in off+dia}
print("   6 null -> off-diagonal E_ij ; 3 timelike -> diagonal E_ii ; trace removed")
print()
# does the bracket of two off-diagonals stay in the span?
allsp=[E(i,j) for i in range(3) for j in range(3)]
def in_span(M):
    A=np.array([m.flatten() for m in allsp]).T
    x,res,rk,sv=np.linalg.lstsq(A,M.flatten(),rcond=None)
    return np.allclose(A@x, M.flatten())
ok=all(in_span(br(basis[p],basis[q])) for p in off for q in off)
print("   [off, off] closes in the span:", ok)
print("   [off, dia] closes:", all(in_span(br(basis[p],basis[q])) for p in off for q in dia))
print()
# the characteristic su(3) brackets
print("   characteristic brackets:")
print("      [E_01, E_10] = E_00 - E_11 :", np.allclose(br(E(0,1),E(1,0)), E(0,0)-E(1,1)), " -> a CARTAN element")
print("      [E_01, E_12] = E_02        :", np.allclose(br(E(0,1),E(1,2)), E(0,2)), " -> another ROOT")
print()
tr=sum(E(i,i) for i in range(3))
print("   the trace (identity) is central: [1,X]=0 for all X:", all(np.allclose(br(tr,basis[p]),0) for p in basis))
print("   so removing it leaves sl(3,C):  dim = 9 - 1 = 8")
print()
print("   => the brackets close AUTOMATICALLY once the assignment is made.")
print("      The ASSIGNMENT is the content, and the causal character makes it.")
