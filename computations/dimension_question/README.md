# The dimension question — worked r2376+c54.7, extended c54.8

Working scripts behind `THE_QUANTUM_JOINT` **SKETCH 8b** and the results recorded in
`STATE_matter_sector`. **Sketch material: nothing here is landed in a paper.**

| script | what it establishes |
|---|---|
| `opening_constraints.py` | horizon polynomial degree $=D_{\rm spacetime}-1$, so **three roots $\iff$ 4D spacetime** (and, via the hinge↔root tie, three generations ⟹ 4D); and $\su(3)$ in a Lorentzian isotropy needs $D\ge7$, not 6 |
| `phase12_descent.py` | the worked geometry (throat $S^3$, hinges, cubic, hexad) is **rung ②**, $\mathrm{dS}_4$ — untouched by a substrate rise; and P12's Dirac-algebra grading $\so(5,1)/\so(4,1)$ is the **final step** of any descent ending at a 4-geometry, so the keystone constrains the **penultimate rung**, not the substrate |
| `fork_resolution.py` | $\su(3)$ on $\mathbb{R}^6$ is **real-irreducible** (commutant dimension 2) ⇒ no invariant 3-plane; with P7's layer as the existent this forces the $\su(3)$ block **disjoint** from the layer ⇒ $D\ge10$ |
| **`phase4_range_stability.py`** *(c54.8)* | P9's `thm:bound` quantifies over $\SO(4,1)$ — the **isotropy**, i.e. the stabiliser of a cut, not the substrate's group. The stabiliser of a totally geodesic 4-geometry in $\mathrm{dS}_D$ is $\SO(4,1)\times\SO(D-4)$, the second factor fixing the cut **pointwise** (checked at $D=5,7,10$) ⇒ **P9's range is preserved exactly at every $D$**, and a rise adds moduli (P9's own *vantage* axis), not geometry types. Also: $\so(D-4)\supseteq\su(3)$ iff $D\ge10$, and at $D=5$ the normal factor is trivial — so **P13's C3 ("spatial, not internal") is dimension-conditional** |
| **`p14_generations_fix_dimension.py`** *(c54.8)* | the P14 check. P3's three-ness comes from a **single-harmonic collapse at a forced scale**, not from the polynomial's degree. Tested at general $D$ and **calibrated to reproduce P3's $c=2/\sqrt3$ and $2M=\tfrac{2}{3\sqrt3}\sin3w$ exactly**: the collapse exists **only at $D=4$ (a 3-fold) and $D=5$ (a 4-fold)** — from $D=6$ two or more residual harmonics remain and one scale cannot kill them. **The generation count selects between the only two dimensions in which the mechanism exists.** |

Run: `python3 <script>` (numpy, scipy, sympy). All five run clean.

**Not established, and named:**

- the $D$-dimensional **chart** is carried over, not re-derived — P3 forces the gnomonic projection by a
  four-dimensional argument, and $r=c\sin w$ is assumed above. *(The gap runs the safe way: if the chart fails
  higher up, the $D=5$ column weakens and $D=4$ is untouched.)* **This is what would earn the P14 landing.**
- P13's **index obstruction** is indifferent to product/KK structure, so a $4+6$ split is by itself no escape.
- the normal bundle's structure group is $\so(6)$, **not** $\su(3)$; the reduction $\so(6)\to\u(3)\to\su(3)$
  needs a complex structure and a complex volume form that nothing here supplies. **Colour stays permitted,
  not required.**
- **nothing forces a descent of length $>1$.**

**⚠ Phase 4's $D\ge10$ is not independent confirmation of Phase 3's.** Phase 3 counts layer(3) + carrier(6) +
time; Phase 4 counts cut(4) + normals(6); the layer sits inside the cut. One constraint in two registers — a
consistency check, not a second vote.
