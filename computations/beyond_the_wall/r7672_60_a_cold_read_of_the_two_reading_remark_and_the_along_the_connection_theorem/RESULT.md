# `r7672` — the verdict: the two readings are now related correctly, the attestation sentences understate their own theorems in one direction and overstate them in another, and the collision the remark inherited is now verbal

Order `r7671` asked a cold read of the along-the-connection remark's new sentences on a named tree,
in three directions. Seven claims plus the residue question were fixed in `PREDICTION.md` before
any bank. **5 SUPPORTED · 3 NOT SUPPORTED.**

## What the repair gets right

**① the reading and the Lean's definition agree to the symbol.** `Δτ` is "the temporal leg
accumulated along it", written `Δτ = ∫N|dt|`, and the Lean's is
`def Δτ := ∫ s in 0..1, σ.n s * |σ.dt s (vel γ s)|`, with `Δx := ∫ √(h(γ′,γ′))` beside it. Both are
**integrals along the curve**, not endpoint differences, and the remark's reason — the geodesic
staying at one value of the invariant spatial coordinate, so running along the frame's own time
direction — is the clause that makes an integral the right object. **②** the Killing-horizon form
`∫|χ|dλ` is now written, and `lem:killing`'s own proof carries `ds² = g(χ,χ)dλ²`, so the
specialisation is in the lemma it is cited to; `r7670` found it consistent but unwritten.
**③** the invariance of the integrand and the non-coordinate character are stated in one clause.
**④** the arbitrary-temporal-function separation is named as staying non-invariant, cited to
`cor:threefold`(iv), which does say it. **The two readings are now related in one place, which is
`r7670`'s ⑩ repaired.** Of the ten sentences of P1 that use the symbol, **every one is covered by
one of the remark's four accounts** — the residue over that set is **zero**.

**⑦** `ac_witness` carries both halves and more: `g(χ,χ) = UV`, `χ` the velocity, the velocity null
and non-zero, the lapse vanishing along the whole curve, `∫dt(γ′) = 1` so the Killing parameter
still separates, `Δτ = 0`, and `γ 0 = (0,1) ≠ (0,e) = γ 1`. `χ` is **proved** Killing. And
`ac_witness_no_positive_lapse` closes the circle — along this curve **no** positive-lapse splitting
satisfies (a) and (b), so the vanishing is forced, not chosen. That is the sharper half, and the
remark does not name it.

## ⑤ — the attestation understates the generality and misstates the hypotheses

**Understated:** "machine-checked on any manifold" is true and then some. At
`ac_metric_singularity_along`'s line only `[TopologicalSpace N]` and `[ChartedSpace E N]` are in
force — the `[IsManifold 𝓘(ℝ,E) 1 N]` instance is declared **later in the file** — and
`FiniteDimensional` and `T2Space` occur zero times. It holds without even a `C¹` atlas.

**Misstated, two ways.** Binders: `S γ σ ha hb hcont`.

1. **`hcont` is a fourth hypothesis the sentence does not state** — continuity of
   `s ↦ h s (γ′ s) (γ′ s)` on `[0,1]`. It is not implied by the splitting, whose `h` is an
   arbitrary field, and it is load-bearing: it is what lets `Δx = 0` give `h(γ′,γ′) = 0`
   *pointwise*. `AdaptedSplitting` also carries `h_nonneg`, which `g = h − N²dt²` does not say.
2. **"along a `C¹` curve" is spurious.** The theorem imposes **no** differentiability class on `γ`;
   `vel` is `mfderiv`, defined regardless.

And the conclusion is **three** conjuncts, not one: `Δτ = 0`, `n·dt(γ′) = 0` pointwise, and
`h(γ′,γ′) = 0` pointwise — (b) recovered pointwise from its integral form.

## ⑥ — "force `p = q`" is conditional, and the hypothesis doing the work is unnamed

`ac_lapse_pos_forces_point`'s binders are `S γ σ ha hb hcont hn hpd`. Besides `hn` (`0 < n`) it
carries **`hpd`: each `h s` positive definite on `ker dt s`** — and `hpd` is what turns
`dt(γ′) = 0` into `γ′ = 0`. The sentence does not state it. And `γ 1 = γ 0` is not a conjunct but
the **consequent of an implication**, holding for `γ` manifold-differentiable on `[0,1]`, which
"force `p = q`" reads as unconditional. This theorem, unlike the first, does sit after the
`IsManifold` instance, so the `C¹` atlas is needed **here** and not **there** — a distinction "on
any manifold" flattens across the two.

## ⑧ — the residue is zero over the symbol, and the one sentence left is now a verbal collision

Computed, not asserted: all ten `Δτ` sentences are covered. **But the sentence the order names is
not in that set, because it does not use the symbol** — the proof's *"These are not coordinate
differences accumulated along some path between `p` and `q`"*. The remark answers its **coordinate**
half ("it is not a coordinate difference") and not its **accumulation** half, while the remark
itself now says `Δτ` is "the temporal leg **accumulated along** it". The two sentences use the same
word for opposite purposes, two paragraphs apart. At `r7670` the collision was latent; it is now
verbal. One clause in the proof — that an invariant integrated along the connection is not what
"accumulated" excludes — would close it.

## The arms, scored

| arm | registered | outcome |
|---|---|---|
| ⓵ cited names resolve | all | **HIT** — 3 of 3 |
| ⓶ hypotheses as stated, `Δτ` an integral | both | **SPLIT** — integral **HIT**, hypotheses **MISS** (`hcont` extra, `C¹` spurious) |
| ⓷ `p = q` from `N > 0` | concluded on endpoints | **HIT on its condition**, with `hpd` and the implication unanticipated |
| ⓸ the witness | both halves | **HIT**, and more |
| ⓹ "on any manifold" | true of the ambient instances | **HIT**, understated |
| ⓺ the residue as a comparison | compute it, whatever the size | **HIT** — zero over the symbol, and the named sentence falls outside the symbol set entirely, which is sharper than the reading I recorded |
| ⓻ the guard | three families | **HIT**, with a fourth added below |

⓺ is the one to note: registering the **comparison** instead of the expected count is what
`r7670` corrected, and it returned a better answer than the reading I had — not "one sentence
unaccounted" but "zero over the symbol, and the sentence at issue never uses the symbol". An
instrument that counts what it was told to count cannot tell you the set was the wrong set.

## The guard, and what it caught in this instrument

All families flipped. The classifier's first draft had **no class for the remark's own sentences**,
so the remark's attestation sentence — which contains `Δτ = 0` — came back UNCLASSIFIED and
inflated the residue to 1. **A residue is a statement about P1's other sentences; counting the
remark against itself measures the classifier.** The class now fires explicitly, and a fourth guard
family checks both that it fires on the attestation sentence **and** that it does not swallow a
Section-1 sentence. With the repair the residue went from 1 to 0, and the real finding moved to
where it belongs — outside the symbol set.
