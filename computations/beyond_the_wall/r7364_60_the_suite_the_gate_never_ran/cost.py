#!/usr/bin/env python3
"""`60`'s next revision -- THE SUITE THE GATE NEVER RAN: the arithmetic of the registration,
written and pushed BEFORE the measurement is read.

** WHY THIS MEASUREMENT, AND WHY IT IS A CONFESSION BEFORE IT IS A RESULT. **  This seat's landing
sequence for the whole phase was `scripts/run_fast_job.sh` -- `126` gates and `10` generators, every
`corpus/check_*.py` -- and it does **not run receipts**.  *Three revisions landed on that sequence.*
The CI job that does run them has been red on this branch and every notification was read as a
superseded head; four receipts turn out to be genuinely red, and not one of them is a receipt this
seat was watching.
  ⇒ ** So the thing to measure is not the four.  It is the size of the hole: how much of the suite
    scope is red behind a landing sequence that cannot see receipts at all, and whether the reds
    share one cause. **

** THE FOUR ALREADY IN HAND, BY HAND, BEFORE THE SCOPE RUN WAS LAUNCHED. **
  `S19` -- two gates reading the live quote-pin ledger, both FAIL-ON-SUCCESS: a `0 < count` floor
    whose defect this seat's own repairs drove to `0`, and an ordering of five rates that swapped
    because the phase retired `60`+ `REPAIR-OWED` rows.
  `P03` -- `Ⓗ②`: `14` modified receipts outside what this seat owns read as UNAUTHORISED.
  `S5`  -- `Ⓕ②` and `Ⓖ③`: the same crossings, under a different notion of `mine`, `5` of them left.
  `S23` -- `Ⓕ③` and `Ⓕ④`: both downstream of `P03`, which `S23` runs.
  ⇒ *Two root causes, not four: a gate reading the live state of a thing its own revision changed,
    and an authorisation carried where neither authorship gate reads it.*

** COMPUTES: ** the three registered bands and their decisive fractions under an exact binomial, and
the scope census read from `SCOPE.txt`, which is the list the run was launched on, pinned here at its
digest.  No outcome: `scored()` returns `None` until the result block is appended by the reading push.

⚠ THE REGISTRATION IS BLIND AND SAYS HOW.  The scope run was launched at `08:45` and was still in
flight when this was written; its output file had been opened and was `0` bytes, and nothing in it has
been read.  *The run having started is not information about its result -- but it is stated rather
than left to be assumed, because a registration whose blindness cannot be checked is not one.*
"""
import io
import os
import re
import subprocess
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
SCOPE = os.path.join(HERE, 'SCOPE.txt')
SEAT = '60'
#: the head the scope was cut at and the run launched from.  Pinned, as `r7356` learned and `r7358`
#: learned twice: a measurement a revision takes of a thing the revision edits cannot be read live --
#: and this revision edits receipts that are IN the scope.
CENSUS = 'c6fe446c'            # r7362's last commit
SCOPE_DIGEST = 'b218389147e3'  # sha1 of SCOPE.txt, the list the run was launched on
#: the scope was cut by `scripts/receipt_scope.py --range 4e9d16ef..HEAD --scope suite`
SCOPE_RANGE = '4e9d16ef..HEAD'
#: the four reds found BY HAND before the run, which arm ⒜ scores on the remainder and not on these
KNOWN_RED = (
    'receipts/L_probability/S19_a_markup_carrier_cannot_be_repaired_by_splitting_it',
    'receipts/L_probability/S23_four_items_and_every_one_was_mis_described',
    'receipts/L_probability/S5_the_set_shaped_class_is_absent_from_the_gate_layer',
    'receipts/P03_SdS_slicing/P03_the_enclosed_mass_is_monotone',
)

# ── arm ⒜: THE RED COUNT ON THE PART NOBODY LOOKED AT ────────────────────────────────────────────
#   ⚠ Scored on the REMAINDER, not on the scope.  The four above were found by following CI logs and
#   the carry ledger's contradiction marks, so they are an ENRICHED sample and a band over all `155`
#   would have a floor of `4` by construction -- an unfailable floor, which `r7325`'s standing rule
#   forbids.  The honest space is the `151` nobody has looked at.
#   Central: this seat's three revisions touched `30` foreign receipts and `13` of its own; the suite
#   scope is the readers of what changed, so the base rate on the unexamined part should be LOW but
#   not zero -- `5` of `152`.
#   ⛔⛭ AND THE SPACE IS `152` AND NOT `151` BECAUSE **`P03` IS NOT IN THE SUITE SCOPE AT ALL.**
#   *`scripts/receipt_scope.py` cuts the scope as the READERS OF THE CHANGED FILES, by path.  `P03`'s
#   `Ⓗ②` reads this branch by asking `git` -- the commits, their messages and their name-only diffs --
#   so it reads the branch without naming a single changed path, and the cutter cannot see it.*
#   ⇒ ** A third face of the hole, under the two in the reds themselves: the scope that was supposed
#     to catch what the gate layer misses is itself blind to a receipt that reads the REPOSITORY
#     instead of a file. **  `P03` was found only because `S23`, which IS in the scope, runs it.
A_SPACE = 152
A_CENTRAL = 0.033              # 5 of 152
A_BAND = (0.013, 0.060)        # 2 to 9 receipts

# ── arm ⒝: ONE CAUSE OR MANY ─────────────────────────────────────────────────────────────────────
#   Of every red the run names, the share whose root cause is A GATE READING THE LIVE STATE OF A
#   THING THIS BRANCH CHANGED -- the fail-on-success family and its authorisation face.
#   ** On the four in hand the share is `4` of `4`. **  If it holds on the remainder, the hole in the
#   landing sequence has ONE shape and a single check closes it; if it does not, the suite scope is
#   carrying unrelated rot that three revisions of this seat merely failed to look at, which is a
#   worse finding and the one this arm exists to be able to report.
#   ⛭ DECLARED: this band can only fail LOW.  Its ceiling is `1.0` and a share cannot exceed it, so
#   a pass at the top is no evidence; the arm is informative only in refutation.  *Stated here rather
#   than discovered later, which is `r7325`'s rule and `r7337`'s third refusal.*
B_CENTRAL = 0.80
B_BAND = (0.55, 1.00)          # fails only below 0.55

# ── arm ⒞: WHAT THE LANDING SEQUENCE WOULD HAVE CAUGHT, AND IT IS A POINT PREDICTION ─────────────
#   ** `0`. **  Not a band: the claim is that NOT ONE red in the scope is visible to any
#   `corpus/check_*.py`, so the sequence this seat landed three revisions on could not have seen any
#   of them.  Scored by running the gate set at the same head and asking whether it is green.
#   ⇒ *A point prediction is the most falsifiable form available here and the arm is worth nothing in
#     any weaker one: if even ONE red is gate-visible, the sequence was partly adequate and the
#     finding is about this seat's attention instead of about the sequence.*
C_PREDICTION = 0

RESULT = {}


def decisive_share(n, central, band):
    """the chance the band is refuted if `central` is true -- the arm's own power, stated up front"""
    lo, hi = band[0] * n, band[1] * n
    return sum(comb(n, k) * central ** k * (1 - central) ** (n - k)
               for k in range(n + 1) if k < lo or k > hi)


def scope():
    """the `155` receipts the run was launched on, read from the pinned list"""
    return [l.strip() for l in io.open(SCOPE, encoding='utf-8') if l.strip()]


def scope_digest():
    import hashlib
    return hashlib.sha1(io.open(SCOPE, 'rb').read()).hexdigest()[:12]


def known_red(rels=None):
    """the four found by hand, matched by prefix against the scope"""
    rels = scope() if rels is None else rels
    return [r for r in rels if any(r.startswith(k) for k in KNOWN_RED)]


def remainder(rels=None):
    """the `151` nobody has looked at -- arm ⒜'s space"""
    rels = scope() if rels is None else rels
    hand = set(known_red(rels))
    return [r for r in rels if r not in hand]


def outside_scope():
    """the hand-found reds the cutter did not put in the scope -- `P03`, and why"""
    rels = scope()
    return [k for k in KNOWN_RED if not any(r.startswith(k) for r in rels)]


def by_prefix(rels=None):
    """the scope by receipt directory, so the census can be read without the result"""
    import collections
    rels = scope() if rels is None else rels
    return collections.Counter(r.split('/')[1] for r in rels)


def mine(rels=None):
    """how much of the scope is this seat's own receipts -- the part a seat would notice first"""
    rels = scope() if rels is None else rels
    return [r for r in rels
            if r.startswith('receipts/L_probability/S') or r.startswith('receipts/P15_CR_cosmology/')]


def gate_names():
    """every `corpus/check_*.py` -- arm ⒞'s whole population, which runs no receipt"""
    return sorted(f for f in os.listdir(os.path.join(ROOT, 'corpus'))
                  if re.match(r'check_.*\.py$', f))


def touched_receipts(sha=CENSUS):
    """the receipts this branch's own commits modified, which is what the scope is the readers of"""
    txt = subprocess.run(['git', '-C', ROOT, 'diff', '--name-only', 'origin/main', sha],
                         capture_output=True, text=True, errors='replace').stdout
    return [l for l in txt.split('\n') if l.startswith('receipts/') and l.endswith('.py')]


def scored():
    """`None` until the reading push appends the result block -- no outcome is registered here"""
    return None if not RESULT else RESULT


def report():
    rels = scope()
    print()
    print(f'  r7364 · {SEAT} — THE SUITE THE GATE NEVER RAN  (registration; nothing scored)')
    print(f'    scope: {len(rels)} receipt(s) in the SUITE scope, cut {SCOPE_RANGE} at {CENSUS}')
    print(f'    scope digest: {scope_digest()}  (registered {SCOPE_DIGEST} — '
          f'{"MATCHES" if scope_digest() == SCOPE_DIGEST else "DIFFERS"})')
    print(f'    of them {len(mine(rels))} are this seat\'s own; {len(known_red(rels))} are the reds '
          f'already found by hand IN IT, and arm ⒜\'s space is the remaining {len(remainder(rels))}')
    print(f'    ⛔ and {len(outside_scope())} hand-found red is NOT IN THE SCOPE: '
          f'{[k.split("/")[-1][:28] for k in outside_scope()]} — it reads the branch through `git` '
          f'and names no changed path, so the cutter cannot see it')
    print(f'    the branch gives the scope {len(touched_receipts())} modified receipt(s) to read')
    print(f'    the landing sequence arm ⒞ scores: {len(gate_names())} gates, '
          f'and not one of them runs a receipt')
    print()
    print(f'    arm ⒜  red in the {A_SPACE} unexamined: central {A_CENTRAL:.3f} '
          f'({round(A_CENTRAL * A_SPACE)} of {A_SPACE}), band {A_BAND[0]}–{A_BAND[1]} '
          f'({round(A_BAND[0] * A_SPACE)}–{round(A_BAND[1] * A_SPACE)} receipts), decisive '
          f'{decisive_share(A_SPACE, A_CENTRAL, A_BAND):.3f}')
    print(f'    arm ⒝  share of red with the ONE cause: central {B_CENTRAL:.2f}, '
          f'band {B_BAND[0]}–{B_BAND[1]} — ⛭ FAILS ONLY LOW, declared')
    print(f'    arm ⒞  reds the gate layer would have caught: POINT PREDICTION {C_PREDICTION}')
    print()
    print('    ⛔ AND THE REPAIRS ARE NOT REGISTERED HERE.  *Two are diagnosed and written out in')
    print('      PREDICTION.md before the count is read, so the diagnosis cannot be fitted to it.*')
    print()


if __name__ == '__main__':
    report()
