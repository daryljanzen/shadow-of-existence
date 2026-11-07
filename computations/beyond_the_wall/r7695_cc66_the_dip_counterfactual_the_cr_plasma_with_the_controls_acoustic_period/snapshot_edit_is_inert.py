"""r7699+cc66 -- THE SNAPSHOT EDIT MUST CHANGE NO PHYSICS, MEASURED AND NOT ASSERTED.

Adding `COMBRHO` to `_SWITCH_SNAPSHOT` changes the instrument's bytes, so by the corpus's own
standard (`r7655`: "a bank's provenance is the file that made it, not the file's intentions") it is a
different instrument.  ⇒ *The claim "additive and inert" is therefore a claim that has to be
MEASURED, and `r7655` records the one time it was assumed: two additive prints broke a receipt.*

This compares the twelve slices run BEFORE the snapshot edit against the twelve run AFTER it, with
every per-k array and every spectrum required BYTE-IDENTICAL, and the configs required to differ in
EXACTLY the two keys that must differ.

    python3 snapshot_edit_is_inert.py <before-dir> <after-dir>
"""
import json
import os
import sys

import numpy as np

BEFORE, AFTER = sys.argv[1], sys.argv[2]
fail = []
n_arr = 0

for sub, suf in (('src', '_fields.npz'), ('dec', '_pairs.npz')):
    for f in sorted(os.listdir(os.path.join(BEFORE, sub))):
        if not f.endswith('.npz'):
            continue
        pb, pa = os.path.join(BEFORE, sub, f), os.path.join(AFTER, sub, f)
        if not os.path.exists(pa):
            fail.append(f'{sub}/{f}: absent from the AFTER run')
            continue
        a = np.load(pb, allow_pickle=True)
        b = np.load(pa, allow_pickle=True)
        if sorted(a.files) != sorted(b.files):
            fail.append(f'{sub}/{f}: key sets differ')
            continue
        for k in a.files:
            if k == 'config':
                ca = json.loads(str(np.atleast_1d(a[k])[0]))
                cb = json.loads(str(np.atleast_1d(b[k])[0]))
                d = sorted(x for x in set(ca) | set(cb) if ca.get(x) != cb.get(x))
                want = ['COMBRHO', 'instrument_blob'] if 'COMBRHO' not in ca else ['instrument_blob']
                if d != want:
                    fail.append(f'{sub}/{f}: config differs in {d}, wanted {want}')
                continue
            va, vb = np.asarray(a[k]), np.asarray(b[k])
            n_arr += 1
            if va.shape != vb.shape or va.dtype != vb.dtype:
                fail.append(f'{sub}/{f}[{k}]: shape/dtype {va.shape}{va.dtype} vs {vb.shape}{vb.dtype}')
            elif va.dtype.kind in 'fc':
                if va.tobytes() != vb.tobytes():
                    _m = float(np.nanmax(np.abs(va - vb))) if va.size else 0.0
                    fail.append(f'{sub}/{f}[{k}]: NOT byte-identical, max |diff| = {_m:.3e}')
            elif not np.array_equal(va, vb):
                fail.append(f'{sub}/{f}[{k}]: differs')

print(f"  THE SNAPSHOT EDIT, measured on {n_arr} arrays across 12 slice pairs")
if fail:
    for f in fail[:30]:
        print(f'  ⛔ [FAIL] {f}')
    print(f'  ⇒ {len(fail)} difference(s): the edit is NOT inert and the claim is withdrawn.')
    raise SystemExit(1)
print(f"  ✔ every one of the {n_arr} arrays is BYTE-IDENTICAL, and each config differs in exactly "
      f"`COMBRHO` and `instrument_blob` -- the two keys that must change and nothing else.")
print("  ⌗ So the edit is inert BY MEASUREMENT.  It is still a different instrument by the corpus's "
      "own provenance standard, which is why the banks it produced are re-run rather than relabelled.")
