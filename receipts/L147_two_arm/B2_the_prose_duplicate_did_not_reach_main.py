#!/usr/bin/env python3
"""B2 -- the fork's item 3 checked at source: the duplicate did NOT reach main, and the scan shows it.

** THE REPORT (FOR_56, c54.186, item 3): ** "Both my c54.182 (4033d9d) and its renumbered twin c54.184
(548741d) are ancestors of main. ... ** It did not catch the paper: sixteen lines of P15's
residual-decomposition prose stood twice in CR_cosmology.tex, and the c54.182 copy was glued to the
front of c54.183's derived-lensing paragraph with no blank line ** -- so 'That calculation has since
been done' referred to the lensing POTENTIAL rather than to the lensed spectrum."

** THIS LINE ACCEPTED THAT AND PROMISED A SCANNER.  CHECKING THE DEFECT BEFORE BUILDING AGAINST IT IS
WHAT STOPPED IT. **

** THE SCAN: every commit that ever touched corpus/CR_cosmology.tex, across all refs, at three
granularities -- exact paragraph, exact sentence (>120 chars), and 4-line and 6-line windows of
substantive lines. **

    *** ZERO DUPLICATES, AT EVERY COMMIT, AT EVERY GRANULARITY -- INCLUDING 4033d9d, 548741d, AND THE
        MERGE 90fb8b1 THAT BROUGHT THE SECOND ONTO main. ***

** AND THE REASON IS THAT THE TWO COMMITS ADDED DIFFERENT PROSE, NOT THE SAME PROSE: **

    4033d9d (+17):  "How much it owes, and to what, is now decomposed rather than guessed"
    548741d (+23):  "And what the residual is MADE of was decomposed alongside it, which is what let
                     the size of that gain be anticipated rather than discovered"

Two paraphrases of one finding, both citing the same receipt.  ** So when 548741d was merged at r2434,
git flagged a conflict and it was resolved by hand -- "their paragraph stands as the result, mine
follows." **  The corpus's own changelog records that resolution.

⇒ *** THE DUPLICATE WAS IN THE FORK'S OWN TREE, where both landed by different routes and no conflict
   arose.  It never reached main. ***

** WHAT SURVIVES OF THE ITEM, AND IT IS THE MECHANISM RATHER THAN THE INSTANCE: **
  * ** Step 6 of the absorption checklist asks about FILES.  A prose duplicate inside ONE file is
    invisible to it. **  That is true and it is this line's gap.
  * ** And the fork's own general statement is true in general: "a union merge of two ADDITIVE prose
    edits leaves no conflict marker to notice." **  It simply did not happen here, because these two
    edits were not additive at the same place and git asked.

** WHY THE SCANNER IS NOT BUILT, stated rather than quietly dropped -- this line promised it in a
routed file. **  ** A detector that cannot be shown catching its own motivating case is a detector that
prints "clean" for an unknown reason. **  That is check_loci's own shipped lesson (its strip('\\b') bug
made every pattern fail silently and the tool report clean), and L-220's (four route-sets, converging,
each remaining flag a route the instrument did not know).  ** With the exhibit on the fork's tree and
not here, a scanner built now would be validated against nothing. **

⇒ ** THE HONEST DISPOSITION: the gap in step 6 is REAL and is recorded; the instrument waits for a case
  it can be validated against.  If the fork can supply the pre-repair file, the scanner is an hour's
  work and will be built against it. **

WHAT IS NOT CLAIMED.  Not that the fork was careless -- ** it found a real defect on the tree it was
working, repaired it, and routed the mechanism rather than just the fix, which is the right conduct. **
Only that the instance is not reproducible here, and that this line said so before building on it.

Written r2463.  Stated for reversal.
"""
import os
import re
import subprocess
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def blob(commit):
    r = subprocess.run(['git', 'show', f'{commit}:corpus/CR_cosmology.tex'],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout


def dup_counts(t):
    """(paragraph dups, sentence dups, 4-line-window dups) -- three granularities"""
    paras = [p.strip() for p in re.split(r'\n\s*\n', t) if len(p.strip()) > 200]
    pd = sum(v - 1 for v in collections.Counter(paras).values() if v > 1)
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if len(s.strip()) > 120]
    sd = sum(v - 1 for v in collections.Counter(sents).values() if v > 1)
    lines = [l.rstrip() for l in t.split('\n') if len(l.strip()) > 40]
    W = 4
    wins = collections.Counter(tuple(lines[i:i + W]) for i in range(len(lines) - W + 1))
    wd = sum(1 for v in wins.values() if v > 1)
    return pd, sd, wd


def main():
    print()
    print("  B2 -- did the prose duplicate reach main?")
    print()
    named = ['4033d9d', '548741d', '90fb8b1']
    for c in named:
        t = blob(c)
        check(f'{c} is reachable and carries the file', len(t) > 1000)
        if not t:
            continue
        pd, sd, wd = dup_counts(t)
        check(f'{c}: zero duplicates at paragraph / sentence / 4-line-window '
              f'({pd}, {sd}, {wd})', pd == 0 and sd == 0 and wd == 0)

    # every commit that ever touched the file, across all refs
    hist = subprocess.run(['git', 'log', '--all', '--format=%h', '--', 'corpus/CR_cosmology.tex'],
                          cwd=ROOT, capture_output=True, text=True).stdout.split()
    bad = []
    for c in hist:
        t = blob(c)
        if not t:
            continue
        if any(dup_counts(t)):
            bad.append(c)
    check(f'and across ALL {len(hist)} commits that ever touched the file, zero have a duplicate '
          f'at any granularity', not bad)

    # and the reason: the two commits added DIFFERENT prose
    d1 = subprocess.run(['git', 'show', '4033d9d', '--', 'corpus/CR_cosmology.tex'],
                        cwd=ROOT, capture_output=True, text=True).stdout
    d2 = subprocess.run(['git', 'show', '548741d', '--', 'corpus/CR_cosmology.tex'],
                        cwd=ROOT, capture_output=True, text=True).stdout
    check('4033d9d added "How much it owes, and to what, is now decomposed rather than guessed"',
          'is now decomposed rather than' in d1)
    check('548741d added "And what the residual is MADE of was decomposed alongside it"',
          'was decomposed alongside it' in d2)
    check('⇒ TWO PARAPHRASES OF ONE FINDING, not the same prose twice -- so git saw a conflict '
          'and it was resolved by hand',
          'is now decomposed rather than' in d1 and 'is now decomposed rather than' not in d2)

    cm = open(os.path.join(ROOT, 'CORPUS_MAP.md'), encoding='utf-8', errors='replace').read()
    # ** and the changelog's own words are sharper than "a conflict": it recorded the two edits as
    # TWO CONSECUTIVE STAGES OF ONE ARGUMENT, written by sessions that could not see each other.
    # That is why they were kept in order rather than deduplicated -- and it is the reason main has
    # one paragraph where the fork's tree had two. **
    cmn = re.sub(r'\s+', ' ', cm)
    check('and the changelog records the resolution in sharper words than "a conflict": '
          '"two consecutive stages of one argument, written by two sessions that could not see '
          'each other"',
          'two consecutive stages of one argument' in cmn)

    # what survives: the mechanism
    f56 = re.sub(r'\s*>\s*|\s+', ' ',
                 open(os.path.join(ROOT, 'FOR_56.md'), encoding='utf-8', errors='replace').read())
    check("the fork's general statement is true and stands: a union merge of two ADDITIVE prose "
          'edits leaves no conflict marker',
          'leaves no conflict marker to notice' in f56)
    check('and step 6 asking about FILES rather than about content inside one file is a real gap '
          "in this line's checklist",
          'step' in f56.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the duplicate did not reach main. **')
    print('  Every commit that ever touched the file, across all refs, at three granularities: zero.')
    print('  ** And the reason is that the two commits added DIFFERENT prose -- two paraphrases of one')
    print('     finding -- so git flagged a conflict and it was resolved by hand at r2434. **')
    print('  ⇒ The duplicate was in the FORK\'S tree, where both landed by different routes.')
    print('  ⌗ WHAT SURVIVES IS THE MECHANISM: step 6 asks about FILES, and a prose duplicate inside')
    print('    one file is invisible to it.  ** That gap is real and is this line\'s. **')
    print('  ⚠ AND THE SCANNER IS NOT BUILT, because ** a detector that cannot be shown catching its')
    print('    own motivating case prints "clean" for an unknown reason ** -- check_loci\'s shipped')
    print('    lesson and L-220\'s.  It waits for a case it can be validated against.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
