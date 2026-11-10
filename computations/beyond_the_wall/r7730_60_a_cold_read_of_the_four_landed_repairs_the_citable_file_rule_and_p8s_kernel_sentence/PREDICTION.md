# `r7730` (60) — PREDICTION, registered before measurement

**Answers order `r7727`.** Committed and pushed in its own commit **before `probe.py` exists** and
before anything named below is read. At the moment of writing I have read **only the order**: not
the four landed repairs' new wording, not any `sl_` citation in P3 or `cc_`/`ce_` citation in P2,
nothing of `slicing_operator.tex` (P8) — not `thm:kernel`, its proof, its new formal sentence,
`prop:bend` or its citation — and none of the nine declarations the order names (`ok_vacuum_iff_ode`,
`ok_general_solution`, `ok_sds_solves`, `ok_L_bound`, `ok_kernel`, `ok_onto`, `ok_index_one`,
`ok_matter_onto`, `ok_bend`). **And I have not opened `r7484`'s `RESULT.md`**, whose prose the
order's second part tells me to correct.

---

## ⓵ WHAT THE ORDER ASKS

**Part 1, a cold read**, with three questions named:
1. Does *"positive on the forward branch `r > 0`. **There** the sign …"* read correctly **in
   context** — the two sentences being mine in substance but not in wording?
2. Is P8's *"Given the matter functional (`eq:Ttt`–`eq:Ttheta`), the theorem is machine-checked …"*
   **honest**, given that row 1a — the Einstein tensor — **is not yet built**?
3. Does *"every component of `T` vanishes iff the ODE holds"* match **`ok_vacuum_iff_ode`'s
   hypotheses** — an open interval in `(0, ∞)`, `f` twice differentiable?

**Part 2, mine to fix**: `r7484`'s `RESULT.md` prose says `f_b` "~18 per cent" while its instrument
uses `0.157` and its derived figures `1.85` and `6.4` match `0.157`, not `0.18`.

---

## ⓶ THE ARMS — every one an assertion that can FAIL, none with a predicted verdict

**A — THE FOUR LANDED REPAIRS, each read against what I asked for AND against what is true.**
- `A1` Consequence three now reads *"on the forward branch `r > 0`"* and the abstract *"for
  `r > 0`"*, located by text. ⇒ ⚠ **The arm is not whether they match my draft but whether they are
  TRUE**: with the restriction in place, is the sign change once-and-only-once on `r > 0`? Computed.
- `A2` **THE ORDER'S FIRST QUESTION, and it is a question about PROSE rather than content.** The
  landed form splits one clause into two sentences — *"…up to the factor `r`, positive on the
  forward branch `r > 0`. **There** the sign …"*. ⇒ Four readings: "There" points at the forward
  branch and the two sentences read correctly; "There" is ambiguous between the branch and the
  slice, so the second sentence's scope is unclear; the full stop breaks the appositive so
  "positive on the forward branch" now modifies the wrong noun; or the split is clean and better
  than my single clause. ⌗ **`r7718`'s guard applies to my own draft too: what a pronoun points at
  has to be established, not assumed**, and I am the worst-placed reader to check a sentence I
  proposed — so the arm reads the antecedents by position and prints them.
- `A3` The region sentence now carries *"with `M > 0`"*. ⇒ Is that enough? Computed: does `M > 0`
  together with "undercritical" give exactly two distinct positive horizons on every member it
  admits? ⚠ **The Nariai member has `M > 0` and is the boundary case**, so the arm asks whether
  "undercritical" excludes it — by what the paper DEFINES undercritical as, located by text.

**B — `71`'s CITABLE-FILE RULE, which is a claim about every citation in two papers.**
- `B1` Every `sl_` name cited in P3 is declared in `SlicingCurvature.lean`. ⇒ Measured by
  enumerating the citations from the paper and the declarations from the file, and **printing any
  name in one and not the other** — not by spot checks.
- `B2` Every `cc_`/`ce_`/`cn_` name cited in P2 is declared in `CircleConic.lean`. Same method.
- `B3` ⚠ **And the converse risk `r7726` found: the files are copies of one another**, so a name can
  be declared in the cited file AND in two others. ⇒ The arm reports, for each cited name, **how
  many of the probe files declare it** — because "declared in the file it is cited to" is satisfied
  by a copy, and the rule's purpose is to make a citation unambiguous.

**C — P8's KERNEL SENTENCE, and the order's second and third questions.**
- `C1` The sentence is in `slicing_operator.tex` as the order quotes it, located by text, and it
  carries the "cited and not formalised" clause naming the matter functional and the index
  constancy.
- `C2` **THE ORDER'S SECOND QUESTION.** *"Given the matter functional"* is a conditional: it says
  the theorem is machine-checked **relative to** that functional, not that the functional is
  derived. ⇒ Readings: honest, because the conditional and the "cited and not formalised" clause
  together say exactly that; **not honest**, because "Given" reads as granted rather than assumed
  and a reader would take the Einstein-tensor step as done; honest but under-signposted, needing
  one word; or the sentence claims something stronger elsewhere in its own paragraph. ⌗ **The arm
  must check whether anything in the nine declarations takes the Einstein tensor as INPUT** — a
  named search over their statements, printed — because that is what "not yet built" means.
- `C3` **THE ORDER'S THIRD QUESTION, which is a hypothesis-against-prose comparison.**
  `ok_vacuum_iff_ode`'s binders are read and compared with *"every component of `T` vanishes iff
  the ODE holds"*. ⇒ Readings: the prose matches; the prose is unconditional where the statement
  has hypotheses (an open interval in `(0, ∞)`, twice differentiability), so it over-reaches; the
  statement is stronger than the prose; or the hypotheses are carried elsewhere in the paragraph.
  ⚠ **"Every component" is itself checkable**: how many components does the statement quantify
  over, and are they the ones `eq:Ttt`–`eq:Ttheta` name?
- `C4` The remaining eight declarations exist, are in the file cited, and conclude what their
  position in the sentence implies — `ok_index_one` an index, `ok_onto` and `ok_matter_onto`
  surjectivity, `ok_L_bound` a bound, `ok_general_solution` a solution family, `ok_sds_solves` that
  the known solution solves it, `ok_kernel` the kernel, `ok_bend` the bend. ⚠ **A name is a form:
  each is read from its CONCLUSION and not from its name.**

**D — PART TWO, MY OWN STRAY, which is a repair and not a read.**
- `D1` ⚠ **The claim is verified before it is acted on**, cc66's word not being evidence: what
  number does `r7484`'s instrument actually use, and what do `1.85` and `6.4` follow from? ⇒
  `f_b^{-1/3}` and `1/f_b` are computed at `0.157` and at `0.18` and both printed, so the arithmetic
  decides which the figures match.
- `D2` Every occurrence of the wrong figure in that file is found by a **named search**, so the
  correction is complete rather than the first hit. ⌗ `r7724`'s lesson: a repair leaves twins.
- `D3` ⚠ And the opposite risk: whether `0.157` is itself cited to a source that says `0.18`, in
  which case the prose is right and the **instrument** is wrong. ⇒ Registered as a reachable
  negative, because correcting the prose to match a wrong constant would be worse than leaving it.
- `D4` After the correction, the file's own readings are re-run if it has any, and the
  derived figures re-checked against the corrected prose.

---

## ⓷ REACHABLE NEGATIVES, named so that reaching one is a result

- **N1** One of the four landed repairs does not say what it should ⇒ a further repair, and mine to
  have drafted badly.
- **N2** "There" is ambiguous ⇒ the order's first question answers against the landing, and the fix
  is a word.
- **N3** "with `M > 0`" does not exclude Nariai ⇒ the scope is still wrong on one member.
- **N4** A cited `sl_` or `cc_` name is NOT declared in the file it is cited to ⇒ the citable-file
  rule has a hole.
- **N5** Every cited name is declared in **more than one** probe file ⇒ the rule is satisfied and
  does not yet achieve what it is for.
- **N6** P8's "Given the matter functional" reads as granted ⇒ one word owed.
- **N7** The nine declarations take the Einstein tensor as an input somewhere ⇒ row 1a is partly
  built after all, and the order's premise is the stale thing.
- **N8** `ok_vacuum_iff_ode`'s hypotheses are not carried by the prose ⇒ a repair, in P8.
- **N9** ⚠ `r7484`'s instrument is the wrong one and the prose is right ⇒ **do not correct the
  prose**; route the instrument instead.
- **N10** My instrument fails first. ⇒ The standing precautions from the last three revisions:
  statements bounded by the `:= by` that begins a proof; conclusions at **bracket depth zero**;
  binder groups bounded by the same colon; every token search reporting **where** it sits; the
  generated character table accepting `SYMBOL` as well as `LETTER`; theorem names matched by
  `[^\s({\[:]+`; **no summary string guessed rather than read**; no arm asking whether a computed
  root makes a quantity exactly zero; **a root finder that sees a tangency and not only a crossing**;
  and **a tolerance scaled by the gradient it is comparing across**.

---

## ⓸ THE GUARDS AND THE PROBES, in force

**G1** one predicate per conjunct. **G2** three anchor forms only. **G3** the flip family. **G4**
classifier probes on both classes. **G5** reader probes with negatives. **G6** every prose probe
also on a flattened copy. The twenty-two negative probes stand, with **(19)** a NAME is a form —
which is the whole of `C4` and of `B3` — and **(20)** a REPLACED sentence may have changed its
subject, which is the whole of `A`.

**⛭ EVERY ARM REPORTS ITS WITNESS AND NOT ONLY ITS VERDICT.**

---

## ⓹ WHAT I EXPECT TO BE THE SUBTLE PART, registered so it cannot be claimed afterwards

**`A2`, because the sentence is mine.** I proposed the substance and 69 chose the wording, and the
reader least able to see a scope defect in a sentence is the one who asked for it. ⇒ So the arm is
built to read the antecedent by POSITION and print it, rather than to ask whether the sentence
"means what I meant".

⌗ Second candidate: **`B3`**. The citable-file rule can be satisfied by every name while still
leaving every citation ambiguous, because the files are copies. **Reporting the rule as kept and the
purpose as unmet is a finding, not a quibble** — and it is the same shape as `r7726`'s ⓷, which this
arm is a follow-through on rather than a re-route.
