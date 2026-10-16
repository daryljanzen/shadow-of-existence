# `r7411+71.6` — PRE-REGISTRATION: campaign 21, the S³ frame core. What rows 65, 66 and 67 compute in the su(2) frame and the Euler box, built once. ⌗ `260` lines (band 150–500), ⛔ stop `600`. ⌗ p `0.6` all nine pieces

*Daryl's instruction: build. These are three of the four rows `r7411+71.2` moved off REAL OBSTRUCTION. Per
`RESULT.md` ①, most of what their receipts compute is frame algebra on su(2), plus integrals over the Euler box.
The two conventions were checked with sympy before this registration, and both hold:*
- *on the unit `S³`, `∇_{E_a}E_b = ε_abc E_c` gives `−∇²h = 6h` and `Ric = 2δ`;*
- *for a diagonal left-invariant metric `λ`, `R = 2(4e₂ − e₁²)/e₃` (Milnor).*

## ① The pieces (one file, `probes/S3Frame.lean`)

| # | piece | rows |
|---|---|---|
| 1 | `−∇²h = 6h` for every frame-constant symmetric traceless `h` (the Levi-Civita contractions on the structure constants) | 66, 67 |
| 2 | `Ric = 2δ`, `R = 6` for the unit `S³` frame | 65, 66 |
| 3 | the Milnor formula `R(diag λ) = 2(4e₂ − e₁²)/e₃`, from the Koszul formula on left-invariant fields | 65, 66 |
| 4 | constant curvature `K` in 3D: `R_ikjl h^kl = −K h_ij` for traceless `h`, `Ric = 2Kδ`, `R = 6K` | 65 |
| 5 | `tr h³ = 3 det h` for traceless `3 × 3` | 66, 67 |
| 6 | `det(e⁻¹He) = det H` | 67 |
| 7 | the Euler-box volume `∫ sinθ/8 = 2π²` over `[0, 2π] × [0, π] × [0, 4π]` | 66, 67 |
| 8 | `ζ(0) = 2[(ζ_R(−2) − 5) − 4(ζ_R(0) − 2)] = 10` | 65 |
| 9 | `∫₁^∞ q^{−4/3} dq = 3`, and the Euler–Lagrange equation of `L₂ = a³φ′²/2 − 4aφ²` is `φ″ + 3Hφ′ + 8φ/a² = 0` | 66, 65 |

***What it will not build:***
- the Euler-chart COORDINATE checks (structure equations of the explicit `σ^a`, transversality via coordinate
  Christoffels). These need a non-diagonal `Fin 3` instance.
- the `ε`-series of `R(exp εH)`;
- row 59's jet ranks and its integrals of non-constant fields;
- row 65's floating cutoff slope;
- row 66's deficiency claim;
- the imported TT spectrum (the library gap).

***Failable:*** BUILT (all 9), BUILT IN PART, or REPORTED. p `0.6`.
- ***Risk:*** piece 3 (Koszul on a symbolic diagonal metric) and piece 7 (a triple interval integral).

***Census if BUILT:*** rows 65, 66 and 67 `ORDER: ENGINE-REACHABLE` → `DONE (chartable half)`. The open half of each
is named: the Euler-chart coordinate checks. Row 59 stays ORDER, with what is built named in its text.

## ② Compile

Priced under `2` minutes.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
