#!/usr/bin/env python3
"""G1 -- THE SIX HINGE-ENDS CARRY AN OCTAHEDRON, AND ITS ANTIPODAL PAIRS ARE THE HINGES.

GRAPH-THEORY FIELD BAKE, probe G1.  Ledger: GRAPH_THEORY_LEDGER.md.

** WHAT P03 ALREADY HAS. **  `P03_hexagon_null_triple` computes the causal character of all
fifteen pairs of the six hinge-ends from one formula -- ends at stations th_a on horns
eps = +-1, with

      X.Y = alpha^2 ( -3 eps eps' + 4 cos(th_a - th_b) )

-- and finds a clean trichotomy: TIMELIKE <=> same hinge (3 pairs), spacelike <=> same horn
(6), NULL <=> neither (6).  P03's prose then reads ONE of the three classes as a graph:
*"six vertices of degree two, bipartite between the horns, which is why the closed figure is
a hexagon and why it alternates."*  ** That reading is correct and this receipt does not
dispute it. **

** WHAT THIS PROBE ADDS, AND IT IS THE OTHER TWO CLASSES. **  3 + 6 + 6 = 15 = C(6,2), so the
trichotomy is a complete EDGE-3-COLOURING OF K_6.  Read as graphs:

      timelike  (same hinge)  3 edges, every degree 1  ->  a PERFECT MATCHING (1-factor)
      spacelike (same horn)   6 edges, every degree 2  ->  TWO DISJOINT TRIANGLES, 2K_3
      null      (neither)     6 edges, every degree 2  ->  the HEXAGON C_6  (P03's reading)

  => *** AND THE COMPLEMENT OF THE TIMELIKE MATCHING IS THE OCTAHEDRON. ***  Deleting the three
     same-hinge pairs from K_6 leaves a 4-regular graph on six vertices in which every vertex
     has EXACTLY ONE non-neighbour -- which is the definition of K_{2,2,2}, the octahedral
     graph.  ** Its three antipodal pairs are exactly the three hinges. **

** WHY THAT IS WORTH A RECEIPT AND NOT JUST A NAME. **  The octahedron is the statement that
the causal relation "not timelike-separated" on the hinge-ends is as symmetric as it can be:
K_{2,2,2} is vertex-transitive AND edge-transitive, and the ONLY structure distinguishing one
vertex from another is which antipode it has.  *So "an end is characterised by its hinge and
nothing else" is a graph-theoretic statement, and this is the graph that says it.*

⌗ HONEST BOUND.  This receipt computes a decomposition of a FINITE graph on six vertices from
  a formula P03 already states.  ** It establishes no new physics ** -- every causal fact it
  uses is P03's, verified here rather than assumed.  What is new is the naming: the corpus
  reads one of the three classes as a graph and leaves the other two, and their complement,
  unnamed.  *A name is not a theorem; it is what lets the next reader see that these are three
  facts about one object.*

⛔ AND IT IS NOT A PERCOLATION OBJECT.  Six vertices is finite; the 2026 supercritical-sharpness
  theorem (arXiv:2603.03257) is about INFINITE transitive graphs and is not in contact with
  this.  That bounce is probe G4's and is recorded there, not smuggled in here.
"""
import itertools
import math
import os
import re
import sys

ALPHA = 1.0
FAILED = []

#: ⛭ r7159+70.1 (70): P03's THREE COUNTS ARE READ FROM P03.  They were literals beside "P03 sec:tour" in a file
#: that opens no paper (`check_unread_figure`, r7151: NO-READ/FIGURE), so `sec:tour` could change a class count
#: and this receipt would stay green.  ⇒ *They are parsed from `sec:tour`'s one display -- "timelike ... (3),
#: spacelike ... (6), null ... (6)" -- the pattern required to match exactly once.*  The geometry is unchanged.
_P03 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus', 'SdS-slicing-curve_v2.tex')
with open(_P03, encoding='utf-8') as _fh:
    _SRC = _fh.read()
_tour = re.findall(r'\\text\{timelike\}\\iff\\text\{same hinge\}\\ \((\d+)\),\\qquad\s*'
                   r'\\text\{spacelike\}\\iff\\text\{same horn\}\\ \((\d+)\),\\qquad\s*'
                   r'\\text\{null\}\\iff\\text\{neither\}\\ \((\d+)\)', _SRC)
assert len(_tour) == 1, f'P03 sec:tour: the class display matches {len(_tour)} time(s), not once'
P03_TOUR = dict(zip(('timelike', 'spacelike', 'null'), (int(x) for x in _tour[0])))


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)
    return ok


def main():
    print()
    print('  G1 -- the six hinge-ends as a graph: matching + 2K_3 + C_6, and the octahedron')
    print()

    # the six ends: three hinges (stations 120 deg apart), two horns each
    ends = [(k, e) for e in (+1, -1) for k in range(3)]
    theta = lambda k: 2.0 * math.pi * k / 3.0

    def dot(A, B):
        (ka, ea), (kb, eb) = A, B
        return ALPHA ** 2 * (-3.0 * ea * eb + 4.0 * math.cos(theta(ka) - theta(kb)))

    check('the object is six ends = 3 hinges x 2 horns', len(ends) == 6)

    cls = {'timelike': [], 'spacelike': [], 'null': []}
    for A, B in itertools.combinations(ends, 2):
        d = dot(A, B)
        if abs(d - 7.0) < 1e-9:
            cls['timelike'].append((A, B))
        elif abs(d + 5.0) < 1e-9:
            cls['spacelike'].append((A, B))
        elif abs(d - 1.0) < 1e-9:
            cls['null'].append((A, B))
        else:
            cls.setdefault('unclassified', []).append((A, B, d))

    # ⓵ P03's own counts, recomputed rather than quoted
    for _c in ('timelike', 'spacelike', 'null'):
        check(f"P03 sec:tour: {_c} pairs number {len(cls[_c])}, the display's printed {P03_TOUR[_c]}",
              len(cls[_c]) == P03_TOUR[_c])
    check('the trichotomy is COMPLETE -- 3+6+6 = 15 = C(6,2), no pair unclassified',
          'unclassified' not in cls
          and len(cls['timelike']) + len(cls['spacelike']) + len(cls['null']) == 15)

    # ⓶ each class read as a graph
    def degrees(edges):
        d = {v: 0 for v in ends}
        for a, b in edges:
            d[a] += 1
            d[b] += 1
        return sorted(d.values())

    check('TIMELIKE is a PERFECT MATCHING -- every degree exactly 1',
          degrees(cls['timelike']) == [1] * 6)
    check('  and it is exactly the SAME-HINGE relation',
          all(a[0] == b[0] for a, b in cls['timelike']))

    check('spacelike is 2-REGULAR -- every degree exactly 2',
          degrees(cls['spacelike']) == [2] * 6)
    check('  and it is exactly the SAME-HORN relation, so it is TWO DISJOINT TRIANGLES',
          all(a[1] == b[1] for a, b in cls['spacelike'])
          and sorted(len([e for e in cls['spacelike'] if e[0][1] == h]) for h in (+1, -1)) == [3, 3])

    check('NULL is 2-REGULAR -- every degree exactly 2', degrees(cls['null']) == [2] * 6)
    check('  and every null pair is cross-horn AND different-hinge, which is P03\'s '
          '"bipartite between the horns"',
          all(a[1] != b[1] and a[0] != b[0] for a, b in cls['null']))

    # the null class is a single 6-cycle, not two triangles: bipartite forbids odd cycles,
    # and 2-regular + connected on six vertices is C_6.  Walked rather than asserted.
    adj_null = {v: [] for v in ends}
    for a, b in cls['null']:
        adj_null[a].append(b)
        adj_null[b].append(a)
    start = ends[0]
    walk, prev, cur = [start], None, start
    for _ in range(6):
        nxt = [w for w in adj_null[cur] if w != prev][0]
        prev, cur = cur, nxt
        walk.append(cur)
    check('  and walking the null relation returns to the start after exactly SIX steps '
          '-- one hexagon, not two triangles',
          walk[6] == start and len(set(walk[:6])) == 6)

    # ⓷ the complement of the timelike matching
    comp = cls['spacelike'] + cls['null']
    adj = {v: set() for v in ends}
    for a, b in comp:
        adj[a].add(b)
        adj[b].add(a)
    check('deleting the 3 timelike pairs from K_6 leaves 12 edges, 4-regular',
          len(comp) == 12 and degrees(comp) == [4] * 6)
    non_neighbours = {v: [w for w in ends if w != v and w not in adj[v]] for v in ends}
    check('*** every vertex has EXACTLY ONE non-neighbour -- this is K_{2,2,2}, '
          'THE OCTAHEDRON ***',
          all(len(non_neighbours[v]) == 1 for v in ends))
    check('*** and each vertex\'s unique non-neighbour is its OWN HINGE\'S other end -- '
          'the octahedron\'s antipodal pairs ARE the three hinges ***',
          all(non_neighbours[v][0][0] == v[0] and non_neighbours[v][0][1] != v[1]
              for v in ends))

    # ⓸ the naming claim, stated as a NON-relation so a later reader cannot infer more
    check('NOT CLAIMED: that this is new physics -- every causal value used here is P03\'s '
          'own formula, recomputed (the three dot products are 7, -5, 1 in units of alpha^2)',
          abs(dot(ends[0], ends[3]) - 7.0) < 1e-9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  ' + '=' * 72)
    print('  RESULT: ALL PASS.  The causal trichotomy on the six hinge-ends is a complete')
    print('  edge-3-colouring of K_6: a perfect matching (the hinges), two triangles (the')
    print('  horns), and a hexagon (the null relation).  Deleting the matching leaves the')
    print('  OCTAHEDRON, whose antipodal pairs are exactly the hinges.  P03 names the')
    print('  hexagon and none of the rest.')
    print('  ' + '=' * 72)
    return 0


if __name__ == '__main__':
    sys.exit(main())
