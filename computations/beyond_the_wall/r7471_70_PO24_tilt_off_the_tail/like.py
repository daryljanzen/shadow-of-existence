"""r7471+70 -- the off-tail n_s likelihood: Planck 2018 plik_lite TT/TE/EE (bins with l_max^bin <= LMAX),
Planck 2018 conservative lensing bandpowers (no linear CMB-dependence correction), a tau prior
0.054 +/- 0.007 standing in for low-l EE, and A_planck with its 1 +/- 0.0025 prior.  Flat LCDM via CAMB."""
import os
import numpy as np
import scipy.linalg
from scipy.io import FortranFile
import camb

HERE = os.path.dirname(os.path.abspath(__file__))
PL = os.path.join(HERE, '..', '..', 'planck_tt_likelihood', 'data', 'planck2018_plik_lite')
NTT, NTE, NEE = 215, 199, 199
N = NTT + NTE + NEE

bval, X, _ = np.genfromtxt(os.path.join(PL, 'cl_cmb_plik_v22.dat'), unpack=True)
blmin = np.loadtxt(os.path.join(PL, 'blmin.dat')).astype(int)
blmax = np.loadtxt(os.path.join(PL, 'blmax.dat')).astype(int)
bw = np.loadtxt(os.path.join(PL, 'bweight.dat'))
_f = FortranFile(os.path.join(PL, 'c_matrix_plik_v22.dat'), 'r')
COV = _f.read_reals(dtype=float).reshape((N, N))
COV = np.tril(COV) + np.tril(COV, -1).T          # the reference code mirrors the lower triangle
LMIN, LMAXD = 30, 2508
NL = LMAXD - LMIN + 1
BIN = np.zeros((NTT, NL))
for i in range(NTT):
    BIN[i, blmin[i]:blmax[i] + 1] = bw[blmin[i]:blmax[i] + 1]
BIN_HI = blmax[:NTT] + LMIN                      # each TT bin's top multipole (TE/EE share the first 199)

LD = os.path.join(HERE, 'lensing')
_lb = np.loadtxt(os.path.join(LD, 'x_bandpowers.dat'))
LENS_DATA = _lb[:, 4]
LENS_COVINV = np.linalg.inv(np.loadtxt(os.path.join(LD, 'x_cov.dat')))
LENS_W = []
for i in range(1, 10):
    w = np.loadtxt(os.path.join(LD, 'win', f'window{i}.dat'))
    LENS_W.append((w[:, 0].astype(int), w[:, 1]))


class Like:
    def __init__(self, lmax=800, spectra='TTTEEE', lensing=True, tau_prior=True):
        tt = BIN_HI <= lmax
        pol = BIN_HI[:NTE] <= lmax
        sel = np.zeros(N, bool)
        if 'TT' in spectra:
            sel[:NTT] = tt
        if 'TE' in spectra:
            sel[NTT:NTT + NTE] = pol
        if 'EE' in spectra:
            sel[NTT + NTE:] = pol
        self.sel = sel
        self.icov = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV[np.ix_(sel, sel)]), np.identity(sel.sum()))
        self.lensing, self.tau_prior, self.lmax = lensing, tau_prior, lmax
        self.lmax_camb = min(2650, max(lmax, 400) + 600)
        self.nbins = int(sel.sum())

    def spectra(self, p):
        ombh2, omch2, H0, lnAs, ns, tau, cal = p
        pars = camb.CAMBparams()
        pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, omk=0, tau=tau)
        pars.InitPower.set_params(As=np.exp(lnAs) * 1e-10, ns=ns)
        pars.set_for_lmax(self.lmax_camb, lens_potential_accuracy=1)
        pars.WantTensors = False
        res = camb.get_results(pars)
        cl = res.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=True, lmax=self.lmax_camb)
        return cl['total'], cl['lens_potential'], res

    def chi2(self, p):
        try:
            tot, pp, _ = self.spectra(p)
        except Exception:
            return 1e30
        cal = p[6]
        l = np.arange(LMIN, LMIN + NL)
        lm = min(LMAXD, tot.shape[0] - 1)
        def binned(col):
            c = np.zeros(NL)
            c[:lm - LMIN + 1] = tot[LMIN:lm + 1, col]
            return BIN @ c
        model = np.concatenate([binned(0), binned(3)[:NTE], binned(1)[:NEE]]) / cal ** 2
        d = (X - model)[self.sel]
        c2 = float(d @ self.icov @ d)
        if self.lensing:
            L = np.arange(pp.shape[0])
            PPm = pp[:, 0] * (L * (L + 1)) ** 2 / (2 * np.pi)   # raw C_L^phiphi -> [L(L+1)]^2 C/2pi
            bp = np.array([np.sum(w * PPm[Ls]) for Ls, w in LENS_W])
            r = LENS_DATA - bp
            c2 += float(r @ LENS_COVINV @ r)
        if self.tau_prior:
            c2 += ((p[5] - 0.054) / 0.007) ** 2
        c2 += ((cal - 1.0) / 0.0025) ** 2
        return c2
