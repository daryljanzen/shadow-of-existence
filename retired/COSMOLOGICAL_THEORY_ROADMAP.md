> **⌖ RETIRED r1537 — verified landed.** This was the roadmap for relocating the formal cosmological development into the **P10–P12 arc** (r514). **Landed:** all three papers exist and compile — `canonical_time`, `dynamics_paper`, `algebroid_paper`.
> Kept as record; **do not work from it.**


> **[†ONT-COSMO] Cosmological grounding — read before computing.** Whenever this doc's work touches the expansion rate, the early universe, or the seam, the forced model to plug in — **not** an FLRW default — is held whole in `ONTOLOGY_FOUNDATION_INDEX.md` §1b: the *observable* rate is radiation-free sinh^{2/3} (Nariai proper frame, fixed by Λ, **read leftward** — radiation/matter inherited content, never a rate source); the *progenitor/local* dynamics is ordinary GR at the standard Friedmann rate (where BBN runs, below the ~1.6 eV onset); the two regimes are distinct and meet at the reassignment seam; the beginning is the finite-curvature seam, not r=0. Conflating the two regimes is the veer that thrashes.

# Cosmological-Theory Formal-Development Roadmap — the forward-pointer's destination

*Living working document (r512, gate session with Daryl). **This is the roadmap the P12
scalar-perturbation reach is worked against**, and the **destination** of the strong
forward-pointer that closes P9. It is built and **enriched incrementally** as the theory is
developed — a strong, durable, always-referenceable description of the current state, polished
as we go (not a perfect cherry dropped at the end). Companion to
`REACH_PLAN_perturbation-projection.md` (the breadcrumb trail) and
`CORPUS_ARCH_FLAG_P9-forward-pointer.md` (the architecture decision). **Stated for reversal**
until the work is done; a forward-pin option to revisit the structuring is held open, but we
proceed confident the change sticks.*

**The separation being run (two axes — settled r513).** P9 (`CR_flatLCDM_v2.tex`) is *both too
much and not enough*. We cut along both axes:
- **The "too much"** — P9's overshadowing formal SdS-cosmology development — is moved to its
  rightful place as **P12's OPENING: the opening that P12 closes.** P12 opens with the formal
  cosmological-theory development (**Part B** below), and its existing perturbation sections
  *close* it — completing the cosmological theory by developing its scalar sector. (The slot is
  P12's thin §`sec:background`, which today merely leans on P9; it *becomes* Part B.)
- **The "not enough"** — P9's conceptual reach, which today stops partway — is **cranked all the
  way up to the end** (**Part A** below): a forward-pointer + a conceptual exposition reaching
  conceptually to the *full* destination (the whole theory developed through P10–P12), confident
  because the route is mapped. P9's crowning achievement becomes the clear conceptual whole, not
  the partial formalism.

So P9 closes the dynamical foundational trilogy by *knowing and showing the whole* conceptually;
the formal development lives where it completes something — P12, the opening it closes.

---

## PART A — P9 end-section: forward pointer + conceptual exposition  *(staged prose; to apply to P9, stated for reversal)*

*Goal: the conceptual crown. Explain what the CR core opens up — the shape of the cosmological
theory — clearly enough that the reader sees the whole, and is handed forward to the formal
development without the paper trying to do that development itself.*

### A1 — The conceptual shape: one reassignment, and a whole cosmology falls out
The CR core has, to this point, established the layered ontology, the projection principle, and
the Null–Boundary Correspondence: distinct Lorentzian metrics on one manifold are distinct
*causal readings* of one evolving spatial layer. The cosmological theory is what this core
*opens up* when the reading is applied to de Sitter space itself. The move is a single causal
reassignment. The de Sitter hyperboloid is ruled by null generators; promote the one
future-directed bundle whose causal sense matches a collapse horizon's generators to the
**timelike** fundamental congruence, and the complementary at-rest comoving worldlines become
the **null** photon congruence — the two trade causal characters, the foliation by expanding
3-spheres preserved. The vacuum representation compatible with this reassignment is
Schwarzschild–de Sitter, and the cosmology is forced to its **Nariai** member — the unique
non-pivoting tilt, fixed by Λ alone, the one configuration whose fundamental worldline grazes
its horizon rather than crossing it (the limiting orientation a collapse actually selects). No
mass is fitted; the cosmology is *selected*, not tuned. What falls out is an expanding closed
3-sphere whose radius obeys the exact sinh^{2/3} law of flat ΛCDM — the empirically successful
expansion history — with no dynamical input from matter density.

### A2 — Why the apparent curvature singularity dissolves
The reading also dissolves a feature the naïve picture takes as real. In the Schwarzschild
(massive) reading the metric carries a curvature singularity at r=0 — the Kretschmann scalar
diverges there. But that divergence is the *odd part* of the geometry under the backward-radial
reflection r↦−r: the de Sitter piece 1−r²/α² is even (invariant, the literal substrate), the
mass piece −2M/r is odd (the perspectival artefact). The kink that reads as a curvature
singularity is the chart's, not the manifold's. It dissolves the moment the construction is
allowed to continue in its natural **imaginary** direction: the slicing curve runs out to the
throat seam and continues analytically (sin θ → cosh ψ, θ → π/2+iψ), and the underlying de
Sitter substrate is smooth (C^∞) across the locus the chart labels r=0 — the continuity runs
through the equatorial seam at X=α, never through the perspectival r=0. The singularity is real
*in the perspectival reading* and absent *from the invariant geometry*: a built feature of the
vantage, not a feature of the world. (Formal account: P3 §sweep/§lap; the even/odd split, P9's
perspectival-singularity remark.)

### A3 — The dynamics and the perturbations, conceptually, with the tensions resolved
Take the one free parameter the theory carries and the picture closes. The expansion **rate** is
fixed by Λ alone — radiation plays no role in it at any epoch — so the present Hubble rate is not
a free parameter but a reading of the one Λ-set geometry at our cosmic epoch. The **Hubble
tension** then dissolves: there is no second H₀ to reconcile; the directly measured rate is the
geometry's, and the lower value the CMB infers rests on a radiation-governed sound horizon this
construction does not share. The matter density is not an independent amplitude but a **clock
reading** — Ω_m records the epoch τ̃₀ at which we observe — so the coincidence problem becomes
the observation that we exist at a time of order the geometry's one timescale. The **acoustic
scale** is reproduced at the *directly* measured H₀ by a single early-universe parameter (the
plasma-onset redshift z_onset, the structural analogue of η): a one-parameter accommodation, not
a tuned fit and not a parameter-free prediction — the load-bearing, falsifiable claim being the
prior one, that radiation carries no term in the rate. And the **perturbations** live on the
layer: gravitational waves are perturbations of h_ij(t) returning the standard graviton in the
linear limit, and the scalar/CMB sector is the same — the de Sitter substrate determines the
*structure* (a closed-S³ source spectrum, its discreteness a candidate large-angle/low-ℓ
signature) while the inherited progenitor handover supplies the *content* (the photon–baryon
plasma that carries the acoustic peaks). The early-time/large-angle regime is where the model is
testable and where it parts from the standard radiation-governed picture.

### A4 — The forward pointer
The full formal development of this cosmological theory — the derivation of the expansion law
from the SdS geometry, the canonical structure, the dynamics of the bend, and the perturbation
spectrum — is carried by the companion arc [P10–P12]. What this paper establishes is the core
the development stands on; the development itself, and the detailed confrontation with data, is
the work of that arc. *(Cite the arc papers; this is the destination — Part B.)*

---

## PART B — The first part of the cosmological theory's formal development  *(the destination; the live roadmap)*

### B0 — Starting point: the SdS metric read cosmologically, and the reassignment
The vacuum solution of R_{μν}=Λg_{μν} with a localized source is Schwarzschild–de Sitter
(`eq:SdS-static`); its metric function f(r)=1−2M/r−r²/α² (α=√(3/Λ)) has the cosmological regime
**ΛG²M²/c⁴ ≥ 1/9**, where the areal radius r is **timelike** and the 3-spheres of constant r are
the spatial slices. The reassignment of §A1 selects, by the limiting causal structure of
collapse (the orientation is tangent, not transverse, to the horizon), the **Nariai** boundary
ΛG²M²/c⁴=1/9 (`eq:Nariai-condition`), M=c²/(3√Λ G) (`eq:Nariai-mass`), where the two positive
horizons merge at areal radius α/√3. The geometric selection (Nariai = the fixed point of the
slicing curve's root-exchange involution, the maximal mass any slicing of a given de Sitter
geometry can carry) is P3's; the cosmology is the third member of one slicing-curve structure,
beside de Sitter and Schwarzschild.

> **Scale discipline (carried from REACH_PLAN §1d, P9 §481).** Three Λ-set scales stay distinct:
> the de Sitter / throat 3-sphere *size* α=√(3/Λ); the merged-horizon areal radius α/√3 (where
> the Nariai cosmology is *seeded*); the areal-radius *amplitude* 2^{1/3}/√Λ (≈0.73α, the
> coefficient of sinh^{2/3}). Do not conflate.

### B1 — From the SdS metric to the proper-frame sinh^{2/3} cosmology  *(the Janzen2015 derivation, DESCRIBED — how we get from A to B)*

*This is the load-bearing derivation P9 currently reaches via eq `SdS-fundamental` + a bare
citation. It must be **described**, not citation-dropped. Source of the steps:
`resources/JanzenFQXi2012.tex` §`sec_CSdSCS` (Janzen 2015), whose result eq `SdS_proper`/`z_SdS`
the development reproduces. Written here in fresh exposition (the original is Daryl's own essay;
the corpus version explains the logic afresh and better, and does not reuse its prose).*

The derivation moves from the static SdS line element to the proper frame of the fundamental
observers in five logical steps.

**(1) The geodesic energy and the radial equation of motion.** For a timelike radial geodesic
the SdS Lagrangian is independent of the coordinate t, so the associated momentum is conserved;
call it E (`eq:E`). Eliminating dt/dτ in favour of E in the normalization condition L=−1
(`eq:L_timelike`) gives a single first-order radial equation, (dr/dτ)² = E² − V_eff(r), with the
effective potential V_eff(r)=(r−2M−Λr³/3)/r (`eq:rtau`,`eq:V_eff`) — formally a unit-mass energy
equation, conserved energy minus potential.

**(2) Selecting the fundamental rest frame: E=1.** A preferred congruence is the set of
worldlines whose motion in r is produced *purely by the field*, i.e. those that would come to
rest exactly where the potential is trivial (V_eff≡1, the line element reducing to Minkowski).
From the radial equation this is precisely E²=1; the positive root E=1 is the worldline whose
proper time runs forward with t in the absence of gravity. E=1 is therefore the specific energy
of a test particle "at rest with respect to the vanishing of the potential" — the fundamental
observers; E≠1 carries uniform momentum relative to them. *(This is the physically load-bearing
choice — the rest frame is defined by the field, not posited.)*

**(3) The single-worldline scale factor.** Normalizing all lengths by the cosmic scale √(3/Λ)
(equivalently striking Λ/3 from the cubic term), the E=1 equations give ∂_τt=r/(r−2M−r³)
(`eq:tdot`) and (∂_τr)²=(2M+r³)/r (`eq:rdot`). Integrating the latter (substitute u²=2M+r³)
yields τ as a closed logarithm of r (`eq:t_int`); inverting, the areal radius along one
fundamental worldline grows as r(τ) ∝ sinh^{2/3}(3τ/2) (`eq:scalefac_scaleinvtau`), with Hubble
rate H=ṙ/r=coth(3τ/2) (`eq:Hubble`) approaching the de Sitter value on a timescale of order the
cosmic scale.

**(4) Building the congruence: the comoving coordinate χ and r(τ,χ).** The lower limit of the
τ-integral is an integration constant per worldline — a spatial label r(0). Choosing the label
so that r(0)=(2M)^{1/3} sinh^{2/3}(3χ/2) (`eq:r(0)`, valid for M≠0) makes the integral solve
*explicitly*: the areal radius across the whole congruence is r(τ,χ)=(2M)^{1/3}
sinh^{2/3}((3/2)[τ+χ]) (`eq:r(tau,chi)`) — it depends on τ and χ only through their **sum**, and
∂_χr=∂_τr (`eq:rprime`). *(This is Lemaître's 1949 form; his argument carried a √3 error in the
scale, corrected here.)*

**(5) The orthogonal proper frame and the line element.** The coordinate transformation t(τ,χ)
is fixed by requiring the comoving spatial coordinate to be **orthogonal to proper time**,
g_χτ=0 (`eq:g_chit`); a one-line computation shows this forces the integration function
F(χ)=χ. The remaining components follow: the proper-frame condition gives g_ττ=−1 (`eq:g_tt`),
and direct calculation gives g_χχ=(∂_χr)² (`eq:g_chichi`), the angular part r²dΩ² already
orthogonal to τ. The result is the **proper-frame line element**
> ds² = −dτ² + (∂_χr)² dχ² + r² dΩ²   (`eq:SdS_proper` ≡ P9 `eq:SdS-fundamental`).

**The cosmic time and the redshift.** By Weyl's principle the fundamental worldlines issue from
a common origin and evolve together, so the constant-cosmic-time slices are those of constant
r — i.e. constant **τ̃ ≡ τ+χ**. The scale factor is then r(τ̃)=(2M)^{1/3} sinh^{2/3}(3τ̃/2)
(`eq:SdS_scalefac`), *exactly* the flat-ΛCDM form, and the redshift is 1+z=r(τ̃₀)/r(τ̃_e)
(`eq:z_SdS`). The constant-τ̃ slices lie at 45° in the (τ,χ)-plane — **not** synchronous with the
fundamental geodesics: the cosmology is non-synchronous, exactly the structure FLRW's
hypersurface-orthogonality assumption forbids.

**What the derivation establishes conceptually.** Of FLRW's kinematic assumptions — (i) a
geodesic congruence, (ii) hypersurface orthogonality, (iii) homogeneity, (iv) isotropy —
assumption (i) is kept and (ii) is *dropped*: the SdS cosmology is homogeneous (the constant-τ̃
slices are coordinate-independent 3-spheres) and observationally isotropic, yet its simultaneity
is not synchronous even in the fundamental rest frame. Lemaître's reading of the constant-τ
Euclidean slices as "space ejected from the r=0 singularity" is causally incoherent and is
*not* the physics; the r=0 of the chart is the perspectival mass-singularity (§A2), off the
continuation. *(The two slicings: constant-τ Euclidean/flat — the observable rest-frame slice,
Ω_k=0 — vs. constant-τ̃ closed-S³ — the cosmological/source slice. Both on one manifold.)*

### B2 — The amplitude, the rate, and the resolution of the tensions  *(formal)*
With M fixed at Nariai, both factors of the expansion law are set by Λ: the rate
½√(3Λ)c is the flat-ΛCDM late-time rate, and the amplitude (6GM/Λc²)^{1/3}=2^{1/3}/√Λ
(`eq:nariai-amplitude`) is the areal-radius scale. The Friedmann equation the sinh^{2/3} law
satisfies, H²=(Λc²/3)coth²(½√(3Λ)cτ̃)=⅓(8πGρ+Λc²) (`eq:friedmann-coth`), makes
Ω_m/Ω_Λ=csch²(½√(3Λ)cτ̃) (`eq:omega-ratio`) — a clock, not a free density. *(Develop here: the
Hubble-tension dissolution; the acoustic scale as the one-parameter z_onset accommodation at the
directly-measured H₀; the structure/content split — pressureless seam-continuation matter vs. the
inherited photon–baryon plasma; ρ_r/ρ_m≈2 as η's analogue, held as P8's falsifiable programme.
This is the formal home of P9's current Hubble-tension remark.)*

### B3 — Forward hooks into the arc
- **P10 (canonical_time):** the deparametrized true Hamiltonian on this foliation; the graviton
  tower; the de Sitter-horizon thermal state. *(The canonical structure of the layer's advance.)*
- **P11 (dynamics):** why the cut bends — the matter density as the bend of the spatial cut,
  the confined Gowdy–dS wave, the onset of free radiation at the wall.
- **P12 (scalar perturbations — THE LIVE REACH):** the scalar/CMB sector. The closed-S³ source
  spectrum (structure) and the inherited content; the low-ℓ discreteness transfer through the
  reassigned-null photon congruence to the observable sky (distance D_M). **This roadmap is
  worked against the reach** (`REACH_PLAN_perturbation-projection.md`): every result the reach
  grounds (the two lengths, the scales of §B0, the projection channel) feeds back here.

---

## P12 POSITIONING — how Part B opens P12 and the perturbation sector closes it  *(mapped against the full P12 read, r513)*

**Recast P12 structure** (`scalar_perturbations_paper.tex`, 237 ll. read whole at source):
1. **§intro** (tensor→scalar; the decomposition thesis "substrate determines structure,
   progenitor supplies content, the seam assigns each its job"; the chimera/Hubble guard).
   *KEEP* — lightly repoint so it opens *into* the now-included formal development rather than
   citing P9 out to it.
2. **THE OPENING = Part B** — the formal cosmological-theory development. **It replaces/absorbs
   the thin §`sec:background`** (today just `eq:rate` + `prop:subhorizon` leaning on P9). The
   rate `eq:rate` and `prop:subhorizon` (acoustic modes sub-horizon at z_seam≈6850) *stay*,
   folded in as the setup the perturbations build on. This is "the opening that P12 closes."
3. **THE CLOSE = the existing perturbation development** (these *complete* the cosmological
   theory): §coherence [argued], §amplitude [established], §throat [established geom + the
   throat-tower interpretation, with its load-bearing guard], §largescale [flat slice
   established; low-ℓ floor argued], §transmission [established — the decisive proof].
4. **§predictions, §scope** — KEEP.

**Straw man crossed (do not derail on it).** The §largescale flat-sky floor
`eq:lowell` ℓ_L≃√(L(L+2))·D_C/r₀ → ℓ₂≈7.8 is a **placeholder, already self-flagged in-paper**
("order-level placeholder, not a pinned multipole"). The closed-S³ **hyperspherical** transfer
(degree-L feeds ℓ≤L, so L=2 feeds the *quadrupole* ℓ=2) is what the geometry requires; the reach
**replaces** the flat-sky estimate, never defends ℓ₂≈8. **Kept sharp, by contrast** (these
*prevent* the derail, not straw men): the chimera guard (§intro l.84 — standard radiation-governed
sound horizon on the radiation-free rate = an artifact of neither model) and the read-the-
Friedmann-leftward guard (§background l.96 — the rate is set; a perturbing fluid's energy is
content the set rate carries, not a term that alters it).

**Reach markers (maturity, at source).**
- *Established (verified, receipts in `computations/perturbation_verify/`):* the transmission
  dichotomy (`prop:transmission`/`prop:transmit`), the amplitude floor (`prop:amplitude`),
  the throat geometry (`prop:throat`), the flat slice (`prop:flat`), `prop:subhorizon`. **Do not
  reopen.**
- *Argued [reach]:* the null-seam coherence mechanism (§coherence — characteristic data ⇒ one
  phase per mode; sufficiency unproven); the low-ℓ floor's scale (`eq:lowell`, leading-order).
- *Open (named):* coherence sufficiency through the full transfer; **the exact large-angle shape
  via the non-synchronous photon transfer of the closed-dS mode functions — "the principal
  unbuilt element," = REACH_PLAN §5 Steps 1–4** (the reach proper); the progenitor spectrum
  n_s, A_s (inherited, matter-sector — P5/P6).

---
- **Enrich incrementally.** As each piece of the reach/theory is worked, update the matching
  Part-B subsection (and Part A's conceptual sketch if the shape sharpens). Keep it the durable
  current-state description — always referenceable, polished as we go.
- **Coupling to the reach plan.** The reach's P9 GO-TOs (eq `SdS-fundamental`/`nariai-amplitude`,
  `thm:null-boundary`, the acoustic remark) point at P9's formal section *today*; when the P9
  recast executes, they repoint here / into the arc. Keep the two in step.
- **Stated for reversal; forward-pin available.** Proceeding confident the separation sticks; if
  ever in doubt, drop a forward-pin to re-ask the structuring question rather than unwinding
  silently. **Positioning was done (r513); the core cut is now EXECUTED (r514).** Both papers
  compile clean: P12 opens with Part B (the formal cosmological-theory development, the Janzen2015
  derivation described), the perturbation sections close it; P9 sheds the theory-development layer
  and gains the cranked-up conceptual reach + forward-pointer (`\subsubsection{What this cosmology
  opens onto}`). **Entanglement finding that refined the cut:** `eq:SdS-fundamental` and
  `eq:r-SdS-solution` are load-bearing for `thm:null-boundary` (P9 ll. 661/665), so the geometric
  result *stays* in P9; only the overshadowing theory layer (exact-ΛCDM-recovery, §amplitude,
  isotropy) moved. P9's abstract stays accurate (P9 still constructs the SdS cosmology); the GO-TOs
  above repoint into the arc (P12 §amplitude now carries the formal rate/amplitude development; the
  banked Hubble remark stays in P9 §687–691). **Finishing stage (lighter than feared):** optional
  synthesis polish in P9, a deeper Part A crank if wanted, the pre-existing missing `dS-SdS.png`.
