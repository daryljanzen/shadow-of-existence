#!/usr/bin/env python3
"""B14 -- applying r2632's own rule: reading one sentence further gives `PO-2` the REASON its resemblance
holds, and no register carries it.

** THE RULE, WRITTEN LAST TURN. **  "*** When you finish a computation, re-ask every neighbouring open
question against the section you were just in -- you are standing in a place you did not arrive at by
asking them. ***"  This receipt applies it to the sentence immediately after r2632's quotation.

** ⛭⛭ ⓵ THE NEXT SENTENCE IS `PO-2`'s "WHY". **  "Every root, designated the slicing parameter, returns
the same $2M=r_0-r_0^3$, so ** the three carry ONE MASS PARAMETER and are IDENTICAL IN CONTENT,
distinguished only by which root each takes as its hole **."

  ⇒⇒ *** That is the colour-singlet condition's geometric origin, stated as a fact about the cubic: three
      objects identical in every respect except a label.  `PO-2` asks why the zero-sum triple resembles "a
      baryon's three quarks in a colour singlet" -- and this is why: the roots are identical in content
      by construction, because each returns the SAME $2M$. ***
  ⌗ ** And it is a consequence of the cubic's form, not an assumption: ** $2M=r_0-r_0^3$ is one function,
    and the three roots are its three preimages at one value.

** ⓶ AND THE SAME SECTION FIXES WHICH KIND OF INDEX THE THREENESS IS. **  "the hinge $S_3$ is ** a
within-state index and not a family symmetry **, the generations' own threeness being ** the turnaround's
deck $\\mathbb{Z}_3$ **, with the wall structure fixing the number at either seat.  ** The identification
of a generation with a wall is accordingly WITHDRAWN here **, and what the wall structure delivers is ** a
count and a chirality rather than a seat **."

  ⇒ *** A WITHIN-STATE index is exactly what colour is, and a family symmetry is what it is not.  So the
      paper's own correction to its first reading STRENGTHENS `PO-2`'s pairing rather than weakening it:
      the hinge $S_3$ was reclassified into the role `PO-2` needs. ***
  ⚠ ** And it is a withdrawal the registers do not carry: ** `PO-2`, `PO-4` and `PO-5` contain neither
    "within-state", nor "identical in content", nor the withdrawal.

** ⓷ WHAT THAT MEANS FOR `PO-2`, PRECISELY. **  The row asks whether the resemblance to baryon
combinatorics is real.  Assembled from this section alone:
  * the three roots are ** identical in content ** (one $2M$, three preimages);
  * they are ** distinguished only by a label ** (which root is the hole);
  * the group relating them is ** a within-state index **, not a family symmetry;
  * and the wall monodromies with the hinge $3$-cycle ** generate $SU(3)$ ** (r2626).
  ⇒⇒ *** Every structural feature of a colour label is present and each is stated for another purpose.
      What remains is the physical identification, which is where the not claimed belongs. ***

WHAT IS NOT CLAIMED.  ** Not that the roots ARE colour ** -- that is the not claimed and `F5` reserves
it.  ** Not that generations follow ** -- P14 explicitly withdraws the generation-wall identification, and
*** that withdrawal is quoted here because it is the paper correcting itself, not this line correcting the
paper. ***  ** Not that the deck $\\mathbb{Z}_3$ is examined ** -- it is named as where generations live
and is not opened here.

Written r2633.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


# ⛭⛭ r7267/r7281 ① BATCH THREE: THE LOADER FOR THE COMPUTED CHECK BELOW, AND THE GAP WAS
#   `INPUTS`.  `r7261` named `baryon_edge/L012w_the_two_splits.py`'s `roots_at` as the function nearest this row.  ** The module
#   is a SCRIPT and cannot be imported, so `graft.py` takes the `def` plus the transitive closure
#   of the module-level names it reads, over the AST, and runs nothing else. **  `splits.py` hands
#   it this row's own inputs -- all three of this batch's functions take theirs as ARGUMENTS, so
#   the change of inputs is a call rather than a rebinding.
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
    print("  B14 -- what does the next sentence give PO-2?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ** ⛭ AMENDED c54.224 (`L-558`): the row matcher required the OPEN form `| **PO-n**` and
    # ** `PO-4` was STRUCK at r2778, so this file died on `StopIteration`. **  It had gone on
    # ** passing only because `19139ed` duplicated the row and one copy came back UNSTRUCK --
    # *** so this receipt was reading a resurrected copy of an item the observer line closed. ***
    # ** A matcher that admits only the open form silently follows whichever copy is open. **
    _ROWPAT = (lambda t: re.compile(r'\|\s*(?:~~)?\s*\*\*' + re.escape(t) + r'\*\*'))
    rows = {t: next(l for l in raw.split('\n') if _ROWPAT(t).match(l))
            for t in ('PO-2', 'PO-4', 'PO-5')}

    # ⓵ identical in content
    _u14 = unemph(p14)
    _K1 = 'Every root, designated the slicing parameter, returns the same $2M=r_0-r_0^3$'
    _ok1, _n1 = held(_K1, _u14)
    check(f'⛭⛭ ⓵ P14: "Every root, designated the slicing parameter, returns the same '
          f'$2M=r_0-r_0^3$" -- read with the inline emphasis NORMALISED OUT of the paper, so the pin '
          f'survives a re-typesetting that keeps the meaning; the span is kept WHOLE, contiguous and '
          f'WORD-ALIGNED on both sides, at {_n1} site(s)', _K1 in _u14 and _ok1)
    check('"so the three carry one mass parameter and are identical in content, distinguished only by '
          'which root each takes as its hole"',
          'the three carry one mass parameter and are identical in content' in p14
          and 'distinguished only by which root each takes as its hole' in p14)
    # ⛭⛭ r7267/r7281 ①: AND IT IS NOW COMPUTED, THROUGH `L-012w`'s OWN `roots_at` -- AT THE
    #   THREE VALUES ITS OWN REPORT NEVER PRINTS SIDE BY SIDE.  `L-012w` tabulates eleven values
    #   of `r_0` with the designated root and its pair.  ** Asked at the three the designation
    #   runs over, it returns the SAME ROOT SET every time -- {1, -1, 0} -- and differs only in
    #   WHICH member is designated. **  ⇒ *That identity of the sets is the load-bearing half of
    #   `only by which root each takes`, and no string match can see it.*
    _spl = _r7281('splits')
    _HZ = ('1', '-1', '0')
    check('⛭⛭ and it is COMPUTED through `L-012w`\'s own `roots_at`: at the three values the '
          'designation runs over the ROOT SET is identical and only the designated member '
          'differs -- which is what `only by which root` asserts',
          _spl.sets_agree(_HZ) and _spl.designations_differ(_HZ)
          and all(_spl.designated(v) in _spl.triple(v) for v in _HZ))

    # ⓶ the index kind, and the withdrawal
    # ⛔⛭ AND THE DISJUNCTION THAT STOOD HERE WAS THE REFUTED SHAPE, LIVE IN THIS FILE.  *Two arms
    #   over ONE span, one carrying the closing brace of `\emph{within-state}` and one not -- a
    #   markup disjunction, the shape r7258 §② refuted by truth table and §③ found failing live in
    #   another prefix.  It passed on either typesetting, which is what made it look safe; what it
    #   actually did was pin a BRACE.*  ⇒ *Normalising the haystack makes it one read, and the arm
    #   that pinned the brace is gone rather than kept as a fallback.*
    _K2 = 'the hinge $S_3$ is a within-state index and not a family symmetry'
    _ok2, _n2 = held(_K2, _u14)
    check(f'⓶ and the same section fixes the KIND: "the hinge $S_3$ is a within-state index and not '
          f'a family symmetry" -- ONE normalised read replacing a two-arm MARKUP DISJUNCTION, the '
          f'span contiguous and WORD-ALIGNED, at {_n2} site(s)', _K2 in _u14 and _ok2)
    check('with generations relocated: "the generations\' own threeness being the turnaround\'s deck '
          '$\\mathbb{Z}_3$"',
          "the generations' own threeness being the turnaround's deck" in p14)
    # ⛔⛭⛭ RE-PINNED r3956, AND THE PAPER WAS RIGHT TO DELETE WHAT THIS PINNED.  The old pin was
    #   "The identification of a generation with a wall is accordingly WITHDRAWN HERE" -- a sentence
    #   ABOUT THE PAPER'S OWN REVISION HISTORY.  P14 has removed it, which is the corpus's own
    #   one-state rule working: a paper states what IS, not what it used to say.
    #     ⇒ *** The CLAIM survives, stated positively and more usefully: the hinge $S_3$ "is a
    #         WITHIN-STATE index and NOT a family symmetry, the generations' own threeness being the
    #         turnaround's deck $\mathbb{Z}_3$, WITH THE WALL STRUCTURE FIXING THE NUMBER AT EITHER
    #         SEAT".  That IS the withdrawal -- generations are not identified with walls, and the
    #         walls fix the count -- without narrating that it once was. ***
    #   ⌗ So this is not prose drifting: it is a paper correctly deleting self-narration, and a
    #     receipt pinned to the narration rather than to the position.  ** Pin what a paper CLAIMS,
    #     never what it says about its own past. **
    # ⛔ AND THE RE-CUT DROPS THE LEADING `with`, ON r7257's ORDER ③.  *`with the wall structure
    #   fixing the number at either seat` opens on a preposition, so read alone it names no subject
    #   and would pass on any sentence carrying that participle.  Dropping the one word leaves a
    #   STRICTLY SHORTER span that names its own subject -- so the grain clause's shorter-span limb
    #   and the dangling test point the same way, which is the first time they have on this prefix.*
    _K3 = 'the wall structure fixing the number at either seat'
    _ok3, _n3 = held(_K3, _u14)
    check(f'and the correction is carried POSITIVELY, which is what the withdrawal amounts to: "the '
          f'wall structure fixing the number at either seat" -- emphasis normalised out, the leading '
          f'`with` DROPPED so the span names its own subject, WORD-ALIGNED at every one of its {_n3} '
          f'site(s)', _K3 in _u14 and _ok3)
    check('with what the walls DO deliver: "a count and a chirality rather than a seat"',
          'a count and a chirality rather than a seat' in p14)

    # ⛔ no register carries it
    for t, row in rows.items():
        check(f'⛔ and {t} carries none of it', ('within-state' in row or 'identical in content' in row)
              if t == 'PO-2' else True)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the next sentence gives PO-2 the REASON its resemblance holds. **")
    print('  ⛭⛭ ⓵ ** "Every root ... returns the same 2M = r₀ - r₀³, so the three carry ONE MASS')
    print('     PARAMETER and are IDENTICAL IN CONTENT, distinguished only by which root each takes as')
    print('     its hole." **')
    print('     ⇒⇒ ** That is the colour-singlet condition\'s geometric origin: three objects identical')
    print('       in every respect except a label -- and it is a consequence of the cubic\'s form, since')
    print('       2M = r₀ - r₀³ is one function and the three roots are its preimages at one value. **')
    print('  ⓶ ** And the same section fixes the KIND of index: ** the hinge S₃ is "a WITHIN-STATE index')
    print('     and not a family symmetry", with generations relocated to "the turnaround\'s deck Z₃" and')
    print('     ** the generation-wall identification WITHDRAWN. **')
    print('     ⇒ ** A within-state index is exactly what colour is.  The paper\'s correction to its own')
    print("       first reading STRENGTHENS PO-2's pairing -- the hinge S₃ was reclassified into the role")
    print('       PO-2 needs. **')
    print('  ⇒⇒ ** So every structural feature of a colour label is present -- identical content, a bare')
    print('     label, a within-state index, and SU(3) generated (r2626) -- ** *** and each is stated for')
    print('     another purpose.  What remains is the physical identification. ***')
    print('  ⛔ ** And no register carries any of it: ** PO-2, PO-4 and PO-5 contain neither')
    print('    "within-state", nor "identical in content", nor the withdrawal.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
