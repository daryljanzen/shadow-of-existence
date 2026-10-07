#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7199`'s STANDING QUESTION, TAKEN ON BANKED DATA AND ANSWERED IN THE NEGATIVE
WITH A REASON RATHER THAN A SHORTFALL.  THE SEPARATING MEASUREMENT IS RUNNABLE ON THE BANK -- IT IS
RUN HERE, NO NEW SPECTRUM -- AND ** THE PHASE SLOPE DOES NOT SEPARATE THE BARYON LOADING FROM THE
DRIVING. **  ALL FOUR BANKED PARAMETER DIRECTIONS MOVE IT BY THE SAME ORDER: EACH NEEDS A `$4$`--`$6$`
PER CENT MOVE TO CARRY THE OBSERVED DRIFT.  ⛔ AND THE TELL IS DECISIVE: `$n_s$` IS A PRIMORDIAL TILT
WITH NO ACOUSTIC PHASE IN IT AND IT MOVES THE STATISTIC AS MUCH AS `$\\omega_b$` DOES, AT EVERY DEGREE
OF MARGINALISATION THAT LEAVES THE STATISTIC INTACT -- SO THE FREE-PERIOD SLOPE IS NOT A PHASE
OBSERVABLE ON A ONE-AMPLITUDE-FITTED RESIDUAL, AND MARGINALISING THE GRADIENT NEVER OPENS THE
DIRECTIONS APART: PUSHED FAR ENOUGH IT BREAKS THE STATISTIC INSTEAD, `$n_s$` CHANGING SIGN THROUGH
ZERO AT DEGREE `$4$`. **

  ⇒ ** SO THE HONEST ANSWER IS THE ONE `r7199` ASKED FOR IF IT CAME: IT NEEDS A GRID, AND IT ALSO
  NEEDS A DIFFERENT STATISTIC. **  *Both halves are stated with what they would cost.*

  ⚠ ** `$n_s$` IS INHERITED AND IS USED ONLY AS A NULL PROBE, WHICH IS WHAT IT COSTS. **  *The
  corpus does not posit a six-parameter vector -- its difference from `$\Lambda$CDM` is carried by
  `$H(a)$` and a substrate -- so the spectral index is ADOPTED from `$\Lambda$CDM`'s own basis and
  derived from nothing this construction predicts.  No conclusion here is a claim about `$n_s$` or
  about the primordial spectrum: it is used because it is the one banked direction whose effect on
  the PEAK PHASE is known a priori to be nil, which is what a control for this statistic requires.*

  ⚠ ** THE CLEAN LEVER IS NOT IN THE BANK, AND THAT IS A FACT ABOUT THE BANK RATHER THAN A CHOICE
  HERE. **  *The instrument has `RBFAC`, which scales the baryon loading ONLY -- sound speed and
  baryon Euler inertia -- by its own documentation.  No banked spectrum records it.  What IS banked
  is `WBH2`, and `omega_b` also sets the free-electron density, so the `WB` direction moves the
  loading AND recombination together.  Even a discriminating `WB` result would have been two
  effects, and this one does not discriminate.*

** COMPUTES: the free-period slope `$k=2\\pi(1/P-1/\\ell_A)$` -- `cc66.153`'s own statistic, each
   configuration at ITS OWN banked `$\\ell_A$` -- on `$38$` banked spectra: the two nine-run
   derivative grids (`r7093_directions/grid_oneclock`, `r7095_directions/grid_licensed`, both arms,
   `base` and `H0`/`OM`/`NS`/`WB` either side) and the two `c54.193` driving-off spectra.  Validated
   first by reproducing `cc66.153`'s `$P=312.00$` and `$-96.6^\\circ$` from the banked whitened
   residual.  Then the smooth-gradient sweep, a polynomial in `$\\ell$` of degree `$0$`--`$4$`
   marginalised out of the whitened residual.  *** No new spectrum, no grid, nothing refitted. ***
   One amplitude per configuration, by the likelihood's own GLS, which is `chi2_of`'s convention. **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~60 s)
"""
import glob
import io
import os
import re
import sys

import numpy as np
import scipy.linalg

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
NPZ = os.path.join(BW, 'r7183_nofit_figure', 'nofit_figure_numbers.npz')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
GL = os.path.join(BW, 'r7095_directions', 'grid_licensed')
ND = {'lcdm': os.path.join(BW, 'spectra', 'c54.193_lcdm_nodrive_L3000.npz'),
      'cr': os.path.join(BW, 'spectra', 'c54.193_cr_nodrive_L3000.npz')}
for _p in [NPZ, GO, GL] + list(ND.values()):
    if not os.path.exists(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

F = np.load(NPZ)
L_FIG, L_A_FIG, ANCHOR = F['ell'], float(F['l_A']), float(F['peak1'])
LC, _FACB = CS.bin_center_and_fac()
GRID = np.arange(240.0, 400.0, 0.25)
LMAX_CUT = 1600.0           # 0.8 * LMAXL=2000, which is `chi2_of`'s own stated truncation rule
DEGS = (-1, 0, 1, 2, 3, 4)  # -1 = no smooth marginalisation

# the base values the two arms actually carry, read off the instrument's own defaults and the
# grids' own `switches` lines -- never recalled
BASEVAL = {'H0': {'cr': 68.60, 'lcdm': 67.40}, 'OM': {'cr': 0.2973, 'lcdm': 0.3150},
           'NS': {'cr': 0.965, 'lcdm': 0.965}, 'WB': {'cr': 0.0224, 'lcdm': 0.0224}}
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}
PARS = ('H0', 'OM', 'NS', 'WB')


# ============================================================ A. the statistic, validated
head("A.  THE STATISTIC IS `cc66.153`'s OWN, AND IT IS VALIDATED BEFORE IT IS EXTENDED")

_z0 = np.load(os.path.join(GL, 'cr_base.npz'), allow_pickle=True)
KEEP = (np.isfinite(CS.bin_spectrum(_z0['ls'], _z0['Dl']))
        & (CS.BIN_HI <= LMAX_CUT) & np.isin(LC, L_FIG))
LG = LC[KEEP]
COV = CS.COV_TT[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COV))
FISH = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(KEEP.sum())))
FISH = 0.5 * (FISH + FISH.T)
XS = (LG - LG.mean()) / (LG.max() - LG.min())

# the smooth null spaces, and the harmonic bases projected into each complement, once
QSM = {}
QHARM = {}
for _d in DEGS:
    QSM[_d] = (None if _d < 0
               else np.linalg.qr(np.array([LINV @ (XS ** j) for j in range(_d + 1)]).T)[0])
    mats = []
    for p in GRID:
        D = np.array([np.cos(2 * np.pi * (LG - ANCHOR) / p),
                      np.sin(2 * np.pi * (LG - ANCHOR) / p)]).T
        if QSM[_d] is not None:
            D = D - QSM[_d] @ (QSM[_d].T @ D)
        mats.append(np.linalg.qr(D)[0])
    QHARM[_d] = np.array(mats)


def best_period(w, deg=-1):
    """the period maximising the explained sum of squares, in the smooth basis's complement."""
    if QSM[deg] is not None:
        w = w - QSM[deg] @ (QSM[deg].T @ w)
    return float(GRID[np.argmax(np.sum(np.einsum('pnk,n->pk', QHARM[deg], w) ** 2, axis=1))])


def slope_of(path, deg=-1):
    """one amplitude by the likelihood's GLS, whiten, best period, slope at this file's own l_A."""
    z = np.load(path, allow_pickle=True)
    m = CS.bin_spectrum(z['ls'], z['Dl'])[KEEP]
    d = CS.X_DATA[KEEP]
    a = float((m @ FISH @ d) / (m @ FISH @ m))
    w = LINV @ (a * m - d)
    p = best_period(w, deg)
    return 2 * np.pi * (1.0 / p - 1.0 / float(z['l_A'])), p, a


# the validation: cc66.153's own footing, cc66.153's own vector, cc66.153's own numbers
_selfull = np.ones(len(L_FIG), dtype=bool)
_QF = []
for p in GRID:
    _D = np.array([np.cos(2 * np.pi * (L_FIG - ANCHOR) / p),
                   np.sin(2 * np.pi * (L_FIG - ANCHOR) / p)]).T
    _QF.append(np.linalg.qr(_D)[0])
_QF = np.array(_QF)
_wf = F['nofit_cr_whitened']
_Pf = float(GRID[np.argmax(np.sum(np.einsum('pnk,n->pk', _QF, _wf) ** 2, axis=1))])
_kf = 2 * np.pi * (1.0 / _Pf - 1.0 / L_A_FIG)
_ddf = np.degrees(_kf * (L_FIG.max() - L_FIG.min()))
print(f"      on cc66.153's own 179-bin footing: P = {_Pf:.2f}, slope = {_kf:+.4e}, "
      f"drift = {_ddf:+.1f} deg")

# ⛭ THE PAPER'S OWN FIGURES ARE READ FROM THE PAPER, NOT HARD-CODED.  `sec:refit-bound` carries this
#   drift in print; a receipt that pins it as a literal goes on passing after the sentence moves.
TEX = io.open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
_PAT = {'period': r'A period of \$([0-9]+)\$, and \$\\ell_\{A\}\$ with a phase',
        'drift': r'drift of the acoustic phase at the correct spacing\}, \$-([0-9.]+)\^\{\\circ\}\$',
        'window': r'across \$([0-9]+)\\le\\ell\\le([0-9]+)\$'}
_GOT = {k: re.search(v, TEX) for k, v in _PAT.items()}
if not all(_GOT.values()):
    print("  ⛔ THE PAPER'S OWN FIGURES NO LONGER READ OUT OF `sec:refit-bound`: "
          f"{[k for k, v in _GOT.items() if not v]}.  The sentence moved; this receipt is stale "
          "rather than passing.")
    sys.exit(1)
P_PAPER = float(_GOT['period'].group(1))
D_PAPER = -float(_GOT['drift'].group(1))
W_PAPER = (float(_GOT['window'].group(1)), float(_GOT['window'].group(2)))
print(f"      and READ from `corpus/CR_cosmology.tex` rather than pinned: the paper prints a period "
      f"of {P_PAPER:.0f}, a drift of {D_PAPER:+.1f} deg, over ell {W_PAPER[0]:.0f}-{W_PAPER[1]:.0f}")
check("Ⓐ①  the slope statistic reproduces the figures `sec:refit-bound` ITSELF prints -- the period "
      "and the drift both CAPTURED from the paper rather than hard-coded here, so this check goes "
      "red if that sentence moves instead of going on passing -- which makes what follows an "
      "EXTENSION of the section's own statistic and not a new one",
      abs(_Pf - P_PAPER) < 1e-9 and abs(_ddf - D_PAPER) < 0.1
      and abs(L_FIG.min() - W_PAPER[0]) < 5.0 and abs(L_FIG.max() - W_PAPER[1]) < 5.0)

_sg = np.isin(L_FIG, LG)
K_OBS = 2 * np.pi * (1.0 / best_period(F['nofit_cr_whitened'][_sg]) - 1.0 / L_A_FIG)
print(f"      the grid can reach {int(KEEP.sum())} bins, ell {LG.min():.0f}-{LG.max():.0f} "
      f"(cut at 0.8*LMAXL = {LMAX_CUT:.0f}, `chi2_of`'s own rule)")
print(f"      the OBSERVED slope re-measured on that same footing: {K_OBS:+.4e} "
      f"against {_kf:+.4e} on the full one -- {abs(K_OBS / _kf - 1) * 100:.1f} per cent apart")
check("Ⓐ②  ** and the observed slope is re-measured on the SAME footing the grid can reach, rather "
      "than compared across windows. **  The two agree to better than 3 per cent, so the footing "
      "change is not what any conclusion below rests on",
      abs(K_OBS / _kf - 1) < 0.03 and int(KEEP.sum()) > 150)


# ============================================================ B. what the bank actually carries
head("B.  THE BANKED LEVERS, READ OFF THE BANK'S OWN `switches` -- AND THE ONE THAT IS MISSING")

_allnpz = sorted(glob.glob(os.path.join(ROOT, 'computations', '**', '*.npz'), recursive=True))
_nsw, _ncfg, _nrb, _nnd = 0, 0, 0, 0
for _f in _allnpz:
    try:
        _z = np.load(_f, allow_pickle=True)
    except Exception:
        continue
    _k = set(_z.files)
    if 'switches' in _k:
        _nsw += 1
        _s = str(_z['switches'])
        if 'RBFAC' in _s:
            _nrb += 1
        if 'NODRIVE' in _s:
            _nnd += 1
    if 'config' in _k:
        _ncfg += 1
print(f"      {len(_allnpz)} banked .npz under computations/;  {_nsw} carry a `switches` line, "
      f"{_ncfg} a `config`")
print(f"      of the {_nsw} that record their switches, {_nrb} name `RBFAC` and {_nnd} name "
      f"`NODRIVE`")
check("Ⓑ①  ** `RBFAC` -- the lever that scales the baryon LOADING alone -- appears in NO banked "
      "spectrum's recorded switches. **  So the loading cannot be moved on banked data without "
      "also moving recombination, and that is a property of the bank rather than a choice here",
      _nrb == 0 and _nsw >= 18)

_sw = {}
for _f in sorted(glob.glob(os.path.join(GO, '*.npz'))) + sorted(glob.glob(os.path.join(GL, '*.npz'))):
    _z = np.load(_f, allow_pickle=True)
    _sw[_f] = str(_z['switches']) if 'switches' in _z.files else ''
_wbvals = sorted({t.split('=')[1] for s in _sw.values() for t in s.split() if t.startswith('WBH2=')})
_nsvals = sorted({t.split('=')[1] for s in _sw.values() for t in s.split() if t.startswith('NS=')})
print(f"      the grids' own `WBH2` values: {_wbvals};   their own `NS` values: {_nsvals}")
check("Ⓑ②  and the two banked grids DO carry a baryon-sector lever and a tilt lever, captured from "
      "their own switches rather than assumed: `WBH2` either side of the default and `NS` either "
      "side of it, which is what makes the comparison in `PART D` possible at all",
      _wbvals == ['0.0216', '0.0232'] and _nsvals == ['0.945', '0.985'])

_ndk = {}
for _a, _p in ND.items():
    _ndk[_a] = slope_of(_p)
    print(f"      driving OFF, {_a:4s}: l_A = {float(np.load(_p)['l_A']):.3f}, "
          f"P = {_ndk[_a][1]:.2f}, slope = {_ndk[_a][0]:+.4e}")
check("Ⓑ③  and the DRIVING lever is banked, as the two `c54.193` driving-off spectra, one per arm "
      "-- so both of the two candidates named at `cc66.153` have some banked lever, which is why "
      "this was worth running before asking for a grid",
      all(np.isfinite(v[0]) for v in _ndk.values()))


# ============================================================ C. the derivative table
head("C.  THE PHASE-SLOPE DERIVATIVE, EVERY BANKED DIRECTION, BOTH ARMS, BOTH GRIDS")

RES = {}
for gname, gdir in (('oneclock', GO), ('licensed', GL)):
    for arm in ('cr', 'lcdm'):
        kb = slope_of(os.path.join(gdir, f'{arm}_base.npz'))[0]
        RES[(gname, arm, 'base')] = kb
        for par in PARS:
            km = slope_of(os.path.join(gdir, f'{arm}_{par}m.npz'))[0]
            kp = slope_of(os.path.join(gdir, f'{arm}_{par}p.npz'))[0]
            dkdln = (kp - km) / (2 * STEP[par]) * BASEVAL[par][arm]
            RES[(gname, arm, par)] = (km, kp, dkdln, (K_OBS - kb) / dkdln)

print(f"      {'grid':9s} {'arm':5s} {'par':3s} {'k(-)':>11s} {'k(+)':>11s} {'dk/dln(th)':>12s} "
      f"{'move for k_obs':>15s}")
for gname in ('oneclock', 'licensed'):
    for arm in ('cr', 'lcdm'):
        for par in PARS:
            km, kp, dkdln, need = RES[(gname, arm, par)]
            print(f"      {gname:9s} {arm:5s} {par:3s} {km:+11.4e} {kp:+11.4e} {dkdln:+12.4e} "
                  f"{need * 100:+14.1f} %")

_need_oc = {p: abs(RES[('oneclock', 'cr', p)][3]) for p in PARS}
_need_lc = {p: abs(RES[('oneclock', 'lcdm', p)][3]) for p in PARS}
print(f"      CR  (oneclock), fractional move needed: "
      + ", ".join(f"{p} {_need_oc[p] * 100:.1f}%" for p in PARS))
print(f"      LCDM          , fractional move needed: "
      + ", ".join(f"{p} {_need_lc[p] * 100:.1f}%" for p in PARS))
_spread_oc = max(_need_oc.values()) / min(_need_oc.values())
_spread_lc = max(_need_lc.values()) / min(_need_lc.values())
print(f"      ⇒ spread between the most and least responsive direction: "
      f"CR {_spread_oc:.2f}x, LCDM {_spread_lc:.2f}x")
check("Ⓒ①  ** THE PHASE SLOPE DOES NOT SINGLE OUT A CARRIER: all four banked directions need a "
      "4-6 per cent move to produce the observed drift, and the most responsive beats the least by "
      "under a factor of two on either arm. **  A statistic that four unrelated parameters move "
      "equally is not identifying one of them",
      all(0.02 < v < 0.08 for v in _need_oc.values())
      and all(0.02 < v < 0.08 for v in _need_lc.values())
      and _spread_oc < 2.0 and _spread_lc < 2.0)

_lc_oc = [RES[('oneclock', 'lcdm', p)][:2] for p in PARS]
_lc_li = [RES[('licensed', 'lcdm', p)][:2] for p in PARS]
check("Ⓒ②  and the control's nine spectra are the SAME in both grids, which the numbers show "
      "rather than the provenance claiming it -- `LEAFGEOM` is an arm-only choice, so every "
      "control slope is identical across the two grids to the last bit",
      all(a[0] == b[0] and a[1] == b[1] for a, b in zip(_lc_oc, _lc_li)))

_cr_oc = {p: abs(RES[('oneclock', 'cr', p)][3]) for p in PARS}
_cr_li = {p: abs(RES[('licensed', 'cr', p)][3]) for p in PARS}
print(f"      and the ARM's own response is convention-dependent: the licensed grid needs "
      + ", ".join(f"{p} {_cr_li[p] * 100:.0f}%" for p in PARS))
check("Ⓒ③  ⛔ ** AND A SECOND REASON NOT TO NAME A CARRIER: the arm's response is not robust to the "
      "arm's own geometry convention. **  The licensed grid asks for several times the move the "
      "one-clock grid does on the same directions -- so even the SIZE of the response is a "
      "statement about `LEAFGEOM` versus `LEAFREC` and not about the physics",
      max(_cr_li[p] / _cr_oc[p] for p in PARS) > 2.5)


# ============================================================ D. the tell
head("D.  THE TELL, AND IT IS DECISIVE: A PRIMORDIAL TILT MOVES IT AS MUCH AS THE BARYON DENSITY")

print("      ⚠ `n_s` IS AN INHERITED QUANTITY AND IS USED HERE ONLY AS A NULL PROBE.  The corpus does")
print("      not posit a six-parameter vector -- its difference from LambdaCDM is carried by H(a) and")
print("      a substrate -- so the spectral index is ADOPTED from LambdaCDM's own basis and is not")
print("      derived from anything this construction predicts.  ** What that costs is stated: no")
print("      conclusion here is a claim about n_s or about the primordial spectrum. **  It is used")
print("      because it is the one banked direction whose effect on the PEAK PHASE is known a priori")
print("      to be nil, which is exactly what a control for this statistic requires.")
print()
print("      `n_s` tilts the PRIMORDIAL spectrum.  It carries no acoustic phase: it cannot move the")
print("      peak positions relative to the sound horizon, because it multiplies the initial power")
print("      and the transfer function is untouched.  If it moves this statistic as much as the")
print("      baryon density does, the statistic is reading smooth spectral gradient and not phase.")
print()
print(f"      {'deg':>4s} {'k_obs':>11s} {'k_base':>11s} "
      + "".join(f"{p:>11s}" for p in PARS) + f"{'NS/WB':>9s}")
SWEEP = {}
for deg in DEGS:
    ko = 2 * np.pi * (1.0 / best_period(F['nofit_cr_whitened'][_sg], deg) - 1.0 / L_A_FIG)
    kb = slope_of(os.path.join(GO, 'cr_base.npz'), deg)[0]
    row = {}
    for par in PARS:
        km = slope_of(os.path.join(GO, f'cr_{par}m.npz'), deg)[0]
        kp = slope_of(os.path.join(GO, f'cr_{par}p.npz'), deg)[0]
        dkdln = (kp - km) / (2 * STEP[par]) * BASEVAL[par]['cr']
        row[par] = (ko - kb) / dkdln if dkdln != 0 else np.nan
    SWEEP[deg] = row
    _ratio = abs(row['NS']) / abs(row['WB'])
    print(f"      {('none' if deg < 0 else str(deg)):>4s} {ko:+11.4e} {kb:+11.4e} "
          + "".join(f"{row[p] * 100:+10.1f}%" for p in PARS) + f"{_ratio:9.2f}")

INTACT = tuple(d for d in DEGS if d < 4)   # degree 4 breaks the statistic -- established below
_ratios = {d: abs(SWEEP[d]['NS']) / abs(SWEEP[d]['WB']) for d in DEGS}
print(f"      ⇒ the NS/WB ratio of required moves, over the {len(INTACT)} treatments that leave "
      f"the statistic intact: {min(_ratios[d] for d in INTACT):.2f} to "
      f"{max(_ratios[d] for d in INTACT):.2f}   (degree 4: {_ratios[4]:.2f}, and `PART D2` is why "
      f"that one is a breakdown rather than a separation)")
check("Ⓓ①  ** `n_s` AND `omega_b` ASK FOR THE SAME MOVE, WITHIN A FACTOR THIS STATISTIC CANNOT "
      "USE -- at every degree of marginalisation that leaves the statistic intact, and in the same "
      "DIRECTION at all of them. **  The tilt has no acoustic phase in it, so this is not two "
      "physical carriers agreeing: it is the statistic failing to isolate phase",
      all(1.0 < _ratios[d] < 2.2 for d in INTACT)
      and all(SWEEP[d]['NS'] < 0 and SWEEP[d]['WB'] < 0 for d in INTACT))

_sp = {d: max(abs(SWEEP[d][p]) for p in PARS) / min(abs(SWEEP[d][p]) for p in PARS) for d in DEGS}
print(f"      and the spread across all four directions, by degree: "
      + ", ".join(f"{('none' if d < 0 else d)}:{_sp[d]:.2f}x" for d in DEGS))
print(f"      ⌗ degree 4's spread is the LARGEST ({_sp[4]:.2f}x) and that is NOT discrimination: "
      f"`NS` passes through zero there")
print(f"        and changes sign (+{SWEEP[4]['NS'] * 100:.1f} per cent against "
      f"{SWEEP[3]['NS'] * 100:+.1f} at degree 3), so the ratio is a small denominator")
check("Ⓓ②  ⛔ ** AND MARGINALISING THE GRADIENT NEVER OPENS THE DIRECTIONS APART -- IT BREAKS THE "
      "STATISTIC. **  Through degree 3 every direction keeps its sign and its 2-6 per cent size; "
      "at degree 4 all four fall under 2.5 per cent and `n_s` CHANGES SIGN, which is the harmonic "
      "pair going degenerate with the smooth basis.  *The wider spread there is `n_s` crossing "
      "zero, not a carrier emerging -- read as discrimination it would be exactly backwards.*",
      max(abs(SWEEP[4][p]) for p in PARS) < 0.025
      and SWEEP[4]['NS'] > 0 and all(SWEEP[d]['NS'] < 0 for d in INTACT)
      and _sp[4] > max(_sp[d] for d in INTACT))


# ============================================================ E. the driving-off limit
head("E.  AND THE DRIVING-OFF LIMIT GOES THE WRONG WAY, WHICH IS A LIMIT AND NOT A DERIVATIVE")

for arm in ('cr', 'lcdm'):
    k, p, _a = _ndk[arm]
    print(f"      {arm:5s} driving OFF: P = {p:.2f}, slope = {k:+.4e}  against an observed "
          f"{K_OBS:+.4e}")
_wrongsign = all(_ndk[a][0] * K_OBS < 0 for a in ('cr', 'lcdm'))
_small = max(abs(_ndk[a][0]) for a in ('cr', 'lcdm')) / abs(K_OBS)
print(f"      ⇒ both driving-off slopes have the OPPOSITE sign to the observed one, and the larger "
      f"is {_small:.2f} of its magnitude")
check("Ⓔ①  ** removing the driving entirely does not produce the observed drift: it moves the "
      "slope the other way and by a third of the size. **  So the driving is not carrying it in "
      "the direction the residual needs -- stated as the limit it is, since `NODRIVE` is a total "
      "removal and not a derivative, and these two spectra are a different vintage from the grids",
      _wrongsign and _small < 0.45)


# ============================================================ F. the verdict and the cost
head("F.  SO IT NEEDS A GRID AND A DIFFERENT STATISTIC, AND BOTH ASKS ARE COSTED")

print("      WHAT WOULD SEPARATE THEM, and why it is not the slope of a global sinusoid:")
print("        * the DRIVING shifts every peak the same way relative to the sound horizon -- a")
print("          COMMON offset in ell_n / ell_A across the peaks;")
print("        * the LOADING acts on the ODD-EVEN alternation, which is the sector's own measured")
print("          mechanism at `g2/g1` -- the control at R=0 gives 1.065 against 0.897 at the")
print("          physical loading, already banked in `PO13`.")
print("      ⇒ Those two signatures are ORTHOGONAL on the peak positions and degenerate in a single")
print("        global period.  The statistic has to be the peak set, not one sinusoid.")
print()
print("      THE COST, in the grids' own units rather than guessed:")
print("        * the statistic: peak positions and their odd-even decomposition on the whitened")
print("          residual -- NO new spectrum, it is a re-read of what is already banked;")
print("        * the clean lever: `RBFAC` at a few values on BOTH arms, because `RBFAC` moves the")
print("          loading without moving recombination and `WBH2` cannot. Eight runs at the grids'")
print("          own configuration (`HIER=1 LMAXL=2000 LSTEP=8 ZSTART=3e7`, KFAC at the corpus")
print("          default 2.0, NK not reduced) -- comparable to ONE of the two nine-run arm grids")
print("          already banked, and idempotent and resumable on output existence as those were.")
check("Ⓕ①  ** the separating measurement was runnable on banked data and it is run here, so the "
      "ask for a grid is a measured conclusion and not an opening position. **  38 banked spectra "
      "read, both candidates exercised, the statistic validated against the section's own numbers "
      "first -- and it still does not separate them",
      int(KEEP.sum()) > 150 and len(RES) == 20 and abs(_Pf - 312.00) < 1e-9)
check("Ⓕ②  and what is asked for is bounded rather than open: one re-read of the bank for the "
      "statistic, and eight instrument runs for the lever the bank does not carry -- named "
      "against the nine-run grids already in tree, which is the only cost unit this sector has "
      "measured",
      _nrb == 0 and _wbvals == ['0.0216', '0.0232'])

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE SEPARATING MEASUREMENT IS RUNNABLE ON THE BANK, IT IS RUN, AND IT DOES NOT")
print("    SEPARATE THE LOADING FROM THE DRIVING. **  All four banked directions need a 4-6 per")
print("    cent move to carry the observed drift, and the most responsive beats the least by under")
print("    a factor of two on either arm.")
print("  ⛔ ** AND THE REASON IS DIAGNOSTIC RATHER THAN A SHORTFALL OF PRECISION: `n_s` MOVES IT AS")
print("    MUCH AS `omega_b` DOES, AT EVERY DEGREE OF SMOOTH MARGINALISATION. **  A primordial tilt")
print("    carries no acoustic phase, so the free-period slope is not a phase observable on a")
print("    one-amplitude-fitted residual -- and taking out the gradient never opens the four")
print("    directions apart. Pushed to degree 4 it breaks the statistic instead: every required")
print("    move falls under 2.5 per cent and `n_s` changes sign through zero.")
print("  ⌗ Two further reasons not to name a carrier on this statistic: the arm's response is")
print("    convention-dependent (the licensed grid asks several times the one-clock grid's move on")
print("    the same directions), and the driving-off limit moves the slope the WRONG WAY at a third")
print("    the magnitude.")
print("  ⇒ ** SO: IT NEEDS A GRID, AND IT ALSO NEEDS A DIFFERENT STATISTIC. **  The peak set with")
print("    its odd-even decomposition separates the two signatures that one global period makes")
print("    degenerate, and that half is a re-read of the bank at no run cost. The lever half is")
print("    eight runs, because `RBFAC` moves the loading alone and appears in NO banked spectrum,")
print("    while `WBH2` moves the loading and recombination together.")
print("  ⚠ Named and not supplied: `NODRIVE` is a total removal rather than a derivative and its")
print("    two spectra are a different vintage from the grids, so `PART E` is a limit and not a")
print("    gradient; and the `WB` direction was never a clean loading lever, so even a")
print("    discriminating `WB` result would have been two effects.")
