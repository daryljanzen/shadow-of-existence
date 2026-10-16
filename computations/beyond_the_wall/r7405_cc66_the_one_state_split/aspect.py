# ASPECT NET -- built FROM the ruled instance pre/post pair rather than from vocabulary.
# Both forms carry the debt word; what differs is the ASPECT of the discharge clause.
# BOUND ON ONE INSTANCE: it flags the pre-fix sentence and not the post-fix one.  That is a
# single case, so its false-negative rate is UNMEASURED and the 0 it returns over the 16 is
# exactly as strong as that one test and no stronger.
import re, os
ROOT='/home/user/shadow-of-existence'
# THIRD NET -- built FROM the ruled instance's pre/post pair, not from vocabulary.
# The two forms share their debt word; what differs is the ASPECT of the discharge clause.
DEBT   = re.compile(r'\b(qualification|caveat|check|question|item|debt|gap)\b[^.!?]{0,80}?'
                    r'\b(is|are|remains?)\s+owed\b|\b(is|are)\s+owed\b', re.I)
PROSP  = re.compile(r'\b(closing|paying|settling|answering|removing|discharging)\s+(it|this|that|them)\b'
                    r'|\bremains? to be\b|\bwill be (?:closed|answered|paid|settled)\b'
                    r'|\bonce (?:it|this|that) is (?:closed|answered|paid)\b', re.I)
DONE   = re.compile(r'\bis (?:closed|answered|discharged|settled|paid|already)\b'
                    r'|\bare (?:closed|answered|discharged|settled|paid)\b'
                    r'|\bis closed in this\b', re.I)
def hit(s):
    return bool(DEBT.search(s)) and bool(PROSP.search(s)) and not DONE.search(s)
def passage(path, key, exact=False):
    raw=open(path,encoding='utf-8',errors='replace').read().split('\n')
    inside=False; lines=[]
    for l in raw:
        m=re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', l)
        if m:
            if inside: break
            inside=any((key[:40] in t or t in key) for t in m); continue
        if inside and not l.lstrip().startswith('%'): lines.append(l)
    return re.sub(r'\s+',' ',' '.join(lines))
def scan(txt):
    return [s for s in re.split(r'(?<=[.!?])\s+',txt) if hit(s)]
print('=== BINDING TEST on the ruled instance (P15 amplitude floor)')
for label,path in (('PRE-FIX  (must flag)  ','/tmp/claude-0/prefix/CR_cosmology.tex'),
                   ('POST-FIX (must not)   ','corpus/CR_cosmology.tex')):
    h=scan(passage(path,'amplitude floor'))
    print('  %s -> %d flag(s)%s' % (label,len(h), '' if not h else ''))
    for s in h:
        m=DEBT.search(s); print('        …'+s[max(0,m.start()-60):m.start()+140].strip()+'…')
print()
FILE={'P9':'range_paper.tex','P11':'dynamics_paper.tex','P13':'boundary_paper.tex',
      'P15':'CR_cosmology.tex','P16':'cosmogenesis_paper.tex','P18':'CR_synthesis.tex'}
WANT={'12','18','21','23','24','25','26','27','29','30','31','35','36','38','39','40'}
rows=[]
with open(os.path.join(ROOT,'computations/beyond_the_wall/r7399_cc66_the_backlog_triage/classified.tsv'),encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'): continue
        p=line.rstrip('\n').split('\t')
        if len(p)>=4 and p[0] in WANT: rows.append(p)
print('=== THE 16, with the aspect net')
tot=0; seen={}
for p in rows:
    n,paper,section=p[0],p[1],p[2]
    txt=passage(os.path.join(ROOT,'corpus',FILE[paper]), section)
    h=scan(txt); tot+=len(h)
    dup=' [same passage as %s]'%seen[(paper,section)] if (paper,section) in seen else ''
    seen.setdefault((paper,section),n)
    print('  %-3s %-4s %-44s flags=%d%s' % (n,paper,section[:44],len(h),dup))
    for s in h:
        m=DEBT.search(s); print('        …'+s[max(0,m.start()-60):m.start()+140].strip()+'…')
print('TOTAL aspect-net flags across the 16:', tot)
print('distinct passages among the 16:', len(seen))
