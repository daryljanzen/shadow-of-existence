#!/usr/bin/env python3
"""check_quote_pins.py -- EVERY QUOTE-PIN SITE IS EITHER ADJUDICATED OR COUNTED, AND THE UNREAD COUNT ONLY FALLS.

** A DRAFT BY NODE 70 (r7125+70.1) FOR NODE 66 TO TAKE, REWRITE OR REFUSE. **  *It is written to run from
`corpus/` beside `quote_pin_baseline.tsv` as `check_prose_pins.py` does, and from this directory as it sits.  It is
NOT registered in `gates.yml`: registering a gate is the gate's call.*

** WHAT A QUOTE-PIN IS. **  An asserting test of a string literal's PRESENCE in text the receipt reads from a file
it does not own -- `'the sentence' in body15`, `re.search('...', body)`, `body.find('...') >= 0`.  *** The defect
is an assertion pinned to wording another seat owns: it fails when that seat rewords, and -- seven times in this
programme -- when the sentence said something was OPEN and the work it was watching succeeded and retired it. ***

** THE MEASUREMENT IS 70's AND THIS GATE DOES NOT REIMPLEMENT IT. **  It runs `scripts/mutate_assertions.py
--quote` as a subprocess and compares the sites against the adjudication baseline.  The same three checks as
`check_prose_pins`:
  ⓵ every reported (receipt, literal) is in the baseline -- a NEW quote-pin is a `[FAIL]`;
  ⓶ every baseline key is still reported -- a `[STALE]` entry describes nothing and is removed;
  ⓷ the UNADJUDICATED count may only FALL, against a ceiling declared HERE and nowhere else.

** THE KEY IS (receipt, literal), NOT A LINE. **  *A line-keyed baseline goes stale on any edit above the site.
The same literal tested twice in one receipt is one adjudication.  A reworded literal is a new key and is read
again -- which is the point: the rewording is exactly the event this class fails on.*

  python3 check_quote_pins.py
  python3 check_quote_pins.py --list        # the unadjudicated backlog, complete and unfiltered

Drafted r7125+70.1.  Stated for reversal.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, 'scripts', 'mutate_assertions.py')) and ROOT != os.path.dirname(ROOT):
    ROOT = os.path.dirname(ROOT)
BASELINE = os.path.join(HERE, 'quote_pin_baseline.tsv')
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')

LINE = re.compile(r'\s*\[QUOTE-PIN\]\[(PAPER|SOURCE)\]\[(SENTENCE|TOKEN)\]\[([A-Z,]*)\]\s+(\S+?):(\d+):(\d+)\s+(".*")$')
UNREAD = 'UNADJUDICATED'
# ⓷ the ratchet.  Seeded at r7125+70.1 as the count of distinct (receipt, literal) keys; lowering it is the point.
CEILING = 2287


def read_baseline():
    rows = {}
    if not os.path.exists(BASELINE):
        return rows
    for ln in open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 6:
            rows[(p[0], json.loads(p[1]))] = (p[2], p[3], p[4], p[5], p[6] if len(p) > 6 else '')
    return rows


def measure():
    r = subprocess.run([sys.executable, INSTRUMENT, '--quote'], cwd=ROOT, capture_output=True, text=True,
                       timeout=600)
    out = {}
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            target, tier, flags, path, _l, _c, lit = m.groups()
            key = (path, json.loads(lit))
            prev = out.get(key)
            # one key, several sites: ALT only if every site is ALT (the stricter reading wins)
            if prev is None or ('ALT' in prev[2] and 'ALT' not in flags):
                out[key] = (target, tier, flags)
    return out


def main():
    print()
    print('  QUOTE-PIN RATCHET -- is every pin on a sentence another seat owns adjudicated, or at least counted?')
    print()
    base = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1
    live = measure()
    print(f'    the instrument reports {len(live)} distinct (receipt, literal) key(s); the baseline carries {len(base)}')
    tally = {}
    for t, tier, flags in live.values():
        for k in [f'{t}/{tier}'] + [f'{t}/{f}' for f in flags.split(',') if f]:
            tally[k] = tally.get(k, 0) + 1
    print(f'    by target/tier and flag: {dict(sorted(tally.items()))}')
    verdicts = {}
    for _t, _ti, _f, v, _w in base.values():
        verdicts[v] = verdicts.get(v, 0) + 1
    print(f'    by verdict: {verdicts}')
    unread = verdicts.get(UNREAD, 0)
    print(f'    {UNREAD}: {unread}   ** the only bucket that means work, and it may only fall **')

    if '--list' in sys.argv:
        print()
        print(f'  THE BACKLOG, COMPLETE AND UNFILTERED -- {unread} key(s):')
        for (p, lit), (t, tier, flags, v, _w) in sorted(base.items()):
            if v == UNREAD:
                print(f'    [{t}/{tier}{"/" + flags if flags else ""}] {p}')
                print(f'               {json.dumps(lit, ensure_ascii=False)}')
        return 0

    bad = 0
    new = sorted(k for k in live if k not in base)
    if new:
        print()
        print(f'  ⛔ {len(new)} NEW QUOTE-PIN KEY(S) -- not in the baseline:')
        for p, lit in new[:40]:
            print(f'    [FAIL] {p}')
            print(f'           {json.dumps(lit, ensure_ascii=False)}')
        if len(new) > 40:
            print(f'    ... and {len(new) - 40} more')
        print('     ⌗ READ IT AND RECORD A VERDICT.  A gate that asserts another seat\'s sentence is present fails')
        print('       when that seat rewords -- and fails on SUCCESS when the sentence said something was open.')
        print('       If the claim is the sentence\'s MEANING, assert what the sentence is for; if both paper')
        print('       states are legitimate, test the disjunction (ALT); if the wording itself is the claim, say so')
        print('       in the baseline as DELIBERATE.')
        bad += 1
    else:
        print('    no new key: the class has not grown.')

    gone = sorted(k for k in base if k not in live)
    if gone:
        print()
        print(f'  ⛔ {len(gone)} STALE BASELINE ENTR(Y/IES) -- no longer reported, so the adjudication describes nothing:')
        for p, lit in gone[:40]:
            print(f'    [STALE] {p}')
            print(f'            {json.dumps(lit, ensure_ascii=False)}')
        if len(gone) > 40:
            print(f'    ... and {len(gone) - 40} more')
        bad += 1
    else:
        print('    no stale entry: every adjudication still describes a live key.')

    if unread > CEILING:
        print()
        print(f'  ⛔ THE UNADJUDICATED COUNT ROSE: {unread} against the declared ceiling {CEILING}.')
        bad += 1
    else:
        print(f'    the ratchet holds: {unread} unadjudicated against a ceiling of {CEILING}')

    print()
    if bad:
        print('  ⛔ THE QUOTE-PIN RATCHET IS RED.')
        return 1
    print('  the quote-pin class is fully accounted: no new key, no stale entry, and the backlog in the open.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
