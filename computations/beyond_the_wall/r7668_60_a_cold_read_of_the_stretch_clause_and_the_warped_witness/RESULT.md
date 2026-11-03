# `r7668` — the verdict: the Cotton bridge is real, and the stretch pair carries the clause's content but not its picture

Order `r7667` asked two questions on a named tree. Twelve claims of the remark's two new passages,
plus the faithfulness reading itself, were fixed in `PREDICTION.md` before any bank.
**11 SUPPORTED · 2 NOT SUPPORTED.** Five of six arms HIT; **the one that missed is the one this
seat was most confident about.**

## ⓶ missed: `ww_gco_bridge` is a bridge, and this seat registered that it probably was not

I registered the bridge as "the arm most likely to fail", on the ground that the order singling it
out plus the tautological form I have shipped twice made restatement the likely answer. It is
wrong. The bridge's left side is **part A's own witness metric**, `Warped.ww_S.gE x`, evaluated on
the three coordinate basis vectors `![((1,0),0), ((0,1),0), ((0,0),1)]`; its right side is **part
B's component array** `ww_gco i j ![x.1.1, x.1.2, x.2]`, the object the whole curvature chain
starts from. Different symbols, different types, not of the form `X = X`, proved by `fin_cases` on
both indices through `ww_w_sq`. The order's doubt is answered in the affirmative.

And the chain behind it is derived at every link, not asserted: `ww_gco` → `ww_ginv` (**proved**
to be the inverse by `ww_ginv_spec`, not assumed) → `ww_Γ` (the Christoffel formula in `ww_ginv`
and `ww_gco`) → `ww_Riem` → `ww_Ric` → `ww_R` → `ww_Sch` (`R_ij − R g_ij/4`, the three-dimensional
Schouten) → `ww_covS` → `ww_Cot i j k = ∇_k S_ij − ∇_j S_ik`. Eleven links, every one of them
mentioning its parent. "Computed in Lean from the metric" is the truth about this chain, and
`C_UUV = −2V` with a point where it is `−2 ≠ 0` is exactly what `ww_cotton_ne_zero` says.

Both halves of the metric agree too: part A's `gE x v w = gM v.1 w.1 + ww_w x² (v.2 w.2)` with
`ww_w x = e^{UV}`, and part B's components `[[0,−1/2,0],[−1/2,0,0],[0,0,e^{2UV}]]` — `−dU dV +
e^{2UV} dy²` on `ℝ³`, in both.

## ⑬ — the pair carries the clause's content, not its picture

P1's clause: *"the stretch of `𝓗⁺` they approach to within any given distance extending to the
future without bound"*. Six parts; **three carried, three not**, beyond the future direction the
remark already names:

| part | verdict |
|---|---|
| "to within any given distance" | **carried** — the metric and `ε` are binders |
| "the cones approach" | **carried** — (S1) is containment in the `ε`-stretch of the cones |
| "without bound" | **carried** — (S2) is escape from every compact set |
| **"the stretch" as ONE portion** | **not carried** — nothing relates `hs_stretch` to connectedness |
| **"extending" as growth in `τ`** | **not carried** — no monotonicity in `τ` is stated |
| **"along its generators"** | **not carried** — nothing ties the stretch to a generator |

`hs_stretch A H τ ε = {q ∈ H | infDist q (A τ) < ε}` is a sublevel set of a distance. It can be a
union of far-apart pieces, and (S1)/(S2) are *eventual* statements, so the set could shrink and
regrow and still satisfy both. What the pair proves is: **a set of horizon points within any given
distance of the cones, which eventually contains every compact part of `𝓗⁺` and eventually
escapes every compact set.** That is the clause's extensional content. "A stretch" — one portion,
climbing the generators, growing with `τ` — is the clause's picture, and three of its elements are
not in the Lean. None of this is an error in P1 or in the formalisation; it is what the pair does
and does not say, which is what the order asked.

## ⑥ — "reaches every value of `V`" is an `>` reported as an `=`

`hs_witness`'s fifth conjunct is `∀ ε > 0, ∀ T : ℝ, ∀ᶠ τ in atTop, ∃ q ∈ hs_stretch …, q.1.2 > T`:
for every **bound** `T`, the stretch eventually contains a point whose `V` **exceeds** `T`. No
conjunct says the stretch contains a point at a **given** `V`. The remark's "the stretch reaches
every value of `V`" renders unboundedness above as surjectivity, and the two coincide only for a
connected stretch — the very thing ⑬ finds unproved. The two findings are one finding seen twice.

**And the remark omits the conjunct that carries the future direction on this witness.**
`hs_witness`'s last conjunct is `∀ q ∈ 𝓗⁺, ∀ K compact, ¬ ({p | Cau q p} ∩ 𝓗⁺) ⊆ K`: from **every**
horizon point, the horizon's own causal future leaves every compact set. That is a futureward
statement, proved, about the generators' direction — and the remark says the future direction is
"not formalised in general" while not saying it is formalised here beyond the `V`-reach sentence.
A reader told the direction is unformalised would want to know this conjunct exists.

## What holds

⑤'s negative is accurate: no theorem or lemma in `HorizonStretch.lean` states the generators'
future inextendibility, and the file's own header says so in writing. ⑦ the warped headline carries
the Cauchy property on the manifold itself, properness, both convergences and tangency at every
horizon point, with `ww_J = range ww_O` so `S.H ww_J` really is `∂J⁻(O)`, and the four-dimensional
headline has the same shape, so "the same holds" is exact. ⑪ the conformal-flatness criterion is
nowhere stated in the Lean and the remark marks it as classical and not included — the same
discipline it now applies to Bernal–Sánchez. ⑫ no conformal extension is defined for the warped or
four-dimensional carrier. All eight cited names resolve in the files named.

## The arms, scored

| arm | registered | outcome |
|---|---|---|
| ⓵ every cited name resolves | all resolve | **HIT** — 8 of 8 |
| ⓶ the bridge is a restatement | most likely to fail | **MISS** — it is a real bridge |
| ⓷ the pair misses part of the clause | ≥1 beyond the future direction | **HIT** — three, including both registered candidates |
| ⓸ ⑤'s negative | no general statement exists | **HIT** |
| ⓹ `hs_witness`'s reach | a universal, not an existence at one value | **HIT** on the registered condition, with the `>`/`=` slip reported beside it |
| ⓺ the guard | three families must flip | **HIT** |

⓶'s miss is worth stating plainly: I predicted a defect from the shape of the question rather than
from the object, and the object was sound. *A prediction drawn from how a question is asked
measures the question.* Two forms of this seat's standing lesson now point the same way — the one
about matchers, and this one about priors — and the correction is the same in both: the verdict has
to be a function of the thing read.

## The guard

All three families flipped: the conjunct probe pair, the anchored-marker family (carrying
`r7666`'s word-boundary assertion, which the scanner now enforces by refusing any marker without
one), and the flip family over all twelve derived verdicts. Nothing in this instrument needed
repair after the fact, which is the first time in this run.
