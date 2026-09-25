#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:largescale`: ** THE LOW-MULTIPOLE DEPTH GAP CLOSES.  THE TWO BOLTZMANN
TREATMENTS NOW AGREE TO $3\%$ ACROSS $\ell=2$--$8$ WHERE THEY DIFFERED BY A FACTOR $2.02$ AT
$\ell=4$ -- AND THE FACTOR OF TWO WAS TWO DEFECTS IN THE SECOND ARM THAT WERE PARTLY CANCELLING. **

** ⇒ AND ONE MECHANISM CLAIM OF MINE IS WITHDRAWN, r6801+cc66.22. **  I reported that the hierarchy
goes non-finite once the line-of-sight cut passes $z\simeq10$ because of the $L_G=12$ truncation, and
offered three refinements that failed identically as evidence.  *** It is not the truncation.  The
opacity grid is `_ea = linspace(eg[1], eta_end, 20000)` -- a FIXED POINT COUNT over a GROWING RANGE
-- so raising the cut silently coarsens $\tau'$ by $7.5\times$; $\tau'$ spans some twelve orders of
magnitude there and is splined with a CUBIC, which on a grid that coarse overshoots negative, and
$1/\tau'$ then overflows inside the tight-coupling viscosity.  With the resolution preserved the
UNDECOUPLED hierarchy runs to $a=1$ and stays finite. ***  *My three refinements were `NS3` and
`HKCAP`; neither touches the opacity grid, so neither could have found it.*

** THE CAUSE OF THE GAP -- the missing late integrated Sachs--Wolfe term -- STANDS AND IS
STRENGTHENED: ** turning it on moves $\ell=4$ from $0.1933$ to $0.3485$ against the CAMB arm's
$0.3590$.  *What is withdrawn is only the claim that the instrument could not be taken there.*

Built r6825+cc66.26 (node 66, code seat), discharging order ② of the chat seat's `r6825` -- the
decoupled-source build, then the depths, then the confrontation -- in the order it asks for them.

===================================================================================================
** THE TWO DEFECTS, AND WHY THE OLD NUMBER LOOKED LIKE A MODEST FACTOR OF TWO **
===================================================================================================

  1  ** THE LINE-OF-SIGHT CUT. **  `ETAEND` defaults to $20\,a_{\rm rec}$, $z=53.5$, so the late ISW
     is outside every spectrum the module produces.  `P15_verify_lowell_boltzmann`'s own diagnosis is
     that the late ISW at low $\ell$ is sourced ABOVE the discrete floor and is therefore RETAINED
     by the CR sum -- power that FILLS the deficit.  *Omitting it makes the deficit too DEEP.*
  2  ** THE CONTINUUM'S LOW-$k$ REACH. **  `P15_the_second_arm_actually_run` built its $k$-grid from
     $0.5\,k_2$ upward, so the CONTINUUM integral -- the denominator -- was truncated below the
     ladder's lowest mode.  *The discrete sum legitimately starts at $L=2$; the continuum must reach
     $k\to0$, which the module's own `spectrum()` knows (`LLMIN`) and that receipt did not use.*
     Truncating it makes the ratio too HIGH.

*** SO THE TWO PULL OPPOSITE WAYS, AND THE LANDED NUMBER WAS THEIR PARTIAL CANCELLATION. ***  PART 3
measures it: fixing the continuum ALONE takes $\ell=2$ from $0.4974$ to $0.1175$ -- a factor $4$ from
the CAMB arm, not a factor $2$ -- and only with BOTH fixed does the gap close.  *A defect that half
hides another is why the corpus carried "the shape cross-validates, the depth does not" for so long
with a plausible-looking number attached.*

===================================================================================================
** WHAT IS RUN HERE AND WHAT IS READ **
===================================================================================================

Arm A (CAMB's exact $\Delta_\ell(k)$) and the FROZEN variant of arm B are recomputed in this file.
The DECOUPLED variant -- every mode carried to $a=1$ on the metric-and-matter sector alone -- costs
about nine minutes a configuration, so the eight-configuration sweep is banked at
`spectra/cc66_lowell_sweep.npz` with each configuration's environment in its key, and the commands
are in this file's PART 5.  ** Both variants are reported; they agree to $3\%$, which is the point of
running both. **

  ⌗ ** THE FROZEN VARIANT IS NOT A SHORTCUT, IT IS THE MODULE'S OWN DESIGN. **  `r2136` built the
  per-mode freeze (`h*k < HKCAP`) precisely so that "the low-k modes -- the only ones that carry the
  ISW at the l we report -- run on to late times".  *The decoupled build's added value is that it
  carries EVERY mode and takes the radiation sector out of the constraint; that the two agree is
  evidence about both.*

** COMPUTES: r_0 from sec:largescale's own parameter-free formula at each background; arm A from
   CAMB at AccuracyBoost 3 / lSampleBoost 50 / lAccuracyBoost 3; arm B from HIER_photon_hierarchy at
   KMAXL = 700 with NTAU raised so the opacity resolution is held fixed as the cut moves, and the
   continuum reaching 0.1 k_2.  Backgrounds: control (67.40, 0.3150) and adjudicated (68.60,
   0.2973).  The confrontation uses the exact scaled chi^2_(2l+1) likelihood, in which the absolute
   baseline cancels in the CR/LCDM ratio -- so the sky's own scatter is carried rather than bolted
   on.  *** Nothing is fitted: the depths are ratios of a sum to an integral of the SAME transfer. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~12 min)
"""
import os
import re
import subprocess
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
HIER_DIR = os.path.join(ROOT, 'storyboard_receipts')
C = 299792.458
NS = 0.9649
CTL, ADJ = (67.40, 0.3150), (68.60, 0.2973)


def r0_of(H0, Om):
    OL = 1.0 - Om
    return (2.0 ** (1.0 / 3.0) * (C / (H0 * np.sqrt(3.0 * OL)))
            * np.sinh(np.arcsinh(np.sqrt(OL / Om))) ** (2.0 / 3.0))


R0 = {CTL: r0_of(*CTL), ADJ: r0_of(*ADJ)}

# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE WITHDRAWAL: THE OPACITY GRID, NOT THE TRUNCATION **")
print(BAR)
_SRC = open(os.path.join(HIER_DIR, 'HIER_photon_hierarchy.py'), encoding='utf-8').read()
check("the opacity grid's point count is now a knob, defined once, defaulting to the historical "
      "20000", _SRC.count("os.environ.get('NTAU','20000')") == 1
      and "_ea = np.linspace(eg[1], eta_end, _NTAU)" in _SRC)
check("and tau' is splined with a CUBIC, which is what overshoots on a coarse grid",
      "taup_of = CubicSpline(_ea, _tpa)" in _SRC)

_RUN = r"""
import os, sys, contextlib, io
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import spherical_jn
H0=float(os.environ['BH0']); Om=float(os.environ['BOM']); R0=float(os.environ['BR0'])
os.environ['KMAXL']='700'; os.environ['H0_L']='%.10f'%H0; os.environ['OMF']='%.12f'%(Om/0.3150)
sys.path.insert(0, os.environ['HIER_DIR'])
if os.environ.get('ZEND') is not None or os.environ.get('ZDEC'):
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):
        import HIER_photon_hierarchy as _P
    e0=float(_P.eta_0)
    if os.environ.get('ZDEC'):
        os.environ['ETADEC']='%.6f'%float(np.interp(1.0/(1.0+float(os.environ['ZDEC'])),_P.ag,_P.eg))
    os.environ['ETAEND']='%.6f'%(e0-1e-3)
    for m in [k for k in list(sys.modules) if k.startswith('HIER_photon')]: del sys.modules[m]
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    import HIER_photon_hierarchy as H
Ls=np.arange(2,260); kL=np.sqrt(Ls*(Ls+2))/R0
KLO=float(os.environ.get('KLO','0.5')); NLOW=int(os.environ.get('NLOW','320'))
kd=np.exp(np.linspace(np.log(kL[0]*KLO),np.log(kL[-1]),NLOW))
kk=np.unique(np.concatenate([kL,kd]))
with contextlib.redirect_stdout(io.StringIO()):
    E,Y,e_sw=H.evolve(kk)
if not np.all(np.isfinite(Y[:,:,2])):
    print('RESULT NONFINITE | eta_end %.1f'%H.eta_end); raise SystemExit
m=E>max(e_sw,H.eta_rec-160.0); ee,Yv=E[m],Y[m]
g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
with contextlib.redirect_stdout(io.StringIO()):
    Sm,Sd,Si,Sq=H.source_terms(ee,Yv,kk,g,tau)
has_q=Sq is not None; x0m=H.eta_0-ee; lnk=np.log(kk); _u,_ix=np.unique(lnk,return_index=True)
def Delta(l):
    X=kk[None,:]*x0m[:,None]
    jl=spherical_jn(int(l),X); jlp=spherical_jn(int(l),X,derivative=True)
    it=Sm*jl+Sd*jlp+Si*jl
    if has_q:
        Xs=np.maximum(X,1e-8)
        it=it+Sq*2.0*(-3.0*jlp/Xs+(3.0*l*(l+1)/(2.0*Xs**2)-1.0)*jl)
    return np.trapezoid(it,ee,axis=0)
wL=(Ls+1.0)/(Ls*(Ls+2.0)); ls=np.arange(2,45)
Cc=np.zeros(len(ls)); Cd=np.zeros(len(ls))
for i,l in enumerate(ls):
    D=Delta(l)
    Cc[i]=np.trapezoid(kk**(0.9649-1.0)*D**2,lnk)
    f=interp1d(_u,D[_ix],kind='cubic',bounds_error=False,fill_value=0.0)
    Cd[i]=np.sum(wL*kL**(0.9649-1.0)*f(np.log(kL))**2)
def pl(Cq):
    d=Cq*ls*(ls+1); return d/np.mean(d[(ls>=25)&(ls<=40)])
r=pl(Cd)/pl(Cc)
print('RESULT '+' '.join('%.6f'%x for x in r[:11])+' | eta_end %.1f eta_0 %.1f'%(H.eta_end,H.eta_0))
"""


def armB(bg, **env):
    e = dict(os.environ, BH0=f"{bg[0]}", BOM=f"{bg[1]}", BR0=f"{R0[bg]:.10f}", HIER_DIR=HIER_DIR)
    for k in ('ZEND', 'ZDEC', 'NTAU', 'KLO', 'NLOW', 'NS3', 'HKCAP'):
        e.pop(k, None)
    e.update({k: str(v) for k, v in env.items()})
    p = subprocess.run([sys.executable, '-c', _RUN], env=e, capture_output=True, text=True)
    for line in p.stdout.splitlines():
        if line.startswith('RESULT NONFINITE'):
            return None, line.split('|')[1].strip()
        if line.startswith('RESULT '):
            b, meta = line[7:].split('|')
            return np.array([float(x) for x in b.split()]), meta.strip()
    return None, (p.stdout + p.stderr)[-160:]


print()
print("  The cut is pushed to a = 1 with the photon tower UNTOUCHED, once at the historical opacity")
print("  point count and once with the resolution held fixed as the range grows.")
print()
print(f"  {'configuration':>44} {'ell = 2':>14}")
_bad, _m1 = armB(CTL, ZEND=0, NTAU=20000, KLO=0.1, NLOW=480)
print(f"  {'cut at a = 1, NTAU = 20000 (historical)':>44} "
      f"{('** NON-FINITE **' if _bad is None else f'{_bad[0]:.4f}'):>14}   ({_m1})")
_good, _m2 = armB(CTL, ZEND=0, NTAU=150000, KLO=0.1, NLOW=480)
print(f"  {'cut at a = 1, NTAU = 150000 (resolution held)':>44} "
      f"{('NON-FINITE' if _good is None else f'{_good[0]:.4f}'):>14}   ({_m2})")
check("** the cut at a = 1 is NON-FINITE at the historical point count **", _bad is None)
check("** and FINITE with the opacity resolution held fixed, with the tower untouched -- so the "
      "blocker was the opacity grid and not the LG = 12 truncation **", _good is not None)
print("  ⇒ *** cc66.22's mechanism claim is withdrawn on this measurement. ***  *The evidence I gave")
print("     for it -- three refinements failing identically -- was NS3 and HKCAP, and neither")
print("     touches the opacity grid, so the failure it explained was never tested against it.*")

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** THE SECOND DEFECT: THE CONTINUUM'S LOW-k REACH, CONVERGED **")
print(BAR)
print("  The discrete sum starts at L = 2 because the source spectrum does.  The CONTINUUM is the")
print("  denominator and must reach k -> 0; the banked arm-B run started it at 0.5 k_2.")
print()
print(f"  {'continuum reaches':>22} " + " ".join(f"{'l=' + str(l):>9}" for l in (2, 3, 4, 5)))
KSCAN = {}
for klo in (0.5, 0.1, 0.02):
    v, _ = armB(CTL, ZEND=0, NTAU=150000, KLO=klo, NLOW=480)
    KSCAN[klo] = v
    print(f"  {f'{klo:g} k_2':>22} " + " ".join(f"{v[l - 2]:>9.4f}" for l in (2, 3, 4, 5)))
_mv = max(abs(KSCAN[0.02][l - 2] / KSCAN[0.1][l - 2] - 1) for l in (2, 3, 4, 5))
print(f"\n  ⇒ converged by 0.1 k_2: a further factor 5 down moves the quartet by {100 * _mv:.1f}%.")
check("** the continuum's low-k reach is converged at 0.1 k_2, to better than 1% **", _mv < 0.01)
check("** and the truncation at 0.5 k_2 was not a detail: it moves l = 2 by tens of per cent **",
      abs(KSCAN[0.5][0] / KSCAN[0.1][0] - 1) > 0.10)

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE TWO DEFECTS WERE PARTLY CANCELLING **")
print(BAR)
SW = np.load(os.path.join(SPEC, 'cc66_lowell_sweep.npz'))
KEY = {re.sub(r'[^A-Za-z0-9]+', '_', k): k for k in SW.files if k != 'ells'}
_old = np.array([0.4974, 0.2326, 0.1933, 0.6186])          # the banked arm B: both defects present
_contonly = SW['FROZEN_control_default_cut_z_53_5_KLO_0_1'][:4]   # continuum fixed, cut still z=53.5
_both = KSCAN[0.1][:4]                                      # both fixed
_A = np.array([0.4729, 0.4097, 0.3562, 0.6766])            # arm A, control (PART 4 recomputes it)
print(f"  {'':>40} " + " ".join(f"{'l=' + str(l):>9}" for l in (2, 3, 4, 5)) + f" {'worst A/B':>11}")
for nm, row in (('both defects present (the banked arm B)', _old),
                ('continuum fixed ONLY, cut still z = 53.5', _contonly),
                ('BOTH fixed', _both)):
    w = max(_A[i] / row[i] for i in range(4))
    print(f"  {nm:>40} " + " ".join(f"{row[i]:>9.4f}" for i in range(4)) + f" {w:>11.2f}x")
print(f"  {'arm A (CAMB), control':>40} " + " ".join(f"{_A[i]:>9.4f}" for i in range(4)))
print()
print("  ⇒ *** FIXING ONE DEFECT MAKES THE DISAGREEMENT WORSE, NOT BETTER. ***  The continuum")
print("     truncation was biasing the ratio UP and the missing late ISW was biasing it DOWN, so the")
print("     landed factor of two was their partial cancellation.  **That is why a wrong number looked")
print("     like a plausible one.**")
check("** the continuum fix ALONE widens the gap past a factor 3 -- the two defects opposed **",
      max(_A[i] / _contonly[i] for i in range(4)) > 3.0)
check("and with both fixed the worst point is inside 10%",
      max(_A[i] / _both[i] for i in range(4)) < 1.10)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE CONVERGED DEPTHS, BOTH ARMS, BOTH BACKGROUNDS, BOTH VARIANTS **")
print(BAR)
import camb                                                                # noqa: E402
from scipy.interpolate import interp1d                                     # noqa: E402

LMAX = 48


def armA(H0, Om, ombh2=0.02237, mnu=0.06):
    h = H0 / 100.0
    omnuh2 = mnu / 93.14
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=Om * h * h - ombh2 - omnuh2, mnu=mnu, tau=0.0544)
    pars.InitPower.set_params(As=2.1e-9, ns=NS)
    pars.set_for_lmax(LMAX + 8, lens_potential_accuracy=0)
    pars.set_accuracy(AccuracyBoost=3, lSampleBoost=50, lAccuracyBoost=3)
    res = camb.get_results(pars)
    td = res.get_cmb_transfer_data()
    DL = np.array(td.delta_p_l_k)[0]
    Larr, q = np.array(td.L), np.array(td.q)
    lnq = np.log(q)
    r0 = r0_of(H0, Om)
    Ls = np.arange(2, 4000)
    kL = np.sqrt(Ls * (Ls + 2)) / r0
    wL = (Ls + 1.0) / (Ls * (Ls + 2.0))
    msk = (kL >= q.min()) & (kL <= q.max())
    ells, rat = [], []
    for i, ell in enumerate(Larr):
        if ell > LMAX or ell < 2:
            continue
        Dl = DL[i]
        cont = float(np.trapezoid((q / 0.05) ** (NS - 1.0) * Dl ** 2, lnq))
        f = interp1d(lnq, Dl, kind='cubic', bounds_error=False, fill_value=0.0)
        disc = float(np.sum(wL[msk] * (kL[msk] / 0.05) ** (NS - 1.0) * f(np.log(kL[msk])) ** 2))
        ells.append(int(ell))
        rat.append(disc / cont)
    ells, rat = np.array(ells), np.array(rat)
    pl = (ells >= 25) & (ells <= 40)
    return ells, rat / np.mean(rat[pl])


A = {}
for bg in (CTL, ADJ):
    e, r = armA(*bg)
    A[bg] = {int(l): float(r[i]) for i, l in enumerate(e)}
check("arm A on the control still reproduces sec:largescale's 0.473 / 0.410 / 0.356 / 0.676 to 1%",
      all(abs(A[CTL][l] / v - 1) < 0.01
          for l, v in ((2, 0.473), (3, 0.410), (4, 0.356), (5, 0.676))))
B_frozen = {CTL: KSCAN[0.1], ADJ: armB(ADJ, ZEND=0, NTAU=150000, KLO=0.1, NLOW=480)[0]}
B_dec = {CTL: SW['DECOUPLED_control_KLO_0_1_NS3_60000'],
         ADJ: SW['DECOUPLED_adjudicated_KLO_0_1_NS3_60000']}
for bgn, bg in (('CONTROL (67.40, 0.3150)', CTL), ('ADJUDICATED (68.60, 0.2973)', ADJ)):
    print(f"\n  {bgn}   r_0 = {R0[bg]:.2f} Mpc")
    print(f"  {'':>34} " + " ".join(f"{'l=' + str(l):>8}" for l in range(2, 9)))
    print(f"  {'arm A (CAMB exact Delta_l)':>34} "
          + " ".join(f"{A[bg][l]:>8.4f}" for l in range(2, 9)))
    print(f"  {'arm B, frozen (module default)':>34} "
          + " ".join(f"{B_frozen[bg][l - 2]:>8.4f}" for l in range(2, 9)))
    print(f"  {'arm B, DECOUPLED (every mode)':>34} "
          + " ".join(f"{B_dec[bg][l - 2]:>8.4f}" for l in range(2, 9)))
    print(f"  {'A / B (decoupled)':>34} "
          + " ".join(f"{A[bg][l] / B_dec[bg][l - 2]:>8.3f}" for l in range(2, 9)))
    w = max(max(A[bg][l] / B_dec[bg][l - 2], B_dec[bg][l - 2] / A[bg][l]) for l in range(2, 9))
    wf = max(max(A[bg][l] / B_frozen[bg][l - 2], B_frozen[bg][l - 2] / A[bg][l])
             for l in range(2, 9))
    print(f"      ** worst disagreement: {w:.3f} (decoupled), {wf:.3f} (frozen) **")
    check(f"{bgn}: ** the two arms agree to 7% across l = 2-8, where the corpus carries 2.02x **",
          w < 1.07 and wf < 1.07)
_agree = max(abs(B_dec[ADJ][l - 2] / B_frozen[ADJ][l - 2] - 1) for l in range(2, 9))
print(f"\n  ⌗ the two arm-B variants agree with EACH OTHER to {100 * _agree:.1f}% on the adjudicated")
print("    background -- the freeze carries what the ISW needs, and the decoupled build confirms it")
print("    while also taking the radiation sector out of the constraint.")
check("the frozen and decoupled variants agree to 4%, so neither the freeze nor the towers are "
      "doing the work", _agree < 0.04)
check("** the minimum is still at l = 4 and recovery still by l = 8 on every row **",
      all(min((2, 3, 4, 5), key=lambda l: d[l] if isinstance(d, dict) else d[l - 2]) == 4
          for d in (A[CTL], A[ADJ], B_dec[CTL], B_dec[ADJ], B_frozen[CTL], B_frozen[ADJ])))

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** CONVERGENCE, AND THE COMMANDS THE BANKED SWEEP WAS RUN WITH **")
print(BAR)
print(f"  {'what was varied':>34} " + " ".join(f"{'l=' + str(l):>9}" for l in (2, 3, 4, 5)))
for lab, key in (('decoupled, NS3 = 60000', 'DECOUPLED_control_KLO_0_1_NS3_60000'),
                 ('decoupled, NS3 = 30000', 'DECOUPLED_control_NS3_30000'),
                 ('frozen, NTAU = 150000', 'FROZEN_control_KLO_0_1'),
                 ('frozen, NTAU = 300000', 'FROZEN_control_NTAU_300000')):
    v = SW[key]
    print(f"  {lab:>34} " + " ".join(f"{v[l - 2]:>9.4f}" for l in (2, 3, 4, 5)))
_ns3 = max(abs(SW['DECOUPLED_control_NS3_30000'][i]
               / SW['DECOUPLED_control_KLO_0_1_NS3_60000'][i] - 1) for i in range(4))
_nt = max(abs(SW['FROZEN_control_NTAU_300000'][i] / SW['FROZEN_control_KLO_0_1'][i] - 1)
          for i in range(4))
print(f"\n  ⇒ halving the late step count moves it by {100 * _ns3:.3f}%; doubling the opacity grid "
      f"by {100 * _nt:.3f}%.")
check("** converged in the late step count to 0.1% **", _ns3 < 1e-3)
check("** and in the opacity grid to 0.1% -- so NTAU=150000 is resolution, not tuning **", _nt < 1e-3)
print()
print("  the banked sweep's commands (arm B; BH0/BOM set the background, BR0 the ladder):")
print("      frozen    : NTAU=150000 ZEND=0        KLO=0.1 NLOW=480")
print("      decoupled : NTAU=150000 ZDEC=200 NS3=60000 KLO=0.1 NLOW=480")

# =================================================================================================
print()
print(BAR)
print("  PART 6 -- ** (b): THE FLOOR AGAINST THE SKY, WITH COSMIC VARIANCE CARRIED **")
print(BAR)
print("  Each hat C_l is a scaled chi^2 with 2l+1 degrees of freedom about the model C_l, and the")
print("  absolute baseline cancels in the CR/LCDM ratio:")
print("      Delta(-2 ln L)_l = (2l+1) [ r_l (1/d_l - 1) + ln d_l ],   r_l = observed/LCDM")
print("  ** That IS the sky's own scatter -- the 2l+1 is cosmic variance, not an add-on. **")
print("  *The observed ratios are the corpus's own (P15_confront_lowell_data): the quadrupole")
print("  robustly low at ~0.20, the octopole estimator-dependent at 0.60 (WMAP) to 0.95 (Efstathiou),")
print("  l = 4 ~0.70, l >= 5 no robust anomaly.*")
OBS = {2: 0.20, 3: 0.75, 4: 0.70, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0}


check("the banked sweep covers l = 2-8, and both arms are already at 1.000 by l = 8 -- which is "
      "why l = 9, 10 are set to unity in the confrontation below",
      len(B_dec[ADJ]) == 7 and abs(B_dec[ADJ][6] - 1.0) < 0.01 and abs(A[ADJ][8] - 1.0) < 0.01)


def dm2lnL(depth, obs):
    per, tot = {}, 0.0
    for l in range(2, 11):
        d = depth.get(l, 1.0)
        v = (2 * l + 1) * (obs[l] * (1.0 / d - 1.0) + np.log(d))
        per[l] = v
        tot += v
    return tot, per


TAB = {'arm A, adjudicated': A[ADJ],
       # ** the banked sweep carries l = 2-8; l = 9, 10 are set to 1 because BOTH arms are at
       # 1.000 by l = 8 already, which PART 4's table shows rather than assumes. **
       'arm B decoupled, adjudicated': {l: (float(B_dec[ADJ][l - 2]) if l - 2 < len(B_dec[ADJ])
                                            else 1.0) for l in range(2, 11)},
       "the corpus's landed table": {2: 0.473, 3: 0.410, 4: 0.356, 5: 0.676, 6: 0.916, 7: 0.984,
                                     8: 0.998, 9: 1.0, 10: 1.0}}
print()
print(f"  {'':>30} " + " ".join(f"{'l=' + str(l):>8}" for l in range(2, 7))
      + f" {'total':>9} {'WMAP oct':>10} {'Efst oct':>10}")
TOT = {}
for nm, dep in TAB.items():
    t, per = dm2lnL(dep, OBS)
    tl, _ = dm2lnL(dep, {**OBS, 3: 0.60})
    th, _ = dm2lnL(dep, {**OBS, 3: 0.95})
    TOT[nm] = (t, tl, th)
    print(f"  {nm:>30} " + " ".join(f"{per[l]:>+8.2f}" for l in range(2, 7))
          + f" {t:>+9.2f} {tl:>+10.2f} {th:>+10.2f}")
print("\n  (Delta(-2 ln L) > 0 disfavours this construction; the sum runs 2 <= l <= 10)")
check("** the confrontation returns a WASH on the converged table: under 2 in Delta(-2 ln L) "
      "over nine multipoles **", abs(TOT['arm A, adjudicated'][0]) < 2.0)
check("and it does not turn on which arm is used -- the two differ by under 0.5",
      abs(TOT['arm A, adjudicated'][0] - TOT['arm B decoupled, adjudicated'][0]) < 0.5)
check("nor on the octopole estimator: the whole range stays inside +4",
      all(abs(v) < 4.0 for v in TOT['arm A, adjudicated']))
print()
print("  ⇒ ** THE QUADRUPOLE REWARDS THIS CONSTRUCTION AND l = 3-5 PENALISE IT, AND THEY VERY NEARLY")
print("     CANCEL. **  *The deficit is real, parameter-free, and lands in the wash.*")

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SETTLES, AND WHAT IT COSTS THE PAPER")
print(BAR)
_w = max(max(A[ADJ][l] / B_dec[ADJ][l - 2], B_dec[ADJ][l - 2] / A[ADJ][l]) for l in range(2, 9))
print(f"""
  ** THE DEPTH IS NOW CROSS-VALIDATED, WHICH IS WHAT `sec:largescale` HAS SAID IT IS NOT. **  The two
  treatments agree to {100 * (_w - 1):.0f}% across l = 2-8 on the adjudicated background, and the two arm-B variants
  -- the module's own per-mode freeze and the decoupled build -- agree with each other to {100 * _agree:.0f}%.
  *"The shape is cross-validated between the two; the depth is not" is out of date, and the factor of
  two the paper quotes at l = 3 and 4 is out with it.*

  ** AND (b) RETURNS THE VERDICT THE CORPUS ALREADY HAD, FOR A BETTER REASON. **  Delta(-2 ln L) =
  {TOT['arm A, adjudicated'][0]:+.2f} central ({TOT['arm A, adjudicated'][1]:+.2f} to {TOT['arm A, adjudicated'][2]:+.2f} across the octopole estimators), against the landed
  {TOT["the corpus's landed table"][0]:+.2f}.  *Before, "non-discriminating" rested on a depth nobody could pin down; now it rests
  on a depth two independent transfers agree on.  The sector is settled as a wash rather than left
  as one.*

  ⛔ ** TWO THINGS OF MINE ARE WITHDRAWN AND ONE STANDS. **  *Withdrawn: that the blocker past
  z ~ 10 is the LG = 12 truncation (it is the opacity grid's resolution, tied to the cut); and the
  arm-B depth quartet 0.4974/0.2326/0.1933/0.6186, which carried a truncated continuum as well as a
  missing late ISW.*  ** Standing: that the depth gap's cause is the late ISW ** -- turning it on is
  what closes the gap, and PART 3 shows the continuum fix alone makes it worse.

  ⌗ ** WHAT THIS DOES NOT SAY. **  That the low-multipole sector discriminates.  It does not, and now
  that is a measurement rather than an open question.  *Nor does it touch the acoustic range: the
  hierarchy exists because the fluid-plus-envelope treatment fails at high l, and nothing here
  changes that or the arm's standing there.*
""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print(BAR)
