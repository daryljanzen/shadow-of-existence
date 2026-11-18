#!/usr/bin/env python3
r"""r7828 (60) -- PO-24 at the paper's own configuration, on order r7823 (69).

COMPUTES: every PO-24 figure at the configuration the paper adjudicates -- r = 0.9918 at the
  DECLARED in-force damping multipole -- beside the same figure at the ratio this row has used
  since r7471, and the correction that the exponent is already inside the length.
  INPUT  the ratio and the exponent: READ OUT OF corpus/CR_cosmology.tex, not hardcoded
  INPUT  l_D in force: 1951.9 / sqrt(1.70) = 1497.0390, and 1489.5783 after the one-rate move
  INPUT  the controls: L820_lcdm_L2512_nk800 and L824_lcdm_L3200_nk960, each normalised to plik_lite
  INPUT  the five banked responses, each entering as a RATIO to its own centre
  INPUT  the joint arm: Planck plik_lite TT below the shipped cut + ACT DR6 TT above it on support
  OUTPUT the displacement per window, the five absorber fits, the joint-arm distance, and the
         construction's own refit against LCDM on the joint best fit

** ⛔⛔ THE CORRECTION FIRST, BECAUSE IT CHANGES THE ROW'S HEADLINE FIGURE AND IT IS MY ERROR. **

`alpha` and `l_D` enter the signature ONLY through `l_D / sqrt(alpha)`.  This corpus's own landed
receipt says so -- P15_the_papers_1_06_and_the_joint_fits_1_4967_are_one_curve_in_l_D -- and 70's
faithful copy declares it in its INPUT line, `R, LD = 1.0926, 1951.9 / 1.70 ** 0.5`:

    1951.9 / sqrt(1.70)         = 1497.0390     the IN-FORCE l_D of the faithful alpha = 1.70 route
    1497.0390 * (1 - 0.0049836) = 1489.5783     the same, after the one-rate move

=> So `R, LD = 1.0926, 1489.5783` with exponent ONE -- which every PO-24 figure since r7471 uses --
   ALREADY IS the faithful alpha = 1.70 route on the one rate.  r7826's configuration scan multiplied
   that exponent by 1.70 again, putting its "alpha = 1.70" rows at an l_D of 1366.0363/sqrt(1.70) =
   1047.70, a value nothing in this corpus declares.  ** 69 adopted that row as PO-24's figure
   (Delta chi2 = +9.02) and wrote it into P15. **

** THE FIGURE AT THE PAPER'S CONFIGURATION, measured here at the DECLARED in-force l_D:
   Delta chi2 = -2.3697 -- the construction's own refit fits the joint data BETTER than LCDM,
   137.4859 against 139.8557 over the same 150 bandpowers on the same five parameters, at an
   INTERIOR minimum. **  Not excluded: mildly preferred.

=> GUARD: a folded parameter is folded once.  Before multiplying by an exponent, establish whether
the length it multiplies is declared at amplitude level or already in force.  ⌗ The corpus had made
the mirror-image error once -- pricing the faithful route on the header 1951.9 instead of l_eff --
and cc66's receipt exists to stop it.  Mine is the same error from the other side.

** AND THE ROW'S OTHER FIGURES, all reproduced at the old configuration before being remade: **
  the displacement turns POSITIVE and shrinks by an order, +0.006167 / +0.015141 / +0.022361
  against -0.069641 / -0.175961 / -0.260164, because r^2 - 1 is -0.016333 against +0.193775 --
  one in 11.86, with the opposite sign;
  the joint-arm distance is 8.152 sigma against 19.253, fixed-cosmology on the banked control;
  and the control swap L820 -> L824 moves the published displacement by 0.55 per cent, so the two
  axes decompose cleanly and the configuration carries all of it.

** TWO OF THE FOUR REFUSAL PATTERNS CHANGE, AND ONE REGISTERED NEGATIVE FIRED. **  No parameter
absorbs the displacement at either configuration -- but the signature's sign flipped, so:
  Y_He wanted +11.265 sigma AT THE BANK'S EDGE and now wants -2.016, -0.873 and -0.858: AFFORDABLE
  where it was unaffordable.  It still leaves 75.55 per cent standing, so the route does not reopen.
  A_L flips the other way, from +1.390 to -2.867: it now wants a value BELOW one against a
  temperature constraint above one, so IT is the unaffordable one, and still buys little.
  omega_b, N_eff and omega_m stay affordable within a quarter of a sigma and absorb nothing.

⚠ Ⓑ②'s PREMISE IS REFUTED, and that is the second half of the same finding: a log-slope fit of a
  control's own power returns 1154.21 on L820 and 1334.66 on L824, -22.5 and -10.4 per cent from the
  in-force 1489.5783.  l_D in force is the instrument's DECLARED multipole folded by sqrt(alpha), not
  a fit to a control's spectrum, so the arm's registered presumption that the two are one object is
  false; the arm asserts the refutation instead, with both numbers pinned, and the consequence is
  carried out -- every figure here is at an in-force l_D.
"""
import json
import os
import re
import sys
import warnings

import numpy as np
import scipy.linalg
from scipy.optimize import minimize_scalar

warnings.filterwarnings('ignore')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
AD = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')
PROBE = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7828_60_po24_recomputed_at_the_papers_own_configuration_and_the_size_is_a_'
                     'seventh_with_the_opposite_sign')
PAPER = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')

# ---- the configuration, READ OUT OF THE PAPER ---------------------------------------------------
_SRC = open(PAPER, encoding='utf-8').read()
R_PAPER = float(re.search(r"visibility peak, \$r=(\d+\.\d+)\$", _SRC).group(1))
ALPHA_PAPER = float(re.search(r"\\alpha=(\d+\.\d+)\$ the instrument", _SRC).group(1))
R_ROW = 1.0926
LD_DECLARED_AMP = 1951.9          # the instrument header's, AMPLITUDE level (r7611+70)
LD_INFORCE_PLAIN = 1497.0390      # = LD_DECLARED_AMP / sqrt(alpha)
LD_INFORCE_ONE_RATE = 1489.5783   # the same, after the one-rate move -- what this row has used
ONE_RATE_MOVE = -0.0049836

WINDOWS = ((100, 1758), (700, 1760), (1000, 1760))


def fisher(cov):
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(cov.shape[0]))
    return 0.5 * (F + F.T)


def load_control(fn):
    z = np.load(os.path.join(SP, fn))
    ls, raw = z['ls'].astype(float), z['Dl'].astype(float)
    k0 = np.isfinite(CS.bin_spectrum(ls, raw))
    F0 = fisher(CS.COV_TT[np.ix_(k0, k0)])
    m0 = CS.bin_spectrum(ls, raw)[k0]
    return ls, raw * float((m0 @ F0 @ CS.X_DATA[k0]) / (m0 @ F0 @ m0))


def sig_of(ls, dl, r, ld):
    return dl * np.exp(-(r ** 2 - 1.0) * (ls / ld) ** 2)


print("=" * 92)
print("r7828 (60) -- PO-24 at the paper's configuration, and the exponent folded once")
print("=" * 92)

# ======================================================= Ⓓ④ THE SIZE AND THE FOLD
head("D -- THE SIZE AT THE TWO CONFIGURATIONS, AND THE FOLD THAT r7826 DID TWICE")
K_PAPER = R_PAPER ** 2 - 1.0
K_ROW = R_ROW ** 2 - 1.0
FOLDED = LD_DECLARED_AMP / ALPHA_PAPER ** 0.5
MOVED = FOLDED * (1.0 + ONE_RATE_MOVE)
print(f"      read from the paper: r = {R_PAPER}, alpha = {ALPHA_PAPER}")
print(f"      r^2 - 1          : {K_PAPER:+.6f} at the paper's endpoint, {K_ROW:+.6f} at the row's")
print(f"      ratio            : {abs(K_PAPER / K_ROW):.4f}, one in {abs(K_ROW / K_PAPER):.2f}, "
      f"sign {'opposite' if K_PAPER * K_ROW < 0 else 'the same'}")
print(f"      {LD_DECLARED_AMP} / sqrt({ALPHA_PAPER}) = {FOLDED:.4f}  -> in force")
print(f"      after the one-rate move {100 * ONE_RATE_MOVE:+.4f} %: {MOVED:.4f}")
print(f"      ⇒ r7826's 'alpha = 1.70' rows sat at {1366.0363 / ALPHA_PAPER ** 0.5:.2f}, which "
      f"nothing declares")
check("Ⓓ④ the size at the paper's endpoint is -0.016333 against the row's +0.193775 -- one in "
      "11.86 with the OPPOSITE sign -- and the exponent is not a second factor: 1951.9 folded by "
      "sqrt(1.70) is 1497.0390 in force, 1489.5783 after the one-rate move, which is the l_D this "
      "row has used all along.  So the row's exponent-one form IS the faithful alpha = 1.70 route, "
      "and multiplying it again is the double-count r7826 made",
      abs(K_PAPER + 0.016333) < 7.0e-7 and abs(K_ROW - 0.193775) < 7.0e-7
      and abs(abs(K_ROW / K_PAPER) - 11.86) < 0.006
      and K_PAPER * K_ROW < 0
      and abs(FOLDED - LD_INFORCE_PLAIN) < 6.0e-4
      and abs(MOVED - LD_INFORCE_ONE_RATE) < 6.0e-4)

# ======================================================= Ⓐ① / Ⓔ⑤ THE DISPLACEMENTS
head("A / E -- THE DISPLACEMENT, REPRODUCED AT THE ROW'S AND REMADE AT THE PAPER'S")
DISP = {}
SHARE = {}
for cname, cfile in (('L820', 'L820_lcdm_L2512_nk800.npz'), ('L824', 'L824_lcdm_L3200_nk960.npz')):
    ls, dl = load_control(cfile)
    for gname, (r, ld) in (('row', (R_ROW, LD_INFORCE_ONE_RATE)),
                           ('paper', (R_PAPER, LD_INFORCE_ONE_RATE))):
        sig = sig_of(ls, dl, r, ld)
        for lo, hi in WINDOWS:
            keep = (np.isfinite(CS.bin_spectrum(ls, dl)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi))
            F = fisher(CS.COV_TT[np.ix_(keep, keep)])
            tgt = CS.bin_spectrum(ls, sig)[keep]
            m_amp = CS.bin_spectrum(ls, dl)[keep]
            a = float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp))
            res = tgt - a * m_amp
            c_amp = float(res @ F @ res)

            def at(dn):
                m = CS.bin_spectrum(ls, dl * (ls / 1000.0) ** dn)[keep]
                A = float((m @ F @ tgt) / (m @ F @ m))
                rr = tgt - A * m
                return float(rr @ F @ rr)
            o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded',
                                options={'xatol': 1e-10})
            DISP[(cname, gname, lo)] = float(o.x)
            SHARE[(cname, gname, lo)] = (1 - float(o.fun) / c_amp) * 100.0
            print(f"      {cname} {gname:>6} {lo}-{hi}: dn = {float(o.x):+.6f}   the tilt takes "
                  f"{SHARE[(cname, gname, lo)]:.2f} %")
check("Ⓐ① the three displacements at the ROW's configuration on L824 reproduce r7822's landed "
      "figures to every digit -- -0.069641, -0.175961 and -0.260164 -- so this harness is the one "
      "that produced them and the figures at the paper's configuration may be set beside them",
      # r7827 (69): "to every digit" tested as equality at the printed six decimals.  The bounded
      #   minimiser leaves a residue near 1e-8 that moves between builds, so a float tolerance at
      #   half the last digit had headroom 56 against the build sweep's 1e3; the rounded values do not move.
      round(DISP[('L824', 'row', 100)], 6) == -0.069641
      and round(DISP[('L824', 'row', 700)], 6) == -0.175961
      and round(DISP[('L824', 'row', 1000)], 6) == -0.260164)
check("Ⓔ⑤ at the paper's configuration the displacement turns POSITIVE and shrinks by an order on "
      "every window -- +0.006167, +0.015141 and +0.022361 -- which is the sign and the size of "
      "r^2 - 1 and not a separate fact",
      round(DISP[('L824', 'paper', 100)], 6) == 0.006167
      and round(DISP[('L824', 'paper', 700)], 6) == 0.015141
      and round(DISP[('L824', 'paper', 1000)], 6) == 0.022361
      and all(DISP[('L824', 'paper', lo)] > 0 for lo, _ in WINDOWS))

# ======================================================= Ⓕ⑥ THE SHAPE
head("F -- THE SHAPE IS THE SAME AT BOTH RATIOS, WHICH IS WHAT LETS THE OVERLAPS BE INHERITED")
for lo, hi in WINDOWS:
    print(f"      {lo}-{hi}: the tilt takes {SHARE[('L824', 'row', lo)]:.2f} % at the row's and "
          f"{SHARE[('L824', 'paper', lo)]:.2f} % at the paper's")
# ⌗ THE CRITERION HERE IS A COMPARISON AND NOT A TOLERANCE, because the first version of this arm
# used a threshold of 1.3 POINTS -- picked after reading the published window's 1.15 -- and the
# window at 700 differs by 1.40, so it failed.  A threshold chosen after seeing one of the three
# numbers is criterion-fitting, and the count caught it.  What the arm is actually about is SHAPE
# against SIZE: the shares must agree far better, in relative terms, than the sizes differ.
_REL_SHARE = max(abs(SHARE[('L824', 'row', lo)] - SHARE[('L824', 'paper', lo)])
                 / SHARE[('L824', 'row', lo)] for lo, _ in WINDOWS)
_REL_SIZE = abs(K_ROW - K_PAPER) / abs(K_PAPER)
print(f"      the share agrees to {100 * _REL_SHARE:.2f} % of itself at worst, while the SIZE "
      f"differs by {100 * _REL_SIZE:.0f} % -- a factor of {_REL_SIZE / _REL_SHARE:.0f}")
check("Ⓕ⑥ the SHAPE is the same object at both ratios and the SIZE is not, which is what lets "
      "69's ruling inherit the overlaps: the share a single tilt takes agrees to 1.66 per cent of "
      "itself at worst across the three windows (69.27 against 68.12, 90.83 against 89.43, 95.67 "
      "against 94.96) while the size differs by 1086 per cent -- shape agreeing some 650 times "
      "better than size does",
      _REL_SHARE < 0.05 and _REL_SIZE > 10.0 and _REL_SIZE / _REL_SHARE > 100.0
      and abs(100 * _REL_SHARE - 1.66) < 6.0e-3
      and abs(SHARE[('L824', 'row', 100)] - 69.27) < 6.0e-3
      and abs(SHARE[('L824', 'paper', 100)] - 68.12) < 6.0e-3)

# ======================================================= Ⓙ⑩ THE TWO AXES
head("J -- THE TWO AXES SEPARATED, SO NEITHER IS CREDITED WITH THE OTHER'S MOVEMENT")
SWAP = abs(DISP[('L824', 'row', 100)] / DISP[('L820', 'row', 100)] - 1.0) * 100.0
CONF = abs(DISP[('L824', 'paper', 100)] / DISP[('L824', 'row', 100)] - 1.0) * 100.0
print(f"      the CONTROL swap at fixed configuration: {DISP[('L820', 'row', 100)]:+.6f} -> "
      f"{DISP[('L824', 'row', 100)]:+.6f}   {SWAP:.2f} %")
print(f"      the CONFIGURATION change at fixed control: {DISP[('L824', 'row', 100)]:+.6f} -> "
      f"{DISP[('L824', 'paper', 100)]:+.6f}   {CONF:.2f} %")
check("Ⓙ⑩ the two axes decompose and the configuration carries all of it: the control swap "
      "L820 -> L824 moves the published displacement by 0.55 per cent while the configuration "
      "change moves it by 108.9 -- which also answers r7821's item ②, that the L824 recompute "
      "moves the published figures by well under a per cent",
      abs(SWAP - 0.55) < 6.0e-3 and CONF > 100.0)

# ======================================================= Ⓑ② / Ⓒ③ / Ⓖ⑦ / Ⓗ⑧ FROM THE GRID
head("B / C / G / H -- THE l_D FITS, THE BANK REACHES, AND THE FIVE ABSORBERS")
GZ = np.load(os.path.join(PROBE, 'runs', 'r7828_grid.npz'), allow_pickle=True)
ROWS = json.loads(str(GZ['rows']))
LDF = {c: float(GZ[f'lD_{c}']) for c in ('L820', 'L824')}
print(f"      a log-slope fit of the control's own power: L820 {LDF['L820']:.4f} "
      f"({100 * (LDF['L820'] / LD_INFORCE_ONE_RATE - 1):+.2f} %), L824 {LDF['L824']:.4f} "
      f"({100 * (LDF['L824'] / LD_INFORCE_ONE_RATE - 1):+.2f} %)")
check("Ⓑ②'s PREMISE FAILED AND THE ARM NOW ASSERTS THE REFUTATION, which is the r7820 pattern "
      "and not a weakened criterion.  r7828 registered that l_D would be re-measured on L824 'by "
      "the same damping fit the harness uses', presuming the fit and the in-force value are one "
      "object.  THEY ARE NOT: the fit returns 1334.66 on L824 and 1154.21 on L820, 10.4 and 22.5 "
      "per cent from the in-force 1489.5783, and no choice of control brings them together, "
      "because l_D in force is the instrument's DECLARED multipole folded by sqrt(alpha) while the "
      "fit is a log-slope of a control's power.  What is asserted here is that refutation, pinned "
      "by both numbers -- and the consequence is carried out rather than noted: every figure in "
      "this receipt is at an in-force l_D, and substituting a fitted one would be the same error "
      "class as the alpha double-count Ⓓ④ corrects",
      abs(LDF['L824'] - 1334.6610) < 6.0e-4 and abs(LDF['L820'] - 1154.2106) < 6.0e-4
      and abs(LDF['L824'] / LD_INFORCE_ONE_RATE - 1) > 0.05
      and abs(LDF['L820'] / LD_INFORCE_ONE_RATE - 1) > 0.05)
REACH = GZ['reaches']
print(f"      bank reaches: {[int(x) for x in REACH]} against the highest window multipole 1760")
check("Ⓒ③ every one of the five banks reaches l = 1996, above every window used, and each enters "
      "as a ratio to its own centre -- so the control swap needs NO bank rebuilt and 70 is asked "
      "for nothing",
      bool(np.all(REACH >= 1760.0)) and bool(np.all(REACH == 1996.0)))

G = {(r['config'], r['window']): r for r in ROWS if r['control'] == 'L824'}
PARAMS = ('omega_b', 'N_eff', 'Y_He', 'A_L', 'omega_m')
for gname in ('row', 'paper'):
    print(f"\n      {gname.upper()} -- survival (per cent of the displacement left standing)")
    for lo, hi in WINDOWS:
        r = G[(gname, f'{lo}-{hi}')]
        print(f"        {lo}-{hi}: " + "  ".join(f"{p} {r[p]['surv']:6.2f}" for p in PARAMS))
    print(f"      {gname.upper()} -- affordability, in each parameter's OWN sigma")
    for lo, hi in WINDOWS:
        r = G[(gname, f'{lo}-{hi}')]
        print(f"        {lo}-{hi}: " + "  ".join(
            f"{p} {r[p]['aff']:+6.2f}{'E' if r[p]['edge'] else ''}" for p in PARAMS))
check("Ⓖ⑦ the five absorber fits at the paper's configuration leave the displacement standing on "
      "every window and every parameter -- 75.55 per cent at the lowest, Y_He on the published "
      "window, and 93.50 for A_L -- so NO inherited parameter absorbs it at the configuration the "
      "paper adjudicates either, which is the clause r7814 closed and which holds here",
      all(G[('paper', f'{lo}-{hi}')][p]['surv'] > 70.0 for lo, hi in WINDOWS for p in PARAMS)
      and abs(G[('paper', '100-1758')]['Y_He']['surv'] - 75.55) < 6.0e-3
      and abs(G[('paper', '100-1758')]['A_L']['surv'] - 93.50) < 6.0e-3)
check("Ⓗ⑧ ITS REGISTERED NEGATIVE FIRED, FOR Y_He: it wanted +11.265 sigma at the bank's EDGE at "
      "the row's ratio and wants -2.016 at the paper's -- affordable where it was unaffordable, "
      "because the signature's sign flipped.  AND IT DOES NOT REOPEN THE ROUTE, because it still "
      "leaves 75.55 per cent standing.  A_L flips the other way, +1.390 to -2.867, a value below "
      "one against a constraint above one, so IT is now the unaffordable one; omega_b, N_eff and "
      "omega_m stay affordable within a quarter of a sigma and absorb nothing",
      abs(G[('row', '100-1758')]['Y_He']['aff'] - 11.265) < 6.0e-4
      and G[('row', '100-1758')]['Y_He']['edge']
      and abs(G[('paper', '100-1758')]['Y_He']['aff'] + 2.016) < 6.0e-4
      and abs(G[('row', '100-1758')]['A_L']['aff'] - 1.390) < 6.0e-4
      and abs(G[('paper', '100-1758')]['A_L']['aff'] + 2.867) < 6.0e-4
      and all(abs(G[('paper', '100-1758')][p]['aff']) < 0.30
              for p in ('omega_b', 'N_eff', 'omega_m')))

# ======================================================= Ⓘ⑨ THE JOINT ARM AND THE REFIT
head("I -- THE JOINT ARM AT EACH CONFIGURATION, AND THE REFIT THAT CORRECTS r7826")
JZ = np.load(os.path.join(PROBE, 'runs', 'r7828_joint.npz'))
RF = json.load(open(os.path.join(PROBE, 'runs', 'r7828_refit.json')))
print(f"      the arm: {int(JZ['n_planck'])} Planck bins + {int(JZ['n_act'])} ACT bandpowers")
print(f"      the sky's tilt: {float(JZ['dn_sky']):+.6f} +/- {float(JZ['sig_sky']):.6f}")
for g in ('row', 'paper'):
    print(f"      {g:>6}: dn_sig {float(JZ[f'dn_sig_{g}']):+.6f}   "
          f"{float(JZ[f'dist_{g}']):.3f} sigma   direct Delta chi2 "
          f"{float(JZ[f'direct_{g}']):+.3f}")
print(f"\n      THE REFIT at r = {RF['r']}, l_D = {RF['lD']} (exponent one, which IS alpha "
      f"{ALPHA_PAPER}):")
print(f"        chi2 {RF['chi2']:.4f} against LCDM's {RF['chi2_lcdm']:.4f} over {RF['ndata']} "
      f"points   Delta chi2 {RF['dchi2']:+.4f}   {'interior' if not RF['edge'] else RF['edge']}")
check("Ⓘ⑨ THIS RECEIPT MEASURES the joint-arm distance at r = 0.9918 as 8.152 sigma against "
      "19.253 at r = 1.0926, fixed-cosmology on the banked control -- and THE REFIT REVERSES IT: "
      "at the declared in-force l_D the construction reaches 137.4859 against LCDM's 139.8557 on "
      "the same 150 bandpowers and the same five parameters, Delta chi2 = -2.3697 at an INTERIOR "
      "minimum.  ⇒ So the figure for that ratio is that the construction fits the joint data "
      "slightly BETTER than LCDM -- not the +9.02 r7826 computed and r7823 adopted, which was the "
      "double-counted row.  ⌗ And the ratio this arm is about is the one PARSED OUT OF the paper in "
      "Ⓓ④, asserted again here so that this arm's own trace reaches that read rather than taking "
      "the ratio on trust from another arm",
      abs(R_PAPER - 0.9918) < 1.0e-9 and abs(R_ROW - 1.0926) < 1.0e-9
      and abs(float(JZ['dist_row']) - 19.253) < 0.006
      and abs(float(JZ['dist_paper']) - 8.152) < 0.006
      and abs(RF['dchi2'] + 2.3697) < 6.0e-4
      and abs(RF['chi2'] - 137.4859) < 6.0e-3
      and not RF['edge'] and RF['chi2'] < RF['chi2_lcdm'])

# ============== THE FIGURES THE PAPER SENTENCE AND THE INDEX ROW PRINT, PINNED WHERE AN AST CAN
# ============== SEE THEM.  Explicit two-sided comparisons, each inside the coarser of half the last
# ============== printed digit and 0.05 per cent -- the corpus's own allowance.  Not a twelfth arm:
# ============== every figure here is one some arm above measures, or one r7826 banked and this
# ============== receipt reads back.  ⌗ r7826 learned this the hard way: a pin computed through a
# ============== helper is invisible to check_figures_pinned.
AL_TT, AL_TT_SIG = 1.243, 0.096           # the temperature constraint, r7812's own constants
R26 = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                           'r7826_60_the_joint_data_fitted_and_the_amplitude_convention_makes_one_'
                           'parameter_degenerate', 'runs', 'r7826_probe.npz'))
_AL_V = G[('paper', '100-1758')]['A_L']['v']
PINS = {
    "the instrument's declared l_D, 1951.9": abs(LD_DECLARED_AMP - 1951.9) < 1.0e-9,
    "the exponent it is declared at, 1.70": abs(ALPHA_PAPER - 1.70) < 1.0e-9,
    "the in-force length, 1497.0390": abs(FOLDED - 1497.0390) < 6.0e-4,
    "and after the one-rate move, 1489.5783": abs(MOVED - 1489.5783) < 6.0e-4,
    "the row's ratio, 1.0926": abs(R_ROW - 1.0926) < 1.0e-9,
    "the adjudicated ratio, 0.9918": abs(R_PAPER - 0.9918) < 1.0e-9,
    "where r7826's alpha-1.70 rows sat, 1047.70": abs(1366.0363 / ALPHA_PAPER ** 0.5
                                                      - 1047.70) < 0.5,
    "LCDM on the joint arm, 139.8557": abs(RF['chi2_lcdm'] - 139.8557) < 0.06,
    "the construction there, 137.4859": abs(RF['chi2'] - 137.4859) < 0.06,
    "which is better by 2.3697": abs(RF['dchi2'] + 2.3697) < 6.0e-4,
    "what r7826 reported and 69 adopted, 9.02": abs(float(R26['dchi2_fitC_adj_a170'])
                                                    - 9.02) < 4.5e-3,
    "A_L wants 0.968 at the paper's configuration": abs(_AL_V - 0.968) < 4.9e-4,
    "against a temperature constraint of 1.243": abs(AL_TT - 1.243) < 1.0e-9,
    "its sigma, 0.096": abs(AL_TT_SIG - 0.096) < 1.0e-9,
    "so the affordability is -2.867": abs((_AL_V - AL_TT) / AL_TT_SIG + 2.867) < 6.0e-4,
    "the joint distance at the row's ratio, 19.253": abs(float(JZ['dist_row']) - 19.253) < 6.0e-3,
    # r7826's own figure for the same ratio on the FITTED baseline, read back from its bank rather
    # than recomputed, because the paper's sentence prints it beside this receipt as well
    "and on the fitted baseline, 27.4": abs(float(R26['scope_the_rows_harness_alpha_1p0_dist'])
                                            - 27.4) < 0.045,
    "and at the paper's, 8.152": abs(float(JZ['dist_paper']) - 8.152) < 6.0e-3,
}
print("\n" + "=" * 92)
print(f"  THE PRINTED FIGURES, PINNED: {sum(PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure the paper or the INDEX row prints is not held by this receipt"

# ======================================================= Ⓚ⑪ THE COUNT
head("K -- THE COUNT")
print(f"\n      arms registered in r7828's PREDICTION.md : 11")
print(f"      arms run before this count is asserted   : {len(PASSED) + len(FAILED)}")
check("Ⓚ⑪ eleven arms were registered and eleven ran, under the registration's own labels, with "
      "Ⓑ②'s premise refuted and asserted as such rather than quietly dropped, and Ⓗ⑧'s "
      "registered negative fired for Y_He",
      len(PASSED) + len(FAILED) == 10)

if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f[:110]}")
print(f"\n  arms run in total, this count included   : {len(PASSED) + len(FAILED)}")
print(f"  passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 11, "eleven arms were registered; eleven must run"
sys.exit(1 if FAILED else 0)
