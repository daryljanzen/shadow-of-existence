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
print("  VERDICT (the arm of record, r7637): ** on the shared comb neither banded statistic survives its")
print("  phase systematic -- the step's null is half or more of it, the retention slope's is all of it.")
print("  On each arm's own comb the step stands: -0.0396 against a null at most a third of it. **")
print("  *The LEAFREC=0 reading (a third of the slope, the step standing on the shared comb) is the")
print("  docstring's below; the arms' combs have since parted, D_l and source alike.*")
