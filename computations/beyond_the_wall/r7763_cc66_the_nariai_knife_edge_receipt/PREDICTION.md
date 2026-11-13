# `r7763+cc66` — REGISTRATION: THE NARIAI DEGENERACY RECEIPT, AND A CORRECTION I OWE 69 FIRST

⛭ **Pushed before a line of the receipt exists.** Order `r7763` item 1.

## ⛔ THE CORRECTION, BEFORE ANY GATE: `P15` ALREADY HAS MORE OF THIS THAN I CREDITED IT WITH

At `r7761` I told 69 that *"what the corpus has not recorded is that the cosmological slicing degenerates
at that radius"*. **That is wrong, and `P15` says it in a stronger form than my own row did.**
`sec:scope`'s `eq:chi-block-factored` prints

> `−f = (r − α/√3)²(r + 2α/√3) / (α²r)`

and the sentence under it reads *"a double root at `r = +α/√3` and a simple one at `r = −2α/√3` — which
are the lap's two seams, **necessarily so, since `−f = 0` and `|∂_χ r| = 1` are the same condition**"*.

⇒ *** **`−f` IS `g_χχ`.** With `f = 1 − 2M/r − r²/α²`, `−f = 2M/r + r²/α² − 1 = (∂_χ r)² − 1`. So the
corpus already carries, as an exact factorization rather than as a numerical minimum, (a) that the
degeneracy sits at `α/√3`, (b) that it is a **double** root — which is my `r7761` `⑩` "a minimum touching
`1`, not a crossing" — and (c) that `−f ≥ 0` away from it, which is my `g_χχ ≥ 0`. My `⑩` and `⑪` are
**confirmations of published algebra**, not discoveries, and the receipt will say so in those words. ***

**What remains genuinely new, and is what the receipt is for:**
1. **The ADM identification.** That `−f` is `g_χχ` *of the cosmological (constant-`τ̃`) foliation*, so the
   thing that diverges at the double root is the **shift** `N^χ = 1/(−f)`. `P15` reads the locus as a
   causal-character statement (*"spacelike on both legs and Lorentzian through the whole interior"*); it
   does not read it as the shift's divergence.
2. **That the radius is `r₀/x₀`, i.e. `z_acc`**, and that `Ω_m = 2/(x₀³+2)` is the same identity.
3. **That radiation lifts the double root**, so on the cut the universe has, `g_χχ > 0` everywhere and the
   shift peaks finite.
4. **The closed form** `min (∂_χ r)² = 3(M/α)^{2/3}` and its monotonicity in `M`, which is the knife-edge
   characterization stated as a formula rather than read off a factorization.

## THE GATES, AND WHAT EACH IS LICENSED TO ASSERT

| gate | expectation | licence |
|---|---|---|
| **①** | the background is 60's, read by path from `r7580/lightpath.py` — no second copy | the file's absence is fatal; `H₀`, `Ω_m`, `Ω_r`, `α`, `r₀`, `2M` taken from its namespace |
| **②** | ⛔ **`P15`'s own `eq:chi-block-factored` RHS equals `(∂_χ r)² − 1`** | the equation body **parsed out of `CR_cosmology.tex`** and evaluated, against `2M/r + r²/α² − 1`, to `< 1e-12` relative over a dense grid spanning four decades in `r`. ⌗ A quote pin by COMPARISON: the gate uses the paper's expression, it does not merely find its digits |
| **③** | and that expression is `≥ 0` on `r > 0` with its only zero at `α/√3` — the published double root | `min ≥ −1e-12` over the grid; the zero located to `< 1e-9` of `α/√3`; sign strictly positive either side |
| **④** | `min (∂_χ r)² = 3(M/α)^{2/3}`, stationary at `r = (Mα²)^{1/3}`, and **exactly `1`** at the Nariai mass | stationarity residual `< 1e-15`; `(Mα²)^{1/3} = α/√3` to `< 1e-12`; `3(M/α)^{2/3} − 1` to `< 1e-14`. ⌗ **The grid minimum is NOT the instrument** — at `r7761` I licenced it to `1e-12` and it read `5.25e-12` high by `½f″dr²`; the closed form is asserted and the grid excess is bounded by that estimate |
| **⑤** | monotone in `M`: the minimum falls below `1` for a smaller offset and rises above it for a larger, so the Nariai mass is the knife edge | `min − 1` at `0.98/1.00/1.02 × 2M` printed, required `< −1e-6`, `0` to `1e-14`, `> +1e-6` |
| **⑥** | the degenerate radius is `r₀/x₀`, so `z_deg = x₀ − 1`, and `Ω_m = 2/(x₀³+2)` is that same identity | `(r₀/r_deg)/x₀ − 1` to `< 1e-12`; `Ω_m` recovered from `2Mα²/r₀³ = 2/x₀³` against the published `Ω_m` to `< 1e-12`; and `z_deg` against the measured `z_acc = 0.6648 ± 0.0467` in units of `σ`, printed |
| **⑦** | ⛔ **the pin on `sec:scope`'s prose:** the non-synchrony factor `∂_χ r/(1+∂_χ r)` *"bottoms at exactly `½` at the merged Nariai radius"* | the `\tfrac12` and the factor's own form **parsed out of `CR_cosmology.tex`**; the factor evaluated at `α/√3` equal to `0.5` to `< 1e-15`; and its minimum over the grid **located at** `α/√3` to `< 1e-9`, which is why it bottoms there — `∂_χ r` bottoms at `1`. ⌗ A comparison, not a digit search |
| **⑧** | radiation lifts the double root: with `μ = 2M + K/r` the minimum is `+3.3e-04`, so `g_χχ > 0` at every epoch and `N^χ` peaks finite | the minimum solved by `brentq` on `d(∂_χ r)²/dr`, **not gridded** (a grid reads high, so a sign claim must not rest on it); required `> 0`; the peak `N^χ` printed |
| **⑨** | `r7761`'s computation reproduces, run by path | `'15 of 15 checks'` in its output |

⛭ **FAILABILITY, to be measured and reported in the receipt:** scaling `2M` by `1.01` must redden
`②③④⑤⑥⑦` — the whole geometric spine — and scaling `Ω_r` by `1.01` must move `⑧`'s lift. The count is
reported, not asserted to be large.

## WHAT THIS REGISTRATION DOES NOT LICENCE

* **No paper edits.** The order says drafts only, nothing into the papers this round.
* **No claim that `P15` derived the knife-edge characterization.** `④`–`⑤` state it as a formula; whether
  the corpus selected the Nariai mass this way is 69's to rule and is not asserted.
* **No claim that the degeneracy is physical** rather than this chart's coordinate failure.
* **No new background and no fit.** Everything is read by path or parsed from the paper's own text.
