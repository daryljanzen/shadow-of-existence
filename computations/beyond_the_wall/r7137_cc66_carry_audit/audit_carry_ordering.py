#!/usr/bin/env python3
"""r7137+cc66.105 -- DOES THE CARRY LEDGER'S OWN RULE "red wins" HOLD IN BOTH ORDERINGS?

`red_carry.py` states it in its concurrency note: *"Two jobs disagreeing about one receipt: red
wins."*  It holds when the ancestor's run is the RED one -- that run re-applies its own delta and the
red survives a descendant's green, which is what `cc66.101` reported as a defect and is in fact the
specification.  ** It does NOT hold in the other ordering: ** an ancestor run that PASSES writes
`del cur[rec]` (`apply()`, the `elif rec in cur` branch) and re-applies that clear on a refused push,
so an ancestor's green removes a red a DESCENDANT recorded.

** WHAT THIS MEASURES, from `refs/ci/carry`'s own history and nothing else. **
  (1) out-of-order writes  -- a write whose head sha is an ANCESTOR of a sha already written for the
      same (branch, class) EARLIER IN WALL CLOCK;
  (2) of those, which cleared and which only re-added;
  (3) reds ACTUALLY lost -- an ancestor's clear naming a receipt a descendant's write had marked red;
  (4) of those, which were re-recorded later and which never were.

⌗ ** A LIMIT, because the ledger cannot settle it: ** "never re-recorded" does not separate *passed
  when next covered* from *never covered again*.  The ledger records DELTAS, not coverage.  So the
  final count is reds the layer stopped chasing, not defects that went unseen.

Run from the repository root with `refs/ci/carry` fetched, e.g.
    git fetch origin '+refs/ci/carry:refs/ci-remote/carry' --force
    python3 computations/beyond_the_wall/r7137_cc66_carry_audit/audit_carry_ordering.py
"""
import collections
import re
import subprocess
import sys

REF = sys.argv[1] if len(sys.argv) > 1 else 'refs/ci-remote/carry'
SUBJ = re.compile(r'^(\w+) @ (\S+) ([0-9a-f]{10}): \+(\d+) -(\d+) =(\d+)$')


def writes(ref):
    """every ledger commit, oldest first, with the receipts its body names"""
    raw = subprocess.run(['git', 'log', '--format=%H|%ct|%s%n%b%n==END==', ref],
                         capture_output=True, text=True).stdout
    out = []
    for block in (b for b in raw.split('==END==') if b.strip()):
        lines = [l for l in block.strip().split('\n') if l.strip()]
        _, ts, subject = lines[0].split('|', 2)
        m = SUBJ.match(subject)
        if not m:
            continue
        cls, branch, sha, _a, _c, _k = m.groups()
        out.append(dict(ts=int(ts), cls=cls, br=branch, sha=sha,
                        added=[l[2:].strip() for l in lines[1:] if l.startswith('+ ')],
                        clr=[l[2:].strip() for l in lines[1:] if l.startswith('- ')],
                        rem=[l[2:].strip() for l in lines[1:] if l.startswith('x ')]))
    out.reverse()
    return out


_has, _anc = {}, {}


def exists(sha):
    if sha not in _has:
        _has[sha] = subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'],
                                   capture_output=True).returncode == 0
    return _has[sha]


def is_ancestor(a, b):
    if (a, b) not in _anc:
        _anc[(a, b)] = subprocess.run(['git', 'merge-base', '--is-ancestor', a, b],
                                      capture_output=True).returncode == 0
    return _anc[(a, b)]


def main():
    ev = writes(REF)
    if not ev:
        raise SystemExit(f'  no parsable ledger commits at {REF} -- fetch refs/ci/carry first')

    # (1) and (2): ordering, from ancestry against wall clock
    seen = collections.defaultdict(list)
    out_of_order, missing = [], 0
    for e in ev:
        key = (e['br'], e['cls'])
        if not exists(e['sha']):
            missing += 1
            seen[key].append(e)
            continue
        for prior in seen[key]:
            if not exists(prior['sha']) or prior['sha'] == e['sha']:
                continue
            if is_ancestor(e['sha'], prior['sha']):
                out_of_order.append((e, prior))
                break
        seen[key].append(e)

    # (3) and (4): which clears actually removed a descendant's red, and which never came back
    red_by, lost = collections.defaultdict(dict), []
    for i, e in enumerate(ev):
        key = (e['br'], e['cls'])
        for rec in e['clr']:
            owner = red_by[key].get(rec)
            if (owner and owner != e['sha'] and exists(owner) and exists(e['sha'])
                    and is_ancestor(e['sha'], owner)):
                lost.append((i, e, rec, owner))
            red_by[key].pop(rec, None)
        for rec in e['added']:
            red_by[key][rec] = e['sha']
        for rec in e['rem']:
            red_by[key].pop(rec, None)
    never = [(e, rec) for i, e, rec, _o in lost
             if not any(rec in f['added'] for f in ev[i + 1:]
                        if f['br'] == e['br'] and f['cls'] == e['cls'])]

    cleared = [p for p in out_of_order if p[0]['clr']]
    readded = [p for p in out_of_order if p[0]['added'] and not p[0]['clr']]
    print()
    print("  CARRY-ORDERING AUDIT -- does \"red wins\" hold in BOTH orderings?")
    print()
    print(f'    ledger writes parsed                                  : {len(ev)}')
    print(f'    head shas no longer in the repository                 : {missing}')
    print(f'    OUT-OF-ORDER WRITES (ancestor wrote after descendant) : {len(out_of_order)}'
          f'  ({len(out_of_order) / len(ev) * 100:.1f}% of all writes)')
    print(f'       of those, writes that CLEARED (the losing direction): {len(cleared)}')
    print(f'       of those, writes that only re-added (as designed)   : {len(readded)}')
    print(f'    REDS ACTUALLY LOST                                    : {len(lost)}')
    print(f'       later re-recorded on the same branch               : {len(lost) - len(never)}')
    print(f'       NEVER re-recorded                                  : {len(never)}')
    print()
    by_branch = collections.Counter(e['br'].split('/')[-1] for _i, e, _r, _o in lost)
    print('    reds lost, by branch:')
    for b, n in by_branch.most_common():
        print(f'       {n:3d}  {b}')
    print()
    print('    never re-recorded:')
    for e, rec in never:
        print(f"       {e['cls']:9s} {e['br'].split('/')[-1][-12:]:12s} "
              f"{rec.split('/')[-1][:62]}   (cleared by ancestor {e['sha'][:8]})")
    print()
    print('  ⌗ THE LIMIT: "never re-recorded" does not separate *passed when next covered* from')
    print('    *never covered again* -- the ledger records deltas, not coverage.  So the last count is')
    print('    reds the layer stopped chasing, NOT defects that went unseen.')
    print()
    print('  ⌗ AND THE SCOPE OF THE HARM: the carry decides which receipts the NEXT run re-tests and')
    print('    nothing else.  It cannot retract a check-run conclusion and does not feed the fast job')
    print('    or a PR\'s own checks.  What this defect falsifies is one sentence of the layer\'s own')
    print('    docstring -- "no push that misses it can silence it: it is re-run until it finishes".')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
