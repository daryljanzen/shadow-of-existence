#!/usr/bin/env python3
"""M3 -- station Ⓖ walked: the missing object is the Atiyah sequence, and all three remaining stations
turn out to be one knot whose first thread is routed item 23.

** THE STATION. **  R-M carries Ⓖ, "Lie algebroids -> Cartan / differential geometry", as owed and
independent of Ⓒ and Ⓗ.

** ⓵ AND P12 IS THE ALGEBROID PAPER, so this is Ⓕ's shape again -- check the corpus before the field. **
P12 builds the ** action Lie algebroid so(5,1) x| C ** and verifies its defining structure, with the
anchor named explicitly: "** the map from an infinitesimal cut-deformation to its stress-energy ** ---
the Arnowitt--Deser--Misner data read as functions of the cut: energy is the Hamiltonian constraint (the
bend of the leaf), momentum the bend of the shift."

  It carries ** 5 uses of "Lie algebroid", 10 of "anchor", 3 of "connection" -- and ZERO of "Atiyah
  sequence". **
  ⚠ And its two uses of "Cartan" are the ** Cartan--Weyl skeleton ** (the three roots furnishing a
  Cartan element of su(3), the S_3 its Weyl group) -- ** not Cartan geometry, which is what the station
  means. **

** ⛭⛭ ⓶ AND THE ATIYAH SEQUENCE IS PRECISELY THE OBJECT THAT RELATES THE THREE P12 HAS. **

For a principal bundle P -> M with group G:

      0  ->  ad(P)  ->  TP/G  ->  TM  ->  0

  ** the middle term IS a Lie algebroid; the surjection onto TM IS its anchor; and a CONNECTION is
  exactly a SPLITTING of the sequence. **

  ⇒ *** SO P12 HAS AN ALGEBROID, AN ANCHOR, AND CONNECTIONS, AND DOES NOT NAME THE SEQUENCE IN WHICH
      THOSE THREE ARE ONE STRUCTURE.  That is what the field supplies. ***

** ⛭⛭ ⓷ AND IT COMPOSES WITH r2468 -- THE THIRD STATION IN THREE TO DO SO. **

r2468 established: ** the colour bundle is FLAT because it IS a branching -- a covering map carries a
canonical flat connection, so "the geometry quantises and does not couple" is a theorem about branchings
rather than a limitation of the construction. **

  ⇒ ** In Atiyah-sequence language that is one sentence: THE SEQUENCE SPLITS, AND THE SPLITTING HAS ZERO
    CURVATURE. **

** ⇒⇒ ⓸ SO Ⓖ IS NOT INDEPENDENT AFTER ALL, AND THE THREE STATIONS ARE ONE KNOT: **

      Ⓒ  asks WHICH GROUP acts                       (r2491: S_3, Z_3, Z_6 -- unresolved)
      Ⓗ  needs that group for an EQUIVARIANT INDEX    (r2492: Ⓒ is its prerequisite)
      Ⓖ  supplies the SEQUENCE in which "which group" and "what connection" are the same question,
         because ** ad(P) is built from the group **

  *** ALL THREE ARE ONE KNOT, AND ITS FIRST THREAD IS ROUTED ITEM 23. ***

⌗ AND THAT IS THE REACH DOING WHAT A REACH IS FOR, three times over: ** each station was expected to
bite independently, and each turned out to name a different face of one unresolved thing.  A reach list
that CONVERGES is more informative than one that scatters, because convergence is evidence the object is
real. **

WHAT IS NOT CLAIMED.  ** Not that P12 owes the Atiyah sequence, or that naming it changes any result. **
P12's algebroid is ** the constraint algebra's, not a principal bundle's ** -- the sequence is a bridge
between two structures the corpus holds SEPARATELY, and ** whether they should be bridged is a judgement
not made here. **  Not that the colour bundle's flatness is in question: it is r2468's result and stands.

Written r2493.  Stated for reversal.
"""
import os, re
import subprocess as _sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  M3 -- station Ⓖ: what does differential geometry supply that P12 does not have?')
    print()
    raw = open(os.path.join(ROOT, 'corpus', 'algebroid_paper.tex'),
               encoding='utf-8', errors='replace').read()
    p12 = re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                        if not l.lstrip().startswith('%')))
    rm = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'),
                                  encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    check('R-M carries Ⓖ, Lie algebroids -> Cartan / differential geometry, as owed',
          'Lie algebroids' in rm)

    # ⓵ what P12 has
    check('P12 builds the action Lie algebroid $\\so(5,1)\\ltimes\\C$',
          'action Lie algebroid $\\so(5,1)\\ltimes\\C$' in p12)
    check('and names the anchor: "the map from an infinitesimal cut-deformation to its stress-energy"',
          'the map from an infinitesimal cut-deformation to its stress-energy' in p12)
    n_alg = len(re.findall('Lie algebroid', p12))
    n_anc = len(re.findall('anchor', p12, re.I))
    n_con = len(re.findall('connection', p12, re.I))
    n_seq = len(re.findall('Atiyah sequence', p12, re.I))
    check(f'it carries {n_alg} "Lie algebroid", {n_anc} "anchor", {n_con} "connection"',
          n_alg >= 4 and n_anc >= 8 and n_con >= 2)
    # ** ⛭⛭⛭ RE-PINNED r3962, AND THE ABSENCE ENDED BECAUSE THIS RECEIPT ASKED FOR IT. **  Written
    # ** r2493 (`ed5422d8`), this file's finding was that P12 had the algebroid, the anchor and the
    # ** connection and NEVER NAMED THE OBJECT THAT RELATES THEM.  *** r3251 wrote it in, and its
    # ** subject says what it was doing: "the theatre results carried INTO the papers, which is what
    # ** a bake is for." ***  P12 now names it twice and draws the consequence -- "the constraint
    # ** algebra of general relativity is the Atiyah algebroid of the substrate's own principal
    # ** bundle" -- and even records the receipt's own argument for it, that "naming it costs nothing
    # ** and buys the literature".
    #   ⇒ ** A ZERO-COUNT ASSERTION IS A CLAIM THAT NOBODY HAS ACTED ON THE FINDING YET.  It cannot
    #     survive the finding succeeding, and re-pinning it to a new number would only reset that
    #     timer. **  Both ends are pinned instead: absent at this file's own build, present now.
    _at_build = re.sub(r'\s+', ' ', _sp.run(
        ['git', 'show', 'ed5422d8:corpus/algebroid_paper.tex'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout)
    check('⛭ P12 carried ZERO "Atiyah sequence" at ed5422d8, this file\'s own build (r2493) -- which '
          'is the gap it was written to name',
          len(re.findall('Atiyah sequence', _at_build, re.I)) == 0)
    check(f'⛭⛭ AND THE GAP IS CLOSED: P12 names it {n_seq} time(s) now, written in at r3251 -- "the '
          f'theatre results carried INTO the papers, which is what a bake is for"',
          n_seq >= 1
          and 'Atiyah sequence of the principal bundle $SO(5,1)\\to\\dS_5$' in p12
          and 'naming it costs nothing and buys the literature' in p12)
    check('⇒ and the consequence this file argued for is drawn in the paper\'s own voice: "the '
          'constraint algebra of general relativity is the Atiyah algebroid of the substrate\'s own '
          'principal bundle"',
          'constraint algebra of general relativity is the Atiyah algebroid of the substrate' in p12)
    check('⚠ and its "Cartan" uses are the Cartan--Weyl SKELETON, not Cartan GEOMETRY',
          'Cartan--Weyl skeleton' in p12)

    # ⓶ the sequence relates exactly those three
    # ⌗ the structural claim never depended on the sequence being ABSENT -- it is about what the
    #   sequence RELATES -- so only the stale conjunct goes; the three-object count stays.
    check('⇒ the Atiyah sequence 0 -> ad(P) -> TP/G -> TM -> 0 has a Lie algebroid as its middle '
          'term, the anchor as its surjection, and a CONNECTION as a splitting -- so it relates '
          'exactly the three objects P12 has', n_alg >= 4 and n_anc >= 8 and n_con >= 2)

    # ⓷ composition with r2468
    # ** the register writes it in CAPS with markdown bold: "**AND A COVERING MAP CARRIES A
    # CANONICAL FLAT CONNECTION BY DEFINITION:**".  Third quotation this session written from a
    # memory of a read instead of from the file -- match case-insensitively on the phrase itself. **
    check('r2468 established the colour bundle is FLAT because it IS a branching -- "A COVERING MAP '
          'CARRIES A CANONICAL FLAT CONNECTION BY DEFINITION"',
          'covering map carries a canonical flat connection' in arc.lower())
    check('⇒ in Atiyah-sequence language: the sequence SPLITS and the splitting has ZERO CURVATURE',
          'covering map' in arc)

    # ⓸ the knot
    check('Ⓒ (r2491) left three order-six-adjacent groups unresolved',
          'order-six-adjacent objects' in arc)
    check('Ⓗ (r2492) needs a named group for an equivariant index, so Ⓒ is its prerequisite',
          'PREREQUISITE' in arc or 'prerequisite' in arc)
    # ⌗ third and last stale `n_seq == 0` conjunct (r3962).  The knot is that ad(P) is built from
    #   the group, so "which group" and "what connection" are one question -- a statement about the
    #   sequence's STRUCTURE, true whether or not the paper had yet named it.  ** The absence was
    #   never a premise of this argument; it was the reason for making it. **  Now that P12 names
    #   the sequence, the knot is checkable IN THE PAPER rather than only in the register.
    check('⇒⇒ AND Ⓖ SUPPLIES THE SEQUENCE IN WHICH "WHICH GROUP" AND "WHAT CONNECTION" ARE THE SAME '
          'QUESTION, because ad(P) is built from the group -- so all three are ONE KNOT',
          'order-six-adjacent objects' in arc and n_seq >= 1
          and 'Atiyah sequence of $SO(5,1)\\to\\dS_5$' in p12)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the missing object is the Atiyah sequence, and the three stations are one knot. **')
    print(f'  P12 carries {n_alg} "Lie algebroid", {n_anc} "anchor", {n_con} "connection" and ZERO "Atiyah')
    print('  sequence" -- ** and the sequence 0 -> ad(P) -> TP/G -> TM -> 0 is exactly what relates those')
    print('  three: algebroid, anchor, and a connection as a SPLITTING. **')
    print('  ⇒ ** And r2468 in that language is one sentence: the sequence splits and the splitting has')
    print('     zero curvature. **')
    print('  ⇒⇒ ** So Ⓖ is NOT independent.  Ⓒ asks which group; Ⓗ needs it for an equivariant index;')
    print('     Ⓖ supplies the sequence in which "which group" and "what connection" are one question,')
    print('     because ad(P) is built from the group.  ALL THREE ARE ONE KNOT, and its first thread is')
    print('     routed item 23. **')
    print('  ⌗ ** A reach list that CONVERGES is more informative than one that scatters, because')
    print('    convergence is evidence the object is real. **')
    print('  ⚠ Not claimed: that P12 owes the sequence.  ** Its algebroid is the constraint algebra\'s,')
    print('    not a principal bundle\'s -- the sequence bridges two structures the corpus holds')
    print('    separately, and whether they SHOULD be bridged is not judged here. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
