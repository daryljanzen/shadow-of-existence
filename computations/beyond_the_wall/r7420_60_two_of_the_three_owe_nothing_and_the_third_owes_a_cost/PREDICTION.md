# r7420 (60) — TWO OF THE THREE OWE NOTHING, AND THE THIRD OWES A COST — registered before the scan

**Registered at this commit, before the scan is run.** `r7415` ③'s next standing item names three
receipts — `S56`, `S12`, `S7` — and does **not** say what they owe. The framing it inherits is `r7385`'s:
*"`S55`'s two keys and `S56`'s two keys and two missing annotations ... adjudicate each with its reason."*
⇒ ***That framing is stale, and deriving the live state rather than inheriting it is the whole point of
this revision*** — which is `r7418`'s own finding applied to an order instead of a comment.

## ⌗ THE LIVE STATE — A DIRECT READ, AND EXPLICITLY NOT AN ARM

Measured before registering, so a band here would be theatre:

| receipt | exit | failing gates | wall, alone | carry entry |
|---|---|---|---|---|
| `S7` | `0` | `0` | seconds | **none** |
| `S12` | `0` | `0` | **`269` s** | **none** |
| `S56` | `0` | `0` | **`425` s** | ⛔ **`tolerance`, on `main`, since `r7411`** |

⇒ ***Nothing is red in any of the three, and the adjudication backlog the order's framing points at is
discharged*** — the quote-pin ledger stands at `2,727` against `2,727` with `0` unadjudicated, and the
prose-pin ratchet at `0` against a ceiling of `0`. **Two thirds of the item is answered by reporting it.**

## ⛔ THE ONE LIVE THING, AND WHY THE `r7412` REMEDY IS NOT AVAILABLE

The trunk's tolerance carry has filed `S56` **unmeasured** — *no gate list, which is the kill signature
`r7412` named* — since `964fef0a` (`r7411`), four orders back. `S56` is **not** declared in
`scripts/run_all_receipts.py`'s `LONG`, so the tolerance sweep's limit for it is
`2 × max(900, budget(f, 600))` = **`1800` s**. It measures **`424.9` s** and **`429.4` s** on two local
builds differing in thread count — *`1` per cent apart* — and the sweep retries serially before filing a
timeout, so the runner exceeded `1800` s **twice**.

⛔ ***And a budget declaration — the remedy that cleared `S54` and `S55` at `r7412` — is forbidden here by
the sweep's own instruction***, in its own words: *not by lengthening the budget, because **"that would
record a pass that the parallel pass does not have."*** ⇒ **So the only remedy the instruments permit is
to make the receipt cheaper.**

## The arms

### ⒜ WHERE THE `425` s GOES — the share in the single most expensive section

`S56`'s wall time attributed to its most expensive measurable section, as a percentage of the whole.

- central **60** per cent, band **20–95**, two-sided.
- *Reasoning*: this seat has **not** profiled it, which is why this is an arm and the table above is not.
  A receipt of this family typically spends its cost in one place — a `git` sweep or an imported
  computation's `main()` — so a figure near the middle means one reducible site. **Below `20` means the
  cost is spread and there is nothing to cut**, which is the outcome that would send this back as
  *irreducible* rather than repaired.

### ⒝ THE REDUCTION MUST NOT MOVE A VERDICT — point prediction

Gates of `S56` whose verdict changes between the current form and the reduced one.

- **exact `0`**, point prediction.
- *Reasoning*: registered because a cost reduction that moves a verdict is not a reduction, it is a
  different receipt. `r7406`'s standing rule in its cheapest form: the remedy is run against the claim it
  is supposed to preserve. **Any non-zero figure kills the repair outright.**

### ⒞ THE RUNNER FACTOR — A BOUND, AND REPORTED AS UNMEASURABLE BEYOND IT

The ratio of the runner's cost for `S56` to this container's is **bounded below at `1800 / 425 = 4.2×`**
by the two timeouts. ⚠ *The figure itself cannot be measured from here, and asserting one would be the
move `r7374` corrected and `r7418` finished correcting.* **So it is registered as a bound and nothing
more**, per `r7415` ①: a measurement that cannot be made is reported as unmeasurable rather than forced.

### ⒟ WHO ELSE IS EXPOSED UNDER THAT BOUND — the census the bound licenses

This line's receipts whose **measured local cost × `4.2`** exceeds the limit that applies to them — the
`600` s suite cap, or their declared `LONG` budget where they have one.

- central **2**, band **0–10**, two-sided.
- *Reasoning*: **the floor is `1` and it is `S56` itself.** The `r7412` declarations were set by the house
  rule at measured × `1.7` — C63's measured contention spread — and `S54` at `1800` and `S55` at `2100`
  would both fall short of `4.2 ×` their measured costs. ⇒ *So the interesting outcome is whether the
  pair `r7412` just declared is exposed on the very factor this bound supplies*, which would say the house
  rule's multiplier is the defect rather than any one receipt's cost. **Above `10` says the rule needs
  restating before any further declaration, and that is a gate-layer decision rather than this seat's.**

## What is not claimed

**Not that the runner is `4.2×` slower than this container** — that is a lower bound forced by two
timeouts, not a measurement, and the container is not the instrument for what the runner has (`r7371` ②
as narrowed). **Not that `S54`'s and `S55`'s declarations are wrong**: both dropped out of the suite carry
after `r7412`, so `1.7` sufficed for the suite; `⒟` asks only whether the same figures survive the
tolerance job's limit, which is a different limit. **Not that the three receipts were never red** — the
order's framing was correct when written; what is claimed is that it is stale now, with the ledger figures
above as the evidence. **And not that `S56`'s cost is reducible**: that is `⒜`'s question, and a spread
cost is a reportable answer rather than a failure to repair.

Written r7420 on `r7415` ③'s standing queue. Stated for reversal.
