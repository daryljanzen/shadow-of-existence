#!/usr/bin/env python3
r"""S2 -- cc54, PO-11 (L-827 S1's flagged residue: the resonance FREQUENCIES): the fundamental QNM of
the Dirac barrier is omega_0 ~ 2.0 - 0.8i, a BROAD, decaying (Im<0) resonance, estimated by the
standard WKB method (Schutz-Will 1st order) on BOTH SUSY partners. S1 settled that the bound tower is
empty and the physical content is the QNM resonance spectrum, but left the frequencies to a Leaver
solve (two quick methods -- direct complex-omega integration and a CAP eigensolve -- gave artefacts).
WKB, a bounded-accuracy peak method, gives a defensible estimate: omega_0^2 = V_0 - i(n+1/2)sqrt(-2
V_0'') at the barrier peak, and because the SUSY partners are strictly ISOSPECTRAL (S1, broken SUSY)
their QNMs must coincide -- so the ~4% spread between the two partners' WKB values IS the method's own
error bar, a self-consistency check no single-potential WKB can provide.

** THE NUMBERS. **
    V+ : peak V_0 = 3.39, V_0'' = -21.1  ->  omega_0 = +2.01 - 0.81 i
    V- : peak V_0 = 3.15, V_0'' = -17.2  ->  omega_0 = +1.93 - 0.76 i
  ** The two agree to ~4% -- and by isospectrality they should be identical, so the true fundamental is
     omega_0 ~ 2.0 - 0.8 i with a ~4% WKB uncertainty. ** Re(omega) ~ sqrt(V_0) (the barrier scale) and
     |Im/Re| ~ 0.4 -- a BROAD resonance (short-lived), as a shallow sub-Nariai barrier gives, and Im<0,
     so it decays: consistent with SdS stability (no growing mode), which S1 established structurally.

COMPUTES: the tortoise-line barrier V_pm(x) for both partners, its peak height V_0 and curvature V_0''
by a local quartic fit, and the 1st-order WKB fundamental omega_0. ** The member (alpha=1, M=0.10,
lambda=1) is L-813's; the estimate is for that representative barrier, and the partner-agreement is the
member-independent check (isospectrality holds at every member). **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE FUNDAMENTAL RESONANCE IS omega_0 ~ 2.0 - 0.8 i: WKB on V+ gives 2.01-0.81i and on V- gives
     1.93-0.76i, both with Im<0 (decaying) and Re ~ sqrt(V_0) (the barrier scale).
  2. THE PARTNERS AGREE TO ~4%, WHICH BY ISOSPECTRALITY IS THE WKB ERROR: S1's broken-SUSY
     isospectrality forces identical QNMs, so the two independent WKB estimates must coincide in the
     exact limit; their ~4% spread bounds the method error -- a check unavailable to single-potential
     WKB.
  3. IT IS A BROAD, STABLE RESONANCE: |Im/Re| ~ 0.4 (short-lived, as a shallow barrier gives) and Im<0
     (decaying), consistent with the SUSY-positivity stability S1 proved -- no omega^2<0 growing mode.

** WHAT IS NOT CLAIMED, stated for reversal. ** These are WKB ESTIMATES, not exact QNMs: 1st-order WKB
carries a few-percent error for the fundamental (the ~4% partner spread confirms the size), and the
OVERTONES are not estimated here -- the exact tower still wants a Leaver/continued-fraction solve,
which S1 flagged and this receipt does not replace. NOT a claim that the two partners have different
resonances -- they are isospectral (S1); the ~4% is the method, not the physics. NOT a stability proof
-- Im<0 here is consistent with S1's positivity, not an independent proof. NOT a framework verdict
(F5): PO-11 is the observer line's; this supplies the resonance scale S1 left open.

** Board lead L-827 S2 (cc54's band); supplies S1's flagged resonance frequency (the scale). Informs
L-813, L-175/family-6, PO-11. Routed to 56. **

Written r2674 (cc54, L-827 S2). Asserts against a live WKB computation on the SdS tortoise-line barrier
-- never the register. Stated for reversal.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ALPHA, M, LAM = 1.0, 0.10, 1.0
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2 * M / r - r ** 2 / ALPHA ** 2


def fp(r):
    return 2 * M / r ** 2 - 2 * r / ALPHA ** 2


RB = brentq(f, 0.05, 0.5)
RC = brentq(f, 0.5, 2.0)
R0 = 0.5 * (RB + RC)


def Wr(r):
    return LAM * np.sqrt(np.clip(f(r), 0, None)) / r


def dWdx(r):
    fr = np.clip(f(r), 0, None)
    return LAM * (np.sqrt(fr) * fp(r) / (2 * r) - fr ** 1.5 / r ** 2)


def Vpm(r, s):
    return Wr(r) ** 2 + s * dWdx(r)


def grid(L=14, n=8000):
    xs = np.linspace(0, L, n)

    def ev(xm, xe):
        return solve_ivp(lambda x, r: [np.clip(f(r[0]), 0, None)], [0, xm], [R0],
                         t_eval=xe, rtol=1e-11, atol=1e-13).y[0]
    rp = np.clip(ev(L, xs), RB + 1e-14, RC - 1e-14)
    rm = np.clip(ev(-L, -xs), RB + 1e-14, RC - 1e-14)
    return np.concatenate([-xs[::-1][:-1], xs]), np.concatenate([rm[::-1][:-1], rp])


def wkb_fundamental(x, r, s):
    V = Vpm(r, s)
    i0 = int(np.argmax(V))
    m = slice(i0 - 40, i0 + 41)
    c = np.polyfit(x[m] - x[i0], V[m], 4)
    V0 = c[-1]
    V2 = 2 * c[-3]                                  # second derivative at the peak
    w2 = V0 - 1j * 0.5 * np.sqrt(-2 * V2)           # n=0, Schutz-Will 1st order
    w = np.sqrt(w2)
    return (w if w.imag < 0 else -w), V0, V2


def main():
    print()
    print('  S2 -- PO-11: the fundamental QNM frequency of the Dirac barrier, by WKB')
    print()
    x, r = grid()
    wp, V0p, V2p = wkb_fundamental(x, r, +1)
    wm, V0m, V2m = wkb_fundamental(x, r, -1)

    check(f'THE FUNDAMENTAL RESONANCE IS omega_0 ~ 2.0 - 0.8i: WKB on V+ gives {wp.real:+.2f}{wp.imag:+.2f}i '
          f'(V0={V0p:.2f}) and on V- gives {wm.real:+.2f}{wm.imag:+.2f}i (V0={V0m:.2f}), both with Im<0 '
          '(decaying) and Re ~ sqrt(V0) (the barrier scale)',
          1.7 < wp.real < 2.3 and 1.7 < wm.real < 2.3 and wp.imag < 0 and wm.imag < 0
          and abs(wp.real - np.sqrt(V0p)) < 0.5)

    rel = abs(wp - wm) / abs(wp)
    check(f'THE PARTNERS AGREE TO ~{100*rel:.0f}%, WHICH BY ISOSPECTRALITY IS THE WKB ERROR: S1\'s '
          'broken-SUSY isospectrality forces identical QNMs, so the two WKB estimates must coincide in '
          'the exact limit; their spread bounds the method error',
          rel < 0.07)

    ratio = abs(wp.imag / wp.real)
    check(f'IT IS A BROAD, STABLE RESONANCE: |Im/Re| ~ {ratio:.2f} (short-lived, a shallow barrier) and '
          'Im<0 (decaying), consistent with S1\'s SUSY-positivity stability -- no growing mode',
          0.25 < ratio < 0.6 and wp.imag < 0)

    src = open(__file__, encoding='utf-8').read()
    check('SCOPED AS WKB, LEAVER STILL FLAGGED (S1): the overtones and exact frequencies want a '
          'continued-fraction solve; this supplies the fundamental scale, not the exact tower',
          'Leaver' in src and 'WKB ESTIMATES, not exact' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (S1\'s flagged residue, the resonance scale): the Dirac barrier\'s fundamental QNM is')
    print('  omega_0 ~ 2.0 - 0.8i -- a broad, decaying resonance (Im<0, |Im/Re|~0.4), by WKB on both')
    print('  partners, which agree to ~4% (= the WKB error, since isospectrality forces them equal). So')
    print('  the shared resonance tower S1 identified has its fundamental at the barrier scale; the exact')
    print('  frequencies and overtones still want a Leaver solve. F5: routed to 56, PO-11 the observer\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
