"""
P15_the_phase_systematic_leaves_the_step_standing_and_carries_a_third_of_the_retention_slope_through_a_phase_drift_between_the_sources

r7055 Q1 -> 70: the phase systematic's effective count against the slope and the step.  Pre-registered at
`computations/beyond_the_wall/r7055_70_phase_count/PREDICTION.md`, committed before this file.

⛭ RE-POINTED r7637 (node 70) ONTO THE ARM OF RECORD, AND ON IT THE SHARED-COMB VERDICTS INVERT.
  The banks are now the `_leafrec1` arm (LEAFREC=1, r7633's refit) against the unchanged control.  On it the
  two arms' combs part: D_l periods 1.0045 against 1.0090, source periods 1.0115 against 1.0170, the source
  phase difference running +0.034 to +0.199 rad across the range (it was +0.013 to +0.042).  So:
  - THE SHARED-COMB STEP DOES NOT STAND.  The step statistic's null reaches 0.0304 / 0.0363 at the real phase,
    half or more of the arm-of-record step of 0.0617, in its direction; N_eff 2.3 / 2.9.
  - ON THE OWN COMB IT DOES (69's ruling 1; `r7637_70_own_comb_statistic/own_comb.py`).  The step is -0.0396;
    at the real phase the null is -0.0039 / -0.0105, so the step survives its subtraction at -0.036 / -0.029.
    Over phase the null's worst is 0.0090 at amplitude 0.5 (0.23 of the step) and 0.0241 at the banks' own
    (0.61) -- the declared sensitivity is the harsher test, and on the LEAFREC=0 arm's shared comb it was 0.44.
  - THE RETENTION SLOPE IS CARRIED WHOLE BY THE NULL.  At the real phase it returns +0.0309 / +0.0291, 115 /
    108 per cent of the arm-of-record slope of +0.0269, and the rise does not survive its subtraction.  The D_l
    side no longer cancels (7 per cent) and the source side reaches 9.
  - One comb for both arms still takes most of the null away (+0.0309 -> +0.0047 at amplitude 0.5), so the
    carrier is still the arms' own combs, now on both sides of the ratio.
  ⇒ The title's two clauses are the LEAFREC=0 arm's.  On the arm of record the step stands only on the own
    comb, and the retention slope is not carried by a third of itself but by all of it.  Routed to 69 for the
    restated stem; the old-arm reading below is kept as written.

What is measured.  Each statistic -- `band_excess` (the step's) and `retained` (the slope's) -- is lifted from
its own receipt by syntax tree and run unchanged.  Each is fed a NULL injection built on every bank it reads:
  - each bank's own envelope, with a comb at that bank's own fitted period and phase;
  - IDENTICAL amplitude on both arms, so the true excess is zero in every band and the true slope is zero;
  - a COMMON phase shift scanned over 24 values.
What comes back is the statistic's own phase systematic, after the arm/control ratio has cancelled what it can.

⛭ WHAT IS FOUND (the pre-registered amplitude 0.5 first; the banks' own amplitudes as a declared sensitivity)
  ② THE EFFECTIVE COUNT.  Against the phase systematic, both statistics have three to three and a half modes
     across their seven bands: N_eff 3.5 / 2.8 for the step's, 3.3 / 3.6 for the slope's.
     - The slope's own effective count, n = 7 (sigma_OLS / sigma_slope)^2, is 8.9 / 5.1.  That is fewer than
       seven at the real amplitudes, but above the pre-registered four.
  THE STEP STANDS.
     - Its false value over phase is at most 0.010 / 0.019, against a step of 0.043.
     - At the real phase it is -0.010 / -0.017: a quarter to two fifths of the step, in the step's own
       direction.
     - Signal to systematic is 7.5 / 3.8.
  ① THE SLOPE CARRIES A THIRD OF ITSELF AS SYSTEMATIC.
     - At the REAL phase the null returns +0.0048 / +0.0052 on the reported twelve-setting mean, against the
       real +0.0136.  That is 36 / 39 per cent, in the slope's own direction.
     - On the single seven-band setting the null reaches +0.0081, over half.
     - The rise survives subtracting the null (+0.0088 / +0.0083).  Its SIZE does not.
     - The phase systematic's spread of the slope (0.0026 / 0.0036) exceeds the reported +-0.0021, which is a
       spread over envelope settings and not a regression error.
  ⛭⛭ AND THE CARRIER IS A PHASE DRIFT BETWEEN THE TWO ARMS' SOURCES.
     - On the D_l side the null cancels to within one per cent in every band.  On the source side it reaches
       six per cent.
     - The two sources' combs sit at periods 1.0170 / 1.0160, so their phase difference runs +0.013 to
       +0.042 rad across the range.
     - Give both arms one comb and the null slope falls to +0.0008.  Flatten the envelope instead and
       +0.0034 of it stays.
     ⇒ The band-RMS ratio is a partial-cycle statistic, and it reads a few hundredths of a radian of phase
       between the arms' sources as a difference in RETENTION.
  ⌗ And the receipt computes +0.01359 +- 0.00202, where the paper and that receipt's own docstring say
     +0.0139 +- 0.0021.  Routed, not edited.

⛔ NOT CLAIMED.  Nothing about the likelihood, which bins at a thirty-fourth of a period (`r7033`'s split).  No
edit to either receipt and no prose edited.  A null injection measures the statistic's response.  It does not
say what the real spectra's arm difference is.
"""
import ast
import os
import re

import numpy as np
from scipy.signal import savgol_filter

FAILS = []


def check(name, cond, got=None):
    ok = bool(cond)
    print(f"    [{'ok' if ok else 'FAIL'}]  {name}" + (f"   {got}" if got is not None else ""))
    if not ok:
        FAILS.append(name)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
LAW = os.path.join(HERE, 'P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_'
                         'and_the_law_has_no_fitted_coefficient.py')
STEPF = os.path.join(HERE, 'P15_the_step_is_the_excesss_own_and_it_sits_at_the_second_acoustic_peak_'
                           'and_none_of_the_four_produces_it.py')
SLOPEF = os.path.join(HERE, 'P15_the_cross_term_is_not_the_channel_and_every_projected_term_carries_the_excess.py')
STEP_REPORTED = 0.0617         # r7637: band 1 below the band 2-7 mean on the ARM OF RECORD, shared comb (was 0.043)
SLOPE_PAPER = 0.0139           # the figure P15 and the slope receipt's docstring carry (the LEAFREC=0 arm's)
PH = np.linspace(0, 2 * np.pi, 24, endpoint=False)
SETTINGS = [(w, nb, hi) for w in (0.75, 1.0, 1.25, 1.5) for nb, hi in ((7, 5.75), (10, 6.10), (5, 5.75))]

print(__doc__)
print("=" * 100)


def lift(path, names, ns):
    tree = ast.parse(open(path, encoding='utf-8').read())
    body = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    check(f"lifted unchanged from `{os.path.basename(path)[:60]}...`: {', '.join(names)}",
          {n.name for n in body} == set(names))
    exec(compile(ast.Module(body=body, type_ignores=[]), path, 'exec'), ns)
    return ns


L = lift(LAW, ['env_a', 'osc', '_fit', 'fit_period'], {'np': np, 'LO': 0.85, 'HI': 5.75})


def phase(q, o, T):
    m = (q >= 0.85) & (q <= 5.75)
    x = q[m]
    X = np.column_stack([np.cos(2 * np.pi * x / T), np.sin(2 * np.pi * x / T), np.ones_like(x), x])
    c, *_ = np.linalg.lstsq(X, o[m], rcond=None)
    return float(np.arctan2(-c[1], c[0]))


def comb_params(q, y):
    o = L['osc'](q, y)
    T = L['fit_period'](q, o)
    m = (q >= 0.85) & (q <= 5.75)
    return L['env_a'](q, y), T, phase(q, o, T), L['_fit'](q[m], o[m], T)[0]


def neff(M):
    lam = np.linalg.eigvalsh(np.corrcoef(M.T))
    return float(lam.sum() ** 2 / (lam ** 2).sum())


# ================================================================================================
print()
print("  " + "=" * 96)
print("  THE STEP'S STATISTIC -- `band_excess('mean')` on the `r6941_fine` banks")
print("  " + "=" * 96)
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr_leafrec1.npz'))['q_edges'], float)
FB = {t: np.load(os.path.join(SP, n)) for t, n in (('lcdm', 'r6941_fine_lcdm.npz'), ('cr', 'r6941_fine_cr_leafrec1.npz'))}
FQ = {t: FB[t]['ls'].astype(float) / float(FB[t]['l_A']) for t in FB}
FY = {t: np.asarray(FB[t]['Dl'], float) for t in FB}
INJ = {}
# ⛔ r7639+cc66.25: this lifts the SHARED-comb reading by name.  `band_excess` in that file was
#   CARRIED at r7639+cc66.8, which both gave it a free variable no lifter supplies AND changed the
#   quantity -- and this receipt's checks below say "shared comb" and assert the alternation, so the
#   carried row would have been the wrong object measured green.
NS = lift(STEPF, ['env', 'band_excess_shared'], {'np': np, 'savgol_filter': savgol_filter,
                                                 'QE': QE, 'fine': lambda t: INJ[t]})
INJ.update({t: (FQ[t], FY[t]) for t in FB})
T_real = NS['band_excess_shared']('mean')
step_real = float(T_real[0] - T_real[1:].mean())
check("the lifted statistic on the arm of record, shared comb: band 1 +0.0186, band 6 +0.0141 BELOW it, "
      "band 1 below the rest by 0.0617 -- the alternation the two arms' parted combs make",
      abs(T_real[0] - 0.0186) < 5e-5 and T_real[5] < T_real[0] and abs(step_real + STEP_REPORTED) < 5e-4,
      "  ".join(f"{v:+.4f}" for v in T_real) + f"   step {step_real:+.4f}")
CPF = {t: comb_params(FQ[t], FY[t]) for t in FB}
print(f"    the banks' own combs: " + ", ".join(f"{t} T {CPF[t][1]:.4f} phase {CPF[t][2]:.3f} amp "
                                            f"{CPF[t][3]:.3f}" for t in CPF))


def step_null(A):
    E = []
    for p in PH:
        for t in FB:
            e, T, ph, _ = CPF[t]
            INJ[t] = (FQ[t], e * (1 + A * np.cos(2 * np.pi * FQ[t] / T + ph + p)))
        E.append(NS['band_excess_shared']('mean'))   # r7639+cc66.25: the shared reading, as above
    return np.array(E)


RS = {}
for lab, A in (('pre-registered amplitude 0.5', 0.5),
               ('declared sensitivity: the banks\' own amplitude', float(np.mean([CPF[t][3] for t in CPF])))):
    E = step_null(A)
    s = E[:, 0] - E[:, 1:].mean(1)
    RS[lab] = dict(E=E, s=s, n=neff(E))
    print(f"\n    {lab} ({A:.3f}):  N_eff {neff(E):.2f} of 7;  false step at the real phase {s[0]:+.4f}, "
          f"spread over phase {s.std():.4f}, worst {np.abs(s).max():.4f}")
    print("      e at the real phase: " + "  ".join(f"{v:+.4f}" for v in E[0]))
p0 = RS['pre-registered amplitude 0.5']
check("⛭ ② the step statistic's phase systematic has fewer than three modes across the seven bands",
      2.0 < p0['n'] < 3.0, f"N_eff {p0['n']:.2f}")
wstep = max(np.abs(r['s']).max() for r in RS.values())
check("⛭ ON THE SHARED COMB THE STEP DOES NOT STAND: its worst false value over phase is half or more of the "
      "step", wstep > 0.45 * STEP_REPORTED, f"worst {wstep:.4f} against {STEP_REPORTED}")
check("     ...and at the real phase the false step is half or more of it, in the step's own direction",
      all(r['s'][0] < -0.45 * STEP_REPORTED for r in RS.values()),
      ", ".join(f"{r['s'][0]:+.4f}" for r in RS.values()))
check("     signal to systematic over the phase spread falls to under four on both amplitudes (it was 7.5 / 3.8)",
      all(STEP_REPORTED / r['s'].std() < 4.0 for r in RS.values()),
      ", ".join(f"{STEP_REPORTED / r['s'].std():.1f}" for r in RS.values()))

# r7637: the same null through the OWN-COMB statistic (69's ruling 1), on both amplitudes
import sys as _sys
_sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC  # noqa: E402
_B = {t: (FQ[t], FY[t]) for t in FB}
E_own, _ = OC.band_excess_own(_B, QE)
s_own = OC.step(E_own)
N_OWN = {A: OC.null(_B, QE, lambda b, q: OC.band_excess_own(b, q)[0], A)[:, 0]
         for A in (0.5, float(np.mean([CPF[t][3] for t in CPF])))}
print("    own comb: " + "  ".join(f"{v:+.4f}" for v in E_own) + f"   step {s_own:+.4f}; null "
      + ", ".join(f"A {A:.3f}: real {n[0]:+.4f} worst {np.abs(n).max():.4f}" for A, n in N_OWN.items()))
_n5, _nb = N_OWN[0.5], [n for A, n in N_OWN.items() if A != 0.5][0]
check("⛭⛭ ON THE OWN COMB THE STEP STANDS at the pre-registered amplitude: -0.0396, the null's worst over phase "
      "under a third of it", abs(s_own + 0.0396) < 5e-4 and np.abs(_n5).max() < abs(s_own) / 3,
      f"step {s_own:+.4f}; worst {np.abs(_n5).max():.4f}")
check("     ⚠ at the banks' own amplitude its worst over phase reaches 0.61 of it -- REPORTED: the declared "
      "sensitivity is the harsher test, and on the LEAFREC=0 arm it reached 0.44 on the shared comb too",
      0.55 < np.abs(_nb).max() / abs(s_own) < 0.67, f"worst {np.abs(_nb).max():.4f}")
check("     ...and at the REAL phase the null is a quarter of the step or less, on both amplitudes, so the step "
      "survives the null's subtraction at -0.029 to -0.036",
      all(abs(n[0]) < 0.3 * abs(s_own) for n in N_OWN.values()),
      ", ".join(f"{s_own - n[0]:+.4f}" for n in N_OWN.values()))

# ================================================================================================
print()
print("  " + "=" * 96)
print("  THE SLOPE'S STATISTIC -- `retained` on the `r6915_pairs` and `r6911_source` banks")
print("  " + "=" * 96)
PR0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', 'r6915_pairs_cr_leafrec1.npz'))}
SO0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in (('lcdm', 'r6911_source_lcdm_leafrec1.npz'), ('cr', 'r6911_source_cr_leafrec1.npz'))}
QL = {t: PR0[t]['ls'].astype(float) / float(PR0[t]['l_A']) for t in PR0}
QK = {t: SO0[t]['k'] * float(SO0[t]['r_s']) / np.pi for t in SO0}
NS2 = lift(SLOPEF, ['env_a', 'osc', 'retained'], {'np': np, 'QL': QL, 'QK': QK})


def slopes(pr, so):
    NS2.update(PR=pr, SO=so)
    x, y, _ = NS2['retained'](1.0, 7, 5.75)
    s12 = [np.polyfit(*NS2['retained'](w, nb, hi)[:2], 1)[0] for w, nb, hi in SETTINGS]
    return x, y, float(np.polyfit(x, y, 1)[0]), float(np.mean(s12)), float(np.std(s12))


xr, yr, s7r, s12r, sd12r = slopes(PR0, SO0)
check("the lifted statistic on the arm of record: +0.0269 +- 0.0123 over twelve settings (the LEAFREC=0 arm's "
      "+0.01359 +- 0.00202)", abs(s12r - 0.02690) < 5e-5 and abs(sd12r - 0.01226) < 5e-5,
      f"{s12r:+.5f} +- {sd12r:.5f}")
print(f"    ⌗ the paper and that receipt's docstring carry +{SLOPE_PAPER} +- 0.0021 -- REPORTED, not required")
CPD = {t: comb_params(QL[t], np.asarray(PR0[t]['Dl'], float)) for t in PR0}
CPS = {t: comb_params(QK[t], np.asarray(SO0[t]['S_i'], float) ** 2) for t in SO0}
print("    D_l combs: " + ", ".join(f"{t} T {CPD[t][1]:.4f} ph {CPD[t][2]:.3f} amp {CPD[t][3]:.3f}" for t in CPD))
print("    source combs: " + ", ".join(f"{t} T {CPS[t][1]:.4f} ph {CPS[t][2]:.3f} amp {CPS[t][3]:.3f}" for t in CPS))


def inject(AD, AS, p, flat=False):
    pr, so = {}, {}
    for t in PR0:
        e, T, ph, _ = CPD[t]
        pr[t] = {'Dl': e * (1 + AD * np.cos(2 * np.pi * QL[t] / T + ph + p))}
        e, T, ph, _ = CPS[t]
        e = np.ones_like(e) if flat else e
        so[t] = {'S_i': np.sqrt(np.maximum(e * (1 + AS * np.cos(2 * np.pi * QK[t] / T + ph + p)), 0.0))}
    return pr, so


RSL = {}
for lab, AD, AS in (('pre-registered amplitude 0.5', 0.5, 0.5),
                    ('declared sensitivity: the banks\' own amplitudes',
                     float(np.mean([CPD[t][3] for t in CPD])), float(np.mean([CPS[t][3] for t in CPS])))):
    Y, S7, S12 = [], [], []
    for p in PH:
        x, y, s7, s12, _ = slopes(*inject(AD, AS, p))
        Y.append(y - 1)
        S7.append(s7)
        S12.append(s12)
    Y, S7, S12 = np.array(Y), np.array(S7), np.array(S12)
    xc = x - x.mean()
    res = np.array([yy - np.polyval(np.polyfit(x, yy, 1), x) for yy in Y])
    s_ols = float(np.sqrt((res ** 2).sum(1) / (len(x) - 2) / (xc ** 2).sum()).mean())
    RSL[lab] = dict(Y=Y, S7=S7, S12=S12, n=neff(Y), n_slope=len(x) * (s_ols / S7.std()) ** 2, s_ols=s_ols)
    print(f"\n    {lab} ({AD:.3f} / {AS:.3f}):  N_eff {neff(Y):.2f} of 7;  n_slope {RSL[lab]['n_slope']:.1f}")
    print(f"      false slope at the real phase: 7-band {S7[0]:+.4f}, twelve-setting mean {S12[0]:+.4f}")
    print(f"      over phase: 7-band spread {S7.std():.4f} worst {np.abs(S7).max():.4f};  "
          f"twelve-setting mean spread {S12.std():.4f} worst {np.abs(S12).max():.4f}")
    print("      e at the real phase: " + "  ".join(f"{v:+.4f}" for v in Y[0]))
q0 = RSL['pre-registered amplitude 0.5']
check("⛭ ② the slope statistic's phase systematic has fewer than four modes across the seven bands",
      3.0 < q0['n'] < 4.0, f"N_eff {q0['n']:.2f}")
check("     ...and the SLOPE's own effective count against it is nine at the pre-registered amplitude and five "
      "at the banks' own -- above the pre-registered four either way",
      all(r['n_slope'] > 4 for r in RSL.values()), ", ".join(f"{r['n_slope']:.1f}" for r in RSL.values()))
f12 = [r['S12'][0] / s12r for r in RSL.values()]
check("⛭⛭ ① at the REAL phase the null returns ALL of the reported slope, in its own direction, on both "
      "amplitudes", all(f > 1.0 for f in f12),
      ", ".join(f"{r['S12'][0]:+.4f} ({f*100:.0f} per cent)" for r, f in zip(RSL.values(), f12)))
check("     ...and on the single seven-band setting it reaches over half of the reported slope",
      q0['S7'][0] > 0.5 * s12r, f"{q0['S7'][0]:+.4f} against {s12r:+.4f}")
check("     ...so the rise does NOT survive the null's subtraction, on either amplitude",
      all(s12r - r['S12'][0] < sd12r for r in RSL.values()),
      ", ".join(f"{s12r - r['S12'][0]:+.4f}" for r in RSL.values()))
check("     the phase systematic's spread of the slope exceeds the reported setting spread",
      all(r['S12'].std() > sd12r for r in RSL.values()),
      ", ".join(f"{r['S12'].std():.4f}" for r in RSL.values()))

# ⛭⛭⛭ `r7681+cc66.1` -- ** THE SAME QUESTION THE STEP IS ALREADY ASKED, ASKED OF THE SLOPE: ON EACH
#   ARM'S OWN COMB, OR ON THE SHARED ONE? **  `r7681` (69) held `r7679`'s rewrite of `l.1781-1793`
#   because every check above is the SHARED-comb statistic and the paragraph did not say so, while the
#   step three screens up is explicitly comb-dependent.  `r7641` had measured the own-comb slope
#   SURVIVING its real-phase null, so the record carried two readings of two different statistics and
#   my routed sentence spoke as if there were one.
#   ⇒ The own-comb retention is 70's `retained_own` out of the module this file ALREADY imports for the
#     step (`r7637_70_own_comb_statistic`), lifted and not retyped, with 70's own `retention_null` for
#     the injection.  Nothing here is a new instrument.
#   ⌗ *Reproduced independently of 70's `measure_retention.txt`, and gated against it to the digit, so
#     this receipt answers the question the sentence that cites it asks.*
_BR = {t: dict(QL=QL[t], QK=QK[t], Dl=np.asarray(PR0[t]['Dl'], float),
               S2=np.asarray(SO0[t]['S_i'], float) ** 2) for t in PR0}
_CR_COMBS = OC.retention_combs(_BR)
_own12, _ownsd = OC.slope12(OC.retained_own, _BR, C=_CR_COMBS)
_shr12, _shrsd = OC.slope12(lambda b, w, nb, hi: OC.retained_shared(b, w, nb, hi), _BR)
_AD0 = float(np.mean([CPD[t][3] for t in CPD]))
_AS0 = float(np.mean([CPS[t][3] for t in CPS]))
# ⛭⛭⛭ `r7687+cc66`, ON 69's ORDER: ** THE SECOND PARAGRAPH'S OWN-COMB FIGURES ARE COMPUTED HERE OR
#   THE PARAGRAPH CANNOT CITE THIS FILE. **  `r7687` found four figures in cc66's routed draft of
#   `l.1779-1793` that are the SHARED statistic's, carried onto the own comb: the worst-phase fraction,
#   the carrier decomposition, `N_eff`, and the slope's effective count.  ⇒ *Three of the four were
#   never computed on the own comb at all.  The FIRST was -- the scan below has always visited all 24
#   phases at both amplitudes -- and the receipt kept only the fitted slope per phase and never said
#   what the worst of them was.  **A measured quantity the file keeps and never prints is as unciteable
#   as one it never measured**, which is why it is printed and pinned now.*
#   ⌗ ** AND THE COMBS ARE FITTED ONCE PER PHASE INSTEAD OF ONCE PER SETTING. **  `retained_own` does
#   `C = C or retention_combs(banks)`, and the twelve settings do not change the banks -- so the old
#   call refitted the same four combs twelve times per phase, 528 times over the scan, for identical
#   results.  Passing `C` is exactly equivalent and pays for the new figures.
_ownnull, _ownY, _ownS7 = {}, {}, {}
for _lab, _AL, _AK in (('pre-registered amplitude 0.5', 0.5, 0.5),
                       ("declared sensitivity: the banks' own amplitudes", _AD0, _AS0)):
    _ns, _ys, _s7 = [], [], []
    for _p in PH:
        _nb = OC.retention_null(_BR, _AL, _AK, _p)
        _Cp = OC.retention_combs(_nb)
        _ns.append(OC.slope12(OC.retained_own, _nb, C=_Cp)[0])
        _x7, _y7 = OC.retained_own(_nb, 1.0, 7, 5.75, C=_Cp)
        _ys.append(_y7)
        _s7.append(np.polyfit(_x7, _y7, 1)[0])
    _ownnull[_lab] = np.array(_ns)
    _ownY[_lab] = np.array(_ys)
    _ownS7[_lab] = np.array(_s7)
# the real-phase own-comb 7-band slope, the reference the effective count is taken against
_ox7, _oy7 = OC.retained_own(_BR, 1.0, 7, 5.75, C=_CR_COMBS)
_own_s7 = float(np.polyfit(_ox7, _oy7, 1)[0])
print(f"\n    ⛭ `r7681+cc66.1` -- THE SLOPE ON EACH ARM'S OWN COMB AND ON THE SHARED ONE")
print(f"      {'statistic':34s} {'twelve-setting slope':>22s} {'real-phase null':>16s} "
      f"{'slope - null':>13s} {'survives?':>10s}")
print(f"      {'shared comb (every check above)':34s} {f'{_shr12:+.5f} +- {_shrsd:.5f}':>22s} "
      f"{q0['S12'][0]:+16.5f} {_shr12 - q0['S12'][0]:+13.5f} "
      f"{('YES' if _shr12 - q0['S12'][0] > _shrsd else 'NO'):>10s}")
for _lab, _n in _ownnull.items():
    print(f"      {('own comb, ' + _lab.split(':')[0])[:34]:34s} "
          f"{f'{_own12:+.5f} +- {_ownsd:.5f}':>22s} {_n[0]:+16.5f} {_own12 - _n[0]:+13.5f} "
          f"{('YES' if _own12 - _n[0] > 2 * _ownsd else 'NO'):>10s}")
print(f"      ⇒ the own-comb slope is {_own12 / _shr12:.2f} of the shared-comb one, and its real-phase "
      f"null is {_ownnull['pre-registered amplitude 0.5'][0] / q0['S12'][0]:.2f} of the shared one's")
check(f"⛔⛭⛭⛭ `r7681` ① ** THE RECONCILIATION: THE SLOPE SURVIVES ITS REAL-PHASE NULL ON EACH ARM'S OWN "
      f"COMB AND DOES NOT ON THE SHARED ONE, so `r7641`'s reading and `r7679`'s are two statistics and "
      f"not a contradiction. **  On the own comb the twelve-setting slope is "
      f"`${_own12:+.5f}\\pm{_ownsd:.5f}$` against a real-phase null of "
      f"`${_ownnull['pre-registered amplitude 0.5'][0]:+.5f}$`, surviving at "
      f"`${_own12 - _ownnull['pre-registered amplitude 0.5'][0]:+.5f}$`; on the shared comb it is "
      f"`${_shr12:+.5f}\\pm{_shrsd:.5f}$` against `${q0['S12'][0]:+.5f}$`, which is "
      f"`${100 * q0['S12'][0] / _shr12:.0f}$` per cent of it and leaves nothing.  *⛔ `r7679` routed the "
      f"shared-comb reading as THE claim without naming the comb, which is exactly the omission 69 "
      f"caught -- and the step in the same paragraph had named it all along*",
      _own12 - _ownnull['pre-registered amplitude 0.5'][0] > 2 * _ownsd
      and all(_own12 - _n[0] > 2 * _ownsd for _n in _ownnull.values())
      and _shr12 - q0['S12'][0] < _shrsd)
check(f"     ⛭⛭ ** AND THE OWN-COMB SLOPE IS NEARLY INVARIANT UNDER THE REPOINT WHERE THE SHARED-COMB ONE "
      f"DOUBLES, which is the mechanism and not a coincidence: ** `$+0.01002$` to `${_own12:+.5f}$` on "
      f"the own comb, `$+0.01359$` to `${_shr12:+.5f}$` on the shared one.  *The arms' combs PARTING is "
      f"what the repoint changed, and a statistic that carries each arm onto its own comb cannot see "
      f"it while one that imposes a common comb reads it as retention.*  ⌗ *70's "
      f"`measure_retention.txt` reports `$+0.01034$` and `$+0.02690$` on this arm; reproduced here to "
      f"the digit from the same banks through the same lifted module*",
      abs(_own12 - 0.01034) < 5e-5 and abs(_shr12 - 0.02690) < 5e-5
      and abs(_own12 / 0.01002 - 1) < 0.10 and _shr12 / 0.01359 > 1.8,
      f"own {_own12:+.5f} (was +0.01002), shared {_shr12:+.5f} (was +0.01359)")

# ===================================================================================================
# ⛭⛭⛭ `r7687+cc66` ITEM 1 -- ** THE FOUR FIGURES `l.1779-1793` PRINTS THAT THIS FILE DID NOT COMPUTE
#   ON THE OWN COMB. **  Each is printed and pinned here, and each is labelled with the statistic it
#   belongs to, so the paragraph cannot carry a shared-comb number as an own-comb one again.
print("\n    \u26ed `r7687+cc66` -- THE SECOND PARAGRAPH'S FOUR FIGURES, ON THE OWN COMB")
print(f"      {'figure':44s} {'own comb':>18s} {'shared comb':>18s}")

# ① the worst phase of the scan, as a fraction of the slope -- ALREADY SCANNED, never printed
_own_worst = {k: float(np.abs(v).max()) for k, v in _ownnull.items()}
# ⌗ `r7687`: the shared column is read from `RSL[_lab]`, THE SAME AMPLITUDE, not from `q0` twice.
#   *A first writing of this block printed amplitude 0.5's shared value on both rows -- a column
#   labelled per-amplitude carrying one amplitude's number, which is this revision's own lesson
#   arriving in the table that reports it.*
for _lab, _w in _own_worst.items():
    print(f"      {('worst phase / slope, ' + _lab.split(':')[0])[:44]:44s} "
          f"{_w / _own12:>18.2f} "
          f"{float(np.abs(RSL[_lab]['S12']).max()) / _shr12:>18.2f}")
check("⛭ `r7687` ① ** THE WORST PHASE OF THE SCAN REACHES ABOUT HALF THE OWN-COMB SLOPE, which is the "
      "'factor of two' clause and was computed by this file all along without being printed **",
      all(0.45 < _w / _own12 < 0.60 for _w in _own_worst.values()),
      ", ".join(f"{_w / _own12:.2f}" for _w in _own_worst.values()))

# ② the carrier, in the OWN convention -- and it does not transplant, it inverts
_oneC = {t: _CR_COMBS['lcdm'] for t in _CR_COMBS}          # one comb for both arms = the shared form
_car_one = OC.slope12(OC.retained_own, OC.retention_null(_BR, 0.5, 0.5, PH[0]), C=_oneC)[0]
_flatB = {t: dict(QL=_BR[t]['QL'], QK=_BR[t]['QK'],
                  Dl=np.ones_like(_BR[t]['Dl']), S2=np.ones_like(_BR[t]['S2']))
          for t in _BR}
_fn = OC.retention_null(_flatB, 0.5, 0.5, PH[0])
_car_flat = OC.slope12(OC.retained_own, _fn, C=OC.retention_combs(_fn))[0]
_car_real = _ownnull['pre-registered amplitude 0.5'][0]
print(f"      {'null at the real phase':44s} {_car_real:>18.5f} {q0['S12'][0]:>18.5f}")
print(f"      {'...with ONE comb for both arms':44s} {_car_one:>18.5f} {'(is the shared)':>18s}")
print(f"      {'...with the envelope flattened':44s} {_car_flat:>18.5f} {'':>18s}")
check("⛔⛭⛭ `r7687` ② ** THE CARRIER CLAUSE DOES NOT TRANSPLANT ONTO THE OWN COMB -- IT INVERTS. ** "
      "'Give both arms one comb and the null slope falls' is a SHARED-comb statement: one comb for "
      "both arms IS the shared convention, so on the own comb it RAISES the null instead of removing "
      "it.  \u21d2 *The own comb is what removes the carrier and one comb is what restores it, which "
      "is the same sentence read from the other end*",
      abs(_car_one) > 3 * abs(_car_real),
      f"own-comb null {_car_real:+.5f} -> {_car_one:+.5f} under one comb, a factor of "
      f"{abs(_car_one / _car_real):.1f} UP (the shared form reads {q0['S12'][0]:+.5f})")
# ⛭ `r7691+cc66`, ON 60's `r7692`: ** AND `_car_flat` IS GATED, WHICH IT WAS NOT. **
#   *I added `_car_flat` to the table above at `r7687` and printed `-0.00003`, and the clause 69
#   landed -- "flattening them leaving nothing" -- RESTS ON IT.  It was the one figure in that table
#   with no check.  60 found that, not me: my own commitment ⑦ says enumerate every assertion the
#   patch adds, and I enumerated the four I WROTE and not the figure I PRINTED BESIDE THEM.*
check("⛭ `r7691` ** FLATTENING THE ENVELOPES LEAVES UNDER A TENTH OF THE OWN-COMB NULL, which is what "
      "the landed carrier clause rests on and had no check until now **",
      abs(_car_flat) < 0.1 * abs(_car_real),
      f"flat {_car_flat:+.5f} against a tenth of the real-phase null, "
      f"{0.1 * abs(_car_real):+.5f}; a factor of {abs(_car_real / _car_flat):.0f} under it")

# ③④ the effective counts, on the own comb
_own_neff = {k: neff(v) for k, v in _ownY.items()}
_own_nslope = {k: 7 * (_own_s7 / _ownS7[k].std()) ** 2 for k in _ownS7}
for _lab in _ownY:
    print(f"      {('N_eff of 7, ' + _lab.split(':')[0])[:44]:44s} "
          f"{_own_neff[_lab]:>18.2f} {RSL[_lab]['n']:>18.2f}")
    print(f"      {('slope effective count, ' + _lab.split(':')[0])[:44]:44s} "
          f"{_own_nslope[_lab]:>18.1f} {RSL[_lab]['n_slope']:>18.1f}")
check("⛭ `r7687` ③ ** THE OWN COMB'S BAND COUNT IS ITS OWN AND NOT THE SHARED ONE'S, so "
      "l.1789's 'two to three and a half' cannot be carried across: it was the shared statistic's **",
      all(1.0 < v < 7.0 for v in _own_neff.values())
      and all(abs(v - RSL[k]['n']) > 0.5 for k, v in _own_neff.items()),
      ", ".join(f"{k.split(':')[0]} {v:.2f} (shared {RSL[k]['n']:.2f})"
                for k, v in _own_neff.items()))
check("⛭ `r7687` ④ ** AND THE OWN-COMB SLOPE'S EFFECTIVE COUNT EXCEEDS THE SHARED ONE ON BOTH "
      "AMPLITUDES, because the count falls with the null's spread over phase and the own-comb null is "
      "the smaller -- so l.1790's 'nine and eighteen' is wrong for the own comb in the UPWARD "
      "direction, not merely unmeasured **",
      all(v > RSL[k]['n_slope'] for k, v in _own_nslope.items()),
      ", ".join(f"{v:.1f} against the shared {RSL[k]['n_slope']:.1f}"
                for k, v in _own_nslope.items()))

print()
print("  WHERE IT COMES FROM -- the two sides of the ratio at the real phase, and a flat-envelope control")
osc = NS2['osc']
pr, so = inject(0.5, 0.5, 0.0)
ed = np.linspace(0.85, 5.75, 8)
dr, sr = [], []
for a, b in zip(ed[:-1], ed[1:]):
    g = np.linspace(a, b, 400)
    d = {t: np.interp(g, QL[t], osc(QL[t], pr[t]['Dl'], 1.0)).std() for t in pr}
    s = {t: np.interp(g, QK[t], osc(QK[t], so[t]['S_i'] ** 2, 1.0)).std() for t in so}
    dr.append(d['cr'] / d['lcdm'] - 1)
    sr.append(s['cr'] / s['lcdm'] - 1)
    print(f"    {a:5.2f}-{b:5.2f}   D_l side {dr[-1]:+.4f}   source side {sr[-1]:+.4f}")
check("⛭ on the arm of record NEITHER side cancels: the D_l null reaches five per cent and more (the arms' D_l "
      "combs have parted too), the source null eight", max(map(abs, dr)) > 0.05 and max(map(abs, sr)) > 0.08,
      f"D_l worst {max(map(abs, dr))*100:.2f}, source worst {max(map(abs, sr))*100:.2f} per cent")
print()
print("  AND WHICH PART OF THE SOURCE SIDE: each arm's own comb or one comb for both, x own or flat envelope")


def inject2(AS, same, flat):
    pr, so = {}, {}
    for t in PR0:
        e, T, ph, _ = CPD[t]
        pr[t] = {'Dl': e * (1 + 0.5 * np.cos(2 * np.pi * QL[t] / T + ph))}
        e, T, ph, _ = CPS[t]
        if same:
            T, ph = CPS['lcdm'][1], CPS['lcdm'][2]
        e = np.ones_like(e) if flat else e
        so[t] = {'S_i': np.sqrt(np.maximum(e * (1 + AS * np.cos(2 * np.pi * QK[t] / T + ph)), 0.0))}
    return pr, so


DEC = {}
for AS in (0.5, float(np.mean([CPS[t][3] for t in CPS]))):
    for same in (False, True):
        for flat in (False, True):
            DEC[(AS > 0.6, same, flat)] = slopes(*inject2(AS, same, flat))[3]
            print(f"    source amplitude {AS:.3f}, {'one comb' if same else 'own combs'}, "
                  f"{'flat' if flat else 'own'} envelope: twelve-setting null slope {DEC[(AS > 0.6, same, flat)]:+.5f}")
dphi = [2 * np.pi * q * (1 / CPS['cr'][1] - 1 / CPS['lcdm'][1]) + CPS['cr'][2] - CPS['lcdm'][2] for q in (0.85, 5.75)]
print(f"    the two arms' source combs: periods {CPS['lcdm'][1]:.4f} / {CPS['cr'][1]:.4f}, so their phase "
      f"difference runs {dphi[0]:+.3f} to {dphi[1]:+.3f} rad across the range")
check("⛭⛭ the carrier is still the arms' own SOURCE COMBS: with one comb for both the null slope falls to a "
      "third or less, while a flat envelope keeps most of it",
      all(abs(DEC[(k, True, False)]) < 0.3 * abs(DEC[(k, False, False)])
          and abs(DEC[(k, False, True)]) > 0.6 * abs(DEC[(k, False, False)]) for k in (False, True)),
      f"own/own {DEC[(False, False, False)]:+.4f}, one comb {DEC[(False, True, False)]:+.4f}, "
      f"flat envelope {DEC[(False, False, True)]:+.4f}")
check("     ...and that drift is now FOUR TIMES the pre-registered 0.05 rad (it was under it on the LEAFREC=0 "
      "arm), which is why the null now carries the whole slope", max(map(abs, dphi)) > 0.15,
      f"{max(map(abs, dphi)):.3f} rad")

# ===================================================================================================
# ⛭⛭⛭ `r7693+cc66` ITEM 4, ON 69's ORDER: ** THE DIP TEST, SO ITS LICENCE IS CITEABLE. **
#   *`r7691` registered that the own-comb null's real-phase band response does NOT reproduce the
#   `q ~ 1.9` departure of the retention from the parameter-free acceptance law, and the measurement
#   FALSIFIED that: it does, and at the real phase specifically.  It lived in a computation directory,
#   so the sentence it licenses could cite nothing.  Computed here, in the receipt that owns the phase
#   systematic.*
#   ⌗ ** AND IT IS CHEAPER THAN THE 37 s I PRICED IT AT, because the 24-phase scan above ALREADY
#     CAPTURED EVERY BAND VALUE IT NEEDS. **  *`_ownY[label]` is `(24, 7)` -- the own-comb band values
#     at every injection phase, kept since `r7687`.  The only new work is the law's seven bands: two
#     bank reads and an interpolation.  ⇒ *I quoted the cost of re-running the scan; the scan was
#     already paid for, and a price quoted without reading what the file already holds is an estimate
#     of the wrong computation.*
_ACC = {t: os.path.join(SP, f'r7041_accept_{n}.npz')
        for t, n in (('lcdm', 'lcdm'), ('cr', 'cr_leafrec1'))}
for _t, _pth in _ACC.items():
    check(f"⛭ `r7693` the acceptance-law bank the dip test needs is present: "
          f"`spectra/{os.path.basename(_pth)}`", os.path.exists(_pth), os.path.basename(_pth))
_AZ = {t: dict(np.load(_ACC[t], allow_pickle=True)) for t in _ACC}
_AQ = {t: np.asarray(_AZ[t]['ls__fixed'], float) / float(_AZ[t]['l_A__fixed']) for t in _AZ}
_AA = {t: np.asarray(_AZ[t]['A'], float) for t in _AZ}


def _lawband(_a, _b):
    """the law's arm/control acceptance ratio over one band, by its band MEAN -- `A_l` is already an
    amplitude fraction, so an RMS of it would be a statistic of a statistic (`r7689` arm 5)"""
    _g = np.linspace(_a, _b, 400)
    return (np.interp(_g, _AQ['cr'], _AA['cr']).mean()
            / np.interp(_g, _AQ['lcdm'], _AA['lcdm']).mean())


_ED7 = np.linspace(0.35 + 0.5 + 1e-9, 5.75, 8)
_LAW7 = np.array([_lawband(_a, _b) for _a, _b in zip(_ED7[:-1], _ED7[1:])])
_DEP = _oy7 - _LAW7                      # the measurement's departure from the law, band by band
_J19 = int(np.argmax(np.abs(_DEP)))


def _detr(_y):
    return _y - np.polyval(np.polyfit(_ox7, _y, 1), _ox7)


_MD = _detr(_oy7)
print(f"\n    \u26ed `r7693` THE DIP TEST -- the null's real-phase band response against the "
      f"departure at q = {_ox7[_J19]:.2f}")
print(f"      the departure: measured {_oy7[_J19]:.4f} against the law's {_LAW7[_J19]:.4f}, "
      f"{_DEP[_J19]:+.4f}; detrended {_MD[_J19]:+.4f}")
print(f"      {'amplitude':46s} {'at q=1.9':>10s} {'of meas':>9s} {'corr':>7s} "
      f"{'rank':>7s} {'|corr|>0.8':>11s}")
_DIP = {}
for _lab in _ownY:
    _Y = _ownY[_lab]
    _nd0 = _detr(_Y[0])
    _cs = np.array([float(np.corrcoef(_detr(_Y[_k]), _MD)[0, 1]) for _k in range(len(PH))])
    _fs = np.array([float(_detr(_Y[_k])[_J19] / _MD[_J19]) for _k in range(len(PH))])
    _rank = int(np.sum(_cs >= _cs[0]))
    _DIP[_lab] = dict(nd=_nd0[_J19], frac=_fs[0], corr=_cs[0], rank=_rank,
                      rank_f=int(np.sum(_fs >= _fs[0])), hi=int(np.sum(np.abs(_cs) > 0.8)))
    print(f"      {_lab:46s} {_nd0[_J19]:+10.4f} {_fs[0]:+9.3f} {_cs[0]:+7.3f} "
          f"{str(_rank) + ' of ' + str(len(PH)):>7s} {_DIP[_lab]['hi']:>11d}")
_P05 = _DIP['pre-registered amplitude 0.5']
_POW = _DIP["declared sensitivity: the banks' own amplitudes"]
for _nm, _got, _want, _tol, _fmt in (
        ("the null's detrended response at q = 1.9, pre-registered amplitude", _P05['nd'], 0.0157, 5e-5, '.4f'),
        ("...as a fraction of the measured departure there", _P05['frac'], 1.185, 5e-4, '.3f'),
        ("...and its seven-band shape correlation", _P05['corr'], 0.922, 5e-4, '.3f'),
        ("the same at the banks' own amplitudes", _POW['nd'], 0.0098, 5e-5, '.4f'),
        ("...as a fraction", _POW['frac'], 0.741, 5e-4, '.3f'),
        ("...and its correlation", _POW['corr'], 0.957, 5e-4, '.3f')):
    check(f"⛭ `r7693` {_nm} is {_want:{_fmt}}", abs(_got - _want) < _tol,
          f"{_got:{_fmt}} against {_want:{_fmt}}")
check("⚑⛭⛭ ** THE MATCH IS NOT A PROPERTY OF THE BANDING: scanned over all 24 injection phases the "
      "REAL phase is rank 1 of 24 at the pre-registered amplitude and rank 2 of 24 at the banks' "
      "own, on both the correlation and the fraction reproduced. **  ⇒ *LICENSED: the `q ~ 1.9` "
      "departure is CONSISTENT IN SHAPE with the phase systematic's own real-phase band response, "
      "and specifically so rather than generically.*  ⛔ *NOT LICENSED -- 'the departure is the "
      "drift': the injection amplitude is CHOSEN, and the fraction swings 1.185 against 0.741 "
      "between two defensible choices, so the SIZE carries no information and only the shape does; "
      "the drift was never turned OFF in the measurement, which is the route that made the "
      "octopole's clock attribution legitimate; and the detrended shape is essentially ONE MODE "
      "whose sign flips with phase -- ten of the 24 align or anti-align above 0.8 in absolute value "
      "at the pre-registered amplitude and eight at the banks' own -- so it is the SIGN and the "
      "MAXIMUM that pick the real phase out, not the existence of a matching shape*",
      _P05['rank'] == 1 and _P05['rank_f'] == 1 and _POW['rank'] == 2 and _POW['rank_f'] == 2
      and _P05['hi'] == 10 and _POW['hi'] == 8,
      f"rank {_P05['rank']}/{_P05['rank_f']} of {len(PH)} at 0.5 and {_POW['rank']}/{_POW['rank_f']} "
      f"at the banks' own; |corr| > 0.8 at {_P05['hi']} and {_POW['hi']} of {len(PH)}")
check("⛔⛭ ** AND THE REGISTERED PREDICTION WAS THE OTHER WAY: `r7691` registered that the null does "
      "NOT reproduce the departure, with a licence ceiling fixed for the case it judged would not "
      "arrive. **  *The ceiling held, and the honest reading of that register is worse than that: a "
      "negative result licenses nothing and so cannot be misread, so the outcome registered was the "
      "one that would have left the rule untested.*  ⇒ What would settle it is a build with the "
      "drift REMOVED, read at these same seven bands -- a bank request, not an analysis available "
      "here, and until it exists nothing is drafted past the ceiling above",
      _P05['nd'] > 0 and _DEP[_J19] > 0 and abs(_ox7[_J19] - 1.90) < 0.05,
      f"the null carries {_P05['nd']:+.4f} where the registration said it carried no feature "
      f"matching the departure's {_DEP[_J19]:+.4f}, at q = {_ox7[_J19]:.2f}")

print()
print("  THE PAPER'S WORDING -- REPORTED, NEVER REQUIRED")
tex = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read())
w = re.search(r'with a slope of \$\+?[\d.]+\$ per acoustic period[^.]*', tex)
print("    P15 reads: " + (f"\"...{w.group(0)[:170]}...\"" if w else "the slope clause is no longer present"))

print()
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print()
# ⛭⛭⛭ `r7683+cc66.1` -- ** THE VERDICT NOW COVERS THE SLOPE ON THE OWN COMB EXACTLY AS IT COVERS
#   THE STEP, WHICH IS `r7683`'s RULING 1 AND 60's BRANCH (b). **  It said "the retention slope's
#   [null] is all of it" and then named the own comb for the STEP alone -- true of the shared-comb
#   statistic and silent about the one 69 has now made the reading of record.
#   ⇒ `r7639+70` calls the shared reading "the beat and not a measurement", so the own comb is the
#     convention for BOTH statistics and the verdict says so for both.  ⌗ *Every digit below is
#     interpolated from what this file computes -- the fifth process commitment -- so the two
#     conventions cannot drift apart in the prose again.*
print(f"  VERDICT (the arm of record, r7637; the OWN-COMB convention, r7683 ruling 1):")
print(f"  ** ON EACH ARM'S OWN COMB BOTH BANDED STATISTICS SURVIVE THEIR PHASE SYSTEMATIC. **  The")
print(f"  step is {s_own:+.4f} against a real-phase null of {N_OWN[0.5][0]:+.4f} to "
      f"{[n[0] for A, n in N_OWN.items() if A != 0.5][0]:+.4f}; the retention slope is "
      f"{_own12:+.5f} +- {_ownsd:.5f}")
print(f"  against {_ownnull['pre-registered amplitude 0.5'][0]:+.5f} to "
      f"{list(_ownnull.values())[1][0]:+.5f}, surviving at "
      f"{_own12 - _ownnull['pre-registered amplitude 0.5'][0]:+.5f} to "
      f"{_own12 - list(_ownnull.values())[1][0]:+.5f}.")
print(f"  ** ON THE SHARED COMB NEITHER DOES: ** the step's null is {abs(RS[list(RS)[0]]['s'][0])/STEP_REPORTED:.0%} "
      f"or more of it and the slope's is {q0['S12'][0]/_shr12:.0%} of it.")
print(f"  *⇒ Which is why `r7639+70` calls the shared reading the BEAT and not a measurement, and why")
print(f"  `r7683` ruling 1 puts `l.1773` on the own comb.  The LEAFREC=0 reading (a third of the slope,")
print(f"  the step standing on the shared comb) is the docstring's below; the arms' combs have since")
print(f"  parted, D_l and source alike, and the shared statistic reads that parting.*")
