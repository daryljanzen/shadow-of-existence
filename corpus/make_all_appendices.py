#!/usr/bin/env python3
"""make_all_appendices.py -- regenerate EVERY Appendix R from receipts/INDEX.md, in one call.

Why this exists.  The appendices are generated, and the generator took one paper at a time,
so regenerating meant remembering eighteen invocations with two different filename
conventions (P01..P09 zero-padded, P10..P17 not).  Nobody remembered.  At r2376+c54.36 the
appendices had not been regenerated in roughly a hundred revisions and the corpus carried
** 105 dead receipt hyperlinks across twelve papers ** -- every \\rcpt{} added since the last
run rendered as a marker linking nowhere.  check_compile.py now fails on them; this is the
one command that fixes them.

Run:  python3 make_all_appendices.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, 'make_receipt_appendix.py')

# scope -> the appendix filename it must be written to (the two conventions, spelt out once)
TARGETS = [(f"P{n}", f"appendix_receipts_P{n:02d}.tex" if n < 10
            else f"appendix_receipts_P{n}.tex") for n in range(1, 18)]
TARGETS.append(('corpus', 'appendix_receipts_corpus.tex'))


def main():
    fails = []
    for scope, out in TARGETS:
        path = os.path.join(HERE, out)
        if not os.path.exists(path):
            print(f"  [skip] {out} -- no such appendix in the corpus")
            continue
        p = subprocess.run([sys.executable, GEN, scope, path], cwd=HERE,
                           capture_output=True, text=True, errors='replace')
        if p.returncode:
            fails.append(out)
            print(f"  [FAIL] {out}\n{p.stderr.strip()}")
        else:
            print("  " + p.stdout.strip().replace("\n", "\n  "))
    print()
    if fails:
        print(f"  {len(fails)} appendix/appendices failed to generate.")
        return 1
    print("  All Appendix R files regenerated from receipts/INDEX.md.")
    print("  Now run check_compile.py -- it fails on any receipt link left dead.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
