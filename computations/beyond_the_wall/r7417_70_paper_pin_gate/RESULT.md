# r7417+70 ①: RESULT. The PAPER half is wired as a ratchet gate: exact, two-sided, 3.4 s here

Registration `7334696a3` (13:31:03 UTC); the gate landed at `r7417+70.2` (`8c878606c`).

| | band | measured | verdict |
|---|---|---|---|
| **P-a** absent PAPER rows at the wiring commit | `118`–`132` | **`125`** of 1510 | **HOLDS** (one more than at `fab1faf51`, because main moved in between) |
| **P-b** gate wall, this container | `1`–`10` s | **`3.4` s** (`3.8` s with `--update`) | **HOLDS** |
| **P-c** gate wall, CI `fast` job | `1`–`20` s | **`2.6` s** (job `116999138820`, 13:52:20.90 → 13:52:23.51, at the merge ref `c4c38bb3`: 125 absent, NEW 0, STALE 0, seed True) | **HOLDS** |
| **P-d** local fast job green with the gate in it | yes | **yes**: `run_fast_job.sh`, 128 gates, exit 0 | **HOLDS** |
| **P-e** two-sided seed | both | **both**: the present literal reads present and its one-character mutant reads absent | **HOLDS** |
| EFFORT | `45` min (`20`–`90`) | **≈ 35 min** (13:31 → ~14:05 UTC, most of it the fast job) | holds |

**Exactness at the wiring commit, not only at `fab1faf51`.** The uninstrumented `_present_at` was re-run over
all 1510 PAPER rows at `7334696a` (`OLD_PAPER_AT_WIRING.tsv`, 9.0 s). It gives 125 absent; the gate's list
also has 125; the symmetric difference is 0.

**The probes (`PROBES.txt`).**
- Removing one listed key fails as **NEW**, naming that key.
- Adding a bogus key fails as **STALE**, counted as no longer a live row.
- The restored list passes.

So each failure direction is shown failing, and the control passes.

**What the list is.** The 125 are candidates: no green-receipt filter is applied, and `NOT-A-PIN` and
`ENCODING-OK` rows may be benign. The ratchet's job is that the count can only fall and that a new candidate
cannot land unlisted. Listing a deliberate absence takes `--update` in the same commit, which is visible in
the diff.

**What it does not claim.** Nothing about the SOURCE half (r7417 ②).
