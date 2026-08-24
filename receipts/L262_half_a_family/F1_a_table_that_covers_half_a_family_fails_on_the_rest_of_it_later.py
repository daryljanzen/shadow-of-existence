#!/usr/bin/env python3
"""F1 -- the appendix generator's glyph table covered `⓵`-`⓹` of a family the corpus uses to `⓾`, and
none of the superscript check suffixes at all.  One INDEX row using `⓺ᶜ` made it refuse the whole
corpus appendix, and three receipts went red downstream of that.

COMPUTES: the two families' coverage at the commit before this one; the exact glyphs the generator
refused and that they are in the corpus's own labelling convention; the downstream failure set and
that all three clear once the table is whole; the generated families and the import-time guard,
SEEDED by removing a member; and that the guard names the family rather than the glyph.  Nothing is
pinned to a parameter.

** ⛭ ⓵ THE CONVENTION. **  *Every receipt in this corpus labels its checks `⓵`, `⓶`, ... with
superscript suffixes for sub-checks -- `⓶ᵇ`, `⓺ᶜ`.*  It is used in hundreds of files and in the
register rows generated from them.

** ⛔⛭⛭ ⓶ AND THE GENERATOR'S TABLE CARRIED HALF OF IT. **  `_UNI` mapped `⓵`-`⓹` and `①`-`⑤` -- *each
of them half a family* -- and not one of `ᵃ ᵇ ᶜ ᵈ ᵉ ᶠ`.
  ⇒ ** The gap was invisible for as long as no INDEX row used the uncovered half. **  *`L-261`'s row
    used `⓺ᶜ`; the generator's phase-3 guard fired, correctly, and refused to produce
    `appendix_receipts_corpus.tex` -- so `check_appendix_current` went red, and the three receipts
    that check it went red with it.*
  ⇒ *** A TABLE THAT COVERS PART OF A FAMILY FAILS ON THE REST OF IT, at whatever later moment
      someone uses the rest.  `L-252`'s half-covered class-fix, reached through a map instead of a
      script; and the same shape as `check_row_matchers`' one-spelling hole. ***

** ⌗ ⓷ THE REPAIR IS NOT TWO MORE ENTRIES. **  *Adding `⓺` and `ᶜ` would leave `⓻`-`⓾` and `ᵈ`-`ⁿ`
for the next person to discover the same way.*  ⇒ ** The families are GENERATED from their ranges,
and a guard at import fails if either is ever partial again -- which is the difference between a fix
and a fix that holds. **

** ⓸ AND THE GUARD THAT CAUGHT IT WAS ALREADY RIGHT. **  *The generator's phase 3 refuses to emit any
glyph it cannot translate, and its own comment says why: "a failure whose cause is three hundred
lines into a log ... Failing HERE names both."*  ⇒ ** So this is not a gate that missed something; it
is a gate that worked, on a table that was incomplete.  The finding is the table, and the loud
failure is what made it findable. **

WHAT IS NOT CLAIMED.  ** Not that the phase-3 guard should be softened ** -- it is the reason this
was a clean failure rather than a corrupt PDF, and it is untouched.  ** Not that every glyph the
corpus might use is covered ** -- two FAMILIES are, whole, and the guard names a family rather than a
glyph so the next gap is a family and not a character.  ** And not that the three downstream failures
were separate defects ** -- they were one, and the receipt below shows they clear together.

    python3 receipts/L262_half_a_family/F1_a_table_that_covers_half_a_family_fails_on_the_rest_of_it_later.py

Written r3144, `L-262`.  Stated for reversal.
"""
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BEFORE = '5da30fa4'          # r3142 -- the revision whose INDEX row broke the generator
GEN = os.path.join(ROOT, 'corpus', 'make_receipt_appendix.py')
DOWNSTREAM = [
    'receipts/L253_the_seed_that_stopped_seeding/S1_a_seed_that_stops_constructing_its_defect_'
    'accuses_the_gate_it_defends.py',
    'receipts/L255_the_exemption_was_a_claim/E1_an_exemption_is_a_claim_and_all_three_were_'
    'false.py',
    'receipts/L556_registry_from_rows/R1_the_registry_was_checked_from_citations_inward_so_twenty_'
    'rows_were_read_by_nothing.py',
]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def load(src, name):
    """import a module from SOURCE TEXT -- so the version at a commit can be measured, not guessed"""
    import types
    m = types.ModuleType(name)
    m.__file__ = GEN
    exec(compile(src, name, 'exec'), m.__dict__)
    return m


def main():
    print()
    print('  F1 -- half a family')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE TABLE AT THE COMMIT THAT REFUSED THE APPENDIX')
    print('  ' + '=' * 74)
    was_src = git('show', f'{BEFORE}:corpus/make_receipt_appendix.py')
    # the module runs a `main()` only under __main__, so importing the text is safe
    was = load(was_src, '_gen_before')
    circ = [chr(0x24F5 + i) for i in range(10)]
    sup = ['ᵃ', 'ᵇ', 'ᶜ', 'ᵈ', 'ᵉ', 'ᶠ']
    had_c = [c for c in circ if c in was._UNI]
    had_s = [c for c in sup if c in was._UNI]
    check(f'⓵ at {BEFORE} the circled check numerals were covered to {len(had_c)} of {len(circ)} '
          f'-- {"".join(had_c)} and no further', had_c == circ[:5])
    check(f'⓵ᵇ and NOT ONE of the superscript check suffixes was covered: {len(had_s)} of '
          f'{len(sup)}', had_s == [])
    check('⓵ᶜ ⌗ and `①`-`⑤` is the same half-family a second time in the same table, so it is a '
          'habit rather than an oversight',
          all(chr(0x2460 + i) in was._UNI for i in range(5))
          and not any(chr(0x2460 + i) in was._UNI for i in range(5, 10)))

    # ** the glyphs the row actually used, and that they are the convention's own **
    row = [l for l in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8')
           if 'r3142, `L-261`' in l]
    check('⓶ the row that triggered it exists and uses the uncovered half',
          len(row) == 1 and '⓺' in row[0] and 'ᶜ' in row[0])
    refused = sorted({c for c in row[0] if ord(c) > 0xFF and c not in was._UNI})
    check(f'⓶ᵇ ⛔ and the generator at {BEFORE} would refuse exactly {refused} -- both of them '
          'members of the two families above', refused == ['ᶜ', '⓺'])

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ THE FAMILIES ARE GENERATED, AND THE GUARD NAMES THE FAMILY')
    print('  ' + '=' * 74)
    spec = importlib.util.spec_from_file_location('_gen_now', GEN)
    now = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(now)
    check(f'⓷ the circled numerals are now covered {len([c for c in circ if c in now._UNI])} of '
          f'{len(circ)}, and `①`-`⑳` with them',
          all(c in now._UNI for c in circ)
          and all(chr(0x2460 + i) in now._UNI for i in range(20)))
    check(f'⓷ᵇ and the superscript suffixes {len([c for c in sup if c in now._UNI])} of {len(sup)}, '
          'each as `\\textsuperscript{...}` rather than degraded to nothing -- they are CONTENT, '
          'since a sub-check is cited by its letter',
          all(now._UNI.get(c, '').startswith('\\textsuperscript') for c in sup))
    check('⓷ᶜ and they are built from RANGES rather than listed, so the next member is covered '
          'before anyone uses it',
          'for _i in range(10)' in open(GEN, encoding='utf-8').read()
          and '_CIRCLED' in open(GEN, encoding='utf-8').read())
    # ** SEEDED: take a member out and the import-time guard must refuse. **
    seeded = open(GEN, encoding='utf-8').read().replace(
        "for _k, _v in {**_CIRCLED, **_SUPER}.items():\n    _UNI.setdefault(_k, _v)",
        "for _k, _v in {**_CIRCLED, **_SUPER}.items():\n"
        "    if _k != chr(0x24FA):\n        _UNI.setdefault(_k, _v)")
    check('⓸ SEEDED: the guard is reachable -- removing one member changes the file', seeded != src_of(GEN))
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, 'gen.py')
        open(f, 'w', encoding='utf-8').write(seeded)
        # ⌗ the generator imports `index_rows` from its own directory, so the seeded copy is run
        #   with `corpus/` on the path -- otherwise the subprocess dies on the IMPORT and the check
        #   would pass on a failure that has nothing to do with the guard.
        env = {**os.environ, 'PYTHONPATH': os.path.join(ROOT, 'corpus')}
        r = subprocess.run([sys.executable, '-c',
                            f'import runpy; runpy.run_path({f!r}, run_name="_x")'],
                           capture_output=True, text=True, errors='replace', timeout=300, env=env)
    check(f'⓸ᵇ and with `⓺` removed the module REFUSES AT IMPORT, exiting {r.returncode} and '
          'naming the FAMILY rather than the glyph',
          r.returncode != 0 and 'families are PARTIAL again' in (r.stdout + r.stderr))

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ THREE DOWNSTREAM FAILURES, ONE CAUSE')
    print('  ' + '=' * 74)
    res = git('show', f'{BEFORE}:receipts/RUN_RESULT.txt')
    print(f'    the run at {BEFORE} is {"complete" if "pass," in res else "INCOMPLETE"}; the three '
          'are verified directly below either way')
    for rel in DOWNSTREAM:
        f = os.path.join(ROOT, rel)
        rc = subprocess.run([sys.executable, f], cwd=os.path.dirname(f), capture_output=True,
                            text=True, errors='replace', timeout=1800).returncode
        check(f'⓹ {os.path.basename(rel)[:46]} exits {rc}', rc == 0)
    ap = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_appendix_current.py')],
                        capture_output=True, text=True, errors='replace', timeout=600)
    check(f'⓹ᵇ and the cause is cleared at its source: check_appendix_current exits '
          f'{ap.returncode}', ap.returncode == 0)
    check('⓺ ⌗ and the phase-3 guard that caught it is UNTOUCHED -- it is the reason this was a '
          'clean failure rather than a corrupt PDF, and its own words say so',
          'nothing untranslated leaves this function' in open(GEN, encoding='utf-8').read().lower()
          and '_left = sorted({c for c in s if ord(c) > 0xFF})' in open(GEN, encoding='utf-8').read())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a translation table that covers part of a family fails on the rest of it, **')
    print('  *at whatever later moment someone uses the rest.*  The generator mapped `⓵`-`⓹` of a')
    print('  family the corpus uses to `⓾`, `①`-`⑤` of another, and none of the superscript check')
    print('  suffixes -- and one INDEX row using `⓺ᶜ` made it refuse the whole corpus appendix.')
    print('  ⌗ ** The repair is not two more entries: ** the families are generated from their')
    print('     ranges, and a guard at import fails if either is partial again.  *Adding `⓺` and')
    print('     `ᶜ` would have left `⓻`-`⓾` for the next person to find the same way.*')
    print('  ⛭ ** And the gate that caught it was already right: ** phase 3 refuses to emit any')
    print('     glyph it cannot translate.  *This is not a gate that missed something; it is a gate')
    print('     that worked, on a table that was incomplete.*')
    print()
    return 0


def src_of(p):
    return open(p, encoding='utf-8').read()


if __name__ == '__main__':
    raise SystemExit(main())
