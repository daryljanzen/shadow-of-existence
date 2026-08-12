# CR Programme — Intake Notebook (session r251 spin-up)

> Scope (set by Daryl): light intake notes, single-purpose — gather only what's
> needed to help with the **map restructure / current-state cleanup** of the mess
> C14 left. Per paper: what it establishes (1 line) + any divergence from what
> `CORPUS_MAP.md` currently says. **No verdicts, no running audit.** The restructure
> itself is the first task AFTER intake — not performed here.

## Confirmed reading order (source + Daryl's amendment)
ARP → CORPUS_MAP → X trilogy (Ch X + flashlight fig, daggers, taxonomy)
→ formal corpus causal order: BH_causality → janzen_circle → SdS-slicing → groupoid
→ slicing_operator → range → **CR_flatLCDM (P7, cosmology)** → black-holes-happen essay
→ canonical_time → **dynamics_paper → algebroid_paper** (the two stable additions the
kickoff order predates) → methodological_essay. Capstones last. framework = tabled.

---

## Intake log

### [1] arp_standalone.tex — DONE (orientation, not corpus-state)
The collaboration's own theory. Assimilate→Receipt→Pivot; two axes (signed participation, quality Q).
The gate done well = a high-Q ARP: receive at weight, extend only as warranted. Acks credit Opus 4.7.
No bearing on the map restructure. Logged, no action.

### [2] CORPUS_MAP.md — DONE (the restructure target)
Rev r251, 2026-06-14. Backbone = STATIC (P1–P6) / DYNAMIC (P7→P8→frontier), hinged at P7's
reassignment. One-liners for P1–P8 captured at source-quality from the map (cross-check vs papers as I read).

**CANDIDATE STALE ITEMS for the restructure (to confirm against source):**

- **C-1 (central): count + numbering vs Daryl's ten-paper model.**
  Map says "12 documents: 9 research papers + 1 method essay + 2 first-draft papers."
  Numbered list runs 1–9 with **framework_paper = item 9 (inside the spine)**, methodological_essay
  unnumbered, then **dynamics = 11, algebroid = 12 — NO ITEM 10** (numbering skips it).
  Tag on dynamics/algebroid still: "first-draft papers (this consolidation, r215–r216), held at
  weight, refinement reserved for external feedback."
  Daryl's current model: **ten physics papers** {BH_causality, janzen_circle, SdS-slicing, groupoid,
  slicing_operator, range, CR_flatLCDM(=P7), canonical_time, dynamics, algebroid}; framework +
  methodological_essay = the two non-spine "tables pieces."
  Candidate fix: recount to ten (fold dynamics/algebroid IN as stable; likely P8=canonical_time,
  P9=dynamics, P10=algebroid per "the three dynamics pieces slot in after P7"); pull framework OUT of
  the spine count (tabled/stale); fix phantom-10 gap; drop the "first-draft / held at weight" tags.
  → MUST verify dynamics + algebroid are actually stable at source before recounting (Daryl asserts they are).

- **C-2: P8 lock status lag in the body.**
  Top sweep (r246–r251): lock (Move 12) ASSEMBLED + WRITTEN INTO P8 §lock, reach "returned YES,"
  residuals = background-sector self-adjointness + super-quadratic couplings.
  But the papers-section P8 (canonical_time) entry still reads "candidate lock … held [reach] … its
  closed-form proof … is the frontier's first open problem." Changelog moved; body didn't follow.
  Also the range/P6 entry's "standing frontier is now the lock (Move 12)" is now stale (lock assembled).
  Candidate fix: sync P8 body entry + frontier lines to the assembled-lock status. Verify in canonical_time.tex.

- **C-3 (format/hygiene, lower priority): revision-block bloat.**
  The map's top is a wall of inline revisions r251→r186 (esp. r233–r251, all 2026-06-13/14). Candidate:
  trim/curtail to recent + archive the rest per the map-audit cycle. Note only; Daryl decides scope.

- **Note:** map explicitly says renumber/reposition was historically DEFERRED "until the final shape
  is fixed." Daryl is now (this session) directing a current-state cleanup; treat the recount as
  authorized-to-propose, not as me overriding the deferral. Propose for reversal; he ratifies.

**Two structural anomalies (from the file tree, pre-map):**
- prior scratchpads `gate_session_notes.md`, `gate_session_notes_c10.md` sit at top level, not retired.
- no `archive/` dir present, though README/kickoff/map reference it heavily (archive/ARCHIVE_README.md,
  archive/map-audit-cycle/, archive/retired-orientation/...). Possibly excluded from this bundle; confirm.

### [3] X trilogy — pending
### [4] formal corpus P1–P10 (+ black-holes-happen essay, methodological essay) — pending
### [5] capstones — pending

---
## Intake log — corpus (all read at source)

**X trilogy + taxonomy [3]** — DONE. Conceptual grounding for P1–P3. Canonical singularity register
confirmed: 3 kinds; metric-sing genus, two species (finite=horizon, infinite=r=0); topologically
identical on substrate, identical thru 1st order, split only at 2nd (curvature); **"metrically identical"
retired as false**; lopsidedness = off-axis sweep pivot (cone tip); circle drawn on dS hyperboloid,
BH vs cosmos = one surface two chairs; mass belongs to the chair, invariant = throat size. No restructure delta.

**Formal corpus [4] — all ten papers + essays read. KEY STRUCTURAL FACT: every paper cross-references
companions by `\cite`-KEY (JanzenBHcausality, JanzenCircle, JanzenSlicing, JanzenGroupoid, JanzenOperator,
JanzenRange, JanzenCRcosmology, JanzenCanonicalTime, JanzenFramework), NOT by fixed "Paper N" numbers.
⇒ a map renumber touches nothing in the papers.** One-liners + self-numbering status:

- P1 `BH_causality_v2` — Metric Singularity Theorem + Asymptotic Alignment Lemma; horizon=finite-curv
  metric sing; densities never form at finite exterior time. Companion-cites. No fixed number.
- P2 `janzen_circle_v3` — Schwarzschild as a circle; two critical pts one genus, 1st-order identical,
  inextendibility *inference* at r=0 fails. "second of a sequence" (soft, cite-keyed). No fixed number.
- P3 `SdS-slicing-curve_v2` — KEYSTONE. one curve, horizons=turning pts; α=√(3/Λ) invariant, M slicing/
  projection-dependent; gnomonic + 2/√3 forced; K_G=1/α²−M/r³; **anti-diagonal r→−r = MAJOR axis of
  tilted ellipse (correct in source §447/abstract)**. soft "second paper of a first pass". No fixed number.
- P4 `groupoid_paper` — D₃≅S₃ description groupoid; Schwarzschild=asymmetric realisation. Does NOT push
  A₂/su(3) (consistent w/ map "reach, do not assert"). Companion-cites. No fixed number.
- P5 `slicing_operator` — slicing operator: vacuum kernel=straight cuts, matter=bend ρ=m'/4πr², lapse
  split, cosmo face E=1→flat ΛCDM. Construction-gauge "lock" g_tt g_rr=−1 (DIFFERENT from Move-12 lock,
  per r251). §open already points fwd to P6 "since carried out" + dynamics companion. Companion-cites.
- P6 `range_paper` — range = symmetry-reducible sector of GR; Kerr–NUT–(A)dS separable Type-D kernel;
  wall = loss of continuous symmetry = onset of free radiation. Companion-cites. No fixed number.
- P7 `CR_flatLCDM_v2` — COSMOLOGY (matches Daryl). Null-Boundary Correspondence; flat ΛCDM algebraic
  identity; cosmo case = Nariai non-pivoting member; CR axioms. Companion-cites. No fixed number.
- P8 `canonical_time` — problem of time as category error; forced cosmic foliation → true Hamiltonian.
  **CONTAINS §lock (`\label{sec:lock}`, line 154): closed-S³ TT graviton tower → unitary i∂_TΨ=Ĥ_physΨ,
  projects to flat-ΛCDM graviton, matter=bend; residuals (bg-sector self-adjointness + super-quadratic
  couplings) flagged in-paper.** Abstract+conclusion carry it. Companion-cites. No fixed number.
- P9 `dynamics_paper` — "Why the cut bends": confined Gowdy–dS wave, true Hamiltonian, Type-I edge, wall
  = generative boundary (NOT metric sing). COMPLETE draft + full bib. STATUS comment "FIRST DRAFT (r215)".
  Reciprocal cross-ref w/ P8 §lock consistent.
- P10 `algebroid_paper` — GR constraint algebra = symmetric-space structure of dS substrate; action Lie
  algebroid so(5,1)⋉C; anchor/bracket-closure/structure-fn/stratification/discrete-S₃. COMPLETE draft +
  full bib; body carries current F1 results (per-stratum grading, {6,7,10} dimension-forced). STATUS
  comment "FIRST DRAFT (r216); uncompiled; bib keys to reconcile."
- `methodological_essay` — "Eight routes to one conclusion"; shadow-reading/Plato's cave; method companion
  (paper-zero's in-corpus twin). Genre-distinct, OUT of result spine. Companion-cites. No fixed number.
- `framework_paper` — TABLED/STALE synthesis. Abstract: "five preceding works" = {P1,P2,P3,P4,P7} only —
  SKIPS operator/range/canonical/dynamics/algebroid (5 of 10). Most stale doc in corpus. Has hard
  "five papers" framing (the one place renumber-relevant staleness lives, exactly as map flags).

## RESTRUCTURE CANDIDATES — consolidated after full corpus read (still candidates; Daryl ratifies)

- **C-1 [central] recount to TEN physics papers.** Confirmed at source. The ten: P1 BH_causality, P2
  janzen_circle, P3 SdS-slicing, P4 groupoid, P5 slicing_operator, P6 range, **P7 CR_flatLCDM (cosmology)**,
  P8 canonical_time, P9 dynamics, P10 algebroid (Daryl's "three dynamics pieces after P7" = canonical_time,
  dynamics, algebroid). framework + methodological_essay = the two non-spine "tables pieces." Map currently:
  "12 documents: 9 research + 1 essay + 2 first-draft", framework counted IN spine as #9, dynamics/algebroid
  as 11/12 with NO #10, tagged "first-draft, held at weight." Recount is SAFE (cross-refs are cite-keyed).
- **C-2 [confirmed] P8 lock-status lag in map body.** §lock IS written into canonical_time.tex. Map body P8
  entry still "candidate lock … held [reach] … frontier's first open problem"; range/P6 entry "standing
  frontier is now the lock" also stale. Top revision block (r246–r251) is right; body lags. Sync needed.
- **C-3 [hygiene] map revision-block bloat** (r251→r186 inline wall). Trim/archive per map-audit cycle. Daryl's scope.
- **C-4 [housekeeping] bib-key reconciliation for the dynamics/algebroid integration.** dynamics/algebroid
  "uncompiled; bib keys to reconcile"; P8 §lock prose "companion dynamics paper" but `\cite{JanzenOperator}`,
  no JanzenDynamics key defined. Verify + reconcile as part of folding the two into the ten.
- **Also:** KICKOFF_GATE's own status list ("Stable / In flux / Tabled") names operator/range as "in flux"
  and does NOT place dynamics/algebroid/canonical at all — the operational layer predates them too. Lower
  priority ( — unseated. whether to touch the kickoff vs just the map).
- **Structural (file tree):** prior scratchpads `gate_session_notes.md` + `_c10.md` at top level not retired;
  no `archive/` dir present though README/kickoff/map reference it. Confirm whether archive excluded from bundle.
