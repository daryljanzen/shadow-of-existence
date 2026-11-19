"""The lensing excess on both arms: scale the lensing smoothing by A_L on banked spectra (the corpus applies one CAMB
lensing ratio, at the Planck point with 0.06 eV, to every spectrum) and score the 185 plik_lite bins with the
amplitude refitted.  Read-only probe; working file for the neutrino-mass question routed through 69."""
import os, sys, numpy as np
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT,'computations','planck_tt_likelihood'))
import camb, chi2_of_spectrum as CS
SP=os.path.join(ROOT,'computations','beyond_the_wall','spectra')
p=camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
cl=camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=3000)
le,un=cl['total'][:,0],cl['unlensed_scalar'][:,0]
LG=np.arange(len(le),dtype=float); R=np.ones_like(le); R[un>0]=le[un>0]/un[un>0]
for fn in ('r7749_leafgeom_refit_verify_cr.npz','cc66_r185_verify_lcdm.npz','r7749_leafgeom_nofit_L2000_cr.npz','cc66_lcdm_L2000.npz'):
    z=np.load(os.path.join(SP,fn),allow_pickle=True); ls=np.asarray(z['ls'],float); D=np.asarray(z['Dl'],float)
    sw=str(z['switches']) if 'switches' in z.files else ''
    res=[]
    for AL in np.arange(0.5,1.81,0.05):
        r=1+AL*(np.interp(ls,LG,R)-1)
        c,nb=CS.chi2_of(ls,D*r)[:2]; res.append((AL,c))
    res=np.array(res); i=res[:,1].argmin()
    # parabola fit near min
    j=slice(max(i-4,0),i+5); co=np.polyfit(res[j,0],res[j,1],2); amin=-co[1]/(2*co[0]); sig=1/np.sqrt(co[0])
    c1=np.interp(1.0,res[:,0],res[:,1])
    print(f'{fn:45s} nb={nb} A_L best {amin:.2f} +- {sig:.2f}; chi2(1)-chi2min = {c1-res[:,1].min():.2f}  [{sw[:90]}]')
