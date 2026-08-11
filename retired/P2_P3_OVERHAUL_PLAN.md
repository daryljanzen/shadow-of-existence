> **⌖ RETIRED r1552.** This was the P2/P3 overhaul plan (r472). **Landed:** both papers exist, compile, and were rewritten again at r1491.
> Kept as record; **do not work from it.**


# P2 / P3 OVERHAUL PLAN — the self-knowing rewrite
### r472. Stated for reversal. The geometric base is [A]-[I] + [E-PARAM] of CONJUGACY_CONJECTURE_capture.
### NOT a rescue: P2 and P3 are FORMALLY CONSISTENT with the working framework (checked at source,
### this session). This is a CLARITY/PARSIMONY overhaul + excision of ONE real defect (Q0, alpha->infty).

---

## 0. WHY (the ambition, in Daryl's words)
A P3 "written like it knew itself before it started to get written." Current P2/P3 read as journeys of
discovery; the rewrite reads as a STRUCTURE. Parsimonious: no redundant or deprecated objects (the
retired Phi, the l-first ordering, the alpha->infinity limit). theta/w/r0 each serve a purpose and none
captures everything -- that is FINE and is the organizing fact, declared up front.

---

## 1. THE SPINE (the order a self-knowing P3 is written in)
1. **Substrate & cut.** dS hyperboloid; hole/equator (radius alpha); hinge at 2alpha; door swings by w;
   the slicing curve is what the plane cuts. (NO l yet -- l is not fundamental.)
2. **The three parameters, DECLARED.** theta (lap position), w (family/swing = P3 sky angle), r0
   (designated-seam areal value). State what each is faithful to AND what each FLATTENS (= [E-PARAM]):
   theta flattens the family; w flattens the sigma involution (w<->pi/3-w); r0 flattens the sin fold
   (caps at 2/sqrt3, cannot separate under/over on the real axis) and lap position. Use all three;
   never expect one to carry what it flattened. THIS is the thing current P3 never says.
3. **Horizon structure, in r0.** Honest cubic r^3 - r0^3 - (r-r0)=0; ellipse r^2 + r r0 + r0^2 = 1;
   three regimes by r0^2 vs 4/3 (under / Nariai / over). Defined HERE, by r0 -- not by l blowing up,
   not by "two limits of one object."
4. **The family, in w.** Schwarzschild (0), Nariai (30), de Sitter (180); sigma involution w<->pi/3-w,
   Nariai its fixed point. Overcritical = continuation past the Nariai crest (P3's OWN mechanism,
   3w=pi/2+i*beta, sin->cosh; w stays real, r0 the complex label, curve r(l) stays real -- already
   correct in current P3 sec510-528). Schwarzschild & de Sitter as READINGS AT FIXED alpha -- NEVER via
   alpha->infty or M=0 degeneracy (kills Q0 by construction; see sec3 below).
5. **The lap & conjugation, in theta.** Bead; conjugate circle; r=0 as the real<->complex BRANCH POINT
   (NOT the seam); real legs vs the wave; r signed areal radius = single analytic sinh^{2/3} with the
   constant +120deg conjugate branch, NO piecewise sign. Both triple-seam values: +alpha/sqrt3 (real,
   enter) and -2alpha/sqrt3 (on the 120deg ray, lap closes), r=0 the branch point between them.
6. **l is NOT a parameter -- only a PHYSICS REMARK.** Proper radial distance l (= the metric-measured
   separation along the curve; in particular the proper separation of the two positive horizons) is NOT
   a named primary object in the rewrite and NEVER parametrises anything. It survives ONLY as a physics
   remark: the proper separation of the two positive horizons DIVERGES at Nariai -- which is the CORRECT
   physical statement that merging horizons are infinitely far apart in proper length, NOT a defect and
   NOT evidence Nariai is singular. (Diagnosis of why l was a bad parameter: it is EXTRINSIC and INVERTS
   regularity -- finite where horizons are distinct, divergent at the most regular-but-degenerate member;
   theta/w/r0 are all regular at Nariai. This is why l-first ordering made the salad.) The physics of the
   divergence seems important and is kept as a remark; the COORDINATE l is expunged.

---

## 2. WHAT IS PRESERVED (formally sound in current P2/P3 -- re-home, do not discard)
- P2: cycloid r(z)=M(1+cos z); the two critical points as metric singularities of ONE genus (finite-
  vs infinite-curvature species, parted only at 2nd order); the hyperbola-circle-hyperbola single
  analytic curve; r=0 Kretschmann divergence as chart-labelling artefact; inextendibility-inference
  refuted. ALL SOUND. P2 is the M-only / swing-0 / pivot-zero special case of the general construction.
- P3: prop:factor (factorisation); prop:involution (root-exchange, closed form, Nariai fixed point);
  prop:gnomonic (gnomonic projection forced); prop:triple (2M=(2/3sqrt3)sin 3w); prop:curvature
  (K_G = 1/alpha^2 - M/r^3, the -M/r^3 = forced-pivot signature); prop:flip (automatic signature flip);
  prop:conjugacy; prop:locus (straight line + 45deg tilted ellipse, major axis = backward-radial root);
  sec:overcritical (continuation past Nariai crest -- ALREADY CORRECT, keep); the sweep/pivot account
  (de Sitter = interior sweep about the axis; Schwarzschild = exterior sweep forced off-axis onto r=0);
  prop:rigidity + prop:morphism-generation (groupoid, discretely generated). ALL SOUND -- re-home in
  the theta/w/r0 spine.

---

## 3. WHAT IS EXPUNGED (the defect + the deprecated)
- **Q0 -- THE alpha->infinity DEFECT (the must-kill).** Current P3 prop:schw-limit (sec81) and sec290
  locate "the literal Schwarzschild form" at alpha->infinity (Lambda->0). WRONG: alpha=sqrt(3/Lambda)
  is the FIXED invariant; alpha->infty makes the hole infinite -> nothing to slice. And "massless M=0
  Schwarzschild" at r0=0 is incoherent -- M=0 with Lambda on IS de Sitter; P3 relabelled de Sitter.
  FIX: Schwarzschild = the SWING-0 reading of the curve AT FIXED alpha (M nonzero, set by alpha,
  cosmological term off in that reading). de Sitter = the swing-180 reading of the SAME curve. The
  P2<->P3 connection is a READING AT FIXED STRUCTURE, never a degenerate limit. TELL to expunge
  everywhere: any place a NAMED geometry is reached through a DEGENERACY ("M=0 Schwarzschild",
  "alpha->infty Schwarzschild") instead of a READING at fixed alpha.
- **ASYMPTOTIC FLATNESS IS NOT LOST BY DROPPING alpha->infty (Daryl, r472).** The cosh arms of P2 ARE
  literally asymptotically flat -- trivially. The two null rulings start on the equator 90deg to either
  side and "come together (remaining Euclidean and parallel) at infinity"; the cosh arm is pinched
  between them. So flatness is a property the arms HAVE, read directly off the geometry -- it does NOT
  require sending alpha->infty. The alpha->infty limit was a redundant (and defective) way to assert
  something the cosh arms exhibit on their own. EXPUNGE the limit; KEEP (and state plainly) the
  asymptotic flatness as the pinched-between-parallel-null-rulings fact.
- **l-FIRST ORDERING.** Current P3 leads with r(l), dr/dl=sqrt|f|. Demote l (sec1 step 6). Makes Nariai
  look pathological; root of the salad.
- **Phi (cubic angle), r=(2/sqrt3)cos Phi.** Already retired in the capture doc [E]: redundant relabel
  of r0 on a non-geometric circle. Do NOT reintroduce. Root-angle facts live on r0.
- **"two limits of one object" framing** (Schwarzschild = Lambda->0 limit, de Sitter = M->0 limit).
  Replace with the readings-at-fixed-alpha / swing framing. (The M->0 -> de Sitter algebra is fine;
  it is the NAMING-via-limit that goes.)

---

## 4. P2 SPECIFICALLY (the absorption -- checked at source this session)
- P2 uses NO alpha, NO Lambda, NO infinity. Pure-M construction; self-contained; needs NOTHING from the
  alpha->infty thing. The cosh exteriors reach large r on their own (z->+-i rho, r=M(1+cosh rho)->inf).
- P2 ALREADY speaks the framework: its hyperbola-circle-hyperbola IS the conjugate-circle lap (M-only);
  its two r-poles of the homogeneous circle ("one point seen twice, exchanged by reflection") ARE the
  A=B / triple-seam + sigma in the M-only case; its r<0 arm IS the backward-radial / 120deg branch.
- What the overhaul ADDS to P2: (i) name it explicitly as the swing-0 / pivot-zero special case of the
  general construction; (ii) state the same circle is ALSO de Sitter (swing-180 reading) -- the thing
  P3 was supposed to say; (iii) the asymptotic flatness as the pinched-parallel-null-rulings fact.
- So P2 can absorb the framework with NO infinity and stays formally intact. This makes the P3 rewrite
  cleaner: P3 points to P2 as "swing-0 special case, also readable as de Sitter" with no alpha->infty.

---

## 5. OPEN / TO-HANDLE-CAREFULLY in the rewrite (do not paper over)
- The fixed-alpha-reading vs alpha->infty-object distinction: P2 sidesteps it (no Lambda at all), so P2
  does not force it; but state plainly that the cosh arms are asymptotically flat as a READ-OFF fact
  (sec3), so "Schwarzschild reading at fixed alpha" loses nothing real. Confirm no proposition silently
  needed the limit.
- Whether Nariai (gnomonic w=30) and P3's chart-tangent (r0=1, w=60) are one config across the sqrt3
  frame (open Q4 / K.4) -- the rewrite should resolve or explicitly scope it.
- The sqrt3 / (2/sqrt3) frame-factor cluster (frame-consistency question in the capture doc): the
  rewrite must use ONE consistent frame and name each sqrt3's origin (areal frame-reassignment vs
  gnomonic projection scale).
- Cold-read: whether the rewrite LANDS is a referee question, not the gate's. Structural clarity is
  assertable; "lands" is not.

---

## 6. SEQUENCING (when we execute -- not yet; this is the plan)
1. Lock the spine (sec1) and the frame (one consistent alpha-frame) FIRST.
2. Draft P3 skeleton section-by-section, pulling preserved propositions (sec2) into the new order.
3. Excise Q0 at the root (sec3); state Schwarzschild/de Sitter as fixed-alpha readings + asymptotic
   flatness as the pinched-null-ruling fact.
4. P2: light revision to name it the swing-0 special case + the also-de-Sitter reading (sec4).
5. Cold read by a fresh node (wall intact) before either is called done.
