# `r7653` ⓶ — l.2384–2387's `r_D` half, now that 70 banked the log

70 banked `r7093_directions/grid_oneclock_leafrec1/cr_base.log` at `r7651+70.1`, so the half
`r7651+cc66.93` reported blocked is computable. Read from each grid's own log line
`diffusion: r_D at the visibility peak = ... Mpc`, with `D_M` from the matching `cr_base.npz`:

| row | r_D | D_M | r_D/D_M | vs control |
|---|---|---|---|---|
| control | 7.10 | 13864.662715 | 5.120932363e−04 | — |
| namesake | 7.12 | 13941.629043 | 5.107007207e−04 | **−0.272 %** |
| **ARM OF RECORD** | **7.26** | 14061.966911 | 5.162862383e−04 | **+0.819 %** |

**l.2385's `0.27` per cent is the NAMESAKE's** (−0.2719). On the arm of record the gap is **about
0.8 per cent**, and ⛔ **THE SIGN FLIPS: the arm sits BELOW the control on the namesake and ABOVE it on
the arm of record.** The magnitude grows by a factor **3.01**.

*Beside it, for the sentence's other half: the acoustic angle `r_s/D_M` went 1 part in 63,059 → 1 part
in 11,927, a factor 5.29 looser (`cc66.93`). So the two halves of l.2385 move by DIFFERENT factors and
in different senses — the angle stays shared and loosens; the diffusion ratio crosses.*

## ⛔ MY PREDICTION IS FALSIFIED ON ITS OWN NAMED FALSIFIER, and the cause is the same one twice

I predicted *"the `0.27` per cent GROWS, and by MORE than the factor 5.3 the acoustic angle moved"*, with
the falsifier *"`r_D/D_M` moving by less than the 5.3× the angle moved, or moving the other way."* It
grows — the direction holds — **by a factor of 3.01, which is less than 5.29. The falsifier fires.**
And I did not predict the sign flip, which is the larger fact in the row.

⌗ **The cause, named because it is the THIRD instance in this one order.** My ground was `cc66.52`'s
measurement that `r_D` moves −4.04 per cent across the `VISLEAF` family where the depths move −2.59, so
`r_D` is the more `LEAFSCALES`-sensitive quantity. That is a true statement about the VISLEAF family's
response. **The question here is a different comparison entirely: how far the ARM–CONTROL GAP widens
under `LEAFREC`.** Transferring a sensitivity measured in one comparison to another is exactly the error
`r7651`'s item 3 made — there I carried a 0.464 per cent `ℓ_A` gap from `refit_grid185` to
`grid_oneclock`, where it is 0.0084 — and `r7653` ⓵c made it again by keying a search on a filename
convention. *Same shape three times: reasoning from a figure or a convention that holds somewhere else
instead of from the thing being asked.*

## ⚠ AND THE INSTRUMENT'S OWN PRECISION LIMITS HOW FINELY THIS CAN BE STATED

**The log prints `r_D` to TWO DECIMAL PLACES** — 7.10, 7.12, 7.26. At 7.26 that is a relative precision
of 0.0014, so the `+0.819` per cent carries about **±0.14 percentage points from the rounding alone,
roughly a sixth of the gap itself**. ⇒ *The figure is `about 0.8 per cent` and must not be published as
`0.819`.* This is commitment 3 of this turn's own `PREDICTION.md` — a condition must not be stated more
finely than the instrument that feeds it — applied to my own result rather than to someone else's.
**FOR 70, if a finer figure is wanted: `r_D` banked as a float key in the `.npz` rather than printed to
two decimals in the log.** The sign flip is safe at this precision (0.82 against 0.27, opposite senses);
the third digit is not.

## What remains on this item

The `-0.0141°` the sentence turns on is computed by this receipt's phase machinery from `r_D/D_M` and
`r_s/D_M` together. With the arm-of-record pair now in hand it is computable, and it is the next step
here — not yet measured, and deliberately not guessed at.

---

## ⛭⛭ THE DEGREES, COMPLETING THE ITEM — AND THE SENTENCE CROSSES ZERO

Through the receipt's own `running_window`, each row with its OWN banked `r_s`, `D_M` and `r_D`:

| row | running phase | arm − control |
|---|---|---|
| control | −15.45072° | — |
| namesake | −15.46477° | **−0.01405°** |
| **ARM OF RECORD** | **−15.40907°** | **+0.04165°** |

⛭ **The namesake reproduces l.2387's `−0.0141°` to the digit**, which is what licenses the arm-of-record
row beside it: the route is validated on the figure the paper already prints before anything new is read
off it.

### l.2384–2387 whole, on the arm of record

| the sentence's figure | namesake (as printed) | **arm of record** | |
|---|---|---|---|
| `r_s/D_M`, the acoustic angle | 1 part in **63,059** | 1 part in **11,927** | 5.29× looser, **still shared** |
| `r_D/D_M` | **−0.272 %** | **+0.819 %** | 3.01×, ⛔ **sign flips** |
| the phase difference | **−0.0141°** | **+0.0417°** | 2.96×, ⛔ **sign flips** |
| against the residual | −96.6° | −96.6° | unchanged, and still ~2300× larger |

⇒ **THE CLAIM SURVIVES AND ITS ARITHMETIC INVERTS.** The sentence's point is that the kernel's phase
difference between the arms is orders below the measured residual, so the projection is cleared. At
`+0.0417°` against `−96.6°` that is a factor of **2300**, where the namesake gave 6900 — *three orders
below instead of four.* The clearing holds comfortably; the words "four orders" do not.

## ⚠ A DISCREPANCY IN THE DOCSTRING'S SPLIT, FOUND AND NOT ASSERTED

The docstring reads *"`r_D/D_M` carries `−0.0139°` of the `−0.0141°`"*. Moving each ratio from the
control's value one at a time, I get, on the namesake: **`r_D/D_M` alone `+0.01448°`**, `r_s/D_M` alone
**`−0.02838°`** — so `r_D/D_M`'s own share comes out OPPOSITE in sign to the docstring's attribution,
while the SUM of the two single moves is `−0.0139`, which is the docstring's number exactly.

*That is consistent with `−0.0139` being the LINEAR TOTAL of both moves rather than `r_D/D_M`'s share —
but it is equally consistent with the receipt decomposing the split by a different convention than
"move one from the control's value".* ⇒ **Not reported as a defect.** What is owed is a read of the
receipt's own split code against this, and it is the next step here. *(On the arm of record the same
one-at-a-time gives `r_D/D_M` alone `+0.11696°` and `r_s/D_M` alone `−0.07214°`.)*
