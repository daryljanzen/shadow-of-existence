# r7227+70.1 — widening `BARE`: results (node 70)

Pre-registered at `PREDICTION.md` (`1cd11637`) before any subject was counted.

**Population.** 4,777 unique commits reachable from every ref. All ten remote branches were fetched, and the
clone is not shallow.

**Scripts.**
- `measure.py`: three patterns over every ref (output in `measure.json`).
- `classify.py`: the 232 newly caught subjects, classified (output in `newly_caught.tsv`).
- `old_form_baseline.py`: the same reading applied to what the old pattern already catches.
- `variants.py`: narrower widenings.
- `collisions_widened.py`: what `collisions()` reports under each pattern.
- `any_only.txt`: the rival "anywhere" pattern.

## Verdict: the widening does not land, and the stopping rule decides it

The HEAD form drops the dash and keeps the head anchor. It newly catches **232** subjects.

**74 of them are citations rather than claims**: 34.1 % of the 217 that come after the band was taken. My
pre-registered limit was 5 %. Most come from a seat writing, at the head of its subject, the number of the order
it is answering:
- `r7219 acknowledged: …` (60);
- `r7109 ⓷: …` (cc66);
- `r7223 reply: …`;
- `r7043 (70) working …` (this seat, before it switched to the suffixed form).

**The control** is the old pattern, which needs the dash directly after the id. Read the same way, it catches
1,274 subjects after the band, and **at most 6.0 %** of them are citations. That figure is an upper bound,
because `rNNNN — item N` is usually a seat numbering the items of its own revision.

⇒ **The dash is doing semantic work by habit.** Seats write `rNNNN — …` when they claim a number and
`rNNNN word …` when they cite one. A widening across the dash takes in the citations along with the claims.

### No narrower widening based on wording falls below the line either

| variant | newly caught | citations (share after the band) | cross-seat claims |
|---|---:|---:|---:|
| HEAD (any text after the id) | 232 | 74 (34.1 %) | 2 |
| COLON (`rNNNN:`) | 54 | 11 (20.4 %) | 2 |
| COLON or a claim word (`orders`, `pre-registration`, `addendum`, `fixup`, …) | 152 | 18 (11.8 %) | 2 |

All 18 citations left in the narrowest variant are cc66's commits from before it adopted `+cc66.<k>`, in the
claim shape: `r6959 pre-registration: …`, `r7041 stage-c launcher …`. **A pattern cannot tell those from 60's
`r7206 pre-registration: …`.** The only difference is whose half the number lies in, and which seat wrote the
commit.

### Widening `collisions()` too makes it red on five false collisions

`collisions_widened.py` was run on this branch's HEAD.

- **Old pattern:** 65 collisions, all of them baselined.
- **HEAD form:** 70 collisions, with **5 new and not baselined**: `r6975`, `r6983`, `r7189`, `r7217` and
  `r7225`.
- **All five are citations.** In each case one side is the order itself and the other side is a seat answering it,
  for example `r7225 item 2 —` from cc66 against 66's `r7225 orders —`.

## What the widening would have caught that is real: 66's own run into the even half

The order asked whether any of the subjects that are now invisible is a seat claiming another seat's number.
**Yes, and the seat is 66.**

- Six commits from 66's session (`01XXeapZ…`) carry **even** ids, which are 60's half:

  | id | 66's subjects | 60's subject on the same id |
  |---|---|---|
  | `r7164` | `orders r7164 -- …` | — |
  | `r7166` | `orders r7166 -- …` | `r7166: the vector and tensor sectors …` |
  | `r7168` | `orders r7168 -- …`<br>`r7168: the metric-singularity result …` (`09161f5c`) | `r7168: PO-83 taken …` (`60dc8766`) |
  | `r7170` | `orders r7170 -- …`<br>`r7170: the INDEX row …` (`b5d8d879`) | `r7170: the four-dimensional step …` |

- **The old pattern sees none of the six.** The HEAD form sees the two `rNNNN:` subjects. It does not see the four
  `orders rNNNN`, because there the id is not at the head.
- **`collisions()` does not report `r7168` or `r7170` even under the HEAD form.** 60's `r7168` (`60dc8766`) is an
  ancestor of 66's `r7168` (`09161f5c`). 66 merged 60's commit and then took the same number, and the ancestry
  test reads that as one line's span, not as a collision.
  - ⌗ **This is a second blindness, and it is not the one ordered.** The ancestry rule cannot tell a span from a
    number reused after a merge. It is reported here, not repaired.

### `3192721e` is not the claim it was taken for

`r7225 item 2 — …` matches cc66's own established form for citing the order it is working on: **54 earlier
subjects** have the same shape. `6b5ab56a` (`r7225 — …`), which cc66 reworded, was the anomaly. It was a
citation written in claim syntax, and the old pattern caught it only because of the dash.

## The "anywhere" rival

- **Coverage.** ANYWHERE matches 2,947 subjects against HEAD's 2,606, which is 1.13×. Measured against the old
  pattern's 2,374, it newly catches 573 against HEAD's 232, which is 2.47×.
- **Citations.** Of the 341 subjects that only ANYWHERE catches, **at least 208 (61 %)** are citations by
  construction:
  - 83 open with a suffixed id;
  - 36 open with a letter-suffixed id;
  - 58 are merge or revert subjects;
  - 31 open with another identifier.
- A sample of the remaining 133 is mostly citations. The exception is 66's `orders rNNNN`, which is a claim with
  the id in second position.

## Predictions

| # | prediction | measured | |
|---|---|---|---|
| P1 | HEAD newly catches 150–450, point 260 | **232** | ✔ |
| P2 | `rN orders` is more than 60 % of the newly caught | 53 / 232 = **23 %** | ✘ |
| P3 | 1–5 cross-seat claims, `3192721e` among them | **2**, and `3192721e` is a citation | ✘ (count ✔, named member ✘) |
| P4 | false-positive share ≤ 2 % | **34.1 %** | ✘ |
| P5 | ANYWHERE ≥ 3× HEAD, and > 50 % of its extra matches are citations | 1.13× (2.47× on newly caught); ≥ 61 % citations | ✘ on the ratio, ✔ on the share |
| P6 | ≥ 1 new collision, `r7225` among them, to be settled in this change | **5 new, `r7225` among them, and all 5 false** | ✔ on the count, ✘ on what it meant |

- **Two hits, three misses and one split.** The misses come from one fact I did not foresee: a number at the head of
  a subject is often the order being answered.
- P4 predicted that the head position is a claim by construction. It is not.

## What would work: wording cannot settle it, so the claim has to be declared

The measurement says that no pattern over the wording of a subject separates a claim from a citation with fewer
than 11.8 % false positives on this history. The difference lies in whose number it is. **I recommend the
following, and the choice is 66's, because it changes how every seat writes subjects:**

1. **Declare citations.** A subject that opens with an order's number writes it in a citation form, `re r7225: …`
   or the existing `r7225+<seat>.<k>`. A plain `rNNNN` at the head then means a claim.
2. **Then widen `BARE` to the HEAD form, with the declared citation forms excluded by the seeds.** The gate's false
   positives then become exactly the commits that break the convention, which is a gate doing its job.
   - **The cost:** 60, cc66 and 69 change how they write acknowledgements and replies.
   - **What it adds:** it brings 66's own `rNNNN:` into view.
3. **Separately, 66's `orders rNNNN` form** puts its own claim in second position. Either it moves to the head, or
   `BARE` learns that one fixed prefix.

Until a convention exists, **nothing in the gate changes.** A widening that fires 34 % of the time on citations
makes the gate impossible to ignore for the wrong reason, which is the risk the order flagged.
