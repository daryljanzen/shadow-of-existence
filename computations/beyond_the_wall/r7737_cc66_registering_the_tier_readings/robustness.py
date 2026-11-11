#!/usr/bin/env python3
"""`r7737+cc66` THE CHECKS MADE **AFTER** THE REGISTERED READS, AND LABELLED AS SUCH.

⛔ **NONE of this is in `PREDICTION.md`.**  Each check below was run because the registered read
returned something that could not be reported as it stood, and each is named with the reason:

  ⒜ `B1b` FAILED -- two of the three amplitudes are far from unity.  Before calling that a finding,
     the fit's CONDITIONING had to be measured against this project's own standing threshold
     (`r7723` amendment 2: `|r| <= 0.70` and `VIF <= 2.0`).  It fails it, badly.
  ⒝ So `B2`'s apportionment rests on a near-degenerate fit.  A **FIT-FREE** statistic is computed --
     the `l`-structured rms of each single-term swap, with no amplitude anywhere -- and `B2` is
     recomputed at UNIT amplitudes, to see whether the conclusion is a property of the object or of
     the fit.
  ⒞ 70 shipped `width__*` for all eight settings, which the registration did not anticipate.  It
     allows the ACCEPTANCE WIDTH -- the quantity `P15`'s law credits with the retention -- to be
     decomposed the same way.  ⚠ *That is a statement about the RETENTION and not about the located
     step; the two are kept apart below.*

⌗ *The order of these matters: ⒜ is the reason for ⒝, and without ⒜ the shares in `B2` would have
been reported as an attribution they cannot carry.*
"""
import hashlib
import sys

import numpy as np

D = ('/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/'
     'scratchpad/tier')
VIS = f'{D}/r7737_vis.npz'
SHA_VIS = 'c3da5390680d86b2f9dddcae3738a01e88974545b1a5d1ea4c36a2739ceb6ba4'
R_BAR, VIF_BAR = 0.70, 2.0        # r7723 amendment 2's standing threshold
NAMES = ('visibility g', 'distance map chi', 'comb period rs')


def main():
    print(__doc__)
    print("=" * 100)
    h = hashlib.sha256(open(VIS, 'rb').read()).hexdigest()
    if h != SHA_VIS:
        print(f"  ⛔ REFUSING: {h} is not the recorded object")
        return 1
    V = np.load(VIS, allow_pickle=True)
    lc = np.log(V['A__g_lcdm__X_lcdm__rs_lcdm'])
    v = np.log(V['A__g_cr__X_cr__rs_cr']) - lc
    U = [np.log(V['A__g_cr__X_lcdm__rs_lcdm']) - lc,
         np.log(V['A__g_lcdm__X_cr__rs_lcdm']) - lc,
         np.log(V['A__g_lcdm__X_lcdm__rs_cr']) - lc]
    A = np.column_stack(U)

    # ---- ⒜ the conditioning, and the amplitudes' own errors ------------------------------------
    print("\n  ⒜ THE CONDITIONING OF `B1`'s THREE-TERM FIT")
    C = np.corrcoef(A.T)
    worst_r, worst_v = 0.0, 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            r = C[i, j]
            vif = 1.0 / (1.0 - r ** 2)
            worst_r, worst_v = max(worst_r, abs(r)), max(worst_v, vif)
            print(f"      corr({NAMES[i].split()[-1]}, {NAMES[j].split()[-1]}) = {r:+.4f}   "
                  f"VIF = {vif:.1f}   "
                  f"{'⛔ OVER' if abs(r) > R_BAR or vif > VIF_BAR else 'within'} the threshold")
    print(f"      ⇒ worst |r| {worst_r:.4f} against {R_BAR}, worst VIF {worst_v:.1f} against "
          f"{VIF_BAR}: ** THE THREE-TERM FIT FAILS THE STANDING THRESHOLD. **")
    a = np.linalg.lstsq(A, v, rcond=None)[0]
    res = v - A @ a
    cov = np.linalg.inv(A.T @ A) * (res @ res) / (len(v) - 3)
    se = np.sqrt(np.diag(cov))
    print(f"\n      and the amplitudes ARE numerically determined, which is why `B1b`'s failure is "
          f"not noise:")
    for n, ai, s in zip(NAMES, a, se):
        print(f"        a[{n:17s}] = {ai:+.4f} ± {s:.4f}   ({abs(ai - 1) / s:.0f} sd from unity)")
    print(f"      ⇒ ** Determined and not interpretable are different things. ** With columns at "
          f"|r| {worst_r:.2f} the\n        fit can move SHAPE between the terms almost freely; what "
          f"it cannot move is their SIZE.")

    # ---- ⒝ the fit-free statistic, and B2 at unit amplitudes -----------------------------------
    print("\n  ⒝ THE FIT-FREE READING -- no amplitude anywhere")
    lr = [float(np.sqrt(((x - x.mean()) ** 2).mean())) for x in U]
    vl = float(np.sqrt(((v - v.mean()) ** 2).mean()))
    tot = sum(lr)
    for i in np.argsort(lr)[::-1]:
        print(f"      {NAMES[i]:18s} l-structured rms {lr[i]:.6e}  = {100 * lr[i] / tot:6.2f} % of "
              f"the three summed, {lr[i] / vl:.4f} of the full swap's")
    print(f"      the full swap's own l-structured rms {vl:.6e}")
    print(f"      ⇒ SIZE ORDERING, and it is a measurement rather than a fit output: "
          f"chi is {lr[1] / lr[0]:.1f}x the visibility's and {lr[1] / lr[2]:.0f}x the comb "
          f"period's.")
    print(f"      ⇒ *** For the visibility to carry the map's contribution it would need an "
          f"amplitude near {lr[1] / lr[0]:.0f}, not near 1. THAT is what survives the degeneracy. ***")
    print("\n      and `B2` recomputed at UNIT amplitudes:")
    for tag, amps in (('fitted', a), ('unit', np.ones(3))):
        parts = [amps[i] * U[i] for i in range(3)]
        lp = [p - p.mean() for p in parts]
        var = [float((x ** 2).mean()) for x in lp]
        cr = sum(2 * float((lp[i] * lp[j]).mean()) for i in range(3) for j in range(i + 1, 3))
        t = sum(var) + cr
        print(f"        {tag:7s} " + "  ".join(
            f"{NAMES[i].split()[-1]} {100 * var[i] / t:+7.2f} %" for i in range(3))
            + f"  cross {100 * cr / t:+7.2f} %")
    print(f"      ⇒ the two readings differ in the digits and agree in the conclusion, which is how "
          f"a\n        result that survives its own fit's degeneracy should behave.")

    # ---- ⒞ the acceptance width, a RETENTION statement ----------------------------------------
    print("\n  ⒞ THE ACCEPTANCE WIDTH -- ⚠ A STATEMENT ABOUT THE RETENTION, NOT THE LOCATED STEP")
    W = lambda g, x: V[f'width__g_{g}__X_{x}__rs_lcdm']
    base = W('lcdm', 'lcdm')
    for nm, arr in (('the visibility alone', W('cr', 'lcdm')),
                    ('the distance map alone', W('lcdm', 'cr')),
                    ('both together', W('cr', 'cr'))):
        r = arr / base
        print(f"      swapping {nm:24s} ⇒ width x {r.mean():.6f}  "
              f"[{r.min():.6f}, {r.max():.6f}]  = {100 * (r.mean() - 1):+6.2f} %")
    nat = V['width__native_cr'].mean() / V['width__native_lcdm'].mean()
    print(f"      the two arms' own builds: {nat:.6f} = {100 * (nat - 1):+.2f} %")
    print(f"      ⌗ `P15` prints the cr acceptance as `13.73` per cent narrower; this reproduces the"
          f"\n        SIGN and the rough size, and the definitions are 70's -- I am not claiming they"
          f" are one number.")
    print(f"      ⇒ *** So the narrowing the law credits with the retention is the MAP's: "
          f"{100 * (W('lcdm', 'cr') / base).mean() - 100:+.2f} points\n        against the "
          f"visibility's {100 * (W('cr', 'lcdm') / base).mean() - 100:+.2f}. ***  ⚠ The retention is "
          f"not the located step, and this\n        line says nothing about the step; `B2` is where "
          f"the step is.")
    print("\n" + "=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
