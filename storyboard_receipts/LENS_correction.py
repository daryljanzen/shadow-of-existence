"""LENS — the lensing correction to TT, from Planck's own lensing-potential spectrum.

WHY.  Our calculation is UNLENSED; Planck's curve is LENSED.  That is the last structural difference
between the two objects being compared (r2150).  Lensing has been argued about repeatedly in this
session -- it reduces peaks and fills troughs, so it deepens a peak deficit -- but never COMPUTED.

METHOD (Hu 2000, first order in C^phi-phi; accurate to a few percent for TT):
    Ctilde_l - C_l = (1/(2pi)^2) Int dl' l' Int dtheta  [l'.(l-l')]^2 C^phiphi_{|l-l'|} [C_l' - C_l]
with l'.(l-l') = l' l cos(theta) - l'^2 and |l-l'|^2 = l^2 + l'^2 - 2 l l' cos(theta).

C^phiphi comes from the PP column of the Planck best-fit theory file, which is
[l(l+1)]^2 C_l^phiphi / 2pi.  C_l for the convolution is taken from the same file's TT column: it is
lensed rather than unlensed, but the correction is first order, so using it costs only second-order
accuracy -- adequate for deciding whether lensing explains a 12% deficit.
"""
import numpy as np
from PLANCK_theory_curve import planck_TT
# PP = [l(l+1)]^2 C_l^phiphi / 2pi, sampled from the same PLA file
PP={2:0.501352e-7,5:0.782921e-7,10:0.106122e-6,20:0.130999e-6,30:0.138304e-6,40:0.137954e-6,
    50:0.133916e-6,70:0.121523e-6,100:0.101565e-6,150:0.750958e-7,200:0.573818e-7,
    300:0.371298e-7,400:0.261214e-7,500:0.192169e-7,700:0.116002e-7,900:0.783181e-8,
    1100:0.562694e-8,1300:0.423935e-8,1450:0.354e-8}
_L=np.array(sorted(PP)); _P=np.array([PP[k] for k in _L])
def Cpp(l):
    l=np.maximum(np.asarray(l,dtype=float),2.0)
    p=np.interp(l,_L,_P, left=_P[0], right=_P[-1])
    hi=l>_L[-1]                       # extrapolate the tail as ~l^-2 rather than flat
    if np.any(hi): p=np.where(hi, _P[-1]*(_L[-1]/np.maximum(l,1.))**2, p)
    return 2*np.pi*p/(l*(l+1))**2
def CTT(l):
    l=np.maximum(np.asarray(l,dtype=float),2.0)
    return 2*np.pi*planck_TT(l)/(l*(l+1))

def lensed_ratio(lvals, nlp=420, nth=192):
    lp=np.exp(np.linspace(np.log(2.),np.log(3000.),nlp)); th=np.linspace(0,2*np.pi,nth,endpoint=False)
    out=[]
    for L in lvals:
        LP,TH=np.meshgrid(lp,th,indexing='ij')
        dot=LP*L*np.cos(TH)-LP**2
        Lm=np.sqrt(np.maximum(L**2+LP**2-2*L*LP*np.cos(TH),1e-6))
        integ=(dot**2)*Cpp(Lm)*(CTT(LP)-CTT(L))*LP
        dlp=np.gradient(lp); dth=th[1]-th[0]
        val=np.sum(integ*dlp[:,None]*dth)/(2*np.pi)**2
        out.append(1.0+val/CTT(L))
    return np.array(out)

if __name__=="__main__":
    Ls=np.array([50,100,220,300,416,538,675,810,1000,1148,1300])
    r=lensed_ratio(Ls)
    print("  LENSING CORRECTION  Ctilde_l / C_l   (from Planck's own C^phiphi)")
    print("      l     lensed/unlensed     effect")
    for L,v in zip(Ls,r): print("   %5d       %8.4f       %+6.2f%%"%(L,v,100*(v-1)))
    print()
    print("  peaks should go DOWN, troughs UP.  Our unlensed spectrum must be MULTIPLIED by this")
    print("  ratio before comparing with Planck's lensed curve.")
