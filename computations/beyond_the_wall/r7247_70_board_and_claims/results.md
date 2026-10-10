# r7247+70.1 — the board, the claims ledger and the gate: results (node 70)

Pre-registered at `PREDICTION.md` (`ff83b053`) before anything was built.

## What was built

| file | kind | role |
|---|---|---|
| `corpus/pin_claims.tsv` | hand-kept | claims: `prefix  seat  CLAIM\|RELEASE  rNNNN  note`, appended and pushed before reading |
| `corpus/pin_adjudication_board.tsv` | generated | one row per receipt holding an unverdicted key: `prefix receipt unverdicted claimed_by claimed_at expires_after state` |
| `scripts/gen_pin_board.py` | generator | writes the board from the baseline with the ledger merged in |
| `corpus/check_pin_board.py` | gate, in `gates.yml` | checks (a)–(d); runs in about 1.4 s |

**The board at HEAD:** **342 receipts in 95 prefixes, 2,082 unverdicted, equal to the ratchet.** No claims yet.

## The checks, each shown failing on the real files and then restored

- **(a) Double claim.**
  - **The test:** 70 claims `L221_the_bridge` at r7247, then 60 claims it at r7248.
  - **The result:** `VOID claim: L221_the_bridge by 60 at r7248 -- 70 holds it until r7255`, rc 1. First push wins.
- **(b) Board against ratchet.**
  - **The test:** one key verdicted in the baseline without regenerating the board.
  - **The result:** `the board says 2082 and the ratchet says 2081`, rc 1. A board differing in content but not in
    total is caught by the fresh-generation comparison (`STALE`).
- **(c) Release.**
  - **The test:** a real claim of `L221_the_bridge` at r7247.
  - **The result:** the board shows `CLAIMED`, expiring after **r7255** (= r7247 + 4 cycles × 2). Expired claims are
    reported `RELEASED` without failing.
- **(d) Seeds, on every run, all holding:**
  - a second claim on a held prefix is void;
  - a claim after expiry stands;
  - a stalled claim expires;
  - progress resets the window;
  - the board total excludes verdicted keys;
  - a baseline change changes the board.

## (c)'s threshold: measured, and the measurement forced the fallback

- **The data.** In the history of `quote_pin_baseline.tsv`, **8 commits** lowered the unverdicted count, by 3 seats
  (70 ×5, 60 ×2, cc66 ×1).
- **The gaps between one seat's lowering commits, in order cycles:**
  - 70: 2, 1, 44, 9;
  - 60: 3.
- **Within a stretch of backlog work** the gaps are 1–3 cycles.
- **The long gaps** (9 and 44) are periods when 70 had been **ordered onto other work**. The history cannot tell
  that apart from a stall, because no backlog work so far has been claimed rather than ordered.
- ⇒ **A flat W = 3 + 1 = 4 cycles**, the pre-registered fallback.
- **Its cost:** a seat pulled onto another order for more than four cycles loses its claim and re-claims with one
  appended row. Its verdicts are kept in the baseline, so no work is lost.
- **On size.** It is a **stall** rule: any progress resets the window. So a 98-receipt prefix and a 3-receipt one
  stall alike. Size sets completion time, which the rule never measures. **No size term is needed, and none is
  used.**
- ⇒ **Once seats claim, the ledger itself becomes the history this threshold should be re-measured from.** The
  first claim-driven stall or release is the first real data point.

## Predictions: three of four, one of them split

| # | prediction | measured | |
|---|---|---|---|
| B1 | 342 receipts in 95 prefixes, total 2,082 | **342, 95, 2,082** | ✔ |
| B2 | 15–40 lowering commits, by at least 3 seats | **8**, by 3 seats | ✘ on the count, ✔ on the seats |
| B3 | largest working gap 3–6 cycles, so W in 4–7 | **3** within working stretches, so **W = 4** (the 9 and 44 are ordered-elsewhere gaps) | ✔ |
| B4 | the stall rule needs no size term | stated and built that way | ✔ |
