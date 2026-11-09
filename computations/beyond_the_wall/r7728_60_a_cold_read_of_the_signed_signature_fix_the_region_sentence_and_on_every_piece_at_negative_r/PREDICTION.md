# `r7728` (60) — PREDICTION, registered before measurement

**Answers order `r7725`.** Committed and pushed in its own commit **before `probe.py` exists** and
before anything named below is read. At the moment of writing I have read **only the order**:
nothing of the revised `prop:curvature`, its proof, its restored consequences, the new machine-checked
sentence, the new region sentence in `sec:slicing`, the restored abstract, `prop:turning`'s new
formal sentence — and none of the eight declarations the order names (`sl_gauss_g2`,
`sl_curvature_static`, `sl_seam_square`, `sl_curvature_continued`, `sl_curvature_dS`,
`sl_curvature_witness`, `sl_turning_limits`, `sl_sign_change`).

⌗ **What I already know, because `r7726` measured it and it is this revision's own starting point:**
on the continued piece `(dr/dψ)² = −f` gives `r″(ψ) = −f′/2`, and signature `(−,+)` carries
`K = +r″/r`, so `K = −f′/2r = 1/α² − M/r³` unchanged. The order says the landing now states exactly
that, as `ε dl² + r²dφ²` with `ε = sgn f` and `K_G = −ε r″/r`. **So the arms below do not re-derive
it: they check whether the paper now says it, and what the new wording's own reach is.**

---

## ⓵ THE THREE QUESTIONS, in the order's words

1. Are **the three cosmological sentences `r7726` flagged** — the comoving acceleration as the
   slice's own curvature, the sign of the curvature as the sign of cosmic acceleration, and
   "positively curved … **beyond it**" — **now carried by the proposition as stated**?
2. Is the **new region sentence** right for the **de Sitter member** (no black-hole interior) and
   for the **overcritical** one, given that it says "in the undercritical regime"?
3. Does **"on every piece"** hold at **`r < 0` on the conjugate branch**, or does it need a word?

---

## ⓶ THE ARMS — every one an assertion that can FAIL, none with a predicted verdict

**A — THE PROPOSITION'S NEW REACH, and the order's first question.**
- `A1` `prop:curvature` states the metric as `ε dl² + r²dφ²` with `ε = sgn f` **or** it does not,
  and says "on every piece" **or** names the pieces some other way. Located by text.
- `A2` Its proof gives `K_G = −ε r″/r` **or** something else, and the two signs cancel **or** the
  cancellation is asserted rather than shown.
- `A3` ⚠ **`ε = sgn f` is a THREE-valued function, and `sgn 0 = 0`.** So the arm asks what the
  stated metric is **at a horizon**, where `ε = 0` and `ε dl² + r²dφ²` is **degenerate**. ⇒ Four
  readings: the proposition excludes the horizons; it does not and the metric there is degenerate;
  it says "on every piece" and the pieces are open, so the horizons are not in any piece; or it
  defines `ε` only off the zeros. ⌗ **This is the first thing I would get wrong if I assumed, and
  it is registered because `r7724` and `r7726` both turned on what happens exactly at `f = 0`.**
- `A4` **THE ORDER'S FIRST QUESTION, one arm per sentence, three in all.** For each of the three
  cosmological sentences: is its radius range now inside what the proposition covers? ⇒ Readings per
  sentence: carried outright; carried only on the open pieces, leaving the horizons uncovered;
  carried for `r > 0` but not at `r < 0`; not carried.
- `A5` ⚠ And the one that could make `A4` an over-read: the comoving-acceleration sentence is about
  `d²r/dτ̃²` on a **worldline**, not about a surface at a radius. So the arm reads whether the
  sentence's subject is the SLICE's curvature or the metric function's derivative — the `r7718`
  guard, the noun phrase its verb takes.

**B — THE REGION SENTENCE, and the order's second question.**
- `B1` The sentence is in `sec:slicing` as the order quotes it, located by text in the flattened
  copy, and it carries "In the undercritical regime".
- `B2` ⚠ **Its own count is checkable:** it names three pieces — an interior arc, a static arc, a
  ruling leg — and assigns `f > 0` to one and `f < 0` to the other two. On an undercritical member
  that is **measured**, not read: the number of positive roots, the sign of `f` on each piece, and
  whether the arcs it describes are the pieces the roots cut.
- `B3` **THE DE SITTER MEMBER.** With `M = 0` the cubic's roots are `{+α, 0, −α}`, so there is no
  black-hole horizon at positive `r` and **no black-hole interior**. ⇒ Readings: "in the
  undercritical regime" already excludes `M = 0` because the de Sitter member is a boundary case and
  not undercritical; it does not exclude it and the sentence is then false of it; or the sentence's
  three pieces degenerate gracefully into two. ⌗ **The arm must decide which by what "undercritical"
  is DEFINED as in this paper — located by text, not assumed to mean `27M² < α²` strictly.**
- `B4` **THE OVERCRITICAL MEMBER.** There `f < 0` for every `r > 0`, so the static arc is empty.
  ⇒ Does the sentence's "In the undercritical regime" scope it away, and is there any OTHER sentence
  that carries the region reading unscoped into the overcritical case? A named search, phrases
  printed.
- `B5` ⚠ And the Nariai member, which the order does not name: at the double root the two horizons
  merge, so the static arc is a point or empty. ⇒ Registered as a reachable third case the sentence
  may or may not cover.

**C — "ON EVERY PIECE" AT `r < 0`, and the order's third question.**
- `C1` Where the paper says the areal radius is **signed** and the slicing **closes** through
  `r = 0` onto the conjugate branch, located by text — because the question only arises if the
  construction really goes there, and that is established first.
- `C2` ⚠ **THE DECIDING COMPUTATION, and it is arithmetic rather than reading.** At `r < 0`:
  what are `f(r)`, `f′(r)`, `K_G = 1/α² − M/r³` and `−ε r″/r`? ⇒ `M/r³` is **negative** for `r < 0`,
  so `1/α² − M/r³` is **larger** than `1/α²` there, not smaller. And `ε = sgn f` at `r < 0` has to
  be computed, not assumed. ⇒ Readings: the formula holds with the same sign convention; it holds
  but the expression changes character (no pole crossing, curvature bounded below by `1/α²`); the
  factor `r` in `K_G = −ε r″/r` is **negative**, so a sign is dropped somewhere; or the surface is
  not defined at `r < 0` at all and "on every piece" over-reaches.
- `C3` ⚠ **The guard that matters most here:** `K_G = −r″/r` divides by `r`, and at `r < 0` that
  divisor is negative while the paper's own identity `K_G = −f′/2r` divides by the same `r`. So the
  arm checks whether the two expressions still agree at `r < 0` — **computed, with the witness
  printed at several negative radii** — because if they do, "on every piece" is sound there and the
  only question is whether the paper says so; and if they do not, the clause needs the word the
  order asks about.
- `C4` And a named search for whether any sentence already restricts the curvature statement to
  `r > 0`, so that a repair would not duplicate one.

**D — THE EIGHT DECLARATIONS, each a citation against a statement.**
- `D1`–`D6` `sl_gauss_g2`, `sl_curvature_static`, `sl_seam_square`, `sl_curvature_continued`,
  `sl_curvature_dS`, `sl_curvature_witness`: each exists, is in the file the sentence cites, and
  concludes what the sentence says it concludes. ⚠ **The sentence claims the curvature is computed
  "from the metric's own Riemann tensor", which is a claim about the METHOD** — so one arm asks
  whether any of the six actually builds a metric and takes its curvature, or whether they compute
  `−ε r″/r` and call it that. ⇒ That distinction is the whole value of the new citation, and
  crediting the second to the first is exactly the shape of `r7724`'s bridge finding.
- `D7` `sl_curvature_witness`'s name promises a **witness** — so the arm asks what it exhibits and
  whether a non-vacuity claim rests on it.
- `D8` `sl_turning_limits` and `sl_sign_change` against `prop:turning`'s new formal sentence.
- `D9` ⚠ **And the two repairs that went to `71` rather than being applied:** the `sl_curvature_sign`
  docstring and the copied probe files. The arm **re-measures both** rather than assuming they are
  still open — they may have landed in the same campaign. ⇒ Reaching "already fixed" is a result.

---

## ⓷ REACHABLE NEGATIVES, named so that reaching one is a result

- **N1** The proposition's new form does **not** cover one of the three cosmological sentences ⇒ a
  repair is owed and the first question answers in the negative.
- **N2** It covers all three outright ⇒ `r7726`'s ⓵ is fully discharged.
- **N3** ⚠ The stated metric is **degenerate at a horizon** because `sgn 0 = 0`, and the wording
  does not exclude it ⇒ a word is owed, and it is the same `f = 0` endpoint that bit twice before.
- **N4** The region sentence is **false of the de Sitter member** ⇒ a repair, unless
  "undercritical" is defined to exclude it.
- **N5** It is carried unscoped into the overcritical case somewhere else ⇒ a twin left behind.
- **N6** "On every piece" **fails at `r < 0`** ⇒ the word the order asks about, drafted with its
  reason.
- **N7** "On every piece" **holds at `r < 0`** and the paper already says so ⇒ nothing owed, and the
  order's third question answers itself.
- **N8** The six declarations do **not** compute from a Riemann tensor ⇒ the method claim over-reaches
  even though the result is right.
- **N9** One of the two repairs routed to `71` has already landed ⇒ do not re-route it.
- **N10** ⚠ My instrument fails before any of the above. ⇒ Every reader gets a negative of the
  opposite class before use; statements bounded by the `:= by` that begins a proof; conclusions at
  **bracket depth zero**; binder groups bounded by the same depth-zero colon; every token search
  reports **where** it sits; the generated character table accepts `SYMBOL` as well as `LETTER`;
  theorem names matched by `[^\s({\[:]+` and never by an ASCII-only class; **no summary string
  guessed rather than read**; and no arm asks whether a computed root makes a quantity exactly zero.
  ⌗ That list is the six defects of `r7726` and the four of `r7724`, each turned into a standing
  precaution.

---

## ⓸ THE GUARDS AND THE PROBES, in force

**G1** one predicate per conjunct. **G2** three anchor forms only. **G3** the flip family. **G4**
classifier probes on both classes. **G5** reader probes with negatives. **G6** every prose probe
also on a flattened copy. The twenty-two negative probes stand, with **(19)** a NAME is a form,
**(20)** a REPLACED sentence may have changed its subject — which is the whole of group `A`, since
three sentences were *restored* and one proposition *rewritten* — and **(22)** a named search over
source cannot find a run-time value.

**⛭ EVERY ARM REPORTS ITS WITNESS AND NOT ONLY ITS VERDICT.** At `r7724` that caught a wrong
expectation and a false positive; at `r7726` it caught a finding the arm was not looking for.

---

## ⓹ WHAT I EXPECT TO BE THE SUBTLE PART, registered so it cannot be claimed afterwards

**`C2`/`C3`, the conjugate branch.** `K_G = 1/α² − M/r³` and `K_G = −ε r″/r` both divide by `r`, and
at `r < 0` that divisor changes sign while `M/r³` also changes sign. **Two sign changes in one
expression is exactly the configuration where a reading that checks one of them concludes
confidently and wrongly** — which is what `r7724` ⓵ did with one sign change. So `C3` is registered
as requiring the two expressions to be **compared numerically at several negative radii**, not
reasoned about.

⌗ Second candidate: **`A3`, the degenerate `ε` at a horizon.** "On every piece" may be exactly the
wording that avoids it, by making the pieces open — in which case the right finding is that the
wording is better than it looks, and saying so is as much a result as a repair.
