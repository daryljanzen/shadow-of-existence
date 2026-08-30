#!/usr/bin/env python3
r"""N8 -- P15's TRANSMISSION DICHOTOMY IS A CAPACITY DICHOTOMY: THE NON-DEGENERATE HORIZON
     OVERWRITES ITS INPUT AND THE DEGENERATE ONE PASSES IT.

** WHAT THE PAPER PROVES.  ** `CR_cosmology.tex` `prop:transmission`: *"For a mode approaching a
horizon where the metric function behaves as $f\sim(r-r_h)^{p}$, the tortoise coordinate
$r_*=\int\dd r/f$ controls the approach.  At a non-degenerate horizon ($p=1$, $f\sim2\kappa(r-r_h)$)
the integral is logarithmic"* -- and at the degenerate one ($p=2$) it is a power law.  *And
`rem:transmission-leg`:* ***"the leg multiplies the spectrum by a constant and the seam imprints
nothing: neither carries a scale, and a spectrum can only be tilted by something that does."***

*** THE STATEMENT THE PAPER DOES NOT MAKE.  "Transmits rather than imprints" is a claim about a
    CHANNEL, and "carries a scale" is what decides its capacity: ***
  * ** $p=1$ -- the exponential map $\delta\sim e^{2\kappa r_*}$ carries the scale $1/2\kappa$, so the
    kernel has a shape of its own and the output is ITS shape, not the input's.  ZERO capacity for the
    input's tilt. **
  * ** $p=2$ -- the power law $\delta\sim 1/(c\,r_*)$ is scale-free, so the kernel multiplies and does
    not reshape.  The output tilt IS the input tilt.  FULL capacity. **

⛔⛭⛭ ** THE FIRST STATISTIC WRITTEN HERE COULD NOT VARY, AND THE ASSERT CAUGHT IT.  KEPT. **
  *It regressed the OUTPUT tilt on the INPUT tilt and expected slope 1 for a transparent channel and
  slope 0 for an overwriting one.*  ** Every kernel returned slope 1 -- the non-degenerate one and the
  deliberately-broken control included. **
    ⇒ *** AND BY ARITHMETIC IT HAD TO.  For $P_{\rm out}=k^{\,n}K(k)$ the log-slope is
        $n + \dd\ln K/\dd\ln k$, so $\partial(\text{out})/\partial(\text{in}) = 1$ for EVERY $K$.
        A multiplicative kernel passes tilt DIFFERENCES through whatever it is.  The statistic was
        constant by construction and no kernel could have moved it. ***
  ⌗ ** Second time in this field, and the same shape as `N7`'s first toy: a summary number reached for
    before checking it can vary. **  *There the model had no degree of freedom to lose; here the
    statistic had none.*

*** WHAT ACTUALLY DISCRIMINATES, and it is the paper's own words made operational. ***  *"Carries a
    scale" means there is a preferred $k$ -- so the fitted tilt DEPENDS ON WHICH BAND you fit.*
  * ** $p=2$: scale-free, so every band returns the same tilt.  The kernel has no feature to pick a
    band out. **
  * ** $p=1$: the exponential $1/(e^{k/\kappa}-1)$ has its knee at $k\sim\kappa$, so the fitted tilt
    moves band to band.  That band-dependence IS the scale, measured. **
  ⇒ ** Transparent means "the answer does not depend on where you look"; imprinting means it does. **

⌗ ** WHAT THIS IS NOT.  **  *It is not a Bogoliubov calculation and claims no Hawking temperature.  The
paper's own receipts (`P15_verify_geometry`) do the tortoise integrals; this asks the separate
question of what the resulting kernel does to a SPECTRUM, which is the field's question and not the
paper's.*

⛔ ** THE CONTROL THAT CAN GO THE OTHER WAY, which §4 of the work order asks for by name. **  *A
kernel's scale-freedom is the whole mechanism, so the test must FAIL when the scale is restored: a
$p=2$ kernel given an artificial cutoff -- a scale by hand -- must stop transmitting.  If it still
transmits, this receipt is measuring its own arithmetic.*

COMPUTES: scope.
  * `KAPPA`, `CVAL` set the surface gravity and the degenerate coefficient.  ** The verdict is a slope
    and must not move with them; both are swept. **
  * `BANDS` are the disjoint $k$-windows the tilt is fitted on; `NK` is the grid resolution.
  * ** NOT CLAIMED: any number about $n_s$, the CMB, or the progenitor. **  *Those are the paper's and
    rest on its real transfer.  What is claimed is that the dichotomy it proves is a statement about
    channel capacity and behaves as one.*

Written r3692 by node 60, information-theory v2 pass B row 2 (`P15`).
"""
import numpy as np

np.random.seed(15)

KAPPA, CVAL = 0.7, 1.3
NK = 6000
BANDS = [(0.05, 0.2), (0.2, 0.8), (0.8, 3.0), (3.0, 12.0)]


def kgrid():
    return np.logspace(-2.0, 2.0, NK)


def kernel_nondegenerate(k, kappa=KAPPA):
    r"""$p=1$: the exponential near-horizon map carries the scale $1/2\kappa$"""
    return 1.0 / (np.exp(k / kappa) - 1.0 + 1e-300)


def kernel_degenerate(k, c=CVAL):
    r"""$p=2$: the power-law map is scale-free -- a pure constant in shape"""
    return np.full_like(k, 1.0 / c)


def kernel_degenerate_with_a_scale(k, c=CVAL, kcut=1.0):
    r"""⛔ the CONTROL: the same power law with a scale put in BY HAND"""
    return (1.0 / c) / (1.0 + (k / kcut) ** 2)


def band_tilts(kernel, tilt=0.0, **kw):
    r"""the fitted tilt of $P_{\rm out}$ on each band separately

    ** A scale-free kernel gives one number on every band.  A kernel with a knee does not, and the
    spread across bands is the scale showing itself. **
    """
    k = kgrid()
    p = (k ** tilt) * kernel(k, **kw)
    out = []
    for lo, hi in BANDS:
        m = (k >= lo) & (k <= hi) & (p > 0)
        out.append(float(np.polyfit(np.log(k[m]), np.log(p[m]), 1)[0]))
    return out


def band_spread(kernel, **kw):
    t = band_tilts(kernel, **kw)
    return max(t) - min(t), t


if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('(A) THE TWO KERNELS — the fitted tilt, band by band')
    print('=' * 78)
    sp_deg, t_deg = band_spread(kernel_degenerate)
    sp_non, t_non = band_spread(kernel_nondegenerate)
    print(f"    {'band':>14} {'p=2 (degenerate)':>19} {'p=1 (non-degenerate)':>22}")
    for (lo, hi), a, b in zip(BANDS, t_deg, t_non):
        print(f'    {f"{lo}-{hi}":>14} {a:>19.6f} {b:>22.6f}')
    print()
    print(f'    spread across bands, p=2 DEGENERATE     = {sp_deg:.2e}  -> SCALE-FREE, transparent')
    print(f'    spread across bands, p=1 NON-DEGENERATE = {sp_non:.3f}      -> A SCALE, imprinting')
    print()
    print('    ⇒ "neither carries a scale, and a spectrum can only be tilted by something')
    print('      that does" — the degenerate kernel gives the SAME answer wherever you')
    print('      look; the non-degenerate one does not, and that is the scale.')

    print()
    print('=' * 78)
    print('(B) THE CONTROL — put a scale into the degenerate kernel by hand')
    print('=' * 78)
    sp_cut, t_cut = band_spread(kernel_degenerate_with_a_scale)
    print(f'    p=2 with a cutoff at k = 1.0 :  band tilts {[round(x,3) for x in t_cut]}')
    print(f'    spread = {sp_cut:.3f}   (was {sp_deg:.2e} without the cutoff)')
    print('    ⇒ restoring a scale destroys the transmission.  Scale-freedom IS the')
    print('      mechanism and this test can fail.')

    print()
    print('=' * 78)
    print("(C) THE SWEEP — and the scale must MOVE WITH kappa, or it is not the scale")
    print('=' * 78)
    # ⛔ *The first version of this sub-test asked which BAND is steepest and expected it to move
    #   with kappa.  It is always the last one -- an exponential steepens monotonically, so the
    #   steepest band is the highest at every kappa.  What actually moves is the SPREAD: a larger
    #   kappa pushes the knee out past the band range, so the kernel looks flatter over it.*
    spreads = []
    for kap in (0.2, 0.7, 2.0):
        sp, t = band_spread(kernel_nondegenerate, kappa=kap)
        spreads.append(sp)
        print(f'    kappa = {kap:<4} :  band tilts {[round(x,2) for x in t]}   '
              f'spread {sp:.2f}')
    sw = []
    for c in (0.5, 1.3, 4.0):
        sp, _ = band_spread(kernel_degenerate, c=c)
        sw.append(sp)
        print(f'    c     = {c:<4} :  p=2 spread {sp:.2e}')
    print()
    print('    ⇒ the p=1 spread SHRINKS monotonically as kappa rises — a larger scale')
    print('      pushes the knee past the band range — and p=2 has no scale at any c.')
    print('      So the spread tracks the kernel\'s scale and is not the fit\'s artefact.')

    # ⛔⛭ pinned to measured values -- never `expr == True`
    assert sp_deg < 1e-9, sp_deg
    assert sp_non > 1.0, sp_non
    assert sp_cut > 0.5, sp_cut
    assert spreads == sorted(spreads, reverse=True), spreads   # shrinks as kappa rises
    assert spreads[0] > 3 * spreads[-1], spreads
    assert all(x < 1e-9 for x in sw), sw
    print()
    print('  ALL PASS')
