# r7908 (60) — THE CORRELATIONS *FALL* ALONG THE PROFILE, THE STRONG EXPECTATION IS REFUTED, AND `r7904`'s UNREGISTERED HEADLINE IS WITHDRAWN: IT COMPARED TWO LIKELIHOODS

This seat's own item on the fork `r7904` routed to `69`, taking the recommended branch. Registered in
`PREDICTION.md` and **pushed** before the first interior entry existed. **Outcome `Ⓟ⓸ + Ⓝ⓷`.**
Receipt arms: `5` gates, `0` failed.

## The three points, one function

| | Σ (eV) | `ρ(Σ,H0)` | `ρ(Σ,Ω_m)` | `ρ(Σ,ω_b)` | `ρ(Σ,n_s)` | `σ(Σ)` eV | `R` |
|---|---|---|---|---|---|---|---|
| `Ⓞ` | `0.00` | `+0.318326` | `−0.155486` | `+0.511698` | `+0.485608` | `0.0545938` | `1.280436` |
| `Ⓐ` | `0.06` | `+0.405646` | `−0.235365` | `+0.505120` | `+0.467824` | `0.0510339` | `1.264440` |
| `Ⓑ` | `0.30` | `+0.391008` | `−0.225727` | `+0.494984` | `+0.434296` | `0.0479808` | `1.235741` |

`Ⓞ` reproduces `r7904`'s recorded block **entry for entry at exactly zero difference**, through this
module's own code path — which is what makes the three points one measurement.

## ① `Ⓟ⓸`: the correlations FALL

`Δρ(Σ, ω_b) = −0.016715` and `Δρ(Σ, n_s) = −0.051311` from Σ = `0` to Σ = `0.30`. The tilt's crosses
the registered `−0.05`, so the outcome is the FALL branch. ⇒ *The instrument becomes LESS degenerate
against both parameters the reference holds as the sum grows, not more.* `Ⓝ⓷`: the degradation factor
is intermediate at both interior points and falls as well, `1.280436 → 1.264440 → 1.235741`.

⌗ *The registration attached NO expectation to `Ⓟ`, on the stated grounds that a plausible story ran
each way and a story that runs both ways is not grounds. That was the right call: the direction is
information precisely because nothing was committed to it.*

## ② ⛔ THE STRONG EXPECTATION IS REFUTED, AND NOT NARROWLY

`PREDICTION.md` put STRONG grounds on `σ(Σ)` GROWING along the profile. It **falls**, from
`0.0545938` to `0.0479808` eV between `Ⓞ` and `Ⓑ` — a factor of `0.878868`. Unregistered, read at
every node `r7888` banked, it falls **monotonically** across all eleven, `0.0545938` eV at Σ = `0`
down to `0.0443392` at Σ = `0.60`; so do both named correlations.

## ③ ⛔ AND THAT REFUTATION FORCED THE REAL FINDING: `r7904`'s UNREGISTERED HEADLINE IS WITHDRAWN

`r7904` reported, unregistered, that the local reading of the limit falls `43.67255` meV short of the
profile's own crossing, and read that as *the limit being set by the profile above its minimum rather
than by the curvature at the origin*. **A monotonically tightening curvature makes that story
impossible**, which is what sent me to look at what the two numbers were actually quantities of.

⛔ **They are quantities of two different likelihoods, under one label.**

- **This block is `chi2_cmb`:** `555` CMB bandpowers, five parameters, nothing else.
- **`r7888`'s crossing is read on `Model6.chi2`:** `Model3.chi2(…, bao=True)` — so the same CMB score
  **plus a BAO term** — **plus a lensing likelihood plus a tau prior**, over **six** parameters, the
  sixth being `tau`, which is the fifth entry of every `x_at_node` and sits near `0.054` throughout.

**The right test is inside ONE object, and the record already carries it:** read the profile's own
curvature from the profile's own `Δχ²` values.

| a parabola about the minimum on | vertex (eV) | `σ` (eV) | the crossing it implies |
|---|---|---|---|
| `3` nodes | `0.075977` | `0.066280` | `185.0880` meV |
| `5` nodes | `0.076143` | `0.070292` | `191.8589` meV |
| `6` nodes | `0.076497` | `0.071419` | `194.0674` meV |
| **the profile's OWN crossing** | | | **`193.5453` meV** |
| the CMB-only block at the same node, for contrast | | `0.0510339` | `144.0125` meV |

⇒ **The profile's own curvature accounts for its own crossing**: `193.5453` meV sits inside the
`[185.0880, 194.0674]` meV range the three fits span. *So there is no shortfall to explain. `r7904`'s
sentence is withdrawn here rather than left standing: the `43.67255` meV was a CMB-only
five-parameter `σ` extrapolated against a six-parameter CMB+BAO+lensing+tau crossing, and the
arithmetic was right while the object was not.*

⌗ **This is the many-to-one-label guard biting on my own work.** `r7904` located a sentence's
quantity by its name — "the limit", "`σ(Σ)`" — without establishing which likelihood each belonged
to. The guard says to check how many-to-one the label is **before** the two are identified; I checked
it on `r7906`'s share and not on `r7904`'s limit.

## The controls

- `Ⓒ⓵` The Σ = `0` block **reproduced entry for entry** against `r7904`'s record, worst absolute
  difference exactly `0` over `25` entries.
- `Ⓒ⓶` **The clamp measured as its PRESENCE, not its size.** Below Σ = `0` the direction splines are
  frozen, so `binned`'s whole Σ-dependence there is the base spline's: that identity departs by
  `3.488e-14` below zero (double-precision cancellation) against `1.175e-04` above it, a factor of
  `3.37e+09`. ⛔ *Two earlier forms of this gate FAILED and both are reported: the first compared the
  one-sided-derivative disagreement at the origin (`4.638e-05`) with the interior points
  (`2.194e-06`, `2.136e-06`) and demanded a factor of a hundred, getting twenty-one — a bar on a
  quantity that mixes kink with curvature, and an invented factor. The second demanded the identity
  hold at exactly zero, which cancellation forbids.*
- `Ⓒ⓷` Each point's four parameters read out of `r7888`'s record at that node, never typed;
  `χ²_cmb` `538.2666`, `544.1528`, `824.5779`.
- `Ⓒ⓸` Every block symmetric and positive definite before any correlation is read from its inverse.
  ⌗ *No conditioning bar is registered — `r7904` established that one on a Fisher block is
  unit-dependent, and the lesson is applied rather than repeated.*
- `Ⓒ⓹` The observed Hessian run as a **convergence check at the loci the verdict uses only**, on a
  step ladder whose plateau is shown, with **no bar on the rest of the matrix** — because `r7904`'s
  bar failed for treating the Fisher matrix and the observed Hessian as one object. At the plateau the
  two routes read `ω_b` `+0.446912` against `+0.505120` at `Ⓐ` and `+0.464814` against `+0.494984` at
  `Ⓑ`, which is the residual-curvature term and is reported as its size.

## What is not claimed

- **No mechanism and no limit.** `r7888`'s `193.545` meV is untouched and no crossing is read here.
- **Nothing about the reference**, whose block on the same mask has not landed. The comparison stays
  **named as waiting**.
- ⚠ **The withdrawal in ③ is about MY sentence, not about `r7888`'s limit**, which is unaffected: its
  profile is accounted for by its own curvature, which is a fact in its favour and not against it.
- ⚠ **This is still the instrument AS USED**, and at Σ = `0.30` the `x4` deviations are larger than at
  the origin, so the quadratic truncation in the four parameters does more work there. Stated in the
  registration and repeated here.
- **The branch of the fork not taken** — `Ⓡ⓵`, the per-bin weights of order `r7895` item ③ — is now
  the only live one on this thread, because `Ⓟ⓸` closes the local reading in both directions.
