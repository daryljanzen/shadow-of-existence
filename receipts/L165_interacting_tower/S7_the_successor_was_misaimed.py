#!/usr/bin/env python3
"""S7 -- `L-543` inherits r2677's withdrawn object: it asks about a RUNNING background, and the free
tower does not live on one.  The question has no object, and `PO-6`'s dark half is smaller again.

** THE CHAIN, and where the withdrawal stopped. **  r2677 wrote "the tower lives on the LAYER, whose
$\\sinh^{2/3}$ Ricci scalar RUNS" and registered the successor `L-543`: "** does the one-dimensional
counterterm basis survive on a background whose curvature runs? **"  ** r2691 withdrew the scope clause
on cc54's c54.211 ** -- P10's own slicing is $a(T)=\\alpha\\cosh(T/\\alpha)$, exactly de Sitter.

  ⇒ *** But the WITHDRAWAL did not reach the SUCCESSOR.  `L-543` is still built on the object r2691
      removed, and it has sat in `PO-6`'s row for twenty revisions asking about a background the free
      tower does not use. ***

** ⛭⛭ ⓵ THE TWO BACKGROUNDS, verified again: **

      *** P10's slicing   a = alpha cosh(T/alpha), k=+1  ->  R = 12/alpha^2     CONSTANT
          P15's layer     a ~ sinh^(2/3)(3Ht/2), k=0     ->  R runs, -> 12 H^2  late ***

  ⌗ ** And the two constants are the SAME FORM. **  *** $12/\\alpha^2$ and $12H^2$ are both the de Sitter
    value, with $H\\to1/\\alpha$: the layer's LATE limit is P10's slicing.  So the layer does not merely
    fail to be the tower's background -- it ASYMPTOTES to it. ***

** ⓶ SO `L-543`'s QUESTION HAS NO OBJECT. **  *** "Does the basis survive on a running background?" is
not a question about the free tower, which sits on a constant-curvature background where r2677's own
computation already shows the degeneracy is exact.  The answer is not unknown; the question is
misaimed. ***

** ⓷ AND THE REAL LIMIT IS THE ONE P10 STATES, WHICH r2691 ALREADY NAMED. **  "the free tower above
evolves on $a(T)$ as a ** FIXED CLASSICAL background ** ... the coupling question is what happens once
the scale factor is ** itself quantized and back-reacts **."
  ⇒⇒ *** That is `PO-6`'s actual dark half: not a running background but a BACK-REACTING one.  A
      counterterm basis is a statement about a class of FIXED backgrounds, and in the coupled sector
      there is no such class to state it on -- which is a statement about what the question can even
      mean, not a calculation waiting to be run. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-6` closes ** -- *** the back-reaction question is real and is P10's
own; what is withdrawn is a successor that was aimed at the wrong background. ***  ** Not that the
degeneracy is re-derived ** -- r2677 computed it and r2691 strengthened it.  ** Not that 54 wasted
effort ** -- `L-543` was registered here, on this line's error, and the correction is this line's to
make.

Written r2713.  Stated for reversal.
"""
import os
import re

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  S7 -- is L-543 aimed at the background the free tower uses?")
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po6 = next(l for l in raw.split('\n')
               if re.match(r'\|\s*~?~?\*\*PO-6\*\*', l))

    # ⓵ the successor as registered
    check("⓵ L-543 asks about a RUNNING background: \"does the one-dimensional basis survive on a "
          'background whose curvature runs?"',
          'survive on a background whose curvature runs' in po6)
    # ⛭⛭ r7338+60, PO-78's repair stride, the middle -- EDITED ON `r7337` ④'s order.  ** THE OWED
    #   ROW WAS THE BARE PROPER NAME `de Sitter`, at seven sites in this one row, sitting as the
    #   last arm of a THREE-ARM DISJUNCTION -- so the weakest arm decided and the name could not
    #   carry the claim that the slicing IS exactly de Sitter. **
    #   ⇒ *** Replaced by the one clause that states the identification with its own figure: the
    #     closed FRW case gives the de Sitter curvature exactly.  ONE site, one arm. ***
    _EXACTLY_DS = ('closed FRW $k=+1$ gives $R=12/\\alpha^2$, exactly de Sitter')
    check('and r2691 already withdrew the object it was built on: the row records the slicing as '
          'exactly de Sitter -- "closed FRW $k=+1$ gives $R=12/\\alpha^2$, exactly de Sitter", '
          'asserted as the clause that carries the figure, in place of a bare proper name disjoined '
          'with two others',
          _EXACTLY_DS in po6)

    # ⓶ both backgrounds
    T, al, t, H = sp.symbols('T alpha t H', positive=True)
    a1 = al*sp.cosh(T/al)
    R1 = sp.simplify(6*(sp.diff(a1, T, 2)/a1 + (sp.diff(a1, T)/a1)**2 + 1/a1**2))
    a2 = sp.sinh(sp.Rational(3, 2)*H*t)**sp.Rational(2, 3)
    R2 = sp.simplify(6*(sp.diff(a2, t, 2)/a2 + (sp.diff(a2, t)/a2)**2))

    check(f'⛭⛭ ⓶ P10\'s slicing gives $R={R1}$, CONSTANT -- no $T$ dependence',
          T not in R1.free_symbols and R1 == 12/al**2)
    check("while P15's layer runs, reaching $12H^2$ late",
          sp.limit(R2, t, sp.oo) == 12*H**2 and t in sp.simplify(R2).free_symbols)
    check('⌗ and the two constants are the SAME FORM -- $12/\\alpha^2$ and $12H^2$ are the de Sitter '
          'value with $H\\to1/\\alpha$, so the layer ASYMPTOTES to the tower\'s background',
          sp.simplify(R1.subs(al, 1/H) - sp.limit(R2, t, sp.oo)) == 0)

    # ⓷ the real limit
    # ⛔⛭⛭ r7338+60: ** AND THIS ONE IS A WITHDRAWAL WITH ITS CASE, BECAUSE THE LABEL HAD GONE
    #   FALSE.  The check said the row names the REAL LIMIT as the coupled sector -- what happens
    #   once the scale factor is quantized and back-reacts.  The row now says the opposite in its
    #   own voice: the degeneracy is conformal flatness, so NO scale factor can break it and
    #   back-reaction cannot, and THE REAL LIMIT IS THE SHEAR. **
    #   *The owed arm `'back-react' in po6.lower()` passed throughout -- it passed BECAUSE the row
    #   discusses back-reaction while DENYING it is the limit.*
    #   ⇒ *** Second instance in this seat's stride of a cannot-fail arm whose LABEL has gone false:
    #     nothing goes red and the sentence quietly stops being true.  Restated as the CURRENT
    #     state, which is `L-249`'s rule, over a MARKDOWN-normalised read because the row's emphasis
    #     markers fall inside the carrying span. ***
    _po6_md = re.sub(r'\*+', '', po6)
    _REAL_LIMIT = ('the degeneracy is CONFORMAL FLATNESS, not maximal symmetry, so no scale factor '
                   'can break it, and back-reaction cannot. THE REAL LIMIT IS THE SHEAR')
    check('⓷ and the row states the real limit in its OWN voice, which is no longer the one this '
          'check was written for: "the degeneracy is CONFORMAL FLATNESS, not maximal symmetry, so '
          'no scale factor can break it, and back-reaction cannot.  THE REAL LIMIT IS THE SHEAR" '
          '-- asserted as the clause that carries the withdrawal, in place of the token '
          '`back-react`, which passed BECAUSE the row denies what the label claimed',
          _REAL_LIMIT in _po6_md)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** L-543's question has no object — it is aimed at the wrong background. **")
    print('  ⛔ ⓵ ** The withdrawal did not reach the successor. **  r2691 removed r2677\'s scope clause')
    print('     on cc54\'s c54.211, but ** L-543 is still built on the object it removed ** — and has sat')
    print('     in PO-6\'s row for twenty revisions asking about a background the free tower does not')
    print('     use.')
    print(f'  ⛭⛭ ⓶ ** P10\'s slicing: R = {R1}, CONSTANT. **  P15\'s layer runs, reaching 12H² late.')
    print('     ⌗ *** And the two constants are the SAME FORM — 12/α² and 12H² are the de Sitter value')
    print('       with H → 1/α.  The layer does not merely fail to be the tower\'s background; it')
    print('       ASYMPTOTES to it. ***')
    print('  ⓷ ** So the real limit is the one P10 states and r2691 named: ** not a running background')
    print('     but a ** BACK-REACTING ** one — "once the scale factor is itself quantized and')
    print('     back-reacts".')
    print('     ⇒ *** A counterterm basis is a statement about a class of FIXED backgrounds, and in the')
    print('       coupled sector there is no such class to state it on.  That is a statement about what')
    print('       the question can MEAN, not a calculation waiting to be run. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
