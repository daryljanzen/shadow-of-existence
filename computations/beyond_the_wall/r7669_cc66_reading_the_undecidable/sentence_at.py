import re, sys
TEX=open('corpus/CR_cosmology.tex',encoding='utf-8',errors='replace').read()

def sentence_at(pos):
    """the LaTeX sentence containing TEX[pos], bounded by a period that is not inside
    braces or math, and extended forward past any trailing \\rcpt{...}\\ldg{...} run."""
    def depth_at(i):
        d=0; m=False
        for ch in TEX[:i]:
            if ch=='{': d+=1
            elif ch=='}': d-=1
            elif ch=='$': m=not m
        return d,m
    # backward: nearest '. ' or '.\n' at brace depth 0 and outside math
    i=pos
    while i>0:
        i=max(TEX.rfind('. ',0,i), TEX.rfind('.\n',0,i))
        if i<=0: return 0,None
        d,m=depth_at(i)
        if d==0 and not m: start=i+2; break
        # keep looking further back
    else:
        start=0
    # forward: first '. ' / '.\n' at depth 0 outside math, AFTER the citation run ends
    j=pos
    while True:
        k=min([x for x in (TEX.find('. ',j), TEX.find('.\n',j)) if x!=-1] or [len(TEX)])
        if k>=len(TEX): return start,len(TEX)
        d,m=depth_at(k)
        if d==0 and not m: return start,k+1
        j=k+2

base=sys.argv[1]
pat='\\rcpt{'+base+'}'
WS=re.compile(r'\s+')
for m in re.finditer(re.escape(pat), TEX):
    ln=TEX[:m.start()].count('\n')+1
    a,b=sentence_at(m.start())
    s=WS.sub(' ',TEX[a:b]).strip()
    ok = pat in TEX[a:b]
    print("line %d  contains-its-own-citation=%s" % (ln, ok))
    print("   "+s[:520])
    print()
