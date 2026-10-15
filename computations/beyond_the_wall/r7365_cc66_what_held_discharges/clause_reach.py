#!/usr/bin/env python3
"""r7365+cc66 ③ -- MEASURE the reach of `PO-78`'s second discharge clause into the `80` invisible pins.

`r7365` ③: *"Say what would discharge the clause for those `80`.  What the row needs is the statement
of what 'held' means for a pin the instrument cannot key."*

⛭ THE CLAUSE IS NOT MINE TO PARAPHRASE AND IT IS ALREADY MECHANISED.  `PO-78`'s second clause reads
*"every pin whose claim is a sentence's MEANING rather than its wording rewritten to what it is for,
by its author"*, and `check_quote_pins`' `MEANING-HELD` verdict (`r7251+70.2`, adopted `r7253`) is
that clause with five conditions on it -- `H1` a resolving sha, `H2` an ancestor of HEAD, `H3` the
literal present in what the key reads there, **`H4` the tier is `SENTENCE` and not `TOKEN`**, `H5` a
commit that changed the receipt.  ⇒ *So the clause's trigger is not a judgement I supply: `H4` IS the
tier field, and the tier of all `117` is frozen in `new117.tsv` at `7db5db61c`.*

WHAT THIS MEASURES, and every figure is a count and not a reading:

  ⒜ the `80` split by the clause's own trigger -- `H4`'s `SENTENCE` against its `TOKEN`;
  ⒝ whether the frozen tier is still what the instrument says, re-derived through the hop's FOLLOW
     on the merged trunk, so the split is the instrument's and not the frozen file's;
  ⒞ the live ledger's saturation -- what a `MEANING-HELD` row for one of the `80` would do to it.

    python3 -I clause_reach.py <scratch-dir-with-patched-extractor-copy> <repo-root>
"""
import importlib.util, json, subprocess, sys

S, ROOT = sys.argv[1], sys.argv[2]
PRE = '7db5db61c'
BASE = 'computations/beyond_the_wall/r7343_cc66_the_container_read/'
LEDGER = 'corpus/quote_pin_baseline.tsv'


def at(p):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{PRE}:{p}'],
                          capture_output=True, text=True, check=True).stdout


# ---- the frozen population and its frozen labels, exactly as r7355's relimit.py reads them -------
rows = [r for r in (ln.split('\t') for ln in at(BASE + 'new117.tsv').split('\n')) if len(r) > 3]
all117 = [(r[0], json.loads(r[1])) for r in rows]
tier = {(r[0], json.loads(r[1])): r[3] for r in rows}
target = {(r[0], json.loads(r[1])): r[2] for r in rows}
keep82 = {(q[0], json.loads(q[1])) for q in
          (ln.split('\t') for ln in at(BASE + 'keep82.tsv').split('\n') if '\t' in ln)}
RES = {'PO-',
       'receipts/P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source_before_the_branch'
       '_point_and_everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic_'
       'content_on_the_expansion_leg.py'}
residual = {k for k in keep82 if k[1] in RES}
assert len(residual) == 2, f'residual lits matched {len(residual)}, expected 2'
PIN = [k for k in all117 if k in keep82 and k not in residual]
assert len(PIN) == 80, f'{len(PIN)} genuine pins, expected 80'

# ---- the live ledger, keyed the way the gate keys it: the literal column is JSON ------------------
# ⛔ r7365+cc66: keying it as RAW TEXT reports 2628 stale and 2628 new on a ledger that is exactly
#    saturated.  The gate does `json.loads` and so must any measurement over it.
led = set()
for ln in open(f'{ROOT}/{LEDGER}', encoding='utf-8').read().split('\n'):
    if '\t' not in ln or ln.startswith('#'):
        continue
    c = ln.split('\t')
    try:
        led.add((c[0], json.loads(c[1])))
    except ValueError:
        pass

# ---- the instrument, through the hop's FOLLOW, on the tree as it stands --------------------------
spec = importlib.util.spec_from_file_location('m', S + '/mutate_assertions.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
hop = {(r['receipt'], r['lit']): r.get('tier') for r in m.quote(ROOT)}

spec2 = importlib.util.spec_from_file_location('u', ROOT + '/scripts/mutate_assertions.py')
u = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(u)
live = {(r['receipt'], r['lit']) for r in u.quote(ROOT)}

# ---- ⒜ the clause's reach, by its own trigger ----------------------------------------------------
sent = [k for k in PIN if tier[k] == 'SENTENCE']
tok = [k for k in PIN if tier[k] == 'TOKEN']
print(f'the 80 invisible genuine pins, split by H4 -- the clause\'s own trigger:')
for nm, pop in (('SENTENCE  (H4 admits)', sent), ('TOKEN     (H4 refuses)', tok)):
    byt = {t: sum(1 for k in pop if target[k] == t) for t in ('PAPER', 'SOURCE', 'UNDECIDED')}
    print(f'  {nm}: {len(pop):3d}   ' + '  '.join(f'{t}={byt[t]}' for t in byt if byt[t]))

# ---- ⒝ is the frozen tier still the instrument's? -------------------------------------------------
surf = [k for k in all117 if k in hop]
agree = [k for k in surf if hop[k] == tier[k]]
print()
print(f'frozen tier re-derived through the hop FOLLOW on this tree:')
print(f'  of 117 frozen keys the follow surfaces : {len(surf):3d}   <-- 117 or the follow is not faithful')
print(f'  tier agrees with the frozen label      : {len(agree):3d}   <-- the split is the instrument\'s, not the file\'s')
for k in surf:
    if hop[k] != tier[k]:
        print(f'    [TIER MOVED] frozen={tier[k]} now={hop[k]} {k[0].split("/")[-1][:44]} | {k[1][:40]!r}')

# ---- ⒞ what a MEANING-HELD row would do to the ledger --------------------------------------------
print()
print(f'the live ledger as the gate reads it:')
print(f'  live keys                              : {len(live)}')
print(f'  baseline rows                          : {len(led)}')
print(f'  baseline rows NOT live  (STALE fails)  : {len(led - live):3d}')
print(f'  live keys with no row   (NEW-KEY fails): {len(live - led):3d}')
print(f'  of the 80, minted by the extractor     : {len(set(PIN) & live):3d}')
print(f'  of the 80, carrying a baseline row     : {len(set(PIN) & led):3d}')
print()
print(f'  ⇒ a MEANING-HELD row for any of the 80 takes STALE from {len(led - live)} to '
      f'{len(led - live) + 1} and the gate is red on it.')
