# WP-B — the order-three bridge: no AFFINE identification at fixed cubic (r986; scope corrected r1430)
> **⌖ RETIRED r1451 — read in full, then filtered into `CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md`.** Its live content went to
> nothing outstanding — the question was resolved this session (P7 `rem:tworealisations`, receipt `order3_bridge.py`). Kept as record; **do not plan from this file.** If something here is not reachable from
> `CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md`, that is a filtering miss — raise it there rather than reviving this.



> ## ⚠ SCOPE CORRECTION (r1430) — this verdict is narrower than it reads
> **What this WP established and what it did not.** Item 3 below is exact and stands: an **affine** map
> `r ↦ ar+b`, applied at **fixed cubic**, cannot carry colinear-real roots to equilateral ones, so **no
> change of variable in r identifies the two root sets**. The **Verdict** section then states this as "the
> bridge, as a structural identification, does not close" — which reads as a general negative and is not one.
> The test is affine-in-r at fixed cubic and is **structurally blind to a relation that deforms one cubic
> into the other**.
>
> **Such a relation exists and is geometric.** Radial geodesics turn on `r³ + (E²−1)α²r + 2Mα² = 0`, one
> family indexed by energy, whose two ends *are* these two cubics: **E=1** (marginally bound, k=0, the flat
> leaf) is the comoving/turnaround cubic; **E=0** (k=+1) is the horizon cubic. The separating de Sitter term
> is the coefficient **E²−1 = −k**, the Friedmann curvature constant. The corpus already carried the family
> (`slicing_operator.tex` §306, eq:Ek — "one congruence at three energies"); it had never been connected here.
> The two root configurations differ because the family **crosses its own discriminant** between the ends,
> `Δ = 4α⁴(α²(1−E²)³ − 27M²) = 0` at `1−E² = 3(M/α)^{2/3}` — and at Nariai that crossing arrives exactly at
> E=0, the same statement as the horizon cubic's double root. So the affine obstruction is the crossing seen
> from its two ends, **not evidence the two three-folds are unrelated**.
>
> **Unchanged and still do-not-assert:** the identification of the two root sets (the A₂ resemblance).
> **Withdrawn:** the "Frontiers wording" by-product below, which proposed *closing* a P7 frontiers item on
> the strength of the over-broad reading. It was never applied to P7, and it must not be.
> Receipt: `turnaround_excursion_work/two_realisations.py`. Landed: `CR_framework.tex`, `rem:tworealisations`.
> Cost of the over-broad phrasing: it caused a later node to retract sound work before tracing the reasoning.


Receipt: `computations/order3_bridge.py` (stages 1–4, all pass/print as described).
Status of the result: **held as established** for the negative/structural claims below
(each is a clean computation or standard algebra); the antimatter-naming and sheet-assignment
consequences remain do-not-assert.

## The question
Is the groupoid's order-three (sky-angle ℤ/3, `w → w + 2π/3`, on the roots of the horizon cubic
`r³ − r + 2M = 0`) the **same** ℤ/3 as the bead's order-three (`r → e^{2πi/3} r` under
`τ̃ → τ̃ + i·2πα/3`, from `r = A sinh^{2/3}(3τ̃/2α)`)? The notes lean on "the groupoid triple"
(`SESSION_FIGURES_CONSOLIDATION.md:44`, `BEAD_WALK.md:92`); thm:bead calls it "the order-three the
companion groupoid analysis carries." This tests whether that is a theorem or a resemblance.

## What is rigorously established

1. **The cosmic-time law satisfies `(dr/dτ̃)² = 1 − f`** (symbolic, exact; stage 4a). Hence the
   **cosmic-time reading turns where `1 − f = 0`**, while the **slicing curve** `(dr/dℓ)² = |f|`
   **turns where `f = 0`**. Two different turning conditions — the corpus's own scope note
   (`CR_framework.tex:750`), here made an identity.

2. **Each order-three belongs to a different cubic:**
   - groupoid ℤ/3 = the Galois ℤ/3 of the **horizon** cubic `f=0`: `r³ − r + 2M = 0`;
   - bead ℤ/3 = the cube-root ℤ/3 of the **comoving-turnaround** cubic `1−f=0`: `r³ + 2M = 0`.

3. **The two cubics are affinely inequivalent** (stage 4b–d). In the complex-r plane the horizon
   roots are **three colinear real points** (casus irreducibilis, sub-Nariai); the comoving roots
   are an **equilateral triangle** (`e^{2πik/3}`, one real + a conjugate pair at ±120°). An affine
   map `r ↦ ar+b` preserves colinearity, so it cannot carry one configuration to the other. No
   change of variable identifies the cubics.

4. **Different covers, different branch loci, opposite degeneration** (stages 2–3):
   - groupoid: 3-sheeted cover of the **mass line**, branch points at **Nariai** `M=±1/(3√3)`;
   - bead: cover of the **cosmic-time line at fixed Nariai mass**, branch point at the **seam** `r=0`;
   - at Nariai the groupoid ℤ/3 **degenerates** (double root, σ's fixed point) exactly where the
     bead ℤ/3 is **clean** (three distinct sheets). The bead lives over a single point (Nariai) of
     the groupoid's base; and the bead's branch (r=0) is the groupoid's **R-fixed point** (a ℤ/2,
     the mass reflection), not its ℤ/3.

## The only sense in which they are "the same order-three"
`S₃` has a **unique** order-three subgroup (the alternating `A₃`). So each cubic's Galois ℤ/3 is
"the" ℤ/3 abstractly — as is every ℤ/3; this is content-free. A *nontrivial* identification would
have to identify the two `S₃`'s (the two root sets), which is exactly the **A₂ / "triality"
resemblance the corpus already logs do-not-assert** (`OPEN_PROBLEMS_MAP.md` J7). Invoking it to
bridge stacks one do-not-assert on another.

## Even if granted, the bridge does not close the sheet-assignment
A groupoid↔bead ℤ/3 iso would label the bead's sheets by **horizon-root index**, not by
**congruence** (A / B / photon). The congruence labels come from the ruling geometry
(`slicing_operator.tex`), an independent structure. So the order-three bridge is **neither
established nor sufficient** for "which congruence rides which sheet."

## Verdict (corrected r1430 — the r986 wording asserted a general negative the computation cannot support)
**Established:** the two order-threes are the Galois/cube-root ℤ/3's of two different turning cubics
(`f=0` vs `1−f=0`), over different bases, branched at different loci, degenerating oppositely at Nariai;
and **no affine map `r ↦ ar+b` identifies their root sets** — affine maps preserve colinearity. "Same
order-three" is true only in the trivial sense that S₃ has a unique ℤ/3.

**NOT established, and not decidable by the above:** that the two cubics are unrelated. The affine test acts
**at fixed cubic** and is blind to a deformation between them. One exists and is geometric: radial geodesics
turn on `r³+(E²−1)α²r+2Mα²=0`, whose **E=1** end (k=0, flat leaf) is the comoving cubic and **E=0** end
(k=+1) is the horizon cubic — the separating term being the coefficient **E²−1 = −k**, the Friedmann
curvature constant, a family `slicing_operator.tex` §306 (eq:Ek) already carries. The configurations differ
because the family crosses its discriminant, `Δ = 4α⁴(α²(1−E²)³−27M²) = 0` at `1−E² = 3(M/α)^{2/3}`, between
the ends; at Nariai that crossing lands exactly at E=0, the same statement as the horizon cubic's double
root. The affine obstruction is that crossing seen from its two ends.

**Open (do-not-assert), unchanged:** whether the A₂ structure at the E=0 end survives the crossing to E=1 —
i.e. whether the two root sets are identified nontrivially. The family makes the question exact; nothing
here answers it. Receipts: `receipts/P07_CR_framework/order3_bridge.py` (stage 5), and
`turnaround_excursion_work/two_realisations.py`.

## Productive by-products (these redirect the program, they don't dead-end it)
- **A clean lemma for the corpus:** `(dr/dτ̃)² = 1 − f`, sharpening the `CR_framework.tex:750`
  scope note from prose to an identity, and cleanly separating the horizon cubic (slicing) from
  the comoving cubic (cosmic time). Candidate home: P7 or P3.
- **The sheet-assignment (C3) needs a different route.** Not the groupoid. The honest route is the
  **ruling-continuation** computation: analytically continue each real congruence (A ruling, B
  ruling, at-rest photon) off the real axis and see which sheet (`Im 0`, `+πα/3`, `−πα/3`) it lands
  on — directly, from the ruling geometry. That is the next real target for C3.
- **A real figure for WP-D:** the complex-r plane the current plate never draws is *exactly* the
  equilateral-triangle root configuration of the comoving cubic (the bead's genuine complex-r ℤ/3),
  set beside the colinear-real horizon roots. This both shows the missing C×C slice and makes the
  distinction visual.
- **~~Frontiers wording~~ — WITHDRAWN r1430 (it proposed closing an open item on the over-broad reading; never applied to P7, and must not be):** the P7 frontiers item currently says "whether the cosmic-time order-three
  is isomorphic to the groupoid's is itself an open theorem." This computation answers it: the
  natural bridge does **not** close; propose sharpening the item to say so (receipt cited), rather
  than leaving it "open."
