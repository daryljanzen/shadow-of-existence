> **⌖ RETIRED r1552.** This was closing the dynamic half (r322). **Landed:** P11 `dynamics_paper`.
> Kept as record; **do not work from it.**


# Closing the dynamic half — the "infinite-dim field-DOF completion" resolved
# Finding (c21, r322). Stated for reversal. Script: scripts/f1_smeared_fullleaf_closure.py
# A clarifying/consolidating closure: the apparent open tail dissolves; the genuine open frontier is elsewhere (quantum).

## What was carried as open
The standing line was: "the finite so(5,1) mode realization is complete; the remaining open F1 piece is the
infinite-dim field-DOF completion." Taken at face value this reads as a dangling computation on the dynamic half.
Read at source, it is not one open thing — it splits cleanly into two, and neither is a dangling open computation.

## The split
**(a) The smeared, infinite-dim HDA homomorphism FOR THE SYMMETRY-REDUCIBLE SECTOR — a corollary, now computed.**
The hypersurface-deformation bracket {H⊥[N],H⊥[M]} = Hₐ[hᵃᵇ(N∂_bM − M∂_bN)] has a **momentum-independent**
structure function: hᵃᵇ, the inverse leaf 3-metric (Dirac/DeWitt — universal GR, not CR-specific). Step 3 (r-only)
closed this for radial lapses; `f1_smeared_fullleaf_closure.py` completes it for **arbitrary lapses N(r,θ,φ)**:
the bracket closes on the full Hₐ, structure function the full inverse SdS leaf metric, with
- angular components hᶿᶿ=1/r², hᵠᵠ=1/(r²sin²θ): **M-invariant** (∂_M = 0) — the retained SO(3), matching steps 7–8;
- radial component hʳʳ=f: **carries the connection** (∂_M hʳʳ = −2/r) — matching steps 5–8;
- at M=0: hᵃᵇ = the de Sitter coset metric (constant → genuine Lie); off it it varies (genuine algebroid).
Because the structure function is the inverse metric — **a tensor field, momentum-independent** — the finite
isometry-mode identification (steps 1–9) already pins it; arbitrary smearing adds **no new CR content**. So the
smeared/infinite-dim homomorphism for the sector is a **corollary** of the finite-mode result, not a separate
open computation. (Consistent with Birkhoff: the symmetry-reducible sector has no local field DOF, so the
non-isometry smearings are pure gauge — nothing closes beyond the universal HDA + the coset identification of hᵃᵇ.)

**(b) The genuine field degrees of freedom — past the wall, and already classically closed (externally grounded).**
By Birkhoff there are no propagating DOF in the symmetry-reducible sector. The genuine field DOF (the graviton's
two polarizations) require non-spherical data — **past the wall** (isotropy→0, Type N), the Move-8 handoff to
dynamics. That sector is the Gowdy–dS propagating model, and its nonlinear future stability is **externally
grounded and already integrated into P9** (`dynamics_paper.tex` l.143): Friedrich 1986 (vacuum small-data
nonlinear stability of de Sitter = CR's perturbative graviton regime, settling in-regime all-orders ADMIT
directly), Andréasson–Ringström 2016 (all-data T³-Gowdy Λ>0 cosmic no-hair, Vlasov — corroboration),
Beyer 2009 (Nariai non-generic — the boundary CR already owns via P5). **The classical FORCE-vs-ADMIT closes
ADMIT for generic data, Nariai the non-generic boundary.** The earlier "not claimed both ways" framing was
**superseded** by this grounding (dynamics_frontier_gowdy-dS_canonical.md §after-13).

## Net — the dynamic half is closed at honest weight
There is **no dangling infinite-dim algebroid computation**. The "infinite-dim field-DOF completion" was: (a) a
corollary for the sector (the structure function is the inverse metric, pinned by the finite modes — now computed
for arbitrary smearing), plus (b) the genuine field DOF, which are the externally-grounded classical dynamics
already in P9. Both closed.

## The honest residual caveat (held, not a dangling computation)
P9 grounds the classical no-hair on a **convergence of results** (vacuum small-data Friedrich + all-data Gowdy
Vlasov Andréasson–Ringström + vacuum Nariai-genericity Beyer), **not** a single named theorem for the exact
vacuum polarized Gowdy–Λ all-data case; the reduction's global/topological hypotheses are taken as in-class.
This is a rigor caveat, honestly held in P9, not an open computation.

## What IS genuinely open is NOT the dynamic half
The remaining open frontier is the **quantum forcing** — does the nonlinear Λ>0 back-reaction *force* quantum
structure via the S₃/A₂ discrete skeleton (Move 13), or only *admit* it? That is **not claimed**, the priority
reach, and it is the **lock/QG frontier** (the one the lock seeds), not the dynamic half. **Not touched here, and
not to be force-closed.**

## Staged (NOT raced) — the P10 scope sentence
P10 (`algebroid_paper.tex` l.135) flags the full field-theoretic homomorphism as "Open (the natural extension)…
flagged, not claimed." Given the above, this is now slightly **under-claimed for the sector** (it is a corollary,
computed) and the "across all of C beyond the per-stratum pattern" conflates the sector-corollary with the
past-the-wall dynamics. A sharpening is available: the smeared closure is established for the symmetry-reducible
sector; the genuine field DOF are past the wall = the externally-grounded classical dynamics. **This is a
canonical (precious-tier) edit — it rides its own fresh cold read, not raced.** Proposed, stated for reversal.
