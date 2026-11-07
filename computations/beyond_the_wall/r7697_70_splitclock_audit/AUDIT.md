# r7697+70 — AUDIT: what in print still rests on `SPLITCLOCK=1`

**Read, not fixed.** `SPLITCLOCK=1` is HIER's split with the retired `STACKPERT` pairing.
- **In print:** two papers carry it, at four sites: P15 `CR_cosmology.tex`:2823–2832 and `CR_synthesis.tex`:1494. Every one is a low-ℓ hierarchy figure, and each has an (L) counterpart banked at r7695.
- **In receipts:** one receipt, the low-ℓ gap receipt, carries it in four check blocks, two of which call `=1` rows "the arm of record".
- **Nowhere else:** no acoustic-sector figure rests on it (the acoustic sector is `ACOUSTIC_two_arm.py`, `LEAFPERT` by default), no other receipt reads an `=1` bank, and `SPLITIC` is in no bank and no print.
- **"Ninety-six per cent the clock's physics"** is not in any paper. It is in `THE_CONSOLIDATION_LEDGER.md`:1130, and it is superseded.

**How it was found:**
- every banked `.npz` in the tree was scanned for `SPLITCLOCK`/`SPLITIC` in its `config` or `manifest`;
- every file that names those banks was grepped;
- the papers (`corpus/*.tex`) and receipts were grepped for the `=1` figures (0.456/0.459/0.465/0.468/0.4589/0.4649/0.4680, "five and a half", "two-clock split", "octopole", "4.9 per cent", "96 per cent").

## 1. Banks built with `SPLITCLOCK=1` (all mine)

| bank | `=1` rows | point | (L) counterpart |
|---|---|---|---|
| `spectra/cc66_lowell_sweep_leafrec1.npz` (r7675) | `FROZEN_adjudicated_KLO_0_1`, `DECOUPLED_adjudicated_KLO_0_1_NS3_60000` (ℓ = 2–8) | refit | `p15_lowell_depths_leafpert_leafrec1` `refit__armB_{frozen,decoupled}__L` |
| `spectra/p15_lowell_depths_leafrec1.npz` (r7681) | `armB_frozen`, `armB_decoupled` (its `armA_exact` is one clock) | refit | the same rows above, plus `p15_lowell_depths_armA_leafpert_leafrec1` `refit__armA__L` |
| `spectra/p15_lowell_depths_distances_leafrec1.npz` (r7683) | `armB_frozen`, `armB_decoupled` (its `armA_exact` is one clock) | distances | `p15_lowell_depths_leafpert_leafrec1` `distances__armB_{frozen,decoupled}__L`, plus `p15_lowell_depths_armA_leafpert_leafrec1` `distances__armA__L` |

- **`SPLITIC`:** in no bank. It appears only in `r7677_70_l3_test_and_band_rms/l3_test.json`, unbanked and read by no receipt.
- **The r7675 run's `result.json`:** unbanked, and read by no receipt.

## 2. Receipts that read an `=1` bank

**Only one:** `receipts/P15_CR_cosmology/P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py`. No other receipt names `SPLITCLOCK`, `SPLITIC` or any of the three banks.

| lines | reads | what it asserts on `=1` rows | (L) counterpart |
|---|---|---|---|
| :244–:285, :466–:500 (check :493) | `cc66_lowell_sweep_leafrec1` as `SW_AOR` / `B_AOR`, **labelled "arm of record"** | the two builds agree (diagnostic); minimum 4 and recovery 8 on both | the refit (L) rows: minimum 4 and recovery 8 hold; the builds agree within 3.5% |
| :515–:570 (checks :518, :553, :555) | `p15_lowell_depths_distances_leafrec1` arm-B rows (`_DF`, `_DD`) | five pinned figures: octopole residual **+5.54%**, largest DECOUPLED residual away from ℓ = 3 **2.33%**, above ℓ = 5 **0.57%**, build spread at ℓ = 4 **−4.90%**, at ℓ = 3 **−0.67%**; the conclusion (4, 8) on both | the (L) rows against arm A (L): octopole −0.88% (DECOUPLED) and −0.73% (FROZEN); largest DECOUPLED residual 2.91% (ℓ = 4); above ℓ = 5, 0.16%; build spread at ℓ = 4 −3.28% and at ℓ = 3 +0.16%; (4, 8) holds |
| :575–:600 (checks :579, :593, :596) | the same arm-B rows against the one-clock bank | "**the octopole's excess is the two-clock split's**, measured by turning the split off" | now known to be 72–77% the retired pairing's dynamics; under (L) the excess is absent (above) |
| :610–:625 (check :613) | `SW_AOR`'s manifest `point` | a point fact, not split physics | unaffected |
| :726–:790 (checks :752, :757, :761) | `_AOR` = the **`=1` DECOUPLED** distances row, **labelled "the arm of record's depth"** | the seven depths pinned (0.478 / 0.459 / 0.358 / 0.651 / 0.906 / 0.982 / 0.998); "six of seven printed depths change"; "the octopole is the largest move, upward" | arm A (L) at the distances point: 0.485 / 0.441 / 0.354 / 0.657 / 0.909 / 0.983 / 0.999. Against print (0.487 / 0.435 / 0.359 / 0.666 / 0.911 / 0.983 / 0.998), six of seven still move at three decimals (ℓ = 7 does not); the octopole moves +0.006 and ℓ = 5 −0.009, so **the octopole is not the largest move** |

The checks at :747 (the exact transfer as printed) and :777 (the one-clock cross-validation) rest on one-clock rows, not on `=1`.

The cc66 computation scripts that read these banks are working files, not receipts, and none is in print: `r7667_cc66…/census.py`, `r7675_cc66…/onesent.py`, `r7685_cc66…/build_spread.py` and `r7687_cc66…/clause_scope.py`.

## 3. Printed figures that rest on an `=1` row

| site | printed | rests on | (L) counterpart (r7695) |
|---|---|---|---|
| P15 `CR_cosmology.tex`:2823–2824 | the hierarchy agrees "to within three per cent at every multipole but the octopole, where it sits **five and a half per cent high**, and to one per cent above ℓ = 5" | receipt :553 (`=1` DECOUPLED distances against one-clock arm A) | arm B (L) against arm A (L): within 2.9% at every ℓ = 2–8, the octopole included (−0.88%), and 0.16% above ℓ = 5. **Exists** |
| P15 `CR_cosmology.tex`:2828–2830 | the two builds "differ by up to **4.9** per cent … at ℓ = 4, where the decoupled build sits **0.25** per cent from the exact transfer and the frozen one **5.15**" | receipt :553 (`=1` FROZEN and DECOUPLED) | at ℓ = 4: DECOUPLED −2.91% and FROZEN −6.19% from arm A (L); spread −3.28%. **Exists** |
| P15 `CR_cosmology.tex`:2830–2831 | "At the octopole, where the hierarchy sits **five and a half per cent high**, the two treatments agree to **0.7** per cent and the excess survives both" | receipt :553 (spread at ℓ = 3 −0.67%) | at ℓ = 3: −0.73% / −0.88% from arm A (L), spread +0.16%; **no excess to survive**. **Exists** |
| P15 `CR_cosmology.tex`:2831–2833 | "**and it goes with the hierarchy's two-clock split**: with the split turned off the hierarchy sits 1.0 and 1.1 per cent below the exact transfer" | receipt :593/:596 (the one-clock numbers are the r7689 bank, not `=1`; the "two-clock split" is `=1`) | the shift was 72–77% the retired pairing's dynamics and +0.007 projection; under (L) the hierarchy sits +0.5 / +0.6% above one-clock arm A and −0.7 / −0.9% below arm A (L). **Exists** |
| P16/synthesis `CR_synthesis.tex`:1494 | "the two transfers agreeing to three per cent away from the octopole, and to **five and a half per cent at it**" | the same as :2823 | under (L): to 2.9% at every ℓ, the octopole included. **Exists** |

**Not resting on `=1`:**
- P15 :2821–2822's seven depths (0.487 / 0.435 / … / 0.998) are the one-clock exact transfer, which r7693 re-keyed `armA_exact`.
- :2826–2827's convergence clause and :2833–2834's "minimum at ℓ = 4, recovery by ℓ = 8" also hold under (L) on every row.
- The appendix entry `appendix_receipts_P15.tex`:985–988 carries no `=1` figure.

## 4. Readings outside print that rest on `=1`

- **"The low-multipole octopole shift is about ninety-six per cent the two-clock split's physics"** (`THE_CONSOLIDATION_LEDGER.md`:1130, from my `r7677_70…/RESULT_item1.md`). That 96% was the `=1` split's shift against two construction choices (onset and `SPLITIC`). r7695 now separates it: 72–77% is the retired pairing's dynamics and about 25% (+0.007) is the arm of record's projection. **Superseded.** It is a ledger and history line, not print.
- **"The photon hierarchy carries the two-clock split"** (`THE_CONSOLIDATION_LEDGER.md`:1128). True of `=1` as built, and it now reads as the retired pairing. History line.
- **My own r7675 HIER comment** that `SPLITCLOCK=1` "does exactly that" (the arm of record's split) was corrected in place at r7695 (`HIER_photon_hierarchy.py`, the ⛔ r7693+70 note).
- **"Split-clock acoustic figures":** none. No acoustic receipt runs HIER with `SPLITCLOCK`. The acoustic sector is ACOUSTIC_two_arm on its own `LEAFPERT` default, which is the (L) construction already.

## 5. One thing to note for the re-point

The receipt's :757/:761 checks ("six of seven change and ℓ = 8 does not"; "the octopole is the largest move, upward") are claims about the `=1` row. On arm A (L) the corresponding statements are:
- six of seven printed depths still change at three decimals: ℓ = 2 (−0.002), 3 (+0.006), 4 (−0.005), 5 (−0.009), 6 (−0.002) and 8 (+0.001). It is ℓ = 7 that does not change, not ℓ = 8, which is the one the check names;
- the largest move is at ℓ = 5, not at the octopole.

cc66's re-point onto arm A (L) will need both checks rewritten, not just re-pointed: the first changes which multipole holds, and the second becomes false.
