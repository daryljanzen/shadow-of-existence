#!/usr/bin/env python3
"""check_withdrawn.py -- the NINTH gate, and it exists because the same failure happened twice
in the one place nobody looks.

** THE FAILURE. **  At c54.31 the matter sector withdrew the identification of a generation with
a hinge/wall: the walls' S_3 is a WITHIN-STATE index and the generations' own threeness is the
turnaround's deck Z_3.  At c54.60 a sweep propagated that to five companion papers.  At c54.86
the frontier audit found it still live in two places the sweep never looked:

  * P14's OWN ABSTRACT -- asserting the identification that P14's own section is titled after
    denying ("Which three the generations are seated on, and why it is not the hinges");
  * P7's frontier item 5 -- which STATES the revision and then, three sentences later, restates
    the withdrawn reading as current, so the paragraph contradicted itself.

** THE PATTERN, WHICH IS THE POINT. **  A result lands in the section that produced it and does
not reach the places that SUMMARISE -- abstracts, frontier lists, synthesis sections.  Those are
exactly where a reader goes first and exactly where a working node edits last.  The c54.60 sweep
fixed five bodies and no summaries.

** WHAT THIS GATE DOES. **  It carries a REGISTRY of withdrawn claims, each a phrase pattern plus
the markers that count as an adjacent correction.  A paper may still contain a withdrawn claim's
wording -- the corpus routinely quotes what it withdrew, and that is honest -- but only if a
revision marker follows within WINDOW characters.  A bare occurrence is a FAILURE.

** ADDING TO THE REGISTRY IS PART OF WITHDRAWING SOMETHING. **  When the corpus withdraws an
identification, the withdrawal is not finished until its phrase is registered here; otherwise the
next summary that quotes the old reading is invisible again.

Run it after any withdrawal, and in the standing gate sweep.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WINDOW = 900          # characters after a hit in which a correction still counts as adjacent

# --- THE REGISTRY -------------------------------------------------------------------------
# (label, phrase pattern, marker pattern, when and where it was withdrawn)
REGISTRY = [
    # r6881+cc66.34.  "THE SHARED FRACTION SAYS THE MISFIT IS THE TRANSFER'S".  `r6879+cc66.33`
    # reported that 73.1% of the CR arm's chi^2 lies along the control's residual direction and read
    # that as attribution -- "on the order's own criterion that part is the transfer's and not the
    # construction's".  ** Both arms are fitted to the SAME data, so r_CR = r_ctl + (m_CR - m_ctl)
    # exactly: the two residuals share the -d term by construction and the statistic ranks how alike
    # the two MODELS are.  A flat-LCDM control deliberately tilted by dn_s = +0.02, at chi^2 = 214.6,
    # scores 82.2% -- HIGHER than the arm. **  The number stands; the inference does not, and the
    # corrected reading points the other way (the control fits at 0.994/bin, so the arm's +105.1
    # excess is the construction's).  ** The row may still QUOTE the sentence -- the withdrawal is
    # recorded by quoting it -- but not assert it. **
    ("the-shared-fraction-attributes-the-misfit-to-the-transfer",
     # ** WIDENED IMMEDIATELY, AND THE FIRST PATTERN IS WHY THE GATE HAS THIS COMMENT. **
     # The first version read "that part is the transfer's and not the construction's" -- MY
     # wording, in MY row.  `P15` says "So three quarters of the disagreement is the transfer's
     # and not the construction's", and the gate reported the tree clean with the withdrawn
     # claim standing in the paper.  ** A registry keyed to one seat's phrasing is a registry
     # that checks one seat ** -- the same lesson r6465 records one entry below.
     r"is the transfer's and not the construction's"
     # ⌗ NARROW ON PURPOSE.  A generic "<fraction> ... is the control's" also fires on
     # `PO-47`'s live and UNWITHDRAWN finding that 57% of the fourth-peak offset is the
     # control's, which is a different claim about a different quantity.  The subject has
     # to be the RESIDUAL.
     r"|three quarters of (?:this arm's|the (?:arm's )?residual)[^.\n]{0,20}is the control's"
     r"|\d\d(?:\.\d)?\s*(?:per cent|\\%) of the arm's (?:residual|\\?chi)[^.\n]{0,40}"
     r"is the control's"
     r"|(?:fraction|per\s*cent|\\%)[^.\n]{0,80}along the control's[^.\n]{0,80}"
     r"(?:is|are) the transfer's",
     r"(?:r6881|withdrawn|WITHDRAWN|similarity|does not follow|inference)",
     "withdrawn r6881+cc66.34; the shared fraction ranks model similarity, not attribution"),
    # r6713+66.1.  THE PROPAGATING DIRAC SECTOR "NOT YET ON THE CHIRAL ONE".  P11 builds the
    # unpolarised Gowdy--de Sitter member as the first chiral member of the reachable sector and
    # puts a massless Dirac field on it; P7 states the chiral geometry built; P14 computes that on
    # it the geometry permits the chirality-asymmetric action and does not select it.  ** The
    # unpolarised member IS the chiral member. **
    ("dirac-sector-not-yet-on-the-chiral-member",
     r'not yet on the chiral (?:one|member)',
     r'(?:r6713\+66|withdrawn|first chiral member)',
     "withdrawn r6713+66.1; the unpolarised member is the first chiral member (P11)"),
    # r6477.  "THE PDFS ARE SERVED FROM JSDELIVR" -- withdrawn at r6475, the site having
    # moved to serving its own from the repository (`CDN = RAW_GH`, and the body had said
    # `NO THIRD-PARTY CDN` since the migration).  It survived in a generator header AND on
    # the live page, telling readers the book depended on a CDN it no longer used.
    # ** A machinery claim may be QUOTED to record its withdrawal -- r6475 does exactly
    # that -- but not asserted. **
    ("the-papers-are-served-from-a-cdn",
     r'(?:Papers|PDFs)\s+(?:are\s+)?(?:served\s+)?(?:from|via)\s+jsDelivr'
     r'|served from jsDelivr'
     r'|FETCHES[^.\n]{0,40}from the CDN',
     r'(?:r6475|withdrawn|no longer|stopped using|went on describing|NO THIRD-PARTY CDN'
     r'|repository)',
     "withdrawn r6475; the site serves its own from the repository"),
    # r6425.  THE COMPACT-FACE SECTOR "IS VECTOR-LIKE".  The face is the FIVE-sphere, and
    # Atiyah--Hirzebruch's equivariant index is Z_2-graded, so its even-dimension hypothesis
    # fails there and that route is vacuous ON THIS FACE.  ** The conclusion survives by the
    # paper's OTHER route -- positive scalar curvature and Lichnerowicz, which needs no
    # dimension -- and gives MORE: the round five-sphere has no Dirac zero modes at all, so the
    # sector is EMPTY rather than vector-like. **  A paper may still quote "vector-like": it is
    # what the literature concluded for the even-dimensional case, and Witten's precedent is
    # untouched.  It may not do so BARE.
    ("the-compact-face-sector-is-vector-like",
     r'(?:sector|spectrum)\s+(?:there\s+)?(?:is|being)\s+(?:therefore\s+)?vector-like'
     # ** r6465: WIDENED.  The first pattern was written against P13's wording, "the
     # GEOMETRIC fermion sector", and p0 says "a COMPACT-FACE fermion sector" -- so the
     # withdrawn claim sat bare in p0 and this gate reported the tree clean.  A registry
     # keyed to one paper's phrasing is a registry that checks one paper. **
     r'|render(?:ing|s)?\s+(?:the|a)\s+[\w-]*\s*fermion sector\s*vector-like'
     # ** r6505: WIDENED A SECOND TIME.  The first widening was keyed to "render ... vector-like";
     #   P13's own SUMMARY paragraph says "yields a vector-like fermion spectrum", which neither
     #   form caught.  *Three wordings, three misses -- a phrase-keyed registry is only ever as
     #   wide as the phrasings someone happened to look at.*  This one matches the ADJECTIVE
     #   applied to the spectrum or sector by any verb. **
     r'|(?:yield|give|produce|leave)(?:s|ing)?\s+(?:a\s+)?vector-like\s+fermion\s+(?:spectrum|sector)'
     r'|vector-like\s+fermion\s+spectrum'
     r'|makes the spectrum vector-like',
     r'(?:empty|no zero modes|odd-dimensional|even dimension|five-sphere|Lichnerowicz'
     r'|vacuous|withdraw|superseded|struck r\d+|the even-dimensional case)',
     "withdrawn r6425 by P13 sec:wall; the conclusion holds by the Lichnerowicz route and is stronger"),
    ("generations-are-the-hinges",
     r'(three generations one object read three ways'
     r'|the generations are \\emph\{one object read three ways\}'
     r'|which wall each binds at'
     r'|a generation (?:per|at each) (?:hinge|wall)'
     r'|family \$S_3\$|family S₃|the family \$S_\{?3\}?\$'
     # both word orders: the map writes "an S_3 family symmetry", the papers "the family S_3"
     r'|\$?S_?\{?3\}?\$? famil(?:y|ies)'
     r'|generations? via \$?S_?\{?3\}?\$?)',
     r'(has since been revised|withdraw|follows the revision|not the hinges|within-state'
     r'|turnaround\'?s deck|the within-state index|STALE|struck r\d+|superseded)',
     "withdrawn r2376+c54.31 by P14 sec:whichthree; propagated c54.60, c54.86"),
    # r2376+c54.105.  The binding-energy naturalness argument for the inherited radiation
    # amplitude.  Written from the CLAIM and not from the sentence, per THE_BASE_RATE's third
    # entry: the noun phrase alone, both word orders, and the contrast it was drawn against.
    # r2376+c54.149-150, registered c54.151.  THE FULL-LAP FLOQUET APPARATUS and every verdict
    # resting on it.  c54.143-148 propagated the progenitor from the closed ball's own a=0,
    # composed with the monodromy, and read a periodic map off the result -- attractors,
    # instability bands, a per-cycle multiplier, two exclusions of "the chain," a 420-mode comb.
    # c54.149 withdrew it (the construction supplies no such background); c54.150 declined to
    # reinstate it (the basis identification is unestablished either way).  ** THE WITHDRAWAL WAS
    # NOT REGISTERED HERE FOR TWO REVISIONS, AND IN THAT WINDOW THE_WORK CARRIED THREE OF ITS FOUR
    # AFFECTED CLOSURE ROWS AS STANDING RESULTS.  THE_BASE_RATE's fourteenth entry. **
    ("the-full-lap-floquet-apparatus",
     r'(\\lvert\\lambda\\rvert\s*=\s*1'
     r'|\|\\lambda\|\s*=\s*1'
     r'|\|lambda\|\^?2?\s*=\s*1'
     r'|per-cycle (?:amplification|multiplier|map)'
     r'|full-cycle map'
     r'|instability bands?'
     r'|stability bands?'
     r'|the transfer is unity'
     r'|cosmogenesis is not a chain'
     r'|the chain is excluded'
     r'|the comb (?:is|as) a prediction'
     r'|a complete cycle with a branch point at each end'
     r'|across a full cycle'
     r'|the cyclic structure of the excursion'
     r'|the output of the previous branch point)',
     r'(withdraw|WITHDRAWN|not reinstated|struck|STRUCK|c54\.149|c54\.150|c54\.151'
     r'|wrong background|no such object|no such epoch|does not hold|not established'
     r'|is not restored|stand withdrawn|the construction has no such)',
     "withdrawn r2376+c54.149, not reinstated c54.150; registered c54.151"),
    # r2376+c54.143, registered c54.151.  THE FIVE COMPOSITION UPPER BOUNDS and the spectral
    # KNEE they all turned on.  c54.132/133/138/141 bounded rho_r/rho_m from the observed
    # spectrum's flatness; four asked where the knee SITS rather than what curvature it leaves
    # where the spectrum is measured, and the fifth assumed the incoming perturbation is a free
    # oscillation.  ** The withdrawal stands; its GROUND has moved.  c54.143 argued from a
    # full-cycle attractor, which is itself withdrawn (see the entry above).  What survives is
    # that the construction SPECIFIES the incoming state -- an overdensity in a universe like
    # ours carries a processed adiabatic spectrum -- so it was never free to idealise. **
    ("the-leaked-branch-knee-and-the-five-composition-bounds",
     r'(the spectrum acquires a knee'
     r'|so that the spectrum has a knee'
     r'|bounds the progenitor\'s radiation fraction'
     r'|the progenitor\'s radiation fraction is (?:now )?bounded'
     r'|BOUNDED FROM BOTH SIDES'
     r'|the crossover to lie beyond it'
     r'|the observed spectrum bounds the (?:parent|progenitor))',
     r'(withdraw|WITHDRAWN|struck|STRUCK|c54\.14[13]|c54\.15[01]'
     r'|not a bound but a determination|is a determination|does not establish'
     r'|no bound (?:follows|exists)|an order of magnitude with a stated assumption)',
     "withdrawn r2376+c54.143 (five bounds); the ground itself revised c54.149-151; registered c54.151"),

    # r2376+c54.150, registered c54.151.  c54.149's OWN GROUND for calling the full lap
    # unphysical -- that the progenitor separated from its ambient expansion, so its past a = 0
    # is algebra rather than history.  ** In the standard spherical-collapse description the
    # patch's a = 0 IS the background's, at the same cosmic time; the separation is a late
    # feature of a history that starts with the ambient universe's.  So the apparatus is not
    # reinstated and this ground is not available either: what the two revisions bracket is the
    # unposed question about the construction's recursion. **
    ("the-full-lap-is-unphysical-because-the-ball-separated",
     r'(its past \$?a\s*=\s*0\$? is a mathematical extension'
     r'|not an epoch it lived through'
     r'|there is (?:no|only one) periodic map'
     r'|the ball separated, turned around and collapsed'
     r'|extending the closed-dust solution back(?:wards)? to \$?a\s*=\s*0\$? is)',
     r'(withdraw|WITHDRAWN|struck|STRUCK|c54\.150|c54\.151|spherical collapse'
     r'|the ambient universe\'s own beginning|the background\'s \$?a\s*=\s*0'
     r'|does not hold|too confident)',
     "withdrawn r2376+c54.150 (c54.149's ground, not the withdrawal it supported); registered c54.151"),

    # r2376+c54.146, registered c54.151.  THE SCALAR MONODROMY AS 2 pi/rho.  c54.131 computed the
    # crunch off-diagonal on z ~ a and the corpus carried the result for the scalar sector; the
    # true hydrodynamical variable z_S = a(a + 2B/3)/a' doubles it to 4 pi/rho.  ** 2 pi/rho is
    # CORRECT for tensors (z_T = a M_Pl/2 exactly, any content), so this pattern is written to
    # fire only where the sector is not named -- a correct statement of the value always says
    # 'tensor', or states the doubling, within the window. **
    ("the-monodromy-is-two-pi-over-rho-for-scalars",
     r'(the mixing is \$?2\\?pi ?[i]?/?\\?rho'
     r'|the mixing is 2 ?pi ?/ ?rho'
     r'|off-diagonal (?:is )?\$?-?2\\pi i/\\rho'
     r'|monodromy (?:is|of) \$?-?2\\pi i?/\\rho)',
     r'(tensor|4\\pi|4 ?pi|twice the tensor|doubl|z_T|z_\{?T\}?|scalar off-diagonal'
     r'|withdraw|WITHDRAWN|c54\.146|c54\.151)',
     "corrected r2376+c54.146: 2 pi/rho is the TENSOR value; the scalar is 4 pi/rho; registered c54.151"),

    ("radiation-of-order-the-matter-density-is-natural",
     r'(radiation of order the matter density'
     r'|of order the matter density is the natural'
     r'|matter density is the natural scale'
     r'|order unity,? (?:and )?not the small tuned value'
     r'|the small tuned value \\?\$?\\eta\\?\$? takes'
     r'|a handover carrying radiation of order)',
     r'(should be withdrawn|withdrawn|it is tempting to read|runs the other way'
     r'|no head start|superseded|struck r\d+|does not support|nine orders)',
     "withdrawn r2376+c54.105 by P15 sec:tensions: rho_r = rho_m at T ~ 0.8 eV, nine orders below "
     "the handover; O(1) there would mean eta ~ 0.5.  The corrected accounting is in P15 and P7."),
    # r6893+cc66.37.  "THE FREE-STREAMING PHASE SHIFT IS UNIFORM ACROSS THE FIRST FOUR PEAKS".
    # `r6889+cc66.36` built `NUFS`, measured the peak shift at +9 on both arms, and gated it as
    # UNIFORM -- "which is what a PHASE shift looks like as against a rescaling of the acoustic
    # scale".  ** The peak positions it compared were quantised to the l grid, and the tolerance was
    # 0.05 on integers that could only differ by a whole bin. **  Located sub-bin, by a parabola
    # vertex and again by an envelope-normalised cross-correlation, on both arms and at four times
    # the multipole resolution, the shift RISES monotonically with l -- about +3 near the first peak,
    # about +12 by l ~ 1500.  ** The uniformity was the grid. **  The SIGN and the existence of the
    # shift stand; its uniformity does not.  \u2317 *The phrase may still be quoted -- this registry
    # exists so that quoting it stays visible -- but not asserted.*
    ("the-free-streaming-shift-is-uniform-across-the-first-four-peaks",
     # ** WIDENED IMMEDIATELY, AND FOR THE REASON THE ENTRY TWO ABOVE RECORDS. **  The first
     # pattern was keyed to MY OWN wording, "uniformly across the first four" -- and `P15`
     # \S`sec:neutrinos` says "every peak on both arms moves to larger multipole by the same
     # amount across the first four".  The gate reported the tree clean with the corrected
     # claim standing in the paper, which is the same defect r6881 records one entry up:
     # ** a registry keyed to one seat's phrasing is a registry that checks one seat. **
     r"(?:UNIFORM|uniform(?:ly)?) across the first four"
     r"|by the same amount across the first four"
     r"|moves? to larger multipole by the same amount"
     r"|phase shift[^.\n]{0,60}is uniform",
     # ⌗ NARROW ON PURPOSE.  Every text that carries this claim ALSO hedges its SIZE as
     # "grid-limited" or "one binned grid step" -- and that hedge is about the size, not about
     # the uniformity, so accepting it as the marker would let the withdrawn half stand.
     r"(?:r6893|withdrawn|WITHDRAWN|CORRECTED|corrected|not uniform|NOT uniform"
     r"|grows with|rises with|rises monotonically|not a constant|not constant"
     # ⌗ AND THREE MORE, BECAUSE THE MARKER SET WAS TOO NARROW FOR A PARAGRAPH WHOSE SUBJECT
     # IS THE WITHDRAWAL.  `FOR_CC66`'s `r6895` block quotes the claim in the course of
     # striking it -- "the vacuous gate reached the corpus", "the gate could not express the
     # difference it tested", "both clauses are out of P15" -- and names the revision that
     # LANDED it rather than the one that took it out, which is the right thing for an order
     # log to do.  ** A correction stated in its own words is still a correction; requiring
     # the word "withdrawn" would be requiring a vocabulary, not a caveat. **
     r"|vacuous gate|could not express the difference|clauses are out of)",
     "corrected r6893+cc66.37; sub-bin the shift grows with multipole and is not a constant"),
]

SKIP = ('appendix_receipts',)

# --- THE NUMERIC REGISTRY, r6907 ------------------------------------------------------------
# (label, value pattern, filename filter or None, what replaced it and where)
#
# ** WHY THIS SITS HERE AND NOT IN A GATE OF ITS OWN. **  It is the same failure as the phrase
# registry above with a different key: a result lands in the section that produced it and the
# OLD VALUE stays live in the documents that summarise.  A cold full-corpus read found sixteen
# such occurrences across five documents in one pass -- a retired driving figure live in two
# papers while a third measured it, an ontology card carrying four superseded numbers with one
# of them SIGN-REVERSED, a damping signature quoted at eight times its size, and a readings
# count that double-counted an identity.  *** None of it is visible from inside any single
# paper, which is exactly why no instrument was looking. ***
#
# ⚠ ** AND THE SEMANTICS ARE STRICTER THAN THE PHRASE REGISTRY'S, FOR A REASON THE CORPUS
# ITSELF SUPPLIES. **  A withdrawn CLAIM may be quoted honestly, so that registry allows a bare
# occurrence when an adjacent correction follows.  A superseded NUMBER has no such form: a paper
# presents one state and never reports its own computational corrections, so a retired value in
# a live document is a plain failure.  ** There is no adjacent-marker escape here. **
#
# ⌗ WHAT IS NOT SCANNED, AND WHY THAT IS NOT A LOOPHOLE.  The changelog, the register, the
# receipts and retired/ are RECORDS -- history is what they are for, and a retirement is
# recorded by naming the number it retired.  Only the live documents are scanned: the papers
# and the ontology index.
#
# ⌗ EVERY ENTRY BELOW WAS CALIBRATED BOTH WAYS BEFORE IT WAS ADDED: each pattern was run
# against the tree as it stood before the correcting revision, where the ten of them return
# SIXTEEN hits across five files, and against the corrected tree, where they return none.
# ** A pattern that has never been seen to fire is not an instrument. **
NUMERIC = [
    ("driving-2.4-times", r'times as far as it does on the', None,
     "r6899: the collapse-side driving measured by subtraction is 0.1717 against the control's "
     "0.1792 -- within four per cent and SLIGHTLY WEAKER rather than stronger.  The retired form "
     "read '2.4 times as far ... overshooting rather than falling short' and stood in two papers "
     "while a third measured it; P15's own receipt marks it retired by name."),

    ("damping-theta-ratio-1.08", r'\\approx\s*1\.08\\,\(\\theta_D', None,
     "r6899: theta_D/theta_* is under a per cent at the adjudicated endpoint, its size fixed by "
     "the handover and its sign by the common endpoint both lengths are carried to.  The 1.08 was "
     "the product of two conventions the construction no longer has -- a stacking clock for r_D "
     "and an r_s truncated at a fitted onset."),

    ("damping-9-per-cent", r'9\\%\$\s*CR-specific diffusion', None,
     "r6899: same retirement, in the form the summary carried it.  The 9% was the pinned "
     "configuration's, and the pin is gone."),

    ("H0-68.5", r'68\.5(?!\d)', ('CR_cosmology', 'ONTOLOGY_FOUNDATION_INDEX'),
     "the joint fit returns H_0 = 68.6; six sites carried it against two, including both "
     "receipted ones.  Filtered to the two documents that quote it, since 68.5 is an ordinary "
     "number elsewhere."),

    ("radius-read-seven-ways",
     r'read seven ways|seven distinct ways|seven independent idioms|'
     r'seven readings of that one radius', None,
     "r6901: the readings of r^3 = M alpha^2 are SIX.  The flat locus of the slice's curvature "
     "and the areal acceleration changing sign are one fact in two languages -- "
     "d2r/dtau2 = -f'/2 = r K_G by differentiating f -- and were counted twice.  ** The "
     "maximal-symmetry-worn-seven-ways count is a DIFFERENT seven and must keep working: that is "
     "why this pattern is a list of the four literal forms the radius count used and not the "
     "word 'seven'. **"),

    ("amplitude-ladder-eighteen", r'eighteen orders separate', None,
     "r6901: TEN orders separate the substrate's vacuum from the progenitor's amplified one.  The "
     "transfer law already carries the crunch mixing, so the amplification is the rho^-6 and not "
     "a second factor on top of it; the two-step ladder double-counted."),

    ("peak-heights-below-the-sky", r'20\.7\\?%\s*and\s*29\.2', None,
     "r6899: the height ratios are 2.264 and 2.298 against the sky's 2.217 and 2.277 -- i.e. 2.1% "
     "and 0.9% ABOVE.  The retired form said twenty and twenty-nine per cent BELOW.  ** A "
     "sign-reversed number in the card a node reads to orient. **"),

    ("chi2-397-over-206", r'397\.13', None,
     "the like-for-like refit reports 550.5/214.1 on 185 bins, 556.7/279.4 on 133, and 1.58/1.01 "
     "per bin refitted.  The 397.13/206.44 pair belonged to a different instrument's arm and "
     "matches none of them."),

    ("lowell-depths-0.49-0.44", r'0\.49\$ and \$0\.44', None,
     "the low-multipole depths are 0.47 and 0.41 at ell = 2 and 3, on three body sites and the "
     "ontology index; one abstract site carried the older pair."),

    ("landing-the-sixteen", r'the sixteen|all 16 rounds', ('geometric_core_paper',),
     "the landing section enumerates SEVENTEEN companions and the header repeated the miscount.  "
     "** A COUNT IS A VALUE, AND THIS IS WHY COUNTS ARE REGISTERED HERE RATHER THAN IN A GATE OF "
     "THEIR OWN. **  A checker that reads a number-word before a list was built and MEASURED at "
     "r6907 and does not work: at the window that catches this instance -- the count sits a hundred "
     "characters back, behind a dash and a comma -- it returns six false positives in seven, firing "
     "on 'gathered in one place', 'that one map', 'the three parametrisations'; at the window with "
     "no false positives it catches neither this instance nor the readings count, which was in prose "
     "with no list at all.  *** Proximity does not separate a count from any other number in the "
     "lead-in, so the instrument was withdrawn rather than allowlisted green. ***  What is left is "
     "the shape the failure actually has: the same miscount in a body and a header while the list "
     "disagrees, which is a superseded VALUE in two documents -- exactly this registry's job."),

    ("dlnL-over-ell-8", r'\+1\.6\$? over \$?2\\le\\ell\\le8', None,
     "Delta(-2 ln L) = +1.8 over 2 <= ell <= 10, on four sites including the canon header.  No "
     "body passage supports +1.6 or the ell <= 8 range."),
]


# --- SECOND SCOPE, added the same revision it was needed -------------------------------------
# The gate began by scanning the PAPERS.  Run on the standing registers it immediately found the
# same withdrawn claim live in five forward-facing documents -- so a withdrawal that reaches the
# papers and not the registers is the failure one layer over, and the registers are what a
# working node reads to decide what to do next.
#
# HISTORICAL documents are exempt BY NAME and only by name: a fork record or a build ledger is a
# record of what was believed at the time, and rewriting it would destroy the record.  Everything
# else is forward-facing and must carry its correction.
REGISTER_DIR = os.path.abspath(os.path.join(HERE, '..'))
HISTORICAL = {
    'FORK_c54.md',                 # the fork's own running record
    'PHASE7_BUILD_LEDGER.md',      # a build ledger: what was believed while building
    'THE_LIVE_ARC.md',             # the arc records the withdrawal and its history
    'THE_BASE_RATE.md',            # the failure ledger, which must quote the failures
    'CORPUS_MAP.md',               # a map of the corpus's own text, quoting it
    'THE_FERMION_SECTOR_GEOMETRY.md',   # states the conflict that produced the withdrawal
    'MATTER_SECTOR_germ.md',       # the sector's germ: what was believed when it was seeded
    'THE_ARSENAL.md',              # a worked-items record
    'THE_RECEIPT_AUDIT.md',        # an audit of receipts as they stood
    'A5_fermion_sector_build.md',  # a build record: what was believed while the sector was built
}


# --- THE SELF-TEST, added r2376+c54.151 --------------------------------------------------------
# ** A GATE THAT HAS NEVER FAILED IS NOT EVIDENCE THAT IT WORKS. **  Three of the six registry
# entries below were added after the claims had already been struck from the corpus, so on the
# current tree they match nothing -- and a pattern that matches nothing is indistinguishable from
# a pattern that is broken.  Each entry therefore carries a KNOWN-POSITIVE string, taken verbatim
# from the text the withdrawal removed, and this gate fails if any pattern stops matching its own.
POSITIVES = {
    # r6893+cc66.37: both forms cc66.36 used -- the gate's own name and the summary line.
    "the-free-streaming-shift-is-uniform-across-the-first-four-peaks": [
        "...and it is UNIFORM across the first four peaks on both arms, which is what a PHASE ",
        "pushes every peak on both arms to LARGER multipole, uniformly across the first four, which is what",
    ],
    "dirac-sector-not-yet-on-the-chiral-member": [
        "the propagating Dirac sector is built on the unpolarised member and not yet on the chiral one",
        "and not yet on the chiral member the projection would act on",
    ],
    # the two real pre-r6475 forms: the generator header and the reader-facing line.
    "the-papers-are-served-from-a-cdn": [
        "The PDFs are served from jsDelivr, a CDN over the",
        "Papers via jsDelivr; the frontier read live at page load.",
    ],
    # the three forms the corpus actually used, taken from the pre-r6425 text of P13
    # sec:wall and its abstract, so the pattern is proved against what it was written for.
    "the-compact-face-sector-is-vector-like": [
        "A geometric, isometry-realized fermion sector there is therefore vector-like",
        "rendering the geometric fermion sector vector-like",
        "that index makes the spectrum vector-like",
    ],
    "generations-are-the-hinges": [
        "the generations are \\emph{one object read three ways}",
        "a generation per hinge",
    ],
    "the-full-lap-floquet-apparatus": [
        "the per-cycle map is a Floquet problem",
        "every physical mode lies in a stability band and $|\\lambda|=1$ to machine precision",
        "because the interior is a complete cycle with a branch point at each end",
        "Propagating the Frobenius basis across a full cycle",
        "here the cyclic structure of the excursion",
    ],
    "the-leaked-branch-knee-and-the-five-composition-bounds": [
        "so that the spectrum acquires a knee",
        "which bounds the progenitor's radiation fraction at maximum expansion",
        "THE PROGENITOR'S RADIATION FRACTION IS NOW BOUNDED FROM BOTH SIDES",
    ],
    "the-full-lap-is-unphysical-because-the-ball-separated": [
        "Its past $a=0$ is a mathematical extension of the closed-dust solution "
        "backwards, not an epoch it lived through.",
        "with one branch point there is no periodic map",
    ],
    "the-monodromy-is-two-pi-over-rho-for-scalars": [
        "the mixing is 2 pi / rho, and it is discontinuous at zero radiation",
        "the resulting monodromy is unipotent with off-diagonal $-2\\pi i/\\rho$",
    ],
    "the-shared-fraction-attributes-the-misfit-to-the-transfer": [
        "On the order's own criterion that part is the transfer's and not the construction's.",
        "So three quarters of the disagreement is the transfer's and not the construction's.",
        "the residuals are where the rejection lives, and three quarters of this arm's is the "
        "control's",
        "73.1\\% of the arm's residual is the control's",
        "73.1\\% of the arm's chi^2 lies along the control's own direction, so that part is the "
        "transfer's",
    ],
    "radiation-of-order-the-matter-density-is-natural": [
        "radiation of order the matter density",
    ],
}


def selftest():
    """Every registered pattern must still match the text its withdrawal removed."""
    bad = []
    for label, phrase, _marker, _prov in REGISTRY:
        pat = re.compile(phrase, re.I)
        cases = POSITIVES.get(label)
        if not cases:
            bad.append((label, "<no known-positive registered>"))
            continue
        for c in cases:
            if not pat.search(c):
                bad.append((label, c))
    print(f"  SELF-TEST -- {sum(len(v) for v in POSITIVES.values())} known-positive string(s) "
          f"across {len(REGISTRY)} registered withdrawal(s)")
    if bad:
        print("  ⛔ A REGISTERED PATTERN NO LONGER MATCHES THE TEXT IT WAS WRITTEN FOR:")
        for label, c in bad:
            print(f"     [{label}] {c[:100]}")
        print()
        return 1
    print("  every pattern still fires on its own known-positive.")
    print()
    return 0


def strip_comments(text):
    return '\n'.join(l for l in text.split('\n') if not l.lstrip().startswith('%'))


def main():
    texs = [t for t in sorted(glob.glob(os.path.join(HERE, '*.tex')))
            if not any(k in os.path.basename(t) for k in SKIP)]
    # ** r6477: THE MACHINERY IS SCANNED TOO, not only the papers. **  A withdrawn claim
    # about HOW THE PIPELINE WORKS lives in a module header or a page template, and this
    # gate was reading neither -- so "the PDFs are served from jsDelivr" stood in a
    # generator header and on the live page after the code stopped using it (r6475), and
    # "the frontier is generated from THE_REGISTER, which is the one source" stood while
    # the runway was a frozen table (r6473).  ** Two header-versus-body divergences in one
    # file in three revisions, and no instrument was looking at headers at all. **
    #
    # ⌗ WHY HERE AND NOT IN A NEW GATE.  A name-based check on headers was MEASURED first
    # and does not work: a CORRECTED header names the wrong thing in order to record the
    # correction, so it fires on the repairs as readily as the defects -- 21 file hits and
    # 23 constant hits, nearly all false, and the one host hit was a correction record.
    # ** That is precisely the problem this gate already solves: the corpus may QUOTE what
    # it withdrew, it may not ASSERT it. **  So the machinery joins the scan rather than
    # getting a fifth instrument that would have to learn the same lesson.
    machinery = [m for m in sorted(
        glob.glob(os.path.join(HERE, '..', 'scripts', '*.py'))
        + glob.glob(os.path.join(HERE, '..', 'BOOK_INTRO_cosmiCave', '*.html')))]
    texs = texs + machinery
    print()
    print(f"  WITHDRAWN-CLAIM SCAN -- {len(REGISTRY)} registered withdrawal(s) "
          f"x {len(texs)} paper(s)")
    print()
    if selftest():
        return 1
    bare = []
    quoted = 0
    for label, phrase, marker, prov in REGISTRY:
        pat = re.compile(phrase, re.I)
        mrk = re.compile(marker, re.I)
        print(f"  ** {label} ** -- {prov}")
        for t in texs:
            body = strip_comments(open(t, encoding='utf-8', errors='replace').read())
            hits = list(pat.finditer(body))
            if not hits:
                continue
            ok = sum(1 for m in hits if mrk.search(body[m.end():m.end() + WINDOW]))
            quoted += ok
            n_bare = len(hits) - ok
            flag = '' if not n_bare else '   <-- BARE'
            print(f"     {os.path.basename(t):<34} {len(hits):>3} hit(s), "
                  f"{ok:>3} corrected{flag}")
            for m in hits:
                if not mrk.search(body[m.end():m.end() + WINDOW]):
                    ctx = body[max(0, m.start() - 90):m.end() + 90].replace('\n', ' ')
                    bare.append((os.path.basename(t), label, ctx))
        print()

    # --- the same scan over the forward-facing standing registers ---------------------------
    import glob as _glob
    regs = [r for r in sorted(_glob.glob(os.path.join(REGISTER_DIR, '*.md')))
            if os.path.basename(r) not in HISTORICAL]
    print(f"  STANDING REGISTERS -- {len(regs)} forward-facing document(s) "
          f"({len(HISTORICAL)} exempt as historical records)")
    # ** THE ROW IS THE UNIT IN A TABLE, added r2376+c54.151. **  The 900-character window is the
    # right scope for prose and the WRONG one for a markdown table: at c54.149 a withdrawal struck
    # ONE row of THE_WORK's closure table and left three others standing on identical grounds, and
    # every one of those three passed this gate because the struck row sat within the window.  So
    # when a hit lands on a table row -- a line beginning with '|' -- the correction must be in
    # THAT row.  *A row rests on grounds, not on its neighbours.*
    for label, phrase, marker, prov in REGISTRY:
        pat = re.compile(phrase, re.I)
        mrk = re.compile(marker, re.I)
        for r in regs:
            txt = open(r, encoding='utf-8', errors='replace').read()
            for m in pat.finditer(txt):
                ls = txt.rfind('\n', 0, m.start()) + 1
                le = txt.find('\n', m.end())
                le = len(txt) if le == -1 else le
                if txt[ls:ls + 1] == '|':
                    scope = txt[m.end():le]          # the rest of this table row only
                else:
                    scope = txt[m.end():m.end() + WINDOW]
                if not mrk.search(scope):
                    ctx = txt[max(0, m.start() - 90):m.end() + 90].replace('\n', ' ')
                    bare.append((os.path.basename(r), label, ctx))
    print()

    # --- THE NUMERIC PASS, r6907 ------------------------------------------------------------
    # ** No adjacent-marker escape, and the scope is the LIVE documents only. **  The records --
    # the changelog, the register, the receipts, retired/ -- are where a retirement is written
    # down by naming what it retired, so scanning them would fire on every correction.
    live = [t for t in sorted(glob.glob(os.path.join(HERE, '*.tex')))
            if not any(k in os.path.basename(t) for k in SKIP)]
    live.append(os.path.join(REGISTER_DIR, 'ONTOLOGY_FOUNDATION_INDEX.md'))
    print(f"  SUPERSEDED-VALUE SCAN -- {len(NUMERIC)} retired value(s) x "
          f"{len(live)} live document(s)")
    print()
    stale = []
    for label, pattern, only, prov in NUMERIC:
        rx = re.compile(pattern)
        # ⌗ A pattern that cannot match anything is a silent gate, so the selftest below
        #   requires each to have been calibrated; here we only guard the obvious degenerate case.
        if rx.search(''):
            print(f"  [FAIL] {label}: the pattern matches the empty string and would fire on "
                  f"everything.")
            return 1
        for t in live:
            base = os.path.basename(t)
            if only and not any(k in base for k in only):
                continue
            # ** HEADERS ARE SCANNED HERE, comments and all, and the phrase registry's own
            #   r6477 note is the precedent: a canon header is what a node reads to orient, so
            #   a superseded value in one is read by every seat that spins up on it.  Two of the
            #   staleness instances found in this sweep were in headers.  ** Measured before
            #   being adopted: scanning raw rather than stripped adds no hit on the clean tree. **
            body = open(t, encoding='utf-8', errors='replace').read()
            for m in rx.finditer(body):
                ctx = body[max(0, m.start() - 110):m.end() + 110].replace('\n', ' ')
                stale.append((base, label, prov, ctx))
    if stale:
        print(f"  ⛔ {len(stale)} SUPERSEDED VALUE(S) LIVE IN A PAPER OR THE INDEX.")
        print(f"     ** A paper presents one state and never reports its own corrections, so a")
        print(f"     retired number has no honest bare form here. **")
        print()
        for f, label, prov, ctx in stale:
            print(f"     [{f}] ({label})")
            print(f"        ...{ctx}...")
            print(f"        what replaced it: {prov}")
            print()
        print("  Fix by carrying the current value, not by annotating the old one.")
        return 1
    print(f"  No superseded value is live.  ⌗ A retirement is not finished until its value is")
    print(f"  in this file's NUMERIC registry -- that is the half a cold read had to do by hand.")
    print()

    if bare:
        print(f"  ⛔ {len(bare)} BARE OCCURRENCE(S) -- a withdrawn claim stated with no adjacent")
        print(f"     correction.  The corpus may QUOTE what it withdrew; it may not ASSERT it.")
        print()
        for f, label, ctx in bare:
            print(f"     [{f}] ({label})")
            print(f"        ...{ctx}...")
        print()
        print("  Fix by stating the revision beside the phrase, or by rewording the phrase.")
        return 1

    print(f"  No bare occurrences.  ({quoted} quotation(s) of withdrawn wording, each carrying")
    print(f"  an adjacent correction -- which is the honest form and is why this gate does not")
    print(f"  simply ban the words.)")
    print()
    print("  ⌗ A withdrawal is not finished until its phrase is in this file's REGISTRY.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
