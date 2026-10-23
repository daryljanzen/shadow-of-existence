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

⛭ r7577 (69): THE CENSUS IS REFRESHED AND THE GATE IS WIRED.  `items_keyed.tsv` is now
`r7577_69_the_census_refresh/`'s: the net run on the papers as they stand, every candidate whose sentence
changed since r7371 read again against the stride's 29 rulings.  Three things change here, each named:
  ① a class for what PO-86's own r7451 clause says must NOT be rowed -- `LIMIT`, an r7013 kind-② stated
    limit, a boundary, a decline or a weight marker -- exempt from ⒜ and counted where it can be seen;
  ② ⒞, the half that makes this a ratchet rather than a snapshot: the gate RE-EXTRACTS the papers with the
    census's own net (`net.py`) and fails on any candidate the census has not read and on any census row
    whose sentence no longer exists -- so a reworded statement of openness is read before it is credited,
    which is the key's own rule (KEY.md);
  ③ it runs in `gates.yml`, PO-86's discharge clause asking for exactly this: "a GATE asserting it, so
    the drift cannot recur".
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CENSUS_DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7577_69_the_census_refresh')
KEYED = os.path.join(CENSUS_DIR, 'items_keyed.tsv')
sys.path.insert(0, CENSUS_DIR)
import net  # noqa: E402 -- the census's own net, so gate and census extract the same candidates
REGISTER = os.path.join(ROOT, 'THE_REGISTER.md')

# ⌗ rows DECLARED infrastructure: live by their own job rather than by a paper stating them open.
#   A row named here is exempt from direction ⒝ and the reason is recorded beside it.
INFRASTRUCTURE = {
    'PO-78': 'the quote/prose-pin family -- an instrument debt, not a physics item any paper states',
    # 'PO-86' was this census's own row and is struck at r7577 on its discharge clause, this gate being its fourth part.
}

# ⛭ r7411: THE CENSUS HAS A VINTAGE AND DIRECTION ⒝ MUST NOT SPEND IT AS IF IT DID NOT.
#   `items_keyed.tsv` is 69's reading of the eighteen papers AS THEY STOOD AT r7371.  Direction ⒝
#   asks whether a live row is stated open in some paper, and it answers from that frozen reading --
#   so a row OPENED AFTER r7371 is reported unstated whether or not a later revision put the
#   sentence in the paper, and four of the five it named on the first run that reached this check
#   (PO-87..PO-91) are in exactly that position, three of them stated open by r7401/r7407/r7409.
#   ⇒ The rows are NOT declared infrastructure -- every one is physics -- and the comparison is NOT
#   silenced.  It is SPLIT: a row the census period covers is a finding, and a row opened after it
#   is this instrument's own blind spot, reported as such and not counted against the tree.  The
#   remedy for the second class is a census refresh (69's reading), never an entry above.
CENSUS_REVISION = 7577


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
    limits = [i for i in items if i['cls'] == 'LIMIT']
    bad = 0

    print()
    print('  OPEN-ITEM COHERENCE -- two lists compared; no item is classified here')
    print(f'    {len(items)} adjudicated candidate(s), {len(opens)} classed OPEN by 69')
    print(f'    {len(limits)} classed LIMIT: stated limits, boundaries, declines and weight markers, which PO-86\'s'
          f' r7451 clause says must not be rowed')
    print(f'    register: {len(live)} live PO row(s), {len(struck)} struck')
    print()

    # ⒞ the census is CURRENT: every candidate the net catches in the papers today has been read, and
    #   every row the census carries still names a sentence the papers contain.
    have = {(i['paper'], i['sent']) for i in items}
    now = net.candidates(ROOT)
    nowset = set(now)
    unread = [k for k in now if k not in have]
    gone = [k for k in sorted(have) if k not in nowset]
    if unread or gone:
        print(f'  ⛔ THE CENSUS IS BEHIND THE PAPERS: {len(unread)} candidate(s) the census has not read, '
              f'{len(gone)} census row(s) whose sentence is gone.')
        for p, t in unread[:12]:
            print(f'    unread  {p:4} {t[:110]}')
        for p, t in gone[:12]:
            print(f'    gone    {p:4} {t[:110]}')
        print('    ⇒ read each unread sentence and add its row (class, topic, register, note) to items_keyed.tsv;')
        print('      drop the rows whose sentence is gone.  A reworded statement of openness is a new site.')
        bad += 1
    else:
        print(f'    ⒞ the census is current: all {len(now)} candidates in the papers are read, none stale.')

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
    # r7411: the key was `int(x[1:])`, which strips ONE character -- fine for `L-165` and a
    #   ValueError on every `PO-NNN`.  So check ⒝ below, the register-to-papers direction of
    #   `PO-86`'s own object, crashed instead of reporting whenever a PO row was unstated, and
    #   this gate was absent from the arbiter's turn batch, so nothing read the traceback.
    #   Sort on (prefix, number) so both id families order.
    def _idkey(x):
        pre, _, num = x.rpartition('-')
        return (pre, int(num))
    unstated = sorted(live - pointed - set(INFRASTRUCTURE), key=_idkey)
    # Split by census vintage: only rows the census period covers are findings (see CENSUS_REVISION).
    reg_text = open(REGISTER, encoding='utf-8').read()
    def _opened_at(po):
        m = re.search(r'^\| (?:~~)?\*\*' + re.escape(po) + r'\*\*(?:~~)? .*$', reg_text, re.M)
        if not m:
            return None
        o = re.search(r'OPENED\s+`?r(\d{3,5})`?', m.group(0))
        return int(o.group(1)) if o else None
    covered, after = [], []
    for po in unstated:
        at = _opened_at(po)
        (after if (at is not None and at > CENSUS_REVISION) else covered).append((po, at))
    if covered:
        print(f'  ⛔ {len(covered)} LIVE row(s) the census period covers that no OPEN item states '
              f'and no declaration covers: {[p for p, _ in covered]}')
        bad += 1
    else:
        print('    ⒝ every live row the census period covers is stated open or declared.')
    if after:
        print(f'    ⌗ {len(after)} live row(s) opened AFTER the census (r{CENSUS_REVISION}) -- this '
              f"instrument cannot see whether a paper states them, so they are NOT counted here:")
        for po, at in after:
            print(f'        {po}  opened r{at}')
        print('      ⇒ THE REMEDY IS A CENSUS REFRESH (69 reads the papers), never a declaration.')
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
