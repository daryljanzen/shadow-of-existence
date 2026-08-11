#!/usr/bin/env python3
"""audit_index.py -- ** DOES `INDEX.md` LIST THE DOCUMENTS A NODE HAS TO FIND? **

Built r2376+c54.167, discharging front #19.

** WHY IT EXISTS. **  At c54.166 the index was 132 revisions stale and fourteen substantive top-level
documents were absent from it -- including `THE_WORK.md`, the live front list, and `THE_BASE_RATE.md`,
which carries what this fork has learned about its own failures.  ** An index that omits the document a
node should open first is worse than no index: it answers the question wrongly rather than not at all. **

`check_currency` could not see this.  It reads the highest revision a register MENTIONS, so an index can
be perfectly current by that measure and still not list half the corpus -- and a node bringing one
current by writing a date at the top would satisfy the gate and fix nothing.  ** That is the same shape
as entry twenty-seven one layer along: the gate's measure was not the thing that mattered. **

EXCLUSIONS, named rather than pattern-hidden:
  * `BUNDLE_*.md`             per-revision manifests -- append-only records, not navigable documents
  * `gate_session_notes_*.md` spin-up notes -- same
Listing either would bury the rows that matter, which is the only reason they are out.

Usage:  python3 scripts/audit_index.py           # report
        python3 scripts/audit_index.py --strict  # exit 1 on any unlisted document
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
INDEX = os.path.join(ROOT, 'INDEX.md')

EXCLUDE_PREFIX = ('BUNDLE_', 'gate_session_notes')
EXCLUDE_EXACT = ('INDEX.md',)


def main(argv):
    idx = open(INDEX, encoding='utf-8', errors='replace').read()
    docs = sorted(f for f in os.listdir(ROOT) if f.endswith('.md'))
    considered, excluded, missing = [], [], []
    for f in docs:
        if f.startswith(EXCLUDE_PREFIX) or f in EXCLUDE_EXACT:
            excluded.append(f)
            continue
        considered.append(f)
        if f not in idx:
            missing.append(f)
    print()
    print(f"  INDEX AUDIT -- {len(docs)} top-level document(s): {len(considered)} navigable, "
          f"{len(excluded)} excluded by name")
    print(f"    {len(considered) - len(missing):>4} listed in INDEX.md")
    print(f"    {len(missing):>4} NOT listed")
    if missing:
        print()
        print("  ⛔ UNLISTED:")
        for f in missing:
            print(f"     {f}")
        print()
        print("  ** An index that omits the document a node should open first answers the question")
        print("  wrongly rather than not at all. **  Add a row, or add the file to the named")
        print("  exclusions above with the reason -- silently is the one option that is not open.")
        return 1 if '--strict' in argv else 0
    print()
    print("  Every navigable top-level document is listed.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
