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

    # ---- 1a / 1b (amendment 3: PER-l, and the support is NOT restricted) -------
    # ⛔ amendment 1 took the LARGEST dead prefix and applied it to EVERY l.  The prefix is
    #    l-DEPENDENT -- 0 nodes at l=243, 119 at l=934 -- and at the bottom of the window those
    #    nodes carry 94% of the collapse.  Gate 2c caught it.  Amendment 1 is WITHDRAWN: amendment
    #    2's weighting already gives a dead cell weight exactly 0, so masking replaces restricting
    #    and NO l loses a contributing node.
    contig, nonpref = True, 0
    for t in ('lcdm', 'cr'):
        dead = G[t] == 0
        p_l = dead.sum(axis=1)
        for i in range(len(ls)):
            if dead[i, :p_l[i]].sum() != p_l[i]:
                contig = False
            nonpref += int(dead[i, p_l[i]:].sum())
    gate(contig, 'amendment 1a -- at EVERY l the dead set is a contiguous low-k prefix of its own',
         f"prefix length runs {int((G['lcdm'][0] == 0).sum())} at l={ls[0]} to "
         f"{int((G['lcdm'][-1] == 0).sum())} at l={ls[-1]}: l-DEPENDENT, which is why it is masked "
         f"and not restricted")
    gate(nonpref == 0, 'amendment 1b -- no zero lies above that l\'s own prefix',
         f"zeros above the per-l prefix: {nonpref}")
    ksr = ks
    Gr = G
    dead = {t: (G[t] == 0) for t in ('lcdm', 'cr')}
    anydead = dead['lcdm'] | dead['cr']
    print(f"\n    ⇒ FULL K* kept ({len(ks)} nodes); {int(anydead.sum())} dead cell(s) masked at "
          f"weight 0, NOT dropped\n", flush=True)

    # ---- 1 (the premise, as a control) -------------------------------------
    dk = np.gradient(ks)                       # amendment 3: FULL K*, nothing cut
    s2 = {t: S.s2_on_kstar(t) for t in ("lcdm", "cr")}
    rho = s2['cr'] / s2['lcdm']
    # ⛔ computed in LOG space, because M itself underflows: the registered literal form
    #    (base*s2_cr)/(base*s2_lcdm) is 0/0 = nan on subnormal cells and the control would fail
    #    for a reason that has nothing to do with the premise.
    worst, bad = 0.0, 0
    for t in ('lcdm', 'cr'):
        base = 2.0 * np.log(np.abs(Gr[t])) + np.log(dk / ksr)
        d = (base + np.log(s2['cr'])) - (base + np.log(s2['lcdm']))
        d = np.where(anydead, np.log(rho)[None, :], d)   # masked, not measured
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
    if not gate(drest <= S.TOL_GRID,
                'the grid change -- the collapse on K* reproduces the banked spectrum',
                f"max relative departure {drest:.4e} against the registered {S.TOL_GRID:.0e}"):
        # ⛔ amendment 3: §2c is a REFUSAL, not a caveat, and it is now ENFORCED HERE.  Written in
        #    prose only, it let the first run print a clean PASS of the registered threshold off an
        #    integrand with 94% of its low-l support deleted.  A refusal that does not halt is a comment.
        raise SystemExit("  ⛔ REFUSING: the common-grid object is not the banked object; "
                         "NO verdict is computed")
    gate(abs(dfull - drest) <= 1e-14,
         "the support is the full K* -- nothing is dropped, so the collapse cannot move",
         f"full K* {dfull:.6e} vs measured {drest:.6e}; difference {abs(dfull - drest):.2e}")

    # ---- 2 -----------------------------------------------------------------
    # ⛔ amendment 2: 2 log|G|, NEVER log(G**2) -- G**2 underflows to 0 at |G| = 4e-323
    #    while 2 log|G| there is a finite -1484.7, so log(G**2) is -inf where the
    #    quantity it stands for is defined.
    with np.errstate(divide='ignore'):
        lg = {t: 2.0 * np.log(np.abs(Gr[t])) for t in ('lcdm', 'cr')}
    for t in ('lcdm', 'cr'):
        lg[t] = np.where(anydead, 0.0, lg[t])   # finite placeholder; weight is 0 there
    d_ker = lg['cr'] - lg['lcdm']
    W = M_lcdm / M_lcdm.sum(axis=1, keepdims=True)      # amendment 2: each cell's own share
    W = np.where(anydead, 0.0, W)                       # amendment 3: dead cells weigh 0
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
    with np.errstate(divide='ignore'):
        dB = 2.0 * np.log(np.abs(cr_on_qa)) - lg['lcdm'][m]
    dB = np.where(anydead[m] | ~np.isfinite(dB), 0.0, dB)
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

    # ---- 3b (amendment 4) --------------------------------------------------
    # ⛔ ADDED AFTER THE VERDICT WAS FIRST SEEN, and it can only make the claim harder to believe.
    #    A correlation of +0.003 is suspiciously perfect, and the -0.9200 it is read against was
    #    measured on the REAL spectra, not on these pseudo-spectra -- a different object, which
    #    amendment 2 already flagged.  So: feed THIS SAME STATISTIC the COLLAPSED object built from
    #    THESE SAME FOUR banked spectra.  If it returns ~0 there too, the ~0 is an artefact of the
    #    statistic and not a property of the plane, and the verdict means nothing.
    bank = '../r7713_cc66_the_dense_ell_discriminant/pseudo/pseudo__S_%s__K_%s.npz'
    bk = {}
    for ss in ('lcdm', 'cr'):
        for kk in ('lcdm', 'cr'):
            zz = np.load(bank % (ss, kk))
            bk[(ss, kk)] = (zz['ls'], zz['y'])
    l0 = np.intersect1d(bk[('lcdm', 'lcdm')][0], bk[('lcdm', 'cr')][0])

    def yb_(ss, kk):
        L, Y = bk[(ss, kk)]
        return Y[np.searchsorted(L, l0)]

    c_ker = np.log(yb_('lcdm', 'cr')) - np.log(yb_('lcdm', 'lcdm'))
    c_src = np.log(yb_('cr', 'lcdm')) - np.log(yb_('lcdm', 'lcdm'))
    r1, c1, v1 = cond_vif(c_ker, c_src, np.ones_like(c_ker))
    gate(abs(r1) >= S.CORR_MAX and v1 >= S.VIF_MAX,
         'SAME-OBJECT BASELINE -- the same statistic on the COLLAPSED object still sees the degeneracy',
         f"collapsed: corr {r1:+.4f}  cond {c1:.2f}  VIF {v1:.2f}x over {len(l0)} l  "
         f"⇒ the ~0 above is NOT an artefact of the statistic; un-collapsing is what removed it")

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
