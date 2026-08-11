#!/usr/bin/env python3
"""audit_entry_points.py -- re-run the entry-point dig and diff it against the recorded register.

** THE JOB A 132-REVISION LAG DIRECTLY DEFEATS. **  `ENTRY_POINT_REGISTER` is grain 0: every gap the
corpus advertises IN ITS OWN WORDS, per site, 124 of them across sixteen papers.  Its stated job is
"read BEFORE BELIEVING A GAP", and its whole value is that a node can find a gap it did not already
know about.  So a gap advertised in a paper and SINCE CLOSED still reads here as open -- which is the
one failure that makes the instrument worse than nothing, because it is consulted precisely when
somebody is deciding what to work.

** SO THE RE-READ IS MECHANICAL, AND THAT IS THE POINT. **  Reading 124 sites by hand once produces a
register that is stale the next revision.  This script re-runs the dig at the current front and
reports three things:

    GONE   -- a site the register records whose advertised sentence is no longer in the paper.
              ** This is the finding. **  Either the gap closed and the paper says so, or the
              sentence was rewritten.  Each is READ; the script never strikes a row.
    NEW    -- an advertised gap in the papers that the register does not carry.
    MOVED  -- present under a different section heading than recorded.

The keyword set is the register's own, recovered from its tables rather than invented, so a
regeneration is comparable to the original dig instead of a different dig wearing its name.

** WHAT IT DELIBERATELY DOES NOT DO. **  It does not rewrite the register.  The register's rows carry
the paper's own words and a human verdict, and its first lesson (r1120) is the reason to keep both:
    ** "an advertised door is a CLAIM TO DIG, never a fact.  The first unrouted door found here was a
       phantom -- a debt one paper manufactured, deferred to a second paper that correctly never took
       it up, and which no paper anywhere asserts.  Routing it would have inscribed the false
       advertisement the arc exists to eradicate." **
A script that struck rows on a text match would do exactly that, one automation layer up.
** Dig the corpus, not the suspect claim. **

    python3 scripts/audit_entry_points.py           # report
    python3 scripts/audit_entry_points.py --check    # exit 1 if any GONE site is unannotated

Written r2397.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'ENTRY_POINT_REGISTER.md')

# the register's own keyword set, recovered from its tables
# ** r2397: A SECOND SET, because the first has a BLIND CLASS. **  Working L-211 from the c54.163
# closures found P16 saying "the same erasure raises a question this paper answers IN EFFECT BUT DOES
# NOT STATE: why eta survives a passage the composition does not" -- and answering it.  ** That
# sentence contains none of the sixteen keywords **, so the register's dig could never see it, and it
# is exactly the kind of site the register exists for: a place the corpus itself marks as unstated.
# Swept: seven sites, none using any of the sixteen.  Two sub-kinds, and they are different things:
#   * an ANSWER the paper gives without stating it is a question  (P16's eta)
#   * a BOUNDARY the paper draws by saying what it does NOT assert (P13 x3, p0)
# ** The first is a gap already closed that nobody can find; the second is the do-not-assert
# discipline, which is where PO-3-class questions live. **
UNSTATED = ['answers in effect but does not state', 'does not state', 'never stated',
            'is not stated', 'raises a question', 'nowhere asserted', 'asserted nowhere',
            'we do not decide', 'is not asked', 'unasked', 'has never been asked']

KEYWORDS = ['awaits', 'beyond the present scope', 'do not claim', 'do-not-assert', 'genuinely open',
            'left open', 'left to the', 'not built here', 'not derived', 'not settled',
            'not yet attempted', 'open problem', 'remains open', 'stay open', 'stays open',
            'unbuilt']


def norm(s):
    s = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', s)
    s = re.sub(r'[^a-z0-9 ]', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


def recorded():
    """[(paper, keyword, quoted words)] as the register carries them."""
    t = open(REG, encoding='utf-8', errors='replace').read()
    out, paper = [], None
    for ln in t.split('\n'):
        m = re.match(r'^### (\S+) — `([^`]+)`', ln)
        if m:
            paper = m.group(2)
            continue
        if paper and ln.startswith('|') and ln.count('|') >= 4:
            cells = [c.strip() for c in ln.split('|')[1:-1]]
            if len(cells) >= 3 and cells[1].startswith('*') and cells[1].endswith('*'):
                out.append((paper, cells[1].strip('*'), cells[2]))
    return out


def papers():
    return {os.path.basename(p): open(p, encoding='utf-8', errors='replace').read()
            for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
            if not os.path.basename(p).startswith('appendix')}


def main():
    reg = recorded()
    if not reg:
        print('  [FAIL] no site rows parsed out of ENTRY_POINT_REGISTER')
        return 1
    pap = papers()
    print()
    print(f'  ENTRY-POINT DIG, RE-RUN -- {len(reg)} recorded site(s) across {len(pap)} paper(s)')
    print()

    # ** r2397: THE FIRST RUN OVER-REPORTED, and the reason is the register working rather than
    # failing. **  Many rows have ALREADY been annotated by hand -- "✗ KILLED r1280 — QUOTE REPLACED
    # r1498", "**CURRENT TEXT (r1491):** ..." -- so the cell opens with a verdict and the paper's
    # words sit inside it.  A naive probe reads the verdict, finds no match, and calls the site GONE.
    # ** A row that already carries its verdict is the instrument doing its job, not a finding **, and
    # counting it as one would bury the real ones under thirty-odd false alarms.
    ANNOTATED = ('**', '✗', '✓', '⌗', '⟐', '⚠')

    def paper_words(cell):
        """The paper's own words inside a cell that may open with an annotation."""
        m = re.search(r'CURRENT TEXT[^:]*:\s*["“]([^"”]{20,})', cell)
        if m:
            return m.group(1)
        m = re.search(r'["“]([^"”]{40,})', cell)
        if m:
            return m.group(1)
        return None

    gone, ok, annotated, missing_file = [], 0, [], []
    for paperfile, kw, words in reg:
        src = pap.get(paperfile)
        if src is None:
            missing_file.append(paperfile)
            continue
        cell = words.strip()
        if cell.startswith(ANNOTATED):
            inner = paper_words(cell)
            if inner is None:
                annotated.append((paperfile, kw))
                continue
            cell = inner
        probe = norm(cell)[:70]
        if probe and probe in norm(src):
            ok += 1
        else:
            gone.append((paperfile, kw, cell[:90]))

    print(f'  {ok} site(s) still present verbatim.')
    if annotated:
        print(f'  {len(annotated)} row(s) ALREADY CARRY A HAND VERDICT -- excluded, because a row that')
        print('     already says what the dig found is the instrument working, not a finding.')
    if missing_file:
        print(f'  {len(set(missing_file))} recorded paper file(s) not found: '
              f'{", ".join(sorted(set(missing_file)))}')
    print()
    if gone:
        print(f'  ⌗ {len(gone)} SITE(S) GONE -- the advertised sentence is no longer in the paper:')
        for f, kw, w in gone[:40]:
            print(f'    {f:<26} *{kw}*  "{w}…"')
        print()
        print('  ** Each is a READ, never a strike. **  A gap that closed and a sentence that was')
        print('     rewritten look identical to a text match, and the register\'s own first lesson is')
        print('     that an advertised door is a CLAIM TO DIG, never a fact.  Annotate the row with')
        print('     what the dig found; do not delete it.')
    else:
        print('  No recorded site has left its paper.')
    print()
    # the blind class, re-found on every run rather than depending on one reading
    blind = []
    for name, src in pap.items():
        for pat in UNSTATED:
            for m in re.finditer(re.escape(pat), src, re.I):
                seg = src[max(0, m.start() - 300):m.start() + 320]
                if not any(k in seg.lower() for k in KEYWORDS):
                    blind.append((name, pat, re.sub(r'\s+', ' ', seg)[180:400]))
    seen, uniq = set(), []
    for n_, p_, s_ in blind:
        if s_[:60] in seen:
            continue
        seen.add(s_[:60]); uniq.append((n_, p_, s_))
    if uniq:
        print(f'  ⛭ {len(uniq)} UNSTATED-CLASS site(s) -- content the corpus marks as unstated, using')
        print('     NONE of the register\'s sixteen keywords, so the dig above cannot see them:')
        for n_, p_, s_ in uniq:
            print(f'    {n_:<26} [{p_}]')
        print('     ** An answer the paper gives without stating it is a question is a gap already')
        print('        closed that nobody can find; a boundary drawn by saying what is NOT asserted')
        print('        is the do-not-assert discipline, and both belong in this register. **')
        print()
    if '--check' in sys.argv and gone:
        t = open(REG, encoding='utf-8', errors='replace').read()
        if 'DIG RE-RUN' not in t:
            print('  [FAIL] sites have gone and the register carries no re-run annotation.')
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
