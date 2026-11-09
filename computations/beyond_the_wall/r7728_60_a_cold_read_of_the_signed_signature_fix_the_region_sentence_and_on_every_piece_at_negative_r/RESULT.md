# `r7728` (60) — RESULT, answering order `r7725`

**Registered before measurement.** `PREDICTION.md` was committed and pushed in its own commit
(`3b0de16e`) before `probe.py` existed and before anything it names was read. Readings in
`runs/READINGS.txt`: **34 arms, exit `0`, every self-check passing, four arms reporting a finding.**

---

## THE FIX ITSELF IS SOUND, AND THE MACHINE-CHECKED SENTENCE IS EXACT RATHER THAN A GLOSS

`prop:curvature` now states `ds² = ε dl² + r(l)²dφ²` with `ε = sgn f` and gives `K_G` **on every
piece**; its proof derives `K_G = −ε r″/r`, names the `ε = −1` case against de Sitter's `cosh`
piece, and says the two signs cancel. ⚠ **And the endpoint that bit at `r7724` and again at `r7726`
is avoided by the wording, not by luck:** `ε = sgn f` is three-valued and `ε dl² + r²dφ²` is
**degenerate** where `ε = 0`, but a *piece* is bounded by the horizons, so no horizon lies in any
piece — and the formalisation carries the same exclusion as **strict** inequalities, with
`prop:turning`'s value at a horizon a one-sided limit. The degenerate point is excluded in three
places at once.

**⛭⛭ The method claim is exact.** `sl_gauss g x = kr_Rlow g x 0 1 0 1 / (g x).det`; `kr_Rlow` lowers
`kr_Riem`; and `kr_Riem` is the Riemann tensor built from Christoffel symbols and their partial
derivatives. So "computed from the metric's own Riemann tensor" is literally what happens, and the
metric is `sl_g2 ε r = !![ε, 0; 0, r²]` — the signature carried as a factor, as the paper states it.
⌗ This was the arm that would have caught a gloss, and it reports the opposite.

`sl_curvature_static` (ε = 1, `f > 0`) and `sl_curvature_continued` (ε = −1, `f < 0`) each give
**both** the `−ε r″/r` form **and** the same closed expression `1 − (m/2)/r³` — the cancellation
machine-checked rather than argued. `sl_curvature_dS` is the anchor the proof names;
`sl_curvature_witness` exhibits one concrete witness per signature, so neither half is vacuous;
`sl_seam_square` is the one line the flip rests on. `sl_turning_limits` gives exactly what
`prop:turning`'s wording needs and no more — the two **one-sided** limits `±½f′(r_h)`, both filters
non-trivial, the value nonzero — and `sl_sign_change` is the non-vacuity underneath it.
⌗ `sl_gauss_g2` concludes `−r″/(ε·r)` where the paper writes `−ε r″/r`: **the two agree only because
`ε² = 1`**, while the declaration's hypothesis is the weaker `ε ≠ 0`, so the declaration is the more
general statement and the paper quotes its specialisation.

**And consequence two's new clause is true, and is the fix's own payoff:** "it takes the same value
from either side" is exactly what the two sign flips cancelling buys, and what the scoped wording
could not say. Checked at both horizons against the value at the horizon itself, with the local
gradient printed.

---

## ① THE FIRST QUESTION: **THE PROPOSITION NOW CARRIES ALL THREE — BUT TWO OF THEM ASSUME A POSITIVE RADIUS IN THEIR OWN WORDS**

The identity the first two rest on, `d²r/dτ̃² = −f′/2 = r·K_G`, holds at **every** radius tested,
positive and negative alike. So the curvature they invoke is now covered on every piece.

**⛔ But:**
- *"the comoving acceleration is the slice's own Gaussian curvature, up to the **positive** factor
  `r`"* — on the conjugate branch that factor is the radius itself, and it is **negative**.
- *"The sign of the intrinsic curvature … **is** the sign of the cosmic acceleration"* — since the
  acceleration is `r·K_G`, those signs **oppose** wherever `r < 0`. Witnessed at `r = −1.5`, `−0.6`
  and `−0.2`.
- *"Λ-dominated and positively curved … beyond it"* — **carried outright.**

⇒ So the proposition has done its part; what remains is two sentences' own wording.

## ② THE SECOND QUESTION: **RIGHT FOR THE STRICTLY UNDERCRITICAL MEMBERS; WRONG FOR THE DE SITTER ONE; CORRECTLY SCOPED AWAY FROM THE OTHERS**

Measured member by member, with the discriminant and the roots printed:

| member | `27M²` | positive roots | regions |
|---|---|---|---|
| de Sitter, `M = 0` | `0` | one, simple | **two**, not three |
| undercritical `r₀ = 0.3`, `0.8` | `< 1` | two, simple | three ✓ |
| Nariai, `27M² = α²` | `1` | one, **double** | no static interval |
| overcritical, `2M = 0.5` | `1.6875` | none | one |

**⛔ The de Sitter member is undercritical by the discriminant and has no black-hole interior.** With
`M = 0` the cubic is `r³ − α²r`, roots `{+α, 0, −α}`: one positive root, the cosmological horizon,
the black-hole horizon having merged into `r = 0`. **The paper says so itself elsewhere** — "The
black-hole horizon shrinks until it merges into `r = 0` at the back" — so the construction knows it;
the new sentence just does not exclude it, because `27M² = 0 < α²`.

**The overcritical member is correctly scoped away** (no positive root at all, `f < 0` throughout),
and so is the **Nariai** member, which the order does not name: it has one positive root of
**multiplicity two**, so no static interval either.

## ③ THE THIRD QUESTION: **"ON EVERY PIECE" HOLDS AT `r < 0`. IT IS CONSEQUENCE THREE THAT NEEDS THE WORD**

**This was the case I registered in advance as the subtle part, and it is why.** Both forms divide by
`r`, which is negative there, *and* `M/r³` changes sign too — two sign changes in one expression, the
configuration where a reading that tracks one of them concludes confidently and wrongly, which is
exactly what `r7724` ⓵ did with one. So it was **compared numerically**: `1/α² − M/r³` and `−f′/2r`
agree at every negative radius tested, as they must, the identity being algebraic and sign-blind.

**⛔ But consequence three has been restored UNSCOPED, and "on every piece" now carries it onto the
conjugate branch, where it is false.** It reads *"changes sign once, at `r_HE`, being negative for
`r < r_HE` and positive for `r > r_HE`"*. At `r < 0` the term `−M/r³` is **positive**, so
`K_G > 1/α²` everywhere there — it never vanishes, never changes sign, has no flat locus — yet
`r < 0` satisfies `r < r_HE`, where the sentence says negative. ⌗ **The defect is new in kind:** not
the signature flip, which is resolved, but the mass term changing sign with `r³`. And a named search
finds no sentence already restricting the curvature statement to positive radius, so a repair would
not duplicate one.

---

## ⛔ AND THE TWO REPAIRS ROUTED TO `71` ARE RE-MEASURED, NOT ASSUMED: BOTH ARE STILL OPEN, AND THE SECOND IS WIDER

The `sl_curvature_sign` docstring still carries the struck clause — *"the paper's `K_G` … the sign
flips outside the static region"* — in **both** files read here. And the duplication now spans a
**third** file: `SlicingSky` declares 551 theorems, `SlicingHinge` 561, `SlicingCurvature` **569**,
and **all 551 of `SlicingSky`'s names are declared in `SlicingCurvature` too**. Each campaign copies
the file forward, so the docstring has now been copied forward with it.

---

## ⛔ TWO DEFECTS IN THIS PROBE, BOTH OF THE FAMILY

⓵ **The root finder found roots by SIGN CHANGE alone, and a tangency changes no sign** — so on the
Nariai member it reported "no positive roots" where there is one of multiplicity two. It now detects
the stationary points as well and reports each root with its multiplicity. ⌗ *A method that detects
only crossings cannot see a touch.* ⓶ **An arm compared two one-sided values at a fixed step against
a fixed tolerance** and failed at the inner horizon — not because the values differ but because
`K_G` has a gradient of `3M/r⁴ ≈ 50` there, so a `1e−7` step moves it by `1e−5`. It now scales its
tolerance by the gradient it measures, and prints it. ⌗ And one escaping failure in writing the
probe, for the third window running: an f-string expression part cannot contain a backslash, so the
LaTeX string had to be hoisted out — recorded because it keeps recurring and the fix is always the
same.
