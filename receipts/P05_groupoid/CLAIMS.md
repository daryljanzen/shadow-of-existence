# P5 — groupoid_paper — claim inventory (Avenue 11 sweep, r1349; growing)
The description groupoid; two generators (sigma root-exchange, R orientation); Aut(A2)=S3xZ2=D6; deck group S3; rigidity as dimensional collapse; the fixed-point cosmology.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | rem:orientation | R (r->-r) conjugates 3<->3bar iff -1 not in W(A2); -1 in W for A1xA1/B2/G2 | YES | `negation_outer_A2.py` | ✔✔ |
| 2 | sec:classification | <S3,R>=S3xZ2=D6 (discrete symmetry of the solution space) | YES | `P05_deck_group_S3.py` | ✔✔ |
| 3 | prop:monodromy/prop:deck/rem:galois | deck group of the 3-sheeted cover = S3 (Nariai monodromies=transpositions, = Galois group) | YES | `P05_deck_group_S3.py` | ✔✔ |
| 4 | sec:rigidity | rigidity as dimensional collapse | likely analytic | — | ? |
| 5 | sec:single-reassignment | single-reassignment uniqueness | likely analytic | — | ? |

**P5 at bar (computational core):** rem:orientation ✔✔, deck-S3/monodromy/Galois/D6 ✔✔. Rigidity/single-reassignment (#4,#5) are analytic (dimensional-collapse + uniqueness arguments), not receipt computations.
