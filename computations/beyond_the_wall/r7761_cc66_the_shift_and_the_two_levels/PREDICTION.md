# `r7761+cc66` — REGISTRATION: DOES RADIATION TOUCH THE **SHIFT**, AND DO THE TWO LEVELS AGREE ON `Ω_m`?

⛭ **Pushed before a line of `shift_and_levels.py` exists.** Order `r7761` items ③ and ④, and the one
quantitative part of item ①. Items ① and ② are readings and carry no registration.

## `R1` — DARYL'S QUESTION: THE SHIFT, OR ONLY THE BEND? (item ③)

The chart is `ds² = −dτ² + (∂_χ r)²dχ² + r²dΩ²` with `τ̃ ≡ τ + χ`. Putting `τ = τ̃ − χ`:

> `g_τ̃τ̃ = −1`, `g_τ̃χ = +1`, `g_χχ = (∂_χ r)² − 1`,

so in ADM form on the **cosmological** (constant-`τ̃`) foliation,

> **`N^χ = 1/((∂_χ r)² − 1)`** and **`N² = (∂_χ r)²/((∂_χ r)² − 1)`**, with `(∂_χ r)² = μ(r)/r + r²/α²`.

⇒ *** Both the lapse and the shift of the cosmological foliation are built from the SAME function
`∂_χ r = dr/dτ̃`. If radiation bends the cut, `μ` gains `K/r` and `(∂_χ r)²` changes — so radiation
would change **both**, and the shift is not an untouched carrier. ***

| row | expectation | licence |
|---|---|---|
| **①** | the ADM reconstruction is right: `−N² + g_χχ(N^χ)² = g_τ̃τ̃` and `g_χχ N^χ = g_τ̃χ` | both to round-off at every node, on the straight cut and the bent one alike |
| **②** | radiation changes `(∂_χ r)²`, and so **both** `N` and `N^χ`, by about **`32` per cent** at `z*` | the three fractional changes reported at `z = 0`, `z = 66.8` and `z*`; `②` fires if the change at `z*` exceeds `10` per cent in `(∂_χ r)²` |
| **③** | and the change is negligible today, of order `Ω_r` | `< 1e-4` at `z = 0` in all three of `(∂_χ r)²`, `N` and `N^χ` |
| **④** | ⛔ **what survives untouched is the chart's FORM, not its functions**: `τ̃ = τ + χ` and `∂_χ r = ∂_τ r` hold on the bent cut as on the straight one, by the radial equation's autonomy | `∂_χ r = ∂_τ r` on the bent cut to `< 1e-9`, as `r7612` measured on the straight one |

## `R1` AMENDED AT `r7761+cc66.1` — ⛔ **ROW `③` MISSED ITS REGISTERED LICENCE, AND THE MISS IS THE FINDING**

⛭ **What was registered and what came back.** Row `③` licenced `< 1e-4` at `z = 0` in all three of
`(∂_χ r)²`, `N` and `N^χ`. Measured: `(∂_χ r)²` changed by `8.819e-05` — which IS `Ω_r` to four figures,
exactly as the row expected — but `N` changed by `−1.311e-04` and `N^χ` by **`−3.504e-04`**. Two of the
three are outside the licence. **I registered the wrong expectation, not a wrong number.**

⛭ **The diagnosis, from the printed numbers alone and before any new computation.** Write
`s ≡ (∂_χ r)²`. The shift is `N^χ = 1/(s−1)` and the lapse is `N = √(s/(s−1))`, so a fractional change
`ε` in `s` propagates as

> `ΔN^χ/N^χ = −ε·s/(s−1)` and `ΔN/N = ½ε(1 − s/(s−1))`.

At `z = 0` the run prints `s = 1.336120`, so the amplifier is `s/(s−1) = 3.9751`, and
`8.819e-05 × 3.9751 = 3.506e-04`, which is the measured shift change; half the difference of the two
terms is `−1.312e-04`, which is the measured lapse change. **The licence was wrong because I took
`N^χ`'s sensitivity to be `1`; it is `s/(s−1)`.**

⛭ **Why it matters for item ③ rather than being bookkeeping.** `g_χχ = (∂_χ r)² − 1` is SMALL today —
`0.336` against `s = 1.336` — so the shift is the most radiation-sensitive of the three quantities now,
by about a factor of four, and the amplifier **diverges** where `(∂_χ r)² = 1`. That sharpens the answer
Daryl asked for: radiation does not merely bend the cut and leave the shift to carry the observation
untouched; the shift is where its effect is largest per unit bend.

| row | expectation | licence |
|---|---|---|
| **③′** | ⛔ **relocated.** `(∂_χ r)²` changes by `Ω_r` at `z = 0` to within a few parts in `10³`; `N` and `N^χ` change by that times the amplifier `s/(s−1)`, which the run must reproduce from the measured `s` | `\|Δs/s − Ω_r\|/Ω_r < 5e-3`; and both `ΔN^χ/N^χ = −(Δs/s)s/(s−1)` and `ΔN/N = ½(Δs/s)(1 − s/(s−1))` to `< 1e-3` RELATIVE, so the row fires if the amplification arithmetic above is not what produced the two numbers |
| **⑨** | ⛔ **NEW, registered here before it is computed.** the amplifier diverges at `(∂_χ r)² = 1`, which on the straight cut with `2M = 2α/(3√3)` is `r = α/√3` exactly — the degenerate (Nariai) radius — so there is a redshift `z_deg = r₀√3/α − 1` at which this chart's shift blows up and the constant-`τ̃` slicing degenerates | `r = α/√3` solves `2M/r + r²/α² = 1` to round-off; `z_deg` printed. **AND the open question, answered either way:** is `r₀√3/α` the same number as `x₀ = (Ω_m⁻¹·2 − 2)^{1/3}`'s root, i.e. does the degeneracy sit AT the acceleration epoch? Printed as a ratio; the row does not presume the answer |

⛭ **What `⑨` does not licence:** no claim that the degeneracy is physical rather than a coordinate
failure of this chart, and no claim about the bent cut's own degenerate radius beyond reporting it.

## `R2` — HOW FAR THE ACTUAL `r(τ̃)` DEPARTS FROM THE PURE `sinh^{2/3}` LAW (item ①'s one number)

The statement under test says the leaves carry radiation's bend **and** that `r ∝ sinh^{2/3}(3τ̃/2α)`.
Those cannot both be exact.

| row | expectation | licence |
|---|---|---|
| **⑤** | the bent `r(τ̃)` departs from the vacuum `sinh^{2/3}` law by of order `Ω_r` today and by **several per cent** near last scattering | the departure in `H` reported at `z = 0`, `z = 66.8` and `z*`; `⑤` fires if it exceeds one per cent anywhere above `z = 67` |

## `R3` — DO THE TWO LEVELS AGREE ON `Ω_m`? (item ④)

`P15` prints `z_acc = x₀ − 1 = 0.6648 ± 0.0467` and the identity `Ω_m = 2/(x₀³+2)`. The leaf-rate refit
returns `Ω_m = 0.2945` (70's, quoted in the order).

| row | expectation | licence |
|---|---|---|
| **⑥** | propagating `z_acc`'s error through the identity gives `Ω_m = 0.3024 ± 0.0178` from the **geometry alone** | the central value and `σ` computed from `dΩ_m/dx₀ = −6x₀²/(x₀³+2)²`, printed |
| **⑦** | ⇒ the refit's `0.2945` lies **well inside** that, under half a standard deviation | the discrepancy in units of `σ` printed; `⑦` fires if it exceeds `1σ` |
| **⑧** | and against the background's own `x₀³ = 4.72721157` (`Ω_m = 0.29730`) the refit sits closer still | the discrepancy in `σ` printed |

⛭ **Why `R3` is a real test and not bookkeeping:** `Ω_m` from `z_acc` is read off the **geometry**, with
no distance ladder, no microwave background and no density; the refit's `Ω_m` is read off the **content's
own spectrum** on the leaf rate. **The two levels agreeing on it is a prediction of the two-level
statement, and their disagreeing would be evidence against it.**

⛔ **70's refit uncertainty is theirs to supply and is NOT assumed here.** `z_acc`'s `±0.0467` dominates
by roughly four to one against a typical spectrum-fit `σ(Ω_m) ~ 0.004`, so the comparison is reported on
`z_acc`'s error alone and the conclusion is stated as conditional on 70's being subdominant.

## WHAT THIS REGISTRATION DOES NOT LICENCE

* **No verdict on the two-level statement.** `R1`–`R3` are measurements the reading in `FOR_66.md` then
  uses; item ①'s answer is a reading of `P7` and is not decided by any number here.
* **No new background, no fit.** Everything is read by path from 60's `r7580/lightpath.py`, with `z_acc`
  and its error read from `P15` `eq:zacc` as printed.
* **No paper edits.** The order says no drafts this round.
