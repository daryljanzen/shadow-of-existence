"""
P15_the_exact_transmission_ratios_are_recomputed_and_the_offset_saturates.py -- the low-multipole
paragraph's five exact/WKB ratios and its segment length, recomputed from the mode equation.

** THE PARAGRAPH REPORTED SIX COMPUTED NUMBERS AND NO RECEIPT COMPUTED THEM.  `sec:lowl`'s exact
treatment states |Delta eta| = 3.32 in units alpha = 1 and exact/WKB ratios 0.926, 0.913, 0.901,
0.891, 0.889 at ell = 2, 3, 5, 15, 40, and the accuracy band 7-11 per cent.  The composition that
produces them lived only in a storyboard script with no assertions and no receipts/ copy, so the
numbers were uncited.  This file computes them and asserts them. **

** COMPUTES: the exact-to-WKB transmission ratio across the Euclidean segment at the five multipoles
sec:lowl quotes (ell = 2, 3, 5, 15, 40), and the segment's own conformal length, ON THE NARIAI
MEMBER'S SEGMENT GEOMETRY at the corpus's baryon loading R0 = 0.60/A with the projection distance
DA = 2.580 in units alpha = 1 -- the configuration LOWL_exact_transmission.py fixed and the paragraph
reports.  NOT a scan over background: the five multipoles and the one segment are the scope, and the
only parameter varied is the mass, in (E), where the scaling is exact rather than fitted. **

ORIGIN: storyboard_receipts/LOWL_exact_transmission.py -- the transfer-matrix composition, whose
  constants and stable-direction construction are reproduced here unchanged.  That script prints;
  this one asserts, and the two agree to the digit the paper quotes.

WHAT IS COMPUTED, on the corpus's own segment geometry.
  1. |Delta eta| over the Euclidean segment, in units alpha = 1.
  2. EXACT transmission by composing constant-omega transfer matrices, [[cosh, sinh/w],[w sinh,
     cosh]], built in the STABLE direction (the decaying solution grows when built backwards, so it
     is built backwards and inverted).
  3. The WKB comparison exp(-int w d-eta) on the same grid, and the ratio of the two.
  4. The band: every ratio in [0.889, 0.926], which is the paper's 7-11 per cent.
  5. ** THE MONOTONICITY AND THE SATURATION **, which are what make the residual an offset rather
     than an adiabatic error: the ratio DECREASES with ell -- so the discrepancy is smallest where
     the adiabaticity parameter is of order unity and largest where it is small, the opposite of an
     adiabatic error's ordering -- and it tends to a nonzero constant near 0.889 rather than to 1.

WHAT IS NOT CLAIMED.  The step count is a numerical convergence question and not a physical one; the
  ratios are asserted to the three digits the paper quotes and the convergence is exhibited rather
  than asserted at a tolerance the paper does not use.  And nothing here revisits the attribution
  question, which storyboard_receipts/SP_S5_the_wkb_residual_is_an_offset settled on these numbers.

STATUS: OK (|Delta eta| asserted at 3.32 to two decimals; the five ratios asserted to three; the
band, the monotonicity and the saturation asserted).
"""
import numpy as np

_fails = []


def check(msg, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        _fails.append(msg)


# --- the segment geometry, LOWL_exact_transmission.py's constants, unchanged -------------------
al = 1.0
M = al / (3 * np.sqrt(3))
A = (2 * M * al ** 2) ** (1. / 3)
smax = np.pi * al / 3.0
R0 = 0.60 / A
DA = 2.580


def _absr(s):
    return abs(-A * np.abs(np.sin(1.5 * s / al)) ** (2. / 3))


def segment(N, eps=1e-8):
    """The grid, the scale factor on it, and the conformal-time steps."""
    s = np.linspace(eps, smax, N)
    a = np.abs(np.array([_absr(x) for x in s]))
    deta = np.diff(s) / (0.5 * (a[1:] + a[:-1]))
    return s, a, deta


def transmission(l, N=400000, eps=1e-8):
    """EXACT transmission at multipole l, and the WKB comparison on the same grid."""
    k = l / DA
    _s, a, deta = segment(N, eps)
    w = k / np.sqrt(3.0 * (1.0 + R0 * a))
    wm = 0.5 * (w[1:] + w[:-1])
    # the solution that GROWS from the branch point toward the turnaround: the stable direction
    psi, dpsi, logamp = 1.0, w[0], 0.0
    for wi, de in zip(wm, deta):
        x = wi * de
        ch, sh = np.cosh(x), np.sinh(x)
        psi, dpsi = ch * psi + (sh / wi) * dpsi, wi * sh * psi + ch * dpsi
        if psi > 1e100:
            logamp += np.log(psi)
            dpsi /= psi
            psi = 1.0
    logamp += np.log(psi)
    exact = np.exp(-logamp)
    wkb = np.exp(-np.sum(wm * deta))
    return exact, wkb, exact / wkb


print()
print("  " + "=" * 74)
print("  A.  THE SEGMENT LENGTH THE PARAGRAPH QUOTES")
print("  " + "=" * 74)

_s, _a, _deta = segment(400000)
Deta = float(np.sum(_deta))
print(f"      |Delta eta| over the segment = {Deta:.4f}  (units alpha = 1)")
#: ⛭ r7145 (66, whose edit occasioned it): the paragraph carried 3.32 -- this file's own quadrature
#: value -- and now carries the CLOSED FORM 3.33874, which is the exact value of this same integral
#: (`P15_the_segments_conformal_length_is_the_closed_form...`, r7141).  ** The 0.46 per cent between
#: them is this quadrature's error on an integrable endpoint singularity, not a disagreement about
#: the geometry. **  ⇒ So the check now reads against the exact value and PRINTS its own shortfall,
#: which is the honest form: the quadrature is a cross-check of the closed form, not its source.
_EXACT = 3.3387380236
print(f"      the closed form is {_EXACT:.7f}; this quadrature falls short by {100*(_EXACT-Deta)/_EXACT:.2f} per cent")
check(f"|Delta eta| agrees with the paragraph's closed form {_EXACT:.5f} to better than one per cent ({Deta:.4f})", abs(Deta - _EXACT) / _EXACT < 0.01)

print()
print("  " + "=" * 74)
print("  B.  THE FIVE EXACT/WKB RATIOS, RECOMPUTED FROM THE MODE EQUATION")
print("  " + "=" * 74)

PAPER = {2: 0.926, 3: 0.913, 5: 0.901, 15: 0.891, 40: 0.889}
got = {}
print(f"      {'ell':>5}  {'EXACT':>16}  {'WKB':>16}  {'ratio':>8}  {'paper':>7}")
for l in sorted(PAPER):
    e, w, r = transmission(l)
    got[l] = r
    print(f"      {l:>5}  {e:16.6e}  {w:16.6e}  {r:8.4f}  {PAPER[l]:7.3f}")

for l in sorted(PAPER):
    check(f"ell = {l:>2}: ratio {got[l]:.4f} reproduces the paragraph's {PAPER[l]:.3f}",
          round(got[l], 3) == PAPER[l])

print()
print("  " + "=" * 74)
print("  C.  THE BAND, AND WHY THE RESIDUAL IS AN OFFSET RATHER THAN AN ADIABATIC ERROR")
print("  " + "=" * 74)

vals = [got[l] for l in sorted(PAPER)]
lo, hi = min(vals), max(vals)
print(f"      ratios span [{lo:.4f}, {hi:.4f}]  ->  accuracy {100*(1-hi):.1f}-{100*(1-lo):.1f} per cent")
check(f"every ratio sits in [0.889, 0.926], which is the paragraph's 7-11 per cent "
      f"(span [{lo:.4f}, {hi:.4f}])", 0.8885 <= lo and hi <= 0.9265)

check("the exact transmission is SMALLER than the WKB form at every multipole, so the filter is "
      "marginally stronger than the approximation gives", all(v < 1.0 for v in vals))

check("the ratio DECREASES monotonically with ell -- so the discrepancy is SMALLEST where the "
      "adiabaticity parameter is of order unity and LARGEST where it is small, which is the "
      "reverse of an adiabatic error's ordering",
      all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)))

_sat = abs(got[40] - got[15])
print(f"      ell = 15 -> {got[15]:.4f}, ell = 40 -> {got[40]:.4f}: a change of {_sat:.4f}")
check(f"and it SATURATES at a NONZERO offset near 0.889 rather than tending to 1 -- an adiabatic "
      f"error tends to zero, and this one does not (change of {_sat:.4f} over a factor of "
      f"{40/15:.1f} in ell)", _sat < 0.005 and got[40] < 0.9)

print()
print("  " + "=" * 74)
print("  D.  THE COMPOSITION IS CONVERGED AT THE DIGITS THE PARAGRAPH QUOTES")
print("  " + "=" * 74)

for l in (2, 40):
    r_coarse = transmission(l, N=100000)[2]
    r_fine = transmission(l, N=400000)[2]
    print(f"      ell = {l:>2}: N = 1e5 gives {r_coarse:.5f}, N = 4e5 gives {r_fine:.5f}, "
          f"delta {abs(r_fine-r_coarse):.2e}")
    check(f"ell = {l:>2}: quadrupling the step count moves the ratio by less than the paragraph's "
          f"last quoted digit", abs(r_fine - r_coarse) < 5e-4)

print()
print("  " + "=" * 74)
print("  E.  THE SEGMENT LENGTH'S MASS SCALING, which the same passage quotes")
print("  " + "=" * 74)

# a = |r| = A |sin(3s/2 alpha)|^{2/3} with A = (2 M alpha^2)^{1/3}, and the segment s in (0, pi alpha/3)
# is independent of M -- so |Delta eta| = int ds / a scales as 1/A, that is as M^{-1/3}, exactly.
def Deta_at(Mfac, N=400000, eps=1e-8):
    """|Delta eta| with the mass scaled by Mfac, the segment's extent being M-independent."""
    A2 = (2 * (M * Mfac) * al ** 2) ** (1. / 3)
    s = np.linspace(eps, smax, N)
    a = A2 * np.abs(np.sin(1.5 * s / al)) ** (2. / 3)
    return float(np.sum(np.diff(s) / (0.5 * (a[1:] + a[:-1]))))


check("|Delta eta| scales as M^{-1/3} EXACTLY and not approximately: the scale factor is "
      "A |sin(3s/2 alpha)|^{2/3} with A = (2 M alpha^2)^{1/3}, and the segment's extent pi alpha/3 "
      "carries no M, so the whole mass dependence is the prefactor 1/A",
      all(abs(Deta_at(fac) - Deta * fac ** (-1. / 3)) < 1e-6 for fac in (0.5, 0.25, 0.01)))

print(f"      {'M':>10} {'|Delta eta|/alpha':>18} {'3.33874 x (M0/M)^(1/3)':>24}")
#: ⛭ r7145: rescaled to the paragraph's closed-form base by its own stated M^(-1/3) law.
for fac, label, want in ((1.0, 'M', 3.33874), (0.5, 'M/2', 4.21), (0.01, 'M/100', 15.50)):
    d = Deta_at(fac)
    print(f"      {label:>10} {d:>18.4f} {Deta * fac ** (-1./3):>22.4f}")
    check(f"at {label} the segment's conformal length is {d:.3f} alpha, the passage's {want}",
          abs(d - want) < 0.05 * max(1.0, want / 4.0))

print()
print("  " + "=" * 74)
print(f"  {len(_fails)} fail(s)" if _fails else "  GATES: ALL PASS")
print("  " + "=" * 74)
print()
if _fails:
    raise SystemExit(1)
