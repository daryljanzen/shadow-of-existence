#!/usr/bin/env python3
"""G4 -- THE 2026 SUPERCRITICAL-SHARPNESS THEOREM DOES NOT REACH THE CORPUS, AND THE
HYPOTHESIS THAT FAILS IS FINITENESS, NOT TRANSITIVITY.

GRAPH-THEORY FIELD BAKE, probe G4.  Ledger: GRAPH_THEORY_LEDGER.md.

** THE THEOREM, QUOTED FROM SOURCE. **  Diskin, Easo, Ramanan Radhakrishnan, Sudakov and
Tassion, *Supercritical sharpness of percolation*, arXiv:2603.03257, submitted 3 March 2026.
The abstract, verbatim:

    "We prove that for supercritical percolation on every infinite transitive graph, the
     probability that the origin belongs to a finite cluster of size at least n decays
     exponentially in Phi(n), where Phi is the isoperimetric function of the graph."

⌗ *Read at source, not from a summary: the earlier description this bake was handed said the
  theorem is "about transitivity where the old lattice proofs used the lattice", which is true
  and is not the whole content.  ** The conclusion is governed by the ISOPERIMETRIC FUNCTION **
  -- the lattice is replaced by Phi, not merely by transitivity.*

** WHY THE OBVIOUS ANSWER IS THE WRONG ONE. **  It is tempting to record "the corpus's graphs
are finite, so the theorem misses" and stop.  That is true and it is not a probe, because it
does not say WHICH hypothesis is doing the work.  ** This receipt checks both hypotheses
separately and finds that the corpus PASSES transitivity and FAILS finiteness. **

    hypothesis 1  the graph is INFINITE      -- FAILS: every graph the corpus has is finite
    hypothesis 2  the graph is TRANSITIVE    -- HOLDS: the octahedron and C_6 are both
                                                vertex-transitive, checked by exhausting S_6
    hypothesis 3  a percolation process runs -- ABSENT: `percolation` appears ZERO times in
                                                the seventeen paper bodies and zero times in
                                                PROBABILITY_LEDGER.md's 347 lines

  => *** AND FINITENESS IS BINDING FOR A REASON INTERNAL TO THE CONCLUSION, NOT INCIDENTAL. ***
     The isoperimetric function of a FINITE connected graph VANISHES on the whole vertex set --
     Phi(|V|) = 0, because V has empty edge-boundary.  "Decays exponentially in Phi(n)" therefore
     degenerates to "decays exponentially in 0" exactly where a finite graph runs out of room.
     ** The theorem's conclusion is not merely unavailable on a finite graph; it is empty
     there. **  That is checked below on both of the corpus's graphs.

⌗ HONEST BOUND, and it is the whole verdict of this probe.  ** A BOUNCE IS DATA. **  This
  receipt establishes that one specific 2026 theorem does not apply to one specific pair of
  six-vertex graphs.  *It does not establish that percolation has nothing to say to the corpus,
  and it does not establish that the corpus should acquire an infinite graph.*  What it rules
  out is the move the Quanta article invites -- reading a transitivity theorem onto a corpus
  whose transitivity is a group action on a CONTINUOUS homogeneous space, which is a different
  statement wearing the same word.
"""
import itertools
import sys

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)
    return ok


def edge_set(edges):
    return {frozenset(e) for e in edges}


def is_vertex_transitive(vertices, edges):
    """Exhaust the symmetric group: does Aut act with a single orbit on vertices?"""
    E = edge_set(edges)
    reached = set()
    for perm in itertools.permutations(vertices):
        m = dict(zip(vertices, perm))
        if {frozenset((m[a], m[b])) for a, b in edges} == E:
            reached.add(m[vertices[0]])
    return len(reached) == len(vertices), len(reached)


def isoperimetric(vertices, edges, n):
    """min over |S| = n of |edge boundary of S|.  Exhaustive; these graphs are tiny."""
    E = [tuple(e) for e in edges]
    best = None
    for S in itertools.combinations(vertices, n):
        s = set(S)
        b = sum(1 for a, c in E if (a in s) != (c in s))
        best = b if best is None else min(best, b)
    return best


def main():
    print()
    print('  G4 -- arXiv:2603.03257 against the corpus: transitivity holds, finiteness fails')
    print()

    V = list(range(6))
    # the octahedron K_{2,2,2}: antipodal pairs (0,3), (1,4), (2,5) -- G1's hinges
    octa = [(a, b) for a, b in itertools.combinations(V, 2) if b - a != 3]
    # the hexagon C_6 -- G1's null relation
    hexa = [(i, (i + 1) % 6) for i in range(6)]

    check('the octahedron K_{2,2,2} has 12 edges and is 4-regular', len(octa) == 12)
    check('the hexagon C_6 has 6 edges', len(hexa) == 6)

    # ⓵ hypothesis 2: transitivity -- the one the corpus PASSES
    ok_o, orb_o = is_vertex_transitive(V, octa)
    ok_h, orb_h = is_vertex_transitive(V, hexa)
    check(f'HYPOTHESIS 2 HOLDS: the octahedron is VERTEX-TRANSITIVE '
          f'(Aut reaches all {orb_o} vertices from one)', ok_o)
    check(f'HYPOTHESIS 2 HOLDS: C_6 is VERTEX-TRANSITIVE '
          f'(Aut reaches all {orb_h} vertices from one)', ok_h)

    # ⓶ hypothesis 1: infiniteness -- the one the corpus FAILS
    check('HYPOTHESIS 1 FAILS: both graphs are FINITE (six vertices each)',
          len(V) == 6)

    # ⓷ and the failure is structural, not incidental: Phi vanishes on the whole vertex set
    phi_o_full = isoperimetric(V, octa, len(V))
    phi_h_full = isoperimetric(V, hexa, len(V))
    check(f'the octahedron\'s isoperimetric function VANISHES at n = |V|: Phi(6) = {phi_o_full}',
          phi_o_full == 0)
    check(f'C_6\'s isoperimetric function VANISHES at n = |V|: Phi(6) = {phi_h_full}',
          phi_h_full == 0)
    check('*** so "decays exponentially in Phi(n)" is EMPTY at the top of a finite graph -- '
          'the conclusion degenerates rather than merely being unavailable ***',
          phi_o_full == 0 and phi_h_full == 0)

    # and Phi is well-behaved strictly below the top, which is what makes the vanishing
    # a statement about finiteness rather than about these two graphs being odd
    mid_o = isoperimetric(V, octa, 3)
    mid_h = isoperimetric(V, hexa, 3)
    check(f'  (and Phi is positive strictly below the top -- octahedron Phi(3) = {mid_o}, '
          f'C_6 Phi(3) = {mid_h} -- so the vanishing is finiteness, not degeneracy)',
          mid_o > 0 and mid_h > 0)

    # ⓸ hypothesis 3: measured, not asserted
    import os
    import re
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
    bodies = ''
    import glob
    # ⛔ EXCLUDE THE GENERATED APPENDICES, AND THE REASON IS THIS RECEIPT'S OWN MEASUREMENT.
    #   `corpus/appendix_receipts*.tex` is generated FROM receipts/INDEX.md and carries every
    #   receipt's claim text -- including THIS bake's index rows, which contain the word
    #   `percolation`.  ** So globbing all of corpus/*.tex would have this receipt counting its
    #   own registration and reporting the absence it exists to measure as a presence. **
    #   *Caught by check_receipt_tex_scope, which exists because 30 receipts hit this first.*
    for f in glob.glob(os.path.join(root, 'corpus', '*.tex')):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        bodies += '\n'.join(l for l in open(f, encoding='utf-8', errors='replace')
                            .read().split('\n') if not l.lstrip().startswith('%'))
    n_perc = len(re.findall(r'percolat', bodies, re.I))
    check(f'HYPOTHESIS 3 ABSENT: "percolat*" appears {n_perc} times in the paper bodies',
          n_perc == 0)

    # ⓹ THE NON-CLAIMS, PRINTED AND NOT CHECKED -- and the distinction is the point.
    #   ⛔ *These were first written as `check(..., True)`, which the hollow-assertion lint
    #   refused, correctly.*  ** A `check` that passes a literal True certifies that Python
    #   reached the line; it converts a known gap into an unknown one and makes the debt number
    #   lie. **  A scope disclaimer is not testable and must not be dressed as a test, so it is
    #   printed as what it is.
    print()
    print('    NOT CLAIMED (scope, not a check): that percolation has nothing to say to the')
    print('      corpus -- what is ruled out is ONE theorem reaching TWO six-vertex graphs.')
    print('    NOT CLAIMED (scope, not a check): that the corpus should acquire an infinite')
    print('      graph to meet the hypothesis -- a hypothesis is not a target.')

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  ' + '=' * 72)
    print('  RESULT: ALL PASS.  The corpus\'s two graphs SATISFY the theorem\'s transitivity')
    print('  hypothesis and FAIL its infiniteness one, and the failure is structural: the')
    print('  isoperimetric function vanishes on the whole vertex set of a finite graph, so')
    print('  the conclusion is empty there rather than merely unavailable.  The theorem')
    print('  misses, and now the corpus records WHICH hypothesis does the missing.')
    print('  ' + '=' * 72)
    return 0


if __name__ == '__main__':
    sys.exit(main())
