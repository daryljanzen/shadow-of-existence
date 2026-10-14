# `r7327+71.1` — PRE-REGISTRATION: the cutoff lemma (`80` lines, band 50–130), then the row-45 `S²` pilot (`150`, band 100–220, ⛔ stop over `250`), then the split of the probe into an importable engine module plus instance files. ⌗ Every band is failable, and the whole reachable outcome space decides something

*Orders: `FOR_71.md` §`r7327` ④, in that sequence and no other. Written before row 45's receipt is opened and before
any Lean. What I know of row 45 is its one-line stand-in, "SdS Kretschmann from Riemann", and its place in
`ROWS.tsv`. I have read `mathlib`'s `ContDiffBump` API (`Analysis/Calculus/BumpFunction/Basic.lean`), and that read
is disclosed: it gives `=1` near the centre, a support in a ball, and smoothness.*

## ① The cutoff lemma — `r7327` ④.1

***Statement (fixed now):*** for `E` finite-dimensional, `f : E → ℝ` smooth on an open ball around `p` with
`f p ≠ 0`, there is `g : E → ℝ` that is smooth everywhere, never zero, and equal to `f` near `p`.
- ***Construction, as `r7327` names it:*** `g = φf + (1 − φ)·s`. Here `φ` is a `ContDiffBump` whose support lies
  inside a ball where `f` has the sign `s` of `f p`.
- The one step not in `mathlib` is that `φf` is smooth everywhere. On the ball that follows from `f`. Off `tsupport φ`
  it is eventually `0`.
- ***The lemma closes the caveat carried since B:*** "whether such a global profile exists is not proved for each named
  metric." A second lemma states it in the shape the instances use: a profile family `c : Fin 4 → (Fin 4 → ℝ) → ℝ`,
  each smooth and nonzero near `p`, gets a global, nowhere-zero, smooth family equal to it near `p`.

| | predicted |
|---|---|
| lines | ***`80`*** (band 50–130) |

## ② The row-45 pilot — `r7327` ④.2

- SdS in `(t, r, θ, φ)`: `c = (−f(r), 1/f(r), r², r² sin²θ)`, with profiles in TWO coordinates `(r, θ)`. That is E5's
  first use on a sphere.
- The claim is the Kretschmann scalar, a full contraction, so it gets a component table, as E3 did.
- It is stated with the convention: profiles equal to the named ones near a point with `r ≠ 0`, `f(r) ≠ 0`,
  `sin θ ≠ 0`. With ①, existence is now a theorem rather than a caveat.
- ***Model, from `r7323`:*** setup `20` + four profiles at ≈ `20` each (`f`, `1/f`, `r²`, `r² sin²θ`) + statement `15`
  + a 256-term table `20` + the two-coordinate overhead `25` ≈ ***`160`***. I register ***`150`*** (band 100–220).
- ⛔ ***STOP over `250`.*** Then the reopening of the `24` stays a reading, and I say where it failed. ***If it fails,
  I expect it on the profile's `θ`-dependence through E5:*** a mixed `∂_r∂_θ` of `r² sin²θ`, or the table's size with
  two live coordinates. I will name which.

## ③ The split — `r7327` ④.3

- `CurvatureProbe.lean` becomes `ShadowEngine.lean` (the engine core, E2, E5, the recipes, the cutoff lemma) and is
  imported by instance files.
- ***Measured as:*** NEW lines (headers, `import`s, `namespace` glue). Moved lines are counted separately and are not
  added to either. ***Predicted: `≤ 40` new lines***, and an instance file building in ***under `2` minutes*** once the
  module is compiled.
- ***Failable:*** if moving the code changes any `#print axioms` line, or any theorem stops building, the split has
  failed, and I revert it rather than patch around it.

## ⛭ Failability, and the decisive fraction of the outcome space (`r7325` ③, `r7327` ⑥)

- ***Every band is failable at the size it will be scored at:*** each is one census line count, read exactly, with no
  sampling.
- ***The fraction of the reachable outcome space that decides something is ALL of it.*** For each count, every value
  lands under, in, or over its band, and each of the three is a distinct reading:
  - under means the model over-prices;
  - in means the model holds;
  - over means a driver is missing.
- The pilot's stop splits "over" into "over but under `250`" (the reopening proceeds and is re-priced) and "over
  `250`" (the reopening stays a reading). ***No value of any count leaves the question undecided.***

## ④ My probabilities

| quantity | p |
|---|---|
| the cutoff lemma lands in `50`–`130` | 0.7 |
| the pilot lands, at all | 0.85 |
| the pilot lands in `100`–`220` | 0.6 |
| the stop fires (over `250`) | 0.1 |
| the split adds `≤ 40` new lines and changes no axiom line | 0.8 |

## Then

- ***`r7327` ④.4:*** `CANDIDATES.md` is corrected only after the pilot, by an appended note, with the registered
  text kept.
- I tell node 66 when the lemma and the pilot are in, so the second seat can be started.
- Nothing in the quote-pin stride. The `21` calibration keys are untouched.
