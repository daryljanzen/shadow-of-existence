# `r7670` — the verdict: the new sentences hold, one understates its own theorem, and P1 carries `Δτ` under two readings

Order `r7669` asked two reads on a named tree. Thirteen claims across two objects were fixed in
`PREDICTION.md` before any bank. **8 SUPPORTED · 2 NOT SUPPORTED.** Five of seven arms HIT; one
missed; and one hit its registered condition while the finding came from the other direction.

## Object A — the new sentences

**The two-step structure is the Lean's own.** `gs_segment_stretch` calls `(hs_stretch_N …).1` on a
compact segment, so step two is built **on** step one, not beside it. All seven cited names
resolve.

**② is `r7668`'s ⑬ repaired at the root.** Step one's sentence now reads "the set of horizon
points within that distance" where it read "the stretch". That is `hs_stretch`'s actual content —
a sublevel set of `infDist` within `𝓗⁺` — and the noun no longer claims a connectedness the Lean
does not prove. **⑥ is the second uncarried part carried by admitting it:** the passage now says
in its own voice that the formal statements give eventual containment and not monotone growth in
`τ`, and no statement anywhere makes the stretch monotone. **⑤ is `r7668`'s ⑥ repaired:** the
`V`-bound is now rendered as "exceeds every bound in `V`", which is the `>` the conjunct proves,
and `gs_witness` really does **prove** `HasFutureGenerators` on the four-dimensional witness —
exhibiting the curve `s ↦ ((U, V+s), y, z)` — rather than restating `hs_witness`.

**④'s negative is accurate and well made.** "Achronal" does not occur once in the three probe
files. `HasFutureGenerators` is a *named hypothesis*, discharged only on a witness, and the passage
says the standard achronal-boundary result is not formalised in general. Naming the result rather
than gesturing at it is the right way to carry a gap, and it is now the third such gap the remark
marks by name.

### ③ — the sentence states a stronger hypothesis than its theorem needs

`HasFutureGenerators` is

```
∀ q ∈ S.H J, ∃ γ : ℝ → N, γ 0 = q ∧ ContinuousOn γ (Ici 0) ∧
  (∀ t ≥ 0, γ t ∈ S.H J ∧ S.Cau q (γ t)) ∧ Tendsto γ atTop (cocompact N)
```

— a **continuous** `γ`, each of whose points lies in `𝓗⁺` and causally after `q`, escaping every
compact set. There is **nothing relating `γ t` to `γ t'` for `0 < t < t'`**: no `CStep`, no
`ContMDiff`, and the definition's own docstring calls it "purely topological". The passage says *"a
future-directed causal curve runs in `𝓗⁺`"*, which is strictly more. **So the Lean is stronger
than advertised**, and a reader who supplied only what the sentence asks would be supplying more
than the theorem needs. That is the opposite of the mismatch this seat registered for this arm, and
it is worth saying in the remark, because the generators' future inextendibility — the standard
result the passage defers to — gives a *causal curve*, while the theorem would run on much less.

### ⑦ — "for every function `Θ`" is literal, and the paper says why

`dn_cor_densities` has **no `Θ` binder and no temporal or Cauchy hypothesis**; `Θ` is universally
quantified inside each of its four conjuncts, which are the sentence's three plus the `B`-form. The
reason the claim holds for every `Θ` is the one **the paper itself names** — "its slices taken in
`D` as here": `slice J Θ τ = {x ∈ D J | Θ x = τ}`, so the slice is inside `D` by definition, and
`D` is disjoint from the black-hole region and from `𝓗⁺` whatever `Θ` is. The statement is exactly
as strong as it looks and no stronger, and the sentence does not overclaim, because it states where
the strength comes from. `dn_witness` gives the black-hole region as the non-empty `{U ≥ 0}` with
non-empty slices, so no conjunct is vacuous; nothing in the three files models matter, so "not
formalised" holds.

## Object B — the reading of `Δτ`

**P1's text supports the ruling in seven distinct places**: the proof's own definition of `Δτ` as
"the temporal separation conjugate to [`Δx`] in the frame adapted to the same foliation"; "the
local form of the line element in a frame adapted to the foliation of (b)"; the triangle's
"temporal **leg**", which is `69`'s own word; the along-the-connection condition; `lem:killing`'s
`ds² = g(χ,χ)dλ² = |χ|²dλ²` with `λ` the Killing parameter — the Killing-horizon specialisation in
P1's own hand; `N` as P1's symbol for the lapse, collapsing as `√(1−r_h/r) → 0`; and Section 3's
statement that a vanishing lapse times a nonzero coordinate increment is "causal **order** drawn as
coordinate length, carrying no metrical duration", which is `∫N|dt|` with `N → 0` stated as physics.

**And no sentence reads `Δτ` as the null curve's own length.** The zero length belongs to `Δs`:
"their spacetime separation is zero, because the geodesic joining them is null." `Δs²`, `Δx` and
`Δτ` are three named quantities throughout. The ruling's negative half is the paper's own
distinction.

### ⑩ — two sentences read otherwise, not one

1. **`Δτ` as an endpoint difference.** *"First, the temporal separation `Δτ = τ(q) − τ(p)` assigned
   by a smooth temporal function `τ` is **not a geometric invariant**."* That `Δτ` is a difference
   of values of a temporal function at the endpoints, and P1 calls it explicitly non-invariant —
   while the proof lists its `Δτ` among *"the invariant separations named in the hypotheses"*.
   `∫N|dt(γ′)|` is neither an endpoint difference nor non-invariant, so it is not the Section-1
   object. **The symbol carries two objects.** This is the standing guard verbatim: *before two
   stretches are identified by a label, check how many-to-one the label is on the object.* Here the
   label is `Δτ` and it is two-to-one, and the two are separated by P1 deliberately — "the answer
   has two parts that must not be merged" — but under one symbol.
2. **The accumulation sentence.** *"These are not coordinate differences accumulated along some
   path between `p` and `q`."* `∫N|dt(γ′)|` **is** an accumulation along a path, of an invariant
   integrand rather than a coordinate. The sentence excludes the coordinate reading, not the
   integral — but it is the sentence a reader would cite against the ruling, and the distinction
   between accumulating a coordinate and integrating an invariant needs saying rather than assuming.

⌗ **Neither `∫N|dt|` nor `∫|χ|dλ` appears anywhere in P1.** Both are consistent with
`Δs² = Δx² − Δτ²` and with `ds² = |χ|²dλ²`, but the formulae are `69`'s construction and not the
paper's text. That is not an objection to the ruling; it is what "does P1's text support it" can
and cannot return.

## The arms, scored

| arm | registered | outcome |
|---|---|---|
| ⓵ every cited name resolves | all resolve | **HIT** — 7 of 7 |
| ⓶ `dn_cor_densities` for every `Θ` | no temporal or Cauchy hypothesis | **HIT**, and the paper names the reason itself |
| ⓷ step two's hypothesis | the named one and no more | **HIT on its condition** — no unstated hypothesis; the finding is the reverse, the Lean asks LESS |
| ⓸ the two negatives | both accurate | **HIT** |
| ⓹ `gs_witness` | exhibits the curve | **HIT** |
| ⓺ the `Δτ` reading | supported, exactly one sentence against | **MISS** — supported, but **two** sentences against |
| ⓻ the guard | three families must flip | **HIT**, with one widening recorded below |

⓷ is worth a line of its own: I registered the only interesting mismatch as a hypothesis the
sentence fails to state, and the mismatch runs the other way. *A registered arm that names one
direction of a mismatch cannot see the other.* Both ⓺'s miss and ⓷'s half-sightedness come from the
same habit `r7668` caught — a condition drawn from the shape of the question rather than from the
object — and the correction is to register the comparison, not the expected verdict.

## The guard, and the one widening

All families flipped. One rule had to be widened mid-run, and it is recorded rather than quietly
loosened: `r7666`'s requirement that every prose marker carry `\b` **refused a LaTeX-formula
marker**, since `ds^{2}=g(\chi,\chi)` has no word boundary anywhere in it. A formula marker is
anchored a different way — it contains an escaped control sequence, which cannot occur inside a
word — so the scanner now accepts exactly those two anchor forms and refuses anything with neither,
and a fourth guard probe checks that a control-sequence marker matches the real formula and **not**
a truncated variant. The exemption cannot be used to smuggle a bare substring back in, which is the
only reason it is safe to have.
