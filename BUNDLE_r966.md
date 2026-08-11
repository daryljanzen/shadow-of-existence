# Bundle r966 — the empirically-favoured arc, the damping correction, and the open-items triage

Covers r959 → r966. Everything below is baked, compiled clean (0 undefined), and stated for reversal.

## The milestone (r959–r964): CR is empirically favoured, baked corpus-wide
- **A1.4 / DESI DR2 (r961→r965):** the radiation-free rate resolves the Hubble tension across the
  full BAO ladder. Confronted with the state-of-the-art **DESI DR2** (13 measurements, 7 tracers),
  CR fits at **χ²/dof ≈ 1.0** with one CMB-calibrated Ω_m = 0.307 (ρ_r/ρ_m ≈ 2.0) at the local
  H₀ = 73, where ΛCDM breaks (χ²/dof ≈ 14). Receipts: `hubble_build/hubble_expansion_confrontation_v2.py`,
  `desi_dr2_confrontation.py`.
- **D1 abundances (r955–r957):** the Big Bang computation — a validated multi-nuclide network on the
  cooling leg — produces D and He-4 within 1σ at the Planck η (StarLib-precise); Li the shared
  standard problem. `computations/p16_bbn/`.
- **A1.2 octopole (r962):** the low-ℓ shape, on a genuine Boltzmann transfer, is a
  cosmic-variance-limited **wash** (Δ(−2lnL) ≈ +1.8), not the old falsification edge.
- **Baked corpus-wide (r964):** coherence → correspondence → confirmed-prediction on several axes,
  in P15/P16/P7/P6/p0 and the meta-docs; structural unification held, still, at coherence.

## The damping-tail saga — and its correction (r965 → r966)
- **What's solid:** the radiation-free rate makes the Silk **diffusion scale ~8% larger**
  (`damping_ratio_clean.py`, `damping_tail_signature.py`), and it is **not reabsorbable** by ω_b
  within BBN + peak-height priors (`damping_reabsorption.py`).
- **The over-reach, caught by Daryl and reverted:** r965 escalated this to a "several-σ sharpest
  edge" and then a "near-refutation," via a transfer pass that **assumed CR's high-ℓ peaks equal
  ΛCDM's** — exactly the unbuilt part, not a free input. Reverted across P15/P16/P7/ONTOLOGY/meta-docs.
- **The deciding transfer, attempted and reclassified (r966):** the validation gate (reproduce
  ΛCDM's full peak-height tail semi-analytically) **failed**; CAMB structurally cannot represent CR's
  radiation-content/rate split; and the high-ℓ driving is gated on CR's **unbuilt perturbation
  sector**. So the damping-tail sign is a genuine **frontier build**, not a tractable shortcut.
  `cr_hiell_transfer.py`, `full_transfer_verdict.py` (conditional, not a verdict), `crossed_wire_hunt.py`.
- **Honest status, everywhere:** a computed, non-reabsorbable ~8% CR-specific effect in the diffusion
  *scale*, its observable high-ℓ consequence **genuinely open**. The path to settle it is stated as a
  debt in P15 §scope and left there.

## Tractable computations spent (r964–r966)
- **C9 / A6.3:** non-spherical matter functionals + EoS collected (KS verified vs eq:ksrho; Weyl
  fluid U-bend + strut γ-bend). `matter_functionals_C9.py`, baked P9.
- **C6/C7 B-series:** overcritical low-point doesn't cap (−2α/√3 is the threshold, not a ceiling);
  ellipse foci at ±2/√3 = Nariai points. `bseries_C6_C7.py`.
- **Contained-build sweep (r966):** **B-4** charge-as-the-bend (RN-dS = exact Maxwell stress-energy;
  C4 closed) · **B-5** no strut-free accelerating vacuum (strut ∝ mA, Λ-independent axis) · **B-6**
  Λ>0 singularity-theorems confrontation (CR consistent — incompleteness at the finite-curvature
  seam) · **B-8** SNe Ia non-discriminating (D_L = flat-ΛCDM to <2e-4) · **B-9** peak temperature
  **T_pk ≈ 170 MeV** (QCD scale, M-independent), baked P16 §peak. Left with the matter sector: B-2,
  B-3 (fermion frame); left with Daryl: B-7 (P6 base-rate first-programme).

## Housekeeping (r966)
- **P convention fixed corpus-wide:** P ≡ mass-reflection/orientation parity r₀→−r₀ = R = γ⁵
  (spacelike, horn-preserving); the areal-radius spatial parity r→−r (γ¹γ²γ³, anticommutes with γ⁵)
  is never written P. Stated in P13 body; the r918 collision note marked resolved.
- **THE_PLAN punch-list currency:** items 1–3 were done at r933/r934 (were still listed as blockers);
  only the references pass (AB-1) and the frontier-vs-chore pass remain above the line.
- **P15_16_CLOSEOUT P15-1 reconciled:** the r945 "radiation-included / +8% is a trap" reading is
  superseded — the three-level rule settles the diffusion as L1 radiation-free; the flip-flop itself
  is recorded as why the +8% is delicate.
- All figures confirmed present (0 missing); all touched papers recompile clean.

## Where the corpus stands
At the "only genuine problems remain" bar. Above the line: the references pass (queued for the
ship window) and the frontier-vs-chore triage (done — everything below publishes-open). The frontier
— matter-sector content, the perturbation sector, quantum completion, the data-gated verdicts — is
the honest open edge, published as such. `TRACTABILITY_SWEEP.md` and `OPEN_PROBLEMS_MAP.md` carry the
live inventory.
