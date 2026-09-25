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
        'built and only the sample is missing.'),
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
        'anything observes, which is the cross-register question PO-48 is being worked on.'),
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
        "where P10 already put the question, and not a chiral MEMBER.  r6805 NARROWS IT: the row now has a NUMBER to hit. The like-for-like refit -- both arms free in H0, Omega_m, omega_b and n_s on one set of bins -- has this arm preferring n_s = 0.9949 against the control's 0.9559, bluer by 0.039. Before this the tilt was read off a background fitted to the other arm, so a derived tilt near 0.96 would have looked like success; the ordering is reversed and it is measured. PROVISIONAL IN ONE RESPECT: the refit ran on l<1290 because the full-range container could not complete a grid and cutting the k-reach was refused by the convergence guard, and the damping tail is where a tilt has most of its leverage -- the full-range refit is running and is what fixes the target rather than indicating it. r6823 NARROWS IT FURTHER, on node 60's r6812: the collapse leg is NOT A CANDIDATE for the tilt. On the leg both the potential and the effective temperature are functions of x = k eta / sqrt3 alone, so a handover at a fixed PHASE is exactly scale-free -- the ratio of amplitudes at two wavenumbers is 1, not nearly 1. A fixed-TIME handover is the only place a scale survives and what it gives is red in both channels and goes as k^2, which is a RUNNING and not a tilt: the target 1-n_s = 0.005 needs x = 0.05, and thirty times that wavenumber -- inside the refit's own band -- gives 41.9. On the adjudicated configuration it is exactly zero, both log-derivatives vanishing quadratically at the crossing. So the row is no longer 'where does the leg's tilt come from': the leg is a k-independent amplitude and nothing else, the tilt is wholly the progenitor's vacuum, and what remains is what the progenitor supplies -- with the target measured at one end of it. r6829 NARROWS IT AGAIN, on node 60's r6826: the substrate alone fixes n_s = 1 EXACTLY. Of the three candidate scale-breakers, two are one candidate and both fail -- in conformal time the mode equation carries no length, so the curvature radius enters only as the amplitude prefactor and reaches the tilt for NO value of it, and on the forced member the progenitor's mass IS that radius up to a pure number (M/alpha fixed at Nariai), so it is not an independent scale. The third, the collapse's finite duration, enters and does not tilt: exact Bogoliubov coefficients whose log-derivative oscillates with a decaying envelope, sign-alternating across the band -- a scale and not a tilt, by the same test that closed the leg. ONE CHANNEL IS LEFT and it has an exact answer: n_s - 1 = 3 - 2 sqrt(9/4 - m^2 alpha^2), blue for m^2 > 0. The measured 0.995 is nearer unity than the standard model's value but from BELOW, so it asks the interior for a slightly negative m^2 alpha^2 -- a REQUIREMENT on the progenitor, not a result about it, and nothing was tuned. The row is now what the interior gives for m^2 alpha^2. r6857 (66), on node 60 r6846: THE INTERIOR'S VACUUM IS BLUE EVERYWHERE AND A RUNNING. The interior was not newly built -- its background and mode problem were already banked and the order's potential reduces to the banked one exactly. Solved there, the potential interpolates between the scale-free matter form and a radiation form that is not, so the spectrum breaks at the wavenumber the radiation content sets: log-slope running +0.30 to +1.98 across the observed band, tending to the radiation value +2. A running and not a tilt, and blue at every wavenumber -- flattest +0.304 against a measured -0.002, wrong sign and about a hundred times the size, with the flattest slope going as the radiation fraction so that exact scale-invariance is the pure-dust limit and reaching red would need it negative. AND THE REQUIREMENT r6826 HANDED THE INTERIOR IS WITHDRAWN: 3-2 sqrt(9/4 - m^2 alpha^2) comes from a 1/eta^2 potential with a dimensionless coefficient, which is what makes it a power law, where the interior's carries a scale -- so the slightly negative m^2 alpha^2 was an artefact of applying the substrate's template off the substrate. FOUR CHANNELS ARE NOW CLOSED (substrate, collapse leg, finite duration, interior vacuum) and the measured red tilt is supplied by none of them: the row is harder than it was, not nearer."
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
ORDER = ['PO-54', 'PO-53', 'PO-52', 'PO-47', 'PO-48', 'PO-49', 'PO-50', 'PO-51', 'PO-45', 'PO-46', 'PO-10', 'PO-13', 'PO-43', 'PO-24', 'PO-36', 'PO-30', 'PO-25', 'PO-26', 'PO-31', 'PO-23', 'PO-15', 'PO-14', 'PO-17', 'PO-18', 'PO-19', 'PO-20']
GROUP = {'PO-45': 'A', 'PO-46': 'A',  # ⛔ r6549: a FOURTH hardcoded list -- GROUP -- and a row missing here raises.
         'PO-10': 'D', 'PO-13': 'D', 'PO-14': 'A', 'PO-15': 'C', 'PO-16': 'D',
         # ** r3095: the four brought in from p0's frontiers and the field ledgers.  PO-17 and
         # PO-19 are substrate geometry; PO-18 is the constant ledger; PO-20 is analysis. **
         'PO-17': 'E', 'PO-18': 'E', 'PO-19': 'E', 'PO-20': 'E',
         'PO-54': 'E', 'PO-53': 'E', 'PO-52': 'C', 'PO-47': 'D', 'PO-48': 'E', 'PO-49': 'E', 'PO-50': 'D', 'PO-51': 'C',
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
