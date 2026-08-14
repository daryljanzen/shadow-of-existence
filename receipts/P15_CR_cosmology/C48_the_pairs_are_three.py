#!/usr/bin/env python3
"""C48 -- `PO-10`'s pairs are THREE, not four: the onset ratio is an identity on inherited inputs, and
C39 took the generous read on the one entry it had just discovered.

** THE OWED ITEM, from r2748. **  *** "Check the OTHER THREE pairs against the receipts that assert
them, as r2748 did for $\\theta_*$ -- the prose value and the asserted value differed by a factor of
2.7 on the first one."  Done, and the check changes the LIST rather than the numbers. ***

** ⛭⛭ ⓵ TWO OF THE THREE HAVE ASSERTING RECEIPTS, AND THE VALUES HOLD. **

      *** r_s      C9_sound_horizon_and_ratio   assert abs(rs_LC - 145.38) < 0.05
          1+z_eq   P15_desi_dr2_confrontation   assert abs((1+zo)/3402 - 2.0) < 0.05 ***

  ⇒ ** Both are asserted, both match P15's prose. **  *** Unlike $\\theta_*$, where the prose carried
    an explicitly approximate value and the receipt the precise one, these two agree. ***

** ⛔⛭⛭ ⓶ AND THE THIRD IS NOT A DERIVED QUANTITY AT ALL. **  `P15_the_two_data_are_one`, on the onset
ratio: on any thermal history $\\rho_r/\\rho_m(T)$ is fixed by $\\eta$ and $\\omega_m/\\omega_b$, "** which
returns $1.99$ at $T=1.6$eV --- the quoted value to one per cent, ** *** from standard thermodynamics
and NO FEATURE OF THIS CONSTRUCTION *** **."

  ⇒⇒ *** It is an IDENTITY ON INHERITED INPUTS.  Given $\\eta$ and the measured matter-to-baryon ratio,
      both inherited for the composition regardless, ** the ratio at onset IS the onset **.  Same class
      as $N_{\\rm eff}$ and $A_s$, which C39 correctly excluded -- ** and the receipt says so in the
      sentence C39 quoted from. ** ***

** ⓷ SO C39 MADE THE ERROR C39 WARNED AGAINST. **  *** Its own closing line: "getting that list generous
is how a derived-quantity score turns back into a fit."  ** It then took the generous read on the one
entry it had just discovered ** -- the entry it was pleased to have found by searching marker phrases
rather than expected quantities.  *** The search method was right and the verdict on its find was
not. ***

  ⚠ ** And the near-miss: ** *** `P15_two_arm_control_and_guard` carries `CR 1.9968` and
  `LambdaCDM 2.0005` -- ** the SOURCE COMB landing on integers, a different quantity with the same
  digits **.  Matching on $1.99$ alone would have found an asserting receipt that asserts something
  else. ***

** ⓸ SO THE COMPARISON IS THREE PAIRS. **  *** $\\theta_*$ ($302.2$ against $301.76$), $r_s$ ($146.4$
against $145.38$), $1+z_{\\rm eq}$ ($3399$ against $3402$), plus the high-$\\ell$ ratio as a SHAPE test.
** What remains owed on this row is one thing: the published uncertainties for three measured
values. ** ***

WHAT IS NOT CLAIMED.  ** Not that the onset ratio is wrong ** -- *** it agrees to one per cent; what is
denied is that agreeing is a TEST of this construction, since no feature of it enters. ***  ** Not that
the three are scored ** -- no $\\sigma$, per r2746.  ** Not that C9 and the DESI receipt are audited ** --
they are read for what they assert.

** COMPUTES: nothing.  *** A search for asserting receipts across the corpus and a read of three. *** **

Written r2758.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def rcpt(n):
    return open(glob.glob(os.path.join(ROOT, 'receipts', '**', n), recursive=True)[0],
                encoding='utf-8', errors='replace').read()


def main():
    print()
    print("  C48 -- do PO-10's other three pairs hold against their asserting receipts?")
    print()

    # ⓵ two have asserting receipts
    check('⛭⛭ ⓵ $r_s$: C9 asserts the measured value -- "assert abs(rs_LC - 145.38) < 0.05"',
          re.search(r'assert\s+abs\(rs_LC\s*-\s*145\.38\)', rcpt('C9_sound_horizon_and_ratio.py'))
          is not None)
    check('and $1+z_{\\rm eq}$: the DESI receipt asserts it -- '
          '"assert abs((1+zo)/3402 - 2.0) < 0.05"',
          re.search(r'assert\s+abs\(\(1\+zo\)/3402', rcpt('P15_desi_dr2_confrontation.py'))
          is not None)

    # ⓶ the third is not derived
    two = rcpt('P15_the_two_data_are_one.py')
    check('⛔⛭⛭ ⓶ while the onset ratio is NOT a derived quantity: it "returns 1.99 at $T=1.6$eV -- '
          'the quoted value to one per cent, from standard thermodynamics and no feature of this '
          'construction"',
          'the quoted value to one per cent, from standard' in two)
    check('and the same receipt says why: "Given $\\eta$ and the measured matter-to-baryon ratio, '
          'both inherited for the composition regardless, the ratio at onset IS the onset"',
          'ratio at onset IS the' in two)

    # ⓷ C39 warned against exactly this
    # ** and C39's own framing was that the list's SIZE is the thing at risk: it says the size
    # question is "decided by reading rather than by choosing" -- which is exactly the step
    # this receipt had to redo, because C39 read the marker and not the receipt behind it. **
    check('⓷ while C39 itself framed the risk: the exclusion list "decides the comparison\'s '
          'size, and it is decided by reading rather than by choosing"',
          "decides the comparison's size, and it is decided by reading rather than by"
          in rcpt('C39_the_derived_list_read.py'))

    # ⚠ the near-miss
    guard = rcpt('P15_two_arm_control_and_guard.py')
    check('⚠ and the near-miss: P15_two_arm_control_and_guard carries "CR 1.9968" and '
          '"LambdaCDM 2.0005" -- the SOURCE COMB landing on integers, a different quantity with the '
          'same digits',
          '1.9968' in guard and 'lands on the integers' in guard)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** three pairs, not four — the onset ratio is an identity on inherited inputs. **")
    print('  ⛭⛭ ⓵ ** Two hold against asserting receipts: ** r_s (C9, 145.38) and 1+z_eq (the DESI')
    print('     receipt, 3402).  ** Unlike θ_*, both agree with P15\'s prose. **')
    print('  ⛔ ⓶ ** The third is not derived at all: ** the onset ratio "returns 1.99 … from standard')
    print('     thermodynamics and NO FEATURE OF THIS CONSTRUCTION".')
    print('     ⇒ *** Given η and the matter-to-baryon ratio, both inherited, THE RATIO AT ONSET IS')
    print('     THE ONSET.  Same class as N_eff and A_s, which C39 correctly excluded — and the')
    print('     receipt says so in the sentence C39 quoted from. ***')
    print('  ⓷ ** So C39 made the error C39 warned against: ** "getting it wrong in the generous')
    print('     direction is how a derived-quantity score turns back into a fit."  ** It took the')
    print('     generous read on the one entry it was pleased to have found. **')
    print('  ⚠ ** Near-miss worth keeping: ** another receipt carries 1.9968 and 2.0005 — the SOURCE')
    print('    COMB on integers, a different quantity with the same digits.  ** Matching on the number')
    print('    alone would have found an asserting receipt that asserts something else. **')
    print('  ⓸ ** The comparison is THREE pairs plus the high-ℓ shape test, and one item remains')
    print('     owed: the published uncertainties for three measured values. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
