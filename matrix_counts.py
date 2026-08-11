# Dependency-matrix citation counter (r895, G9). Handles p0/17's alternate cite labels.
import re, os
papers=[('JanzenBHcausality','BH_causality_v2.tex','P1 \\; wedge'),('JanzenCircle','janzen_circle_v3.tex','P2 \\; circle'),
('JanzenSlicing','SdS-slicing-curve_v2.tex','P3 \\; slicing'),('JanzenModernParallax','modern_parallax.tex','P4 \\; mod.\\ parallax'),
('JanzenGroupoid','groupoid_paper.tex','P5 \\; groupoid'),('JanzenShadowExistence','shadow_of_existence.tex','P6 \\; shadow'),
('JanzenCRframework','CR_framework.tex','\\textbf{P7 \\; framework}'),('JanzenOperator','slicing_operator.tex','P8 \\; operator'),
('JanzenRange','range_paper.tex','P9 \\; range'),('JanzenCanonicalTime','canonical_time.tex','P10 \\; canon.\\ time'),
('JanzenDynamics','dynamics_paper.tex','P11 \\; dynamics'),('JanzenAlgebroid','algebroid_paper.tex','P12 \\; algebroid'),
('JanzenBoundary','boundary_paper.tex','P13 \\; boundary'),('JanzenMatter','matter_sector_paper.tex','P14 \\; matter'),
('JanzenCRcosmology','CR_cosmology.tex','P15 \\; cosmology'),('JanzenCosmogenesis','cosmogenesis_paper.tex','P16 \\; cosmogenesis'),
('JanzenGeometricCore','geometric_core_paper.tex','\\textbf{p0 \\; core}')]
labels=[p[0] for p in papers]
# p0/17's alternate labels -> canonical
alias={'JanzenCausality':'JanzenBHcausality','JanzenParallax':'JanzenModernParallax','JanzenShadow':'JanzenShadowExistence',
'JanzenFramework':'JanzenCRframework','JanzenCanonical':'JanzenCanonicalTime','JanzenCosmology':'JanzenCRcosmology'}
def cites(fn):
    if not os.path.exists('corpus/'+fn): return ''
    s=re.split(r'\\begin\{thebibliography\}',open('corpus/'+fn,encoding='utf-8',errors='ignore').read())[0]
    toks=[]
    for grp in re.findall(r'\\cite[tp]?\{([^}]*)\}',s):
        for t in grp.split(','):
            t=t.strip(); toks.append(alias.get(t,t))
    return ' '.join(toks)
def count(cs,t):
    return len(re.findall(r'(?<![A-Za-z])'+re.escape(t)+r'(?![A-Za-z])',cs))
M={lab:{} for lab,_,_ in papers}
for lab,fn,sh in papers:
    cs=cites(fn)
    for t in labels: M[lab][t]=count(cs,t)
if __name__=='__main__':
    for lab,fn,sh in papers:
        row=re.sub(r'\\.*','',sh).strip()[:5].ljust(6)
        for t in labels: v=M[lab][t]; row+=f'{("--" if t==lab else (str(v) if v else ".")):>4}'
        print(row)
