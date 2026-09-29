"""⓵ THE SAME THREE PROJECTIONS, AGAINST THE INSTRUMENT-NOISE NULL 70 VALIDATED -- r7033+cc66.66.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** THE MEASUREMENT IS UNCHANGED.  ONLY THE BAR CHANGES. **  70's audit: 82 bins over T = 2.78 in q hold about
3.6 independent frequencies and the 110-period ensemble has N_eff = 3.07, so `cc66.65`'s "none of 110" is worth
roughly ONE IN FOUR.  *The wrong-period bar cannot carry an exit.*

** AND THE QUADRATIC TERM CARRIES NO NOISE BY CONSTRUCTION ** -- d is fixed and only r_c moves -- so a quantity
whose modulation sits in d'F d CANNOT FAIL this null, and that is stated beside any such result rather than
read as a pass.
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
ma, mk = MA[OK], KN['term mix'][OK]
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]
qh = QB[HI]
x = np.log(qh / qh.mean())

# ⛔ 70's own definitions, copied rather than re-derived, so this is 70's instrument and not my reading of it.
_xf = np.log(LL / LL.mean())


def shape_fit(m, n, data):
    X = np.column_stack([m * _xf ** j for j in range(n)])
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ data, assume_a='sym')


def detrend(v):
    return v - np.polyval(np.polyfit(x, v, 1), x)


_CS1, _SN1 = np.cos(2.0 * np.pi * qh), np.sin(2.0 * np.pi * qh)
_X1 = np.column_stack([_CS1, _SN1])


def amp1(dd):
    return float(np.hypot(*scipy.linalg.lstsq(_X1, dd)[0]))


def excess(m, data):
    """the two terms of the exact per-bin excess of m over the control, at n = 1"""
    rc = data - shape_fit(mc, 1, data)
    d = shape_fit(m, 1, data) - shape_fit(mc, 1, data)
    return d * (F @ d), -2.0 * d * (F @ rc)


def trio(data):
    """ⓐ, ⓑ, ⓒ over bands 4--7, with beta and gamma RE-ESTIMATED from this data, plus their two terms"""
    qa, ca = excess(ma, data)
    qk, ck = excess(mk, data)
    ea, ek = (qa + ca)[HI], (qk + ck)[HI]
    be = float(ek @ ea / (ea @ ea))
    ga = float(ea @ ek / (ek @ ek))
    return {'ⓐ': ek, 'ⓑ': ea - ga * ek, 'ⓒ': ek - be * ea,
            'ⓐq': qk[HI], 'ⓐx': ck[HI],
            'ⓑq': qa[HI] - ga * qk[HI], 'ⓑx': ca[HI] - ga * ck[HI],
            'ⓒq': qk[HI] - be * qa[HI], 'ⓒx': ck[HI] - be * ca[HI],
            'arm': ea, 'armq': qa[HI], 'armx': ca[HI], 'beta': be, 'gamma': ga}


OBS = trio(dat)
print("\n  ⛔ THE GATE FIRST: DOES THIS REPRODUCE 70's INSTRUMENT?  If not, nothing below can be read.")
print('-' * 104)
rng = np.random.default_rng(7033)
Lc = np.linalg.cholesky(COV)
base = shape_fit(mc, 1, dat)
NDRAW = 2000
DRAWS = [base + Lc @ rng.standard_normal(len(dat)) for _ in range(NDRAW)]
arm_null = np.array([amp1(detrend(trio(ds)['arm'])) for ds in DRAWS])
a_arm = amp1(detrend(OBS['arm']))
print(f"    the arm's comb amplitude       : {a_arm:.4f}   (cc66.64 measured 7.304)")
print(f"    draws reaching it, of {NDRAW}      : {int((arm_null >= a_arm).sum())}   "
      f"(70 reported 0)")
print(f"    the null's maximum             : {arm_null.max():.4f}   (70 reported 2.54)")
print(f"    ⇒ *** {'REPRODUCED' if (arm_null >= a_arm).sum() == 0 and abs(arm_null.max() - 2.54) < 0.6 else 'NOT REPRODUCED -- STOP'} ***")

print('\n' + '=' * 104)
print("\n  ⛭⛭⛭ ⓵ THE THREE PROJECTIONS AGAINST THE INSTRUMENT-NOISE NULL")
print('-' * 104)
print("    *PRIMARY: beta and gamma RE-ESTIMATED on every draw, so the null propagates the estimation.*")
NUL = {k: np.array([amp1(detrend(trio(ds)[k])) for ds in DRAWS]) for k in ('ⓐ', 'ⓑ', 'ⓒ')}
print(f"\n    {'quantity':36s}{'amp':>9s}{'null med':>10s}{'null p99':>10s}{'null max':>10s}"
      f"{'# >= amp':>10s}{'p':>9s}")
RES = {}
for k, lbl in (('ⓐ', 'ⓐ term mix own cost'),
               ('ⓑ', 'ⓑ arm excess it does NOT explain'),
               ('ⓒ', 'ⓒ the 45% it misplaces')):
    a = amp1(detrend(OBS[k]))
    n = NUL[k]
    ge = int((n >= a).sum())
    p = (1 + ge) / (1 + len(n))
    RES[k] = (a, ge, p, float(n.max()))
    print(f"    {lbl:36s}{a:>9.3f}{np.median(n):>10.3f}{np.quantile(n, 0.99):>10.3f}{n.max():>10.3f}"
          f"{ge:>10d}{p:>9.4f}")

print("\n    ⛔ AND THE TWO TERMS, BECAUSE THE QUADRATIC ONE CANNOT FAIL THIS NULL BY CONSTRUCTION")
print(f"    {'quantity':36s}{'amp':>9s}{'null med':>10s}{'null sd':>10s}{'# >= amp':>10s}   what it means")
for k, lbl in (('ⓐq', "ⓐ  d'F d      (noise-free)"), ('ⓐx', "ⓐ  -2 d'F r_c (carries noise)"),
               ('ⓑq', "ⓑ  d'F d      (noise-free)"), ('ⓑx', "ⓑ  -2 d'F r_c (carries noise)")):
    a = amp1(detrend(OBS[k]))
    n = np.array([amp1(detrend(trio(ds)[k])) for ds in DRAWS])
    note = 'no noise in it to fail' if n.std() < 0.05 * max(n.mean(), 1e-9) else 'a real test'
    print(f"    {lbl:36s}{a:>9.3f}{np.median(n):>10.3f}{n.std():>10.4f}{int((n >= a).sum()):>10d}   {note}")

print("\n    ⌗ AND THE HELD-COEFFICIENT VARIANT, pre-registered as the check on how much of any clearance is "
      "the regression chasing noise:")
BE, GA = OBS['beta'], OBS['gamma']


def trio_held(data):
    qa, ca = excess(ma, data)
    qk, ck = excess(mk, data)
    ea, ek = (qa + ca)[HI], (qk + ck)[HI]
    return {'ⓐ': ek, 'ⓑ': ea - GA * ek, 'ⓒ': ek - BE * ea}


print(f"    {'quantity':36s}{'amp':>9s}{'null max':>10s}{'# >= amp':>10s}{'p':>9s}   vs per-draw")
for k in ('ⓐ', 'ⓑ', 'ⓒ'):
    a = amp1(detrend(OBS[k]))
    n = np.array([amp1(detrend(trio_held(ds)[k])) for ds in DRAWS])
    ge = int((n >= a).sum())
    p = (1 + ge) / (1 + len(n))
    same = 'same verdict' if (ge == 0) == (RES[k][1] == 0) else '** DIFFERENT VERDICT **'
    print(f"    {k:36s}{a:>9.3f}{n.max():>10.3f}{ge:>10d}{p:>9.4f}   {same}")

print(f"\n    beta = {BE:.4f}, gamma = {GA:.4f}  (measured; re-estimated on every draw in the primary)")
print('\n' + '=' * 104)

print("\n  ⛭⛭ ⓶ 70's ROUTED FINDING AGAINST `cc66.62`'s SCOPE STATEMENT -- CONFIRM, AMEND OR REJECT")
print('-' * 104)
print("    *`cc66.62` said the anchored locator \"makes no amplitude claim at band 1\".  70 reads that as "
      "true only in the sense that it quotes no band-1 number: its first anchor is INSIDE band 1, averaged "
      "with two outside.  ⇒ The check is where the locator's own anchors fall in q.*")
from scipy.signal import argrelextrema                                    # noqa: E402

_ls_f, _dl_f = LSA, DLA
_pk = [float(_ls_f[i]) for i in argrelextrema(_dl_f, np.greater, order=3)[0][:4]]
_tr = [float(_ls_f[i]) for i in argrelextrema(_dl_f, np.less, order=3)[0][:4]]
B1LO, B1HI = QE[0], QE[1]
print(f"\n    band 1 is q in [{B1LO:.2f}, {B1HI:.2f}); l_A = {AAC:.2f}, so band 1 is "
      f"l in [{B1LO * AAC:.0f}, {B1HI * AAC:.0f})")
print(f"\n      {'anchor':10s}{'ell':>10s}{'q':>10s}   in band 1?")
n_pk_in = 0
for i, a in enumerate(_pk):
    q = a / AAC
    inb = B1LO <= q < B1HI
    n_pk_in += inb
    print(f"      {'peak ' + str(i + 1):10s}{a:>10.1f}{q:>10.3f}   {'YES' if inb else 'no'}")
n_tr_in = 0
for i, a in enumerate(_tr):
    q = a / AAC
    inb = B1LO <= q < B1HI
    n_tr_in += inb
    print(f"      {'trough ' + str(i + 1):10s}{a:>10.1f}{q:>10.3f}   {'YES' if inb else 'no'}")
print(f"\n    ⇒ of the locator's four PEAK anchors, {n_pk_in} fall inside band 1; "
      f"of the four troughs, {n_tr_in} do")
print("    ⌗ *and the instrument `cc66.62` named anchors on PEAKS -- `FINE[t] = peaks_sub(...)` in "
      "`P15_the_locator_is_good_to_three_hundredths...` -- not on troughs.*")
print("\n    ⛔ BUT THE CORPUS'S OWN CHARACTERISATION OF THE INSTRUMENT COVERS BOTH, so the narrow reading "
      "would be a dodge:")
_c17 = open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(HERE))),
                         'receipts', 'P15_CR_cosmology',
                         'C17_the_instrument_already_carries_both.py'), encoding='utf-8').read()
_has = 'trough positions' in ' '.join(_c17.split())
print(f"      `C17_the_instrument_already_carries_both` states the instrument carries "
      f"\"acoustic peak and trough positions to 0.5% across P1-P4\": {_has}")
print(f"      ⇒ so a trough IS one of this instrument's anchors, and trough 1 at q = {_tr[0] / AAC:.3f} "
      f"is inside band 1.  ** 70's FACTUAL CLAIM IS CORRECT. **")
print("\n    ⛭ AND THE DISTINCTION THAT DECIDES THE ANSWER -- WHAT THE LOCATOR RETURNS:")
print("      *`anchored()` returns `-c[1] / (2 * c[0])`, the vertex POSITION in ell.  It never returns "
      "`c[0]`, `c[2]` or any height.*")
_ret_pos = '-c[1] / (2 * c[0])' in ' '.join(open(os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(HERE))), 'receipts', 'P15_CR_cosmology',
    'P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too.py'),
    encoding='utf-8').read().split())
print(f"      the locator returns a POSITION and not an amplitude: {_ret_pos}")
print("\n    ⇒ *** THE ANSWER IS AMEND, AND IT IS THE MIDDLE ONE OF THE THREE I FIXED IN ADVANCE. ***")
print("      ** 70 is right that band 1 is NOT untouched: a trough anchor sits inside it. **")
print("      ** `cc66.62`'s claim survives in substance because the instrument reports that trough's")
print("         POSITION and never an amplitude there -- but \"makes no amplitude claim at band 1\" was")
print("         carrying an implication it had not earned, that the instrument does not reach band 1")
print("         at all.  It does.  The qualifier is: it LOCATES inside band 1 and MEASURES no height")
print("         there. **")
print('\n' + '=' * 104)
