#!/usr/bin/env python3
"""check_exact_counts.py -- AN EXACT COUNT ASSERTED AGAINST A SET ANOTHER SEAT CAN MOVE IS ADJUDICATED OR IT FAILS.

** WHAT THE CLASS IS. **  A claim of the form `count(...) == n` where what is counted is LIVE and SHARED -- a ledger,
a register, another receipt's source, a filesystem enumeration -- so that any seat's legitimate edit to that set
turns the claim red without the claim having become false.  *`r7198` gated the quote-pin backlog at exactly `2170`,
`r7204` read part of it, the backlog fell, and the equality went false: the work the gate watched succeeded and the
gate called it a failure.  `r7227` then turned three more of 60's receipts red on an exact `2167`.*

** THE DETECTOR IS 60's AND THIS GATE DOES NOT RE-TYPE IT. **  `detect`, `grounds_of`, `ground` and `in_claim` are
lifted from `S10`'s own source at import, as `S11` lifts them, so a repair there reaches here and the two cannot
drift.  All three of `S10`'s repairs are on: taint through a function boundary, a count bound to a name, and taint
onto a loop target.  Stage two partitions each claim-site:
    FROZEN       the counted set is read at a pinned SHA -- nobody can move it
    SELF         the counted set is declared in the receipt itself
    ROW-SCOPED   `== 1` -- a uniqueness claim about one row, not a size
    EXPOSED      none of the above: another seat's edit can move the count
** Only EXPOSED is the class.  Every EXPOSED site must carry a verdict in `exact_count_baseline.tsv`. **

⛭ ** WHY A STANDING GATE AND NOT A SWEEP -- 60's `r7242`. **  *A self-including sweep covers only the sites the
sweeping revision itself writes; its retrospective coverage was measured at exactly zero.*  ⇒ ** So this gate walks
EVERY receipt in the working tree on every run, untracked ones included -- a check that cannot see the state it is
run in is the `S11` defect -- and the sites already standing are covered here or nowhere. **

⚠ ** BLIND, AS 60 STATED FOR THE DETECTOR: ** *a count that reaches the comparison only through a subprocess's
output, with no shared path or enumerator in the receipt's source, is not tainted and is not seen.  The coverage of
this gate is set by the detector, not by its scope.*

The same three checks as the pin gates, keyed on (receipt, the comparison's source text) so an edit above the
site does not stale the entry:
  ⓵ every EXPOSED site is in the baseline -- a NEW one is a `[FAIL]`;
  ⓶ every baseline key still fires -- a `[STALE]` entry describes nothing and is removed;
  ⓷ the UNADJUDICATED count may only FALL, against the ceiling declared HERE.
Seeded both ways on every run (`_SEEDS`): sources that must fire and sources that must not.

    python3 corpus/check_exact_counts.py
    python3 corpus/check_exact_counts.py --list     # every EXPOSED site with its verdict

Written r7241+70.1 (node 70) on 66's r7241 order and 60's detector (r7240/r7242).  Stated for reversal.
"""
import ast
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'exact_count_baseline.tsv')
UNREAD = 'UNADJUDICATED'
UNREAD_CEILING = 21          # r7245+70.1: 24 counted at r7241+70.1, three read at r7245+70.1 (two DELIBERATE, one GENUINE-OWED) -- only falls


def _lift():
    """60's detector, out of `S10`'s source -- never re-typed here."""
    files = subprocess.run(['git', 'ls-files', 'receipts/L_probability/'], cwd=ROOT, capture_output=True,
                           text=True).stdout.split('\n')
    rel = [p for p in files if os.path.basename(p).startswith('S10_')][0]
    tree = ast.parse(open(os.path.join(ROOT, rel), encoding='utf-8').read())
    keep = {'detect', 'grounds_of', 'ground', 'in_claim', '_tg', '_reaches'}
    body = [n for n in tree.body
            if (isinstance(n, ast.Assign) and any(getattr(x, 'id', '') in ('SHARED', 'ENUM', 'CNT', 'PINLIKE')
                                                  for x in n.targets))
            or (isinstance(n, ast.FunctionDef) and n.name in keep)]
    ns = {'ast': ast, 're': re, 'os': os}
    exec(compile(ast.Module(body=body, type_ignores=[]), '<S10>', 'exec'), ns)
    return ns['detect'], ns['grounds_of'], ns['ground'], ns['in_claim'], tuple(ns['SHARED']) + tuple(ns['ENUM'])


detect, grounds_of, ground, in_claim, _SHARED_TOKENS = _lift()


def _segment(src, tree, line, col):
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare) and node.lineno == line and node.col_offset == col:
            return ' '.join((ast.get_source_segment(src, node) or '').split())
    return f'L{line}:{col}'


def sites_of(src):
    """every claim-site in one source, as (comparison text, partition, line)"""
    hits = detect(src)
    if not hits:
        return []
    tree = ast.parse(src)
    cl, pre = in_claim(tree), grounds_of(src, tree)
    return [(_segment(src, tree, h[0], h[1]), ground(h, pre), h[0]) for h in hits if h[0] in cl]


def population():
    """every receipt in the WORKING TREE -- tracked and untracked together (`S11`'s repair)"""
    out = subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard', 'receipts/'],
                         cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
    return sorted(p for p in set(out) if p.endswith('.py') and os.path.exists(os.path.join(ROOT, p)))


def _could_taint(src):
    """** A SOUND PRE-FILTER, NOT A HEURISTIC. **  The detector's taint starts only from a SHARED artefact name or a
    filesystem enumerator appearing in the source (as a string, a name or an attribute), so a source carrying none of
    them can produce no site.  It cuts the sweep from ~83 s to a few seconds; `--full` runs without it and the two
    must agree, which r7241+70.1 measured."""
    return any(x in src for x in _SHARED_TOKENS)


def sweep(full=False):
    """{(receipt, comparison): (partition, line)} over the whole population, and the per-partition totals"""
    found, totals = {}, {}
    for rel in population():
        try:
            src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        except (OSError, UnicodeDecodeError):
            continue
        if not full and not _could_taint(src):
            continue
        for seg, part, line in sites_of(src):
            totals[part] = totals.get(part, 0) + 1
            found.setdefault((rel, seg), (part, line))
    return found, totals


# ============================================================ the seeds, both ways
#: ⌗ a plain read, not a comprehension: the detector's SELF test files ANY list comprehension as self-declared, so
#:   `rows = [l for l in open(shared)]` reads as SELF -- a limit of the detector measured at r7241+70.1 and routed.
_SHARED_READ = "rows = open('corpus/quote_pin_baseline.tsv').read().split('\\n')\n"
_SEEDS_FIRE = {
    # 60's one genuine site, in its original form: r7238's Ⓓ② counted a token in another receipt's LIVE source
    'r7238 Ⓓ② as it stood': ("import glob\n_s8src = open(glob.glob('receipts/L_probability/S8_*.py')[0]).read()\n"
                             "gate('the block pin is read twice', _s8src.count('BLOCK_PIN') == 2)\n"),
    'a count bound to a name, on a shared ledger': (_SHARED_READ + "n = len(rows)\ngate('the backlog', n == 2167)\n"),
}
_SEEDS_QUIET = {
    'a count over a list the receipt declares (SELF)': ("PROBE = ['a', 'b', 'c']\n"
                                                        "gate('three probes', len(PROBE) == 3)\n"),
    'the same ledger read at a pinned SHA (FROZEN)': ("import subprocess\nPIN = '9c06b92f'\n"
                                                      "rows = subprocess.run(['git', 'show', f'{PIN}:corpus/"
                                                      "quote_pin_baseline.tsv'], capture_output=True, text=True)"
                                                      ".stdout.split()\ngate('the backlog at the pin', "
                                                      "len(rows) == 2167)\n"),
    'a uniqueness claim (ROW-SCOPED)': (_SHARED_READ + "gate('one row', rows.count('x') == 1)\n"),
    'an if on a count is control flow, not a claim': (_SHARED_READ + "if len(rows) == 2167:\n    print('same')\n"),
}


def seeds_hold():
    bad = [k for k, s in _SEEDS_FIRE.items() if not any(p == 'EXPOSED' for _, p, _ in sites_of(s))]
    bad += [k for k, s in _SEEDS_QUIET.items() if any(p == 'EXPOSED' for _, p, _ in sites_of(s))]
    return bad


# ============================================================ the ledger
def read_baseline():
    rows, dups = {}, []
    if not os.path.exists(BASELINE):
        return rows, dups
    for ln in open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 3:
            if (p[0], p[1]) in rows:
                dups.append((p[0], p[1]))
            rows[(p[0], p[1])] = (p[2], p[3] if len(p) > 3 else '')
    return rows, dups


def main(argv):
    print()
    print('  EXACT-COUNT GATE -- is every exact count on a set another seat can move adjudicated?')
    print()
    bad = seeds_hold()
    if bad:
        print('  ⛔ the detector lost a seeded direction:')
        for k in bad:
            print(f'      {k}')
        return 1
    print(f'    seeds hold: {len(_SEEDS_FIRE)} must fire and do, {len(_SEEDS_QUIET)} must not and do not')
    base, dups = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1
    if dups:
        print(f'  ⛔ {len(dups)} baseline key(s) carry more than one row: {dups[:3]}')
        return 1
    found, totals = sweep(full='--full' in argv)
    exposed = {k: v for k, v in found.items() if v[0] == 'EXPOSED'}
    print(f'    {len(population())} receipts in the working tree; claim-sites by partition: {dict(sorted(totals.items()))}')
    print(f'    {len(exposed)} distinct EXPOSED (receipt, comparison) key(s); the baseline carries {len(base)}')
    verdicts = {}
    for v, _ in base.values():
        verdicts[v] = verdicts.get(v, 0) + 1
    print(f'    by verdict: {dict(sorted(verdicts.items()))}')
    if '--list' in argv:
        for (rel, seg), (part, line) in sorted(exposed.items()):
            print(f'      {base.get((rel, seg), ("(NEW)",))[0]:16s} {rel}:{line}  {seg[:90]}')
    rc = 0
    new = sorted(k for k in exposed if k not in base)
    stale = sorted(k for k in base if k not in exposed)
    if new:
        rc = 1
        print(f'  ⛔ {len(new)} NEW EXPOSED exact count(s) -- an equality on a set another seat can move:')
        for rel, seg in new:
            print(f'      [FAIL] {rel}:{exposed[(rel, seg)][1]}  {seg[:100]}')
        print('    ⇒ make the claim monotone (`<=`/`>=`) where the set only moves one way, read the set at a PIN,')
        print('      or adjudicate it in exact_count_baseline.tsv with what was read.')
    if stale:
        rc = 1
        print(f'  ⛔ {len(stale)} STALE baseline entr(y/ies) -- no longer an EXPOSED site, so remove the row:')
        for rel, seg in stale:
            print(f'      [STALE] {rel}  {seg[:100]}')
    unread = verdicts.get(UNREAD, 0)
    if UNREAD_CEILING is not None and unread > UNREAD_CEILING:
        rc = 1
        print(f'  ⛔ {unread} unadjudicated against a ceiling of {UNREAD_CEILING} -- the backlog only falls.')
    if rc == 0:
        print(f'    the ratchet holds: {unread} unadjudicated against a ceiling of {UNREAD_CEILING}')
        print('  every exposed exact count is accounted: no new site, no stale entry, and the backlog in the open.')
    print()
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
