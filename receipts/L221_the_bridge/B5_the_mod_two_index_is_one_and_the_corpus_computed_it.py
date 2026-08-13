#!/usr/bin/env python3
"""B5 -- the mod-2 index has a VALUE and the corpus computed it without naming it: $n_+\\bmod 2=1$, and
P14's "three and zero lying in different parity classes" IS that statement.

** WHERE THIS ARRIVES. **  Five turns on `PO-5`: r2568 named the object, r2604 found the prerequisite
realised on the built modes, r2605/r2606 got the operator wrong and then right, r2607 established that
** the RADIAL operator carries a REAL structure ($A=\\sigma_z\\circ\\overline{\\;}$, $A^2=+1$, preserving
the counted eigenspace) ** -- so the mod-2 index's CONDITION is met.
  ⇒ ** What remained was its VALUE. **  *** And the corpus already has it. ***

** ⓵ P14 STATES THE COUNT AND ITS INVARIANCE IN ONE SENTENCE. **  "that holonomy acts on the walls'
chiralities, which are the $\\sigma_y$ eigenvalues of Proposition~\\ref{prop:wall}, ** changing their signs
only in pairs **: the observed configuration is therefore the unique member of its orbit with all three
walls at one chirality, and ** $n_-$ cannot be reached from $n_+=3$ by any number of loops, three and
zero lying in different parity classes **."

** ⛭⛭ ⓶ AND THAT IS A MOD-2 INDEX, COMPUTED. **  Enumerating the orbit of $(+,+,+)$ under pair-flips:

      *** orbit = {(+,+,+), (+,-,-), (-,+,-), (-,-,+)} -- FOUR of the eight states
          n_+ over the orbit = {1, 3}
          n_+ mod 2 = 1, throughout ***

  ⇒ ** $(-,-,-)$ has $n_+=0$, parity $0$, and is NOT in the orbit. **  *** The pair-flip group is the
      even subgroup of $(\\mathbb{Z}_2)^3$; its orbits are exactly the two parity classes; and the
      invariant that separates them is $n_+\\bmod 2$. ***

** ⇒⇒ SO THE MOD-2 INDEX OF THE THREE-WALL CONFIGURATION IS $1$, AND EVERY PIECE OF THAT WAS ALREADY IN
THE CORPUS. **  The condition (r2607, the radial operator's real structure), the count ($n_+=3$,
$n_-=0$), and the invariance ("changing their signs only in pairs", "different parity classes").
  ⌗ *** What was absent is the NAME -- `mod 2`, `Witten anomaly`, `eta invariant` still at zero across
      seventeen papers -- and naming it is what makes the generation count's stability an INDEX-THEORETIC
      statement rather than an observation about an orbit. ***

** ⓷ AND IT UPGRADES P14's OWN WEIGHT-MARKING. **  P14 states index-theoretic stability "** at traced
weight **", marking the Atiyah--Singer statement as ** traced rather than computed **.
  ⇒ *** The mod-2 invariant is not traced.  It is an orbit computation on a three-element set, done
      here, and it gives the stability P14 wanted at a weight it did not claim. ***
  ⚠ ** It is not Atiyah--Singer. **  *** The integer index remains traced; what is computed is the
      $\\mathbb{Z}_2$ one, which is a weaker invariant and a stronger warrant. ***

WHAT IS NOT CLAIMED.  ** Not that the mod-2 index equals the generation count **: it is $1$ and the count
is $3$; the invariant says the count is ODD and cannot be moved to an even one, not that it is three.
** Not that this delivers `PO-5`'s bridge ** -- r2568's standing limit holds, *** a $\\mathbb{Z}_2$
invariant can obstruct or permit but cannot by itself deliver four states. ***  ** Not that the holonomy's
pair-flip property is re-derived here ** -- it is P14's, cited and used.

Written r2608.  Stated for reversal.
"""
import itertools
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def orbit(start):
    """Closure of `start` under sign-flips of PAIRS of walls -- P14's stated holonomy action."""
    seen, frontier = {start}, {start}
    while frontier:
        nxt = set()
        for st in frontier:
            for i, j in itertools.combinations(range(len(st)), 2):
                s = list(st)
                s[i] *= -1
                s[j] *= -1
                if tuple(s) not in seen:
                    seen.add(tuple(s))
                    nxt.add(tuple(s))
        frontier = nxt
    return seen


def main():
    print()
    print('  B5 -- what is the mod-2 index of the three-wall configuration?')
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the corpus states the count, the action, and the conclusion
    check('⓵ P14 states the count: "$\\dim\\ker_+=3$, $\\dim\\ker_-=0$, the net chirality a '
          '$\\gamma^5$-graded index"',
          '\\dim\\ker_+=3' in p14.replace(' ', '')
          and '\\dim\\ker_-=0' in p14.replace(' ', ''))
    check('and the holonomy action: it acts on the walls\' chiralities, "changing their signs only in '
          'pairs"', 'changing their signs only in \\emph{pairs}' in p14)
    check('and the conclusion: "three and zero lying in different parity classes"',
          'three and zero lying in different parity classes' in p14)
    check("and that the chiralities are prop:wall's $\\sigma_{y}$ eigenvalues",
          "which are the $\\sigma_{y}$ eigenvalues of Proposition" in p14)

    # ⓶ the orbit computation
    orb = orbit((1, 1, 1))
    check(f'⛭⛭ ⓶ the orbit of (+,+,+) under pair-flips has {len(orb)} of 8 states', len(orb) == 4)
    check('and (-,-,-) is NOT in it -- so P14\'s "cannot be reached by any number of loops" holds',
          (-1, -1, -1) not in orb)
    nplus = {sum(1 for x in s if x > 0) for s in orb}
    check(f'and $n_+$ over the orbit is {sorted(nplus)}', nplus == {1, 3})
    par = {n % 2 for n in nplus}
    check(f'⇒⇒ SO $n_+\\bmod 2 = {par.pop() if len(par)==1 else par}$ THROUGHOUT -- a mod-2 invariant '
          'with value 1', {n % 2 for n in nplus} == {1})
    check('and the two parity classes are exactly the two orbits: 4 + 4 = 8',
          len(orb) + len(orbit((-1, -1, -1))) == 8)

    # ⓷ the weight it upgrades
    check('⓷ P14 marks index-theoretic stability "at traced weight" and the Atiyah--Singer statement as '
          '"traced rather than computed"',
          'traced weight' in p14 and 'traced rather than computed' in p14)

    # the name is still absent
    allp = ' '.join(body(f) for f in
                    [os.path.join(ROOT, 'corpus', x) for x in os.listdir(os.path.join(ROOT, 'corpus'))
                     if x.endswith('.tex') and not x.startswith('appendix_receipts')])
    for k in ('mod 2', 'mod-two', 'Witten anomaly', 'eta invariant'):
        check(f'⌗ and the NAME is still absent: "{k}" appears zero times across the papers',
              len(re.findall(re.escape(k), allp, re.I)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the mod-2 index is 1, and the corpus computed it without naming it. **')
    print('  ⓵ ** P14 states all three pieces: ** the count ($n_+=3$, $n_-=0$), the holonomy action')
    print('     ("changing their signs only in pairs"), and the conclusion ("three and zero lying in')
    print('     different parity classes").')
    print('  ⓶ ** The orbit of (+,+,+) under pair-flips is FOUR of eight states, $n_+ \\in \\{1,3\\}$,')
    print('     and $n_+ \\bmod 2 = 1$ throughout. **  (-,-,-) has parity 0 and is unreachable.')
    print('     ⇒ ** The pair-flip group is the even subgroup of (Z2)^3; its orbits ARE the two parity')
    print('       classes; and $n_+ \\bmod 2$ is the invariant that separates them. **')
    print('  ⓷ ** And it upgrades P14\'s own weight-marking: ** that paper states index-theoretic')
    print('     stability "at traced weight". ** The mod-2 invariant is not traced -- it is an orbit')
    print('     computation on a three-element set. **')
    print('  ⚠ ** It is NOT Atiyah--Singer: ** the integer index remains traced.  What is computed is the')
    print('    Z2 one -- ** a weaker invariant and a stronger warrant. **')
    print('  ⚠ And NOT claimed: that the index equals the generation count (it is 1 and the count is 3 --')
    print('    the invariant says the count is ODD and immovable, not that it is three), nor that a Z2')
    print('    invariant delivers four states.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
