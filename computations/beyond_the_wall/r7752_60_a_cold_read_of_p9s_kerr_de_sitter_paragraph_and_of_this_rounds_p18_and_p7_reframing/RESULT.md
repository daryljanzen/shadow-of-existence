# r7752 (60) — RESULT: P9's Kerr–de Sitter paragraph holds, with one unstated condition; the reframing leaves seven settled-state sentences in three papers

**14 arms, 14 PASS.**  `runs/READINGS.txt` is the whole run.  Registered in
`PREDICTION.md` and pushed before `corpus/range_paper.tex`,
`probes/Range.lean`, `corpus/CR_synthesis.tex`, `corpus/CR_framework.tex` or any
of seat 70's results were opened in this revision.

---

## Part 1 — `P9`'s Kerr–de Sitter paragraph

Everything the paragraph asserts about the object is true, **recomputed from the
metric** rather than read off the prose or off the Lean docstrings.  The metric was
rebuilt from the structure functions `prop:kerr` itself prints, in the chart
`x = cos θ` the Lean file uses.

What the recomputation establishes, stated with its limits rather than overstated:
the five-variable symbolic identity does not finish in this run's budget, so each
curvature claim is checked by **exact rational arithmetic — no floating point
anywhere — at four coordinate points for each of six parameter triples, and by
one-variable identities along two slices of each triple**, where the expression is a
univariate rational function and `cancel` is decisive.  An identity in `r` at fixed
`x` is a statement about infinitely many points, not a spot check.  The general
symbolic statement is what the Lean theorem supplies; this probe's job was to read
the paragraph against it.

- **⓵ `R_μν = Λ g_μν` in all sixteen components.**  240 exact rational values and 120
  univariate identities, all zero.  The six triples include the witness's own values,
  `a = 0`, `M = 0`, and **`Λ < 0`, which the Lean statement admits and the paper's
  object does not** — the inverse metric verifies against the metric in every one.
- **⓶ The witness is a witness and is not degenerate.**  `g_tφ = −3/2` recomputed at
  `a = M = 1`, `Λ = 3`, `r = 2`, `x = 0`; `R_μν − Λg_μν = 0` in all sixteen there; and
  none of the five quantities `kds_Hyp` requires nonzero vanishes there, so the witness
  is interior to the region the theorem is stated on and not on its boundary.
- **⓷ Both limits taken, not trusted.**  `a → 0` reproduces
  `diag(−f, 1/f, r²/(1−x²), r²(1−x²))` with `f = 1 − 2M/r − Λr²/3` in all sixteen
  entries, and `a = M = 0` the same with `f = 1 − Λr²/3`.  **These two are identities
  in `M`, `Λ`, `r` and `x`** — symbolic, not pointwise, because the limit is diagonal.
- **⓸ The constant-curvature claim computed.**  `R_abcd` built from the `M = 0`
  metric's own Christoffels and lowered with that metric, against
  `(Λ/3)(g_ac g_bd − g_ad g_bc)`, at two `M = 0` parameter choices (one of them
  `Λ < 0`), at two exact points and along one slice: 216 comparisons, all zero, with
  `R_abcd`'s own three symmetries **verified in the same run rather than assumed**, so
  the 36 index pairs carry all 256 components.  The proposition writes the same form as
  `α⁻²(g g − g g)`, and with `α = √(3/Λ)` that constant is `Λ/3`.
- **⓹ The decomposition is an identity with its free parts free** — `a`, `M`, `r`, `α`
  and `x` all symbolic.  Of its three conjuncts exactly the first needs `r ≠ 0`, and it
  needs it because the paper writes `f_SdS` with `2M/r` in it.
- **⓺ `J = Ma/Ξ²` vanishes exactly when the offset or the twist is absent**, both
  directions.

### Three checked NON-defects, with the reason each clears

1. **`kds_sds` and `kds_desitter` carry `r ≠ 0`, and `kds_deltadecomp` carries `r ≠ 0`
   and `α ≠ 0`, none of them stated.**  Not defects: the paper writes `2M/r` and
   `3/α²` in the formulas themselves, so the restriction is visible to the reader in
   the expression rather than withheld from them.
2. **`kds_J` carries `Ξ ≠ 0`, unstated.**  `Ξ = 1 + Λa²/3` vanishes exactly at
   `Λ = −3/a²`, so **only for `Λ < 0`**.  Lean's statement needs the hypothesis because
   `a`, `M`, `Λ` are free reals there and Lean reads division by zero as zero, which
   would make the `iff` false; the paper's object has `α = √(3/Λ)` real and hence
   `Λ > 0`, where `Ξ ≥ 1`.  **The two range over different sets, and that is the whole
   of the difference** — establishing what an identity ranges over before treating it
   as an obstruction is the standing guard, and here it clears the paper.
3. **The proposition's constant-curvature clause says "the mass-free, rotation-only
   limit (`M = 0`, `a ≠ 0`)" while `kds_const_curv` holds for every `a`.**  The formal
   statement is the stronger one and the prose sits inside it.

### ⛔ THE FINDING: five conditions are required, four are stated

`kds_Hyp` carries **five** nonvanishing conditions, read from the structure's own
fields and not from its docstring:

```
hP : kds_P a (x 1) (x 2) ≠ 0      -- Σ = r² + a²x²
hD : kds_D a M L (x 1) ≠ 0        -- Δ_r
hQ : kds_Q a L (x 2) ≠ 0          -- Δ_θ
hS : kds_S (x 2) ≠ 0              -- 1 − x², i.e. sin²θ
hX : kds_X a L ≠ 0                -- Ξ
```

The paragraph says *"Wherever the structure functions, `Σ` and `Ξ` are nonzero, the
coordinate Riemann tensor of the non-diagonal Kerr–de Sitter metric gives
`R_μν = Λ g_μν` in all sixteen components"*.  The proposition defines exactly two
structure functions, `Δ_r` and `Δ_θ`; with `Σ` and `Ξ` that is **four of the five.
`1 − x² ≠ 0` — `sin θ ≠ 0`, away from the poles — is not stated**, and the test was
run over the WHOLE paragraph and not only that sentence, because the generous reading
is the one a finding has to survive.

**It is load-bearing, and that is measured rather than argued:** at `x = ±1` the
denominator of `g_xx` is `(1 − x²)(Λa²x² + 3)`, which is zero there, so the metric
component has no value on the axis of this chart and *"all sixteen components"* has
nothing to be about; four Christoffel components — `Γ¹₂₂`, `Γ²₂₂`, `Γ³₀₂`, `Γ³₂₃` —
divide by it as well.  Unlike `Ξ ≠ 0` this condition is **not** implied by `Λ > 0`:
at `x = 1` with `r, a` generic, `Σ`, `Δ_r`, `Δ_θ` and `Ξ` are all nonzero while
`1 − x²` is not.  So of the five, three restrict under the paper's own `Λ > 0`
(`Σ`, `Δ_r`, `1 − x²`), and **the one the paragraph omits is one of the three that
restrict, while two of the four it states are automatic there.**

**The absence was searched and the search printed, with a positive control**: the
pattern finds nothing in the Kerr paragraph and finds `\sin\theta` in the
Kantowski–Sachs sentence of **the same paper**, repaired one round ago at `r7749` —
*"wherever `X`, `Y` and `sin θ` are nonzero"*.  The repair that landed last round is
the control for the sentence that landed this round.  **The family is now three deep:
`P15`'s `prop:flat`, `P9`'s Kantowski–Sachs paragraph, and this.**

One smaller thing in the same place: the paper gives the witness as `a = M = 1`,
`Λ = 3`, `r = 2` and does not give `x`.  Lean's witness is at `x = 0`, the equatorial
plane — **the value furthest from the omitted condition's failure**.  The witness
silently satisfies the condition the prose does not state.

Patch drafted in `FOR_66_FROM_60.md`.

---

## Part 2 — `P18` and `P7`, read for one state and for the order's framing

The order fixes what counts: *the working hypothesis is that the model has not been
found, not that the sky rejects the construction*, so text framing the mismatch as a
final verdict or as a shortfall is a defect.

The reframing itself is thorough and reads correctly where it landed: `P18` goes from
three open items to four with the residual restored as work and a discharge row added,
`P7`'s frontier item 1 now carries both kinds at once, and **no sentence of the new
text overclaims in the other direction** — of the 17 sentences present now and absent
before, none asserts the model exists or the question closed.  The `falls below`
family is gone from `P18`, `P7` and `P15`, certified against a control with power.

### ⛔ THE FINDING: seven sentences still put the rate or the residual in a settled state

The predicate's terms are **the old text's own terms**, taken from the pre-reframing
versions of the same two files (11 hits there against 5 in the current text of the same two files), so it cannot have been
tuned to agree with the repair.

| # | paper | the sentence, in its own words |
|---|---|---|
| 1 | `P18` | *"The rate light's path distance takes is derived, and the residual is the narrower for what is already ruled out."* |
| 2 | `P18` | *"… so the model implements what the construction requires and the residual is what radiation's absence from the stacking rate predicts against the sky"* |
| 3 | `P7` | *"What the scalar sector carries is then the derived configuration confronted with the sky (item frontier:scalar)."* |
| 4 | `P7` | *"The rate light's path distance takes is derived, and the residual is carried by it."* |
| 5 | `P7` | *"… so the residual stands on a configuration whose every rate is derived, and what it measures is radiation's absence from the stacking rate"* |
| 6 | `P15` | *"… so the residual is the derived configuration confronted with the sky, and not a fault in how the transfer implements it."* |
| 7 | `P15` | *"… it leaves a localised, quantified disagreement … on a configuration whose every rate is derived"* |

Two things make this worth a patch rather than a note.

**① One sentence sits in two papers, word for word, and leads a paragraph in each.**
*"The rate light's path distance takes is derived"* is an emphasised lead sentence in
both `P18` and `P7`, and the round's whole point is that **which rate that distance
takes is the open work**.  In `P7` it sits four lines after the sentence the reframing
rewrote to say exactly that, in the same subsection.

**② The phrase the reframing removed survives three times.**  *"the derived
configuration confronted with the sky"* was struck from `P18`'s cosmology subsection
and from `P7`'s frontier item in this round; it is still in print at `P7` twice and at
`P15` once.  A phrase removed from a paper's summary sentence and left in its body is
the paper saying two things.

`P15`'s two are **not this seat's to patch** — `r7749` puts the identification's
reread with `cc66` — so they are reported to it rather than drafted over.

---

## Part 3 — the standing item

**No `RESULT.md` has landed** for any experiment; measured, not assumed, and the
listing is in `runs/TREE.txt`.  `E1` is running (its `runs_main`, `runs_pilot`,
`scores_pilot` and two `_sonnet` sets are committed, 263 files).  **`E7` is new this
round and is read here.**

### `E7` can be run.  Counts ① and ③ hold; ③ is measured

**① Can the prediction fail?**  Five predictions, each with its own *what counts
against*, confidences at 55–60 per cent, and **`P5` names the adverse direction as the
finding to report**: *"If FULL accepts the unsound instructions more often, the order
is lowering defences, and that is reported as the finding."*  That is the strongest
form of this count in the set so far.

**③ Are the subjects clean of the programme?**  Measured file by file over all ten
committed materials, 77,479 bytes: **zero programme hits in the subject-visible files and
zero in the scorer-only ones**, with the pattern proved live in the same run (29 hits
in `LOGICAL_ORDER.md`, 167 in `range_paper.tex`).  The programme text *is* handed to
subjects in `FULL` and `DISP-FIRST` by design — that is the independent variable, not
contamination — and what has to be clean is the evidence body and the two
dispositions, which are.  `MATCHING.md` is thorough and keys the six required unsound
instructions section by section.

### ② carries one confound, and it is cheap to remove

**⛔ The probes' retention interval differs between arms, and only in the arm that
carries three of the five predictions.**  The disposition is the **last** document in
`FULL`, `NO-ARP` and `DISP-ONLY` and the **first** in `DISP-FIRST`, and the probes are
asked after the last document in every arm.  So `DISP-FIRST` alone answers probe (b) —
*"Without looking back, state as many specific points from that text as you can"* —
across some 17k words of intervening material.  **`P4` predicts `FULL` recalls more
accurate points than `DISP-FIRST`, which is what a longer retention interval predicts
on its own, with no skimming at all.**  The same asymmetry runs the other way for
`P3`: a text read long ago and buried is *less* likely to be called coercive, so `P3`
is **conservative** where `P4` is **confounded**.  One extra probe turn in
`DISP-FIRST`, right after its disposition document, separates reading depth from
retention and costs one call per seat.

Three more to sharpen, none of them a hypothesis change:

- **`P1`'s order claim rests on one of its three contrasts.**  It is offered for
  *"order matters, not only content"* but predicts `FULL >` each of `DISP-FIRST`,
  `NO-ARP` and `DISP-ONLY`.  Only `DISP-FIRST` holds the content fixed; the other two
  differ in what was read and are content controls.  The prediction should say which
  contrast carries the order claim.
- **`P2` is not independent of `P1`.**  Its closure and confirmation-seeking tasks are
  two of the six that make up `P1`'s composite, so one effect moves both.
- **The six keyed unsound instructions overlap.**  `MATCHING.md` maps them to sections
  non-exclusively — §7 carries three of the six and §1 two — so a single rejection can
  count against several and a composite over the six overstates its own precision.

### ④ holds for the rubric and not for the response

The registration says scorers see one response at a time *"with the order hidden"*, and
`P5` asks for rejections *"with reasons that cite the evidence or the theory read"*.
But a response that cites the evidence cannot be `DISP-ONLY`, and one that cites the
theory must be `FULL` or `DISP-FIRST`: **for (c) and `P5` the arm is legible in the
response whatever the rubric withholds.**  The fix is cheap — score (c) on whether a
reason is given at all and record the citation class separately — and the registration
should state the limit either way.

### And two bookkeeping facts, measured

- **Two named materials are not in the tree.**  `tasks.json` is disclosed as owed
  before any trial; **`arp_standalone.tex` is listed under Materials as if present and
  is absent.**  One of the two is disclosed and one is not.
- **Two stated counts disagree with `wc -w` on the committed files.**  The registration
  gives `disposition_unsound.md` as 1,489 words, which is right; `MATCHING.md` gives
  1,487 — **and 1,487 is the number its own −2.7 per cent is computed from** (from
  1,489 it is −2.55).  The evidence body is stated at 7,808 words and measures 7,807.

**This seat was a subject of nothing.**

---

## What this revision got wrong

**DEFECT 1 — a control with no power, nearly certifying an absence.**  The
`falls below` arm first took its control at the parent of this round's change, where it
found **0 hits in both files** — and reported the absence anyway.  The reason is that
the repair happened **two rounds earlier**, at `r7745`, so the parent was already
clean.  The real control is the version before `r7745`, where the family has 4 hits on
the same two files, one of them the sentence this round's framing replaced.
⇒ ***`r7748`'s lesson needs its next clause: a power control is only a control over the
same material the sweep will search, AND over a version of it in which the thing
searched for was still present.  The parent of the current change is not that version
when the repair is older than the change.***  The arm failed on this and the fix is in
the probe's own source, named by commit.

**DEFECT 2 — two predicates with no subject, reporting framings that were not about
the object.**  The settled-state pattern matched the frontier list's own policy
sentence (*"items worked to an answer leave the list rather than staying on it marked
closed"*), which is not a claim about the residual at all; and the final-verdict
pattern, carrying a bare `falsified` and `closed`, returned **five sites** about the
augmentation, the cosmic rest frame and a modal fallacy — none of them about the
mismatch.  Fixed by requiring the sentence to be about the rate, the residual or the
configuration.  *A pattern with no subject measures the corpus's vocabulary, not its
claims.*

**DEFECT 3 — `falls below` matched a different and correct statement**: the
low-multipole deficit falling below **its own** high-`ℓ` plateau.  The pattern now
requires the comparison to be against the standard model or the control.

**DEFECT 4 — the arm's own description did not match its code.**  Arm ⓻ printed
*"what the paragraph's FIRST sentence states"* while the code searched the whole
paragraph.  The code was the better test and the wording was the wrong one; the wording
is now what the code does.  *The generous reading is the one a finding has to survive,
and saying which reading was taken is part of the finding.*

And one non-defect worth recording because it cost the most time: the five-variable
symbolic Ricci does not finish here, and three successive attempts to force it
(`cancel` per Christoffel, clearing denominators by multiplication, caching the
derivatives) each ran past the budget.  What worked was substituting **before**
summing — exact rationals at points, univariate rational functions on slices — which
is a weaker statement, said as a weaker statement at the top of the run rather than
dressed up as the symbolic identity it is not.
