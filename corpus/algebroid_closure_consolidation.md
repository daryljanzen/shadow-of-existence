# The algebroid is a built object — GR's constraint algebra as the substrate's symmetric-space structure
*Corpus consolidation note (bracket closure + the isotropy stratification, Moves 6–7, r211,
2026-06-12). The central test of the action Lie algebroid $\mathfrak{so}(5,1)\ltimes\mathcal{C}$, and the
stratification that completes the "built object" criteria. Receipts: `scripts/adm_so51_1.py` (closure),
`scripts/adm_strata_1.py` (stratification), `scripts/adm3.py` (discrete). Not one of the 10 papers — a
corpus support/spine note, like the anchor and Gowdy–dS consolidations. All receipts clean-zero (sympy).
Tags: [established]/[computed]/[reading]/[reach].*

## The claim
$\mathfrak{so}(5,1)\ltimes\mathcal{C}$ is the home of GR's constraint algebra: the substrate isometry
acts on the space of cuts, and the anchor (cut-deformation → constraint) is a homomorphism into the
hypersurface-deformation (Dirac) algebra. The test: does the cut-deformation bracket close, and does the
anchor reproduce the HDA?

## 1. The substrate is the symmetric space $\mathrm{dS}_5 = SO(5,1)/SO(4,1)$
The cuts are leaves of the substrate. At the maximally symmetric (vacuum) cut, the subalgebra of
$\mathfrak{so}(5,1)$ fixing the leaf is $\mathfrak{h}=\mathfrak{so}(4,1)$ — the leaf's own isometry,
10-dimensional — and the cut-*deforming* directions are the coset $\mathfrak{m}$, 5-dimensional, the
normal that carries one leaf to the next. $\mathfrak{so}(5,1)=\mathfrak{h}\oplus\mathfrak{m}$.
The construction's "isotropy = the subalgebra fixing a cut" is exactly $\mathfrak{h}$; the cut-deformations
are exactly $\mathfrak{m}$. **[established geometry; the identification is the construction]**

## 2. The cut-deformation bracket closes **[computed, `adm_so51_1.py`]**
The three symmetric-space inclusions hold, clean: $[\mathfrak{h},\mathfrak{h}]\subset\mathfrak{h}$,
$[\mathfrak{h},\mathfrak{m}]\subset\mathfrak{m}$, and the load-bearing
$[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$ — the cut-deformations close back into the isotropy.
$\mathfrak{m}$ is not a subalgebra (the bracket genuinely returns to $\mathfrak{h}$); e.g.
$[M_{05},M_{15}]=-M_{01}$, two coset deformations bracketing to a single isotropy generator, the sign
the substrate curvature.

## 3. The anchor is a homomorphism — the symmetric-space split is the HDA grading
Identify $\mathfrak{m}\leftrightarrow\mathcal{H}_\perp$ (the normal deformation = the Hamiltonian
constraint) and $\mathfrak{h}\leftrightarrow\mathcal{H}_a$ (the tangential = the momentum/diffeo
constraint). The symmetric-space brackets are the Dirac algebra, term for term:

| symmetric space | hypersurface-deformation algebra |
|---|---|
| $[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$ | $\{\mathcal{H}_\perp,\mathcal{H}_\perp\}\sim\mathcal{H}_a$ |
| $[\mathfrak{h},\mathfrak{m}]\subset\mathfrak{m}$ | $\{\mathcal{H}_a,\mathcal{H}_\perp\}\sim\mathcal{H}_\perp$ |
| $[\mathfrak{h},\mathfrak{h}]\subset\mathfrak{h}$ | $\{\mathcal{H}_a,\mathcal{H}_b\}\sim\mathcal{H}_c$ |

## 4. The structure-function obstruction is the substrate's metric
The HDA's $\{\mathcal{H}_\perp,\mathcal{H}_\perp\}\sim\varepsilon\,h^{ab}\mathcal{H}_b$ carries a structure
*function* $h^{ab}$, not a constant — the feature that makes the algebra a Lie *algebroid*, and the
canonical root of the problem of time. It is the $[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$ bracket
read with the coset metric, which on the reduction is identified with $h^{ab}$ (the coset metric is the
Lorentzian $5$-dim form, signature $(1,4)$ — Killing form $\propto\mathrm{diag}(+,-,-,-,-)$,
`so51_coset_signature.py` — its indefinite sign the problem-of-time $\varepsilon$, not a naive equality with
the Riemannian $3$-metric): **constant** at the symmetric cut (so $\mathfrak{so}(5,1)$ is a
genuine Lie algebra there), **varying** as the cut moves over $\mathcal{C}$ (so the genuine algebroid).
$\varepsilon$ is the signature carried by $\sigma$, the vantage involution (`adm3.py`: exterior Lorentzian
/ interior Euclidean — $\varepsilon\to-\varepsilon$). So the problem-of-time obstruction is the
base-dependence of the substrate's symmetric-space metric — and read on the physically real foliation
(P8, `canonical_time.tex`), it deparametrizes to a true Hamiltonian.

## 5. The discrete skeleton inside (`adm3.py`)
$\sigma$ (vantage, the signature flip, order 2) and $\tau$ (the sky-angle triality on the three cubic
roots, order 3) generate $S_3=\mathrm{Weyl}(A_2)$ acting on the cubic's roots; the permutation rep is
trivial $\oplus$ standard-2d. This is the discrete stabilizer skeleton (Paper 4) sitting inside the
continuous $\mathfrak{so}(5,1)$ — the static/dynamic complementarity as one object's discrete and
continuous structure. **[computed (the $S_3$ action, the rep); the $A_2$ root structure geometrically
grounded since the 2012 thesis fundamental ellipse]**

## 6. The isotropy stratification and the singular-strata coincidence (Move 7)
The isotropy — the cut-fixing subalgebra of $\mathfrak{so}(5,1)$ — varies over $\mathcal{C}$, and its
strata are P6's range/Petrov classes. This is the base-variation of the structure functions that §2–4
verified only at the symmetric cut: as the cut moves, the cut-fixing subalgebra changes and the
algebroid's structure functions change with it.

| stratum | isotropy | dim |
|---|---|---|
| Type O — de Sitter / FLRW (symmetric vacuum cut) | $\mathfrak{so}(4,1)$ | 10 |
| Type D — Schwarzschild–de Sitter | $\mathbb{R}_t\times SO(3)$ | 4 |
| Type D — **Nariai** ($\Lambda M^2=1/9$) | $SO(2,1)\times SO(3)$ | **6 (jump up)** |
| Type D — Kerr–de Sitter | $\mathbb{R}\times SO(2)$ (+ Killing tensor) | 2 |
| Type I — Bianchi I (homogeneous) | 3 spatial KV | 3 |
| Type I — Zipoy–Voorhees / Weyl | $\mathbb{R}\times SO(2)$ | 2 |
| **wall** — Type N (plane wave) | no continuous isometry | 0 |

The strata boundaries are where the isotropy jumps, and they coincide with the metric-singular loci:
- **Inner (computed, `adm_strata_1.py`):** the SdS horizon cubic $r^3-\alpha^2 r+2M\alpha^2$ has
  discriminant $-4\alpha^4(27M^2-\alpha^2)$, vanishing at $\Lambda M^2=1/9$ — the double root
  $r_N=1/\sqrt\Lambda$, two horizons merging, the Nariai seam. At that locus the geometry is
  $\mathrm{dS}_2\times S^2$ (both factors constant-curvature, Ricci scalar $2/b^2$), isometry
  $SO(2,1)\times SO(3)$, so the isotropy jumps $4\to6$. **The isotropy-jump locus is the
  metric-degenerate locus.** [computed]
- **Outer (P6 + Move 9):** the wall is isotropy $\to 0$ — Type N, the onset of free gravitational
  radiation, the loss of all continuous symmetry. Here the isotropy-stratification boundary and the
  metric-singular loci **diverge**: the wall is an isotropy/radiative boundary but **not a metric
  singularity** (Move 9, `adm_wall_1.py`, `wall_ppwave_check.py`). A metric singularity in P1's sense is
  a collapse of the metric's *measure* — a null hypersurface along whose generators the spatial extent
  contracts to zero ($\Delta s^2=0\wedge\Delta x=0\Rightarrow\Delta\tau=0$); a Killing horizon is the worked
  sufficient case, not the definition. The wall, a Type-N plane wave, has a non-degenerate metric ($\det g=-1$;
  no measure-collapse, so not the finite species) and vanishing curvature invariants (VSI; not the infinite
  species), so it is neither. Its own covariantly-constant null Killing vector is null *everywhere* (no
  non-null-to-null transition, no Killing horizon, no measure-collapse). The "isotropy $0$" that marks it is
  the cut-fixing *substrate* isotropy — coinciding with a geometry's own isometry on the symmetry-reducible
  sector, diverging here from the Type-N geometry's own large isometry — so the wall is no metric singularity
  by the measure criterion, not for want of a Killing field. So the wall is the generative boundary
  (where sweep-generation hands off to ordinary evolution), not a cosmogenesis seam. **[computed]**
- The **NBC cosmogenesis horizon** (P7) and the **Riemannian$\leftrightarrow$Lorentzian seam** are the
  vantage/reassignment loci — $\sigma$'s signature flip (§5) — the discrete-operation boundaries, where
  the cut's causal character degenerates rather than its continuous symmetry.

So the isotropy-stratification boundaries and the corpus's **metric-singular** seams coincide at the
**inner** end (Nariai = the double-root Killing horizon = the isotropy jump $4\to6$) but **diverge at the
outer end**: the wall is a singular stratum of the *isotropy* kind that is **not** a metric singularity
(Move 9). The cosmogenesis seams — where a clock re-founds — are the Killing-horizon metric singularities
(the NBC horizon; Nariai); the wall is the generative/radiative boundary. With this, the four
"built object" criteria are met: $\mathcal{C}$ defined (Move 4), anchor complete (Move 5), bracket
closes (Move 6), and the isotropy stratification reproduces the range/Petrov classes (Move 7), with its
boundaries coinciding with the metric-singular seams at the inner end and diverging at the wall. **[computed: the
Nariai inner coincidence + the strata dimensions + the wall's non-metric-singular species (Move 9) + the
per-stratum subalgebra grading (`f1_per_stratum_subalgebra_id.py`, `f1_homomorphism_consolidation.md` §2:
symmetric only at {Type O, Nariai}, the leak elsewhere the algebroid connection); reading:
the NBC/seam discrete-locus unification]**

## 7. The discrete skeleton at the strata (Move 11)
The continuous face $\mathfrak{so}(5,1)$ runs the flow through the symmetry-reducible sector (§2–6). The
discrete face — the $S_3=\langle\sigma,\tau\rangle$ of the horizon cubic (P4, `adm3.py`) — acts at the
strata, but as a **set of distinct operations each anchored at its stratum**, not one unified action: P4
keeps the operations distinct, and Move 11 confirms that can-return (they stay distinct). The cubic's
root structure (the $A_2$, the fundamental ellipse) is what organizes them:

| stratum | discrete operation anchored there |
|---|---|
| Nariai (inner, double root, $\Lambda M^2=1/9$) | the $S_3$ **transposition fixed point** — two of the three roots collide; discriminant $-(3r_0^2-4)(3r_0^2-1)^2=0$ at $r_0^2=1/3$ (physical Nariai, $M>0$) and $r_0^2=4/3$ (the $M<0$ conjugate). [computed, `adm_skeleton_strata_1.py`] |
| NBC cosmogenesis horizon | the **reassignment** involution — null↔timelike on the degenerating Killing field's freed direction (P7; Move 9). |
| Riemann$\leftrightarrow$Lorentz seam | $\sigma$ — the vantage **signature flip** ($\theta\mapsto\pi/2+i\psi$; `adm3.py`, P3 §478). |
| the wall (isotropy 0, Type N) | **none** — no colliding cubic roots, no degenerating Killing field, no measure-collapse (Move 9); the discrete skeleton does not reach it, and past it is pure continuous evolution. |

So "the discrete skeleton acts at the strata" holds in the **bounded** form: the strata are the
fixed-point/locus set of the distinct discrete operations, organized by the cubic root structure — **not**
one unified discrete action, and the wall has none. This is the continuous/discrete complementarity made
precise: the continuous face is the flow between strata, the discrete face the boundary operations, each
marking its stratum; the wall is the lone boundary that is purely continuous (Move 9), consistent with
its being no metric singularity. **[computed: Nariai = the $S_3$ transposition fixed point (double root =
discriminant zero); established: the reassignment at the NBC horizon (P7/Move 9), $\sigma$ at the seam
(adm3/P3), the wall has none (Move 9); reading: the organizing claim (distinct-but-anchored). NOT
asserted: any unification into one discrete action; any continuous $\mathfrak{su}(3)$ — the $A_2$ root
structure is the skeleton, the leap to $\mathfrak{su}(3)$ stays Move 13.]**

## 8. Move 13, first bite — is the $A_2$ resonance the $\mathfrak{su}(3)$ fingerprint? Necessary-not-sufficient; do-not-assert held  **[computed group-theory floor + the established skeleton → the correctly-posed verdict]**
*(c17, r277, 2026-06-16. `scripts/move13_su3_fingerprint_test.py`. The prerequisite root/isotropy data is built
(Moves 6–7–11); this poses Move 13's test **correctly** — the manufactured-wall caution is live: the retracted
rung-4 test checked $\mathfrak{su}(3)\subset\mathfrak{so}(4,1)$, the wrong group, a strawman. The right
necessary condition is $\mathfrak{su}(3)\subset$ the substrate's **compact** isometry.)*

- **The skeleton is present (necessary piece, established).** The horizon cubic $r^3-\alpha^2 r+2M\alpha^2$ has
  no $r^2$ term, so its three roots sum to zero — a **Cartan (traceless) element of $\mathfrak{su}(3)$** — and
  $\sigma,\tau$ generate $S_3=\mathrm{Weyl}(A_2)$ permuting them (§5). So the cubic supplies the $\mathfrak{su}(3)$
  **Cartan + Weyl skeleton**, geometrically grounded (the 2012 fundamental ellipse). The *necessary* condition
  for the resonance is met.
- **The sufficient step fails on $\mathrm{dS}_5$ (computed floor).** For the skeleton to be the shadow of a
  *continuous* $\mathfrak{su}(3)$ realized as a geometric isometry, $\mathfrak{su}(3)$ must sit in the substrate's
  compact isometry. $SU(3)$'s smallest faithful real representation is **6-dimensional** (the fundamental $\mathbf{3}$
  is complex; the adjoint $\mathbf{8}$ has kernel $Z_3$), so $SU(3)\subset SO(6)$ and $SU(3)\not\subset SO(5)$.
  The established substrate is $\mathrm{dS}_5=SO(5,1)/SO(4,1)$, compact isometry $SO(5)$ — and a compact
  $\mathfrak{su}(3)$ can only embed in a maximal compact subalgebra. So **$\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$:
  no continuous $\mathfrak{su}(3)$ geometric isometry exists on $\mathrm{dS}_5$.**
- **Verdict (necessary-not-sufficient; do-not-assert held).** On the established $\mathrm{dS}_5$ substrate the
  $A_2$ resonance is the **discrete $\mathrm{Weyl}(A_2)=S_3$ shadow only** — **gravity-minimal**, colour a shadow.
  A continuous (gauge-capable) $\mathfrak{su}(3)$ requires the substrate to rise to $\mathrm{dS}_6/M^7$
  ($SO(6)\supset SU(3)$); the resonance supplies the skeleton but does **not force** that rise. So the
  $\mathrm{dS}_5$-vs-$\mathrm{dS}_6$ horn (Move 4's second axis) is **not decided by the resonance** — it stays
  open, to be decided by *independent* grounds for $\mathrm{dS}_6$, if any. $\mathfrak{su}(3)$ is **not asserted**;
  it is also **not refuted** (the skeleton is real, and dS₆ would realize it) — it is *correctly located*: the
  resonance is necessary, not sufficient, and silent on the dimension. **[computed: the floor + the skeleton;
  reading: the correctly-posed verdict. The continuous-$\mathfrak{su}(3)$ leap and the dS₆ rise remain
  do-not-assert.]**

## 9. Scope
- **Computed:** the symmetric-space split and closure at the symmetric cut; the bracket-pattern/grading
  match to the HDA; $\mathfrak{so}(5,1)$ a genuine Lie algebra at the symmetric cut; the $S_3$ discrete
  structure; **and the structure-function variation across $\mathcal{C}$ per-stratum**
  (`f1_per_stratum_subalgebra_id.py`, `f1_homomorphism_consolidation.md`): the symmetric grading survives
  at {Type O, Nariai} only, and the $[\mathfrak{m},\mathfrak{m}]$ leak into $\mathfrak{m}$ at every generic
  stratum **is** the algebroid connection (the transverse-modulus variation).
- **Reading (the natural extension, to firm):** the full field-theoretic homomorphism — the **smeared,
  infinite-dim** HDA beyond the finite $\mathfrak{so}(5,1)$ pattern, and whether it closes **intrinsically
  through P3's slicing curve** for matter (the literal embedding route being dead, SdS class 2). **[reading]**
- **The sector:** $\mathfrak{so}(5,1)$ is finite (15-dim); the full HDA is infinite-dimensional. Closure
  is on the **symmetry-reducible sector** — the cuts reachable by substrate isometries, the corpus's
  range/Petrov sector. The wall (isotropy $\to 0$, Move 7) is the boundary of the action algebroid; past
  it the free transverse degrees of freedom — the graviton's two polarizations — take over. The algebroid
  is the home of the symmetry-reducible sector; the wall is where it hands off to dynamics (Move 8).
  **[established for the sector; the inhomogeneous/dynamical extension beyond the wall is the dynamics frontier]**

## Receipts (`scripts/`, clean)
- `adm_so51_1.py` — $\mathfrak{so}(5,1)=\mathfrak{h}\oplus\mathfrak{m}$; the three inclusions;
  $[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$; the anchor identification and the HDA pattern; the curvature sign.
- `adm3.py` — the HDA is an algebroid (structure function $\varepsilon h^{ab}$); $\sigma$ = the signature
  flip $\varepsilon\to-\varepsilon$; $\langle\sigma,\tau\rangle=S_3$ on the cubic roots, trivial $\oplus$ standard-2d.
- `adm_strata_1.py` — the SdS cubic discriminant $\to\Lambda M^2=1/9$ (the Nariai double root); the Nariai
  limit $\mathrm{dS}_2\times S^2$ constant-curvature → isotropy jump $4\to6$ at the metric-degenerate locus (Move 7).
- `adm_wall_1.py` + `wall_ppwave_check.py` — the wall's species (Move 9): the horizon is a Killing horizon
  $|\xi|^2=-f=0$ (the measure-collapse hypotheses met) with finite Kretschmann $48M^2/r^6+24/\alpha^4$
  (finite-curvature metric singularity); the wall (isotropy 0, Type N / Brinkmann pp-wave) has $\det g=-1$
  (no measure-collapse, not the finite species) and all curvature invariants zero (VSI, not the infinite
  species) → not a metric singularity by P1's measure criterion (branch c); its own null Killing vector is
  null everywhere (no Killing horizon).
- `adm_skeleton_strata_1.py` — the discrete skeleton at the strata (Move 11): the three roots sum to zero
  ($A_2$); the discriminant $-(3r_0^2-4)(3r_0^2-1)^2$ vanishes at $r_0^2=1/3$ (physical Nariai, $M>0$) and
  $4/3$ ($M<0$ conjugate) → Nariai is the $S_3$
  transposition fixed point (double root). The distinct-but-anchored picture.
