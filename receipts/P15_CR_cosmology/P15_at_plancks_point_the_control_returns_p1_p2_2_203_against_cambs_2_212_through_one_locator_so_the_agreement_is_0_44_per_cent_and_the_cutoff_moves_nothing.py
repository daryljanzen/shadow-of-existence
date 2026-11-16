"""r7813+70.2 (69's order r7813 ①): THE CONTROL'S FIRST-TO-SECOND HEIGHT RATIO AT PLANCK 2018'S
PUBLISHED POINT, ON THE POLARISATION PATH, AT THE ARMS' KFAC AND AT 1.5x IT, AGAINST CAMB AT THE SAME
POINT THROUGH THE SAME LOCATOR.

** The answer, in one line: through P15's own matched locator the control returns P1/P2 = 2.2026 at
   KFAC 2.0 and 2.2026 at KFAC 3.0 (a move of -0.0001 per cent), and CAMB at the same point returns
   2.2123, so the agreement is -0.44 per cent -- not the 0.23 per cent P15 prints against `2.200`. **

THE POINT: H0 67.36, omega_b 0.02237, omega_c 0.1200, n_s 0.9649 (Planck 2018 base LCDM).  The
instrument takes Omega_m, so Omega_m = 0.313773 (cc66's `r7807` value, 1e-6 from 0.3137721, kept so
`r7807`'s bank is reproduced).  ** The instrument has no neutrino mass ** (three massless species),
while Planck's model has sum m_nu = 0.06 eV: this is Planck's POINT in this instrument, not its MODEL.
CAMB is run both ways, and the difference is reported (`(5)`).

THE PATH: `HIER=1` (the photon hierarchy with polarisation multipoles), `LSTEP=8 LMAXL=2000`, the
185-bin configuration of the arm of record.  KFAC 2.0 is what the arm of record and `r7807`'s control
both carry in their banked config; 3.0 is the 1.5x convergence check.  Each bank is summed from
`KSLICE` pieces of 250 (2547 modes in 11 at KFAC 2, 3822 in 16 at KFAC 3).

THE LOCATOR: `_sweep` of `P15_at_its_own_preferred_H0_...`, IMPORTED, applied identically to the
instrument and to CAMB: Planck binning and bin factor, cubic spline, parabola vertices over seven
windows (40..80), heights and positions averaged.  Lensed: the instrument's TT times CAMB's
lensed/unlensed ratio at this point, against CAMB's own lensed TT.

REGISTERED before any run (`computations/beyond_the_wall/r7813_70_the_height_ratio_at_plancks_point/
PREDICTION.md`, committed at `r7813+70.1`).  Two of its five predictions FAILED and are recorded as
failed: (3) put CAMB's lensed P1/P2 in 2.19-2.21 and it is 2.2123; (4) put the agreement within
+-0.3 per cent and it is -0.44.

COMPUTES: CAMB at the point (four runs) and the locator on the two summed banks.  rc=0 on success.
Run: python3 <this file>   (numpy, scipy, camb; about two minutes)
"""
import contextlib
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
RUN = os.path.join(BW, 'r7813_70_the_height_ratio_at_plancks_point', 'out')
R7807 = os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                    # noqa: E402
import chi2_of_spectrum as CS                                                  # noqa: E402

print(__doc__.split('COMPUTES:')[0])
fails = []


def check(label, ok, got=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"\n         -> {got}" if got else ''))
    if not ok:
        fails.append(label)


COMB = os.path.join(HERE, 'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_'
                          'with_no_fitted_number.py')
_ns = {'__name__': '__r7813_locator__', '__file__': COMB}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(open(COMB, encoding='utf-8').read(), COMB, 'exec'), _ns)
    except SystemExit:
        pass
for _n in ('_sweep', '_FACB', '_WS'):
    if _n not in _ns:
        sys.exit(f'FATAL: the comb receipt no longer defines `{_n}`; P15\'s locator has moved.')
_sweep, _FACB = _ns['_sweep'], _ns['_FACB']

H0, WB, WC, NS, TAU = 67.36, 0.02237, 0.1200, 0.9649, 0.0544


def camb_tt(mnu):
    kw = dict(H0=H0, ombh2=WB, omch2=WC, ns=NS, tau=TAU, As=2.1e-9, omk=0, lmax=3000)
    p = (camb.set_params(mnu=mnu, **kw) if mnu > 0
         else camb.set_params(mnu=0.0, num_massive_neutrinos=0, **kw))
    cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=3000)
    return cl['total'][:, 0], cl['unlensed_scalar'][:, 0]


def located(ls, Dl):
    s = _sweep(CS.bin_spectrum(ls, Dl) * _FACB)
    return dict(pk=[float(x) for x in s['pk']], p12=float(s['p12']), p13=float(s['p13']),
                nW=int(s['nW']))


def bank(kf):
    with np.load(os.path.join(RUN, f'control_planck2018_kfac{kf}.npz'), allow_pickle=True) as z:
        return (np.asarray(z['ls'], float), np.asarray(z['Dl'], float),
                json.loads(str(z['config'])), int(z['n_slices']), float(z['l_A']))


print('=' * 100)
print('  (0) THE BANKS ARE WHAT THE ORDER NAMES, READ FROM THEIR OWN CONFIG')
print('=' * 100)
B = {kf: bank(kf) for kf in (2, 3)}
for kf, (ls, Dl, cfg, ns_, lA) in B.items():
    print(f"    KFAC={cfg.get('KFAC')}  ARM={cfg.get('ARM')}  LMAXL={cfg.get('LMAXL')}  "
          f"slices={ns_}  l_A={lA:.3f}  {len(ls)} multipoles {int(ls[0])}..{int(ls[-1])}")
check("both banks are the control (ARM=lcdm) at LMAXL 2000, at KFAC 2.0 and 3.0 respectively, "
      "summed from 11 and 16 slices of 250 (2547 and 3822 modes)",
      all(B[k][2].get('ARM') == 'lcdm' and B[k][2].get('LMAXL') == 2000.0 for k in (2, 3))
      and B[2][2].get('KFAC') == 2.0 and B[3][2].get('KFAC') == 3.0
      and B[2][3] == 11 and B[3][3] == 16)

with np.load(R7807, allow_pickle=True) as z:
    l7, D7, c7 = np.asarray(z['ls'], float), np.asarray(z['Dl'], float), json.loads(str(z['config']))
same = np.array_equal(l7, B[2][0])
mr = float(np.max(np.abs(B[2][1] / D7 - 1.0))) if same else float('inf')
check(f"PREDICTION (1) HELD: KFAC 2.0 REPRODUCES cc66's `r7807` Planck-point control bank, whose "
      f"config carries KFAC {c7.get('KFAC')} -- max |relative difference| {mr:.1e} <= 1e-12 on every "
      f"one of the {len(l7)} banked multipoles, so the point and the path are `r7807`'s exactly",
      same and mr <= 1e-12 and c7.get('KFAC') == 2.0)

print('\n' + '=' * 100)
print('  (1) CAMB AT THE SAME POINT, AND THE LENSING RATIO IT SUPPLIES')
print('=' * 100)
_pp = camb.set_params(H0=H0, ombh2=WB, omch2=WC, ns=NS, tau=TAU, As=2.1e-9, mnu=0.06, omk=0)
check(f"THE POINT, read back from CAMB's own parameters: H0 {_pp.H0}, omega_b {_pp.ombh2}, "
      f"omega_c {_pp.omch2}, n_s {_pp.InitPower.ns} -- Planck 2018's published base-LCDM point; "
      f"and the instrument's Omega_m {(_pp.omch2 + _pp.ombh2) / (_pp.H0 / 100) ** 2:.6f} at that h",
      abs(_pp.H0 - 67.36) < 0.005 and abs(_pp.ombh2 - 0.02237) < 5e-6
      and abs(_pp.omch2 - 0.1200) < 5e-5 and abs(_pp.InitPower.ns - 0.9649) < 5e-5
      and abs((_pp.omch2 + _pp.ombh2) / (_pp.H0 / 100) ** 2 - 0.313773) < 2e-6)
LEN06, UNL06 = camb_tt(0.06)
LEN00, UNL00 = camb_tt(0.0)
LG = np.arange(len(LEN06), dtype=float)
RATIO = np.ones_like(LEN06)
RATIO[UNL06 > 0] = LEN06[UNL06 > 0] / UNL06[UNL06 > 0]
LC = np.arange(2, 2501, dtype=float)
C = {'lensed 0.06': located(LC, LEN06[2:2501]), 'unlensed 0.06': located(LC, UNL06[2:2501]),
     'lensed 0': located(LC, LEN00[2:2501]), 'unlensed 0': located(LC, UNL00[2:2501])}
I = {}
for kf in (2, 3):
    ls, Dl = B[kf][0], B[kf][1]
    I[f'KFAC {kf}.0 lensed'] = located(ls, Dl * np.interp(ls, LG, RATIO))
    I[f'KFAC {kf}.0 unlensed'] = located(ls, Dl)

print(f"\n    {'spectrum':>26} {'peak 1':>9} {'peak 2':>9} {'peak 3':>9} {'peak 4':>9} "
      f"{'P1/P2':>8} {'P1/P3':>8}  windows")
for lab, s in list(I.items()) + [('CAMB ' + k, v) for k, v in C.items()]:
    print(f"    {lab:>26} " + ' '.join(f'{x:9.2f}' for x in s['pk'])
          + f" {s['p12']:8.4f} {s['p13']:8.4f}  {s['nW']}")
check("the locator resolves all four peaks in all seven windows on every spectrum, instrument and CAMB",
      all(s['nW'] == 7 and len(s['pk']) == 4 for s in list(I.values()) + list(C.values())))

i2, i3, cl = I['KFAC 2.0 lensed'], I['KFAC 3.0 lensed'], C['lensed 0.06']
agree = 100.0 * (i2['p12'] / cl['p12'] - 1.0)
agree_u = 100.0 * (I['KFAC 2.0 unlensed']['p12'] / C['unlensed 0.06']['p12'] - 1.0)
kmove = 100.0 * (i3['p12'] / i2['p12'] - 1.0)
kmove13 = 100.0 * (i3['p13'] / i2['p13'] - 1.0)
mmove = 100.0 * (C['lensed 0']['p12'] / cl['p12'] - 1.0)
agree0 = 100.0 * (i2['p12'] / C['lensed 0']['p12'] - 1.0)

print('\n' + '=' * 100)
print('  (2) THE FIGURES THE ORDER ASKS FOR')
print('=' * 100)
check(f"THE INSTRUMENT, KFAC 2.0, lensed: P1/P2 = {i2['p12']:.4f}, peaks "
      f"{', '.join(f'{x:.2f}' for x in i2['pk'])} -- and it is `r7809+cc66`'s matched-locator figure "
      f"`2.203` at Planck's point to the digit, the same bank through the same procedure",
      abs(i2['p12'] - 2.2026) < 5e-5 and round(i2['p12'], 3) == 2.203
      and abs(i2['pk'][0] - 220.60) < 0.01 and abs(i2['pk'][1] - 537.65) < 0.01
      and abs(i2['pk'][2] - 811.72) < 0.01 and abs(i2['pk'][3] - 1124.75) < 0.01)
check(f"PREDICTION (2) HELD -- CONVERGED: KFAC 3.0 returns P1/P2 = {i3['p12']:.4f}, a move of "
      f"{kmove:+.5f} per cent (P1/P3 {kmove13:+.5f}), against the registered bound of 0.05 per cent; "
      f"the peaks move by at most "
      f"{max(abs(a - b) for a, b in zip(i3['pk'], i2['pk'])):.4f} multipoles",
      abs(kmove) < 0.05 and abs(kmove13) < 0.05)
check(f"CAMB AT THE POINT, Planck's model (sum m_nu 0.06), lensed: P1/P2 = {cl['p12']:.4f}, peaks "
      f"{', '.join(f'{x:.2f}' for x in cl['pk'])} ⇒ ⛔ PREDICTION (3) FAILED: it was registered "
      f"in 2.19-2.21 on the strength of the printed `2.200`, and it is above that band",
      abs(cl['p12'] - 2.2123) < 5e-5 and not (2.19 <= cl['p12'] <= 2.21))
check(f"THE AGREEMENT: instrument / CAMB - 1 = {agree:+.3f} per cent on the lensed spectra, and "
      f"{agree_u:+.3f} per cent unlensed ⇒ ⛔ PREDICTION (4) FAILED: registered within +-0.3 per "
      f"cent; both are -0.44, inside half a per cent and outside the band",
      abs(agree + 0.438) < 0.005 and abs(agree_u + 0.438) < 0.005 and abs(agree) > 0.3)
check(f"PREDICTION (5) HELD: making CAMB's neutrinos massless, as the instrument's are, moves its "
      f"P1/P2 by {mmove:+.3f} per cent (bound 0.2); against massless CAMB the agreement is "
      f"{agree0:+.3f} per cent, so the neutrino mass is not what separates the two",
      abs(mmove) < 0.2 and abs(agree0 + 0.41) < 0.01)

print('\n' + '=' * 100)
print('  (3) WHAT THIS SAYS ABOUT THE PRINTED COMPARISON')
print('=' * 100)
iu, cu = I['KFAC 2.0 unlensed'], C['unlensed 0.06']
check(f"the instrument's UNLENSED P1/P2 through this locator is {iu['p12']:.4f}, equal to three decimals "
      f"to the control figure `2.195` P15 prints on the polarisation path (that one at the corpus's "
      f"old control point, which moves the ratio by about a thousandth, `r7809+cc66`); ** but "
      f"CAMB's unlensed "
      f"P1/P2 through the SAME locator at this point is {cu['p12']:.4f}, not `2.200` ** -- so the "
      f"`2.200` it is set against did not come through this procedure, and through one procedure "
      f"the gap is {agree_u:+.2f} per cent rather than 0.23",
      round(iu['p12'], 3) == 2.195 and round(cu['p12'], 3) == 2.205)
_li = I['KFAC 2.0 lensed']['p12'] / iu['p12']
_lc = cl['p12'] / cu['p12']
check(f"the comparison is like for like: lensing lifts P1/P2 by the factor {_li:.5f} on the instrument "
      f"and {_lc:.5f} on CAMB through the same locator -- equal to 1e-4, as they must be when the "
      f"instrument carries CAMB's own lensing ratio at this point -- so the -0.44 per cent is the "
      f"instrument's unlensed transfer against CAMB's and not the lensing step",
      abs(_li - _lc) < 1e-4 and abs(agree - agree_u) < 0.01)

print('\n' + '=' * 100)
print(f"  THE NUMBERS FOR cc66's ONE PASS (lensed, Planck's model):  instrument {i2['p12']:.4f} "
      f"(KFAC 2.0), {i3['p12']:.4f} (KFAC 3.0);  CAMB {cl['p12']:.4f};  agreement {agree:+.2f} %")
print('=' * 100)
if fails:
    print(f'\n  {len(fails)} CHECK(S) FAILED')
    sys.exit(1)
print('\n  all checks pass (two registered predictions failed and are recorded as failed)')
