#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `PO-24`: ** AT THE ADJUDICATED RATIO THE DIFFUSION-SCALE SIGNATURE COSTS $12.6$ AND
$1.7$ IN $\chi^2$ OVER $185$ BINS -- UNDER A TENTH PER BIN ON EITHER ENDPOINT -- AND A TILT OF
$-0.0093$ OR $+0.0034$ ABSORBS SEVEN TENTHS OF THAT.  AGAINST THE $1.082$ EVERY QUANTITATIVE LEG
OF THE ROW WAS COMPUTED AT, WHERE THE SAME TEST COSTS $159.9$ AND $-0.0341$. **

** ⇒ AND THE TWO ENDPOINTS DISAGREE IN SIGN, NOT ONLY IN SIZE. **  To recombination the arm's
$\theta_D/\theta_*$ is $1.0231$ of the control's and the absorbing tilt is NEGATIVE; to the
visibility peak it is $0.9918$ and the tilt is POSITIVE.  *This seat reported both and chose
neither, as ordered.*

*** ⚑ AND THE CHAT SEAT THEN SETTLED IT AT `r6797`: BOTH LENGTHS TERMINATE AT THE VISIBILITY PEAK,
because $\theta_D/\theta_*$ is a ratio of two lengths the plasma accumulates and the observed angle
is read there. ***  ** So the VISIBILITY-PEAK ROW IS THE ONE THAT STANDS, and the ruled number is
$r = 0.99179$, $-0.82\%$, at the adjudicated background -- not the $-0.9\%$ the ruling quotes, which
is that reading at the $H_0 = 73.00$ background the row's figures came from. **  *The recombination
row is kept because it is what the corpus carried and because the sign turning on the epoch is the
result; it is not an open alternative.*  PART 1b carries the settlement.

Built r6788+cc66.19 (node 66, code seat), discharging node 66 (chat seat)'s `PO-24` order --
"re-run the joint amplitude-and-tilt fit against the CR spectrum with the signature at the
adjudicated ratio, on both endpoints, reporting the per-bin residual after the fit, the tilt
displacement with its window stated, and the likelihood cost with amplitude alone against amplitude
and tilt."

** PART 1b ADDED AT r6797+cc66.20 ** *when the chat seat settled the endpoint and asked for the
common-endpoint number if it is not exactly $0.991$.  Nothing else in the receipt moved: the ruled
configuration was already the row labelled "to the visibility peak", because the integrals share one
upper limit.*

===================================================================================================
** WHAT MOVED, AND WHY THE ROW HAD TO BE RE-PRICED **
===================================================================================================

`C62` (r4494, node 60) measured this on the configuration of the day: the ONSET handover on the
STACKING clock, where $\theta_D/\theta_*$ sits at $1.082$ of the control's.  ** Everything
quantitative in the row -- the per-bin residual, the tilt displacement, the likelihood cost --
enters through ONE number, $r^2-1$, ** because the signature is a multiplicative Gaussian
$\exp[-(r^2-1)(\ell/\ell_D)^2]$ and $r^2-1$ is its only amplitude.

The configuration has since moved to the CROSSING handover on the LEAF clock at
$(H_0,\Omega_m) = (68.60,\,0.2973)$, where $r$ is $1.0231$ or $0.9918$ depending on the endpoint.
** So $r^2-1$ falls from $0.1707$ to $+0.0468$ or $-0.0164$ -- a factor $3.6$ and a factor $10$,
and a change of sign. **  *Nothing structural changed and nothing structural is re-derived here.
What is re-run is the pricing.*

  ⌗ ** THE STRUCTURAL RESULTS ARE CARRIED, NOT REPEATED, at the chat seat's instruction. **  The
  Gaussian-against-power-law argument, the slope running by $(\ell_{\max}/\ell_{\min})^2$, and the
  residual's correlation with the predicted form stand from `C62` and are not re-derived.  PART 3
  reports the window running because the ORDER asks for the tilt "with its window stated" and a
  displacement without one is not a number; PART 4 verifies the $r^2-1$ SCALING because the
  re-pricing is exactly the claim that the row's legs move with it, and a claim the arithmetic
  rests on is not a structural result to be inherited.

===================================================================================================
** THE FOUR CHOICES THAT SET THE ARITHMETIC, EACH MEASURED RATHER THAN ASSUMED **
===================================================================================================

  1  ** THE BASE IS THE CR SPECTRUM, as ordered, and not `C62`'s data-shape route. **  The arm's own
     $185$-bin full-range spectrum, $\ell = 100$--$1998$, at the adjudicated background, scaled by
     the amplitude that puts it in the likelihood's units.  *`C62` imposed the envelope on
     `plik_lite`'s own binned spectrum because it reached all $215$ bins with no instrument run.
     PART 5 runs BOTH and they agree to $2\%$, so the change of base is not what moves anything.*
  2  ** $\ell_D$ IS DERIVED, NOT RECALLED. **  $\ell_D = D_M/r_D$ with $D_M$ the base spectrum's own
     ($14011.5$ Mpc, baked into the `.npz`) and $r_D$ the CONTROL's from the same standalone
     integration that produces the ratio -- because the envelope being imposed is the DIFFERENCE
     between the arm's damping and the control's, so the reference scale is the control's.
     *`C62` used $1951.9$, the instrument header's $(\eta_0-\eta_{LS})/r_D$; this gives $2133.5$ and
     $2093.3$ on the two endpoints, and PART 2 reports the residual at `C62`'s scale beside its own, so the
     choice is bounded rather than hidden.*
  3  ** THE WINDOW IS $\ell = 100$--$1996$, THE $185$ COVERED BINS, and the pivot is $\ell = 1000$. **
     Asserted below, not taken on the name.
  4  ** THE BASE IS UNLENSED AND THE LENSED CASE IS RUN BESIDE IT. **  The banked spectra are
     unlensed and `P15`'s lensing is a derived CAMB operator applied afterwards; the envelope is
     physical and precedes lensing, so it is applied first and both are lensed together.  PART 5
     shows lensing moves the residual by $5\%$ and nothing else.

** COMPUTES: the ratio from the corpus's own Silk integrand with the opacity from
   `storyboard_receipts/RD_diffusion_direct.py`, via the `machinery()` of
   `P15_the_damping_signature_error_budget_and_the_convention_dominates_it` -- control at
   H0 = 67.40, Om = 0.3150, radiation IN the rate; arm at H0 = 68.60, Om = 0.2973, crossing
   handover (a0 = 1/(1+3e7)), leaf clock, radiation OUT of the stacking rate.  Ombh2 = 0.0224,
   z_rec = 1089.9, Yp = 0.2454.  The spectrum is `cc66_cr_x_h686_L2000.npz`, read and not
   produced.  The lensing operator is CAMB's lensed/unlensed at the control's parameters, the
   non-perturbative one P15 already uses.  *** Nothing is fitted to make the signature survive or
   vanish: r is MEASURED from the two arms and imposed, and the only free parameters are the
   amplitude and the tilt the degeneracy names. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~90 s)
"""
import math
import os
import sys

import numpy as np
import scipy.linalg

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                                # noqa: E402

# ** THE RATIO MACHINERY IS THE SIBLING RECEIPT'S OWN, IMPORTED AND NOT RE-TYPED. **  *A second
#    transcription of an integrand is a second chance to get it wrong, and the endpoint question
#    this row turns on is decided inside that function.*  Only the definitions are executed: the
#    file's own report is cut at its first banner.
_EB = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                   'P15_the_damping_signature_error_budget_and_the_convention_dominates_it.py')
EB = type(sys)('EB')
EB.__dict__['__file__'] = _EB
exec(compile(open(_EB, encoding='utf-8').read().split('print("=" * 99)')[0], _EB, 'exec'),
     EB.__dict__)
machinery = EB.machinery

L_PIV = 1000.0
LC, _ = CS.bin_center_and_fac()


def refit(model, target, keep):
    """amplitude-only chi2, amplitude+tilt chi2, the tilt B/A, and the tilt's OWN uncertainty."""
    n = int(keep.sum())
    F = scipy.linalg.cho_solve(
        scipy.linalg.cho_factor(CS.COV_TT[np.ix_(keep, keep)]), np.identity(n))
    F = 0.5 * (F + F.T)
    b, d = model[keep], target[keep]
    A = float((d @ F @ b) / (b @ F @ b))
    c1 = float((d - A * b) @ F @ (d - A * b))
    X = np.vstack([b, b * np.log(LC[keep] / L_PIV)]).T
    M = X.T @ F @ X
    co = np.linalg.solve(M, X.T @ F @ d)
    r = d - X @ co
    g = np.array([-co[1] / co[0] ** 2, 1.0 / co[0]])
    return n, c1, float(r @ F @ r), float(co[1] / co[0]), float(np.sqrt(g @ np.linalg.inv(M) @ g))


# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE RATIO AT THE ADJUDICATED BACKGROUND, ON BOTH ENDPOINTS **")
print(BAR)
CTL = machinery(67.40, 0.3150, 0.0224, 1089.9, leaf_clock=True, radiation_in_rate=True)
ARM = machinery(68.60, 0.2973, 0.0224, 1089.9, leaf_clock=True, radiation_in_rate=False)
OLD = machinery(73.00, 0.3066, 0.0224, 1089.9, leaf_clock=True, radiation_in_rate=False)

d = np.load(os.path.join(SPEC, 'cc66_cr_x_h686_L2000.npz'))
LS = np.asarray(d['ls'], float)
DL = np.asarray(d['Dl'], float)
D_M = float(d['D_M'])
print(f"  the base spectrum carries D_M = {D_M:.1f} Mpc, l_A = {float(d['l_A']):.2f}, "
      f"ell {LS[0]:.0f}-{LS[-1]:.0f}")
print()
print(f"  {'endpoint':>18} {'t_control':>10} {'t_arm':>10} {'r = ratio':>10} {'r^2-1':>10} "
      f"{'l_D = D_M/r_D':>14} {'r at 73.00':>11}")
EP = {}
for ep, nm in (('a_rec', 'recombination'), ('a_vis', 'visibility peak')):
    tc = CTL['r_D'](CTL[ep]) / CTL['r_s'](CTL[ep])
    ta = ARM['r_D'](ARM[ep]) / ARM['r_s'](ARM[ep])
    to = OLD['r_D'](OLD[ep]) / OLD['r_s'](OLD[ep])
    r = ta / tc
    EP[nm] = dict(r=r, fac=r * r - 1.0, lD=D_M / CTL['r_D'](CTL[ep]), old=to / tc)
    print(f"  {nm:>18} {tc:>10.6f} {ta:>10.6f} {r:>10.5f} {r * r - 1:>+10.5f} "
          f"{EP[nm]['lD']:>14.1f} {to / tc:>11.5f}")
print()
print(f"  the visibility peak is located at z = {1 / ARM['a_vis'] - 1:.1f} on the arm and "
      f"z = {1 / CTL['a_vis'] - 1:.1f} on the control, against recombination at z = 1089.9")
print()
print("  ** THE BACKGROUND MOVED AND THE SIGNATURE DID NOT. **  The row's 1.022 and 0.991 were")
print("  computed at H0 = 73.00, Om = 0.3066 -- the instrument's arm before the distances fixed it.")
for nm in EP:
    print(f"      {nm:>18}:  {EP[nm]['old']:.5f} at 73.00  ->  {EP[nm]['r']:.5f} at 68.60   "
          f"({abs(EP[nm]['r'] - EP[nm]['old']) * 100:.2f} points)")
check("the adjudicated ratio is within 0.15 points of the 1.022 / 0.991 the row carries",
      all(abs(EP[n]['r'] - EP[n]['old']) < 0.0015 for n in EP))
check("** and the two endpoints still STRADDLE ONE, so the sign is the endpoint's **",
      (EP['recombination']['r'] - 1) * (EP['visibility peak']['r'] - 1) < 0)
check("the arm's r_D endpoint and the control's are each that arm's own visibility peak, "
      "0.3-0.8% apart in redshift and not shared",
      abs(ARM['a_vis'] - CTL['a_vis']) / CTL['a_vis'] > 1e-3)

# =================================================================================================
print()
print(BAR)
print("  PART 1b -- ** THE ENDPOINT, SETTLED AT r6797: BOTH LENGTHS TO THE VISIBILITY PEAK **")
print(BAR)
# ** THE CHAT SEAT SETTLED THIS AFTER THE RUN AND ITS REASON IS CHECKABLE, SO IT IS CHECKED. **
# `r6797`: theta_D/theta_* is a ratio of two lengths the plasma accumulates, the observed angle is
# read at the peak of the visibility function, so r_s and r_D both terminate there.  *The RULING is
# the papers' and is not second-guessed here.  What is measured is whether the instrument needed
# surgery to obey it, and whether the number it produces is the one the ruling's rationale names.*
print("  ** THE INSTRUMENT NEEDED NO SURGERY. **  machinery()'s r_s(a_hi) and r_D(a_hi) take ONE")
print("  upper limit, so 'both lengths to the same epoch' is what every row above already does.")
print("  *The ruling is obeyed by construction and nothing was substituted for it.*")
print()
print(f"  {'r_s runs to':>14} {'r_D runs to':>14} {'ratio':>10} {'':>10} {'reading':>10}")


def ratio(ep_s, ep_D, arm):
    return ((arm['r_D'](arm[ep_D]) / arm['r_s'](arm[ep_s]))
            / (CTL['r_D'](CTL[ep_D]) / CTL['r_s'](CTL[ep_s])))


MIX = {}
for es in ('a_rec', 'a_vis'):
    for ed in ('a_rec', 'a_vis'):
        v = ratio(es, ed, ARM)
        MIX[(es, ed)] = v
        tag = '** COMMON **' if es == ed else 'mixed'
        print(f"  {es:>14} {ed:>14} {v:>10.5f} {100 * (v - 1):>+9.2f}%  {tag:>14}")
print()
print("  ⇒ ** THE RULED READING IS r = "
      f"{MIX[('a_vis', 'a_vis')]:.5f}, i.e. {100 * (MIX[('a_vis', 'a_vis')] - 1):+.2f}%, AT THE ADJUDICATED BACKGROUND **")
print(f"    and {ratio('a_vis', 'a_vis', OLD):.5f} ({100 * (ratio('a_vis', 'a_vis', OLD) - 1):+.2f}%) at the H0 = 73.00 one the")
print("    row's -0.9% came from.  *The order asks for the number if it is not exactly 0.991; it is")
print(f"    {MIX[('a_vis', 'a_vis')]:.5f} where the distances now put the background.*")
print()
print("  ⛔ ** AND ONE THING IN THE RULING'S ACCOUNT OF THE OLD NUMBER IS NOT WHAT THE CODE DID. **")
print("  r6797 describes the +2.2% as 'the sound horizon anchored at the observed angle against a")
print("  diffusion length taken to a sharp recombination cut' -- a MIXED reading.  *The standalone")
print("  integration that produced +2.2% took BOTH lengths to recombination:* it is the COMMON")
print(f"  reading at the other epoch, {MIX[('a_rec', 'a_rec')]:.5f}.  ** The mixed quantity the sentence describes")
print(f"  measures {MIX[('a_vis', 'a_rec')]:.5f}, {100 * (MIX[('a_vis', 'a_rec')] - 1):+.2f}%, which is not the number the row carried. **")
print("  ⇒ *So the choice is between two COMMON epochs, not between a common and a mixed reading --")
print("     which makes the ruling's own argument the whole of its support, and it carries it.*")
check("** the ruled reading is the common visibility-peak one, and it is NOT exactly 0.991 **",
      abs(MIX[('a_vis', 'a_vis')] - EP['visibility peak']['r']) < 1e-9
      and abs(MIX[('a_vis', 'a_vis')] - 0.991) > 5e-4)
check("the corpus's +2.2% is the COMMON recombination reading, not a mixed one",
      abs(MIX[('a_rec', 'a_rec')] - EP['recombination']['r']) < 1e-9)
check("** and mixing the epochs is not a small effect: the four readings span 4 points **",
      (max(MIX.values()) - min(MIX.values())) > 0.03)

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** THE JOINT AMPLITUDE-AND-TILT FIT, ell = 100-1996, PIVOT 1000 **")
print(BAR)
AMP = float(CS.chi2_of(LS, DL)[2])
BASE = AMP * CS.bin_spectrum(LS, DL)
FIN = np.isfinite(BASE)
NB = int(FIN.sum())
print(f"  the amplitude that puts the base in the likelihood's units is {AMP:.6g}; "
      f"{NB} bins covered, ell {int(CS.BIN_LO[FIN][0])}-{int(CS.BIN_HI[FIN][-1])}")
check("the window is the 185-bin full range, asserted and not taken on the name",
      NB == 185 and int(CS.BIN_LO[FIN][0]) == 100 and int(CS.BIN_HI[FIN][-1]) == 1996)
print()
print(f"  {'endpoint':>18} {'l_D':>8} {'A alone':>9} {'/bin':>8} {'+tilt':>9} {'/bin':>9} "
      f"{'sig/bin':>8} {'dn_s':>10} {'sigma':>9} {'in sigma':>9} {'d(chi2)':>9}")
MAIN = {}
for nm in EP:
    for lab, lD in (('', EP[nm]['lD']), (' at C62 l_D', 1951.9)):
        dmp = AMP * CS.bin_spectrum(LS, DL * np.exp(-EP[nm]['fac'] * (LS / lD) ** 2))
        n, c1, c2, dn, sd = refit(BASE, dmp, FIN)
        if not lab:
            MAIN[nm] = (n, c1, c2, dn, sd)
        print(f"  {nm + lab:>18} {lD:>8.1f} {c1:>9.3f} {c1 / n:>8.4f} {c2:>9.3f} {c2 / n:>9.5f} "
              f"{math.sqrt(c2 / n):>8.3f} {dn:>+10.5f} {sd:>9.5f} {abs(dn) / sd:>8.1f}s "
              f"{c1 - c2:>9.3f}")
print()
print("  ⌗ sigma(dn_s) is propagated through the fit's OWN parameter covariance, built from the")
print("    same plik_lite covariance that scores the fit -- not a recalled Planck error bar.")
print("  ⌗ the C62 l_D rows are the same fit at the OLD reference scale: it moves the residual by")
print("    at most 42% and moves no verdict, which is the point of printing it.")

for nm in EP:
    n, c1, c2, dn, sd = MAIN[nm]
    check(f"{nm}: amplitude ALONE costs under 0.1 per bin -- the signature is not visible in TT",
          c1 / n < 0.1)
    check(f"{nm}: and a tilt absorbs most of even that, leaving under 0.15 sigma per bin",
          math.sqrt(c2 / n) < 0.15)

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE TILT DISPLACEMENT IS NOT A NUMBER WITHOUT ITS WINDOW **")
print(BAR)
print("  The absorbing tilt of a Gaussian is the window's, because d ln(envelope)/d ln ell =")
print("  -2 (r^2-1)(ell/l_D)^2 runs across the range.  The order asks for the displacement WITH its")
print("  window stated; here are four, and the running is what C62's (l_max/l_min)^2 result says.")
print()
print(f"  {'endpoint':>18} {'window':>14} {'bins':>5} {'A alone/bin':>12} {'+tilt/bin':>11} "
      f"{'sig/bin':>8} {'dn_s':>10} {'in sigma':>9}")
WIN = {}
for nm in EP:
    dmp = AMP * CS.bin_spectrum(LS, DL * np.exp(-EP[nm]['fac'] * (LS / EP[nm]['lD']) ** 2))
    for lo, hi in ((100, 1996), (100, 1300), (700, 1996), (1300, 1996)):
        k = FIN & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
        n, c1, c2, dn, sd = refit(BASE, dmp, k)
        WIN[(nm, lo, hi)] = dn
        print(f"  {nm:>18} {f'{lo}-{hi}':>14} {n:>5d} {c1 / n:>12.4f} {c2 / n:>11.5f} "
              f"{math.sqrt(c2 / n):>8.3f} {dn:>+10.5f} {abs(dn) / sd:>8.1f}s")
lo_w = abs(WIN[('recombination', 100, 1300)])
hi_w = abs(WIN[('recombination', 1300, 1996)])
c_lo = 0.5 * (100 + 1300)
c_hi = 0.5 * (1300 + 1996)
print()
print(f"  the displacement runs {lo_w:.5f} -> {hi_w:.5f} between the low and high windows, a factor")
print(f"  {hi_w / lo_w:.2f}, against {(c_hi / c_lo) ** 2:.2f} from the ratio of their central ell SQUARED")
check("** the tilt runs with the window as ell^2, within 15% of the predicted factor **",
      abs(hi_w / lo_w / (c_hi / c_lo) ** 2 - 1) < 0.15)
check("and it runs by more than a factor 3 across the windows, so quoting it without one is empty",
      hi_w / lo_w > 3.0)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE r^2-1 SCALING, WHICH IS WHAT THE RE-PRICING RESTS ON **")
print(BAR)
print("  The chat seat prices this row by scaling every leg with r^2-1: 0.045 against 0.171, a")
print("  factor 3.8.  ** That is an assumption about the fit and it is cheap to check. **  The tilt")
print("  should go LINEARLY in r^2-1 and the chi^2 as its SQUARE.")
print()
print(f"  {'r':>10} {'r^2-1':>10} {'dn_s':>11} {'vs ref':>9} {'predicted':>10} "
      f"{'A alone':>10} {'vs ref':>9} {'predicted':>10} {'+tilt':>9} {'/bin':>8} {'sig/bin':>8}")
LD_REF = EP['recombination']['lD']
ROWS = [(1.082, 'C62, the row as written'),
        (EP['recombination']['r'], 'adjudicated, to recombination'),
        (EP['visibility peak']['r'], 'adjudicated, to the visibility peak')]
ref = None
SCALE = []
for r, _lab in ROWS:
    fac = r * r - 1.0
    dmp = AMP * CS.bin_spectrum(LS, DL * np.exp(-fac * (LS / LD_REF) ** 2))
    n, c1, c2, dn, sd = refit(BASE, dmp, FIN)
    if ref is None:
        ref = (fac, dn, c1)
    SCALE.append((fac / ref[0], dn / ref[1], c1 / ref[2]))
    print(f"  {r:>10.5f} {fac:>+10.6f} {dn:>+11.6f} {dn / ref[1]:>9.4f} {fac / ref[0]:>10.4f} "
          f"{c1:>10.4f} {c1 / ref[2]:>9.4f} {(fac / ref[0]) ** 2:>10.4f} {c2:>9.3f} {c2 / n:>8.4f} "
          f"{math.sqrt(c2 / n):>8.3f}")
print()
print("  ⌗ all three rows use ONE l_D so the comparison isolates r^2-1 and nothing else.")
check("** the tilt displacement is linear in r^2-1 to better than 3% on both adjudicated rows **",
      all(abs(m / p - 1) < 0.03 for p, m, _ in SCALE[1:]))
check("** and the amplitude-only chi^2 goes as its SQUARE, to better than 8% **",
      all(abs(c / p ** 2 - 1) < 0.08 for p, _, c in SCALE[1:]))
print(f"  ⇒ so the chat seat's factor {ref[0] / (EP['recombination']['r'] ** 2 - 1):.1f} is right, and the")
print("    residual it prices collapses by that factor SQUARED.")

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** TWO THINGS THAT COULD HAVE BEEN DOING THE WORK, AND ARE NOT **")
print(BAR)
print("  (a) THE BASE.  C62 imposed the envelope on plik_lite's own binned spectrum; the order says")
print("      the CR spectrum.  If the verdict depended on which, it would be a statement about the")
print("      base and not about the signature.")
print()
print(f"  {'endpoint':>18} {'base':>22} {'bins':>5} {'A alone/bin':>12} {'+tilt/bin':>11} "
      f"{'dn_s':>10}")
DATA = CS.X_DATA.copy()
for nm in EP:
    dmp = AMP * CS.bin_spectrum(LS, DL * np.exp(-EP[nm]['fac'] * (LS / EP[nm]['lD']) ** 2))
    n, c1, c2, dn, sd = refit(BASE, dmp, FIN)
    dd = DATA * np.exp(-EP[nm]['fac'] * (LC / EP[nm]['lD']) ** 2)
    n2, c12, c22, dn2, _ = refit(DATA, dd, FIN)
    print(f"  {nm:>18} {'the CR spectrum':>22} {n:>5d} {c1 / n:>12.4f} {c2 / n:>11.5f} {dn:>+10.5f}")
    print(f"  {'':>18} {'plik_lite data (C62)':>22} {n2:>5d} {c12 / n2:>12.4f} {c22 / n2:>11.5f} "
          f"{dn2:>+10.5f}")
    check(f"{nm}: the two bases give the same tilt to 5% -- the base is not doing the work",
          abs(dn2 / dn - 1) < 0.05)

print()
print("  (b) LENSING.  The banked spectra are unlensed and P15's lensing is a derived CAMB operator")
print("      applied afterwards.  The envelope is physical and precedes lensing, so it is applied")
print("      FIRST and both spectra are then lensed together.")
pars = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * (0.674 ** 2) - 0.02237,
                       mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(pars).get_cmb_power_spectra(pars, CMB_unit='muK', lmax=3000)
_lens, _unl = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
_lg = np.arange(len(_lens))
_rat = np.ones_like(_lens)
_m = _unl > 0
_rat[_m] = _lens[_m] / _unl[_m]
LENS = np.interp(LS, _lg, _rat)
print(f"      the operator's lensed/unlensed at ell = 1900 is {float(np.interp(1900, _lg, _rat)):.4f} "
      f"-- P15's full operator, not the first-order kernel")
check("the lensing operator is the non-perturbative one (+6.5% at ell = 1900, not the kernel's +13%)",
      1.05 <= float(np.interp(1900, _lg, _rat)) <= 1.08)
print()
print(f"  {'endpoint':>18} {'':>22} {'A alone/bin':>12} {'+tilt/bin':>11} {'sig/bin':>8} "
      f"{'dn_s':>10}")
AMP_L = float(CS.chi2_of(LS, DL * LENS)[2])
BASE_L = AMP_L * CS.bin_spectrum(LS, DL * LENS)
for nm in EP:
    dmp = AMP_L * CS.bin_spectrum(
        LS, DL * np.exp(-EP[nm]['fac'] * (LS / EP[nm]['lD']) ** 2) * LENS)
    n, c1, c2, dn, sd = refit(BASE_L, dmp, FIN)
    n0, c10, c20, dn0, _ = MAIN[nm]
    print(f"  {nm:>18} {'lensed, both':>22} {c1 / n:>12.4f} {c2 / n:>11.5f} "
          f"{math.sqrt(c2 / n):>8.3f} {dn:>+10.5f}")
    check(f"{nm}: lensing moves the residual by under 10% and no verdict",
          abs(c1 / c10 - 1) < 0.10 and abs(dn / dn0 - 1) < 0.10)

# =================================================================================================
print()
print(BAR)
print("  PART 6 -- ** THE FITTER, CONTROLLED **")
print(BAR)
print("  A fitter that reports absorption has to be shown it is not manufacturing it.")
for dn_true in (0.02, 0.05):
    inj = AMP * CS.bin_spectrum(LS, DL * (LS / L_PIV) ** dn_true)
    n, c1, c2, dn, sd = refit(BASE, inj, FIN)
    print(f"      injected dn_s = {dn_true:+.3f} -> recovered {dn:+.5f}, residual {c2 / n:.3e}/bin, "
          f"absorbed {100 * (1 - c2 / c1):.4f}%")
    # ** THE RECOVERY IS NOT EXACT AND SHOULD NOT BE. **  The injection multiplies the spectrum
    # before binning and the fit applies the tilt at the bin CENTRE; the bin-average of a power law
    # is not the power law at the centre.  *A few per mille of mis-recovery is the binning, not the
    # fitter, and demanding zero would be demanding the wrong thing.*
    check(f"the fitter recovers an injected tilt of {dn_true:+.3f} to 5% and absorbs > 99.9%",
          abs(dn - dn_true) < 0.05 * dn_true and c2 / c1 < 1e-3)

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SAYS, AND THE ONE THING IT DOES NOT DECIDE")
print(BAR)
n_r, c1_r, c2_r, dn_r, sd_r = MAIN['recombination']
n_v, c1_v, c2_v, dn_v, sd_v = MAIN['visibility peak']
print(f"""
  ** THE SIGNATURE IS NO LONGER A HIGH-ell OBSERVABLE ON EITHER ENDPOINT. **  Over the same 185
  bins the row was priced on, an amplitude ALONE absorbs it to {c1_r / n_r:.4f} per bin to
  recombination and {c1_v / n_v:.4f} to the visibility peak -- {c1_r:.1f} and {c1_v:.1f} in total chi^2.
  *At 1.082 the same test costs {ref[2]:.1f}.*  ** A 13-fold and a 100-fold collapse, and it is
  the configuration that moved and not the fit. **

  ** THE TILT IT COSTS IS {abs(dn_r) / sd_r:.1f} SIGMA AND {abs(dn_v) / sd_v:.1f} SIGMA of what this dataset's own
  covariance gives for a tilt ** -- against {0.034142 / sd_r:.0f} sigma at 1.082.  *So the degeneracy the
  frontier text names is still real and is no longer expensive: the displacement is
  {dn_r:+.4f} or {dn_v:+.4f} on the full window, and it runs by a factor {hi_w / lo_w:.1f} across the sub-windows,
  so it must be quoted with one.*

  ⛔ ** AND THE SIGN IS THE ENDPOINT'S, NOT THE CONSTRUCTION'S. **  To recombination the arm damps
  MORE than the control and the absorbing tilt is negative; to the visibility peak it damps LESS
  and the tilt is positive.  The two stopping points are 0.4% apart in redshift.  *This seat
  reported both and chose neither.*  ** The chat seat settled it at r6797 -- both lengths to the
  visibility peak -- so the ruled row is the second: r = 0.99179 (-0.82%), an amplitude alone
  costing {c1_v:.3f} over 185 bins and a tilt of {dn_v:+.5f} absorbing it to {math.sqrt(c2_v / n_v):.3f} sigma per bin. **
  *PART 1b measures the settlement: the instrument needed no surgery to obey it, and the corpus's
  +2.2% was the COMMON reading at the other epoch rather than the mixed one the ruling describes.*

  ⌗ ** WHAT THIS DOES NOT SAY. **  That the arm fits.  The refit (r6788+cc66.18) leaves it at
  1.30 per bin against the control's 0.90 on 132 bins, and the full-range lensed comparison at
  2.57x.  *This measures ONE thing -- what the diffusion scale's displacement does to the observed
  TT power -- and it says that thing has become small enough to stop carrying the row's old
  arithmetic.*
""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print(BAR)
