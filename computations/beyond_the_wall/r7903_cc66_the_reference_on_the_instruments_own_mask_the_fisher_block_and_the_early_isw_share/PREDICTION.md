# r7903+cc66 — REGISTRATION for order ⑲, written and pushed BEFORE a line of the computation exists

Order `r7903` (69), items ⑲①–④. Registered because ⑲① says so in its own words — *"Register the
expected size first"* — and because the standing rule puts the registration in its own pushed commit
ahead of any computation. Nothing below is measured yet; every figure is an expectation with the
record it is drawn from, and every outcome that would refute it is named.

## Ⓐ ⑲① — AND THE ORDER'S OWN PREMISE IS OFF BY SIXTEEN BINS, FOUND BEFORE COMPUTING

⑲① says: *"set the model to `NaN` below `ℓ = 100`, so that `score_ttteee` keeps exactly the
instrument's 555 bins."* **Read against the arrays, that substitution keeps 571, not 555.** Measured
on `score_ttteee`'s own `BIN_LO`/`BIN_HI`/`BLOCK` before any scoring:

| cut | bins removed | kept |
|---|---|---|
| `BIN_LO < 100` | **42** (14 each from `TT`, `TE`, `EE`) | 571 |
| `BIN_HI > 1996` | **16**, every one `TT` (`BIN_LO` 1997–2476) | — |
| **both** | **58** | **555** |

⇒ **The instrument's mask is `ℓ ≥ 100` AND `ℓ ≤ 1996`, which keeps `185` bins from EACH of `TT`,
`TE` and `EE`.** That `185/185/185` symmetry is why I take this to be the intended mask rather than
a coincidence of counts: a low cut alone leaves `TT` with 201 against 185 apiece for `TE` and `EE`,
because `TT` runs to `BIN_LO 2476` while `TE` and `EE` stop at `1980`. The threshold is not knife
edged — any `BIN_HI` bound in `1996..2012` removes the same 16.

⌗ *So I will do what ⑲① INTENDS, not only what it says: both bounds, `555` bins asserted as a
control before any limit is read, with the literal reading (`571`, low cut only) reported beside it
so the difference is visible rather than silently resolved. If 69 meant the literal `571`, the one
number to take from this is the `555` row and the rest is re-read on request.*

### Ⓐ① The band, decomposed because the operation is TWO cuts and my legs measure them separately

| part | this substitution | nearest measured leg | that leg's move |
|---|---|---|---|
| low | 42 bins (14/block) | `r7863` `bot1800`: 49 bins | `rd_camb` `0.9862`, `rd_min` `1.0320` |
| top | 16 bins (all `TT`) | 60's own: 36 from the top | `0.28` meV |
| top | — | `r7863` `top1800`: 49 bins | `rd_camb` `0.7697`, `rd_min` `1.2355` |

Both parts are SMALLER than the nearest measured leg (42 < 49; 16 < 36 < 49), so each move should be
bounded by it.

⇒ **REGISTERED Ⓐ①: the low part alone is `≤ 0.99` meV (`rd_camb`) and `≤ 1.04` (`rd_min`); the top
part alone is `≤ 0.28` meV; and the FULL 555-bin substitution moves both limits by `|move| ≤ 3.0`
meV, with a central expectation near `1.3` meV.** The `3.0` is deliberately wider than the sum of
the parts, for the reason in Ⓐ② below.

### Ⓐ② ⛔ AND WHETHER THE TWO PARTS ADD IS ITSELF REGISTERED, BECAUSE MY OWN RECORD SAYS IT MAY NOT

`r7892` found a low-end decomposition ADDITIVE at a `6.5` per cent residual; `r7894` then found the
same decomposition NOT additive on the held clock, at `24.7` per cent, **and named the cause: the
four free parameters were absorbing a cross-block interference.** `r7896` narrowed that interference
to the spectral tilt's alone.

⇒ **REGISTERED Ⓐ②: low-plus-top is additive to within 20 per cent of the full move.** Refuted by a
residual above that, which would say the two cuts interfere through the same freedom `r7894` found —
and would make a sum-of-parts estimate of ANY masked limit unsafe, not just this one.

### Ⓐ③ The discriminator I registered before finding the mask, kept because it still bites

`r7903` says *"your `r7863` low cuts suggest it is small"*, and by Ⓐ① that is right. **But this
seat's OTHER record says the opposite about low-end removals:** `r7866`/`r7892` measured the
**36 lowest bandpowers** moving the crossing by **`48.202`** meV. Fewer bins than this
substitution's 58, thirty times the move.

| outcome | what it selects |
|---|---|
| `|move| ≤ 3.0` meV | **the count and the clock are what matter.** The `bot`/`top` legs are the like-for-like operation and `r7866`'s `48.202` is a property of its re-profiled clock, not of the low end. |
| `|move| ≫ 3.0`, toward `r7866`'s scale | **the operation is what matters, and `r7903`'s "small" rests on the wrong leg** — a held-parameter cut and a re-profiled cut are different quantities. |
| `|move| < 0.3` meV | the 58 bins carry less than 36 arbitrary ones, so the mask BOUNDARY and not the count sets the cost. |

⌗ *My position: the first row. The `bot`/`top` legs are this operation in all but name — same reader,
same baseline, held parameters — and `r7866`'s figure comes from the clock `r7894` showed was
absorbing an interference.* ⌗ *One branch of my earlier draft is now CLOSED rather than carried: I
had registered as live the possibility that "bins below `ℓ = 100`" is not the set "the 42 lowest
covered bins". It is — checked on the arrays, the two sets coincide exactly — so the `bot`-leg
analogue is apt and that uncertainty is retired before scoring rather than after.*

## Ⓑ ⑲② — the 5×5 Fisher block, and what would make the factor of 320 either side's

The block is `(Σ, H0, Ω_m, ω_b, n_s)` from this seat's fitter at the reference point, on the 555-bin
mask from ① **and** on 613. `60` measured that freeing `ω_b` and `n_s` moves the instrument's limit
by **`89.6`** meV and the reference's by **`0.28`** — a factor of **`320`**, which `r7903` calls the
largest unexplained number in the comparison.

⇒ **REGISTERED Ⓑ①: the reference is STIFF along `ω_b` and `n_s`.** Concretely: the `2×2` sub-block
for `(ω_b, n_s)` is well conditioned, and the correlation of each with `Σ` satisfies
`|ρ(Σ, ω_b)| ≤ 0.8` and `|ρ(Σ, n_s)| ≤ 0.8` on both masks.

⇒ **REGISTERED Ⓑ②: the factor of 320 is then the INSTRUMENT's degeneracy and not the reference's
stiffness being unusual** — a `0.28` meV move is what a well-conditioned likelihood does, and `89.6`
meV is what a nearly-degenerate one does.

⚠ **What would refute Ⓑ①:** `|ρ| > 0.95` along either direction, or a `(ω_b, n_s)` sub-block whose
condition number exceeds `10^4`. Then the reference is *also* soft there, the `0.28` meV has some
other cause, and `r7896`'s finding that the interference is the tilt's alone does not transfer.

⌗ *`Σ` is bounded below at `0`, so a Fisher block at `Σ = 0` sits on the boundary of the physical
region. I register in advance that I will report the block at the reference point as asked AND state
that the `Σ` row/column is a one-sided curvature there, because a symmetric error ellipse through a
boundary is not a confidence statement — and that caveat is registered now rather than offered later
if the number looks awkward.*

## Ⓒ ⑲③ — the early-ISW share bin by bin

Definition, fixed here and written at the head of the computation: **`(full − no_ISW)/full` per
plik_lite `TT` bin with `100 ≤ ℓ ≤ 207`, UNLENSED scalar `TT`, on the reference's parameters, at
`Σ = 0, 0.06, 0.30, 0.60` eV.** `no_ISW` removes CAMB's own ISW source term, which `r7895+cc66.2`
established is the **TOTAL** ISW; the late half is at most `2.82e-04` there, so in this band the
total is the early ISW to within that, which is why this is the early-ISW share.

⇒ **REGISTERED Ⓒ①: the band-aggregate share is `0.44 ± 0.05`** at every sum, from the aggregate
`0.4436`–`0.4514` already banked at `r7895+cc66.2`.

⇒ **REGISTERED Ⓒ②: bin by bin the share is POSITIVE in every bin and FALLS with `ℓ` across the
band**, because the early-ISW boost is a first-peak effect and `ℓ = 207` is nearer the peak than
`ℓ = 100` is. *Stated as a shape claim so it can fail: a share that rises with `ℓ`, or any negative
bin, refutes it.*

⇒ **REGISTERED Ⓒ③: the share's dependence on `Σ` is WEAK — the per-bin spread across the four sums
is under `0.02` absolute in every bin**, from the aggregate moving only `0.4436 → 0.4514` over the
whole range.

⌗ *`60` computes the same on the instrument as its own ②, and `r7903` is explicit that neither side
reads the other's before both are banked. This registration is what makes that possible from my
side: the definition and all three expectations are fixed here, in a pushed commit, before the
computation exists.*

## Ⓓ ⑲④ — the one line, which the record already answers

The ruling is that the convention of record is `Δχ²` referenced to **the profile's minimum over the
physical region `Σ ≥ 0`**. On this seat's reference profile that minimum sits at **`Σ = 0.06` eV**,
on both the calibrated and the minimised columns, as banked in `r7895`'s `limit_read.json`
(`min_at = 0.06`, `fork.branch = Ⓝ⓵′`, `limit_readable = true`).

⇒ **So under the ruling my limit is the `193.548` meV reading — the one that agreed with `60`'s
`193.545` to one grid step — and NOT the `216.282` meV lowest-sum reading.** The `22.734` meV gap
I measured between them stands as a measurement of what the convention is worth, and is no longer a
live alternative: it is the cost of the convention `r7903` has ruled against.

⌗ *This item is a statement about my own record, so it carries no band. It is registered here rather
than simply answered so that the figure I report cannot drift from the one already banked.*

## Ⓔ What would make this whole revision wrong

* ⑲① landing outside both the `6.0` meV band AND the `r7866` scale — neither mechanism, so the
  substitution does something I have not modelled.
* The 555-bin mask from ① not reproducing `555` exactly. The count is the check that the `NaN`
  substitution did what ⑲① asks, and a different count means the mask is not the instrument's.
* The uncut control failing to reproduce the banked `613`-bin totals EXACTLY. `r7863`'s own run
  refused to report cut numbers until that control passed, for the same reason, and that control is
  carried forward here.
* Any of ⑲③'s three expectations holding only after the definition is adjusted. The definition is
  fixed above and will not be restated to fit the result.
