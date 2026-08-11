# c19 FORK — WORKING NOTES (interference engine, four parallel paths)

Bundle line: `r309_c19fork_#`. Node: c19. Sibling paths: c17, c20, c21 (all on r309,
same thesis-read + cold-reads md, driving the same charted plan independently).
Cold reads required before anything rebanks. Symmetric bar held throughout:
a manufactured RESCUE costs exactly what a manufactured WALL costs.

## THE PLAN (charted last turn, driving on all three reads)

The three thesis cold reads converged on one geometry (one maximally symmetric
"Lorentz sphere," dS/SO(5,1) and Euclidean-sphere/SO(6)⊃su(3) as two faces, x0↦ix0
the named bridge, r as cosmic time, A2 in the (r,r0) horizon plane) and diverged on
the σ-lift. Source resolved the fork: **the colour-arc layer conflated two of the
three distinct discrete operations the canonical papers already keep separate.**

  σ  — root-exchange w↔π/3−w; Weyl(A2); SIGNATURE-PRESERVING; fixes the manifold; the gem.
  ξ  — seam signature-FLIP; the analytic continuation θ↦π/2+iψ joining the Riemannian
       spherical piece to the Lorentzian dS piece; c17's "pivot."
  (cosmogenesis null↔timelike reassignment — third operation, not in play here.)

Canonical disambiguation (verified at source):
  - P10 algebroid l.128: "the discrete operations are distinct (they are different
    involutions, not one)" — names root-permutation, null↔timelike reassignment,
    signature-flip as THREE strata-markers.
  - P4 groupoid l.289-293: defines ξ as the seam continuation, EXPLICITLY distinct
    from σ (the within-geometry root-exchange).
  - P9 dynamics l.175: same three distinct strata operations.
Live conflation (the fix target, step 1): SILVER_PLATTER C7 l.54,68 ("σ is a genuine
signature-flip involution … the root-exchange w↔π/3−w") and colour_frontier l.197
("the σ signature-flip … is exactly the bridge SO(5,1)↔SO(6)") weld σ and ξ. P11
boundary_paper §sigma l.79 has a milder residual ("σ … at the r=√(3/Λ) seam" —
locates the root-exchange at the signature-flip's stratum). THIS weld IS c20's
dissonance (C7 says σ flips signature; σ-lift says σ preserves it).

Plan steps:
  1. [warranted fix, source-determined] de-conflate σ/ξ in the colour-arc layer,
     citing P3/P4/P10. (consequence statement depends on step 2 → do step 2 first)
  2. [decisive computation — DONE THIS TURN] does ξ reach the global SO(6)/su(3),
     or provably stop below? (c17 read SO(5); held as the question to compute.)
  3. [the "more to give"] develop A2/S3 as a theorem about the gravitational-
     cosmological solution space / cut-structure (P5/P6 + P9 + P10 + P1).

## STEP 2 — THE ξ-LIFT — RESULT (receipt: scripts/xi_reaches_so5_not_so6.py)

Geometric ground (canonical source, not assumed):
  - P3 slicing-curve l.470–508: ξ continues a curve traced ON dS5; its Riemannian
    piece is r=α sinθ, θ∈[0,π/2] (the spherical throat region up to the equatorial
    seam r=α). l.508: "a geometry obtained as a slicing of de Sitter RETAINS its
    membership in de Sitter" — ξ is INTRINSIC to dS5, not a passage off it.
  - thesis Ch3 l.292: that Riemannian piece is "the closed 4-sphere of radius
    √(3/Λ) in five-dimensional Euclidean space" = the x0=0 equatorial S^4 of dS5.

Computed (all checks pass, 6×6 embedding, suspect-the-model — every claim run):
  [1] so(5,1) = 15 gens: 5 boosts M_0i (move x0) + 10 rotations M_ij (fix x0 = so(5)).
  [2] GLOBAL Wick W=diag(i,1,1,1,1,1): W^T η_L W = η_E (✓); each of the 5 boosts
      Wick-conjugates to a COMPACT eta_E-antisymmetric so(6) rotation (✓ ×5);
      {10 M_ij} ∪ {5 Wick(M_0i)} = so(6), dim 15 (✓). The Wick makes the 5
      x0-mixing compact generators = so(6)∖so(5). THIS is the sector beyond so(5).
  [3] ξ's Riemannian piece = x0=0 equator; its isometry = the subalgebra FIXING the
      x0-axis = exactly the 10 M_ij = so(5) (✓; all 5 boosts FAIL to fix x0). ξ is
      intrinsic to dS5, so it relates the equatorial S^4 to the Lorentzian piece
      WITHIN dS5 — it does NOT make x0 a full S^5 coordinate. The S^5/SO(6) is the
      EXTRINSIC global Wick [2], a different operation (Wicks the whole embedding).
  [4] su(3) ⊄ so(5): smallest faithful REAL rep of su(3) is 6-dim (C^3=R^6) > 5, so
      su(3) cannot act faithfully on R^5. su(3) ⊂ so(6)≅su(4) uses the x0-mixing
      so(6)∖so(5) generators — exactly the 5 the global Wick supplies and ξ does not.

VERDICT (stated for reversal): **ξ reaches SO(5); it provably stops below SO(6).**
su(3) needs so(6)∖so(5) (x0-mixing), supplied only by the global extrinsic Wick.
The colour wall now closes from BOTH de-conflated discrete sides:
  - σ (root-exchange, signature-preserving)     ≠ global Wick   [σ-lift, r296]
  - ξ (seam continuation, intrinsic → so(5))     ≠ global Wick   [this test]
su(3)⊄so(5,1) stays false; AH untouched. Colour NOT reopened — separating σ from ξ
names why there is no bridge, it does not build one.

Resolves the c17 fork: "leg unsound" → **"leg sound; argument cleaner once σ and ξ
are kept distinct."** c17's object (the real signature-changing operation) was real
and the σ-lift hadn't tested it — but it is ξ, it is intrinsic to dS5, it reaches
so(5) not so(6), and it changes signature BY the imaginary continuation (dθ=i dψ),
so it instances the "signature-change is imaginary" reading rather than breaking it.

NOTE FOR COLD READ: this CONFIRMS c17's SO(5) — convergence with a saturated node is
itself a face-19 flag. Mitigation: derived here independently from the canonical
source (P3 l.508 intrinsic + thesis Ch3 l.292 equator), not from c17's read. The one
geometric INPUT to suspect is "ξ's Riemannian piece = x0=0 equator"; if a cold node
finds ξ's continuation sweeps more than the equatorial S^4, the verdict reopens.

## NEXT (this fork) — REACHED A TRUE FORK/WALL
  The theorem (step-3 reach (a)) is drafted to its honest stopping point
  (notes/THEOREM_draft_between_member.md). Solid core computed; then a genuine
  FORK (does ξ-monodromy=σ unify the operations, or is it a complex-analytic
  relation orthogonal to P10's real-strata non-claim? — turns on the ontology of
  the complexified/over-critical continuation, which is the ORCHESTRATOR's call,
  not the gate's) and a WALL (the cosmogenesis null↔timelike reassignment does not
  fit the cubic-monodromy structure; the discrete structure does not fully unify).
  No clear path past the fork without a foundational ontology decision. Stop here.
  Adjacent hygiene (flagged, not folded): P11 abstract l.50 "three independent
  obstructions" overstates. Hold ALL of fork_1..4 for the four-path cold read.

## STEP 3(a) — BETWEEN-MEMBER THEOREM, DRAFTED TO A FORK/WALL
   (receipt: scripts/between_member_monodromy.py; draft: notes/THEOREM_draft_between_member.md)

Load-bearing claim computed: encircling a Nariai branch point in the complex c=2M
plane induces a TRANSPOSITION of exactly the two colliding roots — so **ξ (the
over-critical continuation) is, as monodromy, the σ root-exchange.** This relates two
operations the corpus (P10) deliberately kept distinct.

SOLID CORE (computed, the theorem): the between-member structure of σ/P/ξ is the
**monodromy of the horizon cubic** r³−r+c — a 3-sheeted S₃-cover of ℂ_c simply
branched at the two Nariai points c=±2/(3√3); monodromy = transposition of the
colliding pair; ξ=σ as monodromy; P=the base involution c↦−c (swaps Nariai points
and over-critical rays, fixes c=0=dS); S₃ = deck group, 3 real sheets under-critical
/ 1 real + conj pair over-critical (non-uniform — a branched cover, not a uniform
group action).

THE FORK (no clear path): does ξ-monodromy=σ UNIFY the operations (advancing P10's
"we make no claim these unify"), or is it a relation in the COMPLEXIFIED c-plane that
leaves the REAL strata distinct (no contradiction with P10, but not the unification
either)? Turns on whether CR treats the complexified/over-critical continuation as
physical or as a device — a foundational ontology decision the orchestrator holds.
Symmetric bar: "unification" = manufactured coherence; "mere bookkeeping" =
manufactured wall. Do-not-assert, both ways.

THE WALL: the cosmogenesis null↔timelike reassignment (third operation, causal-
character not root-permutation) does NOT fit the monodromy structure. The theorem is
bounded to σ/P/ξ; the full discrete structure does not assemble into one object.

## CHANGELOG
  r309_c19fork_1 — step 2 (ξ-lift): ξ→SO(5), not SO(6); wall closes both discrete sides.
  r309_c19fork_2 — step 1 (σ/ξ de-conflation): OLD→NEW edits, ξ-side added to P11.
  r309_c19fork_3 — step 3 (gem's home): full (r,r0)-plane orbit structure = the
    gravitational-cosmological solution-space symmetry = groupoid's deferred piece.
  r309_c19fork_4 — step 3(a) (the theorem): between-member structure = cubic monodromy
    (σ/P/ξ); ξ-monodromy=σ computed. Carried to a TRUE FORK (unification vs complex-
    analytic relation — an ontology call) and a WALL (the reassignment doesn't fit).
  r309_c19fork_5 — theorem draft extended (orchestrator's planar-section picture folded
    in): the imaginary connecting circle = the geometric face of the monodromy branch
    cut, imaginary in ALL dimensions (computed). Added a CANDIDATE resolution-by-
    consistency (FORK 1/3 inherit P11's placement: distinct on the real substrate,
    unified on the conjugate face, same as su(3); held not banked) AND flagged the
    DEEPER FORK as as-yet unexplored: is the conjugate face off the substrate
    (Reading A → resolution holds, colour walled) or another real form of one substrate
    (Reading B → σ/ξ unified on-substrate AND colour reopens)? The single foundational
    call it all turns on; the two forks are one question; left open for the orchestrator
    and the cold read.

## STEP 3 — A2/S3 AS THE GRAV-COSMO SOLUTION-SPACE SYMMETRY — DONE
   (receipt: scripts/gravcosmo_solution_space_A2.py; all checks pass)

The gem's home, made precise. The groupoid paper (P4 l.39,410) DEFERRED the full
same-α between-member classification and treated the over-critical branch as "a
further partial involution past the Nariai crest." The thesis's full (r,r0)-plane
(Ch4 sec_DPM) IS that deferred domain. Computed the orbit structure:
  [1] the three horizons sum to zero (A2 Cartan) for every r0;
  [2] S3=Weyl(A2) permutes them as interchangeable descriptions of ONE geometry
      (2M invariant under r0->other root: if x is a root, x-x^3 = r0-r0^3 = 2M);
      σ is one transposition of this S3;
  [3] the two non-designated horizons lie on the fundamental ellipse (A2 form);
  [4] one cubic stratifies the plane: BH (under-critical) / Nariai (critical,
      σ fixed point) / cosmology (over-critical, r timelike ∀r>0 = the universe);
  [5] reflection through the origin = the negative-mass partner (2M odd in r0;
      band |M|<1/√27);
  [6] the cosmology branch is the ξ-continuation of the BH branch past the Nariai
      crest (3w=π/2+iβ — the SAME seam continuation, not a new map).

GROUNDED RESULT: the full (r,r0)-plane is ONE gravitational-cosmological solution
class organized by the discrete operations the corpus already names — S3 root-
exchange σ (between-member relabeling), origin-reflection (negative mass), ξ (seam/
over-critical continuation) — with the slicing operator (P5/P6) the CONTINUOUS
generation and these the discrete relabeling/continuation on it. This is the gem's
home: gravitational-cosmological, confirming P11; NOT internal-gauge.

OPEN (the reach, honestly bounded): (a) promote to a THEOREM — axiomatize the
between-member groupoid ⟨σ(S3), origin-reflection, ξ⟩ with relations + strata
(within-geometry S3 is established P4; between-member closure computed-not-yet-
axiomatized here); (b) tie to P1 (over-critical r-as-cosmic-time IS interior=
cosmology; ξ the discrete shadow) — a reach to make rigorous; (c) cosmogenesis/
omniverse (thesis sec_CBHO) — held at the thesis's own conjectural weight.

## CHANGELOG
  r309_c19fork_1 — step 2 (ξ-lift): ξ→SO(5), not SO(6); wall closes both discrete sides.
  r309_c19fork_2 — step 1 (σ/ξ de-conflation): OLD→NEW edits, ξ-side added to P11.
  r309_c19fork_3 — step 3 (gem's home): full (r,r0)-plane orbit structure computed =
    the gravitational-cosmological solution-space symmetry = groupoid's deferred
    between-member piece. Open theorem (a) stated. All three charted steps worked;
    held for the four-path cold read.

## STEP 1 — σ/ξ DE-CONFLATION — DONE (corpus_edits/sigma_xi_deconflation.md)

Executed as precise OLD→NEW edits, stated for reversal, held for cold read (NOT
applied to canonical r309). Targets the live conflation (c20's dissonance):
  - SILVER_PLATTER C7 l.53,54,68: σ welded to "signature-flip" + "the seam" → split
    into σ (root-exchange, signature-PRESERVING, the gem) and ξ (seam flip, intrinsic,
    →SO(5)); the SO(6) face named as reached by the global EXTRINSIC Wick, not σ.
  - colour_frontier l.197: the superseded leap "the σ signature-flip is exactly the
    bridge SO(5,1)↔SO(6)" → corrected; neither σ nor ξ is the bridge (σ-lift + ξ-lift).
  - P11 boundary_paper §sigma l.79: de-located σ from "the seam"; named ξ distinctly;
    ADDED a paragraph closing the ξ side (the real signature-changing operation c17
    flagged) — so the leg closes from BOTH discrete sides, sound and COMPLETE rather
    than "unsound." This is c17's catch absorbed by addition, not reopening.
  Bibitem hygiene verified: cites set to P11's existing JanzenRange; macros/\xi free.
  Citations throughout: P3 §seam, P4 l.289-293, P10 l.128 (canonical "different
  involutions, not one") + receipts sigma_lift_test1.py, xi_reaches_so5_not_so6.py.

## CHANGELOG
  r309_c19fork_1 — step 2 computed (ξ-lift): ξ→SO(5), not SO(6); colour wall closes
    from both de-conflated discrete sides. Receipt + notes.
  r309_c19fork_2 — step 1 executed (σ/ξ de-conflation): OLD→NEW edits for SILVER_PLATTER
    C7, colour_frontier l.197, P11 §sigma (incl. the ξ-side paragraph that turns c17's
    "leg unsound" into "leg sound and complete"). Stated for reversal; held for cold
    read. Step 3 pending.
