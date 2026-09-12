#!/usr/bin/env python3
r"""
P15 — ** THE JOINT FIT FOR `PO-24`, RUN.  THE RESIDUAL IS THE PREDICTED GAUSSIAN SHAPE TO SIX
DECIMAL PLACES AND IT SURVIVES LARGER THAN THE BOUND IT WAS TO BE MEASURED AGAINST — BECAUSE THAT
BOUND WAS QUOTED IN THE WRONG UNITS, AND WAS THE MORE FAVOURABLE OF THE TWO `C62` LEFT. **

** THE JOB (64, r6521).**  *`r6409` argued the row's question is not well posed: the signature is a
GAUSSIAN in $\ell$ and a tilt is a POWER LAW, so absorption is window-local and the joint fit meets
a residual no tilt removes.  The order asks for that run, and for the residual "against the bound
already in hand: 0.26 sigma per bin".*

*** ⛔ FIRST, THAT BOUND IS NOT 0.26 SIGMA PER BIN.  `C62` SAYS 0.26 chi^2 PER BIN. ***  *Its own
verdict text: "absorbs it almost completely in SHAPE --- 0.26 chi^2 per bin over P15's 185-bin
ceiling", and its own check converts with a square root (`math.sqrt(c2_/n_) < 1.1`).  `r6409`
restated it as "0.26 sigma per bin" and this order inherited the restatement.*  ** 0.26 chi^2/bin is
0.51 sigma/bin — the two differ by a square root, and the looser of them is the one that was
quoted as the tighter. **

*** ⛔ AND IT IS THE WRONG ONE OF `C62`'s TWO. ***  *`C62` measured the absorption by two routes and
refused to reconcile them: the **data-shape** route (multiply the final spectrum by the Gaussian
ratio) gives 0.26 chi^2/bin and $\Delta n_s=-0.030$; the **instrument** route (`DAMPX` inside the
source) gives 0.92 and $-0.0847$.  Its own words:* **"The instrument route is the more faithful of
the two and it is the LARGER, so the wash is the weaker claim and is asserted at the weaker
bound."**  *`r6409` carried forward the 0.26.*

** WHAT WAS RUN.**  Baseline: the banked control arm to $\ell=2508$ (`L820_lcdm_L2512_nk800`),
normalised to the data.  Target: that baseline times the signature
$S(\ell)=\exp[-(r^2-1)(\ell/\ell_D)^2]$, $r=1.0926$, $\ell_D=1362$.  Model: $A\,(\ell/1000)^{\Delta
n}\times$ baseline.  Metric: plik_lite TT's own bandpowers, binning and covariance, restricted to
covered bins **on the covariance** so the uncovered ones are marginalised rather than conditioned on.

*** ⓵ THE RESIDUAL IS THE PREDICTED SHAPE, NOT MERELY NONZERO. ***  After the joint fit the residual
correlates with the analytic $S(\ell)-A(\ell/1000)^{\Delta n}$ at **1.000000**.  `r6409` predicted a
Gaussian-shaped residual that no tilt removes; that is what is there, exactly.

*** ⓶ AND IT SURVIVES LARGER THAN EITHER OF `C62`'s BOUNDS. ***  Over `P15`'s own 185-bin ceiling
window ($\ell=100$–$1758$, 171 covered bins): **1.497 chi^2/bin after the tilt**, against the
data-shape route's 0.26 and the instrument route's 0.92.  The tilt takes $69.8\%$ of the signature
and leaves the rest.

*** ⓷ AND THE "DISPLACEMENT" IS NOT A NUMBER — MEASURED, NOW, NOT ARGUED. ***  The best-fit
$\Delta n_s$ depends on the window it is fitted over:

      window          bins    Delta n_s    chi^2/bin after    absorbed
      100-1760         171     -0.08304         1.4967         69.8%
      700-1760         104     -0.21008         0.3440         91.4%
      1000-1760         71     -0.30942         0.1085         96.0%
      1000-2508        101     -0.34087         0.1941         95.6%
      1400-2508         56     -0.52084         0.0385         97.6%
      100-2508         201     -0.09988         2.3410         68.5%

*A factor of $6.3$ in the fitted displacement across windows of the same data.*  ** Every number
here is reported with the window it belongs to, because it is the value of nothing without one. **
⌗ *The bounded solver is not housekeeping either: a bracketed one assuming $|\Delta n|<0.3$ FAILS on
the $700$–$1760$ window, which is the row's own point arriving in the optimiser.*

*** ⓸ WHAT IT DOES TO THE COMPARISON, IN THE LIKELIHOOD'S OWN UNITS. ***  Scored against the sky
over the same 171 bins: the signature costs $+357.3$ in $\chi^2$ with amplitude alone, and $+84.5$
after the tilt is refitted.  ** So the fit IMPROVES the comparison, by $272.8$, and does not remove
it: $76\%$ of the cost is absorbed and $+84.5$ over 171 bins remains. **  *The compensating tilt
against the sky is BLUE ($+0.0616$) where the degeneracy fit's is RED ($-0.083$) — they are answers
to different questions and are kept apart.*

** CROSS-CHECK AGAINST `C62`, INDEPENDENTLY.**  This route's $\Delta n_s=-0.0830\pm0.0034$ ($24.8$
sigma) against `C62`'s instrument route $-0.0847$ ($22.7$ sigma): agreement to $2\%$ on a quantity
computed from a different spectrum by a different method.

** T1 — WHICH OF THE TWO THIS IS, SAID RATHER THAN LEFT OPEN.**  $n_s$ is **inherited boundary
data** in this construction, not a prediction: `P15` states $A_s$ and $n_s$ are "inherited as
boundary data exactly as flat $\Lambda$CDM inherits the baryon-to-photon ratio".  ** A displacement
in it is a different INPUT, not a conflict. **  What would be a conflict is a constraint on $n_s$
that does not run through the damping tail; this measures neither.

** T2 — THE GAUSSIAN AND THE POWER LAW, KEPT DISTINCT.**  The SIGNATURE is
$\exp[-(r^2-1)(\ell/\ell_D)^2]$ with $r=1.0926$, $\ell_D=1362$ — two parameters, neither fitted
here.  The FIT is $A(\ell/1000)^{\Delta n}$ — two parameters, both fitted.  *Reporting the fit's
parameters describes the fit; the signature's are the physics and are inputs.*

** WHAT IS NOT ESTABLISHED.**
  · ** This is what a tilt ABSORBS, not whether CR fits the sky. **  Fit II scores the signature's
    effect on one comparison; it is not a verdict on the construction, and `P15`'s own instrument
    floor and multipole ceiling bound what any such verdict could mean here.
  · ** Only two parameters are free. **  `C62`'s scoping applies unchanged: on the SHAPE residual
    freeing more can only absorb more, so this is an upper bound on what survives; on the TILT it is
    neither bound, since $\omega_b$ moves $r_D$ itself and the displacement would be shared.
  · ** TT only**, no polarisation, no lensing, no $\ell<100$ from this baseline.
  · The baseline is the instrument's control arm, unlensed and ceiling-limited where the sky is
    neither — `C62`'s own stated reason its two routes differ by about three.

Written r6522.  Stated for reversal.

COMPUTES: scope.  r = 1.0926 and l_D = 1362 are P15's damping ratio and damping multipole, INPUTS
here and fitted by nothing.  The pivot l* = 1000 is arbitrary and asserted irrelevant (Delta n is
pivot-independent; A absorbs it).  Windows are named by their own l ranges throughout and no number
is quoted without one.  The baseline is the banked L820_lcdm_L2512_nk800 control arm, normalised to
plik_lite by the closed-form amplitude -- a UNITS conversion of ~1.1e4, not a tweak.  0.26 and 0.92
chi^2/bin are C62's two routes, quoted from its verdict text, not recomputed here.
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

FAILED = []
R, LD = 1.0926, 1362.0                 # P15's damping ratio and damping multipole -- INPUTS
K = R**2 - 1
C62_DATA_SHAPE, C62_INSTRUMENT = 0.26, 0.92        # chi^2/bin, C62's two routes


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def sig(l):
    return np.exp(-K * (np.asarray(l, float) / LD) ** 2)


_z = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                          'L820_lcdm_L2512_nk800.npz'))
LS, RAW = _z['ls'].astype(float), _z['Dl'].astype(float)
LC, _ = CS.bin_center_and_fac()


def _fisher(keep):
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (F + F.T), np.sqrt(np.diag(cov))


_k0 = np.isfinite(CS.bin_spectrum(LS, RAW))
_F0, _ = _fisher(_k0)
_m0 = CS.bin_spectrum(LS, RAW)[_k0]
A_UNITS = float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))
DL = RAW * A_UNITS                      # the baseline, in the DATA's units


def window(lo=None, hi=None):
    keep = np.isfinite(CS.bin_spectrum(LS, DL))
    if lo is not None:
        keep &= (CS.BIN_LO >= lo)
    if hi is not None:
        keep &= (CS.BIN_HI <= hi)
    return keep


def joint(target, keep, F, piv=1000.0, base=None):
    """fit A and Delta n jointly; A in closed form, Delta n by a BOUNDED search"""
    b = DL if base is None else base

    def at(dn):
        m = CS.bin_spectrum(LS, b * (LS / piv) ** dn)[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r), A, r

    o = minimize_scalar(lambda d: at(d)[0], bounds=(-3.0, 3.0), method='bounded',
                        options={'xatol': 1e-10})
    dn = float(o.x)
    c, A, r = at(dn)
    h = 1e-4
    sdn = float(np.sqrt(2.0 / ((at(dn + h)[0] - 2 * c + at(dn - h)[0]) / h ** 2)))
    return dn, sdn, c, A, r, at


def main():
    print()
    print('  P15 -- PO-24: the joint fit, and the bound it was to be measured against')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE BOUND IN HAND, READ AT ITS SOURCE')
    print('  ' + '=' * 74)
    c62 = open(os.path.join(HERE, 'C62_the_diffusion_signature_is_a_wash_and_the_isw_is_not_'
                                  'what_it_turned_on.py'), encoding='utf-8').read()
    r6409 = open(os.path.join(HERE, 'P15_the_tilt_is_the_wrong_absorber.py'),
                 encoding='utf-8').read()
    check('⓵ C62 states the bound in chi^2 per bin, not sigma per bin',
          '0.26 chi^2 per bin' in ' '.join(c62.split()))
    check('⓵ᵇ and converts to sigma with a square root in its own check, so the two are not the '
          'same quantity there either',
          'math.sqrt(c2_ / n_) < 1.1' in c62)
    check('⓵ᶜ ⛔ while r6409 restates it as "0.26 sigma per bin" -- the looser bound quoted as the '
          f'tighter one, since 0.26 chi^2/bin is {np.sqrt(C62_DATA_SHAPE):.3f} sigma/bin',
          '0.26 sigma per bin' in ' '.join(r6409.split()))
    # ⌗ The sentence spans a commented continuation, so joining whitespace leaves a '#' inside
    #   it.  Strip comment markers before matching rather than matching a shorter fragment that
    #   could sit anywhere in the file.
    c62_flat = ' '.join(l.lstrip().lstrip('#').strip() for l in c62.split('\n'))
    c62_flat = ' '.join(c62_flat.split())
    check('⓵ᵈ ⛔ and C62 carries TWO routes, saying in terms that the LARGER is the more faithful '
          'and that the wash is asserted at the weaker bound -- 0.92, not 0.26',
          'The instrument route is the more faithful of the two and it is the LARGER' in c62_flat
          and 'asserted at the weaker bound' in c62_flat
          and '0.92 per bin' in c62_flat)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- TWO CALIBRATIONS, AND THE FIRST CANNOT SEE WHAT THE SECOND CATCHES')
    print('  ' + '=' * 74)
    keep = window(hi=1759)
    F, sd = _fisher(keep)
    worst = 0.0
    for d in (-0.05, -0.0304, 0.02):
        dn, _, _, _, r, _ = joint(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** d)[keep], keep, F)
        worst = max(worst, abs(dn - d))
    check(f'⓶ T4: a known injected tilt is recovered to {worst:.1e} -- the fitter works',
          worst < 1e-6)
    b = CS.bin_spectrum(LS, DL)[keep]
    ok_scale = True
    for frac in (0.01, 0.05):
        got = (CS.bin_spectrum(LS, DL * (1 + frac))[keep] - b) / sd
        ok_scale &= bool(np.allclose(got, frac * b / sd, rtol=1e-9))
    check('⓶ᵇ ⛔ AND THE SCALE, WHICH ⓶ IS BLIND TO: a tilt-recovery test is unit-free and passes '
          f'whatever the units are. The banked spectra are in arbitrary units -- the normalisation '
          f'is x{A_UNITS:.0f} -- so a residual divided by plik sigma WITHOUT it is wrong by that '
          f'factor. A known fractional perturbation must land where the data\'s own errors say',
          ok_scale)
    check('⓶ᶜ and the pipeline reproduces chi2_of on the same spectrum and window',
          abs(CS.chi2_of(LS, RAW, lmax=1759)[0] - 630.46) < 0.5)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- *** THE JOINT FIT: THE RESIDUAL IS THE PREDICTED SHAPE ***')
    print('  ' + '=' * 74)
    tgt = CS.bin_spectrum(LS, DL * sig(LS))[keep]
    dn, sdn, c1, A1, r1, at = joint(tgt, keep, F)
    c0 = at(0.0)[0]
    n = int(keep.sum())
    pred = CS.bin_spectrum(LS, DL * (sig(LS) - A1 * (LS / 1000.0) ** dn))[keep]
    corr = float(np.corrcoef(r1, pred)[0, 1])
    print(f'      window l = {int(CS.BIN_LO[keep][0])}-{int(CS.BIN_HI[keep][-1])}, {n} covered bins')
    print(f'      Delta n_s = {dn:+.5f} +/- {sdn:.5f}   ({abs(dn)/sdn:.1f} sigma of this '
          f'dataset\'s own tilt error)')
    print(f'      chi^2/bin  {c0/n:.4f} (amplitude only)  ->  {c1/n:.4f} (with the tilt)   '
          f'{100*(1-c1/c0):.1f}% absorbed')
    check(f'⓷ *** the residual after the joint fit correlates with the analytic '
          f'(Gaussian - best power law) at {corr:.6f} -- r6409 predicted a Gaussian-shaped residual '
          f'no tilt removes, and that is exactly what is there ***',
          corr > 0.999999)
    check(f'⓷ᵇ and it SURVIVES: {c1/n:.3f} chi^2/bin over the 185-bin ceiling window, against '
          f'C62\'s data-shape {C62_DATA_SHAPE} and instrument {C62_INSTRUMENT} -- larger than '
          f'either, so the prediction is confirmed at a size bigger than the bound quoted for it',
          c1 / n > C62_INSTRUMENT)
    check(f'⓷ᶜ ⌗ and this route independently reproduces C62\'s INSTRUMENT-route displacement: '
          f'{dn:+.4f} against its -0.0847, agreeing to '
          f'{100*abs(dn-(-0.0847))/0.0847:.0f}% by a different method on a different spectrum',
          abs(dn - (-0.0847)) / 0.0847 < 0.05)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭ THE DISPLACEMENT IS NOT A NUMBER: IT IS A FUNCTION OF THE WINDOW')
    print('  ' + '=' * 74)
    print(f"      {'window':>14} {'bins':>5} {'Delta n_s':>11} {'chi2/bin':>10} {'absorbed':>9}")
    rows = []
    for lo, hi in ((100, 1760), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)):
        kw = window(lo, hi)
        if kw.sum() < 12:
            continue
        Fw, _ = _fisher(kw)
        tw = CS.bin_spectrum(LS, DL * sig(LS))[kw]
        d_, _s, cw, _A, _r, aw = joint(tw, kw, Fw)
        nw = int(kw.sum())
        rows.append((lo, hi, nw, d_, cw / nw, 100 * (1 - cw / aw(0.0)[0])))
        print(f'      {f"{lo}-{hi}":>14} {nw:>5} {d_:>+11.5f} {cw/nw:>10.4f} {rows[-1][5]:>8.1f}%')
    spread = max(abs(r[3]) for r in rows) / min(abs(r[3]) for r in rows)
    check(f'⓸ *** the fitted displacement runs over a factor of {spread:.1f} across windows of the '
          f'SAME data -- so "the displacement" is the value of nothing without its window, which is '
          f'r6409\'s reading arriving as a measurement ***',
          spread > 3)
    check('⓸ᵇ and absorption improves monotonically as the window narrows upward, which is why a '
          'restricted window makes the wash look complete',
          rows[1][5] > rows[0][5] and rows[4][5] > rows[1][5])

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⓹ WHAT IT DOES TO THE COMPARISON, IN THE LIKELIHOOD\'S OWN UNITS')
    print('  ' + '=' * 74)
    d = CS.X_DATA[keep]

    def sky(base):
        def at_(x):
            m = CS.bin_spectrum(LS, base * (LS / 1000.0) ** x)[keep]
            A = float((m @ F @ d) / (m @ F @ m))
            r = d - A * m
            return float(r @ F @ r)
        o = minimize_scalar(at_, bounds=(-3, 3), method='bounded', options={'xatol': 1e-10})
        return at_(0.0), at_(float(o.x)), float(o.x)

    a_no, b_no, _ = sky(DL)
    a_sg, b_sg, dn_sky = sky(DL * sig(LS))
    cost_A, cost_T = a_sg - a_no, b_sg - b_no
    print(f'      no signature: chi^2 {a_no:8.2f} (A only)   {b_no:8.2f} (A + tilt)')
    print(f'      signature on: chi^2 {a_sg:8.2f} (A only)   {b_sg:8.2f} (A + tilt, '
          f'dn = {dn_sky:+.4f})')
    check(f'⓹ the signature costs {cost_A:+.1f} chi^2 with amplitude alone and {cost_T:+.1f} after '
          f'the tilt is refitted, over {n} bins -- so the joint fit IMPROVES the comparison by '
          f'{cost_A-cost_T:.1f}, absorbing {100*(1-cost_T/cost_A):.0f}%, and does NOT remove it',
          cost_T > 0 and cost_T < cost_A)
    check(f'⓹ᵇ ⌗ and the sky-compensating tilt is BLUE ({dn_sky:+.4f}) where the degeneracy fit\'s '
          f'is RED ({dn:+.4f}) -- different questions, kept apart (T2)',
          dn_sky > 0 > dn)

    print()
    print('  ' + '=' * 74)
    print('  PART 6 -- CONTROL: r = 1, no signature, the construction must go silent')
    print('  ' + '=' * 74)
    d0, _, c00, _, r00, _ = joint(CS.bin_spectrum(LS, DL)[keep], keep, F)
    print(f'      Delta n_s = {d0:+.2e}   chi^2 = {c00:.2e}   max|resid| = '
          f'{np.max(np.abs(r00/sd)):.2e} sigma')
    check('⓺ with no signature the fit returns zero displacement and zero residual, so what PART 3 '
          'measures is the signature and not an artefact of the machinery',
          abs(d0) < 1e-8 and c00 < 1e-12)

    print()
    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f_ in FAILED:
            print(f'      {f_[:110]}')
        return 1
    print('  *** THE JOINT FIT CONFIRMS r6409 BY MEASUREMENT: the residual is the Gaussian,')
    print('    to a correlation of 1.000000, and it survives at 1.50 chi^2/bin over P15\'s own')
    print('    185-bin window -- LARGER than either bound C62 left. The bound the order named')
    print('    was in chi^2 and was restated in sigma, and was the more favourable of C62\'s two.')
    print('    The tilt takes 70% of the signature and 76% of its cost against the sky, leaving')
    print('    +84.5 chi^2 over 171 bins.  ⌗ n_s is INHERITED here: the displacement is a')
    print('    different input, not a tension -- and it is not one number but a function of the')
    print('    window, running a factor of 6.3 across windows of the same data.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
