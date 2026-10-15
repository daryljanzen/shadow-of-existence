import re, os, json, sys
ROOT='/root/shadow-of-existence/corpus'
PAPERS=[('P1','BH_causality_v2'),('P2','janzen_circle_v3'),('P3','SdS-slicing-curve_v2'),('P4','modern_parallax'),('P5','groupoid_paper'),('P6','shadow_of_existence'),('P7','CR_framework'),('P8','slicing_operator'),('P9','range_paper'),('P10','canonical_time'),('P11','dynamics_paper'),('P12','algebroid_paper'),('P13','boundary_paper'),('P14','matter_sector_paper'),('P15','CR_cosmology'),('P16','cosmogenesis_paper'),('P17','geometric_core_paper'),('P18','CR_synthesis')]
PAT=re.compile(r"(remains? open|stays? open|left open|is open\b|are open\b|still open|open (?:question|problem|edge|item)s?|not yet|has not been|have not been|is not derived|not derived here|not computed|is owed|are owed|\bowed\b|outstanding|unresolved|unanswered|undetermined|undelivered|unbuilt|not built|remains to be|remain to be|future work|is not settled|not settled|we do not claim|we claim no|not claimed|conjectur|would settle|what would|is not fixed|not fixed by|frontier|we have not|does not yet|do not yet|cannot yet|is pending|is missing|are missing)",re.I)
def body(f):
    b='\n'.join(l for l in open(f,encoding='utf-8',errors='replace').read().split('\n') if not l.lstrip().startswith('%'))
    j=b.find('\\begin{thebibliography}')
    return b[:j] if j>0 else b
out=[]
for num,stem in PAPERS:
    t=body(os.path.join(ROOT,stem+'.tex'))
    # paragraphs
    paras=[p for p in re.split(r'\n\s*\n',t)]
    sec=''
    for i,p in enumerate(paras):
        m=re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}',p)
        if m: sec=m[-1]
        flat=re.sub(r'\s+',' ',p)
        hits=sorted(set(h.lower() for h in PAT.findall(flat)))
        if hits:
            out.append(dict(paper=num,stem=stem,para=i,section=sec,hits=hits,text=flat))
json.dump(out,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cands.json'),'w'),indent=0)
from collections import Counter
c=Counter(o['paper'] for o in out)
print(len(out)); print(c)
print(sum(len(o['text']) for o in out))
