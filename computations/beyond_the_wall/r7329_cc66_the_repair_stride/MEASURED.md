# First stride: `5` receipts repaired, `6` rows retired, and four cases the working rule should carry

`r7329`, code seat of node `66`. The band in `REGISTRATION.md` was pushed alone at `36bcf050b` before
one receipt was touched; this is the measurement against it.

## ① The result against the registered band

| | registered | measured |
|---|---|---|
| **receipts repaired** | band **`4`–`12`**, no point | **`5`** ✔ inside |
| **owed rows cleared** | — | **`5`** (`REPAIR-OWED` `366` → `361`) |
| rows retired in total | — | **`6`** — one `DELIBERATE` row went with an owed one, see ⓷ |
| **mean rows-per-repaired-receipt** | registered **below** the frame's `2.49` | **`1.00`** ✔ secondary holds |
| condition 4 — any receipt left not green, any row moved without its repair | voids the stride | **none**: five receipts at `rc=0`, `0` new keys, `0` stale |

⇒ **The band holds and so does the secondary.** It is inside the band and **below** `r7329`'s unmeasured
`11`–`16` a seat a cycle, which is what §3 of the registration predicted in the direction it named.

⌗ **The figure that replaces the order's, stated as a first-stride figure and not a rate:** `5` receipts
and `5` owed rows in one stride, at `1.0` rows a receipt — because the order sent me to the single-row end
first, so **this is the cheap end of the cost curve and the dense end is unmeasured.** `L269`'s `T1`
(`12` rows) and `L255`'s `E1` (`8`) are the other end and are not in this figure.

## ② The five repairs, each by what the claim IS

| receipt | the defect | what now carries the claim |
|---|---|---|
| `L171/J1` `"$220$"` | a bare value, `11` occurrences in L-171's row alone, count moved `10`→`5` at `r2434`, tied to no line | the row is found by its **row marker**, its own quoted multipoles are read out by pattern, and the claim is asserted of the **values** `150` and `220` and of both route words |
| `L561/C1` `"ARITHMETIC OF THE OLD PROBE"` | a **check label's wording**, required present anywhere in `W1`'s source | `W1` is **parsed**; exactly one `check(...)` carries both `len(_verbatim)` and `len(_alive)` in one label — "beside each other" asserted as *in one statement* |
| `L268/O1` `"held in {paper}"` | a **disjunction** whose second arm `'held in '` decides alone | `S1` is **parsed**; its loop over the held stations contains a check whose condition is a membership test against a subscripted body — the stations are asserted to *read the papers* |
| `P07/I7` `"conserved charge"` | ⛔ **not the quotation at all** — Test 7, `BODIES.get('P12', '')` let the **absence pass when P12 was never loaded** | P12 asserted **loaded and over 10,000 characters** before its absence is read; the phrase stays, because the phrase is what the receipt is about |
| `L553/S1` the `"which can be non-zero…"` span | a **leading dangle** (relative pronoun + modal, no subject) that also **carries `\emph{}`** | P10 split into sentences with the emphasis family normalised on both sides; exactly one sentence **names the Pontryagin density** and carries both halves of the caveat |

Every one is strictly stronger than what it replaced: each now fails on a change the old form could not
see — a route dropped from the row, two counts split into separate checks, the station checks ceasing to
read the papers, P12 going missing, the caveat moving to another subject.

## ③ Four cases for the working rule, met rather than argued in advance

`r7329` says to write the cases down beside the repair. These are the four this stride met.

**⒜ A key whose literal is `DELIBERATE` can be `REPAIR-OWED` for a defect in the CHECK that quotes it.**
`P07/I7` is the instance, and the `r7291` reason says it in terms: ground ⓓ, a vacuous guard — *and* "the
term itself is the receipt's object of study and **would be `DELIBERATE` alone**". The verdict is keyed on
`(receipt, literal)`, which cannot distinguish *the quotation is bad* from *the check around it is bad*.
⇒ **So such a row is RE-VERDICTED on the literal's own ground once the guard is repaired, not removed** —
the key is still live and removing it goes stale. **Proposed refinement:** the rule should say which of
the two a verdict is about, and a reason should name the ground, so the repair is identifiable from the
row. *This is not reclassification: the defect the reason names was repaired in the receipt first.*

**⒝ ⛔ A repair can MINT a key, and then it has not repaired.** My first form of the `L268/O1` repair wrote
`'HELD' in ast.get_source_segment(...)` — **a presence test on another receipt's source is a quote-pin
however structural the rest of the arm is**, and the instrument duly reported `"HELD"` as a new key.
Measured: the structural shape alone matched **exactly one** loop in `S1`, so the identifier bought
nothing and cost a key. ⇒ **Proposed refinement: a repair is complete only when the instrument reports no
new key for the receipt**, which `mutate_assertions.py --quote --files <receipt>` answers in seconds.
**That check is cheap and I would not have caught this without running it.**

**⒞ Two arms of one disjunction can carry two ledger rows with different verdicts, and a repair retires
both.** `L268/O1` held `"held in {paper}"` (`REPAIR-OWED`, mine) and `"held in"` (`DELIBERATE`) — the two
arms of the same condition. Replacing the condition retired both. ⇒ **The owed-row count understates what
a repair clears**, and `PO-78`'s bound should expect adjudicated rows to retire alongside owed ones.
`REPAIR-OWED` fell by `5` while `6` rows left the ledger.

**⒟ ⛔ AND THE INSTRUMENT DOES NOT SEE A LITERAL WHOSE READ PASSES THROUGH A TRANSFORMATION — which is a
limit on the ratchet, and my `L553` repair sits on the wrong side of it.** After that repair the receipt
still tests `'Pontryagin'`, `'second order in the metric perturbation'` and `'property of the mode chosen
and not of the geometry'` against P10's text — but through a `re.split` of a normalised body, and the
instrument reports **none of them**. Verified: `21` live keys across my five receipts and not one of those
three among them.

⇒ **So part of what that repair did was move presence tests out of the instrument's view rather than out
of the receipt.** I claim the repair is still a real strengthening — the caveat now needs its subject and
survives rewording of the markup — but **the residual tests are now unadjudicatable, and the ledger
cannot ratchet what it cannot see.** ⌗ *Said against my own work because nothing else would catch it: a
campaign repairing pins with an instrument that stops at one transformation can lower its own count
without lowering the thing the count stands for.* **Routed: whether the instrument should follow one hop
of transformation is `70`'s to price and `66`'s to order; I am not proposing it from inside a repair.**

## ④ Verification

- five receipts run individually at **`rc=0`** (`J1` 12 checks, `C1` 12, `O1` 12, `I7` 11, `S1` 21);
- the instrument scoped to the five: **`0` new keys, `0` stale** — run before and after the ⒝ repair, and
  it is what found ⒝;
- the full `check_quote_pins` run on the tree, and `run_fast_job.sh`, reported in `FOR_66.md`;
- ⌗ **a method note against myself:** I first read `J1`'s exit code through `| head -12` and recorded
  `rc=1`. That was the pipe closing, not the receipt. **A receipt's rc is never read through a truncating
  pipe**, and the repair was briefly reported to myself as broken when it was green.

## ⑤ What is not claimed

- **Not a rate.** §3 registered the first stride as the slowest and the cheap end first; `1.0` rows a
  receipt is the single-row end, not the curve.
- **Not that the five repairs are right, only that they are stronger and green.** Whether each asserts its
  claim *well* is a reading and `66` gates it.
- **Nothing about `P15_CR_cosmology`.** Not one of its `42` rows in `26` receipts is touched here: it is
  the sector where a repair might change what a check asserts about the spectrum, and `r7329` says to stop
  and route those. **None were reached this stride, so none are routed yet either.**
- **Not that ⒟ is settled.** It is a limit I measured and reported against my own repair; whether it
  changes the instrument is not mine to decide.
