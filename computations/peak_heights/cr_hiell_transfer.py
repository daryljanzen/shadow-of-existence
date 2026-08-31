"""
CR HIGH-ELL ACOUSTIC TRANSFER (the deciding computation for the damping-tail sign).

The question the damping-tail verdict hinges on: at high ell, do CR's acoustic PEAK HEIGHTS track
flat-LCDM's, or not? The corpus claims they do (collapse-phase driving = LCDM's radiation driving by
time-reversal), but that was verified only through P3. If they match, CR's larger Silk scale makes a
high-ell deficit; if the geometric stacking rate changes the driving envelope, the picture differs.

DISCIPLINE (r966, after the near-refutation over-reach): VALIDATION GATE FIRST. The semi-analytic
driven-oscillator must reproduce CAMB's LCDM peak-height envelope across the WHOLE tail (P1..P6,
ell~200-1800), not just P1-P3, before ANY CR number is reported. If it cannot, the honest conclusion
is that this needs a real Boltzmann code / CR's unbuilt perturbation sector -- NOT a verdict.

PHYSICS. Tight-coupling photon-baryon oscillator in sound-horizon phase s=k*r_s:
   Theta0'' + [R'/(1+R)] Theta0' + Theta0 = -Psi_drive(s) - (potential terms)
The RADIATION DRIVING is the decay of the gravitational potential after horizon entry. The
LCDM potential decays for modes entering in radiation domination (the well-known boost). We model
Phi(k,eta) with the standard large-/small-scale transfer and drive the oscillator, then
  C_l ~ [ (Theta0+Psi)^2 + Doppler^2 ] * Damp(l) * primordial(k) ,  l = k D_M.
LCDM: potential decays (radiation driving on). CR: on the geometric stacking post-seam rate the potential
is matter-dominated (no decay) -- so CR's driving is whatever the COLLAPSE phase transmitted at the
seam; we compute BOTH bracketing readings and report the range, not a single verdict.
"""
import numpy as np, camb
from scipy.integrate import solve_ivp
from scipy.integrate import simpson

# ================= CAMB LCDM reference (the validation target) =================
pars=camb.CAMBparams(); pars.set_cosmology(H0=67.36,ombh2=0.02237,omch2=0.1200,mnu=0.06,tau=0.0544)
pars.InitPower.set_params(As=2.1e-9,ns=0.9649); pars.set_for_lmax(2600,lens_potential_accuracy=0)
res=camb.get_results(pars); dp=res.get_derived_params()
tot=res.get_unlensed_scalar_cls(CMB_unit='muK', raw_cl=False)   # D_l unlensed TT (cleaner peaks)
ellc=np.arange(tot.shape[0]); DlC=tot[:,0]
rs=dp['rstar']; DA=dp['rstar']/(dp['thetastar']/100.); ns=0.9649
Req=0.60   # baryon loading at recomb
print(f"CAMB: r*={rs:.2f}  D_M={DA:.0f}  100theta*={dp['thetastar']:.4f}")

def camb_peaks(lo=150,hi=1900):
    m=(ellc>=lo)&(ellc<=hi); e,d=ellc[m],DlC[m]
    idx=[i for i in range(3,len(d)-3) if d[i]==max(d[i-3:i+4])]
    pk=[]
    for i in idx:
        if not pk or e[i]-pk[-1][0]>120: pk.append((e[i],d[i]))
    return pk
cpk=camb_peaks()
print("CAMB LCDM peaks (l, D_l muK^2):", [(int(l),int(h)) for l,h in cpk])

# ================= semi-analytic driven oscillator =================
def Psi_env(s, driving):
    """potential Phi(s) driving the oscillator. driving='rad' -> LCDM radiation-driving decay
    (potential decays after horizon entry); 'none' -> matter-dominated constant (no decay);
    's' in sound-horizon phase, horizon entry ~ potential decay tied to u=sqrt3 s (RD)."""
    u=np.maximum(np.abs(np.sqrt(3)*s),1e-8)
    if driving=='rad':  return 3*(np.sin(u)-u*np.cos(u))/u**3      # RD potential (decays to 0)
    if driving=='none': return np.ones_like(u)*0.0                  # no potential drive (const, decayed)
    raise ValueError

def spectrum(xD, R, driving, xmax=26):
    # ONE integration of the driven oscillator over [0,xmax], read Theta0(x),Theta0'(x) at all x
    xs=np.linspace(0.2,xmax,2600)
    def rhs(s,y):
        Pn=Psi_env(np.array([s]),driving)[0]
        return [y[1], -y[0]-Pn]
    sol=solve_ivp(rhs,[1e-4,xmax],[-0.5,0.0],t_eval=xs,rtol=1e-8,atol=1e-10,max_step=0.05)
    Th0=sol.y[0]; Th0d=sol.y[1]
    Pn=Psi_env(xs,driving)
    M=(Th0+Pn)-R*Pn; D=(1/np.sqrt(3*(1+R)))*Th0d
    Cl=(M**2+D**2)*np.exp(-2*(xs/xD)**2)*xs**(ns-1)
    ell=xs*DA/rs
    return ell, Cl

# ---- GATE: fit xD so LCDM (driving='rad') matches CAMB damping tail; check peak-height pattern ----
xD_L=9.0
ellL,ClL = spectrum(xD_L, Req, 'rad')
# normalize to CAMB first peak, compare peak ratios across the tail
def model_peaks(ell,Cl,lo=150,hi=1900):
    m=(ell>=lo)&(ell<=hi); e,d=ell[m],Cl[m]
    idx=[i for i in range(3,len(d)-3) if d[i]==max(d[i-3:i+4])]
    pk=[]
    for i in idx:
        if not pk or e[i]-pk[-1][0]>120: pk.append((e[i],d[i]))
    return pk
mpk=model_peaks(ellL,ClL)
if mpk and cpk:
    normM=cpk[0][1]/mpk[0][1]
    print("\n[GATE] LCDM semi-analytic vs CAMB, peak heights (normalized to P1):")
    print(f"   {'peak':>4} {'l_CAMB':>7} {'D_CAMB':>8} {'l_mod':>6} {'D_mod(norm)':>11} {'ratio':>6}")
    for i in range(min(len(mpk),len(cpk))):
        lc,hc=cpk[i]; lm,hm=mpk[i]
        print(f"   P{i+1:>2} {int(lc):>7} {int(hc):>8} {int(lm):>6} {hm*normM:>11.0f} {hm*normM/hc:>6.2f}")
    print("   GATE PASSES only if ratios ~1.0 across ALL peaks P1..P6 (not just P1-P3).")
print("""
============================================================================
GATE RESULT (r966): FAILED. The semi-analytic driven-oscillator reproduces P1 (by
normalization) but is badly wrong across P2-P6 -- P2 ~1.8x too high, P4-P6 an order of
magnitude too low. It cannot reproduce flat-LCDM's OWN peak-height tail, so it certainly
cannot resolve an ~8% CR modification on top of it.

HONEST CONCLUSION: the damping-tail SIGN is NOT settleable with a semi-analytic model. The
deciding computation -- CR's high-ell acoustic transfer on the geometric stacking background --
requires a real Boltzmann-level transfer (the coupled photon-baryon-metric hierarchy solved
mode by mode through recombination), and CAMB cannot supply it because it cannot decouple the
geometric stacking BACKGROUND from radiation-gravitating PERTURBATIONS the way CR's ontology asks.
So this is a genuine BUILD (a CR-specific Boltzmann sector), quite possibly gated on CR's
perturbation dynamics being more fully specified -- i.e. Bucket B (frontier), NOT a tractable
shortcut. My earlier 'partially tractable approximate bound' over-stated it, and the
'near-refutation' rested on assuming exactly the peak-envelope this gate shows is hard to get
right at all. Reclassify the damping-tail sign as a frontier build. Stated honestly.
============================================================================""")
