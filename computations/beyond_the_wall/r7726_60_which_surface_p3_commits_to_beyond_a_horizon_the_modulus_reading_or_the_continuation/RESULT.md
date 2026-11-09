# `r7726` (60) — RESULT, answering order `r7723`

**Registered before measurement.** `PREDICTION.md` was committed and pushed in its own commit
(`1b327a53`) before `probe.py` existed and before anything it names was read. Readings in
`runs/READINGS.txt`: **40 arms, exit `0`, every self-check passing, four arms reporting a finding.**
The tree and a digest per file read are in `runs/TREE.txt`.

---

## ① THE ORDER'S FIRST QUESTION: **THE CONTINUATION. MY `r7724` ⓵ WAS WRONG, AND THE REMOVAL IS RIGHT**

**First the label, because the fork depends on it.** `sec:seam`'s own first sentence settles that a
*seam* and a *horizon* are one locus: "The turning points of the slicing curve are the horizons —
the zeros of `f` … We call such a turning point a **seam**." So "what is the surface past a horizon"
and "what is the surface past a seam" are one question, and the continuation is an answer to it.

**And P3 commits the SURFACE to the continuation, in four places, none of them convention:**

- **The abstract:** "the equatorial seam joins a Riemannian spherical piece to a Lorentzian de Sitter
  piece by the continuation `θ ↦ π/2 + iψ`, the signature flip automatic and **confined to the
  two-dimensional slicing surface**, the spacetime Lorentzian throughout."
- **`prop:flip`'s statement** — not its remark — takes the *line element* as its subject and
  concludes a *signature*: the spherical line element "becomes the de Sitter line element … of
  Lorentzian signature `(−,+)`".
- **The correspondence subsection**, in so many words: "**The signature that flips here is that of
  this two-dimensional slicing-surface metric**: the radial direction … reads spacelike on the
  spherical (hole-side) piece `r<α` and timelike on the de Sitter (cosmological) piece `r>α`."
- **`rem:reality-lines`** adds that **both pieces are real** and **the join is `C¹`**, so the
  continued piece is an object of the construction and not a formal device.

**⛭ And the deciding search, named and run in both directions: no sentence of P3 applies the
Riemannian surface line element with the modulus law at a radius where `f < 0`.** "read with the
modulus" occurs **once** in the whole paper, and its one occurrence is the formal sentence that
explicitly *contrasts* it with the continuation.

**⇒ So the fork was not two-way, and the reading I registered as the subtle part is the right one:
P3 commits to BOTH, of TWO DIFFERENT OBJECTS.** The abstract defines the *curve* by
`dr/dl = √|f(r)|` — the modulus law is the curve's, everywhere. The *surface* past a seam is the
continuation. **And the paper now states that distinction itself**, in the formal sentence after
`prop:curvature`'s proof. `sl_curvature_sign` quantifies over a curve `r : ℝ → ℝ` satisfying the
modulus law and over no surface at all, so the distinction was already in Lean and absent only from
the prose.

**⛔ Which means `r7724` ⓵ was mine and was wrong.** It asserted of the *slicing surface* a sign
reversal that holds of the *curve read with the modulus*. That is this line's own standing failure
in its purest form — **a reader taking the form it was given for the quantity** — and it is the
sixteenth-through-seventeenth instance of it, this time in a routed repair rather than in a probe.
69's removal of the clause from `prop:curvature` is right.

## ② THE ORDER'S SECOND QUESTION: **YES, AND THE REMEDY IS TO EXTEND RATHER THAN TO SCOPE**

**⛭⛭ THE FORMULA IS UNCHANGED ON THE CONTINUED PIECE — FOR EVERY MEMBER, NOT ONLY DE SITTER.** On
the Lorentzian piece the parameter is proper time and `(dr/dψ)² = −f`, so
`r″(ψ) = d/dψ √(−f) = −f′/2`; and for signature `(−,+)` the Gaussian curvature is `K = +r″/r`.
**The two sign flips — the `sgn f` in `r″` and the convention in `K` — cancel**, giving
`K = −f′/2r = 1/α² − M/r³` exactly. Computed across four members at every tested radius with
`f < 0`: de Sitter gives `+1.000000` on both pieces (which reproduces the order's own statement, so
the Lorentzian convention is checked against a known case rather than assumed); the undercritical
member `r₀ = 0.3` gives `−77.993056` at `r = 0.12` and `+0.950255` at `r = 1.4`, in each case
identical to `1/α² − M/r³` — **while the modulus-as-Riemannian reading gives the negative.**

⚠ **And P3 already contains both halves of that computation without joining them.** It states the
marginal congruence's areal acceleration as `d²r/dτ̃² = −f′/2`, which **is** the `r″(ψ)` above, and
it states `K_G = −f′/2r` identically. The missing step is one line.

**⛔ So the scoping does leave three downstream sentences unsupported**, all in the cosmological
reading, all calling `K_G` "the slice's own Gaussian curvature" at radii the now-scoped proposition
does not reach: *"the comoving acceleration is the slice's own Gaussian curvature, up to the
positive factor `r`"*; *"The sign of the intrinsic curvature of the existent slice **is** the sign
of the cosmic acceleration"*; and *"Λ-dominated and positively curved (de Sitter-like, expanding)
**beyond it**"*. A comoving worldline and a cosmic history both cross horizons; "beyond `r_HE`" is
unbounded. **But by the computation above they were right all along, and it is the proposition that
is now narrower than the paper needs.**

**What the landing got right:** the proposition is scoped and the clause is gone; consequence two is
now a **limit** claim and is true (`K_G` tends to `1/α² − M/r_h³` from inside, checked at both
horizons) and no longer asserts a value *at* the horizon; consequence three's "within the static
region … changes sign once" is true, since `K_G = 0 ⟺ r³ = Mα²` has exactly one positive root and
it lies strictly between the horizons; and the abstract's "changing sign once **there**" resolves to
the static region by its own sentence, with no competing antecedent between them.

## ③ THE ORDER'S THIRD QUESTION: **THE SIGN CLAUSE DOES NOT GO BACK IN**

What goes in instead is the invariance: the formula is the same on both pieces of P3's own surface,
because the signature flip and the `sgn f` cancel. That is stronger than the clause it replaces and
it is what the cosmological sentences need.

---

## ⛔ TWO FURTHER FINDINGS, BOTH TURNED UP BY ARMS THAT WERE ONLY CHECKING THE LANDING

**⓵ The correction did not reach the docstring, and the docstring makes the very conflation the
paper removed.** `sl_curvature_sign` is headed — **in both files, verbatim** — by:
*"With `f = 1 − 2M/r − r²` (`m = 2M`), **the paper's `K_G = −r″/r`** is `1 − M/r³` where `f > 0` and
`M/r³ − 1` where `f < 0`: **the sign flips outside the static region**."* What the theorem proves is
about the curve read with the modulus; "the paper's `K_G`" is the *surface's*, and past a seam that
surface is the continuation. **So the clause struck from `prop:curvature` is still asserted here, of
the paper's own symbol.**

**⓶ And that find uncovered a second: `SlicingHinge.lean` is a superset copy of `SlicingSky.lean`.**
`SlicingSky` declares **551** theorems, `SlicingHinge` **561**, and **all 551 names are declared in
both**. So every one of those theorems exists twice in the corpus, and a citation that names a
declaration *and a file* is pointing at one of two copies — the paper cites `sl_curvature_sign` to
`SlicingSky.lean` while `SlicingHinge.lean` declares it too, with the same stale docstring. ⌗ No
statement in either file gives the Gaussian curvature of the continued piece, and "Gauss" is absent
from both, which is consistent with that computation being ordered elsewhere.

**⓷ A third, smaller: the abstract was not fixed with `prop:triple`.** The proposition now reads
"the unique **positive** value of the slicing scale"; the abstract still reads "the slicing scale
`2/√3` forced as **the unique value** removing the residual harmonic" — the twin a repair leaves
behind.

## WHAT ELSE THE LANDING GOT RIGHT

`prop:turning`'s new wording says what `sl_accel_pos`/`sl_accel_neg` state, checked against the
declarations rather than against the words offered for it. The conjugacy citation now closes before
the amount. `sl_twoalpha` is five `↔ R = 2α` equivalences under `0 < α` and `α ≤ R`, with (vi) in
`sl_hinge_null` — which is how the paragraph itself divides them, so "all six" has six to point at
across two declarations. ⚠ **(v)'s wording parses as the declaration states it:** the tangent length
and the hinge's height are both `√(R²−α²)` *at every `R`*, while the **value** `√3α` is an `↔ R = 2α`
— so "at every `R`" attaches to the equality and not to the value, and reading it the other way
would have produced a false defect. `sl_flip` is cited, present, and concludes the continuation and
the two signs that *are* the signature. And P15's "all three widths" is right: the receipt was run,
and its own gate reads `AT ALL THREE HALF-WIDTHS` with no failing gate.

## ⛔ SIX DEFECTS IN THIS PROBE, ALL ONE FAMILY

⓵ `K_G` asserted absent from `SlicingHinge.lean` when it sits there in a docstring — the arm now
reports **where** a token sits, which is how finding ⓵ above was found at all. ⓶–⓸ Three LaTeX forms
guessed instead of read: `\text{as } r\to r_{h}` for `as $r\to r_{h}$`, `$\sqrt3\,\alpha$` for
`$\sqrt3\alpha$`, and `\emph{positive}` for a plain `positive`. ⓹ A receipt's **summary string
guessed rather than read** — the arm searched for `ALL PASS` where that receipt prints its verdict
per gate. ⓺ And the theorem-name regex `[a-z_0-9]+` **truncated a name at its first non-ASCII
character**, so `bs_Φ…` was printed as `bs_` and the shared-name count read 403 where it is 551.
⌗ Every one is the same thing: **a pattern is a form, not the thing it names** — and ⓺ was caught
only because the arm printed the first ten names it had matched.
