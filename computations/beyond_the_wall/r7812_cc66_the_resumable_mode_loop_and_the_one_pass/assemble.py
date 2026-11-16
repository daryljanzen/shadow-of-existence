"""r7812+cc66 (a1): sum banked k-slices into one spectrum, and CHECK THE SUM AGAINST A STRAIGHT RUN.

`C_l` is accumulated as `Cl += _project(kb, ...)` over disjoint k-batches, and the banks store
`Dl = Cl * l(l+1)`, which is linear in `C_l`.  So the assembled spectrum is the SUM of the slices'
`Dl` arrays, on the shared `ls` grid -- asserted identical before anything is added.

⛔ ** AND A FINDING THAT COST THIS SCRIPT ITS FIRST GUARD: THE PLAIN `SAVE` SITE RECORDS NEITHER
`sliced` NOR `n_modes`. **  It writes `D_M, Dl, arm, config, l_A, ls, r_s` and nothing else -- while
`DSAVE`, `POLSAVE` and the rest DO carry `sliced=bool(_ksl)` and `n_modes`.  So a PARTIAL `C_l` from
the plain `SAVE` is indistinguishable from a whole spectrum **except by its filename**, and the
`config` does not help either: it records the FORM switches and `KSLICE` is not among them (`r7807`).
  ⇒ *That is the PO-87 defect class exactly -- a bank whose nature lives only in its name.*  It is
  REPORTED to 69 rather than fixed here, because fixing it means editing the instrument, which this
  round established is not needed for (a1) and would move the blob for nothing.
  ⇒ *So this script cannot assert slice-hood, and does not pretend to.*  What validates the assembly
  is the exactness check against the straight run: if a whole spectrum were summed in by mistake, the
  comparison would fail loudly rather than pass quietly.  The check IS the guard.

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
        total = z['Dl'].copy() if total is None else total + z['Dl']
        n = int(z['n_modes']) if 'n_modes' in z.files else -1
        nmodes += max(n, 0)
        print(f'    + {os.path.basename(p)}  n_modes='
              + (f'{n:5d}' if n >= 0 else 'NOT RECORDED by the plain SAVE site'))
    return ls0, total, nmodes, meta


def main():
    outdir, stem = sys.argv[1], sys.argv[2]
    paths = load_slices(outdir, stem)
    print(f'  {len(paths)} slice(s):')
    ls, Dl, nmodes, meta = assemble(paths)
    print(f'  assembled: {nmodes} modes over {len(ls)} multipoles')
    out = os.path.join(outdir, f'{stem}_assembled.npz')
    # ⛔ Carry EVERY key the slices stored, not a chosen five.  The first version kept only
    # ('arm', 'r_s', 'D_M', 'l_A', 'ns') and so silently dropped `config` -- and `config` is what
    # r7807+cc66's own census reads off a bank, and what a consumer of this assembled spectrum may
    # read too.  A bank that is to STAND IN for another through a np.load swap has to answer every
    # key its consumers ask for; dropping one turns a re-pointing into a KeyError at the reader.
    carried = {k: meta[k] for k in meta if k not in ('sliced', 'n_modes', 'assembled_from')}
    np.savez(out, ls=ls, Dl=Dl, sliced=False, n_modes=nmodes,
             assembled_from=np.array([os.path.basename(p) for p in paths]), **carried)
    print(f'  -> {out}   (carrying {sorted(carried)})')

    if '--against' in sys.argv:
        ref = sys.argv[sys.argv.index('--against') + 1]
        zr = np.load(ref, allow_pickle=True)
        assert np.array_equal(zr['ls'], ls), 'the straight run uses a different l grid'
        if 'n_modes' in zr.files and nmodes > 0:
            assert int(zr['n_modes']) == nmodes, (
                f'mode count differs: straight {int(zr["n_modes"])} vs assembled {nmodes}')
        else:
            print('    ⌗ neither bank records `n_modes`, so the mode counts are not cross-checked '
                  'here; the Dl comparison below is what validates the partition')
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
