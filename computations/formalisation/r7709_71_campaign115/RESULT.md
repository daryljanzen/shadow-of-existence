# `r7709+71.2` — RESULT: campaign 115, **6b BUILT. The four `r ≥ 0` patches, together with the horizons `UV = 0` at which they meet, are exactly Kruskal's `{UV < 1}`, pairwise disjoint. All four patches pull back to P2's metrics on Kruskal's own manifold `sk_S`. 5b is priced in the registration.** ⌗ `16941` lines in one probe (`269` new, inside the registered band of 250–450). ⌗ p `0.7` came true. The expected stop at 6b-i did not occur

*Against `PREDICTION.md` (`r7709+71.1`). 71 ran `lake env lean probes/CirclePatches.lean`. It exits 0 with no errors
and no warnings. All `600` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `586` inherited and
`14` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 114's `CircleExterior.lean`.*

## Where it is stated (69's question)

**On the full domain `{UV < 1}`, carried by Kruskal's own manifold `sk_S` on `Pt`.**
- **The chart:** `sk_S`'s global null chart `p₀` gives `hRep = F·gM` on all of `{UV < 1}` (`sk_hRep`).
- **The reflected patches:** they lie outside `W`. Their metrics are therefore read on `sk_S`, not on `se_S`.
- **On `W`:** the two manifolds agree (`cp_sk_se`), so campaigns 113's and 114's pullbacks carry over.

## 6b-i, onto — BUILT

- **`cp_onto_BH`:** every `(U, V)` with `U, V > 0` and `UV < 1` is `Φ(η, t)`, with `η = arccos(rK/M − 1)` and
  `t = 2M log(V/U)`. The match is made by squares (`s² = UV`, `e^{t/2M} = V/U`), with no square root.
- **`cp_onto_RE`:** every `(U, V)` with `U < 0 < V` is `Ψ(ρ, t)`, with `ρ = arcosh(rK/M − 1)` and
  `t = 2M log(V/(−U))`.
- **`cp_rK_lt` and `cp_rK_gt`:** `rK < 2M` where `UV > 0`, and `rK > 2M` where `UV < 0`.

## 6b-ii, the identity — BUILT

**`cp_kruskal`:** `BH ∪ WH ∪ RE ∪ LE ∪ Hor = {UV < 1}`, and all ten pairs of these five sets are disjoint.
- `BH = Φ((0, π) × ℝ)` and `WH = −Φ(…)`.
- `RE = Ψ((0, ∞) × ℝ)` and `LE = −Ψ(…)`.
- `Hor = {UV = 0}`: all four horizon halves and the bifurcation point, where `r = 2M`.

Each patch lies in its own open quadrant (`cp_BH_quad`, `cp_WH_quad`, `cp_RE_quad`, `cp_LE_quad`).

## 6b-iii, the metrics on `sk_S` — BUILT

**`cp_metrics`:**
- `BH` and `WH` pull back to `−4M²cos⁴(η/2) dη² + tan²(η/2) dt²`.
- `RE` and `LE` pull back to `4M²cosh⁴(ρ/2) dρ² − tanh²(ρ/2) dt²`.
- The reflected patches are handled through `cp_sk_reflect`: `(U, V) ↦ (−U, −V)`, with the derivatives negated.

## What this lifts in P2

The sentence P2 now states in five places, that the four `r ≥ 0` patches "together with the horizons at which they
meet, are the maximal Kruskal–Szekeres extension", is machine-checked:
- on Kruskal's domain `{UV < 1}`, as a disjoint union (`cp_kruskal`);
- with each patch's metric read on Kruskal's manifold `sk_S` (`cp_metrics`).

## Limits

- **The radial plane only.** `sk_S` is the radial plane, as throughout the kit.
- **"Maximal" is not formalised.** Read as the domain `{UV < 1}`, the cover is exactly `{UV < 1}`. That no
  analytic Lorentzian extension of it exists is not stated.
- **The white-hole interior's chart.** It is `−Φ` with `η ∈ (0, π)`. P2's `z = η ∈ (−π, 0)` is the same set,
  since `r` is even (`cy_patches`).

## 5b, priced (in `PREDICTION.md`)

- **5b-i, the coefficients** (horizonless, and asymptotically flat in its coefficients): 40–80 lines at p `0.95`.
- **5b-ii, the geometry and `K = 48M²/r⁶ → 0`**, through a tortoise null chart and `kr_warped`: 300–500 lines at
  p `0.55`.
- **Expected stop:** the tortoise inverse for `r < 0`.

## Marks (P2's inventory)

- **BUILT (17):** 1a, 1b, 2a, 2b, 3, 4a, 4b, 5a, 6a, 6b, 6c, 7a–7e and 8a.
- **Not built (1 formal):** 5b (priced).
- **Interpretive:** 6d and 8b.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
