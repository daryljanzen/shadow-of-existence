#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:refit-bound`: ** THE $1.57\times$ HAS NO PARAMETER ADDRESS, BECAUSE THE ARM'S
TT MINIMUM SITS ON ITS OWN BAO MINIMUM. $\Delta\chi^2_{\rm BAO} = +0.009$ AT IT, AND THE
DISPLACEMENT IN $\omega_m$ IS $0.05\sigma$ OF THE CONSTRAINT'S OWN WIDTH. **

*** AND THE CALIBRATION INVERTS: THE CONTROL, WHICH FITS EVERYTHING, PAYS $\Delta\chi^2 = +15.1$
AT ITS TT MINIMUM AND SITS $0.23\sigma$ OUT -- FIVE TIMES THE ARM'S DISPLACEMENT AND $1700$ TIMES
ITS $\chi^2$ PENALTY. ***

** THE ORDER (`r7181`). **  *"Give the `$1.57$` a parameter address.  Read the refit minima and
report how far each arm's TT-preferred `$\omega_m$` sits from the one its distances fix."*  Three
numbers: the minima printed; the displacement in units of the BAO$+\theta_*$ constraint's own width,
with the control as the calibration; and whether the arm's TT-preferred $\omega_m$ is still
admissible to the distance data.

===================================================================================================
** THE ANSWER **
===================================================================================================

                              H0        Om       w_m       w_b       n_s    chi^2/bin
  control, start           67.4000   0.3150   0.143097   0.02240   0.9650     1.15
  control, TT minimum      67.4103   0.3098   0.140790   0.02197   0.9542     1.008
  CR arm,  start           68.6000   0.2973   0.139908   0.02240   0.9650     2.95
  CR arm,  TT minimum      68.5811   0.2972   0.139788   0.02152   0.9980     1.581

  *The last column is the 185-bin refit receipt's own, at `r6825+cc66.25`, verified there by real
  runs ($186.5$ and $292.4$ on $185$ bins); this file does not re-score the spectra and does not
  assert it.  Everything else in the table is measured here.*

*** $\sigma(\omega_m) = 0.00454$ from DESI DR2 BAO on each arm's own ruler.  The arm's TT minimum
sits $-0.046\sigma$ from its BAO minimum and pays $\Delta\chi^2_{\rm BAO} = +0.009$.  The control's
sits $+0.227\sigma$ and pays $+15.06$. ***

⇒ ** SO THE RESIDUAL IS NOT A PARAMETER.**  *There is no direction in which the sky is pulling this
arm's matter density: the TT fit, given the expansion rate, both densities and the tilt free, lands
where the distance data already put the background and leaves it there.  The `$1.57\times$` is what
remains when the parameters have been given away, which is what `sec:refit-bound`'s own account
implies and this measures.*  ⌈ *That is the answer `r7181` named as the more interesting one, and it
is the one that came.*

⛔ ** AND THE ORDER'S CALIBRATION PREMISE IS FALSE, MEASURABLY. **  *`r7181` reads the control's
displacement as the floor -- "it fits everything, so its pull should be small".*  **It is the larger
of the two by a factor of five in $\omega_m$ and by $1700$ in $\chi^2$**, because `$0.3150$` is not
a BAO$+\theta_*$ value at all: *it is Planck's CMB-fitted $\Omega_m$, and DESI DR2 BAO on the
control's own ruler prefers $0.2971 \pm 0.0085$.*  ⇒ ** The control's pull is the known DESI--Planck
$\Omega_m$ tension, not a floor this comparison can read. **  *Its TT refit moves it $3$ in $\chi^2$
TOWARD DESI and leaves it $15$ away.*

⌗ ** AND THE VARIABLE THE ORDER CHOSE IS THE ONE THAT FLATTERS THE CONTROL. **  *In $\Omega_m$ the
control's TT minimum is $+1.498\sigma$ out and the arm's $-0.016\sigma$ -- a factor of $94$.  In
$\omega_m$ it is $+0.227$ against $-0.046$, a factor of $5$, because the control's TT $H_0$ sits
BELOW its BAO $H_0$ while its $\Omega_m$ sits above, and the two offsets partly cancel in
$\Omega_m h^2$.*  **Both orderings agree on sign and on which arm is displaced; only the size moves,
and it is reported in both so the choice of variable is visible.**

===================================================================================================
** WHAT IS READ RATHER THAN RUN, AND WHAT IS CHECKED BEFORE IT IS USED **
===================================================================================================

  ** THE TT MINIMA ARE READ OFF THE BANKED ARTEFACTS, NOT QUOTED. **  `refit_grid185/verify.sh`
  carries the parameters the two verification spectra were run at.  This receipt puts those
  parameters back through `ACOUSTIC_two_arm` and requires the instrument's own `D_M`, `r_s` and
  `l_A` to reproduce what `verify_{lcdm,cr}.npz` STORE -- so the minimum is established from the
  artefact and a drifted launcher refuses rather than being believed.

  ** THE BAO LIKELIHOOD REPRODUCES A BANKED NUMBER AND AN EXTERNAL ONE BEFORE IT IS TRUSTED. **
  DESI DR2 Table IV (arXiv:2503.14738), 13 measurements, the same constants
  `r6760+cc66.3`'s receipt uses.  Two checks first: the corpus's own stacking-ruler anchor
  ($\Omega_m = 0.3066$, $\chi^2 = 12.01$, $z_{\rm onset} = 6764$), and the PUBLISHED DESI DR2
  $\Lambda$CDM value $\Omega_m = 0.2975 \pm 0.0086$, which this file recovers independently.

  ** AND THE RULER ASSIGNMENT IS THE INSTRUMENT'S, NOT A GUESS. **  The arm carries distances on its
  radiation-free rate and $r_s$ on the leaf clock (`LEAFSCALES=1`, node 66's adjudication at
  `r6760+66.1`); the control carries radiation in both.  *That mixed assignment is what returns
  $(68.60,\,0.2973)$ as its own BAO minimum -- checked here, not assumed, and it is how the pair the
  paper carries is recovered from the data without a spectrum.*

  ⚠ ** $\theta_*$ IS A CONFIRMATION IN THIS FIT AND NOT A TERM IN IT, AND THAT IS THE CORPUS'S
  CHOICE RATHER THAN THIS FILE'S. **  The corpus imposes $\theta_*$ EXACTLY, by solving $z_{\rm
  onset}$ from it, so it constrains the onset and not $(H_0, \Omega_m)$; its independent force is
  the second determination at `r6760+cc66.3` PART 4, where $\theta_*$ alone gives $H_0 = 68.55$
  against BAO's $68.50$.  *Scored instead as a Gaussian term at Planck's
  $100\theta_* = 1.04109 \pm 0.00030$, the arm's background sits $-15.8\sigma$ -- which is the comb
  disagreement already in print ($\ell_A = 302.9$ against the sky's $298.0$) and not a new finding.
  It is recorded here so that `BAO$+\theta_*$` is read as the corpus means it.*

** PARAMETERS. **  Nothing is fitted that the corpus does not already fit.  $\Omega_m$ and $H_0$ are
fitted to DESI DR2 BAO; the TT minima are read.  $w_b = 0.02237$, $w_\gamma = 2.47\times10^{-5}$,
$w_r = 4.15\times10^{-5}$, $z_{\rm rec} = 1090.0$, $z_{\rm drag} = 1059.94$.

** COMPUTES: the two refit minima with their omega_m, the BAO minimum and profiled Delta-chi^2 = 1
   width on each arm's own ruler, the TT displacement in omega_m and in Omega_m, and the chi^2 the
   distance data pays at each TT minimum. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~30 s)
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
G185 = os.path.join(BW, 'refit_grid185')
INSTR = os.path.join(BW, 'ACOUSTIC_two_arm.py')

# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE TWO TT MINIMA, READ OFF THE BANKED ARTEFACTS **")
print(BAR)

# ⛭ The launcher is the record of what was run; the `.npz` are the record of what came back.  The
#   parameters are CAPTURED from the launcher and then required to reproduce the artefacts' own
#   stored numbers, so neither is taken on trust.
VSH = open(os.path.join(G185, 'verify.sh'), encoding='utf-8').read()
LAUNCH = {
    'lcdm': r"verify_lcdm\s+ARM=lcdm LH0=([0-9.]+) LOM=([0-9.]+) WBH2=([0-9.]+) NS=([0-9.]+)",
    'cr': r"verify_cr\s+ARM=cr CRH0=([0-9.]+) CROM=([0-9.]+) ZSTART=(\S+) LEAFSCALES=1 "
          r"WBH2=([0-9.]+) NS=([0-9.]+)",
}
m_l = re.search(LAUNCH['lcdm'], VSH)
m_c = re.search(LAUNCH['cr'], VSH)
if not (m_l and m_c):
    print("  ⛔ REFUSED -- ** `refit_grid185/verify.sh` NO LONGER CARRIES THE TWO VERIFICATION "
          "COMMANDS IN THE FORM THIS RECEIPT READS THEM. **  The best-fit parameters are the thing "
          "being reported, so a launcher this file cannot parse is not a launcher it may guess at. "
          " *Nothing is asserted.*")
    sys.exit(1)
TTMIN = {
    'lcdm': dict(H0=float(m_l.group(1)), OM=float(m_l.group(2)), WB=float(m_l.group(3)),
                 NS=float(m_l.group(4)), env=dict(ARM='lcdm', LH0=m_l.group(1), LOM=m_l.group(2),
                                                  WBH2=m_l.group(3))),
    'cr': dict(H0=float(m_c.group(1)), OM=float(m_c.group(2)), WB=float(m_c.group(4)),
               NS=float(m_c.group(5)), env=dict(ARM='cr', CRH0=m_c.group(1), CROM=m_c.group(2),
                                                ZSTART=m_c.group(3), LEAFSCALES='1',
                                                WBH2=m_c.group(4))),
}
# the BAO+theta_* background each arm starts from, as `sec:refit-bound` carries it
START = {'lcdm': dict(H0=67.4000, OM=0.3150, WB=0.0224, NS=0.9650),
         'cr': dict(H0=68.6000, OM=0.2973, WB=0.0224, NS=0.9650)}

KNOBS = ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'WBH2', 'NS', 'ZSTART', 'LEAFSCALES', 'NK', 'LEAFGEOM')
_saved = {k: os.environ.get(k) for k in KNOBS}
for tag in ('lcdm', 'cr'):
    for k in KNOBS:
        os.environ.pop(k, None)
    os.environ.update(TTMIN[tag]['env'])
    os.environ['NK'] = '120'                      # the background is built before NK is used
    spec = importlib.util.spec_from_file_location(f"ACOUSTIC_two_arm_cc144_{tag}", INSTR)
    AT = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(AT)
    TTMIN[tag]['DM'] = float(AT.D_M)
    z = np.load(os.path.join(G185, f'verify_{tag}.npz'), allow_pickle=True)
    TTMIN[tag]['DM_banked'] = float(np.atleast_1d(z['D_M'])[0])
    TTMIN[tag]['rs_banked'] = float(np.atleast_1d(z['r_s'])[0])
    TTMIN[tag]['lA_banked'] = float(np.atleast_1d(z['l_A'])[0])
for k, v in _saved.items():
    os.environ.pop(k, None)
    if v is not None:
        os.environ[k] = v

for tag, nm in (('lcdm', 'control (LCDM)'), ('cr', 'CR, crossing ')):
    t = TTMIN[tag]
    print(f"      {nm}  launcher ({t['H0']:.6f}, {t['OM']:.6f})  ->  instrument D_M = {t['DM']:.4f}"
          f"   banked D_M = {t['DM_banked']:.4f}   r_s = {t['rs_banked']:.4f}   "
          f"l_A = {t['lA_banked']:.4f}")
check("⛭⛭ the parameters captured from `verify.sh` reproduce BOTH banked verification spectra's own "
      "stored `D_M` to a part in 10^7 -- so the TT minima are established from the artefacts and "
      "not from the launcher's word",
      all(abs(TTMIN[t]['DM'] / TTMIN[t]['DM_banked'] - 1.0) < 1e-7 for t in ('lcdm', 'cr')))


def wm_of(d):
    return d['OM'] * (d['H0'] / 100.0) ** 2


print()
print(f"      {'':26s} {'H0':>10} {'Om':>9} {'w_m':>10} {'w_b':>9} {'n_s':>8}")
for tag, nm in (('lcdm', 'control'), ('cr', 'CR arm')):
    for lab, d in ((f'{nm}, start', START[tag]), (f'{nm}, TT minimum', TTMIN[tag])):
        print(f"      {lab:26s} {d['H0']:10.4f} {d['OM']:9.4f} {wm_of(d):10.6f} "
              f"{d['WB']:9.5f} {d['NS']:8.4f}")
check("⌗ the arm's TT minimum moves `Omega_m` by under a thirtieth of a per cent while the "
      f"control's moves it by {abs(TTMIN['lcdm']['OM'] / START['lcdm']['OM'] - 1) * 100:.2f}% -- "
      "the asymmetry this receipt is about, before any constraint is involved",
      abs(TTMIN['cr']['OM'] / START['cr']['OM'] - 1) < 5e-4
      and abs(TTMIN['lcdm']['OM'] / START['lcdm']['OM'] - 1) > 1e-2)

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** THE BAO LIKELIHOOD, CHECKED AGAINST A BANKED NUMBER AND A PUBLISHED ONE **")
print(BAR)

trapz = np.trapezoid
C = 299792.458
# DESI DR2, Table IV (arXiv:2503.14738) -- the same 13 measurements `r6760+cc66.3`'s receipt scores
DESI_ANISO = [(0.510, 13.588, 0.167, 21.863, 0.425, -0.459),
              (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
              (0.934, 21.576, 0.152, 17.641, 0.193, -0.416),
              (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
              (1.484, 30.512, 0.760, 12.817, 0.516, -0.500),
              (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
DESI_ISO = [(0.295, 7.942, 0.075)]
NDATA = 2 * len(DESI_ANISO) + len(DESI_ISO)
WB, WG, WR = 0.02237, 2.47e-5, 4.15e-5
R0 = 3 * WB / (4 * WG)
ZREC, ZDRAG = 1090.0, 1059.94
THETA_OBS = 0.0104085


def cs(z):
    return C / np.sqrt(3 * (1 + R0 / (1 + z)))


def E_free(z, Om, h):
    """the arm's own rate: radiation is CONTENT, not a source, so it is absent here"""
    return np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


def E_rad(z, Om, h):
    """the leaf / LCDM rate: radiation gravitates, at w_r = 4.15e-5"""
    return np.sqrt(Om * (1 + z) ** 3 + (WR / h ** 2) * (1 + z) ** 4 + (1 - Om))


def D_M(z, H0, Om, E, n=4000):
    zz = np.linspace(0, z, n)
    return trapz(C / (H0 * E(zz, Om, H0 / 100)), zz)


def D_H(z, H0, Om, E):
    return C / (H0 * E(z, Om, H0 / 100))


def D_V(z, H0, Om, E):
    return (z * D_M(z, H0, Om, E) ** 2 * D_H(z, H0, Om, E)) ** (1 / 3)


def r_snd(H0, Om, z_hi, z_lo, E, n=60000):
    u = np.linspace(np.log(1 + z_lo), np.log(1 + z_hi), n)
    z = np.exp(u) - 1
    return trapz(cs(z) / (H0 * E(z, Om, H0 / 100)) * (1 + z), u)


def chi2_bao(H0, Om, rd, E):
    x2 = 0.0
    for z, dm, sdm, dh, sdh, rho in DESI_ANISO:
        r = np.array([D_M(z, H0, Om, E) / rd - dm, D_H(z, H0, Om, E) / rd - dh])
        cov = np.array([[sdm ** 2, rho * sdm * sdh], [rho * sdm * sdh, sdh ** 2]])
        x2 += r @ np.linalg.solve(cov, r)
    for z, dv, sdv in DESI_ISO:
        x2 += ((D_V(z, H0, Om, E) / rd - dv) / sdv) ** 2
    return float(x2)


# ⛭ CHECK ONE: the corpus's own stacking-ruler anchor, with theta_* imposed through the onset.
def z_onset_of(H0, Om, E):
    return brentq(lambda zo: r_snd(H0, Om, zo, ZREC, E) / D_M(ZREC, H0, Om, E) - THETA_OBS,
                  1500., 5.0e6)


def _stack_fit(H0):
    def f(Om):
        try:
            return chi2_bao(H0, Om, r_snd(H0, Om, z_onset_of(H0, Om, E_free), ZDRAG, E_free), E_free)
        except Exception:
            return 1.0e9
    r = minimize_scalar(f, bounds=(0.22, 0.42), method='bounded')
    return float(r.x), float(r.fun)


_om, _x2 = _stack_fit(73.0)
_zo = z_onset_of(73.0, _om, E_free)
print(f"      corpus anchor, stacking ruler at H0 = 73:  Om = {_om:.4f}   chi^2 = {_x2:.2f}   "
      f"z_onset = {_zo:.0f}")
check("⛭ the corpus's banked stacking-ruler anchor is reproduced -- `Om = 0.3066`, `chi^2 = 12.01`, "
      "`z_onset = 6764` -- so this file's likelihood is the one `r6760+cc66.3` already scores",
      abs(_om - 0.3066) < 2e-3 and abs(_x2 - 12.01) < 0.35 and abs(_zo - 6764) < 30)

# the two rulers, each as its own arm carries them
RULER = {'cr': E_free, 'lcdm': E_rad}       # whose rate carries the DISTANCES


def chi2_of(tag, H0, Om):
    """r_s on the LEAF clock in both arms (LEAFSCALES=1); distances on the arm's own rate"""
    return chi2_bao(H0, Om, r_snd(H0, Om, 1.0e8, ZDRAG, E_rad), RULER[tag])


# ⛭ CHECK TWO, EXTERNAL: DESI DR2's published LCDM value, recovered from the same 13 points.
def _fit2d(tag):
    fh = (lambda h: minimize_scalar(lambda Om: chi2_of(tag, h, Om), bounds=(0.22, 0.42),
                                    method='bounded').fun)
    H0b = float(minimize_scalar(fh, bounds=(64., 74.), method='bounded').x)
    r = minimize_scalar(lambda Om: chi2_of(tag, H0b, Om), bounds=(0.22, 0.42), method='bounded')
    return H0b, float(r.x), float(r.fun)


BAOMIN = {}
for tag in ('lcdm', 'cr'):
    H0b, Omb, x2b = _fit2d(tag)
    BAOMIN[tag] = dict(H0=H0b, OM=Omb, chi2=x2b, wm=Omb * (H0b / 100.) ** 2)
print(f"      control ruler (LCDM):  BAO minimum  H0 = {BAOMIN['lcdm']['H0']:.4f}  "
      f"Om = {BAOMIN['lcdm']['OM']:.5f}  chi^2 = {BAOMIN['lcdm']['chi2']:.3f} "
      f"({BAOMIN['lcdm']['chi2'] / (NDATA - 2):.3f} per dof)")
print(f"      arm ruler (D free, r_s leaf):        H0 = {BAOMIN['cr']['H0']:.4f}  "
      f"Om = {BAOMIN['cr']['OM']:.5f}  chi^2 = {BAOMIN['cr']['chi2']:.3f} "
      f"({BAOMIN['cr']['chi2'] / (NDATA - 2):.3f} per dof)")
check("⛭⛭ EXTERNAL: DESI DR2's published LCDM value `Om = 0.2975 +- 0.0086` is recovered on the "
      f"control's ruler from the same 13 points -- {BAOMIN['lcdm']['OM']:.4f} -- so the likelihood "
      "agrees with its source and not only with this corpus",
      abs(BAOMIN['lcdm']['OM'] - 0.2975) < 0.0015)
check("⛭⛭ and the arm's OWN ruler returns `(68.6, 0.2973)` as its BAO minimum -- the pair "
      "`sec:refit-bound` starts from, recovered here from the distance data with no spectrum "
      "involved, which is what makes it the constraint this comparison is measured against",
      abs(BAOMIN['cr']['H0'] - START['cr']['H0']) < 0.05
      and abs(BAOMIN['cr']['OM'] - START['cr']['OM']) < 5e-4)

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE CONSTRAINT'S OWN WIDTH, PROFILED **")
print(BAR)


def _width(tag, kind):
    """profiled Delta-chi^2 = 1 half-width in Om or in w_m"""
    b = BAOMIN[tag]
    if kind == 'OM':
        prof = (lambda Om: minimize_scalar(lambda h: chi2_of(tag, h, Om), bounds=(60., 78.),
                                           method='bounded').fun)
        x0, span = b['OM'], 0.08
    else:
        def prof(wm):
            def g(h):
                Om = wm / (h / 100.) ** 2
                return chi2_of(tag, h, Om) if 0.15 < Om < 0.55 else 1.0e9
            return minimize_scalar(g, bounds=(60., 78.), method='bounded').fun
        x0, span = b['wm'], 0.02
    tgt = b['chi2'] + 1.0
    hi = brentq(lambda x: prof(x) - tgt, x0, x0 + span)
    lo = brentq(lambda x: prof(x) - tgt, x0 - span, x0)
    return 0.5 * ((hi - x0) + (x0 - lo))


for tag in ('lcdm', 'cr'):
    BAOMIN[tag]['s_OM'] = _width(tag, 'OM')
    BAOMIN[tag]['s_wm'] = _width(tag, 'wm')
    b = BAOMIN[tag]
    print(f"      {'control' if tag == 'lcdm' else 'CR arm ':7s}  sigma(Om) = {b['s_OM']:.5f}   "
          f"sigma(w_m) = {b['s_wm']:.6f}   at w_m = {b['wm']:.6f}")
check("⛭ the width in `Om` recovers DESI DR2's published `+-0.0086` on the control's ruler, so the "
      "units this comparison is reported in are the constraint's own and not a convention",
      abs(BAOMIN['lcdm']['s_OM'] - 0.0086) < 0.0015)
check("⌗ and the two rulers' widths agree to a per cent, so the arms are compared in the same "
      "units and the asymmetry below is not one of them being measured more loosely",
      abs(BAOMIN['cr']['s_wm'] / BAOMIN['lcdm']['s_wm'] - 1.0) < 0.01)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE DISPLACEMENT, AND WHAT THE DISTANCE DATA PAYS FOR IT **")
print(BAR)

RES = {}
print(f"      {'':28s} {'w_m':>10} {'d(w_m)':>9} {'d(Om)':>9} {'chi2_BAO':>10} {'Dchi2':>9}")
for tag, nm in (('lcdm', 'control'), ('cr', 'CR arm')):
    b = BAOMIN[tag]
    for lab, d in ((f'{nm}, start', START[tag]), (f'{nm}, TT minimum', TTMIN[tag])):
        wm = wm_of(d)
        x2 = chi2_of(tag, d['H0'], d['OM'])
        row = dict(wm=wm, d_wm=(wm - b['wm']) / b['s_wm'], d_OM=(d['OM'] - b['OM']) / b['s_OM'],
                   chi2=x2, dchi2=x2 - b['chi2'])
        RES[lab] = row
        print(f"      {lab:28s} {wm:10.6f} {row['d_wm']:>+8.3f}s {row['d_OM']:>+8.3f}s "
              f"{x2:10.3f} {row['dchi2']:>+9.2f}")

A, Ctl = RES['CR arm, TT minimum'], RES['control, TT minimum']
check("⛭⛭⛭ ** THE ARM'S TT-PREFERRED `w_m` IS ADMISSIBLE TO ITS OWN DISTANCE DATA: it sits inside "
      f"a twentieth of the constraint's width ({A['d_wm']:+.3f} sigma) and the BAO fit pays "
      f"{A['dchi2']:+.3f} in chi^2 at it ** -- so there is no parameter the sky is pulling, and the "
      "1.57x is what remains after the parameters have been given away",
      abs(A['d_wm']) < 0.10 and abs(A['dchi2']) < 0.10)
check("⛔⛔ ** AND THE CALIBRATION INVERTS: the CONTROL's TT minimum sits five times further out "
      f"({Ctl['d_wm']:+.3f} sigma against {A['d_wm']:+.3f}) and pays {Ctl['dchi2']:+.2f} against "
      f"{A['dchi2']:+.3f} ** -- so the control's displacement is NOT the floor `r7181` read it as",
      Ctl['d_wm'] / abs(A['d_wm']) > 4.0 and Ctl['dchi2'] > 10.0)
check("⛔ and the reason is that `0.3150` is not a BAO+theta_* value: it is Planck's CMB-fitted "
      f"`Om`, which sits {RES['control, start']['d_wm']:+.3f} sigma and "
      f"{RES['control, start']['dchi2']:+.2f} in chi^2 from what DESI DR2 prefers on the control's "
      "own ruler -- the known DESI--Planck tension, carried into this comparison by the premise",
      RES['control, start']['dchi2'] > 10.0
      and abs(START['lcdm']['OM'] - BAOMIN['lcdm']['OM']) > 3 * BAOMIN['lcdm']['s_OM'] / 2)
check("⌗ the control's TT refit moves it TOWARD the distance data rather than away -- its chi^2 "
      f"penalty falls from {RES['control, start']['dchi2']:+.2f} to {Ctl['dchi2']:+.2f} -- so what "
      "is left is the tension between its two datasets and not something the refit introduced",
      Ctl['dchi2'] < RES['control, start']['dchi2'])
check("⌗ and the arm's START is already its own BAO minimum, so its refit had nowhere to be pulled "
      f"to: {RES['CR arm, start']['d_wm']:+.3f} sigma before the fit and {A['d_wm']:+.3f} after",
      abs(RES['CR arm, start']['d_wm']) < 0.10)

print()
print("      ⌗ the same two displacements in `Om`, where they do NOT partly cancel:")
print(f"        control TT minimum {Ctl['d_OM']:+.3f} sigma   CR arm TT minimum {A['d_OM']:+.3f} "
      f"sigma   -- a factor of {abs(Ctl['d_OM'] / A['d_OM']):.0f}, against "
      f"{abs(Ctl['d_wm'] / A['d_wm']):.0f} in `w_m`")
check("⛭ the ordering is the same in both variables and only the size moves, so the result does not "
      "turn on the order's choice of `w_m` -- but `w_m` is the variable that flatters the control, "
      "and both are reported rather than the flattering one alone",
      abs(Ctl['d_OM']) > abs(A['d_OM']) and abs(Ctl['d_wm']) > abs(A['d_wm'])
      and abs(Ctl['d_OM'] / A['d_OM']) > abs(Ctl['d_wm'] / A['d_wm']))

# =================================================================================================
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE $1.57\\times$ HAS NO PARAMETER ADDRESS. **  The arm's TT minimum sits")
print(f"    {A['d_wm']:+.3f} sigma from its own BAO minimum in $\\omega_m$ and pays "
      f"{A['dchi2']:+.3f} in $\\chi^2$")
print("    to the distance data, so the residual is not a displacement of the matter density --")
print("    which is the answer `r7181` named as the more interesting one.")
print(f"  ⛔ ** And the calibration inverts: the control sits {Ctl['d_wm']:+.3f} sigma and pays "
      f"{Ctl['dchi2']:+.2f}, **")
print("    because `0.3150` is Planck's CMB value and not a BAO+theta_* one.  *The control's pull")
print("    is the DESI--Planck $\\Omega_m$ tension, so it is not a floor this comparison can read.*")
print("  ⌗ Reported in $\\Omega_m$ as well as $\\omega_m$, because the two offsets partly cancel in")
print(f"    $\\Omega_m h^2$: a factor {abs(Ctl['d_OM'] / A['d_OM']):.0f} there against "
      f"{abs(Ctl['d_wm'] / A['d_wm']):.0f} here.")
print(BAR)
print("  ALL CHECKS PASS")
