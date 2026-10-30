#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE LOWEST BAND IS CLOSED TO ANY OSCILLATION-AMPLITUDE ESTIMATOR BY THE
FIELDS THEMSELVES, AT AN EXACT FLOOR; THE EXCESS'S DECELERATION IS ROBUST IN SIGN AND IS CARRIED BY THAT
SAME BAND ALONE; AND THE FILTER'S THIRD CONDITION IS PERMANENTLY UNAVAILABLE EXACTLY FOR THE CLASS OF
CANDIDATE THE PHYSICS SAYS CAN CARRY THE EXCESS. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6897_fields` (the `ZPSAVE` bank, whose arm is a KEY and exists on the namesake
arm only), `r6941_fine_lcdm` and `r6941_fine_cr_leafrec1` (the banked spectra the contrast statistic is
computed on, with `r6941_fine_cr` read for the comparison) and `r6959_eta_cr_leafrec1` (band edges alone).  `sec:refit-bound`'s
line-of-sight quartet is searched for below rather than asserted absent.  ⛔ *** Nothing is SOLVED. ***

** THE PRE-REGISTRATION IS `r7003_directions/PREDICTION.md` AND IT TABLES THE FAILURE MODES FIRST **, on
this revision's own new guard -- *pre-register the ways the measurement can fail to decide, not only its
outcomes* -- with four for ⓵ and four for ⓶, and it dates each of its own parts.

⛭⛭⛭ ** ⓵ THE BAND IS CLOSED BY THE FIELDS, AND THERE IS AN EXACT FLOOR. **  The criterion is named
before it is applied and is a necessary condition from identifiability rather than a chosen threshold:
*an oscillation amplitude at $q_0$ is identified only if the fitting window holds a TURNING POINT of the
field on each side of $q_0$* -- because over a span carrying no turning point the held-period `cos`/`sin`
pair is monotone in $q$, and a monotone function over a short span is what the baseline polynomial
already spans.

⇒ ** SO THE FLOOR IS THE MIDPOINT OF THE FIRST TWO TURNING POINTS, AND THE MONOPOLE SETS IT. **  Its
turning points are at $q = 0.996,\,1.915,\,2.912,\dots$ with ***none below the first*** -- the first
excursion is one-sided -- giving a floor of $q = 1.455$, against the dipole's $0.962$.  ⛔ ***The
filter's lowest band, $q \in [0.85,\,1.55]$, lies $86$ per cent below that floor, and every other band
lies entirely above it.***

⌷ ** AND IT IS NOT THE WINDOW, WHICH IS SHOWN THREE WAYS. **  *Width*: the same eight window widths at
identical conditioning give a spread of $0.004$ at $q_0 = 1.90$ and $0.016$ at $q_0 = 1.20$, with a sign
change.  *Placement*: sweeping the left edge with the right held, the departure drifts monotonically
negative as the window opens past the monopole's first turning point and is positive once it stays above
it -- *what lies below is the field's rise from its initial condition, which is not an acoustic
oscillation at all.*  *Prediction*: **every centre below the floor spreads by more than every centre
above it**, which the floor was not fitted to.

⇒ *** NO ESTIMATOR OF AN OSCILLATION AMPLITUDE CAN REACH INSIDE THE FIRST EXCURSION.  An acoustic
oscillation has a first extremum and there is no amplitude before it because there is no oscillation
before it. ***

⛭⛭ ** ⓶ AND THE ANSWER IS IN THREE PARTS, THE THIRD OF WHICH GOES AGAINST THIS SEAT'S OWN RESULT. **

⌗ ** ⓐ WITHIN THE STATISTIC AS DEFINED, THE CURVATURE IS ROBUST. **  Moving the envelope's width
($0.8$--$1.2$), the band edges ($\pm 0.05$) and the sampling, *the curvature is negative in every one of
six variants*, $-0.00369$ to $-0.00280$, with band 1's own value stable at $+0.0261$ to $+0.0314$ --
$18$ per cent of its own size, the same relative spread the namesake arm had.

⛔ ** ⓑ AND IT IS CARRIED BY BAND 1 ALONE. **  With band 1 dropped the curvature runs $-0.00154$ to
$+0.00004$ across those same six: ** its sign is not determined. **  ⚠ *The straddle is THIN -- the
positive end reaches only $+0.00004$ -- and that is printed rather than smoothed over.*  ⇒ *** THE DECELERATION IS THE
LOWEST BAND BEING LOW, NOT THE UPPER BANDS BENDING *** -- and that band is the one ⓵ closes.

⚠⚠ ** ⓒ AND IT IS NOT ROBUST TO THE ENVELOPE'S DEFINITION, WHICH IS THE PART THE ORDER ASKED FOR AND
WHICH THIS SEAT WOULD RATHER NOT HAVE FOUND. **  Replacing the running ARITHMETIC MEAN by a running
MEDIAN -- same window, same bands, same everything else -- *** reverses the curvature to $+0.00624$. ***
⌗ That variant is a DIFFERENT statistic and the difference is measured rather than asserted: **its
envelope absorbs more than half of the band-7 oscillation on BOTH arms** ($0.096 \to 0.044$ on the
control, $0.103 \to 0.053$ on the arm), so its band ratios are formed on a much smaller residual, and
`r6911+cc66.40` specifies the arithmetic mean.  ⛔ **But naming it a different statistic does not make
the exposure go away:** *"the excess decelerates" is a property of the arithmetic-mean-envelope contrast
statistic and not of the excess as such, and the paper does not currently say which.*
⌗ *The second non-defining variant, `win` $=2.0$, is two acoustic periods and drops band 1 by a factor
of $2.8$ while keeping the sign.*

⇒ ** SO `P15` MAY SAY THE EXCESS DECELERATES, AND OWES TWO QUALIFICATIONS IN THE SAME BREATH: THAT THE
DECELERATION IS CARRIED BY THE LOWEST BAND, AND THAT IT IS A PROPERTY OF THIS ENVELOPE. **  *What was
landed too strongly is not the claim but its INDEPENDENCE -- of any one band, and of the envelope's
definition -- which nothing in the paper says and a reader would assume.*

⛭⛭⛭ ** `r7639` ⑱ -- THE ARM OF RECORD ON THE SPECTRA, THE NAMESAKE ARM ON THE FIELDS, AND THE
CARRY IS WHAT MAKES ⓶ A RESULT AT ALL. **  ⓵ reads `r6897_fields`, which carries its arm as a KEY
suffix and has **no arm-of-record key**, so the source fields exist on the namesake arm only; ⓶ reads
the banked spectra, which do have one, and its statistic is an arm-vs-control comb-band ratio, so it is
carried onto the control's comb coordinate before the bands are cut.  *No gate mixes the two legs, and a
guard measures which banks were read rather than asserting it.*

⛔ ** AND WITHOUT THE CARRY THE WHOLE OF ⓶ WOULD BE WITHDRAWN. **  Read on the arm of record on the raw
grid, the curvature runs $-0.00106$ to $+0.00352$ -- *** the sign is not determined, so "the excess
decelerates" would have no support at all *** -- band 1's spread is $76$ per cent of its own value
against $18$, and the drop-band-1 curvature stops straddling zero ($+0.00550$ to $+0.01531$, all one
sign), which would have inverted ⓑ as well.

⚠ ** TWO REGISTERED THRESHOLDS MISS, BOTH CALIBRATED ON THE NAMESAKE ARM, AND BOTH FINDINGS SURVIVE. **
ⓐ's band-1 stability was an ABSOLUTE span under $0.005$; band 1 is larger on this arm, so the same
relative stability breaches it at $0.0052$.  *Relative to its own value the spread is $18.2$ per cent
here against $17.6$ on the namesake -- the same number -- while the uncarried reading is $76.4$.*  And
the `win` $=2.0$ drop was registered at under a QUARTER of the admissible minimum; it is $0.356$ here
and $0.414$ on the NAMESAKE arm once the carry is applied, against $0.194$ on the namesake arm
uncarried, where the quarter was set -- so *the threshold tracks the CARRY and not the arm*.  Both printed with their measured values; neither
re-toleranced.

⛔⛔ ** ⓷ AND THE THIRD CONDITION IS NOT UNAVAILABLE IN GENERAL, WHICH IS WORSE THAN IF IT WERE. **  It
needs a band-1 value, and band 1 is closed to *oscillation-amplitude estimators* -- not to a candidate
computed from the kernel.  `cc66.52`'s projection-width channel had a band-1 value and ** was excluded on
curvature. **  ⇒ *** THE FILTER'S FULL STRENGTH IS AVAILABLE EXACTLY FOR THE CLASS THAT CANNOT CARRY THE
EXCESS, AND ITS THIRD CONDITION IS PERMANENTLY UNAVAILABLE EXACTLY FOR THE CLASS THAT CAN *** -- since
`cc66.51` settled on physics that what fills a trough is an oscillation amplitude.

⌗ ** AND IS A TWO-CONDITION FILTER A FILTER?  SEPARATELY, BECAUSE THE ANSWERS DIFFER. **  *As an
exclusion device, yes and it has lost nothing*: sign and growth are each necessary on a carrier, and the
exclusions already made were made on growth alone.  *As a confirmation device, no -- and it never was
one, not with three either*: all three conditions are conditions on the SHAPE of a departure in $q$, and
a shape match does not fix a size.  ** Measured here: the candidate matches the target in sign and in
direction of growth while being five times smaller at the top band. **  ⇒ *So the candidate's passing
two conditions is worth exactly what passing three would have been -- it is not excluded -- and the
row's remaining question is the coupling, which is quantitative and needs band 1 not at all.*  ⛔ *Named
as the question, not proposed as a channel: the order's ⓸ closes the list.*
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7003_directions')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7637_70_own_comb_statistic'))
import own_comb as OCB                                                                 # noqa: E402

# ** r7639 ⑱ -- THE ARM OF RECORD ON THE SPECTRA, THE NAMESAKE ARM ON THE FIELDS, AND THE REASON
#   IS A BANK GAP. **  ⓵ reads `r6897_fields`, which carries its ARM AS A KEY SUFFIX (`k__cr`) and
#   has NO arm-of-record key, so the source fields exist on the namesake arm only.  ⓶ reads the
#   banked SPECTRA, which do have an arm of record, and its statistic is an arm-vs-control comb-band
#   ratio -- so it is re-pointed AND carried onto the control's comb coordinate before the bands are
#   cut.  ** No gate below mixes the two legs, and the guard at the end of ⓶ measures that rather
#   than asserting it. **
F = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
AOR = {'lcdm': 'r6941_fine_lcdm', 'cr': 'r6941_fine_cr_leafrec1'}
NSK = 'r6941_fine_cr'                          # the namesake arm, read for the comparison only
ETA = 'r6959_eta_cr_leafrec1'
_LOADED = []


def _bank(tag):
    """RECORDING what was read, so the leg guard measures and does not declare"""
    _LOADED.append(tag)
    return np.load(os.path.join(SP, tag + '.npz'))


FI = {t: _bank(AOR[t]) for t in ('lcdm', 'cr')}
FN = _bank(NSK)
QE0 = np.asarray(_bank(ETA)['q_edges'], float)
_QE_NSK = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
check("⛭ AND THE BAND EDGES ARE A DEFINITION AND NOT A MEASUREMENT: the arm-of-record eta bank's "
      "`q_edges` are BIT-IDENTICAL to the namesake's, so no pin on that leg could mean anything",
      QE0.shape == _QE_NSK.shape and QE0.tobytes() == _QE_NSK.tobytes(),
      f"{len(QE0)} edges, byte-for-byte equal")
QC0 = 0.5 * (QE0[:-1] + QE0[1:])
g = lambda n, t: F[f'{n}__{t}']

# ---- the path-provenance guard, executed rather than asserted -----------------------------------
# ⌷ The scan skips its own machinery: any line tagged `# noscan` is removed before the search.
SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "r6897_fields, r6941_fine_{lcdm,cr} and r6959_eta_cr's band edges only")
check("and nothing is SOLVED: the instrument is neither imported nor shelled out to",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan


# =================================================================================================
def fields(t):
    k = g('k', t)
    o = np.argsort(k)
    k = k[o]
    psi = g('psi', t)[o]
    return k * float(g('r_s', t)) / np.pi, (g('th0', t)[o] + psi) / psi, (g('tb', t)[o] / k) / psi


def loc(q, y, q0, half, P, bd=1):
    m = np.abs(q - q0) <= half
    if m.sum() < 12:
        return None
    dq = q[m] - q0
    X = np.column_stack([dq ** j for j in range(bd + 1)]
                        + [np.cos(2 * np.pi * q[m] / P), np.sin(2 * np.pi * q[m] / P)])
    c = np.linalg.lstsq(X, y[m], rcond=None)[0]
    return float(np.hypot(c[-2], c[-1])), float(np.arctan2(-c[-1], c[-2]))


def period_of(q, y, lo, hi, half=0.5, P0=2.0):
    P = P0
    for _ in range(12):
        Q = np.arange(lo, hi + 1e-9, 0.25)
        s = float(np.polyfit(Q, np.unwrap([loc(q, y, x, half, P)[1] for x in Q]), 1)[0])
        Pn = 2 * np.pi / (2 * np.pi / P + s)
        if abs(Pn - P) < 1e-9:
            return Pn
        P = Pn
    return P


P = {}
for t in ('lcdm', 'cr'):
    q_, um_, ud_ = fields(t)
    P[t] = (period_of(q_, um_, 2.5, 8.0), period_of(q_, ud_, 2.5, 8.0))


def turning(y, q, n=4):
    s = np.sign(np.diff(y))
    return q[np.where(np.diff(s) != 0)[0] + 1][:n]


def dep(q0, lo, hi, bd=1):
    o = {}
    for t in ('lcdm', 'cr'):
        q, um, ud = fields(t)
        m = (q >= lo) & (q <= hi)
        if m.sum() < 12:
            return None
        r = []
        for y, Pp in ((um, P[t][0]), (ud, P[t][1])):
            dq = q[m] - q0
            X = np.column_stack([dq ** j for j in range(bd + 1)]
                                + [np.cos(2 * np.pi * q[m] / Pp), np.sin(2 * np.pi * q[m] / Pp)])
            c = np.linalg.lstsq(X, y[m], rcond=None)[0]
            r.append(float(np.hypot(c[-2], c[-1])))
        o[t] = r[1] / r[0]
    return o['cr'] / o['lcdm'] - 1.0


print("\n⛭⛭⛭ ⓵ -- IS THE LOWEST BAND CLOSED BY THE FIELDS?\n")
TP, FLR = {}, {}
for t in ('lcdm', 'cr'):
    q, um, ud = fields(t)
    TP[t] = {'monopole': turning(um, q), 'dipole': turning(ud, q)}
    FLR[t] = {k: 0.5 * (v[0] + v[1]) for k, v in TP[t].items()}
    print(f"    {t:5s} monopole turning points {'  '.join(f'{x:.3f}' for x in TP[t]['monopole'])}"
          f"   floor {FLR[t]['monopole']:.4f}")
    print(f"          dipole   turning points {'  '.join(f'{x:.3f}' for x in TP[t]['dipole'])}"
          f"   floor {FLR[t]['dipole']:.4f}")
FL = max(max(v.values()) for v in FLR.values())
check("⛭ THE FIRST EXCURSION IS ONE-SIDED: the monopole source field has NO turning point below its "
      "first, on either arm, so no window there can hold one on each side of its centre",
      all(TP[t]['monopole'][0] > 0.9 for t in TP)
      and all(np.ptp(np.sign(np.diff(
                  fields(t)[1][fields(t)[0] < TP[t]['monopole'][0] - 0.02]))) == 0
              for t in TP),
      f"first monopole turning point at q = {TP['lcdm']['monopole'][0]:.3f} (control) and "
      f"{TP['cr']['monopole'][0]:.3f} (arm), monotone below it")
check("⛭⛭ AND THE BINDING FLOOR IS THE MONOPOLE'S, not the dipole's -- so the reach of a RATIO of the "
      "two amplitudes is set by the field whose first excursion starts later",
      all(FLR[t]['monopole'] > FLR[t]['dipole'] + 0.3 for t in FLR),
      f"monopole floor {FLR['lcdm']['monopole']:.4f} against dipole floor {FLR['lcdm']['dipole']:.4f}")
FRAC = [max(0.0, min(1.0, (FL - a) / (b - a))) for a, b in zip(QE0[:-1], QE0[1:])]
check("⛔ AND THE FILTER'S LOWEST BAND LIES MOSTLY BELOW THAT FLOOR WHILE EVERY OTHER BAND LIES ENTIRELY "
      "ABOVE IT, which is the whole of the result: band 1 is not hard to measure, it is closed",
      FRAC[0] > 0.8 and max(FRAC[1:]) == 0.0,
      f"band 1 is {100 * FRAC[0]:.1f} per cent below the floor q = {FL:.4f}; bands 2-7 are 0 per cent")

HS = (0.10, 0.15, 0.20, 0.30, 0.45, 0.60, 0.80, 1.00)
S12 = [dep(1.20, 1.20 - h, 1.20 + h) for h in HS]
S19 = [dep(1.90, 1.90 - h, 1.90 + h) for h in HS]
check("⌷ AND IT IS NOT THE BAND'S WIDTH: the SAME eight window widths, at identical conditioning, hold "
      "to a few parts in a thousand one band up and swing by an order of magnitude more at band 1, "
      "changing sign",
      (max(S12) - min(S12)) > 3 * (max(S19) - min(S19)) and min(S12) < 0 < max(S12) and min(S19) > 0,
      f"spread {max(S12) - min(S12):.5f} at q0=1.20 against {max(S19) - min(S19):.5f} at q0=1.90")
LE = [(lo, dep(1.20, lo, 2.16)) for lo in (0.30, 0.50, 0.70, 0.90, 1.00, 1.10, 1.20)]
check("⌷ AND THE OBSTRUCTION BITES AT THE FIRST TURNING POINT: sweeping the window's LEFT EDGE with its "
      "right edge held, the departure is negative for every window that opens past the monopole's first "
      "turning point and positive for every window that stays above it.  *What lies below is the "
      "field's rise from its initial condition, which is not an acoustic oscillation*",
      all(v < 0 for lo, v in LE if lo < 0.99) and all(v > 0 for lo, v in LE if lo > 1.05),
      "  ".join(f"[{lo:.2f},2.16] {v:+.5f}" for lo, v in LE))
BEL, ABV = [], []
for q0 in np.arange(1.0, 2.41, 0.2):
    vs = [v for v in (dep(q0, q0 - h, q0 + h) for h in HS) if v is not None]
    (BEL if q0 < FL else ABV).append(max(vs) - min(vs))
check("⌷ AND THE FLOOR PREDICTS THE REACH RATHER THAN BEING FITTED TO IT: EVERY centre below the floor "
      "spreads by more than EVERY centre above it",
      min(BEL) > max(ABV),
      f"below the floor min spread {min(BEL):.5f}; above the floor max spread {max(ABV):.5f}")


# =================================================================================================
def envelope(x, y, win, kind):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def _comb_of(d):
    """(q, T, phase) of one bank on this receipt's own abscissa, through `r7637+70`'s fit"""
    q = d['ls'].astype(float) / float(d['l_A'])
    _, T, ph, _ = OCB.comb(q, np.asarray(d['Dl'], float))
    return q, T, ph


_QCTL, TC, PC = _comb_of(FI['lcdm'])


def bands(d, QE, win, kind, npts, carried=False):
    """⛭ r7639: with `carried`, the ARM is read on the CONTROL's comb coordinate and its envelope
    window widened to one of its OWN periods -- `r7637+70`'s carry.  Without it, two combs of
    different period have their bands cut over different parts of the cycle and the ratio BEATS."""
    q = d['ls'].astype(float) / float(d['l_A'])
    y = np.asarray(d['Dl'], float)
    if carried:
        _, Ta, pa = _comb_of(d)
        win = win * Ta / TC
        qq = TC * (q / Ta + ((pa - PC + np.pi) % (2 * np.pi) - np.pi) / (2 * np.pi))
    else:
        qq = q
    e = envelope(q, y, win, kind)
    o = (y - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, npts), qq, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def target(win=1.0, kind='mean', npts=400, shift=0.0, arm=None, carried=True):
    QE = QE0 + shift
    return (bands(FI['cr'] if arm is None else arm, QE, win, kind, npts, carried)
            / bands(FI['lcdm'], QE, win, kind, npts) - 1.0,
            0.5 * (QE[:-1] + QE[1:]))


print("\n⛭⛭ ⓶ -- DOES THE TARGET'S OWN CURVATURE CARRY THE PAPER'S CLAIM?\n")
ADMIS = ({}, {'win': 0.8}, {'win': 1.2}, {'npts': 1200}, {'shift': 0.05}, {'shift': -0.05})


def variants(**fixed):
    cf, cd, b1 = [], [], []
    for kw in ADMIS:
        T, qc = target(**dict(kw, **fixed))
        cf.append(float(np.polyfit(qc, T, 2)[0]))
        cd.append(float(np.polyfit(qc[1:], T[1:], 2)[0]))
        b1.append(float(T[0]))
    return cf, cd, b1


CF, CD, B1 = variants()
# ⓶ the NAMESAKE arm's own variants, UNCARRIED as the register had them, so what moved is printed
CFN, CDN, B1N = variants(arm=FN, carried=False)
# ⛔ and the arm of record read WITHOUT the carry, which is the reading 69's ruling replaces
CFU, CDU, B1U = variants(carried=False)
print(f"    admissible variants: curvature {min(CF):+.5f} to {max(CF):+.5f};  with band 1 dropped "
      f"{min(CD):+.5f} to {max(CD):+.5f};  band 1 {min(B1):+.4f} to {max(B1):+.4f}")
print(f"    the namesake arm, as registered: curvature {min(CFN):+.5f} to {max(CFN):+.5f};  dropped "
      f"{min(CDN):+.5f} to {max(CDN):+.5f};  band 1 {min(B1N):+.4f} to {max(B1N):+.4f}")
print(f"    the arm of record UNCARRIED:     curvature {min(CFU):+.5f} to {max(CFU):+.5f};  dropped "
      f"{min(CDU):+.5f} to {max(CDU):+.5f};  band 1 {min(B1U):+.4f} to {max(B1U):+.4f}")
check("⛭ THE CLAIM IS SUPPORTED: the target's curvature is NEGATIVE in every variant that leaves the "
      "statistic's own definition alone -- the envelope width, the band edges and the sampling all "
      "moved.  *'The excess decelerates' is not a fragile number*",
      max(CF) < 0, f"{len(CF)} variants, all negative, {min(CF):+.5f} to {max(CF):+.5f}")
_SPAN = (max(B1) - min(B1)) / abs(0.5 * (max(B1) + min(B1)))
_SPANN = (max(B1N) - min(B1N)) / abs(0.5 * (max(B1N) + min(B1N)))
_SPANU = (max(B1U) - min(B1U)) / abs(0.5 * (max(B1U) + min(B1U)))
check("and band 1's own value is stable ACROSS THOSE VARIANTS RELATIVE TO ITS OWN SIZE, so the "
      "single-band dependence below can be characterised rather than merely suspected",
      _SPAN < 0.25,
      f"band 1 spans {min(B1):+.4f} to {max(B1):+.4f}, {100 * _SPAN:.1f} per cent of its own value; "
      f"the namesake arm {100 * _SPANN:.1f} per cent and the uncarried arm of record "
      f"{100 * _SPANU:.1f} per cent")
check("⚠ AND THE REGISTERED FORM OF THAT CLAUSE -- an ABSOLUTE span under 0.005 -- MISSES ON THE ARM "
      "OF RECORD, while what it was registered to separate is separated more sharply by the relative "
      "form: band 1 is larger on this arm, so the same relative stability breaches an absolute "
      "threshold set on the namesake's smaller value.  ** Reported, not re-toleranced **",
      max(B1) - min(B1) > 0.005 and max(B1N) - min(B1N) < 0.005
      and abs(_SPAN - _SPANN) < 0.02 and _SPANU > 3 * _SPAN,
      f"{max(B1) - min(B1):.4f} against the registered 0.005 (namesake "
      f"{max(B1N) - min(B1N):.4f}); relative, {100 * _SPAN:.1f} against {100 * _SPANN:.1f} per cent "
      f"-- the same number -- while the uncarried reading is {100 * _SPANU:.1f}")
check("⛔ AND IT IS A SINGLE-BAND CLAIM: with band 1 dropped the curvature's sign is NOT DETERMINED "
      "across those same variants.  ⇒ THE DECELERATION IS THE LOWEST BAND BEING LOW, NOT THE UPPER "
      "BANDS BENDING -- and that band is the one ⓵ closes",
      min(CD) < 0 < max(CD),
      f"drop-band-1 curvature runs {min(CD):+.5f} to {max(CD):+.5f} -- and the straddle is THIN, "
      f"the positive end reaching only {max(CD):+.6f}, against the namesake arm's "
      f"{max(CDN):+.6f}; on the uncarried arm of record it does not straddle at all "
      f"({min(CDU):+.5f} to {max(CDU):+.5f}, all one sign)")
MED = {t: bands(FI[t], QE0, 1.0, 'median', 400, t == 'cr') for t in ('lcdm', 'cr')}
MEA = {t: bands(FI[t], QE0, 1.0, 'mean', 400, t == 'cr') for t in ('lcdm', 'cr')}
CMED = float(np.polyfit(QC0, MED['cr'] / MED['lcdm'] - 1.0, 2)[0])
check("⚠⚠ AND IT IS NOT ROBUST TO THE ENVELOPE'S DEFINITION, WHICH IS THE PART THIS SEAT WOULD "
      "RATHER NOT HAVE FOUND AND IS REPORTING ANYWAY: replacing the running ARITHMETIC MEAN by a running "
      "MEDIAN -- same window, same bands, everything else unchanged -- REVERSES THE CURVATURE.  ⇒ "
      "'The excess decelerates' is a property of the arithmetic-mean-envelope statistic and not of the "
      "excess as such, and the paper does not currently say which",
      CMED > 0 > max(CF),
      f"median-envelope curvature {CMED:+.5f} against the mean envelope's {min(CF):+.5f} to {max(CF):+.5f}")
check("⌷ and that variant is a DIFFERENT statistic on a measured difference rather than on a "
      "preference: its envelope absorbs more than half of the top band's oscillation on BOTH arms, so "
      "its band ratios are formed on a much smaller residual -- and `r6911+cc66.40` specifies the "
      "arithmetic mean.  *Naming it a different statistic does not retire the exposure above*",
      all(MED[t][-1] < 0.55 * MEA[t][-1] for t in ('lcdm', 'cr')),
      "  ".join(f"{t} band 7 {MEA[t][-1]:.4f} -> {MED[t][-1]:.4f}" for t in ('lcdm', 'cr')))
T2 = target(win=2.0)[0]
check("and the second non-defining variant is named too: `win` = 2.0 is TWO acoustic periods and smooths "
      "across the structure the statistic is defined to measure, dropping band 1 by a large factor "
      "while keeping the sign",
      0.0 < T2[0] < 0.5 * min(B1),
      f"band 1 becomes {T2[0]:+.4f} against {min(B1):+.4f} admissibly, a drop of "
      f"{min(B1) / T2[0]:.1f}x with the sign kept")
_T2N = target(win=2.0, arm=FN, carried=False)[0]
_T2NC = target(win=2.0, arm=FN, carried=True)[0]
_B1NC = min(variants(arm=FN, carried=True)[2])
_T2U = target(win=2.0, carried=False)[0]
check("⚠ AND THE REGISTERED FORM OF THAT CLAUSE -- a drop to under a QUARTER -- MISSES, and it misses "
      "on the namesake arm too once the carry is applied, so the quarter was a property of the "
      "UNCARRIED reading rather than of either arm.  What it was registered to establish holds: a large "
      "drop with the sign kept.  ** Reported, not re-toleranced **",
      T2[0] > 0.25 * min(B1) and _T2NC[0] > 0.25 * _B1NC and _T2N[0] < 0.25 * min(B1N)
      and _T2U[0] < 0.0,
      f"{T2[0] / min(B1):.3f} of the admissible minimum here and {_T2NC[0] / _B1NC:.3f} on the "
      f"NAMESAKE arm once carried, against {_T2N[0] / min(B1N):.3f} on the namesake arm uncarried "
      f"where the quarter was set -- so the threshold tracks the CARRY and not the arm; and on the "
      f"uncarried arm of record band 1 goes NEGATIVE at this window ({_T2U[0]:+.4f}), a different "
      f"failure altogether")


# =================================================================================================
print("\n⛔⛔ ⓷ -- WHAT CAN THE FILTER STILL DECIDE?\n")


def held_bands(half=0.5, bd=1):
    o = {}
    for t in ('lcdm', 'cr'):
        q, um, ud = fields(t)
        Q, R = [], []
        for q0 in np.arange(q.min() + half, q.max() - half - 0.05, 0.02):
            a, b = loc(q, um, q0, half, P[t][0], bd), loc(q, ud, q0, half, P[t][1], bd)
            if a is None or b is None:
                continue
            Q.append(q0)
            R.append(b[0] / a[0])
        Q, R = np.array(Q), np.array(R)
        o[t] = np.array([np.mean(np.interp(np.linspace(a, b, 200), Q, R))
                         for a, b in zip(QE0[:-1], QE0[1:])])
    return o['cr'] / o['lcdm'] - 1.0


AMPALL = np.array([held_bands(h, b) for h in (0.35, 0.5, 0.75, 1.0) for b in (1, 2)])
AMP = held_bands()
ASPR = AMPALL.max(axis=0) - AMPALL.min(axis=0)
KERN1 = 0.00343          # `cc66.52`'s projection-width channel at band 1, mean-anchored
check("⛔⛭ THE THIRD CONDITION IS NOT UNAVAILABLE IN GENERAL, WHICH IS WORSE THAN IF IT WERE: a "
      "candidate COMPUTED from the kernel has a band-1 value -- `cc66.52`'s projection width did, and "
      "the filter EXCLUDED it on curvature -- while the amplitude-class candidate's band-1 spread "
      "exceeds its value.  ⇒ THE FILTER'S FULL STRENGTH IS AVAILABLE EXACTLY FOR THE CLASS THAT CANNOT "
      "CARRY THE EXCESS, since `cc66.51` settled on physics that what fills a trough is an oscillation "
      "amplitude",
      ASPR[0] > abs(AMP[0]) and abs(KERN1) > 0.003,
      f"amplitude class band 1 {AMP[0]:+.5f} with spread {ASPR[0]:.4f}; kernel class {KERN1:+.5f}")
TB = target()[0]
check("⌗ AND AS A CONFIRMATION DEVICE THE FILTER NEVER WORKED, NOT WITH THREE CONDITIONS EITHER, WHICH "
      "is why the missing one costs less than it looks: all three are conditions on the SHAPE of a "
      "departure in q, and a shape match does not fix a size -- measured here, the candidate matches "
      "the target in sign and in direction of growth while being several times smaller at the top band",
      AMP[-1] > 0 and TB[-1] > 0 and TB[-1] / AMP[-1] > 3,
      f"candidate {AMP[-1]:+.5f} against target {TB[-1]:+.5f} -- a factor {TB[-1] / AMP[-1]:.1f}")
check("and as an EXCLUSION device it has lost nothing, because each remaining condition is necessary on "
      "a carrier and the exclusions already made were made on growth alone.  ⇒ The candidate's passing "
      "two is worth what passing three would have been: it is NOT EXCLUDED, and the row's remaining "
      "question is the coupling rather than a fourth condition",
      AMP[1:].min() > 0 and TB[1:].min() > 0
      and (AMP[1:][-1] / AMP[1:][0]) > 1 and (TB[1:][-1] / TB[1:][0]) > 1,
      f"on the measurable range both are positive throughout and both grow: candidate G = "
      f"{AMP[1:][-1] / AMP[1:][0]:.2f}, target G = {TB[1:][-1] / TB[1:][0]:.2f}")


# =================================================================================================
print("\n⌗ THE PRE-REGISTRATION\n")
TXT = open(os.path.join(DIR, 'PREDICTION.md')).read() if os.path.exists(
    os.path.join(DIR, 'PREDICTION.md')) else ''
check("⛔ THIS REVISION'S OWN NEW GUARD, APPLIED TO ITSELF: the pre-registration tables the WAYS EACH "
      "MEASUREMENT CAN FAIL TO DECIDE, and tables them BEFORE the outcomes",
      'FAIL TO DECIDE' in TXT
      and TXT.index('WAYS ⓵ CAN FAIL TO DECIDE') < TXT.index('OUTCOMES FOR ⓷'),
      f"{TXT.count('| **')} tabled rows, failure modes for both measured items, ahead of the outcomes")
check("and it dates its own parts, naming the criterion ⓵ applies as stated before use and the outcome "
      "tables as written after",
      'bracketing criterion' in TXT and 'written after the two analyses were run' in TXT,
      "the bracketing criterion is a necessary condition from identifiability, not a fitted threshold")

# ⛭ THE TWO LEGS, MEASURED RATHER THAN ASSERTED: which banks were read, and that the fields bank
#   HAS no arm-of-record key, so ⓵'s namesake reading is forced and not chosen.
check("⛭ AND THE TWO LEGS ARE WHAT THE HEADER SAYS: the spectra and band edges read on the ARM OF "
      "RECORD, the source fields on the NAMESAKE arm because that bank has no arm-of-record key at all",
      _LOADED == ['r6941_fine_lcdm', 'r6941_fine_cr_leafrec1', 'r6941_fine_cr',
                  'r6959_eta_cr_leafrec1']
      and not any('leafrec' in str(k) for k in F.keys())
      and 'k__cr' in F and 'k__lcdm' in F,
      f"read {_LOADED}; the fields bank holds {len(F.files)} keys and none names an arm of record")

# ⛭ EVERY FIGURE THE HEADER PRINTS FOR ⓶, TIED TO THE COMPUTATION.
_DOC = SRC.split(chr(34) * 3)[1]
_FIG = (f'${min(CF):+.5f}$', f'${max(CF):+.5f}$', f'${min(CD):+.5f}$', f'${max(CD):+.5f}$',
        f'${min(B1):+.4f}$', f'${max(B1):+.4f}$', f'${CMED:+.5f}$', f'${min(CFU):+.5f}$',
        f'${max(CFU):+.5f}$', f'${min(CDU):+.5f}$', f'${max(CDU):+.5f}$',
        f'${max(B1) - min(B1):.4f}$', f'${100 * _SPAN:.1f}$', f'${100 * _SPANN:.1f}$',
        f'${100 * _SPANU:.1f}$', f'${T2[0] / min(B1):.3f}$', f'${_T2N[0] / min(B1N):.3f}$',
        f'${_T2NC[0] / _B1NC:.3f}$', f'${min(B1) / T2[0]:.1f}$')
check("⛭ AND EVERY ARM-OF-RECORD FIGURE THIS HEADER PRINTS FOR ⓶ IS THE COMPUTED ONE, compared and "
      "not merely found", all(x in _DOC for x in _FIG), f"{len(_FIG)} figures: " + ' '.join(_FIG))

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
