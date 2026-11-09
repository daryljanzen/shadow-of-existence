# r7722 (60) — PREDICTION, registered before measurement

**Order answered:** `r7719` (69). A cold read of P3's first formal landing — **including a
MATHEMATICAL correction to `prop:involution`, which is a different kind of target from every
revision this seat has run: not whether prose matches a file, but whether a corrected proposition
is TRUE.**

**Tree:** `ce392787` (`origin/main` = `r7719`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/SlicingCubic.lean`
  (17,787 lines, 944,708 bytes), located by a NAMED search for `sl_nariai` across the probes
  directory. **Nothing inside it** — none of the eleven `sl_*` declarations has been read.
- **Nothing in P3 at source.** `prop:involution`, its proof, the remark after it,
  `cor:nariai-locus` and the new formal paragraph are all unread, and so is σ's own definition.
- **No receipt.**

## QUESTION ① — IS THE CORRECTED `prop:involution` TRUE AS STATED?

**⚠ This is the first order this seat has had whose question is a mathematical one about the
paper's own statement rather than about a correspondence.** The predicate is registered
accordingly: **the claims are about a FUNCTION's domain, image, fixed points and monotonicity, and
every one of them is checkable by ARITHMETIC once σ is read from ITS OWN DEFINITION — never from
the order's description of it.** The conjuncts, one predicate each (G1):

- **1a** σ(σ(r₀)) = r₀ **on `[−1/√3, 2/√3]`** — an involution claim on a stated interval.
- **1b** it **exchanges** `[0, 2/√3]` with `[−1/√3, 1]`. ⚠ **Registered before reading, because it
  is where I expect the subtlety:** those two intervals **overlap** on `[0, 1]` and their union is
  the whole of `[−1/√3, 2/√3]`. "Exchanges" must then mean σ maps the first ONTO the second and
  the second ONTO the first — which for an involution is one claim, not two — and whether that is
  consistent with 1a is **arithmetic to be done, not a form of words to accept.**
- **1c** on `[0, 1]` it is **decreasing, onto `[0, 1]`**, and carries the parameter **to the other
  non-negative root of its own cubic**. Three sub-claims: monotonicity, surjectivity onto that
  interval, and the root identification.
- **1d ⛔ AND THE HALF THE ORDER PUTS SECOND, WHICH IS A SEARCH AND NOT A READING:** whether
  anything else in P3 **or the companions** leans on the OLD interval `[0, 2/√3]` as σ's domain,
  or on "positive-root half" meaning `r₀ ≤ 2/√3`. **This is a corpus-wide NAMED search, and it is
  named as one: the files searched are listed, the strings searched for are listed, and a NOT
  FOUND is reported as NOT FOUND over exactly those.** ⌗ `r7716`'s landing defect was a bare
  absence; this arm is written to avoid it from the start.

**The honest outcomes:** the statement is true as corrected and nothing else leans on the old
reading — **NO FURTHER DEFECT**; the statement is true but a dependent site still carries the old
interval, and that site is the repair; or the corrected statement is itself wrong somewhere, which
is the sharpest finding available and the one I must be able to reach **against an order that
reports the correction as made.**
⚠ **THE TRAP, named: a correction that has just been made is the easiest thing in the world to
wave through**, and the order's framing — "whether the corrected proposition is now true" —
invites yes. **Both answers must stay reachable, and the arithmetic is done at the endpoints the
order itself names (`2/√3`, `1`, `−1/√3`, `0`) because those are where an interval claim fails.**

## QUESTION ② — ARE THE SEMI-AXES WHAT `sl_ellipse` STATES, OR A CONSEQUENCE?

The paragraph claims *"semi-axes `√(2/3)` along `r = r₀` and `√2` along `r = −r₀`"*. **Registered
predicate: an ellipse can be given by a QUADRATIC IDENTITY or by its SEMI-AXES ALONG NAMED
DIRECTIONS, and these are different statements — the second follows from the first only by a
diagonalisation the file may or may not perform.** So the arm reads `sl_ellipse`' conclusion and
asks whether the numbers `√(2/3)` and `√2`, and the two directions, appear **in it**. Three
outcomes: they are in the conclusion and the paragraph quotes it; the conclusion is a quadratic
identity and the semi-axes are the paragraph's own (sound) consequence, so the citation covers
less than the sentence; or neither.
⌗ This is the `r7718` shape — a consequence attributed to a citation — and the arm is written to
tell "states" from "implies" by reading the conclusion.

## QUESTION ③ — DOES "where the cubic is `(r − r₀)²(r + 2r₀)`" MATCH `sl_nariai`?

**Registered:** a factorisation is an IDENTITY between two polynomials, so the arm compares
`sl_nariai`'s conclusion with that product **as written**, including which variable is the
indeterminate and what hypothesis on `r₀` it carries. ⌗ And a double root at `r₀` with a simple
root at `−2r₀` is a strong claim: whether `sl_nariai` states the factorisation, or states the
Nariai locus and leaves the factorisation to the prose, is exactly the ② distinction again.

## ITEM ④ — THE REST OF THE LANDING

- **4a** The proof's added branch condition (`3r₀ + s ≥ 0`, *"exactly on `[−1/√3, 2/√3]`"*) and the
  monotonicity `σ′ = −(3r₀ + s)/(2s)`. ⚠ **"Exactly on" is an IF AND ONLY IF**, and the word is
  read rather than granted — an inclusion in one direction is not it.
- **4b** The remark's narrowed parenthesis, now `(r₀ ∈ [0, 1], 2M ≥ 0)`: whether `2M ≥ 0` holds on
  `[0,1]` and fails beyond it, by arithmetic from `2M`'s own expression in `r₀`.
- **4c** All eleven named declarations exist, spelled as printed, and are cited; `axiom` and
  `sorry` counts for `SlicingCubic.lean`.
- **4d** This seat's own `r7720` repair, as landed: the Sbierski citation now naming
  `sec:discussion`, and the offered bridge clause taken. Read at source against what was routed.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy.
**⛭ Carried forward and re-tested before use: the conclusion finder at BRACKET DEPTH ZERO
(`r7720`), the equation/inequality conjunct reader (`r7720`), the subject-and-conclusion pair
classifier (`r7718`), the declaration readers (`r7714`, `r7716`) and the name-skeleton matcher
(`r7712`).**
**⛭ NEW HERE, because the question is mathematical: every numerical claim is computed at the
NAMED ENDPOINTS, in exact arithmetic where the value is algebraic, and the computation is PRINTED
beside the verdict so the reader can check it rather than trust it.**

**The twenty-two negative probes stand.** Most exposed: (17) — the order reports a correction
made, so "true as stated" is the expected answer and the instrument must be able to say otherwise;
(19) a NAME is a form; (21) a load-bearing word is read and not granted — here "exchanges",
"onto", "exactly on" and "the other non-negative root"; (22) a named search over SOURCE cannot
find a value that exists only at RUN TIME.

**WHAT THIS REVISION CANNOT DO:** it cannot certify any Lean file as a proof, and it cannot read
the companions' own formalisations. Where a dependent site lies in a companion paper this seat
does not hold, that is NAMED as outside and routed rather than fixed.
