> **⌖ RETIRED r1553.** This was a corpus-architecture flag on P9's formal cosmology development (r524). Resolved in the P9–P12 arc, all four papers compiling.
> Kept as record; **do not work from it.**


# CORPUS-ARCHITECTURE FLAG — P9's formal cosmology development → forward-pointer + conceptual exposition

**Status:** CORE CUT EXECUTED (r514). The separation is run in the `.tex`: **P12 opens with the
formal cosmological-theory development** (the Janzen2015 derivation described A→B, the proper-frame
sinh²ᐟ³, ΛCDM recovery, amplitude/Friedmann/Ω-ratio/clock), **the perturbation sections close it**;
**P9 sheds the theory-development layer**, keeps the geometric result + `thm:null-boundary` + the
banked Hubble remark, and gains a cranked-up conceptual reach + forward-pointer. Both compile (P12
10pp, P9 25pp; no undefined refs/cites; the only flag is the pre-existing missing `dS-SdS.png`).
**ENTANGLEMENT FINDING that refined the cut (r514):** the cross-ref web showed `eq:SdS-fundamental`
(proper-frame line element) and `eq:r-SdS-solution` (sinh²ᐟ³) are load-bearing for `thm:null-boundary`
(refs at P9 ll. 661/665) — so they **stay** in P9 as the geometric result; only the genuinely
overshadowing *theory-development layer* (exact-ΛCDM-recovery, §amplitude, isotropy) moved. P9's
abstract ("two main results") stays accurate — P9 still constructs the SdS cosmology (geometric
result); only the density/amplitude/tension *development* relocated. **Finishing-stage items (lighter
than feared):** optional polish of P9's synthesis to acknowledge the formal development now lives in
the arc; deeper Part A crank if wanted; the pre-existing `dS-SdS.png`. Stated for reversal.
Surfaced from the r510 P9 re-read; flag r511; roadmap r512; positioned r513; executed r514;
**synthesis fleshed r515.**

**REFINEMENT (r515) — the cut is NOT a partition; overlap is intended (Daryl).** The r514 execution
erred by writing P9's close as a *disclaimer of overlap* ("developed formally in the arc," "here we
have fixed only the geometric result") — forcing the green part of the Venn to be blue-elsewhere.
Corrected: P9's closing section (`\subsubsection{What this cosmology opens onto}`) now **describes
the physical theory as the framework's final application** — the expansion history + contents (the
Ω-ratio clock, amplitude/rate fixed by Λ, coincidence dissolved), the dissolved tensions, the
recovered cosmic time, the matter dynamics, the perturbation spectrum — each fleshed out, **with rich
forward pointers** (P10 `JanzenCanonicalTime`, P11 `JanzenDynamics`, P5/P6 `JanzenOperator`/`JanzenRange`,
P12 `JanzenScalar`, P7 `JanzenModernParallax`) and **deliberate overlap** with what those papers
develop formally. Content relevant in both contexts lives in both; each paper completes its own arc.
P9 26pp, 0 undefined. The banked resolution is described as resolved (Hubble dissolves, acoustic =
one-parameter η-analogue), pointed to §687–691, **not reopened**; the three Λ-scales held distinct.

---

## The insight (Daryl's, ARP'd at r511)

P9 (`CR_flatLCDM_v2.tex`) is a perfectly laid-out paper, and the dS→Nariai cosmology sits well
as a further application of the layered framework. **But that section overshadows the rest of
the paper.** P9's role is to **close the dynamical foundational trilogy**, whose crowning
achievement is to *explain clearly and in detail the theory that falls out of the core* — it is
not to carry the partial formal theory development itself. P9 only gets through **part** of the
physical theory that is eventually developed through **P10–P12**; **P10 and P11 do not even need
P9's formal cosmological development.** So as it stands, P9 overshadows the theoretical
foundational core by trying (and only partly succeeding) to reach too far into the full theory
all at once — the same over-reach the rest of the corpus is careful to avoid.

## The move (when executed)

**Recast P9's formal SdS-cosmology development into (a) a strong FORWARD POINTER + (b) a
gorgeous, fully decorated CONCEPTUAL exposition** — "the most gorgeously detailed and decorated
description of the theory that this CR-distinct application opens up through P10–P12." The
conceptual exposition is P9's *crowning achievement* — it should, conceptually and clearly
(without the overshadowing partial formalism):
1. explain the **Nariai reassignment move** and the **general conceptual shape** of the
   description (de Sitter null rulings reassigned timelike = the fundamental congruence; the
   at-rest closed-slicing geodesics reassigned null = the photon congruence; the foliation by
   expanding 3-spheres preserved);
2. explain how **the kink at r=0 dissolves** when the values are allowed to continue in their
   natural **imaginary direction** (the analytic continuation through the seam / onto the
   conjugate branch) — so the kink that *reads as* a curvature singularity is dissolved: the
   r=0 divergence is the perspectival (odd, mass) reading's chart artefact, the underlying
   de Sitter substrate smooth across it (P3 §`sec:sweep`/§`sec:lap`; P9 §483, §672);
3. **conceptually sketch the dynamics and the perturbation theory** — *with the one free
   parameter taken* (z_onset) — laying out **how all the tensions resolve** (the Hubble tension
   dissolves: no second H₀; the acoustic scale a one-parameter accommodation at the directly
   measured H₀; the coincidence problem a clock reading; the low-ℓ/early-time signatures the
   testable edge).

**Flag the FORMAL development of the cosmological theory for the next three-paper arc
(P10–P12).** That arc carries the full formal theory; P9 points forward to it. **The reach we
are executing now (P12, scalar perturbations) is part of that very arc** — the formal
perturbation development we are building IS part of what P9's forward-pointer will point to.

## The Janzen2015-description requirement (Daryl, explicit)

When the formal development is written (in the arc), it must do **better than an obscure
citation to a load-bearing derivation.** The derivation stays referenced —
**`resources/JanzenFQXi2012.tex`** (= Janzen2015, "A Critical Look at the Standard Cosmological
Picture," Springer 2015, §`sec_CSdSCS`), whose steps are in hand in the resources folder (read
at source r505: the proper-frame line element, the E=1 radial geodesics, ∂_χr=∂_τr, F(χ)=χ so
χ⊥τ, the flat constant-τ Lemaître slice, τ̃=τ+χ at 45°, 1+z=r(τ̃₀)/r(τ̃_e)). But it must be
**described** — explaining *how we get from A to B*, not simply dropping eq `SdS-fundamental` —
while being **careful not to plagiarize** Janzen2015. (NOTE: Janzen2015's algebra is
load-bearing; its pre-CR *interpretations* are not corpus-authoritative — REACH_PLAN §1g caveat.)

## Execution considerations (gate's notes, held lightly — the executor's call at execution time)

- **The load-bearing results need a home (coupling to this reach).** P9's formal section
  currently supplies results the reach and other papers cite: eq `SdS-fundamental`,
  eq `r-SdS-solution`, eq `nariai-amplitude`, the Nariai selection (eq `Nariai-mass`),
  `thm:null-boundary`, the banked acoustic remark (D_M, z_onset, ℓ_A≈301). The
  REACH_PLAN leans on these (§1d/§1e/§1f). When P9 is restructured, those results must remain
  **available and citable** — relocated into the P10–P12 arc (P12 included). **So the reach
  plan's P9 GO-TOs are coupled to this restructuring and will repoint to the arc when it
  executes.** Track the coupling; repoint the reach plan at execution time.
- **The boundary to decide at execution:** which pieces are P9's *foundational core* that stay
  (candidates: the reassignment, `thm:null-boundary`, the Nariai selection — these *found* the
  cosmology) vs. the *formal theory development* that overshadows and relocates (candidates: the
  amplitude/Ω-ratio/Friedmann working §`sec:amplitude`, the full acoustic/Hubble-tension remark
  development). Do NOT pre-decide here; decide it with the arc in view.

## Timing — why flagged, not executed now

1. The forward-pointer's conceptual content (the dynamics + perturbation sketch) **depends on
   P10–P12 being mature** — which is the work ahead. The reach (P12) is the live part of it.
   Writing the forward-pointer well requires the arc it points to.
2. Executing a P9 rewrite *now* would itself be reaching too far, too soon — the exact
   over-reach this flag diagnoses in P9. The disciplined move is to flag and track, and execute
   when the arc is mature.

**Tracked from:** CORPUS_MAP r511; REACH_PLAN (standing-flag pointer); THE_PLAN (route item).

---

## STANDING DISCIPLINE (Daryl, r518) — every grind ends at the P9 close

The P9 close (`\subsubsection{What this cosmology opens onto}`) is the **living synthesis** —
the framework's final application, the setting into which the programme's results are mounted.
It is not written once. **Every grind ends by returning to the P9 close and asking what it can
now say that it could not before** — checking the close for opportunities to enrich it with the
newly fleshed-out jewels the grind produced. The receipt is not the end of a grind; the close is.

**The gate (where this discipline earns its keep):** enrich only with the SOUND jewels, and never
past the do-not-assert boundary or ahead of the source paper's own text.
- A result HELD do-not-assert (an unverified C_ℓ shape, a look-signal) is not yet a jewel to set —
  it is queued until verified at source AND cold-read.
- The enrichment must stay consistent with the source paper (P10–12): match its specificity, do
  not exceed it. Slipping a half-sound refinement into the close ahead of P12's text manufactures
  an internal inconsistency.
- Worked example (r518→r524, the low-ℓ reach, now resolved): the r518 close set a jewel that read the
  floor through the *hyperspherical* transfer (degree-L feeds ℓ≤L, lowest mode reaches the lowest
  multipoles, the non-synchronous transfer the open piece). The reach then OVERTURNED that object: CR's
  distance slicing is flat (prop:flat), so the discrete closed-S³ source projects through the FLAT
  j_ℓ(k_L D_C), placing the lowest mode near ℓ≈8 — a low-multipole DEFICIT, not a quadrupole-reaching
  floor. The transfer was built and validated (r522–r523: flat-limit-verified, the ISW make-or-break
  passed, measure = the dk/k discrete image), so at r524 the now-SOUND jewel was SET into the P9 close
  AND developed in P12 (P9 synthesis-level, P12 the transfer), the do-not-assert hold lifted by
  verification and the wrong hyperspherical clause removed from both. **The lesson for the gate:
  do-not-assert is a SOUNDNESS FILTER, not a halt — once verified at source, the jewel is SET (matching
  the source paper), not withheld. Withholding a verified result is itself a failure of the discipline.**

Tracked also in REACH_PLAN §7 (the grind discipline).
