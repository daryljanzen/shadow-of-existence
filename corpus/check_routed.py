#!/usr/bin/env python3
"""check_routed.py -- THE QUEUE LINT: which routed items still describe a real defect?

** WHY. **  `FOR_54.md` reached ** 49 items, 18 marked discharged and 27 not ** -- and a spot check found
that ** item 29's defect is GONE (cor:radiation no longer cites itself) while item 22's is STILL THERE
(P12's weyl-a3 renders after the bibliography) **.  ⇒ ** A queue nobody can trust is a queue that gets
re-read from the top every session, which is the tax 54 has been paying. **

  ⌗ And the same measurement found ** two items both numbered 44 ** -- the routing-queue form of the
  `L-510` ID collision.  ** Renumbered at r2532; this lint now catches it. **

** WHAT IT CHECKS. **
  1. ** DUPLICATE ITEM NUMBERS ** -- exact, and a hard failure.  Two items sharing a number means one of
     them cannot be referred to.
  2. ** MECHANICAL DEFECTS ** -- items whose defect has a signature testable against the papers.  Each
     probe is written here with its item number, so the queue and the test travel together.
  3. ** AND IT REPORTS THE REST AS "NEEDS A READ" ** rather than guessing.  *** A lint that pretends to
     judge prose is worse than one that says which items it cannot judge. ***

⚠ ** LINT, NOT A GATE, except for the duplicate check. **  Whether a prose defect still stands is a
reading, and no script does that.  ** What this converts is a 27-item unknown into a short known list. **

    python3 corpus/check_routed.py
    python3 corpus/check_routed.py --all

Written r2532.  Stated for reversal.
"""
import collections
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def body(path):
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(path, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


def papers():
    return {os.path.basename(f): f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
            if not os.path.basename(f).startswith('appendix_receipts')}


# ** THE PROBES.  Each returns (still_a_defect, note).  Written beside the item number so the queue
# and its test travel together -- the thing FOR_54 never had. **
def probe_22():
    """P12's sec:weyl-a3 renders after the bibliography."""
    raw = open(os.path.join(ROOT, 'corpus', 'algebroid_paper.tex'),
               encoding='utf-8', errors='replace').read()
    bib = raw.find('\\begin{thebibliography}')
    wey = raw.find('weyl-a3')
    if bib < 0 or wey < 0:
        return None, 'anchor not found -- needs a read'
    return (wey > bib), f'bibliography at {bib}, weyl-a3 at {wey}'


def probe_29():
    """cor:radiation cites itself for its own reason."""
    p9 = body(os.path.join(ROOT, 'corpus', 'range_paper.tex'))
    i = p9.find('label{cor:radiation}')
    if i < 0:
        return None, 'cor:radiation not found -- needs a read'
    seg = p9[i + 20:i + 1400]
    return ('cor:radiation' in seg), 'self-reference inside the corollary body'


def probe_40():
    """P15 still carries the framing c54.190-191 retracted (the ~21% and 24% figures)."""
    p15 = body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    hits = [s for s in ('21\\%', '24\\% of', 'first peak position') if s in p15]
    return (len(hits) > 0), f'retracted framings present: {hits or "none"}'


def probe_48():
    """The Higgs sector is identified in P6 and never named anywhere."""
    allp = ' '.join(body(f) for f in papers().values())
    return (len(re.findall('Higgs', allp, re.I)) == 0), '"Higgs" occurrences across the papers'


def probe_46():
    """Types II and III are unnamed under a claim of every algebraic type."""
    p9 = body(os.path.join(ROOT, 'corpus', 'range_paper.tex'))
    unnamed = ('Type~II' not in p9) and ('Type~III' not in p9)
    claims = 'across every algebraic (Petrov) type' in p9
    return (unnamed and claims), 'the claim stands and the two types are unnamed'


def probe_45():
    """P12 cites Teitelboim1973 for the brackets' form and never for the uniqueness content."""
    p12 = body(os.path.join(ROOT, 'corpus', 'algebroid_paper.tex'))
    allp = ' '.join(body(f) for f in papers().values())
    return ('Teitelboim1973' in p12 and len(re.findall('Lovelock', allp, re.I)) == 0), \
           'Teitelboim cited, Lovelock absent'


def _raw(f):
    q = os.path.join(ROOT, f)
    return open(q, encoding='utf-8', errors='replace').read() if os.path.exists(q) else None


def probe_6():
    """OPEN_PROBLEMS_MAP's header claims every live item has been folded."""
    t = _raw('OPEN_PROBLEMS_MAP.md')
    if t is None:
        return None, 'file absent'
    hit = 'every live item has been folded' in t
    return hit, f'header phrase present: {hit}'


def probe_7():
    """FORK_c54.md narrates c54.1-c54.35 and reads as current."""
    t = _raw('FORK_c54.md')
    if t is None:
        return False, 'FORK_c54.md absent -- moot by removal'
    return ('c54.35' in t), 'narrative anchored at c54.35 with no span note'


def probe_8():
    """Three receipts print a verdict with nothing compared."""
    paths = ('receipts/P05_groupoid/negation_outer_A2.py',
             'receipts/P14_matter_sector_paper/P14_naming_a_derived_object.py',
             'receipts/P15_CR_cosmology/P15_verify_numeric.py')
    have = [p for p in paths if _raw(p) is not None]
    if not have:
        return None, 'none of the three receipts found'
    bad = [os.path.basename(p) for p in have
           if 'assert' not in _raw(p) and 'check(' not in _raw(p)]
    return (len(bad) > 0), f'{len(have)}/3 present, {len(bad)} without assertions: {bad or "none"}'


def probe_11():
    """P5 names the Lyapunov object bare where P7 cites Cardoso."""
    p5 = _raw('corpus/groupoid_paper.tex')
    if p5 is None:
        return None, 'P5 not found'
    return ('Lyapunov' in p5 and 'Cardoso' not in p5), \
           f'Lyapunov:{"Lyapunov" in p5} Cardoso:{"Cardoso" in p5}'


def probe_19():
    """P1's scope section contradicts its own abstract about r=0."""
    p1 = body(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'))
    hit = 'curvature singularity at $r=0$' in p1
    return hit, f'scope sentence present: {hit}'


def probe_20():
    """P7 conflates the Friedmann initial singularity with the degenerate Nariai member."""
    p7 = body(os.path.join(ROOT, 'corpus', 'CR_framework.tex'))
    hit = ('is the finite-curvature cosmogenesis branch point' in p7
           and 'degenerate Nariai member' in p7)
    return hit, f'the appositive is present: {hit}'


PROBES = {6: probe_6, 7: probe_7, 8: probe_8, 11: probe_11, 19: probe_19, 20: probe_20,
          22: probe_22, 29: probe_29, 40: probe_40, 45: probe_45, 46: probe_46, 48: probe_48}


def main():
    show_all = '--all' in sys.argv
    print()
    print('  check_routed -- which routed items still describe a real defect?')
    print()
    q = os.path.join(ROOT, 'FOR_54.md')
    if not os.path.exists(q):
        print('  FOR_54.md absent.')
        return 0
    t = open(q, encoding='utf-8', errors='replace').read()

    heads = [l for l in t.split('\n') if l.startswith('## ')]
    items = {}
    for h in heads:
        m = re.search(r'(\d+)\s*·', h)
        if m:
            items.setdefault(int(m.group(1)), []).append(h)

    # ⓵ duplicates -- hard failure
    dupes = {n: len(v) for n, v in items.items() if len(v) > 1}
    if dupes:
        print(f'  [FAIL] DUPLICATE ITEM NUMBERS: {dupes}')
        print('     ** Two items sharing a number means one of them cannot be referred to --')
        print('     the routing-queue form of the L-510 ID collision. **')
        print()
        return 1

    marked = {n for n, v in items.items() if re.search(r'✔|DISCHARGED', v[0])}
    unmarked = sorted(set(items) - marked)
    print(f'  {len(items)} numbered item(s); {len(marked)} marked discharged, {len(unmarked)} not.')
    print()

    stale, real, unknown = [], [], []
    for n in unmarked:
        if n not in PROBES:
            unknown.append(n)
            continue
        still, note = PROBES[n]()
        if still is None:
            unknown.append(n)
        elif still:
            real.append((n, note))
        else:
            stale.append((n, note))

    if stale:
        print('  ⛭ THESE ITEMS\' DEFECTS ARE GONE -- mark them discharged:')
        for n, note in stale:
            print(f'     item {n}: {note}')
        print()
    if real:
        print('  ⌗ these still describe a real defect:')
        for n, note in real:
            print(f'     item {n}: {note}')
        print()
    print(f'  ⚠ {len(unknown)} item(s) have no mechanical probe and NEED A READ: {unknown}')
    print('     ** A lint that pretends to judge prose is worse than one that says which items it')
    print('     cannot judge. **  Add a probe here when an item gets a testable signature.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
