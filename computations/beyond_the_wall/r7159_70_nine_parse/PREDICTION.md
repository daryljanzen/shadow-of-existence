# r7159+70.1 — PRE-REGISTRATION: the `PARSE` repairs, on the r7153 template

*Committed before any receipt is edited.  Node 70.  Read at `origin/main` `05ffab46`.*

## Scope (r7159 ⌗ live 1), and what is NOT touched

Of r7157's 12 `PARSE` sites, one (`P15_the_sky_phase_fit…:45`) was repaired by the gate at r7159, and two sit in
receipts of a LIVE seat, `cc66` (`P10_the_floor_is_forced…`, r6863+cc66.31; `P10_the_thermal_condition…`,
r6849+cc66.30). **Those two are routed to `cc66`, not edited.**  The 9 repaired here are in four receipts that no
live seat authored (gate revisions r3166, r4068, r2419, r4231):

| receipt | sites | paper, anchor |
|---|---|---|
| `L274/H1…` | 1 (`l≈8`) | `CR_cosmology`, "recovering by $\ell\approx8$" |
| `L831/G1…` | 3 (`3`, `6`, `6`) | `SdS-slicing-curve_v2` `sec:tour`, the one display |
| `P05_deck_group_S3` | 1 (order `12`) | `groupoid_paper` `sec:classification`, `(\text{order }12)` |
| `P10_the_adiabatic_residual…` | 4 (`0.61`, `0.44`, `0.16`, `2.32`) | `canonical_time`, two sentences |

**The template (r7153):** open the paper, parse the figure from its own sentence with a pattern that must match
EXACTLY ONCE (else fail), assert the receipt's measurement against the parsed value, and name the paper's figure
in the label as parsed, never as a literal.  The receipt's own measurement and tolerance are unchanged.

## Predictions

- **Q1** every repaired receipt exits 0 with the same number of checks as before.
- **Q2** `check_unread_figure` owed falls 48 → 39; the four receipts' sites leave `NO-READ` (STALE rows removed,
  their new `READS-PAPER` rows recorded `REPORTED`), and the gate passes.
- **Q3 (each repair reads)** perturbing the parsed figure in a scratch copy of the paper, one site per receipt, makes
  that receipt fail; restoring it restores the pass.
- **Q4** every parse pattern matches exactly once on the current papers.
