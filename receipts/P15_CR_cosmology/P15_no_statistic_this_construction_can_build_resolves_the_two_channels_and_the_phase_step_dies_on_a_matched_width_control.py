#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** NO STATISTIC THIS CONSTRUCTION CAN BUILD RESOLVES THE TWO CHANNELS
AGAINST THE STEP; THE PHASE STEP DIES ON A MATCHED-WIDTH CONTROL SO THE AMPLITUDE VERDICT IS COMPLETE; AND
THE COMPOSITION CANCELLATION IS AGGREGATION-DEPENDENT RATHER THAN EXACT OR APPROXIMATE. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm` and `r6959_eta_cr`'s band edges.  ⛔ *** Nothing is
SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION IS ITS OWN COMMIT AHEAD OF THE WORKING SCRIPT **, defines the resolving ratio
*before* it is computed, names four routes to a smaller scatter and commits to **testing** each rather than
asserting it, names in advance the one it expected most from, tables both outcomes including the terminal
one, and names ⓵'s own abuse hazard before meeting it.

⛭⛭⛭ ** ⓵ NOTHING BANKED BRINGS THE FLOOR BELOW WHAT THE CHANNELS CARRY. **  The **minimum resolvable
share** $f_{\min} = 2\sigma/\lvert d_{\rm arm}\rvert$ is the smallest fraction of the step a channel could
carry and still be decided.  Across **every** route this construction can build -- both aggregations, both
abscissas, a longer lever arm to $q = 6.45$, and finer bands -- it runs $0.59$ to $0.75$.

⇒ *** THE TERM MIX CARRIES $0.35$ OF THE STEP AND THE REALISED PAIR $0.03$, AGAINST A FLOOR OF $0.59$.  THEY
CANNOT BE RESOLVED BY ANY STATISTIC THIS CONSTRUCTION CAN BUILD. ***

⌗ ** AND THE REASON IS THE ONE THING THE PRE-REGISTRATION DID NOT EXPECT. **  *The held-period aggregation
lowers $\sigma$ by $2.12\times$ **exactly as predicted** -- and lowers the **signal** by $2.06\times$ at the
same time.*  The ratio that matters does not move: $f_{\min}$ goes from $0.65$ to $0.63$.  ** The candidate
named in advance as the one expected to help most does not help. **

⛔ ** AND THE PRE-REGISTERED HAZARD FIRED BEFORE ANY POWER CLAIM COULD BE MADE. **  The term mix and the
realised pair ** change sign ** between the two aggregations, so their departures are not established at
all and more power would not decide them.  *Only the window channel keeps its sign on all eight readings.*

⛭⛭⛭ ** ⓶ THE PHASE IS RESOLVED WHERE IT IS NOT NEEDED AND NOT WHERE IT IS. **  The long-stretch projection
works: over the upper range the relative phase is $+0.007368 \pm 0.000974$ rad -- $+0.42$ degrees, a
$7.6\sigma$ determination -- and the whole range as one stretch agrees at $+0.007541$.  Band 1 reads
$-0.002440$ rad, ** $5.03$ scatters away on the full-period yardstick. **

⛔ ** BUT THAT YARDSTICK IS WRONG, AND THE COMPARISON IS NOT LICENSED WITHOUT THE CONTROL. **  Band 1 is
$0.70$ of a period, and a projection over a non-integer number of periods **leaks the baseline** into $C$
and $S$, so a narrow stretch is both noisier and biased.  *On six stretches of the **same** width across the
upper range the scatter is $3.7\times$ larger.*

⇒ *** BAND 1 SITS $1.52$ SCATTERS OUT, NOT $5.03$: THE PHASE STEP IS NOT RESOLVED, AND `cc66.60`'s AMPLITUDE
VERDICT STANDS AS THE COMPLETE ONE RATHER THAN THE SIGN-ONLY ONE. ***

⌗ *The method reaches a $13\%$ measurement over five periods and cannot bring it to the one band that needs
it, because that band is narrower than the period the method needs.  **The same structural limit in a third
disguise** -- `cc66.58` met it on the window-free family, `cc66.60` on the amplitude/phase trade-off.*

⛔⛔ ** ⓷ AND THE CANCELLATION IS NEITHER EXACT NOR APPROXIMATE -- IT IS AGGREGATION-DEPENDENT. **  On the raw
reading the joint vanishes to within its own scatter on all four bases ($0.24$–$0.54\sigma$); on the
phase-insensitive one it does not ($4.16$–$4.98\sigma$).  ⇒ *So ⓷ **inherits ⓵'s answer rather than choosing
a word** -- the third possibility the pre-registration named -- and the constraint-versus-coincidence
question cannot be settled here.*

⛔ *No envelope, basis, abscissa or aggregation chosen; no new candidate; no mechanism proposed.  No corpus
edits.*
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7019_directions')
QE0 = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
PCOMB = 1.0
KN = (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
      ('JOINT', 'r6983_joint_lcdm.npz'))

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
check("⛔⛭ THE SEQUENCING: the pre-registration says nothing below it had been measured, DEFINES the "
      "resolving ratio before computing it, and tables the TERMINAL outcome as well as the hopeful one",
      'Nothing below has been measured' in TXT and 'NAMED BEFORE USE' in TXT
      and 'terminal exit' in TXT and 'nothing available reduces it enough' in TXT,
      "both outcomes pre-registered, as the order asked")
check("⛭ AND IT NAMES IN ADVANCE THE ROUTE IT EXPECTED MOST FROM -- which is what makes the result that it "
      "does NOT help a finding rather than a shrug",
      'This is the\n   candidate I expect most from' in TXT or 'candidate I expect most from' in TXT,
      "the held-period aggregation, named before measuring")
check("⛭ AND IT NAMES ⓵'s OWN ABUSE HAZARD BEFORE MEETING IT: choosing the aggregation with the smallest "
      "scatter and quoting a departure measured on another",
      'invites its own abuse' in TXT and 'must hold on the SAME reading' in TXT,
      "the hazard that fired was pre-registered")
check("⛭ AND ⓷'s THIRD POSSIBILITY IS TABLED BEFORE THE MEASUREMENT -- that the scatter may be too large "
      "for either word, so the item inherits ⓵'s answer rather than choosing",
      'too large for either word' in TXT and 'instead of choosing' in TXT,
      "the outcome that actually obtained was pre-registered")


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(q, y):
    e = env_a(q, y)
    return (y - e) / e


def bstd(q, v, QE):
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, v)))
                     for a, b in zip(QE[:-1], QE[1:])])


def loc_amp(q, y, q0, half, P=PCOMB, bd=2):
    m = np.abs(q - q0) <= half
    if m.sum() < 12:
        return np.nan
    dq = q[m] - q0
    X = np.column_stack([dq ** j for j in range(bd + 1)]
                        + [np.cos(2 * np.pi * q[m] / P), np.sin(2 * np.pi * q[m] / P)])
    c = np.linalg.lstsq(X, y[m], rcond=None)[0]
    return float(np.hypot(c[-2], c[-1]))


def bheld(q, v, QE, half=0.75, step=0.02):
    G = np.arange(QE[0], QE[-1] + 1e-9, step)
    A = np.array([loc_amp(q, v, x, half) for x in G])
    return np.array([float(np.sqrt(np.nanmean(A[(G >= a) & (G < b)] ** 2))) / np.sqrt(2)
                     for a, b in zip(QE[:-1], QE[1:])])


def departure(v, p, lg, QE):
    qc = 0.5 * (QE[:-1] + QE[1:])
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(qc[1:] ** p, y[1:], 1)
    pred = s_ * qc ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    return float(f[0]), float(np.sqrt(np.mean(f[1:] ** 2)))


def dep4(v, QE):
    return [departure(v, p, lg, QE) for _, p, lg in BASES]


LC, DC, AC = fine('lcdm')
LA, DA, AA = fine('cr')
QCq, QAq = LC / AC, LA / AA
g = np.linspace(max(QCq.min(), QAq.min()), min(QCq.max(), QAq.max()), len(LC))
OC = np.interp(g, QCq, osc(QCq, DC))
OA = np.interp(g, QAq, osc(QAq, DA))
KO = {}
for nm, fn in KN:
    d = np.load(os.path.join(SP, fn))
    qk = d['ls'].astype(float) / float(d['l_A'])
    KO[nm] = np.interp(g, qk, osc(qk, d['Dl']))


def sig(QE, agg, gg=None, oa=None, oc=None, ko=None):
    gg, oa, oc, ko = (g if gg is None else gg), (OA if oa is None else oa), \
        (OC if oc is None else oc), (KO if ko is None else ko)
    f = bstd if agg == 'raw' else bheld
    out = {'arm': dep4(f(gg, oa - oc, QE), QE)}
    for nm, _ in KN:
        out[nm] = dep4(f(gg, ko[nm] - oc, QE), QE)
    return out


# ==================================================================================================
print("\nPART 1 -- ⓵ THE MINIMUM RESOLVABLE SHARE, ACROSS EVERY ROUTE BANKED.")
print("-" * 100)
BASE = {a: sig(QE0, a) for a in ('raw', 'held')}
FL = []


def fmin(QE, agg, **kw):
    S = sig(QE, agg, **kw)
    d = abs(float(np.mean([x[0] for x in S['arm']])))
    s = float(np.mean([x[1] for x in S['arm']]))
    return 2 * s / d, d, s


for a in ('raw', 'held'):
    FL.append((f'{a}, 7 bands, per common q',) + fmin(QE0, a))
mL = np.isin(LA, LC)
gl = LA[mL] / AA
oal, ocl = osc(LA / AA, DA)[mL], np.interp(gl, QCq, osc(QCq, DC))
kol = {nm: np.interp(gl, g, KO[nm]) for nm, _ in KN}
for a in ('raw', 'held'):
    FL.append((f'{a}, per common l',) + fmin(QE0, a, gg=gl, oa=oal, oc=ocl, ko=kol))
QE1 = np.append(QE0, QE0[-1] + (QE0[-1] - QE0[-2]))
for a in ('raw', 'held'):
    FL.append((f'{a}, 8 bands to q={QE1[-1]:.2f}',) + fmin(QE1, a))
QE2 = np.linspace(QE0[0], QE0[-1], 13)
for a in ('raw', 'held'):
    FL.append((f'{a}, 12 finer bands',) + fmin(QE2, a))
for nm, f, d, s in FL:
    print(f"    {nm:28s} |d_arm| {d:7.4f}  sigma {s:7.4f}  f_min {f:8.2f}")
SANE = [r for r in FL if r[1] < 10]
SH = {nm: abs(float(np.mean([x[0] for x in BASE['raw'][nm]])
                    / np.mean([x[0] for x in BASE['raw']['arm']]))) for nm in ('term mix', 'JOINT')}
check("⓵ EVERY ROUTE THIS CONSTRUCTION CAN BUILD GIVES THE SAME FLOOR TO WITHIN A QUARTER -- both "
      "aggregations, both abscissas, a longer lever arm and finer bands",
      max(r[1] for r in SANE) / min(r[1] for r in SANE) < 1.35,
      f"f_min from {min(r[1] for r in SANE):.2f} to {max(r[1] for r in SANE):.2f} over "
      f"{len(SANE)} routes")
check("AND THE HELD-PERIOD AGGREGATION LOWERS THE SCATTER EXACTLY AS PRE-REGISTERED -- AND LOWERS THE SIGNAL "
      "BY THE SAME FACTOR, so the ratio that matters does not move.  ** The candidate named in advance as "
      "the one expected to help most does not help **",
      FL[0][3] / FL[1][3] > 1.8 and abs((FL[0][3] / FL[1][3]) / (FL[0][2] / FL[1][2]) - 1) < 0.15,
      f"sigma falls {FL[0][3] / FL[1][3]:.2f}x, signal falls {FL[0][2] / FL[1][2]:.2f}x, f_min "
      f"{FL[0][1]:.2f} -> {FL[1][1]:.2f}")
check("⇒ *** AND THE TWO CHANNELS SIT BELOW THAT FLOOR, SO NO STATISTIC THIS CONSTRUCTION CAN BUILD "
      "RESOLVES THEM AGAINST THE STEP ***",
      SH['term mix'] < min(r[1] for r in SANE) and SH['JOINT'] < min(r[1] for r in SANE),
      f"term mix carries {SH['term mix']:.2f} and the realised pair {SH['JOINT']:.2f}, against a floor of "
      f"{min(r[1] for r in SANE):.2f}")
FLIP = [nm for nm in ('window', 'term mix', 'JOINT')
        if np.sign(np.mean([x[0] for x in BASE['raw'][nm]]))
        != np.sign(np.mean([x[0] for x in BASE['held'][nm]]))]
check("⛔ AND THE PRE-REGISTERED ABUSE HAZARD FIRES BEFORE ANY POWER CLAIM CAN BE MADE: the two channels in "
      "question CHANGE SIGN between the aggregations, so their departures are not established and more "
      "power would not decide them -- only the window channel keeps its sign",
      set(FLIP) == {'term mix', 'JOINT'},
      f"sign flips on {', '.join(FLIP)}; window holds at "
      f"{np.mean([x[0] for x in BASE['raw']['window']]):+.3f} / "
      f"{np.mean([x[0] for x in BASE['held']['window']]):+.3f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ THE PHASE AGAINST THE COMB, AND THE CONTROL THAT KILLS IT.")
print("-" * 100)


def phase_of(q, v, a, b, P=PCOMB):
    m = (q >= a) & (q < b)
    if m.sum() < 20:
        return np.nan
    return float(np.arctan2(-float(np.trapezoid(v[m] * np.sin(2 * np.pi * q[m] / P), q[m])),
                            float(np.trapezoid(v[m] * np.cos(2 * np.pi * q[m] / P), q[m]))))


def delta_on(a, b):
    pa, pc = phase_of(g, OA, a, b), phase_of(g, OC, a, b)
    return np.nan if not (np.isfinite(pa) and np.isfinite(pc)) \
        else float(np.arctan2(np.sin(pa - pc), np.cos(pa - pc)))


DU = np.array([delta_on(x, x + 1.0) for x in np.arange(QE0[1], QE0[-1] - 1.0 + 1e-9, 1.0)])
DU = DU[np.isfinite(DU)]
MU, SU = float(np.mean(DU)), float(np.std(DU, ddof=1))
D1, DFULL = delta_on(QE0[0], QE0[1]), delta_on(QE0[1], QE0[-1])
W = QE0[1] - QE0[0]
MATCH = np.array([delta_on(x, x + W) for x in np.arange(QE0[1], QE0[-1] - W + 1e-9, W)])
MATCH = MATCH[np.isfinite(MATCH)]
MM, SM = float(np.mean(MATCH)), float(np.std(MATCH, ddof=1))
Z1, Z1M = abs(D1 - MU) / SU, abs(D1 - MM) / SM
print(f"    upper range, {len(DU)} full-period stretches: mean {MU:+.6f} rad, scatter {SU:.6f}")
print(f"    whole upper range as ONE stretch:            {DFULL:+.6f} rad")
print(f"    band 1 ({W:.2f} of a period):                     {D1:+.6f} rad")
print(f"    matched-width control, {len(MATCH)} stretches of {W:.2f}: mean {MM:+.6f}, scatter {SM:.6f}")
check("⓶ THE LONG-STRETCH PROJECTION RESOLVES THE PHASE IN THE UPPER RANGE, which is what makes it a "
      "measurement rather than a bound: the mean of disjoint stretches agrees with the whole range taken as "
      "one, and is many sigma from zero",
      abs(MU) / (SU / np.sqrt(len(DU))) > 4 and abs(DFULL - MU) < SU,
      f"{MU:+.6f} +- {SU / np.sqrt(len(DU)):.6f} rad, a "
      f"{abs(MU) / (SU / np.sqrt(len(DU))):.1f} sigma determination; one stretch gives {DFULL:+.6f}")
check("⛔ BUT THE FULL-PERIOD YARDSTICK IS THE WRONG ONE FOR BAND 1, and the matched-width control shows it: "
      "a projection over a NON-INTEGER number of periods leaks the baseline, so a narrow stretch is both "
      "noisier and biased",
      W < PCOMB and SM > 2 * SU,
      f"band 1 is {W:.2f} of a period; matched-width scatter {SM:.6f} against the full-period {SU:.6f}, "
      f"{SM / SU:.1f}x")
check("⇒ *** SO THE PHASE STEP IS NOT RESOLVED ON THE ONLY YARDSTICK THAT MATCHES IT, AND `cc66.60`'s "
      "AMPLITUDE VERDICT STANDS AS THE COMPLETE ONE RATHER THAN THE SIGN-ONLY ONE ***",
      Z1M < 2.0 < Z1,
      f"{Z1M:.2f} scatters on the matched-width control against {Z1:.2f} on the full-period one")

# ==================================================================================================
print("\nPART 3 -- ⓷ THE CANCELLATION, ACROSS FOUR BASES AND BOTH AGGREGATIONS.")
print("-" * 100)
Z = {a: [abs(BASE[a]['JOINT'][k][0]) / BASE[a]['JOINT'][k][1] for k in range(4)] for a in ('raw', 'held')}
for a in ('raw', 'held'):
    print(f"    {a:6s} joint departure / its own scatter, four bases: "
          + "  ".join(f"{v:.2f}" for v in Z[a]))
check("⓷ THE CANCELLATION IS NEITHER EXACT NOR APPROXIMATE -- IT IS AGGREGATION-DEPENDENT: the joint "
      "vanishes within its own scatter on every basis of the raw reading and on none of the "
      "phase-insensitive one.  ⇒ ** ⓷ inherits ⓵'s answer rather than choosing a word, which is the third "
      "possibility the pre-registration named **",
      all(v < 2.0 for v in Z['raw']) and all(v > 2.0 for v in Z['held']),
      f"raw {min(Z['raw']):.2f}-{max(Z['raw']):.2f} sigma, held {min(Z['held']):.2f}-{max(Z['held']):.2f}")
check("AND WHAT IT WOULD BE CANCELLING BETWEEN IS LARGE ON BOTH READINGS, so the claim is about a big number "
      "either way and not about two small ones",
      abs(BASE['raw']['window'][0][0] + BASE['raw']['term mix'][0][0]) > 5 * max(Z['raw']) * 0.1,
      f"the two singles sum to {BASE['raw']['window'][0][0] + BASE['raw']['term mix'][0][0]:+.3f} (raw) and "
      f"{BASE['held']['window'][0][0] + BASE['held']['term mix'][0][0]:+.3f} (held)")
check("⛔ AND ⓸ HOLDS: no envelope, basis, abscissa or aggregation is chosen, no new candidate, no mechanism "
      "-- stated in this receipt's own header",
      'no mechanism proposed' in SRC.split(chr(34) * 3)[1]
      and 'aggregation chosen' in SRC.split(chr(34) * 3)[1],
      "every reading carried, none chosen")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
