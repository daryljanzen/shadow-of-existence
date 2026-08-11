# The Bibkey Map — the unification is DONE; one canonical key per paper is now CORRECT

> **⚑ STATUS CORRECTED r1624 (Daryl-directed: "There should be no aliases. We fixed that.").**
> **Verified exhaustively at source this revision:** all six private aliases —
> `JanzenCausality`, `JanzenParallax`, `JanzenShadow`, `JanzenFramework`, `JanzenCanonical`,
> `JanzenCosmology` — have **zero uses and zero `\bibitem` definitions** anywhere in the corpus.
> The corpus now carries **exactly seventeen canonical Janzen keys, one per paper**, and
> `scripts/depmatrix.py`'s key list is those seventeen exactly — checked, complete, correct.
>
> **This document previously opened with the rule** *"A citation topology built on one bibkey per
> paper is WRONG in this corpus"* **and instructed that it be read before any citation or
> dependency-matrix work. That is now the opposite of the truth, and it is struck.** One key per
> paper is right. Nothing here should send a node hunting for aliases that no longer exist, or
> cause it to distrust a correct absence-claim.
>
> **What this document is now:** the record of a defect that was found, why it mattered, and the
> one methodological rule that outlives it.

## The rule that survives — and it is general, not about aliases

> **Absence of a match in a grep window is not absence of a citation.** Before concluding that
> paper X does not cite paper Y, widen the window and **read the site at source.** Twice in the
> r908 session a truncated grep produced a false *"uncited"* report; both were cited at the point
> of use. See `CODA_FIELD_NOTE.md`, the grep faces.

*This rule is why the document is kept. The hazard it was written against is gone; the habit it
teaches is not tied to aliases and has since caught other things.*

## Still live, and a real trap — DISTINCT works, do not merge

These are **not** aliases and never were. Merging any of them into a corpus paper's key would be a
genuine error, and two of the pairs are close enough to invite it:
- `JanzenShadowReading` — *Shadow Reading* (the epistemic method), cited by P6. **Not** P6's own key
  `JanzenShadowExistence`.
- `JanzenSettingRecord` — *Setting the Record Straight* (the historiographic example), cited by P6.
- `JanzenThesis`, `Janzen2025`, `Janzen2015`, `Janzen2012`, `Janzen2014` — the dissertation, the book
  (*Beyond Space-Time*), and the journal precursors.
- `JanzenWildGoose`, `JanzenTrope`, `JanzenMisconstrue`, `JanzenFortress` — the conceptual-boundary
  and epistemic-engine essays.

## HISTORICAL — the alias table as it stood (all six now dead)

*Kept as the record of what was fixed, not as a thing to check. Built r908 from source because two
absence-claims that session were wrong for exactly this reason: p0 appeared to cite P1 zero times
and P4 zero times, and in both cases p0 was citing them under a private alias.*

### The (former) alias table — canonical ← alias · **ALL SIX DEAD, verified r1624**

| Paper | Canonical bibkey (used by 7–16 papers) | Alias | Alias used by |
|---|---|---|---|
| P1 `BH_causality_v2` | `JanzenBHcausality` | `JanzenCausality` | **p0** |
| P4 `modern_parallax` | `JanzenModernParallax` | `JanzenParallax` | **p0** |
| P6 `shadow_of_existence` | `JanzenShadowExistence` | `JanzenShadow` | **p0** |
| P7 `CR_framework` | `JanzenCRframework` | `JanzenFramework` | **p0**, **P14** |
| P10 `canonical_time` | `JanzenCanonicalTime` | `JanzenCanonical` | **p0** |
| P15 `CR_cosmology` | `JanzenCRcosmology` *(also `JanzenCosmology`)* | `JanzenCosmology` | **p0** |

~~**So: p0 carries a private alias set for six papers.** P14 also uses `JanzenFramework`.~~
**No longer true (r1624): p0 and P14 both use the canonical keys throughout; every alias above is unused and undefined.**

**`JanzenCRcosmology`** is P15's single canonical key — 56 uses, defined in eleven papers. *(r1624: this
entry read that P15 must be resolved as **either** `JanzenCRcosmology` **or** `JanzenCosmology`. `JanzenCosmology`
now has zero uses and zero definitions, so there is nothing to resolve — P15 is `JanzenCRcosmology`, full stop.)*

### (historical duplicate of the distinct-works list above — kept with the r908 record)
- `JanzenShadowReading` — *Shadow Reading* (the epistemic method), cited by P6.
- `JanzenSettingRecord` — *Setting the Record Straight* (the historiographic example), cited by P6.
- `JanzenThesis`, `Janzen2025`, `Janzen2015`, `Janzen2012`, `Janzen2014` — the dissertation, the book
  (*Beyond Space-Time* / ontological foundations), and the journal precursors. Distinct sources.
- `JanzenWildGoose`, `JanzenTrope`, `JanzenMisconstrue`, `JanzenFortress` — the conceptual-boundary and
  epistemic-engine essays (Tier C / Tier D). Distinct sources.

## How to build a correct reverse-dependency topology
```
# for target paper Y with canonical key K and alias set A:
for f in corpus/*.tex; do
  n=$( { grep -o "cite[a-z]*{[^}]*K" "$f"; grep -o "cite[a-z]*{[^}]*A1" "$f"; ... } | wc -l )
done
# then READ each apparent zero at source before calling it a gap.
```

## Known title drift (a separate defect — the shared-structural-detail sweep, plan step 5) — RESOLVED r908
Bibitem *titles* for the same paper differ across the corpus, and go stale when a paper's title is
upgraded. Instances found and fixed:
- **P4's title** changed at r901 (gaining "and the measured resolution of the relativity of simultaneity")
  and **nine papers** still carried the old title — repaired r904.
- **P6's title** ("…**scientific** theory-choice as an empirically grounded discipline…"): P15 alone had
  dropped "scientific" — **repaired r908.**
- **P7's title** ("Collapsed matter must become a universe: …") was stale in **thirteen** papers (still
  "Cosmological Relativity: a layered geometric framework…") — **all repaired r908.**
- **Full standardisation, r908 (Daryl: "Standardise"):** built `corpus/CANONICAL_TITLES.txt` (the
  authoritative table, from each paper's own `\title{}`) and rewrote **40 bibitem titles across 9 papers**;
  an independent checker reports **zero mismatches**; all 17 papers compile clean. Two titles the assistant
  itself invented at r905 (P5→P14, P12→P16) were caught and fixed in the same pass.

**Standing rule — whenever a paper's title is upgraded, sweep every bibitem in the corpus for the old
string** (`CANONICAL_TITLES.txt` is the reference for the current strings).
