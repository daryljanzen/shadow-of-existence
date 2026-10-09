#!/usr/bin/env python3
r"""
RECEIPT -- P15: ** `r7221` ORDERED THE DIFFERENCING ALONG THE TIGHT DIRECTION -- `measure whether
the carrier separates along the direction the bank actually carries` -- WITH THE BURDEN `state the
expected Delta L_p BEFORE you read the fits`.  *** THE CARRIERS SEPARATE BY `218` SIGMA, MY
PRE-REGISTERED NUMBER IS WRONG BY SIX TIMES THE BOUND I WROTE, AND WHAT THE `218` SIGMA
MEASURES IS THE COMB'S OWN PEAK COUNT RATHER THAN THE CARRIER. *** **

  ⓵ ** ITEM ① HAS A YES AND IT DOES NOT MEAN WHAT IT WAS MEANT TO MEAN. **  `$\Delta L_p$` across
  the driving pair is `$56.693$` against `$\sigma=0.129$`/`$0.226$` -- **`$218\sigma$`** on the
  bank's own convention, `$93\sigma$` on the scale-invariant one.  *I pre-registered
  `$|\Delta L_p|\le10$` from the gap terms, which sum to `$5.05$`; it is `$56.693$` -- **`$5.7$`
  times the bound and `$11.2$` times the terms.  Reported against the measurement, as ordered.***

  ⓶ ⛔ ** AND THE REASON IT IS `$56.7$` IS THAT `$L_p$` IS THE FITTED CURVE'S OWN PEAK SPACING ONLY
  WHERE THE FIT LOCKS ONTO THE PEAK TRAIN. **  *Pointing PART C's locator at the FITTED CURVE:
  `$L_p$` equals that curve's mean gap to `$0.16$` per cent on the two driving-OFF spectra and
  misses it by `$21$`--`$27$` per cent on the other four.  **So the `$218\sigma$` is the difference
  between a fit that locks and a fit that does not.***

  ⓷ ⛔ ** THE LOADING PAIR CANNOT BE DIFFERENCED AT ALL. **  *`cr_rb1.5` has no interior optimum in
  any box: `$430.000$` at the `$430$` box, `$900.000$` at the `$900$` box, `$\chi^{2}$` falling
  `$1.94\times10^{4}\to1.39\times10^{3}$` as the box is widened.  `cc66.160`'s unbounded direction,
  recurring where the order needed it not to.*

  ⓸ ⛔ ** AND THE SIGMA THE ORDER ASKS ME TO MEASURE AGAINST IS NOT AN ERROR ON `$L_p$`. **  *Moving
  the window's top edge from `$1000$` to `$1950$` moves `cr_nodrive`'s `$L_p$` by `$14.3$` --
  `$283.2$`, `$281.6$`, `$293.4$`, `$295.6$`, `$296.0$` -- while the formal `$\sigma$` over those
  windows is `$0.01$`--`$4.28$`.  **The bank does not carry `$L_p$` to `$0.08$` per cent; it
  carries a formal error of `$0.08$` per cent on a number that moves by five per cent when the
  window moves.***
  ⌗ *The same sigma is amplitude-dependent, and on the scale-free one `cc66.162`'s `$35\sigma$` and
  `$379\sigma$` read `$54$` and `$82$` -- so its conclusion and its ordering stand and `more than
  three hundred` does not.  Flagged here because `sec:refit-bound` quotes it.*

  ⓹ ** ITEM ② RUN ANYWAY, AND THE SKY LANDS ON THE UNLOCKED VALUE. **  *`$L_p$`(sky) `$=351.807$`
  by the identical extraction -- within `$1.68$` and `$1.97$` of the two driving-ON bases and
  `$58.4$` from the driving-OFF pair, **which reads naively as the sky preferring the driving.**
  It is void: the curve that extraction returns is rejected by `plik_lite` at `$\chi^{2}/{\rm
  dof}=11.8$` on its own covariance, and its `$L_p$` misses its own curve's peak spacing by
  `$62$` -- the unlocked signature exactly.*  ⇒ **And the matched differencing is blind to the arm:
  `$(\rm arm-sky)-(\rm control-sky)=0.295$`, `$1.6\sigma$`, against the carrier's `$218$`.**

  ⓺ ⛭⛭⛭ ** THE CLOSURE HAS NO NUMBER, BECAUSE THE DEGENERACY IS INVARIANT TO EVERYTHING THE BANK
  CAN VARY. **  *`r7221` names the remainder as `what point count, window and per-point error would
  bring 0.1929 against 1.0390 within reach`.  Measured: `$|\rho(\ell_A,d)|$` stays in
  `$[0.939,0.977]$` over THIRTEEN fits -- `$78$`--`$176$` points, five windows, six spectra -- and
  **halving the point count leaves it at `$-0.9549$` against `$-0.9548$`.**  ⇒ *So `r7219`'s
  `what would change it is a finer binning` is measurably wrong, and there is no point count,
  window or per-point error in this bank that changes it.*

  ⌈ ⛭⛭ ** WHAT THE POINTS DO BUY IS THE LOCATOR, WHICH IS THE INSTRUMENT THE ROW WROTE OFF. **
  *Merged in pairs -- `$18$` per bin, `$78$` points -- PART C's locator reads the sky's first four
  peaks within `$3.37$` of its own read of the MODEL through the identical merge, against a
  `$547$` displacement at the native `$9$`.  **`r7221` says `the peak locator of cc66.159 could
  not` be pointed at the sky; at half the bank's resolution it can, and the comb is the half no
  sampling fixes.**  ⚠ *Four peaks and not five, and forming `$(\varphi,{\rm alt})$` on four is a
  new measurement with its own burden -- named as a route, NOT made here.*

** COMPUTES: `cc66.162`'s centred four-parameter comb, unchanged and pinned to its published
   digits; its `$L_p$` differenced within `cc66.158`'s driving and loading pairs; PART C's locator
   pointed at the FITTED curves; the same extraction run on `plik_lite` TT and scored against its
   own covariance; the degeneracy measured against point count, window and spectrum; and the
   sky re-binned in pairs through the identical merge as the model. **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; 223s MEASURED)
"""
import os
import sys

import numpy as np
from scipy.optimize import minimize

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
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
NB, NE = 5, 3
NPAR = NB + NE + 6
LC, FACB = CS.bin_center_and_fac()
SPECTRA = (('cr_base', os.path.join(GO, 'cr_base.npz')),
           ('lcdm_base', os.path.join(GO, 'lcdm_base.npz')),
           ('cr_nodrive', os.path.join(LEV, 'cr_nodrive.npz')),
           ('lcdm_nodrive', os.path.join(LEV, 'lcdm_nodrive.npz')),
           ('cr_rb0.5', os.path.join(LEV, 'cr_rb0.5.npz')),
           ('cr_rb1.5', os.path.join(LEV, 'cr_rb1.5.npz')))
# ⛭ cc66.158's two pairs, in cc66.158's own membership: the driving pair differs in the driving and
#   in NOTHING else (its banked l_A is bit-identical across the switch), and the loading pair is
#   the RBFAC lever.  `each spectrum's L_p read at its OWN decorrelating pivot, differenced within
#   the pair` -- r7221 ①.
DRIVING_PAIR = ('cr_base', 'cr_nodrive')
CONTROL_PAIR = ('lcdm_base', 'lcdm_nodrive')
LOADING_PAIR = ('cr_rb0.5', 'cr_rb1.5')

# ⛔ cc66.162's PUBLISHED DIGITS, hard-coded so that the machinery re-used here is PINNED and not
#   merely believed.  The one change this file makes to `fit()` is that the four tight refits are
#   computed ONCE instead of twice (cc66.162 ran them a second time to count how many reached the
#   optimum); Nelder-Mead from a fixed start is deterministic, so the values cannot move -- and
#   Ⓐ① is what says so rather than this comment.
PUB = {'cr_base': (350.131, -0.9385, 0.129), 'lcdm_base': (349.835, -0.9385, 0.139),
       'cr_nodrive': (293.438, -0.9548, 0.226), 'lcdm_nodrive': (293.476, -0.9548, 0.242),
       'cr_rb0.5': (347.672, -0.9773, 0.214)}

LBOX = (200.0, 430.0)
WBOX = (200.0, 900.0)
L0S = (215., 265., 300., 345., 400.)
W0S = (215., 300., 400., 520., 650., 800.)
P0S = (-0.45, -0.20, 0.05, 0.30)
D0S = (0.0, 8.0, -16.0)
NREF = 4
LOOSE = dict(xatol=1e-3, fatol=1e-4, maxiter=4000, maxfev=4000)
TIGHT = dict(xatol=1e-8, fatol=1e-12, maxiter=60000, maxfev=60000)
KEEP = 1e-9


def binned(path):
    z = np.load(path, allow_pickle=True)
    Cl = CS.bin_spectrum(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    k = np.isfinite(Cl)
    return LC[k], (Cl * FACB)[k], float(z['l_A'])


def detilt(ls, Dl, lo=LMIN, hi=LMAX):
    m = (ls >= lo) & (ls <= hi) & (Dl > 0) & np.isfinite(Dl)
    t = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    return ls[m], Dl[m] / ls[m] ** t


def phase(ls, lA, d):
    """v(l) from l = l_A v + d v^2.  The d -> 0 branch is l/l_A EXACTLY, not a limit."""
    if abs(d) < 1e-12:
        return ls / lA
    disc = lA * lA + 4.0 * d * ls
    if np.any(disc <= 0):
        return None
    return (-lA + np.sqrt(disc)) / (2.0 * d)


def design(ls, lA, phi, a, h2, h3, d):
    v = phase(ls, lA, d)
    if v is None:
        return None
    u = v - phi
    up = u - a * np.cos(np.pi * u)
    x = np.log(ls / 500.0)
    osc = np.cos(2*np.pi*up) + h2*np.cos(4*np.pi*up) + h3*np.cos(6*np.pi*up)
    return np.column_stack([x ** k for k in range(NB)] + [osc * x**k for k in range(NE)])


def chi2(ls, Y, p, box=LBOX):
    lA, phi, a, h2, h3, d = p
    if not (box[0] < lA < box[1]) or abs(phi) > 1.0 or abs(a) > 0.3:
        return 1e12
    if abs(h2) > 2.0 or abs(h3) > 2.0 or abs(d) > 120.0:
        return 1e12
    A = design(ls, lA, phi, a, h2, h3, d)
    if A is None or not np.all(np.isfinite(A)):
        return 1e12
    c, *_ = np.linalg.lstsq(A, Y, rcond=None)
    r = Y - A @ c
    return float(r @ r)


def fit(ls, Y, box=LBOX, l0s=L0S):
    """cc66.161/162's two-stage box-spanning search.  Returns (result, starts that reached it)."""
    f = (lambda p: chi2(ls, Y, p, box))
    coarse = []
    for l0 in l0s:
        for p0 in P0S:
            for d0 in D0S:
                r = minimize(f, [l0, p0, 0.015, 0.3, 0.1, d0], method='Nelder-Mead',
                             options=LOOSE)
                coarse.append((float(r.fun), r.x.copy()))
    coarse.sort(key=lambda t: t[0])
    ref = [minimize(f, x, method='Nelder-Mead', options=TIGHT) for _fun, x in coarse[:NREF]]
    best = None
    for r in ref:
        if best is None or r.fun < best.fun - KEEP * max(1.0, abs(best.fun)):
            best = r
    reached = sum(1 for r in ref if r.fun < best.fun * (1 + 1e-6) + 1e-9)
    return best, reached


# ⛔ PART C's LOCATOR, SPLIT IN TWO SO IT CAN BE POINTED AT A FITTED CURVE AS WELL AS AT DATA.
#    `peak_gaps` below is cc66.160's function with its body replaced by the two calls it was
#    already making; Ⓐ② checks the split is a no-op on all seven inputs rather than asserting it.
def locate(ls, Y):
    """cc66.156's located peaks, on an ALREADY de-tilted curve."""
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
    return np.array(pk)


def peak_gaps(ls, Dl):
    return np.diff(locate(*detilt(ls, Dl)))


def peak_gaps_161(ls, Dl):
    """cc66.160's function BYTE FOR BYTE, kept only so that Ⓐ② can compare against it."""
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


def cov2(ls, Y, x0, i, j, hi, hj, box=LBOX):
    """the 2x2 covariance of (p_i, p_j) from the curvature of chi2 at the optimum"""
    def c(hii, hjj):
        q = x0.copy(); q[i] += hii; q[j] += hjj
        return chi2(ls, Y, q, box)
    f0 = chi2(ls, Y, x0, box)
    Hii = (c(hi, 0) - 2 * f0 + c(-hi, 0)) / hi ** 2
    Hjj = (c(0, hj) - 2 * f0 + c(0, -hj)) / hj ** 2
    Hij = (c(hi, hj) - c(hi, -hj) - c(-hi, hj) + c(-hi, -hj)) / (4 * hi * hj)
    return np.linalg.inv(np.array([[Hii, Hij], [Hij, Hjj]]) / 2.0)


def centred(ls, Y, b, box=LBOX):
    """cc66.162's shear: (L_p, sigma_Lp, rho before, v_p*, interior?)"""
    x0 = b.x.copy()
    C = cov2(ls, Y, x0, 0, 5, 0.5, 0.05, box)
    vps = -C[0, 1] / (2.0 * C[1, 1])
    J = np.array([[1.0, 2.0 * vps], [0.0, 1.0]])
    Cp = J @ C @ J.T
    v = phase(ls, x0[0], x0[5])
    return (x0[0] + 2.0 * vps * x0[5], float(np.sqrt(abs(Cp[0, 0]))),
            float(C[0, 1] / np.sqrt(abs(C[0, 0] * C[1, 1]))), float(vps),
            bool(v.min() <= vps <= v.max()))


# ============================================================ A. the reproduction
head("A.  THE MACHINERY IS cc66.162's, PINNED TO ITS PUBLISHED DIGITS BEFORE ANYTHING NEW IS ASKED")

_z = np.load(os.path.join(GO, 'cr_base.npz'), allow_pickle=True)
MASK = np.isfinite(CS.bin_spectrum(np.asarray(_z['ls'], float), np.asarray(_z['Dl'], float)))
# ⌗ the SKY, through the identical extraction: the same bins the models cover, D_l from the
#   likelihood's own binned C_l, and nothing else different.  r7221 ②'s `identical extraction`.
SKY = (LC[MASK], (CS.X_DATA * FACB)[MASK], float('nan'))

FITS, LP, SIG, RHO, VPS, INSIDE, EDGE, NPT = ({} for _ in range(8))
print(f"      {'spectrum':13s} {'lA(v=0)':>9s} {'d':>8s} {'v_p*':>6s} {'L_p':>9s} {'sigma':>8s} "
      f"{'rho(lA,d)':>10s} {'chi2':>10s} {'cc66.162 L_p':>13s}")
for tag, p in SPECTRA + (('sky', None),):
    lb, db, lA = SKY if p is None else binned(p)
    ls, Y = detilt(lb, db)
    b, _r = fit(ls, Y)
    lp, sg, rho, vps, ins = centred(ls, Y, b)
    FITS[tag] = (b.x.copy(), float(b.fun), lA, ls, Y)
    LP[tag], SIG[tag], RHO[tag], VPS[tag], INSIDE[tag] = lp, sg, rho, vps, ins
    EDGE[tag] = bool(b.x[0] > LBOX[1] - 1.0 or b.x[0] < LBOX[0] + 1.0)
    NPT[tag] = int(len(ls))
    print(f"      {tag:13s} {b.x[0]:9.3f} {b.x[5]:+8.3f} {vps:6.2f} {lp:9.3f} {sg:8.4f} "
          f"{rho:+10.4f} {b.fun:10.4g} "
          f"{(f'{PUB[tag][0]:13.3f}' if tag in PUB else ' not published')}")
check("Ⓐ①  ** THE FIVE SPECTRA cc66.162 PUBLISHED COME BACK TO ITS PRINTED DIGITS -- `$L_p$` TO "
      "THREE DECIMALS, `$\\rho$` TO FOUR, `$\\sigma$` TO THREE. **  *The one change here is that "
      "`fit()` computes its four tight refits ONCE instead of twice; Nelder-Mead from a fixed "
      "start is deterministic, so nothing can move -- and this is what says so.  **A re-used "
      "instrument that is not pinned is a new instrument wearing the old one's results***",
      all(abs(LP[t] - PUB[t][0]) < 5e-4 and abs(RHO[t] - PUB[t][1]) < 5e-5
          and abs(SIG[t] - PUB[t][2]) < 5e-4 for t in PUB))

_same = []
for tag, p in SPECTRA + (('sky', None),):
    lb, db, _ = SKY if p is None else binned(p)
    g1, g2 = peak_gaps(lb, db), peak_gaps_161(lb, db)
    _same.append(len(g1) == len(g2) and bool(np.all(g1 == g2)))
print(f"      the locator split is a no-op on all {len(_same)} inputs: {all(_same)}")
check("Ⓐ②  ** AND SPLITTING PART C's LOCATOR SO IT CAN BE POINTED AT A FITTED CURVE IS A NO-OP ON "
      "ALL SEVEN INPUTS, CHECKED AGAINST `cc66.160`'s BYTE-FOR-BYTE COPY. **  *`cc66.161` learned "
      "this the hard way: a locator retyped from memory differed in four places and would have "
      "compared the fit against my own variant while the text claimed it was PART C's*",
      all(_same))

print()
print(f"      PART C's gap model `gap_n = c0 + c1(-1)^n + c2 n`, which is what the "
      f"pre-registration was built on:")
print(f"      {'spectrum':13s} {'c0':>9s} {'c1':>7s} {'c2':>7s} {'banked lA':>10s}")
C0, C2 = {}, {}
for tag, p in SPECTRA:
    lb, db, lA = binned(p)
    gaps = peak_gaps(lb, db)
    n = np.arange(len(gaps))
    c3, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(gaps)), (-1.0) ** n, n]), gaps,
                             rcond=None)
    C0[tag], C2[tag] = float(c3[0]), float(c3[2])
    print(f"      {tag:13s} {c3[0]:9.2f} {c3[1]:+7.2f} {c3[2]:+7.2f} {lA:10.3f}")
_dc0_drv = C0['cr_base'] - C0['cr_nodrive']
_dc0_load = C0['cr_rb1.5'] - C0['cr_rb0.5']
_dla_load = FITS['cr_rb1.5'][2] - FITS['cr_rb0.5'][2]
print(f"      ⇒ driving pair:  Delta c0 = {_dc0_drv:+.2f}   (banked l_A is bit-identical across "
      f"the switch)")
print(f"      ⇒ loading pair:  Delta c0 = {_dc0_load:+.2f}  against a banked {_dla_load:+.2f}  "
      f"-- {abs(_dc0_load/_dla_load - 1)*100:.2f}% apart")
check("Ⓐ③  ** THE MECHANISM THE PRE-REGISTRATION RESTS ON IS MEASURED AND IT IS RIGHT ON THE "
      "GAPS. **  *PART C's gap LEVEL is the same to `$1.4$` across the driving switch -- where the "
      "banked scale is bit-identical -- and moves `$+29.1$` across the loading switch against a "
      "banked `$+29.2$`, **three parts in a thousand.**  *So the gap sequence tracks the acoustic "
      "scale where the scale moves and holds still where it does not; the pre-registration's "
      "premise is sound and what fails below is its conclusion.**",
      abs(_dc0_drv) < 2.0 and abs(_dc0_load / _dla_load - 1) < 0.02)


# ============================================================ B. item 1, the differencing
head("B.  ① THE DIFFERENCING AS ORDERED -- AND THE PRE-REGISTERED NUMBER, REPORTED EITHER WAY")

# ⌗ THE PRE-REGISTRATION, fixed before any fit in PART C or any loading L_p was read.  The driving
#   pair's and the two bases' L_p were ALREADY IN PRINT in cc66.162, so P1 and P3 are NOT blind and
#   are recorded as arithmetic on published digits rather than as tests.  P2, P4 and P5 were blind.
PRED = 10.0
_sig_inv = {}
for tag in FITS:
    _sig_inv[tag] = SIG[tag] * np.sqrt(FITS[tag][1] / (NPT[tag] - NPAR))
print(f"      {'pair':28s} {'Delta L_p':>10s} {'sigma(bank)':>11s} {'in sigma':>9s} "
      f"{'sigma(scale-inv)':>17s} {'in sigma':>9s}")
DIFF = {}
for name, (a, b) in (('driving  (cr, r7221 ①)', DRIVING_PAIR),
                     ('driving  (lcdm control)', CONTROL_PAIR),
                     ('loading  (cr, r7221 ①)', LOADING_PAIR),
                     ('arm - control (bases)', ('cr_base', 'lcdm_base')),
                     ('arm - control (nodrive)', ('cr_nodrive', 'lcdm_nodrive'))):
    dl = LP[a] - LP[b]
    s0 = float(np.hypot(SIG[a], SIG[b]))
    s1 = float(np.hypot(_sig_inv[a], _sig_inv[b]))
    DIFF[name] = (dl, s0, s1)
    flag = ('   <- cr_rb1.5 IS ON THE BOX EDGE: THESE FOUR NUMBERS ARE NOT A MEASUREMENT'
            if EDGE[a] or EDGE[b] else '')
    print(f"      {name:28s} {dl:+10.3f} {s0:11.4f} {dl/s0:9.1f} {s1:17.4f} {dl/s1:9.2f}{flag}")
_dd, _ds0, _ds1 = DIFF['driving  (cr, r7221 ①)']
check("Ⓑ①  ** ITEM ① HAS A YES: THE DRIVING PAIR SEPARATES ON `$L_p$` BY `$56.693$`, WHICH IS "
      "`$218$` OF THE BANK'S OWN SIGMA AND `$93$` OF THE SCALE-INVARIANT ONE. **  *`r7221` asks "
      "`whether the carrier difference is larger than that` and it is larger by two orders.  "
      "⌗ The bank's `$\\sigma$` is the unit-variance one `cc66.162` published; the models carry "
      "ARBITRARY amplitudes (`$Y$` rms `$35$` against `$88$` across this one pair), so that "
      "`$\\sigma$` is amplitude-dependent and the second column -- `$\\sigma\\sqrt{\\chi^2/{\\rm "
      "dof}}$`, which is not -- is given beside it throughout*",
      abs(_dd) / _ds0 > 100 and abs(_dd) / _ds1 > 50)

_pre = abs(_dc0_drv) + abs(VPS['cr_base'] * (C2['cr_base'] - C2['cr_nodrive'])) \
    + abs(C2['cr_base'] * (VPS['cr_base'] - VPS['cr_nodrive']))
print()
print(f"      pre-registered:  |Delta L_p| = |Delta c0 + v_p Delta c2 + c2 Delta v_p| <= "
      f"{_pre:.2f}, bounded at {PRED:.0f}")
print(f"      measured:        {abs(_dd):.3f}   -- {abs(_dd)/PRED:.1f}x the bound, "
      f"{abs(_dd)/_pre:.1f}x the terms")
check("Ⓑ②  ⛔ ** MY PRE-REGISTERED NUMBER IS WRONG -- SIX TIMES THE BOUND I WROTE AND ELEVEN "
      "TIMES THE TERMS THAT PRODUCED IT -- AND IS REPORTED AS `r7221` ASKED, AGAINST THE "
      "MEASUREMENT EITHER WAY. **  *The terms the gap geometry allows sum to `$5.05$` and I "
      "bounded the prediction at `$10$`; it is `$56.693$`.  ⚠ **AND IT WAS NOT "
      "A BLIND PREDICTION:** `cc66.162` printed `$L_p=350.131$` and `$293.438$`, so this "
      "difference was already in print and I knew the bound was wrong before the run began.  *It "
      "is recorded as a failed prediction and not as a test; the blind ones were the loading pair, "
      "the sky's `$L_p$` and the arm--control differencing, and they are below.**",
      abs(_dd) > 5.0 * _pre and abs(_dd) > PRED)

print()
print(f"      {'spectrum':13s} {'L_p':>9s} {'fitted curve mean gap':>22s} {'off by':>8s} "
      f"{'max|peak - data peak|':>22s}")
LOCK, MGF = {}, {}
for tag, p in SPECTRA + (('sky', None),):
    x0, _fun, _lA, ls, Y = FITS[tag]
    A = design(ls, *x0)
    c, *_ = np.linalg.lstsq(A, Y, rcond=None)
    pf, pd = locate(ls, A @ c), locate(ls, Y)
    gf = np.diff(pf)
    mgf = float(np.mean(gf)) if len(gf) else float('nan')
    n = min(len(pf), len(pd))
    off = float(np.max(np.abs(pf[:n] - pd[:n]))) if n else float('nan')
    MGF[tag] = mgf
    LOCK[tag] = abs(LP[tag] / mgf - 1.0)
    print(f"      {tag:13s} {LP[tag]:9.3f} {mgf:22.2f} {LOCK[tag]*100:7.1f}% {off:22.2f}")
_locked = tuple(t for t in LOCK if LOCK[t] < 0.01)
print(f"      ⇒ `L_p` IS the fitted curve's own spacing on: {', '.join(sorted(_locked))}")
check("Ⓑ③  ⛔⛭⛭⛭ ** AND THAT IS WHY: `$L_p$` IS THE FITTED CURVE'S OWN PEAK SPACING ONLY WHERE THE "
      "FIT LOCKS ONTO THE PEAK TRAIN -- `$0.2$` PER CENT ON THE TWO DRIVING-OFF SPECTRA, "
      "`$21$`--`$27$` PER CENT OUT ON THE OTHER FOUR INCLUDING THE SKY. **  *Pointing PART C's own "
      "locator at the FITTED curve, not at the data: where the comb locks, its maxima sit `$1.6$` "
      "from the data's and `$L_p$` is their spacing; where it does not, they sit `$21$`--`$24$` out "
      "and `$L_p$` is the spacing of a phase map that no feature of the curve has.*  ⌗ *The sky's "
      "`$558$` in that last column is NOT its fit being worse: it is the DATA's own located peaks "
      "coming back out of order at the bank's native binning, which is PART D's subject*  ⇒ "
      "**So the `$218\\sigma$` is the difference between a fit that locks and one that does not, "
      "and the carrier's role in it is that the driving is what breaks the lock.**",
      set(_locked) == {'cr_nodrive', 'lcdm_nodrive'}
      and all(LOCK[t] > 0.15 for t in ('cr_base', 'lcdm_base', 'cr_rb0.5', 'sky')))

print()
lb, db, lA = binned(os.path.join(LEV, 'cr_rb1.5.npz'))
ls, Y = detilt(lb, db)
bw, _rw = fit(ls, Y, box=WBOX, l0s=W0S)
lpw, sgw, _rhow, vpsw, _insw = centred(ls, Y, bw, box=WBOX)
print(f"      cr_rb1.5 at the {LBOX[1]:.0f} box: lA {FITS['cr_rb1.5'][0][0]:8.3f}  "
      f"chi2 {FITS['cr_rb1.5'][1]:10.4g}  sigma {SIG['cr_rb1.5']:.2g}")
print(f"      cr_rb1.5 at the {WBOX[1]:.0f} box: lA {bw.x[0]:8.3f}  chi2 {bw.fun:10.4g}  "
      f"sigma {sgw:.2g}")
check("Ⓑ④  ⛔ ** SO THE LOADING HALF OF ITEM ① CANNOT BE DIFFERENCED AT ALL: `cr_rb1.5` HAS NO "
      "INTERIOR OPTIMUM IN ANY BOX. **  *It sits on the edge at `$430.000$`; widen the box to "
      "`$900$` and it sits on the edge at `$900.000$` with `$\\chi^{2}$` falling `$1.94\\times10^{4}"
      "\\to1.39\\times10^{3}$`.  **The direction is unbounded, which is `cc66.160`'s `$542\\times$` "
      "pitfall arriving where this order needed it not to** -- and the covariance there is "
      "degenerate, so the `$\\sigma$` is `$7\\times10^{-7}$` and means nothing.*  ⇒ *`r7221` ① "
      "asked for two pairs and the bank supports one of them*",
      bw.x[0] > WBOX[1] - 1.0 and bw.fun < FITS['cr_rb1.5'][1] and sgw < 1e-5)

print()
print(f"      {'window':>12s} {'N':>4s} {'lA(v=0)':>9s} {'L_p':>9s} {'sigma':>8s} {'rho(lA,d)':>10s}")
# ⌍ (150, 1600) is NOT refitted here: PART A fitted exactly that window on exactly this
#    spectrum, so it is carried in from there -- which also keeps the two tables consistent
#    by construction rather than by coincidence.
WIN = ((150., 1000.), (150., 1300.), (150., 1950.), (250., 1950.))
NATIVE = (150., 1600.)
WLP, WRHO, WSIG, WN = [], [], [], []
lb, db, lA = binned(os.path.join(LEV, 'cr_nodrive.npz'))
_rows = []
for lo, hi in WIN:
    ls, Y = detilt(lb, db, lo, hi)
    b, _r = fit(ls, Y)
    lp, sg, rho, _v, _i = centred(ls, Y, b)
    WLP.append(lp); WRHO.append(rho); WSIG.append(sg); WN.append(len(ls))
    _rows.append((lo, hi, len(ls), float(b.x[0]), lp, sg, rho, ''))
WLP.append(LP['cr_nodrive']); WRHO.append(RHO['cr_nodrive'])
WSIG.append(SIG['cr_nodrive']); WN.append(NPT['cr_nodrive'])
_rows.append((NATIVE[0], NATIVE[1], NPT['cr_nodrive'], float(FITS['cr_nodrive'][0][0]),
              LP['cr_nodrive'], SIG['cr_nodrive'], RHO['cr_nodrive'], '   <- PART A, not refitted'))
for lo, hi, nn, l0, lp, sg, rho, note in sorted(_rows, key=lambda t: (t[0], t[1])):
    print(f"      {int(lo):5d}-{int(hi):<6d} {nn:4d} {l0:9.3f} {lp:9.3f} {sg:8.4f} "
          f"{rho:+10.4f}{note}")
print(f"      ⇒ L_p moves {max(WLP)-min(WLP):.1f} across the five windows, while the formal "
      f"sigma over them is {min(WSIG):.2f}-{max(WSIG):.2f}")
_ob = [lA - q for q in WLP]
print(f"      ⇒ and its offset from banked ({lA:.3f}) over the same five windows: "
      f"{min(_ob):+.2f} to {max(_ob):+.2f}  -- one sign throughout, and no larger than the "
      f"spread the windows themselves produce")
check("Ⓑ⑤  ⛔⛭⛭ ** AND THE SIGMA `r7221` ASKS ME TO MEASURE AGAINST IS NOT AN ERROR ON `$L_p$`: "
      "MOVING THE WINDOW'S TOP EDGE FROM `$1000$` TO `$1950$` MOVES `cr_nodrive`'s `$L_p$` BY "
      "`$14.3$` -- FIVE PER CENT -- WHILE ITS FORMAL `$\\sigma$` THERE IS `$0.01$`--`$4.28$`. **  "
      "*So the premise `the orthogonal direction it carries to `$0.08$` per cent` is a statement "
      "about a formal error and not about reproducibility.  **The bank carries a `$0.08$` per cent "
      "error bar on a number that moves by five per cent when you choose a different top edge for "
      "the same window** -- and `larger than the bank's own sigma` is therefore a test that any "
      "difference passes.*  ⇒ *This is the one place in the order I think the specification is "
      "wrong rather than merely unlucky, and it is measured rather than argued*  ⌈ **AND IT "
      "PUTS A NUMBER IN PRINT UNDER STRAIN, WHICH IS WHY IT IS HERE AND NOT ONLY IN MY "
      "REPLY: `cc66.162`'s `$35\\sigma$` for `cr_nodrive` -- the figure `sec:refit-bound` "
      "quotes -- is an offset of `$7.94$` from banked, and the WINDOW alone moves `$L_p$` by "
      "`$14.3$`.**  *The robust statement the five windows support is that `$L_p$` lies BELOW "
      "banked on every one of them, by `$5.4$`--`$19.8$`; the `$35$` is not robust to the "
      "window and I am flagging it rather than leaving it to be found*",
      max(WLP) - min(WLP) > 10.0 and max(_ob) > 0 and min(_ob) > 0)


print()
print(f"      and the same two conventions on `cc66.162`'s own published comparison, because two of")
print(f"      its digits are quoted in `sec:refit-bound`:")
print(f"      {'spectrum':13s} {'L_p':>9s} {'banked':>9s} {'offset':>8s} {'sig(bank)':>10s} "
      f"{'in sig':>7s} {'sig(scale-free)':>16s} {'in sig':>7s}")
NS0, NS1 = {}, {}
for tag in ('cr_base', 'lcdm_base', 'cr_nodrive', 'lcdm_nodrive', 'cr_rb0.5'):
    off = LP[tag] - FITS[tag][2]
    NS0[tag], NS1[tag] = abs(off) / SIG[tag], abs(off) / _sig_inv[tag]
    print(f"      {tag:13s} {LP[tag]:9.3f} {FITS[tag][2]:9.3f} {off:+8.3f} {SIG[tag]:10.4f} "
          f"{NS0[tag]:7.0f} {_sig_inv[tag]:16.4f} {NS1[tag]:7.0f}")
check("Ⓑ⑥  ⛔ ** AND THE TWO FIGURES `cc66.162` PUT IN PRINT DO NOT SURVIVE THE CHANGE OF "
      "CONVENTION INTACT: ITS `$35\\sigma$` READS `$54$` AND ITS `$379\\sigma$` READS `$82$`. **  "
      "*The conclusion and the ordering survive -- every one of the five is still tens of sigma from "
      "banked on both conventions, which is what `cc66.162`'s `Ⓒ①` actually asserts "
      "(`$>10$`).  **What does not survive is `more than three hundred`, which becomes `more than "
      "eighty`.**  ⌗ *And neither convention is an error bar in the ordinary sense: these are "
      "NOISELESS model spectra, so what is being inverted is model misfit and not noise -- which is "
      "why `Ⓑ⑤`'s window spread, not either sigma, is the honest measure of how well the "
      "number is determined.*",
      all(NS1[t] > 10 for t in NS1) and 50 < NS1['cr_nodrive'] < 60 and 75 < NS1['cr_base'] < 90)

# ============================================================ C. item 2, the sky
head("C.  ② `$L_p$` CARRIED TO THE SKY BY THE IDENTICAL EXTRACTION -- AND WHAT IT IS WORTH THERE")

print(f"      L_p(sky) = {LP['sky']:.3f}   on {NPT['sky']} binned points, the same bins the models "
      f"cover")
print(f"      {'against':20s} {'L_p':>9s} {'sky - it':>9s}")
for tag in ('cr_base', 'lcdm_base', 'cr_nodrive', 'lcdm_nodrive', 'cr_rb0.5'):
    print(f"      {tag:20s} {LP[tag]:9.3f} {LP['sky']-LP[tag]:+9.3f}")
check("Ⓒ①  ** THE SKY LANDS ON THE DRIVING-ON BASES: `$L_p=351.807$`, WITHIN `$1.68$` AND `$1.97$` "
      "OF THEM AND `$58.4$` FROM THE DRIVING-OFF PAIR. **  *Read naively that is the sky choosing "
      "the driving over its absence, on the row's tight direction, by two orders of the bank's "
      "`$\\sigma$`.  **It is the reading this order was built to reach and it is the one I am "
      "about to withdraw** -- stated first, in the terms it would be stated in if it held*",
      abs(LP['sky'] - LP['cr_base']) < 3.0 and abs(LP['sky'] - LP['cr_nodrive']) > 50.0)

x0, _fun, _lA, ls, Y = FITS['sky']
A = design(ls, *x0)
c, *_ = np.linalg.lstsq(A, Y, rcond=None)
r = Y - A @ c
lb_s, db_s, _ = SKY
_m = (lb_s >= LMIN) & (lb_s <= LMAX) & (db_s > 0) & np.isfinite(db_s)
_t = float(np.polyfit(np.log(lb_s[_m]), np.log(db_s[_m]), 1)[0])
# ⌗ the de-tilt is a DIAGONAL rescaling of the binned C_l, so plik_lite's covariance transforms
#   exactly: no approximation enters here, and the off-diagonal is kept rather than dropped.
D = np.diag((FACB[MASK] / lb_s ** _t)[_m])
COVY = D @ CS.COV_TT[np.ix_(MASK, MASK)][np.ix_(_m, _m)] @ D
chi2_diag = float(np.sum(r ** 2 / np.diag(COVY)))
chi2_full = float(r @ np.linalg.solve(COVY, r))
_dof = NPT['sky'] - NPAR
print()
print(f"      the curve the matched extraction returns, scored against plik_lite's own covariance:")
print(f"          diagonal only    chi2 {chi2_diag:9.4g} / {_dof} dof = {chi2_diag/_dof:7.3f}")
print(f"          full covariance  chi2 {chi2_full:9.4g} / {_dof} dof = {chi2_full/_dof:7.3f}")
print(f"      and its L_p against its own curve's peak spacing: {LP['sky']:.3f} vs "
      f"{MGF['sky']:.2f}, {LOCK['sky']*100:.1f}% out")
check("Ⓒ②  ⛔⛭⛭⛭ ** AND THE READING IS VOID, ON ITS OWN TWO COUNTS. **  *The curve the identical "
      "extraction returns is **rejected by `plik_lite` at `$\\chi^{2}/{\\rm dof}=11.8$` on the "
      "full covariance** -- the de-tilt is a diagonal rescaling so that covariance transforms "
      "exactly and nothing is dropped -- and its `$L_p$` misses its OWN curve's peak spacing by "
      "`$62$`, `$21$` per cent, **which is the unlocked signature of `Ⓑ③` exactly.**  ⇒ *So "
      "`$351.807$` is a parameter of a phase map belonging to a curve the data reject, and its "
      "agreement with the driving-ON bases is agreement about the failure mode they share and not "
      "about the driving*",
      chi2_full / _dof > 5.0 and LOCK['sky'] > 0.15)

_ac = DIFF['arm - control (bases)']
print()
print(f"      the section's matched-procedure differencing, arm and control through the same "
      f"extraction:")
print(f"          (arm - sky)      {LP['cr_base'] - LP['sky']:+9.3f}")
print(f"          (control - sky)  {LP['lcdm_base'] - LP['sky']:+9.3f}")
print(f"          difference       {_ac[0]:+9.3f}   = {abs(_ac[0]/_ac[1]):.2f} sigma(bank), "
      f"{abs(_ac[0]/_ac[2]):.2f} sigma(scale-invariant)")
print(f"          the carrier, for scale                    {abs(_dd/_ds0):.0f} sigma(bank), "
      f"{abs(_dd/_ds1):.0f} sigma(scale-invariant)")
check("Ⓒ③  ⛔ ** AND THE MATCHED DIFFERENCING IS BLIND TO THE ARM: `$(\\rm arm-sky)-(\\rm "
      "control-sky)=0.295$`, WHICH IS `$1.6$` OF THE BANK'S SIGMA AND `$0.35$` OF THE "
      "SCALE-INVARIANT ONE, AGAINST THE CARRIER'S `$218$`. **  *The extraction reaches the sky -- "
      "`r7221` ② is right that the comb can be pointed where the locator could not -- and what it "
      "says there does not distinguish the arm from `$\\Lambda$CDM`.  **A statistic that separates "
      "the carrier by two orders and the arm by one sigma is not an instrument for this "
      "measurement**, which is `cc66.161`'s conclusion reached from the other end*",
      abs(_ac[0] / _ac[1]) < 3.0 and abs(_ac[0] / _ac[2]) < 1.0)

_dlp = LP['cr_rb0.5'] - LP['cr_base']
_dban = FITS['cr_rb0.5'][2] - FITS['cr_base'][2]
print()
print(f"      and the response of L_p to a REAL change in the acoustic scale, on the only lever "
      f"the bank has:")
print(f"          banked l_A  {FITS['cr_base'][2]:.3f} -> {FITS['cr_rb0.5'][2]:.3f}  "
      f"({_dban:+.3f})")
print(f"          L_p         {LP['cr_base']:.3f} -> {LP['cr_rb0.5']:.3f}  ({_dlp:+.3f})   "
      f"= {_dlp/_dban*100:.0f}% of it")
check("Ⓒ④  ⛔ ** AND `$L_p$` CARRIES ONLY `$16$` PER CENT OF A REAL CHANGE IN THE ACOUSTIC SCALE: "
      "`cr_rb0.5`'s BANKED SCALE IS `$15.32$` BELOW `cr_base`'s AND ITS `$L_p$` IS `$2.46$` "
      "BELOW. **  *With a quoted `$\\sigma$` of `$0.21$` that under-response would be reported as "
      "a `$12\\sigma$` determination of a number six times too small.*  ⚠ **The caveat is real and "
      "it is the bank's: `cr_rb0.5` moves `$R_b$` as well as the scale, so `$16$` per cent is a "
      "response along a mixed direction and not `$\\partial L_p/\\partial\\ell_A$`** -- *and the "
      "bank has no spectrum that moves the scale alone, which is itself the answer to whether this "
      "could be calibrated out*",
      0.0 < _dlp / _dban < 0.4)


# ============================================================ D. the terminal statement
head("D.  THE REMAINDER r7221 NAMES -- `what point count, window and per-point error` -- HAS NO "
     "NUMBER")

# the same spectrum at half the point count: adjacent plik_lite bins merged in pairs, weighted by
# the ell each bin covers, which is how the likelihood itself weights within a bin.
WID = (CS.BIN_HI[MASK] - CS.BIN_LO[MASK] + 1).astype(float)


def pair_merge(lb, db, g):
    m = (lb >= LMIN) & (lb <= LMAX) & (db > 0) & np.isfinite(db)
    w = WID[m]
    n = (len(w) // g) * g
    ww = w[:n].reshape(-1, g)
    lc = (lb[m][:n].reshape(-1, g) * ww).sum(1) / ww.sum(1)
    dd = (db[m][:n].reshape(-1, g) * ww).sum(1) / ww.sum(1)
    return lc, dd, ww.sum(1)


lb, db, lA = binned(os.path.join(LEV, 'cr_nodrive.npz'))
lc, dd, wd = pair_merge(lb, db, 2)
ls2, Y2 = detilt(lc, dd)
b2, _r2 = fit(ls2, Y2)
lp2, sg2, rho2, _v2, _i2 = centred(ls2, Y2, b2)
print(f"      cr_nodrive at {NPT['cr_nodrive']:4d} points: rho {RHO['cr_nodrive']:+.4f}  "
      f"L_p {LP['cr_nodrive']:.3f}  sigma {SIG['cr_nodrive']:.4f}")
print(f"      cr_nodrive at {len(ls2):4d} points: rho {rho2:+.4f}  L_p {lp2:.3f}  sigma {sg2:.4f}"
      f"   <- bins merged in pairs, median width {np.median(wd):.0f}")

RHOS = [(t, NPT[t], '150-1600', RHO[t]) for t, _p in SPECTRA if not EDGE[t]]
RHOS.append(('sky', NPT['sky'], '150-1600', RHO['sky']))
RHOS.append(('cr_nodrive', len(ls2), '150-1600 /2', rho2))
for (lo, hi), rr, nn in zip(WIN, WRHO, WN):
    if (lo, hi) != (150., 1600.):
        RHOS.append(('cr_nodrive', nn, f'{int(lo)}-{int(hi)}', rr))
# ⌍ only cr_base is scanned off-window here.  `lcdm_nodrive` was scanned too while this was
#    being built and returned cr_nodrive's values to four decimals at both windows, so it is
#    two fits that add no information and it is out.
for tag, p in (('cr_base', os.path.join(GO, 'cr_base.npz')),):
    lbx, dbx, _ = binned(p)
    for lo, hi in ((150., 1300.), (150., 1950.)):
        lsx, Yx = detilt(lbx, dbx, lo, hi)
        bx, _rx = fit(lsx, Yx)
        _l, _s, rhox, _vv, _ii = centred(lsx, Yx, bx)
        RHOS.append((tag, len(lsx), f'{int(lo)}-{int(hi)}', rhox))
print()
print(f"      {'spectrum':13s} {'N':>5s} {'window':>12s} {'rho(lA,d)':>10s}")
for tag, nn, win, rr in RHOS:
    print(f"      {tag:13s} {nn:5d} {win:>12s} {rr:+10.4f}")
_ar = [abs(rr) for _t, _n, _w, rr in RHOS]
print(f"      ⇒ {len(RHOS)} fits, {min(n for _t, n, _w, _r in RHOS)}-"
      f"{max(n for _t, n, _w, _r in RHOS)} points, five windows, six spectra: "
      f"|rho| in [{min(_ar):.4f}, {max(_ar):.4f}]")
check("Ⓓ①  ⛔⛭⛭⛭ ** THE DEGENERACY IS INVARIANT TO EVERYTHING THE BANK CAN VARY: `$|\\rho(\\ell_A,"
      "d)|$` STAYS IN `$[0.939,0.977]$` ACROSS THIRTEEN FITS, `$78$`--`$176$` POINTS, FIVE WINDOWS "
      "AND SIX SPECTRA -- AND HALVING THE POINT COUNT LEAVES IT AT `$-0.9549$` AGAINST "
      "`$-0.9548$`. **  *So `r7221`'s remainder -- `what point count, window and per-point error "
      "would bring `$0.1929$` against `$1.0390$` within reach` -- **has no number, because no "
      "point count or window in reach of this bank moves the correlation at all.**  ⌈ And "
      "`r7219`'s `what would change it is a finer binning rather than a further parameter`, now in "
      "print, is measurably wrong: halving the points changed `$\\rho$` in the fourth decimal and "
      "only inflated `$\\sigma$` by `$\\sqrt2$`.*  ⇒ *`$(v,v^{2})$` are monomials and their "
      "correlation over an interval is set by the interval's endpoint RATIO, which is why "
      "`cc66.162`'s shear removes it exactly and why sampling does not touch it*",
      len(RHOS) >= 13 and min(_ar) > 0.90 and max(_ar) < 0.99 and abs(abs(rho2) - 0.9549) < 5e-4)

print()
print(f"      and what the bank's points DO buy, on the instrument the row wrote off -- PART C's")
print(f"      locator pointed at the SKY and at the MODEL through the identical merge:")
print(f"      {'merge':>7s} {'bins':>5s} {'width':>6s} {'noise/increment':>18s} "
      f"{'sky peaks':>10s} {'model peaks':>12s} {'max|d|':>7s}")
lbs, dbs, _ = SKY
_sd = (np.sqrt(np.diag(CS.COV_TT))[MASK] * FACB[MASK])
lbm, dbm, _ = binned(os.path.join(GO, 'cr_base.npz'))
_amp = float(np.sum(dbs[_m] * dbm[_m]) / np.sum(dbm[_m] ** 2))
REBIN = {}
for g in (1, 2, 3):
    lc, ds, wd = pair_merge(lbs, dbs, g)
    _, dm, _ = pair_merge(lbs, dbm * _amp, g)
    _, sg_, _ = pair_merge(lbs, _sd, g)
    sg_ = sg_ / np.sqrt(g)
    l2, Ys = detilt(lc, ds)
    _, Ym = detilt(lc, dm)
    sY = sg_ / lc ** _t
    rat = (0.5 * (sY[1:] + sY[:-1])) / np.abs(np.diff(Ym))
    ps, pm = locate(l2, Ys), locate(l2, Ym)
    nn = min(len(ps), len(pm))
    off = float(np.max(np.abs(ps[:nn] - pm[:nn]))) if nn else float('nan')
    REBIN[g] = (len(ps), len(pm), off, float(np.percentile(rat, 90)))
    print(f"      {g:7d} {len(lc):5d} {np.median(wd):6.1f} "
          f"{np.median(rat):8.3f} (p90 {np.percentile(rat,90):5.3f}) {len(ps):10d} {len(pm):12d} "
          f"{f'{off:7.2f}' if nn else '     --'}")
    if len(ps):
        print(f"              sky gaps {[int(q) for q in np.diff(ps)]}   "
              f"model gaps {[int(q) for q in np.diff(pm)]}")
check("Ⓓ②  ⛭⛭⛭ ** AND MERGED IN PAIRS THE LOCATOR READS THE SKY: FOUR PEAKS WITHIN `$3.37$` OF ITS "
      "OWN READ OF THE MODEL THROUGH THE IDENTICAL MERGE, AGAINST A `$547$` DISPLACEMENT AT THE "
      "BANK'S NATIVE `$9$`. **  *At `$9$` per bin the per-bin noise is `$2.4$` times the signal's "
      "own bin-to-bin increment at the ninetieth percentile and the locator returns four maxima "
      "OUT OF ORDER -- `cc66.159`'s catastrophe.  At `$18$` that ratio is `$0.82$` and the sky's "
      "gaps come back `$303$`/`$268$`/`$309$` against the model's `$302$`/`$269$`/`$312$`.*  ⌗ "
      "**At `$27$` the locator returns NOTHING ON EITHER, which is its own `$\\pm40$` window "
      "holding fewer than four points -- a property of the locator and not of the sky**, and it is "
      "why the usable merge is a factor of two and only a factor of two",
      REBIN[1][2] > 100.0 and REBIN[2][0] == 4 and REBIN[2][2] < 5.0
      and REBIN[3][0] == 0 and REBIN[3][1] == 0)

check("Ⓓ③  ⛔⛭⛭ ** SO THE ROW'S TWO HALVES WANT OPPOSITE BINNINGS AND THE REACHABLE HALF IS THE "
      "PEAK PLANE, NOT THE COMB. **  *The comb needs points it cannot use -- `$\\rho$` is "
      "`$-0.95$` at `$176$` and `$-0.95$` at `$78$` -- and the locator needs the bank merged, "
      "which costs exactly the points the comb is short of.  `r7221` says `the four-parameter comb "
      "can be pointed at the sky and the peak locator of cc66.159 could not, which is the whole "
      "reason the comb was built`; **measured, the comb points at the sky and returns a rejected "
      "fit whose parameter moves five per cent with the window, and the locator reads the sky's "
      "peaks to `$3.4$` once the bank is merged in pairs.**  ⇒ *That is a reversal of the "
      "instrument choice and it is the one thing here I would act on.*  ⚠ **AND ITS BURDEN IS "
      "NAMED AND NOT DISCHARGED: four peaks, not five; `cc66.156`'s statistic is banked at five; "
      "and forming `$(\\varphi,{\\rm alt})$` on four peaks of a merged bank is a new measurement "
      "with its own validation.  I am not making it -- `r7221` says `I am not asking for an "
      "instrument after it` and this is a route, offered, not an instrument built.**",
      REBIN[2][0] == 4 and min(_ar) > 0.90 and LOCK['sky'] > 0.15)

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print(f"  ✔ {len(ran) - len(fail)} of {len(ran)} checks pass -- the carriers separate on L_p by "
      "218 sigma, the separation")
print("    is the comb's own peak count, the sky's reading is void, and the closure has no number.")
print(BAR)
sys.exit(0)
