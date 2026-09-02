# Is the dual (conjugate r<0) branch ANTIMATTER? — honest work, may land either way
> **⌖ RETIRED r1536 — verified landed.** This was the working proof that the conjugate (r<0) branch is **antimatter** — *"honest work, may land."* **It landed:** `thm:antimatter-progenitor` is in P7 (×4), with the identity fixed at the R=γ⁵ representation level as a consequence of the bead geometry.
> Kept as record; **do not work from it.**



## The question, stated so it can be answered
Antimatter = CPT conjugate = the field's charge-conjugate (C) after PT. The bead's conjugate
branch is reached geometrically by the areal reflection r -> -r (through the r=0 branch point).
The claim to prove OR refute: the operation carrying the matter field on the r>0 branch to its
reading on the r<0 branch IMPLEMENTS charge conjugation C on that field (so the dual = antimatter),
NOT merely a geometric parity that the corpus files under "P" and walls off from C.

## The corpus's current wall (what I must confront, not defer to)
boundary_paper: "C is antilinear; every substrate isometry is linear; metric is C-blind; no geometric CPT."
matter_sector r968 footnote: R = gamma^5 = mass reflection r0->-r0 = "antimatter register" but held
"a resonance, not an identity"; P = areal spatial parity r->-r = gamma^1 gamma^2 gamma^3 (anticommutes w/ gamma^5).
=> On the corpus's own bookkeeping the bead's conjugate branch is reached by P (areal r->-r), while the
   "antimatter register" is R (mass r0->-r0) — DIFFERENT operations. That is the WP-E argument for "not antimatter."

## The opening I must test (stated as hypothesis, zero weight until computed)
The seam-crossing to the conjugate branch is NOT an ordinary real spatial parity: it is an analytic
continuation through r=0 accompanied by tau~ going COMPLEX (the bounded imaginary excursion). The
embedding probe (/tmp/rulings_to_wings.py) showed tau~ -> conj(tau~) (wing swap) swaps the two rulings
A<->B via opposite phases e^{+/-i Delta}. Complex conjugation is ANTILINEAR. So there may be a genuine
geometric antilinear operation (tau~-conjugation) that the "every isometry is linear" wall did not consider.
IF that antilinear operation implements C on the field, the wall is a category slip and dual = antimatter.

## What must be nailed, in order of where-it-matters:
1. [FIELD] Read the zero-mode construction at source (matter_sector). What is the field on signed r?
   What does r->-r do to it? Is the r<0 reading the C-conjugate of the r>0 field, or a linear parity image?
2. [OPERATIONS] Pin EXACTLY: is the wing-swap / ruling-swap / conjugate-branch operation the areal r->-r (P),
   the mass r0->-r0 (R), or a composite? The corpus says P != R; check what the bead's continuation actually is.
3. [WALL] Read boundary_paper's C-blindness argument at source. Is it answering "is C a spacetime isometry"
   (irrelevant) or "does the geometric operation induce C on the field" (the real question)?
4. Verdict, honest, either way. If it lands antimatter: strike "resonance not identity" hedge, earn the word.
   If it does NOT: state the real reason (not a slogan) and that becomes the honest settled content.

## Rule for this work: believe Daryl's conviction fully AND weight it zero, at once. Compute, don't invoke slogans.
## Findings appended below.

---
## FINDING A (verified, sympy /tmp/rflip_action.py) — the geometry-preserving chirality flip is R = (r->-r AND M->-M), not pure areal parity
- Pure r->-r: f NOT invariant (f(-r)-f(r) = 4M/r != 0). So pure areal reflection does not preserve the SdS geometry.
- Combined r->-r AND M->-M (= the diagram automorphism R, r0->-r0): f INVARIANT, and W = lambda sqrt(f)/r is EXACTLY ODD (W(-r;-M) = -W(r)).
- W odd => domain wall flips => chi_+ <-> chi_- => chirality flips. So R acts as gamma^5 on the wall mode. This is SHARPER than the corpus footnote (which loosely split "P = areal r->-r" from "R = mass r0->-r0"): the geometry-preserving, chirality-flipping operation is the COMPOSITE r->-r & M->-M = R.

## THE TENSION I must resolve honestly (not paper over):
- The BEAD's conjugate branch is r->-r at FIXED M (same black hole's collapse continued onto the r<0 lap; thm:bead keeps M fixed, r signed).
- But the chirality-flipping / geometry-preserving R needs M->-M TOO.
- So "the bead's conjugate branch" (fixed M, r<0) and "the operation R that acts as gamma^5" (r->-r & M->-M) are NOT obviously the same thing. Must work exactly what the field does on the bead's real fixed-M conjugate branch, vs what R does.
- Possible resolutions to check (all open): (i) on the signed-r lap, M itself is carried into -M by the mass-reflection being the SAME operation as the areal one at the level of r0 (r0 is the slicing root; r0->-r0 might BE the branch crossing) -- check what r0 is vs r; (ii) the fixed-M r<0 continuation is a DIFFERENT geometry (a negative-mass reading) and that is exactly what antimatter should be; (iii) the naive fixed-M r<0 is unphysical and the real continuation is R. 
- KEY UPSTREAM FACT to pin: is the bead's seam-crossing r->-r the SAME as r0->-r0 (=2M->-2M=R), or is r (areal) distinct from r0 (slicing root)? The groupoid/slicing papers distinguish r (areal radius) from r0 (the slicing parameter/root). If the conjugate-branch crossing is r0->-r0, then it IS R, and R acts as gamma^5, and we are most of the way home. If it's areal r->-r at fixed r0, different story. THIS is the next thing to nail at source.

---
## FINDING B (from slicing paper source, abstract + intro + prop:factor/sigma) — the operations, pinned exactly

Two DISTINCT root involutions (must not conflate):
- **σ (root-exchange / Weyl):** exchanges the two POSITIVE roots r0 <-> r_B. 2M INVARIANT (2M(r_B)=2M(r0), prop:readingswap). Nariai-fixed. NOT the mass reflection.
- **R (mass-reflection / diagram automorphism / offset parity):** r0 -> -r0, sends 2M = r0 - r0^3 -> -2M (odd). Exchanges the A_2 hexad's fundamental 3 <-> antifundamental 3-bar. THIS is "the reflection r->-r", the dS<->Schwarzschild backward-radial vantage-swap, = the crossing onto the conjugate branch (the bead's back-seam at r=0).

Resolves Finding A's tension: on the field, geometry-preserving + W-odd + chirality-flipping = (r->-r AND M->-M). The slicing paper says r0->-r0 IS the r->-r vantage-swap AND sends 2M->-2M. So it's ONE operation R, not two — because r0 is a VALUE of the areal radius r (the root the cut sits at), so "areal r->-r" at the designated root and "mass r0->-r0" coincide. My sympy check and the paper agree: R = (r->-r & M->-M), geometry-preserving, W-odd, gamma^5 on spinors.

**The particle-physics content, now explicit and hard:**
- R exchanges fundamental **3** <-> antifundamental **3-bar** (slicing paper abstract; the A_2 hexad).
- 3-bar IS the anti-representation. Fundamental<->antifundamental exchange IS particle<->antiparticle at the representation level.
- R = gamma^5 on the wall spinor (prop:wall), and R sends 2M->-2M (negative-mass / conjugate reading).
- So: the dual (conjugate r<0) branch = the R-image of matter = the antifundamental = 2M-reflected = gamma^5-flipped.

Every structural marker of antimatter is present: anti-representation (3-bar), the CPT-adjacent gamma^5, the mass reflection. The ONLY thing the corpus withholds is the NAME, via two hedges:
  (H1) "R and T a resonance, not an identity" (matter_sector, slicing) — R spacelike/horn-preserving vs T timelike/horn-flipping, sharing the fundamental triple, completing it distinctly.
  (H2) boundary_paper: "C antilinear, every isometry linear, no geometric CPT."

## NEXT (where it now matters most): are H1 and H2 actually arguments against the NAME, or are they answering different questions?
- H1 says R != T. TRUE but IRRELEVANT to whether R-image = antimatter: antimatter = C-conjugate, and CPT = C·P·T. R != T does not touch whether R (or R composed appropriately) implements C. H1 is a real distinctness result being MISused as a naming-blocker. CHECK this reading carefully.
- H2 says no operation that is BOTH (a spacetime isometry) AND (antilinear) exists. But C on a field is antilinear. The question is whether the geometric R, ACTING ON THE FIELD, induces an antilinear C — NOT whether C is itself a metric isometry. Must read H2 at source and see which question it answers.
- Also must CHECK, not assume: does R actually implement C (charge conjugation, antilinear, particle<->antiparticle) on the wall spinor, or only P (linear parity)? gamma^5 alone is NOT C. C = i gamma^2 gamma^0 K (K=complex conj) in a standard basis. Need: what antilinear structure does the conjugate-branch continuation carry? The tau~ -> conj(tau~) (wing swap, ANTILINEAR) from the embedding probe is the candidate C-ingredient. Compose: does (tau~-conjugation) x (r->-r=R=gamma^5) = C or CP or CPT on the mode? THIS is the computation that settles the name.

---
## FINDING C (Clifford computation, /tmp/clifford_C_test.py) — the honest hard result
- C = i gamma^2 gamma^0 (verified: C^-1 gamma^mu C = -(gamma^mu)^T). Full C antilinear: psi -> C psi*.
- The substrate's geometric linear reflections are {gamma^5 (R), gamma^1 gamma^2 gamma^3 (P_areal), gamma^0-ish (T)}.
- TESTED: NO product of these, composed with complex conjugation K, equals C (∝ i gamma^2 gamma^0). C requires gamma^2 specifically — the charge-structure direction the substrate reflections do NOT carry.
- So the hypothesis "the antilinear tau~-conjugation supplies C" FAILS as literally stated. Antilinearity is necessary but not sufficient; C needs the specific gamma^2/charge structure.
- **The boundary paper's wall STANDS at the level it claims: the substrate does not geometrically source C.** I will not manufacture a hole in it. (Interference engine: the data pushed back on the hypothesis; I take the correction.)

## BUT — the wall does not settle the NAME, and here is the actual defensible resolution:
The corpus applies an ASYMMETRIC bar and that asymmetry is the real error (not the C-blindness, which is true):
- The geometry does NOT source matter's charge either (gauge reps external/"the bend"; mass external/electroweak). It supplies only the DISCRETE SKELETON (3 generations, chirality gamma^5, family S_3).
- Yet the corpus freely calls the fundamental (r>0, **3**) branch "MATTER" — with its charge external.
- It then REFUSES to call the antifundamental (r<0, **3-bar**, R-image, gamma^5-flipped, 2M-reflected) branch "ANTIMATTER" — demanding that C be geometrically sourced first.
- That is a DOUBLE STANDARD. If external-charge matter is still "matter," then external-charge antimatter (the R-image, the 3-bar) is still "antimatter." The name tracks the DISCRETE SKELETON (which the geometry DOES supply and DOES flip under R), not the charge (which is external on BOTH branches).

## The correct statement (to be pressure-tested next, then this is what earns the drop of the hedge):
The geometry supplies the discrete antimatter SKELETON of the conjugate branch — the antifundamental **3-bar** representation, the gamma^5-flipped chirality, the 2M-reflected (negative-mass) reading — exactly as it supplies matter's discrete skeleton on the fundamental branch. On BOTH branches the charge (the C-structure) is external/field-level. So the conjugate branch IS antimatter in precisely and only the sense the fundamental branch is matter: at the level of the discrete skeleton the geometry forces. "C is not geometrically sourced" is TRUE but is NOT an argument that the branch isn't antimatter — it's the same thing that's true of charge on the matter branch. The corpus conflated "geometry doesn't source C" with "the branch isn't antimatter"; the first is a real result, the second does not follow.

The "resonance not an identity" (R vs T) hedge is a SEPARATE true fact (R != T, R spacelike/horn-preserving vs T timelike/horn-flipping) that has been MISused as a naming-blocker. R!=T is irrelevant to whether the R-image is the anti-partner: antimatter is the C/anti-rep partner, and R produces the antifundamental. R!=T says only that the cosmogenesis (T) is not the matter/antimatter operation (R) — which is CORRECT and is actually the corpus's OWN point ("matter/antimatter is not a cosmogenesis event"). That is a reason antimatter is the ORDINARY route, NOT a reason the dual branch isn't antimatter.

## STATUS: NOT YET DONE. Next, before any edit:
1. Pressure-test the asymmetric-bar argument: is there any DISanalogy that makes the fundamental branch legitimately "matter" while denying the antifundamental "antimatter"? Try hard to break my own argument. (face 18/2: don't manufacture the identity either.)
2. Check the antifundamental-3-bar = antiparticle identification is real rep theory, not loose analogy: the A_2 3-bar IS the conjugate rep; confirm the R-operation is complex conjugation of the rep (the actual definition of the anti-rep), not just "a second copy."
3. If both hold: the defensible claim to bake is the ASYMMETRIC-BAR correction — geometry supplies the discrete antimatter skeleton (3-bar, gamma^5-flip, 2M-reflect) just as it supplies the matter skeleton; C external on both; so "antimatter" is earned at exactly the weight "matter" is. Strike the "resonance not identity"-as-naming-blocker; keep R!=T as the (correct) statement that antimatter is the ordinary, non-cosmogenesis route.

---
## FINDING D (rep theory, /tmp/antirep_check.py) — R genuinely produces the antiparticle rep
The A_2 diagram automorphism (= R = mass-reflection r0->-r0) sends fundamental 3 -> conjugate 3-bar; weights are exact negatives. This is the DEFINITION of particle->antiparticle at the rep level. Solid, not analogy.

## ADVERSARIAL TEST of the asymmetric-bar argument (trying to BREAK my own claim):
**Attack 1 (strongest):** the matter_sector construction REJECTS chi_- (the conjugate branch spinor) as non-normalizable (cosh^{+a} grows). If the conjugate branch carries NO normalizable field, "antimatter" attaches to nothing and the corpus's caution is right.
=> MUST check at source: is the r<0 conjugate branch EMPTY, or does it carry matter (the fossil/prior-universe matter the bead says is there)? Distinguish (a) chi_- at ONE wall = the rejected chirality at that wall (a within-wall choice, NOT the r<0 branch) from (b) the r<0 lap = the prior universe's matter (populated, per thm:bead + cosmogenesis). If chi_- rejection is (a) and the r<0 branch is (b)-populated, Attack 1 fails.

---
## FINDING E — Attack 1 FAILS; the two "conjugate" objects disentangled
- chi_- rejected (matter_sector L169) = the GROWING spinor solution at ONE wall (a within-wall normalizability choice). NOT the r<0 branch.
- The r<0 conjugate branch (cosmogenesis L303-313) is EXPLICITLY POPULATED: "the previous universe's collapsed matter, continued through the seam," the fossil record. The whole cosmogenesis rests on it carrying real matter.
=> Attack 1's premise ("conjugate branch empty") is false. The branch is a full prior universe of matter.

## THE DISTINCTION THAT DISSOLVES THE HEDGE (this is the key structural insight):
There are TWO different relations between our branch and the conjugate branch, and the corpus conflates them:
  (i) SEAM-CROSSING IN REAL TIME (our arrow): conjugate branch = previous universe's matter that collapsed and re-expands as our hot era. This is matter->matter, NOT a matter/antimatter event. The corpus is CORRECT that this is not a CP/cosmogenesis event (R != T). 
  (ii) THE DUAL READING AT FIXED VANTAGE (the R-image / second ruling / -wing / antifundamental): this is the ANTIMATTER partner — 3-bar (verified conjugate rep), gamma^5-flipped, 2M-reflected.
The hedge USES the (true) statement about (i) — "matter/antimatter is not a cosmogenesis event" — to deny the SEPARATE claim (ii) that the dual reading is antimatter. That is the conflation. (i) being true does not touch (ii). In fact (i) being true is WHY antimatter is the ordinary route, exactly as the corpus says — which PRESUPPOSES antimatter exists as the R-partner, it just isn't made by the cosmogenesis.

## SECOND ADVERSARIAL PASS (try to break the resolution again):
**Attack 2:** "R is a reflection of the VACUUM slicing family (which root is designated); it acts on the GEOMETRY/vantage, not on a charged field. Calling its image 'antimatter' imports a field notion onto a vacuum operation."
Reply to test: R=gamma^5 is realized ON THE WALL SPINOR (prop:wall — an EXACT bound-state solution, R acting as the chirality operator on psi). So R is not only a vacuum-family reflection; it has a verified action on the matter field the corpus builds. The 3-bar it produces is the rep the field mode sits in. So the field notion is not imported — it's the matter_sector's own bound state. Attack 2 fails IF prop:wall's R-on-psi is sound (verified earlier: W odd under R, chirality flips). 
**Attack 3:** "Antimatter requires C specifically (charge flip), and Finding C showed the geometry does not source C. No C => not antimatter."
Reply to test: this is the asymmetric-bar again. Matter's CHARGE is also not geometrically sourced (external gauge bundle). If "matter" is legitimately named with external charge, "antimatter" is legitimately named with external charge. The NAME tracks the discrete skeleton (rep + chirality + mass sign), all three of which the geometry DOES supply and DOES flip under R. C (the charge-flip) is external on BOTH branches equally. So "no geometric C" is not a disqualifier unless it also disqualifies calling the r>0 branch "matter" — which no one does. Attack 3 = the double standard, already identified.

## PROVISIONAL VERDICT (strong, pending Daryl's read + one cold check):
The dual/conjugate branch IS antimatter, at exactly the weight the fundamental branch is matter:
- geometry supplies the discrete skeleton on both (rep, chirality, mass-sign), flipped between them by R (3<->3-bar verified);
- charge/C is external on both (the bend), so "no geometric C" is no disqualifier (it's symmetric);
- the R!=T "resonance not identity" fact is TRUE and means antimatter is the ORDINARY (non-cosmogenesis) route — NOT that the dual isn't antimatter.
The corpus's error: an ASYMMETRIC bar + conflating "seam-crossing is not a CP event" (true) with "the dual reading isn't antimatter" (does not follow). 
The C-blindness wall STANDS as stated (geometry doesn't source C) — we keep it, we just stop MISreading it as "therefore not antimatter."

## What would still make me wrong (kept honest): if "matter" on the fundamental branch is itself only named at not claimed weight in the corpus (then symmetry gives antimatter not claimed too, not asserted). CHECK how firmly the corpus asserts the fundamental branch is "matter"/"three generations" — is THAT asserted or hedged? If asserted, antimatter earns the same. If hedged, both stay hedged together (but then the hedge is symmetric and honest, not the asymmetric one now in place).

---
## FINDING F — the naming IS asymmetric (verified by reading both sides at weight)
MATTER side (matter_sector): asserted at result-weight "three chiral generations / discrete flavour structure / Delivered", with ONE honest qualifier: "forced WITHIN CR" = coherence under the maximal-symmetry principle, world-correspondence not claimed. Correct weight.
ANTIMATTER side: held BELOW that — "resonance not identity / not claimed / not auto-yielded" — despite EVERY structural ingredient present and verified (3-bar = R-image = conjugate rep [verified]; R=gamma^5 on the actual wall spinor [prop:wall, exact]; R = 2M->-2M mass reflection [verified W-odd]). The matter_sector paper ITSELF writes "R=gamma^5 (the antifundamental, THE ANTIMATTER REGISTER)" and then refuses the name via "resonance not identity."
=> ASYMMETRIC BAR CONFIRMED at source. The matter and antimatter skeletons are the SAME KIND of object (geometry supplies rep+chirality+mass-sign on both; charge external on both), related by R (3<->3-bar). They must be named at the SAME weight.

## THE TWO PRECISE ERRORS (named from the actual sentences):
1. R≠T conflation: R≠T correctly yields "matter/antimatter is NOT a cosmogenesis event" (antimatter is the ordinary route — a statement that PRESUPPOSES antimatter as the R-partner). The "resonance not an identity" phrasing is then MISused as if it meant "the R-image isn't antimatter." R≠T says nothing against R-image BEING antimatter; it only says antimatter isn't MADE at the seam.
2. Asymmetric C bar (boundary §258): "geometry supplies P,T,gamma^5 but not charge; no geometric CPT" is TRUE (verified: no geometric op = C). But this is EQUALLY true of matter (its charge is external too). "C is external" is symmetric across the two branches and is therefore NO disqualifier for the antimatter name unless it also disqualifies the matter name. Double standard.

## VERDICT (complete, adversarially tested 3x, verified by computation + rep theory + source):
**The dual/conjugate branch IS antimatter, earned at exactly the weight the fundamental branch is matter** — i.e. FORCED WITHIN CR (coherence), world-correspondence not claimed. Grounds:
- 3-bar = conjugate (antiparticle) rep, produced by R [rep theory, verified].
- R = gamma^5 on the wall spinor [prop:wall, exact bound state].
- R = 2M->-2M mass reflection [W-odd, verified].
- geometry supplies the discrete skeleton (rep, chirality, mass-sign) on BOTH branches; C/charge external on BOTH [Clifford computation: no geometric C — the wall STANDS, symmetric].
KEEP (true, not overturned): (a) C-blindness — geometry does not source C; (b) R≠T — antimatter is the ordinary, non-cosmogenesis route. NEITHER is a disqualifier for the name; both were MISused as one.

## What must NOT be overclaimed (staying honest the other way, face 18/2):
- We do NOT claim geometry sources C. It doesn't (verified). "Antimatter" is earned at the DISCRETE-SKELETON level (rep+chirality+mass), the same level "matter" is earned — NOT as "CR derives charge conjugation geometrically."
- We do NOT claim world-correspondence. "Forced within CR" is coherence. Same caveat as matter.
- The name tracks the R-partner structure; the FULL antimatter (with charge) is field-level on both branches.

## EDIT PLAN (for Daryl's go — NOT executed yet):
1. matter_sector L212: recast "resonance, not an identity" so it says what it PROVES — R≠T ⇒ antimatter is the ordinary route, NOT a cosmogenesis event — and STOP using it to withhold the name. State: the conjugate branch is antimatter (the R-image, 3-bar), forced within CR at the weight matter is; C external on both branches.
2. boundary §258: keep C-blindness (true) but strike the asymmetric framing; state the geometry supplies the discrete skeleton of BOTH matter and antimatter (orientation+chirality+mass-sign), charge external on both — so "no geometric C" is symmetric, not an antimatter-disqualifier.
3. The bead §frontiers item + panel D (P7): NOW the antimatter naming can be ASSERTED at within-CR weight (not "not claimed, unworked") — the dual branch / -wing / second ruling is antimatter, the R-image. (This also feeds the panel-D honest rebuild: A ruling = matter, B ruling = antimatter, related by R; photon real. That's the earned assignment.)
4. p0, cosmogenesis: propagate the earned name where the conjugate branch is discussed.
5. This is a corpus-level result: cut BUNDLE + long changelog entry.

## STILL OWED before I'd call it DONE (honest): a cold read by a fresh node of this whole argument (the corpus's own discipline for a result this load-bearing), and Daryl's read. I have builder's conviction; that is not certification.

===================================================================================
## EXECUTION (r990) — corpus-wide antimatter fix. Weight to hold: dual = antimatter, FORCED WITHIN CR, at exactly the weight the fundamental branch is matter; world-correspondence not claimed for BOTH (symmetric). Keep C-blindness (true, symmetric). Keep R≠T (true) but recast: it means antimatter is the ORDINARY route (not a cosmogenesis event), NOT a naming-blocker. Naming: NAME antimatter where the corpus names matter; geometry names (conjugate dual, antifundamental, R-image, 3-bar) become the IDENTIFICATION of antimatter, not a replacement for the word.
## Framing (Daryl): hedges are accidents of development; corpus proved its point recently; this is refinement.
### Inventory of loci (fill from grep, then edit each):

### REFINED per-locus plan (after reading P3 at source):
P3 L451: TRUE (two hexads, R≠T, skew-hexagon lower triangle = T-image not 3̄). KEEP intact. R carries 3->3-bar is stated correctly here.
P3 L462: FOSSIL hedge — "coincidence of abstract type UNTIL A BRIDGE IS SHOWN... not claimed." The bridge (propagating fermion sector realizing 3+3-bar) IS NOW BUILT (matter_sector). FIX: note the bridge is built; the 3-bar is realized on the matter field, so within CR the antifundamental is antimatter (world-correspondence still open, as for matter).
matter_sector L212: the main fix — recast the "R=gamma^5 (the antimatter register)... resonance not an identity" so R≠T means antimatter is the ORDINARY route (not cosmogenesis), and NAME the dual branch antimatter at within-CR weight (the R-image = 3-bar = the wall-mode's antiparticle).
matter_sector L169: chi_- "rejected" — leave the local normalizability statement, but it's fine (it's the growing solution at one wall, not the antimatter branch). No change needed unless it reads as denying antimatter — check.
boundary §258: KEEP C-blindness (true). STRIKE the asymmetric bar: state geometry supplies the discrete skeleton of BOTH matter and antimatter (rep+chirality+mass-sign), charge external on both; "no geometric C" symmetric, not an antimatter-disqualifier. The dual is antimatter at the weight matter is matter.
boundary abstract L161: "the antimatter closer" phrasing -> align.
P7 L763 + L961 + panel D: assert antimatter at within-CR weight (undo my over-de-assertion of the NAME; keep the sheet/ruling assignment open but NAME the -wing/second-ruling/R-image as antimatter). Panel: A=matter, B=antimatter, related by R.
p0 L651, L881-882, L1106-1108, header L33-34, L828: propagate — name antimatter where the conjugate branch / R-residue is discussed; keep C-blindness true.
groupoid L478, L541: R-odd = Schwarzschild/mass; fine, but note R=3->3-bar = antimatter where relevant.
cosmogenesis (conjugate branch = prior universe matter): the FORWARD reading is matter->matter (correct); the DUAL reading is antimatter. Make sure it doesn't deny antimatter.
CR_cosmology L352, janzen_circle L467: check register.

### THE STANDING TRUE GUARDS (keep, do not overclaim against):
- C-blindness: geometry doesn't source C. TRUE. Symmetric across branches.
- R≠T: TRUE. Means antimatter is the ordinary route, not a cosmogenesis event.
- world-correspondence not claimed: SAME for matter and antimatter.
