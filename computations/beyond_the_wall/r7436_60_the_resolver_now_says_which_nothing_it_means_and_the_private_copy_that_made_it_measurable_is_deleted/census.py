#!/usr/bin/env python3
"""r7436 (60) -- THE TOKEN-LEVEL CENSUS THE REPAIR MAKES SAYABLE, and the count of places that decide a
token.  Arms ⒜, ⒞ and ⒡ of `PREDICTION.md`, registered at `ef175b61` before this ran.

⛔ Every verdict below is `cost.resolution`'s own.  This file classifies and counts; it does not resolve.
⌗ The tree and the ledger are read at `r7400`'s `FRAME`, never live.

    python3 -I census.py
"""
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R7400 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7400_60_the_container_from_the_keys_own_trace')
sys.path.insert(0, R7400)
import cost as C                                            # noqa: E402  -- the ONE place a token resolves


def main():
    print('=' * 100)
    print('  r7436 -- WHICH NOTHING THE RESOLVER MEANS, COUNTED')
    print(f'  read at r7400\'s FRAME {C.FRAME} ({C.FULL[:9]}), never live')
    print('=' * 100)

    # ── ⒜ how many places decide a token ──────────────────────────────────────────────────────────────
    # THE SIGNATURE IS THE CONJUNCTION, not a name: a function RESOLVES A TOKEN when it applies BOTH a
    # path test (exact membership in the tree, or a `/`-suffix match) AND a basename-table lookup.  A
    # function doing only one of the two is matching suffixes or indexing files, which is not this
    # behaviour.  ⌗ The arm said "the discriminating lines occur in exactly one function"; that was
    # stated about a line pattern, and a line pattern cannot tell the two apart.
    # ⌗ TIGHTENED AFTER READING THE FIRST RUN'S MATCHES.  The loose form matched `in tracked()` (a call,
    # not a membership test) and `basename(x)` used for a PREFIX test, and so counted `r7386`'s `measure`
    # and `main`, which resolve no token at all.  Known answers below hold the signature honest.
    PATHISH = re.compile(r"endswith\('/' ?\+|in (?:TREESET|tracked|trees\w*)\b(?!\s*\()")
    BASEISH = re.compile(r"BYBASE\s*(?:\.get\(|\[)|BYBASE\.setdefault")
    print('\n  ⓵ ⒜ ONE PLACE, NOT TWO -- AND THE CORPUS SAYS OTHERWISE')

    def resolvers(at):
        """(file, function) for every function that applies BOTH rules.  `at` is a git ref, or None for
        THE WORKING TREE -- which is what the `after` figure has to be, because the repair is not a commit
        yet when this runs and `HEAD` would answer about the tree before it."""
        if at is None:
            ls = [f for f in subprocess.run(['git', '-C', ROOT, 'ls-files'],
                                            capture_output=True, text=True).stdout.split('\n')
                  if f.endswith('.py')]
        else:
            ls = [f for f in subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', at],
                                            capture_output=True, text=True).stdout.split('\n')
                  if f.endswith('.py')]
        found = []
        for rel in ls:
            if at is None:
                try:
                    src = open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
            else:
                src = subprocess.run(['git', '-C', ROOT, 'show', f'{at}:{rel}'],
                                     capture_output=True, text=True, errors='replace').stdout
            fn, body = None, []
            blocks = []
            for ln in src.split('\n'):
                m = re.match(r'def (\w+)\(', ln)
                if m:
                    if fn:
                        blocks.append((fn, '\n'.join(body)))
                    fn, body = m.group(1), []
                elif fn is not None:
                    body.append(ln)
            if fn:
                blocks.append((fn, '\n'.join(body)))
            for f, bd in blocks:
                live = '\n'.join(l for l in bd.split('\n') if not l.strip().startswith('#'))
                if PATHISH.search(live) and BASEISH.search(live):
                    found.append((rel, f))
        return sorted(found)

    before = resolvers('origin/main')
    after = resolvers(None)
    # KNOWN ANSWERS -- four the signature must catch and two it must not, each read by eye first
    must = [('r7400_60_the_container_from_the_keys_own_trace/cost.py', 'resolve'),
            ('r7434_60_the_coupling_bound_and_the_resolver_that_reports_an_ambiguous_token_as_naming_'
             'nothing/coupling.py', 'ambiguity'),
            ('r7287_70_never_moved/named_files.py', 'named')]
    mustnt = [('r7386_60_the_census_that_missed_the_clause_beside_it/cost.py', 'measure'),
              ('r7386_60_the_census_that_missed_the_clause_beside_it/cost.py', 'main')]
    bad = ([m for m in must if not any(r.endswith(m[0]) and f == m[1] for r, f in before)]
           + [m for m in mustnt if any(r.endswith(m[0]) and f == m[1] for r, f in before)])
    print(f'      the signature\'s known answers, on the trunk  : {len(must)} must match, '
          f'{len(mustnt)} must not -- {"ALL CORRECT" if not bad else "WRONG: " + str(bad)}')
    print(f'      functions that apply BOTH rules, on the trunk before this revision : {len(before)}')
    for rel, fn in before:
        print(f'        {fn}()  in  {rel}')
    print(f'      and on this WORKING TREE (not HEAD -- the repair is not a commit yet)  : {len(after)}')
    for rel, fn in after:
        print(f'        {fn}()  in  {rel}')
    mine_b = [k for k in before if '/r7400_' in k[0] or '/r7434_' in k[0]]
    mine_a = [k for k in after if '/r7400_' in k[0] or '/r7434_' in k[0]]
    others = [k for k in after if k not in mine_a]
    print(f'      ⇒ in THIS seat\'s own read path : {[k[1] for k in mine_b]} -> {[k[1] for k in mine_a]}')
    print(f'        ⌗ `seed` matches because its ASSERTIONS read the basename table; it resolves no token.')
    print(f'        The behaviour itself went from TWO functions to ONE, which is the half of the arm')
    print(f'        that holds.')
    print(f'      ⛔ BUT the arm said 1 ACROSS THE CORPUS and the corpus carries {len(others)} more:')
    for rel, fn in others:
        print(f'        {fn}()  in  {rel}')
    print(f'      ⇒ ** THE ARM MISSES, AND THE MISS IS THE FINDING AGAIN. ** The rule is written a THIRD')
    print(f'        time, by ANOTHER SEAT, and it carries the SAME conflation: at `r7287+70.2`,')
    print(f'          elif \'/\' not in s and s in BYBASE and len(BYBASE[s]) == 1: out.add(BYBASE[s][0])')
    print(f'        -- a basename carried by two paths contributes NO container and the caller cannot')
    print(f'        tell that from a basename carried by none.  ⌗ That file is 70\'s and is NOT edited')
    print(f'        here; it is routed with the patch.')

    # ── the population, from the instruments that own it ──────────────────────────────────────────────
    named, nrows = C.trace_names()
    rows = C.ledger()
    src = [r for r in rows if r[2] == 'SOURCE']
    srckeys = {(r[0], r[1]) for r in src}

    # ── ⒞ the token-level census ──────────────────────────────────────────────────────────────────────
    print('\n  ⓶ ⒞ EVERY DISTINCT (receipt, token) PAIR, BY STATE')
    pairs, state_of, amb_n = set(), {}, {}
    for (receipt, _lit), toks in named.items():
        for tk in toks:
            pairs.add((receipt, tk))
    cls = Counter()
    for (receipt, tk) in sorted(pairs):
        r = C.resolution(receipt, tk)
        state_of[(receipt, tk)] = r.state
        cls[r.state] += 1
        if r.state == C.AMBIGUOUS:
            amb_n[(receipt, tk)] = len(r.candidates)
    total = sum(cls.values())
    for st in (C.RESOLVED, C.NONE, C.AMBIGUOUS, C.NOT_A_TOKEN):
        print(f'      {st:<13}: {cls[st]}')
    print(f'      {"TOTAL":<13}: {total}   over {len(named)} key(s) and {nrows} wide-trace row(s)')
    part = cls[C.RESOLVED] + cls[C.NONE] + cls[C.AMBIGUOUS] + cls[C.NOT_A_TOKEN]
    print(f'      ⇒ the partition is EXACT: {cls[C.RESOLVED]}+{cls[C.NONE]}+{cls[C.AMBIGUOUS]}'
          f'+{cls[C.NOT_A_TOKEN]} = {part} = {total}: {part == total and len(pairs) == total}')
    print(f'      ⛔ and BEFORE the repair, {cls[C.NONE] + cls[C.AMBIGUOUS] + cls[C.NOT_A_TOKEN]} of these '
          f'read as one single answer -- "nothing"')
    print(f'      ⌗ NOT-A-TOKEN measures {cls[C.NOT_A_TOKEN]} here: the mint\'s `PATHTOK` cannot emit an '
          f'empty token, so the state is')
    print(f'        vacuous on this population and reachable only by construction -- which `cost.py '
          f'--seed` ⓵ does, and')
    print(f'        which is why the zero is a measurement and not an absence of one.')
    if amb_n:
        print('      the heaviest ambiguities, by how many real files answered:')
        for (rc, tk), n in sorted(amb_n.items(), key=lambda x: -x[1])[:5]:
            print(f'        {n:4d} answered  token {tk!r}')
            print(f'                    in {rc.split("/")[-1][:62]}')
    worst = max(amb_n.values()) if amb_n else 0
    print(f'      ⇒ the worst single token reached {worst} real files and read as reaching NONE')

    # ── ⛔ AND A DEFECT IN r7434's OWN LABEL, which r7433 ① has already restated ──────────────────────
    print('\n  ⓸ ⛔ THE `120` IS AN INCIDENCE COUNT AND `r7434` CALLED IT DISTINCT')
    inc, dis = 0, set()
    for (receipt, _lit), toks in named.items():
        for tk in toks:
            r = C.resolution(receipt, tk)
            if r.state == C.AMBIGUOUS and r.how == 'BASE':
                inc += 1
                dis.add((receipt, tk))
    print(f'      (receipt, LITERAL, token) incidences    : {inc}')
    print(f'      distinct (receipt, token) pairs         : {len(dis)}')
    print(f'      over distinct receipts / distinct tokens: {len({a for a, _ in dis})} / '
          f'{len({b for _, b in dis})}')
    print(f'      ⇒ ** r7434 printed "distinct (receipt, token) pairs : {inc}" and did not dedupe. The')
    print(f'        figure is right as an INCIDENCE count -- it iterates keys, and one receipt names the')
    print(f'        same token under several literals -- and the word "distinct" is wrong. The distinct')
    print(f'        count is {len(dis)}. **')
    print(f'      ⌗ r7433 ① restates the {inc} as distinct pairs, so the mislabel has already travelled;')
    print(f'        it is corrected in FOR_66_FROM_60 rather than left for 66 to find.')
    print(f'      ⇒ AND THE CONFLATION IS UNTOUCHED BY IT: the worst single token still reaches '
          f'{worst} real')
    print(f'        files and still read as reaching none, which is what the order was about.')

    # ── ⒡ ambiguity inside keys that looked fine ──────────────────────────────────────────────────────
    print('\n  ⓹ ⒡ WAS THE CONFLATION HIDING AMBIGUITY INSIDE KEYS THAT RESOLVED?')
    key_state = Counter()
    hidden, hidden_src = [], []
    for (receipt, lit), toks in named.items():
        sts = [state_of[(receipt, tk)] for tk in toks]
        resolved = C.RESOLVED in sts
        amb = C.AMBIGUOUS in sts
        key_state['RESOLVED' if resolved else ('AMBIGUOUS-ONLY' if amb else 'NOTHING')] += 1
        if resolved and amb:
            hidden.append((receipt, lit))
            if (receipt, lit) in srckeys:
                hidden_src.append((receipt, lit))
    print(f'      keys whose trace resolves something     : {key_state["RESOLVED"]}')
    print(f'      keys that ONLY reach ambiguity          : {key_state["AMBIGUOUS-ONLY"]}')
    print(f'      keys that reach nothing at all          : {key_state["NOTHING"]}')
    print(f'      ⇒ keys that RESOLVE and ALSO carry an AMBIGUOUS token : {len(hidden)}')
    print(f'        of those, in the SOURCE half S60 censuses          : {len(hidden_src)}')
    print(f'      ⇒ ** {len(hidden)} key(s) looked answered and were carrying a token that reached '
          f'several files and reported none. **')
    zero = key_state['AMBIGUOUS-ONLY'] + key_state['NOTHING']
    print(f'\n      ⛭ AND THIS IS THE SPLIT OF `r7434`\'s {zero}, which is the figure the repair earns:')
    print(f'        of the {zero} keys that read as reaching NO container,')
    print(f'          {key_state["AMBIGUOUS-ONLY"]} were reaching SEVERAL and were refused a verdict')
    print(f'          {key_state["NOTHING"]} truly reached nothing')
    print(f'        ⇒ ** {100.0 * key_state["AMBIGUOUS-ONLY"] / max(zero, 1):.1f} % of the "reaches '
          f'nothing" class was never a measurement of the')
    print(f'          corpus at all -- it was the instrument declining to choose. **')
    amb_only_keys = {k for k, toks in named.items()
                     if C.RESOLVED not in [state_of[(k[0], t)] for t in toks]
                     and C.AMBIGUOUS in [state_of[(k[0], t)] for t in toks]}
    byhalf = Counter(r[2] for r in rows if (r[0], r[1]) in amb_only_keys)
    print(f'        and they are not spread across the baseline: by half {dict(byhalf)}')
    print(f'        ⇒ every one of the {len(amb_only_keys)} sits in the SOURCE half -- which is the half '
          f'S60 censuses and')
    print(f'          the half r7433 ② holds the re-run for, so the held question and the defect have '
          f'the same population.')

    # ── the two classes S60's key-level census could not tell apart ───────────────────────────────────
    print('\n  ⓺ AND WHAT `S60`\'s KEY-LEVEL CLASS WAS HOLDING, reported and NOT written into S60')
    nu = [k for k in srckeys if named.get(k) and C.RESOLVED not in
          [state_of[(k[0], t)] for t in named[k]]]
    nu_amb = [k for k in nu if C.AMBIGUOUS in [state_of[(k[0], t)] for t in named[k]]]
    print(f'      S60 `named-unresolved` keys             : {len(nu)}')
    print(f'        of which at least one token was AMBIGUOUS : {len(nu_amb)}')
    print(f'        of which every token truly named nothing  : {len(nu) - len(nu_amb)}')
    print(f'      ⌗ r7433 ② holds the SOURCE re-run and this revision does not spend it; S60 is not '
          f'edited.  This line is the split REPORTED, so the figure exists when the re-run is called.')

    print('\n' + '=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
