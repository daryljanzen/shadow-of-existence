"""
P15_the_laws_six_of_seven_is_five_at_the_quoted_floor_which_is_one_phases_and_with_the_instruments_own_error_divided_out_all_seven_hold

r7049 -> 70: THE FLOOR UNDER THE ACCEPTANCE LAW'S TEST.  Pre-registered at
`computations/beyond_the_wall/r7049_70_the_laws_floor/PREDICTION.md`, committed before this file.

The claim audited, as landed in `P15` `sec:refit-bound` and in `cc66`'s receipt's gate ⓸:
  "...holds on both arms to within ten per cent everywhere, worst deviation 6.7 per cent, six of the
   seven bands on each arm landing inside the measuring statistic's own 3.74 per cent accuracy on a
   known injected comb..."

The instrument is `cc66`'s -- `env_a`, `osc`, `_fit`, `fit_period`, `band_amp` and the band edges -- and it is
LIFTED FROM THAT RECEIPT'S SOURCE BY ITS SYNTAX TREE AND EXECUTED UNCHANGED.  So nothing here is a
re-implementation, and a change there is a change here.  That receipt is not edited, and its gate ⓪ is not
re-run as a verdict on it.

⛭ WHAT IS FOUND
  ② "Six of seven inside 3.74 per cent" is FIVE of seven on each arm.  The gate counts at 5 per cent, and its
     label names 3.74.  The band at 3.65-4.35 sits at 4.2 / 4.4 per cent.
  ③ The 3.74 per cent is ONE PHASE's error and not the statistic's floor.
     - Gate ⓪ injects one constant-amplitude comb at one phase (0.7), on the control's envelope only.
     - Scanned over phase, at each arm's own period and with the law's own amplitude profile, the worst
       band error is 10.2 per cent (control) and 11.0 per cent (arm).
     - The phase is NOT unknown here, though: the real comb's fitted phase is 0.686, close to the gate's 0.7.
       At that phase the instrument's error is -4.2 / -4.0 per cent in the LOWEST band and under one per cent
       in the other six.
  ① So the pre-registered ① fires on its phase-agnostic arm (F_t > 10 per cent), and it does NOT fire on the
     one that bears on the claim.
     - With the instrument's own error at the real phase divided out, the law and the measurement agree to
       3.4 / 3.6 per cent at worst.
     - ALL SEVEN bands on both arms then land inside 3.74 per cent.
     - The lowest band's 6.3 / 6.7 per cent deviation is two thirds instrument.
     ⇒ The law is BETTER supported than the landed sentence says, and the sentence's count is wrong.
  ④ "Six of seven ON EACH ARM" reads as two tests, and it is ONE.
     - The two arms' deviation patterns correlate at 0.998.
     - Within an arm, the seven band measurements ARE close to independent: N_eff about 6.7 of 7 under the
       instrument's own noise response.
     - The instrument's phase systematic has only about 2.4 independent modes across the seven bands.

⛔ NOT CLAIMED.  No verdict on the law's physics or on `cc66`'s convergence sweep.  No edit to any other
receipt and no prose edited: routed to 66.  The white noise in M3(b) probes the instrument's coupling
between bands.  It is not a noise model for the spectra.
"""
import ast
import os
import re

import numpy as np

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
QUOTED = 0.0374            # the figure the sentence and the gate's label quote
GATE_COUNT_TOL = 0.05      # the threshold the gate's code counts at
NPH, NDRAW, SIG = 24, 400, 0.02

print(__doc__)
print("=" * 100)

# ---- the instrument, lifted from cc66's receipt by its syntax tree and run unchanged ----
src = open(LAW, encoding='utf-8').read()
tree = ast.parse(src)
FN = ('env_a', 'osc', '_fit', 'fit_period', 'band_amp')
body = []
for n in tree.body:
    if isinstance(n, ast.FunctionDef) and n.name in FN:
        body.append(n)
    elif isinstance(n, ast.Assign):
        names = [e.id for t in n.targets for e in (t.elts if isinstance(t, ast.Tuple) else [t])
                 if isinstance(e, ast.Name)]
        if 'ED' in names or 'LO' in names:
            body.append(n)
NS = {'np': np}
exec(compile(ast.Module(body=body, type_ignores=[]), LAW, 'exec'), NS)
env_a, osc, fit_period, band_amp = NS['env_a'], NS['osc'], NS['fit_period'], NS['band_amp']
ED, LO, HI = NS['ED'], NS['LO'], NS['HI']
BANDS = list(zip(ED[:-1], ED[1:]))
check("the instrument is lifted whole from `cc66`'s receipt: five functions, the band edges and the range",
      all(k in NS for k in FN) and len(BANDS) == 7 and (LO, HI) == (0.85, 5.75),
      f"{len(BANDS)} bands, {ED[1]-ED[0]:.2f} wide, range {LO}-{HI}")
m0 = re.search(r'A0, P0, PH0 = ([\d.]+), ([\d.]+), ([\d.]+)', src)
A0, P0, PH0 = (float(x) for x in m0.groups())
print(f"    gate ⓪'s known input, read from that receipt: amplitude {A0} constant, period {P0}, "
      f"phase {PH0}, on the control's envelope only")


def fit_phase(q, o, T):
    """the phase of the whole-range fit at period T -- `_fit`'s own design matrix, its cos/sin kept"""
    m = (q >= LO) & (q <= HI)
    x = q[m]
    X = np.column_stack([np.cos(2 * np.pi * x / T), np.sin(2 * np.pi * x / T), np.ones_like(x), x])
    c, *_ = np.linalg.lstsq(X, o[m], rcond=None)
    return float(np.arctan2(-c[1], c[0]))


def neff(M):
    lam = np.linalg.eigvalsh(np.corrcoef(M.T))
    return float(lam.sum() ** 2 / (lam ** 2).sum())


R = {}
for t in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r7041_accept_{t}.npz'))
    q = d['q__fixed']
    Dl = np.asarray(d['Dl__fixed'], float)
    A = np.asarray(d['A'], float)
    ok = np.isfinite(A)
    Af = np.interp(q, q[ok], A[ok])
    o = osc(q, Dl)
    T = fit_period(q, o)
    ph = fit_phase(q, o, T)
    E = env_a(q, Dl)
    law = np.array([A[(q >= a) & (q <= b) & ok].mean() for a, b in BANDS])
    mea = np.array([band_amp(q, o, a, b, T) for a, b in BANDS])
    inj = np.array([Af[(q >= a) & (q <= b)].mean() for a, b in BANDS])

    def measure(s):
        oo = osc(q, s)
        Tg = fit_period(q, oo)
        return np.array([band_amp(q, oo, a, b, Tg) for a, b in BANDS])

    def comb(phi):
        return E * (1.0 + Af * np.cos(2 * np.pi * q / T + phi))

    phis = np.linspace(0, 2 * np.pi, NPH, endpoint=False)
    Eph = np.array([measure(comb(p)) / inj - 1 for p in phis])
    e_own = measure(comb(ph)) / inj - 1
    rng = np.random.default_rng(7049)
    s0 = comb(ph)
    Bn = np.array([measure(s0 * (1 + SIG * rng.standard_normal(len(q)))) for _ in range(NDRAW)])
    R[t] = dict(T=T, ph=ph, law=law, mea=mea, r=law / mea, e=e_own, Eph=Eph,
                rc=law * (1 + e_own) / mea, neff_b=neff(Bn), neff_c=neff(Eph))

print()
print("  " + "=" * 96)
print("  M1  THE LITERAL COUNT -- the gate's own ratios, recomputed through its own functions")
print("  " + "=" * 96)
print(f"    {'band':>12s}   {'lcdm law/meas':>13s}   {'cr law/meas':>11s}")
for i, (a, b) in enumerate(BANDS):
    print(f"    {a:5.2f}-{b:5.2f}   {R['lcdm']['r'][i]:13.4f}   {R['cr']['r'][i]:11.4f}")
worst = max(np.abs(R[t]['r'] - 1).max() for t in R)
check("the recomputation IS the landed table: worst deviation 6.7 per cent",
      abs(worst * 100 - 6.7) < 0.05, f"{worst*100:.2f} per cent")
n374 = {t: int((np.abs(R[t]['r'] - 1) < QUOTED).sum()) for t in R}
n5 = {t: int((np.abs(R[t]['r'] - 1) < GATE_COUNT_TOL).sum()) for t in R}
check("⛭ ② inside the QUOTED 3.74 per cent: FIVE of seven on each arm, not six",
      n374 == {'lcdm': 5, 'cr': 5}, f"lcdm {n374['lcdm']}/7, cr {n374['cr']}/7")
check("     ...and six of seven is the count at 5 per cent, which is the threshold the gate's code uses",
      n5 == {'lcdm': 6, 'cr': 6}, f"lcdm {n5['lcdm']}/7, cr {n5['cr']}/7")
_mislabel = 'abs(r[2] - 1) < 0.05' in src and 'accuracy on a known input' in src
print("    ⌗ REPORTED, never required: the gate's label against its count, in `cc66`'s source now -- "
      + ("still counting at 5 per cent under the 3.74 label" if _mislabel
         else "the label no longer names 3.74 against a 5 per cent count (corrected there)"))

print()
print("  " + "=" * 96)
print("  M2  DOES THE 3.74 PER CENT TRANSFER TO WHERE THE REAL BANDS ARE?")
print("  " + "=" * 96)
for t in R:
    print(f"    {t}: the real comb's fitted period {R[t]['T']:.4f}, phase {R[t]['ph']:.3f} "
          f"(gate ⓪ injected {P0}, {PH0})")
print(f"\n    injected: each arm's own envelope and grid, the law's own A_l(q) profile, its own period;")
print(f"    the band error e = measured / injected band mean - 1, in per cent")
print(f"    {'band':>12s} {'lcdm e(own)':>12s} {'worst/phase':>12s} {'cr e(own)':>10s} {'worst/phase':>12s}")
for i, (a, b) in enumerate(BANDS):
    print(f"    {a:5.2f}-{b:5.2f} {R['lcdm']['e'][i]*100:12.2f} {np.abs(R['lcdm']['Eph'][:, i]).max()*100:12.2f}"
          f" {R['cr']['e'][i]*100:10.2f} {np.abs(R['cr']['Eph'][:, i]).max()*100:12.2f}")
Ft = {t: float(np.abs(R[t]['Eph']).max()) for t in R}
check("⛭ ③ scanned over phase, the statistic's worst band error is TEN per cent and more on both arms -- "
      "so 3.74 per cent is ONE phase's error and not the statistic's floor",
      all(Ft[t] > 0.08 for t in R), f"lcdm {Ft['lcdm']*100:.1f}, cr {Ft['cr']*100:.1f} per cent")
check("     ...but the phase is MEASURED, and gate ⓪'s 0.7 sits within 0.03 rad of the real comb's",
      all(abs(R[t]['ph'] - PH0) < 0.03 for t in R),
      ", ".join(f"{t} {R[t]['ph']:.3f}" for t in R))
check("     at the real phase the instrument's error is about -4 per cent in the LOWEST band and under one "
      "per cent in the other six, on both arms",
      all(-0.05 < R[t]['e'][0] < -0.03 and np.abs(R[t]['e'][1:]).max() < 0.01 for t in R),
      ", ".join(f"{t} {R[t]['e'][0]*100:.2f} / {np.abs(R[t]['e'][1:]).max()*100:.2f}" for t in R))
print(f"\n    the corrected ratio r_c = law x (1 + e_own) / measured -- the deviation the instrument cannot "
      f"account for")
print(f"    {'band':>12s} {'lcdm r_c':>10s} {'cr r_c':>10s}")
for i, (a, b) in enumerate(BANDS):
    print(f"    {a:5.2f}-{b:5.2f} {R['lcdm']['rc'][i]:10.4f} {R['cr']['rc'][i]:10.4f}")
wrc = {t: float(np.abs(R[t]['rc'] - 1).max()) for t in R}
check("⛭⛭ ① with the instrument's own error divided out the law holds to under four per cent at every "
      "band -- far inside ten", all(wrc[t] < 0.04 for t in R),
      f"worst lcdm {wrc['lcdm']*100:.2f}, cr {wrc['cr']*100:.2f} per cent")
check("     ...ALL SEVEN bands on both arms then land inside the quoted 3.74 per cent",
      all((np.abs(R[t]['rc'] - 1) < QUOTED).sum() == 7 for t in R))
share = {t: 1 - abs(R[t]['rc'][0] - 1) / abs(R[t]['r'][0] - 1) for t in R}
check("     ...and the lowest band's 6.3 / 6.7 per cent deviation is mostly the instrument's",
      all(share[t] > 0.5 for t in R), ", ".join(f"{t} {share[t]*100:.0f} per cent" for t in R))

print()
print("  " + "=" * 96)
print("  M3  HOW MANY INDEPENDENT MEASUREMENTS IS 'SIX OF SEVEN ON EACH ARM'?")
print("  " + "=" * 96)
for t in R:
    print(f"    {t}: the range spans {(HI-LO)/R[t]['T']:.2f} comb periods, each band "
          f"{(ED[1]-ED[0])/R[t]['T']:.2f} of one")
for t in R:
    check(f"(b) {t}: under the instrument's own noise response the seven band amplitudes are CLOSE TO "
          f"independent ({NDRAW} draws, the whole instrument each time)", R[t]['neff_b'] > 6.0,
          f"N_eff {R[t]['neff_b']:.2f} of 7")
for t in R:
    check(f"(c) {t}: the instrument's PHASE systematic has few independent modes across the bands",
          R[t]['neff_c'] < 3.5, f"N_eff {R[t]['neff_c']:.2f} of 7")
cr_ = float(np.corrcoef(R['lcdm']['r'] - 1, R['cr']['r'] - 1)[0, 1])
ce_ = float(np.corrcoef(R['lcdm']['e'], R['cr']['e'])[0, 1])
check("⛭ ④ (d) the two arms' deviation patterns are ONE pattern, so 'on each arm' is one test and not two",
      cr_ > 0.99, f"correlation {cr_:.4f}")
check("     ...and so are the instrument's own errors at the two arms' phases", ce_ > 0.99,
      f"correlation {ce_:.4f}")

print()
print("  " + "=" * 96)
print("  THE PAPER'S WORDING -- REPORTED, NEVER REQUIRED")
print("  " + "=" * 96)
tex = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read())
w = re.search(r'six of the seven bands[^.]*?3\.74\$? per cent[^.]*', tex)
print("    P15 now reads: " + (f"\"...{w.group(0)[:160]}...\"" if w else
                               "the six-of-seven / 3.74 clause is no longer present"))

print()
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print()
print("  VERDICT: ** the count is wrong and the law is better supported than the count says. **")
print("  *Inside the quoted 3.74 per cent sit five bands of seven on each arm, not six.  The 3.74 per cent")
print("  is the error at one phase and not the statistic's floor, which reaches ten per cent across phase.")
print("  But the real comb's phase is that phase to 0.03 rad, and there the instrument is wrong by about")
print("  four per cent in the lowest band and under one elsewhere.  Divided out, all seven bands on both")
print("  arms hold inside 3.74 per cent.*")
print("  ⌗ ** And 'on each arm' is one test: ** the two arms' deviations correlate at 0.998.  Within an")
print("     arm the seven bands are close to independent measurements.")
