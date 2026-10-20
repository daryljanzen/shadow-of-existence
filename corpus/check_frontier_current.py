#!/usr/bin/env python3
"""check_frontier_current.py -- THE FRONTIER'S RUNWAY MUST NOT LAG ITS ROW.

** WHAT THIS CATCHES, AND IT HAD DRIFTED ON EVERY LIVE ROW AT ONCE. **  `THE_FRONTIER.md`
reads as a generated view of `THE_REGISTER.md`, and for which rows are LIVE it is one --
struck rows drop out correctly.  ** But the per-row content -- title, counts, and the
runway prose a node actually reads to decide what to work -- is a hardcoded table inside
`scripts/regen_frontier.py`. **  Nothing updated it when a register row moved.

At r6473 every one of the eight live rows was behind its row by between 1898 and 2578
revisions, and the same text was being served to the public site through
`BOOK_INTRO_cosmiCave/frontier.html`.  *** A document that looks generated and is not is
worse than one that looks hand-written: nobody thinks to check it. ***

** WHY A STAMP CHECK AND NOT GENERATION. **  The runway is an editorial DIGEST of a
register row that runs to tens of thousands of characters; it cannot be mechanically
derived, and pretending otherwise is what would produce a generated-looking lie again.
** What CAN be checked mechanically is its currency: ** the newest revision a runway
cites must be at least the newest its register row cites.  A row that moves without its
runway moving fails here.

⌗ The remedy for a failure is to WRITE the runway forward, not to bump a number -- and
the gate says so, because a stamp bumped without prose is the same defect wearing the
check's own clothes.

** AND FROM r7457 IT ALSO ASKS WHETHER A RUNWAY IS IN THE RIGHT BLOCK, because currency
   was checked and PLACEMENT was not. **  At r7453 the gate seat, writing `PO-78`'s
runway forward on this gate's own instruction, found the block's end with `awk` on a
column-`0` `),` instead of reading `runway_blocks` above -- which ends a block at a
lookahead for the next dict KEY.  `PO-78`'s key sits at column 0 where every other key is
indented four, so 51 lines of `PO-78`'s amendment landed inside `PO-75`'s block.
  ⌗ *`r7453` reported that block as `PO-79`'s and so did the order that priced this gate.
   It was `PO-75`'s.  The wrong id was restated three times before anyone looked at the
   line numbers, which is `r7447`'s rule -- a row reference restated in a ruling is the
   ruling's, exactly as a number is.*
  *** THIS GATE WOULD HAVE STAYED GREEN. ***  `r7453` appeared in *some* block, and
  currency asks only whether a runway is at or ahead of its row.  The misplacement was
  caught by re-running the gate and reading its output, which is not a check.

** WHY THE PREDICATE IS WHAT IT IS, and the two clauses that were priced and rejected. **
`60` priced the candidates at r7456 and REVERSED its own registration:
  - *"the block contains its own row id"* -- PRICED OUT.  10 of 11 live blocks fail it on
    a correct tree, because a runway says "this row" rather than naming itself.  Adopting
    it would mean rewriting ten blocks to satisfy a gate, which is writing to the
    instrument.
  - *"no revision newer than its own row's newest"* -- SOUND where it applies, 0 of 11
    false positives, and it needs no second copy of the mapping: which revisions belong to
    which row is answered by THE REGISTER, the authority the frontier is generated against.
    ** `60` concluded it did NOT reach the motivating case -- `PO-79` is not in its
    testable set, so the gate would have been green on the only instance the family has.
    *** THAT CONCLUSION IS WITHDRAWN AT r7457, AND THE CAUSE WAS THE WRONG ROW ID. ***
    The text landed in `PO-75`, which is struck and whose row ends at `r7243`, so the
    clause reaches it by 210 revisions.  Controlled at r7457: injected at the real site
    the gate FAILS and names it; on the correct tree it exits 0. **

⇒ *** AND THE CAUSE OF THAT BLINDNESS IS IN THIS FILE, NOT IN THE REGISTER. ***  `60`
  prescribed "require every LIVE row to carry a stamp".  Measured at r7457: every live row
  already carries one, 11 of 11, so that prerequisite was already met and would have
  changed nothing.  ** `register_rows` below sees 11 of the register's 82 rows, because a
  struck row is written `| ~~**PO-79**~~` and its regex requires `| **`. **  Widening the
  read to both forms is the whole fix, and it is one group in one pattern.
  ⌗ *Which is this row's own subject once more: the instrument's reach was narrower than
   its object, and the prescription aimed at the object.*

** THE CLAUSE AS ADOPTED: a STRUCK row's runway must cite nothing newer than its own row.**
  Live rows are governed by currency above, which PERMITS a runway to run ahead of its row
  -- so clause 1 cannot be applied to them without contradicting the gate it lives in.
  Struck rows are the complement and the right home for it: nobody should be writing new
  text into a closed row's runway, and `PO-75` is struck, so the motivating case is reached.
  ⌗ *54 of the 65 runway blocks belong to struck rows, so the clause covers the majority of
   the generator's prose -- and `PO-15` is the one site over, read and baselined below.*
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, '..', 'scripts', 'regen_frontier.py')
REG = os.path.join(HERE, '..', 'THE_REGISTER.md')


def newest_revision(text):
    n = [int(x) for x in re.findall(r'r(\d{3,5})', text)]
    return max(n) if n else None


def runway_blocks(gen):
    """A runway block ends at the next DICT KEY, and a dict key is `'PO-n': (` and nothing else.

    ⛭ r7167: THIS FUNCTION USED TO END A BLOCK AT ANY CONTINUATION STRING STARTING `'PO-`.
      ** The runway is a dict of long prose written as adjacent string literals, so a sentence that
      happens to break across lines with `PO-69` at the start of the next one closed the block there
      and the gate read the stump. **  Measured when it happened: `PO-78`'s runway was cut at
      `3,753` of `59,235` characters -- the whole of this revision's text and more -- and the gate
      reported the runway CURRENT, correctly, because `r7167` appeared on the line BEFORE the cut.
      ⇒ *** SO IT WAS BLIND AND NOT YET WRONG, WHICH IS THE ONLY DIFFERENCE FROM THE r7164 CUT
          IN `register_rows` ABOVE -- the same gate, the same failure, the other input, one
          revision later. ***  ⌗ *A gate that reads a stump gives a true verdict until the
      revision stamp moves past the cut, and then gives a false one with no new defect to blame.*
      ⌗ The fix is to require the KEY form in the lookahead rather than a quote and two letters:
      prose cannot imitate `'PO-\\d+':\\s*\\(` without being a key.  *Rewording the sentence that
      tripped it would have been the other repair available, and it is the wrong one: the gate must
      not be fragile to what a register row says.*
    """
    out = {}
    for m in re.finditer(r"'(PO-\d+)':\s*\(.*?\n(?=\s*'PO-\d+':\s*\(|\s*\}\n)", gen, re.S):
        out[m.group(1)] = m.group(0)
    return out


def register_rows(reg):
    """Each row is ONE LINE of the register, so the row ends at the next newline and nowhere else.

    ⛭ r7164: THIS FUNCTION USED TO CUT A ROW AT 60,000 CHARACTERS and silently read the stump.
      ** Found by `PO-78` reaching 68,599 characters: its `r7164` blocks sat past the cut, so this
      gate read a row whose newest revision was `r7163`, compared it against a runway at `r7163`, and
      reported the runway CURRENT while it lagged. **
      ⇒ *** A STALENESS CHECK THAT TRUNCATES ITS INPUT GOES BLIND EXACTLY WHEN A ROW IS BEING WORKED
          HARDEST -- the row grows past the cut because somebody is writing it, which is when its
          runway is most likely to lag. ***  It is the same shape as the four blindness members in
      `PO-78`: an instrument blind at the moment it matters, for a defensible-looking reason.
      ⌗ The cut was a guard against `' |\\n'` not being found and the slice running to the end of the
      file.  Splitting on the newline cannot run away, so the guard is not needed: a row is a line.
    """
    out = {}
    for pid in re.findall(r'\| \*\*(PO-\d+)\*\*', reg):
        i = reg.index(f'| **{pid}**')
        nl = reg.find('\n', i)
        out[pid] = reg[i:nl if nl != -1 else len(reg)]
    return out


def all_register_rows(reg):
    """EVERY row, struck or live -- the same authority, a wider read.

    `register_rows` above answers "which rows are LIVE", and its `| **PO-n**` form is
    correct for that question.  This answers "which revisions belong to row n", which is
    a different question and must not exclude the struck rows: 71 of the register's 82
    rows are struck, and the one this cycle's misplacement landed in is one of them.
    ⌗ The two readers are not two copies of one predicate; they are two questions of one
      file, and the live/struck distinction is what separates them.
    """
    out = {}
    for m in re.finditer(r'\| (?:~~)?\*\*(PO-\d+)\*\*', reg):
        pid = m.group(1)
        nl = reg.find('\n', m.start())
        out[pid] = reg[m.start():nl if nl != -1 else len(reg)]
    return out


# name -> the reason, READ at the site before it was written here.  An entry is a site
# that has been read and found to be correct prose, never a failure deferred.
PLACEMENT_BASELINE = {
    'PO-15': ("its runway carries an `r6925 (66, on node 60 r6920)` entry -- *ATTEMPTS THE ROW "
              "FOR THE FIRST TIME AND THE ONE ULTRAVIOLET CONSTANT BECOMES OBSERVABLE* -- while "
              "its own struck row ends at `r3100`.  READ at r7457: the entry is a correct digest "
              "of later work bearing on a struck row, and that work IS in the register, under "
              "another row's clause rather than this one's.  ⌗ A digest of a closed row may cite "
              "work that reopened the question elsewhere; what it may not carry is another row's "
              "text."),
}


def placement(blocks, live, every):
    """A struck row's runway must cite nothing newer than its own row.  Returns failures."""
    bad = []
    for pid in sorted(blocks, key=lambda s: int(s[3:])):
        if pid in live or pid not in every:
            continue
        v, r = newest_revision(blocks[pid]), newest_revision(every[pid])
        if v is None or r is None or v <= r:
            continue
        bad.append((pid, v, r))
    return bad


def main():
    if not (os.path.exists(GEN) and os.path.exists(REG)):
        print('  [FAIL] generator or register missing')
        return 1
    gen = open(GEN, encoding='utf-8', errors='replace').read()
    reg = open(REG, encoding='utf-8', errors='replace').read()
    blocks, rows = runway_blocks(gen), register_rows(reg)

    print()
    print('  FRONTIER CURRENCY -- each live row\'s runway against its register row')
    print()
    stale, missing = [], []
    for pid, row in rows.items():
        if pid not in blocks:
            missing.append(pid)
            continue
        v, r = newest_revision(blocks[pid]), newest_revision(row)
        if v is None or r is None:
            continue
        mark = 'current' if v >= r else f'STALE by {r - v}'
        print(f'    {pid:<8} runway r{v:<6} row r{r:<6}  {mark}')
        if v < r:
            stale.append((pid, r - v))
    print()
    # ** ⛔ r6549: A RUNWAY IS NOT ENOUGH.  THE GENERATOR HAS FOUR LISTS AND THIS CHECKED ONE. **
    #   *`PO-45` was registered at r6547 with an `EST` runway, and this gate reported "9 live rows;
    #   every runway is at or ahead of its row" while `THE_FRONTIER` rendered EIGHT and the live site
    #   read eight.*  ** The count comes from the live set; the ROWS come from `ORDER`; the sector
    #   comes from `GROUP`, and a row missing from `GROUP` raises outright. **
    #   ⇒ *** A row needs FOUR things to reach a reader: the register row, the runway, `ORDER` and
    #       `GROUP`.  A gate that checks one of four reports a document current while it is short a
    #       row -- and this one said so to the front end for two revisions. ***
    gen_src = open(GEN, encoding='utf-8', errors='replace').read()
    def _listed(name, pid):
        m = re.search(name + r'\s*=\s*[\[{](.*?)[\]}]', gen_src, re.S)
        return bool(m) and f"'{pid}'" in m.group(1)
    unrendered = [pid for pid in rows if not _listed('ORDER', pid)]
    ungrouped = [pid for pid in rows if not _listed('GROUP', pid)]
    if unrendered:
        print(f'  ⛔ {len(unrendered)} live row(s) absent from ORDER, so they do NOT RENDER: '
              f'{", ".join(unrendered)}')
    if ungrouped:
        print(f'  ⛔ {len(ungrouped)} live row(s) absent from GROUP, which RAISES on generation: '
              f'{", ".join(ungrouped)}')
    if missing:
        print(f'  ⛔ {len(missing)} live row(s) with NO runway: {", ".join(missing)}')
    if stale:
        print(f'  ⛔ {len(stale)} STALE RUNWAY(S) -- the row moved and the view did not:')
        for pid, gap in stale:
            print(f'    [FAIL] {pid} lags its register row by {gap} revision(s)')
        print('     ⌗ WRITE THE RUNWAY FORWARD.  Do not bump the stamp: a stamp moved')
        print('       without the prose is this same defect wearing the gate\'s clothes.')
        print()
        return 1
    if missing or unrendered or ungrouped:
        return 1

    # ---- PLACEMENT, r7457.  Currency above; which BLOCK the prose is in, here. ----
    every = all_register_rows(reg)
    struck_with_runway = [p for p in blocks if p in every and p not in rows]
    misplaced = placement(blocks, set(rows), every)
    live_ct = len(misplaced)
    misplaced = [t for t in misplaced if t[0] not in PLACEMENT_BASELINE]
    print(f'  PLACEMENT -- {len(struck_with_runway)} struck row(s) carry a runway; a closed '
          f'row\'s digest must cite nothing newer than its own row')
    for pid, why in sorted(PLACEMENT_BASELINE.items()):
        if pid in blocks:
            print(f'    BASELINED {pid}: {why.splitlines()[0][:96]}...')
    if misplaced:
        print(f'  ⛔ {len(misplaced)} MISPLACED RUNWAY TEXT -- prose newer than the closed row '
              f'it sits under:')
        for pid, v, r in misplaced:
            print(f'    [FAIL] {pid}\'s block cites r{v} while its struck row ends at r{r} '
                  f'(ahead by {v - r})')
        print('     ⌗ READ THE BLOCK BEFORE MOVING ANYTHING.  The likely cause is text')
        print('       appended to the wrong block: `runway_blocks` ends a block at a')
        print('       lookahead for the next dict KEY, and PO-78\'s key is at column 0')
        print('       where every other key is indented four.  THE BLOCK THAT RECEIVES')
        print('       the text is the one BEFORE the next key, not the one named by it:')
        print('       r7453 called PO-75\'s block PO-79\'s for three restatements.')
        print('       If the prose is correct')
        print('       digest for this row, baseline it WITH THE READING, never bare.')
        print()
        return 1

    print(f'  {len(rows)} live row(s); every runway is at or ahead of its row.')
    print(f'  {len(struck_with_runway)} struck row(s) checked for placement; '
          f'{live_ct} site(s) over, {len(PLACEMENT_BASELINE)} baselined and read.')
    print('  ⌗ Currency is what is checkable here.  The runway is a DIGEST and cannot be')
    print('    generated -- which is why it drifted for ~2000 revisions unnoticed.')
    print('  ⌗ And placement is checkable only because the register is the authority for')
    print('    which revisions belong to which row.  A gate carrying its own copy of that')
    print('    mapping would be the copied-list defect wearing this gate\'s clothes.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
