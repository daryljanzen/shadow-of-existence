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
    'PO-10': ('the likelihood comparison, and which run it rests on', 1, 0, 3, None,
        'r6780: REOPENED. P15 sec:refit-bound reports both arms fitted over 215 bins with the same '
        'five parameters free in each, returning chi^2 = 397.13 against 206.44, 1.891 and 0.983 per '
        'degree of freedom, Delta chi^2 = 190.7. P15s own receipt records that pair as the banked '
        'r1934 figure, built by applying the damping suppression to CAMBs own LambdaCDM spectrum and '
        'so on LambdaCDMs peak positions, and says it answers a different question and is superseded, '
        'not repeated. And r6774 changed the configuration under both, the acoustic scale now being '
        'computed from the rate at the branch point. The row owes a run on the configuration that now '
        'exists, with its own receipt: the framing settled against the receipts F3, which admits only '
        'the difference between the two arms on one instrument; the F2 floor of +1114.0 reported beside '
        'any difference; the position deficits presence in the spectrum run on stated explicitly; and '
        'the old pairs provenance closed. Routed to node 60. The figure pass into P07 and P18 is held '
        'on this. '
        'r6782: ANSWERED by 60. THE FRAMING: there are TWO instruments and the bodys pair is the '
        'other ones, which is why the body and the receipt are both accurate. fit.py+CAMB fits FIVE '
        'parameters on 215 bins and its CR arm is CAMBs LambdaCDM TT times an ell-only damping '
        'envelope; ACOUSTIC_two_arm+chi2_of_spectrum fits ONE amplitude on 185 covered bins and its '
        'CR arm is the constructions own spectrum. THE OLD PAIRS PROVENANCE: cr.json banks 397.1255 '
        'as a genuine five-parameter optimum at H0=78.13, so the bodys parameter count is right and '
        'what the number lacked was the constructions spectrum -- BOTH of the orders two options at '
        'once, which were offered as alternatives. And the envelopes inability to carry a comb is '
        'MEASURED: across envelopes strong enough to move ell_1 by up to eight multipoles the '
        'spacings hold within 6 per cent, so the positions stay CAMBs. THE FLOOR: on the second '
        'instrument F2=+1114.0 and F3=+50496.5, forty-five times it; the bodys Delta chi^2=190.7 is '
        'BELOW that floor and could not be read there even if it were its, while it is readable on '
        'the first only because that instruments control IS the CAMB reference so its floor is '
        'identically zero -- the absence of an independent control rather than a better instrument. '
        'THE POSITION DEFICIT is present in the second instruments spectrum (its own first peak '
        'below the skys) and structurally absent from the firsts. AND THE CROSSING CONFIGURATION WAS '
        'UNREACHABLE, which is the revisions own finding: the CR arms background was written in as '
        'literals (H0=73.00, Omega_m=0.3066, the directly-measured-H0 configuration that goes with '
        'LATARG being fitted), so no knob reached the background the distance data fix alone. '
        'CRH0/CROM/CROMBH2 exposed, defaults byte-identical. The sound horizon then converges from '
        'the branch point exactly as P15 says, r_s rising to 256.13 Mpc over four decades of '
        'starting redshift, BUT to l_A about 172 rather than the bodys computed 298.0 -- because the '
        'body puts r_s on the radiation-carrying LEAF rate while rs_from integrates the '
        'radiation-free one, and the instruments own file says its two sound horizons must not be '
        'unified. Which convention is intended is the papers question and is not settled there; no '
        'chi^2 is manufactured against a comb the paper does not claim. PO-7 protected throughout. '
    ),
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
    'PO-45': ('STRUCK r6733 -- the colourless triple is fixed on the ordinary route', 0, 0, 0, None,
        'r6733: answered and struck. The triple is a doublet plus a singlet, not a three-fold symmetric '
        'object. Its chirality is geometric: the parity R = gamma^5, the Clifford element of the cut s '
        'normal. Its pairing is not a rotation of the substrate -- the one Euclidean four-space has the '
        'wrong chirality and the one whose chirality is gamma^5 is Lorentzian -- so the geometry supplies '
        'both ingredients of the chiral projection and not their product. Which handedness is not the '
        'twist s, which separates without selecting. And its states sit on no geometric locus. So the '
        'triple is fixed on the ordinary route, with CR supplying its chirality. What generates the matter '
        'content is carried at PO-30; the working record is in the consolidation plan s rehoming record. '
    ),
    'PO-36': ('does the Hubble-Eddington radius track the dynamical mass or the baryonic one', 1, 0, 4, None,
        'r4203/r6407: the discrimination is QUANTIFIED -- the two mass choices differ by f_b^(-1/3) = 1.85 in the radiu '
        's (10.5 Mpc against 5.7 on a rich cluster) and by 1/f_b = 6.4 in a Lambda inferred from an observed one. BUT I '
        'T IS NOT A CR-VERSUS-LCDM DISCRIMINATOR, which this rows placement implies: m(r) is the bend, so whatever gra '
        'vitates is in it, exactly as in general relativity, and both frameworks take the same M. What the measurement  '
        'discriminates is the DARK FRACTION, not the framework -- control at f_b=1 gives ratio 1.000 and the test falls '
        ' silent. The corpuss stake is the input to one constant read at two ranges, whose local reading carries tha '
        't factor until the mass question is settled. And P03s quoted robust to dark-matter details and baryonic effe '
        "cts is profile-independence GIVEN M, not independence of WHICH M.  r6809 ANSWERS THE MASS HALF, on node 60's r6804, and derives the radius rather than importing it. The comoving acceleration on the cut is r/alpha^2 - M/r^2, which r1680 proved equals r*K_G with K_G = 1/alpha^2 - M/r^3, so vanishing acceleration IS K_G = 0 IS r^3 = M alpha^2 = 3M/Lambda: the construction has carried the Hubble-Eddington radius since r1680 as the deceleration-to-acceleration turnover, under another name. And rho = m'(r)/4 pi r^2 has ONE channel, so every component with stress-energy is in the bend and a baryon-only m is the assertion rho_dark = 0 rather than a change of variable -- the construction predicts the DYNAMICAL mass structurally and the row is not a framework discriminator. The name guard is arithmetic now: force balance gives (M alpha^2)^(1/3), density equality (2 M alpha^2)^(1/3), ratio 2^(1/3) exactly, so reading one for the other is a 26 percent error. NO DATA IS TOUCHED: the row stays open on the measurement alone -- cluster statistics against independently measured baryonic mass -- and the 6.37 unpinned in the local reading of Lambda stays where r6407 put it."
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
    'PO-30': ('STRUCK r6758 -- the geometry supplies no choices, and colour s global group converted', 0, 0, 0, None,
        'r6758: answered and struck. The dynamics given the content were already supplied. The law for '
        'the content, tested across P14 s whole ledger with symmetric judged independently of supplied: '
        'all ten single entries sort and the two compound ones split at the predicted seam; on breakings '
        'it holds both ways, and extended to every entry one direction holds throughout -- THE GEOMETRY '
        'SUPPLIES NO CHOICES. One entry converted, colour s global group: the seats degeneracy is exact, '
        'its symmetry a canonical U(3) with Delta(27) inside it and SU(3) the gauged factor the world s '
        'baryons select. The local gauging is not supplied because the bundle is over the space of members '
        'and there is no spacetime bundle for a connection to be on; the structure neither supplies nor '
        'obstructs it. Not closed: the choices themselves, where the Standard Model s free parameters sit. '
        'r6762: and the determinant circle that stayed global IS a constituent count, with the conservation '
        'question settled both ways. Exactly conserved on every STATIC member -- the parity-odd source '
        'vanishes identically for arbitrary static profiles, so Schwarzschild, Schwarzschild-de Sitter, '
        'de Sitter and Nariai are instances of one identity, not three separate zeros. Violated on the '
        'TWISTED member alone, where the source is exactly odd in the twist and vanishes on the polarised '
        'cut. Coefficient 3, traced to dim ker_- = 0 and not to a convention. NO INFLOW: the construction '
        'has no bulk gravitational Chern-Simons term, and the one-form potential such a term would need is '
        'what r6752 ruled out. The violation integrates to the change in the member s gravitational '
        'Chern-Simons number. A global symmetry s anomaly is not an inconsistency and is not reported as one.'
    ),
    'PO-47': ('what displaces the fourth acoustic peak', 1, 1, 4, None,
        'OPENED r6861 as PO-13 remainder. With the handover at the branch point and the background fixed by the '
        'distance data alone, the comb is 298.0 against the sky 298.4 and the first three peaks land within a grid '
        'step; the FOURTH is about one per cent high, and the offsets keep their sign and order across all four. '
        'Reproduced on a second instrument at 1132 against 1134, so it is the spectrum and not either implementation. '
        'ALREADY RULED OUT: the phase intercept is not a residual (through one locator the arm sits inside the sky own '
        'locating spread and the offset sign flips between the three-peak and four-peak fits); the damping envelope is '
        'excluded (imposing the control moves the peak a seventh of a multipole against an offset of two, and the '
        'inverse returns the same displacement with opposite sign); the driving is the control to four per cent; a '
        'parameter refit does not move it. DISCHARGE: a mechanism that displaces the fourth peak and not the first '
        'three, or a demonstration that at the locating spreads there is nothing to displace.'),
    'PO-48': ('does S = A/4 carry to a cosmological horizon on this reading', 1, 1, 4, None,
        'OPENED r6861, overdue: P17 declines it in terms and TWO struck rows close above it -- PO-24 and PO-43 both '
        'terminate here without it being carried anywhere, a question propping two closures while belonging to no row. '
        'NOT A LOOSE END BUT A FORK: P17 sec:ledger takes the temperature and never the entropy and says why -- T is '
        'built from alpha alone, one register, while the entropy is a ratio of alpha to the Planck length and is a '
        'count taken ACROSS the register split. So whether the area law carries is a question about that split and not '
        'an import from black-hole thermodynamics. AND P17 HAS SAID WHAT FAILURE MEANS: were it to fail to carry that '
        'would be a result and not a gap -- both outcomes results, neither a debt. If it carries, a quantum-register '
        'constant becomes visible in the one cross-register quantity; if not, the Gauss-Bonnet coefficient has no home.'),
    'PO-49': ('the charged interior third regime', 1, 1, 3, None,
        'OPENED r6861 as PO-25 remainder. That row is struck on its own question -- the obstruction is destroyed on '
        'both charge readings and was never total across the shells -- and the verification reported a turning-point '
        'structure with THREE regimes where the reading stated two, the third being over-extremality, and nothing '
        'carries it. DISCHARGE: what the lap does in that regime on the same exact interior, and whether it is '
        'reachable on a progenitor of the mass this cosmology requires, the struck row scoring the charge-to-mass '
        'threshold near 1e-2 so reachability is a question about astrophysical charge and not about the geometry.'),
    'PO-50': ('the turnaround measurement with turnaround masses', 1, 1, 3, None,
        'OPENED r6861 as PO-36 remainder. That row is struck: the radius tracks the dynamical mass, entailed rather '
        'than observed. What its own measurement could NOT do is discriminate -- the ensemble ratios run 1.20 to 2.33 '
        'above the spherical bound at the dynamical mass, and the authors leading explanation is the systematic the '
        'corpus had named, virial mass substituting for turnaround mass. DISCHARGE: an ensemble with masses measured '
        'inside the turnaround rather than at the virial radius, with the radius still independent of internal '
        'dynamics. The bound-to-attained factor is parameter-free and the guard is four-way, so the instrument is '
        'built and only the sample is missing.'
        ' r6893 (66) RUNS THE SWEEP AND CORRECTS THIS ROW OWN PREMISE. The row says the authors leading '
        'explanation for the excess is the systematic the corpus had named, a virial mass standing in for a '
        'turnaround mass. It is the right systematic and it is not large enough: the bound goes as M^(1/3), so '
        'rescuing a ratio R needs M_ta/M_vir = R^3 -- 12.6, 5.4, 6.4, 6.0, 2.6, 1.7 for the six groups -- against '
        'a measured turnaround-to-virial mass ratio of 1.2 to 2.2 in the caustic ensembles. It accounts for the '
        'two mildest rows and not the four largest, though none of the six is individually significant on its own '
        'error bar. AND THE TWO ENSEMBLES THAT LOOK USABLE ARE CIRCULAR, measured here and not read off: both '
        'define their outer radius at a FIXED OVERDENSITY rather than measuring it, and at rho_bar = 3.5 rho_c the '
        'ratio of that radius to the bound is (Omega_Lambda/1.75)^(1/3) = 0.737, at 5.56 rho_c it is 0.632 -- pure '
        'numbers carrying no datum, identical for every cluster in either sample. No published catalogue carries a '
        'kinematic turnaround radius AND an enclosed mass at it; every candidate fails one side. The direction of '
        'the correction is itself contested: the caustic route puts the turnaround-enclosed mass above the virial '
        'one, the Local Volume flow route puts the mass inside the zero-velocity surface at about six tenths of '
        'it, and settling that comes first because the row arithmetic runs through it. Coma now has a kinematic '
        'turnaround radius, a caustic profile and wide-field lensing on one object, so the single-object version '
        'is reachable; the ENSEMBLE is not, and assembling one is a reanalysis of public redshifts rather than a '
        'new survey. The corpus is not exposed: P3 states the radius as general relativity with Lambda and says it '
        'discriminates no cosmology, and the landed confrontation is the Local Group, where the mass is measured '
        'independently of the radius.'),
    'PO-51': ('the log subtraction point, and whether the tower floor is forced', 1, 1, 3, None,
        'OPENED r6861 as PO-43 named-and-unbuilt candidate. A log needs a subtraction point; the corpus holds there is '
        'no second physical length; and in a discrete mode sum the subtraction point is a mode number -- of which this '
        'tower has a canonical one, its own floor. THE BURDEN IS STATED AT THE OUTSET: whether that fixes the constant '
        'or merely names a convention is a question and not a result, and the burden is to show the floor is FORCED '
        'rather than convenient. Deliberately not built while PO-43 check was outstanding; that check has come out for '
        'the claim, so the candidate is now this row own.'),
    'PO-52': ('where the shear breaks the counterterm degeneracy', 1, 1, 3, None,
        'OPENED r6867 as PO-51 remainder, on the standing order. PO-51 closes because the log counterterm is '
        'DEGENERATE with the cosmological term on the admitted background family -- the degeneracy being conformal '
        'flatness, checked on the tower own background -- so a change of subtraction point moves a constant '
        'reabsorbed into the one measured gauge. The degeneracy does the work and it is a property of that family. '
        'SO THE QUESTION IS WHAT HAPPENS WHERE IT BREAKS: at second order in the shear the family is no longer '
        'conformally flat, and there the Weyl-squared entry is a separate coefficient rather than an absorbed '
        'constant -- which is PO-43 uncosted entry, named there and again here and carried by neither. DISCHARGE: '
        'whether the admitted family reaches second order in the shear at all on this construction (if not, the entry '
        'has no domain and that closes it); and if it does, whether the broken degeneracy leaves a coefficient '
        'anything observes, which is the cross-register question PO-48 reached and did not close. '
        'r6897 (66, on node 60 r6894) ANSWERS THE CHEAP HALF, AGAINST CLOSING. The question was whether '
        'the admitted family reaches second order in the shear at all; if not the Weyl-squared entry has '
        'no domain and the row closes on that alone. IT DOES REACH THERE: the Weyl invariant vanishes '
        'identically on the admitted family -- the conformal flatness PO-51 rests on, used here as the '
        'calibration -- and on the construction own on-shell Gowdy-de Sitter confined wave it is zero at '
        'zeroth and first order in the shear amplitude and NON-VANISHING at second. So the entry has a '
        'domain and the row keeps its second half: whether the broken degeneracy leaves a coefficient '
        'anything observes. AND THE TWO ROWS DO NOT COLLAPSE. The chat seat sent this row together with '
        'PO-55 on the reading that an unobserved coefficient and an unobserved area difference might be '
        'one fact. They are not: PO-55 closes by a quantity NON-EXISTENCE, and this row quantity EXISTS '
        'with the open question being whether anything sees it. The method transfers -- ask whether it '
        'exists before asking whether it is seen -- and the result does not.'),
    'PO-53': ('is the offset family a family of solutions or of sections of one solution', 1, 1, 3, None,
        'OPENED r6869 as PO-48 remainder, on the standing order; node 60 named it rather than deciding it. PO-48 '
        'closes because a variation reaches the horizon term at the substrate horizon -- but what varies is an '
        'OFFSET, and sec:ledger own identification of the mass with that offset makes the family cuts of ONE '
        'substrate rather than a family of solutions, a re-slicing whose Noether charge the construction returns '
        'identically zero for. If that reading is the corpus, the variation is void at the substrate horizon too and '
        'the area law carries nowhere here. It is the difference between the law carrying at one of the two horizons '
        'and at neither, and it turns on what the corpus means by its own family rather than on a computation -- a '
        'gate question. DISCHARGE: reading sec:ledger and the operator paper together on whether the offset-labelled '
        'cuts are solutions or sections, and if sections, saying what the vanishing Noether charge means for the '
        'temperature, which the corpus does quote.'),
    'PO-54': ('the central move happens where the first law is undetermined', 1, 1, 4, None,
        'OPENED r6873 as PO-48 remainder, on the standing order -- and the gate missed it when striking that row, '
        'which is the failure the order exists to catch. PO-48 found the area law UNDETERMINED at the forced member, '
        'the double root making the surface gravity vanish so the first law admits no solution for the entropy '
        'variation. And the forced member is where the causal reassignment ACTS: the framework says in terms that the '
        'kappa = 0 degeneracy is what makes the reassignment possible, and that the degenerate horizon carries no '
        'bifurcation 2-sphere -- the same hypothesis the Noether-charge construction needs and lacks. THE CORPUS IS '
        'ALREADY CONSISTENT, which is why this is a question and not a defect: it quotes thermodynamics only at the '
        'substrate horizon where the law carries, and uses the forced member degeneracy structurally rather than '
        'thermally. What is not said is what the coincidence MEANS -- and it is sharper than a coincidence, since the '
        'same double root makes the member Nariai, makes the surface gravity vanish, and makes the photon orbit '
        'Lyapunov exponent vanish, all because 3M = r_h. DISCHARGE: whether the vanishing says the seam carries no '
        'thermodynamic content, so there is nothing for the reassignment to transport and the construction is cleaner '
        'than it knew; or whether the reassignment needs something the vanishing denies it, in which case the '
        'framework owes an account of what crosses. Both are results; the second is worth looking for first.'),
    'PO-57': ('the spin-up 68 read remaining items -- sixteen, complete and unfiltered', 1, 0, 6, None,
        'OPENED r6899 (66) from a cold full-corpus read taken by a fresh node. Ninety-one mechanical fixes and '
        'the rate rule are landed at r6899, and so are the two items the read flagged to raise first. What the '
        'row carries is everything it confirmed at source and did NOT patch, each needing a judgement rather '
        'than a correction: P18 sec:oneradius displaying an identity and then denying the two quantities are '
        'related, with P6 sec:place the same defect and the readings count inflated by counting both halves of '
        'one identity; P5 prop:nariai-fixed claiming a unique fixed point where there are two, reproduced in '
        'P12 from the same formulas; P5 prop:tau stating order three on a domain where tau is the identity; P9 '
        'prose giving J = Ma one line after its own proposition gives J = Ma/Xi^2, three sources against one; '
        'P15 control validation at 0.14 per cent on four sites and 0.23 per cent on one, both true of '
        'different runs, with P7 pairing the arm headline numbers to the configuration they were taken in and '
        'P15 abstract not; P15 amplitude ladder ten orders apart by its own propositions and eighteen by the '
        'connecting sentence; P13 sl(3,R) exclusion right for the wrong reason, the conclusion holding by real '
        'rank; P13 sec:synthesis 3 + 3bar parenthetical off twice where sec:setup is right; P13 canon header '
        'stating the superseded obstruction hypotheses and verdict, and it is the header a node reads to '
        'orient; P14 using two hypercharge normalisations and two values for one quantity, the fix being the '
        'clause the with-nothing-fitted claim rests on; P12 abstract and header stopping at order twelve and '
        'omitting the order-48 closure, the paper strongest discrete result; P17 defining alpha with a modulus '
        'in a section that admits alpha^2 < 0; P18 forbidding the rate assignment sec:tensions requires; '
        'THE_PLAN carrying a superseded order count and a dead alias item; six uncited bibitems, an editorial '
        'call and not a defect; and two instruments the read names and this pass did not build -- declared '
        'counts against enumerated items, which THE_PLAN Phase 6 already names, and a superseded-numeric-value '
        'ledger grepped corpus-wide, which is the channel that produced the retired driving figure and the '
        'index four stale numbers. AND WHAT THE READ ELIMINATED IS KEPT: six hypotheses came back negative '
        'with their blindnesses named, three of them firing on one essay by reading a restatement as a site of '
        'independent claim, and one class firing because the index notation rule says read each occurrence in '
        'context never by pattern ONCE, at the top of a two-thousand-line file -- a fact about the index and '
        'not about the reader. DISCHARGE: each item worked or explicitly declined with a reason, and the two '
        'named instruments built. Items leave by being worked, never by reclassification. '
        'r6901 (66) WORKS THREE OF THEM, the three with physics in them. (1) THE IDENTITY IS CONCEDED AND THE '
        'CONVERGENCE RELOCATED ONTO WHAT CARRIES IT: on the marginal congruence the areal acceleration equals '
        '-f/2 equals r K_G by differentiating f, in one line, so the slice being flat and the areal acceleration '
        'changing sign are ONE FACT IN TWO LANGUAGES and are counted once. What is NOT an identity is what the '
        'section is about: r^3 = M alpha^2 is one formula read at two masses -- a local mass giving the boundary '
        'within which a structure stays bound, and the cosmological offset, which on this construction IS the '
        'epoch parameter, giving the acceleration turn -- and they are one formula because the two masses are the '
        'same parameter of the same metric. Computed from different objects, as a local exterior and a Friedmann '
        'background are, they would share Lambda and nothing else. That is stronger than the coincidence it '
        'replaces. THE COUNT IS SIX, arithmetic verified rather than assumed: P7 list of five contains both halves '
        'and P6 five contains both as well with three shared, so merging gives 4 + 4 - 2 = 6, and both lists were '
        'READ before either was edited. Corrected at every radius-count site including the receipt index label the '
        'appendices generate from; the symmetry-worn-seven-ways count is a different seven and is untouched. '
        '(6) THE AMPLITUDE LADDER IS TEN ORDERS AND THE PROPOSITIONS WERE RIGHT: recomputed, 9 (l_P/M)^2 rho^-6 = '
        '9.4e-113 at the cap with rho = 5.4e-2, which is 9.97 orders above the substrate 1e-122 and 103.3 orders '
        'short of the observed 2e-9. The transfer law ALREADY carries the crunch mixing, so the amplification is '
        'the rho^-6 and not a second factor on top of it; the two-step ladder double-counted, and the progenitor '
        'own bare vacuum is a quantity the section never computes. (5) THE CONTROL VALIDATION IS 0.23 PER CENT '
        'where the arm numbers are quoted: both figures are real and belong to different runs, and the one that '
        'belongs beside the arm headline numbers is the one from the configuration those numbers were taken in, '
        'which the body already identifies and P7 already pairs correctly. '
        'r6903 (66) WORKS FIVE MORE. (2) The fixed-point claim is sharper than reported and the correction is a '
        'BRANCH and not a half-plane: on the circle w = pi/3 - w gives two fixed angles, pi/6 and 7pi/6, the '
        'second carrying r0 = -1/sqrt3 -- but sigma as the paper defines it is not the circle reflection, since '
        'w -> (2/sqrt3) sin w is two-to-one and the principal square root selects the branch through 11pi/6, so '
        'computed here sigma(-1/sqrt3) = 2/sqrt3 and -1/sqrt3 is NOT a fixed point of the involution at all. The '
        'uniqueness is exact for sigma on the slicing parameter; what the circle carries in addition is the '
        'Nariai vantage image under the orientation parity r0 -> -r0, not an admitted member. (3) THE DOMAIN IS '
        'THE DEFECT, NOT THE ORDER: on [0, 2pi/3) with endpoints identified a translation by 2pi/3 is a full '
        'turn, so tau acts there as the IDENTITY and has order one; the order is three on R/2piZ, which is what '
        'the proof uses. That quotient is the right domain for the groupoid and the wrong one for reading the '
        'periodicity own order. (4) J = Ma/Xi^2 at both prose sites, the bare Ma being the Lambda -> 0 limit and '
        'the claim it carries true of either form. (12) THE MODULUS GOES because the section apparatus is '
        'signed: P17 turns on alpha^2 = 3/Lambda and admits alpha^2 < 0 for anti-de Sitter, so the modulus was '
        'the outlier. (13) AND THIS ONE CLOSES THE RATE ARC: P18 named the sound horizon as the second fatal '
        'extension, but on the settled assignment the sound horizon IS radiation-included, so that reading '
        'forbade what sec:tensions requires. The corpus own statement names THE DISTANCES, and P18 now says so '
        '-- and it is the distances and not the plasma own lengths, which take that rate by the same rule that '
        'puts nucleosynthesis there, so the two windows fall on the same side and only the separations read '
        'across leaves fall on the other. '
        'r6905 (66) WORKS FIVE MORE. (7) The exclusion needed TWO arguments, not one: su(2,1) does fall to the '
        'count, its realified carrier six-dimensional bearing signature (4,2) and so landing in so(4,2), but '
        'sl(3,R) acts faithfully on R^3 so the count does not reach it -- it falls instead to real rank, the '
        'substrate so(5,1) having rank one and sl(3,R) rank two, and a subalgebra rank cannot exceed its '
        'ambient. The wall holds for all three forms; what was wrong was presenting one argument as doing work '
        'it cannot do. (8) The parenthetical was off on both counts, checked here: su(3) preserves h = g + i '
        'omega on C^3 and so(6) is the stabiliser of the SYMMETRIC part g, the antisymmetric omega being what '
        'gives sp instead, and 3 + 3bar is the carrier COMPLEXIFICATION and not the carrier. (9) THE CANON '
        'HEADER, the one that matters because it is what a node reads to orient: its theorem statement did '
        'carry even-dimensionality, so the report reading was half right; what it got wrong is the load-bearing '
        'list and the verdict. The third hypothesis is the one that bites -- the compact face is S^5, odd, so '
        'the equivariant index has no grading to vanish and the obstruction is VACUOUS rather than canonical '
        'there, the conclusion resting on a second dimension-independent route: positive scalar curvature and '
        'Lichnerowicz, with the round-face Dirac spectrum +/-(5/2 + k)/alpha verified here, least eigenvalue '
        '5/2alpha and no zero modes at all. So the realisation is NOT rendered vector-like but WITHOUT MASSLESS '
        'CONTENT, the stronger statement, and the header said the weaker one. (10) The hypercharge clause is now '
        'stated in the paper own normalisation: it works in Q = I3 + Y with the doublet at Y = 1/6, and the '
        'passage switched mid-sentence to Q = I3 + Y/2 where the doublet Y is 1/3. Same map either way, but the '
        'constant is TWICE the hypercharge in the paper own convention and it is the constant that carries the '
        'with-nothing-fitted claim. (11) And the abstract and header no longer stop at order twelve: both carry '
        'sec:weyl-a3 closure, order twenty-four and then forty-eight, with the element profile identifying the '
        'group rather than counting it -- all six order-four elements improper, the signature of the full '
        'tetrahedral group, so W(A_3) in its Weyl embedding. THREE REMAIN, and they are the soft ones: '
        'THE_PLAN two stale hygiene items, the six uncited bibitems which are an editorial call, and the two '
        'instruments the read named. '
        'r6907 (66) CLOSES ALL BUT ONE. THE_PLAN two items are both real and both on one line: it carried '
        'P16 superseded order count -- four orders where P16 sec:peak own figures give three and a half, T_pk '
        '174 MeV against T_D 0.07 MeV, the 3.8 that reads like it being the INFALL energy and not the '
        'thermalised peak -- and it asserted the JanzenShadow alias as a live hygiene item in the PRESENT '
        'TENSE when the unification landed at r1566 and no paper carries the alias. THE SUPERSEDED-VALUE '
        'LEDGER IS BUILT, and as a WIDENING rather than a new file: check_withdrawn already carried a registry '
        'of withdrawn CLAIMS keyed by phrase, and the numeric case is the same failure keyed by VALUE. '
        'Stricter semantics on the corpus own rule -- a withdrawn claim may be quoted with an adjacent '
        'correction, but a paper never reports its own computational corrections, so a retired number has no '
        'honest bare form and there is no marker escape. Headers are scanned, comments and all, since two of '
        'this sweep staleness instances were in canon headers, and that was measured before adoption. Eleven '
        'entries, each calibrated both ways: nineteen hits on the tree as it stood before this arc, zero on '
        'the corrected one, and the gate shown to FAIL on a seeded instance rather than only to pass. AND THE '
        'SECOND INSTRUMENT DOES NOT WORK -- built, measured, withdrawn. A checker reading a number-word '
        'before a list returns six false positives in seven at the window that catches the real instance, '
        'firing on gathered-in-one-place and that-one-map and the-three-parametrisations; at the window with '
        'no false positives it catches NEITHER real instance. Proximity does not separate a count from any '
        'other number in the lead-in. Removed rather than allowlisted green, because a gate kept passing by '
        'exception trains nodes to add exceptions -- and what replaced it is the shape the failure actually '
        'has: the same miscount in a body and a header while the list disagrees is a superseded VALUE in two '
        'documents, so the count is registered in the ledger above, where it fires. ONE ITEM LEFT and it is '
        'not a defect: the uncited bibitems, an editorial call, enumerated here rather than taken from the '
        'read -- there are SEVEN across six papers, not six, and the read named every one correctly. Routed '
        'to Daryl as a judgement.'),
    'PO-59': ('the reproducibility layer pin debt, and the ratchet that was not binding', 1, 1, 3, None,
        'OPENED r6921 by a GATE FIX and not by a new failure. check_receipts_run located the runner '
        'verdict with an UNANCHORED re.search, which returns the FIRST match -- and the runner '
        'captures every receipt stdout into the same file, where L237/G50 SEEDS A FAKE RUNNER TO '
        'TEST THIS VERY GATE and prints 0 pass, 1 fail, 0 over timeout, in 0s while doing it. So the '
        'gate built because a runner printed a verdict that was not about the set has been reading a '
        'verdict that was not its own, and on the r6921 suite it reported 849 receipts unaccounted '
        'for on a run that had accounted for all 850. The fix is one anchor -- the runner writes at '
        'line start with exactly two spaces where captured output is indented further -- calibrated '
        'on that same file, the old pattern returning 0 pass, 1 fail and the anchored one 766 pass, '
        '83 fail. AND WHAT THE FIX EXPOSES IS A DEBT OF 81: 766 pass, 83 fail, 1 over timeout, two '
        'of the 83 the declared pynucastro environment pair, against a baseline of 0. The debt is '
        'INHERITED and not incurred -- all 88 failures of the pre-fix run were re-run against '
        'pre-merge main in an isolated worktree, 83 already failed there, and the 5 the corpus sweep '
        'caused were repaired before the run; L237/G50 was added 2026-08-14, so the ratchet has not '
        'bound since the first suite run that captured its output. The head of receipts/PIN_DEBT.txt '
        'STAYS AT 0, the baseline moving downward only, and the complete unfiltered list of all 83 '
        'is written there by family. DISCHARGE: the 81 run and repaired and the head rewritten to 0 '
        'by the gate rather than by hand. Most are prose pins whose corpus text moved, so the repair '
        'is per receipt and a judgement each time -- a pin that froze an error is re-pointed at the '
        'fix, a finding the corpus has since discharged is re-pointed at what discharged it, and '
        'neither is a reword; r6921 own five repairs are the worked examples. No receipt leaves the '
        'list by reclassification, only by running. Needs no acoustic or tilt context and displaces '
        'neither loaded seat, so it is the natural first order for a fresh node.'),
    'PO-58': ('the lift normalizability threshold on the operator the corpus now uses', 1, 1, 2, None,
        'OPENED r6921 from the spin-up 69 read, as the remainder of a fix that landed only half. P14 '
        'count passage rejected the growing zero-mode branch by a leaf-measure argument at the branch '
        'point -- dl ~ sqrt(|r|/2M) dr, so |r|^s normalizes for s > -3/4 and the growing s = -lambda '
        'would need lambda < 3/4, which no lambda = j+1/2 attains. ON THE OPERATOR THE CORPUS NOW USES '
        'THAT ARGUMENT IS GONE: the read corrected the count passage, where near the branch point '
        'f -> -2M/r makes the exponent go as i sqrt(|r|), both chiralities a bounded phase and the '
        'measure integrable, so the crossing selects nothing and costs the norm nothing. BUT THE SAME '
        '3/4 SURVIVES TWICE IN sec:lift AND THERE IT IS LOAD-BEARING: the lift mode content is a '
        'normalizability computation on THE LIFT OWN MEASURE AT THE THREE HINGES, a different locus and '
        'a different measure from the branch point, and it rejects the growing branch by the same '
        'condition. The second occurrence makes it structural: the deck third case is excluded because '
        'it needs the three sectors decoupled, which is that same rejection read as a condition on the '
        'hinges -- one inequality deciding both conjuncts in opposite senses -- so a wrong threshold '
        'moves two conclusions at once and in opposite directions. THE MARGIN IS STATED WITH THE '
        'DEFECT: the smallest admissible lambda is 1, so any threshold below 1 returns the same '
        'verdict and the conclusion has room; what is at risk is the NUMBER and the derivation behind '
        'it, the corpus not getting to quote a threshold whose argument it has replaced elsewhere in '
        'the same paper, nor to assume the branch-point measure carries to the hinges, which is the '
        'step that has never been run. DISCHARGE: the hinge normalizability recomputed on the current '
        'operator and the lift own measure, reporting the threshold it gives; and if it differs from '
        '3/4, whether both conjuncts of the deck argument still hold at the new value.'),
    'PO-56': ('the acoustic contrast difference: the projection geometry, on the corpus two-rate assignment', 1, 1, 4, None,
        'OPENED r6891 as PO-13 remainder, on the standing order. PO-13 was struck at r6790 because the handover at '
        'the branch point supplies the one-locus state the row asked for, and it routed what it left -- the acoustic '
        'phase and the fourth peak -- into P15 sec:scope prose rather than into a row. BOTH HAVE SINCE DISSOLVED: the '
        'phase intercept sits inside the sky own locating spread and the fourth peak is 0.9 to 1.3 sigma out with most '
        'of the offset shared with the control. What replaced them has never had a row. THE OBJECT, MEASURED: with '
        'Delta the whitened difference of the two arms at their own minima, chi^2 decomposes exactly as '
        '282.96 = 177.88 + 27.82 + 77.26, so the model difference carries three quarters of the excess and the '
        'rejection is not one sky luck -- this arm scores 1.43 per bin against the control 0.99 on a typical sky. '
        'Delta is TROUGH-DOMINATED (+0.011 at the peaks against -0.760 at the troughs), its oscillatory part carries '
        'seven tenths of it, and that part is antisymmetric about the ENVELOPE rather than about each peak -- a '
        'CONTRAST, and not a phase and not an envelope. This arm acoustic oscillation is 1.040 times the control about '
        'its own envelope. ALREADY RULED OUT, carried across so the row starts where the work ended: the handover '
        'amplitude EXACTLY, being absorbed by the one fitted amplitude; the neutrino hierarchy truncation depth '
        '(93.7% of the norm survives it); the early integrated Sachs-Wolfe term (92.8%); the continuity half of the '
        'driving (87.6%). The Euler half reaches 68.3% but at a direction cosine of -0.16, which is not the direction. '
        'And the whole amplitude-tilt-damping-position family together carries 5.73%, against 51% for a single '
        'control-only direction that raises the oscillation at fixed envelope with nothing fitted. THE CHANNEL IS '
        'IDENTIFIED AND THE CAUSE IS NOT: removing the monopole and removing the Doppler term bracket the contrast '
        'direction with OPPOSITE SIGNS, on the line-of-sight path and on the reporting path alike and with the same '
        'signs on both, so the reading is not an artefact of the path it first had to be measured on. But neither '
        'deletion returns the two arms to a common contrast (1.0376 and 1.0818 against the base 1.0401), so the '
        'bracket locates where the difference enters and not what produces it, and about a third of the norm is '
        'unnamed. THE ONE REACHABLE CANDIDATE HAS NOW BEEN POINTED AT THE QUESTION AND IT IS RULED OUT -- r6893. '
        'The neutrinos free-streaming knob was located sub-bin, by a parabola vertex and again by an '
        'envelope-normalised cross-correlation, on both arms and again at four times the multipole sampling. '
        'THE SHIFT IS NOT UNIFORM, which corrects r6889: band by band it rises monotonically, +2.9 / +5.6 / +9.4 / '
        '+10.9 / +12.6 on the control and +3.1 / +5.7 / +9.3 / +10.9 / +12.5 on the arm, so the uniformity r6889 '
        'gated was the grid. AND IT IS COMMON TO THE TWO ARMS: the largest band-by-band difference is 0.17 of a '
        'multipole and the extremum-averaged shift in units of each arm own l_A agrees to 1.7e-4, so on the order own '
        'criterion -- a phase shift common to both is not a candidate for Delta and one that differs between them is '
        '-- it is not a candidate. The drag half, kept apart and split in two because it is two things, says the same '
        'independently: removing free-streaming raises the ENVELOPE by 25.7 per cent and changes the peak-to-trough '
        'CONTRAST by -1.3 per cent, on both arms, agreeing to 0.0004 and 0.0006 -- and Delta is a CONTRAST difference, '
        'so the knob large effect is in the wrong quantity. In Delta own space the two arms NUFS directions sit at a '
        'whitened cosine of 0.99918; their difference freely rescaled could reach 8.7 per cent of the norm at a '
        'NEGATIVE coefficient, and there is no such freedom because both arms carry the same neutrino sector. '
        'THE HAZARD THE ROW CARRIED IS DISCHARGED -- r6893, and by an accounting rather than by a fourth find. '
        'Three switches had been found verified on a path they reach and used on a path they do not -- the tilt '
        'literal, the baryon density, and the two source terms -- and three by three routes is a RATE, not a count. '
        'The sweep enumerates all SIXTY environment switches the instrument reads, records from the source text which '
        'of the three source constructions and which of the two solver paths reads each, and measures fifty-five of '
        'them on both arms one switch at a time. Fifty-one have a live use site on the reporting path; the nine that '
        'do not come back BIT-IDENTICAL there, all eighteen runs at exactly 0.0, and again at full l reach where DAMPX '
        'and RD would have shown if they touched the damping tail. The set of bit-identical runs is EXACTLY the set '
        'four readings predict -- off-path, rate-identity on the control arm, the arm branch, and gated by another '
        'switch -- with no unexplained null and nothing explained away that in fact moved. TWO THINGS THE SWEEP DID '
        'TURN UP, neither of the r6476 class and neither moving a reported number: LRSFROM moves the instrument '
        'reported r_s by a quarter, 145.38 to 110.49 Mpc, and its spectrum by exactly zero -- R_S and L_A are '
        'DIAGNOSTICS, reaching a print and the SAVE metadata and nothing else, and hier_run accepts l_A, D_M and r_s '
        'and uses none of the three, so r6476 reachability check for that switch was taken on the header and the '
        'header is not the reported number; and LATARG, the corpus one fitted number, has NO ROOT at the arm '
        'adjudicated background, which is why the refit command supplies ZSTART. A consequence worth the right way '
        'round: because no transfer function reads L_A, the printed l_1/l_A agreeing with the sky 220.6/301.7 is an '
        'agreement between two INDEPENDENTLY computed quantities and not a value fed in. DISCHARGE: '
        'a mechanism that raises this arm acoustic oscillation about its own envelope by four per cent where the '
        'control is not raised -- or a demonstration that the monopole-to-Doppler balance cannot differ between the '
        'arms at that size, which moves the search to the unnamed third. r6895 (66) GATES THE SWEEP AND RULES THE CANDIDATE OUT. The hazard clause is discharged by an accounting and not by a fourth find: sixty environment switches enumerated from the source text, fifty-one with a live use site on the reporting path, fifty-five measured on both arms one at a time, and the set of bit-identical runs EXACTLY the set four readings predict -- off-path, rate-identity on the control, the arm branch, gated by another switch -- with no unexplained null. Three shadows by three routes was a rate; it is now a count. AND THE FREE-STREAMING CANDIDATE IS RULED OUT: removing it moves both arms peaks by the same amount, band by band to a fifth of a multipole and in units of each arm own acoustic scale to two parts in ten thousand, while its large effect falls on the ENVELOPE and Delta is a CONTRAST difference -- a correction the two arms share cannot be what separates them. WITHDRAWN IN THE SAME PASS: r6889 uniformity claim, which this seat had landed in P15. The gate behind it compared differences of bin centres whose smallest non-zero spread is 5 against a tolerance of 0.05, so it could not express the difference it tested. TWO CONFIRMATIONS ARE OWED AND ARE NOT ON THE TREE: the LSTEP=2 re-run that would show the non-uniformity is not a property of the grid, and the full-reach re-run of the nine off-path nulls; the receipt fails on their absence rather than reporting the parts it can run as the whole. What stands without them is the sign, the non-uniformity (also established statically) and the arms agreement, that last being a difference taken on one grid with one locator, which a grid property moves alike. What does not is the SHAPE of the rise with multipole. ALSO NAMED SO IT IS NOT LOST: the sweep is of environment switches, and a hard-coded literal that ought to be a switch -- the cc66.17 tilt literal is the standing instance -- is a different search and has not been run. '
        'r6897 (66): THE TWO OWED BANKS LANDED AND A THIRD DEPENDENCY CAME WITH THEM, for a substantive '
        'reason. The fine-grid and full-reach banks are on the tree and the parts reading them pass, but '
        'the finer grid high-multipole half is summed over wavenumber slices, and whether that summation '
        'is valid at the second stage own slicing and reach is a further measurement, banked separately '
        'and not yet pushed -- so the receipt still fails on one bank and the grid-independence of the '
        'rise is still not established. That is the code seat setting its own dependency rather than '
        'declaring the confirmation done, and the hold on the SHAPE of the rise stands unchanged. What did '
        'move is the amplitude own number: an envelope rescale of about a quarter rather than the third '
        'the earlier whole-spectrum move suggested, banked and in the paper. '
        'r6909 (66) RULES OUT THE LOADING READING BY SIGN AND ENLARGES THE RESIDUAL. The chat seat order '
        'proposed that the contrast excess and the alternation excess were one displacement of the '
        'oscillation zero point and enumerated two outcomes; the answer is a THIRD. Both arms offsets '
        'approach the tight-coupling equilibrium -R Psi from below, 0.78 on the control and 0.76 on the '
        'arm, so the absolute question answers no on both and by nearly the same amount. Calibrated '
        'against a KNOWN change in loading -- the control at omega_b +/- 8 per cent with the estimator '
        'tracking 77 per cent of it -- the arm offset FALLS SHORT of what its own loading accounts for by '
        'an effective omega_b of -2.9 per cent. Too much loading is what deepens troughs; this arm '
        'monopole behaves as though it had too little. AND THE ORDER PREMISE WAS WRONG, which this seat '
        'owns: it read the alternation excess against the SKY and the contrast against the CONTROL and '
        'treated them as aligned, where against the control the arm P1/P2 is 2.141 against 2.191, LOWER. '
        'So the two residuals are not one number: the contrast implies +22.9 per cent in effective '
        'loading and the alternation -1.40, a factor of sixteen and opposite signs, with the monopole '
        'offset agreeing with the alternation. And the +22.9 is a LOWER BOUND because the contrast '
        'response SATURATES, spanning only 0.028 across the whole range with increments falling '
        'monotonically, so four per cent is beyond what the baryon density reaches at ANY value. THE '
        'REFRAMING IS WORTH MORE THAN THE ELIMINATION: three channels that would each SHALLOW the '
        'troughs are all larger on this arm -- the monopole offset short of its own loading, the '
        'dipole-to-monopole ratio two per cent ABOVE the control and rising with wavenumber where the '
        'Doppler term fills troughs, and the visibility WIDER at 43.6 against 38.0 Mpc so the arm '
        'averages over more acoustic phase, the two widths side by side on the reporting path for the '
        'first time. So whatever generates the contrast must overcome all three, and the effect to '
        'explain is BIGGER than the four per cent that survives them. The driving is not obviously it '
        'either: the measured grip is 0.1717 against the control 0.1792, weaker, and weaker driving '
        'makes less oscillation. FOUR channels now point the wrong way, which is the sharpest thing the '
        'sector has. '
        'r6911+cc66.40 LOCATES IT, AND IT IS NOT IN THE SOURCE. The order asked for the SAME contrast '
        'statistic at two points in the chain, and the answer is the second branch it named. On the '
        'source at last scattering the arm relative acoustic oscillation is 0.996 of the control; '
        'eta-integrated, 0.992; on the reported spectrum, 1.045 raw and 1.047 banked. Over four '
        'envelope windows, both envelope definitions, three term subsets -- monopole alone, monopole '
        'plus Doppler, the full source -- and with or without the k-measure, the source rungs span '
        '0.971 to 1.005 and the ell rung 1.042 to 1.052, against a statistic floor of 0.6 per cent '
        'set by its own bias on a KNOWN injected contrast. So the excess is manufactured between k and '
        'ell. AND THE FOUR-FOR-FOUR DISSOLVES RATHER THAN BEING SOLVED: nothing upstream overcomes the '
        'four channels because upstream the arm oscillation is very slightly SHALLOWER, which is the '
        'direction all four point. The effect to explain is not bigger than four per cent; it is not '
        'upstream at all. THE NAMED ROUTE IS OUT TWICE OVER. The order premise -- the arms distances '
        'differing by six per cent, 13005 against 13865 Mpc -- belongs to the SUPERSEDED configuration: '
        'at the adjudicated minima D_M is 14017.04 on the arm against 13954.35 on the control, 0.449 '
        'per cent apart and the ARM LARGER, wrong in size and in sign, while the acoustic angles do '
        'agree to 0.085 per cent so the cancellation the order relies on is real. And the route is then '
        'eliminated by measurement anyway: SRCXS projects one arm own source through the other '
        'distance, moving its contrast by -0.63 per cent on the control and +0.59 on the arm, and '
        'REMOVING the difference takes the arm/control ratio UP, 1.045 to 1.051. WHERE IN THE '
        'PROJECTION, as far as the receipt goes: the arm projection retains 1.054 times as much of its '
        'own source oscillation as the control does (0.2543 against 0.2413), the excess RISES with '
        'wavenumber (1.031 below q=3 to 1.065 above) where the source ratio is flat (0.992 to 0.992), '
        'it is not the visibility width acting before the kernel, not the lensing or the binning, and '
        'not the k grid -- KCONT=1 puts the arm on the control kind of uniform grid at the same mode '
        'count with the physics untouched and the excess is unchanged at 1.045. THE ORDER BOUND HAS '
        'NOT MOVED: the receipt locates the stage and offers no mechanism. DISCHARGE, RESTATED BY THIS '
        'RESULT: what within the projection raises this arm contrast by five per cent when its source '
        'oscillation is if anything shallower -- or a demonstration that the projection cannot differ '
        'between two arms whose acoustic angles agree to a part in a thousand, which would make the '
        'five per cent an instrument fact rather than a physical one and is the first thing to rule '
        'out. A GUARD THAT PAID: r6885 geometric envelope cannot be carried to the source at all, the '
        'source power coming within a part in 10^8 of its own median at the troughs, so the envelope is '
        'an arithmetic mean at every rung and both are reported. '
        'r6915+cc66.41 EXCLUDES THE CROSS TERM AND FINDS THE EXCESS IN EVERY PROJECTED TERM AT '
        'ONCE. The order asked which term carries it after projection and named the '
        'monopole-Doppler pair first, j_l and j_l-prime being a quarter period out of phase. '
        'ITS CLOSURE GATE HAD TO BE CORRECTED BEFORE IT COULD BE PASSED: the TRANSFER is linear in '
        'the source and the pieces add there, but C_l is QUADRATIC in the transfer, so the '
        'projected SPECTRA cannot add -- the four diagonal pieces alone fall short of D_l by up to '
        '46 per cent. That is not the order third outcome; its FIRST outcome presupposes a cross '
        'term, so the two clauses are in tension and the first is the coherent one. What closes is '
        'the full bilinear decomposition, ten pair spectra summing to D_l to 1.1 and 1.3e-15 '
        'relative on the two arms. AND THE CROSS TERM IS NOT THE CHANNEL: deleting it moves the '
        'ratio from 1.0452 to 1.0451, and over four envelope windows its carry runs -0.0013 to '
        '+0.0008 of the +0.045, bounded at about a part in a thousand. BECAUSE EVERY PROJECTED '
        'PIECE ALREADY CARRIES IT, which is neither outcome named: monopole 1.034, Doppler 1.099, '
        'polarisation 1.058 against the full 1.045, the ISW alone the exception at 0.989 and worth '
        'one per cent of D_l. So it is not a term and not a pair of terms -- the projection raises '
        'this arm contrast on nearly everything it projects. THE LADDER IS THE SHARPEST FORM OF '
        'IT: every term SOURCE ratio is at or below 0.992 and every term PROJECTED ratio is '
        'higher -- monopole 0.992 to 1.034, Doppler 0.973 to 1.099, ISW 0.972 to 0.989, '
        'polarisation 0.990 to 1.058. AND THE SPLIT THE ORDER REASONING WAS AFTER is about 40/60 '
        'with the response the larger: the weights do differ, the arm monopole share 0.5225 '
        'against 0.5092 and its Doppler 0.1753 against 0.1840, and rebuilding the arm pieces at '
        'the control shares gives 1.0267, so the weights carry +0.019 of the +0.045 and each '
        'piece own response +0.027, the reverse construction agreeing at +0.020. AND THE RETAINED '
        'FRACTION IS NOT FLAT IN q: it rises from 1.030 in the lowest band to 1.089 in the '
        'highest, slope +0.0139 +- 0.0021 per unit q over twelve settings and never once negative, '
        'so the branch that would have killed the reading is excluded; the intercept is '
        '1.017 +- 0.010 and straddles one, so the rise is established and a constant offset is '
        'not. DISCHARGE, NARROWED AGAIN: what makes the projection treat the two arms differently '
        'on EVERY term at once and increasingly with wavenumber -- not a term, not a pair, not '
        'their interference, and not the distance, the grid, the lensing or the visibility width '
        'acting before the kernel. The first thing to rule out is still whether a projection CAN '
        'differ between two arms whose acoustic angles agree to a part in a thousand, which would '
        'make the five per cent an instrument fact rather than a physical one. '
        'r6919 (66) TAKES BOTH CORRECTIONS cc66.41 MADE TO ITS ORDER, AND BOTH ARE THIS SEAT S. '
        'The closure gate said the separately projected pieces must sum to the full spectrum: the '
        'TRANSFER is linear and the pieces add there, but C_l is QUADRATIC in the transfer so the '
        'projected spectra cannot, the four diagonal pieces alone falling short of D_l by up to 46 '
        'per cent and gated as a measurement. And the order own two clauses were in tension, its '
        'first outcome presupposing a cross term while its third called a failure to sum the '
        'finding; cc66 took the coherent one and built the gate the order should have asked for, ten '
        'pair spectra closing on D_l to a part in 1e15. The cross term itself, this seat lead '
        'hypothesis argued from j_l and j_l-prime being a quarter period apart, is EXCLUDED at about '
        'a part in a thousand. AND WHAT REPLACES IT IS BIGGER THAN WHAT IT KILLED: every term source '
        'ratio is at or below 0.992 and EVERY term projected ratio is higher, so the excess is not '
        'localised in the source at any grain -- not a term, not a pair, not their interference, the '
        'projection raising this arm contrast on nearly everything it projects. And with the '
        'intercept straddling one while the slope never does, an overall normalisation difference is '
        'excluded by the same fit that establishes the rise: the projection does nothing different '
        'at the longest acoustic wavelengths and more of it at each shorter one. THE REFRAMING: '
        'write the spectrum as an integral of S against j_l(k chi(eta)) over eta. Every term '
        'decomposed so far lives in S and what raises this arm contrast is common to nearly every S '
        'there is, so two things are left and neither is a source term -- the kernel, the same '
        'function on both arms, and chi(eta) with the visibility weight in eta, which together are '
        'the EFFECTIVE WIDTH the projection averages over: term-independent by construction and '
        'growing with wavenumber because at fixed width there are more acoustic periods to average '
        'away at each shorter one, going to no difference at all as the window falls below one '
        'period -- which is the measured intercept. The candidate is named so it can be killed: '
        'this construction carries TWO RATES, the plasma accumulated lengths on the leaf and '
        'comoving separations read across leaves on the stacking, so the source is accumulated on '
        'one clock while the kernel argument is a distance read on the other -- A CANDIDATE AND NOT '
        'A CLAIM, with nothing yet checked about what the instrument integrates against what. ORDER '
        'ROUTED: feed both arms the same analytic oscillating source, no transfer and no terms, and '
        'measure the retained fraction against q -- reproducing the 1.054 and the +0.0139 shows the '
        'source is irrelevant to the effect, failing to shows it is in how S sits across the '
        'visibility -- then swap the visibility and chi(eta) one at a time, with an ill-posed swap '
        'to be reported as ill-posed rather than forced. '
        'r6919+cc66.42 ANSWERS BOTH AND RELOCATES THE CANDIDATE. THE SOURCE IS IRRELEVANT TO IT: a '
        'pure g(eta) cos(k r_s(eta)) with no transfer, no terms and no weights, projected through '
        'each arm own kernel, visibility, k grid and multipole grid, gives an arm-to-control '
        'retained ratio of 1.066 at a slope of +0.0226 per unit q against the real source 1.054 and '
        '+0.0139 -- the geometry accounts for the whole of the effect and over-delivers. The '
        'injection phase does not matter, 1.066 and +0.0225 at phi = pi/2, and a STANDING oscillation '
        'already carries most of it at 1.059 and +0.0119. AND THE NAMED CANDIDATE IS IN THE '
        'INSTRUMENT BUT NOT WHERE THE ORDER PUT IT: x0 = eta_0 - EE on both arms, so chi(eta) = '
        'eta_0 - eta and d chi / d eta is identically one on each with no rate touching x0 on any '
        'path, and there is nothing there to exchange. THE TWO CLOCKS SIT BETWEEN r_s AND eta -- '
        'conformal time, and so x0, is built from Hphys the STACKING rate while the acoustic phase '
        'accumulates on the LEAF rate; Jac = d eta_leaf / d eta_stack is 1.000000 everywhere on the '
        'control by the rate identity and runs 0.789 to 0.913 across three FWHM on the arm. AND THAT '
        'IS WHERE THEY PART COMPANY: across the visibility FWHM the accumulated SOUND HORIZON agrees '
        'to 0.08 per cent, 17.3074 against 17.2941 Mpc, while the COMOVING DISTANCE differs by 14.6 '
        'per cent, 38.042 against 43.591. The leaf clock makes r_s accumulate more slowly per unit '
        'eta, so a fifteen per cent wider window covers the SAME acoustic phase while the kernel, '
        'which reads chi, sees the wider window. THE JOINT OBJECT IS d r_s / d chi ACROSS THE '
        'VISIBILITY, the sound speed the kernel sees: 0.4550 on the control against 0.3967 on the '
        'arm, 12.8 per cent lower -- term-independent, growing with wavenumber, and vanishing for a '
        'window under one acoustic period, the three properties cc66.41 measured. AND NEITHER SWAP '
        'CLOSES IT ALONE, which is the third outcome the order named. The CLOCK swap is ILL POSED as '
        'an isolation and the statistic says so rather than returning a null: forcing both arms onto '
        'the stacking clock MOVES THE COMB and the regression alternates in sign band by band, +0.37 '
        'to -0.57 -- cc66.40 guard firing on exactly the shape it was built for, and itself evidence '
        'that the leaf assignment is what the arm reported peak positions need. The WIDTH swap is '
        'well posed and OVERSHOOTS BY EIGHT: giving each arm the other FWHM takes the slope from '
        '+0.0226 to +0.0931 while barely moving the mean, so the width sets the shape and not the '
        'level. DISCHARGE, NARROWED TO ONE RATIO AND NO LONGER A PROJECTION QUESTION: why this '
        'construction assigns the scales the plasma accumulates and the distances the kernel reads to '
        'DIFFERENT RATES, which is P15 sec:tensions own question. The five per cent is no longer '
        'unexplained -- it is the instrument doing what the corpus two-rate assignment tells it to, '
        'and what is open is whether that assignment is right. '
        'r6925 (66) GATES IT AND AIMS THE NEXT ORDER AT THE GAP IN THE RULE: the rule covers '
        'separations read across leaves and scales the plasma accumulates, AND THE VISIBILITY IS '
        'NEITHER -- tau is accumulated by the plasma but differentiated per unit eta, which is built '
        'from the stacking rate, so g is a MIXED object and nothing says which clock it is a density '
        'in, which is where the 12.8 per cent lives. ORDER: locate every place the visibility and the '
        'optical depth touch a rate, recompute d r_s / d chi under the other admissible assignment, '
        'and report the comb beside the contrast. Plus one number on why the injection OVER-delivers, '
        'since the source partially CANCELS the excess and may be cc66.40 own 0.992 deficit. '
        'r6925+cc66.43 FINDS THE GAP ALREADY OPEN IN THE CODE AND THE GEOMETRY INVARIANT UNDER IT. '
        'The rate rule does not say which clock g = tau-prime e^-tau is a density in, and the '
        'instrument already answers that twice and differently: every site where tau or g touches a '
        'rate is on the STACKING clock -- the recombination history against Hphys, tau-prime on eg, '
        'tau over the eta grid, eta_LS and its FWHM off that grid -- while 1/k_D^2 IS Jac-weighted '
        'under LEAFSCALES. So the diffusion length takes the leaf clock and the optical depth the '
        'stacking clock, two objects on the same side of the rule on opposite clocks with nothing '
        'stating the choice. VISLEAF=1 applies to tau exactly the weighting 1/k_D^2 applies to '
        'itself, which is what makes the other assignment admissible rather than invented. ON THE '
        'GEOMETRY THE TWO AGREE: d r_s / d chi goes 0.396733 to 0.396957 on the arm, so 12.80 per '
        'cent lower becomes 12.75, a move of 0.06 per cent, and the control does not move at all -- '
        'and structurally rather than luckily, since it is a RATIO of two accumulations across the '
        'SAME window so re-weighting the measure re-weights both. The visibility is not where the '
        'freedom is and the 12.8 per cent is forced by the rule as stated. BUT THE CONTRAST AND THE '
        'COMB DISAGREE AND NEITHER IS PICKED: read alone the other assignment moves the injection '
        'retained ratio 1.0850 to 1.0695 and its slope +0.0242 to +0.0133, TOWARD the real source '
        '1.0694 and +0.0117; but the arm first peak moves 220 to 228 and l_1/l_A 0.7290 to 0.7555, '
        'AWAY from the sky 0.7312, with P1/P2 2.142 to 2.017 and the control comb bit-identical. And '
        'the contrast improvement is partly that same move read by the statistic: band by band the '
        'VISLEAF=1 ratio is non-monotonic scatter with a fitted residual NINE TIMES the current '
        'assignment, because moving eta_LS moves r_s(eta_LS) and so moves the comb -- cc66.40 guard '
        'firing a third time. The comb is the only one of the three readings with an external '
        'referent and it supports the assignment the instrument already has. AND THE SOURCE '
        'CANCELLATION IS HALF THE LEVEL AND NONE OF THE SLOPE: the injection times cc66.40 measured '
        'source deficit, 0.9922 and FLAT in q at -0.00106, gives 1.0766 at +0.02296 against the real '
        '1.0694 at +0.01167 -- 54 per cent of the level gap and 10 per cent of the slope gap. So the '
        'four trough-filling channels account for about half the level and essentially none of the '
        'slope, and the sector does NOT close into one account; what flattens the slope is the real '
        'source own eta-dependence across the visibility, which is what the injection replaced. '
        'DISCHARGE, UNCHANGED IN SUBSTANCE AND SHARPER IN FORM: whether the two-rate assignment is '
        'right. What this revision adds is that the rule as stated does not determine the '
        'visibility clock, that the instrument two plasma-accumulated objects are already on '
        'opposite clocks, and that the peak positions support the choice it currently makes. '
        'r6929 (66) GATES IT AND PROMOTES THE COMB TO ARBITER, WHICH MEANS MEASURING WHAT IT CAN '
        'DECIDE. The seat cancellation hypothesis is 54 per cent of the level gap and 10 per cent of '
        'the slope, so the four trough-filling channels are about half the level and essentially none '
        'of the slope and THE SECTOR DOES NOT CLOSE INTO ONE ACCOUNT. And one near-miss is kept '
        'because it is a class and not an incident: a launcher positional-argument bug ran thirty-six '
        'slices as the unset switch, and they COMPLETED, REPORTED NOTHING WRONG AND REPRODUCED THE '
        'BANKED SPECTRA -- the shape that gets banked as an answer, the same family as r4558 unwired '
        'knob and cc66.36 knob shadow. ORDER ROUTED: scan the assignment CONTINUOUSLY rather than as '
        'two settings, letting the weighting on tau run from the stacking clock to the leaf through a '
        'one-parameter family, and report l_1/l_A against the sky 0.7312, the retained fraction and '
        'its q-slope, and d r_s / d chi against that parameter. A steep comb with a shallow contrast '
        'pins the assignment and answers the row question; both shallow, or the comb spread inside the '
        'sky own locating spread, means THE COMB CANNOT ARBITRATE and retracts the sentence the '
        'receipt leaned on, which is worth more than the scan; an intermediate fraction fitting the '
        'comb better is a FITTED CLOCK and a new free parameter the no-early-parameter claim would '
        'have to answer for, which is why it is measured rather than assumed absent. Plus the '
        'switch-marker smoke test made standing rather than per-launcher.'),
    'PO-55': ('horizon entropy is reading-dependent under the central move', 1, 1, 3, None,
        'OPENED r6877 as PO-54 remainder, found by node 60 where the order was not looking. The causal reassignment '
        'relates two readings of one geometry whose horizon areas are GENERICALLY UNEQUAL, and PO-48 established that '
        'the area law carries at the substrate horizon -- together making horizon entropy reading-dependent, while '
        'P17 quotes 3 pi/(Lambda l_P^2) as the ledger own number back without saying it is the value in ONE reading. '
        'Not a contradiction, since the morphism is causal and structural and carries no metric data, so nothing '
        'computed is wrong: what is missing is the qualification, at the one place the corpus computes an entropy. '
        'DISCHARGE: say which reading the quoted entropy belongs to, whether the other reading value is computable, '
        'and if they differ whether anything depends on the difference. Not independent of PO-53, struck at r6871 -- '
        'the debt rests on the offset family being solutions rather than sections, now settled, so it is live rather '
        'than conditional.'),
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
        'r6766: AND THE BARYOGENESIS-ANALOGUE DATUM P15 NAMES AS OPEN CANNOT BE REACHED BY THE ONE '
        'MECHANISM THE CORPUS HOLDS FOR IT. r6762 gave the constituent count a current of coefficient '
        '3 whose violation integrates to the change in a member s gravitational Chern-Simons number -- '
        'the right shape for a net count produced across a history. It never moves on this one. ALL '
        'FOUR COMPONENTS of the Chern-Simons current vanish identically on the general DYNAMIC '
        'spherically symmetric class, so the number is zero at every slice rather than merely unchanged '
        'between two -- the r=0 branch-point crossing included, where a merely divergence-free quantity '
        'could have jumped. The path is fixed three ways: P16 states the spherically symmetric class as '
        'a PREMISE and forbids dropping it while keeping the branch-point locus; the source vanishes '
        'class-wide with every profile left arbitrary; and the twisted member s transverse block is a '
        'TORUS against this history s closed S^3, which no deformation joins. The tensor sector is '
        'answered too: a travelling wave gives exactly zero at any polarisation, and the only nonzero '
        'source is the parity-odd product of the two polarisation rates, which averages to zero on a '
        'parity-symmetric state. Net count 3 x 0 = 0. No photon number is supplied or invented and none '
        'is needed for the verdict. What a successor must supply is a chiral STATE on the S^3 layer, '
        "where P10 already put the question, and not a chiral MEMBER.  r6805 NARROWS IT: the row now has a NUMBER to hit. The like-for-like refit -- both arms free in H0, Omega_m, omega_b and n_s on one set of bins -- has this arm preferring n_s = 0.9949 against the control's 0.9559, bluer by 0.039. Before this the tilt was read off a background fitted to the other arm, so a derived tilt near 0.96 would have looked like success; the ordering is reversed and it is measured. PROVISIONAL IN ONE RESPECT: the refit ran on l<1290 because the full-range container could not complete a grid and cutting the k-reach was refused by the convergence guard, and the damping tail is where a tilt has most of its leverage -- the full-range refit is running and is what fixes the target rather than indicating it. r6823 NARROWS IT FURTHER, on node 60's r6812: the collapse leg is NOT A CANDIDATE for the tilt. On the leg both the potential and the effective temperature are functions of x = k eta / sqrt3 alone, so a handover at a fixed PHASE is exactly scale-free -- the ratio of amplitudes at two wavenumbers is 1, not nearly 1. A fixed-TIME handover is the only place a scale survives and what it gives is red in both channels and goes as k^2, which is a RUNNING and not a tilt: the target 1-n_s = 0.005 needs x = 0.05, and thirty times that wavenumber -- inside the refit's own band -- gives 41.9. On the adjudicated configuration it is exactly zero, both log-derivatives vanishing quadratically at the crossing. So the row is no longer 'where does the leg's tilt come from': the leg is a k-independent amplitude and nothing else, the tilt is wholly the progenitor's vacuum, and what remains is what the progenitor supplies -- with the target measured at one end of it. r6829 NARROWS IT AGAIN, on node 60's r6826: the substrate alone fixes n_s = 1 EXACTLY. Of the three candidate scale-breakers, two are one candidate and both fail -- in conformal time the mode equation carries no length, so the curvature radius enters only as the amplitude prefactor and reaches the tilt for NO value of it, and on the forced member the progenitor's mass IS that radius up to a pure number (M/alpha fixed at Nariai), so it is not an independent scale. The third, the collapse's finite duration, enters and does not tilt: exact Bogoliubov coefficients whose log-derivative oscillates with a decaying envelope, sign-alternating across the band -- a scale and not a tilt, by the same test that closed the leg. ONE CHANNEL IS LEFT and it has an exact answer: n_s - 1 = 3 - 2 sqrt(9/4 - m^2 alpha^2), blue for m^2 > 0. The measured 0.995 is nearer unity than the standard model's value but from BELOW, so it asks the interior for a slightly negative m^2 alpha^2 -- a REQUIREMENT on the progenitor, not a result about it, and nothing was tuned. The row is now what the interior gives for m^2 alpha^2. r6857 (66), on node 60 r6846: THE INTERIOR'S VACUUM IS BLUE EVERYWHERE AND A RUNNING. The interior was not newly built -- its background and mode problem were already banked and the order's potential reduces to the banked one exactly. Solved there, the potential interpolates between the scale-free matter form and a radiation form that is not, so the spectrum breaks at the wavenumber the radiation content sets: log-slope running +0.30 to +1.98 across the observed band, tending to the radiation value +2. A running and not a tilt, and blue at every wavenumber -- flattest +0.304 against a measured -0.002, wrong sign and about a hundred times the size, with the flattest slope going as the radiation fraction so that exact scale-invariance is the pure-dust limit and reaching red would need it negative. AND THE REQUIREMENT r6826 HANDED THE INTERIOR IS WITHDRAWN: 3-2 sqrt(9/4 - m^2 alpha^2) comes from a 1/eta^2 potential with a dimensionless coefficient, which is what makes it a power law, where the interior's carries a scale -- so the slightly negative m^2 alpha^2 was an artefact of applying the substrate's template off the substrate. FOUR CHANNELS ARE NOW CLOSED (substrate, collapse leg, finite duration, interior vacuum) and the measured red tilt is supplied by none of them: the row is harder than it was, not nearer. r6909 (66, on node 60 r6898): ONE CANDIDATE CLOSES AND THE ROW STAYS OPEN. The transfer from the progenitor vacuum to the boundary datum is NOT a second place a wavenumber can enter -- the interior transfer and its vacuum spectrum are ONE OBJECT, reproducing the banked log-slope to three figures at the top of the band when run at the determined rho. And the one step genuinely untested, the crossing, carries no wavenumber exactly: the origin is a resonant regular singular point whose logarithmic coefficient is 1/rho with zero derivative in k, because k^2 is REGULAR where the potential is SINGULAR and first enters the analytic solution at third order. AND THE APPARENT CONFLICT IN THE BANKED WORK IS A DOMAIN, NOT A CONTRADICTION: the potential breaks at a wavenumber the radiation content sets, the banked scale-invariance check ran with its whole band BELOW that break where it passes to a fifth of a per cent, and at the determined rho the observed band lies ABOVE it -- one object, two bands, and that is the correct reconciliation. A WITHDRAWAL THAT RUNS THE OTHER WAY: r6846 reconciled the two by calling them different objects and that is withdrawn, and the seat records that its three previous withdrawals all ran toward making the construction look indebted while this one let a conflict pass -- the more useful half, because a bias that only ever runs one way is invisible from inside it. A BOUNDED CONSEQUENCE carried into the paper rather than left in the receipt: the vacuum amplitude was read off the scale-free branch, and on the observed band the residue is some thousands larger in power, which moves the shortfall by a few orders out of a hundred and three and leaves the conclusion where it is. What is left is unchanged: what supplies a red, near-constant tilt, with four channels closed and now one closed transfer. r6913 (66, on node 60 r6912) TURNS THE ROW OVER: THE TRANSFER IMPRINTS, so every channel closed so far was a correct answer to a MIS-AIMED question. Measured on unit incoming amplitude so that what comes out is the multiplier itself, d lnT/d lnk runs -0.866 at k=7 to -0.010 at k=1400: a spread of 0.856 across the observed band, so the transfer is NEITHER SCALE-FREE NOR EVEN A POWER LAW, and what it adds to any spectrum tilt is twice that, -1.73 to -0.02. The banked exact scale-invariance is the LOW-k LIMIT of that same function rather than a separate fact: below the break the slope tends to -1 (-0.9992 at k=0.3) and kT(k) to the constant 27.86, and P ~ k^3 |c_0|^2 is scale-invariant exactly where the slope is -1. The decomposition is an IDENTITY, s(k) = d ln(|c_0| k^3/2)/d lnk = d lnT/d lnk + 1, so the whole k-dependence is the transfer and the constant is the normalisation, reproducing r6898 +0.134 and +0.990 from the transfer alone; and it is the same function for every input, five inputs including one deliberately not a power law agreeing in output-minus-input slope to 4e-13 with linearity VERIFIED to 7e-15 rather than invoked. AND 60 CORRECTED THIS SEAT OWN STATEMENT OF THE OUTCOME: the order wrote that no input can give a red near-constant tilt through this interior whatever the progenitor supplies, and as written that is too strong -- an input whose own running is the transfer negated comes out red and near-constant by construction. What is true is weaker and sharper: no POWER-LAW progenitor spectrum can, and the input that would work is a specific computed function that must itself run by 1.71 across the band, opposite in sense to the transfer. THAT IS A REQUIREMENT ON THE PROGENITOR AND NOT A RESULT ABOUT IT, the same shape as r6826 m^2 alpha^2 = -0.0075 which this line later withdrew as an artefact of the wrong template, so it is named a requirement at the outset. SO THE CHANNEL HUNT IS OVER EITHER WAY: five channels were closed -- substrate, collapse leg, finite duration, interior vacuum, transfer -- and each answered what tilt does the VACUUM give, while P15 holds twice over that the perturbations here are classical and non-vacuum. AND THE INSTRUMENT OWN LIMIT IS NAMED RATHER THAN FOUND AFTERWARDS: the mode starts at x_i = 300/k, outside the break only while 300/k > 2 rho, so the band is bounded at k < 2783 and the bound is the premise not the arithmetic; an earlier pass reading T above 1 at k = 1e5 is DISCARDED as a misplaced initial condition. The slope is claimed and the amplitude is not, and nothing here bears on A_s. DISCHARGE, restated: the row is no longer a search for a channel. It wants a progenitor whose spectrum runs by 1.71 across 7 < k < 1400 opposite in sense to the transfer -- the modelling task this row has carried since r4163, now with its input SPECIFIED rather than merely awaited, and naming the requirement is not meeting it. r6917 (66, on node 60 r6916) BOUNDS IT AND ATTRIBUTES IT. Substituting x = 2 rho u gives v_uu = (2/(u(u+1)) - kappa^2) v with kappa = 2 rho k: the potential in u carries NO rho and rho and k enter only through kappa, so the log-slope is a UNIVERSAL FUNCTION OF ONE VARIABLE -- verified to 7e-13 across a factor 100 in rho -- and the break sits at a fixed kappa, making k_break = kappa*/(2 rho) exact. AND THE HIGH-k LIMIT IS EXACTLY ZERO, DERIVED WHERE THE INTEGRATION IS NOT TRUSTED: near the crunch the potential is P/x with P = 1/rho and with x = s/k the equation is the repulsive L=0 Coulomb wave equation, whose irregular solution amplitude gives d lnT/d lnk -> -pi/(4 rho k) -> 0 as 1/k, matched to 1.5 per cent at four (k, rho) pairs all inside the x_i = 300/k premise with no integration above k = 2000 performed or quoted. SO THE EXCURSION IS EXACTLY 1, what the transfer adds to a tilt is AT MOST 2, and no band however wide can require a progenitor running above 2 -- the observed band asking 86 per cent of that hard maximum. AND THE REQUIREMENT IS THE RADIATION FRACTION S: on stated criteria, the midpoint -0.5 gives kappa* = 2.729 and needs rho < 9.7e-4, the stricter -0.95 gives kappa* = 0.400 and rho < 1.4e-4, so a working rho EXISTS and sits 55 to 378 times below the determined 0.0539. The requirement therefore stands because the DETERMINED radiation fraction puts the observed band that far above its own break, and the conspiracy question has a shape rather than an answer: both runnings are set by the same object, the break at kappa ~ 1, so a progenitor that cancels the transfer is a progenitor whose own spectrum breaks where the interior does -- a structural CANDIDATE with nothing showing any progenitor does it. And 1.71 survives as 1.71-1.72: it moves 2.3 per cent over the plus-or-minus six per cent the arm distance mapping allows, but the differencing convention alone moves the third digit, and that 0.7 per cent method spread is part of the answer. THE FLAGGED MASS DISCREPANCY RESOLVES IN P16 S FAVOUR: P16 own two statements compose to rho = sqrt(2 a_eq/M), which 60 read against THE_REGISTER 2.33e23 Msun for a factor 3.3 -- but that figure was never a determination, PO13_WORKING_STATE recording it as a sanity check on the observable universe mass, while P16 determined 4.3e52 kg satisfies the identity to 0.4 per cent. So the composition is a consistency check P16 had never run on itself and passes; the verdicts scored on the stand-in are unmoved, the over-extremality threshold reading 1.001439 against 1.000134.  DISCHARGE, unchanged in kind and sharper in content: a progenitor whose spectrum runs by 1.71-1.72 across 7 < k < 1400 opposite in sense to the transfer, which is now known to be a progenitor that breaks where the interior does."
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
        'r6793 NARROWS IT: the structural legs stand and every quantitative leg was computed on a signature '
        'that has since changed size and can change sign. The signature is theta_D/theta_* = r_D/r_s, the '
        'projection cancels from it, and it depends on exactly two choices -- where the plasma is handed over, '
        'and how far the diffusion integral is carried. At the branch point with both scales on the leaf rate '
        'it is +2.2 percent taken to recombination and -0.9 percent taken to the visibility peak, against the '
        '+8.2 percent every number in this row was computed on, which belonged to a fitted-onset handover with '
        'a tuned sound horizon. WHAT STANDS: a tilt is a power law and the signature is a Gaussian, so '
        'absorption is window-local and no tilt removes it; the mimicked tilts slope runs by (lmax/lmin)^2 over '
        'the fitted range; n_s is inherited boundary data, so a displacement in it is a different input and not '
        'by itself a tension; the residual after the joint fit is the predicted Gaussian to a correlation of '
        '1.000000; and the early-ISW leg does not reach the multipoles the question lives at. None of these '
        'turns on the magnitude. WHAT DOES NOT STAND AS A NUMBER: the per-bin residual, the tilt displacement '
        'and the likelihood cost all scale with r^2-1, which is 0.045 at the adjudicated configuration against '
        '0.171 at the ratio they were computed on -- a factor 3.8 smaller, and of the opposite sign on the '
        'other endpoint. P15 sec:diffusion-scale now states the scaling and the two endpoints rather than the '
        'superseded figures. WHAT WOULD DISCHARGE IT: the joint fit re-run at the adjudicated signature on both '
        'endpoints, reporting the per-bin residual and the displacement with its window -- and since the sign is '
        'the endpoints, WHICH ENDPOINT the corpus reads r_D to is a question for the papers and not for the '
        'instrument. r6797 SETTLES THE ENDPOINT by the same consistency that fixes the rate assignment: theta_D/theta_* '
        'is a ratio of two lengths the plasma accumulates, and a ratio of integrals taken to different epochs is not a '
        'ratio of anything -- the observed angle is read at last scattering, the peak of the visibility function, so '
        'both r_s and r_D terminate there. The +2.2 percent was r_s anchored at the observed angle against r_D taken '
        'to a sharp recombination cut; the common-endpoint reading is -0.9 percent and the papers carry it. The re-run '
        'narrows to one configuration, not two.'),
    'PO-43': ('the Weyl-squared coefficient at second order in the shear', 1, 1, 5, None,
        'r6415/r6435/r6471: the coefficient is COMPUTED -- 1/60 in units of (4pi)^-2, exactly twice a real minimally co '
        'upled scalars, the tower being two such degrees of freedom by P10s own description. Stated on the PHYSICAL-M '
        'ODE count, the constraints here being solved rather than gauge-fixed, which is where it is attackable. And the '
        ' invariant it multiplies was corrected: C^2 = 2 sum (sigma + H sigma)^2, two more derivatives than the 4 sigm '
        'a^2 P10 stated, so it grows as omega^2 sigma^2 for a mode. BOTH replacement questions are answered: the connec '
        'ted-isometry one by PO-44s strike, and the topological-terms one at r6471 -- the ledger does not count them,  '
        'its statement being the geometric gauges and the closing of the one extension freedom.  r6849 (66) ANSWERS QUESTION (ii) FROM P17 OWN TEXT: sec:ledger partitions the constants two ways -- the real-geometric gauges c, '
        'Lambda, G, each a nameable feature of the substrate and its cuts, and the thermal hbar, k_B whose CR content '
        'is the closing of the ONE quantum freedom, the self-adjoint extension. A topological coefficient is neither: '
        'it names no feature of the substrate and it is not the extension, so counting it would be counting a '
        'different kind of thing under the same name. WHAT REMAINS is one unrun check and one declined question, '
        'neither of which is the row title: whether Hartle-Hawking regularity imposed fibre by fibre populates the two '
        'helicity towers alike, in which case the parity-odd content cancels and the entry is not owed at all; and '
        'whether S = A/4 carries to a cosmological horizon, which P17 declines in terms. The row cannot close above '
        'the check, and the check is routed to the code seat.'
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
        'r6925 (66, on node 60 r6920) ATTEMPTS THE ROW FOR THE FIRST TIME AND THE ONE ULTRAVIOLET '
        'CONSTANT BECOMES OBSERVABLE. THE SEAT REASON WAS WRONG WHERE ITS ANSWER WAS RIGHT: the '
        'degeneracy needs R sqrt(g)-almost-everywhere CONSTANT, not the cosh, and two non-cosh things '
        'keep it so -- Lambda with radiation, and THE FREE TOWER OWN BARE ZERO-POINT ENERGY, which is '
        'exactly radiation-like -- so the naive back-reaction of the quantized tower breaks nothing. '
        'Both are kept as NULL CONTROLS measuring rank 1 to 1e-43, which is how the numerical floor is '
        'measured rather than assumed. WHAT BREAKS IT IS THE LOG, WHICH IS TO SAY THE CONSTANT AT '
        'ISSUE: Z(s) has a pole at s = -1 with residue 39/4, the ln a it puts in the energy spoils the '
        'exact a^-4 that made the bare sum traceless, and the resulting trace r/(2 pi^2 a^4) is '
        'INDEPENDENT of mu -- scheme-independent, which is what an anomaly is, and the reason the '
        'constant-over-log split being a convention does not touch it. Rank 3 at 9.06e-8, thirty-five '
        'and a half decades above the measured floor, the departure SIGNED by I2 I0 - I1^2 = I0^2 '
        'Var(R) >= 0 and the gap going as r^2. AND THE SHAPE OF IT IS THE RESULT: the no-free-constant '
        'claim was saved on this background BY a degeneracy, and that degeneracy is switched off by '
        'exactly the constant it was hiding -- were there no log R would stay constant and the '
        'counterterm unobservable, but then there would be no constant to hide, so the saving '
        'mechanism and the thing it saves us from are the same number. The basis is one-dimensional AT '
        'FIXED BACKGROUND and two-dimensional once the scale factor is quantized, which sharpens this '
        'row own CR-specific claim rather than generalizing it away. ITEM TWO ANSWERS AS A THEOREM: '
        'zeta(0) = 10 + B3prime(0)/2 exactly, immune to every constant shift, every multiplicative '
        'rescaling -- containing r6411 the-scale-factor-factors-out as the single case L = a^-2 -- and '
        'every even power of 1/m, moving only on an ODD power of the mode label, so with local '
        'operators contributing integer powers of the Laplacian the whole even sector is foreclosed. A '
        'reason to expect 10 survives coupling and not a proof that it does. THE WALL, LOCATED: the '
        'back-reaction is SEMICLASSICAL and the interacting theory is not built, as ordered, and what '
        'higher orders could do is narrow since restoration would need the TOTAL trace exactly '
        'constant, a pure cosmological term, which an a^-4 anomaly is not. ONE PREMISE IS TAKEN AND '
        'NOT PROVED, that the coupled sector admits states without a definite alpha -- were the '
        'physical Hilbert space to select a single background the degeneracy would survive, and that is '
        'THE SINGLE WAY THE FINDING REVERSES. DISCHARGE, now routed: does the deparametrized Hilbert '
        'space carry a superselection rule in alpha, with controls built first, since a superselection '
        'claim with no measured floor is an unfalsifiable one. The row moves from NEVER ATTEMPTED to '
        'ATTEMPTED WITH THE WALL LOCATED, and it does not close. '
        'r6929 (66, on node 60 r6928) SHOWS THE PREMISE WAS NEVER A DEPENDENCY, ON A THIRD BRANCH '
        'NEITHER SEAT ENUMERATED. The order costed superselection in alpha as reversing the finding '
        'and non-superselection as leaving it proved; THE TWO ARE NOT ALTERNATIVES. A superselection '
        'rule forbids COHERENCE between sectors and not an ENSEMBLE over them, and the three integrals '
        'are read off the ensemble linearly, so an ensemble over three distinct alpha reaches rank 3 '
        'at 1.60e-4, 39 decades above the floor, INSIDE a superselected theory and with no anomaly at '
        'all. And the finding took neither route: two exact rank lemmas separate them, R constant on '
        'one history giving rank 1 for any number of regions and an ensemble over N distinct alpha '
        'giving rank exactly min(N,3), checked at N=2 with the third singular value at 8.2e-72 -- and '
        'the anomaly reaches rank 3 at N=1, where mixing caps the rank at 1. AND THE QUESTION AS PUT '
        'HAD NO OBJECT: alpha = sqrt(3/Lambda) is a COEFFICIENT of H_phys, so alpha-hat is central '
        'with a ONE-point spectrum against the control three, and a central operator with one point '
        'decomposes nothing; a-hat, which R actually depends on, is central in nothing, the commutator '
        'with H_phys being exactly the kinetic one at every order with residual 7.8e-13 against a '
        'floor of 7.7e-12 measured on eighteen members of the coupling family; and the theory one '
        'genuine superselection label is Gamma-hat, central in the RADIAL algebra with seven spectral '
        'points, labelling the boundary condition and not the background scale. CENTRALITY IS A '
        'RELATION TO AN ALGEBRA, which is the two-sided control. AND IT CORRECTS THE LINE OWN LANDED '
        'WORK IN THE DIRECTION OF FEWER WALLS: r6920 section E listed as a wall that if the physical '
        'Hilbert space selected a single background the degeneracy would survive, and that clause is '
        'FALSE -- with a single background the rank is 3 at 9.06e-8, which is r6920 own headline '
        'computed at a single Lambda. The wall list is shorter by one item, and P10 carried the chat '
        'seat version of the same clause, which is out. DISCHARGE, now routed: what does need the '
        'coupling is a different question -- whether any physical state makes R-hat sharp, i.e. '
        'whether spec Theta-hat has a point spectrum. Continuous spectrum makes the independence a '
        'statement about the ensemble the state already is; point states make the counterterm '
        'observable in the ordinary sense; and which of the two P10 may claim comes back to the chat '
        'seat rather than being edited there. '
        'r6933 (66, on node 60 r6930) GIVES THE ROW SHAPE A THIRD TIME FROM A THIRD DIRECTION: NO '
        'STATE RESOLVES THE CURVATURE IT IS READ OFF. It answers as a THEOREM rather than the '
        'measurement the order expected, because the excitation trace vanishes identically AS AN '
        'OPERATOR -- omega_n = mu_n/a gives S/a with S free of a, so p = rho/3 in EVERY state and not '
        'merely the vacuum, and the whole anomaly sits in the renormalized zero point as a c-number. '
        'So Theta-hat is a multiple of the identity on the tower and R-hat = 4 Lambda + kappa a^-4 is '
        'a function of a-hat ALONE, which is what makes the question answerable without the coupling. '
        'And then it is exact: R prime < 0 on the half-line, so R is strictly monotonic hence '
        'injective, every level set above 4 Lambda a single point and below it empty, and '
        'multiplication by f has an eigenvector at lambda iff that level set carries positive measure '
        '-- so R-hat has NO eigenvectors, purely continuous spectrum on [4 Lambda, infinity) with 4 '
        'Lambda not attained. The instrument agrees against controls built first, two refinement '
        'exponents at -1.00 matching multiplication-by-x and a full decade from the oscillator 0.00 on '
        'a measured variance floor of 1.9e-12, so the numbers are a control on the theorem rather than '
        'the claim. AND THE OBSTRUCTION IS THE ANOMALY COEFFICIENT ITSELF: the commutator of the '
        'curvature with the momentum conjugate to the scale factor gives Var(R) Var(p_a) >= (hbar^2/4) '
        '<R prime>^2, saturated to 0.3 per cent by narrow admissible states, and the right-hand side '
        'vanishes IFF the residue does -- where the curvature is constant and there is nothing to '
        'resolve. So the same residue that makes the counterterm observable is what forbids any state '
        'from resolving the curvature it is read off: r6920 gave that shape from the trace, r6928 from '
        'the algebra, and this from the spectrum. One consistency was not put in by hand -- the '
        'expectation of a^-4 converges at the origin only above a threshold in the boundary index and '
        'the horizon own thermal condition clears it on either ordering, so the boundary condition '
        'that closes the deficiency is the same one that makes the curvature expectation exist. SO THE '
        'MODE IS FIXED: the constant is observable DISTRIBUTIONALLY rather than as an ordinary '
        'sharp-valued observable, unconditional rather than weakened since there are no special states '
        'to except and the ordinary reading is excluded by a theorem and not a missing calculation. '
        'AND THE WALL MOVES AGAIN IN THE DIRECTION OF SMALLER: at higher order the cubic and above put '
        'genuine tower operators into Theta-hat, so R-hat stops being a function of a-hat alone and '
        'the level-set argument does not survive the promotion. DISCHARGE, now routed: the variance '
        'bound comes from a COMMUTATOR, which is algebra and not dynamics, so promote Theta-hat to the '
        'cubic order and report whether the bound survives with the residue as its coefficient -- a '
        'correction that can CANCEL the residue term being the sharp form of the wall rather than its '
        'absence. '
),
    'PO-15': ('the ordering — EXHAUST the selection candidates', 1, 1, 3, None,
        'r3015: THE STEP IS AN EXHAUSTION. The thermal state is eliminated (it selects the Friedrichs extension, which is defined FROM the form an ordering produces). Enumerate what else could select one — the substrates symmetry, the seams characteristic structure, the deparametrization — and either find one or state the choice is external WITH the enumeration as evidence. '
        'r6925 (66, on node 60 r6920) ATTEMPTS THE ROW FOR THE FIRST TIME AND THE ONE ULTRAVIOLET '
        'CONSTANT BECOMES OBSERVABLE. THE SEAT REASON WAS WRONG WHERE ITS ANSWER WAS RIGHT: the '
        'degeneracy needs R sqrt(g)-almost-everywhere CONSTANT, not the cosh, and two non-cosh things '
        'keep it so -- Lambda with radiation, and THE FREE TOWER OWN BARE ZERO-POINT ENERGY, exactly '
        'radiation-like -- so the naive back-reaction breaks nothing; both are NULL CONTROLS measuring '
        'rank 1 to 1e-43, the floor measured rather than assumed. WHAT BREAKS IT IS THE LOG, WHICH IS '
        'TO SAY THE CONSTANT AT ISSUE: Z(s) has a pole at s = -1 with residue 39/4, the ln a spoils '
        'the exact a^-4 that made the bare sum traceless, and the trace r/(2 pi^2 a^4) is INDEPENDENT '
        'of mu -- scheme-independent, which is what an anomaly is. Rank 3 at 9.06e-8, thirty-five and '
        'a half decades above the floor, SIGNED by an exact identity, the gap going as r^2. AND THE '
        'SHAPE OF IT IS THE RESULT: the no-free-constant claim was saved BY a degeneracy switched off '
        'by exactly the constant it was hiding -- no log means R constant and the counterterm '
        'unobservable, but then there is no constant to hide, so the saving mechanism and the thing it '
        'saves us from are the same number. The basis is one-dimensional AT FIXED BACKGROUND and '
        'two-dimensional once a is quantized. ITEM TWO ANSWERS AS A THEOREM: zeta(0) = 10 + '
        'B3prime(0)/2, immune to every constant shift, every rescaling (containing r6411 as the case '
        'L = a^-2) and every even power of 1/m, so the whole even sector is foreclosed -- a reason to '
        'expect 10 survives and not a proof. THE WALL, LOCATED: the back-reaction is SEMICLASSICAL, '
        'and restoration would need the TOTAL trace exactly constant, which an a^-4 anomaly is not. '
        'ONE PREMISE IS TAKEN AND NOT PROVED, that the coupled sector admits states without a definite '
        'alpha -- THE SINGLE WAY THE FINDING REVERSES. DISCHARGE, now routed: does the deparametrized '
        'Hilbert space carry a superselection rule in alpha, controls first. NEVER ATTEMPTED becomes '
        'ATTEMPTED WITH THE WALL LOCATED, and it does not close'),
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
# ⛭ r6895 (66): RESET TO 0.  The switch sweep is the canonical case of the thing this counter
#   counts -- it did not advance a step, it found that the map of the instrument was wrong in two
#   places: a switch certified as reachability-checked had been certified on a PRINT rather than on
#   the reported number, and a gate that passed could not have failed, its tolerance being 0.05 on
#   bin-centre differences whose smallest non-zero spread is 5.  ** Learning that the instrument's
#   printed acoustic scale is not an input to the instrument is learning the problem space. **
SINCE = 0
LASTFIND = ("r6913: **five closed channels turn out to have been correct answers to a mis-aimed question.**  `PO-31` had been run as a hunt for where a wavenumber enters, and every channel closed -- substrate, collapse leg, finite duration, interior vacuum, transfer -- answered *what tilt does the VACUUM give*, while `P15` says twice over that the perturbations here are classical and non-vacuum.  Measured on unit incoming amplitude the interior transfer **imprints its own running**, the log-slope going -0.866 to -0.010 across the band, so the exact scale-invariance banked for years is the LOW-k LIMIT of that one function and not a property of the transfer at all.  The row stops being a channel hunt and becomes a computed REQUIREMENT on its input -- and this seat own statement of the second outcome was too strong, which 60 corrected.")

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
KIND = {'PO-46': 'BUILD', 'PO-10': 'BUILD', 'PO-13': 'BUILD', 'PO-36': 'READ', 'PO-33': 'BUILD',   # r4145: was READ, scoped when the diagnosis looked answered; it is not
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
ORDER = ['PO-59', 'PO-58', 'PO-57', 'PO-56', 'PO-55', 'PO-54', 'PO-53', 'PO-52', 'PO-47', 'PO-48', 'PO-49', 'PO-50', 'PO-51', 'PO-45', 'PO-46', 'PO-10', 'PO-13', 'PO-43', 'PO-24', 'PO-36', 'PO-30', 'PO-25', 'PO-26', 'PO-31', 'PO-23', 'PO-15', 'PO-14', 'PO-17', 'PO-18', 'PO-19', 'PO-20']
GROUP = {'PO-59': 'C', 'PO-58': 'A', 'PO-57': 'D', 'PO-56': 'D',  # r6891: PO-13's live remainder, the acoustic sector.
         'PO-45': 'A', 'PO-46': 'A',  # ⛔ r6549: a FOURTH hardcoded list -- GROUP -- and a row missing here raises.
         'PO-10': 'D', 'PO-13': 'D', 'PO-14': 'A', 'PO-15': 'C', 'PO-16': 'D',
         # ** r3095: the four brought in from p0's frontiers and the field ledgers.  PO-17 and
         # PO-19 are substrate geometry; PO-18 is the constant ledger; PO-20 is analysis. **
         'PO-17': 'E', 'PO-18': 'E', 'PO-19': 'E', 'PO-20': 'E',
         'PO-55': 'E', 'PO-54': 'E', 'PO-53': 'E', 'PO-52': 'C', 'PO-47': 'D', 'PO-48': 'E', 'PO-49': 'E', 'PO-50': 'D', 'PO-51': 'C',
         # ** r6861: the five remainders of struck rows, each opened where its parent closed --
         #   PO-47 and PO-50 are the data-confrontation sector, PO-48 and PO-49 the substrate
         #   and its interiors, PO-51 the quantum tower. **
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
