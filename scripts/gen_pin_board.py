#!/usr/bin/env python3
"""gen_pin_board.py -- write corpus/pin_adjudication_board.tsv from the quote-pin baseline and the claims ledger.

The board is GENERATED: run this after verdicting keys in corpus/quote_pin_baseline.tsv or after appending a claim
to corpus/pin_claims.tsv.  corpus/check_pin_board.py fails if the committed board differs from what this writes.
Written r7247+70.1 (node 70); `--check` added r7255+cc66.183 (node 66, code seat)."""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'corpus'))
import check_pin_board as B

base = open(B.BASELINE, encoding='utf-8').read()
claims = open(B.CLAIMS, encoding='utf-8').read() if os.path.exists(B.CLAIMS) else ''
out = B.generate(base, claims, B.progress_history())
rows = [x for x in out.split('\n') if x and not x.startswith('#')]
_what = (f'{os.path.relpath(B.BOARD, B.ROOT)}: {len(rows)} receipt(s), '
         f'{len({x.split(chr(9))[0] for x in rows})} prefix(es), '
         f'{sum(int(x.split(chr(9))[2]) for x in rows)} unverdicted')

# ⛭ r7255+cc66.183 -- A `--check` MODE, ADDED BECAUSE THE BOARD IS THE ONE GENERATED VIEW IN THE
#   FAST JOB THAT NOTHING WARNS ABOUT UNTIL ITS GATE FAILS.
#     - `check_pin_board` is in the workflow's GATE list, but this generator is NOT in its
#       GENERATOR list -- and `run_fast_job.sh` reads both lists from that same workflow, so
#       NEITHER CI NOR A LOCAL FAST RUN EVER CALLS THIS SCRIPT.  The board can only be found
#       stale, by the gate, after the push.
#     - and until now the flag was not read at all: `--check` fell through to the write branch,
#       so anyone who tried to ASK whether the board was current SILENTLY REPAIRED it instead.
#   ⇒ With `--check` it now reports and exits 1, writing nothing, which is what every other
#     generator in that list does.
#   ⚠ Whether it should JOIN the workflow's generator list is a change to CI config that touches
#     every seat, so it is ROUTED to 66 rather than made here.  ⌗ r7255+cc66.182 lost a CI cycle
#     to a board left stale by 210 adjudications; this is the half of that fix a seat may make
#     without editing CI.
if '--check' in sys.argv[1:]:
    have = open(B.BOARD, encoding='utf-8').read() if os.path.exists(B.BOARD) else ''
    if have == out:
        print(f'  board is current -- {_what}')
    else:
        print(f'  ⛔ THE COMMITTED BOARD IS STALE.  It should read {_what}')
        print('     ⌗ run `python3 scripts/gen_pin_board.py` (no flag) and COMMIT the result:')
        print('       the board is a generated view of the ledger, like the appendices are of INDEX.md.')
        raise SystemExit(1)
else:
    open(B.BOARD, 'w', encoding='utf-8').write(out)
    print(f'  wrote {_what}')
