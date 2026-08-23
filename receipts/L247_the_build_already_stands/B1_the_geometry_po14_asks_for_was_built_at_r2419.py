#!/usr/bin/env python3
r"""B1 -- `L-247`, `PO-14`: THE BUILD THE ROW ASKS FOR WAS DONE AT r2419, AND P14's "NOT BUILT"
SENTENCE WAS FALSE WHEN IT WAS WRITTEN.

** `PO-14` IN THE REGISTER: ** *"THE UNBUILT CHIRAL MEMBER ... **Build it.** ⇒ THE STEP (1, THE
BUILD): extend P11's polarised Gowdy--de Sitter leaf to the unpolarised case -- two propagating
modes, coupled nonlinearly."*  `THE_FRONTIER` prices it at **5 turns, flagged ⚠**, the only flagged
item of the three.

  ⇒ *** P11 `sec:unpolarized` DOES EXACTLY THAT, AND HAS SINCE r2419. ***

** ⛔ AND THE PAPER-LEVEL CLAIM IS NOT MERELY STALE. **  P14 says the unpolarised member *"is named
in the companion development and not built."*  That sentence was written at r3006b.
`sec:unpolarized` entered `dynamics_paper.tex` at r2419.
  ⇒ ** 587 revisions apart -- 825 commits, counted below rather than inferred -- and the built
    section was in the tree at the moment the sentence denying it was written. **  *Both files are read at both SHAs below rather than argued about.*

** ⌗ WHAT THIS DOES NOT DO: strike the row. **  *`PO-14`'s substance survives and is re-specified by
`L-246` -- what is unbuilt is the MATTER SECTOR on the chiral cut, not the cut.*

Run:  python3 receipts/L247_the_build_already_stands/B1_...py

Written r3099 (`L-247`).  Stated for reversal.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BUILD_SHA = 'c01f56c5bb061ae30483f2a1aeacd435c509a1f2'   # r2419
CLAIM_SHA = 'd929d6bf183de511f39f3ba534b374add98ac5c4'   # r3006b
fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


def at(sha, path):
    r = subprocess.run(['git', 'show', f'{sha}:{path}'], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout


print(__doc__)
print('=' * 78)
print('PART 1 -- WHAT THE ROW ASKS FOR, IN THE REGISTER\'S OWN WORDS')
print('=' * 78)
# ⛭⛭ ** THE PIN IS TO THE COMMIT THE ROW STOOD AT, NOT TO THE LIVE FILE -- AND THIS RECEIPT
# ** BROKE ITS OWN PIN ONCE BEFORE IT WAS WRITTEN THIS WAY. **  The finding below caused the row
# ** to be re-specified in the same revision, which moved the wording the check was quoting.
#   ⇒ *** THE PIN BROKE BECAUSE THE ARGUMENT WON.  So the historical wording is read at a SHA and
#       the current state is asserted separately -- the corpus's standing repair for this class. ***
PRE_SHA = 'c7c0fe2c3e4f94839312333254e9075198bb6164'    # origin/main before this revision's re-specification
reg_pre = at(PRE_SHA, 'THE_REGISTER.md')
fro_pre = at(PRE_SHA, 'THE_FRONTIER.md')
check('⓵ `THE_REGISTER` carried PO-14 as THE UNBUILT CHIRAL MEMBER at ' + PRE_SHA[:12],
      'THE UNBUILT CHIRAL MEMBER' in reg_pre)
check('⓵ᵇ and specified the step as extending the polarised leaf to the unpolarised case',
      'unpolarised' in reg_pre and 'two propagating modes' in reg_pre)
check('⓵ᶜ `THE_FRONTIER` priced it there as a BUILD at 5 turns, flagged -- the only flagged item '
      'of the three', 'PO-14' in fro_pre and 'BUILD' in fro_pre and '5 ⚠' in fro_pre)
# ** and the CURRENT state, asserted against the live files rather than assumed from the above **
reg = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8', errors='replace').read()
fro = open(os.path.join(ROOT, 'THE_FRONTIER.md'), encoding='utf-8', errors='replace').read()
check('⓵ᵈ ⛭ and the LIVE row now records the geometry as built and the Dirac sector as what is '
      'owed -- the finding landed rather than being only reported',
      'THE GEOMETRY IS BUILT' in reg and 'nobody has put' in reg)
check('⓵ᵉ and the live frontier row no longer prices an already-standing build at 5 turns',
      'RE-SPECIFIED r3099' in fro and '5 ⚠' not in fro.split('PO-14')[1].split('|')[8])

print()
print('=' * 78)
print('PART 2 -- WHAT P11 ALREADY CARRIES, READ OUT OF THE PAPER')
print('=' * 78)
p11 = open(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'), encoding='utf-8',
           errors='replace').read()
MARKS = [
    (r'\label{sec:unpolarized}', 'a section labelled sec:unpolarized'),
    ('restoring the second polarization', 'which restores the second polarisation'),
    ('wave map into the hyperbolic plane', 'and identifies the two polarisations as a wave map'),
    ('Gaussian curvature $-1$', 'into a target of Gaussian curvature -1'),
    ('determinant $-1$', 'with the exchanging map reversing orientation'),
    ('identity component does not reach', 'so it lies outside the identity component'),
    (r'c=R\,e^{2P}Q_t', 'and carrying the conserved twist c = R e^{2P} Q_t'),
    (r'c\mapsto-c', 'on which the parity acts as a sign flip'),
]
for needle, what in MARKS:
    check(f'⓶ P11 {what}', needle in p11)

print()
print('=' * 78)
print('PART 3 -- ⛔ THE TWO SHAs, AND THE ORDER THEY FALL IN')
print('=' * 78)
p11_build = at(BUILD_SHA, 'corpus/dynamics_paper.tex')
p11_claim = at(CLAIM_SHA, 'corpus/dynamics_paper.tex')
p14_claim = at(CLAIM_SHA, 'corpus/matter_sector_paper.tex')
print(f'    {BUILD_SHA[:12]}  r2419    P11 sec:unpolarized ADDED')
print(f'    {CLAIM_SHA[:12]}  r3006b   P14 "named ... and not built" WRITTEN')
check('⓷ the built section is present at the build commit', r'\label{sec:unpolarized}' in p11_build)
check('⓷ᵇ ⛔ and STILL present in the very tree where P14 wrote "not built"',
      r'\label{sec:unpolarized}' in p11_claim)
check('⓷ᶜ and P14 does carry that sentence at that commit',
      'named in the companion development and not' in p14_claim.replace('\n', ' '))
# ** the ancestry, checked rather than inferred from revision numbers in commit subjects **
anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BUILD_SHA, CLAIM_SHA],
                     cwd=ROOT, capture_output=True)
check('⓷ᵈ and the build commit is an ANCESTOR of the claim commit -- so the ordering is the '
      'repository\'s, not a reading of revision numbers', anc.returncode == 0)
n = subprocess.run(['git', 'rev-list', '--count', f'{BUILD_SHA}..{CLAIM_SHA}'],
                   cwd=ROOT, capture_output=True, text=True).stdout.strip()
print(f'    commits between them: {n}')

print()
print('=' * 78)
print('PART 4 -- WHAT IS ACTUALLY UNBUILT, WHICH IS NOT THE CUT')
print('=' * 78)
for s in [
    '· P11 builds the CHIRAL GEOMETRY.                                       ✔ r2419',
    '· P14 puts a Dirac spinor on the ACHIRAL geometry -> four classes.      ✔',
    '· Nobody has put a Dirac spinor on the CHIRAL geometry.                 ⛔ THIS is what is owed',
    '',
    '⇒ ** So the row is right about what matters and wrong about what is missing. **  `L-246`',
    '  shows the chiral cut is the ONLY place the fifth class could come from, which is why the',
    '  re-specification strengthens the item rather than dissolving it.',
    '',
    '⌗ ** AND P11\'s BUILD BOUNDS ITSELF, which is why "built" is not "finished": ** its receipt',
    '  says the explicit solution is the HOMOGENEOUS reduction and that the inhomogeneous',
    '  z-dependent Gowdy solutions "are the wave map\'s general Cauchy problem and are not solved',
    '  here."  *That is a real remainder and it is not this row\'s to close.*',
]:
    print('  ' + s)
rc = open(os.path.join(ROOT, 'receipts', 'P11_dynamics_paper',
                       'P11_unpolarized_gowdy_cut.py'), encoding='utf-8', errors='replace').read()
check('⓸ P11\'s own receipt bounds itself to the homogeneous reduction',
      'homogeneous reduction' in rc and 'not solved here' in rc)

print()
print('=' * 78)
if fails:
    print(f'  {len(fails)} check(s) FAILED')
    for m in fails:
        print(f'    - {m}')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print('  ⌷ *** The register\'s own warning, at the head of the file this row is filed in: "for')
print('      eighty revisions the answer to \'has this been done?\' was usually YES, and the')
print('      register did not know it.  Look before declaring a build."  This is that once more,')
print('      and the 5-turn ⚠ estimate was an estimate to build something already standing. ***')
print()
