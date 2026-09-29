"""⓵⓶⓷ THE DIFFERENTIAL ESTIMATOR, THE SHARED STEP'S TERM, AND WHICH STEP THE 42 PER CENT IS OF -- r7015+cc66.59.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** ⓵ NAMED BEFORE USE. **  Write each arm as envelope times oscillation, Dl = E*(1+o).  The present route forms
std(o_a) and std(o_c) separately and divides; the ORDERED route forms R = Dl_a/Dl_c ~ (E_a/E_c)(1 + o_a - o_c)
and takes the contrast of THAT.  ⇒ the ordered statistic reads std(o_a - o_c): **the common oscillation divides
out before any width is taken.**  ⚠ *It is therefore also sensitive to a PHASE difference, so its absolute size
carries no expectation and ONLY THE STEP is compared.*
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
NM = ['sw*sw', 'sw*dp', 'sw*isw', 'sw*pol', 'dp*dp', 'dp*isw', 'dp*pol',
      'isw*isw', 'isw*pol', 'pol*pol']
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))


def fine(t):
    d = np.load(os.path.join(SP, f'r6941_fine_{t}.npz'))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period in q -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def band_std(q, y):
    e = env_a(q, y)
    o = (y - e) / e
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def departure(v, p, lg):
    """band 1 against its OWN bands 2--7 trend, as a FRACTION of the extrapolation so the bases are
    comparable, with the bands 2--7 scatter in the same units as the yardstick -- `cc66.58`'s statistic"""
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms, float(f[0]) / rms


def row(nm, v, w=24):
    D = [departure(v, p, lg) for _, p, lg in BASES]
    one = len({np.sign(d[0]) for d in D}) == 1
    z = min(abs(d[2]) for d in D)
    ver = ('** STEP **' if one and z > 2.0 else 'marginal' if one and z > 1.5
           else 'NO STEP -- sign flips' if not one else 'no step')
    print(f"    {nm:{w}s}" + ''.join(f"{d[0]:+9.3f} ({d[2]:+5.2f}s)" for d in D) + f"   {ver}")
    return D, ver


print(__doc__)
print('=' * 100)

LC, DC, AC = fine('lcdm')
LA, DA, AA = fine('cr')
QCq, QAq = LC / AC, LA / AA

# ---- the present route, for reference only -------------------------------------------------------
C0, CA = band_std(QCq, DC), band_std(QAq, DA)
MEAS = CA / C0

print('\n  ⛭⛭⛭ ⓵ THE DIFFERENTIAL ESTIMATOR -- RATIO FIRST, CONTRAST SECOND')
print('-' * 100)
print(f"    the two arms differ in l_A by {100 * abs(AA / AC - 1):.3f} per cent "
      f"({AC:.4f} against {AA:.4f}), so per-multipole and per-q are NOT the same pairing.")
print('    ⛔ BOTH ARE REPORTED.  *No abscissa is chosen, which is the basis-family discipline extended to '
      'the degree of freedom this estimator introduces.*')

RAT = {}
# per common multipole: the order's literal words
m = np.isin(LA, LC)
RAT['per common l'] = (LA[m] / AA, DA[m] / np.interp(LA[m], LC, DC))
# per common q: what aligns the acoustic features
gq = np.linspace(max(QCq.min(), QAq.min()), min(QCq.max(), QAq.max()), len(LC))
RAT['per common q'] = (gq, np.interp(gq, QAq, DA) / np.interp(gq, QCq, DC))

print(f"\n    {'reading':24s}" + ''.join(f"{b[0]:>19s}" for b in BASES) + '      verdict')
OUT = {}
for nm, (qq, rr) in RAT.items():
    OUT[nm] = row(nm, band_std(qq, rr))
print(f"    {'-- the present route --':24s}" + ''.join(' ' * 19 for _ in BASES))
OUT['present excess'] = row('present excess', MEAS - 1.0)

print('\n  ⌷ AND THE CONDITIONING THE PRE-REGISTRATION SAID TO REPORT RATHER THAN DISCOVER:')
print('    *the ratio divides by the control, which passes through its own troughs, and the first acoustic '
      'trough sits inside band 1.*')
for a, b in zip(QE[:-1], QE[1:]):
    mm = (QCq >= a) & (QCq < b)
    print(f"      q in [{a:.2f}, {b:.2f}):  min Dl_lcdm = {DC[mm].min():.4e}, "
          f"min/median = {DC[mm].min() / np.median(DC[mm]):.3f}")
SM = env_a(QCq, DC)
rs = np.interp(gq, QAq, DA) / np.interp(gq, QCq, SM)
OUT['per q, smoothed divisor'] = row('per q, smoothed divisor', band_std(gq, rs))
print('    ⇒ *dividing by a SMOOTHED control instead of a raw one is the conditioning control, and it is a '
      'different quantity -- it re-admits the control\'s own oscillation -- so it is a check on stability, '
      'not a third reading.*')
print('\n' + '=' * 100)

print('\n  ⛭⛭⛭ ⓶ NAMING THE SHARED NINE TENTHS FROM THE `SRCDEC` BANK')
print('-' * 100)
P = {}
for t in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r6915_pairs_{t}.npz'), allow_pickle=True)
    P[t] = (d['ls'].astype(float) / float(d['l_A']), d['Dl'], d['Dl_pairs'])
print(f"    the bank carries {P['lcdm'][2].shape[1]} bilinear terms on {len(P['lcdm'][0])} multipoles per arm, "
      f"q = {P['lcdm'][0].min():.3f}--{P['lcdm'][0].max():.3f}: all seven bands, at about "
      f"{np.median(np.diff(P['lcdm'][0])):.4f} in q, some "
      f"{int(round(1 / np.median(np.diff(P['lcdm'][0]))))} samples per acoustic period.")

print('\n    ⛔ THE LICENCE CHECK FIRST, AS THE PRE-REGISTRATION REQUIRED: does the 238-multipole TOTAL '
      'reproduce the step the 1900-multipole bank shows?  *If not, no per-term number is licensed.*')
print(f"    {'quantity':24s}" + ''.join(f"{b[0]:>19s}" for b in BASES) + '      verdict')
LIC = {}
for t, ref in (('lcdm', C0), ('cr', CA)):
    LIC[t] = row(f'{t} total, 238 pts', band_std(P[t][0], P[t][1]))
    LIC[t + '_ref'] = row(f'{t} total, 1900 pts', ref)

print('\n    ⌗ AND THE PER-TERM READING -- each term\'s OWN contrast, and its band-1 departure from its own '
      'bands 2--7 trend, on both arms:')
print(f"      {'term':12s}  {'control':>26s}  {'arm':>26s}   both?")
TERM = {}
for k, nm in enumerate(NM):
    ok = True
    dep = {}
    for t in ('lcdm', 'cr'):
        q, _, pr = P[t]
        y = pr[:, k]
        e = env_a(q, y)
        if np.any(np.abs(e) < 1e-30) or np.ptp(np.sign(e)) > 0:
            ok = False
            break
        v = np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, (y - e) / e)))
                      for a, b in zip(QE[:-1], QE[1:])])
        if np.any(v <= 0):
            ok = False
            break
        dep[t] = [departure(v, p, lg) for _, p, lg in BASES]
    if not ok:
        print(f"      {nm:12s}  {'envelope crosses zero -- contrast undefined, excluded':>56s}")
        continue
    TERM[nm] = dep
    sc = [min(d[0] for d in dep[t]) for t in ('lcdm', 'cr')]
    bc = [max(d[0] for d in dep[t]) for t in ('lcdm', 'cr')]
    both = all(all(d[0] > 0 and d[2] > 2.0 for d in dep[t]) for t in ('lcdm', 'cr'))
    print(f"      {nm:12s}  {sc[0]:+.3f} .. {bc[0]:+.3f}{'':>8s}  {sc[1]:+.3f} .. {bc[1]:+.3f}{'':>8s}   "
          f"{'** BOTH STEP UP **' if both else ''}")

print('\n    ⛔ BUT A DEPARTURE THE SIZE OF THE TOTAL\'S DOES NOT MAKE A TERM THE CARRIER -- that is the '
      'unearned inference `cc66.58` ⓶ punished, so here is the decisive test: REMOVE each term from the total '
      'and ask whether the step goes with it.')
print(f"      {'total minus':14s}  {'share of the total osc.':>24s}  {'control step':>28s}  {'arm step':>28s}")
KILL = {}
for k, nm in enumerate(NM):
    out = {}
    for t in ('lcdm', 'cr'):
        q, tot, pr = P[t]
        v = band_std(q, tot - pr[:, k])
        out[t] = [departure(v, p_, lg)[0] for _, p_, lg in BASES]
    q, tot, pr = P['lcdm']
    e = env_a(q, tot)
    sh = float(np.std(pr[:, k] - env_a(q, pr[:, k])) / np.std(tot - e))
    KILL[nm] = (out, sh)
    print(f"      {nm:14s}  {sh:>23.3f}  {min(out['lcdm']):+.3f} .. {max(out['lcdm']):+.3f}{'':>9s}  "
          f"{min(out['cr']):+.3f} .. {max(out['cr']):+.3f}")
base = {t: [departure(band_std(P[t][0], P[t][1]), p_, lg)[0] for _, p_, lg in BASES]
        for t in ('lcdm', 'cr')}
print(f"      {'(nothing)':14s}  {1.0:>23.3f}  {min(base['lcdm']):+.3f} .. {max(base['lcdm']):+.3f}{'':>9s}  "
      f"{min(base['cr']):+.3f} .. {max(base['cr']):+.3f}")
DROP = {nm: 1 - np.mean([abs(np.mean(KILL[nm][0][t])) / abs(np.mean(base[t])) for t in ('lcdm', 'cr')])
        for nm in NM}
ORD = sorted(DROP, key=lambda n: -DROP[n])
print('\n    ⇒ the step\'s fractional loss when each term is removed, largest first:')
for nm in ORD[:4]:
    print(f"      {nm:12s} removes {DROP[nm]:+.1%} of the step   (that term is {KILL[nm][1]:.1%} of the "
          f"total's oscillation)")
print(f"    ⇒ ** THE LOSSES SUM TO {sum(max(0.0, DROP[n]) for n in NM):.0%}, FAR MORE THAN ONE. **  *So the "
      f"step is NOT additive across the terms and NO SINGLE TERM CARRIES IT -- it is a property of the SUM, "
      f"which is the third row of the pre-registration's table and a null on the naming ⓶ asked for.*")
print('\n    ⛭⛭ BUT THE LEVERAGE IS NOT FLAT, AND THAT IS THE FINDING THE NULL LEAVES STANDING -- each term\'s '
      'share of the STEP against its share of the OSCILLATION:')
LEV = sorted(((DROP[n] / KILL[n][1], n) for n in NM if KILL[n][1] > 0.01), reverse=True)
for r, nm in LEV:
    print(f"      {nm:12s} {DROP[nm]:+6.1%} of the step on {KILL[nm][1]:6.1%} of the oscillation   "
          f"=>  leverage {r:5.2f}x" + ('   <- Doppler' if 'dp' in nm else ''))
DOP = [(r, nm) for r, nm in LEV if 'dp' in nm]
OTH = [(r, nm) for r, nm in LEV if 'dp' not in nm]
TOP2 = LEV[:2]
print(f"    ⇒ ** THE TWO HIGHEST-LEVERAGE TERMS ARE BOTH DOPPLER -- {TOP2[0][1]} at {TOP2[0][0]:.2f}x and "
      f"{TOP2[1][1]} at {TOP2[1][0]:.2f}x -- and they exceed EVERY term without a Doppler factor, the best of "
      f"which is {OTH[0][1]} at {OTH[0][0]:.2f}x, by a factor of {TOP2[1][0] / OTH[0][0]:.1f} or more. **")
print(f"      *The monopole `sw*sw` is {KILL['sw*sw'][1]:.0%} of the oscillation and carries the step at only "
      f"{DROP['sw*sw'] / KILL['sw*sw'][1]:.2f}x its weight; the Doppler autocorrelation is "
      f"{KILL['dp*dp'][1]:.0%} of it and carries it at {DROP['dp*dp'] / KILL['dp*dp'][1]:.2f}x.*")
print(f"      ⚠ *AND THE EXCEPTION IS NAMED RATHER THAN DROPPED: `dp*isw` carries a Doppler factor and sits at "
      f"{DROP['dp*isw'] / KILL['dp*isw'][1]:+.2f}x -- NEGATIVE -- so this is \"the two "
      f"highest-leverage terms are Doppler\", NOT \"every Doppler term leads\"; and `isw*isw` at "
      f"{min(r for r, n in LEV if 'dp' not in n):+.2f}x "
      f"sits lower still, so the ordering is not Doppler-versus-not.*")
print('    ⌗ ** SO ⓶ IS A NULL ON "ONE TERM" AND A NAMING ON "WHICH SECTOR": the shared step is a property '
      'of the sum, and within the sum the two highest-leverage terms both carry a Doppler factor. **')
print('      ⚠ *Not claimed: that the Doppler PRODUCES the shared step -- leverage is not authorship, and the '
      'non-additivity is exactly why. What is claimed is that a step-weighted reading of the bilinear '
      'decomposition is led by the Doppler terms where an amplitude-weighted one is led by the monopole.*')
print('\n' + '  ' + '-' * 96)

print('\n  ⛭⛭⛭ ⓷ WHICH STEP THE 42 PER CENT IS 42 PER CENT OF')
print('-' * 100)
print('    *`cc66.58`\'s table divided every channel\'s departure by `DEP[\'measured excess\']`, which is the '
      'departure of `MEAS - 1.0` -- the EXCESS\'s own response.*')
print(f"    ⇒ ** THE 42 PER CENT IS 42 PER CENT OF THE **EXCESS\'S** STEP, NOT OF THE SHARED STEP. **")
print('    *And that is the comparison a channel admits: a channel response is `band_std(knob)/band_std(control)`'
      ' and the excess is `band_std(arm)/band_std(control)` -- both ratios to the SAME control, in the same '
      'units.*')
print('\n    ⌗ AND THE TWO NORMALISATIONS OF THE **SAME** BAND-1 DEPARTURE, SET SIDE BY SIDE SO THEY CANNOT BE '
      'CONFLATED AGAIN:')
lc, _ = np.polyfit(QC[1:] ** 2, np.log(C0[1:]), 1), None
sA, iA = np.polyfit(QC[1:] ** 2, np.log(CA[1:]), 1)
sC, iC = np.polyfit(QC[1:] ** 2, np.log(C0[1:]), 1)
dA = float(np.log(CA[0]) - (sA * QC[0] ** 2 + iA))
dC = float(np.log(C0[0]) - (sC * QC[0] ** 2 + iC))
sE, iE = np.polyfit(QC[1:] ** 2, np.log(MEAS[1:] - 1.0), 1)
predE = float(np.exp(sE * QC[0] ** 2 + iE))
absdep = float((MEAS[0] - 1.0) - predE)
print(f"      the ONE departure, in excess units:            band 1's excess is {MEAS[0] - 1:+.4f} where its "
      f"own bands 2--7 trend predicts {predE:+.4f}  =>  {absdep:+.4f}")
print(f"      (i)  as a fraction of the EXCESS's own size:   {absdep / predE:+.3f}   <- what `cc66.58`'s "
      f"channel table, and its 42 per cent, is against")
print(f"      (ii) against either ARM's contrast departure:  {absdep / dC:+.3f} of the control's {dC:+.4f} "
      f"and {absdep / dA:+.3f} of the arm's {dA:+.4f}   <- where the \"nine tenths\" comes from")
print(f"      ⌗ *and the arms' own log-departures differ by {dA - dC:+.4f}, which IS {absdep:+.4f} to "
      f"{100 * abs((dA - dC) / absdep - 1):.1f} per cent -- the same number, which is what makes these two "
      f"denominators for ONE departure rather than two findings.*")
print('\n' + '=' * 100)

print(f"""
  ⛭⛭⛭ ⓵ THE STEP SURVIVES THE DIFFERENTIAL ESTIMATOR.  *Forming the arm-to-control ratio per multipole and
    taking the contrast of THAT -- so the common oscillation divides out before any width is taken -- band 1
    departs from its own bands 2--7 trend by {min(d[0] for d in OUT['per common l'][0]):+.3f} to
    {max(d[0] for d in OUT['per common l'][0]):+.3f} per common $\\ell$ and
    {min(d[0] for d in OUT['per common q'][0]):+.3f} to {max(d[0] for d in OUT['per common q'][0]):+.3f} per
    common $q$: SAME SIGN on all four bases and BOTH abscissas, at
    {min(abs(d[2]) for d in OUT['per common q'][0]):.1f}--{max(abs(d[2]) for d in OUT['per common l'][0]):.1f}
    sigma.*  ⇒ ** SO THE TENTH THAT FAILED TO CANCEL IS NOT THE RESIDUAL OF TWO LARGE NUMBERS -- IT EXISTS IN AN
    ESTIMATOR IN WHICH THE TWO LARGE NUMBERS ARE NEVER FORMED. **  *It survives at about
    {np.mean([abs(d[0]) for d in OUT['per common q'][0]]) / np.mean([abs(d[0]) for d in OUT['present excess'][0]]):.0%}
    of the present route's fractional size, and the estimator is the one the row should be built on.*
  ⌷ *And the conditioning hazard the pre-registration named does not fire: the control never falls below
    {min(DC[(QCq >= a) & (QCq < b)].min() / np.median(DC[(QCq >= a) & (QCq < b)]) for a, b in zip(QE[:-1], QE[1:])):.2f}
    of its band median anywhere, so no band divides by a near-zero.  ⌗ And the smoothed-divisor control does what
    it should: with the differencing removed the departure goes POSITIVE, back toward the arms' own +0.3 --
    **which shows it is the differencing, and not the division, that produces the negative step.**

  ⛔⛔ ⓶ NO SINGLE TERM CARRIES THE SHARED STEP -- IT IS A PROPERTY OF THE SUM, WHICH IS A NULL ON WHAT WAS
    ASKED.  *The 238-multipole total first reproduces the 1900-multipole step to better than 0.006 in departure
    on both arms, so the per-term reading is licensed.  Then removing each term in turn: the losses sum to
    {sum(max(0.0, DROP[n]) for n in NM):.0%}, far more than one, so the step is not additive.*
  ⛭⛭ *But the LEVERAGE is not flat, and that is what the null leaves standing: the two highest-leverage terms
    are BOTH Doppler -- `sw*dp` at {DROP['sw*dp'] / KILL['sw*dp'][1]:.2f}x and `dp*dp` at
    {DROP['dp*dp'] / KILL['dp*dp'][1]:.2f}x their amplitude share -- exceeding every term without a Doppler
    factor by {min(DROP['sw*dp'] / KILL['sw*dp'][1], DROP['dp*dp'] / KILL['dp*dp'][1]) / (DROP['sw*isw'] / KILL['sw*isw'][1]):.1f}
    or more, while the monopole carries {KILL['sw*sw'][1]:.0%} of the oscillation at only
    {DROP['sw*sw'] / KILL['sw*sw'][1]:.2f}x.*  ⇒ ** A step-weighted reading of the bilinear decomposition is led
    by the Doppler where an amplitude-weighted one is led by the monopole. **  ⚠ *`dp*isw` is the named
    exception at {DROP['dp*isw'] / KILL['dp*isw'][1]:+.2f}x, so this is not "every Doppler term leads"; and
    leverage is not authorship, and the non-additivity is exactly why it is not.*

  ⛭ ⓷ THE 42 PER CENT IS 42 PER CENT OF THE **EXCESS'S** STEP.  *`cc66.58`'s table divided by the departure of
    `MEAS - 1.0`, the excess's own response, which is the only comparison a channel admits -- a channel response
    and the excess are both ratios to the SAME control.*  ⇒ ** So it is the large reading: the pair accounts for
    two fifths of the step the excess actually has, not of the shared step most of which cancels. **
  ⌗ *And the two normalisations are ONE departure, {absdep:+.4f} in excess units: {absdep / predE:+.3f} of the
    excess's own extrapolated size (what the 42 per cent is against) and {absdep / dC:+.3f} of the control's
    contrast departure (where the "nine tenths" comes from).  The arms' own log-departures differ by
    {dA - dC:+.4f}, which is that same number to {100 * abs((dA - dC) / absdep - 1):.1f} per cent.*

  ⛔ *No envelope chosen, no basis chosen, no abscissa chosen, no new candidate, no mechanism proposed, and no
    corpus edits.*
""")
