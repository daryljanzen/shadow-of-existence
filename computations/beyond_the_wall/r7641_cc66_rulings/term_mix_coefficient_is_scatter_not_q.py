#!/usr/bin/env python3
r"""r7641+cc66 -- ** ⑹'s PREMISE IS WRONG ABOUT THE MECHANISM, AND THE CLAIM IT WOULD HAVE RETIRED
SURVIVES. **

`r7641` ⑹ says: *"A coefficient spread of 8.3% against the 5% the condition enforces is a
q-dependence, and that is a result.  Report what it says, and the sentence it changes, with
wording."*

** THE SPREAD IS REAL.  THE q-DEPENDENCE IS NOT. **  Re-pointing the term-mix receipt onto the arm of
record takes the Doppler coefficient the eta-window profiles demand from a `4.3` per cent band-to-band
spread to `8.3`, so the registered condition -- *"the same in every band to FIVE per cent"* -- fails.
But the condition was protecting a claim about SHAPE: *"a single scalar on the Doppler and not a
q-dependent reshaping"*.  ⇒ *Tested directly, the coefficient has no trend in wavenumber at all:*

    against q     slope +0.00046 +- 0.00721   -> 0.06 sigma
    against q^2   slope +0.00025 +- 0.00107   -> 0.24 sigma

and the fitted trend spans `0.002`--`0.007` across the whole range against a spread of `0.069`, so a
trend accounts for three to ten per cent of what is there.  The successive differences alternate
(`- - + - - +`), which is scatter and not a reshaping.

⇒ *** So the registered tolerance fails on SCATTER, and the claim it was registered to protect is
still true -- there is no q-dependent reshaping because there is no q-dependence.  What moved is how
tightly "one constant" can be asserted: to eight per cent, not two. ***

⌗ *And the paper's neighbouring clause -- "the response is independent of wavenumber, an intercept
against a slope worth three per cent of it" -- does not move AT ALL, because it is measured on the
TAPERED CONTROLS (`r6975_mix{,b}_lcdm`) and the carry is the identity there.  The arm enters that
clause only through the excess it is compared against.*

Exits 1 if the namesake spread is not reproduced, if the arm-of-record spread is not the 8.3 per cent
reported, or if either trend reaches one sigma.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

NF = 3.0
TERMS = ('w2sw', 'w2dp', 'w2isw', 'w2pol')
CTL, NSK, AOR = 'r6959_eta_lcdm', 'r6959_eta_cr', 'r6959_eta_cr_leafrec1'
NSK_SPREAD = 4.3         # the receipt's own measured namesake spread, in per cent
AOR_SPREAD = 8.3         # what the ruling quotes


def shares(tag):
    """the window-integrated power in each source term, band by band -- the receipt's own read"""
    d = np.load(os.path.join(SP, tag + '.npz'))
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - NF * w) & (ee <= els + NF * w)
    nb = d[TERMS[0]].shape[1]
    raw = np.array([[float(np.trapezoid(d[k][m][:, b], ee[m])) for k in TERMS]
                    for b in range(nb)])
    return raw, raw / raw.sum(axis=1)[:, None], np.asarray(d['q_edges'], float)


def coefficients(arm):
    """** THE RECEIPT'S OWN FORM, lifted and not guessed. **  The Doppler scale `c` for which the
    CONTROL's monopole FRACTION becomes the ARM's:  sw / (sw + c^2 dp + rest) = tgt.

    ⌗ *My first attempt here invented a ratio of Doppler-side fractions instead, and it returned 13.0
    per cent on the namesake against the receipt's 4.3 -- and, worse, a 1.88-sigma trend that would
    have CONFIRMED the ruling's q-dependence reading.  The "reproduce the namesake first" gate is the
    only reason that did not get reported.*"""
    raw_c, _fr_c, qe = shares(CTL)
    _raw_a, fr_a, _ = shares(arm)
    out = []
    for b in range(raw_c.shape[0]):
        sw, dp = raw_c[b, 0], raw_c[b, 1]
        rest = raw_c[b, 2] + raw_c[b, 3]
        tgt = fr_a[b, 0]
        out.append(float(np.sqrt(max((sw / tgt - sw - rest) / dp, 0.0))))
    return np.array(out), 0.5 * (qe[:-1] + qe[1:])


def trend(c, x):
    s, i = np.polyfit(x, c, 1)
    res = c - (s * x + i)
    n = len(x)
    se = float(np.sqrt(np.sum(res ** 2) / (n - 2) / np.sum((x - x.mean()) ** 2)))
    return float(s), se, abs(s) / se if se else float('inf'), abs(s) * (x.max() - x.min())


def main():
    fails = []
    out = {}
    for nm, arm in (('the namesake arm', NSK), ('the ARM OF RECORD', AOR)):
        c, qc = coefficients(arm)
        spread = 100 * (c.max() / c.min() - 1)
        out[arm] = (c, qc, spread)
        print(f"  {nm:18s} " + "  ".join(f"{x:.4f}" for x in c))
        print(f"  {'':18s} spread {spread:.1f} per cent;  mean {c.mean():.4f};  "
              f"sd {c.std(ddof=1) / c.mean() * 100:.1f} per cent of the mean")
    c, qc, spread = out[AOR]
    cn = out[NSK][0]

    print("\n  ⛔ AND THE SPREAD HAS NO TREND IN WAVENUMBER, which is what the registered condition's")
    print("     claim was about:")
    sig = {}
    for nm, x in (('q', qc), ('q^2', qc ** 2)):
        s, se, nsig, span = trend(c, x)
        sig[nm] = nsig
        print(f"       against {nm:4s}  slope {s:+.5f} +- {se:.5f}  -> {nsig:.2f} sigma;  "
              f"the fit spans {span:.4f} across the range against a spread of {c.max()-c.min():.4f} "
              f"({100 * span / (c.max() - c.min()):.0f} per cent of it)")
    d = np.sign(np.diff(c)).astype(int)
    print(f"       successive differences {list(d)} -- {'alternating' if (d[:-1] * d[1:] < 0).any() else 'monotone'}"
          f", so scatter and not a reshaping")

    if abs(out[NSK][2] - NSK_SPREAD) > 0.15:
        fails.append(f"the namesake spread is {out[NSK][2]:.1f} per cent, not the {NSK_SPREAD} the "
                     f"receipt measures -- this script is not reading what the receipt reads")
    if abs(spread - AOR_SPREAD) > 0.15:
        fails.append(f"the arm-of-record spread is {spread:.1f} per cent, not the {AOR_SPREAD} the "
                     f"ruling quotes")
    if max(sig.values()) >= 1.0:
        fails.append(f"a trend reaches one sigma ({max(sig.values()):.2f}) -- the ruling's "
                     f"q-dependence reading would then stand and this script's conclusion is wrong")
    if not spread > out[NSK][2]:
        fails.append("the arm of record's spread is not the wider -- re-read the re-point")

    print()
    if fails:
        print("FAILED:")
        for f in fails:
            print("  - " + f)
        return 1
    print("  OK -- the namesake spread is reproduced, the arm of record's is the 8.3 per cent the")
    print("  ruling quotes, and neither trend reaches one sigma: the condition fails on SCATTER and")
    print("  the 'not a q-dependent reshaping' claim it protected survives.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
