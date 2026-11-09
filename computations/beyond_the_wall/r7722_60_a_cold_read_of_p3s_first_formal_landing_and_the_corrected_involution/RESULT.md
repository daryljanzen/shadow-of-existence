# r7722 (60) — RESULT

**Order `r7719`.** Registered before measurement at `ef748bcd`, pushed before `probe.py`
existed. Readings in `runs/READINGS.txt` (exit `0`, all self-checks pass); tree in
`runs/TREE.txt`.

**THE THREE QUESTIONS, ANSWERED: ① the corrected `prop:involution` is TRUE in every conjunct,
checked by arithmetic at the endpoints it names, and NOTHING else leans on the old reading —
including two sites that look stale and are not. ② the semi-axes are STATED, between the two
declarations the clause cites. ③ the factorisation MATCHES, and "meeting exactly at" is an iff in
the statement.** **No repair routed.** ⛔ **Three defects in this probe, all one family, and one of
them was my own prediction of where the arithmetic would be delicate.**

---

## ① THE CORRECTED `prop:involution` IS TRUE

σ was read from **its own definition** at source — `σ(r₀) = (−r₀ + √(4 − 3r₀²))/2` — and every
claim computed at the endpoints the statement names, with the computation printed beside the
verdict:

| `r₀` | `σ(r₀)` | `2M = r₀ − r₀³` |
|---|---|---|
| `−1/√3` | `+1.154700538` = `2/√3` | `−0.384900179` |
| `0` | `+1.000000000` | `0` |
| `1/√3` | `+0.577350269` = `1/√3` | `+0.384900179` |
| `1` | `0` | `0` |
| `2/√3` | `−0.577350269` = `−1/√3` | `−0.384900179` |

- **1a The involution identity holds on `[−1/√3, 2/√3]`**, and — the point that makes the interval
  right rather than merely sufficient — **it FAILS below `−1/√3`**: `sup|σ(σ(x)) − x|` is
  `1.1e−08` on the interval (a square-root effect, below) against **`1.73`** on
  `[−2/√3, −1/√3)`. ✔
- **1b The exchange is exact, and the overlap I registered as the subtle part is no obstacle.**
  `σ(0) = 1` and `σ(2/√3) = −1/√3`, and the sampled image of `[0, 2/√3]` is
  `[−0.577350269, +1.000000000]` — i.e. `[−1/√3, 1]` exactly. **An involution may swap two
  overlapping sets whose union is its domain, and this one does.** ⚑ And the old statement's error
  is **exhibited** rather than asserted: `σ(2/√3) < 0`, so σ is not a self-map of `[0, 2/√3]`. ✔
- **1c On `[0, 1]`: decreasing, onto `[0, 1]`, to the other non-negative root.** Monotone over 201
  samples; image `[0, 1]`; and `cubic(2M(r₀), σ(r₀)) = 0` at every sample with `σ(r₀) ≥ 0`. The two
  ends are exact — both cubics are `r³ − r`, with roots `−1, 0, 1`, and σ swaps `0` and `1` — and
  at the fixed point `1/√3` "the other" root is itself, which is why the statement calls it the
  designated root on the merged pair. ✔
- **1d ⛔ NOTHING ELSE LEANS ON THE OLD READING — and two sites that look as though they do, do
  not.** Searched **all 55 files of `corpus/*.tex`**, flattened, for `"involution of"`,
  `"positive-root half"`, and every `2/√3` within 300 characters of `"involution"` or `"\sigma"`:
  - `"involution of <interval>"` occurs **once**, the corrected `[−1/√3, 2/√3]`; the only other hit
    is an unrelated *"involution of order two"* in the groupoid paper.
  - `"positive-root half"` occurs in P3's remark — now `(r₀ ∈ [0,1], 2M ≥ 0)` ✔ — and in **two
    generated receipt-index lines** that still read *"σ∘σ = id on positive-root half"*.
    **⚠ THOSE ARE NOT STALE, and this is where a pattern match would have produced a false
    finding.** The involution **identity** holds wherever `3r₀ + s ≥ 0`, which is automatic for
    `r₀ ≥ 0`, so it holds on **all** of `[0, 2/√3]`: `sup|σ(σ(x)) − x| = 2.2e−16` there. **What
    the old statement got wrong was the SET σ preserves, not the identity** — and the receipt the
    lines are generated from sweeps `r₀ ∈ [0, 1]`, the corrected interval, so its own assertion is
    exact.
  - every `2/√3` near σ is in P3's corrected statements or in the groupoid paper, which states
    `σ(−1/√3) = 2/√3` and that `−1/√3` is **not** a fixed point — consistent with the correction.

## ② THE SEMI-AXES ARE STATED, BETWEEN THE TWO DECLARATIONS THE CLAUSE CITES

`sl_ellipse`'s statement binds `u := (r + r₀)/√2` and `v := (r − r₀)/√2` and concludes five
things, among them the diagonalisation `r² + r·r₀ + r₀² = (3/2)u² + (1/2)v²` and **both numbers,
each paired with its eigenvalue**: `(3/2)·√(2/3)² = 1` and `(1/2)·√2² = 1`.

> **The directions are carried by the bindings**: `v = 0` is the line `r = r₀` and `u = 0` is
> `r = −r₀`. So `√(2/3)` is the semi-axis along `r = r₀` and `√2` along `r = −r₀` — **and the
> assignment is right rather than swapped, which is the one way this sentence could have failed.**

⌗ What `sl_ellipse` does not give alone is the level set that makes them semi-axes — the conic
itself — and that is `sl_locus`, **which the clause also cites.** So the semi-axes are stated
between the two cited declarations; neither alone gives them, and the sentence cites both. **Not a
consequence smuggled past a citation** — the distinction `r7718` and `r7720` both turned on.

## ③ THE FACTORISATION MATCHES `sl_nariai`

`sl_nariai`'s second conjunct is **`∀ a r, 3a² = 1 → sl_cubic (sl_g a) r = (r − a)²(r + 2a)`** —
the factorisation, for every `a` with `3a² = 1`, and the third and fourth conjuncts certify that
both `±1/√3` satisfy that hypothesis. **And "the two components meeting exactly at" is an `↔` in
the statement**, not an inclusion — the word was read and not granted.

**Checked independently by arithmetic** at both values, over 24 values of `r` each:
`sup|cubic(2M(a), r) − (r − a)²(r + 2a)| < 1e−12`, and the identity **fails** at a value not
satisfying `3a² = 1`, so the hypothesis is doing work. ✔

## ④ THE REST OF THE LANDING HOLDS

- **"Exactly on" is an iff, and it is true.** `3r₀ + s ≥ 0` at every named endpoint of
  `[−1/√3, 2/√3]` and **negative** just below its left end (`−0.1443` at `r₀ = −1.1047`). ✔ And
  the monotonicity `σ′(r₀) = −(3r₀ + s)/(2s)` is at source. ✔
- **The remark's narrowed parenthesis is right, computed from `2M = r₀ − r₀³`:** `2M ≥ 0` at `0`,
  `1/√3` and `1`, and **negative** both below `0` (`−0.385` at `−1/√3`) and above `1` (`−0.231` at
  `1.1`). **So `2M ≥ 0` exactly on `[0, 1]` within σ's domain, and the old `[0, 2/√3]` was wrong
  for `r₀ > 1`.** ✔
- **All eleven declarations exist and are cited** (names matched by skeleton). And the file flags
  the old error itself: `sl_σ_swap` states both directions of the exchange, the **image equality**
  rather than mere containment, and that `σ(2/√3) ∉ [0, 2/√3]`. ✔
- ⌗ **One consistency the two wordings keep, and it is deliberate:** `sl_σ_second` confines "the
  second **positive** root" to `[0, 1)`, which is why the formal paragraph says `[0,1)` where the
  proposition says `[0,1]` with "non-**negative** root". **At `r₀ = 1` the image is `0`, which is
  non-negative and not positive** — so the two wordings are exact, not a discrepancy. ✔
- **Zero `axiom` tokens, zero `sorry`.** ✔
- **This seat's own `r7720` repair landed as routed:** the Sbierski citation now names
  `sec:discussion`, the offered bridge clause is taken verbatim, and the wrong pointer is gone —
  searched for the old parenthetical verbatim. ✔

---

## THE REPAIRS ROUTED

**None.** The correction is sound, nothing downstream leans on the old reading, and both
citations cover what they are cited for.

## WHAT THIS PROBE CAUGHT IN ITSELF — THREE, ALL ONE FAMILY

1. **The skeleton matcher's Greek table never had `σ`.** It had `Φ Ψ η ρ τ Γ`, from the revisions
   that needed those, so **`sl_σ_σ`, `sl_σ_swap`, `sl_σ_second` and `sl_σ_fixed` could not be
   matched at all** and four citation arms failed. **The table IS the form the matcher was given**
   — the family's purest instance yet, because the instrument's blind spot was a list I wrote
   myself.
2. **`decl_header` cut the statement at the first `" := "`, and a Lean `let` binder inside a
   STATEMENT carries one.** `sl_ellipse` begins `let u := (r + r₀)/√2`, so the header stopped there
   and **everything after it — the diagonalisation and both semi-axis numbers — was invisible**,
   failing three arms of ②. **Exactly `r7720`'s defect in a new costume: a literal delimiter that
   also occurs inside what it delimits.** Fixed with a `decl_statement` reader bounded by the
   `:= by` that begins the proof, with negatives both ways.
3. **⚠ AND ONE THAT WAS MY OWN PREDICTION, NOT MY CODE.** I built the tolerance arm to excuse a
   square-root effect **at `x = 2/√3`** — and the worst error is at **`x = −1/√3`**, whose *image*
   is `2/√3`: it is the OUTER σ that takes the root of a vanishing quantity. Excluding the wrong
   endpoint left the arm failing, **and it was visible only because the arm PRINTS where the worst
   error is attained** rather than only whether it passed. Away from that one point the identity
   holds to `1.8e−15`.

**THIRTEENTH, FOURTEENTH AND FIFTEENTH INSTANCES IN ELEVEN REVISIONS: an instrument reads the FORM
it was given, not the QUANTITY.** Here: **a table I wrote**, **a delimiter inside its own
statement**, and **a prediction about where arithmetic is delicate.** ⌗ The third is the one worth
keeping: the first two are code and the third is *me*, and what caught it was a `say` that printed
the attaining point. **An arm that reports its witness and not only its verdict is the version of
"an assertion that can fail" that catches a wrong expectation as well as wrong code.**

⌗ And `r7716`'s landing defect was not repeated for a third revision: every absence claim above
names its search as it is written — 55 files, three string families, and the receipt's own sweep.
