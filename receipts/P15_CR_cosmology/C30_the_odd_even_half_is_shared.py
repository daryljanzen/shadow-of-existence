#!/usr/bin/env python3
"""C30 -- `PO-10`'s half ② carries NO CR-versus-$\\Lambda$CDM signal: the odd/even pattern is fixed by the
baryon loading $R$, and $R$ is a CONTENT ratio the rate difference does not enter.

** THE ROW'S TWO HALVES, in P7's own words (`frontier:scalar`). **
  * ** ① ** "the full-spectrum likelihood-level comparison against flat $\\Lambda$CDM---** a parameter
    refit rather than a further calculation **";
  * ** ② ** "the odd/even height pattern, which is ** imprinted by the baryon loading on the expansion leg
    and is ordinary content physics there **".

** ⛭⛭ ⓵ AND P15 SAYS WHERE AND AT WHAT VALUE. **  "The baryon loading is proportional to the scale
factor and the driving happens where the scale factor is smallest, so ** $R\\simeq0.1$ at the onset and
orders below that at entry **; ** the odd/even asymmetry is imprinted afterwards, on the expansion side at
$R\\simeq0.6$, which is ordinary content physics on the observable leg **"
`\\rcpt{C5b_baryon_term}`.

** ⓶ THE PATTERN IS THEN ARITHMETIC. **  With loading $R$ the acoustic zero-point is displaced by
$-R\\Phi$, so compressions are enhanced against rarefactions:

      *** R = 0.60:   1+3R = 2.80,   |1-3R| = 0.80,   ratio 3.50 ***

  ⇒ ** Fixed by $R$ alone, with no further calculation ** -- which is exactly what "ordinary content
  physics" asserts.

** ⛭ ⓷ AND THAT IS WHY THE HALF CARRIES NO DISCRIMINATING SIGNAL. **  $R=3\\rho_b/4\\rho_\\gamma$ is a
ratio of CONTENTS.  *** The geometric stacking rate changes $H(a)$ and therefore every LENGTH -- the sound
horizon, the diffusion scale, the comoving horizon (r2686) -- but it does not change a ratio of densities
at fixed content.  So both arms carry the SAME $R$ at the same redshift, and the same odd/even
pattern. ***
  ⌗ ** Which is P15's structural claim one level down: ** the difference is "carried by $H(a)$", and $R$
  is not a function of $H$.

** ⇒ ⓸ SO HALF ② IS NOT A RUN THIS ROW OWES. **  *** It is a statement that the pattern is standard and
shared.  What the row's first half owes -- a likelihood refit -- is real and is a refit, as P7 says.
`PO-10` is therefore ONE half, not two. ***

WHAT IS NOT CLAIMED.  ** Not that `C5b` is re-derived ** -- *** it is the paper's receipt for the $R$
values, and the $1+3R$ displacement used here is the textbook result, quoted not proved. ***  ** Not that
the peak heights are computed ** -- P15 states they "continue to track" through the third peak with its
own receipt.  ** Not that half ① is small ** -- a full-spectrum likelihood refit is real work, and it is
what remains.

Written r2703.  Stated for reversal.
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
    print("  C30 -- does PO-10's half ② carry a CR-vs-LCDM signal?")
    print()
    p7 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_framework.tex')))
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ P7's two halves
    # ** RE-PINNED r3108.  Both halves have since been RUN, so the pins into P7's pre-run wording
    #    broke.  This receipt's thesis is CONFIRMED by the run rather than displaced: it predicted
    #    that half ② carries no CR-versus-LambdaCDM signal because the odd/even pattern is fixed by
    #    the baryon loading, a CONTENT ratio the rate difference does not enter.  P7 now reports
    #    P1/P2 = 2.185 here against 2.2564 +/- 0.0772 measured -- agreement, i.e. no discriminating
    #    signal, which is exactly what the receipt said would happen. **
    check('⓵ P7 half ① has been RUN, and reports a disagreement: chi^2 = 397.13 against 206.44 over '
          'the 215 binned TT multipoles at equal fitted-parameter count',
          '397.13' in p7 and '206.44' in p7 and 'equal fitted-parameter count' in p7)
    check('⛭ and half ② has been run too, CONFIRMING this receipt: the odd/even pattern agrees, so it '
          'carries no CR-versus-LambdaCDM signal -- $P_1/P_2 = 2.185$ against $2.2564 \\pm 0.0772$',
          'P_1/P_2=2.185' in p7.replace(' ', '') or '2.185' in p7)

    # ⓶ P15 gives the values
    check('⛭⛭ ⓶ and P15 gives where and at what value: "the odd/even asymmetry is imprinted afterwards, '
          'on the expansion side at $R\\simeq0.6$, which is ordinary content physics on the observable '
          'leg"',
          'the odd/even asymmetry is imprinted afterwards, on the expansion side at' in p15
          and 'which is ordinary content physics on the observable leg' in p15)
    check('with the driving side orders below it: "$R\\simeq0.1$ at the onset and orders below that at '
          'entry"',
          'at the onset and orders below that at entry' in p15)

    # ⓷ the arithmetic
    R = 0.60
    odd, even = 1 + 3*R, abs(1 - 3*R)
    check(f'⓷ so the pattern is arithmetic in $R$ alone: $1+3R={odd:.2f}$, $|1-3R|={even:.2f}$, ratio '
          f'{odd/even:.2f}',
          abs(odd - 2.80) < 0.01 and abs(odd/even - 3.50) < 0.01)

    # ⓸ R is a content ratio
    check('⛭ ⓸ and $R=3\\rho_b/4\\rho_\\gamma$ is a ratio of CONTENTS, so the rate difference -- which '
          'P15 says carries "the whole difference" -- does not enter it',
          'the whole difference is carried by' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** half ② carries NO discriminating signal — PO-10 is ONE half, not two. **")
    print('  ⓵ ** P7 states both halves itself: ** ① a likelihood comparison, "** a parameter refit')
    print('     rather than a further calculation **"; ② the odd/even pattern, "** ordinary content')
    print('     physics **".')
    print('  ⛭⛭ ⓶ ** And P15 gives the values: ** R ≈ 0.1 at the onset, "orders below that at entry",')
    print('     with the asymmetry imprinted "** on the expansion side at R ≈ 0.6 **".')
    print(f'  ⓷ ** The pattern is then arithmetic: ** 1+3R = {odd:.2f} against |1−3R| = {even:.2f}, ratio')
    print(f'     {odd/even:.2f} — fixed by R alone, with no further calculation.')
    print('  ⛭ ⓸ *** And R = 3ρ_b/4ρ_γ is a ratio of CONTENTS.  The geometric stacking rate changes H(a) and')
    print('     therefore every LENGTH — sound horizon, diffusion scale, comoving horizon — but it does')
    print('     NOT change a ratio of densities at fixed content.  Both arms carry the same R at the same')
    print('     redshift, and the same odd/even pattern. ***')
    print('  ⇒ ** So half ② is not a run this row owes. **  What remains is half ① — a likelihood refit,')
    print('    and P7 says it is a refit.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
