#!/usr/bin/env python3
r"""check_register_ids.py -- TWO REGISTERS IN ONE LEDGER CLAIMING THE SAME ID.

** WHY THIS EXISTS, AND IT IS THE SAME FINDING ONE LEVEL IN. **  *`check_revision_collisions` reports
two lines choosing one revision number because both pick from the FRONT of a shared counter.  Field
ledgers have a second counter with the same shape -- the register ids `I1`, `I2`, ... -- and it has
no band and, until now, no gate.*

  ⛔ ** AND IT HAD ALREADY COLLIDED.  ** *`INTEGRABLE_SYSTEMS_LEDGER.md` carried TWO `## \`I13\``
  headings: 59's "the isotropy stratification is a ledger of first integrals, and it runs short
  exactly where the Carter constant is needed" (r3640) and 60's "the Carter constant is the
  substrate's symmetry, and on Kerr it is not" (r3642).*
    ⌗ ** The two are about the SAME OBJECT, so the collision was not only ambiguous but misleading:
      a reader following `I13` out of one register lands in a different finding about the Carter
      constant. **  *Neither line could have avoided it -- both allocated `I13` as "the next one
      after what I can see", which is exactly the revision-number mechanism.*

*** AND THE REMEDY IS THE OPPOSITE OF THE REVISION-NUMBER ONE, WHICH IS THE POINT WORTH KEEPING. ***
  * *A colliding REVISION id is documented rather than renumbered (`CLAIMS.md` r3563), because it is
    quoted in ledger prose on both lines and rewriting breaks live references.*
  * *A colliding REGISTER id is RENUMBERED, because it is cited only in the registering line's own
    ledger and `receipts/INDEX.md`, plus a GENERATED appendix that regenerates.*  ** 60's `I13`
    became `I16` at r3648 for four edits and no broken reference. **
  ⇒ ** THE RIGHT REMEDY FOR A COLLISION DEPENDS ON HOW FAR THE IDENTIFIER HAS TRAVELLED, and the
    corpus had one rule for both.  ⌗ Renumbering is cheap while an id is local and expensive once it
    is quoted; the moment to pay is therefore the moment it is FOUND, which is what this gate is
    for. **

⌗ ** WHAT THIS IS BLIND TO, stated rather than discovered later. **
  * ** It sees a collision only once BOTH registers are in one file on one tree. **  *While each
    line holds its own unmerged half this cannot fire -- the same limit `check_revision_collisions`
    has, and for the same reason: a collision needs both sides in one history.*
  * ** It does not check that an id is the NEXT free one, only that it is not a duplicate. **  *A
    line may skip ids; skipping wastes a number and confuses nobody.*
  ⇒ *So it prints the next free id per ledger, taking the r3648 lesson: a rule that has to be
    recalled has already failed once, and a number costs nothing to obey.*

⛔⛭⛭ ** AND THE FIRST VERSION OF THIS GATE READ ONLY `##` HEADINGS, WHICH MISSED A SECOND COLLISION
IN THE SAME FILE. **  *A field ledger claims an id in TWO forms -- a `## \`I8\` — ...` heading and a
defining table row `| **\`I8\`** | ...` -- and the probe register uses the row form throughout.*
  ⇒ ** So the heading-only rule saw ten of seventeen ids in `INTEGRABLE_SYSTEMS_LEDGER.md` and would
    have passed a collision living in the other seven.  A gate that reads part of its population
    fails silently in the direction of passing, which is this corpus's own doctrine. **

⌗ *** THE SECOND COLLISION IS 59 WITH ITSELF, AND IT IS THE SAME MECHANISM AGAIN. ***  *`I8` names
BOTH the probe "`Killing form` against `Killing vector` -- a second homonym?" (row, raised by `P03`'s
read at r3608) AND the `P02` pass-B landing "`P02`'s circle is a phase portrait" (heading, r3620).*
** The pass-B landings numbered from the last HEADING rather than from the last id IN USE -- "the next
one after what I can see", with the probe register out of view.  One line, one file, one counter, and
the front it read was only part of the front. **
  ⌷ *`I8` is REPORTED and not renumbered here: both sides are 59's, both are on the trunk, and the
    locator's row 1 cites the heading.  Renumbering another line's registers is not this line's call
    -- but leaving it unreported would be worse, so it is baselined and printed every run.*

⛔ ** WHAT THE GATE CANNOT DECIDE, AND SAYS SO RATHER THAN GUESSING. **  *An id appearing in BOTH a
heading and a table row is USUALLY correct: `I1` is one finding written in a probe row, a summary row
and a section, which is the intended shape.*  ** So co-claim is not a failure -- only a duplicate
HEADING is, and co-claims are REPORTED for a reader. **  *`REVIEWED` below carries the ones a reader
has actually opened and judged, so the report shrinks to what nobody has looked at yet.*

    python3 corpus/check_register_ids.py

Written r3648 (node 60), after the collision above was found by reading the locator table.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

#: a register heading: `## <glyphs> \`I13\` — **TITLE** — r3640`.  The register's own id is the FIRST
#: backticked token of the heading; a later one is a cross-reference and is deliberately not matched.
HEAD = re.compile(r'^#{2,4}\s+[^`\n]*?`([A-Z]{1,3})(\d{1,3})`\s*[—-]')
#: a DEFINING table row -- the probe/register form, `| **\`I8\`** | ...`.  A row that merely mentions
#: an id mid-cell is a cross-reference and is deliberately not matched.
ROW = re.compile(r'^\|\s*\*\*`([A-Z]{1,3})(\d{1,3})`\*\*\s*\|')

#: ⛔ ** `P` IS THE PAPER NAMESPACE AND NOT A REGISTER PREFIX. **  *The locator and reach tables carry
#: rows like `| **`P16`** | ... |`, which are PAPERS.  Counting them made this gate advise `P17` as
#: the "next free register id" in six ledgers -- advice that is not merely useless but wrong, since
#: `P17` is a paper.*  ⇒ *A gate whose ADVICE is wrong is worse than one that gives none, so the
#: paper namespace is excluded by name rather than by hoping no one reads that line.*
PAPER = 'P'

#: ⌗ ** co-claims a reader has OPENED and judged.  `verdict` is what the reading found. **
REVIEWED = {
    ('INTEGRABLE_SYSTEMS_LEDGER.md', 'I1'):
        'ONE finding in three places -- probe row, summary row and section all carry `P09`s Carter '
        'origin and route (a). The intended shape, not a collision.',
    ('INTEGRABLE_SYSTEMS_LEDGER.md', 'I8'):
        '⛔ TWO DIFFERENT FINDINGS. Row: the probe *`Killing form` against `Killing vector` -- a '
        'second homonym?*, raised by `P03`s read at r3608. Heading: *`P02`s circle is a phase '
        'portrait*, r3620. Both are 59s and both are on the trunk; reported, not renumbered.',
}


def registers(path):
    """(headings, defining_rows) -- BOTH forms, because reading one is reading half the population"""
    heads, rows = {}, {}
    with open(path, encoding='utf-8', errors='replace') as fh:
        for n, line in enumerate(fh, 1):
            m = HEAD.match(line)
            if m and m.group(1) != PAPER:
                heads.setdefault((m.group(1), int(m.group(2))), []).append((n, line.strip()))
            m = ROW.match(line)
            if m and m.group(1) != PAPER:
                rows.setdefault((m.group(1), int(m.group(2))), []).append((n, line.strip()))
    return heads, rows


def main():
    print()
    print('  check_register_ids -- do two registers in one ledger claim the same id?')
    print('  (the `check_revision_collisions` mechanism, one level in: a shared counter,')
    print('   no band, and both lines taking "the next one after what I can see")')
    print()
    ledgers = sorted(f for f in os.listdir(ROOT) if f.endswith('_LEDGER.md'))
    bad, total, co_new, co_known = 0, 0, [], []
    nexts = []
    for f in ledgers:
        heads, rows = registers(os.path.join(ROOT, f))
        total += len(set(heads) | set(rows))
        for (pre, num), hits in sorted(heads.items()):
            if len(hits) > 1:
                bad += 1
                print(f'    [FAIL] {f}: `{pre}{num}` is claimed by {len(hits)} REGISTER HEADINGS:')
                for n, line in hits:
                    print(f'           line {n}:  {line[:96]}')
        for k in sorted(set(heads) & set(rows)):
            key = (f, f'{k[0]}{k[1]}')
            (co_known if key in REVIEWED else co_new).append((key, heads[k][0][0], rows[k][0][0]))
        both = set(heads) | set(rows)
        if both:
            pres = {}
            for pre, num in both:
                pres.setdefault(pre, []).append(num)
            nexts.append((f, '   '.join(f'`{p}{max(v) + 1}`' for p, v in sorted(pres.items()))))
    print(f'    {len(ledgers)} ledger(s); {total} register id(s) across BOTH forms; '
          f'{bad} duplicated heading(s)')
    print()

    # ⌗ *co-claims: usually correct, so REPORTED rather than failed -- and the ones a reader has
    #   actually opened are separated from the ones nobody has, so the second list is the work.*
    if co_known:
        print('    co-claimed (heading AND defining row) -- READ AND JUDGED:')
        for (key, hl, rl) in co_known:
            print(f'      {key[1]} in {key[0]}  (heading L{hl}, row L{rl})')
            for chunk in _wrap(REVIEWED[key], 84):
                print(f'          {chunk}')
    if co_new:
        print()
        print('    ⚠ co-claimed and NOT YET READ -- a gate cannot tell one finding written twice')
        print('      from two findings under one id, so these are for a reader:')
        for (key, hl, rl) in co_new:
            print(f'      {key[1]} in {key[0]}  (heading L{hl}, row L{rl})')
    print()
    for f, nxt in nexts:
        print(f'    next free in {f:<34} {nxt}')
    print()
    if bad:
        print('    ⛭ ** A REGISTER ID IS RENUMBERED, NOT DOCUMENTED -- the opposite of the revision')
        print('       remedy, and for a measurable reason: it is cited only in this ledger, in')
        print('       `receipts/INDEX.md`, and in a GENERATED appendix that regenerates. **')
        print('    ⌷ *Renumber the one that landed SECOND, to the next free id above.*')
        print()
        return 1
    print('    no ledger carries two register HEADINGS under one id.')
    print()
    return 0


def _wrap(text, width):
    out, line = [], ''
    for w in text.split():
        if len(line) + len(w) + 1 > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w).strip()
    if line:
        out.append(line)
    return out


if __name__ == '__main__':
    sys.exit(main())
