# r7838 (60) — RESULT: the operator moves, the sampler converges, and the control is now loose by four

On order `r7833` (69), items ①–④, against `PREDICTION.md` as registered and pushed before any run.

## THE HEADLINE

**Every defect `r7836` named, and three more this revision found, are closed — and the control still
does not reproduce the published limit.** It now misses it in the OPPOSITE direction: a `95` per
cent upper limit of `277.7` meV against the published `64.2`, where `r7836`'s was `26.5`. So
registered arm **Ⓔ⑤ FAILS**, with the criterion exactly as written, and the arm of record is
**NOT JUDGED** for the second revision running.

**But the half `r7836` called decisive is now right.** The control's fitted matter-density gap comes
out `+3.70` per cent against the published `+2.48` — the published SIGN — where `r7836`'s came out
`-2.43`. And the arm of record's gap comes out `-1.11` per cent, against `72`'s banked estimate of
`-1.00`, where `r7836`'s apparatus gave `-5.21`.

⇒ **AND THE LOOSENESS IS LOCATED.** It is not the lensing operator, not the minimiser, not the
ruler. Holding the ruler instead of marginalising it moves the limit by five per cent. What is left
is WHAT this harness scores: `185` temperature bins, no polarisation, no lensing reconstruction, no
low-`l`. That is the thing the next revision has to change, and no further turn of this crank will
substitute for it.

## THE NUMBERS, all from converged chains

| | control | arm of record | published |
|---|---|---|---|
| `95` per cent upper limit on the sum | `277.7` meV | `304.1` meV | `64.2` meV |
| factor against the published limit | `4.33` | `4.74` | — |
| effective mass, the sum free to go negative | `+67.5 ± 106.0` meV | `+64.1 ± 115.7` meV | `-101` meV |
| matter-density gap | `+3.70 ± 4.82` per cent | `-1.11 ± 4.95` per cent | `+2.48` per cent |
| `chi^2` at the minimum, `185` bins + BAO | `194.57` | `190.61` | — |
| posterior mass below `59` meV | `29.7` per cent | `29.0` per cent | — |
| posterior mass below `64` meV | `32.2` per cent | `31.4` per cent | — |
| worst split `R-hat`, five parameters | `1.0003` | `1.0012` | — |
| smallest effective sample size | `17848` | `9301` | — |

The control's own limit with the ruler HELD at the instrument's sound horizon of `144.53` Mpc:
`262.9` meV, effective mass `+105.0` meV, gap `+8.32` per cent.

The control's limit with the sum's range capped at `0.30` eV instead of `0.60`: `245.9` meV. The
ceiling doubled and the limit moved `13` per cent, so the posterior falls off on its own and the
limit is the data's rather than the grid edge's.

## THE ARMS, each as registered

* **Ⓐ① PASSES, and it is the one that needed care.** The rebuilt operator did NOT reproduce
  `r7836`'s `0.372` per cent at `0.06` eV and `0.768` at `0.12` "peaking at `l ~ 1980`". So instead
  of guessing, each convention that could have produced those figures was measured, and one does,
  to the printed digits: CAMB's DEFAULT one-massive-species split, with `omch2` held so the total
  rises with the sum, on the window the arms' own spectra reach — `0.3717` per cent at `l = 1979`
  and `0.7681` at `l = 1977`. In the convention the fit actually runs on (the total held, three
  degenerate species) the same signature is `0.1896` and `0.4541`, peaking at `l = 1967`.
  ⇒ **`r7836`'s figure is a factor `1.96` too large at `0.06` eV for the fit it was quoted about**,
  and the claim it carried — that the omitted signature is "the same order as" the retained `0.84`
  per cent lever — is an overstatement: in the fit's own convention it is a quarter of it.
* **Ⓑ② PASSES.** The operator's response is strictly increasing across the whole scan, `0.1896` per
  cent at `0.06` eV to `2.4034` at `0.60`.
* **Ⓒ③ PASSES by six orders of magnitude.** Leave-one-out at every interior node agrees to about a
  millionth of the smallest bin uncertainty, and a spectrum GENERATED at an off-grid sum of `0.21`
  eV agrees with the interpolated model to the same, on both arms. The registered criterion was a
  tenth of a bin uncertainty.
* **Ⓓ④ PASSES.** Six chains, the proposal held after a staged burn-in: worst `R-hat` `1.0012` against
  the registered `1.05`, smallest effective sample size `9301` against the registered `1000`.
* **Ⓔ⑤ FAILS.** `277.7` meV is outside the registered `42.8` to `96.3`, and the effective mass is
  POSITIVE where the published one is negative. Reported as failed, criterion unchanged.
* **Ⓕ⑥ PASSES.** The gap is `+3.70` per cent, the published sign.
* **Ⓖ⑦ NOT JUDGED**, because its precondition Ⓔ⑤ failed. Its registered DIRECTION does hold —
  the arm's limit `304.1` meV is LOOSER than the control's `277.7`, which is what was registered —
  but a direction read off an apparatus that misses its own control is not a result, and the arm's
  number is NOT reported as a limit.
* **Ⓗ⑧** the arm count, asserted in the receipt.

## THREE DEFECTS OF THE BORROWED HARNESS, found while rebuilding it

**① `r7836`'s named cause runs the wrong way.** `r7836` named the frozen operator as the reason its
limit came out too TIGHT. Measured at the grid centre, freezing the operator at `0.06` eV LOWERS
`chi^2` at large sums — by `7.931` at `0.30` eV on the arm of record and `5.003` on the control — so
the frozen harness prefers large sums MORE than the honest one, and its limit is too LOOSE on that
account. Whatever made `r7836`'s limit tight, it was not this.

**② The ruler was pinned, not marginalised.** `r7836` minimised `r_d` inside `(120, 170)`. Over the
region the fit explores the minimising `r_d` leaves that interval, and the bracket binds at `78` of
`441` points in the box on the control and `77` of `441` on the arm — about `17.6` per cent of it —
adding up to `3113` and `3230` in `chi^2` where it binds. A bound that binds is not a
marginalisation. What exposed it was a kink: an interpolation of a term whose second differences are
`1e-13` came out wrong by eleven.

**③ The BAO term is one-dimensional.** With `r_d` minimised, the control's BAO `chi^2` is EXACTLY
independent of `H0` — identical to eight decimals across fourteen units of it, because the ruler
rescales to absorb it — while the arm of record's moves by about `0.03` over the same span. So that
term constrains `Omega_m` alone, which is WHY the sum is so nearly degenerate with `Omega_m` in this
fit: a one-dimensional term is the only thing paying for a moved total. `r7836` orthogonalised
against that degeneracy without naming where it comes from.

## AND ONE DEFECT OF THIS REVISION'S OWN FIRST ATTEMPT, caught before it was read

A short run of the sampler before the real one had Powell walk into the flat `1e12` penalty region
and report the plateau as a minimum, where Nelder-Mead reached `190.6` on the same tree — the same
class of failure `r7836` reported, found here by a smoke test rather than by a reviewer. The
infeasible region is sloped now, any result landing on the barrier is DISCARDED rather than
reported, and the receipt asserts that the reported minimum is the objective at its own point.

## WHAT IS OWED, and it is one thing

The instrument's physics is now right as far as this harness's data can test it. **What it lacks is
data.** The published `64.2` meV rides on polarisation and on the lensing-reconstruction spectrum,
which is the measurement that weighs neutrinos most directly, and on a ruler calibrated against the
microwave background rather than floated. This harness has none of the first two. Until it scores
them, a limit it produces cannot be compared with the published one in either direction, and the
arm of record cannot be read.

`P15` is unchanged, as the order requires until the arm is read.
