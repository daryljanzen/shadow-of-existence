#!/usr/bin/env python3
"""H1 -- the band I took at r3128 constrained one side of a partition and I wrote that this "removes
the collisions this line can cause and no others".  It removes NONE, by arithmetic; and eight landed
in the eight revisions of the turn that took it, every one while the gate ran green and printed the
reassurance.

COMPUTES: the withdrawn sentence read from the commit that carried it; a two-branch sandbox in which
one line is held to the band and the other is not, showing the band check GREEN while a collision
exists; the same sandbox with both halves held, showing the collision cannot be constructed; that the
gate now refuses the word "prevention" while the other half is unrecorded; and the testimony/measured
split over the eight.  No parameter is pinned -- every number is read from a repository built here.

** ⛭ ⓵ WHAT WAS CLAIMED. **  `L-256`, r3128: *"the other line adopting ODD is a request that has been
made and is not presumed answered; until it is, ** this half removes the collisions this line can
cause and no others **."*  ⇒ *The sentence was written to be careful -- it was scoping the claim
downward, and that is why it read as honest.*

** ⛔⛭⛭ ⓶ AND IT IS FALSE BY ARITHMETIC, NOT BY BAD LUCK. **

  *** A PARTITION CONSTRAINS A COLLISION ONLY WHEN BOTH PARTS ARE HELD. ***

A collision at `rN` needs both lines to write `rN`.  Holding this line to the evens leaves *** every
even number fully available to the other line ***, so the set of numbers at which a collision can
occur is unchanged.  ⇒ ** The constrained half removes nothing.  It is not a weak prevention; it is
not a prevention. **

** ⛔ ⓷ AND THE COST WAS ON THE COUNTER WHILE THE GATE PRINTED THE REASSURANCE. **  Node 57 reports
`r3125`, `r3126`, `r3128`, `r3130`, `r3132`, `r3134`, `r3136` and `r3138` each naming different work
in each line -- ** eight collisions across the eight revisions of the turn that took the band. **
  ⇒ *** A GATE THAT IS GREEN WITH A WRONG SENTENCE BESIDE IT IS WORSE THAN A RED ONE.  The red is
      read; the sentence is believed. ***

** ⌗ ⓸ WHAT THE HALF ACTUALLY DID, which is not nothing and is not what was claimed. **  *It made
this line's half ENFORCEABLE, which is what turned a proposal into something the other line could
accept or refuse in one step -- and node 57 did: "This tree now runs `PARITY = 1`, so your gate is
answered rather than presumed."*  ⇒ ** The value of a half-partition is as a proposal with a
mechanism attached.  Stating that is the correction; the enforcement was never the prevention. **

** ⓹ AND THE EIGHT ARE BASELINED APART FROM THE MEASURED ONES. **  *This tree holds one side of each
pair, so it cannot see a single one of them.*  ⇒ ** `TESTIMONY` is separate from `BASELINE` and the
gate prints the confirmed/reported split every run, because a baseline entry that is not an instance
is a gate quietly weakened -- and an entry still unconfirmed after the merge must be struck. **

WHAT IS NOT CLAIMED.  ** Not that the eight are verified here ** -- they cannot be, and the whole of
⓹ is about not letting that fact go quiet.  ** Not that the half-band caused them ** -- both lines
worked one night at one rate from one counter, which is sufficient on its own; what is claimed is
only that the half did not PREVENT them, which is arithmetic.  ** Not that the band is now proved **
-- it is now a partition, and the first revision after this one is its first live test.  ** And not
that the r3128 sentence was careless ** -- it was scoping a claim downward, which is the habit that
usually makes a claim safe, and it is exactly why nothing caught it.

    python3 receipts/L260_half_a_partition/H1_half_a_partition_removes_nothing_and_the_gate_said_otherwise_while_eight_landed.py

Written r3140, `L-260`.  Stated for reversal.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
# ** ⛭⛭ NODE IS SET HERE, BEFORE THE IMPORT (r3964, with `L251/N1`). **  `check_revision_collisions`
# ** reads `NODE` AT IMPORT TIME and *refuses to default* when unset -- r3679's rule, written after an
# ** unset NODE silently certified the EVEN half on odd-banded trees and passed 21 collisions.  The
# ** refusal is right; what was wrong is this file inheriting the answer from whoever ran it: unset in
# ** a plain shell, `ci` under `sweep_gates.sh`.  ** A receipt asserting anything about a band is
# ** making a claim about a NAMED line and must name it. **  Four receipts shared this defect and all
# ** four were on the failure list; they are fixed together because it is one fault, not four.
os.environ.setdefault('NODE', '60')
import check_revision_collisions as C                                     # noqa: E402

FAILED = []
BEFORE = '3ba0b694'          # r3138 -- the commit that carried the withdrawn sentence
GATE = os.path.join(ROOT, 'corpus', 'check_revision_collisions.py')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def sandbox(a_nums, b_nums):
    """two divergent lines committing the revision numbers given, and what the instruments say

    ** The point of building a repository rather than reasoning about one: the claim under test is
    about what the GATE reports, and a gate is only what it does on a tree. **
    """
    d = tempfile.mkdtemp()
    def g(*a):
        return subprocess.run(['git', '-C', d] + list(a), capture_output=True, text=True,
                              errors='replace')
    g('init', '-q', '-b', 'trunk')
    g('config', 'user.email', 'x@y.z')
    g('config', 'user.name', 'x')
    open(os.path.join(d, 'f'), 'w').write('0\n')
    g('add', '-A')
    g('commit', '-q', '-m', 'r1000 — the shared base')
    base = g('rev-parse', 'HEAD').stdout.strip()
    # ** the sandbox needs the same UPSTREAM the band check reads, or the check returns "no
    #   upstream" and PART 2 would pass on a rig where nothing was measured at all. **
    g('update-ref', 'refs/remotes/origin/main', base)
    for branch, nums, who in (('A', a_nums, 'A'), ('B', b_nums, 'B')):
        g('checkout', '-q', '-b', branch, base)
        for n in nums:
            # ** a file per line, so the merge below cannot CONFLICT.  *A conflicted merge leaves
            #   the other side out of the log, and PART 2 would then measure an unmerged history
            #   and report zero collisions -- which is what its first form did.* **
            open(os.path.join(d, f'{who}{n}'), 'w').write(f'{who}{n}\n')
            g('add', '-A')
            g('commit', '-q', '-m', f'r{n} — work done by line {who} at {n}')
    g('checkout', '-q', 'A')
    return d, g


def main():
    print()
    print('  H1 -- half a partition')
    print()

    # ============================================================ (1) the sentence
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE SENTENCE, READ FROM THE COMMIT THAT CARRIED IT')
    print('  ' + '=' * 74)
    was = git('show', f'{BEFORE}:corpus/check_revision_collisions.py')
    SENT = 'this\n    half removes the collisions this line can cause and no others'
    check(f'⓵ at {BEFORE} the gate\'s head claimed the half "removes the collisions this line can '
          'cause and no others"', SENT in was)
    check('⓵ᵇ and it printed the same sentence on every GREEN run, beside a count of zero',
          'this removes the collisions this line can cause and no others' in was)
    now = open(GATE, encoding='utf-8').read()
    check('⓵ᶜ and it is WITHDRAWN in place rather than quietly rewritten',
          'WITHDRAWN r3140' in now
          and 'THAT IS FALSE, AND IT IS FALSE BY\nARITHMETIC' in now
          and 'removes the collisions this line can cause and no others' not in
          now.split('WITHDRAWN r3140')[0])

    # ============================================================ (2) the sandbox
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ ONE HALF HELD: THE GATE IS GREEN AND THE COLLISION IS THERE')
    print('  ' + '=' * 74)
    # ** line A holds the band (evens only); line B is unconstrained and picks the same evens. **
    d, g = sandbox([1002, 1004], [1002, 1004])
    try:
        g('checkout', '-q', 'A')
        v = C.band_violations(root=d)
        assert v is not None, 'the sandbox has no upstream ref -- nothing was measured'
        # the merge that makes both sides visible, which is the only place `collisions` can look
        mr = g('merge', '--no-edit', '-m', 'merge B into A', 'B')
        assert mr.returncode == 0, f'the sandbox merge failed, so nothing was measured: {mr.stderr}'
        bad = C.collisions(root=d)
    finally:
        shutil.rmtree(d, ignore_errors=True)
    check(f'⓶ line A held to EVEN and line B unconstrained: the band check finds {len(v)} violation(s) '
          'on A -- A kept its half exactly', v == [])
    check(f'⛔ ⓶ᵇ *** AND THE COLLISIONS ARE THERE ANYWAY: {sorted(bad)} -- the gate is GREEN on the '
          'half it enforces while the thing the band exists to prevent has happened ***',
          sorted(bad) == ['r1002', 'r1004'])
    check('⓶ᶜ ⇒ so holding one part of a partition removes NO collision: every number A may still '
          'use remained fully available to B',
          len(bad) == 2 and v == [])

    # ============================================================ (3) both halves held
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭ BOTH HALVES HELD: THE COLLISION CANNOT BE CONSTRUCTED')
    print('  ' + '=' * 74)
    d2, g2 = sandbox([1002, 1004], [1003, 1005])
    try:
        g2('checkout', '-q', 'A')
        v2 = C.band_violations(root=d2)
        assert v2 is not None, 'the sandbox has no upstream ref -- nothing was measured'
        mr2 = g2('merge', '--no-edit', '-m', 'merge B into A', 'B')
        assert mr2.returncode == 0, f'the sandbox merge failed: {mr2.stderr}'
        bad2 = C.collisions(root=d2)
        # ** and the CONTROL that the sandbox can produce a collision at all -- otherwise PART 3
        #   would pass on a rig that simply cannot make one. **
        both = sorted(set([1002, 1004]) & set([1003, 1005]))
    finally:
        shutil.rmtree(d2, ignore_errors=True)
    check(f'⓷ A on EVEN and B on ODD: {len(bad2)} collision(s) -- {sorted(bad2) or "none"}',
          bad2 == {})
    check(f'⓷ᵇ and A still keeps its half: {len(v2)} violation(s)', v2 == [])
    check('⓷ᶜ ⌗ and PART 2 is the control for this one, not a separate experiment: the same rig, '
          'the same two lines, the same number of commits -- the ONLY difference is whether the '
          'second half is held, and it is the difference between two collisions and none',
          not both and len(bad2) == 0)

    # ============================================================ (4) the gate's own refusal
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE GATE NOW REFUSES THE WORD UNTIL BOTH HALVES ARE HELD')
    print('  ' + '=' * 74)
    check('⓸ the gate carries OTHER_HALF and it is SET, with the other line\'s own words',
          C.OTHER_HALF is not None and 'PARITY = 1' in C.OTHER_HALF)
    check('⓸ᵇ and when it is None the gate says "THE BAND IS A PROPOSAL, NOT A PREVENTION" and that '
          'half a partition removes NO collision -- so the reassurance cannot print again unheld',
          'THE BAND IS A PROPOSAL, NOT A PREVENTION' in now
          and 'if OTHER_HALF is None:' in now)
    # ** SEEDED: unset it and the gate must change what it says. **
    keep = C.OTHER_HALF
    try:
        C.OTHER_HALF = None
        import contextlib
        import io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            C.check_band()
        unheld = buf.getvalue()
    finally:
        C.OTHER_HALF = keep
    check('⓸ᶜ SEEDED: with OTHER_HALF unset the gate prints the proposal wording and not the '
          'prevention wording', 'PROPOSAL, NOT A PREVENTION' in unheld
          and 'prevention is real' not in unheld)
    check('⓸ᵈ and it is RESTORED -- verified, not trusted to the `finally`',
          C.OTHER_HALF == keep and C.OTHER_HALF is not None)

    # ============================================================ (5) testimony kept as testimony
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ EIGHT REPORTED, NONE MEASURABLE HERE, AND THE SPLIT IS PRINTED')
    print('  ' + '=' * 74)
    check(f'⓹ the eight are held in TESTIMONY, separate from BASELINE: {sorted(C.TESTIMONY)}',
          C.TESTIMONY == {'r3125', 'r3126', 'r3128', 'r3130', 'r3132', 'r3134', 'r3136', 'r3138'}
          and not (C.TESTIMONY & C.BASELINE))
    here = C.collisions()
    check(f'⓹ᵇ ⌗ and NONE of them is measurable in this tree -- it holds one side of each pair, so '
          f'{len(C.TESTIMONY & set(here))} of {len(C.TESTIMONY)} can be confirmed here.  *That is '
          'the fact ⓹ exists to keep from going quiet.*',
          not (C.TESTIMONY & set(here)))
    check('⓹ᶜ and the gate prints the confirmed/reported split on every run, with its source, and '
          'says that an entry still unconfirmed AFTER the merge must be struck',
          'def report_testimony' in now and 'on testimony' in now
          and 'must be struck rather than left' in now)
    subjects = git('log', '--format=%s', '--all').split('\n')
    mine = {r for r in C.TESTIMONY if sum(1 for x in subjects if x.startswith(r + ' ')) == 1}
    check(f'⓹ᵈ ⌗ and every one of the eight is one of THIS line\'s own revision numbers, each '
          f'carried by exactly one commit here: {len(mine)} of {len(C.TESTIMONY)}.  *That is what '
          'makes the report checkable at all -- the other line is naming numbers this tree owns, so '
          'the merge will either produce eight divergent pairs or falsify the report.*',
          mine == C.TESTIMONY)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a partition constrains a collision only when BOTH parts are held. **  *One')
    print('  part held alone removes nothing -- every number this line may still use remains fully')
    print('  available to the other -- and r3128 wrote that it "removes the collisions this line')
    print('  can cause and no others".  Withdrawn.*')
    print('  ⛔ ** Eight landed in the eight revisions of the turn that took the band, ** every one')
    print('     while the gate ran green and printed the reassurance.  *A gate that is green with')
    print('     a wrong sentence beside it is worse than a red one: the red is read, and the')
    print('     sentence is believed.*')
    print('  ⌗ ** What the half actually did was make the proposal enforceable on one side, ** which')
    print('     is what let the other line accept it in one step.  *That is its value, and it is')
    print('     not prevention.*  The gate now refuses the word until both halves are held.')
    print('  ⌗ ** And the eight are TESTIMONY, not measurement: ** this tree holds one side of each')
    print('     pair and can confirm none of them, which the gate prints every run.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
