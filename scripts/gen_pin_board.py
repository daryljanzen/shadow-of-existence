#!/usr/bin/env python3
"""gen_pin_board.py -- write corpus/pin_adjudication_board.tsv from the quote-pin baseline and the claims ledger.

The board is GENERATED: run this after verdicting keys in corpus/quote_pin_baseline.tsv or after appending a claim
to corpus/pin_claims.tsv.  corpus/check_pin_board.py fails if the committed board differs from what this writes.
Written r7247+70.1 (node 70)."""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'corpus'))
import check_pin_board as B

base = open(B.BASELINE, encoding='utf-8').read()
claims = open(B.CLAIMS, encoding='utf-8').read() if os.path.exists(B.CLAIMS) else ''
out = B.generate(base, claims, B.progress_history())
open(B.BOARD, 'w', encoding='utf-8').write(out)
rows = [x for x in out.split('\n') if x and not x.startswith('#')]
print(f'  wrote {os.path.relpath(B.BOARD, B.ROOT)}: {len(rows)} receipt(s), '
      f'{len({x.split(chr(9))[0] for x in rows})} prefix(es), {sum(int(x.split(chr(9))[2]) for x in rows)} unverdicted')
