# r7894 — the location survives the change of clock; the additivity does not

`r7892` decomposed `r7866`'s **re-profiled** low-end move and found it additive and `TT`'s. This
decomposes the **parameters-held** move on the same thirty-six bins — the reference's own treatment,
the other clock — and asks the standing `r7138` question: does the difference survive?

## WHAT WAS REGISTERED

`PREDICTION.md`, committed and pushed before any crossing was computed, fixed three outcomes with
additivity at a `10` per cent residual and dominance at `80` per cent:

| | outcome | meaning |
|---|---|---|
| `Ⓦ⓵` | additive, `TT` dominant | the location survives — it is content |
| `Ⓦ⓶` | additive, another block dominant | the location does not survive |
| `Ⓦ⓷` | not additive | the held move does not decompose by block |

It stated that `Ⓦ⓷` is **not exclusive** with a dominance reading, and that where both fire `Ⓦ⓷` is
the stronger statement. The registered expectation was **`Ⓦ⓵`**.

## WHAT WAS MEASURED

| mask | crossing (meV) | move | share of the whole move |
|---|---|---|---|
| the whole instrument | `57.0775` | — | — |
| minus all thirty-six | `77.1644` | `+20.0868` | `100` per cent |
| minus `TT`'s twelve | `78.4487` | `+21.3711` | **`106.4` per cent** |
| minus `TE`'s twelve | `60.4823` | `+3.4048` | `17.0` per cent |
| minus `EE`'s twelve | `57.3479` | `+0.2703` | `1.3` per cent |

The three sum to `+25.0463` against the whole `+20.0868`: a residual of `4.9594` meV, **`24.7` per
cent**, well over the ten-per-cent bar.

### ⇒ `Ⓦ⓷`: NOT ADDITIVE — AND THE REGISTERED EXPECTATION IS REFUTED

`Ⓦ⓵` is **refuted**. The held move does not decompose additively. `TT` is still dominant and is
reported alongside, as the registration required, but `Ⓦ⓷` is the stronger reading and the shares
below the leading block are not to be trusted as shares.

**`TT` alone moves the crossing FURTHER than all thirty-six together** — `+21.3711` against
`+20.0868`. So removing `TE`'s and `EE`'s twelve *on top of* `TT`'s partially **cancels** the move.
That is a genuine interference between blocks, not a rounding residual: it is a quarter of the whole
move, and it has a sign.

## THE ANSWER TO THE QUESTION THIS REVISION ASKED

| block | re-profiled (`r7892`) | parameters-held (here) |
|---|---|---|
| `TT` | `84.4` per cent | `106.4` per cent |
| `TE` | `16.5` per cent | `17.0` per cent |
| `EE` | `5.6` per cent | `1.3` per cent |
| residual | `6.5` per cent | **`24.7` per cent** |

⇒ **THE LOCATION SURVIVES THE CHANGE OF CLOCK AND THE ADDITIVITY DOES NOT.**

`TT` dominates on both clocks, and more strongly on the held one. By the `r7138` guard, the location
is **content**: `r7892`'s `TT` is the data's and not an artefact of the freedom the instrument is
given and the reference is not.

**The additivity is the artefact.** With the four parameters free to re-fit at every sum, the blocks
decompose cleanly — a `6.5` per cent residual. With them held, they interfere — `24.7` per cent. So
the profiling freedom was **absorbing the cross-block interference**, and `r7892`'s clean
decomposition was clean because of it. ⌗ *That is worth saying plainly: `r7892`'s additivity was a
true measurement of its own column and a misleading guide to the data, and only the second clock
shows which.*

## THE CONTROL

The all-three held move reproduces `r7866`'s banked frozen row exactly: `57.0775` and `77.1644` to
four decimals, the move `20.0868` in magnitude, and the bin counts `555` and `519`. **Both crossings
are checked, not merely their difference**, so a pair of errors cancelling in the difference could
not pass.

Every target — both crossings, the move, and the held parameter vector itself — was read out of
`r7866`'s `same_bins.json` rather than typed here. The held vector is also gated against a fresh
zero-sum fit on the whole mask, which reproduces it with a maximum deviation of **exactly zero**, so
the record is the fit and not a stale copy of one.

⌗ **Sign convention:** `r7866` signs these moves negative; this reads the crossing difference
positive. The same quantity, opposite convention, asserted rather than left to be noticed.

## WHAT IS NOT CLAIMED

- **No mechanism.** A block is not a mechanism, and naming the interference is not explaining it.
  What in `TT`'s twelve lowest bandpowers does the work is still unknown, and now there is a second
  unknown beside it: what the four parameters absorb when they are free.
- The `12`-of-`13` overlap with the late-ISW candidate stays where `r7892` put it — banked as an
  unregistered observation, not a test.
- No limit is read. `r7888`'s `193.545` meV is untouched and the `Ⓡ⓵`/`Ⓡ⓶` fork is not reopened.
- The interference is measured on the held clock only. Whether it has the same structure under
  partial freedom — some parameters free, some held — is a further question this does not open.
