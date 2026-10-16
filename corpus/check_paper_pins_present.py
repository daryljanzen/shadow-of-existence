#!/usr/bin/env python3
"""check_paper_pins_present.py -- NO NEW PAPER PIN WHOSE LITERAL IS IN NO PAPER.  Built r7417+70.2 by node 70 (r7417 ①).

** WHAT THIS CATCHES. **  A row of `quote_pin_baseline.tsv` with target `PAPER` pins a sentence a receipt says the
papers carry.  `check_quote_pins` keys the row; nothing asked, push by push, whether the literal is still IN a
paper.  The dead-pin census (`r7371+cc66`) asked it once and found `123` PAPER rows whose literal is in none of
`corpus/*.tex`.  `r7415+70` ④ built the cheap exact route and `r7417` ① wired the PAPER half here.

** THE TEST IS `check_quote_pins._present_at`, CALLED AND NOT REIMPLEMENTED. **  Its `hit`, `_flat`, `_unmark` and
its PAPER file selection are the gate's own.  Only the I/O is replaced: the `corpus/*.tex` blobs at HEAD are read
once through one `git cat-file --batch`, pre-loaded into its `_SHOW_CACHE`, and its `ls-tree` is answered from
that listing.  Measured exact against the uninstrumented call on all `1510` PAPER rows (and `1217` SOURCE rows)
at `r7415+70.10`: `0` differ.

** A RATCHET, BECAUSE THE ABSENT SET IS NOT EMPTY AND IS NOT ALL DEFECT. **  `paper_pins_absent.tsv` lists the
keys absent today.  They are CANDIDATES, not verdicts: the green-receipt filter is not applied (`r7371+cc66` ④),
and `NOT-A-PIN` / `ENCODING-OK` rows may be benign absences.  The gate fails on:
  NEW    an absent PAPER key not in the list -- a dead-pin candidate landing silently;
  STALE  a listed key now present, or no longer a live row -- the list only shrinks (`--update` rewrites it);
  SEED   the two-sided control: a literal known present must read present, and the same literal with one
         character changed must read absent.
** It says NOTHING about the SOURCE half **, whose test (`_present_at`'s repo-wide branch) is invalid
(`r7371+cc66.44`; `S60`: `94` of `112`).  `r7417` ②: a route validated against an instrument measures agreement
with the instrument, not correctness of the claim.

    python3 corpus/check_paper_pins_present.py [--update | --counts]
"""
import functools
import importlib.util
import json
import os
import subprocess
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(HERE, 'quote_pin_baseline.tsv')
ABSENT = os.path.join(HERE, 'paper_pins_absent.tsv')

_spec = importlib.util.spec_from_file_location('_cqp', os.path.join(HERE, 'check_quote_pins.py'))
Q = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(Q)


def paper_rows():
    """(receipt, literal) for every PAPER row, keyed the way the gate keys it: the literal column is JSON"""
    out = []
    for ln in open(LEDGER, encoding='utf-8').read().split('\n'):
        if '\t' not in ln or ln.startswith('#'):
            continue
        c = ln.split('\t')
        if len(c) < 6 or c[2] != 'PAPER':
            continue
        try:
            out.append((c[0], json.loads(c[1])))
        except ValueError:
            continue
    return out


class _R:
    def __init__(self, out):
        self.stdout, self.stderr, self.returncode = out, '', 0


def install(sha):
    """read corpus/ at `sha` once and route `_present_at`'s PAPER I/O to it"""
    ls = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-z', sha, 'corpus/'], capture_output=True,
                        check=True).stdout.split(b'\0')
    blobs = []
    for e in ls:
        if not e:
            continue
        meta, path = e.split(b'\t', 1)
        if meta.split()[1] == b'blob':
            blobs.append((path.decode('utf-8', 'surrogateescape'), meta.split()[2]))
    p = subprocess.Popen(['git', '-C', ROOT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def feed():                                  # a writer thread, or the two pipes fill and deadlock each other
        p.stdin.write(b''.join(oid + b'\n' for _, oid in blobs))
        p.stdin.close()
    threading.Thread(target=feed, daemon=True).start()
    names = []
    for path, _ in blobs:
        n = int(p.stdout.readline().split()[2])
        raw = p.stdout.read(n)
        p.stdout.read(1)
        if path.endswith('.tex'):                # `_present_at`'s PAPER branch reads only these
            Q._SHOW_CACHE[(sha, path)] = Q._flat(raw.decode('utf-8', 'replace'))
        names.append(path)
    p.wait()
    listing = '\n'.join(names)
    real = Q._git

    def fake(*a):
        if a == ('ls-tree', '--name-only', sha, 'corpus/'):
            return _R(listing)
        return real(*a)
    Q._git = fake
    Q._unmark_text = functools.lru_cache(maxsize=None)(Q._unmark)


def key(receipt, lit):
    return f'{receipt}\t{json.dumps(lit, ensure_ascii=False)}'


def main():
    sha = Q._git('rev-parse', 'HEAD').stdout.strip()
    install(sha)
    rows = paper_rows()
    absent = sorted({key(r, l) for r, l in rows if not Q._present_at(sha, l, 'PAPER', r)})
    live = {key(r, l) for r, l in rows}
    print(f'  PAPER PINS PRESENT -- at {sha[:8]}: {len(rows)} PAPER row(s), {len(absent)} absent from every '
          f'corpus/*.tex')
    if '--update' in sys.argv:
        with open(ABSENT, 'w', encoding='utf-8') as f:
            f.write('# PAPER rows of quote_pin_baseline.tsv whose literal is in no corpus/*.tex -- CANDIDATES, not\n'
                    '# verdicts (no green-receipt filter).  Written by `check_paper_pins_present.py --update`; it may\n'
                    '# only shrink.  receipt<TAB>literal-as-JSON\n')
            f.write(''.join(a + '\n' for a in absent))
        print(f'  wrote {len(absent)} key(s) to {os.path.relpath(ABSENT, ROOT)}')
        return 0
    if '--counts' in sys.argv:
        return 0
    have = {ln for ln in open(ABSENT, encoding='utf-8').read().split('\n') if ln and not ln.startswith('#')}
    new = [a for a in absent if a not in have]
    stale = sorted(have - set(absent))
    gone = [s for s in stale if s not in live]

    # ── the two-sided seed, through the same call ───────────────────────────────────────────────────────
    absent_set = set(absent)
    present = [(r, l) for r, l in rows if key(r, l) not in absent_set and len(l) > 12 and '\\' not in l]
    seed_ok = bool(present)
    if seed_ok:
        r, l = present[0]
        mutant = l[:6] + ('Q' if l[6] != 'Q' else 'Z') + l[7:]
        seed_ok = Q._present_at(sha, l, 'PAPER', r) and not Q._present_at(sha, mutant, 'PAPER', r)
    print(f'    NEW   (absent, not listed):            {len(new)}')
    print(f'    STALE (listed, now present or gone):   {len(stale)}  ({len(gone)} no longer a live row)')
    print(f'    SEED  present read present, one-character mutant read absent: {seed_ok}')
    bad = False
    for a in new[:10]:
        print(f'  ⛔ [FAIL] NEW absent PAPER pin: {a[:160]}')
    for s in stale[:10]:
        print(f'  ⛔ [FAIL] STALE listed key: {s[:160]}')
    if new or stale:
        bad = True
        print('     A NEW key is a PAPER pin whose literal is in no paper: restore the sentence, repair the pin, or --'
              ' if the absence is deliberate -- list it with `--update` in the same commit and say why.  A STALE '
              'key is the list lagging the tree: `python3 corpus/check_paper_pins_present.py --update`.')
    if not seed_ok:
        bad = True
        print('  ⛔ [FAIL] SEED: the control did not read two-sidedly, so this gate cannot tell present from absent')
    if bad:
        return 1
    print('  no new absent PAPER pin; the list is current; the seed reads both ways.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
