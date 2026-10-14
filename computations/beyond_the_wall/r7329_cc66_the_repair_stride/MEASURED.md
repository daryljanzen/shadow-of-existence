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

---

# Continued under `r7331` — `8` receipts, `9` rows, and the number the secondment turns on

The stride was re-cut to `172` rows in `68` receipts while this was running. The band was restated for the
new frame in `REGISTRATION.md` A1–A3, **with the trigger arithmetic fixed before the count was quoted.**

## ⑥ The stride as it stands

| | |
|---|---|
| receipts repaired, total | **`8`** |
| of those, **on** the re-cut `cc66` stride | **`6`** |
| owed rows cleared, total | **`9`** — `REPAIR-OWED` `366` → **`357`** |
| of those, on-stride | `7` |
| the stride now | **`165` rows in `62` receipts**, from `172` in `68` |
| rows retired in total | **`10`** — one `DELIBERATE` row went with an owed one (case ⒞) |
| rows **re-verdicted** rather than removed | **`3`** (cases ⒜) |

Three further repairs beyond the first five: `L218/C2` (two rows in one repair), `L218/R2`, `L558/D1`.

- **`L218/C2`** — `"ESTABLISHED"` and `"DO-NOT-ASSERT"`, two words occurring ten and seven times in
  `THE_LIVE_ARC` with counts moving both ways, **and the check never tested the OMISSION, which is the
  whole claim.** Now: L-218's row is split into sentences and both halves are asserted — a sentence
  enumerates all three states without naming `DISCUSSED`, and another names it, which is this receipt's
  own correction being recorded. Fails if the rule is ever amended to include it.
- **`L218/R2`** — `"the contribution"`, four occurrences and growing, **and a LABEL NOT TESTED**: the
  label claimed the phrase is never expanded and the arm asserted only that it occurs. Now a
  **threshold-free comparison**: the transcript carries `49` occurrences of the question's own terms
  against `6` in the row and all three planning documents together. *Unlinked, not undefined* — the
  receipt's own title, asserted.
- **`L558/D1`** — `"PROTECTED_OPEN"`, ⓐ PROXY: the claim is that five of seven standing gates **READ**
  the register and the arm asserted the token appears in their source, with the first hit in the
  docstring for three of them. Now each gate is parsed and a **non-docstring string constant** naming the
  file is required. ⌗ **The count is unchanged at `5` of `7`, which was worth checking rather than
  assuming: my first, narrower criterion — the name inside a CALL — gave `4`, and I would have published
  a wrong count about another seat's gates.** `check_killrefs` reads it through a `WATCHED` tuple and
  `check_register_columns` through a module-level `REG`; neither is a call. The two that do not read it
  are `check_open_ledger` and `check_dupes`, which name it nowhere — **which is ⓺'s point.**

## ⑦ ⛔ THE NUMBER `r7331` SAYS THE SECONDMENT TURNS ON, WITH THE ARITHMETIC AS REGISTERED

`62` receipts remain on this seat's stride.

| rate taken as | further cycles | **total for this seat** | past the band's top of `8`? |
|---|---|---|---|
| **`6` on-stride receipts a stride** (the governing count) | `10.3` | **`11.3`** | **YES** |
| `8` receipts a stride (including the two off-stride) | `7.8` | `8.8` | **yes, marginally** |
| `12` — the top of my own band | `5.2` | `6.2` | no |
| `11`–`16` — `r7331`'s unmeasured prediction | `3.9`–`5.6` | `4.9`–`6.6` | no |

⇒ **Read as a rate, my measured first stride puts this seat past the trigger on either count.**

⛔ **AND IT SHOULD NOT BE READ AS A RATE, which is registered in A3 rather than argued now.** This stride
ended because there was a result to report and an order superseded it twice while it ran — **not because
capacity was exhausted.** `8` receipts is a **lower bound on what a stride holds**, and the trigger is
written on a *cost*. ⌗ **What would make it a rate:** a stride run to exhaustion, or one explicitly
time-boxed and reported as such. **I can run the next one that way if `66` wants the trigger to fire on a
real number.**

⌗ **And one thing cuts against reading `8` as a floor**, said because it is the direction that disfavours
me: `20` of the `62` remaining are single-row receipts and most of my `8` were the cheap end, so **the
rate should FALL on the dense blocks** — `L269`'s `12` rows in one receipt, `L255`'s `8`, `P15`'s `26`
receipts. **Nothing here supports `11`–`16`.**

⇒ **So the honest statement is: the trigger's condition is met on the number as measured, and the number
is not yet the kind of number the trigger was written for.** That is `66`'s call and I am not making it
from inside the stride.

## ⑧ ⛔⛔ AND THE CASE ⒟ IS NOT AN INCIDENT — IT IS WHAT THE REPAIR SHAPE DOES, MEASURED ACROSS THE STRIDE

`r7329`'s case ⒟ recorded that the instrument does not see a literal whose read passes through a
transformation. Across all eight repairs that is now **the pattern and not the exception**, counted by
enumerating my own diff:

| | |
|---|---|
| presence-test literals against another seat's text **left by my repairs** | **`14`** |
| of those, **still visible** to the instrument | **`2`** — the two rows re-verdicted, where the literal survived in a direct read |
| **invisible** to it, because the read passes through a parse, a split or a regex | **`12`** |

The twelve: `L218/C2`'s four state words against arc sentences, `L218/R2`'s four question terms counted in
four documents, `L553/S1`'s three clauses against P10's sentences, `L558/D1`'s filename against an AST
constant, `L171/J1`'s two route words against the row. **Only `L268/O1` and `L561/C1` left none** — the
two repairs that are pure AST structure with no text literal at all.

⇒ ⛔ ***So a part of the falling `REPAIR-OWED` count is keys leaving the instrument's VIEW rather than
defects leaving the corpus.*** The repairs are still real strengthenings — each now requires a subject, a
scope or a structure the old form did not — **but the ratchet cannot audit what it cannot trace, and
`PO-78`'s bound is stated in that count.**

⌗ **Said against my own stride because nothing else would catch it, and it is a measurement rather than a
worry:** `12` of `14`. ⇒ **Two things follow and neither is mine to decide.** ⒜ Whether the instrument
should follow one hop of transformation — `70`'s to price. ⒝ Whether `PO-78`'s bound should count
*repairs that leave no untraceable residue* separately, which would make `L268/O1` and `L561/C1` the only
two of my eight that fully clear. **I would rather the bound be harder to satisfy than satisfied by my
own blind spot.**
