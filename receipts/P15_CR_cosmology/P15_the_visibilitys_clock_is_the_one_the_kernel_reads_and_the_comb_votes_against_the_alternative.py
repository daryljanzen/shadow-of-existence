"""
P15_the_visibilitys_clock_is_the_one_the_kernel_reads_and_the_comb_votes_against_the_alternative
===============================================================================================

LEVEL: `r6925`'s order -- ** which clock is the visibility a density in, and does the rate rule
determine it? ** -- with the retained fraction and the COMB reported side by side and neither picked
over the other, as the order requires.  Both arms at their verified 185-bin refit minima.

** WHAT THE ORDER ASKED, AND WHAT COMES BACK. **

 ⛭⛭ (1) THE AUDIT TURNS UP SOMETHING THE ORDER DID NOT EXPECT: ** THE INSTRUMENT ALREADY ANSWERS
     THIS QUESTION TWICE, AND DIFFERENTLY. **  Every site where the optical depth or the visibility
     touches a rate is on the STACKING clock -- the recombination history solved against `Hphys`,
     `taup_of` built on `eg`'s conformal time, `tau` integrated over `_egrid`, `ETA_LS` and
     `ETA_LS_W` read off that grid.  ⛔ ** But `1/k_D^2` twenty lines below IS Jac-weighted under
     `LEAFSCALES`. **  ⇒ *So the DIFFUSION length -- a scale the plasma accumulates -- takes the leaf
     clock, and the OPTICAL DEPTH -- also accumulated by the plasma -- takes the stacking clock.*
     ** Two objects on the same side of the rate rule, given opposite clocks, with nothing in the
     instrument or the corpus stating the choice. **  *That is the gap the order named, already open
     in the code.*

 ⌗ (2) SO THE OTHER ASSIGNMENT IS NOT AN INVENTION, IT IS THE ONE THE INSTRUMENT ALREADY USES NEXT
     DOOR.  `VISLEAF=1` applies to `tau` exactly the weighting `1/k_D^2` applies to itself.  On the
     control it is BIT-IDENTICAL, because `Jac == 1` there by the rate identity; on the arm it moves
     the visibility peak from eta = 485.99 to 483.83, its FWHM from 43.591 to 43.952 Mpc, and r_D
     from 7.473 to 7.168.

 ⚑⚑ (3) ON THE GEOMETRY THE TWO ASSIGNMENTS AGREE, WHICH IS THE ORDER'S SECOND BRANCH.

         VISLEAF   d r_s/d chi control   arm      ratio     (12.8% lower means)
         0             0.454950       0.396733   0.8720      12.80% lower
         1             0.454950       0.396957   0.8725      12.75% lower

     ** d r_s/d chi moves by 0.06 per cent. **  ⇒ *And the reason is structural rather than lucky:
     `d r_s/d chi` is a RATIO of two accumulations across the SAME window, so re-weighting the
     window's measure re-weights numerator and denominator alike and the ratio is nearly invariant.*
     ⇒ ** So the visibility is not where the freedom is, and the 12.8 per cent is forced by the rule
     as stated -- which the order called the sharper and more falsifiable place. **

 ⛔ (4) BUT ON THE CONTRAST IT DOES MOVE, AND ON THE COMB IT MOVES THE WRONG WAY -- SO THE TWO
     DISAGREE AND THE ORDER SAYS TO REPORT THAT RATHER THAN PICK.
      * ** THE CONTRAST: the injection's retained ratio goes 1.0850 -> 1.0695 and its slope
        +0.02424 -> +0.01332 **, i.e. TOWARD the real source's 1.054 and +0.0139.  Read alone, that
        is the order's FIRST branch.
      * ⛔ ** THE COMB: the arm's first peak moves from ell = 220 to 228 and ell_1/ell_A from 0.7290
        to 0.7555, against the sky's 0.7312; P1/P2 goes 2.142 to 2.017. **  The control's comb is
        bit-identical both ways.  ⇒ *The assignment that improves the contrast breaks the peak
        positions, and the order's own guard is that an assignment which moves the comb is one the
        peak positions have already voted on.*
      * ⚠ ** AND THE CONTRAST NUMBER IS NOT EVEN CLEAN, FOR THE SAME REASON. **  Band by band under
        `VISLEAF=1` the ratio runs 1.039 / 1.011 / 1.073 / 1.109 / 1.048 / 1.190 / 1.015 --
        non-monotonic scatter -- against 1.029 / 1.055 / 1.070 / 1.088 / 1.107 / 1.100 / 1.146,
        smooth and monotonic, under the current one.  *Moving `eta_LS` moves `r_s(eta_LS)` and so
        moves the comb, and a band ratio of two oscillations no longer aligned in q picks up their
        phase mismatch.*  ⇒ ** That is `cc66.40`'s guard firing a third time, on the shape it was
        built for: the improvement in the fitted slope is partly the statistic reading a phase. **
     ⇒ *** So: the geometry says forced, the contrast says improvable, the comb says no, and the
     contrast's own band structure says its improvement is not to be trusted.  The comb is the only
     one of the three with an external referent, and it votes for the assignment the instrument
     already has. ***

 ⚑ (5) ⓶ AND THE SOURCE'S CANCELLATION IS HALF THE LEVEL AND NONE OF THE SLOPE, so the sector does
     NOT close into one account.  Pure geometry gives 1.0850 at +0.02424; the real source 1.0694 at
     +0.01167.  Multiplying the injection by `cc66.40`'s measured source deficit -- 0.9922, and FLAT
     in q at a slope of -0.00106 -- gives 1.0766 at +0.02296.  ⇒ ** That closes 54 per cent of the
     level gap and 10 per cent of the slope gap. **  *So the four trough-filling channels account
     for about half the level difference and essentially none of the slope difference: the order's
     conditional is half satisfied and the closure it hoped for does not arrive.  What flattens the
     slope is the real source's own eta-dependence across the visibility, which is precisely what
     the injection replaced -- named, not measured here.*

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The audit, site by site with its rate: five stacking-clock sites for tau and g, against
     `1/k_D^2` Jac-weighted under `LEAFSCALES` -- two plasma-accumulated objects on opposite clocks.
 (2) `VISLEAF` is bit-identical when unset on both arms, AND bit-identical when SET on the control,
     which is the rate identity showing in a second place.
 (3) d r_s/d chi across the FWHM under both assignments: 0.396733 against 0.396957 on the arm, the
     control unchanged -- a 0.06 per cent move, with the structural reason stated.
 (4) The injection's retained ratio and q-slope under both, with the band-by-band values that show
     the `VISLEAF=1` slope is contaminated by the comb shift.
 (5) The comb under both: the arm's first four peaks, ell_1/ell_A and P1/P2, against the sky's
     0.7312; and the control bit-identical.
 (6) The source deficit closes 54 per cent of the level gap and 10 per cent of the slope gap.

WHAT IS NOT CLAIMED.

 * NOT that the two-rate assignment is right, which is the row's question now and not this order's.
 * NOT that `VISLEAF=1` is wrong as physics.  ** What is measured is that it moves the comb away
   from the sky while moving the contrast toward the real source, and that its contrast improvement
   is partly a phase artefact. **  Which of the two clocks the optical depth SHOULD be a density in
   is not settled here -- only that the instrument's current choice is the one the peak positions
   support and that the rule as stated does not determine it.
 * NOT that the 0.06 per cent invariance of d r_s/d chi settles the row.  It says the visibility is
   not where the freedom is; the freedom is in the rule's assignment of r_s itself.
 * NOT a mechanism beyond `cc66.42`'s, and nothing here touches `prop:flat`.
 * NOT that the injected runs are spectra of the model.  The `injvl` arrays are the projection's
   transfer of a known input; only the `combvl` arrays are spectra, and they are labelled apart.
 * ⚠ NOT that this receipt's first launcher worked.  It dropped its extra environment through a
   positional-argument bug and thirty-six slices ran as plain `VISLEAF=0` spectra, reporting nothing
   wrong and reproducing the banked spectra -- which is the shape that gets banked as an answer.  The
   episode is in the launcher's own comment and the fix is a smoke test that greps the log for the
   marker the switch must print before the set goes out.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima.  Nothing here re-fits and nothing here moves.
  * `spectra/r6925_visleaf_{lcdm,cr}.npz` (the injection and the real spectrum under `VISLEAF=1`),
    `r6925_geometry.npz` (both assignments, per arm), `r6925_noop.npz` (the two gates).
  * The `VISLEAF=0` side is `r6919+cc66.42`'s and `r6911+cc66.40`'s banks, and the comb's
    `VISLEAF=0` side is `cc66_r185_verify_*` -- read with the SAME statistic, abscissa and window.
  * NOTHING IS FITTED except the straight lines through the band ratios, whose scatter is reported.
"""
import os

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
SRC = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')).read()
NEED = ('r6925_visleaf_lcdm.npz', 'r6925_visleaf_cr.npz', 'r6925_geometry.npz', 'r6925_noop.npz',
        'r6919_injected_lcdm.npz', 'r6919_injected_cr.npz', 'r6911_source_lcdm.npz',
        'r6911_source_cr.npz', 'cc66_r185_verify_lcdm.npz', 'cc66_r185_verify_cr.npz',
        'r6893_switch_screen_lcdm.npz', 'r6893_switch_screen_cr.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK YET, so nothing is read and this receipt")
    print("     FAILS rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

VL = {t: np.load(os.path.join(SP, f'r6925_visleaf_{t}.npz')) for t in ('lcdm', 'cr')}
IJ = {t: np.load(os.path.join(SP, f'r6919_injected_{t}.npz')) for t in ('lcdm', 'cr')}
SO = {t: np.load(os.path.join(SP, f'r6911_source_{t}.npz')) for t in ('lcdm', 'cr')}
VR = {t: np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')) for t in ('lcdm', 'cr')}
GE = np.load(os.path.join(SP, 'r6925_geometry.npz'))
NOOP = np.load(os.path.join(SP, 'r6925_noop.npz'))
g = lambda k, a, v: float(GE[f'{k}__{a}_{v}'])


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running arithmetic mean -- the statistic is that receipt's, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


ED = np.arange(0.85, 5.76, 0.7)
CTR = np.array([(a + b) / 2 for a, b in zip(ED[:-1], ED[1:])])


def bands(Q, O):
    out = []
    for a, b in zip(ED[:-1], ED[1:]):
        x = np.linspace(a, b, 400)
        out.append(np.interp(x, Q['cr'], O['cr']).std() / np.interp(x, Q['lcdm'], O['lcdm']).std())
    return np.array(out)


# ===================================================================================================
print("\nPART 1 -- THE AUDIT: EVERY PLACE THE OPTICAL DEPTH OR THE VISIBILITY TOUCHES A RATE.")
print("-" * 100)
SITES = [("the recombination history's expansion rate", "xe_history(lambda z: Hphys(", 'stacking'),
         ("tau' = n_e sigma_T a, built on `eg`'s conformal time", "taup_of = CubicSpline(_ea,", 'stacking'),
         ("the tau integration's measure", "_tau = np.concatenate([[0.0], np.cumsum(", 'stacking*'),
         ("the visibility and its peak/FWHM, read off `_egrid`", "vis_of = CubicSpline(_egrid,", 'stacking'),
         ("1/k_D^2's measure", "_dE = _dE * 0.5 * (np.asarray(Jac_of(", 'LEAF under LEAFSCALES')]
for nm, needle, clock in SITES:
    check(f"site found and its clock read from the source: {nm} -- {clock}",
          SRC.count(needle) == 1, f"`{needle[:44]}...`")
check("⛔ ** AND THE TWO ARE ON OPPOSITE CLOCKS. **  `1/k_D^2`'s measure is Jac-weighted under "
      "`LEAFSCALES` and `tau`'s is not, so the diffusion length takes the LEAF clock and the optical "
      "depth the STACKING clock -- two objects on the same side of the rate rule, with nothing "
      "stating the choice.  *That is the gap `r6925` named, already open in the code.*",
      SRC.count('_dE = _dE * 0.5 * (np.asarray(Jac_of(') == 1
      and SRC.count('_dTau = _dTau * 0.5 * (np.asarray(Jac_of(') == 1
      # ⌗ `r6929+cc66.44` made `VISLEAF` a FRACTION -- f=0 the stacking clock, f=1 the leaf's -- so
      #   this gate reads the two lines that replaced the flag's single read.  ** The substance it
      #   asserts is unchanged: `1/k_D^2`'s measure is Jac-weighted unconditionally under
      #   `LEAFSCALES` and `tau`'s only under `VISLEAF`, and f == 1 takes the expression above
      #   UNCHANGED so this receipt's own runs are still the code's endpoint, bit for bit. **
      and SRC.count("_VISLF = float(os.environ.get('VISLEAF', '0'))") == 1
      and SRC.count('_VISL = _VISLF != 0.0') == 1,
      "`1/k_D^2` Jac-weighted unconditionally under LEAFSCALES; `tau` only under `VISLEAF`")
for t in ('lcdm', 'cr'):
    b = np.load(os.path.join(SP, f'r6893_switch_screen_{t}.npz'))
    check(f"[{t}] `VISLEAF` UNSET IS BIT-IDENTICAL against the banked base",
          np.array_equal(NOOP[f'Dl__noop_{t}'], b['Dl__base']),
          f"max|dD_l| = {float(np.max(np.abs(NOOP[f'Dl__noop_{t}'] - b['Dl__base']))):.3e}")
check("⚑ and `VISLEAF=1` on the CONTROL is bit-identical TOO -- the rate identity showing in a "
      "second place, and the one-sided nature of the whole finding in one result",
      np.array_equal(NOOP['Dl__visl_lcdm'], NOOP['Dl__noop_lcdm']),
      f"max|dD_l| = {float(np.max(np.abs(NOOP['Dl__visl_lcdm'] - NOOP['Dl__noop_lcdm']))):.3e}")

# ===================================================================================================
print("\nPART 2 -- ⓵ THE GEOMETRY UNDER BOTH ASSIGNMENTS.  THIS IS THE ORDER'S SECOND BRANCH.")
print("-" * 100)
print(f"    {'VISLEAF':8s} {'arm eta_LS':>11s} {'arm FWHM':>10s} {'arm r_D':>9s} "
      f"{'d r_s/d chi ctl':>16s} {'arm':>10s} {'ratio':>8s}")
for v in ('0', '1'):
    print(f"    {v:8s} {g('eta_ls','cr',v):11.2f} {g('fwhm','cr',v):10.3f} {g('rD','cr',v):9.3f} "
          f"{g('cs','lcdm',v):16.6f} {g('cs','cr',v):10.6f} "
          f"{g('cs','cr',v)/g('cs','lcdm',v):8.4f}")
_r0 = g('cs', 'cr', '0') / g('cs', 'lcdm', '0')
_r1 = g('cs', 'cr', '1') / g('cs', 'lcdm', '1')
print(f"    ⇒ 12.8 per cent lower becomes {100*(1-_r1):.2f}: a move of "
      f"{100*abs(_r1-_r0)/_r0:.2f} per cent in the ratio")
check("⚑⚑ ** ON THE GEOMETRY THE TWO ASSIGNMENTS AGREE. **  `d r_s/d chi` is a RATIO of two "
      "accumulations across the SAME window, so re-weighting that window's measure re-weights "
      "numerator and denominator alike -- the invariance is structural, not lucky.  ⇒ The visibility "
      "is NOT where the freedom is, and the 12.8 per cent is forced by the rule as stated",
      abs(_r1 - _r0) / _r0 < 0.005,
      f"{_r0:.6f} against {_r1:.6f}, {100*abs(_r1-_r0)/_r0:.2f} per cent apart")
check("...and the control's geometry does not move at all, so every number here is the arm's alone",
      abs(g('cs', 'lcdm', '1') - g('cs', 'lcdm', '0')) < 1e-12,
      f"{g('cs','lcdm','0'):.6f} both ways")
check("⌗ but the switch is NOT inert on the arm -- the visibility peak, its width and r_D all move, "
      "so this is a connected knob reporting a near-null and not `r4558`'s unwired one",
      abs(g('eta_ls', 'cr', '1') - g('eta_ls', 'cr', '0')) > 1.0
      and abs(g('rD', 'cr', '1') / g('rD', 'cr', '0') - 1) > 0.02,
      f"eta_LS {g('eta_ls','cr','0'):.2f} -> {g('eta_ls','cr','1'):.2f}, "
      f"r_D {g('rD','cr','0'):.3f} -> {g('rD','cr','1'):.3f} "
      f"({100*(g('rD','cr','1')/g('rD','cr','0')-1):+.1f}%)")

# ===================================================================================================
print("\nPART 3 -- THE CONTRAST AND THE COMB, SIDE BY SIDE, NEITHER PICKED OVER THE OTHER.")
print("-" * 100)
Q0 = {t: IJ[t]['ls__sweepown'].astype(float) / float(IJ[t]['l_A__sweepown']) for t in IJ}
O0 = {t: osc(Q0[t], IJ[t]['Dl__sweepown']) for t in IJ}
Q1 = {t: VL[t]['ls__injvl'].astype(float) / float(VL[t]['l_A__injvl']) for t in VL}
O1 = {t: osc(Q1[t], VL[t]['Dl__injvl']) for t in VL}
Y0, Y1 = bands(Q0, O0), bands(Q1, O1)
S0, I0 = np.polyfit(CTR, Y0, 1)
S1, I1 = np.polyfit(CTR, Y1, 1)
print("  (a) THE CONTRAST -- the injection's retained ratio, band by band and fitted")
print(f"      {'q band':22s} " + " ".join(f"{v:6.2f}" for v in CTR))
print(f"      {'VISLEAF=0 (cc66.42)':22s} " + " ".join(f"{v:6.3f}" for v in Y0))
print(f"      {'VISLEAF=1 (the other)':22s} " + " ".join(f"{v:6.3f}" for v in Y1))
print(f"      VISLEAF=0: mean {Y0.mean():.4f}  slope {S0:+.5f}  residual rms "
      f"{np.std(Y0 - np.polyval([S0, I0], CTR)):.4f}")
print(f"      VISLEAF=1: mean {Y1.mean():.4f}  slope {S1:+.5f}  residual rms "
      f"{np.std(Y1 - np.polyval([S1, I1], CTR)):.4f}")
print(f"      the real source (cc66.41/42): mean 1.0694  slope +0.01167")
check("⌗ read ALONE the other assignment moves the contrast TOWARD the real source -- which is the "
      "order's FIRST branch, and is why it cannot be dismissed on the geometry alone",
      Y1.mean() < Y0.mean() and S1 < S0,
      f"mean {Y0.mean():.4f} -> {Y1.mean():.4f}, slope {S0:+.5f} -> {S1:+.5f}, against the real "
      f"1.0694 / +0.01167")
check("⚠ ** BUT THE `VISLEAF=1` BAND STRUCTURE IS NON-MONOTONIC SCATTER where the current one is "
      "smooth, so that slope is contaminated. **  Moving `eta_LS` moves `r_s(eta_LS)` and so moves "
      "the comb, and a band ratio of two oscillations no longer aligned in q reads their phase "
      "mismatch -- `cc66.40`'s guard firing a third time on the shape it was built for",
      np.std(Y1 - np.polyval([S1, I1], CTR)) > 3 * np.std(Y0 - np.polyval([S0, I0], CTR)),
      f"residual rms {np.std(Y0 - np.polyval([S0,I0],CTR)):.4f} -> "
      f"{np.std(Y1 - np.polyval([S1,I1],CTR)):.4f}, a factor "
      f"{np.std(Y1-np.polyval([S1,I1],CTR))/np.std(Y0-np.polyval([S0,I0],CTR)):.1f}")

print("\n  (b) THE COMB -- which the order asks for beside the contrast, and which has an external referent")
SKY = 0.7312
COMB = {}
for t in ('lcdm', 'cr'):
    for v, ls, Dl, lA in (('0', VR[t]['ls'].astype(float), VR[t]['Dl'], float(VR[t]['l_A'])),
                          ('1', VL[t]['ls__combvl'].astype(float), VL[t]['Dl__combvl'],
                           float(VL[t]['l_A__combvl']))):
        pk = argrelextrema(Dl, np.greater, order=3)[0][:4]
        COMB[(t, v)] = dict(pk=[int(ls[q]) for q in pk], r=float(ls[pk[0]] / lA),
                            p12=float(Dl[pk[0]] / Dl[pk[1]]))
        print(f"      {t:5s} VISLEAF={v}  peaks at l = {str(COMB[(t,v)]['pk']):26s} "
              f"l_1/l_A = {COMB[(t,v)]['r']:.4f}   P1/P2 = {COMB[(t,v)]['p12']:.3f}")
print(f"      the sky: l_1/l_A = {SKY:.4f}")
check("⛔ ** THE COMB VOTES AGAINST THE OTHER ASSIGNMENT. **  The arm's first peak moves and its "
      "`l_1/l_A` moves AWAY from the sky, while the control's comb is bit-identical -- and the "
      "order's own guard is that an assignment which moves the comb is one the peak positions have "
      "already voted on",
      COMB[('cr', '1')]['pk'][0] != COMB[('cr', '0')]['pk'][0]
      and abs(COMB[('cr', '1')]['r'] - SKY) > abs(COMB[('cr', '0')]['r'] - SKY)
      and COMB[('lcdm', '1')]['pk'] == COMB[('lcdm', '0')]['pk'],
      f"the arm's l_1 {COMB[('cr','0')]['pk'][0]} -> {COMB[('cr','1')]['pk'][0]}, l_1/l_A "
      f"{COMB[('cr','0')]['r']:.4f} -> {COMB[('cr','1')]['r']:.4f} against the sky's {SKY:.4f}; "
      f"P1/P2 {COMB[('cr','0')]['p12']:.3f} -> {COMB[('cr','1')]['p12']:.3f}")
check("⇒ ** SO THE CONTRAST AND THE COMB DISAGREE, and this receipt says so rather than picking. **  "
      "The comb is the only one of the three readings with an external referent, and it supports the "
      "assignment the instrument already has",
      True,
      "geometry: forced; contrast: improvable but phase-contaminated; comb: against")

# ===================================================================================================
print("\nPART 4 -- ⓶ WHERE THE SOURCE'S PARTIAL CANCELLATION SITS.")
print("-" * 100)
QK = {t: SO[t]['k'] * float(SO[t]['r_s']) / np.pi for t in SO}
QR = {t: SO[t]['ls'].astype(float) / (np.pi * float(SO[t]['D_M']) / float(SO[t]['r_s'])) for t in SO}
O2 = {t: osc(QK[t], SO[t]['S_i'] ** 2) for t in SO}
O3 = {t: osc(QR[t], SO[t]['Dl']) for t in SO}
REAL, SRC_ = [], []
for a, b in zip(ED[:-1], ED[1:]):
    x = np.linspace(a, b, 400)
    REAL.append(np.interp(x, QR['cr'], O3['cr']).std() / np.interp(x, QK['cr'], O2['cr']).std()
                / (np.interp(x, QR['lcdm'], O3['lcdm']).std()
                   / np.interp(x, QK['lcdm'], O2['lcdm']).std()))
    A, B = np.interp(x, QK['cr'], O2['cr']), np.interp(x, QK['lcdm'], O2['lcdm'])
    SRC_.append(float(np.sum(A * B) / np.sum(B * B)))
REAL, SRC_ = np.array(REAL), np.array(SRC_)
PROD = Y0 * SRC_
SR, _ = np.polyfit(CTR, REAL, 1)
SS, _ = np.polyfit(CTR, SRC_, 1)
SX, _ = np.polyfit(CTR, PROD, 1)
print(f"      {'':22s} " + " ".join(f"{v:6.2f}" for v in CTR) + "     mean     slope")
for nm, y, sl in (('the injection', Y0, S0), ('x the source deficit', PROD, SX),
                  ('the real source', REAL, SR), ('the source deficit', SRC_, SS)):
    print(f"      {nm:22s} " + " ".join(f"{v:6.3f}" for v in y) + f"   {y.mean():7.4f}  {sl:+8.5f}")
_lev = (Y0.mean() - PROD.mean()) / (Y0.mean() - REAL.mean())
_slp = (S0 - SX) / (S0 - SR)
print(f"      ⇒ the source deficit closes {100*_lev:.0f} per cent of the level gap and "
      f"{100*_slp:.0f} per cent of the slope gap")
check("⚑ ** THE SOURCE DEFICIT IS HALF THE LEVEL AND NONE OF THE SLOPE, so the sector does NOT close "
      "into one account. **  `cc66.40`'s 0.992 is FLAT in q, so it cannot carry a slope difference "
      "however well it carries a level one -- the order's conditional is half satisfied",
      0.3 < _lev < 0.8 and _slp < 0.25 and abs(SS) < 0.003,
      f"level {100*_lev:.0f} per cent, slope {100*_slp:.0f} per cent, the deficit's own slope "
      f"{SS:+.5f}")
check("...so what flattens the slope is the real source's own eta-dependence across the visibility, "
      "which is exactly what the injection replaced -- NAMED and not measured here",
      abs(S0 - SR) > 3 * abs(S0 - SX),
      f"the injection {S0:+.5f} against the real {SR:+.5f}, and the deficit moves it only to "
      f"{SX:+.5f}")

# ===================================================================================================
print("\n" + "=" * 100)
print(f"""
WHAT `r6925` ASKED AND WHAT THE THREE READINGS SAY.

  ⛭⛭ THE AUDIT FOUND THE GAP ALREADY OPEN IN THE CODE.  Every site where `tau` or `g` touches a rate
  is on the STACKING clock -- the recombination history against `Hphys`, `tau'` on `eg`, `tau` over
  `_egrid`, `ETA_LS` and its FWHM off that grid.  ** But `1/k_D^2` IS Jac-weighted under
  `LEAFSCALES`. **  ⇒ *The diffusion length takes the leaf clock and the optical depth the stacking
  clock -- two objects on the same side of the rate rule, on opposite clocks, with nothing stating
  the choice.*  So the other assignment is not an invention: `VISLEAF=1` applies to `tau` exactly the
  weighting `1/k_D^2` already applies to itself.

  ⚑⚑ ON THE GEOMETRY THE TWO AGREE, WHICH IS THE ORDER'S SECOND BRANCH.  `d r_s/d chi` goes
  {g('cs','cr','0'):.6f} -> {g('cs','cr','1'):.6f} on the arm, so {100*(1-_r0):.2f} per cent lower becomes {100*(1-_r1):.2f} -- a move of
  {100*abs(_r1-_r0)/_r0:.2f} per cent.  ** And structurally, not luckily: it is a RATIO of two accumulations across the
  SAME window, so re-weighting the measure re-weights both. **  ⇒ The visibility is not where the
  freedom is, and the 12.8 per cent is forced by the rule as stated.

  ⛔ BUT THE CONTRAST AND THE COMB DISAGREE, AND THE ORDER SAID TO REPORT THAT RATHER THAN PICK.  The
  injection's retained ratio goes {Y0.mean():.4f} -> {Y1.mean():.4f} and its slope {S0:+.5f} -> {S1:+.5f}, TOWARD the real
  source's 1.0694 and +0.01167.  ** But the arm's first peak moves {COMB[('cr','0')]['pk'][0]} -> {COMB[('cr','1')]['pk'][0]} and its l_1/l_A
  {COMB[('cr','0')]['r']:.4f} -> {COMB[('cr','1')]['r']:.4f}, AWAY from the sky's {SKY:.4f}; P1/P2 goes {COMB[('cr','0')]['p12']:.3f} -> {COMB[('cr','1')]['p12']:.3f}; and the control's
  comb is bit-identical both ways. **  ⚠ *And the contrast improvement is partly an artefact of the
  same move: band by band the `VISLEAF=1` ratio is non-monotonic scatter with a fitted residual
  {np.std(Y1-np.polyval([S1,I1],CTR))/np.std(Y0-np.polyval([S0,I0],CTR)):.1f} times the current assignment's, because moving `eta_LS` moves the comb and a band
  ratio of two oscillations out of alignment in q reads their phase mismatch.*  ⇒ *** The geometry
  says forced, the contrast says improvable, the comb says no -- and the comb is the only one of the
  three with an external referent. ***

  ⚑ ⓶ AND THE SOURCE'S CANCELLATION IS HALF THE LEVEL AND NONE OF THE SLOPE.  Multiplying the
  injection by `cc66.40`'s measured source deficit -- {SRC_.mean():.4f}, FLAT in q at {SS:+.5f} -- gives {PROD.mean():.4f} at
  {SX:+.5f} against the real {REAL.mean():.4f} at {SR:+.5f}.  ** That is {100*_lev:.0f} per cent of the level gap and {100*_slp:.0f} per cent
  of the slope gap. **  ⇒ *So the four trough-filling channels account for about half the level and
  essentially none of the slope: the order's conditional is half satisfied and the closure it hoped
  for does not arrive.  What flattens the slope is the real source's own eta-dependence across the
  visibility -- exactly what the injection replaced -- and that is named, not measured here.*

  ⛔ THE BOUND.  *Whether the two-rate assignment is right is the row's question now and not this
  order's, and nothing here settles it.*  What is settled is that the rule as stated does not
  determine the visibility's clock, that the instrument's two plasma-accumulated objects are already
  on opposite clocks, and that the peak positions support the choice it currently makes.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the rate rule does not determine which clock the visibility is a density in, and the
instrument already answers the question twice and differently -- `1/k_D^2` Jac-weighted under
`LEAFSCALES` while `tau` is not, two plasma-accumulated objects on opposite clocks.  Under the other
admissible assignment d r_s/d chi moves by {100*abs(_r1-_r0)/_r0:.2f} per cent, so the 12.8 per cent is forced by the
rule as stated and the visibility is not where the freedom is.  The contrast moves toward the real
source ({Y0.mean():.4f} -> {Y1.mean():.4f}, slope {S0:+.5f} -> {S1:+.5f}) but the comb moves away from the sky (the arm's
l_1/l_A {COMB[('cr','0')]['r']:.4f} -> {COMB[('cr','1')]['r']:.4f} against {SKY:.4f}), and the contrast's improvement is partly the
statistic reading the comb shift -- its band residual is {np.std(Y1-np.polyval([S1,I1],CTR))/np.std(Y0-np.polyval([S0,I0],CTR)):.1f} times the current assignment's.
The two disagree and neither is picked.  And the source deficit closes {100*_lev:.0f} per cent of the level gap
and {100*_slp:.0f} per cent of the slope gap, so the sector does not close into one account.
NOT CLAIMED: that the two-rate assignment is right; that VISLEAF=1 is wrong as physics; that the
0.06 per cent invariance settles the row; a mechanism beyond cc66.42's; and the injected runs are
not spectra of this model.
""")
