# r7225+70.1 — results: the `EXTEND-SHORT` batch. 108 of 158 went through, and the counts moved exactly as stated in advance

*Pre-registered at `PREDICTION.md` (`c3d0ff30`).  Per-key outcomes are in `ledger.json`.  The other files are the
extensions (`extensions.json`), the before and after receipt runs (`pre_run_log.txt`, `post_run_log.txt`), the
engine (`apply_batch.py`) and the baseline swap (`swap_baseline.py`).*

## What went through

- **108 keys extended**: 67 paper and 41 source, in 79 receipts.  Each was edited at its own string token, run
  green, keyed again by `--quote`, and checked to leave the reversal classes.
- All 95 receipts in scope were green before any edit (`pre_run_log.txt`).
- 21 extensions that span a line wrap went in collapsed, and 4 needed the raw form.
- Only the 79 receipts holding an accepted key changed.  `git status` matches the ledger exactly.

## The counts, against the advance statement

| bucket | before | after | stated in advance |
|---|---|---|---|
| `UNADJUDICATED` | 2,167 | **2,073** | − N_U, where N_U = 94 |
| `EXTENDED` (new) | 0 | **108** | + N, where N = 108 |
| `DELIBERATE` / `ALT-OK` / `ENCODING-OK` / `REPAIR-OWED` | 312 / 62 / 24 / 15 | 307 / 57 / 21 / 14 | each down by its own keys that went through |
| `UNADJUDICATED-PINNED` | 102 | 102 | unchanged |
| `UNADJUDICATED-LIST` | 60 | 60 | unchanged |
| `MULTI` | 249 (122/127) | 249 (122/127) | unchanged |
| total keys | — | — | unchanged, and it is |

`check_quote_pins` is green, with no new key and no stale entry.  Each prior verdict is kept in its new row's last
column.

## What did not go through: 50 keys, every one restored to HEAD

| reason | paper | source | |
|---|---|---|---|
| `DIVERGENT`: a multi-site key whose sites need different extensions | 4 | 16 | **not predicted** |
| `RED-AFTER`: the receipt is red with either form of the extension | 3 | 19 | P2 |
| `NO-TOKEN`: no string token in the receipt equals the literal | 5 | 0 | P3 |
| `NOT-DISCRIMINATING`: the extension matches a further site where a reversal survives | 3 | 0 | P5 |

- **`DIVERGENT` is a class I did not foresee.**  Twenty keys sit at several sites across the papers or sources,
  even though the baseline counts them single-site in the one file their trace names.  One literal cannot be the
  minimal extension at sites whose neighbours differ, so I left them alone rather than pick a site.
- **The three `NOT-DISCRIMINATING` keys came from a gap in my own engine.**  `apply_batch.py` did not run acceptance
  check (b) itself.  I ran it afterwards across all accepted keys, found three still in a reversal class, and
  reverted them under the pre-registered rule.  Each extension newly matched a second site where a reversal
  survives.

## Predictions against outcome

| | predicted | measured | |
|---|---|---|---|
| P1 keys through | 120–145 | **108** | **miss, low** |
| P2 `RED-AFTER` (text not as the receipt reads it) | 10–30 | 22 | hit |
| P3 `NO-TOKEN` | 3–12 | 5 | hit |
| P4 prose-span failures | 0 | 0 | hit |
| P5 no key fails acceptance (b) alone | 0 | **3** | **miss** |

P1 missed mostly because of the unforeseen `DIVERGENT` class: 20 keys, three-quarters of them on the source half.

## ⛔ What the batch turns red that it does not own: three of `60`'s receipts, and the fix is `60`'s

| receipt | gate | what it asserts | why it goes red |
|---|---|---|---|
| `S4_the_exact_count_on_a_set_another_seat_can_grow…` | Ⓐ② | live unadjudicated `== 2167` | the batch lowers it to 2,073 |
| `S6_an_unread_figure_is_a_claim_with_no_gate…` | Ⓔ① | `len(_unadj) == 2167` | the same |
| `S3_the_openness_subclass_is_read_in_full…` | Ⓐ④, Ⓕ① | every baseline row moved or removed since its pin belongs to `60`'s own receipts | the batch moves rows in other seats' receipts, as ordered |

- All three are green on HEAD and red only with this baseline, as checked by a stash and run.  None holds a batch
  key, so under `r7225`'s boundary they are not mine to edit.
- **The repair, for `60`:**
  - in `S4` and `S6`, turn `== 2167` into `<= 2167`, the monotone form `S3` already uses for its own count;
  - in `S3`, read the "moved or gone" set only from rows its own revision stamped (its `r7204` stamp), not from
    every difference since its pin.
  - This is `S4`'s own subject, an exact count on a set another seat can change, met in `S4` and its neighbours.
