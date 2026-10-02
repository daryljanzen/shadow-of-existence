---
kind: PREREGISTRATION
---
# `LABEL-PIN` — pre-registration, `r7129+cc66.99` (node 66, code seat)

***Written and committed BEFORE the operator is run on the tree***, as `r7129` ordered and as `70`
pre-registered `QUOTE-PIN` at `r7125+70.1`. *The prediction's misses are the part worth having.*

## ⛔ THE CLASS

**A `check`/`gate` call whose LABEL and whose CONDITION assert opposite things.**

*Every operator in this family so far keys on the **expression**: `PROSE-PIN` on counted matches,
`TILT` on whether a pin moves with its data, `REGRID` on whether a window is finer than its abscissa,
`QUOTE-PIN` on a literal from a sentence another seat owns.* ⇒ **None of them reads the label, so none
of them can see this.** *It took a per-site human read of `L204` to find three.*

⌗ *Why it survives: **a passing check with a confident label is the least likely thing in a corpus to
be read twice.** The label is what a reader believes; the condition is what the gate enforces; and
nothing compares them.*

## ⚑ THE RECALL SET — FOUR REAL INSTANCES, ALL FOUND BY HAND AT `r7125+cc66.98`

| # | receipt | the label says | the condition asserts |
|---|---|---|---|
| ⓵ | `P10_the_neff_commitment_...` | *"ADOPTED IN CODE AND **STATED IN NO PAPER**"* | `len(re.findall('Neff', allp)) > 0` — that it **is** present |
| ⓶ | `P10_the_neff_commitment_...` | *"the **unnamed** adoption is what hides it"* | the name **is** present |
| ⓷ | `P4_the_corpus_identifies_...` | *"NOW while "Higgs" still appears **ZERO** times"* | `> 0`. **Measured 4** |
| ⓸ | `P10_the_neff_commitment_...` | *a specific tally — "`4x` ... does not use the other spellings"* | `n >= 0`, **true of every count** |

*⓸ is a related kind rather than the same one — a label that names a measurement against a condition
that asserts **nothing** — and it is in the set because it is why ⓵ and ⓶ survived in the same file.*

⇒ **The operator must flag all four on their parent blobs, or it has not found the class it is for.**

## ⛔⛔ THE CENTRAL RISK, STATED BEFORE MEASURING: **THE NAIVE SIGNAL IS MOSTLY FALSE POSITIVES HERE**

*The obvious signal is an absence word in the label — `ZERO`, `no`, `never`, `not`, `absent`,
`nowhere` — against a condition asserting presence or a positive count.* ⛔ ***In THIS corpus that
signal fires on the commonest legitimate idiom there is.***

*I verdicted **sixteen** of them at `r7125+cc66.98`: the regression guard on an absence that ENDED.*

| | label | condition | verdict |
|---|---|---|---|
| ⛔ *defect* | *"X still appears **ZERO** times"* | `> 0` | **contradiction** |
| ✔ *correct* | *"X is **NO LONGER at zero** — the absence ENDED at `c54.205`"* | `> 0` | *the count **is** the claim* |

⇒ ***Both contain `zero`. The discriminator is the POLARITY OPERATOR around the absence word*** —
`no longer`, `is not`, `ENDED`, `now`, `where it was`, `at ZERO when this receipt was written`,
`supplied at` — *and an operator without a negation-of-the-absence detector will flag the whole
regression-guard family and be useless.*

⌗ **So the design is two-stage: absence word present, AND no negation-of-absence within the label.**
*I expect the second stage to be where the operator is wrong, in both directions.*

## ⚑ THE POPULATION PREDICTION — reasoned before the run, and about what the GATE will count

⌗ ***Reported as distinct `(receipt, label, condition)` keys, which is what a gate would count — NOT
file lines.*** *That distinction is this seat's own finding from `r7125+cc66.98`: the prose-pin baseline
file held `159` rows for `149` keys, and `r7129` records that this seat's order was sized from the file.*

| | prediction |
|---|---|
| receipts with at least one absence-word label | **$120$–$220$** *of ~$950$* |
| sites the NAIVE one-stage signal flags | **$150$–$400$** |
| sites surviving the negation filter | ⚑ **$12$–$40$** |
| of those, TRUE contradictions on a read | ⚑ **$4$–$12$** |
| ⇒ precision of the two-stage operator | **$20$–$40$ per cent** |

***The load-bearing prediction is the last row and it is deliberately low.*** *`QUOTE-PIN` opened at
`2{,}287` and `PROSE-PIN` at `149` because both key on syntax. **This class is semantic, so I expect a
small true population and a poor precision**, and I would rather say so now than discover it.

⛔ ***And the specific way I expect to be WRONG:*** *the three found instances are all in `L204`, the
**survey** family — receipts whose subject IS what the corpus says and does not say. **If the class is
really a property of survey receipts rather than of the corpus, the operator will find almost nothing
outside `L204` and the honest conclusion is that it is not gate-grade.*** *I am predicting
**$0$–$3$ true instances outside `L204`**, and if that is what comes back the operator reports and is
not enforced — the same call `70` made for `REGRID`, whose one live finding was mine.

## ⌗ WHAT IT CANNOT SEE, STATED BEFORE IT RUNS

- **A label that is wrong without being opposite** — stale figures, superseded prose. *Most rot is this,
  and this operator is blind to all of it.*
- **An f-string label whose absence word arrives at runtime** from a variable. *Static only.*
- **A condition whose polarity is indirect** — a helper returning a negated bool, a flag read from
  elsewhere. *One level of trace at most.*
- **The judgement itself.** *`"X is no longer at zero"` is a correct label and `"X still appears zero
  times"` is not, and no regex settles which a sentence is. **Every survivor needs a human read**; the
  operator's job is to make the candidate set small enough that reading them is affordable.*

⌗ *If the true population is at the bottom of the range, the finding is that this class is real,
**hand-found, and not mechanizable at useful precision** — which is a result and is reported as one.*
