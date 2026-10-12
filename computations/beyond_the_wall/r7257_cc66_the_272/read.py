#!/usr/bin/env python3
"""`r7257` order ① and ②: join the reading in `forms.py` to the gathered rows and SCORE IT against the
pre-registration, with every witness class resolved against the tree.

** THE WITNESS RESOLUTION IS THE PART THAT CAN COST ME THE HEADLINE. **  `PREDICTION.md` keeps
`COMPUTABLE-NOWHERE` -- computable in principle, no corpus code computing the quantity -- OUT of the
headline share.  So a computable row is only computable if a module exists that computes its class of
quantity NOW.  Every class below is resolved by content over the tree; an empty class is a hard failure
and would move its rows to `NOWHERE`.  Nothing in `forms.py` is taken on my word.

Order ② is answered MECHANICALLY from the holder's own columns, by the rule pinned in advance:
  an AST form needs a file read and `ast.parse`, so it is carryable unless the holder opens no source
  file at all -- a JURISDICTIONAL miss, not a technical one;
  an INDEPENDENT COMPUTATION needs the quantity, so it is carryable only where the holder already
  computes that class of quantity, or reads an instrument artefact it can lift the number from.
"""
import collections
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
from forms import T                                                     # noqa: E402

# ─────────────────────────── the witness classes, resolved by content ───────────────────────────
WITNESS = {
    'GRP':      r'inv_dim|monodrom|holonom|chi_VVV|chi_meson|Weyl group|root[- ]exchange',
    'ZM':       r'zero[-_ ]?mode|equivariant|chiral zero|bound mode',
    'KILLING':  r'\bKilling\b|\blie_g\b|isometry algebra|isometry group',
    'GEOMALG':  r'\bRicci\b|\bRiemann\b|def Ric|def Gam|Christoffel',
    # ⌗ r7257+cc66.7 -- BEAD and ENTROPY were first written with `collapse' and `dimensionless' in
    #   them, which matched 77 and 25 modules and would have let a loose word stand as a witness for a
    #   computation.  ** A witness class resolved by a word that appears in prose is not a witness. **
    #   Tightened to the names the computations actually carry; both still resolve, at 18 and 16.
    'BEAD':     r'bead_|tortoise|tau_of_r|hyperboloid',
    'COSMO':    r'Hleaf|Hphys|rs_from|ell_A|eta_switch|stacking rate',
    'SPECTRUM': r'def spectrum|los_spectrum|P_T_of|transmission|harmonic',
    'ENTROPY':  r'\bentropy\b|\bhbar\b|ell_P',
    'REG':      r'PROTECTED_OPEN|open_items|undelivered',
}


def resolve_witnesses():
    """class -> the modules that compute it, by content over the corpus's own code."""
    out = {}
    for cls, rx in WITNESS.items():
        if cls == 'REG':
            hits = [p for p in ('PROTECTED_OPEN.md', 'THE_PHYSICS_REACH.md')
                    if os.path.exists(os.path.join(ROOT, p))]
        else:
            r = subprocess.run(['grep', '-rlE', rx, 'computations/', '--include=*.py'],
                               cwd=ROOT, capture_output=True, text=True)
            hits = [l for l in r.stdout.splitlines() if l.strip()]
        out[cls] = hits
    return out


# ───────────────────────────────── order ②: can the holder carry it ─────────────────────────────────
NUMERIC = {'NUM', 'SYMPY', 'SOLVE', 'FRAC'}
EXACT = {'NUM', 'SYMPY', 'FRAC', 'SOLVE'}
HEAVY = {'SYMPY', 'SOLVE'}


def carry(form, qclass, caps, reads):
    c, r = set(caps.split('+')) - {'-'}, set(reads.split('+')) - {'-'}
    lift = 'D:computations' in r and (r & {'PY', 'NPZ', 'PKL', 'TSV'})
    if form in ('AST-SIG', 'AST-PLACE'):
        if 'PY' in r:
            return 'Y', 'holder already opens a source file, so the AST is inside what it reads'
        return 'N', 'JURISDICTIONAL: the holder opens no source file -- it reads only prose'
    if form == 'INDEP':
        if qclass == 'REG':
            return ('Y', 'holder already opens the register the count runs over') if (r & {'MD', 'TSV'}) \
                else ('N', 'holder does not open the register')
        if qclass == 'COSMO':
            if 'SOLVE' in c:
                return 'Y', 'holder already runs a solver of this sector'
            if lift:
                return 'Y', 'holder already reads an instrument artefact carrying the number'
            return 'N', 'holder runs no solver and reads no instrument artefact: it would have to grow one'
        if qclass == 'GEOM':
            if c & HEAVY:
                return 'Y', 'holder already computes symbolically or integrates numerically'
            if lift:
                return 'Y', 'holder already reads an instrument artefact carrying the number'
            return 'N', 'holder computes no geometry: no symbolic algebra, no quadrature, no artefact read'
        if qclass == 'ALG':
            if c & EXACT:
                return 'Y', 'holder already computes exactly (numeric or symbolic)'
            if lift:
                return 'Y', 'holder already reads an instrument artefact carrying the number'
            return 'N', 'holder computes nothing: no numeric or symbolic import and no artefact read'
    return '-', '-'


def carry_capability(form, qclass, caps, reads):
    """THE SECOND READING OF ORDER ②, and I report both rather than choosing quietly.

    ⛭ r7257+cc66.6 -- the rule above bars an AST form from a holder that opens no source file, which is
      a JURISDICTIONAL bar: the receipt reads prose and the form needs code.  But the order's own words
      are `a form that needs a QUANTITY THE RECEIPT DOES NOT COMPUTE is not available to it', and an AST
      form needs no quantity at all -- it needs `open` and `ast.parse`, which every receipt in this
      corpus can already do.  ** Adding a file read is not growing a solver. **  So the capability
      reading says every AST form is carryable and only the computed quantities bind, and the strict
      reading says a receipt's jurisdiction is what it opens.  The two differ by 41 rows, which is more
      than the gap between my pinned number and either of them, so naming which is which is the answer
      rather than a caveat.
    """
    if form in ('AST-SIG', 'AST-PLACE'):
        return 'Y', 'an AST form needs open() and ast.parse and no quantity: within every receipt'
    return carry(form, qclass, caps, reads)


def main():
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'GATHERED.tsv'), encoding='utf-8')
            if l.strip() and not l.startswith('#')][1:]
    assert len(rows) == 272, len(rows)

    order, seen = [], set()
    for r in rows:
        if r[1] not in seen:
            seen.add(r[1])
            order.append(r[1])
    assert len(order) == len(T) == 233, (len(order), len(T))

    wit = resolve_witnesses()
    print('── witness classes, resolved by content over the tree ──')
    bad = [c for c, h in wit.items() if not h]
    for c, h in sorted(wit.items()):
        print(f'  {c:9s} {len(h):4d} modules   e.g. {", ".join(os.path.basename(x) for x in h[:3])}')
    assert not bad, f'EMPTY WITNESS CLASS -- these rows are NOWHERE, not computable: {bad}'

    # the prefix guard: the table is keyed by position, so a reorder must crash and not mis-read
    idx = {}
    for i, raw in enumerate(order, 1):
        lit = json.loads(raw) if raw.startswith('"') else raw
        guard, form, qcl, wcl, note = T[i]
        assert lit[:len(guard)] == guard, f'ROW {i} MOVED: table says {guard!r}, ledger has {lit[:30]!r}'
        assert wcl == '-' or wcl in wit, f'row {i}: unknown witness class {wcl}'
        idx[raw] = (form, qcl, wcl, note, lit)

    out = []
    for r in rows:
        form, qcl, wcl, note, lit = idx[r[1]]
        cy, why = carry(form, qcl, r[8], r[9])
        kc, kw = carry_capability(form, qcl, r[8], r[9])
        out.append(dict(stem=r[0], lit=lit, container=r[4], line=r[6], form=form, qclass=qcl,
                        witness=wcl, note=note, caps=r[8], reads=r[9], carry=cy, carry_why=why,
                        carry_cap=kc, carry_cap_why=kw))

    dest = os.path.join(HERE, 'READING.tsv')
    cols = ['stem', 'lit', 'container', 'line', 'form', 'qclass', 'witness', 'note',
            'caps', 'reads', 'carry', 'carry_why', 'carry_cap', 'carry_cap_why']
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('# r7257 order ①/② -- the reading of the 272 MEANING-HELD rows against the rule frozen\n')
        fh.write('# in PREDICTION.md.  `note` is the CONVERSE for a computable row -- the concrete edit\n')
        fh.write('# that reds the predicate -- and the reason code for one that is not.\n')
        fh.write('\t'.join(cols) + '\n')
        for d in out:
            fh.write('\t'.join(str(d[c]).replace('\t', ' ') for c in cols) + '\n')

    n = len(out)
    comp = [d for d in out if d['form'] in ('AST-SIG', 'AST-PLACE', 'INDEP')]
    nowhere = [d for d in out if d['form'] == 'NOWHERE']
    print(f'\n── ORDER ①: {n} rows, {len(seen)} distinct literals ──')
    print('form      :', collections.Counter(d['form'] for d in out).most_common())
    print(f'COMPUTABLE: {len(comp)}/{n} = {100*len(comp)/n:.1f}%   '
          f'(pinned 30%, band 20-42)   NOWHERE {len(nowhere)} = {100*len(nowhere)/n:.1f}% (pinned 8, band 3-18)')
    print(f'upper tail: {100*(len(comp)+len(nowhere))/n:.1f}%')
    for f in ('AST-SIG', 'AST-PLACE', 'INDEP'):
        k = sum(1 for d in comp if d['form'] == f)
        print(f'  {f:10s} {k:4d}  = {100*k/len(comp):.1f}% of computable')
    print('qclass    :', collections.Counter(d['qclass'] for d in comp).most_common())
    print('reason    :', collections.Counter(d['note'] for d in out if d['form'] == 'NO').most_common())

    cy = [d for d in comp if d['carry'] == 'Y']
    print(f'\n── ORDER ②: {len(cy)}/{len(comp)} = {100*len(cy)/len(comp):.1f}% carryable   (pinned 72%, band 55-88) ──')
    for f in ('AST-SIG', 'AST-PLACE', 'INDEP'):
        g = [d for d in comp if d['form'] == f]
        k = sum(1 for d in g if d['carry'] == 'Y')
        if g:
            print(f'  {f:10s} {k:4d}/{len(g):4d} = {100*k/len(g):.1f}%')
    ast = [d for d in comp if d['form'].startswith('AST')]
    ic = [d for d in comp if d['form'] == 'INDEP']
    print(f'  AST forms together   {sum(1 for d in ast if d["carry"]=="Y")}/{len(ast)} = '
          f'{100*sum(1 for d in ast if d["carry"]=="Y")/len(ast):.1f}%  (pinned 95, band 85-100)')
    print(f'  INDEPENDENT COMP     {sum(1 for d in ic if d["carry"]=="Y")}/{len(ic)} = '
          f'{100*sum(1 for d in ic if d["carry"]=="Y")/len(ic):.1f}%  (pinned 20, band 5-40)')
    print('why not   :', collections.Counter(d['carry_why'] for d in comp if d['carry'] == 'N').most_common())
    kc = [d for d in comp if d['carry_cap'] == 'Y']
    print(f'\n── ORDER ② ON THE CAPABILITY READING (AST needs no quantity): '
          f'{len(kc)}/{len(comp)} = {100*len(kc)/len(comp):.1f}%   (pinned 72%, band 55-88) ──')
    print(f'  the two readings differ by {len(kc)-len(cy)} rows, all of them AST forms held by a '
          f'receipt that opens no source file')
    # and the ledger's own target column against the container the receipt actually reads
    led = collections.Counter(r[2] for r in rows)
    con = collections.Counter(d['container'] for d in out)
    print(f'\n── the ledger target column vs the container resolved from the AST ──')
    print('  ledger   :', led.most_common())
    print('  resolved :', con.most_common())
    mis = sum(1 for r, d in zip(rows, out)
              if (r[2] == 'PAPER') != (d['container'] == 'PAPER'))
    print(f'  rows where the two disagree on PAPER-or-not: {mis}')
    print(f'\n{len(out)} rows -> {dest}')


if __name__ == '__main__':
    main()
