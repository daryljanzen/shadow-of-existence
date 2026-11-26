# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE MASS ENTERS THE INSTRUMENT'S PERTURBATIONS ONLY AS A SUBTRACTION AND NEVER AS A SOURCE,
THE TT AMPLITUDE EXCESS IS NOT THE LEAN, AND THE EPOCH-CONSISTENT REPAIR REACHES THE RIGHT OBJECT AND
OVER-APPLIES: IT IS REFUTED ON ITS OWN REGISTERED VALIDATION, BY THE BLOCK THAT ALREADY MATCHED.

COMPUTES: the closure deficit of the instrument's four perturbation weights, measured by EXECUTING
the instrument's own prelude rather than reimplementing it, at two sums and at two epochs, and set
beside the instrument's own banked sum response over the same stretch so that the repair cannot be
credited with more than the defect it removes; the lean re-read with the TT amplitude excess divided
out of the response, on BOTH of the score's columns and under two no-free-parameter interpolations
of `A(Sigma)`, against the move the earlier revision recorded; and the new perturbation switch's
byte-identity when off, its two refusals, the same closure under it, and `A` and `eps` refitted
against CAMB on the repaired perturbations by the PREVIOUS revision's own fit, executed rather than
re-implemented, with its reproduction leg required to return that revision's headline first.
** IT PINS AS RESULTS: the deficits `-2.024528e-03` and `-6.970164e-03` at `0.30` eV and
`-7.544464e-03` and `-1.397832e-02` at `0.60`, against the response's own `1.641809e-02` and
`3.800102e-02`, so `0.1233` and `0.1985` of it; the species' Fermi-Dirac `w` at recombination,
`0.320474` and `0.290599`, against the `1/3` its own equations hard-code; the corrected moves
`-19.330577` and `-19.299451` against the recorded `-20.09`, so `0.0378` and `0.0394` of it removed;
and the closure under the switch at `1.110223e-16` and `2.220446e-16`; and on the repaired
perturbations `A = 0.86401` and `0.81466` in TT against `1.15162` and `1.29592`, with `0.94474` and
`0.91120` in EE against `1.01405` and `1.04630`, the two shear arms `0.00376` and `0.00364` apart,
and the fitted residuals falling by `3.5` to `5.9` times. **
⛔ ** AND IT PINS WHAT WAS WRONG IN THIS LINE'S OWN FIRST RUN AND HOW IT WAS CAUGHT: ** the
correction arm's reproduction leg read the RE-PROFILED column where the headline is the FROZEN one
AND took the move with the opposite sign to the record's own table; both are pinned here as the
defect and as the reproduction that found it, `-20.086848` and `-48.201966` against `-20.09` and
`-48.20`.
⛔ ** AND IT PINS THE VERDICT AS Ⓖ ON A BAND THAT IS NOT MOVED, WITH THE NEAR THING SAID OUT LOUD: **
EE's `0.05526` at `0.30` eV sits just past the `0.05` band, and the threshold is left where it was;
what decides it either way is `0.01405 -> 0.05526`, the repair breaking the block that matched.
⛔ ** NO LIMIT AND NO ENVELOPE CROSSING IS PINNED HERE, because the verdict is Ⓖ and none was read.
No decomposition of the three changes is pinned either: it is not run here, and it is routed. **

⌷ ** THE ID. **  `69` ordered this as `r7875`, which merged `r7874`, ruled the envelope a screen and
the shift-amplitude fit the verdict, and overruled this seat's recommendation not to build the
conditional switch -- on the physics, and not on the share table.

⚠ ** FOUR THINGS IN THIS RECORD ARE THIS SEAT'S OWN: the two defects above; the ONE declared
uncertainty of the approximation, measured and found NOT to be the cause; and a verdict that fires on
a band this seat set, at a margin this seat reports rather than smooths. **

    NODE=60 python3 <this file>

Written r7876 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7876_60_the_epoch_consistent_neutrino_perturbations_and_whether_the_amplitude'
                 '_excess_is_the_lean')
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
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

CL = load('closure.json')
AM = load('amp_arm.json')
BI = load('byte_identical.json')
#: ⛔ *the prose is matched on a WHITESPACE-FLATTENED copy -- four arms of an earlier revision's
#: receipt failed on where a line happened to wrap, which is a fact about the editor and not about
#: the record.*
RESULT = ' '.join(text('RESULT.md').split())
PRED = ' '.join(text('PREDICTION.md').split())
GEN_FLAT = ' '.join(text('gen_nupert.sh').split())
INST = text('ACOUSTIC_two_arm.py', BW)
CLOSE_PY = text('closure.py')
AMP_PY = text('amp_arm.py')

# ══ Ⓐ ① WHAT IS THERE, READ OFF THE SOURCE ══════════════════════════════════════════════════════
# *Every clause of the statement is checked against the file itself.  The landed behaviour is
#  exactly the OFF branch of this revision's switch, which is still present verbatim, so the
#  clauses are checkable on the file as it now stands.*

check('Ⓐ①ᵃ ⛭ ** THE CLUSTERING MATTER LOSES omega_nu AT EVERY EPOCH: the line is `OCDM = OM - OB - '
      'ONU` with `ONU` the species\' LATE constant, and it carries no epoch dependence at all. **  '
      '⇒ *this is the subtraction, and it is the only place the mass reaches the perturbations*',
      INST.count('\nOCDM = OM - OB - ONU\n') == 1
      and '\nONU = MNU / 93.14 / (H0 / 100) ** 2' in INST
      and 'only as a SUBTRACTION and never as a source' in RESULT)

check('Ⓐ①ᵇ ⛭ and the WEIGHT the potential\'s source carries it at is the STRICTLY MASSLESS one, '
      '`FNU * (OR / a^4) / _rt`, with the Fermi-Dirac factor NOT multiplying it.  ⇒ *so in the '
      'perturbations the species gravitates as pure radiation for all time, whatever the background '
      'does*',
      'On_of = CubicSpline(eg, FNU * (OR / ag ** 4) / _rt)' in INST
      and 'Og_of = CubicSpline(eg, (1 - FNU) * (OR / ag ** 4) / _rt)' in INST)

check('Ⓐ①ᶜ ⛭ and the species\' OWN equations hard-code `w = 1/3` and `c_s^2 = 1/3`, with no '
      '`-H(1-3w) theta` drag and no `w-dot` term -- in BOTH right-hand sides, which is why the '
      'repair had to reach both',
      INST.count('out[:, 4] = -(4 / 3) * tn + DRC * 4 * Php') == 2
      and INST.count('out[:, 5] = kk ** 2 * (dn / 4 - sig) + DRE * kk ** 2 * Ps') == 2)

check('Ⓐ①ᵈ ⛭ and the one route by which the repaired BACKGROUND reaches the perturbations is the '
      'shared denominator `_rt`, which divides all four weights TOGETHER and so cannot move the '
      'neutrino\'s share.  ⇒ *that is why a verified background repair left the perturbation defect '
      'standing*',
      "rescales all four weights **together** and so cannot move the neutrino's share"
      in RESULT)

check('Ⓐ①ᵉ ⛭ ** AND THE NO-FREE-PARAMETER INGREDIENT THE REPAIR NEEDS WAS ALREADY IN THE FILE AND '
      'READ NOWHERE: ** `NUW_of`, the Fermi-Dirac `p_nu/rho_nu` spline, is built under the '
      'background switch and is CALLED exactly once in the whole file -- inside the block this '
      'revision adds.  ⇒ *before this revision it was called zero times*',
      INST.count('NUW_of(') == 1
      and 'NUW_of = CubicSpline(_nu_la,' in INST
      and '_w_eg = NUW_of(np.log(ag))' in INST,
      'called %d time(s)' % INST.count('NUW_of('))

check('Ⓐ①ᶠ ⌗ and `Om_of` is DEAD -- defined once, read nowhere.  ⇒ *reported rather than deleted: '
      'this seat does not quietly tidy a file another seat\'s receipts run against*',
      INST.count('Om_of') == 2 and 'Om_of = CubicSpline(eg, ((OM - ONU) / ag ** 3) / _rt)' in INST,
      '%d occurrence(s), one of them the definition' % INST.count('Om_of'))

# ══ Ⓑ ① THE DESIGN NUMBER, MEASURED ═════════════════════════════════════════════════════════════
check('Ⓑ①ᵃ ⛭ ** THE DEFICIT IS MEASURED BY EXECUTING THE INSTRUMENT\'S OWN PRELUDE -- its lines '
      '1..645 in a fresh namespace -- AND NOT BY REIMPLEMENTING ITS SPLINES. **  ⇒ *a second copy '
      'of a definition is how two numbers come to be called the same thing*',
      '_CUT = 645' in CLOSE_PY and 'exec(compile(head, SRC, \'exec\'), ns)' in CLOSE_PY
      and 'EXECUTES the instrument' in ' '.join(CLOSE_PY.split()))

for tag, mnu, dr, dn in (('S030', 0.30, -2.024528e-03, -6.970164e-03),
                         ('S060', 0.60, -7.544464e-03, -1.397832e-02)):
    r = CL[tag]
    check('Ⓑ①ᵇ(%.2f) ⛭ the closure deficit at `Sigma = %.2f` eV: `%+.6e` at recombination and '
          '`%+.6e` today -- the mass the perturbations do not see, as a fraction of the total '
          'gravitating density' % (mnu, mnu, dr, dn),
          abs(r['d_rec'] - dr) < 5e-09 and abs(r['d_now'] - dn) < 5e-09,
          '%.6e / %.6e' % (r['d_rec'], r['d_now']))

for tag, mnu, rms, rat in (('S030', 0.30, 1.641809e-02, 0.1233),
                           ('S060', 0.60, 3.800102e-02, 0.1985)):
    r = CL[tag]
    q = abs(r['d_rec']) / r['r_rms']
    check('Ⓑ①ᶜ(%.2f) ⛭ ** AND IT IS SET BESIDE THE RESPONSE\'S OWN SIZE BEFORE THE REPAIR WAS '
          'DESIGNED: ** rms `%.6e` over the stretch, so the deficit is `%.4f` of it -- above the '
          'tenth the registration set as the floor.  ⇒ *the defect is the right size, and the '
          'repair is not licensed to be credited with more than it*' % (mnu, rms, rat),
          abs(r['r_rms'] - rms) < 5e-08 and abs(q - rat) < 5e-05 and q > 0.10,
          'rms %.6e, ratio %.4f' % (r['r_rms'], q))

for tag, mnu, w in (('S030', 0.30, 0.320474), ('S060', 0.60, 0.290599)):
    check('Ⓑ①ᵈ(%.2f) ⛭ and the LARGER half of the defect is the equation of state, not the weight: '
          'the species\' Fermi-Dirac `w` at recombination is `%.6f`, against the `1/3` its own '
          'continuity and Euler equations hard-code' % (mnu, w),
          abs(CL[tag]['w_rec'] - w) < 5e-07
          and abs(CL[tag]['w_now']) < 1e-04,
          '%.6f, and %.3e today' % (CL[tag]['w_rec'], CL[tag]['w_now']))

# ══ Ⓒ ② THE SEPARATION, AND THE TWO DEFECTS THE REPRODUCTION ARM FOUND ══════════════════════════
check('Ⓒ②ᵃ ⛔⛭ ** THIS FILE\'S FIRST RUN WAS WRONG TWICE AND THE REPRODUCTION ARM IS WHAT SAID SO: '
      'it read the RE-PROFILED column where the `-20.09` headline is the FROZEN one, AND it took '
      'the move with the opposite sign to the record\'s own table. **  ⇒ *both are fixed at the '
      'cause against that record and BOTH columns are now reported; an arm that only ever agreed '
      'would have found neither*',
      'opposite sign, and the reproduction arm is what said so'
      in ' '.join(AMP_PY.split())
      and 'MOVE_REPROFILED = -48.20' in AMP_PY
      and 'THE REPRODUCTION ARM CAUGHT TWO DEFECTS' in RESULT)

for col, rec_m, got_m in (('frozen', -20.09, -20.086848), ('reprofiled', -48.20, -48.201966)):
    u = AM['uncorrected'][col]
    check('Ⓒ②ᵇ(%s) ⛭ and the uncorrected %s column reproduces the record to better than a '
          'hundredth of a meV: `%+.6f` against `%+.2f`' % (col, col, got_m, rec_m),
          u['reproduced'] is True and abs(u['move'] - got_m) < 5e-06
          and abs(u['move'] - rec_m) <= 0.05,
          '%+.6f (|d| = %.4f)' % (u['move'], u['dev']))

check('Ⓒ②ᶜ ⛭ the corrected band is `35` TT bins of the `555` scored, spanning multipoles '
      '`100..414`, of which `12` are among the thirty-six removed -- so the correction covers the '
      'bins whose removal IS the lean',
      AM['band_bins'] == 35 and AM['band_lo'] == 100 and AM['band_hi'] == 414
      and AM['removed_in_band'] == 12)

for f, m, frac in (('L', -19.330577, 0.0378), ('Q', -19.299451, 0.0394)):
    r = AM['forms'][f]['frozen']
    check('Ⓒ②ᵈ(%s) ⛭ ** AND THE VERDICT IS Ⓑ ON BOTH INTERPOLATIONS: ** dividing the whole TT '
          'amplitude excess out of the response moves the lean to `%+.6f` meV, which is `%.4f` of '
          'it removed -- against the `0.30` the registration set for Ⓑ and the `0.982` it set for '
          'Ⓐ' % (f, m, frac),
          abs(r['move'] - m) < 5e-06 and abs(r['f'] - frac) < 5e-05 and r['f'] <= 0.30,
          '%+.6f meV, f = %.4f' % (r['move'], r['f']))

check('Ⓒ②ᵉ ⛭ and the two interpolations agree to `%.4f` in the fraction, far inside the verdict '
      'gap, so the arm is DECIDED and not left to the interpolation -- which is the outcome the '
      'registration made reportable in advance' % AM['f_spread'],
      AM['verdicts'] == ['B'] and AM['agree'] is True and AM['f_spread'] < 0.01
      and abs(AM['f_spread'] - 0.0015493) < 5e-06,
      'spread %.6f' % AM['f_spread'])

check('Ⓒ②ᶠ ⛔ ** AND WHAT THIS SETTLES IS STATED NARROWLY: ** the previous ruling made the low-'
      'multipole residual and the lean ONE OBJECT until a measurement separated them; this '
      'separates them, and it does NOT say the lean is not an instrument defect -- only that what '
      'carries it is not the amplitude of the TT sum response over this band',
      'This is that measurement, and it separates them' in RESULT
      and 'It does not say the lean is not an instrument defect' in RESULT)

# ══ Ⓓ ③ THE SWITCH'S OWN ARMS, BEFORE ANY SPECTRUM IS READ THROUGH IT ═══════════════════════════
check('Ⓓ③ᵃ ⛭ ** BYTE-IDENTICAL OFF IS MEASURED ON OUTPUT AND NOT ASSERTED: ** `origin/main`\'s own '
      'copy of the instrument against the patched one, with the switch ABSENT and with it `=0`, '
      'every array of both saves identical element for element -- `6` in the TT save and `11` in '
      'the polarisation one, four comparisons in all',
      BI['byte_identical'] is True and len(BI['compare']) == 4
      and all(v['arrays_identical'] for v in BI['compare'].values())
      and BI['compare']['tt|absent']['n_arrays'] == 6
      and BI['compare']['pol|absent']['n_arrays'] == 11)

check('Ⓓ③ᵃᵃ ⌗ and the `config` string DIFFERS in all four, and must: it carries the git blob hash '
      'of the file\'s own bytes.  ⇒ *a config that AGREED there would mean the patch had not been '
      'applied, which is the opposite of the thing being checked*',
      all(v['config_same'] is False for v in BI['compare'].values())
      and "it carries the git blob hash of the file's own bytes" in RESULT)

check('Ⓓ③ᵇ ⛔ ** AND IT REFUSES TO RUN HALF: ** the switch on without the Fermi-Dirac background, '
      'and on at a zero sum, both exit non-zero naming the reason -- the repair IS the species\' '
      'own Fermi-Dirac weight, so neither is a configuration it may silently run',
      all(v['refused'] and v['rc'] != 0 for v in BI['refusals'].values())
      and len(BI['refusals']) == 2
      and all('NUPERT=1 needs NUFD=1 and MNU != 0' in (v['message'] or '')
              for v in BI['refusals'].values()))

for tag, mnu, worst in (('S030', 0.30, 1.110223e-16), ('S060', 0.60, 2.220446e-16)):
    r = CL['nupert'][tag]
    check('Ⓓ③ᶜ(%.2f) ⛭ ** AND THE DEFECT THE REPAIR WAS MEASURED AS NOW CLOSES EXACTLY: ** the '
          'deficit under the switch is `%.6e` at `Sigma = %.2f` eV, at recombination and today -- '
          'the numerator becomes the stack term for term' % (mnu, worst, mnu),
          abs(r['worst'] - worst) < 1e-18 and r['worst'] < 1e-12,
          '%.6e' % r['worst'])

check('Ⓓ③ᵈ ⛭ the approximation is NAMED in the code and in the record, and its one gap is DECLARED '
      'and bounded by measurement rather than hidden: the shear ladder is left relativistic at all '
      'epochs, a second arm switches the species\' shear off below `w = 1/6`, and the SPREAD between '
      'them is reported as the approximation\'s own uncertainty on `A`',
      'THE FERMI-DIRAC FLUID APPROXIMATION' in INST
      and '_NU_NR = 1.0 / 6.0' in INST and 'NUSHOFF=1` switches that' in INST
      and 'WHAT IT DOES NOT DO' in INST
      and 'bounded rather than hidden' in RESULT)

check('Ⓓ③ᵉ ⛭ and the weight is redefined WHERE IT IS BUILT and not at its use sites, so all SEVEN '
      'of them -- both right-hand sides and the four source paths -- take it together and cannot '
      'disagree',
      'On_of = CubicSpline(eg, Onu_of(ag) / _rt)' in INST
      and INST.count('On_of(') == 7
      and 'take it together and cannot disagree' in RESULT,
      '%d call site(s)' % INST.count('On_of('))

check('Ⓓ③ᶠ ⌗ and the two new switches are recorded in the run\'s resolved config, for the reason an '
      'earlier revision established when it found the landed bank carried no background-switch key '
      'AT ALL: a bank made before this revision says `null` rather than `false`, which is the '
      'difference between "it was off" and "this bank cannot say"',
      "'NUPERT': bool(NUPERT)," in INST and "'NUSHOFF': bool(NUSHOFF)," in INST
      and 'THE KEY IS ABSENT' in INST)

check('Ⓓ③ᵍ ⌗ and the zero leg is NOT recomputed, with the reason stated where the legs are made: '
      'the background switch is itself gated on a non-zero sum, so the new switch is PROVABLY inert '
      'there -- which is also why it refuses to run there rather than pretending to',
      'WHY THE ZERO LEG IS NOT RE-RUN' in GEN_FLAT
      and 'PROVABLY INERT' in GEN_FLAT
      and 'NUPERT=1' in GEN_FLAT and 'NUSHOFF=' in GEN_FLAT)

# ══ Ⓔ THE REGISTRATION ══════════════════════════════════════════════════════════════════════════
check('Ⓔ⓪ᵃ ⛭ ** THE REGISTRATION WAS COMMITTED AND PUSHED BEFORE ANY MEASUREMENT OF THIS REVISION '
      'RAN, and it carries both verdict tables with their thresholds -- which are the thresholds '
      'the result is read on, unmoved. **',
      'Register-before-measure' in PRED
      and 'the amplitude excess IS the lean' in PRED
      and 'f ≤ 0.30' in PRED)

check('Ⓔ⓪ᵃᵃ ⛭ and it registered a REACHABLE NEGATIVE on the repair before the repair existed -- '
      'that if the deficit came out small against the response, the order\'s own alternative is the '
      'expected finding -- and the measured ratios cleared it rather than the clause being dropped',
      'the defect is elsewhere' in PRED
      and 'will not rescue ③ by widening it' in PRED
      and all(abs(CL[t]['d_rec']) / CL[t]['r_rms'] > 0.10 for t in ('S030', 'S060')))

check('Ⓔ⓪ᵃᵇ ⛭ and the six reads taken before the registration are DECLARED in it, the first being '
      'that item ① IS a read of the code and so could not be taken after',
      'READS TAKEN BEFORE THIS REGISTRATION — DECLARED' in PRED
      and 'READS TAKEN BEFORE THIS REGISTRATION — DECLARED' in PRED
      and 'No spectrum of this revision has been computed' in PRED)

# ══ Ⓔ ③'s VALIDATION, ON THE BAND FIXED BEFORE THE REPAIR WAS WRITTEN ═══════════════════════════
RF = load('refit.json')
REFIT_PY = text('refit.py')

check("Ⓕ③ᵃ ⛭ ** THE FIT IS NOT RE-IMPLEMENTED: the previous revision's own `shift.py` is EXECUTED "
      'with TWO lines rebound -- the bank it reads and the file it writes -- so the CAMB legs, the '
      '`eps` allowance measured off the bank\'s acoustic scale against CAMB\'s own, the `eps` grid, '
      'the `A`-across-the-band measurement and the verdict logic are the ones that revision was '
      'judged on. **  ⇒ *a fit re-implemented here would be a second instrument, and `1.152 -> ?` '
      'would then be a comparison between two of them*',
      'NOT RETYPED, AND NOT APPROXIMATED EITHER' in REFIT_PY
      and 'the_two_rebindings' in REFIT_PY
      and "ON = os.environ['R7876_ON']" in REFIT_PY
      and "OUT = os.environ['R7876_OUT']" in REFIT_PY)

check('Ⓕ③ᵃᵃ ⛭ and its REPRODUCTION leg on the landed bank returns that revision\'s headline to five '
      'decimal places in all four rows, which is what makes the repaired legs readable at all',
      RF['reproduced'] is True
      and abs(RF['landed']['fits']['TT|0.30']['best_A'] - 1.15162) < 5e-06
      and abs(RF['landed']['fits']['TT|0.60']['best_A'] - 1.29592) < 5e-06
      and abs(RF['landed']['fits']['EE|0.30']['best_A'] - 1.01405) < 5e-06
      and abs(RF['landed']['fits']['EE|0.60']['best_A'] - 1.04630) < 5e-06,
      'TT %.5f / %.5f, EE %.5f / %.5f'
      % tuple(RF['landed']['fits'][k]['best_A']
              for k in ('TT|0.30', 'TT|0.60', 'EE|0.30', 'EE|0.60')))

for k, a_now in (('TT|0.30', 0.86401), ('TT|0.60', 0.81466),
                 ('EE|0.30', 0.94474), ('EE|0.60', 0.91120)):
    check('Ⓕ③ᵇ(%s) ⛭ on the repaired perturbations `A = %.5f`' % (k, a_now),
          abs(RF['shear_on']['fits'][k]['best_A'] - a_now) < 5e-06,
          '%.5f' % RF['shear_on']['fits'][k]['best_A'])

check('Ⓕ③ᶜ ⛔⛭ ** THE VERDICT IS Ⓖ -- THE REPAIR IS REFUTED ON ITS OWN REGISTERED VALIDATION, AND BY '
      'THE BLOCK THAT ALREADY MATCHED: ** EE\'s departure from one goes from `0.01405` to `0.05526` '
      'at `0.30` eV and from `0.04630` to `0.08880` at `0.60`, where the order required that EE '
      '"must not move away from its present agreement".  ⇒ *so NO limit is read through the switch, '
      'and ④ does not start*',
      RF['verdict'] == 'G'
      and abs(RF['bands']['EE'] - 0.05) < 1e-12
      and abs(RF['shear_on']['fits']['EE|0.30']['best_A'] - 1.0) > RF['bands']['EE']
      and abs(RF['shear_on']['fits']['EE|0.60']['best_A'] - 1.0) > RF['bands']['EE']
      and 'No limit is read through `NUPERT`' in RESULT)

check('Ⓕ③ᶜᶜ ⛔ and the band is NOT MOVED, with the near thing said rather than smoothed: `0.05526` '
      'against `0.05` at the lower sum is a margin of `0.00526`, and the higher sum is not close at '
      '`0.08880`.  ⇒ *the comparison that decides it either way is not the threshold but '
      '`0.01405 -> 0.05526`*',
      abs(abs(RF['shear_on']['fits']['EE|0.30']['best_A'] - 1.0) - 0.05526) < 5e-06
      and 'the threshold is a near thing' in RESULT
      and 'and it is held unmoved' in RESULT)

for k, frac in (('TT|0.30', 0.1053), ('TT|0.60', 0.3739)):
    check('Ⓕ③ᵈ(%s) ⛭ ** AND THE REFUTATION IS NOT THAT NOTHING HAPPENED: ** TT\'s `A` moves TOWARD '
          'one by `%.4f` of its excess, so the defect ① located is real and the repair\'s SIGN is '
          'right' % (k, frac),
          abs(RF['summary']['shear_on|%s' % k]['frac'] - frac) < 5e-05
          and RF['summary']['shear_on|%s' % k]['frac'] > 0.0,
          '%.4f' % RF['summary']['shear_on|%s' % k]['frac'])

check('Ⓕ③ᵉ ⛔⛭ ** IT OVERSHOOTS, AND THE ORDER\'S VALIDATION DID NOT ENUMERATE THAT STATE: ** `A` '
      'does not fall toward one and stop, it CROSSES and lands at `0.86401` and `0.81466`.  The '
      'order enumerated "falls toward 1" and "does not move"; the repair did neither.  ⇒ *a '
      'defence against a state changing has to enumerate the states it may produce, and this one '
      'produced a third*',
      RF['shear_on']['fits']['TT|0.30']['best_A'] < 1.0
      and RF['shear_on']['fits']['TT|0.60']['best_A'] < 1.0
      and "It OVERSHOOTS, and the order's validation did not enumerate that state"
      in RESULT
      and 'the repair did neither' in RESULT)

check('Ⓕ③ᶠ ⛭ ** AND THE ONE GAP THIS SEAT DECLARED IS MEASURED AND IS NOT THE CAUSE: ** the two '
      'shear arms differ by `0.0037550` and `0.0036366` in `A`, which is `2.76` and `1.96` per '
      'cent of the overshoot they would have to explain.  ⇒ *a declared uncertainty that turns out '
      'not to matter removes a candidate, which is worth as much as one that does*',
      abs(RF['A_spread_shear']['0.30'] - 0.0037550) < 5e-07
      and abs(RF['A_spread_shear']['0.60'] - 0.0036366) < 5e-07
      and max(RF['A_spread_shear'].values())
      < 0.05 * abs(RF['shear_on']['fits']['TT|0.60']['best_A'] - 1.0)
      and 'IS MEASURED AND IS NOT THE CAUSE' in RESULT,
      '%.6f / %.6f' % (RF['A_spread_shear']['0.30'], RF['A_spread_shear']['0.60']))

_rat = [(RF['landed']['fits'][k]['resid_best'] / RF['shear_on']['fits'][k]['resid_best'])
        for k in ('TT|0.30', 'TT|0.60', 'EE|0.30', 'EE|0.60')]
check('Ⓕ③ᵍ ⛭ ** AND THE SHAPE GETS SHARPLY BETTER WHILE THE AMPLITUDE OVERSHOOTS: ** the fitted '
      'residual falls in every block and every sum, by `3.5` to `5.9` times.  ⇒ *the repaired '
      'response has CAMB\'s SHAPE far more closely than the landed one and the wrong amplitude, '
      'which is a different finding from either branch the order wrote down*',
      all(r > 3.0 for r in _rat) and min(_rat) > 3.4 and max(_rat) < 6.0
      and 'THE SHAPE GETS SHARPLY BETTER' in RESULT,
      'factors %s' % ', '.join('%.1f' % r for r in _rat))

check('Ⓕ③ᵍᵍ ⌗ and `eps` grows with it, to `21.65` and `8.22` times its own measured allowance in TT, '
      'so the repair moves the peak position as well as the amplitude -- reported, not absorbed',
      abs(RF['shear_on']['fits']['TT|0.30']['eps_over_allowed'] - 21.65) < 0.05
      and abs(RF['shear_on']['fits']['TT|0.60']['eps_over_allowed'] - 8.22) < 0.05)

check('Ⓕ③ʰ ⛔ ** AND WHAT IS NOT DONE IS SAID: ** the three changes went in TOGETHER and this '
      'revision has no decomposition of which one over-corrects.  It is three legs per sum, it is '
      'NOT run here because it would need its own registration, and it is ROUTED -- narrowed first '
      'by the shear arm\'s result',
      'WHAT IS NOT DONE HERE, AND IS ROUTED' in RESULT
      and 'it is **not run here**' in RESULT
      and 'no decomposition of which one over-corrects' in RESULT)

# ══ Ⓗ THE RED THIS REVISION'S OWN DIFF CAUSED, AND THE CLASS THAT DISPOSES OF IT ════════════════
# *Adding a switch moves the instrument's blob, and two shared `P15` receipts compare the working
#  tree against a BANKED blob through an AST escape hatch that each adding seat extends by routing a
#  patch.  That red IS this revision's, so the class is measured here and routed, and the receipts
#  are not touched.*
SC = load('strip_class.json')
SC_PY = text('strip_class.py')
REPLY = ' '.join(text('FOR_66_FROM_60.md', ROOT).split())

check('Ⓗ⑧ᵃ ⛭ ** THE FIXED POINT: the eighth class reduces the working tree to the banked blob. ** '
      '⇒ *so the hatch certifies the instrument that produced the bank is still the one on disk, '
      'which is the claim the two receipts rest their arm on*',
      SC['fixed_point'] is True)

check('Ⓗ⑧ᵇ ⛭ and THE FLOOR: the seven landed classes ALONE leave it red, so the eighth is doing the '
      'work and is not a no-op riding on the others.  ⇒ *a class that would pass without being '
      'needed is an exemption with a nicer name*',
      SC['floor'] is False)

check('Ⓗ⑧ᶜ ⛭ and EIGHT controls, every one of which keeps the row RED: a moved landed constant, a '
      'deleted landed line, a changed landed operand, the guard made live-when-off, a moved LANDED '
      'default, a moved default of THIS revision\'s own switch, a moved marker of its shear arm, '
      'and an unguarded factor in place of the guarded one',
      len(SC['controls']) == 8 and all(SC['controls'].values()),
      '%d control(s), all red' % len(SC['controls']))

check('Ⓗ⑧ᵈ ⛔⛭ ** AND THIS SEAT\'S OWN HOLE, FOUND BY ITS OWN CONTROL AND FIXED RATHER THAN '
      'DROPPED: ** the landed classes strip a new switch\'s binding BY NAME, and written that way '
      'this class\'s "moved default" control PASSED -- with the binding stripped by name, a later '
      'change making the switch default ON would be invisible and the hatch would certify a tree '
      'whose switch is live.  ⇒ *the class now matches the four statements on their EXACT value '
      'expression, so a moved default keeps the row red; the same hole is in the fifth and seventh '
      'classes and is reported to the seat that owns them rather than repaired here*',
      'TIGHTER THAN ITS PREDECESSORS, AND ON PURPOSE' in SC_PY
      and 'NEW_STATEMENTS' in SC_PY
      and 'the one that found the hole' in REPLY
      and 'The same hole is in the fifth and seventh classes' in REPLY)

check('Ⓗ⑧ᵉ ⛭ and the patch was VERIFIED and then REVERTED: both receipts were run with it applied '
      'and came back clean, and the files were restored, because they are shared and the convention '
      'is that the gating seat applies the patch.  ⇒ *routing a patch and saying it was run is only '
      'honest if it was run*',
      'rc=0`, zero failed arms, zero failed checks on each — then **reverted the files**'
      in REPLY)

check('Ⓗ⑧ᶠ ⌗ and the switch-count gate of another seat is routed the same way, not edited: this '
      'revision takes the instrument from ninety-one environment switches to ninety-three, which is '
      'that gate\'s own convention -- the count may move and each mover is named with its commit',
      'A PATCH FOR YOUR SWITCH-COUNT GATE, ROUTED AND NOT APPLIED' in REPLY
      and 'now reads **93** switches where your gate names 91' in REPLY)

# ══ Ⓖ EVERY FIGURE THE INDEX ROW PRINTS, PINNED POINTWISE AND NOT THROUGH A LOOP ════════════════
# ⚠ *The arms above hold most of these already -- but they hold them through a LOOP VARIABLE, and a
#   literal read off a loop variable is not a pin: the comparison the instrument parses contains no
#   number at all.  That trap cost an earlier revision of this line four figures.  So every figure
#   the register's row prints is pinned HERE, pointwise, with the literal written into the
#   comparison, inside the allowance for the digits the row actually prints.*
F = CL['S030']
G = CL['S060']
AM_F = AM['forms']
RS = RF['shear_on']['fits']
RL = RF['landed']['fits']

check('Ⓖ⓪ᵃ the two sums the record is read at', abs(F['mnu'] - 0.30) < 1e-09
      and abs(G['mnu'] - 0.60) < 1e-09)
check('Ⓖ⓪ᵇ the closure deficit ratio `0.1233` at the lower sum',
      abs(abs(F['d_rec']) / F['r_rms'] - 0.1233) < 5e-05)
check('Ⓖ⓪ᶜ and `0.1985` at the higher',
      abs(abs(G['d_rec']) / G['r_rms'] - 0.1985) < 5e-05)
check('Ⓖ⓪ᵈ the Fermi-Dirac `w` at recombination, `0.320474`',
      abs(F['w_rec'] - 0.320474) < 5e-07)
check('Ⓖ⓪ᵉ and `0.290599`', abs(G['w_rec'] - 0.290599) < 5e-07)
check('Ⓖ⓪ᶠ the corrected move `19.330577` meV, form L',
      abs(abs(AM_F['L']['frozen']['move']) - 19.330577) < 5e-06)
check('Ⓖ⓪ᵍ and `19.299451`, form Q',
      abs(abs(AM_F['Q']['frozen']['move']) - 19.299451) < 5e-06)
check('Ⓖ⓪ʰ the fraction of the lean removed, `0.0378`',
      abs(AM_F['L']['frozen']['f'] - 0.0378) < 5e-05)
check('Ⓖ⓪ⁱ and `0.0394`', abs(AM_F['Q']['frozen']['f'] - 0.0394) < 5e-05)
check('Ⓖ⓪ʲ ⛔ the uncorrected move `20.09` meV, pinned to the digits the row prints and NOT to the '
      'five-hundredths the reproduction arm above allows -- that arm answers "does it reproduce the '
      'record", this one answers "would this receipt fail if the printed figure were wrong", and '
      'they are two questions',
      abs(abs(AM['uncorrected']['frozen']['move']) - 20.09) < 0.0099)
check('Ⓖ⓪ᵏ the refitted `A = 0.86401` in TT at the lower sum',
      abs(RS['TT|0.30']['best_A'] - 0.86401) < 5e-06)
check('Ⓖ⓪ˡ and `0.81466` at the higher', abs(RS['TT|0.60']['best_A'] - 0.81466) < 5e-06)
check('Ⓖ⓪ᵐ and EE\'s `0.94474`', abs(RS['EE|0.30']['best_A'] - 0.94474) < 5e-06)
check('Ⓖ⓪ⁿ and EE\'s `0.91120`', abs(RS['EE|0.60']['best_A'] - 0.91120) < 5e-06)
check('Ⓖ⓪ᵒ the reproduced `1.15162` and `1.29592` in TT',
      abs(RL['TT|0.30']['best_A'] - 1.15162) < 5e-06
      and abs(RL['TT|0.60']['best_A'] - 1.29592) < 5e-06)
check('Ⓖ⓪ᵖ and the reproduced `1.01405` and `1.04630` in EE',
      abs(RL['EE|0.30']['best_A'] - 1.01405) < 5e-06
      and abs(RL['EE|0.60']['best_A'] - 1.04630) < 5e-06)
check('Ⓖ⓪ᑫ the fraction of TT\'s excess removed, `0.1053`',
      abs(RF['summary']['shear_on|TT|0.30']['frac'] - 0.1053) < 5e-05)
check('Ⓖ⓪ʳ and `0.3739`', abs(RF['summary']['shear_on|TT|0.60']['frac'] - 0.3739) < 5e-05)
check('Ⓖ⓪ˢ the two shear arms\' separation, `0.0037550` and `0.0036366`',
      abs(RF['A_spread_shear']['0.30'] - 0.0037550) < 5e-08
      and abs(RF['A_spread_shear']['0.60'] - 0.0036366) < 5e-08)
check('Ⓖ⓪ᵗ EE\'s departure from one, `0.05526`, and the `0.05` band it sits `0.00526` past',
      abs(abs(RS['EE|0.30']['best_A'] - 1.0) - 0.05526) < 5e-06
      and abs(RF['bands']['EE'] - 0.05) < 1e-12)
check('Ⓖ⓪ᵘ the closure under the switch, `1.110223e-16` and `2.220446e-16`',
      abs(CL['nupert']['S030']['worst'] - 1.110223e-16) < 1e-22
      and abs(CL['nupert']['S060']['worst'] - 2.220446e-16) < 1e-22)
check('Ⓖ⓪ᵛ the four closure deficits the row prints',
      abs(F['d_rec'] + 2.024528e-03) < 5e-09 and abs(F['d_now'] + 6.970164e-03) < 5e-09
      and abs(G['d_rec'] + 7.544464e-03) < 5e-09 and abs(G['d_now'] + 1.397832e-02) < 5e-09)
check('Ⓖ⓪ʷ and the two response sizes they are read against, `1.641809e-02` and `3.800102e-02`',
      abs(F['r_rms'] - 1.641809e-02) < 5e-08 and abs(G['r_rms'] - 3.800102e-02) < 5e-08)
check('Ⓖ⓪ˣ the two interpolations\' agreement, `0.0015`',
      abs(AM['f_spread'] - 0.0015493) < 5e-06)
check('Ⓖ⓪ʸ the `2.76` and `1.96` per cent the shear arms are of the overshoot',
      abs(100 * RF['A_spread_shear']['0.30'] / abs(RS['TT|0.30']['best_A'] - 1.0) - 2.76) < 0.005
      and abs(100 * RF['A_spread_shear']['0.60'] / abs(RS['TT|0.60']['best_A'] - 1.0) - 1.96)
      < 0.005)
check('Ⓖ⓪ᶻ and EE\'s `0.01405` before against `0.05526` after, and `0.04630` against `0.08880`',
      abs(abs(RL['EE|0.30']['best_A'] - 1.0) - 0.01405) < 5e-06
      and abs(abs(RL['EE|0.60']['best_A'] - 1.0) - 0.04630) < 5e-06
      and abs(abs(RS['EE|0.60']['best_A'] - 1.0) - 0.08880) < 5e-06)

print('=' * 100)
print('  %d arm(s), %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('   FAILED: %s' % f)
sys.exit(1 if FAILS else 0)
