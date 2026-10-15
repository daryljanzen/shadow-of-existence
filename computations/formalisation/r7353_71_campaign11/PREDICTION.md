# `r7353+71.13` — PRE-REGISTRATION: campaign 11, row 58's last half: the Legendre transform on the positive kinetic form, and the sign read off the per-mode Euler–Lagrange equation. ⌗ `100` lines (band 50–180), ⛔ stop `220`, no table. ⌗ p `0.7`. ⌗ If it lands, row 58 moves from half to DONE

*Orders: `FOR_71.md` §`r7353` ① (register before building, census in the same push). Written before anything is
built. The receipt is `receipts/P10_canonical_time/P10_step_three_is_written_down_…sign.py`, sections B and C. Its
section A is rows 58's two halves already built (`r7353+71.2`, `+71.12`).*

## ① The piece

Four statements, each the receipt's own gate, made exact:
1. ***The Legendre transform as a transform.*** For `L(v) = (α/2)v² + W` with `α > 0`, `sup_v (p·v − L(v))` is
   `p²/(2α) − W`, attained at `v = p/α`. The receipt computes `p·v − L` at the stationary point. This proves it is
   the supremum, which is where `α > 0` (the positive kinetic term from `r7353+71.2`) is actually used.
2. ***The per-mode Euler–Lagrange equation.*** For `L = (a³/8κ)φ̇² − σ(a/2κ)(μ²/4)φ²`, with `a` and `φ` twice
   differentiable and `a ≠ 0`:
   `d/dt(∂L/∂φ̇) − ∂L/∂φ = (a³/4κ)(φ̈ + 3(ȧ/a)φ̇ + σ(μ²/a²)φ)`.
   This is the friction term `3ȧ/a` and the frequency `ω² = σμ²/a²`, proved through `HasDerivAt`, not read off.
3. ***The sign.*** With `μ² = m² − 1`:
   - `σ = +1` gives `ω² = μ²/a² > 0` for every `m ≥ 2`, which is `r6998`'s banked `ω_m = μ_m/a`;
   - `σ = −1` gives `ω² < 0` at every such level.
4. ***The power of `a` in the measure:*** `det(a²M) = a⁶ det M` for `3 × 3`, so `√γ = a³` at `det E = 1`.

***Failable:*** BUILT, BUILT IN PART or REPORTED. p `0.7` under the stop.
- ***Risk:*** the `sup` in (1) through `ciSup`/`IsLUB` plumbing, and the derivative bookkeeping in (2).
- ***What it will not build:***
  - The per-mode coefficient `−μ²/4` is `r7034`'s level sum divided by the degeneracy. The receipt uses it and does
    not re-derive it, and so does this. It enters as a hypothesis-free constant, named as an input.
  - The `a⁻²` from the curvature's dimension is not built here. That would be the scalar curvature's scaling under a
    constant rescaling, which needs the engine (probes cannot import each other).

***Census if BUILT:*** row 58 moves `DONE (chartable half)` → `DONE`, with the two inputs above named as caveats.
Then the counts are DONE `46` and halves `11`.

## ② Decisive fraction, survival, compile

- ***Decisive:*** (2). It is the only step where the sign could be lost to a convention.
- ***Readings:*** none new. The running rate stays `14` of `21`.
- ***Compile:*** no table, so under a minute.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
