# P15 — CR_cosmology — CLAIMS inventory & eleven-avenue worksheet
*Whole-read at source completed r1388 (Arthur). Full gamut to run; nothing enacted yet.*

## Whole-read digest
Empirical heart of the corpus. Develops CR's cosmology + scalar perturbation sector.
Thesis (stated as a controlling quote): the CR primordial scalar spectrum FACTORIZES — the de Sitter
substrate determines its STRUCTURE, the progenitor collapse supplies its CONTENT (A_s, n_s), the seam's
null-and-degenerate geometry assigns each its job. Maturity marks in prose: established / argued / open.
- **sec:background** — causal reassignment selects Nariai (ΛG²M²/c⁴=1/9); proper-frame cosmology derived
  (5 steps, E=1 congruence) → r(τ̃)=(2^{1/3}/√Λ)sinh^{2/3}; exact flat-ΛCDM recovery, amplitude a Λ-length;
  Friedmann H²=(Λc²/3)coth²; Ω_m/Ω_Λ=csch² (density = clock); three-level rule L1(foliation stacking,
  geometric stacking)/L2(leaf local, radiation gravitates)/L3(E=1 projection); Hubble tension dissolved +
  acoustic scale a one-parameter accommodation on ρ_r/ρ_m≈2; BAO ladder (SDSS DR12 χ²≈1.7 vs 49; DESI DR2
  χ²/dof≈1.0 vs 14).
- **perturbation sector** — prop:subhorizon (modes sub-horizon at seam); sec:coherence (null seam →
  characteristic data → one phase/mode → coherence comb Δℓ≈296; time-reversal driving equality; ~8-9%
  damping-scale signature θ_D/θ_*≈1.08×ΛCDM, r_s=144.0 vs 144.4); prop:amplitude (substrate vacuum ~10⁻¹²²
  vs A_s~2e-9); prop:throat (Nariai near-horizon dS₂×S², radii 1/√Λ, no-hair isotropization, tower
  m²/H²=ℓ(ℓ+1)); prop:flat (const-τ slice flat R³) + low-ℓ floor (ℓ_L≈√(L(L+2))D_C/r₀, ℓ₂≈7.8, deficit
  ≈0.47/0.41 at ℓ=2/3, Δ(-2lnL)≈+1.8 = wash); prop:transmission + prop:transmit (degenerate Nariai κ=0 →
  power-law tortoise → scale-free → transmits progenitor spectrum; non-degenerate → exponential → imprints
  n_s→1).
- **predictions / open frontier / discussion / conclusion** — economy-of-assumption vs inflation (requires
  vs permits); Hubble-Eddington radius as independent Λ handle; open: end-to-end transfer, low-ℓ depth,
  progenitor spectrum, likelihood model-selection, matter-crossing dynamics.

## AVENUE 11 — claim → receipt inventory (all 16 receipts located; TRACE+RUN pending)
| # | claim (§) | cited receipt | path | status |
|---|-----------|---------------|------|--------|
| 1 | prop:subhorizon k_hor≈0.010 vs k_peak≈0.022 (§sub) | verify_numeric.py (anchor 7) | computations/perturbation_verify/ | ✔✔ |
| 2 | coherence comb Δℓ≈296 coherent vs washed-out (§coherence) | verify_coherence_comb.py | perturbation_verify/ | ✔✔ |
| 3 | time-reversal driving equality \|Ψ̃(ω=1)\| invariant (§coherence) | cr_collapse_driving.py | perturbation_verify/ | ✔✔ |
| 4 | peak ratios P1/P2≈2.2, P2/P1≈0.45, P3/P1≈0.44 (§coherence) | camb_reference.py | computations/peak_heights/ | ✔✔ |
| 5 | ~8-9% damping: θ_D/θ_*≈1.08×ΛCDM, r_s=144.0 vs 144.4 (§coherence) | damping_ratio_clean.py | peak_heights/ | ✔✔ |
| 6 | damping non-reabsorption r_D∝ω_b^{-0.31} (§coherence) | damping_reabsorption.py | computations/damping_tail/ | ✔✔ |
| 7 | high-ℓ deficit under assume-equal-peaks shortcut (§coherence) | full_transfer_verdict.py | damping_tail/ | ✔✔ |
| 8 | prop:amplitude Λℓ_P²≈3e-122, vacuum ~10⁻¹²² vs A_s (§amplitude) | verify_numeric.py (anchor 5) | perturbation_verify/ | ✔✔ |
| 9 | prop:throat dS₂×S² radii 1/√Λ, f''(r⋆)=-2Λ (§throat) | verify_geometry.py (anchor 2) | perturbation_verify/ | ✔✔ |
| 10 | throat tower m²/H²=ℓ(ℓ+1), ν=½ base, ν²<0 for ℓ≥1 (§throat) | verify_throat_tower.py | perturbation_verify/ | ✔✔ |
| 11 | prop:flat const-τ slice flat R³, Riemann=0 (§largescale) | verify_geometry.py (anchor 1) | perturbation_verify/ | ✔✔ |
| 12 | low-ℓ floor ℓ_L, D_C≈13927, r₀≈5064, stretch 2.75, ℓ₂≈7.8 (§largescale) | verify_closedS3_nonsync.py | perturbation_verify/ | ✔✔ |
| 13 | HZ weight w_L=(L+1)/(L(L+2)); continuum recovery (§largescale) | verify_lowell_exact_measure.py | perturbation_verify/ | ✔✔ |
| 14 | Boltzmann deficit ≈0.47/0.41 at ℓ=2/3, recover by ℓ≈7 (§largescale) | verify_lowell_boltzmann.py | perturbation_verify/ | ✔✔ |
| 15 | Doppler low-ℓ ratio near unity (§largescale) | verify_doppler_lowell.py | perturbation_verify/ | ✔✔ |
| 16 | low-ℓ likelihood Δ(-2lnL)≈+1.8 (+0.3..+3.8); MC ~3.4σ (§largescale/scope) | confront_lowell_data.py, verify_lowell_likelihood_v2.py | perturbation_verify/ | ✔✔ |
| 17 | prop:transmission tortoise integrals p=1 log/exp vs p=2 power-law (§transmission) | verify_geometry.py (anchor 4) | perturbation_verify/ | ✔✔ |
| 18 | BAO: SDSS DR12 χ²≈1.7 vs 49; DESI DR2 χ²/dof≈1.0 vs 14 (§tensions) | hubble_expansion_confrontation_v2.py | hubble_build/ | ✔✔ |
Non-receipt (derivation/structural, verify by trace not a .py): eq:scalefac 5-step derivation; eq:amplitude
2^{1/3}/√Λ; eq:rate/eq:omega-ratio; prop:transmit (structural consequence of prop:transmission).

## AVENUES 1–10 — first-pass observations (off the whole-read; to execute)
- **A1 Q-mine:** paper is disciplined (established/argued/open marks). Candidate scan: none glaring on first pass; verify no caution lowers a claim without adding a result.
- **A2 own accomplishments:** strong candidates already owned (Hubble-tension dissolution as discriminating datum; transmission dichotomy as a proof; the requires-vs-permits verdict). Check nothing earned is undersold.
- **A3 press the gap:** the honest edges are already sharply drawn (the ~8% damping signature's observable consequence "genuinely open"; high-ℓ transfer unbuilt; low-ℓ a "wash"). Check no residual overclaim in the peaks-match / economy verdict.
- **A4 identity:** title = "The cosmology of Cosmological Relativity: the expansion history…, the cosmogenesis seam, and the scalar perturbation sector." Reads at weight; confirm.
- **A5 positive-face:** leads on what's established/inherited-division-of-labour. Confirm the inflation contrast leads positive (requires) not merely negative (inflation-permits).
- **A6 symmetry:** Nariai parity-conjugate pair named (M>0 vs M<0, r↦−r); three Λ-scales kept apart (α, α/√3, amplitude). Check no conjugate dropped in the seam/branch-point discussion.
- **A7 bespoke (two-way, post-P6):** forward — P15's requires-vs-permits reading is a bespoke instance of P6's theory-choice engine (already cited JanzenShadowExistence). Backward — apply P6's least-arbitrariness/world-vs-description to P15's opens (esp. the inherited-datum status).
- **A8 dissolution census:** dissolves — Hubble tension, coincidence problem, horizon problem (causal contact), flatness, r=0 singularity (→ finite-curvature seam), inflation's necessity. Census at weight, verify at source.
- **A9 checklist:** entry-point signs for the 4 named opens; unification-placement recap (P15's piece into P7's synthesis); idiom (Hubble-Eddington radius rename already in); 3d defrag.
- **A10 forward-refs:** dense already (P1,P3,P4,P5,P6,P7,P8,P9,P11,P14,P16,p0). Check completeness + deliberate pointer structure.

## STATUS r1396: 20 claims ✔✔. BAO/Hubble flagship DONE: hubble_expansion_confrontation_v2 (SDSS DR12: CR 1.71, LCDM(73) 49.45; H0-independence exact) + desi_dr2_confrontation (DESI DR2: CR chi2/dof=1.00 Om=0.307, LCDM(73)=13.70; was uncited by name -> now cited). NEXT: derivation/structural claims by trace/sympy -- eq:scalefac (5-step E=1 -> sinh^{2/3}), eq:amplitude (2^{1/3}/sqrt(Lambda) at Nariai), eq:rate/eq:omega-ratio (Friedmann coth^2/csch^2), prop:transmit.

## AVENUES 1–10 — EXECUTED r1398 (off the whole-read, at source). VERDICT: all ten pass; no edits warranted, no red-flags.
- **A1 Q-mine — PASS.** No boundary rhetoric without standing. The hedges present ("still owed", "not yet in hand", "genuinely open") are honest maturity calibration, not softening to strip. "Licensed by the representational freedom" etc. are grounded assertions (cite CRframework), not filler.
- **A2 own accomplishments — PASS.** Earned results claimed at weight: transmission dichotomy "the decisive result"; Hubble resolution "a discriminating datum, not a tie"; standing "stronger than rule-favoured-awaiting-the-datum". "Even" on peak heights is correct (CR matches, not beats), and the match is separately claimed (time-reversal equality "carries the peak heights ... flat LCDM's exactly"). Nothing undersold.
- **A3 press the gap — PASS.** Overclaim guard is exemplary: "The verdict this licenses must be drawn on the right axis, and confined to it." Theory-choice (decidable now, falls to CR) is cleanly separated from data (begun to move, first discriminating result, fuller confirmation owed). Earlier watch-point (abstract's "empirically favoured") RESOLVES on the Discussion's precise scoping ("A theory that fits is not a theory confirmed"). No residual overclaim.
- **A4 identity — PASS.** Title = the cosmology + the seam + the scalar perturbation sector; body and abstract deliver exactly that, at weight.
- **A5 positive-face — PASS.** Inflation contrast leads positive (requires-vs-permits; CR recovers from Lambda alone), dichotomy stated as what CR structurally IS (no attractor / no consistency relation / no B-modes), not mere refutation. "A framework is credited for requiring the structure it explains, not faulted for measuring the boundary data it does not."
- **A6 symmetry — PASS (emphatic).** The seam conjugate is NOT dropped: eq:scalefac is one analytic curve, expanding = real branch tau>0, seam tau=0 = branch point, tau<0 conjugate carried as the progenitor collapse leg (phase 2pi/3, Fig scalefac3d); the paper guards it ("forcing r real manufactures a cusp the smooth curve does not carry"). Three Lambda-scales (alpha, alpha/sqrt3, amplitude) kept apart throughout. M>0/M<0 parity pair named.
- **A7 bespoke two-way — PASS.** Forward: requires-vs-permits is a bespoke instance of P6's theory-choice engine, woven (cite ShadowExistence at the verdict). Backward: P6's world-vs-description applied to the open inherited-datum status (A_s, n_s "inherited exactly as LCDM inherits the baryon-to-photon ratio ... of the same kind and count ... the two stand level").
- **A8 dissolution census — PASS (at weight).** Hubble (CONFIRMED, receipt); coincidence (GROUNDED, csch^2 density=clock, "we exist at a time of order the geometry's single timescale"); horizon/causal-contact (GROUNDED, throat + null seam); flatness (CONFIRMED, prop:flat); r=0 singularity (GROUNDED, finite-curvature seam = branch point); inflation's necessity (CONFIRMED, transmission dichotomy). Lithium honestly NOT dissolved ("shared with flat LCDM").
- **A9 checklist — PASS.** 4 opens flagged with entry points (sec:scope); unification-placement recap present (Discussion: "one thing seen from several sides", threading CRframework/ShadowExistence/Operator/Slicing); Hubble-Eddington idiom in; 3d defrag = Fig scalefac3d.
- **A10 forward-refs — PASS.** Dense, deliberate: BHcausality, Slicing, ModernParallax, Groupoid, ShadowExistence, CRframework, Operator, GeometricCore, Cosmogenesis + Janzen2015 + external (Silk, Eddington, Lemaitre, PavlidouTomaras). Each open points forward; each dissolution points to its source paper.

## P15 FULLY SWEPT (r1398): avenue 11 (19 receipts, every computation run) + avenues 1-10 (all pass). P15 is the most-worked paper in the corpus and it shows: nothing warranted an edit on the framing/claim axes.
