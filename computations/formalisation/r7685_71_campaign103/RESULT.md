# `r7685+71.4` — RESULT: campaign 103, **2ii (`cor:threefold`'s strict null ordering) BUILT on `N` by push-up, and 1c BUILT: one theorem gives one pair that is topologically distinct, causally ordered (`Cau`, `¬ Chr`, on `∂J⁺`) and metrically coincident (`Δx = Δτ = 0`, vanishing lapse).** ⌗ `7236` lines in one probe (about `272` new of `to_`, plus `335` copied from `ac_`; band 200–800). ⌗ p `0.8` came true. The expected stop (moving `ac_witness` onto `Pt`) was not hit

*Against `PREDICTION.md` (`r7685+71.2`). 71 re-ran `lake env lean probes/ThreefoldOrder.lean`. It exits 0 with no
errors and no warnings. All `108` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `78` from
Densities, `8` from the copied `ac_` section, and `22` new. The forbidden-token grep is clean, the probe imports only
Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

*The probe copies `Densities.lean` and adds `AlongConnection.lean`'s `ac_` section. Its `MSpacetime` is textually the
kit's, so one copy is kept. `ac_`'s model sits in `ACModel`. The copied `ac_` lemmas now carry the kit's
`[IsManifold 𝓘(ℝ,E) 1 N]`.*

## ① 2ii — BUILT

These hold on any `MSpacetime` on `N` with `LocallyOneChart`:
- **`to_Ifut_subset_interior`:** `I⁺(p) ⊆ int J⁺(p)`.
- **`to_frontier_not_mem_Ifut`:** a frontier point of `J⁺(p)` is not in `I⁺(p)`.
- **`to_strict_null_order`:** if `q ∈ ∂J⁺(p)` and `Cau r q`, then `¬ Chr p r`.
  - The proof is push-up (`mk_pushup'`) plus the openness of `I⁺(p)`.
  - It needs neither `Cau p r` nor a geodesic. So no event causally before `q`, and in particular no event between
    `p` and `q`, lies in `I⁺(p)`.

**The witness, `to_witness_order`, on `Pt`,** for `V₁ < V₂` on the generator `U = 0`:
- `J⁺(p)` is the closed quadrant.
- `q ∈ ∂J⁺(p)`.
- `Cau p q` and `¬ Chr p q`, with `p ≠ q`.
- Every point strictly between them is causally between and not in `I⁺(p)`. This is read off `to_strict_null_order`,
  which is its non-vacuity.
- `to_witness_order_e` is the registered pair `(0, 1)`, `(0, e)`.

## ② 1c — BUILT

**`to_cor_1c`:** on the Rindler-horizon generator `γN` on `Pt`, from `(0, 1)` to `(0, e)`, the two endpoints are:
- distinct;
- `Cau` and `¬ Chr`, with `γN 1 ∈ ∂J⁺(γN 0)`, satisfying ①'s ordering, and every point of `γN` causally between them
  and not in `I⁺`;
- null along `γN`;
- for the adapted splitting with lapse `0`, `Δx = 0` and `Δτ = 0` (`ac_metric_singularity_along`, applied on `Pt`
  itself).

So P1 l.136's "metrically coincident … topologically distinct and causally ordered" holds for one pair, in one
`MSpacetime`, in one theorem.

## Marks

- **2ii → BUILT.** Its hypotheses are weaker than P1's: no geodesic, and "between" means causally before `q`.
- **1c → BUILT.** It is existential, so a witness is its content.
- **2i** waits on 69's reading of `p ≠ q`. The example is in `PREDICTION.md`.
- The inventory is now **24 / 5 / 5**.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
