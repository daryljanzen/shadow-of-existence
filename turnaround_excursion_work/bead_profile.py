import numpy as np
al=1.0; twoM=2/(3*np.sqrt(3))            # Nariai
A=(twoM*al**2)**(1/3)                     # turnaround radius magnitude = 2^{1/3} alpha/sqrt3
rho=al/np.sqrt(3)                          # merged (Nariai) horizon; front seam = +rho, back = -2rho
print(f"  A (|turnaround|)={A:.4f} = 2^(1/3)/sqrt3={2**(1/3)/np.sqrt(3):.4f}")
print(f"  front seam +rho={rho:.4f}   back seam -2rho={-2*rho:.4f}   (2:1)")
print(f"  ordering on collapse branch: r=0 ... turnaround({-A:.3f}) ... back seam({-2*rho:.3f})")
print(f"  -> turnaround (|{A:.3f}|) is BETWEEN r=0 and the back seam (|{2*rho:.3f}|): 2^(1/3) vs 2.")

# build r(s) and dr/ds along the path: collapse (u:-U->0) + lift (v:pi/3->0) + expansion (w:0->W)
def collapse(u): return -A*np.cosh(3*u/2/al)**(2/3)          # u<0..0 ; dr/du=0 at u=0 (turnaround)
def lift(v):     return -A*np.sin(3*v/2/al)**(2/3)            # v: pi*al/3 -> 0 ; r: -A -> 0
def expand(w):   return  A*np.sinh(3*w/2/al)**(2/3)           # w:0->W ; r:0->+inf
U,W=2.2,2.2
u=np.linspace(-U,0,4000); v=np.linspace(np.pi*al/3,0,4000)[1:]; w=np.linspace(0,W,4000)[1:]
rc,rl,re=collapse(u),lift(v),expand(w)
# arc length s = concatenated parameter (ds=|dtau|=du,dv,dw on each straight leg)
sc=u+U; sl=sc[-1]+(np.pi*al/3-v); se=sl[-1]+w
s=np.concatenate([sc,sl,se]); r=np.concatenate([rc,rl,re])
drds=np.gradient(r,s)
# locate features
i_turn=len(sc)-1                                   # end of collapse = turnaround
i_zero=len(sc)+len(sl)-1                            # end of lift = r=0
# front seam on expansion leg: r=+rho
i_front=len(sc)+len(sl)+np.argmin(np.abs(re-rho))
print(f"\n  dr/ds at turnaround = {drds[i_turn]:.4f}  (expect ~0)")
print(f"  dr/ds just before r=0 = {drds[i_zero-2]:.3f}  (expect large -> vertical tangent)")
# is the front seam the MINIMUM of dr/ds on the expansion leg?
exp_slice=slice(len(sc)+len(sl), None)
i_min_exp=len(sc)+len(sl)+np.argmin(drds[exp_slice])
print(f"  dr/ds MINIMUM on expansion leg at r={r[i_min_exp]:.4f}  (front seam rho={rho:.4f}? {'YES' if abs(r[i_min_exp]-rho)<0.02 else 'no'})")
# analytic: min of sinh^{-1/3}cosh at tanh=1/sqrt3 -> r=(2M)^{1/3}(1/sqrt2)^{2/3}=M^{1/3}=rho at Nariai
print(f"  analytic check: min dr/dw at tanh(3w/2)=1/sqrt3 -> r=M^(1/3)={ (twoM/2)**(1/3):.4f} = rho -> the FRONT SEAM is the dr/ds min.")
# collapse leg: is dr/ds monotonic (back seam NOT an extremum)?
col_drds=np.abs(drds[:len(sc)])
mono = np.all(np.diff(col_drds[10:-10])<=1e-6) or np.all(np.diff(col_drds[10:-10])>=-1e-6)
print(f"  collapse-leg |dr/ds| monotonic from turnaround outward? {mono}  -> back seam is NOT a dr/ds extremum (asymmetry).")

import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(7,7),sharex=True)
ax1.plot(s,r,'k-',lw=1.5); ax1.axhline(0,color='0.7',lw=.6)
for val,lab,c in [(-A,'turnaround (dr/ds=0)','r'),(0,'r=0 conjugation (dr/ds=inf)','b'),(rho,'front seam +rho','g'),(-2*rho,'back seam -2rho','m')]:
    ax1.axhline(val,color=c,lw=.7,ls='--')
ax1.plot(s[i_turn],r[i_turn],'ro'); ax1.plot(s[i_zero],r[i_zero],'bo'); ax1.plot(s[i_front],r[i_front],'go')
ax1.set_ylabel('r'); ax1.set_title('Fig-F bead: r(s), and dr/ds below'); ax1.legend(fontsize=7,loc='upper left')
ax2.plot(s,drds,'k-',lw=1.5); ax2.set_ylim(0,6); ax2.set_ylabel('dr/ds'); ax2.set_xlabel('arc length s')
ax2.plot(s[i_turn],drds[i_turn],'ro'); ax2.plot(s[i_front],drds[i_front],'go')
ax2.axvline(s[i_zero],color='b',lw=.7,ls='--')
plt.tight_layout(); plt.savefig('/home/claude/cr/work/bead_profile.png',dpi=110)
print("  [figure saved: bead_profile.png]")
