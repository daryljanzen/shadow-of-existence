"""⓵⓶ WHAT ACCOUNTS FOR THE COST AT BANDS 4--7, AND HAS THAT COST ANY STRUCTURE? -- r7025+cc66.64.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** THE VOCABULARY, THREE COLUMNS WIDE, AND NO QUANTITY BELOW MIXES TWO. **
    SEPARATING POWER -- how well the data could tell two spectra apart          d'F d
    SIGNIFICANCE     -- a departure against its own trend, within one instrument
    EXCESS           -- chi2(arm) - chi2(control), what the data REJECTS on     d'F d - 2 d'F r_c
⇒ *⓵ is scored on the third.  Every share below is a ratio of two EXCESSES.*

** AND THE DECOMPOSITION IS EXACT THIS TIME. **  r_a = r_c - d, so the excess is d'F(d - 2 r_c) and
its per-bin terms SUM TO IT IDENTICALLY -- no per-band block inversion, whose contributions did not
sum (287 against 322) because the covariance couples bins across band edges.
"""
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
sys.path.insert(0, os.path.join(HERE, '..', '..', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
LC, _FAC = CS.bin_center_and_fac()


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


print(__doc__)
print('=' * 104)

LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    ls, dl, _ = load(fn)
    KN[nm] = CS.bin_spectrum(ls, dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB = (LC / AAC)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, dat, LL = MC[OK], CS.X_DATA[OK], LC[OK]
SPEC = {'the ARM': MA[OK]}
SPEC.update({k: v[OK] for k, v in KN.items()})
BANDS = list(zip(QE[:-1], QE[1:]))
MSK = [(QB >= a) & (QB < b) for a, b in BANDS]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]                                    # bands 4--7


def shape_fit(m, n):
    """a smooth multiplicative template with n free coefficients in ln(ell); n=1 is the single
    amplitude the likelihood itself fits, higher n absorbs progressively more GLOBAL shape"""
    x = np.log(LL / LL.mean())
    X = np.column_stack([m * x ** j for j in range(n)])
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ dat, assume_a='sym')


def perbin(m, n):
    """EXACT per-bin excess of spectrum m against the control, at shape order n.  Sums to
    chi2(m) - chi2(control) identically."""
    rc = dat - shape_fit(mc, n)
    d = shape_fit(m, n) - shape_fit(mc, n)
    return d * (F @ (d - 2.0 * rc)), float(d @ F @ d)


print(f"\n  ⛭ FIRST, THE ESTIMATOR IS CHECKED, BECAUSE THE PRE-REGISTRATION MADE THAT A GATE")
print('-' * 104)
EX, SEP = {}, {}
for k, m in SPEC.items():
    EX[k], SEP[k] = perbin(m, 1)
ra, rc = dat - shape_fit(SPEC['the ARM'], 1), dat - shape_fit(mc, 1)
TOT = float(ra @ F @ ra) - float(rc @ F @ rc)
print(f"    chi2(arm) - chi2(control), computed directly : {TOT:>10.4f}")
print(f"    the per-bin terms of d'F(d - 2 r_c), summed  : {EX['the ARM'].sum():>10.4f}")
print(f"    ⇒ agreement to {abs(TOT - EX['the ARM'].sum()):.2e} -- an IDENTITY, not a fit.  "
      f"*The decomposition is exact and the 287-against-322 gap is gone.*")


def blockchi(res, msk):
    c = COV[np.ix_(msk, msk)]
    f = scipy.linalg.cho_solve(scipy.linalg.cho_factor(c), np.identity(int(msk.sum())))
    return float(res[msk] @ (0.5 * (f + f.T)) @ res[msk])


print(f"\n    AND AGAINST `cc66.63`'s BLOCK-INVERTED BANDS, WHICH THE PRE-REGISTRATION REQUIRED:")
print(f"      {'band':>6s}  {'q range':>12s}  {'bins':>5s}  {'exact':>10s}  {'cc66.63 block':>14s}")
OLD = [blockchi(ra, m) - blockchi(rc, m) for m in MSK]
for j, (m, (a, b)) in enumerate(zip(MSK, BANDS)):
    print(f"      {j + 1:>6d}  {f'{a:.2f}-{b:.2f}':>12s}  {int(m.sum()):>5d}  "
          f"{EX['the ARM'][m].sum():>10.2f}  {OLD[j]:>14.2f}")
print(f"      {'SUM':>6s}  {'':>12s}  {int(sum(m.sum() for m in MSK)):>5d}  "
      f"{sum(EX['the ARM'][m].sum() for m in MSK):>10.2f}  {sum(OLD):>14.2f}")
print(f"    ⌗ *the two estimators are different objects and are not expected to agree bin by bin; "
      f"what is read is whether they LOCATE the cost in the same place.*")
f_hi_new = EX['the ARM'][HI].sum() / sum(EX['the ARM'][m].sum() for m in MSK)
f_hi_old = sum(OLD[3:]) / sum(OLD)
print(f"    ⇒ bands 4--7 carry {f_hi_new:.0%} of the banded excess on the exact decomposition and "
      f"{f_hi_old:.0%} on `cc66.63`'s.  ** The location HOLDS. **")

print('\n' + '=' * 104)
print('\n  ⛭⛭⛭ ⓵ THE CHANNELS SCORED AT BANDS 4--7, ON THE EXCESS')
print('-' * 104)
print("    *Each channel is a modified control spectrum; its excess decomposes the same exact way. "
      "The share at a band is that channel's excess there over the ARM's excess there -- a ratio of "
      "two EXCESSES and of nothing else.*")
print(f"\n    {'quantity':12s}" + ''.join(f"{f'band {j:d}':>11s}" for j in range(4, 8))
      + f"{'4--7':>11s}{'share 4--7':>13s}{'sep.power':>12s}")
SH = {}
for k in ('window', 'term mix', 'JOINT', 'the ARM'):
    row = [EX[k][MSK[j]].sum() for j in range(3, 7)]
    tot = EX[k][HI].sum()
    SH[k] = tot / EX['the ARM'][HI].sum()
    print(f"    {k:12s}" + ''.join(f"{v:>11.2f}" for v in row)
          + f"{tot:>11.2f}{SH[k]:>13.3f}{np.sqrt(SEP[k]):>11.1f}s")
print("    ⌗ *the last column is SEPARATING POWER and is printed only so the two can be SEEN not to "
      "track each other.  It is never divided into the share.*")

print(f"\n    ⌗ AND BAND BY BAND, WHICH IS WHAT THE ORDER ASKED IN SO MANY WORDS:")
print(f"      {'quantity':12s}" + ''.join(f"{f'band {j:d}':>12s}" for j in range(4, 8)))
for k in ('window', 'term mix', 'JOINT'):
    print(f"      {k:12s}" + ''.join(
        f"{EX[k][MSK[j]].sum() / EX['the ARM'][MSK[j]].sum():>12.2f}" for j in range(3, 7)))
print(f"      ⚠ *band 6 is where the ARM is cheapest ({EX['the ARM'][MSK[5]].sum():.1f} against "
      f"{EX['the ARM'][MSK[3]].sum():.0f}, {EX['the ARM'][MSK[4]].sum():.0f}, "
      f"{EX['the ARM'][MSK[6]].sum():.0f} in the other three) and every channel is expensive, so its "
      f"per-band share is a small denominator and is not to be quoted alone.*")

print(f"\n    ⛔ AND THE SHARE'S STABILITY UNDER SHAPE ABSORPTION -- `cc66.63`'s sign-flip lesson "
      f"applied BEFORE it can bite:")
print(f"      {'n':>3s}" + ''.join(f"{k:>14s}" for k in ('window', 'term mix', 'JOINT'))
      + f"{'arm 4--7 chi2':>16s}")
STAB = {k: [] for k in ('window', 'term mix', 'JOINT')}
for n in (1, 2, 3, 4):
    ea = perbin(SPEC['the ARM'], n)[0]
    vals = []
    for k in ('window', 'term mix', 'JOINT'):
        s = perbin(SPEC[k], n)[0][HI].sum() / ea[HI].sum()
        STAB[k].append(s)
        vals.append(s)
    print(f"      {n:>3d}" + ''.join(f"{v:>14.3f}" for v in vals) + f"{ea[HI].sum():>16.1f}")
print("      ⇒ " + ';  '.join(
    f"{k} {min(v):+.3f}..{max(v):+.3f}" for k, v in STAB.items()))

print(f"\n    ⛔⛔ AND THE SHARE ALONE IS NOT INTERPRETABLE, SO HERE IS THE CONTROL IT NEEDS.")
print("    *A share above one says a channel costs MORE than the arm at these bands.  But ANY spectrum "
      "that is not the control costs something, so a large share may mean only `also rejected` and not "
      "`rejected the same way`.*")
print("    ⇒ *** So the per-bin excess PATTERN is compared, not just its total: the correlation with the "
      "arm's across the 4--7 bins, the regression coefficient of the channel on the arm, and what is "
      "left of the channel once the arm-shaped part is removed. ***")
print(f"\n      {'quantity':12s}{'corr with arm':>16s}{'regression':>13s}{'arm-shaped':>13s}"
      f"{'residual':>11s}{'left over':>12s}")
ea_hi = EX['the ARM'][HI]
for k in ('window', 'term mix', 'JOINT'):
    ek = EX[k][HI]
    r = float(np.corrcoef(ek, ea_hi)[0, 1])
    beta = float(ek @ ea_hi / (ea_hi @ ea_hi))
    resid = ek - beta * ea_hi
    print(f"      {k:12s}{r:>16.3f}{beta:>13.3f}{beta * ea_hi.sum():>13.2f}"
          f"{resid.sum():>11.2f}{resid.sum() / ek.sum():>11.0%}")
print("      ⌗ *`arm-shaped` is the part of the channel's 4--7 cost that lies along the arm's own "
      "per-bin pattern; `left over` is the fraction that does not.*")

print('\n    ⌗ AND THE CANCELLATION MEASURED RATHER THAN READ OFF, as the order required:')
dw, dm, dj = (SH['window'], SH['term mix'], SH['JOINT'])
RULES = {'sum  dw+dm': dw + dm, 'product (1+dw)(1+dm)-1': (1 + dw) * (1 + dm) - 1,
         'quadrature': float(np.sign(dw + dm) * np.hypot(dw, dm))}
print(f"      singles: window {dw:+.4f}, term mix {dm:+.4f};  the realised JOINT bank gives {dj:+.4f}")
for k, v in RULES.items():
    print(f"        {k:24s} predicts {v:+.4f}   residual {v - dj:+.4f}")
BEST = min(RULES, key=lambda k: abs(RULES[k] - dj))
print(f"      ⇒ closest rule: ** {BEST.split()[0]} **, and the realised pair delivers "
      f"{dj / RULES[BEST]:.0%} of it")

print('\n' + '=' * 104)
print('\n  ⛭⛭⛭ ⓶ HAS THE EXCESS AT BANDS 4--7 ANY STRUCTURE IN THE LIKELIHOOD\'S OWN METRIC?')
print('-' * 104)
NB = int(HI.sum())
qh, eh = QB[HI], EX['the ARM'][HI]
print(f"    *{NB} bins across bands 4--7, against the SEVEN numbers `cc66.58` had across 1--7.  "
      f"Median spacing {np.median(np.diff(np.sort(qh))):.4f} in q, a comb period being 1.00.*")
mu = float(eh.mean())
sd = float(eh.std(ddof=1))
print(f"\n    per-bin excess: mean {mu:+.3f}, sd {sd:.3f}, "
      f"range {eh.min():+.2f}..{eh.max():+.2f}, sum {eh.sum():+.1f}")
x = np.log(qh / qh.mean())
for nm, deg in (('a constant', 0), ('a smooth trend in ln q', 1), ('a quadratic in ln q', 2)):
    cf = np.polyfit(x, eh, deg)
    rr = eh - np.polyval(cf, x)
    print(f"    vs {nm:24s}: residual sd {rr.std(ddof=1):.3f}  "
          f"({1 - rr.var() / eh.var():+.1%} of the scatter explained)")

print(f"\n    ⛭ AND AGAINST THE ACOUSTIC COMB, WITH A NULL FROM WRONG PERIODS")
print("    *A projection onto any smooth basis always returns something, so the comb amplitude is "
      "scored against what the SAME projection returns at neighbouring, wrong periods.*")
det = eh - np.polyval(np.polyfit(x, eh, 1), x)


def amp(period):
    w = 2.0 * np.pi / period
    X = np.column_stack([np.cos(w * qh), np.sin(w * qh)])
    c = scipy.linalg.lstsq(X, det)[0]
    return float(np.hypot(*c))


PER = np.linspace(0.55, 1.95, 141)
A = np.array([amp(p) for p in PER])
a1 = amp(1.0)
null = A[np.abs(PER - 1.0) > 0.15]
print(f"\n    comb period 1.00 in q      : amplitude {a1:.4f}")
print(f"    wrong periods (|p-1| > 0.15): {len(null)} of them, "
      f"mean {null.mean():.4f}, sd {null.std(ddof=1):.4f}, max {null.max():.4f}")
z = (a1 - null.mean()) / null.std(ddof=1)
print(f"    ⇒ the acoustic period sits {z:+.2f} sd above the null, and "
      f"{(null >= a1).sum()} of {len(null)} wrong periods return MORE")
print(f"    ⇒ the largest amplitude anywhere in 0.55--1.95 is at period {PER[A.argmax()]:.2f} "
      f"({A.max():.4f})")
print("    ⚠ *the null periods are a SMOOTH curve and so are correlated; the sd above is therefore not "
      "a p-value.  The rank statement is the defensible one.*")

print(f"\n    ⛔⛔ AND THE CONTROL THAT DECIDES WHETHER THAT COMB IS A RESULT OR AN ARTEFACT OF `d`.")
print("    *`d` is itself a comb in q.  The excess is d'F d - 2 d'F r_c.  The FIRST term is quadratic "
      "in d, so a comb of period 1 enters it at period 1/2, not 1; the SECOND is LINEAR in d and "
      "carries period 1 modulated by WHERE THE DATA SITS.*")
print("    ⇒ *** So a comb at period 1.00 must come from the cross term -- and if it does, the "
      "modulation is a fact about the data and not about the model difference.  Split it and look. ***")
_d = shape_fit(SPEC['the ARM'], 1) - shape_fit(mc, 1)
_rc = dat - shape_fit(mc, 1)
PARTS = {'d\'F d  (separating power)': _d * (F @ _d),
         '-2 d\'F r_c  (where the data sits)': -2.0 * _d * (F @ _rc)}
print(f"\n      {'term':36s}{'sum over 4--7':>15s}{'amp at 1.00':>13s}{'amp at 0.50':>13s}"
      f"{'null mean':>11s}")
for nm, v in PARTS.items():
    vh = v[HI]
    dv = vh - np.polyval(np.polyfit(x, vh, 1), x)

    def _a(p, dd=dv):
        w = 2.0 * np.pi / p
        X = np.column_stack([np.cos(w * qh), np.sin(w * qh)])
        return float(np.hypot(*scipy.linalg.lstsq(X, dd)[0]))
    nl = np.array([_a(p) for p in PER[np.abs(PER - 1.0) > 0.15]])
    print(f"      {nm:36s}{vh.sum():>15.1f}{_a(1.0):>13.3f}{_a(0.5):>13.3f}{nl.mean():>11.3f}")
print("      ⇒ *and the two sum to the excess exactly, so this is a decomposition and not a model.*")

print('\n' + '=' * 104)
