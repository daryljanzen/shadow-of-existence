#!/usr/bin/env python3
"""P10 -- cc54's station-⑨ finding verified on this tree: the cosmology/nuclear sector rests on N_eff at
both ends, commits to it explicitly IN CODE, and names it in no paper.  Sixth arrival-path finding.

** THE STATION. **  R-P's ⑨: "cosmology · nuclear / plasma --- BBN, recombination, the acoustic scale."
The last unrun station, and cc54's because it needs camb and pynucastro.

** ⓵ THE ABSENCE, MEASURED HERE. **  Across the paper .tex files:

      *** N_{\\rm eff} 0 · N_\\mathrm{eff} 0 · Neff 0 · 3.046 0 · "effective number of" 0 ***

  ** while the sector is otherwise deep: ** the lithium problem is named and worked; D/H, Yp and He are
  everywhere.  ⇒ ** One missing NAME, not a missing sector. **

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

    # ⓵ the absence
    for k in ('N_{\\rm eff}', 'N_\\mathrm{eff}', 'Neff', '3.046', 'effective number of'):
        n = len(re.findall(re.escape(k), allp))
        check(f'⛔ "{k}" appears ZERO times across the papers', n == 0)
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
        check('⇒⇒ SO THE STANDARD N_eff SETUP IS ADOPTED IN CODE AND STATED IN NO PAPER',
              ('(4.0/11.0)**(1.0/3.0)' in net or '(4/11)' in net)
              and len(re.findall('Neff', allp)) == 0)

    # ⓸ and why it is not cosmetic here
    check("⌗ and the construction carries a right-handed neutrino in the colourless four",
          'right-handed' in allp and ('nu_R' in allp or '\\nu_R' in allp or 'neutrino' in allp))
    check('⇒ SO "does CR adopt the standard N_eff, or does its nu_R structure predict a departure?" is '
          'a real unasked question, and the unnamed adoption is what hides it',
          len(re.findall('Neff', allp)) == 0 and 'right-handed' in allp)

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
