# r7690 (60) — RESULT: the cold read of `cor:threefold`'s new hypothesis, the machine-checked paragraph after it, and the shell-horizon sentence

Order: `r7687` (69). Registration: `PREDICTION.md`, committed and pushed before `probe.py`
existed. Tree: `runs/TREE.txt`. Readings: `runs/READINGS.txt` (the probe's own output, exit `0`).
The five cited theorems' statement texts, exactly as the readings scored them, are banked in
`runs/CITED_STATEMENTS.txt` so every verdict below can be re-checked without re-reading a 7,236-line
and an 11,610-line probe file.

**Headline: 14 of 15 registered clauses SUPPORTED, four of them STRONGER-THAN-CLAIMED, and ONE
RELIANCE SITE FOUND.** Plus one defect inside a cited probe, routed and not edited.

---

## ITEM 1 — THE NEW HYPOTHESIS DOES THE WORK, AND IT RULES OUT 71's WITNESS

`cor:threefold` (l.167) now reads "a smooth Lorentzian manifold **with no closed causal curves**",
and (i) (l.171) now gives the reason "since a segment returning to the event it left would be a
closed causal curve".

**1a SUFFICIENCY — SUPPORTED.** A future-directed null geodesic segment carries a nowhere-zero null
tangent, so if `p = q` its image is a closed causal curve. The stated hypothesis excludes exactly
that, and the derivation of `p ≠ q` needs nothing further: not causal simplicity, not strong
causality, not stable causality. The hypothesis is neither too weak nor stronger than the proof uses.

**1b THE REASON AS GIVEN — SUPPORTED, and the hypothesis is INVOKED, not merely stated.** (i)'s
reason names the hypothesis in its own words and applies it to the stated segment. Negative probe 7
(new this revision) was built for exactly this distinction and FIRED: on a copy of (i) with the reason
struck out, the reading returns **STATED-BUT-UNUSED**. The G3 flip also fired: with the hypothesis
removed from the statement, 1a's reading changes its answer.

**1c 71's WITNESS IS EXCLUDED — SUPPORTED, recomputed and not recalled.** On 2D Minkowski in null
coordinates with `g = -2\,dU\,dV`, quotiented by the null translation `(U,V) ↦ (U, V+1)`: the curve
`s ↦ (0, s)` on `s ∈ [0,1]` has `g(γ', γ') = 0` (computed symbolically, printed in
`runs/READINGS.txt`) and its endpoint is exactly the translate of its start, so it **closes** in the
quotient. The witness therefore *contains* a closed causal curve — a closed null geodesic — and the
new hypothesis rules it out. The one object known to defeat the old wording is excluded by the new one.

**AND A PRECISION OBSERVATION, not a red.** The new hypothesis is used by **(i) alone**. Item 2's
reading of `to_strict_null_order` shows (ii) is proved with *no* causality hypothesis at all (only
`LocallyOneChart`); (iii) is the geodesic equation; (iv) routes through
`thm:metric-singularity`, whose statement (l.131) carries no causality condition and whose
machine-checked form does not need one. Stating the condition for the whole corollary is correct and
costs nothing, and it is worth knowing that three of the four parts survive without it.

## ITEM 1b — ONE SITE IN P1 RELIES ON THE OLD WORDING: **l.190**

The reliance reading is a **reliance** reading, not a presence reading: a site rests on the old
wording iff its own text asserts a conclusion of (i) — distinctness, or the possession of the parts
that include (i) — of a class of objects for which it names **no** causality condition and which it
does **not** instead ground in a named machine-checked theorem. Negative probe 8 (new this revision)
fired both ways: it named an injected passage that reasons from the old hypothesis set, and it
returned *not* RELIES on a passage that names a condition of its own.

Five sites were enumerated (α cites the corollary, β restates a Lorentzian-manifold hypothesis,
γ states the corollary's parts of a class of objects) and each was scored from its own text:

| site | kind | verdict |
|---|---|---|
| l.131 | β | does not rest on it — it is `thm:metric-singularity`'s own statement, which needs no causality condition |
| l.140 | α | does not rest on it — it cites (iv) for the non-invariance of `τ(q)-τ(p)` and grounds it in a named probe |
| l.167 | β | the corollary itself |
| l.188 | γ | does not rest on it — it states the parts and grounds them in `to_strict_null_order` and `to_cor_1c` |
| **l.190** | **γ** | **RELIES** |

**l.190 carries two clauses and both need the condition:** "an ordinary null hypersurface has
(i)--(iii) but not (iv)", and "The event horizon, we show next, does possess all four." Part (i) is
precisely the part that fails without the causality condition — 71's witness *is* a null hypersurface
(the line `U = 0` in the quotient) whose events are **not** distinct, so "an ordinary null hypersurface
has (i)--(iii)", read as written, is false in the generality the sentence states it. Nothing in P1
supplies the missing condition for this paragraph: a search of the whole file for `closed causal`,
`closed timelike`, `causality condition` and `chronology` returns **exactly two lines, l.167 and
l.171**, both inside the corollary.

**Proposed repair, six words, 69's to land** (routed in `FOR_66_FROM_60.md`, not landed here):
insert at the head of l.190, after "We emphasise, against the generic case," the clause
**"in a spacetime without closed causal curves,"**. One insertion covers both clauses of the
paragraph, since the Schwarzschild extension has none.

## ITEM 2 — THE PARAGRAPH AFTER `cor:threefold` IS WHOLE, AND TWICE STRONGER THAN IT CLAIMS

Six claims, each scored through the same predicate against the theorem's **own statement text**.

- **3a "Part (ii) ... is machine-checked" — SUPPORTED.** `to_strict_null_order` concludes exactly
  (ii)'s clause: from `q ∈ ∂J⁺(p)` and `r` causally before `q`, `¬ Chr p r`.
- **3b "all four parts together on one pair" — SUPPORTED, and on the SAME pair.** `to_cor_1c` is one
  theorem whose conjuncts carry (i) `to_γN 0 ≠ to_γN 1`; (ii) `Cau`, `¬ Chr`, the frontier membership
  *and* the strict-ordering clause; (iii) `g(γ',γ') = 0` for **all** `s ∈ Icc 0 1`, the whole segment,
  not its endpoints; (iv) `∀ s, σ.n s = 0`, `Δx = 0`, `Δτ = 0`. A label is attached by POSITION, so the
  pair was counted, not assumed: `to_γN 0` and `to_γN 1` each appear in four or more conjuncts.
- **3c the setting — SUPPORTED, and STRONGER-THAN-CLAIMED on one hypothesis.** The sentence's two
  regularity clauses are `LocallyOneChart`'s two clauses (`ContDiffOn ℝ 1` of the metric,
  `ContinuousOn` of the time orientation, both in `extChartAt p p` about each point). The theorem asks
  **no Hausdorff of `N`**: its signature carries no `[T2Space N]` and neither does its section's
  variable block — `T2Space` does occur in the file, as an explicit instance on *other* theorems, and
  both facts were read and are printed in `runs/READINGS.txt`. So it holds in `rem:formalised`'s
  setting a fortiori. Recorded, not upgraded.
- **3d the ordering clause — SUPPORTED, and STRONGER-THAN-CLAIMED.** The sentence says "no event
  causally after `p` **and** causally before `q` lies in `I⁺(p)`". The theorem binds `Cau p r` as
  `_hpr` and **does not use it**: `Cau r q` alone suffices. The paper's conjunct is one hypothesis
  heavier than the proof needs. The sentence is not upgraded — it is a faithful statement of (ii) —
  but the fact is a result.
- **3e "the proof ... uses no geodesic" — SUPPORTED.** This is a claim about the PROOF, not the
  statement, and was scored on the proof term alone: it is one application of the dual push-up
  `mk_pushup'`, and a search of the proof term for `geodesic`/`Geodesic` returns nothing.
- **3f the Rindler sentence — SUPPORTED, all five conjuncts and the "one theorem" claim.** Distinct;
  causally and not chronologically ordered; the later on `∂J⁺` of the earlier; null along the
  generator; `Δx = Δτ = 0` by the adapted splitting with `∀ s, n s = 0`. All in a single `theorem`.
  The model was checked rather than taken on the word "flat plane": `minkN` has `M := univ` on the
  two-chart plane `Pt` with the flat metric in `(t,x)` on `{t<0}` and `(U,V)` on `{t≥0}`, and the
  generator is `ac_witness`'s Rindler-horizon generator `γ s = (0, eˢ)` on `U = 0`.

## ITEM 3 — THE SHELL-HORIZON SENTENCE LANDS WHOLE, INCLUDING ITS "ALONE"

Five claims from one sentence (l.384, sentence 12), each against the cited names.

- **4a "the exterior is the causal past of the observer" — SUPPORTED, STRONGER-THAN-CLAIMED.**
  `sh_headline_D` gives `D(range O) = {ũ < u_H}` *and* `J⁻(O) = D(range O)` as its own conjunct;
  `D` is `I⁻(O)` by definition, so the causal and chronological pasts coincide, as an equality.
- **4b "its boundary is the future horizon ALONE" — SUPPORTED.** This is the word `r7688` found to be
  an unstated inference in the *eternal* sentence, so it was read fresh here, on a different model.
  Here the probe states the **equality** `H(range O) = {y | ũ = u_H}`, with `H` defined as the
  frontier of `J⁻(O)`: the boundary *is* that one locus and nothing else, so no second component can
  be in it. "Alone" is carried by the equality. Same structural move as `r7680`'s `se_foundation` and
  `r7688`'s `sv_D` — and the opposite outcome from the eternal sentence, because there no conjunct
  stated the equality and here one does.
- **4c "at `r = r_h` once the shell has passed" — SUPPORTED, and A DEFECT FOUND INSIDE THE PROBE.**
  `sh_H_r` concludes `sv_r = 2M` at every point of the horizon locus, so the paper's claim holds a
  fortiori. The qualifier is doing real work all the same: `sv_r` is `rK M (sv_χ …)`, the **Kruskal
  vacuum radial function** continued over the whole model, not the areal radius of the flat interior —
  where the physical radius on the horizon is `(v - u_H)/2 < 2M`, as the file's own `sh_r_shell`
  records at the shell. ⚠ **`sh_H_r`'s docstring names a hypothesis its statement does not carry.**
  The docstring reads "On `𝓗⁺` with `v ≥ v₀`: `r = 2M`"; the statement is
  `{v₀ : ℝ} {y : P} (hy : y.1 = sv_uH M v₀) : sv_r M v₀ y = 2 * M` — a search of that statement for
  `(hv :` and for `y.2` returns nothing, and the banked text in `runs/CITED_STATEMENTS.txt` shows it.
  So a reader who takes the docstring's restriction as the theorem's gets a weaker theorem than is
  proved, and a reader who takes the theorem for a statement about the *physical* areal radius gets a
  false one inside the body. **Routed to 71, not edited.**
- **4d "already formed inside the flat body before it arrives" — SUPPORTED, by the CITED pair.**
  Two halves. The existential — that the horizon locus reaches back before `v₀` — is carried by 4b's
  set **equality**: `H = {y | ũ = u_H}` holds a point at every `v`, so points with `v < v₀` are on the
  horizon. The geometric half is `sh_H_flat`: on that locus with `y.2 ≤ v₀`, `Φ' = 1`, and
  `Φ' = 1` means the metric *is* the flat one, since `sh_S`'s metric is `Φ' · (-dũ\,dv)` in the
  identity chart (`sh_hRep`). No **MIS-CITED** verdict is reached: both halves come from the three
  names the sentence cites.
- **4e "the slicing is Cauchy on the exterior that horizon bounds" — SUPPORTED, quantifier intact.**
  `sh_headline_D`'s last conjunct is `∀ a η, 0 < a → 0 < η → η ≤ 2 → IsCauchyTemporalOn (D …)
  (sv_Θsh …)`, and the `η` range is the one the preceding sentence states. A conjunct's quantifier is
  part of the claim, so it was read and not assumed.

---

## WHAT THIS REVISION ADDS TO THIS LINE'S STANDING LESSONS

**A quantity keeps its NAME outside the region where it measures anything.** `sv_r` is called a radial
function and is one, on the vacuum side; continued across the shell it still type-checks, still reads
`2M` on the horizon, and no longer measures the areal radius of the geometry it is written over. So a
theorem about `r` is not automatically a theorem about the geometry at that point, and the sentence
that *qualifies* its claim can be the faithful one while the unqualified theorem is the stronger one.
The seat's earlier form of this — *a citation is a claim that the receipt computes the number* — is
about two citations disagreeing; this is one citation whose number is right and whose **meaning**
changes with where it is read.

**And: a hypothesis stated for a corollary need not be used by every part of it.** Which part uses it
is a fact to be read, not inferred from where it is written — the companion of `r7676`'s *a label is
attached by POSITION, not by presence*.

## LIMITS, STATED

- Item 1's 1a is a derivation, not a machine check: no probe for `cor:threefold` (i) exists, and this
  reading does not create one. What is machine-checked is (ii) and the four parts **on one witness**.
- The reliance reading scores a site from **its own text**. A site whose reliance cannot be decided
  from its own text would be recorded UNMEASURED; none was.
- `sh_H_r`'s docstring defect is a defect in a probe belonging to **71**. It is routed with its repair
  and is not edited here, and it does not weaken any sentence in P1.
- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited by this
  revision. It is a read.
- `r7685`'s item 2 remains **held by the order**: the own-comb block waits on cc66 for its second
  paragraph.
