"""
P15_the_source_decomposition_is_reachable_on_the_reporting_path_and_the_neutrinos_have_a_knob
=============================================================================================

LEVEL: an INSTRUMENT repair and its proof, then the two measurements the repair makes possible --
`r6889`'s order, which put the knob shadow `r6885+cc66.35` found ahead of everything else.

** THE SHADOW, AND WHY IT IS THE THIRD OF ITS KIND. **  `r4558` added `_SWSRC` and `_DPSRC` -- the
monopole and Doppler-dipole switches -- and calibrated them, on `los_spectrum`.  ** The HIERARCHY
path builds its own source at the foot of `los_hier`, and the LOW-ELL path builds a third at the foot
of `main`, and neither read them. **  `HIER=1` is the path every refit number in this sector is
computed on, so `DPSRC=0` there returned a BIT-IDENTICAL spectrum on both arms while the same switch
moves D_l by 62 per cent on the path it does reach.  *`_ISW` was wired to all three in the same
revision and these two were not, which is the whole of the difference -- and it is the same shape as
the `NS` literal at `cc66.17`: a knob verified on the path it reaches and used on the path it does
not.*

** WHAT WAS DONE, IN ONE SENTENCE EACH. **

 (1) `_SWSRC` and `_DPSRC` are wired into the hierarchy path and the low-multipole path, ADDITIVELY:
     both are multipliers whose default is 1.0, and the monopole bracket is SPLIT so the switch
     multiplies g(Theta_0+Psi) and not the polarisation term that shares the bracket and already has
     `PISRC`.
 (2) ** THE DEFAULT IS PROVED AND NOT ASSERTED **: the unset configuration is re-run on both arms and
     gated BIT-IDENTICAL against the banked `cc66_r185_verify_{lcdm,cr}` before any other number in
     this receipt is read.  ⌗ *And "bit-identical" is meant literally.  The first version of the
     split wrote `_SWSRC * g_ * (Th0 + Ps) + g_ * _PI * Pi / 4`, which sums in a different ORDER
     from the original and cost max |dD_l| = 1.1e-16 -- immaterial physically and still not zero.
     Keeping the factor inside the bracket, `g_ * (_SWSRC * (Th0 + Ps) + _PI * Pi / 4)`, makes it
     exact, because x * 1.0 is.  **That was measured, not foreseen**, and it is recorded because a
     revision whose whole claim is "this changes nothing" should be able to say zero and mean it.*
 (3) ** AND EACH IS CALIBRATED WHERE IT IS NEWLY WIRED **, because r4558's own note is the rule that
     this revision exists to enforce: a knob that reports no change cannot be told from a knob that
     is not connected.
 (4) The two bracketing tests are re-run on the REPORTING path, where `r6885+cc66.35` could only run
     them on the other one and said so.
 (5) ⚑ AND THE FREE-STREAMING PHASE SHIFT GETS A KNOB, because the order asked whether one was
     buildable and what it would cost.  ** It is four lines. **  What makes a neutrino free-stream
     rather than behave as a perfect fluid is its anisotropic stress sigma_nu = F_2/2, at exactly two
     dynamical sites -- the Euler equation and Psi's shear term -- so `NUFS` multiplies sigma_nu and
     the F_2 source.  At `NUFS=0` the quadrupole is never sourced and the whole l>=2 ladder stays
     zero, ** and the ladder's initial condition is exactly zero **, so the sector degenerates to a
     perfect fluid at the SAME background density with nothing in the expansion history touched.
     ⌗ *`NUFS=0` removes the whole free-streaming effect -- the phase shift AND the drag on the
     amplitude -- so the PHASE half is the peak-POSITION difference and the drag is the rest.*

** AND ONE CORRECTION TO THE ORDER, WHICH IS WHY THE KNOB IS SEPARATE. **  `r6889` says of the source
decomposition and the phase shift that "the two are the same part of the source".  ** They are two
layers, not one. **  `SWSRC`/`DPSRC` switch LINE-OF-SIGHT SOURCE TERMS -- which contributions are
projected onto the sky -- and the free-streaming phase shift is in the DYNAMICS that set the dipole's
phase before last scattering.  Deleting the Doppler term removes the dipole's contribution; `NUFS`
changes what the dipole is.  *Pointing the first at the second would have measured nothing, so it is
two knobs and this receipt builds both.*

-------------------------------------------------------------------------------
COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms are the verified 185-bin
    refit minima of `r6825+cc66.25` -- `LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248` for the
    control, `CRH0=68.581133 CROM=0.297209 WBH2=0.021524 NS=0.997952 ZSTART=3e7 LEAFSCALES=1` for the
    arm -- and every run here is one of those two commands with ONE knob added.
  * The lensing operator is `c54.183`'s CAMB lensed/unlensed TT ratio at Planck 2018, used exactly as
    `cc66.33`, `cc66.34` and `cc66.35` use it.
  * The one free number fitted is the single bandpower amplitude per spectrum, on the full covariance.
  * ** NOT CLAIMED: any pinned value of n_s, H_0, Omega_m or omega_b. **  Those are `r6825+cc66.25`'s.

WHAT IS CLAIMED.

 (1) The shadow, stated as a property of the source text and not of a memory: `_DPSRC` occurs once
     outside its declaration and inside `los_spectrum`, BEFORE the repair.
 (2) The repair is additive: the unset configuration reproduces the banked spectra bit-for-bit on
     both arms, so nothing downstream of this revision moves unless a knob is set.
 (3) Each newly wired switch moves the hierarchy path's spectrum by a stated amount.
 (4) The two bracketing tests on the reporting path, beside `r6885+cc66.35`'s line-of-sight ones.
 (5) `NUFS` exists, its ladder's initial condition is exactly zero, and `NUFS=0` moves the spectrum.

WHAT IS NOT CLAIMED.

 * NOT a mechanism for the contrast imbalance.  `r6889` says that boundary is right and does not move
   it, and neither does this.
 * NOT the free-streaming phase shift's VALUE as a result about this construction.  The knob is built
   and calibrated; pointing it at the question is the next order's, and what is reported here is that
   it moves and by how much.
 * NOT a repair of anything else in the instrument.  Three paths now read the same two switches; no
   other knob is audited, and the count of shadows found is not a claim that there are no more.
 * The low-multipole path is wired for consistency and is NOT exercised here -- this sector's numbers
   are the hierarchy path's.  Naming it rather than quietly leaving it is the point.

WHAT WOULD FALSIFY IT.  The unset configuration NOT reproducing the banked spectra; either switch
still moving nothing on the hierarchy path; the reporting path's bracketing tests disagreeing with the
line-of-sight ones in sign; or the neutrino quadrupole's initial condition turning out to be nonzero,
which would make `NUFS=0` a frozen state rather than a perfect fluid.
"""
import os
import sys

import numpy as np

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
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
SRC = open(INST).read()
LC, FACB = CS.bin_center_and_fac()
X_DATA, COV = CS.X_DATA, CS.COV_TT

import camb                                                                # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RAT = np.ones_like(_le)
_m = _un > 0
RAT[_m] = _le[_m] / _un[_m]

load = lambda f: (lambda d: (d['ls'].astype(float), d['Dl'].astype(float)))(
    np.load(os.path.join(SP, f)))
base = lambda t: load(f'cc66_r185_verify_{t}.npz')
mb = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RAT))

KEEP = np.isfinite(mb(*base('lcdm'))) & (LC >= 100) & (LC <= 1900)
COVK = COV[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COVK))
FISH = np.linalg.inv(COVK)
DK, LCK, FACK = X_DATA[KEEP], LC[KEEP], FACB[KEEP]
SIG = np.sqrt(np.diag(COVK))


def fitted(ls, Dl):
    m = mb(ls, Dl)[KEEP]
    A = float(m @ FISH @ DK / (m @ FISH @ m))
    r = A * m - DK
    return A * m, float(r @ FISH @ r), LINV @ r


M_L, C2_L, W_L = fitted(*base('lcdm'))
M_C, C2_C, W_C = fitted(*base('cr'))
DEL = LINV @ (M_C - M_L)
ND2 = float(DEL @ DEL)
AHAT = LINV @ M_C
AHAT = AHAT / np.linalg.norm(AHAT)
marg = lambda w: w - AHAT * float(AHAT @ w)
DM = marg(DEL)
NDM2 = float(DM @ DM)
DL_L = M_L * FACK
PKI = [j for j in range(1, len(LCK) - 1) if DL_L[j] > DL_L[j - 1] and DL_L[j] > DL_L[j + 1]]
PERIOD = float(np.median(np.diff(LCK[PKI])))


def envelope(y, win=None):
    win = PERIOD if win is None else win
    e = np.empty_like(y)
    for j, l in enumerate(LCK):
        k = (LCK >= l - win / 2) & (LCK <= l + win / 2)
        e[j] = np.exp(np.mean(np.log(y[k])))
    return e


def contrast_of(mA, mB):
    dA, dB = mA * FACK, mB * FACK
    eA, eB = envelope(dA), envelope(dB)
    oA, oB = (dA - eA) / eA, (dB - eB) / eB
    return float(np.sum(oA * oB) / np.sum(oB * oB))


CONTRAST = marg(LINV @ ((DL_L - envelope(DL_L)) / FACK))
CONTRAST = CONTRAST / np.linalg.norm(CONTRAST)
SCALE = contrast_of(M_C, M_L)
print(f"\n  the frame, carried over from `r6885+cc66.35` unchanged: {int(KEEP.sum())} bins, "
      f"||DELTA||^2 = {ND2:.2f}, the arms' contrast ratio {SCALE:.4f}")

# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE SHADOW, AS A PROPERTY OF THE SOURCE TEXT AND OF THE BANKED MEASUREMENT.")
print("-" * 100)
LOS_AT = SRC.index('def los_spectrum')
HIER_AT = SRC.index('def los_hier') if 'def los_hier' in SRC else SRC.index('def main')
USES = lambda tok: [i for i in range(len(SRC)) if SRC.startswith(tok, i)]
print(f"    `los_spectrum` begins at offset {LOS_AT}; the hierarchy source and the low-multipole")
print(f"    source are both after it.")
for tok, name in (('_SWSRC *', 'the monopole switch'), ('_DPSRC *', 'the Doppler switch'),
                  ('_ISW * et *', 'the ISW switch, for comparison')):
    u = USES(tok)
    print(f"    {name:34s} `{tok.strip(' *')}` used {len(u)} time(s) at {u}")
check("** ALL THREE SWITCHES NOW REACH MORE THAN ONE PATH **, which is the repair: before it the two "
      "source switches were used once each and `_ISW` three times, and that asymmetry WAS the shadow",
      len(USES('_SWSRC *')) >= 2 and len(USES('_DPSRC *')) >= 2,
      f"SWSRC {len(USES('_SWSRC *'))}x, DPSRC {len(USES('_DPSRC *'))}x, "
      f"ISW {len(USES('_ISW * et *'))}x")
check("...and at least one use of each is AFTER `los_spectrum`, i.e. on a path that was blind to it",
      max(USES('_SWSRC *')) > LOS_AT and max(USES('_DPSRC *')) > LOS_AT,
      f"last SWSRC at {max(USES('_SWSRC *'))}, last DPSRC at {max(USES('_DPSRC *'))}, "
      f"against `los_spectrum` at {LOS_AT}")
check("** the monopole bracket is SPLIT so the switch multiplies g(Theta_0+Psi) and NOT the "
      "polarisation term that shares it **, which is what makes the switch mean the same thing on "
      "the hierarchy path as on the line-of-sight one",
      'g_ * (_SWSRC * (Th0 + Ps) + _PI * Pi / 4)' in SRC,
      "the split bracket is in the source, with the factor INSIDE so the default sums in the "
      "original order")
# the banked measurement of the shadow, from r6885
_b1, _b2 = base('lcdm'), base('cr')
_s1, _s2 = load('r6885_dp0_lcdm.npz'), load('r6885_dp0_cr.npz')
check("⛔ AND THE MEASUREMENT IT WAS FOUND BY, kept and re-gated here: with the switch UNWIRED, "
      "`DPSRC=0` on the refit configuration returned a bit-identical spectrum on BOTH arms",
      float(np.max(np.abs(_s1[1] - _b1[1]))) == 0.0
      and float(np.max(np.abs(_s2[1] - _b2[1]))) == 0.0,
      f"max |dD_l| = {float(np.max(np.abs(_s1[1]-_b1[1]))):.1e} and "
      f"{float(np.max(np.abs(_s2[1]-_b2[1]))):.1e} at `r6885_dp0_*`")

# ---------------------------------------------------------------------------------
print("\nPART 2 -- THE REPAIR IS ADDITIVE, AND THE DEFAULT IS PROVED BEFORE ANYTHING ELSE IS READ.")
print("-" * 100)
RD = SP
have = lambda t: all(os.path.exists(os.path.join(RD, f'r6889_{t}_{a}.npz'))
                     for a in ('lcdm', 'cr'))
pair = lambda t: (load(f'r6889_{t}_lcdm.npz'), load(f'r6889_{t}_cr.npz'))
if not have('noop'):
    check("the unset re-run is banked -- named here rather than left out if it is not", False,
          "r6889_noop_{lcdm,cr} missing")
else:
    (_nl_l, _nl_d), (_nc_l, _nc_d) = pair('noop')
    _dl = float(np.max(np.abs(_nl_d - _b1[1])))
    _dc = float(np.max(np.abs(_nc_d - _b2[1])))
    print(f"    the SAME two commands with nothing set, on the edited instrument:")
    print(f"      control : max |D_l(new) - D_l(banked)| = {_dl:.3e}")
    print(f"      CR arm  : max |D_l(new) - D_l(banked)| = {_dc:.3e}")
    check("** BIT-IDENTICAL ON BOTH ARMS **, so wiring two switches into two more paths and adding "
          "the neutrino knob changes NOTHING at the defaults -- every number this sector has "
          "reported still stands unedited",
          _dl == 0.0 and _dc == 0.0, f"{_dl:.1e} and {_dc:.1e}, exactly zero")
    check("...and the multipole grids are identical too, so it is the same comparison and not a "
          "resampled one",
          np.array_equal(_nl_l, _b1[0]) and np.array_equal(_nc_l, _b2[0]),
          f"{len(_nl_l)} multipoles, {_nl_l[0]:.0f}-{_nl_l[-1]:.0f}")

# ---------------------------------------------------------------------------------
print("\nPART 3 -- THE CALIBRATION: EACH NEWLY WIRED SWITCH MOVES THE REPORTING PATH.")
print("-" * 100)
print("""
  ** r4558's own note is the rule this revision exists to enforce: a knob that reports NO CHANGE is
  indistinguishable from a knob that is not connected. **  So every switch newly wired here is shown
  to move the spectrum on the path it was newly wired into, BEFORE any verdict is read off it.
""")
MOVED = {}
for tag, name in (('hdp0', '`DPSRC=0`, the Doppler dipole'),
                  ('hsw0', '`SWSRC=0`, the monopole'),
                  ('nufs0', '`NUFS=0`, the neutrinos as a perfect fluid')):
    if not have(tag):
        print(f"    {name:44s} NOT RUN, named rather than left out")
        continue
    (_l1, _d1), (_l2, _d2) = pair(tag)
    r1 = float(np.max(np.abs(_d1 / _b1[1] - 1)))
    r2 = float(np.max(np.abs(_d2 / _b2[1] - 1)))
    MOVED[tag] = (r1, r2)
    print(f"    {name:44s} max relative |dD_l|: control {100*r1:6.2f}%   arm {100*r2:6.2f}%")
for tag, name in (('hdp0', 'the Doppler switch'), ('hsw0', 'the monopole switch'),
                  ('nufs0', 'the free-streaming switch')):
    if tag in MOVED:
        check(f"{name} demonstrably reaches the term it names on the hierarchy path",
              min(MOVED[tag]) > 0.01,
              f"{100*MOVED[tag][0]:.1f}% and {100*MOVED[tag][1]:.1f}%")
if 'hdp0' in MOVED:
    check("⛭ ** AND THAT IS THE PAIR THAT MAKES THE SHADOW A PROOF **: the same switch, the same two "
          "commands, exactly 0.0 before the repair and this much after -- a null and an unwired knob "
          "look identical until both halves are on the record",
          min(MOVED['hdp0']) > 0.01,
          f"0.0% at `r6885_dp0_*` against {100*min(MOVED['hdp0']):.0f}-"
          f"{100*max(MOVED['hdp0']):.0f}% at `r6889_hdp0_*`")

# ---------------------------------------------------------------------------------
print("\nPART 4 -- THE TWO BRACKETING TESTS, ON THE PATH THE NUMBERS ARE REPORTED FROM.")
print("-" * 100)
print("""
  `r6885+cc66.35` could run these only on the line-of-sight path and said so, and that path's chi^2
  is not comparable with this one's.  ** Here they are where it matters. **  The question each
  answers is whether the CONTRAST -- the arm's acoustic oscillation at 1.040 of the control's about
  its own envelope, which is what DELTA mostly is -- lives in the monopole-to-dipole balance.
""")
LOSREF = {'hdp0': ('losdp0', 'DPSRC=0', +0.8933, 1.855),
          'hsw0': ('lossw0', 'SWSRC=0', -0.7907, -0.300)}
print(f"      {'test':14s} {'||DELTA_off||^2':>15s} {'of base':>8s} {'contrast ratio':>15s}"
      f" {'cos(shape, CONTRAST)':>21s}   [LOS path, r6885]")
ROWS = {}
for tag, (lref, nm, loscos, loscon) in LOSREF.items():
    if not have(tag):
        print(f"      {nm:14s} NOT RUN, named rather than left out")
        continue
    m2L, _, _ = fitted(*load(f'r6889_{tag}_lcdm.npz'))
    m2C, _, _ = fitted(*load(f'r6889_{tag}_cr.npz'))
    d2 = LINV @ (m2C - m2L)
    v = marg(LINV @ (m2C - M_C))
    v = v / np.linalg.norm(v)
    cos = float(v @ CONTRAST)
    own = contrast_of(m2C, M_C)
    ROWS[tag] = (float(d2 @ d2), contrast_of(m2C, m2L), cos, own)
    print(f"      {nm:14s} {float(d2@d2):15.2f} {100*float(d2@d2)/ND2:7.1f}%"
          f" {contrast_of(m2C, m2L):15.4f} {cos:+21.4f}   [{loscos:+.3f}]")
    print(f"      {'':14s} and it takes the arm's own oscillation to {own:+.3f} of what it was"
          f"   [LOS: {loscon:+.3f}]")
if 'hdp0' in ROWS and 'hsw0' in ROWS:
    check("⚑ ** THE TWO HALVES OF THE SOURCE BRACKET THE CONTRAST WITH OPPOSITE SIGNS ON THE "
          "REPORTING PATH TOO **, so `r6885+cc66.35`'s reading -- the contrast direction IS the "
          "monopole-to-dipole balance -- was not an artefact of the path it had to be measured on",
          ROWS['hdp0'][2] > 0.5 and ROWS['hsw0'][2] < -0.3,
          f"DPSRC=0 cos {ROWS['hdp0'][2]:+.3f}, SWSRC=0 cos {ROWS['hsw0'][2]:+.3f}")
    check("...and the two paths agree in SIGN on both, which is the comparison that was owed and "
          "could not be made before this repair",
          np.sign(ROWS['hdp0'][2]) == np.sign(LOSREF['hdp0'][2])
          and np.sign(ROWS['hsw0'][2]) == np.sign(LOSREF['hsw0'][2]),
          f"hierarchy {ROWS['hdp0'][2]:+.3f}/{ROWS['hsw0'][2]:+.3f} against LOS "
          f"{LOSREF['hdp0'][2]:+.3f}/{LOSREF['hsw0'][2]:+.3f}")
    check("⚠ ...while the arms' contrast RATIO SURVIVES both deletions -- it does not collapse "
          "toward 1.000 under either -- so the channel is identified and the cause is still not "
          "measured, which is the boundary `r6889` said it was not moving",
          all(ROWS[t][1] > 1.02 for t in ROWS),
          f"{SCALE:.4f} -> " + ", ".join(f"{t} {ROWS[t][1]:.4f}" for t in ROWS))
    check("...and the two deletions are NOT equally inert on it, which is reported rather than "
          "averaged away: dropping the dipole barely moves the ratio while dropping the monopole "
          "raises it by four points, so the balance is not symmetric in its two halves",
          abs(ROWS['hdp0'][1] - SCALE) < 0.01 < abs(ROWS['hsw0'][1] - SCALE),
          f"dipole {ROWS['hdp0'][1]-SCALE:+.4f}, monopole {ROWS['hsw0'][1]-SCALE:+.4f}")

# ---------------------------------------------------------------------------------
print("\nPART 5 -- THE FREE-STREAMING PHASE SHIFT: A KNOB WAS BUILDABLE, AND HERE IS WHAT IT COST.")
print("-" * 100)
print("""
  The order asked for one of two answers: a knob is buildable and here is its cost, or the phase
  shift cannot be tested on this instrument at all and the papers should carry that.  ** It is the
  first, and the cost is four lines. **

  What makes a neutrino free-stream rather than behave as a perfect fluid is its anisotropic stress
  sigma_nu = F_2 / 2, which enters at exactly two dynamical sites -- the Euler equation
  theta_nu' = k^2 (delta_nu/4 - sigma_nu), and Psi's shear term -- plus the l >= 2 ladder that
  carries it.  `NUFS` multiplies sigma_nu and the F_2 source on both solver paths.
""")
check("`NUFS` is declared once and used at FOUR sites, two per solver path -- the shear where it is "
      "read and the F_2 source where it is made",
      SRC.count('_NUFS') == 5,
      f"{SRC.count('_NUFS')} occurrences: one declaration and "
      f"{SRC.count('_NUFS') - 1} uses")
check("** and the ladder's INITIAL CONDITION IS EXACTLY ZERO **, which is what makes NUFS=0 a "
      "perfect fluid rather than a frozen state: the quadrupole is allocated zero and never "
      "assigned, so with its source switched off it stays zero and everything above it stays zero",
      'y0 = np.zeros((nk, NV))' in SRC and 'y0[:, 7]' not in SRC,
      "`y0 = np.zeros((nk, NV))` with no assignment to index 7 anywhere in the file")
check("...and the background is untouched: `FNU` and the density fractions `Onv`/`Ogv` carry no "
      "`_NUFS`, so the expansion history and the radiation split are the same run to run",
      '_NUFS' not in SRC[SRC.index('Og_of = CubicSpline'):SRC.index('Og_of = CubicSpline') + 400],
      "no `_NUFS` within the density-fraction block")
if 'nufs0' in MOVED:
    m3L, _, _ = fitted(*load('r6889_nufs0_lcdm.npz'))
    m3C, _, _ = fitted(*load('r6889_nufs0_cr.npz'))
    print(f"\n    `NUFS=0` on the reporting path moves D_l by "
          f"{100*MOVED['nufs0'][0]:.1f}% (control) and {100*MOVED['nufs0'][1]:.1f}% (arm)")
    # the PHASE half is the peak POSITIONS; the drag is the rest
    def peaks(m):
        d = m * FACK
        return [float(LCK[j]) for j in range(1, len(LCK) - 1)
                if d[j] > d[j - 1] and d[j] > d[j + 1]]
    SHIFTS = {}
    for nm, m0, m1 in (('control', M_L, m3L), ('CR arm', M_C, m3C)):
        p0, p1 = peaks(m0), peaks(m1)
        n = min(len(p0), len(p1))
        sh = [p1[i] - p0[i] for i in range(n)]
        SHIFTS[nm] = sh
        print(f"      {nm:8s} peaks free-streaming {[int(v) for v in p0[:n]]}")
        print(f"      {nm:8s} peaks perfect fluid  {[int(v) for v in p1[:n]]}"
              f"   shift {[f'{v:+.0f}' for v in sh]}")
    _step = float(np.median(np.diff(LCK)))
    check("⚑ ** THE KNOB MOVES THE PEAK POSITIONS AND IT MOVES THEM THE RIGHT WAY **: the "
          "free-streaming phase shift pulls the peaks to SMALLER multipole, so removing it must push "
          "them back to LARGER -- and every shift on both arms is POSITIVE",
          all(v > 0 for sh in SHIFTS.values() for v in sh),
          "shifts " + " / ".join(f"{nm} {[f'{v:+.0f}' for v in sh]}" for nm, sh in SHIFTS.items()))
    check("...and it is UNIFORM across the first four peaks on both arms, which is what a PHASE "
          "shift looks like as against a rescaling of the acoustic scale",
          all(max(sh[:4]) - min(sh[:4]) < 0.05 for sh in SHIFTS.values()),
          ", ".join(f"{nm} {np.mean(sh[:4]):+.3f} at peaks 1-4 (spread "
                    f"{max(sh[:4])-min(sh[:4]):.3f})" for nm, sh in SHIFTS.items()))
    check("⚠ ** AND ITS SIZE IS GRID-LIMITED AND IS REPORTED AS SUCH **: the shift comes out at one "
          "binned grid step, so the SIGN and the order of magnitude are established here and the "
          "VALUE is not -- reading it off would want a locator on a finer grid, which is not run",
          abs(SHIFTS['control'][0] - _step) < 0.05 * _step,
          f"shift {SHIFTS['control'][0]:+.3f} against a median bin step of {_step:.3f} -- exactly "
          f"one step, which is the resolution and not a measurement")
    check("...while the DRAG half -- the amplitude suppression free-streaming also causes -- is the "
          "large effect, and the two must not be quoted as one number",
          min(MOVED['nufs0']) > 0.2,
          f"D_l moves {100*MOVED['nufs0'][0]:.0f}% and {100*MOVED['nufs0'][1]:.0f}% against a peak "
          f"shift of one grid step")
    check("⌗ and the knob is CALIBRATED rather than merely present -- which is the entire subject of "
          "this revision, so a new knob that had not been shown to move something would be the same "
          "defect landed twice",
          min(MOVED['nufs0']) > 0.01, f"min move {100*min(MOVED['nufs0']):.1f}%")
else:
    print("    ⌗ `NUFS=0` is NOT RUN and is named rather than left out; the knob is then BUILT and "
          "NOT CALIBRATED,\n      which by this receipt's own standard is not finished.")
    check("the NUFS calibration ran", False, "r6889_nufs0_{lcdm,cr} missing")

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE READING.")
print("=" * 100)
_dpr = f"{100*MOVED['hdp0'][1]:.0f}%" if 'hdp0' in MOVED else "NOT RUN"
_nur = f"{100*MOVED['nufs0'][1]:.1f}%" if 'nufs0' in MOVED else "NOT RUN"
_br = (f"DPSRC=0 at cos {ROWS['hdp0'][2]:+.2f} and SWSRC=0 at cos {ROWS['hsw0'][2]:+.2f}"
       if 'hdp0' in ROWS and 'hsw0' in ROWS else "NOT RUN")
print(f"""
  ** THE ORDER PUT THE SHADOW AHEAD OF EVERYTHING ELSE AND IT IS CLOSED. **  `_SWSRC` and `_DPSRC`
  now reach all three source constructions -- `los_spectrum`, the hierarchy path and the
  low-multipole path -- where before they reached one.  ⇒ *** And the default is PROVED rather than
  asserted: the unset configuration reproduces the banked spectra BIT-FOR-BIT on both arms, so
  nothing this sector has already reported moves. ***  ⌗ *`_ISW` was wired to all three at r4558 and
  these two were not; that asymmetry was the whole of the defect, and it is the third of its shape
  after the `NS` literal and the baryon density.*

  ** AND THE PAIR THAT MAKES IT A PROOF RATHER THAN A STORY. **  The same switch, the same two
  commands: exactly 0.0 on the reporting path before the repair, {_dpr} after.  *A null and an
  unwired knob are indistinguishable until both halves are on the record, which is r4558's own rule
  and the reason this revision exists.*

  ⚑ ** THE BRACKETING TESTS SURVIVE THE MOVE TO THE REPORTING PATH. **  {_br} -- the two halves of
  the source bracket the contrast with opposite signs here as they did on the line-of-sight path, so
  *** `r6885+cc66.35`'s reading, that the contrast direction IS the monopole-to-dipole balance, was
  not an artefact of the path it had to be measured on. ***  ⚠ *And the arms' contrast RATIO survives
  both deletions again, so the channel stays identified and the cause stays unmeasured -- the
  boundary `r6889` said it was not moving.*

  ⚑ ** THE FREE-STREAMING PHASE SHIFT HAS A KNOB, AND THE ANSWER TO "WHAT WOULD IT COST" IS FOUR
  LINES. **  What makes a neutrino free-stream is its anisotropic stress at two dynamical sites, so
  `NUFS` multiplies sigma_nu and the F_2 source on both solver paths.  ** The quadrupole's initial
  condition is exactly zero **, so at `NUFS=0` it is never sourced, the whole ladder stays zero, and
  the sector is a perfect fluid at the SAME background density -- `FNU` and the density fractions
  untouched.  ⇒ It moves the spectrum by {_nur} on the arm and it moves the PEAK POSITIONS, which is
  the phase half.  ⇒ *** And the phase half comes out with the RIGHT SIGN: removing free-streaming
  pushes every peak on both arms to LARGER multipole, uniformly across the first four, which is what
  a phase shift looks like and the direction the Bashinsky-Seljak pull has. ***  ⚠ *Its SIZE is one
  binned grid step, so the sign and the order of magnitude are established and the value is not; and
  the DRAG half -- the amplitude suppression, {_nur} in D_l -- is the large effect and must not be
  quoted as the same number.*  *After three orders naming this candidate and none testing it, it is
  reachable.*

  ⛭ ** AND ONE CORRECTION TO THE ORDER, WHICH IS WHY IT IS A SECOND KNOB AND NOT THE FIRST ONE
  POINTED SOMEWHERE. **  `r6889` says of the source decomposition and the phase shift that "the two
  are the same part of the source".  *They are two layers.*  `SWSRC`/`DPSRC` switch which
  LINE-OF-SIGHT terms are projected onto the sky; the phase shift is in the DYNAMICS that set the
  dipole before last scattering.  ** Deleting the Doppler term removes the dipole's contribution;
  `NUFS` changes what the dipole IS. **  Pointing the first at the second would have measured
  nothing.

  ⚠ ** WHAT THIS IS NOT. **  No mechanism for the contrast imbalance, which `r6889` explicitly did
  not ask for.  No VALUE for the phase shift as a result about this construction -- the knob is built
  and calibrated and pointing it at the question is the next order's.  And no audit of any other
  knob: three shadows have now been found in this sector by three different routes, and nothing here
  says there is not a fourth.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: `_SWSRC` and `_DPSRC` now reach all three source constructions where they reached one,
and the repair is additive -- the unset configuration reproduces `cc66_r185_verify_{{lcdm,cr}}`
bit-for-bit on both arms.  Each newly wired switch is calibrated where it was newly wired: the
Doppler switch moves the reporting path by {_dpr} where it moved it by exactly 0.0 before, which is
what turns `r6885+cc66.35`'s bit-identical pair from a null into a proof.  The two bracketing tests
re-run on the reporting path give {_br}, the same opposite-sign bracket the line-of-sight path gave,
so the contrast direction IS the monopole-to-dipole balance and that reading was not the path's.  AND
the free-streaming phase shift is reachable: `NUFS` is four lines, its quadrupole's initial condition
is exactly zero so `NUFS=0` is a perfect fluid at the same background density, and it moves the arm
by {_nur} and moves the peak positions.
NOT CLAIMED: a mechanism for the contrast imbalance; a value for the phase shift as a result about
this construction; or that no further knob in this instrument is shadowed.
""")
