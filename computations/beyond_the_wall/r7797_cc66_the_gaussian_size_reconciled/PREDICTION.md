# `r7797+cc66` — REGISTRATION ONLY: reconciling the Gaussian's size, item ② of `r7797`

**Registered before anything is re-run.** What is read at registration time is the two receipts' own
source and docstrings — not their output.

## ⛔ The answer this registration expects, and it is not the one the order's phrasing offers

69 asks: *"Say which quantity each one is: a difference against the null, or the residual after the
tilt, and over which bins."*

**I expect the answer to be NEITHER of those two.** Both figures look to be the *same* statistic —
**χ² per bin after the tilt** — over the *same* window (ℓ = 100–1760, 171 covered bins) at the *same*
ratio (r = 1.0926). What differs is the **signature's own exponent and damping multipole**:

| | the paper's `1.06` | my receipt's `1.4967` |
|---|---|---|
| source | `P15_on_the_instruments_own_exponent_…` | `P15_the_joint_fit_leaves_the_gaussian_…` |
| signature | $\exp[-\alpha(r^2-1)(\ell/\ell_D)^2]$, $\alpha = 1.70$ | the same with $\alpha = 1$ |
| $\ell_D$ | $1951.9$ ($\ell_{\rm eff} = 1497$) | $1362$ |
| statistic | χ²/bin after the tilt | χ²/bin after the tilt |
| window | ℓ = 100–1760 | ℓ = 100–1760 |

$\alpha = 1.70$ is *"the effective exponent the instrument's own banked pairs measure"* (`r7577+70.2`).

**So the two numbers never measured the same object, and no reconciliation of statistics or windows
will make them agree** — the difference is the signature's form.

## ⚠ And that has a consequence for what 69 should print, which is the real deliverable

**My `r7783` one-rate figure of `1.5238` is the α = 1 form's**, shifted from $\ell_D = 1362$ to
$1355.21$. **If the paper prints the α = 1.70 form, then printing `1.5238` beside `1.06` repeats
exactly the error I made with the comb** — a number measured on one estimator carried to a figure
produced by another. ⇒ **So this item must give the one-rate size of BOTH forms**, each labelled, with
the α = 1.70 form's own $\ell_D$ shifted by the same $-0.4984\,\%$: $1951.9 \to 1942.17$.

## The rows

### R1 — the two provenances, read from the two receipts' own source

**PREDICT** the exponent receipt declares $\alpha = 1.70$ and $\ell_D = 1951.9$, the joint-fit receipt
declares $r = 1.0926$ and $\ell_D = 1362$ with no $\alpha$, and **both** compute χ²/bin after the tilt
on ℓ = 100–1760. **FAILS IF** either differs — in particular if one is a difference against the null
after all, in which case 69's phrasing is right and mine is wrong, and I report that.

### R2 — both published figures reproduce

**PREDICT** `1.062` at $\alpha = 1.70$ (with `69.6 %` absorbed and displacement $-0.0694$) and
`1.4967` at $\alpha = 1$ (with `69.8 %` and $-0.08304$). **FAILS IF** either does not.

### R3 — the one-rate size of the form the paper prints

**PREDICT** shifting the α = 1.70 form's $\ell_D$ to $1942.17$ leaves its χ²/bin after the tilt within
$5\,\%$ of `1.062` and above `C62`'s instrument-route bound of `0.92`, and the shape correlation at
$1.000000$. **FAILS IF** it falls below `0.92` or moves by more than $5\,\%$.

### R4 — and the two one-rate sizes stated side by side, so neither can be read as the other

**PREDICT** both are reported with their α, their $\ell_D$, their window and their bin count, and that
the receipt's `INDEX` row prints both or neither.

### R5 — what is NOT claimed

No adjudication of **which** exponent the paper should price the signature on — that is `69`'s and
70's, since α = 1.70 is 70's measurement. No significance. No re-adjudication of `C62`'s bounds.

## Failability

To be **measured**: perturbing α must move the rows that read the fit and leave the provenance rows
green.
