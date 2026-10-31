#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:refit-bound`: ** THE $1.57\times$ STILL HAS NO PARAMETER ADDRESS -- THE ARM OF
RECORD'S TT-PREFERRED $\omega_m$ STAYS INSIDE THE DISTANCE CONSTRAINT'S OWN WIDTH AND THE BAO FIT
PAYS ONLY $+0.524$ IN $\chi^2$ AT IT -- BUT IT NO LONGER SITS *ON* ITS BAO MINIMUM: $-0.673\sigma$
OFF IT, ABOUT FIFTEEN TIMES THE NAMESAKE ARM'S DISPLACEMENT AND FIFTY-TWO TIMES ITS PENALTY. **

*** AND THE CALIBRATION NO LONGER INVERTS CLEANLY -- IT SPLITS BY VARIABLE. IN $\omega_m$ THE ARM IS
$2.96\times$ FURTHER OUT THAN THE CONTROL; IN $\Omega_m$ THE CONTROL IS $2.09\times$ FURTHER; IN
$\chi^2$ THE CONTROL STILL PAYS $28.7\times$ MORE. THE NAMESAKE'S `FIVE TIMES AND $1700$ TIMES` IS
A STATEMENT ABOUT THE NAMESAKE ARM ALONE. ***

⌗ ** AND THE FILE'S NAME CARRIES THE NAMESAKE ARM'S READING. **  `..._sits_on_its_own_bao_minimum_`
was true of the namesake arm and is NOT true of the arm of record; the name's second half,
`..._while_the_controls_pays_fifteen_in_chi2_to_leave_planck`, holds exactly, at $+15.058$.  *A
registered receipt's name is not this seat's to change -- routed to 69 with the landing table.*

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
  CR arm,  TT minimum      68.5707   0.2912   0.136942   0.02164   1.0151     1.609

  *The arm's TT row is the ARM OF RECORD's (`LEAFREC=1`).  The namesake arm's was
  $(68.5811,\,0.2972,\,0.139788,\,0.02152,\,0.9980)$ at $1.581$ per bin -- every figure in it moved,
  and the tilt moved by $1.7$ per cent.*

  *The last column is the 185-bin refit receipt's own -- `r6825+cc66.25` for the control, `cc66.68`
  for the arm of record -- verified in each by real runs ($186.510$ and $297.668$ on $185$ bins);
  this file does not re-score the spectra and does not assert it.  Everything else is measured here.*

*** $\sigma(\omega_m) = 0.004543$ from DESI DR2 BAO on the arm's own ruler, ** UNMOVED by the
re-point **: the BAO likelihood never imports the instrument, so it cannot see `LEAFREC`, and both
minima and both widths in PARTS 2 and 3 come back unchanged.  *The whole of the move below is in the
TT fit and none of it is in the constraint that move is measured against.*  The arm's TT minimum
sits $-0.673\sigma$ from its BAO minimum and pays $\Delta\chi^2_{\rm BAO} = +0.524$.  The control's
sits $+0.227\sigma$ and pays $+15.058$. ***

⇒ ** SO THE RESIDUAL IS STILL NOT A PARAMETER -- ON A WEAKER FOOTING THAN THE NAMESAKE'S. **  *The
TT fit, given the expansion rate, both densities and the tilt free, lands two-thirds of a standard
deviation from where the distance data put the background: INSIDE the constraint's own width, at a
cost of half a unit of $\chi^2$ on thirteen measurements.  So the TT-preferred $\omega_m$ is still
ADMISSIBLE to the distance data, and the `$1.57\times$` is still what remains when the parameters
have been given away.*  ⛔ *What does NOT survive is `lands where the distance data already put the
background and leaves it there`.  It moves: $2.04$ per cent in $\Omega_m$, $2.12$ in $\omega_m$, and
from a fiftieth of the constraint's width to two-thirds of it -- a factor of $33.8$.*  ⌈ *The answer
`r7181` named as the more interesting one still comes.  It comes with a displacement attached.*

⛔ ** AND THE ORDER'S CALIBRATION PREMISE IS FALSE, MEASURABLY -- BUT NO LONGER IN ONE DIRECTION. **
*`r7181` reads the control's displacement as the floor -- "it fits everything, so its pull should be
small".*  **It is no floor: it pays $28.7$ times the arm's $\chi^2$ penalty and sits $2.09$ times
further out in $\Omega_m$**, because `$0.3150$` is not a BAO$+\theta_*$ value at all: *it is
Planck's CMB-fitted $\Omega_m$, and DESI DR2 BAO on the control's own ruler prefers
$0.2971 \pm 0.0085$.*  ⇒ ** The control's pull is the known DESI--Planck $\Omega_m$ tension, not a
floor this comparison can read. **  *Its TT refit moves it $3$ in $\chi^2$ TOWARD DESI and leaves it
$15$ away.*  ⌗ **In $\omega_m$, though, the ARM is now the more displaced of the two, by $2.96$ --
so the premise fails in $\Omega_m$ and in $\chi^2$, and its CONCLUSION reverses in $\omega_m$.**

⌗ ** AND ON THE ARM OF RECORD THE TWO VARIABLES DISAGREE ON WHICH ARM IS DISPLACED. **  *In
$\Omega_m$ the control's TT minimum is $+1.498\sigma$ out and the arm's $-0.716\sigma$ -- the
CONTROL further, by $2.09$.  In $\omega_m$ it is $+0.227$ against $-0.673$ -- the ARM further, by
$2.96$, because the control's TT $H_0$ sits BELOW its BAO $H_0$ while its $\Omega_m$ sits above and
the two offsets partly cancel in $\Omega_m h^2$.*  **On the namesake arm both orderings agreed, by
$5$ and by $94$; on this one they do not.**  ⌈ *That is visible only because this file reports both.
The safeguard was put here against `r7181`'s choice of variable, and it is what caught this: in
$\omega_m$ alone the arm of record reads as a clean inversion of this file's own headline, and in
$\Omega_m$ alone as a confirmation of it.*

===================================================================================================
** WHAT IS READ RATHER THAN RUN, AND WHAT IS CHECKED BEFORE IT IS USED **
===================================================================================================

  ** THE TT MINIMA ARE READ OFF THE BANKED ARTEFACTS, NOT QUOTED. **  The control's parameters come
  from `refit_grid185/verify.sh`.  ** The arm of record's grid has NO launcher file and no
  `verify_*.npz` at all ** -- `refit_grid185_leafrec1_distances/` carries eight stencil spectra and
  a base -- so its verification point is read from `spectra/cc66_r185_verify_cr_leafrec1.npz`, whose
  manifest carries the launcher command verbatim in `switches` AND the same point structurally in
  `point`.  ** Both halves are read and required to agree before either is used **, which is a check
  the control's single launcher file cannot be given.  This receipt then puts the captured
  parameters back through `ACOUSTIC_two_arm` -- with `LEAFREC=1` for the arm -- and requires the
  instrument's own `D_M`, `r_s` and `l_A` to reproduce what each bank STORES to a part in $10^7$,
  so each minimum is established from the artefact that came back.  *A record this file cannot parse
  REFUSES (exit 1) rather than being guessed at.*

  ⛭⛭⛭ ** AND THAT TRIPLE IS BLIND TO THE ARM, WHICH THIS FILE MEASURES RATHER THAN ASSUMES. **  The
  arm is run a SECOND time at the same point with `LEAFREC=0`: $D_M$, $r_s$ and $l_A$ come back
  BIT-IDENTICAL, because the leaf record acts on recombination's rate and not on the expansion
  history this point's ruler is built from.  *So the background identity check establishes the
  PARAMETERS and cannot establish the ARM -- which is the re-key's own failure mode, where reading
  the wrong key returns the namesake silently.*  ⇒ ** The arm's identity rests instead on the
  instrument's RESOLVED switch snapshot, which agrees with the bank's stored `config` on all seven
  model-defining switches and on the instrument's source hash, and which the `LEAFREC=0` run differs
  from on exactly `LEAFREC`. **  ⌗ *The instrument's own comment names this case: the `__SWITCHES__`
  line records only what the environment SET, and `LEAFREC` now DEFAULTS to on -- so a record of
  what was typed could not have settled this and the resolved snapshot can.  The control's bank
  predates that ratchet and carries no `config`, so the check exists on the arm and not on the
  control: an asymmetry in the banks, recorded here rather than smoothed over.*

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

** COMPUTES: the two refit minima with their omega_m, a THIRD background run at LEAFREC=0 to
   measure what the banked background can and cannot see of the arm, the BAO minimum and profiled
   Delta-chi^2 = 1 width on each arm's own ruler, the TT displacement in omega_m and in Omega_m,
   and the chi^2 the distance data pays at each TT minimum. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~5 s measured)
"""
import contextlib
import importlib.util
import io
import json
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
# ⛭ THE ARM OF RECORD HAS NO LAUNCHER FILE.  `refit_grid185_leafrec1_distances/` carries the eight
#   stencil spectra and a base, and NO `verify.sh` and no `verify_*.npz`.  Its verification point is
#   banked as `spectra/cc66_r185_verify_cr_leafrec1.npz`, whose manifest carries the launcher
#   command verbatim in `switches` AND the same point structurally in `point`.  Both are read and
#   required to agree below, so a manifest whose two halves have drifted apart refuses rather than
#   being believed.  The control's launcher is still its own `verify.sh`.
VSH = open(os.path.join(G185, 'verify.sh'), encoding='utf-8').read()
ARMNPZ = os.path.join(BW, 'spectra', 'cc66_r185_verify_cr_leafrec1.npz')
try:
    _MF = json.loads(str(np.atleast_1d(np.load(ARMNPZ, allow_pickle=True)['manifest'])[0]))
    VSH_ARM, _PT = _MF['switches'], _MF['point']
except Exception:
    VSH_ARM, _PT = '', {}
LAUNCH = {
    'lcdm': r"verify_lcdm\s+ARM=lcdm LH0=([0-9.]+) LOM=([0-9.]+) WBH2=([0-9.]+) NS=([0-9.]+)",
    'cr': r"ARM=cr CRH0=([0-9.]+) CROM=([0-9.]+) HIER=1 LEAFREC=1 LEAFSCALES=1 LMAXL=2000 "
          r"LSTEP=8 NS=([0-9.]+) WBH2=([0-9.]+) ZSTART=(\S+)",
}
m_l = re.search(LAUNCH['lcdm'], VSH)
m_c = re.search(LAUNCH['cr'], VSH_ARM)
if not (m_l and m_c):
    print("  ⛔ REFUSED -- ** THE TWO VERIFICATION COMMANDS ARE NO LONGER CARRIED IN THE FORM THIS "
          "RECEIPT READS THEM. **  The control's comes from `refit_grid185/verify.sh`; the arm of "
          "record's from the `switches` field of `cc66_r185_verify_cr_leafrec1.npz`'s manifest, "
          "because that grid has no launcher file at all.  The best-fit parameters are the thing "
          "being reported, so a record this file cannot parse is not a record it may guess at. "
          " *Nothing is asserted.*")
    sys.exit(1)
TTMIN = {
    'lcdm': dict(H0=float(m_l.group(1)), OM=float(m_l.group(2)), WB=float(m_l.group(3)),
                 NS=float(m_l.group(4)), env=dict(ARM='lcdm', LH0=m_l.group(1), LOM=m_l.group(2),
                                                  WBH2=m_l.group(3))),
    'cr': dict(H0=float(m_c.group(1)), OM=float(m_c.group(2)), WB=float(m_c.group(4)),
               NS=float(m_c.group(3)), env=dict(ARM='cr', CRH0=m_c.group(1), CROM=m_c.group(2),
                                                ZSTART=m_c.group(5), LEAFSCALES='1', LEAFREC='1',
                                                WBH2=m_c.group(4))),
}
check("⓿ the arm of record's TWO independent records of its own launcher AGREE -- the `switches` "
      "string this file regex-captures and the structured `point` the same manifest carries give "
      f"the same four parameters ({TTMIN['cr']['H0']:.6f}, {TTMIN['cr']['OM']:.6f}, "
      f"{TTMIN['cr']['WB']:.6f}, {TTMIN['cr']['NS']:.6f}) and both say `LEAFREC=1` -- so a drifted "
      "manifest is caught BEFORE either half of it is used, which the control's single launcher "
      "file cannot be",
      all(abs(float(_PT[k]) - TTMIN['cr'][v]) < 1e-12
          for k, v in (('CRH0', 'H0'), ('CROM', 'OM'), ('WBH2', 'WB'), ('NS', 'NS')))
      and int(_PT.get('LEAFREC', 0)) == 1 and TTMIN['cr']['env'].get('LEAFREC') == '1')
# the BAO+theta_* background each arm starts from, as `sec:refit-bound` carries it
START = {'lcdm': dict(H0=67.4000, OM=0.3150, WB=0.0224, NS=0.9650),
         'cr': dict(H0=68.6000, OM=0.2973, WB=0.0224, NS=0.9650)}

KNOBS = ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'WBH2', 'NS', 'ZSTART', 'LEAFSCALES', 'NK',
         'LEAFGEOM', 'LEAFREC')
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
    TTMIN[tag]['RS'] = float(AT.R_S)
    TTMIN[tag]['LA'] = float(AT.L_A)
    TTMIN[tag]['snap'] = dict(AT._SWITCH_SNAPSHOT)
    z = np.load(ARMNPZ if tag == 'cr' else os.path.join(G185, f'verify_{tag}.npz'),
                allow_pickle=True)
    TTMIN[tag]['DM_banked'] = float(np.atleast_1d(z['D_M'])[0])
    TTMIN[tag]['rs_banked'] = float(np.atleast_1d(z['r_s'])[0])
    TTMIN[tag]['lA_banked'] = float(np.atleast_1d(z['l_A'])[0])
# ⛭⛭⛭ ** THE BANKED BACKGROUND CANNOT SEE THE SWITCH, AND THIS MEASURES THAT RATHER THAN ASSUMING
#   IT. **  The arm is run a SECOND time at the same point with `LEAFREC=0`.  If `D_M`, `r_s` and
#   `l_A` come back bit-identical, then no identity check on a banked background can establish which
#   arm was run -- the leaf record acts on recombination's rate, not on the expansion history this
#   point's ruler is built from -- and the arm of record's identity has to rest on the instrument's
#   own RESOLVED switch snapshot instead.  Both halves of that are gated below.
for k in KNOBS:
    os.environ.pop(k, None)
os.environ.update(TTMIN['cr']['env'])
os.environ['NK'] = '120'
os.environ['LEAFREC'] = '0'
spec = importlib.util.spec_from_file_location("ACOUSTIC_two_arm_cc144_cr_lr0", INSTR)
_AT0 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(_AT0)
_LR0 = dict(DM=float(_AT0.D_M), RS=float(_AT0.R_S), LA=float(_AT0.L_A),
            snap=dict(_AT0._SWITCH_SNAPSHOT))
for k, v in _saved.items():
    os.environ.pop(k, None)
    if v is not None:
        os.environ[k] = v

for tag, nm in (('lcdm', 'control (LCDM)'), ('cr', 'CR, crossing ')):
    t = TTMIN[tag]
    print(f"      {nm}  launcher ({t['H0']:.6f}, {t['OM']:.6f})  ->  instrument D_M = {t['DM']:.4f}"
          f"   banked D_M = {t['DM_banked']:.4f}   r_s = {t['rs_banked']:.4f}   "
          f"l_A = {t['lA_banked']:.4f}")
check("⛭⛭ the captured parameters reproduce ALL THREE of each bank's stored background quantities "
      "-- `D_M`, `r_s` and `l_A` -- to a part in 10^7, the control's parameters from its "
      "`verify.sh` and the arm of record's from its manifest's `switches`, so each TT minimum is "
      "established from the artefact that came back and not from the record of what was launched",
      all(abs(TTMIN[t]['DM'] / TTMIN[t]['DM_banked'] - 1.0) < 1e-7
          and abs(TTMIN[t]['RS'] / TTMIN[t]['rs_banked'] - 1.0) < 1e-7
          and abs(TTMIN[t]['LA'] / TTMIN[t]['lA_banked'] - 1.0) < 1e-7 for t in ('lcdm', 'cr')))

_BCFG = json.loads(str(np.atleast_1d(np.load(ARMNPZ, allow_pickle=True)['config'])[0]))
_MODEL = ('ARM', 'LEAFSCALES', 'LEAFREC', 'LEAFGEOM', 'STACKPERT', 'VISLEAF', 'NODRIVE')
_snap = TTMIN['cr']['snap']
_cagree = [k for k in _MODEL if k in _BCFG and _snap.get(k) == _BCFG[k]]
_moved = [k for k in _MODEL if _snap.get(k) != _LR0['snap'].get(k)]
_ctlfiles = np.load(os.path.join(G185, 'verify_lcdm.npz'), allow_pickle=True).files
print(f"      LEAFREC=0 at the same point:  D_M {_LR0['DM']:.4f}   r_s {_LR0['RS']:.4f}   "
      f"l_A {_LR0['LA']:.4f}   -- bit-identical: "
      f"{(_LR0['DM'], _LR0['RS'], _LR0['LA']) == (TTMIN['cr']['DM'], TTMIN['cr']['RS'], TTMIN['cr']['LA'])}")
check("⓿⓿ ** AND THE ARM OF RECORD'S IDENTITY RESTS ON THE INSTRUMENT'S OWN RESOLVED SNAPSHOT, "
      "BECAUSE NOTHING IN THE BANKED BACKGROUND CAN SEE THE SWITCH: ** run at this same point with "
      "`LEAFREC=0` the instrument returns `D_M`, `r_s` and `l_A` BIT-IDENTICAL, so the gate above "
      f"establishes the PARAMETERS and is blind to the ARM.  *What is not blind: this run's own "
      f"resolved snapshot agrees with the bank's stored `config` on all {len(_cagree)} "
      f"model-defining switches and on the instrument's source hash, and the `LEAFREC=0` run "
      f"differs from it on EXACTLY {_moved}.*  ⌗ `LMAXL` deliberately differs (this receipt "
      "evaluates the background only), and the CONTROL's bank predates the config ratchet and "
      "carries no `config` at all -- so this check exists on the arm and not on the control, which "
      "is an asymmetry in the banks and not in this file",
      (_LR0['DM'], _LR0['RS'], _LR0['LA'])
      == (TTMIN['cr']['DM'], TTMIN['cr']['RS'], TTMIN['cr']['LA'])
      and _moved == ['LEAFREC'] and len(_cagree) == 7
      and _snap.get('instrument_blob') == _BCFG.get('instrument_blob')
      and 'config' not in _ctlfiles)


def wm_of(d):
    return d['OM'] * (d['H0'] / 100.0) ** 2


print()
print(f"      {'':26s} {'H0':>10} {'Om':>9} {'w_m':>10} {'w_b':>9} {'n_s':>8}")
for tag, nm in (('lcdm', 'control'), ('cr', 'CR arm')):
    for lab, d in ((f'{nm}, start', START[tag]), (f'{nm}, TT minimum', TTMIN[tag])):
        print(f"      {lab:26s} {d['H0']:10.4f} {d['OM']:9.4f} {wm_of(d):10.6f} "
              f"{d['WB']:9.5f} {d['NS']:8.4f}")
_pA = abs(TTMIN['cr']['OM'] / START['cr']['OM'] - 1)
_pC = abs(TTMIN['lcdm']['OM'] / START['lcdm']['OM'] - 1)
check("⛔ ** THE PRE-CONSTRAINT ASYMMETRY THIS RECEIPT OPENED WITH IS GONE ON THE ARM OF RECORD: ** "
      f"the arm moves `Omega_m` by {_pA * 100:.3f}% against the control's {_pC * 100:.3f}% -- a "
      f"factor of {_pA / _pC:.3f} with the ARM the larger, where the namesake arm moved it by under "
      "a thirtieth of a per cent and the gate here asserted exactly that.  *Third independent "
      "appearance of the split: `cc66.68` 2.123% on 185 bins, `cc66.69` 2.16% on 132, and here it "
      "is this file's opening asymmetry rather than a line in a table.*",
      0.0203 < _pA < 0.0204 and 0.0164 < _pC < 0.0165 and 1.23 < _pA / _pC < 1.25)

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
check("⛭⛭⛭ ** THE ARM'S TT-PREFERRED `w_m` IS STILL ADMISSIBLE TO ITS OWN DISTANCE DATA -- it "
      f"sits INSIDE the constraint's own width ({A['d_wm']:+.4f} sigma) and the BAO fit pays only "
      f"{A['dchi2']:+.4f} in chi^2 at it, half a unit on thirteen measurements -- SO THE 1.57x IS "
      "STILL NOT A DISPLACEMENT OF THE MATTER DENSITY. **  *But it no longer sits ON the minimum: "
      "two-thirds of a standard deviation off it, about fifteen times the namesake arm's printed "
      "`0.046` sigma and fifty-two times the `+0.010` printed beside it.*  ⌗ Both of those denominators are "
      "the namesake's ROUNDED printed figures, so the two factors are QUOTED and deliberately NOT "
      "pinned; what is pinned is this arm's own two numbers, two-sided.",
      -0.675 < A['d_wm'] < -0.671 and 0.519 < A['dchi2'] < 0.530 and abs(A['d_wm']) < 1.0)
check("⛔⛔ ** AND THE CALIBRATION NO LONGER INVERTS CLEANLY -- IT SPLITS BY VARIABLE: ** in `w_m` "
      f"the ARM is {abs(A['d_wm'] / Ctl['d_wm']):.4f}x further out ({A['d_wm']:+.4f} against "
      f"{Ctl['d_wm']:+.4f}); in `Om` the CONTROL is {abs(Ctl['d_OM'] / A['d_OM']):.4f}x further "
      f"({Ctl['d_OM']:+.4f} against {A['d_OM']:+.4f}); and in chi^2 the CONTROL still pays "
      f"{Ctl['dchi2'] / A['dchi2']:.3f}x more ({Ctl['dchi2']:+.3f} against {A['dchi2']:+.4f}). "
      " *`r7181`'s calibration premise is still false -- the control's pull is not a floor -- but it "
      "is no longer false in ONE direction, and the namesake's `five times and 1700 times` is a "
      "statement about the namesake arm and not about this one.*",
      A['d_wm'] < 0 < Ctl['d_wm']
      and 2.95 < abs(A['d_wm'] / Ctl['d_wm']) < 2.97
      and 2.08 < abs(Ctl['d_OM'] / A['d_OM']) < 2.10
      and 28.6 < Ctl['dchi2'] / A['dchi2'] < 28.8)
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
_S = RES['CR arm, start']
check("⌗ the arm's START is still its own BAO minimum -- "
      f"{_S['d_wm']:+.4f} sigma, inside a fiftieth of the constraint's width, paying "
      f"{_S['dchi2']:+.4f} in chi^2 -- so the background the distances fix is unchanged by the "
      "re-point, as PARTS 2 and 3 above measure it to be",
      abs(_S['d_wm']) < 0.05 and abs(_S['dchi2']) < 0.01)
check("⛔ ** AND THE REFIT DOES PULL IT OFF, WHICH THIS GATE USED TO DENY WHILE PRINTING THE PROOF "
      f"BESIDE ITSELF: ** from {_S['d_wm']:+.4f} sigma to {A['d_wm']:+.4f}, a factor of "
      f"{abs(A['d_wm'] / _S['d_wm']):.3f}.  *The sentence here read \"so its refit had nowhere to be "
      "pulled to\" and printed both numbers, while its condition tested only the first -- the "
      "stale-label class, and the fifth instance found by reading a run rather than by any gate.*",
      33.6 < abs(A['d_wm'] / _S['d_wm']) < 34.0)

print()
print("      ⌗ the same two displacements in `Om`, where they do NOT partly cancel:")
print(f"        control TT minimum {Ctl['d_OM']:+.4f} sigma   CR arm TT minimum {A['d_OM']:+.4f} "
      f"sigma   -- the CONTROL further by {abs(Ctl['d_OM'] / A['d_OM']):.4f}x, where in `w_m` the "
      f"ARM is further by {abs(A['d_wm'] / Ctl['d_wm']):.4f}x")
check("⛔ ** THE TWO VARIABLES NOW DISAGREE ON WHICH ARM IS DISPLACED ** -- `w_m` says the arm, `Om` "
      "says the control -- where on the namesake arm both said the control, by 5 and by 94.  *That "
      "disagreement is visible ONLY because this receipt reports both: in `w_m` alone the arm of "
      "record would read as a clean inversion of this file's own headline, and in `Om` alone as a "
      "confirmation of it.  The safeguard was put here against the order's choice of variable and "
      "it is what caught this.*",
      abs(Ctl['d_wm']) < abs(A['d_wm']) and abs(Ctl['d_OM']) > abs(A['d_OM'])
      and 1.495 < Ctl['d_OM'] < 1.500 and -0.718 < A['d_OM'] < -0.713)

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** `sec:refit-bound`'S OWN PRINTED FIGURES, CAPTURED FROM THE PAPER **")
print(BAR)

# ⛭⛭ This receipt reads no paper anywhere else, and these captures exist for one reason: the four
#   figure groups `sec:refit-bound` prints for this comparison are the NAMESAKE arm's, and without a
#   capture they would go quietly stale against the arm of record.  Each is CAPTURED rather than
#   quoted, and a sentence reworded past the pattern FAILS here instead of leaving this part
#   asserting nothing -- the vacuity trap, which is worse than a red.
# ⚠ ** THIS PART IS EXPECTED TO GO RED WHEN 69 LANDS THE ARM-OF-RECORD FIGURES, BY DESIGN. **  It is
#   the signal that the landing happened, not a defect; the row is routed in `FOR_69.md`.
P15TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
_TEX = open(P15TEX, encoding='utf-8').read()
PAT = {
    'pct': r"moves by \$([0-9.]+)\\%\$ and its matter density by \$([0-9.]+)\\%\$",
    'sig': r"sits \$([0-9.]+)\$ of a standard deviation from",
    'chi': r"at a cost of \$([0-9.]+)\$ in \$\\chi\^\{2\}\$",
    'ns': r"arm prefers \$([0-9.]+)\$ against the control's \$([0-9.]+)\$, bluer by \$([0-9.]+)\$",
}
CAP = {k: re.search(v, _TEX) for k, v in PAT.items()}
check("⌗ all four of `sec:refit-bound`'s printed figure groups are still FOUND by this file's own "
      f"patterns -- {sorted(k for k, m in CAP.items() if m)} of {sorted(PAT)} -- so a sentence "
      "reworded past one of them reddens this part rather than emptying the set it ranges over",
      len(PAT) == 4 and all(CAP.values()))

if all(CAP.values()):
    _pH = abs(TTMIN['cr']['H0'] / START['cr']['H0'] - 1) * 100
    _pO = abs(TTMIN['cr']['OM'] / START['cr']['OM'] - 1) * 100
    _nsA, _nsC = TTMIN['cr']['NS'], TTMIN['lcdm']['NS']
    _cmp = {
        'H0_pct': (float(CAP['pct'].group(1)), _pH),
        'Om_pct': (float(CAP['pct'].group(2)), _pO),
        'sigma': (float(CAP['sig'].group(1)), abs(A['d_wm'])),
        'chi2': (float(CAP['chi'].group(1)), A['dchi2']),
        'ns_arm': (float(CAP['ns'].group(1)), _nsA),
        'ns_ctl': (float(CAP['ns'].group(2)), _nsC),
        'bluer': (float(CAP['ns'].group(3)), _nsA - _nsC),
    }
    print(f"      {'':10s} {'printed':>10} {'arm of record':>16} {'out by':>12}")
    for k, (p, m) in _cmp.items():
        print(f"      {k:10s} {p:10.6f} {m:16.6f} {abs(p - m):12.6f}"
              f"{'   AGREES' if abs(p - m) <= 5e-4 else ''}")
    _AGREE = sorted(k for k, (p, m) in _cmp.items() if abs(p - m) <= 5e-4)
    _OUT = sorted(k for k, (p, m) in _cmp.items() if abs(p - m) > 5e-4)
    check("⛔⛔ ** EVERY ARM-SIDE FIGURE `sec:refit-bound` PRINTS FOR THIS COMPARISON IS THE "
          f"NAMESAKE ARM'S, AND ONLY THE CONTROL'S TILT SURVIVES THE RE-POINT: ** out = {_OUT}, "
          f"agreeing = {_AGREE}.  *The paper's `0.031` per cent in `Omega_m` is the one that moves "
          f"furthest -- {_pO:.3f} per cent on the arm of record, sixty-six times it -- and its "
          f"`0.046 sigma` / `+0.010` pair becomes {abs(A['d_wm']):.4f} / {A['dchi2']:+.4f}.  The "
          "control's tilt is untouched because the re-point does not reach the control, which is "
          "the same partition `cc66.70`'s caption audit found on the figure bank.*",
          _AGREE == ['ns_ctl']
          and _OUT == ['H0_pct', 'Om_pct', 'bluer', 'chi2', 'ns_arm', 'sigma']
          and 0.0426 < _pH < 0.0428 and 2.035 < _pO < 2.038
          and 0.0607 < (_nsA - _nsC) < 0.0609)
    check("⌗ and the paper's two printed per-cent figures are the NAMESAKE arm's to three decimals, "
          "so this is a re-point and not a disagreement: the namesake moves `H0` by 0.0276 and "
          "`Omega_m` by 0.0306 per cent, which round to the printed 0.028 and 0.031",
          abs(abs(68.5811 / 68.6 - 1) * 100 - _cmp['H0_pct'][0]) < 5e-4
          and abs(abs(0.297209 / 0.2973 - 1) * 100 - _cmp['Om_pct'][0]) < 5e-4)

# =================================================================================================
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE $1.57\\times$ STILL HAS NO PARAMETER ADDRESS. **  The arm of record's TT minimum")
print(f"    sits {A['d_wm']:+.4f} sigma from its own BAO minimum in $\\omega_m$ and the BAO fit pays "
      f"{A['dchi2']:+.4f}")
print("    in $\\chi^2$ at it -- INSIDE the constraint's own width, half a unit on thirteen")
print("    measurements -- so the residual is still not a displacement of the matter density.")
print("  ⛔ ** But it no longer sits ON that minimum, and the file's name says it does. **  The")
print("    namesake arm sat $-0.046\\sigma$ out and paid the $+0.010$ the paper prints; this one")
print("    is fifteen and fifty-two times that, and moves $\\Omega_m$ by $2.04$ per cent where it moved")
print("    it by under a thirtieth of one -- the third appearance of that split today.")
print(f"  ⛔ ** And the calibration SPLITS BY VARIABLE: ** in $\\omega_m$ the arm is "
      f"{abs(A['d_wm'] / Ctl['d_wm']):.2f}x further")
print(f"    out ({A['d_wm']:+.4f} against {Ctl['d_wm']:+.4f}); in $\\Omega_m$ the control is "
      f"{abs(Ctl['d_OM'] / A['d_OM']):.2f}x further")
print(f"    ({Ctl['d_OM']:+.4f} against {A['d_OM']:+.4f}); in $\\chi^2$ the control still pays "
      f"{Ctl['dchi2'] / A['dchi2']:.1f}x more.")
print("    *So `r7181`'s premise is still false -- the control's pull is no floor -- but the")
print("    namesake's `five times and 1700 times` is a statement about the namesake arm alone.*")
print(BAR)
print("  ALL CHECKS PASS")
