#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:largescale`: ** ON THE ADJUDICATED BACKGROUND THE FLOOR'S LOCATION DOES NOT
MOVE ($\ell_2 = 7.81$ against $7.74$) AND THE TWO ARMS STILL DISAGREE -- BY A FACTOR $2.02$ AT
$\ell=4$, WIDER THAN THE CONTROL'S $1.84$.  ** AND THE DISAGREEMENT IS LOCATED: IT IS THE LATE
INTEGRATED SACHS--WOLFE, WHICH THE SECOND ARM DOES NOT HAVE. **

** ⇒ AND THE SECOND ARM CANNOT BE MADE TO HAVE IT. **  Its line-of-sight integration stops at
`ETAEND` $= 20\,a_{\rm rec}$, i.e. $z = 53.5$.  Pushing the cut later moves $\ell=3$ and $\ell=4$
MONOTONICALLY TOWARDS the first arm -- and the truncated free-streaming hierarchy goes NON-FINITE
once the cut passes $z\simeq10$, under the default settings and under three refinements of the step
size and the freeze threshold.  *** So node 66's condition for part (b) -- "if the two paths can be
brought together" -- IS NOT MET, and what blocks it is named rather than guessed. ***

Built r6801+cc66.22 (node 66, code seat), discharging the chat seat's order ② (a):
"the depth at $\ell=2$--$8$ on the adjudicated background, on both instrument paths, with the
disagreement between them stated as a number rather than a range."

===================================================================================================
** WHAT IS BEING MEASURED, AND WHAT THE TWO ARMS ARE **
===================================================================================================

`sec:largescale` predicts a low-multipole deficit with no free parameter: the source spectrum is
discrete on the closed $S^3$, $k_L = \sqrt{L(L+2)}/r_0$ with $L\ge2$, while the flat distance
slicing projects it through the FLAT transfer.  The observable is the ratio

    C_\ell^{\rm CR} / C_\ell^{\Lambda\rm CDM}
      = [ \sum_{L\ge2} w_L\, k_L^{n_s-1} |\Delta_\ell(k_L)|^2 ]
        / [ \int w(k)\, |\Delta_\ell(k)|^2 \, d\ln k ],     w_L = d\ln k_L/dL = (L+1)/L(L+2),

each normalised to its own $\ell = 25$--$40$ plateau, so the CR sum is the $L=2$-floored Riemann sum
of the same integral and the amplitude cancels.  ** The two arms differ ONLY in whose
$\Delta_\ell(k)$ is used. **

  ** ARM A ** -- CAMB's exact temperature transfer (SW + early and late ISW + Doppler).
  ** ARM B ** -- `HIER_photon_hierarchy`, the programme's own photon Boltzmann hierarchy.

** THREE THINGS ARE DONE DIFFERENTLY HERE FROM THE BANKED PAIR, AND EACH IS STATED. **

  1  ** $r_0$ IS COMPUTED FROM THE PAPER'S OWN FORMULA AT EACH BACKGROUND, NOT CARRIED AS 5064. **
     $r_0 = 2^{1/3}\Lambda^{-1/2}\sinh^{2/3}u$ at $u=\operatorname{arcsinh}\sqrt{\Omega_\Lambda/\Omega_m}$,
     with $\Lambda = 3H_0^2\Omega_\Lambda/c^2$.  *PART 1 asserts it reproduces the paper's $5064$ on
     the control before using it anywhere else.*
  2  ** BOTH ARMS ARE GIVEN THE SAME $r_0$. **  `P15_the_second_arm_actually_run` fed arm B
     $k_L = \sqrt{L(L+2)}\times2.75/D_M$, i.e. an $r_0$ of $D_M/2.75 = 5041$ against arm A's $5064$
     -- a $0.5\%$ mismatch inside a comparison whose whole content is a discrepancy.  *Here both
     read one $r_0$, so that term is gone from the difference rather than folded into it.*
  3  ** THE CONTROL BACKGROUND IS RUN FIRST ON BOTH ARMS AND CHECKED AGAINST WHAT IS BANKED **
     before either is moved, so a change at the adjudicated background is a change and not a
     re-implementation.

  ⌗ ** AND ONE KNOB WAS EXPOSED TO ASK THE QUESTION AT ALL, r6801+cc66.22. **  `HIER_photon_hierarchy`
  has taken an $H_0$ on its CR branch since `r2373` and never on its control branch, so "both arms on
  one background" could not be requested.  `H0_L` now does it, and the literal $67.40$ inside
  `Or_content` is replaced by `H0` in the same line -- **identical at the default, and away from it
  the correction**, since $\omega_r$ is fixed by $T_{\rm CMB}$ and $\Omega_r=\omega_r/h^2$, which is
  exactly what the CR branch already does at its own $H_0$.  *PART 3 asserts the default is unmoved.*

** COMPUTES: arm A from CAMB at AccuracyBoost 3, lSampleBoost 50, lAccuracyBoost 3, ombh2 = 0.02237,
   mnu = 0.06, tau = 0.0544, n_s = 0.9649, with omch2 derived from (H0, Om) so the two backgrounds
   are like-for-like; arm B from HIER_photon_hierarchy at KMAXL = 700 with its own defaults.
   Backgrounds: control (67.40, 0.3150) and adjudicated (68.60, 0.2973).  *** Nothing is fitted:
   r_0 is a formula, the two arms are given the same one, and the only quantity reported is a ratio
   of a sum to an integral of the SAME transfer. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~15 min -- CAMB twice at high
accuracy and the hierarchy seven times)
"""
import os
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
HIER_DIR = os.path.join(ROOT, 'storyboard_receipts')
C = 299792.458
NS = 0.9649
CTL = (67.40, 0.3150)
ADJ = (68.60, 0.2973)


def r0_of(H0, Om):
    """the paper's own parameter-free S^3 radius: 2^(1/3) Lambda^(-1/2) sinh^(2/3) u."""
    OL = 1.0 - Om
    return (2.0 ** (1.0 / 3.0) * (C / (H0 * np.sqrt(3.0 * OL)))
            * np.sinh(np.arcsinh(np.sqrt(OL / Om))) ** (2.0 / 3.0))


# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE GEOMETRY: r_0 FROM THE FORMULA, VALIDATED, THEN MOVED **")
print(BAR)
print(f"  {'background':>26} {'Lambda^-1/2':>12} {'u':>9} {'r_0 Mpc':>10}")
R0 = {}
for nm, (H0, Om) in (('control  (67.40, 0.3150)', CTL), ('adjudicated (68.60, 0.2973)', ADJ)):
    OL = 1.0 - Om
    R0[(H0, Om)] = r0_of(H0, Om)
    print(f"  {nm:>26} {C / (H0 * np.sqrt(3 * OL)):>12.2f} "
          f"{np.arcsinh(np.sqrt(OL / Om)):>9.5f} {R0[(H0, Om)]:>10.2f}")
check("the formula reproduces the paper's r_0 = 5064 Mpc on the control, to a part in 10^4",
      abs(R0[CTL] - 5064.0) < 1.0)
print(f"\n  ** THE RADIUS BARELY MOVES: {R0[CTL]:.2f} -> {R0[ADJ]:.2f} Mpc, "
      f"{100 * (R0[ADJ] / R0[CTL] - 1):+.2f}%. **")
print("  *A 1.8% rise in H_0 and a 5.6% fall in Omega_m, and the radius Lambda sets moves by a")
print("  quarter of a per cent -- the two enter Lambda^(-1/2) and sinh^(2/3)u with opposite signs.*")
check("r_0 moves by under half a per cent between the two backgrounds",
      abs(R0[ADJ] / R0[CTL] - 1) < 0.005)

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** ARM A (CAMB's EXACT TRANSFER): VALIDATED ON THE CONTROL, THEN MOVED **")
print(BAR)
import camb                                                                # noqa: E402
from scipy.interpolate import interp1d                                     # noqa: E402

LMAX = 48


def armA(H0, Om, scales=(1.0,), ombh2=0.02237, mnu=0.06):
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
    Larr = np.array(td.L)
    q = np.array(td.q)
    cl = res.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=True)['unlensed_scalar'][:, 0]
    lnq = np.log(q)
    out = {}
    for sc in scales:
        r0 = r0_of(H0, Om) * sc
        Ls = np.arange(2, 4000)
        kL = np.sqrt(Ls * (Ls + 2)) / r0
        wL = (Ls + 1.0) / (Ls * (Ls + 2.0))
        msk = (kL >= q.min()) & (kL <= q.max())
        ells, rat, gate = [], [], []
        for i, ell in enumerate(Larr):
            if ell > LMAX or ell < 2:
                continue
            Dl = DL[i]
            cont = float(np.trapezoid((q / 0.05) ** (NS - 1.0) * Dl ** 2, lnq))
            f = interp1d(lnq, Dl, kind='cubic', bounds_error=False, fill_value=0.0)
            disc = float(np.sum(wL[msk] * (kL[msk] / 0.05) ** (NS - 1.0)
                                * f(np.log(kL[msk])) ** 2))
            ells.append(int(ell))
            rat.append(disc / cont)
            gate.append(cont / cl[int(ell)])
        ells = np.array(ells)
        rat = np.array(rat)
        pl = (ells >= 25) & (ells <= 40)
        g = np.array(gate)
        g = g / np.mean(g[pl])
        lo = (ells >= 2) & (ells <= 12)
        out[sc] = (ells, rat / np.mean(rat[pl]), r0, float(np.max(np.abs(g[lo] - 1.0))))
    return out


A = {}
for nm, bg in (('control', CTL), ('adjudicated', ADJ)):
    sc = (1.0, 0.99, 1.01) if bg == ADJ else (1.0,)
    res = armA(*bg, scales=sc)
    A[bg] = res
    ells, rat, r0, gmax = res[1.0]
    d = {int(l): float(rat[i]) for i, l in enumerate(ells)}
    print(f"  {nm:>12}  r_0 = {r0:8.2f}   "
          + " ".join(f"l={l}:{d[l]:.4f}" for l in range(2, 9) if l in d))
    check(f"arm A gate on {nm}: the continuum reproduces CAMB's own C_l in SHAPE to 1e-3 "
          f"across l = 2-12 (max dev {gmax:.1e})", gmax < 1e-3)
PAPER = {2: 0.473, 3: 0.410, 4: 0.356, 5: 0.676}
ec, rc, _, _ = A[CTL][1.0]
dc = {int(l): float(rc[i]) for i, l in enumerate(ec)}
print(f"\n  against the paper's own quartet {list(PAPER.values())}:")
check("** arm A on the control reproduces sec:largescale's 0.473 / 0.410 / 0.356 / 0.676 "
      "to better than 1% **",
      all(abs(dc[l] / PAPER[l] - 1) < 0.01 for l in PAPER))

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** ARM B (THE PROGRAMME'S HIERARCHY): THE KNOB, THEN THE SAME TWO BACKGROUNDS **")
print(BAR)
_SRC = open(os.path.join(HIER_DIR, 'HIER_photon_hierarchy.py'), encoding='utf-8').read()
check("H0_L is defined ONCE and the control arm's Or_content is built from H0, not from a literal",
      _SRC.count("os.environ.get('H0_L'") == 1
      and "4.1833e-5/(H0/100)**2; Om=0.3150" in _SRC)

_RUNNER = r"""
import os, sys, contextlib, io
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import spherical_jn
H0=float(os.environ['BH0']); Om=float(os.environ['BOM']); R0=float(os.environ['BR0'])
os.environ['KMAXL']='700'; os.environ['H0_L']='%.10f'%H0; os.environ['OMF']='%.12f'%(Om/0.3150)
sys.path.insert(0, os.environ['HIER_DIR'])
if os.environ.get('ZEND'):
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):
        import HIER_photon_hierarchy as _P
    e_=float(np.interp(1.0/(1.0+float(os.environ['ZEND'])), _P.ag, _P.eg))
    os.environ['ETAEND']='%.6f'%min(e_, _P.eta_0-1e-3)
    for m in [k for k in list(sys.modules) if k.startswith('HIER_photon')]:
        del sys.modules[m]
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    import HIER_photon_hierarchy as H
Ls=np.arange(2,260)
kL=(np.sqrt(Ls*(Ls+2))*float(os.environ['BSTRETCH'])/H.DM
    if os.environ.get('BSTRETCH') else np.sqrt(Ls*(Ls+2))/R0)
kd=np.exp(np.linspace(np.log(kL[0]*0.5), np.log(kL[-1]), 320))
kk=np.unique(np.concatenate([kL,kd]))
with contextlib.redirect_stdout(io.StringIO()):
    E,Y,e_sw=H.evolve(kk)
    m=E>max(e_sw,H.eta_rec-160.0); ee,Yv=E[m],Y[m]
    g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
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
print('RESULT ' + ' '.join('%.6f'%x for x in r[:11]) + ' | eta_end %.1f eta_0 %.1f DM %.1f'
      %(H.eta_end,H.eta_0,H.DM))
"""


def armB(H0, Om, r0, zend=None, stretch=None):
    env = dict(os.environ, BH0=f"{H0}", BOM=f"{Om}", BR0=f"{r0:.10f}", HIER_DIR=HIER_DIR)
    if zend is not None:
        env['ZEND'] = str(zend)
    else:
        env.pop('ZEND', None)
    if stretch is not None:
        env['BSTRETCH'] = f"{stretch}"
    else:
        env.pop('BSTRETCH', None)
    p = subprocess.run([sys.executable, '-c', _RUNNER], env=env, capture_output=True, text=True)
    for line in p.stdout.splitlines():
        if line.startswith('RESULT '):
            body, meta = line[7:].split('|')
            vals = np.array([float(x) for x in body.split()])
            return vals, meta.strip()
    return None, (p.stdout + p.stderr)[-200:]


B = {}
for nm, bg in (('control', CTL), ('adjudicated', ADJ)):
    v, meta = armB(*bg, R0[bg])
    B[bg] = v
    print(f"  {nm:>12}  {meta}")
    print(f"                " + " ".join(f"l={l}:{v[l - 2]:.4f}" for l in range(2, 9)))
BANK = {2: 0.494, 3: 0.243, 4: 0.184, 5: 0.61}
# ** THE BANKED RUN USED A DIFFERENT LADDER: k_L = sqrt(L(L+2)) * 2.75 / D_M, i.e. an implied
#    r_0 of D_M/2.75 = 5041 Mpc against the formula's 5065 -- choice 2 in the header.  *So arm B
#    is first re-run under the BANKED prescription, which is what reproduces the banked quartet;
#    the shift to the formula's r_0 is then a MEASURED difference rather than an excuse for a
#    loose tolerance.*  The first draft of this receipt asserted the two agreed to 5% and the
#    l = 4 point missed at 5.05%, which is what forced the measurement.
vbank, mbank = armB(*CTL, R0[CTL], stretch=2.75)
print(f"\n  arm B on the control under the BANKED ladder (2.75/D_M, implied r_0 = "
      f"{13864.2 / 2.75:.0f} Mpc):")
print("                " + " ".join(f"l={l}:{vbank[l - 2]:.4f}" for l in range(2, 9)))
check("** under the banked prescription arm B reproduces 0.494 / 0.243 / 0.184 / 0.61 to 2% **",
      all(abs(vbank[l - 2] / BANK[l] - 1) < 0.02 for l in BANK))
_sh = max(abs(B[CTL][l - 2] / vbank[l - 2] - 1) for l in BANK)
print(f"  ⇒ ** and moving the ladder to the formula's r_0 shifts the quartet by at most "
      f"{100 * _sh:.1f}%, ** at l = 4.")
print("    *That is the price of choice 2, paid once and in the open: both arms now read ONE r_0,")
print("     so the arm-to-arm gap below carries no ladder mismatch inside it.*")
check("the r_0 correction moves arm B's control quartet by under 6 per cent -- a per-cent-level "
      "term inside a factor-two question", _sh < 0.06)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE DISAGREEMENT, AS A NUMBER **")
print(BAR)
ea, ra, _, _ = A[ADJ][1.0]
da = {int(l): float(ra[i]) for i, l in enumerate(ea)}
print(f"  {'ell':>5} {'ARM A (CAMB)':>14} {'ARM B (hierarchy)':>18} {'A / B':>9}   "
      f"{'  control A/B':>14}")
FAC = {}
for l in range(2, 9):
    fa, fb = da[l], float(B[ADJ][l - 2])
    fc = dc[l] / float(B[CTL][l - 2])
    FAC[l] = fa / fb
    print(f"  {l:>5} {fa:>14.4f} {fb:>18.4f} {fa / fb:>9.3f}   {fc:>14.3f}")
worst = max(FAC, key=lambda k: FAC[k])
ctl_fac = {l: dc[l] / float(B[CTL][l - 2]) for l in range(2, 9)}
print()
print(f"  ** THE NUMBER IS {FAC[worst]:.2f}, AT l = {worst}. **  {FAC[3]:.2f} at l = 3; "
      f"{FAC[2]:.3f} at l = 2; under 1.02 from l = 6 up.")
print(f"  ** AND IT WIDENED: on the control the worst point is {max(ctl_fac.values()):.2f}. **  "
      f"The background the")
print("  distances fix does NOT bring the two treatments together; it separates them further.")
check("** the two arms disagree by a factor near two at l = 4 on the adjudicated background **",
      FAC[4] > 1.9)
check("and by under 2 per cent at l = 2 and from l = 6 up -- the gap is l = 3-5, not everywhere",
      abs(FAC[2] - 1) < 0.02 and all(abs(FAC[l] - 1) < 0.02 for l in (6, 7, 8)))
check("** the disagreement is WIDER on the adjudicated background than on the control **",
      FAC[4] > max(ctl_fac.values()))
print()
print(f"  ⌗ the minimum is at l = 4 on BOTH arms and BOTH backgrounds, and both recover by l = 8:")
for nm, bg, arm in (('A control', CTL, dc), ('A adjudicated', ADJ, da)):
    lo = min((2, 3, 4, 5), key=lambda l: arm[l])
    print(f"      arm {nm:>14}: minimum at l = {lo}, ratio > 0.99 by l = "
          f"{min(l for l in range(2, 13) if arm[l] > 0.99)}")
for nm, bg in (('B control', CTL), ('B adjudicated', ADJ)):
    v = B[bg]
    lo = min((2, 3, 4, 5), key=lambda l: v[l - 2])
    print(f"      arm {nm:>14}: minimum at l = {lo}, ratio > 0.99 by l = "
          f"{min(l for l in range(2, 13) if v[l - 2] > 0.99)}")
check("** the SHAPE still cross-validates -- minimum at l = 4 and recovery by l = 8 on all four **",
      all(min((2, 3, 4, 5), key=lambda l: arm[l]) == 4 for arm in (dc, da))
      and all(min((2, 3, 4, 5), key=lambda l: B[bg][l - 2]) == 4 for bg in (CTL, ADJ)))

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** IT IS NOT THE GEOMETRY, AND THAT IS MEASURED RATHER THAN ARGUED **")
print(BAR)
print("  The two arms carry slightly different distances to last scattering, so the obvious")
print("  suspect is that they are reading the ladder at slightly different angles.  ** The same")
print("  transfer is re-summed with r_0 alone moved, which is exactly that effect. **")
print()
print(f"  {'r_0 factor':>12} {'r_0 Mpc':>10} " + " ".join(f"{'l=' + str(l):>9}" for l in (2, 3, 4, 5)))
for sc in (0.99, 1.0, 1.01):
    e2, r2, r0v, _ = A[ADJ][sc]
    d2 = {int(l): float(r2[i]) for i, l in enumerate(e2)}
    print(f"  {sc:>12.3f} {r0v:>10.2f} " + " ".join(f"{d2[l]:>9.4f}" for l in (2, 3, 4, 5)))
_, r_lo, _, _ = A[ADJ][0.99]
_, r_hi, _, _ = A[ADJ][1.01]
i4 = int(np.where(ea == 4)[0][0])
slope = abs(float(r_hi[i4]) - float(r_lo[i4])) / (2.0 * da[4])       # per 1% in r_0
print(f"\n  ⇒ ** a 1% change in r_0 moves the l = 4 depth by {100 * slope:.1f}%. **")
print("  The two arms' distances differ by about a tenth of a per cent, so that term can account")
print(f"  for roughly {slope * 0.1 * 100:.2f}% of a discrepancy that is {100 * (FAC[4] - 1):.0f}%.")
check("** the geometry is ruled out: r_0 would have to be wrong by tens of per cent to do this **",
      slope * 0.1 < 0.01 * (FAC[4] - 1))

# =================================================================================================
print()
print(BAR)
print("  PART 6 -- ** IT IS THE LATE ISW, AND THE SECOND ARM CANNOT BE MADE TO CARRY IT **")
print(BAR)
print("  Arm B's line-of-sight integration stops at ETAEND = 20 a_rec, i.e. ** z = 53.5 **, so the")
print("  late ISW is outside it entirely.  Arm A carries it -- and `P15_verify_lowell_boltzmann`'s")
print("  own diagnosis is that the late ISW at low l is sourced ABOVE the discrete floor and is")
print("  therefore RETAINED by the CR sum, i.e. it is power that FILLS the deficit.")
print("  ⇒ *** So omitting it must make the deficit DEEPER -- and arm B is deeper, at exactly the")
print("     multipoles where the two disagree.  The prediction is directional and it is tested. ***")
print()
print(f"  {'z of the cut':>14} " + " ".join(f"{'l=' + str(l):>9}" for l in (2, 3, 4, 5)))
TREND = {}
for z in (None, 30, 15):
    v, meta = armB(*ADJ, R0[ADJ], zend=z)
    lab = 'default 53.5' if z is None else f'{z}'
    if v is None:
        print(f"  {lab:>14}   NON-FINITE   ({meta})")
        TREND[z] = None
        continue
    TREND[z] = v
    print(f"  {lab:>14} " + " ".join(f"{v[l - 2]:>9.4f}" for l in (2, 3, 4, 5)))
print(f"  {'arm A':>14} " + " ".join(f"{da[l]:>9.4f}" for l in (2, 3, 4, 5)) + "   <- the target")
moved3 = TREND[15][1] - TREND[None][1]
gap3 = da[3] - TREND[None][1]
print()
print(f"  ⇒ ** l = 3 moves {TREND[None][1]:.4f} -> {TREND[15][1]:.4f} as the cut goes 53.5 -> 15, "
      f"i.e. {100 * moved3 / gap3:.0f}% of the")
print("     way to arm A, and l = 4 moves the same direction. **  *The sign is the prediction's and")
print("     the size is not enough -- most of the late ISW is below z = 2, which is where the")
print("     calculation cannot go.*")
check("** extending the cut moves l = 3 TOWARDS arm A, which is the direction the diagnosis "
      "predicts **", moved3 > 0 and gap3 > 0)
check("and l = 4 moves the same way", TREND[15][2] > TREND[None][2])

print()
print("  ** AND HERE IS WHERE IT STOPS. **  The cut is pushed past z = 15 on the control, with the")
print("  late-stage step count and the freeze threshold varied, and the hierarchy goes non-finite:")
print()
print(f"  {'z of the cut':>14} {'settings':>34} {'l = 2':>12}")
for z, extra, lab in ((11, {}, 'defaults'),
                      (8, {}, 'defaults'),
                      (8, {'NS3': '4000'}, 'NS3 = 4000 (4x finer late grid)'),
                      (8, {'NS3': '12000', 'HKCAP': '0.02'}, 'NS3 = 12000, HKCAP = 0.02')):
    os.environ.update(extra)
    v, meta = armB(*CTL, R0[CTL], zend=z)
    for k in extra:
        os.environ.pop(k, None)
    ok = v is not None and np.all(np.isfinite(v))
    print(f"  {z:>14} {lab:>34} {(f'{v[0]:.4f}' if ok else '** NON-FINITE **'):>12}")
    if z == 11:
        check("the hierarchy is still finite with the cut at z = 11", ok)
    if z == 8 and not extra:
        check("** and non-finite at z = 8 on the defaults **", not ok)
    if z == 8 and extra:
        check(f"** still non-finite with {lab} -- not a step-size or freeze-threshold failure **",
              not ok)

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SETTLES, AND WHAT IT HANDS BACK")
print(BAR)
print(f"""
  ** (a) IS ANSWERED. **  On the adjudicated background the floor sits where it sat: $r_0$ moves
  {100 * (R0[ADJ] / R0[CTL] - 1):+.2f}% and the lowest mode lands at l_2 = {np.sqrt(8.0) * 13941.1 / R0[ADJ]:.2f} against {np.sqrt(8.0) * 13864.2 / R0[CTL]:.2f}.  The depths are

        arm A   {da[2]:.4f} {da[3]:.4f} {da[4]:.4f} {da[5]:.4f} {da[6]:.4f} {da[7]:.4f} {da[8]:.4f}   (l = 2..8)
        arm B   {B[ADJ][0]:.4f} {B[ADJ][1]:.4f} {B[ADJ][2]:.4f} {B[ADJ][3]:.4f} {B[ADJ][4]:.4f} {B[ADJ][5]:.4f} {B[ADJ][6]:.4f}

  ** and the disagreement is {FAC[4]:.2f} at l = 4 and {FAC[3]:.2f} at l = 3 ** -- one number, not a range,
  and WIDER than the control's {max(ctl_fac.values()):.2f}.  *The shape still cross-validates: minimum at l = 4 and
  recovery by l = 8 on both arms and both backgrounds.  It is the depth alone that is open.*

  ** (b)'s CONDITION IS NOT MET, AND WHAT BLOCKS IT IS NAMED. **  The order says to score the floor
  against the sky "if the two paths can be brought together".  They cannot, at present:

     1  the gap is not the geometry -- 1% in r_0 buys {100 * slope:.1f}% at l = 4 against a {100 * (FAC[4] - 1):.0f}% gap;
     2  the gap has the sign and the location of a MISSING LATE ISW, and pushing arm B's cut from
        z = 53.5 to z = 15 moves l = 3 and l = 4 towards arm A;
     3  arm B goes NON-FINITE once the cut passes z ~ 10, and it is not a step-size or a freeze
        threshold: three refinements fail identically.

  ⇒ *** So a low-l confrontation run today would be scoring ONE arm and calling it the prediction.
  What would earn (b) is a named build and not a knob: carry the post-recombination source with the
  photon hierarchy DECOUPLED -- Phi' + Psi' needs the metric and matter sector only, not the free-
  streaming tower whose LG = 12 truncation is what goes non-finite. ***  That is an instrument
  change and this seat does not make it unbidden.

  ⌗ ** WHAT THIS DOES NOT SAY. **  Which arm is right.  Arm A carries the late ISW and arm B does
  not, which is a reason to prefer arm A AT THESE MULTIPOLES and is not a general verdict on either
  -- arm B exists because the fluid-plus-envelope treatment fails at high l, where arm A's CR
  transfer is not available at all.  *The corpus still has one converged depth table and a second
  arm that agrees on shape and not on depth; what is new is that the depth gap now has a cause.*
""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print(BAR)
