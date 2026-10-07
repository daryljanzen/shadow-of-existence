# F5 — every ABSENT number at `HEAD`, read by hand against the receipt's captured stdout

There are 17 ABSENT on v1 and 16 on v2.  That is fewer than the 20 pre-registered, so all of them were read.

- **DRIFT**: the INDEX value disagrees with the value the receipt prints for that quantity.
- **PRECISION**: the INDEX carries more digits than the receipt prints, and the two are consistent at the printed
  digits.
- **NOT-PRINTED**: the figure is never printed, so it can be neither confirmed nor refuted.
- **NOT-A-FIGURE**: for example, a runtime.
- **FORM**: the same number in another notation, which is the instrument's miss.

| # | receipt | INDEX | receipt prints | verdict |
|---|---|---|---|---|
| 1 | `P10_the_scale_factor_factors_out_of_the_free_tower` | `9.74998` | `hard cutoff, no zeta function: 3.74999 against 15/4 = 3.75` | **DRIFT** |
| 2 | `P03_the_third_regime_is_the_boundary_of_admissible_data…` | `4.07×10^60` | `4.07e+60` | FORM: v1 refused `e+`.  v2 MATCH |
| 3 | `P10_the_degeneracy_needs_r_constant_not_the_cosh…` | `35.5 decades` | `34.7` | **DRIFT**: a hand-derived count of decades |
| 4-5 | `P15_a_source_with_no_physics_reproduces_the_contrast…` | `eta = 281.7`, `486.0` | (not printed) | NOT-PRINTED |
| 6-7 | `P10_the_commutator_bound_survives_the_cubic…` | `-1.01`, `-1.02` | `-1.00`, `-1.04` | **DRIFT** x2 |
| 8 | `P10_the_second_logarithm_holes_the_mechanism…` | `11.2 decades` | `10.3` | **DRIFT**: decades by hand |
| 9 | `P10_the_second_logarithm_line_closes…` | `11.2 decades` | `10.3` | **DRIFT**: the same figure, carried into a second row |
| 10 | `P15_the_held_period_estimator_reaches_below_the_floor…` | `1.4911` | `1.4910` | **DRIFT**: last digit |
| 11 | `P15_horn_ones_carrier_is_already_the_papers_own…` | `15.4 s` | (a runtime) | NOT-A-FIGURE |
| 12 | `P15_no_paper_fixes_the_primordial_normalisation…` | `2.7618293` | `2.7618` | PRECISION |
| 13-16 | `P15_the_1p57_has_no_parameter_address…` | `0.021966`, `0.954248`, `0.021524`, `0.997952` | `0.02197`, `0.9542`, `0.02152`, `0.9980` | PRECISION x4 |
| 17 | `P15_the_two_exact_twos_are_the_same_pair_of_stretches…` | `4.6083` | (not printed, not in source) | NOT-PRINTED: probably derived by hand |

**Totals: 7 DRIFT** (#1, #3, #6, #7, #8, #9, #10), **5 PRECISION**, **3 NOT-PRINTED**, **1 NOT-A-FIGURE**, **1 FORM.**

⇒ *Three of the seven are `cc66`'s shape exactly: a quantity derived by hand ("decades above the floor") that
disagrees with the receipt's own line.  #8 and #9 are one hand-derived figure copied into two rows.*
