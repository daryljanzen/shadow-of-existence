"""P1 -- THE TRAPPED-SURFACE THEOREM IS CITED AS A THEOREM, AND NEVER AS AN OPEN TEST, AT EVERY SITE AN ANCHOR CAN FIND.

** WHAT IS PINNED. **  `P1` proves, as a theorem of standard general relativity, that no closed trapped surface is
realised and no gravitational collapse completes at finite EXTERIOR time.  Until `r7168` ten sites in four other
papers carried that result as one of two OPEN TESTS the programme poses to the world (66, `PO-85`).  `r7168` restated
them.  This receipt holds the repair: wherever another paper states the claim AND cites `P1` in one sentence, that
sentence must not grade it as an open test.

** HOW, AND WHY THIS SHAPE (`r7170+70.1`, `PO-85` struck on it). **  A corpus-wide grade comparison is not possible
from source: 17 of 1,469 cross-paper citing sites say WHICH result they import, so the owner's end of the comparison
cannot be found for the rest.  For ONE claim it can, by anchoring on the claim's own phrases together with the
owner's citation key.  Measured there: the anchor LOCATES the claim's sites (9 of `r7168`'s 10 at the pre-repair
tree), but reading the grade is a reader's job, because the grade often sits a sentence away.  ⇒ So this pin is
SENTENCE-SCOPED and is never widened: a +-1 sentence window found one more OPEN before the repair and INVENTED one
after it, in `canonical_time`, which by then states the theorem.  ** A window wide enough to hold the grade is wide
enough to misattribute it. **

** THE THREE HALVES. **
  ⓵ ABSENCE  -- no anchored sentence carries the OPEN grade (test(s) / open / held to / discriminate ...
     observationally).
  ⓶ PRESENCE -- the anchor still FINDS its sites, at least as many as at `r7171`, and in each paper `r7168` repaired
     that the anchor reaches, so ⓵ cannot pass by the anchor going stale.  `B25` read zero for three and a half
     thousand revisions for want of this half.
  ⓷ THE STATED LIMIT -- `P17`'s `r7168` site carries the claim and the citation in different sentences, so no
     sentence-scoped anchor reaches it.  That is a real class and a window is not the answer to it.  The limit is
     asserted, so that if the citation moves into the claim's sentence this receipt says the limit has lifted instead
     of passing silently.

** NOT CLAIMED. **  That every site grading this result is found: only the anchored ones are.  That the other papers
grade every OTHER imported result correctly: `PO-85`'s negative says no instrument can check that from source.

Written r7171 by node 70.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CORPUS = os.path.join(ROOT, 'corpus')
OWNER = 'BH_causality_v2.tex'
KEY = 'JanzenBHcausality'

#: the claim's own phrases (r7170+70.1's anchor, unchanged)
ANCHOR = re.compile(r'trapped surface|collapse (?:does not|never|must not)?\s*complete|(?:event )?horizon completes|'
                    r'complet\w* at finite (?:exterior|cosmic) time|finite (?:exterior|cosmic) time', re.I)
#: the wrong grade
OPEN = re.compile(r'\btests?\b|\bopen\b|\bheld to\b|discriminat\w*[^.]{0,60}observational', re.I)
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z\\$(])')
#: the r7171 floor, and the papers r7168 repaired that a sentence-scoped anchor reaches
FLOOR = 10
REPAIRED_REACHED = ('CR_framework.tex', 'janzen_circle_v3.tex', 'canonical_time.tex')
LIMIT_PAPER = 'geometric_core_paper.tex'

FAILED = []


def check(label, ok, got=None):
    print(f"  {'OK  ' if ok else 'FAIL'} {label}" + (f"   ({got})" if got is not None else ''))
    if not ok:
        FAILED.append(label)


def strip(t):
    """drop LaTeX comments (an unescaped % to end of line)"""
    return re.sub(r'(?<!\\)%[^\n]*', '', t)


def anchored(text):
    """[(sentence, is_open)] for every sentence citing the owner and carrying the claim's phrase"""
    out = []
    for s in SENT.split(strip(text)):
        f = ' '.join(s.split())
        if KEY in f and ANCHOR.search(f):
            out.append((f, bool(OPEN.search(f))))
    return out


print(__doc__.split('\n\n')[0])
print()

# the self-test, independent of the corpus: the detector flags the wrong grade and passes the right one
_bad = 'The programme holds one open test: that closed trapped surfaces do not form~\\cite{JanzenBHcausality}.'
_good = 'It is a theorem of standard general relativity that closed trapped surfaces do not form~\\cite{JanzenBHcausality}.'
check('self-test: a synthetic anchored sentence grading the claim an open test is flagged, the same as a theorem is not',
      anchored(_bad) == [(_bad, True)] and anchored(_good) == [(_good, False)])

sites = {}
for p in sorted(glob.glob(os.path.join(CORPUS, '*.tex'))):
    b = os.path.basename(p)
    if b == OWNER or b.startswith('appendix_receipts'):    # the generated appendices carry INDEX text
        continue
    found = anchored(open(p, encoding='utf-8', errors='replace').read())
    if found:
        sites[b] = found
n = sum(len(v) for v in sites.values())
opened = [(b, s) for b, v in sites.items() for s, o in v if o]
print(f'    anchored sites: {n} in {len(sites)} paper(s): ' + ', '.join(f'{b} {len(v)}' for b, v in sites.items()))

# ⓵ the absence
check(f'⓵ no anchored sentence grades P1\'s theorem as an open test ({n} sentences read)', not opened,
      '; '.join(f'{b}: ...{s[:140]}...' for b, s in opened) or None)

# ⓶ the presence
check(f'⓶ the anchor still finds its sites: {n} >= {FLOOR}, the count at r7171', n >= FLOOR, n)
check(f'⓶ and reaches each paper r7168 repaired that a sentence-scoped anchor can: {", ".join(REPAIRED_REACHED)}',
      all(b in sites for b in REPAIRED_REACHED), sorted(set(REPAIRED_REACHED) - set(sites)) or None)

# ⓷ the stated limit, asserted so that its lifting is reported
check(f'⓷ STATED LIMIT still holds: {LIMIT_PAPER}\'s r7168 site carries the claim and the citation in different '
      f'sentences, so no anchored site is found there (if this fails, the limit has LIFTED: raise REPAIRED_REACHED)',
      LIMIT_PAPER not in sites, len(sites.get(LIMIT_PAPER, [])))

print()
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED')
    sys.exit(1)
print('  every anchored site cites P1\'s theorem without grading it an open test, and the anchor still finds them.')
