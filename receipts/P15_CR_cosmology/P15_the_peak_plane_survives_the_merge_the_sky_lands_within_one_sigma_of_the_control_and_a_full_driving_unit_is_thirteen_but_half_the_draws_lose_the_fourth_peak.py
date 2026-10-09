#!/usr/bin/env python3
r"""
RECEIPT -- P15: ** `r7223` ORDERED THE INSTRUMENT THE COMB WAS A SUBSTITUTE FOR -- `form
(phi, alt) on the pair-merged bank and place the sky on the peak plane` -- WITH MY OWN BURDEN
ADOPTED VERBATIM AND ONE ADDITION OF 66's.  *** THE BURDEN IS MET, THE PLANE SURVIVES THE MERGE,
THE SKY LANDS `$0.8\sigma$` FROM THE CONTROL WITH A FULL DRIVING UNIT AT `$13\sigma$` -- AND HALF
OF ALL NOISE REALISATIONS LOSE THE FOURTH PEAK. *** **

  ⓵ ** THE BURDEN: THE MERGED MODEL REPRODUCES THE BANKED PAIR. **  *At matched peak count the
  driving difference on the pair-merged bank is `$+0.12703$`/`$-0.02494$` against the banked
  `$+0.126$`/`$-0.0247$` -- `$1.008\times$` and `$1.010\times$`.  **So the merge costs under one
  per cent on both components and the closure branch `r7223` named does not fire.***

  ⓶ ⛭ ** AND THE FOUR-PEAK RESTRICTION IS A SEPARATE EFFECT, MEASURED SEPARATELY. **  *On four
  peaks the common offset holds to `$0.1$` per cent and the alternation reads `$1.216\times$`
  banked -- and the SAME `$1.20\times$` appears on the instrument's raw samples, so **it is the
  peak count and not the merge.**  ⌈ *The two balanced four-peak windows straddle the five-peak
  value -- peaks `$1$`--`$4$` give `$1.216\times$`, peaks `$2$`--`$5$` give `$0.913\times$` -- so
  the four-peak alternation is window-dependent at `$\pm15$` per cent and neither window is the
  truth.*

  ⓷ ** 66's ADDITION, AND IT DOES NOT COLLAPSE. **  *The separation of the baryon direction from a
  pure tilt, re-measured on four peaks of the merged bank: `$12.0\times$` on the common offset and
  `$8.2\times$` on the alternation, against `cc66.155`'s free-period slope at `$1.3\times$`.
  **The plane survives.**  ⌗ *But the alternation's lever is down `$2.6\times$` from `cc66.156`'s
  `$21.4$`, and the cause is measured rather than guessed: `$n_s$`'s residual leakage onto the
  alternation grows FOUR-FOLD at four peaks, `$-0.00049\to-0.00203$`.  The de-tilt control is
  weaker on four peaks, which is the price of the merge stated in the units it is paid in.*

  ⓸ ⛭⛭⛭ ** THE SKY IS ON THE PLANE. **  *`$(\varphi,\mathrm{alt})=(-0.18571,+0.00804)$` against
  the control's `$(-0.19328,+0.01059)$` through the identical merge, so
  `$(\Delta\varphi,\Delta\mathrm{alt})=(+0.00756,-0.00255)$` and the discriminant is `$0.337$` --
  between the driving's `$0.237$` and the loading's `$1.320$`, which the plane still separates by
  `$5.6\times$` in this statistic.*

  ⓹ ** AND THE ERROR IS PROPAGATED EXACTLY, BECAUSE THE MERGE IS LINEAR. **  *`plik_lite`'s own
  covariance through the merge matrix, `$2000$` draws: the distribution is HEAVY-TAILED -- a
  standard deviation of `$0.107$` against a robust `$0.0096$` -- so the robust scale is what is
  quoted and the tail is reported as what it is.  ⇒ **One full driving unit is `$13.1\sigma$` on
  the offset and `$3.1\sigma$` on the alternation; the sky sits `$0.79\sigma$` and `$0.27\sigma$`
  from the control.**  *So the sky is consistent with the control's own driving and a full unit of
  difference either way is excluded.*

  ⓺ ⛔ ** AND WHAT BOUNDS IT IS NOT THE WIDTH BUT THE EXISTENCE: `$48$` PER CENT OF DRAWS DO NOT
  RETURN FOUR PEAKS. **  *`$47$` per cent return three.  The merge is at the locator's own
  resolution limit -- one further step returns nothing on the sky OR the model -- so the statistic
  is defined on about half of the realisations of this sky, and the robust `$\sigma$` is
  conditional on its being defined at all.*  ⌗ *And the other limit is the assumed scale:
  `$\ell_A$` at `$+1$` per cent moves the sky's offset by `$2.4$` robust `$\sigma$`, so the
  `$0.8\sigma$` agreement requires the sky's acoustic scale to be the control's to `$0.4$` per
  cent and the `$13\sigma$` exclusion requires `$5$`.*

  ⓻ ⚠⛔ ** AND ONE SYSTEMATIC THIS FILE CANNOT BOUND IS LARGER THAN ITS RESULT. **  *`r7225` flags
  it in advance, and the reading here IS differential -- sky MINUS control through the identical
  merge -- so `60`'s identity makes the projection kernel's phase common mode between the two
  ARMS.  **But a data-minus-model difference is not an arm-minus-control difference**: the kernel's
  own running phase is `$0.0429$` of a comb period against the `$+0.00756$` measured here,
  `$5.7\times$` it, so `$0.79\sigma$` is conditional on a cancellation this file does not
  establish.  *The `$13\sigma$` scale of one driving unit is model-against-model and unaffected.*

** COMPUTES: `cc66.156`'s de-tilted peak statistic, unchanged and pinned to its published
   `$11.3$`/`$21.4$`; `cc66.163`'s width-weighted pair merge of `plik_lite`'s TT bins, pinned to
   its published located gaps; the driving difference through the merge at five and at four peaks
   and on raw samples, to separate the merge from the peak count; the tilt separation re-measured
   on four peaks, both arms and both grids; the sky's point and the three carrier directions in
   that one statistic; and `plik_lite`'s covariance carried through the merge exactly and through
   the locator by Monte Carlo.  *** No new spectrum, no fit, no refit. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; 3s MEASURED)
"""
import os
import sys

import numpy as np

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
GL = os.path.join(BW, 'r7095_directions', 'grid_licensed')
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
SPC = os.path.join(BW, 'spectra')
for _p in (GO, GL, LEV, SPC):
    if not os.path.isdir(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

# ⌗ cc66.156's constants, unchanged: the window, the banked step sizes and the base values the
#   logarithmic derivatives are taken at.  NPK is a PARAMETER here rather than a constant, which
#   is the whole of what `r7223`'s `four peaks and not five` requires.
LMIN, LMAX = 150.0, 1600.0
BASEVAL = {'H0': {'cr': 68.60, 'lcdm': 67.40}, 'OM': {'cr': 0.2973, 'lcdm': 0.3150},
           'NS': {'cr': 0.965, 'lcdm': 0.965}, 'WB': {'cr': 0.0224, 'lcdm': 0.0224}}
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}
LC, FACB = CS.bin_center_and_fac()
WID = (CS.BIN_HI - CS.BIN_LO + 1).astype(float)
BANKED = (0.126, -0.0247)          # cc66.156's driving pair, the burden r7223 adopted
PUB156 = (11.3, 21.4, 11.4, 22.6)  # its published separation factors, arm then control
SLOPE = 1.3                        # cc66.155's free-period slope, the thing to beat
GMERGE = 2                         # cc66.163's factor of two, the whole usable range
# ⌗ CITED AND NOT RECOMPUTED, read from `60`'s own `r7236` receipt, which reached `main` while
#    this was being written: the projection kernel's ABSOLUTE running phase is `-15.45 deg`, 16.0
#    per cent of the residual's `-96.6 deg`, `present in ANY spectrum this instrument projects,
#    the control's included, agreeing between the arms to 0.09 per cent`.  Only the percentage is
#    taken on trust; the conversion into this statistic's units and the comparison with the
#    measured displacement are done here.  ⌗ `66`'s `r7225` relays the phase as `-15.46`; `60`'s
#    receipt prints `-15.45`.  The figure used is `60`'s own and the difference changes nothing.
KERN_FRAC = 0.160                  # 60's r7236 -- an input, not a measurement here
RESID_DEG = -96.6                  # the residual's phase drift, the paper's own figure


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
    """cc66.156's locator, on whatever samples it is handed -- raw, binned or merged."""
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


def deriv(gdir, arm, par, **kw):
    """d(phi)/dln(theta), d(alt)/dln(theta) by central difference on the banked pair."""
    sm = phi_alt(os.path.join(gdir, f'{arm}_{par}m.npz'), **kw)
    sp = phi_alt(os.path.join(gdir, f'{arm}_{par}p.npz'), **kw)
    gg = BASEVAL[par][arm] / (2 * STEP[par])
    return (sp[0] - sm[0]) * gg, (sp[1] - sm[1]) * gg


L3ON, L3OFF = (os.path.join(SPC, 'c54.186_lcdm_L3000.npz'),
               os.path.join(SPC, 'c54.193_lcdm_nodrive_L3000.npz'))
SVON, SVOFF = os.path.join(GO, 'lcdm_base.npz'), os.path.join(LEV, 'lcdm_nodrive.npz')
CRON, CROFF = os.path.join(GO, 'cr_base.npz'), os.path.join(LEV, 'cr_nodrive.npz')


# ============================================================ A. the two instruments, pinned
head("A.  BOTH INSTRUMENTS ARE PINNED TO THEIR PUBLISHED DIGITS BEFORE EITHER IS POINTED ANYWHERE")

_l3 = (phi_alt(L3OFF)[0] - phi_alt(L3ON)[0], phi_alt(L3OFF)[1] - phi_alt(L3ON)[1])
_sv = (phi_alt(SVOFF)[0] - phi_alt(SVON)[0], phi_alt(SVOFF)[1] - phi_alt(SVON)[1])
print(f"      {'driving pair, raw samples, 5 peaks':40s} {'dphi':>9s} {'dalt':>9s}")
print(f"      {'cc66.156 L3000 lcdm (the banked pair)':40s} {_l3[0]:+9.5f} {_l3[1]:+9.5f}")
print(f"      {'cc66.158 same-vintage lcdm':40s} {_sv[0]:+9.5f} {_sv[1]:+9.5f}")
print(f"      {'banked, as cc66.156 published it':40s} {BANKED[0]:+9.5f} {BANKED[1]:+9.5f}")
check("Ⓐ①  ** `cc66.156`'s STATISTIC COMES BACK TO ITS PUBLISHED `$+0.126$`/`$-0.0247$` ON BOTH "
      "DRIVING PAIRS. **  *`$+0.12649$`/`$-0.02469$` on the banked `L3000` pair and "
      "`$+0.12651$`/`$-0.02469$` on `cc66.158`'s same-vintage one, which is also `cc66.158`'s own "
      "`Ⓑ①` reproduced.  **The burden below compares against a number this file has shown it can "
      "measure, not against one it is told***",
      abs(_l3[0] / BANKED[0] - 1) < 0.01 and abs(_l3[1] / BANKED[1] - 1) < 0.01
      and abs(_sv[0] / BANKED[0] - 1) < 0.01 and abs(_sv[1] / BANKED[1] - 1) < 0.01)

print()
print(f"      {'the separation factors on raw samples, 5 peaks':48s} {'WB:NS phi':>10s} "
      f"{'WB:NS alt':>10s}")
RAW5 = {}
for arm in ('cr', 'lcdm'):
    w, nsd = deriv(GO, arm, 'WB'), deriv(GO, arm, 'NS')
    RAW5[arm] = (abs(w[0] / nsd[0]), abs(w[1] / nsd[1]))
    print(f"      {'oneclock ' + arm:48s} {RAW5[arm][0]:9.1f}x {RAW5[arm][1]:9.1f}x")
print(f"      {'cc66.156 published':48s} {PUB156[0]:9.1f}x {PUB156[1]:9.1f}x   (arm)")
print(f"      {'':48s} {PUB156[2]:9.1f}x {PUB156[3]:9.1f}x   (control)")
check("Ⓐ②  ** AND ITS PUBLISHED SEPARATION FACTORS COME BACK TO THE TENTH: `$11.3\\times$` AND "
      "`$21.4\\times$` ON THE ARM, `$11.4\\times$` AND `$22.6\\times$` ON THE CONTROL. **  *These "
      "are the four numbers `r7223` asks to have re-measured on four peaks, so they are "
      "reproduced at five first -- a re-measurement against a figure this file cannot reproduce "
      "would measure the reimplementation*",
      abs(RAW5['cr'][0] - PUB156[0]) < 0.1 and abs(RAW5['cr'][1] - PUB156[1]) < 0.1
      and abs(RAW5['lcdm'][0] - PUB156[2]) < 0.1 and abs(RAW5['lcdm'][1] - PUB156[3]) < 0.1)

print()
_lb, _db, _lA, MASK = binned(CRON)
_sl, _sd = sky(MASK)
_wid = WID[MASK]
print(f"      {'merge':>7s} {'sky peaks':>10s} {'sky gaps':>22s} {'model peaks':>12s} "
      f"{'model gaps':>26s} {'max|d|':>7s}")
REB = {}
for g in (1, 2, 3):
    ml, md = merge(_sl, _sd, g, _wid)
    mm, mdm = merge(_lb, _db, g, _wid)
    ps = peak_series(ml, md, 5)[0]
    pm = peak_series(mm, mdm, 5)[0]
    ps, pm = ps[np.isfinite(ps)], pm[np.isfinite(pm)]
    nn = min(len(ps), len(pm))
    off = float(np.max(np.abs(ps[:nn] - pm[:nn]))) if nn else float('nan')
    REB[g] = (len(ps), len(pm), off, [int(q) for q in np.diff(ps)], [int(q) for q in np.diff(pm)])
    print(f"      {g:7d} {len(ps):10d} {str(REB[g][3]):>22s} {len(pm):12d} {str(REB[g][4]):>26s} "
          f"{(f'{off:7.2f}' if nn else '     --')}")
check("Ⓐ③  ** AND `cc66.163`'s MERGE COMES BACK TO ITS PUBLISHED LOCATOR RESULT: GAPS "
      "`$303$`/`$268$`/`$309$` AGAINST THE MODEL'S `$302$`/`$269$`/`$312$` AT `$g=2$`, `$3.37$` "
      "WORST, AGAINST `$547$` AT THE BANK'S NATIVE BINNING -- AND NOTHING AT ALL ON EITHER AT "
      "`$g=3$`. **  *So the bank this statistic is about to be pointed at is the one `main` already "
      "carries, and the factor of two is the whole usable range for the reason `cc66.163` gave: the "
      "locator's own `$\\pm40$` window*",
      REB[2][0] == 4 and REB[2][2] < 5.0 and REB[1][2] > 100.0
      and REB[3][0] == 0 and REB[3][1] == 0 and REB[2][3] == [303, 268, 309])


# ============================================================ B. the burden
head("B.  THE BURDEN r7223 ADOPTED VERBATIM -- AND THE MERGE SEPARATED FROM THE PEAK COUNT")

print(f"      {'pair':20s} {'samples':10s} {'npk':>4s} {'dphi':>9s} {'dalt':>9s} "
      f"{'phi/banked':>11s} {'alt/banked':>11s}")
BUR = {}
for name, (on, off) in (('L3000 lcdm', (L3ON, L3OFF)), ('same-vintage lcdm', (SVON, SVOFF)),
                        ('same-vintage cr', (CRON, CROFF))):
    for lab, kw in (('raw', dict(on_bank=False)),
                    ('bank g=1', dict(on_bank=True, g=1)),
                    ('merged g=2', dict(on_bank=True, g=GMERGE))):
        for npk in (5, 4):
            a, b = phi_alt(on, npk=npk, **kw), phi_alt(off, npk=npk, **kw)
            dp, da = b[0] - a[0], b[1] - a[1]
            BUR[(name, lab, npk)] = (dp, da)
            print(f"      {name:20s} {lab:10s} {npk:4d} {dp:+9.5f} {da:+9.5f} "
                  f"{dp / BANKED[0]:10.3f}x {da / BANKED[1]:10.3f}x")
    print()
_m5 = BUR[('same-vintage lcdm', 'merged g=2', 5)]
check("Ⓑ①  ⛭⛭⛭ ** THE BURDEN IS MET: THE MERGED MODEL REPRODUCES THE BANKED PAIR TO BETTER THAN "
      "ONE PER CENT ON BOTH COMPONENTS AT MATCHED PEAK COUNT -- `$+0.12703$`/`$-0.02494$` against "
      "`$+0.126$`/`$-0.0247$`. **  *`r7223`: `the merged MODEL must reproduce the banked "
      "+0.126/-0.0247 before the sky's position on the plane means anything`.  **It does, on both "
      "driving pairs and on both arms, so the closure branch -- `the peak plane does not survive "
      "the merge` -- does NOT fire.***",
      all(abs(BUR[(nm, 'merged g=2', 5)][0] / BANKED[0] - 1) < 0.01
          and abs(BUR[(nm, 'merged g=2', 5)][1] / BANKED[1] - 1) < 0.02
          for nm in ('L3000 lcdm', 'same-vintage lcdm', 'same-vintage cr')))

_r4 = BUR[('same-vintage lcdm', 'raw', 4)]
_m4 = BUR[('same-vintage lcdm', 'merged g=2', 4)]
print(f"      ⇒ the merge alone, at fixed peak count: alt "
      f"{BUR[('same-vintage lcdm', 'bank g=1', 5)][1] / BANKED[1]:.3f}x -> "
      f"{_m5[1] / BANKED[1]:.3f}x")
print(f"      ⇒ the peak count alone, at fixed sampling: alt "
      f"{BUR[('same-vintage lcdm', 'raw', 5)][1] / BANKED[1]:.3f}x -> {_r4[1] / BANKED[1]:.3f}x "
      f"on RAW samples, and {_m5[1] / BANKED[1]:.3f}x -> {_m4[1] / BANKED[1]:.3f}x on the merge")
check("Ⓑ②  ** AND THE FOUR-PEAK SHIFT IS THE PEAK COUNT AND NOT THE MERGE, WHICH THE 2x2 SHOWS "
      "RATHER THAN ARGUES: `$1.20\\times$` ON THE INSTRUMENT'S RAW SAMPLES AND `$1.22\\times$` ON "
      "THE MERGED BANK, WHILE THE MERGE AT FIXED PEAK COUNT MOVES IT BY `$2.6$` PER CENT. **  *The "
      "common offset holds to a tenth of a per cent throughout.  **So dropping the fifth peak "
      "redefines the alternation by a fifth, and it would have done so on any bank** -- which "
      "matters because it is the four-peak statistic the sky can be read with*",
      abs(_r4[1] / BANKED[1] - 1.20) < 0.03 and abs(_m4[1] / BANKED[1] - 1.22) < 0.03
      and abs(_m4[0] / BANKED[0] - 1) < 0.01)

print()
print(f"      {'peaks used':12s} {'sign pattern':14s} {'dphi':>9s} {'dalt':>9s} {'alt/banked':>11s}")
SUB = {}
for lo, hi in ((1, 5), (1, 4), (2, 5)):
    a = phi_alt(SVON, npk=5, on_bank=True, g=GMERGE, lo=lo, hi=hi)
    b = phi_alt(SVOFF, npk=5, on_bank=True, g=GMERGE, lo=lo, hi=hi)
    SUB[(lo, hi)] = (b[0] - a[0], b[1] - a[1])
    sg = ''.join('-+'[i % 2] for i in range(lo, hi + 1))
    print(f"      {f'{lo}..{hi}':12s} {sg:14s} {SUB[(lo, hi)][0]:+9.5f} {SUB[(lo, hi)][1]:+9.5f} "
          f"{SUB[(lo, hi)][1] / BANKED[1]:10.3f}x")
check("Ⓑ③  ⚠ ** AND THE FOUR-PEAK ALTERNATION IS WINDOW-DEPENDENT AT `$\\pm15$` PER CENT: PEAKS "
      "`$1$`--`$4$` GIVE `$1.216\\times$` BANKED AND PEAKS `$2$`--`$5$` GIVE `$0.913\\times$`, "
      "STRADDLING THE FIVE-PEAK VALUE. **  *I expected the four-peak window to be the CLEANER one "
      "-- its sign pattern is balanced where five peaks' is not -- and that is wrong: the two "
      "balanced windows disagree with each other by a third of the signal.  **Neither four-peak "
      "window is the truth and the five-peak value is not an outlier**, which is the honest shape "
      "of what `r7223`'s `a statistic that loses a peak loses some of its lever` costs*",
      abs(SUB[(1, 4)][1] / BANKED[1] - 1.216) < 0.02
      and abs(SUB[(2, 5)][1] / BANKED[1] - 0.913) < 0.02
      and min(SUB[(1, 4)][1], SUB[(2, 5)][1]) < SUB[(1, 5)][1] < max(SUB[(1, 4)][1], SUB[(2, 5)][1]))


# ============================================================ C. 66's addition
head("C.  66's ADDITION: THE SEPARATION FACTORS RE-MEASURED ON FOUR PEAKS OF THE MERGED BANK")

print(f"      {'samples':10s} {'npk':>3s} {'grid':9s} {'arm':5s} {'dphi/dlnWB':>11s} "
      f"{'dphi/dlnNS':>11s} {'WB:NS phi':>10s} {'dalt/dlnWB':>11s} {'dalt/dlnNS':>11s} "
      f"{'WB:NS alt':>10s}")
SEP = {}
for lab, kw in (('raw', dict(on_bank=False)), ('merged', dict(on_bank=True, g=GMERGE))):
    for npk in (5, 4):
        for gname, gdir in (('oneclock', GO), ('licensed', GL)):
            for arm in ('cr', 'lcdm'):
                w, nsd = deriv(gdir, arm, 'WB', npk=npk, **kw), deriv(gdir, arm, 'NS', npk=npk, **kw)
                SEP[(lab, npk, gname, arm)] = (w, nsd, abs(w[0] / nsd[0]), abs(w[1] / nsd[1]))
                s = SEP[(lab, npk, gname, arm)]
                print(f"      {lab:10s} {npk:3d} {gname:9s} {arm:5s} {w[0]:+11.5f} {nsd[0]:+11.5f} "
                      f"{s[2]:9.1f}x {w[1]:+11.5f} {nsd[1]:+11.5f} {s[3]:9.1f}x")
        print()
_f4 = [SEP[('merged', 4, g, a)] for g in ('oneclock', 'licensed') for a in ('cr', 'lcdm')]
print(f"      ⇒ merged, four peaks: WB:NS is {min(s[2] for s in _f4):.1f}-"
      f"{max(s[2] for s in _f4):.1f}x on the offset and {min(s[3] for s in _f4):.1f}-"
      f"{max(s[3] for s in _f4):.1f}x on the alternation, against {SLOPE} for the free-period slope")
check("Ⓒ①  ⛭⛭⛭ ** THE SEPARATION DOES NOT COLLAPSE: ON FOUR PEAKS OF THE MERGED BANK THE BARYON "
      "DIRECTION IS STILL `$9.8$`--`$12.1\\times$` A PURE TILT ON THE COMMON OFFSET AND "
      "`$8.2$`--`$9.9\\times$` ON THE ALTERNATION, AGAINST `$1.3\\times$` FOR THE SLOPE. **  "
      "*`r7223` named the branch -- `if the four-peak separation collapses to the slope's 1.3, the "
      "merge has bought the sky at the cost of the thing the plane was for` -- and it does not "
      "fire: the worst number in the configuration the sky is actually read in is `$8.2\\times$`, "
      "still most of an order of magnitude above the statistic this row discarded*",
      all(s[2] > 6.0 and s[3] > 6.0 for s in _f4)
      and min(s[3] for s in _f4) / SLOPE > 5.0)

_a5 = SEP[('raw', 5, 'oneclock', 'cr')]
_a4 = SEP[('merged', 4, 'oneclock', 'cr')]
print(f"      and where the alternation's lever went: n_s's residual leakage onto it goes "
      f"{_a5[1][1]:+.5f} -> {_a4[1][1]:+.5f}, a factor of {abs(_a4[1][1] / _a5[1][1]):.1f}")
print(f"      while the baryon direction's own alternation response goes {_a5[0][1]:+.5f} -> "
      f"{_a4[0][1]:+.5f}, a factor of {abs(_a4[0][1] / _a5[0][1]):.2f}")
check("Ⓒ②  ⛔ ** AND THE ALTERNATION'S LEVER IS DOWN `$2.6\\times$` FROM `cc66.156`'s `$21.4$`, FOR "
      "A REASON THAT IS MEASURED AND NOT GUESSED: `$n_s$`'s RESIDUAL LEAKAGE ONTO THE ALTERNATION "
      "GROWS FOUR-FOLD AT FOUR PEAKS, `$-0.00049\\to-0.00203$`, WHILE THE BARYON SIGNAL ITSELF "
      "GROWS. **  *`cc66.156`'s `Ⓐ` established that the de-tilt is what holds the `$n_s$` control "
      "down; on four peaks it holds it down four times less well.  **So the price of the merge is "
      "paid in the control and not in the signal**, which is the part a reader needs in order to "
      "know what would fix it*",
      abs(_a4[1][1] / _a5[1][1]) > 3.0 and abs(_a4[0][1]) > abs(_a5[0][1])
      and PUB156[1] / min(s[3] for s in _f4) > 2.0)


# ============================================================ D. the sky on the plane
head("D.  ⛭⛭⛭ THE SKY ON THE PEAK PLANE, AND WHAT IT IS WORTH THERE")

_wid = WID[MASK]
_n = (len(_wid) // GMERGE) * GMERGE
MLC, MSD = merge(_sl, _sd, GMERGE, _wid)
_clb, _cdb, LAC, _ck = binned(SVON)
MCL, MCD = merge(_clb, _cdb, GMERGE, WID[_ck])
S_SKY = stat(peak_series(MLC, MSD, 4)[0], LAC)
S_CTL = stat(peak_series(MCL, MCD, 4)[0], LAC)
DSKY = (S_SKY[0] - S_CTL[0], S_SKY[1] - S_CTL[1])
print(f"      {'point':22s} {'phi':>10s} {'alt':>10s} {'peaks':>6s}")
print(f"      {'the sky':22s} {S_SKY[0]:+10.5f} {S_SKY[1]:+10.5f} {S_SKY[2]:6d}")
print(f"      {'the control, merged':22s} {S_CTL[0]:+10.5f} {S_CTL[1]:+10.5f} {S_CTL[2]:6d}")
print(f"      {'sky - control':22s} {DSKY[0]:+10.5f} {DSKY[1]:+10.5f}")
print()
_on4 = phi_alt(CRON, npk=4, on_bank=True, g=GMERGE)
_off4 = phi_alt(CROFF, npk=4, on_bank=True, g=GMERGE)
_p5 = phi_alt(os.path.join(LEV, 'cr_rb0.5.npz'), npk=4, on_bank=True, g=GMERGE)
_p15 = phi_alt(os.path.join(LEV, 'cr_rb1.5.npz'), npk=4, on_bank=True, g=GMERGE)
_gl = 1.0 / np.log(1.5 / 0.5)
DIRS = {'driving (more of it)': (-(_off4[0] - _on4[0]), -(_off4[1] - _on4[1])),
        'loading (more of it)': ((_p15[0] - _p5[0]) * _gl, (_p15[1] - _p5[1]) * _gl),
        'baryon direction WB': deriv(GO, 'cr', 'WB', npk=4, on_bank=True, g=GMERGE),
        'the sky, vs control': DSKY}
print(f"      {'direction':22s} {'dphi':>10s} {'dalt':>10s} {'|dalt/dphi|':>12s}")
RT = {}
for kk, v in DIRS.items():
    RT[kk] = abs(v[1] / v[0])
    print(f"      {kk:22s} {v[0]:+10.5f} {v[1]:+10.5f} {RT[kk]:12.4f}")
print(f"      ⇒ loading / driving on the discriminant: "
      f"{RT['loading (more of it)'] / RT['driving (more of it)']:.2f}x")
check("Ⓓ①  ⛭⛭⛭ ** THE SKY IS ON THE PLANE, AND THE PLANE STILL SEPARATES THE CARRIERS IN THE "
      "STATISTIC THE SKY IS READ IN: `$0.24$` FOR THE DRIVING AGAINST `$1.32$` FOR THE LOADING, "
      "`$5.6\\times$`. **  *The sky's own discriminant is `$0.34$`, and its displacement from the "
      "control is `$(+0.00756,-0.00255)$`.  **This is the thing `cc66.159` could not do and the "
      "comb was built to replace: a measured point for the observed spectrum on the peak plane.** "
      "⌗ Formed with the control's banked `$\\ell_A$`, which `Ⓓ④` is about*",
      RT['loading (more of it)'] / RT['driving (more of it)'] > 4.0 and S_SKY[2] == 4)

print()
COVD = (np.diag(FACB[MASK]) @ CS.COV_TT[np.ix_(MASK, MASK)] @ np.diag(FACB[MASK]))[:_n, :_n]
AM = merge_matrix(_wid[:_n], GMERGE, _n)
CMG = AM @ COVD @ AM.T
# ⌗ the merge is a LINEAR map on the binned D_l, so the covariance goes through it exactly:
#    nothing is approximated here and no off-diagonal is dropped.
CH = np.linalg.cholesky(CMG + 1e-10 * np.eye(len(CMG)) * np.trace(CMG) / len(CMG))
RNG = np.random.default_rng(164)
NDRAW = 2000
_P, _A, CNT = [], [], {}
for _ in range(NDRAW):
    d = MSD + CH @ RNG.standard_normal(len(CMG))
    s = stat(peak_series(MLC, d, 4)[0], LAC)
    CNT[s[2]] = CNT.get(s[2], 0) + 1
    if s[2] == 4:
        _P.append(s[0]); _A.append(s[1])
_P, _A = np.array(_P), np.array(_A)


def robust(x):
    m = float(np.median(x))
    return m, float(1.4826 * np.median(np.abs(x - m))), float(x.std(ddof=1))


MPH, SPH, SDPH = robust(_P)
MAL, SAL, SDAL = robust(_A)
print(f"      plik_lite's covariance through the merge exactly, {NDRAW} draws through the locator:")
print(f"      {'':12s} {'median':>10s} {'robust sigma':>13s} {'st.dev.':>10s} {'sd/robust':>10s}")
print(f"      {'phi':12s} {MPH:+10.5f} {SPH:13.5f} {SDPH:10.5f} {SDPH / SPH:9.1f}x")
print(f"      {'alt':12s} {MAL:+10.5f} {SAL:13.5f} {SDAL:10.5f} {SDAL / SAL:9.1f}x")
print(f"      peaks returned: " + ', '.join(f'{v} -> {CNT[v]} ({CNT[v] / NDRAW * 100:.0f}%)'
                                            for v in sorted(CNT)))
check("Ⓓ②  ⛔ ** AND THE ERROR IS HEAVY-TAILED, SO THE STANDARD DEVIATION IS NOT THE WIDTH: "
      "`$0.107$` AGAINST A ROBUST `$0.0096$`, A FACTOR OF ELEVEN. **  *The core is tight -- a "
      "robust `$\\sigma(\\varphi)$` of `$0.0096$` is `$5.8$` in `$\\ell$` per peak, consistent with "
      "the `$3.37$` the located positions actually agree to -- and the tail is the locator "
      "occasionally latching onto a noise maximum.  **Quoting the standard deviation would turn a "
      "`$13\\sigma$` instrument into a `$1\\sigma$` one and quoting only the robust scale would "
      "hide the tail, so both are here***",
      SDPH / SPH > 5.0 and abs(SPH * LAC * 2 - 5.8) < 1.5)

_sig = {'phi': (abs(DIRS['driving (more of it)'][0]), SPH), 'alt': (abs(DIRS['driving (more of it)'][1]), SAL)}
print()
print(f"      {'':22s} {'phi':>12s} {'in sigma':>10s} {'alt':>12s} {'in sigma':>10s}")
print(f"      {'one driving unit':22s} {_sig['phi'][0]:+12.5f} {_sig['phi'][0] / SPH:9.1f} "
      f"{_sig['alt'][0]:+12.5f} {_sig['alt'][0] / SAL:9.1f}")
print(f"      {'one loading unit':22s} {DIRS['loading (more of it)'][0]:+12.5f} "
      f"{abs(DIRS['loading (more of it)'][0]) / SPH:9.1f} "
      f"{DIRS['loading (more of it)'][1]:+12.5f} "
      f"{abs(DIRS['loading (more of it)'][1]) / SAL:9.1f}")
print(f"      {'the sky, vs control':22s} {DSKY[0]:+12.5f} {abs(DSKY[0]) / SPH:9.2f} "
      f"{DSKY[1]:+12.5f} {abs(DSKY[1]) / SAL:9.2f}")
check("Ⓓ③  ⛭⛭⛭ ** SO THE INSTRUMENT WORKS AND THE SKY HAS NO SIGNAL FOR IT: ONE FULL DRIVING UNIT "
      "IS `$13.1\\sigma$` ON THE COMMON OFFSET AND `$3.1\\sigma$` ON THE ALTERNATION, AND THE SKY "
      "SITS `$0.79\\sigma$` AND `$0.27\\sigma$` FROM THE CONTROL. **  *This is the first number this "
      "row has had about the observed spectrum rather than about an instrument: **the sky is "
      "consistent with the control's own driving, and one full unit of difference either way is "
      "excluded at thirteen standard deviations on the better component.**  ⌗ The loading is the "
      "weaker case at `$1.8\\sigma$`/`$2.4\\sigma$` per unit, so what the sky bounds is the "
      "driving*",
      _sig['phi'][0] / SPH > 8.0 and abs(DSKY[0]) / SPH < 2.0 and abs(DSKY[1]) / SAL < 2.0)

print()
_d = 0.01
_s2 = stat(peak_series(MLC, MSD, 4)[0], LAC * (1 + _d))
print(f"      l_A at +1 per cent moves the sky's phi by {_s2[0] - S_SKY[0]:+.5f} "
      f"({abs(_s2[0] - S_SKY[0]) / SPH:.1f} robust sigma) and its alt by {_s2[1] - S_SKY[1]:+.5f} "
      f"({abs(_s2[1] - S_SKY[1]) / SAL:.1f})")
print(f"      ⇒ the {abs(DSKY[0]) / SPH:.2f} sigma agreement needs the sky's scale to be the "
      f"control's to {SPH / (abs(_s2[0] - S_SKY[0]) / _d) * 100:.2f} per cent;")
print(f"        the {_sig['phi'][0] / SPH:.0f} sigma exclusion needs it to "
      f"{_sig['phi'][0] / (abs(_s2[0] - S_SKY[0]) / _d) * 100:.1f} per cent")
check("Ⓓ④  ⚠ ** AND THE LIMITING SYSTEMATIC IS THE ASSUMED SCALE, NOT THE NOISE: `$\\ell_A$` AT "
      "`$+1$` PER CENT MOVES THE SKY'S OFFSET BY `$2.4$` ROBUST `$\\sigma$`. **  *So the "
      "`$0.8\\sigma$` agreement is a statement conditional on the sky's acoustic scale being the "
      "control's to `$0.4$` per cent, and the `$13\\sigma$` exclusion on its being the control's to "
      "`$5$`.  **The second is comfortable and the first is not**, and the row should carry the "
      "exclusion rather than the agreement for that reason*",
      abs(_s2[0] - S_SKY[0]) / SPH > 1.5)

check("Ⓓ⑤  ⛔ ** AND WHAT BOUNDS THE INSTRUMENT IS THE FOURTH PEAK'S EXISTENCE RATHER THAN ITS "
      "POSITION: `$48$` PER CENT OF NOISE REALISATIONS DO NOT RETURN FOUR PEAKS, `$47$` OF THEM "
      "RETURNING THREE. **  *The merge sits at the locator's own resolution limit -- `Ⓐ③` shows one "
      "further step returns nothing on the sky OR the model -- so every number in `Ⓓ③` is "
      "conditional on the statistic existing, which it does on about half of the realisations of "
      "this sky.*  ⇒ **That is the number `r7223` asked for in the form the measurement actually "
      "takes: not a per-point error but a probability that the fourth maximum survives**, and it is "
      "`$52$` per cent on the bank as it stands",
      (CNT.get(4, 0) / NDRAW) < 0.6 and (CNT.get(3, 0) / NDRAW) > 0.3)

print()
_resid_per = RESID_DEG / 360.0
_kern_per = KERN_FRAC * _resid_per
print(f"      the residual's drift, in this statistic's own units: {RESID_DEG:.1f} deg = "
      f"{_resid_per:+.4f} of a comb period")
print(f"      the kernel's share of it, at 60's cited {KERN_FRAC*100:.1f} per cent: "
      f"{_kern_per:+.4f}")
print(f"      this file's measured sky - control on that axis:      {DSKY[0]:+.5f}")
print(f"      ⇒ the kernel's share is {abs(_kern_per / DSKY[0]):.1f}x the displacement measured here")
check("Ⓓ⑥  ⚠⛔ ** AND THE ONE SYSTEMATIC THIS FILE CANNOT BOUND IS LARGER THAN ITS RESULT: THE "
      "PROJECTION KERNEL'S OWN RUNNING PHASE IS `$0.0429$` OF A COMB PERIOD, `$5.7\\times$` THE "
      "`$+0.00756$` MEASURED HERE. **  *`r7225` flags it in advance: `if your merged-bank plane work "
      "places the sky absolutely at any point rather than differentially, a sixth of what it reads "
      "on the phase axis is the kernel's`.  **This reading IS differential -- every statement above "
      "is sky MINUS control through the identical merge** -- and `60`'s identity makes the kernel "
      "common mode between the two ARMS to `$0.09$` per cent.  ⌈ *But a DATA-minus-MODEL difference "
      "is not an arm-minus-control difference, and nothing in this file establishes that the "
      "kernel cancels there: it cancels only to the extent that the instrument's projection of the "
      "control is the real one, which is exactly what `60`'s own `$74\\times$` aliasing finding "
      "says can fail.*  ⇒ **So `Ⓓ③`'s `$0.79\sigma$` is conditional on that cancellation, and if "
      "it fails by its full size the displacement is `$5.3\sigma$` instead** -- the `$13\sigma$` "
      "scale of one driving unit is unaffected, since it is a model-against-model difference.  ⌗ "
      "*`$-15.45^{\\circ}$` and the `$16.0$` per cent are `60`'s own `r7236`, now on `main` and read "
      "from it rather than relayed, and they are INPUTS here.  `60`'s own words for the mechanism "
      "are `it cancels only because both arms carry it`, which is the sentence this check turns on*",
      abs(_kern_per / DSKY[0]) > 3.0 and abs(_kern_per) < abs(_resid_per))

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print(f"  ✔ {len(ran) - len(fail)} of {len(ran)} checks pass -- the plane survives the merge, the "
      "sky lands 0.8 sigma")
print("    from the control, one driving unit is 13, and half the draws lose the fourth peak.")
print(BAR)
sys.exit(0)
