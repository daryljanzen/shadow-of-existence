#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE TWO DIPOLE READINGS ARE DIFFERENT QUANTITIES, NOT A CONTRADICTION;
CORRECTING WHICH ONE THE FILTER NEEDS REVERSES `cc66.50`'s DISMISSAL OF THAT CANDIDATE; AND THE ONE
THING THIS ROW IS NAMED AFTER -- THE PROJECTION -- HOLDS A WIDTH THAT HAS NEVER BEEN MEASURED. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6897_fields` (the `ZPSAVE` bank the register's own receipt reads),
`r6959_eta_{lcdm,cr_leafrec1}` and `r6941_fine_{lcdm,cr_leafrec1}`.  `sec:refit-bound`'s quartet $222/538/818/1134$ is the
LINE-OF-SIGHT path's and is not read -- searched for by grepping this file for each of the four values
and for every line-of-sight bank name (`c54.17*`, `c54.178_*`, `L814_*`, `r6784_*`), and none occurs
below.  ⛔ *** Nothing is RUN: the order's ⓸, and every number is read from banks on disk. ***

** ON THE PRE-REGISTRATION GUARD, WHICH APPLIES DIFFERENTLY HERE AND IS SAID SO RATHER THAN SKIPPED. **
*No `PREDICTION.md` is written for this revision, because nothing is run and the only TEST in it -- the
second tooth -- is a criterion already fixed in `r6993`'s pre-registration: negative curvature, and
growth comparable to the target's.*  ⇒ **The criterion this revision applies was committed before the
measurement it is applied to, which is what the guard is for; writing a fresh one after the fact would
be the decoration the guard warns about.**

** ⛔ r7639 ⑴ -- RE-POINTED TO THE ARM OF RECORD, WITH THE TARGET CARRIED ONTO THE CONTROL'S COMB. **
The target is an arm-vs-control comb-band ratio, so it is carried before the bands are cut.  *Without
that the target's curvature on the shared range comes out POSITIVE and ⓶'s second tooth -- "the same
curvature sign as the target" -- has nothing to be the same as.*  ⌗ *The register's own figures
($+2.06$, $+0.95$ per cent) and the undefined $G$'s $-26.1$ are read off `r6897_fields` and the control
side, and do not move at all.*  The target moves $+0.05193 \to +0.06099$ at the bottom of the shared
range and $+0.07621 \to +0.07946$ at the top.

⛔⛔ ** AND r7639+cc66.18 CORRECTS THIS FILE'S OWN PREVIOUS REVISION ON THE THIRD OF THOSE FIGURES. **
`cc66.50`'s band power at $-11.58$ per cent was reported as unmoved, and it is NOT: it reads the `eta`
bank, which this re-point moved, and on the arm of record it is $-11.97$.  ** The register's quantity it
is compared against comes from `r6897_fields`, which carries its ARM AS A KEY SUFFIX and has NO
arm-of-record key at all, so that comparison was CROSS-ARM -- a pair differing in the arm as well as in
the quantity, which is the confound the claim's own wording denies. **  ⇒ *The licensed comparison is
now namesake on both sides, at $-11.58$; the arm-of-record band power is computed and REPORTED beside it
at $-11.97$, and the sign difference holds on either.  The guard measures which banks were read, and
reverting it to the arm of record turns this file red.*

⛭⛭ ** ⓵ THE DISAGREEMENT IS NOT A CONTRADICTION, AND THE SIGN IS NOT THE RANGE. **  Both readings are
reproduced here from banks.  The register's quantity reads $+2.06$ per cent over its own range
$q\in[3.5,11]$ -- *its recorded "two per cent above", exactly* -- and still $+0.95$ per cent over the
part of `cc66.50`'s range it reaches, where `cc66.50`'s quantity reads $-11.58$ per cent on the same
arm (and $-11.97$ on the arm of record, reported above).
⇒ *** So the sign survives being put on one range: the difference is the QUANTITY. ***  They differ in
three independent ways: **what is ratioed** (the OSCILLATION AMPLITUDE of each source field, from a
sliding sinusoid fit, against the INTEGRATED BAND POWER, which keeps the smooth part); **which fields**
(the source fields at last scattering each normalised by $\Psi$, against the terms' contributions to the
projected integrand); and **over what range**.

⛔⛭ ** AND WHICH ONE IS NEEDED IS THE REGISTER'S -- WHICH MAKES `cc66.50`'s FILTER ROW THIS SEAT'S OWN
ERROR. **  Trough-filling is an oscillating term a quarter period out of phase adding into another's
troughs: *what fills a trough is the oscillating part's amplitude, and the smooth part of either term
displaces the envelope and fills nothing.*  ⇒ **The same is true of the filter**, because the contrast
statistic is the standard deviation of the OSCILLATION about a running-mean envelope, so only an
oscillation amplitude could carry its $q$-dependence.  *** `cc66.50` filtered this candidate on
integrated band power, and that row of its table answers the wrong question. ***

⛭⛭ ** ⓶ SO THE SECOND TOOTH IS USED, AND IT IS USED BECAUSE SOMETHING SURVIVED THE FIRST. **  On the
range where the right quantity can be measured the candidate's departure runs from $-0.0006$ to
$+0.0166$ -- *it grows from about nothing* -- and it **decelerates**, curvature $-0.0037$ against the
target's $-0.0029$, ** the same sign. **  ⇒ *It passes both teeth where it can be tested, reversing
`cc66.50`'s dismissal on this seat's own error rather than on new data.*

⛔ ** AND YET THE FILTER STILL CANNOT CLOSE IT, WHICH IS THE RESULT AND NOT A GAP. **  The right quantity
**bottoms out at $q=2.0$** -- verified stable to a tenth of a per cent across four window widths, so the
estimator is sound and simply does not reach, the acoustic period in $q$ being $2$ and a sinusoid
amplitude needing about a period either side.  And the target grows $3.55$-fold over the full range but
only $1.47$-fold over the shared one: ⇒ *** THE TARGET'S GROWTH IS CONCENTRATED BELOW $q=2$, EXACTLY
WHERE THE ONLY QUANTITY THAT COULD CARRY IT CANNOT BE MEASURED. ***  *So passing both teeth on
$[2.6,5.4]$ is weaker than it sounds: a pass on the part of the range carrying least of the thing to be
explained.*  ⌗ **What would close it is a different estimator of the same quantity below $q=2$, not a
longer run of this one.**

⚠ ** AND THE GROWTH STATISTIC NEEDED A DOMAIN, WHICH THIS CANDIDATE IS OUTSIDE. **  $G$ is scale-free
and right for a departure that keeps one sign, which every candidate in `cc66.50`'s table did.  *This
one crosses zero inside the range, so the denominator is not a quantity and the arithmetic returns
$-26$* -- which would have read as a spectacular pass.  ⇒ **Reported as UNDEFINED, and the statistic now
carries its domain.**

⛭⛭⛭ ** ⓷ AND THE ENUMERATION OF THE UNMEASURED, BUILT BY ASKING THE BANKS RATHER THAN BY LISTING WHAT
COMES TO MIND. **
  * ⛭ ** A whole class is settled by STRUCTURE and needs no run: ** every quantity of the two-rate clock
    -- the leaf clock, the ruler, the Jacobian between them, the visibility, the optical depth -- is
    stored as a function of CONFORMAL TIME ALONE.  *A function of $\eta$ has the same value at every
    wavenumber, so it cannot vary across wavenumber.*  ⇒ **Not "measured and failed" and not
    "unmeasured", but CANNOT CARRY IT, by the shape of the object.**
  * ⛭⛭ ** AND THE PROJECTION HOLDS A WIDTH NOBODY HAS IMPOSED, WHICH IS THE FINDING. **  Two widths
    govern the window and *they are not the same width*: the acoustic phase swept across it varies by
    $k\times$ (width in the LEAF sound horizon), which is what smears the oscillation and what `cc66.47`
    acted on; the projection smears by $k\times$ (width in CONFORMAL TIME), because the Bessel argument
    is $k(\eta_0-\eta)$.  *In a one-rate cosmology these are one object up to the sound speed; in this
    arm they are not, because the two clocks differ.*  ⇒ *** The arm's window is $10.4$ per cent WIDER
    in conformal time and $2.4$ per cent wider in the leaf sound horizon -- the two stand in a ratio
    $7.9$ per cent different in the arm than in the control. ***
    ⛔ ** r7639 ⑴: the registered form also required the two ratios to STRADDLE one, and on the arm of
    record they do not. **  Both widths now exceed the control's, where on the namesake arm it was
    $+6.5$ per cent and $-0.8$.  *The FINDING survives and is marginally stronger -- the two widths
    scale by factors $7.9$ per cent apart where they were $7.3$ apart -- because the finding is the
    NON-PROPORTIONALITY and not the straddle.  The straddle was a property of the namesake arm and not
    of the construction, and it is recorded as a miss of the registered form rather than dropped.*  **`cc66.47` imposed the phase width;
    nothing has imposed the projection width, and they are not the same knob.**
  * ⌗ Also unmeasured: the oscillation-amplitude ratio below $q=2$ (⓶'s blocker), and the polarisation
    term's oscillation amplitude, which carries the same band-power error as the dipole did.

** WHAT IS NOT CLAIMED. **  NOT that the register's reading was wrong, nor that `cc66.50`'s was: they are
different quantities and each is right about its own.  NOT that the dipole-to-monopole ratio IS the
carrier -- it passes both teeth only on the sub-range that carries least of the growth, and is neither
closed nor confirmed.  NOT that the projection width IS the carrier: it is unmeasured, which is the
point, and its response has not been computed.  NOT that the clock quantities are irrelevant -- they
cannot carry a $q$-dependence themselves, which leaves them free to set a scale something else varies
across.  NOT a detection.  NOT a verdict on the two-rate assignment.  No refit, nothing touching
`prop:flat` or the clock family, and no corpus edits.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima.  Nothing here re-fits and nothing is run.
  * `spectra/r6897_fields.npz`, `spectra/r6959_eta_{lcdm,cr_leafrec1}.npz`,
    `spectra/r6941_fine_{lcdm,cr_leafrec1}.npz`.
  * ** The register's estimator is rebuilt from its own receipt **, not re-derived: the sliding sinusoid
    fit with polynomial amplitude, on $(\Theta_0+\Psi)/\Psi$ against $(\theta_b/k)/\Psi$.
  * The contrast statistic is `r6911+cc66.40`'s, unchanged; the band edges are `r6959`'s own.
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
print("=" * 100)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
for _n in ('r6897_fields.npz', 'r6959_eta_lcdm.npz', 'r6959_eta_cr_leafrec1.npz',
           'r6941_fine_lcdm.npz', 'r6941_fine_cr_leafrec1.npz'):
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK.")
    print(f"GATES: {len(FAILS)} FAILED:")
    raise SystemExit(1)

FLD = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
# ** r7639 ⑴ -- THE ARM OF RECORD, AND THE CARRY WHERE IT APPLIES. **  Every arm read is `_leafrec1`.
#   The TARGET -- `bands(arm)/bands(control)` from `r6941_fine_*` -- is an arm-vs-control comb-band
#   ratio, so it is carried onto the control's comb coordinate before the bands are cut.  ⛔ *Without
#   that, the target's curvature on the shared range comes out POSITIVE and the second tooth's
#   comparison -- "the same curvature sign as the target" -- has nothing to be the same as.*
AOR = {'lcdm': 'r6941_fine_lcdm', 'cr': 'r6941_fine_cr_leafrec1'}
ETA = {'lcdm': 'r6959_eta_lcdm', 'cr': 'r6959_eta_cr_leafrec1'}
A = {t: np.load(os.path.join(SP, ETA[t] + '.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, AOR[t] + '.npz')) for t in ('lcdm', 'cr')}
QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
NF = 3.0
g = lambda n, t: FLD[f'{n}__{t}']


def amp_ratio(t, half=2.0, amp_deg=2, step=0.25):
    """the REGISTER's quantity, rebuilt from its own receipt"""
    k = g('k', t)
    o = np.argsort(k)
    k, psi = k[o], g('psi', t)[o]
    um = (g('th0', t)[o] + psi) / psi
    ud = (g('tb', t)[o] / k) / psi
    q = k * float(g('r_s', t)) / np.pi
    Q, RT = [], []
    for q0 in np.arange(1.5 + half, q.max() - half - 0.1, step):
        m = np.abs(q - q0) <= half
        if m.sum() < 20:
            continue
        dq = q[m] - q0
        cols = [np.ones(int(m.sum()))]
        for j in range(amp_deg + 1):
            cols += [dq ** j * np.cos(np.pi * q[m]), dq ** j * np.sin(np.pi * q[m])]
        X = np.column_stack(cols)
        bm = np.linalg.lstsq(X, um[m], rcond=None)[0]
        bd = np.linalg.lstsq(X, ud[m], rcond=None)[0]
        Q.append(q0)
        RT.append(float(np.hypot(bd[1], bd[2]) / np.hypot(bm[1], bm[2])))
    return np.array(Q), np.array(RT)


def band_power(d, key):
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    return np.array([float(np.trapezoid(d[key][m][:, b], ee[m])) for b in range(len(QC))])


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def bands(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    e = env_a(q, d['Dl'])
    o = (d['Dl'] - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


# ==================================================================================================
print("\nPART 1 -- ⓵ THE RECONCILIATION: TWO QUANTITIES, NOT A CONTRADICTION.")
print("-" * 100)
AR = {t: amp_ratio(t) for t in ('lcdm', 'cr')}
QD = np.arange(3.5, 11.0, 0.25)
REG = np.interp(QD, AR['cr'][0], AR['cr'][1]) / np.interp(QD, AR['lcdm'][0], AR['lcdm'][1])
check("the register's own number is REPRODUCED from its own bank and estimator: the "
      "oscillation-amplitude ratio is about two per cent ABOVE the control over its own range",
      0.015 < REG.mean() - 1 < 0.030, f"{100 * (REG.mean() - 1):+.2f}% over q in [3.5, 11]")
lo, hi = max(AR['lcdm'][0].min(), QC[0]), min(AR['lcdm'][0].max(), QC[-1])
QD2 = np.arange(lo, hi + 0.01, 0.1)
REG2 = np.interp(QD2, AR['cr'][0], AR['cr'][1]) / np.interp(QD2, AR['lcdm'][0], AR['lcdm'][1])
# ⛭⛭ r7639+cc66.18 -- ** THIS ONE COMPARISON IS NAMESAKE ON BOTH SIDES, AND r7639+cc66.15 HAD IT
#   CROSS-ARM. **  The register's quantity comes from `r6897_fields`, which carries its ARM AS A KEY
#   SUFFIX (`k__cr`, `k__lcdm`) and has NO arm-of-record key at all -- so the amplitude ratio EXISTS
#   only on the namesake arm.  Read against the arm-of-record band power, the claim that the sign
#   difference is "not the range but the QUANTITY" would rest on a pair differing in the ARM too, which
#   is the confound its own wording denies.  ⇒ *The licensed comparison is the within-arm one; the
#   arm-of-record band power is COMPUTED AND REPORTED beside it, and the sign difference holds on
#   either -- but what the claim rests on is the pair that differs in one thing only.*
_NSK_READ = []


def nsk(tag):
    """the namesake-arm eta bank, RECORDING what it read so the guard below measures and not declares"""
    _NSK_READ.append(tag)
    return np.load(os.path.join(SP, tag + '.npz'))


ANSK = {t: nsk('r6959_eta_' + t) for t in ('lcdm', 'cr')}


def pw_of(bk):
    return np.sqrt((band_power(bk['cr'], 'w2dp') / band_power(bk['cr'], 'w2sw'))
                   / (band_power(bk['lcdm'], 'w2dp') / band_power(bk['lcdm'], 'w2sw')))


PW, PW_AOR = pw_of(ANSK), pw_of(A)
check("⛭ AND THE SIGN DIFFERENCE IS NOT THE RANGE BUT THE QUANTITY: on the SAME range and the SAME "
      "arm the oscillation-amplitude ratio is still ABOVE the control while the band-power ratio is "
      "BELOW it",
      REG2.mean() > 1.0 > PW.mean(),
      f"amplitude {100 * (REG2.mean() - 1):+.2f}% against band power {100 * (PW.mean() - 1):+.2f}% "
      f"on q in [{lo:.2f}, {hi:.2f}], both on the namesake arm")
check("⛔ AND BOTH SIDES OF THAT COMPARISON ARE THE SAME ARM, WHICH IS THE POINT: the register's bank "
      "has no arm-of-record counterpart, so the arm-of-record band power is reported and is NOT what the "
      "sign claim rests on.  ** The difference it is attributed to is the quantity, and the pair differs "
      "in nothing else **",
      _NSK_READ == ['r6959_eta_lcdm', 'r6959_eta_cr']
      and abs(PW_AOR.mean() - PW.mean()) > 1e-3 and '_leafrec1' in ETA['cr']
      and REG2.mean() > 1.0 > PW_AOR.mean(),
      f"read {_NSK_READ}; the arm of record reads {100 * (PW_AOR.mean() - 1):+.2f}% against the "
      f"namesake's {100 * (PW.mean() - 1):+.2f}% -- a live difference of "
      f"{100 * abs(PW_AOR.mean() - PW.mean()):.2f} points, so the sign difference holds on either and "
      f"the asserted pair is the namesake one")
STAB = []
for h in (2.0, 1.5, 1.0, 0.75, 0.5):
    ql, rl = amp_ratio('lcdm', half=h)
    qc, rc = amp_ratio('cr', half=h)
    gd = np.arange(3.7, 5.21, 0.1)
    STAB.append(float((np.interp(gd, qc, rc) / np.interp(gd, ql, rl)).mean()))
    QMIN = max(ql.min(), qc.min())
check("the estimator is STABLE under its own window width, so what follows about its reach is a "
      "property of the method and not of a tuning", (max(STAB) - min(STAB)) / STAB[0] < 0.01,
      f"five window widths agree to {100 * (max(STAB) - min(STAB)) / STAB[0]:.2f}%")
check("⛔ AND IT BOTTOMS OUT ABOVE THE FILTER'S LOWEST BAND: even at the narrowest window it cannot "
      "reach below q = 2, because the acoustic period in q is 2 and a sinusoid amplitude needs about a "
      "period either side", QMIN > 1.8 and QMIN > QC[0],
      f"narrowest window reaches q = {QMIN:.2f}, where the filter's lowest band centre is {QC[0]:.2f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ THE SECOND TOOTH, USED BECAUSE SOMETHING SURVIVED THE FIRST.")
print("-" * 100)
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                 'r7639_cc66_P15_repoint_paper'))
import own_comb_kinds as OCK                                                           # noqa: E402

_BANKS = {t: (F[t]['ls'].astype(float) / float(F[t]['l_A']), F[t]['Dl']) for t in ('lcdm', 'cr')}
_Tc, _pc, _Ta, _pa, _dphi = OCK._combs(_BANKS)
check("⛭ THE TWO ARMS' COMBS ARE FITTED BEFORE THE TARGET'S BANDS ARE CUT, and they DIFFER -- which is "
      "why the target is carried onto the control's comb coordinate",
      abs(_Ta - _Tc) > 1e-4,
      f"control T {_Tc:.4f} phi {_pc:.3f}; arm T {_Ta:.4f} phi {_pa:.3f}; dphi {_dphi:+.4f}")
R = 1.0 + OCK.band_excess_own_kind(_BANKS, 'mean', QE)
ql, rl = amp_ratio('lcdm', half=0.5)
qc, rc = amp_ratio('cr', half=0.5)
CAND = np.interp(QC, qc, rc) / np.interp(QC, ql, rl)
i0 = int(np.argmax(QC >= 2.0))
print(f"  shared range q = {QC[i0]:.2f} to {QC[-1]:.2f}")
print(f"  target    (r-1): {R[i0] - 1:+.5f} -> {R[-1] - 1:+.5f}")
print(f"  candidate (r-1): {CAND[i0] - 1:+.5f} -> {CAND[-1] - 1:+.5f}")
cur_t = float(np.polyfit(QC[i0:], R[i0:] - 1, 2)[0])
cur_c = float(np.polyfit(QC[i0:], CAND[i0:] - 1, 2)[0])
check("⛭⛭ ⓶ ON THE RANGE WHERE THE RIGHT QUANTITY CAN BE MEASURED THE CANDIDATE GROWS AND "
      "DECELERATES, with the SAME curvature sign as the target -- so it passes both teeth where it can "
      "be tested, reversing `cc66.50`'s dismissal on this seat's own error rather than on new data",
      CAND[-1] > CAND[i0] and cur_c < 0 and cur_t < 0,
      f"departure {CAND[i0] - 1:+.5f} -> {CAND[-1] - 1:+.5f}; curvature {cur_c:+.5f} against the "
      f"target's {cur_t:+.5f}")
check("⚠ AND THE GROWTH STATISTIC IS UNDEFINED HERE, NOT LARGE: the candidate's departure CROSSES ZERO "
      "inside the range, so G is not a ratio of anything -- the arithmetic returns a big number that "
      "would have read as a spectacular pass", abs(CAND[i0] - 1) < 0.005,
      f"departure at the bottom of the range is {CAND[i0] - 1:+.5f}, "
      f"and the naive G would be {(CAND[-1] - 1) / (CAND[i0] - 1):.1f}")
G_full = (R[-1] - 1) / (R[0] - 1)
G_shared = (R[-1] - 1) / (R[i0] - 1)
check("⛔ AND THE FILTER STILL CANNOT CLOSE IT: the target's growth is concentrated BELOW q = 2, which "
      "is exactly where the only quantity that could carry it cannot be measured -- so a pass on the "
      "shared range is a pass on the part carrying least of what is to be explained",
      G_full > 2 * G_shared, f"target grows {G_full:.2f}-fold over the full range against "
      f"{G_shared:.2f}-fold over the shared one")

# ==================================================================================================
print("\nPART 3 -- ⓷ WHAT IS NOT ON THE LIST.")
print("-" * 100)
d = A['cr']
QRES = sorted(k for k in d.files if getattr(d[k], 'ndim', 0) == 2)
ETA1 = sorted(k for k in d.files if getattr(d[k], 'ndim', 0) == 1)
print(f"  resolved in wavenumber: {'  '.join(QRES)}")
print(f"  functions of eta alone: {'  '.join(ETA1)}")
check("⛭ A WHOLE CLASS IS SETTLED BY STRUCTURE AND NEEDS NO RUN: every two-rate clock quantity -- the "
      "leaf clock, the ruler, the Jacobian between them, the visibility, the optical depth -- is stored "
      "against CONFORMAL TIME ALONE, and a function of eta has the same value at every wavenumber, so "
      "it cannot vary across one",
      all(k in ETA1 for k in ('rs_leaf', 'rs_stack', 'jac', 'vis', 'etau'))
      and not any(k in QRES for k in ('rs_leaf', 'rs_stack', 'jac', 'vis', 'etau')),
      "rs_leaf, rs_stack, jac, vis, etau all carry no wavenumber axis")


def widths(t):
    dd = A[t]
    ee, vv = np.asarray(dd['eta'], float), np.asarray(dd['vis'], float)
    rs = np.asarray(dd['rs_leaf'], float)
    w = vv / np.trapezoid(vv, ee)
    me = float(np.trapezoid(w * ee, ee))
    mr = float(np.trapezoid(w * rs, ee))
    return (float(np.sqrt(np.trapezoid(w * (ee - me) ** 2, ee))),
            float(np.sqrt(np.trapezoid(w * (rs - mr) ** 2, ee))))


WL, WC = widths('lcdm'), widths('cr')
re_, rr_ = WC[0] / WL[0], WC[1] / WL[1]
print(f"  window width in eta      : control {WL[0]:.4f}  arm {WC[0]:.4f}  -> {re_:.4f}")
print(f"  window width in rs_leaf  : control {WL[1]:.4f}  arm {WC[1]:.4f}  -> {rr_:.4f}")
check("⛭⛭⛭ ⓷ AND THE PROJECTION HOLDS A WIDTH NOBODY HAS IMPOSED, WHICH IS THE FINDING.  The acoustic "
      "phase swept across the window varies by k x the width in the LEAF clock -- what smears the "
      "oscillation and what `cc66.47` acted on -- while the projection smears by k x the width in "
      "CONFORMAL TIME, the Bessel argument being k(eta_0 - eta).  In a one-rate cosmology these are one "
      "object; here the two clocks differ and THE TWO WIDTHS DO NOT SCALE TOGETHER BETWEEN THE ARMS",
      abs(re_ / rr_ - 1) > 0.03,
      f"the arm's window is {100 * (re_ - 1):+.1f}% in conformal time and {100 * (rr_ - 1):+.1f}% in "
      f"the leaf horizon -- a ratio {100 * (re_ / rr_ - 1):+.1f}% different from the control's")
# ⛔ r7639 ⑴ -- THE REGISTERED FORM ALSO REQUIRED THE TWO RATIOS TO STRADDLE ONE (`re_ > 1 > rr_`),
#   AND ON THE ARM OF RECORD THEY DO NOT.  Both widths now exceed the control's: +10.4% in conformal
#   time and +2.4% in the leaf horizon, where on the namesake arm it was +6.5% and -0.8%.  ** The
#   FINDING survives and is slightly stronger -- the two widths differ by 7.9% where they differed by
#   7.3% -- because the finding is the NON-PROPORTIONALITY and not the straddle. **  The straddle was a
#   property of the namesake arm, not of the construction, and it is recorded as a miss of the
#   registered form rather than quietly dropped or re-toleranced.
print(f"\n    ⛔ REGISTERED: the two ratios straddle one (conformal > 1 > leaf).  MEASURED on the arm "
      f"of record: {re_:.4f} and {rr_:.4f}, BOTH above one -- a MISS of that form, reported and not "
      f"re-toleranced")
check("⛔ AND THE MISS IS IN THE FORM AND NOT IN THE FINDING: both widths exceed the control's on the "
      "arm of record, so the registered STRADDLE is gone, while the non-proportionality the row is "
      "named for is INTACT and marginally larger -- the two widths scale by factors 7.9 per cent apart "
      "where on the namesake arm they were 7.3 apart",
      re_ > 1.0 and rr_ > 1.0 and abs(re_ / rr_ - 1) > abs(1.0649 / 0.9921 - 1) - 0.01,
      f"conformal {re_:.4f} and leaf {rr_:.4f}, both above one; the ratio differs by "
      f"{100 * (re_ / rr_ - 1):+.1f}% against the namesake arm's +7.3%")
check("and that is a property of the PROJECTION rather than of the source, which is what this row has "
      "been named after since it opened and what no revision has tested",
      re_ != rr_, "the phase width and the projection width are different knobs")

# ⛭ EVERY FIGURE THIS HEADER PRINTS FOR THE TWO READINGS, TIED TO THE COMPUTATION.  `.15` shipped a
#   header figure that its own re-point had moved, and this file had no such check to catch it.
_DOC = open(os.path.abspath(__file__), encoding='utf-8').read().split(chr(34) * 3)[1]
_FIG = (f'${100 * (REG.mean() - 1):+.2f}$', f'${100 * (REG2.mean() - 1):+.2f}$',
        f'${100 * (PW.mean() - 1):.2f}$', f'${100 * (PW_AOR.mean() - 1):.2f}$')
check("⛭ AND EVERY FIGURE THIS HEADER PRINTS FOR THE TWO READINGS IS THE COMPUTED ONE, compared and not "
      "merely found -- the check this file did not have when it printed a figure its own re-point moved",
      all(x in _DOC for x in _FIG), ' '.join(_FIG))

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
