"""
P15_the_monopole_zero_point_is_not_the_channel_and_the_two_residuals_point_opposite_ways
========================================================================================

LEVEL: `r6897`'s order, which is a measurement and not a mechanism -- **the value the monopole
oscillation swings ABOUT at last scattering, against what each arm's own baryon loading accounts
for**, and then whether the two residual statistics the order names imply the SAME effective
loading displacement.

** THE READING THE ORDER PUT UP, AND IT IS THE RIGHT PLACE TO START. **  `r6897`: *"This arm's peaks
land where the sky's are, its envelope is right, and its troughs are too deep."*  Trough depth is set
by the dipole-to-monopole ratio at last scattering; and the standard thing that lowers that ratio is
the BARYON LOADING, through the displacement of the oscillation's zero point -- the monopole swings
about $-(1+R)\\Psi$ rather than about zero.  ⇒ *And that same displacement is what makes odd peaks
higher than even ones, so a spectrum with too much loading has too much odd-even alternation AND
too-deep troughs, together.*  ⚠ *And the refit has already spent the baryon density trying to cancel
them: it settles at $\\omega_b = 0.021524$ against the control's $0.021966$, low in exactly the
direction that relieves both, and both survive.*

** WHAT THIS RECEIPT MEASURES. **

 (a) ⚑ ** THE EFFECTIVE ZERO POINT, ON THE REPORTING PATH. **  The offset of $\\Theta_0+\\Psi$ as a
     function of $k$ at the visibility peak, in units of that arm's own $\\Psi$.  The tight-coupling
     prediction is $-R$.
 (b) What each arm's own loading accounts for: $R = 3\\rho_b/4\\rho_\\gamma$ at its own visibility
     peak, from its own fitted $\\omega_b$ and its own $z_*$.
 (c) The two residual statistics -- odd-even ALTERNATION and acoustic CONTRAST -- and the effective
     $\\Delta\\omega_b$ each implies, from the control's OWN measured response.  ⇒ *Do the two agree?*

** AND THE ESTIMATOR IS CALIBRATED BEFORE ITS VERDICT IS READ, WHICH IS r4558's RULE APPLIED TO A
MEASUREMENT RATHER THAN TO A KNOB. **  *A number that has not been shown to move when the thing it
measures moves is not a measurement.*  ⇒ The control is re-run with its baryon density displaced by
$\\pm8$ per cent and the estimator is asked whether it tracks the KNOWN $\\Delta R$.  It tracks $79$
per cent of it -- not all, because the offset is not exactly $-R$ (the potential decays inside the
horizon and $R$ grows), which is why the response and not the raw prediction is what converts a
measured offset difference into an effective $\\Delta\\omega_b$.

-------------------------------------------------------------------------------
COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms are the verified 185-bin
    refit minima of `r6825+cc66.25`.  The only parameter displaced anywhere is $\\omega_b$ on the
    CONTROL, and only to measure the control's own response; the displacements are $\\pm4$ and $\\pm8$
    per cent and they are declared in the table that uses them.
  * The fields at the visibility peak are saved by `ZPSAVE`, new here and wired into `hier_run` -- the
    REPORTING path.  ⌗ *`PHISAVE` already saves fields and is one of the nine switches `r6893+cc66.37`
    measured as OFF the reporting path, so using it would have measured the low-multipole construction
    and called it the reporting one.*
  * ** THE NEW SWITCH'S DEFAULT IS PROVED AND NOT ASSERTED **: both arms' bases are re-run against the
    edited file and gated BIT-IDENTICAL against the banked screen, before any other number is read.
  * The alternation and contrast statistics are computed in the binned, lensed, amplitude-fitted space
    `cc66.35` defined them in, and the contrast reproduces its $1.0401$ as a check on the machinery.
  * ** NOT CLAIMED: a mechanism for the contrast imbalance. **  `r6897` says this is an order to
    measure a displacement and check whether two residuals are one, and that no mechanism is being
    asked for and none should be claimed.

WHAT IS CLAIMED.

 (1) The visibility peak and its width are now in the header on every path, which is what `r6897`
     asked for -- and the two arms' widths have never been side by side on the reporting path before:
     $38.04$ Mpc on the control against $43.59$ on the arm.
 (2) `ZPSAVE` is additive: unset, both arms come back bit-identical.
 (3) (b) Each arm's own loading at its own visibility peak: $R = 0.61063$ on the control, $0.59969$ on
     the arm -- the arm's is LOWER, which is the direction its lower $\\omega_b$ requires.
 (4) (a) ⚑ ** BOTH ARMS' MONOPOLE OFFSETS SIT AT THE SAME FRACTION OF THEIR OWN $-R$, AND IT IS NOT
     ONE. **  The offset approaches the tight-coupling equilibrium from below, reaching about $0.78$ of
     $-R$ at the visibility peak on BOTH arms, growing with wavenumber.  *So the absolute question
     "does it match its own $(1+R)$" answers NO on both arms and by the same amount -- which is a fact
     about the approach to equilibrium and not about either arm.*
 (5) ⚑⚑ ** AND THE ARM'S OFFSET FALLS SHORT OF WHAT ITS OWN LOADING ACCOUNTS FOR, WHICH IS THE WRONG
     SIGN FOR THE LOADING READING. **  Calibrated against the control's own $\\omega_b$ response, the
     unaccounted part is an effective $\\Delta\\omega_b$ of about $-2.5$ per cent -- a further DEFICIT
     on top of the $2.0$ per cent the arm's $\\omega_b$ already is.  *Too much loading is what would
     deepen the troughs; the arm's monopole behaves as though it had too little.*
 (6) ⚑⚑ (c) ** AND THE TWO RESIDUALS DO NOT POINT THE SAME WAY -- THEY DIFFER BY A FACTOR OF SIXTEEN
     AND IN SIGN. **  Against the control -- which is the reference $\\Delta$ is built on -- the arm's
     CONTRAST is $4.0$ per cent higher and its ALTERNATION about $2$ per cent LOWER.  Converted through
     the control's own measured responses, the contrast asks for an effective $\\omega_b$ of $+22.9$
     per cent and the alternation for $-1.4$.  ⇒ *They are not one number; the search splits.*
 (6b) ⚑⚑ ** AND THE $+22.9$ IS A LOWER BOUND, BECAUSE THE CONTRAST RESPONSE SATURATES. **  Over the
     whole $\pm8$ per cent range the contrast spans only $0.028$ and its increments FALL monotonically,
     so a straight line overstates what $\\omega_b$ can deliver.  *** A four per cent contrast excess
     is beyond what the baryon density reaches in this construction at any value, not merely at an
     implausible one. ***  ⌗ *And the monopole offset of (5) agrees with the ALTERNATION, at $-2.9$ per
     cent against $-1.4$: two independent measurements of the loading displacement agree, and it is
     the contrast that stands apart.*
 (7) ⚠ ** AND THAT IS PARTLY A CORRECTION TO THE ORDER'S PREMISE, WHICH MIXED TWO REFERENCES. **
     `r6897` reads the alternation excess off $P_1/P_2 = 2.264$ against the SKY's $2.217$, and the
     contrast ratio $1.040$ against the CONTROL.  *Against the control, on the banked spectra, the
     arm's $P_1/P_2$ is $2.141$ against $2.191$ -- LOWER, not higher.*
 (8) And one positive localisation, measured and not inferred: the arm's DIPOLE-to-monopole amplitude
     ratio at the visibility peak is $1.8$ per cent higher than the control's and GROWS with
     wavenumber.  ⚠ *Its naive sign is opposite to the contrast excess -- more Doppler fills troughs
     -- so it does not explain the contrast either, and that tension is stated rather than resolved.*

NOT CLAIMED: a mechanism for the contrast imbalance; that the dipole excess produces the contrast
excess, whose sign is wrong for it; that the offset's approach to $-R$ is a defect of either arm.
-------------------------------------------------------------------------------
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
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
SRC = open(INST).read()
for _need in ('r6897_fields.npz', 'r6897_noop.npz'):
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

# ===================================================================================================
# PART 1 -- THE NEW HEADER LINE, THE NEW SWITCH, AND ITS DEFAULT PROVED.
# ===================================================================================================
print("\nPART 1 -- WHAT THIS REVISION ADDED TO THE INSTRUMENT, AND THE PROOF IT ADDED NOTHING ELSE.")
print("-" * 100)
FLD = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
TAGS = sorted({k.split('__')[1] for k in FLD.files})
g = lambda key, t: FLD[f'{key}__{t}']
print(f"    {'run':6s} {'omega_b':>11s} {'eta_LS':>8s} {'z_*':>9s} {'FWHM/Mpc':>9s} {'R':>9s} "
      f"{'1+R':>9s} {'r_s':>8s} {'modes':>6s}")
for t in ('lcdm', 'cr', 'wblo', 'wbhi'):
    print(f"    {t:6s} {float(g('ombh2', t)):11.8f} {float(g('eta', t)):8.2f} "
          f"{1/float(g('a_ls', t))-1:9.1f} {float(g('eta_ls_w', t)):9.2f} "
          f"{float(g('R_eta', t)):9.5f} {1+float(g('R_eta', t)):9.5f} "
          f"{float(g('r_s', t)):8.2f} {len(g('k', t)):6d}")
check("⚑ the visibility peak and its width are in the header on EVERY path now, which is what `r6897` "
      "asked for -- and the two arms' widths have never been side by side on the reporting path "
      "before, `ETA_LS_W` having been printed only inside `los_spectrum`",
      "visibility: peak at eta" in SRC
      and SRC.index("visibility: peak at eta") > SRC.index("def main():")
      and SRC.index("visibility: peak at eta") < SRC.index("if os.environ.get('LOS', '1') == '1':"),
      f"control FWHM {float(g('eta_ls_w','lcdm')):.2f} Mpc at eta = {float(g('eta','lcdm')):.2f}; "
      f"arm {float(g('eta_ls_w','cr')):.2f} Mpc at {float(g('eta','cr')):.2f} -- "
      f"{float(g('eta_ls_w','cr'))/float(g('eta_ls_w','lcdm')):.3f} times as wide in conformal time")
_noop = {}
for arm in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r6893_switch_screen_{arm}.npz'), allow_pickle=True)
    a = np.load(os.path.join(SP, 'r6897_noop.npz'), allow_pickle=True)
    _noop[arm] = (bool(np.array_equal(a[f'Dl__{arm}'], d['Dl__base'])),
                  float(np.max(np.abs(a[f'Dl__{arm}'] - d['Dl__base']))))
check("⚑ ** AND `ZPSAVE` IS ADDITIVE, WHICH IS MEASURED AND NOT ASSERTED. **  It adds a branch inside "
      "`hier_run`'s own batch loop, so the default path gains a test per batch -- and both arms come "
      "back BIT-IDENTICAL against the banked screen base.  *`cc66.36` is why this seat no longer says "
      "a change is nothing without running it.*",
      all(v[0] for v in _noop.values()),
      f"both arms, max |dD_l| = {max(v[1] for v in _noop.values()):.1f} exactly")
check("...and it saves the UNDAMPED monopole on purpose, which the source text states: the envelope "
      "`D` multiplies the whole of Theta_0, its offset included, so the displacement could not be "
      "read off a damped monopole at all",
      "_ZTH.append(_yl[:, 2] / 4)" in SRC and "UNDAMPED Theta_0" in SRC,
      "Y[:, :, 2] / 4 with no D, at the one eta nearest the visibility peak")

# ===================================================================================================
# PART 2 -- (b) WHAT EACH ARM'S OWN LOADING ACCOUNTS FOR.
# ===================================================================================================
print("\nPART 2 -- (b) THE LOADING EACH ARM'S OWN BARYON DENSITY PUTS AT ITS OWN VISIBILITY PEAK.")
print("-" * 100)
R_L, R_C = float(g('R_eta', 'lcdm')), float(g('R_eta', 'cr'))
W_L, W_C = float(g('ombh2', 'lcdm')), float(g('ombh2', 'cr'))
print(f"    control: omega_b = {W_L:.8f}, a_LS/a_rec = "
      f"{float(g('a_ls','lcdm'))/float(g('a_rec','lcdm')):.5f}  ->  R = {R_L:.5f}, 1+R = {1+R_L:.5f}")
print(f"    arm    : omega_b = {W_C:.8f}, a_LS/a_rec = "
      f"{float(g('a_ls','cr'))/float(g('a_rec','cr')):.5f}  ->  R = {R_C:.5f}, 1+R = {1+R_C:.5f}")
check("the arm's own loading is LOWER than the control's, by very nearly what its own lower omega_b "
      "requires -- so the loading itself is not in question and what is being tested is whether the "
      "monopole's displacement follows it",
      R_C < R_L and abs((R_C / R_L - 1) - (W_C / W_L - 1)) < 0.01,
      f"R: {R_C/R_L-1:+.4f} against omega_b: {W_C/W_L-1:+.4f} -- the small difference is the two "
      f"arms' different a_LS")

# ===================================================================================================
# PART 3 -- (a) THE MEASURED ZERO POINT, AND THE CALIBRATION THAT MAKES IT A MEASUREMENT.
# ===================================================================================================
print("\nPART 3 -- (a) THE VALUE THE MONOPOLE OSCILLATION SWINGS ABOUT, MEASURED.")
print("-" * 100)
print("""
  ** THE ESTIMATOR, AND WHY IT IS A LOCAL FIT AND NOT A MIDPOINT. **  Two obvious estimators are
  biased and were tried first:
    * the midpoint of successive extrema, 0.5(max+min), which carries half the change in amplitude
      between them -- and the amplitude falls steeply with k, so this came out alternating with
      the extremum index by a factor of three;
    * the quarter-half-quarter combination of three consecutive extrema, which cancels a LINEAR
      amplitude variation and left a residual alternation of +-15 per cent from the curvature.
  ⇒ ** So the offset is read off a local five-parameter least squares over exactly one acoustic
  period **, u = c + (a0 + a1 dq) cos(pi q) + (b0 + b1 dq) sin(pi q), on u = (Theta_0+Psi)/Psi with
  q = k r_s / pi.  *The amplitude is allowed to vary linearly across the window, which is precisely
  what biases the other two.*
""")


def offsets(tag, half=2.0, amp_deg=2, step=0.25):
    """the offset of u = (Theta_0+Psi)/Psi in a window of 2*half acoustic periods, with the
    oscillation's amplitude free to vary as a polynomial of degree `amp_deg` across it"""
    k = g('k', tag)
    o = np.argsort(k)
    k = k[o]
    u = ((g('th0', tag) + g('psi', tag)) / g('psi', tag))[o]
    q = k * float(g('r_s', tag)) / np.pi
    out_q, out_c = [], []
    for q0 in np.arange(1.5 + half, q.max() - half - 0.1, step):
        m = np.abs(q - q0) <= half
        if m.sum() < 20:
            continue
        dq = q[m] - q0
        cols = [np.ones(m.sum())]
        for j in range(amp_deg + 1):
            cols += [dq ** j * np.cos(np.pi * q[m]), dq ** j * np.sin(np.pi * q[m])]
        b_ = np.linalg.lstsq(np.column_stack(cols), u[m], rcond=None)[0]
        out_q.append(q0)
        out_c.append(b_[0])
    return np.array(out_q), np.array(out_c)


def readout(half=2.0, amp_deg=2):
    """(fraction of -R on each arm, tracking of a known dR, measured/predicted/unaccounted
    offset difference, effective d omega_b) at one estimator setting"""
    O = {t: offsets(t, half, amp_deg) for t in ('lcdm', 'cr', 'wblo', 'wbhi')}
    QQ = np.arange(1.5 + half, 11.0, 0.25)
    oo = {t: np.interp(QQ, O[t][0], O[t][1]) for t in O}
    dwb = float(g('ombh2', 'wbhi')) - float(g('ombh2', 'wblo'))
    dR = float(g('R_eta', 'wbhi')) - float(g('R_eta', 'wblo'))
    dc = (oo['wbhi'] - oo['wblo']).mean()
    resp = dc / dwb
    pred = resp * (W_C - W_L)
    meas = (oo['cr'] - oo['lcdm']).mean()
    return dict(QQ=QQ, oo=oo, fracL=oo['lcdm'].mean() / -R_L, fracC=oo['cr'].mean() / -R_C,
                scatter=float(oo['lcdm'].std()), track=dc / -dR, resp=resp, dR=dR, dwb=dwb,
                dc=dc, pred=pred, meas=meas, unacc=meas - pred, eff=(meas - pred) / resp)


RD = readout()
QC, oc = RD['QQ'], (lambda t: RD['oo'][t])
print(f"    window = 4 acoustic periods, amplitude quadratic across it; "
      f"q-to-q scatter of the offset on the control = {RD['scatter']:.4f} on an offset of "
      f"{oc('lcdm').mean():.4f}")
print(f"    {'run':6s} {'-R':>9s} {'mean offset':>12s} {'/(-R)':>7s}")
for t in ('lcdm', 'cr', 'wblo', 'wbhi'):
    print(f"    {t:6s} {-float(g('R_eta', t)):9.5f} {oc(t).mean():12.5f} "
          f"{oc(t).mean()/-float(g('R_eta', t)):7.4f}")
check("⚑ ** BOTH ARMS' OFFSETS SIT AT THE SAME FRACTION OF THEIR OWN -R, AND IT IS NOT ONE. **  The "
      "offset approaches the tight-coupling equilibrium FROM BELOW and reaches about four fifths of it "
      "at the visibility peak, on the control and on the arm alike.  *So the absolute form of (b)'s "
      "question answers NO on both arms and by nearly the same amount, which is a fact about the "
      "approach to equilibrium rather than about either arm: the potential decays inside the horizon "
      "and R grows, so the instantaneous -R(eta_*) Psi(eta_*) is not the offset.*",
      0.70 < RD['fracL'] < 0.85 and 0.70 < RD['fracC'] < 0.85
      and abs(RD['fracC'] - RD['fracL']) < 0.03,
      f"control {RD['fracL']:.4f} of its own -R, arm {RD['fracC']:.4f}")

print("\n  ----- THE CALIBRATION, WHICH IS r4558's RULE APPLIED TO A MEASUREMENT -----")
print(f"    omega_b {float(g('ombh2','wblo')):.8f} -> {float(g('ombh2','wbhi')):.8f}  "
      f"(d = {RD['dwb']:+.6f}, {RD['dwb']/W_L*100:+.2f}% of the control's)")
print(f"    R       {float(g('R_eta','wblo')):.5f} -> {float(g('R_eta','wbhi')):.5f}  "
      f"(dR = {RD['dR']:+.5f})")
print(f"    measured d(offset) = {RD['dc']:+.5f}   against the naive prediction -dR = {-RD['dR']:+.5f}")
print(f"    ⇒ the estimator tracks {RD['track']*100:.1f} per cent of a KNOWN dR, and "
      f"d(offset)/d(omega_b) = {RD['resp']:+.3f}")
check("⚑ the estimator MOVES when the thing it measures moves, and by most of the known amount: a "
      "baryon density displaced by 16 per cent produces about four fifths of the offset change the "
      "tight-coupling prediction asks for.  ** The shortfall is the same one the gate above reports, "
      "and it is why the measured RESPONSE and not the raw -R is what converts an offset difference "
      "into an effective displacement. **",
      0.70 < RD['track'] < 0.90 and RD['dc'] < 0,
      f"{RD['track']*100:.1f} per cent of dR, response {RD['resp']:+.3f} per unit omega_b")
print(f"\n    arm - control, MEASURED  d(offset) = {RD['meas']:+.5f}")
print(f"    what their own omega_b ACCOUNTS FOR (response x d omega_b) = {RD['pred']:+.5f}")
print(f"    ⇒ UNACCOUNTED = {RD['unacc']:+.5f}, an effective d(omega_b) of {RD['eff']:+.6f} "
      f"({RD['eff']/W_L*100:+.2f}% of the control's)")
check("⚑⚑ ** AND THE ARM'S OFFSET FALLS SHORT OF WHAT ITS OWN LOADING ACCOUNTS FOR -- WHICH IS THE "
      "WRONG SIGN FOR THE LOADING READING. **  The unaccounted part is an effective omega_b DEFICIT of "
      "about three per cent, on top of the two per cent the arm's fitted omega_b already is.  *** Too "
      "much loading is what deepens troughs and raises alternation.  This arm's monopole behaves as "
      "though it had too LITTLE, and its troughs are deeper anyway. ***  ⇒ On `r6897`'s own branching "
      "this is neither \"the construction supplies an R-like offset\" nor \"both arms sit on their own "
      "(1+R)\": it is a third outcome, and it refutes the loading reading BY SIGN rather than leaving "
      "it undetermined.",
      RD['unacc'] > 0 and RD['eff'] < 0 and abs(RD['eff'] / W_L) > 0.01,
      f"unaccounted offset {RD['unacc']:+.5f} -> effective d(omega_b) {RD['eff']/W_L*100:+.2f}%, sign "
      f"opposite to what deeper troughs would need")
print("\n  ----- AND THE SAME READOUT AT FIVE ESTIMATOR SETTINGS, BECAUSE THE FIRST ONE WAS NOISY -----")
print(f"    {'window':>8s} {'amp':>4s} {'scatter':>8s} {'frac of -R':>11s} {'tracking':>9s} "
      f"{'unaccounted':>12s} {'eff dwb':>9s}")
ALT = []
for _h, _d in ((0.5, 1), (1.0, 1), (1.0, 2), (1.5, 2), (2.0, 2)):
    r = readout(_h, _d)
    ALT.append(r)
    print(f"    {2*_h:8.0f} {_d:4d} {r['scatter']:8.4f} {r['fracL']:11.4f} "
          f"{r['track']*100:8.1f}% {r['unacc']:+12.5f} {r['eff']/W_L*100:+8.2f}%")
check("⚑ ** AND THE VERDICT IS THE ESTIMATOR'S ONLY IN ITS THIRD DIGIT. **  Across five window widths "
      "and amplitude degrees the fraction of -R stays at 0.77-0.78, the tracking of a known dR at "
      "76-79 per cent, and the unaccounted part POSITIVE with an effective omega_b deficit between "
      "two and three per cent.  *The wide windows are the well-conditioned ones: at one period the "
      "constant is nearly collinear with the dq-weighted oscillation terms, which is why the first "
      "version of this scattered by an amount comparable to the offset itself.*",
      all(r['unacc'] > 0 and -0.035 < r['eff'] / W_L < -0.01 and 0.74 < r['track'] < 0.82
          and 0.75 < r['fracL'] < 0.80 for r in ALT),
      f"effective d omega_b from {min(r['eff']/W_L for r in ALT)*100:+.2f}% to "
      f"{max(r['eff']/W_L for r in ALT)*100:+.2f}%, tracking "
      f"{min(r['track'] for r in ALT)*100:.1f}-{max(r['track'] for r in ALT)*100:.1f}%")

# ===================================================================================================
# PART 4 -- (c) THE TWO RESIDUAL STATISTICS, AND THE EFFECTIVE DISPLACEMENT EACH IMPLIES.
# ===================================================================================================
print("\nPART 4 -- (c) ALTERNATION AND CONTRAST, AND WHETHER THEY ARE ONE NUMBER.")
print("-" * 100)
check("the bank the response needs is present: `spectra/r6897_wb_response_lcdm.npz`",
      os.path.exists(os.path.join(SP, 'r6897_wb_response_lcdm.npz')), 'r6897_wb_response_lcdm.npz')
if FAILS:
    print("\n  ⛔ THE RESPONSE BANK IS NOT ON DISK YET.  Part 4 is not run and this receipt FAILS")
    print("     rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("""
  ** THE TWO STATISTICS, IN cc66.35's OWN SPACE. **  Both are read off the binned, lensed,
  amplitude-fitted model, and the CONTRAST is `cc66.35`'s own statistic -- the regression of one arm's
  envelope-normalised oscillation on the other's -- so it reproduces its 1.0401 as a check that the
  machinery here is the same machinery.

  ** AND THE ALTERNATION IS NOT A SECOND DIFFERENCE, WHICH IS THE ONE PLACE THIS COULD HAVE GONE
  WRONG QUIETLY. **  A second difference of the peak heights vanishes on a LINEAR trend, and the
  envelope's decline is strongly CURVED at low multipole -- so a second-difference statistic comes out
  dominated by the first triple and is mostly curvature.  ⇒ At the peak positions the trend and the
  alternation are FITTED TOGETHER, o(p_n) = c_0 + c_1 n + c_2 n^2 + a (-1)^n, and `a` is the answer.
""")
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                                # noqa: E402
import camb                                                                  # noqa: E402

LC, FACB = CS.bin_center_and_fac()
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
_LG = np.arange(len(_le), dtype=float)
RAT = np.ones_like(_le)
_m = _un > 0
RAT[_m] = _le[_m] / _un[_m]
mb = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, _LG, RAT))
sp = lambda f: (lambda d: (d['ls'].astype(float), d['Dl'].astype(float)))(np.load(os.path.join(SP, f)))
_b0 = sp('cc66_r185_verify_lcdm.npz')
KEEP = np.isfinite(mb(*_b0)) & (LC >= 100) & (LC <= 1900)
FISH = np.linalg.inv(CS.COV_TT[np.ix_(KEEP, KEEP)])
DK = CS.X_DATA[KEEP]
LCK, FACK = LC[KEEP], FACB[KEEP]


def fit_amp(ls, Dl):
    m = mb(ls, Dl)[KEEP]
    return float(m @ FISH @ DK / (m @ FISH @ m)) * m


def env1(y, win):
    e = np.empty_like(y)
    for j, l in enumerate(LCK):
        k = (LCK >= l - win / 2) & (LCK <= l + win / 2)
        e[j] = np.exp(np.mean(np.log(y[k])))
    return e


_dL = fit_amp(*_b0) * FACK
_PKI = [j for j in range(1, len(LCK) - 1) if _dL[j] > _dL[j - 1] and _dL[j] > _dL[j + 1]]
PERIOD = float(np.median(np.diff(LCK[_PKI])))
osc = lambda m: (lambda d, e: (d - e) / e)(m * FACK, env1(m * FACK, PERIOD))
REF = fit_amp(*_b0)
OREF = osc(REF)
contrast = lambda m: float(np.sum(osc(m) * OREF) / np.sum(OREF * OREF))


def acoustic_peaks(o, sep=None):
    """one maximum per acoustic period: greedy on height with a minimum separation.  A plain
    local-maximum test finds three 'peaks' eighteen multipoles apart inside one acoustic peak."""
    sep = PERIOD / 2 if sep is None else sep
    out = []
    for j in sorted([j for j in range(1, len(o) - 1) if o[j] > o[j - 1] and o[j] > o[j + 1]],
                    key=lambda j: -o[j]):
        if all(abs(LCK[j] - LCK[i]) > sep for i in out):
            out.append(j)
    return sorted(out)


def alternation(m, deg=2):
    o = osc(m)
    pk = acoustic_peaks(o)
    n = np.arange(len(pk), dtype=float)
    X = np.column_stack([n ** j for j in range(deg + 1)] + [(-1.0) ** n])
    b = np.linalg.lstsq(X, o[pk], rcond=None)[0]
    return float(b[-1]), pk


M_ARM = fit_amp(*sp('cc66_r185_verify_cr.npz'))
A_L, _pk = alternation(REF)
A_C, _ = alternation(M_ARM)
C_C = contrast(M_ARM)
print(f"    the acoustic peaks the statistics are read at: l = {[round(LCK[j]) for j in _pk]}")
print(f"    control: contrast {contrast(REF):.5f}   alternation a = {A_L:+.6f}")
print(f"    arm    : contrast {C_C:.5f}   alternation a = {A_C:+.6f}")
check("the contrast statistic reproduces `cc66.35`'s 1.0401 for the arm against the control, so the "
      "space these two statistics live in is that receipt's space and not a new one",
      abs(C_C - 1.0401) < 0.0005 and abs(contrast(REF) - 1.0) < 1e-12,
      f"arm {C_C:.5f} against cc66.35's 1.0401; the control against itself {contrast(REF):.5f}")
check("⚑⚑ ** AND AGAINST THE CONTROL THE TWO RESIDUALS POINT OPPOSITE WAYS: the arm's CONTRAST is four "
      "per cent HIGHER and its ALTERNATION is about two per cent LOWER. **",
      C_C > 1.02 and A_C < A_L,
      f"contrast {C_C-1:+.4f}; alternation {A_C-A_L:+.6f} ({(A_C/A_L-1)*100:+.2f}%)")
for _d in (1, 3):
    _a1, _ = alternation(REF, _d)
    _a2, _ = alternation(M_ARM, _d)
    print(f"      with the trend at degree {_d}: control {_a1:+.6f}, arm {_a2:+.6f}, "
          f"difference {_a2-_a1:+.6f}")
check("...and the sign of that alternation difference does not depend on how the envelope's own trend "
      "is carried: degree one, two and three all give the arm LOWER",
      all(alternation(M_ARM, _d)[0] < alternation(REF, _d)[0] for _d in (1, 2, 3)),
      ", ".join(f"deg {_d}: {alternation(M_ARM,_d)[0]-alternation(REF,_d)[0]:+.6f}" for _d in (1, 2, 3)))

print("\n  ----- THE CONTROL'S OWN RESPONSE TO ITS BARYON DENSITY -----")
WB = np.load(os.path.join(SP, 'r6897_wb_response_lcdm.npz'), allow_pickle=True)
WBV = sorted(float(x) for x in WB['omega_b'])
print(f"    {'omega_b':>12s} {'of control':>11s} {'slices':>7s} {'contrast':>10s} {'alternation':>12s}")
CR_, AL_ = [], []
for w in WBV:
    key = [k for k in WB.files if k.startswith('Dl__') and abs(float(k[4:]) - w) < 1e-12][0][4:]
    m = fit_amp(WB[f'ls__{key}'].astype(float), WB[f'Dl__{key}'])
    CR_.append(contrast(m))
    AL_.append(alternation(m)[0])
    print(f"    {w:12.8f} {w/W_L-1:+10.2%} {int(WB[f'nsl__{key}']):7d} {CR_[-1]:10.5f} {AL_[-1]:+12.6f}")
CR_, AL_ = np.array(CR_), np.array(AL_)
WBV = np.array(WBV)
pc = np.polyfit(WBV - W_L, CR_, 1)
pa = np.polyfit(WBV - W_L, AL_, 1)
print(f"    d(contrast)/d(omega_b)    = {pc[0]:+.4f} per unit omega_b   "
      f"(= {pc[0]*W_L*0.01:+.6f} per one per cent)")
print(f"    d(alternation)/d(omega_b) = {pa[0]:+.4f} per unit omega_b   "
      f"(= {pa[0]*W_L*0.01:+.6f} per one per cent)")
check("⚑ both statistics respond to the baryon density, and in the directions `r6897`'s reading "
      "requires: MORE loading gives MORE odd-even alternation and MORE contrast -- deeper troughs.  "
      "*Neither is a null, so neither residual is being converted through a response that is not "
      "there.*",
      pa[0] > 0 and pc[0] > 0,
      f"d(alternation)/d(omega_b) = {pa[0]:+.3f}, d(contrast)/d(omega_b) = {pc[0]:+.3f}")
_lin_c = np.max(np.abs(CR_ - np.polyval(pc, WBV - W_L))) / (CR_.max() - CR_.min())
_lin_a = np.max(np.abs(AL_ - np.polyval(pa, WBV - W_L))) / (AL_.max() - AL_.min())
check("...and both are linear enough over this range that a single slope is the right summary, which "
      "is why five values were run rather than two",
      _lin_c < 0.12 and _lin_a < 0.25,
      f"largest departure from the straight line, as a fraction of the range: contrast "
      f"{_lin_c:.3f}, alternation {_lin_a:.3f}")

EFF_C = (C_C - 1.0) / pc[0]
EFF_A = (A_C - A_L) / pa[0]
print(f"\n    the arm's CONTRAST excess  {C_C-1:+.5f}  implies an effective d(omega_b) of "
      f"{EFF_C:+.6f}  ({EFF_C/W_L*100:+.2f}%)")
print(f"    the arm's ALTERNATION diff {A_C-A_L:+.6f}  implies an effective d(omega_b) of "
      f"{EFF_A:+.6f}  ({EFF_A/W_L*100:+.2f}%)")
print(f"    and the arm's own omega_b is already {W_C-W_L:+.6f} ({W_C/W_L-1:+.2%}) from the control's")
check("⚑⚑⚑ ** AND THE ANSWER TO r6897's SINGLE MOST INFORMATIVE NUMBER IS THAT THE TWO DISAGREE, AND "
      "NOT BY A LITTLE: THEY HAVE OPPOSITE SIGNS. **  The contrast excess asks for MORE baryon "
      "loading; the alternation asks for LESS.  *** So the remaining residual is not one parameter's "
      "worth of physics, and the search splits -- which `r6897` says is also worth knowing, and "
      "cheaply. ***",
      EFF_C > 0 > EFF_A,
      f"contrast {EFF_C/W_L*100:+.2f}% against alternation {EFF_A/W_L*100:+.2f}% of the control's "
      f"omega_b -- opposite signs")
_inc = np.diff(CR_)
check("⚑⚑ ** AND THE +23 PER CENT IS A LOWER BOUND, BECAUSE THE CONTRAST RESPONSE SATURATES. **  Over "
      "the whole 16 per cent range the contrast spans only 0.028, and its successive increments FALL "
      "monotonically -- 0.0119, 0.0087, 0.0054, 0.0020 -- so a straight line OVERSTATES what omega_b "
      "can deliver above the control.  *** A four per cent contrast excess is therefore beyond what "
      "the baryon density reaches in this construction at any value, not merely at an implausible "
      "one. ***",
      all(_inc[i] > _inc[i + 1] for i in range(len(_inc) - 1))
      and (CR_.max() - CR_.min()) < (C_C - 1.0),
      f"increments {', '.join(f'{x:+.4f}' for x in _inc)}; the whole response spans "
      f"{CR_.max()-CR_.min():.4f} against a contrast excess of {C_C-1:.4f}")
check("⚑ ...and the third measurement agrees with the second and not with the first: the MONOPOLE "
      "OFFSET of Part 3 also asks for LESS loading, at an effective d(omega_b) of about -3 per cent, "
      "which is the same sign and nearly the same size as the alternation's.  ** Two independent "
      "measurements of the loading displacement agree; it is the CONTRAST that stands apart. **",
      RD['eff'] < 0 and EFF_A < 0 and abs(RD['eff'] - EFF_A) < abs(RD['eff'] - EFF_C),
      f"monopole offset {RD['eff']/W_L*100:+.2f}%, alternation {EFF_A/W_L*100:+.2f}%, contrast "
      f"{EFF_C/W_L*100:+.2f}%")

# ===================================================================================================
# PART 5 -- ⚠ THE ORDER'S PREMISE, WHICH MIXED TWO REFERENCES.
# ===================================================================================================
print("\nPART 5 -- ⚠ WHERE THE 'ALTERNATION EXCESS' CAME FROM, AND WHAT IT IS AGAINST THE CONTROL.")
print("-" * 100)
from numpy.polynomial import polynomial as _P                                # noqa: E402
from scipy.signal import argrelextrema                                       # noqa: E402


def three_peaks(f):
    ls, Dl = sp(f)
    out = []
    for i in argrelextrema(Dl, np.greater, order=3)[0][:3]:
        x, y = ls[i - 3:i + 4], Dl[i - 3:i + 4]
        c = _P.polyfit(x - x.mean(), y, 2)
        lv = x.mean() - c[1] / (2 * c[2])
        out.append((float(lv), float(_P.polyval(lv - x.mean(), c))))
    return out


PK = {t: three_peaks(f) for t, f in (('control', 'cc66_r185_verify_lcdm.npz'),
                                     ('arm', 'cc66_r185_verify_cr.npz'))}
for t, v in PK.items():
    print(f"    {t:8s} peaks at l = {[round(a) for a, _ in v]}   heights "
          f"{[round(b, 4) for _, b in v]}   P1/P2 = {v[0][1]/v[1][1]:.4f}   "
          f"P1/P3 = {v[0][1]/v[2][1]:.4f}")
print(f"    and `r6897` reads the excess off P1/P2 = 2.264 against the SKY's 2.217, while the "
      f"contrast 1.040 is against the CONTROL.")
check("⚠ ** THE PREMISE MIXED TWO REFERENCES, AND AGAINST THE COMMON ONE THE ALTERNATION IS NOT "
      "ELEVATED. **  `r6897` pairs an alternation excess measured against the SKY with a contrast "
      "excess measured against the CONTROL.  *Against the control -- which is the reference Delta is "
      "built on and the reference this row's object is defined by -- the arm's P1/P2 is LOWER.*  ⇒ The "
      "two residuals were never pointing the same way; the appearance that they were is the two "
      "references.",
      PK['arm'][0][1] / PK['arm'][1][1] < PK['control'][0][1] / PK['control'][1][1],
      f"arm P1/P2 = {PK['arm'][0][1]/PK['arm'][1][1]:.4f} against the control's "
      f"{PK['control'][0][1]/PK['control'][1][1]:.4f}")

# ===================================================================================================
# PART 6 -- AND ONE POSITIVE LOCALISATION: THE DIPOLE.
# ===================================================================================================
print("\nPART 6 -- THE DIPOLE-TO-MONOPOLE AMPLITUDE RATIO AT THE VISIBILITY PEAK, MEASURED.")
print("-" * 100)
print("""
  `r6897` says that if the monopole's offset is clean, *"the difference is in how the DIPOLE is
  generated rather than where the monopole sits"*.  ⇒ The same `ZPSAVE` bank carries theta_b, so that
  is a measurement and not a further run: the Doppler source enters the transfer with amplitude
  theta_b/k against the monopole's Theta_0+Psi, and the damping envelope multiplies both and cancels.
""")


def amp_ratio(tag, half=2.0, amp_deg=2, step=0.25):
    k = g('k', tag)
    o = np.argsort(k)
    k = k[o]
    psi = g('psi', tag)[o]
    um = (g('th0', tag)[o] + psi) / psi
    ud = (g('tb', tag)[o] / k) / psi
    q = k * float(g('r_s', tag)) / np.pi
    Q, RT = [], []
    for q0 in np.arange(1.5 + half, q.max() - half - 0.1, step):
        m = np.abs(q - q0) <= half
        if m.sum() < 20:
            continue
        dq = q[m] - q0
        cols = [np.ones(m.sum())]
        for j in range(amp_deg + 1):
            cols += [dq ** j * np.cos(np.pi * q[m]), dq ** j * np.sin(np.pi * q[m])]
        X = np.column_stack(cols)
        bm = np.linalg.lstsq(X, um[m], rcond=None)[0]
        bd = np.linalg.lstsq(X, ud[m], rcond=None)[0]
        Q.append(q0)
        RT.append(float(np.hypot(bd[1], bd[2]) / np.hypot(bm[1], bm[2])))
    return np.array(Q), np.array(RT)


AR = {t: amp_ratio(t) for t in ('lcdm', 'cr')}
QD = np.arange(3.5, 11.0, 0.25)
arl = np.interp(QD, AR['lcdm'][0], AR['lcdm'][1])
arc = np.interp(QD, AR['cr'][0], AR['cr'][1])
print(f"    {'q band':>12s} {'control':>9s} {'arm':>9s} {'arm/control':>12s}")
for lo, hi in ((3.5, 6), (6, 8.5), (8.5, 11), (3.5, 11)):
    m = (QD >= lo) & (QD <= hi)
    print(f"    [{lo:5.1f},{hi:5.1f}] {arl[m].mean():9.5f} {arc[m].mean():9.5f} "
          f"{(arc[m]/arl[m]).mean():12.5f}   ({((arc[m]/arl[m]).mean()-1)*100:+.2f}%)")
_dip = (arc / arl).mean() - 1
check("⚑ the arm's dipole-to-monopole amplitude ratio at the visibility peak is about two per cent "
      "HIGHER than the control's, and it GROWS with wavenumber -- measured on the reporting path, on "
      "the same fields the offset came from",
      _dip > 0.005 and (arc / arl)[QD > 8.5].mean() > (arc / arl)[QD < 6].mean(),
      f"{_dip*100:+.2f}% over q in [3.5,11], rising from "
      f"{((arc/arl)[QD<6].mean()-1)*100:+.2f}% to {((arc/arl)[QD>8.5].mean()-1)*100:+.2f}%")
check("⚠ ** AND ITS NAIVE SIGN IS OPPOSITE TO THE CONTRAST EXCESS, WHICH IS STATED AND NOT RESOLVED. "
      "**  The Doppler term is a quarter period out of phase and FILLS the troughs -- which is what "
      "`cc66.36` measured, `DPSRC=0` taking the arm's own oscillation from 1.040 to 1.828.  *So a "
      "LARGER dipole fraction makes troughs SHALLOWER, and this arm's is larger while its troughs are "
      "deeper.*  ⇒ The dipole fraction does not explain the contrast excess either; it works against "
      "it.  ** What that leaves is a contrast excess whose source is larger than four per cent and "
      "partly cancelled -- which is a statement about size and not a mechanism, and it is as far as "
      "this order's measurements reach.**",
      _dip > 0 and C_C > 1.0,
      f"dipole fraction {_dip*100:+.2f}% (fills troughs, lowers contrast) against a contrast excess of "
      f"{(C_C-1)*100:+.2f}% (deeper troughs)")

# ===================================================================================================
print()
print("=" * 100)
print(f"""
WHAT THIS REVISION ESTABLISHES.

  ⚑ ** THE HEADER CARRIES THE VISIBILITY NOW, ON EVERY PATH, AND THE TWO ARMS' WIDTHS HAVE NEVER BEEN
  SIDE BY SIDE ON THE REPORTING PATH BEFORE. **  The control's last-scattering surface is
  {float(g('eta_ls_w','lcdm')):.2f} Mpc wide in conformal time at eta = {float(g('eta','lcdm')):.2f};
  the arm's is {float(g('eta_ls_w','cr')):.2f} Mpc at {float(g('eta','cr')):.2f} --
  {float(g('eta_ls_w','cr'))/float(g('eta_ls_w','lcdm')):.3f} times as wide.  ⌗ *`ETA_LS_W` was printed
  only inside `los_spectrum`, and `r6897` is right that this is not a shadow -- a print is not a knob,
  which is `LRSFROM`'s own lesson -- but the loading is read off this eta and the header should carry
  it.*

  ⚑⚑ ** (a)/(b) THE MONOPOLE'S ZERO POINT IS NOT THE CHANNEL, AND THE SIGN IS WHAT SAYS SO. **  On both
  arms the offset of Theta_0+Psi approaches the tight-coupling equilibrium -R Psi FROM BELOW and reaches
  {RD['fracL']:.3f} of it on the control and {RD['fracC']:.3f} on the arm at the visibility peak.  ⇒ And
  calibrated against the control's own response to a KNOWN displaced baryon density -- the estimator
  tracking {RD['track']*100:.0f} per cent of a known dR -- ** the arm's offset FALLS SHORT of what its
  own loading accounts for, by an effective omega_b of {RD['eff']/W_L*100:+.2f} per cent, on top of the
  {W_C/W_L*100-100:+.2f} per cent its fitted omega_b already is. **  *** Too much loading is what
  deepens troughs and raises alternation.  This arm's monopole behaves as though it had too LITTLE. ***
  ⇒ On `r6897`'s own branching this is a THIRD outcome, and it refutes the loading reading by sign
  rather than leaving it undetermined.

  ⚑⚑⚑ ** (c) AND THE TWO RESIDUALS ARE NOT ONE NUMBER: THEY HAVE OPPOSITE SIGNS. **  Against the
  control, the arm's CONTRAST is {(C_C-1)*100:+.2f} per cent and its ALTERNATION
  {(A_C/A_L-1)*100:+.2f} per cent.  Converted through the control's own measured responses --
  d(contrast)/d(omega_b) = {pc[0]:+.2f} and d(alternation)/d(omega_b) = {pa[0]:+.2f}, both positive, so
  more loading gives more of both -- ** the contrast asks for an effective omega_b of
  {EFF_C/W_L*100:+.2f} per cent and the alternation for {EFF_A/W_L*100:+.2f} per cent. **  ⇒ *** The
  remaining residual is NOT one parameter's worth of physics; the search splits. ***  ⌗ *And the
  monopole offset agrees with the alternation and not with the contrast -- two independent measurements
  of the loading displacement at {RD['eff']/W_L*100:+.2f} and {EFF_A/W_L*100:+.2f} per cent, against
  the contrast standing apart at {EFF_C/W_L*100:+.2f}.*

  ⚠ ** AND PART OF THAT IS A CORRECTION TO THE ORDER'S PREMISE, WHICH MIXED TWO REFERENCES. **  `r6897`
  pairs an alternation excess read against the SKY (P1/P2 = 2.264 against 2.217) with a contrast excess
  read against the CONTROL (1.040).  *Against the control, on the banked spectra, the arm's P1/P2 is
  {PK['arm'][0][1]/PK['arm'][1][1]:.4f} against {PK['control'][0][1]/PK['control'][1][1]:.4f} --
  LOWER.*  ⇒ ** The two were never pointing the same way, and the appearance that they were is the two
  references. **

  ⚑ ** ONE POSITIVE LOCALISATION, AND ITS SIGN PROBLEM WITH IT. **  The arm's dipole-to-monopole
  amplitude ratio at the visibility peak is {_dip*100:+.2f} per cent and GROWS with wavenumber, from
  {((arc/arl)[QD<6].mean()-1)*100:+.2f} to {((arc/arl)[QD>8.5].mean()-1)*100:+.2f} per cent.  ⚠ *But
  the Doppler term FILLS troughs -- `cc66.36` measured `DPSRC=0` taking the arm's oscillation from
  1.040 to 1.828 -- so a larger dipole fraction makes troughs SHALLOWER, and this arm's is larger while
  its troughs are deeper.*  ⇒ ** So the dipole fraction does not explain the contrast either; it works
  AGAINST it, which leaves a contrast excess whose source is larger than four per cent and partly
  cancelled. **  *That is a statement about size, not a mechanism, and it is as far as this order's
  measurements reach.*

  ⌗ ** AND TWO METHOD NOTES, BECAUSE BOTH WERE PLACES THIS COULD HAVE GONE WRONG QUIETLY. **  The
  offset estimator: a midpoint of successive extrema carries half the change in amplitude between them
  and came out alternating by a factor of three; the quarter-half-quarter combination of three extrema
  cancels a linear amplitude variation and left +-15 per cent of curvature; and a one-period fitting
  window is ill-conditioned because the constant is nearly collinear with the dq-weighted oscillation.
  ** Four periods with a quadratic amplitude gives a q-to-q scatter of {RD['scatter']:.4f} on an offset
  of {RD['oo']['lcdm'].mean():.4f}, and the verdict is unchanged across five settings. **  The
  alternation statistic: a second difference of peak heights vanishes only on a LINEAR trend, and the
  envelope's decline is strongly curved, so the trend and the alternation are FITTED TOGETHER.

  ⚠ ** WHAT THIS IS NOT. **  No mechanism for the contrast imbalance -- `r6897` says this order is a
  measurement and that none should be claimed, and none is.  No claim that the dipole excess produces
  the contrast excess, whose sign is wrong for it.  No claim that the offset's shortfall against -R is
  a defect of either arm: it is the same shortfall on both, and it is the approach to equilibrium.  And
  the width story `r6897` withdrew before sending is not reinstated here -- nothing in these numbers
  attacks its reasoning.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the visibility peak and its width are in the header on every path, and the arm's last
scattering is {float(g('eta_ls_w','cr'))/float(g('eta_ls_w','lcdm')):.3f} times as wide in conformal
time as the control's.  `ZPSAVE` saves the fields at that peak on the REPORTING path and is
bit-identical when unset.  The monopole's zero point sits at {RD['fracL']:.3f} and {RD['fracC']:.3f} of
each arm's own -R, and the arm's FALLS SHORT of what its own loading accounts for by an effective
omega_b of {RD['eff']/W_L*100:+.2f} per cent -- the wrong sign for the loading reading, which is
therefore refuted rather than left open.  And the two residuals r6897 asked about are not one number:
the contrast implies {EFF_C/W_L*100:+.2f} per cent and the alternation {EFF_A/W_L*100:+.2f}, opposite
signs, with the monopole offset agreeing with the alternation.  The arm's dipole-to-monopole ratio is
{_dip*100:+.2f} per cent and rising with wavenumber, and its sign works against the contrast excess
rather than for it.
NOT CLAIMED: a mechanism for the contrast imbalance; that the dipole excess produces the contrast
excess; that either arm's offset shortfall against -R is a defect.
""")
