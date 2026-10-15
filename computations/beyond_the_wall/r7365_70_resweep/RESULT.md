# r7365+70 — RESULT (registration `ccd382d8`, pushed before the sweep ran or the nightly's output was read)

| arm | registered | measured | verdict |
|---|---|---|---|
| **V-d**: new gate reds against the last clean roster at `b4eb552a` | `0` (`0`–`1`) | **`0`**: PASS 128 / FAIL 0 / UNRUN 1, 129 of 129 accounted for. The UNRUN is `check_receipts_run(stale-cache)`, the stated cache-age case | **HOLDS** |
| **V-③**: nightly outputs that break either `r7365` ③ rule | `2` (`1`–`3`) | **`0`** of 2 | **REFUTED LOW** |
| EFFORT (r7365 ②–③) | `15` min (`5`–`40`) | **≈ 54 min** (14:25 → 15:19 UTC) | **REFUTED HIGH** |

**V-d, by seat.** No gate is newly red, so no seat is owed. The trunk's receipt reds (`L_probability` S20,
S29, S39, S50, S51, S52, S54, as PR #444's scoped jobs show) are reds in *receipts*, not gates. The red-carry
ledger already carries each of them on `main`, and none of them is a corpus gate.
Command: `NODE=ci bash scripts/sweep_gates.sh`, which writes its roster to `/tmp/sweep_roster.txt` and
asserts it.

**V-③, one read, no campaign.**
- **`RUN_RESULT.txt`** (`refs/ci/nightly` at `8dcbea47`, run 38702458187 at `dbd23ffd`):
  - Rule (i): **not broken.** The file prints no installed set at all, so nothing is printed and left
    unasserted. The install it runs on is `requirements-ci.txt`, which pins every package. That includes
    `pynucastro==3.1.0`, the one the workflow's install line names a second time
    (`requirements-ci.txt:56`). It also includes the Python version, which is pinned against
    `ENV_FINGERPRINT.txt` (PO-64).
  - Rule (ii): **not broken.** The population is "every registered receipt" at a named commit. The
    selector is the registry and `run_all_receipts.py` at that commit. The commit sha is in the ref's
    message and the file prints a `TREE-DIGEST`, so a re-run at `dbd23ffd` re-derives the 1096.
    `READ_INDEX.json` only orders the run longest-first; it does not select.
- **The READ_INDEX step** (`receipt_scope.py --emit`, the artifact I download and commit):
  - Rule (ii): **not broken.** `emit` writes the traced commit, its date and the tree digest into the
    index's header (`traced_at`), and each receipt entry carries its blob sha, so the committed index
    names its own population.
  - Rule (i): **not broken.** It records reads, not an installed set.

The registration expected two breaks. The read found none, because both outputs already carry their
selector and neither prints its container. The central came from the order's framing rather than from
reading the two files, which is the same failure as `r7355`'s premise, made on my side this time.

**EFFORT, refuted high, two causes, both mine.**
1. My first sweep was run under an outer `timeout 1500` that is shorter than the sweep's own 1800 s
   per-gate cap. It was killed at 25 min with no reading. A sweep must never sit under a cap shorter than
   its own wall time.
2. The re-run took 28 min of wall time by itself, more than the whole band's central. I priced the
   arm without looking at the sweep's measured wall time.
