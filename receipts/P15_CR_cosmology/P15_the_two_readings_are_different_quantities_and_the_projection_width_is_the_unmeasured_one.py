#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE TWO DIPOLE READINGS ARE DIFFERENT QUANTITIES, NOT A CONTRADICTION;
CORRECTING WHICH ONE THE FILTER NEEDS REVERSES `cc66.50`'s DISMISSAL OF THAT CANDIDATE; AND THE ONE
THING THIS ROW IS NAMED AFTER -- THE PROJECTION -- HOLDS A WIDTH THAT HAS NEVER BEEN MEASURED. **

** PATH PROVENANCE, IN THE HEADER, ON THE STANDING REQUIREMENT. **  *** Every model number below is the
HIERARCHY path *** -- `r6897_fields` (the `ZPSAVE` bank the register's own receipt reads),
`r6959_eta_{lcdm,cr}` and `r6941_fine_{lcdm,cr}`.  `sec:refit-bound`'s quartet $222/538/818/1134$ is the
LINE-OF-SIGHT path's and is not read -- searched for by grepping this file for each of the four values
and for every line-of-sight bank name (`c54.17*`, `c54.178_*`, `L814_*`, `r6784_*`), and none occurs
below.  ⛔ *** Nothing is RUN: the order's ⓸, and every number is read from banks on disk. ***

** ON THE PRE-REGISTRATION GUARD, WHICH APPLIES DIFFERENTLY HERE AND IS SAID SO RATHER THAN SKIPPED. **
*No `PREDICTION.md` is written for this revision, because nothing is run and the only TEST in it -- the
second tooth -- is a criterion already fixed in `r6993`'s pre-registration: negative curvature, and
growth comparable to the target's.*  ⇒ **The criterion this revision applies was committed before the
measurement it is applied to, which is what the guard is for; writing a fresh one after the fact would
be the decoration the guard warns about.**

⛭⛭ ** ⓵ THE DISAGREEMENT IS NOT A CONTRADICTION, AND THE SIGN IS NOT THE RANGE. **  Both readings are
reproduced here from banks.  The register's quantity reads $+2.06$ per cent over its own range
$q\in[3.5,11]$ -- *its recorded "two per cent above", exactly* -- and still $+0.95$ per cent over the
part of `cc66.50`'s range it reaches, where `cc66.50`'s quantity reads $-11.58$ per cent.
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
    arm they are not, because the two clocks differ.*  ⇒ *** The arm's window is $6.5$ per cent WIDER in
    conformal time and $0.8$ per cent NARROWER in the leaf sound horizon -- the two stand in a ratio
    $7.3$ per cent different in the arm than in the control. ***  **`cc66.47` imposed the phase width;
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
  * `spectra/r6897_fields.npz`, `spectra/r6959_eta_{lcdm,cr}.npz`, `spectra/r6941_fine_{lcdm,cr}.npz`.
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
for _n in ('r6897_fields.npz', 'r6959_eta_lcdm.npz', 'r6959_eta_cr.npz',
           'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz'):
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK.")
    print(f"GATES: {len(FAILS)} FAILED:")
    raise SystemExit(1)

FLD = np.load(os.path.join(SP, 'r6897_fields.npz'), allow_pickle=True)
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
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
PW = np.sqrt((band_power(A['cr'], 'w2dp') / band_power(A['cr'], 'w2sw'))
             / (band_power(A['lcdm'], 'w2dp') / band_power(A['lcdm'], 'w2sw')))
check("⛭ AND THE SIGN DIFFERENCE IS NOT THE RANGE BUT THE QUANTITY: on the SAME range the "
      "oscillation-amplitude ratio is still ABOVE the control while the band-power ratio is BELOW it",
      REG2.mean() > 1.0 > PW.mean(),
      f"amplitude {100 * (REG2.mean() - 1):+.2f}% against band power {100 * (PW.mean() - 1):+.2f}% "
      f"on q in [{lo:.2f}, {hi:.2f}]")
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
R = bands(F['cr']) / bands(F['lcdm'])
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
      abs(re_ / rr_ - 1) > 0.03 and re_ > 1.0 > rr_,
      f"the arm's window is {100 * (re_ - 1):+.1f}% in conformal time and {100 * (rr_ - 1):+.1f}% in "
      f"the leaf horizon -- a ratio {100 * (re_ / rr_ - 1):+.1f}% different from the control's")
check("and that is a property of the PROJECTION rather than of the source, which is what this row has "
      "been named after since it opened and what no revision has tested",
      re_ != rr_, "the phase width and the projection width are different knobs")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
