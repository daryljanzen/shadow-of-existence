#!/usr/bin/env python3
"""r7858 (60), on order `r7855`: the bank's factor two is TWO definitions, each short in a different
place, and each established alone.

COMPUTES: the location of the factor two `r7856` measured in this instrument's banked CMB spectra,
to two named lines of its own construction; the independent establishment of each of the two missing
factors separately; the switch that supplies them at the source, with its inertness measured against
the unedited instrument; the swept list of absolute statements that a constant on that bank would
move, with each one's owning seat; and what the polarisation blocks are short of.  ** It pins NO
cosmological parameter as a result and reports NO limit: the ordered control run is BLOCKED on a
measured ground and is routed rather than run. **

⌷ ** THE ID. **  69 ordered this as `r7855`, which merged `r7856` and ruled this seat's fork ⒜ --
fix the bank at its source, not at the read point.  This revision's directory, its PREDICTION.md
(pushed before any computation existed) and this receipt carry `r7858`.

** THE LOCATION. **  ⒜ The hierarchy path accumulates `out[j] = np.sum(P * _tr ** 2)` with
`P = kb ** (NS - 1) / kb * dk`, carrying NO `4 pi` where the line-of-sight `C_l` carries one; and ⒝
the save line writes `Dl = Cl * ls * (ls + 1)` against the data's own `l(l+1) C_l / (2 pi)`, so it is
short of `1/(2 pi)`.  ** And `4 pi / (2 pi) = 2` exactly, which is the measured `0.504672`. **

** WHY EACH IS ESTABLISHED ALONE. **  A factor of two can be inserted in a dozen places and close a
ratio from any of them, so closing it is not evidence.  The `4 pi` is therefore put to the
reference's own `C_l` AT THE `C_l` LEVEL -- `out` recovered per multipole before any binning, so no
`D_l` convention appears on this side at all -- and comes to `1.002278` over 238 multipoles.  The
`1/(2 pi)` is then an identity on the save line.  *The first test has no `D_l` step left with which
to absorb a wrong `D_l` convention, which is what makes it independent.*

⛔ ** FOUR THINGS FAIL, ARE REFUTED, OR ARE WITHDRAWN, AND THREE OF THEM ARE THIS SEAT'S OWN. **
`Ⓐ①` fails its registered criterion unmoved (geometric mean 1.009345, worst bin 1.021113, against a
registered 0.01 across all bins).  This revision's FIRST version of the `4 pi` test was INVALID and
is kept rather than deleted -- it divided the binned `l(l+1) out` by the binned `l(l+1)` and returned
9.76e+04 spanning a factor 370, and a wrong constant cannot be k-dependent.  `Ⓒ③ᵇ`'s positive
control FAILED on its first run and caught a census that swept nothing.  And this seat's read of the
source, that the polarisation entries would be short of an `l`-DEPENDENT `2 l(l+1)`, is REFUTED by
its own measurement.

STATUS: OK
rc=0 on success.  Run: NODE=60 python3 <this file>   (numpy; seconds, reads banked json)
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RUN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7858_60_the_cmb_banks_factor_two_found_at_its_source')
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')


def rd(n):
    with io.open(os.path.join(RUN, n), encoding='utf-8') as fh:
        return json.load(fh)


INST = ' '.join(io.open(os.path.join(BTW, 'ACOUSTIC_two_arm.py'), encoding='utf-8').read().split())
L2, FP = rd('locate_two.json'), rd('four_pi.json')
SW, AB, PO = rd('switch.json'), rd('absolute_sweep.json'), rd('polarisation.json')

fail = []


def check(label, cond, detail=''):
    ok = bool(cond)
    print('  %s %s' % ('✔' if ok else '✘', label))
    if detail:
        print('      %s' % detail)
    if not ok:
        fail.append(label.split()[0])
    return ok


print()
print('=' * 100)

check('Ⓞ⓪ THE CONTROL: r7856\'s figure reproduces on this tree before anything is changed -- the '
      'bank\'s binned TT at the seed-derived normalisation is 0.504672 of the reference\'s, to a '
      'relative 1e-6.  ** Nothing below is a reading of a repair until this holds **',
      L2['O0']['holds'] is True and abs(L2['O0']['ratio'] - 0.504672) < 5e-6
      and L2['O0']['n_bins'] == 185,
      'ratio %.6f over %d bins' % (L2['O0']['ratio'], L2['O0']['n_bins']))

check('Ⓐ① THE FACTOR IS LOCATED TO TWO NAMED LINES OF THE INSTRUMENT\'S OWN CONSTRUCTION, each read '
      'off the source and not inferred: the accumulation `out[j] = np.sum(P * _tr ** 2)` carries no '
      '`4 pi`, and the save line `Dl = Cl * ls * (ls + 1)` carries no `1/(2 pi)`.  ** And '
      '4 pi / (2 pi) = 2 EXACTLY, which is the measured factor **',
      L2['lines']['accumulation'] is True and L2['lines']['measure'] is True
      and L2['lines']['save'] is True and abs(L2['lines']['net_factor'] - 2.0) < 1e-12
      and 'out[j] = np.sum(P * _tr ** 2) * _FP_ACC' in INST,
      'the three lines are present and the net is %.1f' % L2['lines']['net_factor'])

check('Ⓐ①ᵇ AND THE `4 pi` IS ESTABLISHED ALONE, AT THE `C_l` LEVEL, WITH NO `D_l` CONVENTION ON '
      'THIS SIDE: `out` is recovered per multipole BEFORE any binning, and `4 pi x AMP x T^2 x '
      'exp(-2 tau) x out` over the reference\'s own C_l gives 1.002278 across 238 multipoles from '
      'l=100 to 1996.  ** So it is not a number that closes a ratio: this test has no `D_l` step '
      'left with which to absorb a wrong one **',
      FP['four_pi']['holds'] is True
      and abs(FP['four_pi']['geometric_mean'] - 1.002278) < 5e-6
      and FP['four_pi']['n_multipoles'] == 238
      and abs(FP['two_pi']['net'] - 2.0) < 1e-12,
      'geometric mean %.6f over %d multipoles, range %.6f .. %.6f'
      % (FP['four_pi']['geometric_mean'], FP['four_pi']['n_multipoles'],
         FP['four_pi']['ratio_min'], FP['four_pi']['ratio_max']))

check('Ⓐ①ᵃ ⚠ AND THIS REVISION\'S FIRST VERSION OF THAT TEST WAS INVALID AND IS KEPT IN THE RECORD '
      'RATHER THAN DELETED: it recovered `out` by dividing the BINNED `l(l+1) out` by the BINNED '
      '`l(l+1)`, which the window\'s own width makes wrong, and returned a geometric mean of '
      '9.76e+04 spanning a factor 370.  ** A wrong CONSTANT cannot be k-dependent, so that spread '
      'is the signature of the test\'s error and not of the physics **',
      L2['A1b_4pi']['holds'] is False
      and L2['A1b_4pi']['ratio_max'] / max(L2['A1b_4pi']['ratio_min'], 1e-300) > 100.0,
      'the invalid version spans %.0f, the rebuilt one %.4f'
      % (L2['A1b_4pi']['ratio_max'] / max(L2['A1b_4pi']['ratio_min'], 1e-300),
         FP['four_pi']['ratio_max'] / FP['four_pi']['ratio_min']))

check('Ⓐ①ᶜ ⛔ AND `Ⓐ①`\'S OWN REGISTERED CRITERION FAILS, UNMOVED: it asked for within 0.01 of one '
      'across ALL 185 bins, and the repair gives a geometric mean of 1.009345 with the worst bin at '
      '1.021113.  *What is left is the instrument\'s own residual shape error, which r7856 measured '
      'independently and which no normalisation can remove*',
      L2['A1']['all_bins_within'] is False
      and L2['A1']['within_one_per_cent'] is True
      and abs(L2['A1']['mean'] - 1.009345) < 5e-6
      and abs(L2['A1']['ratio_max'] - 1.021113) < 5e-6,
      'mean %.6f, worst bin %.6f against a criterion of 0.01'
      % (L2['A1']['mean'], L2['A1']['ratio_max']))

check('Ⓑ② THE FIX IS AT THE SOURCE AND BEHIND A DEFAULT-OFF SWITCH, AND ITS INERTNESS IS MEASURED '
      'AGAINST THE UNEDITED INSTRUMENT RATHER THAN ASSERTED: origin/main\'s instrument and the '
      'edited one with `FOURPI` unset are BITWISE IDENTICAL on ls, Dl, Dl_EE and Dl_TE over 50 '
      'multipoles, and with it set the TT ratio is 2.000000000000 with a worst distance from two of '
      '8.882e-16 while the polarisation blocks are untouched',
      SW['holds'] is True and SW['off']['byte_identical'] is True
      and SW['off']['n_multipoles'] == 50
      and SW['on']['exactly_two'] is True
      and abs(SW['on']['tt_ratio_mean'] - 2.0) < 1e-12
      and SW['on']['ee_untouched'] is True and SW['on']['te_untouched'] is True
      and "os.environ.get('FOURPI', '0') == '1'" in INST,
      'byte-identical off over %d multipoles; on, TT x %.12f, worst |ratio-2| %.3e'
      % (SW['off']['n_multipoles'], SW['on']['tt_ratio_mean'],
         SW['on']['worst_distance_from_two']))

check('Ⓒ③ THE ABSOLUTE STATEMENTS ARE SWEPT AND NOT HAND-LISTED: 12 receipts make a statement a '
      'constant factor on that bank would move -- 3 this seat\'s, 6 cc66\'s and 3 whose first commit '
      'the owner read could not resolve -- beside 4 that score with a FREE amplitude only, which '
      'r7856 established is unaffected in value.  ** The sweep decides nothing about what it finds: '
      'each is reported with its owning seat for 69 to route **',
      AB['C3']['swept_not_hand_listed'] is True and AB['C3']['n_absolute'] == 12
      and AB['C3']['n_free_amplitude_only'] == 4
      and AB['by_owner'].get('cc66') == 6 and AB['by_owner'].get('60') == 3,
      '%d absolute (%s), %d free-amplitude only'
      % (AB['C3']['n_absolute'], AB['by_owner'], AB['C3']['n_free_amplitude_only']))

check('Ⓒ③ᵇ ⚠ AND THAT SWEEP\'S POSITIVE CONTROL FAILED ON ITS FIRST RUN, WHICH IS WHY IT EXISTS: it '
      'reported ZERO absolute statements with zero free-amplitude ones beside them, because `ROOT` '
      'was built with two `dirname` calls instead of three and the walk had nothing to walk.  ** A '
      'census with no positive control would have reported "nothing to route" and been believed -- '
      'the S55 defect on this line\'s own ledger, reproduced and caught the same day. **  It now '
      'asserts that receipts/ is under ROOT',
      AB['control']['holds'] is True and AB['control']['finds_r7856'] is True
      and AB['control']['finds_held_form'] is True
      and AB['control']['excludes_free_only'] is True,
      'the control finds r7856\'s own receipt and an amplitude-held form, and lists no '
      'free-amplitude-only file as absolute')

check('Ⓓ④ᵃ ⚠ AND THIS SEAT\'S READ OF THE SOURCE IS REFUTED BY ITS OWN MEASUREMENT: it predicted the '
      'polarisation entries would be short of an l-DEPENDENT `2 l(l+1)`, and so of a SHAPE error.  '
      'Read as a multiple of l(l+1) the EE factor spreads by 73, which refuses that outright; read '
      'as a CONSTANT all three blocks want about TWO -- TT 1.995455, EE 2.016473, TE 1.939872, '
      'agreeing with TT to 1.1 and 2.8 per cent.  ** The l(l+1) the save names imply is missing is '
      'evidently already carried **',
      PO['own_read_refuted'] is True
      and abs(PO['blocks'][0]['as_constant'] - 1.995455) < 5e-6
      and abs(PO['blocks'][1]['as_constant'] - 2.016473) < 5e-6
      and abs(PO['blocks'][2]['as_constant'] - 1.939872) < 5e-6
      and PO['blocks'][1]['spread_over_l_l_plus_1'] > 10.0,
      'TT %.6f, EE %.6f, TE %.6f as constants; EE over l(l+1) spreads by %.0f'
      % (PO['blocks'][0]['as_constant'], PO['blocks'][1]['as_constant'],
         PO['blocks'][2]['as_constant'], PO['blocks'][1]['spread_over_l_l_plus_1']))

check('Ⓓ④ ⛔ IS BLOCKED ON A MEASURED GROUND AND IS ROUTED RATHER THAN RUN, and the ground is the '
      'weaker one the measurement leaves and NOT the one this seat expected: EE\'s factor is '
      'established only to 18 per cent and TE\'s ratio is unusable where TE crosses zero, so the '
      'SAME constant is not established for all three blocks to the precision ONE SHARED AMPLITUDE '
      'needs.  ⇒ ** No chain is run and no limit is reported against the ordered 54.00 and 30.56 '
      'meV: ** turning the switch on now would score a spectrum whose three blocks this revision '
      'had just made inconsistent by a few per cent',
      PO['D4_blocked'] is True
      and PO['blocks'][1]['spread_as_constant'] > 0.10
      and 'shared amplitude' in PO['reason'],
      'EE spread %.4f, TE spread %.4f -- the ruling needed is whether the polarisation blocks take '
      'the same two factors as TT'
      % (PO['blocks'][1]['spread_as_constant'], PO['blocks'][2]['spread_as_constant']))

check('Ⓔ⑤ AND NOTHING IS CONCLUDED: no limit is computed, the defaults stay OFF as the order '
      'requires until the absolute statements are routed, P15 is untouched by this revision, the '
      'arm of record is NOT JUDGED and 72\'s batch waits',
      PO['D4_blocked'] is True
      and "os.environ.get('FOURPI', '0') == '1'" in INST
      and 'FOURPI' in INST,
      'the switch exists, defaults off, and no chain was run')

print()
print('=' * 100)
print()
if not fail:
    print('  ✔ r7858: the factor two is two definitions, each short in a different place.')
    print('    => `4 pi` missing from the accumulation and `1/(2 pi)` from the save line, and '
          '4 pi/(2 pi) = 2 exactly.')
    print('    => the `4 pi` established ALONE at the C_l level at %.6f over %d multipoles, so it '
          'is not a number that closes a ratio.'
          % (FP['four_pi']['geometric_mean'], FP['four_pi']['n_multipoles']))
    print('    => fixed at the source behind FOURPI: byte-identical off, exactly 2.000000000000 on.')
    print('    => 12 absolute statements swept with their owners, and the sweep\'s own positive '
          'control caught it sweeping nothing first.')
    print('    => Ⓐ① FAILED its bin criterion unmoved, this seat\'s source-read of the '
          'polarisation blocks is REFUTED, and Ⓓ④ is BLOCKED and routed.')
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
