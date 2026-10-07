# r7209+70.2 — results: an operator cannot see a COMPOSED statement by its words.  Verdict NOT-THIS-WAY

*Pre-registered at `PREDICTION.md` (`245a0ba2`).  Outputs: `seeds_log.txt`, `t1_t2_log.txt`, `census_head.tsv`.*

| test | predicted | measured | |
|---|---|---|---|
| seeds | 4 / 4 | **4 / 4** | hit |
| T1 member 25 at `d7b1dd03` | 50/50 | **not flagged** | miss |
| T2 the repair at `6fd00881` | no H1 flag | **no H1 flag**; one H4 flag (`cosmic time`), noise | hit |
| T3 member 26 (`leg`) | invisible by construction | not run; outside the lexicon | as stated |
| T4 census on `f853845e` | 20–150 rows | **314 rows**, 177 receipts, 748 sites | miss, high |
| T5 existing operators | blind, structurally | receipt pins **0** literals with `event horizon` | hit |

## T1 is the finding, and it misses for the reason that matters

- **The join works.**  The `\rcpt` site for the back-seam receipt shares its paragraph with
  `\emph{The back seam is the event horizon of the collapsing matter}` (the 1,974-character paragraph in
  `t1_t2_log.txt`).  So a sentence-to-receipt link is available mechanically.
- **The receipt names the alternative and never tests it.**  Its only `cosmological horizon` is inside Ⓕ③, a
  quote-pin of `P2`'s sentence about the cubic's *other* roots.  The operator reads that as "the receipt knows the
  alternative" and clears the site.
- ⇒ **Naming the alternative is not discriminating against it.**  A lexical proxy cannot tell the difference,
  because the difference is in what is *computed*, not in what is *said*.  r7187's repair Ⓑ② is the computed
  form: it evaluates `f` on both sides of a black-hole root and of a cosmological root at three members, and
  asserts that the third root matches the second and reverses the first.

## T4 says the proxy is too wide as well

- 314 (site, pair) rows: H4-B 86, H2-B 71, H3-B 56, H3-A 49, H4-A 18, H1-B 17, H2-A 13, H1-A 4.
- These come mostly from correct uses of `static`, `degenerate` or `cosmic time` in receipts with no reason to
  name the other side.  So the decision rule's TOO-WIDE branch fires as well.

## A miss in the pre-registration's own facts

- It said 492 `\rcpt` sites on HEAD.  **There are 748** in 37 files.  The 492 came from a grep that capped the
  receipt name at 80 characters, and many receipt names are longer.  The census here reads every site.

## What would see it

- The defect is an identification with no computational referent.  Nothing in member 25's code carried "event
  horizon", so no mutation of its code, and no reading of its words, reaches it.
- The form that does reach it is the shape of r7187's repair, made a requirement:
  - the receipt **declares** the wrong composition it rules out (for member 25: "a black-hole root's signature");
  - one of its checks **computes** that alternative;
  - and the check **fails** on it.
- A gate can verify the declaration exists and is attached to a check.  It cannot verify mechanically that the
  declared alternative is the *relevant* one.  That remains an author's judgement, as with `READ-ELSEWHERE`.
- This is a pin-form and receipt-contract change, so it is a gate design and 66's call.  It is offered here, not
  built.
