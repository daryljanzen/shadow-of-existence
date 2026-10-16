# r7411+70 / r7413+70 — RESULT (registrations `bf03eede7` and `f8317a6c0`)

**The selectors and lists are committed beside the timings** (`scope_*.txt`, `PICK_RUN.txt`,
`PRICE_TIMES.txt`, `READS_RUN.txt`), so each figure can be re-run.

## ① The price, by scope, on this container

| arm | registered | measured | verdict |
|---|---|---|---|
| **L-a** median suite scope, last 20 revisions | `12` (`3`–`60`) | **`15`** receipts | **HOLDS** |
| **L-b** suite run on the median revision (`964fef0a2`, 15 receipts, `--jobs 4`) | `8` min (`2`–`30`) | **`11.5`** min (692 s), all 15 exit 0 | **HOLDS** |
| **L-c** reads run | `10` min (`2`–`40`) | **`0`**: the scope is empty on all 20 revisions (below) | **REFUTED LOW**, and that is the design |
| **L-d** tolerance run, CI's three builds, on a median-sized tolerance scope (`43c33644c`, 5 receipts) | `15` min (`3`–`60`) | **`60.3`** min (1193 + 1231 + 1191 s), both comparisons CLEAN | **REFUTED HIGH**, just past the band |
| **L-e** total | `35` min (`10`–`120`) | **`72`** min | **HOLDS** |
| EFFORT (r7411 ② + r7413 ①) | `60` min (`30`–`120`) | ≈ 74 min (03:31 → 04:45 UTC) | holds |

**What decides the turn batch, as a sentence per scope:**
- **suite: about 11.5 min a turn on the median diff.** That is not "a few minutes". The cost is the
  receipts themselves: this scope's 15 include several slow ones. The distribution is wide: 1, 3 and 11
  at the small end; 83, 108, 121, 211 and 327 at the large end, where a turn touching a shared ledger
  scopes hundreds.
- **reads: 0 a turn**, except on a turn that deletes or renames a read file. Then it costs the
  runner-read sweep over the receipts it selects.
- **tolerance: about 20 min per build, and CI runs three.** It is about an hour even on 5 receipts,
  because every receipt is run with its comparisons instrumented, three times.

*My L-d central assumed the tolerance probe costs what a plain run does. It costs about 1.7× per
build (1193 s against the index's own 1143 s estimate for one), and there are three builds.*

## ① The `reads` zero: design, not breakage

| test | prediction | result |
|---|---|---|
| **R-a** deletes or renames in the same 20 revisions | `0` (`0`–`2`) | **`0`** |
| **R-b** delete a file a receipt traces (`cc66_fig_acoustic_numbers.npz`) | fires, including its reader | **2**, including its reader |
| **R-c** rename a member of a traced glob (`planck_tt_likelihood/PROVENANCE.md`) | fires | **19**, including the glob's owner |
| **R-d** delete a file nobody reads (control) | 0 | **0** |

**Verdict, by the rule fixed in the registration: H-design.** The selector fires on exactly the events
it exists for. No revision in the window produced one: not one of the 20 deleted or renamed any file.
*A gate that selects nothing on twenty revisions is untested in the sense that nothing exercised it.
These four probes are that exercise, and they are committed, so it can be re-run.*

⚠ **One probe of mine was malformed, and it is kept in the output.** My first R-c **added** a glob
member, and the reads branch of `scope()` deliberately reads only `gone`: an addition cannot make a read
resolve to nothing. It returned 0. Under the verdict rule that would have read "broken". Re-run **as
registered**, as a rename (`gone` plus `added`), it fires on 19.
