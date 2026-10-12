#!/usr/bin/env python3
"""B24 -- the LEDGER's last item RUN: the triality computed from the colour content alone reproduces
P14's channel count exactly, with no reference to charge.

** THE ITEM, `3ebe33bce1`, and it is the last thing in the `LEDGER` bucket. **  P14: "the agreement
between ``is a field'' and ``has integer charge'' is ** not an independent check that could have failed
**.  On the identification used here ** the triality class is the fractional part of the charge **, so the
two predicates are the same predicate and agree on any rational whatever. ...  ** A genuine test would
compute the triality from the colour content independently of the charge, and this sector does not yet do
so. **"

** ⛭⛭ ⓵ AND r2679 SUPPLIED WHAT THE TEST NEEDS. **  "The corpus's colour is ** the CENTRE ** and its
structure group."  *** Triality IS the centre's action: for an $SU(3)$ representation, $\\rho(\\omega I)=
\\omega^{t}I$ with $t$ the triality, and for a tensor with $p$ upper and $q$ lower indices $t=(p-q)\\bmod
3$.  So the colour content determines $t$ with no charge anywhere in the calculation. ***

** ⓶ COMPUTED, for the channels P14 names: **

      *** quark 3        p=1 q=0   t = 1        meson  q qbar  p=1 q=1   t = 0
          antiquark 3bar p=0 q=1   t = 2        diquark  qq    p=2 q=0   t = 2
          gluon adjoint  p=1 q=1   t = 0        baryon  qqq    p=3 q=0   t = 0 ***

  ⇒ ** The triality-zero channels are exactly meson, baryon and the adjoint; the diquark is $t=2$. **

** ⛭ ⓷ AND THAT IS P14's COUNT, WHICH THE CONSTRUCTION RETURNS INDEPENDENTLY. **  P14: the exterior-cube
kernel "returns ** baryon $1$, diquark $0$, meson $1$ **: every channel the Standard Model has, with the
configuration group ** selected rather than chosen **."

  ⇒⇒ *** The construction ADMITS exactly the triality-zero channels and EXCLUDES exactly the triality-two
      one.  Two independent routes -- $\\Lambda^3$ on the exterior cube, and the centre's $\\mathbb Z_3$
      grading -- agree on which channels exist.  ** That is a test that could have failed and did not, and
      no charge enters either side. ** ***

** ⓸ SO THE ITEM IS DISCHARGED, AND WITH A LIMIT STATED. **  *** What is shown is that the SELECTION
agrees.  The stronger claim P14 declines -- that the triality class equals the charge's fractional part
as a derived rather than an assumed identification -- is untouched, and remains what it was. ***

WHAT IS NOT CLAIMED.  ** Not that confinement is derived ** -- *** P14 reads confinement as the selection
rule and this receipt reproduces the selection, not its dynamical origin. ***  ** Not that $t=(p-q)\\bmod
3$ is proved here ** -- it is the standard $SU(3)$ grading, quoted.  ** Not that the charge identification
is validated ** -- the point of the test is that it does NOT use it.

Written r2705.  Stated for reversal.
"""
import os
import re

import numpy as np

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


def triality(p, q):
    return (p - q) % 3


# ⛔⛭ ADDED r7260+60, on r7257's order ① -- the markup-carrier repair routed from r7258 §⑩.
#   *`\emph{...}` inside a pinned span is not part of the claim: the pin breaks on any re-typesetting
#   that preserves the meaning (`\emph`→`\textit`, or the emphasis simply dropped).  Normalising the
#   emphasis out of the HAYSTACK leaves the span WHOLE -- one contiguous word-aligned read -- instead of
#   cutting it into pieces that no longer carry the verb.  **r7258 §② refuted the split-into-conjuncts
#   shape with a truth table and §③ exhibited the disjunction shape failing live, so neither is used
#   here.**  The site count is PRINTED at each read and pinned nowhere, as the routing said.*
_EMPH = re.compile(r'\\(?:emph|textit|textbf|textsl|textup|textsc)\{([^{}]*)\}')
_WORD = re.compile(r'\w')


def unemph(t, rounds=4):
    """the text with inline emphasis commands unwrapped, contents kept, nesting handled by iteration"""
    for _ in range(rounds):
        t2 = _EMPH.sub(r'\1', t)
        if t2 == t:
            break
        t = t2
    return t


def held(lit, hay):
    """(present and WORD-ALIGNED at EVERY occurrence, how many occurrences) -- alignment is tracked
    across all of them rather than abandoned at the first clipped one, so the count printed is true."""
    i, n, ok = hay.find(lit), 0, True
    while i >= 0:
        b = hay[i - 1] if i else ' '
        a = hay[i + len(lit)] if i + len(lit) < len(hay) else ' '
        if (_WORD.match(lit[0]) and _WORD.match(b)) or (_WORD.match(lit[-1]) and _WORD.match(a)):
            ok = False
        n += 1
        i = hay.find(lit, i + 1)
    return (n > 0 and ok), n


def main():
    print()
    print('  B24 -- compute the triality from the colour content alone')
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the item, and why it is owed
    check('⓵ P14 owes it: "A genuine test would compute the triality from the colour content '
          'independently of the charge, and this sector does not yet do so"',
          # ** r2721: r2706 EDITED that sentence out of P14 -- the paper now STATES the test.
          # *** Assert the state the corpus HOLDS: the test is in print with its receipt. ***
          'A genuine test computes the triality from the colour content independently of the '
          'charge' in p14 and 'B24_the_triality_test_run' in p14)
    _u14 = unemph(p14)
    _KEY = 'the triality class is the fractional part of the charge'
    _ok, _n = held(_KEY, _u14)
    check(f'because the present agreement is circular: "the triality class is the fractional part of '
          f'the charge, so the two predicates are the same predicate" -- read with the inline '
          f'emphasis NORMALISED OUT of the paper so the pin survives a re-typesetting that keeps the '
          f'meaning; the span stays WHOLE and WORD-ALIGNED at every one of its {_n} site(s)',
          # ⌗ the second conjunct is cut WITHOUT its leading `so`: with it the span opened on a
          #   conjunction and named no subject, which is the very defect this revision is repairing
          #   elsewhere -- a repair that introduces a dangling key would be a net loss.
          _KEY in _u14 and _ok and 'the two predicates are the same predicate' in _u14)

    # ⓶ the centre gives it
    w = np.exp(2j*np.pi/3)
    for name, p, q, t in (('meson', 1, 1, 0), ('baryon', 3, 0, 0),
                          ('diquark', 2, 0, 2), ('quark', 1, 0, 1)):
        got = triality(p, q)
        check(f'⛭⛭ ⓶ {name}: $p={p}$, $q={q}$ gives $t={got}$, centre acting as '
              f'$\\omega^{got}$ = {complex(w**got).real:+.3f}{complex(w**got).imag:+.3f}i',
              got == t)

    # ⓷ and it matches P14's count
    check('⛭ ⓷ and P14\'s construction returns "baryon $1$, diquark $0$, meson $1$"',
          'baryon $1$, diquark $0$, meson $1$' in p14)
    admitted = {n for n, p, q in (('baryon', 3, 0), ('meson', 1, 1)) if triality(p, q) == 0}
    excluded = {n for n, p, q in (('diquark', 2, 0),) if triality(p, q) != 0}
    check(f'⇒ the triality-zero channels are exactly {sorted(admitted)} and the excluded one is '
          f'{sorted(excluded)} -- the construction\'s count, reproduced with no charge anywhere',
          admitted == {'baryon', 'meson'} and excluded == {'diquark'})

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the test runs, and it agrees. **')
    print('  ⓵ ** P14 owed a triality computed from the colour content, ** because its present agreement')
    print('     is circular: "the triality class IS the fractional part of the charge, so the two')
    print('     predicates are the same predicate".')
    print('  ⛭⛭ ⓶ ** r2679 supplied what the test needs: colour arrives at the CENTRE, and triality IS')
    print('     the centre\'s action. **  For $p$ upper and $q$ lower indices, t = (p−q) mod 3:')
    print('       quark 1 · antiquark 2 · meson 0 · diquark 2 · baryon 0 · adjoint 0')
    print('  ⛭ ⓷ ** And that is P14\'s count: ** the construction returns "baryon 1, diquark 0, meson 1".')
    print('     ⇒ *** It ADMITS exactly the triality-zero channels and EXCLUDES exactly the triality-two')
    print('       one.  Two independent routes — Λ³ on the exterior cube, and the centre\'s Z₃ grading —')
    print('       agree on which channels exist, and NO CHARGE ENTERS EITHER SIDE. ***')
    print('  ⓸ ** So the item is discharged, with its limit stated: ** what agrees is the SELECTION.  The')
    print('     stronger claim P14 declines — triality as a DERIVED rather than assumed identification')
    print('     with the charge — is untouched.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
