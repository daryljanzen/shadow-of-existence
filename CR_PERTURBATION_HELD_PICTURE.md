# CR cosmology & perturbations — the held picture (for the heights transfer)

*Assembled r822 (2026-07-05) from a careful read of the scattered source (P13 §properframe, §flatlcdm, §tensions, §subhorizon, §coherence–§transmission; the framework paper). "You need to read the papers… it's good to hold all the relevant stuff" (Daryl). This is the prerequisite the four failed transfer attempts (r818–r821) skipped: CR's actual perturbation structure, held in one place, with my error diagnosed and the correct transfer set up.*

---

## 1. The background rate — set by the geometry, and WHY (§properframe, §flatlcdm)
- The scale factor is **derived**, not posited: r(τ̃)=(2^{1/3}/√Λ)·sinh^{2/3}(½√(3Λ)c·τ̃), from the SdS radial geodesic congruence at E=1 (the rest frame fixed by the field). It is *exactly* the flat-ΛCDM scale factor.
- Friedmann form: **H²=(Λc²/3)coth²(½√(3Λ)c τ̃)=⅓(8πGρ+Λc²)** [eq:rate]. H→matter-like early (H=2/3τ̃), de Sitter late (H→√(Λc²/3)).
- **Read LEFTWARD — the crux.** The rate is *set* geometrically (M+Λ, the sinh^{2/3} law); ρ is *inherited content read off that clock*, not a term that sources the rate. Ω_m/Ω_Λ=csch²(…) is a **clock** (records the epoch τ̃₀), not an independent density.
- **Radiation, like matter, is inherited content read off the clock — NOT a term that sources the rate. There is no radiation-dominated era.** The "a radiation fluid must gravitate and so alter the rate" objection is named a **category error** against a construction that reads eq:rate leftward: the rate is set, and the fluid's energy is among the contents the set rate carries.
- Load-bearing falsifiable claim: **radiation carries no term in the expansion rate.**

## 2. The acoustic scale — one parameter, H₀-decoupled (§tensions)
- r_s=∫_{z_rec}^{z_onset}(c_s/H)dz on the geometric H, depending on ONE early parameter z_onset≈z_onset≈6.8×10³ (T_onset~1.6 eV). Standard radiation-governed r_s is the forbidden z_onset→∞ limit.
- c_s the ordinary **baryon-loaded** value — the seam matter is pressureless (w=0); the throat ratio √3 does NOT set it.
- θ*=r_s/D_M **fixed by Ω_m alone**: the geometric rate carries H₀ out of both r_s and D_M, so the acoustic scale meets the data at the *directly measured* H₀ — no second H₀ (Hubble tension dissolved), the one z_onset the same at every H₀.

## 3. The seam initial conditions — inherited, and SUB-HORIZON (§tensions, prop:subhorizon)
- ρ_r/ρ_m≈2 at the branch point is the **η-analogue**: measured content (the hot handover of the progenitor collapse — this universe formed at a black-hole horizon in a previous one), not geometry-set (the seam's Gibbons–Hawking T~10⁻³⁰ K, 30 orders below onset, confirms no geometric source). Light elements likewise inherited (Y_p≈0.245 generic; no Li problem; deuterium the sharp constraint, gated on the matter-sector handover thermodynamics). A_s, n_s inherited via faithful transmission.
- **prop:subhorizon (decisive for the transfer):** at z_onset≈6850, k_hor=H₀E(z_onset)/[(1+z_onset)c]≈0.010/Mpc, with **E(z)=√(Ω_m(1+z)³+Ω_Λ)** (the geometric rate). The acoustic peaks are at k~π/r_s≈0.022/Mpc **and above** — so the acoustic modes are **inside the horizon at the branch point by ≳2×**.
- **Consequence:** the acoustic modes are NOT frozen super-horizon data awaiting re-entry (the inflationary story). They are *already inside the horizon when the cosmological side begins*. Whatever fixes their amplitudes/phases is the **seam handover itself**, not a super-horizon freeze-out. The substrate's role is to **transmit and gate**, not generate.

## 4. The perturbation sector — established (§coherence–§transmission; r817 read)
Coherence from the null boundary (the comb); classical amplitude (substrate vacuum beaten 10¹¹³); throat isotropization (**guard: throat index ≠ CMB multipole**); the parameter-free low-ℓ floor (ℓ₂≈7.8, flat/discrete decoupling); faithful transmission (degenerate seam, the inherited tilt). Receipts in `computations/perturbation_verify/`.

## 5. THE CORRECT TRANSFER SETUP — what the read fixes
The CR heights transfer is **not** the standard one, and my four attempts (r818–r821) fed the standard one. The correct setup:
- **Background:** the geometric rate H(z)=H₀√(Ω_m(1+z)³+Ω_Λ). Matter-like throughout; **no radiation-dominated epoch**.
- **Initial conditions:** at the branch point z_onset≈6850, the acoustic modes **already sub-horizon**, carrying the coherent seam phase (one characteristic datum per mode) and the inherited seam amplitude (ρ_r/ρ_m≈2, A_s, n_s). NOT super-horizon adiabatic ICs.
- **Evolution:** the baryon-loaded (w=0, c_s ordinary) photon–baryon fluid oscillates from z_onset to z_rec≈1090 on the matter-like background. The potential Ψ evolves **matter-like** (roughly constant — a matter-dominated background does not decay it), so the **radiation-driving is small**, not the standard boost.
- **Heights = seam amplitude × baryon loading (odd/even) × (small) driving × Silk damping**, projected flat (D_M=D_C).
- **The sharp CR prediction & refutation edge:** the geometric rate → little driving → the peaks sit near the *undriven* pattern (higher P1/P2 asymmetry than the driven ΛCDM), UNLESS the seam-handover ICs shift it. Whether the undriven-plus-seam pattern lands the observed heights is the test. This is a *specific, computable* prediction, not a free knob.

## 6. Why the four attempts failed (diagnosed)
All four fed **super-horizon adiabatic ICs driven through radiation domination** — the standard story. CR has neither: the modes start sub-horizon at the branch point, and the background is geometry-set (matter-like). The causal arrow was backwards (rate *sourced* by radiation, vs CR's rate *set* and radiation carried). The r817 skim-not-read error, one level down — now corrected at source.

## 7. The build, correctly scoped
A transfer from the **seam handover** (z_onset≈6850, sub-horizon coherent ICs, inherited amplitude) on the **geometric background** (matter-like, so Ψ≈const, little driving) to recombination — baryon loading, Silk damping, flat projection. Validate the *machinery* on ΛCDM (standard ICs+background) as a code check, then run the CR setup (seam ICs + geometric background) for the prediction. This is now a well-posed, bounded computation with the physics held correctly — the honest next build.
