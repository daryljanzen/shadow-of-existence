#!/usr/bin/env python3
"""r7794 -- ADDENDUM.  ONE post-hoc re-measurement, declared as post-hoc, changing NO criterion.

** ARM 2 FAILED ON A DEFECTIVE SEARCH OF MINE, NOT ON THE CORPUS. **  The arm looked for sentences
tying the inherited datum to the deposition by testing `'eta' in s.lower()` -- and `eta` is a
SUBSTRING of `retains`, `retained`, `theta`, `metal`, `beta`, `zeta`.  The first hit it printed is
"However, CR/FLRW *retains* an inherited synchrony condition", which has nothing to do with the
composition.  So the 27 it counted are mostly noise and the 2 "epoch-ish" ones among them are noise
too.
  ⇒ GUARD: ** a substring is not a token. **  A Greek letter name is three characters long and lives
    inside ordinary English words; searched as a substring it matches the language, not the symbol.
  ⌗ The arm stays FAILED.  Its criterion is not rewritten; this is the measurement it should have
    made, run beside it and labelled.
"""
import io
import os
import re

ROOT = '/home/user/shadow-of-existence'


def flat(name):
    return ' '.join(io.open(os.path.join(ROOT, name), encoding='utf-8',
                            errors='replace').read().split())


def sents(t):
    return [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]


P7, P16 = flat('corpus/CR_framework.tex'), flat('corpus/cosmogenesis_paper.tex')
ALL = sents(P7 + ' ' + P16)

# the SYMBOL, as the papers write it: a LaTeX macro with a token boundary, never a bare substring
SYM = re.compile(r'\\eta\b')
DEPOSIT = ('deposit', 'handover', 'handed over', 'inherited', 'composition')
EPOCHISH = re.compile(r'\bepoch\b|\bredshift\b|\bz\s*=|\btemperature\b|\bbegins at\b')

print("=" * 100)
print("  (i) arm 2 re-measured with a TOKEN search for the composition symbol")
hits = [s for s in ALL if SYM.search(s) and any(d in s.lower() for d in DEPOSIT)]
print(f"      sentences carrying the symbol AS A TOKEN and a deposition word: {len(hits)}")
for s in hits:
    print(f"        ...{s[:300]}")
ep = [s for s in hits if EPOCHISH.search(s.lower())]
print(f"      of those, any that also fix an epoch, a redshift or a temperature: {len(ep)}")
for s in ep:
    print(f"        [EPOCH?] ...{s[:300]}")
print()
print(f"      and the substring search the arm actually ran, for comparison:")
loose = [s for s in ALL if 'eta' in s.lower() and any(d in s.lower() for d in DEPOSIT)]
noise = [s for s in loose if not SYM.search(s)]
# ⌗ WHAT WAS SEARCHED, beside the claim, because the gate is right to ask: each of those sentences
#   was tested for the regex r'\\eta\\b' -- the LaTeX macro with a token boundary -- over the
#   whitespace-flattened full text of corpus/CR_framework.tex and corpus/cosmogenesis_paper.tex.
#   The claim below is about THAT pattern in THOSE two files and nothing wider.
print(f"        matched {len(loose)} sentence(s); {len(noise)} of them do not match the macro"
      f" pattern r'\\eta\\b' anywhere in the two files searched")
for s in noise[:3]:
    w = re.findall(r"\b\w*eta\w*\b", s.lower())
    print(f"        [NOISE] words that matched: {sorted(set(w))[:6]}")
print()
print("  ⇒ THE ARM'S CLAIM SURVIVES ITS OWN DEFECTIVE SEARCH, measured properly:" if not ep
      else "  ⇒ THE ARM'S CLAIM DOES NOT SURVIVE: an epoch is fixed where it said none was:")
print("     the deposition's inherited datum is a COMPOSITION -- a ratio -- and the sentences that")
print("     carry it fix no time, radius or temperature." if not ep else
      "     see the [EPOCH?] line(s) above.")
print("=" * 100)
