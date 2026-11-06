# `r7687+71.3` — RESULT: campaign 104, **2i BUILT under P1's "no closed causal curves": the endpoints of a causal curve are distinct and separated by disjoint open sets; and the hypothesis follows from any temporal function, so it holds on `D` and on Minkowski.** ⌗ `7402` lines in one probe (`166` new, band 120–600). ⌗ p `0.85` came true. The expected stop (strict increase along causal steps) was not hit

*Against `PREDICTION.md` (`r7687+71.1`). 71 re-ran `lake env lean probes/ThreefoldDistinct.lean`. It exits 0 with no
errors and no warnings. All `121` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `108`
inherited and `13` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 103's `ThreefoldOrder.lean`.*

## The definition

**`NoClosedCausal S := ∀ p, ¬ TransGen S.CStep p p`.**
- The kit's `CStep` is a `C¹` curve in `M` with future-causal velocity, and `Cau = ReflTransGen CStep`.
- So a closed causal curve is a non-empty chain of steps from a point back to itself.

## ① 2i — BUILT

- **`td_cor_threefold_i [T2Space N]`:** under `NoClosedCausal`, `TransGen CStep p q` gives `p ≠ q`, together with
  disjoint open `U ∋ p` and `W ∋ q`.
- **`td_transGen_of_cau_ne`:** `Cau p q` with `p ≠ q` is a non-empty chain. So any causal curve from `p` to `q`,
  P1's `γ` included, is one.
- **As registered,** (i) is immediate on this definition. Its content is ②.

## ② The hypothesis holds in P1's settings — BUILT

- **`td_temporal_curve_lt`:** a temporal `τ` strictly increases along every `C¹` future-causal curve in an open `U`.
  The kit had only the timelike case. The proof uses only `FutCausal`, so it is re-proved for causal curves.
- **`td_noClosed_of_temporal`:** `IsTemporalOn M τ` gives `NoClosedCausal`.
- **`td_noClosed_of_temporalOn`:** the same holds on any open `U ⊆ M`.
- **`td_noClosed_D`:** a Cauchy temporal function on `D` gives `NoClosedCausal` for `D` as a spacetime (`DspN`). That is
  P1's globally hyperbolic exterior. It covers chains whose steps stay inside `D`.
- **`td_minkN_noClosed`:** Minkowski on `Pt` has no closed causal curves.
  - `U + V` rises strictly along every step (`td_minkN_cstep_lt`), proved through the vector-space model.
  - `U + V` is used only as a function that increases strictly along steps. It is not proved temporal in the kit's
    sense.
- **`td_cor_1c_hyp`:** `to_cor_1c`'s Rindler pair satisfies (i)'s hypothesis and conclusion.

## Marks

- **2i → BUILT, on P1's ruled reading.**
- The inventory is now **25 / 5 / 4**.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
