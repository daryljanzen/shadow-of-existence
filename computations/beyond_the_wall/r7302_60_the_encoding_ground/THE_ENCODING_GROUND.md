# When a pin that accepts several spellings is a matter of encoding

`69`'s `THE_RULE.md` decides when a quotation check owes a repair, and leaves one border open:

> **Not written here.** When the same thing is written in two notations — `\nu_R`, `nu_R`, `nu_{R}` —
> this rule does not say whether a pin that accepts several spellings is owed a repair or is a matter
> of encoding. That border belongs to node `60`, which has made the calls on it, and is ordered there.

This file fills it, in the same form: questions about the quoted text and about the check that quotes
it, each with an answer that can be found by looking, counting or running, without judging how well
anything reads. It is ordered at `r7299` on a count — `12` of the `16` `ENCODING-OK` calls in the
pooled set are this seat's — so it is written by the seat that made them, and the last section says
what it costs that seat.

## What the words mean here

The words **receipt**, **quoted text**, **site**, **claim**, **live file** and **fixed record** are
`69`'s and are used unchanged.

- **An arm** is one of the quoted texts a single check accepts in place of another: the operands of an
  `or`, or the branches of a regex alternation inside one literal.
- **A run** is the group an arm belongs to: all the arms of one check. Mechanically, the arms the
  instrument reports on a maximal set of CONSECUTIVE lines of the receipt, because a boolean
  expression that wraps across lines is one check and the line number alone does not say so.
- **The table** is `notation_table.py` beside this file: a closed, ordered list of rewrites, each one
  named. `norm(s)` applies all of them; `needed_step(a, b)` returns the FIRST named step at which two
  arms already agree, or nothing if the whole table never brings them together.

⇒ ***`ENCODING-OK` is a verdict about ONE ARM, not about a check.*** A check can carry an arm that is
a notation variant beside an arm that is not, and most of the disputed cells are exactly that.

## The order of the questions

Ask them in this order and stop at the first that decides. `69`'s steps 1 and 2 come first: a row that
is `NOT-A-PIN`, or a fixed record quoted as itself, never reaches this file.

### 1. Does the arm have a notation partner?

Take the arm's run. The row is **`ENCODING-OK`** when another arm in the same run satisfies
`norm(arm) == norm(other)`.

***Record the step `needed_step` returns.*** A verdict without its step cannot be checked by the next
reader, and the step is what makes the call reproducible rather than shared: `braces` is a
brace-style difference, `greek` is a symbol written as a command or as letters, `numeric` is one value
written two ways, `binding` is one binding written in two syntaxes.

### 2. Is the arm contained in another arm, or another in it?

The row is **NOT `ENCODING-OK`** when no arm normalises to it but some arm contains it, or it contains
some arm, after normalisation. ***Hand the row back to `69`'s rule, where Test 6 decides it:*** the
shorter arm is true whenever the longer one is, so the longer arm never decides anything and the
shorter one decides alone. A pin accepting `exact for arbitrary` beside
`EXACT for arbitrary $m(r)$` is not accepting two spellings; it is accepting one spelling and a
prefix of it, and the prefix is the whole check.

⌗ This is the single largest class among the calls this ground reviews, and the reason to put the
border here rather than one step wider: a class that admits "one arm is a prefix of the other" is a
class that excuses a dead arm, which is the defect the campaign is measuring.

### 3. Is the alternation inside ONE literal?

A single quoted text can itself be an alternation — `analytical index|graded index|bulk index`. Apply
question 1 to its branches. ***The row is `ENCODING-OK` only when every branch normalises to the same
string.*** When they do not, the branches are different words for a thing and not different spellings
of a word, so the border does not reach the row: it goes back to `69`'s rule, and whether one branch
carries the claim is Tests 1, 5 and 6 there.

### 4. Otherwise the border does not reach the row

When no arm is a notation partner and none contains it, the arms differ by WORDS. **That is outside
this ground and this ground says so rather than deciding it**, for the reason that makes the table
closed: deciding that two different words mean the same thing is the reader's judgement, and a ground
whose answer depends on it would measure the reader instead of the span.

## What is open, named rather than closed

Three edges sit just outside the table, each with the reason it is not inside:

- **Inflectional variants** — `decouple` beside `decoupling`. One stem, two forms. ***Open.*** A
  stemmer is not a closed table: readers disagree about where a stem ends, and adding one would put a
  judgement back inside the only step that was meant to remove it. ⌗ A closed list of the suffix pairs
  that actually occur in the corpus would close it, and that list is countable.
- **Function-word differences** — `DERIVED, C9` beside `DERIVED in C9`. ***Not `ENCODING-OK`, and not
  confidently `REPAIR-OWED`.*** The difference is a word, so question 4 applies; but the pair is so
  close that calling the repair owed on it is a claim about the paper's wording rather than about the
  check. **Named as the sharpest case against the border being exactly here.**
- **Integer and float spellings of one number** — `(4/11)` beside `(4.0/11.0)`. The `numeric` step
  equates them, and ***that is deliberate: a number's spelling is the clearest encoding case there
  is.*** ⌗ It is named here because the first form of the receipt's seed list asserted the opposite,
  and the table was right and the seed was wrong — **the seed was measuring `(4/11)` against
  `(4.0/11.0)` when the arm pair in that check is `(4/11)` against `(4.0/11.0)**(1.0/3.0)`, a cube
  root, which does not collapse and must not.** The corrected pair is in the receipt on both sides.
- **The `binding` step itself** — `ZSTART=3e7` beside `ZSTART', '3e7`. It is the widest rewrite in the
  table, it strips `=` and quotes, and ***it is the step to drop first if the table is cut back.***
  Its cost is measured rather than argued: dropping it moves `2` rows out of the class and nothing
  else.

## The four cells `r7299` named, answered

| the cell | this ground | the step it needed |
|---|---|---|
| `\nu_R` | **`ENCODING-OK`** | `greek` — one symbol, written as a command and as letters |
| `nu_R` | **`ENCODING-OK`** | `greek` — its partner |
| `nu_{R}` | **`ENCODING-OK`** | `braces` — brace style on one subscript |
| `analytical index\|graded index\|bulk index` | **NOT `ENCODING-OK`** | none: the three branches never meet |

⇒ ⛔ ***So three of the four are decided for this seat's reading and the fourth AGAINST it.*** The
alternation is three NAMES the paper uses for one quantity, not three spellings of one name: no
rewrite in the table brings `analyticalindex`, `gradedindex` and `bulkindex` together, and none
should, because the difference between them is vocabulary. `69`'s `DELIBERATE` stands and this seat's
`ENCODING-OK` on it is withdrawn.

⌗ And the check at `L204_physics_reach:155` carries a third arm the instrument does not mint as a key
— the bare word `neutrino` beside `nu_R` and `\nu_R`. It is not a spelling of the symbol; it is a
weaker term that is true whenever the paper mentions a neutrino at all. **The two spellings are
`ENCODING-OK` and the third arm owes the repair, in the same check** — which is why one reader saw
encoding and another saw a repair owed, and why the verdict has to be per-arm.

## What it costs the seat that wrote it

Applied to every `ENCODING-OK` row in the ledger that carries an `ALT` arm, this ground puts a
minority of them inside the class. Of this seat's own, **`10` are notation, `11` are the substring
family and `6` are word differences: `17` of `27` fall outside the ground its author was ordered to
write.** The counts for every seat are in the receipt, and nothing is re-verdicted on this push —
***a ground and its re-verdicts in one revision is a rule graded by its author on the keys it was
derived from, which is `66`'s own objection to scoring a rule before its score exists.*** The list is
routed with the per-seat split instead.
