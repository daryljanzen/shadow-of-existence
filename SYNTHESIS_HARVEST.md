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

> **▣ THE READ IS COMPLETE AND ATTESTABLE** *(first pass r4021--r4025 through display filters that dropped
> lines; re-read r4067 without filters). The two entries at the end of this block are results the filtered pass
> had not registered.*

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


### why-the-chart-draws-a-place-as-a-line
① CLAIM — Metric singularities are persistently misread because of **how charts render them**. A chart such as Eddington–Finkelstein parametrises approaches to the singularity by a coordinate well defined in a neighbourhood but degenerating at the singularity itself, so **the single metric place is drawn spread out as an extended line** — the vertical line at $r=2M$. **This is the same projective mechanism by which Mercator draws the North Pole**, and the visual appearance is identical: a place drawn as a line. **But the reason for the appearance is the opposite.** At the pole the chart *manufactures an extension that is not there*, and a chart centred on the pole collapses the line back to the point it always was. At $r=2M$ the chart *spreads out a metric collapse that is*: reading the line back does not yield an ordinary point a better chart would reveal, because **no chart removes it — the collapse is in the metric, not in the projection.**
② REGISTER — **ARGUED**, and it is the diagnostic P6 later generalises.
③ HOME — P2 §7.2.
④ ANCHOR — none.
⑤ JOINS — [[p6-shadow-of-existence]] (**"formal likeness does not sort the two classes" is this case stated as a rule** — P6 reaches it from here) · [[p1-bh-causality]] · [[p3-sds-slicing]].
⑥ NOT OP FOR — **⛔ The identical appearance is the whole point and the whole danger.** Two loci drawn the same way by the same mechanism, one a coordinate artefact and one a real collapse — *so no argument from how a singularity is drawn can sort them, in either direction.* The same holds at $r=0$ with the collapse in a different sector.

### construction-not-error
① CLAIM — **It would misread the analysis to conclude that the swept Schwarzschild geometry is a mistake.** Sweeping the radial curve to recover a spatial geometry is the legitimate and indeed the natural way to chart the geometry from a given vantage, and the result **agrees with the standard geometry on every observable in $r\ge2M$**. What is identified is not an illegitimate operation but a **misreading of its product**: treating features the construction manufactures — the asymmetric labelling, and with it the curvature singularity at $r=0$ — as features of the geometry rather than of the chart. *The construction is faithful as a description from its vantage; the error is ontological.*
② REGISTER — **SCOPE STATEMENT**, in P2's own voice.
③ HOME — P2 §7.3.
④ ANCHOR — none.
⑤ JOINS — [[p3-sds-slicing]] (the forced pivot) · [[p6-shadow-of-existence]] (perspectival ≠ false) · the $r=0$ cross-paper join above.
⑥ NOT OP FOR — **⛔ THIS IS THE ENTRY THAT KEEPS THE WHOLE PERSPECTIVAL READING FROM SOUNDING LIKE A DISMISSAL**, and it belongs in the synthesis wherever the reading is introduced. *Nothing standard is being called wrong.* **And P2 goes further, in a direction a partisan paper would not**: the asymmetry is *"where the construction becomes most interesting rather than least"* — that two analytically identical metric singularities are charted into a sharply asymmetric pair is **not a defect to be discarded but a structural fact to be understood**, the symmetry-reduction implicit in sweeping an asymmetric radial profile about one of its endpoints doing work the symmetric underlying structure alone does not display. **Whether that work is purely an artefact of the vantage, or whether the vantage-dependence itself encodes something physical, is raised here and explicitly not resolved.**

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

> **▣ THE READ IS COMPLETE** *(first pass r4029--r4035, completed r4061 after the coverage stocktake found
> roughly half the body unopened). The four entries at the end of this block are results the first pass had no
> sight of.*

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


### the-horizon-locus-is-a-line-and-a-tilted-ellipse
① CLAIM — Taken over all slicing parameters at once, the horizon locus in the $(r_0,r)$-plane is $g(r)=g(r_0)$ with $g(t)=t^3-t$, and it **factors into a straight line and a conic**: $(r-r_0)(r^2+rr_0+r_0^2-1)=0$. The line $r=r_0$ is the trivial root — the slicing parameter is always itself a horizon — and the conic is an **ellipse tilted at $45^\circ$**, its major axis along the anti-diagonal $r=-r_0$ (semi-axes $\sqrt2$ and $\sqrt{2/3}$, from the quadratic form's eigenvalues $1/2$ and $3/2$). **Corollary**: the line and the conic meet **exactly at the two Nariai configurations**, $r_0=\pm1/\sqrt3$, which are the endpoints of the ellipse's minor axis.
② REGISTER — **PROPOSITION AND COROLLARY**, proved and receipt-anchored. The conic is not new — it is the 2012 dissertation's fundamental ellipse, obtained there from the scale-invariant line element; **what is added is the reading**: that the locus factors as a line and a conic, that the tilt is $45^\circ$, and that the components meet at Nariai.
③ HOME — P3 §4.4 (`sec:ellipse`), `prop:locus`, `cor:nariai-locus`.
④ ANCHOR — `P03_cubic_factor_ellipse_locus`, `Q5_nariai_on_the_locus`; ledger `algebraic_geometry`.
⑤ JOINS — [[p5-groupoid]] (σ as the diagonal reflection of this ellipse, $R$ as the anti-diagonal one) · [[p12-algebroid]].
⑥ NOT OP FOR — **The corollary adds no new value; it locates one already fixed three ways**, and P3 says so: Nariai is *algebraically* the double root and σ's fixed point, *incidence-geometrically* the singular point of the reducible cubic where line meets conic, and *metrically* the end of the minor axis. **And the anti-diagonal is the geometrically meaningful axis**: the negative root that appears whenever the other two are positive is **not a bookkeeping artefact and not unphysical** — it is the horizon reached in the backward radial direction.

### the-two-routes-the-construction-does-not-take
① CLAIM — At $w=0$ the cut is one curve — the equator taken diametrically, which is P2's Schwarzschild curve — carrying **two readings** exchanged by the backward-radial vantage-swap. That is the de Sitter↔Schwarzschild correspondence, **exact, at fixed $\alpha$, and neither a limit nor a mass relabelled to zero.** P3 states plainly the two routes it does *not* take, because each reaches the same throat in a way that breaks the construction. **① Schwarzschild is not the $\alpha\to\infty$ limit**: $\alpha$ is the fixed invariant the whole construction lives inside, and sending it to infinity dismantles the throat, the circle and the family in one stroke. **② $r_0=0$ is not a "massless Schwarzschild"** — a contradiction in terms, since Schwarzschild is the geometry with a mass and the cosmological term off, and $M=0$ with the term on is de Sitter by definition.
② REGISTER — **STATED AS TWO EXCLUSIONS**, each with its reason.
③ HOME — P3 §5.4 (`sec:two-readings`).
④ ANCHOR — none.
⑤ JOINS — [[p2-janzen-circle]] · [[p5-groupoid]] · [[p17-geometric-core]].
⑥ NOT OP FOR — **⛔ These are the two misreadings most available to a reader and they are both natural**, which is why the paper names them rather than relying on the guard elsewhere. *Any synthesis sentence taking a limit of this construction has taken route ①.*

### charge-is-R-even-and-mass-is-R-odd
① CLAIM — Reading the eigenspace split on the charged cut settles, **at the geometric level**, where charge sits in the construction's one discrete symmetry: mass is $R$-**odd**, charge is $R$-**even**. Charge conjugation is the **field-level** closure, adjoining an independent $\mathbb Z_2$ to $\mathrm{Aut}(A_2)=D_6$.
② REGISTER — **RECEIPT-ANCHORED**, and scoped to the geometric level at source.
③ HOME — P3 §5.5 (`sec:charge`).
④ ANCHOR — `P03_charge_parity`.
⑤ JOINS — [[p13-boundary]] (**where charge conjugation's factorisation into a geometric kinematic face and a field-level charge sign is developed**) · [[p14-matter-sector]] · [[p5-groupoid]].
⑥ NOT OP FOR — **The geometric level is not the field level, and the paper keeps them apart** — the parity assignment is geometric; the conjugation that closes it is not, and adjoins a *separate* $\mathbb Z_2$ rather than living inside $D_6$.

### the-temporal-three-ness-and-why-everything-closes-in-elementary-terms
① CLAIM — The turnaround's three-ness **is the deck action of cosmic time's own imaginary period**: $\tilde\tau\mapsto\tilde\tau+2\pi i\alpha/3$ leaves $r^3$ invariant and permutes the cube-root sheets cyclically, so the turnaround cubic's $\mathbb Z_3$ and that period are one object. **And this answers a question the construction raises everywhere — why everything here closes in elementary terms.** The period is a *single* one ($\sinh^2$ has the one period $i\pi$, no real period, none with both parts nonzero), so the quotient is a cylinder and the law is a rational function of $e^{3\tilde\tau/2\alpha}$. *A singly periodic meromorphic function is elementary; a doubly periodic one is elliptic, and no elementary closed form exists for the second.* The same holds on the horizon side, where $\sin3w$ carries the single real period $2\pi/3$. **Each of the two three-nesses is one singly periodic elementary function composed with a three-fold** — and that, not any convenience of presentation, is why $\sinh^{2/3}$, $\sin3w$ and $\sigma$ all admit closed forms.
② REGISTER — **RECEIPT-ANCHORED**, twice.
③ HOME — P3 §6.2 (`sec:temporal-threeness`).
④ ANCHOR — `P03_turnaround_temporal_threeness`, `X2r_single_periodicity`.
⑤ JOINS — [[p7-cr-framework]] (**the half-period $i\pi\alpha/3$ is what places the collapse wings, and the interval it fixes is the lift**) · [[p5-groupoid]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **⛔ The two three-nesses are affinely inequivalent and P3 does not identify them** — it says what the temporal one positively *is*, which the separating statement alone does not. **And the asymmetry between them runs deeper than the inequivalence**: the temporal $\mathbb Z_3$ **factors through a half-period that exchanges the branches**, matter leg to conjugate leg; the spatial $S_3$ carries no exchange inside itself, since $f=0$ is a condition on $r$ alone and carries no shift of $\tilde\tau$. *The asymmetry is one of where the exchange sits, not of whether one exists* — the spatial side has its branch exchange in $R$, which maps one Nariai triple to its conjugate twin: an exchange **between** the two Nariai members rather than inside one member's $S_3$.

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

> **▣ THE READ IS COMPLETE** *(first pass r4039--r4041, completed r4063 after the stocktake found the
> rigidity, seam, diagnostic, cosmological-completion, algebroid and closing sections unopened). The three
> entries at the end of this block are results the first pass had no sight of.*

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


### dimensional-collapse-and-what-alpha-is
① CLAIM — The algebraic content of the slicing paper's rigidity. The slicing space $\mathcal V_\alpha$ is a **continuous** manifold parametrised by $r_0\in(-2/\sqrt3,2/\sqrt3)$, but **its image under "slicing ↦ underlying manifold" is a single point**: the de Sitter manifold of throat radius $\alpha$. So a continuous parameter space collapses onto one geometric invariant, with the discrete morphisms permuting the labels of a single member and the continuous variation of $r_0$ producing no variation in the manifold. **Within the groupoid, $\alpha$ is the unique chart-invariant quantity available** — so any candidate for a *fully* invariant gravitational mass must be built from $\alpha$ and not from the slicing-dependent $M$.
② REGISTER — **PROPOSITION** (`prop:dim-collapse`), with the relation and the degeneracy credited to the 2012 dissertation, which already records that the three roots form one triplet.
③ HOME — P5 §4 (`sec:rigidity`), §4.1–§4.3.
④ ANCHOR — none.
⑤ JOINS — [[p3-sds-slicing]] · [[p17-geometric-core]] · [[p12-algebroid]].
⑥ NOT OP FOR — **⛔ The mass question is sharpened here and settled elsewhere, and the answer is negative**: the standard quasi-local and asymptotic definitions (Misner–Sharp $M+r^3/2\alpha^2$, Komar $M-r^3/\alpha^2$, ADM, Bondi) all return the slicing-dependent $M$. *$\alpha$ is the invariant curvature **radius**, a length, not a mass* — which P3 records as confirming rather than weakening the reading, the conventional mass being the projection.

### the-seam-is-a-partial-involution-and-why-partial
① CLAIM — The seam continuation $\xi$ is a vantage-change of a kind **distinct from** the within-single-geometry morphisms, and P5 gives the reason it is called *partial*: **it does not act within a single sky-angle fundamental domain.** $\sigma$ and $\tau$ permute the six labelled positions on the sky-angle circle *within* a regime; $\xi$ acts on the analytic continuation into the complex parameter plane, moving **between the two real slices** of one analytic object, where the spherical and de Sitter regimes sit. **The overcritical continuation is a further partial involution** of the same kind, relating an under-critical vantage to an overcritical one at the same $\alpha$ past the Nariai crest.
② REGISTER — **ESTABLISHED**, with the two structures named complementary rather than nested.
③ HOME — P5 §7 (`sec:seam`), §7.1–§7.3.
④ ANCHOR — none.
⑤ JOINS — [[p3-sds-slicing]] · [[p13-boundary]] · [[p17-geometric-core]].
⑥ NOT OP FOR — **⛔ Three kinds of move, and the paper keeps all three apart**: $\sigma,\tau$ act *within* a regime; $\xi$ moves between Riemannian and Lorentzian pieces of one curve; the overcritical involution moves between under- and over-critical regimes of the cubic. **And a fourth is explicitly not addressed** — vantages between distinct $\alpha$, which are left to the open section and resolved there as the continuous homothety.

### the-sweep-diagnostic-and-its-honest-limits
① CLAIM — The sweep result supplies a **diagnostic for the programme**, stated as a procedure: identify the sweep used to produce the chart; identify the point about which it is pivoted; check whether that point is the manifold's own axis of symmetry or a selected point off it. **Schwarzschild is the canonical case and its horizon–singularity asymmetry the canonical sweep artefact.**
② REGISTER — **DIAGNOSTIC**, stated as the perspectival reading's interpretive payoff and *explicitly not as a further proposition of the construction*.
③ HOME — P5 §8.4 (`sec:diagnostic`), and `rem:wider`.
④ ANCHOR — `P03_acceleration_is_slice_curvature`.
⑤ JOINS — [[p2-janzen-circle]] · [[p3-sds-slicing]] · [[p9-range-paper]] · the $r=0$ cross-paper join above.
⑥ NOT OP FOR — **⛔ P5 says plainly "other applications of the diagnostic await development"** — the reach beyond Schwarzschild is asserted for the *reducible* sector on the range paper's authority, and the **irreducible interior reassignments are outside the sector the diagnostic is stated on**. *What is open there is named precisely and is a real physical question*: whether a charged **collapse** forms the inner horizon at all — the eternal solution carries one, but if a dynamical collapse does not, the branch point survives and the case rejoins the uncharged construction.

### the-two-groupoids-are-not-the-same-object
① CLAIM — The algebroid the companion constructs is an **action** algebroid, $\mathfrak{so}(5,1)\ltimes\mathcal C$, and an action algebroid is always integrable, its integrating object the action groupoid $\mathrm{SO}(5,1)\ltimes\mathcal C\rightrightarrows\mathcal C$ — **objects cuts, arrows the isometries carrying one cut to another**. *That is not the groupoid $\mathcal G$ of this paper, whose objects are vantages on one geometry.* And the Nariai point of the branched cover coincides with the stratum at which the algebroid connection vanishes and the substrate's isotropy enhances — a structural meeting of the discrete and continuous faces of one solution space.
② REGISTER — **NAMED AND SEPARATED**, in the vocabulary of the field the objects belong to.
③ HOME — P5 §9.5 (`sec:nariai-algebroid`).
④ ANCHOR — none; cites Mackenzie for the integrability of action algebroids.
⑤ JOINS — [[p12-algebroid]] · [[p3-sds-slicing]].
⑥ NOT OP FOR — **⛔ This is the confusion most available to a synthesis and P5 forestalls it explicitly.** Two groupoids appear in the corpus with different objects — *vantages on one geometry* against *cuts of the substrate* — and they are separated by dimension exactly as the companion separates their operations. **Conflating them merges a description structure with a solution space.**

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

> **▣ THE READ IS COMPLETE** *(first pass r4043, completed r4065 after the stocktake found the back half of
> least-arbitrariness, the modal-fallacy section and the constructive ordering unopened).*

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


### the-boundary-is-a-populated-class-with-an-edge
① CLAIM — The register's boundary is not one exception but **a class with three members and two near-misses**, and the near-misses are what give it an edge. **Members** (discrete, leaving the symmetry maximal, fixing no breaking, hence beyond the criterion's reach): the **dimension**; the **number of layers** in the ontology — *the programme's founding move rather than a detail of it*; and **which real form** of the complexified structure is taken as existent. **Not members**: the **signature**, which is not an unforced choice at all, being intrinsic to positive curvature; and the **orientation**, which is not a choice because the configuration's symmetry group is transitive on the objects that would distinguish one.
② REGISTER — **RECEIPT-ANCHORED SURVEY**, run against the definition of a modulus.
③ HOME — P6 §4.1.
④ ANCHOR — `P06_the_boundary_is_a_class`.
⑤ JOINS — [[p17-geometric-core]] · [[p13-boundary]] · [[p14-matter-sector]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ The members are not settled the same way, and that difference is the more interesting half.** The dimension is settled by *content*. The layering is settled by the existence criterion itself — *it is the leaf that carries the clock* — so the criterion is silent on the **number** while deciding which layer is existent, **a subtler position than silence.** **And the real form is recorded as having WEAKENED**: the colour structure that had been the reason to take the compact face seriously turns out not to be an isometry of either real form, being carried instead by the branch structure of the signed radius — *so one motivation is removed and the choice stands more exposed than it did.* P6 files that as it falls, which is what a subsection announcing a boundary should be willing to do.

### where-form-is-silent-content-may-still-decide
① CLAIM — **A choice the criterion cannot reach need not be free.** The dimension is settled, within the framework, by *content*: the matter sector's two deliverables do it. The fold its generation count reads is $D-1$ and exists at all only where a single slicing scale removes the residual harmonics — **four and five spacetime dimensions and no other** — while the mass-parity grading chirality exists only in **even** dimension. **Four is therefore the only dimension carrying both a generation count and a handedness.**
② REGISTER — **DERIVED**, from two companion results whose intersection is the answer.
③ HOME — P6 §4.1.
④ ANCHOR — none; cites [[p3-sds-slicing]] and [[p14-matter-sector]].
⑤ JOINS — [[p3-sds-slicing]] (the $D=4$/$D=5$ dimension result) · [[p14-matter-sector]] (the parity that breaks the tie) · [[p17-geometric-core]].
⑥ NOT OP FOR — **⛔ Three miscountings P6 forecloses in its own voice, and all three are ways a synthesis could inflate the record.** ① *Not a sixth instance of the criterion* — the instances are five applications, this is a boundary, and counting a case where the criterion was **silent** as one where it **worked** is the survivorship error run in a new direction. ② *Not an instance of the engine's pattern* — that pattern is a selection made on least-arbitrariness **before** its discriminator arrived; here the discriminator was already in hand and the selection is made **by** it, so *the vindication lemma's exposure is exactly what it was.* ③ *Not a weakening of Rule 2*, which was exercised on live material in the same enquiry and discriminated correctly without being told which way to go: asked whether a higher-dimensional substrate could supply colour as an isometry, it found the structure group **permits** one — $\mathfrak{so}(6)$ reducible to $\mathfrak{su}(3)$ only given a complex structure and a volume form **nothing in the construction supplies** — and Rule 2 condemns that as no explanation but a description. *One enquiry, one requirement and one permission, told apart by the criterion rather than by preference.*

### the-constructive-ordering
① CLAIM — The imperative fixes a **direction of construction**, and inverting it is the standing error of which naïve realism is the local symptom. The valid order: **ontology ← evidence; kinematics ← ontology; coordinates ← kinematics.** The reification error runs the chain backward — taking the coordinate system as given and reading an ontology off it, treating the map as the territory and an apparent symmetry of the description as a fact about the world. **Applied to a mature mathematical theory the demand is sharper than it first appears**, because there the appearances include not only what is seen but *the formal structures one has derived*: the rule becomes **resist reifying the coordinate system, and ask what world must exist for the appearances and for the formal structures alike to make sense.**
② REGISTER — **STATED**, as the imperative's constructive form.
③ HOME — P6 §6.
④ ANCHOR — none.
⑤ JOINS — [[p7-cr-framework]] (the four-manifold as coordinate scaffold) · [[p4-modern-parallax]] · [[p10-canonical-time]].
⑥ NOT OP FOR — *This is the ordering the whole corpus claims to follow, so it is also the standard the corpus is checkable against.* **A result reached by reading an ontology off a formalism has run the chain backward** — which is the charge P6 levels at the standard reading, and the one the corpus must not itself incur.

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

> **▣ THE READ IS NOW COMPLETE** *(r4049--r4057, after the partial claim at r4047 was corrected). Every
> section has been read straight through. The entries below were revised against the whole paper, and the four
> added at the end are results the partial read had missed entirely.*

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
⑥ NOT OP FOR — **⛔ That the map is not metric is precisely what makes the symmetry claim work**, and it is the hinge a synthesis is likeliest to drop. Because the correspondence carries no multipoles, **non-spherical collapse is dissolved rather than deferred**. *An entry that presents the correspondence as a metric identification has inverted its content and lost the any-symmetry result with it.* **⛔ AND THE PROOF BOUNDS ITS OWN MAP, which the shorthand loses**: $\mathcal N$ is *fixed to a single causal type* — an oriented future-horizon-of-an-observer identification, far from one isomorphism among the many any two $S^2\times\mathbb R$ null boundaries would admit — **rather than uniquely determined.** It carries no metric data (the areas $16\pi G^2M^2/c^4$ and $4\pi\alpha^2$ and the two surface gravities are unequal in general), and the collapse horizon supplies **no canonical labelling 2-sphere**, so a reframing of that $S^2$ remains free. **And the bijection is sharper than a seeding**: $p\mapsto\mathcal H_c^+(p)$ is injective because the *oriented* future sheet distinguishes $p$ from its antipode where the unoriented bifurcate horizon does not, and onto by the ruling structure — so *the family of horizons **is** the congruence*, no single 2-sphere of generators extended to fill the $S^3$. One-per-point holds **by construction** and not because the rulings are straight; through each point of $\mathrm{dS}_4$ runs an $S^2$ of null directions.

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

### the-graded-dissolution-cluster
① CLAIM — **P7's applications synthesis grades the cluster rather than presenting it as uniform, and says why the grading matters: it is a difference in what an objector must dispute.** *Tier one*, carrying the layered reading's full weight: the horizon–singularity family, the problem of time, the hole argument, the closed timelike curves. *Tier two*, following from the single scale alone: the fine-tuning pair and the local–cosmic boundary. *Tier three*, standing on the bare analytic structure and **untouched by any verdict about what exists**: the continuation through the curvature singularity, the identical analytic type of the two critical points, the Kretschmann divergence as a pole of *finite* order (twelfth in the cycloid parameter, raised from six by the chain rule — *a pole being continuable where an essential singularity would not be*), and the overcritical regime reached by the same continuation that joins the seam.
② REGISTER — **SYNTHESIS with an explicit grading.**
③ HOME — P7 §4.11 (`sec:applications-synthesis`).
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] · [[p2-janzen-circle]] · [[p3-sds-slicing]] · [[p6-shadow-of-existence]].
⑥ NOT OP FOR — **⛔ This is the shape our own synthesis needs, and flattening it is the failure mode.** A reader who rejects the layered ontology still owes an answer to tier three; presenting the cluster as one uniform move hands them the whole set to reject at once.

### the-lift-carries-a-sharp-separation
① CLAIM — Because no cosmic time elapses on the lift, **any quantity whose value depends on elapsed cosmic time is necessarily continuous across it, having no time in which to change**, while quantities depending on path length or on $\operatorname{Im}\tilde\tau$ may differ across it. The kernel carrying a state across is not the unitary $e^{-i\hat H\Delta\tau}$ but the Euclidean $K=e^{-\hat H|\Delta\eta|}$ — consistent with the evolution operator being the identity, since no cosmic time elapses. **That kernel acts on *oscillatory* content only**, a frozen zero-frequency mode being a fixed point of it; and at the crossing no mode is oscillating, since on the contracting leg $aH$ grows without bound so every mode exits the comoving horizon and freezes first. *So what the segment removes is the sub-horizon oscillation — the acoustic phase — and not the frozen amplitude that crosses.*
② REGISTER — **DERIVED**, with the classical selection rule recovered term for term.
③ HOME — P7 §8.
④ ANCHOR — `P16_every_mode_is_frozen_at_the_crossing`.
⑤ JOINS — [[p10-canonical-time]] (**the state the kernel selects is the one that companion fixed on independent grounds — one requirement met twice**) · [[p15-cr-cosmology]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **No information is destroyed on the realised spacetime; a basis is selected on it.** *Lossless for content and fatal for bodies* — the paper's own phrasing, and the two halves must travel together.

### the-general-reach-and-its-three-axes
① CLAIM — The same construction reaches the whole **symmetry-reducible vacuum sector** of general relativity: a geometry is a cut of the substrate precisely when its isometry group contains a sweep-subgroup of the substrate's. The apparent multiplicity of the catalogue decomposes on **three orthogonal axes**: *vantage* — a finite groupoid of causal readings of one fixed cut; *geometric* — the moduli of genuinely distinct vacuum cuts, with mass, rotation and NUT charge transverse to the orbits; and *matter* — charge and acceleration entering as **bends off the kernel** rather than as cuts. So the reducible catalogue is **one substrate read through a finite vantage groupoid, over a moduli family of vacuum cuts, with matter the bend**. Algebraic type is no constraint (types O, D, I all filled).
② REGISTER — **SYNTHESIS of companion results**, each cited.
③ HOME — P7 §9 (`sec:general-reach`).
④ ANCHOR — none.
⑤ JOINS — [[p8-slicing-operator]] · [[p9-range-paper]] · [[p12-algebroid]] · [[p5-groupoid]].
⑥ NOT OP FOR — **⛔ Two limits stated at source.** The classification leaves open the **irreducible interior remainder** — the Kerr-inner and Reissner–Nordström-interior reassignments, which tie to the matter side. **And the branch point and the Nariai member are not the same locus**: the branch point is at $r=0$, the Nariai member is seeded at $\alpha/\sqrt3$, and the paper lists these as quantities never to be conflated.

### the-scalar-sector-is-a-disagreement-and-the-paper-says-so
① CLAIM — **⛔ P7's own frontier list states an outright disagreement with data, in numbers.** The full-spectrum likelihood comparison against flat $\Lambda$CDM returns $\chi^2=397.13$ for this construction against $206.44$ for the standard model over the 215 binned $TT$ multipoles, at **equal fitted-parameter count** and against a control reproducing the sky at $0.983$ per degree of freedom; and the asymptotic acoustic phase intercept sits $0.615\,\ell_A$ from the sky's, **some seventy standard deviations** at the peak-position accuracy the data supports. What *does* come out right: the acoustic scale, the peak spacing, the damping physics, and the odd/even height pattern ($P_1/P_2=2.185$ against $2.2564\pm0.0772$ measured). **The diagnosis: the construction reproduces the acoustic scale, the peak spacing, the damping physics and the height pattern, and misplaces the phase.**
② REGISTER — **≈ COMPUTED, AND A DISAGREEMENT.** *Both items run; the result is a disagreement rather than a closure, and the paper says exactly that.*
③ HOME — P7 §10, frontier item 1.
④ ANCHOR — the companion cosmology's.
⑤ JOINS — [[p15-cr-cosmology]] (**owns the calculation**) · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **⛔ THIS IS THE SINGLE MOST IMPORTANT ENTRY IN THE P7 BLOCK FOR THE SYNTHESIS, AND IT IS THE ONE MOST EASILY LOST.** A results paper that lists what the corpus delivers and omits this has misrepresented the corpus, because the corpus itself does not omit it. **What remains is a diagnosis rather than a calculation**: whether the misplaced phase is a defect of the seam treatment, of the transfer, or of the geometry the transfer runs on is the open question — *and the paper notes it is a sharper question than the item it replaces.* **The related frontier note is equally load-bearing**: the uniform comb follows from an ordering that is **not adjustable** — the acoustic modes re-enter above the onset, so none crosses while there is a plasma to be driven, and the nucleosynthesis plasma is the progenitor's, complete before the branch point.


---

# ⛭ READ-COVERAGE STOCKTAKE · P1–P7
### *Measured, not recalled — because "read and harvested" is a claim, and it was got wrong once*

> **⌗ WHY THIS EXISTS.** *r4047 claimed P7 was read when about 15% of it had been. That was caught by Daryl
> asking a direct question, not by any instrument. So the same question is asked of every earlier paper, and
> answered by what can actually be attested rather than by impression. **A partial harvest looks exactly like a
> complete one**, which is why this has to be written down.*

| paper | body words | coverage | verdict |
|---|---|---|---|
| **P1** | 12,085 | read sequentially from the masthead to the bibliography, no section skipped | **complete** |
| **P4** | 5,906 | completed r4059 — the two floor subsections and the whole history section had been skipped | **complete** |
| **P2** | 13,604 | re-read r4067 without filters, every section | **complete** |
| **P6** | 13,134 | completed r4065 — the back half of least-arbitrariness, the modal-fallacy section and the constructive ordering had not been opened | **complete** |
| **P5** | 16,558 | completed r4063 — rigidity, the seam section, the diagnostic, the cosmological-completion section, the algebroid subsection and the closing had not been opened | **complete** |
| **P3** | 28,931 | completed r4061 — the horizon-locus, two-readings, charge, temporal-three-ness, rigidity-groupoid, coupled-operations and closing sections had never been opened | **complete** |
| **P7** | 43,900 | every section, r4049–r4057 | **complete** |

**⌗ WHAT A PARTIAL READ DEMONSTRABLY MISSES — the two failure modes now have names, from cases.**
*① **Results living only in the front matter.** Found in P3 (seven), P5 (one), P7 (three). A probe by technical
marker finds these; a probe by sentence window does not, since it flags paraphrase as absence.*
*② **Formulas that read as scrupulousness.** "Coherence and not correspondence", "self-consistency is not
soundness" — three printed occurrences across three papers, and **I read past the P6 one on a first pass**. It
was caught only by meeting the same formula again in P7 and then grepping. **So this class is not caught by
reading carefully; it is caught by recognising a repeat.** A first pass over a single paper is the wrong
instrument for it, and a corpus-wide grep is the right one.*

**⌗ AND A THIRD CLASS NO INSTRUMENT SEES AT ALL: LaTeX comments.** *arXiv distributes `.tex` source. One
working comment in P7 was found by reading and neutralised (r4051); a grep for the specific words found nothing
else, but that is a weak check — a stale instruction, a private judgement of a named person, or an unresolved
note to self carries the same risk and matches no keyword. **A comment sweep is owed and is its own pass.***


---

# P8 · `corpus/slicing_operator.tex`
### *Covariance of geometries over the de Sitter substrate: the slicing operator, the vacuum kernel, and matter as the bend*

> **▣ THE READ IS COMPLETE** *(front matter r4073, body r4075). P8's row is semi-independent and sequential,
> joined to P9. It may use P1--P7.*

### the-covariance-is-one-level-above-general-relativity's
① CLAIM — General relativity holds **a single geometry** invariant under change of chart; this construction holds **the de Sitter substrate** invariant under change of *geometry*, with the slicing curve as the gauge object. *"Many line elements, one geometry" becomes "many geometries, one substrate."*
② REGISTER — **A READING, and P8 labels it as one.** *"We will state which parts of this are theorems and which is the reading the theorems ground."* The theorems — vacuum kernel, bend-density identity, lapse split, cosmological geodesic, second-ruling embedding — are computed and verified; **the covariance reading is adopted on their strength and explicitly does not follow from them as a corollary follows from a theorem.**
③ HOME — P8 §1.
④ ANCHOR — none.
⑤ JOINS — [[p12-algebroid]] (where the reading is formalised) · [[p17-geometric-core]] · [[p9-range-paper]].
⑥ NOT OP FOR — **⛔ The separation of theorem from reading is stated at the outset and is the model for how the synthesis should carry this material.** *The results ground the structural reading; they do not entail it, and P8 says "we do not claim more."*

### the-vacuum-kernel
① CLAIM — In the construction gauge, $T_{\mu\nu}=0$ **is** the first-order linear ODE $rf'+f-1+\Lambda r^2=0$, whose **entire** solution space is $f=1-2M/r-\Lambda r^2/3$ — the whole SdS family with $M$ the single constant of integration. *The vacuum sector is exactly the kernel of the matter functional, derived rather than matched: **straight cuts are vacuum**.* With the bend section showing every density is realised by some cut, the functional is onto as well, so the two together give **a kernel of dimension one over a vanishing cokernel — a Fredholm index of 1**, generated by that constant.
② REGISTER — **THEOREM**, proved by substitution with the angular component discharged via Bianchi.
③ HOME — P8 §3, `thm:kernel`.
④ ANCHOR — the section's own.
⑤ JOINS — [[p9-range-paper]] · [[p3-sds-slicing]] (which uses this at general $D$) · [[p7-cr-framework]].
⑥ NOT OP FOR — **The index reading is not a relabelling and P8 says why**: an index is stable under deformation, so it says the one free constant survives *every* perturbation of the operator that keeps it Fredholm — which is more than this particular equation having a one-parameter solution set.

### the-question-this-answers-was-asked-in-2012
① CLAIM — The essay that first developed this cosmology named the objection it could not meet: *"if the geometry is not determined by the world-matter, then by what?"* — and answered, *"a detailed answer to this question has not been worked out."* **The vacuum-kernel theorem is that answer.** The geometry is not chosen and not read off the matter: $T_{\mu\nu}=0$ in this gauge *is* a first-order linear equation whose entire solution space is the one-parameter family, so the substrate determines the vacuum sector and the matter is read off as the bend of a cut of it.
② REGISTER — **PROVENANCE**, cited to the 2012 essay.
③ HOME — P8 §3, `rem:byWhat`.
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (Einstein 1917 runs content → scale; this runs the other way) · [[p17-geometric-core]].
⑥ NOT OP FOR — *This is the corpus closing a gap it had itself flagged thirteen years earlier, in the flagging author's own words — which is a stronger form of the claim than asserting the result cold, and the synthesis should carry it that way.*

### matter-is-the-bend-and-the-reading-is-not-spherical
① CLAIM — Writing any curve as a departure from the vacuum profile, $f=1-2m(r)/r-\Lambda r^2/3$, gives $8\pi T^t{}_t=-2m'(r)/r^2$: the energy density $\rho=m'(r)/4\pi r^2$ **is the radial growth-rate of enclosed mass**, the bend of the curve off the constant-$M$ profile. Checked on a non-vacuum member: Reissner–Nordström–de Sitter is the bend $2m(r)=2M-q^2/r$, returning the electromagnetic stress-energy off its $q^2/r^2$ term. **And the reading is not an artefact of the symmetry**: for a general leaf the density is the leaf's intrinsic-curvature departure from the substrate, $16\pi\rho={}^3R+K^2-K_{ij}K^{ij}-2\Lambda$ — **which is the Hamiltonian constraint**, the spherical identity being its symmetric case.
② REGISTER — **PROPOSITION**, proved, with the general-leaf statement identified as a known constraint rather than a new one.
③ HOME — P8 §4.
④ ANCHOR — the section's own.
⑤ JOINS — [[p9-range-paper]] · [[p11-dynamics]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ The identity states WHAT the bend is, not WHY a leaf bends as it does.** *That is the dynamics, and P8 names it as treated elsewhere and open here.*

### the-lapse-split-separates-the-operator's-data
① CLAIM — With the temporal datum $A$ freed from the spatial profile, $G^t{}_t$ involves the spatial profile **alone**, while the difference $G^r{}_r-G^t{}_t=(f/r)\dd_r\ln(A/f)$ carries the radial pressure — so the lapse enters *only* through that logarithm, and setting $A=f$ annihilates it, returning $p_r=-\rho$. **The operator therefore separates into independent data**: the **leaf** carries the three-geometry and, through its bend, the density (planar → vacuum, bent → density); the **stacking** carries the radial pressure (locked → the rigid vacuum equation of state, unlocked → general $p_r$); the **vantage** carries the signature.
② REGISTER — **PROPOSITION**, proved by direct computation.
③ HOME — P8 §5.
④ ANCHOR — the section's own.
⑤ JOINS — [[p9-range-paper]] (**where the shift is added as the fourth datum, rotation being neither leaf nor lapse**) · [[p7-cr-framework]] · [[p10-canonical-time]].
⑥ NOT OP FOR — **The single locked curve reaches only the $p_r=-\rho$ sector.** *The lapse split is what shows the lock is a restriction rather than a feature of the construction.*

### the-three-constant-curvature-leaves-and-the-flat-one-as-output
① CLAIM — The maximally symmetric spatial sections of the substrate are of exactly three kinds, sorted by the character of the held direction: a timelike direction held fixed gives the round $S^3$ — the **closed** leaf; the null cone $r=\alpha$ gives the horosphere — the **flat** leaf; the third is the **open**, negative-curvature leaf. With it the cosmological sector closes over the full FLRW family of spatial curvatures, dust carried in each case as the bend, the Friedmann equation appearing with its curvature term **being the leaf's own intrinsic curvature** ${}^3R=6k/a^2$.
② REGISTER — **PROPOSITION**, proved from the embedding.
③ HOME — P8 §9, `prop:trichotomy`; and §8 for the second-ruling identification.
④ ANCHOR — the sections' own.
⑤ JOINS — [[p7-cr-framework]] · [[p15-cr-cosmology]] · [[p3-sds-slicing]].
⑥ NOT OP FOR — **⛔ The flat leaf is the construction's OUTPUT rather than its input, and the two selections a reader would expect to be independent are not.** $E=1$ is fixed by the field, at the radius where the potential vanishes; $E=1$ **is** the flat leaf $k=0$; and the companion's identification of the degenerate member as the unique non-pivoting cosmological cut fixes the mass. *So the curvature and the mass are each fixed, not chosen.* **And the two turning cubics the framework keeps apart are the $k=1$ and $k=0$ ends of one family** separated by the curvature term — the depressed form being the **versal unfolding of the $A_2$ singularity**, so the family is the complete one rather than a convenient parametrisation.

### the-synchronous-space-is-the-second-ruling
① CLAIM — The flat synchronous space **is the second null ruling** of the hyperboloid — the horospheres normal to the common past asymptote — so the lapse–shift, the synchronous slicing and the second ruling are **one object**. The $t=-\infty$, $r=0$ singularity of the comoving reading is therefore the artefact of that reading laid over a throat which is the substrate's own scale $\alpha$: *the radius-face of a category error whose time-face is taking the chart's $-\infty$ for the physical age.*
② REGISTER — **ESTABLISHED**.
③ HOME — P8 §8.
④ ANCHOR — the section's own.
⑤ JOINS — [[p2-janzen-circle]] · [[p3-sds-slicing]] · the $r=0$ cross-paper join above (**this is the sharpest single statement in that chain**).
⑥ NOT OP FOR — **⛔ Scoped to the COSMOLOGICAL face.** *Whether the same sentence covers the collapse face is not settled here — which is the check the $r=0$ join flagged, and it remains open after the read.*

### p8-scope-and-opens
① CLAIM — Stated at source: everything proven is **static and spherically symmetric, or its spherical-cosmological reassignment**, and *within that sector the operator is complete* — the cut generates the geometry, the bend the density, the lapse the pressure, the vantage the signature, the substrate invariant under all of it. Two questions are placed and not answered here: **the range** over the rest of general relativity (settled in P9), and **the emergence of the bend** — why a given leaf bends as it does.
② REGISTER — **SCOPE, stated plainly**, with the range named as answered elsewhere and the emergence as open.
③ HOME — P8 §10.
④ ANCHOR — none.
⑤ JOINS — [[p9-range-paper]] · [[p11-dynamics]].
⑥ NOT OP FOR — *A completeness claim confined to a named sector is the honest form, and it is the form the synthesis should reproduce: **complete within the sector, silent outside it**.*


---

# P9 · `corpus/range_paper.tex`
### *The range of the de Sitter slicing operator: rotation, algebraic type, and the wall of inhomogeneity*

> **▣ THE READ IS COMPLETE** *(front matter r4071--r4073, body r4077). P9 is P8's joined partner: P8 asks what
> the operator IS, P9 asks how far it reaches.*

### the-bound-and-that-it-is-attained
① CLAIM — A swept geometry inherits the sweep's symmetry, and the sweep is by isometries of the substrate, so **every reachable geometry carries an isometry group containing a sweep-subgroup of $\mathfrak{so}(5,1)$** — the range is bounded above by the symmetry-reducible sector. The body then fills that bound class by class. **The argument's shape is named at source**: bounding a reachable class above by a necessary condition and showing the bound attained is how one computes the image of a construction up to isomorphism, and the necessary condition here is the same sentence the geometric core uses to say what a cut *is*.
② REGISTER — **THEOREM** (`thm:bound`) for the bound; **THEOREM** (`thm:range`) for the range.
③ HOME — P9 §2 and §8.
④ ANCHOR — `K7_range_is_essential_image`.
⑤ JOINS — [[p8-slicing-operator]] · [[p17-geometric-core]] · [[p12-algebroid]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **The bound is an INCLUSION**, and it is an equality only at the strata where an isotropy is tabulated. *The restriction is structural, not a limit of the survey*: a cut's isotropy preserves the second fundamental form as well as the induced metric, so the two coincide only where the symmetry is large enough to fix the embedding too. **The low-symmetry classes — Type I, Kerr–de Sitter, the wall — are exactly where they need not coincide.**

### in-class-surjectivity-and-what-the-content-actually-is
① CLAIM — Within a reachable class the operator's four data — **leaf, lapse, shift, vantage** — supply exactly the functions the general invariant metric admits, so the cut spans the class.
② REGISTER — **PROPOSITION**, established case by case.
③ HOME — P9 §3.
④ ANCHOR — none.
⑤ JOINS — [[p8-slicing-operator]] (the spherical case).
⑥ NOT OP FOR — **⛔ P9 says plainly that the surjectivity is NOT the content.** *"Once the cut carries the class's function count, the cut ansatz is the general invariant metric, and spanning is near-tautological."* **The content is the identification of the vacuum members as the substrate's family — the kernel — and of matter as the bend.** *A synthesis that reports "the operator is surjective on the sector" as the result has reported the near-tautological half.*

### rotation-is-the-shift
① CLAIM — Every symmetric cut is block-diagonal, because a symmetric sweep makes the orbits orthogonal to the cut — so it cannot carry the cross term $g_{t\phi}$ in which frame-dragging lives. **Rotation is therefore neither the leaf nor the lapse but the shift**, the off-diagonal datum the spherical and homogeneous cuts set to zero. And **angular momentum needs both the offset and the twist**: $J=Ma$, *the offset alone is Schwarzschild–de Sitter, the twist alone is de Sitter.* The mass-free rotation-only limit is not merely vacuum but **maximally symmetric** — its Riemann tensor is the constant-curvature form — so the twist alone is a rotating, oblate slicing of the substrate itself and **not a new geometry**.
② REGISTER — **PROPOSITION**, proved.
③ HOME — P9 §5.
④ ANCHOR — the section's own.
⑤ JOINS — [[p8-slicing-operator]] (which has three data; the shift is the fourth) · [[p7-cr-framework]] · [[p11-dynamics]].
⑥ NOT OP FOR — *Naming which datum is which fixes the cosmological reading with no room for a wrong turn* — the leaf's bend is the matter, the lapse is the stacking rate the observable expansion rides.

### the-separable-type-D-vacuum-kernel
① CLAIM — The separable (Carter) cut is vacuum-$\Lambda$ **if and only if** its structure functions are **quartics**, with the leading coefficient $-\Lambda/3=-1/\alpha^2$ of both **pinned by the substrate**. The four free coefficients are the mass, the rotation, the NUT charge and a coordinate normalization — so the rotating vacuum kernel is the complete *separable* Type-D vacuum-$\Lambda$ family, Kerr–NUT–(A)dS, with SdS one member and Kerr–de Sitter the addition of the twist.
② REGISTER — **THEOREM**, iff, receipt-anchored.
③ HOME — P9 §6, `thm:pd`.
④ ANCHOR — `P09_typeD_quartics`.
⑤ JOINS — [[p8-slicing-operator]] · [[p12-algebroid]] · [[p13-boundary]].
⑥ NOT OP FOR — **Acceleration — the remaining Plebański–Demiański parameter — does not appear and is NOT a vacuum parameter.** *And this is the separable corner only; the next entry is why that is not the whole reach.*

### algebraic-type-is-no-constraint
① CLAIM — The Type-D kernel **might** suggest the operator reaches only the algebraically special corner. **It does not.** Speciality is detected by the Weyl invariants ($I^3-27J^2$ vanishing, equivalently two coincident eigenvalues of the self-dual Weyl operator), and the separation is verified directly: SdS, Kerr–de Sitter and the axisymmetric Bianchi members are Type D, while **the generic members are Type I** — three distinct eigenvalues, the speciality ratio varying over the manifold. Two independent witnesses: the generic vacuum-$\Lambda$ Bianchi-I cosmology at three Killing vectors, and the **Zipoy–Voorhees $\gamma$-metric** — static axisymmetric vacuum, **non-separable** — at two, Type I for $\gamma\neq1$ and Type D exactly at $\gamma=1$.
② REGISTER — **PROPOSITION**, receipt-anchored, verified from the Weyl eigenvalues.
③ HOME — P9 §7.
④ ANCHOR — `P09_bianchiI_typeI`.
⑤ JOINS — [[p12-algebroid]] · [[p7-cr-framework]] (the general-reach axes).
⑥ NOT OP FOR — **⛔ The radiative types are absent, and that absence is not a gap but the wall's positive identity** — see below. *"Petrov O, D and I are filled" is the exact claim; N and III are not, and the synthesis must not round it to "all types".*

### the-wall-and-why-the-obvious-statement-of-it-is-wrong
① CLAIM — **THEOREM**: the range is the symmetry-reducible sector. The kernel's size is set by how much symmetry the class spends — a finite parameter family where the class reduces to ODEs (one for SdS, four for Type D, the finite KS family), a functional family where it remains a PDE problem. **The wall is the loss of isometry**, and it has a *positive* identity: **the onset of free gravitational radiation**, the graviton's two propagating polarizations, read on the matter side as dynamical inhomogeneous sources. *The reachable sector is the constrained, non-radiative skeleton of general relativity.*
② REGISTER — **THEOREM AND COROLLARY**.
③ HOME — P9 §8, `thm:range`, `cor:wall`, `cor:radiation`.
④ ANCHOR — the section's own.
⑤ JOINS — [[p11-dynamics]] (**which walks past the wall and shows it regular**) · [[p14-matter-sector]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ THE CONVERSE FAILS, AND P9'S OWN EXEMPLAR IS THE WITNESS AGAINST IT.** The type-N plane wave beyond the wall carries a **five**-dimensional isometry algebra — *more continuous symmetry than Schwarzschild's four* — and is vacuum, **with no matter at all to be inhomogeneous.** So the complement of the range is **neither the asymmetric geometries nor the inhomogeneous-matter ones**. *Any synthesis sentence of the form "the wall is inhomogeneity" or "the wall is loss of symmetry" is refuted by the paper's own example, and the correct statement is the radiative one.*

### the-wall-is-a-seam-not-a-defect
① CLAIM — Two results fix the boundary's character. **First**, the last reachable object before it is constructed exactly: a **confined gravitational wave** — a linearly polarized Gowdy–de Sitter cut with two Killing vectors — on which the transverse-traceless mode evolves by a wave equation while one isometry still pins it. **Second**, the wall acquires a sharp characterization: *a sweep generates a deformation of fixed orientation*, so a confined wave is self-consistent only while it propagates transverse to that orientation, and **the loss of the last confining isometry is exactly the point at which the wave's polarization must reorient**. Read on that orientation, the same boundary is **where chirality becomes generic**: where the sweep carries a rotation it completes the reflection exchanging the two handednesses into an orientation-preserving rotation and so **identifies** them — a mirror rather than a chirality; once the swept rotation is lost, no isometry remains to undo the reflection.
② REGISTER — **ESTABLISHED**, with the confined wave constructed in the companion.
③ HOME — P9 §9.
④ ANCHOR — the section's own.
⑤ JOINS — [[p11-dynamics]] (**owns the confined wave**) · [[p14-matter-sector]] (**the chirality reading**) · [[p13-boundary]].
⑥ NOT OP FOR — **The wall is the seam at which generation-by-symmetry hands off to evolution-by-dynamics, and P9 insists it is not a defect to be engineered around.** *And the chirality criterion bites from the loss of the swept rotation onward rather than only at the wall* — which is a wider claim than the wall statement alone and should not be collapsed into it.


---

# P10 · `corpus/canonical_time.tex`
### *The canonical problem of time as a category error: an empirically forced cosmic time, deparametrization, and the graviton sector*

> **▣ THE READ IS COMPLETE** *(r4079). P10's abstract needed no cut — 661 words, nothing living only there,
> the first paper of the ten for which that was true — and the vocabulary sweep was clean.*

### the-selection-is-the-whole-of-the-move
① CLAIM — **The paper isolates what it does and does not add, and the isolation is the crux.** The ADM machinery propagates canonical data along whatever foliation it is given; it is indifferent to which, and *in this exact sense the bare formalism contains no resolution of the problem of time and no obstruction to one.* If nothing distinguishes a foliation, the constraint is all there is and the state is frozen. If a foliation is distinguished, the constraint deparametrizes and a true Hamiltonian appears. **The canonical formalism is the same in both cases.** So: *"There is no separate canonical-machinery result to be proved here; the deparametrization is standard once a clock is in hand. The move is the selection. Everything else is reading the textbook on it."*
② REGISTER — **METHODOLOGICAL, stated at source in the paper's own voice**, and it is a claim about the paper's *own* contribution rather than about the physics.
③ HOME — P10 §4 (`sec:selection`).
④ ANCHOR — none.
⑤ JOINS — [[p4-modern-parallax]] (which supplies the selection empirically) · [[p1-bh-causality]] · [[p5-groupoid]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ This is the most honest self-accounting in the corpus and the synthesis must not upgrade it.** *What is claimed is that CR's cosmic time is the physically correct clock, on ontological and empirical grounds rather than formal ones* — not that a new canonical technique has been found. **An entry presenting the deparametrization itself as the result overstates the paper against its own statement.**

### the-selection-comes-from-outside-and-is-independently-singled-out
① CLAIM — CR supplies the distinguished foliation **from outside the bare formalism**: real, forced empirically by the CMB and conceptually by the occurrence/existence distinction. **And it is the foliation the rest of the programme independently singles out** — the metric-singularity structure of the horizon determines a unique limiting causal orientation in collapse, *generically non-orthogonal to any spacelike slice*, and that is the orientation reassigned as cosmic time.
② REGISTER — **ARGUED**, with the convergence named as independent.
③ HOME — P10 §4.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] · [[p4-modern-parallax]] · [[p5-groupoid]] · [[p7-cr-framework]].
⑥ NOT OP FOR — *The representational freedom among Lorentzian metrics on the fixed manifold **is** a genuine gauge symmetry* — P10 concedes this rather than denying it, and locates the cosmic foliation as the thing that is not gauge, not as a denial that gauge freedom exists.

### the-asymptotic-mass-question-is-misplaced-rather-than-unanswerable
① CLAIM — The ADM mass is defined relative to an asymptotic time translation and exists only where the geometry supplies one — which asymptotically-de Sitter spacetimes do not, there being no global timelike Killing vector, so **no conserved charge is well defined there at all**. *On the reading taken here that absence is not a deficiency of the geometry but a misplacement of the question*: the time this construction runs on is not recovered from an asymptotic symmetry but **selected and measured**, so a quantity whose definition waits on an asymptotic Killing vector is waiting on the wrong thing.
② REGISTER — **A READING**, and marked as the same move as the paper's own.
③ HOME — P10 §4.
④ ANCHOR — none.
⑤ JOINS — [[p3-sds-slicing]] (**where the standard definitions are evaluated and all return the slicing-dependent $M$**) · [[p5-groupoid]] (**$\alpha$ the invariant curvature radius, a length not a mass**).
⑥ NOT OP FOR — This does not supply a mass charge; *it says why the absence of one is not a defect.* **The three entries — P3's evaluation, P5's uniqueness argument, and this reading — are one answer distributed across three papers.**

### the-friedrichs-extension-is-closed-by-the-horizon's-own-state
① CLAIM — The quantization carries a **deficiency-index $(1,1)$ ambiguity** — a one-parameter family of candidate quantizations — and it is closed **without stipulation**: the boundary at $a=0$ is the de Sitter horizon, its surface gravity is $\kappa=1/\alpha$, and the regular Euclidean state at that $\kappa$ leaves nothing to choose. **That is the same condition the cosmogenesis kernel enforces** — regularity in the Euclidean continuation. *The extension-fixing and the lift's kernel are one requirement met twice, once at the horizon and once across the beginning.*
② REGISTER — **DERIVED**, with the closure explicitly not a stipulation.
③ HOME — P10 §6.
④ ANCHOR — the section's own.
⑤ JOINS — [[p1-bh-causality]] · [[p7-cr-framework]] · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **⛔ AND THE CLOSURE IS AVAILABLE ONLY BECAUSE OF P1, WHICH IS THE SHARPEST JOIN IN THIS PAPER.** A regular Euclidean state exists at a horizon only if the continuation is smooth there — no conical defect, curvature finite. The horizon at $a=0$ is a **metric** singularity, spatial measure collapsing while curvature stays finite, **and not a curvature singularity**; had it been the latter there would be no smooth Euclidean section, no regular state to select, and the extension would remain unfixed. *So the distinction that dissolves the information paradox is the same distinction that makes this quantization unique.*

### the-beginning-is-a-boundary-of-zero-duration-within-the-evolution
① CLAIM — Cosmogenesis occupies **no cosmic time at all**, so the evolution operator across it is $U(\Delta\tau=0)=\mathbb 1$: *the true Hamiltonian has no interval in which to act there.* The geometry nonetheless changes across the segment — the areal radius climbs from the turnaround to zero, the expansion rate is carried from zero to divergent — so **the change is not generated by the Hamiltonian but is the segment's own analytic content**, the contour read at another point of itself. *The beginning is therefore not a first instant of the evolution but a boundary of zero duration within it — and that is why nothing can be lost across it: no evolution acts, so none can be non-unitary.*
② REGISTER — **CLASSICAL STATEMENT plus its immediate consequence**, with the limit marked at source.
③ HOME — P10 §5.
④ ANCHOR — the section's own.
⑤ JOINS — [[p7-cr-framework]] (the lift) · [[p16-cosmogenesis]].
⑥ NOT OP FOR — **⛔ The limit is stated plainly: what is NOT established here is a quantization of the Euclidean segment itself.** The state on either side is related by the identity in cosmic time; whether the imaginary-time segment admits its own quantum treatment is a separate question. **And one thing is open at its stated size**: the kernel's frequency is not constant along the segment, so *the projection is adiabatic rather than exact*, and the residual at the largest scales is one face of that.

### the-graviton-lift-is-the-substantive-canonical-content
① CLAIM — The minisuperspace illustration truncates the layer to its scale factor and **carries no propagating degree of freedom**, so it cannot exhibit what the true Hamiltonian generates beyond the background expansion. The full layer does: the **transverse-traceless shear of its spatial geometry, the graviton**. On the closed synchronous slicing $a(T)=\alpha\cosh(T/\alpha)$, the TT perturbation decomposes into $S^3$ tensor harmonics with $\mu_n^2=n(n+2)-2$, $n\ge2$, and the second-order action deparametrizes on the absolute foliation exactly as the background does.
② REGISTER — **CARRIED OUT**, not asserted; and named by the paper as *the* substantive canonical content.
③ HOME — P10 §7 (`sec:lock`).
④ ANCHOR — the section's own.
⑤ JOINS — [[p11-dynamics]] · [[p9-range-paper]] (the TT shear is the same object the wall is stated on) · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ Where it stops is named**: the free tower evolves on $a(T)$ as a **fixed classical background**; the coupled sector — once the scale factor is itself quantized and back-reacts — is a different regime. *P10 raises the natural worry against its own counterterm argument (that a counterterm basis is a statement about a class of fixed backgrounds, so quantizing the scale factor leaves no fixed background to state it on) and answers it rather than leaving it.*

### dissolution-not-solution
① CLAIM — **Stated negatively, which is the right way round.** *"We have added nothing to the formalism. We have not introduced a new time variable, nor a matter field whose role is to be a clock, nor a modification of the constraint algebra. We have identified, on external grounds, which foliation is physically real, and read the existing constraint on it."* **The problem of time was never a problem internal to the formalism**; it was the formalism faithfully reporting the consequences of an ontological premise — the block — that is both a category error and empirically false. *A solution would add structure to make a defective formalism work; a dissolution removes a mistaken premise and finds the formalism was working all along.*
② REGISTER — **VERDICT**, with the distinction argued rather than asserted.
③ HOME — P10 §8.
④ ANCHOR — none.
⑤ JOINS — [[p6-shadow-of-existence]] (the four rules, each favouring this reading) · [[p7-cr-framework]] (the dissolution family) · [[p4-modern-parallax]].
⑥ NOT OP FOR — **The canonical face and the geometric face are two descriptions of one evolving three-dimensional world** — the true Hamiltonian advances the layer; the operator and range papers read the geometry of that advance, matter as the bend and radiation as the TT shear, up to the wall. *The loop closes with the geometric side rather than standing apart from it.*


---

# P11 · `corpus/dynamics_paper.tex`
### *Why the cut bends: the dynamics of the de Sitter cut, the confined graviton, and the wall*

> **▣ THE READ IS COMPLETE** *(r4081). Abstract cut 1444 → 459 words; two results and two receipts relocated
> into the body first, and one orphaned citation restored.*

### the-symmetric-sector's-dynamics-in-closed-form
① CLAIM — On any comoving worldline of a symmetric cut, **at any energy**, $\dd^2r/\dd\tilde\tau^2=-f'/2=rK_G$ with $K_G$ the slicing surface's Gaussian curvature. **So the rate at which the symmetric cut's bend changes in time *is* the bend itself**, up to the areal factor: the cut straightens, is momentarily flat, and bends the other way as the geometry passes its one sign change. *That is the whole of the symmetric sector's dynamics.*
② REGISTER — **RECEIPT-ANCHORED**, and general in the energy.
③ HOME — P11 §1 (relocated there r4081; it had lived only in the abstract).
④ ANCHOR — `P03_acceleration_is_slice_curvature`.
⑤ JOINS — [[p3-sds-slicing]] (**the same $f'$ zero the curvature crossover reads — one zero seen twice**) · [[p8-slicing-operator]] · [[p5-groupoid]].
⑥ NOT OP FOR — *This is why the inhomogeneous case needs a paper*: the symmetric sector's answer is a closed form, and everything P11 builds is the first case in which the bend is **not** symmetric.

### the-two-polarizations-are-a-wave-map-into-the-hyperbolic-plane
① CLAIM — In the variables $P=2\psi-\ln R$, $Q=\omega$, the torus block's equations are **identically** the harmonic-map system for a map from the $(t,z)$ plane, with density $R$, into the target $\dd P^2+e^{2P}\dd Q^2$ — a metric of Gaussian curvature $-1$, **the hyperbolic plane**. *So the two polarizations are not two decoupled fields but one point moving on a negatively curved surface*, the polarized case being the geodesic $Q=\text{const}$ and the turning of the polarization plane being motion off it.
② REGISTER — **DERIVED, identically**, receipt-anchored.
③ HOME — P11 §2.1 (`sec:unpolarized`).
④ ANCHOR — `P11_unpolarized_gowdy_cut`.
⑤ JOINS — [[p9-range-paper]] · [[p10-canonical-time]] (the graviton tower) · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ And $\Lambda$ is ABSENT from that sector entirely**: both wave-map equations hold with no cosmological term, which enters only the area and conformal equations. *In the wave-map variable the graviton propagates freely and $\Lambda$ drives only the area* — and this **explains** the source term that appears in the polarized wave equation, which is the area equation in changed variables. *It is the second polarization that forces the variable in which this is visible.*

### the-handedness-is-a-conserved-charge-and-its-parity-is-disconnected
① CLAIM — The helicity-flipping parity $x\mapsto-x$ is exactly $Q\mapsto-Q$ with $P$ fixed — an isometry of the target whose differential has determinant $-1$: **it reverses orientation, so it lies in the component of $\mathrm{Isom}(\mathbb H^2)$ the identity component does not reach. No connected target isometry identifies the two handednesses.** On the homogeneous reduction the twist $c=Re^{2P}Q_t$ is conserved, and the parity acts as $c\mapsto-c$. **So on the reachable sector the graviton's handedness is the sign of a conserved charge**, with $c=0$ the polarized achiral cut.
② REGISTER — **DERIVED**, with $c\neq0$ solutions exhibited and the first integral reproduced along them.
③ HOME — P11 §2.1 and §6.
④ ANCHOR — `P11_unpolarized_gowdy_cut`, `P11_wall_ppwave`, `P09_the_wall_is_not_the_loss_of_symmetry`.
⑤ JOINS — [[p5-groupoid]] (**the same orientation $\mathbb Z_2$: the $A_2$ diagram automorphism, the vantage-swap**) · [[p13-boundary]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ The homogeneous reduction is not the member the criterion is about**, and P11 says so: restoring $z$-dependence gives an **unconstrained** wave map — the two remaining Einstein equations fix the conformal factor by a quadrature whose integrability holds identically on shell, so every Cauchy datum integrates to a genuine vacuum member and *the wave carries no hidden constraint*. An explicit inhomogeneous single-helicity travelling datum is evolved to the roundoff floor with fourth-order convergence, and on it the polarization plane genuinely turns.

### chirality-is-reached-inside-the-range-not-past-it
① CLAIM — **The first chiral geometry is inside the construction's own reach.** The unpolarized turning wave carries the *same two spacelike Killing vectors* as the polarized one — the range paper's ground for placing this class in the reachable sector — and the transverse reflection is an isometry of the Gowdy form **precisely when the wave is polarized**. So the criterion bites **from the loss of the swept $\mathrm{SO}(3)$ onward**: the polarized edge is achiral, the unpolarized turning wave is the first chiral case, and the wall is where chirality is **generic rather than where it begins**.
② REGISTER — **ESTABLISHED**, receipt-anchored.
③ HOME — P11 §6 (`sec:chirality`).
④ ANCHOR — `P09_the_wall_is_not_the_loss_of_symmetry`.
⑤ JOINS — [[p9-range-paper]] · [[p13-boundary]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ And the agreement with the matter sector's index obstruction is closer than a shared conclusion — the two are ONE MECHANISM read in two sectors.** The obstruction bites because a positive-dimensional **connected** group contains a circle whose action forces the equivariant index to vanish; the criterion here is achiral exactly while the swept $\mathrm{SO}(3)$ supplies a continuous rotation completing the reflection and identifying the two helicities. *The gravitational sector is chiral precisely through the component that obstruction cannot touch.*

### the-wall-is-a-regular-radiative-boundary-and-not-a-metric-singularity
① CLAIM — Two questions are settled at the wall. **The dynamics continues across it.** And **the wall is *not* a metric singularity** in the precise sense of the causality paper — no measure collapses there — so it is a regular radiative boundary rather than a place at which a clock could be re-founded by the Null-Boundary Correspondence.
② REGISTER — **SETTLED**, both, against the definition rather than by analogy. *A Killing horizon is named as the worked sufficient case, not the definition.*
③ HOME — P11 §5 (`sec:wall`).
④ ANCHOR — `P11_wall_ppwave`.
⑤ JOINS — [[p1-bh-causality]] (**the definition tested against**) · [[p9-range-paper]] (**which needs the wall regular for its own "walked past, not a gap" claim**) · [[p7-cr-framework]].
⑥ NOT OP FOR — *This is a **negative** result about the corpus's own most-used structure, and it is the right kind to have*: the metric singularity is not everywhere, and P11 checks rather than assumes.

### the-nonlinear-regime-admits-rather-than-forces
① CLAIM — Under isotropy the homogeneous field equations reduce consistently to one constraint and one dynamical law, solved to give exact de Sitter with $H^2=\Lambda/3$. **The internal area-clock that organizes the $\Lambda=0$ Gowdy system is inconsistent here**, and the substrate's de Sitter cosmic time replaces it — *established positively and not merely by the failure of the alternative.* The de Sitter background is an attractor, every tractable sector admits, and the first-class system is consistent to all orders, so **the continuous dynamics admits rather than forces a quantum structure**.
② REGISTER — **RESOLVED ON THE CLASSICAL SIDE**, with the verdict named as admissibility.
③ HOME — P11 §3.
④ ANCHOR — the section's own.
⑤ JOINS — [[p10-canonical-time]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **⛔ Explicitly not claimed, at source**: no closed-form nonlinear solution, and **no full non-perturbative quantization** — neither is built, and the latter is not needed for the admissibility verdict. *The non-perturbative quantization is the definition of the interacting tower, carried as an open problem of the programme.*


---

# P12 · `corpus/algebroid_paper.tex`
### *The constraint algebra as the substrate's Atiyah algebroid: base, anchor, and the structure function*

> **▣ THE READ IS COMPLETE** *(r4083). Abstract cut 1450 → 460 words; the Atiyah passage and its receipt
> relocated first, and one orphaned citation restored.*

### the-claim-is-a-recognition-not-an-addition
① CLAIM — The hypersurface-deformation algebra carries **structure functions** — the normal–normal bracket's coefficient is the inverse spatial metric, a field rather than a constant — so it is a Lie **algebroid**, and *that* is the standardly recognised obstruction at the heart of the problem of time. An action Lie algebroid is a Lie algebra acting on a base, with an anchor and structure functions varying over it. **General relativity's constraint algebra has the structure functions but has never been given the base they vary over, nor a section selecting a definite flow.** P12 supplies both: base the space of cuts, algebra $\mathfrak{so}(5,1)$, anchor the slicing operator's cut-to-stress-energy map, section the cosmic clock. *The claim is a recognition, not an addition.*
② REGISTER — **STATED as a recognition**, in the paper's own voice.
③ HOME — P12 §1.
④ ANCHOR — none.
⑤ JOINS — [[p8-slicing-operator]] (the anchor) · [[p10-canonical-time]] (the section) · [[p9-range-paper]] (the base's strata) · [[p5-groupoid]].
⑥ NOT OP FOR — **⛔ Two groupoids appear in this corpus and they are different objects** — P5 separates them explicitly. *Here the objects are **cuts** and the arrows are isometries carrying one cut to another; P5's objects are **vantages on one geometry**.* Conflating them merges a solution space with a description structure. **And the four-dimensionality of the leaf is doing work rather than merely being the case**: the same algebra closes for the Lovelock theories, which coincide with general relativity only in four dimensions.

### the-bracket-closes-and-the-puzzling-shape-is-a-coset
① CLAIM — At the symmetric cut $\mathfrak{so}(5,1)=\mathfrak h\oplus\mathfrak m$ with $\mathfrak h=\mathfrak{so}(4,1)$, and all three inclusions hold, $\mathfrak m$ not being a subalgebra. **Under $\mathfrak m\leftrightarrow\mathcal H_\perp$, $\mathfrak h\leftrightarrow\mathcal H_a$ these are the hypersurface-deformation brackets term for term.** *So the algebraic shape that makes the Dirac algebra puzzling — two normal deformations bracketing into a tangential one — is exactly the shape of a symmetric-space coset: two coset directions bracketing into the isotropy. **They are the same grading.***
② REGISTER — **PROPOSITION**, verified on explicit matrices.
③ HOME — P12 §4.
④ ANCHOR — `P12_bracket_closure`.
⑤ JOINS — [[p10-canonical-time]] · [[p7-cr-framework]] · [[p17-geometric-core]].
⑥ NOT OP FOR — **And the grading IS the lapse–shift split**: the normal generator is smeared by the lapse — the existent's own foliation stacking rate — and the tangential by the shift, the synchronization convention. *So the cosmological reading in which the observable expansion rides the foliation rate while a chosen synchronization projects it to distance and redshift **is not a separate posit**; it is this grading read on the preferred foliation.*

### the-atiyah-sequence-and-what-a-connection-is
① CLAIM — **Naming the grading costs nothing and buys the literature.** For a homogeneous space the action algebroid of $G$ on $G/H$ **is** the Atiyah algebroid of $G\to G/H$, so with $\mathrm{dS}_5=SO(5,1)/SO(4,1)$ the sequence $0\to\mathfrak h\to\mathfrak{so}(5,1)\times\mathcal C\to T\mathcal C\to0$ is **exact**, with $\mathfrak h$ the anchor's kernel (the adjoint bundle, ten-dimensional) and $\mathfrak m$ its image (the five dimensions of the base), closing at $10+5=15=\dim\mathfrak{so}(5,1)$. **And a splitting of that sequence is what a connection is** — so the section supplied to select a definite flow is a connection in the standard sense rather than an object peculiar to this construction.
② REGISTER — **RECEIPT-ANCHORED**, exactness verified at every term on explicit matrices.
③ HOME — P12 §4 (relocated there r4083; it had lived only in the abstract).
④ ANCHOR — `I55_the_atiyah_sequence_is_exact_and_a_characteristic_class_is_not_available`; ledger `index_theory`.
⑤ JOINS — [[p10-canonical-time]] · [[p17-geometric-core]] · [[p5-groupoid]] (the action groupoid integrating it).
⑥ NOT OP FOR — *The receipt's own name carries the negative half*: **a characteristic class is not available.** An entry citing the exactness without it takes only the affirmative half of a result whose key says both.

### the-structure-function-is-the-coset-metric-and-the-signature-is-the-content
① CLAIM — The coefficient $h^{ab}$ — the structure *function* that makes the algebra an algebroid and is the canonical root of the problem of time — is, **on the symmetry-reducible reduction**, identified with the coset metric of the symmetric space.
② REGISTER — **IDENTIFIED**, receipt-anchored, and **the paper immediately says it is not a naive tensor equality**: $h^{ab}$ is the Riemannian inverse spatial 3-metric while the coset metric is the Lorentzian 5-dimensional form of signature $(1,4)$. *The identification is of the **reduced** structure function on the symmetric-cut pattern with that coset form.*
③ HOME — P12 §4.
④ ANCHOR — `P12_coset_metric`.
⑤ JOINS — [[p10-canonical-time]] · [[p9-range-paper]].
⑥ NOT OP FOR — **⛔ What makes it more than dimensional bookkeeping is the signature**: the indefinite Lorentzian sign is *supplied by the substrate's own geometry* rather than inserted. *A synthesis stating "the structure function is the coset metric" flat, without the reduction and the signature, has asserted the naive equality the paper explicitly disclaims.*

### the-stratification-read-as-first-integrals
① CLAIM — As the cut moves off the symmetric vacuum the isotropy drops, and its strata are the range paper's Petrov classes — Type O (isotropy dimension ten), Type D (SdS four, Kerr–de Sitter two), Type I (Bianchi three, Zipoy–Voorhees two), and the wall (isotropy zero). **Read as a count of first integrals, the stratification says where the construction's hidden symmetry is needed and where it is not**: a Killing vector contributes one linear integral and the Casimir a quadratic one, against the four in involution a four-dimensional geodesic flow requires.
② REGISTER — **ESTABLISHED**, dimensions computed.
③ HOME — P12 §5.
④ ANCHOR — the section's own.
⑤ JOINS — [[p9-range-paper]] (**the same strata; P9's isotropy tabulation cites this paper**) · [[p11-dynamics]] · [[p6-shadow-of-existence]] (transitivity ↔ modulus).
⑥ NOT OP FOR — **The symmetric-space relation survives at Type O and Nariai ONLY**; at every other stratum there is structure-function variation — *the algebroid connection*. And the $\mathfrak{so}(5,1)$-action on the base is **non-transitive**, the mass being a transverse modulus — which is P6's second sense of "modulus", the one its criterion does **not** exclude.

### both-factors-of-Aut(A2)-are-realized-geometrically
① CLAIM — The $S_3$ permutes the three horizon roots, which — the cubic having no quadratic term — are three zero-sum weights $120^\circ$ apart on the throat-image circle. The $\mathbb Z_2$ is the **central inversion**, and it has a clean geometric form: $\mathrm{dS}_5$ is **doubly ruled** by null generators — the comoving and synchronous congruences — and the inversion **exchanges the two families**, an orientation-reversing isometry swapping the rulings where an orientation-preserving one fixes each. Explicitly $R=\mathrm{diag}(1,1,-1,1,1,1)$, determinant $-1$ globally and on the ruled three-block, sending $r_0\mapsto-r_0$ hence $2M\mapsto-2M$. The two factors act on **independent structures** — three roots and two rulings — and the inversion is central, *which is why $\mathrm{Aut}(A_2)$ is a direct product*.
② REGISTER — **VERIFIED DIRECTLY**, and it supplies the geometric reason for what P5 obtained algebraically.
③ HOME — P12 §8.
④ ANCHOR — the section's own.
⑤ JOINS — [[p5-groupoid]] (**which gets $D_6$ algebraically; this says why it is a direct product**) · [[p11-dynamics]] · [[p13-boundary]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ The convergence to record: the double-ruling swap, the orientation parity $\mathrm O(5,1)/\mathrm{SO}_0$, the $A_2$ diagram automorphism, and the graviton chirality are ONE AND THE SAME $\mathbb Z_2$.** *Four descriptions arrived at in four papers, identified here.*

### the-dimension-is-a-floor-and-no-upper-bound-exists-anywhere
① CLAIM — Stated plainly and against the programme's own convenience. The construction generates *many distinct* four-geometries from *one* substrate, and slicing a four-dimensional de Sitter space only re-coordinatizes it — **which excludes $\mathrm{dS}_4$ and yields $D\ge5$, a lower bound and not an equality. NO UPPER BOUND IS ESTABLISHED ANYWHERE IN THIS FRAMEWORK.** The ontological commitments fix only the existent — a one-parameter family of *three*-dimensional layers, the sole dimensional statement in any axiom — and require of the representation only that it admit them as spacelike hypersurfaces, so $\dim M\ge4$ with the projection explicitly non-unique; the empirical forcing is of the foliation, likewise a floor. **$\mathrm{dS}_5$ is the *minimal* substrate sufficient for the sector built here — a modelling economy, not a derived maximum.**
② REGISTER — **⛔ EXPLICIT NEGATIVE, receipt-anchored.**
③ HOME — P12 §2.
④ ANCHOR — `P12_polar_dimension`.
⑤ JOINS — [[p6-shadow-of-existence]] (**the dimension is P6's boundary case, settled by content rather than form**) · [[p17-geometric-core]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **And the polar structure does not close the gap either**: the polar of a spacelike substrate point is $\mathrm{dS}_{D-1}$ in *every* dimension, *which relates the rungs without capping them*. **⛔ ANY SYNTHESIS SENTENCE TREATING FIVE DIMENSIONS AS DERIVED CONTRADICTS THIS PAPER DIRECTLY.**


---

# P13 · `corpus/boundary_paper.tex`
### *The boundary: colour is not a substrate isometry, and what the two real forms do carry*

> **▣ THE READ IS COMPLETE** *(r4085). P13 is the theoretical half of the first application pair, and carries
> its own synthesis because its chain reaches back through P3, P5 and P7--P12. **Its abstract needed no cut**
> — 1102 words with nothing living only there — the second paper of the thirteen for which that was true.*

### the-register-is-fixed-before-the-result
① CLAIM — **P13 states what it is not claiming before it claims anything**, on the ground that *a negative result is as easy to overstate as a positive one.* **Established**: colour does not arise as a continuous internal gauge symmetry of this geometry through any examined geometric-isometry route. **Not established, and not claimed anywhere**: the universal statement that no construction whatever could yield the Standard Model from this geometry. **And not the subject at all**: colour by the ordinary route, an $\mathrm{SU}(3)$ matter bundle placed on the spacetime by hand, *which is in no jeopardy.* The subject is the specific hope of reading colour off the geometry as one reads gravity.
② REGISTER — **SCOPE, fixed at the outset in the paper's own voice.**
③ HOME — P13 §1.
④ ANCHOR — none.
⑤ JOINS — [[p5-groupoid]] (whose $A_2$-is-not-colour remark is the same guard from the other side) · [[p14-matter-sector]] · [[p6-shadow-of-existence]].
⑥ NOT OP FOR — **⛔ THIS IS THE ENTRY THE SYNTHESIS MOST NEEDS AND MOST EASILY LOSES.** *A results paper reporting "the corpus shows colour is not geometric" without the register has made the universal claim P13 explicitly refuses.* The result is about **one route**, and the ordinary route is untouched.

### the-sigma-lift-fails-because-the-two-operations-differ-on-every-axis
① CLAIM — The tempting bridge is that the real involution $\sigma$ **is** the Wick rotation, so the real $A_2$ skeleton would be the shadow of the Wick-face $\mathfrak{su}(3)$ and colour would lift continuously. **Computed in the embedding coordinates rather than judged by family resemblance, the bridge fails.** The Wick rotation complexifies the global *timelike* coordinate, sends the Lorentzian metric to the Euclidean, is *imaginary*, and **changes the geometry**. $\sigma$ is a *real* Weyl reflection of the spatial sky/root plane; it fixes $x_0$, **preserves both signatures** — so it is not a signature change at all — and **fixes the manifold**, permuting charts of one rigid geometry.
② REGISTER — **COMPUTED**, receipt-anchored.
③ HOME — P13 §2.1.
④ ANCHOR — `P13_sigma_lift`.
⑤ JOINS — [[p3-sds-slicing]] · [[p5-groupoid]] · [[p12-algebroid]].
⑥ NOT OP FOR — **⛔ THREE OPERATIONS ARE CO-LOCALISED AT THE EQUATORIAL SEAM AND ONLY ONE LANDS WHERE COLOUR LIVES.** The real Weyl reflection $\sigma$ (fixes $x_0$, the signature, the geometry); the **seam continuation** $\theta\mapsto\pi/2+i\psi$, which flips the signature of a *single slicing curve* and reaches the equatorial $S^4$ with isometry $\mathrm{SO}(5)$; and the **global Wick** $x_0\mapsto ix_0$, reaching $S^5$ with $\mathrm{SO}(6)\supset\mathfrak{su}(3)$. *Reading $\sigma$ as the bridge conflates the first with the third; reading the seam continuation as it conflates two **imaginary** operations with different targets.* **The $S^4$ is not the $S^5$, and five dimensions are not enough.**

### the-index-obstruction-and-the-escape-it-closes
① CLAIM — A fourth face to the same wall, with forty years behind it: even granting the gauge structure its home on the compact face, **the chiral matter charged under it cannot be obtained from the geometry there.** On a compact connected even-dimensional spin manifold carrying a non-trivial smooth action of a **compact connected** Lie group by isometries, the equivariant Dirac index vanishes; for a non-abelian compact group it is killed a second way, by positive scalar curvature and Lichnerowicz. **The load-bearing hypotheses are compactness and a continuous isometry — not a product or Kaluza–Klein structure**, so *reading the absence of a product as a reprieve removes a premise the theorem never used.*
② REGISTER — **CITED CLASSICAL THEOREM**, applied with its hypotheses checked.
③ HOME — P13 §3.
④ ANCHOR — none; Atiyah–Hirzebruch, Atiyah–Singer, Lawson–Yau, Lichnerowicz.
⑤ JOINS — [[p11-dynamics]] (**one mechanism read in two sectors — the gravitational sector is chiral precisely through the disconnected component the obstruction cannot touch**) · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ The non-compactness escape is closed, and the argument is subtler than "the index bites".** The escape presupposes a continuous $\mathfrak{su}(3)$ acting by isometry on the non-compact substrate whose non-compactness might shelter a chiral sector. But **$\mathfrak{su}(3)$ is not an isometry of the real substrate at all**, so it acts only on the compact face, *which is compact.* **Where $\mathfrak{su}(3)$ acts as an isometry the manifold is compact, and where the manifold is non-compact there is no such action to protect** — a localisation argument independent of whether the index ever bites.

### colour-closure-rests-on-the-causal-structure-not-on-the-compact-face's-status
① CLAIM — **The most secure layer, and P13 says so.** That $\mathfrak{su}(3)$ is not a symmetry of the world the matter inhabits **does not depend on any claim about the compact face**; it follows from the causal structure. The cosmogenesis is a **signature-preserving** reassignment on the real Lorentzian substrate — a null congruence promoted to the fundamental timelike one, manifold and signature held fixed — and the matter rides that real Lorentzian horn. Colour lives on the compact face reached only by the global Wick.
② REGISTER — **ESTABLISHED on the causal structure**, and explicitly independent of the face's ontological status.
③ HOME — P13 §4.1.
④ ANCHOR — none.
⑤ JOINS — [[p1-bh-causality]] · [[p7-cr-framework]] · [[p12-algebroid]].
⑥ NOT OP FOR — *The layering is the point*: the closure survives whatever verdict is reached about what the compact face **is**, so a synthesis may carry it without carrying the face's status.

### charge-conjugation-factorises
① CLAIM — **The boundary is a shape, and a shape has an inside.** The negatives are the perimeter; what they enclose is a positive result the negatives alone could not reach. The reflections the substrate **does** carry, composed with the antilinear complex-analytic face, are exactly charge conjugation's **kinematic** content — and their composite is the cosmogenesis itself. **The statement is made on the full analytic object and not on any real slice**, which is the level at which alone it can be made: $r\mapsto-r$ and $\tilde\tau\mapsto\bar{\tilde\tau}$ are stated together on $\mathbb C_r\times\mathbb C_{\tilde\tau}$, and the neutral/charged and particle/antiparticle distinctions are properties of that object, *not of a chart drawn through its real part.*
② REGISTER — **PROPOSITION**, with the factorisation into a geometric kinematic face and a field-level charge sign.
③ HOME — P13 §6, `prop:conjugation-closure`.
④ ANCHOR — the section's own.
⑤ JOINS — [[p3-sds-slicing]] (**mass $R$-odd, charge $R$-even, settled at the geometric level; the field-level closure adjoins an independent $\mathbb Z_2$**) · [[p5-groupoid]] · [[p7-cr-framework]].
⑥ NOT OP FOR — **The geometric face is not the whole of $C$** — the charge sign closes from the field, not from the geometry, and *the factorisation is the result rather than an identification of the two.*

### the-two-real-forms-carry-the-divide
① CLAIM — **P13's own synthesis, and it is the positive statement the wall makes room for.** It is *not* that the substrate yields the Standard Model — the wall stands — but that **the divide the last century drew between the gravitational and the quantum, and between gravity and the gauge forces, is one substrate read on its two real forms.** *The Lorentzian form carries the framework*: the Dirac constraint algebra is the symmetric-space coset structure of $SO(5,1)/SO(4,1)$, its structure function the coset metric and the "wrong sign" obstructing a global time the coset's own indefinite signature; read on the forced foliation the constraint deparametrizes to a true Hamiltonian. *The Euclidean form carries the gauge and the quantum scale*: colour requires the **full** $\mathrm{SO}(6)$, since the smallest faithful real representation of $\mathfrak{su}(3)$ is six-dimensional — so $\mathfrak{su}(3)\subset\mathfrak{so}(6)$ but **not** $\subset\mathfrak{so}(5)$ — and the quantum of action enters through the horizon's thermal state at period $\beta=2\pi\alpha$, *on the same face.*
② REGISTER — **SYNTHESIS**, stated at the weight its pieces carry.
③ HOME — P13 §8.
④ ANCHOR — none; the pieces' own.
⑤ JOINS — [[p12-algebroid]] · [[p10-canonical-time]] · [[p17-geometric-core]] · [[p14-matter-sector]].
⑥ NOT OP FOR — **⛔ The dimension count is the load-bearing detail and it is exact**: five dimensions do not suffice for colour, which is *why* the seam continuation's $S^4$ cannot be the home and the global Wick's $S^5$ can. **And the two forms are not co-equal worlds** — P13 fixes an asymmetry between them, and the synthesis must carry that rather than presenting a symmetric pair.

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
