"""
P14_the_four_spheres_chirality_anticommutes_with_the_physical_one_so_its_su2_is_not_the_weak_one
===============================================================================================

Object under test -- THE JOIN.  P14's body frames the undelivered gauge content as "a question
about the bundle: what does the operator act on, and what fixes it?"  On the ordinary route the bundle
is imposed; on a geometric route the substrate would supply it, and P14 lists the substrate's own
candidates -- the tangent bundle of the embedding space, "the spinor bundles it carries", the wall's
normal bundle, and the two ruling bundles -- settling that list for COLOUR by a real-form obstruction.

This receipt asks the same question for the WEAK su(2) of one candidate on that list.  The shared
S^4 where the two faces meet has spin group Spin(4) = SU(2)_+ x SU(2)_-, under which its chiral
spinors are (2,1) and (1,2): SU(2)_+ sees a doublet on one chirality and a singlet on the other,
the shape of a chiral SU(2).  Is its spinor bundle the one that supplies weak isospin?

--------------------------------------------------------------------------------
(1) EVERY FOUR-DIMENSIONAL CUT HAS THE CHIRALITY OF ITS OWN NORMAL.

  In the five-dimensional Clifford algebra of the substrate, the product of the four Clifford
  elements tangent to a four-dimensional hypersurface is proportional to the element of its normal.

    the PHYSICAL CUT is tangent to {X_0, a, b, c} with normal r_0:
        its chirality  gamma^0 gamma^1 gamma^2 gamma^3  is proportional to  gamma^{r_0}.
    P12: R reflects "the transverse cut-normal (r_0) direction ... and acts on the cut's natural
    spinor as the chirality operator gamma^5 itself".  So R = gamma^5 = gamma^{r_0}.

    the SHARED S^4 is tangent to {r_0, a, b, c} with normal X_0:
        its chirality  gamma^1 gamma^2 gamma^3 gamma^{r_0}  is proportional to  gamma^{X_0}.

--------------------------------------------------------------------------------
(2) THE TWO ANTICOMMUTE, AND THAT SETTLES THE JOIN.

  gamma^{X_0} and gamma^{r_0} are Clifford elements of different directions, so they anticommute.
  A state of definite SPHERE chirality is therefore an exactly equal mixture of PHYSICAL left and
  right -- computed, weights 0.500 and 0.500.

  SU(2)_+ is chiral with respect to the SPHERE's chirality: it acts on the sphere's positive
  chirality and trivially on its negative.  Each of those is an equal mixture of physical left and
  right.  So SU(2)_+ acts on physical left and right alike.

  ==> *** The weak SU(2) acts on ONE physical handedness.  The shared four-sphere's own chiral
      SU(2) acts on both.  So the spinor bundle on P14's list does not supply weak isospin: its
      chiral su(2) is chiral with respect to the wrong normal.  That extends P14's own settling of
      the substrate's bundles from colour to the weak su(2), for this candidate. ***

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.

  ** NOT that no geometric su(2) could be the weak one. **  What is shown is that the shared
  sphere's -- the one whose shape suggested it -- is chiral with respect to X_0 where the physical
  chirality is r_0.  A different construction is not addressed.

  ** NOT a claim about the physical cut's own spin group. **  Spin(3,1) splits into left and right
  Weyl representations and so acts on the physical chiralities separately, but it is the Lorentz
  group of spacetime, non-compact, and not an internal symmetry; weak isospin commutes with it.

  ** NOT that the index result of r6714 is wrong. **  It is correct for the sphere's own chirality.
  What this adds is that the sphere's chirality is not the physical one, so even a doublet there
  would not have been a physical chiral doublet.
"""

import numpy as np

s0=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]]); Z=np.zeros((2,2))
g0=np.block([[Z,s0],[s0,Z]]); g1,g2,g3=[np.block([[Z,s],[-s,Z]]) for s in (sx,sy,sz)]
g4=1j*g0@g1@g2@g3
G={0:g0,1:g1,2:g2,3:g3,4:g4}          # 0 = X_0, 4 = r_0, 1..3 the shared spatial legs
for i in G:
    for j in G:
        ac = G[i]@G[j] + G[j]@G[i]
        assert np.allclose(ac, 0) if i != j else True
print("  five mutually anticommuting Clifford elements                              OK")

def prop(A,B):
    for c in (1,-1,1j,-1j):
        if np.allclose(A, c*B): return c
chi_cut = G[0]@G[1]@G[2]@G[3]
chi_S4  = G[1]@G[2]@G[3]@G[4]
assert prop(chi_cut, G[4]) is not None and prop(chi_S4, G[0]) is not None
print("  cut chirality is proportional to gamma^{r_0}; sphere chirality to gamma^{X_0}  OK")

assert np.allclose(G[0]@G[4] + G[4]@G[0], 0)
print("  the two chirality operators anticommute                                    OK")

herm = lambda A: A if np.allclose(A, A.conj().T) else 1j*A
H_cut, H_S4 = herm(G[4]), herm(G[0])
w, v = np.linalg.eigh(H_S4); psi = v[:, np.argmax(w)]
p_plus = float(np.real(psi.conj() @ (0.5*(np.eye(4)+H_cut)) @ psi))
assert abs(p_plus - 0.5) < 1e-12
print(f"  a definite sphere-chirality state: physical weights {p_plus:.3f} / {1-p_plus:.3f}      OK")

print()
print("ESTABLISHED: every four-dimensional cut carries the chirality of its own normal. The physical")
print("cut's normal is r_0 and its chirality is P12's R = gamma^5; the shared S^4's normal is X_0 and")
print("its chirality is the X_0 element. The two anticommute, so a definite sphere chirality is an")
print("equal mixture of physical left and right, and the sphere's chiral SU(2)_+ acts on both physical")
print("handednesses. The weak SU(2) acts on one. So the spinor bundle on P14's list of the substrate's")
print("own candidates does not supply weak isospin -- extending P14's settling of that list from colour")
print("to the weak su(2), for this candidate.")
print("NOT CLAIMED: that no geometric su(2) could be the weak one. Nothing about the Lorentz group's own")
print("chiral split. And r6714's index result is correct for the sphere's chirality.")
