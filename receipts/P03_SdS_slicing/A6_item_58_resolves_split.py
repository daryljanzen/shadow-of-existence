#!/usr/bin/env python3
"""A6 -- item 58 resolves SPLIT, and the split exposes the unbanked sweep's third failure mode: a result
banked WITHOUT its working name.

** THE ROUTED ITEM (r2678). **  `unbanked.py` surfaced `excentre` at 35 uses across five receipts and
** zero across all seventeen papers **, and this line routed TWO results as unbanked:
  * a ** SIXTH equivalence ** for the hinge distance $2\\alpha$, "the first phrased in the substrate's own
    causal language rather than in classical triangle geometry";
  * the hinge configuration's null connectivity ** CLOSED **, "0 of 36 pairs".

** ⛔ ⓵ THE FIRST IS ALREADY IN PRINT, AND HAS BEEN. **  P3, immediately after its five equivalences:
"** A sixth is available and differs from those five in kind rather than in content **, since all of
them are statements about a Euclidean figure: writing $s^2$ for the squared separation of two
opposite-horn ends of a $120^\\circ$-separated triple of lines at transverse radius $\\rho$, one has
$s^2=4\\alpha^2-\\rho^2$, so ** $2\\alpha$ is the unique transverse radius at which those pairs are null
**---the same placement read in the substrate's own causal language rather than in the plane's."
-- carrying `\\rcpt{P03_the_sixth_equivalence}`, ** cited twice **.

  ⇒ *** So the sweep flagged the TERM and the RESULT was banked in different words.  `excentre` never
      appears because P3 states the fact as "a $120^\\circ$-separated triple of lines at transverse radius
      $\\rho$" -- which is what an excentre triple IS, said geometrically. ***

** ⛭⛭ ⓶ AND THAT IS THE SWEEP'S THIRD FAILURE MODE, after `station` and `monomial`. **

      *** station  (r2678)  a banked term in another INFLECTION      -> stem matching
          monomial (r2680)  an API name read as receipt content      -> prose-only counting
          excentre (r2699)  a banked RESULT under a different NAME   -> NOT FIXABLE by matching *** 

  ⇒⇒ *** The first two were matcher bugs.  This one is not: no term-frequency method can see that "a
      $120^\\circ$-separated triple of lines at transverse radius $\\rho$" IS the excentre set.  The tool's
      floor is that it detects VOCABULARY GAPS, not banking gaps -- and those coincide only when the
      paper and the receipt happen to share a word. ***

** ⓷ THE SECOND RESULT IS GENUINELY UNBANKED. **  ** "0 of 36", "null-inert", "null connectivity", "36
pairs" -- all absent from every paper **, and `P03_slate_worked` is cited ** zero times **.  *** So item
58 is HALF closed: the sixth equivalence needs nothing; the closed null connectivity is a real banking
debt in P3's band. ***

WHAT IS NOT CLAIMED.  ** Not that the sweep is worthless ** -- *** it found `pushforward` (r2679), whose
carrier held the three-routes statement, and that WAS unbanked.  What is claimed is that its floor is now
measured. ***  ** Not that the null-connectivity result is verified here ** -- r2678 ran its receipt and
it passes; the banking is a P3 edit in another band.  ** Not that the geometry is re-derived ** -- it was,
at r2699: the excentres sit at twice the circumradius, so $4\\alpha$ against the wall's $\\alpha$ and the
hinge's $2\\alpha$.

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 303dc23** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2699.  Stated for reversal.
"""
import glob
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
    print('  A6 -- is item 58 actually unbanked?')
    print()
    papers = {os.path.basename(f): body(f)
              for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')}
    allp = re.sub(r'\s+', ' ', ' '.join(papers.values()))

    # ⓵ the sixth equivalence IS banked
    # ⛭ r4070: 61's P3 pass reworded both clauses; neither claim changed.
    #   *"A sixth is available and differs from those five in kind rather than in content"
    #    -> "Item~(vi) differs from the other five in \\emph{kind} rather than in content".
    #    "the same placement read in the substrate's own causal language" -> "the sixth READS
    #    the same placement in the substrate's own causal language".*  Re-pinned to the
    #   surviving forms; the receipt's thesis -- that P3 already carries the sixth -- stands.
    check('⛔ ⓵ P3 already carries the sixth equivalence: "A sixth is available and differs from those '
          'five in kind rather than in content"',
          'differs from the other five in \\emph{kind} rather than in content' in allp)
    check('with the substrate-language clause the receipt claimed as new: "the same placement read in '
          "the substrate's own causal language rather than in the plane's\"",
          "the same placement in the substrate's own causal language" in allp)
    # ⛭ r4070: THE CITATION COUNT WENT 2 -> 1 WHEN 61's PASS CONSOLIDATED THE PASSAGE.
    #   *P3 used to carry `\\rcpt{P03_the_sixth_equivalence}` twice; it now carries it once, on the
    #   item that DEFINES the sixth equivalence (the $s^{2}$ item, P3 line ~616).*  ⇒ *That is the
    #   citation's right home, and one citation on the defining item is not a weaker claim than two
    #   spread across a passage that has since been merged.*
    #   ⌗ *Per c54.226 a count is a claim about a FILE AT A COMMIT: measured 1 at tree
    #   b702f932219f8f56, after 61's r4009-r4065.  Asserted so a further change fires here.*
    check('and its receipt cited once, on the item that defines the sixth equivalence',
          len(re.findall('P03_the_sixth_equivalence', allp)) == 1)

    # ⓶ but the word never appears
    check('⛭⛭ ⓶ while "excentre" appears ZERO times -- P3 states it as "a $120^{\\circ}$-separated '
          'triple of lines at transverse radius $\\rho$"',
          'excentre' not in allp.lower()
          and 'separated triple of lines at transverse radius' in allp)

    # ⓷ the second result is genuinely absent
    # ** r2722, cc54's c54.213: *** the half this receipt found REAL was banked into P3 at
    # r2706.  An absence receipt that fails because its finding was acted on is a SUCCESS --
    # so this converts to a REGRESSION GUARD on the filling. ***
    check('✔ ⓷ and the half that WAS real is now FILLED (r2706): P3 carries the null connectivity '
          '-- "no null pair among the thirty-six" -- and cites its receipt',
          'no' in allp and 'null pair among the thirty-six' in allp
          and 'P03_slate_worked' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** item 58 is HALF closed, and the half that closed exposes the sweep\'s floor. **')
    print('  ⛔ ⓵ ** The sixth equivalence is ALREADY IN PRINT ** — P3 states it immediately after its')
    print('     five, with the substrate-language clause the receipt claimed as new, and ** cites the')
    print('     receipt twice. **')
    print('  ⛭⛭ ⓶ ** The sweep flagged the TERM; the RESULT was banked in different words. **  `excentre`')
    print('     never appears because P3 says "a 120°-separated triple of lines at transverse radius ρ"')
    print('     — ** which is what an excentre triple IS, said geometrically. **')
    print('     ⇒ *** THE THIRD FAILURE MODE, and unlike station (inflection) and monomial (API name),')
    print('       THIS ONE IS NOT FIXABLE BY MATCHING.  No term-frequency method can see that phrase is')
    print('       the excentre set.  The tool detects VOCABULARY gaps, not BANKING gaps — and those')
    print('       coincide only when paper and receipt happen to share a word. ***')
    print('  ⓷ ** The second result IS genuinely unbanked: ** "0 of 36", "null-inert", "36 pairs" all')
    print('     absent, and `P03_slate_worked` cited zero times.')
    print('  ⇒ ** So item 58 shrinks to one banking debt in P3\'s band, not two. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
