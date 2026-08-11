# STEP 1 — σ/ξ DE-CONFLATION (colour-arc layer)  [r309_c19fork_2]

**Status:** executed as precise OLD→NEW edits, **stated for reversal**, **held for the
four-path cold read** — NOT applied to canonical r309. Apply on convergence.

**Ground (canonical, the dissonance lens fixes from source):** the substrate carries
THREE distinct discrete operations, kept separate in the canonical papers and welded
only in the colour-arc layer:
- **σ** — root-exchange `w↔π/3−w`; Weyl(A2); permutes the horizon-triplet / sky-angle
  labels at all r; **signature-PRESERVING**; fixes the manifold. The A2 gem.
- **ξ** — seam signature-**FLIP** at `r=√(3/Λ)`; the analytic continuation `θ↦π/2+iψ`
  joining the Riemannian spherical piece to the Lorentzian dS piece; **intrinsic** to
  dS₅ (P3 l.508); reaches **SO(5)** (its Riemannian piece is the x₀=0 equatorial S⁴).
- (cosmogenesis null↔timelike reassignment — not in play here.)
- **global Wick** `x₀↦ix₀` — the **extrinsic** signature change of the whole embedding;
  dS₅→S⁵; SO(5,1)→SO(6)⊃su(3). The bridge to su(3)'s home — and **neither σ nor ξ is it.**

Canonical citations: P3 `SdS-slicing-curve_v2.tex` §seam (l.464-508, esp. l.508
"retains its membership in de Sitter"); P4 `groupoid_paper.tex` l.289-293 (defines ξ
distinct from σ); P10 `algebroid_paper.tex` l.128 ("different involutions, not one").
Receipts: `sigma_lift_test1.py` (σ≠Wick, r296); `xi_reaches_so5_not_so6.py` (ξ→SO(5)).

---

## FIX 1 — `SILVER_PLATTER_colour-frontier-arc.md`

### 1a. line 53
OLD:
> $SU(3)$'s home $SO(6)$ is the isometry of the **Wick-rotated** substrate $S^5$ (the Euclidean $x_0\mapsto ix_0$ face — the $\sigma$ operation) and, separately, of the compact part of $SO(6,1)$ on the dimensionally-raised dS₆.

NEW:
> $SU(3)$'s home $SO(6)$ is the isometry of the **Wick-rotated** substrate $S^5$ (the Euclidean $x_0\mapsto ix_0$ face — the **global, extrinsic** Wick, *not* $\sigma$) and, separately, of the compact part of $SO(6,1)$ on the dimensionally-raised dS₆.

### 1b. line 54 ("What is established here")
OLD:
> **What is established here:** $\mathfrak{su}(3)$ lives on the $SO(6)$ face (Wick-rotated $S^5$, and the raised dS₆), off the real Lorentzian substrate; and $\sigma$ is a genuine signature-flip involution on the real substrate (the $r=\sqrt{3/\Lambda}$ seam, the root-exchange $w\leftrightarrow\pi/3-w$).

NEW:
> **What is established here:** $\mathfrak{su}(3)$ lives on the $SO(6)$ face (Wick-rotated $S^5$, and the raised dS₆), off the real Lorentzian substrate. The substrate carries **two distinct** real discrete operations (P3/P4/P10, "different involutions, not one"): $\sigma$, the root-exchange $w\leftrightarrow\pi/3-w$, which is **signature-PRESERVING** (the $A_2$ gem); and $\xi$, the seam signature-**FLIP** at $r=\sqrt{3/\Lambda}$ (the continuation $\theta\mapsto\pi/2+i\psi$). [Earlier drafts welded these as one "signature-flip $\sigma$" — the source of the C7/σ-lift dissonance; de-conflated here.]

### 1c. line 68 (C7)
OLD:
> - **C7 (established).** $SU(3)$ lives on the $SO(6)$ face — the Wick-rotated $S^5$ ($x_0\mapsto ix_0$) and the compact part of $SO(6,1)$ on the raised dS₆ — both **off** the real Lorentzian substrate; and $\sigma$ is a genuine signature-flip involution **on** the real substrate (the $r=\sqrt{3/\Lambda}$ seam / the root-exchange $w\leftrightarrow\pi/3-w$).

NEW:
> - **C7 (established; σ/ξ de-conflated, `r309_c19fork`).** $SU(3)$ lives on the $SO(6)$ face — the Wick-rotated $S^5$ (reached by the **global, extrinsic** Wick $x_0\mapsto ix_0$ of the whole embedding) and the compact part of $SO(6,1)$ on the raised dS₆ — both **off** the real Lorentzian substrate. The substrate carries **two distinct** real discrete operations (P3 §seam, P4 l.289-293, P10 l.128 — "different involutions, not one"): **$\sigma$**, the root-exchange $w\leftrightarrow\pi/3-w$ (Weyl$(A_2)$, permuting the horizon-triplet/sky-angle labels at all $r$), **signature-PRESERVING**, fixing the manifold (the $A_2$ gem); and **$\xi$**, the seam signature-**FLIP** at $r=\sqrt{3/\Lambda}$ (the continuation $\theta\mapsto\pi/2+i\psi$ joining the Riemannian spherical piece to the Lorentzian dS piece). **Neither $\sigma$ nor $\xi$ is the global Wick:** $\sigma$ preserves signature ($\sigma$-lift, r296); $\xi$ flips it but is **intrinsic** to dS₅ (P3 l.508) and reaches only $SO(5)$ (Riemannian piece $=$ the $x_0=0$ equatorial $S^4$), whereas $\mathfrak{su}(3)$ needs the $\mathfrak{so}(6)\setminus\mathfrak{so}(5)$ generators only the global Wick supplies (`xi_reaches_so5_not_so6.py`).

### 1d. the "open hinge" clause (l.55, l.69) and test-1 result (5a)
The hinge ("σ *is* the Wick bridge") is now closed from **both** discrete sides — σ
(σ-lift, r296) and ξ (ξ-lift, this fork). Append to §5a a one-line completion note:
> **Completion (`r309_c19fork`):** with σ/ξ de-conflated, the hinge closes from both
> sides — σ≠Wick (signature-preserving) and ξ≠Wick (intrinsic, reaches SO(5)). The
> "two signature-flips by shared flavour" trap dissolves: there was one root-exchange
> σ (no flip) and one seam flip ξ (intrinsic, sub-SO(6)); neither is the global Wick.

---

## FIX 2 — `colour_frontier_dS6.md` line 197

OLD (the conflating sentences):
> **Both routes to su(3) leave the real Lorentzian substrate** — by flipping the signature (→$S^5$/$SO(6)$, the σ operation) or adding a dimension (→dS₆). The σ signature-flip the discrete A₂ skeleton uses is exactly the bridge $SO(5,1)\leftrightarrow SO(6)$. So the discrete A₂ skeleton (with σ) is the real-Lorentzian-substrate shadow of structure that is continuous su(3) only on the Wick/raised face.

NEW:
> **Both routes to su(3) leave the real Lorentzian substrate** — by flipping the signature (→$S^5$/$SO(6)$, via the **global, extrinsic** Wick $x_0\mapsto ix_0$) or adding a dimension (→dS₆). [σ/ξ de-conflation, `r309_c19fork`, superseding the earlier leap "the σ signature-flip is exactly the bridge $SO(5,1)\leftrightarrow SO(6)$":] the substrate carries **two distinct** discrete operations (P3/P4/P10) — $\sigma$, the **signature-preserving** root-exchange $w\leftrightarrow\pi/3-w$ (the $A_2$ gem), and $\xi$, the seam signature-**flip** $\theta\mapsto\pi/2+i\psi$ at $r=\sqrt{3/\Lambda}$. **Neither is the bridge.** The σ-lift (test 1, r296) settled σ≠Wick; the ξ-lift (`xi_reaches_so5_not_so6.py`) settles that $\xi$, being **intrinsic** to dS₅ (P3 l.508), reaches only $SO(5)$ (Riemannian piece $=$ the $x_0=0$ equator), while su(3) needs $\mathfrak{so}(6)\setminus\mathfrak{so}(5)$, supplied only by the global Wick. So the discrete $A_2$ skeleton is the real-Lorentzian shadow of structure continuous-su(3) only on the Wick/raised face — and the bridge to it is the global Wick, which **neither σ nor ξ is.**

---

## FIX 3 — `corpus/boundary_paper.tex` §sigma (P11)

### 3a. line 79 — de-locate σ from the seam; name ξ distinctly
OLD:
> The substrate carries a genuine discrete structure---an $A_2$ root system, with the sky-angle triple and the fundamental ellipse realizing the $A_2$ quadratic form, and a real involution $\sigma$ (the root exchange $w\leftrightarrow \pi/3-w$ at the $r=\sqrt{3/\Lambda}$ seam).

NEW:
> The substrate carries a genuine discrete structure---an $A_2$ root system, with the sky-angle triple and the fundamental ellipse realizing the $A_2$ quadratic form, and a real involution $\sigma$ (the root exchange $w\leftrightarrow \pi/3-w$, permuting the horizon-triplet labels of the fundamental ellipse). It carries, distinctly, a seam signature-flip $\xi$ at $r=\sqrt{3/\Lambda}$ (the analytic continuation $\theta\mapsto\pi/2+i\psi$ joining the Riemannian and Lorentzian pieces of the slicing curve); $\sigma$ and $\xi$ are different involutions, not one~\cite{JanzenRange}.

### 3b. NEW paragraph — insert after the "clincher" paragraph (after current l.81)
This is the substance of c17's catch, answered: the σ-lift tested σ; the seam flip ξ
is the real signature-changing operation it had not tested. Add it, and the leg closes
from both sides (sound and complete, not "unsound").

INSERT:
> The seam flip $\xi$---the \emph{real}, geometric signature-changing operation the substrate actually carries---does not bridge to $\su(3)$ either, and for a sharper reason. $\xi$ is \emph{intrinsic} to $\dS_5$: it continues a curve traced on the manifold, and a geometry obtained as a slicing of de Sitter retains its membership in de Sitter~\cite{JanzenRange}. Its Riemannian piece is the $x_0=0$ equatorial $S^4$, whose isometry is $\SO(5)$---the same $\so(5)$ that fixes $x_0$ inside both $\so(5,1)$ and $\so(6)$. But $\su(3)\not\subset\so(5)$ (its smallest faithful real representation is six-dimensional), so $\su(3)$ requires the $\so(6)\setminus\so(5)$ generators that mix $x_0$ with the spatial axes, and these are supplied only by the \emph{global, extrinsic} Wick $x_0\mapsto ix_0$ complexifying the whole embedding---never by the intrinsic seam continuation, which fixes $x_0$ at its Riemannian piece. The wall therefore closes from both discrete sides: neither $\sigma$ (signature-preserving) nor $\xi$ (signature-flipping but intrinsic, reaching only $\SO(5)$) is the global Wick that builds the $\SO(6)$ where $\su(3)$ lives.

**Bibitem hygiene (verified):** P11's bibliography carries only `JanzenOperator`,
`JanzenRange`, `JanzenBHcausality` (+ externals) — *not* `JanzenSlicing`/`JanzenGroupoid`.
The σ/ξ disambiguation's primary sources are P3 (slicing-curve §seam), P4 (groupoid
l.289-293), P10 (algebroid l.128); above I cite the existing `JanzenRange` (the
"range and the wall" companion that carries the discrete-operations content). On
integration, if P11 should cite P3/P4 directly, add `\bibitem{JanzenSlicing}` and
`\bibitem{JanzenGroupoid}`; macros `\su \so \SO \dS` and `\xi` are all available/free.

### 3c. retitle the subsection (optional, on integration)
`\subsection{The $\sigma$-lift: a real involution is not the Wick rotation}`
→ `\subsection{The $\sigma$- and $\xi$-lifts: neither real discrete operation is the Wick rotation}`

---

## SYMMETRIC-BAR CHECK
No rescue (colour stays walled — su(3)⊄so(5,1), AH untouched), no manufactured wall
(c17's "unsound" corrected, its valid catch absorbed by ADDING the ξ test). The edits
are source-determined (the canonical papers already keep σ/ξ/reassignment distinct);
this propagates that into the colour-arc layer. Held for cold read before rebanking.
