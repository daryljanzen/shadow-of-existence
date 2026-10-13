#!/usr/bin/env python3
"""B9 -- `PO-3`'s "why" is answered, dimensionally: the parity doubling exists because the mass function
is odd in the signed offset exactly when $D$ is even.

** THE ITEM, never worked (0 dated moves before this). **  `PO-3`: "The $a_2$-meaning drill-site --- ** why
does the SdS geometry produce a zero-sum triple with a $\\mathbf3/\\bar{\\mathbf3}$ parity doubling **, and
does that reason ...", targeting "** the $A_2$ skeleton and the parity doubling **".

** ⛭⛭ ⓵ THE $A_2$ SKELETON IS IDENTIFIED, AND IT IS THE OFFSET-TO-MASS CUBIC. **  P13: "the offset-to-mass
map is no mere labelling: it is a cubic, $2M=((r_0/\\alpha)-(r_0/\\alpha)^3)$, ** whose three zero-sum roots
are the $A_2$ weights that $S_3$ permutes **---mass-tied, moving with $2M$---so ** the geometry does carry
a genuine three-fold $R$-odd mass structure **".

  ⇒ ** So "the zero-sum triple" is the cubic's roots and "the $A_2$ skeleton" is what they form. **  *** Not
    a resemblance: the roots ARE the weights, and $S_3$ permutes them. ***

** ⛭⛭⛭ ⓶ AND THE "WHY" OF THE PARITY DOUBLING IS ANSWERED, IN P14, AS A DIMENSIONAL FACT. **  The
$D$-selection argument runs on two conditions, and the SECOND is exactly this row's question:

  "The second condition is ** the parity **, and it separates those two.  ** The mass function is odd in
   the signed offset exactly when $D$ is even **, so ** at $D=5$ the orientation parity $r_0\\to-r_0$ fixes
   each geometry rather than exchanging it with its conjugate: there is no mass-reflection
   $\\mathbb{Z}_2$, hence no $\\mathbf3\\oplus\\bar{\\mathbf3}$ Nariai hexad, no outer factor of
   $\\mathrm{Aut}(A_2)=S_3\\rtimes\\mathbb{Z}_2$, and no $\\gamma^5$ **"

  ⇒⇒ *** THE ANSWER, read forward: the doubling exists at $D=4$ BECAUSE the mass function is odd in the
      signed offset there, so the orientation parity EXCHANGES each geometry with its conjugate rather
      than fixing it.  That exchange IS the $\\mathbf3/\\bar{\\mathbf3}$ doubling, and it is what supplies
      the outer $\\mathbb{Z}_2$ of $\\mathrm{Aut}(A_2)$ and $\\gamma^5$ with it. ***

** ⓷ AND THE ROW'S SECOND CLAUSE -- "does that reason ..." -- HAS ITS ANSWER TOO. **  The same passage
uses the parity as ** a $D$-selection condition **: it rules out $D=5$, where the first condition (the
harmonic collapse, "at $D=5$ the collapse does occur, at scale $1$, and returns a four-fold") would
otherwise have admitted it.
  ⇒ *** So the reason for the doubling is not a local curiosity: it is one of the two conditions that
      select $D=4$, and P14 uses it as such. ***  ** That is the third $D=4$ argument rehomed at r2582,
      seen from the other end. **

WHAT IS NOT CLAIMED.  ** Not that `PO-3` closes ** -- `F5` reserves that, and the row's own status text
carries corrections from the colour arc that are not audited here.  ** Not that the mass VALUES realise
the three-fold splitting ** -- P13 marks that separately: "whether their masses realise its three-fold
splitting---a ph[ysical question]".  ** Not that this is new physics ** -- *** every clause quoted is in
the papers; what was missing was the connection between the row's question and the passage that answers
it. ***

Written r2627.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


# ⛭⛭ r7267 ①: THE LOADER FOR THE COMPUTED HALF OF THE PIN(S) BELOW, AND THE GAP WAS `INPUTS`.
#   `r7261`'s backlog named, per row, the module AND FUNCTION nearest to computing what this
#   receipt only MATCHES AS A STRING, and classified this row's gap a change of INPUTS.  ** The
#   obstruction was never the mathematics: the named module is a SCRIPT -- it prints its own
#   report at import and some of them run minutes of sympy to do it, so the function could not
#   be imported. **  `graft.py` takes the `def` and the transitive closure of the module-level
#   names it reads, over the AST, and executes nothing else; `parity.py` hands it this row's own
#   inputs.  ⇒ ** The pin below STAYS: it is the citation.  This is the verification. **
def _r7267():
    """`baryon_edge/L006w_the_d5_fourfold.py`'s own functions, grafted, at this row's inputs."""
    if not hasattr(_r7267, 'v'):
        import sys
        sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                        'r7267_cc66_reach_the_71'))
        import parity
        _r7267.v = parity.at_inputs()
    return _r7267.v


# ⛭⛭ r7267/r7281 ① BATCH THREE: THE LOADER FOR THE COMPUTED CHECK BELOW, AND THE GAP WAS
#   `INPUTS`.  `r7261` named `bead_conjugate.py`'s `r_of_tau` as the function nearest this row.  ** The module
#   is a SCRIPT and cannot be imported, so `graft.py` takes the `def` plus the transitive closure
#   of the module-level names it reads, over the AST, and runs nothing else. **  All three of this
#   batch's functions take their inputs as ARGUMENTS, so the change of inputs is a call.
#   ⇒ ** The pin below STAYS: it is the citation; this verifies it. **
def _r7281(which):
    """`L-012w`'s `roots_at`, `L-127`'s `omega_power` or `bead_conjugate`'s `r_of_tau`, grafted."""
    if not hasattr(_r7281, 'v'):
        import sys
        sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                        'r7267_cc66_reach_the_71'))
        import splits
        _r7281.v = dict(zip(('splits', 'omega', 'bead'), splits.at_inputs()))
    return _r7281.v[which]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


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
    print("  B9 -- is PO-3's 'why' answered anywhere?")
    print()
    p13 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'boundary_paper.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw.split('\n')
               if re.match(r'\|\s*~?~?\*\*PO-3\*\*', l))

    # the question
    check("⓵ PO-3 asks why the geometry produces \"a zero-sum triple with a "
          '$\\mathbf3/\\bar{\\mathbf3}$ parity doubling"',
          'parity doubling' in row and 'zero-sum triple' in row)
    check('targeting "the $A_2$ skeleton and the parity doubling"',
          'the $A_2$ skeleton and the parity doubling' in row)

    # ⓵ the A2 skeleton is the cubic's roots
    check('⛭⛭ ⓶ P13 identifies the skeleton: the offset-to-mass map "is a cubic ... whose three zero-sum '
          'roots are the $A_2$ weights that $S_3$ permutes"',
          'whose three zero-sum roots are the $A_{2}$ weights that $S_{3}$ permutes' in p13
          or 'whose three zero-sum roots are the $A_2$ weights that $S_3$ permutes' in p13)

    # ⓶ the why, dimensionally
    check('⛭⛭⛭ ⓷ and P14 answers the WHY: "The mass function is odd in the signed offset exactly when '
          '$D$ is even"',
          'The mass function is odd in the signed offset exactly when $D$ is even' in p14)
    # ⛭⛭ r7267 ①: AND THE DIMENSIONAL FACT IS NOW COMPUTED.  `L-006w`'s `twoM` returns
    #   r_0**(D-3) - r_0**(D-1); substituting r_0 -> -r_0 gives (-1)**(D-1), so the mass
    #   function is odd EXACTLY when D is even -- asked here at D = 4..9 rather than at the
    #   three values `L-006w` prints.  ** The reachable converse is the sentence with `odd` in
    #   place of `even`, and the same predicate is FALSE on it. **
    _par = _r7267()
    check('⛭⛭ and the SAME FACT is COMPUTED through `L-006w`\'s own `twoM`: its R-parity at '
          'D = 4..9 is odd exactly on the even D',
          all(_par.mass_is_R_odd(_D) == (_D % 2 == 0) for _D in range(4, 10))
          and not all(_par.mass_is_R_odd(_D) == (_D % 2 == 1) for _D in range(4, 10)))
    # ⛔⛭ RE-CUT r7260+60 on r7257's orders ① and ③.  *The span was `\emph{fixes} each geometry
    #   rather than exchanging it with its conjugate`: a MARKUP CARRIER whose first word was the
    #   markup command itself, and a DANGLING span -- it opens on a finite verb and names nothing
    #   that does the fixing, so it would pass on any sentence carrying that predicate.  ⇒ Emphasis
    #   normalised out and the span extended LEFT to the paper's own subject, which is the
    #   ORIENTATION PARITY and is the thing the surrounding argument turns on.*
    _u14 = unemph(p14)
    _KEY = ('the orientation parity $r_{0}\\mapsto-r_{0}$ fixes each geometry rather than exchanging '
            'it with its conjugate')
    _ok, _n = held(_KEY, _u14)
    check(f'with the consequence at $D=5$ spelled out: "the orientation parity '
          f'$r_{{0}}\\mapsto-r_{{0}}$ fixes each geometry rather than exchanging it with its '
          f'conjugate" -- emphasis NORMALISED out of the paper and the SUBJECT inside the span, '
          f'word-aligned at {_n} site(s)', _KEY in _u14 and _ok)
    check('and what is then absent: "there is no mass-reflection $\\mathbb{Z}_{2}$, hence no '
          '$\\mathbf3\\oplus\\bar{\\mathbf3}$ Nariai hexad, no outer factor of '
          '$\\mathrm{Aut}(A_{2})=S_{3}\\rtimes\\mathbb{Z}_{2}$, and no $\\gamma^{5}$"',
          'there is no mass-reflection' in p14 and '3}$ Nariai hexad, no' in p14
          and 'no outer factor of' in p14)

    # ⓷ it is a D-selection condition
    # ⛭⛭ r7267 ①: and the ABSENCE is computed too -- at D = 5 the substitution r_0 -> -r_0
    #   FIXES `twoM` (parity +1), so there is no 2M -> -2M involution to be had; the reachable
    #   converse is the same question at D = 4, where the parity is -1 and there is one.
    check('⛭⛭ and the ABSENCE is COMPUTED: at D = 5 `L-006w`\'s `twoM` is FIXED by R, so no '
          'mass-reflection exists to carry a hexad -- while at D = 4 it reverses',
          _r7267().mass_parity(5) == 1 and _r7267().mass_parity(4) == -1)

    check('⓸ and P14 uses it as a $D$-selection condition: "The second condition is the parity, and it '
          'separates those two"',
          'The second condition is the parity, and it separates those two' in p14)
    # ⛭⛭ r7267/r7281 ①: AND THE BRANCH POINT IS NOW COMPUTED, THROUGH `bead_conjugate`'s OWN
    #   `r_of_tau`: at proper time ZERO the collapse radius is exactly 0.0 -- the branch point --
    #   while at 0.5 and 1.0 it is 0.638472 and 1.203939.  ⇒ *So the endpoint is a statement about
    #   proper time zero, and the converse is any proper time away from it.*
    _bd = _r7281('bead')
    check('⛭⛭ and the ENDPOINT is COMPUTED through `bead_conjugate`\'s own `r_of_tau`: the collapse '
          'radius is exactly zero at proper time zero -- the branch point -- and non-zero away '
          'from it',
          _bd.branch_point_at_zero() and _bd.nonzero_away())
    # ⛭⛭ r7267 ①: and WHICH TWO it separates is computed rather than read.  The parity of
    #   `twoM` is -1 at D = 4 and +1 at D = 5, so it separates that pair; ** the reachable
    #   converse is D = 4 against D = 6, where both are -1 and the parity separates nothing. **
    check('⛭⛭ and WHAT IT SEPARATES is COMPUTED: `L-006w`\'s `twoM` has opposite R-parity at '
          'D = 4 and D = 5, and the SAME parity at D = 4 and D = 6',
          _r7267().mass_parity(4) != _r7267().mass_parity(5)
          and _r7267().mass_parity(4) == _r7267().mass_parity(6))
    check('against the first, which alone would admit $D=5$: "At $D=5$ the collapse does occur, at scale '
          '$1$, and returns a four-fold"',
          'the collapse does occur, at scale' in p14 and 'does occur, at scale $1$, and returns a four-fold' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-3's 'why' is answered, dimensionally, and the row never knew. **")
    print('  ⛭⛭ ⓵ ** The $A_2$ skeleton IS the offset-to-mass cubic: ** its "three zero-sum roots are the')
    print('     $A_2$ weights that $S_3$ permutes" -- not a resemblance, an identity.')
    print('  ⛭⛭⛭ ⓶ ** And the WHY is a dimensional fact: ** "The mass function is odd in the signed')
    print('     offset ** exactly when D is even **".')
    print('     ⇒ ** Read forward: at D=4 the orientation parity EXCHANGES each geometry with its')
    print('       conjugate rather than fixing it -- and that exchange IS the 3/3̄ doubling, supplying')
    print('       the outer Z2 of Aut(A_2) and γ⁵ with it. **')
    print('  ⓷ ** And P14 uses the parity as a D-SELECTION condition: ** it rules out D=5, where the')
    print('     harmonic collapse alone "returns a four-fold".')
    print('     ⇒ ** So the reason is not a local curiosity: it is one of the two conditions that select')
    print('       D=4 -- the third D=4 argument, seen from the other end. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
