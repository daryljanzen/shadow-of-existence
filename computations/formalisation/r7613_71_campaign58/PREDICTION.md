# `r7613+71.2` — PRE-REGISTRATION: campaign 58, `r7613` ④, `lem:alignment`'s computational half. ⌗ `250` lines in one probe (band 100–600), ⛔ stop `1000`. ⌗ p: static half `0.9`, retarded half `0.85`

*Under `r7613` ④. The source is `corpus/BH_causality_v2.tex`, lines 330–345. No Lean was written before this registration.*

## ① The pieces (`probes/SchwarzschildSlicing.lean`)

Here `f(r) = 1 − r_h/r` with `r_h > 0`.
- ***Static slicing.*** The Schwarzschild metric is diagonal, `diag(−f, f⁻¹, r², r² sin²θ)`. Its explicit inverse
  has `g^{tt} = −f⁻¹ = −(1 − r_h/r)⁻¹`, checked as a matrix identity `g · g⁻¹ = 1` for `r > r_h` and
  `sin θ ≠ 0`. Then `g^{tt} → −∞` and `N = (−g^{tt})^{−1/2} = √f → 0` as `r → r_h⁺`.
- ***Retarded slicing.*** In `(u, r)` coordinates (`u = t − r*`), the metric is `−f du² − 2 du dr + r² dΩ²`. Its
  inverse block has `g^{uu} = 0`, `g^{ur} = −1`, `g^{rr} = f`, checked as a matrix identity. For
  `Θ = a(u + ηr)`, `∇Θ = (a, aη)` and `g^{ab}∇aΘ∇bΘ = a²(fη² − 2η) = a²η(fη − 2)`. This tends to `−2a²η` as
  `r → r_h`, and it is finite and negative there for `a ≠ 0`, `η > 0`.

***Failable:*** BUILT, BUILT IN PART, or REPORTED. ***Reachable negative:*** if the matrix-inverse identities
cannot be closed by `Matrix.inv`/`simp`/`field_simp` within the stop, the inverses are stated as the two-sided
inverse property, which is the identity itself, and the use of `Matrix.inv` is REPORTED. The limits must land.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
