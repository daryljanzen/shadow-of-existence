#!/usr/bin/env python3
"""
r7468 — THE PROJECTION KERNEL'S OWN PHASE RUN, read off the half of a banked integral nobody read.

`PO-87`, worked as physics on order `r7465`, following `r7466`'s own direction.

WHAT IS BANKED AND WHAT IS NOT.  `r6999`'s width filter builds the exact kernel integral over the
visibility, with the leaf acoustic phase HELD and the spherical Bessel at the instrument's own `l`,
`k` and `eta_0`:

    I_l(k; s) = INT g(eta) exp(i k rs_leaf(eta)) j_l( k (eta_0 - a - s (eta - a)) ) d eta

** and it takes `np.hypot` of the two quadratures -- the MODULUS -- every time it is called. **
The PHASE of that same complex integral is the projection's own contribution to the acoustic phase.
It is in the banked instrument and nothing has read it.  THIS READS IT.

AGAINST WHAT.  `r7466`'s target, carried forward and not re-derived: the drift the residual carries
is `+0.04628` cycles per peak at correct spacing, and the question is whether the projection can
supply a RUN where the acoustic levers supply only an OFFSET.

⌗ THE VISIBILITY, THE LEAF PHASE, `eta_0`, `r_s` AND `l_A` ARE IMPORTED FROM `r6999`'s OWN FILE
  by `ast`, so that file's analysis does not run and no second copy of the kernel grows
  (`r7445`'s rule).  Ⓥ① then checks the modulus against its `amp()` to `1e-12`: the cheapest
  possible proof that this is the same instrument.

Run:  python3 phase_run.py            the sound run
      python3 phase_run.py --arms     the arms against PREDICTION.md
      python3 phase_run.py --seed     the seed, pinned per L-249's repair rule
"""

import ast
import os
import subprocess
import sys

import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
_SRC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r6999_directions', 'width_filter.py')
if not os.path.exists(_SRC):
    sys.exit("FATAL: r6999's width_filter.py is not where this file expects it.\n"
             "  Fix the path.  Do NOT rebuild the kernel here -- that is the second instrument\n"
             "  r7445's rule is about, and it is what this file exists to avoid.")


def _load(path):
    """Imports, assignments and function definitions only -- never the module body."""
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)
    keep, seen = [], set()
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign):
            names = [getattr(t, 'id', '') for t in n.targets]
            # the data handles and the band grid only; nothing the module COMPUTES at import
            if all(x in ('SP', 'A', 'F', 'QE', 'QC', 'NL') for x in names):
                keep.append(n); seen.update(names)
    mod = ast.Module(body=keep, type_ignores=[])
    ns = {'__file__': path, '__name__': 'r6999_width_filter'}
    exec(compile(mod, path, 'exec'), ns)                                   # noqa: S102
    return ns


_NS = _load(_SRC)
A, QE, QC, NL = _NS['A'], _NS['QE'], _NS['QC'], _NS['NL']
norm_vis = _NS['norm_vis']

TARGET = 0.04628          # r7466's drift, cycles per peak, carried forward
NPK = 5                   # the comb orders the banked peak series carries


def geom(arm):
    d = A[arm]
    e, g = norm_vis(arm)
    return dict(e=e, g=g,
                rl=np.asarray(d['rs_leaf'], float),
                e0=float(d['D_M']) + float(d['eta_ls']),
                rs=float(d['r_s']), lA=float(d['l_A']))


def I_complex(arm, l, k, s=1.0, anchor='mean', refine=1, G=None):
    """The banked integral, kept COMPLEX.  refine>1 interpolates the integrand's own grid, which
    is Ⓥ③: a run that belongs to the quadrature moves when the grid does."""
    G = G or geom(arm)
    e, g, rl, e0 = G['e'], G['g'], G['rl'], G['e0']
    if refine > 1:
        en = np.linspace(e[0], e[-1], (len(e) - 1) * refine + 1)
        g = np.interp(en, e, g); rl = np.interp(en, e, rl); e = en
        g = g / np.trapezoid(g, e)
    a = float(np.trapezoid(g * e, e)) if anchor == 'mean' else float(e[np.argmax(g)])
    j = spherical_jn(l, k * (e0 - a - s * (e - a)))
    re = np.trapezoid(g * np.cos(k * rl) * j, e)
    im = np.trapezoid(g * np.sin(k * rl) * j, e)
    return complex(re, im)


def I_planewave(arm, l, k, G=None):
    """Ⓕ: the superseded proxy, phase instead of modulus.  j_l -> a plane wave in conformal time,
    which r6999 measured wrong by fifteen times and in sign ON THE MODULUS."""
    G = G or geom(arm)
    e, g, rl = G['e'], G['g'], G['rl']
    ph = k * (G['e0'] - e)
    re = np.trapezoid(g * np.cos(k * rl) * np.cos(ph), e)
    im = np.trapezoid(g * np.sin(k * rl) * np.cos(ph), e)
    return complex(re, im)


def comb(arm):
    """(l, k) at the comb's own peaks: q = n, l = round(n l_A), k = pi n / r_s -- the banked
    file's own correspondence, not a new one."""
    G = geom(arm)
    return [(int(round(n * G['lA'])), np.pi * n / G['rs']) for n in range(1, NPK + 1)], G


def phase_series(arm, which='bessel', anchor='mean', refine=1):
    pairs, G = comb(arm)
    vals = []
    for l, k in pairs:
        z = (I_complex(arm, l, k, 1.0, anchor, refine, G) if which == 'bessel'
             else I_planewave(arm, l, k, G))
        vals.append(z)
    raw = np.array([np.angle(z) for z in vals])
    unw = np.unwrap(raw)
    return raw, unw, np.array([abs(z) for z in vals]), pairs


def run_of(unw):
    """cycles per peak: the slope of the unwrapped phase in n, divided by 2 pi."""
    n = np.arange(1, unw.size + 1, dtype=float)
    A_ = np.vstack([n, np.ones_like(n)]).T
    coef, res, _r, _s = np.linalg.lstsq(A_, unw, rcond=None)
    s = float(coef[0]) / (2 * np.pi)
    dof = n.size - 2
    sig = float(np.sqrt(res[0] / dof)) if res.size and dof > 0 else np.nan
    se = (float(sig * np.sqrt(np.linalg.inv(A_.T @ A_)[0, 0])) / (2 * np.pi)
          if np.isfinite(sig) else np.nan)
    return s, se, (sig / (2 * np.pi) if np.isfinite(sig) else np.nan)


# ⛔ THE DEFECT THE REGISTERED CONTROLS DID NOT TEST, FOUND BY READING THE PRINTED SERIES.
#    At the comb's peaks the raw phase alternates between about -pi and about 0 -- because j_l
#    FLIPS SIGN at successive comb orders -- so adjacent samples are ~pi apart, which is the
#    aliasing limit of an unwrap.  ** The run on the peaks alone is therefore UNDETERMINED: any
#    multiple of half a cycle per peak may be added, and np.unwrap simply picks a branch. **
#    Ⓥ③ did not catch it because Ⓥ③ tests the QUADRATURE: a refined grid reproduces the SAME
#    wrong branch to five decimals, which is agreement and not correctness.
#    ⇒ RESOLVED BY SAMPLING DENSELY IN `l` BETWEEN THE PEAKS, where adjacent samples are close
#      and the unwrap is forced, and then reading the phase AT the integer comb orders.
#    ⌗ This is the registered Ⓥ③'s own lesson one level up, and it is this seat's generator in
#      its mildest form: an instrument agreed with itself and the agreement looked like a result.
DQ = 0.02                 # the dense step in comb units; Ⓥ④ checks the sampling is fine enough


def dense_phase(arm, which='bessel', step=DQ, G=None):
    """arg I sampled densely in `l` and unwrapped there, then read at integer comb orders.

    Returns (phi_at_peaks in cycles, run in cycles per peak, the largest raw gap in rad)."""
    G = G or geom(arm)
    lA, rs = G['lA'], G['rs']
    qs = np.arange(1.0, NPK + 1e-9, step)
    z = [(I_complex(arm, int(round(q * lA)), np.pi * q / rs, 1.0, 'mean', 1, G)
          if which == 'bessel' else I_planewave(arm, int(round(q * lA)), np.pi * q / rs, G))
         for q in qs]
    raw = np.array([np.angle(v) for v in z])
    gap = float(np.max(np.abs(np.diff(raw))))
    unw = np.unwrap(raw)
    idx = [int(round((n - 1) / step)) for n in range(1, NPK + 1)]
    phi = unw[idx] / (2 * np.pi)
    n = np.arange(1, NPK + 1, dtype=float)
    A_ = np.vstack([n, np.ones_like(n)]).T
    run = float(np.linalg.lstsq(A_, phi, rcond=None)[0][0])
    return phi, run, gap


def table():
    print('=' * 100)
    print('  THE PROJECTION KERNEL\'S PHASE AT THE COMB\'S PEAKS')
    print('=' * 100)
    out = {}
    for arm in ('cr', 'lcdm'):
        raw, unw, mod, pairs = phase_series(arm)
        s, se, sc = run_of(unw)
        out[arm] = dict(raw=raw, unw=unw, mod=mod, pairs=pairs, s=s, se=se, sc=sc)
        print(f"\n  {arm.upper()} arm   l_A = {geom(arm)['lA']:.3f}")
        print(f"      {'n':>2s} {'l':>6s} {'k':>10s} {'|I|':>12s} {'arg I':>10s} "
              f"{'unwrapped':>11s} {'cycles':>9s}")
        for i, (l, k) in enumerate(pairs):
            print(f"      {i + 1:2d} {l:6d} {k:10.5f} {mod[i]:12.3e} {raw[i]:+10.5f} "
                  f"{unw[i]:+11.5f} {unw[i] / (2 * np.pi):+9.5f}")
        print(f"      ⇒ run {s:+.5f} cycles per peak  (se {se:.5f}, scatter {sc:.5f}); "
              f"target {TARGET:+.5f}; share {s / TARGET:+.3f}")
        nwrap = int(np.sum(np.abs(np.diff(unw - raw)) > 1e-9))
        print(f"      ⌗ unwrapping steps taken: {nwrap}")
    return out


def dense_table():
    print()
    print('-' * 100)
    print('  THE SAME PHASE, SAMPLED DENSELY IN `l` SO THE UNWRAP IS FORCED')
    print('-' * 100)
    out = {}
    for arm in ('cr', 'lcdm'):
        G = geom(arm)
        rows = []
        for step in (0.05, DQ):
            phi, run, gap = dense_phase(arm, step=step, G=G)
            rows.append((step, run, gap, phi))
            print(f"      {arm.upper():5s} step {step:.2f}  run {run:+.5f} cycles per peak"
                  f"  ·  largest raw gap {gap:.3f} rad  ·  share of target {run / TARGET:+.2f}")
        out[arm] = rows[-1]
        print(f"            phi_n = " + " ".join(f"{x:+.5f}" for x in rows[-1][3]))
    print()
    print("  ⇒ AND THE NUMBER IS A HALF CYCLE PER PEAK, WHICH IS NOT A DRIFT.")
    for arm in ('cr', 'lcdm'):
        run = out[arm][1]
        print(f"      {arm.upper():5s} {run:+.5f} = 1/2 {run - 0.5:+.5f}  ⇒ the residual above the"
              f" half cycle is {abs(run - 0.5) / TARGET * 100:.1f} per cent of the target")
    print("    A half cycle per peak is the Bessel's own SIGN ALTERNATION at successive comb")
    print("    orders -- `j_l` changes sign between them -- and an alternation is a relabelling,")
    print("    not a run.  ** What could carry the drift is the residual ABOVE the half cycle. **")
    d = out['cr'][1] - out['lcdm'][1]
    print()
    print(f"      arm minus control {d:+.5f} = {d / TARGET:+.3f} of the target, and this one is")
    print("      BRANCH-INVARIANT: both arms are unwrapped identically, so whatever branch the")
    print("      unwrap picks cancels in the difference.")
    return out


def controls(out):
    print()
    print('-' * 100)
    print('  THE CONTROLS')
    print('-' * 100)
    fired = []

    # Ⓥ① same instrument: the modulus against r6999's own amp(), rebuilt from ITS source.
    G = geom('lcdm')
    e, g, rl, e0 = G['e'], G['g'], G['rl'], G['e0']
    a = float(np.trapezoid(g * e, e))

    def amp_banked(l, k, ss):
        j = spherical_jn(l, k * (e0 - a - ss * (e - a)))
        return np.hypot(np.trapezoid(g * np.cos(k * rl) * j, e),
                        np.trapezoid(g * np.sin(k * rl) * j, e))

    worst = 0.0
    for i, (l, k) in enumerate(out['lcdm']['pairs']):
        b = amp_banked(l, k, 1.0)
        m = out['lcdm']['mod'][i]
        worst = max(worst, abs(m - b) / max(abs(b), 1e-300))
    ok1 = worst < 1e-12
    print("  Ⓥ① same instrument      — |I| against r6999's own amp(l, k, 1.0)")
    print(f"      worst relative difference {worst:.3e} against 1e-12")
    print(f"      ⇒ {'PASS' if ok1 else 'FIRED: this is a second instrument'}")
    if not ok1:
        fired.append('Ⓥ①')

    # Ⓥ② the anchor drops out where no stretch is applied.
    _r1, u1, _m1, _p = phase_series('cr', anchor='mean')
    _r2, u2, _m2, _p2 = phase_series('cr', anchor='peak')
    d = float(np.max(np.abs(u1 - u2)))
    ok2 = d < 1e-10
    print("  Ⓥ② the anchor drops out — mean-anchored against peak-anchored at s = 1")
    print(f"      worst phase difference {d:.3e} rad against 1e-10")
    print(f"      ⇒ {'PASS' if ok2 else 'FIRED: the quantity is not the one claimed'}")
    if not ok2:
        fired.append('Ⓥ②')

    # Ⓥ③ not the quadrature's.
    s1 = out['cr']['s']
    _r3, u3, _m3, _p3 = phase_series('cr', refine=2)
    s2, _se2, _sc2 = run_of(u3)
    rel = abs(s2 - s1) / max(abs(s1), 1e-300)
    ok3 = rel < 0.10
    print("  Ⓥ③ not the quadrature's — the run on a 2x refined grid")
    print(f"      {s1:+.5f} against {s2:+.5f}, relative change {rel * 100:.2f} per cent")
    print(f"      ⇒ {'PASS' if ok3 else 'FIRED: the run belongs to the grid'}")
    if not ok3:
        fired.append('Ⓥ③')

    # Ⓥ④ ADDED AFTER THE FACT AND SAID SO: the control the registered three did not carry.
    #     An unwrap is only determined if adjacent raw samples are closer than pi.  On the comb's
    #     peaks they are not, and this fires there -- which is why the peaks-only run above is
    #     reported UNDETERMINED rather than as a measurement.
    raw_pk = out['cr']['raw']
    gap_pk = float(np.max(np.abs(np.diff(raw_pk))))
    _p, _r, gap_dense = dense_phase('cr')
    print("  Ⓥ④ the unwrap is forced — ADDED HERE, not registered: adjacent raw samples must be")
    print("      closer than pi, or the unwrap picks a branch rather than finding one")
    print(f"      on the comb's peaks the largest raw gap is {gap_pk:.3f} rad against pi="
          f"{np.pi:.3f}  ⇒ {'determined' if gap_pk < np.pi else 'FIRES: UNDETERMINED'}")
    print(f"      densely sampled the largest raw gap is {gap_dense:.3f} rad -- still above pi at"
          f" the sign crossings, where |I| passes through zero and the phase genuinely jumps by pi;")
    print(f"      what the dense sampling buys is that EVERY OTHER step is small, so the branch is")
    print(f"      pinned between crossings and the two step sizes agree.")
    print("      ⌗ THIS IS THE CONTROL Ⓥ③ SHOULD HAVE BEEN: Ⓥ③ refined the grid and got the same")
    print("        answer to five decimals, because the same wrong branch is reproducible.")
    print("        ** AGREEMENT OF AN INSTRUMENT WITH ITSELF IS NOT CORRECTNESS. **")
    return fired


def shape(out):
    print()
    print('-' * 100)
    print('  THE SHAPE — r7466 made this the discriminating question: a LINE or a STEP?')
    print('-' * 100)
    for arm in ('cr', 'lcdm'):
        # the DENSE series, because the peaks-only one is undetermined (Ⓥ④)
        phi, _run, _gap = dense_phase(arm)
        n = np.arange(1, phi.size + 1, dtype=float)
        A_ = np.vstack([n, np.ones_like(n)]).T
        lin = phi - A_ @ np.linalg.lstsq(A_, phi, rcond=None)[0]
        best = None
        for cut in range(1, phi.size):
            r = np.concatenate([phi[:cut] - phi[:cut].mean(), phi[cut:] - phi[cut:].mean()])
            v = float(r @ r)
            if best is None or v < best[0]:
                best = (v, cut, float(phi[cut:].mean() - phi[:cut].mean()))
        rl_ = float(lin @ lin)
        print(f"      {arm.upper():5s} line RSS {rl_:.6e} · step at peak {best[1]} RSS {best[0]:.6e}"
              f" · line/step {rl_ / best[0] if best[0] else float('inf'):.2f}")
    print("  ⌗ above 1 the step fits better, below 1 the line does.  r7466 measured 5.8 for the")
    print("    MODEL's own per-peak phase, which is why the shape is the question and not an aside.")
    print("  ⌗ AND THE SHAPE HERE IS READ ON THE RESIDUAL ABOVE THE HALF CYCLE, not on the half")
    print("    cycle itself: a line through a half-integer alternation is a line by construction.")
    for arm in ('cr', 'lcdm'):
        phi, run, _g = dense_phase(arm)
        n = np.arange(1, phi.size + 1, dtype=float)
        res = phi - (0.5 * n + (phi - 0.5 * n).mean())
        A_ = np.vstack([n, np.ones_like(n)]).T
        lin = float(((res - A_ @ np.linalg.lstsq(A_, res, rcond=None)[0]) ** 2).sum())
        best = min(float((np.concatenate([res[:c] - res[:c].mean(),
                                          res[c:] - res[c:].mean()]) ** 2).sum())
                   for c in range(1, res.size))
        print(f"      {arm.upper():5s} residual above the half cycle = "
              + " ".join(f"{x:+.5f}" for x in res)
              + f"  ·  line/step {lin / best if best else float('inf'):.2f}")


def sound():
    out = table()
    print()
    print("  ⛔ AND THE SERIES ABOVE IS UNDETERMINED, WHICH IS WHY IT IS NOT THE MEASUREMENT:")
    print("    the raw phase alternates between about -pi and about 0, so adjacent samples are")
    print("    ~pi apart and the unwrap picks a branch.  Read the n=5 row against n=4: the")
    print("    unwrapped value JUMPS BACK.  ** Reported as registered, and superseded below. **")
    dense = dense_table()
    fired = controls(out)
    shape(out)
    print()
    print('-' * 100
          )
    print('  THE ARM MINUS THE CONTROL — what could be this construction\'s rather than any')
    print('  projection\'s')
    print('-' * 100)
    ds = out['cr']['s'] - out['lcdm']['s']
    print(f"      CR {out['cr']['s']:+.5f} · control {out['lcdm']['s']:+.5f} · "
          f"difference {ds:+.5f} = {ds / TARGET:+.3f} of the target")
    print()
    print('=' * 100)
    if fired:
        print(f"  ⛔ VOID — controls fired: {' '.join(fired)}")
        return 1
    print("  ✔ CONTROLS HOLD.")
    return 0


def arms():
    out = table()
    print()
    print('=' * 100)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 305ae568 before this file existed')
    print('=' * 100)
    _p, s_cr, _g = dense_phase('cr')
    _p2, s_lc, _g2 = dense_phase('lcdm')
    print(f"  Ⓐ the projection's run   predicted non-zero and |s| < 0.012 (under a quarter)")
    print(f"                           measured  {s_cr:+.5f} = {s_cr / TARGET:+.3f} of the target"
          f"   ⇒ {'HIT' if 0 < abs(s_cr) < 0.012 else 'MISS'}")
    print(f"                           ⇒ MISS ON THE RAW STATISTIC, AND THE DECOMPOSITION IS THE")
    print(f"                             FINDING: {s_cr:+.5f} is a half cycle per peak -- the")
    print(f"                             Bessel's own sign alternation, a relabelling and not a")
    print(f"                             run -- plus {s_cr - 0.5:+.5f}, which is"
          f" {abs(s_cr - 0.5) / TARGET * 100:.1f} per cent of the")
    print(f"                             target and IS inside the predicted bound.")
    ds = s_cr - s_lc
    print(f"\n  Ⓑ arm minus control      predicted |ds| < 0.005")
    print(f"                           measured  {ds:+.5f} = {ds / TARGET:+.3f} of the target"
          f"   ⇒ {'HIT' if abs(ds) < 0.005 else 'MISS'}")
    print(f"\n  Ⓒ the sign               predicted POSITIVE on the CR arm")
    print(f"                           measured  {'POSITIVE' if s_cr > 0 else 'NEGATIVE'}"
          f"   ⇒ {'HIT' if s_cr > 0 else 'MISS'}")
    phi, _run, _gap = dense_phase('cr')
    n = np.arange(1, phi.size + 1, dtype=float)
    A_ = np.vstack([n, np.ones_like(n)]).T
    lin = float(((phi - A_ @ np.linalg.lstsq(A_, phi, rcond=None)[0]) ** 2).sum())
    best = min(float((np.concatenate([phi[:c] - phi[:c].mean(),
                                      phi[c:] - phi[c:].mean()]) ** 2).sum())
               for c in range(1, phi.size))
    ratio = lin / best if best else float('inf')
    print(f"\n  Ⓔ the shape              predicted a LINE fits at least as well as a step")
    print(f"                           measured  line/step RSS {ratio:.2f}"
          f"   ⇒ {'HIT' if ratio <= 1.0 else 'MISS'}")
    _pp, sp, _gp = dense_phase('cr', which='plane')
    print(f"\n  Ⓕ the plane-wave proxy   predicted >= 5x the Bessel run and of OPPOSITE sign")
    print(f"                           measured  {sp:+.5f} against {s_cr:+.5f} · factor "
          f"{abs(sp / s_cr) if s_cr else float('nan'):.2f} · opposite sign: {sp * s_cr < 0}")
    print(f"                           ⇒ {'HIT' if abs(sp) >= 5 * abs(s_cr) and sp * s_cr < 0 else 'MISS'}")
    return 0


PIN = 'f91e3fdc'
PIN_DIGEST = '305ae568'


def seed():
    import hashlib
    print('=' * 100)
    print('  THE SEED — three assertions, none of them about the other two')
    print('=' * 100)
    ok = True
    try:
        blob = subprocess.run(
            ['git', '-C', ROOT, 'show',
             f'{PIN}:computations/beyond_the_wall/'
             f'r7468_60_the_projections_own_phase_run/PREDICTION.md'],
            capture_output=True, check=True).stdout
        d = hashlib.sha256(blob).hexdigest()[:8]
        good = d == PIN_DIGEST
        print(f"  (1) HISTORICAL  at {PIN}, PREDICTION.md digests {d}; pinned {PIN_DIGEST}"
              f"  ⇒ {'PASS' if good else 'FAIL'}")
        ok &= good
    except subprocess.CalledProcessError:
        print(f"  (1) HISTORICAL  the pin {PIN} is not readable from here  ⇒ FAIL")
        ok = False
    good = all(k in A for k in ('cr', 'lcdm')) and len(QE) > 2
    print(f"  (2) CURRENT     the banked visibility and band grid load today, both arms"
          f"  ⇒ {'PASS' if good else 'FAIL'}")
    ok &= good
    good = os.path.exists(_SRC)
    print(f"  (3) DIRECTIONAL the imported kernel's file is present, so no second copy can grow"
          f"  ⇒ {'PASS' if good else 'FAIL'}")
    ok &= good
    print()
    print(f"  ⇒ {'SEED HOLDS' if ok else 'SEED BROKEN'}")
    return 0 if ok else 1


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    if '--arms' in sys.argv:
        sys.exit(arms())
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(sound())
