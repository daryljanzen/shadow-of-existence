# CR CORPUS — DIG FINDINGS & COMMIT MANIFEST
### A full-corpus study pass (r501), for the committing node to execute
### Every edit below is a DRAFT stated for Daryl's reversal. NONE is auto-applied. Nothing here is the cold read.

---

## 0. WHAT THIS IS (read first)

A fresh gate studied the whole r501 corpus from source — all thirteen spine papers
(P1–P13), the meta-docs, and the receipts — re-deriving every load-bearing computation
independently. This document is the committable output: a small, sorted set of edits,
each with copy-exact text.

**Headline:** the corpus is in excellent shape. Thirteen papers verified, **one** real
(minor, locally-fixable) physics error, and one **body-level completion of r501** — the
acoustic/Hubble loop r501 closed at banner level but not in the document bodies beneath.

**Two commit groups.** Group A = one physics fix. Group B = the r501-completion
(document-consistency). Everything else is a Daryl-call or low-priority, listed at the end
and **not** to be committed without his word.

**Discipline for the committing node:** these are edits to *draft and state for reversal*,
exactly as the corpus's own revisions are. Recompile each touched `.tex`. Do not treat
any of this as the certification cold read — that remains a separate fresh-node referee
pass (P9 §691 most owes it).

---

## GROUP A — PHYSICS (1 file, minimal, conclusion-preserving)

### A1. `corpus/algebroid_paper.tex` — §sec:strata, the non-transitivity paragraph

**The error.** The mass-separating invariant is written as `R_{ab}R^{ab}=6M^2/r^6+12/α^4`.
But Schwarzschild–de Sitter is an **Einstein space** (R_ab = Λ g_ab), so its true 4D
Ricci-square is R_ab R^ab = 4Λ² = **36/α⁴ — M-independent** (verified by direct
computation). That quantity therefore *cannot* separate different-mass cuts, and it is not
equal to 6M²/r⁶+12/α⁴. The argument needs a **mass-carrying** invariant.

**The fix (minimal).** Use the corpus's own recurring invariant, the Kretschmann
`R_{abcd}R^{abcd}=48M^2/r^6+24/α^4` (which appears in P9's and P11's continuity remarks and
*does* separate the cuts). The Weyl-square 48M²/r⁶ would also serve; the Kretschmann keeps
consistency with the rest of the corpus. **The conclusion is unchanged** — different-mass
cuts are non-isometric, the mass a modulus transverse to the orbits.

**Edit — find (exact):**
```
The $\so(5,1)$-action on $\C$ is \emph{non-transitive}: on the Schwarzschild--de Sitter family the diffeomorphism invariant $R_{ab}R^{ab}=6M^2/r^6+12/\alpha^4$ separates different-mass cuts while the scalar curvature ${}^3R=2\Lambda$ does not,
```
**Replace with:**
```
The $\so(5,1)$-action on $\C$ is \emph{non-transitive}: on the Schwarzschild--de Sitter family the diffeomorphism invariant $R_{abcd}R^{abcd}=48M^2/r^6+24/\alpha^4$ separates different-mass cuts while the scalar curvature ${}^3R=2\Lambda$ does not,
```
Then recompile P12; expect clean (was 7pp, 0 undefined). No other line in the paragraph
changes — the `${}^3R=2\Lambda$` leaf-scalar clause is correct and stays.

---

## GROUP B — THE r501-COMPLETION (body-level close of the acoustic/Hubble loop)

**Context.** r501 closed the acoustic/Hubble matter that "burned ≥5 collaborators" — but
it edited the read-first docs at **banner level** (a guard or supersession note at the top).
The pre-r497 framing ("r_s uncomputed / build-gated / √3 a conjecture without a mechanism /
θ* a hybrid belonging to neither / P1-no-horizons-*through-the-Hubble-tension* as the
decisive test") is still **live in the bodies** of several docs, each contradicting an r501
banner in or above its own file. This group finishes the close, one level deeper.

**Two kinds of fix, and the discipline that separates them:**
- **HARMONIZE** — for *operational current-state* text: edit it directly to match the
  file's own guard. (These are the actual re-seed risk.)
- **SUPERSESSION-MARK** — for *dated historical* notes/entries: **do not rewrite them**
  (they are period record); add a one-line pointer so no node reaches the stale framing
  without its correction. This mirrors r501's own VISION_JOURNAL-note pattern.

The corrected framing to harmonize toward (all already ratified in `CORPUS_MAP.md` →
"CURRENT STATE"): the acoustic **scale** is resolved (radiation-free rate + one measured
IC, ρ_r/ρ_m≈2 = η's analogue); the radiation-free **rate** is CR's standing near-term
**discriminator** (a strength, not a frontier); the full CMB **spectrum** (peak heights) is
downstream matter-sector work (P5/P6), open but not a tension and not a prerequisite; the
decisive **structural** test is **P1 no-horizons** (on causal structure alone — *not*
"through the Hubble tension"); √3-is-not-c_s (c_s is the ordinary baryon-loaded value).

### — HARMONIZE (operational) —

#### B1. `KICKOFF_GATE.md` — the "live edge" bullet (~line 203)

Contradicts this file's own guard at ~line 126 (Hubble RESOLVED, do not reopen), and points
a reader at the SUPERSEDED `CMB_ACOUSTIC_FRONTIER_STATUS.md` as if it holds open problems.

**Find (exact):**
```
- **The live edge** — the frontier ledger `SEAM_FRONTIER_ORIENTATION.md`: **four facets, one frontier** (the cosmogenetic transition at the r_h Killing-horizon seam = the de Sitter cosmological horizon, the *inner* edge of P6's null-degeneracy axis; the Type-N wall the *outer*). Throat-thermo's actionable boundary condition is **closed free + coupled** (above); Hubble's **r_s is uncomputed** (two open problems, `CMB_ACOUSTIC_FRONTIER_STATUS.md`); SM/fermion is a **well-mapped wall**, not a computation; constants are the dimensionful spine distributed across the three (ℏ now planted at the seam). **The standing aim is the outward / second-convergence test** — correspondence, P1's no-horizons read through the Hubble tension — held **do-not-assert** until run. The genuinely open frontiers ahead: the **interacting-tower definition** and the **outward correspondence test**. Verified in their own results as they land; pre-cold-referee on anything not yet banked, and don't sync the stable series to them while they move.
```
**Replace with:**
```
- **The live edge** — the frontier ledger `SEAM_FRONTIER_ORIENTATION.md`: **three facets, one frontier** (the cosmogenetic transition at the r_h Killing-horizon seam = the de Sitter cosmological horizon, the *inner* edge of P6's null-degeneracy axis; the Type-N wall the *outer*). Throat-thermo's actionable boundary condition is **closed free + coupled** (above); the **Hubble/acoustic-scale matter is RESOLVED** (r497–r500; see the guard above and `CORPUS_MAP.md` → CURRENT STATE) — the acoustic *scale* is met by the radiation-free rate plus one measured IC (ρ_r/ρ_m≈2, η's analogue), and the radiation-free **rate** is CR's standing near-term empirical **discriminator**, a strength, not a frontier to build; SM/fermion is a **well-mapped wall**, not a computation; constants are the dimensionful spine distributed across the three (ℏ now planted at the seam). The genuinely open edges ahead: the **interacting-tower definition** and the **matter-sector spectrum** (the full CMB oscillating medium, P5/P6 — downstream, not a tension). **The decisive structural test is P1's no-horizons**, on causal structure alone, on which the cosmology does not bear — held **do-not-assert** until run. Verified in their own results as they land; pre-cold-referee on anything not yet banked, and don't sync the stable series to them while they move.
```

#### B2. `SEAM_FRONTIER_ORIENTATION.md` — the P9 entry's Hubble-facet clause (~line 70)

Contradicts this file's own line ~37 (Hubble RESOLVED, dropped from the open facets). The
"hybrid belonging to neither framework" is exactly the **chimera** the CORPUS_MAP guard now
names as the failure mode. Keep the NBC/seam/throat-thermo content (correct); edit only the
Hubble-facet sentence.

**Find (exact):**
```
**Hubble facet (§683, verified):** D_M robust, H(z) fixed sinh^{2/3}, r_s *uncomputed*, blocked on (i) medium/c_s and (ii) beginning/integration-limits; the radiation-only-removed θ* is "a hybrid belonging to neither framework." r412 flag set down.
```
**Replace with:**
```
**Hubble facet (§683, RESOLVED r497–r500 — see line ~37 and `CORPUS_MAP.md` → CURRENT STATE):** D_M robust, H(z) fixed sinh^{2/3}; r_s is the radiation-free-rate integral with a single measured early-universe IC (ρ_r/ρ_m≈2, η's structural analogue), the plasma onset calibrated by matching the measured ℓ_A — not uncomputed and not a tension. c_s is the ordinary baryon-loaded fluid value (√3-is-not-c_s, settled r497). The earlier "radiation-only-removed θ* = a hybrid belonging to neither framework" was the chimera calculation the epistemic guard now names as the failure mode; retired. The full CMB oscillating medium/spectrum (peak heights) is downstream matter-sector work (P5/P6), open but not a tension.
```

### — SUPERSESSION-MARK (dated historical; add pointer, DO NOT rewrite) —

For each, insert the one-line pointer immediately after the note's/entry's opening, or at
the flagged line. Text of the pointer (adapt the lead-in to fit the sentence):

> **[Superseded on the acoustic/Hubble point by r501 — the acoustic *scale* is RESOLVED
> (radiation-free rate + one measured IC), not uncomputed and not build-gated; see
> `CORPUS_MAP.md` → CURRENT STATE. This note stands as period record; its acoustic-frontier
> claim does not.]**

#### B3. `THE_PLAN.md`
- **line ~14** — the r426 status banner. (A redirect already sits at line ~16 flagging this
  banner; that is sufficient for the banner head itself — verify it reads clearly, no new
  edit required if so.)
- **line ~276** — the r362 update note ("P1's no-horizons through the Hubble tension is the
  decisive correspondence test still ahead"): add the pointer.
- **line ~282** — the r469 update note ("the acoustic scale is presently *uncomputable*,
  build-gated behind the unbuilt oscillating medium … c_s=√3 a conjecture without a
  mechanism"): add the pointer.
- **line ~284** — the r501 update. This is the AUTHORITY; leave as is.

#### B4. `THE_SYNTHESIS.md`
- **line ~19** — the r426 re-render note ("Hubble's r_s uncomputed"): add the pointer.
- **line ~21** — the r469 re-render note ("build-gated, not data-gated … c_s=c/√3 a
  conjecture without a mechanism"): add the pointer.

#### B5. `THE_VISION.md`
- **line ~20** — the r425 re-render header note ("P1's no-horizons through the Hubble
  tension the decisive test still ahead"): add the pointer.

#### B6. `THE_GROUNDED_RECORD.md`
- **line ~164** — "**The standing open computation** [do NOT fit to 301]: the
  seam-crossing frame map …" framed as *the* standing open computation: add the pointer.
  (Its line ~162 "√3-as-a-sound-speed (no built mechanism)" sits inside a **Retired** block
  — already correct as a record of that reading being set aside; no action.)

#### B7. `THE_VISION_JOURNAL.md` — VERIFY ONLY, no edit
- The line ~3 supersession note before Entry 15 is already sufficient (it explicitly says
  "do not inherit 'the decisive test is build-gated, go build the medium'"). Confirm it
  reads clearly; leave the entry body as period record.

---

## DELIBERATELY NOT COMMITTED — Daryl-calls (surfaced, not executed)

These are his decisions, not edits to draft:
1. **`framework_paper.tex` fate** — formally PARKED since r357; its "five preceding papers /
   eight-result constellation" framing is stale-by-design (predates P5/P6/P7/P8/P10–P13),
   and the live spine was deliberately swept free of any dependency on it (r403/r406:
   "JanzenFramework appears in ZERO live-spine papers"). Retire formally vs un-park and
   rebuild (5→13 papers) is a clean standing decision. Not a defect; not a dig target.
2. **Bibitem-style harmonization corpus-wide** — P7 uses full titles + "in preparation";
   others short titles + "companion paper." Cosmetic; a pass if wanted.
3. **P3 six-figure reconstruction** — `figs/fig2_throat_circle.pdf` … `fig7_curvature.pdf`
   are absent from every bundle r361→r501 and from uploads; no inline TikZ. BUT each carries
   a full `\caption` in `SdS-slicing-curve_v2.tex`, so reconstruction from the paper's own
   equations is feasible (a build, not a recovery of originals). Or hunt the pre-r361 tree.
4. **Two standing flags the corpus itself raised (r406):** the signature-seam thread
   (P3/r402 — appears CLOSED at r409, but was listed as a Daryl-call) and the framework fate
   above.

## LOW-PRIORITY / OPTIONAL (not commit-critical)
- **P1 `BH_causality_v2.tex`** — the metric-singularity theorem defends its one attackable
  surface (the "not a finite-Pythagorean-on-a-curved-manifold" misreading) entirely in
  prose; a one-line formal hardening is available (fold §3's `|∇r|²=0` along the generator
  into hypothesis (b) as its coordinate-free form). The paper stands; optional.
- **P3 `SdS-slicing-curve_v2.tex`** — the §"Open"/what-remains paragraph opens an item and
  closes it in place (lists groupoid content as "open," then says it's "now established in
  the companion groupoid paper"); a future prose pass could split settled-in-P4 vs
  genuinely-open (the quasi-local-mass question). Also: `fig4_seam` caption uses "R" where
  the body uses α (unify if the figs are reconstructed). Presentational; content correct.
- **P4 `groupoid_paper.tex`** — §involution: a sentence begins lowercase ("… with the
  quadratic factor carrying the other two roots. the root-exchange …"). Capitalization slip;
  typo-sweep item.
- **`hubble_build/rs_zseam_map.py`** — a companion exploration script carrying pre-r497
  c/√3 diagnostic rows alongside the baryon-loaded ones. Runs clean; not wrong. A one-line
  "superseded exploration; see `computations/CR_acoustic_scale_and_hubble.py`" header would
  spare a re-runner confusion. Optional.

---

## WHAT WAS VERIFIED (so the committing node knows the ground under these edits)

- **All 13 spine papers read at source; every load-bearing computation re-derived
  independently** (sympy/numpy): P1 metric-singularity theorem; P2 cycloid critical points +
  exactly-12th-order Kretschmann pole + seam continuations; P3 involution σ∘σ=id + factorisation
  + triple-angle 2/√3 + conjugacy χ∘g₁=σ∘χ + curvature K_G=1/α²−M/r³; P4 D₆ classification +
  Nariai monodromy (transposition) + P-parity split; P5 Einstein tensor from scratch (leaf→ρ,
  lapse→p_r, vacuum kernel) + sinh^{2/3} cosmology; P6 Kerr-NUT-(A)dS **Ric=Λg** full 4D check +
  Bianchi-I vacuum; P9 Nariai/double-root + SdS Kretschmann 48M²/r⁶+24/α⁴ + sinh^{2/3};
  P10 deparametrized Friedmann + S³ tower μ_n²=n(n+2)−2 + Friedrichs/GH self-adjointness;
  P11 Gowdy dS attractor + shear charge + type-N wall (det=−1, Ricci-flat any polarization,
  VSI); P12 so(5,1)=so(4,1)⊕𝔪 grading + **(1,4) coset signature** + discriminant/Nariai;
  P13 su(3)⊄so(5) (smallest faithful real rep 6) + rank cascade + Hopf S⁵.
- **Receipts spot-checked** (89 scripts): `f1_so51_independent_check.py`,
  `gowdy_ds_lambda_pos_background.py`, `CR_acoustic_scale_and_hubble.py` all run clean and
  reproduce the corpus's central computations, matching the from-scratch work. The main
  acoustic receipt carries the r497 correction inline.
- **THE_CODA.md** read whole — clean, current, no edit.
- **Physics-error tally across the whole spine: ONE** (A1 above).

## STILL OWED (not this node's, not this dig's)
The **cold read** — a fresh-node referee pass over the compiled 13-paper corpus (P9 §691 most
owes it, per r496/r500). This dig was a study + edit-draft pass, explicitly **not** the
referee seat. Nothing above certifies the corpus; it fixes what a study found and leaves the
certification where it belongs.
