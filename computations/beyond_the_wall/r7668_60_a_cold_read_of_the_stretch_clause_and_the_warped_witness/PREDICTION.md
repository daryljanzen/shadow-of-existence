# `r7668` — a cold read of the stretch clause's formalisation and of the warped witness

**Registered before any bank is taken.**  Order `r7667` asks two questions on a named tree, in
`r7666`'s form:

1. Is `hs_stretch_N`'s **(S1)/(S2)** a faithful reading of P1's clause *"the stretch of `𝓗⁺` they
   approach to within any given distance extending to the future without bound"*?  **Report any
   part of the clause the pair does not carry, beyond the future direction the remark already
   names.**
2. Check the remark's sentences on `hs_witness`, the warped witness and the Cotton tensor against
   the Lean — **including whether `ww_gco_bridge` really ties the computed Cotton tensor to the
   witness's own metric.**

## The tree

`runs/TREE.txt` is written before any bank and records the worktree commit, the dirty paths and
the blob hash of every file read.  Every verdict is a verdict on that tree.

## The objects

**Object A, the stretch clause**, in six claims: ① `hs_stretch_N` is a theorem of
`HorizonStretch.lean` with the form the remark gives; ② its distance hypothesis is *any* metric
inducing the manifold's topology; ③ **(S1)** every compact part of `𝓗⁺` lies within the given
distance of the cones of all sufficiently late `τ`; ④ **(S2)** when `𝓗⁺` lies in no compact set
the stretch eventually leaves every compact set; ⑤ the *future* direction, along the generators,
is not formalised in general; ⑥ `hs_witness` shows the stretch reaching every value of `V` on the
four-dimensional witness.

**Object B, the warped witness**, in six claims: ⑦ `ww_witness_headline` and
`ww_witness_tangency` give what `cy_`/`fd_` give — the Cauchy property on the manifold itself,
properness, both convergences, and tangency at every horizon point, with `𝓗⁺ = {U=0}` as
`∂J⁻(O)`; ⑧ the metric is `−dU dV + e^{2UV} dy²` on `ℝ³`; ⑨ the Cotton tensor is **computed in
Lean from the metric** and has `C_UUV = −2V`, not identically zero (`ww_cotton_ne_zero`);
⑩ **`ww_gco_bridge` ties that computed tensor to the witness's own metric**; ⑪ the
conformal-flatness ⟺ Cotton-vanishing theorem is classical and not formalised; ⑫ no conformal
extension is built for the three non-two-dimensional carriers.

**And the faithfulness reading itself**, scored separately as ⑬: the parts of P1's clause that
(S1)/(S2) do **not** carry.

## The arms

- **⓵ Every cited name must resolve** in the file the remark names.  **Registered prediction: all
  resolve.**
- **⓶ `ww_gco_bridge` must be a BRIDGE, not a restatement.**  It is faithful only if one side is
  the general computed object and the other is the witness's own metric or its components — not
  two copies of the same formula.  **Registered prediction: this is the arm most likely to fail.**
  The order singles the bridge out, and a bridge that restates its own definition on both sides is
  the tautological form this seat has shipped twice and caught twice; being asked about it is a
  reason to check it, never to trust it.
- **⓷ The faithfulness of (S1)/(S2).**  **Registered prediction: at least one part of P1's clause
  beyond the future direction is not carried** — the candidates fixed here, before reading: the
  **connectedness** of "the stretch" (P1's noun is a single portion of `𝓗⁺`, and a pair of
  limit statements about compact sets need not give one), and **monotonicity in `τ`** (P1's
  "extending" is a growth in `τ`, and eventual containment is not growth).  If the pair carries
  both, the arm misses.
- **⓸ ⑤'s negative.**  **Registered prediction: no statement of the future direction in general
  exists in `HorizonStretch.lean`** — so the remark's "not formalised in general" is accurate.
- **⓹ `hs_witness`'s reach.**  **Registered prediction: the Lean states it as a universal over `V`**,
  not as a weaker existence at one value.
- **⓺ The guard, carrying `r7664`'s and `r7666`'s repairs.**  Every verdict a function of its
  readings; a flip family re-evaluating each with its inputs negated; every prose probe an anchored
  regex on a whitespace-flattened copy, with the scanner refusing an unanchored marker and
  recording each hit's context.  **If any probe does not flip, every verdict is withdrawn.**

## What would falsify the reading

A claim scored from the prose rather than the Lean; a cited name taken on trust; a bridge accepted
without checking what stands on each side of it; a verdict on a tree other than the one
`runs/TREE.txt` names; a guard probe that does not flip.
