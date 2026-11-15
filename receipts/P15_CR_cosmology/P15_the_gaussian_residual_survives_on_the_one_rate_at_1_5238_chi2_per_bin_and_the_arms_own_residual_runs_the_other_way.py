#!/usr/bin/env python3
r"""`r7783` ** THE DIFFUSION-SCALE GAUSSIAN `P15` SAYS NO TILT REMOVES SURVIVES ON THE RATE THE
UNIVERSE HAS, AND LARGER: `1.5238` chi^2/bin AFTER THE TILT AT `l_D = 1355.21`, AGAINST `1.4967` AT
`1362` -- STILL ABOVE **BOTH** OF `C62`'s BOUNDS, STILL THE PREDICTED SHAPE TO `1.000000`, AND THE
TILT STILL TAKES `69.8` PER CENT. **

** AND THE ARMS' OWN RESIDUAL IS A DIFFERENT OBJECT THAT RUNS THE OTHER WAY: ** a plain power law
fits it BETTER than the Gaussian does (`+0.851` against `+0.498`), and with the power law projected
out the Gaussian's partial correlation is `-0.789`.

Built `r7783+cc66.3`, discharging order ② of the chat seat's `r7783`.

===================================================================================================
** COMPUTES: ** the joint fit of `P15`'s diffusion-scale signature against a tilt, re-run at two
   damping multipoles.  The signature is `S(l) = exp[-(r^2 - 1)(l/l_D)^2]` with `r = 1.0926` and
   `l_D = 1362` as the published INPUTS; the baseline is the banked LambdaCDM control
   `spectra/L820_lcdm_L2512_nk800.npz` normalised to the data; the model is `A (l/1000)^(dn)` times
   that baseline; the metric is `plik_lite` TT's own bandpowers, binning and covariance restricted to
   covered bins ON the covariance.  `l_D` on the one rate is `1362` times the projection distance's
   OWN measured move, read from the two banked arms' `D_M`.  Nothing is fitted to data beyond the two
   parameters the fit is of, and no significance is computed.
===================================================================================================

⛔ ** WHAT `P15` PRINTS FOR THIS IS QUALITATIVE, AND `(1)` CHECKS THAT BEFORE ANYTHING ELSE. **  The
paper says *"the diffusion-scale signature it carries is located by the joint fit as a Gaussian
residual in `l` that no tilt removes"*, and in `sec:coherence` *"whose shape is a Gaussian in `l`, and
no tilt removes a Gaussian"*.  ** Two sites, and neither carries a `chi^2`/bin figure. **  *So this
receipt does not confirm a published number -- it supplies one, so the claim can be quoted with a size
on the rate the universe has, which is the service the comb receipt did for `298.94`.*

⛭ ** WHY ONLY `l_D` MOVES, AND WHY THAT IS NOT AN ASSUMPTION. **  `K = r^2 - 1` is built from the
damping-scale **ratio**, from which the distance cancels identically -- `(2)` measures that the joint
fit and the damping receipt it inherits `r` from mention a distance **zero** times, and that no CR arm
spectrum enters either.  So the only way a projection distance reaches this object is through `l_D`,
which is a multipole.  ⛔ *`(2)` does NOT search for a bare `chi`: that file is full of `chi^2`, and my
first form of this test at `r7779` counted twenty-one of those and reddened its own row.*

⛭ ** THE FIT IS NOT REIMPLEMENTED HERE. **  `(4)` and `(5)` run the joint-fit receipt's OWN source
with its one declared `INPUT` line rewritten, so the two runs differ in `l_D` and in nothing else --
and `(4)` is the row that proves it, reproducing the published `1.4967` exactly at the unshifted value.
⛔ *Both the `HERE` and `ROOT` anchors are pinned, not just `ROOT`: that receipt reads a SIBLING
receipt (`C62`) off `HERE`, and at `r7779` pinning only `ROOT` killed both runs before any fit.*  Each
run costs about `5` s, measured.

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that the one-rate residual is more or less consistent with the sky. **  No significance is
   computed for either value.
 * ** Not a re-adjudication of `C62`'s two routes. **  Both bounds are carried as that receipt left
   them, the instrument route `0.92` and the data-shape route `0.26`.
 * ** Not that `r` is unchanged by the rate. **  `r` is HELD here because `(2)` licenses holding it
   against the DISTANCE; what the clock `r_D` and `r_s` accumulate on does move it, and that is
   `r7767`'s `+2.21 %` against `-34.78 %`, not this receipt's subject.

⛭ ** FAILABILITY, MEASURED. **  Scaling the projection distance's MEASURED move by `1 + 1e-2` -- so
`l_D` shifts by `0.068` of a multipole instead of `6.788` -- reddens `(3)`, `(5)` and `(7)`: the shift,
the one-rate fit and the figure pins.  `(1)`, `(2)`, `(4)` and `(6)` hold, since they read the paper's
prose, the two receipts' source, the fit at the PUBLISHED `l_D` and the arms' spectra.
  ⛔ *Not `r`, which was the probe's first knob and measured nothing: this receipt builds the
  joint-fit receipt's declared `INPUT` line from `R` and `l_D` and refuses to run if that line is not
  found -- a good coupling, since it asserts the published values, but it makes either of them the
  wrong knob, because perturbing one exits `FATAL` before any fit.*  Measured in
`computations/beyond_the_wall/r7783_cc66_the_gaussian_receipt/failability.py`.

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; about 15 s -- two joint fits at 5 s each)
7 gates.  `(7)` pins every figure the INDEX row prints, each to half its last printed digit.
"""
import os
import re
import subprocess
import sys
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
JF = os.path.join(HERE, 'P15_the_joint_fit_leaves_the_gaussian_and_the_bound_was_chi2_not_sigma.py')
DAMP = os.path.join(HERE, 'P15_the_damping_signature_error_budget_and_the_convention_dominates_it.py')
LD0, R_SIG = 1362.0, 1.0926
C62_INSTRUMENT, C62_DATA_SHAPE = 0.92, 0.26
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f'             {witness}')


for p in (JF, DAMP, TEX):
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the instrument has moved.')
tex = open(TEX, encoding='utf-8').read()
jf_src = open(JF, encoding='utf-8').read()
damp_src = open(DAMP, encoding='utf-8').read()

print('=' * 100)
print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------- (1) the paper's claim is qualitative
n_phrase = tex.count('no tilt removes')
has_fig = any(f in tex for f in ('1.4967', '1.5238', '1.50 $\\chi^2$'))
check("⛭⛔⛭ `r7783` ** ① `P15`'s CLAIM HERE IS **QUALITATIVE** -- *\"a Gaussian residual in `l` that no "
      "tilt removes\"*, AT TWO SITES, WITH NO `chi^2`/bin FIGURE ANYWHERE ** ⇒ *** so this receipt "
      "SUPPLIES the number rather than confirming one, and `69` can quote the claim with a size on the "
      "rate the universe has. ** That is the same service the comb receipt did for `298.94`. ** *** ⌗ "
      "*If the paper ever carries a figure for this, THIS row goes red and the receipt's job changes "
      "from supplying to confirming -- which is the state change worth catching*",
      n_phrase >= 1 and not has_fig,
      f"'no tilt removes' appears {n_phrase} times; a chi^2/bin figure for it in the paper: {has_fig}")

# ---------------------------------------------------------------- (2) the amplitude is distance-free
k_line = [l for l in jf_src.splitlines() if l.strip().startswith('K = ')]
dist = len(re.findall(r'\bD_M\b|\bD_C\b|\bD_A\b|comoving', jf_src))
dist_damp = len(re.findall(r'\bD_M\b|\bD_C\b|\bD_A\b|comoving', damp_src))
base = 'L820_lcdm_L2512_nk800.npz' in jf_src
arm = any(t in jf_src for t in ('r7749', 'leafgeom', 'cc66_cr_x_h686'))
check("⛭ `r7783` ** ② THE GAUSSIAN'S AMPLITUDE IS DISTANCE-FREE, SO ONLY `l_D` CAN MOVE: `K = R**2 - 1` "
      "WITH `R` THE **RATIO**, A CONTROL BASELINE, NO CR ARM, AND **ZERO** DISTANCES IN EITHER RECEIPT "
      "** ⇒ *** the damping-scale ratio is the one quantity in this construction the projection cancels "
      "out of identically, which `r7767` item 1 established and this row re-measures at the source. ** "
      "*** ⌗ *NOT a search for a bare `chi`: these files are full of `chi^2`, and my first form of this "
      "test counted twenty-one of those and reddened the row*",
      k_line == ['K = R**2 - 1'] and base and not arm and dist == 0 and dist_damp == 0,
      f"K line {k_line}; control baseline present {base}; a CR arm named {arm}; distances in the joint "
      f"fit {dist} and in the damping receipt {dist_damp}")

# ---------------------------------------------------------------- (3) l_D moves with the distance


def dm(tag):
    with np.load(os.path.join(SPEC, tag + '.npz'), allow_pickle=True) as z:
        return float(z['D_M'])


dmS = dm('cc66_cr_x_h686_L2000_leafrec1_distances')
dmL = dm('r7749_leafgeom_nofit_L2000_cr')
mv = dmL / dmS - 1.0
LD1 = LD0 * (1.0 + mv)
check("⛭ `r7783` ** ③ AND `l_D` IS A MULTIPOLE, SO IT MOVES WITH THE PROJECTION: `1362 -> 1355.21`, A "
      "SHIFT OF `6.788` MULTIPOLES ** ⇒ *the shift is computed from the two banked arms' own `D_M` "
      "(`14011.457 -> 13941.629` Mpc) and not from a retyped percentage, so it moves if either bank "
      "does*",
      abs((LD0 - LD1) - 6.7877) < 0.001,
      f"D_M {dmS:.4f} -> {dmL:.4f} ({100*mv:+.4f}%); l_D {LD0:.2f} -> {LD1:.4f}, "
      f"a shift of {LD0 - LD1:.4f}")

# ---------------------------------------------------------------- (4)(5) the joint fit, twice
_IN = f'R, LD = {R_SIG}, {LD0}'
if _IN not in jf_src:
    sys.exit(f'FATAL: the joint-fit receipt no longer declares its inputs as `{_IN}`.')


def joint(ld, r=R_SIG):
    text = jf_src.replace(_IN, f'R, LD = {r!r}, {ld!r}')
    for rl, new in (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {HERE!r}'),
                    ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')):
        if rl not in text:
            sys.exit(f'FATAL: the joint-fit receipt no longer carries `{rl}`.')
        text = text.replace(rl, new)
    with tempfile.TemporaryDirectory() as td:
        q = os.path.join(td, 'jf.py')
        open(q, 'w', encoding='utf-8').write(text)
        pr = subprocess.run([sys.executable, '-I', q], capture_output=True, text=True, cwd=HERE,
                            timeout=1800)
    m = re.search(r'^\s*100-1760\s+(\d+)\s+(-?\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)%', pr.stdout, re.M)
    c = re.search(r'power law\) at (\d\.\d{4,})', pr.stdout)
    return dict(rc=pr.returncode, bins=int(m.group(1)) if m else None,
                dn=float(m.group(2)) if m else None, chi2=float(m.group(3)) if m else None,
                absorbed=float(m.group(4)) if m else None, corr=float(c.group(1)) if c else None)


A, B = joint(LD0), joint(LD1)
print(f"\n      {'l_D':>10} {'rc':>3} {'bins':>5} {'Delta n_s':>11} {'chi2/bin':>10} "
      f"{'absorbed':>9} {'correlation':>12}")
for lab, g in ((f'{LD0:.2f}', A), (f'{LD1:.2f}', B)):
    print(f"      {lab:>10} {g['rc']:>3} {str(g['bins']):>5} {str(g['dn']):>11} {str(g['chi2']):>10} "
          f"{str(g['absorbed']):>9} {str(g['corr']):>12}")
check("⛭ `r7783` ** ④ AND THE HARNESS IS FAITHFUL: AT THE PUBLISHED `l_D` IT REPRODUCES `1.4967` "
      "chi^2/bin, `69.8 %` ABSORBED AND `1.000000` **EXACTLY** ** ⇒ *** this is the row that makes `⑤` a "
      "measurement of the SHIFT rather than of the copy: the receipt's own source is run, with only its "
      "declared `INPUT` line and its two path anchors rewritten. ** *** ⌗ *`171` covered bins over "
      "`P15`'s own `l = 100`-`1758` ceiling window*",
      A['rc'] == 0 and A['bins'] == 171 and abs(A['chi2'] - 1.4967) < 0.00005
      and abs(A['absorbed'] - 69.8) < 0.05 and A['corr'] is not None and A['corr'] >= 0.999999
      and abs(A['dn'] - (-0.08304)) < 0.000005,
      f"at l_D = {LD0}: chi2/bin {A['chi2']}, absorbed {A['absorbed']}%, correlation {A['corr']}, "
      f"Delta n_s {A['dn']}, over {A['bins']} bins")
rel = abs(B['chi2'] / A['chi2'] - 1.0) if A['chi2'] and B['chi2'] else 1.0
check("⛭⛭⛭ `r7783` ** ⑤ AND AT THE SHIFTED `l_D` THE RESIDUAL **SURVIVES**, `1.81 %` LARGER: `1.5238` "
      "chi^2/bin AFTER THE TILT, ABOVE **BOTH** OF `C62`'s BOUNDS ** ⇒ *** `0.92` by the instrument "
      "route and `0.26` by the data-shape route, so the claim *\"no tilt removes it\"* holds on the rate "
      "the universe has as it does on the arm of record. ** The shape correlation stays `1.000000` and "
      "the tilt still takes `69.8` per cent. ** *** ⌗ *A half-per-cent shift of a smooth Gaussian barely "
      "changes its projection onto a power law, which is why the move is `1.81 %` and not `50`*",
      B['rc'] == 0 and abs(B['chi2'] - 1.5238) < 0.00005 and B['chi2'] > C62_INSTRUMENT
      and rel < 0.05 and abs(B['absorbed'] - 69.8) < 0.05 and B['corr'] >= 0.999999
      and abs(B['dn'] - (-0.08383)) < 0.000005,
      f"at l_D = {LD1:.2f}: chi2/bin {B['chi2']} (a move of {100*rel:.3f}%), absorbed "
      f"{B['absorbed']}%, correlation {B['corr']}, Delta n_s {B['dn']}; C62's bounds "
      f"{C62_INSTRUMENT} and {C62_DATA_SHAPE}")

# ---------------------------------------------------------------- (6) the arms' residual, separated
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                                   # noqa: E402


def binned(tag):
    with np.load(os.path.join(SPEC, tag + '.npz'), allow_pickle=True) as z:
        return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


lsC, DlC = binned('cc66_cr_x_h686_L2000_leafrec1_distances')
rows = []
for tag, lab in (('r7749_leafgeom_nofit_L2000_cr', 'LEAFGEOM=1, nofit'),
                 ('r7749_leafgeom_refit_verify_cr', 'LEAFGEOM=1, refit (verified)')):
    lsA, DlA = binned(tag)
    bC, bA = CS.bin_spectrum(lsC, DlC), CS.bin_spectrum(lsA, DlA)
    keep = np.isfinite(bC) & np.isfinite(bA)
    lc = np.asarray(CS.bin_center_and_fac()[0], float)[keep]
    y = (bA - bC)[keep]
    g = np.exp(-(R_SIG ** 2 - 1.0) * (lc / LD1) ** 2) - 1.0
    pl = (lc / 1000.0) ** (B['dn']) - 1.0
    X = np.vstack([np.ones_like(lc), pl]).T

    def _r(v):
        return v - X @ np.linalg.lstsq(X, v, rcond=None)[0]

    def _c(u, v):
        u, v = u - u.mean(), v - v.mean()
        return float(np.dot(u, v) / np.sqrt(np.dot(u, u) * np.dot(v, v)))

    rows.append((lab, _c(y, g), _c(y, pl), _c(_r(y), _r(g))))
    print(f'      {lab:30s} vs Gaussian {rows[-1][1]:+.4f}; vs a PLAIN POWER LAW {rows[-1][2]:+.4f}; '
          f'partial, power law removed, {rows[-1][3]:+.4f}')
check("⛭⛔⛭ `r7783` ** ⑥ AND THE `r7749` ARMS' OWN RESIDUAL IS A **DIFFERENT OBJECT THAT RUNS THE OTHER "
      "WAY**: A PLAIN POWER LAW FITS IT BETTER THAN THE GAUSSIAN DOES, AND WITH THE POWER LAW PROJECTED "
      "OUT THE GAUSSIAN'S PARTIAL CORRELATION IS `-0.789` ** ⇒ *** `+0.851` against `+0.498` raw, so the "
      "raw agreement is shared smoothness -- two nearly monotone functions of `l` over `185` bins share "
      "a broad shape by construction. ** What those arms leave is the TT contrast residual, whose own "
      "measured carrier is the ratio of the arms' distances to last scattering; it is not this "
      "Gaussian. ** *** ⌗ *The row asserts the SIGN: at `r7779` I wrote this test as "
      "`|partial| <= |raw|`, assuming \"adds nothing\" would read as a partial near zero, and it does "
      "not*",
      len(rows) == 2 and all(p < -0.5 and abs(n) > abs(r) for _, r, n, p in rows),
      '; '.join(f'{l}: raw {r:+.3f}, power law {n:+.3f}, partial {p:+.3f}' for l, r, n, p in rows))

# ---------------------------------------------------------------- (7) every printed figure, pinned
# ⛔ Written as explicit comparisons: `check_figures_pinned` PARSES the receipt rather than running
#   it, so a literal inside a table a loop walks is not a pin.  That cost a cycle at `r7779+cc66.3`.
_ps = [
    ('l_D published', abs(LD0 - 1362.0) < 0.05),
    ('l_D on the one rate', abs(LD1 - 1355.21) < 0.005),
    ('the l_D shift', abs((LD0 - LD1) - 6.788) < 0.0005),
    ('chi2/bin published', abs(A['chi2'] - 1.4967) < 0.00005),
    ('chi2/bin on the one rate', abs(B['chi2'] - 1.5238) < 0.00005),
    ('the move, per cent', abs(100 * rel - 1.811) < 0.0005),
    ('absorbed, published', abs(A['absorbed'] - 69.8) < 0.05),
    ('absorbed, one rate', abs(B['absorbed'] - 69.8) < 0.05),
    ('the shape correlation', A['corr'] >= 0.999999 and B['corr'] >= 0.999999),
    ('Delta n_s published', abs(A['dn'] - (-0.08304)) < 0.000005),
    ('Delta n_s one rate', abs(B['dn'] - (-0.08383)) < 0.000005),
    ("C62's instrument route", abs(C62_INSTRUMENT - 0.92) < 0.005),
    ("C62's data-shape route", abs(C62_DATA_SHAPE - 0.26) < 0.005),
    ('arms vs a power law', abs(rows[0][2] - 0.851) < 0.0005),
    ('arms vs the Gaussian', abs(rows[0][1] - 0.498) < 0.0005),
    ('the partial correlation', abs(rows[0][3] - (-0.789)) < 0.0005),
    ('D_M, stacking rate', abs(dmS - 14011.457) < 0.0005),
    ('D_M, leaf rate', abs(dmL - 13941.629) < 0.0005),
]
off = [n for n, good in _ps if not good]
check("⛭ `r7783` ** ⑦ AND EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED **HERE**, EACH TO HALF ITS LAST "
      "PRINTED DIGIT ** ⇒ *** eighteen of them: both `l_D`, the shift, both `chi^2`/bin, the move, both "
      "absorbed fractions, the shape correlation, both displacements, `C62`'s two bounds, the three "
      "correlation figures and both distances. ** So no figure cited to this receipt can be wrong and "
      "leave it green. *** ⌗ *Written as explicit comparisons, because the gate PARSES this file rather "
      "than running it*",
      not off, f'{len(_ps)} printed figures, {len(off)} off their pin'
               + ('' if not off else ': ' + '; '.join(off[:4])))

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {7 - len(FAILS)} of 7 gates;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
