# `r7411` ① — PRICING THE CENSUS REFRESH, REGISTERED BEFORE THE COUNT

**Pushed before the scan runs.** *The order's ceiling is one revision and says the registration is the
deliverable even if the count is not, so this file stands alone.*

## WHAT IS ASKED

> *"how much of `items_keyed.tsv` is actually invalidated by the revisions since `r7371`? … **the stale
> fraction and the stale *weight* are different numbers and I want both**."*

⛔ **And what is NOT asked: running the refresh.** *`69` reads the papers and `69` runs only when Daryl
prompts. This prices it and performs none of it.*

## THE TEST, AND IT IS THE CENSUS'S OWN RULE RATHER THAN A NEW ONE

`items_keyed.tsv`'s key is **`(paper, normalised marker sentence)`** — `check_prose_pins`' rule one level up,
and the gate's header says so in terms. Its own law: ***an expression that is reworded is a NEW site and must
be read again.*** ⇒ **A row is INVALIDATED iff its normalised marker sentence no longer appears among the
candidates `key.py`'s extraction finds in that paper now.**

⌗ ⛭ **A row whose paper moved but whose sentence survives is NOT stale, and that is the entire point of the
content key.** *`69`'s census used a paragraph INDEX; `r7371` ⑥ re-keyed it on content precisely so that an
edit elsewhere in a paper does not invalidate every row after it. This measurement is the first test of
whether that purchase was worth anything — if nearly all 93 at-risk rows turn out stale, the content key
bought nothing over the index.*

Measured with `key.py`'s own `body()`, `PAT` and `marker_sentence()`, imported rather than re-implemented.

## THE POPULATION AND A HARD BOUND, BOTH BEFORE ANY TEST RUNS

`items_keyed.tsv`: **`257` rows, `80` classed `OPEN`** by `69` (of which `75` are direction ⒜'s orphans, so
`5` do point at live rows).

**Four paper sources changed between `4a7a46e3` — the commit that added `items_keyed.tsv` at `r7371+cc66.46` —
and `origin/main` at `r7411`:** `CR_cosmology` (P15), `CR_framework` (P7), `cosmogenesis_paper` (P16),
`groupoid_paper` (P5). ⇒ ***`66`'s premise is confirmed, and it is a hard ceiling: only a row in a moved paper
can be invalidated.***

| | rows | `OPEN` rows |
|---|---|---|
| P15 | 35 | **25** |
| P7 | 40 | 6 |
| P16 | 11 | 5 |
| P5 | 7 | 0 |
| **at risk** | **`93` of `257` = `36.2` %** | **`36` of `80` = `45.0` %** |
| not at risk | 164 | 44 |

⌗ ⛭ ***The two ceilings already differ in the direction `66` predicted*** — the weight ceiling (`45.0` %)
exceeds the row ceiling (`36.2` %), because `P15` is both the most-edited paper and the one carrying `25` of
the `80` opens. *That is a property of the population, not a result; the bands below are about how far under
these ceilings the answer falls.*

## THE BANDS, BEFORE THE SCAN

| | | central | band |
|---|---|---|---|
| ⒜ | **stale rows** of the 257 | **8** | **3 – 25** |
| ⒝ | stale **fraction** | **3.1 %** | 1.2 – 9.7 % |
| ⒞ | **stale weight** — stale rows among the `80` `OPEN` | **4** | **1 – 14** |
| ⒟ | the stale weight's share **exceeds** the stale row share | **YES** | — |
| ⒠ | **my own** `.61`/`.62` edit to `CR_framework.tex` invalidates a row | **NO** | — |
| ⒡ | **NEW candidates** — paragraphs matching now, absent from the census | **10** | **3 – 30** |

**Reasoning:**

⒜ The revisions since are `66`'s targeted paragraph-level corrections (`r7387`, `r7401`, `r7405`, `r7407`,
`r7409`) plus my own matrix row. Each touched a handful of paragraphs, not a paper. ⑩ measured the corpus as
80.0 % ± 5.9pp owing nothing, so the editing rate is low; `93` is a ceiling I expect the answer to sit far
under.

⒞ `P15` took the most edits and carries `25` opens, so the weight is where the risk concentrates — but
`r7405`/`r7407` rewrote *status* prose, and a status rewrite is exactly what moves a marker sentence. Central
`4` of `80` with a long upper tail.

⒠ The matrix row is inside a `tabular`; `key.py` splits on blank lines and keeps only paragraphs matching its
openness vocabulary, and a row of digits carries none. **If this is wrong I invalidated a census row while
fixing a different staleness, and I would rather have predicted it than discovered it.**

⒡ ⛭ **`66` did not ask for this one and the price is wrong without it.** The refresh's cost is *stale +
new*: a paragraph that now matches the vocabulary and is in no census row has never been read by `69` at all.
⌗ *It is also the number that decides whether a positional re-key is even possible: `key.py` asserts
`len(cands) == len(data)` and refuses to force a positional join, so any non-zero ⒡ means the index route is
shut and the content key is the only one left.*

## WHAT THIS PRODUCES

**A price in rows, with the per-paper split, and nothing re-read.** ⇒ *Whether the refresh happens once at the
end or in stages is `66`'s call on these numbers; I am not recommending a schedule I cannot cost in `69`'s
time.*
