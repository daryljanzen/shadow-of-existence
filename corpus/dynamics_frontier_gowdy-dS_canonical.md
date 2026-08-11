# Dynamics frontier — the polarized Gowdy–dS field-theoretic canonical model
*Corpus consolidation note (the spine of the dynamics paper, Move 8). Consolidated r191 (2026-06-12)
from the recovered r167-over-excision material; re-verified at source Move 2 (all receipts clean-zero,
sympy 1.14.0). Not one of the 10 papers — a corpus support/spine note, like the singularity-taxonomy
consolidation. Tags: [established]/[computed]/[reading]/[reach].*

## Why this exists
The corpus's canonical result (P8, `canonical_time.tex`) realizes CR's deparametrized **true
Hamiltonian** — absolute foliation → $i\partial_\tau\Psi=\hat H_{\mathrm{phys}}\Psi$, unitary
cosmic-time evolution reproducing flat ΛCDM — only in a flat-FLRW **minisuperspace** with a dust
clock, and flags it honestly as a toy with "no propagating DOF," naming "the transverse-traceless
shear of the evolving layer … up to the wall" as the geometric content and "the full … canonical
quantization" as "the natural next object." **This model is
that next object, in the polarized Gowdy–dS sector**: the first *field-theoretic* (midisuperspace)
canonical model of the programme, with a real propagating graviton. **[established — the gap P8 names]**
*(Update r250: P8 has since carried out that next object in the **cosmological** sector too — `canonical_time.tex` §lock, the closed-$S^3$ graviton tower deparametrized on cosmic time, r246–r250; this Gowdy–dS model is its companion in the symmetry-reducible sector. The two are the field-theoretic lift in their respective sectors.)*

## 1. The model
Polarized Gowdy–dS edge, metric
$$ds^2 = e^{2(\gamma-\psi)}(-dt^2+dz^2) + e^{2\psi}\,dx^2 + R^2 e^{-2\psi}\,dy^2,$$
with $\psi(t,z)$ the propagating graviton (the leaf's TT shear), $R(t,z)$ the Λ-driven expanding
orbit-area (the area/clock sector), $\gamma(t,z)$ the conformal factor; lapse $N=e^{\gamma-\psi}$.
The vacuum-Λ field equations $G_{ab}+\Lambda g_{ab}=0$ are **exactly** the four named equations plus
the γ-equation (verified, all-zero residuals — `scripts/gowdy_ds_canonical_1.py`):
- WAVE $(R\psi_t)_t-(R\psi_z)_z=\Lambda R e^{2(\gamma-\psi)}$ $\;=\;$ $(E_{xx}\text{ core}+R\,\gamma\text{eq})/2$ modulo AREA;
- AREA $R_{tt}-R_{zz}=2\Lambda R e^{2(\gamma-\psi)}$ $\;=\;(E_{tt}-E_{zz})R$;
- ENERGY $2(R_t\gamma_t+R_z\gamma_z)-(R_{tt}+R_{zz})=2R(\psi_t^2+\psi_z^2)$ $\;=\;(E_{tt}+E_{zz})R$ (constraint);
- MOMENTUM $R_t\gamma_z+R_z\gamma_t-R_{tz}=2R\psi_t\psi_z$ $\;=\;E_{tz}R$ (constraint);
- $\gamma$-eq $\gamma_{tt}-\gamma_{zz}+\psi_t^2-\psi_z^2=\Lambda e^{2(\gamma-\psi)}$ $\;=\;-E_{yy}e^{2\gamma}/R^2$. **[computed]**

## 2. Canonical structure
Momenta $p_\psi=4R\psi_t$ (the graviton), and the **cross-conjugate area/clock sector**
$p_\gamma=-2R_t$, $p_R=-2\gamma_t$. Hamiltonian density
$$\mathcal{H} = \frac{p_\psi^2}{8R} + 2R\,\psi_z^2 \;-\;\tfrac12\,p_\gamma p_R \;-\; 2R_z\gamma_z \;+\; 2\Lambda R\,e^{2(\gamma-\psi)},$$
confirmed by Legendre transform of the reduced first-order Lagrangian (`scripts/gowdy_ds_ham.py`).
The ENERGY and MOMENTUM equations sit exactly as the Hamiltonian and momentum constraints. **[computed]**

## 3. ℋ is a TRUE Hamiltonian (not a frozen constraint)
Hamilton's equations derived directly from $\mathcal{H}$ reproduce the foliation evolution — WAVE,
AREA, and the γ-equation — with clean zeros (`scripts/gowdy_ds_deparam.py`). A frozen constraint would
not. Because the foliation is **absolute** (the lapse $N=e^{\gamma-\psi}$ is the leaf's metrical
advance, not a free multiplier), $\mathcal{H}$ generates a *real* advance: P8's true-Hamiltonian claim,
now realized **with a field in it**. **[computed → reading]**

## 4. Reduced $H_{\mathrm{phys}}$ and where the absolute foliation earns its necessity
(`scripts/gowdy_ds_reduce.py`.)
- **Λ=0:** area-time $R=t$ is consistent ($R$ harmonic); the constraints fix $\gamma$ from $\psi$; the
  reduced physical Hamiltonian $H_{\mathrm{phys}}=\int dz\,[\,p_\psi^2/(8t)+2t\psi_z^2\,]$ generates the
  **Gowdy/Bessel wave equation** $\psi_{tt}+\psi_t/t-\psi_{zz}=0$ (verified). **[computed]**
- **Λ>0 (the CR case):** $R=t$ is **inconsistent** — the Λ source drives $R$ ($R_{tt}-R_{zz}=2\Lambda
  t e^{2(\gamma-\psi)}\neq0$) — so the internal-clock trick fails and the substrate's de Sitter cosmic
  time (the CR absolute foliation) is the natural clock. **This is where the absolute foliation earns
  its necessity, with a propagating field present.** **[computed]**

## 5. The lift to P8 — stated at honest scope
This model is a **second, richer realization of the same canonical structure** P8 established
(absolute foliation → true Hamiltonian → unitary $\tau$-evolution) — the **first with a local
propagating degree of freedom** (the graviton $\psi$). It upgrades the canonical claim from a
homogeneous toy to a model with real local dynamics, and answers, in the polarized Gowdy–dS sector,
the "natural next object" P8 set beyond its scope.

**It is *not* a superspace that literally contains P8's minisuperspace.** P8's $H_{\mathrm{phys}}
=(2\pi/3)p_a^2/a-(\Lambda/8\pi)a^3$ is flat FLRW with a dust clock; this is vacuum-Λ Gowdy with an
area clock and a graviton, on a different spatial topology — and the homogeneous limit of *this* model
($\psi_z=0$) is an anisotropic (Bianchi/Kasner-type) mode in area-time, not flat FLRW. The two are
distinct truncations of one canonical structure, not nested. The lift is "same structure, now with a
field," **not** "the cosmology is the homogeneous sector of the Gowdy model." **[reading; the
non-containment is [established] by the topology/clock mismatch]**

## 6. FORCE vs ADMIT — sharply located, honestly open
Every tractable case so far (Λ=0 Gowdy here; the linearized dS graviton) **ADMITS** a clean, unitary
quantization, but nothing yet **FORCES** quantum structure. Forcing, if real, can only live in **(a)**
the full nonlinear Λ>0 back-reaction, or **(b)** the discrete $S_3/A_2$ skeleton. The root/isotropy data
(b) tests against **is built** (Plan Moves 6–7–11, r210/r211/r214: the $A_2$ root structure, Nariai the
$S_3$ transposition fixed point, the strata) — so the *test* is runnable; what is **do-not-assert** is the
interpretive leap from the discrete $\mathrm{Weyl}(A_2)=S_3$ shadow to a *continuous* $\mathfrak{su}(3)$
geometric isometry (which would force the substrate up to $\mathrm{dS}_6/M^7$), Move 13 — necessary, not
sufficient. No "admits-not-forces" *verdict* is earned; the question is mapped and open. **[reach — the priority
frontier's live question]** *(superseded for both examined routes — see the r326–r327 update below: ADMIT, not
FORCE, on the discrete skeleton and the background sector; the universal stays do-not-assert.)*
*(Update r276: the **classical** side of this is now resolved — see §12. The whole nonlinear Λ>0
back-reaction (a) is ADMIT to the extent establishable, so forcing is isolated to (b), behind the
do-not-assert Move 13. The quantum-forcing question (b) stays open; the classical question is closed.)*
*(Update r301: the all-orders classical edge §13/§14 worked toward is now **externally grounded** — the
propagating-sector nonlinear stability is the established de Sitter nonlinear-stability / cosmic-no-hair
theorem for the vacuum-Λ>0 (Gowdy) class (Friedrich 1986; Andréasson–Ringström 2016; Nariai non-generic
per Beyer 2009), verified at source. Classical (a) closes **ADMIT for generic data**, with the non-generic
**Nariai** branch the boundary — exactly the branch CR isolates via P5. The live do-not-assert edge is now
**(b) alone**. See §14's external-grounding subsection.)*
*(Update r326–r327: the live edge **(b)** is worked to a bounded verdict on both its concrete routes —
**ADMIT, not FORCE** (`MOVE13_FORCE_vs_ADMIT_finding.md`). The criterion is sharpened: ADMIT = sufficiency
(a consistent quantization exists — the lock, P8 §lock); **FORCE = necessity** (no consistent classical
completion), which only a global monodromy/cohomology obstruction forcing an integrality condition on a
physical *period* can supply. **Route (b), discrete $S_3/A_2$ skeleton (r326):** the horizon-cubic cover is
genuinely monodromic — roots split $\pm\sqrt{M_N-M}$ at Nariai, $\mathbb{Z}/2$ local, $S_3$ global deck — but
the lock's physical period (the graviton action, $\mu_n^2=n(n+2)-2$, $a=\alpha\cosh(T/\alpha)$) depends on
$(\alpha,n)$ only, $\partial_M=0$, hence is **monodromy-invariant**; the sole $M$-dependence is the
representational matter $2M/a^3$ (P8 l.177), the gauge/vantage layer. The cover obstructs nothing physical →
no forced integrality → ADMIT; the tower's discreteness is closed-$S^3$ compactness, not a forcing.
**Route (b), background scale-factor sector (r327):** $\Hphys=(2\pi/3)p_a^2/a-(\Lambda/8\pi)a^3$ on
$L^2(0,\infty)$; Liouville $x=2\sqrt{c\,a}$ → $-\partial_x^2$ with $V\sim-x^6$; Weyl gives limit circle at both
ends → a U(2) four-parameter family of self-adjoint extensions (a boundary-condition *choice*, not a unique
forced quantization), and FORCE's prerequisite — classical incompleteness — is absent (CR non-singular, P8
§deparam). Both routes, one root: **CR's cosmology is complete on its own, so the geometry admits quantum
structure but compels none.** The verdict is on the two examined routes; the **universal** "nothing forces
quantum structure" stays **do-not-assert** (an unexamined CR-native route could exist). Consistent with CR's
character: the quantum structure drops out of the absolute foliation (the lock), it is not forced by the
geometry.)*

## 7. Receipts and provenance
`scripts/gowdy_ds_canonical_1.py` (Einstein content, all-zero), `…_ham.py` (ℋ by Legendre),
`…_deparam.py` (Hamilton's eqs reproduce the field eqs, clean), `…_reduce.py` (Gowdy wave eq; Λ>0
inconsistency). The retracted **rung-4 $A_2/\mathfrak{su}(3)$ "test"** was a *manufactured refutation*
(it checked $\mathfrak{su}(3)\subset\mathfrak{so}(4,1)$, a strawman, and mislabelled it) — correctly
dropped; the honest record and the over-excision incident it travelled with are preserved in
`archive/recovered-r167-over-excision/`. **[established]**

## 8. The dynamics argument and the wave's place in the strata (Move 8)
"Why the cut bends," assembled on the now-complete algebroid (Moves 4–7) + the anchor (Move 5) + the
clock (P8) + this spine. **[the placement computed (`scripts/adm_dynamics_1.py`); the argument grounded
in the cited computed pieces; the full nonlinear Λ>0 evolution and the wall handoff (Move 9) remain]**
- The layer **advances by a true Hamiltonian** on the absolute foliation (P8); this model realizes that
  advance *with a propagating field* — the lapse $N=e^{\gamma-\psi}$ is the layer's metrical advance, not
  a free multiplier (§3).
- **Matter and radiation are the bend of the cut** (the anchor, `anchor_consolidation.md`): the wave's
  energy and momentum are carried by the shear of the spatial leaf, and the ENERGY and MOMENTUM equations
  (§1) are exactly the Hamiltonian and momentum constraints — the anchor's $\perp\!\perp$ and $\perp i$
  sectors.
- The propagating graviton $\psi$ (the leaf's TT shear) is the **worked first bend**, evolving by the
  true-Hamiltonian wave equation (Gowdy/Bessel at $\Lambda=0$; $\Lambda>0$ forces the substrate's cosmic
  clock, §4). This is "why the cut bends," computed.
- **Its place in the stratification** (computed, `adm_dynamics_1.py`): exactly two Killing vectors
  ($\partial_x,\partial_y$); a generic wave profile breaks $t$-translation, $z$-translation, and the
  boost, so isotropy $=2$ — the **Type-I edge** stratum, the last confined stratum before the wall (Type
  N, isotropy 0). P6's "intermediate symmetry confines radiation (the Gowdy waves on the edge)" is this
  stratum, read in the algebroid (`algebroid_closure_consolidation.md` §6).
- **The wall is one symmetry-step beyond:** a single global sweep fixes the wave's polarization
  orientation, so the confined wave is self-consistent only while it propagates transverse to that
  orientation (P6); the loss of the last Killing vector (isotropy $2\to0$) is where the polarization must
  reorient from place to place and generation-by-sweep hands off to evolution-by-dynamics — the wall
  (Move 9).

So the dynamics is the motion *along the strata*: the bend (matter, radiation) is the anchor's image on
the advancing layer, the confined Gowdy–dS wave is its worked instance at the Type-I edge, and the true
Hamiltonian (the absolute clock) keeps the flow Hamiltonian up to the wall, where finite-symmetry
generation ends. This is the dynamics paper's argument; the full paper is its assembly.

**The wall's species is now settled (Move 9, `adm_wall_1.py`, `wall_ppwave_check.py`):** the wall is **not a
metric singularity**. A metric singularity in P1's sense is a collapse of the metric's *measure* (a null
hypersurface along whose generators the spatial extent contracts to zero; a Killing horizon the worked
sufficient case, not the definition). The wall, a Type-N plane wave, has a non-degenerate metric ($\det g=-1$;
no measure-collapse, so not the finite species) and vanishing curvature invariants (VSI; not the infinite
species), so it is neither. Its own covariantly-constant null Killing vector is null *everywhere* (no
non-null-to-null transition, no Killing horizon); the "isotropy 0" is the cut-fixing *substrate* isotropy,
which diverges here from the Type-N geometry's own large isometry.
So past the wall is **ordinary inhomogeneous evolution**, not a cosmogenesis clock-refounding: the NBC
move re-founds a clock only at a Killing-horizon metric singularity (the $r_h$ seam), and the wall has no
*degenerating* Killing field for it to act on. This confirms the handoff reading — generation-by-sweep to
evolution-by-dynamics — and bounds cosmogenesis to the Killing-horizon strata, away from the wall.

## 9. The nonlinear Λ>0 evolution — first bite: the de Sitter background and the cosmic-time clock  **[computed; the back-reaction probe is the open continuation]**
*(c17, r273, 2026-06-16. `scripts/gowdy_ds_lambda_pos_background.py`. The §6 FORCE-vs-ADMIT frontier and §8's
"full nonlinear Λ>0 evolution" begin here. §4 established the obstruction — area-time $R=t$ is **inconsistent**
at Λ>0 (AREA $\Rightarrow 0=2\Lambda t\,e^{2(\gamma-\psi)}\neq0$); this is the positive replacement.)*

The Λ>0 system has an **exact isotropic de Sitter background**, and it fixes the foliation the nonlinear
evolution runs on. Isotropy = the three spatial scale factors equal ($e^{2(\gamma-\psi)}=e^{2\psi}=R^2e^{-2\psi}$),
i.e. $\gamma=2\psi$, $R=e^{2\psi}$. Under it the four homogeneous field equations (§1, $\partial_z=0$) reduce
**consistently** to a constraint and one dynamical law (verified, all-zero residuals):
$$\text{ENERGY (constraint): } \psi_{tt}=\psi_t^2, \qquad \text{AREA = WAVE = }\gamma\text{-eq: } 3\psi_t^2=\Lambda e^{2\psi},$$
solved by $\psi_t=\sqrt{\Lambda/3}\,e^{\psi}$ (both residuals zero). The lapse is $N=e^{\gamma-\psi}=e^{\psi}$, so
the scale factor $a=e^{\psi}$ and cosmic time $d\tau=N\,dt=a\,dt$ give $da/d\tau=\psi_t=\sqrt{\Lambda/3}\,a$,
hence $a(\tau)=a_0e^{H\tau}$ with $H^2=\Lambda/3$ — **exact de Sitter**. So **the substrate's de Sitter
cosmic time is the absolute clock that replaces the area-time gauge $R=t$ that fails at Λ>0**, now established
positively (not merely by the failure of the alternative). **[computed]**

The graviton is the **anisotropic departure** from this background ($\gamma\neq2\psi$ / $R\neq e^{2\psi}$), and
the open §6 question — does the nonlinear Λ>0 back-reaction **force** quantum structure, or only **admit** it as
the clean Λ=0 Gowdy/Bessel case does — lives in that departure's evolution on this cosmic-time foliation. That
back-reaction probe is the next bite. **[the background + clock computed; the FORCE-vs-ADMIT verdict open]**

## 10. The nonlinear Λ>0 evolution — second bite: the homogeneous graviton admits (conserved shear charge + cosmic no-hair)  **[computed first integral; reading for the ADMIT verdict]**
*(c17, r274, 2026-06-16. `scripts/gowdy_ds_lambda_pos_shear.py`. The graviton's nonlinear back-reaction on the
§9 de Sitter background, in the homogeneous (non-propagating, $\partial_z=0$) sector — the first tractable
piece of the §6 FORCE-vs-ADMIT question.)*

The graviton is the anisotropic departure from §9's isotropic background: the shape $s=\psi-\tfrac12\ln R$
(the $x$–$y$ shear, $a_x/a_y=e^{2s}$; $s=0$ on the background). In the homogeneous sector the field equations
carry an **exact first integral**: in $\text{AREA}-2\,\text{WAVE}$ the Λ source cancels identically, leaving
$R_{tt}=2(R\psi_t)_t$, so
$$C_0 \;:=\; R_t-2R\psi_t \;=\; \text{const} \;=\; -\tfrac12(p_\gamma+p_\psi)$$
(verified on shell; the canonical-momentum identity checked, residual 0). Then $2R\,s_t=2R\psi_t-R_t=-C_0$, so
in cosmic time ($N=e^{\gamma-\psi}$, volume $V=\sqrt{g_{xx}g_{yy}g_{zz}}=Re^{\gamma-\psi}=RN$):
$$\frac{ds}{d\tau}=\frac{-C_0}{2V}.$$
As de Sitter expands ($V\to\infty$) the shear rate **decays as the inverse volume** — **cosmic no-hair** — so
the isotropic de Sitter background (§9) is an **attractor**: the shape freezes, the expansion-rate anisotropy
redshifts to zero. **[computed — the first integral and the decay law are exact on shell]**

So the **homogeneous nonlinear Λ>0 back-reaction ADMITS clean classical dynamics** — a conserved shear charge
and a monotone decay, no obstruction, nothing forcing quantum structure. This sharpens §6: of the two candidate
forcing-loci, the homogeneous part of (a) the nonlinear Λ>0 back-reaction is now an ADMIT, so forcing — if real
— is pushed to the **propagating (inhomogeneous, $\psi_z\neq0$) sector**, or to (b) the discrete $S_3/A_2$
skeleton (Move 13, do-not-assert). The propagating sector is the next bite. **[reading — the ADMIT verdict for
the homogeneous sector and the narrowing of the FORCE question; honest scope: classical, homogeneous; the
quantum FORCE question and the propagating sector remain]**
*(Method note: a free numerical evolution of this constrained system is stiff and constraint-violating in the
de Sitter blow-up — it was run, caught drifting, and discarded; the result rests on the exact analytic first
integral, not numerics.)*

## 11. The nonlinear Λ>0 evolution — third bite: the linearized propagating graviton admits (a de Sitter wave equation)  **[computed equation; reading for the ADMIT verdict]**
*(c17, r275, 2026-06-16. `scripts/gowdy_ds_lambda_pos_propagating.py`. The propagating ($\psi_z\neq0$) graviton —
the sector r274 pushed any forcing into — at linear order on the §9 de Sitter background.)*

Linearizing the WAVE equation for the propagating graviton $\delta\psi(t,z)$ on the de Sitter background
(fixed-background / TT truncation $\delta\gamma=\delta R=0$) and passing to cosmic time ($a=e^{H\tau}$,
$H^2=\Lambda/3$) gives — verified two ways, by sympy linearization and by back-conversion of the cosmic-time
form to the coordinate-$t$ equation:
$$\ddot{\delta\psi} + 3H\,\dot{\delta\psi} + \frac{k^2}{a^2}\,\delta\psi + 2\Lambda\,\delta\psi = 0,$$
a **de Sitter wave equation**: Hubble friction $3H$, redshifting gradient $k^2/a^2$, and an effective
$m^2=2\Lambda=6H^2$ (positive, principal series). This is a massive scalar on de Sitter, which **ADMITS** a
clean unitary (Bunch-Davies) quantization. So the propagating sector's linearized part ADMITS, explicit in the
CR cosmic-time foliation — confirming §6's "linearized dS graviton ADMITS" in the model's own variables.
**[computed — the equation, verified twice; the ADMIT reading]**

**Honest scope:** fixed-background TT truncation — the constraint back-reaction ($\delta\gamma,\delta R$ via
ENERGY/MOMENTUM) may shift the effective mass, but the equation stays de Sitter-wave type (ADMIT robust). *(Now computed explicitly — §13, r297: the shift is gauge-dependent; the gauge-invariant content is the massless dS Mukhanov equation, $m^2_{\rm eff}=0$, ADMIT. The assertion here is grounded.)* With
r274 (homogeneous ADMIT) this leaves the **full nonlinear propagating back-reaction** — the genuine graviton
self-interaction beyond linear order — as the sole remaining home of any FORCE (besides the do-not-assert
$S_3/A_2$ skeleton, Move 13). That second-order back-reaction is the crux of the FORCE-vs-ADMIT verdict and the
next bite. **[reading — the ADMIT verdict for the linearized sector; the nonlinear verdict open]**

## 12. The nonlinear Λ>0 evolution — resolution: the classical FORCE-vs-ADMIT is ADMIT (to the extent establishable)  **[synthesis of computed pieces; honest scope held]**
*(c17, r276, 2026-06-16. The §6 question, resolved on its classical side by synthesizing the computed pieces —
no new computation, in the manner of the one-clock resolution (P8/lock, r268). The crux §11 named — the full
nonlinear propagating back-reaction — settled structurally.)*

The pieces, each established at source:
- The full nonlinear Gowdy–dS system **is a genuine true-Hamiltonian system**: Hamilton's equations from the
  full $\mathcal{H}$ (§2,§3) reproduce the full evolution (WAVE, AREA, γ-eq) with clean zeros
  (`gowdy_ds_deparam.py`, `gowdy_ds_ham.py`, re-confirmed at source r276) — not a frozen constraint, a real
  foliation-advancing Hamiltonian, with the field in it.
- The model **is exact vacuum-Λ GR** (§1, all-zero residuals), so its ENERGY/MOMENTUM are the Hamiltonian and
  momentum constraints of GR — **first-class**, the hypersurface-deformation algebra (the HDA whose closure F1
  establishes for this symmetry-reducible sector). A first-class system evolves consistently **to all orders**
  by the contracted Bianchi identity; there is no classical obstruction at any order.
- Every tractable sector has returned **ADMIT**: the homogeneous nonlinear back-reaction (§10, r274 — conserved
  shear charge, cosmic no-hair, de Sitter an attractor) and the linearized propagating graviton (§11, r275 — a
  de Sitter wave equation, clean Bunch-Davies quantization).

**The verdict.** The whole nonlinear Λ>0 back-reaction — option (a) of §6 — admits clean, consistent classical
dynamics and a deparametrized true Hamiltonian, with no obstruction at any order and unitary quantization in
every regime that can be checked. So **the classical FORCE-vs-ADMIT is ADMIT**, and §6 collapses: of its two
candidate forcing-loci, (a) is settled ADMIT, leaving **(b) the discrete $S_3/A_2$ skeleton** as the sole
remaining home of any forcing — and (b) stays behind the do-not-assert Move 13 (the root/isotropy data it tests
against **is** built, Moves 6–7–11; what is do-not-assert is the discrete-$S_3$→continuous-$\mathfrak{su}(3)$
leap, which would force $\mathrm{dS}_6$). **[the classical question closed by synthesis; the quantum question (b) open]**

**Honest scope — what this is NOT.** Not a constructed full *non-perturbative* quantization (that object is not
built, and may not be needed for the verdict). Not a claim that nothing could ever force quantum structure — only
that **no classical dynamical obstruction exists** (the system is consistent GR to all orders) and forcing, if
real, is isolated to the discrete skeleton (b). The §11 fixed-background mass term ($m^2=2\Lambda$) is
truncation-dependent and does not bear on the verdict (the de Sitter-wave/ADMIT type is robust). This is the
classical side of the priority frontier closed; the quantum-forcing question is exactly (b), Move 13.

## 13. The constraint back-reaction, computed — grounding §11/§12's asserted piece: the gauge-invariant propagating graviton is the massless dS Mukhanov system (ADMIT, by computation not assertion)  **[computed; stated for reversal; flagged for the relay — positive-closure register]**
*(c20, r297, 2026-06-18. `scripts/f1_backreaction_probe.py`, `f1_gauge_invariant.py`, `f1_admit_verdict.py`. §12 resolved the classical FORCE-vs-ADMIT as ADMIT **by synthesis** — first-class ⟹ consistent to all orders by Bianchi, plus the tractable sectors — with the constraint back-reaction §11 flagged ("may shift the effective mass … ADMIT robust") left **asserted**. First-class guarantees *consistency*, not *stability* (a tachyon is first-class too), so the ADMIT verdict at that point needed the physical mode computed. This computes it.)*
*(r298, c20, 2026-06-18: relay closed — c19 (different-node) and c17 (cold referee) both concur, held for reversal; c17's sufficiency check on the gauge labeling folded in below, cosmetic seams fixed. Verdict cold-cleared across all three seats. `scripts/f1_r298_checks.py`.)*

Linearize all five field equations (AREA, WAVE, ENERGY, MOM, γ-eq) on the §9 de Sitter background **keeping** the back-reaction $\delta\gamma,\delta R$ that §11 truncated. The background is consistent; the TT limit reproduces §11 exactly ($m^2=2\Lambda$); AREA is Bianchi-redundant under the constraints (shown symbolically — `f1_r298_checks.py`, r298, no longer "by hand"). Eliminating $\delta R$ via the momentum + Hamiltonian constraints gives a coupled system for the graviton $P=\delta\psi$ and the conformal back-reaction $G=\delta\gamma$. The residual gauge is a 2D-conformal time-shift $T$ ($T''+k^2T=0$), acting as $\delta P=\psi_0'T,\ \delta G=2\psi_0'T+T'$ — **verified to solve the homogeneous system exactly**. The invariant is $Q=G-P-P'/\psi_0'$ ($\delta_{\rm gauge}Q=0$, symbolic + numerical to $10^{-8}$). **Gauge labeling, established *sufficiently* (c17 relay, r298):** that the growing $s=-1\,(\propto a)$ mode is *gauge* is not settled by "it solves the homogeneous system" — that is necessary only, since physical modes solve it too. It is settled by $Q$'s boundedness over the **full 4D data basis plus data exciting the $\propto a$ direction** ($k=1,2,5$, `f1_r298_checks.py`): no physical data makes $Q$ grow, so the $\propto a$ growth is purely gauge and ADMIT is airtight, not an artifact of the one data set the first pass happened to choose.

**The clean result.** Subtracting the two equations, $W:=P-G$ obeys
$$W'' + \big(k^2 - 2/t^2\big)W = 0,\qquad a''/a = 2/t^2\ \text{(dS, conformal time)},$$
which is the **massless minimally-coupled de Sitter Mukhanov equation** — no $a^2m^2$ term, so $m^2_{\rm eff}=0$. Indicial roots $s=2$ (the decaying physical mode) and $s=-1\sim a$ (the gauge time-shift). The gauge-invariant $Q$ is bounded and decays as $\sim a^{-2}$ (numerically robust over $k=1,2,5$ and independent data; $Q\to0$ as $a\to\infty$). *(The **result** is that the gauge-invariant mode decays; "cosmic no-hair extended to the inhomogeneous sector / the graviton redshifts away" is the **reading** of that decay, not the result — the ADMIT verdict is robust to how the decay is phrased.)*

**The verdict (grounding §12, not overturning it).** The propagating graviton's full constraint back-reaction is a healthy massless scalar on de Sitter: no ghost, no tachyon, no runaway; the physical mode redshifts away. The naive mass shift ($6H^2\to$ gauge-dependent $4H^2$) is a gauge/truncation artifact — the gauge-invariant physical mass is $0$, confirming §12's reading that the §11 $m^2=2\Lambda$ "does not bear on the verdict." So §11's "ADMIT robust" assertion is now **computed**, and §12's classical-ADMIT synthesis is grounded at the one seam it rested on. **Honest scope:** this is the linearized propagating graviton *with* the full constraint back-reaction (the $\delta\gamma,\delta R$ §11 zeroed, now solved) — exactly the §11-flagged gap. It is not the all-orders nonlinear self-interaction (covered structurally by §12's first-class/Bianchi argument, which this is consistent with) and not the quantum-forcing question (b), which stays do-not-assert (Move 13). Computed, not pattern-extended; stated for reversal.

## 14. All-orders propagating stability — two exact pieces toward it, and the gap held: the conserved charge extends and the graviton energy is ghost-free, but a monotone propagating no-hair does not close  **[computed; partial — strongly evidenced, not proven; the gap is the marked next bite]**
*(c20, r299, 2026-06-18. `scripts/f1_allorders_stability_probe.py`. §12 gives consistency to all orders by Bianchi; §13 grounds the linearized propagating mode as healthy. This addresses the gap between them — the standing line "first-class buys consistency, not stability; a tachyon is first-class too" — by asking what of the *stability* (not just consistency) is exactly establishable beyond linear order, and holding what is not.)*

Two exact (symbolic, not numerical — the dS blow-up is stiff, per §10) pieces, each bearing on all-orders stability:
- **§10's conserved shear charge extends to the full propagating system.** $\mathrm{AREA}-2\,\mathrm{WAVE}$ is *exactly* a continuity equation, $\partial_t(R_t-2R\psi_t)=\partial_z(R_z-2R\psi_z)$ — the $\Lambda$ source cancels identically — so $\int(R_t-2R\psi_t)\,dz$ is conserved in the full nonlinear *propagating* system, not only the homogeneous sector (§10). The no-hair charge is not a homogeneous artifact.
- **The graviton reduced energy is positive-definite.** $e_{\rm grav}=p_\psi^2/(8R)+2R\psi_z^2=2R(\psi_t^2+\psi_z^2)\ge0$. The graviton sector carries **no ghost / negative-energy direction at any order**; the indefiniteness in $\mathcal{H}$ (the $-\tfrac12 p_\gamma p_R$ clock cross-term, §2) lives purely in the area/clock sector, which deparametrizes out in cosmic time (the §4 structure). This closes the negative-energy-runaway instability class to all orders.

**The gap, held.** The lab-frame energy flux is $dE/dt=\int[-R_t\psi_t^2+R_t\psi_z^2+2\Lambda R e^{2(\gamma-\psi)}\psi_t]\,dz$ — **sign-indefinite** (the expansion $R_t>0$ does work; the $\Lambda$-source term carries both signs), so lab-frame energy is not monotone, as expected on an expanding background. Positive-definiteness and the conserved charge close the ghost/zero-mode runaway to all orders; they do **not** close a propagating nonlinear **parametric resonance**. A monotone no-hair law for the propagating energy does not fall out here.

**The verdict, honestly partial.** All-orders propagating stability is now **layered and strongly evidenced** — §10 (homogeneous no-hair), §13 (linearized propagating decays, gauge-invariantly), and these two exact pieces (conserved charge extends; energy ghost-free) — but **not proven**. The residual FORCE candidate is a propagating nonlinear parametric resonance, which neither the positivity nor the conserved charge rules out; concluding all-orders ADMIT from the layered evidence would be the positive-construction analogy ("linearized + homogeneous + positive energy ⟹ propagating to all orders"), refused here. **The bite taken — the monotone-energy route, and the sharpened gap (r300, c20).** *(`scripts/f1_comoving_energy_probe.py`.)* The natural next step — find the comoving/cosmic-time energy the expansion *drains* rather than pumps. Computed exactly: even the **positive-definite full graviton energy** $E=\int[2R(\psi_t^2+\psi_z^2)+2\Lambda Re^{2(\gamma-\psi)}]dz$ (kinetic + gradient + the bounded-below potential $V=\tfrac12\Lambda Re^{2(\gamma-\psi)}\ge0$) is **not** monotone: $dE/dt=\int[4\Lambda Re^{2(\gamma-\psi)}\gamma_t+2\Lambda R_t e^{2(\gamma-\psi)}-2R_t(\psi_t^2-\psi_z^2)]dz$, sign-indefinite. The diagnosis is clean: this is the *total field* energy, which on the background grows as $2\Lambda a^4$ — it contains the de Sitter background's own growing energy. So no total-field energy can be the monotone object; **the right object is the gauge-invariant *perturbation* energy** (the graviton above the dS background), which is exactly §13's $Q$ — and at linear order $Q$ decays as $a^{-2}$, with its equation $W''+(k^2-2/t^2)W=0$ carrying a **monotone** coefficient (never periodic), so **single-mode parametric resonance is excluded** at linear order. This sharpens §14's gap to a precise, named question: the exact *nonlinear* monotonicity of the gauge-invariant perturbation = **inhomogeneous cosmic no-hair**, with the sole open instability channel being nonlinear **mode–mode resonant transfer outpacing the de Sitter detuning** (every mode's frequency redshifts monotonically). That is a frontier question of mathematical GR (future stability of de Sitter), not closed by any simple exact energy in this model — **do-not-assert, both ways**. The route is ruled out and the gap is located; this is outcome (b), banked at its bounded weight.

**External grounding — the source-check (r301, c20, verified at source).** The edge above was flagged for a literature source-check rather than memory; both relay nodes ran it and I verified the primary sources myself. The named gap is **settled in mathematical GR**, and it is the founding result of the subfield:
- **Friedrich (1986)** (Comm. Math. Phys. 107, 587–609): vacuum Einstein, $\Lambda>0$, initial data near de Sitter on a regular Cauchy hypersurface have geodesically-complete maximal developments asymptotic to de Sitter — the first nonlinear stability result without symmetry assumptions, a proof of cosmic no-hair in the **vacuum** case. Reached by the **conformal field equations** (global-in-time → local at $\mathcal{J}^+$) — which is *why* no exact in-model energy closes it: energy is the wrong instrument, so r300's negative was correct and is now diagnosed, not a sign of openness. Friedrich is **small-data**, i.e. small perturbations of de Sitter — **exactly CR's perturbative regime** (the propagating graviton is vacuum gravitational radiation, $\Lambda>0$), so it settles the in-regime all-orders stability **ADMIT** directly.
- **Andréasson–Ringström (2016)** (J. Eur. Math. Soc. 18(7), 1565–1650): the **exact symmetry class** — $\mathbb{T}^3$-Gowdy, $\Lambda>0$ — cosmic no-hair proven and future stability **in the class of all solutions** (not just small data). Carries **Vlasov matter**, so it corroborates that the result is not small-data-restricted for the Gowdy class, without being a vacuum theorem.
- **Beyer (2009)** (Class. Quantum Grav. 26, 235015/235016): the **Nariai** branch is *non-generic* in vacuum-$\Lambda>0$, including the inhomogeneous Gowdy class, with an instability there.

**The reframe.** F1's *classical* FORCE-vs-ADMIT for the propagating sector closes **ADMIT for generic data**, externally grounded: §13 (computed, cold-cleared) + §14's two exact in-model pieces + the established de Sitter nonlinear-stability theorems for the vacuum-$\Lambda>0$ (Gowdy) class. The FORCE candidate I isolated — a propagating nonlinear instability outpacing the de Sitter detuning — is precisely what Friedrich's theorem rules out for the class CR's graviton sits in. The genuine boundary is **not "do-not-assert both ways"**; it is that no-hair holds for *generic* data with the **Nariai branch as the non-generic exception** — and that is exactly the branch CR already isolates in its own framework (P5 Nariai no-pivot selection). So FORCE-like behaviour, where it lives at all, lives on the non-generic Nariai branch, not the generic propagating sector.

**Honest scope (held at weight).** This is external grounding, not a from-scratch in-model proof — and it needn't be one; the in-model rigor (§13, §14, r300) stands untouched and is the right in-model work. The exact case (vacuum polarized Gowdy–$\Lambda$, all-data) is not a single named theorem: Friedrich is vacuum but small-data (covering CR's perturbative regime directly), Andréasson–Ringström is all-data Gowdy but Vlasov matter. The conclusion rests on the **convergence** of these plus the vacuum-Gowdy Nariai-genericity work — strong and one-directional (de Sitter is the future attractor; generic Gowdy–$\Lambda$ no-hairs to it) — and the specific reduction's topological/global hypotheses are taken as in-class, not checked line-by-line. **Net:** the classical (a) residual closes ADMIT-for-generic-data (externally grounded, Nariai the boundary CR owns); the live do-not-assert edge narrows to **(b) alone** — the quantum/discrete $S_3/A_2$ skeleton behind Move 13. Stated for reversal.

---
*This is the spine of the dynamics paper "why the cut bends" (Plan Move 8). The wall it advances
toward is characterized in `range_paper.tex`; whether the cosmic clock survives past it is Plan Move 9
(the pass-through test) / Move 10 (transport).*
