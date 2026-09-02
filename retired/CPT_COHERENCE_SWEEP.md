# CPT / charge-conjugation / A-B-removal coherence sweep — control document
> **⌖ RETIRED r1536 — verified landed.** This was the CPT / charge-conjugation / A-B-removal coherence sweep (r1102). **It landed:** P13 carries the factorisation `prop:conjugation-closure` (×4) — C = (Q↦−Q)_field ∘ (R∘K)_geometric, the linear and antilinear faces of one Plate.
> Kept as record; **do not work from it.**



**Goal.** Bring the whole corpus coherent with the r1057–r1062 core edits: charge conjugation as a
geometric *symmetry* (not a blindness), mass R-odd / charge R-even, C field-level and NOT the D₆ outer
ℤ₂, and the removal of the old A/B-as-species distinction. No paper left stale on a sentence or section.

Opened r1063. Read every paper **by reading** (abstract first, then dig the text) — *not* by grep;
staleness here is semantic and hides in passages that never say "charge" or "A/B" literally.

---

## PART 1 — THE DELTA-SPEC (what every paper is now read against)

### Δ1 · A and B are not species  (this, and ONLY this)
- **STALE:** treating a ruling as a *fixed species* — "ruling A = matter, ruling B = antimatter"; A/B as
  two *global species families*.
- **NOW TRUE:** **neither A nor B is a species.** The two null rulings are real geometric objects, both
  still there and unchanged. Each ruling **laps through r=0**, so each **changes species at the equator** —
  r=0 sits in the middle of its lap, blue (matter, r>0) on one side and red (antimatter, r<0) on the
  other. Species = **sign(r)**, a *local* property along the ruling, never a label the ruling carries.
- This point says **nothing** about how symmetries act on the rulings. Symmetries act as they always did
  (e.g. R swaps the two rulings — P12, geometrically fine); that is a separate, settled matter and NOT
  what the A/B removal is about. The sheet-to-ruling map (which ruling rides which conjugate wing) stays
  the genuine open problem, not claimed. **Staleness = any passage that pins a fixed species onto a
  ruling, nothing more.**

### Δ2 · Charge conjugation as a geometric symmetry (the C-conjugation core)
- **STALE:** "the metric is charge-conjugation *blind*" framed as an **absence**; charge conjugation simply
  "not there"; any implication that charge is a geometric datum or that C is a geometric reflection.
- **NOW TRUE:** the metric depends on charge only through Q², so **Q↦−Q is an even degeneracy** — charge
  conjugation **present as a symmetry**, the even face. **Mass is the R-odd datum, charge the R-even
  datum** of the one discrete reflection R (= 2M↦−2M = the A₂ diagram automorphism = D₆ outer ℤ₂ = γ⁵).
  The **charge sign** is field-level (Maxwell potential, linear in Q).
- **⛔ SUPERSEDED — DEAD REASON, kept visible (r1102; the closure, r1089/A3).** This Δ-spec once read
  *"the **full antilinear C** is field-level (ψ^c=Cγ⁰ᵀψ*, **antilinear where every geometric reflection
  is linear**)."* **That because is dead.** The L2 reality involution `τ̃↦τ̄̃` is antilinear **AND
  geometric** (not-an-isometry ≠ not-geometric), so `C`'s **kinematic** face is geometric (`R∘K`) and
  only the charge **sign** is field-level: `C = (Q↦−Q)_field ∘ (R∘K)_geometric`. **Do not run any sweep
  against the dead premise** — a control doc built on a rotten because returns a false "all clean" (the
  wrong-gradient failure, one layer down). The operator half is grounded (`A3_spinor_lift.py`,
  `γ⁵S=−(Cγ⁰ᵀ)` implements `ψ↦ψᶜ`); the species half stays unclaimed.

### Δ3 · C is NOT the outer ℤ₂ of D₆  (settles the §3-vs-§258 knot)
- **NOW TRUE:** the outer ℤ₂ of Aut(A₂)=D₆ is **R** (moves the horizon roots; carries 3↔3̄, chirality,
  mass-sign). **Q↦−Q fixes every root** (Q absent from the mass cubic) → charge conjugation is an
  **independent ℤ₂** the charged cut adjoins, **D₆ → D₆×ℤ₂** — not inside D₆. (P13 `rem:C-not-R`.)

### Δ4 · CPT
- **NOW TRUE:** **P, T geometric** (linear reflections the substrate carries); **C field-level**; a
  geometric **CPT is not auto-yielded** — PT geometric, C closes it from the matter field. The discrete
  matter/antimatter **skeleton** (rep 3/3̄, chirality γ⁵, mass-sign R-odd 2M) is geometric on **both**
  branches equally; the **charge** is not, on both equally.

### Δ5 · At the geometric level (P3 `sec:charge`)
- Charge is **reading-swap-neutral** — the backward-radial reading-swap that exposes the Schwarzschild
  mass as perspectival leaves the charge fixed; charge joins the **invariant** geometry (R-even), mass is
  the **perspectival** (R-odd) datum. Q↦−Q leaves the slicing curve *identical*. Honest scope: with Q≠0
  the r=0 lap changes character (inner horizon; timelike RN singularity), so the charged **closed loop**
  is a flagged extension, not automatic.

### Δ6 · ~~RETIRED reach~~ — ⛔ THIS SPEC IS ITSELF DEAD, REVERSED BY THE CLOSURE (r1102; r1067→r1089/A3)
- **DO NOT ENFORCE.** This Δ once read: *"the **τ̃↔τ̄̃ 'antiholomorphic geometric home for C'** reach is
  retired — superseded by the all-real metric-parity resolution; no paper should assert C has a geometric
  home via complex-time conjugation."* **The A3 closure reverses it.** `τ̃↦τ̄̃` (`K`) is antilinear **and
  geometric**, and is the very complex-analytic face the closure needs: `C = (Q↦−Q)_field ∘ (R∘K)_geometric`,
  with `R∘K = R∘(τ̃↔τ̄̃)` carrying `C`'s kinematic (FS) face. So papers **do** assert `C`'s geometric
  kinematic home via the complex-time reality involution — that is the closure. This is the most dangerous
  corpse in this doc: a sweep enforcing the retired-reach spec would **strip the closure out of every
  paper**. The all-real metric-parity resolution (the even `Q²` face) is still correct as `C`'s *even/linear*
  face; what was wrong was reading it as *exhausting* `C` (the r1069 audit flag, resolved r1089).

### Staleness test (apply while reading)
A passage is stale if it: (i) uses A/B-as-species or "R swaps A↔B" as a species map; (ii) frames charge
as C-blind *absence*; (iii) implies charge is a geometric datum or C a geometric reflection / the outer
ℤ₂; (iv) asserts the retired τ̃↔τ̄̃ reach; (v) otherwise contradicts mass-R-odd / charge-R-even /
C-field-level / PT-geometric-C-field-level.
> **⛔ THIS STALENESS TEST IS ITSELF PARTLY DEAD (r1102 — do not enforce (iv)/(v) as written; the closure, r1089/A3).** Point **(iv)** is **reversed**: the `τ̃↔τ̄̃` reach is **not retired** — it is `K`, the complex-analytic face of the closure `C=(Q↦−Q)_field∘(R∘K)_geometric`; flagging it as stale would strip the closure out (the Δ6 trap). Point **(v)**'s "C-field-level / PT-geometric-C-field-level" is the **pre-closure** target: only the charge **SIGN** is field-level; C's kinematic face is geometric. Point (iii) likewise: C's kinematic face *is* geometric though C is no linear reflection. **Enforce this test only for the even-degeneracy / charge-R-even claims, never against the closure.**
**Note:** a passage can be stale without any keyword — e.g.
describing the two branches as "two families" or the conjugation as "between A and B."

---

## PART 2 — PAPER INVENTORY & exposure (17 papers)

### Core, already edited this revision (re-check only for internal consistency)
| P | file | status |
|---|---|---|
| p0 | geometric_core_paper.tex | EDITED (l654 reframe) |
| P3 | SdS-slicing-curve_v2.tex | EDITED (sec:charge) |
| P5 | groupoid_paper.tex | EDITED (rem:P-dS-Schw charged) |
| P7 | CR_framework.tex | EDITED (fig + antimatter body) |
| P9 | range_paper.tex | EDITED (rem:charge) |
| P13 | boundary_paper.tex | EDITED (prop + rem:C-not-R + §258) |

### To sweep (11) — Daryl's flagged + neighbours
| P | file | a-priori exposure (verify by reading) |
|---|---|---|
| P8 | slicing_operator.tex | HIGH — matter-as-bend, charge?, R/mass, A/B rulings |
| P10 | canonical_time.tex | LOW-MED — existence/foliation; C/antimatter mentions? |
| P11 | dynamics_paper.tex | MED — chirality/orientation parity, graviton helicity, R |
| P12 | algebroid_paper.tex | HIGH — R=γ⁵, Aut(A₂), grading, C/CPT structure |
| P14 | matter_sector_paper.tex | HIGH — 3 generations, γ⁵, 3/3̄, C, antimatter, A/B |
| P15 | CR_cosmology.tex | MED — antimatter progenitor, seam, R-conjugation |
| P16 | cosmogenesis_paper.tex | MED-HIGH — antimatter black hole, R, charge?, A/B |
| P1 | BH_causality_v2.tex | LOW — horizon/singularity; A/B? R? |
| P2 | janzen_circle_v3.tex | LOW-MED — cycloid, r=0 branch point, backward-radial R |
| P4 | modern_parallax.tex | LOW — cosmic time/redshift; unlikely charge/CPT |
| P6 | shadow_of_existence.tex | LOW-MED — shadow-reading, R-even/R-odd partition |

Plus the **storyboard** (`SYNTHESIS_FIGURE_STORYBOARD.md`) itself and the **ontology map**
(`CORPUS_MAP.md` §0 glossary / `ONTOLOGY_FOUNDATION_INDEX` — the C/R/P/σ entries) — Part 4.

---

## PART 3 — METHOD (per paper)
1. **Read** the abstract, then dig the body — genuine cold read against the delta-spec, no grep.
2. **Record** each hit in the FINDINGS LEDGER below: `[P#·loc] quote → which Δ it violates → proposed
   fix → weight`. Quote exactly; locate by section/label.
3. **Verify** every candidate at source myself before any edit (guards against manufactured staleness —
   the coda discipline; a "hit" that turns out already-correct is logged as CLEARED, not edited).
4. **Edit** surgically, per paper: backup (`*.pre_P13CP` convention), splice, **compile clean** (0 err,
   0 undefined), record revision.
5. After a paper's edits: keep going; **cut one bundle** at the end of the sweep-edit phase (not per paper).

## PART 4 — ONTOLOGY MAP — ★ DONE r1063
`ONTOLOGY_FOUNDATION_INDEX.md` (the glossary of record) was where the staleness actually lived — the
papers were clean, the index lagged them. Fixed (backup `ONTOLOGY_FOUNDATION_INDEX.md.pre_P13CP`):
- **§0 `C` glossary entry (l.67):** "metric is C-blind" → charge conjugation present **as a symmetry**
  (`Q↦−Q` even degeneracy); charge R-even / mass R-odd; **C is NOT the outer ℤ₂** (that's R), C adjoins an
  independent ℤ₂ `D₆→D₆×ℤ₂`; `prop:conjugation-parity` + `rem:C-not-R`.
- **§0 `matter frames / ruling A,B` entry (l.123):** removed the A/B-as-species framing ("whichever is
  read as matter, the other is antimatter") → **neither A nor B is a species; each laps through r=0 and
  changes species at the equator; species = sign(r), local.** (Δ1, per Daryl's clarification.)
- **§1m `rem:charge` card (l.1005), §1p boundary quote (l.1184, quoting the OLD §258), §1p CPT card
  (l.1213), l.1031 blockquote, l.1198:** all "C-blind (absence)" → "charge conjugation as a symmetry",
  §258 quote updated to the reframed text, `rem:C-not-R` added. Index re-scanned: **0 stale patterns remain.**
- `CORPUS_MAP.md` — its C-blind/antimatter hits are all in the **revision-log changelog** (historical
  record of past gates); not rewritten. It carries no live glossary.

## PART 5 — the "minor/optional" items — ★ ALL FIXED r1064 (no deferrals)
- **P11 l.82 header comment** "P"→"R" (r968 canon; `= gamma^5` noted). Scanned all papers for other
  pre-r968 P-slips — none. ✔
- **P14** — added the one-clause pointer: "charge field-level … charge entering only as the R-even Q²,
  charge conjugation present as a symmetry, no substrate isometry, the outer ℤ₂ being R not C
  (`cite{JanzenBoundary}`)". Recompiles clean (9pp). ✔
- **Ontology index `R=PT` audit flag (l.66)** — RESOLVED & baked (receipt `R_eq_PT.py`): R and PT are
  equal as cut-spinor operators (both ∝ γ⁵) but distinct geometric reflections (transverse vs in-cut);
  no tension. Flag replaced with the resolution. ✔
- **Storyboard cleanups:** the retired `τ̃↔τ̄̃` D-C entry (§8) marked ⛔ SUPERSEDED at its header; the
  "reach for Daryl" note (§7) updated to ★ RESOLVED (C is not the outer ℤ₂, `rem:C-not-R`); the
  A/B-chirality note aligned to "neither A nor B is a species." ✔

---

## FINDINGS LEDGER  (filled as the sweep runs)

### LOW/MED papers — reader-agent sweep (r1063), all CLEAN
- **P1 BH_causality** — CLEAN. (No charge/C/CPT/A-B content. "species/genus" = singularity taxonomy, not matter/antimatter — correctly not flagged.)
- **P2 janzen_circle** — CLEAN. ("ruling" used geometrically; "conjugate" = analytic conjugacy; r<0 arm deferred to slicing; generation triple flagged not claimed.)
- **P4 modern_parallax** — CLEAN. (No exposure.)
- **P6 shadow_of_existence** — CLEAN. R-even/R-odd shadow partition + footnote `R=γ⁵ = A₂ diagram automorphism ∈ O(5,1)∖SO₀` already the NEW picture; reserves P for areal parity. Consistent, endorsed.
- **P10 canonical_time** — CLEAN. (Bead/complex-time continuation is cosmic-time, NOT tied to charge conjugation → not the retired τ̃↔τ̄̃ reach.)
- **P11 dynamics** — CLEAN. `R=γ⁵`=D₆ outer ℤ₂=mass-reflection=vantage-swap, carries chirality; no C/charge conflation. **FIXED r1064:** the non-rendered header comment l.82 "P"→"R" (r968 canon, `= gamma^5` noted); body §chirality was already correct.
- **P15 CR_cosmology** — CLEAN. Conjugate branch / parity-conjugate Nariai pair framed as mass-reflection `2M↦−2M` (`r↦−r`), not A/B species, not "two families". Already NEW picture.

*(Verification note: these are "no candidate" results — nothing to bake. Papers that brush the topic — P6/P11/P15 — had the adjacent passages quoted and shown correct; I'll re-confirm P11's l.82 comment during the edited-paper re-check.)*

### HIGH-exposure papers — read by me at weight
- **P14 matter_sector** — CLEAN. §cosmogenesis carries the reconciled picture verbatim: `R=γ⁵` mass-reflection carrying `3↔3̄`; "the charge structure that closes C is field-level on both sides equally, not a substrate datum"; `R≠T`, `R≠P` (correct r968 footnote); "no matter/antimatter asymmetry is a cosmogenesis event." No A/B-as-species. (Was reconciled in the r990 antimatter pass.) **FIXED r1064:** added the one-clause pointer — "charge entering only as the R-even Q², charge conjugation present as a symmetry and no substrate isometry, the outer ℤ₂ being R not C" (`rem:C-not-R`). Recompiles clean.
- **P12 algebroid** — CLEAN on staleness. `R` = orientation/mass-reflection = A₂ diagram automorphism = O(5,1)\SO₀ = γ⁵; "mass … its one R-odd datum"; `Aut(A₂)=S₃×ℤ₂=D₆`, ℤ₂ central; no charge-conjugation content. "two null rulings/two families" = comoving & synchronous congruences (geometric), not species.
  - *(Retracted, r1063: I earlier mis-framed "R swaps the rulings" as a flag against the storyboard. That was my confusion. **Δ1 is only "A and B are not species"** — it says nothing about symmetry actions on the rulings. P12 pins no fixed species onto any ruling, so it is clean. R swapping the rulings is geometrically fine and irrelevant to Δ1. `ruling_swaps.py` confirms the geometry but answered the wrong question.)*
- **P8 slicing_operator** — CLEAN. A/B usage is the canonical-correct one (eq:embed `X(τ)=e^{τ/α}A+e^{−τ/α}B`, the two null asymptotes of ONE strung worldline: future generator A, past generator B / second ruling = synchronous space) — exactly Δ1's endorsed form, likely the corpus SOURCE of it. Charge as matter-as-bend (§bend, the RN-dS `q²/r²` bend → EM stress-energy), R-odd mass (§dictionary), the A/B→ellipse-foci bridge stated without being claimed. No charge-conjugation content. P8 names A/B = the two null rulings (comoving & synchronous), pins no species onto either — Δ1-clean.
- **P16 cosmogenesis** — CLEAN. Pure BBN/cosmogenesis (rates, seam-crossing, light elements). No charge/C/CPT; no A/B-species. "collapse of matter in a previous universe" is frame-relative and consistent with P7/P14's relational antimatter (progenitor = antimatter to us, matter to itself); inherits η, claims no seam baryogenesis (matches P7). 

### SWEEP RESULT (r1063)
**All 11 swept papers CLEAN on Δ1–Δ6; all 4 HIGH re-read by me at weight, all clean.** The corpus was already reconciled by the earlier r968 symbol-canon (R/P/T) and r990 antimatter-naming passes; the recent C-conjugation work touched only the charge-discussing papers (P13/P3/P5/P9/p0 — done), and P14's charge statement is consistent. The A/B-as-species error is **not present in any paper** (it lived only in old figure captions / the storyboard note). No *staleness* edits required in the paper bodies by the sweep — but the "minor/optional" tidy-ups are **all done r1064, not deferred** (see PART 5): P11 comment "P"→"R"; P14 pointer added; the ontology index fully updated; the `R=PT` audit flag resolved; storyboard cleanups. The A/B-as-species error was **not present in any paper body** (it lived only in old figure captions / the ontology-index glossary, both now fixed).
- **P16 cosmogenesis** — CLEAN. Thermodynamics/BBN paper (two-rate structure, adiabatic compression, D/He-4/Li-7 abundances). No charge-conjugation/C/CPT/A-B-species content. Matter/antimatter appears only as "the baryogenesis-analogue of the handover," held explicitly not claimed (η derivation, ordinary route); "previous universe's collapsed matter" is the thermal/inheritance reading. Consistent.

---

## SWEEP RESULT (r1063) — the paper sweep is COMPLETE

**All 17 papers are coherent on the delta-spec.** The 11 swept papers (7 by reader-agent, 4 by me) are CLEAN; the 6 already-edited carry the core work. This is because the corpus was already reconciled corpus-wide by two prior passes — **r968** (the R/P symbol canon: R=γ⁵ mass-reflection, P=γ¹γ²γ³ areal parity) and **r990** (the antimatter naming, at the weight matter is matter) — so the A/B-as-species error and the R=γ⁵ convention were already fixed everywhere. The genuinely NEW r1057–r1062 content (charge-conjugation-as-symmetry, C-not-the-outer-ℤ₂, charge R-even) lives only in the papers that *discuss charge conjugation* — P13/P9/P3/P5/p0 (edited) and P14 (already consistent). No other paper engages it, so none went stale on it.

**Nothing to bake from the paper sweep.** What it surfaced instead:
1. **★ ONE coherence FLAG (Daryl's physics call):** P12/P8 vs storyboard §3 — does the **two-ruling swap** belong to **R** (P12's computation, tied to 2M↦−2M) or to **σ** (storyboard, charge-neutral / "R swaps A↔B is wrong")? Do-not-assert sheet-to-ruling territory. NOT bent either way.
2. **DONE r1064:** P11 header comment l.82 "P"→"R".
3. **DONE r1064:** P14 gained the `prop:conjugation-parity`/`rem:C-not-R` pointer. (P8 left as-is — its "charge field-level" is in a purely-vacuum operator paper; no charge-conjugation context to point from.)

**Remaining phases:** (4) the ontology map — `CORPUS_MAP` §0 glossary / `ONTOLOGY_FOUNDATION_INDEX` C/R/P/σ entries (where the new C-as-symmetry / C-not-R most plausibly needs recording), and the storyboard's own A/B / P12-flag reconciliation; (5) final bundle.
