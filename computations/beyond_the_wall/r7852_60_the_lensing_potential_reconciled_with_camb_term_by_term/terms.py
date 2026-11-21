#!/usr/bin/env python3
"""** THE DECOMPOSITION: WHICH TERM CARRIES THE -14 TO +28 PER CENT. **

Order `r7849` ①.  `C_L^phiphi` is the composition of three maps, and this file crosses them so that
each difference isolates ONE:

    T1  the SOURCE      the 3D power of the potential that lenses, Delta^2(k, z)
    T2  the PROJECTION  the Limber integral, its kernel, chi(z), the `k` clip, the `L` grid
    T3  the BANDPOWERS  the [L(L+1)]^2 / (2 pi) convention and the nine windows

    A = instrument source -> instrument projection -> instrument bins      (the status quo)
    B = CAMB source       -> instrument projection -> instrument bins
    C = CAMB source       -> CAMB's exact projection -> instrument bins
    D = CAMB source       -> CAMB's exact projection -> exact binning

  A<->B isolates T1,  B<->C isolates T2,  C<->D isolates T3,  and A<->D is the published figure.

⚠ ** CAMB's `Weyl` TRANSFER IS `k^2 (Phi+Psi)/2`, NOT `(Phi+Psi)/2`, AND THIS FILE PROVES IT RATHER
THAN ASSERTING IT. **  `seed_weyl_normalisation()` runs the plain Limber integral on CAMB's own Weyl
power both ways and reports which one reproduces CAMB's own `C_L^phiphi`.  The wrong choice is out by
four orders of magnitude at the lowest bandpower, so the seed cannot pass by accident.

⚠ ** EVERYTHING IS LINEAR ON BOTH SIDES. **  CAMB's lensing potential includes a non-linear
correction by default and this instrument has none, so CAMB is forced to `NonLinear_none`.  A
non-linear reference against a linear instrument would put a real difference in the wrong term.

Run: python3 terms.py            (writes terms.json; caches the instrument solve beside it)
"""
import io
import json
import os
import sys
import time

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
sys.path.insert(0, R7846)
sys.path.insert(0, _HERE)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import lensing_like as LL                                                    # noqa: E402
import phiphi as PP                                                          # noqa: E402
import growth_kdep as GK                                                     # noqa: E402

import camb                                                                  # noqa: E402
from camb import model as camb_model                                         # noqa: E402

A = GK.A

# the control's own cosmology, as r7850's camb_reference.py states it
H0, OM, WB, NS, TAU = 67.40, 0.3150, 0.0224, 0.965, 0.054
AS = float(os.environ.get('AS', '2.1e-9'))       # ⚠ a PARAMETER, not a measurement
MNU = float(os.environ.get('MNU', '0.06'))
LMAX = 600
ZMAX_PK = 40.0

ETAREF = float(os.environ.get('ETAREF', '4000'))
NKP = int(os.environ.get('NKP', '220'))
KMIN = float(os.environ.get('KMIN', '2e-4'))
KMAX = float(os.environ.get('KMAX', '1.0'))

_T = {}


def _clock(tag, t0, **cfg):
    """every timing recorded WITH its configuration -- Ⓘ⑨, and r7848's defect"""
    _T[tag] = dict(seconds=round(time.time() - t0, 2), **cfg)
    return _T[tag]


# ─────────────────────────────────────────────────────────────────────────────────────────────────
#  CAMB, forced linear
def camb_results():
    h = H0 / 100.0
    omch2 = (OM - WB / h ** 2) * h ** 2 - MNU / 93.14
    p = camb.set_params(H0=H0, ombh2=WB, omch2=omch2, mnu=MNU, tau=TAU, ns=NS, As=AS,
                        lmax=LMAX, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    p.set_matter_power(redshifts=list(np.linspace(0.0, ZMAX_PK, 81))[::-1], kmax=60.0)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    cfg = dict(H0=H0, ombh2=WB, omch2=omch2, mnu=MNU, tau=TAU, ns=NS, As=AS, lmax=LMAX,
               camb_version=camb.__version__, nonlinear='NonLinear_none', zmax_pk=ZMAX_PK)
    return r, cfg


def camb_exact_cl(r):
    """CAMB's own `C_L^phiphi`, already in `[L(L+1)]^2 C_L / (2 pi)`"""
    return r.get_lens_potential_cls(lmax=LMAX)[:, 0]


def camb_weyl_power(r):
    """`P_Weyl(z, k)` -- the power of `(Phi+Psi)/2`, with CAMB's `k^2` divided out"""
    pk = r.get_matter_power_interpolator(var1='Weyl', var2='Weyl', hubble_units=False,
                                         k_hunit=False, nonlinear=False, extrap_kmax=400.0)

    def P(z, k):
        return float(pk.P(min(max(z, 0.0), ZMAX_PK), k)) / k ** 4
    return P


# ─────────────────────────────────────────────────────────────────────────────────────────────────
#  THE PROJECTION -- structurally the instrument's own, with its defects as switches
def project(ls, D2_of, chis, eta_of_chi, a_of_eta, etaref, clip=None, clamp=True, limit=200):
    """`phiphi.clpp`'s integrand exactly, with the source and the two defects as arguments

    `clip` is the `(kmin, kmax)` the source is clipped to, as `D2_of` does inside `clpp`; `None`
    leaves `k` alone.  `clamp` freezes `eta` at `etaref` for `chi` beyond the carry start, as
    `clpp` does; `False` lets it run.
    """
    out = np.empty(len(ls), float)
    for i, l in enumerate(ls):
        def integ(chi, l=l):
            if chi <= 1.0 or chi >= chis:
                return 0.0
            eta = eta_of_chi(chi)
            if clamp and eta <= etaref:
                eta = etaref
            a = a_of_eta(eta)
            k = (l + 0.5) / chi
            if clip is not None:
                k = float(np.clip(k, clip[0], clip[1]))
            W = -2.0 * (chis - chi) / (chis * chi)
            P = 2 * np.pi ** 2 * D2_of(k, a) / k ** 3
            return W ** 2 / chi ** 2 * P
        out[i] = quad(integ, 1.0, chis, limit=limit)[0]
    return out


def to_convention(ls, cl, wins):
    """`phiphi.bin_through` -- the instrument's `L`-grid spline, then the convention, then the bins"""
    return PP.bin_through(ls, cl, wins)


def bin_exact(cl_int, wins):
    """the SAME windows on a spectrum already known at every integer `L` and already in convention"""
    return np.array([float(np.sum(w * cl_int[L])) for L, w in wins])


# ─────────────────────────────────────────────────────────────────────────────────────────────────
def seed_weyl_normalisation(r, Pw, chis_camb, zc, ls_seed=(28, 100, 377)):
    """⚠ WHICH POWER IS CAMB's `Weyl`?  measured, not assumed"""
    cl = camb_exact_cl(r)
    rows = []
    for L in ls_seed:
        def f(chi, L=L):
            if chi <= 1.0 or chi >= chis_camb:
                return 0.0
            k = (L + 0.5) / chi
            W = -2.0 * (chis_camb - chi) / (chis_camb * chi)
            return W ** 2 / chi ** 2 * Pw(zc(chi), k)
        v = quad(f, 1.0, chis_camb, limit=300)[0] * (L * (L + 1.0)) ** 2 / (2.0 * np.pi)
        rows.append(dict(L=int(L), camb=float(cl[L]), limber=float(v),
                         ratio=float(v / cl[L])))
    return rows


def main():
    t_all = time.time()
    wins = LL.WINDOWS
    Lgrid = np.unique(np.concatenate([L for L, _ in wins]))
    # the instrument's own 36-node log grid, as phiphi.main builds it
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lgrid.min())),
                                        np.log10(Lgrid.max()), 36)).astype(int))
    print('\n  the windows span L = %d to %d over %d multipoles; the instrument splines %d nodes'
          % (Lgrid.min(), Lgrid.max(), len(Lgrid), len(ls)), flush=True)

    # ── CAMB, linear
    t0 = time.time()
    r, cfg = camb_results()
    _clock('camb_background_and_power', t0, **{k: cfg[k] for k in ('lmax', 'zmax_pk', 'nonlinear')})
    cl_camb = camb_exact_cl(r)
    Pw = camb_weyl_power(r)
    chis_camb = float(r.comoving_radial_distance(1100.0))
    _zgrid = np.linspace(0.0, 1200.0, 4001)
    _chigrid = r.comoving_radial_distance(_zgrid)
    _z_of_chi = CubicSpline(_chigrid, _zgrid)

    def zc(chi):
        return float(_z_of_chi(min(max(chi, _chigrid[0]), _chigrid[-1])))

    print('  CAMB %s, linear; chi(z=1100) = %.2f Mpc' % (camb.__version__, chis_camb), flush=True)

    # ── the seed: which Weyl normalisation
    t0 = time.time()
    seed = seed_weyl_normalisation(r, Pw, chis_camb, zc)
    seed_bad = seed_weyl_normalisation(r, lambda z, k: Pw(z, k) * k ** 4, chis_camb, zc)
    _clock('seed_weyl_normalisation', t0, multipoles=3)
    print('\n  ⚠ SEED -- CAMB\'s `Weyl` is k^2 (Phi+Psi)/2, so the POWER needs k^-4:')
    for a_, b_ in zip(seed, seed_bad):
        print('      L = %4d   with k^-4: ratio to CAMB %8.4f      without: %10.3e'
              % (a_['L'], a_['ratio'], b_['ratio']))
    ok_seed = all(abs(x['ratio'] - 1.0) < 0.10 for x in seed) and \
        all(abs(x['ratio'] - 1.0) > 10.0 for x in seed_bad)
    print('    ⇒ the seed %s: the k^-4 form reproduces CAMB and the other is out by orders'
          % ('HOLDS' if ok_seed else 'DOES NOT HOLD'), flush=True)

    # ── the instrument's background, and its source
    chis_inst = float(A.D_M)

    def eta_of_chi_inst(chi):
        return A.eta_0 - chi

    def a_of_eta_inst(eta):
        return float(A.a_of_eta(min(max(eta, float(A.eg[0])), A.eta_0)))

    print('\n  the instrument: chi* = %.2f Mpc, eta_0 = %.2f, carry starts at eta = %.0f (z = %.2f)'
          % (chis_inst, float(A.eta_0), ETAREF, 1.0 / float(A.a_of_eta(ETAREF)) - 1.0), flush=True)

    cache = os.path.join(_HERE, 'instrument_phi_eta%g_nkp%d.npz' % (ETAREF, NKP))
    if os.path.exists(cache):
        z_ = np.load(cache)
        kk, Phi = z_['kk'], z_['Phi']
        print('  the instrument\'s Phi(k) read from its cache (%d modes)' % len(kk), flush=True)
    else:
        print('  solving the instrument for Phi(k) at eta = %.0f on %d modes -- the one long step'
              % (ETAREF, NKP), flush=True)
        t0 = time.time()
        kk, Phi = PP.phi_shape(ETAREF)
        _clock('instrument_phi_solve', t0, etaref=ETAREF, nkp=NKP, kmin=KMIN, kmax=KMAX,
               nk=os.environ.get('NK'), noproj=os.environ.get('NOPROJ'), rtol=float(A.RTOL))
        np.savez_compressed(cache, kk=kk, Phi=Phi)
        print('    %.1f s, cached' % _T['instrument_phi_solve']['seconds'], flush=True)

    a_ref = float(A.a_of_eta(ETAREF))
    D2ref = (kk ** (NS - 1)) * Phi ** 2
    lnP = CubicSpline(np.log(kk), np.log(np.maximum(D2ref, 1e-300)))
    t0 = time.time()
    g = GK.GrowthKDep(0.0, kk=np.logspace(np.log10(KMIN), np.log10(KMAX), 48), a_start=a_ref)
    rat = g.ratio_fn(a_ref)
    _clock('instrument_growth_surface', t0, nk_growth=48, a_ref=a_ref, sum_ev=0.0)

    def D2_inst(k, a):
        return float(np.exp(lnP(np.log(k)))) * rat(k, a) ** 2

    def D2_camb(k, a):
        """CAMB's Weyl power put on the instrument's own (k, a) footing"""
        z = 1.0 / a - 1.0
        return k ** 3 * Pw(z, k) / (2 * np.pi ** 2)

    # ── A : the status quo, through this file's own projection (the positive control)
    t0 = time.time()
    clA = project(ls, D2_inst, chis_inst, eta_of_chi_inst, a_of_eta_inst, ETAREF,
                  clip=(kk[0], kk[-1]), clamp=True)
    _clock('A_instrument_source_instrument_projection', t0, multipoles=len(ls), etaref=ETAREF,
           clip=[float(kk[0]), float(kk[-1])], clamp=True)
    A_bp = to_convention(ls, clA, wins)

    # the positive control: the banked spectrum from phiphi.py's own run, same configuration
    banked = os.path.join(R7846, 'phiphi_z13.json')
    ctrl = None
    if os.path.exists(banked):
        d = json.load(io.open(banked, encoding='utf-8'))
        if list(d['ls']) == [int(v) for v in ls]:
            b0 = np.array(d['cl_shape'], float)
            rel = np.abs(clA / b0 - 1.0)
            ctrl = dict(banked='r7846/phiphi_z13.json', max_relative=float(rel.max()),
                        median_relative=float(np.median(rel)))
            print('\n  ⓪ POSITIVE CONTROL -- this file\'s projection against phiphi.py\'s own run at '
                  'the same configuration: max %.3e relative' % rel.max(), flush=True)

    # ── B : CAMB's source through the instrument's projection, defects and all
    t0 = time.time()
    clB = project(ls, D2_camb, chis_inst, eta_of_chi_inst, a_of_eta_inst, ETAREF,
                  clip=(kk[0], kk[-1]), clamp=True)
    _clock('B_camb_source_instrument_projection', t0, multipoles=len(ls), etaref=ETAREF,
           clip=[float(kk[0]), float(kk[-1])], clamp=True)
    B_bp = to_convention(ls, clB, wins)

    # ── C : CAMB's exact projection, through the instrument's L-grid spline and bins
    C_bp = to_convention(ls, cl_camb[ls] * (2.0 * np.pi) / (ls * (ls + 1.0)) ** 2, wins)
    # ── D : CAMB's exact projection at every integer L, exactly binned
    D_bp = bin_exact(cl_camb, wins)

    # ── the clip and the clamp, each priced on CAMB's source so the source cannot confound it
    t0 = time.time()
    clB_noclip = project(ls, D2_camb, chis_inst, eta_of_chi_inst, a_of_eta_inst, ETAREF,
                         clip=None, clamp=True)
    _clock('B_no_clip', t0, multipoles=len(ls), clip=None, clamp=True)
    B_noclip_bp = to_convention(ls, clB_noclip, wins)
    t0 = time.time()
    clB_noclamp = project(ls, D2_camb, chis_inst, eta_of_chi_inst, a_of_eta_inst, ETAREF,
                          clip=None, clamp=False)
    _clock('B_no_clip_no_clamp', t0, multipoles=len(ls), clip=None, clamp=False)
    B_clean_bp = to_convention(ls, clB_noclamp, wins)

    # ── the shares, each self-normalised so only SHAPE is compared
    def selfnorm(b):
        a_ = float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b))
        return a_ * b, a_

    An, aA = selfnorm(A_bp)
    Bn, aB = selfnorm(B_bp)
    Cn, aC = selfnorm(C_bp)
    Dn, aD = selfnorm(D_bp)
    Bnc, _ = selfnorm(B_noclip_bp)
    Bcl, _ = selfnorm(B_clean_bp)

    T1 = np.log(An / Bn)
    T2 = np.log(Bn / Cn)
    T3 = np.log(Cn / Dn)
    TOT = np.log(An / Dn)
    closure = float(np.max(np.abs(T1 + T2 + T3 - TOT)))

    print('\n  THE DECOMPOSITION -- each spectrum self-normalised, so only shape is compared')
    print('    bin  L_av       A/D-1      T1 source   T2 projection  T3 bandpowers')
    for i in range(LL.NBP):
        print('     %d   %6.1f   %+9.4f   %+9.4f   %+9.4f   %+9.4f'
              % (i + 1, LL.L_AV[i], np.expm1(TOT[i]), T1[i], T2[i], T3[i]))
    shares = dict(T1=float(np.abs(T1).sum()), T2=float(np.abs(T2).sum()),
                  T3=float(np.abs(T3).sum()))
    tot_share = sum(shares.values())
    print('\n    |log| summed over the nine bins:  T1 %.4f   T2 %.4f   T3 %.4f'
          % (shares['T1'], shares['T2'], shares['T3']))
    for k_ in ('T1', 'T2', 'T3'):
        print('      %s carries %6.2f per cent of the total movement' % (k_, 100 * shares[k_] / tot_share))
    print('    closure |T1+T2+T3 - total| = %.3e' % closure)

    print('\n  THE PROJECTION\'S OWN DEFECTS, priced on CAMB\'s source so the source cannot confound')
    print('    bin  L_av     clip costs    clip+clamp cost   Limber itself (clean vs CAMB)')
    limber_err = np.log(Bcl / Dn)
    clip_cost = np.log(Bn / Bnc)
    both_cost = np.log(Bn / Bcl)
    for i in range(LL.NBP):
        print('     %d   %6.1f   %+9.4f   %+9.4f   %+9.4f'
              % (i + 1, LL.L_AV[i], clip_cost[i], both_cost[i], limber_err[i]))

    def sc(b, amplitude=None):
        a_ = (float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b)) if amplitude is None
              else float(amplitude))
        rr = LL.DATA - a_ * b
        return float(rr @ LL.FISHER @ rr), a_

    print('\n  chi^2 against the nine bandpowers, one amplitude fitted:')
    rows = []
    for tag, b in (('A instrument source + instrument projection', A_bp),
                   ('B CAMB source + instrument projection', B_bp),
                   ('B CAMB source, no k clip', B_noclip_bp),
                   ('B CAMB source, no clip and no clamp', B_clean_bp),
                   ('C CAMB exact, instrument L-grid and bins', C_bp),
                   ('D CAMB exact, exactly binned', D_bp)):
        c2, a_ = sc(b)
        rows.append(dict(which=tag, chi2=c2, per_dof=c2 / 8.0, amplitude=a_))
        print('    %-44s chi^2 %10.4f  (%.4f per dof)' % (tag, c2, c2 / 8.0))

    out = dict(
        config=cfg, etaref=ETAREF, nkp=NKP, kmin=KMIN, kmax=KMAX,
        ls=[int(v) for v in ls],
        seed_weyl_k_minus_4=seed, seed_weyl_raw=seed_bad, seed_holds=bool(ok_seed),
        positive_control=ctrl,
        chis_instrument=chis_inst, chis_camb=chis_camb,
        bandpowers=dict(A=[float(v) for v in A_bp], B=[float(v) for v in B_bp],
                        B_no_clip=[float(v) for v in B_noclip_bp],
                        B_clean=[float(v) for v in B_clean_bp],
                        C=[float(v) for v in C_bp], D=[float(v) for v in D_bp]),
        amplitudes=dict(A=aA, B=aB, C=aC, D=aD),
        terms=dict(T1_source=[float(v) for v in T1], T2_projection=[float(v) for v in T2],
                   T3_bandpowers=[float(v) for v in T3], total=[float(v) for v in TOT]),
        total_relative=[float(v) for v in np.expm1(TOT)],
        shares_abs_log=shares, shares_per_cent={k_: 100 * shares[k_] / tot_share for k_ in shares},
        closure_max_abs=closure,
        projection_defects=dict(clip_cost_log=[float(v) for v in clip_cost],
                                clip_and_clamp_cost_log=[float(v) for v in both_cost],
                                limber_error_log=[float(v) for v in limber_err]),
        chi2=rows, timings=_T, total_seconds=round(time.time() - t_all, 2))
    with io.open(os.path.join(_HERE, 'terms.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote terms.json  (%.1f s in all)\n' % out['total_seconds'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
