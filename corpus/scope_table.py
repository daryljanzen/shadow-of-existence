#!/usr/bin/env python3
"""scope_table.py -- what parameter values does each receipt actually RUN at?

** CONTRIBUTED BY NODE 55 (batch 2, F15).  ADOPTED AT r2443 AS A LINT AND NOT A GATE. **

THE GAP IT FILLS, and the contributor's statement of it is exact:

    * check_receipts verifies a citation RESOLVES.
    * check_numbers_at_citations (its batch 1) checks the cited receipt COMPUTES the number.
    * ** Nothing asks what the receipt's SCOPE is. **

And L-230 established at r2442 that ** scope is where a whole class of defects lives, invisible to
every gate the corpus has -- because in every instance the sentence is TRUE and only its scope is
wrong, and no gate reads scope. **  This does the first half: for every receipt, the parameter
settings it hard-codes, INCLUDING default-argument values, which are what a receipt runs at when
called bare.  ** The second half -- does the citing sentence quantify more widely? -- is a reading,
not a computation.  The table makes the reading cheap. **

⚠ ** WHY IT IS A LINT AND NOT A GATE, and it is the same reason check_loci is: ** the DELIBERATE
allowlist.  A receipt running Planck's LambdaCDM at ~0.315 as the REFERENCE the CR result is measured
against must not read as drift, because ** forcing CR's fitted value there would be the error. **
Curating that list is a maintainer's judgement, and a gate cannot hold a judgement -- it can only hold
a declaration.  ** Everything NOT on the list is a question someone chose not to answer yet. **

ITS FIRST YIELD, verified independently at r2443: ** P15's receipt layer carries TWO internally
consistent parameter sets, and the paper draws on both. **

    Set A -- the C-chain (sec:envelope-consequence)  : z_rec = 1100.0
    Set B -- ROBUST / UNC / the-ratio / C11TEST      : Omega_m = 0.3066, z_rec = 1089.9

  ⇒ ** Not a scatter: the receipts cluster. **  Confirmed by reading the seven named receipts.  On a
    like-for-like toy the sets differ by +0.58% in r_s and +0.55% in theta_* (the contributor's own
    figures, from the receipts' own code paths, are 0.76% and 0.72% -- theirs are the ones to quote).

  ⚠ AND WHY IT MATTERS IS NOT THE 0.7%.  P15 sec:refit-bound's argument is a RATIO in which things
    are supposed to cancel -- "the last-scattering thickness ... cancels from the ratio" and z_*
    "moves by only -0.11%".  ** A 0.7% inconsistency between the receipt sets is six times the 0.11%
    the paper reports as negligible, so WHICH SET a number came from is load-bearing there. **

✔ THE PARSER DEFECTS RECORDED AT ADOPTION ARE FIXED (r2446), and there were THREE, each a different
reading of what counts as a setting:

  * ** TUPLE ASSIGNMENT. **  `ombh2, z_rec = 0.0224, 1089.9` matched z_rec and captured 0.0224,
    because the pattern takes the first value after the `=` rather than the one POSITIONALLY
    corresponding to the name.  Fixed by expanding flat tuple assignments before matching.
    ⌗ ** And it resolved into a TRUE positive on the other side of the fix: ** both sites carry real
    settings -- 1089.9 (Set B) and 1100.0 (Set A) -- so correcting the parser ADDED one receipt to
    each set.  ** A false positive that becomes a true positive when fixed is the best kind: the tool
    was seeing something and reporting it under the wrong name. **
  * ** THE NUMBER PATTERN. **  `M = sp.Matrix([[0,1,0],...` matched the M pattern.  A parameter
    pattern must require a bare NUMBER, or it reports every use of the letter.
  * ** STRING LITERALS. **  P14's second M was `det M = +1` inside a PRINTED LABEL.  Narrowing the
    number pattern did not touch it, because the text was a perfectly good "M = +1".
    ⇒ ** A parameter SETTING is code; a parameter mentioned in a string is prose the receipt happens
      to print. **  The same reasoning that already dropped comments and the docstring -- literals
      were simply the case nobody had hit.

⇒ ** AND THE FINDING SURVIVED EVERY FIX AND GOT STRONGER. **  F15's two-set claim rested on z_rec at
7-versus-4 with two spurious rows.  ** It is now 8-versus-7, clean ** -- a near-even split across
P15's receipt layer, which makes "which set is this number at?" a HARDER question for the paper, not
an easier one.

Adopted r2443.  Stated for reversal.
"""

# ── the contributor's own header, kept verbatim ──
# """DRAFT — the scope table: what parameter values does each receipt actually run at?
# 
# THE GAP THIS FILLS.  Batch 2's three findings share one shape: ** a claim verified at one point of
# a family, stated as if it held on the family. **
# 
#   F12  a stratum labelled "Bianchi", true of six of the nine types
#   F13  a concession about "two real forms", where there are four and only one takes su(3)
#   F14  leaf compactness receipted at M = 0.62 M_N and stated unqualified -- and the member that
#        matters most is the one it fails at
#   F11  (batch 1) one quantity, two Omega_m, two published values
# 
# `check_receipts` verifies that a citation RESOLVES.  `DRAFT_check_numbers_at_citations` (batch 1)
# checks that the cited receipt COMPUTES the number beside it.  ** Neither asks what the receipt's
# SCOPE is. **  A receipt that hard-codes M = 0.12 supports a sentence about M = 0.12; whether it
# supports a sentence with no qualifier is a question nothing in the suite poses.
# 
# This does the first half: for every receipt, the parameter settings it hard-codes.  The second half
# -- does the citing sentence quantify more widely than that? -- is a reading, not a computation, and
# is left to the reader.  ** The table is what makes the reading cheap. **
# 
# TWO MODES:
#     python3 DRAFT_receipt_scope_table.py            # the conflict report (short)
#     python3 DRAFT_receipt_scope_table.py --full     # every receipt and every setting
# 
# HONEST BOUNDS, and they matter for how this is used:
# 
#   · It reads ASSIGNMENTS, not semantics.  A receipt that computes M from something else, or sweeps
#     it, will show nothing or show a seed value.  Absence from this table is not evidence of scope.
#   · A spread is NOT automatically a defect.  Most of the P15 Omega_m spread is deliberate: several
#     receipts run Planck's LambdaCDM at ~0.315 as the REFERENCE the CR result is measured against,
#     and forcing CR's fitted value there would be the error.  ** DELIBERATE below is that allowlist,
#     and it is the part a maintainer has to curate. **  The report's value is that everything not on
#     it is a question someone chose not to answer yet.
#   · Default-argument values (`def predict(H0=73.0, Om=0.3066, ...)`) are picked up and are the
#     right thing to pick up -- they are what the receipt runs when called with no argument.
# """

import argparse, collections, os, re, sys

# ** r2443: the original resolved receipts/ as ../../receipts, correct from its own home in
# _dig/findings_batch2/ and wrong from corpus/.  ** A path assumed from one location is a path, not a
# resolution. **  Walk up until receipts/ is found, so the tool runs from anywhere in the tree.
def _find_receipts():
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        cand = os.path.join(d, 'receipts')
        if os.path.isdir(cand):
            return cand
        d = os.path.dirname(d)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'receipts')


RC = _find_receipts()

# ** r2446: TUPLE ASSIGNMENT, which is where both of this tool's false positives came from. **
# `ombh2, z_rec = 0.0224, 1089.9` matched the z_rec pattern and captured 0.0224, because the regex
# takes the first value after the `=` rather than the one POSITIONALLY corresponding to the name.
# Reported at adoption (r2443) as two false positives; this is the fix.
#
# ⌗ AND IT STRENGTHENS THE FINDING RATHER THAN SHRINKING IT: both sites carry real settings --
# P15_the_first_peak_figure_is_not_stable at z_rec = 1089.9 (Set B) and
# P15_the_shear_coefficient_derived_not_remembered at z_rec = 1100.0 (Set A) --
# ** so correcting the parser ADDS two receipts to the two-set picture, one to each side. **
# A false positive that resolves into a true positive on the other side of the fix is the best kind:
# the tool was seeing something and reporting it under the wrong name.
_TUPLE = re.compile(r'^([ \t]*)([A-Za-z_][\w, \t]*?)\s*=\s*([^=\n#][^\n#]*)$', re.M)


def _expand_tuples(src):
    """Rewrite `a, b = x, y` as separate `a = x` / `b = y` lines so the name-patterns below
    capture the value that belongs to the name.  Left alone when the arities disagree, when
    either side contains a call or subscript, or when there is no comma at all."""
    out = []
    for line in src.split('\n'):
        m = _TUPLE.match(line)
        if not m or ',' not in m.group(2):
            out.append(line)
            continue
        names = [n.strip() for n in m.group(2).split(',')]
        rhs = m.group(3)
        # only split a FLAT comma list: no brackets, no calls
        if any(c in rhs for c in '()[]{}'):
            out.append(line)
            continue
        vals = [v.strip() for v in rhs.split(',')]
        if len(names) != len(vals) or not all(n.isidentifier() for n in names):
            out.append(line)
            continue
        out.extend(f'{m.group(1)}{n} = {v}' for n, v in zip(names, vals))
    return '\n'.join(out)


# name -> regex for an assignment or a default argument
KEYS = {
    # ** r2446: narrowed.  The original matched `M = sp.Matrix([[0,1,0],...` and `det M = +1`
    # in P14_the_lap_orientation_is_derived -- a matrix and a determinant, not a mass.
    # ⇒ ** A parameter pattern must require a bare NUMBER, or it reports every use of the letter. **
    'M':       r'(?<![\w.])M\s*=\s*([-+]?[0-9]+\.?[0-9]*(?:[eE][-+]?[0-9]+)?)\s*(?=[;\n#,)]|$)',
    'Omega_m': r'\bOm(?:ega_m)?\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'H0':      r'\bH0(?:_kms)?\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'omega_r': r'\b(?:wr|omega_r|Or_content)\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'ombh2':   r'\bombh2\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'eta10':   r'\beta10\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
    'z_rec':   r'\bz_rec\s*=\s*([0-9][0-9eE+\-*/.()\s]*?)(?=[;\n#,)]|$)',
}

# ** r2446: TWO CATEGORIES, because they are two different judgements and collapsing them hides one. **
#
# DELIBERATE  -- a RECEIPT running someone else's cosmology as the reference CR is measured against.
#                Excluding it is right: forcing CR's fitted value there would be the error.
# BY_DESIGN   -- a PARAMETER that legitimately carries two values across the whole layer, because the
#                paper's argument runs at both.  ** H0 at 67.4 and 73.0 is not drift: it is the Hubble
#                tension itself, and P15's sec:refit-bound turns on evaluating at both ends. **
#                Reporting that as a spread would train a reader to ignore the tool.
#
# ⚠ AND THE DISTINCTION MATTERS BEYOND TIDINESS: a receipt-level exclusion says "this file is not
# about CR"; a parameter-level one says "this quantity has two right answers".  ** Only the second
# survives a reader asking WHICH VALUE a sentence is at -- because for a BY_DESIGN parameter, the
# sentence must say. **  So BY_DESIGN entries are not silenced; they are reported under their own
# heading, as a question about citation rather than about consistency.
BY_DESIGN = {
    ('P15_CR_cosmology', 'H0'): ("67.4 and 73.0 are the two ends of the Hubble tension; "
                                 "sec:refit-bound evaluates at both by construction"),
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
    t = _expand_tuples(open(path, encoding='utf-8', errors='replace').read())
    body = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('#'))
    # ** r2446: STRIP STRING LITERALS.  P14's second `M` setting was `det M = +1` inside a PRINTED
    # LABEL -- a string, not code.  Narrowing the number pattern did not touch it, because the text
    # was a perfectly good "M = +1".  ⇒ ** A parameter SETTING is code; a parameter mentioned in a
    # string is prose the receipt happens to print. **  The same reasoning as dropping comments and
    # the docstring, which this function already does -- the literals were simply the case nobody
    # had hit yet.
    body = re.sub(r'"[^"\n]*"|\'[^\'\n]*\'', '""', body)
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
            # ** r2446: BY_DESIGN is reported under its own heading, not silenced. **  A parameter
            # that legitimately carries two values (H0 at both ends of the Hubble tension) is not a
            # consistency question -- but it IS a citation question, because ** for such a parameter
            # a sentence quoting a number MUST say which value it is at. **  Silencing it would hide
            # the one question it does raise.
            why = BY_DESIGN.get((d, key))
            if why:
                print(f"  ⌗ {key} takes {len(bydir[d])} settings inside {d} BY DESIGN")
                print(f"      {why}")
                print(f"      ⇒ not a consistency question. ** A sentence quoting one of these must")
                print(f"         say which value it is at. **")
            else:
                print(f"  {key} takes {len(bydir[d])} distinct settings inside {d}"
                      f"   (deliberate reference cosmologies excluded)")
            for v, fs in sorted(bydir[d].items(), key=lambda x: -len(x[1])):
                print(f"      {str(list(v)):<26} {len(fs):>2}x  "
                      f"{', '.join(sorted(fs)[:3])}{' ...' if len(fs) > 3 else ''}")
            print()
    if total:
        print(f"  {total} parameter(s) carry more than one setting inside a single paper's receipts"
              f"   (BY_DESIGN entries above are counted here too, and are a CITATION question,"
              f" not a consistency one).")
        print("  That is a QUESTION, not a failure: either the settings are deliberate and belong")
        print("  in DELIBERATE with a reason, or the paper's sentences should say which one they")
        print("  are at.  ** Nothing else in the suite asks it. **")
    else:
        print("  Every tracked parameter has one setting per paper, or is explained in DELIBERATE.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
