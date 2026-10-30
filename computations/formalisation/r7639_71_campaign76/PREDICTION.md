# `r7639+71.2` — PRE-REGISTRATION: campaign 76, `r7639` ②–③, the causal-`P` bootstrap, then differential tangency. ⌗ `700` new lines in one probe (band 250–3000 new), ⛔ stop `5000` total. ⌗ p: near-conoid estimate `0.35`, bootstrap and hence generators as null geodesics outright `0.3`, differential tangency `0.12`

*Under `r7639` ②–③. The setting is campaign 73's `probes/NullGenerators.lean`, copied in under a new namespace. No Lean
was written before this registration.*

## ① The near-conoid estimate (`probes/ConoidBootstrap.lean`)

***Statement.*** On the normal ball, for future-causal `w`, `g_x(P x, w) ≤ C·max(Q x, 0)·‖w‖`.

***Alternative form.*** Where the uniform `C` fails at `p` itself (`P(p) = 0`), the form registered instead is:
`Q⁺(γ(t)) = 0` along a causal curve from `p`, proved by a Grönwall step on `Q⁺ ∘ γ` away from `t = 0`, plus a
separate small-`t` argument.

***Route.***
- Work in normal coordinates. There, `P` is the Euler field and `g_p(P,P) = Q`, by the Gauss lemma.
- Write `w = w_∥ + w_⊥` relative to `P`.
- The sign of `g(P,w)` is controlled by `Q` through the reverse Cauchy–Schwarz inequality with a defect term.

## ② The bootstrap

***Statement.*** Along a Lipschitz causal curve from `p` in the normal ball, `P` stays in the closed future cone, so
`Q ≤ 0`.

***Consequence.*** This discharges campaign 73's "lies on `{Q = 0}`" hypothesis for achronal curves (generators), using
`ng_chr_of_Q_neg`. The generators of `𝓗⁺` are then null geodesics outright.

## ③ Stretch: differential tangency

***What it needs.***
- C¹ control of `𝓗⁺` near a point: locally it is the conoid of an earlier generator point.
- A gradient bound on `Θ` near `𝓗⁺`.

The slices' normals then converge to the generator direction's orthogonal complement.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.***
- `①`'s likely stop is the singular start at `p`. If so, RESULT states the estimate on an annulus, and names the
  small-`t` gap.
- `③` is expected to stop at the gradient bound on `Θ`, which is not implied by the hypotheses.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
