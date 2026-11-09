#!/usr/bin/env python3
"""`r7721+cc66.2` READ the `(l, k)` separability measurement.

⛔ **WRITTEN BEFORE THE ARRAY WAS COMPLETE**, so the reading rule cannot have been chosen after seeing the
number.  `r7713` taught that the hard way: its first reading rule took the WEAKEST window and made three of
five registered table rows unreachable, and it was only caught by planting an effect.

Gate order is the REGISTERED order and is enforced in code, not by where the prints sit:
  0   the banked control                        (≤ 1e-12, the r7715 CI tolerance, same code path)
  1a  the dead set is a contiguous prefix       (amendment 1)
  1b  no zero above the common prefix           (amendment 1)
  1   the premise, AS A CONTROL and not a result
  2c  the grid change, AND the restriction's own free control
  2   how much of the kernel swap a source swap can mimic   ⚠ reported, NOT the verdict
  3   THE VERDICT: conditioning, under BOTH l readings
  4   the interpolation's own size

⛭ The three conditioning numbers are NOT independent: for column-normalised templates the condition
number is `sqrt((1+|r|)/(1-|r|))` and the VIF is `1/(1-r^2)`, both functions of `r` alone.  That is why
the registered threshold `|r| <= 0.70 AND VIF <= 2.0` is ONE statement and neither half can be met alone,
and this file prints all three so the reader can check that rather than take it on trust.
"""
import numpy as np

import separability as S

dense = S.dense
BANK = '../r7713_cc66_the_dense_ell_discriminant/pseudo/pseudo__S_lcdm__K_lcdm.npz'
rows = []


def gate(ok, name, detail):
    rows.append((bool(ok), name, detail))
    print(f"    [{'PASS' if ok else 'FAIL'}]  {name}\n             {detail}", flush=True)
    return bool(ok)


def cond_vif(x1, x2, w):
    """⛭ amendment 2: CONTRIBUTION-WEIGHTED correlation, condition number and VIF.

    The weight IS the integrand's own share of the collapse, so there is no threshold to tune, and a
    cell contributing nothing is down-weighted automatically rather than by a cut chosen by hand.  With
    a flat integrand this reduces exactly to the unweighted form the registration asked for."""
    w = w / w.sum()
    a = x1 - (w * x1).sum()
    b = x2 - (w * x2).sum()
    r = float((w * a * b).sum() / np.sqrt((w * a * a).sum() * (w * b * b).sum()))
    return r, float(np.sqrt((1 + abs(r)) / (1 - abs(r)))), float(1.0 / (1.0 - r * r))


def wfrac(X, w):
    """the weighted Frobenius fraction: the a(k)-only part of X, and the part no column rescaling gives"""
    w = w / w.sum()
    col = (w * X).sum(axis=0) / np.maximum(w.sum(axis=0), np.finfo(float).tiny)
    A = np.tile(col, (X.shape[0], 1))
    R = X - A
    nx = np.sqrt((w * X * X).sum())
    return float(np.sqrt((w * A * A).sum()) / nx), float(np.sqrt((w * R * R).sum()) / nx), R


def main():
    ks = S.kstar()
    ls = S.shared_ls()
    G = {t: S.g_full(t) for t in ('lcdm', 'cr')}
    z = np.load(BANK)
    bl, by = z['ls'], z['y']
    print(f"\n  ⛭ `r7721+cc66.2` the (l, k) separability measurement, read as registered\n"
          f"     shared l: {ls[0]}..{ls[-1]} ({len(ls)});  K* nodes: {len(ks)}\n")

    # ---- 0 -----------------------------------------------------------------
    sl, yb = dense.one_block('lcdm', 'lcdm', 0)
    j = np.searchsorted(bl, sl)
    r0 = float(np.abs(yb - by[j]).max() / np.abs(by[j]).max())
    if not gate(r0 <= S.TOL_CONTROL, 'control -- the banked combination through the banked code path',
                f"max relative departure {r0:.3e} against the registered {S.TOL_CONTROL:.0e}"):
        raise SystemExit("  ⛔ control failed; NOTHING downstream is computed")

    # ---- 1a / 1b -----------------------------------------------------------
    pref, contig, above = {}, True, 0
    for t in ('lcdm', 'cr'):
        dead = G[t] == 0
        p = dead.sum(axis=1)
        for i in range(len(ls)):                      # a prefix of length p[i] and nothing else
            if dead[i, :p[i]].sum() != p[i]:
                contig = False
        pref[t] = int(p.max())
    cut = max(pref.values())
    for t in ('lcdm', 'cr'):
        above += int((G[t][:, cut:] == 0).sum())
    gate(contig, 'amendment 1a -- the dead set is a contiguous low-k prefix at every l',
         f"largest prefix: lcdm {pref['lcdm']}, cr {pref['cr']} of {len(ks)} nodes")
    gate(above == 0, 'amendment 1b -- no zero above the common prefix',
         f"zeros above node {cut}: {above} (a nonzero count means the per-cell form is still undefined)")
    if not (contig and above == 0):
        raise SystemExit("  ⛔ the per-cell form is not computable; reporting that, not masking")
    ksr = ks[cut:]
    Gr = {t: G[t][:, cut:] for t in ('lcdm', 'cr')}
    print(f"\n    ⇒ common live support: nodes {cut}.. , k >= {ksr[0]:.4e}, "
          f"{len(ksr)} of {len(ks)} nodes\n", flush=True)

    # ---- 1 (the premise, as a control) -------------------------------------
    dk = np.gradient(ks)[cut:]
    s2 = {t: S.s2_on_kstar(t)[cut:] for t in ('lcdm', 'cr')}
    rho = s2['cr'] / s2['lcdm']
    # ⛔ computed in LOG space, because M itself underflows: the registered literal form
    #    (base*s2_cr)/(base*s2_lcdm) is 0/0 = nan on subnormal cells and the control would fail
    #    for a reason that has nothing to do with the premise.
    worst, bad = 0.0, 0
    for t in ('lcdm', 'cr'):
        base = 2.0 * np.log(np.abs(Gr[t])) + np.log(dk / ksr)
        d = (base + np.log(s2['cr'])) - (base + np.log(s2['lcdm']))
        bad += int((~np.isfinite(d)).sum())
        worst = max(worst, float(np.abs(d - np.log(rho)[None, :]).max()))
    gate(worst <= S.TOL_CONTROL and bad == 0,
         'the premise -- the source swap IS a column rescaling, A CONTROL AND NOT A RESULT',
         f"worst departure from log rho(k) over both kernels and every (l,k): {worst:.3e}; "
         f"non-finite cells: {bad}  ⌗ near-tautological by construction -- its real content is that "
         f"rho is independent of l AND of the kernel, and that no cell is non-finite")

    # ---- 2c ----------------------------------------------------------------
    M_lcdm = Gr['lcdm'] ** 2 * dk / ksr * s2['lcdm']
    yfull = np.sum(G['lcdm'] ** 2 * np.gradient(ks) / ks * S.s2_on_kstar('lcdm'), axis=1)
    yrest = np.sum(Gr['lcdm'] ** 2 * dk / ksr * s2['lcdm'], axis=1)
    jj = np.searchsorted(bl, ls)
    dfull = float(np.abs(yfull - by[jj]).max() / np.abs(by[jj]).max())
    drest = float(np.abs(yrest - by[jj]).max() / np.abs(by[jj]).max())
    gate(drest <= S.TOL_GRID, 'the grid change -- the collapse on K* reproduces the banked spectrum',
         f"max relative departure {drest:.4e} against the registered {S.TOL_GRID:.0e}")
    gate(abs(dfull - drest) <= 1e-14,
         "the restriction's own control -- dropping EXACT zeros cannot move the collapse",
         f"full K* {dfull:.6e} vs restricted {drest:.6e}; difference {abs(dfull - drest):.2e}")

    # ---- 2 -----------------------------------------------------------------
    # ⛔ amendment 2: 2 log|G|, NEVER log(G**2) -- G**2 underflows to 0 at |G| = 4e-323
    #    while 2 log|G| there is a finite -1484.7, so log(G**2) is -inf where the
    #    quantity it stands for is defined.
    lg = {t: 2.0 * np.log(np.abs(Gr[t])) for t in ('lcdm', 'cr')}
    d_ker = lg['cr'] - lg['lcdm']
    W = M_lcdm / M_lcdm.sum(axis=1, keepdims=True)      # amendment 2: each cell's own share
    f_mimic, f_sep, R = wfrac(d_ker, W)
    sv = np.linalg.svd(R, compute_uv=False)
    lead = float(sv[0] ** 2 / (sv ** 2).sum())
    n90 = int(np.searchsorted(np.cumsum(sv ** 2) / (sv ** 2).sum(), 0.90) + 1)
    print(f"    ⌗ REPORTED, NOT THE VERDICT -- a Frobenius fraction has no units of resolvability:\n"
          f"             f_mimic {f_mimic:.4f}  (the part a source swap could have produced)\n"
          f"             f_sep   {f_sep:.4f}  (the part it could not)\n"
          f"             leading singular component of R: {lead:.4f} of its norm; "
          f"{n90} component(s) hold 90%\n", flush=True)

    # ---- 3 -----------------------------------------------------------------
    t_src = np.tile(np.log(rho), (len(ls), 1))
    read = {}
    rA = cond_vif(d_ker.ravel(), t_src.ravel(), W.ravel())
    read['A (same integer l, NO interpolation)'] = rA
    qa = ls / dense.geom('lcdm')['l_A']
    qc = ls / dense.geom('cr')['l_A']
    m = (qa >= qc[0]) & (qa <= qc[-1])
    cr_on_qa = np.vstack([np.interp(qa[m], qc, Gr['cr'][:, i]) for i in range(len(ksr))]).T
    dB = 2.0 * np.log(np.abs(cr_on_qa)) - lg['lcdm'][m]
    rB = cond_vif(dB.ravel(), t_src[m].ravel(), W[m].ravel())
    read['B (common q, cr kernel interpolated)'] = rB
    print(f"    ⛭ THE VERDICT -- conditioning, against the collapsed route's "
          f"{S.D1_CORR} / {S.D1_COND} / {S.D1_VIF}x:", flush=True)
    passes = []
    for nm, (r, c, v) in read.items():
        ok = abs(r) <= S.CORR_MAX and v <= S.VIF_MAX
        passes.append(ok)
        print(f"             {nm:42s} corr {r:+.4f}   cond {c:.2f}   VIF {v:.2f}x   "
              f"=> {'MEETS' if ok else 'MISSES'} the registered threshold", flush=True)
    gate(all(passes) or not any(passes),
         'the two readings agree on the verdict (registered: a disagreement IS the verdict)',
         f"A {'meets' if passes[0] else 'misses'}, B {'meets' if passes[1] else 'misses'}")
    gate(all(passes), f'THE REGISTERED THRESHOLD -- |corr| <= {S.CORR_MAX} AND VIF <= {S.VIF_MAX}',
         'the (l,k) build BREAKS the degeneracy' if all(passes)
         else 'the (l,k) build does NOT break the degeneracy the collapse could not')

    # ---- 4 -----------------------------------------------------------------
    _, fsepB, _ = wfrac(dB, W[m])
    print(f"\n    ⌗ the interpolation's own size: f_sep {f_sep:.4f} (A) vs {fsepB:.4f} (B), "
          f"corr {rA[0]:+.4f} vs {rB[0]:+.4f}", flush=True)
    gate(abs(abs(rA[0]) - abs(rB[0])) < 0.5 * abs(abs(rA[0]) - S.CORR_MAX) or
         abs(abs(rA[0]) - S.CORR_MAX) < 1e-9,
         "the interpolation does not carry the verdict",
         f"it moves |corr| by {abs(abs(rA[0]) - abs(rB[0])):.4f} against a distance to the "
         f"threshold of {abs(abs(rA[0]) - S.CORR_MAX):.4f}")

    nf_ = sum(1 for ok, _, _ in rows if not ok)
    print(f"\n  {'OK' if nf_ == 0 else '⛔'}  {len(rows) - nf_} of {len(rows)} gates, {nf_} failure(s)\n")
    return 1 if nf_ else 0


if __name__ == '__main__':
    raise SystemExit(main())
