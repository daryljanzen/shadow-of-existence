#!/usr/bin/env python3
"""DRAFT — the fourth gate of the family: does the cited receipt COMPUTE the number beside it?

check_receipts.py verifies that every \\rcpt{} resolves to an INDEX row and a file on disk, and
that a receipts/ copy has not drifted from its ORIGIN.  ** It cannot see whether the receipt the
citation points at actually produces the number standing next to it in the prose. **  P16's
displayed abundance equation is the instance: four correct numbers, produced by the SIBLING
receipt, cited to the one that returns different ones (F06).

METHOD.  Run every receipt once and cache stdout (expensive: ~40 min for the 249, so this is a
per-major-revision tool, not a per-turn one).  Then for each \\rcpt{} in the papers, take the
prose window before it, pull the numeric literals, and check each against the cited receipt's
output AT THE QUOTED PRECISION AND AT ANY POWER OF TEN -- so 5.7 matches 5.68e-14 and 145.7
matches 145.72 Mpc.

HONEST BOUND, and it is the reason this ships as a REPORT and not as a FAILING GATE.  Across ~250
citations it flags 15.  Triaged by hand, fourteen are context bleed -- a number from an adjacent
sentence that has nothing to do with the receipt -- or a number the receipt takes as INPUT rather
than printing.  One is real.  ** A 1-in-15 signal is worth one pass per major revision and is not
worth wiring into the ten-gate suite until the prose window is bounded by the SENTENCE rather than
by a character count. **  Improving that is the whole of what stands between this and a gate.

USAGE:
    python3 capture_receipt_output.py          # writes the stdout cache
    python3 DRAFT_check_numbers_at_citations.py
"""
import re, os, json, sys
ROOT='/root/work'; CORPUS=os.path.join(ROOT,'corpus')
out=json.load(open('/tmp/rcpt_out/all.json'))
amap={}
for f in os.listdir(CORPUS):
    if not f.startswith('appendix_receipts'): continue
    t=open(os.path.join(CORPUS,f),encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'\\label\{rcpt:([^}]+)\}(.*?)\\emph\{Run:\}\s*\\texttt\{python3\s+receipts/([^}]+?)\}', t, re.S):
        amap[m.group(1)]=m.group(3).replace('\\_','_')

OUTNUM=re.compile(r'-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?')
def outvals(s):
    v=set()
    for m in OUTNUM.finditer(s):
        try: v.add(abs(float(m.group(0))))
        except: pass
    return sorted(v)

TEXNUM=re.compile(r'(?<![\w.\\])(\d+(?:\.\d+)?)(?![\w])')
def clean(s):
    s=re.sub(r'\\cite[a-z]*\{[^}]*\}',' ',s)
    s=re.sub(r'\\(ref|eqref|autoref|label|rcpt)\{[^}]*\}',' ',s)
    return s.replace('~',' ')

def matches(v, vals):
    """v quoted with k decimals; accept any output value agreeing to that precision,
       at any power of ten (the paper may quote 5.7 for 5.68e-14, or 145.7 Mpc)."""
    s=v; dec=len(s.split('.')[1]) if '.' in s else 0
    x=float(v)
    if x==0: return True
    import math
    for y in vals:
        if y==0: continue
        for scale in range(-25,26):
            z=y*(10.0**scale)
            if abs(z)<1e-12 or abs(z)>1e12: continue
            if abs(round(z,dec)-x) < 0.5*10**(-dec)+1e-12:
                # require same significant digits, not a coincidence of magnitude
                if abs(z-x) <= max(0.5*10**(-dec), abs(x)*1e-9):
                    return True
    return False

rows=[]
for f in sorted(os.listdir(CORPUS)):
    if not f.endswith('.tex') or f.startswith('appendix_receipts'): continue
    t=open(os.path.join(CORPUS,f),encoding='utf-8',errors='replace').read()
    t='\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', t):
        name=m.group(1); path=amap.get(name)
        o=out.get(path) if path else None
        if o is None and path:
            c=[k for k in out if os.path.basename(k)==os.path.basename(path)]
            o=out[c[0]] if c else None
        if o is None: rows.append((f,name,'NO OUTPUT',[])); continue
        vals=outvals(o)
        ctx=clean(t[max(0,m.start()-350):m.start()])[-350:]
        nums={x.group(1) for x in TEXNUM.finditer(ctx)}
        miss=[v for v in sorted(nums)
              if not re.fullmatch(r'(19|20)\d\d',v) and len(v.replace('.',''))>=2
              and not matches(v,vals)]
        if miss: rows.append((f,name,'MISS',miss))
print(f"{'paper':<24} {'receipt':<38} detail")
for f,name,kind,miss in rows:
    print(f"{f:<24} {name[:37]:<38} {kind}: {miss}")
print(f"\nflagged {len(rows)} of the corpus's \\rcpt citations")
