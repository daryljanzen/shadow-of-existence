"""anchored.py -- r7170+70.1 (70) PO-85 M6: the ANCHORED, one-claim-at-a-time grade check (66's smaller reading).

One claim: P1's theorem that no closed trapped surface is realised and no collapse completes at finite exterior time.
A site states it when a sentence cites JanzenBHcausality AND carries one of the claim's own anchor phrases.  Its
asserted grade is OPEN (test / open / held to / discriminate observationally) or THEOREM (theorem / proven / proved /
general relativity alone); the owner, P1, grades it THEOREM.  Run at the tree before r7168's repair and after.

  python3 anchored.py
"""
import re, subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7043_70_citation_sweep'))
import trace_citations as T  # noqa: E402
from measure import OWN, SENT  # noqa: E402

ANCHOR = re.compile(r'trapped surface|collapse (?:does not|never|must not)?\s*complete|(?:event )?horizon completes|'
                    r'complet\w* at finite (?:exterior|cosmic) time|finite (?:exterior|cosmic) time', re.I)
OPEN = re.compile(r'\btests?\b|\bopen\b|\bheld to\b|discriminat\w*[^.]{0,60}observational', re.I)
THM = re.compile(r'\btheorem\b|\bprov(?:en|ed)\b|general relativity alone|standard general relativity', re.I)


def scan(rev):
    out = []
    for stem in OWN:
        if stem == 'BH_causality_v2':
            continue
        r = subprocess.run(['git', 'show', f'{rev}:corpus/{stem}.tex'], cwd=ROOT, capture_output=True, text=True)
        if r.returncode:
            continue
        for s in SENT.split(T.strip(r.stdout)):
            f = ' '.join(s.split())
            if 'JanzenBHcausality' in f and ANCHOR.search(f):
                g = ('OPEN' if OPEN.search(f) else '') + ('+THEOREM' if THM.search(f) else '')
                out.append((stem, g.strip('+') or 'UNGRADED', f))
    return out


for tag, rev in (('BEFORE r7168 (09161f5c^)', '09161f5c^'), ('AFTER r7168 (09161f5c)', '09161f5c'), ('NOW (HEAD)', 'HEAD')):
    rows = scan(rev)
    from collections import Counter
    print(f'\n== {tag}: {len(rows)} anchored site(s); grades {dict(Counter(g for _, g, _ in rows))}')
    print(f'   per paper: {dict(Counter(p for p, _, _ in rows))}')
    for p, g, f in rows:
        if 'OPEN' in g and 'THEOREM' not in g:
            print(f'     [{g}] {p}: {f[:170]}')


# ⌗ ADDED AFTER THE PRE-REGISTERED RUN (labelled so): the grade window widened to the anchored sentence +-1, to measure
#   whether the grades G6 missed sit one sentence away -- and whether widening invents OPEN on the repaired tree.
def scan_window(rev, w=1):
    out = []
    for stem in OWN:
        if stem == 'BH_causality_v2':
            continue
        r = subprocess.run(['git', 'show', f'{rev}:corpus/{stem}.tex'], cwd=ROOT, capture_output=True, text=True)
        if r.returncode:
            continue
        S = [' '.join(s.split()) for s in SENT.split(T.strip(r.stdout))]
        for i, f in enumerate(S):
            if 'JanzenBHcausality' in f and ANCHOR.search(f):
                ctx = ' '.join(S[max(0, i - w):i + w + 1])
                out.append((stem, bool(OPEN.search(ctx)) and not THM.search(f), f))
    return out


for tag, rev in (('BEFORE r7168, window +-1', '09161f5c^'), ('AFTER r7168, window +-1', '09161f5c')):
    rows = scan_window(rev)
    print(f'\n== {tag}: {sum(o for _, o, _ in rows)} of {len(rows)} anchored sites read OPEN '
          f'(per paper: {dict(Counter(p for p, o, _ in rows if o))})')
