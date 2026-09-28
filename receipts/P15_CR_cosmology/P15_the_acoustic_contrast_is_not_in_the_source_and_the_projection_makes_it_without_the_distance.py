"""
P15_the_acoustic_contrast_is_not_in_the_source_and_the_projection_makes_it_without_the_distance
==============================================================================================

LEVEL: `r6911`'s order -- ** the SAME contrast statistic applied at two points in the chain **, in
k-space on the source at last scattering and in ell-space on the reported spectrum, both arms at
their own verified 185-bin refit minima.  No knob is added and no mechanism is asked for or offered.

** WHAT THE ORDER ASKED, AND WHAT COMES BACK. **

 ⚑ (1) THE ANSWER IS THE ORDER'S SECOND BRANCH, AND IT IS CLEAN.  ** The source ratio is 1.00 and
     the ell-space ratio is 1.045. **  On the source at last scattering the arm's relative acoustic
     oscillation is 0.996 of the control's; eta-integrated, 0.992; and on the reported spectrum,
     1.045.  ⇒ ** The excess is not in the dynamics.  It is manufactured between k and ell. **
     Across four envelope windows and both envelope definitions the source rungs never leave
     0.971-1.005 and the ell rung never leaves 1.042-1.052, so the gap is not a definition.

 ⚑ (2) AND THAT IS WHY FOUR-FOR-FOUR NEEDED NO EXPLANATION.  The order's puzzle was that four
     channels which each SHALLOW the troughs are all larger on this arm, so something upstream had
     to be big enough to overcome all four.  ** Nothing upstream overcomes them, because upstream
     the arm's oscillation IS very slightly shallower -- 0.996 -- which is the direction all four
     channels point. **  ⇒ *The four-for-four was not a paradox; it was the measurement, read at the
     wrong end of the chain.*

 ⛔ (3) THE PREMISE ABOUT THE DISTANCES IS WRONG, AND IT WAS THE WHOLE OF THE NAMED ROUTE.  The
     order writes "the two arms' distances differ by six per cent (13005 against 13865 Mpc)".
     ** At the adjudicated minima the arm's D_M is 14017.04 Mpc against the control's 13954.35 --
     0.449 per cent apart, and the ARM'S IS THE LARGER. **  Both the size and the sign are
     different: 13005/13865 belongs to the superseded configuration (r_s 135.46/144.53), where the
     arm's was the smaller.  ⌗ *The acoustic angles still agree -- l_A 301.80 against 301.54 -- so
     the cancellation the order relies on is real; it is the six per cent that is not.*

 ⚑ (4) AND THE ROUTE IS ELIMINATED BY MEASUREMENT AND NOT BY THE PREMISE.  The same source is
     projected through the OTHER arm's comoving distance -- `SRCXS`, one arm at a time, so the
     geometry is the only thing that moves.  ** It moves the contrast by -0.63 per cent on the
     control and +0.59 per cent on the arm, and REMOVING the distance difference entirely makes the
     arm/control excess LARGER, 1.045 -> 1.051. **  ⇒ *So the projection makes the excess and the
     distance difference is not how.*

 ⌗ (5) THE THIRD OUTCOME THE ORDER NAMED IS NOT WHAT HAPPENED.  The order allowed for a split
     between source and projection.  The source rung sits at 1.00 to within the statistic's own
     resolution, so there is nothing to split: the projection carries it all, and a little more than
     all.

 ⌗ (6) WHERE IN THE PROJECTION, AS ONE NUMBER.  The projection suppresses each arm's source
     oscillation -- rms 0.689 -> 0.166 on the control, 0.684 -> 0.174 on the arm.  ** The arm's
     projection suppresses its own source oscillation 5.4 per cent LESS (0.2543 against 0.2413). **
     That is the localisation restated, and it is as far as this receipt goes: the order's bound has
     not moved and no mechanism is proposed for it.

 ⌗ (7) AND THE EXCESS GROWS WITH WAVENUMBER WHERE THE SOURCE RATIO DOES NOT.  Split at q = 3 (ell
     ~ 905): the ell rung goes 1.031 -> 1.065 while the source rung is flat, 0.992 -> 0.992.

** THE GUARD THE ORDER ASKED FOR, AND IT CHANGED THE DEFINITION. **

 (a) ⛔ ** THE ell-SPACE DEFINITION CANNOT BE CARRIED TO THE SOURCE UNCHANGED, AND FINDING THAT OUT
     IS PART OF THE MEASUREMENT. **  `r6885+cc66.35`'s envelope is a running GEOMETRIC mean, which
     needs a strictly positive quantity.  D_l is; the source POWER is not -- it comes within
     6e-7 of the median at its troughs, so a log-mean there is dominated by near-zeros and
     (P-e)/e diverges.  ⇒ ** The envelope is therefore the running ARITHMETIC mean at EVERY rung,
     including the ell rung, and the receipt reports both definitions side by side: they differ by
     0.003 on the ell rung, against the 0.05 step being measured. **
 (b) THE ABSCISSA IS THE ACOUSTIC PHASE AND IT IS THE SAME OBJECT AT BOTH ENDS.  q = k r_s / pi in
     k and q = ell / l_A in ell, each arm on its own r_s and its own l_A.  ** Under the sharp-
     visibility map ell = k D_M these are the SAME variable, because l_A = pi D_M / r_s. **  And it
     is checked rather than assumed: the source power's own acoustic period in q is 1.0000 on the
     control against 0.9978 on the arm, and the raw spectrum's is 1.0347 against 1.0338 -- the arms
     agree to 0.2 per cent and 0.1 per cent, so the regression is a contrast and not a frequency
     mismatch.  The best-fit lag is +0.005 in q at the source and -0.001 in ell.
 (c) THE SMALLEST DIFFERENCE THE STATISTIC CAN EXPRESS, STATED AS THREE NUMBERS.  The self-null is
     exactly 1.000000; resampling the control through the other arm's abscissa and back returns
     0.9996 in k and 0.9975 in ell; and a contrast of a KNOWN factor injected into the control is
     read back as 1.039 (k, at last scattering), 1.046 (k, eta-integrated) and 1.038 (ell) for an
     injected 1.040.  ** So the floor is 0.6 per cent, set by the estimator's own bias at the
     source's oscillation depth, and the step being measured is 5.3 per cent. **
 (d) AND THE ONE RESOLUTION ARTEFACT THAT COULD HAVE MADE ALL OF IT IS RUN OUT.  The arms' k grids
     are not the same KIND of grid -- the control's is uniform, CR's is its physical ladder with
     varying spacing -- and the projection is a sum over that grid with `dk = np.gradient(kb)` as
     its measure.  ** `KCONT=1` puts the arm on the uniform grid at the same mode count, physics
     untouched, and the excess survives. **  *Three of the last five findings on this line were
     resolution or reference artefacts; this is the check that says this one is not.*

** WHAT THE INSTRUMENT GAINED, AND THE PROOF IT GAINED NOTHING ELSE. **

 `SRCSAVE` writes the source on the reporting path -- term by term at last scattering AND
 eta-integrated -- on the run's own k grid, and `SRCXS` writes beside it the same source projected
 through a scaled x0.  ** Unset, both are bit-identical against the banked base on both arms, and
 `SRCXS` set to 1.5 with `SRCSAVE` unset is bit-identical too. **  The four saved terms sum to the
 instrument's own `S` to 2.8e-17.  And the sliced runs reproduce the banked 185-bin refit spectra to
 4.9e-15 relative on the control and 6.3e-16 on the arm, which is what makes the k end and the ell
 end one run rather than two.

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The same statistic at four rungs -- source at last scattering, source eta-integrated, raw
     D_l, and the lensed/binned/amplitude-fitted D_l -- with the ratio at each: 0.996, 0.992,
     1.045, 1.047.
 (2) The source rungs are 1.00 to within 0.6 per cent, the statistic's own floor, over four envelope
     windows, two envelope definitions, four q sub-windows, three term subsets (monopole alone,
     monopole plus Doppler, the full source) and with or without the k-measure P(k).
 (3) The arms' comoving distances differ by 0.449 per cent with the arm's the larger, not 6.2 per
     cent with the arm's the smaller; and the acoustic angles agree to 0.085 per cent.
 (4) Projecting one arm's source through the other's distance moves its contrast by -0.63 and +0.59
     per cent; removing the difference raises the arm/control ratio to 1.051-1.052.
 (5) The projection's suppression of the source oscillation is 0.2413 on the control against 0.2543
     on the arm, a ratio of 1.054.
 (6) `SRCSAVE` and `SRCXS` are inert when unset, bit-identically, on both arms; the term split sums
     to `S`; and the sliced runs reproduce the banked spectra to 5e-15 relative.

WHAT IS NOT CLAIMED.

 * NOT a mechanism.  "The projection makes it" names a stage, not a cause, and this receipt does
   not say what within the projection produces 5.4 per cent.  The order's bound is unmoved.
 * NOT that the source is identical on the two arms.  It is not: the ratio is 0.992-0.996, which is
   a real deficit of about the statistic's floor, and its sign agrees with all four channels.
 * NOT that the projection is WRONG.  Nothing here bears on whether the flat kernel is the right
   kernel; `prop:flat` settles that and is not revisited.  A projection can manufacture a contrast
   difference while being exactly the correct projection for both arms.
 * NOT that the visibility width is the projection's route to it.  The arm's is 15 per cent wider,
   which SHALLOWS contrast, and rung 1 -> rung 2 -- where an eta-average acts without the kernel --
   moves the ratio by only -0.4 per cent.  That is a bound on one route, not the identification of
   another.
 * NOT that the ell-space 1.0401 of `r6885+cc66.35` is superseded.  It is reproduced here exactly
   under its own definition and comes out 1.047 under this receipt's, and the difference is the
   envelope definition, reported.
 * NOT that the q variable is exact.  The sharp-visibility map ell = k D_M is what makes q one
   object at both ends, and the visibility is 38-44 Mpc against D_M ~ 14000, a part in 300.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms run at
    `r6825+cc66.25`'s verified 185-bin refit minima -- `LH0=67.410309 LOM=0.309826 WBH2=0.021966
    NS=0.954248` for the control and `CRH0=68.581133 CROM=0.297209 WBH2=0.021524 NS=0.997952
    ZSTART=3e7 LEAFSCALES=1` for the arm.  Nothing here re-fits and nothing here moves.
  * The source banks are `spectra/r6911_source_{lcdm,cr}.npz` and the arm's uniform-grid control is
    `spectra/r6911_source_cr_kcont.npz`, all at `LSTEP=8 LMAXL=2000 HIER=1` in `KSLICE` pieces of
    250 on `KBATCH` boundaries.  The commands are in `r6911_directions/`.
  * The ell rung reads `spectra/cc66_r185_verify_{lcdm,cr}.npz` through `chi2_of_spectrum`'s own
    binning and CAMB's lensed/unlensed TT ratio at Planck 2018, exactly as `r6885+cc66.35` does.
  * The no-op pair is `spectra/r6911_noop.npz`, gated against `spectra/r6893_switch_screen_*`'s
    banked base.
  * NOTHING IS FITTED except the single amplitude the ell rung has always carried.  Every envelope
    window is reported over a range rather than chosen.
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
SRC = open(INST).read()
NEED = ('r6911_source_lcdm.npz', 'r6911_source_cr.npz', 'r6911_source_cr_kcont.npz',
        'r6911_noop.npz', 'cc66_r185_verify_lcdm.npz', 'cc66_r185_verify_cr.npz',
        'r6893_switch_screen_lcdm.npz', 'r6893_switch_screen_cr.npz')
for _need in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_need}`",
          os.path.exists(os.path.join(SP, _need)), _need)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK YET, so nothing is read and this receipt")
    print("     FAILS rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

S = {t: np.load(os.path.join(SP, f'r6911_source_{t}.npz')) for t in ('lcdm', 'cr')}
S['crkc'] = np.load(os.path.join(SP, 'r6911_source_cr_kcont.npz'))
VER = {t: np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')) for t in ('lcdm', 'cr')}
NOOP = np.load(os.path.join(SP, 'r6911_noop.npz'))

# ===================================================================================================
# PART 1 -- WHAT THE INSTRUMENT GAINED, AND THE PROOF IT GAINED NOTHING ELSE.
# ===================================================================================================
print("\nPART 1 -- THE TWO NEW NAMES, AND THE PROOF THEY ARE INERT WHEN UNSET.")
print("-" * 100)
print("    `SRCSAVE` writes the source on the REPORTING path -- term by term at last scattering and")
print("    eta-integrated, on the run's own k grid.  `SRCXS` writes beside it the same source")
print("    projected through x0 * SRCXS, which is the other arm's comoving distance.")
for t in ('lcdm', 'cr'):
    b = np.load(os.path.join(SP, f'r6893_switch_screen_{t}.npz'))
    n0, nx = NOOP[f'Dl__noop_{t}'], NOOP[f'Dl__xsonly_{t}']
    check(f"[{t}] `SRCSAVE` UNSET IS BIT-IDENTICAL against the banked base -- not 'small', equal",
          np.array_equal(n0, b['Dl__base']) and np.array_equal(NOOP[f'ls__noop_{t}'], b['ls__base']),
          f"max|dD_l| = {float(np.max(np.abs(n0 - b['Dl__base']))):.3e} over "
          f"{len(n0)} multipoles")
    check(f"[{t}] and `SRCXS=1.5` WITHOUT `SRCSAVE` is bit-identical too, which is what makes the "
          f"swap an output of the save rather than a knob on the physics",
          np.array_equal(nx, n0), f"max|dD_l| = {float(np.max(np.abs(nx - n0))):.3e}")
for t in ('lcdm', 'cr', 'crkc'):
    check(f"[{t}] the four saved source terms SUM to the instrument's own `S`, so the split is not "
          f"taken on trust and a future edit to `S` that forgets the save block fails here",
          float(np.max(S[t]['resid'])) < 1e-15, f"max|S - (sw+dp+isw+pol)| = "
          f"{float(np.max(S[t]['resid'])):.3e} over {len(S[t]['k'])} modes")
for t in ('lcdm', 'cr'):
    rel = float(np.max(np.abs(S[t]['Dl'] - VER[t]['Dl']) / np.abs(VER[t]['Dl'])))
    check(f"[{t}] ⚑ THE SLICED SOURCE RUN REPRODUCES THE BANKED 185-BIN REFIT SPECTRUM, which is "
          f"what makes the k end and the ell end ONE run rather than two",
          np.array_equal(S[t]['ls'], VER[t]['ls']) and rel < 1e-13,
          f"max relative |dD_l| = {rel:.3e} over {len(S[t]['ls'])} multipoles, "
          f"{int(S[t]['n_slices'])} slices")
# and the source-level gate that the bit-identity above is not an accident of one configuration:
# EVERY executable line naming either switch is either its own declaration or sits inside a guarded
# block.  *A binding is not a use -- `r6893+cc66.37`'s rule -- so the declarations are counted apart
# from the loads, and comment lines are stripped first because the prose here names the guard.*
_CODE = [ln for ln in SRC.splitlines() if not ln.lstrip().startswith('#')]
_USE = [ln for ln in _CODE if '_SRCS' in ln or '_SRCXS' in ln]
_DECL = [ln for ln in _USE if ln.startswith(('_SRCS =', '_SRCXS ='))]
# ** r6931+70.1: STALE (c).  `ba9a98b5` (r6915+cc66.41, "the cross term is not the channel") added a
#   third save switch beside these two, `SRCDEC` (`_SRCD`), and hoisted the term-by-term source
#   block this receipt's save reads so the two saves share it: its guard went from `if _SRCS:` to
#   `if _SRCS or _SRCD:`.  That line names `_SRCS`, sits at the top level of the function, and so
#   failed "every use indented under a guard" although it IS a guard -- the block under it only
#   builds `_sw/_dp/_iw/_pl/_md` for the saves and assigns nothing the spectrum reads, and the
#   SRCSAVE-unset bit-identity above is re-run on the current file and still exact.  ** Same finding
#   (the switch is inert when unset, and every load is confined), re-counted: 2 declarations, 2
#   `if _SRCS:` guards plus the one shared `if _SRCS or _SRCD:` guard, and SRCDEC itself declared. **
# ⛭ r6977: the shared guard grew a third disjunct when cc66's r6959 added `SRCETA` to it --
#   `if _SRCS or _SRCD or _SRCE:`.  ** The shape of the finding is unchanged: the switch is inert
#   when unset and every load is confined to a guarded block.  What moved is the guard's text, and
#   a check that reads a guard by its exact text has to be re-pointed when a disjunct is added. **
#   ⌗ *Both spellings are accepted rather than only the new one, because the receipt's claim is
#   about confinement and a two-disjunct guard confines exactly as well as a three-disjunct one.*
_GUARD = [ln for ln in _USE if ln.strip() in ('if _SRCS:', 'if _SRCS or _SRCD:',
                                              'if _SRCS or _SRCD or _SRCE:')]
check("`SRCSAVE` and `SRCXS` are declared beside `_SWSRC`/`_DPSRC` and every load of either sits "
      "inside an `if _SRCS:` block (or the `if _SRCS or _SRCD:` block `SRCDEC` shares) -- a binding "
      "is not a use, so the two declarations are counted apart from the loads and the bit-identity "
      "above is the proof that the loads are confined",
      len(_DECL) == 2 and len(_GUARD) == 3
      and sum(ln.strip() == 'if _SRCS:' for ln in _GUARD) == 2
      and "_SRCD = os.environ.get('SRCDEC')" in SRC
      and SRC.count('if _SRCXS != 1.0:') == 1
      and all(ln.startswith(' ' * 8) or ln in _DECL or ln in _GUARD for ln in _USE),
      f"{len(_DECL)} declarations, {len(_GUARD)} guarded blocks, {len(_USE)} executable lines in all,"
      f" the deepest at indent {max(len(ln) - len(ln.lstrip()) for ln in _USE)}")

# ===================================================================================================
# PART 2 -- THE PREMISE ABOUT THE DISTANCES.
# ===================================================================================================
print("\nPART 2 -- THE ORDER'S SIX PER CENT, AGAINST THE ADJUDICATED CONFIGURATION'S OWN NUMBERS.")
print("-" * 100)
DM = {t: float(VER[t]['D_M']) for t in ('lcdm', 'cr')}
RS = {t: float(VER[t]['r_s']) for t in ('lcdm', 'cr')}
LA = {t: float(VER[t]['l_A']) for t in ('lcdm', 'cr')}
print(f"    {'arm':6s} {'D_M/Mpc':>12s} {'r_s/Mpc':>10s} {'l_A':>9s}")
for t in ('lcdm', 'cr'):
    print(f"    {t:6s} {DM[t]:12.3f} {RS[t]:10.3f} {LA[t]:9.3f}")
dDM = DM['cr'] / DM['lcdm'] - 1
dLA = LA['cr'] / LA['lcdm'] - 1
print(f"    arm/control:  D_M {1+dDM:.6f} ({100*dDM:+.3f}%)   r_s "
      f"{RS['cr']/RS['lcdm']:.6f}   l_A {1+dLA:.6f} ({100*dLA:+.3f}%)")
print(f"    the order's pair, 13005 against 13865, is {13005/13865:.4f} -- "
      f"{100*(13005/13865-1):+.1f}% and the ARM'S SMALLER")
check("⛔ ** THE PREMISE IS WRONG IN SIZE AND IN SIGN. **  The arms' comoving distances differ by "
      "under half a per cent at the adjudicated minima, and the ARM'S IS THE LARGER; 13005/13865 "
      "belongs to the superseded configuration (r_s 135.46/144.53)",
      abs(dDM) < 0.006 and dDM > 0,
      f"{100*dDM:+.3f}% against the order's -6.2%")
check("...and the cancellation the order relies on IS real -- the acoustic angles agree -- so it is "
      "the six per cent and not the reasoning that fails",
      abs(dLA) < 0.002, f"l_A agree to {100*abs(dLA):.3f}%")

# ===================================================================================================
# PART 3 -- THE STATISTIC, DEFINED ONCE, AND ITS OWN RESOLUTION.
# ===================================================================================================
print("\nPART 3 -- ONE STATISTIC, AND THE THREE NUMBERS THAT SAY WHAT IT CAN AND CANNOT EXPRESS.")
print("-" * 100)
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                               # noqa: E402

LC, FACB = CS.bin_center_and_fac()
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LGR = np.arange(len(_le), dtype=float)
RAT = np.ones_like(_le)
_m = _un > 0
RAT[_m] = _le[_m] / _un[_m]
mb = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, LGR, RAT))
KEEP = (np.isfinite(mb(VER['lcdm']['ls'].astype(float), VER['lcdm']['Dl']))
        & (LC >= 100) & (LC <= 1900))
FISH = np.linalg.inv(CS.COV_TT[np.ix_(KEEP, KEEP)])
DK, LCK, FACK = CS.X_DATA[KEEP], LC[KEEP], FACB[KEEP]


def env_a(x, y, win):
    """the running ARITHMETIC mean of y over one window of x -- see the guard note (a)"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def env_g(x, y, win):
    """`r6885+cc66.35`'s GEOMETRIC mean, kept so the definition change is reported and not hidden"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.exp(np.mean(np.log(np.maximum(y[m], 1e-300))))
    return e


def osc(x, y, win=1.0, fn=env_a):
    e = fn(x, y, win)
    return (y - e) / e


LO, HI, NG = 0.85, 5.75, 1200


def stat(qA, oA, qB, oB, lo=LO, hi=HI, lag=0.0):
    """the arm's relative oscillation as a multiple of the control's, both on ONE q grid"""
    g = np.linspace(lo, hi, NG)
    a, b = np.interp(g + lag, qA, oA), np.interp(g, qB, oB)
    return dict(reg=float(np.sum(a * b) / np.sum(b * b)),
                rms=float(np.sqrt(np.sum(a * a) / np.sum(b * b))),
                cos=float(np.sum(a * b) / np.sqrt(np.sum(a * a) * np.sum(b * b))),
                dA=float(a.std()), dB=float(b.std()))


def bestlag(qA, oA, qB, oB, span=0.12):
    ls = np.linspace(-span, span, 241)
    cs = [stat(qA, oA, qB, oB, lag=t)['cos'] for t in ls]
    j = int(np.argmax(cs))
    return float(ls[j]), float(cs[j])


QK = {t: S[t]['k'] * float(S[t]['r_s']) / np.pi for t in S}
QL = {t: S[t]['ls'].astype(float) / (np.pi * float(S[t]['D_M']) / float(S[t]['r_s'])) for t in S}


def fit4(t):
    m = mb(VER[t]['ls'].astype(float), VER[t]['Dl'])[KEEP]
    A = float(m @ FISH @ DK / (m @ FISH @ m))
    return LCK / LA[t], A * m * FACK


R4 = {t: fit4(t) for t in ('lcdm', 'cr')}
print(f"    q = k r_s / pi in k and q = ell / l_A in ell -- ONE variable, because l_A = pi D_M/r_s")
print(f"    window = one acoustic period (Delta q = 1); q in [{LO:.2f}, {HI:.2f}], which is "
      f"ell {LO*LA['lcdm']:.0f}-{HI*LA['lcdm']:.0f}")
print(f"    modes per acoustic period on the k grids: control "
      f"{len(QK['lcdm'])/(QK['lcdm'][-1]-QK['lcdm'][0]):.0f}, arm "
      f"{len(QK['cr'])/(QK['cr'][-1]-QK['cr'][0]):.0f}; bins per period in ell "
      f"{len(LCK)/(R4['lcdm'][0][-1]-R4['lcdm'][0][0]):.0f}")

print("\n  (a) WHY THE ENVELOPE IS AN ARITHMETIC MEAN AND NOT `r6885`'s GEOMETRIC ONE")
_mn = {t: float(np.min(S[t]['S_ls'] ** 2) / np.median(S[t]['S_ls'] ** 2)) for t in ('lcdm', 'cr')}
print(f"      the source POWER at its troughs, as a fraction of its own median: "
      f"control {_mn['lcdm']:.3e}, arm {_mn['cr']:.3e}")
print(f"      the binned lensed D_l, same quantity: {float(np.min(R4['lcdm'][1])/np.median(R4['lcdm'][1])):.3e}")
check("⛔ the ell-space definition CANNOT be carried to the source unchanged: the source power comes "
      "within a part in a million of zero at its troughs, where a running LOG mean is dominated by "
      "near-zeros -- so the envelope is arithmetic at EVERY rung, and both are reported",
      max(_mn.values()) < 1e-5
      and float(np.min(R4['lcdm'][1]) / np.median(R4['lcdm'][1])) > 0.05,
      f"source {max(_mn.values()):.2e} of median against D_l "
      f"{float(np.min(R4['lcdm'][1])/np.median(R4['lcdm'][1])):.3f}")

print("\n  (b) IS q ACTUALLY THE ALIGNER?  the acoustic period of each rung, measured in q")
PER = {}
for nm, t, q, y in (('source at last scattering', 'lcdm', QK['lcdm'], S['lcdm']['S_ls'] ** 2),
                    ('source at last scattering', 'cr', QK['cr'], S['cr']['S_ls'] ** 2),
                    ('source eta-integrated', 'lcdm', QK['lcdm'], S['lcdm']['S_i'] ** 2),
                    ('source eta-integrated', 'cr', QK['cr'], S['cr']['S_i'] ** 2),
                    ('raw D_l', 'lcdm', QL['lcdm'], S['lcdm']['Dl']),
                    ('raw D_l', 'cr', QL['cr'], S['cr']['Dl'])):
    m = (q > 0.8) & (q < 8.0) if q is not QL[t] else (q > 0.3) & (q < 6.7)
    o_ = 12 if len(q) > 500 else 6
    pk = argrelextrema(y[m], np.greater, order=o_)[0]
    PER[(nm, t)] = float(np.median(np.diff(q[m][pk])))
    print(f"      {nm:26s} {t:5s} period in q = {PER[(nm, t)]:.4f}")
for nm in ('source at last scattering', 'source eta-integrated', 'raw D_l'):
    r = PER[(nm, 'cr')] / PER[(nm, 'lcdm')]
    check(f"the two arms' acoustic period in q AGREES at the `{nm}` rung, so the regression there is "
          f"a contrast and not a frequency mismatch",
          abs(r - 1) < 0.005, f"arm/control period = {r:.5f}")

print("\n  (c) THE THREE NUMBERS THAT BOUND THE STATISTIC")
FLOOR = []
for nm, key, ax in (('source at last scattering', 'S_ls', 'k'),
                    ('source eta-integrated', 'S_i', 'k'),
                    ('lensed+binned+fitted D_l', None, 'l4')):
    if ax == 'k':
        qB, yB = QK['lcdm'], S['lcdm'][key] ** 2
        qA = QK['cr']
        oA = osc(qA, S['cr'][key] ** 2)
    else:
        qB, yB = R4['lcdm']
        qA, oA = R4['cr'][0], osc(*R4['cr'])
    oB = osc(qB, yB)
    self_ = stat(qB, oB, qB, oB)['reg']
    eB = env_a(qB, yB, 1.0)
    inj = {f: stat(qB, osc(qB, eB * (1 + f * (yB - eB) / eB)), qB, oB)['reg'] for f in (1.04, 1.20)}
    res = stat(qB, np.interp(qB, qA, np.interp(qA, qB, oB)), qB, oB)['reg']
    FLOOR += [abs(inj[1.04] - 1.04), abs(res - 1)]
    print(f"      {nm:26s}  self {self_:.6f}   injected 1.040 -> {inj[1.04]:.4f}   "
          f"injected 1.200 -> {inj[1.20]:.4f}   resample-null {res:.5f}")
    check(f"[{nm}] the statistic returns EXACTLY 1 against itself and recovers a KNOWN injected "
          f"contrast -- `r4558`'s rule, which applies to a measurement as much as to a knob",
          abs(self_ - 1) < 1e-9 and abs(inj[1.04] - 1.04) < 0.01 and abs(inj[1.20] - 1.20) < 0.045,
          f"self {self_:.6f}, 1.040 -> {inj[1.04]:.4f}, 1.200 -> {inj[1.20]:.4f}")
    check(f"[{nm}] ...and resampling the control through the OTHER arm's abscissa and back returns "
          f"it, so the two grids' difference is not what a ratio would read",
          abs(res - 1) < 0.004, f"{res:.5f}")
FLOOR = float(max(FLOOR))
print(f"      ⇒ the floor, as the largest of those: {100*FLOOR:.2f} per cent")

# ===================================================================================================
# PART 4 -- THE FOUR RUNGS.
# ===================================================================================================
print("\nPART 4 -- THE SAME STATISTIC AT FOUR POINTS IN THE CHAIN.  THIS IS THE ORDER'S ANSWER.")
print("-" * 100)
RUNG = [('1  source at last scattering', 'S_ls', 'k'),
        ('1m   monopole + Doppler only', 'md_ls', 'k'),
        ('1s   monopole alone', 'sw_ls', 'k'),
        ('2  source eta-integrated', 'S_i', 'k'),
        ('2m   monopole + Doppler only', 'md_i', 'k'),
        ('2P   with the k-measure P(k)', 'S_i_P', 'k'),
        ('3  raw D_l, this run', 'Dl', 'l'),
        ('4  lensed + binned + fitted', None, 'l4')]


def rung(nm, key, ax, t):
    if ax == 'k':
        y = S[t]['S_i'] ** 2 * S[t]['P'] if key == 'S_i_P' else S[t][key] ** 2
        return QK[t], y
    if ax == 'l':
        return QL[t], S[t][key]
    return R4[t]


print(f"    {'rung':30s} {'ratio':>8s} {'rms-rat':>8s} {'cos':>8s} {'rms ctl':>8s} {'rms arm':>8s} "
      f"{'lag':>8s}")
RES = {}
for nm, key, ax in RUNG:
    qB, yB = rung(nm, key, ax, 'lcdm')
    qA, yA = rung(nm, key, ax, 'cr')
    oB, oA = osc(qB, yB), osc(qA, yA)
    s = stat(qA, oA, qB, oB)
    bl, bc = bestlag(qA, oA, qB, oB)
    RES[nm] = s
    print(f"    {nm:30s} {s['reg']:8.4f} {s['rms']:8.4f} {s['cos']:8.4f} {s['dB']:8.4f} "
          f"{s['dA']:8.4f} {bl:+8.4f}")
SRCR = RES['1  source at last scattering']['reg']
SRCI = RES['2  source eta-integrated']['reg']
ELL3 = RES['3  raw D_l, this run']['reg']
ELL4 = RES['4  lensed + binned + fitted']['reg']
check("⚑ ** THE SOURCE RATIO IS 1.00 AND THE ell RATIO IS 1.045: the excess is NOT in the dynamics, "
      "and it is manufactured between k and ell. **  This is the order's second branch",
      abs(SRCR - 1) < 3 * FLOOR and abs(SRCI - 1) < 3 * FLOOR and ELL4 > 1.02
      and ELL4 - SRCI > 0.03,
      f"source {SRCR:.4f} / {SRCI:.4f} against ell {ELL3:.4f} / {ELL4:.4f}, a step of "
      f"{ELL4-SRCI:+.4f} on a floor of {FLOOR:.4f}")
check("...and the source ratio is if anything BELOW one, which is the direction all four of the "
      "order's channels point -- so four-for-four needed nothing upstream to overcome it",
      SRCR < 1.0 and SRCI < 1.0, f"{SRCR:.4f} at last scattering, {SRCI:.4f} eta-integrated")
check("the eta-integration alone -- an average over the visibility WITHOUT the kernel -- barely "
      "moves it, so the step is the kernel's and not the visibility width's",
      abs(SRCI - SRCR) < 0.01, f"{SRCR:.4f} -> {SRCI:.4f}, {100*(SRCI-SRCR):+.2f}%")
check("the lensing and the binning are not what make it either: the RAW spectrum already carries "
      "the excess and the banked pipeline adds 0.002",
      abs(ELL4 - ELL3) < 0.01, f"raw {ELL3:.4f} -> lensed/binned/fitted {ELL4:.4f}")
check("and the term subsets agree -- monopole alone, monopole plus Doppler (what the order names), "
      "and the full source -- so the answer is not a choice of terms",
      max(abs(RES[n]['reg'] - 1) for n in ('1m   monopole + Doppler only', '1s   monopole alone',
                                          '2m   monopole + Doppler only')) < 3 * FLOOR,
      "  ".join(f"{n.strip()[:18]} {RES[n]['reg']:.4f}" for n in
                ('1m   monopole + Doppler only', '1s   monopole alone',
                 '2m   monopole + Doppler only')))
check("and including the k-measure P(k) -- whose `dk` is one-sided at each batch edge and whose "
      "tilt differs between the arms -- moves the source rung by less than the floor",
      abs(RES['2P   with the k-measure P(k)']['reg'] - SRCI) < FLOOR,
      f"{SRCI:.4f} -> {RES['2P   with the k-measure P(k)']['reg']:.4f}")

print("\n  (b) AND THE PROJECTION'S SUPPRESSION, WHICH IS THE SAME FACT AS ONE NUMBER PER ARM")
SUP = {}
for t in ('lcdm', 'cr'):
    g = np.linspace(LO, HI, NG)
    a = np.interp(g, QK[t], osc(QK[t], S[t]['S_i'] ** 2)).std()
    b = np.interp(g, QL[t], osc(QL[t], S[t]['Dl'])).std()
    SUP[t] = b / a
    print(f"      {t:5s} rms o(source) {a:.4f} -> rms o(D_l) {b:.4f}   suppression {b/a:.4f}")
check("⚑ the arm's projection RETAINS more of its OWN source oscillation than the control's does, "
      "by the same 5 per cent the ell rung reports -- the localisation restated as one number",
      SUP['cr'] / SUP['lcdm'] > 1.02,
      f"{SUP['lcdm']:.4f} against {SUP['cr']:.4f}, ratio {SUP['cr']/SUP['lcdm']:.4f}")

print("\n  (c) THE EXCESS GROWS WITH WAVENUMBER WHERE THE SOURCE RATIO DOES NOT")
SPL = {}
for nm, key, ax in (('source eta-integrated', 'S_i', 'k'), ('raw D_l', 'Dl', 'l')):
    qB, yB = rung(nm, key, ax, 'lcdm')
    qA, yA = rung(nm, key, ax, 'cr')
    oB, oA = osc(qB, yB), osc(qA, yA)
    lo_ = stat(qA, oA, qB, oB, LO, 3.0)['reg']
    hi_ = stat(qA, oA, qB, oB, 3.0, HI)['reg']
    SPL[nm] = (lo_, hi_)
    print(f"      {nm:26s} q<3 (ell<{3*LA['lcdm']:.0f}) {lo_:.4f}    q>3 {hi_:.4f}    "
          f"change {hi_-lo_:+.4f}")
check("the ell rung's excess RISES with wavenumber and the source rung's is flat, which is one more "
      "way of saying the two are not the same measurement",
      SPL['raw D_l'][1] - SPL['raw D_l'][0] > 0.02
      and abs(SPL['source eta-integrated'][1] - SPL['source eta-integrated'][0]) < 0.01,
      f"ell {SPL['raw D_l'][0]:.4f} -> {SPL['raw D_l'][1]:.4f} against source "
      f"{SPL['source eta-integrated'][0]:.4f} -> {SPL['source eta-integrated'][1]:.4f}")

# ===================================================================================================
# PART 5 -- THE DEFINITION'S OWN SPAN.
# ===================================================================================================
print("\nPART 5 -- THE SAME TABLE OVER FOUR WINDOWS AND BOTH ENVELOPE DEFINITIONS.")
print("-" * 100)
SPAN = {}
for nm, key, ax in (('1 source at last scattering', 'S_ls', 'k'),
                    ('2 source eta-integrated', 'S_i', 'k'),
                    ('3 raw D_l', 'Dl', 'l')):
    for fn, fnm in ((env_a, 'arithmetic'), (env_g, 'geometric')):
        row = []
        for w in (0.75, 1.0, 1.25, 1.5):
            qB, yB = rung(nm, key, ax, 'lcdm')
            qA, yA = rung(nm, key, ax, 'cr')
            row.append(stat(qA, osc(qA, yA, w, fn), qB, osc(qB, yB, w, fn),
                            LO + 0.5 * (w - 1), HI - 0.5 * (w - 1))['reg'])
        SPAN[(nm, fnm)] = row
        print(f"    {nm:28s} {fnm:11s} " + "   ".join(f"w{w:.2f} {v:.4f}"
                                                      for w, v in zip((0.75, 1.0, 1.25, 1.5), row)))
_src = [v for (nm, f), r in SPAN.items() if nm.startswith(('1 ', '2 ')) for v in r]
_ell = [v for (nm, f), r in SPAN.items() if nm.startswith('3 ') for v in r]
check("⚑ ** THE GAP IS NOT A DEFINITION. **  Over four windows and both envelope definitions the "
      "source rungs never leave the neighbourhood of one and the ell rung never comes near it",
      max(_src) < 1.01 and min(_ell) > 1.03 and min(_ell) - max(_src) > 0.025,
      f"source {min(_src):.4f}-{max(_src):.4f}, ell {min(_ell):.4f}-{max(_ell):.4f}")
check("...and the ell rung under `r6885+cc66.35`'s own GEOMETRIC envelope agrees with this "
      "receipt's arithmetic one to within the definition's own span, so 1.0401 is not superseded",
      abs(np.mean(SPAN[('3 raw D_l', 'geometric')])
          - np.mean(SPAN[('3 raw D_l', 'arithmetic')])) < 0.01,
      f"geometric mean {np.mean(SPAN[('3 raw D_l','geometric')]):.4f} against arithmetic "
      f"{np.mean(SPAN[('3 raw D_l','arithmetic')]):.4f}")

# ===================================================================================================
# PART 6 -- THE DISTANCE, RUN OUT ONE ARM AT A TIME.
# ===================================================================================================
print("\nPART 6 -- THE ORDER'S NAMED ROUTE, MEASURED: THE SAME SOURCE THROUGH THE OTHER DISTANCE.")
print("-" * 100)
SW = {}
for t in ('lcdm', 'cr'):
    xs = float(S[t]['xswap'])
    q_own, q_sw = QL[t], S[t]['ls'].astype(float) / (np.pi * xs * float(S[t]['D_M']) / float(S[t]['r_s']))
    o_own, o_sw = osc(q_own, S[t]['Dl']), osc(q_sw, S[t]['Dl_swap'])
    SW[t] = dict(own=(q_own, o_own), sw=(q_sw, o_sw), xs=xs,
                 lA_sw=np.pi * xs * float(S[t]['D_M']) / float(S[t]['r_s']))
    r = stat(q_sw, o_sw, q_own, o_own)
    SW[t]['self'] = r['reg']
    print(f"    {t:5s} x0 * {xs:.6f}: l_A {LA[t]:.3f} -> {SW[t]['lA_sw']:.3f};  its own contrast "
          f"moves to {r['reg']:.4f} of itself ({100*(r['reg']-1):+.2f}%, cos {r['cos']:.4f})")
_b = stat(*SW['cr']['own'], *SW['lcdm']['own'])['reg']
_a = stat(*SW['cr']['sw'], *SW['lcdm']['own'])['reg']
_c = stat(*SW['cr']['own'], *SW['lcdm']['sw'])['reg']
print(f"\n    arm/control, both at their own D_M          : {_b:.4f}")
print(f"    arm/control, the ARM moved to the control's : {_a:.4f}")
print(f"    arm/control, the CONTROL moved to the arm's : {_c:.4f}")
check("⛔ ** THE DISTANCE DIFFERENCE IS NOT HOW THE PROJECTION MAKES IT. **  Moving one arm's source "
      "to the other's distance changes its contrast by well under a per cent, and REMOVING the "
      "difference makes the arm/control excess LARGER rather than smaller",
      max(abs(SW[t]['self'] - 1) for t in ('lcdm', 'cr')) < 0.02 and _a > _b and _c > _b,
      f"control {100*(SW['lcdm']['self']-1):+.2f}%, arm {100*(SW['cr']['self']-1):+.2f}%; "
      f"{_b:.4f} -> {_a:.4f} / {_c:.4f}")
check("...and the swap acts in the direction a wider kernel should: the arm's LARGER D_M gives more "
      "contrast, so the diagnostic is connected and is not reporting a null",
      SW['cr']['self'] > 1 > SW['lcdm']['self'],
      f"arm at the control's smaller D_M {SW['cr']['self']:.4f}, control at the arm's larger "
      f"{SW['lcdm']['self']:.4f}")

# ===================================================================================================
# PART 7 -- THE GRID, WHICH IS THE ARTEFACT THAT COULD HAVE MADE ALL OF IT.
# ===================================================================================================
print("\nPART 7 -- `KCONT=1`: THE ARM ON THE CONTROL'S KIND OF k GRID, PHYSICS UNTOUCHED.")
print("-" * 100)
print(f"    the arm's own grid is its PHYSICAL ladder k_L = sqrt(L(L+2))/r_0 -- "
      f"{len(S['cr']['k'])} modes, dk varying by a factor "
      f"{float(np.max(np.diff(S['cr']['k']))/np.min(np.diff(S['cr']['k']))):.2f} across the range")
print(f"    `KCONT=1` replaces it with the uniform continuum sampling -- {len(S['crkc']['k'])} "
      f"modes, dk varying by "
      f"{float(np.max(np.diff(S['crkc']['k']))/np.min(np.diff(S['crkc']['k']))):.4f}; the control's "
      f"grid has {len(S['lcdm']['k'])} modes")
KC = {}
for nm, key, ax in (('1 source at last scattering', 'S_ls', 'k'),
                    ('2 source eta-integrated', 'S_i', 'k'),
                    ('3 raw D_l', 'Dl', 'l')):
    qB, yB = rung(nm, key, ax, 'lcdm')
    qA, yA = rung(nm, key, ax, 'crkc')
    KC[nm] = stat(qA, osc(qA, yA), qB, osc(qB, yB))['reg']
    q2, y2 = rung(nm, key, ax, 'cr')
    print(f"    {nm:28s} ladder {stat(q2, osc(q2, y2), qB, osc(qB, yB))['reg']:.4f}    "
          f"uniform {KC[nm]:.4f}")
check("⚑ ** THE EXCESS IS NOT THE k GRID. **  On the uniform grid at the control's own mode count, "
      "the arm's physics untouched, the source rungs are still one and the ell rung still carries "
      "the excess -- so the sampling of an oscillating integrand is not what a contrast read off "
      "the projection is reading",
      abs(KC['1 source at last scattering'] - 1) < 3 * FLOOR
      and abs(KC['2 source eta-integrated'] - 1) < 3 * FLOOR
      and KC['3 raw D_l'] > 1.02,
      f"source {KC['1 source at last scattering']:.4f} / "
      f"{KC['2 source eta-integrated']:.4f}, ell {KC['3 raw D_l']:.4f}")
check("...and `KCONT=1` demonstrably reaches the spectrum, so this is a null from a connected knob "
      "and not `r4558`'s unwired one",
      not np.array_equal(S['crkc']['Dl'], S['cr']['Dl']),
      f"max relative |dD_l| ladder against uniform = "
      f"{float(np.max(np.abs(S['crkc']['Dl']-S['cr']['Dl'])/np.abs(S['cr']['Dl']))):.3e}")

# ===================================================================================================
print("\n" + "=" * 100)
print(f"""
WHAT `r6911` ASKED AND WHAT THE CHAIN SAYS.

  The order asked for ONE statistic at two points: the contrast of the source in k, against the
  {ELL4:.3f} it has in ell.  ⇒ *** THE SOURCE RATIO IS {SRCR:.4f} AT LAST SCATTERING AND {SRCI:.4f}
  ETA-INTEGRATED, AND THE ell RATIO IS {ELL3:.4f} RAW AND {ELL4:.4f} BANKED. ***  Over four envelope
  windows and both envelope definitions the source rungs span {min(_src):.4f}-{max(_src):.4f} and
  the ell rung {min(_ell):.4f}-{max(_ell):.4f}, against a statistic floor of {100*FLOOR:.2f} per
  cent set by its own bias on a KNOWN injected contrast.  ** So the excess is manufactured between
  k and ell, and the order's second branch is the answer. **

  ⚑ AND THE FOUR-FOR-FOUR PUZZLE DISSOLVES RATHER THAN BEING SOLVED.  The order's difficulty was
  that four channels which each shallow the troughs are all larger on this arm, so something
  upstream had to overcome all four.  ** Upstream the arm's oscillation is {SRCR:.4f} of the
  control's -- very slightly SHALLOWER, which is exactly the direction those four point. **  Nothing
  overcomes them because nothing had to.

  ⛔ THE NAMED ROUTE IS OUT TWICE OVER.  The premise is wrong in size and sign -- the arms' D_M
  differ by {100*dDM:+.3f} per cent with the arm's the LARGER, not -6.2 per cent with the arm's the
  smaller -- and the route is then eliminated by measurement anyway: projecting one arm's source
  through the other's distance moves its contrast by {100*(SW['lcdm']['self']-1):+.2f} and
  {100*(SW['cr']['self']-1):+.2f} per cent, and removing the difference takes the arm/control ratio
  UP, {_b:.4f} -> {_a:.4f}.

  ⌗ WHERE IN THE PROJECTION, AS FAR AS THIS RECEIPT GOES.  The arm's projection RETAINS
  {SUP['cr']/SUP['lcdm']:.4f} times as much of its own source oscillation as the control's does
  ({SUP['lcdm']:.4f} against {SUP['cr']:.4f}), the excess rises with wavenumber
  ({SPL['raw D_l'][0]:.4f} -> {SPL['raw D_l'][1]:.4f}) where the source ratio is flat
  ({SPL['source eta-integrated'][0]:.4f} -> {SPL['source eta-integrated'][1]:.4f}), it is not the
  visibility width acting before the kernel ({SRCR:.4f} -> {SRCI:.4f}), not the lensing or the
  binning ({ELL3:.4f} -> {ELL4:.4f}), and not the k grid (uniform {KC['3 raw D_l']:.4f}).
  ** The order's bound has not moved and no mechanism is offered.  This receipt locates the stage. **

  ⌗ AND THE GUARD EARNED ITS PLACE.  `r6885`'s geometric envelope cannot be carried to the source
  at all -- the source power comes within {max(_mn.values()):.1e} of its own median at the troughs
  -- so the envelope was changed to an arithmetic mean at EVERY rung and both are reported; the
  abscissa's alignment was measured rather than assumed (the arms' acoustic period in q agrees to
  {100*abs(PER[('source at last scattering','cr')]/PER[('source at last scattering','lcdm')]-1):.2f}
  per cent); and the two artefacts that could have produced the whole answer -- the two arms'
  different k grids, and the interpolation between two abscissae -- were run out rather than argued.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the acoustic contrast excess is not in the source.  The same statistic that reads
{ELL4:.4f} on the reported spectrum reads {SRCR:.4f} on the source at last scattering and
{SRCI:.4f} on the eta-integrated source, and the gap survives four envelope windows, both envelope
definitions, three term subsets, the k-measure, and the arm's k grid replaced by the control's kind.
The excess is manufactured between k and ell.  The order's named route is eliminated: the arms'
comoving distances differ by {100*dDM:+.3f} per cent with the arm's the larger -- not -6.2 per cent
-- and projecting either arm's source through the other's distance moves its contrast by under a
per cent in the direction that makes the excess bigger, not smaller.  The projection suppresses the
arm's source oscillation {1/(SUP['cr']/SUP['lcdm']):.4f} times as much as it does the control's --
equivalently, the arm retains {SUP['cr']/SUP['lcdm']:.4f} times as much of its own.
NOT CLAIMED: a mechanism within the projection; that the projection is the wrong projection; that
the visibility width is its route; that the source is identical on the two arms -- it is
{SRCI:.4f}, shallower, and that sign is the four channels' own.
""")
