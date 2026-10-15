#!/usr/bin/env python3
"""THE COHERENCE GATE -- does every open item the papers state have a live register row, and is every
live row stated open in a paper or declared infrastructure?

⛭ `PO-86` opened on `69`'s census and its discharge depends on this instrument.  `r7371` ⑥ ①: *"Every
open item the papers state has a live register row; and every live row is stated open in a paper or is
declared infrastructure."*

⛔ WHAT THIS GATE MUST NOT DO, and `r7371` ⑥ ④ is explicit: ***it must not decide whether an item is
open.***  That is a reading, `69` refused to make it from a census, and each struck case is either a
stale paper or a row struck too early.  ⇒ **So the class comes from the ADJUDICATED baseline
(`items_keyed.tsv`, `69`'s reading re-keyed) and never from this file.  The gate compares two lists and
names what is in one and not the other.**

THE KEY is `(paper, normalised marker sentence)` -- `check_prose_pins`' own rule one level up.  What
moves it, what does not, and why not `69`'s paragraph index, are in
`computations/beyond_the_wall/r7371_cc66_the_coherence_key/key.py`.

⚠ STATUS: this gate is NOT in `gates.yml` and is not wired to any job.  `r7371` ⑥ ③ asks for the price
first; it prints and exits 0 on a clean correspondence, non-zero otherwise, so it can be wired when
the correspondence is one a ratchet should hold.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYED = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7371_cc66_the_coherence_key',
                     'items_keyed.tsv')
REGISTER = os.path.join(ROOT, 'THE_REGISTER.md')

# ⌗ rows DECLARED infrastructure: live by their own job rather than by a paper stating them open.
#   A row named here is exempt from direction ⒝ and the reason is recorded beside it.
INFRASTRUCTURE = {
    'PO-78': 'the quote/prose-pin family -- an instrument debt, not a physics item any paper states',
    'PO-86': "this census's own row: the coherence question itself, opened by r7371 on 69's reading",
}


def live_rows():
    """PO ids live in THE_REGISTER.md -- struck rows carry ~~**PO-N**~~, live ones do not"""
    s = open(REGISTER, encoding='utf-8').read()
    struck = set(re.findall(r'~~\*\*(PO-\d+)\*\*~~', s))
    return set(re.findall(r'\*\*(PO-\d+)\*\*', s)) - struck, struck


def keyed():
    out = []
    for ln in open(KEYED, encoding='utf-8').read().split('\n'):
        if ln.startswith('#') or '\t' not in ln:
            continue
        c = ln.split('\t')
        if len(c) >= 5:
            out.append(dict(paper=c[0], sent=c[1], cls=c[2], topic=c[3], reg=c[4]))
    return out


def pointers(reg):
    """every PO id a census pointer names, including the `PO-48/54/55` shorthand"""
    if not reg or reg == '-':
        return set()
    ids = set(re.findall(r'PO-\d+', reg))
    head = re.match(r'PO-(\d+)', reg)
    if head:
        ids.update('PO-' + n for n in re.findall(r'/(\d+)', reg))
    return ids


def main():
    live, struck = live_rows()
    items = keyed()
    opens = [i for i in items if i['cls'] == 'OPEN']
    bad = 0

    print()
    print('  OPEN-ITEM COHERENCE -- two lists compared; no item is classified here')
    print(f'    {len(items)} adjudicated candidate(s), {len(opens)} classed OPEN by 69')
    print(f'    register: {len(live)} live PO row(s), {len(struck)} struck')
    print()

    # ⒜ every open item the papers state has a LIVE register row
    orphan = [i for i in opens if not (pointers(i['reg']) & live)]
    if orphan:
        byp = {}
        for i in orphan:
            byp.setdefault(i['paper'], []).append(i)
        print(f'  ⛔ {len(orphan)} OPEN item(s) with no LIVE register row, in '
              f'{len(byp)} paper(s):')
        for p in sorted(byp, key=lambda x: int(x[1:])):
            pts = {q for i in byp[p] for q in pointers(i['reg'])}
            print(f'    {p:4} {len(byp[p]):3d}  '
                  + (f'pointers all struck: {sorted(pts)[:4]}' if pts else 'no pointer at all'))
        bad += 1
    else:
        print('    ⒜ every OPEN item points at a live row.')

    # ⒝ every live row is stated open in a paper, or is DECLARED infrastructure
    pointed = {q for i in opens for q in pointers(i['reg'])}
    unstated = sorted(live - pointed - set(INFRASTRUCTURE), key=lambda x: int(x[1:]))
    if unstated:
        print(f'  ⛔ {len(unstated)} LIVE row(s) no OPEN item states and no declaration covers: '
              f'{unstated}')
        bad += 1
    else:
        print('    ⒝ every live row is stated open in a paper or declared infrastructure.')
    for po, why in sorted(INFRASTRUCTURE.items()):
        if po in live:
            print(f'      ⌗ {po} DECLARED infrastructure: {why}')

    print()
    print('  ⌗ This gate asserts the CORRESPONDENCE and not the physics.  A stated-open item with no'
          ' live row\n    is EITHER a stale paper OR a row struck too early, and which one it is is a'
          ' reading that\n    belongs to the seat that owns the paper -- never to this file.')
    print()
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
