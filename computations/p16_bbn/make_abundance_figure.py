"""
D1 results figure: the computed light-element abundances freezing out along the cooling leg
(the network of bbn_network.py at the CMB-inherited eta10=6.14). This is P16 sec:network's result
made visible -- the standard-BBN pattern produced from the collapse cooling history.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp
import bbn_network as B

# re-run with dense output and capture the trajectory
t_bg,T9_bg,rho_bg,tT9,trho,eta = B.build_background(eta10=6.14)
rc,nuclist,dropped = B.build_network()   # REACLIB: robust single-solve; freeze-out shape is library-independent
from pynucastro import Composition
nuc = rc.unique_nuclei
za = {(n.Z,n.A):i for i,n in enumerate(nuc)}
idx = {'n':za[(0,1)],'p':za[(1,1)],'d':za[(1,2)],'t':za[(1,3)],
       'he3':za[(2,3)],'he4':za[(2,4)],'li7':za[(3,7)],'be7':za[(4,7)]}
A=np.array([n.A for n in nuc]); Zz=np.array([n.Z for n in nuc])

T9_start,T9_end=9.0,8e-2
ti=float(interp1d(T9_bg,t_bg)(T9_start)); tf=float(interp1d(T9_bg,t_bg)(T9_end))
Xn0=B.pre_evolve_np(t_bg,T9_bg,T9_net=T9_start)
Y=np.zeros(len(nuc)); Y[idx['n']]=Xn0; Y[idx['p']]=1-Xn0
comp=Composition(nuc)
def set_comp(Yv):
    for i,n in enumerate(nuc): comp.X[n]=max(Yv[i],0.0)*n.A
    return comp
def rhs(t,Yv):
    T9=float(tT9(t)); T=T9/B.T9_per_MeV; rho=float(trho(t)); set_comp(Yv)
    with np.errstate(over='ignore',invalid='ignore',divide='ignore'):
        yd=rc.evaluate_ydots(rho,T9*1e9,comp); dY=np.array([yd[n] for n in nuc])
    dY=np.nan_to_num(dY,nan=0.0,posinf=0.0,neginf=0.0)
    wnp,wpn=B.lam_np_fast(T),B.lam_pn_fast(T)
    dn=-wnp*Yv[idx['n']]+wpn*Yv[idx['p']]; dY[idx['n']]+=dn; dY[idx['p']]-=dn
    return dY
def jac(t,Yv):
    T9=float(tT9(t)); T=T9/B.T9_per_MeV; rho=float(trho(t)); set_comp(Yv)
    with np.errstate(over='ignore',invalid='ignore',divide='ignore'):
        J=np.nan_to_num(np.array(rc.evaluate_jacobian(rho,T9*1e9,comp)),nan=0,posinf=0,neginf=0)
    wnp,wpn=B.lam_np_fast(T),B.lam_pn_fast(T)
    J[idx['n'],idx['n']]+=-wnp; J[idx['n'],idx['p']]+=wpn
    J[idx['p'],idx['n']]+=wnp;  J[idx['p'],idx['p']]+=-wpn
    return J
atol=np.full(len(nuc),1e-12); atol[idx['n']]=atol[idx['p']]=1e-10
sol=solve_ivp(rhs,[ti,tf],Y,method='LSODA',rtol=1e-6,atol=atol,jac=jac,dense_output=True)

T9ax=np.logspace(np.log10(3.0),np.log10(T9_end),400)
tax=interp1d(T9_bg,t_bg)(T9ax)
Ytr=np.array([sol.sol(tc) for tc in tax]).T
Yp=Ytr[idx['p']]
series=[('n',idx['n'],'#888888','Y$_n$'),('p',idx['p'],'#111111','Y$_p$ (H)'),
        ('d',idx['d'],'#1f6feb','D/H'),('he4',idx['he4'],'#d1495b','$^4$He (Y$_p$/4)'),
        ('he3',idx['he3'],'#2e8b57','$^3$He/H'),('li7',idx['li7'],'#b8860b','$^7$Li/H')]

fig,ax=plt.subplots(figsize=(7.2,5.2))
for name,i,col,lab in series:
    if name in ('n','p'):
        yv=Ytr[i]
    elif name=='he4':
        yv=Ytr[i]           # molar fraction (mass frac = 4x)
    else:
        yv=Ytr[i]/Yp        # per-H ratio
    ax.plot(T9ax,np.clip(yv,1e-14,None),color=col,lw=2,label=lab)
ax.axvline(0.07*B.T9_per_MeV,ls=':',color='0.4',lw=1)
ax.text(0.07*B.T9_per_MeV*1.05,3e-13,'D bottleneck\n$T_D\\simeq0.07$ MeV',fontsize=7,color='0.4')
ax.set_xscale('log'); ax.set_yscale('log'); ax.invert_xaxis()
ax.set_xlim(3.0,T9_end); ax.set_ylim(1e-13,2)
ax.set_xlabel('$T_9$  (temperature $/10^9$ K) — cooling leg $\\rightarrow$')
ax.set_ylabel('abundance  (molar fraction, or per-H ratio)')
ax.set_title('D1: light elements freezing out on the collapse cooling leg\n'
             '(REACLIB network + thermal $n\\leftrightarrow p$, standard window rate, $\\eta_{10}=6.14$)',fontsize=10)
ax.legend(loc='lower left',fontsize=8,ncol=2,framealpha=0.9)
# annotate final values
Yf=sol.y[:,-1]
txt=(f"final:  $Y_p$={4*Yf[idx['he4']]:.3f}   D/H={Yf[idx['d']]/Yf[idx['p']]:.2e}\n"
     f"$^3$He/H={Yf[idx['he3']]/Yf[idx['p']]:.2e}   $^7$Li/H={(Yf[idx['li7']]+Yf[idx['be7']])/Yf[idx['p']]:.2e}")
ax.text(0.42,0.97,txt,transform=ax.transAxes,fontsize=8,va='top',ha='left',
        bbox=dict(boxstyle='round',fc='white',ec='0.7'))
plt.tight_layout()
plt.savefig('fig_abundances.pdf'); plt.savefig('fig_abundances.png',dpi=140)
print("wrote fig_abundances.pdf / .png")
print(f"final: Yp={4*Yf[idx['he4']]:.4f} D/H={Yf[idx['d']]/Yf[idx['p']]:.3e} "
      f"3He/H={Yf[idx['he3']]/Yf[idx['p']]:.3e} 7Li/H={(Yf[idx['li7']]+Yf[idx['be7']])/Yf[idx['p']]:.3e}")
