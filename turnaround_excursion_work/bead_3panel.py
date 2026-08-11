import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
al=1.0; twoM=2/(3*np.sqrt(3)); A=(twoM*al**2)**(1/3); rho=al/np.sqrt(3)

# ---- analytical: the phase structure phi = 2 pi r /(sqrt3 alpha) (the X1 cosine argument, P7 fig E) ----
def phi(r): return 2*np.pi*r/(np.sqrt(3)*al)
print("PHASE phi=2*pi*r/(sqrt3 a) at the critical points (P7 fig E cosine argument):")
for lab,rv in [("front seam +rho",rho),("r=0 (conjugation)",0.0),("turnaround",-A),("back seam -2rho",-2*rho)]:
    print(f"   {lab:22s} r={rv:+.4f}   phi={phi(rv):+.4f} rad = {np.degrees(phi(rv)):+7.1f} deg")
print("   -> seams at +120 / -240 deg (the 120/240 split); r=0 at 0; turnaround at -2*pi*2^(1/3)/3")
print(f"      = {np.degrees(-2*np.pi*2**(1/3)/3):.1f} deg: OFFSET from both r=0 and the clean 120/240 seams (the cube-root 2^(1/3) phase).")
print()
print("THE TWO CUBICS, read off structure (alpha=1):")
# ---- the three-panel figure ----
def collapse(u): return -A*np.cosh(3*u/2/al)**(2/3)
def lift(v):     return -A*np.sin(3*v/2/al)**(2/3)
def expand(w):   return  A*np.sinh(3*w/2/al)**(2/3)
U,W=2.3,2.3
u=np.linspace(-U,0,6000); v=np.linspace(np.pi*al/3,0,6000)[1:]; w=np.linspace(0,W,6000)[1:]
sc=u+U; sl=sc[-1]+(np.pi*al/3-v); se=sl[-1]+w
s=np.concatenate([sc,sl,se]); rr=np.concatenate([collapse(u),lift(v),expand(w)])
d1=np.gradient(rr,s); d2=np.gradient(d1,s)
i_turn=len(sc)-1; i_zero=len(sc)+len(sl)-1
i_front=len(sc)+len(sl)+np.argmin(np.abs(se-rho)); i_back=np.argmin(np.abs(sc-(sc[np.argmin(np.abs(collapse(u)+2*rho))])))
sturn,szero,sfront,sback=s[i_turn],s[i_zero],s[i_front],s[i_back]

RED='#c0392b'; BLUE='#2471a3'; INK='#1c1c1c'; GOLD='#b8860b'; GREY='#8a8a8a'
plt.rcParams.update({'font.size':10,'axes.edgecolor':'#555','axes.linewidth':0.8})
fig,axes=plt.subplots(3,1,figsize=(7.2,8.4),sharex=True)
fig.suptitle(r'The cosmogenetic bead vs arc length $s$: position, rate, acceleration',fontsize=12,y=0.985)

def paint(ax,y,ylab,clip=None):
    neg=rr<=0; pos=rr>=0
    ax.plot(s[neg],y[neg],color=RED,lw=1.8); ax.plot(s[pos],y[pos],color=BLUE,lw=1.8)
    ax.axvline(szero,color=INK,lw=0.7,ls=(0,(4,3))); ax.axvline(sturn,color=GOLD,lw=0.7,ls=(0,(1,2)))
    ax.axvline(sfront,color=GREY,lw=0.6,ls=':'); ax.axvline(sback,color=GREY,lw=0.6,ls=':')
    ax.set_ylabel(ylab)
    if clip: ax.set_ylim(*clip)

# panel A: r(s)
paint(axes[0],rr,r'areal radius  $r$')
axes[0].axhline(0,color='#ccc',lw=0.6)
axes[0].plot(sturn,-A,'s',mfc=GOLD,mec=INK,ms=8,zorder=5)
axes[0].plot(szero,0,'D',mfc='w',mec=INK,ms=7,zorder=5)
axes[0].plot(sfront,rho,'o',mfc='w',mec=INK,ms=7,zorder=5); axes[0].plot(sback,-2*rho,'o',mfc='w',mec=INK,ms=7,zorder=5)
axes[0].annotate('antimatter progenitor\n(collapse, $r<0$)',(sc[len(sc)//4],collapse(u)[len(sc)//4]),color=RED,fontsize=8,ha='left')
axes[0].annotate('our universe\n(expansion, $r>0$)',(se[len(se)//3],expand(w)[len(se)//3]),color=BLUE,fontsize=8,ha='left')
axes[0].annotate('turnaround\n$r=-\\sqrt[3]{2}\\,\\rho$  (collapse stops)',(sturn,-A),xytext=(sturn-2.0,-A-0.55),fontsize=7.5,color=GOLD,arrowprops=dict(arrowstyle='->',color=GOLD,lw=0.8))
axes[0].annotate('$r=0$: species/charge conjugation\n(branch point; the two cubics meet)',(szero,0),xytext=(szero+0.15,1.05),fontsize=7.5,color=INK,arrowprops=dict(arrowstyle='->',color=INK,lw=0.8))
axes[0].annotate('front seam $+\\rho$ (merged horizon)',(sfront,rho),xytext=(sfront+0.1,rho-0.5),fontsize=7,color=GREY)
axes[0].annotate('back seam $-2\\rho$',(sback,-2*rho),xytext=(sback+0.1,-2*rho+0.12),fontsize=7,color=GREY)

# panel B: dr/ds
paint(axes[1],d1,r"rate  $dr/ds$",clip=(0,6))
axes[1].plot(sturn,0,'s',mfc=GOLD,mec=INK,ms=7,zorder=5)
axes[1].plot(sfront,d1[i_front],'o',mfc='w',mec=INK,ms=6,zorder=5)
axes[1].annotate('$=0$ (horizontal tangent)',(sturn,0),xytext=(sturn-2.1,0.7),fontsize=7.5,color=GOLD)
axes[1].annotate(r'$\to\infty$ (vertical tangent)',(szero,5.5),xytext=(szero-2.6,5.2),fontsize=7.5,color=INK)
axes[1].annotate('min at the front seam',(sfront,d1[i_front]),xytext=(sfront+0.15,d1[i_front]+0.9),fontsize=7.5,color=GREY,arrowprops=dict(arrowstyle='->',color=GREY,lw=0.7))

# panel C: r''
paint(axes[2],d2,r"acceleration  $d^2r/ds^2$",clip=(-8,8))
axes[2].axhline(0,color='#ccc',lw=0.6)
axes[2].annotate('sign flip at $r=0$\n(the conjugation)',(szero,0),xytext=(szero+0.15,4.2),fontsize=7.5,color=INK,arrowprops=dict(arrowstyle='->',color=INK,lw=0.7))
axes[2].annotate('$=0$ at the\ndynamical turns\n(turnaround, seam)',(sturn,0),xytext=(sturn-2.2,-6.5),fontsize=7.5,color=GOLD)
axes[2].set_xlabel(r'arc length  $s$  along the bead path in complex $\tilde\tau$')
for ax in axes: ax.margins(x=0.01)
plt.tight_layout(rect=[0,0,1,0.975]); plt.savefig('/home/claude/cr/work/bead_3panel.png',dpi=120)
print("\n[figure saved: bead_3panel.png]")
