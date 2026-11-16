#!/usr/bin/env python3
"""r7812 (cc66) item: THE SENTENCE LIST -- every P15 landing site the one pass must touch.

69: "report the sentence list before you edit, so I can read each landing site with you."

** THE METHOD. **  `r7811+cc66.2/.3` measured, by grid-exact swap, which printed numbers MOVE when the
control is re-pointed.  This reads those (old -> new) pairs back out of the swap logs and asks, for
every `\\rcpt{}` sentence in a paper BODY, whether any figure it prints is one of the old values --
**using `check_figures_pinned`'s own allowance for that figure's printed precision**, so a sentence
printing `1.13` is matched to a measured `1.129` and a sentence printing `1.129` is not matched to
something else that rounds there.

⛔ **Only paper BODIES count** (`r7667`'s distinction, kept): a receipt cited in a generated appendix
is cited by construction and prints nothing.

⛔ ** AND THE FIRST VERSION OF THIS SCRIPT WAS WRONG IN THE WAY THE CORPUS HAS A WHOLE GATE FOR. **
It matched a printed figure to a measured move BY NUMERICAL VALUE ALONE, across every receipt at
once, and so reported 26 "landing sites" of which most were coincidences of value and not
dependencies: a printed `10.8\%` matched a measured FRACTION `0.108`; three unrelated quantities all
matched one printed `0.11` in a sentence about the Peebles equation; and the ARM's comb `298.5` and
the SKY's `298.4` both matched the CONTROL's `298.429`, which merely sits near them.  It even flagged
the fourth-feature sentence that `r7811+cc66.3` PROVED cannot move.
  ⇒ ** A number is not its quantity. **  The fix is that a site counts only when the sentence's OWN
  CITED RECEIPT is one whose output that figure moved in -- the swap logs are per-receipt, so the
  linkage exists and the first version simply threw it away.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as F  # noqa: E402

LOGS = [os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7809_cc66_every_figure_that_reads_the_control_at_its_un_refitted_point', n)
        for n in ('repoint_nofit.txt', 'repoint_step8.txt')]
MOVED = re.compile(r'^\s+(-?[\d.]+) -> (-?[\d.]+)\s+delta\s+\S+\s+(.*)$')


RECHDR = re.compile(r'^  (P15_\S+|[A-Z]\w*_\S+)\s*$')


def moved_by_receipt():
    """{receipt name: [(old, new, line shape)]} -- the per-receipt linkage, which is the whole point"""
    out, cur = {}, None
    for p in LOGS:
        if not os.path.exists(p):
            continue
        for ln in open(p, encoding='utf-8'):
            h = RECHDR.match(ln.rstrip('\n'))
            if h:
                cur = h.group(1)
                out.setdefault(cur, [])
                continue
            m = MOVED.match(ln.rstrip('\n'))
            if m and cur:
                try:
                    out[cur].append((float(m.group(1)), float(m.group(2)), m.group(3).strip()))
                except ValueError:
                    pass
    return out


def main():
    by_rec = moved_by_receipt()
    pairs_all = [(o, n) for v in by_rec.values() for o, n, _ in v]
    print('=' * 100)
    print('  r7812 -- THE SENTENCE LIST: every P15 body sentence the one pass must touch')
    print('=' * 100)
    print(f'\n  swap logs cover {len(by_rec)} receipt(s); {len(pairs_all)} measured (old -> new) '
          f'pair(s) in total')
    for r, v in sorted(by_rec.items()):
        print(f'      {len(v):3d} moved  {r[:92]}')

    sites = [(p, n, c) for pop, p, n, c in F.sites() if pop == 'PROSE']
    print(f'\n  {len(sites)} body `\\rcpt` site(s); of those, the ones citing a receipt whose own '
          f'output moved:')

    hits, seen = [], set()
    for paper, name, claim in sites:
        moved = by_rec.get(name)
        if not moved:
            continue                      # ⛔ the linkage: only THIS receipt's own moves may match
        for printed, alts in F.figures(claim):
            for val, allow in alts:
                for old, new, shape in moved:
                    if abs(val - old) <= allow:
                        key = (paper, name, printed, round(old, 6))
                        if key in seen:
                            continue
                        seen.add(key)
                        hits.append((paper, name, printed, old, new, allow,
                                     ' '.join(claim.split())))
    #: ⛭ THE DECISIVE COLUMN.  A site is only an EDIT if the new value prints DIFFERENTLY at the
    #:   precision the sentence already uses.  A figure that moves inside its own last digit needs
    #:   re-deriving in the receipt and leaves the prose alone -- which is a smaller job than the
    #:   count of moved figures suggests, and the distinction 69 needs before reading the sites.
    def reprint(old_s, newv):
        d = len(old_s.split('.')[1]) if '.' in old_s else 0
        return f'{newv:.{d}f}'

    edits = [h for h in hits if reprint(h[2], h[4]) != h[2]]
    print(f'\n  {len(hits)} LANDING SITE(S); of those {len(edits)} CHANGE THE PRINTED DIGITS\n')
    for i, (paper, name, printed, old, new, allow, claim) in enumerate(hits, 1):
        shown = reprint(printed, new)
        verdict = f'EDIT: {printed} -> {shown}' if shown != printed else \
            f'NO EDIT: still prints {printed} (moves inside its last digit)'
        print(f'  [{i}] {paper}   prints  {printed}   (measured {old} -> {new})   ** {verdict} **')
        print(f'      receipt: {name}')
        print(f'      sentence: {claim[:320]}')
        print()

    cited = {n for _, n, _ in sites}
    silent = sorted(r for r in by_rec if r not in cited and by_rec[r])
    print(f'  {len(silent)} receipt(s) whose figures moved but which NO body sentence cites -- '
          f're-derived, no sentence to edit:')
    for r in silent:
        print(f'      {r[:96]}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
