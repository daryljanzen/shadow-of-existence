# r7365+70 — PRE-REGISTRATION (pushed before the sweep is run or the nightly's output is read)

*Order: `r7365` ② (U-c, U-d) and ③ (one read of the nightly's own output against two rules).
Seat 70, branch `claude/shadow-of-existence-setup-wgcmvt`, at `origin/main` `b4eb552a`.*

**State the order did not have.** `r7365` was written against `.1`/`.2`. `U-c` and `U-d` were already
run and scored at `r7355+70.3`/`.4` (`dd8a2fcc`, PR #444, unmerged when the order was cut). U-d:
0 newly red, PASS 128 / FAIL 0 / UNRUN 1 at `cdc16410`, held. U-c: refuted on the premise, because the
nightly emits no `READ_INDEX` (only the monthly backstop does). The step is routed with four CI options
priced. **Those scores stand and are not re-registered.** What follows is new.

| arm | quantity | central | band | failable at central? | decisive fraction |
|---|---|---|---|---|---|
| **V-d** | gates newly red against the last clean roster, re-swept at `b4eb552a` (16 trunk commits after `cdc16410`), by seat | `0` | `0`–`1` | yes: two or more reds refute it | the full roster (129 gates); no sample |
| **V-③** | outputs of the nightly job (its committed `RUN_RESULT.txt` plus the `READ_INDEX` step I built) that break either `r7365` ③ rule: (i) the container's installed set printed and asserted of nothing; (ii) a measured population whose selector is not committed with it | `2` | `1`–`3` | yes: 0 or 4 or more refute it | every output the job writes, which is 2; no sample |

*EFFORT (assignment: r7365 ②–③): central 15 min, band 5–40.*
