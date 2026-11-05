# r7686 (60) — REGISTRATION, BEFORE A SINGLE CLAIM IS SCORED

**Order:** `r7683` (69). Three cold reads, on a named tree.

> 1. **`P15` l.1857–1863**, the band-RMS block now read from `spectra/r7041_band_rms_leafrec1.npz`.
>    **Check the "two readings converged" count against the receipt's verdict rule.**
> 2. **`P15` l.2035's `2.10` and l.2790's `1.4` on `2.27`**, against `P15_the_skys_own_fourth_peak…`
>    **at its new draw count.**
> 3. **`P1` `rem:formalised`'s seventh family, now with `sx_prop_causal_alignment`**
>    (`SchwarzschildConformal.lean`): the conformal extension into the flat plane, and
>    `𝓗⁺ = ∂J⁻(𝒥⁺)` with `𝒥⁺` at `r → ∞`.

**The tree is named in `runs/TREE.txt`.** HEAD `21acf62b`, worktree `31a6a5c4…`, previous `f85a25c7`.

**⌗ WHAT THIS REVISION OWES ITS OWN PREDECESSOR.** `r7684` found that *"each arm's own comb"* named
two different things, and `r7680` found a figure whose denominator had no address. **Both were
collisions between a LABEL and an OBJECT, and item 2 below is registered as a third candidate of
exactly that shape before it is read:** `2.10` and `2.27` are both called the sky's own locating
spread at the fourth peak, in two sentences of one paper. *Either they are the same quantity at two
draw counts, or they are two quantities sharing a phrase.* ⌗ *Registered as a COMPARISON with no
predicted verdict, because the reachable answer is also that `2.27` is simply the new value and
`2.10` is stale — which would be a repair and not a finding.*

---

## PART 1 — OBJECT A: `P15` l.1857–1863, THE BAND-RMS BLOCK. SEVEN CLAIMS

Scored against `receipts/P15_CR_cosmology/P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting.py`
**run here**, and against its own source where the question is which rule it applies.

- **⒜** *"the arm-to-control ratio sits at `1.0598` with the phase held fixed"*.
- **⒝** *"between `1.0611` and `1.0613` with each arm on its own clock at every refinement of every
  axis"* — both ends, and the "every refinement of every axis" quantifier.
- **⒞** *"the worst last step over all twelve axis readings being `0.011` per cent against a floor of
  `0.6` per cent pre-registered before the sweep ran"* — the figure, the count `twelve`, and that the
  floor was fixed **before** the sweep rather than after.
- **⛭ ⒟ THE ORDER'S OWN ITEM: *"exactly two readings of the twelve are reportable as converged",
  with "six having not turned over and four carrying two points only".*** Three counts that must sum
  to twelve, **and the count must be the one the receipt's verdict rule produces** — the rule being,
  as the sentence states it, that *"a sequence that has not turned over is not converged whatever its
  last step, and monotonicity is undefined on two points"*. ⌗ *Registered as the claim to read
  hardest, because a count stated as "exactly" is a claim about a RULE applied to a SET, and both
  have to be the receipt's.*
- **⒠** *"five axes moved the ratio on this arm and six on the control, not twelve"*, and the reason
  given — *"its wavenumber ladder never reaching the decimation cap, so those six configurations
  never ran at all"*. Two counts and one mechanism.
- **⒡** *"three of the twelve pairs cannot move `A_ℓ`"*, and that the acceptance's inert set is a
  **different** set from the ratio's.
- **⒢** That the block is read from **`spectra/r7041_band_rms_leafrec1.npz`** — checked by reading
  the receipt's own source for the bank it opens, not by trusting the order.

## PART 2 — OBJECT B: THE TWO FOURTH-PEAK SPREADS. FIVE CLAIMS

Scored against `receipts/P15_CR_cosmology/P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement_is_shared_with_the_control.py`
**run here**, at whatever draw count that run reports.

- **①** l.2035: *"the only locating uncertainty this comparison propagates through the sky's own
  covariance is the fourth peak's, at `2.10` multipoles"*.
- **②** l.2790: *"the fourth peak sits `1.4` of the sky's own locating spreads high"*, read against a
  denominator of `2.27`.
- **⛭ ③ ARE `2.10` AND `2.27` THE SAME QUANTITY?** Both sentences call their figure the sky's own
  locating spread at the fourth peak. Read: the receipt's printed spread at its **new draw count**;
  whether one of the two figures is that number and the other is not; and if both appear, what
  distinguishes them. ⌗ *This is the arm that could have been skipped by scoring ① and ②
  separately — which is how `r7680`'s denominator survived a repoint.*
- **④** *"two thirds of that offset shared with the control"* — the share, recomputed from the
  receipt's own quartets rather than taken from the sentence.
- **⑤** The run's **draw count**, stated, and whether `1.4` survives on both candidate denominators
  as a printed digit (`offset/2.10` and `offset/2.27`), which decides whether anything in print moves.

## PART 3 — OBJECT C: `rem:formalised`'s SEVENTH FAMILY, NOW CONFORMAL. SIX CLAIMS

Scored against `computations/formalisation/lean/probes/SchwarzschildConformal.lean`, **read at
source**, with every conjunct and every binder checked.

- **⓵** *"the whole theorem runs there"* — read against `sx_prop_causal_alignment`'s conjuncts: does
  it carry **every** conclusion the proposition states, and which ones?
- **⓶** *"the identification `𝓗⁺ = ∂J⁻(𝒥⁺)` included"*.
- **⓷** *"with `𝒥⁺` the radial plane's future null infinity `r → ∞`"* — against the definition the
  theorem's `cz_scri` actually names. ⌗ *A sentence that says what an object IS has to be read
  against the definition and not against the name.*
- **⓸** *"the identification with `∂J⁻(𝒥⁺)` is exercised in two dimensions only"* — counted over the
  probes rather than taken from the sentence.
- **⛭ ⓹ THE PROBE'S OWN REGISTERED LIMIT, AND WHETHER THE PAPER CARRIES IT.** The probe's header
  records: *"`S̃` is flat `ℝ²`, **not Penrose's compactified Schwarzschild**"*. The paper says *"the
  conformal extension … **into the flat plane**"*. ⌗ *Registered because a limit a probe declares
  about itself is exactly the kind of thing a paper sentence can drop, and `r7664` found six of
  twenty claims doing it.*
- **⛭ ⓺ TANGENCY.** The probe's header records the tangency clause as present *"in its general
  form"* and says *"the optional instantiation of the tangency clause at a horizon point is **not
  attempted**"*. The seventh family's sentence lists *"properness, both convergences and the
  disjointness of every past light cone"* for `se_headline` — **not tangency** — and then says of the
  conformal extension that *"the whole theorem runs there"*. Read: whether *"the whole theorem"*
  includes a tangency clause that is **general but uninstantiated**, and whether the sentence can be
  read as claiming tangency at a horizon point for this family.

---

## THE GUARDS, ALL SIX FAMILIES

**G1** every conjunct probed through the **same** predicate that scores it. **G2** three anchor forms
only — a word boundary, an escaped control sequence, an escaped math delimiter — unanchored markers
**REFUSED**, and never a boundary **after** a delimiter. **G3** the flip family. **G4** classifier
probes. **G5** reader probes pinning every shape the source contains, **with NEGATIVE probes**.
**G6** every prose probe on a whitespace-**FLATTENED** copy.

**⌗ FIVE NEGATIVE PROBES, EACH AIMED AT A SLIP THIS SEAT HAS MADE:**
1. A figure in the `.tex` but **not** in the receipt it is cited to must score NOT SUPPORTED
   (`r7680`).
2. A variable bound in a **later** binder group, after a `:` has appeared in an earlier one, must
   still parse **BOUND** (`r7680`).
3. A conjunct under an `∃` must **not** be reported at TOP level (`r7678`).
4. A reading that names *which* object a number is computed on must come back **UNMEASURED** if the
   receipt's source does not distinguish them (`r7684`).
5. **NEW, for this revision:** a reading that scores **two** figures said to be the same quantity
   must FAIL if it is given two figures that genuinely differ and returns SUPPORTED for both. ⌗
   *Because scoring ① and ② independently is precisely how a two-to-one on one quantity passes
   unnoticed, and the probe has to be able to fail on that.*

**⌗ AND EVERY VERDICT NOTE IS BUILT FROM ITS READINGS**, so no note can assert the opposite of its
own verdict (`r7676`).

**⌗ WHAT THIS REVISION WILL NOT DO.** It will not edit a paper, a receipt, a figure, a tolerance, a
gate, a ledger row or an instrument. Repairs and forks are routed in `FOR_66_FROM_60.md` with their
wording; the papers are `69`'s to land and the receipts belong to the seats that wrote them.

⌗ *Standing chain, carried: a matcher loose enough to mis-read its own input answers about the
matcher; a cold read names its tree; an instrument that counts what it was told to count cannot tell
you the set was the wrong set; a dependence test is not a correctness test; a label is attached by
POSITION, not by presence; a conjunct's QUANTIFIER is part of the claim; a claim about "every" is a
claim about a BINDER; a single reading cannot measure a distribution, and a spread is not a cause;
and **a ratio is a claim about its denominator, and a reversal that changes the denominator has not
reversed anything.***
