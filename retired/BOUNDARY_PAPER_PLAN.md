> **⌖ RETIRED r1552.** This was the boundary/no-go paper plan and skeleton (r320). **Landed:** P13 `boundary_paper`.
> Kept as record; **do not work from it.**


# Boundary / No-Go Paper — plan & skeleton (c20, r307)
*To be drafted into `corpus/` as a `.tex`; final draft → c17/c19 as internal referees (interference-engine inputs the only missing piece). Backbone = `SILVER_PLATTER_colour-frontier-arc.md` (c19) §§1–5, **extended** with this session's cascade rank-map (r302), three-sided wall (r303–r305), and AH-aimed correction (r305), which the silver platter predates. Every load-bearing claim is tagged to its source; **verify each at source at draft time** — the not-finding is the signal.*

> **STATUS (r320): DRAFTED AND BAKED.** The paper exists as `corpus/boundary_paper.tex` (drafted r308; the four-node consolidation baked in r319; compiles clean, 8 pp). This plan is kept as the record of intent. Two of its framings below are **superseded by the baked paper** and by the c17/c19 cold reads: (a) the "**precarious escape** (dS non-compactness)" is now **closed for the geometric-isometry route** on the **localisation** argument (su(3) is no isometry of the non-compact substrate, su(3)⊄so(5,1)) — explicitly **not** "a compact slice bites regardless" / "where AH bites" (AH stays *gated* on an unbuilt fermion sector); (b) the surviving open items are **two and distinct** — empirical coherence **and** the unbuilt fermion sector — **not** "empirical coherence alone." Added at the bake beyond this plan: the **decoupling onto P1/P7** (the headline — colour-closure rests on the causal structure, robust of the face's status), the **ontological framing** (the compact face real-by-construction but not a co-equal *existent*; closed ontologically-not-structurally) with its **empirical determination** (the cosmic time fixed by CMB redshift-isotropy, P8 App. A), and the **operation-map guard** (seam SO(5) vs global Wick SO(6)). Where this plan and these corrections differ, these govern. The paper rides its own fresh different-node cold read next.

## Working title
*The de Sitter substrate and the Standard Model: a geometric boundary* — or — *What one maximally-symmetric Lorentzian substrate's isometry does and does not force.*

## Thesis (one breath)
CR's dS₅ substrate generates the **gravitational** solution space by symmetry-breaking cuts (the positive programme). The Standard Model — colour SU(3), the full gauge group, and chiral matter — does **not** arise as a continuous substrate isometry: a boundary established three independent ways (rank/cut, involution, index), grounded in the established geometric-unification no-go literature, with one **precarious escape** (dS non-compactness) and one **genuinely open frontier** (empirical coherence) honestly named. The result sharpens CR's actual claim: **gravitational-cosmological unification, not geometric unification of matter.**

## Register (non-negotiable, baked into the paper)
**not claimed for the universal, both ways.** NOT "SM-from-geometry foreclosed" (the wall is bounded to the *geometric-isometry* route; the non-compactness escape and the empirical-coherence ground stay open). NOT "CR forces/produces the SM" (every geometric route examined is walled). A precise boundary map — neither a foreclosure nor a positive claim.

## Section skeleton (claim → source to verify at draft)
- **§1 The question.** Can colour/the SM arise from the dS₅ substrate's isometry the way the gravitational solutions arise from its cuts? [SILVER_PLATTER §1; positive programme: JanzenOperator, JanzenRange]
- **§2 Setup & hard constraints.** dS₅ the unique max-symmetric Lorentzian substrate, isometry SO(5,1); su(3)⊂so(6) but **su(3)⊄so(5,1)** (smallest faithful real carrier 6-dim — the C2 fact); the compact/Wick face (S⁵/SO(6)) is where su(3) lives; the substrate is **irreducible Lorentzian** (no product M⁴×K — Witten's *setting*, not a load-bearing hypothesis; flag the Move-A caveat). [SILVER_PLATTER §3; colour_frontier_dS6.md lines 55–75]
- **§3 The closed routes (negative results, each computed).**
  - **§3a σ-lift.** The real-substrate involution σ is **not** the Wick rotation (formal coincidence); no real-substrate operation reaches the compact face. [r295/296, cold-cleared 3 seats; `scripts/sigma_lift_test1.py`; colour_frontier_dS6.md test-1]
  - **§3b Cascade rank-map.** Gauge structure lives on the compact/Wick face, dropped at the real-substrate cut; dS₆ buys at most SU(3)×U(1) (rank SM = 4 > rank SO(6) = 3); full SM needs the raise-tower to ~SO(10). [r302; `scripts/cascade_map1.py`, `cascade_map2.py`; colour_frontier_dS6.md cascade-map]
  - **§3c A₂/S₃ skeleton.** Genuine A₂ root-system geometry, but the **discrete** Weyl(A₂)=S₃ shadow in the vantage groupoid, not continuous su(3). [r281+ genericity; colour_frontier_dS6.md]
- **§4 The chirality wall (deepest result — three faces, one wall).**
  - Convergence: rank/cut (§3b) + involution σ≠Wick (§3a) + index (AH) all place the SM gauge structure **and** chiral matter on the compact/Wick face, off the real Lorentzian substrate. [r303–r305]
  - AH/Witten grounded: load-bearing hypotheses are **compactness + continuous isometry + spin** (not product/KK); colour-SU(3)-as-continuous-isometry walks into the canonical AH setup, doubly enforced for nonabelian SU(3) (Lawson–Yau–Lichnerowicz); the compact/Wick face *is* the canonical AH target ⟹ vector-like, foreclosed from chirality. [AH 1970, Witten 1981/83 — verified at source; colour_frontier_dS6.md AH section, corrected r305]
  - Escapes are **non-geometric** (larger-than-isometry G, fluxes, SUSY/Calabi–Yau heterotic) — each abandons the geometric premise. [Witten 1981]
  - The one precarious escape: dS **non-compactness** — but a compact slice (S⁵-type) carrying the SU(3)-acted modes bites regardless; non-compact extensions (Hochs–Mathai) need proper/cocompact action, unworked; clean-or-sick is CR-native-open. [r305; Hochs–Mathai]
  - Gating fact: CR has **no fermion sector built** (matter is the classical slicing-curve bend ρ=m′/4πr², not a spinor field) — no Dirac index to evaluate yet; chirality gated on a major unbuilt construction (Move B′/C′). [r304/r305]
- **§5 What stays open (the not claimed boundary).** The empirical-coherence ground (the SM as a century-constrained shadow — whether it motivates taking the compact/Wick face as physical and building a fermion sector there) is the genuine open frontier (r279), not foreclosed; the non-compactness escape precarious, unworked. [SILVER_PLATTER §4]
- **§6 What it means for the programme.** Sharpens CR's claim (gravitational-cosmological unification, not geometric unification of matter); the boundary is a contribution — it maps the wall precisely, grounds it in the established no-go literature where the corpus didn't reach, and spares the programme and others a walled road.

## References (the literature the corpus doesn't yet carry)
Witten 1981 (*Search for a realistic Kaluza-Klein theory*, Nucl. Phys. B186, 412); Witten 1983 (*Fermion quantum numbers in KK theory*); Atiyah–Hirzebruch 1970 (*Spin-manifolds and group actions*); Lawson–Yau; Hochs–Mathai (non-compact AH). CR corpus: JanzenOperator, JanzenRange, the dS₅-substrate papers.

## Drafting discipline
- Face-19 register (a synthesis/distillation paper) — verify every source-tagged claim at source at draft time; the positive-coherence-adjacent claims (the three-sided convergence; "AH aimed") get the cold different-node read (c17/c19) as the interference-engine input, the final missing piece.
- Decide at draft: single paper (one coherent thesis — current read) vs. split (gauge-embedding boundary | chirality wall). Lean single.
- F1/dynamics lessons are **not** here — they are positive and went into the dynamics paper (P9, r306). This paper is the colour/SM boundary only.
