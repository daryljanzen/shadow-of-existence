#!/usr/bin/env python3
"""C17 -- `PO-12`'s two "missing" pieces are BUILT and validated: the visibility function and the
line-of-sight projection are `sec:instrument`'s Boltzmann transfer, and r2658's audit was wrong about
both.

** WHAT r2658 CONCLUDED, one revision ago. **  Six of the transfer's eight pieces computed, with two
marked ** "⛔ NOT located" **: the visibility function, and the $k\\to\\ell$ projection.

** ⛔ ⓵ BOTH ARE BUILT, AND THE PAPER HAS A SECTION ABOUT IT. **  `sec:instrument`: "The low-multipole
prediction above and the ratio statements below are carried by ** a Boltzmann transfer built for this
programme **, and its standing should be stated plainly rather than assumed.  It is a full photon
hierarchy with polarisation, second-order tight coupling, massless neutrinos, and ** a Peebles
recombination history **; ** the line-of-sight source carries the monopole with the potential, the Doppler
term, the integrated Sachs--Wolfe term, and the quadrupole with its own projection kernel
$(j_\\ell+3j_\\ell'')$ **."

  ⇒ ** The Peebles history IS the visibility function.  The line-of-sight source with $j_\\ell$ IS the
    $k\\to\\ell$ projection. **  *** r2658 searched the papers for the ingredients by name and missed the
    section that names them together. ***

** ⓶ AND IT IS VALIDATED, NUMBER BY NUMBER. **  Against "an independent Boltzmann code run at identical
parameters, unlensed and with reionisation off", it reproduces:

      *** acoustic peak and trough positions   to 0.5% across P1-P4
          the ionisation history x_e(z) and its derivative   to +/-1% THROUGH THE VISIBILITY PEAK
          matter-radiation equality              to 0.02%
          the transfer function                  to better than 1% for k < 0.02/Mpc ***

  ⌗ ** And it carries its own receipts: ** `verify_lowell_exact_measure.py`, `verify_closedS3_nonsync.py`.

** ⛭⛭ ⓷ SO WHAT IS `PO-12`'s DEBT, GIVEN THAT? **  The paper calls this "** the full FLAT-projection
transfer **" -- *** and the debt names the other thing: "specifying how the fluctuations gravitate on the
RADIATION-FREE background ... and then a bespoke transfer against that specification." ***

  ⇒⇒ *** The instrument is a full standard hierarchy; the bespoke transfer would be that instrument run
      on the geometric stacking background.  And the corpus states exactly what would differ: "in the ratio
      the Thomson physics and the ionisation history cancel identically and ** the whole difference is
      carried by $H(a)$ **." ***
  ⌗ ** That is a much smaller debt than "a genuine build": ** *** the machinery exists, is validated, and
    the CR-specific change is confined to one function. ***

WHAT IS NOT CLAIMED.  ** Not that swapping $H(a)$ is the whole of it ** -- *** the cancellation quoted is
established for the DIFFUSION-LENGTH ratio (r2647), and whether it extends to every source term in the
hierarchy is not shown here and is the natural next question. ***  ** Not that the instrument already
runs geometric stacking ** -- the paper calls it flat-projection and the debt stands.  ** Not that r2658's
other six findings are affected ** -- they are verified independently and stand.

Written r2659.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  C17 -- are PO-12's two missing pieces really missing?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the instrument exists
    check('⛔ ⓵ the transfer exists: "carried by a Boltzmann transfer built for this programme, and its '
          'standing should be stated plainly rather than assumed"',
          'carried by a Boltzmann transfer built for this programme' in p15)
    check('with the VISIBILITY piece: "a full photon hierarchy with polarisation, second-order tight '
          'coupling, massless neutrinos, and a Peebles recombination history"',
          'and a Peebles recombination history' in p15)
    check('and the PROJECTION piece: "the line-of-sight source carries the monopole with the potential, '
          'the Doppler term, the integrated Sachs--Wolfe term, and the quadrupole with its own '
          'projection kernel"',
          'the line-of-sight source carries the monopole with the potential' in p15
          and 'its own projection kernel' in p15)

    # ⓶ validated
    check('⓶ and it is validated against "an independent Boltzmann code run at identical parameters, '
          'unlensed and with reionisation off"',
          'an independent Boltzmann code run at identical parameters' in p15)
    check('reproducing the ionisation history "and its derivative to $\\pm1\\%$ through the visibility '
          'peak"',
          'through the visibility peak' in p15)
    check('and peak positions "to $\\le0.5\\%$ across $P_1$--$P_4$"',
          'trough positions to $\\le0.5\\%$' in p15 and 'across $P_1$--$P_4$' in p15)

    # ⓷ what remains
    check('⛭⛭ ⓷ and the paper calls it flat-projection: "The full flat-projection transfer confirms the '
          'estimate and sharpens it into a prediction"',
          'The full flat-projection transfer confirms the estimate' in p15)
    check("while the debt names the other background: \"specifying how the fluctuations gravitate on the "
          'geometric stacking background\"',
          'specifying how the fluctuations gravitate on the geometric stacking background' in p15)
    check('and the corpus states what would differ: "the whole difference is carried by $H(a)$"',
          'the whole difference is carried by $H(a)$' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** both of r2658's \"missing\" pieces are BUILT and validated. **")
    print('  ⛔ ⓵ ** sec:instrument is a Boltzmann transfer built for this programme: ** a full photon')
    print('     hierarchy with polarisation, second-order tight coupling, massless neutrinos, and ** a')
    print('     Peebles recombination history ** (the visibility function); with ** a line-of-sight source')
    print('     carrying monopole, Doppler, ISW and the quadrupole\'s own kernel ** (the k -> l')
    print('     projection).')
    print('     ⇒ ** r2658 searched for the ingredients BY NAME and missed the section that names them')
    print('       together. **')
    print('  ⓶ ** And it is validated number by number: ** peaks to 0.5%, x_e and its derivative to ±1%')
    print('     ** through the visibility peak **, equality to 0.02%, transfer to <1% below k=0.02/Mpc.')
    print('  ⛭⛭ ⓷ ** So PO-12\'s debt is what the instrument RUNS ON. **  The paper calls this "the full')
    print('     ** flat-projection ** transfer"; the debt names "the ** geometric stacking ** background".')
    print('     ⇒⇒ *** The machinery exists and is validated, and the corpus says exactly what would')
    print('       differ: "the whole difference is carried by H(a)".  That is far smaller than "a genuine')
    print('       build". ***')
    print('  ⚠ NOT claimed: that swapping H(a) is the whole of it.  ** The cancellation quoted is')
    print('    established for the DIFFUSION-LENGTH ratio; whether it extends to every source term in the')
    print('    hierarchy is the natural next question. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
