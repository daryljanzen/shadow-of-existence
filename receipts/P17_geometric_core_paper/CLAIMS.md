# P17 — geometric_core_paper — CLAIMS inventory & eleven-avenue worksheet

## Whole-read digest (r1404)
The foundational CORE paper: "the object, not its uses" -- the maximally symmetric de Sitter substrate itself,
made explicit in three facts the corpus carried implicitly. The longest paper (1416 lines, 11 sections). Deep,
philosophical + geometric. Maturity marks throughout.
- **Three facts (abstract):** (1) the substrate is EVERYWHERE INTRINSICALLY REAL -- a real 4D Riemannian manifold,
  real coordinate basis, Lorentzian signature intrinsic to positive curvature (not imposed); the imaginary
  variables (5th embedding coord, conjugacy circle, seam continuation) are reaching-instruments over a geometry
  real at every point they land on. (2) the substrate is the UNIVERSAL STANDARD OF PHYSICS: alpha=sqrt(3/Lambda)
  + the locked null cone are the intrinsic length + causal structure; Eddington corrected (timelike half as real
  as spatial) + grounded (real ground state); horizon problem dissolved (CMB uniformity = maximal symmetry). (3)
  MAXIMAL SYMMETRY is the single fact from which the corpus results descend as one (parameter-free rigidity,
  constants as unit gauges, augmentation nec+suff, universality, matter-symmetry wall) -- Planck values become
  gauge-combinations, cosmological-constant + coincidence problems dissolve (no Planck scale for Lambda to be
  small against), Lambda's value the ledger's one input scale.
- **sec:real** -- the substrate a real manifold; the 5th coordinate not a coordinate of the manifold; Lorentzian
  signature intrinsic to positive curvature.
- **sec:standard (Lambda-vacuum)** -- Eddington's intuition at weight, corrected/foggy/wrong; universality = maximal symmetry; horizon problem properly stated (dissolved).
- **sec:imaginary** -- reached through the imaginary, real everywhere it lands.
- **sec:rulings + sec:power** -- the straight null rulings = the light cone = visible peak. POWER OF A POINT:
  pow(P)=|X|^2-alpha^2 (Steiner 1826 invariant, = tangent length^2 Euclid III.36) EQUALS x_0^2 (height^2) by the
  hyperboloid eq -x_0^2+|X|^2=alpha^2 [eq:powerisheight]. So tangent^2=x_0^2 -> ds^2=-x_0^2+x_0^2=0: EVERY TANGENT
  to the throat is NULL [prop:tangentnull]. Euclid's tangent-secant relation = the null condition, the metric
  minus sign the only difference. Verified at hinge + 600 random heights, max|ds^2|=5.7e-14. [power_of_a_point.py,
  power_is_null.py] rem:onecircle -- a fact about ONE circle (the waist); power w.r.t. any other circle/chord is
  NOT a height (sharp bound).
- **sec:unification** -- maximal symmetry worn seven ways: the corpus's separately-established results as one fact
  at several rungs (Spin(5)/S^4 unique spin structure at line 851, etc.).
- **sec:ledger/shadows** -- the register split = the substrate's TWO REAL FORMS: real-geometric gauges c,Lambda,G
  on the Lorentzian dS_5=SO(5,1)/SO(4,1); thermal gauges hbar,k_B on the Euclidean S^5=SO(6)/SO(5) (Wick x_0->ix_0).
  Two real forms of one complex SO(6,C), meeting at the horizon beta=2pi alpha. su(3) requires FULL SO(6) (smallest
  faithful real rep of su(3) is R^6, cannot sit in SO(5) of the seam) -> colour + quantum-of-action share the one
  Euclidean real form. [qm_S4_vs_S5.py computes the su(3)⊂so(6),⊄so(5) co-location] GR/quantum + gravity/gauge
  divides = one substrate on its two real forms.
- **sec:landing / sec:frontiers** -- the space the corpus lands in; open frontiers.

## AVENUE 11 -- receipt inventory (3 scripts, scattered; P17 UNWIRED)
| # | claim | script | location | status |
|---|-------|--------|----------|--------|
| 1 | power of a point = height^2 | `power_of_a_point.py` | storyboard_receipts/ | ✔✔ |
| 2 | tangent is null: ds^2=0, max 5.68e-14 @600 | `power_is_null.py` | storyboard_receipts/ | ✔✔ |
| 3 | su(3)⊂so(6),⊄so(5): smallest faithful real rep R^6 | `qm_S4_vs_S5.py` | corpus/ | ✔✔ |

## AVENUES 1-10 -- first-pass (off the whole-read; to execute)
- A1 Q-mine: philosophical register; scan for rhetoric without standing (the "Eddington corrected/foggy/wrong" claims, the dissolution claims).
- A2 own accomplishments: the power=height identity (a genuine classical-geometry result); the two-real-forms consolidation; the seven-way unification. Check nothing undersold.
- A3 press the gap: the dissolution claims (cosmological-constant, coincidence, horizon) at the constant rung -- check scoped (Lambda's value NOT predicted, "the ledger's one input scale"). The su(3)/so(6) matter-synthesis is drawn at the boundary paper (not overclaimed here).
- A4 identity: title = "the geometric core" / "the object, not its uses". Confirm the paper stays on the object.
- A5 positive-face: leads on what the substrate IS (real, standard, maximal symmetry), not on refuting alternatives.
- A6 symmetry: the two real forms (Lorentzian/Euclidean) kept balanced; the imaginary/real; check no real form privileged or conjugate dropped.
- A7 bespoke two-way: forward -- the substrate is the object P6's theory-choice + all papers apply. backward -- P6 world-vs-description on the "real everywhere it lands" (imaginary = description, real = world).
- A8 dissolution census: cosmological-constant problem, coincidence, horizon, Planck-scale-as-gauge, fine-tuning -- all "by that one fact". Census at weight.
- A9 checklist: the corpus LANDING (sec:landing) is the unification recap; idiom (power of a point, Hubble-Eddington); the seven rungs.
- A10 forward-refs: the whole corpus (this is the core all papers cite/descend from). Check the descent structure.

## STATUS r1406: P17 FULLY SWEPT (avenue 11 + avenues 1-10). ==> ENTIRE 17-PAPER CORPUS SWEPT. See below.
## (r1405) AVENUE 11 COMPLETE for P17. All 3 receipts ✔✔ (power_of_a_point, power_is_null, qm_S4_vs_S5). Every .py mention cited; 0/0/26pp checker green, 0 orphans. NEXT: avenues 1-10 on P17 -- the last of the corpus.

## AVENUES 1-10 -- EXECUTED r1406 (off the whole-read, at source). VERDICT: all ten pass; no edits, no red-flags.
- **A1 Q-mine -- PASS.** Philosophical register but every claim has standing (grounded in cited papers + the 3 receipts). The "three faces that turn out to be one" is marked as the thesis; dissolutions scoped ("Lambda's value the ledger's one input scale, not predicted"). Nothing to strip.
- **A2 own accomplishments -- PASS.** The power=height identity ("older than the geometry"), the seven-way unification, the two-real-forms consolidation, all claimed at weight -- with the seven-as-one explicitly a conjecture thesis vs the seven each established. Nothing undersold.
- **A3 press the gap -- PASS (exemplary).** The overclaim guard is STRUCTURAL: the seven-way unification is flagged "[reach -- the seven are each established; reading them as one fact is the thesis, decidable by the test in sec:frontiers]"; the frontiers stake decidable falsification tests (free-data-count; the ledger; the matter home; the seam phase) each marked conjecture/[not claimed]. Lambda NOT predicted (honest). No overclaim anywhere.
- **A4 identity -- PASS (emphatic).** Title = "the object, not its uses"; the paper stays rigorously on the object -- "None of them is about the substrate itself ... This paper is about the object." The uses are the other papers, by design.
- **A5 positive-face -- PASS.** Leads on what the substrate IS (real / universal standard / maximal symmetry); Eddington "at weight, corrected and grounded" not "wrong"; dissolutions are consequences of the positive fact, not refutations.
- **A6 symmetry -- PASS.** The two real forms (Lorentzian dS_5 / Euclidean S^5) both KEPT and both "real by construction"; the Lorentzian-is-existent / Euclidean-is-timeless distinction is a PRINCIPLED, stated warrant ("holds no clock"), not a dropped conjugate. Imaginary/real handled the same (reaching-instrument vs world). No vantage privileged without warrant.
- **A7 bespoke two-way -- PASS.** Forward: the substrate is the object every paper (incl. P6) applies (intro lists the corpus uses). Backward: P6's least-arbitrariness (Rule 2) applied to justify the substrate's selection -- "a symmetry-breaking modulus is the adjustable parameter that criterion rejects, and maximal symmetry the unique structure that requires its configuration".
- **A8 dissolution census -- PASS (at weight).** Cosmological-constant problem (no Planck scale for Lambda to be small against, no bare-vs-vacuum split); coincidence (density=clock, constant rung); horizon (CMB uniformity = maximal symmetry, not early contact); Planck-values-as-gauge-combinations. Lambda's value NOT predicted (honest, the one input scale).
- **A9 checklist -- PASS.** Frontiers stake decidable tests with maturity marks; sec:landing is the corpus-unification recap; idioms (power of a point, Hubble-Eddington, the seven rungs) consistent.
- **A10 forward-refs -- PASS.** This IS the core: every paper descends from it, the intro enumerates the corpus uses, the frontiers point forward to the deciding tests. The descent architecture (seven results from one fact) is the reference structure.

## P17 FULLY SWEPT (r1406): avenue 11 (3 receipts -- power-of-a-point/tangent-null pair + su(3) real-form co-location) + avenues 1-10 (all pass). No computation surfaced unreceipted; no framing edit warranted. The foundational core is the most explicitly maturity-marked paper in the corpus (conjecture/[not claimed] throughout + staked falsification tests).
