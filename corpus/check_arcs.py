#!/usr/bin/env python3
"""check_arcs.py -- the freshness gate on WORK rows, fourteenth of the corpus's gates.

** THIS GATE CLOSES A GAP THE r2378 FOLD ITSELF OPENED, and that is why it exists. **

ARC 14 step 2 folded CONSOLIDATE's fifteen arcs and §13's nine phases into the lead register as
`kind:WORK` rows -- one ID space, because the assignment is a clean slate with nothing owed strewn
about.  The register's other gates were built for QUESTION rows and were deliberately scoped away
from WORK: check_supersession skips them (scoring a programme of work against 268 receipts is
noise), and check_kills' bar is for questions.  ** So for one revision the WORK rows had LESS
watching them than they had as prose in CONSOLIDATE. **  A fold that reduces coverage is not a fold.

WHAT AN ARC ACTUALLY LACKS, and it is not supersession.  ARC 11 sat at "2 of 7 lanes" for hundreds
of revisions with nothing noticing.  An arc does not go stale by being answered elsewhere; it goes
stale by ** its state block standing still while the work it tracks moves. **  So the measure is:

    does the arc's own state text carry a revision marker no older than WINDOW behind the front?

An arc that is genuinely untouched is fine -- work is ordered, and not every arc is live.  What is
NOT fine is an arc whose state block claims a position it no longer holds, because a node reads it
to decide what to do next.  ** So a stale state block is a WARN, and a state block with NO revision
marker at all is a FAIL: **  the first is a position that may have moved; the second is a position
that cannot be checked, and an uncheckable claim about what is done is the worse of the two.

    python3 corpus/check_arcs.py

Written r2378.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')
# r2378: the arc layer is SPLIT across two documents -- ARCs 1-12, 14, 15 are headed in
# CONSOLIDATE §2 and ** ARC 13 is headed in THE_PLAN **.  Found by this gate reporting
# "no section found" for ARC 13 alone.  Both are searched, and the split is itself worth
# knowing: an arc whose home is not where its siblings live is an arc a node will not find
# by reading §2.
HOMES = ['CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md', 'THE_PLAN.md']

WINDOW = 40         # revisions an arc's state block may lag the front before it is reported

# ** r2378, AND THIS IS THE SAME TRAP check_currency FELL INTO. **  When this gate first failed on
# four undated phases, the honest response was to flag each section as UNDATED rather than invent a
# date -- and the flag itself carries the revision it was written at, so the gate promptly read that
# marker and called all four "ok".  A section made current by writing ABOUT being stale.  So an
# UNDATED-POSITION flag is recognised and its own revision is NOT counted: the row is reported as a
# third state, DECLARED-UNDATED -- not a FAIL, because the gap is honestly stated and pointed at
# where the position actually lives; not "ok", because the position still cannot be checked.
UNDATED = re.compile(r'UNDATED POSITION', re.I)
ROW = re.compile(r'^\|\s*(~~)?\*{0,2}(L-\d+)\*{0,2}(~~)?\s*\|(.*)$')


def read(p):
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def front(text):
    rs = [int(x) for x in re.findall(r'c54\.(\d+)', text)]
    return max(rs) if rs else 0


def work_rows():
    """(id, source-code, whole row) for every kind:WORK row that is not struck."""
    out = []
    for ln in read(ARC).split('\n'):
        m = ROW.match(ln)
        if not m or m.group(1):
            continue
        rest = m.group(4)
        if 'KIND:WORK' not in rest.upper():
            continue
        code = re.search(r'`(ARC \d+|PHASE \d+)`', rest)
        # r2380: not every WORK row is an arc or a phase.  L-203/L-204 are the R-M and R-P reach
        # stations, whose positions live in their own documents.  ** A gate that only knows ARC and
        # PHASE reports "no section found" for anything else, which is its parser failing and not
        # the tree. **  So fall back to the document named in the row's ORIGIN cell.
        doc = None
        if not code:
            cells = [c.strip() for c in rest.split(' | ')]
            origin = cells[1] if len(cells) > 1 else ''
            # ALL documents named in the origin, not the first: a position is only as fresh as its
            # STALEST home, and taking the first resolved L-203/L-204 to THE_PLAN (current) when the
            # position they actually track lives in the reach documents (c54.19).
            ds = [x if x.endswith('.md') else x + '.md'
                  for x in re.findall(r'`([A-Z0-9_]+(?:\.md)?)`', origin)]
            doc = [d for d in ds if os.path.exists(os.path.join(ROOT, d))] or None
        out.append((m.group(2), code.group(1) if code else doc, rest))
    return out


def doc_state(names):
    """A WORK row homed in documents: return the head of the STALEST of them.

    A position is only as fresh as its stalest home.  Taking the first named document resolved
    L-203/L-204 to THE_PLAN (current) when the positions they track live in the reach documents,
    which are at c54.19 -- a pass bought by reading the wrong file.
    """
    best = None
    for n in names:
        p = os.path.join(ROOT, n)
        if not os.path.exists(p):
            continue
        head = open(p, encoding='utf-8', errors='replace').read(3000)
        rs = [int(x) for x in re.findall(r'c54\.(\d+)', head)]
        r = max(rs) if rs else -1
        if best is None or r < best[0]:
            best = (r, head, n)
    return best[1] if best else None


def state_text(consol, code):
    """The arc's or phase's own section text in CONSOLIDATE, as far as its next heading."""
    if not code:
        return None
    # arcs are named in §2 headings, phases in §13 '## PHASE N ·' headings
    if code.startswith('PHASE'):
        m = re.search(r'^## PHASE ' + code.split()[1] + r' ·(.*?)(?=^#{2,3} |\Z)',
                      consol, re.S | re.M)
        return m.group(1) if m else None
    # r2378: arcs are HEADINGS (### / ## ⌖ / ## ⌖⌖ ARC N ·), not the first prose mention.  A first
    # draft matched `ARC N` anywhere and then ran to the next `ARC \d`, which for several arcs
    # grabbed a passing mention inside the layer-sequence paragraph -- an extraction bug that would
    # have been reported as the DOCUMENT's defect.  ** A gate must fail on the tree, never on its
    # own parser. **  Match the heading, then read to the next heading of any level.
    n = code.split()[1]
    m = re.search(r'^#{2,3}[^\n]*?\bARC ' + n + r'\b(?![\d])(.*?)(?=^#{2,3} |\Z)',
                  consol, re.S | re.M)
    return m.group(1) if m else None


# ** ---- ADDED r2535: THE SELF-DECLARED-DONE CHECK ---- **
# A row whose own NEXT-STEP field says the work was done, while the row is still LIVE, is a claim the
# register makes about itself and nothing was checking it.  Four instrument rows (L-512, L-515, L-516,
# L-517) sat live for twenty revisions with next-step fields reading "done in the registering revision";
# FOR_54 items 24 and 29 had the same shape.  ** The gates that catch a stale FIELD do not catch a stale
# STATE. **
_DONE_PHRASES = (
    'done in the registering revision',
    'done in its registering revision',
    'DO NOT ACT ON THIS ITEM',
    'nothing remains',
    'discharged in the same revision',
)


def check_self_declared_done(text):
    """Report live rows whose own next-step field says the work is finished."""
    import re as _re
    bad = []
    for line in text.split('\n'):
        m = _re.match(r'\|\s*\*\*(L-\d+)\*\*\s*\|', line)
        if not m:
            continue
        cells = line.split(' | ')
        if len(cells) < 4:
            continue
        step = cells[3]
        for ph in _DONE_PHRASES:
            if ph.lower() in step.lower():
                bad.append((m.group(1), ph))
                break
    return bad


def _selfdone_gate():
    """Run the self-declared-done check as part of this gate.  ** Added r2535 so it FAILS rather than
    merely reports: eleven rows sat live with next-step fields saying the work was done, four of this
    line's and seven of 54's, some for twenty revisions. **"""
    import os as _os
    _root = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
    _p = _os.path.join(_root, 'THE_LIVE_ARC.md')
    if not _os.path.exists(_p):
        return 0
    _bad = check_self_declared_done(open(_p, encoding='utf-8', errors='replace').read())
    if not _bad:
        print('    OK    no live row declares its own work done')
        return 0
    for _rid, _ph in _bad:
        print(f'    [FAIL] {_rid} is LIVE and its next-step field says "{_ph}"')
    print('    ⛔ A row whose own text says done is a CLAIM about itself, and it is exactly as')
    print('       auditable as every other claim in the register.  Strike it or give it a real step.')
    return 1


# ** ---- ADDED r2541: THE BOARD-DRIFT CHECK ---- **
# The board's lead texts live in scripts/regen_board.py as a hand-maintained dict, while the register
# row is edited every time the lead moves.  ** The two drift, and the board is what a node reads to
# choose what to work. **  At r2541 four had: L-204's said "stations ③④" after ⑤⑥⑦⑩ were walked;
# L-218, L-230 and L-240 each lagged by one or more findings.
#   ⇒ ** The signal is cheap and exact: if the REGISTER's next-step field cites a later revision than
#     the board's lead text does, the board is behind. **
def check_board_drift():
    """Report leads whose register next-step cites a later revision than the board text."""
    import importlib.util as _ilu
    import os as _os
    import re as _re
    _root = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
    _gen = _os.path.join(_root, 'scripts', 'regen_board.py')
    _arc = _os.path.join(_root, 'THE_LIVE_ARC.md')
    if not (_os.path.exists(_gen) and _os.path.exists(_arc)):
        return []
    _spec = _ilu.spec_from_file_location('_rb', _gen)
    _rb = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_rb)
    out = []
    for line in open(_arc, encoding='utf-8', errors='replace').read().split('\n'):
        m = _re.match(r'\|\s*\*\*(L-\d+)\*\*\s*\|', line)
        if not m:
            continue
        rid = m.group(1)
        cells = line.split(' | ')
        if rid not in _rb.LEADS or len(cells) < 4:
            continue
        rr = {int(x) for x in _re.findall(r'r(\d{4})', cells[3])}
        rl = {int(x) for x in _re.findall(r'r(\d{4})', _rb.LEADS[rid][0])}
        if rr and (not rl or max(rr) > max(rl)):
            out.append((rid, max(rr), max(rl) if rl else None))
    return out


def _board_drift_gate():
    bad = check_board_drift()
    if not bad:
        print('    OK    no lead text lags its register row')
        return 0
    for rid, newest, have in bad:
        print(f'    [FAIL] {rid}: the register cites r{newest}, the board text stops at '
              f'{"r"+str(have) if have else "no revision"}')
    print('    ⛔ THE BOARD IS WHAT A NODE READS TO CHOOSE WHAT TO WORK.  A lead whose text lags its')
    print('       row sends the next node after a question that has already moved.')
    return 1


# ** ---- ADDED r2542: THE CLOSURE-NEIGHBOUR REPORT ---- **
# A row can be stale by pointing FORWARD at something already answered, not only by declaring itself
# finished.  ** L-801 and L-802 both pointed at questions L-245 absorbed and closed at r2537 -- neither
# said "done in the registering revision", so r2535's check could not see them, and both sat at #2 and
# #3 on the board for five revisions. **
#   ⇒ ** A gate for this would have to judge whether one prose next-step is answered by another row's
#     prose finding.  That is the lint-pretending-to-judge-prose failure, and it is refused here. **
#   ⇒ *** What IS mechanical, and would have caught it: when a row CLOSES, the live rows sharing its
#       VEINS are exactly the ones whose next-steps may have just been answered.  L-245, L-801 and
#       L-802 all fed L-165. ***  This REPORTS them.  It never fails.
def check_closure_neighbours():
    """For each vein, list the live leads beside the most recently closed row on it."""
    import importlib.util as _ilu
    import os as _os
    import re as _re
    _root = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
    _gen = _os.path.join(_root, 'scripts', 'regen_board.py')
    if not _os.path.exists(_gen):
        return {}
    _spec = _ilu.spec_from_file_location('_rb2', _gen)
    _rb = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_rb)
    by_vein = {}
    for rid, entry in _rb.LEADS.items():
        for v in (entry[1] or []):
            by_vein.setdefault(v, []).append(rid)
    live = set(_rb.live_rows())
    return {v: sorted(r for r in rs if r in live) for v, rs in by_vein.items()}


def _closure_neighbour_report():
    groups = check_closure_neighbours()
    if not groups:
        return 0
    print()
    print('    ⌗ LIVE LEADS BY VEIN -- when one of these closes, ** read the others: their next-steps')
    print('      are the ones its finding may just have answered. **')
    for v, rs in sorted(groups.items()):
        if rs:
            print(f'        {v}: {", ".join(rs)}')
    print('      (a report, never a failure -- deciding whether one prose next-step is answered by')
    print('       another row\'s finding is a READ, and no script does it)')
    return 0


# ** ---- ADDED r2552: THE DUPLICATE-KEY CHECK ---- **
# ** A duplicate key in a Python dict literal is SILENT: the later entry wins and the earlier one is
# discarded at load. **  regen_board.py's LEADS dict carried TWO `L-171` entries, so an r2552 edit to
# the first was thrown away every time the module was imported -- and the board-drift check (r2541)
# caught the SYMPTOM ("the board text stops at no revision") while the CAUSE was invisible to it.
#   ⇒ *** A generated file's source is code, and a dict literal with a repeated key is a source that
#       silently ignores an edit.  This reads the file as TEXT, because the parsed dict cannot show
#       what it discarded. ***
def check_duplicate_lead_keys():
    """Report LEADS/VEINS keys that appear more than once in the generator's source text."""
    import collections as _c
    import os as _os
    import re as _re
    _root = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
    _gen = _os.path.join(_root, 'scripts', 'regen_board.py')
    if not _os.path.exists(_gen):
        return []
    src = open(_gen, encoding='utf-8', errors='replace').read()
    keys = _re.findall(r"^\s*'(L-\d+)':\s*\(", src, _re.M)
    return sorted(k for k, n in _c.Counter(keys).items() if n > 1)


def _duplicate_key_gate():
    bad = check_duplicate_lead_keys()
    if not bad:
        print('    OK    no duplicate lead key in the board generator')
        return 0
    for k in bad:
        print(f'    [FAIL] {k} appears more than once in regen_board.py')
    print('    ⛔ A DUPLICATE KEY IN A DICT LITERAL IS SILENT: the later entry wins and any edit to')
    print('       the earlier one is discarded at load, with no error anywhere.')
    return 1


def main():
    consol = '\n'.join(read(os.path.join(ROOT, h)) for h in HOMES)
    arctext = read(ARC)
    if not consol or not arctext:
        print('  [FAIL] cannot read CONSOLIDATE or THE_LIVE_ARC.')
        return 1
    cur = max(front(arctext), front(consol))
    rows = work_rows()
    print()
    print('  ARC FRESHNESS -- does a WORK row\'s state block still hold the position it claims?')
    print()
    print(f'  fork front: c54.{cur}   window: {WINDOW} revisions   WORK rows open: {len(rows)}')
    print()
    fails, warns, ok, undated = [], [], [], []
    print(f"  {'row':>7}  {'source':>9}  {'newest marker':>14}   state")
    for lid, code, _ in rows:
        st = doc_state(code) if isinstance(code, list) else state_text(consol, code)
        if st is None:
            fails.append((lid, code, 'no section found in CONSOLIDATE'))
            print(f'  {lid:>7}  {str(code)[:16]:>16}  {"(no section)":>14}   [FAIL]')
            continue
        declared_undated = bool(UNDATED.search(st))
        if declared_undated:
            # strip the flag block so its own revision marker is not read as the position's date
            st = re.sub(r'>\s*\*\*⚠ UNDATED POSITION.*?not-found form:.*?evidence\.\*', '',
                        st, flags=re.S)
            st = re.sub(r'r2\d{3}', '', st)
        rs = [int(x) for x in re.findall(r'c54\.(\d+)', st)]
        rs += [int(x) for x in re.findall(r'\br(1\d{3}|2\d{3})\b', st)]  # main-line revisions
        if not rs:
            if declared_undated:
                undated.append((lid, code))
                print(f'  {lid:>7}  {str(code)[:16]:>16}  {"declared":>14}   [UNDATED]')
                continue
            fails.append((lid, code, 'state block carries NO revision marker'))
            print(f'  {lid:>7}  {str(code)[:16]:>16}  {"none":>14}   [FAIL]')
            continue
        # a main-line rNNNN marker is not comparable to a c54 count; treat its presence as dated
        c54s = [int(x) for x in re.findall(r'c54\.(\d+)', st)]
        if c54s:
            lag = cur - max(c54s)
            tag = f'c54.{max(c54s)}'
        else:
            lag = None
            tag = f'r{max(rs)}'
        if lag is not None and lag > WINDOW:
            warns.append((lid, code, lag))
            print(f'  {lid:>7}  {str(code)[:16]:>16}  {tag:>14}   [WARN] {lag} behind')
        else:
            ok.append(lid)
            # ** the print below was OUTSIDE this else, so a WARN branch reached it with `label`
            # never assigned -- a latent UnboundLocalError that only fires when a warn precedes an
            # ok.  L-210's strike at r2546 was the first ordering that produced it. **
            label = (min(code, key=lambda n: len(n)) if isinstance(code, list) else str(code))
            print(f'  {lid:>7}  {label[:16]:>16}  {tag:>14}   ok')
    print()
    for lid, code, why in fails:
        print(f'  [FAIL] {lid} ({code}): {why}.')
        print( '         An arc whose position cannot be CHECKED is worse than one that has moved:')
        print( '         a node reads the state block to decide what to do next.')
    for lid, code, lag in warns:
        print(f'  [WARN] {lid} ({code}): state block {lag} revisions behind the front.')
    if undated:
        print()
        print(f'  DECLARED-UNDATED: {len(undated)} — ' +
              ', '.join(f'{l} ({c})' for l, c in undated))
        print( '    Each says so in its own section and points at where the position actually lives.')
        print( '    ** Not a pass. **  The gap is honest, not closed: nobody can read these sections')
        print( '    and know what is done.  They clear only when the position is recorded at its home.')
    if fails:
        print()
        print('  ⛔ Arc freshness FAILED.  Give each state block a dated marker, or say in it what')
        print('     it does not cover.  ARC 11 sat at "2 of 7 lanes" for hundreds of revisions with')
        print('     nothing noticing, which is the failure this gate exists for.')
        return 1
    if warns:
        print()
        print('  Arcs lagging but checkable.  Work is ordered and not every arc is live; what this')
        print('  reports is a position that MAY have moved, which is a read and not a defect.')
    elif undated:
        print()
        print('  No undatable positions left unflagged — but see DECLARED-UNDATED above.')
    else:
        print('  Every WORK row\'s state block is dated and within the window.')
    print()
    # ** the self-declared-done check, added r2535 -- see _selfdone_gate below. **
    return (_duplicate_key_gate() or _selfdone_gate() or _board_drift_gate()
            or _closure_neighbour_report())


if __name__ == '__main__':
    sys.exit(main())
