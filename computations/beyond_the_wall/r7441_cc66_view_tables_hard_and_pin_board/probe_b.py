#!/usr/bin/env python3
"""r7441 -- CAN check_pin_board's (b) FIRE ON ANY BASELINE?

(b) is `if total_board != total_base: rc = 1` (corpus/check_pin_board.py:228).  Both sides are
computed IN THE SAME RUN from the SAME baseline text:

    total_base  = sum(counts(baseline).values())
    fresh       = generate(baseline, claims, history)      # generate() calls counts(baseline) itself
    rows        = [x for x in fresh.split('\n') if x and not x.startswith('#')]
    total_board = sum(int(x.split('\t')[2]) for x in rows)

generate() emits exactly ONE row per key of counts(), with that key's count in field 2.  So the two
sums are the same sum unless a row is DROPPED by the `not x.startswith('#')` filter or MISREAD by
`split('\t')[2]`.  A row is dropped only if its receipt field starts with '#' -- and counts() skips
any baseline line starting with '#', so no key can.  This probe tries to break that anyway, on
baselines chosen to attack the filter and the field index.  It does NOT edit the instrument.
"""
import importlib.util, os, sys
spec = importlib.util.spec_from_file_location('pb', os.path.join('corpus', 'check_pin_board.py'))
pb = importlib.util.module_from_spec(spec); spec.loader.exec_module(pb)

U = sorted(pb.UNVERDICTED)
print(f'  UNVERDICTED verdicts that count: {U}')
print()

def row(receipt, verdict):
    return '\t'.join([receipt, 'k', 'span', 'q', 'why', verdict])

CASES = {
    'empty baseline': '',
    'comments only': '# a\n# b\n',
    'one unverdicted key': row('receipts/A/x.py', U[0]),
    'two receipts, three keys': '\n'.join([row('receipts/A/x.py', U[0]),
                                           row('receipts/A/x.py', U[0]),
                                           row('receipts/B/y.py', U[0])]),
    'a receipt field that STARTS WITH #': row('#receipts/A/x.py', U[0]),
    'a receipt field that CONTAINS #': row('receipts/A/#x.py', U[0]),
    'an EMPTY receipt field': row('', U[0]),
    'a receipt field of only spaces': row('   ', U[0]),
    'trailing blank lines + CRLF': row('receipts/A/x.py', U[0]) + '\r\n\n\n',
    'a 6-field row exactly': 'receipts/A/x.py\tk\ts\tq\tw\t' + U[0],
    'a 5-field row (too short to count)': 'receipts/A/x.py\tk\ts\tq\tw',
    'a verdicted row (must not count)': row('receipts/A/x.py', 'DELIBERATE'),
    'every UNVERDICTED verdict at once': '\n'.join(row(f'receipts/A/r{i}.py', v)
                                                   for i, v in enumerate(U)),
    'one receipt, 250 keys': '\n'.join(row('receipts/A/x.py', U[0]) for _ in range(250)),
}
if len(U) > 1:
    CASES['mixed verdicted and not'] = '\n'.join([row('receipts/A/x.py', U[0]),
                                                  row('receipts/A/x.py', 'DELIBERATE'),
                                                  row('receipts/A/x.py', U[1])])

CLAIMS = 'receipts/A\tcc66\tCLAIM\tr7000\tprobe\n'
bad = 0
for name, bl in CASES.items():
    base = sum(pb.counts(bl).values())
    fresh = pb.generate(bl, CLAIMS, {})
    rows = [x for x in fresh.split('\n') if x and not x.startswith('#')]
    board = sum(int(x.split('\t')[2]) for x in rows)
    fires = board != base
    if fires:
        bad += 1
    print(f'    {"(b) FIRES" if fires else "equal    "}  board {board:>4}  ratchet {base:>4}  '
          f'rows {len(rows):>4}  -- {name}')
print()
print(f'  {len(CASES)} baseline(s) tried, {bad} made (b) fire.')
print('  ⌗ This is NOT a claim that the check is wrong -- it is a measurement of WHAT CAN REACH IT.')
print('    (b) compares a sum against itself: generate() emits one row per counts() key carrying')
print('    that key\'s own count, and counts() cannot produce a key starting with "#" because it')
print('    skips any baseline line that starts with one.  The branch is reachable only by editing')
print('    generate() or counts() -- the instrument\'s own control -- which is SELF-REFERENTIAL by')
print('    r7437 ④, not reachable by data.')
print()
print('  ⛭ AND THE SOURCE SAYS SO ITSELF, in the docstring of check (b):')
print('      "the board\'s unverdicted total EQUALS the baseline\'s -- a seeded property of')
print('       `generate`, checked on the board this gate generates.  (Its staleness half went')
print('       with the committed copy at r7257+70.1.)"')
print('    The half that could differ was the COMMITTED board going stale.  r7257+70.1 deleted the')
print('    committed copy and made the gate generate the board every run -- which removed the only')
print('    way the two numbers could ever disagree.  The seeded property is checked at line 199,')
print('    inside _seeds(); line 228 re-checks it on data that cannot differ.')
sys.exit(1 if bad else 0)
