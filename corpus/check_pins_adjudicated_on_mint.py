#!/usr/bin/env python3
"""check_pins_adjudicated_on_mint.py -- A RANGE THAT MINTS A QUOTE-PIN KEY ADJUDICATES IT IN THE SAME RANGE.

** r7275+70.1, on 66's r7271 ①. **  `check_pin_board` names the unverdicted class --
`UNADJUDICATED`, `UNADJUDICATED-LIST`, `UNADJUDICATED-PINNED` -- and reports it, and four seats have been clearing
it; NOTHING refused a commit that added one, so the ledger could be refilled behind them.  This gate refuses it.

** THE RULE, AND IT IS THE SHAPE THE MEASUREMENT LEFT STANDING
(computations/beyond_the_wall/r7275_70_mint_ratchet/). **  A key is MINTED when the range's tip carries a
`(receipt, literal)` row the range's base does not, with a verdict in the unverdicted class.  A minted key is
ALLOWED only when BOTH hold:
  * it is in a RESERVED class (`-PINNED`, `-LIST`) -- a declared hold, never the plain `UNADJUDICATED`; and
  * its RECEIPT is unchanged in the range -- the pin was already there and only the instrument now sees it.
Everything else is refused: a receipt added or edited in the range adjudicates its own pins in that range, which is
`69`'s recommendation and 66's standing rule.
  ⌗ *Measured over the last 200 first-parent commits on `main`: 47 touched the baseline; exactly ONE minted
    unverdicted keys -- 102 `UNADJUDICATED-PINNED` keys, in a merge that changed the INSTRUMENT and none of the 39
    receipts.  This rule allows it and refuses 0 of the 47, so it refuses no commit that cleared keys (66's
    wrong-shape negative does not fire) and stands well under the 10% too-strict line.*

** THE RANGE. **  On a branch: `merge-base(origin/main, HEAD)..HEAD`.  On `main` itself (HEAD is `origin/main`):
`HEAD^1..HEAD`, the last first-parent step, which for a merge is the whole merged branch.  `MINT_RANGE=a..b` overrides.
A shallow clone is REFUSED: on one commit there is no base to compare against.

    python3 corpus/check_pins_adjudicated_on_mint.py
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BASELINE = 'corpus/quote_pin_baseline.tsv'
UNVERDICTED = ('UNADJUDICATED', 'UNADJUDICATED-LIST', 'UNADJUDICATED-PINNED')   # check_pin_board's own tuple
RESERVED = ('UNADJUDICATED-LIST', 'UNADJUDICATED-PINNED')


def _git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace')


def rows(text):
    out = {}
    for ln in text.split('\n'):
        q = ln.split('\t')
        if len(q) >= 6 and not ln.startswith('#'):
            try:
                out[(q[0], json.loads(q[1]))] = q[5]
            except ValueError:
                pass
    return out


def refused(base_rows, tip_rows, changed):
    """[(receipt, literal, verdict, why)] for every key the range mints and may not"""
    out = []
    for k, v in sorted(tip_rows.items()):
        if v not in UNVERDICTED or k in base_rows:
            continue
        if v not in RESERVED:
            out.append((*k, v, 'the plain class is never a hold: adjudicate it'))
        elif k[0] in changed:
            out.append((*k, v, 'its receipt changed in this range, so the pin is new and is adjudicated here'))
    return out


def _seeds():
    """both directions, on built rows"""
    base = {('r/a.py', 'old'): 'DELIBERATE'}
    cases = [
        ('a new receipt mints a plain key', {('r/new.py', 'x'): 'UNADJUDICATED'}, {'r/new.py'}, True),
        ('an edited receipt mints a reserved key', {('r/a.py', 'y'): 'UNADJUDICATED-PINNED'}, {'r/a.py'}, True),
        ('an unchanged receipt mints a plain key', {('r/b.py', 'z'): 'UNADJUDICATED'}, set(), True),
        ('an unchanged receipt mints a reserved key (an instrument widening)',
         {('r/b.py', 'z'): 'UNADJUDICATED-PINNED'}, set(), False),
        ('a new receipt mints an ADJUDICATED key', {('r/new.py', 'x'): 'DELIBERATE'}, {'r/new.py'}, False),
    ]
    bad = []
    for label, add, changed, want in cases:
        got = bool(refused(base, {**base, **add}, changed))
        if got != want:
            bad.append(f'{label}: expected {"refused" if want else "allowed"}, got {"refused" if got else "allowed"}')
    return bad


def the_range():
    if os.environ.get('MINT_RANGE'):
        a, b = os.environ['MINT_RANGE'].split('..')
        return a, b
    head = _git('rev-parse', 'HEAD').stdout.strip()
    main = _git('rev-parse', '--verify', '--quiet', 'origin/main').stdout.strip()
    if main and head != main:
        mb = _git('merge-base', main, head).stdout.strip()
        if mb and mb != head:
            return mb, head
    return f'{head}^1', head


def main():
    print()
    print('  PINS ADJUDICATED ON MINT -- does this range add an unadjudicated quote-pin key it may not?')
    print()
    if _git('rev-parse', '--is-shallow-repository').stdout.strip() == 'true':
        print('  ⛔ a SHALLOW clone has no base to compare against.  Fetch full history (`fetch-depth: 0`).')
        return 1
    bad = _seeds()
    if bad:
        print('  ⛔ the seeds lost a direction:')
        for b in bad:
            print(f'      {b}')
        return 1
    print('    seeds hold: a plain mint and an edited receipt\'s mint are refused; an instrument widening\'s reserved'
          ' mint and an adjudicated mint are allowed')
    a, b = the_range()
    if _git('rev-parse', '--verify', '--quiet', f'{a}^{{commit}}').returncode != 0:
        print(f'    no base for the range ({a}): a root commit, nothing to compare')
        return 0
    base_rows = rows(_git('show', f'{a}:{BASELINE}').stdout)
    tip_rows = rows(_git('show', f'{b}:{BASELINE}').stdout)
    changed = set(_git('diff', '--name-only', a, b).stdout.split())
    out = refused(base_rows, tip_rows, changed)
    minted = sum(1 for k, v in tip_rows.items() if v in UNVERDICTED and k not in base_rows)
    print(f'    range {a[:10]}..{b[:10]}: {minted} unverdicted key(s) minted, {len(out)} refused')
    if out:
        print()
        for rc, lit, v, why in out[:40]:
            print(f'    [MINTED] {rc}  {json.dumps(lit, ensure_ascii=False)[:60]}  ({v}) -- {why}')
        if len(out) > 40:
            print(f'    ... and {len(out) - 40} more')
        print()
        print('  ⛔ A RANGE THAT MINTS A PIN LEAVES IT FOR SOMEONE ELSE TO CLEAR.')
        print('     Read each key and give it a verdict in `corpus/quote_pin_baseline.tsv` in this same range.')
        return 1
    print('  no unadjudicated key is minted that this range could have adjudicated.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
