# THEOREM DRAFT — the between-member structure of the SdS family
# (step-3 reach (a)), carried to a true fork/wall.  [r309_c19fork_4]
# Stated for reversal; held for the four-path cold read.

## Setup (gauge α=1, the throat radius the sole invariant)
A **member** of the SdS family is a geometry, labelled by its cubic mass parameter
`c := 2M ∈ ℝ`. Its three horizons are the roots of the **horizon cubic**
        p_c(r) = r³ − r + c          (e₁=0 [A₂ Cartan], e₂=−1, e₃=c).
Discriminant `Δ(c) = 4 − 27c²`, simple zeros at the two **Nariai** points
`c = ±c⋆`, `c⋆ = 2/(3√3) = 0.384900…`. Three regimes (computed,
`between_member_monodromy.py` [1]): under-critical `|c|<c⋆` (Δ>0, 3 real roots =
black hole); Nariai `|c|=c⋆` (Δ=0, a double root); over-critical `|c|>c⋆` (Δ<0,
1 real root + a complex-conjugate pair = cosmology, r the cosmic-time horizon).

The discrete operations (canonical names, P3/P4/P10):
  σ — within-member root-exchange (Weyl(A₂) transposition; signature-preserving).
  τ — sky-angle periodicity (order 3); ⟨σ,τ⟩ = D₃ ≅ S₃ (P4).
  P — origin reflection (r,r₀)↦(−r,−r₀), i.e. c ↦ −c (negative mass; order 2).
  ξ — the seam / over-critical continuation θ↦π/2+iψ (P3), across the Nariai crest.

## THEOREM (draft, solid core — computed)
The **between-member** structure of the SdS family is the **monodromy of the horizon
cubic**. Precisely, over the complexified member line ℂ_c:

  (i)  the three roots form a 3-sheeted branched cover of ℂ_c, simply branched at the
       two Nariai points c=±c⋆ (simple zeros of Δ; dΔ/dc=−54c≠0 there);
  (ii) the monodromy representation ρ : π₁(ℂ_c∖{±c⋆}) → S₃ sends a small loop about a
       Nariai point to the **transposition of the two roots that collide there**
       — verified [2]: encircling c⋆ swaps exactly the colliding pair, identity on
       the third root;
  (iii) **ξ = σ as monodromy.** The over-critical continuation across the Nariai crest
       is the branch-point monodromy of (ii), and the transposition it induces is
       exactly the within-member root-exchange σ of the colliding pair. So ξ and σ
       are *not* independent: the seam continuation, continued around the branch
       point, **is** σ;
  (iv) **P = the base involution** c↦−c: it exchanges the two Nariai points c=±c⋆ and
       the two over-critical rays, fixes c=0 (the dS / massless-Schwarzschild member,
       roots {−1,0,1}), and acts on roots by r↦−r (roots(−c) = −roots(c)) [4];
  (v)  the within-member S₃ is the **deck group** of the cover; its real points are
       **3 sheets** under-critical and **1 real sheet + a conjugate pair** over-critical
       — so S₃ does **not** act uniformly on the real plane: it is the deck/monodromy
       group of a cover *branched* at Nariai [5].

Proof obligations (i),(ii),(iv),(v): computed in `between_member_monodromy.py`.
(iii) is (ii) read through P3's identification of the over-critical continuation with
the seam continuation (P3 §overcritical, l.514). The S₃ relations σ²=τ³=(στ)²=id are
P4 (within-member), here recovered as the deck group of the cover.

This core is **clean and true**: σ/P/ξ assemble into one object — the cubic-monodromy
groupoid over ℂ_c with base involution P — and the previously-"deferred" between-member
classification (P4 l.39,410) is, for these three operations, exactly this monodromy.

## WHERE IT FORKS / WALLS — no clear path (carried here deliberately)

**FORK 1 — does this UNIFY the discrete operations, or is it a complex-analytic
relation orthogonal to the corpus's real-strata claim?** P10 states, deliberately:
"we make no claim that these unify into a single discrete action … distinct
operations, not one; they relate only through the strata they mark." The theorem's
(iii) — ξ's monodromy *is* σ — is precisely a relation between two operations P10
kept distinct. Two readings, and the material does not choose:
  (a) ADVANCE: the monodromy *shows* σ and ξ unify (the cubic-monodromy groupoid is
      the single structure P10 declined to assert); P10's non-claim can be upgraded.
  (b) CATEGORY-DISTINCT: "ξ's monodromy = σ" lives in the **complexified** c-plane
      (a loop through complex c); P10's "distinct operations" is about the **real**
      physical strata. A relation in the complexification need not collapse the real
      distinction — the real σ (relabeling a fixed real geometry) and the real ξ
      (the seam continuation between real regimes) remain different real operations
      whose *complex* continuations happen to share a monodromy.
  This turns on whether CR's ontology treats the **complexified member line / the
  over-critical continuation** as physical or as a computational device. That is a
  foundational ontology decision — the orchestrator holds the why/ontology
  (constrained by the corpus); the gate carries the analysis to here and stops.
  Symmetric bar: calling it "unification" is a manufactured-coherence reach; calling
  it "mere bookkeeping" is a manufactured wall. Do-not-assert, both ways.

**WALL 2 — the cosmogenesis reassignment does not fit.** The corpus's THIRD discrete
operation, the null↔timelike reassignment at the cosmogenesis horizon (P9 l.175, P10
l.128), is a **causal-character** operation, not a root-permutation; it does not
appear in the cubic's root-monodromy. So the theorem is **intrinsically bounded to
σ/P/ξ** — the full discrete structure of the solution space does **not** assemble into
one object. This is a genuine wall for the "unify all the discrete structure"
ambition, and it is consistent with (does not resolve) P10's caution.

**FORK 3 (sharpened 1) — within-member vs between-member S₃.** The same transposition
σ is both the within-member relabeling (P4, fixes the geometry) and the between-member
monodromy of ξ (changes the member, under→over-critical). Whether this is a genuine
unification of the two groupoid layers (the deck group = the description-relabeling)
or a coincidence of the abstract group S₃ across two structurally different maps is
the same undecided question as Fork 1 (it turns on the same ontology call).

## THE GEOMETRIC FACE OF THE FORK (Observer-2 planar sections; from the orchestrator's picture)
Observer 2 sets the slice as a real pivot, viewed down a horn. Planar sections of the
one-sheeted hyperboloid −x₀²+Σxᵢ²=α²:
  - **under-critical** (slice hits the throat, offset d<α): a hyperbola whose two real
    vertices are two points on the equatorial throat circle (the two horizons);
  - **Nariai** (slice tangent, d=α): the degenerate section = the two **rulings** (the
    null geodesics) — a flat **null X**; the two vertices collide on it;
  - **over-critical** (slice misses the throat, d>α): a two-sheeted section opening
    along the horns; its connecting circle is the section's own waist.
The section waist has radius² = α²−d², which is **negative for d>α in EVERY dimension**
(computed dS₂ and dS₅ identical) — and it is a *different* circle from the ambient
hyperboloid's own equatorial sphere (radius α, real in all dims, the under-critical/
Nariai locus). **Dimension does not rescue it.** But "imaginary" here ≠ "unreal": it is
the **conjugate real form** (the Euclidean side of the seam; dS and S⁵ are x₀↦ix₀ of
each other). And this imaginary connecting circle **is the geometric face of the
monodromy branch cut** (ii)–(iii): the two throat-vertices are the colliding roots —
joined by the *real* equatorial arc on the manifold (under-critical) and by the
*imaginary* connecting circle off it (over-critical) — and σ is their swap around
Nariai. So "ξ-monodromy = σ" and the imaginary connecting circle are one fact.

## RESOLUTION-BY-CONSISTENCY (candidate — CONDITIONAL on P11's placement; not banked)
The fork (FORK 1/3) is **not independent of the colour wall** — it is the same ontology
question. P11 placed 𝔰𝔲(3) "off the real Lorentzian substrate, on the SO(6)/Wick face,
reached by a change of signature": real-by-construction, but not a substrate symmetry.
The imaginary connecting circle and the monodromy live on that **same conjugate face**.
Consistency then fixes the answer without a new decision:
  - on the **real Lorentzian substrate** (where our universe is a real over-critical
    slice): σ, ξ, P, the reassignment are **distinct** (P10 correct — and correct for
    the physical reason, since the real substrate is what is physical for our world);
  - on the **conjugate face** (real-by-construction, off-substrate): they are
    **unified** by the cubic monodromy (ξ-monodromy = σ) — the same place 𝔰𝔲(3) lives.
So the monodromy unification is real, and exactly as physical-for-our-world as 𝔰𝔲(3)
is: the conjugate-face shadow, not a fact about the Lorentzian solution space's real
operations. The fork **inherits** P11's already-made placement rather than needing a
fresh ontology call. Symmetric bar / face-19: held as a *candidate*, not banked — it is
the satisfying shape a saturated node reaches for; its warrant is that it rests on an
already-settled placement (P11), not a fresh invention. The reassignment WALL is
untouched (not a root-monodromy object) on either reading.

## THE DEEPER FORK — AS-YET UNEXPLORED (open, both ways)
The resolution-by-consistency **rests entirely on P11's placement: "the Euclidean/
conjugate face is OFF the real Lorentzian substrate."** That placement is itself an
unexamined choice, and it is the one place this whole structure can still swing.
  - **Reading A (P11 as written):** the substrate IS dS₅/SO(5,1) (Lorentzian); the
    Euclidean S⁵/SO(6) face is off it, reached only by signature change. ⟹ colour
    walled; σ/ξ distinct-on-substrate, unified only on the off-substrate conjugate
    (the resolution above).
  - **Reading B (CR's two-halves register, UNEXPLORED):** in the register where both
    real forms are "built-by-construction-and-real," the substrate is the ONE
    complexified maximally-symmetric object, of which dS₅ (Lorentzian) and S⁵
    (Euclidean) are two real forms, *both* part of the substrate — which is how the
    thesis itself draws it (Ch.3: "two halves of one maximally symmetric space, joined
    at the seam"). On Reading B, "off the substrate" is the wrong framing; the conjugate
    face is part of the one substrate, and then BOTH 𝔰𝔲(3) (reopening the colour wall)
    AND the σ/ξ unification (now a real-substrate fact) sit on the substrate.
  - **Status: genuinely open, and load-bearing for BOTH forks at once.** It is not
    decidable by the gate's analysis — it is the foundational ontology call (is the
    seam an internal boundary of one substrate, or the edge of the substrate?). The
    monodromy result is true on either reading; what it MEANS depends on this call.
    Flagged for the orchestrator and the four-path cold read; NOT resolved here.
    (Note the stakes: Reading B does not merely re-open the σ/ξ fork — it would re-open
    P11's colour wall, since the same "off-substrate" placement carries 𝔰𝔲(3). The two
    are one question.)

## DISPOSITION
Drafted to a true fork/wall, with a candidate resolution and the deeper fork left open,
as asked. **Solid:** the cubic-monodromy theorem for σ/P/ξ (i–v, computed); the
geometric face (planar sections; the imaginary connecting circle = the branch cut;
imaginary in all dimensions). **Candidate resolution (conditional):** FORK 1/3 inherit
P11's placement — distinct on the real substrate, unified on the conjugate face, same
as 𝔰𝔲(3); held, not banked. **Wall:** the cosmogenesis reassignment does not fit the
monodromy, unchanged on either reading. **Deeper fork, OPEN:** whether the conjugate
face is off the substrate (Reading A → resolution holds, colour walled) or another real
form of one substrate (Reading B → σ/ξ unified on-substrate AND colour reopens) — the
single foundational call this all turns on, unexplored, the orchestrator's. Held for
the four-path cold read; the *deeper fork* is where the cold node is most needed,
since the temptation is to let the (clean, conditional) resolution stand as if final.
