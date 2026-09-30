"""THE ACCEPTANCE LAW, exhibited on the integral and used forward with no fitted coefficient.

** NOTHING HERE IS A SPECTRUM OF THE MODEL. **  Every number is what each arm's projection makes of a
KNOWN analytic oscillation (`SRCINJ`), so nothing here may be compared with a banked spectrum or the sky.

THE LAW.  For a standing oscillation the line-of-sight integral factorises EXACTLY:

    Delta_l(k) = cos(k r_s*) * k^((1-ns)/2) * G_l(k),     G_l(k) = INT vis(eta) j_l(k x0) d eta

so the comb passes into the transfer untouched and ** the only thing that can damp it is the sum over k
at fixed l **, whose weight is W_l(k) = P(k) k^(1-ns) G_l(k)^2 = G_l(k)^2 dk/k -- the tilt cancels.  Then
C_l = INT W cos^2(k r_s*) dk = (1/2) INT W + (1/2) Re INT W exp(2 i k r_s*), so the comb's FRACTIONAL
amplitude in C_l is

    A_l = | INT W exp(2 i k r_s*) dk | / INT W dk

*** WITH NO FREE COEFFICIENT.  It therefore predicts an ABSOLUTE amplitude and can be killed by one. ***

⌗ Read physically: retention is the comb averaged over the kernel's own k-acceptance, and that acceptance
is narrowed by a WIDER chi-extent of the visibility.  This arm's window is 14.6 per cent the wider while
accumulating the same sound horizon to 0.08 per cent (r6919+cc66.42), so it averages the comb over less of
an acoustic period and retains more of it.

⛔⛔ AND THE MEASURING INSTRUMENT TOOK THREE ATTEMPTS.  THE FIRST TWO ARE IN THE SOURCE BECAUSE THE GATE
   THAT CAUGHT THEM IS THE POINT.
  ① A band std after a running-mean envelope.  Pushed a comb of KNOWN amplitude 0.5 through it and it
    returns 0.46 to 0.55 -- swings of up to 46 per cent on a known input.  *A statistic that wrong cannot
    test a law to a few per cent.*  ** The arm-to-control RATIO survived it only because the same factor
    divides out of both arms, which is exactly why the ratio agreed while the absolute did not. **
  ② A per-band matched filter selecting the period by MAXIMISING the fitted amplitude.  Broken twice over:
    maximising signal is not a fit criterion (a longer period absorbs more of the band's trend, so the
    search runs to the edge of the range by construction), and a band is 0.70 wide in q where the comb's
    period is about 1.00 -- ** LESS THAN ONE CYCLE, so a per-band fit cannot determine a period at all. **
  ③ What is used: ONE period for the whole range, chosen by MINIMUM RESIDUAL, then HELD while the
    amplitude is fitted band by band.  Recovers the known input's period to 0.24% and its amplitude to
    3.74%, and ** the gate refuses to print a measurement if it does not. **
  ⌗ That is `cc66.60`'s error -- the instrument not matching the question's grain -- for the third time in
  this row, and the first time it was caught before a number was reported rather than after.
"""
import os
import sys

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
ED = np.arange(0.85, 5.76, 0.7)
LO, HI = 0.85, 5.75
GATE_TOL = 0.05                      # the known input must come back to 5%


def env_a(x, y, win=1.0):
    """r6911+cc66.40's running arithmetic mean -- that receipt's statistic, unchanged"""
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
    m = (q >= LO) & (q <= HI)
    x, y = q[m], o[m]
    return min(((_fit(x, y, T)[1], T) for T in pers))[1]


def band_amp(q, o, a, b, T):
    m = (q >= a) & (q <= b)
    return _fit(q[m], o[m], T)[0]


def acceptance(d, tag, step=2):
    """G_l(k), the acceptance weight W, and A_l -- read off the SAVED transfer"""
    ls = d[f'ls__{tag}'].astype(int)[::step]
    k = d[f'k__{tag}']
    ee, x0, v = d[f'eta__{tag}'], d[f'x0__{tag}'], d[f'vis__{tag}']
    RS, ns = float(d[f'r_s__{tag}']), float(d[f'ns__{tag}'])
    Dlk = d[f'Dlk__{tag}'][::step]
    dk = np.gradient(k)
    A = np.full(len(ls), np.nan)
    dkw = np.full(len(ls), np.nan)
    res = np.full(len(ls), np.nan)
    for i, l in enumerate(ls):
        J = spherical_jn(int(l), k[None, :] * x0[:, None])
        G = np.trapezoid(v[:, None] * J, ee, axis=0)
        mx = np.max(np.abs(Dlk[i]))
        if mx > 0:
            pred = np.cos(k * RS) * k ** (0.5 * (1 - ns)) * G
            res[i] = np.max(np.abs(pred - Dlk[i])) / mx
        W = G ** 2 * dk / k
        s = W.sum()
        if s > 0:
            A[i] = abs(np.sum(W * np.exp(2j * k * RS))) / s
            kb = np.sum(W * k) / s
            dkw[i] = 2 * np.sqrt(max(np.sum(W * (k - kb) ** 2) / s, 0.0))
    return dict(q=ls / float(d[f'l_A__{tag}']), A=A, dkw=dkw, res=res, RS=RS)


def main():
    need = [f'r7039_transfer_{t}.npz' for t in ('lcdm', 'cr')]
    for n in need:
        if not os.path.exists(os.path.join(SP, n)):
            print(f"  ⛔ the transfer bank `spectra/{n}` is not on disk.  It is deliberately NOT")
            print("     tracked (see `.gitignore`): 15.5 MB against 359 kB for the largest tracked")
            print("     bank.  Regenerate with `r7039_directions/launch.sh` then its `bank.py`.")
            return 1
    T = {t: np.load(os.path.join(SP, n)) for t, n in zip(('lcdm', 'cr'), need)}
    print(__doc__)
    print("=" * 104)

    # ⓪ the instrument's gate, on a KNOWN input, before any measurement is printed
    d = T['lcdm']
    q = d['ls__fixed'].astype(float) / float(d['l_A__fixed'])
    E = env_a(q, np.asarray(d['Dl__fixed'], float))
    A0, P0, PH0 = 0.5, 1.0347, 0.7
    syn = osc(q, E * (1.0 + A0 * np.cos(2 * np.pi * q / P0 + PH0)))
    Tg = fit_period(q, syn)
    rec = [band_amp(q, syn, a, b, Tg) for a, b in zip(ED[:-1], ED[1:])]
    err = max(abs(A - A0) for A in rec) / A0
    print(f"  ⓪ THE GATE: a synthetic comb of amplitude {A0:.4f} at period {P0}, phase {PH0} rad")
    print(f"     period recovered {Tg:.4f} ({abs(Tg-P0)/P0*100:.2f}%);  amplitudes "
          + ", ".join(f"{A:.4f}" for A in rec))
    print(f"     worst amplitude error {err*100:.2f}% against a {GATE_TOL*100:.0f}% tolerance")
    if err > GATE_TOL:
        print("     ⛔ THE INSTRUMENT DOES NOT RECOVER A KNOWN INPUT.  Nothing further is printed:")
        print("        a measurement from an ungated statistic is what attempts ① and ② produced.")
        return 1
    print("     ✔ gated.  The measurement below is read.")
    print()

    AC = {}
    for t in ('lcdm', 'cr'):
        AC[t] = acceptance(T[t], 'fixed')
        m = np.isfinite(AC[t]['res'])
        print(f"  {t}: the factorisation is EXACT -- residual max "
              f"{np.nanmax(AC[t]['res']):.2e} over {m.sum()} multipoles")
    print()
    for t in ('lcdm', 'cr'):
        a_ = AC[t]
        mm = (a_['q'] >= LO) & (a_['q'] <= HI) & np.isfinite(a_['dkw'])
        print(f"  {t}: the acceptance spans 2 r_s* dk = "
              f"{(2*a_['RS']*a_['dkw'])[mm].mean():.4f} of acoustic phase")
    aa = AC['cr'], AC['lcdm']
    sp = [(2 * x['RS'] * x['dkw'])[(x['q'] >= LO) & (x['q'] <= HI) & np.isfinite(x['dkw'])].mean()
          for x in aa]
    print(f"    ⇒ the arm's is {(1-sp[0]/sp[1])*100:.1f}% narrower, against r6919's dr_s/dchi "
          f"0.454950 -> 0.396733, which is 12.8% lower")
    print()
    print("  THE LAW FORWARD, ABSOLUTE, NO FITTED COEFFICIENT")
    print(f"    {'band':>12s} {'lcdm law':>9s} {'lcdm meas':>10s} {'ratio':>7s}   "
          f"{'cr law':>9s} {'cr meas':>9s} {'ratio':>7s}")
    for a, b in zip(ED[:-1], ED[1:]):
        row = []
        for t in ('lcdm', 'cr'):
            d = T[t]
            qq = d['ls__fixed'].astype(float) / float(d['l_A__fixed'])
            oo = osc(qq, np.asarray(d['Dl__fixed'], float))
            Tf = fit_period(qq, oo)
            m = (AC[t]['q'] >= a) & (AC[t]['q'] <= b) & np.isfinite(AC[t]['A'])
            law = float(AC[t]['A'][m].mean())
            mea = band_amp(qq, oo, a, b, Tf)
            row += [law, mea, law / mea]
        print(f"    {a:5.2f}-{b:5.2f} {row[0]:9.4f} {row[1]:10.4f} {row[2]:7.3f}   "
              f"{row[3]:9.4f} {row[4]:9.4f} {row[5]:7.3f}")
    print()
    print("  ⌗ The gate's own accuracy on a known input is 3.74%, so a band agreeing to better than")
    print("    that is agreeing to within the instrument and no tighter claim is made for it.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
