# r7802 (60) — RESULT: a read and a fix, and NEITHER is a registered measurement

**Declared plainly, because the form matters:** this revision carries two things, and neither began as a
pushed registration.

1. **`r7801`'s order was a READ** — *"This is a read, not a build. Put a receipt only where a claim
   lacks one."* Its claims are textual readings, each quoted, plus one existing receipt run to green.
   **No receipt is minted: neither claim lacks one.**
2. **The fix was triggered by a GATE FLAG** on a receipt already merged into `main`, which the cron
   treats as mine to fix. Its measurement was made while diagnosing the flag, and is marked as a
   declared post-hoc diagnosis in the receipt's own new row.

⌗ *Nothing here is reported as a registered arm, and nothing claims to be.*

---

## PART ONE — `r7801`'s read

### ⓵ The difference I went looking for is not there, and the declared search is what killed it

`sec:sds-closure` says the Nariai geometry *"stands to the cosmological layer as that Minkowski
projection stands to its layer … the projection the reassignment yields."* `P7`'s own **Minkowski
Projection** proposition yields *Minkowski spacetime*, *"independent of the intrinsic curvature of
`h_ij(t)`"* — a **different** spacetime from the layer. On that reading `P15`'s derivation, which
integrates the **Nariai radial equation** for the scale factor and the redshift, would be computing on
the projection — the error `P7`'s own methodological passage exists to prevent.

**The reading is wrong.** Searched: every occurrence of `projection` within 170 characters of `Nariai`,
`SdS`, `symmetric description` or `de Sitter`, in `corpus/CR_framework.tex` and
`corpus/CR_cosmology.tex` — 20 hits in the first, 1 in the second and that one a source comment. The
usage is settled and long predates the new subsection: *"projections of the same cosmic foliation"*,
*"a morphism between two projections of the same ontological layer"*, *"two distinct Lorentzian metrics
as projections of the same underlying ontological layer"*.

⇒ **A projection in `P7` is a Lorentzian representation of one layering; the Minkowski proposition is
the flat instance, not the definition.** `P15` says it in its own words — *"two presentations of this
one geometry"* — `sec:sds-closure` marks the disanalogy itself (*"It is not empty, as Minkowski is"*),
and **the corpus already carries the receipt**:
`P15_the_layer_is_R_times_S2_on_the_reassigned_chart_and_the_two_presentations_are_two_metrics_on_one_layering_related_by_the_null_reassignment`.

**So the two routes do not say different things and do not rest on different premises on this point.**

### ⓶ ⛔ But one inference in `sec:sds-closure` is under-supported, and this line is why

> *"A projection is valid only if its causal structure faithfully encodes signal propagation on the
> layer … and the layer the signals cross is the content-bearing one … so each takes the expansion of
> the cut that carries the content."*

**That step is the one `r7607` established does not go through alone.** The observer's-readout
identification was found rate-neutral: its flatness half gives `D_M = χ` for either rate, its
three-metric half carries no rate, and the rule needed a **third criterion, photon-path observable,
which that derivation did not carry.**

What closes it is `P15` `sec:scope`'s photon-path step: the bundle goes to the constant-proper-time
family, which **crosses the leaves at unit cosmic-time rate**, and the rate is **cut-independent**
because `dr/dτ = rH(r)/c` has a right-hand side in `r` alone for every mass function.

⇒ **`P7` states that premise in its rate remark** (*"rests on the radial equation's autonomy at `E=1`
and holds on any cut, bent or straight"*), **but `sec:sds-closure` does not point at it, and its own
argument needs it.** Recommended citation at that sentence:
`P15_the_derivation_holds_on_any_cut_because_the_radial_equation_is_autonomous_and_radiation_in_the_cut_moves_the_distance_away_from_the_sky`.

### ⓷ The Misner–Sharp sentence: BACKED, clause by clause

Receipt: `P15_r_labels_the_leaf_so_radiation_bends_the_cut_in_epoch_and_its_pressure_work_gives_the_leaf_rate`,
run here and green.

| `P7`'s clause | the receipt's row |
|---|---|
| the areal radius labels the leaf | **②** `r` constant on each leaf, varying `1091`-fold between them — asserted with the spread, so the row is a test |
| `dm/dr = −4πr²p`; dust constant; `+K/r`; positive density | **⑥** `K` derived from the pressure-work law itself, the density positive at every node, pressure-work `K` equal to the inverted `K` |
| the cut expands at `H_leaf` | **③** the bend `μ = 2M + K/r` has the leaf rate for its own rate |

⇒ **`P7` should cite it.** `P15` cites it at both of its own statements of the same claim.

---

## PART TWO — the flip the build sweep caught, in my own merged receipt

**The three-build tolerance sweep flagged one site**, and it was mine: the multistart selection
`if best is None or o.fun < best.fun` in the three-parameter fit. `err_a = 5.73164258216858`,
`err_b = 5.731642582163483` against a tolerance of `5.73164258216389` — **a FLIP**, the two builds
landing on opposite sides.

### What it was, measured

| | spread across the twelve starts |
|---|---|
| the objective, `100`–`1758` | `1.25e-09` (relative `7.9e-12`) |
| `Δn` | `7.13e-09` here, `1.61e-07` on `700`–`1760`, `5.45e-08` on `1000`–`1760` |
| `ω_b` | `≤ 3.41e-10` on all three |

**All twelve starts reach the same minimum.** The flip re-ordered which start was called best and
**moved no number the receipt prints** — `Δn` and `ω_b` are unchanged to every digit reported.

### But the gate was right, and the fix makes the receipt stronger

A selection among numerically tied candidates **is not a comparison; it is noise with an `if` in front
of it, and it decided what the receipt reported.** The selection is now deterministic — a strict
improvement must beat a relative epsilon, so tied starts keep the fixed sequence's order — and the
agreement the flip exposed is now a **measured row**, `Ⓒ④ᵇ`, so the minimum's uniqueness is asserted
instead of assumed. **The receipt went from 9 checks to 10 and the new one is marked as an addition.**

### ⌗ And I set its bound wrong first, for the third time in this family

`Ⓒ④ᵇ`'s first form required `Δn` to agree to `1e-7` — a bound read off the published window, where the
spread is `7e-9`. It **failed on `700`–`1760`**, where the spread is `1.61e-07`.
⇒ **GUARD, now earned three times here: a bound set from one case and applied to a grid you have not
measured is not a criterion.** Measure the grid, then write the bound. The row now states `2e-7`, with
the relative size (`1e-6` of the smallest displacement) asserted beside it so the bound carries its own
meaning.

## What this revision does not do

It mints no receipt and changes no paper. It does not decide whether `sec:sds-closure`'s Minkowski
analogy should be reworded — the usage is `P7`'s own and the disanalogy is already marked. And the
multistart fix changes no reported number, which is the point of measuring before fixing.
