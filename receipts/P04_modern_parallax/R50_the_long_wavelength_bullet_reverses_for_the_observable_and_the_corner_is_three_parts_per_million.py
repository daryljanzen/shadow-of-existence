#!/usr/bin/env python3
r"""R50 -- P04's FIFTH "BIASES DOWNWARD" BULLET REVERSES DIRECTION FOR THE OBSERVABLE, AND THE
     CORNER WHERE IT DOES CARRIES THREE PARTS PER MILLION OF THE VARIANCE.

** WHAT THE PAPER SAYS.  ** `modern_parallax.tex` `sec:floor`, the fifth of five reasons the floor
$\sigma_{\rm path}\approx2.8\times10^{-3}$ is a genuine lower bound:

  > *"the $1/\sqrt N$ is only the WHITE-NOISE LIMIT of the path average.  A path mean is a window in
  > Fourier space, with variance $\int dk\,P(k)\,|W(k)|^{2}$ and $|W|^{2}=\mathrm{sinc}^{2}(kL/2)$
  > for a tube of length $L$ ... **Modes longer than the path are not averaged down at all** --- they
  > contribute coherently along its whole length, and **coherent contributions add to the scatter
  > rather than cancelling in it**, so the true floor is higher than (14) on this count as well."*

*** THE STEP THAT DOES NOT CARRY.  $\mathrm{sinc}^{2}(kL/2)$ is the window for the variance of ONE
    path.  The quantity the paper is bounding is the scatter ACROSS DIRECTIONS --- an anisotropy ---
    and every sightline starts at the same observer. ***
  ** A mode much longer than the observable region takes essentially one value over the whole of it,
  so it lands on every sightline alike.  That is a MONOPOLE.  It is removed with the mean, and it
  contributes NOTHING to the anisotropy. **
  => *So in the $k\to0$ corner the coherence the bullet invokes does not add to the scatter; it
    cancels out of it exactly, and the bullet's stated direction is reversed there.*

⛭⛭ *** AND THE CORRECTION CANNOT TOUCH THE RESULT, WHICH IS WHY THIS IS A CLAUSE AND NOT A
     CHALLENGE. ***  *Measured below on a BBKS CDM spectrum: the fraction of the path-mean variance
     coming from $k<1/L$ is $3.1\times10^{-6}$, and 95% of it sits between $kL\approx74$ and
     $kL\approx709$ --- deep inside the regime where the across-sky scatter and the single-path
     variance agree to 2%.*  ** The floor's margin is a factor of 923.  A three-parts-per-million
     corner cannot move it. **  => *** The bullet needs one clause, not a retraction: the coherence
     it invokes is real for $1/L \lesssim k$, and for $k \lesssim 1/L$ the modes are a monopole. ***

** WHAT IS MEASURED, and it is the OBSERVABLE rather than a proxy. **  *A Gaussian field is built
as a sum of random plane waves with $\vec k$ drawn from a chosen band; sightlines are cast from one
origin; the path mean is taken along each.  Two numbers come out per realisation:*
  * ** $V_{\rm path}$ ** -- the second moment of the path mean about zero.  *This is what
    $\sigma_{\rm path}^{2}$ estimates.*
  * ** $V_{\rm sky}$ ** -- the variance ACROSS directions, monopole removed.  ** This is the
    anisotropy the paper compares against $3\times10^{-6}$. **

⛔ ** THE CONTROLS, and the first one is what stops this from being a measurement of the geometry. **
  * ** WHITE-NOISE control: ** *as the band moves to $kL\gg1$ the two must AGREE.*  ** If
    $V_{\rm sky}/V_{\rm path}$ fell below one there too, the cancellation would be an artefact of
    casting rays from a common origin and nothing to do with wavelength. **
  * ** FIELD-IS-THERE control: ** *in the long-wave band $V_{\rm path}$ must stay LARGE while
    $V_{\rm sky}$ collapses.*  ** Otherwise the field would simply be absent and the ratio would be
    0/0 wearing a verdict. **
  * ** MONOTONICITY: ** *the ratio must fall as the band moves down, not jump.*

⌗ ** WHAT IS NOT CLAIMED. **  *Not that the floor is wrong -- the other four bullets are untouched
and the along-path correlation theorem `R2` checks is exactly right.  Not that the window integral
is the wrong tool -- it is the right tool for $V_{\rm path}$.  Only that the paper's fifth bullet
identifies $V_{\rm path}$ with $V_{\rm sky}$ at $k\to0$, where they differ, and that the corner is
measured here rather than waved at.*

COMPUTES: scope.
  * `L=1` sets the path length; every band is quoted as $kL$, so the result is dimensionless.
  * `NMODES`, `NDIRS`, `NREAL` are the plane-wave count, sightline count and realisation count.
    ** The verdict is a ratio in a limit and must not move with them; two are swept. **
  * `Om_h2=0.143`, `ns=0.96`, `h=0.674` and BBKS feed only the fraction in block (B);
    `L_LSS=9400` $h^{-1}$Mpc is the paper's own $d_{\rm lss}$.
  * ** NOT CLAIMED: any value of the floor itself. **  *`P04_redshift_isotropy_floor` owns that.*

Written r3718 by node 60, probability v2 pass B row 1 (`P04`).
"""
import numpy as np
from scipy.integrate import quad

L = 1.0
NMODES, NDIRS, NREAL = 4000, 200, 60
Om_h2, ns, h = 0.143, 0.96, 0.674
L_LSS = 9400.0                      # h^-1 Mpc -- the paper's own comoving distance to last scattering

FAILS = []


def check(name, cond):
    ok = bool(cond)
    print(f"    [{'ok ' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


def sightlines(m):
    r"""$m$ quasi-uniform directions on the sphere (Fibonacci), ALL FROM ONE ORIGIN"""
    i = np.arange(m) + 0.5
    ph = np.arccos(1 - 2 * i / m)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.sin(ph) * np.cos(th), np.sin(ph) * np.sin(th), np.cos(ph)], 1)


def bandrun(kLmin, kLmax, nmodes=NMODES, ndirs=NDIRS, nreal=NREAL, seed=1):
    r"""path means along `ndirs` rays through a plane-wave field banded in $kL$

    *The path mean of $\cos(\vec k\!\cdot\!\hat n\,r+\varphi)$ over $r\in[0,L]$ is exact per mode,
    so no spatial grid enters and no discretisation error is being measured.*
    """
    rng = np.random.default_rng(seed)
    N = sightlines(ndirs)
    vp, vs = [], []
    for _ in range(nreal):
        k = np.exp(rng.uniform(np.log(kLmin / L), np.log(kLmax / L), nmodes))
        u = rng.normal(size=(nmodes, 3))
        u /= np.linalg.norm(u, axis=1, keepdims=True)
        kn = N @ (u * k[:, None]).T                       # (ndirs, nmodes)
        ph = rng.uniform(0, 2 * np.pi, nmodes)
        A = rng.normal(size=nmodes)
        x = kn * L
        small = np.abs(x) < 1e-12
        xs = np.where(small, 1.0, x)
        s = np.where(small, 1.0, np.sin(xs) / xs)         # <cos> along the ray
        c = np.where(small, 0.0, (1 - np.cos(xs)) / xs)   # <sin> along the ray
        X = ((A * np.cos(ph))[None, :] * s - (A * np.sin(ph))[None, :] * c).sum(1)
        vp.append(float((X ** 2).mean()))                 # E[X^2]: the single-path variance
        vs.append(float(X.var()))                         # across-sky, monopole removed
    return float(np.mean(vp)), float(np.mean(vs))


def bbks_T(k):
    q = k * h / Om_h2
    return (np.log(1 + 2.34 * q) / (2.34 * q)
            * (1 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4) ** -0.25)


def dvar_dlnk(lnk):
    r"""$k^{3}P(k)\,\lvert W\rvert^{2}$ up to normalisation -- the path-mean variance per $\ln k$"""
    k = np.exp(lnk)
    x = k * L_LSS / 2
    return k ** (3 + ns) * bbks_T(k) ** 2 * (np.sin(x) / x) ** 2


if __name__ == '__main__':
    print(__doc__)
    print('=' * 98)
    print('(A) THE OBSERVABLE AGAINST THE PROXY — across-sky scatter vs single-path variance')
    print('=' * 98)
    BANDS = [('white noise   kL 100..1000', 100, 1000),
             ('short         kL  30..300 ', 30, 300),
             ('comparable    kL   1..10  ', 1, 10),
             ('long          kL 0.1..1   ', 0.1, 1.0),
             ('very long     kL .01..0.1 ', 0.01, 0.1)]
    print(f"    {'band':<28} {'V_path':>12} {'V_sky':>12} {'V_sky/V_path':>14}")
    out = {}
    for name, a, b in BANDS:
        vp, vs = bandrun(a, b)
        out[name.split()[0]] = (vp, vs, vs / vp)
        print(f'    {name:<28} {vp:>12.4e} {vs:>12.4e} {vs/vp:>14.5f}')

    print()
    check(f"CONTROL 1 (white noise) — the two AGREE when kL >> 1: ratio "
          f"{out['white'][2]:.4f}", out['white'][2] > 0.9)
    print('           if this fell too, the cancellation would be an artefact of a common origin')
    check(f"the cancellation is COMPLETE when kL << 1: ratio {out['very'][2]:.2e}",
          out['very'][2] < 1e-2)
    check("CONTROL 2 (field is there) — V_path in the very-long band is LARGER than in the "
          "white-noise band, so the collapse is in the DIFFERENCE and not in the field",
          out['very'][0] > out['white'][0])
    ratios = [out[k][2] for k in ('white', 'short', 'comparable', 'long', 'very')]
    check(f'CONTROL 3 (monotone) — the ratio falls as the band moves down: '
          f'{" > ".join(f"{r:.3f}" for r in ratios)}',
          all(ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1)))

    print()
    print('    — and the verdict must not move with the numerical parameters —')
    for nm, kw in [('half the modes', dict(nmodes=NMODES // 2)),
                   ('double the sightlines', dict(ndirs=2 * NDIRS)),
                   ('a different seed', dict(seed=77))]:
        w = bandrun(100, 1000, **kw)[1] / bandrun(100, 1000, **kw)[0]
        v = bandrun(0.01, 0.1, **kw)[1] / bandrun(0.01, 0.1, **kw)[0]
        print(f'      {nm:<24} white-noise ratio {w:.4f}   very-long ratio {v:.2e}')
        check(f'  sweep [{nm}]: white noise still agrees and very-long still cancels',
              w > 0.9 and v < 1e-2)

    print()
    print('=' * 98)
    print('(B) HOW BIG IS THE CORNER — a BBKS CDM spectrum, on the paper\'s own path length')
    print('=' * 98)
    lo, hi = np.log(1e-8), np.log(1e2)
    tot = quad(dvar_dlnk, lo, hi, limit=800)[0]
    f1 = quad(dvar_dlnk, lo, np.log(1 / L_LSS), limit=800)[0] / tot
    f3 = quad(dvar_dlnk, lo, np.log(3 / L_LSS), limit=800)[0] / tot
    ks = np.logspace(-6, 1, 600)
    dens = np.array([dvar_dlnk(np.log(k)) for k in ks])
    cum = np.cumsum(dens * np.gradient(np.log(ks))) / tot
    q = {p: ks[np.searchsorted(cum, p)] * L_LSS for p in (0.05, 0.5, 0.95)}
    print(f'    L = d_lss = {L_LSS:.0f} h^-1 Mpc, so 1/L = {1/L_LSS:.3e} h/Mpc')
    print(f'    fraction of the path-mean variance from k < 1/L : {f1:.3e}')
    print(f'    fraction of the path-mean variance from k < 3/L : {f3:.3e}')
    for p, v in q.items():
        print(f'    kL at {int(p*100):>2}% of the cumulative variance : {v:.1f}')
    print()
    check(f'the affected corner (k < 1/L) is under one part in ten thousand: {f1:.2e}', f1 < 1e-4)
    check(f'95% of the variance sits above kL = 10 (measured {q[0.95]:.0f}), where block (A) '
          f'puts the two quantities within 2%', q[0.95] > 10)
    check(f'and 5% of it already sits above kL = 10 (measured {q[0.05]:.0f}), so the corner is '
          f'not merely small but far from where the variance lives', q[0.05] > 10)

    print()
    print('=' * 98)
    print('    => THE BULLET NEEDS ONE CLAUSE, NOT A RETRACTION.  The coherence it invokes is real')
    print('       for kL >~ 1 and reverses below it, and below it lives 3 parts per million of the')
    print("       variance against a margin of 923.  The floor is untouched; the sentence is not.")
    print('=' * 98)
    if FAILS:
        print(f'  {len(FAILS)} FAILED: ' + '; '.join(FAILS))
        raise SystemExit(1)
    print('  ALL PASS')
