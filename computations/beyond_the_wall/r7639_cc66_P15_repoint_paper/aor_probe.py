"""Run a receipt with every cr-arm spectrum load REDIRECTED to its `_leafrec1` counterpart.

This is the DRYRUN's question asked under this seat's control: what does each receipt SAY on the arm of
record, read with its OWN statistic, before any carry is applied?  It answers which assertions move,
which fail, and -- the one that matters most after r7639+cc66.9 -- which receipts say exactly the same
thing on either arm, where a green would mean nothing.

** IT REPORTS ITS OWN REDIRECT COUNT. **  A probe that runs is not a probe that measures: if no load was
redirected, the run is the namesake run under a different name, and the output says so instead of
pretending.
"""
import os, sys, runpy, numpy as np

SPEC = os.path.realpath('/home/user/shadow-of-existence/computations/beyond_the_wall/spectra')
DISK = set(f for f in os.listdir(SPEC) if f.endswith('.npz'))
HITS, MISSES = [], []
_orig = np.load


def load(f, *a, **k):
    try:
        if isinstance(f, str) and f.endswith('.npz'):
            d, b = os.path.split(os.path.realpath(f))
            if d == SPEC and '_leafrec1' not in b:
                alt = b[:-4] + '_leafrec1.npz'
                if alt in DISK:
                    HITS.append((b, alt))
                    return _orig(os.path.join(d, alt), *a, **k)
                if '_cr' in b or b.startswith('cr_'):
                    MISSES.append(b)
    except Exception:
        pass
    return _orig(f, *a, **k)


np.load = load
path = sys.argv[1]
rc = 0
try:
    sys.argv = [path]
    runpy.run_path(path, run_name='__main__')
except SystemExit as e:
    rc = e.code if isinstance(e.code, int) else 0
except Exception as e:
    print(f"\n[PROBE] the receipt raised {type(e).__name__}: {e}")
    rc = 99
print(f"\n[PROBE] rc={rc}  redirected {len(HITS)} load(s): "
      + ', '.join(sorted(set(a for a, _ in HITS))))
if MISSES:
    print(f"[PROBE] cr-arm loads with NO `_leafrec1` on disk: "
          + ', '.join(sorted(set(MISSES))))
if not HITS:
    print("[PROBE] ⛔ NOTHING WAS REDIRECTED -- this run is the namesake run and says nothing about "
          "the arm of record.")
