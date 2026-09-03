#!/usr/bin/env python3
r"""V1 -- a translation table validated only against what it was asked to render carries its next
failure already in the tree: the appendix generator refused L-269's register row over a single "star",
and asked how many OTHER untranslated glyphs were already sitting in the register documents, the
answer was eighteen, in one hundred and eighty-two occurrences.

COMPUTES: the generator's refusal reproduced on the row that triggered it; the full survey of the five
register and reach documents against the generator's OWN escape function, at the parent commit and at
this one; the eighteen glyphs and their counts; the four that were genuinely above the generator's
refusal threshold once the survey was made to RUN the rule instead of restating it; and the new gate,
seeded in both directions.  Nothing is pinned numerically and nothing is fitted.

** ⛭ ⓵ TWO CORRECT REPAIRS THAT NEVER ASKED THE QUESTION UNDERNEATH. **  *`L-262` made
`make_receipt_appendix` refuse, loudly and by name, on a glyph it cannot render -- a real repair, and
it has fired since.  `L-267` found that refusal being swallowed by `cmd && loop; echo "gates green"`
and built `scripts/gate_sweep.py` so a generator failure can no longer print a pass -- also real.*
  ⇒ ** Both treat an untranslatable glyph as an EVENT: something that happens when a row is written. **
  ⇒ ** Neither asks how many are already in the tree, waiting for a row to reach for them. **

** ⛔⛭⛭ ⓶ ASKED, THE ANSWER WAS EIGHTEEN. **  *Surveying the five register and reach documents against
the generator's own table: `⌷` seventy-one times, `⌫` twenty-six, `⟨` and `⟩` twenty-one each, `★`
eighteen, `▣` six, and twelve more.*
  ⇒ *** `★` DID NOT BECOME A PROBLEM WHEN IT WAS WRITTEN.  It became one when a register row happened
      to reach for it, eighteen occurrences later. ***
  ⇒ ** So the generator's refusal is a backstop, not a measurement: it reports the glyph that arrived,
    and is silent about the seventeen already standing behind it. **

** ⛔ ⓷ AND THIS GATE'S OWN FIRST FORM RESTATED THE RULE INSTEAD OF RUNNING IT. **  *It flagged every
character above `U+00A0` with no table entry and reported TEN -- of which SIX were the accented letters
in author names (`ö é î ü`), a pilcrow and a division sign, all of which the generator passes through
happily, because `pdflatex` handles Latin-1 and the refusal fires only above `U+00FF`.*
  ⇒ *** A GATE THAT RESTATES THE RULE IT GUARDS MEASURES ITS OWN RESTATEMENT -- and drifts in whichever
      direction the copy drifted: here toward false alarm, and next time toward silence. ***
  ⇒ ** The repair removes the threshold rather than correcting it: the gate calls the generator's own
    `tex_escape` on each distinct character and records what that function refuses.  There is nothing
    left to keep in step, because the measurement IS the thing enforced. **

** ⌗ ⓸ AND THE FOUR THAT SURVIVED THE CORRECTED SURVEY WERE REAL. **  *`Φ`, `ħ`, a combining
circumflex, and -- the sharpest -- a SMALL CAPITAL `ʙ` used once as a check-label suffix where the
rest of the corpus writes the superscript `ᵇ`.*
  ⇒ ** The same label in a second spelling, which is exactly how a family-shaped table gets a hole:
    `L-262` generated the check-label family from its RANGE so it could not be partial, and a glyph
    from outside that range wearing the same meaning walked straight past it. **

WHAT IS NOT CLAIMED.  ** Not that the table is now complete ** -- it is complete over the SURVEYED
documents, which is what the gate says and all it says.  ** Not that coverage is correctness ** -- a
glyph mapped to the wrong LaTeX passes this gate and comes out wrong in the PDF; the gate measures
whether the generator refuses, nothing else.  ** Not that the wide table should replace the loud
refusal ** -- the refusal stays, because a table this wide could otherwise swallow an unsurveyed glyph
silently, and a build that stops is better than a page that lies.  ** And not that `L-262` or `L-267`
were wrong ** -- both repairs stand and both fired; what is added is that an event-shaped repair leaves
the standing population unmeasured.

    python3 receipts/L270_the_table_that_carried_its_next_failure/V1_a_translation_table_validated_only_against_what_it_was_asked_to_render.py

Written r3158, `L-270`.  Stated for reversal.
"""
import collections
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
PARENT = '5722ecf7'          # r3156 -- before this revision widens the table

SURVEYED = ['THE_LIVE_ARC.md', 'receipts/INDEX.md', 'THE_MATHEMATICS_REACH.md',
            'THE_PHYSICS_REACH.md', 'OWED.md']


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def load_generator(path):
    spec = importlib.util.spec_from_file_location('_mra_%d' % abs(hash(path)), path)
    mod = importlib.util.module_from_spec(spec)
    saved = sys.argv
    sys.argv = ['make_receipt_appendix.py', '-', '-']
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    finally:
        sys.argv = saved
    return mod


def refused(mod, ch):
    try:
        mod.tex_escape(ch)
    except BaseException:
        return True
    return False


def survey(mod, texts):
    """{glyph: count} for every non-ASCII character the generator's own escape refuses"""
    out, verdict = collections.Counter(), {}
    for t in texts:
        for ch in t:
            if ord(ch) < 0x80:
                continue
            if ch not in verdict:
                verdict[ch] = refused(mod, ch)
            if verdict[ch]:
                out[ch] += 1
    return out


def main():
    print()
    print('  V1 -- the table carried its next failure already in the tree')
    print()

    gen_now = load_generator(os.path.join(ROOT, 'corpus', 'make_receipt_appendix.py'))

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE REFUSAL FIRED, AND IT WAS RIGHT')
    print('  ==========================================================================')
    check('⓵ the generator still REFUSES rather than emitting an unknown glyph verbatim: an '
          'unassigned pictograph raises out of tex_escape',
          refused(gen_now, chr(0x1F600)))
    check('⓵ᵇ and it accepts a glyph it knows, so the refusal is a measurement and not a blanket',
          not refused(gen_now, '⌗'))
    src = open(os.path.join(ROOT, 'corpus', 'make_receipt_appendix.py'),
               encoding='utf-8', errors='replace').read()
    check('⓵ᶜ the refusal is above LATIN-1 by the generator\'s own rule, and that threshold lives in '
          'the generator alone -- it is not copied into the gate',
          'ord(c) > 0xFF' in src
          and 'ord(c) > 0xFF' not in open(os.path.join(ROOT, 'corpus',
                                                       'check_glyph_coverage.py'),
                                          encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ AND SEVENTEEN MORE WERE ALREADY STANDING BEHIND IT')
    print('  ==========================================================================')
    # ** the survey is run at the PARENT, where the table had not yet been widened. **
    #   *Reading the present tree for the state this revision changes is `L-268`'s class.*
    old_gen_src = git('show', f'{PARENT}:corpus/make_receipt_appendix.py')
    tmp = os.path.join('/tmp', 'mra_parent_L270.py')
    open(tmp, 'w', encoding='utf-8').write(old_gen_src)
    gen_parent = load_generator(tmp)
    old_texts = [git('show', f'{PARENT}:{fn}') for fn in SURVEYED]
    check('⓶ the parent commit is the one this revision widens the table from, and its generator '
          'loads', hasattr(gen_parent, 'tex_escape') and len(old_gen_src) > 1000)

    before = survey(gen_parent, old_texts)
    check(f'⓶ᵇ ⛔ AT THE PARENT, {len(before)} distinct glyph(s) in the register documents had no '
          f'translation, in {sum(before.values())} occurrence(s) -- and the generator was green, '
          'because no row had reached for one yet',
          len(before) >= 10 and sum(before.values()) >= 100)
    for ch, n in before.most_common(6):
        print(f'          U+{ord(ch):04X}  {ch!r:>8}  ×{n}')
    check('⓶ᶜ ★ was among them, and the row that finally reached for it is this revision\'s own '
          'L-269 index row -- so the glyph had been in the tree long before the build that failed',
          '★' in before and before['★'] > 5)
    check('⓶ᵈ ⌷ and the most common was not ★ at all: a structural bullet used dozens of times, '
          'which would have broken whichever row happened to carry it first',
          before.most_common(1)[0][1] > 20)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔ THE FIRST FORM OF THE GATE RESTATED THE RULE AND MISMEASURED')
    print('  ==========================================================================')
    # ** the discarded form: "flag anything above U+00A0 with no table entry" **
    naive = collections.Counter()
    for t in old_texts:
        for ch in t:
            if ord(ch) > 0x00A0 and ch not in gen_parent._UNI:
                naive[ch] += 1
    latin1 = {ch for ch in naive if ord(ch) <= 0xFF}
    check(f'⓷ the restated rule flags {len(latin1)} Latin-1 character(s) the generator passes '
          'through happily -- the accented letters in author names among them',
          len(latin1) >= 4 and all(not refused(gen_parent, ch) for ch in latin1))
    check('⓷ᵇ so the two rules DISAGREE on real characters in the real tree, which is what makes '
          'the restatement a defect rather than a stylistic difference',
          set(naive) != set(before))
    check('⓷ᶜ ⌗ and the repair removes the threshold rather than correcting it: the gate calls the '
          'generator\'s tex_escape and has no codepoint literal of its own',
          'tex_escape' in open(os.path.join(ROOT, 'corpus', 'check_glyph_coverage.py'),
                               encoding='utf-8', errors='replace').read())
    check('⓷ᵈ and the finding is recorded IN THE GATE, not only here',
          'RESTATES THE RULE IT GUARDS' in open(os.path.join(ROOT, 'corpus',
                                                             'check_glyph_coverage.py'),
                                                encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⚠ THE SMALL-CAPITAL B, AND HOW A FAMILY-SHAPED TABLE GETS A HOLE')
    print('  ==========================================================================')
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('⓸ the register uses a SMALL CAPITAL ʙ (U+0299) as a check-label suffix',
          'ʙ' in arc)
    check('⓸ᵇ while the corpus elsewhere writes that suffix as the superscript ᵇ (U+1D47), and '
          'L-262 generated THAT family from its range so it could not be partial',
          'ᵇ' in arc and '_SUPER' in src)
    check('⓸ᶜ ⛭ so the hole is not a missing member of a family -- it is the SAME MEANING wearing '
          'a glyph from outside the range the family was generated from',
          not (0x1D43 <= 0x0299 <= 0x1D7F))
    check('⓸ᵈ and it is translated to its family\'s form rather than to nothing, because dropping '
          'it would silently delete a label',
          gen_now._UNI['ʙ'].endswith('{b}'))

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ THE GATE, SEEDED BOTH WAYS')
    print('  ==========================================================================')
    now = survey(gen_now, [open(os.path.join(ROOT, fn), encoding='utf-8',
                                errors='replace').read() for fn in SURVEYED])
    check(f'⓹ on the repaired tree the survey returns {len(now)} untranslated glyph(s)', not now)
    rc = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_glyph_coverage.py')],
                        cwd=ROOT, capture_output=True, text=True, errors='replace', timeout=600)
    # ** ⛭⛭⛭ RE-PINNED r3976, AND THE GATE GREW A SECOND RAIL. **  These three pinned the gate's
    # ** REPORT WORDING from when it surveyed one rail -- "every glyph in the surveyed documents has
    # ** a translation", "documents surveyed", "control: an unknown glyph is refused".  The gate now
    # ** runs TWO rails, `\rcpt` and `\ldg`, and prints per rail; the ledger rail was added because
    # ** *"it ran for sixty revisions unsurveyed"*, which is the gate getting STRONGER.
    # **   ⇒ ** A pin into a gate's OUTPUT is a pin into prose, and it breaks the same way. **  Same
    # **     class as a paper's sentence moving -- met here on an instrument instead of a paper.
    # **   ⛔ AND THE CONTROL LINE STOPPED PRINTING BECAUSE IT PASSES: it is a failure path now, so
    # **     `'control: ...' in rc.stdout` could only ever be true when the control BROKE.  ** A
    # **     check that can only pass when the thing it guards is broken is worse than no check. **
    # **     It is SEEDED below instead, which is what it always wanted to be.
    check(f'⓹ᵇ and the gate agrees, exiting {rc.returncode} with every glyph translated on BOTH '
          f'rails',
          rc.returncode == 0
          and 'every glyph on both rails has a translation in the table that rail uses' in rc.stdout)
    _gsrc = open(os.path.join(ROOT, 'corpus', 'check_glyph_coverage.py'),
                 encoding='utf-8', errors='replace').read()
    check('⓹ᶜ it reports its population every run -- feeding documents, per rail -- and FAILS on an '
          'empty survey, because a survey that read nothing is green forever',
          'feeding document(s)' in rc.stdout and 'An empty survey is green forever' in _gsrc)
    # ** SEEDED: put an untranslatable glyph into a surveyed document and the gate must catch it **
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, 'corpus'))
        os.makedirs(os.path.join(td, 'receipts'))
        # ** the generator imports siblings by bare name; the sandbox needs the whole module set,
        #   and asserting that rather than assuming it is why the first seed run failed CLEAN. **
        import glob as _glob
        for f in _glob.glob(os.path.join(ROOT, 'corpus', '*.py')):
            open(os.path.join(td, 'corpus', os.path.basename(f)), 'w', encoding='utf-8').write(
                open(f, encoding='utf-8', errors='replace').read())
        # ** ⛔⛭ AND THE SANDBOX WAS BUILT FOR A ONE-RAIL GATE (r3976). **  The gate now surveys the
        # ** `\ldg` rail too, whose feeders are `corpus/ledgers_registry.md` and the `*_LEDGER.md`
        # ** files the rows name -- ** which live at the REPOSITORY ROOT and were never copied in **.
        # ** So the ledger rail found no feeder, refused to report a rail it had not measured, and
        # ** the CLEAN run exited 1 alongside the seeded one: `clean == seeded == 1`, a seed test
        # ** that discriminated nothing.
        # **   ⇒ *** THIRD FIXTURE IN THIS DEBT MISSING THE ROOT-LEVEL LEDGERS, after `L556/R1`. ***
        # **     A gate that grows a rail grows a fixture requirement, and nothing tells the
        # **     fixtures.  The clean baseline is asserted below rather than assumed.
        for _need in ('ledgers_registry.md',):
            _src = os.path.join(ROOT, 'corpus', _need)
            if os.path.exists(_src):
                open(os.path.join(td, 'corpus', _need), 'w', encoding='utf-8').write(
                    open(_src, encoding='utf-8', errors='replace').read())
        for _led in _glob.glob(os.path.join(ROOT, '*_LEDGER.md')):
            os.symlink(_led, os.path.join(td, os.path.basename(_led)))
        for fn in SURVEYED:
            d = os.path.dirname(os.path.join(td, fn))
            if d:
                os.makedirs(d, exist_ok=True)
        seeds = {}
        for name, payload in (('clean', 'a clean row with ⌗ and ★ only\n'),
                              ('seeded', 'a row reaching for ' + chr(0x1F4A1) + '\n')):
            for fn in SURVEYED:
                open(os.path.join(td, fn), 'w', encoding='utf-8').write(payload)
            r = subprocess.run([sys.executable,
                                os.path.join(td, 'corpus', 'check_glyph_coverage.py')],
                               cwd=td, capture_output=True, text=True, errors='replace',
                               timeout=600)
            seeds[name] = r.returncode
        # ** ⛭ AND THE CONTROL IS SEEDED TOO (r3976), because it no longer announces itself. **  The
        # ** gate's control asks the generator's OWN escape to refuse a glyph it cannot know and to
        # ** accept one it does: `refused(mod, chr(0x1F600)) and not refused(mod, rail['known'])`.
        # ** *** Neuter the escape so it refuses NOTHING and the gate must say the control did not
        # ** fire -- rather than reporting a clean sweep over glyphs it silently accepted. ***
        for fn in SURVEYED:
            open(os.path.join(td, fn), 'w', encoding='utf-8').write('a clean row with ⌗ only\n')
        _gen = os.path.join(td, 'corpus', 'make_receipt_appendix.py')
        _orig = open(_gen, encoding='utf-8', errors='replace').read()
        open(_gen, 'a', encoding='utf-8').write(
            '\n\n# seeded by L-270: an escape that refuses nothing\n'
            'def tex_escape(s, *a, **k):\n    return s\n')
        assert open(_gen, encoding='utf-8').read() != _orig, (
            'the seed must actually change the generator, or the control test is testing nothing')
        _neutered = subprocess.run(
            [sys.executable, os.path.join(td, 'corpus', 'check_glyph_coverage.py')],
            cwd=td, capture_output=True, text=True, errors='replace', timeout=600)
        seeds['no-control'] = _neutered.returncode
        seeds['no-control-said'] = 'the CONTROL did not fire' in _neutered.stdout
    check(f'⓹ᵈ SEEDED: with the generator\'s escape neutered so it refuses nothing, the gate exits '
          f'{seeds["no-control"]} and says the CONTROL did not fire ({seeds["no-control-said"]}) -- '
          f'so an import that silently stopped refusing cannot read as clean',
          seeds['no-control'] == 1 and seeds['no-control-said'])
    check(f'⓹ᵉ SEEDED BOTH WAYS: a document reaching for an untranslated glyph fails the gate '
          f'({seeds["seeded"]}), and the same documents without it pass ({seeds["clean"]}) -- so a '
          'green result is a measurement and not an empty set, and the clean baseline is GREEN '
          'rather than red on both rails',
          seeds['seeded'] == 1 and seeds['clean'] == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a translation table validated only against what it was asked to render')
    print('  carries its next failure already in the tree. **')
    print('  *The generator refused L-269\'s register row over one glyph, and behind it stood')
    print('  seventeen more, in a hundred and eighty-two occurrences, every one a build break')
    print('  scheduled for whenever a row happened to reach for it.*')
    print('  ⛔ ** And the first form of the repair restated the rule instead of running it, **')
    print('     flagging six Latin-1 characters the generator passes through -- so it would have')
    print('     drifted from the generator in whichever direction the copy drifted.  *The gate now')
    print('     calls the generator\'s own escape and has no threshold of its own.*')
    print('  ⌗ ** The loud refusal stays. **  *This gate is the early warning; the refusal is the')
    print('     backstop, and a table wide enough to swallow an unsurveyed glyph silently would be')
    print('     worse than a build that stops.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
