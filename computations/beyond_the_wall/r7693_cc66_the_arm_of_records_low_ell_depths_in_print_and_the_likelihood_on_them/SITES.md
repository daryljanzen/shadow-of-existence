# `r7693` (cc66) — ITEM 2: **EVERY SITE THAT PRINTS A DEPTH, THE LIKELIHOOD OR THE CROSS-VALIDATION**

Built by **searching** for each printed value and clause across all three papers and the figure's
generator, not by working down the order's list — *registered in advance as the risk, because my `r7679`
defect was a sentence resting on a number no gate read and its mirror here is a printed figure I fail to
find.* ⇒ **The order names ten sites. The search finds the same ten and FOUR MORE, all generated.**

## THE FIGURES, ALL COMPUTED IN THIS REVISION AND NONE TAKEN FROM THE ORDER TEXT

| quantity | in print | arm of record | pinned in |
|---|---|---|---|
| depths ℓ = 2–8 | `0.487 0.435 0.359 0.666 0.911 0.983 0.998` | **`0.478 0.459 0.358 0.651 0.906 0.982 0.998`** | `…depth_gap_closes…` (this revision) |
| ℓ = 4 at **two** places | `0.36` | **`0.36` — UNCHANGED** | same |
| cross-validation | `3 %` except the octopole at `5.5 %` | **worst `2.92 %` at ℓ = 4, no exception; octopole `1.10 %`; above ℓ = 5 under `0.25 %`** | same |
| the split's octopole shift | — | **`+0.029`** | same (`r7691`) |
| likelihood total | `+1.58` | **`+1.44`** | same |
| per multipole | `−2.5 +1.0 +2.0 +1.0` | **`−2.60 +0.74 +2.05 +1.18`**, nothing above | same |
| octopole-estimator range | `+0.2` to `+3.4` | **`+0.2` to `+3.1`** | same |

⛔ **`+2.05` IS A ROUNDING-CONVENTION QUESTION AND NOT A MEASURED ONE.** *At one decimal place it is
`+2.0` half-to-even and `+2.1` half-up, and `sec:largescale` states no convention. **69's to settle; I
will not pick it silently.*** Pinned at three places, where the question does not arise.

## THE TEN SITES THE ORDER NAMES

**①  `P15` l.134** (the overview). Prints `0.36`, `0.487`, `0.435`, and the cross-validation clause
*"agree to three per cent at every multipole but the octopole, and to five and a half per cent there"*.
⌗ **`0.36` SURVIVES** — `0.359` and `0.358` both round to it. *So this site loses two figures, not three,
and a redraft that changes `0.36` would be introducing an error rather than removing one.*

**②  `P15` l.2592** — `fig:lowL-floor`'s **caption**. Prints all four of `0.487 0.435 0.359 0.666` and
the same cross-validation clause. ⇒ ✔ **THE FIGURE ITSELF NEEDS NO REGENERATION.** *Read out of
`computations/perturbation_figures.py`: `fig_lowL_floor` computes `ratio = D_C/r0` and
`ellL = sqrt(L(L+2))·ratio` and plots those against mode degree, plus a **shaded band** labelled "observed
large-angle deficit". **No depth appears in its plotted data at all.** The depths live only in the prose
of the caption.* ⌗ *The order asks whether the figure needs regenerating and from what; the answer is
**no**, and it is the caption that carries the figures.*

**③  `P15` l.2604** — prints `0.487 0.435 0.359 0.666`.

**④  `P15` l.2608** — prints the same four, the cross-validation clause, **and** `r7691`'s landed clause
*"the excess being the two-clock split's and not the tower treatment's"*. ⌗ *That clause is **unaffected**:
it is about the split, which is exactly what the re-point keeps.* ⚠ *The order places this clause at
l.2600; l.2600 carries the late-ISW sentence and prints no depth. **Reported rather than silently
corrected** — a line number is a fact about a tree.*

**⑤  `P15` l.2810** (`sec:largescale`) — prints `0.487 0.435 0.359 0.666`.

**⑥  `P15` l.2814** — the likelihood: `+1.58`, *"the same to the digit over `2 ≤ ℓ ≤ 10`"*, the range
`+0.2` to `+3.4`, and the per-multipole `−2.5`, `+1.0`, `+2.0`, `+1.0`. ⌗ **The "same to the digit" clause
is a claim about the 8-vs-10 agreement, NOT about the value, and it SURVIVES** — gated this revision as
two separately computed sums rather than inferred from the total.

**⑦  `P15` l.2821–2822** — prints **all seven** depths and the full cross-validation clause, including
*"and to one per cent above ℓ = 5"*. ⌗ *That last limb survives with room: the one-clock comparison is
under `0.25 %` above ℓ = 5.*

**⑧  `P7` l.778** (`corpus/CR_framework.tex`) — prints `0.487 0.435 0.359 0.666`.

**⑨  `P18` l.1494** (`corpus/CR_synthesis.tex`) — *"the two transfers agreeing to three per cent away from
the octopole, and to five and a half per cent at it"*. **Prints no depth** — the cross-validation clause
only.

**⑩  `fig:lowL-floor`'s plotted data** — see ②: **there is none to change.**

## ⚑ AND FOUR SITES THE ORDER'S LIST DOES NOT NAME, ALL GENERATED

| file | line | what it carries |
|---|---|---|
| `corpus/appendix_receipts_P15.tex` | 156 | the depth receipt's INDEX entry, carrying `0.487 0.435 0.359 0.666` |
| `corpus/appendix_receipts_corpus.tex` | 769 | the same entry in the corpus-wide appendix |
| `corpus/appendix_receipts_P15.tex` | 986, 993 | the depth-**gap** receipt's entry, carrying `3 per cent` and `3.4 becomes 4.2` |
| `corpus/appendix_receipts_corpus.tex` | (same entry) | ditto |

⇒ ✔ **These are NOT hand-drafted.** *They regenerate from `corpus/make_all_appendices.py` once the
receipt's INDEX row changes, and `check_appendix_current` is what proves it was run.* ⌗ **But they are
listed, because "every site" means every site: a generated file carrying a stale figure is still a paper
printing a wrong number, and the thing that makes it right is a command, not a draft.**

## WHAT NEEDS REGENERATING, AND FROM WHAT

| artefact | regenerate? | from |
|---|---|---|
| `corpus/lowL-floor.png` | **NO** | *its plotted data contains no depth* |
| `corpus/appendix_receipts_P15.tex`, `…_corpus.tex` | **YES** | `corpus/make_all_appendices.py`, after the INDEX row moves |
| the PDF of any paper whose appendix moved | **YES** | the paper's own compile |
| `P15`, `P7`, `P18` prose and the caption | **hand-drafted** | the table at the top of this file |

⌗ **P7 and P18 are touched, so this is a three-paper edit and not a `P15` one** — *which is a cost worth
naming before it is discovered at the compile step.*
