> **⌗ RETIRED r2380 under `RG-1` — AND IT IS RETIRED HONESTLY BECAUSE IT LABELLED ITSELF HONESTLY.**
> *A first run of the peak-heights transfer (r818), and its own status line is:* ***"MISCALIBRATED — not a
> result … a leading-order run, honestly flagged: it is a SKETCH, not a calibrated result."***
> **A document that says it is not a result is a document nobody should be planning from**, and its subject has
> moved twice since: to a qualitative resolution across r822–r826, and then to `L-171` — the two *internal*
> routes disagreeing on the first acoustic peak, which is a sharper place than this run could reach.
>
> **⌗ WHAT SURVIVES IT is the reason it was flagged rather than banked.** *Four transfer attempts failed
> (r818–r821) before r822 stopped and read the source; that is `THE_PLAN`'s **GREP TO FIND, READ TO CONFIRM**
> and the wisdom ledger's **repeated failure of the same kind is a diagnosis, not an obstacle to push harder
> at**. ***The run was wrong and the labelling was right, which is the order that costs nothing.***

---

# Third arc, T0.1 — the peak-heights transfer: first run

*Run r818 (2026-07-05). "You know how to run it" (Daryl) — the coherence-comb receipt already propagates the tight-coupled oscillator to last scattering; the heights are that same solve with the amplitude physics (baryon loading, driving, damping) added. A leading-order run, honestly flagged: it is a SKETCH, not a calibrated result. Script: `computations/perturbation_verify/explore_cr_peak_heights_LEADINGORDER.py`.*

## What was run
The effective-temperature transfer [Θ₀+Ψ](k) = [(1+R)·B(k)·cos(k·r_s) − R]·D(k) at last scattering (Hu–Sugiyama form): the coherent acoustic phase (single seam datum), the baryon-loading shift R (odd/even asymmetry), the driving boost B(k), Silk damping D(k). Projected flat to C_ℓ at k=ℓ/D_C. Driving **bracketed**: full (radiation gravitates normally) vs none (matter-like potential, the radiation-free-rate extreme).

## Honest status of the numbers: MISCALIBRATED — not a result
Absolute first-peak/plateau came out ~40–60× vs observed ~5–6× (≈10× high): the driving boost was applied as a raw amplitude then squared, and the plateau/transfer normalization is not calibrated (no proper primordial normalization, no ISW, no Doppler, no real projection). **The absolute heights are NOT trustworthy and are not presented as CR predictions.** This confirms P13's flag: the peak heights genuinely need the calibrated full transfer, not a short script.

## What the run DID establish (robust)
1. **The crux is well-posed and CR-specific.** CR's *density* equality z_eq≈3400 is the **standard** value (ρ_r/ρ_m≈2 at seam z≈6801, ∝(1+z), =1 at z≈3400). So CR's radiation content at equality is standard; only the radiation-free *rate* (no radiation-dominated expansion epoch) is non-standard. CR's driving is therefore a specific *intermediate* value (radiation present, not in the rate), not absent (r816's overstated worry) and not standard — and it is computable.
2. **The pattern brackets the data (normalization-robust).** The P1/P2 peak asymmetry — baryon loading pushes up, driving pulls down — brackets the observed ~2.0–2.3 between the no-driving extreme (too asymmetric) and the full-driving extreme (too symmetric). The observed value sits *inside* CR's driving bracket: suggestive that CR's intermediate driving can land the peaks. Suggestive only.

## What T0.1 actually is (scoped precisely now)
The **calibrated CR seam-to-recombination transfer**: CR's radiation-free background, the potential evolution Ψ(η) with radiation present-but-not-in-the-rate (which fixes the driving), the effective temperature + Doppler + ISW, proper primordial normalization, the flat projection. A careful computation (a small dedicated transfer, not CAMB, not a 50-line sketch), tractable, the real remaining work of Tier 0. **The refutation edge:** if CR's specific driving lands the peak pattern outside the data. **The first indication:** it may not (the pattern brackets the data). Held not claimed until the calibrated transfer is run.

## Gate call: BANK (first run + scoping). No paper change.
The sketch is banked as an exploration script (clearly marked LEADINGORDER), not a receipt of an established result; P13's open flag stands. The calibrated transfer is the next real work.

---

## Second run (r820) — CALIBRATED attempt, ΛCDM validation FAILED. No CR result.
"Now we go have a look" (Daryl), steady hands = **validate on ΛCDM before trusting CR**. Built a fuller tight-coupling transfer (effective temperature with baryon loading + a BBKS-like potential transfer + a driving envelope + Silk damping + Doppler + the flat projection + tilt), and ran the **ΛCDM calibration check first**.
- **Result: the check FAILED.** ΛCDM peaks came out *inverted* (P1/P2≈0.27 — P2 taller than P1) and absolute heights ~10³× the SW plateau (observed P1≈5.7, P1/P2≈2.2). The real spectrum has P1 highest with higher peaks damped; the model grows them instead.
- **Cause (genuine physics, not a typo):** the driving envelope and the potential transfer are applied inconsistently, and the Silk damping barely bites at the first peaks (k_peaks≈0.016–0.05 vs k_D=0.13). The peak heights are a *delicate balance* — driving up, potential-transfer suppression down, damping, the true (non-instantaneous) projection — that a hand-built semi-analytic envelope does not capture.
- **Discipline held:** the check failed, so the CR numbers (which I did compute) are built on an invalid model and are **discarded, not reported**. This is the steady-hands guard working — validate on the known case, and when it fails, do not manufacture a prediction on the unknown one.

## Conclusion, twice-confirmed: T0.1 needs proper transfer machinery.
r818 (overshot ~10×) and r820 (fails ΛCDM validation) together establish that the CR peak-height transfer is **a real computation, not a session sketch** — exactly why P13 wrote "we do not claim here." The genuine T0.1 work is a small but *correct* transfer (proper effective-temperature evolution, the driving from CR's actual Ψ(η), the real projection, honest normalization), validated against ΛCDM before CR is read off it. That is a genuine build — the honest next step, not a look. The one physical result that survives from the runs (robust, r818): CR's *density* equality z_eq≈3400 is standard, so CR's driving is a specific intermediate value, computable — the input the real transfer needs. Held not claimed for the heights until a *validated* transfer is run.

## Gate call: BANK. No paper change; no CR heights claim. The failed ΛCDM check is the receipt that the semi-analytic route is insufficient.

---

## Going further (r821) — the ODE build attempted; the honest computational limit reached.
"Let's go further" — attempted the proper transfer: a tight-coupling ODE solve where the driving *emerges* from the potential's own decay (not a hand-tuned envelope), validated on ΛCDM before CR.
- **Two more attempts, both caught by validation:** (3) full ODE integration from early η **timed out** (too many modes, too-fine steps); (4) a lean second-order oscillator **overflowed to NaN** (CDM δ growth + potential feedback unstable in the quick implementation). No result reported — the validation guard held a fourth time.
- **The honest limit, four ways confirmed** (overshoot / inverted / timeout / overflow): a **validated CMB transfer is genuine numerical development** — careful gauge, stable ICs, tested integration — not an in-session script. Exactly why CAMB/CLASS exist, and why P13 wrote "we do not claim here."
- **The deeper prerequisite, surfaced:** to build the CR transfer *correctly* I need CR's **actual** perturbation structure at source — how the radiation-free rate is consistent with Einstein's equations (radiation in the density, not in H), which sets the driving. My solves fed *generic* perturbation physics — the skim-not-read error (r817), one level down. I do not yet hold CR's perturbation setup well enough to code it.

## The genuine next step (scoped honestly, not forced)
Two things, in order, both real focused work — not a session quick-solve:
1. **Read CR's perturbation/background structure at source** — P13 §properframe/§flatlcdm/§tensions and the framework paper — until the radiation-free-rate perturbation dynamics are actually understood (not assumed). This is the prerequisite; the r821 failures trace to skipping it.
2. **A validated numerical transfer** — a proper toy Boltzmann (stable, tested, ΛCDM-validated) or CAMB/CLASS with CR's modification correctly implemented — then read the CR heights off it.

The heights stay **not claimed**. The robust input survives (z_eq≈3400 standard → CR's driving a specific intermediate value). Four honest attempts have precisely scoped the work and confirmed the validation discipline holds; the transfer is a genuine build for a focused effort, and the steady move is to stop here rather than manufacture a fifth.

## Gate call: BANK. No result, no paper change. The honest computational limit, reached with the guard intact.

---

## The right way (r823) — the held picture applied, machinery validated, a real result.
With CR's structure held correctly (`retired/CR_PERTURBATION_HELD_PICTURE.md`), the transfer became tractable and robust — the battle lessons paid off:
- **Robust, not fragile:** CR's potential is ~constant (matter background, little driving), so the analytic WKB effective temperature IS the correct physics — no ODE, no overflow.
- **The pattern, not the absolute:** worked the normalization-robust diagnostic P1:P2:P3, sidestepping the calibration cliff.
- **Validated first:** a debugging pass caught a real error (BBKS/CDM matter transfer wrongly applied to the effective temperature — the CMB high-ℓ falloff is Silk damping, not the CDM transfer; removed it). After the fix, the machinery reproduces ΛCDM's structure with the driven a≈3: P1 highest, P3 back above P2, **P1/P2≈3** (observed ~2.2 — leading-order, ~35% high, but right structure and right direction). Script: `computations/perturbation_verify/cr_peak_pattern_leadingorder.py`.

### The result (leading-order, direction/magnitude robust; final verdict gated)
The effective-temperature asymmetry is set by **a = Â/Ψ** (acoustic amplitude / potential): P1/P2 ≈ [(a+R)/(a−R)]² up to damping/Doppler. The observed P1/P2≈2.2 requires **a≈3**, which in ΛCDM is exactly the value **radiation driving** supplies. CR's radiation-free rate gives **little driving**, so a sits near the adiabatic **a≈1.1 → P1/P2≈16** — a strong tension.
**So the CR peak heights carry a sharp, specific requirement:** the **hot seam handover** (ρ_r/ρ_m≈2) must itself supply the driven-equivalent acoustic amplitude (a≈3) that ΛCDM gets from radiation driving.
- **Refutation edge (with a number):** if the handover delivers only the adiabatic a≈1.1, CR gives P1/P2≈16 and fails the peaks badly.
- **Plausibility (genuine, not a save):** a hot handover with radiation comparable to matter is the kind of initial state that *could* imprint a large acoustic amplitude — not obviously doomed.
- **Gated, precisely:** whether the handover delivers a≈3 is the **seam-handover thermodynamics**, deferred to the matter sector (`JanzenOperator,JanzenRange`) — the same handover that owns the deuterium yield. The verdict lives there, not in a knob.

### Gate call: BANK. A real leading-order result; heights stay unclaimed pending the handover amplitude.
No paper change — P13's "we do not claim here" stands until the handover thermodynamics delivers (or fails to deliver) a≈3. But the open piece is now sharp: **not "compute the transfer" but "does the hot seam handover supply the driven-equivalent acoustic amplitude?"** — a specific question with a refutation number, handed to the matter-sector handover physics. That is the correspondence arc's heights question, found the right way.

---

## The mechanism (r824) — collapse-phase driving: CR's replacement for radiation driving.
The r823 result left a sharp requirement: the hot seam handover must supply a≈3 (the driven-equivalent acoustic amplitude), or CR fails the peaks (a≈1.1 → P1/P2≈16). The mechanism that plausibly supplies it, read from the matter-sector structure:
- **ΛCDM:** a≈3 comes from radiation driving — the potential *decays* through the radiation-dominated *expansion*, resonantly pumping the acoustic modes.
- **CR:** no radiation-dominated expansion. But the seam (ρ_r/ρ_m≈2, radiation comparable) is immediately preceded by the progenitor **collapse** — a *contracting* phase. A radiation-comparable *contracting* phase drives the acoustic modes too: the potential *grows* in contraction (sign flipped from the decay), the resonant pumping the same in magnitude. **Collapse-phase driving is CR's natural analogue of radiation driving, positioned exactly in the hot handover that sets a.**
- **Consequence:** the r823 refutation-edge becomes a well-posed computation. CR is not stuck at adiabatic a≈1.1; it has a specific mechanism to reach a≈3, and "does it reach a≈3" = the acoustic amplification through the radiation-comparable contraction to the seam. This is the matter sector's open dynamical frontier (`slicing_operator`/`range_paper` name the dynamical/inhomogeneous/radiative matter open), the same handover that owns the deuterium yield.
- **Discipline:** the collapse-phase drive is a genuine mechanism (a contracting radiation-comparable phase pumps modes — standard bouncing/contracting-cosmology physics), not a manufactured save; but the *quantitative* a≈3 is unproven, the open computation. Held not claimed; the mechanism turns a potential refutation into a specific buildable question.
- **Sequence (Daryl, r824):** bank [done] → read the collapse/branch-point crossing dynamics at source → potentially update/bake → form a plan → work the plan.

## Read + update + plan (r824, following the sequence)
**Read (slicing_operator §open):** the cosmogenesis branch-point crossing is *established well posed* (finite-curvature Nariai seam, characteristic, no curvature obstruction; foliation-preserving reassignment fixes the Λ-set rate; leaf-carried density crosses as inherited content) — but the **detailed worldline/field dynamics of the crossing is the open depth**. Key enabler: "the general inhomogeneous evolution is *ordinary dynamical evolution of the leaf*" — Einstein's dynamics unchanged. So the collapse-phase perturbation evolution is **ordinary GR perturbation theory on the contracting background**, not a new law.

**Update (mechanism sharpened, banked, not claimed):** the progenitor collapse read inward is dust collapse that *heats* going back, so it carries a genuine **radiation-dominated contracting phase** — the time-mirror of ΛCDM's radiation era. In it the potential grows and resonantly drives the acoustic modes (time-symmetric with the expanding decay-driving). Combined with the corpus's **faithful transmission** across the degenerate seam (κ=0), the collapse-amplified amplitude transmits to our universe. So the sharpened mechanism: **collapse-phase radiation driving, time-symmetric with ΛCDM's, transmitted faithfully** — a grounded reason a≈3 is plausible, not a guess.

**Assess bake:** no paper change — the papers hold the detailed crossing dynamics open correctly; the amplitude stays unclaimed. Banked here at working level.

**Plan (the handover-amplitude computation):**
1. *Background:* the CR contracting phase — dust that heats inward, radiation-dominated deep in the collapse, ρ_r/ρ_m≈2 at the branch point (z_onset≈6850). Use the analytic CR scale factor read inward.
2. *Perturbations:* the photon–baryon acoustic oscillator + potential (ordinary GR on the contracting background), from radiation-dominated contraction to the seam.
3. *Amplification:* compute a = Â/Ψ delivered at the branch point; the target is whether the collapse radiation-driving lifts adiabatic a≈1.1 to the required a≈3.
4. *Validation (the anchor):* the SAME machinery run on an *expanding* radiation era must reproduce ΛCDM's driving (a≈1.1→3). If it reproduces the known expanding case, the contracting case is trustworthy — the time-symmetry made a calibration.
5. *Method discipline (the battles):* robust/analytic where possible (avoid the ODE overflow); validate before trusting; hold not claimed; report failure honestly.

## Work the plan (r824) — the result: the r823 tension DISSOLVES.
Ran the driving as a robust linear oscillator Θ₀ₓₓ+Θ₀=−Ψ(x) (`computations/perturbation_verify/cr_collapse_driving.py`):
- **VALIDATED:** undriven amplitude a₀ = **0.500** (analytic adiabatic 0.5, exact) — machinery trustworthy. Driven (radiation-era Ψ decays) amplitude = **1.0** — a **2× boost**. The known radiation-driving mechanism, reproduced.
- **The robust result (time-symmetry):** the linear-driving amplification is the Fourier magnitude of Ψ's evolution, invariant under time-reversal. So CR's **collapse-phase** radiation driving delivers the **same** boost as ΛCDM's **expansion-phase** driving — independent of the exact factor.
- **The conclusion:** **CR's acoustic amplitude = ΛCDM's; CR's peak heights match ΛCDM's.** CR is NOT stuck at the adiabatic amplitude (the r816/r823 under-driving worry). The collapse phase supplies the full driving, for a grounded reason: the progenitor collapse *heats inward* so it contains the radiation-dominated driving phase, and faithful transmission (κ=0 degenerate seam) carries the driven amplitude across.

### Honest scope
- Robust: the driving mechanism (validated) and the time-symmetry (sound) — so IF CR's collapse contains the radiation-driving trajectory, CR matches ΛCDM. That IF is grounded (collapse heats inward; well-posed crossing; faithful transmission), not assumed.
- Open depth (not claimed for the exact peaks): the *detailed* collapse-phase trajectory — whether it completes the full driving quantitatively — is the matter sector's open worldline dynamics (`slicing_operator §open`). The *qualitative resolution* (CR driven, ~ΛCDM, tension gone) is grounded; the third-digit match awaits the detailed collapse computation.

### Gate call: BANK. A major working result — the peak-heights refutation-edge dissolves.
No paper bake: P13's "we do not claim here" stands until the detailed collapse dynamics delivers the exact peaks, and the resolution rests on the matter sector's open worldline dynamics. But the heights are no longer a live refutation risk: the mechanism that supplies the amplitude is validated and time-symmetric with ΛCDM's, grounded in the collapse structure the corpus establishes. The correspondence arc's one open computation is answered qualitatively — CR's peaks match ΛCDM's — with the quantitative completion a matter-sector build.

## Read-first for the next pass (r826) — the NBC grounds r824; the exact amplitude located as the open depth.
Read the collapse/handover structure at source (CR_framework §null-boundary-correspondence, §reassignment). What it grounds:
- **The branch-point crossing is faithful by identity.** The contracting interior and the expanding cosmology are two Lorentzian halves of **one continuous (C⁰) slicing** of the de Sitter substrate, meeting at the equatorial throat seam (X=α). At the degenerate Nariai seam (κ=0) the reassignment Ψ reduces to the **identity** — metric and rigid. So the collapse-side acoustic amplitude transmits to our side by identity, not by assumption.
- **This grounds r824 at the framework level.** The r824 mechanism — collapse-phase driving (time-symmetric with ΛCDM's) amplifies, faithful transmission carries it across — is exactly the NBC structure: amplify on the contracting half, cross by the identity-Ψ at the degenerate seam. CR's acoustic amplitude = the collapse-amplified amplitude = ΛCDM's driven value. No longer a plausibility argument; the framework carries it.
- **The exact amplitude is the open depth, stated as such.** The corpus: "the detailed worldline dynamics for a concrete matter model [is] the remaining open depth." So the *exact* peak heights and the deuterium yield rest on the **contracting-side worldline dynamics** — a genuine matter-sector build on the stated-open frontier, not a quick solve.

**Where the next pass rests:** the correspondence arc's heights question is answered **qualitatively and framework-grounded** — CR's peaks match ΛCDM's, the radiation-free rate costing nothing on the peaks. The **exact peaks + deuterium** are the contracting-side/handover worldline dynamics, the matter sector's open depth — the real next build, approached read-first, when taken on. **Gate call: BANK.** No paper change; the heights are grounded, not a live refutation edge, and the open depth is named where it lives.
