"""
NOT-A-RECEIPT: an ENGINE imported by `P16_validate_bbn.py`, `C6_neutrino_term.py` and two
L-204 receipts -- it asserts nothing of its own and is exercised through its callers.
** Declared c54.225 (`L-559`) rather than inferred: this file was the fourth orphan under
`receipts/`, and it is named in `run_all_receipts`' own SLOW tuple -- a per-file timeout budget
for a file the runner has never run, because the budget is written by hand and the file list is
read from the INDEX. **

P16_bbn_network ENGINE (imported by P16_validate_bbn.py). The genuine multi-nuclide BBN network for P16
sec:network: {n,p,D,T,3He,4He,7Li,7Be} on JINA REACLIB rates (pynucastro, forward + detailed-balance
reverse) + the corpus finite-T weak n<->p, integrated on the standard radiation-dominated cooling background
at the inherited eta. STATUS: gate-certified by P16_validate_bbn.py (verified r1401). Needs pynucastro.
"""
"""
D1 -- P16's owed computation: the full multi-abundance BBN network on the cooling leg.

WHAT THIS COMPUTES (P16 sec:network). P16 proves the cooling leg of the progenitor's
local thermal history IS a standard big-bang nucleosynthesis:
  * sec:rate   -- in the nuclear window the local Friedmann readout |H|=sqrt(8 pi G rho_r/3)
                  is IDENTICAL to standard BBN at every temperature (radiation included, L2);
  * sec:peak   -- the adiabatic infall peaks fully dissociated at Tpk >~ O(10^2) MeV >> T_D,
                  M-independently, so nucleosynthesis starts from free n,p;
  * sec:trev   -- a freeze-out lives ONLY on the cooling (expanding) leg; the turnaround makes it;
  * sec:network-- therefore the cooling leg reproduces the standard pattern at the inherited eta.
So D1 = run a genuine nuclear network on the standard cooling history and read off
(Y_p, D/H, 3He/H, 7Li/H). This retires P16's do-not-assert on the stated anchors.

RATES. Strong/EM/nuclear-weak reactions: JINA REACLIB (via pynucastro) -- the published,
peer-reviewed compilation, forward AND detailed-balance reverse rates. The thermal n<->p weak
conversion (finite-T lepton phase space, the piece REACLIB carries only as free decay) is spliced
in from the corpus's own validated module (Yp_freezeout.py, certified to 1.5% on Y_p).

BACKGROUND. Standard radiation-dominated cooling with e+- annihilation and nu decoupling
(g_*(T), g_{*s}(T), T_nu/T -> (4/11)^{1/3}); n_b tracked by entropy (n_b/s = const), normalized
to the inherited eta. This is the standard-BBN background BY sec:rate -- not a CR-specific choice.

GATE. Outputs are validated against accepted standard-BBN values at eta10=6.14 before any CR
claim is made: Y_p~0.247, D/H~2.5e-5, 3He/H~1.0e-5, 7Li/H~5.0e-10.
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d
import pynucastro as pyna

# ----------------------------------------------------------------------------------
# physical constants (MeV, s, cm, K units; natural where noted)
# ----------------------------------------------------------------------------------
MeV = 1.0
K_per_MeV = 1.160451e10          # 1 MeV = 1.16045e10 K
T9_per_MeV = K_per_MeV/1e9       # T9 = 1.16045 at T=1 MeV  -> T9/T_MeV = 11.6045
MeV_per_s = 1.0/6.582119569e-22  # hbar^-1  [1/s per MeV]
MPl = 1.22091e22 * MeV           # Planck mass
G_N = 1.0/MPl**2                 # in natural units
zeta3 = 1.2020569
Na = 6.02214076e23               # Avogadro
m_u = 1.66053907e-24             # g  (atomic mass unit)
me, Qnp, tau_n = 0.511, 1.29333, 879.4   # MeV, MeV, s
r_nu = (4.0/11.0)**(1.0/3.0)

# ----------------------------------------------------------------------------------
# 1) BACKGROUND: standard radiation-dominated cooling history  T9(t), rho_b(t)
#    (== the window rate, by P16 sec:rate)
# ----------------------------------------------------------------------------------
def Tnu_over_T(T_MeV):
    # neutrinos share the plasma T until ~ e+- annihilation, then decouple to (4/11)^1/3
    return 1.0 if T_MeV > 0.20 else r_nu

def _fe(T_MeV):
    # smooth e+- energy-density fade factor across m_e (0 -> 1 as T rises through ~m_e)
    return 1.0/(1.0+np.exp((np.log(0.17)-np.log(T_MeV))/0.15))

def gstar(T_MeV):
    # energy-density relativistic dof: photons(2) + e+-(7/8*4*fade) + 3 nu(7/8*2 each, at T_nu)
    ge = (7.0/8.0)*4.0*_fe(T_MeV)
    gnu = 3.0*(7.0/8.0)*2.0*Tnu_over_T(T_MeV)**4
    return 2.0 + ge + gnu

def gstar_s(T_MeV):
    # entropy dof
    ge = (7.0/8.0)*4.0*_fe(T_MeV)
    gnu = 3.0*(7.0/8.0)*2.0*Tnu_over_T(T_MeV)**3
    return 2.0 + ge + gnu

def rho_rad(T_MeV):
    # total radiation energy density [MeV^4]
    return (np.pi**2/30.0)*gstar(T_MeV)*T_MeV**4

def Hubble(T_MeV):
    # H = sqrt(8 pi G rho/3)  [MeV], then to 1/s
    H_nat = np.sqrt(8.0*np.pi*G_N*rho_rad(T_MeV)/3.0)
    return H_nat*MeV_per_s      # 1/s

def build_background(T9_hi=170.0, T9_lo=1.5e-2, N=9000, eta10=6.14):
    """Return interpolators t->T9, t->rho_b[g/cm^3], and T9 grid endpoints in time."""
    T9 = np.linspace(T9_hi, T9_lo, N)
    T = T9/T9_per_MeV                                  # MeV
    gs = np.array([gstar_s(t) for t in T])
    # scale factor from entropy: a ∝ 1/(gs^{1/3} T)  -> use x = gs^{1/3} T  (∝ 1/a)
    x = gs**(1.0/3.0)*T
    # dt = -da/(aH) ; a ∝ 1/x  => da/a = -dx/x ; dt = (dx/x)/H
    Harr = np.array([Hubble(t) for t in T])            # 1/s
    integrand = (1.0/x)/Harr                           # dt = integrand * dx ; but x decreases as T falls
    # integrate over x from high to low: t increases as T (and x) decrease
    # order by increasing t == decreasing T == decreasing x
    dxdt_sign = -np.gradient(x)                          # positive as T decreases
    dt = (dxdt_sign)/x/Harr
    t = np.concatenate([[0.0], np.cumsum(0.5*(dt[1:]+dt[:-1]))])
    t = t - t[0]
    # baryon density: n_b/s = const, normalized so that today's eta is recovered.
    # n_b(T) = (eta * n_gamma0 / s0) * s(T);  s(T)=(2pi^2/45) gs T^3 ; n_gamma=(2 zeta3/pi^2)T^3
    # ratio n_b/n_gamma at temperature T = eta * (gs(T)/gs0) * (n_gamma0-defn cancels) -> simpler:
    # n_b(T) = eta * (2 zeta3/pi^2) * T^3 * (gs(T)/gs_today) with gs_today=3.9091 (photon+nu entropy)
    gs_today = 2.0 + 3.0*(7.0/8.0)*2.0*r_nu**3
    eta = eta10*1e-10
    n_b_nat = eta*(2.0*zeta3/np.pi**2)*T**3*(gs/gs_today)   # [MeV^3]
    # convert MeV^3 -> cm^-3 : (MeV/hbar c)^3 ; hbar c = 197.3269804 MeV fm = 197.3e-13 MeV cm
    hbarc_cm = 197.3269804e-13                              # MeV cm
    n_b_cm3 = n_b_nat/hbarc_cm**3
    rho_b = n_b_cm3*m_u                                     # g/cm^3 (mass density ~ m_u per baryon)
    tT9 = interp1d(t, T9, kind='cubic', bounds_error=False, fill_value=(T9[0],T9[-1]))
    trho = interp1d(t, rho_b, kind='cubic', bounds_error=False, fill_value=(rho_b[0],rho_b[-1]))
    return t, T9, rho_b, tT9, trho, eta

# ----------------------------------------------------------------------------------
# 2) THERMAL WEAK n<->p  (spliced from the validated corpus module)
# ----------------------------------------------------------------------------------
def _pe(E): return np.sqrt(max(E*E-me*me, 0.0))
from scipy.integrate import quad
_I_dec = quad(lambda E:_pe(E)*E*(Qnp-E)**2, me, Qnp)[0]
_Cweak = 1.0/(tau_n*_I_dec)
def _fFD(E,T): return 1.0/(1.0+np.exp(np.clip(E/T,-500,500)))
def lam_np(T_MeV):                    # n->p  [1/s]
    Tn=Tnu_over_T(T_MeV)*T_MeV
    c1=quad(lambda E:_pe(E)*E*(E-Qnp)**2*_fFD(E-Qnp,Tn), Qnp, Qnp+80*T_MeV, limit=200)[0]
    c2=quad(lambda E:_pe(E)*E*(E+Qnp)**2*_fFD(E,T_MeV),    me, me+80*T_MeV, limit=200)[0]
    c3=quad(lambda E:_pe(E)*E*(Qnp-E)**2,                  me, Qnp, limit=200)[0]
    return _Cweak*(c1+c2+c3)
def lam_pn(T_MeV):                    # p->n  [1/s]
    Tn=Tnu_over_T(T_MeV)*T_MeV
    d1=quad(lambda E:_pe(E)*E*(E-Qnp)**2*_fFD(E,T_MeV),    Qnp, Qnp+80*T_MeV, limit=200)[0]
    d2=quad(lambda E:_pe(E)*E*(E+Qnp)**2*_fFD(E+Qnp,Tn),   me, me+80*T_MeV, limit=200)[0]
    return _Cweak*d1+_Cweak*d2

# tabulate the weak rates once (5-10x speedup vs per-step quad); interpolate in log T
_Tgrid = np.logspace(np.log10(15.0), np.log10(1e-3), 500)        # MeV (covers freeze-out)
_lnp_tab = np.array([lam_np(T) for T in _Tgrid])
_lpn_tab = np.array([lam_pn(T) for T in _Tgrid])
_lam_np_i = interp1d(np.log(_Tgrid), _lnp_tab, kind='cubic', bounds_error=False,
                     fill_value=(_lnp_tab[0],_lnp_tab[-1]))
_lam_pn_i = interp1d(np.log(_Tgrid), _lpn_tab, kind='cubic', bounds_error=False,
                     fill_value=(_lpn_tab[0],_lpn_tab[-1]))
def lam_np_fast(T): return float(_lam_np_i(np.log(T)))
def lam_pn_fast(T): return float(_lam_pn_i(np.log(T)))

# ----------------------------------------------------------------------------------
# 3) NETWORK from REACLIB, minus the free n-decay (replaced by thermal n<->p)
# ----------------------------------------------------------------------------------
def _pair_matches(r, setA, setB):
    """True if rate r is either direction of the reaction setA<->setB (by (Z,A) multiset sorted)."""
    rr=sorted((x.Z,x.A) for x in r.reactants); pp=sorted((x.Z,x.A) for x in r.products)
    a=sorted(setA); b=sorted(setB)
    return (rr==a and pp==b) or (rr==b and pp==a)

def build_network(scales=None, library='reaclib'):
    """scales: optional list of dicts {reac:set, prod:set, factor:f} -- multiplies BOTH directions
    of each named reaction's rate by f, for sensitivity/precision studies. Baseline: scales=None.
    library: 'reaclib' (JINA REACLIB, default) or 'starlib' (Sallaska et al. 2013, an independent
    Monte-Carlo evaluation) -- the precision cross-check on the light-nuclide rate evaluations."""
    lib = pyna.StarLibLibrary() if library=='starlib' else pyna.ReacLibLibrary()
    nuclei=['n','p','d','t','he3','he4','li7','be7']
    rc = pyna.RateCollection(libraries=[lib.linking_nuclei(nuclei)])
    # remove REACLIB's one-way free neutron decay (thermal n<->p supplied separately)
    # (a) free n-decay -> replaced by thermal n<->p ;  (b) >=3-body reactions -> negligible in
    # BBN and their high-density reverse rates overflow (BBN is a 2-body + photodissoc network).
    drop=[r for r in rc.rates if
          (len(r.reactants)==1 and str(r.reactants[0])=='n' and 'p' in {str(p) for p in r.products})
          or len(r.reactants)>=3]
    rc.remove_rates(drop)
    if scales:
        for sc in scales:
            f=sc['factor']; setA=list(sc['reac']); setB=list(sc['prod']); hit=0  # keep multiset (d+d!)
            for r in rc.rates:
                if _pair_matches(r,setA,setB):
                    _orig=r.eval
                    r.eval=(lambda T,_o=_orig,_f=f,*a,**k: _f*_o(T,*a,**k)); hit+=1
            sc['_hits']=hit
    return rc, list(rc.unique_nuclei), drop

# ----------------------------------------------------------------------------------
# 4) DRIVER
# ----------------------------------------------------------------------------------
_METHOD='LSODA'; _SOLVEKW={}; _TRAJ=False      # overridable for diagnostics
_SANITIZE=False                   # not needed once network starts at T9<=9 (REACLIB-valid)

def pre_evolve_np(t_bg, T9_bg, T9_hi=160.0, T9_net=9.0):
    """Weak freeze-out of n/p using ONLY the thermal n<->p rates (no REACLIB), from equilibrium
    at T9_hi down to T9_net. Returns X_n at T9_net -- the correctly-frozen neutron fraction that
    seeds the nuclear network (kept inside REACLIB's T9<~10 validity)."""
    from scipy.interpolate import interp1d as _i1
    T9_to_t = _i1(T9_bg, t_bg)
    ti = float(T9_to_t(T9_hi)); tf = float(T9_to_t(T9_net))
    T0 = T9_hi/T9_per_MeV
    Xn0 = 1.0/(1.0+np.exp(Qnp/T0))
    t_to_T9 = _i1(t_bg, T9_bg, bounds_error=False, fill_value=(T9_bg[0],T9_bg[-1]))
    def rhs(t,X):
        T = float(t_to_T9(t))/T9_per_MeV
        return [-lam_np_fast(T)*X[0] + lam_pn_fast(T)*(1.0-X[0])]
    s = solve_ivp(rhs,[ti,tf],[Xn0],method='LSODA',rtol=1e-8,atol=1e-11,max_step=(tf-ti)/200)
    return float(s.y[0,-1])

def run(eta10=6.14, T9_start=9.0, T9_end=8e-2, verbose=True, scales=None, library='reaclib'):
    # T9_end=0.08 is the freeze-out plateau: the trajectory shows D,He4,Li7 all stationary from
    # T9~0.3 down (dY<1% over T9 0.1->0.05). Reading yields here is standard; we deliberately do
    # NOT integrate into the T9<0.05 tail, where REACLIB fits extrapolate out of validity and
    # spuriously over-burn D over the ~1e6 s inert stretch.
    t_bg,T9_bg,rho_bg,tT9,trho,eta = build_background(eta10=eta10)
    rc,nuclist,dropped = build_network(scales=scales, library=library)
    from pynucastro import Composition
    nuc = rc.unique_nuclei
    A = np.array([n.A for n in nuc])
    # index by (Z,A) so naming/capitalization is irrelevant
    za = {(n.Z,n.A):i for i,n in enumerate(nuc)}
    idx = {'n':za[(0,1)],'p':za[(1,1)],'d':za[(1,2)],'t':za[(1,3)],
           'he3':za[(2,3)],'he4':za[(2,4)],'li7':za[(3,7)],'be7':za[(4,7)]}

    # start/end times from background
    ti = float(interp1d(T9_bg, t_bg)(T9_start))
    tf = float(interp1d(T9_bg, t_bg)(T9_end))

    # initial n/p: pre-evolved through weak freeze-out (thermal rates only) down to T9_start,
    # which lies inside REACLIB's validity so the nuclear network never sees out-of-range fits.
    Xn0 = pre_evolve_np(t_bg, T9_bg, T9_net=T9_start)
    Y = np.zeros(len(nuc))
    Y[idx['n']] = Xn0
    Y[idx['p']] = (1.0-Xn0)
    # (Y_i = X_i/A_i ; for n,p A=1)

    comp = Composition(nuc)
    def set_comp(Yv):
        for i,n in enumerate(nuc):
            comp.X[n] = max(Yv[i],0.0)*n.A
        return comp

    def rhs(t, Yv):
        T9 = float(tT9(t)); T = T9/T9_per_MeV
        rho = float(trho(t))
        set_comp(Yv)
        with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
            yd = rc.evaluate_ydots(rho, T9*1e9, comp)     # pyna wants T in K
            dY = np.array([yd[n] for n in nuc])
        # At the high-T start the strongly-bound nuclei (He4,Li7,Be7) are pinned at ~0 by
        # bottleneck photodissociation whose reverse rate overflows float; inf x (~0 abundance)
        # -> nan. Those nuclei's TRUE ydot is ~0 (they cannot form yet), so sanitize to 0.
        if _SANITIZE:
            dY = np.nan_to_num(dY, nan=0.0, posinf=0.0, neginf=0.0)
        # thermal weak n<->p  (dY/dt in molar fraction/s ; Y_n,Y_p are number per baryon)
        wnp, wpn = lam_np_fast(T), lam_pn_fast(T)
        dn = -wnp*Yv[idx['n']] + wpn*Yv[idx['p']]
        dY[idx['n']] += dn
        dY[idx['p']] -= dn
        return dY

    def jac(t, Yv):
        T9 = float(tT9(t)); T = T9/T9_per_MeV
        rho = float(trho(t))
        set_comp(Yv)
        with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
            J = np.array(rc.evaluate_jacobian(rho, T9*1e9, comp))
        J = np.nan_to_num(J, nan=0.0, posinf=0.0, neginf=0.0)
        # add thermal weak n<->p Jacobian terms
        wnp, wpn = lam_np_fast(T), lam_pn_fast(T)
        i_n,i_p = idx['n'],idx['p']
        J[i_n,i_n]+=-wnp; J[i_n,i_p]+= wpn
        J[i_p,i_n]+= wnp; J[i_p,i_p]+=-wpn
        return J

    # per-species atol scaled to each nuclide's peak abundance -- a flat atol=1e-16 forces LSODA
    # to resolve heavy nuclides that are ~0 in the early transient, collapsing the step size.
    atol_vec = np.full(len(nuc), 1e-12)
    atol_vec[idx['n']] = atol_vec[idx['p']] = 1e-10
    # retry ladder: the stiff n+p<->d transient makes a single (method,rtol) fail erratically at
    # some eta; re-solving with a nudged tolerance/method reliably converges (same physical answer).
    attempts = [(_METHOD,1e-5),(_METHOD,3e-6),(_METHOD,1e-4),('BDF',1e-6),('Radau',1e-5)]
    sol=None
    for meth,rt in attempts:
        s = solve_ivp(rhs,[ti,tf],Y,method=meth,rtol=rt,atol=atol_vec,jac=jac,
                      dense_output=_TRAJ,**_SOLVEKW)
        if s.success and s.y[idx['he4'],-1]>1e-3:   # a real freeze-out, not a stalled solve
            sol=s; break
        sol=s
    if _TRAJ:
        print(f"  --- trajectory (eta10={eta10}) ---")
        print(f"    {'T9':>7s} {'t[s]':>9s} {'Y_n':>10s} {'Y_p':>8s} {'Y_d':>10s} {'Y_he4':>10s} {'Y_li7':>10s}")
        for T9c in [1.5,1.0,0.9,0.8,0.7,0.5,0.3,0.1,0.05]:
            tc=float(interp1d(T9_bg,t_bg)(T9c))
            if not (sol.t[0]<=tc<=sol.t[-1]): continue
            yy=sol.sol(tc)
            print(f"    {T9c:7.2f} {tc:9.1f} {yy[idx['n']]:10.3e} {yy[idx['p']]:8.4f} "
                  f"{yy[idx['d']]:10.3e} {yy[idx['he4']]:10.3e} {yy[idx['li7']]+yy[idx['be7']]:10.3e}")
    Yf = sol.y[:,-1]
    Yf = np.clip(Yf,0,None)

    # abundances
    Yp_mass = Yf[idx['he4']]*4.0                       # He-4 mass fraction
    H_num = Yf[idx['p']] + Yf[idx['d']] + Yf[idx['t']]  # hydrogen-ish? no: H nuclei = p only for /H ratio
    Hn = Yf[idx['p']]                                   # free protons ~ all H at end
    DH   = Yf[idx['d']]/Hn
    He3H = Yf[idx['he3']]/Hn
    Li7H = (Yf[idx['li7']]+Yf[idx['be7']])/Hn           # 7Be decays to 7Li later
    Zarr = np.array([n.Z for n in nuc])
    baryon = float(np.sum(A*Yf))            # should be 1 (baryon number per baryon)
    charge = float(np.sum(Zarr*Yf))         # should equal initial proton fraction
    out = dict(eta10=eta10, Yp=Yp_mass, DH=DH, He3H=He3H, Li7H=Li7H,
               Yn=Yf[idx['n']], Yp_free=Yf[idx['p']], t_end=sol.t[-1], nfev=sol.nfev,
               baryon_sum=baryon, charge_sum=charge,
               success=sol.success, message=sol.message)
    if verbose:
        print(f"eta10={eta10}: Yp={Yp_mass:.4f}  D/H={DH:.3e}  3He/H={He3H:.3e}  7Li/H={Li7H:.3e}")
        print(f"   integ: success={sol.success} t_end={sol.t[-1]:.1f}s nfev={sol.nfev}  {sol.message}")
    return out

if __name__=='__main__':
    print("=== background sanity ===")
    t_bg,T9_bg,rho_bg,tT9,trho,eta = build_background()
    for Tmev in [10,2,1,0.3,0.086,0.03]:
        T9c=Tmev*T9_per_MeV
        tc=float(interp1d(T9_bg,t_bg)(T9c)) if T9_bg.min()<T9c<T9_bg.max() else float('nan')
        print(f"  T={Tmev:6.3f} MeV (T9={T9c:6.3f})  t={tc:9.2f}s  H={Hubble(Tmev):.3e}/s  rho_b={float(trho(tc)) if tc==tc else float('nan'):.3e} g/cc")
    print("\n=== weak-rate sanity (detailed balance lam_pn/lam_np vs exp(-Q/T)) ===")
    for Tmev in [2.0,1.0,0.8,0.7]:
        print(f"  T={Tmev} MeV: lam_pn/lam_np={lam_pn(Tmev)/lam_np(Tmev):.3f}  exp(-Q/T)={np.exp(-Qnp/Tmev):.3f}  lam_np/H={lam_np(Tmev)/Hubble(Tmev):.2f}")
    print("\n=== BBN run at eta10=6.14 ===")
    run(eta10=6.14)

    # ** r2376+c54.161: this file is the shared BBN ENGINE, imported by the receipts rather than
    #    registered as one -- and it was the last file in the tree carrying no check of any kind.
    #    A library that no one asserts anything about is exactly where a silent regression lives,
    #    so its __main__ path now pins the two figures P16 quotes from it, under both rate
    #    libraries.  ** The engine can now fail on its own, not only through its callers. **
    _oR = run(eta10=6.14, verbose=False, library='reaclib')
    _oS = run(eta10=6.14, verbose=False, library='starlib')
    print(f"\n  ENGINE SELF-CHECK: StarLib D/H {_oS['DH']:.4e}, 7Li/H {_oS['Li7H']:.4e}; "
          f"REACLIB D/H {_oR['DH']:.4e}, 7Li/H {_oR['Li7H']:.4e}")
    assert abs(_oS['DH'] / 2.4980e-05 - 1) < 0.01, f"StarLib D/H moved: {_oS['DH']:.4e}"
    assert abs(_oS['Li7H'] / 5.1448e-10 - 1) < 0.02, f"StarLib 7Li/H moved: {_oS['Li7H']:.4e}"
    assert abs(_oR['DH'] / 2.5671e-05 - 1) < 0.01, f"REACLIB D/H moved: {_oR['DH']:.4e}"
    assert abs(_oS['Yp'] * 1.016 / 0.2471 - 1) < 0.005, f"Y_p moved: {_oS['Yp']*1.016:.4f}"
    print("  ENGINE SELF-CHECK PASSES")
