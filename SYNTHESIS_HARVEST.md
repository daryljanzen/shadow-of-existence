---
name: synthesis-harvest
kind: WORKING
current: r4009
job: The harvest the synthesis paper is written from — every substantive result of the corpus, at its own register, with its home, its anchor, its joins, and what it is NOT operative for. Read WHILE BUILDING OR UPDATING THE SYNTHESIS, and when working a frontier item that needs to know everything the corpus already holds about it.
---

# The Synthesis Harvest

> **▣ WHAT THIS IS.** *The reading record behind the synthesis paper. Every substantive result of the
> seventeen papers, the ledgers and the instruments, entered as it is stated at source, with the register
> the source assigns it. **It is not the paper.** The paper is written from this; this is what the paper
> can be checked against.*

> **⛔ IT IS A FORWARD DOCUMENT.** *It is ahead of the corpus by construction — that is its job. Where an
> entry disagrees with a paper, a ledger or a map, **the disagreement is the work product**: a finding to
> work, not a defect to fix in the harvest. `THE_CODA` §"The source answers back". **Never make the harvest
> compliant**, and "stale" is a word for the corpus, never for the instrument examining it.*

---

## THE SIX FIELDS — every entry carries all six

| field | what goes in it |
|---|---|
| **① CLAIM** | *the result **as the source states it** — verbatim enough that the entry can be audited against the source without re-reading the paper* |
| **② REGISTER** | *the source's own tag: ⊢ **EXACT** (an identity, no measurement enters) · ≈ **COMPUTED** · ≈ **MEASURED** · ? **NAMED-UNRUN** · **NOT CLAIMED** · **CONJECTURE**. **Take the tag from the source, never assign one.** Where the source assigns none, the field reads `UNTAGGED AT SOURCE` — which is itself a finding* |
| **③ HOME** | *paper and section, or ledger and row. One home; a result stated in three places has one home and two joins* |
| **④ ANCHOR** | *receipt id, ledger row, or **none** — and `none` is written, never left blank. A claim with no anchor is not a defect; an unrecorded absence of one is* |
| **⑤ JOINS** | *which other papers state it, need it, or would be changed by it. **This is the propagation set**: when the claim moves, these are the documents that move with it* |
| **⑥ NOT OPERATIVE FOR** | *what the claim does **not** reach, and what the test that established it was blind to. **A face that is not operative somewhere is exactly as load-bearing as one that is** — `THE_CODA` §"The negatives are the map". Branches walked and found closed are entered here and never deleted* |

**⌗ Why ⑥ is not optional.** *Without it the harvest records only the turns that worked, and the synthesis
re-enters traps the corpus already walked. The blindness is the reusable part: it is what stops the next
pass re-running a test that could only ever return one answer.*

**⌗ Why ⑤ is what makes the arc work.** *Daryl's aim is that resolving a frontier item updates the synthesis
**and the documents it synthesises, all at once**. That is only possible if each claim already carries the
list of documents a change to it must reach. The joins field is that list, built during the read rather
than reconstructed after it.*

---

## THE ENTRY FORM

```
### <short handle>
① CLAIM      — <as stated at source>
② REGISTER   — <tag>
③ HOME       — <paper §section | ledger row>
④ ANCHOR     — <receipt id | ledger row | none>
⑤ JOINS      — <papers/ledgers that state, need, or would be changed by it>
⑥ NOT OP FOR — <what it does not reach; what its test was blind to>
```

---

## THE HARVEST

*(Entries land here as the read proceeds, grouped by source document in the read order of the arc.
Nothing is entered from memory: an entry is written with the source open.)*

---

# P1 · `corpus/BH_causality_v2.tex`
### *The event horizon is a metric singularity: a missing definition in general relativity, and the black-hole problems it dissolves*

> **▣ THE PAPER'S OWN FLOOR, which governs how every entry below is to be read.** *P1 stands on standard
> Lorentzian and causal structure alone — no substrate, no foliation, no augmentation, no reassignment. Its
> citations to the rest of the corpus are forward pointers and never dependencies. **So no entry here may be
> strengthened by anything downstream**: when a later paper extends one of these results, that extension is
> the later paper's claim and not P1's.*

### metric-singularity-theorem
① CLAIM — Two events null-separated ($\Delta s^2=0$) and spatially coincident ($\Delta x=0$ in the sense that they and every point of the joining null geodesic share one value of an invariantly-defined spatial coordinate) have vanishing temporal separation, $\Delta\tau=0$. They are *metrically coincident* while remaining topologically distinct and causally ordered. Two of the three separations vanishing forces the third.
② REGISTER — **THEOREM**, proved. The paper states the proof is trivial once both hypotheses are in view and that the triviality is the content: it isolates the extra condition turning an ordinary null relation into a metrically singular one.
③ HOME — P1 §1, `thm:metric-singularity`.
④ ANCHOR — `P01_metric_singularity_algebra` (carries the invariant-separation half in §3).
⑤ JOINS — [[p2-janzen-circle]] (classifies this as the finite-curvature species of one genus) · [[p3-sds-slicing]] (the metric singularity as geometric cause of the horizon/centre asymmetry) · [[p7-cr-framework]] (Null-Boundary Correspondence; the bead) · [[p17-geometric-core]] (the substrate's everywhere-real null boundary rests on this) · [[p10-canonical-time]] (finite curvature is what makes the regular Euclidean state available).
⑥ NOT OP FOR — **Does not apply to an ordinary null hypersurface.** A past light cone satisfies (a) and fails (b): it carries real spatial depth and nonzero temporal separations. The paper states this against the generic case explicitly and repeatedly. **Does not merge the events**: metric coincidence is a fact about the measure, not about the point set, and the affine parameter still distinguishes them. **Says nothing about events on different generators** — those fail hypothesis (a) and are not events the theorem relates.

### threefold-structure
① CLAIM — A metric singularity carries four properties: topological distinctness, strict null causal order $p\prec_\partial q$, geometric coincidence (null separation), and — under the additional spatial coincidence — metrical coincidence. An ordinary null hypersurface has the first three and not the fourth.
② REGISTER — **COROLLARY**, proved. `cor:threefold`.
③ HOME — P1 §2.
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] (the genus and its second species).
⑥ NOT OP FOR — Without spatial coincidence the temporal separation assigned by a smooth temporal function has **no invariant meaning at all** and may be altered arbitrarily by smooth local deformations. So (iv) is not a strengthening of (iii); it is what makes any temporal statement invariant in the first place.

### horizon-is-a-metric-singularity
① CLAIM — Every horizon-crossing event occurs at the same areal radius $r_h=2GM/c^2$; the areal radius is an invariant (defined by the area $4\pi r^2$ of the symmetry spheres, chart-independent); so hypothesis (b) holds along each generator and $\mathcal H^+$ is a metric singularity.
② REGISTER — **PROVED**, by application of the theorem. Two routes given and stated to agree: the geometric one above and the algebraic forcing below.
③ HOME — P1 §3.
④ ANCHOR — `P01_metric_singularity_algebra`.
⑤ JOINS — [[p3-sds-slicing]] · [[p7-cr-framework]] · [[p15-cr-cosmology]] · [[p17-geometric-core]].
⑥ NOT OP FOR — **The angular direction.** Two events on different generators are spacelike-separated across the horizon 2-sphere; the paper states this is neither a residual uncollapsed extent nor a weaker sector but simply not what the metric singularity is. The collapse is total *along every generator*, and that is the whole of the structure.

### algebraic-forcing-in-every-chart
① CLAIM — In any coordinates with $r$ the areal radius, along a generator $dr=d\theta=d\phi=0$, so $ds^2=g_{tt}dt^2$; the generator is null and $dt\neq0$, forcing $g_{tt}=0$. No metric component is specified anywhere in the argument, so the conclusion is forced **in every chart** rather than checked chart by chart. Invariantly the vanishing quantity is $|\zeta|^2=g(\zeta,\zeta)$, the squared norm of the timelike Killing vector — a scalar, of which "$g_{tt}=0$ in this chart" is the reading. Independently $|\nabla r|^2=g^{rr}$ vanishes at $r_h$, so the exterior's spacelike radial direction degenerates onto the null generator.
② REGISTER — **PROVED**, and run explicitly in Painlevé–Gullstrand, the chart used to argue nothing singular happens at the horizon: the finite $\Delta T$ there is the nonzero increment the null condition requires the coefficient to annihilate, not a counterexample.
③ HOME — P1 §3.
④ ANCHOR — `P01_metric_singularity_algebra`.
⑤ JOINS — [[p3-sds-slicing]] · [[p8-slicing-operator]] (the lapse's ontological reading).
⑥ NOT OP FOR — **Does not deny the finite coordinate increment.** A horizon-penetrating chart genuinely assigns two generator events distinct finite times; the argument is that the metric multiplies that increment by zero. The paper notes the sharper a slicing insists on finite time-extent, the more directly it exhibits $g_{TT}\to0$. **And it is not the infinite-redshift or Killing-horizon statement**: those are properties holding *at* the surface and are compatible with reading the horizon as an extended null hypersurface persisting in time; the metric singularity is the relation *between* distinct events on one generator.

### killing-horizon-extension
① CLAIM — The forcing is not special to Schwarzschild: it holds at any Killing horizon. Generators are orbits of the horizon-generating field $\chi$ ($\chi=\partial_t$ for Schwarzschild, $\chi=\partial_t+\Omega_H\partial_\phi$ for Kerr), null there. In coordinates adapted to $\chi$ the interval along a generator is $ds^2=|\chi|^2d\tau^2$ and $|\chi|^2=0$ is forced as before; lying on one orbit of the invariantly-defined $\chi$ **is** the spatial coincidence (b) requires. The Kerr event horizon is a metric singularity by the same argument.
② REGISTER — **PROVED**.
③ HOME — P1 §4, opening.
④ ANCHOR — none.
⑤ JOINS — [[p9-range-paper]] (Kerr–NUT–(A)dS as the separable kernel) · [[p7-cr-framework]] (non-spherical collapse dissolved rather than deferred).
⑥ NOT OP FOR — **The static lone-survivor reduction fails for Kerr**, and the paper says why: the generator twists in the static azimuth and $g_{tt}$ there is nonzero, its vanishing locus being the ergosphere, which lies outside the horizon except at the poles. The structure carries over; that particular reduction does not. **And the radial collapse/merger construction of §4 is carried out in Schwarzschild only**, by declared restriction.

### horizon-as-fixed-point-and-surface-gravity
① CLAIM — In ingoing EF coordinates outgoing null rays obey $\dd r/\dd v=f(r)/2$, whose equilibria are exactly the zeros of $f$: a generator sits at $r_h$ because $r_h$ is a fixed point of that flow. The eigenvalue is the surface gravity, $\dd r/\dd v\simeq\kappa(r-r_h)$ with $\kappa=f'(r_h)/2$, so neighbouring rays separate as $e^{\kappa v}$ and the fixed point is hyperbolic exactly when $\kappa\neq0$. Between consecutive simple zeros $f$ does not change sign, so $f'$ alternates: the Schwarzschild–de Sitter black-hole and cosmological horizons are necessarily a repeller and an attractor with fixed-point indices summing to zero. **The alternation is forced by the intermediate value theorem, not by the metric.** The Nariai member is where the hypothesis fails — the roots merge, both eigenvalues vanish, and the degenerate fixed point carries the index the pair had between them.
② REGISTER — **PROVED / RECEIPT-ANCHORED.** The paper's own framing: the horizon's invariant spatial constancy and its surface gravity are one statement about one fixed point, read at zeroth and first order.
③ HOME — P1 §3.
④ ANCHOR — `I53_the_two_horizons_are_a_repeller_attractor_pair_and_the_alternation_is_forced`; ledgers `index_theory`, `integrable_systems`.
⑤ JOINS — [[p3-sds-slicing]] (the horizon cubic and its root-exchange involution) · [[p5-groupoid]] (Nariai as the unique fixed point of $\sigma$) · [[p7-cr-framework]] (the tangency trichotomy forcing the Nariai condition) · [[p15-cr-cosmology]].
⑥ NOT OP FOR — The alternation is **generic to any function with simple zeros** and therefore says nothing metric-specific; the paper is explicit that this is not a result about the Schwarzschild–de Sitter metric. Its force is the *degenerate* case, where the hypothesis fails.

### exterior-slicings-never-reach-the-horizon
① CLAIM — For any asymptotically flat, globally hyperbolic spacetime with $\mathcal H^+=\partial J^-(\mathscr I^+)$, any future-complete exterior worldline $O$ and any smooth Cauchy temporal function adapted to it: the past-light-cone cross-sections rise toward future infinity along $\mathcal H^+$, the level sets accumulate on it and become asymptotically tangent to its generators in direction, and **each finite slice lies entirely in the exterior**, meeting $\mathcal H^+$ only in the limit. The event horizon does not occur on any finite exterior time-slice; it occurs only as the null future boundary approached in the infinite-time limit.
② REGISTER — **PROPOSITION**, proved. `prop:causal-alignment`. The paper states it uses only global hyperbolicity, the defining property of the horizon, and the future-completeness of $O$ — **independent of the metric-singularity identification**.
③ HOME — P1 §5.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (the existence/occurrence distinction at the root of the cosmological ontology, reached empirically there and causally here) · [[p7-cr-framework]] (`prop:lapse-shift`; the augmentation) · [[p15-cr-cosmology]].
⑥ NOT OP FOR — **Concerns exterior-adapted slicings only** and, in the paper's own words, does not address the global structure of the spacetime beyond that domain. **And it is not an observational-limitation claim**: the slices extend well beyond the observer's past light cone and include everything taken as "out there now", and none of them intersects the horizon at finite $\Theta$.

### lapse-collapse-is-a-metric-step-not-a-causal-one
① CLAIM — In Schwarzschild the degeneration is explicit and its *magnitude* is fixed, which the causal proposition leaves open: $g^{ab}\nabla_a\Theta\nabla_b\Theta\to-\infty$ and the lapse $N\to0$. The sign is settled not by the tilt but by the adaptation condition $\Theta(O(\tau))=\tau+\text{const}$ — a fixed $\Theta$-increment realised over a vanishing lapse. Stationary check: $g^{tt}=-1/(1-r_h/r)\to-\infty$, $N=\sqrt{1-r_h/r}\to0$.
② REGISTER — **LEMMA**, proved. `lem:alignment`.
③ HOME — P1 §5.
④ ANCHOR — none.
⑤ JOINS — [[p8-slicing-operator]] (lapse as the existent's rate of advance) · [[p10-canonical-time]].
⑥ NOT OP FOR — **⛔ The paper flags its own scope here and the flag is load-bearing.** The accumulation, the directional alignment and the finite-time conclusion use causal structure alone; **the magnitude half rests on a metric fact** — the vanishing of the redshift factor $-g_{tt}\to0$. It is general to a Killing or causal horizon and not special to Schwarzschild, but it is a metric input. The paper records this as *the second such metric step, not the only one*, correcting a stronger reading that would make the metric-singularity identification the sole metric ingredient.

### no-completed-horizon-is-realised
① CLAIM — The event horizon is a *global* structure, its location defined only with respect to the entire future development. A present astrophysical black hole continues to merge and accrete; at each interaction the exterior to the future of the outgoing null hypersurface must be replaced by the solution carrying the new mass, energy and angular momentum, and the pre-interaction exterior cannot be extended across it without describing a counterfactual. Because general relativity is local, every outgoing generator of the realised exterior traces back to the pre-horizon worldtube, never to a completed horizon or interior. A horizon defined prior to an interaction is the horizon of an auxiliary solution assuming no further interaction. **Two independent routes agree**: the exterior foliations of §5, and this one read along the source's own generators.
② REGISTER — **ARGUED FROM STANDARD CAUSAL STRUCTURE**, no modification of GR. This is the premise the three dissolutions rest on.
③ HOME — P1 §6 opening (`sec:problems`).
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] (the first synthesis: the same distinction dissolving a wider family at one stroke) · [[p6-shadow-of-existence]] (dissolution by identity, not patchwork — rule R4).
⑥ NOT OP FOR — Scoped to **black holes causally accessible to the external universe**, in a universe of ongoing collapse and accretion. It is not a claim that no horizon can be completed in any spacetime — the eternal Schwarzschild horizon is completed, and is treated as thermal below.

### dissolution-penrose-and-censorship
① CLAIM — Penrose's theorem is a correct mathematical result whose hypothesis is a *realised* closed trapped surface interior to the event horizon. No completed horizon, hence no trapped surface it would enclose, is physically realised. Singularities are not *avoided* by new physics — they are rendered physically irrelevant by causal structure alone, the curvature singularity remaining a feature of a global extension the realised worldtube never instantiates. Cosmic censorship is correspondingly unnecessary: where no singularity is realised, none needs censoring.
② REGISTER — **DISSOLUTION**, on causal grounds alone. Explicitly not a correction of Penrose's mathematics.
③ HOME — P1 §6, *Trapped surfaces and the singularity theorems*.
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] (the infinite-curvature species) · [[p7-cr-framework]] (the dissolution census).
⑥ NOT OP FOR — Does not touch the theorem's validity, only its physical preconditions in the astrophysical domain.

### dissolution-hawking-radiation
① CLAIM — The Bogoliubov construction requires three things: a globally defined horizon, a completed causal structure joining $\mathscr I^-$ to $\mathscr I^+$ across it, and permanent loss of causal contact rendering the two vacua inequivalent. **The third has an exact criterion**: two Fock representations are unitarily equivalent precisely when $\beta$ is Hilbert–Schmidt (Shale), and a thermal $\beta$ fails at the infrared end, its $1/\omega$ tail making $\lVert\beta\rVert_{\rm HS}^2$ logarithmically divergent. The criterion supplies the conclusion rather than qualifying it — and is equally what makes the absence of a realised background decisive: *a criterion on $\beta$ has nothing to be applied to when there is no $\beta$ to compute.* None of the three is realised for a present astrophysical black hole.
② REGISTER — **DISSOLUTION**, on causal grounds; the unitary-equivalence criterion is a cited classical result (Shale 1962).
③ HOME — P1 §6, *Hawking radiation*.
④ ANCHOR — ledger `functional_analysis`.
⑤ JOINS — [[p10-canonical-time]] (the Hartle–Hawking state at the substrate's cosmological horizon) · [[p15-cr-cosmology]].
⑥ NOT OP FOR — **⛔ The scope statement is narrower than "black holes do not radiate" and the paper says the distinction is essential.** What is absent is *horizon-induced* radiation. Local particle production not requiring a horizon — strong-field vacuum polarisation and the like — is untouched and not excluded; a perpetually collapsing ultra-compact body need not be quiescent.

### the-criterion-is-completion-not-perspective
① CLAIM — An argument of the form "the horizon is perspectival, therefore no thermal flux" is refuted before it starts, and is **not** the argument P1 makes. The Rindler horizon is observer-dependent *and complete* — the boost field is an exact Killing field of the whole spacetime — and the Unruh spectrum is thermal. Across the four horizons the programme names, the sorting is clean on one criterion only: Rindler (complete, observer-dependent) thermal; the substrate's cosmological horizon (complete, observer-dependent) thermal, carrying the Euclidean state; eternal Schwarzschild (complete, observer-independent) thermal; the collapse horizon of a present astrophysical black hole (never completed) the one case with no realised background. **Observer-dependence sorts the first two wrongly; completion sorts all four.**
② REGISTER — **RECEIPT-ANCHORED** sorting argument. The paper presents it as what fixes which criterion is doing the work.
③ HOME — P1 §6, *Hawking radiation*.
④ ANCHOR — `P1_the_unruh_case_is_what_makes_the_criterion_completion_and_not_perspective`.
⑤ JOINS — [[p10-canonical-time]] (the Hartle–Hawking state at $\kappa=1/\alpha$) · [[p6-shadow-of-existence]] (perspectival readings and what they do and do not license).
⑥ NOT OP FOR — **This is a self-imposed constraint on the programme's own rhetoric, and it is the most reusable thing in the paper.** It rules out an argument the framework might otherwise be tempted into everywhere: perspectivalness alone never licenses denying a physical effect. **Does not claim a derivation of the Unruh effect from the substrate**, and does not claim any new temperature value.

### nariai-kappa-zero-and-the-missing-exponential
① CLAIM — The member a collapse reaches on this construction is the Nariai one, at which $f$ has a double root and $\kappa$ vanishes. So the thermal flux is absent twice over, for independent reasons: because no completed horizon is realised (this paper's argument, independent of which member is reached), and — granting completion for the sake of the objection — because $\kappa=0$ at the member completed. **The sharper statement is about mechanism, not value**: near a simple root $f\sim2\kappa\delta$ makes $r_*=\int\dd r/f$ logarithmic and the approach $\delta\sim e^{2\kappa r_*}$, and it is that exponential relation between affine and Killing parameters that carries positive frequencies into a Planck spectrum. At a double root $f\sim c\delta^2$ gives $r_*\sim-1/c\delta$, a power law: **the construction has no first step to take.** The right statement is that the *mechanism is absent*, not that the temperature is zero.
② REGISTER — **RECEIPT-ANCHORED**, and the paper explicitly declines the stronger "temperature is zero" claim.
③ HOME — P1 §6, *Hawking radiation*.
④ ANCHOR — `P1_thermality_is_the_exponential_and_a_double_root_has_no_exponential`.
⑤ JOINS — [[p15-cr-cosmology]] (**the same $p=1$ vs $p=2$ split determines what crosses the branch point**: a non-degenerate horizon's exponential approach imprints a scale, the degenerate member's power law imprints none — one fact serving two purposes) · [[p7-cr-framework]] (the ringdown carrying no scale at that configuration).
⑥ NOT OP FOR — **The second argument is not offered as a replacement for the first.** A degenerate horizon is exactly where reading a temperature off $\kappa/2\pi$ is least safe — the near-horizon geometry is the equal-radii $\mathrm{dS}_2\times S^2$ throat, which carries a scale of its own — and **the two readings are not reconciled in this paper**. What is claimed is the coincidence and not a value. **And it does not say the configuration is athermal in every sense**: a scale-free power-law approach can still act on a spectrum, which is a different question from whether a Planck spectrum arises.

### de-sitter-accelerated-temperature
① CLAIM — On the substrate the accelerated temperature is $T(a)=\frac{1}{2\pi}\sqrt{H^2+a^2}$, reducing to $a/2\pi$ at large $a$ and to the Gibbons–Hawking $H/2\pi$ at rest. With $H=1/\alpha$ and $\alpha=\sqrt{3/\Lambda}$ the substrate's only dimensionful constant, the rest term is exactly the $\kappa=1/\alpha$ of the Euclidean state, and $T(a)=\frac{1}{2\pi}\sqrt{\alpha^{-2}+a^2}$ **carries no adjustable parameter**: the observer supplies $a$, the substrate supplies the rest. The structural difference from the flat statement is that the rest term does not vanish — an unaccelerated observer on this substrate is already in a thermal state, and acceleration adds to a bath rather than creating one.
② REGISTER — **CITED CLASSICAL RESULT** (Narnhofer–Peter–Thirring 1996; Deser–Levin 1997) read on the substrate's own constant. Parameter-freeness is a consequence of there being a single constant, stated as such and not as an additional assumption.
③ HOME — P1 §6, eq. `eq:unruh-ds`.
④ ANCHOR — none.
⑤ JOINS — [[p10-canonical-time]] (the horizon's thermal state closing the quantization ambiguity without a free parameter) · [[p17-geometric-core]] (one scale, constants as gauges).
⑥ NOT OP FOR — Not a derivation of the Unruh effect from the substrate, and not a new temperature value — both explicitly disclaimed.

### finite-curvature-makes-the-euclidean-state-available
① CLAIM — A regular Euclidean state exists at a horizon only if the Euclidean continuation is smooth there — no conical defect, curvature finite. That is precisely what this paper's distinction supplies: the horizon is a *metric* singularity, spatial measure collapsing while curvature stays finite, and **not** a curvature singularity at which no smooth Euclidean section would exist and no regular state could be selected. So the definition supplied here is what makes the companion's state available, and through it makes the imaginary-time segment of the cosmogenetic contour a well-posed object rather than a formal manoeuvre.
② REGISTER — **STATED as positive downstream work of the result**, and the paper flags it as not obvious from either side.
③ HOME — P1 §6, *Hawking radiation*.
④ ANCHOR — none.
⑤ JOINS — [[p10-canonical-time]] (Friedrichs extension closed by the horizon's own thermal state) · [[p7-cr-framework]] (`thm:bead`; the bounded contour $|{\rm Im}\,\tilde\tau|\le\pi\alpha/3$).
⑥ NOT OP FOR — **⛔ The paper corrects the obvious version of its own general point, and the correction is the useful part.** Finite curvature is *sufficient* for a continuation to cross a boundary but **not necessary**, and the construction crosses two boundaries of opposite type: at the horizon curvature is finite while the tortoise measure $r_*=\int\dd r/f$ diverges; at $r=0$, $f\to-2M/r$ diverges so **$r_*$ converges** while the curvature invariants do not. Each is crossable for opposite reasons. *What the two share is not a property but a negation: neither failure is a failure of both.* **The curvature criterion and the affine-measure criterion are independent** — stated against the habit of reading "singularity" as a single verdict.

### transplanckian-finite-at-each-time-not-bounded
① CLAIM — The trans-Planckian objection targets the Bogoliubov construction, which P1 does not perform, so it does not transfer as stated. But the reading here has a version needing no mode-tracing: a static observer at $r$ measures $\omega_{\rm loc}=\omega_\infty/\sqrt f$, and near a simple root the blueshift goes as $\delta^{-1/2}$, diverging only as the surface is reached — which §5 says is never reached at finite exterior time. **The available claim is "finite at each finite exterior time", NOT "bounded."** For radial infall $\delta\propto e^{-2\kappa t}$ so $\omega_{\rm loc}/\omega_\infty\propto e^{\kappa t}$: the supremum over exterior time is infinite. Taking $\omega_\infty\sim\kappa$, the exterior time at which the local frequency first reaches the Planck value is $\kappa^{-1}\ln(\kappa^{-1}/t_P)$ — about $2\times10^{-3}$ s at a solar mass, $2\times10^{-2}$ s at ten, and of order months for the heaviest resolved supermassive hole. *The logarithm suppresses nothing.*
② REGISTER — **RECEIPT-ANCHORED COMPUTATION**, with the weaker claim named and the stronger one refused.
③ HOME — P1 §6, *Hawking radiation*.
④ ANCHOR — `P1_the_transplanckian_claim_is_finite_at_each_finite_time_and_it_is_not_bounded`.
⑤ JOINS — [[p15-cr-cosmology]] · [[p11-dynamics]] (where the crossing question has its home).
⑥ NOT OP FOR — **⛔ This is the paper's own strongest self-limitation and it should survive into the synthesis intact.** The finiteness is *not* a suppression of ultraviolet physics but a statement about which limit is taken, and the regime is entered on a timescale short by every astrophysical measure. The claim that the conclusion needs no ultraviolet completion of gravity is a claim about **what the argument requires**, not that the late-time collapsing surface is free of ultraviolet physics — *"It is not, and this paper does not say it is."* Whether that regime is benign is not settled here and is not claimed. **And the exponential is the same $\kappa$ twice**: once as the mechanism of thermality, once as what carries the collapsing surface into the ultraviolet.

### dissolution-information-paradox
① CLAIM — The paradox arises only if a completed horizon forms and subsequently evaporates. Both premises fail together: no completed horizon forms, and with no horizon-induced radiation there is no evaporation to carry the loss. The realised spacetime remains globally connected — a global Cauchy surface, no hidden interior sector to trace over, unitary evolution unobstructed. The paradox is not *resolved* by a mechanism recovering information; **it does not arise**, because the spacetime it requires is never instantiated.
② REGISTER — **DISSOLUTION**, on causal grounds alone.
③ HOME — P1 §6, *The information paradox*.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] (the first synthesis' dissolution family) · [[p6-shadow-of-existence]] (R4, against patchwork).
⑥ NOT OP FOR — Approaches modifying the near-horizon state while retaining the completed-horizon background address a configuration the realised universe does not contain; P1 removes the premise rather than adjusting the response. It offers **no** information-recovery mechanism, because on its reading none is needed.

### black-hole-mechanics-status
① CLAIM — The zeroth/first laws and the area theorem are correct results whose object is a *realised* event horizon carrying a definite area and surface gravity. That object is never instantiated on a finite exterior slice, so no finite slice carries the area whose monotonicity the theorem asserts. The laws characterise the auxiliary completed geometry. The Bekenstein–Hawking entropy, **in the reading on which it is the entropy *of* that horizon**, shares their status.
② REGISTER — **DISSOLUTION by the same premise**, with a scope qualifier attached to the entropy claim at source.
③ HOME — P1 §6, *The laws of black-hole mechanics*.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] (the standing-problems family) · [[p10-canonical-time]].
⑥ NOT OP FOR — **⛔ An explicit open, stated at source and not to be smoothed over.** *"What content survives for a perpetually collapsing ultra-compact body — as with the local particle-production processes — is not settled by this argument."* The entropy claim is scoped to one reading of Bekenstein–Hawking and does not touch other readings.

### finite-curvature-case-and-what-p1-does-not-treat
① CLAIM — The metric singularity is a locus at which the curvature remains **finite**. It is a different object from the one standardly called the curvature singularity at $r=0$, where the curvature invariants computed on the areal radius diverge. P1 establishes the first, with the event horizon as its exemplar, and says nothing about the second.
② REGISTER — **SCOPE STATEMENT**; that the two admit a common treatment, and what becomes of the divergence at $r=0$ under it, is established in the companion and not here.
③ HOME — P1 §2, "A word on scope".
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] (**owner of the genus**) · [[p7-cr-framework]] · [[p15-cr-cosmology]].
⑥ NOT OP FOR — P1 establishes the finite-curvature case and the horizon as its exemplar, and nothing about the curvature singularity at $r=0$ beyond noting that it is a different object. **⛔ AND THE STANDING RULE THIS ENTRY EXISTS TO CARRY — now the arc's Phase 0b, run on every paper as it is opened: P1 must be readable by any physicist with no corpus vocabulary at all.** It may name what it *supplies* the later papers, at the end; it may not *use* their terms. Every such term was cleared from its body at r4019 — substrate, seam, branch point, conjugate branch, throat, cosmogenetic bead, genus and species — and the physics said in ordinary language instead. **The same test applies to every paper: the corpus reads linearly, and a paper that leans on a term defined three papers later is not a paper a reader can enter.**

### p1-p4-deliberate-non-dependence
① CLAIM — P1 supplies the **structural** half of the augmentation's necessity and P4 the **empirical** half, and neither leans on the other: P1 reaches its distinction from standard general relativity alone, P4's result stands on causal structure alone and needs none of the cosmological evidence. **Because neither leans on the other, their convergence is evidence rather than construction** — a dependency between them would make the necessity circular. P1 also supplies its own epistemic floor (only the fixed causal past yields certain information — the M31 V1 example), which is a bespoke instance of the imperative P6 later states in general, reached here on causal structure alone.
② REGISTER — **STRUCTURAL RELATION**, declared in the paper's masthead and honoured in its text; the adjacent-and-negative citations are reciprocal (P1 §scope names P4 precisely to disclaim reliance; P4 returns it in kind).
③ HOME — P1 masthead and §1 footnote; §6 opening.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] · [[p6-shadow-of-existence]] (draws on P1's instance without circularity) · [[p7-cr-framework]].
⑥ NOT OP FOR — **The forbidden thing is leaning for support, not reference.** Forward citations that disclaim reliance while naming what P1 supplies are permitted and used. **⛔ For the synthesis this is a constraint on presentation, not only on logic**: any section that presents P1 and P4 as a joint argument, or lets one carry weight for the other, destroys exactly the independence that makes their agreement evidential.


---

# P2 · `corpus/janzen_circle_v3.tex`
### *One circle, two poles: the Schwarzschild horizon and $r=0$ as critical points of a single curve*

> **▣ P2'S FLOOR.** *P2 may use P1's metric singularity and defines its own singularity taxonomy on its own
> geometry. **Its falsification rests on the analytic structure of $r(z)$ alone** and on nothing later. Its ring
> is its own subject, claimed at the end. Entries below are P2's; where one names a companion result, it names
> it as the companion's.*

### the-cycloid-and-its-two-critical-points
① CLAIM — The Schwarzschild interior in Lemaître–Tolman cycloid coordinates has areal radius $r(z)=M(1+\cos z)$, $z\in[0,\pi]$, with $r=2M$ at $z=0$ and $r=0$ at $z=\pi$, proper time $\tau(z)=M(z+\sin z)$ and horizon-to-centre proper time $M\pi$. Extended to $z\in\mathbb R$, $r(z)$ is $C^\infty$ and both endpoints are **non-degenerate critical points of identical analytic character**: $\dd r/\dd z=0$ at both, $\dd^2r/\dd z^2=\mp M$.
② REGISTER — **PROPOSITION**, proved, receipt-anchored.
③ HOME — P2 §2–§3, `prop:cycloid`, `prop:critical`.
④ ANCHOR — `P02_cycloid_and_critical_points`, `P02_interior_metric`.
⑤ JOINS — [[p1-bh-causality]] (supplies the metric singularity the two points are instances of) · [[p3-sds-slicing]] · [[p7-cr-framework]] · [[p17-geometric-core]].
⑥ NOT OP FOR — **The cycloid form is specific to vacuum Schwarzschild.** Charge, rotation and $\Lambda$ are not reached by generalising the cycloid, and P2 says so; the companions reach them by a different construction.

### the-identity-is-forced-by-a-circle-not-a-coincidence
① CLAIM — The identical character of the two critical points is not an accident of $M(1+\cos z)$. Since $r-M=M\cos z$ obeys $r''=-(r-M)$, the arc is the projection of uniform motion on the circle $(r-M)^2+s^2=M^2$, and the two critical points are its two $r$-poles. **Three independent readings of the same fact**: the circle is homogeneous, so has no distinguished point; it is the phase-space orbit of a harmonic oscillator at conserved energy $M^2/2$, so the critical points are the orbit's two turning points, exchanged by the time reversal $z\mapsto-z$; and it is a Thales circle on $[0,2M]$, so they are the two ends of a diameter, which has no preferred end.
② REGISTER — **PROVED**, with ledger support.
③ HOME — P2 §1 and §3.
④ ANCHOR — ledgers `integrable_systems`, `figure_theorem`.
⑤ JOINS — [[p3-sds-slicing]] · [[p5-groupoid]] (the discrete symmetry that exchanges the two ends).
⑥ NOT OP FOR — Homogeneity is of the *level set of a conserved quantity*, not of the spacetime. **The sole asymmetry between the poles is which value the chart's origin assigns each** — the geometry supplies none.

### one-curve-six-patches-and-two-beyond-kruskal
① CLAIM — Continuing $z$ into the complex plane at each critical point gives a single analytic curve, hyperbola–circle–hyperbola. At $z=0$, $z\mapsto\pm i\rho$ gives $r=M(1+\cosh\rho)\in(2M,\infty)$: **two** isometric asymptotically flat exteriors meeting at the bifurcation 2-sphere. At $z=\pi$, $z\mapsto\pi\pm i\rho'$ gives $r=M(1-\cosh\rho')\in(-\infty,0)$: **two** regions on $r<0$, both horizonless ($f=\coth^2(\rho'/2)>1$, no zero on $r<0$) and asymptotically flat as $r\to-\infty$. With the time-parity choice the curve carries six patches; the four at $r\ge0$ **are** the maximal Kruskal–Szekeres extension, and the two at $r<0$ are what Kruskal never reaches, having stopped at the $r=0$ turn.
② REGISTER — **PROPOSITIONS**, proved by explicit substitution; the metrics are checked against the standard Schwarzschild form in each region.
③ HOME — P2 §4–§5, `prop:region_I_metric`, `prop:back_seam_metric`, `prop:four_regions`.
④ ANCHOR — `P02_analytic_continuations`.
⑤ JOINS — [[p3-sds-slicing]] (identity of the $r<0$ arm) · [[p7-cr-framework]] · [[p13-boundary]].
⑥ NOT OP FOR — **The fragmentation into "regions" is a chart artefact, not a structural fact** — the $(r,t)$ coordinates degenerate at the two critical points and cut the single curve at exactly the turns. **And the continuation is of the curve.** P2 does not claim it is an extension of the Schwarzschild Lorentzian manifold; that distinction is what keeps the Sbierski concession honest.

### kretschmann-divergence-is-a-chain-rule-artefact
① CLAIM — $K(z)=48M^2/r(z)^6=48/[M^4(1+\cos z)^6]$ has a **twelfth-order pole** at $z=\pi$ and is finite ($3/4M^4$) at $z=0$. The pole order is the product of the critical point's multiplicity (2) and the power of $r$ in the denominator (6). **Corollary**: had the chart labelled the horizon critical point $r=0$ instead of $r=2M$, $K$ would diverge *there* and the standard classification would call the horizon a true curvature singularity. The divergence tracks the chart's labelling.
② REGISTER — **PROPOSITION AND COROLLARY**, proved.
③ HOME — P2 §6, `prop:Kretschmann`, `cor:Kretschmann_at_z0`.
④ ANCHOR — `P02_kretschmann_chain_rule`.
⑤ JOINS — [[p3-sds-slicing]] (what produces the asymmetric labelling) · [[p6-shadow-of-existence]] (a worked reclassification) · [[p17-geometric-core]].
⑥ NOT OP FOR — **⛔ P2 does not claim the divergence is unreal, and this is the single most misquotable result in the paper.** It is the curvature scalar of the Schwarzschild perspectival metric — the metric as a tensor field over the parameter $r$ — **real as that metric's, and marking a genuine curvature singularity**. What it is *not* is an invariant of the smooth manifold on which $z$ is natural. Any synthesis sentence of the form "the singularity is a chart artefact" overstates P2 and hands a hostile reader the paper.

### the-two-species-genus
① CLAIM — Both critical points are metric singularities of one genus — each a place at which the metric assigns no separation, drawn by the $r$-chart as an extended locus. The horizon is the **finite-curvature** species (P1's result, on independent grounds): the point worldlines pass *through*. $r=0$ is the **infinite-curvature** species: the point worldlines *end* at, where the construction is legitimately singular. **The difference sorts exactly by derivative order.** At zeroth order both collapse the ruler; at first order nothing distinguishes them (the lowest scalar invariant is second order, the connection is gauge, and the $r$-chart degenerates at both symmetrically); the first invariant that separates them is the curvature itself, second order. So the distinction is *sourced* at zeroth order in the single value the chart assigns each pole and *lands* at second order.
② REGISTER — **DEFINITION AND ARGUMENT**, P2's own, built on P1's finite-curvature case.
③ HOME — P2 §7.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] (the finite-curvature species) · [[p3-sds-slicing]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ The paper heads off its own tempting overstatement: the two are NOT identical as metrics.** A metric fixes curvature through its second derivatives and the curvature differs. And a reader testing the identity against the full interior metric finds the two behaving oppositely — $g_{tt}\to0$ at the horizon with the 2-sphere finite, against the 2-sphere collapsing at $r=0$ with $g_{tt}\to\infty$. P2 argues that opposition **is** the finite-versus-infinite distinction displaying itself, every one of those behaviours being a function of the single areal value the chart assigns; it is the signature of the identity, not a second distinction beside it.

### the-sweep-does-not-repair-either-point
① CLAIM — Recovering the full spatial geometry by sweeping the radial curve through the 2-sphere multiplies the points but does not make either critical point ordinary. At the horizon the swept sphere is ordinary (radius $2M$, area $16\pi M^2$) and events at different angles are genuinely spacelike-separated, while the collapse **along the generator** survives untouched — zero separation carried around an orthogonal symmetry is still zero. At $r=0$ the swept sphere itself degenerates, the collapse living in the angular sector instead. In both, the sweep adds no separation where the metric assigns none.
② REGISTER — **ARGUED**, and P2 marks it as where the standard picture quietly goes wrong.
③ HOME — P2 §7.1.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] (the angular sector is not what the metric singularity is) · [[p3-sds-slicing]].
⑥ NOT OP FOR — Consequently the horizon does not become a sphere of normal radius enclosing a normal interior, and **$r=0$ does not become a normal centre at which space tears**.

### the-falsification-of-the-inextendibility-inference
① CLAIM — The standard classification infers from the curvature divergence at $r=0$ that no continuation through it exists. **The continuation $z\mapsto\pi+i\rho'$ is a counterexample, and one counterexample refutes a universal.** It is the same analytic operation the standard treatment already accepts at $z=0$ as removing the horizon. So $r=0$ is a critical point the construction passes through, not a boundary at which it stops, and the divergence-to-terminus inference fails — **independently of any ontological reading**.
② REGISTER — **ESTABLISHED OUTRIGHT**, and P2 is explicit that this is what it establishes and the ontology is not.
③ HOME — P2 §8 and §8.5 (conclusion); the separation is made in §8.3.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] (the other end of the same asymmetry) · [[p3-sds-slicing]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ Three limits, all stated at source, and the synthesis needs all three.** ① It refutes the *inference*, not the singularity: the worldline still ends at $r=0$ and the curvature still diverges. ② **Sbierski's $C^0$-inextendibility stands untouched** — proved by causal-geometric arguments that never invoke the curvature divergence, and a continuation of the *curve* is not a $C^0$ extension of the Lorentzian manifold. P2 concedes this precisely and asks nothing of it. ③ It does not establish that the $z$-manifold is more fundamental than the $r$-chart; that remains a choice of reading.

### what-is-established-versus-what-remains-a-choice
① CLAIM — P2 separates the two explicitly, on the ground that running them together is what makes the result look weaker than it is. **Established**: the extendibility of the curve and the failure of the divergence-to-terminus inference. **A choice**: whether the residual divergence is a feature of the geometry or of the perspectival chart. The two readings agree on every observable in $r\ge2M$ and agree that the curve continues; they differ only on which of the $z$-curve and the $r$-chart is fundamental. What breaks the symmetry is supplied elsewhere — and P2 states the ground plainly: the perspectival reading **explains why** the chart labels two analytically identical points asymmetrically, where the standard reading must posit that asymmetry as brute fact.
② REGISTER — **ESTABLISHED / CHOICE**, separated by the paper itself.
③ HOME — P2 §8.3.
④ ANCHOR — none.
⑤ JOINS — [[p6-shadow-of-existence]] (**the reclassification constraint: an admissible reading must explain the appearance, not merely reproduce it**) · [[p3-sds-slicing]].
⑥ NOT OP FOR — **⛔ AND P2 REACHES THIS INSTANCE WITHOUT LEANING ON P6, WHICH IS THE POINT AND NOT A GAP.** An instance derived without the method that would later license it is a worked case on which that method's claim to track the world can rest **without circularity** — the same non-leaning relation P1 holds to P4. *For the synthesis: presenting P6 as licensing P2's move destroys exactly this.* **And the surviving objection is stated rather than dodged**: $K$ is coordinate-independent and its divergence resists relabelling — as the curvature of the perspectival metric. Whether that metric is fundamental is the very point at issue.

### the-ring-and-what-it-carries
① CLAIM — P2's own claim, made at the end. The single horizon exhibited here is the $\Lambda\to0$ degeneration of a root **triple**: for $\Lambda>0$, $f=1-2M/r-r^2/\alpha^2$ carries a horizon cubic whose cosmological root and backward-radial partner run to infinity as $\alpha\to\infty$, leaving one finite horizon with $r=0$ persisting throughout. **Horizon multiplicity is a reading of the cosmological constant.** Beside the root triple sits a second, independent triple in the structure function's *values*: on the forced member $(\dd r/\dd\tilde\tau)^2=1-f$, and the excursion's three critical loci sit at $f=0$ (seam, speed $\pm1$), $f=1$ (turnaround, speed $0$) and $f=2$ (interior Euclidean null, speed $\pm i$) — so $1-f\in\{+1,0,-1\}$ and **the three critical loci are the three causal characters**. The root triple grades position on the ring; these values grade causal character along it.
② REGISTER — **RECEIPT-ANCHORED for the $\Lambda\to0$ limit**; the readings built on the roots are named as the companions'.
③ HOME — P2 §8.4 (`sec:ring`).
④ ANCHOR — `P02_ring_lambda_limit`, `P02_the_approach_is_mass_free`, `P02_the_third_axis_is_two_poles`, `P02_bead_K_mass_free`.
⑤ JOINS — [[p3-sds-slicing]] (the horizon cubic and its involution) · [[p5-groupoid]] · [[p7-cr-framework]] (the closed excursion) · [[p13-boundary]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ The two triples are NOT claimed to be one structure**: no derivation producing $\{0,1,2\}$ from a single condition has been exhibited, and P2 says that until one is, the coincidence of the two counts is a coincidence of counts. **And the cycloid establishes only that the extra roots are the ones $\Lambda$ supplies** — everything read off them is the companions'.

### the-classical-seed-oppenheimer-snyder
① CLAIM — $r(z)=M(1+\cos z)$ is, term for term, the scale factor of a closed dust Friedmann–Lemaître cosmology, $a(\eta)=\tfrac{a_m}{2}(1+\cos\eta)$, with cosmic time $t(\eta)=\tfrac{a_m}{2}(\eta+\sin\eta)$ matching $\tau(z)$ under $M\leftrightarrow a_m/2$. **Black-hole collapse and a closed cosmos are one curve, not analogues** — the Oppenheimer–Snyder identity, read at the level of the vacuum areal radius rather than a matched dust ball. And the curve only ever decelerates: the radial acceleration is $-M/r^2$, Newtonian free fall, negative at every radius, so the cycloid has **no turning point of its rate**.
② REGISTER — **CLASSICAL**, cited to Oppenheimer–Snyder; requires nothing of the corpus.
③ HOME — P2 abstract, §1, and the §2 remark.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] · [[p15-cr-cosmology]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **The identity here is at $\Lambda=0$ and closed.** The turn belongs to a positive cosmological constant, not to the collapse: it appears only when the circle is carried to $\Lambda>0$. *This is the entry that lets the synthesis say where the collapse–cosmology identity starts without importing anything — it is visible in bare Schwarzschild.*

### p2-open-items
① CLAIM — Stated open at source: the complex parameter admits a **third axis**, $z\in\mathbb C$ generically, whose status P2 raises and does not settle; the cycloid form does not generalise to charge, rotation or $\Lambda$; and the ontological framing is offered as an alternative rather than as a derivation forcing it.
② REGISTER — **OPEN, stated at source.**
③ HOME — P2 §8.6 (limitations).
④ ANCHOR — `P02_the_third_axis_is_two_poles`.
⑤ JOINS — [[p3-sds-slicing]] · [[p9-range-paper]].
⑥ NOT OP FOR — The ontological limitation attaches **to the ontological claim only** and not to the falsification, which is established outright and independent of which manifold is taken as fundamental.


---

# ⚯ CROSS-PAPER JOIN · what $r=0$ finally is
### *A conclusion the corpus reaches in pieces and never assembles — and the forward references owed so that P2's care does not read as a retreat*

> **▣ WHY THIS BLOCK EXISTS.** *P2 declines to say the curvature divergence at $r=0$ is unreal, and that
> restraint is correct: at P2's floor the question is genuinely undecided. **But the corpus does not leave it
> undecided.** The verdict is assembled across four later papers and stated in full by none of them. Read
> linearly, P2's care therefore looks like a concession the programme never takes back — a hostile reader is
> handed "even they admit the singularity is real" with nothing downstream visibly recovering it. The join is
> real and the papers already contain every link; what is missing is the statement.*

### the-chain, link by link, each verified at its own source
- **P2** — $r=0$ is a non-degenerate critical point of $r(z)$, of identical analytic character to the horizon. The Kretschmann divergence is the curvature scalar of **the Schwarzschild perspectival metric**, real as that metric's. Whether that metric is fundamental is *stated as a choice the construction does not make*.
- **P3** — the choice is made on the geometry. The de Sitter description sweeps the complete arc about the manifold's own symmetry axis; the Schwarzschild description, viewing the hole from outside in the timelike orientation, **cannot use that axis and is forced to pivot on a selected off-axis point** — the critical point the chart labels $r=0$. The slicing closes *through* it, "a branch point and not a barrier, the substrate being smooth across the locus the chart labels $r=0$, the divergence of the curvature reading there a perspectival artefact of the areal coordinate."
- **P4 and P6** — supply the two things that make "perspectival" a verdict rather than a preference: an existing evolving world for the descriptions to be perspectives *of*, forced empirically; and the constraint that an admissible underlying object must **explain** the appearance rather than merely reproduce it.
- **P7** — perspectival geometries as readings of one substrate, from first principles, with the closure through $r=0$ established as a theorem.
- **P8** — the sharpest single statement in the chain, and it is about the cosmological face: *"$r=0$ is not a point matter emerges from; it is a horizon the slicing is anchored to."* The $t=-\infty$/$r=0$ singularity is the artefact of the comoving reading laid over a throat that is the substrate's own constant $\alpha$ — the radius-face of a doubled category error whose time-face is taking the chart's $-\infty$ for the physical age.

### the-terminal-claim, as the corpus's pieces actually support it
① CLAIM — The locus the Schwarzschild chart labels $r=0$ is **not a place in the world**. It is the conjugate critical point of a perspectival chart, reached by analytic continuation past the metric singularity, and the geometry is smooth across it. **The curvature divergence is real as the perspectival metric's and is not a curvature of the substrate**, which carries none there. So P2's undecided question is decided — against the divergence being fundamental — and decided on the geometry rather than by preference.
② REGISTER — **⛔ NOT STATED AS SUCH ANYWHERE.** Every link is established at its own source; the assembled claim appears in no paper. This is a join the synthesis makes, and then delivers back.
③ HOME — distributed: P2 §6/§8.3, P3, P7, P8.
④ ANCHOR — the links' own; the assembled claim has none, because it has never been stated.
⑤ JOINS — [[p2-janzen-circle]] · [[p3-sds-slicing]] · [[p4-modern-parallax]] · [[p6-shadow-of-existence]] · [[p7-cr-framework]] · [[p8-slicing-operator]].
⑥ NOT OP FOR — **The verdict is about the divergence's status, not about the worldline.** The infalling worldline still ends at that critical point in finite proper time, and **Sbierski's $C^0$-inextendibility of the maximal analytic Schwarzschild spacetime still stands** — it is a theorem about that object, and the substrate is a different object. Neither is touched by deciding the divergence perspectival.

### what-is-owed-back-to-the-papers
*Forward references, at the point each paper's own restraint is stated, saying where the question is settled and by what. **Not the conclusion imported** — the paper must still not claim it.*
- **P2** — where §8.3 says the construction does not choose between the readings, name that the companion supplies the geometric cause and finds the divergence perspectival, the locus being an ordinary point of the geometry it slices. **⛔ Phrased as "settled there, not here"**, never as support P2 draws on: P2's independence is what the next item protects.
- **P3** — its statement is already the pivotal one and is made in passing, inside a longer sentence. It carries the corpus's answer to P2's open question and deserves to be visible as that.
- **P7 / P8** — P8's formulation is the sharpest in the corpus and is scoped to the cosmological face. Whether the same sentence covers the collapse face is the thing to check when those papers are opened.

**⛔ AND THIS IS NOT THE P6 NON-CIRCULARITY POINT, though it touches it.** *That point: P2 reaches its
perspectival instance without leaning on P6, and that independence is what lets P6's method rest on it without
circularity. **This point**: P2's specific open question about $r=0$ is closed later, and the closure is never
stated. They pull in opposite directions at exactly one place — the forward reference owed to P2 must point at
where the question is settled **without** converting P2's independent instance into a lean. Both survive if the
reference says where the answer is and does not borrow it. Collapsing the two loses one of them.*


---

# ⚯ CROSS-PAPER JOIN · two independent routes to three hinges
### *P3 owes a forward reference that strengthens its own case, and the corpus has never put the two routes side by side*

① CLAIM — **The number three in the hinge figure is reached twice, by arguments that share no premise.**
**Route A (P3, algebraic).** The horizon cubic has three roots; a vantage is fixed by which root it reads as its own black-hole horizon; the roots are on the same footing, so the vantages are, and there are exactly as many — three, at $120^\circ$, with the root-permutation group relating them.
**Route B (p0/17, dimensional).** Written at general dimension the hinge figure is a regular $(D-1)$-gon with the throat as its incircle. **At $D=4$ that is a triangle.** p0 then separates which of the hinge relations are dimensional accidents and which are not: the tangent length equalling the hinge's height survives at every $D$ (both are $\sqrt{R^2-\alpha^2}$), as does midpoint tangency (a property of any regular polygon's incircle); what does **not** survive is the placement $R=2\alpha$, the $60^\circ$ subtense, and the throat's identification with the nine-point circle.
② REGISTER — **Route A: established in P3** (§8.1, as of r4029). **Route B: established in p0/17 — and, on the read, P3 already contains the $(D-1)$-gon generalisation too**, using it in its dimension section as a *check* on the $D=4$/$D=5$ result ("the hinge placement generalises to a regular $(D-1)$-gon with the throat as incircle, whose vertex distance returns the forced $2\alpha$ at $D=4$"). **⛔ So the gap is narrower and more specific than "the corpus lacks Route B": P3 has the generalisation in hand and never reads it back as an independent derivation of the count.** The joint claim — that three is forced twice over, algebraically and dimensionally — appears nowhere.
③ HOME — P3 §8.1–§8.2; p0/17's general-dimension treatment of the hinge figure.
④ ANCHOR — `alpha_alone`, `euclid7_nine_point`, `P03_the_sixth_equivalence` (Route A's figure); p0's own for Route B.
⑤ JOINS — [[p3-sds-slicing]] · [[p17-geometric-core]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ Neither route is evidence for the physical generation count, and the whole value of the pair is that they run the other way.** Both are prior to any empirical three: they fix a number on the geometry, and whether the observed generations are that number is a separate question owned by the matter sector. *The join's use is exactly this: it lets P3 say the three is necessary on geometric grounds **before** the empirical count is in view, so the agreement is a fit rather than a fitting.* An entry that presents the routes as confirming the generations inverts it.

### what-is-owed-to-P3
*A forward reference at §8.1, where the count is now derived: naming that a companion reaches the same figure
from the dimension and separates which of its relations are special to $D=4$~\cite{JanzenGeometricCore}.*
**⛔ Phrased as a second route and not as support** — Route A must stand alone, exactly as the derivation
now written does. P3 already cites the geometric-core paper in the $2\alpha$ paragraph for the circle's other
faces; **it does not cite it for the count**, which is the gap.


---

# P3 · `corpus/SdS-slicing-curve_v2.tex`
### *The de Sitter substrate and its slicing curve: horizons as turning points, de Sitter and Schwarzschild as two readings*

> **▣ P3'S FLOOR AND ITS LICENCE.** *P3 may use P1 and P2 and works in the perspectival reading P2 set out. It
> is the geometric machinery paper and is licensed to **overdevelop** — but every piece must be motivated by a
> question visible inside P3. As of r4029--r4033 it meets that test at the place it previously failed: **the
> number of hinges is now derived from the horizon cubic before any matter is mentioned.***

### the-slicing-curve-and-its-turning-points
① CLAIM — One radial curve $r(l)$ with $\dd r/\dd l=\sqrt{|f|}$, $f=1-2M/r-r^2/\alpha^2$. $\dd r/\dd l$ vanishes exactly where $f=0$: **the horizons are the turning points of the slicing curve** — non-degenerate at simple roots ($\dd^2r/\dd l^2=\pm\tfrac12 f'\neq0$), degenerate at the double root. Clearing the denominator gives the horizon cubic $r^3-r+2M=0$ in the gauge $\alpha=1$, whose three regimes are read off the single discriminant $4-3r_0^2$.
② REGISTER — **DEFINITION AND PROPOSITION**, proved.
③ HOME — P3 §2–§4, `def:slicing`, `prop:turning`.
④ ANCHOR — the section's own; the trichotomy is also read from the 2012 dissertation's discriminant.
⑤ JOINS — [[p2-janzen-circle]] · [[p8-slicing-operator]] (promotes the curve from classifier to generator) · [[p9-range-paper]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **Proper distance $l$ is derived, not the spine.** At the degenerate member the merging horizons stand infinitely far apart in $l$ (the integral diverges logarithmically) while the Gaussian curvature there is finite and the geometry regular — *a coordinate running to infinity where the invariant curvature is finite is reporting on the slicing, not on the manifold.* The spine is the signed $r$; the clock is the swing angle.

### alpha-is-the-invariant-and-is-never-sent-to-a-limit
① CLAIM — $2M=\alpha\bigl((r_0/\alpha)-(r_0/\alpha)^3\bigr)$ is **linear in $\alpha$ with a dimensionless slicing profile as its coefficient**, so $M$ cannot be held fixed while $\alpha$ varies without turning the slicing. Hence $\alpha\to\infty$ at fixed $M$ drives the profile to zero, which is a choice of reticle offset and not a limit of the geometry. **Schwarzschild is this substrate read at a small sky angle, not a limit of it.** The throat radius is the invariant — fixed under the reading-swap, across all slicings, and under the projection; $M$ is its slicing- and projection-dependent factor, bounded by $\alpha$. *Mass is a turning point, not a coefficient.*
② REGISTER — **PROVED**, and the prohibition is stated as a *consequence* of the mass section rather than as a stipulation.
③ JOINS — [[p17-geometric-core]] (one scale, constants as gauges) · [[p7-cr-framework]] · [[p15-cr-cosmology]].
④ ANCHOR — none.
③ HOME — P3 §1 and §10.4 (`sec:mass`).
⑥ NOT OP FOR — **⛔ This is the guard that stops the whole construction being read as "SdS with $\Lambda$ small".** Any synthesis sentence taking a $\Lambda\to0$ or $\alpha\to\infty$ limit of this construction dismantles the throat it lives on.

### the-root-exchange-is-a-symmetry-of-the-line-element
① CLAIM — The cubic factors cleanly when the slicing parameter is one of its own roots, $(r-r_0)(r^2+rr_0+r_0^2-1)=0$ with $2M=r_0-r_0^3$. The map carrying one root to another, $\sigma(r_0)=\tfrac12(-r_0+\sqrt{4-3r_0^2})$, is an **involution** with fixed point at $r_0=1/\sqrt3$ (the degenerate member). Because $f$ depends on $r_0$ only through $2M$, and both roots return the same $2M$, **the exchange leaves the metric function strictly unchanged**: it is a genuine symmetry of the line element, not a coincidence at one parameter value.
② REGISTER — **PROPOSITIONS**, proved. The involution's closed form is read from the 2012 dissertation's expression for the two further horizons, here read as a *map*.
③ HOME — P3 §5.1–§5.3.
④ ANCHOR — `P03_the_two_splits`.
⑤ JOINS — [[p5-groupoid]] (the complete within-geometry morphism group) · [[p12-algebroid]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ A second partition of the same triple runs alongside the designation split and the two are neither independent nor identical**, which P3 states rather than leaving side by side. They coincide exactly when $|r_0|>1$; the discriminating quantity is the offset, not the mass; and **at the degenerate member the designation split loses its content while the sign split stays sharp.** *Two structures that fail in different places are not two readings of one structure.*

### the-projection-fixes-the-parameter-and-forces-the-triple-angle
① CLAIM — The slicing parameter is fixed by the geometry of observation: the hole's image lies on the observer's celestial sphere, and a planar chart forces the **gnomonic** projection (orthographic excluded). The offset is then $r_0=\tfrac{2}{\sqrt3}\sin w$ with $w$ a genuine geometric angle, and the horizon relation is the **pure triple angle** $2M=\tfrac{2}{3\sqrt3}\sin 3w$, the slicing scale $2/\sqrt3$ forced as the unique value removing the residual harmonic. The throat carries a second genuine angle $u$ with $\sin u=\tfrac{2}{\sqrt3}\sin w$, and the chart involution and the cubic involution are **one involution in two coordinates**, conjugate by an explicit closed-form map.
② REGISTER — **PROPOSITIONS**, proved.
③ HOME — P3 §6.1–§6.3.
④ ANCHOR — the section's own.
⑤ JOINS — [[p5-groupoid]] (the sky angle as the cubic's Galois closure) · [[p17-geometric-core]].
⑥ NOT OP FOR — **Three parameters, each blind to something, and P3 declares all three at the outset rather than letting them blur.** $u$ is tied to one circle and cannot see which member is in play; $w$ collapses the three-fold structure into $\sin 3w$ and **folds the involution from view as a mere reflection**; $r_0$ is one number per seam and cannot see where on the lap one stands. *The full symmetry is reached only by carrying them coupled* — which is why the paper is written object-first, the swinging door being the thing and the three angles its projections.

### the-dimension-result
① CLAIM — The collapse to a pure multiple angle is available at $D=4$ and, up to a parity, at $D=5$, **and in no other dimension**: from six dimensions upward the harmonics standing below the top one number two or more while the construction has a single scale to spend. Two independent checks: the hinge placement generalises to a regular $(D-1)$-gon with the throat as incircle, whose vertex distance $\alpha/\cos(\pi/(D-1))$ returns the forced $2\alpha$ at $D=4$; and in both surviving dimensions the tangent from a hinge lands on the Nariai radius computed independently from the double root. **And the one input the extension formerly assumed is now obtained**: the $D$-dimensional $f$ was taken as the standard Tangherlini–de Sitter form, and the slicing operator's vacuum condition — the kernel of the matter functional on a cut — generalises without adjustment, $T^t{}_t=0$ giving a first-order linear equation whose *entire* solution space is that family with $M$ the single constant of integration.
② REGISTER — **RECEIPT-ANCHORED**, several.
③ HOME — P3 §6.2 (the dimension remark).
④ ANCHOR — `P03_dimension_collapse`, `P03_operator_at_general_D`, `P03_reach_probe_deepening`, `P03_step3_sweep`, `P03_step3_refused`.
⑤ JOINS — [[p8-slicing-operator]] · [[p14-matter-sector]] (which of $D=4$ and $D=5$ survives is settled there, on the parity of $2M$ in the signed offset) · [[p17-geometric-core]].
⑥ NOT OP FOR — **⛔ The separation of what is dimension-independent from what is decoration is the reusable part, and it cuts against the construction's prettiest facts.** Of the five equivalent hinge statements, the two that are the *substrate's* — tangent length equalling the hinge's height, and midpoint tangency — hold at every $D$; the three that are the *equilateral triangle's* do not, the nine-point identification failing because Euler's theorem is about triangles. *The load-bearing identity is on the dimension-independent side; what is dimension-specific is the decoration.* **Two inputs still remain**, stated at source: that the construction gauge's lock $g_{tt}g_{rr}=-1$ is enforced at general $D$, and that the transverse space is the round $S^{D-2}$.

### the-forced-pivot-and-what-it-produces
① CLAIM — The de Sitter and Schwarzschild descriptions are not two labellings of one swept geometry but **two sweeps of one curve**, differing in whether the sweep can be taken about the manifold's own symmetry axis. The de Sitter vantage sweeps the complete arc about that axis and breaks no symmetry. The Schwarzschild vantage, viewing the hole from outside in the timelike orientation, **cannot use that axis and is forced to pivot on a selected off-axis point** — the critical point the chart labels $r=0$. **This forced pivot is the geometric origin of the horizon-versus-singularity asymmetry P2 found algebraically.** There is not a second symmetry break here but one, cascading: the manifold's single broken symmetry is the hole, and an observer who takes the hole as reference is forced into everything that follows.
② REGISTER — **ARGUED**, and P3's own answer to the question P2 left open.
③ HOME — P3 §10.3 (`sec:sweep`).
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] (**this closes P2's stated-open question**) · [[p8-slicing-operator]] · [[p6-shadow-of-existence]] · the $r=0$ cross-paper join above.
⑥ NOT OP FOR — **⛔ P3 is careful about exactly what survives the sweep and this is easy to overstate.** The two critical points are *topologically* identical on the substrate — two matching turning points of one intrinsic curve — and **emphatically not metrically identical**, because the metric fixes curvature through its second derivatives and on the swept geometry that curvature is lopsided. *The identity is topological and lives on the substrate; it does not survive onto the geometry.* **And read the other way the same fact says how the construction PRODUCES a curvature singularity** — by the sweep about the areal origin and at no other locus, which is why none of them is fundamental.

### the-rigidity-and-the-two-distinct-operations
① CLAIM — The slicing curve is an **intrinsic curve on the de Sitter manifold**: the slicing parameter marks a point on it and the horizon relation $2M=r_0-r_0^3$ is read off the manifold curve, not off any chart. Moving the charting observer changes only the image of the curve on that observer's celestial sphere — the geometry is rigid — so admissible charting vantages form a groupoid of descriptions whose single invariant is the geometry, $M$ included. **This must be held apart from the de Sitter/Schwarzschild correspondence, which is a different operation**: not re-charting a fixed swept geometry, but one curve swept from two vantages.
② REGISTER — **PROPOSITION** (`prop:rigidity`), proved; the within-geometry morphisms are shown **forced discrete** by the rigidity, with the involution and the sky-angle periodicity as forced generators.
③ HOME — P3 §11.
④ ANCHOR — none.
⑤ JOINS — [[p5-groupoid]] (**owns the completeness question**) · [[p12-algebroid]].
⑥ NOT OP FOR — **Whether those generators generate the discrete structure in full is NOT settled here** and is carried in the companion; P3 states the generators as forced and stops. *The two operations are the thing most likely to be run together in a synthesis, and P3 separates them explicitly.*

### the-seam-and-the-closed-lap
① CLAIM — The equatorial seam joins a Riemannian spherical piece to a Lorentzian de Sitter piece by $\theta\mapsto\pi/2+i\psi$, $\sin\theta\mapsto\cosh\psi$; **the signature flip is automatic**, since $\dd\theta=i\dd\psi$ squares the continuation factor to $-1$ — and the signature that flips is that of the two-dimensional slicing surface, **not of the spacetime, which is Lorentzian throughout**. Overcritical SdS is the same continuation applied past the degenerate crest. Because the areal radius is signed, the slicing **closes**: inward to the seam, around the throat through $r=0$, and out onto the conjugate branch, closing on the backward-radial root.
② REGISTER — **PROPOSITION** (`prop:flip`), proved.
③ HOME — P3 §9.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] · [[p13-boundary]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **The imaginary variables are instruments over an everywhere-real geometry**, and P3 guards this locally at the seam while naming the substrate-level statement as the geometric-core paper's. **The $\mathrm{dS}_5$/$\mathrm{dS}_4$ distinction is handled the same way** — P3 works the equatorial section throughout, where the distinction does not bear on the construction, and says so rather than eliding it.


---

# P4 · `corpus/modern_parallax.tex`
### *The modern parallax: the isotropy of the cosmological redshift as a measurement of uniform expansion*

> **▣ P4'S FLOOR, AND WHY IT IS THE STRICTEST IN THE CORPUS.** *P4 stands alone and reaches for nothing. Its
> result is the confrontational one and must land on evidence a reader who has conceded nothing earlier can
> accept. **Its non-dependence on P1 is load-bearing**: neither leans on the other, which is what makes their
> convergence evidence rather than construction — and a synthesis that presents them jointly destroys that.*

### the-redshift-is-a-path-integral-not-a-source-property
① CLAIM — $1+z=a_{\rm obs}/a_{\rm em}$, so $\ln(1+z)=\int H\,\dd t$ along the ray: **the cosmological redshift is the accumulated expansion in that direction**. The observed temperature $T_{\rm obs}(\hat n)=T_{\rm em}(\hat n)/(1+z(\hat n))$ therefore separates *exactly* into a **source** term fixed at last scattering and a **cumulative** term set by the directional variation of the integrated expansion. The two are independent — the value of one constrains the other not at all — so observed isotropy requires **both** to be small.
② REGISTER — **EXACT**, an identity. The conserved-charge reading is given: in conformal form $\partial_\eta$ is a *conformal* Killing vector whose charge is conserved only on the null cone, where it is $a\omega$; its constancy **is** $1+z=a_{\rm obs}/a_{\rm em}$.
③ HOME — P4 §2.
④ ANCHOR — ledger `integrable_systems`.
⑤ JOINS — [[p15-cr-cosmology]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **The restriction to the null cone is not incidental; it is why the argument works.** For a massive carrier $p\cdot p=-m^2$, the charge is not conserved and no line-of-sight integral exists — *so this is a statement about light and could not have been obtained from any other messenger.*

### the-isotropy-measures-expansion-not-homogeneity
① CLAIM — Grant the common reading its strongest form: let last scattering be **perfectly** homogeneous. Then $\delta T_{\rm obs}/T_{\rm obs}=-\delta\!\int H\,\dd t$ with nothing left over, and **the entire observed isotropy is the statement that the integrated expansion was the same in every direction.** Homogeneity at the source does not *supply* the isotropy; granted perfectly, it removes one term and leaves the isotropy as a direct measurement of uniform expansion. **The widespread supposition that the monopole's isotropy is delivered by homogeneity at decoupling is a category error** — it credits the source for a fact about the observed radiation residing entirely in the intervening expansion.
② REGISTER — **PROVED**, by granting the opposing premise in full.
③ HOME — P4 §2.
④ ANCHOR — none.
⑤ JOINS — [[p6-shadow-of-existence]] · [[p15-cr-cosmology]].
⑥ NOT OP FOR — *This is a claim about the monopole's isotropy, not about the anisotropies.* The next entry is what keeps it distinct from Sachs–Wolfe.

### the-effect-is-distinct-from-sachs-wolfe
① CLAIM — **The crux, and P4 marks it as such.** When lumpiness clusters upon a *single* background, a photon's gravitational redshift descending into a potential well is undone climbing out, so the contributions **telescope** along the path and leave no $\sqrt N$ accumulation. A genuine *differential expansion* accumulates because **there is nothing to cancel against**. So the observed isotropy selects the telescoping picture over the accumulating one; the effect is not a re-derivation of the Sachs–Wolfe anisotropies.
② REGISTER — **ARGUED**, and named by the paper as the point on which the result turns.
③ HOME — P4 §3.
④ ANCHOR — none.
⑤ JOINS — [[p15-cr-cosmology]].
⑥ NOT OP FOR — **⛔ If this distinction fails, the floor is a re-derivation of a known effect and the paper's claim collapses.** Any synthesis use of the floor must carry it.

### the-floor
① CLAIM — Under the hypothesis that the large-scale expansion rate tracks the matter lumpiness region by region, with no single global scale factor, the accumulated redshift would scatter by $\sim10^{-3}$ across the sky, against an observed $\lesssim3\times10^{-6}$ — **an exclusion by three orders of magnitude**. **Every choice in the estimate biases it downward, so the number is a floor**, not an estimate: correlated cells raise it (for $N$ cells of mean pairwise correlation $\bar\rho$ the variance of the mean is $(\sigma^2/N)(1+(N-1)\bar\rho)$, exceeding the independent value for every $\bar\rho>0$ — *a theorem, not a caution*), and modes longer than the path are not averaged down at all.
② REGISTER — **≈ COMPUTED**, receipt-anchored, with the downward-bias argument itemised.
③ HOME — P4 §3.
④ ANCHOR — `R2_the_papers_correlation_figures...`, `R50_the_long_wavelength_bullet...`; ledger `probability`.
⑤ JOINS — [[p15-cr-cosmology]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **⛔ P4 draws the boundary on its own strongest bullet rather than banking it.** The long-wavelength argument adds to the scatter only for $k\gtrsim1/L$: a mode much longer than the observable region takes one value over the whole of it, lands on every direction alike, and **is removed with the monopole**. The paper then shows the boundary costs nothing here — on a CDM spectrum the fraction of path-mean variance below $k=1/L$ is $3\times10^{-6}$ — but the qualification is stated before the reassurance, which is the right order and should survive into any use of the number.

### the-disjunction-is-exhausted
① CLAIM — Two escapes, closed separately. The **statistical** one is closed by the floor. The **structured** one — a finely tuned, spherically symmetric inhomogeneity centred on the observer, which would give isotropic redshift with no global uniform expansion and is untouched by a $\sqrt N$ argument — is closed by the Copernican principle *together with* the independently measured isotropy of the **expansion history** (BAO and Type Ia supernovae reconstructing the expansion along many directions and agreeing across the sky). With both excluded, the observed isotropy forces uniform cosmic expansion.
② REGISTER — **ARGUED**, with the second escape closed on independent data rather than on principle alone.
③ HOME — P4 §4.
④ ANCHOR — none.
⑤ JOINS — [[p15-cr-cosmology]].
⑥ NOT OP FOR — The centred escape is **not** closed by the floor and P4 says so; a synthesis that cites only the three-orders-of-magnitude number has closed one escape of two.

### what-a-single-datum-establishes
① CLAIM — The rejected region is **not a parameter corner but the entire class of histories lacking a single global scale factor on a single global time**. To reject that class is to select a global, time-ordered expansion — the cosmic foliation made dynamical. And **the foliation is logically prior to everything the standard model otherwise assumes**: "space" is one of its slices, "expansion" an ordered family of them, "isotropy" and "homogeneity" properties of a slice — none statable until the foliation is in hand. So one datum establishes, from the bottom up, the cosmic time, the uniformity of its advance, and the maximal symmetry of its slices.
② REGISTER — **ESTABLISHED**, with the last clause explicitly scoped.
③ HOME — P4 §4.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] · [[p10-canonical-time]] · [[p6-shadow-of-existence]].
⑥ NOT OP FOR — **⛔ The scope split is stated at source and must travel with the claim.** The *temporal* claim — uniform expansion throughout cosmic history — is clean, being the integral from decoupling to the present along observed rays. **The extension to a globally maximally symmetric space rides on the Copernican principle and is an extrapolation beyond the directly constrained region.** And what is excluded is an inhomogeneous expansion **rate**; *the matter lumpiness is untouched*, so uniform expansion and lumpy matter are consistent.

### the-augmentation-theorem
① CLAIM — Augmenting general relativity by fixing a physical foliation and reading it ontologically — the lapse the objective rate at which the existing world advances, the shift the relativity of synchrony — is **both necessary and sufficient** for a coherent formal description of an existing, evolving world. *Necessary*: a description lacking the lapse part collapses existence into occurrence. *Sufficient*: the two parts close the only coherent escapes — the "events exist" horn as a category error, the "no objective present" horn as a modal fallacy, **the latter then falsified outright by the measured isotropy**. The augmentation alters none of general relativity's equations.
② REGISTER — **THEOREM**, with its necessary half **measured** rather than posited — which is what turns it from a coherent option into a forced one.
③ HOME — P4 §4, `thm:augmentation`.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] (**this is the augmentation P7's axioms formalise**) · [[p10-canonical-time]] · [[p1-bh-causality]] (the structural half, non-dependent).
⑥ NOT OP FOR — **⛔ The theorem does not fix which geometry realizes the augmented structure**, and P4 states this: it fixes that the structure is necessary and sufficient, and the measurement fixes that its necessary half obtains. *Which four-geometry carries it, and how matter sits on it, are not settled here.* **And both of the theorem's moves are made on P4's own ground** — the category-error diagnosis is a correction of what the formalism asserts, the require-over-permit preference is ordinary inference to the best explanation — with the general question of when such inferences are reliable named as a companion's and **explicitly not drawn on**. That independence is what lets the companion rest on this instance without circularity.

### the-history-the-measurement-closes
① CLAIM — The structure this datum forces was posited by Einstein in February 1917, **explicitly "against the spirit of relativity"**, and on the empirical ground that stellar proper motions are small compared with $c$; countered a month later by de Sitter, who placed the choice among candidate universes outside physical argument and pressed as his sharpest objection that in Einstein's solution "time has a separate position"; and defended in 1920 by Eddington on geometric grounds, in the declared absence of any experimental knowledge on cosmical scales. **Einstein then went nearly silent on cosmology for the rest of his life** and never addressed how the cosmic time his own assumption distinguished stands to the relativity of simultaneity. *The assumption was correct, and the objection was correct as a description of the structure though not as a reason to reject it.*
② REGISTER — **HISTORICAL**, from the primary sources.
③ HOME — P4 §5.
④ ANCHOR — none.
⑤ JOINS — [[p6-shadow-of-existence]] (**an episode of theory-choice read against the myth — but P4 reaches it independently**).
⑥ NOT OP FOR — This is history, not evidence for the physical claim: the floor stands or falls on the data alone. *Its use is to show that the structure now measured was available, argued, and abandoned for reasons that were never empirical.*


---

# P5 · `corpus/groupoid_paper.tex`
### *The description groupoid: relations, completeness, and the discrete symmetry of the solution space*

> **▣ P5'S FLOOR AND ITS LICENCE.** *P5 leans on the P1--P3 arc and on P4, and is the algebraic counterpart to
> P3 — same overdevelopment licence, same discipline. Its own test: **is each piece motivated by a question
> visible inside P5?** On the read it is, once two orderings were fixed (r4041).*

### the-two-generators-and-their-relations
① CLAIM — The within-single-geometry morphisms have two generators, given coordinate-independently: the **root-exchange involution** $\sigma$, the reflection of the sky angle about $w=\pi/6$, of order two; and the **sky-angle periodicity** $\tau: w\mapsto w+2\pi/3$, of order three, which is forced because $2M=\tfrac{2}{3\sqrt3}\sin 3w$ has period $2\pi/3$. They satisfy $(\sigma\tau)^2=\mathrm{id}$, computed directly, so the generated group is $D_3\cong S_3$.
② REGISTER — **PROPOSITIONS**, proved.
③ HOME — P5 §3, `prop:sigma`, `prop:tau`, `prop:relations`.
④ ANCHOR — `P05_dihedral_generators`.
⑤ JOINS — [[p3-sds-slicing]] (supplies both generators as forced) · [[p12-algebroid]].
⑥ NOT OP FOR — These are the morphisms acting **within a single geometry**, at fixed $2M$. The between-member morphisms are a separate classification.

### completeness-the-headline-result
① CLAIM — **Every** within-single-geometry morphism lies in $\langle\sigma,\tau\rangle$, so the group is *exactly* $D_3\cong S_3$. **The argument turns on invertibility, not continuity.** A morphism acts on the sky angle as $T$ with $\sin 3T(w)=\sin3w$, which admits at each $w$ either branch $3T\equiv3w$ or $3T\equiv\pi-3w$. *Continuity alone does not select between them* — the branches meet at $w=\pi/6\bmod\pi/3$ and a continuous map could switch there. What excludes a switch is that every morphism is a **bijection**: the branches have slopes $+1$ and $-1$, so a switch folds the domain and destroys injectivity. A continuous bijection therefore stays on one branch uniformly, giving three rotations (the powers of $\tau$) and three reflections ($\sigma$ and its $\tau$-translates) — six maps, exactly $D_3$.
② REGISTER — **PROPOSITION, PROVED.** *This closes the generation question P3 left open: the generators identified there are not merely forced and present but complete.*
③ HOME — P5 §3, `prop:completeness`.
④ ANCHOR — none.
⑤ JOINS — [[p3-sds-slicing]] (**closes its stated-open item**) · [[p12-algebroid]].
⑥ NOT OP FOR — **⛔ Until r4041 this proposition rendered as unproved.** The proof sat *after* an intervening remark, so it attached to the remark instead — on the paper's headline result. Reordered to proposition → proof → remark. *The content was never missing; the presentation lost it.*

### the-projective-invariant
① CLAIM — The three horizon roots appear on the sky angle as the preimages $w$, $w+120^\circ$, $w+240^\circ$, and their cross-ratio with the centre is the **equianharmonic** value $\lambda=e^{i\pi/3}$, $\lambda^2-\lambda+1=0$, independently of $w$ — the unique cross-ratio at which the six-element orbit generated by permuting the four points collapses. **So no relabelling by the group moves it**: the group has a projective invariant.
② REGISTER — **REMARK**, receipt-anchored.
③ HOME — P5 §3, `rem:equianharmonic`.
④ ANCHOR — `Q4_equianharmonic_vantages`; ledger `quadric_geometry`.
⑤ JOINS — [[p3-sds-slicing]] (the $120^\circ$ spacing the triple-angle forces).
⑥ NOT OP FOR — **⛔ P5 refuses the identification the coincidence invites, and the refusal is the valuable part.** The classical equianharmonic case has vanishing $j$-invariant and complex multiplication by $\omega$; that curve is a *double* cover branched at four points, whereas the cover of §9 is *three*-sheeted over the $2M$-plane branched at the two Nariai values — **a different degree over a different base with a different branch set**, so a $j$-invariant computed from the four points says nothing about it. *The cross-ratio is equianharmonic, the monodromy contains an order-three cyclic subgroup, and the two are not here shown to be one thing.* **And the remark names a consequence of a forced fact rather than adding one**: any three vantages so spaced are equianharmonic automatically.

### single-reassignment-uniqueness
① CLAIM — A reassignment promoting a null direction to the fundamental timelike congruence is **available at exactly one member, and the group structure is what decides it.** At a generic member $\sigma$ exchanges the member's two vantages, so a reassignment made at one is undone at its partner and the two-cycle structure forbids it. At the single fixed point $w=\pi/6$ there is no partner — the member's one vantage is its own — and the reassignment is available there and nowhere else. That fixed point is the Nariai member, $r_0=1/\sqrt3$, $2M=2/(3\sqrt3)$. **The selection is a structural fact about the groupoid, not a fact about dynamics or fine-tuning.**
② REGISTER — **PROPOSITION**, proved from the group structure.
③ HOME — P5 §5, `prop:single`.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (**converges with the empirical forcing of a cosmic time — two routes sharing no premise**) · [[p7-cr-framework]] (reaches the same configuration on independent grounds) · [[p3-sds-slicing]].
⑥ NOT OP FOR — **⛔ Until r4041 the section opened by citing the companion's result and then supplying the group reason for it**, which reads as rationalising rather than deriving. Reordered so the group argument comes first and the companion is named after, with the explicit note that nothing here draws on it. *That ordering is what makes the convergence with P4 evidential rather than circular.* **And the fixed point's coincidence with the turning radius is recorded without a derivation claim**: on the forced member it sits at $r=\alpha/\sqrt3=(M\alpha^2)^{1/3}$, where the areal acceleration changes sign and the slicing surface is flat — *the vantage at which the reassignment is uniquely available is the radius at which the member's own expansion history turns*, exact, and neither fact derived from the other.

### the-discrete-symmetry-of-the-solution-space
① CLAIM — The same-$\alpha$ between-member morphisms are the **monodromy** of the horizon cubic's three-sheeted cover branched at the two Nariai points, with monodromy group $S_3$ and **trivial deck group** (a degree-three cover is normal only if its monodromy has order three; $S_3$ has order six — the group that *is* a deck group is the same $S_3$ on the degree-six Galois closure). That monodromy group is equally the **Galois group** of the cubic over $\mathbb C(2M)$ — **one $S_3$ worn as monodromy, Weyl, and Galois symmetry alike**. Adjoining the mass-reflection $2M\mapsto-2M$ gives $\mathrm{Aut}(A_2)=S_3\times\mathbb Z_2\cong D_6$; the action between distinct $\alpha$ is the continuous homothety, under which the discrete structure is invariant.
② REGISTER — **PROPOSITIONS**, proved and receipt-anchored, with the Galois step's hypothesis discharged explicitly.
③ HOME — P5 §9, `prop:monodromy`, `prop:deck`, `rem:galois`, `prop:autA2`.
④ ANCHOR — `P05_deck_group_S3`, `X5_monodromy_group`, `T1_the_galois_inference_needs_irreducibility_and_it_holds`; ledger `number_theory`.
⑤ JOINS — [[p3-sds-slicing]] · [[p12-algebroid]] · [[p13-boundary]].
⑥ NOT OP FOR — **⛔ Two hypotheses are discharged rather than assumed, and both had real alternatives.** The Galois step needs the cubic to be **irreducible** — a reducible cubic can have a non-square discriminant with a group of order two — and irreducibility holds cheaply here, the cubic being of degree one in $2M$ so that Gauss's lemma forbids a factorisation. And the generation claim needs the two Nariai monodromies to transpose **different** pairs of sheets, which is a computation: they give $(0\,2)$ and $(1\,2)$, so the group has order six. *Had the same pair collided at both, the group would have been $\mathbb Z_2$ and the claim false.* **The monodromy also does not act uniformly on the real structure** — all of $S_3$ under-critically, only the order-two subgroup over-critically, the real root distinguished.

### R-is-the-correspondence-and-the-parity-split
① CLAIM — The mass-reflection $R$ — the $A_2$ diagram automorphism, the outer $\mathbb Z_2$ — **is** the de Sitter$\leftrightarrow$Schwarzschild correspondence itself rather than a structure standing outside the group. It acts on the metric function by parity: $f(r)=(1-r^2/\alpha^2)+(-2M/r)$ splits into an **$R$-even** piece, the invariant de Sitter geometry, and an **$R$-odd** piece, the Schwarzschild mass the vantage carries and the swap reverses.
② REGISTER — **REMARK/PROPOSITION**, proved.
③ HOME — P5 §9, `rem:P-dS-Schw`, `sec:autA2`.
④ ANCHOR — none.
⑤ JOINS — [[p6-shadow-of-existence]] (**this is the reclassification in closed form — an exact involution rather than a general perspective**) · [[p13-boundary]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ Three discrete operations, distinct as maps, which P5 says must not be conflated**: $\sigma$ (Weyl, diagonal reflection — mass-invariant, Nariai-fixed, **no branch-point crossing at all**), $R$ (diagram, anti-diagonal — the vantage-swap, de Sitter-fixed, **the $r=0$ crossing**), and $\xi$ (the partial involution at the throat seam). $\sigma$ and $R$ generate $D_6$; $\xi$ is the analytic continuation whose invertibility secures the correspondence's exactness. *They share a continuation mechanism and do not coincide as maps.*

### the-seam-involution-is-invertible-because-it-is-mobius
① CLAIM — The correspondence's exactness rests on $\xi$'s invertibility, and that is a nameable property. In the eigenvalue $\lambda=\alpha^2/(\alpha^2-u)$ with $u=\mathbf x^2$, the map from position to signature is **Möbius**, $(a,b,c,d)=(0,\alpha^2,-1,\alpha^2)$ with $ad-bc=\alpha^2\neq0$, and its inverse is Möbius again. **So $\xi$ is invertible because a Möbius map is a bijection of the Riemann sphere**, and the two signature regions are two arcs of that sphere joined *through the point at infinity*: $\lambda>0$ Riemannian below the seam, $\lambda<0$ Lorentzian above, $\lambda=\infty$ at the seam. The map's zero sits at $u=\infty$ and not at the seam — **the same statement as the metric never degenerating there**.
② REGISTER — **ESTABLISHED**, ledger-anchored.
③ HOME — P5 §1 and §7.
④ ANCHOR — ledgers `complex_analysis`, `spectral_theory`.
⑤ JOINS — [[p3-sds-slicing]] (the seam and its automatic signature flip) · [[p17-geometric-core]].
⑥ NOT OP FOR — The signature flip is **a property of the continuation, not of the descriptions**, and $\xi$ is a *partial* involution — a vantage-change crossing the seam, distinct in kind from the within-single-geometry morphisms.

### the-A2-is-not-a-realised-colour-isometry
① CLAIM — The $A_2$ here is the root system of the SdS **solution space** — a discrete symmetry of the slicing family, realised by the roots of the horizon cubic. It is the same *abstract* root system as the Cartan–Weyl skeleton of $\mathfrak{su}(3)$ but **a different realisation**, and the coincidence of abstract type does not on its own make the discrete gravitational symmetry an internal colour symmetry as a *realised* one.
② REGISTER — **REMARK**, a scope guard stated in P5's own voice.
③ HOME — P5 §9, `rem:a2-distinct`.
④ ANCHOR — none.
⑤ JOINS — [[p13-boundary]] · [[p14-matter-sector]] · [[p17-geometric-core]].
⑥ NOT OP FOR — **This is a guard, not a claim, and it is the right shape for one.** What the argument establishes is the distinct *realisation* and the absence of a continuous-isometry colour — **not** that the shared abstract root system is without significance. *A synthesis that reads this remark as either asserting or denying a colour identification has read it wrongly in both directions.*


---

# P6 · `corpus/shadow_of_existence.tex`
### *The shadow of existence: scientific theory-choice as an empirically grounded discipline, calibrated on the record*

> **▣ P6'S ROW IS THE FIRST THAT PERMITS REACHING BOTH WAYS**, so the test changes: not "did it borrow" but
> **does each forward draw serve the same epistemic end as the developed material?** On the read it does. The
> defect found was the reverse of the usual one — P6 *understated* its own case by describing the corpus as
> leaning on it.

### the-imperative-and-the-reclassification-constraint
① CLAIM — Write $\Phi=\pi(W)$: appearances are the image of a world under a perspectival projection, and the observer holds $\Phi$, never $W$. The appearances divide into **literal** components, on which $\pi$ acts trivially, and **perspectival** ones that are artefacts of $\pi$. **Both classes are non-empty, and this is an observed fact rather than a postulate** — the Sun's annual path along the ecliptic is a perspectival illusion of the Earth's motion, the Moon's monthly circuit a literal orbit. Because both occur, no blanket reading is admissible: reading every appearance literally is the error a method must first forbid. The **imperative**: infer $W$ such that $\Phi=\pi(W)$. The **constraint**: an admissible $W$ must *explain* the perspectival appearances — exhibit the projection under which they arise — not discard them or merely reproduce them.
② REGISTER — **STATED AND ARGUED**, with the non-emptiness grounded in cases rather than assumed.
③ HOME — P6 §2.
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] · [[p4-modern-parallax]] · [[p5-groupoid]] (the $R$-even/$R$-odd split is this constraint in closed form).
⑥ NOT OP FOR — **⛔ Perspectival does NOT mean false, and P6 uses P1 to show it.** The metric's verdict that two null-separated horizon events share one place and one instant is a genuine fact about the measure — the separation truly collapses — *yet perspectival still*, a fact about the ruler and not about the identity of the events, which stay distinct on the point set. **The perspectival class is the class of appearances that image $\pi$ rather than $W$; some are entirely real as facts about $\pi$.** *This is the single most useful correction in the paper for the synthesis, because it is what stops "perspectival" being read as "unreal" anywhere in the corpus.*

### formal-likeness-does-not-sort-the-two-classes
① CLAIM — A genuine metric collapse — a place its chart draws as an extended line — sits beside the Mercator map's rendering of the North Pole as its top edge, an identical-looking line that is a pure coordinate artefact concealing an ordinary point. **The appearances coincide in form.** Only exhibiting the projection each arises under sorts one from the other.
② REGISTER — **ARGUED**, from P2's worked case.
③ HOME — P6 §2.
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] · [[p1-bh-causality]].
⑥ NOT OP FOR — **This is exactly why the reclassification constraint demands the projection be shown and not merely the appearance saved.** *A synthesis that argues from resemblance — "this looks like a chart artefact, so it is one" — has made the error this section exists to forbid.*

### least-arbitrariness
① CLAIM — A candidate world may carry an **unforced modulus**: a parameter fixing how a symmetry is broken that neither appearances nor principle pin. Such a structure is **not a single world but a family**, and inadmissible on that ground; the equant is its historical type. A structure carrying no such modulus *requires its configuration as a consequence of its own form*. **The maximally symmetric structure is the unique one of that kind** — every less symmetric structure requires a choice of how to break the symmetry, and that choice is a modulus. This is Rule 2 read in the ontological register.
② REGISTER — **CRITERION**, with an exact group-theoretic counterpart: what leaves nothing to choose is a group acting **transitively**, a modulus being a coordinate transverse to the orbits, so one exists precisely when the action is not transitive — and read on geodesics the same transitivity says the flow is **maximally superintegrable**. *Least-arbitrariness and superintegrability are one property read epistemically and dynamically.*
③ HOME — P6 §4.
④ ANCHOR — ledger `integrable_systems`; the identification cites [[p12-algebroid]] and [[p17-geometric-core]].
⑤ JOINS — [[p17-geometric-core]] · [[p12-algebroid]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ THE REGISTER'S BOUNDARY IS DRAWN WITH IT, AND THE GUARD SEPARATES THREE SENSES OF "MODULUS" THAT THE CORPUS OTHERWISE RUNS TOGETHER.** ① *An unforced parameter indexing candidate worlds* — unpinned, so the candidate answers "what is the world?" with a family. **This alone is what the criterion excludes.** ② *A coordinate on a space of inequivalent solutions* — as the mass is for the space of cuts, transverse to the orbits. **The criterion does not exclude this and nothing here counts against it**: a space of physically distinct solutions is not a family of rival worlds, and a theory is not made arbitrary because its solutions differ. ③ A choice that leaves the symmetry **maximal** — since a modulus fixes how a symmetry is *broken*, an unforced choice leaving it unbroken **lies outside the register entirely**, the dimension of a maximally symmetric substrate being the programme's first such case; *where form is silent, content may still decide.* **A criterion claimed to apply everywhere is as suspect as one applying only where it was formulated.**

### the-modal-fallacy
① CLAIM — The imperative's characteristic dual: **the absence of a local discriminator is not the absence of the fact.** Reading local undetectability as non-existence is a modal error, and it is the error the century-old reading of synchrony's relativity committed.
② REGISTER — **STATED**, and the corpus's instance of it is *falsified by measurement* rather than argued against.
③ HOME — P6 §5.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (**where the fallacy is falsified outright**) · [[p1-bh-causality]].
⑥ NOT OP FOR — Naming a fallacy does not establish the fact whose undetectability is at issue; it removes an argument against it. *The fact itself, in the corpus's case, is supplied by a measurement.*

### the-engine-and-why-the-record-must-be-shadow-read-first
① CLAIM — The rules' reliability is a matter of fact and the fact is recorded; the data are episodes of theory-choice and the engine is historiography. **But the received record is itself shadow-distorted** — mythologised into independent geniuses and clean confrontations with crucial experiments — so **de-mythologising is not a preface to the evidence but the validation of it**. Two corrections carry it: Copernicus had read Archimedes' *Sand-Reckoner* before circulating his system, the *Commentariolus*' fourth postulate reproducing Archimedes' recast of Aristarchus's proportion — a relation Copernicus had no internal use for, never employed, and dropped from *De revolutionibus*. And **the parallax objection is anachronistic**: while the stars were held to lie on a single spherical boundary, a relative parallax was not a measurement that could fail — it was inconceivable; neither the *Almagest* nor *De revolutionibus* argues from parallax at all, but from symmetry. The objection was first pressed by Tycho, after Digges gave the cosmos depth, and rested on stellar "disc" sizes now known to be seeing artefacts.
② REGISTER — **HISTORICAL**, from primary sources.
③ HOME — P6 §7.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (which reaches its own historical instance independently).
⑥ NOT OP FOR — **A history effacing the first correction reads the episode as evidence that great theories spring *ex nihilo*; one effacing the second reads it as evidence that a correct theory was rightly held back by a sound empirical objection. Both lessons are false.** *The de-mythologising is what determines whether the data say what they are taken to say.*

### the-vindication-lemma-stated-falsifiably
① CLAIM — Stated as an object of research rather than an article of faith: **across a properly sampled reference class of theory-choice episodes — successes and failures alike — structures favoured by the rules ahead of a decisive non-local measurement are subsequently confirmed at a rate above the base rate at which merely permitted structures are confirmed.** The sampling that would test it is the discipline's first programme: assemble the class, classify each episode by whether its eventual victor was *required* or merely *permitted*, and measure the differential.
② REGISTER — **⛔ FALSIFIABLE CLAIM, NOT YET TESTED. The outcome is explicitly not presumed.**
③ HOME — P6 §9.
④ ANCHOR — none.
⑤ JOINS — every paper the corpus offers as an instance.
⑥ NOT OP FOR — **⛔ The sampling requirement includes failures AND the episodes in which the criterion was applied in print and disregarded**, on the stated reasoning that *a reliability estimate built from one's own successes is survivorship and not measurement*. **And the reflexive closure is explicitly not soundness**: a method can be coherently, reflexively wrong. **The scope is disciplined at source** — the subject is the epistemology of scientific theory-choice, ampliative inference under underdetermination, and *not* epistemology entire.

### the-relation-to-the-corpus-runs-the-other-way
① CLAIM — **The corpus's papers do not lean on this discipline.** Each reaches its instance on its own ground and says so — P2 its perspectival reading on the analytic structure of $r(z)$, P4 both of its moves as ordinary scientific inference, P5 its selection from the group structure. **That independence is what makes them data.** Each is a structure the rules favoured ahead of its decisive measurement, reached *without* the rules, so the record of what those measurements returned is evidence **about** the rules rather than an application of them.
② REGISTER — **STRUCTURAL RELATION**, corrected at r4043 to match what the papers now say.
③ HOME — P6 abstract, §1, §10.
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] · [[p4-modern-parallax]] · [[p5-groupoid]].
⑥ NOT OP FOR — **⛔ AN INSTANCE DERIVED BY APPLYING THE METHOD WOULD CERTIFY NOTHING.** *This is the load-bearing constraint on the synthesis: any section presenting P6 as licensing the corpus's readings destroys the evidential value of every instance at once, and it does so silently, since the resulting text reads perfectly well.*


---

# P7 · `corpus/CR_framework.tex`
### *Collapsed matter must become a universe: the necessary and sufficient augmentation, proven for collapse of any symmetry*

> **▣ P7 IS THE MIDPOINT SYNTHESIS WITH A SIGNIFICANT BENT.** *It synthesises P1--P6, develops its own axioms,
> worked constructions and central theorem, then takes the rest-of-corpus fallout. **Because it develops real
> results it cannot be purely holistic** — which is exactly why the outside results paper this arc builds is a
> distinct object. P7 synthesises from the inside while building; ours synthesises the whole from outside once
> built.*

### the-axioms-and-what-cosmic-time-is-not
① CLAIM — A one-parameter family of smooth Riemannian three-manifolds $\{\mathcal S_t\}$, the **ontological spatial layers**, ordered by a global parameter $t$, **cosmic time**. That parameter is *not* defined operationally, *not* identified with any coordinate time on $M$, and *not* assumed orthogonal to the spatial geometry. A spacetime $(M,g)$ is the layers' representation under a causal assignment; distinct Lorentzian metrics on one manifold are projections of one layer; and admissible causal reassignment **preserves the cosmic foliation**, leaving the field equations, the metric and the causal structure unchanged.
② REGISTER — **AXIOMS**, introduced as hypotheses with their justification declared twofold and both halves named: *structural*, via the SdS construction and the Null–Boundary Correspondence, and *empirical*, via P4.
③ HOME — P7 §2.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (**the augmentation P4's theorem establishes as necessary and sufficient**) · [[p10-canonical-time]] · [[p8-slicing-operator]].
⑥ NOT OP FOR — **The augmentation adds no equation and changes none.** *It fixes which of the formally available foliations is physical and reads that one as the existent — nothing more.*

### the-six-foundational-data
① CLAIM — P7 fixes what it builds on explicitly, as six established results with their sources: **(F1)** the horizon's causal structure, from Lorentzian causal structure alone and making **no use of spherical symmetry**; **(F2)** the singularity taxonomy, horizon and $r=0$ two species of one genus; **(F3)** the slicing curve, with the degenerate configuration the fixed point of the root-exchange involution; **(F4)** the reassignment groupoid, each morphism altering the causal reading of one fixed geometry rather than the geometry; **(F5)** the forced foliation, measured; **(F6)** the existent, with both competing readings closed — "no objective present" as a modal fallacy falsified by (F5), "the block is the existent" as a category error whose canonical symptom is the frozen problem of time.
② REGISTER — **DECLARED DEPENDENCIES**, each cited to its own paper.
③ HOME — P7 §7.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] · [[p2-janzen-circle]] · [[p3-sds-slicing]] · [[p5-groupoid]] · [[p4-modern-parallax]] · [[p6-shadow-of-existence]] · [[p10-canonical-time]].
⑥ NOT OP FOR — **⛔ This list is the corpus's own statement of what P7's theorem rests on, and it is the single most useful object in the paper for the synthesis** — it says which results are load-bearing and which are context. *Note that (F1) is flagged at source as symmetry-free; that is what the any-symmetry claim later turns on.*

### the-causal-reassignment-and-the-forced-member
① CLAIM — On the forced foliation, the limiting null direction the event horizon selects is reassigned as the fundamental **timelike** congruence. The Einstein equations then return the Schwarzschild–de Sitter metric, and the **tangency trichotomy** — transverse, tangent, or no horizon — forces the degenerate member, at which $\Lambda G^2M^2/c^4=1/9$ holds **as an equality rather than as a saturated bound**. The comoving law is $r=(2M\alpha^2)^{1/3}\sinh^{2/3}(3\tilde\tau/2\alpha)$: the exact flat-$\Lambda$CDM expansion history with its rate fixed by $\Lambda$ alone.
② REGISTER — **DERIVED**, the member forced by the trichotomy rather than chosen.
③ HOME — P7 §5.
④ ANCHOR — the section's own.
⑤ JOINS — [[p5-groupoid]] (**which forces the same member from the group structure, independently**) · [[p3-sds-slicing]] · [[p15-cr-cosmology]].
⑥ NOT OP FOR — Synchrony is a **representational** assumption, not an ontological one: the model is non-synchronous while its observational expansion history coincides exactly with flat $\Lambda$CDM.

### the-null-boundary-correspondence
① CLAIM — **THEOREM.** A collapse horizon $\mathcal H^+$ and a de Sitter cosmological horizon represent **one ontological layer under distinct causal assignments**, and the map between them is **causal and structural rather than metric** — it carries no metric multipoles.
② REGISTER — **THEOREM**, proved.
③ HOME — P7 §6.
④ ANCHOR — the section's own.
⑤ JOINS — [[p1-bh-causality]] · [[p13-boundary]] · [[p15-cr-cosmology]].
⑥ NOT OP FOR — **⛔ That the map is not metric is precisely what makes the symmetry claim work**, and it is the hinge a synthesis is likeliest to drop. Because the correspondence carries no multipoles, **non-spherical collapse is dissolved rather than deferred** — the argument does not depend on the symmetry of the collapse. *An entry that presents the correspondence as a metric identification has inverted its content and lost the any-symmetry result with it.* **And the generic map's horizon areas and surface gravities differ**; the coincidence is at the forced member.

### the-central-theorem
① CLAIM — Three results landed together. **(1)** The CR augmentation is the **necessary and sufficient** completion under which general relativity describes a world that exists and evolves — required, not optional, with its necessary half **measured**. **(2)** On that augmentation, gravitational collapse cannot terminate but must continue as a cosmology: **collapsed matter becomes a universe**, the collapse horizon and the cosmological seam one ontological layer. **(3)** This holds for collapse of **any** symmetry.
② REGISTER — **THEOREM**, `thm:augmentation-p7` and `thm:bead`, from (F1)–(F6).
③ HOME — P7 §7.
④ ANCHOR — the section's own.
⑤ JOINS — [[p4-modern-parallax]] · [[p1-bh-causality]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — The scope is marked at source: **the necessity is a structural result with its necessary half measured**, while *whether the observed cosmos realizes this cosmology in detail* stays open to the world and is held to two named tests — the structural one that closed trapped surfaces do not form, and the empirical one against the microwave background.

### the-lift-and-the-explanation-of-the-initial-rate
① CLAIM — Along the segment of the closed contour on which $\operatorname{Re}\tilde\tau$ does not advance, the areal radius is carried continuously from the comoving turnaround to the branch point. Because cosmic time **is** $\operatorname{Re}\tilde\tau$, **that entire process occupies no cosmic time at all** — a forced phase shift of finite extent. The universe therefore *arrives* at $r=0$ carrying exactly the initial data the Friedmann equations require of it. **This answers, rather than restates, the objection Eddington pressed against the Einstein–de Sitter model in 1933**, retired unanswered rather than met: the initial expansion rate is explained rather than postulated. *The big bang is not a point but a bounded interval, and the interval is a physical process that can be drawn.*
② REGISTER — **THEOREM plus its worked reading**; the segment is a solution of a variational principle, an instanton in the inverted potential.
③ HOME — P7 §7 (`thm:bead`) and §8.
④ ANCHOR — the sections' own; ledger `combinatorics`.
⑤ JOINS — [[p10-canonical-time]] (**whose regular Euclidean state, fixed on independent grounds, is the state the kernel here selects**) · [[p16-cosmogenesis]] · [[p2-janzen-circle]].
⑥ NOT OP FOR — **The explanation is of this framework's characteristic kind and P7 says so**: the divergent rate and the deceleration are **effective** — perspectival consequences of parametric motion rather than dynamical causes. *Nothing acts at the beginning; the shape of the history is a property of a fixed curve.*

### the-fold-and-what-is-dimension-independent-in-it
① CLAIM — At the merger the horizon polynomial has a double root with non-vanishing second derivative while the mass enters additively at first order — **a fold**, in the standard classification of one-parameter collisions — so the two horizons separate as the **square root** of the distance from the critical mass, and $\kappa$ vanishes at that same rate. **The exponent is fixed by the collision type, not by this family**, and the check is the one that could have refuted it: at general dimension the degenerate member persists with the polynomial's second derivative equal to $-2(D-1)$, never vanishing, which is the fold condition. So the square root is **dimension-independent**; what is particular to four dimensions is only the value $-6$.
② REGISTER — **RECEIPT-ANCHORED**, with a refutation-capable check run.
③ HOME — P7 §6 (relocated there r4045; it had lived only in the abstract).
④ ANCHOR — `D4_fold_scaling`; ledger `catastrophe_singularity`.
⑤ JOINS — [[p3-sds-slicing]] · [[p15-cr-cosmology]] (the transmission reading: *how near* the forced member a configuration must sit for its surface gravity to carry no appreciable scale has a definite answer, and it is a square root).
⑥ NOT OP FOR — **⛔ Terminology guard, stated at source:** *fold* is bifurcation-theoretic here and is **not** to be read against the bifurcation **sphere** of a Killing horizon, **which the degenerate member does not possess.**

### the-dissolution-family
① CLAIM — Turned on the theory's standing problems, the same augmentation dissolves a family together: the non-localizability of gravitational-wave energy, closed timelike curves, cosmic censorship, the information paradox, the laws of black-hole mechanics, and the hole argument — **not one at a time by separate devices but as consequences of a single distinction**.
② REGISTER — **SYNTHESIS**, the paper's own first synthesis.
③ HOME — P7 §9.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] (which reaches three of them on causal structure alone) · [[p6-shadow-of-existence]] (R4, against patchwork).
⑥ NOT OP FOR — **⛔ P6 amends this account of itself, and the amendment must travel with the claim**: the dissolutions are **not one move recurring but two** — *reclassification*, which exhibits a projection, and *least-arbitrariness*, which denies a quantity a referent — with **distinct failure conditions and no implication between them**. *A synthesis presenting the family as one mechanism has adopted the account P6 corrected.*

### the-frontiers-section-and-its-own-distinction
① CLAIM — P7 distinguishes two kinds of entry in its own open list, and the distinction is reusable. **Work** is something unworked that a definite computation would close, and it *shrinks as it is done*. A **boundary** is a result rather than a gap — a statement of where this construction hands over and to which sector — and it *does not shrink, because there is nothing in it left to do*.
② REGISTER — **METHODOLOGICAL**, stated in P7's own voice.
③ HOME — P7 §10.
④ ANCHOR — none.
⑤ JOINS — the frontier gather below; every paper's open list.
⑥ NOT OP FOR — **⛔ This is directly load-bearing for Phase 3, and it cuts both ways.** *A list that ends with only boundaries and standing conditions has not failed to empty; it has finished* — and saying which entries are which is what lets that be told from a list quietly going stale. **But the distinction is also the easiest way to retire an item by reclassification rather than by work**, which the arc forbids. *Phase 3 uses it to describe items, never to remove them.*

---

## THE FRONTIER GATHER

*(Phase 3. Every open item from every source, in one place, deduplicated by **room** rather than keyword —
the register's own warning, since a keyword gather overcounts about fivefold. Each item gets: what it is,
what it bears on, **what it does not bear on**, and what would discharge it. **Complete and unfiltered**:
no triage, no verdicts attached that excuse an item from the list, and items leave only when the work is
done. Each is worked fresh before being listed as open, because the base rate says most "open / not yet /
deferred" claims in this corpus are stale links.)*

*(empty — Phase 3 has not begun)*

---

## THE DISAGREEMENTS

*(Where the harvest and a source part company, or where two sources part company with each other. **These
are findings, not defects to reconcile away.** Each records both statements at source, and what would
settle it. Nothing here is resolved by picking the reading with the better number.)*

*(empty)*
