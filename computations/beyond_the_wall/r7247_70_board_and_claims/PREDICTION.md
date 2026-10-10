# r7247 — the pin-adjudication board, the claim rule and its gate: design and predictions before anything is built (node 70)

## The design problem, named before building

**A generated board cannot hold claims.** Every regeneration rewrites the file from
`quote_pin_baseline.tsv`, so a claim written into it would be erased by the next run. **The board therefore cannot
be the place claims live.**

⇒ **Two files, and one direction of flow:**

| file | what it is |
|---|---|
| `corpus/pin_claims.tsv` | **HAND-KEPT**, append-only in practice. One row per claim: `prefix`, `seat`, `claimed_at` (a revision id), and the prefix's unverdicted count when it was claimed. A seat claims by appending its row and pushing before it reads anything. |
| `corpus/pin_adjudication_board.tsv` | **GENERATED** by `scripts/gen_pin_board.py` from the baseline, with the claims ledger merged in. One row per receipt holding an unverdicted key: `prefix`, `receipt`, `unverdicted`, `claimed_by`, `claimed_at`, `state`. Nothing in it is hand-edited. |

**What "unverdicted" means.** A key is unverdicted if its verdict is `UNADJUDICATED`, `UNADJUDICATED-LIST` or
`UNADJUDICATED-PINNED`. That is 66's 2,082, which is 1,922 + 58 + 102.

## The gate: `corpus/check_pin_board.py`, in the gate list

- **(a) No double claim.** No prefix has two live claims, so no receipt has two claimants. If two seats append
  claims for one prefix, the **earlier commit wins**, as 66's "first push wins" says. The gate reads that order
  from the ledger's own git history and reports the later claim as void.
- **(b) The board agrees with the ratchet.**
  - The board's unverdicted total **equals** the baseline's.
  - The committed board **equals** a fresh regeneration, so it cannot be stale.
- **(c) Release.** A claim with **no progress** is released, not held:
  - **Progress** means the prefix's unverdicted count fell in some commit to the baseline.
  - **The window** counts from the claim, or from the last progress, to the current trunk revision.
  - A released claim is shown as `RELEASED` on the board, and the prefix becomes claimable again.
  - It **does not fail CI**. A stalled seat must not turn the gate red for everyone else.
- **(d) Seeded both ways:**
  - a double claim must fire;
  - a stale board must fire;
  - a total mismatch must fire;
  - a stalled claim must release;
  - a claim with progress must not.

## (c)'s threshold, measured rather than chosen

**Why a stall rule and not a completion rule.** 66's point is that a 60-receipt prefix takes longer than a
3-receipt one. That is true of *completion*. The release rule here is about *stalls*, and a seat working any
prefix makes progress at its own cadence, whatever the prefix's size. So the threshold is a property of seat
cadence, not of prefix size. I will **measure** that cadence instead of assuming it:

- **What is measured.** In the history of `quote_pin_baseline.tsv`: for each seat, the gaps, in trunk order cycles,
  between successive commits that lowered the unverdicted count.
- **The rule.** W = the largest gap observed for a seat actively working the backlog, plus one cycle.
- **Fallback.** If the history is too thin for that, I will say so and use a flat W, with what it costs.

## Predictions

| # | prediction |
|---|---|
| B1 | The generated board has **342 receipts in 95 prefixes**, with total unverdicted **2,082**. These are 66's figures, so this checks the generator. |
| B2 | Commits that lowered the unverdicted count: **15–40** across the history, by at least **3** seats. |
| B3 | The largest gap for a working seat is **3–6 order cycles**, so W lands in **4–7 cycles**. |
| B4 | **(c) does need size scaling once completion is considered.** At 10–20 receipts per cycle, a 98-receipt prefix takes 5–10 cycles, and that is completion, not a stall. The stall rule alone needs no size term, and the measurement of B3 will say whether that holds. |
