> **⌖ RETIRED r1546.** This was the tractability sweep (r958, Daryl-directed) — what can actually be computed. **Its verdicts fed the plan's lanes** and the open-problems map's readiness sort, which is the runway Lane 1 came from.
> Kept as record; **do not work from it.**


# The tractability sweep (r958, Daryl-directed) — what else is a built computation sitting unspent

**The trigger.** D1 (the Big Bang computation) and its two follow-ons — the abundance likelihood and
the StarLib precision upgrade — were each *currently tractable* and, spent, turned "argued" into
"confirmed against data" (D and He-4 within 1σ of the measured primordial values at the Planck η,
the lithium problem shared). Daryl's bar refinement: **the first edition owes not just P16's title
earned, but nothing *tractable* left unspent.** So sweep the corpus/plan for every item that is a
*built computation buildable now* — as against a genuine frontier or a data-gated wait — and run them.

**The discriminator (three buckets).**
- **A — TRACTABLE NOW:** a concrete numerical/symbolic computation buildable today with in-sandbox
  tools (numpy/scipy/**sympy**, **CAMB** ✓ installed, **pynucastro** ✓, existing corpus scripts), no
  new physics, no unavailable data. *These are owed.*
- **B — GENUINE FRONTIER:** needs the matter sector / a not-yet-existing derivation, or is
  fundamentally data-gated (waiting on a measurement, or on data not reachable here). Not buildable now.
- **C — SCHOLARSHIP:** citations, figures, terminology.

Enabling tools verified this pass: **CAMB 1.6.6** (installs, runs — gates the CMB items),
**pynucastro** (the BBN network), sympy/numpy/scipy. Restriction that bites: **public observational
datasets** (BAO tables, SNe catalogues, the Planck high-ℓ likelihood) are not freely fetchable in the
sandbox — small *compressed* tables (a dozen BAO points, ~30 H(z) chronometers) can be entered from
published values; full catalogues/likelihood codes cannot. This splits some CMB/expansion items.

---

## BUCKET A — tractable now (the owed computations), ranked by impact

1. **A1.4 / E4-ext · The radiation-free rate vs the full late-time expansion history.** The L1
   sinh$^{2/3}$ rate that dissolves the Hubble tension, confronted against BAO ($D_M/r_s$, $D_H/r_s$,
   DESI/SDSS) + cosmic-chronometer $H(z)$ + (compressed) SNe. *Build:* astropy/CAMB distances + a
   scipy likelihood over the compressed data points (enterable). *Impact:* the **data-side companion
   to D1** — the same "confirm against data, not by ΛCDM-analogy" move, on the very rate that resolves
   Hubble. Partly data-limited (full SNe catalogue out of reach) but the compressed BAO+$H(z)$ leg is
   buildable and decisive. **Highest value; ties to the Hubble-completion story.**
2. **A2.3-damping · The damping-tail signature through CAMB.** P15 holds the ${\sim}8\%$ larger
   $\theta_D/\theta_*$ (radiation-free diffusion) **not claimed pending the high-ℓ likelihood**.
   *Build:* CAMB with the radiation-free vs radiation-included recombination-era rate → quantify
   $\theta_D/\theta_*$ and where the $\sim\!8\%$ sits against Planck's high-ℓ error envelope. Turns a
   not claimed into a computed number. (Full model-selection needs the Planck likelihood = data-gated;
   the *quantification* is tractable.)
3. **A1.2 · Low-ℓ octopole / exact large-angle shape.** The exact closed-$S^3$ hyperspherical (or full
   Boltzmann) large-angle transfer, firming the octopole falsification verdict. *Build:* extends the
   existing `verify_closedS3_Cl_exact.py` / `verify_lowell_*` machinery to the exact shape. Computation-
   complete; the *verdict* is cosmic-variance-limited (data-gated), but the exact-shape solve closes the
   last `[reading]`.
4. **A6.3 / C9 · Explicit matter functionals + equations of state.** Stress-energy functionals and EoS
   for the homogeneous (Kantowski–Sachs) and axisymmetric (Weyl) cut classes. *Build:* symbolic
   Einstein-tensor → $T_{\mu\nu}(\text{cut})$, read EoS (sympy). Method established; only the systematic
   collection remains.
5. **Small self-contained symbolic-GR items (B-series / C6,C7,C4).** **C6/B.1** overcritical low-point
   size law (does it cap at a clean multiple of α?); **C7/B.2** A/B null generators ↔ ellipse foci at
   $\pm2/\sqrt3$; **C4/B.3** charge/rotation folded into the slicing-curve picture (RN–dS / Kerr as the
   bend); **A4.9** the Λ-dependence of generation three-ness. *Build:* sympy turning-point / embedding
   scans. Low individual impact, genuinely closeable, cheap.
6. **A4.7 · Zero-mode continuation onto the cosmological leaf** (concrete model) and **the bent-cut
   spinor vielbein** (the $M\neq0$ frame the $R=\gamma^5$ derivation deferred). Contained, buildable.

## BUCKET B — genuine frontier (not buildable now; the bar's honest below-the-line)

- **The matter sector's content** (A4.1–A4.6: gauge/colour su(3)⊄so(5,1), the mass hierarchy, the
  colour-from-geometry universal) — the hinge; unbuilt physics.
- **A2.2 / F1 · Derivation of the inherited data** (η, ρ_r/ρ_m, $A_s$, $n_s$, the progenitor spectrum,
  and the *contracting-phase thermal history* that would let the abundances be derived rather than run on
  the inherited η) — gated on the matter/handover sector. *Note: this is the one that would let D1's η
  itself be predicted; it is genuinely frontier, not tractable now.*
- **The two CMB "early-universe" open problems** (the oscillating medium / $c_s(z)$; the exact seam-vs-
  recombination placement and the $r_s$ integration limit) — need the medium construction (matter sector).
- **A1.1/A1.3/A2.1 · The decisive data verdicts** (P1 no-horizons; full-spectrum CR-vs-ΛCDM model
  selection; the multi-abundance likelihood *verdict*) — data-gated: the world judges, and the deciding
  data/likelihood is not reachable here.
- **A3 quantum completion; A6.2/A6.4 interior remainder + grand claim; A6.1 beyond-the-wall** — gated on
  the matter sector or open-ended.

## BUCKET C — scholarship/hygiene
- **E.1/H2 citation audit; E.2/H1 figure sweep; D.2 terminology; D.3 the "P"-symbol collision.**

---

## Verdict of the sweep
The tractable set is **one high-value data-confrontation (A1.4/E4-ext, the Hubble-rate vs expansion
data), one CMB quantification (A2.3-damping, the ~8% via CAMB), one exact-shape solve (A1.2 octopole),
and a cluster of self-contained symbolic-GR computations (matter functionals + the B-series).** These
are what "nothing tractable left unspent" now means for the first edition. Everything the corpus itself
calls the frontier — the matter sector, the derivation of the inherited data, the quantum completion —
is genuinely gated, and the sharp *data verdicts* are data-gated (the world's to judge), not
computation-gated. **Recommended spend order: A1.4 → A2.3-damping → A1.2 → matter functionals → B-series.**
*Stated for reversal.*

---

## SPEND LOG (what has been run)
- **A1.4 ✓ SPENT (r961→r963).** The radiation-free rate vs the full BAO expansion history — built (`hubble_build/hubble_expansion_confrontation_v2.py`), **resolves the Hubble tension**: CR fits DR12 at the local $H_0=73$ (χ²≈1.7) where ΛCDM cannot (χ²≈49), the invariant the dimensionless $\Omega_m$ (a hidden-FLRW-$\omega_m$ assumption caught and corrected). Baked P15 §tensions + `fig_hubble_bao`. **Empirically-favoured milestone; item 1 of the sweep.**
- **A1.2 ✓ SPENT (r962→r963).** Low-ℓ octopole exact shape — built on the **genuine Boltzmann transfer** (`computations/perturbation_verify/verify_lowell_boltzmann.py`, CAMB's $\Delta_\ell(k)$ = CR's transfer): depth $\sim0.47/0.41$ at $\ell=2,3$, recovering by $\ell\!\approx\!7$; the old "octopole falsification edge / striking quadrupole match" corrected to a **cosmic-variance-limited wash** (likelihood recomputed, `verify_lowell_likelihood_v2.py`: Δ(−2lnL)≈+1.8 central, a wash). Baked P15 §largescale + corpus-wide. **Closes the last low-ℓ `[reading]`.**
- **A2.3-damping ✓ ALREADY SPENT (peak-heights arc) + INDEPENDENTLY RECONFIRMED (r964).** The sweep listed this as "turn a not claimed into a computed number," but the number was **already computed** during the peak-heights arc (`computations/peak_heights/damping_ratio_clean.py`) and **already baked into P15 §coherence**: the radiation-free rate is ~15% below the radiation-included one at recombination ($\rho_r/\rho_m\approx0.3$), so the diffusion length runs **~9% longer** while $r_s$ is matched to the acoustic scale → $\theta_D/\theta_*\approx1.08\,(\theta_D/\theta_*)_{\Lambda{\rm CDM}}$, the ~8% signature. Reconfirmed r964 by an **independent second implementation** (`computations/damping_tail/damping_tail_signature.py`, different grid/code path, thermodynamics held fixed while only H(z) is swapped): **Silk diffusion length +8.90%**, pipeline validated ($r_s=144.01$ vs CAMB $144.44$, −0.3%). The magnitude is computed and stable across two independent codes; the only thing stated without being claimed is the **model-selection verdict** against Planck's high-ℓ likelihood, which is correctly **data-gated** (the full likelihood is not reachable in-sandbox) — not a computation gap. *So the sweep's own inventory was stale here: A2.3-damping is done.*
- **A6.3/C9 ✓ SPENT (r964).** The explicit matter functionals + EoS for the non-spherical cut classes, collected and verified symbolically (`computations/matter_functionals/matter_functionals_C9.py`, sympy): **KS** functionals confirmed exactly against P9 eq:ksrho + partners, both vacuum kernels (SdS interior + Nariai) → 0, conservation identity verified, EoS collected; **Weyl** Einstein tensor computed, Λ=0 vacuum kernel verified to vanish in all four components, off-kernel bend collected as fluid U-bend + axial-strut γ-bend (conical-defect EoS). Baked into **P9 §open** (paragraph reframed "collected," 12pp, compiles clean); map C9 entry marked collected/strike-eligible.
- **B-series C6 + C7 ✓ SPENT (r964)** (`computations/slicing_bseries/bseries_C6_C7.py`). **C6** (overcritical low-point size law): answered **negative** — no family-wide cap; the clean $-2\alpha/\sqrt3$ is the Nariai-threshold value, overcritically the backward-radial root deepens as $\sim-(2M)^{1/3}\alpha$ without bound. **C7** (ellipse foci): the horizon-locus ellipse foci sit **exactly at $\pm2/\sqrt3=\sqrt{a^2-b^2}$**, coinciding with the Nariai vertical-tangent points / the critical threshold — the ellipse side of the A/B-generator bridge is now an exact identity (the remaining P8-side cross-plane identification is low-priority, P8-flagged not-load-bearing). Map C6/C7 entries updated; P3 body already carries the substance (§ellipse/§lap), no P3 edit warranted.
- **C4/B.3 ✓ SPENT (r966).** Charge as the bend closed (`computations/matter_functionals/bseries_B4_charge.py`): RN–dS's departure from the SdS vacuum kernel is **exactly** the Maxwell stress-energy of a radial $E=Q/r^2$ field ($8\pi\rho=+Q^2/r^4$, $p_r=-Q^2/r^4$, $p_\theta=+Q^2/r^4$, traceless, vanishing at $Q=0$) — the charge is the EM bend off the same kernel C9 read neutral matter off. Rotation-as-shift ($J=Ma$) was already P9 prop:kerr. C4 collected.

## CONTAINED-BUILD SWEEP (r966, Daryl-directed: "cross off most of those builds")
- **B-4 ✓ (above)** — charge as the bend / C4.
- **B-5 ✓ SPENT.** No strut-free accelerating vacuum (`bseries_B5_strut.py`): the C-metric angular function $P(x)=(1-x^2)(1+2mAx)$ is $\Lambda$-independent ($dP/d\Lambda=0$), its poles have unequal $|P'|$ for $mA\neq0$, so a conical strut of tension $\mu\approx mA$ is irremovable — $\Lambda$ cannot regularise the axis. Acceleration is matter (the strut's $T^z{}_z=-\rho$, the conical-defect EoS C9 collected), not a vacuum parameter. Closes P9 rem:accel in the negative.
- **B-6 ✓ SPENT (confrontation).** $\Lambda>0$ singularity theorems (`singularity_theorems/B6_singularity_confrontation.md`): CR is *consistent with* the theorems — it meets their hypotheses (collapse trapped surface persists with $\Lambda$), accepts the conclusion (geodesic **incompleteness**), and locates that incompleteness at the finite-curvature Nariai seam (P1 finite-curvature species; the $r=0$ divergence a perspectival sweep-artefact, P3), denying only the folklore "⇒ curvature singularity where physics ends." Two specialised $\Lambda>0$ citations flagged for AB-1 (references pass).
- **B-8 ✓ SPENT (non-discriminating).** SNe Ia (`hubble_build/sne_consistency.py`): CR's $D_L(z)$ = flat-$\Lambda$CDM's to $<2\times10^{-4}$ across $z<2.3$ (radiation negligible), so SNe cannot discriminate — a consistency axis, not a discriminator; the discriminating late-time ruler is BAO (DESI DR2). No paper change forced.
- **B-9 ⊙ PARKED (defused).** Exact regulated peak temperature — argued downstream-irrelevant in `P15_16_CLOSEOUT` (P16-D); confirmed parked, no build warranted.
- **B-3 ✓ SPENT + BANKED in P13 (r966).** The M≠0 leaf tetrad's radial–angular spin connection $\omega^2{}_1=\omega^3{}_1=(\sqrt f/r)e$ gives the massless Dirac radial superpotential $W=\lambda\sqrt f/r$ — exactly P13's eq, now derived from the explicit frame (`B3_spinor_vielbein.py`); banked in P13 §chirality.
- **B-2 ✓ SPENT + BANKED in P13 (r966).** The explicit zero-mode continuation onto the cosmological leaf — P13's one stated open thread — carried out (`B2_zeromode_continuation.py`): $W$ real between horizons (bound wall-mode) → imaginary past a horizon (propagating cosmic-time fermion), matching the $E=1$ sinh$^{2/3}$ leaf's conformal-weight-$a^{-3/2}$ Dirac form; the three wall-modes → three propagating families, $\gamma^5$ chirality preserved. Banked in P13 §cosmogenesis (the "left for a concrete model" thread closed).
- **B-7 (P6 base-rate calibration) — ASSESSED (r966): a GENUINE RESEARCH DIRECTION, correctly left open; NOT a finite result-task, and a quick pilot would be counterproductive.** The vindication lemma's base-rate test (do rule-*required* structures beat merely-*permitted* ones, sampled across theory-choice wins AND losses) has its whole methodological weight in two non-computational parts: assembling a reference class *without selection bias*, and the contestable historical required-vs-permitted classification per episode — a standalone history-and-philosophy-of-science project. A hand-picked-dozen pilot would RECREATE the survivorship bias the programme exists to defeat (P6 §boundary is explicit: "the outcome is not presumed here"), so it would be worse than nothing. **Disposition: leave exactly as P6 has it — an honestly-marked open first-programme, publishing-open at no cost.** The one legitimately-finite move (if ever pursued) is sharpening the pre-registered operationalization + unbiased sampling protocol, not producing a number; P6 already sketches enough to stand. His to lead if/when. **This clears the last below-the-line contained item.**
- **AB-1** references pass deferred to the overnight/ship window.
- **REMAINING: A4.9** (Λ-dependence of generation three-ness) — this touches the matter sector (P14's γ⁵-graded generation index); assessed as **frontier-adjacent, not a clean geometry item**: the generation count is a topological (index) quantity, expected Λ-independent, but confirming it needs P14's index machinery, not a standalone symbolic scan. Held with the matter sector (Bucket B), not the clean-tractable B-series.

## RE-ASSESSMENT OF THE "DATA-GATED" BUCKET (r965, Daryl-prompted: is gated stuff actually tractable where we have the model + data access?)
The Bucket-B "data-gated" label was doing lazy work. Re-sorted honestly:
- **A1.4-ext / DESI DR2 BAO ✓ SPENT (r965) — was mislabeled gated.** The full late-time BAO confrontation is *tractable*: DESI DR2 (arXiv:2503.14738) publishes a compressed 13-measurement table (7 tracers, with $D_M$-$D_H$ correlations), enterable. Run (`hubble_build/desi_dr2_confrontation.py`): **CR fits at $\chi^2/{\rm dof}=1.00$** with one CMB-calibrated parameter $\Omega_m=0.307$ (at which $\rho_r/\rho_m\approx2.0$ exactly), at *any* $H_0$ incl. local 73; $\Lambda$CDM breaks at 73 ($\chi^2/{\rm dof}\approx14$). Supersedes A1.4's 3 DR12 points with the state-of-the-art dataset. Baked into **P15 §tensions** (+ DESI2025 bibitem, 22pp, compiles clean).
- **The multi-abundance likelihood VERDICT — already SPENT (r956), never actually gated.** The measured primordial abundances are a handful of published numbers (Cooke 2018 D/H, Aver 2021 $Y_p$); the joint likelihood at the Planck $\eta$ was computed: D $+1.1\sigma$, $Y_p +0.5\sigma$, Li $\sim5$--$7\sigma$ (StarLib: D $-0.5\sigma$). Done.
- **SNe Ia (Pantheon+/DES-SN5YR) — tractable but NON-DISCRIMINATING.** CR's $D_L(z)$ is the same flat-$\Lambda$CDM form ($\Omega_m$, local $H_0$), so SNe are a consistency check, not a discriminator (both are flat $w=-1$). Low value; the binned Hubble diagram is enterable if a confirmation is wanted.
- **The CMB damping-tail — reabsorption bound ✓ SPENT (r965); the "verdict" attempt OVER-REACHED and was corrected (r966).** What is solid (`damping_reabsorption.py`): the $+8.9\%$ is in the diffusion **scale** ($r_D\propto\omega_b^{-0.31}$) and is **non-reabsorbable** by $\omega_b$ (needs $\sim29\%$ vs $\sim1\%$ allowed). What was WRONG: r965 then escalated to "several-$\sigma$ sharpest edge" and a "near-refutation," via a transfer pass (`full_transfer_verdict.py`) that **assumed CR's high-$\ell$ peaks equal $\Lambda$CDM's** and multiplied by the $+8\%$ damping to get a large high-$\ell$ deficit. **That assumption is exactly the unbuilt part** (peaks-match verified only to P3, $\ell\lesssim800$) — not a free input. Daryl caught the panic. `crossed_wire_hunt.py` further shows the $+8\%$ itself rides a subtle $r_s$ seam-cut asymmetry (LCDM's $r_s$ changes 31\% between seam-cut and to-$\infty$). **Honest status (r966): a computed, non-reabsorbable $\sim8\%$ CR-specific effect in the diffusion SCALE, whose OBSERVABLE high-$\ell$ consequence is entangled with the unbuilt high-$\ell$ acoustic transfer — genuinely OPEN, neither a demonstrated tension nor a wash.** Reverted across P15/P16/P7/ONTOLOGY/meta-docs. *The lesson (anti-panic, r959): a single fragile number does not override deep coherence + broad correspondence; hunt the crossed wire first.*
- **The deciding high-$\ell$ transfer — ATTEMPTED (r966), and RECLASSIFIED to Bucket B (frontier build, NOT a tractable oversight).** Built the semi-analytic driven-oscillator with a validation gate (`computations/peak_heights/cr_hiell_transfer.py`): it must reproduce CAMB's flat-$\Lambda$CDM peak-height envelope across the whole tail P1–P6 before any CR number is trusted. **The gate FAILED** — the toy model gets P1 (by normalization) but is $\sim$1.8× high at P2 and an order of magnitude low by P5–P6; it cannot reproduce $\Lambda$CDM's own tail, let alone an 8% CR effect on it. Two independent walls confirm this is a genuine build, not a shortcut: **(1)** CAMB cannot supply the CR spectrum — it ties the photon fluid's gravity to its presence, so CR's "radiation present as content but not sourcing the background rate" split is *unrepresentable* (killing the photon density breaks recombination itself; verified). **(2)** Even a bespoke Boltzmann solver needs CR's *perturbation sector specified* — specifically whether/how the fluctuations gravitate on the radiation-free background, which drives the peak envelope and **is unbuilt**. So the damping-tail sign is genuinely gated on building CR's perturbation dynamics, i.e. **Bucket B (frontier)**, not an overlooked tractable item. This also settles that the r965 "near-refutation" was doubly unwarranted: the baseline it implicitly assumed (the $\Lambda$CDM-matching high-$\ell$ envelope) can't even be reproduced semi-analytically, and the CR side is gated on unbuilt physics. *Honest reclassification, stated for reversal.*
- **Genuinely gated (unbuilt physics):** P1 no-horizons (structural, BH-shadow/ringdown signature, not a simple number); growth of structure / $S_8$ / $f\sigma_8$ / weak lensing (CR has no matter-perturbation growth sector — needs the matter sector, Bucket B).

## SWEEP STATUS (r964)
**All cleanly-tractable Bucket-A computations are now spent.** A1.4 (Hubble), D1 + likelihood + StarLib (abundances), A1.2 (octopole), A2.3-damping (Silk scale, reconfirmed), A6.3/C9 (matter functionals), C6/C7 (slicing B-series) — run and dispersed to the papers/map. What remains is genuinely **Bucket B** (matter sector, derivation of the inherited data, quantum completion — gated on unbuilt physics) and **data-gated verdicts** (the world judges: P1 no-horizons, the full CMB likelihood, the multi-abundance likelihood verdict). *"Nothing tractable left unspent" is now true for the first edition.* Stated for reversal.
