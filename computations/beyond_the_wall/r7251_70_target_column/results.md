# `r7251+70.4` — results: the operator's `target` column repaired, for 29 keys

*Pre-registered at `PREDICTION.md` (`28932672`). The change is in `scripts/mutate_assertions.py`: `_reads`,
`_trace`, `_only_tex` and the `tasg` binding in `quote()`. The list of flipped keys is `FLIPS.tsv`.*

## What changed

The operator decides whether a site is a key exactly as before. The narrow trace is unchanged.

A **second, wide** trace is consulted only to file a key as `PAPER`. It does two extra things:

1. it keeps every helper body it visits, so the `corpus/*.tex` glob in `papers()` is seen beside the `open()` in
   `body()`;
2. it binds loop variables to what they iterate, so `for pid, fn in WANT.items()` reaches `WANT`'s `.tex` names.

A key is filed `PAPER` by the wide trace **only if `.tex` is the only file kind it names**.

## Results over the operator's full output

| # | predicted | measured | |
|---|---|---|---|
| T1, `SOURCE` → `PAPER` | 150 (40–400) | **29** | **REFUTED LOW** |
| T2, `PAPER` → `SOURCE` | 0 (0–3) | **0** | held |
| T3, keys gained or lost | 0 | **0** (2,786 before and after) | held, in the final form; see below |
| T4, the 9 `L204` keys | 9 of 9 | **9 of 9**, plus `P2`'s `stress tensor` | held |
| T5, cc66's `C4` keys | not predicted | **14 of 16**. The other 2 are formulas read from a non-paper source | — |

The 29 flips are in 7 receipts:

- 14 in cc66's `C4`;
- 10 in `L204` (`P7` 6, `P2` 3, `P3` 1);
- 2 each in `D2` and `F1`. Their literals are regex patterns run over the papers;
- 1 in `I7`.

**My T1 guess was five times too high.** The runtime-path pattern is confined to a handful of receipts.

## The two wirings that failed first, and why the final one is narrow

1. **Keeping helper bodies only inside a branch that reads gave 14 flips and missed `C4`.** The loop variable
   `fn` was a dead end.
2. **Passing the loop-bound map to `_reads` itself** gave 41 flips, but it **changed the key set: 108 keys
   gained and 25 lost.** It also gave 28 flips the other way, from `PAPER` to `SOURCE`. That is because `_reads`
   decides keyhood too, so the pre-registered T3 claim was false for that wiring.
3. **Splitting the roles fixed T3.** The narrow trace decides keyhood and the wide one decides `PAPER`. But one
   step still flipped 5 keys in `L250`/`Q1` and 3 in `S1` that are not paper pins:
   - `Q1`'s container is a helper's return message;
   - `S1` reads `.py` files, but the name `c` was bound in another loop over `.tex` files.
4. **The `.tex`-only rule removed those 8**, and every remaining flip checks out by hand.

## Not changed, and routed

- **The baseline's `target` column is not rewritten.** cc66's `C64` Ⓔ asserts that the column misreads `C4`,
  so it goes red when the column is right. That gate pins a defect in its as-found state.
  - If 66 wants the baseline corrected, `FLIPS.tsv` is the change, and `C64` Ⓔ needs converting in the same
    revision.
  - `check_quote_pins` keys on `(receipt, literal)`, so the operator and the baseline disagreeing on `target`
    fails nothing.
- **`cannot_fail` still uses the narrow trace for its target.** Moving it would change what that ratchet
  measures, and it was not ordered.
- **Checks:** `check_quote_pins`, `check_prose_pins`, `check_cannot_fail`, `check_exact_counts`,
  `check_tilt_pins`, `check_unread_figure`, and the two receipts that import the operator (`S5`, `S7`) all
  exit 0.
