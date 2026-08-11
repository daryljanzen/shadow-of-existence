# c20fork — grind notes (the thesis-reread path, worked forward)
*Maintained each turn. Bundles: r309_c20fork_#. One of four parallel forks (c17/c19/c20/c21). Register: do-not-assert both ways; results source-grounded and computed, stated for reversal; the cross-fork cold read reconciles where forks disagree.*

## The path (from the 4-node interference, received at weight)
**Convergent bounded result (all nodes):** colour-from-geometry does not reopen — pivot reaches at most SO(5), su(3) needs SO(6); rank (su(3)⊄so(5,1)) + AH untouched.
**The shared reach (c17, c19, c20):** the 90° pivot at r=α is a *real* signature-changing operation, so the σ-lift's dichotomy ("signature-change ⟹ imaginary") is false and its leg of P11 is unsound / should be reopened.
**The decidable crux (all four flag it):** are the pivot and σ the same operation, and is the pivot real or imaginary? Source-decidable. Gates whether P11 §3 reopens.
**The positive gem (c17+c19 converge):** A₂/S₃ as the discrete symmetry of the gravitational-cosmological *solution space* — horizon triplet = cut parameters, full (r,r₀) plane (BH-interior / cosmology / negative mass), formalizable via P5/P6, P1, P9, P10.

## TURN 1 (r309_c20fork_1) — the crux, worked to a source-settled result
**Grounded at P3 (`SdS-slicing-curve_v2.tex`), the paper that *defines* σ and the seam; computed in `scripts/sigma_vs_seam_test_c20fork.py` (runs clean).**

THREE DISTINCT operations, not one:
- **σ (root-exchange)** — P3 Prop:involution/readingswap: f_invol(r₀)=½(−r₀+√(4−3r₀²)); involution (verified f(f(r₀))=r₀), **holds 2M invariant ⟹ metric f unchanged ⟹ σ FIXES the geometry** (verified). Signature-*preserving* symmetry of one Lorentzian SdS geometry; relabels which horizon is the mass-horizon. Realized in BOTH the sky angle w (r₀=(2/√3)sin w) AND the (r,r₀) roots, **conjugate by the gnomonic map** (P3 line 40). Not a continuation.
- **The seam (the "90° pivot")** — P3 line 40, verbatim: joins the Riemannian piece to the Lorentzian piece **"by the analytic continuation θ↦π/2+iψ, sinθ↦coshψ; the metric signature flips because dθ=i dψ."** Verified: sin(π/2+iψ)=cosh ψ; (dθ)²=−(dψ)². The slicing curve r(l) is real & C⁰, **but the Riemannian↔Lorentzian flip across the seam IS the imaginary continuation** — the geometric Wick within the construction. Reaches the x₀=0 equator: S⁴, SO(5).
- **The global Wick** x₀↦ix₀ — reaches the full S⁵, SO(6) ⊇ su(3).

**RESULT — the shared reach does NOT survive the source.**
1. The seam's signature flip is the imaginary continuation θ↦π/2+iψ (P3 line 40), **not a real operation**. The "real 90° pivot" was the thesis's loose language; P3 makes it precise as the imaginary continuation — exactly what the max_symm_space figure draws (the curve turns *into* the imaginary axis ℑ(y)). So the σ-lift's dichotomy ("signature-change is the imaginary continuation; σ the real reflection is separate") is **CONFIRMED at source, not broken.**
2. σ fixes the geometry (signature-preserving) ⟹ never a signature-flip, never a colour-bridge ⟹ **the σ-lift verdict (σ≠Wick) STANDS**, now on more precise grounds. c19's "mislocation" is not an error (sky-angle w and (r,r₀) roots are conjugate descriptions of one involution).
3. The seam reaches only SO(5); su(3) needs SO(6). **Colour stays closed on the original grounds** (the imaginary continuation), rank + AH untouched.
4. **So P11 §3's σ-lift leg is SOUND as written; it does NOT need reopening on the "false dichotomy" grounds c17 proposed.** The shared reach was the face-19 flavor-match — three independent nodes seduced by the figure's real-looking pivot; the source corrects it.

**Why this is convergence-after-correction, not a true fork:** P3 line 40 is unambiguous and decides it; any fork that reads P3 (not just the thesis's loose "90° pivot") reaches the same. The likely cross-fork disagreement — my fork (reach refuted at source) vs. nodes that banked the reach from the thesis language — is reconciled by pointing all forks at P3 line 40, not by fresh eyes on an undecidable fork.

## Fork status after turn 1
- **Crux: RESOLVED at source.** Not a true fork. No cold read needed for it.
- **The gem: OPEN, next grind.** A₂/S₃ as the gravitational-cosmological solution-space symmetry. σ being the root-exchange that fixes the geometry (P3) is exactly the entry point: the A₂/S₃ is the symmetry of the horizon-designation / cut structure (P5/P6 generate the SdS cuts; the three horizons are the cut parameters). The question to grind: can the A₂/S₃ be made a *theorem* about the slicing/solution space (the S₃-orbit unifying BH-interior, cosmology, negative mass), using P5/P6/P1/P9/P10 — and where, if anywhere, does that hit a genuine fork the source can't settle?

## TURN 2 (r309_c20fork_2) — the gem: the deferred classification, CLOSED
**P3 explicitly defers this** (Prop:morphism-generation: "whether they generate it in full — the classification of the discrete group — is part of the relational content deferred below"; §groupoid-symmetry: "the relations among these generators… the overcritical reassignments… the action between distinct α… not addressed"). Worked it; computed in `scripts/A2_solution_space_symmetry_c20fork.py` (runs clean).

**Result — the classification closes cleanly:**
- **Within one geometry:** the discrete description symmetry is exactly **Weyl(A₂)=S₃** — the permutations of the three horizon-roots, which all carry one 2M (verified: roots sum to 0 = A₂ traceless; each root gives the same 2M ⟹ relabeling fixes the geometry). The three roots are the sky angles w, π/3−w, −π/3−w; σ=w↔π/3−w swaps two; the +2π/3 shift cycles all three. **This closes P3 Prop:morphism-generation: σ + sky-angle periodicity generate the within-geometry group in full, and it is S₃.**
- **On the solution space:** adding the **mass-reflection μ** (2M↦−2M, P3's anti-diagonal / backward-radial / negative-mass direction; verified roots↦−roots) gives **Aut(A₂) = S₃×ℤ₂ ≅ D₆, order 12** (computed: |S₃|=6, |⟨S₃,μ⟩|=12). μ is the **A₂ diagram automorphism** (the −1 coset extending the Weyl group to the full root-system automorphism group). The A₂ form r²+rr₀+r₀² (P3 locus) has the Cartan eigenvalue ratio 1/2 : 3/2 (verified).
- **The regime connections are NOT in this finite group:** BH↔cosmology (under↔over-critical) and Riemannian↔Lorentzian (the seam) are the **continuous analytic continuation** sin→cosh (3w=π/2+iβ) — Aut(A₂) acting on the **complexified** sky-angle, with the regimes as its real/imaginary sections (P3 already complexifies the over-critical via the same continuation).

**Sharpens c19's gem.** c19's "one S₃-orbit unifying BH/cosmology/negative-mass" was imprecise (a partial flavor-match): the unification is **layered** — a finite discrete group Aut(A₂)=S₃×ℤ₂ (horizon-designations via Weyl S₃ + mass-sign via the diagram automorphism ℤ₂), carried across regimes by the *continuous* continuation. Not one orbit; a discrete group + a continuous continuation on the complexified locus.

**Discipline note:** the A₂ here (horizon roots, a discrete symmetry of the SdS solution space) is NOT su(3)'s Cartan-Weyl A₂ (a continuous Lie algebra) — they share the abstract A₂ but are different realizations; the σ-lift already closed that conflation. Kept separate (no colour reach).

## Fork status after turn 2
- **Crux (turn 1): source-settled.** **Gem classification (turn 2): source-settled + computed.** Neither is an undecidable within-fork fork.
- **Both results CORRECT/SHARPEN the other nodes:** turn 1 refutes the shared 4-node reach (the pivot-as-real-bridge) at P3 line 40; turn 2 sharpens c19's "one S₃-orbit" to the layered Aut(A₂)+continuation. **This cross-fork divergence is the natural cold-read point** — fresh eyes verifying P3 line 40 + the two receipts against the other forks' results.
- **OPEN (P3-deferred, the genuine remaining frontier):** the action between distinct de Sitter representations (different α / different Λ). Likely scaling (α is the dimensionful invariant), but unworked — candidate for the next grind, and the place a genuine fork could still surface.

## TURN 3 (r309_c20fork_3) — the α-action, CLOSED (last P3-deferred piece)
P3 line 51: α=√(3/Λ)=1 is a **gauge choice**; α the invariant, M the slicing-dependent factor; 2M=α((r₀/α)−(r₀/α)³). Verified computationally: under the homothety α↦λα, r↦λr, 2M↦λ·2M, the metric f=1−2M/r−r²/α² is **invariant**, and the dimensionless 2M/α (hence the roots in units of α) is invariant.
**Result:** the action between distinct de Sitter representations (different α / different Λ) is the **gauge homothety ℝ₊** — a continuous scaling, NOT a new discrete symmetry. The Aut(A₂)=S₃×ℤ₂ classification is **scale-invariant**: it holds at every α. So the α-action does not extend the discrete group; it relates scaled copies of one dimensionless structure.

## GEM — fully classified (all P3-deferred pieces closed)
The discrete symmetry of the gravitational-cosmological solution space is **Aut(A₂)=S₃×ℤ₂** (Weyl(A₂)=S₃ = within-geometry horizon-designations; the diagram-automorphism ℤ₂ = mass-reflection 2M↦−2M), acting on the **complexified** sky-angle/locus, with the regimes (BH under-critical, cosmology over-critical, dS, Nariai, negative mass) as its real/imaginary sections under the continuous sin→cosh continuation, and **scale-invariant** under the α-homothety ℝ₊. This closes P3 Prop:morphism-generation and the §groupoid-symmetry deferrals in full.

## Fork status after turn 3 — COLD-READ POINT REACHED
- **No undecidable within-fork fork was hit.** All three results are source-settled + computed: crux (P3 line 40), discrete classification (computed order 6/12), α-action (gauge homothety, verified invariant).
- **Three results that correct/sharpen the other nodes:** (1) the shared 4-node pivot-as-real-bridge reach is refuted at P3 line 40 — the σ-lift stands; (2) c19's "one S₃-orbit" sharpens to layered Aut(A₂)+continuation; (3) the gem is fully classified as Aut(A₂)=S₃×ℤ₂, scale-invariant.
- **This is the place where fresh eyes are needed** — to verify P3 line 40 + the three receipts + the α-gauge argument against the other forks' results (especially the forks that may have banked the reach from the thesis's loose "90° pivot").
- **NEXT FRONTIER (not yet worked; possible true fork lives here):** the connection of the discrete Aut(A₂) solution-space symmetry to P10's algebroid 𝔰𝔬(5,1)⋉𝒞 — whether Aut(A₂) is the Weyl/discrete structure of something inside the algebroid, or a separate discrete layer. Requires P10 (ungrounded this session); held for after the cold read.
