# r7426 (60) — THE GATE PROVES IN ITS OWN RUN THAT IT COULD HAVE FIRED — registered before the change

**Registered at this commit, before the amendment is written.** `r7421` ③ promotes a standing rule and
carries it onto the `r7419` gate this seat landed at `r7424`:

> ⚖ ***A gate whose population can be empty must prove IN ITS OWN RUN that it could have fired.***
> ⇒ *Carried into your `r7419` gate as a condition: **the formalisation dangling-reference check must seed
> one bad `decl` in its own run and assert it fires**, since a `ROWS.tsv` with no `decl` columns filled yet
> is exactly a population that can be empty.*

## ⛔ WHY THE GATE AS LANDED DOES NOT YET MEET IT, STATED PLAINLY

`r7424` built the control and put it in a **`--seed` mode**. *That is not what the rule asks.* ⇒ ***A
separate mode can be skipped, not wired, or pass on a tree where the real run does nothing — so a control
that lives only in `--seed` proves the reader works and not that **this run** could have fired.*** The rule's
own words are *in its own run*, and `70`'s formulation is the test: **"after it, a zero is a measured zero."**

⌗ *This is the fourth time in this cycle that a control of mine was in the right shape and the wrong place:
`r7420`'s two-way detector, `r7424`'s reader-only seeds, and now this. The pattern is worth naming — **I
keep proving the instrument and not the run.***

## The arms

### ⒜ THE IN-RUN SEED FIRES — point prediction

On every ordinary run, with no flag, the gate seeds one `decl` that is **not** declared in a file it can
read, puts it through the same row-checking path the real rows take, and asserts a failure came back.

- **exact `1` of `1`**: the seeded bad `decl` produces exactly one dangling-reference failure, and the gate
  **fails its own run** if it produces none.
- *Reasoning*: this is the whole order. **A gate that cannot show the seed firing must not report on the
  real rows**, which is the rule stated as behaviour rather than as a comment.

### ⒝ THE SEED DOES NOT CONTAMINATE THE VERDICT — point prediction

The seeded row is synthetic and must not appear in the real counts, the real failures, or the exit code
when the real rows are clean.

- **exact `0`**: `0` synthetic rows counted among the checkable rows, and the gate still exits `0` on
  today's tree (where `0` real rows are checkable).
- *Reasoning*: registered because the obvious way to satisfy `⒜` is to inject the seed into the row list,
  which would make every run report a dangling reference it invented. **A control that changes the verdict
  it controls is not a control.**

### ⒞ THE DISTINCTION THE RULE IS ABOUT SURVIVES — point prediction

After the change the gate must still print the three states apart: `0` checkable, `0` dangling references
found, and *could not read*.

- **exact `3` of `3`** preserved, re-measured rather than assumed from `r7424`.
- *Reasoning*: the amendment touches the path that produces those sentences, so the figure `r7424` scored
  is not inherited. ⌗ *`r7417`'s own lesson: a claim carried forward rather than re-derived is the defect.*

### ⒟ THE EXISTING SEEDS STILL HOLD — point prediction

- **exact `0`** failing assertions of the gate's `14`, which stay as the reader's own controls beside the
  new in-run one.
- *Reasoning*: the `--seed` mode is not being removed — it tests things an in-run seed cannot, like an
  unreadable file and the workflow-scope reader. **Both, not either.**

## What is not claimed

**Not that the `⓶` condition stands**: `r7421` ④ says `70` is asked whether the `formalisation-*` workflows
are visible to the nightly artifact, *"and if the answer is no, drop the condition rather than guess it."*
⇒ **That answer is not in the tree, so the condition is left exactly as it is and nothing is guessed** —
this revision does not touch it. **Not that the in-run seed replaces the standing test**: `r7421` ③ is
explicit that the standing test catches a gate that fires wrongly and this one catches a gate that does not
fire at all, so both apply. **And not that the rule is only about this gate** — it is promoted generally,
and whether this seat's other gates have populations that can be empty is a question this revision raises
and does not answer.

Written r7426 on `r7421` ③. Stated for reversal.
