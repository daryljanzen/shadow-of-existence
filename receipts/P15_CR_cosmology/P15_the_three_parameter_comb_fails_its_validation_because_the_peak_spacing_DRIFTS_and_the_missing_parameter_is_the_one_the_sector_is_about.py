#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7213` ORDERED THE PARAMETRIC COMB -- POSITION, SPACING AND ALTERNATION AS FITTED
PARAMETERS -- AND ATTACHED A VALIDATION BURDEN: `show it recovers cc66.156's and cc66.158's own model
directions ... If it does not recover them, that is the result and the data half does not happen`.
*** IT DOES NOT RECOVER THEM.  THE DATA HALF DOES NOT HAPPEN.  AND THE REASON IS THAT THE PEAK
SPACING DRIFTS, WHICH IS A FOURTH DEGREE OF FREEDOM THE THREE PARAMETERS CANNOT CARRY. ***

  ⓵ ** THE TEMPLATE IS RIGHT AND THAT IS CHECKED RATHER THAN ASSUMED. **
  `$\\cos(2\\pi[u-a\\cos\\pi u])$` has its maxima at `$u=n+a(-1)^{n}$`, verified numerically on a
  `$10^{-5}$` grid at three values of `$a$`.  *So a comb with position, spacing and alternation is
  exactly what is being fitted, and a failure below is the model's and not the algebra's.*

  ⓶ ⛔ ** IT RECOVERS THREE SPECTRA OF SIX AND MISSES THREE, AND IN EACH DRIVING PAIR IT MISSES
  EXACTLY ONE MEMBER. **  *Both `NODRIVE` spectra come back inside `$0.11$` per cent, and so does
  the driving-ON `cr_rb0.5` at `$0.27$`.  `cr_base`, `lcdm_base` and `cr_rb1.5` come back
  `$18$`--`$19$` per cent HIGH.  **Since `$\\phi$` is referred to the FITTED `$\\ell_A$`, a pair
  whose two members disagree about the spacing by `$18$` per cent cannot be differenced at all** --
  so `cc66.158`'s directions are not reproduced badly, they are not constructible, and by `r7213`'s
  own terms that ends it.*

  ⛔⛭ ** AND THE FIRST VERSION OF THIS RECEIPT GOT THAT SPLIT WRONG, BECAUSE THE SEARCH WAS WRONG. **
  *It used a `$3\\times3$` grid of starts offset from the banked `$\\ell_A$` and reported that every
  driving-ON spectrum failed.  That grid returns a worse `$\\chi^{2}$` on five of the six spectra --
  by `$57$` per cent on the driving-off pair -- and on `cr_rb0.5` it lands `$65$` multipoles from the
  minimum.  **A start grid centred on the answer I expected could not tell me the answer was
  somewhere else.**  *The starts now span the whole feasible box and every optimum is checked to be
  interior to it; `fit_narrow` is kept in the file so the defect is visible beside its repair.**

  ⓷ ⛭⛭ ** THE REASON IS SPECIFIC: THE GAPS DRIFT. **  *A comb's gaps are
  `$\\ell_A(1\\mp2a)$` -- the high gaps equal each other and the low gaps equal each other.  On
  `cr_base` they are `$302/270/312/295$`: alternating, yes, **but the highs rise by `$10$` and the
  lows by `$25$`.**  Fitting the four gaps with spacing and alternation alone leaves an rms of
  `$9.5$` multipoles; adding one linear drift term cuts it to `$3.8$`, and on `cr_rb0.5` from
  `$8.5$` to `$0.5$`.  **Every spectrum tried wants the drift.***

  ⇒ ⛭⛭⛭ ** AND OMITTING IT BIASES THE ALTERNATION BY FORTY PER CENT, WHICH IS ONE OF THE TWO
  COMPONENTS THE WHOLE SEPARATION RESTS ON. **  *`cr_base`'s implied alternation goes
  `$0.0208\\to0.0295$` when the drift is admitted, and `cr_rb0.5`'s `$0.0090\\to0.0174$`.  **A
  three-parameter comb does not merely fit worse; it returns a wrong alternation.***

  ⌈ ** AND THE MISSING PARAMETER IS NOT ARBITRARY -- IT IS THE QUANTITY THIS SECTOR IS ABOUT. **  *A
  drift in spacing IS a linear phase drift at fixed `$\\ell_A$`, which is `cc66.153`'s own
  description of this residual (`$-96.6^{\\circ}$` at the correct spacing).  **So the instrument
  `r7213` specified is missing exactly the degree of freedom the sector has been chasing** -- and
  adding it is widening the order, which is `66`'s to do and not this seat's.*

  ⚠ ** ONE PITFALL REPORTED BECAUSE I WALKED INTO IT. **  *Given a generic basis -- each harmonic
  with its own polynomial envelope -- `$\\chi^{2}$` falls by nearly three orders of magnitude and
  `$\\ell_A$` runs to the edge of the search box at `$430.000$`.  The comb parameters become
  UNIDENTIFIED while the fit looks perfect.  **A good `$\\chi^{2}$` from a comb fit is not evidence
  the comb was found**, and the disciplined basis -- one envelope, scalar harmonic ratios -- is what
  makes the numbers above mean anything.*

** COMPUTES: the ordered three-parameter comb, profiled over a smooth baseline and one shared
   envelope with scalar harmonic ratios, a coarse multi-start over the whole feasible box
   refined at its best few, on six likelihood-binned model spectra; the template's maxima
   verified numerically; the gap pattern decomposed into
   spacing+alternation against spacing+alternation+drift; and the unidentifiability of the generic
   basis exhibited.  *** No new spectra, no refit, and the data is deliberately NOT touched. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~6 min)
"""
import os
import sys

import numpy as np
from scipy.optimize import minimize

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
# ⌗ COUNTED, NOT REMEMBERED.  The footer below said `6 of 6` while this file ran eight checks: a
#   hard-coded count is the same defect as a hard-coded start grid, one revision later.
ran = []


def check(label, ok):
    ran.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
for _p in (GO, LEV):
    if not os.path.isdir(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

LMIN, LMAX, NPK, HALFWIN = 150.0, 1600.0, 5, 40.0
NB, NE = 5, 3            # baseline degree, shared-envelope degree
LC, FACB = CS.bin_center_and_fac()
SPECTRA = (('cr_base', os.path.join(GO, 'cr_base.npz')),
           ('lcdm_base', os.path.join(GO, 'lcdm_base.npz')),
           ('cr_nodrive', os.path.join(LEV, 'cr_nodrive.npz')),
           ('lcdm_nodrive', os.path.join(LEV, 'lcdm_nodrive.npz')),
           ('cr_rb0.5', os.path.join(LEV, 'cr_rb0.5.npz')),
           ('cr_rb1.5', os.path.join(LEV, 'cr_rb1.5.npz')))
DRIVING_OFF = ('cr_nodrive', 'lcdm_nodrive')


def binned(path):
    z = np.load(path, allow_pickle=True)
    Cl = CS.bin_spectrum(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    k = np.isfinite(Cl)
    return LC[k], (Cl * FACB)[k], float(z['l_A'])


def detilt(ls, Dl):
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0) & np.isfinite(Dl)
    t = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    return ls[m], (Dl / ls ** t)[m]


def peak_gaps(ls, Dl):
    """cc66.156's located peaks, and the gaps between them."""
    ls, Y = detilt(ls, Dl)
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    Di = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(Di) - 2)
           if Di[i] > Di[i - 1] and Di[i] >= Di[i + 1] and Di[i] > Di[i - 2] and Di[i] >= Di[i + 2]]
    co = []
    for i in idx:
        if not co or lg[i] - co[-1] > 60.0:
            co.append(lg[i])
    pk = []
    for l0 in co[:NPK]:
        w = (ls >= l0 - HALFWIN) & (ls <= l0 + HALFWIN)
        if w.sum() < 4:
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        if c[0] < 0:
            pk.append(l0 - c[1] / (2 * c[0]))
    return np.diff(np.array(pk))


# ---- the ordered comb: position phi, spacing lA, alternation a, with the smooth parts profiled out
def design(ls, lA, phi, a, h2, h3, generic=False):
    x = np.log(ls / 500.0)
    u = ls / lA - phi
    up = u - a * np.cos(np.pi * u)
    cols = [x ** k for k in range(NB)]
    if generic:
        # ⚠ THE PITFALL BASIS: every harmonic its own envelope.  Shown, not used for the numbers.
        for h in (1, 2, 3):
            cols += [np.cos(2 * np.pi * h * up) * x ** k for k in range(NE)]
            cols += [np.sin(2 * np.pi * h * up) * x ** k for k in range(NE)]
    else:
        osc = (np.cos(2 * np.pi * up) + h2 * np.cos(4 * np.pi * up) + h3 * np.cos(6 * np.pi * up))
        cols += [osc * x ** k for k in range(NE)]
    return np.column_stack(cols)


def chi2(ls, Y, p, generic=False):
    if not (200.0 < p[0] < 430.0) or abs(p[1]) > 1.0 or abs(p[2]) > 0.3:
        return 1e12
    if not generic and (abs(p[3]) > 2.0 or abs(p[4]) > 2.0):
        return 1e12
    A = design(ls, p[0], p[1], p[2], p[3], p[4], generic)
    c, *_ = np.linalg.lstsq(A, Y, rcond=None)
    r = Y - A @ c
    return float(r @ r)


# ⛔⛔ THE SEARCH IS PART OF THE INSTRUMENT, AND MY FIRST VERSION OF IT WAS NOT ADEQUATE.  This receipt
#    first used a 3x3 grid of starts offset from the banked `l_A`, and every number in `PART B` was
#    wrong because of it -- not by round-off but by basins: on `cr_rb0.5` that grid returned
#    `351.961` where the minimum is at `286.841`.  **A start grid centred on the answer you expect
#    cannot tell you the answer is somewhere else.**  So the starts now span the WHOLE feasible box
#    in `l_A` and a full period in `$\phi$`, coarsely, and only the best few are refined -- which
#    makes `the optimum is interior to the box` a property this file CHECKS rather than hopes.
LBOX = (200.0, 430.0)                       # the box `chi2` enforces; the starts must span it
L0S = (210., 240., 265., 290., 315., 340., 370., 400., 425.)
P0S = (-0.45, -0.30, -0.15, 0.0, 0.15, 0.30)                       # a full period in phi
NREF = 5
LOOSE = dict(xatol=1e-3, fatol=1e-4, maxiter=4000, maxfev=4000)
TIGHT = dict(xatol=1e-8, fatol=1e-12, maxiter=60000, maxfev=60000)

# ⛔ AND THE TIE-BREAK IS NOT A TOLERANCE AND MUST NOT BE DECIDED AT THE LAST BIT.  Caught by the
#    tolerance perturbation, not by me: where several starts converge to the SAME minimum to
#    `1e-13`, a bare `r.fun < best.fun` picks the winner on round-off and its truth value flips
#    between linear-algebra builds.  Requiring a MATERIAL improvement makes order the tie-break --
#    deterministic on any build.  *The choice is immaterial to every number here: the contending
#    optima differ by `2e-7` in `$\ell_A$`.*
KEEP = 1e-9


def better(old, new):
    return new if (old is None or new.fun < old.fun - KEEP * max(1.0, abs(old.fun))) else old


def fit(ls, Y, lA0, generic=False):
    """coarse over the whole box, then refine the best NREF.  Returns (result, winning l_A start)."""
    f = (lambda p: chi2(ls, Y, p, generic))
    coarse = []
    for l0 in L0S:
        for p0 in P0S:
            r = minimize(f, [l0, p0, 0.015, 0.3, 0.1], method='Nelder-Mead', options=LOOSE)
            coarse.append((float(r.fun), l0, r.x.copy()))
    coarse.sort(key=lambda t: t[0])
    best, bl0 = None, None
    for _fun, l0, x in coarse[:NREF]:
        r = minimize(f, x, method='Nelder-Mead', options=TIGHT)
        if better(best, r) is r:
            best, bl0 = r, l0
    return best, bl0


def fit_narrow(ls, Y, lA0, generic=False):
    """EXACTLY the inadequate search this receipt first used, kept so the file carries its own
       correction: a reader sees that the narrow grid, and not the model, produced the dichotomy
       the first version of `PART B` reported."""
    f = (lambda p: chi2(ls, Y, p, generic))
    best = None
    for dl in (-8.0, 0.0, 8.0):
        for dp in (-0.1, 0.0, 0.1):
            best = better(best, minimize(f, [lA0 + dl, -0.2 + dp, 0.015, 0.3, 0.1],
                                         method='Nelder-Mead', options=TIGHT))
    return best


# ============================================================ A. the template
head("A.  ⓵ THE TEMPLATE PUTS ITS MAXIMA WHERE THE COMB WANTS THEM -- CHECKED, NOT ASSUMED")

_okT = True
for _a in (0.0, 0.02, -0.04):
    _u = np.arange(0.5, 5.0, 1e-5)
    _T = np.cos(2 * np.pi * (_u - _a * np.cos(np.pi * _u)))
    _i = [k for k in range(1, len(_u) - 1) if _T[k] > _T[k - 1] and _T[k] >= _T[k + 1]]
    _pk = np.array([_u[k] for k in _i])[:4]
    _pr = np.array([n + _a * (-1) ** n for n in range(1, 5)])
    _w = float(np.max(np.abs(_pk - _pr)))
    # ⌗ at a = 0 the relation is EXACT and the residual is float/grid noise, so there is no a^2
    #   to scale against; that case gets its own bound rather than a fabricated one.
    if _a == 0.0:
        print(f"      a = {_a:+.3f}:  maxima {np.round(_pk, 4)}  wanted {np.round(_pr, 4)}  "
              f"worst {_w:.1e}  (exact; this is float noise)")
        _okT = _okT and _w < 1e-9
    else:
        print(f"      a = {_a:+.3f}:  maxima {np.round(_pk, 4)}  wanted {np.round(_pr, 4)}  "
              f"worst {_w:.1e}  (= {_w / (_a * _a):.2f} a^2)")
        _okT = _okT and _w < 0.25 * _a * _a
check("Ⓐ①  the template's maxima sit at `$n+a(-1)^{n}$` ** TO SECOND ORDER IN `$a$` AND NOT "
      "EXACTLY **, the deviation being under a quarter of `$a^{2}$` at every `$a$` tried -- "
      "`$4\\times10^{-5}$` at `$a=0.02$` and `$3.1\\times10^{-4}$` at `$a=-0.04$`.  ⚠ *I first wrote "
      "this check as `better than 2e-4` and it FAILED at `$a=-0.04$`: the displacement "
      "`$a\\cos\\pi u$` is evaluated at the SHIFTED maximum, so the relation carries an "
      "`$O(a^{2})$` term I had treated as exact.*  ⇒ *It is negligible against the signals -- "
      "`$3\\times10^{-4}$` in `$u$` against a driving offset of `$0.126$` -- but the fitted `$a$` is "
      "the comb\'s alternation only to that order, and saying so is the difference between a "
      "measured bound and an assumed identity*", _okT)


# ============================================================ B. the fit
head("B.  ⓶ ⛔ THE ORDERED COMB RECOVERS THREE SPECTRA OF SIX AND MISSES THREE -- AND THE SPLIT IS "
     "NOT THE ONE I FIRST REPORTED")

print(f"      {'spectrum':13s} {'l_A fit':>9s} {'banked':>9s} {'error %':>8s} {'phi':>9s} "
      f"{'a':>9s} {'chi2':>10s} | {'3x3 l_A':>9s} {'3x3 chi2':>10s} {'3x3 worse':>9s}")
FIT, NAR, INSIDE = {}, {}, {}
for tag, p in SPECTRA:
    lb, db, lA = binned(p)
    ls, Y = detilt(lb, db)
    r, _l0 = fit(ls, Y, lA)
    n = fit_narrow(ls, Y, lA)
    FIT[tag] = (r.x[0], r.x[1], r.x[2], r.fun, lA)
    NAR[tag] = (n.x[0], n.fun)
    INSIDE[tag] = bool(LBOX[0] + 1.0 < r.x[0] < LBOX[1] - 1.0)
    print(f"      {tag:13s} {r.x[0]:9.3f} {lA:9.3f} {100 * (r.x[0] / lA - 1):+8.2f} {r.x[1]:+9.5f} "
          f"{r.x[2]:+9.5f} {r.fun:10.4g} | {n.x[0]:9.3f} {n.fun:10.4g} "
          f"{100 * (n.fun / r.fun - 1):8.1f}%")
ERR = {t: abs(FIT[t][0] / FIT[t][4] - 1) for t, _ in SPECTRA}
REC = [t for t, _ in SPECTRA if ERR[t] < 0.01]
MISS = [t for t, _ in SPECTRA if ERR[t] > 0.15]
_nworse = sum(1 for t, _ in SPECTRA if NAR[t][1] > FIT[t][3] * 1.01)

print(f"      ⇒ the 3x3 grid this receipt first used is worse on {_nworse} of 6, by up to "
      f"{100 * max(NAR[t][1] / FIT[t][3] - 1 for t, _ in SPECTRA):.0f} per cent, and on `cr_rb0.5` "
      f"it lands {abs(NAR['cr_rb0.5'][0] - FIT['cr_rb0.5'][0]):.0f} multipoles away")
check("Ⓑ①  ⛔⛭ ** THE DICHOTOMY THE FIRST VERSION OF THIS RECEIPT REPORTED WAS THE SEARCH AND NOT "
      "THE MODEL. **  *A `$3\\times3$` grid of starts offset from the banked `$\\ell_A$` returns a "
      "worse `$\\chi^{2}$` on five of the six spectra -- by `$57$` per cent on the driving-off pair "
      "-- and on `cr_rb0.5` it reports `$351.961$` where the minimum is `$286.841$`.*  ⇒ *The box "
      "is spanned now and every optimum below is INTERIOR to it, so `the search was adequate` is "
      "measured here rather than assumed. **This is the defect, and it is mine: a start grid "
      "centred on the answer I expected could not tell me the answer was elsewhere.**",
      _nworse >= 5 and all(INSIDE.values()))

print(f"      ⇒ recovered to under 1%: {', '.join(REC)}")
print(f"      ⇒ missed by over 15%:    {', '.join(MISS)}")
check("Ⓑ②  ** THE COMB RECOVERS `$\\ell_A$` ON THREE SPECTRA OF SIX -- BOTH DRIVING-OFF ONES AND THE "
      "DRIVING-ON `cr_rb0.5` -- AND MISSES THE OTHER THREE BY `$18$`--`$20$` PER CENT. **  *So the "
      "instrument is not blind to a spectrum merely because it carries a driving: it recovers "
      "`cr_rb0.5` to `$0.27$` per cent at a `$\\chi^{2}$` the inadequate search missed by a quarter.*  "
      "⇒ *What separates the three it fails is PART C's drift and not the driving, which is where "
      "this receipt's diagnosis was right and its bound was wrong*",
      set(REC) == {'cr_nodrive', 'lcdm_nodrive', 'cr_rb0.5'} and len(MISS) == 3)

for _b, _o in (('cr_base', 'cr_nodrive'), ('lcdm_base', 'lcdm_nodrive')):
    print(f"      ⇒ the {_b.split('_')[0]} driving pair: {_b} off by {100 * ERR[_b]:+.1f}% and {_o} by "
          f"{100 * ERR[_o]:+.2f}% -- a difference between them is not a driving difference")
check("Ⓑ③  ⛔ ** AND `r7213`'s VALIDATION BURDEN IS STILL NOT MET, FOR A SHARPER REASON THAN I FIRST "
      "GAVE. **  *In EACH driving pair the comb misses one member's spacing by `$18$` per cent and "
      "recovers the other's to `$0.1$`, and `$\\phi$` is defined against the fitted `$\\ell_A$`.  "
      "**So the two members' phases are not referred to the same comb and no driving difference can "
      "be formed at all** -- `cc66.158`'s `$0.1929$`/`$1.0390$` separation is not merely "
      "reproduced badly, it is not constructible from this instrument.*  ⇒ *`r7213` made that "
      "recovery the condition for going on to the data, so the data is not touched here*",
      all(ERR[_b] > 0.15 and ERR[_o] < 0.01
          for _b, _o in (('cr_base', 'cr_nodrive'), ('lcdm_base', 'lcdm_nodrive'))))


# ============================================================ C. why: the gaps drift
head("C.  ⓷ ⛭⛭ WHY -- A COMB'S HIGH GAPS REPEAT AND THESE RISE, SO ONE DRIFT TERM IS MISSING")

print("      a comb gives gaps l_A(1 -+ 2a): the highs equal each other, the lows equal each other")
print(f"      {'spectrum':13s} {'gaps':24s} {'highs rise':>11s} {'lows rise':>10s} "
      f"{'rms comb':>9s} {'rms +drift':>11s} {'a comb':>8s} {'a +drift':>9s}")
GAP = {}
for tag, p in SPECTRA:
    lb, db, _lA = binned(p)
    g = peak_gaps(lb, db)
    n = np.arange(len(g))
    A2 = np.column_stack([np.ones(len(g)), (-1.0) ** n])
    A3 = np.column_stack([np.ones(len(g)), (-1.0) ** n, n])
    c2, *_ = np.linalg.lstsq(A2, g, rcond=None)
    c3, *_ = np.linalg.lstsq(A3, g, rcond=None)
    r2 = float(np.sqrt(((g - A2 @ c2) ** 2).mean()))
    r3 = float(np.sqrt(((g - A3 @ c3) ** 2).mean()))
    a2, a3 = abs(c2[1]) / c2[0] / 2, abs(c3[1]) / c3[0] / 2
    GAP[tag] = (r2, r3, a2, a3)
    print(f"      {tag:13s} {str([int(x) for x in g]):24s} {g[0::2][-1] - g[0::2][0]:+11.0f} "
          f"{g[1::2][-1] - g[1::2][0]:+10.0f} {r2:9.2f} {r3:11.2f} {a2:8.4f} {a3:9.4f}")
check("Ⓒ①  ** ON EVERY SPECTRUM THE HIGH GAPS AND THE LOW GAPS BOTH RISE rather than repeating, and "
      "one linear drift term cuts the gap-fit residual on every one of them. **  *That is a FOURTH "
      "degree of freedom in the peak pattern, and the ordered instrument has three*",
      all(GAP[t][1] < GAP[t][0] for t, _ in SPECTRA))
_bias = [abs(GAP[t][3] / GAP[t][2] - 1) for t, _ in SPECTRA if t not in DRIVING_OFF]
print(f"      ⇒ admitting the drift changes the implied alternation by "
      f"{100 * min(_bias):.0f}--{100 * max(_bias):.0f} per cent on the driving-on spectra")
check("Ⓒ②  ⛭⛭⛭ ** AND OMITTING THE DRIFT DOES NOT MERELY FIT WORSE -- IT RETURNS A WRONG "
      "ALTERNATION, by tens of per cent, on every driving-on spectrum. **  *The alternation is one "
      "of the two components `cc66.158`'s whole separation rests on, so a three-parameter comb "
      "would have carried a biased value into the one number the sector is using*",
      min(_bias) > 0.25)


# ============================================================ D. the pitfall
head("D.  ⚠ THE PITFALL: A GENERIC BASIS MAKES THE COMB UNIDENTIFIED WHILE LOOKING PERFECT")

_lb, _db, _lA = binned(os.path.join(GO, 'cr_base.npz'))
_ls, _Y = detilt(_lb, _db)
_rg, _ = fit(_ls, _Y, _lA, generic=True)
_d_chi, _d_lA = FIT['cr_base'][3], abs(FIT['cr_base'][0] / _lA - 1)
_g_lA = abs(_rg.x[0] / _lA - 1)
print(f"      cr_base, each harmonic given its own polynomial envelope (18 oscillatory columns):")
print(f"         disciplined basis: l_A {FIT['cr_base'][0]:7.3f} ({100 * _d_lA:+.1f}%), "
      f"chi2 {_d_chi:10.4g}")
print(f"         generic basis:     l_A {_rg.x[0]:7.3f} ({100 * _g_lA:+.1f}%), chi2 {_rg.fun:10.4g}"
      f"{'   -- AT THE BOX EDGE' if _rg.x[0] > LBOX[1] - 1.0 else ''}")
print(f"         ⇒ chi2 improves {_d_chi / _rg.fun:.0f}x while the answer gets "
      f"{'WORSE' if _g_lA > _d_lA else 'better'} by {100 * (_g_lA - _d_lA):+.1f} points")
check("Ⓓ①  ** THE GENERIC BASIS IMPROVES `$\\chi^{2}$` BY NEARLY THREE ORDERS OF MAGNITUDE AND RUNS "
      "`$\\ell_A$` TO THE EDGE OF THE SEARCH BOX. **  *So a good `$\\chi^{2}$` from a comb fit is not "
      "evidence the comb was found: the extra oscillatory freedom absorbs the spectrum rather than "
      "locating its comb, and every number in `PART B` depends on the basis being disciplined "
      "instead.*  ⚠ *I have now had this check wrong in BOTH directions, from one cause.  I first "
      "wrote `runs to the boundary with chi2 essentially exact`, then walked it back to a measured "
      "`$122\\times$` because that is what the file returned.  **Both readings came from the "
      "inadequate search: with the box spanned, the boundary behaviour I first described is what "
      "the receipt's own basis does.**  The lesson is not that I over-claimed and then "
      "under-claimed -- it is that neither number meant anything while the search was wrong*",
      _rg.fun < _d_chi / 50.0 and _g_lA > _d_lA and _rg.x[0] > LBOX[1] - 1.0)


# ============================================================ E. what follows
head("E.  WHAT FOLLOWS, AND WHAT IS NOT DONE")

print("  ⛔ THE DATA HALF DOES NOT HAPPEN.  `r7213` set recovering the model directions as the")
print("     condition and it is not met.  No observed point is placed and no carrier is named.")
print("  ⌈ THE MISSING PARAMETER IS NOT ARBITRARY.  A drift in the spacing IS a linear phase drift")
print("     at fixed l_A, which is cc66.153's own description of this residual -- the -96.6 degrees")
print("     at the correct spacing.  So the three-parameter instrument is missing precisely the")
print("     degree of freedom this sector has been chasing since r7181.")
print("  ⛔ AND ADDING IT IS WIDENING THE ORDER, WHICH IS NOT THIS SEAT'S TO DO.  r7213 ordered")
print("     three parameters and said not to reduce the count without saying so; it did not")
print("     authorise a fourth.  Naming it and stopping is the same discipline held at r7203 and")
print("     r7211, and both times 66 sustained it.")
print("  ✔ AND NOTHING IS WITHDRAWN.  cc66.157 and cc66.158 use located peaks with l_A FIXED at its")
print("     banked value, so the drift never enters their difference statistics as a free")
print("     parameter -- it is common to both sides of every difference they take.")
_rc = max(GAP[t][0] for t in REC)
_mc = min(GAP[t][0] for t in MISS)
print(f"  ⛭ AND WHAT SEPARATES THEM IS PART C's DRIFT, NOT THE DRIVING.  The three spectra the comb")
print(f"     recovers are the three with the SMALLEST driftless gap residual "
      f"({', '.join(f'{GAP[t][0]:.2f}' for t in REC)}) and the three it misses are the three")
print(f"     largest ({', '.join(f'{GAP[t][0]:.2f}' for t in MISS)}) -- a perfect ordering, at "
      f"{_rc:.2f} against {_mc:.2f}.")
print(f"  ⚠ AND THAT IS AN ORDERING ON SIX SPECTRA AND NOT A THRESHOLD.  A 3/3 split falling in")
print(f"     perfect order arises by luck once in twenty times, and the margin is {_mc - _rc:.2f} of")
_spread = max(GAP[t][0] for t, _ in SPECTRA) - min(GAP[t][0] for t, _ in SPECTRA)
print(f"     a multipole against a spread of {_spread:.2f}.")
print("     So it is consistent with the diagnosis and it does not establish where the boundary is.")
check("Ⓔ①  ⛭ ** THE INADEQUACY IS NOT SPECIFIC TO SPECTRA CARRYING A DRIVING -- IT TRACKS THE DRIFT. "
      "**  *Every spectrum the comb recovers has a smaller driftless gap residual than every "
      "spectrum it misses.  **I first bounded this finding by the driving, and that bound was an "
      "artefact of the narrow search: `cr_rb0.5` carries a driving and is recovered to `$0.27$` "
      "per cent.**  What the comb cannot do is fit a spectrum whose gaps drift too far for three "
      "parameters, which is PART C's diagnosis and not a second one.*  ⇒ *Stated as the ordering it "
      "is: six spectra, a `$3/3$` split, a margin under one multipole -- so it says a "
      "four-parameter comb should first be tested where the drift is largest, and it does not say "
      "where the boundary lies*",
      _rc < _mc)

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print(f"  ✔ {len(ran) - len(fail)} of {len(ran)} checks pass -- and what they establish is that the "
      "ORDERED instrument fails its")
print("    own validation, for a named reason, with the missing parameter identified.")
print(BAR)
sys.exit(0)
