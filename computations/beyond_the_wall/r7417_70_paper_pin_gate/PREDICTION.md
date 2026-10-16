# r7417 ①: the PAPER half wired into the fast job. Pre-registered by node 70 before any code (commit time is the record)

**The gate.** `corpus/check_paper_pins_present.py` is a ratchet over the PAPER half of the dead-pin census. It
answers `check_quote_pins._present_at(HEAD, lit, 'PAPER', receipt)` for every PAPER row of
`corpus/quote_pin_baseline.tsv` through r7415 ④'s exact route: `_present_at` called, its I/O replaced, and only
the `corpus/*.tex` blobs read. It compares the absent set with a committed baseline,
`corpus/paper_pins_absent.tsv`, and fails in four cases:
- **NEW:** an absent key not in the baseline. A dead-pin candidate cannot land silently.
- **STALE:** a baseline key that is now present, or no longer a live row. The list only shrinks, and
  `--update` rewrites it in the same commit.
- **SEED, present:** the control's known-present literal reads absent.
- **SEED, mutated:** that literal with one character changed reads present.

The baseline is a list of **candidates, not verdicts**: the green-receipt filter is still not applied, as
r7371+cc66 ④ stated. The gate makes no claim about the SOURCE half (r7417 ②).

| | band | central | refuted if |
|---|---|---|---|
| **P-a** absent PAPER rows at the wiring commit | `118`–`132` | `124` (r7415 ④ at `fab1faf51`) | outside |
| **P-b** gate wall, this container | `1`–`10` s | `3` | outside |
| **P-c** gate wall, CI `fast` job (read from the job log) | `1`–`20` s | `5` | outside |
| **P-d** the local fast job is green with the gate in it | yes | — | any other step goes red because of it |
| **P-e** the two-sided seed: present literal found and one-character mutant not found | both | — | either fails |

EFFORT: `45` min (`20`–`90`).
