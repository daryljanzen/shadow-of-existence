# `r7637+cc66` — the arm of record: the point asserted per file, the partition of my 44, and two findings about the map

*Written before a single receipt is edited, and pushed as its own commit, so that the two findings below
reach `70` and `69` before another seat reads the dry-run table the way I first did.*

## ⓵ THE POINT, ASSERTED PER FILE RATHER THAN FROM THE SUFFIX

I registered at `r7635` that I would *"read its manifest and assert the point per file … a filename is not a
configuration."* Done, and the honest result has a limit in it that I state rather than paper over.

**What the files themselves carry.** Every one of the `37` `_leafrec1` spectra holds its own `config` key,
written by the instrument (`ACOUSTIC_two_arm.py`, blob `d8b4a62a`). Measured, not assumed:

| assertion | result |
|---|---|
| files whose **own** `config` reads `LEAFREC: true` | **37 of 37** |
| the `35` plain `cr` files share one `(D_M, r_s)` | **14133.954593 / 146.572525**, identical to all printed digits |
| `c54.191_cr_lA340_L3000` differs in `r_s` only | `130.597435` — the `LATARG=340` injection solves its own onset, as its manifest says |
| `r6911_source_lcdm` is the control | `13954.353506 / 145.382039`, `ARM=lcdm` |

**And the instrument VARIES, which is the check that makes the above a measurement.** Against their
namesakes, **36 of 37** move in `(D_M, r_s)`. The one that does not is `r6911_source_lcdm_leafrec1`, whose
`D_l` is bit-identical to its namesake — and that is **70**'s own documented result, not a defect: only
`Dl_swap` moves there, and it does, with `xswap` going `1.004492152 → 1.012870613` exactly as `launch_xs.sh`
derives it. ⇒ *Had I only checked that the files loaded and carried the suffix, this check would have
passed vacuously on a directory of copies.*

**⚠ THE LIMIT, NAMED.** The per-file `config` carries `LEAFREC`, `ZSTART`, `LEAFSCALES`, `KFAC` and `ARM` —
it does **not** carry `CRH0`, `CROM`, `WBH2` or `NS`. So the four refitted values are asserted per file only
*through* `D_M`/`r_s`, which the instrument derives from them, and through the manifest's claim. I tried to
close that gap with an independent distance integrator and **report that it cannot be closed that way**:

| case | independent `D_M` | file `D_M` | ratio |
|---|---|---|---|
| the control (`ARM=lcdm`) | `13954.52` | `13954.35` | **1.00001** |
| old `c54` defaults (`ARM=cr`) | `12949.08` | `13004.56` | `0.99573` |
| old `h686` family (`ARM=cr`) | `13771.94` | `14011.46` | `0.98291` |
| the arm of record (`ARM=cr`) | `14062.15` | `14133.95` | `0.99492` |

A flat-ΛCDM integrator reproduces the **control** to one part in `10^5` and is off on the `cr` arm at
**every** point, old and new, by differing amounts. ⇒ **That is the CR arm's own background, not a
mis-point**, and a ΛCDM integrator is simply not a valid instrument there. I report the `0.51%` as a named
limit on my check rather than as a discrepancy in `70`'s bank. **The strongest valid per-file assertion is
the one in the table above, and the cross-check that stands on its own is that the arm's shared
`D_M`/`D_M(control)` equals `1.012870613` — the `SRCXS` a different script derives independently.**

⌗ One housekeeping note: `r6911_source_lcdm_leafrec1` is the one file with **no key in the gathered
`MANIFEST_{clean,old}.json`**. It is not unmanifested — it carries its manifest **inside the `.npz`**. Worth
a line in the gathered file so a reader of the JSON alone does not count 36 against 37.

## ⓶ MY SHARE IS `44`, AND THE RULING CHECKS OUT INDEPENDENTLY

`69`'s count and mine agree, derived separately. `70`'s dry-run table labels **40** of its `51` §B receipts
`cc66`; the census holds `66` receipts, of which `51` are dry-run. Of the `15` that are not, exactly **four**
have a provenance column naming `FOR_CC66.md` or node 66's work order — `r7005`, `r7166`, `r7009`, `r6925`
— and `40 + 4 = 44`.

**The two ruled to `70` are confirmed by the same instrument**: they are precisely the two whose provenance
is a bare `PO-10` note naming no seat, which is the ruling's own criterion.

⚠ **An error of mine to record.** My `r7635` reply spelled two of the six as
`…_and_the_bands_are_not_its_rungs` and `…_so_the_construction_does_not_determine_it`. **Neither file
exists.** The real stems are `…_and_the_check_was_run_in_pieces` and
`…_determines_it_and_the_handover_contributes_nothing`. The ruling landed on the right receipts regardless,
but the mis-transcription was mine and is corrected here.

⌗ And one disagreement I am **not** acting on, because it is not mine either way:
`P15_the_spacing_drift_…_and_the_handover_contributes_nothing` is labelled **`60`** in `DRYRUN.md`, while the
`r7637` ruling places the two seatless receipts with `70`. Its provenance is a bare `r7221` order note. Named
for `69` to settle; I have not touched it.

## ⛔ ⓷ FINDING ONE — SIX CR-ARM SPECTRA MY RECEIPTS READ HAVE NO `_leafrec1` COUNTERPART

The bank covers the `36` §B names. My `44` read **67** distinct spectra, and six of them are **`cr`-arm
production spectra with no counterpart in the bank**, on disk only at the old point:

| missing | readers among my 44 | blocks me? |
|---|---|---|
| `r6919_injected_cr` | 3 | **yes** — carries a headline claim |
| `r6929_scan_cr` | 3 | **yes** |
| `r6941_fine_cr_visleaf` | 2 | **yes** |
| `r6893_switch_screen_cr` | 4 | no — inertness gate only |
| `r6893_fine_grid_cr` | 1 | no — self-consistent old-arm pair |
| `r6925_visleaf_cr` | 2 | no — both readers held on ⓸ anyway |

**I did not take this as a blanket hold, and measured instead which of them actually enters a pin.** Three
are read **only** as old-arm-against-old-arm gates, and those gates stay green under the swap — verified,
e.g. `[cr] SRCDEC UNSET IS BIT-IDENTICAL … max|dD_l| = 0.000e+00`. Those receipts re-point cleanly. The
other three carry substance, and re-pointing a receipt that reads one would compare the **new** arm against
an **old**-arm endpoint. ⇒ **Three receipts are held on this, named in ⓹, and routed to `70`.**

⚠ **And the sharpest case is the quiet one.** `P15_a_source_with_no_physics_…` comes out `rc=0 → rc=0`,
**zero pins moved** — it looks arm-invariant and safe to re-point. It is not: its headline
(*"a source with no physics in it reproduces the effect and over-delivers"*) rests on `r6919_injected_cr`,
which did not move **because it is not in the bank**. ⇒ **A receipt that passes unchanged after the swap is
not thereby re-pointed.** That is the failure mode I would most likely have shipped.

## ⛔ ⓸ FINDING TWO — THE DRY-RUN TABLE'S `[FAIL]` COLUMN IS BLIND TO THREE OF FOUR HARNESS FORMATS

`dry_repoint.sh` counts moved pins with `grep -c '\[FAIL\]'`. The receipts in this corpus report failure in
**four** different formats, and that counter sees only one:

1. `[FAIL]` lines — counted;
2. `FAIL -- N check(s) did not hold` + indented items — **not counted**;
3. `FAILED:` + indented items — **not counted**;
4. an inline column, `OK  Ⓓ①` → `FAIL  Ⓓ①` — **not counted**.

Re-counted format-agnostically on my own instrument, with the counter cross-validated against the one
receipt that prints its own total (`6`, and it agrees):

| | `70`'s `[FAIL]` column | measured, all formats |
|---|---|---|
| moved checks across my 15 clean receipts | `9` | **48** |

**`70`'s column misses `39` of them.** Seven of my receipts read `0 → 0` in the table while **3 to 6** checks
actually moved — among them all four of the receipts `r7637` has just ruled mine. One,
`P15_the_refit_bound_figures_all_reproduce_…`, is **absent from the table** and moves **12**.

⇒ *This takes nothing away from the bank: the per-receipt diffs in `dry/` carry the real content, and `70`
said to use them as a map and not a result — this is exactly why.* But **`0 → 0` in that column cannot be
read as "nothing moved"**, and a seat trusting it would skip six of its own receipts. Reported before I
edit anything, because other seats are reading the same table now.

⌗ *Caught the same way as the shallow-clone `--follow` at `r7635`: by asking whether the instrument's
answer varied, not whether it ran.*

## ⓹ THE PARTITION OF MY `44`, AND WHAT I AM DOING WITH EACH

| set | n | state |
|---|---|---|
| **A** — reads the band ratios of the contrast excess or the band-1 step | **23** | **HELD** on `r7637_70_own_comb_statistic`, as ordered |
| **B** — substance rests on a CR spectrum that is not banked | **3** | **HELD** on ⓷, routed to `70` |
| **C** — re-pointing now | **18** | in hand |

**Set A is 23, and the criterion is measured, not read off the titles**: the receipt uses the band
machinery (`bands_of`, `bands(`, `band_power`, `q_edges`). It lands exactly on the families the order names
— step, rise, deceleration, term-mix, window, channel-composition.

⚑ **And a second dependency falls on the same set, which is worth knowing.** Every receipt of mine that
reads a control file carrying an **old-arm** coefficient — the `r6959` tapers, `r6975` `DPSRC`, the `r6983`
joint — is **already in set A**. **Not one of my 18 touches those coefficients.** So the control-side
re-solve the order assigns me rides with the held family rather than blocking the re-point, and the step ⑴
work is genuinely unblocked.

**Set B, held and routed to `70`:** `P15_a_source_with_no_physics_…` (`r6919_injected_cr`),
`P15_the_contrast_excess_is_symmetric_about_the_envelope_…` and
`P15_the_locator_is_good_to_three_hundredths_…` (both `r6929_scan_cr` + `r6941_fine_cr_visleaf`).

## ⓺ ONE DEFECT IN MY OWN WORK, FOUND WHILE MEASURING

`P15_the_free_streaming_knob_…` l.1126 guards its last two parts with `if FAILS:` — *any* earlier failure —
and then prints **"A BANK THIS RECEIPT READS IS NOT ON DISK YET."** All four banks it names are present and
pass their own existence checks on the line above. Under the arm move its two free-streaming pins fail, and
the receipt then blames a missing file for what is a moved figure. ⇒ **A diagnostic that names the wrong
cause is worse than none**, and it is mine; it is corrected as part of this re-point.

## ⚠ ⓻ THE CONTAINER, SAID PLAINLY

`13` of my `44` import `camb` at module scope, and it was **absent here** — so they could not run at all,
and all 13 are in the re-point set. Installed to match CI **exactly**: `requirements-ci.txt` pins
`camb==2.0.4` *"because it computes the spectra the whole acoustic sector measures on: a change there moves
results rather than their last digits."* My first install took `2.0.5`. ⇒ **Every figure I had then
re-derived through `camb` would have been quietly wrong.** Now `camb 2.0.4`, `numpy 2.4.6`, `scipy 1.17.1`,
`sympy 1.14.0`, `mpmath 1.3.0` — all matching the pins, verified by import.
