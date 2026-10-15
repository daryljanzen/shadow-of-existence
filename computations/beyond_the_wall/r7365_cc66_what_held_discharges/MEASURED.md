# `r7365+cc66.38` — what "held" discharges for the `80`: the clause reaches **`34`**, is **already discharged for the other `46`**, and for the `34` it cannot be discharged without the extractor minting the key — and the `11` were never in that path

*`r7365` ③: **"Say what would discharge the clause for those `80`. What the row needs is the statement
of what 'held' means for a pin the instrument cannot key — whether `80` rows HELD with a named reason
discharges the clause, or whether the clause requires the `11` unreachable ones to be reclassified
first. If your reading is that the clause cannot be discharged without an instrument change, say that
plainly."*** ⇒ **It is the third reading, and the reason is narrower than the question.**

## ① ⛭ THE CLAUSE IS ALREADY MECHANISED, SO ITS TRIGGER IS NOT A JUDGEMENT I SUPPLY

`PO-78`'s second discharge clause reads *"every pin whose claim is a sentence's MEANING rather than
its wording rewritten to what it is for, by its author."* **That clause is `check_quote_pins`'
`MEANING-HELD` verdict** (`r7251+70.2`, adopted `r7253`), and it is gated on five conditions:

| | |
|---|---|
| `H1` | the row names `held at <sha>` and it resolves |
| `H2` | that commit is an ancestor of `HEAD` |
| `H3` | the literal is present in what the key reads **there** |
| **`H4`** | **the tier is `SENTENCE` — `'H4 a TOKEN is not a meaning pin'`** |
| `H5` | the commit **changed the receipt** |

⌗ *And the gate states why `H5` is there: **"`H5` is what separates held from unread"** — `H1`–`H4`
alone pass a key stamped with `HEAD` that nobody read, because a green receipt's sentence is present
at `HEAD` by construction.*

⇒ ***So "held with a named reason" is not a thing to define: it is defined, it is gated, and the
clause's trigger is `H4`, which is the extractor's own `tier` field.***

## ② THE REACH, BY THE CLAUSE'S OWN TRIGGER

| of the `80` invisible genuine pins | | |
|---|---|---|
| **`H4` admits — `SENTENCE`** | **`34`** | `17` PAPER, `17` SOURCE |
| **`H4` refuses — `TOKEN`** | **`46`** | `9` PAPER, `32` SOURCE, `5` UNDECIDED |

⛭ **And the split is the INSTRUMENT'S, not the frozen file's.** *Re-derived through the hop's FOLLOW
on this tree, the tier the extractor emits agrees with the label frozen at `7db5db61c` on **`117` of
`117`**.*

⇒ ⒜ ***`46` of the `80` are discharged by the clause's trigger failing.*** *Their claim **is** the
wording — that is what `TOKEN` means — so the clause quantified over sentences never reached them.
Nothing is owed for them: not performed, not held, outside. **That is a discharge of `46` rows by
reading the clause, and it costs nothing.*** ⒝ *The clause's real reach is `34`.*

## ③ ⛔ AND FOR THE `34` THE CLAUSE CANNOT BE DISCHARGED, BECAUSE A VERDICT NEEDS A ROW AND A ROW NEEDS A KEY

*Saying it plainly, as ③ invites. **The obstruction is not the definition of "held" and not the reading
— it is the ledger's key.***

| the live ledger as the gate reads it | |
|---|---|
| live keys | `2629` |
| baseline rows | `2629` |
| baseline rows NOT live — **STALE** fails | **`0`** |
| live keys with no row — **NEW-KEY** fails | **`0`** |
| of the `80`, minted by the extractor | **`0`** |
| of the `80`, carrying a baseline row | **`0`** |

***The ledger is exactly saturated.*** *`check_quote_pins` ⓵ fails on a key the instrument reports
with no row, and fails on a baseline row whose key the instrument does not report —
`gone = [k for k in base if k not in live]`.*

⇒ ⛔ ***Writing a `MEANING-HELD` row for any of the `34` takes STALE from `0` to `1`, and the gate is
red on it the same run*** — not because the verdict is wrong but because **an adjudication whose key
the instrument does not mint describes nothing**, which is the exact defect the stale rule exists to
catch. *A row cannot be the vehicle for a verdict about a key that does not exist.*

⇒ ⛭ **So the instrument change the clause waits on is the narrow one and it is nameable: THE EXTRACTOR
MUST MINT THE KEY.** *Nothing else about the clause is missing — the verdict exists, the conditions
exist, the readings are `34` and each has an author. `r7341`'s hop was **a** route to minting them and
it died on its own held-out test; the clause's discharge waits on a minting route, not on a rewrite.*

⌗ ⛭ **And the obstruction is NOT that these pins are hard to read.** *`23` of the `34` sit in receipts
the ledger already carries rows for — **the files are covered and the keys are not.** So what the
clause asks for is not reading nobody has done; it is `34` readings with nowhere to be recorded.*

## ④ ⛔ THE `11` ARE NOT THE OBSTRUCTION, AND RECLASSIFYING THEM IS THE ONE MOVE `r7351` ④ CLOSED

*③'s second option was *"whether the clause requires the `11` unreachable ones to be reclassified
first."* **No, and they were never in that path.***

*The `13` and the `11` priced the **hop**: `13` keys no stated container rule excludes, `11` of them
because the trace names nothing to test. They are the precision cost of a ROUTE, measured against a
bar, on a test whose declaration and labels were frozen and scored once.* ⇒ **`r7351` ④ forbids
re-scoring it by name — *"re-scoring a frozen test against a bar changed after seeing the score is
precisely what the freeze exists to prevent"*** — *and a reclassification of the `11` is that
re-scoring under another name.*

⌗ *The `11` and the `23`-of-`34` above are **different elevens and different populations**, and I am
saying so because the coincidence invites exactly the conflation this file is against: the `11` are
non-pins the container rule keeps with an empty narrow trace; the `11` of the `34` are genuine
SENTENCE pins whose receipt carries no ledger row at all.*

## ⑤ ⛔ AND ONE ERROR OF MINE, CAUGHT IN THE MEASURING

*My first ledger-coverage pass keyed the baseline by its **raw literal column**, where the gate does
`json.loads` on it. It reported **`2628` stale and `2628` new-key on a ledger that is exactly
saturated*** — the gate read as maximally broken at the moment it is exactly green.

⇒ *Caught because the number is absurd on its face: `2628` of `2629` wrong in **both** directions is
not a ledger state, it is a key mismatch. The corrected keying is in `clause_reach.py` with the reason
at the site.*

⌗ ⛔ **This is the third time this phase I have measured the ledger with a key the ledger does not
use** — `.29`'s two hand-typed baseline keys (a glyph, a collapsed whitespace run), `.37` ⒠'s
substring test where the instrument keys an AST constant, and now raw text where the gate keys JSON.
***The class is one thing and it is not carelessness about typing: it is that I keep re-deriving a key
instead of asking the instrument that owns it for the key it uses.***

## ⑥ WHAT IS HERE

`clause_reach.py` (the measurement; the frozen population and labels read at `7db5db61c` exactly as
`r7355`'s `relimit.py` reads them, the hop's FOLLOW from the committed `follow_patch.py`),
`clause_reach.txt` (the run).

*The one faithfulness check is stated in the script and binding: the follow must surface all `117`.
It surfaces `117`, and the tier agrees on `117` of `117`.*
