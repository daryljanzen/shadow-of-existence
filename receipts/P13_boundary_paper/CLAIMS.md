# P13 — boundary_paper — claim inventory (Avenue 11 sweep, r1379)
The geometric-isometry boundary: where CR's geometric core ends and the gauge/field sector begins. 0 equations
-- heavily conceptual. Propositions on the boundary, conjugation parity, charge-conjugation factorisation, residue.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | prop:conjugation-closure | C=(Q->-Q)_field o (R o K)_geometric on the bead; R o K blind to sign(Q) | YES | `P13_A3_factorization.py` | ✔✔ (existing storyboard receipt) |
| 2 | prop:boundary | SM gauge group is not a substrate isometry | STRUCTURAL | — | analytic |
| 3 | prop:conjugation-parity | R=gamma^5 (grades chirality); mass odd/charge even; R!=P | YES | `P13_conjugation_parity.py` | ✔✔ |
| 4 | prop:closure(iii) | R swaps the two null rulings (generic) | YES | `P13_ruling_swaps.py` | ✔✔ |
| 5 | prop:conjugation-parity (spinor) | R acts on a cut spinor as gamma^5 (spinor lift) | YES | storyboard `A3_spinor_lift.py` | ⬚ TO VERIFY |
| 6 | (bead Kretschmann) | Kretschmann on the bead | YES | storyboard `kretschmann_bead.py` | ⬚ TO VERIFY |
| 7 | prop:closure(i) | 3bar=R(3) matter/antimatter | YES | storyboard `closure_i_check.py` | ⬚ TO VERIFY |
| 8 | prop:closure(iv) | R fixes r=0 = the bead's branch point | YES | storyboard `closure_iv_check.py` | ⬚ TO VERIFY |
| 9 | sec:synthesis (QM) | S^4 vs S^5 quantum comparison | YES | storyboard `qm_S4_vs_S5.py` | ⬚ TO VERIFY |

**P13 COMPLETE (r1379-r1383) -- 10 receipts, all ✔✔ cited in place, checker green, compiles 0/0/26pp.**
Coverage: prop:boundary (structural; supported by `cascade_rank`), prop:conjugation-closure (`A3_factorization`),
prop:conjugation-parity (`conjugation_parity` + `A3_spinor_lift`), prop:closure (i)`closure_i_check` (ii)`conjugation_parity`
[mass term -2M/r odd + offset R:r0->-r0 on 2M] (iii)`ruling_swaps` (iv)`closure_iv_check`, sec:sigma (`sigma_lift` --
the boost->rotation clincher, bounded negative), sec:cascade (`cascade_rank`), sec:synthesis (`qm_S4_vs_S5`), bead
Kretschmann (`kretschmann_bead`). DOC FINDING (non-blocking): prop:closure(i) owed one A2-specificity clause -- NOTES_owed_clause.md.
Unused storyboard receipts (A3_attack, spinor_lift_check, foci_ruling_2sqrt3, R_ruling_swap_6D, rulings_between_levels,
closure_levels_check) are adversarial re-checks / exploratory, NOT cited in the paper.
