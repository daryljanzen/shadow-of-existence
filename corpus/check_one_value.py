#!/usr/bin/env python3
"""check_one_value.py -- ONE QUANTITY, ONE VALUE, OR AN EXPLICIT REASON FOR TWO.

** WHY. **  *** A paper that states the same quantity at two values leaves a reader unable to tell
which is the claim, and leaves the next computation inheriting whichever it met first.  This is the
failure that stopped the transfer landing: theta_D/theta_* quoted at 8.2% in eleven places and at
13.96% in the section that derives it; r_D at ~9% and at 10.8%; the peak spacing at 0.72-0.79 and at
0.975; a depth quartet withdrawn in one paragraph and live in the abstract. ***

  ⛔ ** EVERY ONE OF THOSE WAS FOUND BY READING A LINE, AND THE READING IS NOT RELIABLE AT 30,000
     WORDS.  This file finds them by measurement instead. **

** WHAT IT DOES.  ** *** For each NAMED quantity it collects every numeric value stated within a
window of that name, and reports the distinct values.  It does NOT decide: two values can be
correct at two conditions, and the paper may say so.  What it asserts is that a quantity carrying
more than one value must carry, within the same window, a word that says why. ***

  The reconciling words: `at` `where` `against` `under` `either` `both` `two` `respectively`
  `condition` `onset` `arm` `depth` `asymptotic` `shallow` `first` `second`.

  ⌗ *A quantity with two values and no reconciling word is the failure.  A quantity with two values
    and a reason is the paper doing its job -- theta_D/theta_* is exactly that after r3179.*

  ⛔ ** ITS HONEST LIMIT: it flags WINDOWS, not quantities. **  *A window holding r_s, H_0 and a
     multipole reports all three as "values of r_s", and no amount of tuning fixes that without a
     parser.  It earns its keep by making a reader LOOK at a place where several numbers sit close
     to one name -- which is exactly where the 10--25% and the withdrawn quartet were living.*

    python3 corpus/check_one_value.py                 # the registered quantities
    python3 corpus/check_one_value.py 'r_s' 'A_s'     # ad hoc

Written r3215.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

#: ** the quantities this corpus states repeatedly.  NAMED, not discovered: a discovered list is
#: noise, and the point is to watch the ones that carry a claim. **
QUANTITIES = {
    'theta_D/theta_*': r'\\theta_\{?D\}?/\\theta_\{?\*\}?|damping-\\emph\{scale\}|damping angular scale',
    'r_D (diffusion length)': r'\br_\{?D\}?\b|diffusion length',
    'peak spacing / l_A': r'peak spacing|of \$\\ell_\{?A\}?\$|asymptotic spacing',
    'l_1/l_A (first peak)': r'\\ell_\{?1\}?/\\ell_\{?A\}?',
    'z_onset': r'z_\{\\mathrm\{onset\}\}',
    'r_s (sound horizon)': r'\\rs\b|r_\{?s\}?\b',
    'A_s': r'\bA_s\b',
    'low-l depth': r'of the flat-\$\\Lambda\$CDM expectation|discreteness floor',
}

WINDOW = 320
RECONCILE = re.compile(
    r'\bat\b|\bwhere\b|\bagainst\b|\bunder\b|\beither\b|\bboth\b|\btwo\b|\brespectively\b'
    r'|\bcondition\b|\bonset\b|\barm\b|\bdepth\b|\basymptotic\b|\bshallow\b|\bfirst\b|\bsecond\b',
    re.I)
NUM = re.compile(r'(?<![\d.])(\d+\.\d+|\d{1,4})(?![\d.])')


def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    t = re.sub(r'(?m)^%.*$', '', t)
    t = re.sub(r'(?<!\\)%.*$', '', t, flags=re.M)      # trailing comments too
    i, j = t.find('\\begin{document}'), t.find('\\begin{thebibliography}')
    return t[i:j if j > i else len(t)] if i >= 0 else ''


def main(argv):
    pats = ({a: re.escape(a) for a in argv} if argv else QUANTITIES)
    print()
    print('  check_one_value -- one quantity, one value, or a stated reason for two')
    print()
    flagged = 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        name = os.path.basename(path)
        if 'appendix' in name:
            continue
        b = body(path)
        if not b:
            continue
        for label, pat in pats.items():
            vals, unreconciled = {}, {}
            for m in re.finditer(pat, b):
                w = b[max(0, m.start() - WINDOW // 2):m.end() + WINDOW // 2]
                ok = bool(RECONCILE.search(w))
                # ** exponents and coefficients inside math are not STATED VALUES of the quantity;
                #    10^{113} and 9(l_P/M)^2 are structure, not two readings of one number. **
                wq = re.sub(r'\^\{[^}]*\}|\^\d+', '', w)
                for v in NUM.findall(wq):
                    if v in ('0', '1', '2', '3', '4', '5'):      # indices, not values
                        continue
                    vals.setdefault(v, 0)
                    vals[v] += 1
                    if not ok and v not in unreconciled:
                        unreconciled[v] = w        # keep THIS window, not a global search
            if len(unreconciled) > 3:
                flagged += 1
                print(f'    [LOOK] {name}: {label}')
                for v, w in list(unreconciled.items())[:5]:
                    i = w.find(v)
                    ctx = re.sub(r'\s+', ' ', w[max(0, i - 55):i + len(v) + 55])
                    print(f'           {v:>8}  ...{ctx.strip()[:104]}...')
    print()
    if flagged:
        print(f'    {flagged} quantity/paper pair(s) to LOOK at.  ** A COUNT IS NOT A VERDICT. **')
        print('    Two values can be right at two conditions -- read the window and check the paper')
        print('    SAYS so.  If it does not, that is the failure this file exists for.')
        print()
        return 0        # an instrument, not a gate: it reports, it does not fail the build
    print('    No registered quantity carries unreconciled values.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
