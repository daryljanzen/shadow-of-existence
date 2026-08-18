import re, sys, os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
led=open(os.path.join(R,'THE_MODEL_LEDGER.md'),encoding='utf-8',errors='replace').read()
scan=os.path.join(R,'storyboard_receipts','RADSCAN.py')
if not os.path.exists(scan):
    print("  [FAIL] RADSCAN.py missing — the ledger describes an instrument that is gone"); sys.exit(1)
src=open(scan,encoding='utf-8',errors='replace').read()
sw=set(re.findall(r"_SW\('(\w+)'", src))
led_sw=set(re.findall(r"\*\*`(\w+)`\*\*\s*\|", led))
bad=[]
for s in sw-led_sw: bad.append(f"switch {s} exists in RADSCAN and is NOT in the ledger")
for s in led_sw-sw: bad.append(f"ledger names {s} which RADSCAN does not define")
for b in bad: print(f"    [FAIL] {b}")
if bad: sys.exit(1)
print(f"    [OK] model ledger: {len(sw)} switches, every one bound to a theory statement")
