#!/usr/bin/env python3
"""`r7713+cc66` ONE combination of the dense-`l` discriminant, for a CI runner.

⛭ `r7715` (69) ruled option 1: the remaining three combinations run as a GitHub Actions matrix, one
   per runner, on the IDENTICAL instrument and grid as the combination already banked here, with the
   registered `5` sd target unchanged.

⛔ THE CONTROL COMES FIRST AND DECIDES WHETHER THIS RUNNER'S OUTPUT IS TRUSTED AT ALL.  The banked
   combination was computed in this project's container; this script recomputes its FIRST BLOCK here
   and refuses unless the two agree to `1e-12`.  Two things make that control worth the minute it
   costs rather than a formality:

   ⒜ It runs `dense.one_block`, the SAME function `build` uses, so it compares two MACHINES and not
      two implementations.  A control that reimplemented the kernel would answer a different question
      and would pass while the real thing differed.
   ⒝ `scipy.special.spherical_jn` at orders in the hundreds and arguments in the thousands is exactly
      the regime where a BLAS or libm difference between two machines shows up.  If the three new
      combinations were computed on a different arithmetic from the banked one, every ratio read
      against it would carry that difference as though it were physics -- and the ratios all share
      the banked combination as their denominator, so the error would not cancel anywhere.

⇒ A failed control exits NONZERO and computes nothing.  It is not a warning.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dense                                                                 # noqa: E402

TOL = 1e-12
BANKED = ('lcdm', 'lcdm')          # the combination computed in the container, used as the control


def control():
    """recompute the banked combination's first block HERE and compare, or refuse"""
    path = os.path.join(dense.OUT, 'pseudo__S_%s__K_%s.npz' % BANKED)
    if not os.path.exists(path):
        print(f"  ⛔ CONTROL IMPOSSIBLE: the banked combination is not in this checkout ({path}).")
        print("     Without it there is nothing to compare this runner's arithmetic against, so")
        print("     nothing computed here could be trusted against it. Refusing.")
        return False
    z = np.load(path)
    ref = np.asarray(z['y'], float)
    t0 = time.time()
    sl, yb = dense.one_block(*BANKED, 0)
    here = np.asarray(yb, float)
    ours = ref[:len(here)]
    if len(ours) != len(here):
        print(f"  ⛔ CONTROL IMPOSSIBLE: banked combination has {len(ref)} values, fewer than this "
              f"block's {len(here)}.")
        return False
    identical = bool(np.array_equal(here, ours))
    rel = float(np.max(np.abs(here / ours - 1.0)))
    print(f"\n  ⛔ THE CONTROL: block 0 of S={BANKED[0]} K={BANKED[1]}, l {int(sl[0])}-{int(sl[-1])}, "
          f"{len(here)} values  [{time.time() - t0:.1f} s]")
    print(f"       byte-identical to the banked values: {identical}")
    print(f"       max relative difference: {rel:.3e}   (registered tolerance {TOL:.0e})")
    ok = identical or rel <= TOL
    print(f"       ⇒ this runner's arithmetic is {'TRUSTED' if ok else '⛔ NOT TRUSTED'} "
          f"against the banked combination")
    if not ok:
        print("\n  ⛔ REFUSING TO COMPUTE. The three new combinations would all be read as ratios")
        print("    against the banked one, so a difference here would enter every ratio as physics")
        print("    and would not cancel anywhere. This is a finding about the two machines, not a")
        print("    flake, and it is reported rather than retried.")
    return ok


def main():
    src = os.environ.get('DENSE_SRC', '')
    ker = os.environ.get('DENSE_KER', '')
    if src not in dense.SRC or ker not in dense.ACC:
        print(f"  ⛔ DENSE_SRC={src!r} DENSE_KER={ker!r}: expected each of "
              f"{sorted(dense.SRC)} and {sorted(dense.ACC)}")
        return 2
    if (src, ker) == BANKED:
        print(f"  ⛔ {src}|{ker} is the BANKED combination and is the control, not a target. "
              f"Recomputing it here would overwrite the only thing the control compares against.")
        return 2
    print("=" * 100)
    print(f"  ⛭ `r7713+cc66` one combination on a runner: S={src}  K={ker}")
    print(f"     grid: every integer l with q in [{dense.QLO}, {dense.QHI}], "
          f"{len(dense.geom(ker)['ls'])} l, {dense.n_blocks(ker)} blocks of {dense.BLOCK}")
    print("=" * 100)
    if not control():
        return 1
    t0 = time.time()
    q, y = dense.build(src, ker)
    out = os.path.join(dense.OUT, f'pseudo__S_{src}__K_{ker}.npz')
    z = np.load(out)
    print(f"\n  ⛭ ASSEMBLED {len(y)} l in {time.time() - t0:.0f} s of COMPUTE on this runner")
    print(f"     q {q.min():.4f} .. {q.max():.4f};  finite {bool(np.isfinite(y).all())};  "
          f"all positive {bool((y > 0).all())}")
    print(f"     meta {json.loads(str(z['meta']))}")
    print(f"     -> {out}")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
