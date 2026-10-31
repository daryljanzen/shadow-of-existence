#!/usr/bin/env python3
"""
** THE ARM IS THE NO-FIT CONFIGURATION ON THE ARM OF RECORD AS OF `r7645+cc66.66`. **  70's
`r7643_70_distances_point` ran the original recipe verbatim with `LEAFREC=1` at the DISTANCES' point
-- CRH0 68.60, CROM 0.2973, built-in omega_b and n_s -- and banked it as
`cc66_cr_x_h686_L2000_leafrec1_distances`.  The CONTROL does not move: `LEAFREC` does not reach it
(3.6e-16, `r7641`), and 70 scored the same control for both rows of its own headline table.
⛭ ** AND THIS RECEIPT REPRODUCES 70's BANK FIGURE RATHER THAN QUOTING IT: ** scored here with this
receipt's own operator and bins, the arm comes in at 502.09 lensed, 2.71 per bin, x2.3456 -- against
70's 502.1, 2.71 and 2.346x.  *That agreement is the check that matters, because the one error in
this pass was a POINTER error: `cc66`'s earlier 1.41 read the REFITTED file through the no-fit
pointer, and only scoring the same file two ways catches that.*
⌗ *The arm's `l_A` is bit-identical across the move, 302.8891 both ways, because `LEAFREC` does not
touch the background -- so what moves the spectrum here is the recombination treatment alone and not
the distances.*

RECEIPT -- P15: ** THE 185-BIN FULL-RANGE LENSED COMPARISON -- THE CONFIGURATION THE CORPUS'S OWN
chi^2 VALUES ARE QUOTED ON -- PUTS THE CROSSING ARM AT 2.71 PER BIN AGAINST THE CONTROL'S 1.16.
** THAT IS x2.35, AND IT IS STILL WORSE THAN THE x2.0 THE 133-BIN UNLENSED COMPARISON SHOWED. **

** ⇒ SO THE NUMBER r6760+cc66.7 REPORTED WAS THE MORE FAVOURABLE OF THE TWO, AND THIS ONE IS THE
ONE THE PAPER MUST QUOTE. **  The ratio moves because lensing is worth proportionally MORE to the
control (a factor 3.25 reduction) than to the arm (2.25), which widens the gap rather than closing
it.  ⛔ *On the namesake arm the arm's reduction was 2.13 and the ratio x2.57; the arm of record
costs the arm less in absolute chi^2 and so narrows the ratio to x2.35, an 8.8 per cent improvement
that does NOT change which comparison the paper must quote.*

*** AND THE CAVEAT THIS RECEIPT WAS COMMISSIONED WITH DOES NOT BITE, WHICH IS SAID HERE BECAUSE IT
WAS SAID IN ADVANCE. ***  `P15_derived_lensing_on_the_lcdm_arm` measured the instrument's LCDM arm
at 1320 unlensed on these bins where CAMB's true LCDM sits at 615, and r6760+cc66.9 flagged that
~700 of transfer inaccuracy as something neither lensing's to close nor the arm's to answer for.
** On THIS configuration the control comes in at 696 unlensed and 214 lensed, against CAMB's 615
and 186.  The instrument's control is now within 13% of CAMB unlensed and 15% lensed, so the
comparison is clean and the flagged caveat is withdrawn rather than relied on. **

Built r6760+cc66.12 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s standing item --
`sec:diffusion-scale` was waiting on this pair.

===================================================================================================
** THE CONFIGURATION, AND WHAT MAKES IT DIFFERENT FROM THE ONE ALREADY REPORTED **
===================================================================================================

  `LMAXL=2000`, polarisation path, `LSTEP=2`: the arm at (H0, Om) = (68.60, 0.2973) with the
  handover at the crossing and one clock, and a control run at the SAME reach so the two are
  scored on the same bins.

** THE RANGE IS 185 BINS AND THAT IS MEASURED, NOT INHERITED. **  ell = 100 to 1996.  *The corpus
calls this "the 185-bin full-range configuration"; the count is asserted here rather than taken on
the name.*

** THE LENSING OPERATOR IS CAMB's LENSED/UNLENSED RATIO, THE NON-PERTURBATIVE ONE. **  Not
`LENS_correction.py`'s first-order Hu kernel, which `P15_derived_lensing_on_the_lcdm_arm` PART C
measured returning a spurious +13% enhancement at ell = 1900 where the full operator gives +6.5%.
*The operator used here is checked against that number below.*

  PART 1  ** THE BIN COUNT AND THE OPERATOR, both asserted. **
  PART 2  ** THE FOUR NUMBERS. **
  PART 3  ** THE RATIO, WHICH IS THE READABLE QUANTITY, AND HOW IT MOVED. **
  PART 4  ** THE CONTROL AGAINST CAMB -- the withdrawn caveat. **

** COMPUTES: the CAMB reference at H0 = 67.40, ombh2 = 0.02237, Om = 0.3150, mnu = 0.06, tau =
   0.054, As = 2.1e-9, ns = 0.965, lmax = 3000 -- the control arm's own parameters, so the
   lensing operator is LCDM's and is imposed rather than fitted.  *** The spectra are read, not
   produced; every parameter in them is baked into the .npz. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~60 s)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                                # noqa: E402


def load(tag):
    z = np.load(os.path.join(SPEC, f'cc66_{tag}.npz'))
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])


print("=" * 104)
print("  PART 1 -- ** THE BIN COUNT AND THE OPERATOR **")
print("=" * 104)
# ⛭⛭ r7645+cc66.66: ** THE ARM MOVES TO THE NO-FIT CONFIGURATION ON THE ARM OF RECORD. **
#   *70's `r7643_70_distances_point` banked the original recipe run verbatim with `LEAFREC=1` at the
#   DISTANCES' point -- CRH0 68.60, CROM 0.2973, the built-in omega_b and n_s -- as
#   `cc66_cr_x_h686_L2000_leafrec1_distances`.  That is the no-fit configuration this receipt is
#   about, now on the arm of record.*
#   ⌗ ** THE CONTROL DOES NOT MOVE, and that is measured rather than assumed: ** `LEAFREC` does not
#   reach the control (3.6e-16, `r7641`), and 70 scored the SAME control for both rows of its
#   headline table.  *A move in PART 4 would mean I had re-pointed the control by mistake.*
_ARM = 'cr_x_h686_L2000_leafrec1_distances'
ls_a, Dl_a, lA_a = load(_ARM)
ls_c, Dl_c, lA_c = load('lcdm_L2000')
mb = CS.bin_spectrum(ls_a, Dl_a)
ok = np.isfinite(mb)
NB = int(ok.sum())
print(f"  the arm reaches ell = {ls_a[0]:.0f} to {ls_a[-1]:.0f}; the control {ls_c[0]:.0f} to "
      f"{ls_c[-1]:.0f}")
print(f"  ** bins fully covered: {NB} **, ell {int(CS.BIN_LO[ok][0])} to {int(CS.BIN_HI[ok][-1])}")
if NB != 185:
    fail.append(f"the range covers {NB} bins, not the 185 the corpus calls it")
if int(np.isfinite(CS.bin_spectrum(ls_c, Dl_c)).sum()) != NB:
    fail.append("the arm and the control do not cover the same bins -- the comparison is not matched")

pars = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * (0.674 ** 2) - 0.02237,
                       mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
cl = camb.get_results(pars).get_cmb_power_spectra(pars, CMB_unit='muK', lmax=3000)
lensed, unlens = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
lg = np.arange(len(lensed))
ratio = np.ones_like(lensed)
m = unlens > 0
ratio[m] = lensed[m] / unlens[m]
r1900 = float(np.interp(1900, lg, ratio))
print(f"\n  the operator's lensed/unlensed at ell = 1900:  {r1900:.4f}")
print(f"  ** P15_derived_lensing_on_the_lcdm_arm PART C gives +6.5% for the FULL operator there,")
print(f"     against the first-order kernel's spurious +13%.  This is the full operator. **")
if not (1.05 <= r1900 <= 1.08):
    fail.append(f"the operator gives {r1900:.4f} at ell = 1900, not the ~1.065 of the full operator")


def score(ls, Dl):
    u = CS.chi2_of(ls, Dl)
    L = CS.chi2_of(ls, Dl * np.interp(ls, lg, ratio))
    return u[0], L[0], u[1]


cu, cL, cn = score(ls_c, Dl_c)
au, aL, an = score(ls_a, Dl_a)

print()
print("=" * 104)
print("  PART 2 -- ** THE FOUR NUMBERS **")
print("=" * 104)
print(f"  {'':>22} {'bins':>5} {'unlensed':>10} {'/bin':>7} {'lensed':>10} {'/bin':>7} {'d(chi2)':>10}")
print(f"  {'control LCDM':>22} {cn:>5d} {cu:>10.1f} {cu / cn:>7.2f} {cL:>10.1f} {cL / cn:>7.2f} "
      f"{cL - cu:>+10.1f}")
print(f"  {'arm, crossing at 68.60':>22} {an:>5d} {au:>10.1f} {au / an:>7.2f} {aL:>10.1f} "
      f"{aL / an:>7.2f} {aL - au:>+10.1f}")
if aL >= au or cL >= cu:
    fail.append("lensing did not reduce chi^2 on one of the arms -- the operator is wired wrong")

print()
print("=" * 104)
print("  PART 3 -- ** THE RATIO, AND IT MOVED THE UNFAVOURABLE WAY **")
print("=" * 104)
print(f"  {'comparison':>42} {'arm/control':>12}")
print(f"  {'133-bin, unlensed (r6760+cc66.7)':>42} {4.16 / 2.10:>11.2f}x")
print(f"  {'185-bin full range, unlensed':>42} {au / cu:>11.2f}x")
print(f"  {'185-bin full range, LENSED':>42} {aL / cL:>11.2f}x")
print(f"""
  ** WHY IT MOVES: LENSING IS WORTH PROPORTIONALLY MORE TO THE CONTROL. **  The control falls by a
  factor {cu / cL:.2f} and the arm by {au / aL:.2f}, so the gap WIDENS.  *A smoothing operator helps a
  spectrum whose peaks are already in the right place more than one whose fourth peak is 0.9% out
  and whose acoustic phase is 2.3% out -- which is the same two residuals r6760+cc66.7 named, seen
  from the likelihood's side.*

  ⇒ *** SO THE x2.0 REPORTED AT cc66.7 WAS THE MORE FAVOURABLE OF THE TWO COMPARISONS, AND
  {aL / cL:.2f}x IS THE ONE sec:SR-15 MUST QUOTE, ** because the corpus's own chi^2 values are quoted on
  the full-range lensed configuration and a number scored on one may not be quoted against the
  other. ***  *Both are stated here so neither can be picked for being the kinder.*""")
if aL / cL <= au / cu:
    fail.append("the lensed ratio is not worse than the unlensed one -- PART 3's claim is wrong")
# ⛔⛭ r7645+cc66.66: ** RE-PINNED AT THE NO-FIT CONFIGURATION'S OWN VALUE ON THE ARM OF RECORD. **
#   *The 2.57 was the namesake arm's and this gate was set on it.  70 measured 2.346 for this
#   configuration with this receipt's own operator; scored here it is 2.3456.*  ⇒ ** The tolerance
#   goes from 0.15 -- which was six per cent of the figure and would have admitted the namesake's
#   value -- to 0.01, which is inside `check_figures_pinned`'s own allowance and would not. **
if abs(aL / cL - 2.3456) > 0.01:
    fail.append(f"the lensed ratio is {aL / cL:.4f}x, not the 2.3456 this configuration gives")
# ⛭ ** AND 70's BANK FIGURE IS REPRODUCED RATHER THAN TAKEN, which is the check that would have
#   caught the one pointer error in this pass (`cc66`'s 1.41 on the refitted file). **
if abs(aL - 502.1) > 0.5 or abs(aL / an - 2.71) > 0.005:
    fail.append(f"the arm scores {aL:.2f} ({aL / an:.3f} per bin), not 70's 502.1 and 2.71 -- "
                f"the same file scored two ways must agree")
# ⌗ *and the background is unchanged across the move, which is why this is a recombination result*
if abs(lA_a - 302.8891) > 5e-4:
    fail.append(f"the arm's l_A is {lA_a:.4f}, not the 302.8891 the namesake also carries -- "
                f"LEAFREC must not touch the background")

print()
print("=" * 104)
print("  PART 4 -- ** THE CONTROL AGAINST CAMB: THE FLAGGED CAVEAT IS WITHDRAWN **")
print("=" * 104)
CAMB_U, CAMB_L = 615.0, 186.0      # P15_derived_lensing_on_the_lcdm_arm PART A, these bins
OLD_ARM_U = 1320.0                 # the same receipt, PART B: the c54.178 LCDM arm
print(f"  {'':>34} {'unlensed':>10} {'lensed':>9}")
print(f"  {'CAMB LCDM (that receipt, PART A)':>34} {CAMB_U:>10.1f} {CAMB_L:>9.1f}")
print(f"  {'the c54.178 control (PART B)':>34} {OLD_ARM_U:>10.1f} {'989':>9}")
print(f"  {'THIS control':>34} {cu:>10.1f} {cL:>9.1f}")
print(f"""
  ⇒ ** THIS instrument's control is within {abs(cu / CAMB_U - 1) * 100:.0f}% of CAMB unlensed and
  {abs(cL / CAMB_L - 1) * 100:.0f}% lensed, where the c54.178 control was {OLD_ARM_U / CAMB_U:.1f}x CAMB's. **

  *r6760+cc66.9 flagged, BEFORE these numbers existed, that the control might carry ~700 of transfer
  inaccuracy on the full range -- "neither lensing's to close nor the arm's to answer for" -- and
  said the ratio should be read rather than either absolute.* ⇒ *** The caveat DOES NOT BITE on this
  configuration and is withdrawn rather than relied on.  The control is sound, so the ratio in PART
  3 is a statement about the arm and not about the instrument. ***
  ⌗ *It is recorded rather than deleted because it was stated in advance: a caveat raised before the
  measurement and then dropped in silence is indistinguishable from one that was never raised.*""")
if cu / CAMB_U > 1.5:
    fail.append(f"the control is {cu / CAMB_U:.2f}x CAMB unlensed -- the caveat DOES bite and "
                "PART 4 may not withdraw it")

# ===================================================================================================
# ⛭⛭ r7645+cc66.66: ** EVERY COMPUTED FIGURE THIS RECEIPT'S `INDEX.md` ROW PRINTS IS PINNED HERE,
#   TWO-SIDED, IN THE `abs(x - c) < t` FORM. **
#   ⛔ *This receipt's own gates are written `if abs(x - c) > tol: fail.append(...)`, which is a
#   two-sided pin in substance -- but `check_figures_pinned` looks for `abs(.. c ..) < t` and does
#   NOT recognise the `> tol`-and-fail form, so every figure the row printed read as unpinned.  That
#   is a real limitation of the detector and not of the gates; rather than rewrite this receipt's
#   style I state the row's guarantee in the form the guard verifies.*
print()
print("  THE FIGURES THE `INDEX.md` ROW PRINTS, PINNED TWO-SIDED:")
print(f"    arm (no-fit, arm of record): unlensed {au:.2f}, lensed {aL:.2f}, {aL / an:.3f} per bin, "
      f"ratio {aL / cL:.4f};  l_A {lA_a:.4f}")
print(f"    control (unmoved): unlensed {cu:.1f}, lensed {cL:.2f}, {cL / cn:.2f} per bin")
print(f"    lensing's reduction: control x{cu / cL:.2f}, arm x{au / aL:.2f};  "
      f"unlensed ratio {au / cu:.4f}")
_PIN = (
    abs(aL / cL - 2.3456) < 1e-4
    and abs(aL - 502.09) < 5e-3 and abs(aL / an - 2.714) < 5e-4
    and abs(au - 1129.76) < 5e-3 and abs(au / cu - 1.6233) < 1e-4
    and abs(cu - 695.97) < 5e-3 and abs(cL - 214.06) < 5e-3
    and abs(cL / cn - 1.157) < 5e-4
    and abs(cu / cL - 3.2513) < 1e-4 and abs(au / aL - 2.2501) < 1e-4
    and abs(lA_a - 302.8891) < 5e-5
)
if not _PIN:
    fail.append("a figure the `INDEX.md` row prints is not what this receipt computes -- the row's "
                "numbers must fail this receipt when they are wrong")

print()
print("=" * 104)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 104)
