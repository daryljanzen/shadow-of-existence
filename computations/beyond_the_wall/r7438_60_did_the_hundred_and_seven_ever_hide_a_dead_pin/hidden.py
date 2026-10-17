#!/usr/bin/env python3
"""r7438 (60) -- DID THE 107 EVER HIDE A DEAD PIN?  Six arms, registered in PREDICTION.md at `7b11b9df`
before this ran.  `r7435` ③ is the order; `r7433` ②'s hold is lifted because `r7436` discharged its reason.

⛔ THE PRESENCE TEST IS `check_quote_pins._present_at` ITSELF, reached through `cost.present_in`, CALLED AND
NOT REIMPLEMENTED -- only its file list is replaced, exactly as `r7400` and `S60` do it.  The containers come
from `cost.resolution`, which is the one place a token resolves.  Everything is read at `r7400`'s FRAME.

    python3 -I hidden.py
"""
import json
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R7400 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7400_60_the_container_from_the_keys_own_trace')
sys.path.insert(0, R7400)
import cost as C                                            # noqa: E402

# S60's own pinned figures, for the control -- named rather than remembered
S60_ABSENT, S60_RESOLVED, S60_GAP, S60_RATE = 112, 839, 94, 83.9
VIOLATOR = 'receipts/L165_interacting_tower/D1_the_boundary_is_per_fibre_and_the_UV_is_over_fibres.py'
VIOL_LIT = '1+\\lambda\\phi'
S60_VIOL_RW = False      # what S60's own run printed for this call -- a known answer, not a guess


def main():
    t0 = time.time()
    print('=' * 100)
    print('  r7438 -- DID THE 107 EVER HIDE A DEAD PIN?')
    print(f'  read at r7400\'s FRAME {C.FRAME} ({C.FULL[:9]}), never live')
    print('=' * 100)

    named, nsites = C.trace_names()
    rows = C.ledger()
    half = {(r[0], r[1]): r[2] for r in rows}
    verdict = {(r[0], r[1]): r[4] for r in rows}

    # ── ⒜ the population, re-derived ─────────────────────────────────────────────────────────────────
    print('\n  ⓵ ⒜ THE POPULATION, RE-DERIVED IN THIS RUN AND NOT INHERITED')
    hidden = {}            # key -> sorted candidates, over its AMBIGUOUS tokens
    for key, toks in named.items():
        res = {tk: C.resolution(key[0], tk) for tk in toks}
        if any(r.state == C.RESOLVED for r in res.values()):
            continue
        cands = sorted({p for r in res.values() if r.state == C.AMBIGUOUS for p in r.candidates})
        if cands:
            hidden[key] = cands
    byhalf = Counter(half.get(k, '?') for k in hidden)
    print(f'      keys reaching only ambiguity    : {len(hidden)}')
    print(f'      by half                         : {dict(byhalf)}')
    print(f'      distinct tokens behind them     : '
          f'{len({tk for k in hidden for tk in named[k] if C.resolution(k[0], tk).state == C.AMBIGUOUS})}')
    print(f'      distinct candidate containers   : {len({c for v in hidden.values() for c in v})}')
    print(f'      candidates per key, min/med/max : '
          f'{min(len(v) for v in hidden.values())}/'
          f'{sorted(len(v) for v in hidden.values())[len(hidden) // 2]}/'
          f'{max(len(v) for v in hidden.values())}')
    print(f'      ⇒ {len(hidden)} keys, all in {sorted(byhalf)} -- and the whole trace has '
          f'{nsites} site(s)')

    # ── ⒡ the control FIRST, because a measurement with an unverified instrument is worth nothing ────
    print('\n  ⓶ ⒡ THE CONTROL -- the instrument is unchanged, checked before the figure is read')
    selfcont = [(k[0], c) for k, v in hidden.items() for c in v if c == k[0]]
    print(f'      candidates that are their own receipt : {len(selfcont)}')
    rw = C.present_repo_wide(VIOL_LIT, VIOLATOR)
    print(f'      S60\'s named violator, re-tested repo-wide : {rw}  '
          f'-- S60\'s own run recorded {S60_VIOL_RW}: {"MATCH" if rw == S60_VIOL_RW else "⛔ MOVED"}')
    ok_ctl = not selfcont and rw == S60_VIOL_RW
    print(f'      ⇒ {"✔" if ok_ctl else "⛔"} `_present_at`\'s own rule -- text from a file the receipt '
          f'does not own -- holds over all {sum(len(v) for v in hidden.values())} candidate slots')

    # ── ⒝ / ⒞ the test ───────────────────────────────────────────────────────────────────────────────
    print('\n  ⓷ ⒝⒞ THE TEST: is the pinned literal in ANY file the token actually reached?')
    t1 = time.time()
    present, absent = [], []
    for key in sorted(hidden):
        receipt, lit = key
        (present if C.present_in(lit, receipt, hidden[key]) else absent).append(key)
    t_test = time.time() - t1
    print(f'      present in at least one candidate : {len(present)}')
    print(f'      ABSENT from every candidate       : {len(absent)}')
    print(f'      ⇒ of {len(hidden)}, {100.0 * len(absent) / max(len(hidden), 1):.1f} % are absent from '
          f'every file their own trace named')
    if absent:
        vb = dict(Counter(verdict.get(k, '?') for k in absent))
        print(f'      the absent ones by baseline verdict : {vb}')
        if set(vb) == {'DELIBERATE'}:
            print(f'      ⇒ ** ALL {len(absent)} ARE `DELIBERATE`, which the baseline defines as *the '
                  f'wording IS the claim*')
            print(f'        -- a name, a value or a label.  So the class the conflation hid is the class '
                  f'where')
            print(f'        the exact text is what is being asserted, and not the loosely quoted kind. **')

    # ── ⒟ of those absent, how many does the repo-wide branch call PRESENT ───────────────────────────
    print('\n  ⓸ ⒟ OF THOSE ABSENT, HOW MANY THE REPO-WIDE BRANCH CALLS PRESENT')
    gap = [k for k in absent if C.present_repo_wide(k[1], k[0])]
    frac = 100.0 * len(gap) / max(len(absent), 1)
    print(f'      absent from own containers, PRESENT repo-wide : {len(gap)} of {len(absent)} '
          f'= {frac:.1f} %')
    print(f'      S60\'s figure for the keys that DID resolve    : {S60_GAP} of {S60_ABSENT} '
          f'= {S60_RATE} %')
    print(f'      ⇒ the two sets differ by {abs(frac - S60_RATE):.1f} point(s)')

    # the caveat S60 established, carried rather than dropped
    exposed = [k for k in absent if '\\' in k[1]]
    print(f'      the caveat S60 established, CHECKED rather than recited:')
    print(f'        absent keys whose literal carries a backslash : {len(exposed)} of {len(absent)}')
    if exposed:
        print(f'        ⚠ S60 established the repo-wide branch builds its file list with the BACKSLASHES')
        print(f'          DELETED, so for those {len(exposed)} the {frac:.1f} % is read with a known defect')
        print(f'          in it; the one-line correction stays ROUTED and is not applied here.')
    else:
        print(f'        ✔ NONE -- so the mangled-needle defect S60 found cannot touch this figure, and')
        print(f'          {frac:.1f} % is read clean.  ⌗ The caveat is CHECKED and found not to apply,')
        print(f'          which is a different statement from not mentioning it.')

    # ── ⒠ the price ──────────────────────────────────────────────────────────────────────────────────
    total = time.time() - t0
    print('\n  ⓹ ⒠ THE PRICE, MACHINE-NAMED')
    print(f'      the presence test over {len(hidden)} keys : {t_test:.1f} s')
    print(f'      the whole run                             : {total:.1f} s')
    print(f'      S60\'s estimate for this question          : ~4200 s (roughly seventy minutes)')
    print(f'      ⇒ {total:.1f} s against ~4200 s estimated -- a factor of '
          f'{4200.0 / max(total, 0.1):.0f}')

    # ── the findings, written where the next reader will look ────────────────────────────────────────
    out = os.path.join(HERE, 'absent.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('# receipt\tliteral(json)\tverdict\tn_candidates\trepo_wide\n')
        for k in sorted(absent):
            fh.write('\t'.join((k[0], json.dumps(k[1]), verdict.get(k, '?'),
                                str(len(hidden[k])), 'PRESENT' if k in gap else 'ABSENT')) + '\n')
    print(f'\n  ⌗ the {len(absent)} absent keys are written to absent.tsv, keyed as the gate keys them')
    print('\n' + '=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
