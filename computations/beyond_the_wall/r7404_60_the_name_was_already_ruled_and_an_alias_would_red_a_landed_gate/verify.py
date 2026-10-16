#!/usr/bin/env python3
"""r7404 (60) -- THE NAME WAS ALREADY RULED, AND THE ALIAS THE RULING ASKS FOR WOULD RED A LANDED GATE.

⛔ THIS IS A VERIFICATION AND NOT A SCORED REVISION, and it says so rather than dressing a grep as a
prediction: `r7403` ② rules a decision whose premise -- *both names are in the tree right now* -- is
checkable in one pass, and nothing here was unknown enough to band.  Every figure below is a count over
named files at `HEAD`, printed with its role, so the ruling can be re-aimed rather than argued with.

THE RULING: *standardise on `WBH2`; make both readers accept EITHER name, preferring `WBH2`, and leave
`CROMBH2` in place as a deprecated alias so no banked run stops reproducing.*

WHAT THIS MEASURES, in three parts:
  ① whether either name is a LIVE KNOB in the instrument the arms actually run;
  ② what role every remaining occurrence of the deprecated name plays -- knob, assertion, or prose;
  ③ whether a gate already landed on this branch ASSERTS the deprecated name's absence, which is what
    decides whether "deprecated is not excised" can be implemented at all.

    python3 -I verify.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
INSTR = os.path.join('computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
CANON, DEPRECATED = 'WBH2', 'CROMBH2'
# the receipt whose check asserts the deprecated name is ABSENT from the instrument
ASSERTER = ('receipts/P15_CR_cosmology/P15_the_likelihood_pair_is_another_instruments_and_the_crossing'
            '_run_needed_a_missing_knob.py')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def text(rel):
    p = os.path.join(ROOT, rel)
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


head = git('rev-parse', 'HEAD').strip()
instr = text(INSTR)
print(f'# r7404 (60) -- the name, verified at HEAD {head[:12]}')
print(f'# the instrument the arms run: {INSTR}')

# ── ① the live knob ───────────────────────────────────────────────────────────────────────────────
reads = {n: re.findall(r"os\.environ\.get\(\s*'" + n + r"'", instr) for n in (CANON, DEPRECATED)}
print()
print(f'# ① LIVE KNOB in the instrument')
for n in (CANON, DEPRECATED):
    print(f'#    {n:9} occurrences {instr.count(n):2d}, '
          f'`os.environ.get` reads {len(reads[n])}')
print(f'#    ⇒ the canonical name is read {len(reads[CANON])} time(s) and the deprecated name '
      f'{len(reads[DEPRECATED])}.')
print('#      ⛔ SO THE PREMISE "both names are in the tree right now" IS TRUE OF PROSE AND FALSE OF')
print('#        THE INSTRUMENT: there is one knob, and it already carries the ruled name.')

# ── ② what every remaining occurrence actually is ─────────────────────────────────────────────────
print()
print(f'# ② every remaining occurrence of {DEPRECATED}, by file and role')
rows = []
for f in git('ls-files').split('\n'):
    if not f or f.endswith(('.pdf', '.png')):
        continue
    t = text(f)
    if DEPRECATED not in t:
        continue
    knob = len(re.findall(r"os\.environ\.get\(\s*'" + DEPRECATED + r"'", t))
    asserted = len([1 for ln in t.split('\n')
                    if DEPRECATED in ln and re.search(r"\bnot in\b|\bin \w*INSTR|check\(|gate\(", ln)])
    rows.append((f, t.count(DEPRECATED), knob, asserted))
for f, n, knob, asserted in sorted(rows):
    role = 'LIVE KNOB' if knob else ('ASSERTED ABSENT' if asserted else 'PROSE / HISTORY')
    print(f'#    {n:3d}  knob={knob}  asserted={asserted}  {role:16}  {f}')
print(f'#    ⇒ {sum(1 for r in rows if r[2])} file(s) read it as a knob; '
      f'{sum(1 for r in rows if not r[2] and r[3])} assert its ABSENCE; the rest record the decision.')

# ── ③ the gate that decides whether the alias is implementable ────────────────────────────────────
print()
a = text(ASSERTER)
pat = f"'{DEPRECATED}' not in INSTR"
print(f'# ③ the landed gate: {pat!r} in {os.path.basename(ASSERTER)[:60]}: {pat in a}')
print(f'#    and the canonical read it asserts: '
      f'{chr(34)}OMBH2 = float(os.environ.get({chr(39)}{CANON}{chr(39)}, OMBH2)){chr(34)} in _CRBLK -> '
      f'{"OMBH2 = float(os.environ.get(" + chr(39) + CANON + chr(39) + ", OMBH2))" in a}')
print('#    ⇒ ⛔ RE-EXPOSING THE DEPRECATED NAME AS AN ALIAS WOULD TURN THAT CHECK RED, and the check')
print('#      is this seat\'s, landed, and asserts exactly what the earlier ruling decided:')
print('#      r6786 (FOR_60 ①) ruled the name "dropped, NOT aliased".  So the two rulings disagree,')
print('#      and the disagreement is the finding rather than the edit.')
