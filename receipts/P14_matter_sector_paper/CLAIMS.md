# P14 matter_sector_paper — CLAIMS ledger

The fermion / matter sector. 2 propositions (prop:wall, prop:forced), 4 numbered eqns, boxed "generations = 3".
P13's gamma^5 / A3_spinor_lift forward-reference this paper.

## Receipts (in progress, r1384-)
- `P14_B3_spinor_vielbein.py` ✔✔ (prop:wall) — M!=0 tetrad -> Cartan -> spin connection -> W=lambda sqrt(f)/r (P13's deferred superpotential, derived); W=0 at horizons, odd in signed r = domain wall.
- `P14_B2_zeromode_continuation.py` ✔✔ (zero-mode continuation) — chiral zero-mode bound (f>0) -> propagating (f<0) across horizon; maps onto E=1 sinh^{2/3} expanding-leaf Dirac; chirality intact; three wall-modes -> three families.

- `P14_L8_the_three.py` ✔✔ (sec:family — THE 3: hinges=roots, same cubic, forced).
- `P14_L8_the_two.py` ✔✔ (sec:twofactors — THE 2: ruling/parity/automorphism = one 2 [A:YES]; horns' 2 distinct [B:NO, counterexample]).
- `P14_L8_the_twelve.py` ✔✔ (sec:family — THE 12 = |D_6|, forced by dihedral structure).
- `P14_P14_payoff.py` ✔✔ (sec:cosmogenesis — A3's R o K lands on P14's zero-modes: sigma_y=+/-1, normalizability, chirality flip).
- `P14_dual_norm.py` ✔✔ NEW (prop:wall — dual-norm: leaf-normalizable, NOT conserved-Dirac-normalizable; tortoise measure log-diverges at horizon).
- CROSS-REF: L224 A3_spinor_lift (P13 receipt) stays informal \texttt (cross-paper label).

- `P14_leaf_compactness.py` ✔✔ NEW (sec:count index claim — leaf compact in dl=dr/sqrt|f|: finite proper length, integrable sqrt-singularities at horizons and r=0, vs tortoise pole that diverges => well-defined Dirac index, cites Atiyah-Singer).

## STATUS: P14 COMPLETE (r1387). 8 receipts, all ✔✔ cited-in-place, compiles 0/0/12pp, checker green.
Coverage audit done: both propositions (wall, forced), all 4 numbered eqns, the compact-leaf/well-defined-index argument, all 7 sections. Final-audit catch = leaf_compactness (the body's finite-leaf-length/compact-leaf claim behind the Atiyah-Singer index invocation was unreceipted; distinct measure dr/sqrt|f| from dual_norm's flat-vs-tortoise contrast).

## Key claims
- prop:wall: each throat wall binds exactly ONE normalizable chiral zero-mode; chirality = definite sigma_y eigenvalue (sign = sign of signature/wall). Z_2 chirality realised as bound state.
- sec:count: single wall at r=0 (on the throat circle); three hinges (radius 2alpha, polar 0/120/240) -> three r=0 walls.
- prop:forced: the three-plane construction is FORCED within CR (one-plane needs an arbitrary hinge choice); rests on maximal symmetry. => number of chiral generations = 3 (boxed).
- sec:family: family symmetry (L8_the_three/two/twelve).
