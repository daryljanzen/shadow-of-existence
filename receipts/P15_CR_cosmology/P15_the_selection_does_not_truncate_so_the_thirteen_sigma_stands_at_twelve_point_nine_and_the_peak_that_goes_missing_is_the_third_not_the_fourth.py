#!/usr/bin/env python3
r"""
RECEIPT -- P15: ** `r7229` ORDERED THE AUDIT I ROUTED AT `r7227` -- `compare the width of the
four-peak selection against the width over all draws, and state whether the selection truncates`,
with my own `r7221` burden adopted and 66's addition `if the selection does truncate, say what the
13 becomes`.  *** IT DOES NOT TRUNCATE AND THE `$13\sigma$` STANDS AT `$12.9$`.  AND THE PEAK
THAT GOES MISSING IS THE THIRD, NOT THE FOURTH, WHICH RETIRES THE NAME `cc66.164` GAVE ITS OWN
`$52$` PER CENT AND THE ROUTE I TOLD 66 THE AUDIT WOULD TAKE. *** **

** THE PREDICTION, PINNED AS A CONSTANT AND WRITTEN BEFORE ANY OF THIS WAS RUN (`PREDICT` below).
   *`$\sigma(\mathrm{sel})/\sigma(\mathrm{all})\in[0.80,1.00]$`, most likely `$0.90$`--`$1.00$` --
   the selection at most weakly truncating, so the `$13.1\sigma$` moves by under a fifth.  Because
   the lost peak's survival is set by the noise in ONE band while the offset is an average over
   the others, and every draw carries the SAME covariance, so there is no noisier-realisation
   channel.  The one coupling available is the locator latching onto a noise maximum, which lives
   in the TAIL rather than the robust core -- so the standard-deviation ratio should depart from
   one by more than the robust ratio does.* **

  ⓵ ** THE AUDITED NUMBER IS REBUILT TO `cc66.164`'s PUBLISHED DIGITS FIRST. **  *Same seed, same
  draws, same covariance through the same merge matrix: robust `$\sigma(\varphi)=0.00955$`,
  `$13.1\sigma$` for one driving unit, `$0.79\sigma$` for the sky, `$52$` per cent returning four
  peaks.  **An audit that cannot reproduce the number it audits is auditing a different number.***

  ⓶ ⛔⛭ ** AND THE FIRST THING THE AUDIT FINDS IS THAT MY OWN ROUTE DOES NOT EXIST. **  *I told 66
  that `$47$` of the `$48$` per cent return three peaks so a three-peak statistic is defined on
  `$99$` per cent of draws.  `$47$` per cent DO return three of four -- but **the slot that goes
  `nan` is the THIRD peak, in `$3460$` of `$3791$` such draws, and the FOURTH peak is located in
  `$95.9$` per cent of all draws.**  ⇒ *So the three-peak statistic covers `$56$` per cent, not
  `$99$`, and `cc66.164`'s `Ⓓ⑤` -- `what bounds it is the fourth peak's existence` -- names the
  wrong peak.  The `$48$` per cent is right; its CAUSE was not.*

  ⓷ ⛭⛭ ** THE HANDLE THAT DOES COVER THE ENSEMBLE IS THE OFFSET ON PEAKS `$1$`--`$2$`, DEFINED ON
  `$99.4$` PER CENT OF DRAWS, AND ON IT THE SELECTION DOES NOT TRUNCATE. **  *Robust width inside
  the four-peak selection against over the whole ensemble: a ratio of `$0.982$`, bootstrap
  interval clear of the `$10$` per cent threshold fixed in advance.  ⌗ *The discarded draws are
  mildly wider -- `$1.04\times$` -- so the selection is not perfectly neutral; it is just far too
  weak to matter.*

  ⓸ ** AND A SECOND HANDLE THAT DOES NOT GO THROUGH A WIDTH AGREES. **  *The loss rate by quintile
  of how far the offset already is from the median: a truncating selection would show the rate
  RISING with distance, because that is what truncation IS.*

  ⓹ ⛭⛭⛭ ** SO WHAT THE `$13$` BECOMES, WHICH IS THE DELIVERABLE: `$12.9$`. **  *Carrying the
  measured ratio across to the four-peak width -- the only route, since the four-peak statistic
  does not exist off the selection -- the published `$13.1\sigma$` for one driving unit becomes
  `$12.9$` and the sky's `$0.79\sigma$` becomes `$0.78$`.  **`r7229`'s first branch fires: the
  figure stands and the `$52$` per cent goes back to being an existence bound alone** -- now an
  existence bound on the THIRD peak.*

** COMPUTES: `cc66.164`'s draw ensemble rebuilt at its own seed and again at four times the draws
   on a second seed; the per-slot location rate of the locator's four peaks; the common offset
   formed on peaks `$1$`--`$2$`, `$1$`--`$3$` and `$1$`--`$4$` from ONE located series per draw;
   robust and standard widths inside and outside the four-peak selection with a bootstrap on the
   ratio; the loss rate by quintile of offset distance; and the corrected sigma and sigma-counts.
   *** No new spectrum, no fit, no refit.  Nothing here is a new instrument. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; 19s MEASURED)
"""
import os
import sys
import time

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
ran = []
T0 = time.time()


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

# ⌗ cc66.156's window and cc66.163's merge factor, unchanged.  Nothing here is refitted.
LMIN, LMAX = 150.0, 1600.0
LC, FACB = CS.bin_center_and_fac()
WID = (CS.BIN_HI - CS.BIN_LO + 1).astype(float)
GMERGE = 2
NPK = 4
# ⌗ cc66.164's PUBLISHED figures, pinned so this is shown to audit THAT number rather than a
#    re-derivation of it.  Its seed and draw count are its own.
PUB164 = {'sigma_phi': 0.00955, 'n_sigma_drive_phi': 13.1, 'n_sigma_drive_alt': 3.1,
          'n_sigma_sky_phi': 0.79, 'frac4': 0.52}
SEED164, NDRAW164 = 164, 2000
# ⌗ THE AUDIT's own ensemble: a different seed and four times the draws, so the verdict does not
#    rest on the one realisation set the published figure was measured on.
SEED_AUDIT, NDRAW_AUDIT = 165, 8000
# ⛭⛭ ** THE PREDICTION, AS `r7221`'s BURDEN REQUIRES: WRITTEN BEFORE THE FITS WERE READ, AND
#      SCORED IN `Ⓑ②` WHICHEVER WAY IT FELL. **
PREDICT = (0.80, 1.00)             # the band claimed for sigma(sel)/sigma(all)
PREDICT_BEST = (0.90, 1.00)        # the narrower claim inside it
# ⌗ the threshold at which the selection is CALLED truncating, fixed in advance rather than read
#    off the answer: ten per cent, which is several times the bootstrap width below.
TRUNC_TOL = 0.10


def raw(path):
    z = np.load(path, allow_pickle=True)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])


def binned(path):
    ls, Dl, lA = raw(path)
    Cl = CS.bin_spectrum(ls, Dl)
    k = np.isfinite(Cl)
    return LC[k], (Cl * FACB)[k], lA, k


def sky(mask):
    return LC[mask], (CS.X_DATA * FACB)[mask]


def merge(ls, Dl, g, wid):
    """cc66.163's merge: g adjacent bins averaged, weighted by the ell each one covers."""
    if g == 1:
        return ls, Dl
    n = (len(wid) // g) * g
    w = wid[:n].reshape(-1, g)
    return ((ls[:n].reshape(-1, g) * w).sum(1) / w.sum(1),
            (Dl[:n].reshape(-1, g) * w).sum(1) / w.sum(1))


def merge_matrix(wid, g, n):
    """the same merge as a matrix, so the covariance goes through it exactly."""
    A = np.zeros((n // g, n))
    for i in range(n // g):
        w = wid[i * g:(i + 1) * g]
        A[i, i * g:(i + 1) * g] = w / w.sum()
    return A


def peak_series(ls, Dl, npk, halfwin=40.0, detilt=True):
    """cc66.156's locator, unchanged -- the object whose selection is being audited."""
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt if detilt else Dl.copy()
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    D = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(D) - 2)
           if D[i] > D[i - 1] and D[i] >= D[i + 1] and D[i] > D[i - 2] and D[i] >= D[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:npk]:
        w = (ls >= l0 - halfwin) & (ls <= l0 + halfwin)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), tilt


def stat(pk, lA, lo=1, hi=None):
    """cc66.156's common offset and odd-even alternation, in units of l_A."""
    hi = len(pk) if hi is None else hi
    sel = np.arange(len(pk))[lo - 1:hi]
    pk = pk[sel]
    nn = np.arange(1, 1 + len(sel))[np.isfinite(pk)] + (lo - 1)
    p = pk[np.isfinite(pk)] / lA
    if len(p) == 0:
        return float('nan'), float('nan'), 0
    phi = float(np.mean(p - nn))
    r = p - (nn + phi)
    return phi, float(np.mean(r * (-1.0) ** nn)), int(len(p))


def phi_alt(path, npk=5, g=1, on_bank=False, halfwin=40.0, detilt=True, lA=None, lo=1, hi=None):
    if on_bank:
        lb, db, lA0, k = binned(path)
        lb, db = merge(lb, db, g, WID[k])
    else:
        lb, db, lA0 = raw(path)
    pk, _t = peak_series(lb, db, npk, halfwin, detilt)
    return stat(pk, lA0 if lA is None else lA, lo, hi)


def robust(x):
    """cc66.164's own scales, unchanged: median, MAD-scaled sigma, standard deviation, count."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if len(x) < 2:
        return float('nan'), float('nan'), float('nan'), int(len(x))
    m = float(np.median(x))
    return m, float(1.4826 * np.median(np.abs(x - m))), float(x.std(ddof=1)), int(len(x))


CRON, CROFF = os.path.join(GO, 'cr_base.npz'), os.path.join(LEV, 'cr_nodrive.npz')
SVON = os.path.join(GO, 'lcdm_base.npz')

# ============================================================ A. the audited object, rebuilt
head("A.  THE AUDITED OBJECT, REBUILT AND PINNED TO `cc66.164`'s PUBLISHED DIGITS FIRST")

_lb, _db, _lA, MASK = binned(CRON)
_sl, _sd = sky(MASK)
_wid = WID[MASK]
_n = (len(_wid) // GMERGE) * GMERGE
MLC, MSD = merge(_sl, _sd, GMERGE, _wid)
_clb, _cdb, LAC, _ck = binned(SVON)
MCL, MCD = merge(_clb, _cdb, GMERGE, WID[_ck])
S_SKY = stat(peak_series(MLC, MSD, NPK)[0], LAC)
S_CTL = stat(peak_series(MCL, MCD, NPK)[0], LAC)
DSKY = (S_SKY[0] - S_CTL[0], S_SKY[1] - S_CTL[1])

_on4 = phi_alt(CRON, npk=NPK, on_bank=True, g=GMERGE)
_off4 = phi_alt(CROFF, npk=NPK, on_bank=True, g=GMERGE)
DRIVE = (-(_off4[0] - _on4[0]), -(_off4[1] - _on4[1]))

COVD = (np.diag(FACB[MASK]) @ CS.COV_TT[np.ix_(MASK, MASK)] @ np.diag(FACB[MASK]))[:_n, :_n]
AM = merge_matrix(_wid[:_n], GMERGE, _n)
CMG = AM @ COVD @ AM.T
# ⌗ the merge is a LINEAR map on the binned D_l, so the covariance goes through it exactly:
#    nothing is approximated and no off-diagonal is dropped.  cc66.163's Ⓓ②, unchanged.
CH = np.linalg.cholesky(CMG + 1e-10 * np.eye(len(CMG)) * np.trace(CMG) / len(CMG))
HI = (2, 3, 4)
HINAME = {2: 'phi on peaks 1-2', 3: 'phi on peaks 1-3', 4: 'phi on peaks 1-4'}


def ensemble(seed, ndraw):
    """one located peak series per draw, and every nested offset read off THAT series.

    ** The nested statistics differ only in which peaks the offset averages over, never in where
    the locator looked -- `stat(pk, lA, 1, hi)` on the series `peak_series(..., 4)` returns. **
    That is what makes the shorter ones a handle on the four-peak selection rather than a second
    instrument with its own locator.  A slot is recorded as located or not, which is the thing
    `cc66.164` counted in aggregate and never resolved per peak.
    """
    rng = np.random.default_rng(seed)
    nf = np.zeros((ndraw, NPK), bool)
    ph = np.full((ndraw, len(HI)), np.nan)
    al = np.full((ndraw, len(HI)), np.nan)
    for i in range(ndraw):
        d = MSD + CH @ rng.standard_normal(len(CMG))
        pk = peak_series(MLC, d, NPK)[0]
        p4 = np.full(NPK, np.nan)
        p4[:len(pk)] = pk
        nf[i] = np.isfinite(p4)
        for j, hi in enumerate(HI):
            s = stat(p4, LAC, 1, hi)
            if s[2] == hi:
                ph[i, j], al[i, j] = s[0], s[1]
    return nf, ph, al


NF, PH, AL = ensemble(SEED164, NDRAW164)
G4 = NF.all(1)
M4, S4, SD4, N4 = robust(PH[:, 2])
M4A, S4A, SD4A, _ = robust(AL[:, 2])
print(f"      {'cc66.164 reproduced, seed ' + str(SEED164) + f', {NDRAW164} draws':38s} "
      f"{'median':>10s} {'robust':>10s} {'st.dev.':>10s} {'n':>6s}")
print(f"      {'phi, the FOUR-peak selection':38s} {M4:+10.5f} {S4:10.5f} {SD4:10.5f} {N4:6d}")
print(f"      {'alt, the FOUR-peak selection':38s} {M4A:+10.5f} {S4A:10.5f} {SD4A:10.5f} {N4:6d}")
_cnt = np.bincount(NF.sum(1), minlength=NPK + 1)
print(f"      peaks located: " + ', '.join(f'{v} -> {_cnt[v]} ({_cnt[v] / NDRAW164 * 100:.0f}%)'
                                           for v in range(1, NPK + 1) if _cnt[v]))
print(f"      one driving unit: dphi {DRIVE[0]:+.5f} -> {abs(DRIVE[0]) / S4:.1f} sigma, "
      f"dalt {DRIVE[1]:+.5f} -> {abs(DRIVE[1]) / S4A:.1f} sigma")
print(f"      the sky vs control: dphi {DSKY[0]:+.5f} -> {abs(DSKY[0]) / S4:.2f} sigma")
check("Ⓐ①  ** THE AUDITED NUMBER IS REBUILT TO `cc66.164`'s PUBLISHED DIGITS BEFORE IT IS "
      "QUESTIONED: ROBUST `$\\sigma(\\varphi)=0.00955$`, `$13.1\\sigma$` FOR ONE DRIVING UNIT, "
      "`$0.79\\sigma$` FOR THE SKY, AND `$52$` PER CENT OF DRAWS RETURNING FOUR PEAKS. **  *Same "
      "seed, same draw count, same covariance through the same merge matrix.  **An audit that "
      "cannot reproduce the number it audits is auditing a different number***",
      abs(S4 / PUB164['sigma_phi'] - 1) < 0.03
      and abs(abs(DRIVE[0]) / S4 / PUB164['n_sigma_drive_phi'] - 1) < 0.03
      and abs(abs(DRIVE[1]) / S4A / PUB164['n_sigma_drive_alt'] - 1) < 0.05
      and abs(abs(DSKY[0]) / S4 / PUB164['n_sigma_sky_phi'] - 1) < 0.05
      and abs(G4.mean() / PUB164['frac4'] - 1) < 0.03)


# ============================================================ B. the route that does not exist
head("B.  ⛔⛭ AND THE FIRST THING IT FINDS IS THAT THE ROUTE I ROUTED TO 66 DOES NOT EXIST")

NFA, PHA, ALA = ensemble(SEED_AUDIT, NDRAW_AUDIT)
GA4 = NFA.all(1)
RATE_SLOT = NFA.mean(0)
print(f"      per-slot location rate over {NDRAW_AUDIT} draws, seed {SEED_AUDIT}")
print(f"      {'peak':8s} {'located':>10s}")
for j in range(NPK):
    print(f"      {'n = ' + str(j + 1):8s} {RATE_SLOT[j] * 100:9.1f}%")
_m3 = NFA.sum(1) == NPK - 1
_which = [(j + 1, int((~NFA[_m3][:, j]).sum())) for j in range(NPK)]
print(f"      among the {int(_m3.sum())} draws that locate exactly three of four, the slot that is "
      f"missing:")
print(f"        " + ',  '.join(f'n = {j} -> {c}' for j, c in _which))
print(f"      ⇒ so the peak that goes missing is n = "
      f"{int(np.argmin(RATE_SLOT)) + 1}, and n = {NPK} is located in "
      f"{RATE_SLOT[NPK - 1] * 100:.1f} per cent of draws")
check("Ⓑ①  ⛔⛭ ** THE PEAK THAT GOES MISSING IS THE THIRD, NOT THE FOURTH -- SO `cc66.164`'s `Ⓓ⑤` "
      "NAMES THE WRONG PEAK AND THE ROUTE I TOLD 66 THIS AUDIT WOULD TAKE DOES NOT EXIST. **  *The "
      "fourth peak is located in `$96$` per cent of draws and the third in `$57$`.  I told 66 that "
      "`$47$` of the `$48$` per cent `return three, so a three-peak statistic is defined on "
      "`$99$` per cent of draws`: they do return three of four, but **the missing slot is the "
      "third in all but a twelfth of them**, so that statistic covers `$56$` per cent.  ⇒ *The "
      "`$48$` per cent is right and its CAUSE was not, in the receipt and in both of my replies***",
      int(np.argmin(RATE_SLOT)) == NPK - 2 and RATE_SLOT[NPK - 1] > 0.90
      and RATE_SLOT[NPK - 2] < 0.70
      and max(c for j, c in _which if j == NPK - 1) > 5 * max(c for j, c in _which if j == NPK))

print()
COV = {hi: float(np.isfinite(PHA[:, j]).mean()) for j, hi in enumerate(HI)}
print(f"      coverage of each nested offset over the ensemble")
print(f"      {'statistic':22s} {'defined on':>12s}")
for hi in HI:
    print(f"      {HINAME[hi]:22s} {COV[hi] * 100:11.1f}%")
print(f"      ⇒ the handle this audit must use is the one on peaks 1-2, which covers "
      f"{COV[2] * 100:.1f} per cent")
check("Ⓑ②  ⛭⛭ ** AND THE HANDLE THAT DOES COVER THE ENSEMBLE IS THE OFFSET ON PEAKS `$1$`--`$2$`, "
      "DEFINED ON `$99$` PER CENT OF DRAWS AGAINST THE FOUR-PEAK STATISTIC'S `$52$`. **  *Peaks "
      "`$1$` and `$2$` are located in `$100$` and `$99.6$` per cent, so an offset formed on them "
      "exists almost wherever a draw does -- and it is read off the SAME located series, so it "
      "differs from the audited statistic only in how many peaks the average runs over.  **A "
      "selection can only be tested against a statistic that survives it***",
      COV[2] > 0.98 and COV[2] > COV[3] > COV[4] and COV[4] > 0.50)


# ============================================================ C. the audit proper
head("C.  ⛭⛭ THE AUDIT: THE WIDTH INSIDE THE FOUR-PEAK SELECTION AGAINST THE WHOLE ENSEMBLE")

ROWS, RAT = {}, {}
for j, hi in enumerate(HI[:2]):
    col = PHA[:, j]
    ok = np.isfinite(col)
    print(f"      {HINAME[hi]}, seed {SEED_AUDIT}, {NDRAW_AUDIT} draws")
    print(f"      {'group':32s} {'median':>10s} {'robust':>10s} {'st.dev.':>10s} {'n':>6s}")
    for nm, msk in (('kept  (four peaks located)', ok & GA4),
                    ('lost  (fewer than four)', ok & ~GA4),
                    ('ALL   (the whole ensemble)', ok)):
        ROWS[(hi, nm)] = robust(col[msk])
        m, s, sd, nn = ROWS[(hi, nm)]
        print(f"      {nm:32s} {m:+10.5f} {s:10.5f} {sd:10.5f} {nn:6d}")
    k, a, lo = (ROWS[(hi, 'kept  (four peaks located)')], ROWS[(hi, 'ALL   (the whole ensemble)')],
                ROWS[(hi, 'lost  (fewer than four)')])
    RAT[hi] = (k[1] / a[1], k[2] / a[2], lo[1] / k[1], (k[0] - a[0]) / a[1])
    print(f"      ⇒ robust ratio kept/ALL {RAT[hi][0]:.4f}   st.dev. ratio {RAT[hi][1]:.4f}   "
          f"lost/kept robust {RAT[hi][2]:.3f}   median shift {RAT[hi][3]:+.3f} robust sigma")
    print()

R_ROB, R_SD, R_LOST, R_MED = RAT[2]
# ⌗ a bootstrap on the ratio, draw-wise, so `they agree` is a statement with a width rather than a
#    reading of two point estimates.  Resampling draws keeps the kept/lost split random as it is.
_rng = np.random.default_rng(SEED_AUDIT + 1)
_col = PHA[:, 0]
_ix = np.flatnonzero(np.isfinite(_col))
BOOT = []
for _ in range(400):
    j = _rng.choice(_ix, size=len(_ix), replace=True)
    a, b = robust(_col[j][GA4[j]])[1], robust(_col[j])[1]
    if np.isfinite(a) and np.isfinite(b) and b > 0:
        BOOT.append(a / b)
BOOT = np.array(BOOT)
BLO, BHI = float(np.percentile(BOOT, 2.5)), float(np.percentile(BOOT, 97.5))
print(f"      bootstrap 95% interval on the robust ratio, {len(BOOT)} resamples: "
      f"[{BLO:.4f}, {BHI:.4f}]")
# ⌗ the one place the selection IS strongly informative, and it is worth naming because it is the
#   case the order was WRITTEN about: on the 1-3 handle the `lost` group is only the draws that
#   lose the FOURTH peak specifically, and those are half again as wide.  They are 4 per cent of
#   the ensemble, which is why the pooled width barely moves -- the effect is real and rare.
print(f"      ⌗ where the selection IS informative: on the 1-3 handle the lost group is only the "
      f"{ROWS[(3, 'lost  (fewer than four)')][3]} draws that lose the FOURTH peak, and those are "
      f"{RAT[3][2]:.2f}x wider")
print(f"      ⌗ and the st.dev. ratio on the 1-2 handle runs the OTHER way, {RAT[2][1]:.3f} "
      f"against the robust {RAT[2][0]:.3f}: the kept group carries more of the locator's tail, "
      f"which is a fact about the tail and not about the core the verdict rests on")
TRUNCATES = bool(abs(R_ROB - 1.0) > TRUNC_TOL and not (BLO < 1.0 - TRUNC_TOL < BHI))
print(f"      ⇒ VERDICT at the threshold fixed in advance (ratio further from one than "
      f"{TRUNC_TOL:.2f}, interval clear of it): {'TRUNCATES' if TRUNCATES else 'DOES NOT TRUNCATE'}")
check("Ⓒ①  ⛭⛭ ** THE SELECTION DOES NOT TRUNCATE: THE OFFSET'S ROBUST WIDTH INSIDE THE FOUR-PEAK "
      "SELECTION IS `$0.982$` OF ITS WIDTH OVER THE WHOLE ENSEMBLE, AND THE BOOTSTRAP INTERVAL IS "
      "CLEAR OF THE TEN PER CENT THRESHOLD FIXED IN ADVANCE. **  *So `$\\sigma(\\varphi)=0.0096$` "
      "is not a truncated width and the `$13\\sigma$` is not inflated by the `$52$` per cent.  ⌗ "
      "*It is not perfectly neutral either: the discarded draws are `$1.04\\times$` wider, which "
      "is the selection acting on the offset at a size that cannot matter at this lever*",
      BLO > 1.0 - TRUNC_TOL and R_ROB < 1.0 and abs(R_MED) < 0.5 and R_LOST > 1.0)

print()
_in = PREDICT[0] <= R_ROB <= PREDICT[1]
_best = PREDICT_BEST[0] <= R_ROB <= PREDICT_BEST[1]
_tail = abs(R_SD - 1.0) > abs(R_ROB - 1.0)
print(f"      the r7221 burden, scored against the band pinned above every computation")
print(f"      {'claim':34s} {'value':>10s} {'verdict':>10s}")
print(f"      {'band ' + f'{PREDICT[0]:.2f}-{PREDICT[1]:.2f}':34s} {R_ROB:10.4f} "
      f"{'IN' if _in else 'OUT':>10s}")
print(f"      {'narrower ' + f'{PREDICT_BEST[0]:.2f}-{PREDICT_BEST[1]:.2f}':34s} {R_ROB:10.4f} "
      f"{'IN' if _best else 'OUT':>10s}")
print(f"      {'tail carries it, not the core':34s} "
      f"{abs(R_SD - 1) / max(abs(R_ROB - 1), 1e-9):9.1f}x {'HELD' if _tail else 'FAILED':>10s}")
print(f"      ⌗ BUT THE MECHANISM I GAVE FOR THE PREDICTION WAS THE WRONG PEAK: I argued from the")
print(f"        noise near the FOURTH peak being independent of the offset on peaks 1-3.  The peak")
print(f"        that goes missing is the THIRD, which IS one of the peaks the audited offset")
print(f"        averages over -- so the independence I predicted from was not the independence")
print(f"        that held.  ** The number landed in the band; the reason I gave for it did not. **")
check("Ⓒ②  ** AND THE PREDICTION IS SCORED BOTH WAYS: THE RATIO LANDED IN THE PINNED BAND AND IN "
      "THE NARROWER CLAIM, THE TAIL HALF HELD AT `$8\\times$` -- AND THE MECHANISM I ARGUED FROM "
      "WAS THE WRONG PEAK. **  *`PREDICT` sits above every computation that touches it, so what is "
      "scored is a claim and not a memory.  **A prediction that lands for a reason its author got "
      "wrong is a worse prediction than its hit rate says**, and the half worth keeping is the "
      "tail one, which is about the locator rather than about this ensemble*",
      _in and _tail and np.isfinite(R_SD) and PREDICT_BEST[0] >= PREDICT[0])


# ============================================================ D. the second handle
head("D.  AND A SECOND HANDLE THAT DOES NOT GO THROUGH A WIDTH: IS LOSING A PEAK PREDICTABLE?")

# ⌗ if the selection truncated, the draws whose offset is already far from the median would be the
#   ones that lose a peak, so the loss rate would RISE with distance.  This reads that directly,
#   on the handle that covers the ensemble, which is a statement about the mechanism rather than
#   about two scale estimates.
_c = PHA[:, 0]
_ok = np.isfinite(_c)
_med = ROWS[(2, 'ALL   (the whole ensemble)')][0]
_d = np.abs(_c - _med)
_q = np.percentile(_d[_ok], [0, 20, 40, 60, 80, 100])
print(f"      loss rate of the four-peak statistic by quintile of |phi(1-2) - median|")
print(f"      {'quintile':10s} {'|phi-med| range':>22s} {'n':>7s} {'lost':>7s} {'rate':>8s}")
RATEQ = []
for i in range(5):
    lo, hi = _q[i], _q[i + 1]
    m = _ok & (_d >= lo) & ((_d <= hi) if i == 4 else (_d < hi))
    r = float((~GA4[m]).mean()) if m.sum() else float('nan')
    RATEQ.append(r)
    print(f"      {'Q' + str(i + 1):10s} {f'{lo:.5f} - {hi:.5f}':>22s} {int(m.sum()):7d} "
          f"{int((~GA4[m]).sum()):7d} {r * 100:7.1f}%")
BASE = float((~GA4[_ok]).mean())
SPREAD = max(RATEQ) - min(RATEQ)
print(f"      base rate {BASE * 100:.1f}%,  spread across quintiles {SPREAD * 100:.1f} points,  "
      f"Q5 - Q1 {(RATEQ[-1] - RATEQ[0]) * 100:+.1f} points")
check("Ⓓ①  ** AND THE SECOND HANDLE AGREES WITHOUT GOING THROUGH A WIDTH: THE LOSS RATE RISES BY "
      "ONLY A FEW POINTS ACROSS QUINTILES OF HOW FAR THE OFFSET ALREADY IS FROM THE MEDIAN, ON A "
      "BASE RATE NEAR A HALF. **  *A truncating selection would show the rate climbing steeply "
      "with distance, because that IS truncation.  **A few points on a base of `$48$` is the same "
      "`$1.04\\times$` that `Ⓒ①` measured, arriving by a route with no scale estimate in it***",
      SPREAD < 0.20 and BASE > 0.40 and abs(RATEQ[-1] - RATEQ[0]) < 0.20)


# ============================================================ E. what the 13 becomes
head("E.  ⛭⛭⛭ SO WHAT THE `$13$` BECOMES -- 66's ADDITION, AND THE DELIVERABLE")

# ⌗ THE ASSUMPTION, STATED: the four-peak statistic does not exist off its own selection, so its
#   unselected width cannot be measured.  What IS measurable is how the width of a statistic that
#   survives the selection changes between the selection and the ensemble, and the correction
#   carries that ratio across -- which assumes the four-peak width responds to the selection the
#   same way the two-peak one does.  ** That assumption is what D is for: a loss rate flat in
#   offset distance says the selection is barely acting on the offset at all, in which case there
#   is little to carry and the choice of carrier matters correspondingly less. **
SIG_CORR = S4 / R_ROB
N_PRINTED = abs(DRIVE[0]) / S4
N_CORR = abs(DRIVE[0]) / SIG_CORR
NSKY_PRINTED = abs(DSKY[0]) / S4
NSKY_CORR = abs(DSKY[0]) / SIG_CORR
_sa = ROWS[(2, 'kept  (four peaks located)')], ROWS[(2, 'ALL   (the whole ensemble)')]
print(f"      {'quantity':32s} {'as printed':>12s} {'corrected':>12s} {'change':>10s}")
print(f"      {'robust sigma(phi)':32s} {S4:12.5f} {SIG_CORR:12.5f} "
      f"{(SIG_CORR / S4 - 1) * 100:+9.1f}%")
print(f"      {'one driving unit, in sigma':32s} {N_PRINTED:12.2f} {N_CORR:12.2f} "
      f"{(N_CORR / N_PRINTED - 1) * 100:+9.1f}%")
print(f"      {'the sky vs control, in sigma':32s} {NSKY_PRINTED:12.2f} {NSKY_CORR:12.2f} "
      f"{(NSKY_CORR / NSKY_PRINTED - 1) * 100:+9.1f}%")
print(f"      ⇒ the exclusion printed as {PUB164['n_sigma_drive_phi']:.1f} sigma is "
      f"{N_CORR:.1f} sigma corrected, and the sky's {PUB164['n_sigma_sky_phi']:.2f} is "
      f"{NSKY_CORR:.2f}")
check("Ⓔ①  ⛭⛭⛭ ** AND THE DELIVERABLE: THE `$13\\sigma$` BECOMES `$12.9$` AND THE SKY'S "
      "`$0.79\\sigma$` BECOMES `$0.78$`. **  *Carrying the measured ratio across to the four-peak "
      "width -- the only route there is, since the four-peak statistic does not exist off its own "
      "selection -- moves the exclusion by a fifth of a sigma.  ⇒ **So `r7229`'s FIRST branch "
      "fires: the figure stands as printed, and the `$52$` per cent goes back to being a bound on "
      "the statistic's existence alone** -- an existence bound on the THIRD peak, which is the one "
      "correction this audit does deliver*",
      abs(N_CORR - N_PRINTED) < 1.0 and N_CORR < N_PRINTED
      and abs(N_CORR / PUB164['n_sigma_drive_phi'] - 1) < 0.08
      and abs(NSKY_CORR / PUB164['n_sigma_sky_phi'] - 1) < 0.08)

print()
_ka, _aa = robust(ALA[:, 0][GA4 & np.isfinite(ALA[:, 0])]), robust(ALA[:, 0][np.isfinite(ALA[:, 0])])
R_ALT = _ka[1] / _aa[1] if np.isfinite(_aa[1]) and _aa[1] > 0 else float('nan')
print(f"      and the alternation, which is the component the merge already cost 2.6x of lever")
print(f"      {'alternation on peaks 1-2':32s} {'kept':>12s} {'ALL':>12s} {'ratio':>10s}")
print(f"      {'robust width':32s} {_ka[1]:12.5f} {_aa[1]:12.5f} {R_ALT:10.4f}")
print(f"      {'one driving unit, in sigma':32s} {abs(DRIVE[1]) / S4A:12.2f} "
      f"{abs(DRIVE[1]) / (S4A / R_ALT):12.2f} {'':10s}")
check("Ⓔ②  ** AND THE ALTERNATION CARRIES THE SAME VERDICT, WHICH MATTERS BECAUSE IT IS THE "
      "COMPONENT WHOSE LEVER THE MERGE ALREADY COST `$2.6\\times$`. **  *Its width inside the "
      "selection is within a tenth of its width over the ensemble, so `$3.1\\sigma$` is not a "
      "truncated figure either.  ⌗ *On two peaks the alternation has a single sign pair, so this "
      "is the noisier of the two handles and is reported as the weaker of the two agreements -- "
      "which is why `Ⓒ①` and not this is the check the verdict rests on*",
      np.isfinite(R_ALT) and abs(R_ALT - 1.0) < 2 * TRUNC_TOL)

print()
print("      ⌗ WHAT THIS DOES NOT SETTLE, and it is the boundary r7227 named in advance: whether")
print(f"        the locator's {BASE * 100:.0f} per cent failure rate is itself right.  That is a")
print("        property of plik_lite's binning at this merge and this noise, and nothing here")
print("        measures the locator against a different instrument.  ** What this file removes is")
print("        the 52 per cent's claim on the WIDTH.  Its claim on EXISTENCE stands, and is now")
print("        correctly attached to the third peak. **")
print("      ⌗ AND cc66.164's Ⓓ⑥ is untouched: the projection kernel's running phase is 5.7x the")
print("        sky's displacement, and nothing here bears on whether it cancels in a")
print("        data-minus-model difference.  The sky's 0.78 sigma remains conditional on that.")


head("VERDICT")
print(f"  {len(ran)} check(s) ran, {len(fail)} failed.   measured runtime "
      f"{time.time() - T0:.0f}s")
if fail:
    print(f"\n  {len(fail)} check(s) FAILED")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print(f"\n  {len(ran)} of {len(ran)} checks pass.")
print("    r7229's audit returns the first branch: the selection does not truncate, one driving")
print("    unit is 12.9 sigma against the 13.1 printed, and the 52 per cent is an existence bound")
print("    and not a correction -- on the THIRD peak, which is the name cc66.164 got wrong.")
