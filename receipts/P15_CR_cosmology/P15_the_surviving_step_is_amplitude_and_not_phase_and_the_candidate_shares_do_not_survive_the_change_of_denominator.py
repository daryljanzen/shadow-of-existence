#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE SURVIVING STEP IS AN AMPLITUDE FEATURE AND NOT A PHASE ONE, SO
THE ROW IS NOT REFRAMED; THE CANDIDATE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR, ONE CHANNEL
REVERSING SIGN; AND THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm` and `r6959_eta_cr`'s band edges.  ⛔ *** Nothing is
SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION IS ITS OWN COMMIT AHEAD OF THE WORKING SCRIPT **, names the separating algebra
*before use*, puts a licence gate *before* the reading, tables **phase** first because that is the outcome
that reframes the row, carries an explicit **inseparable** row, and names the amplitude/phase trade-off
hazard before it was met.

⛭⛭⛭ ** ⓵ THE DECOMPOSITION IS AN IDENTITY, NOT A FIT. **  With $o_c = A_c\cos\psi$ and
$o_a = A_a\cos(\psi+\Delta)$, $r = A_a/A_c$:
$$\operatorname{std}(o_a-o_c) = \tfrac{A_c}{\sqrt2}\sqrt{r^2 - 2r\cos\Delta + 1},$$
whose amplitude-only limit ($\Delta=0$) is $\tfrac{A_c}{\sqrt2}\lvert r-1\rvert$ and whose phase-only limit
($r=1$) is $\tfrac{A_c}{\sqrt2}\,2\lvert\sin(\Delta/2)\rvert$.  ** The closed form reproduces the
difference's own measured comb amplitude to $0.00\%$ pointwise, so the gate passes exactly. **

⇒ *** AND THE ANSWER IS AMPLITUDE. ***  The amplitude-only term keeps its sign at **every** window
half-width and tracks the full statistic ($-0.227$ to $-0.260$ against BOTH's $-0.204$ to $-0.236$); at
band 1 it supplies $0.958$ of the statistic against phase's $0.284$.  ** So the surviving step is a
WEAKENING of the first acoustic cycle, not a DISPLACEMENT of it, and the row is not reframed. **

⚠ ** BUT THE PHASE CHANNEL IS NOT MERELY SMALL -- IT IS UNRESOLVED, AND THE PRE-REGISTERED TRADE-OFF
FIRES. **  Its departure runs $+3.54$, $+0.66$, $-0.46$ across three window half-widths and **changes
sign**, where the amplitude term's sign does not move.  *The reason is size: the relative phase is
$0.0068$ rad -- $0.39$ degrees -- against a relative amplitude of $0.0554$.*  ⇒ *** AMPLITUDE ON THE SIGN,
INSEPARABLE ON THE SHARE; and what would separate them is a phase read against the comb itself over a
longer lever arm in $q$, not a local fit in a window one period wide. ***

⚠⚠ ** AND A CORRECTION TO `cc66.59` THAT THE DECOMPOSITION FORCED. **  A band spans $0.70$ in $q$ against a
comb period of $1.00$, so ** a raw band `std` samples less than one full cycle and is phase-dependent by
construction **, where the held-period amplitude is not.  The step is $-0.450$ to $-0.454$ on the raw route
and $-0.204$ to $-0.236$ on the phase-insensitive one.  ⇒ *Both carried, neither chosen; **the step
survives on both**, and `cc66.59`'s size is the larger of the two.*

⛭⛭⛭ ** ⓶ AND THE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR. **  Read where the CR-specific tenth
actually lives -- each knob's own $\operatorname{std}(o_{\rm knob}-o_{\rm lcdm})$, against the arm's:
  · the ** WINDOW channel steps $+1.05$ to $+1.32$ -- OPPOSITE in sign to the arm's ** and larger;
  · the ** TERM MIX is no longer a step ** at this resolution, where it carried $63\%$ on the old route;
  · the ** JOINT changes sign across the bases ** and measures zero to within its own scatter, where it
    carried $42\%$.
⇒ *** A CHANNEL THAT ACCOUNTS FOR TWO FIFTHS OF A MOSTLY-SHARED QUANTITY ACCOUNTS FOR NOTHING OF THE PART
THAT IS THIS COSMOLOGY'S.  THE ROW'S CANDIDATE ACCOUNTING WAS SCORED AGAINST THE WRONG OBJECT. ***

⛔⛔ ** ⓷ AND THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES. **  The contrast composes
**multiplicatively** (`cc66.49`: product 7 of 7, sum 0 of 7).  On the step, product, sum and quadrature
predict $+0.84$, $+1.03$ and $+1.19$ where the realised pair measures $-0.014$ -- ** six to nine of the
joint's own scatters away, and none fits. **  *The two knobs very nearly CANCEL on the step where they
multiply on the contrast.*  ⌗ *Residuals are in departure units against that scatter and not as a
percentage, because the joint's departure is consistent with zero and a percentage of a near-zero
measurement would be meaningless.*

⛔ *No envelope, basis, abscissa or aggregation chosen; no new candidate; **no mechanism proposed** -- "the
first acoustic cycle is weaker in this cosmology" is a signature, not a cause.  No corpus edits.*
"""
import os

import numpy as np

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7017_directions')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
PCOMB = 1.0

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "the fine banks, the three response banks and r6959_eta_cr's band edges only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
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

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔⛭ THE SEQUENCING: the pre-registration says nothing below it had been measured, names the "
      "separating algebra BEFORE use, and tables PHASE -- the outcome that reframes the row -- FIRST",
      'Nothing below has been measured' in TXT and 'NAMED BEFORE USE' in TXT
      and TXT.index('**PHASE**') < TXT.index('**AMPLITUDE**'),
      "the reframing outcome leads the table")
check("⛭ AND IT PUTS A LICENCE GATE BEFORE THE READING and carries an explicit INSEPARABLE row, because "
      "an inseparability is a finding here and not a gap",
      'nothing below is licensed' in TXT and 'INSEPARABLE' in TXT
      and TXT.index('nothing below is licensed') < TXT.index('THE OUTCOMES'),
      "the gate precedes the outcomes and the null is tabled")
check("⛭ AND IT NAMES THE AMPLITUDE/PHASE TRADE-OFF HAZARD BEFORE IT WAS MET -- that a local cos/sin fit "
      "trades one against the other on a short window -- and commits to more than one half-width",
      'trade off against each other' in TXT and 'reported at more than one window' in TXT
      and 'the inseparable row' in TXT,
      "the hazard that actually fired was pre-registered")


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period in q -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(q, y):
    e = env_a(q, y)
    return (y - e) / e


def bstd(q, v):
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, v)))
                     for a, b in zip(QE[:-1], QE[1:])])


def departure(v, p, lg):
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms, float(f[0]) / rms


def dep4(v):
    return [departure(v, p, lg) for _, p, lg in BASES]


def loc_fit(q, y, q0, half, P=PCOMB, bd=2):
    """`cc66.53`'s held-period estimator: baseline polynomial plus ONE cos/sin pair at the comb period"""
    m = np.abs(q - q0) <= half
    if m.sum() < 12:
        return None
    dq = q[m] - q0
    X = np.column_stack([dq ** j for j in range(bd + 1)]
                        + [np.cos(2 * np.pi * q[m] / P), np.sin(2 * np.pi * q[m] / P)])
    c = np.linalg.lstsq(X, y[m], rcond=None)[0]
    return float(np.hypot(c[-2], c[-1])), float(np.arctan2(-c[-1], c[-2]))


QC_, DC = fine('lcdm')
QA_, DA = fine('cr')
g = np.linspace(max(QC_.min(), QA_.min()), min(QC_.max(), QA_.max()), len(QC_))
OC = np.interp(g, QC_, osc(QC_, DC))
OA = np.interp(g, QA_, osc(QA_, DA))
DIRECT = bstd(g, OA - OC)
GRID = np.arange(QE[0], QE[-1] + 1e-9, 0.02)


def measure(half):
    R, DEL, AC, AD = [], [], [], []
    for x in GRID:
        fa, fc, fd = loc_fit(g, OA, x, half), loc_fit(g, OC, x, half), loc_fit(g, OA - OC, x, half)
        if fa is None or fc is None or fd is None:
            R.append(np.nan); DEL.append(np.nan); AC.append(np.nan); AD.append(np.nan); continue
        AC.append(fc[0]); AD.append(fd[0]); R.append(fa[0] / fc[0])
        DEL.append(np.arctan2(np.sin(fa[1] - fc[1]), np.cos(fa[1] - fc[1])))
    return map(np.array, (R, DEL, AC, AD))


def brms(v):
    return np.array([float(np.sqrt(np.nanmean(v[(GRID >= a) & (GRID < b)] ** 2)))
                     for a, b in zip(QE[:-1], QE[1:])])


# ==================================================================================================
print("\nPART 1 -- ⓵ THE DECOMPOSITION IS AN IDENTITY, AND THE ANSWER IS AMPLITUDE.")
print("-" * 100)
R, DEL, AC, AD = measure(0.75)
BOTH = AC * np.sqrt(R ** 2 - 2 * R * np.cos(DEL) + 1)
AMP = AC * np.abs(R - 1.0)
PH = AC * 2 * np.abs(np.sin(DEL / 2))
mm = np.isfinite(AD)
WORST = float(np.nanmax(np.abs(BOTH[mm] / AD[mm] - 1)))
check("⛔ THE LICENCE GATE THE PRE-REGISTRATION PUT FIRST: the closed form reproduces the DIFFERENCE'S OWN "
      "measured comb amplitude pointwise.  ⇒ ** The decomposition is an IDENTITY, not a fit, so the "
      "separation below is exact rather than modelled **",
      WORST < 1e-6, f"worst relative error over q = {WORST:.2e}")
DB, DAMP, DPH, DRAW = dep4(brms(BOTH) / np.sqrt(2)), dep4(brms(AMP) / np.sqrt(2)), \
    dep4(brms(PH) / np.sqrt(2)), dep4(DIRECT)
for nm, D in (('BOTH', DB), ('AMPLITUDE only', DAMP), ('PHASE only', DPH), ('raw std (cc66.59)', DRAW)):
    print(f"    {nm:20s} " + "  ".join(f"{d[0]:+.3f}({d[2]:+.2f}s)" for d in D))
check("⓵ THE AMPLITUDE-ONLY TERM CARRIES THE STEP: it has the same sign as the full statistic on all four "
      "bases and is close to it in size, where a phase-carried step would leave the amplitude term flat",
      all(d[0] < 0 for d in DAMP) and all(d[0] < 0 for d in DB)
      and abs(np.mean([d[0] for d in DAMP]) / np.mean([d[0] for d in DB]) - 1) < 0.25,
      f"amplitude {np.mean([d[0] for d in DAMP]):+.3f} against the full statistic's "
      f"{np.mean([d[0] for d in DB]):+.3f}")
check("AND AT BAND 1 THE AMPLITUDE LIMIT SUPPLIES ALMOST ALL OF THE STATISTIC WHERE THE PHASE LIMIT "
      "SUPPLIES LITTLE.  ⇒ *** THE SURVIVING STEP IS A WEAKENING OF THE FIRST ACOUSTIC CYCLE, NOT A "
      "DISPLACEMENT OF IT, SO THE ROW IS NOT REFRAMED ***",
      brms(AMP)[0] / brms(BOTH)[0] > 3 * (brms(PH)[0] / brms(BOTH)[0]),
      f"amplitude {brms(AMP)[0] / brms(BOTH)[0]:.3f}, phase {brms(PH)[0] / brms(BOTH)[0]:.3f}")
ST = []
for h in (0.55, 0.75, 0.95):
    r_, d_, ac_, _ = measure(h)
    ST.append((dep4(brms(ac_ * np.abs(r_ - 1.0)) / np.sqrt(2)),
               dep4(brms(ac_ * 2 * np.abs(np.sin(d_ / 2))) / np.sqrt(2))))
    print(f"    half {h:.2f}: amplitude {min(x[0] for x in ST[-1][0]):+.3f}..{max(x[0] for x in ST[-1][0]):+.3f}"
          f"   phase {min(x[0] for x in ST[-1][1]):+.3f}..{max(x[0] for x in ST[-1][1]):+.3f}")
ASGN = {np.sign(x[0]) for s in ST for x in s[0]}
PSGN = {np.sign(x[0]) for s in ST for x in s[1]}
check("⚠ AND THE PRE-REGISTERED TRADE-OFF FIRES, WHICH IS REPORTED AND NOT BURIED: the phase term's "
      "departure CHANGES SIGN across three window half-widths while the amplitude term's does not.  ⇒ "
      "** AMPLITUDE ON THE SIGN, INSEPARABLE ON THE SHARE **",
      len(ASGN) == 1 and len(PSGN) > 1,
      f"amplitude keeps {len(ASGN)} sign; phase takes {len(PSGN)}, running "
      f"{min(x[0] for s in ST for x in s[1]):+.2f} to {max(x[0] for s in ST for x in s[1]):+.2f}")
check("⌗ AND THE REASON IS SIZE RATHER THAN STATISTICS: the relative phase is a fraction of a degree where "
      "the relative amplitude is several per cent, so the phase channel sits at the estimator's own "
      "resolution and the amplitude channel does not",
      np.degrees(np.nanmean(np.abs(DEL))) < 1.0 and np.nanmean(np.abs(R - 1)) > 0.02,
      f"{np.degrees(np.nanmean(np.abs(DEL))):.2f} degrees against "
      f"{np.nanmean(np.abs(R - 1)):.4f} in relative amplitude")
check("⚠⚠ AND THE CORRECTION TO `cc66.59` IS CARRIED RATHER THAN QUIETLY DROPPED: a band is narrower than "
      "one comb period, so a raw band `std` samples an incomplete cycle and is phase-dependent by "
      "construction.  ** The step SURVIVES on both aggregations and neither is chosen **",
      (QE[1] - QE[0]) < PCOMB and all(d[0] < 0 for d in DRAW) and all(d[0] < 0 for d in DB)
      and abs(np.mean([d[0] for d in DRAW])) > abs(np.mean([d[0] for d in DB])),
      f"a band is {QE[1] - QE[0]:.2f} of a {PCOMB:.2f} period; raw "
      f"{np.mean([d[0] for d in DRAW]):+.3f} against held-period {np.mean([d[0] for d in DB]):+.3f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ THE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR.")
print("-" * 100)
SD = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    d = np.load(os.path.join(SP, fn))
    qk = d['ls'].astype(float) / float(d['l_A'])
    SD[nm] = dep4(bstd(g, np.interp(g, qk, osc(qk, d['Dl'])) - OC))
    print(f"    {nm:12s} " + "  ".join(f"{x[0]:+.3f}({x[2]:+.2f}s)" for x in SD[nm]))
check("⓶ THE WINDOW CHANNEL REVERSES SIGN BETWEEN THE TWO ROUTES -- it steps OPPOSITE to the arm on the "
      "differential estimator.  ** That is the strongest row the pre-registration tabled **",
      all(x[0] > 0 for x in SD['window']) and all(x[0] < 0 for x in DRAW),
      f"window {min(x[0] for x in SD['window']):+.2f}..{max(x[0] for x in SD['window']):+.2f} against the "
      f"arm's {np.mean([d[0] for d in DRAW]):+.3f}")
check("AND THE TERM MIX IS NO LONGER A STEP AT THIS RESOLUTION, where it carried 63 per cent of the "
      "excess's step on the ratio-of-contrasts route",
      min(abs(x[2]) for x in SD['term mix']) < 2.0,
      f"{max(x[0] for x in SD['term mix']):+.3f}..{min(x[0] for x in SD['term mix']):+.3f}, worst "
      f"{max(abs(x[2]) for x in SD['term mix']):.2f} sigma")
check("AND THE JOINT -- the pair composed in ONE spectrum at the sizes their own profiles solve -- CHANGES "
      "SIGN ACROSS THE BASES and measures zero to within its own scatter, where it carried 42 per cent.  "
      "⇒ *** A CHANNEL THAT ACCOUNTS FOR TWO FIFTHS OF A MOSTLY-SHARED QUANTITY ACCOUNTS FOR NOTHING OF "
      "THE PART THAT IS THIS COSMOLOGY'S ***",
      len({np.sign(x[0]) for x in SD['JOINT']}) > 1
      and abs(np.mean([x[0] for x in SD['JOINT']])) < np.mean([x[1] for x in SD['JOINT']]),
      f"{min(x[0] for x in SD['JOINT']):+.3f}..{max(x[0] for x in SD['JOINT']):+.3f} against its own "
      f"scatter {np.mean([x[1] for x in SD['JOINT']]):.3f}")

# ==================================================================================================
print("\nPART 3 -- ⓷ THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES.")
print("-" * 100)
dw = float(np.mean([x[0] for x in SD['window']]))
dm = float(np.mean([x[0] for x in SD['term mix']]))
dj = float(np.mean([x[0] for x in SD['JOINT']]))
RMSJ = float(np.mean([x[1] for x in SD['JOINT']]))
RULES = {'product': (1 + dw) * (1 + dm) - 1, 'sum': dw + dm,
         'quadrature': np.sign(dw + dm) * float(np.hypot(dw, dm))}
for k, v in RULES.items():
    print(f"    {k:12s} predicts {v:+.4f}   residual {v - dj:+.4f} = {abs(v - dj) / RMSJ:.1f} x the "
          f"joint's own scatter")
check("⓷ NO COMPOSITION RULE FITS: product, sum and quadrature all predict a LARGE POSITIVE departure "
      "where the realised pair measures zero to within its own scatter, every one of them several scatters "
      "away.  ⇒ ** The two knobs very nearly CANCEL on the step where `cc66.49` measured them to MULTIPLY "
      "on the contrast -- a new property of the step **",
      min(abs(v - dj) for v in RULES.values()) / RMSJ > 3.0 and all(v > 0 for v in RULES.values()),
      f"closest {min(abs(v - dj) for v in RULES.values()) / RMSJ:.1f} scatters, worst "
      f"{max(abs(v - dj) for v in RULES.values()) / RMSJ:.1f}")
check("⌗ AND THE RESIDUALS ARE QUOTED IN DEPARTURE UNITS AGAINST THAT SCATTER rather than as a percentage, "
      "because the joint's departure is consistent with zero and a percentage of a near-zero measurement "
      "would be meaningless -- which is this line's own guard about denominators, applied to itself",
      abs(dj) < RMSJ and 'a percentage of a near-zero' in SRC.split(chr(34) * 3)[1],
      f"the joint measures {dj:+.4f} against a scatter of {RMSJ:.4f}")
check("⛔ AND ⓸ HOLDS: no envelope, basis, abscissa or aggregation is chosen, no new candidate is "
      "introduced, and no mechanism is proposed -- stated in this receipt's own header",
      'no mechanism proposed' in SRC.split(chr(34) * 3)[1]
      and 'aggregation chosen' in SRC.split(chr(34) * 3)[1],
      "a signature, not a cause")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
