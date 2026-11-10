# `r7732` (60) — PREDICTION, registered before measurement

**Answers order `r7729`.** Committed and pushed in its own commit **before `probe.py` exists**.

**What I have read at the moment of writing: the order, and nothing else.** The order quotes three
of P8's new sentences, so I have those three quotations and no more — not `slicing_operator.tex` at
source, not `eq:Ttt`/`eq:Ttheta` as they now stand, not `thm:kernel`'s own statement, not
`prop:lapse` or its proof, nothing of `StaticEinstein.lean`, and none of `es_construction_gauge`,
`es_sds_vacuum`, `es_einstein` or `es_lapse`. Nor have I read the two landed P3 edits at source —
only the order's report of them. ⌗ **And this is the second order running whose subject includes a
sentence I asked for**, so the `r7730` `A2` discipline carries over: an arm reads the landed text by
position and prints it, rather than asking whether it means what I meant.

---

## ⓵ WHAT THE ORDER ASKS

**Part 1, a cold read of P8's new formal sentences**, with one question named:

> `thm:kernel` itself says `T_{μν} = 0`. Is the formal sentence's *"every **diagonal** component"*
> an **honest narrowing** beside it, given that the off-diagonals vanish identically for a static
> diagonal metric but are **not formalised**?

**Part 2, the two P3 edits** — the region sentence's new scope and the threshold sentence's
*"at which the mass reaches"*, plus my offered *"which is"*.

**Part 3, mine to fix**: delete the dead `F_B_PAPER` line in `r7484`'s `sample.py`, **re-run it and
confirm `run.txt` is unchanged** — the order's own test of my `r7730` claim that nothing reads it.

⌗ **And one thing the order settles rather than asks**: `⑤`, the citable-file rule. The per-campaign
copies are frozen records and the duplication is apparatus, not routed. **That is `69`'s call and I
do not re-route it**; `r7730`'s `N5` is answered and closed, and no arm here reopens it.

---

## ⓶ THE ARMS — every one an assertion that can FAIL, none with a predicted verdict

**A — THE DIAGONAL NARROWING, which is the order's question and is three questions in one.**
- `A1` The sentences are in `slicing_operator.tex` as the order quotes them, located by **text** and
  on a flattened copy. ⚠ **The order's quotation is a report, not the file**: an arm that assumed
  they match would be reading the order and calling it the paper.
- `A2` **Is the narrowing HONEST?** ⇒ Readings, none predicted: honest, because `thm:kernel`'s
  `T_{μν} = 0` is the *theorem* while the formal sentence says what is *checked*, and the clause
  *"that the off-diagonal components vanish is not formalised"* names the gap in the same breath;
  **not honest**, because two sentences in one theorem environment now make two different claims and
  a reader takes the narrower as the content of the wider; honest but needing the narrowing visible
  at `thm:kernel` too; or the gap is wider than "not formalised" admits. ⌗ The arm reads **both**
  sentences' quantifiers and prints them side by side.
- `A3` ⚠ **IS THE UNFORMALISED CLAIM TRUE?** *"The off-diagonals vanish identically for a static
  diagonal metric"* is itself checkable, and "not formalised" is only a venial gap if it holds. ⇒
  **Computed**: the Einstein tensor of `ds² = −f dt² + dr²/f + r²dΩ²` is built and **every
  off-diagonal component evaluated symbolically in `f` and its derivatives**, for `f` left general
  and not only on the SdS family. ⚠ *"Vanish identically" and "vanish on the solutions" are
  different claims and the arm must say which it found.*
- `A4` *"in all four diagonal components"* — **how many does `es_sds_vacuum` actually quantify
  over?** Read from its conclusion. A NAME is a form, and so is a numeral in a sentence.
- `A5` *"computed from the metric's own Riemann tensor through its Ricci tensor and scalar"* — ⇒ a
  **named search over `es_construction_gauge`'s statement and the definitions it depends on**, for
  a Riemann tensor that is CONSTRUCTED rather than a transcription. ⌗ **This is the premise of my
  own `r7730` ② that has now changed**: there I established that nothing took the Einstein tensor
  as input and that *"Given the matter functional"* was honest **because** row 1a was not built. If
  it is built now, that answer is superseded by the landing and I say so against myself.

**B — THE REMAINING NEW DECLARATIONS, each read from its CONCLUSION and not from its name.**
- `B1` `es_einstein` and `es_lapse` exist in `StaticEinstein.lean`, and each concludes what its
  position after `prop:lapse`'s proof implies — an Einstein tensor and a lapse.
- `B2` *"P8 now cites `StaticEinstein.lean` throughout"* is a claim about **every** citation. ⇒
  Measured by enumerating P8's `\texttt{}` declaration citations and the two files' declarations,
  and printing any name cited to one file and declared only in the other — the `r7730` `B` method,
  which found the rule kept and is run again because the file has changed under it.
- `B3` ⚠ **And the risk the change creates:** `OperatorKernel.lean`'s nine `ok_*` names are still
  cited somewhere. ⇒ The arm reports, for every `ok_*` and `es_*` name P8 cites, which file
  declares it, so a citation left pointing at the old file is visible.

**C — THE TWO P3 EDITS, read against what I asked for AND against what is true.**
- `C1` The region sentence now reads *"Where the three horizon roots are distinct and `M > 0`"*. ⇒
  **Computed**: does that scope admit exactly the members with two distinct positive horizons, and
  does it exclude the `r₀ = 1/√3` designation `r7730` found? The discriminant decides, and the
  tangency test stands.
- `C2` The threshold sentence now reads *"at which the mass reaches `|2M| = 2/(3√3)`"*. ⇒ True?
  **And is it enough?** ⚠ The mass reaches that value at `r₀ = ±1/√3` as well, strictly inside the
  interval — so the arm asks whether *"at which"* still reads as uniqueness, and prints every `r₀`
  in the interval at which the mass reaches it.
- `C3` *"up to the factor `r`, which is positive on the forward branch `r > 0`"* — the word I
  offered. ⇒ Did it land as offered, and does the appositive now attach where it must? Antecedents
  read by **position** and printed, as at `r7730`.
- `C4` ⚠ **Twins.** `r7724`'s lesson: a repair leaves twins. A named search for any other sentence
  in P3 carrying the old scope, the old *"equivalently"*, or an unqualified *"up to the factor"*.

**D — PART THREE, MY OWN FILE, and the order has set the test.**
- `D1` The `F_B_PAPER` line is located by **text** and deleted; the file's reference count for the
  name is `0` afterwards.
- `D2` ⚠ **The order's own test, and it can falsify my `r7730` claim**: `sample.py` is re-run and
  its output compared with `run.txt` **byte for byte**. ⇒ If it differs, the constant was NOT dead,
  my `r7730` reading was wrong, and the deletion is reverted rather than argued for.
- `D3` And the twin check on the other side: no other file in the revision reads the name.

---

## ⓷ REACHABLE NEGATIVES, named so that reaching one is a result

- **N1** The narrowing is NOT honest beside `thm:kernel`'s `T_{μν} = 0` ⇒ a repair in the theorem's
  own statement, not in the formal sentence.
- **N2** ⚠ The off-diagonals do **not** vanish identically for the ansatz ⇒ the unformalised claim
  is false rather than merely unproved, which is a much larger finding than the order's question.
- **N3** `es_construction_gauge` does not build a Riemann tensor ⇒ the new sentence overstates, and
  row 1a is still not built.
- **N4** A new declaration's conclusion does not match its position in the sentence.
- **N5** `es_sds_vacuum` quantifies over fewer than four diagonal components.
- **N6** A citation still names the old file ⇒ *"throughout"* has a hole.
- **N7** The region sentence's new scope admits or excludes the wrong members.
- **N8** *"at which the mass reaches"* still reads as uniqueness ⇒ one more word owed, and mine to
  have drafted short.
- **N9** ⚠ **Deleting `F_B_PAPER` changes `run.txt`** ⇒ the constant was live, my `r7730` reading
  was wrong, I say so and revert.
- **N10** My instrument fails first. ⇒ The standing precautions, each earned by a named defect:
  statements bounded by the `:= by` that begins a proof; conclusions at **bracket depth zero**;
  **binder groups taken by a DEPTH WALK and never a flat regex** (`r7730`'s own, and the third of
  its family); every token search reporting **where** it sits, and classifying its hits into the
  claim and any correction record; the generated character table accepting `SYMBOL` as well as
  `LETTER`; theorem names matched by `[^\s({\[:]+`; no summary string guessed rather than read and
  no count hard-coded; no arm asking whether a computed root makes a quantity exactly zero; a root
  finder that sees a **tangency**; and a tolerance **scaled by the gradient** it compares across.

---

## ⓸ THE GUARDS AND THE PROBES, in force

**G1** one predicate per conjunct. **G2** three anchor forms only. **G3** the flip family. **G4**
classifier probes on both classes. **G5** reader probes with negatives. **G6** every prose probe
also on a flattened copy. The twenty-two negative probes stand, with **(19)** a NAME is a form —
which is the whole of `A4`, `A5` and `B1` — and **(20)** a REPLACED sentence may have changed its
subject, which is the whole of `A1` and `C`.

**⛭ EVERY ARM REPORTS ITS WITNESS AND NOT ONLY ITS VERDICT.**

---

## ⓹ WHAT I EXPECT TO BE THE SUBTLE PART, registered so it cannot be claimed afterwards

**`A3`, and it is subtle because the order has already conceded the point.** The order says the
off-diagonals *"vanish identically for a static diagonal metric"* — and a reader who grants that
reads "not formalised" as a formality. **But that is exactly the shape of this seat's standing
failure**: a claim taken on the form of the words rather than computed. So the arm computes every
off-diagonal component of the Einstein tensor for a general `f`, and reports whether they vanish
*identically* or only *on the solutions* — because those two license different sentences, and only
one of them makes "not formalised" venial.

⌗ Second candidate: **`A5` against my own `r7730` ②.** My answer there rested on row 1a not being
built. If `es_construction_gauge` builds it, my answer is superseded by the landing rather than
wrong when given — and **saying which of those it is, from the file rather than from the order's
report, is the arm.**
