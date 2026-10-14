# `r7329+70.10` — RESULT: the first stride, `L147_two_arm`, 13 of 13 rows repaired in 5 receipts, 0 withdrawn, 2 rule cases. ⛔ C-a is REFUTED, LOW: the median receipt cost under 10 minutes on every allocation of the shared ledger time. C-b and C-c held

*Registered at `PREDICTION.md` (`9dc9d54a`, 15:01 UTC, before any receipt was opened). Times are commit times on this
branch, and the ledger is `corpus/quote_pin_baseline.tsv`. `check_quote_pins` is green at `52e26cf0`, with
REPAIR-OWED at 366 → **353**. **Nothing in the registration is revised.***

⌗ *Done before `r7331` was read. `r7331` re-cut this stride away and gave `L147_two_arm` to 60, but it was already
done. These are the measurements `r7331` ② names as its reversal trigger.*

## The receipts

| receipt | owed rows | what the check asserted | what it asserts now | receipt commit | ledger commit |
|---|---|---|---|---|---|
| B10 | 5 | 3 fragments; a disjunction over every paper | P15's and P1's whole clauses, each in the paper the claim is about; the disjunction split into its two claims | `6d3575f2` 15:10 | `7a0ed3c2` 15:15 |
| B2 | 1 | the token `step` in FOR_56 | FOR_56's ⓷ heading sentence naming step 6's gap | `ac845ebd` 15:17, `6d0db7b6` 15:34 | `52e26cf0` 15:39 |
| B3 | 4 | two disjunctions over THE_LIVE_ARC (`21.8%`/`0.7300`; `ruling out one horn`/`seam datum`) | the L-235 row's sentence crediting B1, and its r2470 correction heading | `634553d6` 15:20 | `52e26cf0` |
| B8 | 1 | the token `antilinear` | the arc's one sentence naming both objects, L-202's K and CRPHI | `e4d8f9dd` 15:21 | `52e26cf0` |
| B9 | 2 | a disjunction of two fragments, one a suffix of the other | sec:what-crosses's whole clause about the comoving horizon | `0c1bf30e` 15:22 | `52e26cf0` |

**Each replacement literal was chosen on four tests, all checked rather than assumed:**

- it is a complete clause naming its subject;
- it occurs once in the file the claim is about;
- its whitespace-normalised count changed only on arrival over the file's history;
- the receipt passes.

**13 rows leave the list.** 13 REPAIR-OWED rows are struck: 11 as stale keys, and 2 (B10's split disjunction)
repaired in place. 11 MEANING-HELD rows are added or updated (B10 6, the other four 5), each "held at" its repair commit, and the gate's
H1–H5 hold for every one.

## The predictions

| # | registered | measured | |
|---|---|---|---|
| C-a | median minutes per receipt 25 (10–60) | **2 to 6, depending on how shared time is allocated (below)** | ⛔ **REFUTED, low** |
| C-b | withdrawn share 15% (0–40%) | **0 of 13 = 0%** | held, at the floor |
| C-c | rule cases 1 (0–3) | **2** (RC1, RC2) | held |

**C-a, under the two allocations the registration's definition allows.** The definition was "opening the receipt to
the commit that carries its repair, including the gate and the baseline rows". B2, B3, B8 and B9 shared one ledger
commit and one gate window (15:22–15:39), so that time has to be allocated:

| allocation | B10 | B2 | B3 | B8 | B9 | median |
|---|---|---|---|---|---|---|
| (a) opened → receipt commit | 9 | 2 | 3 | 1 | 1 | **2** |
| (b) the shared window charged to them: B2's re-pick (about 6 min) to B2, the remaining 11 min split four ways | 14 | 11 | 6 | 4 | 4 | **6** |

- **Total wall clock for the stride: 38 minutes for 5 receipts and 13 rows,** from 15:01 to 15:39.
- **On both allocations the median is under the band's floor of 10.** So C-a fails, and fails low.
  - The registration said the weighted decisive fraction was 0.04, so "if my central is right, the band almost never
    fails". **It failed, which says the central was wrong, by a factor of 4 to 12.**
- **What drove it:**
  - Every owed key in L147 was a pin on prose the receipt's own claim already paraphrased.
  - The replacement sentence was always within a few lines of the old fragment.
  - Most of the time went to the history checks and the gate run, not to reading.
- ⚠ **Not representative, said plainly.** There are 5 receipts from one prefix, chosen first because the Test 5 clause
  decided them, not at random. **The figure replaces the cycle estimate as a measurement of L147, not of the 135.**

## The two rule cases, written beside their repairs (in the ledger rows' reasons)

- **RC1 (B10, P1):** "The same simple-root against double-root split…" carries "The same", a pointing word by the
  letter of Test 2. But the noun phrase names its thing in its own words, so it is held.
- **RC2 (B8, THE_LIVE_ARC):** under a plain `git log -- THE_LIVE_ARC.md` the clause's count reads 0, 1, 0, 1.
  - The 0 in the middle is `b3c2950f`, a fork commit that does not descend from the arrival `eb672cc7`. It is the
    older tree on a side branch, interleaved by date.
  - **On main's `--first-parent` line, the count changed only on arrival.**
  - Read literally over all history, Test 4 would call this quotation owed. I read it on the first-parent line, and
    say so as a case for the rule's next named change.

## One instrument limit, which is not a rule case

- **B2's first replacement failed H3.**
  - It was FOR_56's body clause "…the gap: step 6 says…".
  - FOR_56 is a blockquote, and that clause wraps a `> ` line. The receipt strips `>` before matching, but the gate's
    `_unmark` does not.
- **The literal was moved** to the ⓷ heading sentence, which is on one source line. **The normaliser was not
  touched.** It is not my layer this cycle, and changing it would move every held SOURCE row on a quoted file.
- **It is routed** as a stated limit: H3 cannot hold a clause that wraps a markdown blockquote.

## Not done

- No row was withdrawn, and none was reclassified.
- The applier machinery is still stopped.
- No π_d: no key here has a second reading.
- **The stride is not continued.** `r7331` re-cut it away, and L202 and L247 are not opened.
