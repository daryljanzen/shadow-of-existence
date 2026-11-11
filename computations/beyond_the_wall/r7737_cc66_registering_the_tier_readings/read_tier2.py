#!/usr/bin/env python3
"""`r7737+cc66` TIER 2 READ — the registered Part B, run on 70's `r7737_vis`.

⛭ `PREDICTION.md` Part B, registered and pushed at `r7737+cc66.0` before this build existed.
   `B0` is a PRECONDITION: if the located transition does not show in `log A_l`'s own swap, Part B
   answers a different question than `PO-87`'s last step, and `B2` is NOT run.

⛔ ONE CHOICE IS MADE HERE AND IS DECLARED AS MADE NOW, NOT REGISTERED.  `B0` said "the step statistic
   `P15` already uses, read on `log A_l`".  That statistic is defined on a curve of BAND RMS against a
   window centre in comb multiples; `A_l` is one value per multipole.  ⇒ The transposition used is the
   minimal faithful one: read `log A_l`'s swap at `q = l / l_A`, average it over the SAME sliding
   windows at the SAME three half-widths, and take the SAME low-band/high-band difference over the
   same band edges, against `r7721`'s own phase-randomised step-free null.  *Declared because it was
   not in the registration; nothing else about `B0` is changed, and its licence `p <= 0.01` is not
   moved.*
"""
import hashlib
import json
import os
import sys

import numpy as np

D = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
     'scratchpad/tier')
VIS = os.path.join(D, 'r7737_vis.npz')
SHA_VIS = 'c3da5390680d86b2f9dddcae3738a01e88974545b1a5d1ea4c36a2739ceb6ba4'
GRID = (0.85, 3.0, 0.05)          # r7721's window centres, in comb multiples
LO, HI = 1.4, 2.2                 # r7721's band edges
HALVES = (0.175, 0.25, 0.35)      # r7721's three half-widths
N_NULL = 20000                    # floors p at 5.0e-05, far below B0's 0.01 licence
B0_P = 0.01                       # registered
B1A = 0.20                        # registered: the interaction residual
B1B = 0.10                        # registered: each amplitude within this of unity
B2_LINE = 0.60                    # registered: one term above this closes PO-87 on that term
SEED = 7737
FAILS = []


def gate(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def curve(q, y, half):
    cs = np.arange(GRID[0] + half, GRID[1], GRID[2])
    out = np.array([y[(q >= c - half) & (q <= c + half)].mean()
                    if ((q >= c - half) & (q <= c + half)).any() else np.nan for c in cs])
    ok = np.isfinite(out)
    return cs[ok], out[ok]


def step(cs, R):
    lo, hi = cs < LO, cs > HI
    if not lo.any() or not hi.any():
        return np.nan
    return float(R[hi].mean() - R[lo].mean())


def surrogate_steps(cs, R, n, rng):
    """`r7721`'s null: remove a least-squares line across ALL centres -- which makes the surrogate
    step-free BY CONSTRUCTION -- then randomise phases, keeping the amplitude spectrum and so the
    scatter and the autocorrelation exactly."""
    resid = R - np.polyval(np.polyfit(cs, R, 1), cs)
    amp = np.abs(np.fft.rfft(resid))
    L = len(resid)
    lo, hi = cs < LO, cs > HI
    ph = rng.uniform(0, 2 * np.pi, (n, len(amp)))
    ph[:, 0] = 0.0
    if L % 2 == 0:
        ph[:, -1] = 0.0
    s = np.fft.irfft(amp[None, :] * np.exp(1j * ph), n=L, axis=1)
    return s[:, hi].mean(1) - s[:, lo].mean(1)


def main():
    print(__doc__)
    print("=" * 100)
    h = hashlib.sha256(open(VIS, 'rb').read()).hexdigest()
    gate('input', h == SHA_VIS, "r7737_vis.npz is the object 70 recorded", h)
    if FAILS:
        return 1
    V = np.load(VIS, allow_pickle=True)
    meta = json.loads(str(V['meta'].item()))
    cl = meta['closure']
    lA = cl['l_A']
    print(f"\n    70's closures: T2_C1 lcdm max_rel {cl['T2_C1_lcdm']['max_rel']:.3e}, "
          f"cr G identical {cl['T2_C1_cr']['G_identical']}, "
          f"T2_C2 {cl['T2_C2']['identical']} of {cl['T2_C2']['checked']} identical")
    print(f"    the arms' visibility widths: lcdm {cl['W']['lcdm']:.6f}, cr {cl['W']['cr']:.6f} "
          f"⇒ the cr arm is {100 * (cl['W']['cr'] / cl['W']['lcdm'] - 1):.2f} % wider")
    print(f"      ⌗ P15 prints `15.5` per cent for that, and this is 70's independent build of it.")
    print(f"    the sound horizons: lcdm {cl['r_s']['lcdm']:.6f}, cr {cl['r_s']['cr']:.6f} "
          f"⇒ {100 * (cl['r_s']['cr'] / cl['r_s']['lcdm'] - 1):.3f} % apart")

    ls = V['ls'].astype(float)
    CTL = 'A__g_lcdm__X_lcdm__rs_lcdm'
    FULL = 'A__g_cr__X_cr__rs_cr'
    with np.errstate(divide='ignore', invalid='ignore'):
        lA_ctl = np.log(V[CTL])
        v = np.log(V[FULL]) - lA_ctl
        u_g = np.log(V['A__g_cr__X_lcdm__rs_lcdm']) - lA_ctl
        u_x = np.log(V['A__g_lcdm__X_cr__rs_lcdm']) - lA_ctl
        u_r = np.log(V['A__g_lcdm__X_lcdm__rs_cr']) - lA_ctl
    live = np.isfinite(v) & np.isfinite(u_g) & np.isfinite(u_x) & np.isfinite(u_r)
    print(f"\n    live multipoles {int(live.sum())} of {ls.size}")
    q = ls / lA['lcdm']

    # ---------------------------------------------------------------- B0, the precondition
    print(f"\n    ⛭ B0 -- DOES THE LOCATED TRANSITION SHOW IN `log A_l`'s OWN SWAP?")
    rng = np.random.default_rng(SEED)
    ps, rows = [], []
    for half in HALVES:
        cs, R = curve(q[live], v[live], half)
        st = step(cs, R)
        ss = surrogate_steps(cs, R, N_NULL, rng)
        n_ge = int((np.abs(ss) >= abs(st)).sum())
        p = (n_ge + 1) / (N_NULL + 1)
        ps.append(p)
        rows.append((half, len(cs), st, float(ss.std(ddof=1)), n_ge, p))
        print(f"        half {half}: {len(cs)} centres, step {st:+.6f}, surrogate sd "
              f"{ss.std(ddof=1):.6f}, {n_ge} of {N_NULL} reach it ⇒ p {p:.3e}")
    b0 = gate('B0', all(p <= B0_P for p in ps),
              f"the located transition shows in `log A_l`'s swap at every half-width, "
              f"p <= {B0_P}",
              "; ".join(f"h{h}: p {p:.3e}" for (h, _, _, _, _, p) in rows))

    if not b0:
        print("\n" + "=" * 100)
        print("  ⛔ B0 FAILED, AND THE REGISTRATION SAYS WHAT THAT MEANS:")
        print("     `A_l` does NOT carry the located step, so TIER 2 ANSWERS A DIFFERENT QUESTION")
        print("     than `PO-87`'s last step.  B2 is NOT run, and no named term is credited with")
        print("     carrying a step it has not been shown to carry.  `PO-87` stays open.")
        print("=" * 100)
        # B1 is still reported, because it is a statement about A_l and makes no step claim
    # ---------------------------------------------------------------- B1, the three-term fit
    print(f"\n    ⛭ B1 -- THE THREE-TERM DECOMPOSITION OF `log A_l`'s SWAP (a statement about `A_l`)")
    A = np.column_stack([u_g[live], u_x[live], u_r[live]])
    a = np.linalg.lstsq(A, v[live], rcond=None)[0]
    pred = A @ a
    r1 = float(np.sqrt(((v[live] - pred) ** 2).mean()) / np.sqrt((v[live] ** 2).mean()))
    gate('B1a', r1 <= B1A, f"the interaction residual is within the registered {B1A}",
         f"rms(v - fit)/rms(v) = {r1:.4f}")
    names = ('visibility g', 'distance map chi', 'comb period rs')
    gate('B1b', all(abs(x - 1.0) <= B1B for x in a),
         f"each amplitude is within {B1B} of unity",
         ", ".join(f"{n}: {x:+.4f}" for n, x in zip(names, a)))
    sizes = [abs(a[i]) * float(np.sqrt((A[:, i] ** 2).mean())) for i in range(3)]
    order = np.argsort(sizes)[::-1]
    print(f"        B1c the ORDERING plus the three sizes, which is the licence and not a name:")
    for i in order:
        print(f"            {names[i]:18s} |a| x rms  {sizes[i]:.6f}   "
              f"(a {a[i]:+.4f}, template rms {np.sqrt((A[:, i] ** 2).mean()):.6f})")

    # ---------------------------------------------------------------- B2, only if B0 passed
    if b0:
        print(f"\n    ⛭ B2 -- THE MULTIPOLE STRUCTURE TERM BY TERM — `PO-87`'s QUESTION AS WORDED")
        parts = [a[i] * A[:, i] for i in range(3)]
        mean = [p.mean() for p in parts]
        lp = [p - m for p, m in zip(parts, mean)]
        var = [float((x ** 2).mean()) for x in lp]
        cross = 0.0
        for i in range(3):
            for j in range(i + 1, 3):
                cross += 2 * float((lp[i] * lp[j]).mean())
        tot = sum(var) + cross
        for i in order:
            print(f"            {names[i]:18s} {100 * var[i] / tot:+7.2f} % of the l-structured "
                  f"variance")
        print(f"            {'cross terms':18s} {100 * cross / tot:+7.2f} %")
        top = max(range(3), key=lambda i: var[i] / tot)
        if var[top] / tot > B2_LINE:
            print(f"\n        ⇒ ONE TERM ABOVE {B2_LINE}: **{names[top]}** carries the located step's")
            print(f"          multipole structure, at {100 * var[top] / tot:.2f} %.  `PO-87`'s last "
                  f"step CLOSES on that term.")
        else:
            print(f"\n        ⇒ NO term above {B2_LINE} (largest {names[top]} at "
                  f"{100 * var[top] / tot:.2f} %): the structure is SHARED, and `PO-87` closes on "
                  f"the shares rather than on a name.")
    print("\n" + "=" * 100)
    print(f"  {'OK' if not FAILS else '⛔'}  {4 - len(FAILS)} of 4 registered checks"
          + ("" if not FAILS else f";  not met: {', '.join(FAILS)}"))
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
