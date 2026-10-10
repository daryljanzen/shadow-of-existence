# r7245 — the twenty unowned claim-sites: predictions before any is read (node 70)

**Population.** These are 60's `r7244` (`S12`) UNOWNED bucket: claim-sites whose last writer, by `git blame`, has
a subject carrying no revision id. Under the parity rule, no seat owns them. 60 counted 20 of 160. Nothing about
them has been looked at yet beyond that count.

## Method, fixed now

1. **Recompute the bucket** with `S12`'s own rule: `detect` and `in_claim` from 60's detector, `git blame
   --line-porcelain`, and parity of `^r\d{4}` in the subject. Do it at the commit where 60 measured it and at HEAD,
   and report any difference in membership.
2. **For each site, record:**
   - **The last writer:** sha, date and subject, and its kind, which is one of: a merge; an apparatus or tool
     commit (sweep, rename, reformat, generator); a revision commit without an id; or a commit from before the
     numbering began.
   - **The introducer:** the commit that first wrote the comparison, found with `git log -S` on the comparison
     text, and whether *it* carries an id. If it does, its parity says whose the site is.
3. **Read each site and give it one of these readings:**
   - **ABSENCE-GUARD:** `== 0` over prose or a set, asserting that something is absent.
   - **DELIBERATE:** the exact count is the claim, and the set cannot move under it, or its control is in the
     receipt.
   - **GENUINE:** an exact count on a set another seat can move, with nothing protecting it.
   - **FALSE-POSITIVE:** the detector's taint is wrong.
   - **NOT-THE-CLASS:** stage two already clears it as FROZEN, SELF or ROW-SCOPED, and reading confirms that.

## Predictions

| # | prediction |
|---|---|
| U1 | **Why they are unowned.** At least 12 of the 20 last writers are merges or apparatus commits; at most 4 are commits from before revision ids existed. |
| U2 | **Introducers.** At least 15 of the 20 have an introducer that carries a revision id, so ownership is recoverable from the introducer. |
| U3 | **66's negative (unowned only because the commits predate the numbering) does NOT fire.** The bucket is mostly an artefact of last-writer blame landing on id-less commits, not of history before numbering. |
| U4 | **Partition.** NOT-THE-CLASS (FROZEN/SELF/ROW-SCOPED): 12–17. EXPOSED: 3–8. |
| U5 | **Readings among the EXPOSED.** ABSENCE-GUARD 2–6. GENUINE 0–2 (point 1). FALSE-POSITIVE 0–2. |

## What a seat should do with an unowned site

This is the part 66 says no measurement settles. My position, fixed now, will be argued from the results:
- **Ownership should follow the introducer, not the last writer.**
- **When even the introducer carries no id,** the site belongs to whoever owns the receipt's directory row in
  `receipts/INDEX.md`.
- **When nothing assigns it,** the gate's own seat holds it. This seat holds `check_exact_counts`, so that is me.
