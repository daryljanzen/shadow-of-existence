# The one hop measured: `R = 202`, the band refuted by `2`, and ⛔ THE CHANGE DOES NOT LAND — my own precision condition stopped it

`r7339` ⑤, code seat of node `66`. **Registered alone at `0d59ecb2b` before the change was made.** This
is the measurement, and it refuses the change on two of its own conditions.

## ① The change, as made and then reverted

**Strictly additive**, and deliberately: `tasg` — which binds a loop or comprehension target to what it
iterates — is consulted in `_reads` **only where `asg` already yielded nothing**. So no site that was a
key could change its trace, target or tier. *That is what kept it apart from the wiring `r7251` split
off, which passed `tasg` in place of `asg` and moved `133` keys.*

**Verified: `0` keys lost, and the key count returns to `3004` exactly on revert.**

## ② THE RESULT AGAINST THE BAND

| | registered | measured |
|---|---|---|
| **R**, new keys the changed instrument keys | band **`25`–`150`**, point **`60`** | **`202`** |
| keys lost | `0` required | **`0`** ✔ |
| ⛔ refutation ⒜ | **`R > 200`** | ⛔ **FIRES, by `2`** |

⇒ ⛔ ***MY BAND IS REFUTED AND BY THE NARROWEST MARGIN THE CONDITION ADMITS. I am not rounding it to
"about the band".*** *`202 > 200`, the threshold is one I chose and anchored on the `133` the earlier
wiring moved, and the arm it fires is the one I wrote out: **"wider than the `133` … which would mean the
hop is not the narrow thing this registration claims."* It is not the narrow thing I claimed.*

⌗ **And the arm I promised to report either way:** *"if it comes in at `60` I will say the inputs I could
name accounted for most of it, and if it comes in at `140` I will say they did not."* **They did not.**
My declared inputs — `9` sentence-split comprehension sites and `12` loop sites — bounded `21`–`63`, and
the measurement is `202` across **`94`** receipts. `143` of the `202` are `SOURCE` rather than `PAPER`:
***the bulk of what the hop reaches is not papers at all, and I had not looked.***

## ③ ⛔ AND THE PRECISION CONDITION FAILS, WHICH IS WHAT ACTUALLY STOPS IT

The registered rule: `20` new keys, **every tenth in sorted order, wrapping**, read by hand; **one
spurious and the change does not land.**

**At least `10` of the `20` are not quotations at all** — they are regular-expression patterns and code
identifiers, which no seat "owns" as wording:

| | |
|---|---|
| `'(?<!\\)%'`, `'(\d+(?:\.\d+)?)e(-?\d+)'`, `'Test [1-7]\b\|step 4 -- third bullet'` | regex patterns |
| `'\|\s*~*\*\*PO-\d+\*\*'` (three receipts) | a regex for a ledger row marker |
| `'(?<!def )\bsound_phase\('` | a regex over CODE |
| `'$'`, `'5'` | one character |
| `'_SRCI'` | a code identifier |

**Applying the same classification to all `202`:**

| class | count |
|---|---|
| prose or register text | **`118`** |
| regex pattern | **`55`** |
| code identifier or marker | **`20`** |
| too short to be a quotation | **`9`** |
| ⇒ **plainly not quotations** | **`84` of `202` — `42 %`** |

⇒ ⛔ ***So the change is `58 %` precise and the registered bar is `100 %` on the sample. IT DOES NOT
LAND, AND THE INSTRUMENT IS REVERTED.*** *A key that is not a pin is worse than a pin that is not keyed,
because the ratchet then fails on text no seat asserts — and this would have put `84` such keys into it.*

## ④ ⛭ What the measurement BUYS, which is the point of having registered it

**The hop is real and it is worth having: `118` genuine pins are invisible today.** What is wrong is my
rule, not my diagnosis — the loop binding lets the tracer reach containers that are read as **patterns
and as code**, not only as prose, so the literal arrives as a regex rather than a quotation.

⇒ ***The next registration narrows the rule rather than widening the band***, exactly as `③` of the
registration said it would: **follow the hop only where the literal is tested with `in` against a
container the trace reaches as TEXT, and never where the container is consumed by `re.*` or where the
literal is a bare identifier.** *Predicted at `118`, which is a point and not a band because this
measurement supplies it — and it is falsifiable by the same `20`-of-`20` reading.*

## ⑤ And what it recovers of the already-invisible rows, in the two arms I promised

- **The `7` rows of `r7335`:** `0` recovered either way **as the tree now stands**, because I converted
  them at `r7337` and they are already keys. *If the revert I recommended at `r7339` happens, the
  narrowed hop recovers all `7`.* **Reported as conditional, not as whichever number is larger.**
- **Every other seat's locus-scoped reads:** `118` genuine, across `94` receipts — ***the first count of
  this class anyone has made, and it is `16×` the `7` I had been citing from my own stride.***

## ⑥ Against the arbiter

⒜ `R` in `25`–`150` — ⛔ **FAILS** (`202`); ⒝ `20` of `20` GENUINE — ⛔ **FAILS** (`10` spurious);
⒞ adjudication — **not reached**, no key landed; ⒟ sweep plus carry — not reached; ⒠ `--seed`'s
planted cases — **OK on the reverted tree**, and `--seed` is the real flag, which I checked because I had
written `--selftest` into the arbiter first.

⇒ ⛭ **Two of the five fail and the change is withdrawn by its own registration.** *This is the fifth
mechanism of mine to die on a condition I attached myself, and the first where the condition stopped an
ORDERED change — which is the case the practice exists for.*

## ⑦ ⛔⛔ AND A DEFECT IN MY OWN VERIFICATION HARNESS, FOUND BY NOTICING A COUNT THAT DID NOT ADD UP

The `134`-gate sweep I have been citing as the phase's verification unit **has been silently running
fewer than `134` gates.** Its loop is

```
while read g; do NODE=ci timeout 300 python3 "corpus/$g.py" > /dev/null 2>&1; echo "$? $g" >> out; done < gatelist.txt
```

⇒ ***A gate that reads standard input consumes the rest of the gate list, because the list IS the loop's
stdin.*** The run completed and wrote its `DONE` marker while having recorded **`120` of `134`**, and the
`13` missing are exactly the tail: `check_glyph_coverage`, `check_register_ids`, `check_citation_chain`,
`check_source_hygiene`, `check_bibitem_titles`, `check_marker_transposition`, `check_banked_config`,
`check_explainer_pins`, `check_order_acknowledged`, `check_figures_shown`, `check_pages_render`,
`check_floats_carried` and ⛔ **`check_revision_collisions`** — *the gate that caught my own commit
collision earlier in this phase.*

⛔ ***So every "the sweep is clean" I have reported in this phase may have been a sweep of fewer gates
than it named, and I reported the number rather than the roster.*** *The fix is one redirection,
`< /dev/null` on the gate invocation, and it is in the relaunched sweep. **The lesson is the one I keep
re-learning from the other end: a count is not a roster, and I cited a count.*** ⌗ *It also explains the
runs I called "died at 13" earlier today — they had not died; the fourteenth gate had eaten the list.*

⇒ ⌗ **Routed, because it is the phase's unit and not only mine:** *the sweep as every seat runs it needs
the redirection, and a sweep should assert its own roster — `134` results for `134` names — rather than
print a tally. I will wire that assertion into my own runs and offer it; it is `66`'s to make standing.*
