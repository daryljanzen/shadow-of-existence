#!/usr/bin/env python3
"""
P7's FRONTIER SECTION, CHECKED AGAINST THE REGISTER — and the check reads the paper rather than a
list typed into the check.

The previous instrument (`P07_frontier_and_synthesis_audit.py`, c54.83) hardcoded the seven items it
was written against and asserted a defect that has since been repaired.  ** It therefore fails on the
current tree for the best possible reason, and its failure is the same base rate one level up: an
instrument fitted to the state it was built in goes stale exactly like the prose it polices. **  This
one parses.

  PART 1  ** THE ITEMS, PARSED FROM THE PAPER. **
  PART 2  ** THE LEAD-IN'S ARITHMETIC AGAINST THE LIST'S OWN LENGTH. **
  PART 3  ** EACH ITEM AGAINST THE REGISTER: struck, open, or unregistered. **
  PART 4  What the section owes.

Run: python3 P07_frontier_currency.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

t = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'), encoding='utf-8',
         errors='replace').read()
t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
m = re.search(r'\\section\{[^}]*\}\\label\{sec:frontiers\}', t)
j = m.start()
# slice to the END OF THE ENUMERATE, not to a fixed window: this section runs past any
# window one would guess, and a truncated slice silently drops its last items.
_e = t.find(r'\end{enumerate}', t.find(r'\begin{enumerate}', j))
assert _e > j, "the frontier enumerate was not found"
SEC = t[j:_e + len(r'\end{enumerate}')]
ARC = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8').read()

# =====================================================================
print("=" * 78)
print("PART 1 — THE ITEMS, PARSED FROM THE PAPER")
print("=" * 78)
def _titles(seg):
    """\item \emph{...} with BRACE BALANCING -- a title containing a nested group is still a title,
    and a naive [^}]* silently drops the item."""
    out = []
    # ** an OPTIONAL \label between \item and \emph: c54.118 labelled the items so the clues ledger
    # could address them by name instead of by ordinal, and the naive pattern then matched NOTHING
    # and the assert below fired.  Which is the pattern working: a parser that silently returns
    # zero items would have reported the section empty and clean. **
    for mm in re.finditer(r'\\item\s*(?:\\label\{[^}]*\})?\s*\\emph\{', seg):
        i, d = mm.end(), 1
        while i < len(seg) and d:
            if seg[i] == '{' and seg[i-1] != '\\':
                d += 1
            elif seg[i] == '}' and seg[i-1] != '\\':
                d -= 1
            i += 1
        out.append(seg[mm.end():i-1])
    return out


items = _titles(SEC)
print(f"  the enumerate carries {len(items)} items:")
for k, it in enumerate(items, 1):
    print(f"    {k}. {it}")
assert items

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE LEAD-IN'S ARITHMETIC")
print("=" * 78)
lead = SEC[:SEC.find(r'\begin{enumerate}')]
claim = re.search(r'it opened at (\w+) and stands at (\w+)', lead)
WORD = {'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8}
if claim:
    opened, stands = WORD[claim.group(1)], WORD[claim.group(2)]
    print(f"  the lead-in says: opened at {opened}, stands at {stands}")
    print(f"  the enumerate actually carries: ** {len(items)} **")
    ok = (stands == len(items))
    print(f"  ** do they agree?  {ok} **")
    if not ok:
        print(f"  ⛔ ** THE STATED COUNT IS {stands} AND THE LIST IS {len(items)}. "
              f"The lead-in is stale by {stands - len(items)}. **")
else:
    print("  the lead-in states no count")
    ok = None
print()
for s in [
 "⌗ *A frontier list's own count is the one number a reader checks first, and it is the number a",
 "node editing the list forgets last.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — EACH ITEM AGAINST THE REGISTER")
print("=" * 78)
# item -> the register rows that own its content
OWNS = {
 'matter branch-point crossing':      [('L-138', 'A·4')],
 'Inherited boundary data':           [('L-150', 'F·1')],
 'classification of causal reassign': [('L-141', 'C·5'), ('L-138', 'A·4')],
 'scalar perturbation sector':        [('L-146', 'E·1'), ('L-147', 'E·2'), ('L-148', 'E·3')],
 'Standard-Model fermion and gauge':  [('L-164', 'A·5')],   # registered c54.115, by this check
 'quantum sector':                    [('L-165', 'B·1')],   # registered c54.116, by this check
}


def status(lid):
    if re.search(r'\|\s*~~%s~~\s*\|' % re.escape(lid), ARC):
        mm = re.search(r'\|\s*~~%s~~\s*\|.*?\*\*STRUCK ([^*]+)\*\*' % re.escape(lid), ARC)
        return 'STRUCK ' + (mm.group(1).strip() if mm else '?')
    if re.search(r'\|\s*\*\*%s\*\*\s*\|' % re.escape(lid), ARC):
        return 'OPEN'
    return 'not in the register'


print(f"  {'#':>2} {'item':>44} {'owns':>16} {'register':>22}")
rows = []
for k, it in enumerate(items, 1):
    key = next((kk for kk in OWNS if kk.lower() in it.lower()), None)
    leads = OWNS.get(key, None)
    if leads is None:
        rows.append((k, it, '?', '** UNMAPPED **'))
        print(f"  {k:>2} {it:>44} {'?':>16} {'** UNMAPPED **':>22}")
        continue
    if not leads:
        rows.append((k, it, '(A·5)', 'never registered'))
        print(f"  {k:>2} {it:>44} {'(A·5)':>16} {'never registered':>22}")
        continue
    sts = [(lid, nm, status(lid)) for lid, nm in leads]
    tag = ' · '.join(f"{nm}:{s.split()[0]}" for _, nm, s in sts)
    allstruck = all(s.startswith('STRUCK') for _, _, s in sts)
    rows.append((k, it, ' '.join(nm for _, nm in leads),
                 '** ALL STRUCK **' if allstruck else tag))
    print(f"  {k:>2} {it:>44} {' '.join(nm for _, nm in leads):>16} "
          f"{('** ALL STRUCK **' if allstruck else tag):>22}")
print()
fully = [r for r in rows if 'ALL STRUCK' in r[3]]
print(f"  ** {len(fully)} of {len(items)} items are owned entirely by STRUCK register rows. **")
for k, it, ow, _ in fully:
    print(f"     item {k}: {it}  ({ow})")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE SECTION OWES")
print("=" * 78)
for s in [
 "⌗ ** THE SECTION'S OWN STANDARD, STATED IN ITS LEAD-IN, IS THE RIGHT ONE: ** *'Where an item has",
 "   been overtaken, the item says so and says by what, since a frontier list whose entries quietly",
 "   empty is worse than none: a reader uses it to choose what to work.'*",
 "",
 "⇒ ** SO THE OWED WORK IS NOT DELETION.  It is (i) the count in the lead-in brought to the list's",
 "   actual length, and (ii) any item whose register rows are ALL struck moved below the list with",
 "   its resolution named -- the treatment item seven already received and which the section",
 "   describes as its own practice. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE CLUES LEDGER'S ADDRESSES INTO THIS LIST  (added c54.118)")
print("=" * 78)
# ** THE_OPEN_PROBLEMS_LEDGER addresses each family's HOME to a P7 frontier item.  It did so by
# ORDINAL, and this list ran seven -> six -> four, so five of eight families were pointing at the
# wrong item -- put there by the revision that shrank the list and did not propagate.  An ordinal
# into a shrinking list is a guaranteed-stale address; a \label is not. **
LED = open(os.path.join(ROOT, 'THE_OPEN_PROBLEMS_LEDGER.md'), encoding='utf-8').read()
ordinals = re.findall(r'HOME:\s*P7 `sec:frontiers` item (\d+)', LED)
labelled = re.findall(r'HOME:\s*P7 `sec:frontiers` \\ref\{(frontier:[a-z]+)\}', LED)
inpaper = set(re.findall(r'\\label\{(frontier:[a-z]+)\}', SEC))
print(f"  ledger HOMEs addressed by ORDINAL : {len(ordinals)}  {ordinals}")
print(f"  ledger HOMEs addressed by LABEL   : {len(labelled)}  {labelled}")
print(f"  labels actually in P7's enumerate : {len(inpaper)}  {sorted(inpaper)}")
dead = [l for l in labelled if l not in inpaper]
print(f"  ** ledger labels with no matching \\label in the paper: {dead} **")
assert not dead, dead
if ordinals:
    print(f"  ⛔ ** {len(ordinals)} HOME(s) STILL ADDRESSED BY ORDINAL — each will go stale the next "
          f"time this list changes length. **")
else:
    print("  ** No ledger HOME addresses this list by ordinal. **")
assert not ordinals, ordinals
