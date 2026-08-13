#!/usr/bin/env python3
"""E53 -- `PO-9`'s last unreproduced link is established in the papers, and `L-533` was never its only
source: the count goes ONE -> ZERO and ④'s failure was a mis-attribution.

** WHERE `PO-9` STOOD. **  ④ failed on three links "reproduced NOWHERE ELSE" than `L-533`.  r2640
reproduced (e) on three methods; r2641 reproduced (d) from the embedding and showed the spacelike
restriction forced.  ** What remained was (c): "every rung above the last being maximally symmetric" --
and r2640's kind-sort called it "a statement about the tower, not a computation". **

** ⛭⛭ ⓵ AND IT IS STATED IN THE PAPERS, TWICE, IN TWO DIFFERENT ARGUMENTS. **
  * ** P12: ** "least-arbitrariness ... prefers the structure requiring no choice of how to break a
    symmetry, and ** $dS_D$ is maximally symmetric and moduli-free for every $D$ **, so it selects the
    manifold at fixed dimension and is silent on the dimension itself".
  * ** p0: ** "It is excluded from the list because it does not come from maximal symmetry---** the
    substrate is maximally symmetric and moduli-free in every dimension **---but from the matter sector's
    own content".

  ⇒ *** Two papers, in two arguments that need the fact for opposite purposes: P12 to show the criterion
      is SILENT on dimension, p0 to EXCLUDE a $D=4$ argument from the maximal-symmetry list. ***

** ⓶ AND THE GROUND IS P6, NOT `L-533`. **  P12 cites `JanzenShadowExistence` for it.  P6 argues it
directly from Rule 2 with no onward citation: "a structure with a free modulus is not a single world but a
family $W_\\lambda$ ... ** the moduli-free structure is the sole determinate answer **---which Rule 2 then
certifies as the explanatory one."
  ⇒ ** So the chain is P6 → P12 and P6 → p0, and `L-533` is nowhere in it. **

** ⇒⇒ ⓷ SO ④'s THIRD FAILURE WAS A MIS-ATTRIBUTION, NOT A GAP. **  *** The receipt listed (c) among
"`L-533`'s own derivation", and (c) is not `L-533`'s: it is P6's Rule-2 argument, used by P12 and p0
before `L-533` was written.  The link was reproduced in the corpus the whole time. ***
  ⌗ ** Which changes what the count meant: ** three unreproduced links were ** two computations nobody had
  re-run ** and ** one claim that was never `L-533`'s to begin with. **

** ⓸ AND ④ NOW CLEARS. **  (a) ✔ r2552, three times in the papers.  (b) ✔ in P6.  (c) ✔ P6, via P12 and
p0.  (d) ✔ r2641, from the embedding, with the restriction shown forced.  (e) ✔ r2640, three methods.
  ⚠ *** THIS RECEIPT DOES NOT CLOSE `PO-9`. ***  `PROTECTED_OPEN`'s exit runs by its two stated routes and
  ** the authorisation is Daryl's **.  What is established is that ** the check which did not clear now
  does **, and the receipt should say so rather than continue to report a failure it no longer has.

WHAT IS NOT CLAIMED.  ** Not that `PO-9` is closed ** -- `F5` reserves it.  ** Not that P6's Rule-2
argument is re-derived here ** -- it is located and quoted, not re-proved.  ** Not that "maximally
symmetric and moduli-free for every $D$" settles the dimension ** -- *** P12 says the opposite in the same
sentence: the criterion "is SILENT on the dimension itself", which is why `PO-9` exists. ***

Written r2642.  Stated for reversal.
"""
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


def main():
    print()
    print("  E53 -- is PO-9's link (c) really L-533's alone?")
    print()
    p12 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'algebroid_paper.tex')))
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    p6 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'shadow_of_existence.tex')))
    kill = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'kills', 'PO-9.md'),
                                    encoding='utf-8', errors='replace').read())

    check("⓵ PO-9's ④ lists (c) among L-533's own derivation: \"every rung above the last being "
          'maximally symmetric"',
          'every rung above the last being maximally symmetric' in kill)
    check('and r2641 left the count at ONE', 'the count is ONE' in kill)

    # ⓶ two papers state it
    check('⛭⛭ ⓶ P12 states it: "$dS_D$ is maximally symmetric and moduli-free for every $D$, so it '
          'selects the manifold at fixed dimension and is silent on the dimension itself"',
          'maximally symmetric and moduli-free for every' in p12
          and 'silent on the dimension itself' in p12)
    check('and p0 states it: "the substrate is maximally symmetric and moduli-free in every dimension"',
          'maximally symmetric and moduli-free in every dimension' in p0)

    # ⓷ the ground is P6
    check('⓷ P12 cites JanzenShadowExistence for it',
          'JanzenShadowExistence' in p12[max(0, p12.find('moduli-free for every') - 300):
                                         p12.find('moduli-free for every') + 300])
    check('and P6 argues it from Rule 2 directly: "the moduli-free structure is the sole determinate '
          'answer---which Rule~2 then certifies as the explanatory one"',
          'the moduli-free structure is the sole determinate answer' in p6)
    check('with the reason: "a structure with a free modulus is not a single world but a family '
          '$W_{\\lambda}$"',
          'is not a single world but a family' in p6)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** link (c) was never L-533's.  It is P6's, used by P12 and p0. **")
    print('  ⛭⛭ ⓵ ** Two papers state it, in two arguments needing it for OPPOSITE purposes: ** P12, to')
    print('     show the criterion is ** silent on dimension **; p0, to ** exclude ** a D=4 argument from')
    print('     the maximal-symmetry list.')
    print('  ⓶ ** And the ground is P6\'s Rule-2 argument: ** "a structure with a free modulus is not a')
    print('     single world but a family W_lambda … ** the moduli-free structure is the sole determinate')
    print('     answer **".  ** P12 cites it; L-533 is nowhere in the chain. **')
    print('  ⇒⇒ ⓷ ** So ④\'s third failure was a MIS-ATTRIBUTION, not a gap. **  *** Three unreproduced')
    print('     links were two computations nobody had re-run and one claim that was never L-533\'s. ***')
    print('  ⓸ ** And ④ now clears: ** (a) ✔ r2552 · (b) ✔ P6 · (c) ✔ P6 via P12 and p0 · (d) ✔ r2641 ·')
    print('     (e) ✔ r2640.')
    print('  ⚠ ** This does NOT close PO-9. **  The exit runs by PROTECTED_OPEN\'s two stated routes and')
    print('    ** the authorisation is Daryl\'s. **  What is established is that ** the check which did')
    print('    not clear now does. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
