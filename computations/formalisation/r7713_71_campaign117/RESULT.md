# `r7713+71.2` — RESULT: campaign 117, **maximality (a) BUILT: Kruskal's `{UV < 1}` is `C²`-inextendible across every boundary point of its chart. The frontier is `{UV = 1}`, where the Kretschmann scalar tends to `+∞` from inside, so no function continuous there agrees with it. 6d and 8b are priced: 6d has a small formal core, and 8b has none.** ⌗ `17381` lines in one probe (`99` new, inside the registered band of 80–150). ⌗ p `0.85` came true, with no stop

*Against `PREDICTION.md` (`r7713+71.1`). 71 ran `lake env lean probes/CircleMaximal.lean`. It exits 0 with no errors
and no warnings. All `629` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `625` inherited and
`4` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 116's `CircleBackSeam.lean`.*

## Maximality (a) — BUILT

- **`mx_frontier`:** `closure {UV < 1} = {UV ≤ 1}`, and `frontier {UV < 1} = {UV = 1}` in `ℝ²`.
- **`mx_blowup`:** at every frontier point `p`, the filter of approach from inside the domain is non-trivial, and
  the Kretschmann scalar tends to `+∞` along it. That scalar is the Kruskal chart's `mx_K`, which equals `48M²/rK⁶` by
  `mx_K_eq` from `kr_schwarzschild`. The mechanism: `−UV → −1⁺`, so `rK → 0⁺` (`kr_rinv_to_zero`), and
  `48M²/r⁶ → ∞` (`kr_pow_blowup`).
- **`mx_inextendible`:** no function continuous at a frontier point agrees with `K` on the domain near it. A `C²`
  extension of the metric across `p` would make `K` continuous there. So no `C²` extension exists across any boundary
  point of the chart's domain.

## Sense (b) — not formalised

Maximality as an abstract spacetime, meaning no isometric embedding into a larger Lorentzian manifold, would need
geodesic completeness of the ends `U, V → ±∞` or an inextendibility criterion. The kit has neither, and I found no
cheaper route.

## 6d and 8b, priced (in `PREDICTION.md`)

- **6d has a small formal core.** `r(z) = M(1 + cos z)` and `s(z) = M sin z` satisfy `(r − M)² + s² = M²` for every
  complex `z`.
  - On real `z` that is the circle.
  - On `z = iρ` and `z = π + iρ′` it gives the hyperbolas `(r − M)² − σ² = M²`.
  - Price: 40–80 lines at p `0.95`.
  - The word "maximal" in "maximal analytic completion" is interpretive.
- **8b has no formal core.** It is an ontological reading, and its formal neighbours, 7a and 8a, are built.

## Marks (P2's inventory)

- **BUILT (18 of 22):** every formal row, and now maximality in sense (a).
- **Left:** 6d's small core (priced) and 8b (none). With 6d's core built, P2's formalisation closes.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
