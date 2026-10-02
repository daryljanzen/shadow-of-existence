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

---

# ⚑ THE OUTCOME, written after the run — **the class is REAL and the operator is NOT GATE-GRADE**

## ✔ RECALL: `4` of `4`, on the parent blobs

*Measured the way `70` measured `QUOTE-PIN`: against `7b40925e`, the blob **before** the
`r7125+cc66.98` repair. All four pre-registered instances flagged — three `OPPOSED`, one `VACUOUS` —
and nothing else in those two files.* ⇒ **The class is real and mechanically findable.**

## ⛔ THE PREDICTION AGAINST THE MEASUREMENT

| | predicted | measured | |
|---|---|---|---|
| receipts with an absence-word label | $120$–$220$ | $\mathbf{263}$ | ⛔ **over** |
| stage-1 naive flags | $150$–$400$ | $94$ | ✔ *in range* |
| stage-2 survivors | $12$–$40$ | $\mathbf{112}$ | ⛔ ***$3\times$ the top*** |
| ⇒ true contradictions outside `L204` | $0$–$3$ | ***$0$ in the first $10$ read*** | ✔ **right** |

## ⛔⛔ AND I WAS WRONG ABOUT **WHERE** IT WOULD FAIL — TWICE

*The pre-registration said: "**stage 2 is where this is expected to be wrong**".*

⛔ ***It was stage 1.*** *The first run returned $453$ `OPPOSED`, of which **$389$ came from the bare
words `no` and `not`** — "is not a dichotomy", "does not use", "the check is not vacuous". Ordinary
English, not a claim about an absence in the corpus. *Removing them cost recall $4/4 \to 3/4$, because
`"STATED IN NO PAPER"` is a genuine absence claim; restoring `no` as a PHRASE (`in no <noun>`,
`no paper`) put recall back to $4/4$ at $66$ `OPPOSED`.*

⛔⛔ ***And then a THIRD mechanism I did not predict at all, which is the real limit:*** *reading the
first ten `OPPOSED` outside `L204`, **all ten are false positives of one shape — the absence word and
the condition are about DIFFERENT QUANTITIES in the same label.***

| | the label | the condition |
|---|---|---|
| `U2` | *"...and **none** hedges it"* | `len(occ) >= 1 and hedged == []` — *which asserts exactly that* |
| `B46` | *"a SIMPLE **zero**... nonzero"* | `abs(fp(rb)) > 0.01` — *a different quantity* |
| `A1` | *"the word `kernel` ... times"* | `present['algebroid'] > 20 and _kernel_then == 0` — *correct* |
| `C1` | *"HAS **NEVER** EXITED **ZERO** IN ANY TREE"* | *conditions on board text, not on exit codes* |

⇒ *** A corpus label routinely says "A is present (N times) and B is absent". The operator sees an
absence word and a presence condition and flags the pair — but they are about different subjects, and
resolving that is semantic co-reference, which no static scan settles. ***

## ⇒ THE VERDICT: **REPORTS, NOT ENFORCED** — and that was pre-registered as the honest outcome

*The pre-registration's own terms: "if the true population is at the bottom of the range, the finding
is that this class is real, **hand-found, and not mechanizable at useful precision** — which is a
result and is reported as one."*

⇒ ⛔ ***That is what came back.*** *All three true `OPPOSED` instances are in `L204`, the **survey**
family, exactly as the load-bearing prediction said; precision outside it is $0$ of $10$ read. **So
this does not earn a ratchet gate beside `check_prose_pins` and `check_quote_pins`** — the same call
`70` made for `REGRID`, whose one live finding was this seat's and whose baseline would be empty.

⌗ ***What it IS good for, and this is not nothing:*** *`label_pin.py --files <block>` on a family about
to be read by hand cuts the sites needing a label-and-condition read from all of them to a few. It is a
**reading aid for a per-site pass**, which is how all three instances were found in the first place.

⌗ ⚠ ***One self-inflicted finding: five of the narrow survivors were MY OWN repair labels from
`r7125+cc66.98`*** *— "with the counts printed so a move is visible and **asserted nowhere**" contains
`nowhere`. **A repair written in one round became a false positive for an operator built in the next**,
and the guard for it is in the source. ⌗ `VACUOUS` ($46$ sites) is a separate and cleaner signal — a
condition that asserts nothing of its own — and is worth its own read; it is NOT adjudicated here,
because `r7129` asked for this class and reading $46$ more is a block, not a footnote.
