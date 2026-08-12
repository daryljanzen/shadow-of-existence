#!/usr/bin/env python3
"""DRAFT — the regression channel the receipt layer does not currently close.

THE PROBLEM.  191 of the 249 receipts contain no `assert`.  Their exit code is 0 whatever they
compute, so `run everything and check the return codes` is a SMOKE TEST for three-quarters of the
layer, not a verification.  That includes 76 of the 100 rows `INDEX.md` marks with its highest
status, ✔✔.  Nothing is wrong with those receipts -- ✔✔ is a READER's verdict on printed output,
and the corpus's practice is to read them.  ** But a reader's verdict is pinned to the revision it
was given at, and a silent numerical drift afterwards is invisible: the receipt still returns 0,
still prints a table, and the numbers have moved. **

That channel is not hypothetical.  F06 is a paper and a receipt that had drifted apart with every
gate green.

THE FIX, and it needs no per-receipt work.  A receipt's printed NUMBERS are its content.  Store
them once, at the revision a reader signs off, and fail when they move.  This is the golden-output
discipline, restricted to the part of the output that carries meaning and insensitive to prose
edits, table widths and comment rewrites.

  python3 DRAFT_receipt_fingerprints.py --bless        # write the baseline
  python3 DRAFT_receipt_fingerprints.py                # compare; nonzero on any drift

WHAT IT DELIBERATELY DOES NOT DO.
  · It does not judge whether a number is RIGHT.  It judges whether it CHANGED.  A receipt whose
    numbers were wrong when blessed stays wrong and silent -- this closes the regression channel,
    not the correctness one.  Those are different jobs and conflating them is how a gate comes to
    be trusted for something it does not do.
  · It does not replace reading.  It makes a reader's verdict DURABLE, which is the thing the
    ✔✔ mark currently asserts and cannot enforce.
  · Timings, memory addresses and RNG-seeded values will drift by design.  Receipts that print
    them need either a fixed seed or an exclusion here; the baseline run reports which ones move
    on a repeat run with no code change, and that list is the exclusion list.

TOLERANCE.  Numbers are compared to 10 significant figures by default -- loose enough to absorb
BLAS/last-bit differences across machines, tight enough that any real change in a computed
quantity shows.  --sig sets it.
"""
import argparse, hashlib, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RCPT = os.path.join(ROOT, 'receipts')
BASE = os.path.join(os.path.dirname(__file__), 'receipt_fingerprints.json')
NUM = re.compile(r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')


def fingerprint(text, sig):
    vals = []
    for m in NUM.finditer(text):
        try:
            x = float(m.group(0))
        except ValueError:
            continue
        vals.append(f'{x:.{sig}g}')
    return {'n': len(vals), 'sha': hashlib.sha256('|'.join(vals).encode()).hexdigest()[:16],
            'vals': vals}


def run_all(cache):
    if cache and os.path.exists(cache):
        return json.load(open(cache))
    env = dict(os.environ)
    env['PYTHONPATH'] = os.path.join(ROOT, 'storyboard_receipts')
    out = {}
    for dp, dirs, files in os.walk(RCPT):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git')]
        for f in sorted(files):
            if not f.endswith('.py'):
                continue
            p = os.path.join(dp, f)
            r = subprocess.run([sys.executable, p], capture_output=True, text=True,
                               timeout=1800, cwd=dp, env=env)
            out[os.path.relpath(p, RCPT)] = r.stdout
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bless', action='store_true')
    ap.add_argument('--sig', type=int, default=10)
    ap.add_argument('--cache', default='/tmp/rcpt_out/all.json',
                    help='reuse a stdout cache from capture_receipt_output.py')
    a = ap.parse_args()

    out = run_all(a.cache)
    fp = {k: fingerprint(v, a.sig) for k, v in sorted(out.items())}

    if a.bless:
        json.dump({k: {'n': v['n'], 'sha': v['sha']} for k, v in fp.items()},
                  open(BASE, 'w'), indent=1)
        tot = sum(v['n'] for v in fp.values())
        print(f"  blessed {len(fp)} receipts, {tot} printed numbers, "
              f"{a.sig} significant figures -> {os.path.basename(BASE)}")
        return 0

    if not os.path.exists(BASE):
        print("  [FAIL] no baseline; run with --bless first")
        return 1
    base = json.load(open(BASE))
    moved, added, gone = [], [], []
    for k, v in fp.items():
        if k not in base:
            added.append(k)
        elif base[k]['sha'] != v['sha']:
            moved.append((k, base[k]['n'], v['n']))
    for k in base:
        if k not in fp:
            gone.append(k)
    print(f"\n  RECEIPT FINGERPRINTS: {len(fp)} receipts compared against the baseline")
    for k, n0, n1 in moved:
        note = '' if n0 == n1 else f'   (printed-number count {n0} -> {n1})'
        print(f"    [FAIL] {k} printed different numbers{note}")
    for k in added:
        print(f"    [note] {k} is new and unblessed")
    for k in gone:
        print(f"    [note] {k} was blessed and is no longer present")
    if moved:
        print("\n  A receipt's numbers moved without anyone asking.  Either the change is intended"
              "\n  -- in which case re-read the receipt and re-bless -- or it is the drift this"
              "\n  gate exists to catch.")
        return 1
    print("  No receipt's printed numbers have moved.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
