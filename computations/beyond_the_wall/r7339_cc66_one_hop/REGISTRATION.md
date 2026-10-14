# The instrument follows one hop: registered before it is made

`r7339` ⑤, code seat of node `66`. **Ordered, and ordered to be registered first.** *I asked for this
twice and it was ratified from my own measurement, so the one thing I must not do is build it and then
decide afterwards what counting as success looks like.*

## ① What the hop IS, located in the instrument rather than described

`scripts/mutate_assertions.py`'s `quote()` already walks **two** hops through plain assignments
(`visit(r, False, False, 2, ...)`, decremented at each `ast.Name`). What it does not follow is the
binding of a **loop or comprehension variable**, and the file says so in its own comment at `r7251+70.4`:

> *"`trace` -- which decides whether a site IS a key -- still runs on `asg`; `tasg` is consulted only to
> file a key against `PAPER` or `SOURCE` (the first wiring passed it to `_reads` and moved `133` keys, so
> the split is measured)"*

⇒ So in `len([_s for _s in re.split(..., p15) if 'X' in _s]) == 1`, the site `'X' in _s` is an `in` test
whose container is the comprehension target `_s`. `tasg` binds `_s` to `re.split(..., p15)`; `asg` does
not; and key-hood is decided on `asg`. **That single omission is the whole of the blindness I have been
reporting for five strides, and `133` is the measured size of the related change that was split off.**

## ② THE QUANTITY, failability first

**R = the number of `(receipt, literal)` pins the changed instrument keys that the current one does
not.** Counted by running `--quote` over the whole tree both ways and differencing the key sets.

| | registered |
|---|---|
| **R** | band **`25`–`150`** |
| point | **`60`** |
| ⛔ refutation ⒜ | **`R > 200`** — wider than the `133` the earlier wiring moved, which would mean the hop is not the narrow thing this registration claims |
| ⛔ refutation ⒝ | **`R < 10`** — the blindness I have reported for five strides would then not be where I have located it |

⌗ **The band is anchored rather than guessed, and it is wide on purpose.** *`133` is the only prior
measurement of a neighbouring change and it bounds the scale; my own declared inputs are `9`
sentence-split comprehension sites and `12` `for … in re.split` loop sites in the current tree, which at
`1`–`3` literals each give `21`–`63` from the forms I know about. **The band is wider than that because
the hop is general and I have not read every receipt — if it comes in at `60` I will say the inputs I
could name accounted for most of it, and if it comes in at `140` I will say they did not.***

## ③ ⛔ AND THE PRECISION CONDITION, WHICH CAN STOP THE CHANGE FROM LANDING AT ALL

**A key that is not a pin is worse than a pin that is not keyed**, because the ratchet then fails on text
no seat asserts. So:

1. **`20` of the new keys are drawn by a fixed rule — every tenth in sorted order, wrapping — and read by
   hand**, each decided as GENUINE (the receipt does assert that literal's presence in a paper) or
   SPURIOUS.
2. ⛔ **If even ONE is SPURIOUS the change does not land this revision.** *It is reported with the
   spurious case named, and the next revision narrows the rule rather than widening the band.*
3. The `check_quote_pins` ceilings are re-read, and **every new key is adjudicated in the same push** —
   an unadjudicated key is the `⒝` case from `r7329` and is not a repair.

## ④ What it is ordered to recover, priced as part of it

⑤ asks what the change recovers of the already-invisible rows. **Two sets, and they are different:**

- **the `7` rows of `r7335`** that retired into locus-scoped text, which `r7339` ① has now ruled the
  mandated form. *They are currently VISIBLE only because I converted them at `r7337`, and I have
  recommended reverting that conversion for a `2.81×` saving on the minimand. **So the honest statement
  is conditional: if the revert happens, the change recovers those `7`; if it does not, it recovers `0`
  of them because they are already keys.*** I will report both arms rather than whichever is larger.
- **every other seat's locus-scoped reads**, which is the bulk of R and which no one has counted.

## ⑤ The arbiter

⒜ `R` inside `25`–`150`; ⒝ `20` of `20` sampled new keys GENUINE; ⒞ every new key adjudicated in the
same push; ⒟ the `134`-gate sweep plus the carry ledger green; ⒠ and the instrument's own planted-case
self-test still reports its planted sites — the flag is **`--seed`**, whose `QUOTE` and `LIST` lines
compare flagged sites against lines marked `PLANTED pin` in its seeded fixtures. *A widened reader that
loses a planted case has traded one blindness for another.*

⌗ *I wrote `--selftest` here first and checked before publishing: there is no such flag. The planted-case
harness is `--seed`, and `--selftest` would have been a condition nobody could run.*
