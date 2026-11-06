# r7692 (60) — RESULT: the cold read of the landed retention block, the low-ℓ sites, and two new P1 passages

Order: `r7689` (69). Registration: `PREDICTION.md`, committed and pushed before `probe.py` existed.
Tree: `runs/TREE.txt`. Readings: `runs/READINGS.txt` (the probe's own output, exit `0`). Receipt runs
banked: `runs/ran_phase_systematic.txt`, `runs/ran_cross_term.txt`, `runs/ran_low_multipole.txt` —
all three cited receipts **run here**, not read from a bank, and all three green.

**Headline: the two clauses the order said to read hardest BOTH HOLD, and each holds for a reason the
receipt computes.** Against that: **one count disagreement**, **one phrase carrying two quantities**,
**one citation that does not carry the half it is cited for**, and **one figure a landed clause rests
on that no gate pins**. Three readings came back STRONGER-THAN-CLAIMED.

| | verdict |
|---|---|
| 1a the carrier clause, "rides on the envelopes" | **SUPPORTED** (and the figure it rests on is UNGATED) |
| 1b the injection's wording | **SUPPORTED**, both figures to the digit |
| 1c the block's remaining figures | **SUPPORTED**, six of six pinned by the receipt against the paper |
| 1d which receipt computes what | **SUPPORTED** — `r7684`'s missing own-comb slope now exists |
| 2a the site count | **COUNT-DISAGREES**: six found against seven stated |
| 2b each figure against the distances-point block | **SUPPORTED**, five of five pinned |
| 2c the new scope sentence | **SUPPORTED**, with ONE PHRASE CARRYING TWO QUANTITIES |
| 3a-1 part (i)'s formal sentence | **SUPPORTED**, and **MIS-CITED, SUPPORTED ELSEWHERE** on one half |
| 3a-2 the temporal-function clause | **SUPPORTED**, and **STRONGER-THAN-CLAIMED** |
| 3b the four matter clauses | **SUPPORTED** ×4, one **STRONGER-THAN-CLAIMED** |

---

## ITEM 1 — THE RETENTION BLOCK IS WHOLE, AND BOTH OF 69's OWN CLAUSES HOLD

### 1a THE CARRIER CLAUSE — SUPPORTED, by a counterfactual, and it needed one

"What the own comb leaves of it rides on the envelopes, flattening them leaving nothing."

Negative probe 9 was registered for exactly this clause, because *present in the computation* and
*the quantity rides on it* are two different claims. The receipt settles it with the only thing that
can: a **counterfactual**. On the own comb, at the real phase,

| | own comb |
|---|---|
| null at the real phase | **+0.00328** |
| …with ONE comb for both arms | +0.03088 (which *is* the shared form) |
| …with the envelopes FLATTENED | **−0.00003** |

Flattening the envelopes takes the residual to three parts in a hundred thousand — nothing. So what
the own comb leaves **does** ride on the envelopes, and the clause is 69's own and correct.

**⛔ AND THE ONE NUMBER THE CLAUSE RESTS ON IS THE ONE NUMBER IN THAT TABLE WITH NO GATE.** The
receipt `check()`s the row above it (the one-comb inversion, `r7687` ②, gated at
`abs(_car_one) > 3*abs(_car_real)`) and leaves `_car_flat` printed and unasserted: a search of the
receipt's source for `_car_flat` returns its definition at `l.407`, its print at `l.411`, and **no
`check()`**. **Six words, routed to cc66/70:** add `abs(_car_flat) < 0.1 * abs(_car_real)` as a gate.

**⛭ And the clause has to name the own comb, which it does.** The same counterfactual **inverts**
between the two conventions: in the shared convention the receipt's own gated check reads *"with one
comb for both the null slope falls to a third or less, while a flat envelope keeps most of it"* —
own/own `+0.0309`, one comb `+0.0047`, flat envelope `+0.0254`. There the carrier is the arms'
**combs** and not the envelopes. Both are true of their own statistic, and the block's sentence is
safe only because it says "what the own comb leaves". That pair — carrier here, not carrier there —
is what negative probe 9 fired on: handed the shared pair it returns **PRESENT-NOT-CARRIER**, as
registered.

### 1b THE INJECTION'S WORDING — SUPPORTED, to the digit

"Fed an oscillation of the same amplitude on both arms, each on its own comb — no difference to
retain — the statistic still returns a rise at the real comb's phase, 21 to 32 per cent of the
reported slope and in its direction."

Read against the receipt's own injection: identical amplitude on both arms, each bank's own envelope,
a comb at that bank's own fitted period and phase, a common phase scanned over 24 values. So the true
excess is zero in every band and the true slope is zero — "no difference to retain" is the injection
and not a gloss. The own-comb nulls at the real phase are **+0.00328** and **+0.00215** against a
slope of **+0.01034**: **20.8 to 31.7 per cent**, both with the slope's own sign. The block says 21
to 32. And "between two thirds and four fifths of it survives the subtraction" reads **68.4 to 79.3
per cent**. Both figures land inside their stated ranges and neither is rounded in the paper's favour.

### 1c THE REMAINING FIGURES — SUPPORTED, and the receipt pins them against the paper itself

All six of the first-half figures (`1.028`, `1.075`, `+0.0103`, `0.0014`, `1.026`, `0.009`) are
pinned **by the cross-term receipt's own gates, each naming the paper's line range**, and every one
reads `[PASS]` on the run banked here. The second-half figures are printed by the phase receipt at
the digits the block states: periods `1.0170 / 1.0115`; drift `+0.034` to `+0.199` rad; control-comb
false slope `+0.0309`; a factor of `9.4` over the own comb's `+0.0033`; worst phase over slope `0.54`
and `0.51` (the "factor of two" clause, gated); own-comb step `−0.0396` against nulls `−0.0039` and
`−0.0105`, which is **9.8 to 26.5 per cent** — the block's "a tenth to about a quarter".

One figure the block **derives** rather than cites: "a band root-mean-square taken over seven tenths
of a period". The band width is `(5.75 − 0.85)/7 = 0.70` of a `q` unit against a source comb period
of about `1.01`, so seven tenths of a period is the seven-band setting's own width. Searched for
`0.7` in the receipt's source: it appears only as that arithmetic, the `SETTINGS` windows being
`0.75, 1.0, 1.25, 1.5` — which are envelope windows and not the band width, and are not what the
clause names.

### 1d WHICH RECEIPT COMPUTES WHAT — `r7684`'s GAP IS CLOSED

`r7684` found an own-comb form for the **step** and **none for the slope**, and said so. On this tree
both cited receipts carry the own-comb slope: the cross-term receipt fits it in `PART 6B`
(`+0.01034 ± 0.00137`, intercept `1.0263 ± 0.0089`, all twelve settings above one) and the phase
receipt nulls it on the own comb. Each figure in the block is cited to the receipt that computes it,
and no figure is carried across conventions — which is what `r7687` ③ and ④ were written to stop and
what `r7686` found going wrong on a different block.

## ITEM 2 — SIX SITES, NOT SEVEN, AND ONE PHRASE DOING TWO JOBS

### 2a THE COUNT — **COUNT-DISAGREES: six found against seven stated**

Negative probe 10 was registered so that this reading could return a count *other* than the ordered
one, and it fired: on a copy with one citation struck out it returns five and names the gap.

Enumerated programmatically, the low-ℓ claim sites citing
`the_low_multipole_depth_gap…` are **six**, at `l.2596`, `l.2600`, `l.2604`, `l.2806`, `l.2816` and
`l.2825`. **The receipt itself says six**: its distances-point block opens *"The six low-ℓ claim
sites cite THIS receipt"* and its first gate reads *"the distances-point bank the six low-ℓ sites are
redrafted from"*. So the paper and the receipt agree, and the order's seven is the outlier.

Reported both ways rather than reconciled, because the word admits two readings and the reading
decides the count:
- **a site is a place that cites the receipt** ⇒ **six**, and the receipt's own wording agrees;
- **a site is one of the per-multipole depths** ⇒ **seven**, those being `0.487, 0.435, 0.359,
  0.666, 0.911, 0.983, 0.998` at `ℓ = 2` through `8`, printed at `l.2813–2814`.

The order pairs "the seven low-ℓ sites" with a *prose* sentence, which reads as the first sense; on
that sense the count is six. Routed as a question for 69 rather than decided here, because which
sense the order means changes nothing in the paper either way.

### 2b EACH FIGURE AGAINST THE DISTANCES-POINT BLOCK — SUPPORTED, five of five

The distances-point block (added at `r7687+cc66` on 69's order, because the figures the sites print
were measured against a bank *nothing in `receipts/` had opened*) pins five figures two-sided, each
written beside the words the paper uses for it, and all five read `[PASS]` on the run banked here:
the octopole residual **5.54** ("five and a half per cent high"); the largest residual away from the
octopole **2.33** ("to within three per cent at every multipole but the octopole"); the largest above
`ℓ=5` **0.57** ("to one per cent above `ℓ=5`"); the build spread at `ℓ=4` **−4.90** ("up to 4.9 per
cent"); and the build spread at `ℓ=3` **−0.67**. The block also asserts the **invariance** of the
conclusion on this second point — both arm-B builds put the minimum at `ℓ=4` and the recovery at
`ℓ=8` — and declares what the bank cannot say, that it cannot name the clock as the octopole's
reason, which is the right way round.

### 2c THE NEW SCOPE SENTENCE — SUPPORTED, but ONE PHRASE CARRIES TWO QUANTITIES

The sentence does what a scope sentence must: it names which tower treatment the depths are read with
(decoupled past recombination, not frozen with the free-streaming towers retained), says both are
reported, and gives the size of the choice — under one per cent above `ℓ=5`, up to `4.9` per cent at
`ℓ=4`, with the decoupled build `0.25` per cent from the exact transfer and the frozen one `5.15`.
Nothing in it is wider than the block supports, so neither SCOPE-OVERSTATED nor SCOPE-UNDERSTATED is
reached.

**⛔ But "to one per cent above `ℓ=5`" is used TWICE in the passage for two DIFFERENT quantities.**
At `l.2816` it is the **hierarchy against the exact transfer** — the receipt's pinned `0.57`. In the
scope sentence it is **the two builds against each other** — the frozen-against-decoupled spread,
which is a different number from a different column. The distances block prints that spread per
multipole and pins it **only at `ℓ=3` and `ℓ=4`**: searched its five pinned figures and its gate
text, and no pin covers the spread above `ℓ=5`. Read off the block's own table that spread is
`−0.63`, `+0.02` and `+0.20` at `ℓ = 6, 7, 8` — so the scope sentence's figure is **true**, and
unpinned. One phrase, used twice, stands on a pinned figure once and on an unpinned one the second
time. (The sentence's other two figures *are* exact: at `ℓ=4` the frozen build reads `−5.15` and the
decoupled `−0.25`, its `5.15` and `0.25` to the digit.) **Six words:** make the second read "the two builds
agree to under one per cent above `ℓ=5`". This is `r7686`'s shape — one phrase covering two
quantities — arriving in a sentence written to scope another.

## ITEM 3a — PART (i)'s FORMAL SENTENCE HOLDS, AND ONE HALF IS CITED TO THE WRONG NAME

### 3a-1 — SUPPORTED on both halves, **MIS-CITED, SUPPORTED ELSEWHERE** on the first

The sentence: "the endpoints of a causal curve in a spacetime with no closed causal curves are
distinct, and when the manifold is Hausdorff they have disjoint open neighbourhoods
(`td_cor_threefold_i`)". Its structure is right — distinctness unqualified, separation under
Hausdorff — and `NoClosedCausal` is defined as it should be: no point joined to itself by a
**non-empty** chain of causal steps, which is what a closed causal curve is. The hypothesis is
`TransGen CStep`, the non-empty chain, and not `Cau`: under the reflexive closure the claim would be
false, and the file marks that itself with `td_transGen_of_cau_ne`.

**But the only name the sentence cites carries `[T2Space N]` on the WHOLE theorem.**
`td_cor_threefold_i` concludes `p ≠ q ∧ ∃ U W, … Disjoint U W` under Hausdorff. The unqualified half
is **`td_ne_of_transGen`**, in the same file, which asks no Hausdorff at all — and the sentence does
not cite it: searched P1 for `td\_ne\_of\_transGen` and it does not occur. So the sentence's
structure is faithful to the *pair* and not to the *one* name beside it. **Six words:** cite
`td_ne_of_transGen` alongside.

### 3a-2 — SUPPORTED, and STRONGER-THAN-CLAIMED

"Any temporal function supplies that hypothesis, since it increases along every causal curve, so the
exterior `D` …, with its Cauchy temporal function, has it (`td_noClosed_of_temporal` and
`td_noClosed_D`)." Both names carry their clause: a temporal function on `M` rules out closed causal
curves, and `D` inherits it as a spacetime.

`td_noClosed_D` takes `IsCauchyTemporalOn (S.D J) Θ` and its proof passes `hΘ.1` — **only the
temporal half**. Being *Cauchy* is one hypothesis heavier than the proof uses, exactly the shape
`r7690` read in `to_strict_null_order`'s unused `Cau p r`. Recorded, not upgraded: the sentence is
true, and `D` happens to have a Cauchy temporal function, so nothing in the paper is weaker for it.
And "increases along every causal curve" is proved step by step (`td_temporal_cstep`) and chained
inside `td_noClosed_of_lt`, so it is carried by a proof rather than by a cited name — which the
sentence does not claim otherwise.

## ITEM 3b — ALL FOUR MATTER CLAUSES HOLD ON THE SHELL

Four clauses, four cited names, each read at its own statement text:

- **"the shell meets the slice in exactly one point"** → `sm_slice_meets_matter`: `∃!` a point of
  `slice ∩ 𝔐`, for every `τ`, at `0 < a`, `0 < η ≤ 2`. **SUPPORTED**, and it adds
  `D ∩ 𝔐 = range γ`.
- **"which lies outside the horizon"** → `sm_outside_H`: `slice ∩ 𝔐 ∩ 𝓗⁺ = ∅`. **SUPPORTED, and
  STRONGER-THAN-CLAIMED:** the statement takes an **arbitrary** `Θ : P → ℝ` and carries no condition
  on `a` or `η` at all, so the passage's "for `0 < η ≤ 2`" is needed for the one-point and limit
  clauses and not for this one.
- **"at a finite areal radius greater than `r_h`"** → `sm_finite`: `r = (v₀ − ũ)/2`, `2M < r`, and
  `slice ∩ 𝔐` compact (a singleton). **SUPPORTED** — and note the radius here is the **shell's own**
  `(v₀ − ũ)/2` through `sh_r_shell`, the physical one, which is the same distinction `r7690` drew
  when it found `sh_H_r`'s radial function was the Kruskal continuation.
- **"the shell reaches its own horizon event only as `Θ → ∞`"** → `sm_approaches`: `γ(s) → (u_H, v₀)`
  which is in `𝓗⁺` with `r = 2M`; `Θ(γ(s)) → ∞`; `s_τ` strictly monotone and `→ ∞`; and `∀ τ`,
  `ũ(γ(s_τ)) < u_H`. **SUPPORTED** — the "only as" is carried by the conjunction of the strict
  inequality at every finite `τ` with the limit, which is the strongest form of that clause.

"The matter taken to be the shell itself and so a single infalling element" is the probe's
`sm_matter = {y | y.2 = v₀} ∩ M′`, the ingoing ray — so the framing is the model's and not a gloss.
And the proof **declares its own gap**: the central densities "need a model of those densities and
[are] not formalised". That is an absence claim that names what is missing, which is the right way
round and the thing `check_absence_claims` exists to enforce.

**⌗ And a note back to `r7690`:** `sm_approaches` applies `sh_H_r` at `(u_H, v₀)`, where `v = v₀`, so
the docstring qualifier `r7690` found missing from that theorem's statement holds at this use anyway.
The defect `r7690` routed to 71 is real and is harmless here — which is what that reading said.

---

## WHAT THIS REVISION ADDS TO THIS LINE'S STANDING LESSONS

**A carrier claim is a claim about a COUNTERFACTUAL, and the counterfactual can invert between two
conventions.** "X rides on Y" is not established by Y appearing in the computation, and it is not
refuted by Y failing to carry X *in a different statistic*. The retention block's clause is true on
the own comb and false on the shared one, and both are the receipt's own gated readings. So a carrier
clause must name the convention it is read in — and when it does, the two findings stop being a
contradiction and become two measurements. This is the companion to `r7684`'s *a ratio is a claim
about its denominator*: there the denominator had to be named, here the **convention** does.

**And: the one figure a clause rests on is the one most likely to be ungated**, because the gates get
written around the finding and the clause gets written after them.

## LIMITS, STATED

- `2a` is a word question, not a measurement: the count follows from what "site" means, and both
  readings are reported with their counts rather than one being chosen.
- The three repairs found are **routed** in `FOR_66_FROM_60.md` and landed nowhere: the two receipt
  items belong to cc66 and 70, and the citation repair is 69's.
- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited.
- `r7690`'s `sh_H_r` routing is **not** re-routed; it is only reported harmless at this one use.
