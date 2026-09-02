> **⌖ RETIRED r1543.** This was the first-edition audit (r935) — every flagged uncertainty and dangler. **Landed:** its punch-list is carried in `THE_PLAN` (×3), items 1–3 struck DONE at r933/r934.
> Kept as record; **do not work from it.**


# First-Edition Audit — every flagged uncertainty and dangler in the corpus, classified

**Built r931 (c37) by a six-reader source audit of all 17 papers (P1–P16 + p0/17), read at weight against the first-edition bar.** This is the awareness deliverable: *be aware of, and have worked, every flagged uncertainty still dangling in the corpus.*

**THE BAR — "only genuine problems remain."** The first edition ships when the corpus is fully internally coherent and every dangling thing is EITHER resolved by a good honest effort OR a genuine open research problem, honestly and visibly marked open ("go figure out what the Higgs is"). Nothing accidental: no unfinished chores, no unkept "we will show" promises, no stale cross-refs, no internal contradictions, no unproven-but-asserted claims, no missing figures, no build errors.

**THE HEADLINE FINDING — the corpus is close, and the line is a bounded cleanup, not a research effort.** The content-level open problems are almost uniformly **well-marked not claimed / `conjecture`** — the discipline is exemplary; the readers found **no case of a claim asserted as established but secretly unproven.** The danglers are overwhelmingly (a) a handful of reader-visible **staleness bugs from the matter-sector build** (P7, P12, P13, P16 — specific and fixable), plus (b) mechanical **bibliography / figure / hygiene** items. Cross the line and you have both the publishable book and the distributable programme.

---

## Part 1 — THE DANGLERS (above the line; the first-edition work-list)

> **✔✔ STAGE-1 CLEANUP FULLY COMPLETE (r933 + r934).** Every Part-1 item is now **worked and verified**; all 17 papers recompile clean (0 undefined citations). The two items deferred at r933 were completed autonomously at **r934** (Daryl away): **A1** the six P3 figures generated into `corpus/figs/` (Arthur's faithful renderings from the papers' math, for Daryl's review — P3 now 31pp, 0 missing-figure warnings) and **C5** p0's drifted §landing line-anchors refreshed to current (all 14 corrected, verified at source; p0 clean 19pp). **No hard danglers remain.** — The r933 pass:
>
> **✔ STAGE-1 CLEANUP DONE (r933).** All items below **worked and verified** except two, and all 17 papers recompile clean (0 undefined citations): **A2** P5 bibitem fixed; **A3** P7 "unbuilt→propagating fermion field" contradiction resolved (abstract/intro/item-5); **A4** P16 stale P15 meta-correction reworded; **B1** P12 `\cite{JanzenMatter}` added *(+ its bibitem)*; **B2** P13 spinor-sector wording sharpened; **C1** bibliography normalized to "companion paper (P#)." across **185 bibitems** (external works untouched); **C2** three orphan bibitems dropped (verified uncited: P13 `HochsMathai`, P11 `JanzenCircle`, P15 `JanzenCanonicalTime`); **C3** two receipt-pointers removed; **C4** P8 "forthcoming companion" → `\cite{JanzenCanonicalTime}` *(+ its bibitem)*; **C6** p0 "stub by design" reworded. **DEFERRED AT r933, NOW DONE AT r934:** **A1** the six P3 figures generated and **C5** p0's §landing anchors refreshed (both verified, papers clean).

### A. Hard — build-breaking or reader-visible incoherence (fix first)

**A1 · P3: six missing figures.** ✔ **DONE (r934).** All six generated into `corpus/figs/` (`fig2_throat_circle, fig3_cubic_involution, fig6_tilted_ellipse, fig5_triple_angle, fig4_seam, fig7_curvature`) via matplotlib rendered from the papers' own math (serif/cm mathtext), each visually checked. P3 recompiles clean at 31pp with **0 missing-figure warnings**. These are **Arthur's faithful renderings** — offered for Daryl's review/replacement if he holds originals. *(The two `figures/*.png` hinge/hexagon figures and the root-diagram PNGs already existed.)*

**A2 · P5: corrupted `JanzenAlgebroid` bibitem** (L565–568). A stray `}` closes `\emph` early and a `$` closes math never opened → **real LaTeX errors** (`Missing $ inserted`, `Extra }`) and a garbled rendered title. *Needs:* replace with the canonical string used cleanly elsewhere (`…the action Lie algebroid of the symmetry-reducible sector`).

**A3 · P7: fermion "unbuilt vs now-built" contradiction.** The abstract (L211), intro (L222), and Frontiers item 5 (L927) call the fermion sector "the framework's largest unbuilt undertaking" / "no fermion sector built at all" — while the *same item* says it is "now built and forced within CR (P14)." Reader-visible contradiction, stale since P14 landed. *Needs:* thread the built-discrete-skeleton (P14) vs unbuilt-propagating-field-sector distinction through the abstract, intro, and item 5.

**A4 · P16: stale meta-correction of P15** (§network L469). P16 says it "corrects the reading carried in the cosmology paper, where the light elements were taken as inherited … lithium dissolved" — but **P15 already carries the synthesis / shared-lithium reading** (P15 abstract L95, §tensions L175/177, §discussion L323) and cites P16 as its source. A reader with both sees P16 assert P15 says X while P15 says not-X. *Needs:* reword to "the synthesis reading P15 adopts (cross-referenced there), correcting an earlier inherited reading."

### B. Substantive — matter-sector-build staleness (reader-visible, specific)

**B1 · P12 §discrete: stale generation cross-ref.** Attributes "three zero-sum weights → three generations" to P13 as a not claimed conjecture and cites **only** `JanzenBoundary`; never cites `JanzenMatter` (P14), whose thesis now *delivers* the count as "forced within CR" (and whose R=γ⁵ chirality cites *this* paper). *Needs:* add `\cite{JanzenMatter}` and reconcile the "conjectural / not built" wording with P14's delivered count.

**B2 · P13 §open L250: "does not yet supply a propagating spinor sector."** Sits in the same paragraph as "It has since been built … `\cite{JanzenMatter}`." Defensible (P14's is a bound leaf-mode, not a bulk sector to orbifold-project) but reads mildly stale. *Needs:* one clause disambiguating the two.

### C. Bibliography & hygiene (mostly mechanical; one corpus-wide pass)

**C1 · Bibitem house-style split — the big recurring one.** The corpus uses **four** styles for its own papers: "in preparation" (~10 papers — stale, they ship together), "companion paper" (P15/P4/P7…), "in the CR corpus" (P13/p0), and **"(Pn)" tokens** (P16, p0, and stray in P10/P11/P12/P13/P14). *Needs:* pick ONE house style and apply it corpus-wide (a single mechanical pass; P15's clean "companion paper" with a systematic P-number is a natural reference).

**C2 · Orphan / uncited bibitems** (defined, never `\cite`d — print as dead references): **P11** `JanzenCircle`; **P13** `HochsMathai` (a referee note also flags its venue to re-verify); **P15** `JanzenCanonicalTime`. *Needs:* cite each at its natural point of use, or drop it.

**C3 · Informal internal-file pointers in printed prose:** P3 §628 "(receipts: `verify_alpha_mass.py`)"; P11 §189 "(clean residuals; see the receipts in the consolidated derivation)". *Needs:* convert to a proper supplementary-materials reference or remove.

**C4 · P8 §323: uncited "forthcoming companion"** for the canonical formulation — the companion (P10/P11) exists and ships together. *Needs:* add the citation (or drop "forthcoming").

**C5 · p0 §landing: drifted §-anchors.** ✔ **DONE (r934).** Confirmed at source the `\S`-anchors are **line numbers** (P7 §750's verbatim quote → L917; P15 §288's "sole scale" → L313). All 14 refreshed to current, each verified against the target line's content: P1 151→175, P2 55→96, P3 2→113, P4 177→196, P7 659/662→744/746 & 746→913 & 750→917, P8 50→110, P9 51→119, P12 141→248, P13 143→262, P15 89→114 & 288→313. p0 clean 19pp. **Then enacted (r935):** Daryl handed the design call to Arthur ("what the LLM finds easiest — you're the writer and user"). Numeric line-anchors are the worst form for an LLM (no meaning on sight, lookup to act, re-drift on every edit); Arthur reaches targets by grepping content. So **all numeric anchors were converted to descriptive section anchors** (P1→"its scope note", P3→"its substrate-and-cut section", P7→"its null-boundary-correspondence section"/"its synthesis section", P13→"its closing programme-significance section", etc.) — matching the style the newer entries already used. Zero numeric `\S` anchors remain; the drift problem is structurally gone. p0 clean 19pp.

**C6 · p0 §landing L811: "stub by design"** wording — the section is now a fully populated 16-round two-way map. *Needs:* reword the stale self-description.

### D. References-completeness pass (a SEPARATE, deeper pass — Daryl's spec; not yet run)

Distinct from C (bib hygiene): the audit checked internal coherence, **not** whether every load-bearing *external* concept is referenced. Per Daryl, a first edition needs, for **load-bearing definitions and principles that aren't Google-able named things**, a reference a reader can chase; and for **significant results, a significance-reference** explaining what it overturns / why it matters (his example: the Carter-constant explanation). *Status:* not yet run — a dedicated pass (dispatchable paper-by-paper), reading each paper for un-referenced load-bearing definitions/principles + significance-ref opportunities.

### E. Non-rendered (LaTeX comments — ship only in the raw `.tex`, which the distributable programme includes)

P7 CANON NOTE header ("copilot artefact", "ASK the author"); P16 stale %-header note (a completed-chore residue). *Needs (low priority, separable):* a light pass on operating-philosophy comments before the `.tex` is distributed publicly.

---

## Part 2 — THE GENUINE OPEN PROBLEMS (below the line; the honest frontier, publishes as-is)

The audit confirms these are **correctly and clearly marked** open — the "go figure out the Higgs" category. They are the edition's *strength* (its falsifiable edges and honest frontier), not its debt. By paper, the notable ones:

- **P1:** all cosmology forward-claims held "asserted nowhere" (exemplary). **P2:** spacetime-vs-curve extension across r=0 (Sbierski conceded); info-paradox link; other-singularity analogues; third complex-z axis. **P3:** A₂-skeleton↔SM and three-fold→generations (not claimed); groupoid completeness (deferred to P5). **P4:** global maximal-symmetry as a Copernican extrapolation. **P5:** sweep-diagnostic in Kerr/RN dynamics; cross-geometry NBC component; the a2-distinct question. **P6:** the base-rate calibration of the vindication lemma (the epistemics' own "first programme").
- **P7:** the six Frontiers items — seam-crossing dynamics, the baryogenesis-analogue IC, the irreducible interior remainder, the octopole verdict, the fermion *content*, the quantum completion — plus coherence-≠-soundness. **P8:** the emergence-of-the-bend (dynamical matter, the deepest open); A/B↔foci. **P9:** off-kernel matter functionals; the wall / free-radiation frontier; the strut-free-acceleration caveat.
- **P10:** the interacting-tower definition. **P11:** no closed-form nonlinear / non-perturbative quantization; beyond-the-wall + detailed worldline dynamics. **P12:** su(3)/dimensional-rise (held both ways); general-cut anchor functionals; beyond-wall handoff; the six-hinge resonance. **P13:** mass-hierarchy, world-correspondence, the universal colour-foreclosure, empirical coherence. **P14:** the hierarchy identification, the mass values, the cosmological-side zero-mode continuation.
- **P15:** the low-ℓ/octopole falsification edge; the peak-height end-to-end transfer; the n_s/A_s progenitor-spectrum derivation; the seam-crossing dynamics. **P16:** the multi-abundance likelihood / η-derivation; the exact regulated peak. **p0:** the six-ways unification `conjecture`; the generation descent; phase-structure-at-the-seam.

**Two "needs-sharpening" (marked-open but the marking could be crisper):** P13's "does not yet supply a propagating spinor sector" (= B2 above), and p0's "stub by design" (= C6). Both are on the dangler list.

**Confirmed current (a flag that passed):** p0's §landing P16 entry *is* current to P16's synthesis/shared-lithium reading — not stale.

---

## Part 3 — The verdict: how close is the line

**Close, and bounded.** The first-edition endgame is:
1. **Four hard fixes** (A1–A4): the P3 figures, the P5 bibitem, the P7 fermion-contradiction, the P16 meta-correction.
2. **Two staleness reconciliations** (B1–B2): the P12 and P13 matter-sector cross-refs.
3. **One bibliography pass** (C1–C6): house-style, orphans, receipt-pointers, anchor refresh — mostly mechanical.
4. **One references-completeness pass** (D): Daryl's spec — the only item that is real scholarly *work* rather than cleanup, and it's dispatchable paper-by-paper.
5. **(Optional, pre-`.tex`-release)** the comment cleanup (E).

Everything else — the matter *content* (Higgs, what-an-electron-is), the quantum completion, the interior remainder, the unification verdict, the final narrative placement of the matter material — is a **genuine open problem, below the line**, published in edition 1 as the honest, marked frontier and the invitation for others to join. **No secretly-unproven claim was found.** The corpus already very nearly meets the "only genuine problems remain" bar; what stands between here and the first edition is a defined, mostly-mechanical punch-list plus one scholarly references pass.

---

## Part 4 — The limitation this audit does NOT cover (added r932, Daryl's catch)

**This audit measures coherence-against-itself, not completeness-against-intent.** It certifies that what is *in* the papers is internally coherent and dangler-free. It does **not** certify that everything *intended* for the papers is in them. Read-only readers cannot see intent — so they classify **every marked-open item as a "genuine open problem,"** and they **cannot distinguish a genuine frontier ("go compute the Higgs") from an outstanding chore we meant to finish** that also happens to read as marked-open. That distinction lives in the record of intended work and in the authors' heads (esp. the c33 physics thread), not on the page.

**Where this bites hardest: P16** (the least-worked paper, still under development when the audit ran). Source-checked: the collapse-dynamics arc (`THE_COLLAPSE_DYNAMICS_ARC.md`) reached a **qualitative** resolution baked at r883 (adiabatic heating → standard BBN → He-4/D at observed, Li-7 shared); the **exact** pieces — digit-level peak heights (arc Phase 3 = `THE_PLAN` A2.3), the deuterium yield to a number + the full multi-abundance likelihood (arc Phases 4 = A2.1/A2.5) — were **never run** and sit open, not claimed. Those are genuine frontier, correctly below the line. But whether P16 has *other* outstanding development (sections, a Phase-5 consolidation that never landed because the exact numbers weren't computed, writing c33 intended) **cannot be certified from the papers alone.**

**So the first-edition line needs a second pass the coherence audit could not do — the FRONTIER-vs-CHORE pass:** over every marked-open item in the corpus, tag each *genuine frontier* (leave it; publish as the honest open edge) or *outstanding chore* (finish before edition 1). This requires intent — Daryl's, and the arc-docs'/c33 record — not just a source read. Until it's run, "the corpus is close" is a statement about **coherence**, not about **development-completeness**. (Added to `THE_PLAN`'s first-edition line as an above-the-line requirement.)
