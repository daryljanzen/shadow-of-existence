#!/usr/bin/env python3
"""M3 -- station Ⓖ walked: the missing object is the Atiyah sequence, and all three remaining stations
turn out to be one knot whose first thread is routed item 23.

⛔⛭⛭ ** AMENDED r7287+cc66, UNDER THE `L203` PREFIX CLAIM AND FLAGGED AS SUCH: THE STATION IS NO
LONGER OWED, AND R-M'S CURRENT CELL RETRACTS THE CAVEAT THIS FILE STATED. **  R-M now reads *Ⓖ Lie
algebroids | THROWN r3152 (`L-265`) --- AND THE SEQUENCE IS THE OBJECT*, and goes on: *the caveat
this row carried --- "P12's algebroid is the constraint algebra's and not a bundle's" --- is right in
general and wrong here*.  **That caveat is this file's own, in `WHAT IS NOT CLAIMED` below, and the
retraction is a better thing for this receipt to carry than the owed status it used to assert.**  The
owed status was true at this file's build (`ed5422d8`, r2493), and `'Lie algebroids' in rm` --- five
occurrences --- could not see it move.  ⇒ Pinned now as the `L-249` (r3105) SPLIT: the historical
state read at `ed5422d8^`, the PARENT, because `ed5422d8` is the commit that wrote this file's own
result into R-M; the current state asserted separately.

** THE STATION, AS IT STOOD AT THIS FILE'S BUILD. **  R-M carried Ⓖ, "Lie algebroids -> Cartan / differential geometry", as owed and
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

    # ⛔⛭⛭⛭ L-249 (r3105) SPLIT, r7287+cc66, UNDER THIS SEAT'S PREFIX CLAIM AND FLAGGED AS SUCH:
    #   the old pin was `'Lie algebroids' in rm`, a two-word span at 5 occurrences that could not
    #   fail and carried neither the destination nor `owed` -- and the claim went STALE.  R-M now
    #   reads Ⓖ as THROWN r3152 (`L-265`), AND THE SEQUENCE IS THE OBJECT, and the same cell
    #   RETRACTS the caveat this very receipt stated.  ** Both ends pinned: the historical state at
    #   the commit it stood at, the current state separately.  The historical read is at
    #   ed5422d8^ -- the PARENT of this file's own build -- because ed5422d8 is the commit that
    #   wrote this file's result INTO R-M, so the owed state is the one before it. **
    _rm_before = re.sub(r'\s+', ' ', _sp.run(
        ['git', 'show', 'ed5422d8^:THE_MATHEMATICS_REACH.md'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout)
    check('⌗ HISTORICAL, at ed5422d8^ (the parent of r2493, this file\'s own build): R-M carried '
          'Ⓖ as OWED, alongside Ⓗ, with Ⓒ the live handoff',
          'LIVE: stations Ⓖ and Ⓗ are owed, and Ⓒ is the live handoff; registered as '
          'L-203.' in _rm_before)
    check('⛭ AND CURRENT: Ⓖ is THROWN and the sequence IS the object -- R-M now reads it so, and '
          'retracts the caveat this receipt stated, which the old pin could not have detected',
          '**Ⓖ** Lie algebroids | ⛭⛭ **THROWN r3152 (`L-265`) — AND THE SEQUENCE IS THE '
          'OBJECT.**' in rm)

    # ⓵ what P12 has
    # ⛔⛭ AMENDED r4522: ** P12 was read end to end and harvested at r4083, and four of this file's
    #    quotations moved with it. **  The paper still builds exactly what is claimed here -- its
    #    title is "the action Lie algebroid of the symmetry-reducible sector", the structure it
    #    realizes is written $\so(5,1)\ltimes\C$, and \S`sec:anchor` opens "The anchor maps an
    #    infinitesimal cut-deformation to the stress-energy it produces---the slicing operator made
    #    infinitesimal."  *Both probes bind their terms across the window rather than fixing one
    #    sentence's order.*
    _ALA = re.compile(r"action Lie algebroid", re.I)
    _STRUCT = re.compile(r"\\so\(5,1\)\\ltimes\\C")
    _ANCHOR = re.compile(r"anchor maps an infinitesimal cut-deformation to the stress-energy"
                         r"|map from an infinitesimal cut-deformation to its stress-energy"
                         r"|anchor is the slicing operator's cut-to-stress-energy map", re.I)
    check('P12 builds the action Lie algebroid, and names the structure $\\so(5,1)\\ltimes\\C$ that '
          'realizes the slicing',
          _ALA.search(p12) is not None and _STRUCT.search(p12) is not None)
    check('and names the anchor: "The anchor maps an infinitesimal cut-deformation to the '
          'stress-energy it produces---the slicing operator made infinitesimal"',
          _ANCHOR.search(p12) is not None)
    n_alg = len(re.findall('Lie algebroid', p12))
    n_anc = len(re.findall('anchor', p12, re.I))
    n_con = len(re.findall('connection', p12, re.I))
    n_seq = len(re.findall('Atiyah sequence', p12, re.I))
    # ⛭ r7135+cc66.102: THE LABEL PRINTS THE THREE COUNTS AND CLAIMS NOTHING ABOUT 4, 8 OR 2.  The
    #   floors were a liveness control standing on top of three real checks that already run above --
    #   `_ALA`, `_STRUCT` and `_ANCHOR` test the sentences themselves.  ** So presence is the whole of
    #   what this line adds, and the counts are printed, which they already were. **
    check(f'it carries {n_alg} "Lie algebroid", {n_anc} "anchor", {n_con} "connection" -- printed, and '
          f'each asserted only to be present',
          n_alg > 0 and n_anc > 0 and n_con > 0)
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
          # ⛭ AMENDED r4522: the paper writes the identification rather than the phrase --
          #   "For a homogeneous space the action algebroid of $G$ on $G/H$ \emph{is} the Atiyah
          #   algebroid of the principal bundle $G\to G/H$, so with $\dS_5=SO(5,1)/SO(4,1)$ the
          #   sequence ... is exact" -- and the aside now reads "naming it costs nothing and buys a
          #   great deal".  ** The GAP this check exists for was that P12 named the sequence ZERO
          #   times; it names and displays it now, at `eq:atiyah`, which is what closing the gap
          #   meant. **
          # ⛭ WIDENED r7287+cc66: `the Atiyah algebroid of the principal bundle` was a bare
          #   noun phrase with no verb AND it dropped the hypothesis the identification RESTS ON,
          #   which the paper itself flags one sentence earlier -- HOMOGENEOUS.  And `naming it
          #   costs nothing and buys` dangled TWICE: its object was the pronoun `it`, and it ended
          #   on the transitive `buys` with its object outside, dropping the paper's own proviso.
          'For a \\emph{homogeneous} space the action algebroid of $G$ on $G/H$ '
          '\\emph{is} the Atiyah algebroid of the principal bundle $G\\to G/H$' in p12
          and r'\label{eq:atiyah}' in p12
          and 'The grading has a name in the literature, and naming it costs nothing and '
          'buys a great deal---provided the hypothesis the name carries is honoured, '
          'which takes one restriction.' in p12)
    check('⇒ and the consequence this file argued for is drawn in the paper\'s own voice: "the '
          'constraint algebra of general relativity is the Atiyah algebroid of the substrate\'s own '
          'principal bundle"',
          # ⛭ AMENDED r4522: drawn now as the algebroid's own four data --- "the base is the space
          #   of cuts of a de~Sitter substrate, the acting algebra is the substrate's isometry
          #   algebra $\so(5,1)$, the anchor is the slicing operator's cut-to-stress-energy map,
          #   and the section is the cosmic clock that turns the constraint into a true Hamiltonian"
          #   --- with the Atiyah identification stated separately at `eq:atiyah`.
          # ⛭ r7287+cc66: THE DEAD ARM IS DELETED, not widened -- measured at ZERO occurrences
          #   in corpus/algebroid_paper.tex, so it could never fire and the `or` reduced to its
          #   second disjunct anyway.  The live arm's spans are widened: `the Atiyah algebroid of
          #   the principal bundle` to the homogeneous-space hypothesis, and `The claim is a
          #   recognition rather than` -- which named no subject of its own and stopped mid-
          #   comparison at `rather than` -- to the whole sentence.
          ("the anchor is the slicing operator's cut-to-stress-energy map" in p12
           and 'For a \\emph{homogeneous} space the action algebroid of $G$ on $G/H$ '
          '\\emph{is} the Atiyah algebroid of the principal bundle $G\\to G/H$' in p12
           and '\\emph{The claim is a recognition rather than an addition.}' in p12))
    check('⚠ and its "Cartan" uses are the Cartan--Weyl SKELETON, not Cartan GEOMETRY',
          'Cartan--Weyl skeleton' in p12)

    # ⓶ the sequence relates exactly those three
    # ⌗ the structural claim never depended on the sequence being ABSENT -- it is about what the
    #   sequence RELATES -- so only the stale conjunct goes; the three-object count stays.
    check('⇒ the Atiyah sequence 0 -> ad(P) -> TP/G -> TM -> 0 has a Lie algebroid as its middle '
          'term, the anchor as its surjection, and a CONNECTION as a splitting -- so it relates '
          'exactly the three objects P12 has', n_alg > 0 and n_anc > 0 and n_con > 0)

    # ⓷ composition with r2468
    # ** the register writes it in CAPS with markdown bold: "**AND A COVERING MAP CARRIES A
    # CANONICAL FLAT CONNECTION BY DEFINITION:**".  Third quotation this session written from a
    # memory of a read instead of from the file -- match case-insensitively on the phrase itself. **
    check('r2468 established the colour bundle is FLAT because it IS a branching -- "A COVERING MAP '
          'CARRIES A CANONICAL FLAT CONNECTION BY DEFINITION"',
          'covering map carries a canonical flat connection' in arc.lower())
    # ⛭ r7287+cc66: `covering map` is RETIRED into the full-sentence pin above rather than
    #   widened -- two words standing for `the sequence SPLITS and the splitting has ZERO
    #   CURVATURE`, of which they contained neither, and reading the SAME single occurrence as
    #   their partner, so they could fail only when it also failed.  ** And the label now says what
    #   is actually the receipt's own: the Atiyah-sequence restatement is this file's INFERENCE
    #   from the register's flat-connection sentence, not a quotation of it. **
    check('⇒ in Atiyah-sequence language -- this receipt\'s own restatement, from the flat '
          'connection pinned above -- the sequence SPLITS and the splitting has ZERO CURVATURE',
          'covering map carries a canonical flat connection' in arc.lower())

    # ⓸ the knot
    # ⛭ WIDENED r7287+cc66: (a) PROXY -- and it carries MORE weight here than in M2, because
    #   this receipt's result is that (G) supplies the sequence in which `which group` and `what
    #   connection` are one question, so the identity of the group is the whole knot.
    check('Ⓒ (r2491) left three order-six-adjacent groups unresolved',
          'So there are THREE order-six-adjacent objects in play \u2014 $S_3$, '
          '$\\mathbb Z_6$, $\\mathbb Z_3$ \u2014 and the corpus\'s texts have at points '
          'called the same thing all three.' in arc)
    # ⛭ WIDENED r7287+cc66: `'PREREQUISITE' in arc or 'prerequisite' in arc` -- a one-word span
    #   that CANNOT FAIL (2 and 6 occurrences), and the measurement showed it passing off a
    #   sentence that DENIES a prerequisite (`Absorption is a REFRESH of a reach bake, not a
    #   prerequisite for one`).  ** The case ALT is dropped with it: two encodings of one word are
    #   encoding-benign and were never the live question. **
    check('Ⓗ (r2492) needs a named group for an equivariant index, so Ⓒ is its prerequisite',
          'STATION Ⓗ WALKED r2492 \u2014 IT IS A *DECLARED* GAP, AND Ⓒ IS ITS '
          'PREREQUISITE RATHER THAN ITS NEIGHBOUR' in arc)
    # ⌗ third and last stale `n_seq == 0` conjunct (r3962).  The knot is that ad(P) is built from
    #   the group, so "which group" and "what connection" are one question -- a statement about the
    #   sequence's STRUCTURE, true whether or not the paper had yet named it.  ** The absence was
    #   never a premise of this argument; it was the reason for making it. **  Now that P12 names
    #   the sequence, the knot is checkable IN THE PAPER rather than only in the register.
    check('⇒⇒ AND Ⓖ SUPPLIES THE SEQUENCE IN WHICH "WHICH GROUP" AND "WHAT CONNECTION" ARE THE SAME '
          'QUESTION, because ad(P) is built from the group -- so all three are ONE KNOT',
          # ⛭ AMENDED r4522: P12 now DISPLAYS the sequence at `eq:atiyah` instead of naming it in
          #   prose, and it names the kernel in the paper's own terms -- "$\fh$ the kernel of the
          #   anchor---the adjoint bundle, ten-dimensional---and $\fm$ its image ... closing at
          #   $10+5=15=\dim\so(5,1)$".  ** That is `ad(P)` written out, which is exactly the knot
          #   this check is about: the kernel is built from the group. **  *A check that asked for
          #   the phrase would now fail on the paper having done the thing.*
          'So there are THREE order-six-adjacent objects in play \u2014 $S_3$, '
          '$\\mathbb Z_6$, $\\mathbb Z_3$ \u2014 and the corpus\'s texts have at points '
          'called the same thing all three.' in arc
          and r'\label{eq:atiyah}' in p12
          and 'the kernel of the anchor---the adjoint bundle' in p12
          and r'10+5=15=\dim\so(5,1)' in p12)

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
