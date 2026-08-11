#!/usr/bin/env python3
"""check_kills.py -- the gate on NEGATIVE verdicts, the mirror of check_receipts.py.

Every mechanical instrument this corpus had policed OVER-CLAIMING; nothing policed a
closure on an open question, and the guard set LEANS toward the negative because every
guard in it was forged against a node that softens.  This is the missing half.

It reads PROTECTED_OPEN.md's register, finds each item's home, and fails if closure
language appears there without an authorised kill receipt under kills/.

A node may write a BOUNDED NEGATIVE (scope stated, object named, filed as material).
A CLOSURE on a registered item requires kills/<ID>.md with all four checks answered and
an explicit authorisation line.  Bounded negatives are the node's; closures are Daryl's.

Exit 1 on any unauthorised closure.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')
KILLDIR = os.path.join(ROOT, 'kills')

# Strong closure tokens.  Deliberately narrow: these are words that tell a later reader
# to stop looking.  Hedged or scoped negatives ("did not produce", "on this route") are
# NOT here, because those are exactly what a node is allowed to write.
CLOSURE = re.compile(
    r'\b(?:IS\s+KILLED|IS\s+DEAD|KILLED,|⛔\s*DEAD|is\s+settled\s+in\s+the\s+negative'
    r'|the\s+lead\s+is\s+dead|question\s+is\s+closed|CLOSED\s+in\s+the\s+negative'
    r'|forecloses?\b|rules?\s+it\s+out\b|cannot\s+be\s+made\s+to\s+work)\b',
    re.I)

# Wording that marks a negative as bounded -- present near a closure token, it is a
# scoped result rather than a verdict, and the gate lets it through.
BOUNDED = re.compile(
    r'\b(?:BOUNDED\s+NEGATIVE|on\s+this\s+route|on\s+the\s+object\s+computed'
    r'|scope[d]?\s+to|RETRACTED|remains?\s+OPEN|stands?\s+OPEN|STAYS\s+OPEN)\b', re.I)

REQUIRED_FIELDS = ['SAME-OBJECT:', 'INVERSION:', 'PRICE:', 'CHAIN:', 'AUTHORISED BY:']


def parse_register():
    if not os.path.exists(REG):
        print('  [FAIL] PROTECTED_OPEN.md is missing -- the register IS the gate.')
        sys.exit(1)
    items = []
    # r2378: read ONLY the register table.  The cross-reference table added the same revision also
    # carries `**PO-N**` cells, and parsing it as the register duplicated every item with the wrong
    # cells -- which immediately produced a false FAIL on an unrelated row.  Found by the gate's own
    # output, not by inspection: the alias wiring and this bug landed in the same pass.
    whole = open(REG, encoding='utf-8', errors='replace').read()
    marker = '## ⌗ THE REGISTER'
    body = whole.split(marker, 1)[1] if marker in whole else whole
    for ln in body.split('\n'):
        m = re.match(r'\|\s*\*\*(PO-\d+[a-z]?)\*\*\s*\|(.*)$', ln)
        if not m:
            continue
        pid, rest = m.group(1), m.group(2)
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', rest)]
        obj = cells[1] if len(cells) > 1 else ''
        homes = re.findall(r'`([^`]+)`', cells[2] if len(cells) > 2 else '')
        items.append({'id': pid, 'question': cells[0], 'object': obj, 'homes': homes,
                      'aliases': []})
    attach_aliases(items)
    return items


def attach_aliases(items):
    """r2378 -- THE BAR HAD A HOLE EXACTLY THE WIDTH OF A NAME.

    This gate protected an item by its `PO-` id.  The lead register in THE_LIVE_ARC carries the
    same OBJECTS under `L-` ids, so a strike written against the L- name tripped nothing.  It
    happened once, in good faith: at c54.128 the fork struck L-164 and reasoned in the row itself
    that "L-164 appears nowhere in PROTECTED_OPEN.  No rule required a sign-off."  Correct on the
    letter -- and L-164's content is PO-4's object.  The node followed the rules as written and the
    rules as written could not see it.  ** The defect was the namespace split, not the node. **

    PROTECTED_OPEN now carries a REGISTER CROSS-REFERENCE table naming, for each item, the register
    row that carries the same object.  This reads those L- codes and protects them under the same
    id, so the hole is closed by the cross-reference EXISTING rather than by anyone remembering it.
    """
    text = open(REG, encoding='utf-8', errors='replace').read()
    if 'REGISTER CROSS-REFERENCE' not in text:
        return
    block = text.split('REGISTER CROSS-REFERENCE', 1)[1]
    block = block.split('## ⌗ THE REGISTER', 1)[0]
    by_id = {i['id']: i for i in items}
    for ln in block.split('\n'):
        if not ln.startswith('|'):
            continue
        pids = re.findall(r'\*\*(PO-\d+[a-z]?)\*\*', ln)
        lids = re.findall(r'\*\*`(L-\d+)`\*\*', ln)
        if not (pids and lids):
            continue
        for pid in pids:
            if pid in by_id:
                by_id[pid]['aliases'].extend(l for l in lids if l not in by_id[pid]['aliases'])


def home_files(homes):
    out = []
    for h in homes:
        for cand in (h, h + '.md', h + '.tex',
                     os.path.join('corpus', h + '.tex'),
                     os.path.join('capstones', h + '.md')):
            p = os.path.join(ROOT, cand)
            if os.path.isfile(p):
                out.append(p)
                break
    return out


def main():
    items = parse_register()
    print(f"  PROTECTED OPEN: {len(items)} registered items")
    unnamed = [i for i in items if 'NOT NAMED' in i['object'].upper()]
    if unnamed:
        print(f"  {len(unnamed)} with NO NAMED OBJECT -- protected absolutely "
              f"(nothing definite to close): {', '.join(i['id'] for i in unnamed)}")

    aliased = [i for i in items if i['aliases']]
    if aliased:
        print(f"  {len(aliased)} item(s) carry a register alias, protected under the same bar: " +
              ', '.join(f"{i['id']}={'/'.join(i['aliases'])}" for i in aliased))

    failures = []
    # r2378: the register itself is a home for any item carrying a register alias, so a strike
    # written against the L- name is scanned under the PO- item's own bar.
    ARCFILE = os.path.join(ROOT, 'THE_LIVE_ARC.md')
    for it in items:
        files = home_files(it['homes'])
        if it['aliases'] and os.path.isfile(ARCFILE):
            files = files + [ARCFILE]
        if not files:
            print(f"  [WARN] {it['id']}: no home file resolved from {it['homes']}")
            continue
        for f in files:
            text = open(f, encoding='utf-8', errors='replace').read()
            lines = text.split('\n')
            # r2378: the register is 300+ KB of many rows.  Adding it whole as a home let the
            # pre-existing key-substring heuristic match an UNRELATED row that merely mentioned the
            # item's words near closure language -- a false FAIL on L-15 for PO-5, caught by the
            # gate's own output within a minute of the alias wiring landing.  ** Scan only the rows
            # that carry one of the item's aliases. **  The alias is the whole point of the link;
            # widening past it re-introduces exactly the name-matching looseness the fix was for.
            if it['aliases'] and os.path.abspath(f) == os.path.abspath(ARCFILE):
                lines = [(i, l) for i, l in enumerate(lines, 1)
                         if any(a in l for a in it['aliases'])]
            else:
                lines = list(enumerate(lines, 1))
            for ln_no, line in lines:
                if not CLOSURE.search(line):
                    continue
                # is the item itself the subject of this line?
                tag = it['question'].split('—')[0]
                key = re.sub(r'[^A-Za-z0-9]', '', tag)[:12]
                flat = re.sub(r'[^A-Za-z0-9]', '', line).lower()
                near = bool(key) and key.lower() in flat
                # ...or the line names one of the item's register aliases
                if not near:
                    near = any(a.replace('-', '').lower() in flat for a in it['aliases'])
                if not near:
                    continue
                if BOUNDED.search(line):
                    continue          # a scoped negative, or an explicit retraction
                kp = os.path.join(KILLDIR, it['id'] + '.md')
                if not os.path.exists(kp):
                    failures.append((it['id'], os.path.relpath(f, ROOT), ln_no,
                                     'closure language, NO kill receipt'))
                    continue
                kt = open(kp).read()
                missing = [fl for fl in REQUIRED_FIELDS if fl not in kt]
                if missing:
                    failures.append((it['id'], os.path.relpath(f, ROOT), ln_no,
                                     'kill receipt missing ' + ', '.join(missing)))
                elif 'NOT NAMED' in it['object'].upper():
                    failures.append((it['id'], os.path.relpath(f, ROOT), ln_no,
                                     'object NOT NAMED -- cannot be closed by anyone yet'))

    print()
    if failures:
        print(f"  UNAUTHORISED CLOSURES: {len(failures)}")
        for pid, f, ln, why in failures:
            print(f"    [FAIL] {pid}  {f}:{ln}  -- {why}")
        print()
        print("  A node may write a BOUNDED NEGATIVE: scope stated, object named, filed")
        print("  as material.  A CLOSURE on a protected item needs kills/<ID>.md with")
        print("  SAME-OBJECT, INVERSION, PRICE, CHAIN answered and AUTHORISED BY set.")
        return 1
    print("  No unauthorised closures on protected open questions.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
