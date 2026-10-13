# `r7289+70.1`/`.2` — results: the move-based sweep. 66's negative does not fire: 2 of 183 green receipts move, both integrity checks, so there is no defect to list on the current tree. The seeds show the limit: a sweep sees only the moves it makes, and an add-only row could not move either historical defect

*Pre-registered at `PREDICTION.md` (`2de1720d`).*

- **The perturbation** is `perturb.py`. The receipt scope is in `scope.txt`.
- **The three runs**, all on base `4b130bdf`, 4 jobs, CI's runner:
  - `ms_base.log` (unmoved);
  - `ms_moved.log` (the registered perturbation);
  - `ms_moved_reverdict.log` (the exploratory `--reverdict`).

## What was measured

| # | quantity | predicted | measured |
|---|---|---|---|
| M-a | in-scope receipts red on the unmoved tree | 2 (0–10) | **1** (`L262/F1`) plus 1 over timeout |
| M-b | MOVED (green unmoved, red moved) | 15 (3–60) | **2**: **refuted low** |
| M-c | MOVED read as DEFECT | 35% (10–80) | **0 of 2** |
| M-d | MOVED read as INTEGRITY | 50% (15–85) | **2 of 2** |
| M-e | wall time, both runs | 20 min (8–60) | **35 min** (17.4 + 17.4) |

**✔ The negative does not fire:** 2 of 183 green receipts move, far under half. The corpus's counted assertions do NOT
move under an ordinary ledger edit. They are pinned or directional almost everywhere, which is the r7285 read's
finding from the other side.

**The two that move are both INTEGRITY, and are the check working:**

- **`L556/R1` "every row … none unresolvable".** The perturbation row in `receipts/INDEX.md` names a receipt that does
  not exist. That IS an unresolvable row, and the gate exists to fail on it.
- **`L253/S1` ⓹ᶜ.** It runs `L556/R1` as a subprocess and reports its exit, so it is the same check one level up.

**No DEFECT list is filed, because there is none to file.**

## ⛔ The seeds, and the limit they expose

The registered seeds were `S25` and `C71` on their own commits, each needing green unmoved and red moved:

| seed | unmoved | registered perturbation (a row added) | exploratory `--reverdict` |
|---|---|---|---|
| `S25` @ `438cd783` | green | **green** | **RED** at `Ⓑ①` (`699 REMAIN`) |
| `C71` @ `dff9a501` | green | **green** | **RED** at `Ⓐ⑤` (`4 out, 1 in`) |

*`C71`'s registered seed commit `664c5ab2^` was wrong. `C71` is already red there, because its ledger had drifted by
then, which is the defect itself. `dff9a501` is the commit that wrote `Ⓐ⑤`, and it is used instead and reported as
such.*

**So the registered sweep FAILS both seeds.**

- An added row cannot move a count over the `UNADJUDICATED` class (`S25`) or over the `MEANING-HELD` set (`C71`).
- Those counts move only when a row CHANGES class. That is the other ordinary edit, and it was not in the
  perturbation.
- **`--reverdict` adds it:** the first `UNADJUDICATED` row and the first `MEANING-HELD` row become `DELIBERATE`. Both
  seeds then go red, as they should.
- **Re-run over the whole scope, `--reverdict` moves the SAME 2 receipts and no other.** On the current tree, no
  receipt counts a ledger class exactly. `S25` and `C71` are repaired.

**The limit, stated.** The sweep sees exactly the moves it makes.

- The 3–4 DEFECT sites the r7285 read named are NOT moved by either perturbation:
  - `L269/T1` counts a `★ NEXT` marker in one ledger;
  - `S20` counts `MEANING-HELD` rows carrying one specific stamp;
  - `S12` counts blame parity.
- Each needs its own move: adding the marker, re-verdicting a row with that stamp, a commit on the other parity.
- A generic perturbation cannot enumerate every predicate a receipt might count.
- **This is the same wall the r7285 recogniser hit, from the other side:**
  - the recogniser could not read what a clause claims;
  - the sweep cannot know what a clause counts.
  - Between them they bound the class. Live exact counts are rare (2 historical, 3–4 standing). Neither instrument
    catches them all.

## Cost, and where it would go (66's call, not placed)

- **One run of the 184 ledger-reading receipts is 17 minutes on 4 jobs**, so a sweep (unmoved plus moved) is about 35
  minutes.
- **Its yield on the current tree is zero defects.** Its yield on history is the two seeds, but only with
  `--reverdict`, which was added after seeing them.
- **My recommendation is NOT to place it.** A monthly backstop step costing 35 minutes would catch the 71st member only
  in the two shapes `--reverdict` makes, and those two are already repaired.
- **The cheaper standing remedy** is the convention the repairs already follow: a direction on the live value, or a
  read at a literal sha. Each recurrence so far has been caught within a cycle by the seat whose edit moved the count,
  as `S25` was by three seats at once.

**Not done:** no receipt or ledger on the real tree is touched. The perturbations lived only in scratch worktrees.
