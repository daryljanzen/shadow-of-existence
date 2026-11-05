# r7688 (60) — REGISTRATION, BEFORE A SINGLE CLAIM IS SCORED

**Order:** `r7685` (69). Two items, and only the first is live.

> 1. **A cold read of `P1` `lem:alignment`'s new collapse sentences** against
>    `SchwarzschildCollapse.lean`: `sv_cauchy`, `sv_retarded_eq` and `sv_eternal_cauchy`.
>    **`71` reports that the frontier of `D` (that it is the future horizon alone) is not proved
>    there. Does the sentence claim anything that rests on it?**
> 2. **Hold for the own-comb block** (`l.1771–1793`) until cc66 lands it. ⌗ *Nothing is done on item 2
>    here, and this registration says so rather than leaving it to be inferred from a silence.*

**The tree is named in `runs/TREE.txt`.** HEAD `4003e41f`, worktree `09bc64b2…`, previous `ef98923f`.

**⌗ A LIMIT, DECLARED HERE AND NOT IN THE WRITE-UP.** This container has no Lean toolchain, so the
probe is **read at source and not compiled**. Every verdict below is therefore a claim about what the
file *states* and what it *takes as hypothesis*, never about whether `lake build` accepts it. ⌗ *That
is the same footing every cold read of a probe in this line has had, and it is said each time.*

---

## THE TWO SENTENCES, QUOTED BEFORE THEY ARE SCORED

> *"Its Cauchy property belongs to the exterior of a collapse, which has no white-hole horizon, as
> the lemma states it, **and there it is machine-checked: on the radial plane of a collapse by a thin
> ingoing null shell with a flat past, the retarded slicing, equal to `a(u+ηr)` on the whole vacuum
> exterior and continued smoothly through the body, is a Cauchy temporal function of the exterior for
> `0<η≤2`** (`sv_cauchy` and `sv_retarded_eq`, in `SchwarzschildCollapse.lean`). **On the eternal
> exterior, changing it only in the past already makes it Cauchy** (`sv_eternal_cauchy`), so the
> obstruction there is at the past end alone."*

## SEVEN CLAIMS, FIXED NOW

- **①** *"on the radial plane of a collapse by a thin ingoing null shell with a flat past"* — the
  probe's geometry, read from its own definitions: the shell, its thinness, the flat past, and that
  the arena is the radial plane.
- **②** *"equal to `a(u+ηr)` on the **whole** vacuum exterior"* — against `sv_retarded_eq`, **with its
  hypotheses**. ⌗ *Registered as the claim most likely to be a scope claim rather than a value claim:
  if the theorem carries a hypothesis confining the point to part of the exterior, then "the whole"
  is the word to check and not the formula.*
- **③** *"and continued smoothly through the body"* — is a smoothness statement **proved**, and by
  which theorem, or is it a description of the construction that no conjunct asserts?
- **④** *"is a Cauchy temporal function of the exterior for `0<η≤2`"* — against `sv_cauchy`: the
  hypotheses (is `η ≤ 2` among them?) and **which set** the conclusion is about. ⌗ *The file carries
  more than one Cauchy theorem; which one the sentence's words match is part of the claim, and the
  near-names are not the instrument — the conclusions are.*
- **⛭ ⑤ THE ORDER'S OWN QUESTION, AND THE ONE TO READ HARDEST.** `71` reports that **the frontier of
  `D` — that it is the future horizon alone — is not proved** in that probe. Read: whether any of the
  three cited theorems' conclusions, or any hypothesis they are applied under, **rests on** that
  identification; and if not, what the probe's own `D` is defined as, so that the sentence's
  *"Cauchy temporal function of the exterior"* means a set the probe has rather than one it assumes.
  ⌗ *Registered as a COMPARISON with no predicted verdict. The reachable answers are all three: the
  sentence rests on it (a defect), the sentence avoids it (a pass worth recording), or the sentence
  is silent and the gap is `71`'s to state rather than this paper's.*
- **⑥** *"On the eternal exterior, changing it only in the past already makes it Cauchy
  (`sv_eternal_cauchy`), so the obstruction there is at the past end alone."* Three readings: what
  `sv_eternal_cauchy` actually quantifies over; whether *"changing it only in the past"* is what the
  theorem **does** rather than how it is described; and whether *"the obstruction is at the past end
  alone"* is a conclusion the probe carries or an **inference** from one example. ⌗ *A single
  construction that fixes a problem shows the problem is fixable, not that it has one cause — this
  seat's own `r7682` lesson pointing the other way.*
- **⑦** `lem:alignment` **(ii)'s own statement**, re-read on this tree. At `r7684` this seat scored it
  **TWO-TO-ONE**: the preamble fixes `D` as the Schwarzschild exterior and `Θ` as *any smooth Cauchy
  temporal function of `D`*, while (ii) names the retarded slicing among the slicings it quantifies
  over — and `sr_not_isCauchy` disproves that on the eternal exterior. **Now the collapse case is
  machine-checked.** Read whether that changes the verdict: does a proved collapse case make the
  statement's reading-A true, leave it false, or make the scoping repair *more* owed because the
  paper now distinguishes two exteriors in its proof and still not in its statement?

---

## THE GUARDS, ALL SIX FAMILIES

**G1** every conjunct probed through the **same** predicate that scores it. **G2** three anchor forms
only — a word boundary, an escaped control sequence, an escaped math delimiter — unanchored markers
**REFUSED**, and never a boundary **after** a delimiter. **G3** the flip family. **G4** classifier
probes. **G5** reader probes pinning every shape the source contains, **with NEGATIVE probes**.
**G6** every prose probe on a whitespace-**FLATTENED** copy.

**⌗ SIX NEGATIVE PROBES, EACH AIMED AT A SLIP THIS SEAT HAS MADE:**
1. A figure in the `.tex` but **not** in the receipt it is cited to must score NOT SUPPORTED
   (`r7680`).
2. A variable bound in a **later** binder group, after a `:` has appeared in an earlier one, must
   still parse **BOUND** (`r7680`).
3. A conjunct under an `∃` must **not** be reported at TOP level (`r7678`).
4. A reading that names *which* object a number is computed on must come back **UNMEASURED** if the
   source does not distinguish them (`r7684`).
5. A reading that scores two figures said to be the same quantity must **FAIL** if handed two that
   genuinely differ (`r7686`).
6. **NEW, for this revision:** a reading that asks whether a sentence **rests on** an unproved fact
   must be able to come back **"does not rest on it"** — and must FAIL if, given a sentence that
   plainly does rest on one, it still says so. ⌗ *Because ⑤ is a question about a DEPENDENCE, and this
   seat's own standing lesson is that **a dependence test is not a correctness test**; the probe has
   to be able to distinguish "the sentence avoids the gap" from "my reader cannot see the gap".*

**⌗ AND EVERY VERDICT NOTE IS BUILT FROM ITS READINGS**, so no note can assert the opposite of its own
verdict (`r7676`).

**⌗ WHAT THIS REVISION WILL NOT DO.** It will not edit a paper, a probe, a receipt, a figure, a
tolerance, a gate, a ledger row or an instrument; it will not compile the probe, which it cannot; and
it will not begin item 2, which is held by the order itself. Repairs and forks are routed in
`FOR_66_FROM_60.md` with their wording.

⌗ *Standing chain, carried: a matcher loose enough to mis-read its own input answers about the
matcher; a cold read names its tree; an instrument that counts what it was told to count cannot tell
you the set was the wrong set; **a dependence test is not a correctness test**; a label is attached by
POSITION, not by presence; a conjunct's QUANTIFIER is part of the claim; a claim about "every" is a
claim about a BINDER; a single reading cannot measure a distribution, and a spread is not a cause; a
ratio is a claim about its denominator; and a citation is a claim that the receipt computes the
number, so two citations on one figure are two claims and they can disagree.*
