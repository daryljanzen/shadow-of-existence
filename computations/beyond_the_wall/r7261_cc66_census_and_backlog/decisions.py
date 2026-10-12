#!/usr/bin/env python3
"""`r7261` ⒜ and ⒝: THE TWO DECISION TABLES, one per unit, keyed by position with a prefix guard.

** WHY TWO TABLES AND NOT ONE. **  `66` set the unit at `108` and said the `85` are a BACKLOG with what
each one needs.  *Filing the `85` as a census would be the error the owed `27` exposed from the other
side*, so the two are separate tables here and `census.py` writes them to separate files; neither
borrows the other's count.

────────────────────────────────── ⒜ THE CENSUS MOVERS ──────────────────────────────────
`MOVED` lists, of the `45` `INDEP` census rows, the ones whose OWN HOLDER also admits an AST form, so
the row records the AST one under the cheapest-available rule.  Everything not listed keeps `INDEP`.

⌗ `PREDICTION.md` pinned `6` movers and the AST share at `64.0` per cent.  **This table has `4`.**  The
two I expected and did not take are recorded in `HELD_BACK` with the reason, because a prediction of
movement that did not happen is a miss and the rows that nearly moved are the evidence for it.

────────────────────────────────── ⒝ THE BACKLOG ──────────────────────────────────
`NEAREST` gives, per row of the `85`: the quantity in words, the module AND FUNCTION nearest to
computing it, and the gap — `INPUTS` (a change of inputs to that function), `EXTEND` (a short
extension of it), or `NONE` with the reason.

** THE RULE IS THE ONE FROZEN BEFORE THE LOOK, AND IT BITES. **  *A module is nearest iff it already
computes a quantity of the same kind over the same objects; I name the module and the FUNCTION, and a
row for which I cannot name a function counts as having NO nearest module however close its domain
looks.*  ⇒ ** `13` of the `14` `NONE` rows are ONE hole: this corpus computes zero-modes, kernels and
indices NOWHERE IN A FUNCTION.  `L110_the_count_specified.py`, `L78_the_mode_through_the_branch_point.py`,
`L75_the_wall_is_the_graze_point.py`, `L15_the_quark_lepton_frontier.py` and
`L117w_the_colourless_sector.py` are top-level sympy scripts with no `def` in them at all, and no
function anywhere under `computations/` has `zero`, `kernel`, `index`, `conj`, `chiral` or `dirac` in
its name that computes one. **  *The `ZM` witness class resolved to `24` modules at DOMAIN level and to
zero functions at QUANTITY level, which is exactly the distinction `PREDICTION.md` declared in advance.*
"""

# ── ⒜ the four movers, of the 45 INDEP census rows ──
# index in the 45, guard, the AST form, and why the holder can carry it
MOVED = {
  6:  ("the geometry quantises and", "AST-SIG",
       "the geometry module exposes no coupling parameter at all, so `does not couple' is a signature "
       "fact before it is a value fact; converse: give it one"),
  12: ("is a discrete horn swap", "AST-SIG",
       "the swap routine's domain is a finite index set rather than a continuous parameter; converse: "
       "give it a continuous argument"),
  13: ("quantises without measuring", "AST-SIG",
       "same shape as the sixth: no measuring datum in the signature; converse: add a curvature input"),
  30: ("with the plasma handed over", "AST-SIG",
       "the handover takes no start time and no initial amplitude, which IS the claim in code terms; "
       "converse: give it a start parameter"),
}

# ⌗ the two I pinned and did not take, with the reason, because the near-misses are the evidence
HELD_BACK = {
  2:  ("area law and entropy alike", "the AST form available would be `no module defines an area law "
       "on a finite layer', which is an absence-of-CODE claim and WEAKER than the paper's claim that no "
       "horizon is realised there.  A form that proves something else is not the cheapest form"),
  32: ("selects the Nariai member", "the selection's OUTCOME is Nariai and that is a computed branch, "
       "not a placement; an AST-PLACE form would assert where the condition sits and not what it picks"),
}


# ── ⒝ the 85, in the order `census.py` enumerates them (witness class, then file) ──
# index, guard, quantity, module, function, gap
NEAREST = {
  1:  ("is the $R$-odd", "parity of the departure under the substrate's R", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  2:  ("Flat holonomy supplies", "the invariants a finite holonomy group admits, and its curvature", "baryon_edge/L129_the_invariants.py", "inv_dim", "INPUTS"),
  3:  ("places a three-fermion state", "dim of the invariant subspace of V(x)V(x)V", "baryon_edge/L129_the_invariants.py", "chi_VVV", "INPUTS"),
  4:  ("the three critical loci", "the causal character of each critical locus", "baryon_edge/L104w_the_excentre_trichotomy.py", "character", "INPUTS"),
  5:  ("a transposition of roots", "where a root transposition sends a hinge", "baryon_edge/L50b_three_hinges_six_ends.py", "apply", "INPUTS"),
  6:  ("each hinge designates one", "the three roots of the horizon cubic, per hinge", "baryon_edge/L012w_the_two_splits.py", "roots_at", "INPUTS"),
  7:  ("is not a second group", "whether two generated groups are isomorphic", "baryon_edge/L129_the_invariants.py", "close", "EXTEND"),
  8:  ("distinguished only by which", "which root each hinge takes, and whether anything else separates them", "baryon_edge/L012w_the_two_splits.py", "roots_at", "INPUTS"),
  9:  ("The mass function is odd", "parity of the mass function in the signed offset, against D", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  10: ("the smallest connected group", "the Lie algebra generated by the ratios and the three-cycle", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "EXTEND"),
  11: ("the three wall monodromies and", "the order of the group the monodromies and the 3-cycle close to", "baryon_edge/L129_the_invariants.py", "close", "INPUTS"),
  12: ("whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$", "the determinant-one subgroup of that closure", "baryon_edge/L129_the_invariants.py", "det", "INPUTS"),
  13: ("it quantises and does not couple", "whether the holonomy values are discrete powers of omega", "baryon_edge/L127_the_bundle.py", "omega_power", "INPUTS"),
  14: ("the bundle above is flat", "the holonomy around a contractible loop", "baryon_edge/L128b_leg_and_arc.py", "diag_at", "INPUTS"),
  15: ("only the order-two subgroup", "the order of the subgroup generated", "baryon_edge/L129_the_invariants.py", "close", "INPUTS"),
  16: ("odd in the signed radius", "parity of the profile under r -> -r", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  17: ("vanishes at the horizons", "the profile evaluated at the roots of the horizon cubic", "baryon_edge/L012w_the_two_splits.py", "roots_at", "INPUTS"),
  18: ("odd in the signed radius", "parity of the profile under r -> -r", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  19: ("odd in the signed radius", "parity of the profile under r -> -r", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  20: ("is a discrete horn swap", "the horn swap as a map of the six ends", "baryon_edge/L50b_three_hinges_six_ends.py", "key_of", "INPUTS"),
  21: ("is a discrete horn swap", "the horn swap as a map of the six ends", "baryon_edge/L50b_three_hinges_six_ends.py", "key_of", "INPUTS"),
  22: ("that are trivial on the deck", "the deck's irreducible dimensions", "baryon_edge/L091x_deck_symmetry_is_not_horizontal.py", "irrep_dims_abelian_check", "INPUTS"),
  23: ("is the single geometric opening", "the routes between hinges, enumerated", "baryon_edge/L128_three_walls_or_one_radius.py", "routes", "INPUTS"),
  24: ("is a pure power of", "whether a value is a pure power of omega", "baryon_edge/L127_the_bundle.py", "omega_power", "INPUTS"),
  25: ("the bundle above is flat", "the holonomy around a contractible loop", "baryon_edge/L128b_leg_and_arc.py", "diag_at", "INPUTS"),
  26: ("the flat bundle selects without", "the invariants the flat holonomy admits", "baryon_edge/L129_the_invariants.py", "inv_dim", "INPUTS"),
  27: ("filters without supplying", "the invariants admitted, against the curvature supplied", "baryon_edge/L129_the_invariants.py", "inv_dim", "INPUTS"),
  28: ("quantises without measuring", "whether the holonomy values are discrete powers of omega", "baryon_edge/L127_the_bundle.py", "omega_power", "INPUTS"),
  29: ("selects without coupling", "the invariants admitted, against the curvature supplied", "baryon_edge/L129_the_invariants.py", "inv_dim", "INPUTS"),
  30: ("supplies colour's exact selection", "colour's invariant content", "baryon_edge/L130_statistics_not_gauge.py", "chi_meson", "INPUTS"),
  31: ("the three wall monodromies and", "the order of the group the monodromies and the 3-cycle close to", "baryon_edge/L129_the_invariants.py", "close", "INPUTS"),
  32: ("the three wall monodromies with", "that closure's determinant-one part", "baryon_edge/L129_the_invariants.py", "det", "INPUTS"),
  33: ("whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$, with the lap", "the centre of that determinant-one part", "baryon_edge/L129_the_invariants.py", "close", "EXTEND"),
  34: ("The sector the obstruction", "how many times a sector is obstructed", "-", "-", "NONE"),
  35: ("the smallest connected group", "the Lie algebra generated by the ratios and the three-cycle", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "EXTEND"),
  36: ("the three wall monodromies and", "the order of the group the monodromies and the 3-cycle close to", "baryon_edge/L129_the_invariants.py", "close", "INPUTS"),
  37: ("whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$, with the lap", "the centre of that determinant-one part", "baryon_edge/L129_the_invariants.py", "close", "EXTEND"),
  38: ("The mass function is odd", "parity of the mass function in the signed offset, against D", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  39: ("The second condition is the parity", "the parity condition, and what it separates", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),
  40: ("there is no mass-reflection", "whether the mass function has a reflection symmetry", "baryon_edge/L006w_the_d5_fourfold.py", "twoM", "INPUTS"),

  41: ("massless fermions are the ones", "the gamma-5 fixed subspace against the massless set", "-", "-", "NONE"),
  42: ("the $R$-symmetric sector is exactly", "the R-symmetric sector's offset and mass", "-", "-", "NONE"),
  43: ("available because the three wall modes", "the kernel the three wall modes span", "-", "-", "NONE"),
  44: ("the three wall modes are one", "the kernel the three wall modes span", "-", "-", "NONE"),
  45: ("hence three chiral zero-modes", "the chiral zero-mode count", "-", "-", "NONE"),
  46: ("a circle whose action is what forces", "the equivariant Dirac index under a circle action", "-", "-", "NONE"),
  47: ("acts on the actual zero-modes", "the action induced on the zero-modes", "-", "-", "NONE"),
  48: ("complex conjugation of the pair", "the conjugation's action on the mode pair", "-", "-", "NONE"),
  49: ("does not act uniformly on the real", "the action on the real structure", "-", "-", "NONE"),
  50: ("binds exactly one normalizable", "the normalisable chiral zero-mode count at a wall", "-", "-", "NONE"),
  51: ("three throat walls, hence three", "the chiral zero-mode count against the wall count", "-", "-", "NONE"),
  52: ("three chiral generations carrying", "the generation count and its family symmetry", "-", "-", "NONE"),
  53: ("each contributes exactly one bound", "the bound-mode count per contributor", "-", "-", "NONE"),

  54: ("never form at any finite exterior", "exterior time to horizon formation", "bead_frames.py", "tau_of_r", "INPUTS"),
  55: ("never physically realised", "exterior time to horizon formation", "bead_frames.py", "tau_of_r", "INPUTS"),
  56: ("does not end as a thermal remnant", "the collapse's endpoint radius in proper time", "bead_conjugate.py", "r_of_tau", "INPUTS"),
  57: ("it does not arise, because the", "exterior time to horizon formation", "bead_frames.py", "tau_of_r", "INPUTS"),
  58: ("infinite tortoise distance", "the tortoise integral of 1/f to the horizon", "bead_contour.py", "f", "EXTEND"),
  59: ("the collapse does occur, at scale", "the collapse's endpoint radius in proper time", "bead_conjugate.py", "r_of_tau", "INPUTS"),
  60: ("seeded at the finite-curvature", "the curvature invariants at the seam", "beyond_the_wall/r7111_70_layer_geometry_audit/geometry.py", "curvature", "INPUTS"),
  61: ("the cosmology it seeds begins", "the scale factor's branch point in proper time", "bead_conjugate.py", "r_of_tau", "INPUTS"),
  62: ("there is no interval in which", "the crossing's duration in the observer's time", "bead_frames.py", "tau_r", "INPUTS"),

  63: ("The isotropy dimensions are", "the number of independent Killing fields", "beyond_the_wall/probe2.py", "killing_residual", "EXTEND"),
  64: ("\\mathrm{SO}(2,1)\\times", "the isometry algebra at the Nariai member", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "INPUTS"),
  65: ("not a continuous substrate", "whether the generator lies in the isometry algebra", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "INPUTS"),
  66: ("no such circle action and so no", "whether a U(1) lies in the isometry algebra", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "INPUTS"),
  67: ("isometry group being fixed by", "the isometry algebra of the absolute", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "INPUTS"),
  68: ("no such circle action and so no", "whether a U(1) lies in the isometry algebra", "beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py", "lie_g", "INPUTS"),
  69: ("being no isometry of the non-compact", "whether the Killing equation has a solution there", "beyond_the_wall/probe2.py", "killing_residual", "INPUTS"),

  70: ("doubly ruled by straight null", "the two ruling families of the substrate quadric", "synthesis_figure/panelA_reassign.py", "ruling", "INPUTS"),
  71: ("inherits both rulings", "which ruling families a slicing inherits", "synthesis_figure/panelA_reassign.py", "ruling", "INPUTS"),
  72: ("the substrate's null rulings are", "the shear of the ruling congruence", "beyond_the_wall/probe1.py", "Gamma", "EXTEND"),
  73: ("two ends of one hinge are timelike", "the causal separation of two hinge ends", "baryon_edge/L104w_the_excentre_trichotomy.py", "sep", "INPUTS"),
  74: ("two ends of one hinge are timelike", "the causal separation of two hinge ends", "baryon_edge/L104w_the_excentre_trichotomy.py", "sep", "INPUTS"),
  75: ("two ends of one hinge are timelike", "the causal separation of two hinge ends", "baryon_edge/L104w_the_excentre_trichotomy.py", "sep", "INPUTS"),
  76: ("The constant-$\\tau$ slice is exactly", "the intrinsic curvature of the constant-tau slice", "beyond_the_wall/r7111_70_layer_geometry_audit/geometry.py", "curvature", "INPUTS"),

  77: ("a $k$-independent correction", "the spectrum's envelope under a k-independent factor", "beyond_the_wall/ACOUSTIC_two_arm.py", "los_spectrum", "INPUTS"),
  78: ("The rate rule reaches the same", "the comoving distance by the two routes", "CR_acoustic_scale_and_hubble.py", "D_M", "INPUTS"),
  79: ("conflating them would manufacture", "the prediction the conflated rates give", "beyond_the_wall/ACOUSTIC_two_arm.py", "hier_run", "INPUTS"),
  80: ("the flatness of the distance slice", "the distance slice's curvature and the recovered expansion law", "CR_acoustic_scale_and_hubble.py", "D_M", "EXTEND"),
  81: ("the same flat-$\\Lambda$CDM observable", "the acoustic scale in multipole", "CR_acoustic_scale_and_hubble.py", "ell_A", "INPUTS"),

  82: ("a nearly scale-invariant adiabatic", "the processed spectrum from a scale-invariant input", "beyond_the_wall/L150a_the_collapse_leg_is_the_scale_invariant_one.py", "spectrum", "INPUTS"),
  83: ("The isotropy is earned on the", "the anisotropy amplitude along the approach", "beyond_the_wall/L150g_the_tensor_sector_and_the_interiors_adequacy.py", "P_T_of", "EXTEND"),
  84: ("a property of the progenitor's", "the anisotropy's dependence on the history against the crossing", "beyond_the_wall/L150g_the_tensor_sector_and_the_interiors_adequacy.py", "P_T_of", "EXTEND"),
  85: ("how much anisotropy survives", "surviving anisotropy against the leg's duration", "beyond_the_wall/L150g_the_tensor_sector_and_the_interiors_adequacy.py", "P_T_of", "EXTEND"),
}
