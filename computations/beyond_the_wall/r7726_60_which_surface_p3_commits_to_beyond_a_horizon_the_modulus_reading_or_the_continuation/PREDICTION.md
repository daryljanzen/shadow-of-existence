# `r7726` (60) — PREDICTION, registered before measurement

**Answers order `r7723`.** Committed and pushed in its own commit **before `probe.py` exists** and
before anything named below is read. At the moment of writing I have read **only the order**:
nothing in `SdS-slicing-curve*.tex` — not the abstract, not `sec:seam`, not `rem:reality-lines`,
not `prop:flip` or its remark, not the revised `prop:curvature`, its consequences or the new formal
sentence — nothing in `SlicingSky.lean` (`sl_flip`, `sl_twoalpha`, `sl_tangent_height` unread), and
not the new P15 clause or its receipt.

---

## ⓵ THE QUESTION, AND WHY IT IS NOT A TWO-WAY FORK

The order asks whether, beyond a horizon, P3 commits to **(A)** the curve `dr/dl = √|f|` read with
the modulus, whose `−r″/r` is machine-checked to flip sign, or **(B)** the continuation
`θ ↦ π/2 + iψ` of `prop:flip`, which carries the surface onto a **Lorentzian** piece and, on the de
Sitter member, keeps the constant curvature `1/α²` with no sign change.

**⚠ This seat's own standing guard says to check the fork before answering it:** *when a fork names
two objects, check that the thing they are supposed to be alternatives FOR has a slot for only one
of them.* So four readings are registered, not two, and **reaching any of them is a result**:

- **(A)** P3 commits to the modulus reading as the surface beyond a horizon ⇒ the sign clause goes
  back in, with its reason, and the static-region scoping is too narrow.
- **(B)** P3 commits to the continuation ⇒ my `r7724` ⓵ conflated the curve with the surface, 69's
  correction stands, and the remaining question is only whether the scoping leaves anything false.
- **(C)** ⚠ **P3 commits to BOTH, of two DIFFERENT objects** — the modulus reading of the *curve*
  (a one-dimensional object, which is what `sl_curvature_sign` is about) and the continuation of the
  *surface* — in which case the fork is ill-posed as a fork and the repair is a distinction rather
  than a choice of clause.
- **(D)** P3 commits to **neither**: the slicing surface is simply not defined past a horizon, and
  both readings are extensions the paper does not take. ⇒ Then the static-region scoping is not
  merely safe but **exactly right**, and the previous clause was the only error.

⌗ **I register (C) as the one I expect to be the subtle part**, and say so now so it cannot be
claimed afterwards. But it is an expectation and not a prediction of the verdict: `(A)`, `(B)` and
`(D)` are each reachable and each would be reported as found.

---

## ⓶ THE ARMS — every one an assertion that can FAIL, every one a comparison with no verdict predicted

**A — WHAT THE SURFACE IS, read from P3's own commitments and not from convention.**
- `A1` The abstract's own words about the surface and about the curvature's sign, located BY TEXT.
  ⇒ Readings: it scopes the sign claim; it does not; it says nothing about a sign at all.
- `A2` `sec:seam`'s account of passing a seam: whether the object carried across is **the curve**,
  **the surface**, or **the geometry**, read as the noun phrase each verb takes — the `r7718` guard,
  never by counting words.
- `A3` `rem:reality-lines`: what it says is real past a seam, and of which object.
- `A4` `prop:flip`'s **statement** (not its remark): what flips, and whether its conclusion names a
  surface, a signature, a metric or a curve.
- `A5` ⚠ **The decisive arm, and the one that decides between (A)/(B) and (C):** does any sentence of
  P3 apply `ds² = dl² + r²dφ²` with `dr/dl = √|f|` at a radius where `f < 0`? A named search, with
  the phrases searched printed beside the verdict — never a bare absence claim (`r7716`'s landing
  defect, not to be repeated for a fifth revision).
- `A6` And its converse: does any sentence apply the **continuation** to the *surface* as against to
  the geometry or the metric? Same discipline.

**B — WHAT THE FORMALISATION COMMITS TO, which is a different question from what the paper does.**
- `B1` `sl_curvature_sign`'s hypotheses name a curve `r : ℝ → ℝ` with `∀ t, HasDerivAt r √|f(r t)| t`
  — already read at `r7724` — so the arm is whether **anything** in the file quantifies over a
  *surface* at all, or whether every statement is about the curve. ⇒ If every statement is about the
  curve, then `(C)`'s distinction is already present in Lean and absent only from the prose.
- `B2` `sl_flip`'s statement: what it concludes, and of which object.
- `B3` ⚠ And the guard against my own instrument reading a NAME as a thing (`r7724`'s third defect,
  the eight `section KG…` headers): every token searched for is reported with **where it sits** — in
  a statement, in a docstring, or nowhere.

**C — WHETHER THE STATIC-REGION SCOPING LEAVES ANYTHING FALSE (the order's second question).**
- `C1` The revised `prop:curvature` statement, located by text: what it now claims and over what.
- `C2` The revised consequence two ("…does not detect the horizons **from the static region**.
  Approaching a horizon `r_h` … the curvature **tends to** `1/α² − M/r_h³`…"): ⚠ this is now a
  **limit** claim, so the arm is whether the limit exists and equals that number **from inside**,
  computed with its witness. ⇒ Reachable negative: the limit is correct but the sentence still
  asserts something at `r_h` itself.
- `C3` The revised consequence three ("Third, **within the static region** the curvature changes
  sign once, at …"): whether "once" is now true **within that region** — which requires that
  `r_HE` lie inside it and that no second zero of `K_G` does. Computed on an explicit member, with
  the zeros printed.
- `C4` The abstract's "changing sign once **there**": whether "there" resolves to the static region
  by its own sentence, or to something else. ⇒ `r7718`'s lesson: *a pronoun is a form, and what it
  points at has to be established rather than assumed.*
- `C5` ⚠ **The arm that could find the scoping too narrow:** is there any claim elsewhere in P3 that
  needs the curvature **outside** the static region and is now unsupported by any proposition? A
  named search over the paper for the curvature's symbol and its expression, each hit classified by
  whether its radius is inside the static region.

**D — THE REST OF THE LANDING, each a citation-against-statement comparison.**
- `D1` `prop:turning`'s new wording against `sl_accel_pos`/`sl_accel_neg` — the words are mine, so
  the arm is whether they say what those two declarations state, **not** whether they match my draft.
  ⚠ Checking my own offered words against the declarations rather than against my memory of them is
  the point of this arm.
- `D2` The conjugacy citation, now closing before the amount: whether what the citation covers is
  exactly what `sl_conjugacy` and `sl_conjugacy_fails` conclude.
- `D3` `prop:triple`'s "the unique **positive** value": whether that now matches
  `sl_triple_unique`'s `0 < ϱ`.
- `D4` `sl_twoalpha` and the formal paragraph after `prop:twoalpha`: all six, cited and present.
- `D5` `sl_tangent_height` against (v)'s new wording — "the tangent length …, which equals the
  hinge's height in the embedding at every `R`, is `√3α`". ⚠ Three claims in one clause (a length, an
  equality at every `R`, a value), and an arm that checks one and credits three has read the form.
- `D6` `sl_flip` after `prop:flip`'s proof: present, cited, and concluding what the citation says.
- `D7` P15's new clause, "…beyond every one of a million step-free surrogates of the curve's own
  scatter and autocorrelation at **all three widths**": ⚠ **"all three" is now the claim where
  `r7724` found "the two wider" was right for a different quantity** — so the arm reads the host
  receipt's own printed output at run time (negative probe 22) and asks whether the surrogate
  statement holds at all three, the narrowest included. ⌗ And `r7724`'s finding there was a
  hard-coded label disagreeing with its own witnesses, so **every number in this clause is checked
  against a witness and never against a label.**

---

## ⓷ REACHABLE NEGATIVES, named so that reaching one is a result

- **N1** P3 commits to the modulus reading ⇒ my `r7724` ⓵ was right and 69's removal is the error.
- **N2** P3 commits to the continuation ⇒ **my `r7724` ⓵ WAS WRONG**, having credited a statement
  about the *curve* to the *surface*. ⌗ **This is the negative I most expect to have to report
  against myself**, and it is the same family as every defect this seat has logged: *an instrument —
  or a reader — takes the form it was given for the quantity.* If it is reached, it is reported as
  this seat's error in the plainest terms, because `r7724`'s own routed clause asserted it.
- **N3** Both, of two objects ⇒ the fork is ill-posed and the repair is a distinction.
- **N4** Neither ⇒ the scoping is exactly right and nothing further is owed.
- **N5** The scoping leaves a claim elsewhere unsupported ⇒ a repair is owed, routed with its words.
- **N6** Consequence two's new limit claim is false, or true only one-sidedly.
- **N7** "Once … within the static region" is false on some member ⇒ a second zero exists there.
- **N8** One of my own offered words, as landed, does not say what the declarations state ⇒ my draft
  was wrong, or its transcription was.
- **N9** P15's "all three widths" fails at the narrowest ⇒ the clause overreaches where the last one
  did not.
- **N10** ⚠ My instrument fails before any of the above: a declaration unmatched, a statement cut at
  a delimiter inside it, a conclusion split inside a cast, a name read in a different sense, or a
  floating-point question asked of an exact zero. ⇒ So every reader gets a negative of the opposite
  class before use; statements are bounded by the `:= by` that begins a proof; conclusions are found
  at **bracket depth zero**; every token search reports **where** it sits; the Greek table is
  generated from the characters present **and accepts `SYMBOL` as well as `LETTER`**, which is
  `r7724`'s own defect; and no arm asks whether a computed root makes a quantity exactly zero.

---

## ⓸ THE SIX GUARD FAMILIES AND THE NEGATIVE PROBES, in force

**G1** one predicate per conjunct. **G2** three anchor forms only, unanchored markers REFUSED.
**G3** the flip family. **G4** classifier probes on both classes. **G5** reader probes with
negatives. **G6** every prose probe also on a whitespace-FLATTENED copy.

The twenty-two negative probes stand. The three this revision leans on hardest: **(19)** an
instrument reads the FORM it was given — and a NAME is a form; **(20)** a REPLACED sentence may have
changed its subject, which is the whole of section `C`; **(22)** a named search over SOURCE cannot
find a value that exists only at RUN TIME, which is why `D7` runs the receipt.

**⛭ And the rule bought at `r7722` and paid for again at `r7724`: EVERY ARM REPORTS ITS WITNESS AND
NOT ONLY ITS VERDICT.** At `r7724` it caught a wrong expectation, a false positive from a name, and
a write-up sentence that contradicted the very line printed beneath it.

**⛭⛭ And one discipline specific to this revision, because the order is a question about MY OWN
LAST ANSWER:** an arm that tests whether 69's correction is right must be built so that it can
return "my clause was sound" as readily as "my clause was wrong". So every arm in section `A` is
stated as a reading of P3's text with both outcomes named, and **none of them mentions `r7724` at
all** — the instrument is not shown which answer flatters its author.
