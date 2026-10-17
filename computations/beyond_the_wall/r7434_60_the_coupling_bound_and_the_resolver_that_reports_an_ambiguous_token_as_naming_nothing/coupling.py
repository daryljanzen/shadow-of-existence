#!/usr/bin/env python3
"""r7434 (60) -- THE COUPLING BOUND: how many pins have a SECOND container reachable by a path token,
and what `r7400`'s resolver does with a token that reaches several.

⛭ THE RESOLVER IS IMPORTED AND NOT REBUILT.  `r7400`'s `cost.py` says of itself: *"the module level is
CHEAP -- the ledger, the tree at FRAME, the resolver -- so a receipt can import it for the resolver and
the frame without running the sweep."*  This takes it at its word.  ⇒ *`r7428`'s lesson applied before
the fact: a seat that does not own a format must not carry a private reader of it, and the same holds
for a resolver this seat already wrote once.*

⛔⛭⛭⛭ AND THE THING WORTH MEASURING IS IN THE RESOLVER'S OWN CODE:

    if '/' in tok:
        hits = ...
        return (hits, 'PATH') if len(hits) == 1 else ([], '')     # <--

*** A `/`-BEARING TOKEN THAT RESOLVES TO SEVERAL CONTAINERS IS RETURNED AS RESOLVING TO NONE. ***  Not
as ambiguous, not as many -- as nothing, and indistinguishable at the call site from a token naming a
file that does not exist.
  ⇒ So the registered question has a THIRD answer the instrument cannot currently give: **a pin may have
    a second container and be reported as having none.**
  ⌗ This is `PO-78`'s family inside a resolver this seat wrote at `r7400`, which is why the arms measure
    the DROP and not only the coupling.

⚠ Everything is read at `r7400`'s `FRAME`, never live: mixing a live tree with a pinned ledger is the
provenance defect `r7406` was about.

    python3 -I coupling.py
"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
R7400 = os.path.join(os.path.dirname(HERE), 'r7400_60_the_container_from_the_keys_own_trace')
sys.path.insert(0, R7400)
import cost as C                                                     # noqa: E402  -- r7400's resolver


# ⛔ r7436 (r7433 ①): the private `ambiguity()` THIS FILE CARRIED IS DELETED.  It was six lines that
# re-applied the resolver's own rules in order to report what the resolver discarded -- the right probe
# when nothing else could ask the question, and **the same behaviour written twice**, which is the rule
# this revision's own finding earned:
#
#   ⚖ A PREDICTION AIMED AT AN IMPLEMENTATION RATHER THAN AT A BEHAVIOUR WILL MISS WHEREVER THE SAME
#     BEHAVIOUR IS WRITTEN TWICE.                            -- PO-78's twenty-first family, member ⒜
#
# `C.resolution` now answers it from the one place, and every figure below is read through that.  The
# translation is behaviour-preserving by construction: AMBIGUOUS carries the candidates the old copy
# counted, RESOLVED carries the paths it counted, and NONE / NOT-A-TOKEN carry the zero it returned.


def reached(receipt, token):
    """(n_containers, route, ambiguous) -- ONE CALL into the repaired resolver, replacing the private copy.
    `n` is how many the token actually reached, which is the question the old resolver could not be asked."""
    r = C.resolution(receipt, token)
    return len(r.candidates), r.how, r.state == C.AMBIGUOUS


def main():
    print('=' * 100)
    print('  r7434 -- THE COUPLING BOUND, AND WHAT THE RESOLVER DROPS')
    print(f'  read at r7400\'s FRAME {C.FRAME} ({C.FULL[:9]}), never live')
    print('=' * 100)

    rows = C.ledger()
    named, nrows = C.trace_names()
    print(f'\n  ⓪ THE POPULATION, from the instruments that own it')
    print(f'      baseline rows at the frame      : {len(rows)}')
    print(f'      wide-trace rows                 : {nrows}')
    print(f'      (receipt, literal) keys w/ names: {len(named)}')

    reach = Counter()          # how many distinct containers a key reaches
    route = Counter()          # what made it >= 2
    hows = Counter()
    dropped = []               # (receipt, token, n) -- `/` tokens C.resolve reports as nothing
    wide_amb = []              # bare basenames ambiguous repo-wide AND unresolvable by the receipt's dirs
    multi_tok, amb_tok, both = 0, 0, 0

    for (receipt, lit), toks in named.items():
        conts, hs = C.containers(receipt, toks)
        reach[min(len(conts), 3)] += 1
        for h in hs:
            hows[h] += 1
        # the two routes to a second container, counted APART and never summed
        per = {}
        for tk in sorted(toks):
            n, how, amb = reached(receipt, tk)
            if amb and how == 'PATH':
                dropped.append((receipt, tk, n))
            if amb and how == 'BASE':
                wide_amb.append((receipt, tk, n))
            if n:
                per[tk] = n
        many_tokens = len([t for t, n in per.items() if n]) >= 2
        one_ambiguous = any(n >= 2 for n in per.values())
        if len(conts) >= 2:
            if many_tokens and one_ambiguous:
                both += 1
            elif many_tokens:
                multi_tok += 1
            elif one_ambiguous:
                amb_tok += 1

    anyc = sum(v for k, v in reach.items() if k >= 1)
    two_plus = reach[2] + reach[3]
    print(f'\n  ⓵ ⒜ THE COUPLING BOUND')
    print(f'      keys reaching 0 containers      : {reach[0]}')
    print(f'      keys reaching exactly 1         : {reach[1]}')
    print(f'      keys reaching exactly 2         : {reach[2]}')
    print(f'      keys reaching 3 or more         : {reach[3]}')
    print(f'      ⇒ of the {anyc} keys that reach ANY container, {two_plus} reach a SECOND: '
          f'{100.0 * two_plus / max(anyc, 1):.1f} %')
    print(f'      routes the resolver used        : {dict(hows)}')

    print(f'\n  ⓶ ⒞ AND THE TWO ROUTES TO A SECOND CONTAINER, COUNTED APART AND NOT SUMMED')
    print(f'      several TOKENS, each naming one : {multi_tok}')
    print(f'      ONE token naming several        : {amb_tok}')
    print(f'      both                            : {both}')
    print(f'      ⌗ a receipt naming two files is coupled by its own TEXT; a receipt naming one basename')
    print(f'        that exists in two directories it binds is coupled by the CORPUS\'s shape.')

    print(f'\n  ⓷ ⛔ ⒝ THE SILENT DROP: `/` TOKENS THAT REACH SEVERAL AND ARE REPORTED AS REACHING NONE')
    print(f'      distinct (receipt, token) pairs : {len(dropped)}')
    if dropped:
        worst = sorted(dropped, key=lambda x: -x[2])[:5]
        for r, t, n in worst:
            print(f'        {n:3d} containers  token {t!r}')
            print(f'                       in {r.split("/")[-1][:62]}')
        print(f'      ⇒ ** each of these is a key whose trace names a real token reaching {worst[0][2]} '
              f'or fewer containers, and which `C.resolve` reports as naming NOTHING. **')
    else:
        print(f'      ⇒ ** ZERO. The branch is dead code on this population, which is a finding and the')
        print(f'        one I did not predict: the drop is real in the code and empty in the data. **')

    print(f'\n  ⓸ AND THE BARE-BASENAME SIBLING, which `C.resolve` ALSO reports as nothing when the')
    print(f'      receipt binds no directory holding it')
    print(f'      distinct (receipt, token) pairs : {len(wide_amb)}')
    if wide_amb:
        w = sorted(wide_amb, key=lambda x: -x[2])[0]
        print(f'        worst: {w[2]} containers for token {w[1]!r}')

    print(f'\n  ⓹ ⒟ THE ARCHETYPE, RE-DERIVED AND NOT INHERITED')
    ps, how = C.resolve(C.ARCHETYPE_RECEIPT, 'COMPARISON.tsv')
    n, _, _ = reached(C.ARCHETYPE_RECEIPT, 'COMPARISON.tsv')
    print(f'      `S17`\'s COMPARISON.tsv resolves to {len(ps)} container(s) by {how!r}, reaching {n}')
    ok = len(ps) == 1 and ps[0] == C.ARCHETYPE
    print(f'      {"✔" if ok else "⛔"} S60\'s archetype {"still resolves alone" if ok else "HAS MOVED"}'
          f' -- {ps[0] if ps else "(nothing)"}')
    print('\n' + '=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
