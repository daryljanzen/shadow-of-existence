# `r7666` — the verdict: the revised remark holds almost everywhere, and the corrected proof sentence reaches the Lean's conclusion by a route that is not the Lean's

Order `r7665` asked for two objects on a named tree. Twenty-three claims of the revised
`rem:formalised` and four steps of the corrected proof sentence were fixed in `PREDICTION.md`
before any bank. **24 SUPPORTED · 2 NOT SUPPORTED · 1 UNMEASURED BY THIS SEAT**, and **all seven
registered arms HIT** — the first time in this line's recent run that none missed.

## The repairs hold

Every one of `r7664`'s six is carried, and carried in the Lean's own terms:

- **③/④** the extension is now stated with all eight of `ConformalExtension`'s fields, `timeOrient`
  and `maps_M` among them, and the setting says "on an open region `M`", which is where
  `MSpacetime`'s Lorentzian conditions actually live.
- **⑧** the double equality is split between the theorem that carries each half; `S.H (range O)`
  is still absent from `cd_prop_causal_alignment`'s conclusion, and the sentence no longer claims
  otherwise.
- **⑫** the tangency clause states `FrameHyp`'s second half — `dΘ` positive on the frame's future
  causal cone — and that the covector is read in the chart at `q`.
- **⑬** three carriers, named as three, with the worldline's stated as derived. This was the arm
  this seat itself got wrong at `r7664` (`𝒥⁺`'s carrier went unnamed in my own report), and the
  remark now names it.
- **⑮** the Bernal–Sánchez equivalence is cited and marked as *not* included in the formal
  statement — the right repair, since no theorem in the six probe files mentions hyperbolicity.
- **⑲/㉒** the cylinder's unproved reason is dropped and only the fact kept.

Two of my five omissions are now checkable on the **new** theorem's own ambient instances rather
than inherited: `ConeDisjoint.lean`'s variable block is `[NormedAddCommGroup E] [NormedSpace ℝ E]`
with `[IsManifold 𝓘(ℝ,E) 1]` on both carriers, and `FiniteDimensional`/`CompleteSpace` occur zero
times in all six files. And `cd_prop_causal_alignment`'s binders are **identical** to
`mx_prop_causal_alignment`'s, so the eighth conjunct costs no hypothesis — which is what "adds the
clause" ought to mean and does.

The remark's **five** claimed conclusions cover all **eight** conjuncts with none uncovered: the
identification, properness, the four Kuratowski conjuncts, the cone clause, and tangency. `69`'s
sharpening of my ⑳ is also better than what I wrote: "a witness whose metric is not conformally
flat is not yet built" names the condition that actually fails, where I had written "a curved one
beyond conformal rescaling".

## ⑲ — the sentence asserts an equation and cites two theorems that do not contain it

`cz_witness_headline` gives the compact closure and `range ι ≠ univ`; `cz_Ω_nonconst` gives
non-constancy by evaluating `Ω²` at three points. **Neither contains the formula
`Ω² = 1/[(1+U²)(1+V²)]`.** It is `cz_Ω_sq` (and `cz_ΩF_sq`) in the same file, cited nowhere. One
citation away from being right, and the only claim in the remark that points at a theorem for
something the theorem does not say.

## ㉖ — the proof sentence's conclusion is the Lean's; its argument is not

The sentence's assertion (㉔) is `cd_cone_disjoint` exactly, and its closing clause (㉗) —
"neither `J⁻(O(τ))` nor its boundary" — is `cd_closure_Jpast_inter_H`, which is precisely the
boundary case `r7665` says campaign 91 found the old one-liner missing. Both land.

But the **route** does not. The prose argues: a past-directed timelike curve from `x` lies in
`I⁻(x) ⊆ D`, is future-inextendible in `D`, and the Cauchy property makes `Θ` grow without bound.
The Lean never constructs a curve from `x` — its curves run *into* points of `M` — and it does not
go through unboundedness of `Θ`. It goes

> Cauchy → **future**-Cauchy (`me_futCauchy_of_cauchy_N`, by gluing a past extension) → `int J⁻(J) ⊆ D` (`mh_hint`) → **properness** (`mh_sublevelProper`, a blow-up at a horizon point, needing `[T2Space N]` and `𝓗⁺ ⊆ M`) → the closure-of-sublevel step (`mh_past_step`, `cd_chr_of_mem_closure_Jpast`, `cd_mem_closure_sublevel`) → `closure J⁻(p) ∩ M ⊆ D` → `𝓗⁺ ∩ D = ∅` (`mh_not_mem_D_of_H`).

**Nine of the ten links that chain needs are not in the sentence.** The two that matter most:

1. **`𝓗⁺ ∩ D = ∅` is never stated**, and the prose's curve is future-inextendible *in `D`* only
   because `x ∉ D`. The step the argument turns on is the step it omits.
2. **Properness is never mentioned**, and it is the Lean's load-bearing input. The remark's ⑪ says
   the clause "rests on the Cauchy property of `Θ`, **as in the proof above**". The first half is
   the Lean's — `cd_cone_disjoint` takes `hΘ` and its own docstring records that `hadapt` is not
   used. The second half is not: the Lean does not follow this proof.

Also unstated: `𝓗⁺ ⊆ M`, Hausdorffness, and the openness/push-up step that turns "`x` in the
closure of `J⁻`" into a statement about `I⁻(x)`, which the prose asserts rather than argues.

**And the sentence immediately before it has no Lean counterpart at all.** "By global hyperbolicity
of `D`, each level set `S_τ` meets the past light cone `J⁻(O(τ))` in a smooth spacelike
hypersurface, and `∂J⁻(O(τ))` is a null hypersurface" — `hypersurface` and `spacelike` occur zero
times in `ConeDisjoint.lean`, and the Lean assumes only `C¹`, so neither smoothness nor
hypersurface structure is available to it. The corrected argument does not use that sentence, which
is why the correction works; but it stands at the head of a proof the remark says the formal
statement follows.

## ① what this seat cannot decide

The axiom claim needs `#print axioms`' **output** and there is no toolchain here. Measurable, and
not reported as the claim: the audit is requested for all three of the new theorems among 74
`#print axioms` lines in `ConeDisjoint.lean`, and `sorry`/`admit`/`native_decide`/`axiom` number
zero across the six probe files. All eighteen theorem names the remark cites resolve in the files
it names.

## The arms, scored

| arm | registered | outcome |
|---|---|---|
| ⓵ every cited name resolves | all resolve | **HIT** — 18 of 18 |
| ⓶ binder census | zero unaccounted | **HIT** — and the binders match the old theorem's exactly |
| ⓷ conclusion census | five cover all eight | **HIT** — none uncovered |
| ⓸ the cone clause's ground | `cd_cone_disjoint` takes the Cauchy hypothesis | **HIT** |
| ⓹ the two omissions on the NEW file | `C¹` atlas, no finite dimensionality | **HIT** |
| ⓺ the proof sentence | at least one needed step missing | **HIT** — nine of ten |
| ⓻ the guard | three families must flip | **HIT** — and one of them caught this instrument |

## What the guard caught in this instrument

The chain scanner's first draft matched markers as bare substrings, and `'proper'` matched inside
**"the Cauchy pro*perty*"** — scoring properness as present in a sentence that does not contain
the word. That is the understating direction: a loose matcher made the finding look smaller than
it is, exactly as `r7660`'s group-name scraper did. Every marker is now an anchored regex, the
scanner refuses any marker without a word boundary, each hit is recorded with the text around it so
it can be audited, and a third guard probe asserts that `\bproper\b` does **not** match "the Cauchy
property". With the repair the count went from seven missing links to nine.

*A matcher loose enough to mis-read its own input answers about the matcher* — fifth form, and the
first time it has been caught inside the same revision that introduced it.
