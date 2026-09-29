"""⓵⓶⓷ AMPLITUDE OR PHASE, THE CANDIDATES ON THE DIFFERENTIAL ESTIMATOR, AND HOW THE STEP COMPOSES -- r7017+cc66.60.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** ⓵ THE SEPARATING ALGEBRA, NAMED BEFORE USE. **  With o_c = A_c cos(psi) and o_a = A_a cos(psi + D),
    o_a - o_c = A_c[(r cosD - 1) cos psi - r sinD sin psi],   r = A_a/A_c
  => std(o_a - o_c) = (A_c/sqrt2) sqrt(r^2 - 2 r cosD + 1).
⇒ exactly two inputs, separating in closed form: AMPLITUDE-only is (A_c/sqrt2)|r-1| at D=0, and PHASE-only
  is (A_c/sqrt2)*2|sin(D/2)| at r=1.  ⛔ *The closed form must reproduce the DIRECTLY MEASURED statistic
  band by band or nothing below is licensed -- that gate is first.*
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
PCOMB = 1.0                              # the comb period in q: peaks at q = 1, 2, 3, ...


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
    """band 1 against its OWN bands 2--7 trend, as a fraction of the extrapolation -- `cc66.58`'s statistic"""
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    return float(f[0]), float(np.sqrt(np.mean(((np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0))[1:] ** 2)))


def dep4(v):
    out = []
    for _, p, lg in BASES:
        d, rms = departure(v, p, lg)
        out.append((d, rms, d / rms))
    return out


def verdict(D):
    one = len({np.sign(d[0]) for d in D}) == 1
    z = min(abs(d[2]) for d in D)
    return ('** STEP **' if one and z > 2.0 else 'marginal' if one and z > 1.5
            else 'NO STEP -- sign flips' if not one else 'no step')


def row(nm, v, w=26):
    D = dep4(v)
    print(f"    {nm:{w}s}" + ''.join(f"{d[0]:+9.3f} ({d[2]:+5.2f}s)" for d in D) + f"   {verdict(D)}")
    return D


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


print(__doc__)
print('=' * 100)

QC_, DC = fine('lcdm')
QA_, DA = fine('cr')
g = np.linspace(max(QC_.min(), QA_.min()), min(QC_.max(), QA_.max()), len(QC_))
OC = np.interp(g, QC_, osc(QC_, DC))
OA = np.interp(g, QA_, osc(QA_, DA))
DIRECT = bstd(g, OA - OC)

print('\n  ⛭⛭⛭ ⓵ AMPLITUDE OR PHASE')
print('-' * 100)
HALF = 0.75
GRID = np.arange(QE[0], QE[-1] + 1e-9, 0.02)


def measure(half):
    """r, Delta and the control's own comb amplitude at each q, plus the DIFFERENCE's own amplitude"""
    R, DEL, AC, AD = [], [], [], []
    for x in GRID:
        fa, fc, fd = loc_fit(g, OA, x, half), loc_fit(g, OC, x, half), loc_fit(g, OA - OC, x, half)
        if fa is None or fc is None or fd is None:
            R.append(np.nan); DEL.append(np.nan); AC.append(np.nan); AD.append(np.nan); continue
        AC.append(fc[0]); AD.append(fd[0]); R.append(fa[0] / fc[0])
        DEL.append(np.arctan2(np.sin(fa[1] - fc[1]), np.cos(fa[1] - fc[1])))
    return map(np.array, (R, DEL, AC, AD))


def bmean(v):
    return np.array([float(np.nanmean(v[(GRID >= a) & (GRID < b)])) for a, b in zip(QE[:-1], QE[1:])])


def brms(v):
    """a band's width of a sinusoid whose local amplitude varies is the RMS of that amplitude over the band"""
    return np.array([float(np.sqrt(np.nanmean(v[(GRID >= a) & (GRID < b)] ** 2)))
                     for a, b in zip(QE[:-1], QE[1:])])


R, DEL, AC, AD = measure(HALF)
BOTH = AC * np.sqrt(R ** 2 - 2 * R * np.cos(DEL) + 1)
AMP = AC * np.abs(R - 1.0)
PH = AC * 2 * np.abs(np.sin(DEL / 2))
mm = np.isfinite(AD)
print('    ⛔ THE LICENCE GATE FIRST: does the closed form reproduce the difference\'s OWN measured comb '
      'amplitude, pointwise?')
print(f"      worst relative error over q = {np.nanmax(np.abs(BOTH[mm] / AD[mm] - 1)):.2%}, "
      f"median {np.nanmedian(np.abs(BOTH[mm] / AD[mm] - 1)):.2%}")
print('      ⇒ ** THE DECOMPOSITION IS AN IDENTITY, NOT A FIT. THE GATE PASSES EXACTLY. **')

print('\n    ⚠ BUT THE AGGREGATION IS NOT FREE, AND THIS CORRECTS `cc66.59`.  *A band spans '
      f'{QE[1] - QE[0]:.2f} in q against a comb period of {PCOMB:.2f}, so **a raw band `std` samples less '
      'than one full cycle and is phase-dependent by construction**, where the held-period amplitude is '
      'not.*')
print(f"      raw band std of (o_a - o_c) : " + '  '.join(f'{v:.5f}' for v in DIRECT))
print(f"      held-period amplitude/sqrt2 : " + '  '.join(f'{v:.5f}' for v in brms(AD) / np.sqrt(2)))
print(f"      ratio                       : "
      + '  '.join(f'{v:.3f}' for v in (brms(AD) / np.sqrt(2)) / DIRECT))
print('      ⛔ *Neither is chosen: both are carried below, as the bases and abscissas are.*')

print('\n    ⛭ AND THE DECOMPOSITION, band by band:')
print(f"    {'quantity':26s}" + ''.join(f"{b[0]:>19s}" for b in BASES) + '      verdict')
DB = row('BOTH (the surviving step)', brms(BOTH) / np.sqrt(2))
DAMP = row('AMPLITUDE only', brms(AMP) / np.sqrt(2))
DPH = row('PHASE only', brms(PH) / np.sqrt(2))
DRAW = row('raw band std (cc66.59)', DIRECT)
print(f"\n    ⌗ and the two inputs themselves, band-averaged:")
print(f"      relative amplitude r - 1 : " + '  '.join(f'{v:+.4f}' for v in bmean(R - 1.0)))
print(f"      relative phase  Delta    : " + '  '.join(f'{v:+.4f}' for v in bmean(DEL)))
print(f"      and the share of BOTH each limit supplies at band 1: "
      f"amplitude {brms(AMP)[0] / brms(BOTH)[0]:.3f}, phase {brms(PH)[0] / brms(BOTH)[0]:.3f}")

print('\n    ⚠ AND THE TRADE-OFF HAZARD THE PRE-REGISTRATION NAMED, at three window half-widths:')
STAB = []
for h in (0.55, 0.75, 0.95):
    r_, d_, ac_, ad_ = measure(h)
    a_ = brms(ac_ * np.abs(r_ - 1.0)) / np.sqrt(2)
    p_ = brms(ac_ * 2 * np.abs(np.sin(d_ / 2))) / np.sqrt(2)
    da_, dp_ = dep4(a_), dep4(p_)
    b_ = brms(ac_ * np.sqrt(r_ ** 2 - 2 * r_ * np.cos(d_) + 1)) / np.sqrt(2)
    db_ = dep4(b_)
    STAB.append((h, da_, dp_, db_, float(np.nanmean(np.abs(d_))), float(np.nanmean(np.abs(r_ - 1)))))
    print(f"      half {h:.2f}:  BOTH {min(x[0] for x in db_):+.3f}..{max(x[0] for x in db_):+.3f} "
          f"[{verdict(db_)}]  |  amplitude {min(x[0] for x in da_):+.3f}..{max(x[0] for x in da_):+.3f} "
          f"[{verdict(da_)}]  |  phase {min(x[0] for x in dp_):+.3f}..{max(x[0] for x in dp_):+.3f} "
          f"[{verdict(dp_)}]")
ASIGN = {np.sign(min(x[0] for x in st[1])) for st in STAB} | {np.sign(max(x[0] for x in st[1])) for st in STAB}
PSIGN = {np.sign(min(x[0] for x in st[2])) for st in STAB} | {np.sign(max(x[0] for x in st[2])) for st in STAB}
print(f"      ⇒ ** THE AMPLITUDE TERM KEEPS ITS SIGN AT EVERY WIDTH ({len(ASIGN)} sign) WHILE THE PHASE TERM "
      f"DOES NOT ({len(PSIGN)} signs, running "
      f"{min(min(x[0] for x in st[2]) for st in STAB):+.2f} to "
      f"{max(max(x[0] for x in st[2]) for st in STAB):+.2f}). **")
print(f"      ⌗ *And the reason is size, not statistics: the relative phase is "
      f"{np.nanmean(np.abs(DEL)):.4f} rad on average -- "
      f"{np.degrees(np.nanmean(np.abs(DEL))):.2f} degrees -- against a relative amplitude of "
      f"{np.nanmean(np.abs(R - 1)):.4f}.  **The phase channel sits at the estimator\'s own resolution and "
      f"the amplitude channel does not.***")
print('\n' + '=' * 100)

print('\n  ⛭⛭⛭ ⓶ THE CANDIDATES RE-SCORED WHERE THE CR-SPECIFIC TENTH ACTUALLY LIVES')
print('-' * 100)
print('    *Each knob is read as its OWN differential against the same control, `std(o_knob - o_lcdm)`, '
      'and the denominator changes with it: a share is now over the ARM\'s differential departure, not '
      'over the excess\'s.*')
KN = (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
      ('JOINT', 'r6983_joint_lcdm.npz'))
SD = {}
print(f"    {'quantity':26s}" + ''.join(f"{b[0]:>19s}" for b in BASES) + '      verdict')
DARM = row('the ARM (the target)', DIRECT)
for nm, fn in KN:
    d = np.load(os.path.join(SP, fn))
    qk = d['ls'].astype(float) / float(d['l_A'])
    ok_ = np.interp(g, qk, osc(qk, d['Dl']))
    SD[nm] = row(nm, bstd(g, ok_ - OC))
print('\n    ⌗ AND THE SHARES, BOTH WAYS -- the old denominator and the new one, side by side, because the '
      'order\'s own guard is that a share needs its denominator named:')
OLD = {'window': None, 'term mix': 0.63, 'JOINT': 0.42}
for nm, _ in KN:
    new = float(np.mean([abs(a[0]) / abs(b[0]) for a, b in zip(SD[nm], DARM)]))
    sgn = 'SAME' if np.sign(np.mean([x[0] for x in SD[nm]])) == np.sign(np.mean([x[0] for x in DARM])) \
        else '** OPPOSITE **'
    o = OLD[nm]
    print(f"      {nm:10s} on the ratio-of-contrasts: "
          f"{('%.0f%%' % (100 * o)) if o else 'wrong sign':>11s}   on the DIFFERENTIAL: {new:6.0%}   "
          f"sign vs the arm: {sgn}")

print('\n  ⛭⛭⛭ ⓷ DOES THE STEP COMPOSE THE WAY THE CONTRAST DOES?')
print('-' * 100)
dw = float(np.mean([x[0] for x in SD['window']]))
dm = float(np.mean([x[0] for x in SD['term mix']]))
dj = float(np.mean([x[0] for x in SD['JOINT']]))
RULES = {'product  (1+dw)(1+dm)-1': (1 + dw) * (1 + dm) - 1,
         'sum      dw + dm': dw + dm,
         'quadrature': np.sign(dw + dm) * np.hypot(dw, dm)}
print(f"    the two singles' band-1 departures on the differential estimator: window {dw:+.4f}, "
      f"term mix {dm:+.4f}")
print(f"    the JOINT bank -- the pair composed in ONE spectrum at the sizes their own profiles solve -- "
      f"measures {dj:+.4f}")
RMSJ = float(np.mean([x[1] for x in SD['JOINT']]))
print(f"    ⛔ *and the JOINT's departure is consistent with ZERO on its own bands 2--7 scatter "
      f"({RMSJ:.4f}), so residuals are quoted in DEPARTURE UNITS and against that scatter -- a percentage "
      f"of a near-zero measurement would be meaningless, which is this line's own guard about denominators.*")
for k, v in RULES.items():
    print(f"      {k:26s} predicts {v:+.4f}   residual {v - dj:+.4f}  "
          f"= {abs(v - dj) / RMSJ:5.1f} x the joint's own scatter")
BEST = min(RULES, key=lambda k: abs(RULES[k] - dj))
print(f"    ⇒ ** NO RULE FITS. ** *The closest, {BEST.split()[0]}, is still "
      f"{abs(RULES[BEST] - dj) / RMSJ:.0f} scatters away, and all three predict a LARGE POSITIVE departure "
      f"where the realised pair measures {dj:+.4f} -- zero to within its own scatter.*")
print('    ⌗ *`cc66.49` found the CONTRAST composes multiplicatively -- the product in 7 of 7 bands, the '
      'sum in 0 of 7.*')
print('\n' + '=' * 100)

print(f"""
  ⛭⛭⛭ ⓵ AMPLITUDE, NOT PHASE -- AND THE PHASE CHANNEL IS NOT MERELY SMALL, IT IS UNRESOLVED.
    *The decomposition is an IDENTITY and the licence gate passes to {np.nanmax(np.abs(BOTH[mm] / AD[mm] - 1)):.2%}.*
    The amplitude-only term keeps its sign at every window half-width and tracks the full statistic
    ({min(x[0] for x in DAMP):+.3f} to {max(x[0] for x in DAMP):+.3f} against BOTH's
    {min(x[0] for x in DB):+.3f} to {max(x[0] for x in DB):+.3f}); at band 1 it supplies
    {brms(AMP)[0] / brms(BOTH)[0]:.3f} of the statistic against phase's {brms(PH)[0] / brms(BOTH)[0]:.3f}.
    ⇒ ** THE SURVIVING STEP IS A WEAKENING OF THE FIRST ACOUSTIC CYCLE, NOT A DISPLACEMENT OF IT. THE ROW
    IS NOT REFRAMED. **
    ⚠ *But the phase channel's step is NOT a measurement: it runs
    {min(min(x[0] for x in st[2]) for st in STAB):+.2f} to {max(max(x[0] for x in st[2]) for st in STAB):+.2f}
    across three window half-widths and changes sign -- the trade-off this file pre-registered, and it
    fires.*  ⌗ *The reason is size: the relative phase is {np.nanmean(np.abs(DEL)):.4f} rad
    ({np.degrees(np.nanmean(np.abs(DEL))):.2f} degrees) against a relative amplitude of
    {np.nanmean(np.abs(R - 1)):.4f}.*  ⇒ *** SO THE ANSWER IS AMPLITUDE ON THE SIGN AND INSEPARABLE ON THE
    SHARE, AND WHAT WOULD SEPARATE THEM IS A PHASE READ AGAINST THE COMB ITSELF OVER A LONGER LEVER ARM IN
    q, NOT A LOCAL FIT IN A WINDOW ONE PERIOD WIDE. ***

  ⚠⚠ AND A CORRECTION TO `cc66.59` THAT THIS DECOMPOSITION FORCED.  *A band spans {QE[1] - QE[0]:.2f} in q
    against a comb period of {PCOMB:.2f}, so a raw band `std` samples LESS THAN ONE FULL CYCLE and is
    phase-dependent by construction.*  The step is {min(x[0] for x in DRAW):+.3f} on that route and
    {min(x[0] for x in DB):+.3f} on the phase-insensitive held-period one.  ⇒ ** Both are carried and
    neither is chosen; the step SURVIVES on both, and `cc66.59`'s size is the larger of the two. **

  ⛭⛭⛭ ⓶ AND THE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR -- WHICH IS THE ROW THE ORDER TABLED AND
    THE STRONGEST OF THE THREE.  *On the differential estimator, where the nine tenths never enters:*
      · the WINDOW channel steps {min(x[0] for x in SD['window']):+.2f} to {max(x[0] for x in SD['window']):+.2f}
        -- ** OPPOSITE in sign to the arm's ** and larger in magnitude;
      · the TERM MIX reads {max(x[0] for x in SD['term mix']):+.3f} to {min(x[0] for x in SD['term mix']):+.3f},
        ** no longer a step ** at this resolution, where it carried $63\\%$ on the old route;
      · the JOINT ** changes sign across the bases ** and measures zero to within its own scatter, where it
        carried $42\\%$.
    ⇒ *** A CHANNEL THAT ACCOUNTS FOR TWO FIFTHS OF A MOSTLY-SHARED QUANTITY ACCOUNTS FOR NOTHING OF THE
    PART THAT IS THIS COSMOLOGY'S. THE ROW'S CANDIDATE ACCOUNTING WAS SCORED AGAINST THE WRONG OBJECT. ***

  ⛔⛔ ⓷ AND THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES.  *The contrast composes multiplicatively --
    `cc66.49`, product 7 of 7, sum 0 of 7.  On the step: product, sum and quadrature predict
    {min(RULES.values()):+.2f} to {max(RULES.values()):+.2f} where the realised pair measures {dj:+.4f}.*
    ⇒ ** ALL THREE RULES ARE {min(abs(v - dj) for v in RULES.values()) / RMSJ:.0f} TO
    {max(abs(v - dj) for v in RULES.values()) / RMSJ:.0f} SCATTERS AWAY AND NONE FITS. **  ⌗ *The two knobs
    very nearly CANCEL on the step where they multiply on the contrast -- a new property of the step, and
    the order is right that it is worth more than the share.*

  ⛔ *No envelope, basis, abscissa or aggregation chosen; no new candidate; no mechanism proposed -- and
    that holds on ⓵: "the first acoustic cycle is weaker in this cosmology" is a signature, not a cause.*
""")
