# `r7666` — a cold read of the revised `rem:formalised`, and of the corrected proof sentence

**Registered before any bank is taken.**  Order `r7665` asks for two objects, in `r7664`'s form,
on a named tree: the revised remark against `cd_prop_causal_alignment`, `mx_H_eq_boundary` and the
witness theorems it names; and the proof sentence of `prop:causal-alignment` that begins *"No past
light cone of an exterior event meets `𝓗⁺`"* against `cd_cone_disjoint` and
`cd_closure_Jpast_inter_H` — **is each step the Lean's, and is any step the Lean needs missing
from the prose?**

## The tree

`runs/TREE.txt` is written before any bank and records the worktree commit, the dirty paths, and
the blob hash of every file read.  Every verdict is a verdict on that tree.

## The objects

**Object A, the remark**, decomposed into **twenty-three** claims: ① the attestation and the three
theorem names it cites; ② the setting as Hausdorff, `C¹`-atlas, arbitrary real normed model, *so
that the theorem holds in every dimension*; ③ the metric and orientation on an open `M`, `C¹` and
continuous in a chart about each point; ④ the extension's seven parts, `dι` carrying the time
orientation among them; ⑤ causal curves as chains of `C¹` causal arcs; ⑥ `D = I⁻(J)` and
`𝓗⁺ = ∂J⁻(J)`; ⑦ the hypotheses on `O` and `Θ`; ⑧–⑫ the **five** things claimed proved — the
identification, properness, the Kuratowski clause, *no past light cone meets `𝓗⁺`*, and tangency
with the frame conditions and the chart at `q` now stated; ⑬ *assumes* — three carriers and the
worldline's derived; ⑭ *does not use*, now extended to the atlas; ⑮ global hyperbolicity through
`hΘ` with Bernal–Sánchez cited as **not** included; ⑯ the one clause left out; ⑰ the 2d Rindler
witness with `cd_witness`; ⑱ the oscillating slicing failing **both** the rate condition and the
tangency; ⑲ the compactification, its compact closure, its proper image and `cz_Ω_nonconst`;
⑳ the `F`-family, its non-vacuity, and the curved tangency with `F = e^V` differing; ㉑ the three-
and four-dimensional witnesses; ㉒ the identification exercised in two dimensions only; ㉓ no
non-conformally-flat witness.

**Object B, the proof sentence**, decomposed into **four** steps: ㉔ the assertion itself; ㉕ the
`I⁻(x) ⊆ I⁻(O(τ))` step and `Θ < Θ(O(τ))` on it; ㉖ the contradiction from the Cauchy property
along a future-inextendible curve; ㉗ the conclusion that neither `J⁻(O(τ))` nor its boundary meets
`𝓗⁺`.

Each claim is scored **SUPPORTED**, **NOT SUPPORTED** or **UNMEASURED BY THIS SEAT**, never from
the prose's own wording.

## The arms

- **⓵ Every cited name must RESOLVE.**  The remark cites theorems by name and by file.  A name that
  is not a theorem in the file named is NOT SUPPORTED, and a name whose file is wrong is reported
  as such.  **Registered prediction: every cited name resolves in the file named.**
- **⓶ The binder census of `cd_prop_causal_alignment`**, every binder mapped to a sentence.
  **Registered prediction: ZERO unaccounted.**  `r7664` found three carriers assumed where the
  remark named two, one of them derived; ⑬ now names exactly three and says the worldline's is
  derived, so the census should close.  If a binder has no sentence, ⑬ is NOT SUPPORTED.
- **⓷ The conclusion census.**  The remark claims **five** things of a conclusion that should now
  carry **eight** conjuncts — `mx_prop_causal_alignment`'s seven plus the cone clause.
  **Registered prediction: the five cover all eight and none is lost.**
- **⓸ ⑪'s ground.**  "Rests on the Cauchy property of `Θ`" is checkable: `cd_cone_disjoint` must
  take the Cauchy-temporal hypothesis among its binders.  **Registered prediction: it does.**
- **⓹ The two omissions this seat supplied must now be true of the NEW theorem's own ambient
  instances**, not inherited from the old file: `ConeDisjoint.lean`'s variable block must carry
  `IsManifold … 1` and no finite-dimensionality.  **Registered prediction: both hold.**
- **⓺ The proof sentence, in both directions.**  Each of its four steps against the two named
  theorems, and then the reverse: a hypothesis or step the Lean needs that the prose does not
  state.  **Registered prediction: at least one step the Lean needs is missing from the prose.**
  This is the arm registered as most likely to decide the order, because a corrected one-line
  argument is exactly where a needed step goes unwritten.
- **⓻ The guard, carrying `r7664`'s three repairs.**  Every verdict is a function of its readings;
  a flip family re-evaluates each derived verdict with its inputs negated; every prose probe runs
  on a whitespace-flattened copy; and a true/false probe pair runs through the conjunct machinery.
  **If any probe does not flip, every verdict in this receipt is withdrawn.**

## What would falsify the reading

A claim scored from the prose rather than the Lean; a binder or conjunct not enumerated from the
source; a cited name taken on trust; a verdict on a tree other than the one `runs/TREE.txt` names;
a guard probe that does not flip.
