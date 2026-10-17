#!/usr/bin/env python3
"""r7433 ② -- LOCATE every refusal site in each register instrument's own source, for adjudication.

** THE UNIT, from the order. ** *"A refusal site is countable: the `raise SystemExit`, the `exit 1`, the
explicit red branch."*  In this corpus's gates the explicit red branch is the place that sets the failure
state: a call to the gate's own `fail(...)`, an `rc = 1` / `bad += 1`, a `FAILED.append`, a `sys.exit(1)` or
a `raise SystemExit`.  Each DISTINCT such branch is one site, because each one is a refusal with its own
printed address -- which is what the grade is about.

** THIS SCRIPT LOCATES, IT DOES NOT COUNT. **  It prints every candidate with its line and text so the
count can be adjudicated by reading.  *A count produced by this script alone would be the scrape `r7425` ②
caught, one level up.*

** THE SOURCE PER ROW IS WRITTEN HERE BY HAND. **  Six of the 21 register rows are not gate scripts (two
`ROWS.tsv` columns, three data files, one sub-aspect), so the instrument whose refusals bear on that key is
named explicitly rather than inferred from the row's name.

    python3 sites.py            # every candidate, grouped by register row
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

#: register row -> (source path, note).  `None` means NO instrument refuses on this key, which is a reading
#:   and is recorded as such rather than as a zero nobody looked at.
ROWS = [
    ('check_prose_pins',                  'corpus/check_prose_pins.py', ''),
    ('check_quote_pins',                  'corpus/check_quote_pins.py', ''),
    ('check_open_references',             'corpus/check_open_references.py', ''),
    ('check_open_item_coherence',         'corpus/check_open_item_coherence.py', ''),
    ('check_exact_counts',                'corpus/check_exact_counts.py', 'three walked at r7429'),
    ('check_marker_transposition',        'corpus/check_marker_transposition.py', ''),
    ('check_tilt_pins',                   'corpus/check_tilt_pins.py', ''),
    ('check_paper_pins_present',          'corpus/check_paper_pins_present.py', ''),
    ('check_revision_collisions',         'corpus/check_revision_collisions.py', ''),
    ('check_cannot_fail',                 'corpus/check_cannot_fail.py', 'one walked at r7429'),
    ('check_unread_figure',               'corpus/check_unread_figure.py', ''),
    ('check_paper_pins_not_comment_only', 'corpus/check_paper_pins_not_comment_only.py', ''),
    ('check_figures_pinned',              'corpus/check_figures_pinned.py', ''),
    ('check_pin_board',                   'corpus/check_pin_board.py', ''),
    ('check_pins_adjudicated_on_mint',    'corpus/check_pins_adjudicated_on_mint.py', ''),
    ('ROWS.tsv : index',                  'corpus/check_formalisation_join.py',
     "60's join gate is the only instrument that refuses on a ROWS.tsv row"),
    ('ROWS.tsv : class',                  None,
     "no instrument refuses on register-row candidacy: r7421 (1) ruled the two populations unjoined"),
    ('corpus/quote_pin_mint_held.tsv',    'corpus/check_pins_adjudicated_on_mint.py',
     'the hold register is read by the mint gate; same source as its own row'),
    ('check_view_tables : the debt file',  'corpus/check_view_tables.py', 'hit at .57'),
    ('red_carry : the carry ledger',      'scripts/red_carry.py', ''),
    ('corpus/frontier_steps_history.tsv', None,
     'a generator input, not a gate: regen_frontier.py consumes it and emits no refusal keyed on it'),
]

PATTERNS = (
    (r'\bfail\s*\(',              'fail() call'),
    (r'\bFAILED\.append\b',       'FAILED.append'),
    (r'\brc\s*=\s*1\b',           'rc = 1'),
    (r'\bbad\s*(\+=\s*1|=\s*1)\b', 'bad += 1'),
    (r'\bsys\.exit\s*\(\s*1\s*\)', 'sys.exit(1)'),
    (r'\braise\s+SystemExit\b',   'raise SystemExit'),
    (r'\bexit\s*\(\s*1\s*\)',     'exit(1)'),
    (r'\breturn\s+1\b',           'return 1'),
    (r'\bok\s*=\s*False\b',       'ok = False'),
    #: ⛔ ADDED AFTER A MISS OF MY OWN: the first pass matched `bad += 1` and not `bad = True`, and
    #:   check_paper_pins_present sets the flag that way -- so that gate came back with ONE site when it has
    #:   more.  The miss is the same shape as the r7425 scrape: a locator trusted before it was tested.
    (r'\b(bad|failed|red|hard_fail|soft_rise)\s*=\s*True\b', 'flag = True'),
)


def candidates(path):
    src = open(os.path.join(ROOT, path), encoding='utf-8').read().split('\n')
    out = []
    for i, line in enumerate(src, 1):
        s = line.strip()
        if s.startswith('#') or s.startswith('*') or s.startswith('"'):
            continue
        for pat, name in PATTERNS:
            if re.search(pat, line):
                out.append((i, name, s[:120]))
                break
    return out


def main():
    print('=' * 104)
    print('  REFUSAL SITES, LOCATED FOR ADJUDICATION -- r7433 (2).  The count is NOT taken here.')
    print('=' * 104)
    for row, path, note in ROWS:
        print(f'\n  {row}')
        if path is None:
            print(f'      ** NO REFUSING INSTRUMENT ** -- {note}')
            continue
        print(f'      source: {path}{("  (" + note + ")") if note else ""}')
        cs = candidates(path)
        print(f'      candidate refusal sites: {len(cs)}')
        for ln, kind, txt in cs:
            print(f'        {ln:>5}  {kind:<16} {txt}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
