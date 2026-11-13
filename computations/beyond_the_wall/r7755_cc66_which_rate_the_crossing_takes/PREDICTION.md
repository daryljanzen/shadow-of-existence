# `r7755+cc66` — REGISTRATION: INVERTING THE CUT FOR THE LEAF RATE

⛭ **Pushed before a line of `invert_cut.py` exists.** Order `r7755`, the item that follows §③: *"invert
`H²(r) = H²_leaf(z(r))` for the mass function it demands, and say whether that `m(r)` is admissible."*

## WHY THIS IS NOW LOAD-BEARING AND NOT A CURIOSITY

The reading of the corpus this revision sets out (see `FOR_66.md`) leaves exactly three options and no
fourth:

* **(a)** the leaves' areal-radius history IS the vacuum cut's, and the distance takes `H_stack`;
* **(b)** the actual history is the one the full field equations give on the leaf, and the distance
  takes `H_leaf`;
* **(c)** radiation enters the cut itself, so that the cut's own rate IS the leaf rate.

`r7753+cc66`'s §③ showed that **no amplitude** of the `ρ_r ∝ r⁻⁴` profile reaches (c). This inversion
asks the stronger question: does ANY mass function reach it? If none does, (c) is closed outright and
the choice is exactly (a) against (b) — which is a classification question and not a dynamical one.

## THE SETUP, FROM THE CORPUS'S OWN EQUATIONS

`P15` `sec:properframe` step (iii) writes the radial equation at `E = 1` as
`(dr/dτ)² = 2GM/c²r + r²/α² − k`, with `k = 1 − E² = 0`. Dividing by `r²` and using `H = (dr/dτ)/r`:

> **`H²(r) = (2G/c²)·m(r)/r³ + 1/α²`** — for a general mass function `m(r)`, with the straight cut
> `m ≡ M` returning `c²H²_stack = (c²/α²)(1 + 2(1+z)³/x₀³)` through `1 + z = r₀/r`, `x₀ = r₀/r_N`,
> `r_N = α/√3`.

⛭ **The algebra was done by hand before this file was written, and the result it predicts is stated
below so the computation is a CHECK OF A STATED EXPECTATION rather than a search.** Saying so is the
point of registering: if the run disagrees with any row, the row is wrong and gets reported as wrong.

## `R1` — THE DEMANDED MASS FUNCTION

| row | expectation | licence |
|---|---|---|
| **① the form** | `m(r) = M + K/r` **exactly**, with `K = (c²/2G)·H₀²Ω_r·r₀⁴` | the recomputed `m(r)` reproduces `H_leaf(z)` to `< 1e-10` relative over `z ∈ [0, z*]`, and the closed form above matches the solved one to round-off |
| **② the sign** | `m'(r) = −K/r² < 0`: the mass function DECREASES outward | checked on a grid; `m' < 0` at every node |
| **③ the density** | `ρ(r) = m'(r)/(4πr²) = −K/(4πr⁴) < 0` — **radiation's own `r⁻⁴` profile with the sign reversed** | `ρ < 0` at every node, and `ρ·r⁴` constant to round-off |
| **④ admissibility** | **NOT admissible**: weak and null energy conditions violated at every radius, and `m(r) → ∞` as `r → 0` | both stated against the computed arrays rather than asserted |

⛔ **`R1` FIRES AGAINST THE LEAF-RATE READING'S EASIEST ROUTE, NOT FOR IT.** If ①–④ hold, option (c)
is closed: there is no cut, bent however one likes, whose own rate is the leaf rate. That REMOVES the
reading on which radiation could enter the rate dynamically, and leaves the question where this
revision's reading puts it — on which object the distance is read off.

## `R2` — THE CONSISTENCY CHECK THE PRESENT TEXT ALREADY CARRIES

`P15` `sec:flatlcdm` prints the physical bend's law as
`H² = H₀²[Ω_m(1+z)³ + Ω_Λ − 3Ω_r z(1+z)³]`, a radiation term `−3z/(1+z)` times the leaf's.

| row | expectation | licence |
|---|---|---|
| **⑤** | taking `ρ_r ∝ r⁻⁴` POSITIVE with `m(r₀) = M` reproduces a term `∝ −z(1+z)³` — the printed `z(1+z)³` shape, **sign and all**, from this same `H²(r)` relation | the recomputed exponent structure matches `−z(1+z)³` to `< 1e-10` relative, so the inversion and `r7614`'s published law are one instrument |
| **⑥** | and the two normalisations differ: the exact-leaf cut does **not** satisfy `m(r₀) = M` | reported as a number, `m(r₀) − M`, not as a verdict |

⌗ **If ⑤ fails, the inversion is not reading the same object `r7614` read, and nothing in `R1` may be
quoted against the corpus until that is resolved.** That is the honest failure mode and it is named
here rather than discovered later.

## WHAT THIS REGISTRATION DOES NOT LICENCE

* **No claim that (b) is right.** The inversion closes (c). Choosing between (a) and (b) is a reading
  of the corpus, carried in `FOR_66.md`, and no number here decides it.
* **No new background, no fit, no significance.** `H₀`, `Ω_r`, `Ω_m` and `α` are the sector's published
  values, read from 60's `r7580/lightpath.py` by path as at `r7751` and `r7753`.
* **Not a claim about LTB generality.** `ρ = m'/(4πr²)` is the mass-function reading the corpus itself
  uses for the bend; if the corpus's own convention differs, the convention is reported, not replaced.
