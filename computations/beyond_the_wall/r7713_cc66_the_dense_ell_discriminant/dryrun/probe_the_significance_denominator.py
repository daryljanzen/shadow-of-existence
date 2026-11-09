"""⛔ A PROBE, NOT A CHANGE.  Does the registered slide's significance saturate because its scatter
   includes the gradient it is measuring?  And would estimating the scatter about a straight line
   inside each band group fix that WITHOUT manufacturing significance where there is none?

   Nothing here is written into the instrument.  The question goes to 69.
"""
import os
import sys

import numpy as np

ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
import own_comb_kinds as OCK                                                 # noqa: E402

LA = 301.5427
LS = np.arange(int(np.ceil(0.80 * LA)), int(np.floor(3.10 * LA)) + 1)
Q = LS / LA
rng = np.random.default_rng(7713)
base = lambda q: 1e-6 * (1.0 + 0.4 * np.cos(2 * np.pi * q)) * np.exp(-0.15 * q)


def both(xa, ya, xc, yc, h=0.35):
    st = OCK.own_state({'lcdm': (xc, yc), 'cr': (xa, ya)}, 'mean', 1.0)
    cs = np.arange(0.85 + h, 3.0, 0.05)
    R = np.array([OCK._rms(st['ua'], st['oa'], c - h, c + h)
                  / OCK._rms(st['xc'], st['oc'], c - h, c + h) - 1.0 for c in cs])
    lo, hi = cs < 1.4, cs > 2.2
    L, H = R[lo], R[hi]
    step = H.mean() - L.mean()
    # ① AS REGISTERED: the within-group variance, which a gradient traversing the group inflates
    sd_reg = np.sqrt((L.var(ddof=1) + H.var(ddof=1)) / 2)
    # ② THE CANDIDATE: the scatter ABOUT A STRAIGHT LINE inside each group, so a trend inside the
    #    group is not counted as uncertainty about the group's LEVEL, which is what the step compares
    def res(c, r):
        if len(r) < 3:
            return np.nan
        return (r - np.polyval(np.polyfit(c, r, 1), c)).std(ddof=2)
    sd_alt = np.sqrt((res(cs[lo], L) ** 2 + res(cs[hi], H) ** 2) / 2)
    return step, sd_reg, sd_alt, len(L), len(H)


def run(tag, f_ker, f_src, noise):
    y00 = base(Q)
    n = lambda: 1.0 + noise * rng.standard_normal(len(Q))
    ker, src = f_ker(Q), f_src(Q)
    d = {'lcdm|lcdm': y00 * n(), 'cr|lcdm': y00 * ker * n(),
         'lcdm|cr': y00 * src * n(), 'cr|cr': y00 * ker * src * n()}
    print(f"\n  {tag}   (noise {noise})")
    print("    ratio            step        sd(registered)  sd(candidate)   as-registered  candidate")
    for nm, (a, c) in (('own x own  ', ('cr|cr', 'lcdm|lcdm')),
                       ('kernel only', ('cr|lcdm', 'lcdm|lcdm')),
                       ('source only', ('lcdm|cr', 'lcdm|lcdm'))):
        s, r, al, nl, nh = both(Q, d[a], Q, d[c])
        print(f"    {nm}   {s:+.5f}    {r:.6f}        {al:.6f}      "
              f"{abs(s) / r:8.2f} sd  {abs(s) / al:8.2f} sd")


run('A  kernel dominant, source opposite', lambda q: 1 + 0.12 * (q - 1), lambda q: 1 - 0.06 * (q - 1), 0.0004)
run('A  the same, five times the noise  ', lambda q: 1 + 0.12 * (q - 1), lambda q: 1 - 0.06 * (q - 1), 0.002)
run('B  THE NULL: no planted difference ', lambda q: 1 + 0 * q, lambda q: 1 + 0 * q, 0.002)
run('B  THE NULL at the lower noise     ', lambda q: 1 + 0 * q, lambda q: 1 + 0 * q, 0.0004)
