#!/usr/bin/env python3
"""`r7733+cc66` WHAT "UNIT AMPLITUDE" DOES AND DOES NOT SAY -- the decomposition behind the P15 sentence.

⛔⛔ ** THIS IS A DESCRIPTIVE MEASUREMENT AND IT WAS NOT REGISTERED, which is stated here rather than
left to be noticed. **  It sets no threshold, declares no pass and no fail, and nothing in `r7731`'s
verdict depends on it.  It exists because order `r7733` item 2 asks for a SENTENCE, and before drafting
one I had to know whether "both contribute at unit amplitude" licenses "both contribute equally to the
LOCATED STEP".  ⇒ *Those are different statements, and a reader who takes the first for the second has
been misled by the sentence rather than by the measurement.*

⛭ ** AND MY OWN EXPECTATION GOING IN WAS WRONG, IN THE OPPOSITE DIRECTION. **  I expected the source
template to be SMALL beside the kernel's, so that unit amplitude on it would be unit amplitude on a
small thing.  It is LARGER (`0.278` against `0.219` at the primary binning).  The resolution is not
size at all -- it is SHAPE, and that is the second measurement below.

** WHAT IS MEASURED, and why these two and not others. **

A located transition is a feature AT an `l`.  ⇒ A template that is CONSTANT in `l` cannot produce one,
however large it is, because it moves every multipole by the same factor.  So the template is split
against the weighted norm into
    * its `k`-only part   -- the weighted mean over `l` at each `k`-bin, a featureless rescaling;
    * its `l`-structured part -- what is left, the only part that can carry a transition,
and then the FITTED model's `l`-structured variance is apportioned between the two terms and their
cross term.  ⛭ *The weights are `r7723`'s amendment-2 contribution weights, the same `W` the fit uses,
because a decomposition in an unweighted norm would be a decomposition of a different object than the
one the amplitudes were fitted in.*

⚠ The split is not unique -- "constant in `l`" is one choice of a featureless direction, and a
different one would apportion differently.  It is the choice the printed sentence is about: `P15` says
the transition is LOCATED, at an `l`, and a template flat in `l` is exactly what cannot locate one.
"""
import os
import sys

import numpy as np

BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r7733_binned.npz')
CELLS = ('S_lcdm__K_lcdm', 'S_lcdm__K_cr', 'S_cr__K_lcdm', 'S_cr__K_cr')
READINGS = (('PRIMARY', '12'), ('SECONDARY', '23'))


def arena(z, tag):
    """the templates, the observation and the weights, formed here and not banked"""
    B = {c: z[f'B{tag}__{c}'] for c in CELLS}
    dead = np.zeros(B[CELLS[0]].shape, bool)
    for c in CELLS:
        dead |= B[c] <= 0
    lb = {c: np.where(dead, 0.0, np.log(np.where(B[c] > 0, B[c], 1.0))) for c in CELLS}
    tk = lb['S_lcdm__K_cr'] - lb['S_lcdm__K_lcdm']
    ts = lb['S_cr__K_lcdm'] - lb['S_lcdm__K_lcdm']
    obs = lb['S_cr__K_cr'] - lb['S_lcdm__K_lcdm']
    W = B['S_lcdm__K_lcdm'] / B['S_lcdm__K_lcdm'].sum(axis=1, keepdims=True)
    W = np.where(dead, 0.0, W)
    return tk, ts, obs, W, dead


def wrms(X, W):
    return float(np.sqrt((W * X ** 2).sum() / W.sum()))


def split(X, W):
    """the `k`-only part (weighted mean over `l` at each `k`-bin) and the `l`-structured remainder"""
    cw = W.sum(axis=0, keepdims=True)
    flat = np.where(cw > 0, (W * X).sum(axis=0, keepdims=True) / np.where(cw > 0, cw, 1.0), 0.0)
    return np.broadcast_to(flat, X.shape), X - flat


def main():
    print(__doc__)
    print("=" * 100)
    z = np.load(BANK, allow_pickle=True)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'r7731_cc66_the_detectability_read'))
    import four_cell as FC                                                   # noqa: E402

    for name, tag in READINGS:
        tk, ts, obs, W, dead = arena(z, tag)
        a_ker, a_src = FC.fit2(obs, tk, ts, W)
        print(f"\n  ⛭ {name}  ({tk.shape[1]} bins, {tk.shape[0]} multipoles, "
              f"{int(dead.sum())} cells masked)")
        print(f"      fitted   a_ker {a_ker:+.4f}   a_src {a_src:+.4f}   "
              f"(the r7731 verdict, refitted here from the bank)")

        rk, rs = wrms(tk, W), wrms(ts, W)
        ck, cs = abs(a_ker) * rk, abs(a_src) * rs
        print(f"\n      ① SIZE -- the source template is the BIGGER of the two, not the smaller")
        print(f"         template rms      kernel {rk:.5f}   source {rs:.5f}   "
              f"source/kernel {rs / rk:.4f}")
        print(f"         contribution rms  kernel {ck:.5f}   source {cs:.5f}   "
              f"source is {100 * cs / ck:.1f} % of kernel")

        fk, lk = split(tk, W)
        fs, lsr = split(ts, W)
        shk, shs = wrms(lk, W) / rk, wrms(lsr, W) / rs
        print(f"\n      ② SHAPE -- and this is where they part company")
        print(f"         kernel template  `l`-structured {100 * shk:.2f} %   "
              f"`k`-only {100 * (1 - shk):.2f} %   (rms fractions)")
        print(f"         source template  `l`-structured {100 * shs:.2f} %   "
              f"`k`-only {100 * (1 - shs):.2f} %")

        ak, asr = a_ker * lk, a_src * lsr
        vk = float((W * ak ** 2).sum() / W.sum())
        vs = float((W * asr ** 2).sum() / W.sum())
        vx = float(2 * (W * ak * asr).sum() / W.sum())
        vt = vk + vs + vx
        print(f"\n      ③ THE `l`-STRUCTURED VARIANCE OF THE FITTED MODEL, apportioned")
        print(f"         kernel {vk:.6f} ({100 * vk / vt:+.1f} %)   "
              f"source {vs:.6f} ({100 * vs / vt:+.1f} %)   "
              f"cross {vx:.6f} ({100 * vx / vt:+.1f} %)   total {vt:.6f}")
        print(f"         ⇒ in rms the kernel carries {np.sqrt(vk / vs):.2f}x the source's "
              f"`l`-structure")
    print("\n" + "=" * 100)
    print("  ⇒ UNIT AMPLITUDE IS A STATEMENT ABOUT THE COEFFICIENT, NOT ABOUT THE SHARE OF THE STEP.")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
