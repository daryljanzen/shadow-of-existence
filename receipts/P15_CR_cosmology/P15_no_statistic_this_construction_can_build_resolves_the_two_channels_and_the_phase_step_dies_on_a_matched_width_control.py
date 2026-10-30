#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** NO STATISTIC THIS CONSTRUCTION CAN BUILD RESOLVES THE TWO CHANNELS
AGAINST THE STEP; THE PHASE STEP DIES ON A MATCHED-WIDTH CONTROL SO THE AMPLITUDE VERDICT IS COMPLETE; AND
THE COMPOSITION CANCELLATION IS AGGREGATION-DEPENDENT RATHER THAN EXACT OR APPROXIMATE. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** --
`r6941_fine_lcdm`, `r6941_fine_cr_leafrec1` (with `r6941_fine_cr` read for the comparison only),
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm` and `r6959_eta_cr_leafrec1`'s band edges.  ⛔ *** Nothing is
SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION IS ITS OWN COMMIT AHEAD OF THE WORKING SCRIPT **, defines the resolving ratio
*before* it is computed, names four routes to a smaller scatter and commits to **testing** each rather than
asserting it, names in advance the one it expected most from, tables both outcomes including the terminal
one, and names ⓵'s own abuse hazard before meeting it.

⛭⛭⛭ ** ⓵ NOTHING BANKED BRINGS THE FLOOR BELOW WHAT THE CHANNELS CARRY. **  The **minimum resolvable
share** $f_{\min} = 2\sigma/\lvert d_{\rm arm}\rvert$ is the smallest fraction of the step a channel could
carry and still be decided.  Across **every route that bands at or above the comb's own period** -- both
aggregations, both abscissas and a longer lever arm to $q = 6.45$ -- it runs $0.91$ to $1.11$.  *The two
twelve-band routes are reported below rather than averaged in, and the reason is measured.*

⇒ *** THE TERM MIX CARRIES $0.53$ OF THE STEP AND THE REALISED PAIR $0.05$, AGAINST A FLOOR OF $0.91$.  THEY
CANNOT BE RESOLVED BY ANY STATISTIC THIS CONSTRUCTION CAN BUILD. ***

⌗ ** AND THE REASON IS THE ONE THING THE PRE-REGISTRATION DID NOT EXPECT. **  *The held-period aggregation
lowers $\sigma$ by $2.13\times$ **exactly as predicted** -- and lowers the **signal** by $2.46\times$ at the
same time.*  The ratio that matters does not improve: $f_{\min}$ goes from $0.96$ to $1.11$.  ** The candidate
named in advance as the one expected to help most does not help. **

⛔ ** AND THE PRE-REGISTERED HAZARD FIRED BEFORE ANY POWER CLAIM COULD BE MADE. **  The term mix and the
realised pair ** change sign ** between the two aggregations, so their departures are not established at
all and more power would not decide them.  *Only the window channel keeps its sign on all eight readings.*

⛭⛭⛭ ** ⓶ THE PHASE IS RESOLVED WHERE IT IS NOT NEEDED AND NOT WHERE IT IS. **  The long-stretch projection
works: over the upper range the relative phase is $+0.102910 \pm 0.015101$ rad -- $+5.90$ degrees, a
$6.8\sigma$ determination -- and the whole range as one stretch agrees at $+0.108517$.  Band 1 reads
$+0.025464$ rad, ** $2.56$ scatters away on the full-period yardstick. **

⛔ ** BUT THAT YARDSTICK IS WRONG, AND THE COMPARISON IS NOT LICENSED WITHOUT THE CONTROL. **  Band 1 is
$0.70$ of a period, and a projection over a non-integer number of periods **leaks the baseline** into $C$
and $S$, so a narrow stretch is both noisier and biased.  *On six stretches of the **same** width across the
upper range the scatter is $1.79\times$ larger.*

⇒ *** BAND 1 SITS $1.62$ SCATTERS OUT, NOT $2.56$: THE PHASE STEP IS NOT RESOLVED, AND `cc66.60`'s AMPLITUDE
VERDICT STANDS AS THE COMPLETE ONE RATHER THAN THE SIGN-ONLY ONE. ***

⌗ *The method reaches a $15\%$ measurement over five periods and cannot bring it to the one band that needs
it, because that band is narrower than the period the method needs.  **The same structural limit in a third
disguise** -- `cc66.58` met it on the window-free family, `cc66.60` on the amplitude/phase trade-off.*

⛔⛔ ** ⓷ AND THE CANCELLATION IS NEITHER EXACT NOR APPROXIMATE -- IT IS AGGREGATION-DEPENDENT. **  On the raw
reading the joint vanishes to within its own scatter on all four bases ($0.24$–$0.54\sigma$); on the
phase-insensitive one it does not ($4.15$–$4.97\sigma$).  ⇒ *So ⓷ **inherits ⓵'s answer rather than choosing
a word** -- the third possibility the pre-registration named -- and the constraint-versus-coincidence
question cannot be settled here.*

⛭⛭⛭ ** `r7639` ⑱ -- THIS FILE READS THE ARM OF RECORD, AND THE CARRY SPLITS IN TWO INSIDE IT. **
PART 1 asks how LARGE the arm-control difference is against its own scatter, so the arm is carried onto
the control's comb coordinate before a band is cut.  ** PART 2 asks what the arm-control PHASE IS -- and
the carry's own parameter IS that phase: carried, the $6.8\sigma$ determination collapses to $0.4\sigma$,
so carrying there would not sharpen the statistic, it would DELETE it. **  And ⓷ moves by $0.003$ in the
worst of its eight readings, because both of its channels are controls.

⛔ ** AND THE CARRY IS LOAD-BEARING FOR THE HEADLINE, NOT A PRESENTATION CHOICE. **  Read without it on
the registered banding, the term mix's share is $0.505$ against a floor of $0.43$ -- *above* it -- and this
receipt's verdict would invert.  Carried, it is $0.533$ against $0.91$.

⚠ ** TWO REGISTERED FORMS MISS, AND BOTH FINDINGS SURVIVE. **  ⓵'s *every* route becomes every route that
bands at or above the comb's own period; over those six the floor runs $0.91$ to $1.11$, while the two
twelve-band routes -- bands $0.41$ wide against a comb period of $1.01$ -- put the full spread at
$3.87\times$ against the registered $1.35\times$.  And ⓶'s matched-width scatter is $1.79\times$ the
full-period one rather than the registered more-than-twice, which still leaves it larger and still leaves
the verdict turning on it.  *Both reported, neither re-toleranced.*

⌗ ** AND ⓵'s REGISTERED FORM PASSED ON THE NAMESAKE ARM ONLY BECAUSE A FILTER DROPPED ITS OWN WORST
ROUTE. **  That arm's raw twelve-band route reads an $f_{\min}$ of $52.16$, and this receipt's own `f_min < 10`
filter removed it -- so "every route" was never every route.  *On the arm of record the same route lands
INSIDE the filter, at $3.51$, and the miss is visible where it was not before.*

⛔ *No envelope, basis, abscissa or aggregation chosen; no new candidate; no mechanism proposed.  No corpus
edits.*
"""
import os
import sys

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
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7639_cc66_P15_repoint_paper'))
import own_comb_kinds as OCK                                                           # noqa: E402

# ** r7639 ⑱ -- THE ARM OF RECORD, AND A CARRY THIS RECEIPT MUST SPLIT IN TWO. **  Every arm read
#   below is `_leafrec1`.  PART 1 asks how LARGE the arm-control difference is against its own
#   scatter, which is an amplitude question, so the arm is carried onto the control's comb
#   coordinate before any band is cut (`r7637+70`'s ruling).  ** PART 2 asks what the arm-control
#   PHASE IS -- and the carry's own parameter IS that phase, so carrying there would set the
#   measured quantity to zero by construction. **  Both halves are MEASURED below, not argued.
FINE = {'lcdm': 'r6941_fine_lcdm.npz', 'cr': 'r6941_fine_cr_leafrec1.npz'}
NSK = 'r6941_fine_cr.npz'                     # the namesake arm, read for the comparison only
ETA = 'r6959_eta_cr_leafrec1.npz'
QE0 = np.asarray(np.load(os.path.join(SP, ETA))['q_edges'], float)
_QE_NSK = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
check("⛭ AND THE BAND EDGES ARE A DEFINITION AND NOT A MEASUREMENT: the arm-of-record eta bank's "
      "`q_edges` are BIT-IDENTICAL to the namesake's, so no pin on that leg could mean anything",
      QE0.shape == _QE_NSK.shape and QE0.tobytes() == _QE_NSK.tobytes(),
      f"{len(QE0)} edges, byte-for-byte equal")
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

NEED = ('r6959_eta_cr.npz', ETA, 'r6941_fine_lcdm.npz', NSK, FINE['cr'],
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


def fine(f):
    d = np.load(os.path.join(SP, f))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(q, y, win=1.0):
    e = env_a(q, y, win)
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


LC, DC, AC = fine(FINE['lcdm'])
LA, DA, AA = fine(FINE['cr'])
LN, DN, AN = fine(NSK)
QCq, QAq, QNq = LC / AC, LA / AA, LN / AN
TC, _PC, TA, _PA, DPHI = OCK._combs({'lcdm': (QCq, DC), 'cr': (QAq, DA)})
QAu = TC * (QAq / TA + DPHI / (2 * np.pi))     # the arm, on the CONTROL's comb coordinate
OCo = osc(QCq, DC)
OAo = osc(QAq, DA, TA / TC)                    # the arm's envelope over one of ITS OWN periods
# ⓵ the carried reading, which every band of PART 1 is cut on
g = np.linspace(max(QCq.min(), QAu.min()), min(QCq.max(), QAu.max()), len(LC))
OC = np.interp(g, QCq, OCo)
OA = np.interp(g, QAu, OAo)
# ⓶ the SAME arm, UNCARRIED, which is PART 2's statistic and PART 1's comparison
gU = np.linspace(max(QCq.min(), QAq.min()), min(QCq.max(), QAq.max()), len(LC))
OCU = np.interp(gU, QCq, OCo)
OAU = np.interp(gU, QAq, osc(QAq, DA))
# ⓷ the NAMESAKE arm as the registered reading had it, for what moves and what does not
gN = np.linspace(max(QCq.min(), QNq.min()), min(QCq.max(), QNq.max()), len(LC))
OCN = np.interp(gN, QCq, OCo)
ONN = np.interp(gN, QNq, osc(QNq, DN))
KO = {}
for nm, fn in KN:
    d = np.load(os.path.join(SP, fn))
    qk = d['ls'].astype(float) / float(d['l_A'])
    KO[nm] = np.interp(g, qk, osc(qk, d['Dl']))
KOU = {nm: np.interp(gU, g, KO[nm]) for nm, _ in KN}
KON = {nm: np.interp(gN, g, KO[nm]) for nm, _ in KN}


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
QE1 = np.append(QE0, QE0[-1] + (QE0[-1] - QE0[-2]))
QE2 = np.linspace(QE0[0], QE0[-1], 13)


def _fm(S):
    d = abs(float(np.mean([x[0] for x in S['arm']])))
    s = float(np.mean([x[1] for x in S['arm']]))
    return 2 * s / d, d, s


def fmin(QE, agg, **kw):
    return _fm(sig(QE, agg, **kw))


def reading(gg, oa, oc, ko, lq, loa):
    """the eight routes on whichever reading is handed in, and its 7-band signatures"""
    B = {a: sig(QE0, a, gg=gg, oa=oa, oc=oc, ko=ko) for a in ('raw', 'held')}
    out = [(f'{a}, 7 bands, per common q',) + _fm(B[a]) for a in ('raw', 'held')]
    ocl = np.interp(lq, QCq, OCo)
    kol = {nm: np.interp(lq, gg, ko[nm]) for nm, _ in KN}
    out += [(f'{a}, per common l',) + fmin(QE0, a, gg=lq, oa=loa, oc=ocl, ko=kol)
            for a in ('raw', 'held')]
    out += [(f'{a}, 8 bands to q={QE1[-1]:.2f}',) + fmin(QE1, a, gg=gg, oa=oa, oc=oc, ko=ko)
            for a in ('raw', 'held')]
    out += [(f'{a}, 12 finer bands',) + fmin(QE2, a, gg=gg, oa=oa, oc=oc, ko=ko)
            for a in ('raw', 'held')]
    return out, B


mL, mLN = np.isin(LA, LC), np.isin(LN, LC)
FL, BASE = reading(g, OA, OC, KO, QAu[mL], OAo[mL])
FN, BASEN = reading(gN, ONN, OCN, KON, QNq[mLN], osc(QNq, DN)[mLN])
print("    the arm of record, carried onto the control's comb        |  the namesake arm, as registered")
for (nm, f, d, s), (_, fn_, dn, sn) in zip(FL, FN):
    print(f"    {nm:28s} |d| {d:7.4f} s {s:7.4f} f_min {f:7.2f}  |  "
          f"|d| {dn:7.4f} s {sn:7.4f} f_min {fn_:7.2f}")
SANE = [r for r in FL if r[1] < 10]
SANEN = [r for r in FN if r[1] < 10]
# ⌘ THE ROUTES THAT BAND AT OR ABOVE THE COMB'S OWN PERIOD.  The registered form says "every
#   route", and the twelve-band routes cut bands 0.41 wide against a comb period of 1.01 -- so they
#   do not band the comb at all.  ** On the namesake arm that was hidden by this receipt's own
#   `f_min < 10` filter, which dropped its raw twelve-band route at 52.16 and left the claim
#   reading as though every route agreed. **  On the arm of record the same route lands INSIDE the
#   filter, so the registered form's miss is visible where it was not before.
WIDE = [r for r in SANE if 'finer' not in r[0]]
LOP, HIP = min(r[1] for r in WIDE), max(r[1] for r in WIDE)
LOS, HIS = min(r[1] for r in SANE), max(r[1] for r in SANE)
LON, HIN = min(r[1] for r in SANEN), max(r[1] for r in SANEN)
SH = {nm: abs(float(np.mean([x[0] for x in BASE['raw'][nm]])
                    / np.mean([x[0] for x in BASE['raw']['arm']]))) for nm in ('term mix', 'JOINT')}
SHN = {nm: abs(float(np.mean([x[0] for x in BASEN['raw'][nm]])
                     / np.mean([x[0] for x in BASEN['raw']['arm']]))) for nm in ('term mix', 'JOINT')}
check("⓵ EVERY ROUTE THAT BANDS AT OR ABOVE THE COMB'S OWN PERIOD GIVES THE SAME FLOOR TO WITHIN A "
      "QUARTER -- both aggregations, both abscissas and a longer lever arm",
      HIP / LOP < 1.35,
      f"f_min from {LOP:.2f} to {HIP:.2f} over {len(WIDE)} routes, {HIP / LOP:.2f}x")
check("⛔ AND THE REGISTERED FORM -- *every* route, the two twelve-band readings included -- MISSES ON "
      "THE ARM OF RECORD, WITH ITS CAUSE MEASURED: those bands are narrower than the comb period, so "
      "they do not band the comb.  ** Reported, not re-toleranced **",
      HIS / LOS > 1.35 and (QE2[1] - QE2[0]) < 0.5 * TC and (QE0[1] - QE0[0]) > 0.5 * TC,
      f"all {len(SANE)} routes {LOS:.2f} to {HIS:.2f} ({HIS / LOS:.2f}x against the registered 1.35x); "
      f"twelve-band width {QE2[1] - QE2[0]:.2f} and registered width {QE0[1] - QE0[0]:.2f} against the "
      f"comb's {TC:.2f}")
check("⚠ AND THE NAMESAKE ARM PASSED THE REGISTERED FORM ONLY BECAUSE ITS OWN RAW TWELVE-BAND ROUTE "
      "WAS FILTERED OUT: the filter is this receipt's `f_min < 10`, and the route it dropped is the one "
      "the arm of record keeps.  ** So 'every route' was never every route **",
      len(SANEN) == len(FN) - 1 and len(SANE) == len(FN) and HIN / LON < 1.35,
      f"the namesake drops {len(FN) - len(SANEN)} of {len(FN)} at f_min "
      f"{max(r[1] for r in FN):.2f} and then runs {LON:.2f} to {HIN:.2f}; the arm of record drops none")
check("AND THE HELD-PERIOD AGGREGATION LOWERS THE SCATTER EXACTLY AS PRE-REGISTERED -- AND LOWERS THE SIGNAL "
      "BY THE SAME FACTOR, so the ratio that matters does not move.  ** The candidate named in advance as "
      "the one expected to help most does not help **",
      FL[0][3] / FL[1][3] > 1.8 and abs((FL[0][3] / FL[1][3]) / (FL[0][2] / FL[1][2]) - 1) < 0.15,
      f"sigma falls {FL[0][3] / FL[1][3]:.2f}x, signal falls {FL[0][2] / FL[1][2]:.2f}x, f_min "
      f"{FL[0][1]:.2f} -> {FL[1][1]:.2f}; the namesake arm {FN[0][3] / FN[1][3]:.2f}x and "
      f"{FN[0][2] / FN[1][2]:.2f}x, f_min {FN[0][1]:.2f} -> {FN[1][1]:.2f}")
# ⌘ THE SAME ARM WITHOUT THE CARRY, ON THE REGISTERED BANDING, so the next check's floor is not
#   taken on trust: this is the reading 69's ruling replaces, and it is computed and not recalled.
BASEU = {a: sig(QE0, a, gg=gU, oa=OAU, oc=OCU, ko=KOU) for a in ('raw', 'held')}
FU = [_fm(BASEU[a]) for a in ('raw', 'held')]
SHU = {nm: abs(float(np.mean([x[0] for x in BASEU['raw'][nm]])
                     / np.mean([x[0] for x in BASEU['raw']['arm']]))) for nm in ('term mix', 'JOINT')}
LOU = min(r[0] for r in FU)
check("⇒ *** AND THE TWO CHANNELS SIT BELOW THAT FLOOR, SO NO STATISTIC THIS CONSTRUCTION CAN BUILD "
      "RESOLVES THEM AGAINST THE STEP ***",
      SH['term mix'] < LOP and SH['JOINT'] < LOP,
      f"term mix carries {SH['term mix']:.2f} and the realised pair {SH['JOINT']:.2f}, against a floor of "
      f"{LOP:.2f}; on the namesake arm {SHN['term mix']:.2f} and {SHN['JOINT']:.2f} against {LON:.2f}")
check("⛔ AND THE CARRY IS WHAT KEEPS THAT VERDICT: read on the arm of record WITHOUT it, on the "
      "registered banding, the term mix's share EXCEEDS the floor and this receipt's headline would "
      "invert.  ** The carry is load-bearing here and is not a presentation choice **",
      SHU['term mix'] > LOU and SH['term mix'] < LOP,
      f"uncarried, {SHU['term mix']:.3f} against a floor of {LOU:.2f}; carried, {SH['term mix']:.3f} "
      f"against {LOP:.2f}")
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


def delta_on(a, b, q=None, va=None, vc=None):
    """⓶ THE UNCARRIED READING, and that is the whole point of PART 2: the carry's own parameter is
    the arm-control phase, which is exactly what this function measures."""
    q, va, vc = (gU if q is None else q), (OAU if va is None else va), (OCU if vc is None else vc)
    pa, pc = phase_of(q, va, a, b), phase_of(q, vc, a, b)
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
# ⓶ THE NAMESAKE ARM'S SAME FOUR NUMBERS, so what moved is printed and not recalled -- and the
#   CARRIED arm's, which is how the class claim above is measured rather than asserted.
DUN = np.array([delta_on(x, x + 1.0, gN, ONN, OCN) for x in np.arange(QE0[1], QE0[-1] - 1.0 + 1e-9, 1.0)])
DUN = DUN[np.isfinite(DUN)]
MUN, SUN = float(np.mean(DUN)), float(np.std(DUN, ddof=1))
MATCHN = np.array([delta_on(x, x + W, gN, ONN, OCN)
                   for x in np.arange(QE0[1], QE0[-1] - W + 1e-9, W)])
MATCHN = MATCHN[np.isfinite(MATCHN)]
MMN, SMN = float(np.mean(MATCHN)), float(np.std(MATCHN, ddof=1))
D1N = delta_on(QE0[0], QE0[1], gN, ONN, OCN)       # the NAMESAKE's own band 1, never this arm's
DUC = np.array([delta_on(x, x + 1.0, g, OA, OC) for x in np.arange(QE0[1], QE0[-1] - 1.0 + 1e-9, 1.0)])
DUC = DUC[np.isfinite(DUC)]
MUC, SUC = float(np.mean(DUC)), float(np.std(DUC, ddof=1))
print(f"    the namesake arm, same stretches:           mean {MUN:+.6f} rad, scatter {SUN:.6f}")
print(f"    the arm of record CARRIED, same stretches:  mean {MUC:+.6f} rad, scatter {SUC:.6f}")
check("⛔⛭ AND THIS IS WHY PART 2 IS NOT CARRIED, MEASURED AND NOT ARGUED: the carry maps the arm onto "
      "the control's comb coordinate by the very phase offset measured here, so on the CARRIED arm the "
      "determination collapses to nothing.  ** Carrying here would not sharpen the statistic, it would "
      "DELETE it **",
      abs(MUC) / (SUC / np.sqrt(len(DUC))) < 2.0 < abs(MU) / (SU / np.sqrt(len(DU))),
      f"carried {MUC:+.6f} rad at {abs(MUC) / (SUC / np.sqrt(len(DUC))):.1f} sigma against the "
      f"uncarried {MU:+.6f} at {abs(MU) / (SU / np.sqrt(len(DU))):.1f} sigma")
check("⓶ THE LONG-STRETCH PROJECTION RESOLVES THE PHASE IN THE UPPER RANGE, which is what makes it a "
      "measurement rather than a bound: the mean of disjoint stretches agrees with the whole range taken as "
      "one, and is many sigma from zero",
      abs(MU) / (SU / np.sqrt(len(DU))) > 4 and abs(DFULL - MU) < SU,
      f"{MU:+.6f} +- {SU / np.sqrt(len(DU)):.6f} rad, a "
      f"{abs(MU) / (SU / np.sqrt(len(DU))):.1f} sigma determination; one stretch gives {DFULL:+.6f}")
check("⛔ BUT THE FULL-PERIOD YARDSTICK IS THE WRONG ONE FOR BAND 1, and the matched-width control shows it: "
      "a projection over a NON-INTEGER number of periods leaks the baseline, so a narrow stretch is "
      "NOISIER",
      W < PCOMB and SM > SU,
      f"band 1 is {W:.2f} of a period; matched-width scatter {SM:.6f} against the full-period {SU:.6f}, "
      f"{SM / SU:.2f}x")
check("⚠ AND THE REGISTERED FORM OF THAT CLAUSE -- the matched-width scatter at more than TWICE the "
      "full-period one -- MISSES ON THE ARM OF RECORD, while what it was registered to establish holds: "
      "the scatter is still larger, and the verdict below still turns on it.  ** Reported, not "
      "re-toleranced **",
      SM / SU < 2.0 and SM > SU and SMN / SUN > 2.0,
      f"{SM / SU:.2f}x on the arm of record against {SMN / SUN:.2f}x on the namesake arm, where the "
      f"registered 2x was set")
check("⇒ *** SO THE PHASE STEP IS NOT RESOLVED ON THE ONLY YARDSTICK THAT MATCHES IT, AND `cc66.60`'s "
      "AMPLITUDE VERDICT STANDS AS THE COMPLETE ONE RATHER THAN THE SIGN-ONLY ONE ***",
      Z1M < 2.0 < Z1,
      f"{Z1M:.2f} scatters on the matched-width control against {Z1:.2f} on the full-period one; the "
      f"namesake arm read {abs(D1N - MMN) / SMN:.2f} against {abs(D1N - MUN) / SUN:.2f}")
check("⛭ AND THE ARM IS PINNED ON A FIGURE THAT MOVES BY MORE THAN AN ORDER OF MAGNITUDE: the "
      "long-stretch phase determination. ** Revert the arm and this receipt cannot stay green **",
      MU > 0.05 and MUN < 0.02 and MU / MUN > 10,
      f"{MU:+.6f} rad on the arm of record against the namesake's {MUN:+.6f}, {MU / MUN:.1f}x")

# ==================================================================================================
print("\nPART 3 -- ⓷ THE CANCELLATION, ACROSS FOUR BASES AND BOTH AGGREGATIONS.")
print("-" * 100)
Z = {a: [abs(BASE[a]['JOINT'][k][0]) / BASE[a]['JOINT'][k][1] for k in range(4)] for a in ('raw', 'held')}
ZN = {a: [abs(BASEN[a]['JOINT'][k][0]) / BASEN[a]['JOINT'][k][1] for k in range(4)]
      for a in ('raw', 'held')}
for a in ('raw', 'held'):
    print(f"    {a:6s} joint departure / its own scatter, four bases: "
          + "  ".join(f"{v:.2f}" for v in Z[a])
          + "   | the namesake arm: " + "  ".join(f"{v:.2f}" for v in ZN[a]))
check("⛭ AND ⓷ DOES NOT MOVE WITH THE ARM, WHICH IS A MEASUREMENT AND NOT AN EXPECTATION: both "
      "channels of this comparison are CONTROL channels, so the arm enters only through the shared "
      "grid's endpoints and the four bases read the same on either arm",
      max(abs(Z[a][k] - ZN[a][k]) for a in ('raw', 'held') for k in range(4)) < 0.1,
      "worst base moves by "
      f"{max(abs(Z[a][k] - ZN[a][k]) for a in ('raw', 'held') for k in range(4)):.3f}")
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

# ⛭ EVERY ARM-OF-RECORD FIGURE THE HEADER PRINTS, TIED TO THE COMPUTATION.  Hand-written header
#   figures have been caught twice in this family by exactly this check, so the header is not trusted.
_DOC = SRC.split(chr(34) * 3)[1]
_FIG = (f'${LOP:.2f}$', f'${HIP:.2f}$', f'${SH["term mix"]:.2f}$', f'${SH["JOINT"]:.2f}$',
        f'${MU:+.6f}', f'${DFULL:+.6f}$', f'${D1:+.6f}$', f'${SM / SU:.2f}', f'${Z1M:.2f}$',
        f'${Z1:.2f}$', f'${HIS / LOS:.2f}', f'${SHU["term mix"]:.3f}$', f'${LOU:.2f}$',
        f'${max(r[1] for r in FN):.2f}$', f'${QE2[1] - QE2[0]:.2f}$', f'${TC:.2f}$')
check("⛭ AND EVERY ARM-OF-RECORD FIGURE THIS HEADER PRINTS IS THE COMPUTED ONE, compared and not "
      "merely found: a header figure written by hand has been caught twice in this family",
      all(x in _DOC for x in _FIG), f"{len(_FIG)} figures: " + ' '.join(_FIG))

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
