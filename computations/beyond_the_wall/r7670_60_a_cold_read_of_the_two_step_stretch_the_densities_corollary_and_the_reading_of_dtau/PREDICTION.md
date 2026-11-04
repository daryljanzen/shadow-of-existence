# `r7670` — two cold reads: the two-step stretch and the densities corollary, and the reading of `Δτ`

**Registered before any bank is taken.**  Order `r7669` asks two reads on a named tree, in
`r7668`'s form.

## Object A — the new sentences

1. The **two-step stretch passage** of `rem:formalised` against `hs_stretch_N`,
   `gs_segment_stretch`, `gs_future_stretch`, `gs_witness` and `hs_witness`.
2. The **corollary's last sentence** against `dn_cor_densities` and `dn_witness`.

Seven claims, fixed here: ① the passage's two-step structure, step one being `hs_stretch_N`;
② step one's content, now written as *"the set of horizon points within that distance"* rather
than *"the stretch"*; ③ step two's hypothesis — *if from each horizon point `q` a future-directed
causal curve runs in `𝓗⁺` and leaves every compact set* — and its two conclusions, every finite
segment eventually within the distance of the cones, and the set eventually containing points of
`J⁺(q) ∩ 𝓗⁺` outside any given compact set; ④ that the generators are such curves is the standard
achronal-boundary result, **not formalised in general**; ⑤ on the four-dimensional witness it is
proved and the stretch exceeds every bound in `V`; ⑥ the explicit disclaimer that the formal
statements give eventual containment and **not** monotone growth in `τ`; ⑦ the corollary's
sentence — machine-checked **for every function `Θ`**, slices taken in `D`, no slice meeting the
black-hole region, `𝓗⁺`, or any set inside that region, with a witness whose black-hole region is
the non-empty `{U ≥ 0}`, and the matter statements not formalised.

## Object B — the reading of `Δτ`

`69` has ruled, for `71`, that `Δτ` is the temporal leg `∫N|dt|` of the frame adapted to (b)'s
foliation — `∫|χ|dλ` on a Killing horizon — and **not the null curve's own length**.  The question
is whether P1's text supports that, and **any sentence of P1 that reads otherwise**.  Six claims:
⑧ the proof's own definition of `Δτ`; ⑨ the sentence that the quantities *"are not coordinate
differences accumulated along some path between `p` and `q`"*; ⑩ the along-the-connection remark's
condition on the whole connection; ⑪ *"the local form of the line element in a frame adapted to the
foliation of (b)"*; ⑫ the *"temporal leg"* of the isosceles right triangle; ⑬ the generators at
constant areal radius along their entire length, and `lem:killing`'s reading of the adapted time.

## The arms

- **⓵ Every cited name must resolve** in the file the paper names.  **Registered prediction: all
  resolve.**
- **⓶ `dn_cor_densities`'s *"for every function `Θ`"*.**  **Registered prediction: it carries no
  temporal and no Cauchy hypothesis on `Θ`**, and the claim's strength comes from the slices being
  taken inside `D`, which makes the disjointness from `𝓗⁺` and from the black-hole region a
  consequence of `D`'s own definition rather than of anything about `Θ`.  I will report that as the
  reason the sentence is true, not as a defect — a statement that holds for every `Θ` because its
  object is `D` is exactly as strong as it looks and no stronger.
- **⓷ Step two's hypothesis must be the named one and no more.**  **Registered prediction:
  `gs_segment_stretch` and `gs_future_stretch` assume a future causal curve in `𝓗⁺` leaving every
  compact set, and nothing further.**  If either carries a hypothesis the sentence does not state,
  that is a finding.
- **⓸ The two negatives.**  **Registered prediction: no achronal-boundary theorem anywhere in the
  probe files, and no monotonicity statement about the stretch** — so ④ and ⑥ are accurate, and ⑥
  is the disclaimer `r7668` asked for, now carried in the paper's own voice.
- **⓹ `gs_witness` must PROVE the generator property on the four-dimensional witness**, not restate
  `hs_witness`.  **Registered prediction: it exhibits the curve.**
- **⓺ The `Δτ` reading.**  **Registered prediction: P1's text SUPPORTS the ruling, and exactly one
  sentence reads against it** — *"These are not coordinate differences accumulated along some path
  between `p` and `q`"*, which excludes coordinate accumulation rather than invariant integration,
  since `∫N|dt(γ′)|` is not a coordinate difference.  If more than one sentence reads against it,
  or none does, the arm misses.  ⌗ *`r7668`'s lesson applies to this arm by name: a prediction drawn
  from how a question is asked measures the question.  `69` asks whether the text supports a reading
  `69` has already ruled; the verdict has to come from the sentences.*
- **⓻ The guard, three families.**  Every verdict a function of its readings; a flip family
  re-evaluating each with its inputs negated; every prose probe an anchored regex, the scanner
  refusing an unanchored marker and recording each hit's context.  **If any probe does not flip,
  every verdict is withdrawn.**

## What would falsify the reading

A claim scored from the prose rather than the Lean, or from `69`'s ruling rather than P1's
sentences; a cited name taken on trust; a verdict on a tree other than the one `runs/TREE.txt`
names; a guard probe that does not flip.
