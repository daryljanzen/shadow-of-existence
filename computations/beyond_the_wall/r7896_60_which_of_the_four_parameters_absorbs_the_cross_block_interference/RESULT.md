# r7896 — the cross-block interference is the tilt's, and the tilt's alone

`r7892` found the low-end move's block decomposition **additive** at a `6.5` per cent residual with
the instrument's four parameters re-profiled at every sum. `r7894` found the same decomposition
**not additive** at `24.7` per cent with them held at the zero-sum fit, and concluded that the four,
when free, absorb a cross-block interference the held clock exposes. It named the open question:
*which* of them does the absorbing. This answers it.

For each of `H0`, `OM`, `WB`, `NS` in turn: hold **that one** at the zero-sum fit, leave the other
three **free** to re-fit at every sum, and read the residual of the same decomposition — the whole
mask, minus all thirty-six, minus each block's lowest twelve.

## WHAT WAS REGISTERED

`PREDICTION.md`, committed and pushed before any constrained fit ran, defined each parameter's share
of the rise between the two banked ends,

    share(p) = ( residual(hold p only) − 6.5% ) / ( 24.7% − 6.5% )

and fixed three outcomes at a bar of `0.5`:

| | outcome | meaning |
|---|---|---|
| `Ⓧ⓵` | CONCENTRATED | some parameter's share reaches the bar |
| `Ⓧ⓶` | DISTRIBUTED | none alone reaches it, but the four together do |
| `Ⓧ⓷` | JOINT | none alone reaches it and the four together do not either |

It required that where two or more clear the bar the outcome is `Ⓧ⓵` and **both are named**, because
redundant absorption is itself a finding; and it declared in advance that a share below zero or
above one is **reported, not clipped**. The registered expectation was `Ⓧ⓵` with **`H0`**, on
grounds the registration itself called weak — `r7872`'s basin finding, which is about a different
quantity.

## THE TWO CONTROLS, AND WHY THEY GATE EVERYTHING

A share is a position between two numbers, so the registration withheld every share unless both ends
reproduced from the same code path that computes the arms. One fitter minimises over the **free
indices only**: freeing all four reduces it to `r7866`'s own `fit_x4` — same optimiser, same two
starting points projected onto the subset — and holding all four reduces it to a bare evaluation at
the banked vector, with no optimiser called. The arms are therefore not compared against a second
implementation that might agree for the wrong reason.

| control | measured | banked | from |
|---|---|---|---|
| all four free, residual | `6.47%` | `6.47%` | `r7892`'s record |
| all four held, residual | `24.69%` | `24.69%` | `r7894`'s record |
| all four free, move | `+48.2020` | `+48.2020` | `r7892`'s record |
| all four held, move | `+20.08685` | `+20.08685` | `r7894`'s record |

Both ends land exactly, on the residual **and** on the move.

## WHAT WAS MEASURED

| held | base | move, all 36 | `TT` | `TE` | `EE` | residual | share |
|---|---|---|---|---|---|---|---|
| none (control) | `68.1331` | `+48.2020` | `+40.6703` | `+7.9668` | `+2.6853` | `6.47%` | — |
| `H0` | `64.6741` | `+33.9461` | `+29.4864` | `+5.6133` | `+1.77875` | `8.64%` | `+0.119` |
| `OM` | `66.902045` | `+40.7737` | `+37.2821` | `+6.8201` | `+2.2393` | `13.655%` | `+0.394` |
| `WB` | `60.9505` | `+25.2133` | `+16.30745` | `+4.5487` | `+1.4393` | `11.57%` | `+0.280` |
| `NS` | `61.91914` | `+42.7261` | `+47.7113` | `+5.15305` | `+0.6110` | `25.16%` | `+1.026` |
| all four (control) | `57.0775` | `+20.08685` | `+21.37115` | `+3.4048` | `+0.27034` | `24.69%` | `1` |

### ⇒ `Ⓧ⓵`: CONCENTRATED IN `NS` — AND THE REGISTERED EXPECTATION IS REFUTED

Holding the spectral tilt alone, with the other three free to re-fit at every sum, reproduces the
**whole** of the non-additivity that holding all four produces: share `+1.026`. The registered
expectation was `H0`, and `H0` carries the **least** of the four, `+0.119`.

## THE SHARES ARE NOT A PARTITION, AND THE LABEL SAYS SO

They sum to `+1.819`. The word "share" is therefore one-to-many against the thing it names: each arm
frees three parameters that can substitute for one another, so the four arms overlap and their
numbers are **positions on an interval, not fractions of a whole**. `NS` exceeding one is the same
fact from the other side — one hold slightly overshoots what four holds do, because the three left
free in that arm are not the same three as in any other.

What the numbers do support is an ordering and a threshold, and only one parameter crosses it.

## THE SIGNATURE, AND WHEN IT APPEARS

`r7894` found the held clock's tell: `TT`'s own move **exceeds** the all-thirty-six move, so the
blocks cannot be adding. That tell tracks `NS` exactly:

| clock | `TT` | all 36 | `TT` outruns all 36? |
|---|---|---|---|
| all four free | `+40.6703` | `+48.2020` | no |
| `NS` held, three free | `+47.7113` | `+42.7261` | **yes** |
| all four held | `+21.37115` | `+20.08685` | **yes** |

It appears in precisely the configurations where the tilt is held, and in no other.

## THE CONVERSE — NOT REGISTERED, AND REPORTED AS SUCH

The registration asked which hold **breaks** additivity. It did not ask whether freeing that one
alone **restores** it, and a share above one makes the converse the sharper question, because
necessity and sufficiency are different claims and hold-one arms can only speak to the first. Four
further arms, hold three and free one, were run afterwards and are reported here as an unregistered
follow-on. They did not and cannot change the outcome above, which the registered arms fixed before
they ran.

| freed alone | base | move, all 36 | residual | additivity recovered |
|---|---|---|---|---|
| `H0` | `57.1865` | `+20.3504` | `25.32%` | `−0.035` |
| `OM` | `57.2726` | `+20.2923` | `25.28%` | `−0.032` |
| `WB` | `57.57235` | `+21.5928` | `25.45%` | `−0.042` |
| `NS` | `60.7231` | `+24.0614` | `9.2955%` | `+0.845` |

Freeing the tilt alone recovers `+0.845` of the rise. Freeing any one of the other three alone
recovers **nothing** — all three land slightly worse than holding everything. The two directions
name the same parameter, so the interference is the tilt's to absorb in both senses, and that is why
this revision states it without a hedge.

The other three barely move the base when freed alone: in the table above each of their bases sits
within a fraction of a meV of the all-held base, while freeing the tilt alone moves it more than
five times further than any of them. Once the tilt is pinned, the other three have almost no
freedom left to exercise at the low end.

## WHAT IS NOT CLAIMED

- Not that `NS` **causes** the lean. It absorbs the part of it that the block decomposition sees as
  interference. `r7892`'s located content and this absorption are different quantities.
- Not that the three non-tilt parameters are inert. They are nearly inert *in this measurement*,
  with the low twelve of each block dropped and the tilt held; `r7872` found a basin in `H0` for a
  different quantity, and nothing here touches that.
- Not that `+1.026` and `+0.845` should agree. They are computed on different arms over overlapping
  subsets, and the shares are not a partition; that they name the same parameter is the finding, not
  that they coincide numerically.
- Not a statement about any clock but the two banked ones. Every arm here holds its parameters at
  `r7866`'s zero-sum fit on the whole mask, and no other freezing point was tried.
