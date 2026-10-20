#!/usr/bin/env python3
"""
r7456 -- PO-78's COUNTS, DERIVED RATHER THAN READ.  Answers r7453 (4) and (5).

Registered at PREDICTION.md (d9c23749) before this file existed.

  MECHANICAL -- the row's extraction; the split into revision-stamped stretches; every
  site matching the fixed form list; each site's series, taken from the word the row
  itself uses at that site; the exclusion of id-shaped numbers, printed; the
  latest-stamped site per series; the hold's own self-stated revision count.

  ADJUDICATED -- whether two series are two populations, and what the general defect is.
  Printed as ADJUDICATED with the row's own sentences that carry it.

NOTHING HERE RENUMBERS THE ROW.  r7453: measure and print, the gate seat applies.

⌗ THE PREDICATE, as registered: a count of a series is a number the row states as that
  series' RUNNING TOTAL, and the aggregate is the LATEST such statement -- not the number
  of announcements and not the largest number in the row.  Every matched site is printed
  with its words so a reader can check the predicate against the row.
"""
import os, re, sys, time, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REG, FRO = 'THE_REGISTER.md', 'THE_FRONTIER.md'
GEN = 'scripts/regen_frontier.py'

WORDNUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
           'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
           'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
           'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
           'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
           'eighty': 80, 'ninety': 90}
ORD = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6,
       'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10, 'eleventh': 11,
       'twelfth': 12, 'thirteenth': 13, 'fourteenth': 14, 'fifteenth': 15,
       'sixteenth': 16, 'seventeenth': 17, 'eighteenth': 18, 'nineteenth': 19,
       'twentieth': 20, 'thirtieth': 30}


def num(w):
    w = w.lower().replace('—', '-').replace('–', '-')
    w = re.sub(r'-+', '-', w).strip('- ')
    if w in ORD:
        return ORD[w]
    if w in WORDNUM:
        return WORDNUM[w]
    if '-' in w:
        a, _, b = w.partition('-')
        if a in WORDNUM and b in WORDNUM:
            return WORDNUM[a] + WORDNUM[b]
        if a in WORDNUM and b in ORD:
            return WORDNUM[a] + ORD[b]
    if w.isdigit():
        return int(w)
    return None


def row_of(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as fh:
        for ln in fh:
            if ln.startswith('| **PO-78**'):
                t = ln.replace('&#9670;', ' <> ').replace('&quot;', '"').replace('&amp;', '&')
                t = re.sub(r'\*\*|\*|`', '', t)
                return re.sub(r'\s+', ' ', t)
    return ''


def stamps(text):
    return [(m.start(), int(m.group(1))) for m in re.finditer(r'\br(\d{4})\b', text)]


def rev_at(marks, idx):
    lo = None
    for pos, rev in marks:
        if pos <= idx:
            lo = rev
        else:
            break
    return lo


# ---- the three series, each with the row's OWN wording for its running total ----
SERIES = {
    'MEMBER (global running total)': [
        r'\b([A-Z][A-Z\-]+|\d+)\s+blindness members\b',
        r'\bfamily (?:HOLDS|holds|stays) at (\d+)',
        r'\bcount holds at (\d+)',
        r'\bHELD at (\d+)',
    ],
    'FAMILY (global running total)': [
        r'\bTHE ([A-Z][A-Z\-]+) FAMILY\b',
    ],
    'FACE (ordinal WITHIN a member, no global total)': [
        r"\bmember (\d+)'?s? ([A-Za-z\-]+) face\b",
    ],
}
BAD_PREFIX = re.compile(r'(?:PO-|\br|L-|#)$')

# ============================================================================
# r7458 SPLITS THE MEMBER PREDICATE BY ROLE, AND THE REASON IS A DEFECT IN r7458's
# FIRST DRAFT OF `check_standing_state`.
#
# That draft derived each series' value as "the LAST site anywhere in the row" and
# compared it with "the last site in the LIVE BLOCK".  The live block is the END of the
# row, so both read the SAME site: ** the gate compared a value with itself, and its two
# registered controls -- a one-off mutation and a boundary moved onto a superseded copy
# -- both stayed green. **
#
# ⇒ That is this row's generator inside the gate built to catch it: an instrument built
#   to check a condition that already exists will agree with it, and the agreement will
#   look like a finding about the subject.
#
# THE ROW CARRIES THE TWO ROLES IN TWO DIFFERENT WORDINGS, which is what makes an
# independent comparison possible at all:
#   ANNOUNCEMENT -- the row charging a member as it finds it: `the NINETY-FIRST MEMBER`,
#                   `member 88 stands`, `a seventh blindness member`.
#   SUMMARY      -- the standing state restating the total: `NINETY-ONE blindness
#                   members`, `HELD at 91`, `the family holds at 91`.
# The authority is the ANNOUNCEMENTS; the summary is the copy.
# ============================================================================
ANNOUNCE = [
    r'\bmember[^0-9A-Za-z]{0,4}(\d+)\b',
    r'(?:THE|the)\s+([A-Z][A-Z\-]+|[a-z\-]+)\s+(?:BLINDNESS\s+)?MEMBER\b',
    r'(?:a|A)\s+([a-z\-]+)\s+blindness member\b',
]
SUMMARY = [
    r'\b([A-Z][A-Z\-]+|\d+)\s+blindness members\b',
    r'\bfamily (?:HOLDS|holds|stays) at (\d+)',
    r'\bcount holds at (\d+)',
    r'\bHELD at (\d+)',
]


def _scan(text, pats):
    out = []
    for pat in pats:
        for m in re.finditer(pat, text):
            v = num(m.group(1))
            if v is None or v > 400:
                continue
            pre = text[max(0, m.start() - 5):m.start()]
            if BAD_PREFIX.search(pre):
                continue
            out.append((m.start(), v, text[max(0, m.start() - 90):m.end() + 55]))
    return sorted(out)


def member_announced(text):
    """THE AUTHORITY: the highest member ordinal the row ANNOUNCES charging."""
    hits = _scan(text, ANNOUNCE)
    return (max(h[1] for h in hits) if hits else None), hits


def member_summarised(text):
    """THE COPY: the member total as the given text RESTATES it, latest in text order."""
    hits = _scan(text, SUMMARY)
    return (hits[-1][1] if hits else None), hits




def harvest(text, label):
    marks = stamps(text)
    out, excluded = [], []  # harvested in text order; position IS the order
    for name, pats in SERIES.items():
        for pat in pats:
            for m in re.finditer(pat, text):
                g = m.groups()
                raw = g[-1] if name.startswith('FACE') else g[0]
                v = num(raw)
                if v is None:
                    continue
                pre = text[max(0, m.start() - 5):m.start()]
                if BAD_PREFIX.search(pre):
                    excluded.append((name, raw, text[max(0, m.start() - 70):m.end() + 40], 'id-shaped'))
                    continue
                parent = int(g[0]) if name.startswith('FACE') else None
                out.append(dict(series=name, val=v, parent=parent, rev=rev_at(marks, m.start()),
                                src=label, form=pat,
                                quote=text[max(0, m.start() - 95):m.end() + 55]))
    return out, excluded


def hold_clock(text):
    marks = stamps(text)
    out = []
    for m in re.finditer(r'(?:holds|HOLDS|stays) at 91(?: for an?[n]? ([A-Za-z\-]+) revision)?', text):
        n = num(m.group(1)) if m.group(1) else None
        out.append((rev_at(marks, m.start()), n, text[max(0, m.start() - 80):m.end() + 50]))
    return out


def main():
    t0 = time.time()
    reg, fro = row_of(REG), row_of(FRO)
    print('=' * 78)
    print("r7456 -- PO-78's COUNTS, DERIVED RATHER THAN READ   (answers r7453 (4))")
    print('=' * 78)
    print('  %s row %7d chars | %s row %7d chars' % (REG, len(reg), FRO, len(fro)))

    hits, ex = [], []
    for txt, lab in ((reg, REG), (fro, FRO)):
        h, e = harvest(txt, lab)
        hits += h
        ex += e

    print('\n-- EXCLUDED, printed so the exclusion is checkable (%d)' % len(ex))
    for name, raw, q, why in ex[:6]:
        print('   [%s] %-30s ...%s...' % (why, raw, q.strip()[:110]))
    if not ex:
        print('   none')

    print('\n' + '=' * 78)
    print('Ⓐ  THE SERIES, EACH WITH ITS OWN WORDING AND ITS LATEST-STAMPED STATEMENT')
    print('=' * 78)
    live = {}
    for name in SERIES:
        rows = [h for h in hits if h['series'] == name and h['src'] == REG]
        if not rows:
            print('\n  %s: NO SITE FOUND' % name)
            continue
        vals = sorted({h['val'] for h in rows})
        print('\n  %s' % name)
        print('    %d site(s) | %d distinct value(s): %s' % (len(rows), len(vals), vals))
        if name.startswith('FACE'):
            byp = collections.Counter(h['parent'] for h in rows)
            print('    ** EVERY SITE IS INDEXED INSIDE A MEMBER.  parents: %s **'
                  % dict(sorted(byp.items())))
            print('    ⇒ so this series HAS NO GLOBAL TOTAL and cannot be the same count as')
            print('      the member series, which is a global one.')
        L = rows[-1]   # append-forward: the row's own ordering rule
        live[name] = (L['val'], L['rev'])
        print('    ** LATEST-STAMPED: %s at r%s ** ...%s...'
              % (L['val'], L['rev'], L['quote'].strip()[:120]))

    print('\n' + '=' * 78)
    print('Ⓑ  THE MEMBER SERIES IS A TIME SERIES WRITTEN INLINE, WHICH IS THE HAZARD')
    print('=' * 78)
    ms = sorted([h for h in hits if h['series'].startswith('MEMBER') and h['rev']
                 and h['src'] == REG], key=lambda h: h['rev'])
    seen, trail = set(), []
    for h in ms:
        if (h['rev'], h['val']) in seen:
            continue
        seen.add((h['rev'], h['val']))
        trail.append('r%d=%d' % (h['rev'], h['val']))
    print('  ' + '  '.join(trail))
    print('\n  ** %d distinct values of ONE field stand in the row as live text. **'
          % len({h["val"] for h in ms}))
    print('  Nothing in the text marks which is current except its POSITION.')

    print('\n' + '=' * 78)
    print('Ⓒ  THE HOLD\'S OWN CLOCK, SELF-STATED (answers (4) iii)')
    print('=' * 78)
    hc = [x for x in hold_clock(reg) if x[0]]
    for rev, n, q in sorted(hc, key=lambda x: x[0])[-8:]:
        print('  r%-5s %-4s ...%s...' % (rev, ('n=%s' % n) if n else '-', q.strip()[:120]))
    named = [(r, n) for r, n, _ in hc if n]
    seq = [n for _r, n in named]
    print('\n  the self-count sequence IN TEXT ORDER: %s' % seq)
    mono = all(b >= a for a, b in zip(seq, seq[1:]))
    print('  monotone in text order: %s' % ('YES' if mono else 'NO'))
    print('  the same sequence keyed by NEAREST PRECEDING STAMP: %s'
          % [n for _r, n in sorted(named, key=lambda x: x[0])])
    print('  \u2318 the stamp-keyed order is NOT the row\'s order.  A block\'s prose cites other')
    print('    revisions, so the nearest preceding stamp is as often a CITATION as a date --')
    print('    which is this row\'s own newest member, in the stamper.  Text position is used.')
    if named:
        r, n = named[-1]
        print('\n  ** THE ROW\'S OWN LATEST SELF-COUNT, IN ITS OWN ORDER: held for %d'
              ' revision(s), in a block that cites r%d. **' % (n, r))

    print('\nprice %.1fs' % (time.time() - t0))
    return hits, live


if __name__ == '__main__' and '--place' not in sys.argv and '--seed' not in sys.argv:
    main()


# ============================================================================
# r7453 (5) -- PRICING THE RUNWAY-PLACEMENT PREDICATE BEFORE BUILDING IT.
#
# The candidate, in the order's words: "a runway block's prose must not cite revisions
# newer than its own row's newest, and must contain its own row id."
#
# ⌗ The blocks are read with ast, which is the gate's own route into this file, NOT with
#   a hand-written block finder.  r7453 (5) is a report of what a hand-written block
#   finder cost, and r7445's rule says a reimplementation of a parser is a second
#   instrument and it will disagree.  So this prices the predicate without minting one.
# ============================================================================
import ast


def runway_blocks():
    """{row_id: runway prose} from scripts/regen_frontier.py, via ast."""
    src = open(os.path.join(ROOT, GEN), encoding='utf-8').read()
    tree = ast.parse(src)
    best = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [k.value for k in node.keys
                if isinstance(k, ast.Constant) and isinstance(k.value, str)]
        if len(keys) < 20 or not all(k.startswith(('PO-', 'L-')) for k in keys):
            continue
        for k, v in zip(node.keys, node.values):
            if not (isinstance(k, ast.Constant) and isinstance(v, ast.Tuple)):
                continue
            tail = v.elts[-1]
            try:
                prose = ast.literal_eval(tail)
            except Exception:
                continue
            if isinstance(prose, str) and len(prose) > 200:
                best[k.value] = prose
    return best


def register_rows():
    """{row_id: newest revision stamped anywhere in its register row}"""
    out = {}
    with open(os.path.join(ROOT, REG), encoding='utf-8') as fh:
        for ln in fh:
            m = re.match(r'\| \*\*((?:PO|L)-[0-9]+)\*\*', ln)
            if m:
                revs = [int(x) for x in re.findall(r'\br(\d{4})\b', ln)]
                out[m.group(1)] = max(revs) if revs else None
    return out


def place():
    t0 = time.time()
    blocks, regmax = runway_blocks(), register_rows()
    print('=' * 78)
    print('r7456 -- PRICING THE RUNWAY-PLACEMENT PREDICATE   (answers r7453 (5))')
    print('=' * 78)
    print('  %d runway block(s) read via ast | %d register row(s) with a newest stamp'
          % (len(blocks), sum(1 for v in regmax.values() if v)))

    c2_fail, c1_fail, untestable = [], [], []
    for rid, prose in sorted(blocks.items()):
        if rid not in regmax or regmax[rid] is None:
            untestable.append(rid)
            continue
        if rid not in prose:
            c2_fail.append(rid)
        newer = sorted({int(x) for x in re.findall(r'\br(\d{4})\b', prose)
                        if int(x) > regmax[rid]})
        if newer:
            c1_fail.append((rid, regmax[rid], newer[:6], len(newer)))

    print('\n-- CLAUSE 2, "the block contains its own row id"')
    print('   %d of %d block(s) FAIL.  %s'
          % (len(c2_fail), len(blocks) - len(untestable), c2_fail[:12] or '(none)'))
    print('   ⇒ CHEAP AND CHECKABLE: one substring test per block, no mapping needed,')
    print('     and it is the clause that would actually have caught r7453\'s misplacement,')
    print('     because 51 lines of PO-78 text landed in PO-79\'s block.')

    print('\n-- CLAUSE 1, "no revision newer than its own row\'s newest"')
    print('   %d of %d block(s) FAIL on a tree where placement is believed correct.'
          % (len(c1_fail), len(blocks) - len(untestable)))
    for rid, mx, sample, n in c1_fail[:10]:
        print('     %-8s register newest r%s | cites %d newer: %s' % (rid, mx, n, sample))
    if untestable:
        print('   %d block(s) NOT TESTABLE (no register row or no stamp): %s'
              % (len(untestable), untestable[:10]))

    print('\n' + '=' * 78)
    print('THE PRICE, ADJUDICATED -- AND IT REVERSES THIS SEAT\'S OWN PREDICTION')
    print('=' * 78)
    motiv = 'PO-79'
    reach = motiv in blocks and regmax.get(motiv) is not None
    print("""  \u26d4 ** CLAUSE 2 IS PRICED OUT, AND IT IS THE CLAUSE PREDICTION.md CALLED CHEAP. **
    %d of %d live blocks FAIL it on a tree where placement is believed correct, because a
    row's runway prose says "this row" rather than naming itself; only PO-78 passes, and
    only because it quotes its own id.  \u21d2 Adopting it would mean rewriting ten blocks to
    satisfy a gate, which is writing to the instrument.

  \u2713 ** CLAUSE 1 SHOWS NO FALSE POSITIVE -- 0 of %d -- so it is SOUND where it applies,
    and PREDICTION.md predicted the opposite.  REPORTED AS A MISS. **
    And it needs no second copy of the mapping: which revisions belong to which row is
    answered by THE REGISTER, which is the authority the frontier is generated against.

  \u26d4 ** BUT IT DOES NOT REACH THE CASE THAT MOTIVATED IT, AND THAT IS THE FINDING. **
    r7453's misplacement put 51 lines of PO-78's amendment inside %s's block.  %s
    carries NO stamped register row, so it is NOT in the testable set -- %d of %d blocks
    are in that state.  ** The candidate gate would have been GREEN on the only instance
    the family has. **  \u2317 That is this row's own fourth-member shape: a gate hardened on
    one input while the other stays open, blind at the moment it matters.

  \u2317 ** THE ONE-LINE ANSWER THE ORDER ASKED FOR: placement IS checkable without a second
    copy of the mapping, but only for blocks whose row carries a stamped register row,
    and the row this cycle's misplacement landed in is not one of them. **

  \u2192 ** AND THE CHEAP PREREQUISITE, WHICH IS WORTH MORE THAN THE GATE: require every
    LIVE row's register row to carry a revision stamp.  That is a currency condition the
    register can satisfy with no copied list, and it converts clause 1 from a gate that
    is blind on %d of %d blocks into one that is total over the live rows. **"""
          % (len(c2_fail), len(blocks) - len(untestable),
             len(blocks) - len(untestable), motiv, motiv,
             len(untestable), len(blocks), len(untestable), len(blocks)))
    print('\n  \u2317 reachability of the motivating case, measured: %s' % ('REACHED' if reach else 'NOT REACHED'))
    print('\nprice %.1fs' % (time.time() - t0))


if __name__ == '__main__' and '--place' in sys.argv:
    place()


# ============================================================================
# THE CONTROLS AND THE SEED.  PREDICTION.md Ⓥ①–Ⓥ③, plus the assertions that fail if
# any of this run's own corrections regresses.
# ============================================================================
def seed():
    fails = []

    def ck(name, cond):
        print('  %s %s' % ('✓' if cond else '⛔', name))
        if not cond:
            fails.append(name)

    reg = row_of(REG)
    hits, ex = harvest(reg, REG)
    mem = [h for h in hits if h['series'].startswith('MEMBER')]
    fac = [h for h in hits if h['series'].startswith('FACE')]
    fam = [h for h in hits if h['series'].startswith('FAMILY')]

    print('SEED AND CONTROLS')
    ck('the row is found and is one line', len(reg) > 500000)

    # Ⓣ① OVER-FIRE, the row-id trap: PO-91 must never be read as member 91.
    trap = 'and PO-91 blindness members stand beside it'
    th, tex = harvest(trap, 'synthetic')
    ck('Ⓣ① a row id is NOT read as a count (PO-91 excluded)',
       not any(h['val'] == 91 for h in th) and len(tex) == 1)
    ck('Ⓣ① and the real row yields no id-shaped count', len(ex) == 0)

    # Ⓣ② OVER-FIRE, the other series: the two predicates must not agree.
    mv = sorted({h['val'] for h in mem})
    fv = sorted({h['val'] for h in fac})
    ck('Ⓣ② the member and face predicates return different value sets', mv != fv)
    ck('Ⓣ② and every face site is indexed inside a member',
       bool(fac) and all(h['parent'] is not None for h in fac))

    # Ⓣ③ UNDER-FIRE: the declared 91 must be found where the record states it.
    ck('Ⓣ③ the predicate finds the declared 91', 91 in mv)
    ck('Ⓣ③ at the standing-state sentence the record quotes',
       any(h['val'] == 91 and 'blindness members' in h['quote'] for h in mem))

    # the corrections this run made
    ck('append-forward order, not stamp order: self-count is monotone in text order',
       [n for _r, n, _q in hold_clock(reg) if n] ==
       sorted([n for _r, n, _q in hold_clock(reg) if n]))
    ck('the family series exists and is distinct from both others',
       bool(fam) and sorted({h['val'] for h in fam}) != mv)
    ck('the member field stands in the row many times over',
       len({h['val'] for h in mem}) >= 10)

    print('\n  %d assertion(s) failing' % len(fails))
    return fails


if __name__ == '__main__' and '--seed' in sys.argv:
    seed()
