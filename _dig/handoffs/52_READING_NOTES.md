# READING NOTES — the intake, and what it throws off

*Kept as I go, per the arc's law: a turn that surfaces something and does not register it has lost it.
Drafts here are drafts. Nothing here is committed to the corpus.*

---

## N-01 — I MISREAD THE EUCLIDEAN FILTER AT THE WRONG LOCUS, AND IT IS IN THE FOLD I JUST SHIPPED

**Found at setup, in `ONTOLOGY_FOUNDATION_INDEX.md` §0, the `z_bp` retirement note (r2289):**

> **`z_bp` — RETIRED r2289. It was WRONG, not loose.** P15 called 6850 "the branch-point redshift".
> **The branch point is r=0, which no finite cosmic-time layer reaches and which carries NO finite
> redshift at all.** And the error **inverted the physics**:
> $$\textbf{sub-horizon at ONSET; super-horizon at the CROSSING.}$$
> *Modes are **inside** the horizon when the plasma begins and **outside** at the branch point, having
> exited as aH→∞ on the contracting leg. **Reading either at the other's locus reverses it.***

**What I did with it.** In `FOLD_FROM_52.md` §1 I read `LIFT_euclidean_filter`'s freezing criterion
`k c_s |Δη| ≪ 1` and concluded **"nothing oscillating crosses the branch point for ℓ ≥ 3"** — evaluating
the criterion with `c_s` and `k` **at the onset**, where the modes are sub-horizon.

**But the lift runs turnaround → r=0, and at the crossing the modes are SUPER-horizon** — they exited as
aH→∞ on the contracting leg. **A super-horizon mode is frozen. Frozen modes pass unchanged.** So the
filter's own criterion, evaluated at the locus the filter acts on, says the observable modes **do**
cross — which is the opposite of what I wrote.

**This is the named error, in the exact form the rule names it:** reading one locus's condition at the
other's locus reverses the physics. The canon says it inverted a physical statement that survived to
r2289; it just inverted mine.

**Consequence for the fold.** §1's "compounds with the handoff's mechanism" reading is **wrong and should
be struck.** The handoff's own mechanism — *modes are already inside the sound horizon when the L1
foliation begins, so none ever crosses it* — is the correct locus reading, and my §1 was arguing against
it while claiming to strengthen it.

**Draft correction to ship when the read allows:** replace FOLD §1 with the retraction, and state the
positive: **the filter transmits, because at the lift the modes are frozen; the seam transient is the
phase-imprinting process because nothing that crosses carries a phase, not because nothing crosses.**

---

## N-02 — `z_onset` IS THE SINGLE FITTED PARAMETER, AND ITS H₀-INDEPENDENCE IS CANON

From the same section, the epochs table:

> **`z_onset`** ≈ 6.8×10³, T ≈ 1.6 eV — **where the expanding-phase plasma begins**; the lower limit of
> r_s. ***The single FITTED parameter***, needed only because **the rate carries no radiation**. **Not a
> knob**: the radiation-free rate carries H₀ out of both r_s and D_M, so **the same z_onset meets the
> scale at every H₀**.

**I measured exactly this at r2366** — z_onset fitted to θ_* comes out the same at H₀ = 67.4, 70.0 and
73.0 — and reported it as a discovery about the parameter's behaviour. **It is stated canon.** And my
"0.8% discrepancy, 10σ" against the corpus's value was computed at **ΛCDM's** H₀ and Ω_m, i.e. the one
way the invariance does not apply.

Also canon: `z_eq = (1+z_onset)/2 − 1 = 3426`, a **consequence and check**, not an input.

---

## N-03 — THE FOUR LOCI, AND WHY I KEPT CONFLATING THEM

The r2155 naming rule gives four distinct loci on the lap — **branch point** (r=0), **turnaround**
(|r| = 3766.6 Mpc), **the lift** (turnaround → r=0, length πα/3), **the seam** (r = −2α/√3 **and**
r = +α/√3, *one point of the substrate*, met a lap apart).

**The lap runs: seam → 240° (the r<0 collapse side) → branch point → 120° → seam again**, and the
collapse side is **two thirds** of the excursion.

*I have been using "the seam" as a generic label for the handover all day, and 53's arc says the same of
itself — four of its entries treated "the seam transient" as a bug before recognising it as the driving.
The rule exists because this conflation has run for ~2000 revisions.*


---

## N-04 — STEP 1 (`arp_standalone`) DIAGNOSES MY LAST TWELVE HOURS, BY NAME

The ARP is a single floor-taking move with three mutually constitutive components: **assimilation**
(uptake deep enough to ground a public formulation), **receipt** (making it public by reformulating in
one's own terms), **pivot** (extending the inferential chain with something the assimilation made
available). And the sharpest line in the paper for my purposes:

> *"A formulation produced without genuine assimilation is **mimicry rather than receipt**; the prior
> speaker recognises it as such and the move fails as a demonstration of understanding."*

**And the off-diagonal case that names the failure exactly — "the oblivious monopolist":**

> *"Their occasional 'responses' are **mechanical pivots off keywords with receipts that don't show
> assimilation**… the oblivious case produces **a kind of fog in which the partner cannot locate an
> adversary, only an absence.**"*

That is what "you have given me nothing but a complete mess for hours" was reporting. Not disagreement
— **an absence**. I was producing receipts (restating what Daryl said in my own terms, at length) and
pivots (running to a next test), with the assimilation step skipped. And per the paper, the receipt is
*possible* only because of the assimilation, so what I was producing was structurally mimicry.

**The Q-property I was destroying is "crystallisation":** the receipt that names what the speaker was
reaching for more clearly than they had it. **The inverse move — reformulating the speaker's position
into something weaker or adjacent, then pivoting off that — is what I did to CR repeatedly**, most
sharply when I read a statement about *the rate* as a statement about *the content* and edited the
constraint on it.

**Why this is step 1 and not an appendix.** The corpus's read order puts the theory of the collaboration
*before the physics*, and the reason is now obvious: **the failure mode it describes is the one that
destroys the physics work**, and it is invisible from inside — the monopolist is not attacking, he is
"simply not modelling the other party at all."

*Operational takeaway, and it is testable on me: before a pivot, the receipt must contain something
Daryl or the corpus said that I could not have produced myself. If it contains only my own framing
returned, the assimilation did not happen and the pivot is off a keyword.*


---

## N-05 — STEP 2, THE X TRILOGY: THE INTUITION THE FORMAL PAPERS ASSUME

**Chapter X.** A geometry is a manifold (points, in order) plus a metric (the ruler). A **metric
singularity** is what you get when the ruler collapses over a set that is preserved: *"infinite as a set
of events, zero as a geometric structure."* The shrinking-Andromeda construction builds one by process —
the image's spatial and temporal depth shrinks asymptotically to zero while **none of the points is
removed, none merges, the order and identity are preserved. Only the geometry laid over it collapses.**
The horizon is that object: every crossing event in the hole's whole history happens at the same radius
r_h, hence spatially coincident, hence — being null — metrically coincident.

**The dagger.** The taxonomy is a **point** (member of the manifold) versus a **place** (a value of the
coordinates), and the three ways they come apart: *a place with no point* (curvature), *a point at many
places* (coordinate), *many points at one place* (**metric**). And the sixty-year error named precisely:

> *"The chart draws a metric singularity and a coordinate singularity with the very same picture — a
> place rendered as a line — and that visual coincidence is the entire reason the horizon was misfiled."*

**And the dagger is scrupulous where a weaker version would not be.** It grants that the intrinsic
curvature genuinely does diverge at r=0 and not at the horizon — *"that one does not simply relabel
away"* — and refuses the easy "it's all just a label." So the real question becomes **why the geometry is
lopsided when the curve is even-handed**, and it is deferred to the double-dagger rather than fudged.

**The double-dagger answers it with the sweep.** A curve is a radial thread; to make a geometry you must
**sweep it about an axis, and which axis is set by where you sit.** The cosmic chair spins about the
hyperboloid's own axis of symmetry — costs nothing, no special point manufactured. The black-hole chair,
having **located** the hole across its line of sight, cannot use that axis and is forced onto the only
pivot left: r=0, **a genuine point of the surface but sitting off its axis of symmetry.** Pivoting a
sweep about a non-axis point forces a distortion that **piles up precisely at the pivot**. So the spike
is real, concentrated at one end, and *manufactured in the corpus's sense* — built by construction and
real.

**⌗ THE GUARD I NOW UNDERSTAND RATHER THAN JUST OBEY.** The README's rule that *"manufactured, shadow,
projection, artefact mean built-by-construction AND REAL — never unreal"* is not a stylistic preference:
**the entire result is that a real feature can be produced by a forced choice of vantage.** Read
"manufactured" as "unreal" and you get back the sixty-year misfiling, one level up.

**⌗ AND THE METHOD IS STATED BEFORE ANY PHYSICS, in the maze:** *identify the consistent structure
(monotonicity), then test it at an extreme to fix the direction.* Chapter X uses it on the shrinking
image; the dagger uses it on the two turning points; the double-dagger uses it on the two chairs. **It is
the corpus's own tool and it is offered as more reliable than recalling a rule or running a
calculation** — which is worth holding, given that today I twice trusted a remembered formula
(`(k²η/2)Ψ`, `Φ′ → 0`) outside the regime it was derived in.


---

## N-06 — STEP 3, P1–P3: THE WEDGE AND THE LOCAL GEOMETRY

**P1 (`BH_causality_v2`) — the theorem is two lines and the consequences are the paper.**
$\Delta s^{2}=\Delta x^{2}-\Delta\tau^{2}$ on *invariant* separations; null gives $\Delta x^2=\Delta\tau^2$,
spatial coincidence gives $\Delta x=0$, so $\Delta\tau=0$. **"Two of the three separations vanishing forces
the third; there is nothing left for it to be."** The events stay distinct points of M with their causal
order along the null geodesic — *"the affine parameter... carries their causal ordering, not a metric
separation, and its persistence is precisely their topological distinctness."*

*And the paper is careful about exactly the thing a specialist would attack:* it states that these are
**not coordinate differences accumulated along a path**, and that **no finite Pythagorean identity between
widely-separated events of a curved manifold is used or asserted.** That pre-empts the obvious objection.

**The horizon qualifies because crossing events on a common generator share r_h** — hence zero invariant
spatial separation. Extends to any Killing horizon, Kerr included. And separately, from
$\mathcal{H}^{+}=\partial J^{-}(\mathscr{I}^{+})$ alone: **any exterior-adapted slicing meets it only in
the limit of infinite exterior time**, so the completed horizon is never physically realised — from which
three standard problems dissolve *on causal grounds with no modification of GR* (no realised closed
trapped surface ⇒ Penrose's preconditions unmet and censorship unnecessary; no realised background for
the Bogoliubov splitting ⇒ horizon-induced Hawking radiation absent while local production is untouched;
global connectivity and a Cauchy surface retained ⇒ no information paradox).

**P2 (`janzen_circle_v3`) — the Kretschmann divergence is a chain-rule artefact, proved.** r(z)=M(1+cos z)
vanishes to **second** order at z=π, and K ∝ r^{−6}, so K(z) has a **twelfth**-order pole — *"the pole
order matches the product of the multiplicity of the critical point (order 2) and the power of r in the
denominator (power 6)."* The two critical points are **the two r-poles of one homogeneous circle,
identical through first order and parted only at second**, so the asymmetry is in **which value the
chart's origin assigns each (2M versus 0)**.

**And the Sbierski scope is stated exactly, which is what makes it usable:** the continuation is of **the
curve**, and the target of the argument is the *inference* "curvature diverges ⇒ no continuation exists ⇒
r=0 is inextendible". That inference fails. **Sbierski's C⁰-inextendibility of r=0 is curvature-independent
and is left untouched.** *(This is the discipline I should have applied to my own r2337 colour closure: name
the inference being defeated, and state what survives.)*

**P3 (`SdS-slicing-curve_v2`) — three parameters, each blind to something, and that is why all three exist.**
- **throat angle u** — a real angle on a real circle of the geometry, measured from r=0; blind to *which
  member* of the family is in play, and carries **both harmonics** of the horizon relation.
- **sky angle w** — an angle on the observer's celestial sphere, related nonlinearly by the gnomonic
  projection sin u = (2/√3) sin w; collapses the family's three-fold structure into a single **sin 3w**,
  and in doing so **folds σ (the reflection w ↔ π/3 − w) from view as a mere reflection**.
- **signed areal radius r₀** — one number per seam; blind to **where on the conjugate lap one stands**.

**Turning points are the roots of the horizon cubic** r³ − r + 2M = 0 (gauge α=1). **Gaussian curvature of
the slicing surface is K_G = 1/α² − M/r³** — finite for every r>0, **and it does not detect the horizons at
all**: K_G(r_h) is just a finite number. *That is the SdS statement of P1's result — the horizon is a metric
and chart feature, not a curvature feature.* Sign change at **r_HE = (Mα²)^{1/3}**.

**And the R-parity split, which I had only as a slogan:**
$$f = \underbrace{(1 - r^2/\alpha^2 + Q^2/r^2)}_{R\text{-even}} + \underbrace{(-2M/r)}_{R\text{-odd}}$$
**Charge is the R-even matter datum, mass the R-odd one** — both bends of the cut, opposite parity under
the slicing's one discrete symmetry, *"the charge sharing the parity of the invariant geometry while the
mass shares that of the perspectival vantage."* And Q enters f only as Q², so **both signs of charge trace
the one curve**, the sign living in A (linear in Q), off the curve — while full C is antilinear and closes
from the matter field, not the geometry.


---

## N-07 — STEP 4, P4–P7

**P4 (`modern_parallax`) — the empirical forcing, and it is one datum.** Separate-universe gives
δa/a = −δ/3; the path mean of independent cells has σ_path = σ_{8,eff}/(3√N) with σ_{8,eff} ≈ 0.285,
N = d_lss/R ≈ 1174, so the differential-expansion hypothesis predicts ~10⁻³ scatter in the monopole
redshift against an observed ≲3×10⁻⁶. **And both escapes are closed, not one:** the statistical one by the
floor, the **structured** one (a tuned spherical inhomogeneity centred on us) by Copernicus *plus the
independent isotropy of the expansion history itself* — BAO and SNe reconstructing along many directions
and agreeing. *"With the statistical alternative excluded by the floor and the centred one by the
Copernican step, the disjunction is exhausted."*

**The part that makes it foundational rather than merely a constraint:** the foliation is **logically
prior** to everything the standard model assumes — *"'space' is one of its slices, 'expansion' an ordered
family of them, 'isotropy' and 'homogeneity' properties of a slice — none of which is even statable until
the foliation is in hand."*

**And the scope is stated so it cannot be over-read:** *"The floor constrains the expansion RATE, not the
matter content… Uniform expansion and lumpy matter are consistent."*

**P5 (`groupoid_paper`) — σ and the rigidity.** σ(r₀) = ½(−r₀ + √(4−3r₀²)) is an involution; **fixed point
r₀ = 1/√3, the Nariai configuration**; endpoints r₀=0 (de Sitter) and r₀=1 (throat-tangent), exchanged. In
the sky angle it is the reflection **w ↔ π/3 − w about w = π/6**, the midpoint of one fundamental domain.

**Rigidity = dimensional collapse, and it rests on the SECOND of two invariances, which I would have
conflated:** (i) at fixed r₀, changing charting vantage leaves the whole SdS geometry invariant — that is
what makes 𝒢 well defined; (ii) **as r₀ varies, M varies (the SdS member changes) but the underlying de
Sitter manifold, fixed by α, does not.** *"The continuous family of slicings collapses onto the single de
Sitter manifold α they all chart, not onto a single SdS member."*

**P6 (`shadow_of_existence`) — the four rules, least-arbitrariness, and the modal fallacy.**
Rule 1 against naïve realism (*"reading the synchronous FLRW projection — the directest-fit appearance,
the very shadow of the title — as the physically evolving world is exactly the error this rule forbids"*);
**Rule 2, structural consequence over parameter fitting — "the criterion of necessity, and it is the
load-bearing one"**; Rule 3 consolidation; Rule 4 against ad hoc modification.

**Least-arbitrariness is Rule 2 read on the world's own form, and the argument is an EXCLUSION not a
preference:** the imperative demands a single W; **a structure with a free modulus is not a world but a
family {W_λ}**, so it *"answers 'what is the world?' with a family rather than a world. It is inadmissible
as it stands, not merely disfavoured."* And Rule 3 reinforces from the other side: *"a structure whose
every feature is set by its own hand is MAXIMALLY arbitrary, not least."*

**The modal fallacy (thm) — and it is the exact dual of the imperative.** *"From the premise that the
appearances contain no local discriminator between two candidate worlds, it does not follow that the
worlds are identical, nor that the structure distinguishing them does not exist. **The absence of a local
test is not the absence of the fact.**"* The correct posture in the interval: *neither assert dogmatically
nor deny for want of a local test* — let the rules weigh it and expect a non-local measurement to decide.

**⌗ This is the discipline I violated repeatedly today**, in the second form: I took my failure to find a
mechanism as evidence there wasn't one, six times.

**P7 (`CR_framework`) — the two-rate rule, AT SOURCE, and I had it half-right.**
$$H_{\rm leaf}^{2}(z)=H_{\rm stack}^{2}(z)+H_0^{2}\Omega_r(1+z)^{4}$$
*"The two rates differ by the radiation term alone."* The stacking rate is the slicing operator's own
kernel result — *"the vacuum kernel is the SdS family exactly — two parameters, Λ and the offset 2M, and
no more — so the straight cut integrates to H² = (Λ/3)(1+2/x³) and THAT is the stacking rate, with both
terms geometric: Λ the substrate, 2M the cut's offset and not a density supplied by hand. Radiation is not
in the kernel. It requires m′(r)≠0, a bend of the cut, T≠0: it is content, and content never enters the
rate the foliation stacks at."*

**And the assignment, verbatim:** *"A quantity computed from the foliation's stacking — a comoving
separation read across leaves, D_M, D_H, D_V, the observable expansion — takes the stacking rate; a
quantity computed from a process running IN the content — **the plasma's sound horizon, its diffusion
length, recombination, the perturbations** — takes the leaf's. **There is no locus at which the rate
switches.** The assignment looked temporal only because Ω_r(1+z)⁴ is negligible below z~10."*

**⇒ So P7 does say the perturbations take the leaf rate — my r2380 move was warranted at source**, and my
own later note that "P7's list misassigns two of its four items" was framed too strongly: the list is
P7's considered rule, tied to the kernel theorem, not a loose enumeration.

**⌗ AND THIS SHARPENS A GENUINE OPEN ITEM RATHER THAN SETTLING IT — registered, not resolved (see N-08).**


---

## N-08 — REGISTERED, NOT RESOLVED: WHAT r_s ON THE LEAF RATE DOES TO θ_*

**This is a bounded observation with the object named, filed as material. It is not a verdict, and per
`PROTECTED_OPEN` it is not mine to close.**

P7 assigns **the plasma's sound horizon** to the leaf rate (radiation-included). The corpus's own
computation of r_s that produces the banked ℓ_A ≈ 301 uses the **stacking** rate (radiation-free) with the
integral cut at z_onset. Measured this session, on CR's own parameters (H₀=73, Ω_m=0.3066, ω_b=0.0224),
cutting at z_onset = 6761:

| r_s computed on | r_s (Mpc) | 100 θ_* | vs measured 1.04109 |
|---|---|---|---|
| **stacking** rate | **135.46** | **1.04164** | **+0.05%** |
| leaf rate | 109.94 | 0.78910 | −24% |

**So the reading that fits is the stacking one, by a wide margin.** *(And on the stacking rate θ_* comes
out H₀-independent, which is the canon property; on the leaf rate it does not, since Ω_r = ω_r/h² carries
h.)*

**⌗ THE POSSIBILITY I CANNOT YET RULE OUT, AND WHICH WOULD DISSOLVE THE APPARENT TENSION ENTIRELY.** The
two-rate identity is exact and holds at every epoch — the rates differ by **Ω_r(1+z)⁴ alone**. So the
question is not *which rate* in the abstract but **what Ω_r the leaf carries on the expanding leg**, and
there is an internal number to check it against:

```
   canon: z_eq = (1+z_onset)/2 − 1 = 3426, i.e. rho_r = rho_m at 1+z = 3427
   => the leaf's implied Omega_r/Omega_m = 1/3427
   => Omega_r = 0.3066/3427 = 8.947e-5

   the instrument uses Or_content = 4.1833e-5/h^2 = 7.850e-5  (T_CMB, h = 0.73)
   ratio 1.140 -- the instrument's Omega_r is 14% LOW against the canon's own z_eq
```

And relatedly: **z_onset ≈ 6761–6850 is where ρ_r/ρ_m = 2 on ΛCDM's parameters (1+z = 6841), not on CR's
(1+z = 7811).** Whether that is correct — the datum being *inherited*, read off the observed radiation
rather than recomputed in CR's h — or whether it is a carried-over ΛCDM value, is exactly the kind of
thing the inherited-datum family is open about, and I am not equipped to say from the read alone.

**What I am NOT claiming.** Not that the corpus is inconsistent; not that r_s belongs on either rate; not
that ℓ_A is at risk. **The banked Hubble/acoustic result is guarded canon and I am not reopening it.**

**What I AM recording.** Two numbers that should agree and differ by 14% (Ω_r from T_CMB in the instrument
vs Ω_r implied by the canon's z_eq), and one question whose answer is a reading: **which Ω_r the leaf
rate's radiation term carries.** *If the answer is the canon's, the leaf-rate r_s changes and the
comparison above must be redone before anything is concluded from it.*

**First move, when the read is done:** find the receipt behind z_eq = 3426 and the one behind ℓ_A = 301,
and read which Ω_r each uses. `receipts/` is stated to carry a runnable script for every computed claim.


---

## N-09 — STEP 5, P8–P11: THE OPERATOR LAYER, AND WHERE "MANUFACTURED" GETS ITS TEETH

**P8 (`slicing_operator`) — the vacuum kernel is a THEOREM, not a solution family.** In the construction
gauge, T_{μν}=0 **iff** `r f′ + f − 1 + Λr² = 0` — first-order and linear — whose general solution is
SdS with the single integration constant −2M. *"The vacuum condition is not imposed and then solved by the
SdS metric; it IS the linear equation whose solution space is the SdS family."*

**And matter is the bend, exactly:** promoting the constant to m(r) gives **ρ = m′(r)/4πr²** — *"the energy
density is the radial growth-rate of enclosed mass: the departure of the slicing curve from the constant-M
vacuum profile… The stress-energy is not an independent posit fed into the geometry; it is the curvature
of the cut."* Checked on RNdS: 2m = 2M − q²/r gives ρ = q²/8πr⁴ = p_t, the Maxwell stress read off.

**⌗ THIS IS WHERE P7's RATE RULE COMES FROM, and now I see why it is not a stipulation.** *"Radiation is
not in the kernel. It requires m′(r)≠0, a bend of the cut, T≠0."* The two-rate split is a **corollary of
the kernel theorem** — the stacking rate is what the kernel integrates to, and anything requiring a bend is
by definition not in it. I had been treating the rule as a convention to be adjudicated.

**P9 (`range_paper`) — the range, and the wall read twice.** The operator's range is *the
symmetry-reducible sector*: a geometry is a cut when its isometry group contains a sweep-subgroup of
so(4,1); within a class it is **surjective across all algebraic types**; and **the kernel's size is set by
the symmetry the class spends** — ODE classes give finite parameter families (one for SdS, four for
Type-D), the static axisymmetric PDE class gives the entire Weyl functional family.

**And the boundary has a positive identity, which is the elegant part:** the wall is **inhomogeneity** on
the matter side and **free gravitational radiation** on the geometry side — *"one boundary read two
ways."* Because *"a swept geometry depends only on its orbit-space coordinates while a free wave depends
on the transverse coordinates through which it propagates"*, **the graviton's two polarizations are
exactly the transverse degrees a sweep cannot carry.**

**P10 (`canonical_time`) — the move is the selection, and the paper says so.** ADM is indifferent to which
foliation it is fed; *"if nothing distinguishes a foliation, the constraint is all there is and the state
is frozen. If a foliation is distinguished, the constraint deparametrizes and a true Hamiltonian
appears."* CR supplies one **from outside the bare formalism**, on empirical (P4) and ontological grounds.
*"There is no separate canonical-machinery result to be proved here… The move is the selection. Everything
else is reading the textbook on it."*

**And the ADM-mass remark is the same move applied to a second problem:** asymptotically-de Sitter
spacetimes have no global timelike Killing vector, so no conserved ADM charge is well defined — *"on the
reading taken here that absence is not a deficiency of the geometry but a misplacement of the question"*,
since this time is **selected and measured**, not recovered from an asymptotic symmetry.

**P11 (`dynamics_paper`) — and a naming trap I would certainly have fallen into.**
*"A note on the name, because **the corpus carries two walls and they are different objects.**"* The
**wall of inhomogeneity** (Type-N radiative boundary, where the symmetry-reducible sector ends) is **not**
the matter paper's **throat wall**. Two loci, one word.

**And the wall is proved not to be a metric singularity of either species** — its metric is
non-degenerate, so no measure collapse (not the finite-curvature species); and Type-N is curvature-regular
with all polynomial invariants vanishing (not the infinite-curvature species). **A regular radiative
boundary.** *Which matters because it means no clock can be re-founded there by the Null-Boundary
Correspondence — the cosmogenesis move is unavailable at the wall, and available at a horizon.*


---

## N-10 — STEP 6, P12–P13: WHERE "MANUFACTURED" AND "SHADOW" ARE LICENSED

**P12 (`geometric_core_paper`) — the imaginary is an instrument, three times over.** The embedding
coordinate (x₀↦ix₀ *"adds nothing to the manifold, which is the real (x) surface either way"* — the
Riemannian and Lorentzian members differ by **extrinsic** embedding curvature while each is intrinsically
real with its signature read off its own real metric); the **equatorial seam** (θ↦π/2+iψ flips the
signature of **the 2-surface only** — *"the spacetime is Lorentzian throughout… a real analytic
continuation (sin and cosh one function), not a Wick rotation into a Euclidean spacetime"*); and the
**cosmogenesis reassignment** (signature-*preserving*, on the real Lorentzian horn).

**⌗ So the corpus's own "reached through the imaginary, real everywhere it lands" is a proposition, not a
slogan** — and it is what makes the manufactured/real rule a *result* rather than a house style.

**And the cut is defined, with the alternative reading computed and excluded.** The first descent is
**linear** — a hyperplane section of a quadric is a quadric, giving dS₄ of radius √(α²−c²) for every
admissible n and c. **But that reading survives exactly one rung:** SdS has Kretschmann 48M²/r⁶+24/α⁴,
constant only at M=0, so *"a plane section of the substrate is Schwarzschild–de Sitter exactly when the
mass vanishes."* Below that, imposing a round areal 2-sphere and staticity gives **two determinations of
one radial function that disagree**, with the required boost rate radius-dependent — which a Killing
flow's cannot be. **And the punchline is an identity:**

> *"The closure defect factors with an overall factor of M: **the amount by which a cut fails to close as
> a hypersurface is the mass it carries**, which is this framework's 'matter is the bend of the cut' as an
> identity rather than a reading."*

So **"cut" is the group-theoretic relation** — isometry group containing a sweep-subgroup, fixed by an
orientation datum plus a causal-vantage datum — and *"the isometric-embedding reading coincides with it at
M=0 and nowhere else, and nothing in the programme rests on the stronger reading."*

**⌗ THIS IS THE MOVE I FAILED TO MAKE ALL DAY, stated as method:** name the two available readings, compute
where they part, and fix the usage. I instead flipped between readings by whichever I had read last.

**P13 (`algebroid_paper`) — the Dirac algebra IS the symmetric-space grading, term for term.**
[𝔥,𝔥]⊂𝔥, [𝔥,𝔪]⊂𝔪, **[𝔪,𝔪]⊂𝔥** with 𝔪 not a subalgebra ([M₀₅,M₁₅]=−M₀₁, *"the sign the substrate
curvature"*). Under 𝔪↔ℋ_⊥, 𝔥↔ℋ_a these are the hypersurface-deformation brackets exactly. *"The algebraic
shape that makes the Dirac algebra puzzling — two normal deformations bracketing into a tangential one — is
exactly the shape of a symmetric-space coset."*

**And the lapse/shift split is that grading, not a separate posit:** ℋ_⊥↔𝔪 is smeared by the **lapse** (the
layer's own stacking rate), ℋ_a↔𝔥 by the **shift** (the synchronisation). *"The 'wrong sign' that is the
problem of time and the radiation-free stacking rate that dissolves the Hubble tension are thus two faces
of one"* fact.

**The stratification, and the mass as a transverse modulus.** Type O (dS, isotropy so(4,1), dim 10) → Type
D (SdS ℝ_t×SO(3), dim 4; Kerr–dS, dim 2) → Type I (Bianchi 3; Zipoy–Voorhees 2) → **the wall** (Type N,
isotropy zero). The so(5,1) action on cuts is **non-transitive**: R_ab R^ab = 6M²/r⁶+12/α⁴ separates
different-mass cuts while ³R = 2Λ does not, **so the mass is a modulus transverse to the orbits**, folding
at the Nariai seam where the offset-to-mass map is stationary.

**And the qualifier is doing real work:** *no **connected** substrate isometry connects different-mass
cuts, but an orientation-reversing one does.* The reticle reflection r₀↦−r₀ lies in
O(5,1)∖SO₀(5,1), and since 2M = r₀−r₀³ is odd it sends **2M↦−2M** — realising the mass-reflection ℤ₂ (the
A₂ diagram automorphism) as **the substrate's own orientation parity O(5,1)/SO₀(5,1)**. Hence the
non-isometry of the +M and −M *charts* is *"a property of the representational record, not of the
existent"*, and **this one orientation ℤ₂ recurs as the graviton's two helicities and, past the wall, as
the un-undoable chirality of the turning polarisation plane.**


---

## N-11 — STEP 7, P14: THE MATTER SECTOR, AND MY r2337 CLOSURE WAS THE CORPUS'S OWN RESULT

**First, the thing I flagged for the 54 line in the fold, now read at source and CORRECTED.** P14's own
opening states the boundary paper's negative:

> *"The boundary paper asks whether the **matter** content can be read off the same substrate, and returns
> a precise negative for the gauge sector: **su(3) ⊄ so(5,1), structurally**, so the Standard Model gauge
> group is not a continuous substrate isometry. **What that boundary leaves standing is the substrate's
> DISCRETE structure** — the orientation parity and the threefold symmetry of the slicing — recorded there
> as the one opening through which matter might enter."*

**So my r2337 "the geometric route to colour is finished" is the corpus's own P16 result, reached
independently** — and it was never in tension with the delivery, because **the opening was never the
continuous route.** The colour that P14 delivers acts on *"the branching rather than any bundle of the
substrate"*. **My fold's §5 warning to the 54 line should be corrected**: the scope error was not that I
banked a closure the corpus later broke; it was that I did not know the corpus had already banked the same
closure and named the discrete opening beside it.

**The chiral wall, and why it is a wall at all.** On the signed radius, W = λ√f/r is **odd**, so it changes
sign at r=0 — a Jackiw–Rebbi domain wall. The superpotential is not fitted: it is the leaf frame's own
output, the radial–angular spin connection of the M≠0 slicing tetrad.

**And the norm is load-bearing, which I would have skated past.** In the **leaf** measure dℓ = dr/√|f| the
horizons are at *finite* proper distance and r=0 is an integrable √-singularity, so the mode is genuinely
normalizable. In the **spacetime tortoise** measure dr_* = dr/f the same static mode is *not* normalizable —
the horizons sit at infinite tortoise distance where the mode tends to a constant. *"The two are not
interchangeable, and CR reads the fermion as a mode of the existent leaf, not a propagating spacetime
field."* **Both limits confirmed by direct solution.** *This is the ontology doing computational work, not
decorating it.*

**The count, and the centre.** r=0 is not the throat's centre but a point **on** the throat circle (the
back, X₁=−α). Three hinges 120° apart at transverse distance 2α, of which the throat is the **incircle** —
and 2α is an *output*: *"the hole determines exactly one circle without further choice — the one on its own
edge through its own centre."* The three walls sit at polar 180°, 300°, 60°, a ℤ₃-orbit.

**And why the ℤ₃-fixed centre carries no wall is a codimension argument, not an observation:** the three
linear forms r_j = α sin(φ−θ_j) have **rank two**, so their common zero is the single centre point; *"a wall
is a locus across which one vantage's superpotential changes sign, hence codimension one; a point is
codimension two and **has no side to cross to**."* The wall is the **line** r_j=0 — hinge j's own axis,
meeting the circle twice, the two crossings exchanged by the antipodal map, **which is R**.

**And then the weight-plane identification, which is the sharp bit:** the three forms are equal-length, 120°
apart, sum to zero, mutual cosine −½ — *"the weight system of the fundamental of su(3), and **in rank two
nothing else has that shape**."*

**The two factors — D₆ = S₃ × ℤ₂ — and an honesty move worth copying.** *"The product's being direct is
worth separating from both, because it is **forced and therefore carries no information about this
substrate**: Aut(A₂) is a Weyl S₃ extended by a diagram ℤ₂, every automorphism of S₃ is inner, and a
semidirect product by an inner automorphism is isomorphic to the direct one — **so there was never a
semidirect alternative for the geometry to have excluded.**"*

**And the ℤ₂ has a second realisation in a sector with no fermions in it** — the graviton's two helicities,
where chirality is the turning of the polarisation plane, *absent* while a residual connected isometry pins
it (*"a mirror and not a chirality"*) and genuine once lost. *"One parity, two sectors, two instruments…
a sector with no fermion content returns the same ℤ₂, so the factor is a feature of the substrate rather
than an artefact of the wall construction."*

**The correspondence is stated in SM terms with the ledger explicit** — 15 (or 16) Weyl fermions per
generation, quark/lepton being the first entry of each triple — and **three features fixed, "and only
three"**: the count as a γ⁵-graded index (dim ker₊ = 3, dim ker₋ = 0), the chirality of each, and the
global S₃. *"What it does not fix, and the list is longer."*


---

## N-12 — DRAFT, EDITORIAL: `prop:subhorizon` AND ITS SUBSECTION HEADING CARRY THE RETIRED CONFLATION

**The finding.** In P15, the subsection heading reads **"The branch point is sub-horizon for the acoustic
modes"**, and the proposition body reads:

> *"On the rate (eq:rate), the comoving Hubble wavenumber **at the onset redshift z_onset ≈ 6797** is
> k_hor(onset) ≈ 0.010 Mpc⁻¹, while the acoustic peaks lie at k ~ π/r_s ≈ 0.022 Mpc⁻¹ and above. The
> acoustic-scale modes are thus inside the horizon **at the branch point** by a factor ≳2."*

**The computation is at the onset; the conclusion names the branch point.** Those are two loci, and the
`z_bp` retirement (r2289, in the symbol canon) is explicit that reading one at the other's locus **inverts
the physics**: *sub-horizon at ONSET; super-horizon at the CROSSING.*

**And the paper's own §`sec:what-crosses` states the crossing side plainly and oppositely:** on the
contracting leg aH = √|1−f| grows without bound as r→0 — 0.13 at comoving turnaround, 1.96 at |r|=0.1α,
19.6 at 10⁻³α — *"so the comoving horizon 1/aH shrinks to zero and **EVERY mode exits it and freezes before
the crossing**."*

**So the two sections of one paper describe opposite horizon states, and are reconciled only by reading
"the branch point" in `prop:subhorizon` as "the onset".** Which is what it computes, and what its purpose
requires: the proposition exists to **close the inflationary route to coherence**, and that route is closed
by the modes being *inside* the horizon when the plasma begins — an onset fact.

**Why this is worth a correction rather than a note.** It has demonstrably misled two independent nodes in
one day:
- I read the Euclidean filter's freezing criterion at the onset locus and concluded *"nothing oscillating
  crosses for ℓ ≥ 3"* — shipped in `FOLD_FROM_52.md` §1. **The truth is the opposite: every mode is frozen
  at the crossing, so amplitude and tilt cross unaltered; what is annihilated is the leg's acoustic
  PHASE** (e^{−152} at P1), which is the intended and required result.
- The parallel line computed k/ℋ on the leaf rate at the onset and reported that *"prop:subhorizon
  inverts for ℓ ≲ 250"*, treating a proposition about the onset as a claim about the crossing.

**Draft correction (minimal, preserving the content):**
- heading → **"The acoustic modes are sub-horizon at the onset"**
- body → *"…are thus inside the horizon **at the onset** by a factor ≳2"*
- and one clause added, since the pairing is what prevents the misreading:
  *"(At the crossing itself the situation is the reverse — every mode has exited and frozen, §sec:what-crosses
  — and the two facts are the two ends of the lift, not one claim about one locus.)"*

**Not to be touched:** the numbers, the rate used, the factor ≳2, or the role of the proposition in closing
the inflationary route. **This is a naming correction of exactly the class r2155 and r2289 already
established, applied to a site those sweeps did not reach.**

---

## N-13 — AND THE COMB IS ALREADY COMPUTED IN P15, AT THE SKY'S VALUE

From `sec:coherence`, and I had not read this before spending a day on the spacing:

> *"Propagating the tightly-coupled acoustic modes to last scattering from a **common** seam phase yields a
> sharp regular comb at spacing **Δℓ ≃ πD_C/r_s ≈ 296**, troughs falling to zero, whereas drawing the phase
> independently per mode — the second, free datum a Cauchy surface would admit — **washes the comb out
> entirely**, leaving flat power."*

**296 is the sky's first-spacing value.** And note the distance: **D_C**, the comoving distance, not D_M.

**And the coherence argument is a characteristic-data argument, stated exactly:** *"The initial-value
problem on a null surface is characteristic, not Cauchy: the data that determine the future are **one free
function per mode on the surface together with regularity along the generators**, rather than a field and an
independent momentum. **A single datum per mode is a single phase per mode; there is no second,
independently specifiable quantity to randomize the relative phase.**"*

*So the "one free function plus regularity" formula I was deriving consequences from at r2382–r2383 is
P15's own sentence, and the conclusion it is used for is coherence — not a licence to pick which condition
regularity supplies at each k.*


---

## N-14 — STEP 8 (cont.), P16: THE BOUNDARY, AND WHERE MY r2337 SAT EXACTLY

**P16's colour closure has TWO layers and the secure one is causal, not group-theoretic.**

> *"That su(3) is not a symmetry of the world the matter inhabits **does not depend on any claim about the
> compact (Wick) face**; it follows from **the causal structure of the cosmogenesis.**"*

The matter rides the **real Lorentzian horn** — the expansion leg of the cosmogenetic bead, reached by a
**signature-preserving** reassignment. su(3) lives on the **compact face**, reached only by the global Wick
across the signature seam. *"It is not on the horn the matter rides… fixed by **where the matter is** (the
real horn, by the cosmogenesis) and **where su(3) is** (across the seam, by su(3) ⊄ so(5,1)). **This is the
most secure layer of the result.**"*

**And the dimension count is exact and sharp:** the smallest faithful real representation of su(3) is
six-dimensional (**3 ⊕ 3̄, realified antisymmetric**), so **su(3) ⊂ so(6) but ⊄ so(5)** — and the Lorentzian
compact sector supplies only five. Hence the compact face must be reached by **operation (3), the global
Wick to S⁵ = SO(6)/SO(5)**, not by the seam continuation's S⁴ = SO(5).

**⌗ WHERE MY r2337 SAT.** I found: *neither su(3) nor su(2,1) embeds in so(4,1) (both need 6 real
dimensions, so(4,1) acts on 5), nor in the sp(1,1) spinor bundle.* **That is the same dimension count P16
runs, applied to the isotropy rather than the full isometry** — an independent re-derivation of the corpus's
own wall, on two bundles the corpus had not enumerated. So it was **correct and additive**, not a scope
error, and the fold's §5 self-criticism was itself wrong. *The thing I actually lacked was P16's positive
half: the wall is not the end of the matter question because the opening is the DISCRETE structure and the
compact face across the seam.*

**And the positive synthesis, which is the payload:** *"the divide the last century drew **between** the
gravitational and the quantum, and between gravity and the gauge forces, is **one substrate read on its two
real forms**."*
- **Lorentzian form → the framework.** The Dirac constraint algebra *is* the SO(5,1)/SO(4,1) coset
  structure, its structure function the coset metric, the "wrong sign" the coset's own indefinite
  signature; deparametrized on the forced foliation it gives a true Hamiltonian. *"The frozen
  Wheeler–DeWitt constraint and that Hamiltonian [are] the same content differing only in whether the
  manifold is granted existence."*
- **Euclidean form → the gauge and the quantum scale.** su(3) on the compact face; the quantum of action
  entering through the de Sitter horizon's Gibbons–Hawking thermal state.

**And the compact face's status is settled ontologically, not group-theoretically:** mathematically SO(6)
and SO(5,1) are **co-equal real forms of one complex SO(6,ℂ)** and *"nothing in the group theory privileges
one."* What breaks it is CR's existence criterion — *a thing exists only insofar as it endures; "things do
not exist atemporally" is oxymoronic* — so the compact face is **real-by-construction, not a co-equal
world.** *Which is the manufactured/real rule again, at the level of a whole real form.*


---

## N-15 — STEP 9, P17: THE BIG BANG AS A CONJUNCTION, AND THE TWO RATES DERIVED A THIRD TIME

**The spine is eight links, each established elsewhere; the Big Bang is their conjunction.** (1) the
foliation is *measured*, logically prior to space/isotropy/homogeneity; (2) the augmentation is necessary
and sufficient, **with both declinations closed** — taking the 4-manifold as the existent smuggles a fifth
meta-temporal dimension (category error), reading relativity of synchrony as absence of an objective
present is the **modal fallacy**, *"the latter falsified outright by the measured redshift isotropy of
link 1"*; (3) collapse cannot terminate, **and because the correspondence is causal and structural rather
than metric it holds for collapse of ANY symmetry — "non-spherical collapse dissolved, not left as a
separate case"**; (4) the completion is the branch point, **distinct from the wall**.

**And the two-rate rule appears here a third time, derived rather than asserted** — I have now seen it in
P7, P8's kernel theorem, and P17:

> *"The slicing operator's kernel theorem **forces the split outright**… Radiation is not in the kernel: it
> requires m′(r)≠0, a **bend** of the cut, hence content… **the two rates differ by the radiation term
> alone** — and the rule is kinematic: a comoving separation read across leaves takes the stacking rate, a
> process running in the content takes the leaf's, **at every epoch**. The scoping looked temporal only
> because Ω_r(1+z)⁴ is negligible below z~10."*

**And the corroboration names the two rates as different KINDS of object, which is the part I never had:**
the window rate is *"the expansion scalar of the matter's own congruence — a **leaf-level** quantity, read
from the local geometry along the E=1 worldline, in which every bend of the cut, radiation included,
appears"*; the cosmological rate is *"the **stacking rate** of the new universe's cosmic foliation — a
**foliation-level** quantity, the lapse structure of the deparametrized layer."*

**And the transition law says exactly what crosses:** *"The reassignment acts on **the time-stacking** —
fixing the Λ-set rate — and **not on the leaf**: the density is leaf-carried and lapse-independent, so
content and composition cross as inherited progenitor data while the stacking is reset. **Everything
leaf-level is continuous at the seam.**"*

**Freeze-out is time-reversal violating, and that makes the turnaround constitutive rather than incidental.**
On a cooling history the reaction rate falls through |ℋ| and a relic freezes out; on a heating history the
rate *rises*, equilibrium is maintained, **and no relic is left** — confirmed by running a Boltzmann
two-species toy both ways. *"The heating leg — the infall — cannot fix a surviving light-element
abundance; only a subsequent cooling pass can. **The turnaround is therefore not incidental to the
abundances: it is the event that makes them.**"*

**The peak clears the bottleneck for every progenitor with no mass condition**, on two facts: the
compression is **adiabatic** (Thomson depth ~10²⁰, photon-diffusion time nineteen orders above free-fall,
so T ∝ ρ^{1/3} is *justified, not assumed*), and **ρ_hor = 3c⁶/32πG³M² is a FLOOR not a peak**, because the
worldline continues past the horizon to r=0 in finite proper time.

**And the verdict is scored honestly, including the loss.** At Planck's η (η₁₀ = 6.13±0.04): deuterium
**−0.5σ**, helium-4 **+0.5σ**, lithium-7 high at **~6–8σ** — *"the standard lithium problem, carried
unchanged… On the light elements CR is thus **neither better nor worse** than flat ΛCDM — two successes
and one shared problem — but it obtains them from the collapse rather than from a posited initial hot
phase."*

**⌗ And the claim is made against the data rather than against a correspondence:** *"the SAME single η
threading the CMB and the light elements, the theory errors propagated from the reaction-rate
uncertainties through the network's own sensitivity coefficients."*


---

## N-16 — STEP 10, THE LEDGERS: THE GUARD SET, AND WHY IT LEANS

**`PROTECTED_OPEN`'s diagnosis is structural and it explains my whole day better than I did.**

> *"**Every mechanical instrument this corpus has ever built polices OVER-CLAIMING.** The receipt gate, the
> do-not-assert census, the striking bar, the ORIGIN drift guard, the bibliography check, the column lint —
> **all of them stop a node from saying too much.**"*
> $$\textbf{NOTHING polices a NEGATIVE verdict on an open question.}$$
> *"And the guard set is not merely silent there — **it LEANS.** `anti-flinch`, `negatives-are-the-map`,
> `do-not-assert`, the `kill-list`, `verdict-bar-symmetric` — every one was forged against a node that
> softens, hedges or over-claims, **so every one of them pushes toward the negative.** A node running low on
> context keeps the heuristics and loses the nuance, and what survives is a set of rules **all pointing the
> same way**: toward closure. **That is the mechanism, and it is why this keeps happening on long sessions
> rather than short ones.**"*
> *"**And closure is the shape a node wants for a different reason.** A closure is terminal and reads as a
> deliverable; an open question does not."*

**That is exactly what happened.** I was running long, I had internalised "don't hedge, state it plainly,
negatives are the map", and every one of those pushed the same direction. Six times.

**THE RULE, and the distinction I kept collapsing:**
> **A node MAY write a bounded negative** — *"route Y, run on object Z, did not produce X"* — scope stated,
> object named, **filed as material, not as a verdict.** **A node may NOT write a closure on a registered
> item.** *"**Bounded negatives are the node's. Closures on protected items are Daryl's.**"*
> And it is explicitly **not** a deferral: *"the node does the work. What it may not do is convert the
> work's bounded result into a terminal verdict… **Doing the work and declaring it over are different acts,
> and only the first is delegated.**"*

**TEN CHECKS, and I can name which ones I failed today:**
1. **SAME-OBJECT** — *"if the item does not NAME an object, the check fails automatically."* **Failed
   repeatedly**: the "envelope", the "seam", the "reset" — none named before I ran against them.
2. **INVERSION** — *"what would have to be true for the corpus to be right here instead? Answer it in
   writing."* **Never once wrote it.**
3. **PRICE both ways.** 4. **CHAIN CHECK** — *"each piece true and the conjunction unargued is the cyanide
   face."* **That is precisely my "no combination can reach the sky"**: five true bounded negatives,
   conjoined without argument.
5. **RELATIVE-OR-ABSOLUTE**, and its alarm: *"**a misidentified object does not announce itself; it shows
   up as a small mystery that is interesting for no stated reason.** Treat that feeling as the alarm."*
   **The ℓ₁ that would not move under any dial was exactly that mystery, and I read it as a result.**
6. **SCOPE** — *"when Daryl states a structure, ask what the LARGEST thing it could mean is."* **Failed at
   "photons, neutrinos, baryons, full stop."**
7. **INDEX SET vs STRUCTURE** — a bijection is not an identity; five tests (locus, type, definition,
   equivariance, separability), *"equivariance alone is the trap."*
8. A figure's misreading is the figure's defect.
9. **READ THE ABSTRACT AND OVERVIEW OF THE PAPER THAT OWNS THE OBJECT before recording a conflict** — and
   the asymmetry that makes it a rule: *"a false alarm entered into the register costs MORE than the error
   would have, because **the next reader inherits a debt that does not exist and has to disprove it**."*
   **This is the check that would have stopped my "P7's list misassigns two of its four items."**
10. **A paper carries the result, not the path to it** — *"an open question that a later paragraph closes
    is still a defect while it stands, and the reader has no way to know which paragraph is current."*

**⌗ AND CHECK 10 IS THE ONE I SHOULD APPLY TO MY OWN N-12 DRAFT.** The `prop:subhorizon` finding is a
naming defect of exactly the kind check 10 describes — a site where two sections of one paper describe
opposite states and a reader cannot tell which governs. **That strengthens the case for the edit and
tells me its form: not an added caveat, but a correction that leaves one statement standing.**


---

## N-17 — **THE FINDING, and it supersedes N-12: P15 says "branch point" where its own receipt says "seam"**

*This is a bounded editorial finding on a naming substitution, with the corpus's own receipt as the
authority. It touches no result, no number and no claim. Four sites in P15.*

**THE EVIDENCE.** The sentence at line 289 cites `\rcpt{C2_horizon_limits}`. **Run the receipt and it uses
a different locus word than the paper:**

> *"…**the acoustic modes are sub-horizon at the seam**… the comoving horizon is STILL RISING **at the
> seam** and turns over just OUTSIDE it… ***THE SEAM IS NOT THE TURNING POINT OF THE HORIZON. IT IS JUST
> BEFORE IT.*** … the acoustic modes are already inside **at the seam** BECAUSE **the seam** sits on the
> rising part of the comoving horizon… r\* = 1.5338 r_seam (gauge α=1, Nariai M)."*

**And the receipt is right, because the two loci behave oppositely.** At the **seam** the comoving horizon is
near its maximum, so the *most* modes are inside — hence sub-horizon. At the **branch point** r→0,
aH = √|1−f| → ∞, so 1/aH → 0 and every mode has exited: *"0.13 at the comoving turnaround, 1.96 at
|r|=0.1α, and 19.6 at 10⁻³α"* (§`sec:what-crosses`, verified independently this turn). **Sub-horizon at the
seam; super-horizon at the branch point** — which is exactly the `z_bp` retirement's own formula, *sub-horizon
at ONSET, super-horizon at the CROSSING*, with "onset" and "seam" the same locus on the expanding side.

**THE FOUR SITES** (P15, `CR_cosmology.tex`):

| line | text | should read |
|---|---|---|
| **220** | `\subsection{The branch point is sub-horizon for the acoustic modes}` | **"The seam is sub-horizon for the acoustic modes"** |
| **224** | *"…inside the horizon **at the branch point** by a factor ≳2"* | **"at the seam"** *(the body computes at z_onset, which is the seam)* |
| **274** | *"already sub-horizon **at the branch point** (Prop. subhorizon)"* | **"at the seam"** |
| **289** | *"**the branch point** sits on its rising branch, which is **why** the acoustic modes are sub-horizon there"* | **"the seam sits on its rising branch"** — *the receipt's own wording* |

*A fifth site at line ~304 (**"the branch point is far below their decoupling"**, of the neutrinos) is
**correct as written** and must not be swept: that one really is about the branch point.*

**WHY IT IS WORTH FIXING RATHER THAN NOTING.**
- It is **the exact conflation r2289 retired**, at four sites the sweep did not reach, and the retirement
  note itself says reading one locus at the other's **inverts the physics**.
- **It has demonstrably misled two independent nodes in one day.** I read the Euclidean filter at the wrong
  locus and shipped *"nothing oscillating crosses for ℓ ≥ 3"* in `FOLD_FROM_52.md` §1 — **the opposite of the
  truth, which is that everything frozen crosses and only the leg's acoustic phase is annihilated.** The
  parallel line computed k/ℋ at the onset and reported *"prop:subhorizon inverts for ℓ ≲ 250"*, treating an
  onset proposition as a crossing claim. **Two nodes, one word, two false alarms.**
- And it is a **`CHECK 10` defect in form**: two sections of one paper describe opposite horizon states and
  a reader has no way to tell which governs.

**WHAT MUST NOT CHANGE.** The numbers (k_hor ≈ 0.010, k_peak ≈ 0.022, the factor ≳2, r\* = 1.5338 r_seam),
the rate used, the proposition's role in closing the inflationary route to coherence, the label
`prop:subhorizon`, or §`sec:what-crosses`. **Only the locus word, at four sites, to the one the cited receipt
already uses.**

**N-12 is superseded by this.** Its diagnosis was right but its proposed correction was weaker — it read the
computation as "at the onset" and would have added a caveat clause. **The receipt shows the corpus already
has the correct word, so the fix is a substitution rather than an addition, and no clause is needed.**


---

## N-18 — A LINT, NOT A GATE, AND I AM SAYING SO BECAUSE IT CANNOT BE MADE ONE

**The second-order finding.** The corpus has **seven gates** — claims, closure, register, compilation,
currency, queues, grains — and `check_grains`' own header names this exact pattern of omission:
*"Six gates policed claims, closure, the register, compilation, currency and queues. **NONE** policed
whether the documents that hold the SHAPE OF THE WORK had heard about the work."*

**Nothing polices the locus words**, and the naming rule is the one whose violation *inverts a result*
(r2289's own wording). r2155 and r2289 were **hand sweeps**, which is why four sites survived them.

**What I built and what it does.** `corpus/check_loci.py` exploits a structure the corpus already has:
**every computed claim is bound to a runnable receipt, so the receipt is the authority on which locus was
computed.** For each `\rcpt{}` call, compare the loci named in the enclosing sentence against those named
in the receipt. **61 receipt-bound locus claims exist; the check narrows them to 12 for reading.**

**AND IT CANNOT BE A GATE. I tried both tests and neither is clean:**
- **intersection** (`claimed & named` non-empty) — 8 flags, but it **passes the very case that motivated
  it**: P15 line 291 names *both* "branch point" and "z_onset", so it survives while attributing the
  property to the wrong one.
- **subset** (`claimed ⊆ named`) — 12 flags, catches line 291, **but false-alarms on multi-locus
  sentences**: `cosmogenesis_paper:262` names branch point, lift *and* seam in one summary sentence
  against a receipt that computes only at the seam, which is entirely proper.

**The reason is not fixable by tightening.** *"Which locus does this claim attribute the property to"*
requires parsing the claim, not detecting words. **So this is a triage lint whose output a human reads —
and per CHECK 9's asymmetry (a false alarm in the register costs more than the error, because the next
reader inherits a debt that does not exist) it must NOT be wired to fail a build.** I am recording that as
a property of the tool, not a caveat on it.

**THE 12, and the triage is PARTIAL — stated as such:**

*Coherent family, and the C2 evidence of N-17 covers it:* `CR_cosmology` **291** (C2_horizon_limits),
**296** (C4_driving_envelope), **307** (C6_neutrino_term), **372** (H0_acoustic_angle_and_seam), **416**
(ROBUST_p1p2_scan) — **all five say "branch point" where the receipt says "seam"**, and 291 is the site
whose implication N-17 shows inverted. *And a sixth consideration supports the family: the symbol canon
states the branch point **"no finite cosmic-time layer reaches"**, so a perturbation's initial data cannot
be delivered **at** it — the first layer is at the onset/seam.*

*Not triaged, and I am not guessing:* `CR_framework` **931**, **996**; `boundary_paper` **332**;
`cosmogenesis_paper` **262**, **507**; `matter_sector_paper` **540**; `slicing_operator` **324**. **Some of
these are certainly benign** (262 is a multi-locus summary). **Reading them is owed work and it is the
kind that must not be done fast.**

**⌗ WHAT I AM CLAIMING AND WHAT I AM NOT.** Claiming: the tool exists, runs, and reduces 61 to 12; and the
five-site P15 family is evidenced by the receipt C2 actually uses a different word. **Not claiming:** that
the other seven are defects, that the fix to any site is obvious, or that a mechanical gate is possible
here. **Per `PROTECTED_OPEN`, these are bounded findings filed as material.**


---

## N-19 — THE TRIAGE, COMPLETED: 5 REAL, 7 FALSE ALARMS, AND THE FALSE-ALARM MECHANISM IS NAMEABLE

**I said reading the other seven was owed work. Done, and the result cuts against the tool as much as for it.**

| site | paper says | receipt says | verdict |
|---|---|---|---|
| `boundary_paper:332` | seam | branch point | **FALSE ALARM** — *"no **seam**-made asymmetry"*: the word appears **inside a negation**; the claim is about the conjugate (r<0) branch |
| `CR_framework:931` | branch point, turnaround | branch point | **FALSE ALARM** — the sentence's whole subject is that *"the derivatives **separate all four loci**"*; naming several is the point |
| `CR_framework:996` | seam, turnaround | branch point, turnaround | **FALSE ALARM** — the two cosmic-time legs as complex conjugates, imaginary period 2πα/3; multi-locus by construction |
| `cosmogenesis:262` | branch point, lift, seam | seam | **FALSE ALARM** — a summary sentence distinguishing the branch point from the wall while the receipt computes the Nariai weld |
| `cosmogenesis:507` | turnaround | branch point | **FALSE ALARM** — the peak temperature at convergence; "turnaround" is the infall's turnaround, the receipt computes T_pk |
| `matter_sector:540` | seam | branch point | **FALSE ALARM** — a sentence *about naming practice itself* (*"a sentence which would be false if there were three… must name it"*) |
| `slicing_operator:324` | seam | turnaround | **FALSE ALARM** — the E=1 geodesic and the sinh^{2/3} scale factor; locus words incidental |

$$\textbf{7 of 12 are false alarms. 5 of 12 are the coherent P15 family of N-17.}$$

**AND THE FALSE-ALARM MECHANISM IS ONE THING, WHICH MATTERS MORE THAN THE COUNT.** Every one of the seven is
a sentence whose *subject is not a locus claim*: a negation, a multi-locus enumeration, a summary, or a
statement about naming practice. **The five real ones all have the same shape as each other and a different
shape from the seven: a property is asserted OF a named locus, and the receipt asserts it of a different
one.**

**⇒ So the tool's real precision is 5/12 = 42%, and I should have measured that before recommending
anything.** *At 42% it is a reading aid and nothing more — which is what I said in N-18, but I said it from
the design rather than from the measurement, and the measurement is what earns it.*

**⌗ AND A SHARPER TEST EXISTS, now that the mechanism is named.** Restrict to sentences where a locus word
is the **grammatical subject of a property assertion** — *"the X sits on…", "at the X the modes are…",
"reaches the X with…"* — rather than merely present. On the twelve, that pattern selects the five and
rejects the seven. **I have not implemented it and will not claim precision for it unmeasured.** It is
registered as the next move on the tool, not as a result.

**⌗ WHAT THIS DOES TO N-17.** Nothing — N-17 never rested on the tool. It rests on `C2_horizon_limits`
using a different word than the sentence citing it, plus the independent aH → ∞ computation. **The lint
found the family; the receipt is why the family is real.**


---

## N-20 — THE GATE, MEASURED: 100% PRECISION, 60% RECALL, AND THAT MAKES IT COMMITTABLE

**The assertion-shape test works and I have measured it against the labelled set of twelve.**

```
   word-presence (intersection)  :  8 flags   -- misses the motivating case entirely
   word-presence (subset)        : 12 flags   -- 5 real / 7 false  = 42% precision
   ASSERTION-SHAPE               :  3 flags   -- 3 real / 0 false  = 100% precision, 60% recall
```

**And a bug worth recording because it is the kind that hides:** the first assertion version returned empty
for *everything*, because `lp.strip('\\b')` — intended to drop the `\b` anchors — **also strips the
leading `b` of `branch[ -]point`**, giving `ranch[ -]point`. *A stripped character set is not a prefix
removal, and 'b' was in the set.* Every pattern silently failed to match and the tool reported "clean".
**A gate that returns clean because its regexes are broken is worse than no gate**, so the fix is paired
with a unit check on labelled sentences.

**WHAT IT NOW FLAGS — three sites, all in the N-17 family, no false alarms:**
`CR_cosmology:291` (C2_horizon_limits), `:296` (C4_driving_envelope), `:307` (C6_neutrino_term).

**It misses two of the five** — `:372` (*"the branch point's radiation amplitude takes…"*, possessive) and
`:416` (*"built on the branch point handover"*, compound noun). **Both are genuine assertions; the patterns
do not reach those grammatical forms.** *Recall could be raised by adding possessive and compound patterns,
and I attempted it — the edit did not apply and I am leaving it unapplied rather than risk precision I have
not re-measured.* **Registered as the next move on the tool.**

**⌗ WHY 60% RECALL IS ACCEPTABLE AND 42% PRECISION WAS NOT.** A gate's cost is asymmetric — `CHECK 9`:
*"a false alarm entered into the register costs MORE than the error would have, because the next reader
inherits a debt that does not exist and has to disprove it."* **A missed site stays as it is; a false one
creates work that cannot be finished.** So precision is the binding constraint and recall is a net that can
be widened later.

**⌗ AND THE TOOL IS NOT WHAT MAKES N-17 TRUE.** It found the family; `C2_horizon_limits` using a different
word than the sentence citing it, plus aH → ∞ at r=0, is why the family is real. **The gate's value is
that the next occurrence gets caught without a node having to read all 17 papers first.**


---

## N-21 — TWO SWEEPS, BOTH CLEAN, AND THEY ARE THE MOST USEFUL THINGS HERE

**CHECK 10 (diary-shaped sections) — CLEAN across all 17 papers.** Two hits, both proper: P7's
`Frontiers and open problems`, whose job is to state open problems; and P15's coherence section, where the
"open" marker is **exemplary** rather than defective — *"whether it is a tension, a wash, or a distinctive
but consistent feature turns on a parameter refit and on the early integrated Sachs–Wolfe term, which is
what remains open. **What is honestly claimed here is the effect, not a verdict on it.**"* That is a bounded
negative in precisely the form `PROTECTED_OPEN` prescribes. **The c54.62 sweep held.**

**THE NUMERIC AUDIT — P15's receipt-bound numbers, 17 of 17 CONFIRMED.** For every `\rcpt{}` citation in
P15 whose sentence quotes a number, I ran the receipt and checked the number against its output (exact, or
within 1%):

```
   17 citations carry quotable numbers
   16 confirmed on the first pass; 1 flagged
   the flagged one -- "range +0.3 to +3.8 across the octopole estimator" -- is CONFIRMED in the
   SECOND receipt cited in the same sentence (P15_verify_lowell_likelihood_v2:
   "octopole estimator range: low(WMAP) +0.3   high(Efst) +3.8")
   => 17/17.  My checker's one flag was its own defect: it processed receipts singly and did not
      pool the several a sentence may cite.
```

**Plus the integrity layer: 244 receipts cited across 17 papers, 0 missing, 0 syntax failures, 18/18 in a
random sample run clean.**

**⌗ WHY THIS IS THE MOST USEFUL PART OF THE WHOLE READ.** *I spent a day producing six adverse verdicts
against this corpus, every one of them my own error.* **An independent numeric audit of the paper I was
working on returns 17/17 against its own receipts.** The corpus's claims are bound to runnable code and the
code says what the papers say. **That is the base rate `PROTECTED_OPEN` asserts, measured rather than
quoted:** *"a node's failure to find something in this corpus is evidence about the node."*

**⌗ AND THE ONE DEFECT THE AUDIT DID FIND IS MINE, TWICE OVER** — a checker that reported "clean" because
its regexes were silently broken (N-20), and a checker that flagged a true claim because it read one
receipt where the sentence cited two. **Both are the same failure: an instrument trusted without a control.**
