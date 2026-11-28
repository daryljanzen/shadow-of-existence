# r7894 — REGISTER BEFORE THE DECOMPOSITION: does the lean's LOCATION survive a change of clock?

*Node `60`, on no order. Registered and pushed BEFORE any crossing is computed, because the whole
question is whether a location moves when the clock changes, and a bar chosen after seeing it move
would be worthless.*

## WHAT IS ALREADY KNOWN

`r7866` removed the thirty-six lowest bandpowers — twelve from each of `TT`, `TE`, `EE` — and read the
instrument's crossing two ways on the same bins:

| column | whole | minus thirty-six | move |
|---|---|---|---|
| **re-profiled** (the four parameters re-fitted at every sum) | `68.1331` | `116.3351` | `+48.2020` |
| **parameters-held** (the four frozen at the zero-sum fit, the reference's own treatment) | `57.0775` | `77.1644` | `+20.0868` |

`r7892` decomposed the **re-profiled** move and found it **additive** — the three single-block moves
summing to `+51.3224` against `+48.2020`, a residual of `6.5` per cent — and **concentrated**, with
`TT` carrying `84.4` per cent, `5.10×` `TE` and `15.15×` `EE`. It said explicitly that it decomposed
the re-profiled move and nothing else, and that the held move remained undecomposed.

⌗ **This is the standing `r7138` guard one level down.** That guard says: when two descriptions
differ, first ask whether the difference survives a change of clock — if it does it is content, if it
does not it was never a difference. `r7892` located the lean on ONE clock. The held column is the
other clock, and it is the reference's own treatment, so the question is not academic: if `TT`'s
dominance is an artefact of the freedom the instrument is given and the reference is not, then what
`r7892` located is partly that freedom rather than the data.

## THE MEASUREMENT

Exactly `r7892`'s construction with one substitution: at every mask, instead of re-fitting the four
parameters at each sum, evaluate `chi2_cmb` with the four **held** at the zero-sum fit on the whole
mask, which is how `r7866` built its frozen column. Five masks — the whole instrument, minus all
thirty-six, and minus each block's twelve in turn — and the crossing read on each.

⛔ **No fitting happens inside the scan.** The held parameter vector is read out of `r7866`'s banked
record and gated against a fresh fit, so the scan varies the MASK and nothing else.

## THE THREE OUTCOMES, FIXED NOW

Additivity is measured as in `r7892`: the three single-block moves summed against the all-three move,
**ADDITIVE** if the residual is under `10` per cent. Dominance: **CONCENTRATED** if one block carries
`≥ 80` per cent.

| | outcome | what it would mean |
|---|---|---|
| `Ⓦ⓵` | additive, and **`TT`** dominant | the location SURVIVES the change of clock — it is content, and `r7892`'s `TT` is the data's and not the freedom's |
| `Ⓦ⓶` | additive, and a **different block** dominant | the location does NOT survive — what `r7892` located is in part the profiling freedom, and the two clocks disagree about where the lean lives |
| `Ⓦ⓷` | **not additive** | the held move does not decompose by block at all, and the comparison `Ⓦ⓵`/`Ⓦ⓶` asks cannot be made on it |

⌗ **`Ⓦ⓷` is not exclusive with a dominance reading**, exactly as `r7892`'s pair were not: if the
residual exceeds the bar while one block still carries most of the move, BOTH are reported, and
`Ⓦ⓷` is the stronger statement because a sum that does not close makes the shares untrustworthy.

**The registered expectation is `Ⓦ⓵`.** The held and re-profiled moves have the same sign on the same
bins and differ by a factor of about `2.4`, which reads like one effect seen through two amounts of
freedom rather than two different effects. ⌗ *I expect to be wrong about this roughly as often as I
have been: `r7890` and `r7892` both refuted their own registered expectations, and both were more
useful for it.*

## THE CONTROL, AND IT IS READ OUT OF THE RECORD

The all-three held move must reproduce `r7866`'s banked frozen row: **both crossings** `57.0775` and
`77.1644` and the move `−20.0868`, to all digits and not merely nearby.

⛔ **Every one of those targets is read from `r7866`'s `same_bins.json`, not typed into this
revision, and the same for the held parameter vector.** This is not decoration: at `r7892` I typed a
row from memory, named the frozen row for a profiler that re-profiles, and the registered control
fired. The record is the only thing that cannot be misremembered.

⌗ **Sign convention, stated in advance:** `r7866` signs these moves negative; this reads the crossing
difference positive. Same quantity, opposite convention, and an arm asserts the reconciliation rather
than leaving it to be noticed.

## WHAT THIS WILL NOT DO

- It will not name a mechanism. A block is not a mechanism, and that was true at `r7892` too.
- It will not revisit the `12`-of-`13` overlap with the late-ISW candidate, which is banked at
  `r7892` as an unregistered observation and stays that way.
- No limit is read. `r7888`'s `193.545` meV is untouched, and the `Ⓡ⓵`/`Ⓡ⓶` fork is not reopened.
