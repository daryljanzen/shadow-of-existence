> **⌗ RETIRED r2380 under `RG-1` — AND IT IS RETIRED PARTLY BECAUSE IT IS KNOWN WRONG IN A WAY ONE BANNER
> CANNOT HOLD.**
> *A4, the first build of the matter branch-point crossing.* ⛔ ***It carries an r2206 LOCUS CORRECTION at its
> head saying that the build "repeatedly identifies the crossing surface as the Nariai degenerate horizon at
> $r=+\alpha/\sqrt3$", which is WRONG — the crossing is the BRANCH POINT $r=0$, corrected in the corpus at
> r2154 and never propagated into this file's body.*** *So the document is **twenty kilobytes of prose
> repeatedly stating a wrong locus, with one correction at the top**. That is the naming rule's own hazard
> (`ONTOLOGY_FOUNDATION_INDEX` §0: four loci, repeatedly conflated for ~2000 revisions) in its purest form, and
> **a banner is not a fix — it is a sticky note**, which is exactly why `retired/` exists as a place and not a
> banner.*
>
> **⌗ ITS LIVE CONTENT, and it is genuinely load-bearing:** *A4's **structural transition law** — the causal
> reassignment **fixes the RATE (time-stacking, $\Lambda$-set) and does not touch the DENSITY (leaf-carried,
> inherited)** — is settled corpus and is stated at the ontology map §1e and §1·LEVELS, and it is what Phase 1
> combined to inherit the generations. **The law survives; the locus in this file does not.**
> ⌗ *And the crossing question itself closed at c54.113: there is no worldline crossing to compute.*

---

# A4 — Matter branch-point crossing dynamics: the first-build log

> ## LOCUS CORRECTION (r2206) — READ BEFORE USING THIS DOCUMENT
> **This build repeatedly identifies the crossing surface as *the Nariai degenerate horizon* at
> $r=+\alpha/\sqrt3$. That is WRONG, and it was corrected in the corpus at r2154 (P15
> `prop:transmission`) without being propagated here.**
>
> - **The crossing — where matter transitions, where the collapse leg becomes the expansion leg —
>   is the BRANCH POINT $r=0$.** It is *interior* to the lap.
> - **$r=+\alpha/\sqrt3$ is the SEAM**, the Nariai double root — the lap's unit-speed locus, met a
>   full lap after the branch point, at $z\approx0.66$. *It is not the beginning and not the crossing.*
> - The two are separated by the whole excursion: seam $\to240^\circ$ (the $r<0$ collapse side)
>   $\to$ **branch point** $\to120^\circ\to$ seam again.
> - At $r=0$, $f\to-2M/r$ diverges, so $r_*$ is **finite** — which is *why* transmission is
>   scale-free (r2154). The Nariai argument the old text used is replaced, not repaired.
>
> **Every statement below that places the crossing at the Nariai horizon is to be read as placing it
> at $r=0$.** *The physics — finite-curvature characteristic IVP, isotropisation, scale-freedom, the
> transition law — survives; only the locus was misassigned.*

---


**Frontier:** Cluster A, the matter sector. A4 = the dynamics by which matter and observers
transition through the cosmogenesis branch point. This is the first-named open problem in P7's own
abstract, and P7 defers it three separate times (§547, the thm:null-boundary remark, and the
Perspectival-Singularity remark): the *geometric* continuity across the branch point is established;
the *matter* transition through it is not.

**SCOPE GUARD (load-bearing; confirmed with Daryl).** A4 builds the *transition
dynamics/structure* — how matter degrees of freedom and observers cross the seam, what is
preserved vs. reassigned, and the regularity that makes the crossing well-posed. It does **not**
derive the inherited *values* — ρ_r/ρ_m, A_s, n_s, composition. Those are F1, which the corpus
has settled as measured data (η-analogue), off-runway. If any step here starts producing a value
for the inherited content, the guard has failed and the step is void. Everything below is stated
for reversal.

---

## What is ALREADY established across the branch point (so A4 does not re-fight it)

Three layers are built; A4 is only the fourth.

- **Geometry — [established].** The Null-Boundary Correspondence Ψ carries the collapse horizon
  ℋ⁺ to the cosmological horizon ℋ_c⁺(p) by causal reassignment; it preserves the null
  fibration, affine ordering, future orientation; it is not in general an isometry (areas,
  surface gravities differ) — causal and structural, not metric. At the *occurrence* it is
  forced to the Nariai degenerate double root and reduces to the identity: metric and rigid at
  the seam. C⁰ *geometric* continuity is stated. *(P7 `CR_framework.tex`, thm:null-boundary
  §602–634, and the Perspectival-Singularity remark §644–645.)*
- **Fields / linear perturbations — [established, P13].** What the branch point does to perturbation
  modes crossing it is already built: the seam is a **null** surface, so its initial-value
  problem is **characteristic, not Cauchy** — one datum, hence one phase, per mode → coherence
  (§coherence); the dS₂ throat **isotropizes** (de Sitter no-hair damps every ℓ≥1, only the ℓ=0
  monopole survives; §throat, prop:throat); and because the seam is **degenerate (κ=0)**, its
  approach is power-law / scale-free and it **transmits the progenitor spectrum unaltered**
  (§transmission, the transmission dichotomy). The acoustic modes are **sub-horizon** at the
  seam (prop:subhorizon), so whatever fixes them is the handover, not a super-horizon freeze-out.
  *(P13 `CR_cosmology.tex` §coherence, §throat, §transmission, §sec:properframe.)*
- **Content — [inherited / measured; OFF-LIMITS = F1].** ρ_r/ρ_m ≈ 2, A_s, n_s, light-element
  composition. Measured boundary data, the η-analogue. Not A4's to derive.

The field-transmission story is *linear modes on a fixed background seam*. A4 is the transition
of the **matter itself** — the stress-energy, and material worldlines/observers — through it.

---

## Milestone 1a — the object that must transition: matter is the bend of the cut — [established at source]

In CR the matter content is not an independent posit fed into the geometry; it is the curvature
of the spatial cut.

- Spherical, from the slicing curve `f(r) = 1 − 2m(r)/r − Λr²/3`: the energy density is the
  radial growth-rate of enclosed mass,
  **ρ(r) = m′(r) / 4πr²**, i.e. `8π G^t_t = (rf′ + f − 1)/r² + Λ`.
  A straight cut (m′≡0) is vacuum; the bend (m′≠0) *is* the density. Crucially it depends on the
  **spatial profile alone**, independent of the lapse (the lapse carries the radial pressure via
  `8π(p_r+ρ) = (f/r) d_r ln(A/f)`; the construction-gauge lock A=f gives p_r=−ρ).
  *(P8 `slicing_operator.tex` §sec:bend prop:bend eq:rho, §sec:lapse prop:lapse.)*
- General spatial leaf: the density is the leaf's intrinsic+extrinsic curvature departure from
  the substrate — the **Hamiltonian constraint**,
  **16πρ = ³R + K² − K_ij K^ij − 2Λ**, of which ρ = m′/4πr² is the spherical instance.
  *(P8 §sec:open.)*

So the object crossing the seam is the bend — carried by the leaf's ³R and extrinsic curvature
K_ij. The transition law is a statement about *that* object on the seam.

---

## Milestone 1b — the seam locus map — [distinctions established at source; one relation OPEN]

The cosmogenesis branch point must not be conflated with three neighbouring objects. The papers hold
them deliberately apart, and getting the locus right is prerequisite to writing any transition.

- **The cosmogenesis branch point (where matter transitions):** the **Nariai degenerate horizon** —
  the merged double root at areal radius **r⋆ = α/√3** in the static SdS chart, `f(r⋆)=f′(r⋆)=0`,
  surface gravity κ=0, near-horizon geometry a **dS₂×S²** throat. A null-*and*-degenerate
  finite-curvature metric singularity. This is what the NBC forces at the occurrence and what the
  perturbations cross. *(P13 §causal-reassignment §95–101, prop:throat; P7 thm:null-boundary.)*
- **Read in the proper frame (§properframe):** the same beginning is `τ̃ = 0`, where the
  cosmological scale factor `r(τ̃) = (6GM/Λc²)^{1/3} sinh^{2/3}(…)` → 0. This is the **branch
  point** of the analytic scale factor (the conjugate branch sits at constant phase **2π/3** for
  τ̃<0), *not* a real r=0 boundary — "the analytic counterpart of the beginning at the
  finite-curvature seam." *(P13 §sec:properframe, eq:scalefac, fig:scalefac3d.)*
- **NOT the throat X=α:** the equatorial throat, where the slicing curve runs tangent to the
  throat circle, is a *different* turning point — the locus of the 2D slicing-surface signature
  turnover (`sinθ ↦ coshψ`, θ↦π/2+iψ), the spacetime staying Lorentzian throughout. *(P3
  `SdS-slicing-curve_v2.tex` abstract + §sec:seam; P7 §644 states explicitly it is distinct from
  α/√3.)*
- **NOT the backward-radial r=0:** the reflection r↦−r onto the conjugate (r<0) branch is a
  distinct crossing again, and r=0 is the *perspectival* (odd, mass-carried) curvature
  singularity, which no finite-time layer reaches. *(P7 §644; P3 §sec:ellipse.)*
- **Three Λ-set scales kept apart throughout (P13 §101):** α = √(3/Λ) (the dS 3-sphere size);
  α/√3 (the merged-horizon radius); 2^{1/3}/√Λ = 2^{1/3}α/√3 ≈ 0.73α (the scale-factor
  amplitude (6GM/Λc²)^{1/3} at the Nariai M). Do-not-conflate.
- Also distinct: the **wall** (Type-N, free radiation) is *not* a cosmogenesis branch point — it has no
  degenerating Killing field for the NBC to act on; cosmogenesis lives only at the
  finite-curvature Killing-horizon strata. *(P11 `dynamics_paper.tex` §sec:wall prop:wall.)*

**OPEN sub-question (must pin at source before any transition setup):** the precise
coordinate/reading relationship between the proper-frame seam (τ̃=0, scale factor → 0, the branch
point) and the static-chart Nariai degenerate horizon (areal radius α/√3, dS₂×S²). These are two
readings of the one cosmogenesis event, but *where in the geometry the matter actually crosses* —
and how the dS₂×S² near-horizon throat that the fields cross relates to the τ̃→0 scale-factor
branch point that the cosmology begins at — is not yet pinned here. This is load-bearing: the
transition law is written on whichever surface is the true crossing.
**→ RESOLVED in Milestone 2 below** (P12 §discrete disambiguates three distinct seam-operations).

---

## Milestone 2 — the crossing surface, resolved — [established at source]

The overloaded "seam"/"throat" is disambiguated by P12 `algebroid_paper.tex` §sec:discrete,
which names **three distinct discrete operations**, each anchored at its own locus by the horizon
cubic `r³ − α²r + 2Mα²` (roots summing to zero, the A₂ configuration):

1. **The Nariai seam** — the fixed point of the root-permutation transposition, where two roots
   collide and the discriminant `−4α⁴(27M²−α²)` vanishes: the double root at areal radius
   **r⋆ = 1/√Λ = α/√3**, near-horizon geometry **dS₂×S²**, isotropy jumping 4→6. Here the
   isotropy-jump locus *is* the metric-degenerate locus (κ=0). *(P12 §strata §124, §discrete
   §128; P13 prop:throat.)*
2. **The cosmogenesis horizon** — the locus of the **null↔timelike reassignment** (the NBC move,
   the radial direction promoted to cosmic time). *(P12 §128; P7 thm:null-boundary.)*
3. **The Riemannian↔Lorentzian seam** — the locus of the **signature flip** (`sinθ↦coshψ`,
   θ↦π/2+iψ), at the equatorial throat X=α where the slicing curve is tangent to the throat
   circle; the 2D slicing-*surface* signature turns over, the spacetime Lorentzian throughout.
   *(P12 §128; P3 §sec:seam prop:flip.)*

**The crossing surface for A4 is #1∘#2: the Nariai degenerate horizon (r⋆ = α/√3 = 1/√Λ, κ=0,
dS₂×S²), where the null↔timelike cosmogenesis reassignment acts.** The NBC forces the *occurrence*
to the Nariai member (§95), so the generically-distinct collapse and cosmological horizons merge
there and the cosmogenesis-reassignment locus coincides with the Nariai degenerate horizon. This
is the finite-curvature metric singularity of P1 — the null-and-degenerate species.

**Held distinct (NOT the crossing surface):** the Riemannian↔Lorentzian signature-flip seam at
r=α (#3) is the general `sin→cosh` *continuation mechanism* — P3 §418 calls it "the geometric
substrate of the cosmogenesis," i.e. the tool by which any radial direction is reassigned to
cosmic time — but it is a *different operation at a different locus* from the physical
matter-crossing (P7 §644 states this explicitly, "neither is the merged-horizon α/√3"). And
r=0 (the backward-radial branch point, the perspectival curvature singularity) is a third,
distinct crossing again. Three operations, three loci; the matter crosses at #1∘#2.

**Proper-frame reading:** the same cosmogenesis event, read along the fundamental (E=1) congruence,
is τ̃=0 where the scale factor r(τ̃)∝sinh^{2/3} → 0 — the analytic branch point (conjugate branch
at phase 2π/3), the cosmological face of the beginning at the Nariai degenerate horizon.

---

## Milestone 3 — the matter transition, set up — [setup + regularity established; the T^μ_ν reassignment flagged OPEN]

**The setting, pulled at source.** The crossing surface's near-horizon geometry is **dS₂×S² with both curvature radii 1/√Λ** (prop:throat: at Nariai `f(r⋆)=f′(r⋆)=0`, `f″(r⋆)=−2Λ`, `r⋆=α/√3=1/√Λ`; the S² has Ricci R₂=2Λ, the dS₂ has radius²=1/Λ; the Ginsparg–Perry limit). What is **already built here for the linear FIELD modes** (P13, established): (i) **angular no-hair** — the degree-ℓ S²-harmonic is a dS₂ field of mass² `m²=ℓ(ℓ+1)Λ`, so the monopole ℓ=0 is the ν=½ scale-invariant survivor while every ℓ≥1 is heavy principal-series (ν²<0), oscillating and decaying under the dS₂ de~Sitter no-hair (prop:throat); (ii) **scale-free transmission** — the degenerate κ=0 approach is power-law (tortoise `r∗∼−1/[Λ(r−r⋆)]`), carrying no thermal scale, so the progenitor spectrum crosses unaltered (prop:transmission, prop:transmit). **The A4 target is the same crossing for the MATTER** — the background stress-energy and material worldlines, not the linear perturbation modes — the piece P7 defers.

**3a — the simplest matter-carrying cut [grounded choice].** The matter-as-bend (P8 §bend): a cut with mass function m(r), m′≠0, carries ρ(r)=m′(r)/4πr², radial pressure set by the lapse's divergence from the curve (§lapse, `p_r+ρ=(f/r) d_r ln(A/f)`). The simplest matter-carrying cut crossing the Nariai degenerate horizon is the **spherically-symmetric (ℓ=0, isotropic) bend** — a small matter content m′≠0 on the Nariai vacuum background (whose m is the constant Nariai mass) — the non-vacuum analogue of P11's polarized-Gowdy minimal vacuum-radiative choice, and exactly the isotropic monopole the throat's angular no-hair selects as the survivor.

**3b — the transition as characteristic data [extension of established machinery].** The Nariai degenerate horizon is **null** (κ=0), so the bend's initial-value problem on it is **characteristic, not Cauchy** (standard for a null hypersurface; CR applies it at the branch point in P13 §coherence). The bend — (³R, K_ij), the leaf's intrinsic+extrinsic curvature carrying the stress-energy via the Hamiltonian constraint — is set as characteristic data on the degenerate null surface. What that data does on crossing, in three parts:
- **Angular [extension, grounded on prop:throat]:** the same dS₂ no-hair that damps the ℓ≥1 field modes damps the **anisotropic (ℓ≥1) component of the crossing stress-energy** — the stress-energy is curvature content via `16πρ=³R+K²−K_ijK^ij−2Λ`, so the no-hair acts on it — leaving the isotropic ℓ=0 monopole. The matter counterpart of the established field angular no-hair: the crossing **isotropizes the matter content**.
- **Scale [extension, grounded on prop:transmission]:** the degenerate κ=0 approach is scale-free, so **no thermal scale is imprinted** on the crossing matter — the matter counterpart of faithful field transmission.
- **Regularity [ESTABLISHED — the first result]:** the crossing is **well-posed for finite bend**, because the Nariai degenerate horizon is a **finite-curvature** surface (r⋆=1/√Λ, dS₂×S² both radii 1/√Λ — prop:throat), so ρ=m′/4πr² is finite there and the characteristic data is finite. This is P1's **null-and-degenerate** species — null (characteristic IVP) *and* finite-curvature (finite bend) — so the matter crosses with **no curvature obstruction**, unlike the r=0 perspectival singularity no finite-time layer reaches. This is the matter counterpart of the established C⁰ geometric continuity (P7 NBC thm).

**Delivered:** the matter transition is a **well-posed characteristic-data crossing on the finite-curvature degenerate null surface, isotropizing and scale-free** — the matter counterpart of the established C⁰ geometry + field transmission. **No value derived** (guard holds: what the surviving isotropic ρ's amplitude and composition *are* remains the inherited F1 datum, off-limits).

**3c — the reassignment's action on the matter, resolved [established at source; the T^μ_ν "reassignment" dissolved, not filled].** Read at source, the flag was right and the finding is sharper than a "frame map." The NBC theorem (thm:null-boundary §602–634) is a **causal/structural, vacuum** correspondence: Ψ maps the collapse horizon to the cosmological horizon preserving the null fibration, affine ordering, and future orientation, is *not* in general an isometry, and reduces to the identity at the Nariai seam — it carries **no action on T^μ_ν**. And the matter transition is **explicitly deferred, twice, right at the theorem**: the mechanism by which matter and observers transition through the shared layer is "beyond the scope of this paper" (§641), and "the matter dynamics of the transition lie beyond the present scope" (§644). So there is no stress-energy reassignment to read off the theorem; the earlier "branch-point crossing frame map on stress-energy → ρ_r/ρ_m = Γ_eff−1" was manufacturing an action the theorem does not contain. **The chimera dissolves — it is not to be filled.**

What the theorem *does* fix settles the transition structurally, through P8's leaf/stacking split:
- The reassignment **preserves the cosmic foliation** (§604, §623–625) — the leaves, the expanding 3-spheres. The density ρ = m′/4πr² is **leaf-carried and lapse-independent** (P8 prop:lapse). So the reassignment, acting on causal roles and not on the leaf, **does not touch the isotropic density**: it crosses as inherited progenitor content, its value the F1 datum.
- The reassignment's whole action is on the **causal roles / the time-stacking** — the null direction promoted to timelike cosmic time (§625) — i.e. the **rate**. The theorem's own result is exactly that: it fixes the sinh^{2/3} rate, Λ-set (§637 corollary, §659).

**The structural transition law: the reassignment fixes the RATE (time-stacking, Λ-set) and does not touch the DENSITY (leaf-carried, inherited).** This is the structural *reason* the matter content (ρ_r/ρ_m, composition) is inherited (F1) rather than produced — the mechanism acts on the rate, never on the leaf — recovering CORPUS_MAP's CURRENT STATE and P5's "forces the rate, not the matter" *from* the reassignment's foliation-preservation. **No value produced; the guard is confirmed by the mechanism, not asserted against it.**

**The genuine remaining open piece** (not manufactured): the matter *dynamics* — the actual propagation of material worldlines/fields through the seam for a given matter model — is what P7 defers, and what 3b's regularity shows to be **well-posed** (finite-curvature characteristic crossing), matching P7 §658 ("the Null–Boundary Correspondence … fixes the cosmological beginning at the branch point at $r=0$ (well-posed because $r_*$ CONVERGES, **not** because curvature is finite -- it diverges there; r2234), which makes the early-universe sector well posed"). The well-posedness is established; the detailed worldline dynamics is the deferred depth — and it is *dynamics*, never a value.

---

## Milestone 3 — delivered

The matter transition is: a **well-posed characteristic-data crossing on the finite-curvature degenerate null surface** (3b regularity, matching P7 §658), **isotropizing and scale-free** (extensions of the established field no-hair/transmission, marked as extensions), and structurally governed by **the reassignment fixing the rate and inheriting the density** (3c). This is a real advance on what P7 defers three times — it moves the matter transition from "beyond scope" to *well-posed, with the structural transition law in hand and the F1 boundary explained from the mechanism* — while the detailed matter dynamics (solving the crossing for a specific matter model) remains the deferred depth. **No value derived anywhere; the scope guard held throughout and was confirmed by the mechanism.**

## Next

Milestone 3 is a coherent unit → logs as r564 + bundle. The matter-sector frontier's next open pieces are a genuine strategic fork (the material doesn't pick for us): (a) the matter *dynamics* — the worldline/field propagation through the now-well-posed seam for a concrete matter model; (b) the **wall** as the onset of free gravitational radiation (P8/P9, `range_paper` cor:radiation); (c) the **chiral matter forced across the branch point**, AH-walled and non-geometric (P14 `boundary_paper`). Which of these is Daryl's call.

*Milestones 1–3 banked. Source-grounded, scope guard held and mechanism-confirmed, extensions marked as extensions, the chimera dissolved at source. Stated for reversal.*
