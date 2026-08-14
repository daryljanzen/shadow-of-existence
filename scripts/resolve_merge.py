#!/usr/bin/env python3
"""resolve_merge.py -- RESOLVE A MERGE WITHOUT DESTROYING BINARIES.

** WHY.  r2736: ** *** merging c54.218, this line ran a conflict-marker stripper over every `UU` path
with `encoding='utf-8', errors='replace'` and wrote each back.  **On a binary that substitutes U+FFFD
for every invalid byte.  Seventeen PDFs came out matching NEITHER parent** -- `matter_sector` went
703,274 / 708,206 bytes in to 1,267,092 out. ***

** ⛔ AND EVERY SURFACE CHECK PASSED. **  *** `%PDF` header present ✔ · `%%EOF` present ✔ · no
conflict-marker text ✔ · disk hash == `HEAD` ✔.  **All four were true of a destroyed file**, and the
last was true BECAUSE the destruction was already committed.  The test that found it was comparing
against **BOTH PARENTS** -- the only comparison that distinguishes "merged" from "mangled". ***

** THE RULE THIS ENCODES. **  *** A merge resolver must dispatch on FILE KIND before it touches
content.  Text can be marker-stripped; a binary can only be TAKEN FROM A SIDE.  There is no
"resolve" operation on a PDF, and treating one uniformly with a markdown file is not a shortcut but a
category error. ***

    python3 scripts/resolve_merge.py            # resolve, then verify against both parents

Written r2736.  Stated for reversal.
"""
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** regenerated wholly by scripts/ -- ours, then rebuild. **
REGEN = {'BOARD.md', 'ID_SPACE_CENSUS.md', 'THE_WORK_EDGE.md', 'TEED_UP.md',
         'BURN_DOWN.md', 'GRAIN_CURRENCY.md', 'MAP_STATUS.md'}
BINARY = ('.pdf', '.png', '.jpg', '.zip', '.gz', '.bundle')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def show(ref, f):
    return subprocess.run(['git', 'show', f'{ref}:{f}'], cwd=ROOT, capture_output=True).stdout


def main():
    st = subprocess.run(['git', 'status', '--short'], cwd=ROOT,
                        capture_output=True, text=True).stdout
    conf = [l[3:].strip() for l in st.split('\n') if l.startswith('UU')]
    if not conf:
        print('  no conflicts')
        return 0

    binaries = [f for f in conf if f.lower().endswith(BINARY)]
    regen = [f for f in conf if os.path.basename(f) in REGEN]
    text = [f for f in conf if f not in binaries and f not in regen]

    print()
    print(f'  {len(conf)} conflict(s): {len(binaries)} binary · {len(regen)} regenerated · '
          f'{len(text)} text')
    print()

    # ⛔ BINARIES: taken from a side, NEVER rewritten.
    for f in binaries:
        subprocess.run(['git', 'checkout', 'MERGE_HEAD', '--', f], cwd=ROOT)
    if binaries:
        print(f'  {len(binaries)} binary path(s) TAKEN from MERGE_HEAD, not rewritten')

    for f in regen:
        subprocess.run(['git', 'checkout', '--ours', '--', f], cwd=ROOT)
    if regen:
        print(f'  {len(regen)} regenerated path(s) taken ours (rebuild after)')

    for f in text:
        p = os.path.join(ROOT, f)
        t = open(p, encoding='utf-8', errors='replace').read()
        for pat in (r'^<<<<<<< [^\n]*\n', r'^=======\n', r'^>>>>>>> [^\n]*\n'):
            t = re.sub(pat, '', t, flags=re.M)
        open(p, 'w', encoding='utf-8').write(t)
    if text:
        print(f'  {len(text)} text path(s) marker-stripped, both sides kept')

    subprocess.run(['git', 'add', '-A'], cwd=ROOT)

    # ⛭ THE VERIFICATION THAT FOUND IT: against BOTH parents.
    bad = []
    for f in binaries:
        d = open(os.path.join(ROOT, f), 'rb').read()
        if sha(d) not in (sha(show('HEAD', f)), sha(show('MERGE_HEAD', f))):
            bad.append(f)
    print()
    if bad:
        print(f'  ⛔ {len(bad)} binary path(s) match NEITHER parent -- MANGLED:')
        for f in bad:
            print(f'      {f}')
        return 1
    print(f'  ✔ all {len(binaries)} binary path(s) verified byte-identical to a parent')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
