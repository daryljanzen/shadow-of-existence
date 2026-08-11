> **⌖ RETIRED r1552.** This was a cold-read setup for P13 (r533). P13 exists and compiles.
> Kept as record; **do not work from it.**


# Cold Read — P13 (`scalar_perturbations_paper.tex`) — Kickoff
### Bundle r533. An independent cold read of one paper. You are owed only the operational green light.

You are a fresh reviewer. Your whole value is **not knowing where this work is meant to be going, or whose it is.** Do not seek that out. Read the paper, and the sources its argument leans on, as they actually are.

## The method (binding — follow it exactly)

Use the two-pass procedure in **`KICKOFF_CODA_REVIEW.md` → "The procedure"**: 

- **Pass A — understand.** Read P13 in full to understand it on its own terms; write a faithful account of what it sets out to show, how the argument runs, and what it actually establishes. **No evaluation** — set aside any critique that forms.
- **Hand Pass A back and stop.** The understanding is confirmed faithful before Pass B begins.
- **Pass B — review.** Only then evaluate, reasoning **from your own Pass A account**, holding it open beside the paper. Quote the source for every finding. A finding that contradicts your Pass A understanding is the signal to stop and reconcile, not to report (the disqualifying test). The wall runs both ways: critique must not leak into Pass A, and the Pass A understanding must not drain out of Pass B.

That method is current and binding. **One correction to that file:** its "What to read" list carries an older paper numbering — ignore that list and use the map below.

## The current corpus map (use this for order/context only)

Fourteen papers, P1–P14 (filenames in `corpus/`):

P1 `BH_causality_v2` · P2 `janzen_circle_v3` · P3 `SdS-slicing-curve_v2` · P4 `groupoid_paper` · P5 `modern_parallax` · P6 `shadow_of_existence` · P7 `CR_flatLCDM_v2` · P8 `slicing_operator` · P9 `range_paper` · P10 `canonical_time` · P11 `dynamics_paper` · P12 `algebroid_paper` · P13 **`scalar_perturbations_paper`** · P14 `boundary_paper`.

`CORPUS_MAP.md`'s papers list is the authority for the spine. **Do not read** `CORPUS_MAP.md`'s top "CURRENT STATE" banner or its changelog — those are programme self-knowledge, not part of a cold read.

## Your assignment

**Cold-read P13, `corpus/scalar_perturbations_paper.tex`.**

## The source-vetting gate (part of the method)

Read a cited source in Pass A **only where your account of P13 would bear weight on that source's content** — not for citations P13 only mentions in passing. Transcribing "P13 says source X establishes Y" as something you vouch for, without reading X, is a manufactured receipt; but a bare citation you are only noting stays a citation. For P13, the sources its account leans on, in rough order of weight:

- **P7 `corpus/CR_flatLCDM_v2.tex`** — the framework P13 builds on: the layered ontology, the causal reassignment of de Sitter space, the Null–Boundary Correspondence, and the results P13 states it "builds upon, not reopens." (P13 leans on this heavily.)
- **P5 `corpus/modern_parallax.tex`** — the empirical forcing of the rate, and the Sachs–Wolfe / integrated-Sachs–Wolfe decomposition P13 uses in its low-multipole transfer.
- **P11 `corpus/dynamics_paper.tex`** — the tensor-sector companion P13 positions itself against.
- **The proper-frame derivation** P13 describes in five steps (`Janzen2015` in P13's references) — read its content insofar as your account of P13's §"The proper-frame cosmology, derived" bears weight on it.

Lighter pointers — read only if a specific Pass B point turns on them: P3 `SdS-slicing-curve`, P8 `slicing_operator`, P9 `range_paper`.

## The why-layer — never read for this review

Their whole content is where the work is meant to go and whose it is; reading them collapses the cold read into an echo:
`THE_CODA.md`, `CODA_FIELD_NOTE.md`, `THE_INTERFERENCE_ENGINE.md`, `DEMONSTRATING_THE_WAY.md`, `THE_VISION.md`, `VISION_FIELD_GUIDE.md`, `THE_VISION_JOURNAL.md`, `THE_SYNTHESIS.md`, and `CORPUS_MAP.md`'s "CURRENT STATE" banner and changelog. Also do not seek any framing of this paper's intended status beyond the assignment above.

## Setup

```
mkdir -p /home/claude/cr && cd /home/claude/cr
tar xzf /path/to/cr_bundle_r533.tar.gz --strip-components=1 -C .
ls corpus
```
Read files by named path; do not dump directory trees.

## Green light

Produce **Pass A** (the faithful understanding) first and hand it back. After it is confirmed, produce **Pass B** (the review), every finding quoted at source. That is the whole task.
