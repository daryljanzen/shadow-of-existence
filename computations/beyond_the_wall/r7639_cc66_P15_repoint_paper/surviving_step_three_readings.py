"""READ-ONLY: the surviving_step receipt's amplitude/phase decomposition on three readings.

Validated against the receipt's own printed namesake row before the other two are believed.
"""
import os, sys, numpy as np
ROOT='/home/user/shadow-of-existence'
SP=os.path.join(ROOT,'computations','beyond_the_wall','spectra')
sys.path.insert(0,os.path.join(ROOT,'computations','beyond_the_wall','r7637_70_own_comb_statistic'))
import own_comb as OC

QE=np.asarray(np.load(os.path.join(SP,'r6959_eta_cr.npz'))['q_edges'],float)
QC=0.5*(QE[:-1]+QE[1:]); PCOMB=1.0
BASES=(('v ~ q',1,False),('v ~ q2',2,False),('ln v ~ q',1,True),('ln v ~ q2',2,True))

def fine(tag):
    d=np.load(os.path.join(SP,tag+'.npz'))
    return d['ls'].astype(float)/float(d['l_A']), np.asarray(d['Dl'],float)
def env_a(x,y,win=1.0):
    e=np.empty_like(y,dtype=float)
    for j,v in enumerate(x):
        m=(x>=v-win/2)&(x<=v+win/2); e[j]=np.mean(y[m])
    return e
def osc(q,y,win=1.0):
    e=env_a(q,y,win); return (y-e)/e
def departure(v,p,lg):
    y=np.log(v) if lg else np.asarray(v,float)
    s_,i_=np.polyfit(QC[1:]**p,y[1:],1); pred=s_*QC**p+i_
    f=(np.exp(y-pred)-1.0) if lg else (y/pred-1.0)
    rms=float(np.sqrt(np.mean(f[1:]**2)))
    return float(f[0]),rms,float(f[0])/rms
def dep4(v): return [departure(v,p,lg) for _,p,lg in BASES]
def loc_fit(q,y,q0,half,P=PCOMB,bd=2):
    m=np.abs(q-q0)<=half
    if m.sum()<12: return None
    dq=q[m]-q0
    X=np.column_stack([dq**j for j in range(bd+1)]+[np.cos(2*np.pi*q[m]/P),np.sin(2*np.pi*q[m]/P)])
    c=np.linalg.lstsq(X,y[m],rcond=None)[0]
    return float(np.hypot(c[-2],c[-1])), float(np.arctan2(-c[-1],c[-2]))
GRID=np.arange(QE[0],QE[-1]+1e-9,0.02)
def brms(v):
    return np.array([float(np.sqrt(np.nanmean(v[(GRID>=a)&(GRID<b)]**2)))
                     for a,b in zip(QE[:-1],QE[1:])])

def reading(arm, carry, half=0.75):
    qc,yc=fine('r6941_fine_lcdm'); qa,ya=fine(arm)
    if carry:
        _,Tc,pc,_=OC.comb(qc,yc); _,Ta,pa,_=OC.comb(qa,ya)
        dphi=(pa-pc+np.pi)%(2*np.pi)-np.pi
        oa_n=osc(qa,ya,Ta/Tc); qa=Tc*(qa/Ta+dphi/(2*np.pi))
    else:
        oa_n=osc(qa,ya)
    g=np.linspace(max(qc.min(),qa.min()),min(qc.max(),qa.max()),len(qc))
    OCg=np.interp(g,qc,osc(qc,yc)); OAg=np.interp(g,qa,oa_n)
    R,DEL,AC,AD=[],[],[],[]
    for x in GRID:
        fa,fc,fd=loc_fit(g,OAg,x,half),loc_fit(g,OCg,x,half),loc_fit(g,OAg-OCg,x,half)
        if fa is None or fc is None or fd is None:
            R.append(np.nan);DEL.append(np.nan);AC.append(np.nan);AD.append(np.nan);continue
        AC.append(fc[0]);AD.append(fd[0]);R.append(fa[0]/fc[0])
        DEL.append(np.arctan2(np.sin(fa[1]-fc[1]),np.cos(fa[1]-fc[1])))
    R,DEL,AC,AD=map(np.array,(R,DEL,AC,AD))
    BOTH=AC*np.sqrt(R**2-2*R*np.cos(DEL)+1); AMP=AC*np.abs(R-1.0); PH=AC*2*np.abs(np.sin(DEL/2))
    mm=np.isfinite(AD)
    worst=float(np.nanmax(np.abs(BOTH[mm]/AD[mm]-1)))
    DB,DAMP,DPH=dep4(brms(BOTH)/np.sqrt(2)),dep4(brms(AMP)/np.sqrt(2)),dep4(brms(PH)/np.sqrt(2))
    return dict(worst=worst, DB=DB, DAMP=DAMP, DPH=DPH,
                b1_amp=brms(AMP)[0]/brms(BOTH)[0], b1_ph=brms(PH)[0]/brms(BOTH)[0],
                medel=float(np.nanmedian(np.abs(DEL)))*180/np.pi,
                meR=float(np.nanmedian(np.abs(R-1.0)))*100)

for arm in ('r6941_fine_cr','r6941_fine_cr_leafrec1'):
    for carry in (False,True):
        d=reading(arm,carry)
        amp=np.mean([x[0] for x in d['DAMP']]); both=np.mean([x[0] for x in d['DB']])
        print(f"{arm.replace('r6941_fine_',''):12s} carry={str(carry):5s} identity {d['worst']:.1e} | "
              f"amp {amp:+.3f} both {both:+.3f} ratio {amp/both:.3f} | "
              f"band1 amp {d['b1_amp']:.3f} phase {d['b1_ph']:.3f} | "
              f"|phase| med {d['medel']:.3f} deg, |R-1| med {d['meR']:.2f}%")
        print(f"{'':28s} AMP signs {[round(x[0],3) for x in d['DAMP']]}  BOTH signs {[round(x[0],3) for x in d['DB']]}")
