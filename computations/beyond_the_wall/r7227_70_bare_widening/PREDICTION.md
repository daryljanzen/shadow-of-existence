# r7227 — widening `BARE`: pre-registration (node 70)

Written and committed **before** any subject in the history was counted under any widened pattern.
The only subjects seen so far are the two `cc66` named in its `r7225+cc66.164` body
(`6b5ab56a` / `3192721e`) and the subjects of the most recent `origin/main` log lines.

## What is being changed

`corpus/check_revision_collisions.BARE` is `^(r\d{3,5})\s*[—-]\s*(.*)$`. It matches a revision id only when a
dash follows it **directly**. `r7225 item 2 — …` makes a claim to `r7225` that the band check cannot see.

**Proposed widening (the "HEAD" form).** A bare id at the head of a subject is the claim, whatever follows it:

    ^(r\d{3,5})(?![\w+.])\s*(?:[—-]\s*)?(.*)$

- The lookahead keeps the two forms the old pattern already let through.
  - `r3100a`, the deliberate follow-up suffix, still passes.
  - `r7225+70.1` and `r7225+cc66.164`, the seat-suffixed forms, still pass.
- A dash is no longer required.

**The rival (the "ANYWHERE" form).** A bare id anywhere in the subject: `(?<![\w+.])(r\d{3,5})(?![\w+.])`.
It is measured only to state what the order's wording "anywhere in a subject" would cost.

## Definitions, fixed now

- **Population.** Unique commits reachable from every ref (`git log --all`, after fetching every remote
  branch), so that all four seats' branches are counted.
- **Newly caught.** A subject the widened pattern matches and the old `BARE` does not.
- **Innocent mention (a false positive).** A matched id that is not the commit's own number. Examples are an id
  the subject is *about*, *answers* or *corrects*, where the commit's own number is elsewhere or absent.
- **Cross-seat claim.** A newly caught subject whose head id lies in a half its authoring seat does not hold.
  A suffix-only seat (`cc66`, `70`) holds no half, so any bare head id it writes counts.
- **Seat attribution.** The commit's `Claude-Session` trailer is mapped to a seat through the suffixed subjects
  (`+cc66.`, `+70.`, `+60.`, …) written in the same session. A session with only bare ids takes its majority
  parity. Commits that cannot be attributed are counted as such and are not guessed.

## Predictions

| # | Prediction |
|---|---|
| P1 | The HEAD form newly catches **150–450** subjects (point estimate **260**). |
| P2 | The commonest newly caught shape is 66's `rNNNN orders — …`, at **more than 60 %** of the newly caught. |
| P3 | **1–5** of the newly caught are cross-seat claims, and `3192721e` is one of them. |
| P4 | The HEAD form's false-positive rate over the newly caught is **≤ 2 %**. |
| P5 | The ANYWHERE form matches **at least 3×** as many subjects as the HEAD form. **More than 50 %** of the subjects only it catches are innocent mentions, so ANYWHERE is the wrong widening. |
| P6 | Widening `BARE` itself also adds **at least one** new divergent collision to `collisions()` on this branch's HEAD (`r7225`: `3192721e` against 66's own `r7225`). That collision has to be settled in the same change rather than left red. |

## Acceptance for the widening to land

- Two seeds in the check, both of which fail under the old pattern or the wrong widening:
  - a subject that **must** fire (`r7225 item 2 — …`);
  - a subject that **must not** fire: a mid-subject mention, the `+70.` / `+cc66.` suffixed forms, and `r3100a`.
- The plain suite's band and collision receipts are green: `L251/N1`, `L256/B1`, `L260/H1`, `L261/A1`,
  `L259/D1` and `L267/G1`.
- The false-positive rate over the real history is stated in the reply before the change is offered.

## Stopping rule

If the HEAD form's false-positive rate is above 5 %, it does **not** land. The narrower variant that would hold is
reported instead.
