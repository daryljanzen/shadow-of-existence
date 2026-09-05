#!/usr/bin/env python3
"""regen_grain_currency.py -- the grains' "what I do not cover" block, GENERATED.

** WHY THIS EXISTS, and it is a structural answer to a recurring debt rather than a third payment
of it. **

`check_grains` has failed on THE_PLAN and THE_OPEN_PROBLEMS_LEDGER three times: at r2440, at r2445
(where they were given a hand-written currency block naming the rows struck and opened since r2417),
and at r2468, ** twenty-three revisions later, for exactly the same reason. **

⇒ ** These documents will go stale every ~20 revisions FOREVER, because of what they ARE. **  ARC 17's
finding names the class: the corpus has no place for a sentence that is true-for-now, and ** a
document whose whole content is "the shape of the work" is made wholly of such sentences ** -- the same
diagnosis that explained why THE_EVOLUTION_MAP was the stalest document in the corpus.

** SO THE ANSWER IS NOT TO WRITE THE BLOCK AGAIN.  IT IS TO GENERATE IT. **  The register is
machine-readable: every row carries its ID, its struck/live state in the leading `**`/`~~`, and the
revisions at which it was REGISTERED / FOLDED / OPENED / STRUCK.  ** So "which rows moved since revision
N" is a computation, not a reading ** -- and the corpus already handles exactly this class with
regen_teed_up, regen_burn_down and regen_map_status.

** WHAT IT DOES AND DOES NOT SOLVE, stated so it is not oversold: **
  * ** SOLVES: the ID half. **  Which rows were struck and which opened since the block's own baseline,
    listed and always correct.
  * ** DOES NOT SOLVE: the reading half. **  What a document's BODY now gets wrong is a judgement, and
    ** a gate can check a declaration, not a judgement ** (r2447).  The generated block therefore
    carries a hand-written PROSE slot which the script preserves verbatim across regenerations and
    never invents.
  ⇒ ** So the recurring mechanical debt is dissolved and the standing editorial one is made visible,
    which is the correct division. **

⌗ AND THE TRAP THIS AVOIDS, recorded because this line walked into it at r2440: `check_grains` measures
lag ** by git commits **, so writing ANYTHING into a stale document turns it green.  ** A generated
block is not a defence against that -- nothing is.  What it is instead is a block whose ID half can be
AUDITED against the register by anyone who doubts the green. **

    python3 scripts/regen_grain_currency.py           # rewrite the blocks
    python3 scripts/regen_grain_currency.py --check   # verify they match the register

Written r2469.  Stated for reversal.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# both ID spaces: THE_LIVE_ARC carries the L-row history and stopped at r3001;
# THE_REGISTER opened at r3009 and carries the live PO-rows.  A currency block
# that reads only one of them cannot report the other's movement.
REGISTERS = [os.path.join(ROOT, 'THE_LIVE_ARC.md'),
             os.path.join(ROOT, 'THE_REGISTER.md')]

# the grains that carry a currency block, and the baseline each declares from
# ⛔⛭⛭ ** EXTENDED r3112 (`L-252`): THIS COVERED TWO OF THE FOUR GRAINS `check_grains` MEASURES. **
# *This script's own docstring says these documents "will go stale every ~20 revisions FOREVER,
# because of what they ARE" -- and then answered that for `THE_PLAN` and `THE_OPEN_PROBLEMS_LEDGER`
# while `OPEN_PROBLEMS_MAP` and `THE_WEAVE` were left to the rot the script was built to end.*
#   ⇒ *** So the structural answer covered half the structure, and the other half failed on schedule.
#       A fix built for a class must cover the class, or it converts a known debt into a surprising
#       one -- which is worse, because nobody is watching the half that was fixed. ***
# ** The list is IMPORTED from the gate rather than copied, so the two cannot drift apart again --
# the same reason `check_burndown` imports `check_id_bands`'s BANDS. **
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('_cg', os.path.join(ROOT, 'corpus', 'check_grains.py'))
_cg = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_cg)
GRAINS = [fn for fn, _what in _cg.GRAINS]

BEGIN = '<!-- GRAIN-CURRENCY:BEGIN -->'
END = '<!-- GRAIN-CURRENCY:END -->'
PROSE_BEGIN = '<!-- GRAIN-CURRENCY:PROSE -->'


def rows():
    """(id, struck, [revisions mentioned]) for every register row"""
    out = []
    unstamped = []
    lines = []
    for reg in REGISTERS:
        if os.path.exists(reg):
            lines += open(reg, encoding='utf-8', errors='replace').read().split('\n')
    for line in lines:
        # ⛔⛭ ** THE PATTERN DID NOT MATCH THE REGISTER'S OWN ROWS -- repaired r4149. **
        # *It required the id to be its own first cell (`| **PO-13** |`).  `THE_REGISTER`'s LIVE rows
        # put the id and its text in the SAME cell (`| **PO-13** **THE DRIVING...**`), and its STRUCK
        # rows wrap the id twice (`| ~~**PO-14**~~ |`).  Neither form matched, so this script read the
        # register, found no PO rows at all, and emitted a currency head enumerating only `L-` ids --
        # **silently, and looking like a complete answer.**  `THE_OPEN_PROBLEMS_LEDGER` is the document
        # Phase 3's complete-and-unfiltered list is drawn from, and it carried none of `PO-21`..`PO-31`.*
        #   ⇒ *The id is now taken from the first cell however it is decorated, and the trailing `\|` is
        #     dropped because a one-cell row is a legitimate row shape here.*
        m = re.match(r'^\|\s*(?:~~|\*\*)+((?:L|PO)-\d+)(?:~~|\*\*)+', line)
        if not m:
            continue
        struck = line.lstrip().startswith('| ~~')
        opened = [int(r) for r in re.findall(r'\b(?:REGISTERED|FOLDED|OPENED)\s+r(\d{4})', line)]
        if not opened and not struck:
            opened = [int(r) for r in re.findall(r'\bopened\s+r(\d{4})', line)]
        # ⛔⛭ ** AND A LIVE ROW WITH NO OPENED-STAMP WAS INVISIBLE -- repaired r4149. **
        # *`PO-13`, `PO-23`, `PO-25` and `PO-26` are live rows carrying no `OPENED r####` of any
        # spelling, so they classified as neither opened nor struck and appeared in no currency
        # list.  ** A row that exists and is reported nowhere is exactly the failure a
        # complete-and-unfiltered list exists to prevent, and it is worse than a missing row
        # because the instrument still reports a total. **
        #   ⛔ *A first attempt INFERRED the opening from the earliest revision the row names, and that
        #     is a guess that goes wrong exactly where it matters: `PO-25`'s earliest named revision is
        #     a CLOSURE it cites (`Kerr half closed r2378`), not its opening, so the inference filed a
        #     live post-baseline row as pre-baseline.*
        #   ⇒ *** An unstamped live row is REPORTED AS UNSTAMPED, not dated by inference.  The
        #       instrument's job is to make every row visible, and a wrong date is less honest than a
        #       named gap -- it looks like knowledge. ***
        if not opened and not struck:
            unstamped.append(m.group(1))
        killed = [int(r) for r in re.findall(r'\bSTRUCK\s+r(\d{4})', line)]
        out.append((m.group(1), struck, opened, killed))
    if unstamped:
        sys.stderr.write('  unstamped live rows (reported, not dated): '
                         + ' '.join(sorted(set(unstamped))) + '\n')
    return out


def since(baseline):
    st, op = [], []
    for rid, struck, opened, killed in rows():
        if any(r >= baseline for r in killed):
            st.append(rid)
        if any(r >= baseline for r in opened):
            op.append(rid)
    return sorted(set(st)), sorted(set(op))


def front():
    """the register's own highest main-line revision"""
    t = ''
    for reg in REGISTERS:
        if os.path.exists(reg):
            t += open(reg, encoding='utf-8', errors='replace').read()
    rs = [int(x) for x in re.findall(r'\br(\d{4})\b', t)]
    return max(rs) if rs else 0


def block(baseline, prose):
    st, op = since(baseline)
    L = [BEGIN, '']
    L.append(f'## ⌗⌗⌗ CURRENCY — **GENERATED** by `scripts/regen_grain_currency.py`, '
             f'baseline r{baseline}, register front r{front()}')
    L.append('')
    L.append('> ⚠ **THE BODY BELOW STOPS AT THE BASELINE. This head is the list of what has moved '
             'since, and it is REGENERATED rather than written** — *because these documents go stale '
             'every ~20 revisions by construction, and paying that by hand is a debt that recurs '
             'rather than a defect that closes.*')
    L.append('>')
    L.append(f'> **⌗ NOT COVERED — STRUCK since r{baseline} ({len(st)} rows):**')
    L.append('> ' + (' '.join(f'`{x}`' for x in st) if st else '*(none)*'))
    L.append('>')
    L.append(f'> **⌗ NOT COVERED — OPENED since r{baseline} ({len(op)} rows):**')
    L.append('> ' + (' '.join(f'`{x}`' for x in op) if op else '*(none)*'))
    L.append('>')
    L.append('> ⌗ ***The ID half is machine-checked against the register; run '
             '`regen_grain_currency.py --check`. The prose half below is a JUDGEMENT and is written '
             'by hand — the script preserves it verbatim and never invents it, because a gate can '
             'check a declaration and not a judgement.***')
    L.append('')
    L.append(PROSE_BEGIN)
    L.append(prose.strip() if prose.strip() else
             '> *(no hand-written note — what the body actively misleads about has not been stated)*')
    L.append('')
    L.append(END)
    return '\n'.join(L)


def existing_prose(text):
    if PROSE_BEGIN not in text or END not in text:
        return ''
    return text.split(PROSE_BEGIN, 1)[1].split(END, 1)[0]


def baseline_of(text, default):
    m = re.search(r'baseline r(\d{4})', text)
    return int(m.group(1)) if m else default


def main():
    checking = '--check' in sys.argv
    bad = []
    for g in GRAINS:
        p = os.path.join(ROOT, g)
        t = open(p, encoding='utf-8', errors='replace').read()
        base = baseline_of(t, 2417)
        prose = existing_prose(t)
        new = block(base, prose)
        if BEGIN in t and END in t:
            head, rest = t.split(BEGIN, 1)
            _, tail = rest.split(END, 1)
            out = head + new + tail
        else:
            i = t.index('\n---\n', 4) + len('\n---\n')
            out = t[:i] + '\n' + new + '\n' + t[i:]
        if checking:
            if out != t:
                bad.append(g)
        else:
            open(p, 'w', encoding='utf-8').write(out)
            st, op = since(base)
            print(f'  {g:<32} baseline r{base}: {len(st)} struck, {len(op)} opened since')

    if checking:
        if bad:
            print(f'  [FAIL] grain currency block is stale in: {", ".join(bad)}')
            print('     Run: python3 scripts/regen_grain_currency.py')
            return 1
        print(f'  grain currency blocks match the register ({len(GRAINS)} grains)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
