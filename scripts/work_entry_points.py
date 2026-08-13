#!/usr/bin/env python3
"""work_entry_points.py -- run the register's UNMARKED sites through the machinery.

** WHY THIS IS NOT THE PASS THE LIST STARTED AS (Daryl, r2399). **

The entry-point dig was worked by hand once, around five hundred revisions ago, and got about ten
sites in before the arc moved on -- and P14's whole 54-development eventually fell out of those ten.
Two things have changed since, and they point the same way:

  * ** The corpus has deepened where it matters to this list. **  Its closed-formness, its
    combinatorial strings, monodromies and representations have been tapped far harder since; the
    ontology is well past where it was.  So relatively there is LESS left to give per site, and a
    site that would have opened a front then may now be answered three papers over.
  * ** The machinery did not exist. **  The by-hand pass had no supersession scan, no struck-row
    register, no protected-item bar, no receipt corpus to score against.  ** The harness now
    automates, comprehensively, what was being done imperfectly by hand. **

So the 94 unmarked sites go through the machinery, not through ninety-four readings.

** WHAT THIS SCRIPT DOES AND DOES NOT DECIDE. **  It TRIAGES and it proposes; it never writes a
verdict into the register.  The register's own first lesson is the reason, and it is the whole
discipline of the instrument:

    ** "an advertised door is a CLAIM TO DIG, never a fact.  The first unrouted door found here was a
       phantom -- a debt one paper manufactured, deferred to a second paper that correctly never took
       it up, and which no paper anywhere asserts.  Routing it would have inscribed the false
       advertisement the arc exists to eradicate." **

A triage that wrote verdicts would inscribe them at machine speed.  ** Dig the corpus, not the
suspect claim. **  What the script buys is that each reading arrives with its evidence already
gathered, which is exactly the difference between the by-hand pass and this one.

THE FOUR TESTS, in the order a reader wants them:

  GONE       -- the sentence is no longer in its paper.  Already answered by audit_entry_points.
  ANSWERED?  -- IDF-weighted overlap against the 164 STRUCK register rows and the receipt index.
                A high score means ** go read this row against this site **, never that it is closed.
  ONE ROOM?  -- overlap against the other unmarked sites: sites that collapse together are one door
                wearing several advertisements, which is the `⊕ ONE ROOM` marker's whole purpose.
  PROTECTED? -- names an object a PROTECTED_OPEN item covers, in which case it routes rather than
                opens, and a node may not close it.

    python3 scripts/work_entry_points.py            # triage report
    python3 scripts/work_entry_points.py --top 25   # the strongest candidates only

Written r2399.  Stated for reversal.
"""
import os, re, sys, math, glob
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'ENTRY_POINT_REGISTER.md')
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')
PO = os.path.join(ROOT, 'PROTECTED_OPEN.md')
RIDX = os.path.join(ROOT, 'receipts', 'INDEX.md')

STOP = set("""the a an and or of to in on at is are was were be been being it its this that these those
for with as by from into over under about which whether what where when how not no nor but if then than
one two three first second we our us their there here also only just more most much many such same other
another any all each both either neither some none paper papers section sections corpus construction
open closed question questions problem problems work works read reads reading left stays stay remains
remain built build unbuilt derived settled claim claims scope present yet still does do did done
emph cite ref label textbf rcpt r2376 c54""".split())


def words(s):
    s = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    return [w for w in re.findall(r'[a-z][a-z\-]{2,}', s.lower()) if w not in STOP]


def read(p):
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def unmarked_sites():
    """Rows in the register with no verdict marker -- the register's own definition of unworked."""
    t = read(REG)
    out, paper = [], None
    # ** r2399: THE MARKER SET WAS TOO NARROW ON THE FIRST RUN. **  The register's stated markers are
    # ✔ LIVE / ✗ NOT A DOOR / ⊕ ONE ROOM, but rows in the wild also carry ✗ KILLED, ✔ WORKED, TURNED
    # AROUND and CURRENT TEXT verdicts.  Eight of the first run's top eight were rows that ALREADY
    # carried a verdict -- ** a triage that re-triages worked rows spends its whole budget on the
    # part of the list that is done. **
    MARK = ('✔ LIVE', '✗ NOT A DOOR', '⊕ ONE ROOM', '✗ KILLED', '✔ WORKED', '✔ ', '✗ ',
            'TURNED AROUND', 'CURRENT TEXT', 'RETRACTED')
    for ln in t.split('\n'):
        m = re.match(r'^### (\S+) — `([^`]+)`', ln)
        if m:
            paper = m.group(1)
            continue
        if paper and ln.startswith('|') and ln.count('|') >= 4:
            cells = [c.strip() for c in ln.split('|')[1:-1]]
            if len(cells) < 3 or not (cells[1].startswith('*') and cells[1].endswith('*')):
                continue
            if any(k in ln for k in MARK):
                continue
            # ** r2400 (band 1, B4): A SECTION HEADING IS NOT A SITE. **  Three "sites" scoring as one
            # room turned out to be the section TITLES -- \section{Scope and open problems},
            # \section{Scope and what remains open}, \section{What stays open}.  ** A heading is where
            # gaps are DECLARED, never itself a gap **, and it scores as one room with its siblings
            # because every paper names that section the same way.
            # ** A dig that indexes the door's sign as a door will find one in every paper. **
            if re.match(r'^\\\\?section\{[^}]*\}(\\\\?label\{[^}]*\})?…?$', cells[2].strip()):
                continue
            out.append((paper, cells[0], cells[1].strip('*'), cells[2]))
    # ** AND ONE SITE INDEXED UNDER SEVERAL KEYWORDS IS ONE SITE. **  The register lists a sentence
    # once per keyword it matched, so the same quoted words appear two to six times.  Scored raw,
    # every such row's nearest neighbour is ITSELF under another keyword -- which is how the first
    # run produced "ONE ROOM? 18.7" between a row and its own twin.  ** A duplicate is not a
    # coincidence to report; it is an artefact of the index. **  Collapse by quoted text, keep the
    # keyword multiplicity, and score once.
    seen, uniq = {}, []
    for paper, sec, kw, txt in out:
        key = re.sub(r'\s+', ' ', txt)[:90]
        if key in seen:
            seen[key][2].append(kw)
            continue
        entry = [paper, sec, [kw], txt]
        seen[key] = entry
        uniq.append(entry)
    return [(p_, s_, '/'.join(k_), t_) for p_, s_, k_, t_ in uniq]


def struck_rows():
    t = read(ARC)
    out = []
    for ln in t.split('\n'):
        m = re.match(r'^\|\s*~~(L-\d+)~~\s*\|(.*)$', ln)
        if m:
            out.append((m.group(1), m.group(2)[:2500]))
    return out


def receipts():
    out = []
    for ln in read(RIDX).split('\n'):
        # ** r2555: case-sensitive on the paper column, and p0 is lowercase -- the same
        # silent-discard shape fixed in run_all_receipts and check_receipts. **
        if ln[:3].upper().startswith('| P') and ln.count('|') >= 3:
            cells = [c.strip() for c in ln.split('|')[1:-1]]
            out.append((cells[0][:60], ' '.join(cells[1:3])))
    return out


def protected():
    t = read(PO)
    out = []
    for m in re.finditer(r'\|\s*(?:~~)?\*\*(PO-\d+[a-z]?)\*\*(?:~~)?\s*\|([^|]{0,300})', t):
        out.append((m.group(1), m.group(2)))
    return out


def scorer(docs):
    df = Counter()
    for _, txt in docs:
        df.update(set(words(txt)))
    n = max(1, len(docs))

    def idf(w):
        return math.log((n + 1) / (1 + df.get(w, 0)))
    return idf


def main():
    sites = unmarked_sites()
    if not sites:
        # ** r2402: AN EMPTY LIST MEANS DONE, NOT BROKEN. **  The first pass finished and this gate
        # answered "[FAIL] no unmarked sites parsed out of the register" -- ** a triage that cannot
        # express its own success trains its caller to read completion as breakage **, which is the
        # cry-wolf class one last time and in the friendliest possible place.
        print('  ✔ NO UNMARKED SITES REMAIN -- the first pass over the entry-point register is')
        print('    COMPLETE.  Every site carries a verdict marker.')
        print()
        print('    ** This is not the front closing. **  `L-210` is the register worked once through;')
        print('    what stays live is `L-211` -- the closure-adjacency debt, which is TRIGGERED')
        print('    rather than enumerated, and fires again on every closure the corpus makes.')
        print()
        return 0
    sr, rc, po = struck_rows(), receipts(), protected()
    pool = sr + rc
    idf = scorer(pool)
    top = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 0

    print()
    print(f'  ENTRY-POINT TRIAGE -- {len(sites)} unmarked site(s) against '
          f'{len(sr)} struck row(s), {len(rc)} receipt(s), {len(po)} protected item(s)')
    print()
    print('  ** Every score below is a POINTER TO A READING, never a verdict. **  A high ANSWERED?')
    print('     score means go read that row against this site.  The register\'s own first lesson is')
    print('     that an advertised door is a claim to dig, never a fact -- and a triage that wrote')
    print('     verdicts would inscribe the false ones at machine speed.')
    print()

    rows = []
    for paper, sec, kw, txt in sites:
        w = set(words(txt))
        if not w:
            continue
        best, bl = 0.0, ''
        for lid, body in pool:
            shared = w & set(words(body))
            if not shared:
                continue
            s = sum(idf(x) for x in shared) / math.sqrt(len(w))
            if s > best:
                best, bl = s, lid
        # one-room: overlap with other unmarked sites
        room, rn = 0.0, ''
        for p2, s2, k2, t2 in sites:
            if (p2, s2, k2) == (paper, sec, kw):
                continue
            sh = w & set(words(t2))
            if not sh:
                continue
            s = sum(idf(x) for x in sh) / math.sqrt(len(w))
            if s > room:
                room, rn = s, f'{p2} §{s2[:18]}'
        pro = [c for c, d in po if len(set(words(d)) & w) >= 3]
        rows.append((best, bl, room, rn, pro, paper, sec, kw, txt))

    rows.sort(key=lambda r: -max(r[0], r[2]))
    shown = rows[:top] if top else rows
    for best, bl, room, rn, pro, paper, sec, kw, txt in shown:
        flag = '★' if (best >= 3.0 or room >= 3.0 or pro) else ' '
        print(f'  {flag} {paper:<6} §{sec[:22]:<22} *{kw}*')
        print(f'      "{re.sub(chr(92)+"s+", " ", txt)[:110]}…"')
        bits = []
        if best >= 1.0:
            bits.append(f'ANSWERED? {best:.1f} → {bl}')
        if room >= 1.0:
            bits.append(f'ONE ROOM? {room:.1f} → {rn}')
        if pro:
            bits.append(f'PROTECTED → {", ".join(pro)}')
        print('      ' + ('  ·  '.join(bits) if bits else 'no pointer — read cold'))
        print()

    starred = sum(1 for r in rows if r[0] >= 3.0 or r[2] >= 3.0 or r[4])
    print(f'  {starred} of {len(rows)} carry a pointer worth reading first; the rest read cold.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
