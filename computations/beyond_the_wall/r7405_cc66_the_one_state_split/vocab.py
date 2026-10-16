# VOCABULARY NET -- debt language in the referenced passage.  IT DOES NOT DISCRIMINATE:
# it matches the ruled instance AND its fix identically (2 fragments each).  Its job is to
# SURFACE sentences for reading, never to score the class.  See aspect.py for the one that does.
import re, sys, os, csv
ROOT='/home/user/shadow-of-existence'
FILE={'P9':'range_paper.tex','P11':'dynamics_paper.tex','P13':'boundary_paper.tex',
      'P15':'CR_cosmology.tex','P16':'cosmogenesis_paper.tex','P18':'CR_synthesis.tex'}
WANT={'12','18','21','23','24','25','26','27','29','30','31','35','36','38','39','40'}
rows=[]
with open(os.path.join(ROOT,'computations/beyond_the_wall/r7399_cc66_the_backlog_triage/classified.tsv'),encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'): continue
        p=line.rstrip('\n').split('\t')
        if len(p)>=4 and p[0] in WANT: rows.append(p)
# DEBT language: a sentence asserting something is owed / qualified / outstanding
DEBT=re.compile(r'\b(is owed|are owed|owed|qualification|caveat|must first|remains to be|'
                r'not yet|have not been|is not yet|outstanding|pending|we do not yet|'
                r'is required before|before (?:this|that|it) can)\b', re.I)
def body(path, title):
    raw=open(path,encoding='utf-8',errors='replace').read().split('\n')
    out=[]; inside=False
    for i,l in enumerate(raw):
        m=re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', l)
        if m:
            inside = any(title[:40] in t or t in title for t in m)
            if inside: start=i+1
            continue
        if inside and not l.lstrip().startswith('%'):
            out.append((i+1,l))
    return out
def sents(lines):
    txt=' '.join(l for _,l in lines)
    txt=re.sub(r'\s+',' ',txt)
    return re.split(r'(?<=[.!?])\s+', txt)
print('n\tpaper\tsection\tdebt-sentences')
for p in rows:
    n,paper,section=p[0],p[1],p[2]
    path=os.path.join(ROOT,'corpus',FILE[paper])
    lines=body(path, section)
    hits=[s for s in sents(lines) if DEBT.search(s)]
    print('%s\t%s\t%s\tlines=%d debt=%d' % (n,paper,section[:46],len(lines),len(hits)))
    for h in hits[:4]:
        print('      · '+re.sub(r'\\[a-zA-Z]+\*?(\{[^}]*\})?',' ',h)[:300].strip())
