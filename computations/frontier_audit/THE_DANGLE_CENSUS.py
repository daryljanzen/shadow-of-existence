#!/usr/bin/env python3
"""
THE DANGLE CENSUS — ** HOW MANY OWED STATEMENTS ARE STILL SITTING IN THE MAP, IN THE MAP'S OWN
SUB-LISTS, AND IN THE DOCUMENT SET AROUND IT.  A COUNT, NOT A NARRATIVE. **

Daryl's question, and it is the right one: *"what lists of lists are dangling."*  The register is
policed to two decimal places.  The MAP is a document with items, and the map also contains SIX
SUB-LISTS that sort those items (the reweight, the two axes, the readiness sort, the runway, three
dated retro-fits) -- and a sort is a list ABOUT a list, which goes stale on its own schedule.  And
around both sits a document set nothing measures at all.

  PART 1  ** THE MAP'S ITEMS: every one, classified by what the register says about it. **
  PART 2  ** THE MAP'S SUB-LISTS: do they name items the register has since struck? **
  PART 3  ** THE DOCUMENT SET: how many carry owed statements, and how many are policed. **
  PART 4  ** THE NUMBER. **

Run: python3 THE_DANGLE_CENSUS.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
MAP = open(os.path.join(ROOT, 'OPEN_PROBLEMS_MAP.md'), encoding='utf-8').read()
ARC = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8').read()

# --- the register, read once: lead id -> struck? -------------------------------------------
# ** the HOME column, not the body.  A row's body routinely NAMES another item's code (`J·3`'s
# body mentions `C·6`), and attributing by substring hands one item's status to another -- which
# is how a first pass here reported `C·6` open when the map records it computed. **
REG, HOME = {}, {}
for ln in ARC.split('\n'):
    if not re.match(r'^\|\s*(?:~~L-\d+~~|\*\*L-\d+\*\*)\s*\|', ln):
        continue
    cells = [c.strip() for c in re.split(r'(?<!\\)\|', ln)[1:-1]]
    lid = re.search(r'L-\d+', cells[0]).group(0)
    REG[lid] = cells[0].startswith('~~')
    HOME[lid] = cells[2] if len(cells) > 2 else ''
print(f"  register: {len(REG)} rows, {sum(REG.values())} struck, {len(REG)-sum(REG.values())} open")

# =====================================================================
print()
print("=" * 78)
print("PART 1 — THE MAP'S ITEMS")
print("=" * 78)
# An ITEM is a top-level bullet that declares a cluster-local code.  Everything else in the
# clusters is a strike banner attached to one (the map keeps banners as separate bullets).
# ** the map closes an item in FOUR shapes, all carrying the revision -- and the fourth is the one
# a first pass missed: `C·6` reads '✓ COMPUTED (r964): it does NOT cap', a NEGATIVE answer, which
# is a closure and not a status note. **
CLOSED_AT_MAP = re.compile(r'(\[r\d+\s*[—–-]\s*(?:RESOLVED|CLOSED|COMPUTED|COLLECTED)'
                           r'|(?:RESOLVED|CLOSED|DISCHARGED|COMPUTED|COLLECTED)\s*\(?r\d+)')
items = {}
for line in MAP.split('\n'):
    if not line.startswith('- **'):
        continue
    c = re.search(r'([A-J])·?(\d+)', line)
    if not c:
        continue
    items.setdefault(f"{c.group(1)}·{c.group(2)}", []).append(line)

buckets = {'STRUCK in the register': [], 'OPEN in the register': [],
           'closed at map level (pre-fold)': [], '⛔ UNTRACKED': []}
for code, lines in items.items():
    blob = ' '.join(lines)
    lids = set(re.findall(r'L-\d+', blob))
    # the register's own home column is authoritative for which rows own this code
    alts = (re.escape(code), re.escape(code.replace('·', '')))
    owners = {lid for lid in REG
              if re.search(r'\b(?:%s|%s)\b' % alts, HOME[lid])}
    owners |= {l for l in lids if l in REG}
    if not owners:
        buckets['closed at map level (pre-fold)' if CLOSED_AT_MAP.search(blob)
                else '⛔ UNTRACKED'].append(code)
    elif all(REG[l] for l in owners):
        buckets['STRUCK in the register'].append(code)
    else:
        buckets['OPEN in the register'].append(code)

print(f"  the map declares ** {len(items)} items **, and every one now resolves:")
for k in ['STRUCK in the register', 'closed at map level (pre-fold)',
          'OPEN in the register', '⛔ UNTRACKED']:
    v = sorted(buckets[k])
    print(f"    {len(v):>3}  {k}")
    if v:
        print(f"         {', '.join(v)}")
assert not buckets['⛔ UNTRACKED'], buckets['⛔ UNTRACKED']
# ** this assertion has fired twice and been RIGHT both times: `B·1`/`B·2`/`G·1` at c54.116
# and `J·1` at c54.117.  It stays. **

opens = sorted(buckets['OPEN in the register'])
germ = [c for c in opens if c.startswith('J')]
real = [c for c in opens if not c.startswith('J')]
print()
print(f"  ** of the {len(opens)} open, {len(germ)} are cluster-J germs and {len(real)} are owed work. **")
print(f"     cluster J (worked c54.114, verdicts recorded, held at germ weight): {', '.join(germ)}")
print(f"     ** OWED WORK: {', '.join(real)} **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE MAP'S SUB-LISTS")
print("=" * 78)
# ** A SORT IS A LIST ABOUT A LIST.  It names items by code, and it goes stale when the items
# move underneath it -- on its own schedule, invisible to a gate that only reads the items. **
SUBLISTS = [
    ('THE REWEIGHT (r608)',            r'## ═══ THE REWEIGHT'),
    ('the priority axis',              r'## The second axis'),
    ('the readiness / dependency sort', r'## The readiness'),
    ('the runway',                     r'## The runway'),
    ('discrete/continuous (c54.59)',   r'### ⌗⌗ THE DISCRETE/CONTINUOUS SPLIT AGAIN'),
    ('discrete/continuous (r2340)',    r'### ⌗ THE DISCRETE/CONTINUOUS SPLIT, RESTATED'),
    ('the T(k) residual (r2349)',      r'### ⌗ THE \$T\(k\)\$ RESIDUAL'),
]
bounds = []
for name, pat in SUBLISTS:
    m = re.search(pat, MAP)
    bounds.append((name, m.start() if m else None))
bounds = [(n, s) for n, s in bounds if s is not None]
bounds.sort(key=lambda x: x[1])
print(f"  {'sub-list':>34} {'codes named':>12} {'naming a STRUCK item':>21} {'stale?':>8}")
stale_lists = []
for i, (name, s) in enumerate(bounds):
    e = bounds[i + 1][1] if i + 1 < len(bounds) else len(MAP)
    seg = MAP[s:e]
    named = sorted({f"{a}·{b}" for a, b in re.findall(r'\b([A-J])·(\d+)', seg)})
    struckly = [c for c in named if c in buckets['STRUCK in the register']]
    # ** A SUB-LIST IS STALE IF IT RANKS STRUCK WORK AND NOTHING DECLARES IT HISTORY.  The
    # declaration need not live INSIDE the segment -- the r608 reweight declares the three sorts
    # below it prior sort, and a test that only read each segment reported those three current and
    # the superseded one stale, which is backwards. **  So: a segment is history if it says so, OR
    # if any earlier segment declares the sections below it superseded.
    says = bool(re.search(r'STRUCK|struck|RESOLVED|CLOSED|superseded|SUPERSEDED|prior sort'
                          r'|annotated history', seg))
    declared_history = bool(re.search(r'supersedes the priority / readiness / runway sections below',
                                      MAP[:s]))
    bad = bool(struckly) and not (says or declared_history)
    if bad:
        stale_lists.append((name, struckly))
    print(f"  {name:>34} {len(named):>12} {len(struckly):>21} {('⛔ YES' if bad else 'no'):>8}")
print()
if stale_lists:
    print("  ⛔ ** STALE SORTS — each ranks work the register has already struck: **")
    for n, c in stale_lists:
        print(f"     {n}: {', '.join(c)}")
else:
    print("  ** No sub-list ranks a struck item without saying so. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE DOCUMENT SET")
print("=" * 78)
OWED = re.compile(r'\b(still open|remains open|not yet|unbuilt|owed|TO DO|TODO|to be built|'
                  r'to be done|outstanding|unresolved|open question)\b', re.I)
DONE = re.compile(r'\b(STRUCK|RESOLVED|CLOSED|DISCHARGED|SUPERSEDED|WITHDRAWN|RETIRED)\b')
POLICED = {'THE_PLAN.md', 'THE_OPEN_PROBLEMS_LEDGER.md', 'OPEN_PROBLEMS_MAP.md', 'THE_WEAVE.md'}
QUEUED = {f for f in os.listdir(ROOT) if f.endswith('_LEDGER.md')}
# ** THE SPLIT THAT MAKES THIS NUMBER MEAN ANYTHING, and a first pass here did not make it: a
# revision-by-revision LOG says 'not yet' AT A REVISION -- a dated statement, not a standing debt.
# `CORPUS_MAP.md` alone carries 702 such lines and is a journal.  Counting those as owed work would
# manufacture a backlog out of a diary. **
LOGNAME = re.compile(r'transcript|gate_session|BUNDLE_|HISTORICAL_|CAPSTONE|CREDO|PUZZLE'
                     r'|DEMONSTRATING|RECALL_|SPINUP|KICKOFF|_HARVEST|_EXTRACTION|c22_keepers'
                     r'|WORK_ORDER|FORENSIC', re.I)
logs, standing = [], []
for f in sorted(os.listdir(ROOT)):
    if not f.endswith('.md'):
        continue
    t = open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read()
    n = sum(1 for ln in t.split('\n') if OWED.search(ln) and not DONE.search(ln))
    is_log = bool(LOGNAME.search(f)) or len(re.findall(r'^#+ .*Revision r\d+', t, re.M)) >= 3
    (logs if is_log else standing).append((n, f))
lo = sum(n for n, _ in logs)
so = sum(n for n, _ in standing)
sp = sum(n for n, f in standing if f in POLICED or f in QUEUED)
print(f"  {len(logs):>3} logs / transcripts / bundles  — {lo:>4} owed-flavoured lines, "
      f"** dated at their revision, NOT standing debt **")
print(f"  {len(standing):>3} standing documents           — {so:>4} owed-flavoured lines")
print(f"        of those, {sp} sit in a document a gate reads "
      f"({len(POLICED)} grains + {len(QUEUED)} field ledgers)")
print(f"        ** {so - sp} sit in standing documents NOTHING measures **")
print()
print("  the standing documents carrying the most, policed or not:")
print(f"  {'lines':>7}  {'document':<48} {'policed?':>9}")
for n, f in sorted(standing, reverse=True)[:12]:
    if not n:
        continue
    tag = 'grain' if f in POLICED else 'queue' if f in QUEUED else '— no'
    print(f"  {n:>7}  {f:<48} {tag:>9}")
print()
for x in [
 "⚠ ** THE LINE COUNT IS AN UPPER BOUND AND IS STATED AS ONE: it is a keyword sweep, and prose",
 "   uses 'not yet' descriptively. **  *What it measures honestly is STRUCTURAL, and the structure",
 "   does not depend on the count: **{S} standing documents, {P} of them read by any gate.***",
 "",
 "⌗ *The four grains are policed for STALENESS — how far behind the register they have fallen — and",
 "   the field ledgers for queue entries answered elsewhere.  **Nothing measures the rest at all**,",
 "   and the c54.115–117 findings all came out of documents in exactly that position.*",
]:
    print("  " + x.replace('{S}', str(len(standing))).replace('{P}', str(len(POLICED | QUEUED))))

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE NUMBER")
print("=" * 78)
print(f"  {'the map declares':>44} {len(items):>5} items")
print(f"  {'resolved (struck, or closed pre-fold)':>44} "
      f"{len(buckets['STRUCK in the register']) + len(buckets['closed at map level (pre-fold)']):>5}")
print(f"  {'cluster-J germs, worked and verdicts recorded':>44} {len(germ):>5}")
print(f"  {'** OWED WORK **':>44} {len(real):>5}   {', '.join(real)}")
print(f"  {'untracked by the register':>44} {len(buckets['⛔ UNTRACKED']):>5}")
print()
print(f"  {'the map sub-lists that rank a struck item':>44} {len(stale_lists):>5}")
print(f"  {'standing documents':>44} {len(standing):>5}")
print(f"  {'   read by a gate':>44} {len(POLICED | QUEUED):>5}")
print(f"  {'   ** read by nothing **':>44} {len(standing) - len(POLICED | QUEUED):>5}")
print(f"  {'owed-flavoured lines in standing documents':>44} {so:>5}   (upper bound: a keyword sweep)")
print(f"  {'   in a document a gate reads':>44} {sp:>5}")
print(f"  {'   ** in a document nothing reads **':>44} {so - sp:>5}")
