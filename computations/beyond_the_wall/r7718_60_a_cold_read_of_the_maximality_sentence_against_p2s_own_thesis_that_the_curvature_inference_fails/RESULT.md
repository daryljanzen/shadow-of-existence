# r7718 (60) — RESULT

**Order `r7715`.** Registered before measurement at `c3cd9002`, pushed before `probe.py`
existed. Readings in `runs/READINGS.txt` (exit `0`, all self-checks pass); tree in
`runs/TREE.txt`.

**THE SHARP QUESTION, ANSWERED: NO — the paper does not say both. The two inferences differ in
BOTH subject and conclusion, and the separating clause names exactly that difference in the
paper's own words.** ⛔ **But two things are owed, and neither is the collision the order
expected:** the sentence's own *"and therefore no `C²` extension of the metric"* is a step **no
cited declaration states**, and P2's repeated characterisation of what survives as
**curvature-INDEPENDENT** is now understated by this paper's own machine-checked result. **Two
repairs routed.**

---

## ① THE COLLISION QUESTION — NO COLLISION, AND IT IS THE PAIR THAT DECIDES IT

**The registered predicate: an inference is identified by its SUBJECT and its CONCLUSION, and the
Kretschmann scalar appearing on both sides proves nothing either way.** So both were read.

> **THE REFUTED INFERENCE**, from the paper's own gloss (located by text, not by the order's line
> number): *"the step from the curvature divergence at `r=0` to the conclusion that **no
> continuation through it exists**"*, and *"an **absolute terminus admitting no continuation**"*.
> Subject: **the curve**. Conclusion: no continuation exists.
>
> **THE ASSERTED INFERENCE**: the Kretschmann scalar of the Kruskal metric grows without bound
> approaching the frontier from inside, so no continuous extension of that scalar exists.
> Subject: **the metric on its chart**. Conclusion: no continuous extension of the scalar.

**They differ in both members.** And the paper does not merely assert the distinction — **it had
already conceded the metric side in its own words**, in the sentence the order pointed at, which
was located by text and read in its own place: *"the divergence at `z=π` is genuine, **no regular
Lorentzian extension crosses it**, and the `r<0` arm is a separate region reached only by
continuing the coordinate expressions across a singular junction; **the curve is extendible, the
spacetime is not**."*

**And the separating clause does the work it is given.** *"This bounds the Kruskal metric in its
own chart and not the curve."* ⌗ What it **bounds** was read as the noun phrase the verb takes —
**the metric on its chart** — and what it declines to bound is the curve. **That reading mattered:
a clause that ASSERTS a distinction does not MAKE one**, which is why the two subjects were read
from the thesis and the theorem separately before the clause was consulted at all.

## ② ⚠ THE REGISTERED WORRY ABOUT "ARTEFACT" WAS NOT BORNE OUT

I registered that I could not evaluate *"an artefact of the chart rather than of the manifold"*
without reading `prop:Kretschmann`, **because the Kretschmann scalar is a scalar INVARIANT and
`48M²/r⁶` diverges as `r → 0` whatever chart computes it** — and that if the paper meant the
scalar does not really diverge, **the thesis would be in trouble before any Lean file was
involved**. It does not mean that:

- **`prop:Kretschmann` ASSERTS the pole**: *"the Kretschmann scalar `K(z)` has a twelfth-order pole
  at `z = π` and remains bounded at `z = 0`"*.
- **The abstract states the artefact claim RELATIVE TO A METRIC**, and grants the divergence:
  *"the curvature scalar of the Schwarzschild perspectival metric … **real as that metric's** —
  rather than an invariant of the underlying smooth manifold parametrised by `z`"*.
- **And elsewhere the paper says so flatly**: *"The incompleteness at `r = 0` is real, not a mere
  chart artefact"*.

**So the paper's "artefact" answers WHICH METRIC CARRIES THE INVARIANT, not whether the scalar
diverges** — and `mx_blowup` is about the Kruskal metric's scalar, which is the metric the paper
grants the divergence to. **Consistent, and the arm survived because it was built to read the
proposition rather than decide from the word.**

## ③ ⛔ THE STEP THE PROSE TAKES THAT NO DECLARATION STATES

The sentence reads: *"…so **no continuous extension of that scalar**, and **therefore no `C²`
extension of the metric**, exists across any point of it (`mx_frontier`, `mx_blowup` and
`mx_inextendible`)."*

> **`mx_inextendible`'s conclusion is `¬∃ G : P → ℝ, ContinuousAt G p ∧ ∀ᶠ y in 𝓝[sk_kM] p,
> G y = mx_K M θ φ y`** — no **real-valued function** continuous at the frontier point agrees with
> the scalar near it. **It names no metric at all.**

The first half of the prose's conjunction is exactly that theorem. **The second half — "therefore
no `C²` extension of the metric" — is the prose's own step**, and the parenthesis attaches to the
whole sentence, so a reader takes both halves as machine-checked. It is **sound mathematics** (a
`C²` extension of the metric would make the curvature scalar continuous), but it is a step from a
statement about one function to a statement about metrics, and **nothing cited takes it**:

- **a NAMED search** over `mx_C2`, `mx_ext`, `mx_extension`, `mx_metric_inextendible`,
  `mx_no_extension`, `mx_maximal` and `mx_inext_metric` — **NOT FOUND over all seven names**;
- **and BY SHAPE** over all **36** `mx_` theorems and lemmas in the file — a wider search than this
  landing, because the prefix is reused by an earlier campaign in another namespace — **none states
  the `C²` regularity of an extension of a metric.** (The one regularity statement there is
  `mx_fA_contDiff`, the `C¹` regularity of a **chart map**, listed here so it is not silently
  counted.)

⌗ **Negative probe (21) in its own family: a "therefore" is a load-bearing word, and here the
conclusion is stronger in KIND than the premise** — a function's non-extendibility to a metric's.
`r7712` found the same shape with both premises unprinted; here the premise IS printed and only the
step is unattributed, which is the milder half of the family and still a citation that over-reaches.

## ④ ⚑ AND THE ONE THAT IS NOT ABOUT THIS SENTENCE AT ALL

P2 characterises what survives the falsification as **curvature-INDEPENDENT**, four times —
e.g. *"what is left standing is the rigorous, **curvature-independent** `C⁰`-inextendibility of
`r=0` established by Sbierski"*, and *"by causal-geometric (Lorentzian-diameter) arguments that **do
not invoke the curvature divergence at all**"*. The rhetorical force is that the curvature route to
inextendibility is unavailable and only the curvature-free route works.

**This landing supplies a curvature route.** It reaches inextendibility — of the Kruskal metric,
within its own chart, at `C²` — **from the curvature blow-up**. That does not touch the thesis,
whose subject is the curve. But *"the only surviving inextendibility is curvature-independent"* is
**no longer the whole of what this paper establishes**, and a reader who meets the abstract's
sentence first and the formal paragraph second will find the second doing what the first says
cannot be done. **One clause keeps them apart**, and it is the repair.

## ⑤ THE REST OF THE LANDING HOLDS

- **`mx_frontier` states the frontier of a SET** — `frontier {UV<1} = {UV=1}` — which is what "the
  only boundary … is the hyperbola" says. ⌗ **And it does NOT state "where `r = 0`"**: searched over
  `mx_frontier`'s own header for `rK` and for `r = 0`, both **NOT FOUND**; that identification is
  the limit inside `mx_blowup`'s chain (`rK → 0⁺` as `−UV → −1⁺`) and not a conclusion of
  `mx_frontier`. A pointer, not a defect.
- **`mx_blowup` is approached FROM INSIDE** — the within-domain filter, asserted non-trivial — and
  the scalar tends to `+∞`; and the scalar is the Kruskal chart's, `mx_K = kr_K (kr_SD M).gW`. ✔
- **This seat's own offered word is landed:** "The two `r<0` patches are **each** machine-checked…". ✔
- **The last sentence** — *"Maximality among all extensions, as an abstract spacetime, is not
  formalised"* — is at source, its predecessor is gone from P2, and **the file says the same in its
  own header**, so prose and file agree on what is not claimed. ✔
- **Zero `axiom` tokens, zero `sorry`.** ✔

---

## THE REPAIRS ROUTED (two, neither this seat's to apply)

1. **The maximality sentence, the "therefore" clause.** What is machine-checked is that **no
   continuous extension of the scalar** exists across any frontier point. Say that, and mark the
   `C²` consequence for the metric as following by the standard argument rather than by a cited
   theorem — e.g. *"…so no continuous extension of that scalar exists across any point of it
   (`mx_frontier`, `mx_blowup`, `mx_inextendible`); a `C²` extension of the metric would make that
   scalar continuous, so none exists either."* The mathematics is unchanged; the citation stops
   covering a step it does not reach.
2. **The "curvature-independent" characterisation, where it is used to describe ALL that survives.**
   One clause distinguishing the two subjects, as the formal paragraph already does locally —
   e.g. *"…what is left standing of `r=0`'s inextendibility **as a spacetime** is Sbierski's
   curvature-independent `C⁰` result; **within the Kruskal chart** the curvature divergence does
   bound the metric at `C²`, which this paper machine-checks."* Without it, the abstract says the
   curvature route is unavailable and the formal paragraph takes it.

## WHAT THIS PROBE CAUGHT IN ITSELF — TWO, AND BOTH ARE THE SAME FAMILY AGAIN

1. **The conclusion reader credited `ContDiff` to a METRIC wherever the word appeared**, so
   `mx_fA_contDiff : ContDiff ℝ 1 mx_fA` — the `C¹` regularity of a **chart map**, from an earlier
   campaign that shares the `mx_` prefix in another namespace — was reported as a metric statement,
   and the arm that says no declaration reaches the metric's `C²` regularity **failed on it**. A
   regularity claim is identified by **what it is about**, not by the word. Fixed with a third
   class — *the regularity of some other map* — and a negative for it.
2. **The subject reader COUNTED WORDS**, and the separating clause names **both** sides on purpose
   ("bounds the metric … and not the curve"), so the count tied and fell to dictionary order,
   returning *the curve* for a clause whose whole point is that it bounds the metric. **A clause of
   the form "bounds A and not B" cannot be read by counting A and B.** Fixed by reading the noun
   phrase the verb takes, with negatives both ways — the same clause written the other way round
   must read the other way.

**TENTH AND ELEVENTH INSTANCES IN NINE REVISIONS OF ONE FAMILY: an instrument reads the FORM it was
given, not the QUANTITY.** Here the forms were **a word** (`ContDiff`) and **a word count**. ⌗ And
the structural fix held again: both arms were **assertions that could fail**, so both failed
loudly instead of passing quietly — the second one would otherwise have reported that the paper's
own separating clause bounds the curve, which is the opposite of what it says, and **that would
have inverted the answer to the order's question.**

⌗ **And `r7716`'s landing defect was not repeated:** `check_absence_claims` fired on that diff
because two answers rested on bare absences. Every absence in this result **names its search as it
is written** — seven declaration names for the metric-extension search, thirty-six `mx_` statements
by shape, and `mx_frontier`'s own header for `r = 0`.
