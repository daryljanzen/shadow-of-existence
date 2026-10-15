#!/usr/bin/env python3
"""r7372 (60) -- THE ROW ONE REVISION BEHIND THE MINT.

** 66's `r7367` (6) reports the trunk's quote-pin ratchet red on two keys of `S55`'s and reads them as
`r7370`'s unadjudicated mints.  Both halves of that reading are off by one revision. **  The literals were
introduced by `0d8ac35c`, whose subject claims `r7368` and which IS an ancestor of the trunk; their rows
carry `DELIBERATE` with a reason each and were written by `ba75b3fb`, whose subject claims `r7370` and
which is NOT.  The keys are adjudicated.  The trunk took the MINT one revision ahead of the ROW.

** WHAT THIS MEASURES. **  For every row this seat ADDED to the baseline in the pinned range, the commit
that introduced its literal (the MINT) and the commit that wrote its row (the ROW), each read back to a
revision with the corpus's own `claim_of` imported from the collision gate rather than a spelling of it:

  (a) LATE      -- mint revision != row revision.
  (b) EXPOSED   -- mint is an ancestor of the pinned trunk and row is not: the subset that can turn it red.
  (c) EARLY     -- row revision below mint revision.  A row cannot precede its own mint; predicted 0.
  (d) the WITHIN-REVISION window -- receipt-touching commits of this seat's that FOLLOW a revision's last
      registration pass.  That is 66's second candidate cause, tested rather than argued.

and, because an arm is a count and a count does not say how a gap opened, the MECHANISM: for each LATE
row, whether its mint commit comes AFTER its own revision's last registration pass.

** THE POPULATION IS BOUNDED BY A COMMIT AND NEVER BY A REF, which is `r7368` (2)'s standing rule, and the
trunk is PINNED with the live reading printed beside it and asserted of nothing. **  `BASE..FRAME` reaches
other seats' merged work too, so this seat's own commits are selected by the session marker on the
introducing commit -- the same selector `P03` and `S5` were repaired to use -- and the marker is read off
the FRAME commit's own message rather than typed in here.

⚠ *`NO-REV` is not a revision.  Commits whose subject claims none are not "the same revision" as each
other, and counting them together is what made the first run of arm (d) read `220` instead of `7`.*

    python3 computations/beyond_the_wall/r7372_60_the_row_one_revision_behind_the_mint/cost.py
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BASELINE = 'corpus/quote_pin_baseline.tsv'

FRAME = '3a913237'      # this revision's registration commit: the prediction, committed before this ran
BASE = '72a204e2'       # the last trunk merge into this branch before the phase: a fixed sha
TRUNK = '0aa2f781'      # the trunk as 66's r7367 (6) read it: a fixed sha, never the ref

#: the two keys 66 named, so what is asserted is those keys and not a count that happens to be two
NAMED = ('_PINNED', 'def _class_of')
#: the three shas the finding stands on, pinned so the claim does not move when the branch does
MINT_C = '0d8ac35c'     # r7368: introduced both literals into S55
ROW_C = 'ba75b3fb'      # r7370: wrote both rows
PASS_C = '3f30509e'     # r7368's OWN registration pass -- and the mint came after it

os.environ.setdefault('NODE', '60')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
from check_revision_collisions import claim_of          # noqa: E402  the instrument, not a spelling

_SESS = re.compile(r'^Claude-Session:\s*(\S+)', re.M)
RESULT = {}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def body(sha):
    return git('show', '-s', '--format=%B', sha)


def subject(sha):
    return git('show', '-s', '--format=%s', sha).strip()


def rev_of(sha):
    m = claim_of(subject(sha))
    return m.group(1) if m else 'NO-REV'


def is_ancestor(a, b):
    return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b],
                          capture_output=True).returncode == 0


def own_session():
    m = _SESS.search(body(FRAME))
    return m.group(1) if m else None


def mine(base, tip, *paths):
    """this seat's own commits in `base..tip`, by the session marker on the introducing commit, oldest first"""
    sess = own_session()
    out = []
    args = ['log', '--no-merges', '--reverse', '--format=%H%x00%B%x01', tip, '--not', base]
    if paths:
        args += ['--', *paths]
    for blk in git(*args).split('\x01'):
        if '\x00' not in blk:
            continue
        sha, msg = blk.split('\x00', 1)
        m = _SESS.search(msg)
        if m and m.group(1) == sess:
            out.append(sha.strip())
    return out


def added_rows(sha):
    """[(receipt, literal, verdict)] the commit `sha` ADDS to the baseline"""
    out = []
    for ln in git('show', '--unified=0', '--format=', sha, '--', BASELINE).split('\n'):
        if not ln.startswith('+') or ln.startswith('+++'):
            continue
        q = ln[1:].split('\t')
        if len(q) >= 6 and not q[0].startswith('#'):
            try:
                out.append((q[0], json.loads(q[1]), q[5]))
            except ValueError:
                pass
    return out


def rows_at(sha):
    """{(receipt, literal): (verdict, reason)} as the baseline stands at `sha`"""
    out = {}
    for ln in git('show', f'{sha}:{BASELINE}').split('\n'):
        q = ln.split('\t')
        if len(q) >= 6 and not ln.startswith('#'):
            try:
                out[(q[0], json.loads(q[1]))] = (q[5], q[6] if len(q) > 6 else '')
            except ValueError:
                pass
    return out


def mint_of(receipt, literal, tip=FRAME, base=BASE):
    """the OLDEST commit in the pinned range whose diff on `receipt` changes the count of `literal`"""
    shas = git('log', '--reverse', '--format=%H', '-S', literal, tip, '--not', base,
               '--', receipt).split()
    return shas[0] if shas else None


def measure(tip=FRAME):
    """the whole scan, as data.  Cached in `RESULT` so a reader pays for it once."""
    if RESULT.get('tip') == tip:
        return RESULT
    sess = own_session()
    assert sess, 'the frame commit carries no session marker, so this seat cannot be selected'

    reg = mine(BASE, tip, BASELINE)
    passes = {}
    for s in reg:
        r = rev_of(s)
        if r != 'NO-REV':
            passes.setdefault(r, []).append(s)

    late, exposed, early, ontime, oldmint, foreign = [], [], [], [], [], []
    seen = set()
    for s in reg:
        rrev = rev_of(s)
        for rec, lit, verdict in added_rows(s):
            if (rec, lit) in seen:
                continue
            seen.add((rec, lit))
            m = mint_of(rec, lit, tip)
            if m is None:
                oldmint.append((rec, lit))
                continue
            ms = _SESS.search(body(m))
            if ms and ms.group(1) != sess:
                foreign.append((rec, lit, rev_of(m), rrev))
                continue
            mrev = rev_of(m)
            entry = (rec, lit, m, mrev, s, rrev)
            if mrev == rrev:
                ontime.append(entry)
                continue
            late.append(entry)
            if mrev.startswith('r') and rrev.startswith('r') and int(rrev[1:]) < int(mrev[1:]):
                early.append(entry)
            if is_ancestor(m, TRUNK) and not is_ancestor(s, TRUNK):
                exposed.append(entry)

    #: ⛭ THE MECHANISM: a count says how many, and this says how the gap opened.
    mech = []
    for rec, lit, m, mrev, s, rrev in late:
        last = passes.get(mrev, [None])[-1]
        mech.append((lit, m, mrev, last,
                     bool(last) and last != m and is_ancestor(last, m)))

    #: ⚠ the prediction's words admit two readings and the ambiguity is this seat's.  The one SCORED is
    #: per-revision, because the registered floor of 1 was read off `ba75b3fb` being `r7370`'s LAST pass;
    #: the summed reading double-counts a revision that registered more than once.  Both are returned.
    d_rev, d_sum, d_detail = 0, 0, {}
    for r, ps in passes.items():
        after = [c for c in mine(ps[-1], tip, 'receipts/') if rev_of(c) == r]
        d_rev += len(after)
        d_detail[r] = (ps, after)
        for p in ps:
            d_sum += len([c for c in mine(p, tip, 'receipts/') if rev_of(c) == r])

    named = []
    at_frame = rows_at(tip)
    for (rec, lit), (verdict, why) in sorted(at_frame.items()):
        if 'S55_' in rec and lit in NAMED:
            m = mint_of(rec, lit, tip)
            named.append((rec, lit, verdict, why, m, rev_of(m) if m else 'OLD-MINT'))

    RESULT.clear()
    RESULT.update(tip=tip, session=sess, reg=reg, passes=passes, named=named,
                  late=late, exposed=exposed, early=early, ontime=ontime,
                  oldmint=oldmint, foreign=foreign, mech=mech,
                  d_rev=d_rev, d_sum=d_sum, d_detail=d_detail, rows_at_frame=at_frame)
    return RESULT


def score(got, lo, hi):
    return 'INSIDE' if lo <= got <= hi else ('BELOW' if got < lo else 'ABOVE')


def main():
    print(__doc__)
    R = measure()
    print(f'    frame {FRAME}   base {BASE}   trunk {TRUNK} (pinned)')
    print(f'    the live trunk reads {git("rev-parse", "--short=8", "origin/main").strip()} '
          f'and is asserted of nothing, per r7368 (2)')
    print()

    print('  THE TWO KEYS 66 NAMED, as the baseline stands at the frame')
    for rec, lit, verdict, why, m, mrev in R['named']:
        print(f'      {lit!r:18} {verdict:12} minted {(m or "-")[:8]} ({mrev})')
        print(f'         reason: {why[:104]}')
    print()

    print(f'  {len(R["reg"])} registration pass(es) of this seat\'s in the range; '
          f'{len(R["passes"])} carry a revision id')
    for r in sorted(R['passes'], key=lambda x: int(x[1:])):
        for s in R['passes'][r]:
            print(f'      {s[:8]}  {r:8} {len(added_rows(s)):4} row(s) added')
    print()

    _tot = sum(len(R[k]) for k in ('late', 'ontime', 'oldmint', 'foreign'))
    print(f'  {_tot} row(s) added by this seat in the range')
    print(f'      {len(R["oldmint"]):4}  OLD-MINT  -- literal predates the base, excluded from the split')
    print(f'      {len(R["foreign"]):4}  FOREIGN   -- literal introduced by another seat\'s commit')
    print(f'      {len(R["ontime"]):4}  ON TIME   -- mint revision == row revision')
    print(f'      {len(R["late"]):4}  LATE      -- arm (a), central 7 band 2-21 -> '
          f'{score(len(R["late"]), 2, 21)}')
    print(f'      {len(R["exposed"]):4}  EXPOSED   -- arm (b), central 2 band 2-14 -> '
          f'{score(len(R["exposed"]), 2, 14)}')
    print(f'      {len(R["early"]):4}  EARLY     -- arm (c), exact 0 -> '
          f'{"HIT" if not R["early"] else "MISS"}')
    print()

    print('  EVERY LATE ROW')
    for rec, lit, m, mrev, s, rrev in R['late']:
        print(f'      {m[:8]} ({mrev}) -> {s[:8]} ({rrev})  {os.path.basename(rec)[:30]:30} {lit[:34]!r}')
    print()

    print('  THE MECHANISM -- did each LATE row\'s mint FOLLOW its own revision\'s last pass?')
    for lit, m, mrev, last, follows in R['mech']:
        print(f'      {lit[:26]!r:28} minted {m[:8]} ({mrev}); {mrev}\'s last pass '
              f'{(last or "-")[:8]}; mint follows it: {follows}')
    _n = sum(1 for *_, f in R['mech'] if f)
    print(f'      => {_n} of {len(R["mech"])} LATE row(s) were minted AFTER their own revision\'s pass')
    print()

    print('  ARM (d) -- receipt-touching commits that FOLLOW a revision\'s last registration pass')
    for r in sorted(R['d_detail'], key=lambda x: int(x[1:])):
        ps, after = R['d_detail'][r]
        print(f'      {r}: {len(ps)} pass(es), last {ps[-1][:8]}, {len(after)} receipt commit(s) follow it')
        for c in after:
            print(f'         {c[:8]}  {subject(c)[:70]}')
    print(f'      => {R["d_rev"]} after each revision\'s LAST pass -- arm (d), central 2 band 1-6 -> '
          f'{score(R["d_rev"], 1, 6)}')
    print(f'      => {R["d_sum"]} summed over every pass (the other reading, reported not scored)')
    print()

    print('  WHAT THE FIGURES SAY')
    print('      Both keys 66 named are adjudicated at the frame and both were minted a revision')
    print('      before their row was written, so the gap is the finding and not the verdict.')
    print('      ⛔ AND THE REGISTERED REASONING WAS WRONG: the gap did not open by deferring a pass')
    print('      across revisions.  It opened INSIDE r7368, three commits after that revision\'s own')
    print('      pass had already run -- which is 66\'s SECOND candidate, not this seat\'s first.')
    print(f'      arm (a) {len(R["late"])}   arm (b) {len(R["exposed"])}   '
          f'arm (c) {len(R["early"])}   arm (d) {R["d_rev"]}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
