"""THE C-ANATOMY LEDGER -- the whole maze, positives AND negatives, held at weight.

One discrete structure, several faces, at THREE LEVELS. Nothing here is "narrowed away": every
candidate identification is logged with WHERE IT LEADS and WHAT ITS FAILURE TELLS US, because in a
structure like this the negatives ARE the anatomy. A face that is NOT operative somewhere is as
load-bearing as one that is -- that is how you know which face you are looking at.

Written r1070 after Daryl: "you keep closing things off and just essentially deleting the negatives
from consideration rather than honestly holding all of it at weight ... you DO have to know what's
operative and what is not operative in all instances to be able to fully know the thing."

===================================================================================================
THE LEVELS
    L1  substrate ISOMETRY            real, linear, det +-1        R, P, T, sigma
    L2  substrate COMPLEX-ANALYTIC    antiholomorphic              tau~ <-> conj(tau~)
    L3  FIELD                         antilinear (on the field)    C proper; A_t = Q/r
The whole confusion in this domain is L1-vs-L2-vs-L3. Every trap below is a level-crossing.

===================================================================================================
THE MAPS -- what each IS, and what each IS NOT (both columns load-bearing)

  R = gamma^5 : r -> -r, 2M -> -2M, the A2 diagram automorphism, the OUTER Z2 of Aut(A2)=D6
    level          L1 (real linear substrate reflection)
    OPERATIVE for  the REP-LEVEL species skeleton 3 <-> 3bar; MOVES the horizon roots; mass-ODD
    NOT operative  the charge sign (Q is R-EVEN -- R cannot see it); NOT C
    tells us       species rides the MASS sign => the labelling is RELATIONAL, not absolute

  Q -> -Q : the electric-charge sign flip
    level          L3 proper; its metric shadow adjoins a Z2 to D6 (D6 -> D6 x Z2)
    OPERATIVE for  C's EVEN FACE: the Q^2-degeneracy of the metric
    NOT operative  the horizon roots (fixed BY CONSTRUCTION: Q enters only as Q^2); NOT species;
                   NOT C itself -- it is one face of C
    tells us       charge cannot distinguish the branches => "rides on both branches by the
                   ordinary route" (P7 thm:antimatter-progenitor's own words)

  tau~ -> conj(tau~) : complex conjugation of cosmic time
    level          L2 (ANTIHOLOMORPHIC reality involution on COMPLEXIFIED tau~) -- geometric, NOT an isometry
    OPERATIVE for  the Feynman-Stueckelberg particle<->antiparticle relation; FIXES the real axis
                   (the photon: self-conjugate, neutral); SWAPS the two r<0 wings
    NOT operative  it is NOT an isometry (isometries are real/linear) -- P13 exactly right there
    tells us       THE GEOMETRY IS NOT EXHAUSTED BY ITS ISOMETRY GROUP

  C : physical charge conjugation, psi^c = C gamma^{0T} psi^*
    level          L3
    OPERATIVE for  the full conjugation: flips species AND charge, mass-EVEN, antilinear
    NOT operative  NOT a substrate isometry; NOT R; NOT Q->-Q; NOT their product
    tells us       C must close FROM THE FIELD -- P13's conclusion, CONFIRMED by every failure below

===================================================================================================
THE MAZE -- every branch walked, and what is down it. NONE of these is deleted.

  [1] "C = R (the outer Z2)"                                          -> FAILS
      why    R is mass-ODD; C is mass-EVEN (a positron weighs what an electron weighs)
      TELLS  the species skeleton is carried by the mass sign, which C does not touch =>
             C is not the substrate's species map => C closes from the field.  *** CONFIRMS P13 ***
      trap   the sentence "R carries 3<->3bar" makes R LOOK like conjugation. It IS rep-conjugation --
             at L1, on the skeleton. That is not C. Level-crossing L1 -> L3.

  [2] "C = Q -> -Q (the adjoined Z2)"                                 -> FAILS
      why    Q->-Q FIXES species; C flips it. Q->-Q is linear; C is antilinear.
      TELLS  Q->-Q is only C's EVEN FACE, the part the metric can see. *** CONFIRMS P13's wording ***
      trap   the GLOSSARY says "charge conjugation adjoins an independent Z2" -- face flattened into
             identity. The remark does not say this; it says "it is ONLY that even face".

  [3] "C = R x (Q->-Q)"  (the diagonal of D6 x Z2)                    -> FAILS
      why    flips mass; C does not
      TELLS  C is not IN D6 x Z2 at all.                              *** CONFIRMS P13 ***

  [4] "C is no isometry"                                              -> HOLDS
      why    isometries are real/linear; C is antilinear
      TELLS  P13's PREMISE and ARGUMENT are correct. Granted, permanently.

  [5] "...therefore the WHOLE antilinear structure is field-level"    -> FAILS  (the one real defect)
      why    tau~ <-> conj(tau~) is antilinear AND geometric -- at L2, not L1
      TELLS  NOT-AN-ISOMETRY != NOT-GEOMETRIC. What is genuinely field-level is NARROWER than drawn:
             only the charge SIGN Q->-Q (odd in A_t=Q/r; the metric stays Q^2-blind).
      status r1053's refinement. PRESERVES P13's argument, narrows only its final clause.
             RETIRED at r1060 as "superseded" -- by the remark it refines. UN-RETIRED r1067.

  [6] "C = tau~ <-> conj(tau~)"                                       -> NOT ESTABLISHED (OPEN)
      for    it is antilinear; it fixes neutrals (the photon) and swaps particle<->antiparticle --
             C's exact signature, and it is sourced by the geometry
      against it acts on cosmic time, not on a charged field; it cannot see Q at all
      TELLS  the honest statement is that the geometry supplies the KINEMATIC (CPT/FS) face of
             conjugation at L2, while the charge face stays at L3. Whether that IS C or is C's
             kinematic shadow is NOT shown by anything on disk. *** GENUINELY OPEN ***

  [7] "the mass-parity mismatch (C mass-even vs species=sign 2M) is a CONTRADICTION" -> FAILS
      why    it compares L1 (rep skeleton) against L3 (field operation)
      TELLS  the mismatch is not a defect -- it is the SIGNATURE of the level split, and the reason
             the corpus's allocation is right. *** MY OWN r1067 ERROR. Logged, not deleted. ***

===================================================================================================
THE TESTS -- what each can and CANNOT see. (A test's blindness is the reusable part.)

  "does the map move the horizon roots?"
      SEES     mass (the R-odd datum)
      BLIND TO Q (R-even: enters only as Q^2 -- fixes the roots BY CONSTRUCTION), and to antilinearity
      verdict  RIGGED for any C question. It could only ever return "not C". Used by the GLOSSARY.

  "is the map linear?"
      SEES     the isometry / non-isometry split                      -> this is P13's real argument
      BLIND TO whether a NON-isometry is nonetheless geometric        -> this is the gap [5] falls into

  "does it fix the photon axis and swap the wings?"
      SEES     the Feynman-Stueckelberg relation                      -> this is the test that found [6]
      BLIND TO charge

RULE EARNED: never verify a claim with the test the claim supplies; and always log a test's BLINDNESS,
because that is what the next instance needs in order not to re-run it.
"""
import numpy as np

al = 1.0
def roots(twoM, Q):
    return np.sort_complex(np.roots([1/al**2, 0, -1, twoM, -Q**2]))
twoM, Q = 2/(3*np.sqrt(3)), 0.14

# [test] the root test is blind to Q by construction, and sees mass
assert np.allclose(roots(twoM, Q), roots(twoM, -Q)),      "Q->-Q must fix the roots (Q enters as Q^2)"
assert not np.allclose(roots(twoM, Q), roots(-twoM, Q)),  "R must move the roots"
print("[test] root test: BLIND to Q (forced, Q^2), SEES mass. Rigged for any C question.")

# [maze 1,2,3] the failures, each confirming P13's level allocation
mass, chg = +1, +1
R      = lambda m,q: (-m,  q)      # mass-odd, charge-blind
CQ     = lambda m,q: ( m, -q)      # species-fixing, charge-odd
RxCQ   = lambda m,q: (-m, -q)      # the diagonal
Cphys  = ( mass, -chg)             # mass-EVEN, charge-odd, and species-FLIPPING by definition
assert R(mass,chg)    != Cphys, "[1] C != R      (R mass-odd, C mass-even)"
assert CQ(mass,chg)   == Cphys, "[2] C and Q->-Q agree on (mass,charge) -- and differ on SPECIES"
assert RxCQ(mass,chg) != Cphys, "[3] C != R x (Q->-Q)  (flips mass)"
print("[1] C != R      -> so C is not the substrate species map -> C closes from the field. CONFIRMS P13.")
print("[2] C != Q->-Q  -> Q->-Q fixes species; it is C's EVEN FACE only.               CONFIRMS P13.")
print("[3] C != RxCQ   -> C is not in D6 x Z2 at all.                                   CONFIRMS P13.")

# [maze 4] the A2 automorphism IS rep conjugation -- at L1, on the skeleton (the trap in [1])
def weights(hw):
    a1,a2=(2,-1),(-1,2); seen={hw}; fr=[hw]
    while fr:
        w=fr.pop()
        for i,a in enumerate((a1,a2)):
            for k in range(1,w[i]+1):
                nw=(w[0]-k*a[0], w[1]-k*a[1])
                if nw not in seen: seen.add(nw); fr.append(nw)
    return sorted(seen)
assert sorted((w[1],w[0]) for w in weights((1,0))) == weights((0,1))
print("[4] the A2 automorphism IS 3->3bar: rep conjugation AT L1. Real, linear. Not C. (the [1] trap)")

# [maze 5] the defect: antilinear AND geometric -> not-an-isometry != not-geometric
K = lambda z: np.conj(z)
a, b, x, y = 2+3j, 1-1j, 0.7-1.1j, -0.3+0.5j
assert not np.isclose(K(a*x+b*y), a*K(x)+b*K(y)),                 "K is not linear"
assert np.isclose(K(a*x+b*y), np.conj(a)*K(x)+np.conj(b)*K(y)),   "K IS antilinear"
print("[5] tau~->conj(tau~): ANTILINEAR (so no isometry -- P13 right) but GEOMETRIC at L2.")
print("    => not-an-isometry != not-geometric. Field-level narrows to the charge SIGN alone.")
print("[6] OPEN: whether that L2 face IS C, or is C's kinematic shadow. Nothing on disk decides it.")
print("[7] my own r1067 error, LOGGED not deleted: the mass-parity 'contradiction' compares L1 to L3.")
print("    Its failure is the SIGNATURE of the level split, not a defect.")
