"""Q6-CONFIRMED — the polar slice sits at RUNG 2, and that answers A18.
CONFIRMATION 1 (ontology): section 0's five-rung ladder. Rung 1 = the substrate dS_5 = SO(5,1)/SO(4,1).
Rung 2 = 'A CUT of the substrate -- a four-geometry. dS_4 is one such: the maximally symmetric one...
A geometry is a cut exactly when its isometry group contains a sweep-subgroup of the substrate's.'

ORIGIN: storyboard_receipts/Q6r_polar_is_the_background.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
eta=np.diag([-1,1,1,1,1,1.0]); al=1.0
print("="*74); print("Q6r — THE POLAR SLICE IS THE dS_4 BACKGROUND (rung 2)"); print("="*74)
P=np.array([0,1,0,0,0,0.0])*al
print(f"\n  substrate point P:  eta(P,P) = {P@eta@P:.4f}  = alpha^2 > 0")
B=[]
for i in range(6):
    e=np.zeros(6); e[i]=1
    B.append(e - (P@eta@e)/(P@eta@P)*P)
Q=[b for b in B if np.linalg.norm(b)>1e-9]
G=np.array([[a@eta@c for c in Q] for a in Q]); ev=[e for e in np.linalg.eigvalsh(G) if abs(e)>1e-9]
print(f"  polar hyperplane dim = {len(ev)};  induced signature = "
      f"({sum(1 for e in ev if e<0)} neg, {sum(1 for e in ev if e>0)} pos)  -> (1,4)")
print("\n  So the substrate cut by the polar is a totally geodesic dS_4, isometry SO(4,1).")
print("  SO(4,1) < SO(5,1) is a sweep-subgroup, so by section 0's own criterion THIS IS A CUT --")
print("  and being maximally symmetric it is THE dS_4 BACKGROUND, rung 2.")
print("\n  *** A18 asked how the background dS_4 sits in the substrate dS_5.  POLARITY IS THE ANSWER: ***")
print("  *** the background is the polar slice of a substrate point, and the point it is polar to ***")
print("  *** is what selects it.  One background per substrate point, none privileged.            ***")
print("="*74)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  The run above computed the signature at ONE point and ONE alpha
# and printed the rest -- the totally geodesic character, the isometry SO(4,1), the "one
# background per substrate point" -- as prose.  Here:
#   (1) the signature (1,4) is asserted at 40 RANDOM substrate points and at three scales
#       alpha = 1, 2.5, 7.3, so "one per substrate point, none privileged" is tested;
#   (2) the section is exhibited: Y in P^perp with eta(Y,Y) = alpha^2 is a dS_4 of radius alpha
#       (pinned at alpha = 2.5, where alpha^2 = 6.25);
#   (3) TOTAL GEODESY is computed, not asserted: the eta-reflection in P is an isometry of the
#       substrate whose fixed-point set is exactly the section, and a fixed-point set of an
#       isometry is totally geodesic;
#   (4) the ISOMETRY GROUP is counted, not named: the subalgebra of so(5,1) annihilating P has
#       dimension 10 = dim so(4,1), out of dim so(5,1) = 15.
def signature_of_perp(Pv):
    Bv = [np.eye(6)[i] - (Pv@eta@np.eye(6)[i])/(Pv@eta@Pv)*Pv for i in range(6)]
    Qv = [bv for bv in Bv if np.linalg.norm(bv) > 1e-9]
    Gv = np.array([[u@eta@v for v in Qv] for u in Qv])
    e_v = [e for e in np.linalg.eigvalsh(Gv) if abs(e) > 1e-9]
    return len(e_v), sum(1 for e in e_v if e < 0), sum(1 for e in e_v if e > 0)
assert signature_of_perp(P) == (5, 1, 4)                      # the printed row, now pinned
rng_q = np.random.default_rng(1961)
for al_v in (1.0, 2.5, 7.3):
    for _ in range(40):
        v = rng_q.normal(size=6)
        if v@eta@v <= 1e-6:
            v[1:] *= 4
        if v@eta@v <= 1e-6:
            continue
        Pv = v*al_v/np.sqrt(v@eta@v)                          # a substrate point at this alpha
        assert abs(Pv@eta@Pv - al_v**2) < 1e-9
        assert signature_of_perp(Pv) == (5, 1, 4)
        if abs(al_v - 2.5) < 1e-12:                           # the section IS dS_4 of radius alpha
            w = rng_q.normal(size=6)
            w = w - (Pv@eta@w)/(Pv@eta@Pv)*Pv                 # w in P^perp
            if w@eta@w > 1e-6:
                Y = w*al_v/np.sqrt(w@eta@w)
                assert abs(Y@eta@Y - 6.25) < 1e-9 and abs(Pv@eta@Y) < 1e-9
        R = np.eye(6) - 2*np.outer(Pv, eta@Pv)/(Pv@eta@Pv)    # the eta-reflection in P
        assert np.allclose(R.T@eta@R, eta, atol=1e-9)         # an ISOMETRY of the ambient
        assert np.allclose(R@R, np.eye(6), atol=1e-9)
        w2 = rng_q.normal(size=6)
        w2 = w2 - (Pv@eta@w2)/(Pv@eta@Pv)*Pv
        assert np.allclose(R@w2, w2, atol=1e-9)               # fixed set = P^perp: totally geodesic
        assert np.linalg.norm(R@Pv - Pv) > 1e-3               # and P itself is NOT fixed
so51 = [np.linalg.inv(eta)@S for S in
        [np.eye(6)[:, [i]]@np.eye(6)[[j], :] - np.eye(6)[:, [j]]@np.eye(6)[[i], :]
         for i in range(6) for j in range(i+1, 6)]]
assert len(so51) == 15                                        # dim so(5,1)
for A in so51:
    assert np.allclose(A.T@eta + eta@A, 0, atol=1e-12)
stab = np.array([A@P for A in so51]).T                        # generators killing P
assert 15 - np.linalg.matrix_rank(stab) == 10                 # dim so(4,1) = 10
print("  [r2376+c54.161] signature (1,4) asserted at 120 substrate points over alpha = 1, 2.5,")
print("  7.3; the section pinned as dS_4 of radius alpha; total geodesy computed from the")
print("  reflection's fixed set; and the stabiliser subalgebra counted: 15 - 5 = 10 = dim so(4,1).")
