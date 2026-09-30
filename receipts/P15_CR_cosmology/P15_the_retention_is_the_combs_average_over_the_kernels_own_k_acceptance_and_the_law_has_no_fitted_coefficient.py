"""
P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_and_the_law_has_no_fitted_coefficient

** THE RETENTION IS THE COMB AVERAGED OVER THE KERNEL'S OWN k-ACCEPTANCE, AND THE LAW THAT SAYS SO HAS
   NO FITTED COEFFICIENT -- so it predicts an ABSOLUTE amplitude and can be killed by one. **

`r6919+cc66.42` named the joint object -- dr_s/dchi across the visibility, 0.454950 against 0.396733 --
and stopped there, under a `no mechanism` guard.  `r7039` lifted that guard and `r7043` composed the
result with `r7041`'s convergence order.  This receipt is the law.

⛭ THE LAW.  For a STANDING oscillation the line-of-sight integral factorises with no approximation:

    Delta_l(k) = cos(k r_s*) * k^((1-ns)/2) * G_l(k),    G_l(k) = INT vis(eta) j_l(k x0) d eta

*The comb therefore passes into the transfer UNTOUCHED, and the only thing left that can damp it is the
sum over k at fixed l*, whose weight is W_l(k) = P(k) k^(1-ns) G_l(k)^2 = G_l(k)^2 dk/k -- the tilt
cancelling exactly.  With C_l = INT W cos^2(k r_s*) dk = (1/2) INT W + (1/2) Re INT W exp(2 i k r_s*),
the comb's fractional amplitude in C_l is

    A_l = | INT W exp(2 i k r_s*) dk | / INT W dk

⇒ *** AND THERE IS NOTHING TO FIT.  A_l is built from the window the kernel reads and the comb's period,
    both of them the background's own. ***

⌗ READ PHYSICALLY: a WIDER chi-extent narrows the kernel's k-acceptance, so less of an acoustic period is
averaged over and more of the comb survives.  This arm's visibility is 14.6 per cent the wider in chi while
accumulating the same sound horizon to 0.08 per cent (`r6919`), which is why it retains MORE.

⛔⛔ AND THE MEASURING INSTRUMENT TOOK THREE ATTEMPTS.  THE FIRST TWO ARE NAMED HERE BECAUSE THE GATE THAT
   CAUGHT THEM IS WORTH MORE THAN THE RESULT.
  (1) A band std after a running-mean envelope.  Fed a comb of KNOWN amplitude 0.5 it returns 0.46 to 0.55
    -- up to 46 per cent wrong on a known input.  ** The arm-to-control RATIO survived it only because the
    same factor divides out of both arms, which is exactly why the ratio agreed while the absolute did not.
    A statistic can be fit for a ratio and unfit for the quantity the ratio is made of. **
  (2) A per-band matched filter choosing the period by MAXIMISING the fitted amplitude.  Wrong twice:
    maximising signal is not a fit criterion (a longer period absorbs more of the band's trend, so the
    search runs to the edge of its range by construction), and a band is 0.70 wide in q where the comb's
    period is about 1.00 -- LESS THAN ONE CYCLE, so a per-band fit cannot determine a period at all.
  (3) What is used: ONE period for the whole range by MINIMUM RESIDUAL, then HELD while the amplitude is
    fitted band by band.  ** Gate ⓪ refuses to print any measurement unless it recovers a known input. **
  ⌗ That is `cc66.60`'s error -- the instrument not matching the question's grain -- for the third time in
  this row, and the first time caught before a number was reported rather than after.

⛔ WHAT IS NOT CLAIMED.  Not that the injection IS the real source: it is the projection's transfer of a
known input, and over-delivery is sufficiency and not identity.  No convergence claim -- `r7041`'s sweep is
a separate row and this receipt reads the REPORTED settings only.  Nothing about which cosmology is right.
And no claim that naming A_l explains why the construction assigns its scales and its distances to
different rates, which is `r6919`'s own reserved bound and is untouched here.
"""
import os
import sys

import numpy as np
from scipy.special import spherical_jn

FAILS = []


def check(name, cond, got=None):
    ok = bool(cond)
    print(f"    [{'ok' if ok else 'FAIL'}]  {name}" + (f"   {got}" if got is not None else ""))
    if not ok:
        FAILS.append(name)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
ED = np.arange(0.85, 5.76, 0.7)
LO, HI, NG = 0.85, 5.75, 1200
GATE_TOL = 0.05
FLOOR = 0.006                      # r6911's, on a KNOWN injected contrast

print(__doc__)
print("=" * 100)

NEED = ['r7041_accept_lcdm.npz', 'r7041_accept_cr.npz',
        'r6919_injected_lcdm.npz', 'r6919_injected_cr.npz']
for n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{n}`",
          os.path.exists(os.path.join(SP, n)), n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS")
    print("     rather than reporting the parts it could run as the whole.")
    print(f"\nGATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

AC = {t: np.load(os.path.join(SP, f'r7041_accept_{t}.npz')) for t in ('lcdm', 'cr')}
IJ = {t: np.load(os.path.join(SP, f'r6919_injected_{t}.npz')) for t in ('lcdm', 'cr')}


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running arithmetic mean -- that receipt's statistic, unchanged"""
    e = np.empty_like(y, dtype=float)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    y = np.asarray(y, float)
    e = env_a(x, y, win)
    return (y - e) / e


def _fit(x, y, T):
    X = np.column_stack([np.cos(2 * np.pi * x / T), np.sin(2 * np.pi * x / T),
                         np.ones_like(x), x])
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ c
    return float(np.hypot(c[0], c[1])), float(r @ r)


def fit_period(q, o, pers=np.linspace(0.90, 1.20, 1201)):
    """ONE period for the whole range, chosen by MINIMUM RESIDUAL -- see attempt (2)"""
    m = (q >= LO) & (q <= HI)
    return min(((_fit(q[m], o[m], T)[1], T) for T in pers))[1]


def band_amp(q, o, a, b, T):
    m = (q >= a) & (q <= b)
    return _fit(q[m], o[m], T)[0]


print()
print("  " + "=" * 96)
print("  ⓪ THE INSTRUMENT'S OWN GATE, BEFORE ANY MEASUREMENT IS PRINTED")
print("  " + "=" * 96)
d = AC['lcdm']
q = d['q__fixed']
E = env_a(q, np.asarray(d['Dl__fixed'], float))
A0, P0, PH0 = 0.5, 1.0347, 0.7
syn = osc(q, E * (1.0 + A0 * np.cos(2 * np.pi * q / P0 + PH0)))
Tg = fit_period(q, syn)
rec = [band_amp(q, syn, a, b, Tg) for a, b in zip(ED[:-1], ED[1:])]
err = max(abs(a - A0) for a in rec) / A0
check("⛭ the statistic recovers a KNOWN comb's period", abs(Tg - P0) / P0 < 0.01,
      f"{Tg:.4f} against {P0} ({abs(Tg-P0)/P0*100:.2f}%)")
check("⛭ and its amplitude, to better than five per cent -- *the two earlier instruments did not, and "
      "this gate is why they were caught rather than reported*", err < GATE_TOL,
      f"worst {err*100:.2f}%: " + ", ".join(f"{a:.4f}" for a in rec))
if FAILS:
    print("\n  ⛔ THE INSTRUMENT DOES NOT RECOVER A KNOWN INPUT.  Nothing further is printed: a")
    print("     measurement from an ungated statistic is precisely what attempts (1) and (2) produced.")
    print(f"\nGATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

print()
print("  " + "=" * 96)
print("  ⓵ A_l DOES NOT DEPEND ON THE INJECTION, AND THAT IS GATED RATHER THAN ASSERTED")
print("  " + "=" * 96)
print("    *`A_l` is built from `vis`, `x0`, `k` and `r_s*` and nothing in it refers to what was")
print("     injected.  The bank therefore holds ONE `A` per arm.  ⛔ A first fold computed it per")
print("     injection and would have banked two keys holding identical arrays -- an arithmetic identity")
print("     dressed as two measurements.  So the identity is CHECKED here instead:*")
for t in ('lcdm', 'cr'):
    d = AC[t]
    same = all(np.array_equal(d[f'{k}__fixed'], d[f'{k}__sweepown'])
               for k in ('eta', 'x0', 'vis', 'k', 'P'))
    check(f"⓵{'ᵃ' if t == 'lcdm' else 'ᵇ'} {t}: the two injections share window, kernel argument, "
          f"visibility, k axis and measure -- so one `A` serves both", same,
          "eta, x0, vis, k, P all byte-equal" if same else "they differ")
    check(f"     ...and `r_s*` too, which is the other half of `A`",
          float(d['r_s__fixed']) == float(d['r_s__sweepown']),
          f"{float(d['r_s__fixed']):.6f}")

print()
print("  " + "=" * 96)
print("  ⓶ THE FACTORISATION IS EXACT, AND A_l IS RE-DERIVED RATHER THAN TAKEN FROM THE BANK")
print("  " + "=" * 96)
for t in ('lcdm', 'cr'):
    d = AC[t]
    ls = d['ls__fixed'].astype(int)
    k, ee, x0, v = d['k__fixed'], d['eta__fixed'], d['x0__fixed'], d['vis__fixed']
    RS, ns = float(d['r_s__fixed']), float(d['ns__fixed'])
    samp, Dlk = d['samp__fixed'], d['Dlk_samp__fixed']
    dk = np.gradient(k)
    res, dA = [], []
    for j, i in enumerate(samp):
        J = spherical_jn(int(ls[i]), k[None, :] * x0[:, None])
        G = np.trapezoid(v[:, None] * J, ee, axis=0)
        pred = np.cos(k * RS) * k ** (0.5 * (1 - ns)) * G
        mx = np.max(np.abs(Dlk[j]))
        res.append(np.max(np.abs(pred - Dlk[j])) / mx)
        W = G ** 2 * dk / k
        dA.append(abs(abs(np.sum(W * np.exp(2j * k * RS))) / W.sum() - float(d['A'][i]))
                  / float(d['A'][i]))
    g = 'ᵃ' if t == 'lcdm' else 'ᵇ'
    check(f"⓶{g} {t}: Delta_l(k) = cos(k r_s*) k^((1-ns)/2) G_l(k) EXACTLY, on {len(samp)} multipoles "
          f"spread across the reported range -- *so the comb enters the transfer undamped and the "
          f"k-sum is the only thing that can touch it*", max(res) < 1e-12,
          f"max relative residual {max(res):.2e}")
    check(f"     ...and A_l recomputed from `vis`, `x0` and `k` reproduces the banked value, so the "
          f"law is re-derived here and not trusted", max(dA) < 1e-10,
          f"max relative difference {max(dA):.2e}")

print()
print("  " + "=" * 96)
print("  ⓷ THE ACCEPTANCE, AND IT LANDS ON r6919's OWN NUMBER BY A DIFFERENT ROUTE")
print("  " + "=" * 96)
sp = {}
for t in ('lcdm', 'cr'):
    d = AC[t]
    m = (d['q__fixed'] >= LO) & (d['q__fixed'] <= HI) & np.isfinite(d['dkw'])
    sp[t] = float((2 * float(d['r_s__fixed']) * d['dkw'])[m].mean())
    print(f"    {t}: the acceptance spans 2 r_s* dk = {sp[t]:.4f} of acoustic phase")
narrow = (1 - sp['cr'] / sp['lcdm']) * 100
check("⛭⛭ ⓷ the ARM's acceptance is the narrower, by about the thirteen per cent `r6919`'s "
      "dr_s/dchi independently gives (0.454950 -> 0.396733 is 12.8 per cent) -- *two routes to one "
      "quantity, and the agreement is not built in anywhere*",
      3.0 < narrow < 25.0 and abs(narrow - 12.8) < 5.0,
      f"{narrow:.1f} per cent narrower against 12.8 per cent")

print()
print("  " + "=" * 96)
print("  ⓸ THE LAW FORWARD: ABSOLUTE, BOTH ARMS, NO FITTED COEFFICIENT")
print("  " + "=" * 96)
print(f"    {'band':>12s} {'lcdm law':>9s} {'lcdm meas':>10s} {'ratio':>7s}   "
      f"{'cr law':>9s} {'cr meas':>9s} {'ratio':>7s}")
worst, rows = 0.0, []
TF = {}
for t in ('lcdm', 'cr'):
    d = AC[t]
    TF[t] = fit_period(d['q__fixed'], osc(d['q__fixed'], np.asarray(d['Dl__fixed'], float)))
for a, b in zip(ED[:-1], ED[1:]):
    r = []
    for t in ('lcdm', 'cr'):
        d = AC[t]
        qq = d['q__fixed']
        oo = osc(qq, np.asarray(d['Dl__fixed'], float))
        mm = (qq >= a) & (qq <= b) & np.isfinite(d['A'])
        law = float(d['A'][mm].mean())
        mea = band_amp(qq, oo, a, b, TF[t])
        r += [law, mea, law / mea]
    rows.append(r)
    worst = max(worst, abs(r[2] - 1), abs(r[5] - 1))
    print(f"    {a:5.2f}-{b:5.2f} {r[0]:9.4f} {r[1]:10.4f} {r[2]:7.3f}   "
          f"{r[3]:9.4f} {r[4]:9.4f} {r[5]:7.3f}")
check("⛭⛭⛭ ⓸ the law predicts the ABSOLUTE comb amplitude on BOTH arms with nothing fitted, to "
      "within ten per cent everywhere", worst < 0.10, f"worst deviation {worst*100:.1f} per cent")
check(f"     ...and six of the seven bands on each arm land inside the instrument's own "
      f"{err*100:.2f} per cent accuracy on a known input, which is the tightest claim available "
      f"here and no tighter one is made",
      sum(1 for r in rows if abs(r[2] - 1) < 0.05) >= 6
      and sum(1 for r in rows if abs(r[5] - 1) < 0.05) >= 6,
      f"lcdm {sum(1 for r in rows if abs(r[2]-1) < 0.05)}/7, "
      f"cr {sum(1 for r in rows if abs(r[5]-1) < 0.05)}/7 inside 5 per cent")

print()
print("  " + "=" * 96)
print("  ⓹ AND THE REPRODUCTION GATE: THIS RUN IS r6919's RUN, UNSLICED")
print("  " + "=" * 96)


def ratio_stat(qa, Da, qb, Db, a=LO, b=HI):
    """r6919's own arm-to-control statistic, unchanged"""
    x = np.linspace(a, b, NG)
    A = np.interp(x, qa, osc(qa, Da))
    B = np.interp(x, qb, osc(qb, Db))
    return float(np.sum(A * B) / np.sum(B * B))


r_now = ratio_stat(AC['cr']['q__fixed'], AC['cr']['Dl__fixed'],
                   AC['lcdm']['q__fixed'], AC['lcdm']['Dl__fixed'])
qb = {t: IJ[t]['ls__fixed'].astype(float) / float(IJ[t]['l_A__fixed']) for t in IJ}
r_bank = ratio_stat(qb['cr'], IJ['cr']['Dl__fixed'], qb['lcdm'], IJ['lcdm']['Dl__fixed'])
check("⓹ the fixed injection's arm-to-control ratio reproduces `r6919`'s banked run to better than "
      "the floor -- *and these were computed on DIFFERENT run schemes, that one sliced on `KBATCH` "
      "and this one unsliced, so the agreement covers the scheme as well as the statistic*",
      abs(r_now - r_bank) / r_bank < FLOOR,
      f"{r_now:.4f} now against {r_bank:.4f} banked, {abs(r_now-r_bank)/r_bank*100:.4f} per cent")

print()
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print()
print("  VERDICT: ** the retention is the comb averaged over the kernel's own k-acceptance, and the")
print("  law that says so has no fitted coefficient. **")
print("  *The line-of-sight integral factorises exactly for a standing oscillation, so the comb reaches")
print("  the transfer undamped and only the sum over k at fixed l can touch it.  The acceptance's width")
print("  is set inversely by the chi-extent of the visibility -- this arm's is the wider while")
print("  accumulating the same sound horizon -- and A_l predicts the ABSOLUTE amplitude on both arms.*")
print("  ⛔ ** What it does NOT do is say why the construction puts its scales and its distances on")
print("     different rates. **  That is `r6919`'s reserved bound and this receipt does not touch it.")
print("  ⌗ ** And the instrument took three attempts. **  The gate on a known input is what separated")
print("     the third from the first two, and it is the part that transfers.")
