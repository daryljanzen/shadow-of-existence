# `r7724` (60) — PREDICTION, registered before measurement

**Answers order `r7721`.** This file is committed and pushed in its own commit **before `probe.py`
exists**, and before anything named below is read. At the moment of writing I have read **only the
order**: nothing in `SdS-slicing-curve*.tex`, nothing in `SlicingCubic.lean` or any companion, and
none of the P15 sentence, its host receipt, or any of the eleven declarations the order names.

---

## ⓵ WHAT THE ORDER ASKS, in its own words, so the arms cannot be re-read after the fact

1. **`prop:conjugacy`** now says "conjugate **on `[0, 1]`**" and cites `sl_conjugacy`; a formal
   sentence after the proof adds that the identity **fails at every point of `[−1, 0)`**
   (`sl_conjugacy_fails`), "the domain being the one the proof's `a ∈ [0, π/2]` already takes".
2. **`prop:curvature`** now reads "**On the static region `f > 0`**, the slicing surface … has
   Gaussian curvature `K_G = …` ; **where `f < 0` its sign is reversed.**" A formal sentence after
   the proof cites `sl_curvature_sign` and says the surface-of-revolution formula `K_G = −r″/r` is
   **cited and not formalised**.
   → **THE ORDER'S FIRST QUESTION:** do the **three consequences that follow `prop:curvature`**
   remain true as written, given that they speak of "the static region"?
3. **After `prop:turning`'s proof:** `sl_turning`, `sl_turning_simple`, `sl_accel_pos`,
   `sl_accel_neg`, with "the limit of the second derivative at the root itself is not formalised".
   → **THE ORDER'S SECOND QUESTION:** does the statement "`d²r/dl²` at `r_h` = `±½f′(r_h)`" need a
   word, given that the limit **at the root** is not formalised?
4. **After `prop:triple`'s proof:** `sl_triple` and `sl_triple_unique`.
5. **In P15:** the source exclusion now reads "would have stood at more than **six** times that
   ratio's own scatter **at the two wider smoothings**".
   → **THE ORDER'S THIRD QUESTION:** is that what the **host receipt's `6.6` and `11.8`** carry?
6. **Explicitly NOT landed:** `71`'s strengthening of `prop:twoalpha` (v), which waits for row 11,
   campaign 121. ⇒ **An arm that reports `prop:twoalpha` as changed would be reporting a thing the
   order says is absent, so its ABSENCE is a registered expectation and its PRESENCE is a finding.**

---

## ⓶ THE ARMS, every one an ASSERTION THAT CAN FAIL, and every one a COMPARISON with no verdict predicted

⛔ **No arm below is registered with an expected answer.** Each names the two readings it decides
between, and **reaching either is a result.** Where an arm compares prose against a declaration, the
declaration is read from source and the prose from the flattened `.tex`; where it compares prose
against a number, the number is **computed or read from the receipt's own output**, never from the
order's summary of it.

**A — the conjugacy pair.**
- `A1` `prop:conjugacy`'s statement says "on `[0, 1]`" **or** it does not. ⌗ Decided from the
  proposition's own text, located BY TEXT and not by line number.
- `A2` `sl_conjugacy`'s conclusion is an identity **restricted to a set**, and that set is `[0,1]`
  **or** it is something else (all of `ℝ`, a half-line, `[0, 2/√3]`, an interval stated via a
  hypothesis rather than a `Set`). ⇒ **Three readings, not two:** restricted to `[0,1]`; restricted
  to another set; unrestricted with the interval carried only by a hypothesis on `a`.
- `A3` `sl_conjugacy_fails` asserts failure **at every point** of `[−1, 0)` **or** at some point,
  **or** on a set that is not `[−1, 0)`. ⌗ A universally quantified failure and an exhibited
  counterexample are DIFFERENT CLAIMS, and the prose says the first.
- `A4` ⚠ **The order's own justification is itself a claim to check:** "the domain being the one the
  proof's `a ∈ [0, π/2]` already takes". So the arm is: does the proof's `a` range map onto `[0,1]`
  under the map the proposition uses — computed, with the endpoints printed — **or** onto something
  wider or narrower? ⇒ If it maps onto something wider, "on `[0,1]`" is narrower than the proof
  supports and the restriction is unnecessary; if narrower, the restriction is **not enough**.

**B — the reversed sign, and the order's first question.**
- `B1` `prop:curvature`'s statement carries "On the static region `f > 0`" **or** it does not, and
  carries "where `f < 0` its sign is reversed" **or** it does not.
- `B2` `sl_curvature_sign`'s conclusion is about **the sign of `K_G`**, on which region, and whether
  it is one claim or two. ⇒ Readings: a single two-sided statement; one statement per region; a
  statement about `−r″/r` rather than about `K_G`; a statement with the regions as hypotheses.
- `B3` ⚠ **"cited and not formalised" is a claim about what is ABSENT, so it is checked by a NAMED
  SEARCH and never by a bare assertion** (`r7716`'s landing defect, not to be repeated for a fourth
  revision): the formula `K_G = −r″/r` is derived inside some declaration **or** it is not, searched
  for by the shapes it could take, with the search named beside the verdict.
- `B4` **THE ORDER'S FIRST QUESTION, and the one that can bite.** Locate **every** consequence that
  follows `prop:curvature` — by text, counting them rather than trusting "three" — and for each ask
  whether its subject is scoped to the static region. ⇒ Four readings per consequence, and they are
  **not** interchangeable: (a) it says "the static region" and is therefore still true as written;
  (b) it says "the static region" but its conclusion is one the reversed sign would **contradict**
  outside it, so the scope is load-bearing and present; (c) it does **not** scope, and the reversed
  sign makes it false somewhere; (d) it does not scope and does not need to, because its conclusion
  is sign-independent. ⌗ **(d) is the reading a careless probe would miss**, and (b) and (c) are the
  two that differ only in whether a word is there — so each consequence is read for its scope AND
  for whether its conclusion depends on the sign at all.
- `B5` ⚠ **A guard against my own instrument:** "its sign is reversed" is a claim about a quantity
  that could be **zero** somewhere, and reversed-sign claims are false at a zero. So the arm asks
  what happens where `f = 0` and whether either wording commits to a sign there. ⇒ `r7722`'s lesson
  in a new place: *the endpoint I would excuse may not be the endpoint that bites.*

**C — the unformalised limit, and the order's second question.**
- `C1` `prop:turning`'s statement carries `±½f′(r_h)` **or** another coefficient, read from the
  proposition's own text.
- `C2` `sl_turning` and `sl_turning_simple` conclude **what**, and does either reach the value **at**
  `r_h` or only on a punctured neighbourhood / as a limit along the curve? ⇒ Readings: the value at
  the root is stated; only the sign is stated; the value is stated under a hypothesis excluding the
  root; the pair divides as *general* and *simplified* with only one of them reaching the root.
- `C3` `sl_accel_pos` and `sl_accel_neg` are the two **signs** of a one-sided statement **or** two
  cases of a region split. ⌗ The distinction matters, because "±" in the prose could be a two-sided
  limit, a one-sided pair, or a sign convention on the branch.
- `C4` **THE ORDER'S SECOND QUESTION.** Does the prose assert the value **AT** `r_h`, while what is
  machine-checked holds **only away from it**? ⇒ Three readings: (a) the prose says "at `r_h`" and
  nothing formalised reaches `r_h`, so a word IS needed and I name it; (b) the prose already hedges
  (a limit, an approach, a one-sided value), so no word is needed; (c) something formalised **does**
  reach the root, so the order's own parenthetical is the thing that is stale. ⌗ **(c) is a
  reachable negative and would be a finding against the order rather than the paper**, which is
  exactly the shape `r7714` and `r7720` both turned up, so it is registered here as live.
- `C5` ⚠ And the `r7718` guard, since this is a (subject, conclusion) question: `d²r/dl²` is a
  property of the **curve**, while `f′(r_h)` is a property of the **metric function**; an arm that
  credits a statement about one to the other has read the form and not the quantity. So the subject
  of each declaration's conclusion is read as a **noun phrase its verb takes**, never by counting
  words.

**D — the triple pair.**
- `D1` `sl_triple` and `sl_triple_unique` exist, are cited where the order says, and conclude
  **existence** and **uniqueness** respectively — **or** the division is otherwise.
- `D2` "unique" is uniqueness of a **point**, of a **parameter**, or of a **configuration**; and
  whether the statement is an `↔`, an `∃!`, or an `∃` plus a separate uniqueness lemma. ⌗ `r7720`'s
  lesson: *an "exactly" in prose is an iff in the statement or it is not, and that is read.*

**E — P15, and the order's third question.**
- `E1` The exclusion sentence reads "more than six times … at the two wider smoothings" **or**
  something else, located by text in the flattened paper.
- `E2` The host receipt's own printed numbers for the ratio-to-scatter quantity are **read from the
  receipt's output**, not from the order. ⇒ The arm: are there exactly **two** values above the
  stated factor and a **third** below it, and are the two `6.6` and `11.8`?
- `E3` ⚠ **THE ARM THAT DECIDES THE QUESTION, and it is an inequality, not a match.** "More than
  six" against `6.6` is true; against `11.8` it is true; so the sentence is sound **iff** six is
  below BOTH and the excluded third smoothing is the one at `0.81`. ⇒ Readings: (a) sound and the
  tightest of the two is `6.6`, so "six" is the right floor and not a rounding of `6.6`; (b) sound
  but slack — a larger integer floor would also hold, which is a style point and not a defect;
  (c) **unsound**, because one of the two is **below** six or the narrowest is **above** it, which
  would make "the two wider" the wrong set. ⌗ And (d), the one `r7708` already paid for in this
  corpus: *the number is nearer the next integer than the one written* — so the arm reports the
  distance to both neighbouring integers rather than only whether the inequality holds.
- `E4` ⚠ **A named search, not an absence claim:** whether any OTHER sentence in the corpus states
  that factor or that smoothing set, so that a correction here would leave a twin behind. The
  phrases searched are printed beside the verdict.

**F — the registered absence.**
- `F1` `prop:twoalpha`'s statement is **unchanged** from what the previous landing left, read by
  text. ⇒ If it HAS changed, the order's "not landed yet" is wrong and that is a finding.

---

## ⓷ WHAT WOULD MAKE THIS REVISION WRONG — the reachable negatives, named so that reaching one is a result

- **N1** A consequence after `prop:curvature` that is NOT scoped and IS sign-dependent ⇒ a repair is
  owed, routed with the words.
- **N2** All consequences scoped **and** sign-independent ⇒ the order's first question has a
  *negative* answer in an interesting way: the scope was never load-bearing.
- **N3** Something formalised reaches `r_h` after all ⇒ the order's parenthetical is stale, not the
  paper's sentence.
- **N4** The prose already hedges the value at the root ⇒ no word needed, and the order's second
  question answers itself.
- **N5** One of P15's two values is below the stated factor, or the narrowest is above it ⇒ the
  sentence's SET is wrong, which is worse than its number.
- **N6** `sl_conjugacy` carries its interval only as a hypothesis on `a` rather than as a set ⇒
  "conjugate on `[0,1]`" is a reading of the statement and not the statement, and the citation needs
  a word.
- **N7** `prop:twoalpha` has changed ⇒ the landing record is wrong.
- **N8** ⚠ **My own instrument fails before any of the above:** a declaration cannot be matched (a
  Greek letter absent from a table — `r7722`'s purest defect), a statement is cut at a delimiter
  that also occurs inside it (`r7720` and `r7722` both), or a conclusion is found by splitting on a
  string that appears inside a cast. ⇒ So **every reader gets a negative of the opposite class
  before use**, every statement reader is bounded by the `:= by` that begins a proof rather than by
  the first `:=`, every conclusion is found at **bracket depth zero**, and the Greek table is
  **generated from the characters actually present in the files read**, not written out by hand.

---

## ⓸ THE SIX GUARD FAMILIES, in force

**G1** one predicate per conjunct. **G2** three anchor forms only — plain prose, an escaped control
sequence, an escaped math delimiter — and an unanchored marker is REFUSED. **G3** the flip family:
every classifier is shown a member of each class it can return. **G4** classifier probes tested on
both classes. **G5** reader probes with negatives. **G6** every prose probe is run on a
whitespace-FLATTENED copy as well.

⌗ And the twenty-two negative probes stand, with the two this revision leans on hardest: **(19)** an
instrument reads the FORM it was given — and a NAME is a form; **(22)** a named search over SOURCE
cannot find a value that exists only at RUN TIME, which is why `E2` reads the receipt's **output**.

**⛭ And the newest, bought by `r7722` and carried here as a rule rather than a hope: EVERY ARM
REPORTS ITS WITNESS AND NOT ONLY ITS VERDICT** — the value, the endpoint, the matched text, the
count — because that is what catches a wrong expectation as well as wrong code, and at `r7722` it
was the only thing that did.

---

## ⓹ WHAT I EXPECT TO BE THE SUBTLE PART, registered so it cannot be claimed afterwards

**The reversed sign and the three consequences (`B4`).** A scope word that is PRESENT is easy to
check; what is hard is deciding whether it is **load-bearing**. A consequence can be scoped and
sign-independent, in which case the scope is decoration; or unscoped and sign-independent, in which
case nothing is wrong despite the missing word. **Those two cases look identical to a probe that only
greps for "static region", and opposite to one that only asks whether the conclusion changes sign.**
So `B4` is registered as needing BOTH readings per consequence, and the count of consequences is
MEASURED rather than taken from the order's "three".

⌗ Second candidate: **`E3`'s inequality**. "More than six" is not a match to `6.6`, and the arm that
tests equality rather than the inequality would report a false defect — the mirror image of `r7722`'s
two receipt-index lines that looked stale and were not.
