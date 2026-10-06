# D3 — a seeded sample of 20 MULTI-SITE receipt pins (`random.seed(7183)`, `sample20.tsv`), read against every occurrence

The two verdicts are as follows.
- **AMBIGUOUS:** the occurrences make different claims, so removing the intended one leaves the pin green.
- **RESTATEMENT:** every occurrence states one claim, in the abstract and the body or twice in one section.

| # | receipt:line | literal | x | verdict |
|---|---|---|---|---|
| 1 | `S8_the_floor_follows:97` | `at the origin` | 9 | AMBIGUOUS: a generic phrase across nine claims |
| 2 | `P15_the_construction_fixes_no_closed…:197` | `r_0\approx5051` | 2 | RESTATEMENT |
| 3 | `Z1_the_phase_is_the_antilinear_face…:110` | `reality involution` | 3 | AMBIGUOUS: a term used in three claims |
| 4 | `B16_the_coupling_cannot_come_from_this_bundle:87` | `has a holonomy about the Nariai points` | 2 | RESTATEMENT (abstract and body) |
| 5 | `B34_the_join_crosses_the_inner_horizon:115` | `JanzenBoundary` | 26 | AMBIGUOUS: a citation key |
| 6 | `S1_the_quartic_is_a_constant_vacuum_energy…:125` | `gauge-combination` | 3 | RESTATEMENT |
| 7 | `S1_every_mode_of_interest_freezes…:169` | `before the crossing` | 3 | RESTATEMENT |
| 8 | `P15_the_harmonic_expansion…:208` | `D_C/r_0\approx2.774` | 2 | RESTATEMENT (one section) |
| 9 | `G3_the_axis_names_two_orderings:128` | `plane wave` | 5 | AMBIGUOUS |
| 10 | `D1_the_boundary_is_per_fibre…:156` | `ultraviolet definition of the tower sums` | 2 | RESTATEMENT (one section) |
| 11 | `B15_po3_both_clauses_answered:142` | `odd in the signed offset` | 2 | RESTATEMENT |
| 12 | `C18_bespoke_means_two_legs:149` | `The full flat-projection transfer` | 2 | AMBIGUOUS: "turns this into a deficit" against "confirms the estimate and sharpens it", in one section |
| 13 | `P15_the_harmonic_expansion…:204` | `D_C\approx1.4011\times10^{4}` | 2 | RESTATEMENT (one section) |
| 14 | `P15_the_floors_understatement…:254` | `\S\ref{sec:largescale}` | 11 | AMBIGUOUS: a cross-reference |
| 15 | `F2_the_flatness_is_what_a_branching_IS:89` | `returns the \emph{same} $2M=r_0-r_0^3$` | 2 | RESTATEMENT |
| 16 | `C40_the_pair_was_quoted_against_a_rounding:90` | `against the measured` | 8 | AMBIGUOUS |
| 17 | `P15_the_locus_is_wrong_in_six_places…:411` | `\label{prop:` | 7 | AMBIGUOUS: a structural prefix, not a claim at all |
| 18 | `B5_the_mod_two_index_is_one…:101` | `\dim\ker_+=3` | 3 | RESTATEMENT |
| 19 | `B14_identical_in_content_is_po2s_reason:122` | `identical in content` | 2 | RESTATEMENT |
| 20 | `P15_the_projection_joins…:146` | `D_C\approx1.4011\times10^{4}` | 2 | RESTATEMENT (one section) |

**Totals: 8 AMBIGUOUS, 12 RESTATEMENT.**
- **7 of the 8 AMBIGUOUS are short or generic strings:** a phrase of two or three words, a citation key, a
  cross-reference, a LaTeX prefix.  Only #12 is a long, specific phrase reused for two different claims.  It is the
  same shape as the explainer's `by three independent routes`, and it is the dangerous kind, because nothing about
  the string warns that it is shared.
- **The 12 RESTATEMENTS are harmless only while every copy moves together.**  When one copy is repaired and the other
  is not, the pin cannot tell which copy it is reading.
