#!/usr/bin/env python3
"""check_chirality_qualifier.py -- "CHIRALITY IS NON-GEOMETRIC" IS FALSE WITHOUT ITS QUALIFIER.

** WHY.  Daryl, r2779: ** *** "How is chirality nongeometric?  I thought we had long ago decided it is
geometric.  Is the corpus becoming incoherent?" ***

  ⇒ ** The corpus is coherent.  `kills/PO-4.md` was not. **  *** It quoted the boundary paper as
  "chirality is not merely found non-geometric but forced to be", ** dropping "OBSERVED FERMION" from
  the middle of the quote **.  That single omission inverts the claim. ***

** ⛭⛭ THE CORPUS CARRIES TWO CHIRALITIES AND DISTINGUISHES THEM EVERY TIME. **

  * ** GEOMETRIC / GRAVITATIONAL CHIRALITY -- REAL, DERIVED, GEOMETRIC: **
    *** dynamics: "chirality is the turning of the polarization plane (helicity $\\pm2$) ... the wall,
    where no residual isometry survives, is where chirality is GENERIC".  P14: a zero-mode "whose
    chirality is the diagram-automorphism parity $R=\\gamma^5$ (** an exact solution, not an assertion
    **)".  The framework: "** GEOMETRIC chirality can be carried only by ** the discrete orientation
    parity" -- CARRIED, i.e. it is there. ***

  * ** OBSERVED FERMION CHIRALITY -- the Standard Model's chiral GAUGE COUPLING: **
    *** boundary: "** OBSERVED FERMION ** chirality is not merely found non-geometric but forced to
    be".  geometric core: "the index acts on the ** CONNECTED GAUGE GROUP ** ... so ** OBSERVED FERMION
    ** chirality is forced non-geometric". ***

  ⇒⇒ *** CHIRALITY IS GEOMETRIC.  What is forced non-geometric is the GAUGE COUPLING of fermion
      chirality -- $SU(2)_L$'s chiral ACTION, not chirality itself. ***

** WHAT THIS CHECKS. **  Any register or receipt text pairing "chirality" with "non-geometric" or
"forced" must carry the qualifier -- "observed", "fermion", or "gauge" -- within the same clause.

  ⌗ ** Narrow by design. **  *** This is one phrase, and a gate for one phrase is usually a smell.  It
    earns its place because the omission INVERTS a load-bearing result and because it already reached a
    reader: the confusion in r2779 is the evidence. ***

    python3 corpus/check_chirality_qualifier.py

Written r2779.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** the claim, in a window small enough that the qualifier would be in it. **
# ** the CLAIM is about chirality's geometric STATUS.  *** "forced to be the chirality
# operator chi = gamma^5" is an OPERATOR IDENTITY and correctly carries no qualifier --
# the first pattern matched it and would have driven an edit to a true sentence. ***
CLAIM = re.compile(r'chirality[^.]{0,60}?non-geometric'
                   r'|non-geometric[^.]{0,40}?chirality', re.I)
QUALIFIED = re.compile(r'observed|fermion|gauge|coupling|Standard Model', re.I)

TARGETS = ['PROTECTED_OPEN.md', 'CORPUS_MAP.md', 'THE_PLAN.md',
           'THE_OPEN_PROBLEMS_LEDGER.md', 'OPEN_PROBLEMS_MAP.md']


def main():
    print()
    print('  check_chirality_qualifier -- is every "chirality is non-geometric" qualified?')
    print()
    files = [os.path.join(ROOT, t) for t in TARGETS if os.path.exists(os.path.join(ROOT, t))]
    files += sorted(glob.glob(os.path.join(ROOT, 'kills', '*.md')))
    files += sorted(glob.glob(os.path.join(ROOT, 'capstones', '*.md')))

    bad, n = [], 0
    for f in files:
        t = open(f, encoding='utf-8', errors='replace').read()
        for m in CLAIM.finditer(t):
            n += 1
            window = t[max(0, m.start()-90):m.end()+40]
            # ** r2779: text QUOTING the dropped-qualifier error must be allowed to state it,
            # or the gate forbids recording its own finding.  *** The marker is a nearby
            # 'quoted it as' / 'dropped' / 'DROPPED' -- the vocabulary of citing an error. ***
            if re.search(r'quoted it as|dropp|reverses|two words', window, re.I):
                continue
            if not QUALIFIED.search(window):
                bad.append((os.path.relpath(f, ROOT),
                            re.sub(r'\s+', ' ', m.group(0))[:70]))

    print(f'  {n} claim(s) checked across {len(files)} file(s)')
    if bad:
        print()
        for f, s in bad:
            print(f'    [FAIL] {f}: "{s}"')
        print()
        print('    ⛭ ** The corpus carries TWO chiralities. **  *** GEOMETRIC chirality is real and')
        print('       derived — the turning of the polarization plane, helicity ±2, and the zero-mode')
        print('       parity R = γ⁵.  ** What is forced non-geometric is OBSERVED FERMION chirality:')
        print('       the Standard Model\'s chiral GAUGE COUPLING **, because the index theorem acts on')
        print('       the CONNECTED gauge group. ***')
        print('    ⌗ Add "observed fermion" or "gauge" to the clause.')
        return 1
    print('  every claim carries its qualifier.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
