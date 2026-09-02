# Perturbation paper — cold verification log
Re-derivation of every load-bearing result from scratch, against corpus source forms
pulled this session (post-r501). Nothing trusted from the earlier exploratory cr_acoustic_*.py.

## Constants/relations confirmed at source (P9 = CR_flatLCDM_v2.tex)
- alpha = sqrt(3/Lambda) — throat 3-sphere size (P9 L531, L481, L638)
- merged Nariai horizon areal radius r_* = alpha/sqrt3 = 1/sqrt(Lambda) (P9 L481)
- Nariai selection: Lambda G^2 M^2/c^4 = 1/9 (P9 L479)
- fundamental-observer line element ds^2=-dtau^2+(d_chi r)^2 dchi^2+r^2 dOmega^2 (eq:SdS-fundamental)
  r=(6GM/Lambda c^2)^{1/3} sinh^{2/3}((3/2)sqrt(Lambda c^2/3)(tau+chi)); const-tau slices Euclidean (P9 text)
- Kretschmann 48G^2M^2/c^4 r^6 + 24/alpha^4 (P9 L673)
- acoustic SCALE resolved: radiation-free rate + rho_r/rho_m~2 (z~6850) at directly-measured H0
  (P9 sec687-691); c_s = ordinary baryon-loaded (NOT sqrt3); scale != spectrum (CORPUS_MAP CURRENT STATE r501)

## GEOMETRIC ANCHORS — verify_geometry.py  [ALL PASS, cold]
1. const-tau slice = flat R^3 (Riemann==0; lone term a trig-simpl artifact, =0 by expand_trig). [E] P9 eq:SdS-fundamental
2. Nariai -> equal-radii dS2xS2: double root 1/sqrt(Lambda), f''=-2Lambda, R2(S2)=2Lambda, dS2 radius^2=1/Lambda. [E]
3. Kretschmann = 48G^2M^2/c^4r^6 + 8Lambda^2/3 (=24/alpha^4); M->0 remainder regular -> perspectival singularity. [E] P9 L673
4. transmission: simple root -> log tortoise -> exp (thermal/imprint); double root -> 1/x tortoise -> power-law (scale-free/transmit). [E]

## NUMERIC ANCHORS — verify_numeric.py  [DONE, cold]
5. substrate vacuum amplitude: Lam*lP^2=2.85e-122; (H_Lam/M_P)^2=9.5e-123; A_s=2.1e-9; substrate ~113
   orders BELOW A_s. [E] for the conclusion (amplitude = inherited classical, not substrate vacuum -> no
   inflationary consistency relation). Prefactor (6e-123 / 9.5e-123 / 2.85e-122) is 2pi & reduced-vs-full
   M_P convention; conclusion robust to it.
6. low-ell cutoff: present epoch u=asinh(sqrt(OL/Om))=1.180; 1/sqrt(Lam)=3103 Mpc; r_0=5064 Mpc;
   D_C=13927 Mpc (radiation-free integrand to z_rec=1089). ell_L=sqrt(L(L+2))D_C/r_0: L=1->4.8, L=2->7.8,
   L=3->10.7, ... quasi-continuous by L~20. [R] leading-order kD projection; PARAMETER-FREE from Lambda;
   lowest PHYSICAL mode L=2 (quadrupole) -> ell~7-8, in the observed low-ell-deficit region. NOT pinned;
   O(1) ambiguity = S^3 areal-vs-curvature radius + discrete-L->continuous-ell projection.
7. sub-horizon at seam: k_hor(seam, z=6850)=0.0104/Mpc; first acoustic peak k~pi/r_s(145)=0.0217/Mpc;
   ratio 2.1x>1 -> acoustic modes SUB-HORIZON at seam (r_s here a scale reference only, not re-derived). [E]

## VERIFIED [E]/[R] MAP (the spine the draft is written from)
[E] cold: flat/discrete decoupling (P9 property); Nariai dS2xS2; Kretschmann/perspectival singularity;
          transmission dichotomy; substrate floor ->inherited-classical; sub-horizon-at-seam.
[R] cold: low-ell discreteness floor ell~a few (parameter-free from Lambda; order-level match to deficit).
[O]: coherence mechanism rigor (demo only, not re-run here); full closed-dS transfer for exact low-ell shape;
     progenitor handover spectrum (n_s,A_s) = separate paper.
SCALE: banked in P9 (sec687-691), built upon, not re-opened.

## NOTES
- The acoustic SCALE is NOT re-derived here — banked in P9; the paper builds on it, does not re-open. The
  earlier 145-vs-277 "tension" was a retired chimera (CORPUS_MAP CURRENT STATE).

---
## verify_closedS3_transfer.py — closed-S^3 hyperspherical SW transfer, low-ℓ (added 2026-06-29, r516)
**TAG: [R] first pass — DO-NOT-ASSERT** (method-accuracy + non-synchronous gaps open; cold read owed).
- **CHECK B [E]:** Φ^β_ℓ(χ) = 0 for ℓ > L=β-1 (exact closed-S^3 cutoff). VERIFIED. → degree-L feeds ℓ≤L;
  lowest physical mode L=2 feeds the QUADRUPOLE, not ℓ≈8. The flat-sky placeholder P12 eq:lowell (ℓ₂≈7.8)
  is qualitatively wrong at low ℓ and is replaced by this.
- **Quadrupole value [E]:** Φ^25_2(χ_lss=2.75) = 6.490e-2 by TWO independent methods (Gegenbauer = ODE-from-
  origin, 6 digits). The stable downward recursion is 0.4% low here.
- **Low-ℓ C_ℓ shape [R, not claimed]:** no single hyperspherical-Bessel method is trustworthy across all
  (β,ℓ) at χ_lss≈2.75 (near antipode): recursion few-% off at low ℓ; Gegenbauer precision-loses at high β;
  ODE-from-origin underflows at high ℓ. First-pass closed/flat quadrupole ratio ≈0.99 sits WITHIN the method
  error → the suppression question (k_min argument expects a deficit) is UNRESOLVED, not "no suppression".
- **Object caveat:** this is the STANDARD closed transfer, NOT the CR non-synchronous τ̃=τ+χ transfer
  (closed-S^3 source on FLAT distance projection, prop:flat) — the actual unbuilt element (P12 §scope).
- NEXT: accurate uniform hyperspherical-Bessel routine (log-space / published closed-universe benchmark),
  then the non-synchronous transfer.

---
## verify_closedS3_Cl_exact.py — EXACT closed-S^3 SW low-ℓ transfer (added 2026-06-29, r519)
**Supersedes the recursion-based C_ℓ in verify_closedS3_transfer.py.** Method-accuracy gap RESOLVED.
- **[E] METHOD:** extended-precision (mpmath) Gegenbauer is the only uniformly accurate method at
  χ_lss≈2.75. The r516 downward recursion was found **WRONG by up to 28%** at low β (exact Φ²⁵₁₀=0.06984
  vs recursion 0.05043; Φ⁵₂=0.20220 vs 0.18158). Float Gegenbauer precision-loses at high ℓ; ODE underflows.
- **[E] SUPPRESSION PRESENT (direction + rough magnitude):** ℓ(ℓ+1)C_ℓ rises monotonically ℓ=2→30,
  quadrupole at ~0.39 of the ℓ=25–30 level, β_max-converged (300/600/900 stable). The standard
  closed-universe low-ℓ suppression (k_min argument), in the region of the observed deficit.
  **Overturns the r516 "≈no suppression" look-signal — that was the recursion artifact** (the not claimed
  hold is exactly what kept it out of the corpus).
- **[R] DEPTH/SHAPE not claimed:** ℓ(ℓ+1)C_ℓ has not cleanly plateaued by ℓ=30 → depth is
  normalisation-dependent; the closed-universe scale-invariant weight (w=1/β vs curvature-corrected HZ)
  and near-antipode geometry need care before a pinned shape.
- **OPEN OBJECT:** standard closed transfer, NOT the CR non-synchronous τ̃=τ+χ transfer — a stepping
  stone confirming the mechanism, not the CR prediction. P12 cold read owed.

---
## CORRECTION (r520) to verify_closedS3_Cl_exact.py — the suppression result is WALKED BACK
A flat-limit machinery check (the discipline applied late) overturns the r519 "suppression present":
- **Test:** ℓ(ℓ+1)C_ℓ must reduce to the flat SW plateau (=const) in the near-flat limit (small χ_lss).
  The flat sum Σ_β(1/β) **j_ℓ²**(βχ) DOES (≈0.5 const, all χ). But my closed sum Σ_β(1/β)**Φ^β_ℓ**²
  RISES even at χ_lss=0.5 (a barely-closed universe that should look nearly flat) — 0.21→1.18.
  Unphysical → a bug in the C_ℓ ASSEMBLY, not near-antipode physics.
- **Diagnosis (closure sum rule):** Σ_{ℓ}(2ℓ+1)Φ^β_ℓ(χ)² should be 1 (it is, for flat j_ℓ). Mine gives
  1.30 (β=10), 1.91 (β=25), 3.94 (β=50) at χ=0.5 — β- and χ-dependent. So the flat-limit-normalised
  radial functions (correct AS FUNCTIONS — exact mpmath, the recursion-vs-exact finding STANDS) carry a
  β-dependent normalisation that is WRONG for the C_ℓ sum. Summing (1/β)Φ² mis-weights the spectrum.
- **Status:** the r519 "[E] suppression present, quadrupole ~0.39 of plateau" is **DOWNGRADED to
  not claimed** — the C_ℓ shape (incl. the suppression direction) is not trustworthy until the C_ℓ
  assembly reduces correctly to flat in the flat limit. What STANDS: (1) the method-accuracy finding —
  the downward recursion was wrong up to 28%, mpmath Gegenbauer is exact for the radial functions;
  (2) the exact cutoff ℓ≤L (degree-L feeds the quadrupole as lowest mode).
- **Open item (sharpened):** the correct closed-universe SW C_ℓ formula — the proper normalisation of the
  hyperspherical radial functions (closure → 1) and the scale-invariant primordial measure — to be
  GROUNDED at source (closed-universe CMB literature), not hacked. Then re-test against the flat limit.

---
## verify_closedS3_Cl_corrected.py — CORRECTED & flat-limit-verified (r521). Authoritative for ordinary-SW.
The C_ℓ-normalisation open item (r520) is RESOLVED. Two fixes made it sound:
- **[E] radial normalisation:** use the S^3-ORTHONORMAL Pi (M² = (β-1-ℓ)!·β·(ℓ!)²·2^{2ℓ+1}/(π Γ(β+ℓ+1)),
  from Gegenbauer orthogonality). VERIFIED: closure Σ_ℓ(2ℓ+1)Pi² is CONSTANT in χ (homogeneity) —
  the r519 flat-normalised functions failed this, the cause of the spurious "suppression".
- **[E] weight:** scale-invariant w(β)=1/(β(β²-1)) (closed HZ), SELECTED by the flat-limit test
  (ℓ(ℓ+1)C_ℓ→flat as χ→0); w=1/β, 1/(β²-1) fail.
- **RESULT [E, flat-limit-verified, β_max-converged]:** at χ_lss≈2.75, ℓ(ℓ+1)C_ℓ is FLAT to <1%
  (→ flat as β_max→∞). **NO significant low-ℓ suppression** in the ordinary-SW closed-S^3 transfer.
  Method is alive (not trivially flat): χ near antipode (3.05) develops low-ℓ structure.
- **Supersedes:** the recursion C_ℓ (r516) and the suppression reading (r519) — both artifacts, opposite signs.
- **LOOK-SIGNAL for P12 (not a verdict):** the closed-S^3 discreteness does NOT give a low-ℓ power
  DEFICIT by ordinary SW → P12's "discreteness floor in the region of the observed deficit" is not
  supported as a power deficit by this computation. CAVEATS: ordinary SW only (no ISW); STANDARD-closed,
  not the CR non-synchronous τ̃=τ+χ transfer. P12 cold read owed before any corpus action.

---
## verify_closedS3_nonsync.py — the CR NON-SYNCHRONOUS transfer (r522). The actual CR object.
Resolves the apparent r521 "no suppression" as a wrong-object artifact. The decoupling, grounded at source:
- **PROJECTION FLAT** [E, source]: prop:flat (distance slicing Euclidean, Ω_k=0) → D_M=D_C≈13927 Mpc.
  Cross-check: D_M=D_C gives ℓ_A≈301 (banked ✓); D_M=r₀≈5064 gives ℓ_A≈110 (the retracted r506 chimera).
  So the photon projection is flat: flat j_ℓ(k·D_C).
- **SOURCE DISCRETE** [E, source]: closed-S³ curvature radius r₀ → k_L=√(L(L+2))/r₀, L≥2, hard lowest mode L=2.
- **Transfer** = discrete source projected through FLAT j_ℓ (NOT the hyperspherical Φ of the standard-closed
  r521 object): C_ℓ=Σ_{L≥2} w_L j_ℓ²(k_L D_C), w_L=(L+1)/(L(L+2)) (scale-invariant discrete measure).
- **RESULT [E, flat-limit-verified, L_max-converged]** at χ=D_C/r₀≈2.75: ℓ(ℓ+1)C_ℓ ≈ 0.12/0.10/0.20/0.65/0.92/0.99
  for ℓ=2..7, ≈1.00 for ℓ≥8 → **STRONG low-ℓ deficit below ℓ≈7-8, recovered by ℓ≈8**. Flat-limit PASSES
  (χ=0.1→1.002; χ=0.5→flat). Vindicates eq:lowell (deficit below ℓ≈8) for the right reason.
- **Mechanism**: the flat projection maps k_L → ℓ≈√(L(L+2))·(D_C/r₀); the stretch factor D_C/r₀≈2.75
  (projection distance / curvature radius — the decoupling, numerical) pushes the lowest mode L=2 to ℓ≈8,
  leaving ℓ<8 empty. Standard-closed (r521) instead maps degree-L→ℓ≤L and fills ℓ=2 → flat. The whole
  difference is flat-vs-curved PROJECTION.
- **Deficit LOCATION (ℓ≈8) is geometric** (set by k_2·D_C), robust to the weight; exact shape depends on it.
- **CAVEATS (not claimed the final CR word):** (a) leading-order ordinary SW only (no ISW); (b) the discrete
  measure w_L convention to be cross-checked vs a first-principles closed-S³ primordial normalisation;
  (c) fresh-node P12 cold read owed before corpus enrichment.

---
## verify_isw_lowell.py — the MAKE-OR-BREAK ISW test (r523): the CR low-ℓ deficit SURVIVES.
Tests whether the late-ISW fills the bare-SW deficit of verify_closedS3_nonsync.py. Scope fixed at source:
P7 §floor (l.135) — in CR's uniform-expansion picture the gravitational redshift telescopes, leaving "the
endpoint potential and the small integrated term", so the cumulative term IS the standard SW + standard ISW
(CR's own differential-expansion floor is zero). No CR-specific ISW; the standard ISW sourced by the same
discrete spectrum. Assumptions (leading-order, flagged): standard-LCDM potential growth g(z)=D/a (CR=flat-LCDM
background; scalar dynamics taken standard — confirm vs P12); large-scale T(k)~1; adiabatic (1/3)SW; no Doppler.
- T_SW=(1/3)j_ℓ(kD_C); T_ISW=2∫dz(dg/dz)j_ℓ(k d(z)); C_ℓ=Σ_L w_L[T_SW+T_ISW]², coherent.
- **CONTINUUM CHECK [PASSES]:** k→0 gives flat ℓ(ℓ+1)C_ℓ for SW, and SW+ISW reproduces the known LCDM
  late-ISW rise (+56% at ℓ=2). Machinery + ISW amplitude validated against textbook LCDM.
- **RESULT [E, continuum-validated]** ℓ(ℓ+1)C_ℓ norm. to ℓ=25-30:
    SW only (CR): ℓ2=0.12 ℓ3=0.10 ℓ4=0.20 ℓ5=0.65 (bare deficit ~8× at ℓ2)
    SW+ISW (CR):  ℓ2=0.50 ℓ3=0.41 ℓ4=0.47 ℓ5=0.85 (deficit PARTIALLY filled, SURVIVES)
    LCDM (cont.): ℓ2=1.56 ℓ3=1.35 (ISW-enhanced, for contrast)
- **READING:** the late-ISW fills the bare SW deficit only partway (ℓ2: 0.12→0.50) — it CANNOT erase it,
  because the ISW is sourced by the same discrete spectrum (no modes below k_2). Net: CR sits a factor ~3
  BELOW LCDM at ℓ=2-4 — a genuine low-multipole deficit, in the direction of the observed anomaly. The one
  effect that could have killed the deficit does not. **Make-or-break ISW test PASSED.**
- **Remaining (not claimed the corpus claim):** the discrete measure w_L convention (sets exact depth, not
  survival); confirm scalar dynamics/g(z) vs P12; fresh-node P12 cold read.

---
## verify_lowell_exact_measure.py -- the exact discrete measure + the octopole verdict (r544, E1 spearhead)
**Resolves caveat (b) of verify_closedS3_nonsync.py and closes the "exact discrete measure" candidate
named in confront_lowell_data.py as a possible ell=2/ell=3 differentiator.** WRITTEN INTO P13
(\S largescale + \S scope, r545), stated for reversal; the cold read runs on the live corpus whenever
it runs -- progress is never withheld from the programme.
- **[E] DERIVATION:** the scale-invariant (HZ) weight on the closed S^3 is DERIVED from scratch
  (not fitted): per-mode power P_beta proportional to 1/(beta(beta^2-1)) (=the r521 corrected weight,
  now derived), and the flat-j_ell C_ell summation weight = degeneracy g_beta=beta^2 x P_beta =
  (L+1)/(L(L+2)) EXACTLY (numerically confirmed). So the nonsync/radiative headline weight IS the
  first-principles closed-S^3 measure. Large-L limit w_L*L -> 1 = dk/k (scale-invariant continuum).
- **[E] flat-limit test passes** (chi=D_C/r0 -> 0 gives flat ell(ell+1)C_ell) -- machinery alive.
- **[E] CR bare-SW with the derived measure** (chi=2.75): l2=0.121 l3=0.104 l4=0.199 ... recovering
  by l~7-8 -- reproduces the r522 nonsync deficit.
- **[E] THE OCTOPOLE VERDICT -- the measure does NOT differentiate ell=2 from ell=3.** D2/D3=1.16 and
  STABLE across the weight family (q in [-0.4,+0.4]: D2/D3 = 1.07..1.21; pure-per-mode wrong weight:
  1.23). The single floor k_2 starves ell=2 and ell=3 ALIKE; if anything the exact measure makes the
  OCTOPOLE slightly MORE suppressed (D2/D3>1) -- the wrong direction to relieve the observed tension
  (observed: ell=2 low, ell=3 ~LCDM, i.e. D2<D3). So the exact measure FIRMS the octopole
  over-prediction rather than relieving it.
- **STATUS:** with Doppler already non-differentiating (verify_doppler_lowell.py), TWO of the three
  confront_lowell_data.py differentiator candidates are closed. The smooth ell<~7 deficit is FIRM and
  the octopole is the falsification edge. RESIDUAL (not claimed): candidate (iii), the full Boltzmann
  solve / exact non-synchronous transfer, ~10-20% on the transfer, not expected to lift the factor ~4-5.
- **OBJECT/CAVEATS:** flat-j_ell projection of the discrete closed-S^3 source (the CR object, prop:flat);
  bare ordinary SW for the measure test (the ISW/radiative depth is in verify_lowell_full_radiative.py
  and does not change the D2/D3 ratio, which is set by the source-projection). P13 updated live (r545).

---
## verify_lowell_likelihood.py -- the low-ell likelihood-level CR-vs-LCDM model selection (r546, E2)
**Closes the low-ell half of P13 sec:scope item 3 ("the largest blind spot"). WRITTEN INTO P13 live
(sec:largescale pointer + sec:scope item rewritten), stated for reversal.** Reported straight -- this
does NOT favour CR.
- **[E] INSTRUMENT:** exact low-ell cosmic-variance likelihood, (2ell+1) Chat_ell/C_ell ~ chi^2_{2ell+1},
  so -2lnL = sum (2ell+1)[Chat/C + ln C]; the model comparison Delta(-2lnL) works in CR/LCDM ratio
  units (baseline cancels): Delta_ell = (2ell+1)[r_obs(1/r_C - 1) + ln r_C].  Inputs grounded: r_C the
  radiative CR/LCDM ratio (verify_lowell_full_radiative.py); r_obs the confront_lowell_data.py literature
  set (central + estimator range).
- **[E] PER-ELL (central):** l2 = -4.0 (quadrupole match REWARDS CR); l3 = +12.3, l4 = +5.5 (octopole
  + l=4 PENALISE CR); l>=5 ~0.  Net 2<=l<=30 = +14.0 -> LCDM preferred at central data.
  **The octopole outweighs the quadrupole** under the proper likelihood -- the eyeball "lands the
  quadrupole" overstates CR's case.
- **[E] ESTIMATOR SENSITIVITY (the verdict's true limiter):** net Delta(-2lnL) = -0.2 (low-octopole
  WMAP value) / +14 (central) / +28 (high Efstathiou value).  THE SIGN FLIPS -> the low-ell verdict is
  estimator-limited, not a clean preference.
- **[E] MONTE-CARLO (10^4 skies):** if LCDM true <Delta>=+37 (std 21); if CR true <Delta>=-14 (std 5);
  model separation ~3.4 sigma -> the low-ell sector has only marginal IN-PRINCIPLE discriminating power,
  and the octopole measurement uncertainty currently swamps it.  Observed Delta=+14 sits ~12th pctile of
  LCDM-true (consistent w/ LCDM ~1sigma), far out the CR-true tail at central octopole.
- **VERDICT:** the low multipoles are a GENUINE BUT BLUNT test; they do not presently favour CR and at
  central estimates lean LCDM through the octopole; no clean verdict from this sector alone.  Decisiveness
  must come from outside it: the radiation-free rate (P7) and the FULL-spectrum likelihood (peak heights /
  oscillating medium, downstream in the matter sector -- E3, gated). Coherence shown is not correspondence
  earned -- held at exactly that weight.

---
## verify_alpha_mass.py -- C1: is alpha the intrinsic gravitational mass? (r547)
**Resolves the open question of P3 sec:mass (l.529) and P4 (abstract/intro/outlook). WRITTEN INTO P3
(sec:mass + sec:open) and P4 (4 mentions reconciled), stated for reversal.** Answer: NO -- the
gravitational mass is the perspectival M; alpha is the invariant curvature radius, a length.
- **[E] Misner-Sharp** m_MS(r) = (r/2)(1-f) = M + r^3/(2 alpha^2): returns parameter M (alpha only the
  +r^3/2a^2 dS background).  **[E] Komar** m_K(r) = (1/2)r^2 f'(r) = M - r^3/alpha^2: returns M (alpha
  only the -r^3/a^2 dS term).  Both -> M at r->0.
- **[E] pure dS (M=0):** zero mass parameter; alpha = dS curvature RADIUS (Kretschmann 24/alpha^4) -- a
  length, NOT a mass.  Asymptotics: SdS is asymptotically dS not flat, so ADM/Bondi inapplicable; the
  asymptotically-dS mass returns M.
- **[E] Nariai lock:** double root of r^3 - alpha^2 r + 2M alpha^2 = 0 gives M_Nariai = sqrt3 alpha/9 =
  alpha/(3 sqrt3), Lambda M^2 = 1/9.  This is the LONE member whose mass is an alpha-built invariant;
  for a general slicing 2M = alpha(s - s^3), s = r0/alpha in [0,1], M free over [0, alpha/(3 sqrt3)].
- **[reading] SYNTHESIS / reconciliation with P4:** P4 proved alpha is the unique chart-invariant, so any
  FULLY invariant mass must be alpha-built.  C1 completes it: the standard definitions return the
  non-invariant M, so the standard gravitational mass is the perspectival/P-odd projection (computed in
  the Schwarzschild vantage), there is no general alpha-built intrinsic mass (only the Nariai lock), and
  alpha is the invariant length.  CONFIRMS the perspectival reading (M = projection) rather than
  weakening it -- same shape of honest result as E2.
- **Incidental fix:** the pre-existing malformed JanzenAlgebroid bibitem in P4 (unmatched $, dropped
  $\mathfrak{so}$) repaired; P4 now compiles (20 pp, 0 errors). P3 verified in graphicx-draft (28 pp,
  0 errors; figures are an environment artifact, not a corpus issue).

---
## verify_lowell_boltzmann.py — A1.2 COMPLETED (r962): the exact low-ℓ shape from a genuine CAMB transfer × discrete source
The analysis started many nodes ago (r516–r522, the SW-analytic estimates) is now finished with a
genuine Boltzmann transfer, the ontology finally clean enough to hold it. Method: CR's temperature
transfer IS flat-ΛCDM's (flat projection prop:flat + zero differential floor P7 §floor ⇒ SW+ISW+Doppler
common), so CAMB's exact Δ_ℓ(k) (`get_cmb_transfer_data`) IS CR's transfer; only the SOURCE differs.
  C_ℓ^CR = Σ_{L≥2} w_L (k_L/k_piv)^{ns-1} |Δ_ℓ(k_L)|² ,  k_L=√(L(L+2))/r₀ ,  w_L=(L+1)/(L(L+2))=dln k_L/dL
  C_ℓ^LCDM = ∫ dln k (…) |Δ_ℓ(k)|²  (continuum).  So CR is the L=2-floored Riemann sum of the same integral.
- **[E] GATE PASSES:** my continuum integration reproduces CAMB's own C_ℓ to 4 sig figs (ℓ=2: 972.32 vs
  972.49; ℓ=5,10,20 likewise). Transfer integration validated.
- **[E] ROBUST:** depths stable under ±2% r₀ (ℓ=2: 0.46→0.49, ℓ=3: 0.43→0.39, smooth — no aliasing on
  the Bessel oscillations, which the discrete modes sample at ~5.6 pts/period); the "messy" delicacy is
  controlled.
- **RESULT [E]:** CR/LCDM depth ℓ=2:**0.47**, ℓ=3:**0.41**, ℓ=4:0.36, ℓ=5:0.68, →1 by ℓ≈7. ℓ=2,3
  suppressed TOGETHER (ratio 0.87). **Supersedes the SW-analytic 0.22/0.20** (verify_lowell_full_radiative).
- **WHY the old estimate was too deep:** it assumed CR loses the late-ISW boost ("no low-k modes"). Wrong
  — the late ISW at ℓ=2 is sourced at k~few×10⁻³ (late times/small distances), ABOVE the floor k_2=5.6e-4,
  so CR RETAINS it. The exact transfer carries the ISW; the SW-analytic approximation dropped it.
- **CONSEQUENCE (not claimed; revises the corpus, held for Daryl):** CR predicts a SMOOTH modest low-ℓ
  deficit (~0.4–0.5 at ℓ=2–3), not a sharp quadrupole dip. The earlier "striking quadrupole match" (0.22
  vs observed ~0.2) does NOT survive — CR sits ABOVE the observed quadrupole; and the octopole
  over-suppression SOFTENS (0.41 vs old 0.20). Net: a mild, cosmic-variance-consistent deficit, neither a
  sharp correspondence success nor a sharp falsification risk. P15/P16 low-ℓ numbers + the quadrupole-match
  claim need revising if Daryl accepts this.
