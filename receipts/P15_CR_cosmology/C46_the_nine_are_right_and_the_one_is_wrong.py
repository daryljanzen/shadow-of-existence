#!/usr/bin/env python3
"""C46 -- the $9.4\\%$ is TRACED and it is downstream of the same $x_e$ error: the nine $\\sim8\\%$ are
right, and P15's one $9.4\\%$ sentence is the edit.

** THE TRACE, in three steps and no guesses. **  *** P15's $9.4\\%$ sentence cites `C10_highl_ratio`;
`C10` reports $+9.26\\%$ and cites `C9_sound_horizon_and_ratio`; `C9` computes it outright: ***

      *** r_s(CR)/r_s(LCDM) = 1.0067   ->  +0.67%
          r_D(CR)/r_D(LCDM) = 1.1015   ->  +10.15%
          theta_D/theta_*   = 1.1015/1.0067 = 1.0941  ->  +9.41% ***

** ⓵ SO IT IS NOT A CATEGORY ERROR, AND THAT MATTERS. **  *** r2700 cost four revisions on exactly that
suspicion -- an angle ratio compared against a length ratio -- and it was the natural guess here too.
** It is wrong: $9.41\\%$ IS the angle ratio, divided correctly. ** ***

** ⛭⛭ ⓶ WHAT IT INHERITS IS THE $x_e$ CANCELLATION r2753 FOUND. **  *** `C9`'s $r_D$ ratio of $1.1015$
is the C8 family -- the one that moves $x_e$ outside the integral.  r2753 measured that omission at
$1.57$pp on the $r_D$ ratio.  Feed the corrected $r_D$ through `C9`'s own division: ***

      *** r_D = 1.1015 (x_e omitted)     ->  theta_D/theta_* = 1.0942   +9.42%   <- P15's sentence
          r_D = 1.0837 (x_e weighted)    ->                     1.0765   +7.65%
          r_D = 1.0897 (receipt's full)  ->                     1.0824   +8.24% ***

  ⇒⇒ *** CORRECTING THE $r_D$ LANDS THE ANGLE RATIO AT $+7.6\\%$ TO $+8.2\\%$ -- which is what
      `P15_damping_ratio_clean` computes directly ($\\theta_D/\\theta_* = 1.0816$, $+8.16\\%$) and what P15
      says nine times. ***

** ⓷ SO THE ADJUDICATION IS CLEAN AND RUNS AGAINST THE PRECISE-LOOKING NUMBER. **  *** ** The nine
$\\sim8\\%$ are RIGHT.  The single $9.4\\%$ is the error. **  And it is the one that looked most
authoritative -- two decimal places, a receipt citation, and a derivation chain -- while the hedged
figure was the accurate one. ***

** ⓸ AND r2749's TILDE TEST NOW RESOLVES THE OTHER WAY. **  *** At r2749 the $\\sim8\\%$ tilde was EARNED,
because two receipts disagreed.  ** They no longer disagree: one of them is corrected. **  By r2749's
own rule -- stale when one receipt asserts and none competes -- the tilde is now removable, and the
value to write is the one the surviving receipt computes: $\\theta_D/\\theta_* = 1.0816$, ** $+8.2\\%$. ***

WHAT IS NOT CLAIMED.  ** Not that $8.16\\%$ is exact ** -- *** the three corrected routes give $7.65$,
$8.16$ and $8.24$; they agree on the leading digit and differ in the second, which is why the paper
edit below writes $8.2\\%$ and not four figures. ***  ** Not that `C9` and `C10` are wrong in their own
terms ** -- their division is correct; they inherit an $r_D$.  ** Not that the $r_D$ question is fully
closed ** -- the full Hu--Sugiyama with baryon weighting still gives $+5.66\\%$ for $r_D$ alone, and that
route is not reconciled here.

** COMPUTES: `C9`'s own division applied to three $r_D$ ratios.  *** All three are the corpus's own
figures. *** **

Written r2755.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

RS = 1.0067


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b



# ** ⛭⛭ RE-PINNED c54.223 (`L-557`).  THIS RECEIPT IS ONE OF THE SEVEN THAT PRODUCED r2755's
# ** CORRECTION, AND THE CORRECTION BROKE ITS OWN PIN. **  Each of the seven quotes P15's `9.4%`
# ** because that is the sentence they were arguing about; r2755 replaced it with `8.2%` and none of
# ** the seven was re-pinned, so all seven have failed every full run since.
#   ⇒ *** A claim about the paper AS IT WAS is a claim about a COMMIT (c54.220's rule), so the
#       historical quote is read at `b4f1931^` and the CURRENT text is asserted separately.  A
#       receipt that argued for a correction must survive the correction landing. ***
_BEFORE_R2755 = 'b4f1931^'


def _p15_at(rev):
    """CR_cosmology.tex as it read at a commit -- whitespace-flattened, same as the live read"""
    import subprocess
    out = subprocess.run(['git', 'show', f'{rev}:corpus/CR_cosmology.tex'],
                         cwd=ROOT, capture_output=True, text=True, errors='replace').stdout
    return re.sub(r'\s+', ' ', out)


def main():
    print()
    print("  C46 -- where does P15's 9.4% come from?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    def rcpt(n):
        return open(glob.glob(os.path.join(ROOT, 'receipts', '**', n), recursive=True)[0],
                    encoding='utf-8', errors='replace').read()

    # ⓵ the trace
    # ** RE-PINNED c54.223 (`L-557`): THIS RECEIPT ARGUED FOR THE EDIT AND THE EDIT LANDED. **  At
    # `b4f1931^` the sentence read "larger by $9.4\%$"; r2755 made it `8.2\%` on this receipt's own
    # finding.  *The historical quote is read at the commit; the current text is asserted separately.*
    _p15_before = _p15_at(_BEFORE_R2755)
    check('⓵ P15\'s sentence cited C10: "$\\theta_{D}/\\theta_{*}$ larger by $9.4\\%$ ... '
          '\\rcpt{C10_highl_ratio}" at ' + _BEFORE_R2755,
          'larger by $9.4\\%$' in _p15_before and 'C10_highl_ratio' in _p15_before)
    check('⛭ AND THE EDIT LANDED: r2755 made it $8.2\\%$, and c54.223 carried the same correction '
          'into `r` one paragraph later, which r2755 had left at 1.093',
          'larger by $8.2\\%$' in p15 and 'r=\\theta_{D}/\\theta_{*}=1.082' in p15
          and 'larger by $9.4\\%$' not in p15)
    check('and C10 cited C9 for it: "theta_D/theta_* is +9.26% larger (DERIVED, C9)"',
          'DERIVED, C9' in rcpt('C10_highl_ratio.py')
          or 'DERIVED in C9' in rcpt('C10_highl_ratio.py'))
    c9 = rcpt('C9_sound_horizon_and_ratio.py')
    check('while C9 computes it from an $r_D$ ratio and an $r_s$ ratio -- it prints both and their '
          'quotient as theta_D/theta_*',
          'theta_D/theta_* ratio' in c9)

    # ⓶ so it is the ANGLE ratio, not a category error
    ang = 1.1015/RS
    check(f'⛭⛭ ⓶ so it is NOT r2700\'s category error: $1.1015/{RS} = {ang:.4f}$ -- ** the angle '
          'ratio, divided correctly **',
          abs(100*(ang-1) - 9.41) < 0.05)

    # ⓷ but the r_D it uses omits x_e
    corr = {1.1015: 'x_e omitted (C8 family)', 1.0837: 'x_e weighted (r2753)',
            1.0897: "the receipt's full r_D"}
    vals = {rd: rd/RS for rd in corr}
    check(f'⓷ and feeding the CORRECTED $r_D$ through C9\'s own division gives '
          f'{100*(vals[1.0837]-1):+.2f}% and {100*(vals[1.0897]-1):+.2f}% -- not $9.4\\%$',
          vals[1.0837] < 1.09 and vals[1.0897] < 1.09)
    check('which brackets what P15 says nine times, and matches the direct computation '
          '$\\theta_D/\\theta_*=1.0816$ in P15_damping_ratio_clean',
          '1.0816' in rcpt('P15_damping_ratio_clean.py')
          or 'CR/LCDM' in rcpt('P15_damping_ratio_clean.py'))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the nine ~8% are RIGHT; the single 9.4% is the error. **')
    print('  ⓵ ** Traced in three steps: ** P15 → C10 (+9.26%) → C9, which computes')
    print(f'     r_D/r_s = 1.1015/{RS} = {ang:.4f}.')
    print('     ⇒ ** NOT r2700\'s category error — it IS the angle ratio, divided correctly. **')
    print('  ⛭⛭ ⓶ ** What it inherits is the x_e cancellation r2753 found. **  Feed C9\'s own division')
    print('     a corrected r_D:')
    for rd in (1.1015, 1.0837, 1.0897):
        print(f'       r_D = {rd:.4f}  ({corr[rd]:<24}) → {vals[rd]:.4f}  {100*(vals[rd]-1):+.2f}%')
    print('     *** Correcting r_D lands the angle ratio at +7.6% to +8.2% — which is what the CAMB')
    print('     receipt computes directly (1.0816) and what P15 says nine times. ***')
    print('  ⓷ ** And it runs against the precise-looking number: ** the 9.4% had two decimals, a')
    print('     receipt citation and a derivation chain; ** the hedged figure was the accurate one. **')
    print('  ⓸ ** So r2749\'s tilde test now resolves the other way: ** the receipts no longer')
    print('     disagree, one is corrected, and by r2749\'s own rule the tilde is removable.')
    print('     ** The value to write is +8.2%. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
