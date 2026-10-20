# `r7443+71.26` — PRE-REGISTRATION: campaign 42, library-gap row 96 (the history is spherically symmetric throughout, so the Chern–Simons number never moves). ⌗ `900` lines (band 500–1600), ⛔ stop `2100`. ⌗ p `0.35`

*Under `r7443` ②, step 4, registered with campaign 41 in one push. The receipt is
`P15_the_history_is_spherically_symmetric_throughout_so_the_chern_simons_number_never_moves.py`. No Lean was
written before this registration. It reuses campaign 40's Levi-Civita/Pontryagin core, copied, since probes do not
import each other.*

## ① The piece: `probes/Row96ChernSimons.lean`

- ***Part 1.*** Nariai `dS₂ × S²` has `*RR = 0`, and so does its non-diagonal rotated form.
- ***Part 2.***
  - polarised Gowdy (`ω = 0`, with `A`, `ψ`, `R` arbitrary): `0`;
  - unpolarised: nonzero;
  - row 69's plane-wave facts, quoted from campaign 40 by copying.
- ***Part 3, Stokes.***
  - The Chern–Simons current `K^μ`, with `∂_μ K^μ = −√−g *RR` on the receipt's member
    `gowdy(0, log(t−z), t−z, t)`.
  - The volume integral of `√−g *RR` over `[3,5] × [0,1]` equals minus the boundary flux, and is nonzero.
  - Mathlib's divergence theorem on a rectangle is expected.
- ***Part 4.*** The general dynamic spherically symmetric metric (`A`, `B`, `C`, `S` arbitrary in `(t, r)`, with the
  `dt dr` cross term) has `*RR ≡ 0` and `K^μ ≡ 0` for all four `μ`.
  - `PRICING.md` names the risk exactly: `K^φ` is not killed by `φ`-parity, and needs a structural argument or
    large tables.
- ***Part 6.*** The arithmetic.

***Caveats, registered.***
- The density and the current are the receipt's coordinate formulas on THE connection of the coordinate metric. Their
  covariance is not proved.
- The seven paper-text checks are pins.

***Failable:*** BUILT, BUILT IN PART (per part; Part 4's `K^φ` the likeliest gap), or REPORTED. p `0.35`.

***Census:***
- If BUILT: row 96 → `DONE`.
- If `K^φ ≡ 0` or Stokes is not reached: row 96 → `DONE (chartable half)`, the half named exactly.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
