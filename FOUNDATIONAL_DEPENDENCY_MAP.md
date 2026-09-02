# Foundational Dependency Map — P1–P7 at source (r623)

*Extracted at source (internal `\cite` matrix over the six papers + P7), post-r620 physics-first numbering. Counts are citation multiplicities, a proxy for load-bearing weight. Stated for reversal; this is a reading instrument for the spine order, not a claim over any paper.*

**Post-swap numbering:** P1 `BH_causality` · P2 `janzen_circle` · P3 `SdS-slicing-curve` · P4 `modern_parallax` · P5 `groupoid_paper` · P6 `shadow_of_existence` · P7 `CR_framework`. Cite-keys are semantic (unaffected by numbering).

## The internal DAG (who depends on whom, among P1–P6)

Backward edge = dependency runs with the order (✓ consistent). Forward edge = a "developed-in-the-companion" pointer unless it is a genuine dependency (only P4↔P5 was, now fixed).

| paper | depends on (backward, load-bearing) | forward-points to (pointer, not dependency) |
|---|---|---|
| **P1** wedge | — (root; depends on none of P1–P6) | P2, P3, P4 (×1 each — "developed in…") |
| **P2** circle | **P1 ×9** | P3 ×13 (the companion generalisation), P6 ×2 |
| **P3** slicing | **P2 ×3**, P1 ×1 | P5 ×5 (the groupoid develops its relational content), P6 ×1 |
| **P4** modern_parallax | **— (co-equal root)** ‡ | P6 ×1 |
| **P5** groupoid | **P3 ×33, P2 ×9, P1 ×3, P4 ×4** | P6 ×1 |
| **P6** shadow | **P1 ×2, P4 ×4, P5 ×1** | — |

**‡ CORRECTION (r626, Daryl caught it, verified at source) — P4→P1 is complementarity, NOT dependency; P1 and P4 are TWO CO-EQUAL FOUNDATIONAL FORCINGS.** The r623 table counted P4's three references to P1 as a dependency (P4 "depends on P1"). Read at source, all three are the opposite of a dependency — they are lateral *complementarity/independence* references: P4 §79 calls itself "the empirical counterpart of the conceptual results of the companion papers~[P1]"; P4 §90 and §177 (verbatim) say the P1 result "stands on causal structure alone and **needs none of the cosmological evidence**." And P1 §300 already reciprocates: "the enduring cosmic time that existence requires is itself empirically forced~[P4]; the present paper reaches the distinction **from standard general relativity alone**." So **P4 depends on nothing** — it is a *second root*, co-equal with P1. The two are **two independent forcings of one cosmic foliation**: P1 a **structural** forcing (local causal structure / the horizon metric-singularity, from GR alone) and P4 an **empirical** forcing (the redshift-isotropy floor / precision cosmology and its structural consequences). Each paper cites the other exactly to mark that it needs none of the other's evidence — the citation topology is *symmetric complementarity*, and it was already in the corpus at source; only this map (and the r624 graph, now redrawn) had mischaracterized it. This strengthens the cross-product: not one root branching, but **two co-equal roots**, laterally complementary, both feeding the convergence.

## What it says (read as it fell, including what complicates the clean line)

1. **The P4↔P5 swap is vindicated at source.** P5 (groupoid) depends on P4 (modern_parallax) ×4; P4 does **not** depend on P5. Post-swap that heavy edge runs **backward** (P5→P4) — the inversion is fixed, and it was the *only* one.

2. **The order P1–P6 is now dependency-consistent.** Every load-bearing dependency runs backward against the post-swap numbering. **No further reordering is forced among P1–P6.** The forward citations (P1→P2/3/4, P2→P3, P3→P5) are all companion "developed-in" pointers, not inversions — the real dependencies run the other way.

3. **It is a cross-product, not a line — and here is the actual shape.** P1 is the root, and it **branches into two streams**:
   - **the geometry stream** — P1 → P2 → P3 → P5 (groupoid the algebraic terminus, leaning hardest on P3 ×33);
   - **the empirical stream** — P1 → P4 (modern_parallax), which depends on **P1 only**.
   These **converge**: the groupoid (P5) pulls in the empirical foundation (P4 ×4); the epistemics (P6) pull from both (P4 ×4, P5 ×1) plus P1; and P7 gathers all six.

4. **The honest complication (the edge that does *not* fit the naive linear grouping).** P4 (modern_parallax) at position 4 depends only on P1 — **not on P2/P3**, the "local geometry" right before it. So "P1–3 local geometry, P4–5 cosmological" is a fine *reading/presentation*, but it is **not a dependency chain**: P4 is a **parallel foundation stream from P1**, not a continuation of P2/P3. The physics-first *order* (P4 before P5) is correct and vindicated; the two are different streams, not one line. This is the cross-product's real texture, and it is more interesting than the clean line.

   **Both directions, stated to avoid a misread.** The above is about what P4 *depends on* (its foundations — few, as befits a foundation). In the *other* direction P4 is a **major feeder**: it is depended on by P5 (×4), P6 (×4), and P7 (×11) — **19 citations across three downstream papers**, *more* than P2 (16, into P3/P5/P7) though below the wedge P1 (37, into all six). Few dependencies, many dependents — the signature of a foundation, not an orphan. P4 hits everything past P3 directly.

## The feed into P7 (the compounding)

P7 draws **directly on all six**, heaviest on the two foundations:

**P1 ×19** · **P4 ×10** · P5 ×7 · P6 ×7 · P3 ×6 · P2 ×4

This *is* the compounding: P7 is not the end of a chain receiving one accumulated input — it is the **convergence node** taking each of P1–P6 as a direct numbered datum (F1–F6 in `sec:central`), leaning hardest on **P1 (the crisis wedge, ×19)** and **P4 (the empirical forcing, ×10)**. P1's content reaches P7 both *through* the geometry chain and *directly* (the NBC's use of the horizon's null structure) — the compounding par excellence: the root feeds the convergence without the intermediate papers as intermediary.

## Adjudication for the spine order

- **P4↔P5: swap correct, already landed (r620).**
- **No further reordering forced among P1–P6** by the DAG. The branching (two streams from P1) is a *structural reading* to carry in the map, not a reorder — a line cannot express it, but the numbering P1–P6 is dependency-consistent as a linearisation of the branch.
- **Still open (the larger arc, held):** the P12→P14 internals; the border/capstone's placement is now settled (**p0/16** since r796, when the matter sector earned p15) — a separate extraction; this map covers P1–P7 only.
- **The gravitational-entropy point** (`OPEN_PROBLEMS_MAP` r618) sites naturally in the **empirical stream at P4** (modern_parallax, the physics-first foundation): the observed arrow toward collapsed states is of a piece with the redshift-isotropy forcing — both are what the *observed world* forces. Candidate home confirmed as P4 or an adjacent frontier; not claimed depth until worked.

*Extracted r623 at source; stated for reversal.*
