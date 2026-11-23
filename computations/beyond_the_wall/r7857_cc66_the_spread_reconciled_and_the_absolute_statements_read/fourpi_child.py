#!/usr/bin/env python3
r"""ONE receipt, run with the bank's instrument TT spectra DOUBLED -- which is exactly what turning
`FOURPI` on does to them, and not an approximation of it:

    FOURPI=1  =>  Cl *= 4 pi   (_FP_ACC, on the accumulation)
                  Dl  = Cl * l(l+1) / (2 pi)   (_FP_DL, on every D_l write)
    =>  Dl_new / Dl_old = 4 pi / 2 pi = 2 EXACTLY   (60 measured 2.000000000000, worst 8.9e-16)

So a regenerated bank is bit-for-bit predictable from the existing one, which is 60's own statement
at `r7858` -- and this child applies that prediction at the point every receipt reads the bank.

** WHAT IS AND IS NOT DOUBLED, AND WHY THE ASYMMETRY IS THE POINT. **
  `Dl`                 -> x2       `out[j]` carries `_FP_ACC` and the write carries `_FP_DL`
  `Dl_EE` / `Dl_TE`    -> x2 only under MODE=all; TT-only under MODE=tt, which is the live switch
  `Dl_pairs`           -> UNCHANGED, always: `_dec` is accumulated beside `out[j]` and never sees
                          `_FP_ACC`, and the save line applies no `_FP_DL` to it either
  everything else      -> UNCHANGED (D_M, r_s, l_A, fields, transfers: no factor touches them)

Usage: MODE=tt|all python3 fourpi_child.py <receipt.py>
Prints the receipt's own output, then a trailer naming how many arrays it actually doubled.  A run
that doubled NOTHING is a vacuous probe and says so in the trailer rather than passing quietly.
"""
import os
import runpy
import sys

import numpy as np

MODE = os.environ.get('MODE', 'tt')
KEYS = {'Dl'} if MODE == 'tt' else {'Dl', 'Dl_EE', 'Dl_TE'}
HITS = {}
OPENED = []
_real_load = np.load


class _Doubling:
    """an npz whose instrument TT spectra come out doubled -- and nothing else does"""

    def __init__(self, z, path):
        self._z, self._p = z, path

    def __getitem__(self, k):
        v = self._z[k]
        if k in KEYS:
            HITS[f'{os.path.basename(self._p)}:{k}'] = int(np.asarray(v).size)
            return np.asarray(v, float) * 2.0
        return v

    def __contains__(self, k):
        return k in self._z

    def __iter__(self):
        return iter(self._z)

    def keys(self):
        return self._z.keys()

    def get(self, k, d=None):
        return self[k] if k in self._z else d

    def close(self):
        return self._z.close()

    @property
    def files(self):
        return self._z.files

    def __getattr__(self, n):
        return getattr(self._z, n)


def _load(path, *a, **kw):
    z = _real_load(path, *a, **kw)
    if hasattr(z, 'files'):
        OPENED.append(os.path.basename(str(path)))
    if hasattr(z, 'files') and any(k in KEYS for k in z.files):
        return _Doubling(z, str(path))
    return z


np.load = _load
rc = 0
try:
    runpy.run_path(sys.argv[1], run_name='__main__')
except SystemExit as e:
    rc = int(e.code or 0)
except BaseException as e:                                        # noqa: BLE001 -- reported, not hidden
    rc = 99
    print(f'__FOURPI_RAISED__ {type(e).__name__}: {e}')
sys.stdout.flush()
print(f'__FOURPI_OPENED__ {len(OPENED)} {sorted(set(OPENED))}')
print(f'__FOURPI_HITS__ {len(HITS)} {sorted(HITS)}')
print(f'__FOURPI_RC__ {rc}')
# ⛔ ** THE CHILD EXITS WITH THE RECEIPT'S OWN CODE. **  *It did not, for one run of this audit:
#   the cross-term receipt printed `[FAIL]` twice under doubling and this wrapper still exited `0`,
#   so the driver's summary line said `0 FAIL` over a log that showed two.  A wrapper's exit code is
#   never the verdict -- and a wrapper of MINE reporting a verdict it had not read is the same defect
#   this seat has now logged eleven times.*
sys.exit(rc)
