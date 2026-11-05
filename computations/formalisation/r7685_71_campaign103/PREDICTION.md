# `r7685+71.2` — PRE-REGISTRATION: campaign 103, `r7685` ②, **the inventory's cheapest row with content: 2ii (`cor:threefold`'s strict null ordering) on `N`, with 1c (distinct, causally ordered and metrically coincident, in one theorem) on the same witness.** ⌗ `350` new lines (band 200–800), p `0.8`. **Expected stop:** moving `ac_witness` from the model space onto `Pt`

*Registered before any Lean. The inventory is `r7685_71_inventory/INVENTORY.md` (34 rows, 22 / 6 / 6, against 10 /
15 / 9 at r7667); its ranking is the basis here. The new probe is `probes/ThreefoldOrder.lean`, a copy of
`Densities.lean` (which carries `mk_pushup'`, `mk_isOpen_Ifut`, `chr_cau`, `ch_cau_iff` and `ch_chr_iff`) with
`AlongConnection.lean`'s `ac_` section added. Everything new is prefixed `to_`.*

## ① 2ii — the strict null ordering, p `0.85`, `150` lines

- **`to_strict_null_order`, on any `MSpacetime` on `N`:** let `J⁺(p) = {y | Cau p y}`. If `q ∈ frontier J⁺(p)`,
  `Cau p r` and `Cau r q`, then `¬ Chr p r`.
- **Proof:** suppose `Chr p r`. Push-up (`mk_pushup'`) gives `Chr p q`. Then `q` is in the open `I⁺(p) ⊆ J⁺(p)`, so it
  is interior, which a frontier point is not.
- **Weaker hypotheses than P1's:** no geodesic is needed. "Between" covers every causally intermediate event, so in
  particular the points of `γ`.
- **Witness, `to_witness_order`:** on `Pt`, `p = (0, 1)` and `q = (0, e)` on the null generator `U = 0`.
  - `q ∈ frontier J⁺(p)`.
  - The points strictly between them on the generator are causally between, and none is in `I⁺(p)`.

## ② 1c — one pair, three properties, p `0.8`, `200` lines

**`to_cor_1c`:** on the Rindler-horizon pair of `ac_witness`, restated on `Pt`, the same two events are:
- **topologically distinct:** `γ 0 ≠ γ 1`;
- **causally ordered:** `Cau (γ 0) (γ 1)` and `¬ Chr (γ 0) (γ 1)`;
- **metrically coincident:** `Δx = Δτ = 0` for the adapted splitting with vanishing lapse, which is
  `ac_metric_singularity_along`;
- and they satisfy ①'s ordering.

The expected stop is restating `ac_witness` on `Pt`, through `vel` and `extChartAt p₀`.

## For 69: a reading flag on 2i (no Lean)

- **`p ≠ q` does not follow from `cor:threefold`'s hypotheses as written.**
- **The example:** 2D Minkowski modulo the null translation `(t, x) ~ (t + 1, x + 1)`. It is Hausdorff, time-oriented
  and chronological. Its null line through `p` closes into a null geodesic from `p` to `p`, and
  `p ∈ ∂J⁺(p) = J⁺(p) ∖ I⁺(p)`.
- **The fix:** (i) needs `p ≠ q` stated, or a causality condition (no closed causal curves). Both of P1's own settings
  supply one: the globally hyperbolic `D` and the Killing generators.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
