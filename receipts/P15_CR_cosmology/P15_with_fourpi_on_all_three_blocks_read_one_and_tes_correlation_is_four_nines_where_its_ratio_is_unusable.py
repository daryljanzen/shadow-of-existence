"""
P15, r7861+cc66.8, on 69's orders r7859 ③ and r7861 ③ and ⑥.

** WITH `FOURPI` ON, ALL THREE BLOCKS READ ONE: TT `1.006625`, EE `0.994360`, AND TE -- WHOSE
PER-BIN RATIO IS UNUSABLE -- CORRELATES WITH CAMB AT `0.999959`.  THE PAIRS CLOSE AGAIN AT
`1.313e-15` WHERE THEY WOULD HAVE READ A HALF.  AND THE CALIBRATED REFERENCE'S PROFILE IS BANKED
FOR 60, WITH THE DRAG RULER'S LEVER OVER THEIR GRID TURNING OUT TO BE `Om` AND NOT `omega_b`. **

===================================================================================================
** ③ THE THREE-BLOCK CHECK, AGAINST BANDS REGISTERED BEFORE ANY OF IT EXISTED (r7859+cc66.1) **
===================================================================================================

  block   abs mean   |mean - 1|   per-bin spread      band        verdict
  TT      1.006625     0.006625         0.113269   |x-1| < 0.02   HOLDS
  EE      0.994360     0.005640         0.292787   |x-1| < 0.02   HOLDS
  TE      1.244761       --            26.881564   unusable, as r7855 declared it

  TE correlation with CAMB:  FOURPI=1  0.999959     FOURPI=0  0.999959
                             |difference| 2.220e-16                     < 1e-12   HOLDS

⇒ ** THE FACTOR TWO IS GONE FROM ALL THREE BLOCKS AND NOT ONLY FROM TEMPERATURE. **  TT and EE each
read one to better than seven parts in a thousand, inside per-bin spreads of `0.11` and `0.29`.

⛭ ** AND THE TE RESULT IS WORTH MORE THAN THE BAND ASKED FOR. **  Its per-bin ratio runs `-5.70` to
`21.18` and is as unusable as `r7855` said; its CORRELATION over the same `185` bins is `0.999959`.
So TE's SHAPE agreement is essentially perfect and the ratio's uselessness is entirely its three
sign crossings inside the instrument's reach.  ⇒ *That vindicates `r7855`'s refusal to quote a TE
mean, and answers "TE by its correlation coefficient" with a number saying the block is sound.*
  ⚠ ** IT IS NOT 60's STATISTIC. **  `r7861` reports *"TE's correlation coefficient at a median
  `0.0196`"*; a median is a per-bin or per-window quantity, this is the Pearson coefficient of the
  `185` binned values against CAMB's.  **The two are different objects and must not be read against
  each other.**

** THE EXACT FACTOR, AND THE CLOSURE. **  Against `r7855`'s switch-off point on an identical grid,
every block is exactly twice: worst departure from `2` of `1.332e-15` (TT), `1.110e-15` (EE),
`7.550e-15` (TE).  And the ten bilinear pairs close on their own saved `D_l` at `1.313e-15` with the
switch ON, against `1.308e-15` with it off and against the `0.500000` this seat measured on all four
banked `SRCDEC` files before 60's repair.  ⌗ *Both `Dl` and `Dl_pairs` scale by exactly two between
the legs, so the repair moved BOTH sides of the identity together -- which is why the closure
survives rather than merely appearing to.*

===================================================================================================
** ⑥ THE CALIBRATED REFERENCE'S PROFILE, AND THE DRAG RULER OVER 60's GRID **
===================================================================================================

The profile is ASSEMBLED from `r7853`'s own checkpoints and NOT re-fitted: re-fitting would publish
numbers that are not the ones the landed `54.00` and `30.56` meV limits came from.

⛔ ** AND THE BAND THAT MATTERED IS REFUTED ON BOTH LIMBS. **  `Ⓗ` registered that the ruler's range
over 60's eight displaced points is under `1.5` Mpc and that `omega_b` is the dominant lever.
Measured: the range is **`4.461444`** Mpc -- `H0m` at `149.1496` against `H0p` at `144.6881` -- and
`Om`'s `+/-0.0150` step moves it **`3.581708`** Mpc against `omega_b`'s `+/-0.0008` at
**`1.353121`**.  ⇒ `Om` leads by a factor `2.6`.
  *The reason is plain once measured: the grid's `H0` and `Om` steps move `omega_m` far more than its
  `omega_b` step moves `omega_b`, and `rdrag` answers to both.*  ⇒ ** So the warning owed to 60
  INVERTS: if their rerun moves the limit, the ruler can account for several Mpc of it rather than a
  fraction of one. **

⌗ `Ⓖ` SPLITS: `rdrag` at the control is `146.8930` Mpc, which misses the registered `147.0`-`147.8`
interval and sits inside the registered refutation window of `146.5`-`148.5`.  Both are reported.
⌗ `Ⓘ` holds on its first limb EXACTLY -- the calibrated arm's `rd_used` equals its own `rd_camb` at
every sum, so "calibrated" means what it says -- and is refuted on its second at one point of eight:
the minimised arm differs by `0.839` Mpc at `Sum = 0` where the band said more than `1`.
⌗ `Ⓙ` holds: the calibrated ruler varies `0.770` Mpc across the sums.
⌗ *And the registration said "nine sums" where this seat's own profile has EIGHT by design.*

-------------------------------------------------------------------------------
COMPUTES: the three blocks' binned ratios against the CAMB reference with `FOURPI` on; TE's
  correlation coefficient with the switch on AND off; the exact factor between the two bank points
  block by block; the ten pairs' closure on each leg; and the drag-epoch ruler at 60's control and
  across their eight grid displacements.  ** IT PINS NO COSMOLOGICAL PARAMETER OF ITS OWN: ** every
  parameter is 60's grid's or `r7853`'s profile's, read from their files.
STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy; under a second -- it reads the banked records
  and the two bank points, and runs no instrument and no `camb`)
"""
import json
import os
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 100
fail = []
RAN = []


def check(label, ok, got=None):
    RAN.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   (got {got})" if got is not None else ""))
    if not ok:
        fail.append(label)


# ⛔ THREE directory steps: `HERE` is `<root>/receipts/P15_CR_cosmology`.  The assertion is what
#   catches a miscount, and this seat miscounted it twice today in other files.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
assert os.path.isdir(os.path.join(ROOT, 'computations')), f'ROOT is wrong: {ROOT}'
CD = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7861_cc66_the_three_block_check_with_fourpi_on_and_the_calibrated_profile')
OFF = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7855_cc66_an_independent_check_of_the_factor_two_in_the_cmb_bank', 'bank',
                   'lcdm_S000.npz')
ON = os.path.join(CD, 'bank_fourpi', 'lcdm_S000.npz')
CMP = json.load(open(os.path.join(CD, 'compare_fourpi_vs_camb.json')))
RDG = json.load(open(os.path.join(CD, 'rdrag_grid.json')))
PRO = json.load(open(os.path.join(CD, 'calibrated_profile.json')))
BLK = {b['block']: b for b in CMP['blocks']}

# =================================================================================================
print(BAR)
print("  Ⓐ -- ** ③ TT AND EE READ ONE, EACH INSIDE ITS OWN SPREAD **")
print(BAR)
for b in ('TT', 'EE', 'TE'):
    print(f"      {b:3s} abs mean {BLK[b]['abs_mean']:10.6f}   spread {BLK[b]['abs_spread']:10.6f}"
          f"   bins {BLK[b]['n_bins']}")
check("Ⓐ① ** TT reads `1.006625`, which is `0.0066` from one against a per-bin spread of `0.113269` "
      "** -- the band registered at r7859+cc66.1 was `|TT-1| < 0.02`, so it HOLDS with a margin of "
      "three",
      abs(BLK['TT']['abs_mean'] - 1.006625) < 5e-6
      and abs(BLK['TT']['abs_spread'] - 0.113269) < 5e-6
      and abs(BLK['TT']['abs_mean'] - 1.0) < 0.02,
      f"{BLK['TT']['abs_mean']:.6f}")
check("Ⓐ② ** and EE reads `0.994360`, `0.0056` from one against a spread of `0.292787` ** -- so the "
      "factor two is gone from the POLARISATION block too, which is what 60's r7860 wiring was for "
      "and what this seat's EE at `0.497180` predicted when the switch reached only TT",
      abs(BLK['EE']['abs_mean'] - 0.994360) < 5e-6
      and abs(BLK['EE']['abs_spread'] - 0.292787) < 5e-6
      and abs(BLK['EE']['abs_mean'] - 1.0) < 0.02,
      f"{BLK['EE']['abs_mean']:.6f}")
check("Ⓐ③ and both are read on the SAME bin count as 60's own report, `185`, so the comparison is "
      "like for like in its binning even where it is not in its object",
      BLK['TT']['n_bins'] == 185 and BLK['EE']['n_bins'] == 185 and BLK['TE']['n_bins'] == 185)

# =================================================================================================
print()
print(BAR)
print("  Ⓑ -- ** ③ TE BY ITS CORRELATION, AND THE SHARP HALF OF THAT BAND IS AN INVARIANCE **")
print(BAR)
TEC = CMP['te_correlation']
print(f"      correlation with CAMB: FOURPI=1 {TEC['fourpi_on']:.12f}   FOURPI=0 "
      f"{TEC['fourpi_off']:.12f}   |difference| {TEC['abs_difference']:.3e}")
print(f"      while TE's own per-bin ratio spreads {BLK['TE']['abs_spread']:.6f}")
check("Ⓑ④ ** TE's correlation coefficient is INVARIANT under the switch to `2.2e-16` **, which is "
      "the band's sharp half: a correlation coefficient is scale-free, so this tests the PIPELINE "
      "rather than the physics -- if it moved, something other than a constant had changed",
      TEC['abs_difference'] < 1e-12 and TEC['n_bins'] == 185,
      f"{TEC['abs_difference']:.3e}")
check("Ⓑ⑤ ** and its VALUE is `0.999959`, against a registered guess of `> 0.9` ** -- so TE's SHAPE "
      "agreement with CAMB is essentially perfect while its per-bin ratio spreads `26.881564` and "
      "is unusable, which is exactly what three sign crossings inside the reach do to a ratio",
      abs(TEC['fourpi_on'] - 0.999959) < 5e-7 and TEC['fourpi_on'] > 0.9
      and abs(BLK['TE']['abs_spread'] - 26.881564) < 5e-6,
      f"r = {TEC['fourpi_on']:.6f}")
check("Ⓑ⑥ ⚠ and it is NOT the statistic 60 report: a MEDIAN per bin or per window is a different "
      "object from the Pearson coefficient of the binned values, so `0.0196` and this number must "
      "not be read against each other -- recorded here so the next reader cannot take them as one.  "
      "The gap is pinned on BOTH sides, so a mis-transcription of either number reddens this arm "
      "rather than leaving a quoted figure beside a receipt that would not notice it being wrong",
      0.98035 < TEC['fourpi_on'] - 0.0196 < 0.98045,
      f"{TEC['fourpi_on'] - 0.0196:.6f}")

# =================================================================================================
print()
print(BAR)
print("  Ⓒ -- ** ③ THE EXACT FACTOR, BLOCK BY BLOCK, AND THE PAIRS' CLOSURE ON BOTH LEGS **")
print(BAR)
_a, _b = np.load(ON, allow_pickle=True), np.load(OFF, allow_pickle=True)
_same = np.array_equal(np.asarray(_a['ls']), np.asarray(_b['ls']))
_w = {}
for k in ('Dl', 'Dl_EE', 'Dl_TE'):
    r = np.asarray(_a[k], float) / np.asarray(_b[k], float)
    _w[k] = float(np.max(np.abs(r - 2.0)))
    print(f"      {k:7s} on/off ratio min {r.min():.12f} max {r.max():.12f}   worst |r-2| "
          f"{_w[k]:.3e}")
check("Ⓒ⑦ ** every block of the regenerated point is EXACTLY twice the switch-off point ** -- worst "
      "departures `1.332e-15`, `1.110e-15` and `7.550e-15` against a registered `1e-12` -- so 60's "
      "bit-for-bit claim is confirmed independently, and for the polarisation blocks their own "
      "claim could not cover before r7860 wired them",
      _same and _w['Dl'] < 1e-12 and _w['Dl_EE'] < 1e-12 and _w['Dl_TE'] < 1e-12
      and abs(_w['Dl'] - 1.332e-15) < 5e-18 and abs(_w['Dl_EE'] - 1.110e-15) < 5e-18
      and abs(_w['Dl_TE'] - 7.550e-15) < 5e-18,
      f"worst {max(_w.values()):.3e}")
_P = os.path.join(CD, 'pairs_fourpi')
_clo = {}
for tag, f in (('off', 'lcdm_S000_fourpi0.npz'), ('on', 'lcdm_S000_fourpi1.npz')):
    z = np.load(os.path.join(_P, f), allow_pickle=True)
    d, p = np.asarray(z['Dl'], float), np.asarray(z['Dl_pairs'], float)
    _clo[tag] = float(np.max(np.abs(p.sum(axis=1) - d) / np.abs(d)))
    print(f"      pairs closure, switch {tag:3s}  {_clo[tag]:.3e}")
check("Ⓒ⑧ ** THE TEN PAIRS CLOSE AGAIN WITH THE SWITCH ON, AT `1.313e-15`, WHERE THEY WOULD HAVE "
      "READ A HALF ** -- against `1.308e-15` with it off, and against the `0.500000` this seat "
      "measured on all four banked `SRCDEC` files before the repair existed",
      _clo['on'] < 1e-12 and _clo['off'] < 1e-12
      and abs(_clo['on'] - 1.313e-15) < 5e-18 and abs(_clo['off'] - 1.308e-15) < 5e-18,
      f"on {_clo['on']:.3e}, off {_clo['off']:.3e}")
_zo, _zn = np.load(os.path.join(_P, 'lcdm_S000_fourpi0.npz')), np.load(os.path.join(_P, 'lcdm_S000_fourpi1.npz'))
_rd = np.asarray(_zn['Dl'], float) / np.asarray(_zo['Dl'], float)
_rp = np.asarray(_zn['Dl_pairs'], float) / np.asarray(_zo['Dl_pairs'], float)
check("Ⓒ⑨ ...and the closure survives because BOTH sides of the identity moved: `Dl` and `Dl_pairs` "
      "each scale by exactly two between the legs, measured off the arrays rather than read off the "
      "instrument's own print",
      abs(float(_rd.min()) - 2.0) < 1e-12 and abs(float(_rd.max()) - 2.0) < 1e-12
      and abs(float(_rp.min()) - 2.0) < 1e-12 and abs(float(_rp.max()) - 2.0) < 1e-12)

# =================================================================================================
print()
print(BAR)
print("  Ⓓ -- ** ⑥ THE DRAG RULER OVER 60's GRID, AND Ⓗ REFUTED ON BOTH LIMBS **")
print(BAR)
_ctl = RDG['rdrag']['lcdm control']['rdrag']
print(f"      rdrag at 60's lcdm control {_ctl:.4f} Mpc")
print(f"      the ends: {RDG['ends']['hi']} {RDG['rdrag'][RDG['ends']['hi']]['rdrag']:.4f} and "
      f"{RDG['ends']['lo']} {RDG['rdrag'][RDG['ends']['lo']]['rdrag']:.4f}   range "
      f"{RDG['ends']['range_mpc']:.6f} Mpc")
print(f"      the levers: Om {RDG['levers']['Om']:.6f} Mpc   omega_b "
      f"{RDG['levers']['omega_b']:.6f} Mpc")
check("Ⓓ⑩ ⛔ ** Ⓗ IS REFUTED ON BOTH LIMBS: the range over 60's eight displaced points is "
      "`4.461444` Mpc where the band said under `1.5`, and `Om`'s step moves the ruler `3.581708` "
      "Mpc against `omega_b`'s `1.353121` ** -- so `Om` leads by a factor `2.6` and this seat had "
      "the lever backwards",
      abs(RDG['ends']['range_mpc'] - 4.461444) < 5e-6
      and abs(RDG['levers']['Om'] - 3.581708) < 5e-6
      and abs(RDG['levers']['omega_b'] - 1.353121) < 5e-6
      and RDG['ends']['range_mpc'] > 1.5 and RDG['levers']['Om'] > RDG['levers']['omega_b'],
      f"range {RDG['ends']['range_mpc']:.6f}, Om {RDG['levers']['Om']:.6f} vs omega_b "
      f"{RDG['levers']['omega_b']:.6f}")
check("Ⓓ⑪ ⌗ and Ⓖ SPLITS, reported as both: `rdrag` at the control is `146.8930` Mpc, which misses "
      "the registered `147.0`-`147.8` interval and sits inside the registered refutation window of "
      "`146.5`-`148.5`",
      abs(_ctl - 146.8930) < 5e-5 and not (147.0 <= _ctl <= 147.8) and 146.5 <= _ctl <= 148.5,
      f"{_ctl:.4f}")
check("Ⓓ⑫ and the ends are the two `H0` displacements rather than the `omega_b` ones, which is the "
      "same finding read off the names instead of the sizes",
      RDG['ends']['hi'] == 'H0m' and RDG['ends']['lo'] == 'H0p')

# =================================================================================================
print()
print(BAR)
print("  Ⓔ -- ** ⑥ THE PROFILE IS CALIBRATED WHERE IT SAYS IT IS, AND FREE WHERE IT SAYS IT IS **")
print(BAR)
CAL, MIN = PRO['profile']['rd_camb'], PRO['profile']['rd_min']
_exact = all(r['rd_used'] == r['rd_camb'] for r in CAL)
_gaps = sorted(abs(r['rd_used'] - r['rd_camb']) for r in MIN)
print(f"      calibrated arm: {len(CAL)} sums, rd_used == rd_camb on all of them = {_exact}")
print(f"      minimised arm:  gaps from that point's own rd_camb, {_gaps[0]:.4f} to {_gaps[-1]:.4f} Mpc")
_span = max(r['rd_camb'] for r in CAL) - min(r['rd_camb'] for r in CAL)
print(f"      the calibrated ruler's own span across the sums: {_span:.4f} Mpc")
check("Ⓔ⑬ ** Ⓘ's first limb holds EXACTLY: the calibrated arm's `rd_used` equals its own `rd_camb` "
      "at every sum, to the digit ** -- so `r7853`'s \"calibrated\" means what it says, and its "
      "`30.56` meV stands on a ruler recomputed at each point",
      _exact and len(CAL) == 8)
check("Ⓔ⑭ ⌗ and Ⓘ's SECOND limb is refuted at one point of eight: the minimised arm differs from "
      "that point's own `rdrag` by `0.839` Mpc at `Sum = 0` where the band said more than `1`, and "
      "by more than `1` at the other seven",
      abs(_gaps[0] - 0.839) < 0.001 and len(MIN) == 8
      and sum(1 for g in _gaps if g > 1.0) == 7,
      f"smallest gap {_gaps[0]:.4f} Mpc")
check("Ⓔ⑮ Ⓙ holds: the calibrated ruler varies `0.770` Mpc across the eight sums, so the ruler and "
      "the mass are not strongly entangled on this reference.  ⌗ *And the registration said NINE "
      "sums where this seat's own profile has eight by design, which is recorded rather than "
      "quietly corrected*",
      abs(_span - 0.770) < 0.001 and len(CAL) == 8,
      f"{_span:.4f} Mpc over {len(CAL)} sums")
check("Ⓔ⑯ and the profile is READ rather than re-fitted, which its own record states, so the "
      "numbers banked for 60 are the ones the landed limits came from",
      'NOT re-fitted' in PRO['source'] and PRO['n_live'] == 16 and PRO['n_cold'] == 2)

# =================================================================================================
print()
print(BAR)
print("  Ⓕ -- ** THE COUNT, COUNTED **")
print(BAR)
_before = len(RAN)
print(f"      {_before} arms ran before this one, {len(set(RAN))} of them distinct")
check(f"Ⓕ⑰ ** sixteen arms ran before this one and every one was adjudicated **, the count read off "
      f"the list `check` itself appends rather than typed beside them",
      _before == 16 and len(set(RAN)) == _before,
      f"{_before} arms")

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** ③ ALL SIX REGISTERED BANDS HOLD: TT 1.006625, EE 0.994360, TE's correlation 0.999959")
print("    and invariant to 2.2e-16, every block exactly twice to 1e-15, and the pairs closing again")
print("    at 1.313e-15 where they would have read a half. **")
print("  ⛔ ** ⑥ AND THE BAND THAT MATTERED IS REFUTED BOTH WAYS: the drag ruler's lever over 60's")
print("    grid is Om and not omega_b, by a factor 2.6, and its range is 4.46 Mpc and not under")
print("    1.5 -- so the ruler can account for several Mpc of a limit shift, not a fraction of one. **")
print(BAR)
print("  ALL CHECKS PASS")
