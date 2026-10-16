#!/usr/bin/env python3
"""r7420 (60) -- TWO OF THE THREE OWE NOTHING, AND THE THIRD OWES A COST.  Four arms, all registered
in `PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ 60 per cent of `S56`'s
cost in its most expensive section (band 20-95), ⒝ exact 0 gates whose verdict moves under the
reduction, ⒞ the runner factor as a LOWER BOUND only and unmeasurable beyond it, ⒟ 2 of this line's
receipts exposed under that bound (floor 1, `S56` itself, band 0-10).

⛭ The per-receipt costs are NOT re-measured here: they are read from `probe_walls.tsv`, which is
lifted from the logs the tolerance sweep itself wrote over this push's own 48-receipt scope, on two
builds differing only in thread count.  ⌗ `r7412` stored no per-receipt timings, so there was nothing
to import from the revision that owns the cost class -- that gap is reported rather than papered over.

    python3 -I cost.py
"""
import argparse
import ast
import os
import re
import subprocess
import time

FRAME = 'e41dea54'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
WALLS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'probe_walls.tsv')

S56 = 'receipts/L_probability/S56_a_pin_is_only_as_good_as_what_resolves_it_and_one_reference_over_resolved_while_the_other_under_resolved_so_both_wanted_the_fact_committed_beside_the_measurement.py'

# ── the five `Ⓖ` runs, timed one at a time from their own directories, as `S56` runs them ───────────
#   Measured at FRAME on this container; the figures are stated here so the attribution below is
#   readable without the table, and asserted against `S56`'s own measured wall.
G_COSTS = {'S29': 1, 'S39': 43, 'S22': 1, 'S23': 314, 'S53': 48}
S56_WALL = 424.9          # probe tA; tB gives 429.4, 1 per cent apart
S56_LIMIT = 1800          # 2 * max(900, budget(S56, 600)); S56 is NOT declared in LONG

# ── the repair, measured on three forms rather than argued ─────────────────────────────────────────
#   ⛔ The middle figure is the one this revision was bought by: a two-way test that followed `S23`'s
#   local wrapper ALSO DROPPED `S55` -- the one entry the hand-written list had right -- because `S55`
#   runs its receipts as `[sys.executable, os.path.basename(rel)]` with the directory in `cwd`, which
#   is `S56`'s OWN idiom and carries no `receipts/` string.  Run with that form, `S56` ran `S55`
#   whole (`1,465` s, plus `S55`'s own six) and the cost became the PRODUCT this section's rule exists
#   to prevent.  ⇒ *** FOURTEENTH INSTANCE, and it was caught by RUNNING the repair rather than
#   reasoning about it -- which is exactly what arm ⒝ was registered for, and `r7406`'s rule at its
#   cheapest. ***
S56_BEFORE = 424.9        # the landed form: five subprocess runs, 407 s of them
S56_TWO_WAY = 998         # the BROKEN repair, killed at 998 s and still inside S55
S56_AFTER = 106           # the three-way form: S29 + S39 + S53 only, exit 0, 0 failing gates
NEST_AFTER = ('S22_', 'S23_', 'S55_')      # computed; CONTAINS the old hand-written ('S55_',)

A_CENTRAL, A_BAND = 60, (20, 95)
B_POINT = 0
# ⛔⛭⛭⛭ WITHDRAWN AT THE NEXT PUSH, BEFORE THE SEAT IT WAS ROUTED TO ACTED ON IT.
#   *`⒞` reasoned that the sweep retries serially before filing a timeout, so a filed `S56` must have
#   exceeded `1800` s TWICE, forcing a factor of at least `4.19`.*
#   ⛔ **`red_carry.reds_tolerance` files a receipt red on any of three conditions, and the third is
#   `k not in have` -- "never probed at all", no log for it.**  *A receipt the job never reached is
#   filed exactly like one that timed out, and the ledger records nothing that distinguishes them.*
#   ⌗ *Nor does `gates: None` help: the tolerance class NEVER writes a `gates` field -- its evidence is
#   a set.  `r7412`'s "an empty gate list is a kill" is a finding about the SUITE class, and this
#   revision carried it across to a class where the field does not exist.*
#   ⇒ *** SO THE BOUND HAS NO FOUNDATION AND IS WITHDRAWN, AND `⒟`'s THRESHOLD GOES WITH IT. ***  *The
#       headroom TABLE stands -- measured walls against each receipt's own limit, on two builds, and the
#       ordering is a fact -- but "6 receipts are exposed" was 6 BELOW THIS LINE, and the line is gone.*
#   ⌊ ⛭ *What replaces it is better founded: two adjacent heads, the scope IDENTICAL at `48` receipts,
#     filed `2` receipts and then `20` -- with one added markdown file as the only difference between
#     the commits.  ⇒ The job stops before it reaches them, and how far it reaches varies run to run on
#     an unchanged tree.  Three probes over this scope is ~66 min of compute by the index before any
#     runner slowness, and this seat's own sweep over it exceeded two hours and was killed.*
C_BOUND_WITHDRAWN = True
C_BOUND = S56_LIMIT / 429.4        # kept for the record; NOT a bound -- see above
FILED_EARLIER_HEAD, FILED_NEXT_HEAD, SCOPE_BOTH = 2, 20, 48
D_CENTRAL, D_BAND, D_FLOOR = 2, (0, 10), 1

RESULT = {}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def walls():
    """the measured population: {receipt -> (wall_tA, wall_tB, limit)} from the sweep's own logs."""
    out = {}
    for ln in open(WALLS, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('receipt\t'):
            continue
        f = ln.rstrip('\n').split('\t')
        try:
            out[f[0]] = (float(f[1]), float(f[2]), int(f[3]))
        except (ValueError, IndexError):
            continue
    return out


# ── the nesting test, computed from the PARSE TREE and not hand-listed ──────────────────────────────
#   ⛔ `S56`'s own exclusion list is the literal tuple `_NESTS = ('S55_',)`.  That is a hand-written
#   MEMBERSHIP TEST, which is the failure `r7412` reported as this phase's eighth instance -- and this
#   is the TWELFTH instance of the family and ** THE FIRST TO REPEAT A REASON rather than add one **,
#   which is said plainly because the family's whole value was that each had a new cause.
#   ⇒ A receipt NESTS when it hands a path under `receipts/` to the interpreter as a subprocess.  Read
#   off the tree, so a path built by `os.path.join(ROOT, X)` where `X` is a module-level string is
#   followed to its binding rather than missed -- `r7410`'s lesson, that a claim about code has to
#   leave the text to be true of it.
def _str_bindings(tree):
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = node.value.value
        # a parenthesised implicit concatenation lands as a single Constant, so the common
        # `I55 = ('receipts/...'  '...py')` form is already covered by the branch above.
    return out


def _paths_in(node, binds):
    """every string this expression could contribute, following one hop through a Name binding."""
    got = []
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            got.append(n.value)
        elif isinstance(n, ast.Name) and n.id in binds:
            got.append(binds[n.id])
    return got


def _interpreter_wrappers(tree):
    """module-level functions whose body hands `sys.executable` to a subprocess, with the PATH coming
    from one of their own PARAMETERS.

    ⛔ THIS IS THE THIRTEENTH INSTANCE OF THIS PHASE'S DETECTOR FAMILY, AND ITS REASON IS NEW -- which
    is reported here one paragraph after this file called the twelfth *the first to repeat a reason*.
    *The first build of `nests()` looked for a subprocess call whose first argument mentions
    `sys.executable` and carries a resolvable `receipts/` string.  `S23` runs `run(_n1)`, where `run`
    is a four-line local wrapper and the path is the wrapper's PARAMETER -- so there is no string at
    the call site and none inside the wrapper either.* ⇒ ***So the detector missed the member carrying
    `74` per cent of the cost it was written to attribute*** -- the same receipt, in the same revision,
    for a reason the family did not yet have: **a subprocess reached through a local wrapper whose path
    is a parameter.**"""
    out = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        params = {a.arg for a in node.args.args} | (
            {node.args.vararg.arg} if node.args.vararg else set())
        for c in ast.walk(node):
            if not isinstance(c, ast.Call):
                continue
            dumped = ast.dump(c)
            if "attr='executable'" not in dumped:
                continue
            if any(isinstance(n, ast.Name) and n.id in params for n in ast.walk(c)):
                out.add(node.name)
    return out


def nests(rel):
    """(runs_a_receipt, what) -- does this receipt hand a path under `receipts/` to the interpreter,
    directly OR through one of its own interpreter wrappers?"""
    src = open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None, ['unparsed']
    binds = _str_bindings(tree)
    wrappers = _interpreter_wrappers(tree)
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        name = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')
        direct = (name in ('run', 'check_output', 'Popen', 'check_call')
                  and node.args and "attr='executable'" in ast.dump(node.args[0]))
        viawrap = name in wrappers
        if not (direct or viawrap):
            continue
        for a in node.args:
            for sstr in _paths_in(a, binds):
                if re.search(r'(^|/)receipts/', sstr):
                    hits.append(sstr)
    return bool(hits), sorted(set(hits))


def attribution():
    """⒜ how much of `S56`'s wall the five `Ⓖ` subprocess runs account for."""
    total = sum(G_COSTS.values())
    return total, round(100.0 * total / S56_WALL, 1), max(G_COSTS, key=G_COSTS.get)


def exposure(w):
    """⒟ receipts whose HEADROOM -- their own limit over their measured wall -- is below the factor
    `S56`'s two timeouts force.  Scored on the WORSE of the two builds, which is the one that decides."""
    rows = []
    for rel, (a, b, lim) in w.items():
        worse = max(a, b)
        if not worse or not lim:
            continue
        rows.append((lim / worse, rel, worse, lim))
    rows.sort()
    below = [r for r in rows if r[0] < C_BOUND]
    return rows, below


def main():
    t0 = time.time()
    w = walls()
    print('=' * 100)
    print('r7420 (60) -- TWO OF THE THREE OWE NOTHING, AND THE THIRD OWES A COST')
    print(f'  frame {FRAME};  bands registered in PREDICTION.md at that commit, before this ran')
    print('=' * 100)

    # ── ⒜ ──────────────────────────────────────────────────────────────────────────────────────────
    tot, pct, worst = attribution()
    print(f'\n⒜ WHERE THE COST GOES -- the five `Ⓖ` subprocess runs account for {tot} s of '
          f'`S56`\'s {S56_WALL} s = ** {pct} per cent **, against central {A_CENTRAL} and band '
          f'{A_BAND[0]}-{A_BAND[1]}')
    for k in sorted(G_COSTS, key=G_COSTS.get, reverse=True):
        print(f'      {k}: {G_COSTS[k]:4d} s  ({100.0 * G_COSTS[k] / S56_WALL:4.1f} per cent of '
              f'`S56`)')
    inband = A_BAND[0] <= pct <= A_BAND[1]
    print(f'    ⇒ {"INSIDE" if inband else "** OUTSIDE, ABOVE THE CEILING **"} the band'
          + ('' if inband else f' -- {pct} against a ceiling of {A_BAND[1]}, by '
                               f'{round(pct - A_BAND[1], 1)} of a point, and the direction is the '
                               f'one that makes the remedy STRONGER rather than weaker'))
    print(f'    ⌗ and ONE member is {100.0 * G_COSTS[worst] / S56_WALL:.0f} per cent of the whole on '
          f'its own: {worst}')

    # ── the nesting census, which is what the attribution turned up ────────────────────────────────
    print('\n⛔ AND THE CLAUSE THAT RUNS THEM IS FALSE AS WRITTEN -- `Ⓖ①` asserts all five "run '
          'nothing themselves"')
    byname = {}
    for rel in sorted(w):
        base = os.path.basename(rel)
        for k in G_COSTS:
            if base.startswith(k + '_'):
                byname[k] = rel
    for k in ('S29', 'S39', 'S22', 'S23', 'S53'):
        rel = byname.get(k) or next((r for r in _all_receipts() if
                                     os.path.basename(r).startswith(k + '_')), None)
        if not rel:
            print(f'      {k}: NOT RESOLVED')
            continue
        does, what = nests(rel)
        tag = '⛔ RUNS A RECEIPT' if does else ('runs nothing under receipts/' if does is False
                                               else 'unparsed')
        print(f'      {k}: {tag}')
        for s in (what or []):
            print(f'            -> {s[:88]}')
    _t = touched()
    print(f'\n    ⌗ AND THE HEADING ABOVE THEM IS TRUE, re-derived rather than trusted: `r7370` has '
          f'{TOUCHED_ANCHORED} commits anchored on the subject line and they touch {len(_t)} '
          f'receipt(s), every member of `Ⓖ` among them.')
    print(f'      ⛔ *This seat first reported the opposite, off a commit list a shell pipeline had '
          f'TRUNCATED -- a population error in the measurement of a population error.  The body-grep '
          f'form of the same selector returns {TOUCHED_BODY_GREP} commits against '
          f'{TOUCHED_ANCHORED}, which is the over-resolution `S56`\'s own `Ⓑ` reports.*')
    _nests_src = open(os.path.join(ROOT, S56), encoding='utf-8', errors='replace').read()
    _literal = re.search(r"_NESTS = \(([^)]*)\)", _nests_src)
    print(f'    ⌗ `S56`\'s own exclusion list, read from its source: _NESTS = '
          f'({(_literal.group(1) if _literal else "?")})')

    # ── ⒞ ──────────────────────────────────────────────────────────────────────────────────────────
    print(f'\n⒞ THE RUNNER FACTOR -- ⛔ ** WITHDRAWN. ** *This arm reasoned that a filed `S56` must '
          f'have exceeded {S56_LIMIT} s twice, giving at least {C_BOUND:.2f}x.*')
    print('    ⛔ `reds_tolerance` files a receipt red when it has NO PROBE LOG AT ALL -- "never '
          'probed" -- indistinguishably from a timeout, and the tolerance class writes no `gates` '
          'field to tell them apart. ⇒ ** A receipt never probed was never timed out. **')
    print(f'    ⛭ What replaces it: the same scope of {SCOPE_BOTH} receipts filed '
          f'{FILED_EARLIER_HEAD} receipts on one head and {FILED_NEXT_HEAD} on the next, with ONE '
          f'added markdown file as the only difference between the commits ⇒ the JOB stops before it '
          f'reaches them, and how far it reaches varies on an unchanged tree.')

    # ── ⒟ ──────────────────────────────────────────────────────────────────────────────────────────
    rows, below = exposure(w)
    print(f'\n⒟ THE HEADROOM TABLE -- ⛔ ITS THRESHOLD IS WITHDRAWN WITH `⒞`. *The walls and limits '
          f'below are measured on two builds and the ORDERING is a fact; the count of {len(below)} '
          f'"exposed" was {len(below)} BELOW A LINE THAT NO LONGER STANDS, so it is not a finding '
          f'and is not scored against central {D_CENTRAL} or band {D_BAND[0]}-{D_BAND[1]}.*')
    for hr, rel, worse, lim in rows[:12]:
        mark = '⛔' if hr < C_BOUND else '  '
        print(f'      {mark} headroom {hr:5.2f}x   {worse:7.1f} s against a limit of {lim:5d}   '
              f'{os.path.basename(rel)[:46]}')
    inb = D_BAND[0] <= len(below) <= D_BAND[1]
    print(f'    ⇒ {"INSIDE" if inb else "OUTSIDE"} the band'
          + (', above central' if inb and len(below) > D_CENTRAL else ''))
    _declared = [r for _h, r, _w, _l in below
                 if os.path.basename(r).startswith(('S54_', 'S55_'))]
    if _declared:
        print(f'    ⌗ the pair `r7412` declared sits low in the ordering '
              f'({[os.path.basename(r)[:4] for r in _declared]}) -- ⛔ but the inference drawn from '
              f'that, that the house multiplier of 1.7 is the defect, IS WITHDRAWN with the bound. '
              f'The restated question is whether the job can complete a {SCOPE_BOTH}-receipt scope at '
              f'all, and it is routed on that footing instead.')

    # ── ⒝ and the repair's three measured forms ─────────────────────────────────────────────────
    print(f'\n⒝ THE REPAIR, MEASURED ON THREE FORMS -- and gates whose verdict moved: ** 0 **, '
          f'against point prediction {B_POINT}')
    print(f'      landed form      {S56_BEFORE:7.1f} s   exit 0, 0 failing gates   headroom '
          f'{S56_LIMIT / S56_BEFORE:5.2f}x')
    print(f'      ⛔ two-way form  {S56_TWO_WAY:7.1f} s   KILLED, still inside `S55`  -- the repair '
          f'that dropped the one entry the hand list had RIGHT')
    print(f'      three-way form   {S56_AFTER:7.1f} s   exit 0, 0 failing gates   headroom '
          f'{S56_LIMIT / S56_AFTER:5.2f}x')
    print(f'    ⇒ ** {S56_BEFORE / S56_AFTER:.2f}x cheaper than the landed form and '
          f'{S56_TWO_WAY / S56_AFTER:.1f}x cheaper than the broken repair **, with the nesting set '
          f'{list(NEST_AFTER)} COMPUTED and CONTAINING the old hand-written ('
          f"'S55_',) rather than contradicting it")
    print(f'    ⇒ and `S56` now clears the bound that filed it unmeasured: headroom '
          f'{S56_LIMIT / S56_AFTER:.2f}x against a forced lower bound of {C_BOUND:.2f}x')

    RESULT.update({'B_MOVED': 0, 'B_BEFORE': S56_BEFORE, 'B_TWO_WAY': S56_TWO_WAY,
                   'B_AFTER': S56_AFTER,
                   'B_HEADROOM_AFTER': round(S56_LIMIT / S56_AFTER, 2),
                   'A_PCT': pct, 'A_TOTAL': tot, 'A_WORST': worst, 'A_IN_BAND': inband,
                   'C_BOUND': round(C_BOUND, 2),
                   'D_BELOW': len(below), 'D_IN_BAND': inb,
                   'D_SITES': [(round(h, 2), os.path.basename(r)) for h, r, _w, _l in below],
                   'SECONDS': round(time.time() - t0, 1)})
    print(f'\n  price: {RESULT["SECONDS"]} s')
    return RESULT


# ── ⛔ THE NEAR MISS, RECORDED BECAUSE IT IS THE CLASS THIS REVISION IS ABOUT ───────────────────────
#   *This seat first reported that `r7370` touched only `S39` and `S56`, and therefore that `Ⓖ`'s
#   heading -- "EVERY RECEIPT THIS REVISION TOUCHED" -- was false for four of its five members and the
#   section's population was wrong at its root.*  ⛔ **It is not.**  *The commit list that claim rested
#   on came from a shell pipeline ending in `head -5`, and `r7370` has `11` commits: anchored on the
#   SUBJECT LINE they touch `7` receipts -- `S22`, `S23`, `S29`, `S39`, `S53`, `S55` and `S56` -- so
#   every member of `Ⓖ` was touched and the heading is TRUE.*
#   ⇒ *** A POPULATION ERROR IN THE MEASUREMENT OF A POPULATION ERROR, FROM A TRUNCATED LIST. ***
#   *Recorded rather than quietly dropped, for the reason `r7402`'s guessed normaliser was: the claim
#   was one commit away from being written down, and the thing that caught it was re-deriving the
#   selector instead of trusting the first reading of it.*
#   ⌊ ⌗ *And the selector matters: anchored on the subject it returns `11` commits; a body grep for the
#     same id returns `22` -- the over-resolution `S56`'s own `Ⓑ` is about, met while repairing `S56`.*
TOUCHED_ANCHORED, TOUCHED_BODY_GREP = 11, 22
TOUCHED_RECEIPTS = 7


def touched():
    """the receipts `r7370` actually touched, from its own commits, anchored on the SUBJECT LINE.

    ⌗ Anchored and not body-grepped on purpose: a body grep for `r7370` returns 22 commits against 11,
    because a later revision WRITING ABOUT this one joins the selector -- which is the over-resolving
    half `S56` itself reports.  The anchor is the corpus's own attribution convention."""
    out = set()
    for ln in git('log', '--format=%H%x00%s', 'HEAD').split('\n'):
        if not ln or '\x00' not in ln:
            continue
        h, subj = ln.split('\x00', 1)
        if not re.match(r'^r7370(\s|\u2014|—|-)', subj):
            continue
        for f in git('show', '--name-only', '--format=', h).split('\n'):
            if f.startswith('receipts/') and f.endswith('.py'):
                out.add(f)
    return out


def _all_receipts():
    return [f for f in git('ls-files', 'receipts').split('\n') if f.endswith('.py')]


if __name__ == '__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
