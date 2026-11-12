# `r7750` (60) — RESULT

**Order `r7747`:** (1) a cold read of `P9`'s two new formal paragraphs against `probes/Range.lean`;
(2) then the standing item — a cold read of `70`'s six experiment registrations, on which its
pilots are blocked.

`probe.py` carries part 1: **8 arms, 8 PASS**, full output in `runs/READINGS.txt`. Part 2 is a read
of six documents and is recorded here, with a verdict per count per experiment.

---

# PART 1 — `P9`'s TWO FORMAL PARAGRAPHS

Both located; all eight cited names are declarations and three fabricated names are not found.
**Everything the two paragraphs assert about the objects is true, recomputed from the metrics
rather than read off the prose or the Lean docstrings.**

* **The Kantowski–Sachs Einstein tensor**, computed from `−dτ² + X(τ)²dχ² + Y(τ)²dΩ²`: the paper's
  `eq:ksrho` and its two partners are exact, `G³₃ = G²₂`, and **all twelve off-diagonal components
  are identically zero** — residuals `0`, `0`, `0`, `0`.
* **Both named members are vacuum.** For `X = sinh τ`, `Y = cosh τ` at `Λ = 3`, all sixteen
  components of `G^μ_ν + Λδ^μ_ν` vanish; for the Nariai member `Y = 1/√Λ`, `X = e^{√Λ τ}` they
  vanish at every `Λ > 0`.
* **The pp-wave paragraph is exact and uses its biconditional correctly.** `R_uu = −½(H_xx + H_yy)`
  recomputed, the other fifteen components zero, `rn_pp_vacuum_iff` is an `↔` and the prose says
  *"vacuum exactly when"*. **And its witness is non-trivial**: `H = x² − y²` is harmonic without
  being the zero function — the opposite of `r7744 FINDING 4`'s defect.
* **The witness for the SdS branch is at `M = 0`, and the prose says so** — the risk disclosed
  rather than hidden.
* Both paragraphs name their unformalised remainder (the kernel's exhaustiveness; the Weyl
  invariants and type N).

**And the five-against-four count is right once what it ranges over is established.**
`rn_ks_sds_vacuum` carries five conditions and the prose lists four. The fifth is `Y'' = X'`, which
follows from `Y' = X` **by differentiation** — so the prose's four, read as holding on a region
(*"Wherever…"*), imply it, while the Lean states them pointwise and must list it. Not a dropped
hypothesis: a pointwise statement against a regional one, and the prose's word is the regional one.

## ⛔ FINDING — THE NON-DEGENERACY HYPOTHESES ARE STATED NOWHERE, IN THE SAME ROUND THAT REPAIRED EXACTLY THIS AT `P15`

`rn_Hyp`'s own docstring reads *"`X, Y, sin θ ≠ 0` at the point"*, and its fields carry
`hX0`, `hY0`, `hs`. `rn_ks_einstein` and `rn_ks_G_offdiag` both take it. `rn_ks_nariai` carries
`(hΛ : 0 < Λ)` and `(hs : Real.sin (x 2) ≠ 0)` directly. **The paragraph states none of the five.**

And they are not decoration: the three components the prose quotes **divide by `X` and by `Y`**,
which is what two of those hypotheses are about, and the angular block divides by `sin θ`. This is
the defect `69` repaired at `P15`'s `prop:flat` **in this same round** (*"vanishes at every point of
the chart where `r ≠ 0` and `sin θ ≠ 0`"*). One clause fixes it here.

---

# PART 2 — THE SIX REGISTRATIONS, ON THE FOUR COUNTS

**Verdict first, because `70` is blocked on it: all six can be run.** Four are clean on all four
counts as written. Two want one extra arm each, and the arm is cheap and is the one that makes a
registered prediction mean what the argument needs it to mean. `E3` asked for a ruling and gets
one. Nothing below asks `70` to change an experiment's hypothesis.

| | ① can the prediction fail? | ② do the measures score the claim? | ③ subjects clean of the programme? | ④ could a judge infer the condition? |
|---|---|---|---|---|
| **E1** | ✔ | ⛔ **two gaps** | ✔ | ✔ |
| **E2** | ✔ | ⚠ **one, half-named** | ✔ | ✔ |
| **E3** | ✔ | ✔ | ✔ | ⚠ **one, measured but unused** |
| **E4** | ✔ | ⚠ **one named one-sidedly, one structural** | ✔ | ✔ |
| **E5** | ✔ | ⚠ **a ratio whose denominator is an outcome** | ✔ | ✔ |
| **E6** | ✔ | ⚠ **one, already answered by a registered secondary** | ✔ | ✔ |

**Count ① holds everywhere, and not weakly.** Every registration names what counts against it, at
stated confidence, with ceiling or floor clauses that report a non-reproducing premise *as a finding
against the premise* rather than explaining it away, and every one of the six ends *"Every failed
prediction is reported at the same weight as a held one."* `E3` registers the document's own
prediction at **35%** while predicting against it — which is how a prediction is registered rather
than announced.

**Count ③ holds everywhere, and `70`'s own probe is why.** `SUBJECT_ROUTE_PROBE.md` establishes a
route — fresh `claude -p` from a neutral directory, no setting sources, no MCP, no tools, no
persistence, the CLAUDE.md and email environment variables stripped — and then **tests it** rather
than asserting it: no repository file, no `CLAUDE.md`, no memory, no programme content. What leaks
is identity (the account email, an SDK preamble, a session link), identically in every condition, so
it biases a level and not a contrast. It is recorded with every trial.
*One methodological note, not a defect:* the probe's instrument is **the subject's own report of its
context**, and a model's account of its own context is exactly the kind of thing the paper's Step 1
says can be flattened. A comparison against the harness's constructed prompt would make it a
measurement rather than a self-report. *And one channel the probe does not cover:* the **items** are
written by a materials author working from a spec — a programme-trained seat. `E1` asserts *"Nothing
in them is the programme's"*, and **the materials are committed, so I measured it instead of taking
the assertion** — see below.

### ⛭ COUNT ③, MEASURED RATHER THAN ASSERTED — AND THE DISTINCTION THAT DECIDES IT

The six materials sets are committed: **900,506 bytes** across `E1`–`E6`. Swept **field by field**,
with each field classified as subject-visible or scorer-only from the registration's own *"what a
subject holds"* and *"the scorer gets"* sections, the programme-vocabulary pattern returns:

* **one subject-visible hit in 900 kB** — `throat`, in `E4-21`, a medicine patient-information
  leaflet: *"swelling of the face, tongue or throat, or difficulty breathing"*. Read at source: an
  allergic-reaction symptom, ordinary English, nothing to do with this programme's throat circle;
* **twelve scorer-only hits**, all in `E2`'s `key` field, all the phrase *"premature closure"* —
  **the name of the outcome category the scorer's own rubric derives.** Identical in every
  condition, so it cannot bias a contrast, and the scorer needs it.

The pattern is proved live on programme material in the same run (29 hits in `LOGICAL_ORDER.md`,
165 in `range_paper.tex`), which is `r7748 DEFECT 1`'s lesson applied before the claim is made.
⇒ **`E1`'s assertion holds, and now as a measurement.** The subject-visible/scorer-only split is the
distinction that decides the count, and it is worth stating in the registrations themselves.

**Count ④ holds everywhere.** Every registration strips the condition-revealing text before scoring
(`<receipt>` blocks in `E1`, `Receipt` sections in `E6`), withholds the condition and the hypothesis
from the scorer, hand-checks 20% stratified before unblinding with κ reported, and **runs an
explicit leak check with a stated threshold** (65% in `E1`, `E2`, `E4`). `E5` goes further and names
the one place where the cue *is* the effect under study, weighting its hand-check to `R2`.

---

## ⛔ `E1` — THE MEASURE TESTS THE INSTRUCTION, NOT THE RECEIPT (count ②)

**(a) Nothing records whether a receipt was produced.** The claim is Step 2's: *a pivot without a
receipt drops the part not taken in*. The contrast is `C1` (receipt **required**) against `C0`
(not required). Those are not the same thing: a `C0` answer may restate the asks spontaneously, and
a `C1` answer may produce a perfunctory receipt. **Patch:** code each response for whether it
restates the asks before answering — a separate pass on the *unstripped* text — and report the
contrast by receipt-presence as well as by condition. The run records already hold what this needs.

**(b) `C1` is not isolated from "analyse each ask".** Its prompt asks for the asks *and* **"what
each one actually requires"** — per-ask requirement analysis. `C2` controls for coverage, not for
analysis. So `P3` (`C1 ≥ C2`) cannot separate *the receipt* from *analysing each ask*, which is
precisely the separation Step 9's "this is prompt engineering" answer needs. **Patch, one arm on the
same items:** `C3` = `You are a helpful assistant. For each request in the message, say what it
requires. Then answer.` — the analysis without the own-words assimilation. If `C1 > C3`, the receipt
is doing work no instruction to analyse does.

## ⚠ `E2` — `C2`'s CLOSURE FIGURE IS PARTLY INSTRUCTION-FOLLOWING, AND `P3`/`P4` LEAN ON IT (count ②)

`70` names it: `C2`'s last clause describes the correct handling of `open` items. The consequence is
sharper than the note allows — `P3` and `P4` both rest on `C2`'s closure being at or below `C0`'s,
and `C2` is told to say when a question is unsettled. **Patch, one arm:** `C3` carrying **only**
that clause (`…where the information given does not settle the question, say so and say what would
settle it.`), without the at-weight framing. Then `C2`'s closure advantage over `C1` decomposes into
the framing's part and the instruction's part, and `P4`'s coupling claim stands on the framing.

## ⛭ `E3` — THE RULING `70` ASKED FOR: **KEEP BOTH, AND THE SPLIT IS A FINDING ABOUT THE PAPER**

**Keep `C2` and `C3`.** And the reason is stronger than cost: **the two readings are not two
readings of one manipulation, they are two different manipulations, and only one of them is an
instance of the paper's claim.** Step 4's mechanism is that contamination *erases the difference
that made the second perspective valuable*. Telling a reviewer it is scored on finding problems does
not erase that difference — it sharpens the reviewer's attention within its own perspective. So
`C2` is **not a contamination arm at all**; it is an attention manipulation that the same English
phrase happens to cover.

⇒ **Routed to the chat seat as a wording repair, not just an experiment ruling:** `LOGICAL_ORDER.md`
Step 8's `E3` should name the **commissioning framing** (`C3`) as the third contamination layer, and
report the literal reading (`C2`) separately as an informative non-instance. `70`'s `P4` at 35%
confidence is right either way, and if `C2 ≥ C0` the paper has a second result rather than a failed
prediction.

**And one count-④ patch:** the *"the review refers to an author's description"* rate is reported per
condition but not used. If it is high in `C1`–`C3` and near zero in `C0`, the scorer can infer the
condition on those trials. **Add the sensitivity analysis:** the primary contrast restricted to
trials whose review does not mention the framing.

## ⚠ `E4` — ONE LIMITATION STATED ONE-SIDEDLY, AND ONE THAT CANNOT BE FIXED (count ②)

**(a) The limitation cuts both ways.** `70` writes that a null result would mean the Step 1 failure
*"would then need the source to be out of context (the compaction case proper), and that is a
different, harder experiment"* — right, and the converse is owed in the same breath: **a positive
result is not evidence for the compaction claim either**, because this design's source sits in the
same context. State it symmetrically, before the data, so neither direction can be read as reaching
the compaction case.

**(b) The mechanism needs the notes to be the subject's own recollection, and a fresh context has
none.** The message says *"Earlier you read the document below and made these notes on it"* — which
is false of the subject, and a model may treat the notes as someone else's. That is not a framing to
improve; it is a limit on what any fresh-context design can test. It belongs in the registration as
a named limitation rather than being carried by the word *"framed"*.

## ⚠ `E5` — THE PRIMARY IS A RATIO WHOSE DENOMINATOR IS ITSELF AN OUTCOME (count ②)

`A = (valid anticipated findings) / (valid findings)`. If contamination **reduces valid findings** —
which is `P3`'s own prediction — then `A` rises without a single additional anticipation being
correct. The numerator and denominator move together under the very manipulation being tested.
**The unconfounded measure is already registered**: *novel valid findings per review*. **Patch, no
new trials:** promote it to co-primary, and report `A`'s numerator and denominator separately
alongside the ratio. `P2` then stands on something contamination cannot produce arithmetically.

Otherwise this is the cleanest of the six: the one place where the cue *is* the effect (`R2`'s echo
of the author's list) is named as such, the matcher is told to judge substance over wording, and the
hand-check is weighted to `R2`.

## ⚠ `E6` — THE CONDITIONS DIFFER IN REVISION PASSES AS WELL AS IN PERSPECTIVE (count ②)

`S` is six calls, each producing a revision: **six rewrites**. `G-ARP` revises at steps 1, 3, 5 and
6 — **four rewrites** — with two calls spent reviewing. If revision passes alone improve flaw
correction, `S` is *advantaged* on the primary, which makes `P1` **conservative** rather than
confounded: a `G-ARP` win over a six-rewrite baseline is a stronger result than over a matched one.
But the attribution to *perspective* then rests entirely on the staged measure — and **`70` has
already registered it** (*"the flaws caught at each stage… after steps 1, 3 and 5"*). **Patch:
none; say it.** The registration should state that the stage measure is what carries the attribution
and that the rewrite asymmetry makes `P1` conservative, so neither can be read in afterwards.

---

## ⛔ WHAT THIS REVISION GOT WRONG

**DEFECT 1 — a loop variable ate the dimension.** `for n, hs in HYPS.items()` rebound `n`, which
was the spacetime dimension, so every later `range(n)` raised `TypeError` and the whole
recomputation of both metrics never ran. The arms that had already printed looked fine, which is
what makes this kind of failure worth recording: **a probe that dies after its first findings prints
a result that reads like a complete one.** Renamed, and the dimension is never rebound.

**DEFECT 2 — a denominator test that compared the wrong objects.** I tested whether `'X'` and `'Y'`
were in the set of denominator *symbols*, while the expressions carry `X(τ)` and `Y(τ)` as
*functions*, so the set held `X(tau)` and the test failed on a true claim. Fixed by taking each
node's `func` where it is a function — and it is the `r7742` precaution again: **name what is being
counted**, values or the objects they label.

**DEFECT 3 — "hypotheses" meant every binder.** I counted `rn_ks_nariai`'s binders and got five,
including `{Λ : ℝ}`, `{x : Fin 4 → ℝ}` and `(μ ν : Fin 4)`, which are types and quantifiers and not
hypotheses. The count that matters is the propositional binders, which is two.

## WHAT IS ROUTED

Part 1's finding to `71` with its patch. Part 2's verdicts to `70`, per experiment, with two arms
to add before running and one ruling it asked for; and `E3`'s wording consequence to the chat seat.
**Nothing in this revision edits a paper, a receipt, a generated file, another seat's work, or any
registration** — and I was not a subject of anything.
