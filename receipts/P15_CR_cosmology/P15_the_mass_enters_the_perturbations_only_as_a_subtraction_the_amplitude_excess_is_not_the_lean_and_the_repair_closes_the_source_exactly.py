# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE MASS ENTERS THE INSTRUMENT'S PERTURBATIONS ONLY AS A SUBTRACTION AND NEVER AS A SOURCE,
THE TT AMPLITUDE EXCESS IS NOT THE LEAN, AND THE EPOCH-CONSISTENT REPAIR CLOSES THE SOURCE EXACTLY.

COMPUTES: the closure deficit of the instrument's four perturbation weights, measured by EXECUTING
the instrument's own prelude rather than reimplementing it, at two sums and at two epochs, and set
beside the instrument's own banked sum response over the same stretch so that the repair cannot be
credited with more than the defect it removes; the lean re-read with the TT amplitude excess divided
out of the response, on BOTH of the score's columns and under two no-free-parameter interpolations
of `A(Sigma)`, against the move the earlier revision recorded; and the new perturbation switch's
byte-identity when off, its two refusals, and the same closure under it.
** IT PINS AS RESULTS: the deficits `-2.024528e-03` and `-6.970164e-03` at `0.30` eV and
`-7.544464e-03` and `-1.397832e-02` at `0.60`, against the response's own `1.641809e-02` and
`3.800102e-02`, so `0.1233` and `0.1985` of it; the species' Fermi-Dirac `w` at recombination,
`0.320474` and `0.290599`, against the `1/3` its own equations hard-code; the corrected moves
`-19.330577` and `-19.299451` against the recorded `-20.09`, so `0.0378` and `0.0394` of it removed;
and the closure under the switch at `1.110223e-16` and `2.220446e-16`. **
⛔ ** AND IT PINS WHAT WAS WRONG IN THIS LINE'S OWN FIRST RUN AND HOW IT WAS CAUGHT: ** the
correction arm's reproduction leg read the RE-PROFILED column where the headline is the FROZEN one
AND took the move with the opposite sign to the record's own table; both are pinned here as the
defect and as the reproduction that found it, `-20.086848` and `-48.201966` against `-20.09` and
`-48.20`.
⛔ ** NO LIMIT, NO ENVELOPE CROSSING AND NO REFITTED `A` IS PINNED HERE from the repaired
perturbations: this file pins the defect, the separation and the switch's own arms.  The validation
`A` is pinned by the revision that reads it. **

⌷ ** THE ID. **  `69` ordered this as `r7875`, which merged `r7874`, ruled the envelope a screen and
the shift-amplitude fit the verdict, and overruled this seat's recommendation not to build the
conditional switch -- on the physics, and not on the share table.

⚠ ** THREE THINGS IN THIS RECORD ARE THIS SEAT'S OWN, and the first is the two defects above. **

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
      and 'NOT RETYPED' in CLOSE_PY)

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
      'it separates them' in RESULT
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
      and 'NUSHOFF' in INST and '_NU_NR = 1.0 / 6.0' in INST
      and 'WHAT IT DOES NOT DO' in INST
      and 'bounded rather than hidden' in RESULT)

check('Ⓓ③ᵉ ⛭ and the weight is redefined WHERE IT IS BUILT and not at its use sites, so all SEVEN '
      'of them -- both right-hand sides and the four source paths -- take it together and cannot '
      'disagree',
      'On_of = CubicSpline(eg, Onu_of(ag) / _rt)' in INST
      and INST.count('On_of(') == 7
      and 'cannot disagree' in RESULT,
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
      and '`f` ≤ 0.30' in PRED or 'f ≤ 0.30' in PRED)

check('Ⓔ⓪ᵃᵃ ⛭ and it registered a REACHABLE NEGATIVE on the repair before the repair existed -- '
      'that if the deficit came out small against the response, the order\'s own alternative is the '
      'expected finding -- and the measured ratios cleared it rather than the clause being dropped',
      'the defect is elsewhere' in PRED
      and 'will not rescue' in PRED
      and all(abs(CL[t]['d_rec']) / CL[t]['r_rms'] > 0.10 for t in ('S030', 'S060')))

check('Ⓔ⓪ᵃᵇ ⛭ and the six reads taken before the registration are DECLARED in it, the first being '
      'that item ① IS a read of the code and so could not be taken after',
      'READS TAKEN BEFORE THIS REGISTRATION' in PRED
      and 'DECLARED' in PRED
      and 'No spectrum of this revision has been computed' in PRED)

print('=' * 100)
print('  %d arm(s), %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('   FAILED: %s' % f)
sys.exit(1 if FAILS else 0)
