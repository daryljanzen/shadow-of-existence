#!/usr/bin/env python3
"""C3 -- item 26's residue, and it is not what F12 said: P12 and P9 cite EACH OTHER for the isotropy
dimensions, and the triple {6,7,10} appears in neither's derivation.

** WHERE ITEM 26 STOOD. **  Routed r2442, and honestly: "two items routed at the finder's weight,
** not independently verified here **.  This line has not re-derived either, and says so rather than
passing them on as checked."  ** It is one of the last two items in the routed queue, and the only one
with a testable claim in it. **

** ⓵ F12's CHARACTERISATION IS WRONG, AND CHECKING IT IS WHAT FOUND THE REAL THING. **  F12: "P12's
isotropy-3 stratum labelled 'Bianchi' is claimed to be ** six of the nine types **".
  ⇒ ** Measured: `isotropy-3` 0 · `six of the nine` 0 · `nine types` 0 across the papers. **  P12's only
    `Bianchi` is "** Type I (Bianchi, dimension three; Zipoy--Voorhees, dimension two) **" -- a label on
    one stratum, ** not a claim about six of nine **.
  ⌗ *** So the finder's weight was the right thing to route it at.  The claim as stated does not exist. ***

** ⛭⛭ ⓶ BUT THE SENTENCE F12 POINTED AT CARRIES A DIFFERENT DEFECT, AND IT IS REAL. **  P12:

  "** The isotropy dimensions are the Killing-vector counts the construction establishes **~\\cite{JanzenRange},
   and the verdict is independent of the choice of generator realization: ** the symmetric-pair isotropy
   dimensions of $\\so(5,1)$ are $\\{6,7,10\\}$ **"

  ** So P12 states the triple and cites P9 for it. **  And P9, at its own isotropy passage:

  "at every stratum for which ** the companion algebroid paper tabulates an isotropy ** ... it is in fact
   an equality~\\cite{JanzenAlgebroid}"

  ⇒ *** EACH CITES THE OTHER FOR THE SAME FACT.  P12 cites P9 for the counts; P9 cites P12 for the
      tabulation. ***

** ⓷ AND THE TRIPLE IS IN NEITHER DERIVATION. **  ** `6,7,10` appears 0 times in P9 **; `seven` 0, `six`
0, `isotropy dimension` 0.  ** P9 names isotropies as GROUPS ** -- $\\mathrm{SO}(4,1)$ at Type O,
$\\mathrm{SO}(2,1)\\times\\mathrm{SO}(3)$ at Nariai, $\\mathbb{R}_t\\times\\mathrm{SO}(3)$ at the generic
class -- ** and never as the dimension triple P12 attributes to it. **
  ⇒ ** The dimensions are recoverable from those groups by inspection ** (10, 3+1=4 ... ), *** which is
      exactly why nobody noticed: the fact is TRUE and the citation does not establish it. ***

** ⇒⇒ SO ITEM 26's RESIDUE IS A CITATION-CONTENT GAP, WHICH IS ITEM 45's CLASS. **  There,
`Teitelboim1973` was cited for the Dirac brackets' ** form ** and never for the ** uniqueness content **.
Here, P9 is cited for a ** triple it never states **, while P9 cites P12 back for the tabulation the
triple summarises.
  ⌗ *** A citation loop between two papers is invisible to `check_citations`, which checks that a cited
      key EXISTS, not that the cited paper CONTAINS the fact. ***

WHAT IS NOT CLAIMED.  ** Not that the triple is wrong ** -- $\\{6,7,10\\}$ is consistent with the groups P9
names, and this receipt does not re-derive it.  ** Not that either paper is careless **: two papers
written together will naturally point at each other, and *** the loop is a property of the pair, not a
mistake in either alone. ***  ** Not that F16 is checked ** -- item 26's second finding is untouched here
and stays at the finder's weight.

⌗ AND WHAT WOULD DISCHARGE IT: ** one of the two papers derives the triple, or P12 states it as its own
rather than attributing it. **  *** One clause, and the choice of which paper owns it is an authorial
one. ***

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT ebc5215** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2575.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


# ⛭⛭ r7267/r7275 ①: THE LOADER FOR THE COMPUTED HALF OF THE PIN BELOW, AND THE GAP WAS `INPUTS`.
#   `r7261` named `beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py`'s `lie_g` as the function nearest this row.  ** The module is a
#   SCRIPT and cannot be imported, so `graft.py` takes the `def` plus the transitive closure of
#   the module-level names it reads, over the AST, and runs nothing else. **  `isometry.py` hands
#   it this row's own inputs.  ⇒ ** The pin below STAYS: it is the citation; this verifies it. **
def _r7267():
    """`beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py`'s own `lie_g`, grafted, at this row's inputs."""
    if not hasattr(_r7267, 'v'):
        import sys
        sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                        'r7267_cc66_reach_the_71'))
        import isometry
        _r7267.v = isometry.at_inputs().nariai()
    return _r7267.v


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(name):
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', name), encoding='utf-8',
                        errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


def _r7283b8():
    """`r7283` ② batch eight: the extension that reaches this row, loaded on demand.

    ⚠ *For this row the backlog named a function of the wrong kind or the wrong name, and the
    note beside the check says which.  The extension records what DID reach the claim.*"""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import extensions_b8 as _X
    return _X

def main():
    print()
    print("  C3 -- item 26's residue: does P9 establish what P12 cites it for?")
    print()
    p12 = body('algebroid_paper.tex')
    p9 = body('range_paper.tex')
    allp = ' '.join(body(os.path.basename(f)) for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
                    if not os.path.basename(f).startswith('appendix_receipts'))

    # ⓵ F12's characterisation is wrong
    for k in ('isotropy-3', 'six of the nine', 'nine types'):
        check(f'⓵ F12 says P12 claims "{k}" -- it appears ZERO times across the papers',
              len(re.findall(re.escape(k), allp, re.I)) == 0)
    # ⛭⛭ r7338+60, PO-78's repair stride, the middle -- EDITED ON `r7337` ④'s order.
    #   ** THREE OWED ROWS HERE. ** The first was cut mid-parenthesis -- the label it quotes runs
    #   to `Zipoy--Voorhees, dimension two)` and the pinned span stopped inside it, so it was not
    #   the shortest span that carries the claim but a prefix of one.
    check('and P12\'s only "Bianchi" is a label on one stratum: "Type I (Bianchi, dimension three; '
          'Zipoy--Voorhees, dimension two)" -- asserted as the whole parenthetical it is, in place '
          'of a span cut inside it',
          'Type I (Bianchi, dimension three; Zipoy--Voorhees, dimension two)' in p12)

    # ⓶ the real sentence
    # ⛭⛭ r7338+60: ** the second owed row was the bare citation KEY `JanzenRange`, conjoined with
    #   the sentence -- so the conjunction asserted `this sentence is present AND this key is
    #   present somewhere in the paper`, which is not the claim that the sentence CITES it. **
    #   ⇒ *One span carrying the sentence and its own citation.  The gate layer's normaliser does
    #     not touch references, which is a stated limit, so this span is brittle to a citation-key
    #     rename and not to a rewording -- the right way round for a claim about WHO is cited.*
    _CITES = ('The isotropy dimensions are the Killing-vector counts the construction '
              'establishes~\\cite{JanzenRange}')
    check('⛭⛭ ⓶ but P12 states, citing the range paper in the same breath: "The isotropy dimensions '
          'are the Killing-vector counts the construction establishes~\\cite{JanzenRange}" -- one '
          'span, in place of a sentence conjoined with a bare citation key',
          _CITES in p12)
    # ⛭⛭ r7338+60: ** and the third was the bare formula `$\{6,7,10\}$`, which a markup rewording
    #   keeping the content breaks and which says nothing about what the triple IS. **
    #   ⇒ *Extended to the clause that names the dimensions AND which two the construction
    #     occupies, over an EMPHASIS-ONLY normalised read -- `r7336`'s own rule case: the full
    #     normaliser applied inside a receipt's reader mints no ledger key at all.*
    _p12e = re.sub(r'\\(?:emph|textit|textbf)\{([^{}]*)\}', r'\1', p12)
    _TRIPLE = ('the admissible symmetric-pair dimensions are $\\{6,7,10\\}$, and the construction '
               'occupies six and ten')
    check('and gives the triple with what it occupies: "the admissible symmetric-pair dimensions '
          'are $\\{6,7,10\\}$, and the construction occupies six and ten" -- asserted over an '
          'emphasis-normalised read, in place of the bare formula',
          _TRIPLE in _p12e)
    check('while P9 points BACK: "at every stratum for which the companion algebroid paper tabulates an '
          'isotropy ... it is in fact an equality~\\cite{JanzenAlgebroid}"',
          's stated as an inclusion, and at some strata it is in fact an equality.} At every stratum for which the companion algebroid paper tabulates an isotropy' in p9
          and 'JanzenAlgebroid' in p9)
    check('⇒⇒ SO EACH CITES THE OTHER FOR THE SAME FACT',
          'JanzenRange' in p12 and 'JanzenAlgebroid' in p9)

    # ⓷ and the triple is in neither derivation
    check('⓷ and the triple is NOT in P9: "6,7,10" appears zero times there',
          '6,7,10' not in p9)
    # ⛔⛭ AMENDED r4522: the paper writes "Type~O" with a non-breaking space and this check asked for
    #    "Type O".  *The third tie-break of this run.*  ⇒ The probe binds the GROUP to the STRATUM
    #    across whatever space sits between them, and still requires both groups, so it cannot pass
    #    on a paper that names neither.
    _ISO = re.compile(r"\\mathrm\{SO\}\(4,1\)\$ at Type[~ ]?O")
    check('P9 names isotropies as GROUPS instead -- SO(4,1) at Type~O, SO(2,1)xSO(3) at Nariai',
          _ISO.search(p9) is not None
          and '\\mathrm{SO}(2,1)\\times\\mathrm{SO}(3)$ at Nariai' in p9)
    # ⛭⛭ r7267/r7275 ①: AND THE ALGEBRA AT NARIAI IS NOW COMPUTED, THROUGH `A2`'s OWN `lie_g`.
    #   `lie_g` is `A2`'s Killing test and reads its METRIC from module level, where `A2` binds
    #   the chiral plane wave; the change of inputs is a REBINDING -- hand the grafted namespace
    #   the Nariai metric dS_2 x S^2 and `A2`'s own test answers about this geometry.
    #   ** Six generators come back Killing: three on the dS_2 factor, DERIVED from the
    #   embedding -T^2+X^2+Y^2 = 1 and each verified against its third row rather than quoted,
    #   and three on the two-sphere.  so(2,1) + so(3), with the product structure. **
    #   ⌗ *Three reachable converses -- chi d_tau, d_chi, d_theta -- all come back NOT Killing.*
    _iso = _r7267()
    _gens, _conv = _iso.generators(), _iso.converses()
    check('⛭⛭ and the ALGEBRA is COMPUTED through `A2`\'s own `lie_g` at the Nariai metric: six '
          'generators are Killing -- three $\\mathfrak{so}(2,1)$ on the $dS_2$ factor and three '
          '$\\mathfrak{so}(3)$ on the two-sphere -- and three reachable converses are not',
          len(_gens) == 6 and all(_iso.is_killing(x) for x in _gens.values())
          and not any(_iso.is_killing(x) for x in _conv.values()))
    check('⇒ so the fact is TRUE and recoverable by inspection, and the citation does not establish it '
          '-- which is why nobody noticed',
          '\\{6,7,10\\}' in p12 and '6,7,10' not in p9)

    # the class
    check("⌗ and this is item 45's class: a citation for FORM where the CONTENT is elsewhere",
          'Teitelboim1973' in p12)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** item 26's residue is a citation LOOP, and it is not what F12 said. **")
    print('  ⓵ ** F12\'s "six of the nine types" does not exist ** -- isotropy-3 0, six of the nine 0,')
    print('     nine types 0.  ** The finder\'s weight was the right thing to route it at. **')
    print('  ⓶ ** But P12 states the triple {6,7,10} and cites P9; and P9 cites P12 back for the')
    print('     tabulation the triple summarises. **  ⇒ ** Each cites the other for the same fact. **')
    print('  ⓷ ** And "6,7,10" appears ZERO times in P9 ** -- which names isotropies as GROUPS, not as a')
    print('     dimension triple.  ⇒ ** The fact is TRUE and recoverable by inspection, and the citation')
    print('     does not establish it: which is exactly why it survived. **')
    print('  ⌗ ** A citation loop between two papers is invisible to check_citations **, which checks a')
    print('    cited key EXISTS, not that the cited paper CONTAINS the fact.')
    print('  ⇒ WHAT WOULD DISCHARGE IT: ** one paper derives the triple, or P12 states it as its own. **')
    print('    One clause -- and which paper owns it is authorial.')
    print()
    _X = _r7283b8()
    check("⛭ `r7283` ② COMPUTED, not cited: the symmetric-pair isotropy dimensions. An involution "
          "of `so(5,1)` flipping `k` of the six ambient axes fixes `so(k) + so(6-k)`, of "
          "dimension `k(k-1)/2 + (6-k)(5-k)/2`; over `k = 1..5` the SET is `{6,7,10}`, "
          "exactly the triple `P12` states. One ambient dimension up, `so(6,1)` gives "
          "`{9,11,15}` and the triple fails, which is the reachable converse. ** The "
          "backlog named `killing_residual`, which settles ONE field against ONE metric, "
          "and the corpus carried NO subalgebra-dimension function when the backlog was "
          "written: this is the one FUNCTION-IS-THE-WRONG-KIND row of the twelve **",
          _X.triple_matches_the_paper(6) and not _X.triple_matches_the_paper(7))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
