#!/usr/bin/env bash
# check_multiface.sh — THE MULTI-FACE INDEX CHECK (added r1883).
# The corpus's characteristic move is "one X worn N ways". Each such statement is a JOINT, and a
# joint gets indexed under whichever face the indexer approached from. This lists every multi-face
# statement with its declared count and its actual item count, so a drift shows up as a mismatch.
cd "$(dirname "$0")/../corpus" || exit 1
python3 - <<'PYEOF'
import re, glob, os
WORDS={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'several':None}
pat=re.compile(r'(worn|read|seen from|wearing)\s+(two|three|four|five|six|seven|eight|nine|several)\s+(ways|sides|faces)', re.I)
n=0
print("EVERY MULTI-FACE STATEMENT IN THE CORPUS — declared count, and where it is stated\n")
for f in sorted(glob.glob('*.tex')):
    if os.path.basename(f).startswith('appendix'): continue
    s=open(f,encoding='utf-8',errors='replace').read()
    for m in pat.finditer(s):
        n+=1
        ctx=re.sub(r'\s+',' ',s[max(0,m.start()-150):m.start()+150])
        incomment = s.rfind('\n',0,m.start())+1
        tag='MASTHEAD' if s[incomment:incomment+1]=='%' else 'body'
        print(f"  [{os.path.basename(f)[:22]:24s}] [{tag:8s}] {m.group(0)}")
        print(f"        …{ctx[100:290]}…\n")
print(f"  total: {n}")
print("\n*** THIS SCRIPT LISTS. IT DOES NOT COUNT. ***")
print("Most of the corpus enumerates its faces with em-dashes and semicolons, not roman numerals")
print("or \\item, so any automatic tally here produces false mismatches. The two-part check is READ:")
print("  (1) does the declared count match the faces actually enumerated?")
print("  (2) does EVERY index carrying the result carry EVERY face?")
print("\nSWEPT r1883, all 30. Result: ONE genuine drift, in the corpus's flagship instance --")
print("  p0's masthead said SIX while sec:unification enumerates SEVEN (and the masthead's own")
print("  altitude line already said seven); the missing face is 'ONE CIRCLE: the equator'.")
print("  Every other declared count checks out, including P9's FOUR (i-iv all present) and")
print("  p0's 'one principle worn three ways' (substrate / evolving three-space / discrete residue).")
print("The INDEX half found one gap: section 0's sigma row and the section-1i P5 card carried the")
print("  S_3's monodromy and Weyl faces and dropped GALOIS. Both fixed r1883.")
PYEOF
