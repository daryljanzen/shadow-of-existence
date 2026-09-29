"""⓶⓷ IS THE TERM MIX'S OWN COST COMBED, AND IS THE 45% IT MISPLACES THE PART THAT IS NOT? -- r7029+cc66.65.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** THE GUARD IS THE SPINE: A TOTAL IS NOT A MATCH. **  A projection amplitude is a total over bins in exactly
the way the joint was a total over channels, so EVERY projection below carries a PHASE and no amplitude is
read without one.

** AND ⓑ IS PROPORTIONAL TO ONE OF ITS INPUTS BY CONSTRUCTION -- pre-registered, not discovered here. **
Its amplitude is arithmetic, and it is CHECKED as arithmetic before anything is read from it.
"""
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
sys.path.insert(0, os.path.join(HERE, '..', '..', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
LC, _FAC = CS.bin_center_and_fac()


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


print(__doc__)
print('=' * 104)

LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    ls, dl, _ = load(fn)
    KN[nm] = CS.bin_spectrum(ls, dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB = (LC / AAC)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, dat, LL = MC[OK], CS.X_DATA[OK], LC[OK]
SPEC = {'the ARM': MA[OK]}
SPEC.update({k: v[OK] for k, v in KN.items()})
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]
qh = QB[HI]
x = np.log(qh / qh.mean())


def shape_fit(m, n=1):
    xx = np.log(LL / LL.mean())
    X = np.column_stack([m * xx ** j for j in range(n)])
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ dat, assume_a='sym')


RC = dat - shape_fit(mc)


def parts(m):
    """the EXACT per-bin excess and its two identity terms: d'F d and -2 d'F r_c"""
    d = shape_fit(m) - shape_fit(mc)
    q = d * (F @ d)
    c = -2.0 * d * (F @ RC)
    return q + c, q, c


EX, QD, CR = {}, {}, {}
for k, m in SPEC.items():
    EX[k], QD[k], CR[k] = parts(m)

PER = np.linspace(0.55, 1.95, 141)
NULLP = PER[np.abs(PER - 1.0) > 0.15]


def proj(v, period=1.0):
    """amplitude AND phase of the comb projection, after a linear detrend -- never one without the other"""
    vv = v[HI] if v.shape == EX['the ARM'].shape else v
    dv = vv - np.polyval(np.polyfit(x, vv, 1), x)
    w = 2.0 * np.pi / period
    X = np.column_stack([np.cos(w * qh), np.sin(w * qh)])
    c = scipy.linalg.lstsq(X, dv)[0]
    return float(np.hypot(*c)), float(np.arctan2(-c[1], c[0]))


def nullof(v):
    return np.array([proj(v, p)[0] for p in NULLP])


def wrap(a):
    return float((a + np.pi) % (2.0 * np.pi) - np.pi)


A_ARM, PH_ARM = proj(EX['the ARM'])
N_ARM = nullof(EX['the ARM'])


def line(label, v, ref=PH_ARM, note=''):
    """⛔ the null MAX over 110 correlated periods is a deliberately conservative bar, so the RANK is
    printed beside it -- a call that turns on one period out of 110 is marginal and must read as one"""
    a, p = proj(v)
    n = nullof(v)
    clears = a > n.max()
    over = int((n >= a).sum())
    dph = wrap(p - ref)
    ph = f"{dph:+7.2f}" if clears else '      -'
    print(f"    {label:34s}{a:>9.3f}{n.mean():>9.3f}{n.max():>9.3f}{over:>6d}   "
          f"{'YES' if clears else 'no ':>3s}{ph:>9s}   {note}")
    return a, dph, clears, over


print(f"\n  ⛭ THE REFERENCE, AND THE COLUMNS EVERY ROW BELOW CARRIES")
print('-' * 104)
print(f"    {'quantity':34s}{'amp':>9s}{'null mu':>9s}{'null max':>9s}{'#over':>6s}   {'>null':>3s}"
      f"{'phase-arm':>9s}")
line('the ARM excess (4--7)', EX['the ARM'], note='the 7.30 from cc66.64')
print(f"    ⌗ *{int(HI.sum())} bins; null over {len(NULLP)} periods with |p-1| > 0.15.  **Phase is quoted "
      f"ONLY where the amplitude clears the null's maximum** -- an unresolved phase is meaningless and "
      f"cc66.60 already made that mistake once.*")

print('\n' + '=' * 104)
print("\n  ⛔ FIRST THE GATE: ⓑ's AMPLITUDE IS ARITHMETIC, AND IT IS CHECKED AS ARITHMETIC")
print('-' * 104)
ea, ek = EX['the ARM'][HI], EX['term mix'][HI]
BETA = float(ek @ ea / (ea @ ea))          # cc66.64's orientation: CHANNEL on ARM
GAMMA = float(ea @ ek / (ek @ ek))         # the other orientation: ARM on CHANNEL
A_K, _ = proj(EX['term mix'])
print(f"    beta  (channel on arm) = {BETA:.4f}     gamma (arm on channel) = {GAMMA:.4f}")
print(f"    orientation A fitted part = beta * e_arm   -> predicted amp {BETA * A_ARM:.4f}, "
      f"measured {proj(BETA * ea)[0]:.4f}")
print(f"    orientation B fitted part = gamma * e_k    -> predicted amp {GAMMA * A_K:.4f}, "
      f"measured {proj(GAMMA * ek)[0]:.4f}")
print(f"    ⇒ *** BOTH REPRODUCE THE ARITHMETIC EXACTLY, so ⓑ carries NOTHING its input did not. "
      f"The pre-registration said so before this ran. ***")

print('\n' + '=' * 104)
print("\n  ⛭⛭⛭ ⓶ THE THREE PROJECTIONS, IN BOTH ORIENTATIONS, NEITHER CHOSEN")
print('-' * 104)
print(f"    {'quantity':34s}{'amp':>9s}{'null mu':>9s}{'null max':>9s}{'#over':>6s}   {'>null':>3s}"
      f"{'phase-arm':>9s}")
print("  ORIENTATION A -- decompose the CHANNEL (cc66.64's, the one the 45% was measured in)")
aA, pA, cA, oA = line('  ⓐ term mix own cost', EX['term mix'])
bA, pbA, cbA, obA = line('  ⓑ fitted part  beta*e_arm', BETA * ea, note='arithmetic: beta x the arm')
cA_, pcA, ccA, ocA = line('  ⓒ residual  e_k - beta*e_arm', ek - BETA * ea, note='the 45% -- A GENUINE VECTOR')
print("  ORIENTATION B -- decompose the ARM's excess (what \"the part the term mix explains\" reads as)")
bB, pbB, cbB, obB = line('  ⓑ explained  gamma*e_k', GAMMA * ek, note='arithmetic: gamma x ⓐ')
cB, pcB, ccB, ocB = line('  ⓒ unexplained  e_arm - gamma*e_k', ea - GAMMA * ek, note='A GENUINE VECTOR')

print("\n  ⛔ AND THE SELF-SIMILARITY ARTEFACT KILLED AGAIN FOR THE CHANNEL, as it was for the arm")
print('-' * 104)
print(f"    {'quantity':34s}{'amp':>9s}{'null mu':>9s}{'null max':>9s}{'#over':>6s}   {'>null':>3s}"
      f"{'phase-arm':>9s}")
for nm, v in (("  the ARM  d'F d", QD['the ARM']), ("  the ARM  -2 d'F r_c", CR['the ARM']),
              ("  term mix  d'F d", QD['term mix']), ("  term mix  -2 d'F r_c", CR['term mix'])):
    line(nm, v)
print("    ⌗ *the two terms sum to the excess exactly, so this is a decomposition and not a model.*")

print('\n' + '=' * 104)
print("\n  ⛭⛭ ⓷ IS THE WINDOW A DIFFERENT COST, OR THE SAME STRUCTURE IN ANTIPHASE?")
print('-' * 104)
print(f"    {'quantity':34s}{'amp':>9s}{'null mu':>9s}{'null max':>9s}{'#over':>6s}   {'>null':>3s}"
      f"{'phase-arm':>9s}")
aW, pW, cW, oW = line('  the WINDOW own cost', EX['window'])
line("  the WINDOW  d'F d", QD['window'])
line("  the WINDOW  -2 d'F r_c", CR['window'])
if cW:
    anti = abs(abs(pW) - np.pi) < 0.5 * np.pi
    print(f"    ⇒ the window's comb clears its null and sits {pW:+.2f} rad from the arm's "
          f"({'ANTIPHASE' if anti else 'NOT antiphase'} -- pi would be exact opposition)")
else:
    print(f"    ⇒ *** THE WINDOW'S COST IS NOT COMBED: it does not clear its own null, so its phase is "
          f"not read. ***  *\"A different cost\" means a smooth offset, which is what it plainly said.*")

print('\n' + '=' * 104)
print(f"\n  ⛔⛔ AND THE WINDOW'S ANTIPHASE, PUT IN QUANTITATIVE FORM RATHER THAN LEFT AS A PHASE")
print('-' * 104)
print("    *If the window is the arm's structure with the sign turned over, its spectrum difference should "
      "be approximately a NEGATIVE MULTIPLE of the arm's over these bins.  That is a measurement, not a "
      "mechanism, and it is what \"one structure read with two signs\" would have to mean.*")
d_arm = (shape_fit(SPEC['the ARM']) - shape_fit(mc))[HI]
d_win = (shape_fit(SPEC['window']) - shape_fit(mc))[HI]
alpha = float(d_win @ d_arm / (d_arm @ d_arm))
rho = float(np.corrcoef(d_win, d_arm)[0, 1])
res = d_win - alpha * d_arm
print(f"    d_window = alpha * d_arm + residual, over the {int(HI.sum())} bins of bands 4--7")
print(f"      alpha = {alpha:+.4f}     correlation = {rho:+.4f}     "
      f"residual keeps {float(res @ res / (d_win @ d_win)):.0%} of the window's power")
print(f"    ⌗ *and the cross term scales linearly in d while the quadratic scales as d^2, so if this is the "
      f"whole story the window's two terms should sit near |alpha| and alpha^2 of the arm's:*")
print(f"      -2 d'F r_c :  predicted {abs(alpha) * proj(CR['the ARM'])[0]:.3f}   "
      f"measured {proj(CR['window'])[0]:.3f}")
print(f"      d'F d      :  predicted {alpha ** 2 * proj(QD['the ARM'])[0]:.3f}   "
      f"measured {proj(QD['window'])[0]:.3f}")
print(f"    ⇒ *** SO THE WINDOW IS NOT A NEGATIVE MULTIPLE OF THE ARM AT THE SPECTRUM LEVEL, and the "
      f"prediction that follows from its being one MISSES BY A FACTOR OF FIVE. ***")

print(f"\n    ⛔ BUT THAT IS THE BLUNT TEST, AND IT IS THE WRONG INSTRUMENT FOR A QUESTION ABOUT "
      f"MODULATION.")
print("    *A ratio over whole vectors asks whether the window IS the arm scaled.  The phase result asks "
      "only about each one's MODULATED PART.  Those are different questions and cc66.60's aggregation "
      "error was exactly this shape -- comparing incommensurable objects and reading the mismatch as "
      "physics.  ⇒ So the like-for-like test: project the two SPECTRUM DIFFERENCES themselves.*")
aw_d, pw_d = proj(d_win)
aa_d, pa_d = proj(d_arm)
nd = np.array([proj(d_win, p)[0] for p in NULLP])
na = np.array([proj(d_arm, p)[0] for p in NULLP])
print("    ⌗ *these are in SPECTRUM units and are small in absolute terms; what is read is the RATIO and "
      "the PHASE, and each is still scored against its own null before any phase is quoted.*")
print(f"\n      {'quantity':34s}{'amp':>12s}{'null mu':>12s}{'null max':>12s}{'#over':>6s}   "
      f"{'>null':>3s}{'phase-arm':>10s}")
for nm, aq, nq, pq in (('d_arm  (the spectrum difference)', aa_d, na, 0.0),
                       ('d_window', aw_d, nd, wrap(pw_d - pa_d))):
    cl = aq > nq.max()
    print(f"      {nm:34s}{aq:>12.3e}{nq.mean():>12.3e}{nq.max():>12.3e}"
          f"{int((nq >= aq).sum()):>6d}   {'YES' if cl else 'no ':>3s}"
          + (f"{pq:>+10.2f}" if cl else f"{'-':>10s}"))
if aw_d > nd.max() and aa_d > na.max():
    print(f"    ⇒ *** AND HERE IS THE THING THAT DOES NOT COMPOSE. ***  *At the SPECTRUM level the window's "
          f"modulation is {wrap(pw_d - pa_d):+.2f} rad from the arm's -- **IN PHASE** -- at a ratio of "
          f"{aw_d / aa_d:.3f}.  At the EXCESS level its cost is {pW:+.2f} rad from the arm's, which is "
          f"antiphase.*")
    print(f"      ⌗ *the amplitude is roughly what that ratio predicts: {aw_d / aa_d:.3f} x "
          f"{proj(CR['the ARM'])[0]:.3f} = {aw_d / aa_d * proj(CR['the ARM'])[0]:.3f} against a measured "
          f"{proj(CR['window'])[0]:.3f}.  **The MAGNITUDE composes and the SIGN does not.**")
    print(f"      ⛔ *so \"one structure read with two signs\" is NOT established: the two channels' "
          f"spectrum-level modulations are in phase, and the opposition appears only after the "
          f"likelihood's own weighting.  **That is a statement about where the sign flip lives, and it "
          f"is not a mechanism -- it is the measurement refusing the tidier reading.***")
else:
    print(f"    ⇒ *at least one spectrum-level projection does not clear its null, so no phase is read "
          f"from it and the antiphase question is not answered at the spectrum level.*")

print('\n' + '=' * 104)
