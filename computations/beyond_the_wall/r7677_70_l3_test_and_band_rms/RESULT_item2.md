# r7679+70 — RESULT, the band-RMS sweep on the arm of record (r7677 item 2)

**Nothing moves it on the arm of record either.**
- `fixed` sits at **1.0598**, flat across every refinement of every axis. The namesake was 1.0587.
- `sweepown` sits at **1.0611–1.0613**. The namesake was 1.0659–1.0660.
- The worst last step over all twelve axis readings is **0.011%** (sweepown/LSTEP), against the 0.6% floor. The namesake's was 0.008%.
- **Two of the twelve readings are now reportable as converged**, not one: `fixed/KFAC` turns over on the arm of record, alongside the namesake's `sweepown/NLOSW`. The counts are 2 converged, 6 not-turned-over, 4 two-points-only, against the namesake's 1 / 7 / 4.

Bank change: **addition**, `spectra/r7041_band_rms_leafrec1.npz` (137 kB): `ls__`, `Dl__` and `l_A__<tag>` for all 44 folded configurations, plus `config` and `manifest`.

## What was built

`launch_band_rms.sh` is r7041's `launch_sliced.sh` injection set:
- **CR legs (20):** 2 injections × 10 settings at the refit licensed point, LEAFREC=1. `nk15`/`nk20` are `base` on the arm by construction: the arm's k ladder never reaches the NK cap, and r7669 ③'s GRIDSAVE grids are byte-identical on the arm of record too.
- **Control legs (24):** 2 × 12 at the recorded control point with LEAFREC=1. NK is real there. LEAFREC does not reach the control (r7669), so these equal the namesake control. They had to be built because the namesake's folded runs live only in `/tmp/n66` and were never banked.
- **Settings for every run:** `HIER=1 LSTEP=8 LMAXL=2000`, sliced 250 wide, 475 slices, each declaring `__SLICE__ lo:hi`.
- **Folding:** `r7041_directions/fold.load` folded every configuration and checked that its declared slices tile [0, modes) exactly. Slices per configuration: 6 to 21.
- **The first, unsliced launch was lost** to a container restart at about 100 minutes. The container is reclaimed when the session idles without a harness-tracked background task, which happened three more times; each cost only the slices in flight.
- **Compute:** 22 300 s of wall for the final launch on 4 cores, about 25 CPU-h in all. Heaviest per slice: `nlos2240` (about 1070 s) and `lstep4`.

**Scoring** (`fold_band_rms.py` → `band_rms.json`): the receipt's own `env_a`, `osc`, `verdict`, `SEQ`, `FLOOR`, `LO`/`HI`/`NG` and `INERT_ON_ARM` are lifted by `ast`. The ratio is its `from_bank` arithmetic, pointed at this bank.

## The twelve sequences (arm of record)

| axis | fixed | sweepown |
|---|---|---|
| KFAC (base, 2.6, 3.2, 4.0) | 1.0597818, 1.0597819, 1.0597819, 1.0597819 — **converged** | 1.0612331, 1.0612828, 1.0612849, 1.0612850 — not turned over |
| NK (base, 1274, 1698) | 1.0597818 ×3 — not turned over | 1.0612331, 1.0612330, 1.0612330 — not turned over |
| NLOS (base, 1120, 2240) | 1.0597818, 1.0597815, 1.0597815 — not turned over | 1.0612331, 1.0612297, 1.0612289 — not turned over |
| NLOSW (base, 9, 12) | 1.0597818, 1.0597814, 1.0597813 — not turned over | 1.0612331, 1.0612278, 1.0612286 — **converged** |
| NLOSF (base, 0.90) | 1.0597818, 1.0597832 — two points only | 1.0612331, 1.0612576 — two points only |
| LSTEP (8, 4) | 1.0597818, 1.0597364 — two points only | 1.0612331, 1.0611165 — two points only |

- **Last steps, largest first:** sweepown/LSTEP 0.0110%, fixed/LSTEP 0.0043%, sweepown/NLOSF 0.0023%, and every other reading under 0.0002%.
- **Per-axis counts, unchanged:** five axes move the ratio on the arm (NK inert by construction) and six on the control.

## For P15 l.1857 and the receipt

**What l.1857 prints, and the arm-of-record values:**

| l.1857 figure | namesake | arm of record |
|---|---|---|
| fixed | 1.0587 | **1.0598** |
| own-clock | 1.0659–1.0660 | **1.0611–1.0613** |
| worst last step | 0.008% | **0.011%** |
| per-axis counts | five / six | five / six (unchanged) |

**Two things in the receipt would change if repointed:**
- its `assert round(worst, 3) == 0.008` would read 0.011;
- its `exactly one converged, sweepown/NLOSW` would read two, `fixed/KFAC` and `sweepown/NLOSW`.

The pre-registration (P6) said the verdict counts were not registered to hold, because they turn on step signs at the 1e-7 level. `fixed/KFAC`'s steps are +7.1e-8, +4.2e-10, +1.1e-10 on the namesake (monotone) and +7.2e-8, +2.3e-10, −7.7e-10 here: the last step changes sign at the 1e-10 level, which is what "turned over" reads.

**Predictions:**
- P5 holds: base `fixed` within 0.01 of 1.0587 (+0.0011); `sweepown` within 0.01 of 1.0660 (−0.0048); every last step inside the floor; the worst under 0.05%.
- P4 (price) missed on wall time: about 2 h CR plus 3.5 h control was registered, about 6.2 h was run, and the restarts cost more.
- P6 was not registered, and the counts did move.

## Gates

- `check_banked_config`: passes.
- The receipt itself, run by stem, passes on its banked table. It does not yet read this bank; that repoint is cc66's.
- `run_touched_readers.sh --class1`: GREEN.
