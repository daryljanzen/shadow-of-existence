import sys, numpy as np, camb, warnings, json, os
warnings.filterwarnings('ignore')
sys.path.insert(0,'/tmp/planckdata')
from planck_lite_py import PlanckLitePy
from scipy.integrate import quad
from scipy.optimize import minimize
lik=PlanckLitePy(data_directory='/tmp/planckdata/data', year=2018, spectra='TT', use_low_ell_bins=False)
lmax=2508; c=299792.458
def run(H0,ombh2,omch2,As,ns,tau=0.054):
    p=camb.CAMBparams(); p.set_cosmology(H0=H0,ombh2=ombh2,omch2=omch2,tau=tau)
    p.InitPower.set_params(As=As,ns=ns); p.set_for_lmax(2600,lens_potential_accuracy=0)
    p.set_accuracy(AccuracyBoost=1.0, lSampleBoost=1.0)
    r=camb.get_results(p); d=r.get_cmb_power_spectra(p,CMB_unit='muK')['total']
    return d, r.get_derived_params()
def cr_supp(d,dp,H0,ombh2,omch2,z_onset=6797.0):
    Om=(ombh2+omch2)/(H0/100)**2; OL=1-Om
    z_rec=dp['zstar']; a_rec=1/(1+z_rec); Or=Om/(1+dp['zeq'])
    R_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rf=lambda a: R_rec*(a/a_rec)
    g=lambda a: (Rf(a)**2/(1+Rf(a))+8/9)/(6*(1+Rf(a)))
    H=lambda a,rad: H0*np.sqrt(Or/a**4*rad+Om/a**3+OL)
    a_s=1/(1+z_onset)
    IL,_=quad(lambda a:g(a)/H(a,1.0),1e-9,a_rec,limit=120)
    IC,_=quad(lambda a:g(a)/H(a,0.0),a_s,a_rec,limit=120)
    sL,_=quad(lambda a:c/(a**2*H(a,1.0)*np.sqrt(3*(1+Rf(a)))),1e-9,a_rec,limit=120)
    sC,_=quad(lambda a:c/(a**2*H(a,0.0)*np.sqrt(3*(1+Rf(a)))),a_s,a_rec,limit=120)
    r=(np.sqrt(IC/IL))/(sC/sL)
    full=np.arange(d.shape[0]); sel=(full>1400)&(full<2400)
    co=np.polyfit(full[sel].astype(float)**2, np.log(np.maximum(d[sel,0],1e-12)),1)
    lD=np.sqrt(-1/co[0]); ell=np.arange(2,lmax+1)
    return np.exp(-(ell/lD)**2*(r**2-1)), r, lD
def chi2(pv, cr):
    H0,ombh2,omch2,As9,ns=pv
    if not(55<H0<85 and 0.018<ombh2<0.026 and 0.09<omch2<0.16 and 1.5<As9<3.0 and 0.85<ns<1.25):
        return 1e6
    try:
        d,dp=run(H0,ombh2,omch2,As9*1e-9,ns)
        Dltt=d[2:lmax+1,0].copy(); Dlte=d[2:lmax+1,3]; Dlee=d[2:lmax+1,1]
        if cr:
            s,_,_=cr_supp(d,dp,H0,ombh2,omch2); Dltt=Dltt*s
        return -2*lik.loglike(Dltt,Dlte,Dlee,ellmin=2)
    except Exception:
        return 1e6
if __name__=="__main__":
    which=sys.argv[1]; budget=int(sys.argv[2])
    x0=[67.4,0.0224,0.120,2.1,0.965]
    if os.path.exists(f'/tmp/planckdata/{which}.json'):
        x0=json.load(open(f'/tmp/planckdata/{which}.json'))['x']
    cr = (which=='cr')
    r=minimize(chi2,x0,args=(cr,),method='Nelder-Mead',
               options={'maxfev':budget,'xatol':2e-3,'fatol':0.5})
    json.dump({'x':list(r.x),'fun':float(r.fun)}, open(f'/tmp/planckdata/{which}.json','w'))
    print(f"{which}: chi2={r.fun:.1f}  x={[round(v,5) for v in r.x]}")
