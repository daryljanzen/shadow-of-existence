# r7712 (60) — RESULT

**Order `r7709`.** Registered before measurement at `b0dc820c`, pushed before `probe.py`
existed. Readings in `runs/READINGS.txt` (exit `0`, all self-checks pass); tree in
`runs/TREE.txt`.

**THE THREE QUESTIONS, ANSWERED: ① right in all five places, and the registered expectation of
a defect was NOT borne out. ② yes — "therefore" needs a bijection the sketch does not cite, and
one of the four patches cannot be covered by that citation at all. ③ yes — and the region the
prose claims a map onto lies outside the spacetime the formalisation is built on.** Two repairs
routed.

---

## ① THE HORIZONS CLAUSE IS RIGHT IN ALL FIVE PLACES

The clause is on five lines — the abstract, the introduction, `prop:four_regions`, its proof,
and the formal paragraph — and **the arm was not whether it appears five times but whether each
of the five SENTENCES is a claim the clause belongs to.** A subject classifier was tested on an
injected point-set sentence and an injected curve sentence before it was used; **all five are
point-set claims**, so the clause belongs in each.

**And the geometry it repairs was checked rather than taken:** each patch is given on an OPEN
interval — `η ∈ (0,π)`, `ρ ∈ (0,∞)`, `ρ' ∈ (0,∞)` — so the patches exclude `r = 2M` and `r = 0`.
The clause adds back exactly what the open patches drop, and since the extension "terminates at
`r = 0`", `r = 0` is rightly **not** added.

**⌗ This answer was reachable, and the prediction expected the opposite.** I registered, at
moderate confidence, that at least one of the five would be attached to a sentence whose subject
was the curve rather than the point set — the family this seat has found repeatedly. It is not
so. Reporting five SUPPORTED was the cheap answer and is also the true one, **which is why the
subject was read each time rather than the clause counted.**

## ② "EACH PATCH IS THEREFORE ISOMETRIC" NEEDS A BIJECTION THE SKETCH DOES NOT CITE

What the proof sketch has is **a match of metric COEFFICIENTS** in each domain of `r`, by
`lem:interior_metric` and `prop:region_I_metric`. What it concludes is that **each patch is
therefore isometric** to the corresponding region.

> An isometry of a patch with a region needs **both** the coefficient identity **and** that the
> chart map is a bijection onto that region. A coefficient match alone gives an isometry onto
> the **image** of the map; it is the region only if the map is onto it.

**The outcome is (b), exactly as registered:** the bijections *are* established —
`cc_Φ_inj` and `ce_Ψ_inj` both exist and are both cited in P2's formal paragraphs — but **the
sketch's own passage cites neither.** So "therefore" is doing work the sketch does not show,
and the repair is a citation rather than a new result.

**⛔ AND ONE PATCH THE CITATION CANNOT COVER.** The four `r ≥ 0` patches include the **second
exterior**, and by ③ below that region lies outside the domain the spacetime is defined on. So
for that patch there is no isometry statement in the formalisation to cite, while "each patch"
quantifies over it. **The citation repairs three of the four; the fourth rests on the
reflection, which proves an invariance and not an isometry onto a region.**

⌗ Negative probe (21), registered for this revision: *a "therefore" is a load-bearing word, and
when the conclusion is stronger in KIND than what precedes it, the step IS the claim.*

## ③ "CARRIES IT ONTO THE SECOND EXTERIOR" SAYS MORE THAN `ce_reflection` PROVES

**The spacetime's domain, read from its definition:**
`def seWS : Set P := {p | 0 < p.2 ∧ p.1 * p.2 < 1}` — with its own docstring, *"EF's domain
`W = {V > 0, UV < 1}` (regions I and II)."*

**⚠ AND THIS IS WHERE THE REGISTERED PREDICTION WAS WRONG, which is why it was registered.** I
recorded that if `seWS` were `{UV < 1}` then `U > 0 > V` would have `UV < 0 < 1` and the second
exterior would be *inside* it, contradicting 71's note — and that the probe must read the
definition rather than decide from memory. **`seWS` carries the extra condition `V > 0`, so the
second exterior is outside. 71 is right and the guess was wrong, and the arm survived because
it was built to read.** Checked by arithmetic, not recollection: first exterior `(−1, 1)` in
`W`; black-hole interior `(0.5, 0.5)` in `W`; **second exterior `(1, −1)` not in `W`.**

**What `ce_reflection` states:** `(M : ℝ) (y a b : P) : rK M (−y) = rK M y ∧ FS M (−y) · gM(−a)(−b) = FS M y · gM a b`.
**No domain condition on any binder, and no mention of `se_S`.** It is a **pointwise algebraic
invariance on the whole plane** — the reflection preserves `r` and the metric expression, for
any point and any pair of vectors.

**"Carries it onto the second exterior" asserts a map onto a region** — and that region is
outside the domain the spacetime is defined on, so the formalisation cannot state it as a region
at all. **The file's own docstring says so in those words: "outside `W`."** ⌗ (`r7700`: a scope
claim is a claim about its SUPPORT — and here the support is not merely different from the
prose's, it is absent.)

## ④ THE REST OF THE LANDING HOLDS

- **"on that plane"** is at source and the old "on that manifold" is gone. ✔
- **The map clause** reads "into the radial plane of that manifold, onto the black-hole interior
  `U, V > 0`" — **and `U, V > 0` is checked rather than accepted:** the black-hole interior
  inside `W` needs `V > 0` (from `seWS`) and `UV > 0`, hence `U > 0` too. It is that region. ✔
- **The half-repair is taken:** `cc_Φ_inj` is cited beside "one-to-one". ✔
- **The three new declarations** — `ce_Ψ_inj`, `ce_pullback`, `ce_reflection` — all exist with
  their binders, and all three are printed in P2. Zero `axiom` tokens, zero `sorry`. ✔
- **P15, and this seat's own `r7710` finding:** the as-run offset now reads "about three per
  cent" in words, `$3.2$ per cent` occurs once in that sentence, and **the collision is gone.**
  The figure agrees with the receipt's own recorded text, *"NS3 900 was ~3 per cent short at
  ℓ = 4."*
  ⌗ **And one NOT FOUND, said as NOT FOUND over a named search:** the order attributes a
  *computed* `3.23 per cent` to the receipt. Searched by the digits across every receipt — one
  hit, in an unrelated P17 receipt — and by content in both NS3-bearing P15 receipts, where the
  figure appears as a **recorded comment** and not as a computed gate. So the paper's figure
  agrees with what the receipt **records**; whether a gate **computes** `3.23` is not
  established by these searches.

---

## THE REPAIRS ROUTED (two, neither this seat's to apply)

1. **P2, `prop:four_regions`' proof** — cite `cc_Φ_inj` and `ce_Ψ_inj` at the "therefore
   isometric" step, since a coefficient match alone gives an isometry onto the image. **And say
   something about the second exterior, whose isometry the formalisation does not reach**: the
   citation covers three of the four patches.
2. **P2, the reflection clause** — say the reflection **preserves** `r` and the metric
   coefficient-wise, and that the image lies **outside the chart's domain**, which is what
   `ce_reflection` proves and what the file's own docstring says.

## WHAT THIS PROBE CAUGHT IN ITSELF — ONE, AND IT WOULD HAVE PRODUCED TWO FALSE FINDINGS

- **The citation test looked for `cc\_Φ\_inj` with the Greek letter as a literal Unicode
  character. P2 prints it `cc\_$\Phi$\_inj` — the letter in MATH MODE — and `ce_Ψ_inj` as
  `ce\_$\Psi$\_inj`. Both ARE cited, and the probe reported both NOT FOUND**, which would have
  said the half-repair was not taken and that a landed citation was missing. **Two false
  findings, caught only by noticing that two arms of the same probe disagreed about the same
  string.** Fixed by matching the name's SKELETON: each ASCII run in order, with each Greek
  letter allowed as the character, as `$\Phi$`, as `\Phi`, or as `Phi`.

  **SEVENTH instance in seven revisions of one family: an instrument reads the FORM it was
  given, not the QUANTITY — and a NAME is a form.** Negative probe (19) says that in those
  words, was registered for this revision, and the arm broke anyway. ⌗ The honest lesson is not
  "remember the rule" — it is that **a rule written down is not a check**: what caught this was
  two arms reading the same string and disagreeing, which is the G4/G5 discipline doing its job
  one level up.

⌗ And one guard fired as designed before any reading: **G2 REFUSED** the first draft of the
subject markers, because `the four regions at $r \geq 0$` mixes prose with math and is none of
the three anchor forms. The markers are plain prose now — which is also the better reading,
since the math that follows varies (`$r \geq 0$`, `$r\ge0$`) and the prose does not.
