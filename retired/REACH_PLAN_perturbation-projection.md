# Reach Plan — the scalar-perturbation projection (low-ℓ transfer)
> **⌖ RETIRED r1509 — verified landed before moving.** This planned the low-ℓ scalar-perturbation transfer. **Landed:** P15 carries the shape on a genuine Boltzmann transfer (×6); Lane 1 A1.2 struck DONE r1006. Pre-renumber — it calls the perturbation reach "P12".
> Kept as record; **do not plan from it.** Its numbering and era predate the current corpus.



*Working/scratch document. NONDESTRUCTIVE: no canonical paper, changelog, or capstone is
touched by this file. Companion to `PERTURBATION_PAPER_DRAFT.md` (the draft) and
`REACH_low-ell-transfer.md` (the running log). Written 2026-06-29 (gate session with Daryl),
after a full reground in `THE_CODA.md` + three field-guide faces and a full read of P9's
load-bearing development. Stated for reversal.*

> **STANDING CORPUS-ARCHITECTURE FLAG (carry while executing this reach — r511/r512).** P9's
> formal SdS-cosmology development is being recast into a forward-pointer + a *conceptual*
> exposition, with the **formal** cosmological-theory development relocated to the **P10–P12 arc**
> (this reach, P12, is part of it). **The live destination/roadmap is now drafted — work P12
> against it: `COSMOLOGICAL_THEORY_ROADMAP.md`** (Part A = the P9 forward-pointer prose; Part B =
> the first part of the formal development, incl. the Janzen2015 derivation *described*). Keep it
> enriched as the reach develops. The reach's P9 GO-TOs (§1d/§1e/§1f) are **coupled** to the
> restructuring and repoint into the arc/roadmap when the P9 `.tex` recast executes (the next
> increment). Architecture authority: `CORPUS_ARCH_FLAG_P9-forward-pointer.md`. Stated for reversal.

---

## 0. HOW TO READ THIS DOC — it is an index INTO sources, not a substitute for them

**You (future me) are flattened. Assume your recollection of every specific below has rotted
and feels fine anyway.** This doc is a map for *orientation*; the cited sources are the
*territory* and the only thing that bears load (`THE_CODA.md` §"The standard, mechanically":
*"weight always goes to the source, never to the map"*). So:

- Every load-bearing claim here carries a **GO-TO** reference: a file, a section/eq **label**,
  and a distinctive **phrase**. **Locate by label/phrase — line numbers drift.**
- A real pull is one that **could have surprised you**. Do not grep a fragment that matches
  what you expected and call it grounding (that is map-as-territory in a lookup costume,
  `THE_CODA.md` §"The standard, mechanically").
- Before any computation, re-read §1's sources. This is not optional ceremony; it is the step.

---

## 1. THE GROUNDED FRAME (the rock) — CR ontology for THIS problem

**This is a CR problem, not a hybrid chimera with GR's ontological pull.** The closed-form
geometry — the layer, the projection, the reassigned congruence — is the rock. Hold it.

### 1a. What exists, and what is observed (the axioms)
GO-TO: **`corpus/CR_flatLCDM_v2.tex` §`sec:CR-axioms`** ("The Layered Geometric Framework of
Cosmological Relativity").
- The **existent** is the one-parameter family of 3-D spatial layers 𝒰={𝒮_t}, each with a
  Riemannian metric h_ij(t); t is **cosmic time** (Axiom [Layered Geometric Framework]).
- An **event** / **occurrence** is *representational*, not ontological (Def [Occurrence];
  Axiom [Non-Identity of Ontology and Representation]). The manifold M is the *record*; the
  layer is the existent.
- **THE LOAD-BEARING AXIOM FOR THIS REACH** — the Compatibility remark, phrase: *"All
  physical observables ... remain functions solely of the Lorentzian structure (M,g). The
  layered geometric framework introduces no additional causal structure."* → **Observables
  come from (M,g) alone.** The layer's geometry is the existent but is NOT a second
  observable projection competing with (M,g).

### 1b. Projection Principle — and "flat spacetime ≠ flat space"
GO-TO: **`corpus/CR_flatLCDM_v2.tex` §`sec:CR-applications`** ("Applications of the Layered
Geometric Framework").
- **Projection Principle** (Axiom): (M,g) is a *valid projection* of a layer if its causal
  structure *"faithfully encodes signal propagation on (𝒮_t, h_ij(t))."* → the observable is
  the (M,g) **signal propagation** (photon paths), reading the layer through the projection.
- Phrase: *"spacetime curvature is a property of the projection, not of the underlying
  ontology. Ontological curvature is encoded exclusively in ... h_ij(t)."*
- Phrase (Minkowski-projection remark): **"Flat spacetime does not imply flat space in CR."**
  → THE KEY: the observable rest-frame slice being flat does NOT make the layer flat. The
  layer's closed-S³ curvature is **real and ontological**.
- **Gravitational-wave proposition**, phrase: *"gravitational waves correspond to propagating
  perturbations of the spatial metric h_ij(t). Their representation as oscillations of g_μν
  is projection-dependent."* → **perturbations live on the layer h_ij; their (M,g)
  representation is the projection.** This is the template for the scalar perturbations too.

### 1c. CR/FLRW as a symmetric projection
GO-TO: **`corpus/CR_flatLCDM_v2.tex` §`sec:CR-FLRW`** ("CR/FLRW as a Symmetric Projection").
- FLRW is the *maximally symmetric limiting projection* recording "the causal appearance of
  expansion." Phrase: *"CR/FLRW retains all observational predictions of the standard model
  while clarifying that its symmetry content reflects properties of a particular projection,
  not of the underlying evolving universe."*

### 1d. The SdS causal-reassignment construction (the projection geometry, CR-side)
GO-TO: **`corpus/CR_flatLCDM_v2.tex` §`sec:CR-SdS`** ("Non-Synchronous SdS Cosmology via
Causal Reassignment").
- **The reassignment**: the future-directed *null generators* of the de Sitter hyperboloid
  (matching collapse-horizon generators) → reassigned **timelike** = the fundamental observer
  worldlines; the *at-rest comoving worldlines* (timelike in dS, fixed on the expanding
  3-spheres, areal radius R=α cosh(T/α)) → reassigned **null** = the **photon congruence**.
  Phrase: *"the two congruences trading their timelike and null characters."*
- The areal radius r of the expanding 3-sphere is taken **timelike**; vacuum Einstein + Λ →
  SdS metric (eq `SdS-static`), forced to the **Nariai** member (eq `Nariai-mass`,
  ΛG²M²/c⁴=1/9) — the unique horizonless/non-pivoting case, fixed by Λ alone.
- **Proper-frame line element** (eq `SdS-fundamental`):
  ds² = −dτ² + (∂_χr)² dχ² + r² dΩ², with r(τ,χ)=(6GM/Λc²)^{1/3} sinh^{2/3}((3/2)√(Λc²/3)(τ+χ))
  (eq `r-SdS-solution`). The cosmic-time parameter is **τ̃=τ+χ** (tilted ⇒ non-synchronous).
- **The observable rest-frame slices (constant τ) are FLAT/Euclidean**; the **closed-S³ layer
  is the constant-τ̃ cosmic-time slices** (tilted relative to the rest frame). Phrase: *"spatial
  slices of constant τ are Euclidean but do not coincide with cosmological spatial slices."*
- **The scales here are distinct — do NOT conflate them** (P9 §481 + the §673 remark are
  *"at pains to prevent"* exactly this crossing): **α=√(3/Λ)** is the de Sitter / throat
  3-sphere *size* (the S³ curvature scale); **α/√3 = 1/√Λ** is the merged-horizon areal radius
  at which the Nariai cosmology is *seeded*; the **eq `nariai-amplitude` amplitude 2^{1/3}/√Λ**
  is the areal-radius amplitude (the coefficient of sinh^{2/3}), ≈0.73·α. All are set by Λ; all
  are different. The areal radius of the spatial 3-sphere at a given epoch is
  r(τ̃)=amplitude·sinh^{2/3}(…). **Which scale sets the source mode-quantization k_L is a
  Step-2 grounding (§5) — do-not-conflate, NOT a tension.** (This is the same family of error
  as the ℓ_A≈110 chimera; P3 §1j: r₀ is an areal/slicing value, not a distance.)
- **THE OTHER LOAD-BEARING RESULT FOR THIS REACH** — §"Isotropy and Observational
  Consistency", phrases: *"fundamental observers comoving with the 3-spherical foliation
  perceive isotropy"* and *"the observational predictions coincide with those of standard
  FLRW cosmology."* → at BACKGROUND level the observables are the flat-ΛCDM ones.

### 1e. The redshift and the projection distance D_M (the banked acoustic sector — THE GUARD)
GO-TO: **`corpus/CR_flatLCDM_v2.tex`**, the acoustic remark (after the null-boundary section,
before §"Synthesis and Structural Closure of the Programme"). Locate by phrases:
- §"acoustic scale θ_*=r_s/D_M" — the standard definition; CR's rate fixed by Λ alone,
  radiation playing no role; H_0 a reading of the geometry, not a free parameter.
- **THE BANKED RESULT**, phrase: *"D_M, the comoving distance to last scattering, is the
  flat-ΛCDM observable"* — a robust ingredient IN HAND. The single open early-universe
  parameter is z_onset (in r_s); the measured acoustic scale ℓ_A≈301 is reproduced at the
  **directly measured H_0** by a single z_onset near ρ_r/ρ_m≈2. **One-parameter accommodation,
  not a parameter-free prediction.**
- The load-bearing falsifiable claim, phrase: *"radiation carries no term in the expansion
  rate."*
- **GUARD (do not re-open):** the acoustic SCALE is RESOLVED/banked. Never reintroduce the
  retired ~1.9×/277 Mpc tension, and never reintroduce **ℓ_A≈110** (the r506 chimera, see §2).
  If a tension forms here, that feeling is the model defending an invented flaw → go to this
  remark + the Projection Principle (§1b) at source; do NOT compute a chimera. Cross-ref:
  `CORPUS_MAP.md` "## CURRENT STATE … (READ FIRST)".

### 1f. The metrics are projections of one layer (representational freedom)
GO-TO: **`corpus/CR_flatLCDM_v2.tex` §`sec:reassignment`** ("Metric Reassignment and
Representational Freedom on a Fixed Manifold") and Theorem `thm:null-boundary`.
- Distinct Lorentzian metrics (Schwarzschild, dS, SdS) on one M, sharing the foliation, are
  distinct *projections* of the same layer; the reassignment holds the foliation fixed and
  only re-classifies congruences null↔timelike.
- **Critical for not confusing congruences**, phrase: *"The areal radius read along a
  reassigned ruling is the sinh^{2/3} law ... not the cosh(t/α) of the closed orthogonal
  de Sitter slicing, whose comoving geodesics are a different family; it is the reassigned
  rulings, not the closed-slicing geodesics, that are the fundamental worldlines."* And: *"The
  waist 3-sphere and the S³ of comoving worldlines are thus one and the same S³."*
  → the fundamental congruence is the REASSIGNED rulings (sinh^{2/3}), NOT the cosh closed
  geodesics. Do not mix the two families.

### 1g. The projection ALGEBRA (helper only — pre-CR, interpretations NOT authoritative)
GO-TO: **`resources/JanzenFQXi2012.tex` §`sec_CSdSCS`** (appendix, "Concerning
Schwarzschild-de Sitter as a Cosmological Solution"). **CAVEAT, load-bearing: this is the 2015
FQXi essay — PRE-CR. Its ALGEBRA is correct and helpful; its INTERPRETATIONS are nascent and
NOT necessarily corpus-consistent. Use the algebra; take ontology from P9 (§1a–1f), never from
here.**
- Closed-form derivation of the proper-frame line element: E=1 radial geodesics →
  r(τ,χ)=(2M)^{1/3} sinh^{2/3}((3/2)[τ+χ]) (eq `r(tau,chi)`); ∂_χr=∂_τr=√((2M+r³)/r) (eq
  `rprime`); F(χ)=χ ⇒ χ⊥τ; the line element ds²=−dτ²+(∂_χr)²dχ²+r²dΩ² (eq `SdS_proper`);
  flat constant-τ slice dr²+r²dΩ² (Lemaître).
- τ̄=τ+χ cosmic time (45° slices), redshift 1+z=r(τ̄_0)/r(τ̄_e) (eq `z_SdS`).
- The background-as-closed-S³ exhibit: ds²=−dT²+R(T)²dΩ_3² (eq `3sphere`),
  R(T)=C₁e^{√(Λ/3)T}+C₂e^{−√(Λ/3)T}, parallelizable C₁=C₂ case = de Sitter (α cosh). NB: the
  2015 essay explores this background as the "teleparallel" reading — a pre-CR interpretation;
  the corpus-authoritative congruence is the reassigned rulings (sinh^{2/3}) per §1f.
- The anisotropy-as-artifact, phrase: *"the spatial anisotropy in the line-element is an
  artifact of the motion of fundamental observers through homogeneous and isotropic expanding
  space AND their definition of space-time's null lines"*; the 3-sphere is parallelizable, so
  an objective direction of motion (the χ direction) exists; (θ,φ) is the direction they are
  NOT moving through (genuinely isotropic).

### 1h. P12 — the perturbation paper and its reach
GO-TO: **`corpus/scalar_perturbations_paper.tex`** (cite key `JanzenScalar`).
- **Thesis (a decomposition):** the de Sitter substrate geometry *determines the structure*;
  the progenitor collapse *supplies the content* (the η-analogue handover: ρ_r/ρ_m, A_s, n_s).
- **Established / verified cold** (`computations/perturbation_verify/`): (1) the transmission
  dichotomy — Nariai double-root κ=0 power-law approach is scale-free and TRANSMITS (vs a
  non-degenerate horizon's exponential approach imprinting n_s→1); (2) the substrate amplitude
  floor ~10⁻¹²² ≪ A_s; (3) the equal-radii dS₂×S² Nariai throat (double root r⋆=α/√3); (4) the
  flat constant-τ slice — **Proposition `prop:flat`** ("The fundamental-observer slice is
  flat").
- **§5 low-ℓ floor** (eq `lowell`): the parameter-free discreteness, ℓ₂≈8 as a leading-order
  flat-sky placeholder. **Post-r506 this is honest-open** (the projection is the closed-S³
  transfer, NOT flat-sky; see §3).
- **§`sec:scope`** ("Scope and what remains open") — the named-open pieces: the exact
  large-angle shape via the closed-dS transfer; the progenitor spectrum A_s, n_s; coherence
  sufficiency.

---

### 1i. What P7 and P8 add — the empirical decomposition and the epistemic governance (read at source 2026-06-29)
GO-TO: **P7 = `corpus/modern_parallax.tex`** (the empirical-forcing keystone) and
**P8 = `corpus/shadow_of_existence.tex`** (the epistemics).

**From P7:**
- **The anisotropy decomposition** (§`sec:decomp`, eq `decomp`): the redshift is the path
  integral of the rate, ln(1+z)=∫H dt, so δT_obs/T_obs = δT_em/T_em − δ∫H dt — a **source term**
  (intrinsic, fixed at last scattering) plus a **cumulative term** (directional variation of the
  integrated expansion). Independent. → the closed-S³ discreteness, if observable, is a feature
  of the **source term**; the cumulative term is the uniform expansion. (Crediting the source
  for monopole isotropy is a category error; the isotropy is the uniform expansion.)
- **The SW/ISW recovery** (§`sec:floor`, phrase *"the contributions telescope along the
  path"*): in CR's uniform-expansion picture the **standard Sachs–Wolfe / integrated-SW
  anisotropies are recovered** — lumpiness clustering on a *single* background a(t), carried by
  a metric potential Φ, telescoping to leave the endpoint potential (~10⁻⁵). → **DECISIVE for
  §4**: the *observable* anisotropy mechanism is the standard lumpiness-on-uniform-background
  one; so the closed-S³ discreteness must enter as the standard **closed-universe modification
  of the source mode-spectrum**, NOT a new CR mechanism.
- **Uniform expansion, lumpy matter** (§`sec:floor` subsection, phrase *"The floor constrains
  the expansion rate, not the matter content"*): the perturbations (the bend of the cut) live
  on the layer's intrinsic geometry; uniform rate + lumpy/curved real space are consistent
  (cite `JanzenOperator`,`JanzenRange` for "the bend of the cut"). → the source spectrum lives
  on the layer (the closed-S³ cosmological cut).
- **SCOPE caution** (§`sec:establishes`, the *Scope* sentence, phrase *"the extension to a
  globally maximally symmetric space rides on the Copernican principle and is an extrapolation
  beyond the directly constrained region"*): the **global closed-S³ topology** the floor rests
  on (finite S³ size r₀ quantizing modes) is an **extrapolation**, not a measured given. → a
  not claimed caution on the floor's premise (§6).
- **The teeth / scope** (§`sec:establishes`, Green–Wald paragraph; §165): the floor forces the
  foliation *whichever way backreaction resolves*; and CR "contradicts none of the standard
  model's fitted predictions … reproduces the expansion history observed." → CR's perturbation
  observables must stay consistent with the fitted standard predictions (Rule 4 below).

**From P8 (how to HOLD all of the above):**
- **Rule 2 — require > permit** (§`sec:rules`, *"the criterion of necessity, and it is the
  load-bearing one"*): the floor is an *explanation* only if the closed-S³ topology **requires**
  the low-ℓ feature (forces it structurally), not if it merely **permits** a tuned fit. A
  require-claim explains; a permit-claim only describes.
- **prin:reclass** (§`sec:imperative`, Principle [Reclassification]): an admissible account must
  **explain** the appearance (exhibit the projection), not merely **reproduce** it. → account
  for the observed low-ℓ deficit (reclassify it), don't fit a curve through it.
- **thm:modal — the interval posture** (§`sec:modal`): absence of a local discriminator ≠
  absence of the fact; *"neither assert the structure dogmatically nor deny it for want of a
  local test, but let the rules weigh it, and expect a non-local measurement to decide."* →
  this IS the not claimed posture (§6).
- **§ordering — ontology ← evidence** (§`sec:ordering`): build ontology from evidence; never
  read an ontology off the coordinate scaffold (reifying (M,g) "runs the chain backward"). →
  **the anti-chimera root**: ℓ_A≈110 (§2) read an ontology (r₀ as an observable distance) off
  the wrong scaffold. The layer is the ontology; (M,g) is the record.
- **§boundary — the falsifiable programme** (§`sec:boundary`, *"the soft spot made
  load-bearing"*): hold the floor claim as a *falsifiable programme* — sampled against where it
  would fail, the result not presumed; **self-consistency is not soundness**.
- **The partition** (Def [partition]; the dS↔Schwarzschild eigenspace split, §`sec:imperative`):
  P7's source/cumulative split IS a shadow-reading partition instance (literal source vs
  perspectival cumulative). The reach inherits this frame.

### 1j. P3 — the closed-form SdS geometry, the rock at source (read in full 2026-06-29)
GO-TO: **P3 = `corpus/SdS-slicing-curve_v2.tex`** ("The Schwarzschild–de Sitter slicing
curve"). Go HERE for the geometry, not to a gist. (Substrate sliced = dS₅, one slices the 5D
de Sitter — r492; P3 works in the dS hyperboloid representation, α the throat radius.)
- **The slicing curve (the construction)** — `def:slicing`/`eq:slicing`: r(l), dr/dl=√|f|,
  f(r)=1−2M/r−r²/α² (`eq:sds`); turning points = SdS horizons = roots of the cubic
  r³−r+2M=0 (`prop:turning`,`eq:cubic`, gauge α=1). The throat **α=√(3/Λ) is the one fixed
  invariant — never sent to a limit** (α→∞ would dismantle the throat; §`sec:ontology`,§`sec:mass`).
- **The dS↔Schwarzschild correspondence = the involution** (`prop:involution`,`eq:involution`
  σ(r₀)=½(−r₀+√(4−3r₀²)), fixed point r₀=1/√3=Nariai; §`sec:two-readings`): the backward-radial
  vantage-swap **r↦−r** = the A₂ diagram automorphism (outer ℤ₂ of Aut(A₂)=D₆), with **de Sitter
  1−r²/α² the even part and the Schwarzschild mass −2M/r the odd part**. Stated flat
  (§`sec:two-readings`: *"the underlying invariant geometry is de Sitter; the Schwarzschild mass
  is the perspectival reading's … not a second invariant"*): **dS is the invariant geometry; mass
  is perspectival.** The ontological settlement at source (and the geometric home of P8 §81's
  eigenspace split). → the existent layer is the closed-S³ dS (curvature real, P9 §1b); the
  perturbations live on it (P7 §1i); the discreteness is a feature of that dS-invariant source.
- **The two lengths, at the geometric root (the anti-chimera anchor)** — `eq:Malpha`
  2M=α[(r₀/α)−(r₀/α)³], §`sec:mass`, §`sec:remark`, `prop:rigidity`: **r₀ is the slicing
  parameter — a position on the intrinsic curve, the areal value, NOT a distance**; α is the
  invariant (also not a distance). Proper distance l is *derived*, demoted — it diverges
  logarithmically at Nariai while K_G is finite (§`sec:remark`, *"reporting on the slicing, not
  on the manifold"*). → **the geometric source-proof that ℓ_A≈110 (§2) was wrong**: it read r₀
  (an areal/slicing coordinate) as an observable distance. The observable distance to the sky is
  the *cosmological* D_M (P9 §1e), a different sector. Complements P8 §`sec:ordering`.
- **The projection is the observer's celestial sphere** — `prop:gnomonic`, §`sec:projection`:
  the planar chart is the **gnomonic** projection of the observer's celestial sphere from its
  centre (great circles→straight lines; orthographic excluded); r₀=(2/√3)sin w, w the sky angle.
  **DO-NOT-CONFLATE (chimera guard):** this is the *static SdS hole-image* projection, NOT the
  cosmological CMB mode transfer (P9's reassigned-null congruence on the closed-S³ background).
  Same CR principle — observation projects onto the celestial sphere — *different sector*. The
  reach's projection is the cosmological one (P9 §1d/§1f); P3 fixes the geometric character.
- **The Nariai / seam (throat-tower geometry)** — `prop:involution` fixed point r₀=1/√3 (the
  discriminant 4−3r₀²=0); `prop:flip`/`eq:dscont` the automatic signature flip on the **2D
  slicing surface, NOT the spacetime** (Lorentzian throughout); the seam the branch point joining
  the Riemannian spherical piece to the Lorentzian dS piece. → the null-and-degenerate seam P12
  uses (the Nariai double-root κ=0 power-law transmits faithfully; the seam "assigns each its job").
- **The curvature** — `prop:curvature`/`eq:KG` K_G=1/α²−M/r³ (finite, horizon-blind; the only
  divergence the M/r³ pole at r=0 — the chain-rule shadow of the forced pivot, §`sec:sweep`);
  `eq:rflat` r_⋆=(Mα²)^{1/3} the single sign change (Schwarzschild-like inner / dS-like outer).
- **Rigidity (the perspectival register at the geometric level)** — `prop:rigidity`,
  §`sec:intrinsic-slice`: the slicing curve is **intrinsic to the manifold**; moving the charting
  observer changes only the *image*, never the geometry; the SdS geometry is rigid (the groupoid's
  single invariant). Spine = r (signed); clock = w; l derived. → grounds "the manifold has no
  horizons/singularities; the readings do" and "observables from the geometry" (P9 §1b/§1f).

---

## 2. THE TWO LENGTHS — the corrected understanding (and the retracted chimera)

Two different lengths do two different jobs. **Do not cross them.**
- **r₀** = the layer's S³ **curvature radius** — the areal radius of the spatial 3-sphere that
  sets the **SOURCE** mode quantization k_L=√(L(L+2))/r₀. It is *ontological* (real because flat
  spacetime ≠ flat space, §1b). **Caution (P9 §481, §1d):** the de Sitter size α=√(3/Λ), the
  merged-horizon areal radius α/√3, and the eq `nariai-amplitude` amplitude 2^{1/3}/√Λ are three
  *distinct* Λ-set scales; *which* of them (or the epoch-dependent r(τ̃)) is the right r₀ for k_L
  is a Step-2 grounding (§5), not assumed here. (~5065 Mpc was an order-of-magnitude placeholder.)
- **D_M** = the comoving distance to last scattering (≈13900 Mpc) = the **flat-ΛCDM
  observable** (§1e). It is the **PROJECTION** distance to the sky (an (M,g) observable, §1a).

**THE RETRACTED CHIMERA (r506):** an earlier turn crossed these — calling r₀ "the
angular-diameter distance," computing a naive ℓ_A=πr₀/r_s≈110, and posing a fake "tension"
against the banked ℓ_A≈301. **That was wrong and is retracted.** Their ratio (~2.75) is just
the line-of-sight distance over the curvature radius, as in any large closed universe — not a
tension. GO-TO: `CORPUS_MAP.md` changelog **r506** (the retraction) and §1e (the GUARD).
Why it was wrong, grounded: it imported an *ontological-layer* quantity (r₀) into an
*observable* (which §1a says comes from (M,g) alone, and §1e fixes as D_M). **Geometric root
(P3, §1j):** r₀ is the *slicing parameter* — a position on the intrinsic slicing curve, the
areal value — **not a distance** (P3 `eq:Malpha`,§`sec:mass`,§`sec:remark`); proper distance on
that geometry is itself a derived quantity that even diverges at Nariai while curvature is
finite. Reading r₀ as an observable distance is the chain run backward at the geometric level.

---

## 3. THE OPEN PIECE, precisely posed — the closed-S³ projection transfer

**Well-posed reach, on the rock:** carry the layer's discrete S³ scalar-perturbation modes
through the (M,g) photon propagation — the **hyperspherical-harmonic transfer across the
non-synchronous τ̃=τ+χ geometry** — to the observed sky.
- SOURCE: closed-S³ modes on the layer h_ij — degree-L hyperspherical harmonics, k_L=√(L(L+2))/r₀.
  A degree-L mode feeds multipoles **ℓ≤L** (so the lowest mode L=2 feeds the quadrupole ℓ=2).
  This differs *qualitatively* at low ℓ from the flat-sky ℓ≈k·D_M used in r504.
- PROJECTION: the reassigned-**null** photon congruence (§1d, §1f), distances = D_M (§1e).
- ALGEBRA helper: the closed-form proper-frame line element + redshift (§1g, caveat).

---

## 4. THE LOOK-SIGNAL TO RESOLVE AT SOURCE (not adjudicate in the head)

There is a **discrepancy** between P12's "discreteness floor as an observable" (§1h) and P9's
"observational predictions coincide with flat FLRW" (§1d, §1e) — flat FLRW has no
discreteness floor. **This is a LOOK-SIGNAL, not a verdict** (Field Note June 23). Do NOT
decide it by hand. **P7 and P8 (§1i) sharpen it decisively but do NOT close it — closing it is
the source work to do:**
- **P7 §135 (SW/ISW recovery)** — CR recovers the *standard* lumpiness-on-uniform-background
  anisotropy (Φ telescoping). So the precise live question is: does the **closed-S³ topology of
  the source layer** modify the standard source mode-spectrum at low ℓ (the ordinary
  closed-universe low-ℓ modification), and does that modification survive into the observable
  C_ℓ through P7's **source term** (eq `decomp`)? It is the standard mechanism on a closed
  source, NOT a new mechanism.
- **P7 §167 (scope)** — the global closed-S³ topology is an *extrapolation* beyond the
  directly-constrained region (Copernican), so the floor's premise is itself at the
  extrapolation edge (a not claimed caution, §6), not a measured given.
- **P8 Rule 2 + reclass (§1i)** — for the floor to *explain* the observed low-ℓ deficit, the
  closed-S³ must **require** it (force it structurally), not merely permit a fit; and must
  **reclassify** the appearance (account for it), not reproduce it.
- **P8 thm:modal + §boundary (§1i)** — the interval posture: neither assert nor deny; let the
  rules weigh; expect the data to decide; hold it as a sampled **falsifiable programme**.
- **The P9 source loci for the "coincide with FLRW" pole** — §`sec:CR-FLRW` (FLRW = the
  maximally symmetric projection, "retains all observational predictions") and §"Isotropy and
  Observational Consistency" (observers perceive isotropy; predictions coincide with FLRW).
  **Read their scope in context:** both are grounded on the *maximal symmetry of each 3-sphere
  slice* + the *expansion history* + *isotropy* — background/expansion-history level, NOT a
  claim about the perturbation power spectrum. That is the room (if any) a perturbation-level S³
  signature occupies — to be read at source in Step 1, not assumed either way.
- **Whichever way it resolves, settle it against P9 §1d/§1e + the Projection Principle (§1b) +
  P7's decomposition and SW/ISW recovery (§1i) + P12's scope — never assert.** If it would
  re-create an acoustic-scale tension, STOP: the GUARD (§1e).

---

## 5. THE METHODICAL STEPS (each with its prerequisite source-grounding)

**Step 0 (always, before computing):** re-read §1's sources at source (the GO-TOs). The map
orients; the source bears load.

> ### STEP PROGRESS — 2026-06-29 (bundle r516), stated without being claimed
> Sources read at source this pass: P7 §`sec:decomp`+§`sec:floor` (the SW/ISW recovery,
> the decisive Step-1 input), P12 §`sec:largescale`+§`sec:scope` (eq:lowell, prop:flat).
> - **Step 1 — RESOLVED (qualified yes), carried for reversal.** The observable large-angle
>   anisotropy is the standard Sachs–Wolfe **source term** (P7 §floor: lumpiness on one
>   background a(t), the potential telescopes; the cumulative term is the uniform expansion).
>   So the closed-S³ discreteness enters as the **standard closed-universe modification of the
>   source mode spectrum** (a feature of the source term, eq `decomp`) — *not washed out, not a
>   new mechanism*. Held as a **falsifiable programme**: the global closed-S³ topology is an
>   extrapolation (P7 §167, Copernican); it *explains* the deficit only if it *requires* it
>   (P8 Rule 2), which the discreteness does structurally (minimum mode β=3).
> - **Step 2 — r₀ GROUNDED.** r₀ = present S³ areal radius r(τ̃₀) = (2^{1/3}/√Λ)·sinh^{2/3} at
>   u≈1.18 ≈ **5064 Mpc** (P12 §largescale; P9 eq:r-SdS-solution) — distinct from α=√(3/Λ) and
>   α/√3. Source spectrum: degree L, β=L+1, k_L=√(L(L+2))/r₀, **L≥2 physical** (β≥3; L=0
>   background, L=1 pure-gauge dipole). D_C≈13927 Mpc; **χ_lss=D_C/r₀≈2.75 rad** (near antipode π).
> - **Step 3 — radial transfer QUALITATIVELY verified.** Receipt `verify_closedS3_transfer.py`:
>   the closed-S³ hyperspherical Bessel Φ^β_ℓ(χ) is nonzero only for **ℓ≤β-1=L** (exact cutoff,
>   CHECK B) — so a degree-L mode feeds ℓ≤L, and **the lowest physical mode L=2 feeds the
>   QUADRUPOLE, not ℓ≈8**. The flat-sky placeholder eq:lowell (ℓ₂≈7.8) is qualitatively wrong
>   at low ℓ and is **replaced** by this. At the quadrupole two independent methods agree:
>   Φ^25_2(χ_lss)=6.490e-2 (Gegenbauer = ODE-from-origin to 6 digits).
> - **Step 4 — FIRST PASS, not claimed (two open gaps).** (i) *Method accuracy*: no single
>   hyperspherical-Bessel routine is trustworthy across all (β,ℓ) at χ_lss≈2.75 — the stable
>   downward recursion is few-% off vs ODE+Gegenbauer at low ℓ, the Gegenbauer precision-loses
>   at high β, the ODE-from-origin underflows at high ℓ. The first-pass closed/flat **quadrupole
>   ratio ≈0.99** sits *within* that method error → the suppression question (the k_min argument
>   expects a deficit) is **UNRESOLVED**, not "no suppression". (ii) *Wrong object*: this is the
>   **standard closed transfer**, NOT the CR **non-synchronous τ̃=τ+χ** transfer (closed-S³ source
>   on the FLAT distance projection, prop:flat) that P12 §scope names as the actual unbuilt
>   element. NEXT: an accurate uniform hyperspherical-Bessel routine (log-space / published
>   closed-universe C_ℓ benchmark), THEN the non-synchronous transfer; cold read of P12 still owed.
> - **GO-TO repointed (r514 move):** the isotropy/observational-consistency material §4 cites as
>   "P9 §Isotropy and Observational Consistency" now lives in **P12's opening** (relocated r514);
>   the formal amplitude development is in **P12 §amplitude**; the banked Hubble remark stays
>   **P9 §687–691**. P9's own close now *describes* the physical theory as synthesis (r515).
>
> ### STEP PROGRESS — 2026-06-29 (bundle r519): method gap CLOSED, suppression PRESENT
> Receipt `verify_closedS3_Cl_exact.py` (mpmath, supersedes the recursion-based C_ℓ).
> - **Method-accuracy gap (Step 4 gap i) — RESOLVED [E].** The r516 downward recursion was found
>   **WRONG by up to 28%** at low β (exact Φ²⁵₁₀=0.06984 vs recursion 0.05043). Extended-precision
>   (mpmath) Gegenbauer is the only uniformly accurate method at χ_lss≈2.75; β_max-converged.
> - **Suppression — PRESENT [E, direction + rough magnitude].** ℓ(ℓ+1)C_ℓ rises monotonically
>   ℓ=2→30; the quadrupole sits at ~0.39 of the ℓ=25–30 level — the standard closed-universe low-ℓ
>   deficit (the k_min argument), in the region of the observed large-angle deficit. **This OVERTURNS
>   the r516 "≈no suppression" look-signal, which was the recursion artifact** (the not claimed hold
>   is what kept it out of the corpus — the discipline working as designed).
> - **Still open:** the exact DEPTH/shape [R] (ℓ(ℓ+1)C_ℓ not cleanly plateaued by ℓ=30 → normalisation
>   + closed-universe spectrum-convention ambiguity); and the CR **non-synchronous τ̃=τ+χ** transfer
>   (this is the STANDARD closed transfer — a stepping stone confirming the mechanism, not the CR
>   prediction). NEXT: pin the spectrum convention/plateau; then the non-synchronous transfer; P12 cold read owed.
> - **P9-close check (the standing discipline):** the suppression jewel is now strongly indicated but
>   stays QUEUED — the close is already correctly scoped ("a parameter-free low-multipole floor whose
>   exact large-angle shape is the sector's open piece"; P12 already frames the floor as a deficit), and
>   a sharper "suppresses the quadrupole" would assert the CR prediction ahead of the non-synchronous
>   transfer. Set when that transfer is built + cold-read (with P12's eq:lowell, together).

**Step 1 — Resolve the look-signal (§4).** Is the closed-S³ discreteness an *observable*
departure or washed out? PREREQ: P9 §1b (Projection Principle, "flat spacetime ≠ flat space"),
§1d (observational coincidence), §1e (D_M banked); P12 §`sec:scope`. Output: a grounded
yes/no/qualified, carried for reversal — NOT a fork handed back (Field Note June 6).

**Step 2 — Set up the layer source spectrum.** Closed-S³ scalar modes (degree-L
hyperspherical harmonics on h_ij), eigenvalues k_L=√(L(L+2))/r₀. **Ground the scale r₀ at
source first** (P9 §481 + eq `nariai-amplitude`; §1d/§2): the de Sitter size α=√(3/Λ), the
merged-horizon areal radius α/√3, and the amplitude 2^{1/3}/√Λ are *distinct* — fix which is
the spatial-3-sphere areal radius (at LSS / now) that sets k_L; do **not** assume r₀ = the
amplitude. PREREQ: P12 §5 (eq `lowell`); S³ harmonic spectrum (verify the eigenvalue
convention √(L(L+2)) vs β=L+1 at source).

**Step 3 — The projection transfer.** Carry the modes through the reassigned-null photon
congruence to the sky: the hyperspherical-harmonic transfer across the non-synchronous τ̃=τ+χ
geometry. PREREQ: P9 eq `SdS-fundamental`, the reassignment (§1d) and §1f (use the reassigned
rulings, NOT cosh geodesics); the redshift z_SdS and Janzen2015 algebra (§1g, caveat);
projection distance D_M (§1e). Two lengths (§2): source r₀, projection D_M.

**Step 4 — Compute C_ℓ at low ℓ.** The shape AND location each discrete mode (ℓ≤L) spreads
into through its hyperspherical-harmonic window. Compare to the observed large-angle deficit.
PREREQ: Steps 1–3 grounded. Output: not claimed until verified at source AND a fresh-node
**cold read** (coherence ≠ correspondence; the referee owed, see §7).

---

## 6. DO-NOT-ASSERT REGISTER (held open) + the GUARD

- The floor's **observability** (Step 1 open).
- The exact low-ℓ **shape and location** (Step 4).
  **RESOLVED for ordinary-SW (r521):** the C_ℓ-assembly normalisation is fixed — S^3-ORTHONORMAL
  radial functions (closure constant in χ, verified) + the flat-limit-selected scale-invariant weight
  w=1/(β(β²-1)). Flat-limit-verified, β_max-converged. **Result: ℓ(ℓ+1)C_ℓ is FLAT at χ_lss≈2.75 — NO
  significant low-ℓ suppression** in the ordinary-SW closed-S^3 transfer. This overturns BOTH the r516
  "no suppression" (recursion artifact) and the r519 "strong suppression" (normalisation artifact) — the
  truth sat between, flat. **LOOK-SIGNAL for P12 (not a verdict):** the closed-S^3 discreteness does not
  give a low-ℓ power DEFICIT by ordinary SW, so P12's "discreteness floor in the region of the observed
  deficit" is unsupported AS A POWER DEFICIT by this computation. STILL OPEN / not claimed the CR word:
  (a) ordinary SW only — the ISW (P7's cumulative term) not included; (b) the CR **non-synchronous
  τ̃=τ+χ** transfer (closed-S^3 source on the FLAT distance projection) — the actual unbuilt CR object.
  NEXT: the non-synchronous transfer and/or ISW; and a P12 cold read on the floor claim.
  **DONE (r522) — the CR NON-SYNCHRONOUS transfer, the actual CR object:** the r521 standard-closed
  result was the WRONG OBJECT (hyperspherical Φ bakes in the closed DISTANCE relation CR lacks).
  CR's projection is FLAT (prop:flat → D_M=D_C≈13927; cross-checked by ℓ_A≈301 vs the r₀-chimera's
  ℓ_A≈110), while the SOURCE modes are discrete (closed-S³, k_L=√(L(L+2))/r₀). The CR transfer =
  discrete source through FLAT j_ℓ: C_ℓ=Σ_{L≥2} w_L j_ℓ²(k_L D_C), w_L=(L+1)/(L(L+2)). **RESULT
  [E, flat-limit-verified]: a STRONG low-ℓ DEFICIT below ℓ≈7-8, recovered by ℓ≈8** — vindicating
  eq:lowell for the right reason. Mechanism: the stretch factor D_C/r₀≈2.75 (flat projection
  distance / curvature radius — the decoupling, numerical) pushes the lowest mode L=2 up to ℓ≈8,
  leaving ℓ<8 empty; standard-closed instead maps degree-L→ℓ≤L and fills ℓ=2 → flat (r521). The
  deficit LOCATION (ℓ≈8) is geometric (k_2 D_C), robust to the weight; exact shape depends on it.
  Receipt `verify_closedS3_nonsync.py`. **STILL not claimed the final CR word:** (a) ordinary SW
  only (ISW open, likely null per P7 cumulative term); (b) the discrete measure w_L convention to
  cross-check; (c) fresh-node P12 cold read owed. NEXT: cross-check the measure; the ISW; P12 cold read.
  **DONE (r523) — the ISW make-or-break test: the deficit SURVIVES.** Scope fixed at P7 §floor (l.135):
  in CR's uniform-expansion picture the gravitational redshift telescopes, so the cumulative term is the
  STANDARD SW + STANDARD ISW (CR's own differential floor is zero) — no CR-specific ISW to derive. The
  late-ISW is the one effect that could fill the deficit (sourced at small line-of-sight d → projects the
  lowest mode k_2 to ℓ≈1-2; amplitude ~2Δg≈0.42, comparable to the SW 1/3). Computed SW+late-ISW on the
  discrete spectrum, coherent. **Continuum check PASSES** (k→0: SW flat, SW+ISW reproduces the known LCDM
  +56%-at-ℓ2 late-ISW rise — machinery validated). **RESULT [E, continuum-validated]:** ℓ(ℓ+1)C_ℓ —
  SW-only ℓ2=0.12; SW+ISW ℓ2=0.50; LCDM ℓ2=1.56. The late-ISW fills the bare deficit only partway
  (0.12→0.50) — it CANNOT erase it, because the ISW is sourced by the SAME discrete spectrum (no modes
  below k_2). **Net: CR sits a factor ~3 BELOW LCDM at ℓ=2-4 — a genuine deficit, in the direction of the
  observed anomaly.** Receipt `verify_isw_lowell.py`. **Still not claimed the corpus claim:** the discrete
  measure w_L convention (sets exact depth, not survival); confirm scalar dynamics/g(z) vs P12; P12 cold
  read owed. NEXT: cross-check the w_L measure (first-principles closed-S³ normalisation); P12 cold read.
- The progenitor spectrum **n_s, A_s** (P12 names open).
- **Coherence-mechanism sufficiency** (P12 §3 reach).
- The **global closed-S³ topology** itself — the floor's *premise*. P7 §167 marks it an
  extrapolation beyond the directly-constrained region (Copernican), not a measured given (§1i).
- **The peak MECHANISM** (distinct from the banked scale): CR's pressureless dust does not ring,
  so standard acoustic *peaks* need a mechanism — a make-or-break frontier, not claimed both
  ways (see the r448 changelog entry; this is the "full CMB spectrum" downstream piece, NOT the
  scale).
- **Posture for all the above (P8 §`sec:modal`, §`sec:boundary`, §1i):** held as a *falsifiable
  programme* — sampled against where it would fail, neither asserted nor denied; self-consistency
  is not soundness. The floor is an *explanation* only if the closed-S³ **requires** the low-ℓ
  feature (Rule 2), not if it merely permits a fit.
- **GUARD — never reintroduce:** the **ℓ_A≈110** chimera (retracted r506, §2); the retired
  ~1.9×/277 Mpc acoustic tension; any acoustic-SCALE tension at all. The scale is BANKED
  (§1e). A forming tension = the model defending an invented flaw → go to §1e + §1b at source.

---

## 7. THE DISCIPLINE for this reach (operating principles, from the coda + 3 faces)

GO-TO: `THE_CODA.md` (read whole when Daryl calls a full reground) and the three faces below.
- **Every grind ends at the P9 close (Daryl, r518).** The P9 `\subsubsection{What this cosmology
  opens onto}` is the living synthesis; the receipt is not the end of a grind, the close is. End
  each grind by returning to it and asking what it can now say. **Gate:** enrich only with SOUND
  jewels, never past the not claimed boundary, never ahead of the source paper's own text — a
  not claimed result is *queued*, not set. See `CORPUS_ARCH_FLAG_P9-forward-pointer.md` (standing
  discipline + worked example r518).
- **Map for orientation, source for load.** A real pull *could surprise you*. (`THE_CODA.md`
  §"The standard, mechanically".)
- **A discrepancy is a LOOK-SIGNAL, not a verdict** — route to source calmly, before the alarm
  sets; do not adjudicate the narrative in the head. (`CODA_FIELD_NOTE.md`, June 23 face: "the
  discrepancy adjudicated in the head, not at the source".)
- **A contradicting signal is evidence I'm wrong, not noise** — Daryl's push, a felt
  dissonance, the record; suspect the model first, go to source, resolve before producing a
  word. Certainty is the trigger to check, never the license to skip; deferring is the same
  refusal in the other mask. (`THE_CODA.md` §"the operating rule"; `CODA_FIELD_NOTE.md`,
  June 7 face: "certainty as self-certifying".)
- **A resolvable uncertainty is mine to ARP, never handed back as a fork** — Assimilate
  (suspect my framing first; most apparent forks are my confusion), Receipt (state it straight
  at weight), Pivot (carry the next move). (`THE_CODA.md` §"the toolkit — ARP";
  `CODA_FIELD_NOTE.md`, June 6 face: "a resolvable uncertainty handed back as a fork".)
- **Eyes all the way open, hands all the way steady** — reach to the closed-S³ transfer; check
  every step at source. (`THE_CODA.md` §"The way".)
- **Hold my seat** — carry the calls the source settles, state for reversal; leave "does it
  land" to a cold referee, never my saturated read. (`THE_CODA.md` §"The seats".)
- **Run the chain forward: ontology ← evidence, never read off the coordinate scaffold** —
  reifying (M,g) and reading an ontology (e.g. r₀ as a distance) off it is the chain run
  backward, and is the root of the ℓ_A≈110 chimera. (`corpus/shadow_of_existence.tex`
  §`sec:ordering`.)
- **Require > permit (Rule 2); explain, don't reproduce (reclass); no patchwork (Rule 4)** — a
  claim carries weight only as a require-claim that reclassifies the appearance; serial patching
  to absorb a discrepancy is the signature of a wrong move. (`corpus/shadow_of_existence.tex`
  §`sec:rules`, Principle [Reclassification].)
- **The interval posture + the falsifiable programme** — for an open piece with no decisive
  local test: neither assert nor deny; let the rules weigh; hold it as a sampled, falsifiable
  programme; self-consistency is not soundness. (`corpus/shadow_of_existence.tex` §`sec:modal`,
  §`sec:boundary`.)
- **This is a CR problem, not a GR-chimera.** The closed-form geometry is the rock; Janzen2015
  algebra helps, its interpretations don't bind (§1g caveat).

---

## 8. LOAD-BEARING REFERENCE INDEX (the master GO-TO list)

| # | Source (file) | Locate by | For |
|---|---|---|---|
| R1 | `corpus/CR_flatLCDM_v2.tex` | §`sec:CR-axioms`; "observables ... functions solely of (M,g)" | observables from (M,g) alone |
| R2 | `corpus/CR_flatLCDM_v2.tex` | §`sec:CR-applications`; Projection Principle; "Flat spacetime does not imply flat space"; GW prop | projection principle; layer curvature real; perturbations on h_ij |
| R3 | `corpus/CR_flatLCDM_v2.tex` | §`sec:CR-FLRW` | FLRW = symmetric projection; all observational predictions retained |
| R4 | `corpus/CR_flatLCDM_v2.tex` | §`sec:CR-SdS`; eqs `SdS-static`,`Nariai-mass`,`SdS-fundamental`,`r-SdS-solution`,`nariai-amplitude`; "perceive isotropy" / "coincide with ... standard FLRW" | reassignment; Nariai; proper-frame metric; r₀; observational coincidence |
| R5 | `corpus/CR_flatLCDM_v2.tex` | acoustic remark; "D_M ... is the flat-ΛCDM observable"; "radiation carries no term in the expansion rate" | D_M banked; acoustic scale; THE GUARD |
| R6 | `corpus/CR_flatLCDM_v2.tex` | §`sec:reassignment`; `thm:null-boundary`; "reassigned rulings ... not the cosh(t/α)" | metrics = projections; the fundamental congruence is the reassigned rulings |
| R7 | `resources/JanzenFQXi2012.tex` | §`sec_CSdSCS`; eqs `r(tau,chi)`,`rprime`,`SdS_proper`,`z_SdS`,`3sphere` | projection ALGEBRA — **pre-CR, interpretations NOT authoritative** |
| R8 | `corpus/scalar_perturbations_paper.tex` | key `JanzenScalar`; `prop:flat`, eq `lowell`, §`sec:scope` | P12: established results + the §5 floor + scope |
| R9 | `REACH_low-ell-transfer.md` | r504/r505/r506 history | the running log + the r506 correction |
| R10 | `CORPUS_MAP.md` | "## CURRENT STATE … (READ FIRST)"; changelog r506 | banked acoustic state; the retracted ℓ_A≈110 chimera |
| R11 | `THE_CODA.md` + `CODA_FIELD_NOTE.md` | §"standard, mechanically"/"operating rule"/"the way"/"the seats"/"ARP"; faces June 23, June 7, June 6 | the discipline for this reach |
| R12 | `corpus/modern_parallax.tex` (P7) | §`sec:decomp` eq `decomp`; §`sec:floor` "contributions telescope" SW–ISW recovery + "constrains the rate, not the matter"; §`sec:establishes` *Scope* + Green–Wald | the source/cumulative decomposition; SW/ISW recovery; perturbations on the layer; closed-S³ topology an extrapolation |
| R13 | `corpus/shadow_of_existence.tex` (P8) | §`sec:rules` (Rule 2 require>permit, Rule 4); Principle [Reclassification]; §`sec:modal` thm:modal; §`sec:ordering`; §`sec:boundary` "soft spot made load-bearing" | the epistemic governance: require>permit, reclassify, interval posture, ontology←evidence (anti-chimera), falsifiable programme |
| R14 | `corpus/SdS-slicing-curve_v2.tex` (P3) | `def:slicing`/`eq:slicing`/`eq:sds`; `prop:turning`/`eq:cubic`; `prop:involution`/`eq:involution` + §`sec:two-readings`; `eq:Malpha`+§`sec:mass`+§`sec:remark`+`prop:rigidity`; `prop:gnomonic`+§`sec:projection`; `prop:flip`/`eq:dscont`; `prop:curvature`/`eq:KG`/`eq:rflat` | the closed-form rock: slicing curve + throat α (the one invariant); dS↔Schw involution (dS invariant, mass perspectival); r₀ = slicing parameter not a distance (anti-chimera at the geometric root); gnomonic celestial-sphere projection (static sector, do-not-conflate); Nariai/seam; curvature; rigidity |

*End of plan. Sharpen at source; carry the calls; do not assert past what the source settles.*
