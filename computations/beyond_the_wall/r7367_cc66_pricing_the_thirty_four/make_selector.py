#!/usr/bin/env python3
"""r7367+cc66 ③ -- WRITE THE COMMITTED SELECTOR: the named list of the `34`.

`r7367` ③: *"Commit the selector with the measurement, per your own `r7365` rule -- the named list of
`34` is a committed file, not a count in prose. That is the rule you wrote after finding the hop's
selector was nowhere in the tree, and this is its first use."*

⛭ SO THIS IS THE FIRST USE OF THE `r7365` ② STANDING RULE, APPLIED TO MY OWN WORK BEFORE THE
MEASUREMENT RATHER THAN AFTER IT.  The `34` are DERIVED, here, from two frozen inputs and nothing
else -- so the list is reproducible from the tree and not from this file's prose:

  ⒜ `new117.tsv` and `keep82.tsv` at `7db5db61c` -- the hand labels, frozen before `r7345` was
     written, giving `80` PIN of the `117`;
  ⒝ the `tier` column of `new117.tsv`, which is the extractor's own emitted field and IS the clause's
     trigger (`check_quote_pins`' `H4`: `'H4 a TOKEN is not a meaning pin'`).

⇒ `SENTENCE` and PIN gives the `34`.  The `23`/`11` split `r7367` ③ orders FIRST is by whether the
receipt already carries rows in the live `corpus/quote_pin_baseline.tsv` -- the files the ledger
already covers, where a minted key joins rows rather than opening a receipt.

    python3 -I make_selector.py <repo-root> > thirty_four.tsv
"""
import json, subprocess, sys

ROOT = sys.argv[1]
PRE = '7db5db61c'
BASE = 'computations/beyond_the_wall/r7343_cc66_the_container_read/'


def at(p):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{PRE}:{p}'],
                          capture_output=True, text=True, check=True).stdout


rows = [r for r in (ln.split('\t') for ln in at(BASE + 'new117.tsv').split('\n')) if len(r) > 3]
keep82 = {(q[0], json.loads(q[1])) for q in
          (ln.split('\t') for ln in at(BASE + 'keep82.tsv').split('\n') if '\t' in ln)}
RES = {'PO-',
       'receipts/P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source_before_the_branch'
       '_point_and_everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic_'
       'content_on_the_expansion_leg.py'}
residual = {k for k in keep82 if k[1] in RES}
assert len(residual) == 2, f'residual lits matched {len(residual)}, expected 2'

# the live ledger, keyed as the GATE keys it: the literal column is JSON.
# ⛔ r7365+cc66.38 ⒢ / r7367 ④: keying it as raw text reports 2628 stale on an exactly-green ledger.
led_receipts = set()
for ln in open(f'{ROOT}/corpus/quote_pin_baseline.tsv', encoding='utf-8').read().split('\n'):
    if '\t' in ln and not ln.startswith('#'):
        led_receipts.add(ln.split('\t')[0])

sel = []
for r in rows:
    k = (r[0], json.loads(r[1]))
    if k not in keep82 or k in residual:      # NON-PIN
        continue
    if r[3] != 'SENTENCE':                    # H4 refuses a TOKEN
        continue
    sel.append((r[0], r[1], r[2], r[3], 'COVERED' if r[0] in led_receipts else 'NO-ROW'))

assert len(sel) == 34, f'selector holds {len(sel)}, expected 34'
cov = sum(1 for s in sel if s[4] == 'COVERED')
assert cov == 23, f'{cov} in covered receipts, expected 23'

print('# THE 34 -- the reach of PO-78\'s second discharge clause into the 80 invisible pins.')
print('# r7367+cc66 ③.  DERIVED by make_selector.py from new117.tsv + keep82.tsv at 7db5db61c and')
print('# the tier column that IS check_quote_pins\' H4.  Not hand-typed: regenerate, never edit.')
print('# receipt <TAB> literal (JSON) <TAB> target <TAB> tier <TAB> ledger-coverage of the receipt')
print(f'# {len(sel)} keys: {cov} COVERED (r7367 ③ orders these first), {len(sel) - cov} NO-ROW.')
for s in sorted(sel):
    print('\t'.join(s))
