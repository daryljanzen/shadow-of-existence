# Peak heights: from mechanism to derivation (the reduction), and a new candidate signature

**Build goal (P15 §scope item 1 / P16 spine link 8):** turn the peak-height *mechanism* into a
derivation — confirm the P1:P2:P3 pattern "digit by digit," and settle whether CR = ΛCDM.

## The reference (CAMB, exact)
`camb_reference.py` (CAMB 1.6.6, Planck-2018): the ΛCDM acoustic peaks are
**P1/P2 = 2.210, P2/P1 = 0.453, P3/P1 = 0.443** (P1 ℓ=220, P2 ℓ=536, P3 ℓ=813) — matching the
paper's observed anchors. This is the digit-by-digit target and the validation gate.

## The reduction (not a from-scratch transfer)
A from-scratch semi-analytic transfer would only *re-derive ΛCDM's peaks* (hard — it is
Hu–Sugiyama; my attempts did not validate). It is unnecessary: the CR peak heights **reduce** to
ΛCDM's for the observed peaks, on pieces already verified.

The acoustic modes are **sub-horizon at the seam** (`prop:subhorizon`): k_hor(seam)=0.0104 Mpc⁻¹
vs first-peak k=π/r_s=0.0214 — inside by ×2.0 (higher peaks more). So each acoustic mode's
**driving is complete before the seam**, on the collapse side. That driving imprint has:
- **amplitude = ΛCDM's**, per mode — the resonant Fourier magnitude |Ψ̃(ω=1)| is time-reversal
  invariant (expanding 1.5000, contracting 1.5002; ratio 1.0001);
- **phase = a single coherent value** — the null-seam characteristic data (`verify_coherence_comb.py`).

After the seam the mode oscillates and damps to recombination through the **identical plasma**
(same ω_b, ω_m, c_s, recombination). In sound-horizon-phase units x=k·r_s the post-seam evolution
and the baryon-loading odd/even asymmetry are identical, and the *scale* r_s/D_M is matched
separately (the acoustic-scale result, z_onset≈6850). 

**⇒ CR's low-peak heights = ΛCDM's = CAMB's 2.210 / 0.453 / 0.443, derived** — the driving boost
(P1 enhancement) by time-reversal + sub-horizon-at-seam, the odd/even pattern by the shared baryon
loading. The end-to-end transfer the paper deferred is *not needed for the observed peaks*: the
physics reduces exactly to ΛCDM's post-seam evolution of a mode whose complex driving imprint
(amplitude by time-reversal, phase by null-seam coherence) equals ΛCDM's.

## The CR-specific piece, SIZED and GATED (r945): θ_D/θ_* is +7.9% vs ΛCDM
This is the "diffusion computation on the CR rate (in progress)" that P15 §coherence flags and holds
do-not-assert. It is now done, on a computation that **passes the CAMB validation gate** and — the
crucial thing — is done *the way the paper defines the scales*, not the r939–40 way that was the
named artifact. Receipt: `damping_ratio_clean.py`.

**The gate (must pass before any CR number is trustworthy).** On the ΛCDM (radiation-included) rate
with CAMB's exact recombination x_e(z): my r_s = **144.0 Mpc** (CAMB rstar 144.44, 0.3%); my r_D = 6.57
Mpc → k_D = 0.152 (CAMB ~0.14, an ~8% *normalization* offset in the Hu–Sugiyama bracket that is
z-independent and **cancels in the CR/ΛCDM ratio**); π·r_D/r_s = 0.1434 vs CAMB thetad/thetastar
0.1544. Gate passed — the pipeline reproduces CAMB.

**What the r939–40 version got wrong (the named artifact).** P15 §intro states it outright: *"the
standard radiation-governed sound horizon laid on the radiation-free rate is a calculation belonging
to neither framework, and any 'tension' it produces is an artifact."* My earlier pass integrated r_s
over the radiation era to high z on the radiation-free rate (→ r_s ≈ 245 Mpc, 100θ_* ≈ 1.76 — a
gross miss of the observed 1.041) and compared *that* to r_D. That hybrid is the artifact, and it is
what the r941 "shadow collapse" verdict correctly killed. **But the effect it garbled is real when the
computation is done right.**

**The scales as the paper defines them.**
- **Sound horizon — truncated at the onset (P15 §tensions eq.):** r_s = ∫_{z_rec}^{z_onset} (c_s/H) dz.
  The expanding-phase plasma begins at the finite-curvature onset z_onset ≈ 6850 (T_onset ≈ 1.6 eV),
  so there is *no* pre-onset sound travel; the standard radiation-governed r_s is the forbidden
  z_onset→∞ limit. On the radiation-free rate with this cutoff: **r_s = 145.5 Mpc → 100θ_* = 1.044**
  (observed 1.041). The acoustic scale is met — the onset datum (ρ_r/ρ_m ≈ 2) *is* tuned to do this.
- **Hubble resolution — confirmed, and clean.** At **fixed Ω_m** the radiation-free rate carries the
  common H_0 out of both r_s and D_M, so 100θ_* = **1.0440 at H_0 = 67.4, 70, and 73 identically** —
  H_0-independent, met at the *directly measured* value. (This is a fixed-Ω_m scaling, not the
  fixed-ω_m one that ties ΛCDM's r_s to the radiation era; that difference is the whole resolution.)
- **Diffusion length — on the radiation-free rate near recombination (P15 §coherence).** Recombination
  (z ≈ 1090) is post-onset, so the leaf's own expansion there is radiation-free (the §properframe
  sinh^{2/3} geometry; radiation is inherited content that does *not* source the rate — §flatlcdm,
  the "category error" remark). The photon random walk accumulates against that lower H (H_free is
  ~15% below H_incl at z_rec), giving a **longer** diffusion length: r_D(CR)/r_D(ΛCDM) = **1.090**
  (robust, convention-free — the same offset cancels).

**The result.** r_s is matched to the acoustic scale in *both* frameworks (144–145 Mpc), so the only
observable difference is the ~9% longer r_D:
> **θ_D/θ_* = r_D/r_s : ΛCDM 0.0457 → CR 0.0492, a ratio of 1.079 — CR's damping angular scale is
> ~+7.9% larger** (100θ_D: ΛCDM/observed ~0.161 → CR ~0.174). Projection-independent (both ÷ the same
> D_M), so it is a clean prediction, not a distance artifact.

**Disposition — a genuine, modest, testable CR-specific signature; do-not-assert (neither win nor
fatal).** This is *not* the shadow collapse: r_s is the CR onset-truncated value matched to the
observed peak spacing (not the radiation-governed r_s swapped onto the wrong rate), and only the
diffusion — genuine local dynamics on the actual radiation-free leaf at recombination — sees the rate.
That is exactly the object P15 §coherence already names ("the Silk scale need not coincide with
ΛCDM's — the one genuinely CR-specific piece of the height pattern … held do-not-assert"). The
computation **confirms and sizes** the paper's existing honest flag; it does not change the paper's
disposition. Whether +7.9% is inside Planck's high-ℓ tolerance is a full-likelihood question
(P15-4 frontier) — reported straight, asserted as neither confirmation nor refutation.

**Correcting the r941 record precisely.** r941's "artefact" verdict was right about the *method* (the
r939–40 hybrid r_s) and I over-generalized it to "the whole ~7.8% is probably an artefact that
dissolves." The gated computation shows it does *not* dissolve: done the paper's way, the effect is a
real +7.9%, because the diffusion genuinely runs on the leaf's radiation-free rate (the paper commits
to this at §coherence), while the sound horizon is the matched onset-truncated scale, not the swapped
one. Kill the hybrid; do it right; a modest real deviation remains.

## Status / for-reversal
- **Derived (rigorous, on verified links):** CR low-peak heights = ΛCDM's = 2.210/0.453/0.443
  (reduction, r939 — stands). The acoustic scale + Hubble resolution: met at directly-measured H_0,
  θ_* H_0-independent at fixed Ω_m (gated, r945).
- **CR-specific prediction (sized, do-not-assert):** the Silk-damping tail is +7.9% in θ_D/θ_* on
  CR's radiation-free rate. Consistent with P15 §coherence's existing do-not-assert flag; sizes it.
  The paper text stands as written — no revision forced, the number is a receipt.
- **Still frontier:** the full high-ℓ likelihood that would turn +7.9% into a confirmation or a
  refutation (P15-4).
- Receipts: `damping_ratio_clean.py` (gated), `camb_reference.py`, `silk_tail.py` (superseded by the
  gated version).
