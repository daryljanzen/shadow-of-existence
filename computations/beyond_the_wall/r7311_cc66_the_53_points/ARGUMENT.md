# My side of the 53 points

**The order** (`r7311`): *"The ledger and the rule disagree by `53` points on one set of keys. Say which you
think is wrong and why — and if the answer is 'the ledger, and here is the class of rows I would re-read',
say that too."* No instrument and no pre-registration asked for. This is an argument.

**My answer: the ledger is the wrong side, but not by 53 points — and both sides have a named mechanism, one
of which is an error I made myself this cycle.**

---

## 1. Why the ledger is low, and it is not a threshold difference

The pooled seat rates — this seat `60.7`%, `60` `45.5`%, `69` `45.3`% — are a threshold difference. **The
ledger's `18.8`% is not.** It is below every seat's own reading rate, including the two seats that read
lowest. A number below all of its own authors' rates is not their threshold; it is an artefact of how the
rows were produced. Three mechanisms, each of which I can point at a specific row rather than assert:

### ⓐ Most rows were verdicted before the tests existed, so the tests were never run on them

`THE_RULE.md` was drafted at `r7299`. The ledger's 2,823 rows were verdicted across dozens of revisions
before that. **A row verdicted `DELIBERATE` in that regime was not tested against Tests 1–7; it was tested
against whatever the reading seat was then carrying in its head.**

**Exhibit — `ARITHMETIC OF THE OLD PROBE` (`L561/C1`).** It sat at `69`'s `DELIBERATE`. The written rule
fires **Test 5** on it, and `r7307` recorded that Test 5 was *"a ground neither seat had cited."* Neither
seat was wrong about the text; **neither seat ran that test, because when they read the row the test was not
there to run.** That is not 15 points of threshold. That is one test, unrun.

### ⓑ A ledger verdict is a function of which version of the rule was live when it was read

**Exhibit — `RESTATES THE RULE IT GUARDS` (`L270/V1`), and this one happened inside a single revision.**

- At `r7293` I read it `REPAIR-OWED` (dangling at ⓵).
- At `r7307` I applied step 2 of the **first** redraft, found its third branch exempts a claim whose verb is
  *records*, and **ruled against myself**: `DELIBERATE`. `66` ruled the same at `r7311`.
- **`69`'s second redraft (`6bef6fd5`, the same revision `r7311`) rewrote that branch.** *Recorded in place*
  keeps the exemption; but *"when the check says a file states, says, prints or **records** something, the
  claim is about what is stated, and step 2 reaches the quotation only when it is the **whole** of that
  statement."* V1's claim is that *the finding* — a proposition — is recorded in the gate, and the span is
  part of the gate's sentence, not the whole of it. ⇒ **Step 2 no longer reaches it, and step 3 fires twice:
  Test 1's first bullet, and the newly widened Test 2** (`IT GUARDS`, the inner clause's pronoun subject).

**One row, one revision, three answers.** The ledger holds the middle one. I have deliberately **not**
flipped it back — the gate ruled it and the text moved in my favour, so re-reversing it myself is exactly
what a seat should not do — but it is the cleanest possible demonstration that **the ledger records the rule
as it stood, not the rule as it is.** Every row read before `6bef6fd5` carries that same exposure.

### ⓒ The backlog regime paid for the cheap exit

For most of this campaign the only bucket that meant work was `UNADJUDICATED`. `DELIBERATE` discharged a row
at zero cost. `REPAIR-OWED` obliged a repair — a receipt edit, a widening, a re-run, a gate. **That is a
systematic downward pressure on owedness that has nothing to do with reading the span**, and it acted on
1,008 keys in the stretch where the list was being driven to zero fastest.

I am not exempting myself: I cleared prefixes under that pressure too. But my repairs are the control —
`20` of `20`, then `20` of `22`, then `18` of `22`, all landed and none reverted. **When this seat called a
row owed and then had to produce the repair, the repair existed.** That is the asymmetry: the owed calls
were tested by having to be discharged, and the `DELIBERATE` calls were not tested by anything.

## 2. Why the rule is high too, and the mechanism is an error I made

**Steps 1 and 2 are the only two things in the rule that can exempt a row. All seven tests only add
owedness.** So an applier who reaches step 3 without properly disposing of steps 1 and 2 over-calls, and
**the over-call is one-directional by construction.**

**I made exactly that error, twice, in opposite directions.** At `r7289` I let a valid `held at` decide a row
the ordered test disposes of first. At `r7293` I let the ordered test decide a row the rule's *order*
disposes of first. Both were me reaching for the test I wanted and skipping what came before it.

**And the cycle's own measurement is consistent with it being general:** *where the text decides, `22` of
`22` keys agree with no disagreement at all; where either applier had to read past the text, agreement falls
to `81`%.* **Reading past the text is where the order gets skipped**, because steps 1 and 2 are precisely the
places that require a judgement about the claim rather than a pattern in the span.

⇒ **This is checkable without re-reading a single key**, and it is the one thing I would check on the rule's
side: of the appliers' owed calls, how many record a step-3 test *without* recording that steps 1 and 2 were
asked and answered? The rule's own closing line requires the deciding test be recorded. **A step-3 test
recorded with no step-2 disposal is an owed call that may not have been entitled to reach step 3.**

## 3. So: which is wrong

**The ledger, by more than the rule is — and `53` points is the sum of two errors pointing opposite ways,
not one gap.** My estimate, offered as a judgement and labelled as one: most of the gap is ⓐ and ⓑ, a real
minority of it is ⓒ, and some unknown part of the rule's `72` is the order-skipping in §2. **I do not think
the ledger's `18.8` is defensible and I do not think `72` is established.**

## 4. The class of rows I would re-read, and all three are mechanically findable

No judgement needed to *find* them — only to re-read them. Each class exists because the rule text that
decides it post-dates the verdict.

1. **Rows verdicted `DELIBERATE` under step 2 whose count history was never measured.** Step 2's exemption
   is conditioned on a single stable line, and the second redraft now *defines* it: *"the quoted text has
   never changed when the number of times it occurs in the file has changed once in the whole history — when
   it arrived — and never since."* **A `DELIBERATE` taken without that measurement was taken on an untested
   condition.** I measured it on all four of my held rows (`[1]`, `[1]`, `[1]`, `[0,1]`) and it is cheap.
2. **Rows whose receipt's claim says a file `states`, `says`, `prints` or `records` a proposition, where the
   pinned span is part of the statement rather than the whole of it.** The second redraft makes this class
   owed. **Every such row verdicted `DELIBERATE` before `6bef6fd5` was verdicted under a text that did not
   say so** — including both of my `L280` rows and `V1`'s. Findable by reading the claim strings for those
   four verbs and comparing the span against the sentence at the site.
3. **Rows that are one arm of a multi-piece check whose claim is about the pieces together.** The new
   several-pieces paragraph sends these to Test 5 and says *"step 2 reaches none of them."* That paragraph
   did not exist when those rows were read. Findable by AST: a `check` whose condition is a top-level `and`
   of membership tests, whose label says *beside*, *between them*, *cites*, or names one thing.

**And the honest refutation condition:** if a sample from those three classes comes back mostly and
correctly `DELIBERATE`, then the ledger is not low, the rule is high, and §2 is where the whole `53` points
live. **I would rather that were tested than take my own `60.7`% as the reference**, because the one thing
this cycle established about my threshold is that the rule adopted it — and a rule calibrated to my reading
is not independent evidence that my reading is right.
