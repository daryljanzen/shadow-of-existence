# `r7711+cc66` — VERDICT: **(3) TODAY, BUT NOT FOR THE REASON I REGISTERED — AND THE READING THAT SETTLES IT IS PRICED**

The registered answer was (3) *because both routes would be blocked*. **One of the two obstructions held and
the other did not.** What blocks the answer is neither of the things I named: it is the acceptance banks'
`l` sampling, and that is removable for a stated price.

## ⓵ OBSTRUCTION 1 HELD — no smoothing resolves a tenth with a plateau intact

| half | n_lo | source sd | source's own step | a tenth of the spectra's |
|---|---|---|---|---|
| `0.175` | 8 | `0.00622` | `+0.0025` (`0.40` sd) | `0.39` sd |
| `0.250` | 6 | `0.00367` | `+0.0024` (`0.65` sd) | `0.66` sd |
| `0.350` | 4 | `0.00206` | `+0.0018` (`0.88` sd) | `1.18` sd |
| `0.425` | 3 | `0.00171` | `−0.0006` (`0.36` sd) | **`1.42` sd ← the best available** |
| `0.450` | 2 | — | — | ⛔ UNMEASURABLE |
| `0.550` | 0 | — | — | plateau empty |

**No setting resolves a tenth.** Two things the sweep shows that the argument for it did not: the scatter
**stops falling** past `0.35` (it wobbles back up at `0.375` and `0.400`), because the plateau has too few
points for its own variance to be stable — *so widening stops buying resolution well before it stops being
measurable*; and a setting with under three plateau centres is **refused** rather than given a scatter,
because the standard deviation of two numbers is not a scatter.

## ⓶ OBSTRUCTION 2 DID **NOT** HOLD — the kernel swap is LIVE, which I had registered as the likely blocker

Registered: the only banked kernel is the acceptance law's, which `r7703` and `r7707` measured as having no
step of its own, so a swap test on it should be inert. **The control says otherwise.**

| fixed source | own kernel against the other's | |
|---|---|---|
| `lcdm` | median `6.196` %, max `17.37` % | |
| `cr` | median `6.267` %, max `21.08` % | |

⇒ **The swap moves the pseudo-spectrum by some six per cent in the median and up to twenty-one. The
instrument is live, and the registered inertness case is ruled out.**

⌗ **And this is not a contradiction of `r7707`, because it is a different object.** `r7707` read the
acceptance law's **own band ratios** `A_l` — the retention factor — and found them ramping. Here the object
is a **pseudo-spectrum**, the source's oscillating power carried through the kernel, `Pseudo(S,K)_l = Σ_k
G_l^K(k)² S(k)² dk/k`, which keeps the source's comb and lets the kernel modulate it. *The two differ, and
saying which is which first is the whole reason this does not read as `r7707` reversing itself.*

## ⓷ THE DISCRIMINANT HAS THE RIGHT STRUCTURE — AND IS NOT RESOLVED

| ratio | what it isolates | best step | at |
|---|---|---|---|
| own × own, `(cr│cr)/(lcdm│lcdm)` | both differences | `+0.0232` | `1.99` sd |
| kernel held, `(cr│lcdm)/(lcdm│lcdm)` | the **source** difference alone | `−0.0277` | `1.35` sd |
| source held, `(lcdm│cr)/(lcdm│lcdm)` | the **kernel** difference alone | `+0.0482` | `1.71` sd |

**What this would say if it were resolved:** the kernel difference alone produces a step of the measured
**sign and about twice the measured size**, the source difference alone produces one of the **opposite
sign**, and the observed step is what survives their partial cancellation — which would favour *the
projection creates it, and the source partly cancels it*. And own × own reproduces the measured step's size
(`+0.0232` against the spectra's `+0.0242`).

⛔ **It is not resolved, and I do not report it as an answer.** Every one of the nine readings sits between
`0.73` and `1.99` sd of its own plateau scatter. **Nothing here passes two sigma.** *That is the `r7695`
trap exactly — a shape that looks like a decomposition at a significance that cannot support one — and the
only thing that stops this becoming `r7695` again is refusing it at the point where the pattern is most
inviting.*

## ⛭ SO WHAT ACTUALLY BLOCKS IT IS THE SAMPLING, AND THAT IS NOT WHAT I REGISTERED

The acceptance banks carry `238` `l`, of which **87** fall in `q ∈ [0.80, 3.10]`. The fine spectra `r7707`
read carry **1900**. ⇒ The low significance is a **limit of the acceptance banks' `l` grid, not of the
method**, and the method is the one route of the two that works.

**Priced, from this revision's own measurement:** scatter falls as `1/√n`, so taking own × own from
`1.99` sd to `5` sd needs about **`6.3`× the `l` points — some `549` per combination**, against `87` now.
At the measured `1456.7` s for four combinations at `87`, that is about **`2.6` hours**. ⇒ **That is the
reading that settles the question, it needs no new instrument and no solver run, and it is an afternoon of
compute rather than a rebuild.** *It is 69's to order or not.*

## ⚑ THE PRICE — I REGISTERED IT WRONG, AND THE REASON IS SPECIFIC

Registered **under 300 s**; measured **`1456.7` s**, a `4.9`× overrun. The registration committed to saying
what it cost rather than charging it elsewhere, so:

⛔ **I priced the kernel by its array size — `560 × 2547` Bessel evaluations per `l` — and ignored
`spherical_jn`'s cost as a function of ORDER and ARGUMENT.** Measured after the fact, the per-call cost
runs from about `1.9` s at `l = 100` to `0.18` s at `l = 900`, a factor of ten across the range, and the
real arguments (`k·x₀` up to some `4000`) sit far outside the range I sanity-checked when setting the
bound. *The two arms also differ: the `lcdm` combinations cost `465` s each against the `cr` ones' `262`,
because the `k` grids are `2547` and `1452`.* **A cost model built on how much data a call touches and not
on what the call does is not a cost model.**

## WHAT IS NOT CLAIMED

- **Neither alternative is favoured.** "Fails to cancel" was registered as not the default and it is not
  the conclusion; "creates" is the direction the unresolved numbers point, and pointing is not showing.
- **Nothing is printed from this revision.**
- **No attribution**, unchanged across `r7707`, `r7709` and here.
- ⚠ **The own × own agreement with the measured step's size is consistency at under two sigma**, and is
  offered as that and nothing more.
