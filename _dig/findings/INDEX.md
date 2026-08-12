# _dig/findings — the drafts table

*Working area for the long dig. Nothing here is a closure. Bounded negatives are the node's;
closures on registered items are Daryl's (`PROTECTED_OPEN.md`). Every item states what it does
NOT claim, and every recommendation is stated for reversal.*

| # | one line | kind | artefact | verified at source? |
|---|---|---|---|---|
| **F01** | the reproducibility layer's front door is a frozen r2376 snapshot (deps under-declared, `pynucastro` missing, `run_all.py` absent, the ORIGIN debt it books as open is closed), and one registered receipt cannot run where it is registered | bounded negative | `F01_receipts_front_door.md` | yes — full 249-receipt run |
| **F02** | the causal trichotomy at two independent radii, in closed form; `P03_the_sixth_equivalence`'s 51 enumerated pairs are its evaluation table; the null condition is chord-tangency at any two radii | offered (a compression) | `F02_the_two_radius_causal_law.md` + `DRAFT_P03_the_two_radius_causal_law.py` (rc=0) | yes — symbolic + 2×10⁵ random controls |
| **F03** | `check_currency` reads its clock from `FORK_c54.md`, which it does not watch, so it cannot fail; five registers 43–76 revisions stale are reported current, and it prints negative lags | bounded negative | `F03_the_currency_gate_cannot_fail.md` + `DRAFT_check_currency_patched.py` (rc=1 on the live tree) | yes |
| **F04** | P9 `cor:radiation` cites itself; the L-137 landing paragraph came to rest inside the environment instead of after it, against the register's own note | bounded negative | `F04_a_corollary_cites_itself.md` + `DRAFT_check_compile_selfref.py` (rc=1, 1 hit in 35 files) | yes |
| **F05** | three of the nine Bianchi symmetry algebras (II, IV, VI_h) are not subalgebras of so(4,1) at all, so they cannot be the sweep — and a sharp question about whether those geometries are cuts of a G₂ class instead | offered (one fact, one question) | `F05_which_bianchi_types_can_sweep.md` + `DRAFT_P09_which_homogeneous_cosmologies_are_cuts.py` (rc=0) | yes — explicit so(4,1), 4000+20000+20000 controls |
| **F06** | P16's displayed abundance equation cites `P16_validate_bbn`, which returns different D/H and ⁷Li; the numbers are produced exactly by the sibling receipt at StarLib. And the library spread is 2.5× (D/H) and 2.0× (⁷Li) the theory-error budget it is filed inside | bounded negative | `F06_the_bbn_equation_cites_the_wrong_receipt.md` + `DRAFT_check_numbers_at_citations.py` + `capture_receipt_output.py` | yes — all 249 receipts run, output cached and compared |
| **F07** | 191 of 249 receipts contain no `assert`, so their exit code is 0 whatever they compute — including 76 of the 100 rows marked ✔✔. Corrects F01's own headline. Closed by a printed-number fingerprint baseline | bounded negative (structural) | `F07_three_quarters_of_the_receipts_cannot_fail.md` + `DRAFT_receipt_fingerprints.py` + blessed `receipt_fingerprints.json` | yes — measured; gate blessed, passes, and bites on a one-digit perturbation; determinism checked on a live 40-receipt resample |
| **F08** | the lift's Euclidean gravitational action is **S_E = −Mα/4G** exactly — linear in the progenitor mass; the quoted −0.0481 α²/G is −α²/(12√3 G) at the forced member; the integrand is −2M cos²(3s/2α) so the cutoff ladder truncates a regular integral rather than regularising a singular one | offered (closed form) + one labelling slip | `F08_the_lift_action_is_minus_M_alpha_over_four.md` + `DRAFT_P10_the_lift_action_in_closed_form.py` (rc=0) | yes — symbolic; truncation error predicted exactly at every cutoff |
| **F09** | the lift's factor **2.32 = Γ(1/6)/(√π Γ(2/3)) = 3Γ(1/3)³/2^{4/3}π²**, mass- and α-independent; the exponent goes as **M^{−1/3}**; and **C is not bounded by 1.72** — it diverges at the branch point and vanishes at the turnaround, 1.72 and 0.16 being the receipt's first and last samples. Conclusion survives via the exact window law s*/s_max = (2/π)(2M/α)/μ_n³ | offered (closed forms) + bounded negative (a false bound) | `F09_the_adiabatic_constants.md` + `DRAFT_P10_the_adiabatic_constants_in_closed_form.py` (rc=0) | yes — closed forms match quadrature to 9 figures across a 10× mass range |
| **F10** | one closed form **r'' = ε(3r²−cα²)/(2rα²)** gives the acceleration at all four marked loci of the lap (front seam **0** exactly, back seam **−3√3/4α**, turnaround, Euclidean null) — and the paper's *order of contact* distinction between the two seams is the **multiplicity of the root**, the same doubling that makes the member Nariai | offered (consequence of the caption's own cubic) | `F10_one_formula_for_the_triptych.md` + `DRAFT_P07_one_formula_for_the_triptych.py` (rc=0) | yes — symbolic, plus an independent finite-difference control |
| **F11** | P15 quotes ρ_r/ρ_m at the angle-fixed onset as both **1.71** and **1.69** ~40 lines apart; both are correctly receipted and the two receipts run CR's *own* rate at Ω_m = 0.3066 vs 0.3150 (z_onset 6747 vs 6797). The argument's pivot — "exact at h ≃ 0.68" — moves from 67.4 to 68.3 with it | bounded negative | `F11_two_omega_m_two_answers.md` + `DRAFT_P15_one_path_two_omega_m.py` (rc=0) | yes — one code path reproduces both quoted values |

## The gate patches, together

F01·C, F03 and F04 each end in the same place, and the corpus's own rule is the one that put
them there — `check_currency.py`'s docstring: **"A recurring defect wants a gate."** All three
are drop-in, in the house style, and each was run against the live tree before being written up:

| patch | closes | current result |
|---|---|---|
| `DRAFT_check_currency_patched.py` | a gate anchored to an unwatched document | rc=1, 5 stale registers |
| `DRAFT_check_compile_selfref.py` | a `\ref` resolving to its own environment | rc=1, 1 hit |
| `DRAFT_check_numbers_at_citations.py` | a `\rcpt` whose receipt does not compute the number beside it | 15 flags / ~250 citations, 1 real — ships as a **report**, not a gate |
| `DRAFT_receipt_fingerprints.py` | a print-only receipt whose numbers silently move after a reader blessed it | baseline blessed: 249 receipts, 23 390 numbers, clean; bites on one perturbed digit |
| *(sketched, F01·C)* import-resolution check in `check_receipts.py` | a receipt whose dependency did not travel with it | would catch `ROBUST_p1p2_scan.py` |

The five share a shape worth naming: **each gate models a document as its text, and each defect
lives in something the document depends on that the model does not carry** — the clock a gate
compares against, the environment a reference sits in, the directory a receipt imports from, the
computation a citation stands next to. The ORIGIN drift guard was the first of this family (a
receipt's identity is wider than its docstring); these are the next four; F07's fingerprint baseline is the fifth and closes the channel the other four leave open — a document that stops matching itself.

## Standing discipline for this dig

- Mirror-check pair most at risk: **invent-a-flaw ↔ invent-a-reassurance.** A standing brief to
  find things to update manufactures findings. Every item above was verified at source, and
  "nothing here" stays a legitimate result.
- README guards held: **α is never sent to a limit** · the throat is **X = α**, never `r = α` ·
  the Hubble/acoustic matter is **RESOLVED and banked**, not reopened · "manufactured / shadow /
  projection" mean **built-by-construction AND REAL**.
- **The pattern across eleven findings, stated because it is the useful summary:** the corpus's
  *computations* keep coming out right when checked at source. What drifts is the connective
  tissue — the pointer (F06), the clock (F03), the placement (F04), the endpoint label (F08), the
  gloss quoted one notch tighter than the calculation supports (F09, F06·C). Two findings are
  additions rather than defects (F02, F05), and three are closed forms the corpus evaluates
  numerically (F08, F09, F10) — all three found by the same move: take a quoted decimal that
  sits beside a stated structure and ask the structure for it.
- *"Your failure to find something in this corpus is evidence about you."* F02 was searched
  against the corpus before it was written, and most of what looked new was already there —
  `P03_hexagon_null_triple` at 2α, L-53 at general D,
  `THE_GEOMETRY_AND_THE_PHYSICS` §II for the one-point theorem. What survived that search is
  stated at the weight it survived at, and no more.
