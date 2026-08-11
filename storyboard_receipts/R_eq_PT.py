"""
R_eq_PT.py -- resolve the ontology-index AUDIT FLAG (l.66):
  "R = gamma^5 ∝ PT sits in tension with 'R horn-preserving / T horn-flipping'."

The resolution: R and PT are EQUAL as cut-spinor operators (both ∝ gamma^5) but
DISTINCT as geometric reflections -- because R reflects the TRANSVERSE (5th,
cut-normal) direction while P,T reflect directions WITHIN the 4D cut. Different
arenas; no contradiction.

Corpus canon:  R = gamma^5 (transverse cut-normal reflection, fixes all 4 spacetime
legs -> horn-preserving);  P = gamma^1 gamma^2 gamma^3 (areal spatial parity);
T = gamma^0 (time reflection, X0->-X0 -> horn-flipping).
"""
import numpy as np

# Dirac gammas, mostly-plus-free convention (signature (+,-,-,-)); only algebra matters.
I2=np.eye(2,dtype=complex); Z=np.zeros((2,2),dtype=complex)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
g0=blk(I2,Z,Z,-I2); g1=blk(Z,sx,-sx,Z); g2=blk(Z,sy,-sy,Z); g3=blk(Z,sz,-sz,Z)
g5=1j*g0@g1@g2@g3
I4=np.eye(4,dtype=complex)

def prop(A,B):  # A proportional to B (A = c B, c a scalar)?
    # find c from a nonzero entry
    idx=np.unravel_index(np.argmax(np.abs(B)),B.shape)
    c=A[idx]/B[idx]
    return np.allclose(A, c*B), c

print("(1) gamma^5 identity and involution")
print("   g5 = i g0 g1 g2 g3 ;  g5^2 = I ?", np.allclose(g5@g5, I4))

print("\n(2) spinor operators of P and T, and their product")
P = g1@g2@g3          # areal spatial parity  (in-cut, spatial)
T = g0                # time reflection        (in-cut, temporal)
R = g5                # mass/transverse reflection = chirality operator (corpus)
okPT, c = prop(P@T, R)
print("   P=g1g2g3 , T=g0 :  P*T ∝ gamma^5 = R ?", okPT, " (P*T =", np.round(c,4), "* R)")
okTP, c2 = prop(T@P, R)
print("   T*P ∝ R ?", okTP, " (T*P =", np.round(c2,4), "* R)")
assert okPT and okTP
print("   => as CUT-SPINOR operators, R = gamma^5 ∝ PT.  [the identity the flag noted]")

print("\n(3) but GEOMETRICALLY R and PT act oppositely on the horn (X0)")
# geometric reflections on the 5D embedding block (X0,X1,X2, transverse Xn):
# T flips X0 (timelike, horn-flipping); P is spatial (fixes X0); R reflects the
# transverse cut-normal Xn (fixes all four spacetime legs incl. X0, horn-preserving).
Tgeo = np.diag([-1,1,1,1,1.0])   # X0 -> -X0
Pgeo = np.diag([1,-1,-1,-1,1.0]) # spatial legs flipped, X0 fixed  (areal spatial parity)
Rgeo = np.diag([1,1,1,1,-1.0])   # transverse (5th) cut-normal flipped, ALL 4 spacetime legs fixed
def horn(M): return "preserving" if M[0,0]==1 else "FLIPPING"
print("   T geometric: X0 ->", int(Tgeo[0,0]), "-> horn", horn(Tgeo))
print("   R geometric: X0 ->", int(Rgeo[0,0]), "-> horn", horn(Rgeo), " (reflects the TRANSVERSE leg, not a spacetime leg)")
PT = Pgeo@Tgeo
print("   (P*T) geometric: X0 ->", int(PT[0,0]), "-> horn", horn(PT))
print("   => geometric R (horn-preserving) != geometric PT (horn-flipping): DIFFERENT reflections.")
assert Rgeo[0,0]==1 and PT[0,0]==-1

print("""
RESOLUTION (no tension):
  R reflects the TRANSVERSE cut-normal (the 5th, offset direction), fixing all four
  spacetime legs -> horn-PRESERVING; its induced action on the 4D cut spinor is the
  chirality operator gamma^5 (standard: reflecting the normal of a 4D cut in a 5D
  spin manifold acts as the 4D volume element gamma^5).
  P, T reflect directions WITHIN the 4D cut; T flips X0 -> horn-FLIPPING; their
  spinor product P*T also equals (up to phase) gamma^5, since gamma^5 = i g0g1g2g3
  is the 4D volume element = the product of the four in-cut reflection generators.
  So R and PT induce the SAME cut-spinor operator (gamma^5) while being DISTINCT
  geometric reflections (transverse vs in-cut; horn-preserving vs -flipping).
  'R = gamma^5 ∝ PT' is a statement about induced 4D-cut spinor operators; 'R
  horn-preserving / T horn-flipping' is a statement about the 5D geometric action.
  Different arenas, both true -- the flag was a category conflation of the two.
""")
print("ALL CHECKS PASSED.")
