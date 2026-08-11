"""Does su(3) admit an invariant 3-plane in its R^6?  If not, CR's own axiom decides the fork:
P7 makes the LAYER (3-dimensional) the EXISTENT, a definite object -- so an isometry in the isotropy
must map layers to layers, i.e. preserve the layer's tangent 3-plane."""
import numpy as np, itertools
l=[np.array(m,dtype=complex) for m in [
 [[0,1,0],[1,0,0],[0,0,0]], [[0,-1j,0],[1j,0,0],[0,0,0]], [[1,0,0],[0,-1,0],[0,0,0]],
 [[0,0,1],[0,0,0],[1,0,0]], [[0,0,-1j],[0,0,0],[1j,0,0]], [[0,0,0],[0,0,1],[0,1,0]],
 [[0,0,0],[0,0,-1j],[0,1j,0]], np.array([[1,0,0],[0,1,0],[0,0,-2]])/np.sqrt(3)]]
gen=[1j*m/2 for m in l]                                   # anti-hermitian su(3) generators
def real6(A):                                             # C^3 -> R^6 realification
    return np.block([[A.real,-A.imag],[A.imag,A.real]])
G=[real6(g) for g in gen]
print("  su(3) realified on R^6:  %d generators, all real 6x6, all antisymmetric: %s"
      %(len(G), all(np.allclose(g,-g.T) for g in G)))
# irreducibility: orbit of a random vector under the generated algebra must span R^6
rng=np.random.default_rng(7); v=rng.normal(size=6); S=[v]
for _ in range(8):
    S = S + [g@w for g in G for w in S]
    R=np.linalg.matrix_rank(np.array(S),tol=1e-9)
    if R==6: break
print("  span of the su(3)-orbit of a generic vector has rank %d of 6  -> %s"
      %(R,"IRREDUCIBLE over R (no proper invariant subspace)" if R==6 else "reducible"))
# explicit: is ANY 3-plane invariant?  test the commutant (Schur): dim of matrices commuting with all G
M=np.zeros((0,36))
for g in G:
    M=np.vstack([M, np.kron(np.eye(6),g)-np.kron(g.T,np.eye(6))])
ns=36-np.linalg.matrix_rank(M,tol=1e-9)
print("  commutant dimension = %d  (=2 means complex type: only aI+bJ commute -> no real invariant plane)"%ns)
print()
print("  ==> su(3) admits NO invariant 3-plane in R^6.")
print("      P7 axiom: the LAYER is the existent, a definite 3-manifold; an isotropy element must")
print("      carry layers to layers, i.e. preserve the layer tangent 3-plane.")
print("      Therefore the su(3) block must be DISJOINT from the layer's 3 directions:")
print("         spatial dirs >= 3 (layer) + 6 (su(3) block) = 9   =>   D >= 10.")
print("      And the descent must still END on so(5,1)/so(4,1) to keep P12's Dirac-algebra match.")
