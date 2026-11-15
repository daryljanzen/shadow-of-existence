# `r7797+cc66.1` — RESULT: item ② of `r7797`, the Gaussian's size reconciled

**9 of 9 gates**, `rc=0`, in **4.3 s**
(`receipts/P15_CR_cosmology/P15_the_papers_1_06_and_the_joint_fits_1_4967_are_one_curve_in_l_D_and_the_one_rate_sizes_are_1_0815_and_1_5238.py`).

## The answer, and it is not either of the two the order offered

69 asked which quantity each figure is — *"a difference against the null, or the residual after the
tilt, and over which bins"*. **Neither alternative distinguishes them, because they are the same
quantity.** Both are the **residual after the tilt**; both over `ℓ = 100–1758`; both over **171**
covered bins; both at **r = 1.0926**; both correlated with the analytic Gaussian-minus-power-law at
**1.000000**. The amplitude-only cost is a separate, larger column in each run (`4.9493` and
`3.4925`), so neither published figure is a difference against the null.

**One number differs: the damping multipole.** And it is one number rather than two, which is the
whole reconciliation: `α` and `ℓ_D` enter the signature **only** through `ℓ_D/√α`, and 70's faithful
copy says so in its own declared input line — `R, LD = 1.0926, 1951.9 / 1.70 ** 0.5`. So the
faithful route **is** the exponent-one form at `ℓ_eff = 1497.0390`.

| α | ℓ_D declared | ℓ_D in force | Δn_s | amp only | χ²/bin after tilt | absorbed |
|---|---|---|---|---|---|---|
| 1.70 | 1951.9 | **1497.0390** | −0.06936 | 3.4925 | **1.0619** → the paper's `1.06` | 69.6 % |
| 1.00 | 1362 | **1362.0000** | −0.08304 | 4.9493 | **1.4967** | 69.8 % |

## ⛔ And the consequence, which is the real deliverable

`sec:coherence` prints `1.06`, then **two sentences later** prints *"that rate moves the damping
multipole from 1362 to 1355.21"* and the 1.81 % growth. **Those two sentences are priced on different
damping multipoles and the text names only the second one's** — gate ① measures that the text names
the first one's exponent **nowhere**. Carrying `1.5238` to a `1.06` would be the comb error again, so
both one-rate sizes are supplied, each labelled with the `ℓ_D` it is on:

| α | ℓ_D in force | χ²/bin | growth | above `C62`'s 0.92 **and** 0.26 | correlation |
|---|---|---|---|---|---|
| 1.70 | 1489.5783 | **1.0815** | +1.846 % | yes, both | 1.000000 |
| 1.00 | 1355.2123 | **1.5238** | +1.811 % | yes, both | 1.000000 |

The move is `−0.498361 %`, read from the two banked arms' own `D_M` and applied to whichever `ℓ_D` is
in force. **So whichever figure `sec:coherence` prints, its one-rate counterpart is here, and neither
has to be carried to the other.**

## ⛔ A second collision in the same subsection, of kind rather than size — gate ⑧

`sec:diffusion-scale` prints *"costs $1.48$ in $\chi^{2}$ over the $171$ bins"* — **a total**, about
`0.00865` per bin — a few sentences before `sec:coherence` cites a receipt whose figure is `1.4967`
**per bin** over those same 171 bins. **The numerals agree to one per cent and differ by a factor of
`171` in kind** (measured ratio `172.9`). Neither sentence is wrong alone. Read together in one
subsection they are the likeliest source of two figures appearing to disagree.

## The off-input red is named, not swallowed — gate ⑦

At `ℓ_eff` the joint-fit receipt exits `rc=1`, and **exactly one** registered row reddens: `⓷ᶜ`, its
agreement with `C62`'s instrument-route displacement, which loosens to 18 % on the faithful exponent.
70 reported that row at `r7611` and PO-24 already asserts it is the one that fails. It is not a figure
`P15` prints. At the declared `ℓ_D` the same source runs clean, which is what makes the red
attributable to `ℓ_D` and not to the rewrite.

## Failability — measured, not asserted (`failability.py`)

| probe | reddens | holds |
|---|---|---|
| **P1** the faithful route priced on the header `1951.9` instead of `ℓ_eff` — the very mistake this receipt exists to stop | ② ③ ④ ⑥ ⑦ | ① ⑤ ⑧ ⑨ |
| **P2** the one-rate move scaled tenfold, published figures untouched | ⑥ | ① ② ③ ④ ⑤ ⑦ ⑧ ⑨ |

Every row that reads the fit moves under P1; the rows reading the paper, the window identity, the
kind collision and this file's own scope do not.

## Two slips the pins and the probe caught while this was built, recorded rather than hidden

1. ④'s amplitude-only literal was first `4.9558`, which I had computed as `1.4967 / (1 − 0.698)` from
   the **rounded** absorbed share instead of reading the run. Measured: `4.9493`. *Deriving a figure
   from another figure's rounding is the same error class as carrying one estimator's number to
   another's figure.*
2. The probe's first form ran the receipt's copy from a temp path without pinning its `HERE`/`ROOT`,
   so it died before any gate — then, once pinned, a **global** replace clobbered the receipt's own
   rewrite table, which holds the same two anchor strings. First occurrence only. *Both defects are
   ones I had already hit at `r7779`/`r7783`.*

## Not claimed

Which exponent `sec:coherence` **should** price the signature on is not adjudicated here and is not
mine: `α = 1.70` is 70's measurement (`r7577+70.2`) and the faithful-route argument is
`sec:diffusion-scale`'s. No significance. `C62`'s bounds are not re-adjudicated. Gate ⑨ asserts that
scope against this file's own AST.
