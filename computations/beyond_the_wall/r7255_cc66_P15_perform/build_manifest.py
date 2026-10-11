#!/usr/bin/env python3
"""Build PERFORMED.tsv -- r7255 order ①'s record of the 27 REPAIR-OWED rows of
receipts/P15_CR_cosmology and what performing each one did.

The 27 are taken from the ledger AS IT STOOD AT THIS CYCLE'S PRE-REGISTRATION (9feb2f12),
not from recollection, and each one's fate is read from the ledger at this head: a key is
RETIRED when it is no longer live, KEPT when it still is.  The FORM column is this seat's
classification and is the only hand-entered field; it is checked against the retired/kept
split by the receipt that reads this file.

columns: stem  old_sha8  old_literal(JSON)  fate  form  subform  new_literal(JSON)  note
"""
import hashlib, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PREREG = '9feb2f12'


def sha8(s):
    return hashlib.sha1(s.encode()).hexdigest()[:8]


def rows_of(text):
    return [l.rstrip('\n').split('\t') for l in text.splitlines()
            if l.strip() and not l.startswith('#')]


def ledger_at(rev):
    out = subprocess.run(['git', 'show', f'{rev}:corpus/quote_pin_baseline.tsv'],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return rows_of(out)


# (basename PREFIX, old sha8) -> (form, subform, new literal or '-', note).  The prefix must
# resolve to exactly one of the 27; the receipt re-checks the resolution is 1:1.
FORM = {
 ('C26_', '8b6fc9b5'): (
   'RECUT', 'PROSE-ANCHOR', '"\\\\$10\\\\.8\\\\\\\\%\\\\$.{0,60}?diffusion length"',
   'exposure reduced not removed: the anchor is prose, and $10.8% occurs twice in the paper'),
 ('C62_', 'd1a90a24'): (
   'RECUT', 'PROSE-ANCHOR', '"\\\\$185\\\\$.{0,40}?converged"',
   'exposure reduced not removed: the anchor is prose, and $185 occurs four times in the paper'),
 ('P15_the_fitted_onset', 'e3cb0cf9'): (
   'DELETED', 'REDUNDANT', '-', 'abs(z_on_s - 6764.0)/6764.0 < 0.01 sits on the line beside it'),
 ('P15_the_fitted_onset', '6fd13f54'): (
   'DELETED', 'REDUNDANT', '-', 'the gate above computes the Jacobian across +-3 FWHM'),
 ('P15_the_fitted_onset', 'e093984a'): (
   'DELETED', 'REDUNDANT', '-', 'section D computes the 1.6-1.8 factor and the 1.286 pair'),
 ('P15_the_fitted_onset', '8db9df1e'): (
   'DELETED', 'REDUNDANT', '-', 'the Jacobian gate agrees with the instrument to two per cent'),
 ('P15_the_fitted_onset', 'cf55e50a'): (
   'DELETED', 'AST-REPLACED', '-', '_hier_accepts_and_uses_none() reads hier_run signature and body'),
 ('P15_the_fitted_onset', 'c17e4f5f'): (
   'DELETED', 'AST-REPLACED', '-', 'same AST property test carries this clause'),
 ('P15_the_fitted_onset', '2ab7160e'): (
   'DELETED', 'REDUNDANT', '-', 'abs(rs_l_on - 105.36) < 0.5 and the 1.286 ratio sit beside it'),
 ('P15_the_fitted_onset', '1a76563a'): (
   'RECUT', 'SYMBOL-ANCHOR',
   '"\\\\$\\\\\\\\ell_\\\\{A\\\\}\\\\$[^$]{0,30}\\\\$([\\\\d.]+)\\\\$[^$]{0,30}\\\\$([\\\\d.]+)\\\\$[^$]{0,80}\\\\$([\\\\d.]+)\\\\$[^$]{0,30}\\\\$([\\\\d.]+)\\\\$"',
   'the four connectives from/down to/sits between/throughout freed; same four values'),
 ('P15_the_fitted_onset', '61d2ed7b'): (
   'SHORTEN', 'LIMB-TWO', '"the sound horizon has no lower endpoint to place"',
   'the trailing consequent is a second claim the gate does not use; one occurrence'),
 ('P15_the_freezing_census', '137d0e5a'): (
   'RECUT', 'SYMBOL-ANCHOR', '"\\\\$1\\\\.96\\\\$.{0,40}?0\\\\.1\\\\\\\\,\\\\\\\\alpha"',
   'fully reword-immune: both ends are symbols, the window carries no prose'),
 ('P15_the_harmonic_expansion', '2152f995'): (
   'DELETED', 'AST-REPLACED', '-', '_prod_uses_phys reads the attribute Hphys from the syntax tree'),
 ('P15_the_harmonic_expansion', '5f49fc3c'): (
   'DELETED', 'AST-REPLACED', '-', '_rad_term_placement reads the Div-over-Pow-4 term and its guard'),
 ('P15_the_harmonic_expansion', '4832ab3e'): (
   'SHORTEN', 'LIMB-TWO', '"The constant-$\\\\tau$ slice is exactly flat"',
   'the dropped tail is the spelling of the conclusion, not the conclusion'),
 ('P15_the_kernels_distance', 'fafeced8'): (
   'SHORTEN+ANCHOR', 'LIMB-TWO', '"Because the distance slicing is flat"',
   'the clause exemplar: the short form occurs TWICE, so the read is scoped to a 400-char window'),
 ('P15_the_kernels_distance', '4832ab3e'): (
   'SHORTEN', 'LIMB-TWO', '"The constant-$\\\\tau$ slice is exactly flat"',
   'same shortening, same paper sentence, different receipt'),
 ('P15_the_kernels_distance', '6fa619cf'): (
   'REVERDICT', 'LIMB-ONE', '"prop:flat"',
   'a \\label is an IDENTITY, so limb ONE holds it; what was wrong was the hollow True is bool(...) shape'),
 ('P15_the_one_ground', 'ab86629b'): (
   'SHORTEN', 'LIMB-TWO', '"The constant-$\\\\tau$ slice is exactly flat"',
   'same shortening, third receipt'),
 ('P15_the_one_ground', 'e8d91b9e'): (
   'SHORTEN', 'LIMB-TWO', '"$D_M=D_C$"',
   'the dropped prose restates the symbols it carries; the formula pin is reword-IMMUNE where the long one was not'),
 ('P15_the_optical_depth', '19a65c83'): (
   'RECUT', 'SYMBOL-ANCHOR', '"\\\\$0\\\\.7312\\\\$.{0,60}?\\\\$f=-0\\\\.304\\\\$"',
   'fully reword-immune: BOTH halves are values and the claim is their pairing'),
 ('P15_the_rate_rule', 'd9a1eb91'): (
   'SHORTEN', 'LIMB-TWO',
   '"a comoving separation read across leaves, $D_M$, $D_H$, $D_V$, the observable expansion---takes the stacking rate"',
   'the leading frame is not part of what the gate claims; the shortened form is already a live key in two other receipts'),
 ('P15_the_rate_rule', '28265f1a'): (
   'SHORTEN', 'LIMB-TWO',
   '"the comoving angular-diameter distance \\\\emph{is} the light-travel distance $D_C$"',
   'the bundled antecedent is a key of its own in the same receipt'),
 ('P15_the_rate_rule', '53f030c2'): (
   'DELETED', 'COMPUTED-ELSEWHERE', '-',
   'P15_the_one_ground... computes all 81 Riemann components of the same induced three-metric'),
 ('P15_the_rate_rule', '2b101fc7'): (
   'DELETED', 'COMPUTED-ELSEWHERE', '-',
   'same 81-component computation; the pin was prose standing in for it'),
 ('P15_the_segments', '8a522131'): (
   'RECUT', 'PROSE-ANCHOR', '"\\\\$-152\\\\$.{0,40}?acoustic peak"',
   'exposure reduced not removed: the anchor is prose'),
 ('P15_the_segments', '137d0e5a'): (
   'RECUT', 'SYMBOL-ANCHOR', '"\\\\$1\\\\.96\\\\$.{0,40}?0\\\\.1\\\\\\\\,\\\\\\\\alpha"',
   'fully reword-immune; same pattern as the freezing census, same load-bearing half'),
}


def main():
    old = ledger_at(PREREG)
    live = {(r[0], r[1]) for r in rows_of(open(
        os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read()) if len(r) >= 6}
    owed = [r for r in old if len(r) >= 6 and r[5] == 'REPAIR-OWED' and 'P15_CR_cosmology' in r[0]]
    out, missing = [], []
    for r in sorted(owed, key=lambda x: (x[0], x[1])):
        stem, lit = r[0], r[1]
        base, h = os.path.basename(stem), sha8(lit)
        hit = [v for (tag, hh), v in FORM.items() if hh == h and base.startswith(tag)]
        if len(hit) != 1:
            missing.append((base[:40], h, len(hit)))
            continue
        form, sub, new, note = hit[0]
        fate = 'KEPT' if (stem, lit) in live else 'RETIRED'
        out.append([stem, sha8(lit), lit, fate, form, sub, new, note])
    if missing:
        print('UNCLASSIFIED:', missing, file=sys.stderr)
        raise SystemExit(2)
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PERFORMED.tsv')
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('# r7255 order ① -- the 27 REPAIR-OWED rows of receipts/P15_CR_cosmology, performed.\n')
        fh.write(f'# the 27 are selected from the ledger at {PREREG} (this cycle\'s pre-registration);\n')
        fh.write('# `fate` is read from the ledger at this head; `form`/`subform`/`note` are this seat\'s.\n')
        fh.write('# stem\told_sha8\told_literal\tfate\tform\tsubform\tnew_literal\tnote\n')
        for row in out:
            fh.write('\t'.join(row) + '\n')
    print(f'{len(out)} rows -> {dest}')


if __name__ == '__main__':
    main()
