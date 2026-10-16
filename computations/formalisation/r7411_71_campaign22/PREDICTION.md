# `r7411+71.8` — PRE-REGISTRATION: campaign 22, row 95 under THE connection: SdS's `so(3)` Killing fields, and the scalar wave operator separating on spherical harmonics. ⌗ `380` lines (band 220–700), ⛔ stop `850`. ⌗ p `0.55`

*Daryl's instruction: build. Row 95 was misfiled as no-connection (`r7411+71.2`); its content is connection
content, now reachable. The receipt (`P15_the_four_dimensional_treatment…`) was read in full at `+71.2`.*

## ① The piece: `probes/Row95Wave.lean`

- ***(A) Killing:*** on `−F dt² + dr²/F + P(dθ² + S dφ²)` (with `P = r²`, `S = sin²` near the point), the three
  `so(3)` fields have zero Killing form under THE connection at every point off the poles:
  - `∂_φ`;
  - `sin φ ∂_θ + cot θ cos φ ∂_φ`;
  - `cos φ ∂_θ − cot θ sin φ ∂_φ`.

  This uses `killF_model` (campaign 19, re-proved locally because probes do not import each other) and the
  engine's `gamD`.
- ***(B) Separation:*** `boxD` of `cos(ωt) R(r) Y(θ, φ)` equals `cos(ωt) Y` times the radial operator
  `ω²R/F + (1/r²)(r² F R′)′ − ℓ(ℓ + 1) R / r²`, for ANY `Y` satisfying the angular eigen-equation at the point.
  This is one theorem for all `ℓ, m`.
- ***(C) The receipt's nine harmonics:*** `ℓ = 1, 2, 3`, `m = 0..ℓ`, each satisfies the eigen-equation with
  `ℓ(ℓ + 1)`. That is trig identities, with real harmonics (`cos mφ`, `sin mφ` times associated Legendre in `cos θ`)
  standing for the receipt's complex ones. Hence "the same operator for every `m`" and
  `op(2) − op(1) = −(6 − 2)R/r²`.
- ***(D)*** `L(L + 2) = 4j(j + 1)` at `j = L/2` (`ring`).

***Not built:*** the receipt's Hopf-fibre part (four ad hoc expressions with hand-assigned `m`), and its text pins.

***Failable:*** BUILT (A–D), BUILT IN PART, or REPORTED. p `0.55`.
- ***Risks:*** (A)'s two non-constant fields, which have `cot θ` coefficients; and (B)'s contraction through `gamD`,
  with four nontrivial coefficients.

***Census if BUILT:*** row 95 `ORDER: ENGINE-REACHABLE` → `DONE`.

## ② Compile

Priced `1–5` minutes.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
