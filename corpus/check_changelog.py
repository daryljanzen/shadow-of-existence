#!/usr/bin/env python3
"""check_changelog.py -- the gate on the CHANGELOG, thirteenth of the corpus's gates.

THE_PLAN's four-step state advance, step 1: "Log CORPUS_MAP.md -- a dated `### Revision rNNN`
entry in house style: what changed and why."  ** Nothing failed when it was skipped, and it was
skipped 107 times. **

Found r2377: CORPUS_MAP carried ONE `### Revision` entry for a fork that ran 108 revisions.  The
gap cannot be repaired after the fact -- a changelog is the one grain where a claim and its later
correction sit in the same record, and reconstructing entries from the register would invent that
record.  ** So the only defence is a gate that fires while the memory is still in the room. **

WHAT IT MEASURES.  The fork front (the highest c54.N anywhere in the standing documents) against
the newest revision CORPUS_MAP actually LOGS.  A log entry is `### Revision r<N>` or
`### Revision r2376+c54.<N>`; a mention of a revision in prose is not an entry, and the gate does
not count it -- that distinction is the whole point, since the r2377 defect was precisely a file
full of revision numbers and empty of revision entries.

TWO LOGS, AND THE GATE MUST NOT CONFLATE THEM (refined the same revision it was written).  A first
draft measured the FORK front against the FORK entries and failed at 124, which is true and is
**not repairable** -- that gap is the working fork's, it is closed as far as it can be by the
copied commit record, and a gate that fails forever on an unrepairable fact gets ignored, which is
the failure mode this whole family exists to prevent.  ** So the gate FAILS on what this line can
actually discharge -- its own unlogged advances -- and REPORTS the fork's historical gap beside it,
with the pointer to the fork-span record. **  Reporting it is not softening: an unrepairable gap
that is stated every run is a gap nobody re-discovers.

WHY THE FORK-SPAN SECTION DOES NOT SATISFY IT.  scripts/build_fork_span.py copies commit subjects
into CORPUS_MAP verbatim, which is an honest record at the weight a commit subject carries.  It is
NOT a changelog entry and is not counted here.  The gate reports it separately so the two are never
confused.

    python3 corpus/check_changelog.py

Written r2378.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
MAP = os.path.join(ROOT, 'CORPUS_MAP.md')
WINDOW = 3          # revisions the log may trail the front before it is a failure

FRONT_DOCS = ['THE_LIVE_ARC.md', 'THE_PLAN.md', 'WHATS_TEED_UP.md', 'FORK_HISTORY_c54.txt',
              'THE_OPEN_PROBLEMS_LEDGER.md', 'OPEN_PROBLEMS_MAP.md']

# documents this line writes: work described in them must be logged in the main-line changelog
LINE_DOCS = ['THE_STAGED_REVISIONS.md', 'CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md',
             'EDITS_r2377.md']


def line_front():
    """the highest main-line revision this line's own documents describe work at"""
    best, whence = 0, None
    for n in LINE_DOCS:
        p = os.path.join(ROOT, n)
        if not os.path.exists(p):
            continue
        rs = [int(x) for x in re.findall(r'\br(2[3-9]\d\d)\b',
              open(p, encoding='utf-8', errors='replace').read())]
        if rs and max(rs) > best:
            best, whence = max(rs), n
    return best, whence


def fork_front():
    best, whence = 0, None
    for n in FRONT_DOCS:
        p = os.path.join(ROOT, n)
        if not os.path.exists(p):
            continue
        rs = [int(x) for x in re.findall(r'c54\.(\d+)',
              open(p, encoding='utf-8', errors='replace').read())]
        if rs and max(rs) > best:
            best, whence = max(rs), n
    return best, whence


def logged():
    if not os.path.exists(MAP):
        return None, None, 0
    t = open(MAP, encoding='utf-8', errors='replace').read()
    body = t.split('<!-- FORK-SPAN')[0]          # the fork span is not a changelog
    fork = [int(x) for x in re.findall(r'^### Revision r2376\+c54\.(\d+)', body, re.M)]
    main = [int(x) for x in re.findall(r'^### Revision r(\d{3,4})\b', body, re.M)]
    span = len(re.findall(r'\| .*?\*\*c54\.\d+\*\* \|', t))
    return (max(fork) if fork else None), (max(main) if main else None), span, len(fork)


def main():
    front, whence = fork_front()
    newest_fork, newest_main, span_rows, fork_entries = logged()
    print()
    print('  CHANGELOG -- does the log know about the work?')
    print()
    if front == 0:
        print('  [FAIL] cannot read the fork front from any standing document.')
        return 1
    print(f'  fork front:            c54.{front}   (from {whence})')
    print(f'  newest fork entry:     ' +
          (f'c54.{newest_fork}' if newest_fork is not None else 'NONE'))
    print(f'  fork entries in total: {fork_entries}')
    print(f'  newest main-line entry: ' +
          (f'r{newest_main}' if newest_main is not None else 'NONE'))
    if span_rows:
        print(f'  fork-span rows:        {span_rows}   '
              f'(copied commit subjects -- NOT changelog entries, not counted)')
    print()

    # ---- REPORTED: the working fork's historical gap, not this line's to discharge
    fork_gap = front - newest_fork if newest_fork is not None else front
    print(f'  [REPORT] the WORKING FORK\'s changelog gap is {fork_gap} revisions '
          f'({fork_entries} entry(s) for a fork that has run {front}).')
    print( '           Not repairable and not this line\'s to discharge: a changelog is the one')
    print( '           grain where a claim and its later correction sit in the same record, so')
    print( '           reconstructing entries would invent it.  What exists is copied verbatim')
    print(f'           into CORPUS_MAP\'s fork-span section ({span_rows} commit subjects).')
    print( '           Stated every run so nobody re-discovers it as news.')
    print()

    # ---- FAILED ON: this line's own advances
    lf, lw = line_front()
    if lf == 0:
        print('  no main-line work described in this line\'s documents; nothing to log.')
        print()
        return 0
    print(f'  main-line work described at: r{lf}   (in {lw})')
    if newest_main is None or newest_main < lf:
        print(f'  [FAIL] the newest main-line changelog entry is '
              f'{"NONE" if newest_main is None else "r" + str(newest_main)}, '
              f'behind the work described at r{lf}.')
        print()
        print('  ⛔ This is step 1 of the four-step state advance, and it is the step whose')
        print('     lapse is LEAST RECOVERABLE.  A stale card can be re-read from source; a')
        print('     missing changelog entry cannot be written later without inventing it,')
        print('     because the reasoning it was meant to hold is gone with the session.')
        print('     Log the advance now, while it is still in the room.')
        return 1
    print(f'  The main-line log is current: newest entry r{newest_main}.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
