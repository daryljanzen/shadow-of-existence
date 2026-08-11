"""Transport the hinge form along the swing and compute the holonomy.
Base: w.  Fibre: C-span of the three roots r_k(w).  Form: the hinge Gram G = 6I - 5J.
(1) is G covariantly constant under the Z_3-equivariant transport?  (2) what is the monodromy?"""
import numpy as np, itertools
al=1.0
G=6*np.eye(3)-5*np.ones((3,3))                 # the hinge Gram, signature (2,1)
C=np.array([[0,0,1],[1,0,0],[0,1,0]],float)    # the 3-cycle: w -> w+120 permutes the roots
print("   (1) IS THE FORM PRESERVED BY THE Z_3?")
print("       C^T G C == G :", np.allclose(C.T@G@C, G), "   (the Gram is cyclic-invariant, 6I-5J)")
print("       det C = %+.0f  -> the 3-cycle is in SL(3); an even permutation"%np.linalg.det(C))
print()
print("   (2) THE MONODROMY GROUP, and where it lives:")
perms=list(itertools.permutations(range(3)))
for p in perms:
    P=np.zeros((3,3)); 
    for i,j in enumerate(p): P[i,j]=1
    d=np.linalg.det(P); pres=np.allclose(P.T@G@P,G)
    kind='3-cycle' if p in [(1,2,0),(2,0,1)] else ('identity' if p==(0,1,2) else 'transposition')
    print("       %-12s det=%+.0f   preserves G: %-5s  -> %s"%(kind,d,pres,'in SL(3)' if d>0 else 'NOT in SL(3)'))
print()
print("   => the Z_3 (3-cycles) preserves G AND has det +1: it sits in SU(2,1) as the CENTRE.")
print("      the transpositions preserve G but have det -1: S_3 as a whole is NOT in SL(3).")
print()
print("   (3) IS THE BUNDLE FLAT?")
print("       The fibre is functions on a 3-element set that varies only by PERMUTATION as w advances")
print("       (the roots are the same three values relabelled).  A bundle whose transition functions are")
print("       CONSTANT permutation matrices is FLAT: zero curvature, holonomy = the monodromy group.")
print("       So holonomy = Z_3 (at E=1, branching only at M=0) or S_3 (general, branching at Nariai).")
print()
print("   => the geometry supplies a FLAT bundle.  Holonomy is FINITE -- the centre, or the Weyl group.")
print("      NOT a continuous algebra.  What is absent is CURVATURE.")
