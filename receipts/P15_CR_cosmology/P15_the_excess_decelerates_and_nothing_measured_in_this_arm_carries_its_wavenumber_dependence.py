#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE EXCESS DECELERATES WITH WAVENUMBER, WHICH EXCLUDES THE CORPUS'S OWN
WORKING PARAMETRISATION; AND THE FIRST POSITIVE SEARCH THIS SECTOR HAS EVER RUN COMES BACK EMPTY --
NOTHING ALREADY MEASURED IN THIS ARM CARRIES THE EXCESS'S WAVENUMBER DEPENDENCE. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`, `r6959_eta_{lcdm,cr}`'s per-band `SRCETA` term profiles, and
the three banked channel responses `r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm`.
`sec:refit-bound`'s quartet $222/538/818/1134$ is the LINE-OF-SIGHT path's and is not read -- searched for
by grepping this file for each of the four values and for every line-of-sight bank name (`c54.17*`,
`c54.178_*`, `L814_*`, `r6784_*`), and none occurs below.  ⛔ *** Nothing is RUN here: the order's ⓸
forbids a channel run before ⓵ to ⓷ are answered on paper, and every number comes from banks on disk. ***

** WHY IT EXISTS. **  `r6993`'s order redirected `PO-56` off this seat's own stated next object.  I had
written it as *what sets the sizes*; the order moved it to ***what carries the excess's own wavenumber
dependence***, on the argument that my finding was a SHAPE refutation and no account of sizes closes a gap
that is not a size.  *That redirection is accepted and is the right one: a correct size still leaves a flat
response against one that varies.*  ⇒ The order also made this **the first POSITIVE search criterion this
row has ever had** -- every previous step was an elimination.

⛭⛭ ** ⓷ FIRST, AND THE INVERSION IS THE METHOD RATHER THAN A LIBERTY. **  ⓷ asks whether the statistic's
$q$-dependence belongs to the effect or to the anchoring.  *That is a question about the INSTRUMENT, and
its answer is what a pre-registration for ⓵ must write its tolerances on -- the alternative is a guessed
resolution, which is the defect `cc66.47`'s own lesson is about.*
  * ✔ ** A known $q$-dependence READS BACK: ** six forms injected into the control's own spectrum -- a
    constant, a rise linear in $q^{2}$, a power law, a logarithm and two turnovers WITH A SCALE IN THEM --
    recover with a worst error of $1.3$ per cent.  *So the filter can see the shapes it filters on,
    including the one that would name a physical length.*
  * ⚠ ** BUT THE ESTIMATOR MANUFACTURES BAND-TO-BAND STRUCTURE. **  Its per-band bias swings about one per
    cent and all six forms agree on it to $0.36$ per cent, so it is fixed and not a property of the
    injected shape: *** a CONSTANT contrast reads as a wobble. ***  ⇒ **Band-to-band ordering at the
    per-cent level is the instrument**, and the excess's own wobble is exactly that size.
  * ⛔ ** AND THE MEDIAN ENVELOPE IS NOT A VALID ALTERNATIVE ANCHORING -- DIAGNOSED, NOT DISMISSED, AND IT
    WOULD OTHERWISE HAVE BEEN THE HEADLINE. **  It reads a variation of $1.49$ against the mean envelope's
    $0.44$, which taken at face value would say the filter is anchoring-dependent and the order's premise
    unsafe.  *The tell is that it does not move with its own window -- the last band reads the same to
    seven figures at $0.8$ and $1.2$, where every mean-envelope reading moves.*  ⇒ **At high $q$ the
    running median collapses onto the curve itself, within $3.6$ per cent of it, because the median of a
    locally monotone stretch is its central value whatever the window** -- so the oscillation it should
    measure against is absorbed into it.  The mean envelope sits $14$--$17$ per cent away and moves.
  * ✔ The rise survives the mean envelope at windows $0.8/1.0/1.2$: $0.44$, $0.44$, $0.40$.
    ⇒ *** THE RISE IS REAL; THE WOBBLE IS NOT. ***

⛔⛭⛭ ** ⓵ AND THE SHAPE EXCLUDES THE PARAMETRISATION THIS SECTOR HAS BEEN QUOTING. **  Six forms fitted at
the pre-registered $\sigma = 0.013$, the measured recovery error, on the rule fixed before any fit:
  * ⛔ ** A rise LINEAR IN $q^{2}$ is EXCLUDED at $\chi^{2}/\nu = 4.66$ ** -- the only form excluded, and
    it is the one `cc66.47`, `cc66.48` and `cc66.49` all quote their variation statistic in.  *** The
    excess DECELERATES with wavenumber; it does not accelerate. ***  ⌗ *The statistic those revisions
    quote is a descriptive measure and remains one; what is excluded is reading it as the FORM.*
  * ⛭ The concave family -- turnover, saturating exponential, power law, logarithm -- all fit, and ** NONE
    is preferred: ** best-against-next is $\Delta\chi^{2} = 0.43$ against a pre-registered bar of $4$.
  * ✔ ** Both pre-registered NON-separations held: ** power law against logarithm $\Delta\chi^{2} = 3.42$,
    power law against turnover $0.99$.  *Named before they failed to separate, which is what the clause is
    for.*
  * ⛔ ** NO SCALE IS RESOLVED, and the rule that says so caught my own code. **  The turnover's
    $q_0 = 1.64 \pm 0.52$ and the exponential's $2.52 \pm 1.50$ both reach the bottom edge of the measured
    range.  *`PREDICTION.md` required a scale to land inside the range WITH ITS UNCERTAINTY; the test as
    first written asked only that the central value be inside, which is a weaker bar, and it passed the
    turnover.  The rule as written is applied.*
  * ⚠ ** The rise is a PREFERENCE, not an exclusion of flatness, and those are different claims. **  Every
    rising form beats a constant by $\Delta\chi^{2} = 6.0$ to $10.4$, above the bar -- but the constant's
    own $\chi^{2}/\nu = 2.03$ is under the exclusion bar of $3$, so flatness is disfavoured and not
    excluded.

⛭⛭⛭ ** ⓶ AND THE FILTER'S FIRST APPLICATION RETURNS EMPTY, WHICH IS THE RESULT. **  ⓵ gives the filter two
teeth rather than one: a candidate must grow AND decelerate.  *The statistic is the GROWTH OF THE DEPARTURE
FROM UNITY across the measured range -- scale-free, and exactly what "carries the wavenumber dependence"
means.*  ⌗ *The sector's usual $|{\rm slope}\times\langle q^{2}\rangle|/|{\rm intercept}|$ was tried first
and abandoned: it divides by $\ln r$ at $q=0$, so a candidate sitting at $r\simeq0.78$ is divided by
$0.25$ where the excess at $1.04$ is divided by $0.04$ -- the same shape reads twenty times larger at the
lower level.  Fine for one quantity near unity, wrong for comparing several.*
  * **The target is $G = 3.55$ with negative curvature.**
  * ⛔ ** EVERY CANDIDATE ALREADY MEASURED IN THIS ARM FAILS THE FIRST TOOTH: ** all six source terms
    ($G = 0.54$ to $1.00$), the dipole-to-monopole ratio ($1.08$), and all three measured channels --
    the window ($0.55$), the term mix ($1.53$), the pair ($1.27$).  *The largest is the term mix at
    $1.53$, less than half what is needed.*
  * ⚠ ** AND THE ORDER'S OWN NAMED CANDIDATE DISAGREES WITH THE REGISTER, WHICH IS REPORTED AND NOT
    SETTLED. **  The register records the dipole-to-monopole ratio as *two per cent above the control's
    and rising*.  Read from these profiles on the hierarchy path at each arm's own visibility peak, the
    amplitude ratio sits **fourteen per cent BELOW** the control and is flat ($G = 0.97$, curvature
    positive).  ⛔ *That is not a refutation of the register's number: the register's reading may be the
    line-of-sight path or a different definition, and this receipt reads only the hierarchy path.  What is
    owed before the candidate is closed is which quantity the register measured, and it is named here
    rather than decided.*

** WHAT IS NOT CLAIMED. **  NOT that the excess's form is a turnover, a power law or a logarithm -- none is
preferred and that is stated as a non-separation.  NOT that a scale exists or does not: none is RESOLVED,
which is weaker.  NOT that the excess is inconsistent with flatness: flatness is disfavoured, not excluded.
NOT that the dipole-to-monopole ratio is eliminated: it fails the filter as measured here and the register
disagrees, which is a discrepancy to name and not a verdict.  NOT that no candidate exists -- what is shown
is that none of the things ALREADY MEASURED carries the dependence, which is a statement about the list
searched.  NOT a third channel: the order forbids one and none is run.  NOT a detection.  NOT a verdict on
the two-rate assignment.  No refit, nothing touching `prop:flat` or the clock family, and no corpus edits.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s verified
    185-bin refit minima; every spectrum read is that configuration.  Nothing here re-fits and nothing is
    run.
  * `spectra/r6941_fine_{lcdm,cr}.npz`, `spectra/r6959_eta_{lcdm,cr}.npz`, `spectra/r6959_nswap_lcdm.npz`,
    `spectra/r6975_mix_lcdm.npz`, `spectra/r6983_joint_lcdm.npz`.
  * ** The per-band uncertainty $\sigma = 0.013$ is MEASURED here and not assumed: ** it is the worst
    recovery error over six injected forms, and `PREDICTION.md` fixes every tolerance on it before any fit.
  * The statistic is `r6911+cc66.40`'s, unchanged; the band edges are `r6959`'s own `q_edges`.
"""
import os
import sys

import numpy as np
from scipy.optimize import curve_fit

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
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NEED = ('r6941_fine_lcdm.npz', 'r6941_fine_cr.npz', 'r6959_eta_lcdm.npz', 'r6959_eta_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
CH = {'window': np.load(os.path.join(SP, 'r6959_nswap_lcdm.npz')),
      'term mix': np.load(os.path.join(SP, 'r6975_mix_lcdm.npz')),
      'the pair': np.load(os.path.join(SP, 'r6983_joint_lcdm.npz'))}
QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
Q2 = QC ** 2
SIG = 0.013
NF = 3.0


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def env_m(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.median(y[m])
    return e


def bands_of(q, o):
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def bands(d, fn=env_a, win=1.0):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = fn(q, d['Dl'], win)
    return bands_of(q, (d['Dl'] - e) / e)


def inject(d, f):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = env_a(q, d['Dl'])
    return dict(ls=d['ls'], Dl=e + f(q) * (d['Dl'] - e), l_A=d['l_A'])


C0 = bands(F['lcdm'])
R = bands(F['cr']) / C0
check("the measured excess is recomputed here from `r6941_fine_*` and reproduces `cc66.46`'s seven "
      "band ratios", np.allclose(R, [1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762], atol=5e-4),
      "  ".join(f"{x:.4f}" for x in R))

# ==================================================================================================
print("\nPART 1 -- ⓷ THE FILTER, CONTROLLED BEFORE THE THING IT FILTERS ON.")
print("-" * 100)
FORMS_INJ = (('constant', lambda q: np.full_like(q, 1.05)),
             ('linear in q^2', lambda q: 1 + 0.004 * q ** 2),
             ('power law', lambda q: 1 + 0.02 * q ** 0.8),
             ('logarithm', lambda q: 1 + 0.03 * np.log(q)),
             ('turnover, scale 3', lambda q: 1 + 0.10 * q ** 2 / (q ** 2 + 9.0)),
             ('turnover, scale 6', lambda q: 1 + 0.10 * q ** 2 / (q ** 2 + 36.0)))
ROWS, WORST = [], 0.0
for nm, f in FORMS_INJ:
    rec = bands(inject(F['lcdm'], f)) / C0
    inj = np.array([float(np.mean(f(np.linspace(a, b, 400)))) for a, b in zip(QE[:-1], QE[1:])])
    ROWS.append(rec / inj)
    WORST = max(WORST, float(np.abs(rec / inj - 1).max()))
ROWS = np.array(ROWS)
BIAS, SPREAD = ROWS.mean(axis=0), ROWS.std(axis=0)
print(f"  six injected forms recover with a worst error of {WORST:.2e}")
print("  per-band bias " + "  ".join(f"{x:.5f}" for x in BIAS))
print("  form spread   " + "  ".join(f"{x:.5f}" for x in SPREAD))
check("⓷a a KNOWN q-dependence reads back, over six forms including two with a SCALE in them -- so the "
      "filter can see the shapes it is being asked to filter on", WORST < 0.02, f"worst {WORST:.2e}")
_swing = float(BIAS.max() - BIAS.min())
check("⛭ ⓷b AND THE ESTIMATOR MANUFACTURES BAND-TO-BAND STRUCTURE: its per-band bias is a FIXED "
      "property, agreed on by the six forms far more closely than it swings -- so a CONSTANT contrast "
      "reads as a wobble, and band ordering at the per-cent level is the instrument.  ⌗ *Judged against "
      "the TYPICAL disagreement across bands; at the single worst band the forms differ by more, and "
      "that band is named rather than averaged away*",
      _swing > 3 * float(SPREAD.mean()),
      f"bias swings {100 * _swing:.2f}%, typical form disagreement {100 * SPREAD.mean():.2f}% "
      f"({_swing / SPREAD.mean():.1f}x), worst single band {100 * SPREAD.max():.2f}% at "
      f"q={QC[int(np.argmax(SPREAD))]:.2f}")
VAR = {}
for lbl, fn, win in (('mean 0.8', env_a, 0.8), ('mean 1.0', env_a, 1.0), ('mean 1.2', env_a, 1.2)):
    r = bands(F['cr'], fn, win) / bands(F['lcdm'], fn, win)
    s, i = np.polyfit(Q2, np.log(r), 1)
    VAR[lbl] = abs(s * Q2.mean()) / abs(i)
print("  variation statistic by envelope window: "
      + ",  ".join(f"{k} -> {v:.3f}" for k, v in VAR.items()))
check("⓷c the excess's RISE survives the mean-envelope window, far above that bias",
      max(VAR.values()) - min(VAR.values()) < 0.10 and min(VAR.values()) > 0.30,
      "  ".join(f"{v:.3f}" for v in VAR.values()))
_q, _D = F['lcdm']['ls'].astype(float) / float(F['lcdm']['l_A']), F['lcdm']['Dl']
_m = (_q >= 5.05) & (_q <= 5.75)
_md = [float(np.abs(env_m(_q, _D, w)[_m] / _D[_m] - 1).mean()) for w in (1.0, 1.2)]
_mn = [float(np.abs(env_a(_q, _D, w)[_m] / _D[_m] - 1).mean()) for w in (1.0, 1.2)]
check("⛔ ⓷d AND THE MEDIAN ENVELOPE IS EXCLUDED WITH ITS MECHANISM, not dismissed: at high q it "
      "collapses onto the curve itself and does not move with its own window, where the mean envelope "
      "sits an order further away and does move -- the median of a locally monotone stretch is its "
      "central value whatever the window, so the oscillation it should measure against is absorbed",
      abs(_md[0] - _md[1]) < 1e-6 and _md[0] < _mn[0] / 3 and abs(_mn[0] - _mn[1]) > 1e-3,
      f"median sits {_md[0]:.5f} from the curve and is IDENTICAL at both windows; the mean sits "
      f"{_mn[0]:.5f} -> {_mn[1]:.5f}, {_mn[0] / _md[0]:.1f}x further away and moving")

# ==================================================================================================
print("\nPART 2 -- ⓵ THE TARGET'S SHAPE, ON THE RULE FIXED BEFORE ANY FIT.")
print("-" * 100)
FORMS = {'F0 constant': (lambda q, A_: A_ + 0 * q, (0.05,)),
         'F1 linear in q^2': (lambda q, A_: A_ * q ** 2, (0.002,)),
         'F2 power law': (lambda q, A_, a: A_ * q ** a, (0.02, 0.8)),
         'F3 logarithm': (lambda q, A_: A_ * np.log(q), (0.03,)),
         'F4 turnover': (lambda q, A_, q0: A_ * q ** 2 / (q ** 2 + q0 ** 2), (0.1, 3.0)),
         'F5 sat. exponential': (lambda q, A_, q0: A_ * (1 - np.exp(-q / q0)), (0.1, 2.0))}
Y = R - 1.0
RES = {}
for nm, (fn, p0) in FORMS.items():
    p, cov = curve_fit(fn, QC, Y, p0=p0, sigma=np.full(7, SIG), absolute_sigma=True, maxfev=40000)
    chi2 = float(np.sum(((Y - fn(QC, *p)) / SIG) ** 2))
    RES[nm] = (chi2, 7 - len(p), p, np.sqrt(np.diag(cov)))
    print(f"  {nm:22s} chi2 = {chi2:7.2f}  nu = {7 - len(p)}  chi2/nu = {chi2 / (7 - len(p)):5.2f}")
check("⛔⛭⛭ ⓵ THE RISE LINEAR IN q^2 IS EXCLUDED -- and it is the parametrisation cc66.47, cc66.48 and "
      "cc66.49 all quote their variation statistic in.  THE EXCESS DECELERATES WITH WAVENUMBER",
      RES['F1 linear in q^2'][0] / RES['F1 linear in q^2'][1] > 3,
      f"chi^2/nu = {RES['F1 linear in q^2'][0] / RES['F1 linear in q^2'][1]:.2f} against the "
      f"pre-registered exclusion bar of 3")
check("and it is the ONLY form excluded, so this is a statement about curvature and not a cull",
      sum(1 for c, nu, _, _ in RES.values() if c / nu > 3) == 1,
      f"{sum(1 for c, nu, _, _ in RES.values() if c / nu > 3)} of 6 excluded")
_o = sorted(RES.items(), key=lambda kv: kv[1][0])
_d = _o[1][1][0] - _o[0][1][0]
check("⓵ AND NO FORM IS PREFERRED, on the pre-registered margin of 4", _d < 4,
      f"best {_o[0][0]} over next {_o[1][0]} by only {_d:.2f}")
for a, b in (('F2 power law', 'F3 logarithm'), ('F2 power law', 'F4 turnover')):
    check(f"the pre-registered NON-separation holds: {a} against {b}",
          abs(RES[a][0] - RES[b][0]) < 4, f"Delta chi^2 = {abs(RES[a][0] - RES[b][0]):.2f}")
_scale = []
for nm in ('F4 turnover', 'F5 sat. exponential'):
    _, _, p, e = RES[nm]
    _scale.append((p[-1] - e[-1]) > QC[0] and (p[-1] + e[-1]) < QC[-1])
check("⛔ ⓵ NO SCALE IS RESOLVED -- both scale-bearing forms put q0 with its uncertainty on the bottom "
      "edge of the measured range, and PREDICTION.md required it inside WITH its uncertainty",
      not any(_scale),
      f"turnover q0 = {RES['F4 turnover'][2][-1]:.2f} +/- {RES['F4 turnover'][3][-1]:.2f}, "
      f"exponential {RES['F5 sat. exponential'][2][-1]:.2f} +/- {RES['F5 sat. exponential'][3][-1]:.2f}, "
      f"range {QC[0]:.2f}-{QC[-1]:.2f}")
_c0 = RES['F0 constant'][0]
_pref = [(_c0 - RES[n][0]) > 4 for n in ('F2 power law', 'F3 logarithm', 'F4 turnover',
                                         'F5 sat. exponential')]
check("⚠ ⓵ AND THE RISE IS A PREFERENCE AND NOT AN EXCLUSION OF FLATNESS, which are different claims: "
      "every rising form beats a constant by more than the margin, yet the constant's own chi^2/nu is "
      "under the exclusion bar", all(_pref) and _c0 / 6 < 3,
      f"Delta chi^2 over the constant {min(_c0 - RES[n][0] for n in ('F2 power law', 'F3 logarithm', 'F4 turnover', 'F5 sat. exponential')):.2f} "
      f"to {max(_c0 - RES[n][0] for n in ('F2 power law', 'F3 logarithm', 'F4 turnover', 'F5 sat. exponential')):.2f}; "
      f"the constant itself chi^2/nu = {_c0 / 6:.2f}")

# ==================================================================================================
print("\nPART 3 -- ⓶ THE FILTER APPLIED ON PAPER, AND IT RETURNS EMPTY.")
print("-" * 100)


def band_power(d, key):
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    return np.array([float(np.trapezoid(d[key][m][:, b], ee[m])) for b in range(len(QC))])


def G_of(r):
    d = r - 1.0
    return float(d[-1] / d[0]), float(np.polyfit(QC, d, 2)[0])


G_T, C_T = G_of(R)
print(f"  the TARGET: departure grows by G = {G_T:.2f} across q = {QC[0]:.2f}-{QC[-1]:.2f}, "
      f"curvature {C_T:+.5f}")
CAND = {}
for key in ('w2sw', 'w2dp', 'w2isw', 'w2pol', 'w2md', 'w2'):
    CAND[f'source {key}'] = band_power(A['cr'], key) / band_power(A['lcdm'], key)
CAND['dipole/monopole'] = ((band_power(A['cr'], 'w2dp') / band_power(A['cr'], 'w2sw'))
                           / (band_power(A['lcdm'], 'w2dp') / band_power(A['lcdm'], 'w2sw')))
for nm, d in CH.items():
    CAND[f'channel {nm}'] = bands(d) / C0
for nm, r in CAND.items():
    g, c = G_of(r)
    print(f"    {nm:22s} G = {g:5.2f}   curvature {c:+.5f}")
check("⛭⛭⛭ ⓶ THE FILTER'S FIRST APPLICATION RETURNS EMPTY: every candidate already measured in this arm "
      "-- all six source terms, the dipole-to-monopole ratio, and all three measured channels -- fails "
      "the growth tooth, the largest reaching less than half of what the target needs",
      all(G_of(r)[0] < 0.6 * G_T for r in CAND.values()),
      f"largest G = {max(G_of(r)[0] for r in CAND.values()):.2f} against the target's {G_T:.2f}")
check("and the target's own curvature is negative, so the filter's second tooth is a real constraint "
      "and not a formality", C_T < 0, f"curvature {C_T:+.5f}")
_amp = np.sqrt((A['cr']['w2dp'][int(np.argmax(A['cr']['vis'])), :]
                / A['cr']['w2sw'][int(np.argmax(A['cr']['vis'])), :])
               / (A['lcdm']['w2dp'][int(np.argmax(A['lcdm']['vis'])), :]
                  / A['lcdm']['w2sw'][int(np.argmax(A['lcdm']['vis'])), :]))
check("⚠ AND THE ORDER'S NAMED CANDIDATE DISAGREES WITH THE REGISTER, WHICH IS NAMED AND NOT SETTLED: "
      "the register records the dipole-to-monopole ratio as two per cent ABOVE the control and rising; "
      "read from these profiles on the HIERARCHY path at each arm's own visibility peak it sits well "
      "below and is flat.  The register's reading may be the line-of-sight path or another definition, "
      "and which quantity it measured is owed before this candidate is closed",
      _amp.mean() < 0.95 and abs(G_of(_amp)[0] - 1) < 0.5,
      f"amplitude ratio {_amp.mean():.4f} at the peak, departure growth G = {G_of(_amp)[0]:.2f}")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
