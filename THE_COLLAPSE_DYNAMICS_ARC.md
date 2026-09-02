# THE COLLAPSE-DYNAMICS ARC — the exact acoustic amplitude and the deuterium test, from the contracting-side worldline dynamics (c31/Artie, r828, Daryl-directed)

## What this arc is, and why now
The correspondence arc (r815–r826) took the CMB peak **heights** from "open" to a *qualitative* resolution: CR's replacement for ΛCDM's radiation driving is a radiation-comparable **contracting (collapse) phase** pumping the acoustic modes (r824), and by time-reversal invariance of linear driving plus the **κ=0 identity transmission** at the Nariai seam (the null-boundary correspondence, r826), CR's acoustic amplitude **equals** ΛCDM's driven value — heights match, framework-grounded, no longer a plausibility argument. What remains is the **open depth r826 named exactly**: *the detailed worldline dynamics for a concrete matter model.* Two deliverables ride on it — the **exact** peak heights (completing r824's structural match to a precise number) and the **deuterium-yield** refutation test (the contracting-phase thermal history → light elements). This arc works that depth.

## The honest stakes (this is a test, not a victory lap)
The r824/r826 result makes the heights **favourable** (structurally, CR ≈ ΛCDM). But the exact computation can go three ways, and the arc reports whichever it is:
- the exact heights land on the observed pattern (P1/P2≈2.2) → CR passes a sharp quantitative test;
- they deviate in a specific, measurable way → a CR-specific *prediction*, distinct from ΛCDM;
- the contracting-phase thermal history gives the wrong **deuterium** → a genuine falsification of the collapse-driving picture (or of CR).
The deuterium edge especially is a real refutation test. We do not steer toward the favourable branch. Do-not-assert until established; state every call for reversal.

## Governing discipline (the heights arc's hard-won lessons, banked)
- **Read-first.** The heights arc failed four times (overshoot / inverted / timeout / overflow) before r822 stopped and *read the source*. Phase 1 is the deep read, and no computation runs until the collapse structure is held whole. This is the gate.
- **Ordinary GR on the contracting background** — *not a new law*. `slicing_operator §open`: "the general inhomogeneous evolution is ordinary dynamical evolution of the leaf." The contracting-phase perturbation evolution is standard GR perturbation theory on a contracting background; the novelty is the *background* (CR's collapse worldline + seam handover), not the perturbation law.
- **Validate the machinery on ΛCDM before trusting a CR number** (the guard that caught all four failures). Every transfer step reproduces the known ΛCDM result first.
- **Hold the terrain; robust method over fragile ODE** (r823: the analytic WKB effective temperature was the *correct* physics for CR's ~constant potential — no fragile ODE, no overflow). Prefer normalization-robust patterns to absolutes where the physics allows.
- Do-not-assert; state for reversal; the gate carries source-settled calls and never hands them down (r826 coda re-grounding).

## PHASE 1 — THE DEEP READ [THE GATE]
Hold CR's collapse / contracting-phase structure whole, at source, before a line of computation. The reading list, at weight:
- **`slicing_operator.tex §open`** — the branch-point crossing well-posedness (finite-curvature Nariai seam, characteristic, density inherited, rate Λ-set), and the key line: the inhomogeneous evolution is *ordinary evolution of the leaf*. This is the law the whole arc runs on.
- **`CR_framework.tex §null-boundary-correspondence + §reassignment`** — the two Lorentzian halves of one C⁰ slicing at the throat seam; the **κ=0 degenerate Nariai seam → reassignment Ψ = identity** (metric, rigid): why the collapse-side amplitude transmits faithfully.
- **`CR_cosmology.tex` (P13)** — the perturbation sector actually built (the transmission dichotomy, the acoustic structure, the low-ℓ confrontation), so the heights sit in their real context.
- **`CR_PERTURBATION_HELD_PICTURE.md`** — the two root corrections held: the rate read *leftward* (radiation inherited, not sourcing the rate — no radiation-dominated *era*), and `prop:subhorizon` (acoustic modes sub-horizon at the branch point).
- **The validated computations** — `computations/perturbation_verify/cr_peak_pattern_leadingorder.py` (r823, the P1:P2:P3 machinery, ΛCDM-validated) and `cr_collapse_driving.py` (r824, the linear-oscillator driving, undriven=0.500 exact, radiation→1.0). Read what is *already validated* so the arc builds on it, not around it.
- **The progenitor collapse** — how the collapse read inward heats and carries a radiation-dominated *contracting* phase (the thermal history the deuterium test needs); `CR_framework §thm:cosmogenesis` and the when-black-holes-happen essay.
**Deliverable:** the contracting-phase picture held whole — background (the collapse worldline + the κ=0 seam), perturbation law (ordinary GR on the leaf), thermal/radiation content (ρ_r/ρ_m≈2 at the branch point), transmission (identity). A short held-picture note (extend `CR_PERTURBATION_HELD_PICTURE.md` or a sibling) so the terrain is on the record before computing.
**GATE:** past 1 only when the collapse structure is held whole and the picture is written down. No computation before this.

## PHASE 2 — THE CONTRACTING BACKGROUND (a concrete matter model)
Set up the concrete contracting-side background the open depth requires — the "concrete matter model."
- **2.1** The collapse worldline / contracting background: the leaf's contracting evolution approaching the Nariai seam (the scale factor's contracting branch, Λ-set rate, the finite-curvature seam).
- **2.2** The thermal/radiation history: the radiation-dominated contracting phase (progenitor collapse heats inward), pinned to the measured seam IC ρ_r/ρ_m≈2. The temperature history T(t) on the contracting branch — the input both deliverables need.
- **2.3** The concrete matter model: a realistic-enough progenitor (what is collapsing) so the background is concrete, not schematic — held at the minimal realism the computation needs, flagged where idealized.
**Deliverable:** the concrete contracting background + thermal history, ΛCDM-cross-checked where a limit exists. GATE: past 2 when the background is concrete and the thermal history is pinned to the seam IC.

## PHASE 3 — THE ACOUSTIC PERTURBATION EVOLUTION → the exact heights
Ordinary GR perturbation evolution on the Phase-2 background → the exact driving amplitude and peak pattern.
- **3.1** The perturbation evolution: the acoustic oscillator Θ₀ₓₓ+Θ₀=−Ψ(x) with **Ψ the contracting-phase potential evolution** (from Phase 2), not a schematic constant. Validate against ΛCDM's expansion-driving Ψ first (must reproduce a≈3 → P1/P2≈2.2).
- **3.2** The exact CR driving amplitude a=Â/Ψ from the contracting-phase Ψ evolution — is it *exactly* the ΛCDM value (r824's time-reversal claim holds precisely), or a specific CR deviation?
- **3.3** The exact peak pattern P1:P2:P3, confronted with the observed heights. The precise prediction.
**Deliverable:** the exact peak heights — a precise, data-confronted prediction (pass / CR-specific deviation), with the r824 structural match either confirmed exactly or corrected. Do-not-assert until the ΛCDM validation passes and the CR number is robust.

## PHASE 4 — THE DEUTERIUM TEST (the refutation edge)
The Phase-2 thermal history → light-element nucleosynthesis on the contracting phase → the deuterium yield.
- **4.1** The contracting-phase BBN: standard nuclear network on CR's contracting thermal history (T(t) from Phase 2), validated against standard BBN in the expanding limit first.
- **4.2** The deuterium (and He-4) yield — CR's prediction vs observed primordial abundances.
- **4.3** The verdict: consistent (CR passes) / a specific deviation (a prediction) / inconsistent (falsification). Reported as it falls.
**Deliverable:** the deuterium prediction and its verdict — the correspondence arc's sharpest refutation test, resolved.

## PHASE 5 — SYNTHESIS + BAKE
- **5.1** Consolidate: the exact heights (Phase 3) + the deuterium verdict (Phase 4) into one held picture — the correspondence arc's heights closed, confirmed or falsified.
- **5.2** Bake into **P13** (`CR_cosmology`) at earned weight: the peak heights confronted (the exact result, not claimed where data-gated), the deuterium test stated. Only what's established; conditional pieces stay conditional; the honest verdict preserved whichever way it fell.
- **5.3** Currency: `THE_THIRD_ARC`, `CORPUS_MAP` CURRENT STATE, the spine — the correspondence arc's heights moved from "collapse-phase driving (qualitative)" to "exact result + deuterium verdict."
**GATE:** the bake reflects exactly what Phases 3–4 established; nothing steered, the refutation edge honoured.

## The risks the arc watches (named, tested at their phase)
- The contracting-phase Ψ evolution may not give *exactly* ΛCDM's driving — a CR-specific heights deviation (Phase 3). Fine if real; reported.
- The concrete matter model may need more realism than tractable — flag the idealization, bound its effect (Phase 2).
- The contracting-phase BBN may falsify (Phase 4) — the genuine refutation edge; if it falls that way, that is the result.
- Fragile-ODE / overflow traps (the heights arc's failures) — mitigated by read-first, ΛCDM-validation, and robust-method-over-ODE.

## The one-line course
Read the collapse structure whole (Phase 1) → build the concrete contracting background + thermal history (Phase 2) → ordinary-GR perturbation evolution → the exact heights (Phase 3) → contracting-phase BBN → the deuterium verdict (Phase 4) → synthesize and bake at earned weight (Phase 5). Read-first, ΛCDM-validated, not claimed, stated for reversal, the refutation edge honoured.
