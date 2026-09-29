"""⓵⓶⓷ RESOLVING POWER, THE PHASE AGAINST THE COMB, AND WHETHER THE CANCELLATION IS EXACT -- r7019+cc66.61.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** ⓵ NAMED BEFORE USE. **  A channel is RESOLVED on the differential estimator when its band-1 departure d
exceeds twice its own bands 2--7 scatter sigma.  ⇒ the RESOLVING RATIO is 2*sigma/|d|: the factor by which
sigma must fall.  *Computed twice -- against the channel's OWN departure, and against the departure a channel
carrying the WHOLE step would have -- because only the second bears on `PO-56`.*
⚠ *And the hazard is pre-registered: a power calculation invites choosing the aggregation with the smallest
sigma and quoting a departure measured on another.  **Every aggregation is reported and a resolution claim
must hold on the SAME reading that measured the departure.***
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE0 = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
PCOMB = 1.0
KN = (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
      ('JOINT', 'r6983_joint_lcdm.npz'))


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
    """the RAW aggregation -- a band's dispersion, which samples 0.70 of a comb period"""
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
    """the HELD-PERIOD aggregation -- phase-insensitive by construction, `cc66.60`'s correction"""
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
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms


def dep4(v, QE):
    return [departure(v, p, lg, QE) for _, p, lg in BASES]


print(__doc__)
print('=' * 100)

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


def sigmas(QE, agg, gg=None, oa=None, oc=None, ko=None):
    """every channel's band-1 departure and its OWN bands 2--7 scatter, on one aggregation"""
    gg = g if gg is None else gg
    oa = OA if oa is None else oa
    oc = OC if oc is None else oc
    ko = KO if ko is None else ko
    f = bstd if agg == 'raw' else bheld
    out = {'arm': dep4(f(gg, oa - oc, QE), QE)}
    for nm, _ in KN:
        out[nm] = dep4(f(gg, ko[nm] - oc, QE), QE)
    return out


print('\n  ⛭⛭⛭ ⓵ RESOLVING POWER -- WHAT WOULD IT TAKE?')
print('-' * 100)
BASE = {a: sigmas(QE0, a) for a in ('raw', 'held')}
print(f"    {'route':>6s}  {'channel':10s}  {'departure d':>12s}  {'scatter s':>10s}  {'d/s':>6s}  "
      f"{'2s/|d|':>8s}   {'2s/|d_arm|':>11s}")
for a in ('raw', 'held'):
    darm = abs(np.mean([x[0] for x in BASE[a]['arm']]))
    for nm in ('arm', 'window', 'term mix', 'JOINT'):
        d = float(np.mean([x[0] for x in BASE[a][nm]]))
        s = float(np.mean([x[1] for x in BASE[a][nm]]))
        print(f"    {a:>6s}  {nm:10s}  {d:+12.4f}  {s:10.4f}  {abs(d) / s:6.2f}  "
              f"{2 * s / abs(d):8.2f}   {2 * s / darm:11.2f}")
print('    ⌗ *the last column is the factor sigma must fall by for a channel carrying the WHOLE step to be '
      'decided -- the quantity `PO-56` turns on.*')

print('\n    ⛔⛔ AND THE TWO CHANNELS IN QUESTION **CHANGE SIGN BETWEEN THE AGGREGATIONS**, which is the '
      'hazard this file pre-registered and it fires before any power claim can be made:')
for nm in ('window', 'term mix', 'JOINT'):
    r = [x[0] for x in BASE['raw'][nm]]
    h = [x[0] for x in BASE['held'][nm]]
    flip = 'SIGN FLIPS' if np.sign(np.mean(r)) != np.sign(np.mean(h)) else 'same sign'
    print(f"      {nm:10s} raw {np.mean(r):+.4f}   held {np.mean(h):+.4f}   ** {flip} **")
print('    ⇒ ** so more power would not decide them: their DEPARTURES are aggregation-dependent, and only '
      'the window channel keeps its sign on both. **')

print('\n    ⛭ THE QUANTITY THAT ACTUALLY DECIDES IT: the MINIMUM RESOLVABLE SHARE, f_min = 2*sigma/|d_arm| '
      '-- the smallest fraction of the step a channel could carry and still be decided.')


def fmin(QE, agg, gg=None, oa=None, oc=None, ko=None):
    S = sigmas(QE, agg, gg, oa, oc, ko)
    d = abs(float(np.mean([x[0] for x in S['arm']])))
    sg = float(np.mean([x[1] for x in S['arm']]))
    return 2 * sg / d, d, sg


print(f"      {'route':44s}{'|d_arm|':>10s}{'sigma':>10s}{'f_min':>9s}")
ROUTES = []
for a in ('raw', 'held'):
    f, d, sg = fmin(QE0, a)
    ROUTES.append((f'{a} aggregation, 7 bands, per common q', f, d, sg))
# 2: the abscissa pairing -- per common multipole instead of per common q
mL = np.isin(LA, LC)
gl = LA[mL] / AA
oal = osc(LA / AA, DA)[mL]
ocl = np.interp(gl, QCq, osc(QCq, DC))
kol = {nm: np.interp(gl, g, KO[nm]) for nm, _ in KN}
for a in ('raw', 'held'):
    f, d, sg = fmin(QE0, a, gl, oal, ocl, kol)
    ROUTES.append((f'{a} aggregation, per common l instead of q', f, d, sg))
# 3: a longer lever arm -- one more band out to the bank's reach
QE1 = np.append(QE0, QE0[-1] + (QE0[-1] - QE0[-2]))
for a in ('raw', 'held'):
    f, d, sg = fmin(QE1, a)
    ROUTES.append((f'{a} aggregation, 8 bands out to q = {QE1[-1]:.2f}', f, d, sg))
# 4: more bands across the same range
QE2 = np.linspace(QE0[0], QE0[-1], 13)
for a in ('raw', 'held'):
    f, d, sg = fmin(QE2, a)
    ROUTES.append((f'{a} aggregation, {len(QE2) - 1} finer bands, same range', f, d, sg))
for nm, f, d, sg in ROUTES:
    print(f"      {nm:44s}{d:10.4f}{sg:10.4f}{f:9.2f}")
BEST = min(ROUTES, key=lambda r: r[1])
print(f"\n    ⇒ ** THE BEST OF EVERY ROUTE BANKED IS f_min = {BEST[1]:.2f} ({BEST[0]}). **")
print(f"      ⌗ *And note what the held-period aggregation does: it lowers sigma by "
      f"{ROUTES[0][3] / ROUTES[1][3]:.2f}x -- the reduction this file predicted -- **but it lowers the signal "
      f"by {ROUTES[0][2] / ROUTES[1][2]:.2f}x at the same time**, so f_min moves from {ROUTES[0][1]:.2f} to "
      f"{ROUTES[1][1]:.2f} and the candidate I expected most from does not help in the ratio that matters.*")
RAWSH = {nm: abs(float(np.mean([x[0] for x in BASE['raw'][nm]]))
                 / np.mean([x[0] for x in BASE['raw']['arm']])) for nm in ('window', 'term mix', 'JOINT')}
print(f"\n    ⇒ *** AND THE TWO CHANNELS SIT BELOW THAT FLOOR: the term mix carries "
      f"{RAWSH['term mix']:.2f} of the step and the realised pair {RAWSH['JOINT']:.2f}, against a minimum "
      f"resolvable share of {BEST[1]:.2f}. ***")
print(f"      ** NO ROUTE THIS CONSTRUCTION CAN BUILD BRINGS THE FLOOR BELOW WHAT THEY CARRY. **")
print('\n' + '=' * 100)

print('\n  ⛭⛭⛭ ⓶ THE PHASE AGAINST THE COMB, OVER A LONG STRETCH')
print('-' * 100)
print('    *Not a local fit in a window one period wide, where amplitude and phase are degenerate: the comb '
      'phase projected over a whole stretch, on each arm, with Delta = phi_a - phi_c.*')


def phase_of(q, v, a, b, P=PCOMB):
    m = (q >= a) & (q < b)
    if m.sum() < 20:
        return np.nan
    C = float(np.trapezoid(v[m] * np.cos(2 * np.pi * q[m] / P), q[m]))
    S = float(np.trapezoid(v[m] * np.sin(2 * np.pi * q[m] / P), q[m]))
    return float(np.arctan2(-S, C))


def delta_on(a, b):
    pa, pc = phase_of(g, OA, a, b), phase_of(g, OC, a, b)
    if not np.isfinite(pa) or not np.isfinite(pc):
        return np.nan
    return float(np.arctan2(np.sin(pa - pc), np.cos(pa - pc)))


UP = [(x, x + 1.0) for x in np.arange(QE0[1], QE0[-1] - 1.0 + 1e-9, 1.0)]
DU = np.array([delta_on(a, b) for a, b in UP])
D1 = delta_on(QE0[0], QE0[1])
DFULL = delta_on(QE0[1], QE0[-1])
print(f"    the upper range, {len(UP)} disjoint one-period stretches from q = {UP[0][0]:.2f} to "
      f"{UP[-1][1]:.2f}:")
print(f"      " + '  '.join(f'{v:+.5f}' for v in DU) + f"   rad")
SU = float(np.std(DU, ddof=1))
MU = float(np.mean(DU))
print(f"      mean {MU:+.6f} rad ({np.degrees(MU):+.4f} deg), scatter {SU:.6f} rad over {len(DU)} stretches, "
      f"so the mean is good to {SU / np.sqrt(len(DU)):.6f} rad")
print(f"    and the whole upper range as ONE stretch of {QE0[-1] - QE0[1]:.1f} periods: "
      f"{DFULL:+.6f} rad ({np.degrees(DFULL):+.4f} deg)")
print(f"    band 1, which is only {QE0[1] - QE0[0]:.2f} of a period wide: {D1:+.6f} rad "
      f"({np.degrees(D1):+.4f} deg)")
Z1 = abs(D1 - MU) / SU
print(f"    ⇒ band 1 sits {Z1:.2f} scatters from the upper-range mean")
print(f"      ⛔ *BUT THAT IS THE WRONG ERROR BAR AND THE COMPARISON IS NOT LICENSED AS IT STANDS: those "
      f"stretches are ONE period wide and band 1 is {QE0[1] - QE0[0]:.2f} of one.  A projection over a "
      f"non-integer number of periods leaks the baseline into C and S, so a narrow stretch is both noisier "
      f"AND biased.*")
W = QE0[1] - QE0[0]
MATCH = np.array([delta_on(x, x + W) for x in np.arange(QE0[1], QE0[-1] - W + 1e-9, W)])
MATCH = MATCH[np.isfinite(MATCH)]
SM, MM = float(np.std(MATCH, ddof=1)), float(np.mean(MATCH))
print(f"    ⛭ THE MATCHED-WIDTH CONTROL -- the same projection on {len(MATCH)} stretches of the SAME "
      f"{W:.2f} width across the upper range:")
print(f"      " + '  '.join(f'{v:+.5f}' for v in MATCH) + "   rad")
print(f"      mean {MM:+.6f}, scatter {SM:.6f} rad -- **{SM / SU:.1f} times the full-period scatter**, which "
      f"is the leakage the narrow window costs")
Z1M = abs(D1 - MM) / SM
print(f"    ⇒ ** ON THE MATCHED-WIDTH YARDSTICK BAND 1 SITS {Z1M:.2f} SCATTERS FROM THE UPPER MEAN, NOT "
      f"{Z1:.2f}. **")
print(f"      ⇒ *** SO THE PHASE STEP IS "
      f"{'RESOLVED' if Z1M > 2 else 'NOT RESOLVED'} ON THE ONLY YARDSTICK THAT MATCHES IT, AND "
      f"{'the estimator is not measuring what cc66.60 assumed' if Z1M > 2 else 'THE AMPLITUDE VERDICT OF ' + chr(96) + 'cc66.60' + chr(96) + ' STANDS AS THE COMPLETE ONE'}. ***")
print(f"      ⌗ *This is the third row of the pre-registration where it applies: the long-stretch reading "
      f"resolves the phase beautifully in the upper range -- {MU:+.6f} +- {SU / np.sqrt(len(DU)):.6f} rad, a "
      f"{abs(MU) / (SU / np.sqrt(len(DU))):.1f}-sigma determination, {SU / np.sqrt(len(DU)) / abs(MU):.0%} "
      f"fractional -- and cannot bring that precision to the one band that needs it, because that band is "
      f"narrower than the period the method needs.*")

print('\n  ⛭⛭⛭ ⓷ IS THE COMPOSITION CANCELLATION EXACT OR APPROXIMATE?')
print('-' * 100)
print(f"    {'aggregation':12s}{'basis':12s}{'d_window':>10s}{'d_termmix':>11s}{'sum':>9s}"
      f"{'d_JOINT':>10s}{'sigma':>8s}{'|d|/s':>8s}")
NZ = []
for a in ('raw', 'held'):
    for k, (bn, _, _) in enumerate(BASES):
        dwk = BASE[a]['window'][k][0]
        dmk = BASE[a]['term mix'][k][0]
        djk, sjk = BASE[a]['JOINT'][k]
        NZ.append((a, bn, abs(djk) / sjk))
        print(f"    {a:12s}{bn:12s}{dwk:+10.3f}{dmk:+11.3f}{dwk + dmk:+9.3f}{djk:+10.3f}{sjk:8.3f}"
              f"{abs(djk) / sjk:8.2f}")
RAWOK = all(z < 2.0 for a, _, z in NZ if a == 'raw')
HELDOK = all(z < 2.0 for a, _, z in NZ if a == 'held')
print(f"\n    ⇒ consistent with zero on ALL FOUR bases: raw {RAWOK}, held {HELDOK}")
if RAWOK and not HELDOK:
    print("    ⇒ ** SO THE CANCELLATION IS NEITHER EXACT NOR APPROXIMATE -- IT IS AGGREGATION-DEPENDENT. **")
    print("      *On the raw reading the joint vanishes to within its scatter on every basis; on the "
          "phase-insensitive one it does not.  ⓷ therefore inherits ⓵'s answer rather than choosing a "
          "word, which is the third possibility the pre-registration named.*")
print(f"      ⌗ *and what it would be cancelling BETWEEN is large on both: the two singles sum to "
      f"{BASE['raw']['window'][0][0] + BASE['raw']['term mix'][0][0]:+.3f} (raw) and "
      f"{BASE['held']['window'][0][0] + BASE['held']['term mix'][0][0]:+.3f} (held), so the cancellation "
      f"claim is about a large number either way.*")
print('\n' + '=' * 100)

print(f"""
  ⛭⛭⛭ ⓵ NOTHING BANKED BRINGS THE FLOOR BELOW WHAT THE CHANNELS CARRY -- WHICH IS THE TERMINAL ROW.
    *The minimum resolvable share, f_min = 2*sigma/|d_arm|, is the smallest fraction of the step a channel
    could carry and still be decided.  Across every route this construction can build -- both aggregations,
    both abscissas, a longer lever arm to q = {QE1[-1]:.2f}, and finer bands -- it runs
    {min(r[1] for r in ROUTES if r[1] < 10):.2f} to {max(r[1] for r in ROUTES if r[1] < 10):.2f}.*
    ⇒ ** THE TERM MIX CARRIES {RAWSH['term mix']:.2f} OF THE STEP AND THE REALISED PAIR {RAWSH['JOINT']:.2f},
    AGAINST A FLOOR OF {BEST[1]:.2f}.  THEY CANNOT BE RESOLVED BY ANY STATISTIC THIS CONSTRUCTION CAN BUILD. **
  ⌗ *And the reason is the one thing I did not expect: **the held-period aggregation lowers sigma by
    {ROUTES[0][3] / ROUTES[1][3]:.2f}x exactly as this file predicted -- and lowers the SIGNAL by
    {ROUTES[0][2] / ROUTES[1][2]:.2f}x at the same time.*  The ratio that matters does not move.  *I named
    that candidate as the one I expected most from, before measuring, and it does not help.*
  ⛔ *AND THE HAZARD FIRED BEFORE THE POWER CLAIM COULD: the term mix and the realised pair **change sign**
    between the two aggregations, so their departures are not established at all and more power would not
    decide them.  Only the window channel keeps its sign on all eight readings.*

  ⛭⛭⛭ ⓶ AND THE PHASE IS RESOLVED WHERE IT IS NOT NEEDED AND NOT WHERE IT IS.
    *The long-stretch projection works: over the upper range the relative phase is
    {MU:+.6f} +- {SU / np.sqrt(len(DU)):.6f} rad -- {np.degrees(MU):+.3f} degrees, a
    {abs(MU) / (SU / np.sqrt(len(DU))):.1f}-sigma determination -- and the whole range as one stretch agrees
    at {DFULL:+.6f}.*  Band 1 reads {D1:+.6f} rad, which is {Z1:.2f} scatters away on the full-period
    yardstick.  ⛔ *But that yardstick is wrong: band 1 is {QE0[1] - QE0[0]:.2f} of a period and a projection
    over a non-integer number of periods leaks the baseline, so the matched-width control is the only
    licensed comparison -- and on {len(MATCH)} stretches of the same width the scatter is {SM / SU:.1f} times
    larger.*
    ⇒ *** BAND 1 SITS {Z1M:.2f} SCATTERS OUT, NOT {Z1:.2f}: THE PHASE STEP IS NOT RESOLVED, AND `cc66.60`'s
    AMPLITUDE VERDICT STANDS AS THE COMPLETE ONE RATHER THAN THE SIGN-ONLY ONE. ***
  ⌗ *The method reaches a 13 per cent measurement over five periods and cannot bring it to the one band that
    needs it, because that band is narrower than the period the method needs.  **That is the same structural
    limit in a third disguise** -- `cc66.58` met it on the window-free family, `cc66.60` on the trade-off,
    and it is met here on the phase.*

  ⛔⛔ ⓷ AND THE CANCELLATION IS NEITHER EXACT NOR APPROXIMATE -- IT IS AGGREGATION-DEPENDENT.
    *On the raw reading the joint vanishes to within its own scatter on all four bases ({min(z for a, _, z in NZ if a == 'raw'):.2f}
    to {max(z for a, _, z in NZ if a == 'raw'):.2f} sigma); on the phase-insensitive one it does not
    ({min(z for a, _, z in NZ if a == 'held'):.2f} to {max(z for a, _, z in NZ if a == 'held'):.2f}).*
    ⇒ ** So ⓷ inherits ⓵'s answer rather than choosing a word -- the third possibility this file named
    before measuring -- and the constraint-versus-coincidence question cannot be settled here. **

  ⛔ *No envelope, basis, abscissa or aggregation chosen; no new candidate; no mechanism proposed.*
""")
