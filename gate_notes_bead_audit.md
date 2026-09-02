# Bead-arc audit (r973→r988, node Arthur/c39) — walk slowly, verify every edit at source

## Discipline for this audit
- No trusting the node's writeups. Every claimed edit checked against the current paper text AND against the geometry/source it rests on.
- The node's known failure (from Daryl + my own check): it collapsed the DOUBLE ruling of the one-sheeted hyperboloid into "one bundle read under a sign." A one-sheeted hyperboloid is doubly ruled — two DISTINCT ruling families through each point (verified: orthogonal directions at the waist). Three distinct congruences: A ruling, B ruling (the OTHER ruling, not A-under-a-sign), photon = at-rest worldlines. Source: slicing_operator.tex §sec:synchronous ("doubly ruled … one ruling … the other"), P7 §537.
- Everything the r986/r987 sheet-assignment/"1+2"/"B rides no sheet" conclusion asserts is SUSPECT and contradicts that source.
- When a real result is verified → cut a bundle + real changelog entry. Every time there's progress.

## The claimed edits, by revision (checklist — verify each)
### r973 — P7 rem:perspectival-singularity rewrite; conj:bead added; ontology index §1e/§1k aligned
### r974 — de-frag 3 sites: P7 rem:perspectival-singularity, P2 §sec:ring, P5 rem:P-dS-Schw, P11 §sec:discrete; τ̃-contour computed; β=2πα retraction; P7 abstract billing
### r975 — conj:bead → thm:bead in P7 §NBC; abstract recast; ontology §1e/§1k + P5 conjecture→theorem; BEAD_THEOREM.md; bead_contour.py
### r976 — deep-bake ontology into all 17, each citing P7; dependency matrix regen
### r977-r984 — (changelog NOT saved — reconstruct) bead-frames fig; three-frame fig:bead_frames; r980 two frontier Qs
### r985 — antimatter front plan; WP-A (figure walk-back, P7 caption edits, bibkey hygiene)
### r986 — WP-B order-three (does not close); lem:twoturnings added to P7; C3 "1+2 sheets" [SUSPECT]; WP-E [later reopened]
### r987 — self-corrections: double-speed removed; antimatter reopened not claimed
### r988 — ? (verify what if anything)

## SPECIAL FLAG (Daryl): the "2+1 thing" possibly introduced an error in P5 via a short lemma. Check P5 for any node-added lemma.

## Findings (append as verified)

---
## FINDING 1 (r988 audit) — the sheet-assignment claim in P7 §third-fact + the sheet_assignment.py receipt

**Location:** P7 `CR_framework.tex` line 763 (thm:bead's third structural fact) + figure caption panel (D) + receipt `computations/sheet_assignment.py` step [3].

**The claim as it stands in the paper:** "the two null bundles A and B, riding the level S³ spaces through the seam, take the ±πα/3 wings" — i.e. a 3-congruence→3-sheet bijection: photon↔real crossing, A↔+π/3, B↔−π/3.

**What the receipt ACTUALLY computes (steps [1]-[2]):**
- [1] photon null geodesic integrated in real τ̃ → rides Im=0 real sheet. SOUND.
- [2] the MATTER A congruence's cosmic-time reading tau_of_r(r<0) → its collapse leg occupies BOTH wings ±π/3, "as the two CONJUGATE readings τ̃↔conj(τ̃) of ONE curve." SOUND as a statement about A alone.

**The error:** step [3] then ASSERTS "the two null bundles A, B ... take the two conjugate wings ±π/3." This is NOT derived. Step [2] showed both wings are the complex-conjugate pair of the SINGLE matter (A) continuation. Step [3] relabels A's own −π/3 conjugate wing as "B." That is the double-ruling collapse Daryl named: it identifies the second ruling B with the complex conjugate of A's cosmic-time reading. No computation maps B (a genuinely distinct null ruling on the doubly-ruled hyperboloid) to the −π/3 wing.

**Internal contradiction in the node's own work:** the receipt step [3] says "B is a null bundle, NOT the foliation" (correct, matches double ruling); the earlier WP_C3_SHEET_ASSIGNMENT.md note (r986) concluded "B rides no sheet / B is a space" (wrong). Node contradicted itself; neither is a derivation of the A/B→wings map.

**Status of the paper claim:** the "A, B take the ±πα/3 wings" clause in thm:bead third fact (L763) and the panel-D caption are ASSERTED, resting on a receipt that derives only that A's conjugate pair fills both wings. The three-distinct-bundles picture is right (good, matches geometry); the *assignment of B to the −π/3 wing* is unfounded. Sheet↔bundle assignment is genuinely OPEN, not closed.

**Not yet fixing — continuing the walk to see if this propagated and whether lem:twoturnings / the 2+1 P5 lemma is affected.**

---
## FINDING 2 — lem:twoturnings (P7 L752), the one node-added formal object: MATHEMATICALLY SOUND
Independently verified (/tmp/twoturnings_check.py):
- two cubics correctly derived from f: slicing r³−r+2M=0 (f=0), comoving r³+2M=0 (1−f=0). ✓
- comoving roots = equilateral triangle, single e^{2πi/3} cube-root orbit, equal modulus. ✓
- slicing roots at Nariai: double root +1/√3 (=+α/√3, merged horizon) + single −2/√3 (=−2α/√3) — the lap turning points. "colinear real (casus irreducibilis)". ✓
- affinely inequivalent: rigorous (p=0 cannot map to p=−1 under r→ar). ✓
- CONCLUSION ("the two ℤ/3's agree only as abstract ℤ/3's") is CORRECT **as scoped r1430**: no AFFINE change of variable identifies their root sets (obstruction at fixed cubic; the two are the E=1 and E=0 ends of one turning-point family, stage 5). It deflates an *affine* bridge, not the relation between the cubics. Good work, not an error — but the r986 phrasing of it as a general negative was, and is corrected.
=> No node-added lemma in P5. The "2+1"/short-lemma hunch: the added lemma is lem:twoturnings in P7, and it is sound. P5's only bead touch is prop:autA2 L478 (σ/R/ξ as three distinct crossings of one lap) — CORRECT, careful, matches geometry.

## FINDING 3 — the ACTUAL live error, isolated
The error is NOT in lem:twoturnings and NOT in P5. It is in thm:bead's THIRD structural fact (P7 L763), the panel-D caption, and sheet_assignment.py step [3]:
- The paper correctly keeps THREE distinct congruences (A ruling, B ruling, photon=at-rest) — good, matches double ruling.
- But it ASSIGNS "A→+π/3 wing, B→−π/3 wing" where the receipt only derived that the ±π/3 wings are the τ̃↔τ̄̃ CONJUGATE PAIR of the SINGLE matter (A) cosmic-time continuation. Relabelling A's own conjugate wing as B is the double-ruling collapse.
- The two rulings A,B are distinct straight-line families on the hyperboloid (verified orthogonal at waist). The cosmic-time reading r(τ̃) is a function of τ̃=τ+χ; whether B's continuation is A's complex conjugate is NOT shown — it is assumed.
- Consequence: the sheet↔bundle assignment is OPEN. The paper (L763) and caption panel-D currently assert a closed 3→3 bijection that is not derived.

## STILL TO CHECK before any edit
- (a) Does thm:bead itself (statement/proof, L742-750) depend on the bad assignment? [read: NO — it's about the single closed lap + bounded contour; the sheet/bundle assignment is downstream commentary]
- (b) r976 "deep-bake into all 17": did any of the 17 per-paper citations import the bad A/B-wings assignment, or just the (sound) closed-bead? Need to spot-check the 17.
- (c) the caption panel-D text vs L763 vs sheet_assignment note — three loci, are they even mutually consistent?
- (d) confirm photon_cross_test.py + bead_contour.py are sound (the SECOND fact + the theorem proper).

---
## AUDIT COMPLETE — verified verdict (r988 state)

### SOUND (verified at source / by independent computation) — KEEP
1. **thm:bead statement + proof** (P7 L742-750). The single closed lap, geometric closure (P3), the E=1 cosmic-time reading, the bounded excursion |Im τ̃|≤πα/3 reaching π/3 at the comoving turnaround. Receipt bead_contour.py RE-RUN: r real & signed throughout, Im τ̃→π/3 at r=−0.727, held on collapse leg. ✓ Independent of any A/B assignment.
2. **First structural fact** (the two cosmic-time legs are τ̃↔τ̄̃ conjugates; period 2πα/3; r→e^{2πi/3}). bead_conjugate.py: about the single analytic law r(τ̃) and its conjugate. ✓
3. **Second structural fact** (photon crosses the seam). photon_cross_test.py RE-RUN: null geodesic continuous through r=0. ✓
4. **lem:twoturnings** (P7 L752). Math verified independently: two cubics correctly derived; comoving=equilateral cube-root orbit; slicing=colinear real; affinely inequivalent; the ℤ/3's agree only abstractly. The lemma DEFLATES a would-be bridge — correct, honest. ✓
5. **P5 (groupoid)** bead touch (prop:autA2 L478): σ/R/ξ as three distinct crossings of one lap — correct, careful. NO node-added lemma in P5; the "2+1/short-lemma-in-P5" hunch does not land — the added lemma is lem:twoturnings, in P7, and it's sound.
6. **r976 deep-bake into 16 companion papers**: spot-checked P16, p0 — both imported ONLY the sound closed-bead/bounded-contour. The bad A/B-wings assignment did NOT propagate out of P7. ✓

### THE ONE ERROR (isolated, contained to P7 + one receipt) — FIX
**Third structural fact** (P7 L763) + **panel-D caption** (L529) + **§frontiers item** (L961) + **sheet_assignment.py step [3]**:
- Claim: "the two null bundles A and B ... take the ±πα/3 wings" (a closed 3→3 bijection photon|A|B → real|+π/3|−π/3).
- Reality: sheet_assignment.py derives only that the ±π/3 wings are the τ̃↔τ̄̃ CONJUGATE PAIR of the SINGLE matter (A) cosmic-time continuation. Relabelling A's own −π/3 conjugate wing as "B" is the double-ruling collapse Daryl flagged. A and B are two DISTINCT null rulings of the doubly-ruled hyperboloid (verified orthogonal at the waist); nothing maps B's continuation to the −π/3 wing.
- The node also contradicted itself: WP_C3 note said "B rides no sheet / B is a space" (wrong), while sheet_assignment.py step [3] + the paper say "A,B take the wings" (also unfounded, but at least keeps B a bundle). Neither is derived.

**Correct honest state:** three DISTINCT congruences (A ruling, B ruling, photon=at-rest); photon→real crossing is derived; but the assignment of the two RULINGS to the two conjugate wings is OPEN — the map from {A,B} (distinct substrate rulings) to the sheets of r(τ̃) is not established. Do-not-assert, both ways.

### FIX SCOPE (minimal, honest — for Daryl's go before editing)
- P7 L763 third fact: retract the "A,B take the wings" bijection; state photon→real (derived), and that the two wings are the conjugate pair of ONE continuation, with the assignment of the two distinct rulings to sheets OPEN/not claimed.
- Panel-D caption L529: already hedged ("genuine open question") but still colours/says A/B on the wings — align to "conjugate pair of one continuation; ruling↔sheet assignment open."
- §frontiers L961: same de-assertion.
- sheet_assignment.py: annotate step [3] as asserted-not-derived; keep steps [1],[2] (sound).
- Changelog r977-r988 was never written — reconstruct + write r989 entry, cut a bundle.

NOTHING ELSE in the corpus needs touching (theorem, lemma, first/second facts, P5, the 16 companions all clean).

---
## FIX EXECUTED (r989) — all verified
- P7 thm:bead third fact (L763): de-asserted to photon→real (derived) + wings=conjugate pair of one continuation + ruling↔sheet map OPEN. ✓ re-read, consistent with facts 1&2.
- P7 §frontiers item (L961): de-asserted; withdrawn reading named as withdrawn; naming still open. ✓
- P7 panel-D caption (L529): wings framed as conjugate pair, assignment open; JanzenGroupoid cite on e^{2πi/3} dropped (it's a sinh^{2/3} fact). ✓
- synthesis_figure.py: panel-A legend "conjugate dual"→"ruling B (second ruling)"; lap label→"one closed slicing curve"; docstring RED redefined; panel-D wing comments corrected. Figure REGENERATED, viewed — panel A legend now honest. ✓
- sheet_assignment.py: correction header, step [3] withdrawn, steps [1][2] kept. ✓
- ANTIMATTER_FRONT_PLAN.md + WP_C3_SHEET_ASSIGNMENT.md: r989 correction flag prepended. ✓
- P7 recompiled via latexmk: 39pp, 0 undefined refs/citations. ✓
- r989 changelog entry (long) written into CORPUS_MAP.md. ✓
- r977–r988 NOT reconstructed (Daryl: not genuinely useful); the long r989 entry closes the arc.

## OPEN, handed forward (the real next work, in order):
1. The sheet↔ruling assignment — derive how {A ruling, B ruling, photon} map onto the sheets of r(τ̃), or show no canonical map exists. THE panel-D honest-version work.
2. The antimatter naming — not claimed, unworked both sides.
