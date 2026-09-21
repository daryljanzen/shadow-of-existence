"""
P14_no_rotation_of_the_substrate_is_a_compact_chiral_su2
========================================================

Object under test -- P14's list, worked for the WEAK su(2).  P14 poses the undelivered gauge content
as "a question about the bundle: what does the operator act on, and what fixes it?", lists the
substrate's own candidates -- the embedding tangent bundle, the spinor bundles, the wall's normal
bundle, the two ruling bundles -- and settles them for COLOUR in one move: "every candidate was built
from the substrate's ambient geometry, and ambient geometry is real: the question was never which
real bundle but where the complex structure is."

r6723 settled one candidate for the weak su(2).  This settles the list in one move of the same kind.

--------------------------------------------------------------------------------
(1) A REAL CHIRAL SPLIT NEEDS EUCLIDEAN SIGNATURE.

  The chiral split of a four-dimensional rotation algebra is the split of two-forms into the
  eigenspaces of the Hodge star, and ** on two-forms is +1 in Euclidean signature and -1 in
  Lorentzian -- computed.  So so(4) = su(2) + su(2) as REAL compact algebras, with eigenvalues +-1;
  while so(3,1), with eigenvalues +-i, splits only after complexification into sl(2,C) factors
  exchanged by conjugation, and as a real algebra is simple, with no real su(2) ideal.

--------------------------------------------------------------------------------
(2) AND THE EUCLIDEAN FOUR-SPACE IS NEVER THE ONE WHOSE CHIRALITY IS gamma^5.

  A four-dimensional subspace's chirality is the Clifford element of its normal (r6723).  Of the
  substrate's five four-dimensional subspaces:

    tangent {a,b,c,r_0},  normal X_0   Euclidean    chirality = gamma^5 ?  NO
    tangent {X_0,b,c,r_0},normal a     Lorentzian   NO
    tangent {X_0,a,c,r_0},normal b     Lorentzian   NO
    tangent {X_0,a,b,r_0},normal c     Lorentzian   NO
    tangent {X_0,a,b,c},  normal r_0   Lorentzian   chirality = gamma^5 ?  YES

  *** The one Euclidean four-space has the wrong chirality; the one four-space whose chirality is
  the physical gamma^5 is Lorentzian, where no real chiral su(2) exists. ***

--------------------------------------------------------------------------------
(3) AND THE COMPACT su(2) THAT DOES COMMUTE WITH gamma^5 IS VECTOR-LIKE.

  The spatial rotations of {a,b,c} generate a compact su(2) commuting with gamma^5 -- computed -- and
  it acts on BOTH gamma^5 eigenspaces: the same rotation acts on left and right.

  ==> *** No rotation of the substrate is a compact su(2) acting on one physical handedness.  Every
      candidate on P14's list is built from the substrate's ambient geometry, so its holonomy lies
      in the substrate's rotation algebra -- and the weak su(2) is a compact su(2) projected onto
      ONE eigenspace of gamma^5, which no rotation performs.  This is P14's colour move, made for the
      weak su(2): the question is never which geometric bundle, because the chiral projection is not
      a rotation. ***

  ⌗ The embedding tangent bundle, of signature (5,1), is the tangent bundle of a flat ambient space,
  so its induced connection on the substrate's directions is the substrate's own and (1)-(3) apply.

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.

  ** NOT that weak isospin is absent. **  What is shown is WHERE it is not: it is not a rotation of
  the substrate, because a compact su(2) chiral with respect to the physical chirality would need a
  Euclidean four-space whose normal is r_0, and there is none.  A chirally projected compact su(2)
  is an internal symmetry acting on one handedness -- which is where P14's body places the question,
  in the bundle the operator acts on.

  ** NOT a claim about bundles not built from the substrate's ambient geometry. **  The argument
  covers holonomy lying in the substrate's rotation algebra, which is every candidate on P14's list.

  ** Computed on the substrate's five directions. **
"""

import itertools, numpy as np

def hodge_sq(sig):
    n=len(sig); pairs=list(itertools.combinations(range(n),2)); idx={p:k for k,p in enumerate(pairs)}
    S=np.zeros((6,6))
    for (a,b) in pairs:
        rest=[x for x in range(n) if x not in (a,b)]
        sign=np.linalg.det(np.eye(n)[[a,b]+rest])
        S[idx[tuple(sorted(rest))], idx[(a,b)]] = sign*sig[a]*sig[b]
    return S@S
assert np.allclose(hodge_sq([1,1,1,1]),  np.eye(6))
assert np.allclose(hodge_sq([-1,1,1,1]), -np.eye(6))
print("  ** on two-forms: +1 Euclidean, -1 Lorentzian                                  OK")

s0=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]]); Z=np.zeros((2,2))
g0=np.block([[Z,s0],[s0,Z]]); g1,g2,g3=[np.block([[Z,s],[-s,Z]]) for s in (sx,sy,sz)]; g4=1j*g0@g1@g2@g3
G=[g0,g1,g2,g3,g4]; SIG=[-1,1,1,1,1]; g5=G[4]
def prop(A,B): return any(np.allclose(A,c*B) for c in (1,-1,1j,-1j))
rows=[]
for omit in range(5):
    S=[i for i in range(5) if i!=omit]
    V=G[S[0]]@G[S[1]]@G[S[2]]@G[S[3]]
    rows.append((omit, all(SIG[i]>0 for i in S), prop(V,g5)))
euclid=[r for r in rows if r[1]]; chiral=[r for r in rows if r[2]]
assert len(euclid)==1 and euclid[0][0]==0 and not euclid[0][2]
assert len(chiral)==1 and chiral[0][0]==4 and not chiral[0][1]
print("  the one Euclidean four-space (normal X_0) has the wrong chirality;             OK")
print("  the one four-space with chirality gamma^5 (normal r_0) is Lorentzian            OK")

gens=[G[i]@G[j]/2 for i,j in ((1,2),(2,3),(3,1))]
assert all(np.allclose(X@g5,g5@X) for X in gens)
H=g5 if np.allclose(g5,g5.conj().T) else 1j*g5
w,v=np.linalg.eigh(H); Pp=v[:,w>0]; Pm=v[:,w<0]
assert any(not np.allclose(Pp.conj().T@X@Pp,0) for X in gens)
assert any(not np.allclose(Pm.conj().T@X@Pm,0) for X in gens)
print("  the compact su(2) commuting with gamma^5 acts on both eigenspaces: vector-like   OK")

print()
print("ESTABLISHED: a real chiral split needs Euclidean signature, where ** = +1 on two-forms. Of the")
print("substrate's five four-dimensional subspaces, the one Euclidean one has the wrong chirality and the")
print("one whose chirality is the physical gamma^5 is Lorentzian, where the split is complex. The compact")
print("su(2) that does commute with gamma^5 acts on left and right alike. So no rotation of the substrate")
print("is a compact su(2) acting on one physical handedness, and every candidate on P14's list -- built")
print("from ambient geometry, holonomy in the rotation algebra -- is settled for the weak su(2) at once.")
print("NOT CLAIMED: that weak isospin is absent -- only that it is not a rotation of the substrate.")
