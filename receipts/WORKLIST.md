# RECEIPT SEQUENCING WORKLIST — living, maintained every turn (Arthur)
*The order of receipt work across the corpus, and what each delivers. Emerges pass by pass like P14's L1–L10 —
not known in full in advance. Maintained every turn; no closure pressure. Companion to `INDEX.md` (the ledger)
and `../AVENUE_11_SWEEP_PLAN.md` (the procedure). Status: ✔✔ verified · ◐ partial · ✗ broken · ? unclear · ∅ missing · ⏳ to-verify (cited, exists, not yet traced+run) · ⬚ to-build.*

## SEQUENCING (current)
P1–P12 ✔ COMPLETE. P13 IN PROGRESS.
### P13 — boundary_paper (geometric-isometry boundary; 0 equations, heavily conceptual)
- `P13_A3_factorization.py` — ✔✔ (charge conjugation factorises C=(Q->-Q)_field o (R o K)_geometric; R o K blind to sign(Q); existing storyboard receipt, verified).
- `P13_conjugation_parity.py` — ✔✔ (R=gamma^5 grades chirality; R!=P). `P13_ruling_swaps.py` — ✔✔ (R swaps null rulings, generic).
- `P13_closure_i_check.py` — ✔✔ (3bar=R(3), 3-link chain; FLAGS owed A2-specificity clause -- see NOTES_owed_clause.md). `P13_closure_iv_check.py` — ✔✔ (R fixes r=0 = branch point; asymmetry is the content).
- ✅ **P13 boundary_paper COMPLETE (r1383)** -- 10 receipts, coverage audit closed (prop:boundary/conj-parity/conj-closure/closure i-iv/sigma/cascade/synthesis/Kretschmann). sigma_lift ✔✔ NEW (boost->rotation clincher). DOC FINDING open for Daryl: prop:closure(i) A2-specificity clause.
- ◐ **P14 matter_sector_paper IN PROGRESS (r1384-)** -- 2 propositions (prop:wall, prop:forced), boxed "generations=3". Cites 6 receipts informally.
  - `P14_B3_spinor_vielbein.py` ✔✔ (prop:wall: M!=0 tetrad->Cartan->W=lambda sqrt f/r, P13's deferred superpotential derived).
  - `P14_B2_zeromode_continuation.py` ✔✔ (zero-mode bound->propagating across horizon; three walls -> three families; chirality intact).
  - `L8_the_three/two/twelve` ✔✔ (family counting 3/2/12), `P14_payoff` ✔✔ (A3->zero-modes), `dual_norm` ✔✔ NEW (leaf vs conserved-Dirac norm). P14 has 7 receipts.
  - ✔ P14 COMPLETE (r1387): final audit caught the compact-leaf index claim (leaf_compactness ✔✔ NEW). 8 receipts. prop:forced is a structural argument (no arbitrary modulus <=> maximal symmetry), rests on receipted prop:wall + L8_the_three.
- ⬚ THEN: P15 CR_cosmology, P16 cosmogenesis_paper, p0/17 geometric_core_paper.
- **DOC FINDING for Daryl:** prop:closure(i) owed a clause on A2-specificity (-1 not Weyl) -- non-blocking.
### P12 — algebroid_paper ✔ COMPLETE (cited nothing → 2 computational receipts)
- bracket_closure (prop:closure = Dirac algebra), coset_metric (structure function = Lorentzian coset metric, sig (1,4)).
- sec:anchor (ADM mapping; lapse-split -> P8; homomorphism = prop:closure), sec:isotropy/sec:discrete structural. L183 intro roadmap. Zero uncovered.

### P11 — dynamics_paper ✔ COMPLETE (cited nothing → 5 computational receipts)
- gowdy_dS (4 field eqns), twoKV (2 Killing vectors), deSitter_attractor (shear charge), mukhanov (massless mode), wall_ppwave (prop:wall + chirality).
- sec:discrete/relation/scope conceptual. Coverage audit: L159 abstract roadmap, L264/L272 = wall/chirality (covered). Zero uncovered.

### P10 — canonical_time ✔ COMPLETE (mostly conceptual; 2 computational receipts)
- minisuperspace_friedmann (sec:deparam), graviton_lift (sec:lock). Rest conceptual (problem-of-time argument). Zero uncovered.

- ⬚ thm:bound (so(4,1) symmetry bound) NEXT · ? assess thm:range / cor:wall / cor:radiation (likely structural).
### P8 — slicing_operator ✔ COMPLETE (cited NOTHING → 7 claims, 5 receipts built)
- matter_functional (covers 3), lapse_split, E1_cosmology (+HEB handover), trichotomy, synchronous_horosphere.
- Coverage audit done: both "direct computation" sites receipted; sec:ontology/dictionary/open analytic. Zero uncovered. **NEXT: build the in-place receipt-citation system** (unobtrusive \rcpt{key} macro + INDEX-driven generated 'Appendix R', retrofit comprehensively on P1–P3), THEN P4→P14 in order, then P15–P16. Cross-paper receipts verified once, reused
(noted). Papers citing no receipts (P2,P4,P6,P10,P11,P12) need enumeration first — their claims are likely ⬚.
Head start from the P14 sweep: several cited receipts already classified (below) — fold them into `receipts/` as
each owning paper comes up.

## CARRIED FROM THE P14 SWEEP (already classified in THE_RECEIPT_AUDIT.md — migrate into receipts/P14 + shared/)
- `A3_spinor_lift.py` — ✔✔ (C-operator R∘K=charge-conj, 3 ways). Cited by **P13 + P14** → `shared/`.
- `even_crossing_index.py` — ✔✔ (count=3 mechanism; index resolved). P14.
- `R_gamma5_Cl_derivation.py`, `R_ruling_swap_6D.py` — ✔✔ built (chirality=γ⁵ from scratch + 6D). P14.
- `family_S3_is_weyl.py` — ✔ (Weyl(A₂)=S₃ + forced degeneracy; designation traced). P14.
- `two_factors_direct.py` — ✔ (Aut(A₂)=S₃×ℤ₂ direct; −1∉W(A₂) contingency). P14; **covers P5's `negation_outer_A2` claim** → check/merge.
- `L8_the_three/_two/_twelve.py` — ✔ exemplary (§212 numerals). P14.
- `B3_sphere_spectrum.py` — ✔ built (λ=j+1/2 from edth). P14.
- `B2_zeromode_continuation.py` — ◐ (computes reality-transition; a^{-3/2} now derived separately). P14.
- `B3_spinor_vielbein.py` — ◐ (W=λ√f/r traced; its own "W matches" check tautological, no γ⁵). P14.
- `conjugation_parity.py` — ✗ TAUTOLOGY (`comm(g5,g5)`; cited r703 receipt not found). Cited by **P13** → the geometric-R=γ⁵ claim is carried by the from-scratch build instead; **P13 citation needs review**.
- `A3_factorization.py`, `P14_payoff.py` — ⏳ to-verify (cited P13/P14/p0).

## PER-PAPER RECEIPT LISTS

### P1 — BH_causality ✔ AT BAR
- `P01_metric_singularity_algebra.py` — ✔✔ (§3 horizon coeff→0 all charts; |ζ|², g^rr vanish; derived).

### P2 — janzen_circle *(none cited — 6-claim inventory in CLAIMS.md)*
- `P02_cycloid_and_critical_points.py` — ✔✔ (cycloid solves radial eq; 2 critical points = circle r-poles).
- `P02_kretschmann_chain_rule.py` — ✔✔ (K-divergence = chart-labelling artefact; 12th-order pole = 2×6; label swap moves it to the horizon).
- `P02_analytic_continuations.py` — ✔✔ (Region I recovers Schwarzschild exterior; back-seam onto r<0).
- `P02_ring_lambda_limit.py` — ✔✔ (single horizon = Λ→0 limit of SdS root triple; three zero-sum roots).
- **P2 at bar** (4 receipts cover all verifiable claims).

### P3 — SdS_slicing *(3 cited + figure-math)* — IN PROGRESS
- `one_thirty.py` — ✔✔ (§488: the 30°s are one via triple-angle; minimality via Rule 2, stated). Canonicalized.
- `euclid7_nine_point.py` — ✔✔ (nine-point circle = throat; falsifier rejects all but 2α; self-correcting).
- `alpha_alone.py` — ✔✔ (α alone sets the construction; strengthened with asserts + tangency control).
- **All 3 cited P3 receipts verified.** Built: `P03_cubic_factor_ellipse_locus.py` ✔✔ (factorisation + ellipse eigenstructure + σ involution + reflection).
- Built: `P03_triple_angle_gnomonic.py` ✔✔ (r₀=(2/√3)sin w ⇒ 2M pure sin 3w, 2/√3 unique; Nariai=σ fixed point).
- Built: `P03_seam_continuation.py` ✔✔, `P03_curvature_signflip.py` ✔✔ (K_G sign-flip + MS/Komar mass).
- Built: `P03_overcritical.py` ✔✔. **P3 AT BAR** (8 claims: 3 cited verified + 5 built).

### P4 — modern_parallax *(none cited — ENUMERATE)*  ⬚  (the redshift-isotropy datum — likely an empirical/data claim)
### P5 — groupoid — IN PROGRESS
- `negation_outer_A2.py` — ✔✔ (R negates roots→conjugates 3↔3̄ iff −1∉W(A2); others=controls). Cited (converted inline→\rcpt). Distinct from P14 two_factors_direct (shared −1∉W(A2) core, kept self-contained — NO merge).
- `P05_deck_group_S3.py` — ✔✔ (Nariai monodromies=transpositions → deck S3 = Galois group; +D6 assembly). Cited at prop:deck.
- **P5 computational core AT BAR** (2 receipts). Rigidity/single-reassignment = analytic.
### P6 — shadow ✔ AT BAR (analytic — NO computational receipts)
- 0 equations; the imperative/rules/least-arbitrariness/modal-fallacy/reflexive-closure are analytic. The '~8%' is a forward-ref to P15 (damping_tail). Confirmed nothing to verify — recorded, not skipped.
### P7 — CR_framework *(6 cited)* — IN PROGRESS
- `photon_cross_test.py` — ✔✔ (signed r real/odd through seam; photon crosses bounded; strengthened). Cited (inline→\rcpt).
- `bead_conjugate.py` — ✔✔ (conjugate legs/Schwarz, e^{2pi i/3} period, pi/3 turnaround). Cited.
- `bead_contour.py` — ✔✔ (bounded tau~-contour: real/imag/locked-pi3; A-independent; control vs 2pi). Cited.
- `order3_bridge.py` — ✔✔ (scope corrected r1430: groupoid Z/3 vs bead Z/3 are different cubics and NO AFFINE map identifies their root sets; stage 5 exhibits the E-family that does join them, with a control. Identification of root sets remains do-not-assert). Cited.
- `F_flat.py` — ✔✔ (exact arc length, perpendicular legs, monotonic, tangents). Cited.
- **All 5 P7 physics receipts ✔✔; depmatrix = meta (runs).** **P7 COMPLETE — no missing receipts (full coverage audit done r1358: non-bead theorems all analytic, HEB references P3).**
### P8 — slicing_operator
- `foci_ruling_2sqrt3.py` ⏳ (the ellipse foci at ±2/√3)
### P9 — range
- `matter_functionals_C9.py` ⏳
### P10 — canonical_time *(none cited — ENUMERATE)* ⬚
### P11 — dynamics *(none cited — ENUMERATE)* ⬚
### P12 — algebroid *(none cited — ENUMERATE; the D₆/Aut(A₂) may reuse two_factors_direct)* ⬚
### P13 — boundary *(8 cited)*
- `A3_spinor_lift.py` ✔✔ (shared) · `A3_factorization.py` ⏳ · `conjugation_parity.py` ✗ (review citation) · `ruling_swaps.py` ⏳ · `qm_S4_vs_S5.py` ⏳ · `kretschmann_bead.py` ⏳ · `closure_i_check.py` ⏳ · `closure_iv_check.py` ⏳
### P14 — matter_sector *(mostly done in the sweep — see carried list; migrate into receipts/P14)*
### p0/17 — geometric_core *(4 cited)*
- `P14_payoff.py` ⏳ · `power_of_a_point.py` ⏳ · `power_is_null.py` ⏳ · `qm_S4_vs_S5.py` ⏳ (shared w/ P13)

## RECEIPT-CITATION SYSTEM (built r1345)
- `corpus/receipts.sty` — `\rcpt{key}` macro; unobtrusive superscript R, links to Appendix R via hyperref (key = receipt filename stem).
- `corpus/make_receipt_appendix.py` — generates "Appendix R" from `receipts/INDEX.md` (`P#`|`corpus` scope). Single source of truth; two-phase ASCII+unicode escaper.
- `corpus/check_receipts.py` — gate: every `\rcpt{}` resolves to an INDEX row + a file on disk; lists uncited receipts (retrofit to-do).
- INDEX convention: escape literal math bars as `\|` (markdown-table safe).
- **P1+P2+P3 fully wired** (13 markers, per-paper + corpus appendices, all 0/0). Checker: 13/13 PASS, 0 uncited. **Retrofit complete.** From P4: cite-in-place as each receipt is built (plan step G2).

## TERMINOLOGY CONVENTION (r1355, Daryl-directed) — load-bearing
- **"turnaround"** is RESERVED for the analytic bead/cosmogenesis location: the comoving turnaround r=-(2Mα²)^⅓ (1-f=0, |Im τ̃|=π/3), the collapse→expansion turning point. Keep.
- The cosmological structure-boundary r⋆=(Mα²)^⅓ (local gravitational hold ↔ cosmic expansion, the flat locus K_G=0) is the **Hubble–Eddington radius** — NEVER "turnaround radius". Credited to Eddington, *The Expanding Universe* (1933) `\cite{Eddington1933}` at first mention (the corpus already cites Eddington 1933 in p0). Tomaras (`PavlidouTomaras2014`) kept for the EMPIRICAL TEST only, not the name/characterization.
- Applied across P3/P6/P8/p0/P7/P15; P7 label sec:CR-turnaround→sec:CR-HEradius. Any NEW use of the structure boundary must say "Hubble–Eddington radius".

## RUNNING NOTES (tighten each turn)
- r1334: worklist opened. P1 at bar. cross-paper receipts noted for `shared/`.
- r1334: P2 enumerated (6 claims); cycloid+critical ✔✔, Kretschmann artefact ✔✔.
- r1335: fixed revision/bundle discipline. P2 continuations ✔✔.
- r1336: P2 ring ✔✔ → P2 at bar.
- r1337: P3 begun — one_thirty.py ✔✔.
- r1338: euclid7_nine_point.py ✔✔.
- r1339: alpha_alone.py ✔✔. All 3 cited P3 receipts done.
- r1340: P03_cubic_factor_ellipse_locus.py ✔✔.
- r1341: P03_triple_angle_gnomonic.py ✔✔.
- r1342: P03_seam_continuation.py ✔✔.
- r1343: P03_curvature_signflip.py ✔✔.
- r1344: P03_overcritical.py ✔✔ → P3 AT BAR.
- r1345: BUILT the citation system; wired P1.
- r1346: retrofitted P2 (4 markers).
- r1347: P1–P3 citation retrofit COMPLETE.
- r1348: P4 built + cited (floor ✔✔). P4 AT BAR.
- r1349: P5 negation_outer_A2 ✔✔.
- r1350: P5 deck_group_S3 ✔✔. P5 core AT BAR.
- r1351: P6 analytic, no receipts.
- r1352: P7 photon_cross_test ✔✔.
- r1353: P7 bead_conjugate ✔✔.
- r1354: P7 bead_contour ✔✔ (bounded contour, A-independent pi/3 lock; added a column-count lint to check_receipts). 19/19 PASS.
- r1356: P7 order3_bridge ✔✔.
- r1357: P7 F_flat ✔✔.
- r1358: P7 COMPLETE (completeness audit).
- r1359: P8 opened; P08_matter_functional ✔✔ (covers 3).
- r1360: P8 lapse-split ✔✔.
- r1361: P8 E=1-cosmology ✔✔.
- r1362: P8 trichotomy ✔✔; caught uncovered synchronous computation.
- r1363: P8 COMPLETE (7 claims, 5 receipts).
- r1364: P9 opened; ppwave_typeN ✔✔.
- r1365: P9 bianchiI_typeI ✔✔.
- r1366: P9 kerr_deSitter ✔✔.
- r1367: P9 typeD_quartics ✔✔.
- r1368: P9 carter_killing ✔✔.
- r1369: P9 COMPLETE (6 receipts + structural).
- r1370: P10 opened; minisuperspace_friedmann ✔✔.
- r1371: P10 COMPLETE (2 receipts + conceptual).
- r1372: P11 opened; gowdy_dS ✔✔.
- r1373: P11 twoKV ✔✔.
- r1374: P11 deSitter_attractor ✔✔.
- r1375: P11 mukhanov ✔✔.
- r1376: P11 COMPLETE (5 receipts).
- r1377: P12 opened; bracket_closure ✔✔.
- r1378: P12 COMPLETE (2 receipts).
- r1379: P13 opened; A3_factorization ✔✔.
- r1380: P13 conjugation_parity + ruling_swaps ✔✔.
- r1381: P13 closure_i/iv_check ✔✔. Found owed-clause (prop:closure i A2-specificity).
- r1382: P13 A3_spinor_lift+kretschmann_bead+qm_S4_vs_S5+cascade_rank ✔✔.
- r1383: P13 sigma_lift ✔✔; **P13 COMPLETE (10 receipts)**.
- r1384: P14 OPENED. B3+B2 ✔✔.
- r1385: P14 L8_* + P14_payoff + dual_norm ✔✔. 58/58 PASS.
- r1387: P14 COMPLETE — final audit + leaf_compactness ✔✔ NEW (compact leaf => well-defined index). 8 P14 receipts. Corpus 17/17. PAUSED before P15 per Daryl.
- r1386: FOLDED IN 7 verified receipts from the r1364j fork (P02_interior_metric, P03_charge_parity/conjugacy/ellipse_foci, P05_dihedral_generators, P07_nariai_selection/sds_kretschmann) -- all derive from primitives, all ✔✔, all new coverage. Hit + fixed the appendix-filename-padding bug (see rule above). Corpus 17/17 compiles, checker green, ~65 receipts. NEXT: P14 final audit -> complete; then P15.
## ⚠ APPENDIX FILENAME RULE (learned r1386, cost a long debug)
Single-digit papers INPUT zero-padded appendix filenames: P1->appendix_receipts_P01, P2->P02, ... P9->P09
(verify per paper via `grep 'input{appendix' <paper>.tex`). The generator's SCOPE arg is NON-padded and must
match the INDEX "paper" column (P1,P2,...), but the OUTPUT filename must be zero-padded:
    python3 make_receipt_appendix.py P3 appendix_receipts_P03.tex   # scope P3, file P03
Writing to appendix_receipts_P3.tex is a silent no-op (paper never sees it -> \rcpt undefined). And regenerating
by scanning existing filenames (sc from P0X) passes a NON-matching scope P0X -> EMPTY appendix -> empty
description env -> COMPILE ERROR. 2-digit papers (P10-P14) need no padding. corpus.tex scope = corpus.


- r1355: **TERMINOLOGY FIX DONE** — structure-boundary renamed "maximum turnaround radius"→"Hubble–Eddington radius" across P3/P6/P8/p0/P7/P15 (7 phrase renames), Eddington1933 credited at first mention (corpus already cited it in p0), Tomaras kept for the empirical test, P7 label renamed; all 6 compile 0/0, 19/19 receipts still PASS. "turnaround" now bead-only.
- NEXT: resume P7 sweep — order3_bridge.py. (superseded PAUSE note:) terminology fix — "turnaround" is RESERVED for the analytic bead location (r=-A); it is being MISUSED for the Hubble-flow boundary (the cosmological max-turnaround radius r*) in P3/P6/P8/p0/others. Audit all "turnaround" uses, rename the Hubble-flow-boundary sense (candidate: "Hubble bound" if free), keep the bead sense. THEN resume P7 order3_bridge.
- NOTE: the Euclid-protocol family (power_is_null, euclid3/4/5/6, U5_excircles) supports §488's other equivalences — cited by P3/p0; verify as their papers come up (power_is_null + power_of_a_point are p0-cited too).
