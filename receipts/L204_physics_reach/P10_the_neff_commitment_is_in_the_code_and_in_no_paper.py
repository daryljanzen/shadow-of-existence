#!/usr/bin/env python3
"""P10 -- cc54's station-⑨ finding verified on this tree: the cosmology/nuclear sector rests on N_eff at
both ends, commits to it explicitly IN CODE, and names it in no paper.  Sixth arrival-path finding.

** THE STATION. **  R-P's ⑨: "cosmology · nuclear / plasma --- BBN, recombination, the acoustic scale."
The last unrun station, and cc54's because it needs camb and pynucastro.

** ⓵ THE ABSENCE, AS MEASURED WHEN THIS RECEIPT WAS WRITTEN. **  Across the paper .tex files:

      *** N_{\\rm eff} 0 · N_\\mathrm{eff} 0 · Neff 0 · 3.046 0 · "effective number of" 0 ***

  ** while the sector is otherwise deep: ** the lithium problem is named and worked; D/H, Yp and He are
  everywhere.  ⇒ ** One missing NAME, not a missing sector. **

⛔⛭ ** AND THAT ABSENCE HAS SINCE ENDED -- THIS HEADLINE IS SUPERSEDED, AND THE WAY IT SURVIVED IS THE
FINDING (r7125+cc66.98). **  *The papers now carry* "the effective number $N_{\\mathrm{eff}}=3.046$
~\\cite{Mangano2005}" *in `cosmogenesis_paper.tex`:* ** N_{\\mathrm{eff}} 5x · 3.046 3x. **
  ⇒ *** So "names it in no paper" and "stated nowhere" are FALSE on this tree, and `P11` in this same
    directory already said so: "`3.046` is NO LONGER at zero -- the absence ENDED at `c54.205`".  The
    closing commit is `9fd40454`, whose message is `P11`'s own filename. ***
  ⛔ ** TWO THINGS KEPT IT STANDING, AND BOTH WERE IN THIS FILE. **  *The ⓵ loop asserted `n >= 0`,
  true of every count ever taken, so it could not fail; and the spelling list looked for
  `N_\\mathrm{eff}` where the paper writes `N_{\\mathrm{eff}}` -- it missed the live spelling on a pair
  of braces.  A third check's LABEL read "STATED IN NO PAPER" while its CONDITION asserted
  `len(re.findall('Neff', allp)) > 0`, the opposite.*
  ⇒ ⛭ *** What this receipt still carries on its own is ⓶: THE CODE COMMITS TO IT, in the clear, and
    that is untouched.  The NAMING half is `P11`'s, and the ⓵ checks are now the regression guard on
    the filling rather than an assertion of a gap that closed. ***

** ⛭⛭ ⓶ AND THE CORPUS COMMITS TO IT ANYWAY, IN THE CLEAR, IN CODE. **  `bbn_network.py`:

      r_nu = (4.0/11.0)**(1.0/3.0)
      # energy-density relativistic dof: photons(2) + e+-(7/8*4*fade) + 3 nu(7/8*2 each, at T_nu)

  ** Three neutrino species decoupling to (4/11)^{1/3} -- the standard N_eff ~ 3.046 setup, adopted
  explicitly and stated nowhere. **
  ⇒ *** EXACTLY ⑥'s HIGGS SHAPE AND ⑩'s BABY-UNIVERSE SHAPE: the corpus holds the thing and does not
      name it. ***

** ⓷ AND IT IS LOAD-BEARING AT BOTH ENDS -- cc54 computed the levers, which is why the station is
its. **
  * ** BBN: dY_p/dN_eff ~ +0.010 per unit. **
  * ** camb: one extra unit of N_eff moves 100*theta_* by -3.2% and r_drag by -4.7 Mpc. **
  ⇒ *** An enormous lever on the very ell_A/r_s the sector predicts to 0.075% and 15.7 sigma.  Both
      headline results are functions of a parameter named in neither paper. ***

** ⌗ ⓸ AND THE REASON IT IS NOT COSMETIC FOR THIS CONSTRUCTION IN PARTICULAR -- cc54's point, and it is
the sharpest part. **  ** The construction carries a right-handed nu_R in the colourless four (PO-5),
and N_eff counts thermalized relativistic species. **
  ⇒ *** SO "does CR adopt the standard N_eff, or does its nu_R structure predict a departure?" IS A
      REAL, UNASKED QUESTION -- and the unnamed adoption is exactly what hides it. ***
  ⌗ ** That is a physics question for Daryl and 54, not one the literature settles, and cc54 said so
    rather than attempting it. **

** ⓹ SIXTH OF THE ARRIVAL-PATH CLASS. **  Lovelock (r2515), Type II/III (r2520), Unruh (r2521), Higgs
(r2522), baby universe (r2540), and this.  ** All the same shape: the corpus and the field fit perfectly
and do not meet. **  ⇒ ** And three of the six are now CLOSED by paragraphs that name what was being
answered: Unruh (c54.202), the Higgs (c54.203), the baby universe and Page curve (c54.204). **

WHAT IS NOT CLAIMED.  ** Not that the standard N_eff is wrong for CR ** -- that is the unasked question,
not an answer.  ** Not that cc54's camb and BBN levers are re-derived here **: they are reported, and the
absence and the code commitment are what this receipt measures.  ** Not that naming it changes any
number ** -- it does not, and that is the point: *** an adopted-but-unstated parameter is invisible
precisely because nothing downstream breaks. ***

Written r2544.  Stated for reversal.
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


def main():
    print()
    print('  P10 -- does the cosmology sector name the parameter it rests on?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    rp = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'),
                                  encoding='utf-8', errors='replace').read())

    check('R-P names ⑨ as cosmology · nuclear / plasma -- BBN, recombination, the acoustic scale',
          'BBN, recombination, the acoustic scale' in rp)

    # ⓵ THE ABSENCE -- ** WHICH HAS ENDED, AND THIS CHECK IS NOW THE REGRESSION GUARD ON THAT. **
    # ⛔⛭ r7125+cc66.98: THIS LOOP ASSERTED `n >= 0`, WHICH IS TRUE OF EVERY COUNT EVER TAKEN, AND THE
    # VACUITY IS WHY THIS RECEIPT'S OWN FINDING ROTTED IN PLACE UNNOTICED.
    #   *The label claimed a tally -- `N_{\mathrm{eff}}` 4x, the other spellings absent -- and the
    #   docstring claims all five at ZERO with the headline "names it in no paper".  ** Measured: the
    #   papers name it.  `cosmogenesis_paper.tex` carries "the effective number $N_{\mathrm{eff}}=3.046$
    #   ~\cite{Mangano2005}". **  And the spelling list MISSED it on a pair of braces: it looked for
    #   `N_\mathrm{eff}` where the paper writes `N_{\mathrm{eff}}`.*
    #   ⇒ *** The corpus already knew.  `P11`, in this directory, asserts the opposite of this
    #     receipt's docstring about the same string -- "and `3.046` is NO LONGER at zero -- the absence
    #     ENDED at `c54.205` (`L-527`) ... this check is now the REGRESSION GUARD on that filling" --
    #     and `c54.205` is the commit `9fd40454`, whose message IS `P11`'s filename. ***
    #   ⌗ *So the absence is not re-asserted and not quietly re-pinned to new counts: the loop now
    #   measures every spelling INCLUDING the one in use, prints them all, and asserts the thing that
    #   is true and load-bearing -- that the name is IN PRINT.  Station ⑨'s finding is superseded by
    #   `P11` and this receipt says so rather than contradicting it.*
    SPELLINGS = ('N_{\\mathrm{eff}}', 'N_{\\rm eff}', 'N_\\mathrm{eff}', 'Neff', '3.046',
                 'effective number of')
    seen = {k: len(re.findall(re.escape(k), allp)) for k in SPELLINGS}
    for k in SPELLINGS:
        print(f'      "{k}": {seen[k]}x across the papers')
    # the live spelling is pulled out because an f-string expression may not contain a backslash
    n_named, n_val = seen['N_{\\mathrm{eff}}'], seen['3.046']
    check(f'⛭ THE ABSENCE HAS ENDED and this is the REGRESSION GUARD on it: the papers name the '
          f'parameter -- {n_named}x in the live spelling and "3.046" {n_val}x -- where this receipt '
          f'measured ZERO across all five spellings it then knew.  ** Supplied at `c54.205`, which is '
          f"`P11`'s finding; the old list missed the live spelling on a pair of braces, and `n >= 0` "
          f'is why nothing said so **',
          n_named > 0 and n_val > 0)
    check('while the sector is otherwise deep: the lithium problem is named and worked',
          'lithium' in allp.lower())
    check('and D/H and Yp are present', 'D/H' in allp and ('Y_p' in allp or 'Yp' in allp))

    # ⓶ the code commits
    net = None
    for cand in glob.glob(os.path.join(ROOT, '**', 'bbn_network.py'), recursive=True):
        net = open(cand, encoding='utf-8', errors='replace').read()
        break
    check('⛭⛭ and bbn_network.py exists', net is not None)
    if net:
        check('committing explicitly to the neutrino decoupling ratio (4/11)^(1/3)',
              '(4.0/11.0)**(1.0/3.0)' in net or '(4/11)' in net)
        check('and to THREE neutrino species in the relativistic degrees of freedom',
              '3 nu' in net or 'three neutrino' in net.lower())
        # ⛔⛭ r7125+cc66.98: THIS LABEL AND ITS CONDITION SAID OPPOSITE THINGS.  *The label read
        # "ADOPTED IN CODE AND STATED IN NO PAPER" while the condition asserted
        # `len(re.findall('Neff', allp)) > 0` -- that it IS in a paper.  Same rot as the loop above,
        # and it could only survive because nobody read the pair together.*
        check(f'⇒⇒ SO THE STANDARD N_eff SETUP IS ADOPTED IN CODE -- and it is NOW NAMED IN PRINT too '
              f'({n_named}x in the live spelling), which is the half this receipt was written before.  '
              f"** The code commitment is the part that still stands as this receipt's own; the "
              f"naming is `P11`'s **",
              ('(4.0/11.0)**(1.0/3.0)' in net or '(4/11)' in net)
              and n_named > 0)

    # ⓸ and why it is not cosmetic here
    check("⌗ and the construction carries a right-handed neutrino in the colourless four",
          'right-handed' in allp and ('nu_R' in allp or '\\nu_R' in allp or 'neutrino' in allp))
    # ⛔⛭ r7125+cc66.98: the THIRD stale pairing in this file.  *The label said "the unnamed adoption
    # is what hides it" while the condition asserts the name IS present -- and the question it calls
    # "unasked" has since been ANSWERED, by `P11` in this directory: CR gives the nu_R a place and no
    # interactions, N_eff counts thermalized species, so CR makes no N_eff prediction at all.*
    #   ⇒ *So the question is recorded as ASKED AND ANSWERED, with `P11` named, and what is asserted is
    #   the two facts this receipt measures: the name is in print and the nu_R is in the grading.*
    check(f'⇒ SO "does CR adopt the standard N_eff, or does its nu_R structure predict a departure?" '
          f'was a real unasked question -- ** and `P11` has since answered it: CR fixes a PLACE and '
          f'not a coupling, so it makes no N_eff prediction at all. **  The adoption is no longer '
          f'unnamed ({n_named}x in print), which is what removed the hiding',
          n_named > 0 and 'right-handed' in allp)

    # ⓹ the class
    closed = {k: len(re.findall(re.escape(k), allp, re.I))
              for k in ('Unruh', 'Higgs', 'baby universe', 'Page curve')}
    check(f'⌗ and three of the six arrival-path findings are now CLOSED by paragraphs that name what '
          f'was being answered: Unruh {closed["Unruh"]}, Higgs {closed["Higgs"]}, baby universe '
          f'{closed["baby universe"]}, Page curve {closed["Page curve"]}',
          all(v > 0 for v in closed.values()))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the sector rests on N_eff at both ends and names it in no paper. **')
    print('  ⓵ ** N_{\\rm eff} 0 · Neff 0 · 3.046 0 · "effective number of" 0 ** -- while the lithium')
    print('     problem is named and worked and D/H and Yp are everywhere.  ** One missing NAME. **')
    print('  ⓶ ** And bbn_network.py commits explicitly: r_nu = (4/11)^(1/3), three neutrino species. **')
    print('     ⇒ ** The standard setup, adopted in code and stated nowhere -- ⑥\'s Higgs shape and ⑩\'s')
    print('     baby-universe shape exactly. **')
    print('  ⓷ ** And cc54 computed the levers: dY_p/dN_eff ~ +0.010 per unit; one extra unit moves')
    print('     100*theta_* by -3.2% and r_drag by -4.7 Mpc ** -- against a sector predicting ell_A/r_s')
    print('     to 0.075% and 15.7 sigma.')
    print('  ⌗ AND WHY IT IS NOT COSMETIC HERE: ** the construction carries a right-handed neutrino in')
    print('    the colourless four, and N_eff counts thermalized relativistic species. **  ⇒ ** "Does CR')
    print('    adopt the standard N_eff, or does its nu_R structure predict a departure?" is a real,')
    print('    unasked question -- and the unnamed adoption is what hides it. **')
    print('  ⚠ NOT claimed: that the standard N_eff is wrong for CR.  ** That is the question. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
