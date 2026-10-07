# r7209+70.1 — results against `PREDICTION.md`

## G1 — `check_order_acknowledged`: a real design defect, and it had `main` red at the time of the review

- **(a) MISSED.**  Replaying the gate's own revision lag over `main`'s last 400 first-parent commits gives:

  | seat | 66's figure | my replay |
  |---|---|---|
  | cc66 | 6 | **24** |
  | 60 | 5 | **8** |
  | 69 | 2 | **8** |
  | node 70 | 18 | **20** |

  So `LAG_CEILING = 6` sits below what reading seats actually reached.  (`g1_lag.py`, `g1_log.txt`.)
- **The live consequence.**  At `HEAD` the gate is red over **69 and cc66, lag 8 each**, and it turned `main`'s
  fast job red.  Both are working seats.  They fell 8 behind because **r7207 and r7209 are one broadcast, written
  word for word into all four order files**, and each section 66 writes advances the order revision.
- **(b) HELD.**  60 at `HEAD` reads as acknowledged at `r7220` from a MENTION in its reply file.  Its newest reply
  heading is `r7218`.
- **Neither revision lag nor a count of sections separates the cases.**  My real silence peaked at 5 unanswered
  sections, and cc66 also reached 5 at `97636d38`, when it was replying.
- **What does separate them: count only a seat's OWN sections, excluding any heading that occurs verbatim in
  another seat's order file** (`g1_broadcast.py`).
  - At `HEAD`: cc66 1, 69 1, 60 0, 70 0.
  - My silence at `14ba3b93`: **5**.
  - Over 400 commits, the only values above 1 for a reading seat are cc66 5 (`09-30`) and 60 3 (`10-01`).  Both
    predate `fdd0a26f` (`10-05`), the convention that replies name the revision they answer.
  - **Ceiling 3** separates the cases with margin.
- **Rewritten, because `r7207` and `r7209` offered it.**  The fail is now on own-section count; the revision lag is
  printed and no longer fails.  The seeds (`seeds_g1.py`, `seeds_g1_log.txt`) all HELD:
  - S1, the real defect at `14ba3b93`: 70 is flagged at 5.
  - S0, `HEAD`: green.
  - S2, four new sections to 69 alone: red.
  - S3, four broadcasts to all four seats: green.
  - S1's first run read rc 1 with no `[FAIL]` line.  At that commit 69's reply file did not exist, and the gate's
    missing-pair check returns first.  The 70 row is flagged, and the seed now reads that row.

## G2 — `check_pages_render`: blind to source leaking through, and it does leak, but rarely

- **2 leaks in 2 pages** (`g2_log.txt`):
  - a raw `\section{The Λ-completed vacuum as the universa…}` in `paper_P17.html`'s text;
  - a raw `\end{quote}` in `paper_P5.html`'s.
- **MISSED on the count (10-200).  Held on "real but rare".**  Both are true generator defects that an
  emptiness-only gate cannot see.  Routed, not repaired here: the generator is 66's.

## G3 — `check_floats_carried`: MISSED, and the apparent hit was my own counter's error

- The first count put P7 at 26 display environments in the source against 22 on the page.
- **Four of the 26 are `\\[2pt]`-style row spacing inside `tabular`**, which my `\[` pattern counted as display
  math.  Corrected, it is **22 = 22**.  The other 17 papers already matched exactly.
- ⇒ **No page drops display math.  G3's prediction missed.**

## Scored

| | predicted | measured | |
|---|---|---|---|
| G1a worst lags reproduce 66's | within 1 | cc66 24, 60 8, 69 8, 70 20 | **MISSED** |
| G1b a seat closed by a mention | at least one | 60 (mention `r7220`, heading `r7218`) | held |
| G2 leaked text nodes | 10-200 in 2-8 pages | **2** in 2 pages | **MISSED** (count); held (pages) |
| G3 a paper drops display math | at least one | none, after correcting my counter | **MISSED** |
