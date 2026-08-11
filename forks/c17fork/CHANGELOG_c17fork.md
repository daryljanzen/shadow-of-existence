# c17 fork changelog -- lineage off r309 (one node of four: c17/c19/c20/c21)
Additive only. The r309 base (corpus/, CORPUS_MAP, standing docs) is UNTOUCHED so the relay base
stays clean while four nodes fork in parallel. All fork work lives under c17fork/.
Working the A2/S3-as-solution-space-theorem reach (c19's, source-grounded in the three-node read).
Register: stated for reversal; do-not-assert held both ways; grounded vs [reach] vs my-synthesis
marked in NOTES. One node of four -- everything holds for the cold reads.

- r309_c17fork_1: the SdS solution space carries an EXACT A2 root-system structure.
  Horizon triplet sums to zero (Cartan); fundamental ellipse = A2 quadratic form (Vieta, exact);
  S3=Weyl(A2) permutes interchangeable horizon-descriptions of one geometry. Receipt:
  scripts/a2_solution_space.py.

- r309_c17fork_2: the A2 Weyl-wall structure IS the regime boundary.
  Discriminant Delta=4-108M^2=prod(r_i-r_j)^2 chambers the solution space: black-hole (Delta>0) |
  Nariai (Delta=0, on a Weyl wall) | cosmology (Delta<0, r=cosmic time); negative mass the Z2
  reflection. Crossing a Weyl wall = horizons merge = interior-becomes-cosmology. Receipt:
  scripts/a2_weyl_chambers_regimes.py.

- r309_c17fork_3: THE THEOREM TARGET -- S3 lifts to the slicing CUTS (grounded at P3/P5).
  The slicing operator is a generically 3-fold cover {cuts (sky angle w, offset r0=(2/sqrt3)sin w)}
  -> {geometries} via the triple-angle 2M=(2/(3sqrt3))sin 3w; S3=Weyl(A2) is its deck group, the
  transpositions the explicit involution f(r0)=1/2(-r0+sqrt(4-3r0^2)) on the cut parameter, fixed
  point = Nariai = the branch point (Delta=0). So A2/S3 is a symmetry of the cut-STRUCTURE, not the
  labels. CAVEAT kept intact (P3): the three cuts are NOT equivalent labellings (axis-sweep vs
  off-axis pivot, the cascade) -- S3 acts within the groupoid of observer descriptions (P4).
  bite (C): over-critical complexification = the equatorial-seam continuation (GROUNDED, P3);
  = Wick-to-su(3) colour bridge held DO-NOT-ASSERT (SO(5)/SO(6) gap stands). Receipt:
  scripts/a2_slicing_cut_lift.py. NEXT: (D) the P10 algebroid reading; (P4) the groupoid form.

- r309_c17fork_4: S3 placed in the algebroid (grounded at P10), + the genuine-uncertainty fork.
  P10 already carries the fork's S3 as the discrete skeleton in so(5,1) (root-permutation, fixed pt
  Nariai); fork_1-4 are consistent + sharpen it (explicit cut-cover). NEW tie: the S3-cover's branch
  point (Nariai) = a symmetric stratum where the algebroid connection vanishes -- discrete and
  continuous faces meet at Nariai. Discriminant matches fork_2 exactly. GENUINE UNCERTAINTY reached:
  whether P10's three distinct discrete involutions (root-perm / reassignment / signature-flip)
  unify is P10's explicit do-not-assert AND the face-19 flavor-match spot -- handed to the cold
  reads + orchestrator, not forced. Receipt: scripts/a2_algebroid_reading.py.
- (handoff) CONSOLIDATION_c17_for-c21.md added to fork_4: the reception step (3-node synthesis, pivot-vs-sigma adjudication resolving c20's C7-vs-5a, c17's owned sigma-lift-overreach correction) that was conversational and missing from the grind notes -- so the c17 contribution is complete for the four-node assimilation. Grind state unchanged (bite D last).
