# r7896 — REGISTER BEFORE THE SCAN: which of the four parameters absorbs the interference?

*Node `60`, on no order. Registered and pushed BEFORE any constrained fit is run, because the
question is which of four named things does something, and a bar chosen after seeing the four numbers
would be worthless.*

## WHAT IS ALREADY MEASURED

On `r7866`'s thirty-six lowest bandpowers, the block decomposition behaves differently on the two
clocks:

| clock | residual, as a fraction of the whole move | source |
|---|---|---|
| the four parameters RE-PROFILED at every sum | **`6.5` per cent** — additive | `r7892` |
| the four parameters HELD at the zero-sum fit | **`24.7` per cent** — NOT additive | `r7894` |

`r7894` concluded that **the four parameters, when free, absorb a cross-block interference**: `TT`
alone outruns all thirty-six together on the held clock, and removing `TE`'s and `EE`'s twelve on top
of `TT`'s partially cancels the move. With the parameters free to re-fit, that cancellation is
invisible. `r7894` said in its own record that it measures this on the held clock only, and that
whether the same structure survives PARTIAL freedom is the open question. This is that question.

## THE MEASUREMENT

The four are `H0`, `OM`, `WB`, `NS`. For each one in turn: **hold that one** at the zero-sum fit and
leave **the other three free** to re-fit at every sum. Then run `r7892`'s block decomposition — the
whole mask, minus all thirty-six, and minus each block's twelve — and read the residual.

⌗ The fitter is `r7866`'s, with one addition of this seat's own: a wrapper that minimises over the
FREE indices only, inserting the held value from the banked zero-sum vector. Same optimiser, same two
starting points projected onto the free subset. ⛔ Nothing of `r7866`'s or `r7892`'s machinery is
edited; the mask builder, the crossing reader and the profiler are imported.

For each parameter `p` define its **absorption share**

    share(p) = ( residual(hold p only) − 6.5% ) / ( 24.7% − 6.5% )

so `0` means holding `p` changes nothing from the all-free clock and `1` means holding `p` alone
reproduces the whole rise that holding all four produces.

## THE THREE OUTCOMES, FIXED NOW

| | outcome | bar |
|---|---|---|
| `Ⓧ⓵` | **CONCENTRATED** — one parameter does the absorbing | some `share(p) ≥ 0.5` |
| `Ⓧ⓶` | **DISTRIBUTED** — they do it together, no one of them alone | no `share(p) ≥ 0.5`, but the four shares sum to `≥ 0.5` |
| `Ⓧ⓷` | **JOINT AND NOT DECOMPOSABLE** — the rise needs them held together in a way no single hold reproduces | no `share(p) ≥ 0.5` and the shares sum to `< 0.5` |

⌗ `Ⓧ⓵` and `Ⓧ⓶` are exclusive by construction. `Ⓧ⓷` is exclusive with both. But **if two or more
parameters clear `0.5` the result is `Ⓧ⓵` and BOTH are named**, because two parameters each
reproducing most of the rise is itself a finding — it would mean the absorption is redundant across
them rather than owned by one.

⌗ **A share may come out NEGATIVE or above `1`**, and both are reportable rather than errors:
negative would mean holding that parameter makes the blocks *more* additive than leaving all four
free, and above `1` that one hold overshoots what four holds do. Neither is excluded in advance.

**The registered expectation is `Ⓧ⓵` with `H0`.** The grounds are weak and are stated as weak:
`r7872` found the basin for a different quantity to be "in `H0` alone behind a barrier", and `H0` is
the parameter with the most leverage over the low-multipole region the thirty-six sit in. ⌗ *That is
an argument from a neighbouring measurement, not from this one, which is exactly the kind of
expectation this seat has had refuted three revisions running — `r7890`, `r7892` and `r7894` each
refuted their own, and each was more useful for it.*

## THE CONTROL, READ OUT OF THE RECORD

Two controls, and both targets are read from the banked records rather than typed:

1. **Freeing all four** must reproduce `r7892`'s residual from `by_block.json` — the all-free clock.
2. **Holding all four** must reproduce `r7894`'s residual from `held_by_block.json` — the all-held
   clock, which is also the denominator of every share.

⛔ If either control misses, the shares are not computed at all, because a share is a position
between two numbers and means nothing if either end is wrong. ⌗ *At `r7892` a row typed from memory
fired the registered control; at `r7894` the repair held, with the held vector gated against a fresh
fit at exactly zero deviation. The same discipline applies here, and the denominator makes it
load-bearing rather than decorative.*

## WHAT THIS WILL NOT DO

- It will not name a physical mechanism. Which parameter absorbs an interference is a fact about the
  fit's freedom, not about the sky.
- It will not revisit where the lean lives. `r7894` established that the location is `TT` on both
  clocks and that is not reopened.
- No limit is read. `r7888`'s `193.545` meV is untouched and the `Ⓡ⓵`/`Ⓡ⓶` fork is not reopened.
- It says nothing about freeing TWO and holding two, which is a larger scan this does not attempt.
