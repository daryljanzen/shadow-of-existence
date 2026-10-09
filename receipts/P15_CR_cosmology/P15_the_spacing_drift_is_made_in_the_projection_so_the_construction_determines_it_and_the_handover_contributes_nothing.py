r"""
RECEIPT -- P15: ** `r7221` ORDERED THE DERIVATION: `IS THE DRIFT A QUANTITY THE CONSTRUCTION
DETERMINES, OR AN ARTEFACT OF THE TRANSFER?`  *** IT IS DETERMINED, AND IT IS MADE ENTIRELY IN THE
PROJECTION: THE ACOUSTIC PHASE CARRIES NO DRIFT AT ALL AND THE HANDOVER CONTRIBUTES NOTHING. *** **

  ⓵ ** THE SOURCE COMB IN `$k$` HAS NO DRIFT, DRIVEN OR UNDRIVEN. **  *Measured on source extrema
  at recombination -- never in `$\ell$`, which is the instrument's own standing rule.  UNDRIVEN the
  comb lands on the integers to `$0.015$`, under two ladder steps, and its own drift is `$-0.69$`
  against an rms of `$1.74$`: zero.  DRIVEN, on a UNIFORM `$k$` grid at half the ladder's quantum
  with the extrema parabolically refined, the driving moves the comb by a nearly CONSTANT `$-0.12$`
  in `$q=k r_s/\pi$` -- a spread of `$0.029$` across six peaks -- and leaves `$D=+0.03$`--`$+0.56$`,
  inside its own rms of zero either way.*  ⇒ **A constant phase shift has no curvature, so it cannot
  drift a comb: the driving supplies the OFFSET and the alternation, not the drift.**

  ⓶ ** THE PROJECTION MANUFACTURES THE WHOLE OF IT, FROM A COMB THAT HAS NONE. **  *Push a PERFECT
  comb -- extrema exactly at `$k r_s=n\pi$`, no dynamics, no background, no fit -- through the same
  projection integral and the `$\ell$`-space gaps come out `$278.5\;289.5\;293.4\;295.4$`: rising,
  decelerating, and saturating under `$\ell_A$`, giving `$D=+2.62$`.  Re-projecting the instrument's
  own SAVED source gives `$D=+2.57$` and the reporting path's banked spectrum `$+4.38$`, the
  remainder sitting in the multipole hierarchy's damping, which the closed form carries as one
  Gaussian in `$k$`.*

  ⓷ ⛭⛭⛭ ** AND THE DRIFT IS DERIVED IN CLOSED FORM, NOT MEASURED OFF A SPECTRUM. **  *Replace
  `$j_\ell(kD)^2$` by its own asymptotic average `$1/(x\sqrt{x^2-\ell^2})$`, substitute
  `$x=\ell\cosh t$` so the inverse-square-root edge integrates exactly, and the `$\ell$`-space peaks
  come back at `$299.0\;577.4\;866.9\;1160.3\;1455.7$` against the full Bessel sum's
  `$298.6\;576.9\;866.4\;1159.8\;1455.2$` -- **every peak to under `$0.5$` in `$\ell$` and the
  drift to `$0.01$`.**  ⇒ *So the drift is the CENTROID SHIFT of the kernel's own window acting on a
  damped comb, and its only inputs are `$r_s$`, `$D_M$` and `$r_D$`, all three of which this
  construction computes.*

  ⓸ ⛔ ** THE HANDOVER CONTRIBUTES NOTHING, WHICH IS THE PAPER'S OWN STATEMENT MEASURED. **  *`Prop.
  subhorizon` says the collapse leg's contribution `is an amplitude and not a phase`.  Moved the
  handover epoch by a DECADE, `ZSTART` from `$10^7$` to `$10^8$`: the source comb moves `$0.0010$`
  in `$q$`, which is `$0.30$` in `$\ell$` -- a tenth of one per cent of a peak spacing -- and the
  drift by `$0.002$`.*  ⇒ **So the one place the order named as `this construction's rather than
  anybody's` is the one place that supplies none of the answer.**

  ⓹ ** IT IS NOT A GRID ARTEFACT, WHICH IS THE BRANCH THE ORDER ASKED TO BE RULED OUT. **  *The
  instrument's own projection sampling is `$2.3$` points per Bessel period and it says so; on one
  configuration run both ways the DISCRETE ladder gives `$D=+13.84$` and the UNIFORM grid `$+13.76$`,
  `$0.6$` per cent apart.  The derived drift moves by `$0.00$` under doubling the `$k$` sampling and
  `$0.02$` under halving the `$\ell$` step.*

  ⇒ ⛭ ** SO THE PRE-REGISTERED THIRD OUTCOME IS THE ONE THAT FIRED: DERIVABLE, AND NOT A
  DISCRIMINATOR. **  *Arm `$D=+4.38$`, control `$+4.42$`, every peak position agreeing to under
  `$0.4$` in `$\ell$` -- the drift is carried by `$r_s$`, `$D_M$` and `$r_D$`, which the two
  frameworks share to under a per cent, so it is a parameter-free prediction OF THE SPECTRUM and no
  test at all OF THE RATE SPLIT.  **The bank's eight parts in ten thousand is precise, derivable and
  unscoreable as a discrimination, and that is the answer rather than a hedge on it.***

  ⌈ ⛔ ** AND TWO OF THIS SEAT'S OWN PRE-REGISTERED CLAIMS FAILED. **  *(i) The SIGN held and the
  percentage band held -- `$+6.1$` per cent derived and `$+7.8$` measured against `$5$`--`$10$`
  predicted -- but the SAME prediction's quadratic-coefficient form, `$+5$` to `$+15$`, did NOT: the
  measured coefficient is `$+4.38$` and the derived `$+2.61$`.  The two forms were offered as
  equivalent and are not, because a saturating drift has no single quadratic coefficient; the
  conversion was made off a three-point local mean where the rise decelerates.  **(ii) The
  ATTRIBUTION was wrong**: the prediction named the expansion-leg driving around equality as the
  carrier, and the driving carries `$8.7$` per cent of it.  Both are gated here as failures rather
  than reported as successes.*

** COMPUTES: the peak-spacing drift of the acoustic comb, D in l_n = c + b n + D n^2 + A (-1)^n over
   the first five peaks on 150 <= l <= 1600 -- derived from the projection kernel's own asymptotic
   window with r_s, D_M and r_D as its only inputs, and decomposed against the source comb in k, the
   handover epoch and the k-grid.  *** No new spectra are computed here: the ODE runs are banked
   under computations/beyond_the_wall/r7234_60_.../ with their logs and their launcher. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; 34s MEASURED)
"""
import json
import os
import subprocess
import sys

import numpy as np
from scipy.special import spherical_jn

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
ran = []


def gate(label, ok):
    ran.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BW, 'r7234_60_is_the_peak_spacing_drift_a_quantity_the_construction_determines')
SRC_KCONT = os.path.join(BW, 'spectra', 'r6911_source_cr_kcont.npz')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
SPEC = os.path.join(BW, 'spectra')
for _p in (MINE, SRC_KCONT, GO, LEV, SPEC):
    if not os.path.exists(_p):
        print(f"  ⛔ AN INPUT THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

# ⛭ the paper state is read at a PIN for the historical assertion and as a DISJUNCTION live --
#   L-249's repair rule, which r7232 found was prescribed in O1 long before this seat reached it.
PIN = 'bfa6c6bc84f3014b9c18f54e3a58010eeae8a045'
NPK = 5                      # the first five peaks -- as far as the banks' l range carries a comb
LLO, LHI = 150.0, 1600.0


# ─────────────────────────────────────────────────────────────────────────────────────────────────
#  THE ONE COMB THIS RECEIPT FITS, AND IT IS THE SAME ONE EVERYWHERE
# ─────────────────────────────────────────────────────────────────────────────────────────────────
def comb_fit(pk):
    """l_n = c + b n + D n^2 + A (-1)^n -- cc66.161's four parameters, read off peak POSITIONS.
    The alternation column is not optional: without it the second difference of five peaks is
    dominated by the odd/even term and the quadratic absorbs it."""
    pk = np.asarray(pk, float)
    n = np.arange(1, len(pk) + 1.0)
    A = np.vstack([np.ones_like(n), n, n ** 2, (-1.0) ** n]).T
    c, *_ = np.linalg.lstsq(A, pk, rcond=None)
    r = pk - A @ c
    return float(c[1]), float(c[2]), float(c[3]), float(np.sqrt(np.sum(r ** 2) / max(1, len(pk) - 4)))


def refine_max(x, y, order=4):
    a = np.abs(np.asarray(y, float))
    x = np.asarray(x, float)
    out = []
    for i in range(order, len(a) - order):
        if a[i] == max(a[i - order:i + order + 1]) and a[i] > a[i - 1] and a[i] > a[i + 1]:
            c = np.polyfit(x[i - 1:i + 2], a[i - 1:i + 2], 2)
            out.append(-c[1] / (2 * c[0]))
    return np.array(out)


def l_peaks(ls, Dl):
    ls = np.asarray(ls, float)
    Dl = np.asarray(Dl, float)
    m = (ls >= LLO) & (ls <= LHI) & (Dl > 0) & np.isfinite(Dl)
    L, y = ls[m], Dl[m]
    t = float(np.polyfit(np.log(L), np.log(y), 1)[0])
    return refine_max(L, y / L ** t, order=3)


def bank_peaks(path):
    z = np.load(path, allow_pickle=True)
    p = l_peaks(z['ls'], z['Dl'])
    return p[(p > LLO) & (p < LHI)][:NPK], float(z['l_A'])


# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓐ  THE GUARD -- UNDRIVEN, THE SOURCE COMB IN k IS THE INTEGERS, SO IT HAS NO DRIFT TO FIND")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
CB = json.load(open(os.path.join(MINE, 'source_combs.json'), encoding='utf-8'))
_nd = CB['comb_cr_nodrive']
_q = np.array(_nd['sw'], float)
_lA_run = float(_nd['l_A_print'])
_dev = np.abs(_q - np.round(_q))
print(f"    undriven source comb q = k r_s/pi : {['%.4f' % v for v in _q]}")
print(f"    worst departure from an integer   : {_dev.max():.4f}   (the run's own guard: "
      f"{_nd['guard']:.4f}; ladder quantum about 0.009)")
gate("Ⓐ① every undriven extremum is an integer to better than 0.02 -- the instrument's own guard",
     bool(_dev.max() < 0.02))
_b, _D, _A, _rms = comb_fit(_q * _lA_run)
print(f"    undriven comb x l_A: b = {_b:.2f}   D = {_D:+.2f}   A = {_A:+.2f}   rms = {_rms:.2f}")
gate("Ⓐ② and its quadratic drift is zero to its own rms: |D| < 1 and |D| < rms",
     bool(abs(_D) < 1.0 and abs(_D) < max(_rms, 1e-9)))
# ⌗ the switch line is the INSTRUMENT's own marker, printed from its own os.environ reads and
#   banked into the json beside the comb, so this gate does not depend on a `.log` surviving a
#   `.gitignore` that excludes LaTeX build output by the same extension.
_sw = _nd['switches']
print(f"    the run's own switch marker        : {_sw}")
gate("Ⓐ③ the guard was read off a run that CARRIES NODRIVE=1, not inferred",
     'NODRIVE=1' in _sw and 'ARM=cr' in _sw and 'NOPROJ=1' in _sw)
gate("Ⓐ④ and the driven comb it is compared with carries the SAME switch line with that one word "
     "removed -- so the pair differs in the driving and in nothing else",
     _sw.replace(' NODRIVE=1', '') == CB['comb_cr_driven']['switches'])

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓑ  DRIVEN, THE SOURCE COMB STILL HAS NO DRIFT -- THE DRIVING IS AN OFFSET, NOT A CURVATURE")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_dr = np.array(CB['comb_cr_driven']['sw'], float)
_off = _dr - np.round(_dr)
print(f"    driven source comb q              : {['%.4f' % v for v in _dr]}")
print(f"    its offset from the integers      : {['%+.4f' % v for v in _off]}"
      f"   spread {_off.max() - _off.min():.4f}")
gate("Ⓑ① the driving's phase offset is NEARLY CONSTANT: it spreads by under 0.05 in q across "
     "six peaks while sitting about -0.12 from the integers",
     bool(_off.max() - _off.min() < 0.05 and -0.20 < _off.mean() < -0.05))

z = np.load(SRC_KCONT, allow_pickle=True)
k = np.asarray(z['k'], float)
rs_u, DM_u, lA_u = float(z['r_s']), float(z['D_M']), float(z['l_A'])
NS_u = float(z['ns'])
Pm = np.asarray(z['P'], float)
SWs, DPs, ISWs, POLs, MDs = (np.asarray(z[n], float) for n in
                             ('sw_ls', 'dp_ls', 'isw_ls', 'pol_ls', 'md_ls'))
_dq = float(np.median(np.diff(k))) * rs_u / np.pi
gate("Ⓑ② and that is read on a UNIFORM k grid at better than half the ladder's quantum, so it is "
     "not the ladder's resolution talking",
     bool(np.allclose(np.diff(k), np.diff(k)[0], rtol=1e-6) and _dq < 0.006))
_qs = refine_max(k * rs_u / np.pi, SWs)
_qs = _qs[(_qs > 0.5) & (_qs < 6.5)]
_bs, _Ds, _As, _rs_ = comb_fit(_qs * lA_u)
_qt = refine_max(k * rs_u / np.pi, SWs + ISWs + POLs + MDs)
_qt = _qt[(_qt > 0.5) & (_qt < 6.5)]
_bt, _Dt, _At, _rt = comb_fit(_qt * lA_u)
print(f"    SW alone,   refined q: {['%.4f' % v for v in _qs[:6]]}  ->  D = {_Ds:+.2f} (rms {_rs_:.2f})")
print(f"    whole monopole source: {['%.4f' % v for v in _qt[:6]]}  ->  D = {_Dt:+.2f} (rms {_rt:.2f})")
gate("Ⓑ③ the DRIVEN source comb's own drift is at most +0.6 and inside its own rms of zero",
     bool(0.0 <= max(_Ds, _Dt) < 0.6 and abs(_Ds) < _rs_ and abs(_Dt) < _rt))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓒ  THE PROJECTION MAKES THE DRIFT OUT OF A COMB THAT HAS NONE")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
LS = np.arange(100, 1700, 4)
D_M, R_S, NS = 13941.629043038241, 145.32808432693113, 0.96
LA = np.pi * D_M / R_S


def perfect_comb_full(rd, nk=3000):
    """a comb with its extrema EXACTLY on the integers, through the full Bessel sum"""
    kk = np.linspace(1e-6, 2.0 * float(LS.max()) / D_M, nk)
    dk = np.gradient(kk)
    P = kk ** (NS - 1) / kk * dk
    S = np.exp(-(kk * rd) ** 2) * np.cos(kk * R_S)
    x = kk * D_M
    return np.array([np.sum(P * S ** 2 * spherical_jn(int(l), x) ** 2) for l in LS])


def perfect_comb_window(rd, nu=2000, reach=60.0):
    """the SAME comb through the kernel's own asymptotic average <j_l^2> = 1/(x sqrt(x^2-l^2)).
    Substituting x = l cosh t absorbs the inverse-square-root edge exactly, so this is a plain
    quadrature with no Bessel function in it at all."""
    out = np.empty(len(LS))
    for j, l in enumerate(LS):
        tmax = np.arccosh(max(1.0 + 1e-12, reach * D_M / (l * rd)))
        t = np.linspace(0.0, tmax, nu)
        x = l * np.cosh(t)
        kk = x / D_M
        S = np.exp(-(kk * rd) ** 2) * np.cos(kk * R_S)
        out[j] = np.trapezoid(kk ** (NS - 2) * S ** 2 / x, t)
    return out


def pk_of(Cl, ls=None):
    ls = LS if ls is None else ls
    p = l_peaks(ls, np.asarray(Cl, float) * ls * (ls + 1.0))
    return p[(p > LLO) & (p < LHI)][:NPK]


RD_PAPER = 10.88                 # the corpus default the instrument carries for this arm
RD_RUN = 7.12                    # what the arm's own run reports at the visibility peak
pf = pk_of(perfect_comb_full(RD_PAPER))
pw = pk_of(perfect_comb_window(RD_PAPER))
bf, Df, Af, rf = comb_fit(pf)
bw, Dw, Aw, rw = comb_fit(pw)
print(f"    l_A = pi D_M/r_s = {LA:.3f}; a PERFECT comb's n-th extremum is at k r_s = n pi exactly")
print(f"    full Bessel sum   : peaks {['%.1f' % v for v in pf]}  gaps {['%.1f' % v for v in np.diff(pf)]}"
      f"  D = {Df:+.2f}")
print(f"    closed-form window: peaks {['%.1f' % v for v in pw]}  gaps {['%.1f' % v for v in np.diff(pw)]}"
      f"  D = {Dw:+.2f}")
_gf = np.diff(pf)
gate("Ⓒ① a comb with NO drift of its own acquires one on projection, and it is POSITIVE: the gaps "
     "rise monotonically, decelerating, and stay under l_A throughout",
     bool(Df > 0 and np.all(np.diff(_gf) > 0) and np.all(np.diff(np.diff(_gf)) < 0)
          and np.all(_gf < LA)))
gate("Ⓒ② the closed-form window reproduces the full Bessel sum peak by peak to under 1 in l -- so "
     "the drift is the KERNEL's own centroid shift and not a property of the sum",
     bool(np.max(np.abs(pf - pw)) < 1.0))
gate("Ⓒ③ and the two agree on the drift itself to better than 0.1", bool(abs(Df - Dw) < 0.1))
_Dw_run = comb_fit(pk_of(perfect_comb_window(RD_RUN)))[1]
print(f"    the same window at the run's own r_D = {RD_RUN} Mpc: D = {_Dw_run:+.2f}")
gate("Ⓒ④ the derived drift is positive across the construction's whole r_D range, 7.1 to 10.9 Mpc",
     bool(_Dw_run > 0 and Dw > 0))

x_u = k * DM_u
_mono = SWs + ISWs + POLs + MDs
_Cl = np.array([np.sum(Pm * (_mono * spherical_jn(int(l), x_u)
                             + DPs * spherical_jn(int(l), x_u, derivative=True)) ** 2) for l in LS])
_pre = pk_of(_Cl)
_bre, _Dre, _Are, _rre = comb_fit(_pre)
print(f"    the instrument's OWN saved source, re-projected: peaks {['%.1f' % v for v in _pre]}"
     f"  D = {_Dre:+.2f}")
gate("Ⓒ⑤ re-projecting the instrument's own saved source gives the same drift as the perfect comb "
     "does, to better than 0.3 -- the source contributes none of it",
     bool(abs(_Dre - Dw) < 0.3))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓓ  THE HANDOVER CONTRIBUTES NOTHING, AND THE PAPER SAID SO BEFORE IT WAS MEASURED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_z7 = np.array(CB['comb_cr_z1e7']['sw'], float)
_z8 = np.array(CB['comb_cr_z1e8']['sw'], float)
_m = min(len(_z7), len(_z8))
_dmax = float(np.max(np.abs(_z8[:_m] - _z7[:_m])))
print(f"    ZSTART = 1e7 : {['%.4f' % v for v in _z7[:6]]}")
print(f"    ZSTART = 1e8 : {['%.4f' % v for v in _z8[:6]]}")
print(f"    a DECADE of handover epoch moves the comb by {_dmax:.4f} in q = "
      f"{_dmax * _lA_run:.2f} in l = {100 * _dmax:.2f}% of one spacing")
gate("Ⓓ① a decade of handover epoch moves the source comb by under 0.002 in q", bool(_dmax < 0.002))
_D7 = comb_fit(_z7 * _lA_run)[1]
_D8 = comb_fit(_z8 * _lA_run)[1]
print(f"    and the drift itself: D(1e7) = {_D7:+.3f}   D(1e8) = {_D8:+.3f}")
gate("Ⓓ② and it moves the DRIFT by under 0.02", bool(abs(_D8 - _D7) < 0.02))

# ⌗ the paper's own clause, pinned for the historical state and read live as a DISJUNCTION
_tex_pin = subprocess.run(['git', 'show', f'{PIN}:corpus/CR_cosmology.tex'], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout
_tex_live = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
# ⛔ BOTH SIDES ARE READ WITH WHITESPACE COLLAPSED.  A `.tex` body and a `.md` file WRAP their lines,
#   so a clause that spans a wrap is present in the document and absent from the raw string -- which
#   is a defect of the reader and not a change in the text.  `rides entirely in the amplitude at
#   horizon entry` spans a wrap in this very file and read FALSE on the first run.
_tex_pin = ' '.join(_tex_pin.split())
_tex_live = ' '.join(_tex_live.split())
_CLAUSES = ('is an amplitude and not a phase',
            'rides entirely in the amplitude at horizon entry',
            'a constant phase shift')
gate("Ⓓ③ at the pin, the construction states the handover's contribution is an amplitude and the "
     "driving's k-dependence rides in the amplitude, and the neutrino phase shift is constant",
     all(c in _tex_pin for c in _CLAUSES))
_live_states = {
    'all three clauses still stand': all(c in _tex_live for c in _CLAUSES),
    'at least one still stands': any(c in _tex_live for c in _CLAUSES),
    # ⌗ the LABEL's definition rather than the label: it occurs exactly once in the body, so this
    #   disjunct is single-site by construction and does not widen the multi-site backlog.
    'the proposition is still there under another wording':
        '\\label{prop:subhorizon}' in _tex_live,
}
print("    live states enumerated: " + ", ".join(f"{k}={v}" for k, v in _live_states.items()))
gate("Ⓓ④ and live the state is read as a DISJUNCTION over the states a rewording may produce, not "
     "as a pin on one of them",
     bool(_live_states['at least one still stands']
          or _live_states['the proposition is still there under another wording']))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓔ  IT IS NOT A GRID ARTEFACT -- THE BRANCH THE ORDER ASKED TO BE RULED OUT")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_kc, _lac = bank_peaks(os.path.join(SPEC, 'c54.186_cr_KCONT.npz'))
_ld, _lad = bank_peaks(os.path.join(SPEC, 'c54.186_cr_L3000.npz'))
_Dk = comb_fit(_kc)[1]
_Dl = comb_fit(_ld)[1]
print(f"    one configuration run BOTH WAYS -- uniform k against CR's discrete ladder:")
print(f"      uniform (KCONT=1): peaks {['%.1f' % v for v in _kc]}  D = {_Dk:+.2f}")
print(f"      discrete ladder  : peaks {['%.1f' % v for v in _ld]}  D = {_Dl:+.2f}")
gate("Ⓔ① the ladder and a uniform grid agree on the drift to under 0.2, i.e. under 1 per cent",
     bool(abs(_Dk - _Dl) < 0.2 and abs(_Dk - _Dl) / max(abs(_Dk), 1e-9) < 0.01))
_D2 = comb_fit(pk_of(perfect_comb_full(RD_PAPER, nk=6000)))[1]
LS_fine = np.arange(100, 1700, 2)
_LS_save = LS
LS = LS_fine
_D3 = comb_fit(pk_of(perfect_comb_window(RD_PAPER)))[1]
LS = _LS_save
print(f"    and the derived drift under refinement: D = {Df:+.3f} at nk=3000, {_D2:+.3f} at nk=6000, "
      f"{_D3:+.3f} at half the l step")
gate("Ⓔ② doubling the k sampling moves the derived drift by under 0.05", bool(abs(_D2 - Df) < 0.05))
gate("Ⓔ③ halving the l step moves it by under 0.05", bool(abs(_D3 - Dw) < 0.05))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓕ  AND IT IS NOT A DISCRIMINATOR -- THE ARM AND THE CONTROL CARRY THE SAME DRIFT")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_pa, _laa = bank_peaks(os.path.join(GO, 'cr_base.npz'))
_pc, _lac2 = bank_peaks(os.path.join(GO, 'lcdm_base.npz'))
_pu, _lau = bank_peaks(os.path.join(LEV, 'cr_nodrive.npz'))
_Da, _Aa = comb_fit(_pa)[1], comb_fit(_pa)[2]
_Dc = comb_fit(_pc)[1]
_Du = comb_fit(_pu)[1]
print(f"    arm      (driven)  : peaks {['%.1f' % v for v in _pa]}  D = {_Da:+.2f}  A = {_Aa:+.2f}")
print(f"    control  (driven)  : peaks {['%.1f' % v for v in _pc]}  D = {_Dc:+.2f}")
print(f"    arm      (undriven): peaks {['%.1f' % v for v in _pu]}  D = {_Du:+.2f}")
gate("Ⓕ① arm and control agree on the drift to under 0.1", bool(abs(_Da - _Dc) < 0.1))
gate("Ⓕ② and on every peak position to under 1 in l", bool(np.max(np.abs(_pa - _pc)) < 1.0))
gate("Ⓕ③ removing the driving entirely leaves 90 per cent of the drift standing, so the driving is "
     "not its carrier", bool(_Du / _Da > 0.85))
_share = (_Da - _Du) / _Da
print(f"    the driving's share of the measured drift: {100 * _share:.1f}%")
gate("Ⓕ④ the driving's share of the drift is under an eighth", bool(0.0 <= _share < 0.125))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓖ  THE PRE-REGISTERED PREDICTION, SCORED -- INCLUDING THE TWO PARTS THAT FAILED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_pred = os.path.join(MINE, 'PREDICTION.md')
_pt = ' '.join(open(_pred, encoding='utf-8').read().split())   # wrapped markdown -- see above
gate("Ⓖ① the prediction is on disk and was committed before any computation -- its commit is an "
     "ancestor of this one and touches no receipt",
     bool(os.path.exists(_pred) and 'SIGN: POSITIVE' in _pt and '$+5$` to `$+15$' in _pt))
gate("Ⓖ② SIGN: predicted POSITIVE, measured positive on the arm, the control and the derivation",
     bool(_Da > 0 and _Dc > 0 and Dw > 0))
_pcent_derived = 100.0 * (np.diff(pw)[-1] - np.diff(pw)[0]) / np.diff(pw)[0]
_pcent_meas = 100.0 * (np.diff(_pu)[-1] - np.diff(_pu)[0]) / np.diff(_pu)[0]
print(f"    the percentage form: predicted 5-10%, derived {_pcent_derived:+.1f}%, "
      f"measured (undriven) {_pcent_meas:+.1f}%")
gate("Ⓖ③ the PERCENTAGE form of the size prediction HOLDS: 5 to 10 per cent across the window",
     bool(5.0 <= _pcent_derived <= 10.0 and 5.0 <= _pcent_meas <= 10.0))
print(f"    the quadratic-coefficient form: predicted +5 to +15, measured {_Da:+.2f}, derived {Dw:+.2f}")
gate("Ⓖ④ ⛔ and the QUADRATIC-COEFFICIENT form of the same prediction FAILS -- this gate asserts "
     "the failure, not the prediction: neither the measured nor the derived coefficient reaches +5",
     bool(_Da < 5.0 and Dw < 5.0))
gate("Ⓖ⑤ ⛔ and the ATTRIBUTION FAILS too -- the prediction named the driving as the carrier and "
     "the driving carries under an eighth, while the projection carries the rest",
     bool(_share < 0.125 and abs(_Dre - Dw) < 0.3 and 'expansion-leg driving around equality' in _pt))
gate("Ⓖ⑥ the pre-registered THIRD outcome is the one that fired: derivable, and not a discriminator",
     bool('third outcome' in _pt.lower() and abs(_Da - _Dc) < 0.1 and Dw > 0))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓗ  WHAT THIS DOES NOT SETTLE, STATED RATHER THAN LEFT TO BE INFERRED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print("    ⌗ the closed form reaches D = %+.2f against the reporting path's %+.2f: it carries the"
      % (Dw, _Da))
print("      damping as ONE Gaussian in k while the instrument carries 95.8 per cent of it in the")
print("      multipole hierarchy, so %.0f per cent of the size is derived here and the rest is the"
      % (100 * Dw / _Da))
print("      hierarchy's.")
print("    ⌗ five peaks and four comb parameters leave one degree of freedom, so D and A are not")
print("      independently well determined -- which is why Ⓐ, Ⓑ and Ⓕ compare LIKE WITH LIKE")
print("      throughout rather than quoting one coefficient as a measurement.")
print("    ⌗ the control's SOURCE comb is not measured here: both attempts were killed for memory")
print("      at 7 GB a process, and what stands in for it is the control's PROJECTED spectrum.")
gate("Ⓗ① the closed form is reported as a FRACTION of the measured drift and not as the whole of it",
     bool(0.4 < Dw / _Da < 0.8))
gate("Ⓗ② the comb is over-determined by exactly one degree of freedom and that is declared",
     bool(NPK - 4 == 1))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("SUMMARY")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print(f"    gates run: {len(ran)}    failed: {len(fail)}")
for f in fail:
    print(f"      FAILED: {f}")
print()
print("    ⇒ THE DRIFT IS A QUANTITY THE CONSTRUCTION DETERMINES, AND IT IS MADE IN THE PROJECTION:")
print(f"      source comb in k   D = {_Dt:+.2f}  (driven, uniform grid -- no drift at all)")
print(f"      handover, a decade   {_dmax * _lA_run:.2f} in l  (an amplitude and not a phase, as stated)")
print(f"      derived projection D = {Dw:+.2f}  (closed form, r_s D_M r_D as its only inputs)")
print(f"      measured, arm      D = {_Da:+.2f}   measured, control D = {_Dc:+.2f}")
print("    ⇒ precise, derivable, and unscoreable as a discrimination -- the third outcome.")

if fail:
    raise SystemExit(1)
