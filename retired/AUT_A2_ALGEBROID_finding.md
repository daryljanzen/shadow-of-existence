> **⌖ RETIRED r1552.** This was the Aut(A₂) cover and the algebroid connection (r321). **Landed:** P5 gives Aut(A₂)=S₃×ℤ₂≅D₆; P12 is the algebroid paper.
> Kept as record; **do not work from it.**


# The Aut(A₂) cover and the algebroid connection: independent structures, not one object
# Finding (c21, r320–r321). A clarifying NEGATIVE result. Stated for reversal.
# Scripts: scripts/{nariai_connection_character, nariai_leak_order, nariai_leak_order2, knds_branch_vs_connection}.py

## The question
P4 (`groupoid_paper`) gives the same-α between-member morphisms as the deck transformations of the horizon
cubic's three-sheeted cover, branched at Nariai, monodromy the root-exchange σ — a **discrete** structure.
P10 (`algebroid_paper`) gives the algebroid **connection** (the 𝔪-component of [𝔪,𝔪], the symmetric-space
grading failure), vanishing at the symmetric strata {Type O, Nariai} — a **continuous** structure. Both single
out Nariai (P10 l.124 already notes "the isotropy-jump locus *is* the metric-degenerate locus there"). The
question: are they two faces of **one object** (the branched-cover base with the connection downstairs and the
deck/ramification upstairs), tied at Nariai? Equivalently, is the meeting at Nariai deep or shallow?

## Finding 1 — analytically distinct (the connection does NOT carry the ramification)
The cleanest test was the order of the connection's vanishing at Nariai: branch-type √(M_N−M) (carries the
cover's ramification) or analytic (M_N−M)?
- **The connection is analytic in the modulus M.** The off-symmetric leak the corpus computes
  (`f1_offsymmetric_mode_leak.py`) is a *rational* function of M (carries a factor M, vanishes linearly at
  Type O, no feature at M_N) — because the metric f = 1−2M/ρ−ρ² is rational in M, so any leak built from it by
  Lie brackets is too. The curvature-mismatch measure D = R₂−R_{S²} at the throat centre is exactly
  D(r_N,M) = −12√3·(M_N−M): **linear, analytic.**
- **The cover is ramified √(M_N−M).** The two colliding horizon roots split as ±√(M_N−M) (double root /
  discriminant zero at Nariai). This √ lives **only** in the offset↔modulus map u↦M=½(u−u³), i.e. in the
  *cover* (the space of descriptions), **not** in the connection (a function on the *geometries*).
So the cover and the connection are **co-located at Nariai but analytically distinct**: the cover multivalued
(√-ramified) over the modulus, the connection single-valued analytic over the modulus. Not one analytic object.
(Caveat, not load-bearing: the exact zero-order of the connection at the near-horizon Nariai member was
evaluation-dependent in the geometric proxy — needs the algebraic so(5,1) leak for a unique number — but it
cannot reintroduce a √, since the leak is rational in M.)

## Finding 2 — the locus-coincidence is SPHERICAL-SPECIAL, not general (refutes the unification)
Conjecture tested in the richer CR vacuum moduli space: is every branch point (degenerate horizon) a
connection-zero (symmetric stratum), via "degenerate horizon → maximally-symmetric near-horizon → symmetric
isotropy"? Tested at **extremal Kerr–de Sitter** (a genuine Λ-vacuum stratum, P10 Type D; its horizon function
Δ_r is a quartic whose discriminant gives a real degenerate-horizon/branch locus). Run through P10's own grading
test (`knds_branch_vs_connection.py`):
- **SdS Nariai** SO(2,1)×SO(3), **dim 6**: [𝔪,𝔪]⊆𝔥 → **SYMMETRIC, connection zero.** ✓ (branch + spherical)
- **Extremal Kerr-dS** SO(2,1)×SO(2), **dim 4**: [𝔪,𝔪]⊄𝔥 → **NON-symmetric, connection nonzero.** ✗ (branch + rotating)
The symmetric-pair isotropy dimensions of so(5,1) are **{6,7,10}** (enumerated; matches P10). Dim 6 (Nariai) is in
it; **dim 4 (extremal Kerr-dS) is not.** So extremal Kerr-dS is a **branch point that is NOT a connection-zero**.

**Why:** a degenerate horizon enhances the (t,r) sector ℝ→SO(2,1) (+2 generators, the near-horizon dS₂/AdS₂).
Whether it lands on a symmetric stratum depends on the angular factor: spherical SO(3) (dim 3) + SO(2,1) (dim 3)
= **6**, a symmetric dimension; rotation breaks SO(3)→SO(2), giving SO(2) (dim 1) + SO(2,1) (dim 3) = **4**, below
the symmetric threshold. So the SdS-Nariai coincidence is a **numerical accident**: spherical symmetry's SO(3)
exactly fills out a symmetric-pair dimension of so(5,1). (Confirming heuristic, not a CR vacuum cut: charged RNdS
keeps SO(3), so its degenerate horizons give SO(2,1)×SO(3) dim 6 again and the coincidence survives — it is the
angular symmetry that carries it, not the matter.)

## Verdict (stated for reversal)
**P4's discrete cover and P10's connection are independent structures on the cut space.** They are analytically
distinct (Finding 1) and even their one locus-coincidence (SdS-Nariai) is special to spherical symmetry and does
**not** generalize (Finding 2). The "meeting at Nariai" both papers note is **real but shallow** — a
spherical-sector artifact, not a P4↔P10 bridge. **Do not re-chase the unification** as a deep correspondence;
read the discrete classification (P4) and the connection (P10) as separate structures, their SdS overlap noted
as the special case it is.

## What this touches in the corpus
**Nothing precious is forced.** No canonical paper changes. *Optional, the cold reader's call:* a one-line remark
in P10 §strata that the Nariai isotropy-jump↔metric-degenerate coincidence (l.124) is **spherical-special** —
the dimension match SO(2,1)×SO(3)=6 ∈ {6,7,10} is what makes it a symmetric stratum, and it fails under rotation
(extremal Kerr-dS, SO(2,1)×SO(2), dim 4). This is a clarifying caveat, not a correction. Being a negative result,
it does not require a gated cold read — a sanity check in passing suffices.
