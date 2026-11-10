# `r7734` (60) — PREDICTION, registered before measurement

**Answers order `r7731`.** Committed and pushed in its own commit **before `probe.py` exists**.

**What I have read at the moment of writing: the order, and nothing else.** The order quotes three
of P8's new sentences and reports one P3 edit, so I have those quotations and that report — not
`slicing_operator.tex` at source, not `thm:kernel`'s new sentence or its index clause in place, not
`prop:cosmo` or its proof, nothing of `StaticEinstein.lean` as it now stands, and none of
`es_Ric_offdiag`, `es_G_offdiag`, `es_sds_vacuum_full`, `rg_cosmo`, `rg_witness`, `rg_sinh23`,
`rg_sinh23_radial` or `rg_tau23`. Nor have I read P3's repaired parenthetical at source.

⌗ **Third order running whose subject includes a sentence this seat asked for**, and the second in
which `71` has gone *further* than the repair I routed. So two disciplines carry over: every target
is located in the FILE and the order's quotation is never taken for the paper; and an arm that would
confirm my own previous answer is built to be able to refute it.

---

## ⓵ WHAT THE ORDER ASKS

**A cold read of the landing**, with two questions named:

> ① Whether *"`T_{μν} = 0` if and only if (`vacode`)"* is what **`ok_vacuum_iff_ode` with
> `es_G_offdiag`** delivers, **given that one is stated with MIXED components and on an interval**.
>
> ② Whether `prop:cosmo`'s *"unit timelike, obeys `ṙ² = E² − f`"* matches **`rg_cosmo`'s
> hypotheses**.

---

## ⓶ THE ARMS — every one an assertion that can FAIL, none with a predicted verdict

**A — THE ORDER'S FIRST QUESTION, WHICH IS A COMPOSITION AND NOT A LOOKUP.**
- `A1` The three sentences are in `slicing_operator.tex` as the order quotes them, located by text
  and on a flattened copy. ⚠ The order's quotation is a report; an arm that assumed they match
  would be reading the order and calling it the paper.
- `A2` ⚠ **THE INDEX-POSITION STEP.** `T_{μν} = 0` is a claim about the **lower-index** tensor;
  `ok_Tt`/`ok_Tθ` and `es_G` are **mixed**. ⇒ `T^μ_ν = 0 ⟹ T_{μν} = 0` needs the metric to be
  **invertible** at the point, i.e. `A ≠ 0` and `F ≠ 0` — which on the construction gauge `A = F = f`
  means **`f ≠ 0`, and that fails at every horizon.** The arm asks: does the interval
  `(r₁,r₂) ⊂ (0,∞)` the sentence quantifies over **exclude the horizons**, and does any declaration
  carry `f ≠ 0`? ⇒ Readings, none predicted: the step is covered by a hypothesis I will find; it is
  covered because `T_{μν} = g_{μα}T^α_ν` and a **vanishing** mixed tensor gives a vanishing lower one
  with no invertibility needed at all; it is not covered and the sentence over-reaches at the
  horizons; or the paper's gauge sentence excludes them elsewhere. ⌗ **I register now that I do not
  know which, and that the second reading may be the right one** — lowering an index multiplies, so
  zero may go to zero regardless. **The arm computes it rather than arguing it.**
- `A3` ⚠ **THE DOMAIN STEP.** `ok_vacuum_iff_ode` is quantified over `∀ r ∈ Ioo a b`;
  `es_G_offdiag` is, on the order's own wording, about a **profile** and presumably a point `x`. ⇒
  Are the two quantifications compatible as the sentence conjoins them, and is the conjunction
  *stated* anywhere or assembled by the reader? Both statements are read and their binders printed.
- `A4` *"every off-diagonal component vanishes for every profile"* — **how many components, and how
  general is "every profile"?** Read from `es_Ric_offdiag`'s and `es_G_offdiag`'s conclusions. ⚠
  "Every profile" is a quantifier over `A` and `F`, and the arm prints what they actually range
  over, because the ansatz is itself a restriction.
- `A5` *"a vacuum in all sixteen components"* — read from `es_sds_vacuum_full`'s conclusion. A
  NUMERAL in a sentence is a form.
- `A6` **The index clause.** *"as a linear map `C¹[r₁,r₂] → C⁰[r₁,r₂]` its index, `dim ker − codim
  range`, is `1`"*. ⚠ **`r7732` found that `ok_index_one`'s conclusion contains no "index" and that
  the integer is assembled by the reader from four conjuncts.** The new clause is more explicit about
  what it means — so the arm asks whether any declaration now states a **dimension** or a
  **codimension**, or whether the clause has made the reader's arithmetic *visible* without making
  it machine-checked. ⌗ *Either answer is a result; the second is not a complaint, because naming
  the arithmetic is itself an improvement on asserting its conclusion.*

**B — THE ORDER'S SECOND QUESTION, AND THE FIVE NEW `rg_*` DECLARATIONS.**
- `B1` `prop:cosmo`'s sentence located by text, and `rg_cosmo`'s binders read at depth zero and
  printed beside it. ⇒ Readings: the prose matches; the prose says "unit timelike" where the
  statement has a different normalisation or none; the statement has hypotheses the prose omits; or
  `ṙ² = E² − f` is in the statement with a sign or a factor the prose drops.
- `B2` ⚠ **And the claim is CHECKED, not only compared.** For the energy family, is
  `ṙ² = E² − f` what a unit timelike curve in this metric gives? **Computed** from the metric the
  Lean file declares, with the normalisation `g(u,u) = −1` imposed and `ṙ²` solved for.
- `B3` `rg_witness`, `rg_sinh23`, `rg_sinh23_radial` and `rg_tau23` exist, are in the file cited,
  and conclude what their position implies — a witness, a `sinh` relation, its radial form, and a
  proper-time statement. ⚠ **Each read from its CONCLUSION and not from its name.**
- `B4` Every declaration P8 cites is declared in the file P8 names, by enumeration — the `r7730`
  method, run again because the file has changed under it twice.

**C — THE P3 REPAIR, AND WHETHER IT LEFT A TWIN OF ITS OWN.**
- `C1` The parenthetical now reads *"(three real roots, distinct except at the designations
  `r₀ = ±1/√3`: the undercritical regime)"*, located by text. ⇒ **Is it TRUE?** Computed with the
  discriminant and the closed-form roots: is `r₀ = ±1/√3` the *only* designation in the open
  interval at which the roots are not distinct?
- `C2` ⚠ **Twins again.** A named search for any other sentence in P3 that glosses the strict
  interval as three distinct roots, or that reads "undercritical" as distinctness. `r7724`'s lesson
  has now fired twice in three revisions.

**D — MY OWN LAST ANSWER, WHICH THIS LANDING HAS GONE PAST.**
- `D1` `r7732` answered the diagonal narrowing **honest**, on the ground that the off-diagonal
  vanishing is an identity. `71` has now formalised it. ⇒ The arm asks whether the *new* sentence
  needs the old caveat at all, and whether anything in P8 still says the off-diagonals are not
  formalised — a stale clause left by a repair that overtook it.
- `D2` And the two stale Lean headers I routed at `r7732` `⓶`/`⓷` go to `71` by the order. ⇒
  **Re-measured rather than assumed still open**, because a header may have been fixed in passing.

---

## ⓷ REACHABLE NEGATIVES, named so that reaching one is a result

- **N1** ⚠ The mixed-to-lower step is not covered and `T_{μν} = 0` over-reaches where `f = 0`.
- **N2** The two declarations' quantifications do not compose as the sentence conjoins them.
- **N3** `es_sds_vacuum_full` quantifies over fewer than sixteen components.
- **N4** `es_Ric_offdiag`/`es_G_offdiag` are narrower than *"every profile"*.
- **N5** No declaration states a dimension or a codimension ⇒ the index clause names an arithmetic
  it does not check.
- **N6** `rg_cosmo`'s hypotheses are not what *"unit timelike, obeys `ṙ² = E² − f`"* says.
- **N7** `ṙ² = E² − f` is not what a unit timelike curve gives in this metric ⇒ a finding about the
  physics and not about the wording.
- **N8** One of the four other `rg_*` declarations does not conclude what its position implies.
- **N9** The P3 parenthetical is still wrong, or a twin of it survives elsewhere.
- **N10** ⚠ A clause saying the off-diagonals are not formalised survives the landing that
  formalised them.
- **N11** My instrument fails first. ⇒ The standing precautions, every one earned: statements
  bounded by the `:= by` that begins a proof; conclusions at **bracket depth zero**; binder groups
  by a **depth walk**; **a prose window bounded by its own end and never by a character count**;
  **every prose literal also matched on the flattened copy**, because a sentence may be line-wrapped;
  every token search reporting **where** it sits and classifying claim against record; **a reader's
  window never ending where the thing it reads begins**, and a not-found candidate reported as not
  found; **code and prose occurrences counted separately**; **roots from the closed form**, because a
  grid cannot resolve a near-tangency; **a positive control containing only cases its predicate is
  claimed for**, with the opposite class given its own negative; no count hard-coded and no summary
  string guessed; a tolerance scaled by the gradient it compares across; and **no f-string
  expression part containing a backslash**, which has bitten four windows running.

---

## ⓸ THE GUARDS AND THE PROBES, in force

**G1** one predicate per conjunct. **G2** three anchor forms only. **G3** the flip family. **G4**
classifier probes on both classes. **G5** reader probes with negatives. **G6** every prose probe
also on a flattened copy. The twenty-two negative probes stand, with **(19)** a NAME is a form —
which is the whole of `A4`, `A5` and `B3` — and **(20)** a REPLACED sentence may have changed its
subject, which is the whole of `A1`, `C` and `D1`.

**⛭ EVERY ARM REPORTS ITS WITNESS AND NOT ONLY ITS VERDICT.**

---

## ⓹ WHAT I EXPECT TO BE THE SUBTLE PART, registered so it cannot be claimed afterwards

**`A2`, and I register my own uncertainty about it in advance.** The order points at mixed versus
lower indices as though it were a gap, and it may be — or it may be that lowering an index is a
multiplication, so a vanishing mixed tensor gives a vanishing lower one with no invertibility
needed, and the worry dissolves. **I do not know which, and that is exactly the condition under
which this seat has gone wrong before**: `r7724` ⓵ asserted of one object what held of another
because the reading *sounded* right. So the arm **computes** `T_{μν} = g_{μα} T^α_ν` symbolically
at a general point, including where `f = 0`, and reports what it finds rather than which reading it
preferred.

⌗ Second candidate: **`B2`.** Comparing a prose hypothesis with a Lean binder is a form-to-form
comparison, and both could agree while **neither** is what a unit timelike curve actually satisfies.
So the normalisation is imposed on the metric and `ṙ²` solved for, independently of both.
