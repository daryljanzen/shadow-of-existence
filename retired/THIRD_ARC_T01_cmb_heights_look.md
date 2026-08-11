> **⌖ RETIRED r1553.** This was a lookahead for the CMB-heights transfer (r817) — superseded by `THIRD_ARC_T01_heights_firstrun`, which is item 2's build material.
> Kept as record; **do not work from it.**


# Third arc, T0 — the correspondence sector: what is actually built (corrected read)

*Surveyed r816, first pass; **corrected r817** after a proper read of P13's perturbation sector and its receipts (Daryl's mirror-check: the first pass grep-skimmed an unfamiliar piece and badly overstated its openness). This is the accurate state.*

## Correction of the r816 framing
The r816 look called the CMB "barely started, a major computation not yet begun, the sharpest place CR can be refuted." **Wrong.** The perturbation sector is extensively **built and verified**, with receipts in `computations/perturbation_verify/` (nine scripts) and `hubble_build/` (two). The spearhead already confronted it with data to "favoured-and-awaiting." I mistook a room I was standing in for new territory.

## What is ESTABLISHED (P13, receipt-backed)
- **Coherence** (§coherence): acoustic phase coherence from the null seam (one characteristic phase per mode); the sharp comb Δℓ≈296 vs washed-out incoherent — `verify_coherence_comb.py`.
- **Classical amplitude** (§amplitude, prop:amplitude): the substrate de Sitter vacuum (~10⁻¹²²) is negligible against observed A_s≈2×10⁻⁹ — by 10¹¹³. The fluctuations are progenitor-supplied, classical, not the stretched vacuum. `verify_numeric.py`.
- **Throat isotropization** (§throat, prop:throat): dS₂×S² no-hair damps every ℓ≥1 (heavy principal series), only the monopole survives. `verify_throat_tower.py`. **Load-bearing guard:** the throat-tower index is the near-horizon S²-harmonic degree, NOT the CMB multipole — conflating them manufactures a false prediction. The map is §largescale.
- **The low-multipole floor** (§largescale — "its sharpest large-scale statement, the load-bearing piece established"): the flat/discrete decoupling (prop:flat, the observer slice exactly flat ℝ³, Ω_k=0), the closed-S³ discrete spectrum projected through the *flat* Bessel (not the hyperspherical transfer), placing the lowest mode at ℓ₂≈7.8 (from D_C/r₀≈2.75, parameter-free: D_C≈13927 Mpc, r₀≈5064 Mpc). `verify_geometry.py`, `verify_lowell_exact_measure.py`, `verify_closedS3_Cl_exact.py`, `verify_doppler_lowell.py`, `verify_lowell_likelihood.py`.
- **Transmission** (§transmission, prop:transmission): the degenerate (κ=0) seam gives a power-law (not exponential) approach — faithful transmission of the progenitor spectrum, no thermal imprint, no scale-invariant attractor. `verify_geometry.py`.
- **The matter crossing** (§scope): well-posed, isotropizing, structural transition law — established, and the detailed dynamics advanced by Phase 1 (r810–811).

## What is CONFRONTED with data (the spearhead, "favoured-and-awaiting", data-limited)
- The low-ℓ deficit: lands the quadrupole strikingly, **over-predicts the ℓ=3–4 suppression** (cosmic-variance-limited) — the *known* exposed risk, already on the table.
- The radiation-free rate (E4): the knob-free CR-vs-ΛCDM discriminator, H₀-independent — established before the spectrum.
- The abundances (F1): first sample favourable, deuterium the sharp constraint.

## What is genuinely OPEN (the one piece)
- The peak **heights** — full sufficiency awaits the *complete seam-to-recombination transfer* (§coherence, "we do not claim here"). This is the one open buildable computation. The radiation-driving question (CR's no-radiation-dominated-era vs ΛCDM's peak boosting) is a *plausible consideration* for this one open piece — not, as r816 framed it, the whole correspondence. It is held honestly open (ρ_r≈2ρ_m present at the seam; the radiation-free rate makes the potential evolution non-standard); only the transfer settles it.

## The accurate course through the sector
The correspondence is **largely confronted, favoured-and-awaiting** — the turn to the sky already happened, via the spearhead. What genuinely remains, accurately:
1. **The one open computation:** the seam-to-recombination transfer for the peak heights (a real build, the matter sector unblocks its start). Guard: respect the throat-index-≠-multipole rule; don't manufacture.
2. **The landing (the arc's real remaining WORK):** dissemination — the book, publication — carrying an already-largely-confronted, favoured-and-awaiting cosmology (plus the complete matter sector) to the world for the data-discrimination verdict that is genuinely the world's.

So the third arc is not a fresh confrontation barely begun; it is a largely-confronted correspondence with one open transfer computation and a landing. The chart is corrected accordingly.

## Gate call: BANK (corrected survey). No paper change — P13 already marks each result at its right maturity; the correction is to my own map, not the corpus.
