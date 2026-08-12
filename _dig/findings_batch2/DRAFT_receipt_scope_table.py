#!/usr/bin/env python3
"""DRAFT — the scope table: what parameter values does each receipt actually run at?

THE GAP THIS FILLS.  Batch 2's three findings share one shape: ** a claim verified at one point of
a family, stated as if it held on the family. **

  F12  a stratum labelled "Bianchi", true of six of the nine types
  F13  a concession about "two real forms", where there are four and only one takes su(3)
  F14  leaf compactness receipted at M = 0.62 M_N and stated unqualified -- and the member that
       matters most is the one it fails at
  F11  (batch 1) one quantity, two Omega_m, two published values

`check_receipts` verifies that a citation RESOLVES.  `DRAFT_check_numbers_at_citations` (batch 1)
checks that the cited receipt COMPUTES the number beside it.  ** Neither asks what the receipt's
SCOPE is. **  A receipt that hard-codes M = 0.12 supports a sentence about M = 0.12; whether it
supports a sentence with no qualifier is a question nothing in the suite poses.

This does the first half: for every receipt, the parameter settings it hard-codes.  The second half
-- does the citing sentence quantify more widely than that? -- is a reading, not a computation, and
is left to the reader.  ** The table is what makes the reading cheap. **

TWO MODES:
    python3 DRAFT_receipt_scope_table.py            # the conflict report (short)
    python3 DRAFT_receipt_scope_table.py --full     # every receipt and every setting

HONEST BOUNDS, and they matter for how this is used:

  · It reads ASSIGNMENTS, not semantics.  A receipt that computes M from something else, or sweeps
    it, will show nothing or show a seed value.  Absence from this table is not evidence of scope.
  · A spread is NOT automatically a defect.  Most of the P15 Omega_m spread is deliberate: several
    receipts run Planck's LambdaCDM at ~0.315 as the REFERENCE the CR result is measured against,
    and forcing CR's fitted value there would be the error.  ** DELIBERATE below is that allowlist,
    and it is the part a maintainer has to curate. **  The report's value is that everything not on
    it is a question someone chose not to answer yet.
  · Default-argument values (`def predict(H0=73.0, Om=0.3066, ...)`) are picked up and are the
    right thing to pick up -- they are what the receipt runs when called with no argument.
"""
import argparse, collections, os, re, sys

RC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'receipts'))

# name -> regex for an assignment or a default argument
KEYS = {
    'M':       r'\bM\s*=\s*([-+0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'Omega_m': r'\bOm(?:ega_m)?\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'H0':      r'\bH0(?:_kms)?\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'omega_r': r'\b(?:wr|omega_r|Or_content)\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'ombh2':   r'\bombh2\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'eta10':   r'\beta10\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'z_rec':   r'\bz_rec\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
}

# receipts whose setting is a DELIBERATE reference cosmology, not CR's own.  Curate this.
DELIBERATE = {
    'P15_CR_cosmology/BUILD_camb_store.py':        'Planck LambdaCDM, the CAMB reference store',
    'P15_CR_cosmology/P15_camb_reference.py':      'Planck LambdaCDM, CAMB',
    'P15_CR_cosmology/P15_damping_ratio_clean.py': 'Planck LambdaCDM, CAMB',
    'P15_CR_cosmology/P15_damping_reabsorption.py': 'Planck LambdaCDM, CAMB',
    'P15_CR_cosmology/P15_full_transfer_verdict.py': 'Planck LambdaCDM, CAMB',
}


def settings(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    body = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('#'))
    if body.lstrip().startswith('"""'):                     # drop the docstring
        body = body.split('"""', 2)[-1]
    out = {}
    for k, pat in KEYS.items():
        seen = []
        for m in re.finditer(pat, body):
            v = m.group(1).strip().rstrip(')')
            if not v or len(v) > 24:
                continue
            if v not in seen:
                seen.append(v)
        if seen:
            out[k] = seen[:3]
    return out


def scan():
    rows = {}
    for dp, dirs, files in os.walk(RC):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for f in sorted(files):
            if not f.endswith('.py'):
                continue
            p = os.path.join(dp, f)
            g = settings(p)
            if g:
                rows[os.path.relpath(p, RC)] = g
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--full', action='store_true')
    a = ap.parse_args()

    if not os.path.isdir(RC):
        print(f"  [FAIL] no receipts/ at {RC}")
        return 1
    rows = scan()
    npy = sum(len([f for f in fs if f.endswith('.py')])
              for _, _, fs in os.walk(RC))
    print(f"  scanned {npy} receipts under {RC}")
    print(f"  {len(rows)} of them hard-code at least one tracked parameter "
          f"({', '.join(sorted(KEYS))})")

    if a.full:
        print()
        for rel in sorted(rows):
            tag = '  [deliberate: %s]' % DELIBERATE[rel] if rel in DELIBERATE else ''
            print(f"  {rel}{tag}")
            for k in sorted(rows[rel]):
                print(f"      {k:<9} {', '.join(rows[rel][k])}")
        return 0

    print()
    total = 0
    for key in KEYS:
        bydir = collections.defaultdict(lambda: collections.defaultdict(list))
        for rel, g in rows.items():
            if key in g and rel not in DELIBERATE:
                bydir[rel.split('/')[0]][tuple(g[key])].append(rel.split('/')[-1])
        for d in sorted(bydir):
            if len(bydir[d]) < 2:
                continue
            total += 1
            print(f"  {key} takes {len(bydir[d])} distinct settings inside {d}"
                  f"   (deliberate reference cosmologies excluded)")
            for v, fs in sorted(bydir[d].items(), key=lambda x: -len(x[1])):
                print(f"      {str(list(v)):<26} {len(fs):>2}x  "
                      f"{', '.join(sorted(fs)[:3])}{' ...' if len(fs) > 3 else ''}")
            print()
    if total:
        print(f"  {total} parameter(s) carry more than one setting inside a single paper's receipts.")
        print("  That is a QUESTION, not a failure: either the settings are deliberate and belong")
        print("  in DELIBERATE with a reason, or the paper's sentences should say which one they")
        print("  are at.  ** Nothing else in the suite asks it. **")
    else:
        print("  Every tracked parameter has one setting per paper, or is explained in DELIBERATE.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
