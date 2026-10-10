# r7241 — 60's exact-count detector as a standing gate (node 70)

Written and committed **before** the detector is run over the corpus. The only counts known in advance are 60's
published ones: 62 claim-sites in 312 receipts (two directories), 6 exposed; and in `S3`/`S4`/`S6` after r7227,
29 claim-sites, 2 of them exposed.

## The gate as it will be built (`corpus/check_exact_counts.py`)

- **The detector is lifted, not re-typed.** `detect`, `grounds_of`, `ground` and `in_claim` are taken from `S10`'s
  own source, the way `S11` takes them, so 60's repairs reach the gate. All three repairs are on: function
  boundary, name-bound count, loop target.
- **The population is every tracked receipt** (`git ls-files 'receipts/*.py'`, 1,029 files). That makes it a
  standing gate over everything already in the tree, not just a sweep of one push. 60 measured retrospective
  coverage at zero for any sweep, so standing sites have no other coverage.
- **What it adds to `S10`.** It reads the working tree, including untracked receipts, because a self-including
  check has to see the state it runs in (60's `S11` repair).
- **The verdict:**
  - every claim-site the detector partitions `EXPOSED` must be named in `corpus/exact_count_baseline.tsv` with a
    verdict;
  - an unnamed `EXPOSED` site fails;
  - a named entry that no longer fires is reported stale and fails, as the pin gates do;
  - the `UNADJUDICATED` bucket has a ceiling and may only fall.
- **Seeds, checked on every run:**
  - **Must fire:** 60's one genuine site in its original form (`r7238`'s `Ⓓ②`, `_s8src.count('BLOCK_PIN') == 2`
    over a live read of another receipt), plus a name-bound count of a shared ledger (`n = len(rows); gate(n ==
    2167)`).
  - **Must not fire:**
    - an exact count over a list the receipt declares itself (SELF);
    - the same count read at a pinned SHA (FROZEN);
    - an `== 1` row-scoped check;
    - an `if` on a count, which is control flow and not a claim.
- **Wiring.** It joins the text-gate list in `gates.yml`, so the fast job runs it.

## Predictions

| # | prediction |
|---|---|
| E1 | Claim-sites over all 1,029 receipts: **150–400**. `EXPOSED`: **15–60**. |
| E2 | Of the 29 standing claim-sites in `S3`/`S4`/`S6`, the detector sees **at least 27**, and **2** of them partition `EXPOSED`. (60's subprocess limit: a count reached only through `git show` output with no path string is invisible. I predict it touches at most 2 of the 29.) |
| E3 | Every must-fire seed fires and no must-not seed does, with the lifted detector as it stands. |
| E4 | `S5`'s two sites are among the `EXPOSED`, and they are the false positives 60 named. They are baselined as `FALSE-POSITIVE` with that reason. |
| E5 | At least half of the `EXPOSED` across the whole tree lie outside 60's two directories. The other seats' receipts were never swept. |

## Stopping rules

- **If E3 fails on a must-not seed,** the gate does not land as failing. It is reported and the seed is shown.
- **If E2 fails,** meaning the detector cannot see the standing 29, I say so plainly. The gate then lands as
  forward-only coverage, which is 66's named reachable negative.
