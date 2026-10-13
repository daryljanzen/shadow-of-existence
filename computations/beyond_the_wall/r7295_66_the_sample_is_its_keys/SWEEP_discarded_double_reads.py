import subprocess, collections, json, sys
def g(*a):
    return subprocess.run(['git']+list(a), capture_output=True, text=True, cwd='/home/claude/shadow-of-existence').stdout
TSV='corpus/quote_pin_baseline.tsv'
def load(ref):
    out=g('show', ref+':'+TSV)
    d={}
    for l in out.split('\n'):
        if not l.strip() or l.startswith('#'): continue
        r=l.split('\t')
        if len(r)>6: d[(r[0],r[1])]=(r[5],r[6])
    return d
OPEN={'UNADJUDICATED','UNADJUDICATED-PINNED','UNADJUDICATED-LIST'}
merges=[x for x in g('log','--merges','--format=%H %P','-400').split('\n') if x.strip()]
found=[]
for line in merges:
    p=line.split()
    if len(p)!=3: continue
    m,p1,p2=p
    # did the merge discard p2's ledger?
    if not g('diff','--numstat',p2,m,'--',TSV).strip(): continue   # p2 side kept
    if g('diff','--numstat',p1,m,'--',TSV).strip(): continue       # merge changed trunk side too -> not a wholesale take
    A=load(p2); B=load(m)
    hits=[]
    for k,(va,na) in A.items():
        if k not in B: continue
        vb,nb=B[k]
        if va in OPEN or vb in OPEN: continue
        if va==vb: 
            hits.append((k,va,vb,na,nb,True)); continue
        hits.append((k,va,vb,na,nb,False))
    # only rows where the two sides were authored by different seats
    def seat(n):
        for s in ('cc66','+69','+60','+70','+71','+66'):
            if s in n: return s
        return '?'
    cross=[h for h in hits if seat(h[3])!=seat(h[4]) and seat(h[3])!='?' and seat(h[4])!='?']
    if cross:
        ag=sum(1 for h in cross if h[5])
        found.append((m[:9], g('log','-1','--format=%s',m).strip()[:60], len(cross), ag, collections.Counter((seat(h[3]),seat(h[4])) for h in cross)))
        json.dump([[h[0][0],h[0][1],h[1],h[2],seat(h[3]),seat(h[4])] for h in cross], open('/tmp/claude-0/sc/cross_%s.json'%m[:9],'w'))
for f in found:
    print(f[0], f'cross={f[2]:4d} agree={f[3]:4d} {100*f[3]/f[2]:5.1f}%', dict(f[4]), f[1])
print('TOTAL merges with discarded cross-verdicts:', len(found))
