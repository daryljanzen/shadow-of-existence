> **⌖ RETIRED r1546.** This was the uniform-expansion (isotropy) reductio (r339). **Landed:** P4 carries the argument — the redshift-isotropy floor forcing the cosmic foliation, with Green–Wald weighed against it at source.
> Kept as record; **do not work from it.**


# The uniform-expansion (isotropy) argument — reductio structure and step verification

*Working note for Step 2 of `LENS_INSERTION_PLAN.md`: the central-limit / uniform-expansion calculation
in `resources/CR_firstdraft.tex` §"The isotropy and cosmic time problems" (lines 61–144), with the
growth-factor normalization settled in `resources/CR_RNAAS_growth-normalization.tex` (J(Ω_m)=1 at
Ω_m\*=0.315162, verified independently). Structure locked with Daryl (c19, 2026-06-17). Stated for reversal.*

> **CANONICAL HOME (updated r339):** the finished proof lives in the corpus as the standalone **P8 (`corpus/modern_parallax.tex`)**,
> *"The modern parallax: the redshift-isotropy floor and the empirical forcing of cosmic time and uniform expansion"*;
> P9 (`canonical_time.tex`) §necessity forward-references it; refs (Buchert2000, Wiltshire2007) source-verified, now carried in the new paper. This note is the
> working distillation and provenance (the verification ledger + the wake-grounded convergence after two
> compacted-frame swings), not the canonical statement. Edit the appendix, not this note, for the corpus text.

---

## 1. The proof structure — a reductio (LOCKED)

The argument is a proof by contradiction. Its target is the GR-local ("backreaction") expectation; its
payload is that the standard model's uniform-expansion axiom is **empirically verified, not merely assumed.**

- **Hypothesis under test, P.** Local matter-density inhomogeneity perturbs the local rate of cosmic
  expansion — the expansion along a line of sight is governed by the density encountered along it
  (Friedmann applied region-by-region; ρ ∝ a⁻³ read as differential expansion). This is the GR-local
  expectation the backreaction literature takes seriously, and it is the **negation** of the standard
  model's uniform-expansion axiom.
- **Consequence under P, C.** A CMB photon's accumulated cosmological redshift then varies across lines of
  sight in proportion to the line-of-sight density contrast. Carried conservatively (factor of 3 in;
  no-correlation → maximal N; growth-suppressed σ₈,eff), the predicted monopole-redshift / temperature
  anisotropy is δT/T = δz/z ≈ σ₈,eff/(3√N) ≈ **2.8×10⁻³**. This is the *primary* effect of inhomogeneous
  expansion *of* space — distinct from and on top of the *secondary* effects (SW, ISW, lensing, RS, SZ)
  the standard treatment already includes.
- **Observation, O.** The measured monopole-redshift anisotropy, after the dipole, Galactic contamination,
  and all secondary effects are removed, is ≲ **3×10⁻⁶**.
- **Contradiction.** C exceeds O by ~10³. The predicted primary effect is absent.
- **Conclusion, ¬P.** Local density inhomogeneity does *not* perturb the expansion rate. Outside bound
  structures, expansion is uniform — not on average, but to the precision of the null result, ~10⁻⁶.
- **Corollary (the payload).** Uniform expansion ⟺ a globally well-defined cosmic time and rest frame (the
  RW line-element's foundational assumption). So the quantity the standard model *assumed* — cosmic time —
  is the quantity its own data *verify*, to ~10⁻⁶: assumption elevated to empirical necessity. The dipole
  surviving the null, 369.82 km/s toward Crater, is our measured velocity through that verified frame.

**Why this defeats "FLRW expansion is uniform by construction."** Exactly so — and the construction (the
uniform-expansion axiom) is the thing under test. The reductio does not accuse the standard model of an
arithmetic error; it shows the axiom does load-bearing empirical work it was never credited for: it
overrides the GR-local prediction C, and the data confirm the axiom over the GR-local expectation. The
objection *concedes* the point — the construction is what the null result verifies.

---

## 2. The load-bearing joint — where the justification must be airtight

The reductio is valid as a reductio for any C that genuinely follows from P. Its *force* turns entirely on
**C genuinely following from P** — that the GR-local expectation really does predict ~10⁻²–10⁻³, and that
this primary effect is genuinely **distinct from, and additional to, the secondary effects (esp. the ISW)
the standard perturbation treatment already computes at ~10⁻⁵.** This is the joint the backreaction crowd
will contest: they will say full GR perturbation theory on the imposed FLRW background already yields the
observed ~10⁻⁵ and there is no separate ~10⁻² effect. Defeating that requires showing the ~10⁻² is what
naive GR-local reasoning predicts *without* the uniform-expansion axiom, and that the standard ~10⁻⁵ is a
*consequence of imposing* the axiom, not an axiom-independent GR result. Making §3's chain airtight,
step by step, is what closes this joint.

---

## 3. Step verification of the formal calculation (C-from-P)  [in progress]

- **Step 1 [LOCKED, c19].** ρ_m ∝ a⁻³ (continuity, p=0) ⇒ d ρ/ρ = −3 da/a; with da/a ~ dz/z ⇒
  |δz/z| = (1/3)|δρ/ρ|. Factor of 3 **in** — rigorous matter coefficient *and* conservative (dropping it
  overstates the prediction 3×). Effect on the final: σ_path = σ₈,eff/(3√N), taking 8.3×10⁻³ → 2.8×10⁻³,
  still ~920× the observed 3×10⁻⁶.
- **Step 2 [VERIFIED, c19].** With A ≡ a_ob/a_em = 1+z the accumulated expansion factor, the CMB
  temperature is T_obs = T_lss/A ∝ 1/(1+z). Perturbing a line of sight: δT/T = −δA/A = −δz/(1+z) = −δa/a.
  So **|δT/T| = |δa/a| exactly** — the observable temperature anisotropy *is* the fractional
  accumulated-expansion perturbation. The draft's δz/z is the high-z form (z/(1+z)=0.99908 at z_lss=1089,
  a 0.09% nicety, not a real approximation); writing δT/T = δa/a exactly preempts any nitpick. Sign:
  overdense → less expansion (step 1) → less redshift → hotter spot (matches draft line 79). Combining
  steps 1+2, per bin: |δT/T| = (1/3)|δρ/ρ|, ready for the central-limit sum (step 4). Bonus for the joint
  (§2): this *primary* effect (path-accumulated expansion) is physically distinct in mechanism from the
  *secondary* SW (gravitational potential at emission), reinforcing C ≠ secondary effects.
- **Step 3 [VERIFIED, c19].** Reproduced numerically (Ω_m=0.315, σ₈(0)=0.8, z_lss=1089). Growth factor
  D(z) properly normalized: J(0.315)=1.0004, D(0)=1; D(1)=0.607 → σ₈(1)=0.49 (draft footnote ≈0.5 ✓);
  D(1089)=0.0012 → σ₈≈0 ✓. **σ₈,eff[0,1089] = 0.2849 ≈ 0.285 ✓**; low-z-excluded **σ₈,eff[1,1089] = 0.1703
  ≈ 0.17 ✓** (result not dominated by low-z). Comoving distance ∫dz/E = 3.132 → d_lss,0 = 9.39 h⁻¹Gpc
  (draft 9.42 ✓) → N = 1174 (draft ~1200 ✓). Conservative: the growth factor *suppresses* σ₈ at high z, so
  σ₈,eff=0.285 sits well below the naive σ₈(0)=0.8-everywhere value (which would give a 2.8× larger
  prediction) — the realistic, correctly H⁻¹-weighted number, not an inflation. Running final with the
  factor of 3: σ_path = 0.285/(3√1174) = 2.77×10⁻³, ~924× the observed 3×10⁻⁶.
- **Step 4 [VERIFIED, c19].** σ_path = σ₈,eff/(3√N) is the std of the path-MEAN of N i.i.d. bin contrasts
  (Monte Carlo confirms: N=1174 → std(mean)=0.00826 vs σ/√N=0.00831). The 1/√N (not √N) is correct: the
  observable is the *fractional* redshift contrast δz/z = the path-averaged expansion contrast, so
  independent bin fluctuations average DOWN. N = d_lss,0/8Mpc = 9390/8 = 1174 (draft ~1200 ✓).
  **Conservative (rigorous):** positive clustering correlations only ADD to Var(path-mean), so the
  no-correlation N=1174 value is a strict FLOOR; correlations push it UP — L_corr=138 h⁻¹Mpc (basins of
  attraction, line 103) → N_eff≈68 → σ_path≈1.2×10⁻², ~4× the floor. **Final (floor): σ_path = 2.77×10⁻³,
  ~924× the observed 3×10⁻⁶**; the realistic value (with correlations) is larger, up to ~10⁻².

## 4. Status — formal calculation verified; the joint correctly located (c19, 2026-06-17)

Steps 1–4 all check out, and every step biases the prediction *downward*: factor of 3 in (step 1);
growth-suppressed, correctly H⁻¹-weighted σ₈,eff (step 3); no-correlation → maximal N (step 4). The floor
δT/T ≈ 2.8×10⁻³ exceeds the observed ≲3×10⁻⁶ by ~3 orders of magnitude. The arithmetic is closed and a
genuine underestimate.

**The premise-defense crux, regrounded (correcting an earlier overswing).** A first pass mistakenly
identified C with the standard Sachs–Wolfe/ISW effect and concluded the calculation strawmanned
backreaction. That was a category error and is **withdrawn**. The clean distinction:

- **(a) Uniform expansion + clustering** (standard ΛCDM). One a(t); density lumps are static potential
  wells. A photon's gravitational redshift entering each well is undone exiting it — the path contributions
  **telescope**, leaving only the endpoint potential (SW at the LSS, ~10⁻⁵) + small ISW (well evolution).
  No σ₈/√N accumulation. This (a)-effect — Φ-sourced, Poisson-suppressed, ~10⁻⁵ — *is* what's observed, and
  it is **not** what the draft computes.
- **(b) Differential expansion** (backreaction/timescape regime). No single a(t); overdense regions
  expanded less. Accumulated redshift is a *bulk, additive* function of the path's density profile — does
  **not** telescope — and central-limits to exactly the draft's σ₈/(3√N) ≈ 10⁻²·⁵.

The sky shows ~10⁻⁵, not 10⁻²·⁵ ⇒ regime (b) is excluded ⇒ uniform expansion (a) holds to ~10⁻⁶. The draft's
calculation is the **correct (b)-prediction**; its **absence** is the evidence, and the reductio is **valid**.
It is not the SW effect (different mechanism, different place, and *present* at 10⁻⁵); it is the
differential-expansion anisotropy that is *absent*. The 1967 SW "10⁻² failed by 10³" was an *amplitude*
(input-lumpiness) error and is unrelated to this calc, which uses the measured σ₈ — that comparison is
withdrawn too.

**Remaining genuine joint** — about the *model under test*, not the logic: the (b)-magnitude assumes the
per-region expansion-rate contrast tracks the density contrast (separate-universe, step 1) and that regions
contribute independently (central-limit). A smoother/milder differential-expansion model predicts less — but
the margin is ~10³, so any δ-level, region-local differential expansion is excluded robustly.

**Timescape (Wiltshire) and the monopole.** The reductio does *not* strawman backreaction; it converts the
**CMB redshift monopole isotropy** (z_LSS ≈ 1089 in every direction, probing the full expansion history along
each line of sight) into a constraint on present-day differential expansion. The 2023 *Conversation* review
(inhomogeneous-cosmology program) leans on CMB uniformity as evidence the universe *was* smooth, argues
against present-day uniformity, and catalogues the dipole / power asymmetry / Hubble tension / matter dipole —
but never raises the monopole-redshift isotropy. So the constraint appears **unconfronted**. Caveat held:
Wiltshire's technical CMB fits are to the acoustic *scale* (peak positions), a different quantity from the
monopole isotropy. Daryl's separate structural objection — that timescape's variable-age "now" silently
re-imports the absolute cosmic present it claims to dispense with — is a coherence problem noted but
**not adjudicated here**.
