"""r7097 (70) -- the gate's fail paths, each planted on a SCRATCH copy of the banks (symlinks, plus the one
file each case changes).  Nothing in the repository's bank is touched.  Each case must produce exactly the
failure it plants, and the clean copy and the 'carries a good config' case must pass."""
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_banked_config as G                                   # noqa: E402


def scratch():
    t = tempfile.mkdtemp()
    os.makedirs(os.path.join(t, 'corpus'))
    shutil.copy(os.path.join(ROOT, 'corpus', 'banked_config_manifest.json'), os.path.join(t, 'corpus'))
    for b in G.BANKS:
        os.makedirs(os.path.join(t, b))
        for f in os.listdir(os.path.join(ROOT, b)):
            if f.endswith('.npz'):
                os.symlink(os.path.join(ROOT, b, f), os.path.join(t, b, f))
    return t


def run(t):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = G.main(t)
    return rc, buf.getvalue()


SP = os.path.join('computations', 'beyond_the_wall', 'spectra')
one = sorted(f for f in os.listdir(os.path.join(ROOT, SP)) if f.endswith('.npz'))[0]
good = json.dumps({'switches': {'ARM': 'cr', 'LEAFSCALES': '1', 'ZSTART': '3e7', 'STACKPERT': '0', 'VISLEAF': '0'},
                   'instrument': 'blob-hash'})
CASES = []


def case(name, want_rc, want, mutate):
    t = scratch()
    try:
        mutate(t)
        rc, out = run(t)
        ok = rc == want_rc and (want is None or want in out)
        CASES.append(ok)
        print(f'  [{"ok" if ok else "FAIL"}]  {name:44s} rc={rc}  {"(" + want + ")" if want else ""}')
        if not ok:
            print(out)
    finally:
        shutil.rmtree(t)


case('clean copy of today\'s bank', 0, None, lambda t: None)
case('a NEW .npz with no config', 1, 'NEW',
     lambda t: np.savez(os.path.join(t, SP, 'new_run_cr.npz'), ls=np.arange(3), Dl=np.ones(3)))
case('a legacy file REWRITTEN in place', 1, 'REWRITTEN',
     lambda t: (os.remove(os.path.join(t, SP, one)), np.savez(os.path.join(t, SP, one), ls=np.arange(3))))
case('a legacy file removed (STALE entry)', 1, 'STALE', lambda t: os.remove(os.path.join(t, SP, one)))
case('a legacy file that gains config (STALE)', 1, 'STALE',
     lambda t: (os.remove(os.path.join(t, SP, one)), np.savez(os.path.join(t, SP, one), ls=np.arange(3), config=good)))
case('a new .npz with a MALFORMED config', 1, 'MALFORMED',
     lambda t: np.savez(os.path.join(t, SP, 'new_bad.npz'), ls=np.arange(3), config=json.dumps({'ARM': 'cr'})))
case('a new .npz carrying a good config', 0, None,
     lambda t: np.savez(os.path.join(t, SP, 'new_good.npz'), ls=np.arange(3), config=good))
print(f'\n  {sum(CASES)} of {len(CASES)} cases behave as planted')
sys.exit(0 if all(CASES) else 1)
