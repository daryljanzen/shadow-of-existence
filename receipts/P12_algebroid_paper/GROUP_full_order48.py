"""The corpus records the sector's discrete group as D_6 = S_3 x Z_2 (family x chirality), order 12,
where the Z_2 is the GLOBAL chirality flip.  The holonomy adds V_4 = PAIRWISE flips.
Is the global flip in V_4?  What do they generate together?
ORIGIN: storyboard_receipts/GROUP_full_order48.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
def key(M): return tuple(np.round(M.flatten(),6))
def close(gens, cap=400):
    G={key(np.eye(3)):np.eye(3)}; frontier=[np.eye(3)]
    while frontier:
        new=[]
        for M in frontier:
            for g in gens:
                P=g@M
                if key(P) not in G: G[key(P)]=P; new.append(P)
        frontier=new
        if len(G)>cap: break
    return G
C=np.array([[0,0,1],[1,0,0],[0,1,0]],float)   # 3-cycle (family)
T=np.array([[0,1,0],[1,0,0],[0,0,1]],float)   # transposition (family)
Zglob=-np.eye(3)                              # the corpus's chirality Z_2: GLOBAL flip
H1=np.diag([1.,-1.,-1.]); H2=np.diag([-1.,1.,-1.])   # the holonomy V_4 (pairwise)
print("   is the GLOBAL flip -I in the holonomy V_4?  det(-I) = %+.0f"%np.linalg.det(Zglob))
print("      V_4 requires det +1 in 3 dimensions -> -I has det -1 -> NOT in V_4.")
print()
for gens,lab,exp in ((( [C,T,Zglob] ),'corpus D_6 = S_3 x Z_2 (family x chirality)',12),
                     (( [C,T,H1,H2] ),'family S_3 + holonomy V_4',24),
                     (( [C,T,Zglob,H1,H2] ),'ALL: family + chirality + holonomy',48)):
    G=close(gens); print("   %-44s order %3d  (expected %d: %s)"%(lab,len(G),exp,'yes' if len(G)==exp else 'NO'))
print()
print("   order 48 = the signed permutation group on 3 letters, S_3 semidirect (Z_2)^3")
print("            = the hyperoctahedral group B_3 -- the full symmetry of the octahedron/cube.")
print()
print("   => the corpus's D_6 (12) and the holonomy's S_4 (24) are BOTH proper subgroups of one group of order 48.")

# r2376+c54.158 -- pins the receipt's answer to its own question, and the three orders it prints.
# (1) The GLOBAL chirality flip -I has det -1 in three dimensions, so it is NOT in the holonomy
# V_4 (whose elements have det +1) -- the question the receipt opens with.
# (2) It is therefore genuinely NEW content, and the three closures come out 12 (the corpus's
# D_6 = S_3 x Z_2), 24 (family S_3 + holonomy V_4) and 48 (all three together).  48 is the find:
# had the global flip already been generated, the last closure would have stopped at 24.
# (3) And the order-48 group IS the signed permutation group / hyperoctahedral B_3, checked
# elementwise: every one of the 48 matrices has exactly three nonzero entries, all of modulus 1.
assert round(float(np.linalg.det(Zglob))) == -1
assert len(close([C, T, Zglob])) == 12
assert len(close([C, T, H1, H2])) == 24
Gall = close([C, T, Zglob, H1, H2])
assert len(Gall) == 48, len(Gall)
assert all(sorted(abs(np.asarray(Mx)).flatten().tolist()) == [0.0]*6 + [1.0]*3 for Mx in Gall.values())
