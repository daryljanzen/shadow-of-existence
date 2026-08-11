"""
BBN rate-sensitivity scan: alpha_i = d ln(abundance) / d ln(rate_i) for each key reaction,
by perturbing that reaction (both directions) by +15% and re-running the network at eta10=6.14.
Ranks which reactions control D/H, 3He/H and 7Li/H -- the map for the precision upgrade and the
theory-error budget.
"""
import numpy as np, sys
import bbn_network as B

n,p,d,t,he3,he4,li7,be7 = (0,1),(1,1),(1,2),(1,3),(2,3),(2,4),(3,7),(4,7)
REACTIONS = [
 ("p(n,g)d",        [n,p],   [d]),
 ("d(p,g)3He",      [p,d],   [he3]),
 ("d(d,n)3He",      [d,d],   [n,he3]),
 ("d(d,p)t",        [d,d],   [p,t]),
 ("t(d,n)4He",      [d,t],   [n,he4]),
 ("3He(d,p)4He",    [d,he3], [p,he4]),
 ("3He(n,p)t",      [n,he3], [p,t]),
 ("3He(a,g)7Be",    [he3,he4],[be7]),
 ("t(a,g)7Li",      [t,he4], [li7]),
 ("7Be(n,p)7Li",    [n,be7], [p,li7]),
 ("7Li(p,a)4He",    [p,li7], [he4,he4]),
]
S=1.15; lnS=np.log(S)

def abun(o): return dict(Yp=o['Yp'],DH=o['DH'],He3H=o['He3H'],Li7H=o['Li7H'])

print("baseline...", flush=True)
base=abun(B.run(eta10=6.14, verbose=False))
print(f"  Yp={base['Yp']:.4f} D/H={base['DH']:.3e} 3He/H={base['He3H']:.3e} 7Li/H={base['Li7H']:.3e}\n", flush=True)
print(f"{'reaction':16s} {'a(D/H)':>8s} {'a(3He/H)':>9s} {'a(7Li/H)':>9s} {'a(Yp)':>8s}", flush=True)
print("-"*54, flush=True)

rows=[]
for name,reac,prod in REACTIONS:
    sc=[{'reac':reac,'prod':prod,'factor':S}]
    o=abun(B.run(eta10=6.14, verbose=False, scales=sc))
    aD =np.log(o['DH']/base['DH'])/lnS
    aHe=np.log(o['He3H']/base['He3H'])/lnS
    aLi=np.log(o['Li7H']/base['Li7H'])/lnS
    aYp=np.log(o['Yp']/base['Yp'])/lnS
    rows.append((name,aD,aHe,aLi,aYp))
    print(f"{name:16s} {aD:8.2f} {aHe:9.2f} {aLi:9.2f} {aYp:8.3f}", flush=True)

print("\nTop drivers:")
for lab,k in [('D/H',1),('3He/H',2),('7Li/H',3)]:
    top=sorted(rows,key=lambda r:-abs(r[k]))[:3]
    print(f"  {lab:6s}: "+", ".join(f"{r[0]}({r[k]:+.2f})" for r in top))
