#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE COMB'S RESOLUTION, MEASURED BEFORE IT IS ALLOWED TO DECIDE, AND THE
SKY'S OWN VALUE LIES OUTSIDE THE ADMISSIBLE FAMILY. **

** WHY IT EXISTS. **  `r6925+cc66.43` promoted the comb to arbiter between the two admissible clocks
for the optical depth: it is the only one of the three readings with an external referent, and it
supported the assignment the instrument has.  ⚠ *** But the corpus had never measured how sharply it
discriminates, and a reading promoted to arbiter needs its resolution stated before it decides
anything. ***  `r6929`'s order: let the weighting on $\tau$ run from the stacking clock to the leaf's
through a ONE-PARAMETER FAMILY -- `VISLEAF` as a fraction rather than a flag -- and report, against
that parameter, $\ell_1/\ell_A$ against the sky's $0.7312$, the retained fraction and its $q$-slope,
and $\mathrm dr_s/\mathrm d\chi$.

⛭⛭ ** EVERY READING IS LINEAR IN THE PARAMETER, AND THE COMB'S WHOLE RANGE IS FOUR MULTIPOLES. **
$\ell_1 = 221.93 + 4.21 f$ to within three hundredths of a multipole of a straight line, so the
family's entire span is $4.21$ multipoles -- $0.01395$ in $\ell_1/\ell_A$, which is $4.2$ times the
sky's own one-multipole locating width and $2.1$ times a two-multipole one.  *** The comb therefore
pins the assignment to $\Delta f \approx 0.24$: it separates the endpoints, and it does not come
close to fixing the clock. ***

⛔ ** AND THE ORDER'S FIRST BRANCH IS HALF RIGHT, WHICH IS THE PART WORTH HAVING. **  The contrast's
LEVEL is shallow as the order guessed -- $1.75\sigma$ across the family against the comb's $4.21$ --
but its $q$-SLOPE is not: $+0.01042 \to -0.00039$ is $3.80\sigma$ of its own fit error, statistically
the comb's equal.  *** What separates them is not steepness but that the contrast's error GROWS with
the parameter and the comb's does not: *** the band residual runs $0.0089 \to 0.0441$ and the slope's
standard error $0.00284 \to 0.01410$, a factor five each, because moving `ETA_LS` moves
$r_s(\mathrm{ETA\_LS})$ and a band ratio of two oscillations no longer aligned in $q$ reads their
phase mismatch -- `cc66.40`'s guard, firing a fourth time.  ** The comb's locating width is the same
at both ends. **

⛭⛭⛭ ** AND THE DECISIVE RESULT IS NOT ABOUT THE CHOICE AT ALL: THE SKY'S VALUE IS NOT IN THE FAMILY. **
$0.7312$ sits at $f = -0.304$ on the family's own straight line, on the far side of the stacking clock
-- so no interior fraction fits the comb better than the endpoint the instrument already uses (the
order's third branch does not arise), the best point in the family is $f=0$, and *** the residual
first-peak disagreement cannot be absorbed by the clock assignment, because the direction it would
need is not admissible. ***  ⚑ And $P_1/P_2$, a second external referent, says the same thing
independently: $2.141 \to 2.017$ against the sky's $2.217$, so it too is best at $f=0$.

⚠ ** AND THIS RECEIPT CORRECTS `cc66.43`'s OWN COMB NUMBERS, WHICH WERE GRID-LIMITED. **  Read on the
raw `LSTEP=8` grid the arm's first peak went $220 \to 228$ and $\ell_1/\ell_A$ $0.7290 \to 0.7555$;
those are ONE BIN STEP and its consequence.  Sub-bin -- with the locator validated against the banked
`LSTEP=1` spectrum first, where it recovers the fine-grid position to $0.004$ of a multipole -- the
motion is $221.95 \to 226.16$ and $0.73543 \to 0.74938$.  *** The direction survives and the
magnitude was overstated by $1.9\times$; and the SIGN of the arm's offset from the sky at $f=0$ flips,
from $0.7290$ (below) to $0.73543$ (above, by $1.3$ multipoles). ***  ⌗ The same grid caveat applies
to `cc66.43`'s FWHM reading: the width is a threshold crossing on the same $\eta$ grid, $43.591 \to
43.952$ is exactly ONE step of it, and the value jitters NON-monotonically across the family, so the
width's motion is not resolved -- while `ETA_LS`'s (six
steps, monotone) and $r_D$'s ($-4.1\%$, smooth) are.

⚑ ** THE ORDER'S OWN GUARD, ANSWERED AND SEPARATED THREE WAYS. **  It asked whether the comb moves
because the visibility peak relocates or because the acoustic phase changes, and to say so if they
cannot be separated.  They can, because the injection is a $\cos(k r_s)$ source with no plasma
dynamics in it:
    the relocation through $r_s(\mathrm{ETA\_LS})$, $146.099 \to 145.241$   $+0.591\%$   ** 31% **
    the visibility's re-weighting of the kernel (the injection, above that)  $+0.175\%$   **  9% **
    the plasma's own acoustic phase (the real spectrum, above the injection) $+1.131\%$   ** 60% **
*** So the comb's motion is NOT mostly the peak relocating: three fifths of it is the plasma
responding to the re-weighted optical depth. ***

** WHAT IS NOT CLAIMED. **  NOT a verdict on the two-rate assignment -- the row's question is whether
it is right, and a measurement of how well the comb constrains it is evidence toward that, not the
answer.  NOT that $f<0$ is admissible: the family is bounded by the two clocks and the sky's implied
$-0.304$ is an EXTRAPOLATION of the family's straight line, reported because the order asked for the
comb's discriminating power and this is what it says, not because a negative fraction is a candidate.
NOT a re-derivation of the sky's locating width: the one- and two-multipole values are P15's own
(`P15_the_sky_phase_fit_and_its_uncertainty`), taken as given here.  NOT that the injected runs are
spectra of this model -- they are the projection's transfer of a known input.  No mechanism beyond
`cc66.42`'s, nothing that touches `prop:flat`, and no refit.
"""
import os
import re
import sys

import numpy as np
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SP = os.path.join(BTW, 'spectra')
SRC = open(os.path.join(BTW, 'ACOUSTIC_two_arm.py')).read()
SMOKE = os.path.join(BTW, 'switch_smoke.sh')
LAUNCH = os.path.join(BTW, 'r6929_directions', 'launch.sh')
NEED = ('r6929_scan_cr.npz', 'r6929_geometry.npz', 'r6929_noop.npz', 'r6925_visleaf_cr.npz',
        'r6925_noop.npz', 'r6919_injected_lcdm.npz', 'r6919_injected_cr.npz',
        'cc66_r185_verify_lcdm.npz', 'cc66_r185_verify_cr.npz', 'r6941_fine_cr.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS")
    print("     rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

S = np.load(os.path.join(SP, 'r6929_scan_cr.npz'))
GE = np.load(os.path.join(SP, 'r6929_geometry.npz'))
NO = np.load(os.path.join(SP, 'r6929_noop.npz'))
N25 = np.load(os.path.join(SP, 'r6925_noop.npz'))
VL = np.load(os.path.join(SP, 'r6925_visleaf_cr.npz'))
VR = {t: np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')) for t in ('lcdm', 'cr')}
IJ = {t: np.load(os.path.join(SP, f'r6919_injected_{t}.npz')) for t in ('lcdm', 'cr')}
# ⛭⛭ RE-POINTED AT r7097+cc66.79, onto a substrate that is RE-DERIVABLE.
# *`70` established that this receipt's locator check held on `cc66_cr_x_lstep1.npz` -- which **has no
# command anywhere in the repository**, so it could not be rebuilt, and whose comb is the superseded
# STACKING ruler's ($\ell_A = 172.841$).*  ** `r6941_fine_cr.npz` has a launcher, carries
# $\ell_A = 301.799$, and spans ell 100-1999 at spacing 1. **
#   ⇒ *And it is STRICTER there: `70` measured $\ell_1$ to $0.0035$ and the worst of four to $0.023$ on
#   the new substrate against $0.0043$ and $0.133$ on the old.  Measured in
#   `r7095_70_artefact_configuration/locator_substrate_log.txt`; this edit is the re-pointing only, and
#   `r7097` reserved it to this seat because re-pointing what a receipt READS changes its subject.*
L1 = np.load(os.path.join(SP, 'r6941_fine_cr.npz'))

FS = [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]
SKY, SKY_P12 = 0.7312, 2.217           # P15's sky comb: l_1/l_A and P1/P2 (220.6 / 538.1 / 809.8)
TAG = {f: f'{f:g}'.replace('.', '') for f in FS}


# ---- the statistic, `r6911+cc66.40`'s, unchanged --------------------------------------------------
def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


ED = np.arange(0.85, 5.76, 0.7)
CTR = np.array([(a + b) / 2 for a, b in zip(ED[:-1], ED[1:])])
DES = np.vstack([CTR, np.ones_like(CTR)]).T


def bands(Qa, Oa, Qb, Ob):
    return np.array([np.interp(np.linspace(a, b, 400), Qa, Oa).std()
                     / np.interp(np.linspace(a, b, 400), Qb, Ob).std()
                     for a, b in zip(ED[:-1], ED[1:])])


def fit(Y):
    """slope, intercept, the slope's standard error, and the residual rms -- the band fit"""
    co = np.linalg.lstsq(DES, Y, rcond=None)[0]
    s2 = float(np.sum((Y - DES @ co) ** 2) / (len(CTR) - 2))
    return (float(co[0]), float(co[1]),
            float(np.sqrt(s2 * np.linalg.inv(DES.T @ DES)[0, 0])),
            float(np.std(Y - DES @ co)))


def peaks_sub(ls, Dl, n=4, order=3):
    """`cc66`'s locator: the extremum refined by the parabola through its three samples"""
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        if i < 1 or i > len(ls) - 2:
            out.append(float(ls[i]))
            continue
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    return out


def peaks_raw(ls, Dl, n=4, order=3):
    return [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=order)[0][:n]]


def heights_sub(ls, Dl, n=4, order=3):
    """the heights at the same parabola's vertex, so P1/P2 is not grid-limited either"""
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(y1 - 0.25 * (y0 - y2) * off))
    return out


# ===================================================================================================
print("\nPART 1 -- THE SWITCH IS A FRACTION, ITS ENDPOINT IS THE FLAG, AND THE GUARD IS STANDING.")
print("-" * 100)
CODE = [l.split('#')[0] for l in SRC.splitlines()]
n_of = lambda s: sum(l.count(s) for l in CODE)
check("`VISLEAF` is read as a FRACTION and the family is `1 + f (Jac - 1)` on `d(tau)`'s measure",
      n_of("_VISLF = float(os.environ.get('VISLEAF', '0'))") == 1
      and n_of('_VISL = _VISLF != 0.0') == 1
      and n_of('_dTau = _dTau * (1.0 + _VISLF * (_Jm - 1.0))') == 1,
      "one binding, one activity test, one interpolation")
check("⚑ and the ENDPOINT takes `r6925`'s expression UNCHANGED, because `1 + 1*(Jac-1)` is not `Jac` "
      "in floating point and r6925's banked runs are what the endpoint is read against",
      n_of('if _VISLF == 1.0:') == 1
      and n_of('_dTau = _dTau * 0.5 * (np.asarray(Jac_of(') == 1,
      "the f == 1 branch is the r6925 line, character for character")
check("⛭ THE SWITCH MARKER IS IN THE INSTRUMENT and its inventory is read off the file's OWN SOURCE "
      "rather than hand-maintained -- `r3512`'s flag inventory was WIDER than the code, and a list "
      "derived from the `os.environ` reads cannot drift from them",
      n_of('print("__SWITCHES__ "') == 1 and n_of('SWITCH_NAMES = tuple(sorted(set(re.findall(') == 1
      and n_of('open(__file__).read()') == 1,
      "one marker print, one derived inventory, no hand-kept list")
_inv = tuple(sorted(set(re.findall(r"os\.environ(?:\.get)?[(\[]\s*'([A-Z][A-Z0-9_]*)'", SRC))))
check("   and the regex the instrument uses finds the switches this work actually passes, so the "
      "marker is not a list of names nobody reads",
      all(n in _inv for n in ('VISLEAF', 'LEAFSCALES', 'KSLICE', 'SRCINJ', 'LSTEP', 'ARM')),
      f"{len(_inv)} names, including VISLEAF / LEAFSCALES / KSLICE / SRCINJ / LSTEP / ARM")
_sm = open(SMOKE).read()
_ln = open(LAUNCH).read()
check("⛭⛭ THE GUARD IS STANDING, NOT PER-LAUNCHER: `switch_smoke.sh` asserts every assignment "
      "appears in the marker, and the launcher runs it on EVERY distinct environment before the set "
      "goes out AND checks every slice's own log afterwards",
      "'^__SWITCHES__ '" in _sm and 'switch_smoke.sh' in _ln
      and "grep -m1 '^__SWITCHES__ '" in _ln and 'nothing launched' in _ln,
      "the smoke test, the pre-launch loop, and the per-slice check")
check("⚠ and what it cannot catch is stated where it is built -- that the value reached the PHYSICS "
      "is the knob shadow and takes a differential, not a print",
      'knob shadow' in _sm and 'r4558' in _sm, "named in switch_smoke.sh itself")

print()
check("⓵ `VISLEAF=0` IS the unset path on the arm, bit for bit",
      np.array_equal(NO['Dl__zero_cr'], NO['Dl__unset_cr']),
      f"max|dD_l| = {float(np.max(np.abs(NO['Dl__zero_cr'] - NO['Dl__unset_cr']))):.3e}")
check("⓶ and the arm unset still reproduces `r6925`'s banked no-op bit for bit, so the code change "
      "moved nothing that was already measured",
      np.array_equal(NO['Dl__unset_cr'], N25['Dl__noop_cr']),
      f"max|dD_l| = {float(np.max(np.abs(NO['Dl__unset_cr'] - N25['Dl__noop_cr']))):.3e}")
check("⓷ THE CONTROL DOES NOT MOVE AT ANY f -- `Jac == 1` there by the rate identity, so the whole "
      "family collapses to one run.  *Gated, not assumed*",
      np.array_equal(NO['Dl__noop_lcdm_f050'], NO['Dl__noop_lcdm_f0'])
      and np.array_equal(NO['Dl__noop_lcdm_f0'], N25['Dl__noop_lcdm']),
      f"f=0.5 against f=0: max|dD_l| = "
      f"{float(np.max(np.abs(NO['Dl__noop_lcdm_f050'] - NO['Dl__noop_lcdm_f0']))):.3e}")
check("⓸ ** THE FAMILY'S ENDPOINT IS THE FLAG: f=1 reproduces `r6925`'s banked `VISLEAF=1` spectra "
      "BIT FOR BIT, both the real spectrum and the injection **",
      np.array_equal(S['Dl__comb_cr_f1'], VL['Dl__combvl'])
      and np.array_equal(S['Dl__inj_cr_f1'], VL['Dl__injvl']),
      "max|dD_l| = 0 on both")
_d0 = float(np.max(np.abs(S['Dl__comb_cr_f0'] - VR['cr']['Dl'])) / np.max(np.abs(VR['cr']['Dl'])))
check("⓹ and f=0 reproduces the banked REPORTED spectrum to the `KSLICE` sum's own rounding, which "
      "is this scan's provenance: the base of the family is the corpus's own arm",
      _d0 < 1e-14, f"relative max|dD_l| = {_d0:.3e}")

# ===================================================================================================
print("\nPART 2 -- ⓵ THE BACKGROUND OVER THE FAMILY, AND WHICH OF ITS MOTIONS ARE RESOLVED.")
print("-" * 100)
fg = GE['f__cr']
G = lambda k, a: GE[f'{k}__{a}']
print(f"    {'f':>6} {'eta_LS':>10} {'FWHM':>9} {'r_D':>8} {'l_A':>10} {'r_s(eta_LS)':>12} "
      f"{'dr_s/dchi':>10}   ctl dr_s/dchi")
for i, f in enumerate(fg):
    print(f"    {f:6.2f} {G('eta_ls','cr')[i]:10.4f} {G('fwhm','cr')[i]:9.4f} {G('rD','cr')[i]:8.4f} "
          f"{G('l_A','cr')[i]:10.4f} {G('rs_leaf','cr')[i]:12.5f} {G('cs','cr')[i]:10.6f}   "
          f"{G('cs','lcdm')[i]:.6f}")
_step = float(np.min(np.diff(np.unique(G('eta_ls', 'cr')))))
check("`ETA_LS` drifts MONOTONICALLY and its drift is six times the eta-grid's own step, so it is "
      "resolved", np.all(np.diff(G('eta_ls', 'cr')) <= 0)
      and (G('eta_ls', 'cr')[0] - G('eta_ls', 'cr')[-1]) > 5 * _step,
      f"{G('eta_ls','cr')[0]:.4f} -> {G('eta_ls','cr')[-1]:.4f}, "
      f"{(G('eta_ls','cr')[0]-G('eta_ls','cr')[-1])/_step:.1f} grid steps of {_step:.4f} Mpc")
_fw = G('fwhm', 'cr')
check("⚠ ** BUT THE FWHM'S MOTION IS NOT RESOLVED, AND `cc66.43` READ IT AS IF IT WERE. **  The "
      "width is a threshold crossing on the same grid `ETA_LS` is read off, so it takes "
      "three values in steps of that same eta grid, it moves NON-monotonically in f, and the pair "
      "r6925 quoted -- 43.591 -> 43.952 -- is exactly ONE step apart: the quantisation, not a width "
      "change",
      len(np.unique(np.round(_fw, 6))) == 3 and np.any(np.diff(_fw) > 0) and np.any(np.diff(_fw) < 0)
      and (_fw.max() - _fw.min()) <= 2.01 * _step
      and abs(abs(43.9516 - 43.5913) - _step) < 1e-3,
      f"values {sorted(set(round(float(x), 4) for x in _fw))}, whole range "
      f"{_fw.max()-_fw.min():.4f} = {(_fw.max()-_fw.min())/_step:.1f} steps of {_step:.4f} Mpc, "
      f"and r6925's pair exactly one")
check("⓵ and `r_D` moves smoothly and monotonically -- a resolved motion of about four per cent",
      np.all(np.diff(G('rD', 'cr')) <= 0)
      and 0.03 < 1 - G('rD', 'cr')[-1] / G('rD', 'cr')[0] < 0.05,
      f"{G('rD','cr')[0]:.4f} -> {G('rD','cr')[-1]:.4f} "
      f"({100*(G('rD','cr')[-1]/G('rD','cr')[0]-1):+.1f}%)")
check("⓵ `d r_s/d chi` reproduces `r6925`'s two endpoints exactly and RISES across the family, its "
      "only departures from monotone sitting at the sixth decimal where `ETA_LS`'s grid jitters: the "
      "ratio the row turns on does not move",
      abs(G('cs', 'cr')[0] - 0.396733) < 5e-7 and abs(G('cs', 'cr')[-1] - 0.396957) < 5e-7
      and float(np.min(np.diff(G('cs', 'cr')))) > -2e-6
      and G('cs', 'cr')[-1] > G('cs', 'cr')[0],
      f"{G('cs','cr')[0]:.6f} -> {G('cs','cr')[-1]:.6f}, "
      f"{100*(1-G('cs','cr')[-1]/G('cs','lcdm')[-1]):.2f}% lower against "
      f"{100*(1-G('cs','cr')[0]/G('cs','lcdm')[0]):.2f}%")
check("⚑ and `l_A` does not move AT ALL over the family, so `l_1/l_A` is `l_1` in other units -- "
      "which matters for the order's guard: the acoustic scale is not absorbing any of the shift",
      len(np.unique(G('l_A', 'cr'))) == 1, f"l_A = {G('l_A','cr')[0]:.4f} at every f")
check("   and NOTHING on the control moves at any f, at every quantity in the table",
      all(len(np.unique(G(k, 'lcdm'))) == 1
          for k in ('eta_ls', 'fwhm', 'rD', 'l_A', 'cs', 'rs_leaf', 'tau_ls')),
      "eta_LS, FWHM, r_D, l_A, dr_s/dchi, r_s and tau at the peak: one value each")

# ===================================================================================================
print("\nPART 3 -- THE LOCATOR IS VALIDATED BEFORE IT IS USED, AND `cc66.43`'s COMB WAS GRID-LIMITED.")
print("-" * 100)
_lsf = L1['ls'].astype(float)
_m8 = np.isin(_lsf, np.arange(100, 2000, 8))
_pf, _p8 = peaks_sub(_lsf, L1['Dl']), peaks_sub(_lsf[_m8], L1['Dl'][_m8])
print(f"    the banked LSTEP=1 spectrum, sub-bin        : {[round(x, 3) for x in _pf]}")
print(f"    the same data decimated to the LSTEP=8 grid : {[round(x, 3) for x in _p8]}")
check("⚑ the sub-bin locator recovers the FINE-GRID first peak from the coarse grid to better than a "
      "hundredth of a multipole, so the scan's abscissa is validated on the corpus's own bank before "
      "it is read", abs(_pf[0] - _p8[0]) < 0.01 and max(abs(a - b) for a, b in zip(_pf, _p8)) < 0.2,
      f"l_1 differs by {abs(_pf[0]-_p8[0]):.4f}, the worst of four by "
      f"{max(abs(a-b) for a, b in zip(_pf, _p8)):.3f}")

R = {}
for f in FS:
    t = TAG[f]
    ls, Dl = S[f'ls__comb_cr_f{t}'].astype(float), S[f'Dl__comb_cr_f{t}']
    lA = float(S[f'l_A__comb_cr_f{t}'])
    ps, pr, hs = peaks_sub(ls, Dl), peaks_raw(ls, Dl), heights_sub(ls, Dl)
    Q, O = ls / lA, osc(ls / lA, Dl)
    Y = bands(Q, O, VR['lcdm']['ls'].astype(float) / float(VR['lcdm']['l_A']),
              osc(VR['lcdm']['ls'].astype(float) / float(VR['lcdm']['l_A']), VR['lcdm']['Dl']))
    sl, ic, se, rr = fit(Y)
    lsi, Dli = S[f'ls__inj_cr_f{t}'].astype(float), S[f'Dl__inj_cr_f{t}']
    lAi = float(S[f'l_A__inj_cr_f{t}'])
    Qi, Oi = lsi / lAi, osc(lsi / lAi, Dli)
    QLi = IJ['lcdm']['ls__sweepown'].astype(float) / float(IJ['lcdm']['l_A__sweepown'])
    Yi = bands(Qi, Oi, QLi, osc(QLi, IJ['lcdm']['Dl__sweepown']))
    sli, ici, sei, rri = fit(Yi)
    R[f] = dict(l1=ps[0], raw=pr[0], ps=ps, r=ps[0] / lA, p12=hs[0] / hs[1], lA=lA,
                Ym=float(Y.mean()), sl=sl, se=se, rr=rr, l1i=peaks_sub(lsi, Dli)[0],
                Yim=float(Yi.mean()), sli=sli, sei=sei, rri=rri)
print()
print(f"    {'f':>5} {'l_1 raw':>8} {'l_1 sub':>9} {'l_1/l_A':>9} {'P1/P2':>7} | "
      f"{'contrast':>8} {'q-slope':>9} {'s.e.':>8} {'resid':>7} | {'inj l_1':>8} {'inj c':>7} "
      f"{'inj slope':>10}")
for f in FS:
    r = R[f]
    print(f"    {f:5.2f} {r['raw']:8.0f} {r['l1']:9.3f} {r['r']:9.5f} {r['p12']:7.3f} | "
          f"{r['Ym']:8.4f} {r['sl']:+9.5f} {r['se']:8.5f} {r['rr']:7.4f} | {r['l1i']:8.3f} "
          f"{r['Yim']:7.4f} {r['sli']:+10.5f}")
print(f"    the sky: l_1/l_A = {SKY:.4f}, P1/P2 = {SKY_P12:.3f}")

_sl_l1, _ic_l1 = np.polyfit(FS, [R[f]['l1'] for f in FS], 1)
_res_l1 = float(np.max(np.abs(np.array([R[f]['l1'] for f in FS])
                             - np.polyval([_sl_l1, _ic_l1], FS))))
check(f"⛭⛭ ** EVERY READING IS LINEAR IN THE PARAMETER. **  l_1 = {_ic_l1:.2f} + {_sl_l1:.2f} f to "
      f"within three hundredths of a multipole -- six parts in a thousand of its whole span -- so "
      f"the family has ONE number in it and the scan is not hiding structure between its points",
      _res_l1 < 0.03,
      f"max deviation from the straight line {_res_l1:.4f} multipoles")
check("⚠ ** AND `cc66.43`'s 220 -> 228 WAS ONE BIN STEP. **  The raw locator takes two values across "
      "the whole family where the sub-bin locator moves smoothly, and the true motion is 1.9 times "
      "SMALLER than the grid said",
      len(set(R[f]['raw'] for f in FS)) == 2
      and abs((228 - 220) / (R[1.0]['l1'] - R[0.0]['l1']) - 1.9) < 0.2,
      f"raw {sorted(set(int(R[f]['raw']) for f in FS))} against sub-bin "
      f"{R[0.0]['l1']:.3f} -> {R[1.0]['l1']:.3f} (+{R[1.0]['l1']-R[0.0]['l1']:.3f})")
check("⚠ and the SIGN of the arm's offset from the sky at f=0 flips with the refinement: the raw grid "
      "put l_1/l_A BELOW the sky at 0.7290, sub-bin it is ABOVE it",
      R[0.0]['r'] > SKY and 0.7290 < SKY,
      f"0.7290 (raw, below) -> {R[0.0]['r']:.5f} (sub-bin, above by "
      f"{(R[0.0]['r']-SKY)*R[0.0]['lA']:.2f} multipoles)")

# ===================================================================================================
print("\nPART 4 -- ⓵ THE RESOLUTION, WHICH IS WHAT THE ORDER ASKED FOR: WHAT CAN THIS COMB DECIDE?")
print("-" * 100)
ONE = 1.0 / R[0.0]['lA']
d_comb = R[1.0]['r'] - R[0.0]['r']
d_lev = R[1.0]['Ym'] - R[0.0]['Ym']
d_slp = R[1.0]['sl'] - R[0.0]['sl']
print(f"    one multipole in l_1/l_A                       : {ONE:.5f}")
print(f"    the family's whole span in l_1/l_A             : {d_comb:.5f} "
      f"= {d_comb/ONE:.2f} multipoles")
print(f"    ⇒ in the sky's own locating widths (1 / 2 mult.): {d_comb/ONE:.2f} / {d_comb/(2*ONE):.2f} "
      f"sigma   ->  f pinned to +-{ONE/d_comb:.2f} / +-{2*ONE/d_comb:.2f}")
print(f"    the contrast's LEVEL  : {d_lev:+.5f} against its band scatter {R[0.0]['rr']:.5f} "
      f"-> {abs(d_lev)/R[0.0]['rr']:.2f} sigma, f to +-{R[0.0]['rr']/abs(d_lev):.2f}")
print(f"    the contrast's SLOPE  : {d_slp:+.5f} against its fit s.e.   {R[0.0]['se']:.5f} "
      f"-> {abs(d_slp)/R[0.0]['se']:.2f} sigma, f to +-{R[0.0]['se']/abs(d_slp):.2f}")
check("⓵ ** THE COMB DISCRIMINATES THE FAMILY'S ENDS, AND ONLY JUST: four multipoles end to end, "
      "which is four of the sky's one-multipole locating widths and two of its two-multipole ones. "
      "**  ⇒ It pins f to about a quarter of the family and nowhere near the clock",
      3.5 < d_comb / ONE < 5.0 and 0.2 < ONE / d_comb < 0.3,
      f"{d_comb/ONE:.2f} multipoles end to end, f to +-{ONE/d_comb:.2f}")
check("⛔ ** AND THE ORDER'S FIRST BRANCH IS HALF RIGHT. **  The contrast's LEVEL is shallow as it "
      "guessed -- under two sigma where the comb is over four -- but its q-SLOPE is not: it is the "
      "comb's statistical equal, so 'steep comb, shallow contrast' is not what separates them",
      abs(d_lev) / R[0.0]['rr'] < 2.0 and abs(d_slp) / R[0.0]['se'] > 3.0,
      f"level {abs(d_lev)/R[0.0]['rr']:.2f} sigma, slope {abs(d_slp)/R[0.0]['se']:.2f} sigma, "
      f"comb {d_comb/ONE:.2f}")
check("⛭ ** WHAT SEPARATES THEM IS THAT THE CONTRAST'S ERROR GROWS WITH THE PARAMETER AND THE "
      "COMB'S DOES NOT. **  The band residual and the slope's standard error each grow about five "
      "times from f=0 to f=1 -- `cc66.40`'s guard firing a fourth time, on the phase mismatch a band "
      "ratio reads when the two combs stop being aligned in q",
      R[1.0]['rr'] / R[0.0]['rr'] > 3.5 and R[1.0]['se'] / R[0.0]['se'] > 3.5,
      f"residual {R[0.0]['rr']:.4f} -> {R[1.0]['rr']:.4f} "
      f"({R[1.0]['rr']/R[0.0]['rr']:.1f}x), s.e. {R[0.0]['se']:.5f} -> {R[1.0]['se']:.5f} "
      f"({R[1.0]['se']/R[0.0]['se']:.1f}x)")
check("   and the injection carries the same degradation, so it is the statistic's response to the "
      "comb moving and not something in the plasma",
      R[1.0]['rri'] / R[0.0]['rri'] > 3.5,
      f"{R[0.0]['rri']:.4f} -> {R[1.0]['rri']:.4f} ({R[1.0]['rri']/R[0.0]['rri']:.1f}x)")
check("   ⌗ and the injection's two endpoints reproduce `r6925`'s own contrast table exactly, which "
      "is this scan's continuity with the reading it refines",
      abs(R[0.0]['Yim'] - 1.0850) < 5e-4 and abs(R[1.0]['Yim'] - 1.0695) < 5e-4
      and abs(R[0.0]['sli'] - 0.02424) < 5e-5 and abs(R[1.0]['sli'] - 0.01332) < 5e-5,
      f"{R[0.0]['Yim']:.4f} / {R[1.0]['Yim']:.4f} against r6925's 1.0850 / 1.0695")

# ===================================================================================================
print("\nPART 5 -- ⛭⛭⛭ AND THE DECIDING RESULT: THE SKY'S OWN VALUE IS NOT IN THE FAMILY.")
print("-" * 100)
f_sky = (SKY - R[0.0]['r']) / d_comb
print(f"    the sky's l_1/l_A = {SKY:.4f}; the family runs {R[0.0]['r']:.5f} (f=0) -> "
      f"{R[1.0]['r']:.5f} (f=1)")
print(f"    ⇒ on the family's own straight line the sky sits at f = {f_sky:+.3f}")
print(f"    P1/P2, a SECOND external referent: {R[0.0]['p12']:.3f} (f=0) -> {R[1.0]['p12']:.3f} "
      f"(f=1) against the sky's {SKY_P12:.3f}")
check("⛔ ** NO INTERIOR FRACTION FITS THE COMB BETTER THAN THE ENDPOINT THE INSTRUMENT USES, so the "
      "order's third branch does not arise and there is no fitted clock to declare. **  l_1/l_A is "
      "monotone in f and already ABOVE the sky at f=0, so every f>0 is worse",
      all(R[FS[i + 1]]['r'] > R[FS[i]]['r'] for i in range(len(FS) - 1)) and R[0.0]['r'] > SKY
      and min(abs(R[f]['r'] - SKY) for f in FS) == abs(R[0.0]['r'] - SKY),
      "|l_1/l_A - sky| is smallest at f=0: "
      + ', '.join('%g:%.4f' % (f, abs(R[f]['r'] - SKY)) for f in FS))
check("⛭⛭⛭ ** AND THE SKY'S VALUE LIES OUTSIDE THE ADMISSIBLE FAMILY, at f ~ -0.3 on the far side "
      "of the stacking clock.  ⇒ The residual first-peak disagreement CANNOT be absorbed by the "
      "clock assignment, because the direction it would need is not admissible **",
      f_sky < -0.1, f"f_sky = {f_sky:+.3f}, and the family is bounded by f in [0, 1]")
check("⚑ and P1/P2 says the same independently: it moves AWAY from the sky as f rises, so the two "
      "external referents agree on f=0 and neither is being traded against the other",
      R[0.0]['p12'] < SKY_P12 and R[1.0]['p12'] < R[0.0]['p12'],
      f"{R[0.0]['p12']:.3f} -> {R[1.0]['p12']:.3f} against the sky's {SKY_P12:.3f}")

# ===================================================================================================
print("\nPART 6 -- ⓶ THE ORDER'S GUARD: RELOCATION, THE KERNEL'S WEIGHTING, OR THE PLASMA'S PHASE.")
print("-" * 100)
_i1 = int(np.argmin(np.abs(fg - 1.0)))
rs0, rs1 = float(G('rs_leaf', 'cr')[0]), float(G('rs_leaf', 'cr')[_i1])
fr_rel = rs0 / rs1 - 1.0
fr_inj = R[1.0]['l1i'] / R[0.0]['l1i'] - 1.0
fr_real = R[1.0]['l1'] / R[0.0]['l1'] - 1.0
print(f"    r_s(ETA_LS) {rs0:.5f} -> {rs1:.5f}: the RELOCATION alone predicts "
      f"dl_1/l_1 = {100*fr_rel:+.4f}%   ({100*fr_rel/fr_real:.0f}%)")
print(f"    the INJECTION -- a cos(k r_s) source with NO plasma dynamics -- moves "
      f"{100*fr_inj:+.4f}%, so the VISIBILITY'S re-weighting of the kernel is "
      f"{100*(fr_inj-fr_rel):+.4f}%   ({100*(fr_inj-fr_rel)/fr_real:.0f}%)")
print(f"    the REAL spectrum moves {100*fr_real:+.4f}%, so THE PLASMA'S OWN PHASE is "
      f"{100*(fr_real-fr_inj):+.4f}%   ({100*(fr_real-fr_inj)/fr_real:.0f}%)")
print(f"    in multipoles on l_1: total {R[1.0]['l1']-R[0.0]['l1']:+.3f} = relocation "
      f"{R[0.0]['l1']*fr_rel:+.3f}, visibility {R[0.0]['l1']*(fr_inj-fr_rel):+.3f}, plasma "
      f"{R[0.0]['l1']*(fr_real-fr_inj):+.3f}")
check("⓶ ** THE TWO CAN BE SEPARATED, and the order's guard is answered rather than deferred: the "
      "injection has no plasma dynamics in it, so its motion above the relocation is the kernel's "
      "weighting and the real spectrum's motion above the injection is the plasma's own phase **",
      fr_rel > 0 and fr_inj > fr_rel and fr_real > fr_inj,
      f"{100*fr_rel:+.4f}% < {100*fr_inj:+.4f}% < {100*fr_real:+.4f}%")
check("⛔ ** AND THE COMB'S MOTION IS NOT MOSTLY THE VISIBILITY PEAK RELOCATING. **  Relocation is a "
      "third of it, the kernel's re-weighting a tenth, and THREE FIFTHS is the plasma responding to "
      "the re-weighted optical depth",
      0.25 < fr_rel / fr_real < 0.4 and (fr_real - fr_inj) / fr_real > 0.5,
      f"relocation {100*fr_rel/fr_real:.1f}%, visibility "
      f"{100*(fr_inj-fr_rel)/fr_real:.1f}%, plasma {100*(fr_real-fr_inj)/fr_real:.1f}%")
check("   and the three shares add to the whole by construction, which is what makes this a "
      "decomposition and not three separate readings",
      abs((fr_rel + (fr_inj - fr_rel) + (fr_real - fr_inj)) / fr_real - 1.0) < 1e-12,
      "31.1 + 9.2 + 59.6 = 100.0 per cent")

# ===================================================================================================
print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    sys.exit(1)
print("GATES: ALL PASS.")
print(f"""
  ⛭⛭ THE COMB'S RESOLUTION, STATED BEFORE IT DECIDES: the whole one-parameter family between the two
  admissible clocks spans {d_comb/ONE:.2f} multipoles in l_1 -- {d_comb:.5f} in l_1/l_A, which is
  {d_comb/ONE:.1f} of the sky's one-multipole locating widths and {d_comb/(2*ONE):.1f} of its
  two-multipole ones.  The comb separates the family's ends and pins f only to about +-{ONE/d_comb:.2f}.

  ⛔ THE ORDER'S FIRST BRANCH IS HALF RIGHT.  The contrast's LEVEL is shallow
  ({abs(d_lev)/R[0.0]['rr']:.2f} sigma against the comb's {d_comb/ONE:.2f}) but its q-SLOPE is the
  comb's equal ({abs(d_slp)/R[0.0]['se']:.2f} sigma).  What separates them is that the contrast's own
  error grows about five times across the family while the comb's locating width does not move.

  ⛭⛭⛭ AND THE DECIDING RESULT IS NOT ABOUT THE CHOICE.  The sky's {SKY:.4f} sits at f = {f_sky:+.3f}
  on the family's straight line -- OUTSIDE it, on the far side of the stacking clock.  So no interior
  fraction fits better than the endpoint in use (there is no fitted clock to declare), the best point
  is f=0, and the residual first-peak disagreement cannot be absorbed by the clock assignment.
  P1/P2 agrees independently: {R[0.0]['p12']:.3f} -> {R[1.0]['p12']:.3f} against the sky's {SKY_P12:.3f}.

  ⚑ THE GUARD: the comb's motion is {100*fr_rel/fr_real:.0f}% the peak relocating through
  r_s(ETA_LS), {100*(fr_inj-fr_rel)/fr_real:.0f}% the visibility's re-weighting of the kernel, and
  {100*(fr_real-fr_inj)/fr_real:.0f}% the plasma's own acoustic phase.  They separate.

  ⚠ AND TWO OF cc66.43's NUMBERS WERE GRID-LIMITED: l_1 220 -> 228 is really
  {R[0.0]['l1']:.2f} -> {R[1.0]['l1']:.2f}, l_1/l_A 0.7290 -> 0.7555 is really {R[0.0]['r']:.5f} ->
  {R[1.0]['r']:.5f} (and the arm sits ABOVE the sky at f=0, not below), while the FWHM's
  43.591 -> 43.952 is exactly one step of the eta grid and is not a resolved motion at all.

  NOT CLAIMED: a verdict on the two-rate assignment; that f<0 is admissible (the -0.304 is the
  family's line extrapolated, reported because the order asked what the comb can decide); a
  re-derivation of the sky's locating width, which is P15's own; that the injected runs are spectra of
  this model; any mechanism beyond cc66.42's; nothing touches prop:flat and there is no refit.
""")
sys.exit(0)
