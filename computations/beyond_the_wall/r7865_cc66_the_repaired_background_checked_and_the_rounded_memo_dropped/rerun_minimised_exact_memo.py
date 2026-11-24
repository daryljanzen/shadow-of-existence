"""r7865+cc66 item ⑦: RE-RUN THE MINIMISED ARM WITH THE MEMO KEYED EXACTLY, AND SEE IF 54.00 MOVES.

Order r7865 (69): *"Drop the rounding from the key, re-run the minimised arm, and state whether
54.00 meV moves."*  Bands Ⓕ and Ⓖ registered at `r7865+cc66.1` before this file existed.

** THE REPAIR IS IN r7853's OWN FILE, BECAUSE 69 RULED IT THERE. **  `bao_min`'s key was
`(round(h0, 4), round(om, 5))` and is now `(h0, om)`.  Nothing else about the arm changes: same
five free parameters, same `LMAX`, same box, same CAMB build, same BAO and lensing terms.

** THE LANDED POINTS ARE NOT OVERWRITTEN. **  `r7853/out5` is the record of what the published
`54.00` meV was computed from, and a repair that erased it would destroy the evidence that the
repair was needed.  The re-run writes to `out_exact/` here, and the receipt compares the two.

** IDEMPOTENT: one JSON per sum, an existing file skipped.  Warm-started from the LANDED point at
the same sum **, so the two differ by the memo and not by the path the minimiser took to get there.

Run: python3 -I rerun_minimised_exact_memo.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT    # THREE dirnames, asserted
R7853 = os.path.join(os.path.dirname(HERE),
                     'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
assert os.path.isdir(R7853), R7853
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                             # noqa: E402

MODE = 'rd_min'
OUT = os.path.join(HERE, 'out_exact')
BANKED = os.path.join(R7853, 'out5')


def main():
    os.makedirs(OUT, exist_ok=True)
    # the repair must actually be in the file this run imports, checked rather than assumed
    import inspect
    src = inspect.getsource(PL.bao_min)
    if 'round(h0' in src:
        print('  ⛔ the memo is still rounded in the imported module -- refusing to run')
        return 1
    print('  the imported `bao_min` keys on the exact pair, confirmed by reading its source',
          flush=True)
    done = skipped = 0
    for s in PL.SUMS:
        path = os.path.join(OUT, '%s_%.3f.json' % (MODE, s))
        if os.path.exists(path):
            skipped += 1
            print('  skip (already done): %s' % os.path.basename(path), flush=True)
            continue
        b = json.load(open(os.path.join(BANKED, '%s_%.3f.json' % (MODE, s))))
        start = (b['H0'], b['Om'], b['ombh2'], b['ns'], b['tau'])
        det = PL.profile(s, MODE, start)
        det['warm_from_landed'] = True
        det['landed_total'] = b['total']
        det['interior'] = all(lo + 1e-9 < v < hi - 1e-9 for v, (lo, hi)
                              in zip((det['H0'], det['Om'], det['ombh2'], det['ns'], det['tau']),
                                     PL.BOX))
        json.dump(det, open(path, 'w'), indent=1)
        done += 1
        print('  Sum=%.3f: total %10.3f (landed %10.3f, moved %+8.4f)  H0 %7.3f  rd %8.3f  '
              'interior %s  nfev %d'
              % (s, det['total'], b['total'], det['total'] - b['total'], det['H0'],
                 det['rd_used'], det['interior'], det['nfev']), flush=True)
    print('\n  wrote %d, skipped %d, of %d' % (done, skipped, len(PL.SUMS)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
