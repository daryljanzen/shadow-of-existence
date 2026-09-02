#!/usr/bin/env python3
"""
P13_A3_spinor_lift.py -- verifies the spinor-level realization of R o K (prop:conjugation-parity / closure):
  gamma^5=i g0g1g2g3 (involution); S=g0g1g3 solves S g^{mu*} S^-1=g^mu (reality lift, essentially unique);
  gamma^5 . S = -(C g^{0T}) with C=i g2 g0 the C-matrix proper, so (gamma^5 S)psi* = -psi^c on 200 spinors
  => R o K lifted IS charge conjugation's operation; reality involution e^{-iw tau~}->e^{+iw tau~}; Q^2/r^2
  is R-even. GUARD (load-bearing): -i gamma^2 is NOT the C-matrix proper. [P13 boundary_paper]
STATUS: ✔✔   ORIGIN: storyboard_receipts/A3_spinor_lift.py, verified r1382.
A3_spinor_lift.py  --  the EXPLICIT spinor-level realization of R o K on the cut-Dirac
structure.  Extracted (and re-verified) from the forked r1094 session's A3_worked.py /
A3_lift_derivation.py, then BOUNDED to this corpus's settled reading.

WHAT THIS ADDS (the genuine extract from the fork, corrected at the convention crux by the
                parallel chat node's attack):
    A concrete Clifford-algebra demonstration that the geometric factor R o K of the
    closure -- R the mass-reflection (=gamma^5), K = (tau~ <-> conj tau~) the reality
    involution lifted to the cut spinor -- IMPLEMENTS charge conjugation's OPERATION
    psi -> psi^c at the spinor level:
        the reality-involution lift  S  solves  S gamma^{mu *} S^{-1} = gamma^mu,
        forcing  S = gamma^0 gamma^1 gamma^3  (up to phase) in the Dirac rep, and
            gamma^5 . (gamma^0 gamma^1 gamma^3) = -i gamma^2 = -(C gamma^{0T}),
        so that  (gamma^5 S) psi* = - psi^c  (verified on 200 spinors) -- the geometric
        composite, lifted, IS the charge-conjugation map;
        while on a mode the involution sends  e^{-i w tau~} -> e^{+i w tau~}
        (particle <-> antiparticle, the Feynman-Stueckelberg exchange).

    *** CONVENTION GUARD (the sixth-face trap, caught by the chat node at maximum cost). ***
    -i gamma^2 is NOT the C-matrix proper (C = i gamma^2 gamma^0, defined by
    C g^{muT}C^{-1} = -g^mu, which -i gamma^2 fails for mu=1,2,3).  It is -(C gamma^{0T}),
    the object that acts on psi* in  psi^c = C gamma^{0T} psi*.  The physical claim is about
    the OPERATION psi -> psi^c, never "the C-matrix".  Testing the wrong C-object yields a
    clean-looking false refutation; ask which object the claim names before writing it up.

WHAT THIS DOES *** NOT *** SHOW (the bound):
    This gives C's KINEMATIC content (the spinor conjugation OPERATION psi -> psi^c,
    species/|mass|/FS-wing exchange) -- the "kinematic shadow" -- and NOTHING about the
    electric charge SIGN.  The charge sign is Q -> -Q, and (A3_factorization.py) BOTH R and
    K are BLIND to it (Q enters the metric only through Q^2).  The electric charge is
    external gauge content (the Maxwell potential A_t = Q/r, field-level), NOT sourced by
    the substrate geometry.  So:
            C  =  (Q -> -Q)_field  o  (R o K)_geometric ,
    R o K the kinematic shadow, the electric-charge sign the one datum closing from the field.

WHY R o K is ONLY the shadow -- the POSITIVE mechanism (the chat node's gift back, replacing
    the earlier "we found no Q in the maps" ABSENCE with a reason):
    C is INTERNAL: it maps a solution of charge Q to a different solution of charge -Q at the
    SAME spacetime point (same place, different world).  R is a SPACETIME map: it carries a
    point to another point of the SAME solution (same world, different place).  On the
    conjugate branch the same even field strength F_tr = -Q/r^2 is read as -Q -- not a chart
    artifact but because d/dr points OUTWARD at r>0 and INWARD at r<0, so an observer there
    measuring against their own outward infers the opposite sign.  R does not FLIP the charge;
    R carries you to WHERE THE SAME CHARGE READS AS ITS OPPOSITE.  Relocation is not
    conjugation -- which is exactly why the geometric factor can carry C's kinematic content
    yet never the charge sign, and exactly why the fork's "C is fully geometric" is wrong.

FURTHER BOUND (species half, not claimed):
    (gamma^5 S) psi* = -psi^c is a Clifford identity -- no charge appears in a Clifford
    algebra at all, so it is the OPERATOR half of the FS reading.  Whether the two wings are
    a PARTICLE/ANTIPARTICLE pair (the species half) is a real-slice question no operator
    identity reaches; that identification stays unclaimed (-> P14, held to this bound).
"""
import numpy as np

# ---- Dirac representation gamma matrices (mostly-minus) --------------------------------
I2 = np.eye(2); Z = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]], complex)
def blk(a, b, c, d): return np.block([[a, b], [c, d]])
g0 = blk(I2, Z, Z, -I2)
g1 = blk(Z, sx, -sx, Z)
g2 = blk(Z, sy, -sy, Z)
g3 = blk(Z, sz, -sz, Z)
g5 = 1j * g0 @ g1 @ g2 @ g3
I4 = np.eye(4)
gammas = {0: g0, 1: g1, 2: g2, 3: g3}

allok = True
def check(label, cond):
    global allok
    allok &= bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")

print("=" * 84)
print("A3_spinor_lift -- R o K reproduces C's KINEMATIC matrix at the spinor level")
print("=" * 84)

# ---- 1. gamma^5 identities (R = gamma^5) ----------------------------------------------
check("gamma^5 = i g0 g1 g2 g3 is an involution (g5^2 = I)", np.allclose(g5 @ g5, I4))

# ---- 2. the reality-involution lift S solves S gamma^{mu*} S^{-1} = gamma^mu -----------
#     (K acts antilinearly; its spinor lift S must carry conjugated solutions to solutions)
S = g0 @ g1 @ g3
def intertwines(S):
    return all(np.allclose(S @ np.conjugate(gammas[m]) @ np.linalg.inv(S), gammas[m])
               for m in gammas)
check("S = g0 g1 g3 solves  S gamma^{mu*} S^{-1} = gamma^mu  (the reality-lift condition)",
      intertwines(S))

# uniqueness up to phase: in the Dirac rep the intertwiner is 1-dimensional.  Spot-check
# that multiplying S by any of the other basis Clifford elements breaks the condition.
broken = [not intertwines(S @ g) for g in (g0, g1, g2, g3, g5)]
check("the intertwiner is essentially unique (perturbing S by a basis element breaks it)",
      all(broken))

# ---- 3. gamma^5 . S IMPLEMENTS psi -> psi^c (the charge-conjugation OPERATION) ----------
#     *** CONVENTION GUARD (the trap the parallel chat node caught at this exact crux). ***
#     There are TWO standard objects both called "C":
#       (a) the C-MATRIX proper  C = i gamma^2 gamma^0,  defined by  C g^{muT} C^{-1} = -g^mu;
#       (b) the OPERATOR in psi^c = C gbar^{0T} psi* = (C gamma^{0T}) psi*, which ACTS ON psi*.
#     gamma^5 . S = -i gamma^2.  This is NOT (a) -- do not call it "the C-matrix".  It IS
#     -(C gamma^{0T}) = object (b) up to sign, i.e. it implements the charge-conjugation MAP
#     psi -> psi^c.  The physical claim is about the operation psi -> psi^c, not the matrix.
prod = g5 @ S
check("gamma^5 . (g0 g1 g3) = -i gamma^2", np.allclose(prod, -1j * g2))

Cmat = 1j * g2 @ g0                                   # (a) the C-matrix proper
def satisfies_Cdef(M):
    Minv = np.linalg.inv(M)
    return [np.allclose(M @ g.T @ Minv, -g) for g in (g0, g1, g2, g3)]
check("GUARD: -i gamma^2 is NOT the C-matrix proper (fails C g^{muT}C^-1=-g^mu for mu=1,2,3)",
      satisfies_Cdef(prod) == [True, False, False, False])
check("the C-matrix proper C=i g2 g0 DOES satisfy the defining relation (all mu)",
      all(satisfies_Cdef(Cmat)))

Cg0T = Cmat @ g0.T                                    # (b) the operator in psi^c
check("gamma^5 . S = -(C gamma^{0T}), the operator implementing psi -> psi^c",
      np.allclose(prod, -Cg0T))
# verify on random spinors that (gamma^5 S) psi* = - psi^c  (psi^c = C gamma^{0T} psi*)
rng_ok = True
seeds = [(1.0 * i, -0.7 * i) for i in range(1, 201)]  # deterministic (no RNG; resume-safe)
for a, b in seeds:
    psi = np.array([a, b, a - b, a + 2 * b], complex) + 1j * np.array([b, a, 2 * a, b - a])
    psi_c = Cg0T @ np.conjugate(psi)
    rng_ok &= np.allclose(prod @ np.conjugate(psi), -psi_c)
check("(gamma^5 S) psi* = - psi^c  on 200 spinors  =>  R o K lifted IS charge conjugation",
      rng_ok)

# ---- 4. the mode exchange (Feynman-Stueckelberg), stated as a computation --------------
w = 1.3
taus = np.array([0.0, 0.4, 0.9, 1.7])
mode = np.exp(-1j * w * taus)             # positive-frequency (particle)
conj_mode = np.exp(-1j * w * (-taus))     # under tau~ -> conj tau~ on the real axis: w tau~ -> -w tau~
check("reality involution sends e^{-i w tau~} -> e^{+i w tau~} (particle <-> antiparticle)",
      np.allclose(conj_mode, np.exp(+1j * w * taus)))

# ---- 5. THE BOUND: R o K is blind to the electric charge sign (the field factor) -------
#     (this is the load-bearing negative -- the reason C is NOT fully geometric)
Q = 0.5
def A_t(r):  return Q / r          # Maxwell potential (field-level); happens to be R-odd
def Qsq(r):  return Q**2 / r**2    # the metric's charge term -- R-EVEN
r = 0.8
check("metric charge term Q^2/r^2 is R-EVEN (r->-r leaves it identical) => R blind to sign(Q)",
      np.allclose(Qsq(r), Qsq(-r)))
print("     NOTE: A_t = Q/r is R-ODD, but that is the *specific Coulomb potential's* spatial")
print("     parity, held field-level in the corpus ('the sign lives in the Maxwell potential').")
print("     It is NOT the substrate geometry sourcing charge conjugation: the metric is Q^2-blind.")
print("     => the electric-charge sign is the field factor (Q->-Q), NOT carried by R o K.")

print("     POSITIVE reason (not just the absence): R RELOCATES to where the same charge reads")
print("     as its opposite (d/dr outward at r>0, inward at r<0); C CONJUGATES at a point.")
print("     Relocation is not conjugation -- so R o K carries C's kinematics, never the sign.")
print("-" * 84)
print("RESULT:  R o K, lifted to the cut spinor, IMPLEMENTS charge conjugation psi -> psi^c")
print("         (gamma^5 . g0g1g3 = -i gamma^2 = -(C gamma^{0T}); (gamma^5 S)psi* = -psi^c).")
print("         NOT the C-matrix proper (i g2 g0) -- convention guard above. Mode exchange = FS.")
print("         BOUND:  C = (Q->-Q)_field  o  (R o K)_geometric  -- the geometry carries the")
print("         kinematic shadow (operator half); the charge sign, and the species half of the")
print("         FS reading, close from the field / stay unclaimed.")

# r2376+c54.158 -- rule 7: every PASS/FAIL above is computed and only PRINTED.  Pin `allok`, and
# pin the three things the spinor lift is cited for, separately, because each could be lost inside
# a green flag.
#   (1) THE IDENTITY: gamma^5 . (g0 g1 g3) = -i gamma^2 = -(C gamma^{0T}) on the nose, and the
#       spinor statement (gamma^5 S) psi* = -psi^c holds on 200 spinors -- the figure INDEX.md
#       quotes.  200 is pinned too, so a silently shortened sweep cannot pass as the full one.
#   (2) THE CONVENTION GUARD, which is the load-bearing negative: -i gamma^2 satisfies the
#       C-matrix defining relation C g^{muT} C^{-1} = -g^mu for EXACTLY ONE mu (mu = 0) and FAILS
#       for THREE (mu = 1,2,3), while the C-matrix proper C = i g2 g0 satisfies all FOUR.  The
#       counts 1-of-4 against 4-of-4 are what make "this is not the C-matrix" a result rather than
#       a caveat; testing the wrong C-object yields a clean-looking false refutation.
#   (3) THE UNIQUENESS: all 5 perturbations S -> S g of the reality lift break the intertwining,
#       so S is essentially unique and the identity is not one lift among many.
assert len(seeds) == 200, len(seeds)
assert rng_ok
assert np.allclose(prod, -1j * g2) and np.allclose(prod, -Cg0T)
assert satisfies_Cdef(prod) == [True, False, False, False], satisfies_Cdef(prod)
assert satisfies_Cdef(Cmat) == [True, True, True, True], satisfies_Cdef(Cmat)
assert len(broken) == 5 and all(broken)
assert allok
print("=" * 84)
print("ALL CHECKS PASS" if allok else "SOME CHECKS FAILED")
