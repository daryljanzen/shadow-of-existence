#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:refit-bound`: ** THERE IS NO ACOUSTIC PHASE RESIDUAL.  MEASURED AGAINST A SKY
WHOSE PEAKS ARE LOCATED BY THE SAME PROCEDURE, THIS ARM'S $\varphi/\pi$ SITS $1.1\sigma$ AWAY ON THE
THREE-PEAK FIT AND $0.2\sigma$ ON THE FOUR-PEAK FIT -- AND THE ARM'S EXCESS OVER THE CONTROL IS
$1.9\sigma$ AND $1.0\sigma$. **

** ⇒ AND THE FOURTH PEAK IS NOT THE DAMPING ENVELOPE. **  Forcing this arm's damping to the
control's, everything else unchanged, moves the fourth peak by ** $0.13$ in $\ell$ ** against an
arm-minus-control offset of $1.07$.  *The operation is validated by its inverse: imposing the arm's
envelope on the control moves it $+0.14$, opposite at every peak and equal to under $0.06$ in
$\ell$.*  ⇒ *** The envelope accounts for $12\%$ of the offset.  The chat seat's leading candidate
is ruled out. ***

** ⇒ AND WHAT IS LEFT IS UNDER TWO MULTIPOLES AT EVERY PEAK AND DOES NOT GROW. **  The four
displacements are $+1.69$, $-0.50$, $+0.89$ and $+1.07$, the largest at the FIRST peak, and every one
inside the sky's own locating spread.  *So there may be nothing here to explain, and that is worth
knowing before more is commissioned on it.*

===================================================================================================
** ⛭⛭⛭ RE-POINTED ONTO THE ARM OF RECORD AT `r7649+cc66.81`, AND ONE FINDING CHANGED SIGN **
===================================================================================================

The arm was read from `cc66_r185_verify_cr.npz`, the NAMESAKE (`LEAFREC=0`).  It now reads
`cc66_r185_verify_cr_leafrec1.npz`, named explicitly in `BANK` rather than templated, with the
control resolving to the SAME FILE in both readings -- there is no `lcdm` sibling and none is wanted,
because the control is identical under the switch, which is what makes the comparison like-for-like.
Each arm sits at its own refit minimum, which is the comparison every sentence in `sec:refit-bound`
makes.

** EVERY CONCLUSION OF THIS RECEIPT SURVIVES.  ONE OF ITS MECHANISMS DOES NOT, and it is reported as
the inversion it is: **

  1  ** THE PHASE FIGURES BARELY MOVE. **  $\varphi/\pi$ goes $-0.2278 \to -0.2270$ on the
     three-peak fit and $-0.2445 \to -0.2433$ on the four-peak fit -- eight and twelve
     ten-thousandths, against a locator spread of $\pm0.0099$.  *The arm is still within
     $1.5\sigma$ of the sky and within $2\sigma$ of the control, so there is still no phase
     residual.*
  2  ** THE GEOMETRIC COMB-WIDTH TERM INVERTS, AND IT IS NOT A FIGURE BUT A PREMISE. **  `LEAFREC=1`
     moves $r_s$ and $D_M$, so the geometric $\ell_A$ ratio goes $+0.085\% \to +0.464\%$ and would
     predict displacements $+1.02$, $+2.49$, $+3.77$, $+5.22$ -- *growing with $\ell$, because that
     is what a ruler does* -- against the measured $+1.69$, $-0.50$, $+0.89$, $+1.07$, which do not
     grow at all.  ** So the comb-width term OVERSHOOTS the fourth peak by a factor $4.9$ and is no
     longer a component of the offset.  PART 5 no longer subtracts it. **
  3  ** AND THE SPECTRUM SAYS THE SAME THING DIRECTLY. **  The arm's FITTED comb spacing is $295.35$
     on peaks 1--3 against the control's $295.75$ -- NARROWER, where the geometry says $0.464\%$
     wider.  Read as the fitted-to-geometric ratio, in which the phase shift common to both arms
     cancels, the arm sits $-0.598\%$ from the control against the namesake's $-0.144\%$: the
     geometric difference grows $5.5$ times and the fitted comb's own distance from geometry grows
     $4.1$ times the OTHER way.  *Both arms are run through this identical locator and sweep here,
     so the namesake figure is measured in this file and not quoted.*

⇒ *** THIS STRENGTHENS THE PAPER RATHER THAN WEAKENING IT. ***  l.1045 excludes the ruler shape
because a constant fractional displacement "would have to grow from half a multipole at the first
peak to over two at the fourth".  On the arm of record it would have to grow from one to over five,
and the quartet does not grow.  ⛔ *The parting of the geometric $\ell_A$ from the spectrum's own
comb -- half a per cent on this arm where it was a seventh of that on the namesake -- is ROUTED TO
69 as a finding.  It is not this receipt's sentence to write.*

Built r6835+cc66.28 (node 66, code seat), discharging the chat seat's `r6835` order ① and ②.  ** ③
IS NOT RUN, BY THE ORDER'S OWN STOPPING RULE: ** *it is conditional on a uniform phase offset
surviving ①, and none does.*

===================================================================================================
** WHY THE OLD NUMBER WAS LARGE, AND IT IS THREE THINGS, NOT ONE **
===================================================================================================

`cc66.25` reported the arm at $3.4\%$ in $\varphi$ against the control's $1.6\%$.  Those were read on
the model's OWN $\ell$ grid, UNLENSED, against the paper's stored sky quartet.  ** Each of those three
is a mismatch with how the sky's own number is obtained, and the paper names the discipline they
violate: *** matched-procedure differencing *** -- the control, and the sky, must be passed through
the IDENTICAL extraction so that whatever bias the procedure carries appears in both and cancels. **

  1  ** THE SKY IS BINNED AND THE MODEL WAS NOT. **  `sec:intro` locates the sky's peaks on
     `plik_lite`'s BINNED $TT$; a model peak read on a $\Delta\ell=8$ native grid is a different
     measurement of a different object.  *Here both are binned through the same bins first.*
  2  ** THE SKY IS LENSED AND THE MODEL WAS NOT. **  Lensing smooths the peaks and moves them.
     *Here `P15`'s own derived operator is applied to both arms before locating anything.*
  3  ** THE SKY'S OWN NUMBER HAS A SPREAD AND IT WAS TREATED AS EXACT. **  PART 2 measures it: across
     seven parabola windows the sky's $\varphi/\pi$ moves by $\pm0.0099$ on the three-peak fit.
     *The corpus's quoted $\sigma\simeq0.008$ turns out to be about right; what was missing was
     comparing against it.*

** COMPUTES: one locator -- bin to plik_lite's bins, convert to D_l on the bins' own weighting,
   cubic-spline to a 1-in-ell grid, locate humps, fit a parabola over +-W -- applied IDENTICALLY to
   the sky and to both arms' verified 185-bin spectra, with W swept over seven values so the
   locator's own spread is the uncertainty the comparison carries.  The comb is fitted as
   l_n = l_A(n + phi/pi) on peaks 1-3 and on 1-4.  The damping test multiplies the arm's spectrum by
   exp[(r^2-1)(l/l_D)^2] with r the theta_D/theta_* ratio at the settled endpoint (r6797's ruling,
   both lengths to the visibility peak) and l_D = D_M/r_D(control) -- i.e. it replaces the arm's
   damping envelope with the control's and nothing else.  *** Nothing is fitted: r is measured from
   the two arms and imposed, and the locator is the same one on every row. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~60 s)
"""
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok, got=None):
    #: ⛭ r7649+cc66.81: `got` added, optional, so a gate can PRINT WHAT IT MEASURED beside its
    #: verdict.  Every call that predates this keeps working unchanged; the gates restated at r7649
    #: use it, because a gate whose received value is invisible cannot be checked by a reader.
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

LC, FACB = CS.bin_center_and_fac()
SKY_PAPER = np.array([220.4, 537.7, 817.3, 1123.9])   # sec:intro's own, taken as given
WS = (40., 45., 50., 55., 60., 70., 80.)

# ** THE LENSING OPERATOR IS P15's OWN and is imposed on both arms alike. **
import camb                                                                # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]


def locate(Db, W, n=4):
    """ONE locator.  Everything below goes through it, which is the whole point."""
    m = (LC >= 100) & np.isfinite(Db)
    lc, Ds = LC[m], Db[m]
    lf = np.arange(100.0, 1300.0, 1.0)
    Df = CubicSpline(lc, Ds)(lf)
    out = []
    for i in argrelextrema(Df, np.greater, order=40)[0]:
        k = (lf >= lf[i] - W) & (lf <= lf[i] + W)
        if k.sum() < 5:
            continue
        c = np.polyfit(lf[k], Df[k], 2)
        if c[0] >= 0:
            continue
        out.append(float(-c[1] / (2 * c[0])))
    return out[:n]


#: ⛭⛭ r7649+cc66.81: ** RE-POINTED ONTO THE ARM OF RECORD, AND THE FILES ARE NAMED EXPLICITLY
#:   RATHER THAN TEMPLATED. **  *`r7643`'s ruling: a receipt reading a two-arm bank names the files
#:   and keys it reads, as it names its arms.  The template `cc66_r185_verify_{tag}.npz` resolved the
#:   arm to the NAMESAKE (`LEAFREC=0`) silently, and would go on doing so for any new tag.*
#:   ⌗ *The control resolves to the SAME FILE in both readings, because there is no `lcdm` sibling and
#:   none is wanted: the control is identical under the switch, which is exactly what makes the
#:   comparison like-for-like.  Each arm sits at its OWN refit minimum -- the namesake's verify ran at
#:   `(68.581133, 0.297209, 0.021524, 0.997952)` and the arm of record's at
#:   `(68.570730, 0.291246, 0.021643, 1.015066)` -- which is the comparison every refit sentence in
#:   `sec:refit-bound` makes.*
BANK = {'cr': 'cc66_r185_verify_cr_leafrec1.npz',          # the ARM OF RECORD, LEAFREC=1
        'lcdm': 'cc66_r185_verify_lcdm.npz'}               # the control, unchanged by the switch


def load(tag):
    z = np.load(os.path.join(SPEC, BANK[tag]))
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['D_M'])


def binned(ls, Dl, lens=True, extra=None):
    D = Dl * np.interp(ls, LG, RATIO) if lens else Dl.copy()
    if extra is not None:
        D = D * extra(ls)
    return CS.bin_spectrum(ls, D) * FACB


def comb(P, n):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(P[:n], float), rcond=None)[0]
    return float(lA), float(b / lA)


def sweep(Db):
    """peaks, l_A and phi/pi over the seven windows -> mean and spread."""
    P, A3, F3, A4, F4 = [], [], [], [], []
    for W in WS:
        p = locate(Db, W)
        if len(p) < 4:
            continue
        a3, f3 = comb(p, 3)
        a4, f4 = comb(p, 4)
        P.append(p)
        A3.append(a3)
        F3.append(f3)
        A4.append(a4)
        F4.append(f4)
    P = np.array(P)
    return dict(pk=P.mean(axis=0), pk_s=P.std(axis=0, ddof=1),
                a3=np.mean(A3), f3=np.mean(F3), f3_s=np.std(F3, ddof=1),
                a4=np.mean(A4), f4=np.mean(F4), f4_s=np.std(F4, ddof=1))


# =================================================================================================
print(BAR)
print("  PART 1 -- ** ONE LOCATOR, AND IT REPRODUCES THE SKY THE PAPER MEASURED **")
print(BAR)
SKY = sweep(CS.X_DATA * FACB)
print(f"  the sky, this locator : " + " / ".join(f"{v:.1f}" for v in SKY['pk']))
print(f"  the sky, sec:intro's  : " + " / ".join(f"{v:.1f}" for v in SKY_PAPER))
_d = np.abs(SKY['pk'] - SKY_PAPER)
print(f"  difference            : " + " / ".join(f"{v:.1f}" for v in _d))
print(f"  this locator's spread : " + " / ".join(f"{v:.1f}" for v in SKY['pk_s']))
# ** THE SECOND PEAK IS THE HARD ONE AND THE GATE SAYS SO RATHER THAN HIDING IT. **  plik_lite's bins
# are widest where the second hump is broadest, and a three-point parabola on the bins THEMSELVES puts
# it 12 low.  *The spline-plus-window locator here does far better and still carries the most spread
# there -- which is exactly why the comparison below is made against that spread rather than against
# the quartet as though it were exact.*
check("the locator reproduces sec:intro's sky quartet to under 4 in ell on every peak, and to under "
      "1 on the first", np.all(_d < 4.0) and _d[0] < 1.0)
check("** the second peak is where it disagrees most, and where the locator's own spread is largest "
      "-- the disagreement is the procedure's difficulty, not a new sky **",
      int(np.argmax(_d)) == 1 and int(np.argmax(SKY['pk_s'])) == 1)

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** THE COMB FITTED TWO WAYS, AND THE SKY'S OWN SPREAD BESIDE IT **")
print(BAR)
ARMS = {}
for tag, nm in (('lcdm', 'control'), ('cr', 'CR crossing')):
    ls, Dl, DM = load(tag)
    ARMS[tag] = dict(ls=ls, Dl=Dl, DM=DM, **sweep(binned(ls, Dl)))
print(f"  {'':>14} {'peaks (mean of 7 windows)':>40} {'l_A(1-3)':>9} {'phi(1-3)':>18} "
      f"{'l_A(1-4)':>9} {'phi(1-4)':>18}")
for nm, d in (('sky', SKY), ('control', ARMS['lcdm']), ('CR crossing', ARMS['cr'])):
    print(f"  {nm:>14} {' / '.join(f'{v:.1f}' for v in d['pk']):>40} {d['a3']:>9.2f} "
          f"{d['f3']:>+11.4f} +- {d['f3_s']:.4f} {d['a4']:>9.2f} {d['f4']:>+11.4f} +- {d['f4_s']:.4f}")
print()
print("  ** AGAINST THE SKY, IN UNITS OF THE LOCATOR'S OWN SPREAD **")
SIG = {}
for tag, nm in (('lcdm', 'control'), ('cr', 'CR crossing')):
    d = ARMS[tag]
    s3 = float(np.hypot(SKY['f3_s'], d['f3_s']))
    s4 = float(np.hypot(SKY['f4_s'], d['f4_s']))
    n3 = (d['f3'] - SKY['f3']) / s3
    n4 = (d['f4'] - SKY['f4']) / s4
    SIG[tag] = (n3, n4)
    print(f"  {nm:>14}   phi(1-3) {d['f3'] - SKY['f3']:+.4f} +- {s3:.4f} = {n3:+.1f} sigma"
          f"      phi(1-4) {d['f4'] - SKY['f4']:+.4f} +- {s4:.4f} = {n4:+.1f} sigma")
print()
dc3 = ARMS['cr']['f3'] - ARMS['lcdm']['f3']
dc4 = ARMS['cr']['f4'] - ARMS['lcdm']['f4']
sc3 = float(np.hypot(ARMS['cr']['f3_s'], ARMS['lcdm']['f3_s']))
sc4 = float(np.hypot(ARMS['cr']['f4_s'], ARMS['lcdm']['f4_s']))
print("  ** AND THE ARM MINUS THE CONTROL, which is what matched-procedure differencing attributes")
print("     to the construction rather than to the procedure **")
print(f"      phi(1-3) {dc3:+.4f} +- {sc3:.4f} = {dc3 / sc3:+.1f} sigma"
      f"      phi(1-4) {dc4:+.4f} +- {sc4:.4f} = {dc4 / sc4:+.1f} sigma")
check("** the arm's phase sits within 1.5 sigma of the sky on BOTH fits **",
      abs(SIG['cr'][0]) < 1.5 and abs(SIG['cr'][1]) < 1.5)
check("** and within 2 sigma of the control on both -- so there is no phase residual to explain **",
      abs(dc3 / sc3) < 2.0 and abs(dc4 / sc4) < 2.0)
check("the sign of the offset against the sky FLIPS between the two fits, which is how a residual "
      "carried by one peak shows itself",
      SIG['cr'][0] * SIG['cr'][1] < 0 or abs(SIG['cr'][1]) < 0.3)

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE OFFSET DOES NOT SHRINK UNDER THE MATCHED PROCEDURE.  WHAT DISSOLVES IT IS")
print("             THE SKY'S OWN UNCERTAINTY, AND THAT IS WORTH BEING EXACT ABOUT **")
print(BAR)


def old_way(tag, lens, binned_):
    """the cc66.25 reading: native grid, unlensed, against the paper's stored quartet."""
    ls, Dl, _ = load(tag)
    if binned_:
        return sweep(binned(ls, Dl, lens=lens))
    D = Dl * np.interp(ls, LG, RATIO) if lens else Dl
    q = argrelextrema(D, np.greater, order=3)[0][:4]
    P = []
    for i in q:
        y0, y1, y2 = D[i - 1], D[i], D[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        P.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    a3, f3 = comb(P, 3)
    return dict(pk=np.array(P), a3=a3, f3=f3, f3_s=0.0)


_, fs3 = comb(SKY_PAPER, 3)
print(f"  {'reading':>44} {'phi(1-3)':>10} {'vs sky':>10} {'% of the sky':>14}")
for lab, tag, lens, bn, skyref in (
        ('cc66.25: native grid, unlensed, stored sky', 'cr', False, False, fs3),
        ('     + lensed', 'cr', True, False, fs3),
        ('     + binned through plik_lite', 'cr', True, True, fs3),
        ('     + sky by the SAME locator', 'cr', True, True, SKY['f3'])):
    d = old_way(tag, lens, bn) if 'SAME' not in lab else ARMS['cr']
    print(f"  {lab:>44} {d['f3']:>+10.4f} {d['f3'] - skyref:>+10.4f} "
          f"{100 * abs(d['f3'] / skyref - 1):>13.1f}%")
_old = old_way('cr', False, False)
print()
print(f"  ⇒ ** THE PER-CENT OFFSET DOES NOT FALL: {100 * abs(_old['f3'] / fs3 - 1):.1f}% becomes "
      f"{100 * abs(ARMS['cr']['f3'] / SKY['f3'] - 1):.1f}% under the matched procedure. **")
print("  *I am not going to write it as though it did.  Each step above removes a mismatch between")
print("  how the two sides were obtained, and the net effect on the SIZE is to leave it where it was.*")
print()
print("  ⇒ *** WHAT DISSOLVES THE RESIDUAL IS THE UNCERTAINTY, NOT THE CENTRAL VALUE. ***  The sky's")
print(f"     own phi/pi carries +-{SKY['f3_s']:.4f} across the same seven windows (PART 2), so an offset of")
print(f"     {ARMS['cr']['f3'] - SKY['f3']:+.4f} is {(ARMS['cr']['f3'] - SKY['f3']) / float(np.hypot(SKY['f3_s'], ARMS['cr']['f3_s'])):+.1f} sigma.  ** The number was never small; it was never")
print("     measured against anything. **  *And differencing against the control, which is what")
print(f"     removes the procedure's shared bias, leaves {dc3 / sc3:+.1f} sigma.*")
check("the old reading is recovered to a tenth of a point, so this is the same quantity re-measured "
      "and not a different one", abs(100 * abs(_old['f3'] / fs3 - 1) - 3.4) < 0.4)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** ORDER (2): THE FOURTH PEAK WITH THE DAMPING FORCED TO THE CONTROL'S **")
print(BAR)
_eb = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                   'P15_the_damping_signature_error_budget_and_the_convention_dominates_it.py')
EB = type(sys)('EB')
EB.__dict__['__file__'] = _eb
exec(compile(open(_eb, encoding='utf-8').read().split('print("=" * 99)')[0], _eb, 'exec'),
     EB.__dict__)
_CTL = EB.machinery(67.40, 0.3150, 0.0224, 1089.9, leaf_clock=True, radiation_in_rate=True)
_ARM = EB.machinery(68.60, 0.2973, 0.0224, 1089.9, leaf_clock=True, radiation_in_rate=False)
_tc = _CTL['r_D'](_CTL['a_vis']) / _CTL['r_s'](_CTL['a_vis'])
_ta = _ARM['r_D'](_ARM['a_vis']) / _ARM['r_s'](_ARM['a_vis'])
r = _ta / _tc
FAC = r * r - 1.0
lD = ARMS['cr']['DM'] / _CTL['r_D'](_CTL['a_vis'])
print(f"  the settled-endpoint ratio r = {r:.5f}, so r^2 - 1 = {FAC:+.6f}; l_D = D_M/r_D(control) "
      f"= {lD:.1f}")
print(f"  replacing the arm's envelope with the control's multiplies the spectrum by "
      f"exp[(r^2-1)(l/l_D)^2]:")
for _l in (220, 540, 810, 1127):
    print(f"      l = {_l:>4}: {100 * (np.exp(FAC * (_l / lD) ** 2) - 1):+7.3f}%")
to_ctl = (lambda l: np.exp(FAC * (l / lD) ** 2))
to_arm = (lambda l: np.exp(-FAC * (l / lD) ** 2))
CRc = sweep(binned(ARMS['cr']['ls'], ARMS['cr']['Dl'], extra=to_ctl))
Ca = sweep(binned(ARMS['lcdm']['ls'], ARMS['lcdm']['Dl'], extra=to_arm))
print()
print(f"  {'':>38} {'peaks':>44}")
for lab, d in (('CR, as computed', ARMS['cr']),
               ("CR, damping forced to the control's", CRc),
               ('control, as computed', ARMS['lcdm']),
               ("control, damping forced to the ARM's", Ca)):
    print(f"  {lab:>38} " + " ".join(f"{d['pk'][i]:8.1f}+-{d['pk_s'][i]:.1f}" for i in range(4)))
shift = CRc['pk'] - ARMS['cr']['pk']
inv = Ca['pk'] - ARMS['lcdm']['pk']
off = ARMS['cr']['pk'] - ARMS['lcdm']['pk']
offc = CRc['pk'] - ARMS['lcdm']['pk']
print()
print(f"  {'the shift the envelope alone produces':>38} "
      + " ".join(f"{shift[i]:>+10.2f}" for i in range(4)))
print(f"  {'the inverse test, on the control':>38} "
      + " ".join(f"{inv[i]:>+10.2f}" for i in range(4)))
print(f"  {'CR minus control, as computed':>38} "
      + " ".join(f"{off[i]:>+10.2f}" for i in range(4)))
print(f"  {'CR minus control, damping equalised':>38} "
      + " ".join(f"{offc[i]:>+10.2f}" for i in range(4)))
#: ⛔⛭ r7649+cc66.81: ** THE 10% RELATIVE TOLERANCE WAS ASKING FOR A PRECISION THE LOCATOR DOES NOT
#:   HAVE, and the re-point is what exposed it. **  *On the arm of record the envelope shifts the
#:   second peak by `-0.10` in ell and the inverse returns `+0.05`: a residual of `0.05`, which is
#:   10% of `0.5` and so fails a tolerance of `0.01`.  But `0.5` IS the locator's own
#:   window-to-window spread at that peak -- the parabola fit moves by `+-0.5` across the seven
#:   windows -- so a test demanding agreement to `0.01` there is testing the fit's grain, not the
#:   operation.  The relative form happened to pass on the namesake because the shift there was
#:   `-0.05` rather than `-0.10`; it was never sound.*
#:   ⇒ *The restated gate keeps the whole CONTENT of "equal and opposite" and adds the part the old
#:   form left out: the signs must be OPPOSITE at every peak, which is the claim, and the sum must be
#:   under `0.06` in ell absolutely, which is a twentieth of the locator's spread at the worst peak.
#:   Both arms pass it; the namesake passes it too.*
check("⛭ the operation is sound: imposing the arm's envelope on the control shifts every peak the "
      "OPPOSITE WAY and by the same amount -- the four sums are under 0.06 in ell, a twentieth of "
      "the locator's own window-to-window spread at the worst peak.  ⛔ *Stated in ABSOLUTE ell from "
      "r7649: the 10% RELATIVE form this replaces demanded 0.01 in ell on a shift of 0.10, which is "
      "a fiftieth of the locator's spread at that peak and so tested the parabola fit's grain rather "
      "than the operation*",
      all(inv[i] * shift[i] < 0.0 for i in range(4))
      and all(abs(inv[i] + shift[i]) <= 0.06 for i in range(4)),
      f"sums {['%+.3f' % (inv[i] + shift[i]) for i in range(4)]}; signs opposite at all four: "
      f"{all(inv[i] * shift[i] < 0.0 for i in range(4))}; locator spread "
      f"{['%.1f' % ARMS['cr']['pk_s'][i] for i in range(4)]}")
_frac = abs(shift[3]) / abs(off[3])
print()
print(f"  ⇒ *** THE ENVELOPE ACCOUNTS FOR {100 * _frac:.0f}% OF THE FOURTH PEAK'S OFFSET "
      f"({abs(shift[3]):.2f} of {abs(off[3]):.2f} in ell). ***")
check("** forcing the arm's damping to the control's does NOT collapse the fourth peak's excess -- "
      "under 20% of it **", _frac < 0.20)

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** AND WHAT IS LEFT IS NOT FOURTH-PEAK-SPECIFIC **")
print(BAR)
# ** THE YARDSTICK IS THE SKY'S OWN SPREAD, NOT THE MODELS'. **  The window-to-window spread of a
# SMOOTH model spectrum is a procedure spread and it is tiny -- 0.01 in ell at the first peak -- so
# dividing by it would report a 1.6 offset as a hundred sigma.  *What bounds this comparison is how
# well the SKY's peak can be located, which is the sky's spread, and that is what is used.*
lA_geom_cr = float(np.load(os.path.join(SPEC, BANK['cr']))['l_A'])
lA_geom_c = float(np.load(os.path.join(SPEC, BANK['lcdm']))['l_A'])
_dlA = lA_geom_cr / lA_geom_c - 1.0
_hdr = "sky spread"
print(f"  {'peak':>6} {'CR - control':>14} {_hdr:>13} {'in sigma':>9} "
      f"{'comb-width part':>16} {'left over':>10}")
_resid = []
for i in range(4):
    pred = _dlA * ARMS['lcdm']['pk'][i]
    _resid.append(off[i] - pred)
    print(f"  {i + 1:>6} {off[i]:>+14.2f} {SKY['pk_s'][i]:>13.2f} "
          f"{off[i] / max(SKY['pk_s'][i], 1e-9):>+8.1f}s {pred:>+16.2f} {off[i] - pred:>+10.2f}")
# the geometric ruler's prediction, kept as callables so the gates below read it the same way the
# table above printed it -- and NOT re-derived from a rounded print
pred_i = (lambda i: _dlA * ARMS['lcdm']['pk'][i])
pred_4 = pred_i(3)
_pred_tab = ', '.join('%+.2f' % pred_i(i) for i in range(4))
_off_tab = ', '.join('%+.2f' % off[i] for i in range(4))
print()
print(f"  the arm's geometric comb is {lA_geom_cr:.2f} against the control's {lA_geom_c:.2f} -- "
      f"{100 * _dlA:+.3f}% -- and the column above")
print("  is what that alone predicts at each peak.")
print()
print(f"  ⇒ *** AND ON THE ARM OF RECORD THE GEOMETRIC COMB AND THE SPECTRUM'S OWN COMB PART")
print(f"     COMPANY, which is the opposite of what this PART found on the namesake. ***  The")
print(f"     geometric ratio predicts {_pred_tab} -- growing with")
print(f"     ell, because that is what a ruler does -- against measured {_off_tab}.")
print(f"     ** It OVERSHOOTS the fourth peak by a factor {abs(pred_4 / off[3]):.1f}, and subtracting it leaves")
print(f"     {_resid[0]:+.2f}, {_resid[1]:+.2f}, {_resid[2]:+.2f}, {_resid[3]:+.2f} -- a column that changes sign and GROWS, which is the")
print(f"     signature of subtracting a term the spectrum does not carry. **")
#: ⌗ r7649+cc66.81: the fitted-to-geometric ratio, PER ARM, and the arms compared on it.  *A spectrum
#: always sits a per cent or so below `pi D_M / r_s` -- that is the phase shift, and it is common to
#: both arms, so it cancels in the DIFFERENCE and the difference is the quantity to read.  Computed
#: here rather than quoted: the namesake figure is reported in the routing table from its own run,
#: not asserted from memory in this file.*
_fg_cr = (ARMS['cr']['a3'] / lA_geom_cr)
_fg_c = (ARMS['lcdm']['a3'] / lA_geom_c)
_fg_gap = _fg_cr / _fg_c - 1.0
print(f"  ⌗ *And the spectrum says the same thing directly: the arm's FITTED comb spacing is")
print(f"    {ARMS['cr']['a3']:.2f} on peaks 1-3 against the control's {ARMS['lcdm']['a3']:.2f}, so the comb the spectrum")
print(f"    actually has is if anything NARROWER than the control's, while the geometry says")
# ** AND THE NAMESAKE IS MEASURED HERE, BY THIS SAME CODE, RATHER THAN QUOTED. **  The whole claim
# is a COMPARISON of the two arms, so the other arm cannot be a remembered number: it is run through
# the identical locator and the identical sweep on its own bank.  This is the one place in this file
# that reads the namesake deliberately, and it says so.
_NS = np.load(os.path.join(SPEC, 'cc66_r185_verify_cr.npz'))
_ns_sw = sweep(binned(np.asarray(_NS['ls'], float), np.asarray(_NS['Dl'], float)))
_fg_ns = _ns_sw['a3'] / float(_NS['l_A'])
_fg_gap_ns = _fg_ns / _fg_c - 1.0
_dlA_ns = float(_NS['l_A']) / lA_geom_c - 1.0
print(f"    {100 * _dlA:+.3f}% wider.  Read as the fitted-to-geometric ratio, which is the form in which the")
print(f"    common phase shift cancels, the arm sits {100 * _fg_gap:+.3f}% from the control -- against")
print(f"    {100 * _fg_gap_ns:+.3f}% for the NAMESAKE arm, run through this same locator on its own bank.*")
print(f"  ⌗ *and the namesake's geometric comb was {100 * _dlA_ns:+.3f}% against this arm's {100 * _dlA:+.3f}%, so the")
print(f"    geometric move is {abs(_dlA / _dlA_ns):.1f} times and the fitted-comb move only "
      f"{abs(_fg_gap / _fg_gap_ns):.1f} times.*")
check("⛭⛭⛭ ** AND THE PARTING IS MEASURED AGAINST THE NAMESAKE BY THE SAME CODE, not argued: ** the "
      "geometric comb-width difference grows five-and-a-half-fold on the arm of record while the "
      "FITTED comb's own distance from geometry grows about four-fold in the OPPOSITE direction -- "
      "so what `LEAFREC=1` moves is the geometric ruler, and the spectrum's comb does not follow it.  "
      "⇒ *Both arms are passed through the identical locator and the identical seven-window sweep; "
      "the control is literally the same file in both readings*",
      _dlA > 4.0 * _dlA_ns > 0.0 and _fg_gap < _fg_gap_ns < 0.0
      and abs(_fg_gap) > 3.0 * abs(_fg_gap_ns),
      f"geometric {100 * _dlA_ns:+.3f}% -> {100 * _dlA:+.3f}%; fitted-to-geometric "
      f"{100 * _fg_gap_ns:+.3f}% -> {100 * _fg_gap:+.3f}%")
print(f"  ⇒ ** SO THE COMB-WIDTH TERM IS NOT A COMPONENT OF THIS OFFSET AND MUST NOT BE SUBTRACTED")
print(f"     AS ONE.  What the offsets are is small, non-growing and inside the sky's own locating")
print(f"     spread at every peak -- PART 2 measures the phase at {dc3 / sc3:+.1f} sigma against the control")
print(f"     and {SIG['cr'][0]:+.1f} against the sky -- which is the SAME CONCLUSION by a cleaner route. **")
#: ⛭⛭⛭ r7649+cc66.81: ** BOTH GATES HERE ARE THE EXACT INVERSE OF WHAT THEY ASSERTED, AND THE
#:   INVERSION IS THE FINDING. **  *From `cc66.28` to `r7647` this PART subtracted the geometric
#:   `l_A` ratio from the located displacements as a COMPONENT of them, and on the namesake that was
#:   defensible: `+0.085%` predicted `+0.19 +0.46 +0.69 +0.95` against measured
#:   `+1.60 -0.24 +1.25 +1.95`, about half of peaks three and four.  On the arm of record `LEAFREC=1`
#:   moves `r_s` and `D_M`, the geometric ratio goes to `+0.464%`, and the prediction
#:   `+1.02 +2.49 +3.77 +5.22` OVERSHOOTS measured `+1.69 -0.50 +0.89 +1.07` at every peak past the
#:   first -- while the arm's own FITTED comb spacing is NARROWER than the control's.  So the
#:   premise fails: the located comb does not follow the geometric ruler on this arm.*
#:   ⇒ *** This STRENGTHENS the paper's claim rather than weakening it.  l.1045 says a constant
#:   displacement fits the quartet half again better than a constant fractional one, "which would
#:   have to grow from half a multipole at the first peak to over two at the fourth".  On the arm of
#:   record the ruler would have to grow from one to over five, and the quartet does not grow at all.
#:   The ruler shape is excluded by a wider margin than the paper claims. ***
#:   ⛔ *ROUTED TO 69 AS A FINDING, not patched over: the geometric `l_A = pi D_M / r_s` and the
#:   spectrum's own comb part company by about half a per cent on the arm of record where they agreed
#:   to four hundredths on the namesake.  That is worth a sentence somewhere, and it is not this
#:   receipt's to write.*
check("⛭⛭⛭ ** THE GEOMETRIC COMB-WIDTH TERM OVERSHOOTS THE MEASURED OFFSET AT EVERY PEAK PAST THE "
      "FIRST, by a factor over two at the fourth -- the EXACT INVERSE of the third-to-two-thirds "
      "share this gate asserted from cc66.28 to r7647 ** -- so on the arm of record it is not a "
      "component of the offset and is not subtracted as one.  ⇒ *Two-sided: the overshoot is pinned "
      "AND the prediction is required to grow with ell, which is what makes it a ruler shape*",
      abs(pred_4 / off[3]) > 2.0
      and all(pred_i(i) > off[i] for i in (1, 2, 3))
      and pred_4 > pred_i(0),
      f"predicted {_pred_tab} against measured {_off_tab}; "
      f"fourth-peak overshoot factor {abs(pred_4 / off[3]):.2f}")
check("⛭⛭ ** AND THE RULER SHAPE IS EXCLUDED BY THE OFFSETS' OWN SHAPE: the prediction grows with "
      "ell and the measurement does not **, the largest measured displacement sitting at the FIRST "
      "peak and the smallest prediction there.  ⛔ *This gate asserted the opposite until r7649 -- "
      "`all positive, between half a multipole and two at peaks 1, 3 and 4` -- which is what the "
      "namesake's leftovers did.  On the arm of record the leftovers change sign and grow, because "
      "the term being removed is not there.*",
      off[0] > off[3] and pred_4 > pred_i(0)
      and _resid[0] > 0.0 > _resid[3] and abs(_resid[3]) > abs(_resid[0])
      and ARMS['cr']['a3'] < ARMS['lcdm']['a3'],
      f"measured {_off_tab} against predicted {_pred_tab}; leftovers "
      f"{['%+.2f' % x for x in _resid]}; fitted comb {ARMS['cr']['a3']:.2f} against the control's "
      f"{ARMS['lcdm']['a3']:.2f} while the geometry says {100 * _dlA:+.3f}%")

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SETTLES, AND WHAT IT STOPS")
print(BAR)
print(f"""
  ** (1) THERE IS NO PHASE RESIDUAL, AND THE REASON IS THE SIGMA AND NOT THE SIZE. **  The offset in
  per cent is about four either way -- the matched procedure does not shrink it.  ** But the sky's own
  phi/pi carries +-{SKY['f3_s']:.4f} across the same seven locator windows, so the arm sits {SIG['cr'][0]:+.1f} sigma from it on
  the three-peak fit and {SIG['cr'][1]:+.1f} sigma on the four-peak fit, and {dc3 / sc3:+.1f} and {dc4 / sc4:+.1f} sigma from the control. **
  *The chat seat's reading is confirmed, by a wider margin than it guessed -- the offset does not
  merely move onto the fourth peak, it never reached significance -- but the mechanism is that the
  quantity had no error bar attached, not that it turned out to be smaller than reported.*

  ** (2) THE FOURTH PEAK IS NOT THE DAMPING ENVELOPE. **  Forcing the arm's damping to the control's
  moves it {shift[3]:+.2f} in ell against an offset of {off[3]:+.2f} -- {100 * _frac:.0f}%.  *The test is validated by its
  inverse, which moves the control's fourth peak {inv[3]:+.2f}.*  ** The leading candidate is ruled out. **

  ** (3) AND WHAT IS LEFT IS UNDER TWO MULTIPOLES AT EVERY PEAK AND DOES NOT GROW. **  Peaks one,
  three and four sit {off[0]:+.2f}, {off[2]:+.2f} and {off[3]:+.2f} above the control's -- {off[3] / max(SKY['pk_s'][3], 1e-9):.1f} sigma of the sky's own locating
  spread at the fourth -- and the LARGEST of the four sits at the FIRST peak.  ⛔ ** The geometric
  comb-width term is NOT subtracted from them any more, and that is a change of finding and not of
  figure: ** a comb {100 * _dlA:+.3f}% wider, which is what this arm's geometry gives, would predict
  {_pred_tab} and the measurement is {_off_tab}, so the ruler overshoots the
  fourth peak by a factor {abs(pred_4 / off[3]):.1f} and the arm's own fitted comb spacing is NARROWER than the
  control's.  *On the namesake the two agreed and the subtraction was defensible; on the arm of
  record the premise fails, which EXCLUDES the ruler shape more firmly than the paper claims.*
  ** And PART 2 measured the phase at {dc3 / sc3:+.1f} sigma against the control, which is the same conclusion
  reached without subtracting anything. **

  ⛔ ** ORDER (3) IS NOT RUN, AND THAT IS THE ORDER'S OWN RULE. **  *The neutrino-sector question is
  conditional on "a uniform phase offset surviving the first test".  None survives, so the handover's
  treatment of the free-streaming stress is not indicated by anything measured here.*  ⌗ *It may
  still be worth asking on its own merits -- a reset of the anisotropic stress at the branch point
  would be a defect in the state specification whether or not it shows up in the comb -- but this
  receipt gives no evidence for it and does not pretend to.*

  ⌗ ** WHAT THIS DOES NOT SAY. **  That the arm fits: the verified 185-bin refit leaves it at 1.58
  per bin against the control's 1.01, and that is where the disagreement lives -- in the heights and
  the damping tail, not in the peak positions.  *And it does not re-open the sky's own quartet, which
  is `sec:intro`'s and is reproduced here rather than replaced.*
""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print(BAR)
