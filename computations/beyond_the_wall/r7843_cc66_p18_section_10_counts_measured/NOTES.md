# NOTES — r7843+cc66.1

## The method, and why the provenance hunt was the whole job

The order's ① says to read the convention *off the sentence and its section*. What actually
settled four of the six was **finding where each figure came from**:

- the environments → the retired document's `196 formal environments`
- the hard register → the harvest's `roughly seventy-four hard-tagged results`, whose own entry
  names `the register-tag census` as its source

**A convention I inferred would have been an imposition dressed as a measurement.** A
convention whose figure the document's own ancestor printed is the author's. That distinction
is the difference between this revision and a plausible-sounding rewrite, and it is why the
hunt for provenance mattered more than the counting, which was easy.

## ⛔ Guards this revision earned

### ⓵ Having a number is not having the right number

Prediction ③ put the environment count at 250–290, on the strength of **my own previous
revision's measurement** of "263 spine environments". That figure was counting **Lean
declarations**. The sentence means **LaTeX environments**. Different object, same word.

The live Lean tree, measured here: **410** declarations outside `probes/`, and **50,054**
inside it, because `probes/` is vendored. So "263" was not even a stable reading of the object
it was measuring.

⇒ **Guard: a figure carried forward from your own earlier revision is an input like any other,
and needs its subject checked before it is used as a prior.** I trusted it because I had
produced it.

### ⓶ The backslash-absent presence class, hit a SECOND time — one revision after I wrote the guard for it

`check_paper_pins_present` read this receipt's hard-register pattern absent from every paper,
because it carried literal spaces and no backslash, so the test's `hit` fell back to a plain
`in` test. **This is identical to `r7841+cc66.1`, where I found it on two patterns, fixed both
with `\s`, and wrote it up in NOTES.**

⇒ **Guard: a guard recorded as a note about past instances is not yet a guard.** It has to live
in the habit of writing the next instance. This one is now recorded **in the baseline row
itself**, where the next person writing a PAPER pin will meet it.

### ⓷ A receipt that reads the paper through a glob cannot be classified

Every sentence pin came back target **`UNDECIDED`** — a target this baseline has never carried
in 3031 rows — because the receipt read P18 out of a glob-built dict. The pin operator traces a
literal to the file the receipt **opens**, and through a glob it cannot.

**And fixing that exposed a defect the dict had hidden:** reading the file as it now stands made
an arm fail, because **this revision's own edit to P18** put a convention phrase after
"receipt-anchored" and the pattern ended at the full stop. *The receipt had stopped parsing the
sentence it had just annotated.*

⇒ **Guard: open the paper by its path, and re-run the receipt after editing the paper it reads.**
Editing the subject and the instrument in one revision means the instrument must be re-run
against the edited subject, not against the state it was written for.

### ⓸ And a figure retyped inside the arm written to catch retyping

`Ⓑ⑥` asserted the without-remarks count as **116** when the computed value is **118** — a
scratch count that had also dropped `principle`. In the arm whose whole purpose is to hold the
competing convention's figure.

### ⓹ An order's verb can carry a structural requirement

③ said *pin each at the printed precision*. In this corpus "pinned" is defined by
`check_figures_pinned`, whose site definition is *"every `\rcpt{X}` in a non-appendix paper"*.
So the word **pin** required P18 to gain a `\rcpt` site, and therefore its first receipts
appendix, and therefore a change to two range limits that both deliberately stopped at P17.

⇒ **Guard: when an order uses a word the corpus has defined in a gate, read the gate's
definition before choosing an implementation.** I nearly satisfied "cite the receipt" with a
parenthetical, which would have left the figure unpinned by the only instrument that measures
pinning.

## What this revision does NOT settle

- **That these conventions are the author's intent.** For two there is provenance and for two
  the figures are exact, but intent is a reading and no gate checks a reading.
- **The two unmeasurable counts.** They stay 69's. The honest options are to leave them as
  prose, to register their subjects so they *become* countable, or to drop them from a sentence
  that insists the register is a count.
- **Whether P18 should carry a receipts appendix at all.** Implemented because the order's
  "pin" requires it; flagged as reversible because it changes what `r7841` established about
  P18's character.
