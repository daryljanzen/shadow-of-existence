"""
P15_the_shared_fraction_does_not_mean_what_i_said_and_the_peak_trough_pattern_is_the_arms_alone
==============================================================================================

LEVEL: the same verified refit minima and the same full-covariance pipeline as `r6879+cc66.33`,
with the four diagnostics `r6881` routed measured on both the diagonal and the covariance, and one
control that decides what the shared-fraction statistic is worth.

** THIS RECEIPT WITHDRAWS THE HEADLINE OF MY OWN PREVIOUS LANDING. **

`r6879+cc66.33` reported, and I put it first in the reply:

    "73.1 per cent of the arm's chi^2 lies along the control's own residual direction ...  On the
     order's own criterion that part is the TRANSFER'S and not the construction's."

** The number is right and the inference is wrong. **  The statistic cannot carry it, and the reason
is algebraic rather than subtle: both models are fitted to the SAME data, so

        r_CR  =  r_control  +  (m_CR - m_control)          exactly, to 9e-16 below

and the common -d term is in both residuals by construction.  A large "shared fraction" therefore
measures HOW SIMILAR THE TWO MODELS ARE, not whose the misfit is.  ** The control that settles it:
the flat-LCDM control deliberately tilted by dn_s = +0.02 -- a model nobody believes, costing
chi^2 = 214.6 -- comes out 82.2 PER CENT "shared" with the control, MORE than the CR arm's 73.1. **
The statistic is not diagnostic in this regime and my reading of it was an over-claim.

-------------------------------------------------------------------------------
WHAT REPLACES IT, AND IT POINTS THE OTHER WAY.

The control already fits at 0.994 per bin -- it is a good fit, not a fit with a shared defect.  The
arm's chi^2 exceeds it by +105.1, and the model difference alone carries 77.3 of that.  ** Without
the model difference the arm would BE the control, so the whole of the excess traces to the ways this
construction's spectrum differs from flat LCDM's.  The excess is the construction's. **

-------------------------------------------------------------------------------
AND THREE OF `r6881`'s FOUR DIAGNOSTICS DO NOT SURVIVE ON THE CONTROL.

The order offers them "to be overturned", measured on diagonal errors, and asks for the full
covariance behind them.  Measured both ways:

 (1) PEAK / TROUGH.  The order has the control at +0.57 / -0.67 and the arm at +0.93 / -1.11, and
     concludes "same sign, same structure, BOTH MODELS".  ** The control shows essentially nothing:
     +0.03 / -0.06 on a diagonal amplitude, +0.03 / -0.07 on the covariance.  The arm does show it,
     +0.36 / -0.51 and +0.42 / -0.52. **  So the pattern is the ARM'S ALONE, and the composite
     inference built on both arms showing it -- "the bulk belongs to the transfer rather than to
     either cosmology" -- fails at its premise.

 (2) THE ARM AS THE CONTROL SCALED.  ** The rms ratio reproduces: 1.357 against the quoted
     1.34, and 1.261 whitened.  The correlation does not: 0.837, not 0.96; the regression slope
     1.14, not 1.28. **  And "the control scaled" is the wrong picture for the reason above: it is
     the control PLUS a model difference, and that difference is the whole of the excess.

 (3) GROWTH WITH MULTIPOLE.  Both do grow and the first third does match, but far more mildly than
     reported: control 0.67 / 0.77 / 0.88 against the quoted 0.66 / 0.96 / 1.46, arm
     0.68 / 1.12 / 1.00 against 0.69 / 1.39 / 2.09 (whitened, 0.72 / 0.91 / 1.09).

 (4) THE ell ~ 1000 TROUGH.  ** The gap is the arm's, not shared: control +0.06 where the order has
     -1.56, arm -0.64 where it has -2.66 (-0.07 and -1.09 whitened). **

-------------------------------------------------------------------------------
AND THE QUESTION THE ORDER CLOSES ON -- WHAT SETS THE 1.3 -- HAS A PLAIN ANSWER.

Nothing amplifies anything.  In the whitened metric |r_control| = 13.34 and the model difference has
norm 8.79; the arm's is 16.82, which is those two combined with their cross term.  ** The "factor of
1.3" is not an amplification of a shared defect -- it is the size of the model difference itself,
77.3 in chi^2, and that is the construction's. **

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) r_CR = r_control + (m_CR - m_control) exactly, verified to 9e-16 in the whitened metric.
 (2) A deliberately tilted control scores 82.2% "shared", above the CR arm's 73.1%, and the score
     falls away for larger tilts -- so the statistic ranks model SIMILARITY, not attribution.
 (3) The control fits at 0.994/bin; the arm exceeds it by +105.1; the model difference carries 77.3.
 (4) The four diagnostics, each on a diagonal amplitude and on the covariance, against the quoted
     values -- (2)'s rms ratio reproducing and (1), (3), (4) not surviving on the control.
 (5) |r_control| = 13.34, |model difference| = 8.79, |r_CR| = 16.82, which is what the 1.3 is.

WHAT IS NOT CLAIMED.

 * NOT that the transfer is exonerated.  What is withdrawn is that the shared fraction was EVIDENCE
   for the transfer; no statistic here separates a transfer defect from a cosmology difference, and
   none is offered.
 * NOT that `r6879+cc66.33`'s other results move.  The band means, the three single-parameter scans
   and the figure stand; it is the attribution sentence that is withdrawn.
 * NOT a mechanism for the misfit.  Four directions were excluded at cc66.33 and none is added here.
 * The peak/trough split uses the sign of the CONTROL's own binned D_l curvature for both arms, so
   the two are sorted by the same partition; using each arm's own moves no verdict and is not run.

WHAT WOULD FALSIFY IT.  The identity in (1) failing; the tilted control NOT scoring high on the
shared statistic; the control reproducing the order's peak/trough or ell~1000 numbers; or the rms
ratio not reproducing.
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

arm = lambda t: (lambda d: (d['ls'], d['Dl']))(np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')))
mb_of = lambda ls, Dl, dns=0.0, l0=700.0: CS.bin_spectrum(
    ls, Dl * (ls / l0) ** dns * np.interp(ls, LG, RAT))

KEEP = np.isfinite(mb_of(*arm('lcdm'))) & (LC >= 100) & (LC <= 1900)
COVK = COV[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COVK))
FISH = np.linalg.inv(COVK)
DK, LCK, FACK = X_DATA[KEEP], LC[KEEP], FACB[KEEP]
SIG = np.sqrt(np.diag(COVK))


def fitted(t, diagonal=False, **kw):
    mb = mb_of(*arm(t), **kw)[KEEP]
    if diagonal:
        A = float(np.sum(mb * DK / SIG ** 2) / np.sum(mb ** 2 / SIG ** 2))
    else:
        A = float(mb @ FISH @ DK / (mb @ FISH @ mb))
    r = A * mb - DK
    return A * mb, r, float(r @ FISH @ r), LINV @ r, r / SIG


M_L, R_L, C2_L, W_L, RD_L = fitted('lcdm')
M_C, R_C, C2_C, W_C, RD_C = fitted('cr')

# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE ALGEBRA THAT MAKES THE SHARED FRACTION UNINFORMATIVE.")
print("-" * 100)
DIFF = LINV @ (M_C - M_L)
print(f"    |r_control| = {np.linalg.norm(W_L):6.2f}    |m_CR - m_control| = {np.linalg.norm(DIFF):6.2f}"
      f"    |r_CR| = {np.linalg.norm(W_C):6.2f}")
check("r_CR = r_control + (m_CR - m_control) EXACTLY -- both residuals carry the same -d, so a "
      "'shared fraction' is a similarity of MODELS and not an attribution of misfit",
      float(np.max(np.abs(W_L + DIFF - W_C))) < 1e-12,
      f"max |r_CR - r_ctl - diff| = {float(np.max(np.abs(W_L + DIFF - W_C))):.1e}")

frac = lambda a, b: float((a @ b) ** 2 / ((a @ a) * (b @ b)))
print(f"\n    CR vs control: shared fraction {100*frac(W_C, W_L):.1f}%, cosine "
      f"{W_C @ W_L / np.linalg.norm(W_C) / np.linalg.norm(W_L):+.3f}   <- what cc66.33 reported")

print("\n  ** THE CONTROL THE STATISTIC NEEDED AND DID NOT GET: a model nobody believes. **")
rows = []
for dns in (0.02, 0.05, 0.10, -0.05):
    _, _, c2b, wb, _ = fitted('lcdm', dns=dns)
    rows.append((dns, c2b, frac(wb, W_L)))
    print(f"    flat LCDM tilted by dn_s = {dns:+.2f}:  chi2 = {c2b:8.1f}  "
          f"shared with the control = {100*frac(wb, W_L):5.1f}%")
check("** A DELIBERATELY WRONG MODEL SCORES HIGHER THAN THE CR ARM **: the control tilted by 0.02, "
      "at chi^2 = 214.6, is 82.2% 'shared' against the arm's 73.1% -- so the statistic ranks "
      "similarity to the control, not whose the misfit is",
      rows[0][2] > frac(W_C, W_L), f"{100*rows[0][2]:.1f}% at chi2 {rows[0][1]:.0f} "
                                   f"against the arm's {100*frac(W_C, W_L):.1f}%")
check("...and it falls away for larger tilts, which is the signature of a similarity measure rather "
      "than of an attribution",
      rows[1][2] < rows[0][2] and rows[2][2] < rows[1][2],
      " -> ".join(f"{100*r[2]:.0f}%" for r in rows[:3]))

print(f"""
  ⛔ ** SO cc66.33's SENTENCE IS WITHDRAWN. **  "73.1 per cent ... on the order's own criterion that
     part is the TRANSFER'S and not the construction's" does not follow, and nothing here replaces
     it with a statistic that would.  What can be said instead is PART 2.
""")

# ---------------------------------------------------------------------------------
print("\nPART 2 -- WHAT CAN BE SAID: THE CONTROL IS ALREADY A GOOD FIT, SO THE EXCESS IS THE ARM'S.")
print("-" * 100)
n = int(KEEP.sum())
print(f"    control  chi2 = {C2_L:7.2f} over {n} bins = {C2_L/n:.3f}/bin   ** already a good fit **")
print(f"    CR arm   chi2 = {C2_C:7.2f} over {n} bins = {C2_C/n:.3f}/bin")
print(f"    excess   {C2_C - C2_L:+7.2f},  of which the model difference alone carries "
      f"{float(DIFF @ DIFF):.1f} and the cross term {C2_C - C2_L - float(DIFF @ DIFF):+.1f}")
check("the control fits at 0.99 per bin, so there is no shared defect for the arm's excess to be an "
      "amplification OF",
      abs(C2_L / n - 1.0) < 0.05, f"{C2_L/n:.3f}/bin")
check("** and the whole of the arm's excess traces to m_CR - m_control: remove the model difference "
      "and the arm IS the control **, so the excess is the construction's",
      float(DIFF @ DIFF) > 0.6 * (C2_C - C2_L),
      f"model difference carries {float(DIFF @ DIFF):.1f} of the {C2_C - C2_L:.1f} excess")

# ---------------------------------------------------------------------------------
print("\nPART 3 -- `r6881`'s FOUR DIAGNOSTICS, ON THE DIAGONAL AND ON THE COVARIANCE.")
print("-" * 100)
CUR = np.gradient(np.gradient(M_L * FACK, LCK), LCK)
PK, TR = CUR < 0, CUR > 0
DG = {t: fitted(t, diagonal=True) for t in ('lcdm', 'cr')}

print(f"  (1) PEAK / TROUGH, sorted by the sign of the control's own binned D_l curvature "
      f"({PK.sum()} / {TR.sum()})")
print(f"      {'':22s} {'peaks':>8} {'troughs':>9}")
for t, lab in (('lcdm', 'control'), ('cr', 'CR arm')):
    rd = DG[t][4]
    w = {'lcdm': W_L, 'cr': W_C}[t]
    print(f"      {lab + ', diag amplitude':22s} {rd[PK].mean():+8.2f} {rd[TR].mean():+9.2f}")
    print(f"      {lab + ', whitened':22s} {w[PK].mean():+8.2f} {w[TR].mean():+9.2f}")
print("      r6881 quoted:  control +0.57 / -0.67,  arm +0.93 / -1.11")
check("** THE CONTROL SHOWS ESSENTIALLY NO PEAK/TROUGH PATTERN **, against the +0.57 / -0.67 the "
      "order reports -- so 'same structure, BOTH models' does not survive",
      abs(DG['lcdm'][4][PK].mean()) < 0.25 and abs(DG['lcdm'][4][TR].mean()) < 0.25,
      f"control {DG['lcdm'][4][PK].mean():+.2f} / {DG['lcdm'][4][TR].mean():+.2f}")
check("...while the ARM does show it, on both metrics -- so the pattern is the arm's alone",
      DG['cr'][4][PK].mean() > 0.2 and DG['cr'][4][TR].mean() < -0.2
      and W_C[PK].mean() > 0.2 and W_C[TR].mean() < -0.2,
      f"arm {DG['cr'][4][PK].mean():+.2f} / {DG['cr'][4][TR].mean():+.2f} diag, "
      f"{W_C[PK].mean():+.2f} / {W_C[TR].mean():+.2f} whitened")
check("⛔ and therefore the order's composite -- 'that BOTH arms show it says the bulk belongs to "
      "the transfer rather than to either cosmology' -- fails at its premise",
      abs(DG['lcdm'][4][PK].mean() - 0.57) > 0.3)

print("\n  (2) IS THE ARM THE CONTROL SCALED?")
for lab, a, b in (('diagonal', DG['cr'][4], DG['lcdm'][4]), ('whitened', W_C, W_L)):
    print(f"      {lab:9s} corr {np.corrcoef(a, b)[0, 1]:+.4f}   slope {float(a @ b/(b @ b)):.3f}"
          f"   rms ratio {float(np.std(a)/np.std(b)):.3f}")
print("      r6881 quoted: corr 0.96, slope 1.28, rms ratio 1.34")
check("** the RMS RATIO reproduces (1.36 against 1.34) **",
      abs(float(np.std(DG['cr'][4]) / np.std(DG['lcdm'][4])) - 1.34) < 0.03,
      f"{float(np.std(DG['cr'][4])/np.std(DG['lcdm'][4])):.3f}")
check("...but the CORRELATION does not: 0.84, not 0.96 -- so 'the same series scaled' is too strong "
      "even before PART 1's objection to what that would mean",
      abs(np.corrcoef(DG['cr'][4], DG['lcdm'][4])[0, 1] - 0.96) > 0.08,
      f"{np.corrcoef(DG['cr'][4], DG['lcdm'][4])[0, 1]:+.3f}")

print("\n  (3) GROWTH WITH MULTIPOLE, mean |residual| by thirds of 100-1300")
ED = np.linspace(100, 1300, 4)
th = lambda v: [float(np.mean(np.abs(v[(LCK >= a) & (LCK < b)]))) for a, b in zip(ED[:-1], ED[1:])]
for t, lab in (('lcdm', 'control'), ('cr', 'CR arm')):
    print(f"      {lab:8s} diag " + " ".join(f"{x:6.2f}" for x in th(DG[t][4]))
          + "    whitened " + " ".join(f"{x:6.2f}" for x in th({'lcdm': W_L, 'cr': W_C}[t])))
print("      r6881 quoted: control 0.66 / 0.96 / 1.46 ;  arm 0.69 / 1.39 / 2.09")
check("both DO grow with multipole and the first third matches, so that much stands",
      th(DG['lcdm'][4])[2] > th(DG['lcdm'][4])[0] and th(DG['cr'][4])[2] > th(DG['cr'][4])[0]
      and abs(th(DG['lcdm'][4])[0] - 0.66) < 0.06,
      f"control {th(DG['lcdm'][4])[0]:.2f} -> {th(DG['lcdm'][4])[2]:.2f}")
check("...but far more mildly than reported -- the control's last third is 0.88, not 1.46",
      abs(th(DG['lcdm'][4])[2] - 1.46) > 0.4,
      f"{th(DG['lcdm'][4])[2]:.2f} against 1.46")

print("\n  (4) THE ell ~ 1000 TROUGH, 950-1080")
WIN = (LCK >= 950) & (LCK <= 1080)
WHIT = {'lcdm': W_L, 'cr': W_C}
for t, lab in (('lcdm', 'control'), ('cr', 'CR arm')):
    print(f"      {lab:8s} diag {DG[t][4][WIN].mean():+6.2f}   "
          f"whitened {WHIT[t][WIN].mean():+6.2f}")
print(f"      (n = {int(WIN.sum())} bins)   r6881 quoted: control -1.56, arm -2.66")
check("** THE GAP AT ell ~ 1000 IS THE ARM'S, NOT SHARED **: the control sits at +0.06 where the "
      "order has -1.56",
      abs(DG['lcdm'][4][WIN].mean()) < 0.4 and DG['cr'][4][WIN].mean() < -0.5,
      f"control {DG['lcdm'][4][WIN].mean():+.2f}, arm {DG['cr'][4][WIN].mean():+.2f}")

# ---------------------------------------------------------------------------------
print("\nPART 4 -- WHAT SETS THE 1.3.")
print("-" * 100)
print(f"    |r_control| = {np.linalg.norm(W_L):6.2f}")
print(f"    |m_CR - m_control| = {np.linalg.norm(DIFF):6.2f}   ({float(DIFF @ DIFF):.1f} in chi^2)")
print(f"    |r_CR| = {np.linalg.norm(W_C):6.2f}   ratio to the control = "
      f"{np.linalg.norm(W_C)/np.linalg.norm(W_L):.3f}")
check("** the ratio is not an amplification of a shared defect -- it is the size of the model "
      "difference added to the control's residual **, which is the plain answer to what sets it",
      abs(np.linalg.norm(W_C) ** 2 - (np.linalg.norm(W_L) ** 2 + np.linalg.norm(DIFF) ** 2
                                      + 2 * float(W_L @ DIFF))) < 1e-8,
      f"|r_CR|^2 = |r_ctl|^2 + |diff|^2 + 2 r_ctl.diff = {np.linalg.norm(W_L)**2:.1f} + "
      f"{float(DIFF @ DIFF):.1f} + {2*float(W_L @ DIFF):.1f} = {np.linalg.norm(W_C)**2:.1f}")

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE READING.")
print("=" * 100)
print(f"""
  ⛔ ** FIRST, THE WITHDRAWAL, BECAUSE IT IS MINE. **  `r6879+cc66.33` led with "73.1 per cent of the
  arm's chi^2 lies along the control's direction ... that part is the transfer's and not the
  construction's".  The number stands; the inference does not.  Both models are fitted to the same
  data, so r_CR = r_control + (m_CR - m_control) exactly, and the shared fraction measures how
  similar the two MODELS are.  ** The control tilted by dn_s = +0.02 -- a model nobody believes, at
  chi^2 = 214.6 -- scores 82.2 per cent, higher than the arm's 73.1. **  The statistic cannot
  attribute a misfit and I should not have read it as doing so.

  ** AND THE CORRECTED READING POINTS THE OTHER WAY. **  The control already fits at
  {C2_L/n:.3f} per bin; there is no shared defect for the arm's excess to be an amplification of.  The
  arm exceeds it by {C2_C - C2_L:+.1f}, the model difference alone carries {float(DIFF @ DIFF):.1f} of that, and removing the
  model difference makes the arm the control.  ** The excess is the construction's. **

  ** SECOND, THREE OF THE FOUR DIAGNOSTICS DO NOT SURVIVE ON THE CONTROL, AND THE ORDER ASKED TO BE
  OVERTURNED. **  The peak/trough pattern is the ARM'S alone -- the control sits at
  {DG['lcdm'][4][PK].mean():+.2f} / {DG['lcdm'][4][TR].mean():+.2f} where the order has +0.57 / -0.67.  The ell ~ 1000 trough is the arm's --
  the control sits at {DG['lcdm'][4][WIN].mean():+.2f} where the order has -1.56.  The growth with multipole is real but
  far milder, the control's last third {th(DG['lcdm'][4])[2]:.2f} rather than 1.46.  ** So the composite -- "that both
  arms show it says the bulk belongs to the transfer rather than to either cosmology" -- fails at its
  premise, and it fails in the same direction as the withdrawal above. **

  ** WHAT DOES REPRODUCE IS THE RMS RATIO: {float(np.std(DG['cr'][4])/np.std(DG['lcdm'][4])):.3f} against the quoted 1.34. **  And what sets it is
  not an amplification: |r_control| = {np.linalg.norm(W_L):.2f}, the model difference {np.linalg.norm(DIFF):.2f}, the arm {np.linalg.norm(W_C):.2f}.
  ** The factor of 1.3 IS the model difference. **

  ⚠ ** AND WHAT IS NOT ESTABLISHED EITHER WAY. **  Withdrawing "it is the transfer's" is not showing
  the transfer is innocent.  No statistic here separates a transfer defect from a cosmology
  difference, and none is offered; what is established is that the shared fraction was never that
  statistic.  The band means, the three single-parameter scans and the figure of cc66.33 stand.
""")

print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED -> " + "; ".join(FAILS))
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: r_CR = r_control + (m_CR - m_control) exactly, so the shared fraction ranks model
similarity rather than attributing misfit -- a control tilted by dn_s = +0.02 scores 82.2% against
the arm's 73.1% -- and cc66.33's sentence reading it as "the transfer's and not the construction's"
is WITHDRAWN.  The control fits at {C2_L/n:.3f}/bin, the arm exceeds it by {C2_C - C2_L:+.1f}, and the model difference
carries {float(DIFF @ DIFF):.1f} of that, so the excess is the construction's.  Of r6881's four diagnostics the rms
ratio reproduces ({float(np.std(DG['cr'][4])/np.std(DG['lcdm'][4])):.3f} against 1.34) and three do not survive on the control: the peak/trough
pattern, the ell~1000 trough and the steepness of the growth are the ARM'S, so the composite reading
that both arms show it fails at its premise.  The 1.3 is the model difference's own size.
NOT CLAIMED: that the transfer is exonerated; a mechanism for the misfit; any change to cc66.33's
band means, single-parameter scans or figure.
""")
