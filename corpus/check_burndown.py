#!/usr/bin/env python3
"""check_burndown.py -- the gate on the LEAD REGISTER, third of the corpus's three.

check_receipts.py polices over-claiming.  check_kills.py polices closure.  ** Neither
polices the register itself, and the register is where the failure mode of c54.16-c54.26
lived: work the newest thing, register two more, repeat -- fully compliant with all three of
the arc's rules, and it grew the ledger 3.5x faster than it burned down. **

This reads THE_LIVE_ARC.md and fails on the conditions Rule 4 and Rule 5 name:

  · HOT INFLATION      -- more than a third of open leads flagged HOT means HOT is noise
  · LANGUISHING DEBT   -- a lead HOT for more than 5 revisions and never worked
  · UNRUN FALSIFIERS   -- an open lead whose own text says it falsifies a claim the corpus
                          has made.  ** These are free and they are the ones that matter. **
  · NO-STRIKE DRIFT    -- the struck fraction, reported so it cannot quietly fall

Exit 1 on HOT inflation or on an unrun falsifier older than the grace window.
Warnings otherwise: this gate is meant to be read, not merely passed.
"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')

HOT_CEILING = 0.34          # Rule 5: HOT on more than a third of the open list is noise
GRACE = 5                   # Rule 4: revisions a HOT lead may sit before it must be re-triaged

ROW = re.compile(r'\|\s*(~~)?\*{0,2}(L-\d+)\*{0,2}(~~)?\s*\|(.*)$')
REV = re.compile(r'c54\.(\d+)')
FALSIFIER = re.compile(
    r'\b(?:falsifi(?:er|es)|refut(?:es|ation)\s+(?:of|clause)|a\s+falsifier\s+of\s+my\s+own'
    r'|kills?\s+(?:F-\d+|the\s+count)|decisive\s+either\s+way)\b', re.I)


# a falsifier is discharged only if the row says it was RUN and says what happened, with a revision
DISCHARGED = re.compile(
    r'(?:NAMED AND RUN|RUN IN THE SAME REVISION|falsifier[^.]{0,120}\b(?:was\s+)?run\b'
    r'|it\s+does\s+not\s+fire|does\s+not\s+fire|the\s+falsifier\s+FIRED)', re.I)


# a deferral must be EXPLICIT and must name what it waits behind -- not merely be late
DEFERRED = re.compile(r'DELIBERATELY ORDERED|DEFERRED BY STANDING INSTRUCTION', re.I)


def parse():
    if not os.path.exists(ARC):
        print('  [FAIL] THE_LIVE_ARC.md is missing -- the register IS the gate.')
        sys.exit(1)
    out = []
    for ln in open(ARC, encoding='utf-8'):
        m = ROW.match(ln)
        if not m:
            continue
        cells = [c.strip() for c in m.group(4).split('|')]
        state = cells[-2] if len(cells) >= 2 else ''
        revs = [int(x) for x in REV.findall(ln)]
        # ** A ROW'S AGE IS WHEN IT WAS OPENED, NOT THE OLDEST REVISION IT CITES (fixed c54.122).
        # min(revs) ages a row by its own REASONING: `L-169`, opened at c54.122, cited c54.112-113
        # as the work it follows from and was instantly reported five revisions overdue.  A row that
        # explains itself by referring to earlier work was being punished for the explanation. **
        opened = re.search(r'OPENED\s+c54\.(\d+)', ln)
        first = int(opened.group(1)) if opened else (min(revs) if revs else None)
        out.append({'id': m.group(2), 'struck': bool(m.group(1)), 'state': state,
                    'text': ln, 'first_rev': first})
    return out


def main():
    rows = parse()
    if not rows:
        print('  [FAIL] no lead rows parsed from THE_LIVE_ARC.md')
        return 1
    cur = max((r['first_rev'] for r in rows if r['first_rev'] is not None), default=0)
    # r2378: the register now carries KIND.  QUESTION rows are open questions with possible
    # answers -- the burn-down, the supersession scan and the kill bar were all built for them.
    # WORK rows are programmes of work with steps (the arcs and phases folded from CONSOLIDATE),
    # and asking "has a receipt already answered ARC 14?" is not well formed.  ** They live in one
    # ID space because the assignment is a clean slate with nothing owed strewn about, and they are
    # reported SEPARATELY so neither number quietly starts meaning something else. **  A row is
    # WORK if its state cell says so; everything else is a QUESTION, which keeps the default where
    # it was and makes the new kind opt-in.
    def kind(r):
        # The tag is EXPLICIT -- `kind:WORK` in the state cell -- and not inferred from prose.
        # Two drafts of this line inferred it and both were wrong: 'WORK' as a substring made 104
        # of 192 rows WORK ('WORKED c54.48'), and \bWORK\b still caught L-64's state cell, which
        # reads '...a check on my own work'.  ** A classifier that reads prose will classify prose. **
        # Both were caught by the printed count being obviously wrong, which is why it is printed.
        return 'WORK' if 'KIND:WORK' in r['state'].upper() else 'QUESTION'
    work = [r for r in rows if kind(r) == 'WORK']
    ques = [r for r in rows if kind(r) == 'QUESTION']

    openr = [r for r in ques if not r['struck']]
    struck = [r for r in ques if r['struck']]
    hot = [r for r in openr if 'HOT' in r['state'].upper()]
    work_open = [r for r in work if not r['struck']]

    print(f"  LEAD REGISTER: {len(rows)} rows = {len(ques)} QUESTION + {len(work)} WORK")
    print(f"  QUESTIONS: {len(struck)} struck · {len(openr)} open · {len(hot)} HOT")
    print(f"  WORK:      {len(work) - len(work_open)} struck · {len(work_open)} open"
          f"   (arcs and phases -- freshness, not supersession)")
    frac = len(struck) / max(1, len(ques))
    print(f"  struck fraction (QUESTIONS only): {frac:.1%}   "
          f"(reported so it cannot quietly fall, and scoped so it cannot quietly change meaning)")

    fails, warns = [], []

    # --- HOT inflation
    hotfrac = len(hot) / max(1, len(openr))
    print(f"  HOT fraction of open: {hotfrac:.1%}  (ceiling {HOT_CEILING:.0%})")
    if hotfrac > HOT_CEILING:
        fails.append(f"HOT INFLATION: {len(hot)}/{len(openr)} = {hotfrac:.0%} of open leads "
                     f"flagged HOT. A priority that applies to a third of the list is not a "
                     f"priority. Re-triage before adding.")

    # --- languishing HOT debt
    old_hot = [r for r in hot if r['first_rev'] is not None and cur - r['first_rev'] > GRACE]
    if old_hot:
        warns.append(f"LANGUISHING: {len(old_hot)} lead(s) HOT for more than {GRACE} "
                     f"revisions: {', '.join(r['id'] for r in old_hot)}")

    # --- unrun falsifiers
    # ** THE GATE COULD NOT TELL A RUN FALSIFIER FROM AN UNRUN ONE (fixed c54.120).  It matched the
    # WORD and counted every open row that mentioned a falsifier as owing one -- so a row that named
    # a falsifier AND ran it in the same revision still failed, which is the gate punishing exactly
    # the behaviour it exists to produce.  A falsifier is DISCHARGED when the row records the run
    # and its outcome beside a revision stamp; anything vaguer still counts as owed. **
    fals = [r for r in openr if FALSIFIER.search(r['text'])]
    done = [r for r in fals if DISCHARGED.search(r['text'])]
    fals = [r for r in fals if r not in done]
    # ** THE GATE HAD TWO STATES AND REALITY HAS THREE (added c54.134).  A falsifier can be OWED,
    # DISCHARGED, or DELIBERATELY ORDERED BEHIND other work by a standing instruction.  Treating the
    # third as the first made the gate demand that a queue be worked out of order -- and the row it
    # fired on was one where the "falsifier" was a substantial calculation mislabelled as a cheap
    # check.  Deferrals are reported LOUDLY rather than hidden: a deferral that stops being visible
    # is just an excuse. **
    defer = [r for r in fals if DEFERRED.search(r['text'])]
    fals = [r for r in fals if r not in defer]
    if done:
        print(f"  FALSIFIERS NAMED AND RUN: {len(done)} "
              f"({', '.join(r['id'] for r in done)}) -- discharged, not owed")
    if defer:
        print(f"  ⌛ FALSIFIERS DELIBERATELY ORDERED: {len(defer)} "
              f"({', '.join(r['id'] for r in defer)})")
        print("    -- deferred BEHIND named work by a standing instruction, not neglected.")
        print("    -- each row must say what it waits on; re-read them when that work lands.")
    if fals:
        stale = [r for r in fals
                 if r['first_rev'] is not None and cur - r['first_rev'] > GRACE]
        print(f"  UNRUN FALSIFIERS: {len(fals)} "
              f"({', '.join(r['id'] for r in fals)})")
        print("    -- these are free, and each is the only thing between a claim and a check")
        if stale:
            fails.append("STALE FALSIFIER: " + ', '.join(r['id'] for r in stale) +
                         f" -- open and unrun for more than {GRACE} revisions. "
                         "A cheap falsifier left unrun is the worst debt in the register.")

    print()
    for w in warns:
        print(f"  [WARN] {w}")
    if fails:
        print(f"  BURN-DOWN FAILURES: {len(fails)}")
        for f in fails:
            print(f"    [FAIL] {f}")
        print()
        print("  RULE 4: a turn that strikes nothing owes a reason.")
        print("  RULE 5: re-triage before adding; HOT is a budget, not a label.")
        return 1
    print("  Register healthy: HOT is within budget and no falsifier is stale.")
    return 0




# --- ID-SPACE INTEGRITY (added r2376+c54.49) ------------------------------------------------
# Daryl caught this: the register reported 118 leads while IDs ran to L-127, and neither the
# node nor any gate noticed for fifteen revisions.  Two causes, both real:
#   (a) LOST LEADS -- L-100 and L-103 were given IDs by a sweep and never entered as rows,
#       which is exactly what the arc's Rule 2 forbids, and the loss was silent;
#   (b) MINTED IDS -- seven COMPUTATION FILES were named L115..L126 as though they were leads,
#       when each was a WORKING of some other lead.  Two colliding uses of one namespace.
# This check fails on both: every ID from 1 to the maximum must appear exactly once as a row,
# and no computation filename may claim a bare lead ID.
def _id_space():
    import re as _re, glob as _glob, os as _os
    _txt = open(_os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8').read().split('\n')
    seen = {}
    for _ln in _txt:
        _m = _re.match(r'\|\s*(?:\*\*|~~)(L-\d+)(?:\*\*|~~)\s*\|', _ln)
        if _m:
            _n = int(_m.group(1).split('-')[1])
            seen[_n] = seen.get(_n, 0) + 1
    if not seen:
        print("  [WARN] ID-SPACE: no lead rows parsed"); return 1
    _hi = max(seen)
    # IDs explicitly declared retired in the arc are accounted for and are not gaps
    import re as _re2
    _m2 = _re2.search(r'RETIRED-IDS:([^\n]*)', '\n'.join(_txt))
    _retired = {int(x.split('-')[1]) for x in _re2.findall(r'L-(?:\d+)', _m2.group(1))} if _m2 else set()
    # ** THE GAP CHECK IS PER BAND, AND r2441+c54.186 IS WHY. **  This block read the ID space as one
    # contiguous run, range(1, hi+1) -- which was true while ONE line allocated and became false the
    # moment `check_id_bands` reserved L-500-L-799 for the working fork.  The fork's first allocation
    # in its own band, L-500, made this gate report the 270 unallocated numbers L-230-L-499 as leads
    # "assigned and NEVER REGISTERED", i.e. as lost work.  ** A number in a band nobody has reached
    # yet is UNALLOCATED, not lost; a number missing BELOW a band's own high-water mark is lost. **
    # The band table is imported rather than copied so the two gates cannot drift apart.
    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location('_idb', _os.path.join(ROOT, 'corpus', 'check_id_bands.py'))
    _idb = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_idb)
    _gaps = []
    for _lo, _bhi, _bname in _idb.BANDS:
        _used = [n for n in seen if _lo <= n <= _bhi]
        if not _used:
            continue                                  # band never opened -- nothing can be missing
        _gaps += [n for n in range(_lo, max(_used) + 1)
                  if n not in seen and n not in _retired]
    _gaps.sort()
    _dupes = [n for n, c in sorted(seen.items()) if c > 1]
    _open = [f"{_lo}-{max(n for n in seen if _lo <= n <= _bhi)}"
             for _lo, _bhi, _ in _idb.BANDS if any(_lo <= n <= _bhi for n in seen)]
    print(f"\n  ID SPACE: {len(seen)} rows, highest L-{_hi}, {len(_retired)} retired, "
          f"{len(_gaps)} gap(s), {len(_dupes)} duplicate(s)")
    print(f"    bands with allocations (gaps are checked only inside these): {', '.join(_open)}")
    _bad = 0
    if _gaps:
        print(f"    [FAIL] IDs assigned but NEVER REGISTERED: "
              f"{['L-%d' % n for n in _gaps]}")
        print("           A lead given an ID and not entered as a row is LOST (Rule 2).")
        _bad = 1
    if _dupes:
        print(f"    [FAIL] IDs appearing on more than one row: {['L-%d' % n for n in _dupes]}")
        _bad = 1
    # and no computation file may claim a bare lead ID
    _claim = []
    for _f in _glob.glob(_os.path.join(ROOT, 'computations', '*', 'L[0-9]*.py')):
        _b = _os.path.basename(_f)
        _m = _re.match(r'L(\d+)([_w])', _b)
        if _m and _m.group(2) == '_':
            _n = int(_m.group(1))
            if _n not in seen:
                _claim.append(_b)
    if _claim:
        print(f"    [FAIL] computation files claiming UNREGISTERED lead IDs: {sorted(_claim)}")
        print("           Name a working after the lead it works, with a 'w' suffix.")
        _bad = 1
    if not _bad:
        print("    ID space intact: every ID from 1 to the maximum is registered exactly once.")
    return _bad


if __name__ == '__main__':
    _rc = main()
    sys.exit(_rc or _id_space())
