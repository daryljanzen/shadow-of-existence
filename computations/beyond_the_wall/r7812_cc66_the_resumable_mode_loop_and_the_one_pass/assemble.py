"""r7812+cc66 (a1): sum banked k-slices into one spectrum, and CHECK THE SUM AGAINST A STRAIGHT RUN.

`C_l` is accumulated as `Cl += _project(kb, ...)` over disjoint k-batches, and the banks store
`Dl = Cl * l(l+1)`, which is linear in `C_l`.  So the assembled spectrum is the SUM of the slices'
`Dl` arrays, on the shared `ls` grid -- asserted identical before anything is added.

⛔ The assembled bank records `assembled_from` and is NOT marked `sliced`: a slice is not a spectrum
and says so in its own `sliced` flag, while the assembly IS one.  Keeping both facts is the point.

Run: python3 assemble.py <out-dir> <stem>     [--against <straight.npz>]
"""
import glob
import os
import sys

import numpy as np


def load_slices(outdir, stem):
    paths = sorted(glob.glob(os.path.join(outdir, f'{stem}_k*.npz')),
                   key=lambda p: int(os.path.basename(p).split('_k')[1].split('_')[0]))
    if not paths:
        raise SystemExit(f'no slices under {outdir} for stem {stem}')
    return paths


def assemble(paths):
    ls0, total, nmodes, meta = None, None, 0, None
    for p in paths:
        z = np.load(p, allow_pickle=True)
        if ls0 is None:
            ls0, meta = z['ls'], {k: z[k] for k in z.files if k not in ('ls', 'Dl', 'Cl')}
        else:
            assert np.array_equal(ls0, z['ls']), f'{p}: a different l grid -- refusing to add'
        assert bool(z['sliced']), f'{p} is not marked sliced; it may be a whole spectrum'
        total = z['Dl'].copy() if total is None else total + z['Dl']
        nmodes += int(z['n_modes'])
        print(f'    + {os.path.basename(p)}  n_modes={int(z["n_modes"]):5d}')
    return ls0, total, nmodes, meta


def main():
    outdir, stem = sys.argv[1], sys.argv[2]
    paths = load_slices(outdir, stem)
    print(f'  {len(paths)} slice(s):')
    ls, Dl, nmodes, meta = assemble(paths)
    print(f'  assembled: {nmodes} modes over {len(ls)} multipoles')
    out = os.path.join(outdir, f'{stem}_assembled.npz')
    np.savez(out, ls=ls, Dl=Dl, sliced=False, n_modes=nmodes,
             assembled_from=np.array([os.path.basename(p) for p in paths]),
             **{k: meta[k] for k in ('arm', 'r_s', 'D_M', 'l_A', 'ns') if k in meta})
    print(f'  -> {out}')

    if '--against' in sys.argv:
        ref = sys.argv[sys.argv.index('--against') + 1]
        zr = np.load(ref, allow_pickle=True)
        assert np.array_equal(zr['ls'], ls), 'the straight run uses a different l grid'
        assert int(zr['n_modes']) == nmodes, (
            f'mode count differs: straight {int(zr["n_modes"])} vs assembled {nmodes}')
        a, b = np.asarray(zr['Dl'], float), np.asarray(Dl, float)
        bit = bool(np.array_equal(a, b))
        rel = float(np.max(np.abs(b / a - 1.0)))
        ulp = float(np.max(np.abs(b - a) / np.maximum(np.abs(a), 1e-300) / np.finfo(float).eps))
        print('\n  ===== THE EXACTNESS CHECK (69\'s (a1)) =====')
        print(f'    straight run : {ref}')
        print(f'    bit-identical: {bit}')
        print(f'    max |assembled/straight - 1| = {rel:.3e}')
        print(f'    worst difference in ULPs     = {ulp:.2f}')
        print('    ⇒ ' + ('BIT-IDENTICAL: the partition is exact, not merely close.'
                          if bit else
                          f'NOT bit-identical; residual {rel:.3e} is a SUMMATION-ORDER artefact if '
                          f'it is at the ULP scale, and a real disagreement if it is not.'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
