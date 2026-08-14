#!/usr/bin/env python3
"""landing.py -- WHERE DOES THIS TURN LAND THE PROGRAMME?

** WHY.  Daryl, r2735: ** "*** every turn should well know where it lands the programme and what is
still outstanding work to be done ... What then becomes owed work or still todos sitting there newly
as a result.  What's the shape of the open region then as a result. ***"

** THE FAILURE THIS ANSWERS. **  *** r2733 stated a finding and stopped.  r2734 assessed it only
because Daryl asked -- and that assessment found the holonomy wall's stated reason was too narrow,
which the finding alone would never have surfaced.  ** A finding is not an assessment, and the gap
between them is where the programme's shape goes stale. ** ***

** THE FOUR QUESTIONS. **

      *** ① WHAT CHANGED         -- the finding, stated once
          ② WHAT IT TOUCHES      -- which OTHER rows it bears on: verdicts AND STATED REASONS
          ③ WHAT IS NEWLY OWED   -- work that did not exist before this turn and does now
          ④ THE SHAPE AFTER      -- what the open region looks like, not a count ***

  ⛭ ** ③ IS THE ONE WITH NO INSTRUMENT ANYWHERE IN THIS CORPUS. **  *** Every register here tracks
  work DISCHARGED -- the table, the ledger, the routed queue, the kill files.  **Nothing records work
  a turn CREATED.**  So newly-owed work has only ever existed in whatever the turn happened to say,
  and it evaporates at the next compaction. ***

** WHAT THIS DOES. **  Renders ②, ③ and ④ from the register and `OWED.md`, so the assessment is
composed against the actual state rather than from memory.

    python3 scripts/landing.py                 # render the current shape
    python3 scripts/landing.py --owe "text"    # record work this turn created

Written r2735.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')
OWED = os.path.join(ROOT, 'OWED.md')


def rows():
    out = []
    if not os.path.exists(REG):
        return out
    for l in open(REG, encoding='utf-8', errors='replace').read().split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+)\*\*', l)
        if not m:
            continue
        tail = l.split(' | ')[-1]
        out.append({
            'id': m.group(2),
            'struck': bool(m.group(1)),
            'answered': 'ANSWERED' in tail[:60].upper(),
            'gated': bool(re.search(r'gated on .?.?(PO-\d+|PO-seam)', l)),
            'gate': (re.search(r'gated on .?.?(PO-\d+|PO-seam)', l) or [None, ''])[1],
            'line': l,
        })
    return out


def owed_items():
    if not os.path.exists(OWED):
        return []
    return [l for l in open(OWED, encoding='utf-8', errors='replace').read().split('\n')
            if l.startswith('- [ ]')]


def discharge(needle, by):
    """mark an owed item DONE.  r2757 -- the half r2735 forgot to build.

    ** r2735 built `OWED.md` because "every register here counts things going away; nothing
    tracked work a turn PUT THERE."  *** And then built only the APPEND half.  `--owe` adds and
    nothing ever marks done, so the count grows monotonically BY CONSTRUCTION -- and "the owed
    list grew again" became a fact about the instrument rather than about the work. ***

      ⛭ ** The irony is exact: ** *** r2735 diagnosed the old registers as one-sided (discharge
      only) and built the mirror-image defect (creation only).  **A register needs BOTH halves or
      it is a monotone counter.** ***
    """
    if not os.path.exists(OWED):
        print('  no OWED.md')
        return
    lines = open(OWED, encoding='utf-8', errors='replace').read().split('\n')
    n = 0
    for i, l in enumerate(lines):
        if l.startswith('- [ ]') and needle.lower() in l.lower():
            lines[i] = l.replace('- [ ]', '- [x]', 1) + f'  -> DONE {by}'
            n += 1
    open(OWED, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f"  {n} item(s) discharged by {by}")


def record(text):
    rev = subprocess.run(['git', 'rev-list', '--count', 'HEAD'],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if not os.path.exists(OWED):
        open(OWED, 'w', encoding='utf-8').write(
            "---\nname: owed\nkind: STATE\ncurrent: r2735\n"
            "description: Work this programme's turns CREATED — the register every other register "
            "here lacks, since all of them track work discharged.\nsources: [chat]\n---\n\n"
            "# OWED — work a turn created\n\n"
            "> ⛭ *Daryl, r2735: \"what then becomes owed work or still todos sitting there newly as a\n"
            "> result.\" Every other register tracks work DISCHARGED. This one tracks what a finding\n"
            "> PUT THERE — and it is the half that evaporates at a compaction unless it is written.*\n\n")
    with open(OWED, 'a', encoding='utf-8') as f:
        f.write(f"- [ ] ({rev}) {text}\n")
    print(f"  recorded as owed at commit {rev}")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == '--owe':
        record(' '.join(sys.argv[2:]))
        return 0
    if len(sys.argv) > 3 and sys.argv[1] == '--done':
        discharge(sys.argv[2], sys.argv[3])
        return 0

    rs = rows()
    live = [r for r in rs if not r['struck'] and not r['answered']]
    gated = [r for r in live if r['gated']]
    free = [r for r in live if not r['gated']]

    print()
    print('  ⌗ THE SHAPE OF THE OPEN REGION')
    print()
    print(f'    WORKABLE NOW ({len(free)}):')
    for r in free:
        print(f'      {r["id"]}')
    print(f'    GATED ({len(gated)}):')
    for r in gated:
        print(f'      {r["id"]:<8}waits on {r["gate"]}')
    print()

    ow = owed_items()
    print(f'  ⌗ OWED — work this programme\'s turns CREATED ({len(ow)}):')
    if not ow:
        print('      (none recorded)')
    for l in ow:
        print(f'    {l[:100]}')
    print()
    print('  ⚠ ** This renders ② and ④.  ③ is only as good as what was RECORDED **')
    print('    -- run `landing.py --owe "..."` in the turn that creates the work,')
    print('    *** because a turn that names newly-owed work and does not file it has')
    print('    done the assessment and thrown it away. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
