> **⌖ RETIRED r1552.** This was the C5-reducible build — the GR catalogue as substrate cuts (r570). **Landed:** P9 `range_paper` is that catalogue.
> Kept as record; **do not work from it.**


# C5-reducible — the GR catalogue as substrate cuts (geometric vs vantage multiplicity)

**Frontier:** P7 §frontiers item 3, the full classification of the admissible causal reassignments.
**Scope here:** the *reachable* (symmetry-reducible) sector only — Tier-0, leaning on established
results (P9 thm:range/thm:bound/§97/§155, P3/P4 the reading-swap, P12 the orientation parity,
P13/A4 the seam). The gated Kerr-inner / RN-interior cases are Tier-3, matter-side, NOT here.
This is a synthesis of established results into one classification, not a new theorem. Stated for
reversal.

## The master question (P7 §frontiers item 3, roadmap C5)
How much of the standard GR catalogue is **geometric multiplicity** (genuinely distinct cuts of the
substrate — distinct leaves / symmetry classes / bends) versus **vantage multiplicity** (one cut,
distinct causal readings on the fixed substrate)?

## The frame, grounded
- **The reachable set = the symmetry-reducible sector** (P9 thm:range §184): a geometry is a cut of
  the dS substrate exactly when its isometry group contains a sweep-subgroup of ŝo(5,1).
- **The reachable classes** (P9 thm:bound §65): SO(3) (spherical), SO(4)/E(3)/SO(3,1) (closed/flat/
  open FLRW), the Kantowski–Sachs group and the abelian translation groups (homogeneous / Bianchi),
  ℝ×SO(2) (stationary axisymmetric).
- **Within a class the operator is surjective**; the vacuum members are the substrate's own family,
  matter is the bend (P9 §70).

## Milestone 1 — the classification, first pass

### Vantage multiplicity (one cut, different causal readings — the *description groupoid*, P4)
- **de Sitter ↔ Schwarzschild** — the backward-radial vantage-swap r↦−r; two readings of one
  slicing of the fixed-α manifold, not two limits (P3 abstract/§sec:seam; P4 groupoid). *Vantage.*
- **±M charts (black hole ↔ naked)** — the orientation parity R∈O(5,1)\SO₀ sending 2M↦−2M; the two
  Lorentzian charts are one existent's shadow, the A₂ diagram automorphism (P12 §strata). *Vantage.*
- **Kantowski–Sachs ↔ flat-FLRW** — *the same SdS geometry* read in two different ŝo-classes
  (ℝ×S² anisotropic vs flat E(3)), differing by exactly the rest-energy "−1" in (dr/dτ)² (P9 §97).
  The apparent anisotropy is an artifact of which slicing one takes. *Vantage.*
- **Collapse interior ↔ cosmological expansion** — one ontological layer under the NBC causal
  reassignment (null↔timelike), the foliation preserved (P7 thm:null-boundary). *Vantage.*

### Geometric multiplicity (genuinely distinct cuts — different class / leaf / bend)
- Different **symmetry classes** are different cuts: spherical SdS, the FLRW isometry classes, the
  homogeneous/Bianchi classes, stationary-axisymmetric — each a distinct ŝo-subgroup class
  (P9 thm:bound). Non-transitive ŝo-action: different-mass SdS cuts are non-isometric (P12 §strata,
  R_ab R^ab separates them) — mass is a modulus *transverse* to the orbits. *Geometric.*
- The **vacuum kernels** by class (P9): the one-parameter SdS family (spherical); Kerr–NUT–(A)dS,
  the complete separable Type-D family (stationary axisymmetric, thm:pd §124); the Weyl functional
  class (static axisymmetric); the Bianchi families (homogeneous). Distinct leaves. *Geometric.*

### Matter-side (not vacuum cuts — the bend)
- **Charge** (RN–dS, Kerr–Newman–dS): electrovac, the charge the bend m(r)=M−Q²/2r, sourced by the
  Maxwell field; enters only through +Q², rotation-independent, C-blind (P9 §155). *Bend, not a cut.*
- **Acceleration** (the C-metric / Plebański–Demiański a): not a vacuum parameter — a bare
  accelerating mass leaves an irremovable conical strut; enters on the matter side as a bend
  (P9 §155). *Bend, not a cut.*

### The anchor entry — FRW-initial = the cosmogenesis seam
The flat-FLRW reading of SdS carries the sinh^{2/3} scale factor (P9 §97; P7/P13). Its beginning
(τ̃=0, r→0) is **not** a curvature singularity but the **finite-curvature Nariai degenerate seam**
— the cosmogenesis seam whose crossing A4 built (Nariai double root α/√3, dS₂×S², κ=0; the r=0
curvature singularity is perspectival and no finite-time layer reaches it, P7 §644). So in the
catalogue the "FRW initial singularity" is re-read as a *substrate-cut boundary* — the seam — not a
breakdown of the geometry. This is the entry the A4 build underwrites, and it ties the classification
to the recurring object of the whole programme (P9 §97: "the programme's recurring object is again
the seam").

## Milestone 2 — the per-class sweep (every reachable catalogue member placed)

Grounded in P9 thm:bound §65 (the reachable classes), thm:pd §124 (the Type-D kernel), §97
(the seam / the KS↔FLRW reading), §155 (charge & acceleration as bends), thm:range §184.

| Catalogue member | ŝo-class (P9 §65) | Vacuum kernel (P9) | Petrov | Classification |
|---|---|---|---|---|
| de Sitter | all classes' vacuum limit | the substrate itself | O | the fixed background — the one existent |
| FLRW closed/flat/open | SO(4) / E(3) / SO(3,1) | dS (matter = bend) | O | **geometric** (distinct classes); flat-FLRW ↔ KS is **vantage** (§97) |
| Schwarzschild–dS | SO(3) spherical | 1-param SdS family | D | **geometric** (mass modulus) + a **vantage** web (below) |
| Kantowski–Sachs | KS group | SdS interior + Nariai tangency | D | **vantage** of the SdS interior (§97); its Nariai member = the seam |
| Kerr–NUT–(A)dS | ℝ×SO(2) stationary axisym. | separable Type-D (thm:pd) | D | **geometric** (mass/rotation/NUT moduli; rotation = the shift, J∝Ma; twist alone → dS) |
| Bianchi I–IX (homogeneous) | abelian translation groups | Bianchi vacuum families | I (3 KVs) | **geometric** (anisotropic cuts) |
| Weyl / Zipoy–Voorhees | static axisymmetric | Weyl functional class | I (2 KVs) | **geometric** (functional kernel) |
| Reissner–Nordström–dS, Kerr–Newman–dS | spherical / axisym. | *not vacuum* — charge is the bend (§155) | D | **matter-bend** (RN-interior = gated Tier-3) |
| C-metric (accelerating) | — | *not vacuum* — acceleration is the bend, conical strut (§155) | D | **matter-bend** |

The vantage web on the *one* SdS geometry (the description groupoid, P4): the backward-radial swap
r↦−r (dS↔Schwarzschild, P3 §sec:seam); the orientation parity ±M (black-hole↔naked, P12 §strata);
the slicing/signature reassignment KS↔flat-FLRW (the rest-energy "−1", §97); the null↔timelike
reassignment collapse↔cosmology (the NBC, P7 thm:null-boundary). Four readings, one cut.

## The master statement

In the symmetry-reducible sector the catalogue's apparent multiplicity decomposes on **three
orthogonal axes**:

1. **Vantage** — a *discrete groupoid* of causal readings of one fixed cut (P4): the backward-radial
   swap (P3), the orientation parity ±M (P12), the KS↔flat-FLRW slicing reassignment (§97), the
   null↔timelike collapse↔cosmology reassignment (P7). Changes the reading, not the geometry.
2. **Geometric** — the *moduli of distinct vacuum cuts* within the reachable ŝo-classes (thm:bound):
   the vacuum kernels SdS (1-param), Kerr–NUT–(A)dS (finite separable Type-D, thm:pd), Weyl/Bianchi
   (functional), with mass/rotation/NUT the transverse moduli (the ŝo-action non-transitive, mass a
   modulus off the orbits, P12). Genuinely distinct geometries.
3. **Matter-bend** — *orthogonal to vacuum cuts*: charge and acceleration (§155), and general matter,
   entered as the bend off the kernel, not as cuts at all.

**Verdict.** The reducible catalogue is not a zoo of unrelated solutions: it is **one substrate read
through a finite vantage groupoid, over a moduli family of vacuum cuts, with matter the bend.**
Algebraic type is no constraint (O/D/I all reached, thm:range); Type D is the separable *corner*
where the substrate's symmetry surfaces as the Carter constant (cor:carter), not the edge. And the
FRW "initial singularity" is, on this classification, the finite-curvature **cosmogenesis seam**
(Nariai degenerate horizon, A4/§97) — a cut-boundary, not a breakdown of the geometry.

## Status
Milestones 1–2 built: the reachable-sector classification is synthesized — the frame, every
reachable catalogue member placed with its class / kernel / Petrov type, the vantage web on the SdS
geometry, and the single master statement — all from established results (P9/P3/P4/P12/P13/A4). This
covers C5-reducible's stated scope (classify the reachable catalogue as substrate cuts, sorting
vantage vs geometric vs matter-bend). **C5 as a whole stays open** on its gated Tier-3 remainder
(Kerr-inner / RN-interior, matter-side).

## Propagation (r570)
Propagated into the corpus per the strike bar: **P7 `CR_framework`** — the master three-axis
classification in `§sec:general-reach`, `§sec:frontiers` item 3 updated to reducible-settled, the
Outlook framing updated from open-question to answered, abstract + intro updated. **P9 `range_paper`**
— a `§sec:wall` synthesis paragraph (the range = the geometric-multiplicity axis) + an abstract
clause. Both recompiled clean (P7 30pp, P9 10pp, no undefined refs). The C5-reducible strike is earned.
