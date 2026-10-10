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

** r6931+70.1 (PO-59) -- HALF ② IS RUN AND THE PREDICTION IS SCORED. **  *** P15 now reports this arm's
$P_1/P_2=2.264$ on the polarisation path (r6772+66.16, `b5b6ac97`), against the sky's $2.2564\\pm0.0772$
and flat $\\Lambda$CDM's $2.200$: the arms sit inside one sky sigma of each other, so half ② carries no
discriminating signal at the sky's resolution, as ⓷-⓸ predicted -- with the paper's scope that heights
are the polarisation path's. ***  Half ① is run too (r6799/r6833: 1.57x the control at matched freedom),
so "`PO-10` is ONE half" is the r2703 accounting; both halves are delivered.
"""
import os
import re
import subprocess

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
    # ⛔⛭⛭ AMENDED r4518, AND THE TWO HALVES FAILED FOR DIFFERENT REASONS.
    #    ⓵ IS A MOVE, NOT A LOSS: r4111 restated P15's acoustic section (539 lines to 73) and
    #      carried the same correction into P7's frontier item, so the refit figures now live in
    #      P15 and P7 no longer repeats them.  *A receipt that pins a number to a FILE is asserting
    #      where the corpus keeps it; the claim is that the corpus states it.*  Asserted against
    #      P15, with the move named.
    #    ⛔ ⓵ᵇ IS A RETRACTION, AND IT GOES AGAINST THIS RECEIPT.  The note above records "P7 now
    #      reports P1/P2 = 2.185 here against 2.2564 +/- 0.0772 measured -- agreement, i.e. no
    #      discriminating signal, which is exactly what the receipt said would happen."  ** 2.185 is
    #      gone from the corpus, and P15 now says what this construction returns for that quantity
    #      "waits on the transfer of \S\ref{sec:refit-bound}, since a peak height is exactly what an
    #      unconverged transfer gets wrong". **  ⇒ *** So half ② has NOT been run on this arm, and
    #      the confirmation this receipt claimed is withdrawn.  The PREDICTION stands unchanged --
    #      the odd/even pattern is fixed by the baryon loading, a content ratio the rate difference
    #      does not enter -- and it is now what it always was: a prediction, waiting on the
    #      transfer, not a confirmed agreement. ***
    # ** r6931+70.1 (PO-59): CLASS (c), RE-MEASURED WITH PROVENANCE.  The 215-bin, five-parameter figures
    #    ($397.13$ against $206.44$) were the fitted-onset arm's; `754e76db` (r6772+66.36, "the stale
    #    refit figures out of P15") removed them when the arm moved to the branch-point handover, the
    #    refit was re-run on that arm and landed at `2007dc1e` (r6799), and was carried to the full
    #    lensed range at `62c8ae58` (r6833).  *** What the check carries is unchanged -- half ① is RUN,
    #    at matched freedom, and reports a DISAGREEMENT -- and the numbers are now: expansion rate,
    #    matter and baryon densities and tilt free in each arm, amplitude in closed form; control
    #    $1.01$ per bin, this arm $1.58$, "the arm at $1.57$ times the control's distance". ***  The
    #    old figures are read where they stood (`754e76db^`). **
    _then = re.sub(r'\s+', ' ', subprocess.run(
        ['git', 'show', '754e76db^:corpus/CR_cosmology.tex'], cwd=ROOT,
        capture_output=True, text=True, errors='replace').stdout)
    check('⓵ half ① has been RUN and reports a disagreement -- at matched freedom ("the tilt free in each '
          'arm and the amplitude in closed form"), control $1.01$ per bin against this arm\'s $1.58$, '
          '"the arm at $1.57$ times the control\'s distance"; the r3005-r6772 figures ($397.13$ against '
          '$206.44$, 215 bins) read at `754e76db^`',
          'the tilt free in each arm and the amplitude in closed form' in p15
          and 'control settles at $1.01$ in $\\chi^{2}$ per bin and this arm at $1.58$' in p15
          and "\\emph{the arm at $1.57$ times the control's distance" in p15
          and '397.13' in _then and '206.44' in _then and '397.13' not in p15)
    # ** r6931+70.1 (PO-59): CLASS (b), DISCHARGED.  "waits on the transfer" went at `440623b6` (r6719,
    #    "the transfer is run"), and the number it waited for landed at `b5b6ac97` (r6772+66.16): "what
    #    this construction returns for the same quantity is $2.264$ on the polarisation path, on the
    #    transfer of sec:refit-bound with its wavenumber integral converged".  *** So half ② HAS been run
    #    on this arm, and the prediction the r4518 note held as a prediction is now scored: $2.264$
    #    against the sky's $2.2564\\pm0.0772$ and flat LCDM's $2.200$ -- the two arms $0.064$ apart,
    #    inside ONE sky standard deviation, i.e. no discriminating signal at the sky's resolution,
    #    which is what this receipt predicted. ***  ⚠ Stated with the paper's own scope: heights are
    #    the polarisation path's ("every height quoted here is the polarisation path's"), the fluid
    #    path returning $2.448$; the check pins that scope too, so the confirmation carries it. **
    check('⛔ ⓵ᵇ [discharged r6719/r6772+66.16] HALF ② HAS NOW BEEN RUN ON THIS ARM: "$2.264$ on the '
          'polarisation path" against the sky\'s $P_1/P_2=2.2564\\pm0.0772$ and flat $\\Lambda$CDM\'s '
          '$2.200$ -- the arms $0.064$ apart, inside one sky sigma, so the prediction below is CONFIRMED '
          'at the sky\'s resolution, with the paper\'s scope: "every height quoted here is the '
          'polarisation path\'s"',
          'waits on the transfer' not in p15
          and 'is $P_1/P_2=2.2564\\pm0.0772$, and flat $\\Lambda$CDM\'s is $2.200$' in p15
          and 'what this construction returns for the same quantity is $2.264$ on the polarisation '
              'path' in p15
          and "so every height quoted here is the polarisation path's and is stated as such" in p15
          and abs(2.264 - 2.200) < 0.0772 and abs(2.264 - 2.2564) < 0.0772
          and '2.185' not in p15 + p7)

    # ⓶ P15 gives the values
    check('⛭⛭ ⓶ and P15 gives where and at what value: "the odd/even asymmetry is imprinted afterwards, '
          'on the expansion side at $R\\simeq0.6$, which is ordinary content physics on the observable '
          'leg"',
          'the odd/even asymmetry is imprinted afterwards, on the expansion side at' in p15
          and 's imprinted afterwards, on the expansion side at $R\\approx0.6$, which is ordinary content physics on the observable leg' in p15)
    # ** r6931+70.1 (PO-59): CLASS (c), STALE.  `de97f96e` (r6772+66.11, "the last of the fitted-onset
    #    reading cleared from P15's prose") rewrote "$R\\simeq0.1$ at the onset" as "$R\\lesssim0.1$ where
    #    the driving happens" -- same bound, same "orders below that at entry"; only the retired onset's
    #    name left the clause. **
    check('with the driving side orders below it: "$R\\lesssim0.1$ where the driving happens and orders '
          'below that at entry"',
          '$R\\lesssim0.1$ where the driving happens and orders below that at entry' in p15)

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
    print("  VERDICT (r6931+70.1): ** half ② is RUN on this arm -- P1/P2 = 2.264 (polarisation path) against")
    print("     the sky's 2.2564 ± 0.0772 and LCDM's 2.200, inside one sky sigma: the prediction below is")
    print("     confirmed at the sky's resolution.  Half ① is run too (1.57x at matched freedom). **")
    print("  ** half ② carries NO discriminating signal — PO-10 is ONE half, not two. **")
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
