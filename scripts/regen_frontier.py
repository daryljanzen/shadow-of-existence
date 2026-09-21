#!/usr/bin/env python3
"""regen_frontier.py -- writes THE_FRONTIER.md: the one board Daryl reads every turn.

** WHAT IT IS FOR. **  *** Ten open problems, in dependency order, each with: what it is, how many steps
to close, where it stood LAST revision, whether its runway is clear, and what must be cleared first.
** The overall and the breakdown, on one screen. ** ***

** THE ESTIMATES ARE STORED HERE AND EDITED BY HAND ** -- *** they are judgements, not measurements, and
the file records them so the CHANGE is visible turn to turn.  A step is one worked result, not one turn;
turns-per-step is the separate estimate. ***

    python3 scripts/regen_frontier.py

** WHAT IS GENERATED HERE AND WHAT IS NOT -- stated because the difference drifted for
   about two thousand revisions on every live row at once (r6473). **

  GENERATED from THE_REGISTER.md: which rows are LIVE.  Struck rows drop out correctly
  and always have.

  ** NOT GENERATED: the per-row title, counts, and RUNWAY PROSE.  Those are the EST
  table below -- editorial digests of register rows that run to tens of thousands of
  characters, which cannot be mechanically derived. **  Nothing updated them when a row
  moved, and the result read as a generated view while being a frozen table.

  *** A document that looks generated and is not is worse than one that looks
  hand-written: nobody thinks to check it. ***  corpus/check_frontier_current.py now
  fails when a runway lags its row -- and the remedy is to WRITE THE RUNWAY FORWARD,
  never to bump a stamp.

"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(ROOT, 'THE_FRONTIER.md')

# ** id: (short name, steps-left, steps-last-revision, turns-per-step, gate, runway note) **
EST = {
    'PO-13': ('the handover datum, and what sets this arms first peak', 1, 1, 6, None,
        'r6476: THE LAST CONVENTION IS STRIPPED and the instruments own standing question is ANSWERED -- NO. '
        'ACOUSTIC_two_arm exposed LATARG at r2441 expressly to ask whether the deficit is an artefact of where the '
        'pin was put, and the question had never been run. Scanned over a factor of 3.6 in z_onset on the converged '
        'grid: l_A runs 360.6 -> 239.3, a range of 51%, while l_1 sits at 206-210, a range of 2%. THE ONE FITTED '
        'NUMBER MOVES THE DENOMINATOR AND LEAVES THE NUMERATOR. The deficit is l_1 = 206 against the skys 220.6 at '
        'EVERY onset, so the pin cannot reach the quantity it lives in -- and the trade is an IDENTITY: pinning l_A '
        'costs 6.59% on l1/lA and pinning l1/lA costs 6.59% on l_A, the same number twice. Both pinned is '
        'UNREACHABLE, not skipped: the controls scale approaches 301.4 from above, so LATARG=301.6 is below its '
        'floor. Two defects of 60s own found in the same text, both against r4549: its three conclusion paragraphs '
        'sat past CR_cosmologys own end{document} and had NEVER compiled (rehoused here; check_tex_tail now fails '
        'on it), and the receipt its message said would land next never landed -- run now, the residue is TWO '
        'FIFTHS of the original, not the quarter it reported. Earlier: r6433/r6447, the potentials half of the '
        'one-locus statement ANSWERED from this rows own named lead, size 10/9 and scale-invariant so not the cure, '
        'with l1/lA unchanged and P1/P2 moved because dg0 = 4(Theta - Psi) is a DIFFERENCE. Remaining, and it is a '
        'DIFFERENT object from the one just closed rather than the same one narrowed: an account of the MODE rather '
        'than of the scale it is reported against -- on this arm the first peak is not set by the sound horizon, '
        'and nothing about the pin explains where 206 comes from. '
),
    'PO-46': ('STRUCK r6691 -- the premise was false', 0, 0, 0, None,
        'r6685 registered this on four open-ledger rows marked NAMED-UNBUILT and P14s sentence "what is not '
        'built is the Dirac sector on it", as though the chiral members propagating Dirac sector were '
        'unbuilt. IT IS BUILT. C50 builds it and says so in its own opening: P07s open item had three pieces, '
        'two already existed, and "the owed work is one thing: put a Dirac field on the member P11 already '
        'built, and report what it does. That is what this does." The receipt is registered and runs green. '
        'AND THE MEMBER IS THE CHIRAL ONE: P11 is explicit that the polarised cut is achiral, its single '
        'polarisation pinned by the residual T^2, and that the first chiral member is its unpolarized '
        'generalization -- the member C50 puts the Dirac field on. So unpolarised and chiral name one member, '
        'and the gap registered was between two names for it. THE ERROR: NAMED-UNBUILT labels taken at face '
        'value without opening the receipts that close them, which is the failure r6659-r6683 spent its time '
        'correcting elsewhere. The four ledger rows are not wrong -- each papers prose does name the sector as '
        'unbuilt, and that is a defect in those papers rather than a gap in the corpus. '
    ),
    'PO-45': ('the colourless triple has no seat, and the reason is the dimension result', 1, 0, 3, None,
        'r6546/r6547: P14 delivers 12 of the 15 Weyl fermions of a generation and not the colourless 3, and '
        'that shortfall now states what would discharge it. The triple wanted is a doublet plus a singlet. '
        'THE DOUBLET EXISTS: the Z3-fixed axis carries a vantage at IMAGINARY height, pow = -alpha^2 giving '
        'the pair +/- i alpha by the same power-of-a-point rule that puts a hinge at sqrt3 alpha. THE SINGLET '
        'IS OBSTRUCTED, and by a coincidence of two conditions rather than an absence: a single branch '
        'requires pow = 0, which holds exactly on the throat circle and nowhere else, and the three walls lie '
        'on that circle, each antipodal to its hinge -- so being unbranched and being coloured are ONE '
        'condition here. AND THE WELDING IS FORCED RATHER THAN PLACED, which makes the shortfall the D=4 '
        'result read from the matter side: a wall is antipodal to its hinge and a graze point lies BETWEEN '
        'two, and those coincide exactly when the hinge count is ODD, hence in EVEN D. With the count at '
        'D-1, D=4 gives n=3 -- odd, welded -- so the separation lives only at odd D, which P14s own count '
        'and parity jointly exclude. WHAT WOULD DISCHARGE IT: a construction separating pow=0 from the '
        'colour index -- neither a new three nor a larger substrate, but that one separation. AND THE '
        'SEARCH SPACE IS CLOSED OF ITS SOURCES with its own reopening named: r6537 enumerated TWELVE threes '
        'across P3s geometry and P14s count, chirality and whichthree -- eight reduce to the hinge three, '
        'three to the turnaround three, and the one that is neither (the causal classes) fails because '
        'causal character is a metric invariant, so R acts as the IDENTITY, 3+0 and not the 2+1 a seat '
        'needs. Exhaustive of its sources and NOT a theorem that no other three exists: a three arising in '
        'P5s groupoid, P12s algebroid, or the charged sector would reopen it, and that is the next place '
        'to look. '
        'r6555 WALKS THAT REOPENING AND THE CLOSURE HOLDS, WIDER. All three places searched, and they '
        'yield two more genuinely third threes and no seat. P5s THREE DISCRETE OPERATIONS -- sigma (no '
        'seam-crossing), R (the back seam at r=0), xi (the throat seam at r=alpha) -- are three distinct '
        'maps at three distinct loci, so genuinely third; they fail because R DOES NOT ACT on the set at '
        'all: sigma and R generate D_6 so conjugation carries sigma outside it (their product has order '
        'six, so they do not commute), and xi is a PARTIAL involution outside the group. P12s {6,7,10} -- '
        'the symmetric-pair isotropy dimensions of so(5,1) -- is genuinely third and fails because THE '
        'THIRD MEMBER IS ABSENT: 10 = so(4,1) (Type O) and 6 = so(2,1)+so(3) (Nariai) are realised, 7 by '
        'nothing, so it is 2 + nothing rather than 2+1. The charged sectors threes are the cubics roots, '
        'already reduced. AND THE FOUR CANDIDATES FOUND FOUR DISTINCT WAYS TO FAIL A SEAT: R acts and acts '
        'TRIVIALLY (causal classes); the three splits 2+1 but SHARES THE HINGE, so it has fermion content '
        'or colour-freedom and never both (the reassignment three); R does not act at all (the '
        'operations); the third object does not exist ({6,7,10}). Exhaustive of FIVE papers now and still '
        'not a theorem, and the demand on a successor is unchanged: introduce structure, do not re-read '
        'what is present. '
        'r6561 OPENS A DIFFERENT DOOR -- the worldline description, and [6*] gains a stake. The r1000 '
        'figures resurrected with the infrastructure they lacked: THE LIFT SITS ON THE WALL RAYS. Face 2 '
        '(tau~ real) is on the hinges at 0,120,240; face 4 (the lift, tau~ imaginary) is on the walls at '
        '60,180,300 -- and the walls are the graze points, P14s colour index. Real time on the hinges, '
        'imaginary time on colour. And Im tau~ is THREE-FOLD PERIODIC BY CONSTRUCTION: sinh^2 is '
        'invariant mod i pi and tau~ = (2a/3)w, so the period is 2 pi alpha / 3 and exactly THREE sectors '
        'fill the horizons thermal circle beta = 2 pi alpha. The ceiling pi/3 on the lift is HALF the '
        'period -- the sectors midpoints, which is the walls own arrangement. AND [6*] IS POSED AS A '
        'DISJUNCTION WHILE ITS OWN DIAGNOSIS DENIES ONE: r1080 states the two readings are about MOTION '
        'ALONG A BEAD versus WHERE A POINT SITS -- those are not the same thing -- then asks which is the '
        'objects. Two answers to two questions do not compete. And they do different work: R as MOTION '
        'permutes the three sectors {0->2, 1->1, 2->0}, a 2+1; R as POSITION maps between sides and '
        'permutes nothing. So which reading governs decides whether a candidate seat exists at all. HELD '
        'AT WEIGHT: a reframing, not a settlement -- not that the readings are complementary, NOT that '
        'the sectors are genuinely third (the lift on the wall rays makes reduction to the wall three '
        'the thing to test), and nothing about leptons. '
        'r6563 DECIDES THAT TENSION: THE SECTORS ARE GENUINELY THIRD. Neither triple maps onto the '
        'other -- a 120 deg rotation of r leaves r^3 and hence tau~ fixed, and a sector shift is '
        'w -> w + i pi, which flips sinh w and leaves sinh^2 w, hence r ITSELF, unchanged -- so the map '
        'collapses each triple to a single point of the others space, which is exactly how eight of '
        'r6537s twelve died and does not happen here. And the shared 120 deg is EXPLAINED: both '
        'three-foldnesses come from ONE exponent, the cube in r^3 and the same 3 in w = 3 tau~/2a '
        'dividing sinh^2s i pi period down to 2 pi a/3. One source, two independent threes. And on the '
        'lift there are EXACTLY TWO R-invariant fibres, bases 0 and pi/3, landing on the hinge and wall '
        'angles in imaginary time, and EACH IS A 2+1. The first candidate in this search to pass BOTH of '
        'r6537s tests. CONTINGENT ON [6*] and that is the whole of its status: under the POSITION '
        'reading R maps between sides and permutes no fibre, so no 2+1 and no seat. Still unshown: that '
        'the fibres three elements ARE the colourless fermions, that the 2+1 is doublet-plus-singlet, '
        'anything about masses. A structure of the right shape in the right place is not an '
        'identification. '
        'r6565 CHARACTERISES THE LIFTS INTERIOR AND CORRECTS r6563s FRAMING. The frame exchange is ONE '
        'rule: with u = (r/A)^(3/2), r -> -r IS u -> i u EVERYWHERE, verified on both sides of |r| = A '
        'against the original figures own wing, real part included. The map does not change at the '
        'binding radius -- arcsinh does. AND THE BINDING RADIUS IS A BRANCH POINT OF THE TIME MAP: '
        'arcsinh branches at +-i, so arcsinh(i u) branches at u = +-1, exactly |r| = A, which is '
        '2^(1/3) R_TA,max -- P3s largest shell that stays gravitationally bound. The bound/unbound '
        'boundary and the branch point of the time map are one radius. And the two R-invariant fibres '
        'are THE LIFTS TWO ENDS: hinges {0,120,240} at the branch point, walls {60,180,300} at the '
        'binding radius, every fibre strictly between failing invariance. AND r6563 OVERSTATED THE '
        'CONTINGENCY: it called the 2+1 contingent on [6*], conflating a MAP question (which involutions '
        'act -- computable, needing no labelling) with a LABELLING question (whether species is sign(r) '
        'or the quadrant sign, which is what [6*] actually asks and is open). The 2+1 is a fact about an '
        'involution and does not wait on [6*]; what waits on it is whether that 2+1 means anything about '
        'matter and antimatter. And P7s caption is what makes r -> -r a map at all: the two R-conjugate '
        'frames read each matter on its OWN r>0 side, so r is frame-relative. NOT CLAIMED: that a branch '
        'point IS a binding mechanism -- the two coincide in RADIUS, and coincidence of radius is what '
        'is shown. '
        'r6571 CORRECTS THIS ROWS CONDITIONALITY: IT WAS ON A QUESTION ALREADY RESOLVED. r6561-r6569 held '
        'the lift result as contingent on [6*]. [6*] was resolved by A3_factorization, worked on the full '
        'C_r x C_tau~ -- the very object r1080 said would be needed -- registered, green, reporting '
        '[6] RESOLVED, bounded. It establishes C = (Q -> -Q)_field o (R o K)_geometric, with R o K '
        'reproducing Cs action on species, |mass|, mass-sign and the Feynman-Stuckelberg wing structure '
        'while blind to the charge sign, both factors depending on Q only through Q^2. And P13 says it in '
        'published prose: a species = sign r reading is NOT vindicated, since sign r has no meaning off '
        'the real axis. AND BOTH READINGS THIS LINE ELIMINATED BY HAND WERE MISSTATEMENTS OF THE CORPUS '
        'MAPS: its R is (r, tau~; 2M, Q) -> (-r, tau~; -2M, Q), flipping 2M and holding tau~ FIXED, and '
        'its K is tau~ -> conj(tau~), not tau~ -> -tau~. One thing survives and it is the useful part: on '
        'the lift Re tau~ = 0, so conj(tau~) = -tau~ exactly, and the involution r6566 measured is K '
        'RESTRICTED TO THE LIFT -- the corpus own antilinear Feynman-Stuckelberg face rather than a '
        'conjectured rule. The 2+1 is graded by the right operator, by a route that did not know it. '
        'WHAT REMAINS OPEN IS NOT [6*] BUT A3s OWN DO-NOT-ASSERT: that R o K acts on P14s actual fermion '
        'zero-modes as Cs kinematic conjugation. That is exactly the identification the lift result would '
        'need, and P13 scopes it the same way -- the kinematic face is confirmed on the zero-modes for R '
        'carrying each generation to its bound antimatter partner ON THE REVERSED WALL, which is not the '
        'lift. The mode count stands as a mode count; calling it a species grading is the thing the '
        'corpus says not to assert. '
        'r6591-r6601 SEPARATE THE COORDINATES AND SETTLE TWO THINGS. 2M = (2/3sqrt3) sin 3w depends on '
        'the CUT alone; r^3 = 2M alpha^2 sinh^2(tilde-w) on the cut AND the bead phase -- so w (which '
        'cut) and tilde-w (when) are INDEPENDENT COORDINATES. Every cut-side operation fixes the bead '
        'phase: sigma, R, xi, and the horn swap, which P14 calls a substrate isometry in the '
        'order-twelve group D_6 = <sigma,R>. widetilde-T alone moves it, so IT IS A FOURTH DISCRETE '
        'OPERATION, and it commutes with the cut-side ones. AND THE LIFTS THREE ARE COLOURLESS BY '
        'INDEXING: the colour grading is sigma (P03_winding_and_closure records sigma->colour), which '
        'moves w; the twelves colour index is the graze point, a w-index; the lifts three are indexed '
        'by the Im tilde-tau sectors, whose period 2 pi alpha/3 carries no M- and no w-dependence, so '
        'sigma acts trivially and they sit in the trivial rep of the colour grading. The same fact that '
        'makes widetilde-T a fourth operation makes its eigenvectors colour-neutral. NOT CLAIMED: that '
        'the three are leptons -- colourless is one clause of one requirement, the weak-isospin and '
        'chirality assignments untouched; not that the 2+1 is doublet-plus-singlet; nothing about '
        'masses. And colour-neutrality was never in doubt -- what is added is the REASON. '
        'r6602/r6605 RUN THE ISOSPIN CLAUSE AND THE LIFT FAILS IT. The three lift modes occupy ONE '
        '(T,R) character, (t,+1), where the wall sector occupies FOUR. The pair matching the left-handed '
        'doublet is {+1,-1} within one R-eigenspace, and the lifts single R-eigenspace carries {t,t,t} -- '
        'so the lift fails to reproduce the one thing the wall sector got right. The mechanism is TWO '
        'INDEPENDENT COLLAPSES: T commutes with R so it is a scalar on a one-dimensional R-eigenspace; T '
        'fixes the bead phase where the deck moves it so it is diagonal; and a diagonal operator commuting '
        'with a transitive Z_3 has EQUAL entries, one common scalar. R alone caps the reachable characters '
        'at two however T is assigned, and Ts scalar-ness removes the second. AND THE RIGHT-HANDED '
        'MISMATCH P14 RECORDS DOES NOT APPEAR, BY ABSENCE RATHER THAN REPAIR: the lift has no R-odd '
        'content, so the comparison cannot be made there. The two loci differ and the difference cuts '
        'against the lift -- the wall REACHES the right-handed structure and gets one pair wrong, the lift '
        'does not reach it. NOT ESTABLISHED: t itself (one common scalar, not which -- exactly P14s '
        'situation at a single wall), and none of the three answers rests on it. The comparison is '
        'ASYMMETRIC, sector occupation against locus mode space, stated not elided. The chirality clause '
        'is untouched: in the gamma^5 grading the lift is 3+0, as the wall is. The seat stays '
        'unidentified. '
        'r6566 RUNS THE DECIDING COMPUTATION -- THE LIFT FIBRES MODE CONTENT, NOT ITS FIBRE '
        'PERMUTATION. The lift fibre binds THREE normalizable modes, one per sector, all on the '
        'sigma_y = +1 branch, and under the involution that acts there they split dim ker_+ = 2, '
        'dim ker_- = 1 -- the 2+1 S3 asks for, at the locus where the wall gave 3+0. AND THE '
        'DIFFERENCE FROM THE WALL IS ONE FACT: at the wall R is antipodal WITHIN each wall, so it '
        'fixes every seat and is +1 times the identity on the mode space; on the lift it MOVES '
        'them, a transposition inside the seat symmetry rather than a central factor beside it. '
        'The deck Z3 is transitive in BOTH cases, so transitivity is not what separates them. T1 '
        'is honoured by construction rather than by assertion, which is the whole of why this is '
        'not r6563 restated: the mode space is computed FIRST -- the normalizability cut run ON '
        'the lift, with an engine calibrated to return the walls 3+0 -- and R is then built BY '
        'PROJECTION onto it and diagonalised, so the 2+1 is an eigenvalue multiplicity and not a '
        'permutations cycle type. AND THE LIFTS GEOMETRY IS DERIVED, RETURNING WHAT THE CORPUS '
        'ALREADY CARRIES: integrating the leaf measure along the bead relation gives ell(theta) = '
        '(2 alpha/3) sin(3 theta/2), which vanishes at the hinge angles {0,120,240} and is '
        'extremal at the wall angles {60,180,300} -- r6565s two invariant fibres -- whose fold is '
        'r6565s monodromy, and whose half-loop at a hinge sends r -> omega r, which is '
        'sec:chiralitys own omega^lambda wall monodromy recovered from the lift. T3 is answered by '
        'MEASUREMENT: the measure is derived, d ell = alpha cos(3 theta/2) d theta, flat in '
        'imaginary time at the hinge with alpha x 2pi = beta and DEGENERATE at the binding radius, '
        'and the cut it gives is the walls and is the same in BOTH candidate measures, so the '
        'number does not turn on that choice. T5: the binding radius is the domains edge AND a '
        'branch point and obstructs NEITHER branch, so the selection is made at the hinges and the '
        'count does not depend on the branch taken at |r| = A. AND [6*]S TWO READINGS ARE NOT TWO '
        'INTERPRETATIONS OF ONE MAP -- THEY ARE A MAP AND ITS SQUARE: on the lift (r -> -r)^2 = '
        '(tau~ -> -tau~), verified pointwise, and r -> -r does not act within the lift at all, the '
        'lift being the r <= 0 wing entire, so the frame exchange swaps it with the Lorentzian '
        'wing. Under the position reading there is no involution to grade by, which is a worse '
        'answer for that reading than disagreement would be. AND IT SHARPENS '
        'P14_S3_against_the_wall_contents PART 3, and P14 sec:whichthree with it: that receipt '
        'forbids a 2+1 by transitivity plus Rs centrality, but a CENTRAL R acting -1 on the '
        'standard representation gives 1+2 on a transitive triple, constructed and diagonalised, '
        'so the stated reason does not by itself forbid it -- what forbids it at the wall is that '
        'R FIXES EACH SEAT. The conclusion stands; the reason is corrected. NOT ESTABLISHED, at '
        'the same weight: the number DEPENDS ON [6*], which is open; and the three sector modes '
        'are counted independent, which is sec:counts own reading, while under the CONTINUATION '
        'reading the space is one-dimensional and graded only at lambda = 0 mod 3, giving 1+0 -- '
        'so the reading that would remove the 2+1 does not replace it with a 3+0 either. Not that '
        'the fibres elements ARE the colourless fermions, not that the split is '
        'doublet-plus-singlet, nothing about masses, and S3 is a requirement P14R21 NAMES rather '
        'than a sufficient one. '
        'r6574 SETTLES THE OPERATOR IDENTIFICATION AND IT COMES OUT THE OTHER WAY: THE LIFTS '
        '2+1 IS NOT GRADED BY THE CORPUSS CONJUGATION. A3_factorization marks exactly one '
        'thing DO-NOT-ASSERT, that R o K acts on P14s actual fermion zero-modes as Cs '
        'kinematic conjugation; the wall half is discharged by P14_P14_payoff and the lifts '
        'was not, because r6566 built its involution BY PROJECTION. Built instead from the '
        'Clifford data, gamma^5 o K ANTIcommutes with gamma^5, so it FLIPS CHIRALITY -- and '
        'the lifts three modes are all sigma_y = +1 while R sends 2M -> -2M, so it carries '
        'every one of them OFF the mode space and onto the CONJUGATE geometry. It is not an '
        'endomorphism there, has no eigenvalues there, and is NOT the involution r6566 '
        'measured. AND THIS IS NOT A DEFECT OF THE LIFT -- IT IS WHAT CONJUGATION DOES: '
        'P14_P14_payoff records the same at the wall, R carrying the bound mode to a bound '
        'mode of OPPOSITE chirality. AND WHAT r6566 MEASURED CAN NOW BE NAMED, WHICH ANSWERS '
        'r6569S NARROWING that a defence must say what grades species on the lift: it is T, '
        'tau~ -> -tau~ with r and 2M FIXED, a symmetry of the bead relation in its own right '
        'since sinh^2 is even -- neither R, which flips the mass, nor K, which flips the '
        'chirality. T flips neither. W1 AND IT IS THE WHOLE REASON THE TWO LOOKED ALIKE: on '
        'the lift Re tau~ = 0, so conj(tau~) = -tau~ THERE AND NOWHERE ELSE; on the '
        'Lorentzian wing tau~ is real and the two differ by a sign. And there is no grading '
        'to recover: (gamma^5 o K)^2 = -1, antilinear with square -1, no eigenvectors '
        'anywhere including the doubled matter-plus-antimatter space. THE CALIBRATION IS '
        'WHAT SEPARATES THIS FROM THE OTHER ANSWER: A3 names two objects both called C, and '
        'the C-matrix proper i g2 g0 COMMUTES with gamma^5 where the operator in psi -> '
        'psi^c ANTIcommutes, so a construction using the wrong one reports chirality '
        'preserved and the identification appears to go through. A3 warned that trap yields '
        'a false refutation; here it yields a false CONFIRMATION, the more expensive '
        'direction. AND THE CORPUS CARRIES R IN TWO SENSES, which is why the confusion was '
        'available: sec:counts antipodal map within one geometry with the mass fixed, and '
        'sec:cosmogenesiss r_0 -> -r_0 with 2M -> -2M. Both verbatim and they are different '
        'maps, so r6566 compared two candidate readings of which NEITHER was A3s. W4 ASKED '
        'AND ANSWERED, AND THE ANSWER REMOVES THE DIFFERENCE: R fixes a point only if r = -r '
        'AND 2M = -2M, i.e. only at r = 0 AND M = 0, so NO locus of a fixed-mass geometry is '
        'R-fixed -- the lifts two invariant fibres are invariant under T, not under R. NOT '
        'ESTABLISHED: that r6566s 2+1 is wrong, its eigenvalues being reproduced unchanged '
        'with only the operators name corrected; and not that S3 is unmet, the lifts content '
        'still being a single sigma_y eigenspace. Nothing about the charge sign (W3, '
        'controlled: the construction is Q-blind and a geometric charge sign would be a bug), '
        'nothing about masses, no identification of the fibres elements with the colourless '
        'fermions. WHAT WOULD DISCHARGE THE ROW NOW IS NO LONGER [6*], which r6571 found '
        'resolved and r6574 shows was posed over two maps neither of which was A3s. What the '
        'seat still lacks is a reason the beads TIME REVERSAL should grade a matter '
        'multiplet: the split is real, its map is named, and what it means is not. '
        'r6602 RUNS THE WEAK-ISOSPIN CLAUSE AND IT SEPARATES THE TWO LOCI AGAINST THE '
        'LIFT. r6601 settled colour as trivial by indexing; this is the (T,R) occupation. '
        'ONE: the lifts three modes occupy EXACTLY ONE of the four (T,R) characters, '
        '(t,+1), where the wall sector occupies all four. TWO: and they do NOT carry the '
        '{+1,-1} pair that matches the left-handed doublet, for EITHER value of t -- that '
        'pair is two T-values on ONE R-eigenspace, and the lifts single R-eigenspace '
        'carries {t,t,t}, one value three times, so the lift fails to reproduce the one '
        'thing the wall sector got right. THREE: and P14s right-handed mismatch does not '
        'appear there either, by ABSENCE rather than repair -- the lift has no R-odd '
        'content for the comparison to be about, where the wall reaches that structure and '
        'differs from the Standard Model by exactly one pair. The two loci differ on this '
        'and the difference cuts against the lift. THE MECHANISM, every link computed '
        'rather than read off an index: T commutes with R, so on the one-dimensional '
        'R-eigenspace each mode spans it acts by a SCALAR; it FIXES the bead phase where '
        'the deck MOVES it (r6591), so it is DIAGONAL in the sector basis; and a diagonal '
        'operator commuting with a TRANSITIVE Z_3 has all three entries equal. So T = t.I '
        'on the whole three-dimensional mode space -- the four characters need BOTH '
        'R-values and the lifts three lie in a single one. AND THE CALIBRATION IS THE '
        'ERROR THE ORDER EXISTS TO PREVENT, RUN AS A TEST: the naive reading, T fixes the '
        'index so T acts trivially so one character, RETURNS ONE CHARACTER ON THE WALL '
        'WHERE P14 PUBLISHES FOUR, so a construction using it is not measuring occupation '
        'at all. And the mechanism is visible in P14s own factorisation: the twelve factor '
        '3 x 2 x 2 as graze point x horn x ruling, and T IS the horn swap, so it fixes the '
        'graze-point index and moves the horn factor. Occupation lives in the factor, not '
        'in the index -- P14R55s locus-versus-mode distinction one level over. NOT '
        'ESTABLISHED: t itself is not determined, the construction fixing that T is one '
        'common scalar and not which, exactly as P14 finds at a single wall where the '
        'distinction has no content -- and none of the three answers rests on it. The '
        'comparison is asymmetric, P14s four being a SECTOR occupation and the lifts three '
        'a LOCUS mode space, which is stated rather than elided. The chirality clause of '
        'S3 is untouched: in the gamma^5 grading the lift is 3+0, exactly as the wall is, '
        'r6566s 2+1 being widetilde-Ts, and whether one sigma_y eigenspace could carry a '
        '2-left-1-right split by some other reading is a separate question nobody has '
        'asked. And nothing here says the three lift modes ARE the colourless fermions. '
        'WHERE THE ROW STANDS: three clauses run on the lift -- colour trivial, isospin a '
        'single character that misses the doublet, chirality 3+0 and untouched. The seats '
        'shape was right and its gradings are not, and what remains open is the chirality '
        'clause and whether any locus carries the doublets two T-values at all. '
        'r6686 ANSWERS THAT, AND THE ANSWER IS NO -- AS ONE FACT RATHER THAN FIVE '
        'SEPARATE FAILURES. r6602s mechanism named three escapes: an R-eigenspace of '
        'dimension greater than one, a deck not transitive on the modes, or T not '
        'commuting with R. Running P07s causal stratification -- five spans and four '
        'joints -- against all three: EVERY TWO-VALUED DATUM THE STRATIFICATION OFFERS IS '
        'THE SAME INVOLUTION, the exchange of the beads two ends, AND THAT INVOLUTION IS '
        'R. The horn label sign(X_0), T being the horn swap; the leg label sign(r), matter '
        'against antimatter; and the rates sign, collapse against expansion -- three names '
        'for one exchange. So the two values are split ACROSS the R-eigenspaces and never '
        'within one: the datum is not merely absent, it IS R, and R cannot split its own '
        'eigenspace. Q1, THE HORN SPANS ESCAPE THE LIFTS COLLAPSE AND STILL FAIL, '
        'DIFFERENTLY: T does not act WITHIN either horn span, it exchanges them, so on a '
        'single span it is not an endomorphism and grades nothing, while on the PAIR it is '
        'a transposition and TWO characters are occupied against the lifts one -- but they '
        'are (+1,+1) and (-1,-1), a CORRELATED pair and not a doublet, R being the same '
        'transposition there so each R-eigenspace on the pair is one-dimensional. Q2, '
        'THREE OF THE FOUR JOINTS SELECT NO BRANCH: at both seams f = 0 and the measures '
        'inverse square root is integrable with psi finite, and at the turnaround f = 1 '
        'and the measure is regular, so the selection is the branch points alone -- and '
        'the FRONT SEAM, P07s one joint that changes no character, carries no selection '
        'either, what persists across it being ONE branch, one value and not two. Q3, AND '
        'THE RATES SIGN FAILS FOR THE OPPOSITE REASON TO T ON THE LIFT: (dr/dtau~)^2 = '
        '1 - f and f is R-EVEN, so the rates SQUARE is even while the RATE IS R-ODD, '
        'verified symbolically with the defect under the bare backward reflection being '
        'exactly twice P07s own R-odd part -2M/r. An R-odd grading ANTIcommutes with R: it '
        'carries the R=+1 eigenspace to the R=-1 one, so it is not an endomorphism of '
        'either and cannot grade one at all. T on the lift COLLAPSED to a scalar; the '
        'rates sign does not collapse, it does not PRESERVE the eigenspaces it would have '
        'to split. AND THE DIMENSION COUNT SAYS WHY THE WALL SECTOR IS THE ONLY PLACE IT '
        'WORKS: two T-values within one R-eigenspace needs that eigenspace to have '
        'dimension at least two, hence at least FOUR states, and the stratifications '
        'two-valued data are all TWO-STATE exchanges, so every R-eigenspace they produce '
        'is one-dimensional -- P14s colourless four being the only object in the '
        'construction with a two-dimensional one. NOT ESTABLISHED: that {0,1,2} is a three '
        'of the kind the other two are -- L8_the_pencil is explicit that the pencil runs '
        'over ALL f and does not select them, and that verdict stands unchanged; not that '
        'the rates sign is isospin or anything else, only that it is R-odd; Ts scalar on a '
        'one-dimensional R-eigenspace is still undetermined as r6602 left it, and no '
        'answer rests on it. WHERE THE ROW STANDS, AND IT IS TWO STATEMENTS RATHER THAN '
        'FOUR CLAUSES (r6689): COLOUR PASSES, and on the other coordinate entirely -- the three '
        'lift modes are indexed by the Im tau~ sectors, whose period 2 pi alpha/3 carries no M- '
        'and no w-dependence, so the colour grading sigma acts trivially on them. ISOSPIN AND '
        'CHIRALITY BOTH FAIL, AND BY ONE FACT: the three lie in a SINGLE R-eigenspace. That one '
        'fact gives both -- a one-dimensional R-eigenspace admits only a scalar, which is r6602s '
        'first collapse; and since R = gamma^5, the gamma^5 grading is 3+0 BY THAT SAME FACT '
        'rather than as a separate measurement. The row previously carried chirality as '
        'untouched; it is measured at r6605 and it is not independent. AND r6686 GENERALISES THE '
        'ONE FACT: every two-valued datum the stratification offers is one involution and that '
        'involution IS R. THE DEMAND, AS THE ROW HAS ALWAYS STATED IT: a DOUBLET PLUS A SINGLET, '
        'colour-neutral -- two left-handed states with two T-values in one R-eigenspace and one '
        'right-handed state in the other, a 2+1 across R. IT IS NOT A THREE-FOLD SYMMETRIC OBJECT: '
        'a doublet and a singlet of opposite chirality cannot be a Z_3 orbit, and r6693-r6697 '
        'asked whether candidates carry a Z_3 three, which is what set C50s member aside. WHAT '
        'SURVIVES: binding leaves every state it keeps in ONE R-eigenspace (r6698s unpaired '
        'level), so a bound sector gives 3+0 and cannot host a 2+1 -- THE COLOURLESS TRIPLE DOES '
        'NOT COME FROM A BOUND SECTOR. Two T-values inside one '
        'R-eigenspace needs four states, and every two-valued datum here is a two-state '
        'exchange; P14s colourless four is the only object in the construction with a '
        'two-dimensional R-eigenspace. WHERE THAT POINTS: PO-46, the chiral members propagating '
        'Dirac sector, is the one place the corpus says structure is MISSING rather than '
        'measured-and-absent, and it is the member carrying the matter content. '
        'r6696 RUNS THE HEXAD READ HINGE-RELATIVELY AGAINST EXACTLY THAT DEMAND -- find a '
        'locus whose modes span both R-eigenvalues -- AND THE SHAPE IS REAL WHILE THE '
        'CONJUNCTION IS STILL NOT MET, for two reasons with the second larger. The '
        'structure verifies: the six Nariai marks sit at sky angles 30/150/270 with '
        '2M > 0 and 90/210/330 with 2M < 0, each hinges neighbours at +-30 are one from '
        'each triple, so three hinges each carry an R-conjugate pair, 3 x 2 = 6, and '
        'dim R_+ = dim R_- = 3. THE LIFTS FIRST COLLAPSE IS GENUINELY KILLED. ONE: A '
        'THIRD COLLAPSE, IN TWO COMMUTATIONS. T is diagonal on the marks, fixing the sky '
        'angle; WITHIN a triple the hinge Z_3 is transitive, forcing one entry per block, '
        'and ACROSS the blocks T commutes with R -- which P14 establishes outright -- '
        'forcing t_+ = t_-. ONE T-value across the whole hexad, the characters being '
        '(t,+1) and (t,-1): two characters with one T-value each, so no R-eigenspace '
        'carries two. The lift died of dimension and of the deck; the hexad dies of the '
        'one commutation P14 states outright. TWO, AND THE LARGER REASON: NOTHING BINDS '
        'THE HEXAD BECAUSE IT IS NOT A MODE SPACE. The six are MARKS in the cut parameter '
        'space -- which Nariai member at which sky angle -- and not solutions on a leaf, '
        'so no normalizability question arises and there is no branch to reject. It has '
        'both R-eigenvalues for exactly the reason C50s member does, nothing binding it, '
        'so it does NOT defeat r6695s trade: it sits on the PROPAGATING side of it, with '
        'a three that is a three of MARKS. So it meets the demands wording on spanning '
        'both R-eigenvalues while failing it on MODES, which is the member-versus-locus '
        'distinction at the top level. Q3 IS ANSWERED IN THE SHARPEST WAY AVAILABLE: the '
        'hinge-relative +-30 label and sign(2M) are compared mark by mark and are '
        'IDENTICAL ON ALL SIX, since 2M = (2/3 sqrt3) sin 3w and 3(w_h +- 30) is +-90 '
        'modulo 360 at every hinge -- so it is not a datum independent of R that r6686 '
        'merely failed to reach, it is Rs own label hinge-relatively named. Q1: NEITHER '
        'widetilde-T NOR T IS OFF-DIAGONAL. widetilde-T fixes r and the MASS by '
        'definition and the two triples ARE the 2M-sign blocks, so it is block-diagonal '
        'for the same reason the blocks exist; T is diagonal too, fixing the sky angle. '
        'And the DECK is not in play at all -- it moves the bead phase where the hexad is '
        'indexed by the sky angle, so the transitive Z_3 acting here is the HINGE three. '
        'NOT ESTABLISHED: that the hexads structure is wrong or uninteresting -- the '
        '3 + 3bar with dim R_+- = 3 is exactly the shape the first conjunct asks for and '
        'the only object computed here supplying it; not that a parameter-space three '
        'could never be a mode three, what is shown being that THIS one is not; t itself '
        'is undetermined as r6602 left it and no answer rests on it. W4, PLAINLY: the '
        'largest discrete structure the construction carries supplies the demands FIRST '
        'conjunct and fails the second, and the failure is not narrow -- the two-valued '
        'label it would use is Rs own, and the object it would use is a parameter space '
        'rather than a mode space. '
        'r6698 WORKS THE LAST LEG -- CAN A PROPAGATING MODE SPACE CARRY A THREE -- AND THE '
        'SURVEYS PREMISE FAILS FIRST. C50s member is NOT the only propagating sector this '
        'construction builds. sec:cosmogenesis builds a second, with a receipt of its own: '
        'under the signature flip the three bound wall-modes continue past the horizon into '
        'THREE FAMILIES PROPAGATING IN COSMIC TIME -- a propagating mode space that DOES '
        'carry a three, and a three of MODES rather than of marks. IT FAILS THE CONJUNCTION '
        'BECAUSE IT INHERITED BOTH HALVES: the continuation is a term-for-term bijection '
        'COMMUTING WITH gamma^5 -- computed on the corpuss own undercritical model, where W '
        'is real between the horizons and imaginary past one and both branches stay two and '
        'stay opposite -- so the map that carries the three across carries the single '
        'R-eigenvalue with it. Propagation acquired after binding transports what the '
        'binding settled; it does not re-decide it. AND THE SETTLING IS ONE EVENT RATHER '
        'THAN TWO, WHICH IS THE MECHANISM Q3 ASKS FOR. The wall operator is first order and '
        'its two branches are the two R-eigenspaces; written A = d/dl + W, the partner map '
        'A-dagger carries EVERY free eigenfunction to an eigenfunction of the wall problem '
        'AT THE SAME ENERGY -- residual exactly zero, symbolically -- and those states are '
        'REFLECTIONLESS, |T|^2 = 1 with no reflected component at all. A wall that binds one '
        'mode transmits everything else perfectly. So the pairing fails at E = 0 and nowhere '
        'else, and E = 0 is the bound level: LOCALISATION, WHICH A THREE REQUIRES, AND THE '
        'COLLAPSE TO ONE R-EIGENVALUE ARE THE SAME UNPAIRED LEVEL. Q2: the deck indexes no '
        'propagating mode space on either reading. As a PHASE it is a translation by an '
        'IMAGINARY amount, multiplying e^{-i omega tau~} by e^{2 pi omega alpha/3}, a '
        'positive real for real omega, so it generates an INFINITE group -- its order is '
        'three exactly on omega = i n / alpha, the Matsubara tower, which is periodicity in '
        'imaginary time. As a PERMUTATION it needs the three sectors decoupled, and that is '
        'sec:counts lambda < 3/4 rejection read as a condition on the hinges. ONE INEQUALITY '
        'DECIDES BOTH CONJUNCTS, IN OPPOSITE SENSES. W4, PLAINLY -- AND THE OBSTRUCTION IS '
        'AN ANTICOMMUTATION: the first-order operators boundary form, the only object that '
        'could couple the sectors, is carried by the off-diagonal Clifford element and '
        'anticommutes with R = gamma^5, so its matrix elements between states of one '
        'R-eigenvalue vanish identically. A mode space inside one eigenspace has nothing '
        'with which to couple its sectors, and a coupled one is not inside one eigenspace. '
        'CALIBRATED ON THREE TRAPS, the third the one this object invites: a space taken '
        'together with its own R-partner spans both R-eigenvalues by construction, a '
        'tautology built here so the corpuss explicit antimatter families are not mistaken '
        'for a finding. NOT ESTABLISHED: that no propagating sector could ever carry a three '
        '-- one does; what is shown is that the two routes to propagation, NATIVE and '
        'INHERITED, fail different conjuncts. Not that the families are the colourless '
        'triple: they are the continued WALL three, the chiral seats, carrying the '
        'colour index -- and not the generations either, which sec:whichthree seats on '
        'the deck. Nothing named, nothing seated, chirality and L8s verdict untouched. '
        'r6702 PUTS THE DEMAND AS A DOUBLET, WHICH IS WHAT THE ROW HAS ALWAYS SAID, AND '
        'ASKS C50s MEMBER THE ONE THING IT HAD NOT BEEN ASKED. IT GETS FURTHER THAN '
        'ANYTHING ELSE HERE BEFORE IT FAILS. Q1: T IS NOT CARRIED THERE AT ALL -- P14s T '
        'acts on the twelves HORN factor, and a Gowdy-de Sitter member has no embedding '
        'X_0, no vantage and no horn pair. What it could carry instead is the spinorial '
        'time reflection, and EVERY reflection of an ODD number of directions '
        'anticommutes with gamma^5 -- enumerated over all sixteen sign patterns with '
        'each implementer verified against its own conjugation rule -- so a time '
        'reflection EXCHANGES the chirality blocks rather than grading one. The '
        'background refuses it independently: psi_t = sqrt(Lambda/3) e^psi admits no '
        'Lambda > 0 at which psi_t = -psi_t, so the obstruction is the cosmological '
        'constant itself. Q2: THERE IS NO (T, CHIRALITY) CHARACTER TABLE AT ALL, the two '
        'labels not commuting -- the lift collapsed to ONE of four characters, and this '
        'member fails earlier, on simultaneous diagonalisability. AND IT HAS THE SPLIT, '
        'WHICH NOTHING ELSE IN THIS LINE SUPPLIES: the 4D operator is massless so '
        'gamma^5 decouples it at every momentum, Sigma = gamma^0 gamma^1 commutes with a '
        'block EXACTLY when the transverse momenta vanish (the commutator is carried by '
        'm_x and m_y alone, measured), the commutant inside a block is spanned by 1 and '
        'Sigma and nothing else, and BOTH Sigma-values are occupied -- the two '
        'dispersion branches. Q3: WHAT IT HAS NOT GOT IS THE PAIRING. At one energy the '
        'two sit at DIFFERENT MOMENTA, k = E + b and k = b - E, so a pairing is not a '
        'matrix but a matrix and a reflection. Of the sixteen, exactly four preserve '
        'chirality and flip Sigma: tx, ty, zx, zy. Only zx and zy also preserve the '
        'ENERGY -- tx and ty reflect t, so they send E -> -E, the frequency wing, which '
        'this corpus assigns to conjugation and not to isospin. AND zx AND zy BOTH SEND '
        'c -> -c. So THE ONLY OPERATIONS THAT COULD PAIR TWO STATES OF ONE CHIRALITY AT '
        'ONE ENERGY ARE EXACTLY THE ONES THAT FLIP THE TWIST -- and the twist is what '
        'makes the member chiral, P11 stating outright that c = 0 is the polarised, '
        'ACHIRAL cut. The member can be chiral or doublet-paired and not both: its '
        'chirality and its pairing are carried by one field. CALIBRATED ON BOTH LEGS '
        'BEFORE USE -- a known YES (the walls four characters), a known NO (r6696s '
        'both-R-one-T trap) and a second NO where the split is present but the pairing '
        'leaves the block, which is the leg this member turns on. W5, PLAINLY: r6698 put '
        'the colourless triple out of every BOUND sector by the pairings single unpaired '
        'level, and this puts it out of the one NATIVE PROPAGATING sector by the twist. '
        'Where it is not is now stated twice over, on two different mechanisms. NOT '
        'ESTABLISHED: that Sigma is weak isospin or that the split is a doublet under '
        'some other reading -- two values in one chirality is the SHAPE and it is the '
        'pairing that fails; nothing is named. Not that no propagating sector could '
        'carry a doublet: THIS one cannot, for a stated reason. Nothing about the c = 0 '
        'member, where the pairing exists and the chirality does not. '
        'r6704 MOVES THE QUESTION TO THE COMPACT FACE, where the corpus puts continuous '
        'curved algebras, and the branching is FORCED while the matter is absent. Q1: '
        'that face is the round S^5s isometry algebra so(6) -- P06 C7 -- which is the '
        'COMPACT real form, and so(6) = su(4), exhibited rather than named: the six '
        'weights of the antisymmetric square of the 4 fall into THREE +- PAIRS, which is '
        'the so(6) vectors own weight shape. Q2: THE EMBEDDING IS FORCED -- su(3) has no '
        'irreducible of dimension two or four, so its only faithful four-dimensional '
        'representation is 3 + 1, and the colourless index is the only thing the algebra '
        'allows. BUT THE CORPUS CARRIES TWO OBJECTS CALLED COLOUR: P14s holonomy group -- '
        'the three wall monodromies with the hinge three-cycle -- is FINITE, of order 81, '
        'built and counted, hence zero-dimensional and FLAT by Ambrose-Singer, acting '
        'irreducibly on C^3 with scalar commutant, where a compact-face su(3) would be an '
        'isometry CARRYING A CURVATURE. P06s own appendix already records that the colour '
        'structure is not an isometry of either real form. Q3: AND BOTH BRANCHES CLOSE, '
        'on two facts the corpus already carries. SPINORIAL -- the so(6) spinor IS the 4, '
        'so 4 = 3 + 1 supplies the singlet, and the round S^5 has scalar curvature '
        'n(n-1) = 20 > 0, so Lichnerowicz forces ker D = 0 and there is NO CONTENT to '
        'carry it. VECTORIAL -- the 6 is 3 + 3bar, self-conjugate hence REAL hence '
        'vector-like, with NO COLOURLESS WEIGHT AT ALL, which is P14s own report from the '
        'other side that every candidate bundle is real. So THE SINGLET APPEARS IN '
        'EXACTLY THE REPRESENTATION THE FACE HAS NOTHING IN, and those are the only two. '
        'Q4: the hexad sits at the weights of 3 + 3bar EXACTLY -- in the sky angle the '
        'A_2 ROOTS are the ZEROS of 2M, the hinge and wall angles, and the 3 + 3bar '
        'WEIGHTS are the six Nariai MARKS, set for set, with the triples split by '
        'sign(2M). But the 30-degree offset is TRIGONOMETRY -- zeros and extrema of '
        'sin 3w interleave for any three-fold structure -- so the placement is FORCED by '
        'the A_2 structure already carried: it explains where the six marks sit and is '
        'not new information about so(6). AND THE DECISIVE PART IS WHAT IS ABSENT: what '
        'makes the six the VECTOR rather than a 3 and a 3bar is the SIX-DIMENSIONAL '
        'coset of so(6) mixing the triples continuously, and the construction offers a '
        'DISCRETE exchange and a SIGN where a phase would be needed. The weight diagram, '
        'not the module -- P03s own resonance-and-not-an-identity, a third time. W5, '
        'PLAINLY: the colourless state does not come from the compact face, not because '
        'the branching is missing but because the representation carrying it has no '
        'content and the one with content carries no singlet. THREE PLACES IT IS NOT -- '
        'bound sectors, the native propagating sector, the compact face -- ON THREE '
        'DIFFERENT MECHANISMS. NOT ESTABLISHED: that the colourless index is a lepton; a '
        'fourth index beside a triplet is a SHAPE, this is not Pati-Salam, nothing is '
        'named. Not a doublet: the so(4) does not commute with this su(3), shown two '
        'ways. Not that a branching label is a state. Not that either su(3) is wrong -- '
        'that they are two objects is a fact about the corpus. '
        'r6710 ASKS WHICH INDEX P14s Delta(27) ACTS ON, and the two-colours collision '
        'comes out stated exactly rather than carried as a wording. Q1: IT ACTS ON THE '
        'SEAT INDEX AND ON THE GENERATION INDEX NOT AT ALL. The holonomy is built from '
        'WALL monodromies, diagonal in the vantage basis, so its C^3 is the three '
        'signed areal radii, one per hinge -- the chiral SEATS, where this construction '
        'puts the colour grading. And the two indices are functions of INDEPENDENT '
        'variables: the seat datum 2M = (2/3 sqrt3) sin 3w carries no bead phase, the '
        'decks sector period 2 pi alpha/3 carries no sky angle and no mass, and the deck '
        'leaves sinh^2 invariant hence r hence every hinge. A group moving one fixes the '
        'other identically. Q2: SIGMA MEETS IT ON THE SAME SEATS WITHOUT ENTERING IT. '
        'Sigma is an involution where Delta(27) has EXPONENT THREE, so the group has no '
        'element of order two at all; read on the sky angle sigma carries each hinge to '
        'a WALL -- 0 to 60, 120 to 300, 240 to 180 -- and since each wall is antipodal '
        'to its own hinge that is a permutation of the SEAT index, the transposition '
        'fixing one seat. So sigma acts on the same index, NORMALISES Delta(27), and the '
        'two together give order 54: an extension at index two, not a coincidence and '
        'not an identity. Q3: NO, AND THE OBSTRUCTION IS ONE LINE. A holonomy is a '
        'representation of the FUNDAMENTAL GROUP of the space it is a holonomy on, and '
        'the round S^5 is SIMPLY CONNECTED, so every flat bundle over the compact face '
        'has holonomy of order ONE against the built groups 27 -- Delta(27) cannot arise '
        'there at all. A second and independent reason: a monodromy group needs a BRANCH '
        'LOCUS, and a homogeneous face has none where the Lorentzian face carries the '
        'invariant triple of zeros of 2M. SO THE TWO STRUCTURES THIS CONSTRUCTION CALLS '
        'COLOUR ARE NOT ONE OBJECT TWICE DESCRIBED, and the reason is not that two '
        'embeddings happen to differ: one is a pi_1 representation, and the face '
        'carrying the other has no loops to have holonomy around. Q4: the corpuss two '
        'usages name DISJOINT lists -- flavour skeleton is three generations, the family '
        'symmetry and the chirality, with the generations seated on the turnarounds '
        'cyclic three; discrete content of colour is the branching module, the wall '
        'monodromies with the hinge 3-cycle, and baryon 1 diquark 0 meson 1 -- and P14s '
        'own appendix bound enumerates the within-state S_3, the deck Z_3 and the '
        'discrete content of colour as SEPARATE deliverables. The corpus does not '
        'equivocate; what pulls the other way is the literatures label for the abstract '
        'group, and that label is SHOWN to carry no information about the index: the '
        'same abstract group built from generators on an unrelated index returns every '
        'invariant identical. NOT ESTABLISHED: that Delta(27) is the Standard Models '
        'colour SU(3) or any gauge group -- it is a finite FLAT holonomy giving '
        'selection rules and no force, as P14 states. Not that the compact faces su(3) '
        'is defective. Nothing about occupation. Not that the two threes could never be '
        'related by something unbuilt: what is shown is that nothing in the corpus '
        'relates them now. '
        'r6714 ASKS THE INDEX QUESTION ON THE SHARED FOUR-SPHERE that r6713 located, and '
        'the sphere turns out to supply its own twist while still returning a singlet. '
        'Q1: YES, THE TWIST IS GEOMETRIC. Computed in the EXPLICIT SPINOR representation, '
        'where the spin connection Omega_mu = (1/2) omega^{ab}_mu Sigma_ab is BLOCK '
        'DIAGONAL in gamma^5, so its two 2x2 blocks ARE the su(2) connections on the '
        'chiral spinor bundles with nothing left to normalise: k(S+) = +1 and k(S-) = -1, '
        'so c_2 = -1 and +1, equal and opposite as p_1(S^4) = 0 requires. The self-dual '
        'half of the round spheres own spin connection is the UNIT BPST INSTANTON, and '
        'the sphere radius drops out, so this is the substrates alpha-sphere and not only '
        'the unit one. LICHNEROWICZ IS EVADED BY THE GEOMETRY rather than by an added '
        'field. AND THE NORMALISATION IS NOT FREE, which is why it is done on the chiral '
        'block: writing A^i = c eta^i_{ab} omega^{ab} and fixing c by a consistency '
        'condition returns |k| = 5, a value no orientation or convention can produce from '
        '1, and one the p_1 identity cannot catch because it is ODD and cancels in the '
        'sum. A basis-free self-duality test confirms the two blocks independently of the '
        'integral. Q2: THE INDEX IS ONE, computed two independent ways -- Atiyah-Singer '
        'from the Chern number, the A-hat genus being 1 because p_1 = 0, and Hodge theory '
        'from the Betti numbers on the same operator read as a complex of forms. Their '
        'AGREEMENT is what pins c_2(S+) = -1 rather than leaving it quoted, and the '
        'kernel is (1, 0), reported apart from its difference. Q3: NO, AND NOT BY '
        'VACANCY. The one zero mode is the CONSTANT FUNCTION, a singlet of the su(2) that '
        'supplied the twist. S+ tensor S+ is 1 + 3 and contains NO DOUBLET AT ALL while '
        'carrying the zero mode; S- tensor S+ IS a doublet -- the (2,2), which is '
        'Lambda^1 -- and carries none, because b_1(S^4) = 0. THE CHIRALITY THAT HAS A '
        'STATE HAS NO DOUBLET IN IT AND THE ONE THAT IS A DOUBLET HAS NO STATE, and the '
        'obstruction is a Betti number. Q4: the factor supplying the twist is the factor '
        'of which the zero mode is a singlet -- the bundle-level shape is real, one '
        'factor seeing only one handedness, and the state sits in the singlet of that '
        'same factor; twisting by S- instead is the mirror and not an escape. TWO '
        'BOUNDARIES BELONG WITH IT: these su(2) factors rotate the spheres TANGENT space '
        'and are not internal, so nothing here is called isospin and the Kaluza-Klein '
        'question is untouched; and a zero mode on a face with no time in it, in an '
        'instanton background, is an INDEX STATEMENT ABOUT THE SPHERE and not a state in '
        'a spectrum. W5, PLAINLY: a FOURTH place the colourless state is not, and a '
        'FOURTH mechanism -- the unpaired level, the twist, Lichnerowicz, and now '
        'b_1 = 0. NOT ESTABLISHED: that the sphere carries no index -- it carries exactly '
        'one, and the geometric twist is a real finding. Not that no other twist could '
        'give a doublet: what is shown is that the bundle THE SPHERE supplies gives a '
        'singlet. '
),
    'PO-36': ('does the Hubble-Eddington radius track the dynamical mass or the baryonic one', 1, 0, 4, None,
        'r4203/r6407: the discrimination is QUANTIFIED -- the two mass choices differ by f_b^(-1/3) = 1.85 in the radiu '
        's (10.5 Mpc against 5.7 on a rich cluster) and by 1/f_b = 6.4 in a Lambda inferred from an observed one. BUT I '
        'T IS NOT A CR-VERSUS-LCDM DISCRIMINATOR, which this rows placement implies: m(r) is the bend, so whatever gra '
        'vitates is in it, exactly as in general relativity, and both frameworks take the same M. What the measurement  '
        'discriminates is the DARK FRACTION, not the framework -- control at f_b=1 gives ratio 1.000 and the test falls '
        ' silent. The corpuss stake is the input to one constant read at two ranges, whose local reading carries tha '
        't factor until the mass question is settled. And P03s quoted robust to dark-matter details and baryonic effe '
        'cts is profile-independence GIVEN M, not independence of WHICH M. '
),
    'PO-26': ('the compact-face fermion sector -- CAN IT BE BUILT', 1, 1, 6, None,
        'r3867: opened r3861 on a WRONG PREMISE -- I framed it as whether a sector can be built on the discrete '
        'component, and P14 has built one there. P13 sec:open: two things stay genuinely open and they are '
        'distinct; FIRST, the compact-face fermion sector. P14s sector lives on the DISCRETE component and '
        'supplies NO equivariant index, its count being a wall-localised leaf index well defined precisely where '
        'the bulk index is not. The sector the obstruction acts on is the other one, gauge-acted and '
        'isometry-realised on the compact face, and it remains unbuilt -- the major undertaking any geometric '
        'gauge-matter route would first have to complete. TRIP-WIRE: forcing the gauge group forces the Higgs '
        'representation with it.'),
    'PO-30': ('the curves own dynamics -- A GENERATIVE LAW FOR THE MATTER CONTENT', 1, 1, 6, None,
        'r6423/r6463: the curves dynamics GIVEN content is SUPPLIED -- the contracted Bianchi identity is entailed by  '
        'the cuts own geometry, not imposed, and a constitutive relation closes the system into ODEs on the cut: the T '
        'OV system in the operators own variables for the spherical class, P09s single ODE on (X,Y) for the homogeneo '
        'us. What is NOT supplied is the equation of state, and general relativity does not supply it either -- so the '
        ' slicing operator is kinematic is a caveat true of any geometric theory and not a defect of this one. The dif '
        'ference is that content is read LEFTWARD off the cut rather than fed into it. What is owed is a generative law '
        ' for the CONTENT, which P08 now hands to the matter sector -- and PO-26s strike (r6463) closes the geometric  '
        'route on the compact face, twice over, so that route is not where it comes from. '
        'r6479 joins this row to the head: every lap after the first inherits its cuts shape and the '
        'head inherits nothing, so PO-30 discharged discharges what the head owes and the converse fails. '
        'r6481 RULES OUT THE OBVIOUS CANDIDATE FOR THE LAW. p0s offset-mass relation has a UNIQUE positive '
        'stationary point and it lands exactly on the NARIAI member, r0 = alpha/sqrt3 and M = alpha sqrt3/9 '
        '-- a third route to that member, where P05 reaches it as sigmas fixed point and P07 by a collapse '
        'trichotomy, and unremarked at any of the four sites the cubic appears. BUT EVERY MEMBER OF THAT '
        'FAMILY HAS m(r) CONSTANT, so rho vanishes identically -- the one intrinsically distinguished cut '
        'carries NO distributed matter, where PO-41 says the head owes baryons. So the law must fix a '
        'FUNCTION m(r) and not a number: the constructions one distinguished point is in the wrong space. '
        'r6483 RETRACTS the third-route claim: the offset relation IS the horizon condition f(r)=0 '
        'written in r0, so extremising it is the double-root condition f = f = 0 that P15 already '
        'states at the Nariai locus -- the same computation in other variables, and the absence '
        'claim beside it was made from a grep without opening P03, P17 or P15. What survives is the '
        'connection and the function-not-a-number finding. '
        'r6485 IS WHOLLY RETRACTED at r6487 -- wrong at the root, and it inverted the programmes own '
        'thesis. Rule 2 is a criterion of NECESSITY VERSUS TUNING: prefer the world that REQUIRES a '
        'phenomenon as a structural consequence over one that merely PERMITS it through adjustable '
        'parameters. It is not a symmetry-maximiser, it governs the SUBSTRATE as the thing cut FROM, and '
        'what it rejects is a free MODULUS and not a breaking. P17s capstone is that physics IS the '
        'broken-symmetry shadow of one maximally symmetric object, so a breaking is what the construction '
        'produces rather than what it cannot. Rule 2 is therefore the STANDARD a law for the content must '
        'meet -- follow from the structure rather than enter as a tuned input -- and not a bar to one. '
        'The row stands OPEN, with that criterion attached to what an answer would look like. '
        'r6489 ASKS THE QUESTION PROPERLY, by looking at what actually breaks the symmetry in the '
        'cases already built. P14s prop:forced: a one-plane construction must select WHICH hinge, a free '
        'modulus, and the Z3-symmetric three-plane is the unique configuration carrying none -- so the '
        'criterion chooses AMONG BREAKINGS and takes the one that is itself symmetric, p0 extending this '
        'to the discrete sector and holding that the discrete breaking is itself maximally symmetric. AND '
        'BY THAT ROUTE CONTENT IS ALREADY GENERATED: P14 delivers the generation count, the chirality and '
        'the family symmetry. The wall, the generations and the chirality are ONE residue of the waist '
        'read at three places -- Aut(A2) = S3 x Z2, S3 on the points ON the circle and Z2 on the lines '
        'TANGENT to it. So the sharp open question is: the discrete residue is a FINITE group with a '
        'symmetric point, so its moduli-free configuration exists and is unique; a profile lives in a '
        'FUNCTION SPACE. Is there a moduli-free configuration for the continuous content, as the Z3 '
        'three-plane is for the discrete? Open, and nothing yet answers it. '
        'r6491 LOCATES THE DIFFICULTY by a join of three statements not previously read together. '
        'P14 also says, of the family symmetry, that what the sector supplies is the SYMMETRY and not the '
        'BREAKING -- the S3 arrives from the geometry while the breaking generating observed masses and '
        'mixings is marked external, alongside the gauge representations. Both are true, so there are two '
        'kinds of breaking: the three-plane configuration is ITSELF SYMMETRIC so there is nothing to '
        'choose and no modulus, while a hierarchy must DISTINGUISH the three planes and so is not, '
        'carrying exactly the modulus Rule 2 rejects. The boundary between what the geometry supplies and '
        'what it marks external COINCIDES with whether the breaking is itself symmetric -- one fact, and '
        'the reason the COUNT is forced while the MASSES are not. And p0s free-data budget is named and '
        'has shrunk once: the count, chirality and family symmetry moved from free data to forced when '
        'P14 built them, leaving the mass spectrum and the gauge representations. So this row is, in the '
        'corpus own accounting, whether the remaining entries can be converted as the first were. '
        'NOTHING IS CLOSED: P14 bounds its own marking -- the constraint is informative rather than '
        'prohibitive, it does not say a geometric route to the representation content is impossible, and '
        'P14 claims no construction. A mechanism outside the connected-isometry route is not excluded. '
),
    'PO-31': ('the progenitor spectrum, and what the throat damps under rotation', 1, 1, 6, None,
        'r6510: THE WARPED HARMONIC PROBLEM IS DONE AND THE PROXY WAS TELLING THE TRUTH. r6499 computed '
        'lambda on the rotating family but read it AT THE POLE, warning that the near-horizon sphere is '
        'warped through r_N^2 + a^2 cos^2 theta so one ratio may not describe it and l may not be a good '
        'label. The genuine problem now answers it. The near-horizon limit, TAKEN as a limit rather than '
        'posited and checked coefficient by coefficient, is a WARPED product and not a direct one: rho0^2 '
        'multiplies the dS_2 and polar directions alike and the dS_2 is FIBRED over the sphere by '
        'ktilde = 2 r0 a Xi/(r0^2+a^2), non-zero at every rotating member. AND THE ROWS OWN WORRY IS '
        'ANSWERED BY THE STRUCTURE: W ~ sin(theta) and P ~ Dtheta sin(theta) EXACTLY, so for the '
        'axisymmetric modes the warp cancels ALTOGETHER and the problem is a spheroidal deformation of '
        'Legendre in which rho0 never appears -- the harmonic label survives the warping rather than being '
        'spoiled by it, and rho0 enters only at m != 0. THE VERDICT IS EXACT RATHER THAN SCANNED: '
        'nu^2 = 1/4 - L^2 E - L^4 m^2 ktilde^2 with the fibration term NON-NEGATIVE, and two closed-form '
        'bounds -- L^2 >= 1 on the physical branch and E1 >= 2 above the monopole, each with equality only '
        'at a = 0 -- give L^2 E1 >= 2 against the threshold 1/4. A FACTOR OF EIGHT across 0 <= a < a_max, '
        'attained where the rotation VANISHES: the marginal member is the NON-ROTATING one, so rotation '
        'strictly improves the case. The monopole keeps nu^2 = 1/4 exactly. NOT settled, and said so: this '
        'is a massless SCALAR proxy, it is about whether the DAMPING MECHANISM reaches these modes and NOT '
        'about whether J survives the leg, and the near-horizon geometry is the fixed point rather than the '
        'approach to it. Remaining on this row: the progenitor spectrum itself, a modelling task awaiting a '
        'progenitor interior, and eta, inherited because a conservation law protects it. '
),
    'PO-25': ('the charged bead -- DOES A CHARGED COLLAPSE FORM THE CAUCHY HORIZON', 1, 1, 4, None,
        'r3827/r6405: the step is RUN and comes out the same in both charge readings, which decouples it from the datum '
        ' fork. The criterion is beta = (decay rate)/kappa_- against 1/2 -- and Lambda>0 is why it needed a number, the '
        ' decay being exponential rather than Price-tailed so the horizon CAN survive near extremality. On the progenit '
        'or it does not: beta ~ 1e-251 intensive, 1e-15 extensive, with a generous ceiling so the figure bounds the hor '
        'izons chances from above. THE ETERNAL INNER HORIZON IS NOT FORMED, so the obstruction is a property of a stat '
        'ionary solution the dynamical problem does not reach. NOT delivered: inextendibility is not a spacelike r=0, s '
        'o the charged case is not thereby rejoined to the bead. '
        'r6521 SHARPENS WHAT REMAINS, by applying this rows own move to the claim beside it. r6405 '
        'found the inner-horizon obstruction to be a property of a STATIONARY solution the dynamical '
        'problem does not reach -- and P03 makes that distinction once and does not apply it to the '
        'sign-switch obstruction next to it, which is read off the same stationary f with M CONSTANT. '
        'Dynamically half survives and half is a condition: Gauss law makes the Q^2/r^2 term real, so '
        'charge does not wait for stationarity to gravitate -- but m is then a FUNCTION, and the sign at '
        'the origin switches iff 2m/r stays below Q^2/r^2, i.e. iff m(r) = o(1/r) as r -> 0. Writing '
        'm ~ k r^-p: p<1 keeps the obstruction, p>1 destroys it, p=1 decided by whether 2k exceeds Q^2. '
        'So what stands in the horizons place is not an open-ended ask about the interior -- it is one '
        'condition on the interior mass function. NOT CLAIMED that m fails it: nothing computes the '
        'interior, and mass inflation is about the Cauchy horizon at FINITE r, not about the origin. '
),
    'PO-24': ('whether the tilt displacement is a tension', 1, 1, 5, None,
        'r4505/r6409: the remaining question is not well posed as asked. It presumes the displacement is a NUMBER; it i '
        's the local slope of a curve whose slope varies by (lmax/lmin)^2 = 6989 across the likelihoods own l=30-2508. '
        ' So a single tilt is a one-parameter fit to a function whose log slope varies by seven thousand over the data  '
        'scoring it, absorption is WINDOW-LOCAL, and the quoted -0.0304 is the true slope at l=381 and nowhere else. A  '
        'joint fit therefore meets a GAUSSIAN-SHAPED residual, not a shifted tilt, and no tilt removes a Gaussian -- so '
        ' what it weighs is the shape residual, already bounded at 0.26 sigma per bin. And n_s is inherited boundary da '
        'ta, so a displacement in it is a different input, not a conflict. '
        'r6522 RUNS THE JOINT FIT, and r6409s reading is confirmed by MEASUREMENT. A_s and n_s fitted '
        'jointly against the CR spectrum with the signature present, on plik_lites own l range and '
        'covariance: Delta n_s = -0.08304 +/- 0.00335 over l=100-1758, 171 covered bins, which '
        'independently reproduces C62s INSTRUMENT-route displacement (-0.0847) to 2 percent by a '
        'different method on a different spectrum. THE RESIDUAL AFTER THE FIT CORRELATES WITH THE '
        'ANALYTIC GAUSSIAN-MINUS-BEST-POWER-LAW AT 1.000000 AND SURVIVES AT 1.497 chi^2 PER BIN, '
        'larger than either bound C62 left. The tilt takes 69.8 percent of the signature and no more. '
        'TWO CORRECTIONS THE RUN FOUND BY READING ITS OWN SOURCE: C62 states 0.26 in CHI^2 per bin and '
        'converts to sigma with a square root in its own check, while r6409 restated it as 0.26 SIGMA '
        'per bin -- the looser bound quoted as the tighter, 0.26 chi^2/bin being 0.510 sigma/bin. And '
        'C62 carries TWO routes and says in terms that the instrument route is the more faithful and '
        'the LARGER, so the wash is asserted at the weaker bound: 0.92, not 0.26. AND THE DISPLACEMENT '
        'IS NOT A NUMBER, MEASURED: across windows of the same data it runs -0.083 (100-1760), -0.210 '
        '(700-1760), -0.309 (1000-1760), -0.341 (1000-2508), -0.521 (1400-2508), a factor of 6.3, with '
        'absorption climbing 69.8 to 97.6 percent as the window narrows upward -- so a restricted '
        'window is what makes the wash look complete. IN THE LIKELIHOODS OWN UNITS the signature costs '
        '+357.3 chi^2 with amplitude alone and +84.5 after the tilt is refitted over the same 171 '
        'bins: the fit IMPROVES the comparison by 272.8, absorbing 76 percent, and does NOT remove it. '
        'The sky-compensating tilt is BLUE (+0.0616) where the degeneracy fits is RED (-0.0830), kept '
        'apart. Calibrated before believed, and the first calibration was blind to what the second '
        'caught: a known injected tilt recovers to 7e-11, but that test is UNIT-FREE and passed while '
        'residuals were divided by plik sigma without the x11021 normalisation the banked spectra need. '
        'WHAT KEEPS THE ROW OPEN IS NOT THE FIT: n_s is inherited, so the displacement is a different '
        'input rather than a tension, and what this run does not reach is a constraint on n_s off the '
        'damping tail -- low-to-mid-l shape, TE/EE, lensing. This was TT alone. '
),
    'PO-43': ('the Weyl-squared coefficient at second order in the shear', 1, 1, 5, None,
        'r6415/r6435/r6471: the coefficient is COMPUTED -- 1/60 in units of (4pi)^-2, exactly twice a real minimally co '
        'upled scalars, the tower being two such degrees of freedom by P10s own description. Stated on the PHYSICAL-M '
        'ODE count, the constraints here being solved rather than gauge-fixed, which is where it is attackable. And the '
        ' invariant it multiplies was corrected: C^2 = 2 sum (sigma + H sigma)^2, two more derivatives than the 4 sigm '
        'a^2 P10 stated, so it grows as omega^2 sigma^2 for a mode. BOTH replacement questions are answered: the connec '
        'ted-isometry one by PO-44s strike, and the topological-terms one at r6471 -- the ledger does not count them,  '
        'its statement being the geometric gauges and the closing of the one extension freedom. '
),
    'PO-23': ('the mode sums beyond the free static case', 1, 1, 5, None,
        'r4537/r6411/r6453: the free case is EXACT -- zeta(0) = 10 by a terminating expansion, log coefficient 39/4 as  '
        'the 1/m term of d(m)mu(m), a cutfree cutoff agreeing. 60s r6436 adds that NO RESCALING discharges it, L = (39 '
        '/4)sqrt(1+eps), generalising to any multiplicative renormalisation -- but only WITHIN the class of spectral de '
        'formations, and that premise cannot be established ahead of this row, since it asks what the coupling does to  '
        'the sum and the open item IS the definition of that sum. So the free-spectrum method reaches exactly as far as '
        ' it reaches. This is the LAST of P07s three parts: the operator is bounded below and its spectrum is computab '
        'le branch by branch, both now said. '
        'And r6455 adjudicates rather than cites the r1291 restoration: the remainder is a GENUINE '
        'CR open, not the generic non-renormalisability problem -- the counterterm basis here is '
        'ONE-dimensional, the constraint is SOLVED so there is a true Hamiltonian on a compact slice '
        'with a discrete spectrum, and unlike PO-36 no other framework has this tower. '
),
    'PO-15': ('the ordering — EXHAUST the selection candidates', 1, 1, 3, None,
        'r3015: THE STEP IS AN EXHAUSTION. The thermal state is eliminated (it selects the Friedrichs extension, which is defined FROM the form an ordering produces). Enumerate what else could select one — the substrates symmetry, the seams characteristic structure, the deparametrization — and either find one or state the choice is external WITH the enumeration as evidence'),
    'PO-14': ('the unbuilt chiral member — THE BUILD', 1, 1, 5, None,
        'r3015: extend P11s polarised Gowdy-de Sitter leaf to the unpolarised case — two propagating modes, coupled nonlinearly. P09: reachable, needing no machinery the operator lacks. Until built, four classes where five are required'),
    # ** r3095: brought in from p0's frontiers and the field ledgers, which carried them
    # unregistered.  Estimates are stated as unknown (0) rather than guessed: none of these
    # four has had a step scoped, and a fabricated estimate is worse than none. **
    'PO-17': ('the phase structure at the seam — real structure, or interpretation', 1, 1, 0, None,
        'NARROWED BY RECEIPT: Z1 rules out both the matter/antimatter labelling and the continuous-parameter readings; Z2 settles the OBJECT level (K is real structure of the plate, the photon congruence its fixed set). The live question is strictly: DOES A MASSIVE TRAJECTORY CARRY A PHASE. Held not claimed both ways'),
    'PO-18': ('the maximal-symmetry ledger — ENUMERATE what the substrate forces', 1, 1, 0, None,
        'THE LEDGER IS RUN: CONSTANT_LEDGER_receipt.md reads Lambda as the sole scale, c and G as unit gauges, hbar locked by the horizons thermal state — the gravitational-quantum sector spends ZERO free dimensionless constants; U3 answers the second half. What is open: it is NOT BANKED into a paper, and the matter sectors count waits on the matter build'),
    'PO-19': ('the cube-root-two ratio between the two turnings', 1, 1, 0, None,
        'CHECKED against order3_bridge, which relates the two cubics as one family at two energies and carries W(A2)=S3 at both ends — that is the SYMMETRY relation, not this rows object. The metric ratio between two specific radii is untouched by it and by lem:twoturnings. Undecided since r1103; both cheap answers forbidden'),
    'PO-20': ('growth and order at infinity — is boundedness an analytic statement', 1, 1, 0, None,
        'COMPLEX_ANALYSIS_LEDGER 4d queue, registered L-209 when found and lost at the r3009 turnover. sinh essential singularity at infinity sits outside the finite lap — noted, not used. The question is UNASKED, so the step is to ask it'),
}
# ** THE COUNTER, AND THE CRITERION IT IS SCORED AGAINST (r2847, after Daryl caught two
# turns wrongly scored 0).  *** A turn is a 0 ONLY IF it found the problem space DIFFERENT
# from what the register said.  Running a stated computation and getting the EXPECTED answer
# is a STEP ADVANCED, not a discovery -- however good the result. ***
#
#   0   r2842  PO-7   the two numbers were never a contradiction; the spacing is ell-dependent
#   0   r2843  PO-10  half 1 was TWO questions and one was already answered
#   0   r2844  PO-1c  six was the wrong KIND of number -- configurations, not states
#   ×   r2845  PO-1b  the type-check PASSED as expected -- a step, not a discovery
#   ×   r2846  PO-6   the commutator SURVIVED as expected -- a step, not a discovery
#
# ** I scored both of the last two as 0 and they were not. **  *** The counter rising is the
# thing it exists to show, and inflating it to 0 makes the step estimates a lie -- which is
# the exact failure it was built to expose. ***
# ⛭ r6611: these are JUDGEMENTS, not derivable, so they are hardcoded -- and LASTFIND had gone
#   ~2000 revisions stale, still naming r4549 while the problem space moved repeatedly.  ** A
#   "last actual move" line that is two thousand revisions behind reports the opposite of what it
#   is for. **  Set to the last find that actually moved the picture.
SINCE = 2
LASTFIND = ("r6713: **the two faces are both five-dimensional and share one four-sphere** -- the "
            "throat of dS_5 and the equator of S^5, fixed by the Wick rotation -- which is the one "
            "place in either face where chirality exists, and its so(5) carries su(2) and cannot "
            "carry colour. With r6709-r6711 it moves the picture: P14's SU(3) part is the finite "
            "Delta(27), acting on the seat index, with SU(3) only its smallest connected home.")

# ** CALIBRATION (r2848) -- estimates measured against actuals rather than felt. **
# *** Six steps closed with a number attached; EVERY ONE took one turn; I had predicted
# 2-3.  Mean overestimate 2.3x. ***  Every one was a READ or a SHORT COMPUTATION on
# material already in the corpus.
#
#   r2838 PO-6  locate C6/C7 tension    est 3  actual 1
#   r2842 PO-7  compare peak-finders    est 3  actual 1
#   r2843 PO-10 read M2's bound         est 1  actual 1
#   r2844 PO-1c the horn count          est 2  actual 1
#   r2845 PO-1b the type-check          est 2  actual 1
#   r2846 PO-6  the commutator          est 3  actual 1
#
# ** SO: a READ step is estimated at 1 turn, from evidence. **
# ⚠ *** A BUILD step has NO completed instance to calibrate against -- PO-11's continuum,
# PO-6's UV definition, PO-1a's derivation.  Those are marked BUILD and their estimates
# are declared unmeasured rather than dressed as measured. ***
KIND = {'PO-46': 'BUILD', 'PO-13': 'BUILD', 'PO-36': 'READ', 'PO-33': 'BUILD',   # r4145: was READ, scoped when the diagnosis looked answered; it is not
         'PO-14': 'BUILD', 'PO-15': 'READ', 'PO-16': 'READ',
        # ** brought in r3095 from p0's frontiers and the field ledgers, which carried them
        # unregistered.  PO-17 is a DECISION stated without being claimed both ways; PO-18 an
        # ENUMERATION; PO-19 and PO-20 are unattempted questions, so READ is the wrong kind
        # for them and WORK is used. **
        'PO-17': 'READ', 'PO-18': 'READ', 'PO-19': 'WORK', 'PO-20': 'WORK'}

# ** PO-23 added r3809: the ultraviolet definition of the mode sums, the one part of P07's
# three-part 'definition of the interacting tower' that is neither settled nor attempted. **
# ⛔ r6549: `ORDER` IS A THIRD HARDCODED LIST, and a row absent from it does not RENDER even
#   though it is live and has a runway.  *`PO-45` was registered at r6547 with an `EST` entry,
#   and the generator reported "9 open" while the table showed EIGHT -- the count comes from
#   the live set and the rows come from here.*  ** Adding a row needs three things: the
#   register row, the runway, and this list. **  check_frontier_current now checks all three.
ORDER = ['PO-45', 'PO-46', 'PO-13', 'PO-43', 'PO-24', 'PO-36', 'PO-30', 'PO-25', 'PO-26', 'PO-31', 'PO-23', 'PO-15', 'PO-14', 'PO-17', 'PO-18', 'PO-19', 'PO-20']
GROUP = {'PO-45': 'A', 'PO-46': 'A',  # ⛔ r6549: a FOURTH hardcoded list -- GROUP -- and a row missing here raises.
         'PO-13': 'D', 'PO-14': 'A', 'PO-15': 'C', 'PO-16': 'D',
         # ** r3095: the four brought in from p0's frontiers and the field ledgers.  PO-17 and
         # PO-19 are substrate geometry; PO-18 is the constant ledger; PO-20 is analysis. **
         'PO-17': 'E', 'PO-18': 'E', 'PO-19': 'E', 'PO-20': 'E',
         'PO-23': 'C', 'PO-43': 'C', 'PO-24': 'D', 'PO-25': 'E', 'PO-26': 'A', 'PO-27': 'A', 'PO-29': 'E', 'PO-31': 'D', 'PO-30': 'A', 'PO-36': 'D', 'PO-34': 'E'}
# ⛭ r6611: sector B carried A's title and NO row has ever been assigned to it -- the
#   assignments run A:5, C:3, D:5, E:7, B:0.  ** A vestigial sector printing a duplicate
#   heading over an empty table is a reader's trap, not a section. **  Dropped; if a row
#   ever needs a second matter sector it gets a title of its own at that point.
GNAME = {'A': 'the matter sector', 'C': 'the quantum sector',
         'D': 'the cosmology', 'E': 'the substrate geometry'}



def _cites():
    """** r2874: how many receipts each open row cites, counted from the register. **
    *** Daryl: every row needs to be citing the corpus.  The register held 11% of its
    own worked corpus; this column makes that visible every turn. ***"""
    raw = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8',
               errors='replace').read()
    out = {}
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m or m.group(1):
            continue
        out[m.group(2)] = len({c for c in re.findall(r'`([A-Za-z0-9_]+)`', line)
                               if re.match(r'^[A-Z]\d+[a-z]?_|^L\d+|^S\d+_|^P\d+_|'
                                           r'^M\d+_|^C\d+_|^B\d+_|^Z\d+_', c)})
    return out


def main():
    raw = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8', errors='replace').read()
    CITES = _cites()
    live = set()
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if m and not (m.group(1) or line.lstrip('|').lstrip().startswith('~~')):
            live.add(m.group(2))

    steps = sum(EST[p][1] for p in ORDER if p in live)
    was = sum(EST[p][2] for p in ORDER if p in live)
    turns = sum(EST[p][1] * EST[p][3] for p in ORDER if p in live)

    L = []
    # ** r3095: THE FRONTIER carried NO currency marker, so check_currency measured it by body
    # scrape and reported it UNDECLARED -- the live view, unmeasurable.  The marker is written
    # HERE because this generator is the only thing that brings the file current, which is the
    # gate's own rule: a declaration written only by the pass that actually does the work.
    # The declared value is THE_REGISTER's own `current:`, because that is what was read. **
    _regcur = ''
    try:
        _rt = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8', errors='replace').read()
        _rm = re.search(r'(?m)^current:\s*(\S+)', _rt)
        _regcur = _rm.group(1) if _rm else ''
    except OSError:
        pass
    L.append('---')
    L.append('name: the-frontier')
    L.append('kind: VIEW')
    L.append('job: the open problems in dependency order — generated from THE_REGISTER, the one source')
    if _regcur:
        L.append(f'current: {_regcur}')
    L.append('sources: [chat]')
    L.append('---\n')
    L.append('# ▣ THE FRONTIER\n')
    L.append('*Generated by `scripts/regen_frontier.py`. **The open problems, in dependency order.** '
             'A STEP is one worked result; turns-per-step is a separate estimate.*\n')
    L.append(f'## ⇒ **{len(live)} OPEN · {steps} STEPS LEFT** *(was {was} last revision)* '
             f'**· ~{turns} turns at current estimates**\n')
    blocked = [p for p in ORDER if p in live and EST[p][4]]
    # ** r2839, Daryl: the number to hold is TURNS SINCE WE LAST DISCOVERED WE DID NOT KNOW
    # THE PROBLEM SPACE.  *** 0 means the last turn found a misunderstanding -- which is what
    # fixing the problem FUNDAMENTALLY looks like, as against advancing a step incrementally.
    # It is guidance for CHOOSING a turn: pick the row held least well, not the row nearest
    # closing. ***
    L.append(f'## ⇒ **TURNS SINCE WE LAST FOUND WE DID NOT KNOW THE PROBLEM SPACE: '
             f'{SINCE}**\n')
    L.append(f'*⌗ **LAST ACTUAL MOVE — {LASTFIND}***\n')
    if SINCE == 0:
        # ** r2842, Daryl: while this counter reads 0 the step and turn estimates above are
        # NOT TRUSTWORTHY -- each 0 means the problem space itself moved, so the estimates were
        # made against a picture that has since changed.  *** They become meaningful only once
        # the counter starts rising, and saying so on the board is the honest form. ***
        L.append('> ⚠ ***AND WHILE THIS READS 0, THE STEP AND TURN ESTIMATES ABOVE ARE NOT '
                 'TRUSTWORTHY.*** *Each 0 means the problem space moved, so the estimates were '
                 'made against a picture that has since changed. **They acquire meaning only when '
                 'this counter starts rising** — that is what the counter is for.*\n')
    else:
        L.append('*⚠ **Above 0 means the last turn advanced a step without learning the space. '
                 'Pick the row held LEAST well next, not the one nearest closing.***\n')
    L.append(f'**RUNWAY: {len(live)-len(blocked)} of {len(live)} clear now**; '
             f'{len(blocked)} gated ({", ".join(f"{p}→{EST[p][4]}" for p in blocked)}).\n')

    for g in sorted(GNAME):
        L.append(f'\n### {g} · {GNAME[g]}\n')
        L.append('| id | what it is | steps | was | turns/step | kind | cites | gate | runway |')
        L.append('|---|---|---|---|---|---|---|---|---|')
        for p in ORDER:
            if GROUP[p] != g or p not in live:
                continue
            name, s, w, t, gate, note = EST[p]
            arrow = '' if s == w else (f' ↓{w-s}' if s < w else f' ↑{s-w}')
            k = KIND.get(p, '?')
            tcell = f'{t}' if k == 'READ' else f'{t} ⚠'
            L.append(f'| **{p}** | {name} | **{s}**{arrow} | {w} | {tcell} | {k} | '
                     f'{CITES.get(p, 0)} | {gate or "—"} | {note} |')

    L.append('\n---\n')
    L.append('*⚠ **READ estimates are MEASURED**: six steps closed, every one took one turn '
             '(I had predicted 2–3; mean overestimate 2.3×). **BUILD estimates carry ⚠ and are '
             'UNMEASURED** — no build step has ever been completed here, so those numbers are '
             'judgement with nothing behind them.*\n')
    L.append('*⌗ Steps and turn-estimates are judgements recorded so their CHANGE is visible. '
             'They are edited in `scripts/regen_frontier.py`, never here.*')
    open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(f'  THE_FRONTIER.md written: {len(live)} open, {steps} steps (was {was}), ~{turns} turns')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
