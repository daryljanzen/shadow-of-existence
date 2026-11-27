# r7892 — the low-end lean decomposed by block, on crossings, not on a difference map

`r7866` located a low-end lean: removing the thirty-six lowest bandpowers — twelve from each of `TT`,
`TE`, `EE` — moves the instrument's crossing by `+48.20` meV, and two thirds of that move had no
named mechanism. `r7890` then established why a difference map cannot name it: on the band the two
pipelines differ most on, the difference operator's own artefact is seven times the signal. So this
revision does not use a difference map. It removes one block at a time and reads the **crossing**
each time, which is the quantity the limit is actually made of.

## WHAT WAS REGISTERED, BEFORE ANY PROFILE RAN

`PREDICTION.md` was committed and pushed before the first profile. It enumerated three outcomes,
explicitly **not exclusive** — "if both fire, both are reported":

| | outcome | bar |
|---|---|---|
| `Ⓚ⓵` | **additive** — the single-block moves sum to the whole | residual `< 10` per cent |
| `Ⓚ⓶` | **concentrated** — one block carries the move | `≥ 80` per cent in one block |
| `Ⓚ⓷` | **non-additive** — the blocks do not decompose the move | neither of the above |

The registered expectation was **`Ⓚ⓷`**, weakly **`EE`** if one block did dominate.

## WHAT WAS MEASURED

| mask | crossing (meV) | move (meV) | share of the whole move |
|---|---|---|---|
| the whole instrument | `68.1331` | — | — |
| minus all thirty-six | `116.3351` | `+48.2020` | `100` per cent |
| minus `TT`'s twelve | `108.8034` | `+40.6703` | `84.4` per cent |
| minus `TE`'s twelve | `76.0999` | `+7.9668` | `16.5` per cent |
| minus `EE`'s twelve | `70.8184` | `+2.6853` | `5.6` per cent |

The three single-block moves sum to `+51.3224` against the whole `+48.2020`: a residual of
`3.1205` meV, **`6.5` per cent** of the whole move, inside `Ⓚ⓵`'s ten-per-cent bar. `TT` alone
carries `84.4` per cent, over `Ⓚ⓶`'s eighty-per-cent bar.

### ⇒ BOTH REGISTERED OUTCOMES FIRE, AND BOTH REGISTERED EXPECTATIONS ARE REFUTED

`Ⓚ⓵` **additive** and `Ⓚ⓶` **concentrated** both fire, and both are reported, because the
registration said they are not exclusive and that choosing between them once the numbers are seen is
exactly what was excluded. The slight super-additivity — the parts summing to more than the whole —
is the whole of the departure from independence, and it is small.

The registered expectation `Ⓚ⓷` is **REFUTED**. The weak expectation that `EE` would dominate is
**REFUTED**: it is `TT`, by a factor of five over `TE` and fifteen over `EE`. The registration said
in advance that a refutation here would be the better outcome, because it hands the next step a
named block instead of a harder instrument. It did.

## THE REGISTERED CONTROL FIRED, AND IT WAS RIGHT

`PREDICTION.md` named `−20.09` meV as the all-three move the control had to reproduce. The measured
all-three move is `+48.20`. **The control fired because the registration named the wrong row**:
`−20.09` is `r7866`'s **parameters-held** move, while this profiler re-profiles the four parameters
at every sum and therefore computes `r7866`'s **other** row, `−48.20`. The error was in the
registration, not in the machinery.

And the registration was not short of the right figure. `−48.20` appears in `PREDICTION.md` itself,
just not in the lines that designate the control — so this was not missing information but a
misreading of which row this profiler computes, with both rows on the page.

The repair is not a loosened bar. The control is now read **out of `r7866`'s own record**
(`same_bins.json`) rather than typed into this revision, so the row cannot be mis-named again; and it
now checks **both crossings** (`68.1331` and `116.3351`) and not only their difference, which is
stricter than the registration asked for. A sign-convention arm states explicitly that `r7866` signs
these moves negative while this reads the crossing difference positive — the same quantity, opposite
convention, recorded rather than silently differing.

**What this therefore decomposes is the re-profiled move.** It says nothing about the
parameters-held `−20.09` move, which is a separate question and remains undecomposed.

## WHERE THE CARRYING BLOCK'S TWELVE SIT — NOT REGISTERED

Measured after the outcome was read, and reported as an observation rather than as a test.

`r7866` attempted the late ISW as a candidate mechanism and recorded it **UNREADABLE** on this mask:
the instrument has only `13` TT bins below the first peak, and no crossing is readable on them —
neither confirmed nor refuted. On `r7866`'s own criterion, read out of its source (`BIN_HI < 220`),
the recount reproduces that `13`.

Twelve of those thirteen are **exactly** the twelve `TT` bins this revision drops. None of the
dropped twelve lies outside the set; the one sub-peak bin left standing is `[208, 216]`.

So the block carrying `84` per cent of the low-end move is, bin for bin, where the one candidate
`r7866` could neither confirm nor refute lives. This **cannot** confirm that candidate — it is
unreadable on precisely these bins, which is `r7866`'s finding, not a gap in this one. What it does
is remove "unreadable" as a reason to set the candidate aside: the only mechanism that could not be
tested is the only one located where the move actually is.

The sub-peak set is `TT`'s by construction, so this comparison bears on the carrying block only
because the carrying block **is** `TT`. That clause is asserted in a gate rather than assumed, so a
re-measure that moved the lean to another block fires the gate instead of silently comparing two
different blocks.

## WHAT IS HONESTLY STILL OPEN

A block is not a mechanism. This names where the move lives and rules out the difference map as the
way to read it; it does not say what in `TT`'s twelve lowest bandpowers does the work. The next step
is a mechanism readable on bins whose crossing the instrument cannot resolve — which is the same
obstruction `r7866` hit, now with its location pinned rather than its candidate list open.
