#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE CONTROL'S BASE LOG IS NOW BANKED BESIDE THE GRIDS, AND WITH IT THE PEAK-HEIGHT
CELL IS A SIGN RATHER THAN AN EMPTY ONE -- A CONCORDANT SIGN.  THE FORBIDDEN CONFIGURATION'S HEIGHTS
ARE THE CONTROL'S OWN, AT 0.18 ON TWO DEGREES OF FREEDOM IN THE DATA'S OWN UNITS, WHICH IS A FOURTH
STATISTIC SAYING WHAT chi^2, THE CROSSINGS AND THE LONGEST RUN ALREADY SAID. **

*** AND THE STATISTIC THAT FILLS THE CELL ALSO SAYS IT COULD NEVER HAVE BEEN A CONTRARY SIGN: ALL
FOUR ARMS SIT INSIDE 1.1 ON TWO DEGREES OF FREEDOM AGAINST THE SKY'S OWN PEAK-HEIGHT RATIOS, SO THE
HEIGHTS CANNOT SEPARATE ANY CANDIDATE FROM THE DATA OR FROM EACH OTHER. ***

Built r7109+cc66.84 (node 66, code seat), answering `r7109` ⓶.

===================================================================================================
** WHAT WAS MISSING, AND IT WAS NOT AN OVERSIGHT **
===================================================================================================

`70`'s three-grid audit (`r7101_70_three_grid_audit/audit_log.txt`) closes on exactly this blank:

    peak structure printed by the instrument at each arm's base (line-of-sight, hierarchy):
      licensed  peaks at l = [220, 532, 812, 1132]   l_1/l_A = 0.7263   P1/P2 = 2.283 ...
      forbidden peaks at l = [220, 540, 812, 1132]   l_1/l_A = 0.7300   P1/P2 = 2.199 ...
    (the control's base has no log banked beside the grids; its peak ratios are not compared here)

** The control had no log because both grid launchers COPY the control's nine spectra from
`refit_grid185/` instead of re-running them. **  `LEAFGEOM` and `LEAFREC` are provable no-ops on the
control -- `Hleaf` and `Hphys` are character-identical when radiation is in the rate -- and the copy
was verified bit-identical.  *A copy carries the `.npz` and not the stdout, and the peak table is
printed to stdout.*  So the blank was a property of the copy, not of the measurement.

===================================================================================================
** AND WITHOUT THAT ROW, ONE READING OF THE HEIGHTS COULD NOT BE TOLD FROM ITS OPPOSITE **
===================================================================================================

With the arm's two logs alone, `P1/P2 = 2.199` forbidden against `2.283` licensed reads as the
forbidden configuration's heights being *better* -- nearer the `2.217` the instrument prints on the
line beneath.  ** But the three rigidity statistics say the forbidden configuration IS the control:
chi^2 184.989 against the control's 186.007, crossings 91 against 87, longest run 8 against 8. **  So
`2.199` has two possible meanings and the banked set could not choose between them:

    (a)  the forbidden configuration's heights are BETTER than the licensed one's -- a contrary sign,
         the heights dissenting from the other three statistics; or
    (b)  the forbidden configuration's heights are THE CONTROL'S -- a concordant sign, the collapse
         showing up in a fourth statistic.

** IT IS (b), AND IT IS NOT CLOSE. **  The control's own base reads `P1/P2 = 2.196`, `P1/P3 = 2.190`.

  PART 1  ** THE LOG IS BANKED, AND IT IS THE LOG OF THE BANKED ARTEFACT RATHER THAN OF A RE-RUN. **
          `refit185/lcdm_base.log` is the original stdout of the run whose `.npz` IS the banked
          `lcdm_base.npz`, md5 `5df16bcd401dcd2a624fb230313c97f7` on `refit_grid185/` and on both
          grids.  *A re-run's log would describe a re-run; this one describes the artefact.*  Both
          banked copies are asserted identical, and tracked -- `*.log` is ignored by default and the
          exception is declared in `.gitignore`, which is the defect `r7099` Q1 caught last round.
  PART 2  ** THE FOUR READINGS, RECOMPUTED AT FULL PRECISION THROUGH THE INSTRUMENT'S OWN PEAK
          DEFINITION rather than read off three printed decimals. **  `argrelextrema(Dl, greater,
          order=3)` on the banked `Dl`, which is the instrument's own line.
  PART 3  ** THE DATA'S OWN PEAK-HEIGHT RATIOS, WITH THE ERROR BAR, so the cell has units. **
          `2.2564 +- 0.0772` and `2.2800 +- 0.0737` from the published covariance's 2x2 block --
          reproducing `P15_the_height_target_was_below_the_resolution_of_its_own_statistic` (c54.176)
          through the same route.  ⌗ ** AND THE LINE THE AUDIT READ IS THE BARE ONE. **  The
          instrument's non-`DSCAN` print still quotes `P1/P2 = 2.217, P1/P3 = 2.277` with no bar,
          while its `DSCAN` print carries `2.256 +-3.4%` and `2.280 +-3.2%` -- two sky references in
          one file.  *The bare pair is not WRONG: it is inside 1 sigma of the propagated pair, which
          c54.176 asserts.  It is BARE, and a 0.084 difference quoted against it is a fifth of the
          bar nobody was carrying.*
  PART 4  ** THE CELL, IN THE DATA'S OWN UNITS: lensed, binned by the likelihood's own binning, the
          same peak finder, the same 185-bin window, and ONE number per arm from the joint
          covariance of the two ratios. **  A model read on its own 2-multipole grid against a sky
          read on 185 coarse bins is not "the same units", and reading it that way is the mistake
          this sector has now named four times.
  PART 5  ** AND ONE RUN, which is what `r7109` ⓶ budgeted: the instrument AS IT IS NOW, at the
          control's own settings, returns the banked control's arrays -- `ls`, `l_A`, `D_M` and `r_s`
          BIT-IDENTICAL and `Dl` to 6.8e-15, which is the same cross-machine reduction order the
          `DAMPX` pair showed against `r4494` (6.4e-15) and is reported as relaxed rather than
          asserted as bit-identical. **  *The bank was built at r6801 on another machine.*  That also measures the
          `LEAFREC` no-op live rather than inheriting it, because `LEAFREC` defaults to 1 since
          r7095+cc66.75 and the banked control predates the flip.  *Skipped with a named reason, not
          silently, when the run is not present -- PARTS 1-4 do not depend on it.*

===================================================================================================
** THE ANSWER TO `r7109` ⓶, IN ONE LINE EACH **
===================================================================================================

  ⓐ ** THE CELL IS A CONCORDANT SIGN. **  forbidden against the control, as a 2-dof distance in the
     data's own units: ** 0.18 **.  licensed against the control: ** 2.83 **.  *The configuration the
     rule licenses moves the heights; the one it forbids does not move them off the control.*
  ⓑ ** AND THE HEIGHTS CANNOT VOTE. **  Against the sky, on two degrees of freedom: banked 0.85,
     licensed 1.05, forbidden 0.44, control 0.59.  ** Every one of them is inside 1.1, and the two
     ratios do not even agree on an ordering. **  ⇒ *So there was never a contrary sign available
     here, and the apparent one came from quoting a difference a fifth of the statistic's resolution
     against a sky number carrying no bar.*
  ⓒ ** THE THREE RIGIDITY STATISTICS KEEP THEIR STANDING AS THE ONES WITH THE INFORMATION **, which
     is c54.176's conclusion arriving a second time by a second route: chi^2 separates 278.79 from
     184.99 where the heights separate 1.05 from 0.44.

** COMPUTES: nothing on the instrument. ***  Every spectrum is read from a banked `.npz` and
   scored; the parameters are the ones baked into those files -- the three grids at
   (H0, Om) = (68.60, 0.2973) on the arm and the instrument's own (67.40, 0.3150) on the control,
   `ZSTART=3e7`, `LEAFSCALES=1`, `KFAC=2.0`, `HIER=1 LSTEP=8 LMAXL=2000`.  *What is computed here is
   the peak finder, the likelihood's binning and CAMB's lensing operator at the fiducial LambdaCDM
   that operator is defined on -- none of which sets a CR parameter.*  PART 5's one run is at the
   control's own settings, `ARM=lcdm` and nothing else, and is an independent check rather than an
   input.

SETTINGS: the banked grids as committed -- `HIER=1 LSTEP=8 LMAXL=2000`, `KFAC=2.0`, the reporting
path.  ** The sky's error bars are a property of plik_lite and do not move with the transfer's
depth **, which is why c54.176 could establish them at reduced settings and this file can read them
at production.  PART 5's run is `r7109_directions/launch_control_base.sh`.

rc=0 on success.  Run: python3 P15_the_controls_base_log_is_banked_beside_the_grids_and_the_peak_heights_concur_with_the_three_rigidity_statistics.py
                       (numpy scipy camb, ~40 s)
"""
import os
import subprocess
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

# the instrument's own peak line, quoted rather than reimplemented
ORDER = 3

GRIDS = [
    ('banked', os.path.join(BW, 'refit_grid185', 'cr_base.npz')),
    ('licensed', os.path.join(BW, 'r7095_directions', 'grid_licensed', 'cr_base.npz')),
    ('forbidden', os.path.join(BW, 'r7093_directions', 'grid_oneclock', 'cr_base.npz')),
    ('control', os.path.join(BW, 'refit_grid185', 'lcdm_base.npz')),
]
CTRL_NPZ = [
    os.path.join(BW, 'refit_grid185', 'lcdm_base.npz'),
    os.path.join(BW, 'r7093_directions', 'grid_oneclock', 'lcdm_base.npz'),
    os.path.join(BW, 'r7095_directions', 'grid_licensed', 'lcdm_base.npz'),
]
CTRL_LOG = [
    os.path.join(BW, 'r7093_directions', 'grid_oneclock', 'lcdm_base.log'),
    os.path.join(BW, 'r7095_directions', 'grid_licensed', 'lcdm_base.log'),
]
AUDIT = os.path.join(BW, 'r7101_70_three_grid_audit', 'audit_log.txt')
LAUNCH = os.path.join(BW, 'r7109_directions', 'launch_control_base.sh')
INSTR = os.path.join(BW, 'ACOUSTIC_two_arm.py')

# =====================================================================
print("=" * 100)
print("  PART 1 -- ** THE LOG IS BANKED, AND IT IS THE LOG OF THE BANKED ARTEFACT **")
print("=" * 100)

# ⚠ the scope gate asks git, rather than asserting "tracked in this repository" off os.path.exists --
#    which is the defect r7101 caught in this seat's own work.
INPUTS = [p for _, p in GRIDS] + CTRL_NPZ + CTRL_LOG + [AUDIT, LAUNCH, INSTR]
try:
    subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch'] + INPUTS,
                   check=True, capture_output=True)
    print(f"  all {len(INPUTS)} inputs are tracked by git in this checkout")
except subprocess.CalledProcessError as exc:
    missing = exc.stderr.decode('utf-8', 'replace').strip().split('\n')
    fail.append(f"an input is not tracked by git: {missing[0][:120]}")
except (OSError, FileNotFoundError):
    absent = [p for p in INPUTS if not os.path.exists(p)]
    if absent:
        fail.append(f"{len(absent)} input(s) absent and git unavailable to check tracking")
    else:
        print(f"  git unavailable here; all {len(INPUTS)} inputs exist on disk (tracking unchecked)")

import hashlib                                                            # noqa: E402


def md5(p):
    with open(p, 'rb') as fh:
        return hashlib.md5(fh.read()).hexdigest()


BANKED_MD5 = '5df16bcd401dcd2a624fb230313c97f7'
got = {p: md5(p) for p in CTRL_NPZ}
for p, h in got.items():
    print(f"  {os.path.relpath(p, BW):>52}  md5 {h}")
if len(set(got.values())) != 1:
    fail.append("the control's base .npz is NOT the same file across the three directories")
elif next(iter(got.values())) != BANKED_MD5:
    fail.append(f"the control's base .npz is {next(iter(got.values()))}, not the quoted {BANKED_MD5}")
else:
    print(f"  ** one file in three places, md5 {BANKED_MD5} -- so ONE log describes all three **")

lh = {p: md5(p) for p in CTRL_LOG}
if len(set(lh.values())) != 1:
    fail.append("the two banked copies of the control's base log differ")
else:
    print(f"  the two banked log copies are identical (md5 {next(iter(lh.values()))})")

LOG = open(CTRL_LOG[0], encoding='utf-8', errors='replace').read()
if 'ARM=lcdm' not in LOG:
    fail.append("the banked control log does not say ARM=lcdm")
if 'refit185/lcdm_base.npz' not in LOG:
    fail.append("the banked control log does not name the .npz it saved -- it may not be that run's")
else:
    print("  the log names its own output: '" +
          next(l.strip() for l in LOG.split('\n') if 'saved' in l) + "'")

# the audit's own sentence, so this receipt's premise is quoted and not remembered
AUD = open(AUDIT, encoding='utf-8', errors='replace').read()
PREMISE = "the control's base has no log banked beside the grids"
if PREMISE not in AUD:
    fail.append("the audit does not carry the blank this receipt fills -- the premise has moved")
else:
    print(f"  the audit's own words, quoted: \"{PREMISE}; its peak ratios are not compared here\"")

# =====================================================================
print()
print("=" * 100)
print("  PART 2 -- ** THE FOUR READINGS, AT FULL PRECISION, THROUGH THE INSTRUMENT'S OWN DEFINITION **")
print("=" * 100)


def read(path):
    z = np.load(path)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    pk = [q for q in argrelextrema(Dl, np.greater, order=ORDER)[0]]
    return ls, Dl, float(z['l_A']), pk


FINE = {}
print(f"  {'arm':>10} {'peaks at ell':>26} {'l_A':>9} {'l_1/l_A':>9} {'P1/P2':>10} {'P1/P3':>10}")
for nm, p in GRIDS:
    ls, Dl, lA, pk = read(p)
    r12, r13 = Dl[pk[0]] / Dl[pk[1]], Dl[pk[0]] / Dl[pk[2]]
    FINE[nm] = (float(ls[pk[0]]), lA, float(r12), float(r13))
    print(f"  {nm:>10} {str([int(ls[q]) for q in pk[:4]]):>26} {lA:9.3f} "
          f"{ls[pk[0]] / lA:9.6f} {r12:10.6f} {r13:10.6f}")

# ** the printed log is the check on this route, not the other way round: three decimals, so the
#    agreement is asserted at three decimals and not finer. **
for nm, want in (('control', (2.196, 2.190)),):
    if abs(FINE[nm][2] - want[0]) > 5e-4 or abs(FINE[nm][3] - want[1]) > 5e-4:
        fail.append(f"the {nm}'s recomputed ratios disagree with its own banked log's printed pair")
if 'P1/P2 = 2.196' not in LOG or 'P1/P3 = 2.190' not in LOG:
    fail.append("the banked control log does not print the pair this receipt reads off it")
else:
    print("  ** the banked log's own printed pair, 2.196 / 2.190, is reproduced from the .npz "
          "to its three decimals **")
# and the two arm logs the audit read, likewise
for nm, rel, want in (('licensed', os.path.join('r7095_directions', 'grid_licensed', 'cr_base.log'),
                       (2.283, 2.311)),
                      ('forbidden', os.path.join('r7093_directions', 'grid_oneclock', 'cr_base.log'),
                       (2.199, 2.213))):
    t = open(os.path.join(BW, rel), encoding='utf-8', errors='replace').read()
    if f'P1/P2 = {want[0]:.3f}' not in t:
        fail.append(f"the {nm} arm's banked log does not print P1/P2 = {want[0]:.3f}")
    if abs(FINE[nm][2] - want[0]) > 5e-4 or abs(FINE[nm][3] - want[1]) > 5e-4:
        fail.append(f"the {nm}'s recomputed ratios disagree with its own banked log")

# ⛭ the structural claim: the forbidden arm's l_A and comb ARE the control's, the licensed one's are not
dlA_f = abs(FINE['forbidden'][1] - FINE['control'][1])
dlA_l = abs(FINE['licensed'][1] - FINE['control'][1])
print(f"\n  l_A: forbidden is {dlA_f:.4f} from the control in {FINE['control'][1]:.3f} "
      f"({dlA_f / FINE['control'][1]:.2e} relative); licensed is {dlA_l:.4f} ({dlA_l / FINE['control'][1]:.2e})")
if not dlA_f < 0.05:
    fail.append("the forbidden arm's l_A is not the control's -- the collapse claim's premise")
if not dlA_l > 1.0:
    fail.append("the licensed arm's l_A is indistinguishable from the control's")
print("  ** so the forbidden configuration's acoustic angle is the control's and the licensed one's "
      "is 1.5 away: **")
print("     the heights are being read on an arm that has ALREADY collapsed in its geometry.")

# =====================================================================
print()
print("=" * 100)
print("  PART 3 -- ** THE DATA'S OWN PEAK-HEIGHT RATIOS, WITH THE BAR, SO THE CELL HAS UNITS **")
print("=" * 100)

lc, fac = CS.bin_center_and_fac()
# ** X_data is binned C_l, not D_l ** -- CS's own docstring, and the reason the first peak is lost
DSKY = CS.X_DATA * fac
CDSKY = CS.COV_TT * np.outer(fac, fac)


def interior_peaks(arr, lo, hi):
    """local maxima of arr[lo:hi] that are ORDER away from BOTH ends of the window

    The window's own edges are not peaks: the model spectra start at ell = 100, so the first covered
    bin beats its padding on the left and comes out as a spurious maximum at ell = 104 if the edges
    are left in.  *That is the same failure CS.bin_center_and_fac's docstring records for X_data.*
    """
    sub = arr[lo:hi]
    q = argrelextrema(sub, np.greater, order=ORDER)[0]
    return [int(x) + lo for x in q if ORDER <= x < len(sub) - ORDER]


_ok = np.isfinite(CS.bin_spectrum(*read(GRIDS[3][1])[:2]))
LO, HI = int(np.argmax(_ok)), int(len(_ok) - np.argmax(_ok[::-1]))
NB = int(_ok.sum())
print(f"  the window the models cover: {NB} bins, ell {lc[LO]:.1f} to {lc[HI - 1]:.1f}")
if NB != 185:
    fail.append(f"the models cover {NB} bins, not the 185 the grids are named for")

sp = interior_peaks(DSKY, LO, HI)[:3]
print(f"  the sky's own peaks in the binned D_l: ell = {[round(float(lc[i]), 1) for i in sp]}")
a, b, c = sp
R12, R13 = DSKY[a] / DSKY[b], DSKY[a] / DSKY[c]
J = np.array([[1 / DSKY[b], -DSKY[a] / DSKY[b] ** 2, 0.0],
              [1 / DSKY[c], 0.0, -DSKY[a] / DSKY[c] ** 2]])
C2 = J @ CDSKY[np.ix_(sp, sp)] @ J.T
E12, E13 = float(np.sqrt(C2[0, 0])), float(np.sqrt(C2[1, 1]))
RHO = float(C2[0, 1] / np.sqrt(C2[0, 0] * C2[1, 1]))
print(f"  ** P1/P2 = {R12:.4f} +- {E12:.4f} ({100 * E12 / R12:.2f}%)   "
      f"P1/P3 = {R13:.4f} +- {E13:.4f} ({100 * E13 / R13:.2f}%) **   correlation {RHO:+.4f}")
print("  *The full 3x3 block of the published covariance, propagated to both ratios at once -- so the")
print("   two are not treated as independent, which they are not: they share P1.*")
# c54.176's own pair, reproduced
for nm, got_, want in (('P1/P2', R12, 2.256), ('P1/P3', R13, 2.280)):
    if abs(got_ - want) > 5e-4:
        fail.append(f"the sky's {nm} came out {got_:.4f}, not c54.176's {want:.3f}")
for nm, e, r in (('P1/P2', E12, R12), ('P1/P3', E13, R13)):
    if not 0.02 < e / r < 0.06:
        fail.append(f"the sky's {nm} bar came out {e / r:.1%} -- c54.176's 3.2-3.4% has moved")
print(f"  c54.176's pair, 2.256 +- 0.077 and 2.280 +- 0.074, reproduced through the same route")

# ⌗ THE TWO SKY REFERENCES IN ONE FILE, which is the line the audit read
SRC = open(INSTR, encoding='utf-8', errors='replace').read()
BARE = ('P1/P2 = 2.217' in SRC, 'P1/P3 = 2.277' in SRC)
WITHBAR = ('2.256' in SRC and '+-3.4%' in SRC)
print(f"\n  the instrument's non-DSCAN print carries the BARE pair: {BARE[0] and BARE[1]}")
print(f"  its DSCAN print carries the pair WITH the bar (2.256, +-3.4%): {WITHBAR}")
if not (BARE[0] and BARE[1]):
    print("  ⌗ the bare pair is no longer in the instrument -- this note is spent and can be dropped")
elif not WITHBAR:
    fail.append("the instrument carries the bare sky pair and not the one with the bar")
else:
    print("  ⚠ ** TWO SKY REFERENCES IN ONE FILE, and the audit read the bare one. **")
    for nm, bare, r, e in (('P1/P2', 2.217, R12, E12), ('P1/P3', 2.277, R13, E13)):
        print(f"     {nm}: bare {bare:.3f} against {r:.4f} +- {e:.4f}  -> {abs(r - bare) / e:.2f} sigma")
        if abs(r - bare) > e:
            fail.append(f"the bare {nm} is more than 1 sigma from the propagated one -- "
                        f"c54.176 asserts it is inside")
    print("     *So the bare pair is not WRONG -- it is inside 1 sigma, which c54.176 asserts and this")
    print("      re-asserts.  It is BARE, and that is enough to make a 0.084 difference look like a")
    print("      sign.*  ⇒ ** Routed to the gate rather than swept: a dozen registered receipts carry")
    print("      2.217 as SKY and the protocol is the paper's, not this seat's. **")

# =====================================================================
print()
print("=" * 100)
print("  PART 4 -- ** THE CELL, IN THE DATA'S OWN UNITS, ONE NUMBER PER ARM **")
print("=" * 100)
import camb                                                               # noqa: E402

_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * (0.674 ** 2) - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
_lg = np.arange(len(_le))
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]
r1900 = float(np.interp(1900, _lg, RATIO))
print(f"  the lensing operator (CAMB's lensed/unlensed, the non-perturbative one) at ell 1900: "
      f"{r1900:.4f}")
if not 1.05 <= r1900 <= 1.08:
    fail.append(f"the lensing operator gives {r1900:.4f} at ell 1900, not the full operator's ~1.065")
print("  *The same operator `P15_the_full_range_lensed_comparison...` uses, and the same check on it:")
print("   the first-order kernel's spurious +13% there against the full operator's +6.5%.*")

CI2 = np.linalg.inv(C2)
print(f"\n  {'arm':>10} {'peaks (binned)':>26} {'P1/P2':>9} {'P1/P3':>9} "
      f"{'chi2 vs sky':>12} {'(2 dof)':>9}")
MATCH = {}
for nm, p in GRIDS:
    ls, Dl, _, _ = read(p)
    mb = CS.bin_spectrum(ls, Dl * np.interp(ls, _lg, RATIO)) * fac
    pm = interior_peaks(np.where(np.isfinite(mb), mb, -1e300), LO, HI)[:3]
    r12, r13 = mb[pm[0]] / mb[pm[1]], mb[pm[0]] / mb[pm[2]]
    d = np.array([r12 - R12, r13 - R13])
    x2 = float(d @ CI2 @ d)
    MATCH[nm] = (float(r12), float(r13), x2)
    print(f"  {nm:>10} {str([round(float(lc[i]), 1) for i in pm]):>26} {r12:9.4f} {r13:9.4f} "
          f"{x2:12.4f} {np.sqrt(x2):9.3f}")

# ⓐ the cell: forbidden against the CONTROL, in the data's units
ctrl = MATCH['control']
DIST = {}
for nm in ('banked', 'licensed', 'forbidden'):
    d = np.array([MATCH[nm][0] - ctrl[0], MATCH[nm][1] - ctrl[1]])
    DIST[nm] = float(d @ CI2 @ d)
print(f"\n  ** against the CONTROL, as a 2-dof distance in the data's own units: **")
for nm in ('banked', 'licensed', 'forbidden'):
    print(f"     {nm:>10}  chi2 = {DIST[nm]:7.4f}")
print(f"\n  ⓐ ** THE CELL IS A CONCORDANT SIGN: the forbidden configuration's heights are the")
print(f"     control's own at {DIST['forbidden']:.2f} on two degrees of freedom, where the licensed")
print(f"     one's are {DIST['licensed']:.2f} away. **  The heights say what chi^2, the crossings and")
print("     the longest run say: the forbidden configuration lands on the control.")
if not DIST['forbidden'] < 0.5:
    fail.append(f"the forbidden arm's heights are {DIST['forbidden']:.3f} from the control's, not on "
                f"them -- the concordance claim fails")
if not DIST['licensed'] > 1.0:
    fail.append(f"the licensed arm's heights are {DIST['licensed']:.3f} from the control's -- it does "
                f"not move them, and ⓐ's contrast fails")
if not DIST['forbidden'] < DIST['licensed'] / 4:
    fail.append("the forbidden arm is not decisively nearer the control than the licensed arm is")

# ⓑ and the heights cannot vote
print(f"\n  ⓑ ** AND THE HEIGHTS CANNOT VOTE: every arm is inside 1.1 against the SKY on two degrees")
print("     of freedom, and the two ratios do not agree on an ordering. **")
worst = max(MATCH[nm][2] for nm, _ in GRIDS)
if not worst < 1.2:
    fail.append(f"an arm sits at chi2 {worst:.2f} against the sky's heights -- ⓑ's claim that none "
                f"is separable fails")
o12 = sorted(((abs(MATCH[nm][0] - R12) / E12, nm) for nm, _ in GRIDS))
o13 = sorted(((abs(MATCH[nm][1] - R13) / E13, nm) for nm, _ in GRIDS))
print(f"     nearest on P1/P2: {[n for _, n in o12]}")
print(f"     nearest on P1/P3: {[n for _, n in o13]}")
if [n for _, n in o12] == [n for _, n in o13]:
    print("     ⌗ the two orderings agree here -- weaker than claimed above, and said so")
else:
    print("     ** the two orderings disagree, at separations all under 1.3 sigma -- so 'which arm")
    print("        fits the heights better' is not a question this statistic answers. **")

# ⓒ against the statistic that does have the information
print(f"\n  ⓒ ** WHAT THE STATISTIC WITH THE INFORMATION SAYS, for contrast: ** chi^2 over the 185")
print("     bins separates 278.79 (licensed) from 184.99 (forbidden) against the control's 186.01 --")
print(f"     a gap of 93.8 -- where the heights separate {MATCH['licensed'][2]:.2f} from "
      f"{MATCH['forbidden'][2]:.2f}.")
print("     *c54.176's conclusion arriving a second time by a second route.*")

# the fine-grid route must give the same sign, or the result is an artefact of the binning
fd_f = abs(FINE['forbidden'][2] - FINE['control'][2]) / E12
fd_l = abs(FINE['licensed'][2] - FINE['control'][2]) / E12
print(f"\n  ** AND THE SIGN IS NOT THE BINNING'S: on the instrument's own fine grid, unlensed, the")
print(f"     same contrast is {fd_f:.3f} sigma (forbidden) against {fd_l:.3f} sigma (licensed) on")
print("     P1/P2 -- the same sign and the same order of magnitude as the matched route. **")
if not fd_f < 0.2 < fd_l:
    fail.append("the fine-grid route does not reproduce the matched route's sign -- the result may "
                "be an artefact of the binning or the lensing operator")

# =====================================================================
print()
print("=" * 100)
print("  PART 5 -- ** THE ONE RUN: THE INSTRUMENT AS IT IS NOW RETURNS THE BANKED CONTROL **")
print("=" * 100)
RERUN = os.path.join('/tmp', 'n66', 'r7109_control', 'lcdm_base.npz')
if not os.path.exists(RERUN):
    print(f"  SKIPPED with a reason: {RERUN} is not present in this tree.")
    print("  *This is the one run `r7109` ⓶ budgeted, and it is an INDEPENDENT CHECK on PARTS 1-4")
    print("   rather than an input to them: the banked log already describes the banked artefact,")
    print("   proven by md5 in PART 1.  Re-make it with `r7109_directions/launch_control_base.sh`.*")
else:
    zb = np.load(CTRL_NPZ[0])
    zr = np.load(RERUN)
    print(f"  the re-run's keys: {sorted(zr.files)}")
    print(f"  the banked file's: {sorted(zb.files)}")
    extra = set(zr.files) - set(zb.files)
    print(f"  ⌗ the re-run carries {sorted(extra) if extra else 'no'} key(s) the bank does not -- "
          f"expected: the r7109 ⓵ config writer")
    worstrel = 0.0
    for k in ('ls', 'Dl', 'l_A', 'D_M', 'r_s'):
        x, y = np.atleast_1d(np.asarray(zb[k], float)), np.atleast_1d(np.asarray(zr[k], float))
        if x.shape != y.shape:
            fail.append(f"the re-run's {k} has shape {y.shape} against the bank's {x.shape}")
            continue
        bits = int(np.sum(x != y))
        rel = float(np.max(np.abs(y - x) / np.maximum(np.abs(x), 1e-300)))
        worstrel = max(worstrel, rel)
        print(f"    {k:>4}: {bits} of {x.size} elements differ; largest relative difference {rel:.3e}")
    if worstrel == 0.0:
        print("  ** BIT-IDENTICAL on all five arrays. **  So the instrument at this revision returns")
        print("     the banked control exactly, and the `LEAFREC` no-op on the control is MEASURED")
        print("     here rather than inherited: `LEAFREC` defaults to 1 and the bank predates the flip.")
    elif worstrel < 1e-12:
        print(f"  ** reproduced to {worstrel:.1e}, which is reduction order and not a configuration")
        print("     difference. **  Reported as relaxed rather than asserted as bit-identical.")
    else:
        fail.append(f"the re-run differs from the banked control by {worstrel:.3e} -- the banked log "
                    f"may not describe what the instrument now does")
    rl = open(os.path.join('/tmp', 'n66', 'r7109_control', 'lcdm_base.log'),
              encoding='utf-8', errors='replace').read()
    if 'P1/P2 = 2.196' in rl and 'P1/P3 = 2.190' in rl:
        print("  and the re-run prints the same peak pair, 2.196 / 2.190")
    else:
        fail.append("the re-run's log does not print the banked log's peak pair")

# =====================================================================
print()
print("=" * 100
      )
if fail:
    print(f"  FAIL -- {len(fail)} check(s) did not hold")
    for f in fail:
        print(f"    - {f}")
    print("=" * 100)
    sys.exit(1)
print("  ** ALL CHECKS HOLD. **  `r7109` ⓶ is answered: the control's base log is banked beside both")
print("  grids and is the log of the banked artefact; the peak-height cell is filled in the data's own")
print(f"  units; and it is a CONCORDANT sign -- the forbidden configuration's heights are the")
print(f"  control's at {DIST['forbidden']:.2f} on two degrees of freedom, a fourth statistic agreeing")
print("  with chi^2, the crossings and the longest run.  ** And the same statistic shows the cell")
print("  could never have held a contrary sign: no arm is separable from the sky by the heights. **")
print("=" * 100)
sys.exit(0)
