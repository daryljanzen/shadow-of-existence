# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE MASSIVE SPECIES' OWN BOLTZMANN HIERARCHY VALIDATES JOINTLY -- THE FIRST CANDIDATE TO PUT
BOTH BLOCKS INSIDE THE BAND AT BOTH SUMS -- AND IT IS JOINTNESS AND NOT SIZE THAT IT ACHIEVES,
BECAUSE THE WEIGHT CHANGE ALONE WAS CLOSER IN TT AND OUT OF BAND IN EE; THE MASSLESS-LIMIT GATE
CAUGHT A SEEDING DEFECT ON THE ONLY ARM THAT MATTERS AND NO SWITCH ARM COULD HAVE.

COMPUTES: the sum-response amplitude of the massive neutrino sector closed by its own momentum-binned
Boltzmann hierarchy, at the two sums the order fixed and at the banked spectral resolution, fitted
against CAMB by the fit of record -- executed and not re-implemented, its reproduction leg required
to return that fit's four headline amplitudes first; the hierarchy's two numerical parameters, the
momentum-node count and the l-cutoff, each fixed by a gate registered before any grid was tried and
each converged by doubling and by raising; the massless limit of the whole construction, measured
rather than trusted, together with the floor under that measurement identified as the quadrature
grid's own representation error; and the wall-clock cost of every leg, which the registration
declared a RISK and required as a measurement.
** IT PINS AS RESULTS: `A` = `0.989142` and `0.978850` in TT at `0.30` and `0.60` eV and `0.980552`
and `0.977398` in EE, so `0.01086`, `0.02115`, `0.01945` and `0.02260` off one -- ALL FOUR inside the
order's `0.03` band, in BOTH blocks at BOTH sums, which no candidate before this reached; the
quadrature gate's `3.052e-05` and `3.331e-05` against `1e-04` at 12 nodes on `[0, 20]`; the
convergence gates' worst moves in `A` of `8.444e-04` for the node count doubled and `3.892e-05`
for the cutoff raised by half, each against `0.003`; the massless limit's
`2.335e-05` and `2.446e-05` at 12 nodes falling to `6.692e-06` and `7.771e-06` at 24 -- a factor
`3.5` and `3.1` against a registered `3`, flat across the mass decade to `1.05` and `1.16` against a
registered `2`; the limit read on the fit's own quantity at `1.161e-03` against `0.003`; and the
measured cost, `3175` and `3161` seconds with the hierarchy off against `3532` and `3537` with it on,
which is `11.5` per cent and not a multiple although the state vector grows from 20 to 176 per
mode. **
⛔ ** AND IT PINS WHAT THE VERDICT IS NOT: ** the weight change alone was CLOSER than this in TT at
`0.30` eV -- `0.00490` against `0.01086` -- and was OUTSIDE the band in EE at `0.04005`.  So the two
comparison rows do not fire because the BOTH-OUTSIDE case they split did not arise -- both blocks
are inside the band -- and not because of how that comparison came out.  ** And the comparison
SPLITS BY SUM: ** against the fluid family's best TT this revision is CLOSER at `0.60` eV, `0.02115`
against `0.05621`, and NOT closer at `0.30`, `0.01086` against `0.00490`.  ** Reading this revision
as the tightest TT everywhere would be reading it wrongly, and so would reading it as tighter
nowhere. **
⛔ ** AND IT PINS A DEFECT THE SWITCH ARMS COULD NOT HAVE CAUGHT: ** the seeding sat inside one
branch of the initial-condition `if`/`else`, so on the arm every validation number here is read on
the moments started at ZERO and grew from the sources -- `delta` a factor eight short early and only
caught up by recombination.  Byte-identical-off says nothing about a seed only the ON path reads;
the fluid's bit-identity says nothing about a branch the fluid never enters; and the seed/integral
inversion HAD been verified exact at the initial time, which was a true fact about the seeding
function and not about whether the solver ever received it.  ** The gate measured the limit and the
arms did not, which is the whole reason the gate was registered. **
⛔ ** AND IT PINS THAT THE REGISTERED MASSLESS-LIMIT TEST WAS STRONGER THAN WHAT WAS REGISTERED AND
UNSATISFIABLE BY CONSTRUCTION: ** the criterion is agreement to the fit's own resolution, and the
shrink reading of it cannot be met because a FINITE quadrature puts a MASS-INDEPENDENT floor under
the comparison.  Two arms were registered before either ran: one identifying the floor as the grid's
by doubling the nodes, one asserting the criterion on the quantity the fit actually reads.  The
original test keeps its verdict as run and nothing was overwritten.
⛔ ** AND IT PINS THAT EXACTLY ONE REGISTERED ROW FIRES, ** which the reader raises rather than
reports if the count is not one.
⛔ ** NO LIMIT IS PINNED HERE AND NONE WAS READ, ** even under the validating row: the order puts the
limit in its next item on the closed cross-seeded envelope, with its own registration.  ** AND THIS
IS ONE FITTER: ** the order requires both, the legs are banked for the second fit whatever the
verdict, and a disagreement beyond its own reproduction tolerance IS the finding with no limit read
through either.

⌷ ** THE ID. **  `69` ordered this as `r7879` item ②, having ruled the massive species' own
Boltzmann hierarchy THE REPAIR and required it converged and validated jointly, with the q-grid and
l-cutoff numerical and not tuned.

⚠ ** THREE THINGS IN THIS RECORD ARE THIS SEAT'S OWN: ** the label in the two comparison rows was
MANY-TO-ONE and the reading was fixed to the hardest available one before any leg was fitted; the
massless-limit criterion's reach is stated rather than left implicit, because its legs are fitted
against a target that cancels and its bound does not transport to the validation sums; and the
registered shrink test's unsatisfiability is named as a defect in the registration, not in the
hierarchy.

    NODE=60 python3 <this file>

Written r7882 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
D = os.path.join(BW, 'r7882_60_the_massive_species_own_boltzmann_hierarchy')
R7878 = os.path.join(BW, 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic'
                         '_sound_speed')
INSTF = os.path.join(BW, 'ACOUSTIC_two_arm.py')
FAILS = []
NARMS = 0


def load(name, d=None):
    with io.open(os.path.join(d or D, name), encoding='utf-8') as fh:
        return json.load(fh)


def text(name, d=None):
    with io.open(os.path.join(d or D, name), encoding='utf-8') as fh:
        return fh.read()


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


print(__doc__)
print('=' * 100)

QD = load('quad.json')
FL = load('floor.json')
LF = load('limitfit.json')
SW = load('switch_arms.json')
BL = load('fluid_baseline.json')
VA = load('validate.json')
#: ⛔ *the prose is matched on a WHITESPACE-FLATTENED copy -- four arms of an earlier revision's
#: receipt failed on where a line happened to wrap, which is a fact about the editor and not about
#: the record.*
RESULT = ' '.join(text('RESULT.md').split())
PRED = ' '.join(text('PREDICTION.md').split())
INST = io.open(INSTF, encoding='utf-8').read()
COST = text(os.path.join('limitfit', 'COST.txt'))
S = ('0.30', '0.60')
BLK = ('TT', 'EE')

# ══ Ⓐ THE SWITCH, AND WHAT OFF MEANS ════════════════════════════════════════════════════════════

check('Ⓐ⓵ᵃ ⛭ ** THE LANDED INSTRUMENT CARRIES NO SUCH SWITCH, SEARCHED OVER ITS OWN BYTES: ** the '
      'arm reads `origin/main`\'s copy of this instrument at source and tests every byte of it for '
      'the switch\'s name.  ⇒ *so this revision ADDS the hierarchy rather than re-reading one that '
      'was already there*',
      SW['landed_has_no_switch'] is True and SW['patched_has_switch'] is True
      and SW['differ_in_source'] is True)

check('Ⓐ⓵ᵇ ⛭⛭ ** OFF IS BYTE-IDENTICAL, BOTH WAYS OF BEING OFF, MEASURED ON OUTPUT AND NOT ON THE '
      'SOURCE: ** the switch absent and the switch present at a zero sum each reproduce the landed '
      'arrays exactly, over all 6 TT arrays and all 11 polarisation arrays.  ⇒ *which is what makes '
      'the hierarchy an addition and not a quiet re-plumbing of the sector*',
      SW['off_identical'] is True
      and all(SW['off_rows'][w][b]['arrays_identical'] is True
              for w in ('absent', 'zero') for b in ('tt', 'pol'))
      and SW['off_rows']['absent']['tt']['n_arrays'] == 6
      and SW['off_rows']['absent']['pol']['n_arrays'] == 11)

check('Ⓐ⓵ᶜ ⛭ ** AND THE FLUID APPROXIMATION IS BIT-IDENTICAL ACROSS THIS DIFF: ** the sector\'s '
      'landed closure, at its own defaults, returns the same bytes before and after.  ⇒ *so the '
      'two closures can be compared inside one run without the baseline having moved*',
      SW['fluid_identical'] is True
      and all(SW['fluid_rows'][b]['arrays_identical'] is True for b in ('tt', 'pol')))

check('Ⓐ⓶ ⛭⛭ ** THE SWITCH REFUSES TO RUN BESIDE THE FLUID APPROXIMATION, BY THE FORK GUARD: ** '
      'two models of ONE sector, and that sector has one slot -- so the instrument raises rather '
      'than running both and silently preferring one.  It also refuses a zero sum and a grid that '
      'is not a grid.  ⇒ *the refusal is in the instrument, not in a convention a caller may '
      'forget*',
      SW['all_pass'] is True
      and 'NUHIER=1 and NUPERT=1 are two models of ONE sector' in INST
      and "NUHIER=1 needs NUFD=1 and MNU != 0" in INST)

# ══ Ⓑ THE DEFECT NO SWITCH ARM COULD HAVE SEEN, AND THE CLAUSE THE REPAIR REASONS FROM ══════════

_SEED = "y0[:, I_PN:] = _nuhier_seed(np.zeros((nk, NQ, LMAXNU + 1)), kk,"
_IFLC = "if ARM == 'lcdm' or _cric == 'branchpoint':"
_SEEDAT = INST.index(_SEED)
_RHSAT = INST.index('    def rhs(e, Y):', INST.index(_IFLC))
_ELSEAT = INST.index('\n    else:\n', INST.index(_IFLC))
check('Ⓑ⓵ ⛭⛭⛭ ** THE SEEDING IS OUTSIDE THE INITIAL-CONDITION `if`/`else`, WHICH IS THE CLAUSE THE '
      'REPAIR REASONS FROM: ** it is seeded ONCE, after both data have been written and before the '
      'right-hand side is defined, at a point reached whichever arm ran.  ⇒ *asserted on the '
      'instrument\'s own text and at ONE indentation level, because the defect was exactly that the '
      'seeding sat inside one branch: seeded in the CR branch alone, the arm every validation '
      'number here is read on left the moments at zero and grew them from the sources*',
      _SEEDAT > _ELSEAT and _SEEDAT < _RHSAT
      and INST.count(_SEED) == 1
      and INST[INST.rindex('\n', 0, _SEEDAT) + 1:_SEEDAT] == '        ')

check('Ⓑ⓶ ⛭⛭ ** AND ONE SEEDING IS CORRECT FOR BOTH ARMS BECAUSE BOTH DATA WRITE THE SAME TWO '
      'SLOTS: ** each branch sets the species\' density and velocity to `dg0` and `th0`, so the '
      'single seeding below them reads the right two numbers in either case.  ⇒ *the arm checks the '
      'premise rather than the conclusion -- if a branch were changed to seed the species '
      'differently, this fails and the lifted seeding becomes wrong*',
      #: ⛔ *counted over LINES WHOSE STRIPPED FORM IS THE ASSIGNMENT, not over the whole
      #: file: a comment in this same file quotes the line, so a raw `count` reads 3 and the
      #: arm would have passed or failed on a sentence instead of on the two data.*
      sum(1 for _l in INST.splitlines()
          if _l.strip() == 'y0[:, 4], y0[:, 5] = dg0, th0') == 2)

check('Ⓑ⓷ ⛭⛭ ** AND THE SWITCH ARMS COULD NOT HAVE CAUGHT IT, WHICH IS WHY THE GATE EXISTS: ** '
      'byte-identical-off says nothing about a seed only the ON path reads, and the fluid\'s '
      'bit-identity says nothing about a branch the fluid never enters -- and the seed/integral '
      'inversion HAD been verified exact at the initial time, which was a true fact about the '
      'seeding function and not about whether the solver ever received it',
      SW['all_pass'] is True
      #: ⛔ *ONE conjunction and no `or`: `A and B or C` would mint a spurious ALT group in the
      #: quote-pin gate, and it also hides which half of the arm carried the pass.*
      and 'The arms could not have seen it.' in RESULT
      and 'WHICH NO SWITCH ARM COULD HAVE' in RESULT)

# ══ Ⓒ GATE Ⓠ⓵ -- THE QUADRATURE AGAINST THE BACKGROUND ALREADY BUILT ═════════════════════════════

_C = QD['candidates']['12@20']
check('Ⓒ⓵ ⛭⛭ ** GATE Ⓠ⓵ IS MET AND THE GRID IS FIXED BY IT: ** 12 Gauss-Legendre nodes on `[0, 20]` '
      'reproduce the instrument\'s own background splines to `3.052e-05` in the density and '
      '`3.331e-05` in the equation of state, against the registered `1e-04`, at every decade of the '
      'scale factor.  ⇒ *the two numbers the hierarchy carries are fixed by a gate registered '
      'before any grid was tried, which is what makes them numerical and not tuned*',
      _C['passes'] is True and _C['n'] == 12 and abs(_C['qmax'] - 20.0) < 1e-12
      and abs(_C['worst_rho'] - 3.052e-05) < 5e-09
      and abs(_C['worst_w'] - 3.331e-05) < 5e-09
      and _C['worst_rho'] < 1e-04 and _C['worst_w'] < 1e-04,
      '%.3e, %.3e' % (_C['worst_rho'], _C['worst_w']))

check('Ⓒ⓶ ⛭ ** AND THE SCAN SEPARATES TRUNCATION FROM QUADRATURE ERROR RATHER THAN REPORTING ONE '
      'NUMBER: ** on `[0, 15]` the error SATURATES whatever the node count, so the cut matters and '
      'not only the nodes.  ⇒ *a grid chosen on node count alone would have sat on a floor it could '
      'not see*',
      all(QD['candidates']['%d@15' % n]['passes'] is False for n in (12, 16)
          if '%d@15' % n in QD['candidates'])
      and QD['candidates']['12@15']['worst_rho'] > 1e-04)

# ══ Ⓓ GATE Ⓠ⓸ -- THE MASSLESS LIMIT, AND THE FLOOR UNDER IT ══════════════════════════════════════

check('Ⓓ⓵ ⛭⛭⛭ ** ARM Ⓠ⓸ᵃ: THE FLOOR UNDER THE MASSLESS LIMIT IS THE QUADRATURE GRID\'S AND NOT A '
      'DEFECT: ** doubling the nodes to 24 drops the on-against-off residual by `3.5` at a sum of '
      '`1e-3` and `3.1` at `1e-4`, against a registered factor `3`, while it stays flat across the '
      'decade to `1.05` and `1.16` against a registered factor `2`.  ⇒ *so a residual that does not '
      'shrink with the mass is the grid\'s representation error, which CANNOT shrink with the mass, '
      'and a shrink test cannot read this gate*',
      FL['met'] is True and FL['fell'] is True and FL['stayed_flat'] is True
      and abs(FL['FALL'] - 3.0) < 1e-12 and abs(FL['FLAT'] - 2.0) < 1e-12
      and all(FL['fall'][k] >= FL['FALL'] for k in ('1e-3', '1e-4'))
      and all(FL['flat'][k] <= FL['FLAT'] for k in ('12', '24'))
      and abs(FL['fall']['1e-3'] - 3.489) < 0.0005
      and abs(FL['fall']['1e-4'] - 3.147) < 0.0005,
      '%.3f, %.3f' % (FL['fall']['1e-3'], FL['fall']['1e-4']))

check('Ⓓ⓶ ⛭ ** AND THE FLOOR IS THE GRID\'S IN SIZE AS WELL AS IN BEHAVIOUR: ** it is '
      '`2.335e-05` and `2.446e-05` at 12 nodes and `6.692e-06` and `7.771e-06` at 24, which is the '
      'same order as the quadrature error gate Ⓠ⓵ measured independently against the background '
      'splines.  ⇒ *two routes to the same number, one of them a gate that knew nothing about this '
      'comparison*',
      abs(FL['nodes']['12']['1e-3'] - 2.335e-05) < 5e-09
      and abs(FL['nodes']['12']['1e-4'] - 2.446e-05) < 5e-09
      and abs(FL['nodes']['24']['1e-3'] - 6.692e-06) < 5e-10
      and abs(FL['nodes']['24']['1e-4'] - 7.771e-06) < 5e-10
      and max(FL['nodes']['12'].values()) < 10.0 * _C['worst_rho'])

check('Ⓓ⓷ ⛭⛭⛭ ** ARM Ⓠ⓸ᵇ: THE REGISTERED CRITERION, ASSERTED ON THE QUANTITY THE FIT ACTUALLY '
      'READS: ** with the reproduction leg returning the fit of record\'s four headline amplitudes '
      'first, switching the hierarchy on where it must be inert moves `A` by at most `1.161e-03` '
      'over both blocks and both limit sums, against the registered `0.003`.  ⇒ *so GATE Ⓠ⓸ IS MET: '
      'at the massless limit nothing the fit reads moves*',
      LF['met'] is True and LF['reproduction']['reproduced'] is True
      and abs(LF['MOVE'] - 0.003) < 1e-12
      and abs(LF['worst'] - 1.1613e-03) < 5e-07
      and LF['worst'] < LF['MOVE']
      and max(LF['difference'].values()) == LF['worst'],
      '%.3e' % LF['worst'])

check('Ⓓ⓸ ⛭⛭ ** AND THE ARM\'S REACH IS PINNED, NOT LEFT IMPLICIT: ** its legs sit at the limit sums '
      'and are fitted against the validation sums\' CAMB targets, so the arm is a DIFFERENCE at a '
      'FIXED target and the target cancels -- which is why every `A` in it is near ZERO and not '
      'near one.  ⛔ *NO `A` from these legs is a validation number.  The consequence, stated in the '
      'record rather than inferred from it: the arm bounds the move at the limit and does not '
      'transport that bound to `0.30` and `0.60` eV, where the convergence gates speak instead*',
      all(abs(LF['A'][t]['%s|%s' % (b, s)]) < 0.01
          for t in ('off', 'on') for b in BLK for s in S)
      and 'no `A` from those legs is a validation number' in RESULT.replace('**', '')
      and LF['slots']['0.30'].endswith('1e-3') and LF['slots']['0.60'].endswith('1e-4'))

# ══ Ⓔ THE COST, MEASURED AND NOT ESTIMATED ══════════════════════════════════════════════════════

_W = dict((ln.split(']')[0].split('[')[1], int(ln.split('wall=')[1].rstrip('s')))
          for ln in COST.strip().splitlines() if 'wall=' in ln)
_OFF = [_W[k] for k in _W if k.startswith('off/')]
_ON = [_W[k] for k in _W if k.startswith('on/')]
check('Ⓔ⓵ ⛭⛭ ** THE DECLARED COST RISK IS DISCHARGED BY MEASUREMENT: ** at the banked resolution '
      'the hierarchy-off legs ran `3175` and `3161` seconds and the hierarchy-on legs `3532` and '
      '`3537`, so the hierarchy costs `11.5` per cent more wall time -- NOT a multiple -- although '
      'the state vector grows from 20 to 176 per mode.  ⇒ *the mode solve is not what dominates a '
      'banked leg, so the validation legs and both convergence banks fit in one revision and the '
      'item does not split*',
      len(_OFF) == 2 and len(_ON) == 2
      and sorted(_OFF) == [3161, 3175] and sorted(_ON) == [3532, 3537]
      and abs((sum(_ON) / float(sum(_OFF)) - 1.0) * 100.0 - 11.5) < 0.25,
      '%.1f%%' % ((sum(_ON) / float(sum(_OFF)) - 1.0) * 100.0))

# ══ Ⓕ THE MANY-TO-ONE LABEL IN THE TWO COMPARISON ROWS ══════════════════════════════════════════

_R78 = load('refit_parts.json', R7878)['arms']
check('Ⓕ⓵ ⛭⛭⛭ ** THE LABEL THE TWO COMPARISON ROWS USE IS MANY-TO-ONE ON THE OBJECT, AND IT WAS '
      'CHECKED BEFORE TWO THINGS WERE IDENTIFIED BY IT: ** the previous revision measured FIVE '
      'fluid arms and their TT disagrees by a factor sixteen at `0.30` eV between the full fluid '
      'model and the weight change alone.  ⇒ *so "the fluid approximation gave" did not name one '
      'number, and a row read on the looser arm is far easier to pass than the same row read on the '
      'tighter one*',
      len(BL['arms']) == 5
      and abs(BL['arms']['A1']['TT'][0] / BL['arms']['W']['TT'][0] - 16.0) < 0.5,
      '%.1f' % (BL['arms']['A1']['TT'][0] / BL['arms']['W']['TT'][0]))

check('Ⓕ⓶ ⛭⛭ ** AND THE BASELINE IS READ FROM THE PREVIOUS REVISION\'S OWN RECORD, NOT '
      'TRANSCRIBED: ** every one of the five arms\' two TT distances agrees with that revision\'s '
      'fitted amplitudes to the last bit.  ⇒ *the number that reaches this receipt is the record\'s*',
      BL['source'].startswith('r7878')
      and all(abs(BL['arms'][a]['TT'][i]
                  - abs(_R78[a]['fits']['TT|%s' % s]['best_A'] - 1.0)) < 1e-12
              for a in BL['arms'] for i, s in enumerate(S)))

check('Ⓕ⓷ ⛭⛭ ** AND THE READING TAKEN IS THE HARDEST AVAILABLE ONE, FIXED BEFORE ANY LEG OF THIS '
      'REVISION WAS FITTED: ** the fluid family\'s BEST TT at each sum, which is the weight change '
      'alone at both -- `0.00490` off one at `0.30` eV and `0.05621` at `0.60`.  ⇒ *and at `0.30` eV '
      'that is TIGHTER THAN THE VALIDATION BAND ITSELF, because the weight change is already inside '
      'the band there: a baseline chosen to be beatable would have turned a negative finding into '
      'its opposite*',
      BL['best_TT_off_one']['0.30']['arm'] == 'W'
      and BL['best_TT_off_one']['0.60']['arm'] == 'W'
      and abs(BL['best_TT_off_one']['0.30']['value'] - 0.00490) < 5e-06
      and abs(BL['best_TT_off_one']['0.60']['value'] - 0.05621) < 5e-06
      and BL['best_TT_off_one']['0.30']['value'] < 0.03
      and all(BL['best_TT_off_one'][s]['value']
              == min(BL['arms'][a]['TT'][i] for a in BL['arms'])
              for i, s in enumerate(S)))

# ══ Ⓖ THE VALIDATION, ON THE ORDER'S OWN BANDS ══════════════════════════════════════════════════

_A = VA['A']['base']
_OFF = VA['validation']['off_one']
check('Ⓖ⓵ ⛭⛭⛭ ** THE REPAIR VALIDATES JOINTLY, WHICH NO CANDIDATE BEFORE IT DID: ** `A` is '
      '`0.989142` and `0.978850` in TT at `0.30` and `0.60` eV and `0.980552` and `0.977398` in '
      'EE, so `0.01086`, `0.02115`, `0.01945` and `0.02260` off one -- ALL FOUR inside the order\'s '
      '`0.03` band, in BOTH blocks at BOTH sums.  ⇒ *and the fit is the one of record, with its '
      'reproduction leg returning that fit\'s four headline amplitudes before any of these was '
      'read*',
      VA['reproduction']['reproduced'] is True
      and abs(_A['TT|0.30'] - 0.989142) < 5e-07
      and abs(_A['TT|0.60'] - 0.978850) < 5e-07
      and abs(_A['EE|0.30'] - 0.980552) < 5e-07
      and abs(_A['EE|0.60'] - 0.977398) < 5e-07
      and all(_OFF['%s|%s' % (b, s)] <= 0.03 for b in BLK for s in S)
      and VA['validation']['TT_inside_both'] is True
      and VA['validation']['EE_inside_both'] is True,
      ', '.join('%.5f' % _OFF['%s|%s' % (b, s)] for b in BLK for s in S))

check('Ⓖ⓶ ⛭⛭⛭ ** AND WHAT MAKES IT THE FIRST IS NOT THAT ITS NUMBERS ARE THE SMALLEST: ** the '
      'weight change alone was CLOSER than this in TT at `0.30` eV -- `0.00490` against `0.01086` '
      '-- and was OUTSIDE the band in EE at `0.04005`.  ⇒ *which is exactly the shape the order '
      'ruled against, so the thing achieved here is JOINTNESS and not size; pinned because reading '
      'this revision as the tightest TT would be reading it wrongly*',
      BL['arms']['W']['TT'][0] < _OFF['TT|0.30']
      and BL['arms']['W']['EE'][0] > 0.03
      and abs(BL['arms']['W']['EE'][0] - 0.04005) < 5e-06)

check('Ⓖ⓷ ⛭⛭ ** AND THE TWO COMPARISON ROWS DO NOT FIRE FOR THE RIGHT REASON: ** they split the '
      'BOTH-OUTSIDE case, and that case did not arise -- NOT because this revision beat the fluid '
      'family\'s best TT, which it did NOT at either sum.  ⇒ *the record says so in the same place '
      'it reports the verdict, so the verdict cannot be read as a comparison it did not win*',
      #: ⛔ *ONE conjunction and no `or`: the first version of this arm was `A and B or C`,
      #: which mints a spurious ALT group in the quote-pin gate AND hides which half passed.*
      VA['baseline']['TT_closer_at_both'] is False
      and VA['rows']['Ⓓ'] is False and VA['rows']['Ⓔ'] is False
      and _OFF['TT|0.30'] > BL['arms']['W']['TT'][0]
      and _OFF['TT|0.60'] < BL['arms']['W']['TT'][1]
      and 'closer at `0.60 eV`' in RESULT
      and 'not closer at `0.30 eV`' in RESULT)

check('Ⓖ⓸ ⛭ ** AND EVERY ONE OF THE FOUR SITS BELOW ONE, BY `0.011` TO `0.023`: ** a small, '
      'same-signed undershoot in both blocks at both sums, where the fluid approximation\'s failure '
      'was an overshoot in TT with EE dragged out of band the other way',
      all(_A['%s|%s' % (b, s)] < 1.0 for b in BLK for s in S)
      and 0.010 < min(_OFF.values()) and max(_OFF.values()) < 0.024)

# ══ Ⓗ THE CONVERGENCE GATES, WHICH ARE WHAT STAND BEHIND THE VERDICT ════════════════════════════

_CV = VA['convergence']
check('Ⓗ⓵ ⛭⛭ ** GATE Ⓠ⓶ IS MET: THE QUADRATURE CANNOT DECIDE THE VERDICT. ** Doubling the node '
      'count to 24 at the banked resolution moves `A` by at most `8.444e-04` over both blocks and '
      'both validation sums, against the registered `0.003` -- one tenth of the order\'s band, '
      'fixed before any grid was tried.  ⇒ *so the numerical error is an order of magnitude below '
      'the margin the verdict turns on*',
      _CV['Ⓠ⓶']['read'] is True and _CV['Ⓠ⓶']['met'] is True
      and abs(_CV['Ⓠ⓶']['worst'] - 8.444e-04) < 5e-08
      and _CV['Ⓠ⓶']['worst'] < VA['MOVE'],
      '%.3e' % _CV['Ⓠ⓶']['worst'])

check('ⓗ⓶ ⛭⛭ ** GATE Ⓠ⓷ IS MET: THE ℓ-CUTOFF CANNOT DECIDE IT EITHER. ** Raising the cutoff by '
      'half moves `A` by at most `3.892e-05` over both blocks and both sums, against the same '
      'registered `0.003` -- nearly TWO orders below the margin, where the node count is one.  '
      '⇒ *so neither of the hierarchy\'s two numerical parameters can decide the verdict, which '
      'is what the order required when it said they are numerical and converged rather than '
      'tuned; and the cutoff is converged some twenty times better than the grid at the cost '
      'actually spent, so the GRID is where the remaining numerical error lives*',
      _CV['Ⓠ⓷']['read'] is True and _CV['Ⓠ⓷']['met'] is True
      and abs(_CV['Ⓠ⓷']['worst'] - 3.892e-05) < 5e-09
      and _CV['Ⓠ⓷']['worst'] < VA['MOVE']
      and _CV['Ⓠ⓷']['worst'] < _CV['Ⓠ⓶']['worst'],
      '%.3e' % _CV['Ⓠ⓷']['worst'])

check('Ⓗ⓷ ⛭⛭ ** AND THIS READ IS THE WHOLE ONE, NOT A PARTIAL: ** all three banks were read, so no '
      'convergence gate here is reported met on a bank that was never built.  ⛔ *The reader takes '
      'its banks from the environment, which narrows WHAT IS READ and cannot touch a criterion, and '
      'a run that reads fewer marks itself partial in its own record -- so an earlier partial read '
      'of this same file could not have been mistaken for this one*',
      VA['partial'] is False
      and sorted(VA['banks_read']) == ['base', 'lmax18', 'nq24']
      and VA['converged'] is True)

# ══ Ⓘ EXACTLY ONE ROW, AND WHAT IS NOT CLAIMED ══════════════════════════════════════════════════

check('Ⓘ⓵ ⛭⛭⛭ ** EXACTLY ONE OF THE FIVE REGISTERED ROWS FIRES, AND THE READER RAISES RATHER THAN '
      'REPORTING A VERDICT IF THE COUNT IS NOT ONE: ** the previous two revisions each had a '
      'registration defect here -- one with two rows firing at once, one with a row whose condition '
      'was not defined -- and the rows are exhaustive and exclusive by construction, partitioning '
      'on whether each block is inside the band at both sums with the two comparison rows splitting '
      'the remainder',
      VA['exactly_one'] is True and VA['fired'] == ['Ⓐ']
      and sum(1 for k in VA['rows'] if VA['rows'][k]) == 1
      and len(VA['rows']) == 5)

check('Ⓘ⓶ ⛔⛭⛭ ** AND NO LIMIT IS READ HERE EVEN UNDER THE VALIDATING ROW: ** the order puts the '
      'limit in its next item, on the closed cross-seeded envelope, with its own registration.  '
      '⇒ *pinned as an absence because a validating verdict is exactly where a limit would be '
      'easiest to read without being asked for*',
      'NO LIMIT IS READ IN THIS REVISION even under' in PRED
      and 'No limit.' in RESULT
      and 'NO LIMIT IS READ HERE' in RESULT)

check('Ⓘ⓷ ⛔⛭⛭ ** AND THIS IS ONE FITTER, NOT THE JOINT READ THE ORDER ASKED FOR: ** the order '
      'requires both, the legs are banked for the second fit whatever the verdict, and a '
      'disagreement beyond its own reproduction tolerance IS the finding with no limit read through '
      'either.  ⇒ *so the verdict above is this seat\'s fitter and is recorded as such*',
      #: ⛔ *ONE conjunction and no `or`, for the same reason as the arm above.*
      'One fitter so far.' in RESULT
      and "These legs are banked for `cc66`'s second fit whatever the verdict" in RESULT)
# ══ Ⓙ EVERY FIGURE THIS REVISION PRINTS, PINNED — AND THE GRIDS READ FROM THE LEGS THAT RAN ══

import json                                                                     # noqa: E402

import numpy                                                                    # noqa: E402

VAL = os.path.join(D, 'valid')


def leg_config(bank, slot):
    """the config THE LEG ITSELF RECORDED, not the generator's intent"""
    with numpy.load(os.path.join(VAL, bank, 'lcdm_%s_pol.npz' % slot), allow_pickle=True) as z:
        return json.loads(str(z['config']))


_CFG = dict(((b, sl), leg_config(b, sl))
            for b in ('base', 'nq24', 'lmax18') for sl in ('S030', 'S060'))
check('Ⓙ⓵ ⛭⛭ ** THE TWO SUMS ARE READ OFF THE LEGS THEMSELVES: ** every bank records `0.30` at its '
      'first slot and `0.60` at its second, and the hierarchy switch records as ON in all six.  '
      '⇒ *so the sums this revision prints are the legs\' own and not a repetition of what the '
      'generator was asked for — a generator typo would show here instead of being inherited*',
      all(abs(_CFG[(b, 'S030')]['MNU'] - 0.30) < 5e-07
          and abs(_CFG[(b, 'S060')]['MNU'] - 0.60) < 5e-07
          and _CFG[(b, sl)]['NUHIER'] is True
          for b in ('base', 'nq24', 'lmax18') for sl in ('S030', 'S060')))

check('Ⓙ⓶ ⛭⛭ ** AND THE TWO GRIDS ARE READ OFF THEM TOO: ** the base bank ran at `12` nodes and '
      'cutoff `12`, the convergence banks at `24` nodes and at cutoff `18`, each on both sums, and '
      'the cut is `20` throughout.  ⇒ *so gates Ⓠ⓶ and Ⓠ⓷ are known to have measured the change '
      'they are named for, rather than two banks that happened to be labelled that way*',
      all(_CFG[('base', sl)]['NQ'] == 12 and _CFG[('base', sl)]['LMAXNU'] == 12
          and _CFG[('nq24', sl)]['NQ'] == 24 and _CFG[('nq24', sl)]['LMAXNU'] == 12
          and _CFG[('lmax18', sl)]['NQ'] == 12 and _CFG[('lmax18', sl)]['LMAXNU'] == 18
          and abs(_CFG[(b, sl)]['QMAXNU'] - 20.0) < 1e-12
          for sl in ('S030', 'S060') for b in ('base', 'nq24', 'lmax18')))

check('Ⓙ⓷ ⛭ ** AND EVERY OTHER FIGURE THIS REVISION PRINTS IS PINNED WITHIN HALF A PRINTED '
      'DIGIT: ** the four distances from one `0.01086`, `0.02115`, `0.01945` and `0.02260`; the '
      'order\'s band `0.03`; and the massless limit\'s flatness factors `1.05` and `1.16`.  '
      '⇒ *printed beside this receipt, so each has to fail here if it were wrong*',
      abs(_OFF['TT|0.30'] - 0.01086) < 5e-06
      and abs(_OFF['TT|0.60'] - 0.02115) < 5e-06
      and abs(_OFF['EE|0.30'] - 0.01945) < 5e-06
      and abs(_OFF['EE|0.60'] - 0.02260) < 5e-06
      and abs(VA['BAND'] - 0.03) < 1e-12
      and abs(FL['flat']['12'] - 1.05) < 5e-03
      and abs(FL['flat']['24'] - 1.16) < 5e-03)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
