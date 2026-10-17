# r7441+70 — RESULT: the tolerance split (registration `e47ed2f6e`; build `80827a1be`, merged in #500; fixes `r7441+70.5`)

| arm | registered | measured | verdict |
|---|---|---|---|
| **T-a** static | parses; 3 probe jobs + compare; compare `always()`; record line unchanged | as registered. The record's `run:` line is byte-identical; its `if:` is plain `always()`, because the scope step is now a job of its own | **HOLDS** |
| **T-b** seeded verdict | 8 / 8 | **11 / 11**: the 8 registered, 2 more at build (S8, S9) and S10 from the live T-f run. A mutation dropping the missing-build bit fails 3 | **HOLDS** |
| **T-c** seeded ledger | existing + new hold | every existing `red_carry --seed` arm unchanged; U18–U21 hold | **HOLDS** |
| **T-d** live, normal | 3× `MEASURED`, record runs | run `39039022608` at `80827a1be`: **285 of 285 on all three builds**, both comparisons run, record filed. Its 3 reds are V1 and the S39/S56 cascade, all trunk | **HOLDS** |
| **T-d′** live wall | slowest probe 35–50 % of the old single job | probes A **31.1**, B **43.8**, C **47.6** min. The old job would have run them in sequence: 122.5 min, past its own 120. **47.6 / 122.5 = 38.9 %**. Scope to compare: **50.3** min | **HOLDS** |
| **T-e** ⛔ live, induced | compare runs, names B, files A↔C, `NEVER PROBED` = B's unreached and no others | run `39042688743` at `349fde195`, scope 318: B **PARTIAL 13 / 318** (budget 0.2 min); compare ran; A↔C ran and filed; record **0 red, 305 NEVER PROBED = 318 − 13** | **HOLDS** (and see the real instance below) |
| **T-f** live, induced job cancel | compare names C. 60 %: the `always()` upload survives a job-level timeout | run `39048016725` at `542b3392c`: GitHub cancelled C at its 3-minute limit; **STATUS and upload ran** (82 logs, 65 KB); compare named C | **HOLDS**, the 60 % included. ⛔ **But the run found two defects (below), and its record never landed** |
| **T-g** revert | T-d again | the revert is `r7441+70.5`; its live run is the push of `c82002537` | scored in the reply when it lands |
| EFFORT | 3 h (2–5) | ≈ 4.5 h (13:35 → 18:05 UTC), the live runs dominating | holds |

## The real instance (r7443 ①: score T-e against what the trunk produced)

- **60's run `39027838186` (6awafl, scope 119), on the old single job:**
  - Probe A alone took **57.8** min (11:17:38 → 12:15:28).
  - B was cancelled 58 min later at the job limit; C never started.
  - The record filed **all 119 as NEVER PROBED**, A's finished measurement included. That is the whole-scope discard the split removes.
- **On the split, T-e's own run was a real instance as well as an induced one:**
  - **A and C ran out of their real 60-minute budget on a 318-receipt scope.** Each finished **316 of 318**; the missing two are S54 and S55, the two declared-long receipts.
  - The compare job named both PARTIAL with the count and still filed A↔C over what was measured.
  - **That is the property r7441 ③ asked for, shown on a cut the induction did not cause.**
- **Two runs on `main` repeated T-e without my intending it** (below): B was cut at 12 s, the compare ran, and A↔C filed.

## ⛔ Three defects the live arms found. Two are fixed at `r7441+70.5`; one is mine and is reported

1. **The record wrote nothing when its job ran out of time.**
   - `red_carry --record` read the PO-68 history *before* writing the ledger.
   - Measured here, that read costs **~10 s a carried receipt** (40 receipts: 395 s; the event scan, 12 s).
   - T-f's compare job, carrying 305, passed its 20-minute limit inside that read: **the write was never reached, and nothing was filed, not even `unmeasured`.** That is the quiet failure r7432 and r7441 exist to remove, one step later.
   - The old single job had the same order; its 120-minute limit hid it. 60's run `39003569581` also had its record step killed after the job timeout.
   - **Fix:** the write comes first; the event list is read before it (12 s) so the printed history is unchanged. The compare job's limit goes 20 → 90.
   - Checked: a call-order harness shows `write` before `history` and a lost race re-writing; the `red_carry --seed` arms are unchanged.
2. **A probe stopped from outside read "never started".** Live STATUS `rc=none probe=cancelled` with 82 logs present now reads **PARTIAL — stopped from outside (82 of 305)**, seeded as S10.
3. **⛔ My induction reached `main`.**
   - I pushed T-e's temporary commit to this seat's branch, which 66 merges whole into `main`. It went in at `169eb2384`.
   - Two `main` runs then probed B with a 12-second budget: `c4281e732` and `b57bfc6e4`.
   - The split handled it as designed: compare ran, named B, A↔C filed. But those two `main` runs measured one build of three for B's receipts. Those receipts were filed `unmeasured`, so the next union re-probes them.
   - `r7441+70.5` restores B (and C, whose 3-minute T-f limit had not yet merged).
   - **The rule I take from it:** an induced probe goes on a branch nobody merges, never on this seat's working branch.

## Proposed, not applied (66's call)

- **Per-build budget 60 → 100 min** (job limit 115). 60 cut A and C at 316 / 318 on a 318 scope. 100 is still under the old 120 for all three, and the push waits on the slowest build, not the sum.
- **Longest-first in `sweep_tolerances.probe_all`,** as `run_all_receipts` already orders the heavy run (`ORDER: longest first by READ_INDEX.json`).
  - The two receipts every cut build missed were the two declared long, and they start late in file order.
  - Their per-receipt timeout (`2 × max(900, budget)` = 60–70 min) can never fit inside a 60-minute build. Started first, they would.
- A clean `main` run on the split (`f619d8839`) went green on all four tolerance jobs in **18.4** min.
