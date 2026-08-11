"""Which embedding of S_4 in O(3) is our group?  Distinguish by invariants:
 - rotational cube group (chiral octahedral, O): all det +1, contains 6 four-fold rotations (order 4, det +1)
 - full tetrahedral group T_d: det +-1, order-4 elements are IMPROPER (S_4 rotoreflections, det -1)
W(A_3) acting on the A_3 root space is T_d.  W(B_3) is the FULL octahedral group O_h, order 48."""
import numpy as np, itertools
def key(M): return tuple(np.round(M.flatten(),6))
def close(gens, cap=200):
    G={key(np.eye(3)):np.eye(3)}; fr=[np.eye(3)]
    while fr:
        new=[]
        for M in fr:
            for g in gens:
                P=g@M
                if key(P) not in G: G[key(P)]=P; new.append(P)
        fr=new
        if len(G)>cap: break
    return list(G.values())
C=np.array([[0,0,1],[1,0,0],[0,1,0]],float)
T=np.array([[0,1,0],[1,0,0],[0,0,1]],float)
H1=np.diag([1.,-1.,-1.]); H2=np.diag([-1.,1.,-1.])
G=close([C,T,H1,H2])
print("   our family+holonomy group: order %d"%len(G))
def order(M):
    P=M.copy()
    for k in range(1,13):
        if np.allclose(P,np.eye(3)): return k
        P=P@M
    return None
from collections import Counter
prof=Counter((order(M), int(round(np.linalg.det(M)))) for M in G)
print("   (element order, det) profile:")
for k in sorted(prof): print("      order %s  det %+d :  %d elements"%(k[0],k[1],prof[k]))
print()
n4p=prof.get((4,1),0); n4m=prof.get((4,-1),0)
print("   order-4 elements with det +1 (proper 4-fold rotations): %d"%n4p)
print("   order-4 elements with det -1 (improper, rotoreflections): %d"%n4m)
print()
if n4m>0 and n4p==0:
    print("   => the order-4 elements are IMPROPER  ->  this is T_d, the FULL TETRAHEDRAL group")
    print("      which is exactly W(A_3) acting on the A_3 root space.")
elif n4p>0 and n4m==0:
    print("   => the order-4 elements are PROPER rotations -> chiral octahedral O (cube rotations),")
    print("      NOT the Weyl-group embedding.")
else:
    print("   => mixed; inspect further.")

# r2376+c54.158 -- pins the invariant this receipt exists to read off, at the figures it prints.
# The generated group has order 24, and T_d and the chiral octahedral group O BOTH have order 24 --
# order alone cannot tell them apart, which is why the receipt asks for the (order, det) profile.
# The discriminator is the order-4 class: 6 elements of order 4, EVERY one of them IMPROPER
# (det -1, rotoreflections S_4), and NOT ONE proper four-fold rotation.  That is T_d = W(A_3) and
# not O, and it is the sec:weyl-a3 identification.  Full profile pinned with it: 1 identity,
# 6 reflections (order 2, det -1), 3 half-turns (order 2, det +1), 8 three-fold rotations.
assert len(G) == 24, len(G)
assert (n4p, n4m) == (0, 6), (n4p, n4m)
assert dict(prof) == {(1, 1): 1, (2, -1): 6, (2, 1): 3, (3, 1): 8, (4, -1): 6}, dict(prof)
assert sum(prof.values()) == 24 and sum(v for (o, d), v in prof.items() if d == -1) == 12
