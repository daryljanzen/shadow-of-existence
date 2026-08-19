import re, glob, os, sys
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ** a DEFERRAL says the thing is not done HERE.  It must either point somewhere,
#    or say plainly that it is open programme-wide.  "not claimed here" alone
#    implies a home the reader cannot find. **
PAT=re.compile(r'(not claimed here|not settled by this reading|not addressed here|not treated here|beyond the scope of this paper|left for future work)', re.I)
POINTS=re.compile(r'(\\S\\ref|\\cite|\\ref\{|companion|below|open problem|frontier|programme)', re.I)
bad=[]
for f in sorted(glob.glob(os.path.join(R,'corpus','*.tex'))):
    raw=open(f,encoding='utf-8',errors='replace').read()
    body=' '.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
    for m in PAT.finditer(body):
        ctx=body[max(0,m.start()-260):m.end()+520]
        if not POINTS.search(ctx):
            bad.append((os.path.basename(f), re.sub(r'\s+',' ',ctx)[:110]))
for f,c in bad: print(f"    [FAIL] {f}: deferral with no forward pointer\n           ...{c}...")
if bad: sys.exit(1)
print(f"    [OK] deferrals: every 'not done here' points somewhere or names its openness")
