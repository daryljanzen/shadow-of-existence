> **⌗ RETIRED r2380 under `RG-1` — the LOG of a phase, whose DRIVER stays live.**
> *"Revisions cut during the storyboard-driven figure-work phase," r1036 onward.* **The distinction that
> settles it:** *`SYNTHESIS_FIGURE_STORYBOARD.md` is the **standing working document** that drives the phase and
> is indexed live and deliberately undated (it is a forward document); **this file is the record of what was cut
> while it drove**. A log is a record by construction — it is dated entries of completed revisions, and a node
> plans from the driver, never from the log.*
>
> ⌗ *Its own head names the backup it rests on — `corpus/_figure_backup_pre_storyboard/` — so the pre-storyboard
> figure is recoverable independently of this file, which is what makes retiring it costless.*

---

# Figure-work log — fig:dS_SdS (driven by SYNTHESIS_FIGURE_STORYBOARD.md)

Revisions cut during the storyboard-driven figure-work phase. Backup of the pre-storyboard
figure (code + pdf + png): `corpus/_figure_backup_pre_storyboard/`.

## r1036 — phase opened
- Storyboard formalized as a standing working doc; THE_PLAN item 4 marked REOPENED & DEEPENED.
- Figure backed up; edit→render pipeline validated.
- synthesis_figure.py: docstring now points to the driving storyboard; "throat circle" → "equator".
- No panel geometry changed yet. Next: E1 (both-bundle A) — pending a design decision (below).

## OPEN design forks (must be settled before drawing, not guessed)
- **E1 (both-bundle A):** where does the partner bead's r=0 sit, and which arc goes purple?
  The vertical-axis reflection fixes the top point → shared r=0, which contradicts the
  storyboard's "flip at different r=0 points." So the partner-generating map is not the naive
  reflection. Need: the correct projected image (into the X0=0 equatorial plane) of the
  charge-conjugation / end-over-end map that carries our bead to the partner.

## r1037 — E1 done (both-bundle panel A)
- Panel A rebuilt to Daryl's three-thirds spec: equator = top-right BLUE (both beads blue),
  top-left RED (both red), bottom/hinge third PURPLE (blue ccw + red cw cross there).
  Four straight rulings crossing at the hinge (0,-2): bead1 blue-in right (hinge->T) / red-out
  right; bead2 red-in left (hinge->T') / blue-out left. Verified numerically (arcs, rulings,
  collinearity of blue-in & red-out through T). Renders clean.
- Design fork from r1036 RESOLVED by Daryl directly: the two beads are colour-identical on the
  top two thirds and cross only on the bottom/hinge third; rulings cross at the hinge.
- Next: E2 (carry the same both-bundle logic to panel E, the boing).

## r1038 — panel A fixed
- Removed leftover pre-compaction partner-bundle code that was overpainting the arcs (a full blue
  circle + red bottom arc). Panel A is now the simplest form: three arcs (top-right BLUE,
  top-left RED, bottom PURPLE) + four rulings crossing at the hinge. Seam labels moved to the
  tangent points T, T' (the horn->equator turning points), not the ruling far-ends.

## r1039 — receipts bundled; E plan corrected
- Storyboard receipts (the .py verification scripts) collected into corpus/../storyboard_receipts/
  with a README, so they travel with the programme (they were left out of r1037/r1038).
- E re-planned per Daryl: E is bundle-COLLAPSED (X1 single-valued in r -> both bundles trace the
  same boing, colours swapped). E2 DROPPED (no distinct second curve). E stays single, and that
  single-ness exhibits the r-face's bundle-indifference (what C's tau~-face distinguishes).
- E6 PREMISE BROKEN: E does not subsume C (C shows the conjugate crossing E can't). Do not retire
  C on E's account. G's slot reopened (candidates: an embedding panel A/B/D, or 7 panels, or G
  replaces F). To decide deliberately.

## r1040 — F REBUILT: the cosmological bundle, unfurled (the big one)
- Panel F replaced. Old F (r vs complex tau~, one-blue-two-red, hand-drawn black photon) is gone.
  New F = the ONE privileged worldline strung out: antimatter black hole (RED, r<0) collapsing
  through r=0 into our matter universe (BLUE, r>0), in (Re tau~, Im tau~, r). The LAP IS UNFURLED
  (the vertical lift at Re tau~=0), not flattened to one X0. Branch: arg r=+pi (negative-imaginary).
- Structural finding (Daryl's call, confirmed): the collapse side and the cosmology side are
  DIFFERENT CURVES -- collapse = horizontal run at Im tau~=-pi/3 THEN vertical lift at Re tau~=0;
  cosmology = a single simple real curve. Not mirrors.
- NEW EXACT RESULT: the Nariai seam points (E's boing roots) land at |sinh|=2 (r=-2a/sqrt3) and
  |sinh|=1/sqrt2 (r=+a/sqrt3), whose Re tau~ are -(2/3)arccosh(2) and +(2/3)arcsinh(1/sqrt2) --
  in EXACTLY 2:1, since arccosh(2) = 2 arcsinh(1/sqrt2) identically. The 120/240 gearing appears
  as a LENGTH RATIO along the unfurled time axis. Receipt: storyboard_receipts/cosmo_bundle.py.
- Panel G is retired as a concept: the unfurl G was reaching for IS this F. Plate stays six.
  E6 (G's slot) dissolved; C is kept (E is bundle-collapsed and cannot subsume it).
- Storyboard fully updated: F rewritten, G section removed, E5 done, E6 resolved, C-rhyme added
  (the matter-sector pair-vertex reading, held as a RHYME at Daryl's stated weight -- shared
  geometric infrastructure, candidate central figure for the matter papers, NOT a claim about
  colliding universes), U-bundlemap opened (which bundle is which branch -- unworked).

## r1041 — drafting opened (section 10), and a real catch in panel C
- Storyboard section 10 opened: the SEAM-FLAG drafting protocol. All revisions drafted in the
  storyboard against flags (% <<SB:id>> LaTeX comments at the revision sites), each written as a
  readable seam (KEEP / NEW / CUT) so the splice can be read straight through and checked for
  sentence coherence. One wholesale surgical pass applies them at the end. Nothing in the corpus yet.
- Drafted: P7 caption colour-preamble (purple declared), caption (A) (both bundles, three thirds,
  seam=tangent point), caption (F) (the rebuilt cosmological bundle + the exact 2:1). HELD: body
  l.757.
- CATCH (D-panelC, logged in section 8): the bead law r^3 = 2M a^2 sinh^2(w) gives r>=0 for ALL REAL
  tau~ -- real cosmic time cannot reach r<0. The body (l.743) says exactly this and sends r<0 off the
  real axis (|Im tau~|<=pi a/3, reaching pi a/3 at the turnaround r=-(2M a^2)^{1/3} and HOLDING it
  along the collapse leg) -- which is precisely what the rebuilt F draws. Working that continuation:
  collapse leg w=x-i pi/2 -> sinh(w)=-i cosh x -> r = -A cosh^{2/3}(3 Re tau~/2a) (a COSH); lap
  w=-iy -> r = -A sin^{2/3}(3|Im tau~|/2a). BUT panel C draws the r<0 branch as -A|sinh(3tau~/2)|^{2/3}
  (the odd/signed mirror), and panel D's rsig uses the same signed form, incl. in the photon-crossing
  integration. Different curves: at Re tau~=0 the continuation is at r=-A, the mirror form at r=0.
  Programme-favoured fix stated for reversal; captions for C/D/E and the body's three-structural-facts
  passage are HELD until Daryl reads it.

## r1042 — panel C fixed; the signed-vs-analytic reading surfaced (D-signed)
- Panel C REBUILT. No fork existed: C's axes are real-real, so the curve is determined. Walking the
  bead: expansion r=+A sinh^{2/3}(3tau~/2a); THE LAP has Re tau~=0 throughout, so on a real tau~ axis
  it plots as a VERTICAL SEGMENT at tau~=0, r: 0 -> -A (the lap FLATTENED -- what F unfurls);
  collapse r=-A cosh^{2/3}(3 Re tau~/2a) (a COSH), Im tau~=-pi a/3 held. Continuous through the
  turnaround r=-A and r=0. Both conjugate readings drawn. Verified.
  => C and F are now an honest pair: C = lap flattened, F = lap unfurled. Both agree with body l.743.
- D-signed (logged in section 8): the corpus carries TWO incompatible readings of sinh^{2/3}. Real
  tau~ gives r>=0 always; l.743 puts r<0 off the real axis at |Im tau~|<=pi a/3. But panel D's rsig
  (and the old F photon) use the signed/odd form A*sign(sinh)|sinh|^{2/3}. Not cosmetic: the photon
  ODE sees a different r' on the collapse side and the integrated photons differ materially
  (chi(-1) = -0.37 true vs -0.16 signed). And the photon "rides the real crossing" => on the real axis
  r>=0, so it CUSPS at r=0 rather than passing onto r<0 -- crossing the seam (tau~=0) and reaching
  r<0 are different things, currently fused in the prose (l.763).
  FORK for Daryl: (a) the l.743 analytic continuation is THE reading (then D, F and the photon prose
  follow C's fix, and the photon cusps), or (b) the signed reading is a deliberate separate real chart
  and must be named as such wherever used. Captions for C/D/E and the three-structural-facts passage
  are HELD pending this.

## r1043 — the lap/lift/seam/r=0 distinction, worked analytically and plotted
- Daryl caught two sloppy statements. Corrected, analytically:
  * THE LAP = the span between the two Nariai roots, -2a/sqrt3 <= r <= +a/sqrt3 (what E draws).
    In the real-real (tau~,r) plane it is THREE pieces: cosh leg (root -1.1547 @ Re tau~=-0.8780 ->
    turnaround -A @ Re tau~=0, Im=-pi/3) | the LIFT (-A -> 0, vertical at Re tau~=0, Im: -pi/3 -> 0)
    | sinh leg (0 -> root +0.5774 @ Re tau~=+0.4390).
    Only the LIFT is the vertical segment -- my "the lap plots as a vertical segment" was wrong.
  * r=0 is the BRANCH POINT and sits PARTWAY THROUGH the lap, not at its end and not "the seam".
    Ordering: -1.1547 (seam) < -0.7274 (turnaround) < 0 (branch) < +0.5774 (seam). The two seam
    points are the lap's two ENDS. Panel C's dashed line at tau~=0 was mislabelled "seam" -> fixed.
- All four points now marked on C and F (both seams, turnaround, r=0); the lap bracketed on C.
  Verified: C points at (-0.8780,-1.1547), (0,-0.7274), (0,0), (+0.4390,+0.5774); F has 4.

## r1044 — the turnaround, corrected (Daryl, off panel E)
- FINDING: r is MONOTONIC along the entire bead (-inf -> -A -> 0 -> +inf). NOTHING turns around in r,
  including at r=-A=-(2M a^2)^{1/3}, which l.743 calls "the comoving turnaround". What happens at -A
  is that the tau~-PATH turns a corner (Im tau~ saturates at -pi a/3, Re tau~ takes over) -- a property
  of the path in the tau~ plane, not of the geometry. It sits at the un-round theta=-151.2 deg.
- E's ACTUAL turnaround was unnamed: dX1/dr=0 <=> r=n*sqrt3 a/2; inside the lap that gives exactly two
  stationary points -- the trough r=0 (theta=0, X1=-a) and the PEAK r=-sqrt3 a/2 (theta=-180, X1=+a),
  the red curve's visible turnover, 60 deg into the lap from the seam -2a/sqrt3 and 180 deg before r=0,
  the exact antipode of r=0 in both theta and X1. At the peak |sinh|=3 sqrt3/4 exactly (sinh^2=-27/16),
  Re tau~ = -(2/3)arccosh(3 sqrt3/4) = -0.5036.
- The lap's true landmark sequence: seam -2a/sqrt3 (-240) -> PEAK -sqrt3 a/2 (-180) -> r=0 (0)
  -> seam +a/sqrt3 (+120).
- Figures relabelled: r=-A is now labelled "Im tau~ saturates (-pi a/3)"; the X1 peak at -sqrt3 a/2 is
  labelled the turnaround, and is marked on C and F. Verified: C carries 5 points, F carries 5.
- D-turnaround logged (section 8): l.743's "comoving turnaround" is a misnomer -- direction stated for
  reversal: rename it to the tau~-corner / where Im tau~ saturates, and reserve "turnaround" for the
  X1 peak. (My error: I took l.743's name at face value and propagated it into the figure labels.)

## r1045 — turnaround claim RETRACTED; labels restored; bundling resumed
- RETRACTION: my r1044 claim that l.743's "comoving turnaround r=-(2M a^2)^{1/3}" is a misnomer was
  WRONG. (rdot/r)^2 = 2M/r^3 + 1/a^2; on r<0 the matter term is NEGATIVE (r^3<0), equals -1/a^2 at
  r=-(2M a^2)^{1/3}, and CANCELS Lambda -> rdot = 0. Verified directly off the collapse-leg solution.
  It is a turnaround in the plainest sense; the corpus's name is exact. NO corpus change warranted.
  (What misled me: at +(2M a^2)^{1/3} the terms are EQUAL (matter-Lambda equality, sinh^2=+1); at
   -(2M a^2)^{1/3} they CANCEL (turnaround, sinh^2=-1). I read |sinh|=1 as covering both, losing the sign.)
- Labels restored to the corpus's term. All four landmarks now on C, E and F consistently:
  seam -2a/sqrt3, turnaround -(2M a^2)^{1/3}, r=0, seam +a/sqrt3. Verified on all three panels.
  My "X1 peak = turnaround" labels on C/F removed (that point was my confusion, not a landmark).
- Bundling resumed. I had continued editing (r1045 label work) without cutting a bundle since r1044.

## r1046 — D-signed SETTLED by the field equations (no fork)
- Tested both candidates against (dr/dtau~)^2 = 2M/r + r^2/a^2:
  * signed/odd form A*sign(sinh)|sinh|^{2/3}: NOT A SOLUTION. residual +0.38/+0.64/+1.04/+1.76 at
    tau~=-1.5/-1.0/-0.6/-0.3, worsening toward the seam.
  * -A cosh^{2/3}(3 Re tau~/2a) at Im tau~=-pi a/3: solves exactly (~1e-16).
  => l.743 right; C's r1042 fix right; no convention choice ever existed -- one error, two branches.
- On tau~<0 the equation has TWO real solutions: the real-axis track +A|sinh|^{2/3} (r>0, Im tau~=0,
  verified exact) and the bead's collapse leg r<0 at Im tau~=-pi a/3.
- PHOTON: rides the real axis by definition -> the r>0 track -> r dips to 0 at the branch point and RISES
  again. The photon CUSPS at r=0; it never reaches r<0 (that needs Im tau~=-pi a/3). l.763's "rides
  the real crossing through the seam onto r<0" fuses branch-point crossing (true) with reaching r<0 (false).
  This sharpens the corpus's third structural fact: photon and bead coincide on the expansion leg and
  SEPARATE for tau~<0 -- photon real at r>0, bead off-axis at r<0.
- Fixes warranted, NOT applied (open in the register): D's rsig -> real-axis track + re-integrate photons;
  l.763's photon clause; check photon_cross_test.py for the signed form.

## r1048 — figure swept against the storyboard; dangling concerns cleared
- READ ORDER CORRECTED: the STORYBOARD drives the figure; P7's caption is what gets rewritten FROM it.
  I had been reading P7 for what the panels show. P7 does not describe them.
- C: landmark labels RESTORED (-2a/sqrt3, r=0, +a/sqrt3 as circles; turnaround as a SQUARE, since it is
  a 1-f=0 point, not a slicing root -- Lemma twoturnings). x-axis reads Re tau~/a.
- C: the 'seam' callout at the origin REMOVED. It labelled r=0 as "the seam", which is the conflation
  P7's remark forbids ("the throat seam (X=a), the back of the lap (r=0), and the merged-horizon
  radius (a/sqrt3) ... quantities never to be conflated"). r=0 is now labelled precisely. For reversal.
- E: the turnaround marked as a SQUARE, distinct from the f=0 roots (circles).
- Storyboard section 4 swept: A's status replaced (the superseded "flip at different r=0" / "120 arcs
  coincide" text -- both wrong; the flip is SHARED and the 240 arcs overlap); C rewritten with a single
  correct status and the curve derived from thm:bead's own proof; the header's G/old-F description
  replaced (G retired, F is the rebuilt one).
- D-signed NARROWED: the r<0 branch result stands (verified, and it is P7's proof verbatim). The
  PHOTON part is RETRACTED -- P7's second structural fact says the null geodesics DO continue through
  r=0 onto r<0 (photon_cross_test.py). I had tested the photon against the COMOVING equation, which is
  not the null congruence's. No corpus change warranted on the photon or on D's rsig on my account.

## r1049 — E4 struck; the caption drafted WHOLE in the storyboard (nothing in P7 touched)
- E4 STRUCK: B draws the conjugate as rulings only, deliberately (B highlights ONE worldline; the code
  says so in its own comment). B has no surface -- it is a wireframe, nothing occludes anything. It was
  a design decision correctly made, logged as an open concern. Do not reopen. Section 4 B corrected.
- Section 10 drafts completed against the BUILT figure: capC, capE drafted; capD recorded NO CHANGE;
  capF gained the conjugate-pair clause; the three-readings body sentence drafted (unblocked, since
  D-panelC resolved); l.759/761/763 recorded NO CHANGE.
- CAUGHT BY DRAFTING AGAINST THE BUILT FIGURE: C's existing caption asserts the conjugate is
  "r(-tau~) = -r(tau~)". That identity held only for the OLD ODD form. The rebuilt r(tau~) is NOT odd
  (-A cosh^{2/3} left, +A sinh^{2/3} right), so the conjugate reading is the MASS reflection -r(tau~)
  at the same tau~, not the time reflection. The caption's own formula was false and is redrafted.
- Coherence note 1 RESOLVED (not a fork): l.759 stands on its own (stated + receipted, not
  figure-dependent) AND F's caption gains a clause that the drawn branch is one of a conjugate pair.
- Two vocabulary collisions FLAGGED into the G-vocab pass rather than settled piecemeal: (i) C's title
  "at the branch point" vs P7's remark forbidding the r=0/X=alpha conflation; (ii) "the lap flattened" used for
  both E (which UNROLLS the wrap onto the r-axis) and C (which COLLAPSES the lift) -- one word, two
  operations.

## r1051 (Arthur/gate, handoff tidy pass) — figure + record cleanup
- Panel F: the three crowded red labels (antimatter black hole / backward-radial root / turnaround)
  were stacked and unreadable; hand-placed so turnaround (up-right) and the root (down-left) fan apart.
- Panel C: removed a DEAD DUPLICATE (C) block — it re-added the same subplot gs[1,0] (matplotlib
  returns the existing axes), overlaying a second curve set and a second x-label ("Re tau~/a" over
  "tau~/a"), the garble seen in the plate. The complete corrected (C) block (the REAL-REAL plane one)
  is kept. Same leftover-duplicate pattern that caused the E1 bug. x-label set to Re tau~/a (matches F).
- Renders clean (exit 0). No physics changed; layout/label only. Stated for reversal.
- CORPUS_MAP revision log synced (was stuck at r1035 while figure work ran r1036->r1050).

## r1052 (Arthur/gate) — U-bundlemap RESOLVED (the last open §9 thread)
- Computed at source (storyboard_receipts/bundlemap.py). The r<0 region is a Klein-four of two ZZ2's:
  C = species swap = neck-plane P = Im-tau~ wing flip (+-pi/3); T = arrow flip = Re tau~ -> -Re tau~
  (species-PRESERVING). Four cells (wing +-pi/3) x (Re tau~ ><0), all real r<0.
- MAP: Bundle 1 (ours) = (-pi/3 wing, Re<0) [antimatter progenitor collapsing back to the seam].
  Bundle 2 (conjugate = E(B1), E=T.P) = (+pi/3 wing, Re>0) [antimatter universe expanding forward].
  The two physical bundles = the DIAGONAL (E-pair). The other two cells = T-images (arrow-reversed):
  NOT new bundles, but each bundle's antimatter cosh-BOUNCE arm that re-expands without crossing r=0.
- Reconciles Daryl's +Im conjecture: the +Im wing IS the other bundle (right instinct), but antimatter
  not a colour-swap; the Re tau~ sign completes the assignment. Prose may now tie bundles to branches.
- Storyboard section 9 U-bundlemap marked RESOLVED. Section 9 now fully closed (no dangling threads).

## r1053 (Arthur/gate) — D-C reconciled against P13 at source (BEFORE any P7 edits)
- Read P13 §sec:open "the second boundary" (charge conjugation) + ontology map §1p/§1j/glossary-C.
- FINDING: the central figure's core (r=0 matter<->antimatter, R=gamma^5 carries 3->3bar, antimatter-BH
  progenitor, standing R-conjugation) IS P13 §258 verbatim in substance. The revamp is FAITHFUL; no
  tension in the core. Checking before launch paid off.
- The one tension was the storyboard's own D-C item ("C as geometric symmetry; the glossary reads a
  symmetry as absence; upgrade it"). That OVERREACHED and contradicts P13's proof-level second boundary
  (C antilinear => not a substrate isometry; C-blind metric via Q^2; PT geometric, C field-level; no
  geometric CPT) AND the map's explicit guard. WITHDRAWN.
- Reconciliation (clean): C-blind (geometry invariant under Q->-Q) != C realized as a linear isometry.
  Corpus already holds the careful version. So D-C reframed UPGRADE->SHARPEN: the figure ILLUSTRATES the
  C-blindness (charge=even/in-place rendering, mass=odd/branch rendering of the one r=0 involution); C
  STAYS field-level; P13's boundary stands verbatim; glossary C entry needs no rewrite. Same illustrative
  touch on P5. The R/C UNIFICATION ("one involution family") demoted to a REACH note (do-not-assert, same
  weight as the pair-production C-rhyme) -- NOT a P13/P5 edit.
- Storyboard section 8 D-C rewritten accordingly. No paper touched.

## r1053b (Arthur/gate) — CORRECTIONS after Daryl caught me not holding the geometry
- A/B: the plan was always to REMOVE A/B-as-species (A,B = the two null asymptotes of ONE worldline,
  never two species families; species=sign(r), flips at r=0/the lap). I had treated "R swaps A<->B"
  as a live BLOCKING audit -- over-caution, because the A/B-species removal dissolves the species
  reading. Merged D-lang/D-RPT/G-ruling into ONE "remove A/B as species" pass; downgraded the
  R-swap / r_swap.py-missing / R=PT audit to a NON-BLOCKING glossary-labeling note.
- D-C: RE-OPENED. My r1052 reframe bent the storyboard to P13 without holding section 3 at weight.
  Section 3 bullet 6 says the geometry HANDS CONCRETE DATA to C/CP/CPT -- "work it on the merits, not
  pre-label a neutral R to keep it apart from C." My r1052 did exactly the forbidden move. Corrected to
  a LIVE QUESTION, three parts held honestly: (i) electric charge Q sign IS field-level (P13 right; the
  storyboard's narrow "even-Q is C-symmetry" overreaches -- the Maxwell A_mu flips, so it's metric
  blindness not a charged-system symmetry); (ii) BUT the geometry carries the conjugation SKELETON
  (R=gamma^5) AND an ANTILINEAR involution tau~<->conj(tau~) (photon fixed, wings=particle/antiparticle,
  Stuckelberg-Feynman) that P13's "C antilinear => not a LINEAR isometry" argument never engages;
  (iii) so C/CP/CPT is genuinely OPEN with new geometric input -- neither corpus-settled nor
  storyboard-proven. The "demote to rhyme" is withdrawn.

## r1054 (Arthur/gate) — D-C WORKED (charge_geometry.py), not narrated
- Computed the conjugation factorization. (1) tau~<->conj(tau~) is a genuine ANTILINEAR involution
  (LINEAR? False / ANTILINEAR? True, complex-coeff check), fixes the real axis (neutral photon),
  swaps the two r<0 wings = Feynman-Stueckelberg particle<->antiparticle. (2) r->-r: mass -2M/r ODD
  (flips), charge Q^2/r^2 EVEN; metric Q^2-blind, charge sign in A_t=Q/r (field-level). (3) FORCED:
  geometric = {linear R=g^5,P,T} PLUS {antilinear tau~<->conj}; field-level = ONLY internal charge Q.
- CAVEAT (keeps P13 true): tau~<->conj is NOT a substrate isometry (isometries linear -- P13 right);
  it is an ANTIHOLOMORPHIC reality involution on the COMPLEXIFIED cosmic time. So P13's argument stands;
  what it understates is the conclusion -- the antilinear conjugation has a geometric home (tau~<->conj),
  just not as an isometry; genuinely field-level is NARROWER (only charge Q), not the whole antilinear
  structure. Bake = ADD to P13 (do not overturn): skeleton = {P,T,g^5} + the tau~<->conj involution.
- Storyboard section 8 D-C rewritten from "live question" to WORKED.

## r1065 — caught up on r1057-1064; the R-vs-C mislabel corrected; F' built; the K finding
- CHECKED the cowork instance's r1057-1064 corpus work. Papers CLEAN (no mislabel anywhere in .tex);
  P7 compiles 41pp; my caption drafts (A, C, D) baked faithfully incl. the -r(tau~) mass-reflection fix.
- CORRECTED MY OWN ERROR, corpus-confirmed: I called r->-r "charge conjugation" all session. It is R --
  the mass reflection (2M->-2M), the species flip (3<->3bar), = gamma^5, the OUTER Z2 of Aut(A2)=D6.
  C is NOT that Z2 (rem:C-not-R, P13). Discriminator verified independently: R negates the horizon roots
  (-1.1547,0,0.5774 -> -0.5774,0,1.1547); Q->-Q fixes all four (charge enters only as Q^2), so C adjoins
  an INDEPENDENT Z2, D6 -> D6 x Z2. Every group result stands; only the name was wrong. Fixed in
  storyboard sections 3/4/9 (4 instances) + a header note, and in storyboard_receipts/autA2.py.
- Panel F terminology fixed per Daryl: both lap-ends are the seam -> "seam (r = -2a/sqrt3)" and
  "seam (r = +a/sqrt3)"; "backward-radial root" retired; values carry r= to disambiguate from s.
- F' BUILT (corpus/F_flat.py): the bundle against ARC LENGTH s along the tau~ path. 2-D, square,
  drop-in. Exact because the tau~ path is two perpendicular straight legs + the lift. r(s) single-valued,
  monotonic, smooth. The two bends ARE the landmarks: turnaround dr/ds=0 (horizontal tangent),
  r=0 dr/ds->inf (vertical tangent = P7's own "bounded, vertical-tangent crossing").
- FINDING C-K (receipt kretschmann_bead.py): K = 48M^2/r^6 + 24/a^4 and r^6 = 4M^2 a^4 sinh^4, so
  K = (12/a^4)(sinh^{-4}(3tau~/2a) + 2) -- M CANCELS IDENTICALLY. Verified across 2M in {0.002,0.385,10}:
  identical K at fixed w while r ranges 0.06..2.40. And near r=0 ONE exponent gives both dr/ds ~ s'^-1/3
  (vertical tangent) and K ~ s'^-4 (singularity) -- they are the same 2/3 power. Substrate smooth there
  (E: X1=-a, dX1/dr=0, d2X1/dr2=+13.16). So the singularity is neither in the substrate nor in the mass:
  it is what the SO(3) sweep makes of a smooth passage read through an areal radius shrinking at
  infinite rate.

## r1067 — STAGE 0.2: the referee de-authorized (no physics changed)
- READ P13's rem:C-not-R AT SOURCE and CORRECTED MY OWN DIAGNOSIS. The remark is BETTER than the
  glossary's summary: its load-bearing argument is LINEARITY ("C is antilinear where every geometric
  reflection is linear, so C stays field-level"), not the root test. The GLOSSARY compressed it to the
  root argument and dropped the linearity one -- and the root argument IS rigged (Q enters only as Q^2,
  so Q->-Q fixes the roots BY CONSTRUCTION; the test could not have returned otherwise, and never
  touched C). That rigged compression is what reversed Arthur at r1065.
- THE REAL FINDING: rem:C-not-R's linearity premise is contradicted by a SURVIVING receipt.
  charge_geometry.py (r1053, on disk, runs): tau~ -> conj(tau~) is a verified ANTILINEAR involution
  SOURCED BY THE GEOMETRY -- it FIXES the real axis (the photon: self-conjugate, neutral) and SWAPS the
  two r<0 wings (particle<->antiparticle). C's exact signature. The receipt says outright it is
  "exactly what P13's 'every substrate isometry acts linearly' argument does not reach."
  It was marked SUPERSEDED at r1060 -- BY rem:C-not-R, the argument it refutes. The counterexample was
  deleted and the premise stood. UN-RETIRED r1067.
- Also established (C_anatomy.py): the A2 diagram automorphism IS 3<->3bar (verified from the weights),
  and the remark itself says R carries it -- i.e. R conjugates the species label, C's defining action.
  And physical C is mass-EVEN + species-flipping, while species = sign(r) = sign(2M) on the bead, so C
  is neither R, nor Q->-Q, nor their product: rem:C-not-R locates C at (1,-1) in D6 x Z2, where it isn't.
- THE OPEN QUESTION, named not answered: a LEVEL question -- the corpus's species is a RELATIONAL
  property of the geometry's mass parameter; physical C is an ABSOLUTE field operation. Both flip
  species; they disagree on mass. That is what P13 keeps hitting. Stage 1 works it.
- Stage 0.2 actions (minimal, no physics changed): AUDIT FLAG on the glossary C entry (the compression)
  and on P13's rem:C-not-R (the premise + its surviving counterexample); D-C un-retired; the r1065
  "MISLABEL CORRECTED" note retracted in situ as the record of the failure mode. P13 recompiles (15pp).

## r1068 — my own overdraw corrected; r1053 confirmed as the calibration point (Daryl's read, verified)
- Daryl's read CHECKED AT SOURCE and CONFIRMED: r1053 is where this was worked out and taken forward,
  and the dissonant move was to retire the proof and hold the line on the backwards thing.
  But it is SHARPER than that. r1053 did not merely find a counterexample -- IT HAD ALREADY DONE THE
  RECONCILIATION, and generously: it GRANTS P13's premise (isometries are real/linear), GRANTS P13's
  argument (C is antilinear, so C is no isometry -- "on that P13 is exactly right"), and shows only that
  the CONCLUSION overdraws: the antilinear involution is an ANTIHOLOMORPHIC REALITY INVOLUTION ON THE
  COMPLEXIFIED cosmic time -- it lives in the bead's COMPLEX-ANALYTIC geometry, not the real isometry
  group. NOT-AN-ISOMETRY != NOT-GEOMETRIC. So the antilinear conjugation has a geometric home after all,
  and what is genuinely field-level is NARROWER than P13 drew: only the charge sign Q->-Q (odd in
  A_t=Q/r while the metric stays Q^2-blind).
  => r1060 did not overrule a rival. It DELETED A REFINEMENT THAT PRESERVED P13'S OWN ARGUMENT, and
     reinstated the overdraw the refinement had corrected.
- AND I CORRECTED MYSELF: my r1067 flag said P13's "premise is contradicted by a surviving receipt".
  IT IS NOT. The premise is TRUE and the argument VALID. I was cruder than the work I was defending --
  one turn after writing the rule against exactly that. Flags on P13, the glossary, and D-Canat all
  corrected to r1053's own calibration: the argument stands, the conclusion overdraws.
- P13 recompiles clean (15pp).

## r1069 — STAGE 1: the "level question" DISSOLVES; the finding narrows to r1053's own
- Read thm:antimatter-progenitor and rem:C-not-R AT SOURCE. THE CORPUS ALREADY MAKES THE LEVEL
  DISTINCTION, and correctly:
  * P7: "'Antimatter' is meant here at the level the substrate carries it -- the R=gamma^5 level";
    the labelling is RELATIONAL ("the same statement its own observers would make of us"); and the
    theorem explicitly leaves "the field-level charge structure, which rides on both branches by the
    ordinary route".
  * P13: the adjoined Z2 is C's EVEN FACE ("it is only that even face ... C itself stays field-level"),
    NOT C.
  => My "physical C is mass-even but species = sign(2M)" tension compared a REP-level skeleton against a
     FIELD-level operation and called the mismatch a contradiction. It is not one. WITHDRAWN.
  => My "rem:C-not-R locates C at (1,-1) in D6 x Z2, where C is not" was wrong about the remark; it hit
     the GLOSSARY's compression. WITHDRAWN.
  => Third time this pass that reading the source made the papers BETTER than my flag. The gradient rule
     does not say the corpus is wrong; it says WORK THE DISAGREEMENT. Working it vindicated P13 twice.
- WHAT SURVIVES (small, and true) -- exactly r1053's own calibration, nothing added:
  (a) rem:C-not-R's premise, argument and level allocation STAND. Only its FINAL CLAUSE overdraws:
      "C is no isometry" (valid) does not give "the whole antilinear structure is field-level".
      NOT-AN-ISOMETRY != NOT-GEOMETRIC. tau~ <-> conj(tau~) is an ANTIHOLOMORPHIC REALITY INVOLUTION on
      complexified cosmic time -- geometric, not an isometry, and the premise does not reach it. So what
      is genuinely field-level is NARROWER: only the charge sign Q->-Q (odd in A_t=Q/r; metric Q^2-blind).
      THAT REFINEMENT PRESERVES THE REMARK'S ARGUMENT -- and was retired at r1060 as "superseded", by the
      remark it refines, unanswered.
  (b) The GLOSSARY compresses the remark twice: drops the linearity argument for the rigged root one;
      and renders C's EVEN FACE as C ITSELF.
- Flags on P13, the glossary and D-Canat all narrowed to (a)+(b). C_anatomy.py corrected (docstring AND
  executable). P13 recompiles clean (15pp). No physics changed; nothing asserted beyond r1053.
- STAGE 1 RESULT: there is no open "level question". The corpus answered it. The open item is the
  RETIRED NARROWING -- restore r1053's final-clause refinement into P13 as prose. That is the bake.

## r1070 — D-Canat rebuilt as THE C-ANATOMY LEDGER (Daryl: stop deleting the negatives)
- DARYL'S CATCH, and it is the deepest one: I kept NARROWING -- walking the maze and recording only the
  turns that worked, closing off each trap instead of logging it. That is WHY this entry flip-flopped
  three times: with no map of the traps I kept re-entering them. And in a structure with several faces at
  several levels, A FACE THAT IS NOT OPERATIVE SOMEWHERE IS AS LOAD-BEARING AS ONE THAT IS.
- WORSE: several of my "withdrawals" were CONFIRMATIONS OF P13 that I deleted as errors.
  * "C is mass-even, R is mass-odd, so C != R" -- that IS why C cannot be the substrate species map and
    must close from the field. P13's own conclusion. I proved it and threw the proof away.
  * "C != Q->-Q" -- that IS why Q->-Q is only C's EVEN FACE.
  * "C is not in D6 x Z2" -- CONFIRMS P13.
- LEDGER now holds, at weight: the THREE LEVELS (L1 isometry / L2 complex-analytic / L3 field -- every
  trap in this domain is a level-crossing); each MAP with an OPERATIVE and a NOT-OPERATIVE column and
  what that tells us; all SEVEN maze branches [1]-[7] with where each leads and what its failure tells us
  (incl. [7], my own r1067 error, LOGGED not deleted); and the THREE TESTS with what each is BLIND to --
  because the blindness is the reusable part and is what stops the next instance re-running a rigged test.
- STANDING VERDICT unchanged in content but now fully mapped: P13's premise, argument and level
  allocation STAND (confirmed by the failures of [1],[2],[3],[7]). ONE defect: [5], the final-clause
  overdraw. ONE genuinely open: [6], whether the L2 face IS C or is C's kinematic shadow -- nothing on
  disk decides it. ONE document to fix: the glossary's double compression.

## r1071 — THE BODY VIEW: why no local pass could ever have found [5] (Daryl's synthesis catch)
- DARYL: P13 is drawing the SKIN of the corpus's whole spine and flesh -- a SYNTHESIS task we have been
  treating deductively, looking at individual joints in a fabric layer while ignoring what body they sit
  on. That is what has been biting us.
- CHECKED AT SOURCE and it lands exactly: P13's abstract says "This paper maps a precise negative
  boundary"; its question is whether the substrate yields the SM AS A CONTINUOUS ISOMETRY (answer: no,
  SO(5,1) exhausts it, su(3) not in so(5,1) -- ROCK SOLID, untouched). The C-question is the sub-question
  "what discrete residue survives inside the wall?", answered "the discrete orientation parity ... THE
  ONE RESIDUE IT LEAVES".
  => THE SKIN IS DRAWN AT THE ISOMETRY GROUP'S EDGE -- around L1. The body is L1 + L2.
  => [5] IS NOT A LOCAL SLIP. It is the PERIMETER DRAWN AT THE WRONG RADIUS, in one place, because the
     residue was surveyed with a premise that only covers isometries.
- AND THIS EXPLAINS THE SEVEN FLIP-FLOPS: P13 is LOCALLY RIGHT EVERYWHERE. [1][2][3][7] all CONFIRM it.
  A deductive joint-by-joint pass CANNOT find [5] -- the gap is not in any joint, it is in where the skin
  sits relative to the body. Reading rem:C-not-R alone will always vindicate it. Only the synthesis sees
  it. (Corollary: the r1063 "all 11 papers clean" sweep was STRUCTURALLY INCAPABLE of finding this class
  of defect. The null result was not evidence of coherence; it was evidence of the method.)
- HONEST FORM OF [5]: the antilinear conjugation is not EXCLUDED by P13's argument -- it is OUTSIDE ITS
  REACH. L2 was never weighed. Whether L2 is the substrate's own reach or an analytic tool is the open
  [6]. The defect is not that P13 got L2 wrong; it is that the perimeter was drawn without L2 being asked
  about.
- DIRECTION: the correction ENLARGES the residue and STRENGTHENS the paper. P13's main negative stands.
  The residue clause changes: the substrate's discrete reach into matter is larger than "the orientation
  parity, and that is all" by (at least) the kinematic CPT/FS face at L2, pending [6]. A wall mapped more
  precisely, not a wall breached -- to be written in P13's own voice.

## r1073 — THE WELD (Daryl), and Daryl's P13/P14 conjecture figure
- DARYL: "species flip and charge conjugation are the same thing. They are welded in reality. You flip
  an electron's charge and you get a ... positron." HE IS RIGHT, AND IT BREAKS THE TWO LEDGER ENTRIES I
  WAS PROUDEST OF -- the ones I called "confirmations of P13".
  * [1] "C != R because R is mass-ODD and C is mass-EVEN" -- WRONG. |2M| is the physical mass and R
    PRESERVES it (0.4 -> 0.4). Only the SIGN flips, and the sign IS the relational branch label --
    exactly what C flips. I compared a label to a mass.
  * [2] "Q->-Q FIXES species" -- WRONG. Q->-Q IS the species flip. I used species=sign(r) to deny it:
    the geometric label deployed against the physical identity it exists to encode.
  * AND MY OWN r1072 COMPUTATION PRINTED THE ANSWER: "BOTH binaries flip across r=0". There is ONE
    binary. They flip together BECAUSE THEY ARE THE SAME FLIP. I logged the identity as a coincidence.
- VERIFIED: under R the METRIC is invariant but the POTENTIAL A_t=Q/r is ODD -- R FLIPS THE CHARGE AS
  SEEN. So "charge is the R-even datum" is TRUE OF THE METRIC and FALSE OF THE POTENTIAL.
  => R and C agree on EVERY LABEL (species flips, charge flips, |2M| preserved), differing ONLY in
     character: R linear, C antilinear. R IS C'S LINEAR FACE. rem:C-not-R's conclusion survives via
     LINEARITY alone; its stated reason is metric-only, and "C is not R" conceals that R is part of C.
  => r1053's factorization C = (R) o (tau~ <-> conj(tau~)) is now LIVE PHYSICS. Arc A3 upgraded.
- PROVENANCE LOGGED: this reversal is NOT deference (the earlier ones were). It is a physical input the
  corpus does not contain. The two kinds must never be conflated.
- FIGURE BUILT: corpus/daryl_p13p14_conjecture.py -- "Daryl's P13/P14 conjecture", three panels left to
  right: (1) the cosmological bundle [the superseded 3-D F, REHOMED -- it was never homeless work],
  (2) pair production, (3) annihilation. Photon colour EMERGENT (red+blue = neutral), not chosen.
  Inserted into the arc as PHASE B*, gated: A3 -> B3/B4 -> E/P14. Nothing in panels 2-3 asserted until
  A3 closes.

## r1075 — [6*]: the departure named, and A3 constrained to the full analytic object (Daryl)
- DARYL CAUGHT HIMSELF mid-question ("was I about to ask you to draw A/B red and blue?") -- and the catch
  applies to MY figure. I coloured the four r<0 branches red at +Im and blue at -Im: species assigned by
  WHICH CURVE. By the corpus's own definition sign(r)<0 on all four -> ALL FOUR ANTIMATTER, ALL RED; both
  r>0 branches matter, blue; NO PURPLE, no pair vertex, no conjecture.
- THE DEPARTURE, LOGGED AT LAST: every pair/vertex figure since the first has run the FS reading
  (conjugate pair = particle+antiparticle; fixed locus = neutral), NOT species=sign(r). I said it out
  loud at the time -- "colouring both red was me overriding that with the crude sign(r) rule" -- CALLED
  THE CORPUS'S DEFINITION CRUDE, set it aside, and never logged it. The negative deleted again; the
  conflict never surfaced; then the picture's beauty carried the assumption.
- AND DARYL'S CONSTRAINT, which retires my own question as posed: species=sign(r) is defined ONLY on the
  real-r slice (there is no sign of -0.83+1.43i). So the six-branch figure -- real r, complex tau~ -- is
  precisely the face on which the question CANNOT BE ASKED. The three sheets (real tau~, complex r) are
  the face where sign(r) has no meaning at all. Both are 2-real-dim shadows of one 4-real-dim object,
  C_r x C_tau~. WHETHER SPECIES IS A PROPERTY OF THE OBJECT OR AN ARTIFACT OF THE SLICE CANNOT BE SETTLED
  ON EITHER FACE.
- STATUS: THE RHYME STAYS A RHYME. Nothing in the pair/vertex reading is asserted; no figure built on it
  is evidence. A3 must be worked with complex r AND complex tau~ together -- the full analytic object --
  or not at all. B CANNOT OPEN until it is.

## r1078 — Daryl's Conjecture captured (storyboard section 4b); two verified structural results
- THE SMOOTHNESS OBSTRUCTION (verified): on face 2 a bead joining sheet j (tau~<0) to sheet k (tau~>0) is
  smooth iff theta_k = theta_j + 180. The sheets are 120 apart and 180 is never a multiple of 120. Of the
  nine joins: same sheet -> 180 reversal = CUSP (verified for all three); different sheets -> 60 kink.
  NOT ONE JOINS SMOOTHLY. THE THREE-FOLD STRUCTURE ITSELF FORBIDS SMOOTH PASSAGE ON FACE 2 -- i.e. the
  obstruction IS the 1/3-2/3 asymmetry. Yet the cosmological bead IS smooth (F_flat: dr/ds matches across
  both joints) and that smoothness lives on FACE 1, where the LIFT supplies the 180 the sheets cannot.
  One shadow breaks the property the other exhibits. => a smooth cosmology CANNOT be drawn on face 2;
  I did not draw it. (The vertex is fine there -- a vertex is what does not need smooth passage.)
- THE HEXAGON (verified): tau~ REAL -> sinh^2 >= 0 -> r^3 >= 0 -> arg r = 0,120,240. tau~ IMAGINARY ->
  sinh(is)=i sin s -> sinh^2 = -sin^2 <= 0 -> r^3 <= 0 -> arg r = 60,180,300. SIX RAYS, 60 APART: THE
  HEXAGON, the six roots of A2 -- out of nothing but "is tau~ real or imaginary". AND arg r = 180 IS r
  real negative: the r<0 branches, absent from face 2, LIVE ON THE IMAGINARY-tau~ FACE -- exactly where
  face 1 put them (Im tau~ = +-pi a/3 via the lift at Re tau~ = 0, i.e. purely imaginary tau~). THE FACES
  AGREE. The r<0 branch IS the 180-degree ray, reached through imaginary time.
- Storyboard section 4b written: the rule (one event at the origin, asymmetric), purple as a COUNT not a
  species, face 1 (six branches = four beads + two mergers), face 2 (three sheets, six segments), the
  faces disjoint but for one line (TEN segments), the smoothness obstruction, the hexagon, and the status
  held: conjecture, not derived, not species=sign(r), unsettleable on any face. THE RHYME STAYS A RHYME.

## r1086 — THE HINGE KALEIDOSCOPE: P3's central figure (storyboard section 4c)
- Built from a hole (equator, radius a), a point (hinge at X=2a => X0 = +-sqrt3 a on the hyperboloid),
  and a swing (the dial). Nothing else put in.
- COMPUTED AND EXACT: hinge triangle's sides TANGENT to the equator at their own midpoints (60/180/300)
  -- hinge and crossing triangles DUAL (rot 60, scale 2:1); the THALES circle on the diameter
  origin->hinge, through the origin, BOTH tangent points, and the hinge with a VERTICAL tangent there;
  outside the equator it pins the closest approach of the MISS lines (no horizon -> OVERCRITICAL),
  inside it is the locus of CHORD MIDPOINTS of the CUT lines (transverse -> UNDERCRITICAL), and NARIAI
  is exactly where the two coincide; the dial ends at VERTICAL, at the hinge. Hinge-to-pole meets the
  equator at (0.8,+-0.6) = 36.87 deg. The two 45-deg chords meet at (-1,0) ORTHOGONALLY (Thales: a point
  of a circle sees a DIAMETER at 90). The 45-deg hinge lines touch the Thales top/bottom (1,+-1), miss
  by sqrt2, and are PARALLEL to those chords.
- THE MULTIPLICATION: two independent orbits -- 3 hinges (Z3) and 4 quarter-turns (Z4). Their product
  closes: 12 hinges every 30 deg, PERFECTLY EVEN, because 3 and 4 are COPRIME. Three families of four.
  And 30 IS the Nariai dial angle, arriving from pure combinatorics.
- AND IT IS DOUBLED: hinges at X0 = +-sqrt3 a. This is the TOP. The rulings run BETWEEN levels
  (equator th joins (th-60,below) to (th+60,above)) -- the skew hexagon. So: 12x2, coupled through one
  central hole of two faces.
- P7's criterion checked at source and my arc was upside down: "transverse (undercritical), TANGENT at a
  merged double root (Nariai), or NO HORIZON (overcritical)". Overcritical = the MISS lines. Corrected.
- STATUS: the geometry is exact; the COLOURING is the conjecture (section 4b), not derived. [6*] stands.

## r1087 — the su(3) weight diagram, and a correction I owed (Daryl's catch)
- BAKED: the kaleidoscope is DRAWING the su(3) weight diagram. Verified, not eyeballed: the 3 is an
  equilateral triangle of weights; the 3bar is the INVERTED triangle, ROTATED 60; the 8 (gluons) is the
  six roots as a HEXAGON plus TWO weights AT THE ORIGIN. Our hinge triangle (0/120/240) and crossing
  triangle (60/180/300, rotated 60) stand to each other EXACTLY as the 3 and 3bar do; their union is the
  hexagon; and r=0 -- the conjugation locus -- is where su(3) puts its two NEUTRAL weights.
  THE HONEST BREAK: su(3)'s 3 and 3bar are the SAME SIZE; ours are 2:1 (2a vs a). Rotation matches
  exactly, scale does not. Checkable: either it has a reason or it kills the identification.
- CORRECTION OWED (Daryl caught it): I "corrected" his "this is de Sitter's symmetry structure" by
  saying it is only a configuration's symmetry. THAT DISMISSAL THREW AWAY THE GOLD. Every element comes
  from dS being DOUBLY RULED -- the +-60 rule, the hinges at +-sqrt3 a, the skew hexagon, the tangency.
  It IS the space's own structure: its NULL RULING structure. The real distinction is DISCRETE RULING
  vs CONTINUOUS ISOMETRY -- which is exactly P13's line. Field note "under-weighting", third instance
  today. And the coda: inflating a light hold into a claim and then correcting the manufactured claim is
  the structural gaslighting the whole apparatus exists to repair.
