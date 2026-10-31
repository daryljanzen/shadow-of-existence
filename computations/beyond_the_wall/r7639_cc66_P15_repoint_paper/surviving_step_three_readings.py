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

FAILS=[]
ROWS={}
for arm in ('r6941_fine_cr','r6941_fine_cr_leafrec1'):
    for carry in (False,True):
        d=reading(arm,carry)
        ROWS[(arm,carry)]=d
        amp=np.mean([x[0] for x in d['DAMP']]); both=np.mean([x[0] for x in d['DB']])
        ph=np.mean([x[0] for x in d['DPH']])
        print(f"{arm.replace('r6941_fine_',''):12s} carry={str(carry):5s} identity {d['worst']:.1e} | "
              f"amp {amp:+.3f} both {both:+.3f} ratio {amp/both:.3f} | "
              f"band1 amp {d['b1_amp']:.3f} phase {d['b1_ph']:.3f} | "
              f"|phase| med {d['medel']:.3f} deg, |R-1| med {d['meR']:.2f}%")
        print(f"{'':28s} AMP signs {[round(x[0],3) for x in d['DAMP']]}  BOTH signs {[round(x[0],3) for x in d['DB']]}")
        print(f"{'':28s} PH  signs {[round(x[0],3) for x in d['DPH']]}   mean {ph:+.3f}")

# =================================================================================================
# ** r7641 ⑷ -- THE TWO CLAUSES THE RULING'S WORDING DROPS, CHECKED ON THE ARM OF RECORD. **
#   `r7641` ⑷: "Before landing, check on the arm of record the two clauses this wording drops: the
#   phase-only term stepping the other way, and the phase step reversing sign as the window widens.
#   If either holds, restore it in the wording above.  If either fails, it stays out."
# =================================================================================================
AOR=('r6941_fine_cr_leafrec1',False)      # the reading the ruling adopts: UNCARRIED on the arm of record
NSK=('r6941_fine_cr',False)
print()
print("="*100)
print("  ⑷'s TWO DROPPED CLAUSES, ON THE READING THE RULING ADOPTS (arm of record, UNCARRIED)")
print("="*100)

# ---- ⒜ does the phase-only term step the OTHER WAY? --------------------------------------------
for tag,key in (('the namesake arm',NSK),('the ARM OF RECORD',AOR)):
    d=ROWS[key]
    a=[x[0] for x in d['DAMP']]; p=[x[0] for x in d['DPH']]
    opp=all(np.sign(pi)!=np.sign(ai) for pi,ai in zip(p,a))
    print(f"  ⒜ {tag:18s} AMP {[round(x,3) for x in a]}  PH {[round(x,3) for x in p]}"
          f"  -> phase steps {'the OTHER way on every basis' if opp else 'the SAME way somewhere'}")
    ROWS[key]['ph_opposite']=opp

# ---- ⒝ does the phase step REVERSE SIGN as the window widens? ----------------------------------
print("  ⒝ the phase step against the local-fit half-window, on the arm of record, uncarried:")
SWEEP=(0.5,0.75,1.0,1.5,2.0)
phs=[]
for h in SWEEP:
    d=reading(AOR[0],AOR[1],half=h)
    ph=np.mean([x[0] for x in d['DPH']]); phs.append(ph)
    print(f"       half={h:4.2f}   phase step {ph:+.4f}   amp step "
          f"{np.mean([x[0] for x in d['DAMP']]):+.4f}")
REVERSES=(min(phs)<0.0<max(phs))
print(f"     -> the phase step {'REVERSES sign' if REVERSES else 'keeps one sign'} across the sweep "
      f"({min(phs):+.4f} to {max(phs):+.4f})")

# ---- the verdict, and the validation that licenses reading it ----------------------------------
# ⛭ the namesake UNCARRIED row is the receipt's own published reading, so it is the figure this
#   instrument is checked against before either clause above is believed.
_a=np.mean([x[0] for x in ROWS[NSK]['DAMP']]); _b=np.mean([x[0] for x in ROWS[NSK]['DB']])
if not (abs(_a+0.243)<5e-3 and abs(_b+0.220)<5e-3 and abs(_a/_b-1.106)<5e-3):
    FAILS.append(f"the namesake uncarried row is not reproduced: amp {_a:+.3f} both {_b:+.3f}")
if ROWS[AOR]['worst']>1e-9:
    FAILS.append(f"the BOTH/AD identity does not hold on the arm of record: {ROWS[AOR]['worst']:.1e}")
_ra=np.mean([x[0] for x in ROWS[AOR]['DAMP']])/np.mean([x[0] for x in ROWS[AOR]['DB']])
_RA_WANT = 0.705          # the figure the ruling's "about seven tenths" rests on
if not abs(_ra-_RA_WANT)<5e-3:
    FAILS.append(f"the arm-of-record amplitude share is {_ra:.3f}, against the {_RA_WANT} this "
                 f"instrument is pinned to -- the ruling's 'about seven tenths'")
_DEG_WANT, _PCT_WANT = 5.55, 7.56       # the ruling's "five and a half degrees" / "seven and a half per cent"
if not (abs(ROWS[AOR]['medel']-_DEG_WANT)<0.05 and abs(ROWS[AOR]['meR']-_PCT_WANT)<0.05):
    FAILS.append(f"the arm-of-record phase/amplitude medians are {ROWS[AOR]['medel']:.2f} deg and "
                 f"{ROWS[AOR]['meR']:.2f}%, against the {_DEG_WANT} and {_PCT_WANT} this instrument "
                 f"is pinned to")

# ---- ⛔ AND A THIRD THING IN THE WORDING, WHICH ⑷ DID NOT ASK ABOUT -----------------------------
#   `dep4` returns each SERIES' OWN band-1 fractional step, not a share of another series.  So the
#   three are comparable, and on the arm of record they order as |PH| > |BOTH| > |AMP| -- the two
#   channels partially CANCEL in the composite.  ⇒ *The ruling's "with the phase-only term a
#   substantial minority of the rest" is then not supported: the phase-only series' own step is
#   LARGER than the composite's, not a minority of it.  And it steps WITH the statistic on all four
#   bases where on the namesake arm it stepped AGAINST it on all four.*
_AMP=np.mean([x[0] for x in ROWS[AOR]['DAMP']]); _BOTH=np.mean([x[0] for x in ROWS[AOR]['DB']])
_PH=np.mean([x[0] for x in ROWS[AOR]['DPH']])
_PH_N=np.mean([x[0] for x in ROWS[NSK]['DPH']])
print(f"\n  ⒞ the three series' OWN band-1 steps on the arm of record: AMP {_AMP:+.3f}, "
      f"BOTH {_BOTH:+.3f}, PH {_PH:+.3f}")
print(f"       -> AMP is {_AMP/_BOTH:.3f} of the composite and PH is {_PH/_BOTH:.3f} of it, so the "
      f"phase-only term is the LARGER and not a minority")
print(f"       -> and PH's sign flips between arms: {_PH_N:+.3f} on the namesake against "
      f"{_PH:+.3f} on the arm of record")
if not (abs(_PH/_BOTH)>1.0 and _PH<0<_PH_N):
    FAILS.append(f"⒞ does not hold as measured: PH/BOTH {_PH/_BOTH:.3f}, PH {_PH:+.3f} against the "
                 f"namesake's {_PH_N:+.3f}")
_PH_WANT = 1.524
if not abs(_PH/_BOTH-_PH_WANT)<5e-3:
    FAILS.append(f"the phase-only share is {_PH/_BOTH:.3f}, against the {_PH_WANT} this instrument "
                 f"is pinned to")

print()
print("  ⇒ VERDICT for ⑷: clause ⒜ (the phase-only term steps the other way) "
      f"{'HOLDS' if ROWS[AOR]['ph_opposite'] else 'FAILS'} on the arm of record; "
      f"clause ⒝ (the phase step reverses as the window widens) "
      f"{'HOLDS' if REVERSES else 'FAILS'}.")
print()
if FAILS:
    print("FAILED:")
    for f in FAILS: print("  - "+f)
    sys.exit(1)
print("  OK -- the namesake row is reproduced, the decomposition identity holds, and the two figures")
print("  the ruling's wording states are the measured ones.")
sys.exit(0)
