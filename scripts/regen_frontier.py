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
    'PO-13': ('the handover datum, and the rigid phase split beneath it', 1, 1, 6, None,
        'r6433/r6447: the potentials half of the one-locus statement is ANSWERED from this rows own named lead -- the '
        ' super-horizon join is conservation of R, hence (3/2)/(5/3) = 9/10 exactly, which P15 already states and recei '
        'pts (C21) while the instrument sets the potential to its primordial value instead. Its size is 10/9 and SCALE- '
        'INVARIANT, so not the cure. Measured by 60: l1/lA unchanged at 0.6764 exactly as the bound says, but P1/P2 mov '
        'ed 1.975->1.996 -- because dg0 = 4(Theta - Psi) is a DIFFERENCE with Theta set independently, so a 10% change  '
        'in Psi is a 19% affine shift, and affine shifts move ratios. THE HALF THAT FAILS IS THIS ROWS OWN DEFECT WITH '
        ' A NUMBER ON IT. Also: CRIC=branchpoint bypasses the handover block, so CRPSI is inert under it. Remaining: th '
        'e last convention stripped, both arms free or both pinned -- a run, with 60. '
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
    'PO-31': ('the progenitor spectrum', 1, 1, 6, None,
        'r4493/r6427: two of three rooms closed by impossibility; what remains is the progenitor spectrum, a modelling  '
        'task awaiting a progenitor interior. And ONE ROUTE IS NOW CLOSED: the only route the corpus ever named for DER '
        'IVING A_s rather than inheriting it -- a fixed point of a stationary recursion, recorded in the wisdom ledger  '
        'at r1942 and never entered into any paper -- is excluded by PO-40s monotone, twice over on premises that do n '
        'ot overlap. Entropy per baryon rises strictly at every crossing, so the lap map has no fixed point; and the ch '
        'ain is finite besides. So the constraint in kind gains a third exclusion: not a thermal history, not merely a  '
        'conserved charge, and not a fixed point. The derivation must reach the HEAD of a bounded genealogy -- the same '
        ' terminus eta reaches, so this row and PO-41 are one question asked of two quantities. '
),
    'PO-25': ('the charged bead -- DOES A CHARGED COLLAPSE FORM THE CAUCHY HORIZON', 1, 1, 4, None,
        'r3827/r6405: the step is RUN and comes out the same in both charge readings, which decouples it from the datum '
        ' fork. The criterion is beta = (decay rate)/kappa_- against 1/2 -- and Lambda>0 is why it needed a number, the '
        ' decay being exponential rather than Price-tailed so the horizon CAN survive near extremality. On the progenit '
        'or it does not: beta ~ 1e-251 intensive, 1e-15 extensive, with a generous ceiling so the figure bounds the hor '
        'izons chances from above. THE ETERNAL INNER HORIZON IS NOT FORMED, so the obstruction is a property of a stat '
        'ionary solution the dynamical problem does not reach. NOT delivered: inextendibility is not a spacelike r=0, s '
        'o the charged case is not thereby rejoined to the bead. '
),
    'PO-24': ('whether the tilt displacement is a tension', 1, 1, 5, None,
        'r4505/r6409: the remaining question is not well posed as asked. It presumes the displacement is a NUMBER; it i '
        's the local slope of a curve whose slope varies by (lmax/lmin)^2 = 6989 across the likelihoods own l=30-2508. '
        ' So a single tilt is a one-parameter fit to a function whose log slope varies by seven thousand over the data  '
        'scoring it, absorption is WINDOW-LOCAL, and the quoted -0.0304 is the true slope at l=381 and nowhere else. A  '
        'joint fit therefore meets a GAUSSIAN-SHAPED residual, not a shifted tilt, and no tilt removes a Gaussian -- so '
        ' what it weighs is the shape residual, already bounded at 0.26 sigma per bin. And n_s is inherited boundary da '
        'ta, so a displacement in it is a different input, not a conflict. '
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
SINCE = 3
LASTFIND = ("r4549: **the two-arm undriven split is dominated by a comparison asymmetry, not a physical "
            "difference.** The peak-to-scale ratio has the distance cancel out of it, so it was never a "
            "projection quantity -- which is why every source term, the damping envelope and the visibility "
            "each left it untouched. Run with the start and the sound-horizon convention matched it falls to "
            "a quarter of its size and changes sign, the two mismatches having been partly cancelling.")

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
ORDER = ['PO-13', 'PO-43', 'PO-24', 'PO-36', 'PO-30', 'PO-25', 'PO-26', 'PO-31', 'PO-23', 'PO-15', 'PO-14', 'PO-17', 'PO-18', 'PO-19', 'PO-20']
GROUP = {'PO-13': 'D', 'PO-14': 'A', 'PO-15': 'C', 'PO-16': 'D',
         # ** r3095: the four brought in from p0's frontiers and the field ledgers.  PO-17 and
         # PO-19 are substrate geometry; PO-18 is the constant ledger; PO-20 is analysis. **
         'PO-17': 'E', 'PO-18': 'E', 'PO-19': 'E', 'PO-20': 'E',
         'PO-23': 'C', 'PO-43': 'C', 'PO-24': 'D', 'PO-25': 'E', 'PO-26': 'A', 'PO-27': 'A', 'PO-29': 'E', 'PO-31': 'D', 'PO-30': 'A', 'PO-36': 'D', 'PO-34': 'E'}
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
