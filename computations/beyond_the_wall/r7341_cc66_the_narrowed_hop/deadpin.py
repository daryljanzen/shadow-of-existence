#!/usr/bin/env python3
"""deadpin.py -- a live quote-pin key whose literal occurs ZERO times in the container it is checked against.

** WHY IT IS A CLASS AND NOT A CURIOSITY (r7337+cc66.3, ratified r7341 ⑧). **  `P15_the_history...` asserted
EITHER `permits the chirality-asymmetric action and does n` OR a bare `does not \\emph{select} it`.  The first
matched ZERO times -- the paper says `permits ... BUT does not select it` -- and it carried a ledger row with
verdict `EXTENDED`, adjudicated as a widening.
  ⇒ *** A dead pin sits green and adjudicated for as long as the disjunction around it carries the check, and
  NO COUNT OF OWED ROWS CAN SEE IT. ***  That is what makes it bear on the quantity this phase is scored on.

⛔ STATED LIMITS, before the number (registered at `950e7418b`):
  * `SOURCE`-filed keys are NOT covered -- their containers are registers, ledgers, receipt sources and data
    files, which this pass does not load.  `82` of `r7341`'s `117` new keys were `SOURCE`, so the uncovered
    share is large and the `PAPER` number does not stand for the ledger.
  * a row flagged `PINNED` is EXCLUDED: its container is a read at a fixed commit, so absence from the LIVE
    paper is the point of it rather than a defect (`C28`'s `9.4`, read at `_BEFORE_R2755`).
  * generated `appendix_receipts_*.tex` are NOT loaded, because they are built FROM the receipts and would
    hide a dead pin by re-containing its literal.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys
import importlib.util

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
_spec = importlib.util.spec_from_file_location('cqp', os.path.join(R, 'corpus', 'check_quote_pins.py'))
_m = importlib.util.module_from_spec(_spec)
sys.modules['cqp'] = _m
try:
    _spec.loader.exec_module(_m)
except SystemExit:
    pass
_unmark = _m._unmark

_RE_META = re.compile(r'\\[dswbWSDB]|\(\?|\[\^|\.\{|\.\*|\.\+|\\\$|\|')

LINE = re.compile(r'\s*\[QUOTE-PIN\]\[(PAPER|SOURCE|UNDECIDED)\]\[(SENTENCE|TOKEN)\]\[([A-Z,]*)\]\s+'
                  r'(\S+?):(\d+):(\d+)\s+(".*")$')


def _occurrences(src, lit):
    """every index at which `lit` appears in the receipt's source."""
    i = src.find(lit)
    while i >= 0:
        yield i
        i = src.find(lit, i + 1)


def _negated_key(src, lit):
    """does this receipt assert the literal is ABSENT rather than present?

    ⛔ r7341+cc66, FOURTH form of this test, and the three before it were each wrong in a way the next
    occurrence exposed.  `all(occurrence is negated)` is too strict: a receipt may MENTION the literal in
    a comment (`"… -- ** was correct when written"`) beside the two places it tests `not in`, and a prose
    mention is not an assertion.  So the rule is over the ASSERTING occurrences only: negated if at least
    one reads `not in` and NONE reads a positive `in`.
    """
    neg = pos = 0
    i = src.find(lit)
    while i >= 0:
        w = src[i + len(lit):i + len(lit) + 26]
        if ' not in ' in w:
            neg += 1
        elif ' in ' in w:
            pos += 1
        i = src.find(lit, i + 1)
    return neg > 0 and pos == 0


def body(f):
    b = '\n'.join(l for l in io.open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    papers = {os.path.basename(f): re.sub(r'\s+', ' ', body(f))
              for f in glob.glob(os.path.join(R, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts_')}
    un = {k: _unmark(v) for k, v in papers.items()}
    pinned = set()
    for ln in io.open(os.path.join(R, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if len(p) >= 6 and 'PINNED' in p[4]:
            pinned.add((p[0], json.loads(p[1])))
    r = subprocess.run([sys.executable, 'scripts/mutate_assertions.py', '--quote'],
                       cwd=R, capture_output=True, text=True, env=dict(os.environ, NODE='ci'))
    live = []
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m and m.group(1) == 'PAPER':
            live.append((m.group(4), json.loads(m.group(7)), m.group(2), m.group(3)))
    # ⛔ r7341+cc66, CORRECTED BEFORE THE NUMBER WAS REPORTED.  The first form asked only
    #   `_unmark(lit) not in _unmark(text)`, and that conflates THREE classes:
    #     * a REGEX PATTERN never occurs literally -- it MATCHES -- so `_quote_site`'s `_re` route
    #       (`re.search(PATTERN, body)`) looks dead by construction and is not;
    #     * a VANISHING span is present RAW and destroyed by the normaliser, which is the class this
    #       revision's registration explicitly DEFERRED;
    #     * a DEAD pin is absent BOTH ways, which is the one registered here.
    #   Separating them is the whole correction, and the first run's D of 130 was all three together.
    dead, vanishing, pattern, negated, skipped = [], [], [], [], 0
    for rc, lit, tier, flags in live:
        if (rc, lit) in pinned or 'PINNED' in flags:
            skipped += 1
            continue
        if _RE_META.search(lit):
            pattern.append((rc, lit, tier, flags))
            continue
        raw_hit = any(lit in t for t in papers.values())
        norm_hit = any(_unmark(lit) in t for t in un.values())
        if not raw_hit and not norm_hit:
            # ⛔ r7341+cc66, THIRD CORRECTION, from spot-checking 3 of the first 63: a receipt may
            #   assert a literal is ABSENT -- `'...' not in P16`, the replaced-sentence form -- and then
            #   absence is the POINT and not a defect.  One of the three I read was this.  So every
            #   occurrence of the literal in the receipt's own source is examined, and the key is a dead
            #   pin only if NONE of them sits in a `not in` context.
            src = io.open(os.path.join(R, rc), encoding='utf-8', errors='replace').read()
            if _negated_key(src, lit):
                negated.append((rc, lit, tier, flags))
            else:
                dead.append((rc, lit, tier, flags))
        elif raw_hit and not norm_hit:
            vanishing.append((rc, lit, tier, flags))
    print(f'\n  deadpin -- live PAPER keys {len(live)};  PINNED excluded {skipped};  '
          f'papers loaded {len(papers)}\n')
    for rc, lit, tier, flags in sorted(dead):
        print(f'    DEAD  {tier:8s} {flags:18s} {rc.split("/")[-1][:44]:46s} {lit[:58]!r}')
    print(f'\n  D = {len(dead)} DEAD (absent raw AND normalised) of {len(live) - skipped} checked')
    print(f'      {len(vanishing)} VANISHING (present raw, destroyed by the normaliser) '
          f'-- the class this revision DEFERRED, counted here because the same pass yields it')
    print(f'      {len(negated)} NEGATED excluded: the receipt asserts the literal is ABSENT, so'
          f' absence is the point -- found by spot-reading 3 of the first 63, one of which was this')
    print(f'      {len(pattern)} REGEX PATTERNS excluded: a pattern MATCHES and never occurs, so the'
          f' first form of this measurement called them dead by construction')
    print('  ⛔ A dead pin asserts the presence of text that is not there, and passes for as long as')
    print('     something else in its condition carries the check.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
