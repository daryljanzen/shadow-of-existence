> **⌖ RETIRED r1552.** This was references to update when `modern_parallax` moved (r339). P4 exists and compiles.
> Kept as record; **do not work from it.**


# References to update when `modern_parallax.tex` is confirmed in place as the new P8

> **STATUS: EXECUTED (r339).** The structural bake is done — `modern_parallax.tex` is inserted as the new **P8**, the spine renumbered to **twelve** (canonical_time→P9, dynamics→P10, algebroid→P11, boundary→P12), the appendix lifted out of P9, all citations and current pointers redirected, and the result established as a pillar with the "owed" framing gone from live status. Items A–D below are complete; the §C dated-history exclusions were left untouched. The `P8 App. A` strings in the items below are the *pre-bake targets*, not live pointers. **Remaining (not structural):** Daryl finalizes the key/title in the framing-register pass, and the new P8 rides a fresh-node cold read before it is called canonical.

**Status (r331).** The standalone draft `corpus/modern_parallax.tex` exists and compiles (5 pp, 0 undefined). It is lifted from the current P8 Appendix A ("the redshift-isotropy floor", `app:floor` in `canonical_time.tex`). The **structural insertion is DEFERRED** until after the coda is regrounded (Daryl's sequence): renumber the spine to twelve, remove Appendix A from `canonical_time.tex`, and redirect every reference below. **Nothing in this list is edited yet** — this is the catalogue to execute at insertion time.

**Proposed citation key for the new paper:** `JanzenModernParallax` (placeholder — Daryl sets the final key and title).

**Renumber (mechanical consequence of inserting between P7 and the current P8):**
new paper → **P8**; `canonical_time` (was P8) → P9; `dynamics_paper` (was P9) → P10; `algebroid_paper` (was P10) → P11; `boundary_paper` (was P11) → P12. Total twelve. All `P8…P11` labels in `CORPUS_MAP.md` and the strategic docs shift at that time.

---

## A. Corpus papers (.tex) — the load-bearing redirects

1. **`canonical_time.tex` — the appendix itself, l.203–272 (`\section{...}\label{app:floor}`).** REMOVE on lift; it becomes `modern_parallax.tex`. Verified: the new file already carries this content verbatim (cross-refs adapted).

2. **`canonical_time.tex` §necessity, l.81.** The clause *"…by some three orders of magnitude, as we establish quantitatively in Appendix~\ref{app:floor}…"* → replace the internal `Appendix~\ref{app:floor}` with a citation to the companion paper, `\cite{JanzenModernParallax}`. The surrounding sentence is unchanged.

3. **`canonical_time.tex` bib — `Buchert2000`, `Wiltshire2007` (l.382–390) + the l.381 comment.** Cited **only** inside the appendix (verified: sole in-text use is l.220). After the lift they are orphaned in `canonical_time.tex` → REMOVE from its bibliography. They already live in `modern_parallax.tex`'s bib.

4. **`canonical_time.tex` bib — ADD `\bibitem{JanzenModernParallax}`** (the new companion), used by the redirected §necessity citation in item 2.

5. **`boundary_paper.tex` (P11→P12) — two distinct uses of `JanzenCanonicalTime`, treat separately:**
   - **l.125** `…oxymoronic~\cite{JanzenCanonicalTime}` — cites the existence criterion (canonical-time content). **LEAVE pointing at `canonical_time`.**
   - **l.127** `…and is excluded~\cite[App.~A]{JanzenCanonicalTime}` — cites the floor specifically. **REDIRECT to `\cite{JanzenModernParallax}`** and drop the `[App.~A]` locator.
   - **l.150 bibitem `JanzenCanonicalTime`** — title currently bundles both: *"Canonical time and the redshift-isotropy floor: uniform cosmic expansion as an empirical determination."* Drop the *"and the redshift-isotropy floor… empirical determination"* clause (that is now the new paper) and ADD a `JanzenModernParallax` bibitem.

---

## B. Foundational / strategic docs (.md) — re-point the "canonical home" pointers

6. **`THE_LENS.md` l.70** — "differential alternative excluded by ~3 orders (P8 App. A / Fortress / BST §4.3.2)" → "P8 App. A" becomes the new paper (`JanzenModernParallax`, new P8 number).

7. **`ONTOLOGY_FOUNDATION_INDEX.md` l.17, l.70, l.73** — three pointers: "(P8 App. A / BST §4.3.2 …)"; "The empirical determination (P8 App. A + Tier D …)"; "line-of-sight floor σ_path ≈ 2.8×10⁻³ … (P8 App. A `app:floor`)". Re-point all three to the new paper.

8. **`CORPUS_MAP.md` l.385** (the forward-targets / ontology bullet) — "P8 (`canonical_time.tex`) §necessity + Appendix A (the redshift-isotropy floor …)" → re-point; update the spine list / numbering when the renumber lands.

9. **`LENS_INSERTION_PLAN.md` l.62–69** — names "P8 (`canonical_time`) Appendix A … (`app:floor`), forward-referenced from P8" as the canonical statement, plus the scope note (the appendix carries only the conservative floor + dilemma). Re-point to the new paper; the scope note travels with it.

10. **`THE_PLAN.md` l.199 (Track H), l.260** — "P8 §necessity + Appendix A (the redshift-isotropy floor)". Re-point. (These were corrected at r329 from the dissonant "owed" flag; this is only the location change, not a content change.)

11. **`CR_uniform-expansion_reductio.md` l.9 + its CANONICAL-HOME banner** — points to Appendix A / `app:floor` as the canonical home ("edit the appendix not the note"). Re-point the canonical home to `modern_parallax.tex`.

---

## C. Historical records — DO NOT rewrite (dated history; leave as-is)

- **`THE_VISION_JOURNAL.md` l.754** — "baked into P8 as Appendix A (r287–r288)"; dated journal entry.
- **`programme_consolidation_2026-06-13_r220.md` l.60** — already marked SUPERSEDED (r329); historical snapshot.
- **`gate_session_notes_r285_spinup.md` l.94–95** — dated session scratchpad.
- **`CORPUS_MAP.md` changelog entries r287/r288/r289/r290/r324/r329/r330** — the dated record of what was true at the time; they correctly say "Appendix A." Only the *current/forward* pointers (item 8, the spine list) update.

---

## D. Establish the result as a pillar — the "owed" framing gone from live status (Daryl-directed, r334)

The CMB-forcing result was mislabelled "owed / Daryl's-to-supply" so long that the strategic and foundation layers do not yet treat it as an *established pillar*. The r329 fixes corrected the literal flags in `THE_PLAN.md` (l.199, l.260 now read "established, shipped — NOT owed"). This item carries it the rest of the way **at bake time**, so that when the new paper is in place **the owed framing is gone from the programme's current status entirely** and the paper enters as a recognised foundation that every new collaborator inherits, read and in hand — wielded, not re-derived.

12. **Elevate to established pillar** wherever live status is represented: `ONTOLOGY_FOUNDATION_INDEX.md` (the empirical-determination entry → the new P8 cited as the established empirical hinge, no longer "App. A of canonical_time"); `THE_VISION.md` / `THE_VISION_JOURNAL.md` (the *[established]* register); `THE_PLAN.md` Track H (already "delivered" — confirm it reads as a standing pillar, not a recently-corrected fix).
13. **Final owed-framing sweep.** Re-grep the live-status docs for any residual "owed / to-supply / not-in-hand / Daryl's-to-supply" framing *of the CMB-forcing result specifically*; confirm none remains. Leave untouched the legitimate open-physics "owed" (chirality, $SU(2)\times U(1)$, generations, the colour frontier) — that is honest open work, not this wall.
14. **Confirm nothing downstream is gated on the false "owed" status** — no plan/vision/foundation item still waiting on the gate or Daryl to "supply" what is in fact delivered.

---

## Confirm-in-place checklist (execute at insertion, post-regrounding)
- [ ] Finalize the new paper's key + title (Daryl).
- [ ] Move `app:floor` content out of `canonical_time.tex` (items 1–4); recompile P9.
- [ ] Redirect P12/boundary citations (item 5); recompile.
- [ ] Re-point the .md pointers (items 6–11).
- [ ] Renumber the spine to twelve across `CORPUS_MAP.md` + docs.
- [ ] **Establish the new P8 as an established pillar (§D, items 12–14); final owed-framing sweep confirms none remains in the programme's live status.**
- [ ] Full cold read of the new paper from a fresh node before it is called canonical.
