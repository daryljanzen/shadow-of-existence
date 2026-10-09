# r7225+70.1 — the `EXTEND-SHORT` batch at 158: method, count changes and failures, pre-registered before any edit

*Ordered at `r7225`.  This is the first pass in this line that edits files.  The scope is exactly the 158 keys
and their baseline rows.  No other receipt, verdict field or baseline row changes.*

## Inputs, seen before writing (composition only, no outcome)

- 158 keys: 82 paper `REVERSAL` keys and 76 source `REVERSAL`/`PARTIAL` keys, in `EXTEND-SHORT` (D ≤ 25) on the
  `r7223+70.1` wrap-tolerant count.  They sit in 108 receipts (`batch_inputs.json`).
- Current baseline verdicts: **141 `UNADJUDICATED`**, 7 `DELIBERATE`, 5 `ALT-OK`, 4 `ENCODING-OK`, 1
  `REPAIR-OWED`.  None is `UNADJUDICATED-PINNED` or `UNADJUDICATED-LIST`, and none carries `MULTI` in the
  baseline.

## Method, fixed now

For each key:

1. **The extension** is the minimal-D extension `r7215`/`r7221` measured.  It is the extended raw substring at the
   key's site in the pinned body `S7`/`S8` read, preferring the leftmost on ties.  For a source key the prose-span
   bound applies, as at `r7221`.
2. **The edit**: every Python string token in the receipt whose value equals the old literal is replaced by the
   extended string, written with the same quote style and escaping.  Docstrings and comments are skipped.  Labels
   are left alone unless their value is exactly the literal.
3. **Acceptance, all of these or the key is reverted**:
   - (a) the edited receipt runs green;
   - (b) `S7`/`S8`'s own `reversals()` on the key's clause breaks the extended string, so the key leaves the
     reversal classes;
   - (c) `--quote` reports the new key from the same site.
4. **The baseline swap**: the old row is removed and the new key added with the verdict **`EXTENDED`**.  Its last
   column records the old literal, D, and the prior verdict, which is kept rather than overwritten.
5. **Order and stopping**: keys are processed receipt by receipt.  A receipt whose edit fails is restored from git
   before the next receipt.  If anything other than a single key failing its own acceptance goes wrong (the
   baseline does not reconcile, or a gate other than the expected count changes), **the pass stops there and
   reports**, with the baseline in a consistent state.

## Count changes, stated in advance (N = keys that go through, N_U = those of them that were `UNADJUDICATED`)

- `UNADJUDICATED` 2,167 → **2,167 − N_U**.
- `EXTENDED` (new) 0 → **N**.
- `DELIBERATE`, `ALT-OK`, `ENCODING-OK` and `REPAIR-OWED` each fall by however many of their keys go through.
- **`UNADJUDICATED-PINNED` 102, `UNADJUDICATED-LIST` 60 and `MULTI` 249 are unchanged.**  None of the 158 is in
  them, and an extension can only shorten a key's site list.
- The total key count comes out where it went in.  Each repaired key is one row out and one row in.

## Predictions

- **P1**: **120–145 of the 158 go through.**
- **P2, the commonest failure**: the extended string is not in the text the receipt reads at HEAD.  Either the
  paper or source changed after `S7`/`S8`'s pins, or the extension spans a line wrap while the receipt compares
  raw text.  10–30 keys.
- **P3**: the receipt has no string token equal to the literal (for example, it is built at run time): 3–12 keys.
- **P4**: the prose span stops the extension: **0**.  The 26 span-bound keys are all in `>300`, not in this batch,
  so `r7225`'s named failure mode does not apply to it.
- **P5**: no key that goes through lands anywhere but out of the reversal classes.  That is acceptance (b), so it
  holds by construction for the ones that pass.  The prediction is that **no key fails (b) alone**.
