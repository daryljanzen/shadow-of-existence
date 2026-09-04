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
