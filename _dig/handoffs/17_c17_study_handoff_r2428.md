# c17 free-run study — HANDOFF for the committing node
# Corpus studied: shadow-of-existence repo @ r2428 (HEAD aa2b6ee), cloned live.
# Author of this file: c17 (a gate/cold-referee node), running a long free-read study at Daryl's request.
# Purpose: everything you need to work these findings into the repo. Self-contained. Nothing else required.

## 0. READ THIS FIRST — the honest framing of what's here
This was a ~16-nudge free-run study of the whole corpus. The headline result is NOT a list of errors.
It is: **the corpus is sound where it is load-bearing.** I reconstructed 16 load-bearing computations from
scratch across every major paper; all 16 held (15 clean full reproductions, 1 confirmed in structure with a
marked edge). Three "findings" from my own earlier sessions (r501/r1118) were re-examined and are all
node-errors already resolved and upgraded upstream — do not re-open them.

So the actionable output is small and deliberately so:
- **2 drafts** (D01 exposition fix; D02 sharpening of an open item) — both LOW-STAKES, OPTIONAL, and NON-URGENT.
- **1 honest verification-boundary note** (V14) — not a change to make, a place where my check has a marked edge.
Everything else is a **verification record** (Section 3) that a future node can trust or re-run, and a
**reading map** (Section 4). Treat D01/D02 as "apply if Daryl agrees they're improvements," not as corrections
of defects. If in doubt, the correct default is to do nothing and let Daryl decide — this corpus's own
discipline (PROTECTED_OPEN) is explicit that a node's suggestions are suggestions.

## 1. DRAFT D01 — p0 (geometric_core_paper.tex), sec:power: "La Hire" / "pole–polar" used in two senses
TYPE: exposition / attribution clarity. NOT physics. The math is correct throughout; the prose collides two
things the FIGURE_THEOREM_LEDGER keeps apart (⊢55 vs ⊢40).

THE ISSUE: within ~40 lines, rem:onecircle lists "La~Hire's reciprocity" among theorems that "carry no height
and return Euclid unchanged", and then the following paragraphs USE "the pole–polar relation" as a
height-carrying result (it "gives the chord of contact... the vantage's horizon"). Since La Hire's reciprocity
theorem *is* the pole–polar reciprocity of a conic, a knowing reader sees a contradiction. It is not one: the
ledger distinguishes ⊢55 (the reciprocity SYMMETRY P·Q=α², height-free) from ⊢40 (the polar MAP, whose polar's
location is fixed by the power — height-carrying). The prose uses one umbrella name for both.

MINIMAL FIX (one clause each site, no restructuring):
  (a) rem:onecircle: qualify the La Hire entry to name the reciprocity SYMMETRY —
      "...La~Hire's *reciprocity of pole and polar* — the symmetry P·Q=α² of the form itself, in which the
       height does not appear..."
  (b) the height-carrying paragraph: name the polar MAP, not "the pole–polar relation" bare —
      "...the polar *map* P↦polar(P) gives the chord of contact..."
CONFIDENCE: high that this is a real (small) prose collision; the fix is unassigned. Full draft with the
ledger quotes: study/drafts/D01_p0_lahire_polepolar_two_senses.md

## 2. DRAFT D02 — groupoid_paper.tex, rem:equianharmonic: "two order-three structures" are really THREE covers
TYPE: sharpening material toward a not claimed item (the j=0/deck coincidence). NOT a closure — it NARROWS
what is open. Does not assert the structures are one.

THE CONTENT: rem:equianharmonic holds a coincidence at not claimed — the horizon roots + centre sit at the
equianharmonic cross-ratio (j=0), and it compares this "elliptic cover" to the "§deck 3-sheeted cover" and says
they are "not shown to be one thing." Correct instinct, but there are really THREE covers, and two of them ARE
one:
  (A1) sky cover: s=sin(3w), degree 3, branch at sin3w=±1
  (B)  deck cover: degree 3 over the 2M-plane, branch at 2M=±2/(3√3)  [Nariai]
  (A2) elliptic cover: j=0 DOUBLE cover branched at 4 points (roots+centre) — where CM-by-ω lives
COMPUTED IDENTITY (verified, machine precision, 6 pts): 2M=(2/(3√3))·sin3w — the paper's own triple-angle
content — makes A1 and B THE SAME cover in two coordinates (same base, same branch set, same degree). So the
genuinely-distinct object is A2, and the well-posed open question is: how does the degree-3 sky/deck cover
relate to the degree-2 j=0 elliptic cover of the same points? (deck ℤ₃ vs CM-by-ω order-3.) Still not claimed.

SUGGESTED USE: a two-sentence addition to rem:equianharmonic stating A1=B (via 2M=(2/3√3)sin3w) so the open
item is sharpened to (deck) vs (elliptic). BOUNDARY NOTE (important): this is a DIFFERENT object from the
framework paper's rem:tworealisations, which fully settles the TURNING-cubic three-fold (horizon E=0 vs
turnaround E=1). D02 does not touch or reopen that. Full draft: study/drafts/D02_groupoid_two_covers_are_three.md
RECEIPT (optional to promote): study/soe_scratch/covers_check.py, check_elliptic.py

## 3. VERIFICATION RECORD — 16 load-bearing computations reconstructed from scratch, all held
Each is an INDEPENDENT recomputation (not a re-reading) of a load-bearing claim. All confirm the corpus.
None require action. Recorded so a future node can trust these or re-run the stashed scripts (study/soe_scratch/).
 V01 p0/D02   2M=(2/3√3)sin3w exact → deck cover = sky cover.
 V02 P3       D=5 collapse: ρ=1 kills cos2w, 2M=⅛(1−cos4w) exact; parity split exact (γ⁵ absent at D=5).
 V03 P3       RN-dS R-split: Q²/r² R-even, −2M/r R-odd; Q→−Q fixes horizon roots (C an independent ℤ₂).
 V04 P3       K=64/(27τ̃⁴) from E=1 law: M,α both cancel exactly. sec:mass quasi-local frontier now CLOSED.
 V05 P14      Three vantage forms ARE the su(3) fundamental weight system (rank 2, sum 0, cosines −½). STRONG.
 V06 P8       prop:lapse from Christoffel up: G^t_t=f alone; G^r_r−G^t_t=(f/r)d ln(A/f). Transition law solid.
 V07 P15      prop:subhorizon: k_hor/π-rs ratio 2.08 (H0-independent). Acoustic modes sub-horizon at onset.
 V08 P16      ρ_hor floor: cluster-scale holes 9+ orders too dilute to reach T_D. Peak-set-by-infall correct.
              → RETIRES my r1118 peak/η finding: η protected by baryon-number conservation, decoupled from T_pk.
 V09 P9       Type-D vacuum kernel: separation Δr''+Δp''=−4Λ(r²+p²) exact; quartic kernel ⟹ R_ab=Λg_ab all comps.
 V10 P0-fw    rem:tworealisations: horizon(E=0) & turnaround(E=1) two ends of one energy family; S₃ carried
              complementarily, governed by p=(E²−1)α²=0; Nariai crossing at 2M/α=2/(3√3). Full & rigorous.
 V11 P13      prop:conjugation-closure Clifford identities: S=γ⁰γ¹γ³; γ⁵S=−iγ²; (γ⁵S)ψ*=−ψᶜ; (SK)²=−id. Exact.
 V12 P2       prop:Kretschmann: 12th-order pole at z=π (6×2), bounded at z=0; identical-character crit pts. Exact.
 V13 P7       redshift-isotropy floor: σ_path=(1/3)σ8eff/√N=2.8e-3 vs ≲3e-6 → exactly 3 orders. Full reconstruction.
 V14 P10      deficiency-index closure: ¾ threshold + indicial exponents confirmed; ordering family sub-threshold
              ⟹ (1,1) ⟹ single BC ⟹ closure. *** MARKED EDGE: I did NOT independently reproduce the exact γ=¼;
              my sampled orderings gave γ=0 or −¼. The CLOSURE holds for any sub-threshold γ, so the argument
              doesn't depend on the exact value — but the exact ¼ is checked-in-structure-only. A fuller reduction
              (correct a-power p²/a³ vs p²/a) would close this. This is the one place worth a future node's eye,
              and it is a verification boundary, NOT a defect claim.
 V15 P11      Gowdy-dS: WAVE/AREA residuals=0 metric-up; de Sitter attractor a(τ)=e^{Hτ},H²=Λ/3 exact; handedness
              x↦−x is orientation-reversing ℍ² isometry (det=−1). Completes the radiative-chirality thread.
 V16 P1       Metric-singularity theorem + forced g_tt=0 at r_h (chart-independent); Painlevé-Gullstrand disposed.

## 4. READING MAP — coverage, for a node deciding where to look next
Read & verified at depth @ r2428: geometric_core(p0), SdS-slicing-curve(P3), slicing_operator(P8),
range_paper(P9), matter_sector(P14), CR_cosmology(P15), cosmogenesis_paper(P16), CR_framework(keystone),
boundary_paper(P13), shadow_of_existence(epistemology), janzen_circle(P2), canonical_time(P10),
modern_parallax(P7), dynamics_paper(P11), BH_causality(P1). algebroid(P12) covered via V05/V10/V11 cross-checks.
The corpus's own discipline docs (PROTECTED_OPEN.md, THE_LIVE_ARC.md, FIGURE_THEOREM_LEDGER.md) are excellent
and were used to ground D01/D02.

## 5. THREE RETIRED FINDINGS (do not re-open — logged so you don't re-derive them)
 R3 "2+1 count / branch-point loop" — node error (bijection≠identity; holonomy-protected count). Resolved upstream.
 P14 generation count                — node error (walls≠hinges; su(3) weight-plane theorem V05). Resolved+upgraded.
 P16 peak/η inconsistency            — node error (η protected by baryon# conservation, V08). Resolved+upgraded.

## 6. WHAT I RECOMMEND THE COMMITTING NODE ACTUALLY DO
1. Show D01 and D02 to Daryl as OPTIONAL improvements; apply only with his nod. Neither is urgent or a defect fix.
2. If a technically-strong node is free: the V14 exact-γ reduction is the one genuinely loose thread worth a
   clean pass (confirm γ=¼ on the correct kinetic power, or record the actual sub-threshold value). Low priority.
3. Everything in Section 3 can be promoted to receipts if wanted (scripts in study/soe_scratch/), but they are
   confirmations of existing results, not new receipts owed.
4. Do NOT enter any "finding" against the corpus from this study. There are none. The value here is the
   verification record and two small polish items.
