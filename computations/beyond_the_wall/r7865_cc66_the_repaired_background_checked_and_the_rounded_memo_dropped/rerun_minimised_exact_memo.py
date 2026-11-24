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
    # ** the repair must be in the file this run imports, and the check is STRUCTURAL. **
    #   ⛔ The first cut of this guard asked whether `'round(h0'` appears in the source -- and it
    #   REFUSED on the repaired file, because the docstring explaining the repair quotes the old
    #   key.  A guard keyed on a spelling, tripped by prose about the very thing it guards.  So it
    #   now parses the function and reads the `key` assignment itself: the value must be a plain
    #   tuple of bare names, which a `round(...)` call is not, whatever any comment says.
    import ast
    import inspect
    fn = ast.parse(inspect.getsource(PL.bao_min).lstrip()).body[0]
    keys = [n.value for n in ast.walk(fn)
            if isinstance(n, ast.Assign) and len(n.targets) == 1
            and isinstance(n.targets[0], ast.Name) and n.targets[0].id == 'key']
    exact = (len(keys) == 1 and isinstance(keys[0], ast.Tuple)
             and all(isinstance(e, ast.Name) for e in keys[0].elts))
    if not exact:
        print('  ⛔ the imported `bao_min` does not key on bare names -- refusing to run.  '
              'Its key is: %s' % (ast.dump(keys[0]) if len(keys) == 1 else '%d assignments'
                                  % len(keys)))
        return 1
    print('  the imported `bao_min` keys on the exact pair (%s), read off its parsed source rather '
          'than matched in its text' % ', '.join(e.id for e in keys[0].elts), flush=True)
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
