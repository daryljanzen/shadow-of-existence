# `r7443+71.42` — RESULT: campaign 46, `11` of `12` LIMIT rows `DONE`. Row 101 is BUILT IN PART: one check is open, a Beta-type ratio. ⌗ `2366` lines in two probes (band 700–2400, IN BAND). ⌗ The all-twelve p of `0.30` did not come true; the median prediction of `9` was beaten by `2`

*Scored against `PREDICTION.md` (pushed at `r7443+71.37` before any Lean), not revised. Both probes build with no
error and only linter warnings, and both were re-run by 71:*
- *`probes/LimitQuadricFlow.lean`: 11 theorems, `255 s`.*
- *`probes/LimitNariai.lean`: 17 theorems, `205 s`.*

*Every theorem is on `[propext, Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`). No `native_decide`.*

| row | result |
|---|---|
| 9, 10 | `DONE`. The splits hold for every `D`; the receipt's dimensions are instances |
| 106 | `DONE`. The Wick map over ℂ; the invariants are also re-derived from the constant-curvature tensor |
| 91 | `DONE` |
| 26 | `DONE`. The completion table is stated as the receipt's definition |
| 40 | `DONE`. The first integral holds for every `D ≥ 3`, and so does the deck shift. The deck group itself is not claimed |
| 97 | `DONE`. §C is computed in SdS's static chart at `r = r(τ)`; that this matches the receipt's reassigned chart is not built |
| 105, 12, 21 | `DONE`. `f ≤ 0` on all `r > 0` comes from the factorisation; the blueshift limits are `Tendsto` statements |
| 100 | `DONE`. ***The log divergence is proved analytically*** (not interval-integrable across `r_N`, plus a `log(1/ε)` lower bound). The receipt's floats are rational brackets |
| 101 | ***BUILT IN PART.*** Every check but one. ***Open:*** the `23.254 %` ratio `∫_{π/4}^{π/2} sin^{−2/3} / ∫_0^{π/2} sin^{−2/3}`, an incomplete Beta function with no closed form. The receipt's tolerance needs about `4·10⁻⁵` relative accuracy, beyond the rational brackets built so far |

***Routed to the owner of row 101's receipt:*** its check Ⓒ① evaluates the collapse leg at `s = +acosh(2)/k`. That
leg is `s ≤ 0`, where `dr/ds > 0` by its own Ⓔ①, so the speed at the actual back seam is ***`+1`***, not `−1`. Lean
builds both values.

***Rename:*** the probe's copies of `section_quadric` and `sds_kretschmann` are renamed `*_copy`, so that rows 45 and
108 keep a single declaration each in the join.
