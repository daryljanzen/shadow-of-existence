#!/usr/bin/env python3
"""regen_frontier.py -- writes THE_FRONTIER.md: the one board Daryl reads every turn.

** WHAT IT IS FOR. **  *** Ten open problems, in dependency order, each with: what it is, how many steps
to close, where it stood LAST revision, whether its runway is clear, and what must be cleared first.
** The overall and the breakdown, on one screen. ** ***

** THE ESTIMATES ARE STORED HERE AND EDITED BY HAND ** -- *** they are judgements, not measurements, and
the file records them so the CHANGE is visible turn to turn.  A step is one worked result, not one turn;
turns-per-step is the separate estimate. ***

    python3 scripts/regen_frontier.py
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(ROOT, 'THE_FRONTIER.md')

# ** id: (short name, steps-left, steps-last-revision, turns-per-step, gate, runway note) **
EST = {
    'PO-13': ('the handover datum, and the rigid phase split beneath it', 1, 1, 6, None,
        'r4519: the candidate mechanism is that the modes are driven twice, on the collapse leg and again on the leaf, which gives the direction, the ordering with peak number and the overshoot together. THE CHECK ON IT CAME BACK NEITHER BRANCH. The transfer never integrates the collapse leg -- it enters as a three-number handover per mode, and THE TWO HALVES ARE READ AT DIFFERENT POINTS OF IT: the photon amplitude carries the closed-form transfer and the potential is left at its primordial value, so the expanding-leg driving is re-applied from a potential already spent. Carrying the decay across does not halve the driving, it doubles it again to 5.14x the control; reading both halves at one point kills the comb. Three codings, three answers, so THE FACTOR OF 2.4 IS A PROPERTY OF THE CHOICE AND NOT YET OF THE CONSTRUCTION. The mechanism is not refuted -- the instrument cannot weigh it. AND BENEATH ALL OF IT: undriven, this arm sits at 1.1273 of the acoustic scale and the control at 0.9158, on opposite sides of the adiabatic value, a 23 per cent split no account of the driving can produce. r4527 LOCATES THE SPLIT: measured without the peak-finder, both arms turn over at exactly one half-period undriven -- control 0.9989-1.0009, the arm 0.9989-1.0001 -- so the oscillator is excluded and the split is not in the acoustic phase or the sound-horizon bookkeeping. And every available change to the handover moves the arm the WRONG way, so the handover is excluded too. THE SPLIT IS IN THE PROJECTION: both arms would sit at unity if the projected peak sat at the sources turnover, and the control lands 8.4 per cent below while the arm lands 12.7 above -- what differs is what rides with the monopole into the source, the potential, integrated and Doppler terms, which the two arms do not carry alike. r4535: THE SUBTRACTION IS DONE AND IT IS NONE OF THE THREE. Removing the integrated term WIDENS the split to 29.4 per cent, the Doppler term leaves 23.8, the monopole leaves 27.5, and switching the diffusion damping off entirely widens it to 26.0. The split never collapses, so what sets the undriven position is common to all three sources and to the envelope. TWO FRAMINGS DISSOLVE: opposite sides of the adiabatic value is a property of the baseline and not of the split, since with the monopole removed both arms sit above it and the split stands; and the ratio is far steadier than its parts, 1.23 to 1.29 across configurations whose peak positions move by up to 30 per cent. DISCHARGED BY: the projection kernel -- the visibility function -- which is the next discriminator; and separately a statement of what the photon perturbation and the potential both are at ONE locus.',
        ),
    'PO-36': ('does the Hubble-Eddington radius track the dynamical mass or the baryonic one', 1, 0, 4, None,
        'r4207 NAME GUARD: the standard literature calls this radius a maximum TURNAROUND radius; in this corpus TURNAROUND is the comoving turnaround, where the worldline turns at r = -(2M alpha^2)^(1/3) on the conjugate leg -- a different locus, and their word is used only in reporting their result. The radius is derived in the standard framework and proposed there as a '
        'local test of Lambda, with the same M^(1/3) scaling this construction gives, so the two are '
        'DEGENERATE on the radius. The circularity is in how the test has been run: the N-body calibrations '
        'are dark-matter-only and the observational masses are dynamical, so which mass sets it is assumed '
        'rather than measured. Discharged by the radius measured against independently measured BARYONIC mass. '
        'Held at weight: a baryonic-set radius is smaller, which is the OPPOSITE direction from the '
        'dark-matter evidence, so this is a discriminating measurement and not a dark-matter explanation'),
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
        'r3882: P08 sec:open states it and no register row carried it. The bend-density identity is EXACT but it '
        'states WHAT the bend is, not WHY a cut bends as it does: the slicing operator is KINEMATIC, generating the '
        'stress-energy from the curve and not the curves own dynamics. P08 narrows it sharply and the narrowing is '
        'the papers own -- the confined case IS exhibited; the boundary at which free radiation begins IS the range '
        'papers wall, and beyond it the framework leaves GR UNCHANGED so the general inhomogeneous evolution is '
        'ordinary leaf evolution with its canonical form in P10; and the branch-point crossing IS well posed, with '
        'the worldline taken up in P16. What is left after all of that is one thing: the matter contents own '
        'generative law where the construction does not supply one, a dynamics for the curve itself as against the '
        'ordinary leaf evolution that carries it -- which P08 calls the distinction between a complete dynamical '
        'theory and a kinematical one, and the deepest question this construction opens onto. ITS LEDGER ROW '
        '11b0140039 POINTED AT PO-6 SINCE r2581, and PO-6s object is the interacting quantum tower: a classical '
        'dynamics gap routed to a quantum item, which is why nobody could work it. THE ESTIMATE IS A FLOOR, scored '
        'as a build because nothing smaller has been identified, not because a route is known.'),
    'PO-31': ('the progenitor spectrum -- DERIVE eta AND THE ONSET', 1, 1, 6, None,
        'r3969: family 3 of THE_OPEN_PROBLEMS_LEDGER, and P15 calls it THE GENUINE FRONTIER as against its '
        'buildable debts. PO-16 is struck and its own text names this as what stays open beyond the strike, so the '
        'object was correctly identified and unregistered since r3012. The strike is sound and is why this is a '
        'frontier rather than a gap: the infall thermalizes four orders above the deuterium bottleneck so the '
        'progenitors composition is ERASED and the abundances are synthesized in the window, while BARYON NUMBER '
        'survives because no dissociation destroys it. So eta is inherited because a conservation law protects it '
        'and the abundances are predicted because none protects them. AND THAT CONSTRAINS THE DERIVATION IN KIND: '
        'it must reach a CONSERVED CHARGE of the progenitor, not a thermal history. P16 has already excluded one '
        'mechanism -- the Euclidean action is odd under the standing conjugation so the two branches carry equal '
        'and opposite action, the balance exact rather than approximate.'),
    'PO-25': ('the charged bead -- DOES A CHARGED COLLAPSE FORM THE CAUCHY HORIZON', 1, 1, 4, None,
        'r3827: P03 states the obstruction exactly -- with Q nonzero, Q^2/r^2 dominates as r -> 0 so f -> +inf '
        'rather than -inf, an inner Cauchy turning point appears, and r=0 becomes a TIMELIKE RN singularity '
        'rather than the branch point through which the signed radius passes to the conjugate branch. So the '
        'cosmogenetic loop has no branch point to close through when the collapsing matter carries charge. And '
        'the limit is SINGULAR: r_inner = M - sqrt(M^2 - Q^2) -> Q^2/2M shrinks to zero as Q^2, but at ANY Q>0 '
        'the origin is timelike and only at Q=0 exactly is it a branch point -- the bead closes on a set of '
        'measure zero in Q. P03s charged case is the ETERNAL RN-de Sitter geometry, stationary; PO-13s object is '
        'the DYNAMICAL collapse. The question is whether a charged collapse forms the eternal inner horizon at '
        'all, real collapses being widely held not to, in which case the branch point survives dynamically and '
        'the charged case rejoins the bead. HANDS OFF TO PO-13 IN THAT LIMIT. And the arbitrariness objection '
        '-- that a loop closing only at Q=0 exactly is a flatness problem in other clothes -- is answered '
        'structurally rather than numerically: the sub-Planckian answer is FALSE at cosmological scale, since on '
        '1e80 baryons even the lab bound 1e-21 on |q_p+q_e|/e gives 1e59 net charges and an inner horizon near '
        '1e19 m. The progenitor is ORDINARY MATTER and ordinary matter is neutral because it is made of atoms, so '
        'Q=0 is inherited from the content rather than imposed on the geometry.'),
    'PO-24': ('whether the tilt displacement is a tension', 1, 1, 5, None,
        'r4505 NARROWED -- the computation is done and the verdict is neither of the two expected. A refit of amplitude and tilt absorbs the signature almost entirely in SHAPE, 0.26 per bin over the 185-bin ceiling and less the higher one looks, because over a restricted high-ell range a Gaussian in ell is well approximated by a power law. THE ABSORPTION COSTS a tilt shift of -0.0304 against sigma = 0.00323 from the same covariance that scores the fit, so the signature does not vanish -- it relocates into an inferred parameter. THE EARLY-ISW LEG IS ANSWERED AND SMALL: 0.77 sigma per bin over 700-1296 against 3.49 over 100-1296, so the term the row named as one of two things the answer turns on does not reach the multipoles in question. BOUNDS THAT TRAVEL WITH IT: the shape residual IS an upper bound; the tilt displacement is NOT, since more parameters would share it; and the magnitude is not robust to a factor of three between the data-shape and in-source routes, stated at the weaker bound with closing the factor named as work not done. DISCHARGED BY: whether a displacement of that size in the inferred tilt is a tension, which is a joint fit and is the whole of what remains.',
        ),
    'PO-44': ('is the tower boundary condition helicity-blind', 1, 1, 5, None,
        'r4547 OPENED as the single marked step in PO-43s chirality verdict -- one check, and it closes or opens the parity-odd question outright. The parity-odd entry rested on two independent failures and THE FIRST IS REMOVED: the tower IS chirally capable, its two helicities being inequivalent representations of the connected isometry group exchanged only on the disconnected component. So the second stands alone -- a counterterm answers to the effective action and the effective action to THE STATE. THE CHECK: P10s boundary condition is Hartle-Hawking regularity imposed fibre by fibre, and does its statement anywhere distinguish the self-dual from the anti-self-dual tower? If not, the two are populated alike, the parity-odd content cancels, and the question closes BY THE STATE AND NOT BY THE GEOMETRY -- a different closure from achirality and not to be read as one. If it does, the chirality reaches the state and the entry is owed. DISCHARGED BY: a reading of the conditions own statement in P10, identified as directly checkable and not yet run.',
        ),
    'PO-43': ('the Weyl-squared coefficient at second order in the shear', 1, 1, 5, None,
        'r4543 OPENED. P10 carries the whole chain and names the entry: the three quadratic invariants collapse to two, the R-squared term at second order is a multiple of Einstein-Hilbert for a transverse-traceless perturbation, Gauss-Bonnet contributes no field equation, and THE SHEAR COSTS EXACTLY ONE NEW COUNTERTERM AND IT IS THE WEYL-SQUARED ONE. So the ledger acquires that entry and the question is at what coefficient. AND PO-23s zeta(0) IS NOT THAT COEFFICIENT: the background is conformally flat so the Weyl-squared invariant vanishes identically on it, and a background computation cannot see the counterterm at all -- what was measured is the log on the degenerate combination. The entry lives at SECOND ORDER in the mode amplitude where the shear is the propagating content. NO COLLISION with the ghost-free result, which P07 scopes as classical in the sentence that states it. A SECOND POSSIBLE ENTRY is chirality-tied and unworked: the Pontryagin density is non-zero at second order for a circularly polarised mode, so whether a parity-odd entry is owed depends on the towers polarisation, on which the corpus has a position in the matter sector. r4545: THE PARITY-ODD SECOND ENTRY IS NOT OWED ON PRESENT GROUNDS, and the tempting chain fails at two separate joins. The five faces give a Z_2 exchanging the helicities and grading fermion chirality, but a map that exchanges two things is a grading and every parity-even theory has one; the corpus own criterion is that NO CONNECTED ACTION COMPLETES the reflection, applied to the radiating sector and never to this tower. And independently, a counterterm answers to a parity-odd divergence of the EFFECTIVE ACTION and not to a basis mode, so a mode-level evaluation cannot fix it in either direction -- P10 caveat bounds its own instrument. AND EVEN IF OWED IT IS A DIFFERENT KIND OF THING: the density is a total derivative contributing no field equation, so whether it is a ledger entry is a question about whether the audit counts topological terms. TWO INDEPENDENT QUESTIONS REPLACE IT: whether a connected isometry of the closed layer identifies the two helicities of an S3 tensor harmonic, and whether the ledger counts topological terms. DISCHARGED BY: the Weyl-squared coefficient at second order in the shear with the sub-leading heat-kernel coefficients, which is the instrument P10 names and stopped short of running.',
        ),
    'PO-23': ('the mode sums beyond the free static case', 1, 1, 5, None,
        'r4537: THE NUMBER IS COMPUTED AND IT IS NOT ZERO. On the towers own spectrum -- eigenvalues n(n+2)-2 with degeneracy 2(n-1)(n+3), which P10 derives from Peter-Weyl rather than importing -- the spectral zeta at zero is 10 EXACTLY, the asymptotic series terminating at s=0 so it is an identity and not an estimate; and the zero-point sums log-scale coefficient is the residue, 39/4. THE TOWERS AND NOT THE SCHEMES: a hard cutoff with no zeta function in it returns 9.749 against 39/4, and 39/4 is independently the 1/m coefficient of the summands own expansion -- two regulators sharing no machinery agreeing to a part in ten thousand. SO THE MODE SUMS SPEND ONE DIMENSIONLESS CONSTANT, and the no-free-constants claim carries the scoping its own frontier sentence names. AND THE COST WAS ALREADY NAMED: the logarithmic successor goes with curvature-squared invariants, which P10 says is not an entry in this frameworks ledger. WHAT REMAINS: the scope is free and static on the instantaneous spectrum -- time-dependence does not move the leading coefficient, but that the regularisation commutes with the evolution is not established and the couplings are not in it. DISCHARGED BY: the coupled and non-adiabatic computation, which could still return zero; what is excluded is the claim holding trivially on the most favourable case.',
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
SINCE = 3
LASTFIND = ("r3103: **PO-21 answered — the geometry lifts the obstruction but does not deliver the "
            "fifth multiplet.** `L-834` closes the positive half `L-246` left open: on the c!=0 cut the "
            "horn swap T acts on the wall mode by pullback (invertible), so it CONJUGATES its c=0 "
            "action, and 'T trivial on a chirality block' is a conjugation invariant -- so the 2+2 P14 "
            "reports is preserved, never 2+1+1. The twist can ROTATE T but not PROJECT it; the lifting "
            "invariant (c, transverse) is orthogonal to the operation that would realise the split (a "
            "chiral projection). **A step advanced in the anticipated direction (definable, not forced) "
            "with the mechanism supplied; the fifth multiplet is named as what a successor must carry, "
            "and it is a projection the geometry does not.**")

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
KIND = {'PO-13': 'BUILD', 'PO-36': 'READ', 'PO-33': 'BUILD',   # r4145: was READ, scoped when the diagnosis looked answered; it is not
         'PO-14': 'BUILD', 'PO-15': 'READ', 'PO-16': 'READ',
        # ** brought in r3095 from p0's frontiers and the field ledgers, which carried them
        # unregistered.  PO-17 is a DECISION stated without being claimed both ways; PO-18 an
        # ENUMERATION; PO-19 and PO-20 are unattempted questions, so READ is the wrong kind
        # for them and WORK is used. **
        'PO-17': 'READ', 'PO-18': 'READ', 'PO-19': 'WORK', 'PO-20': 'WORK'}

# ** PO-23 added r3809: the ultraviolet definition of the mode sums, the one part of P07's
# three-part 'definition of the interacting tower' that is neither settled nor attempted. **
ORDER = ['PO-13', 'PO-44', 'PO-43', 'PO-24', 'PO-36', 'PO-30', 'PO-25', 'PO-26', 'PO-31', 'PO-23', 'PO-15', 'PO-14', 'PO-17', 'PO-18', 'PO-19', 'PO-20']
GROUP = {'PO-13': 'D', 'PO-14': 'A', 'PO-15': 'C', 'PO-16': 'D',
         # ** r3095: the four brought in from p0's frontiers and the field ledgers.  PO-17 and
         # PO-19 are substrate geometry; PO-18 is the constant ledger; PO-20 is analysis. **
         'PO-17': 'E', 'PO-18': 'E', 'PO-19': 'E', 'PO-20': 'E',
         'PO-23': 'C', 'PO-43': 'C', 'PO-44': 'C', 'PO-24': 'D', 'PO-25': 'E', 'PO-26': 'A', 'PO-27': 'A', 'PO-29': 'E', 'PO-31': 'D', 'PO-30': 'A', 'PO-36': 'D', 'PO-34': 'E'}
GNAME = {'A': 'the matter sector', 'B': 'the matter sector', 'C': 'the quantum sector',
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
