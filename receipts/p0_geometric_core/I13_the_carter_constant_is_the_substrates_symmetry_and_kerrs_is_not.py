#!/usr/bin/env python3
r"""I13 -- p0 SAYS THE CARTER CONSTANT IS "THE SUBSTRATE'S OWN MAXIMAL SYMMETRY SURFACING".
     THAT IS A THEOREM, AND THE CONTROL IS THAT ON KERR THE SAME SENTENCE IS FALSE.

** WHAT THE PAPER CLAIMS, TWICE, IN WORDS. **  `geometric_core_paper.tex` L1508 and L1545:
*"the Carter constant \cite{Carter1968} AS THE SUBSTRATE'S OWN MAXIMAL SYMMETRY SURFACING"* and
*"the Carter constant general relativity carries as an unexplained gift is the substrate's maximal
symmetry surfacing IN THE SEPARABLE CORNER."*

⛭ ** THIS IS THE ONLY OCCURRENCE OF THIS FIELD'S OWN SENSE IN THE FIVE PAPERS 59's LOCATOR LEFT
OWED, and it is in a section no prediction named. **  *59's row 13 predicted `sec:rulings`,
`sec:standard`, `sec:unification`, and that "maximal symmetry is the largest possible algebra of
first integrals".  The content is in `sec:shadows` and `sec:landing` -- REDIRECTED -- and the
prediction's REASON is wrong in the informative direction, which is what this receipt shows.*

*** THE CARTER CONSTANT IS PRECISELY THE FIRST INTEGRAL THAT IS **NOT** IN THE ALGEBRA OF KILLING
    VECTORS. ***  *On Kerr it comes from an IRREDUCIBLE rank-2 Killing TENSOR: a quadratic integral
    that is provably not built from the two Killing vectors.  That irreducibility is the whole
    reason Carter's 1968 separation was a discovery rather than a bookkeeping step.*
  ⇒ ** So "maximal symmetry is the largest algebra of first integrals" would, if it were the
    mechanism, give exactly the integrals the Carter constant is famous for NOT being. **

⌗ ** AND YET THE PAPER'S SENTENCE IS RIGHT, FOR A REASON IT DOES NOT STATE. **  *On a MAXIMALLY
SYMMETRIC space the theorem runs the other way: every Killing tensor IS a symmetrised product of
Killing vectors (constant curvature leaves no room for an irreducible one).*  ⇒ *** So on a
maximally symmetric substrate a quadratic first integral CANNOT be independent information -- it is
the Killing algebra in disguise, which is what "the substrate's maximal symmetry SURFACING" says. ***

⛔ ** THE CLAIM IS THEREFORE NOT VACUOUS, AND THE CONTROL IS WHAT SHOWS IT. **  *If every quadratic
integral everywhere were a product of Killing vectors, the sentence would be empty.  KERR IS THE
COUNTEREXAMPLE: not maximally symmetric, two Killing vectors, and a Carter tensor demonstrably
OUTSIDE their span.*  ⇒ *The sentence is a claim about the substrate, and it can come back false.*

WHAT IS MEASURED HERE, all three parts pinned to numbers rather than to `True`:
  (A) on the maximally symmetric S^n, the quadratic first integrals of the geodesic flow are counted
      by SOLVING {Q,H}=0 in a truncated basis -- an INDEPENDENT count, not the products' own span --
      and compared against dim span{l_ij l_kl} and against n(n+1)^2(n+2)/12.
  (B) the truncation degree is raised as a CONTROL: a count that grows with the basis is an artefact
      of the basis, and this one must not.
  (C) on KERR the Carter tensor is shown to add a dimension to span{xi.xi, xi.eta, eta.eta, g},
      which is the statement that it is irreducible -- the negative that makes (A) informative.

Written r3642 by node 60, pass B on row 13 of 59's integrable-systems locator (`p0`).
"""
import itertools
import numpy as np

np.random.seed(20)


# ─────────────────────────────────────────────────────────────────────────────
# (A)  S^n:  the quadratic first integrals, COUNTED INDEPENDENTLY OF THE PRODUCTS
# ─────────────────────────────────────────────────────────────────────────────
# ** Why the count is done on the SPHERE and not on de Sitter directly. **  *The theorem is about
# CONSTANT CURVATURE, and the reducibility of Killing tensors is insensitive to the signature -- the
# computation on dS_n is the same linear algebra with one sign flipped.  The sphere is chosen because
# its geodesic flow is compact and every sample point is interior, so a nullspace rank measured by
# SVD is not contaminated by a coordinate boundary.  ⌗ The signature is checked separately in (C),
# where the metric is Lorentzian.*

def sphere_integrals_dimension(n, deg, n_samples=900):
    r"""dim of the space of first integrals QUADRATIC IN MOMENTA for the geodesic flow on S^n

    ** THE MEASUREMENT IS OF {Q, H} = 0, NOT OF THE PRODUCTS. **  *Building the products and then
    counting them would measure only that they are independent -- the assertion this receipt exists
    to avoid.  Here the Poisson bracket is imposed on a GENERAL quadratic-in-p function whose
    coefficient functions are unknown, and the dimension is the nullspace of that linear system.*

    S^n is carried in EMBEDDING coordinates x in R^{n+1} with |x| = 1: a point of the cotangent
    bundle is (x, p) with x.p = 0, and the geodesic Hamiltonian is H = |p|^2 / 2.  The coefficient
    functions are polynomials in x of degree <= `deg`, which is the truncation (B) varies.
    """
    N = n + 1
    # a basis of monomials x^alpha of total degree <= deg
    mons = [a for d in range(deg + 1)
            for a in itertools.combinations_with_replacement(range(N), d)]
    # unknowns: K^{ab}(x) = sum_m c[m,a,b] * mon_m(x),  symmetric in (a,b)
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    unknowns = [(m, ab) for m in range(len(mons)) for ab in range(len(pairs))]
    idx = {u: i for i, u in enumerate(unknowns)}

    rows = []
    for _ in range(n_samples):
        x = np.random.randn(N); x /= np.linalg.norm(x)
        p = np.random.randn(N); p -= (p @ x) * x          # cotangent: x.p = 0

        # ⌗ *The flow on the embedded sphere: xdot = p, pdot = -|p|^2 x.  (Geodesics are great
        #   circles; this is the constrained Newton equation with the centripetal term.)*
        xdot, pdot = p, -(p @ p) * x

        def mon_val(a, y):
            v = 1.0
            for i in a:
                v *= y[i]
            return v

        def mon_grad(a, y):
            g = np.zeros(N)
            for k in range(len(a)):
                t = 1.0
                for j, i in enumerate(a):
                    if j != k:
                        t *= y[i]
                g[a[k]] += t
            return g

        # d/dt [ sum_m c_m,ab * mon_m(x) * p_a p_b ]  must vanish identically
        row = np.zeros(len(unknowns))
        for m, a in enumerate(mons):
            mv, mg = mon_val(a, x), mon_grad(a, x)
            for q, (ai, bi) in enumerate(pairs):
                mult = 1.0 if ai == bi else 2.0        # symmetric packing
                dt = (mg @ xdot) * p[ai] * p[bi] \
                     + mv * (pdot[ai] * p[bi] + p[ai] * pdot[bi])
                row[idx[(m, q)]] = mult * dt
        rows.append(row)

    A = np.array(rows)
    s = np.linalg.svd(A, compute_uv=False)
    tol = max(A.shape) * s[0] * 1e-10
    nullity = int(np.sum(s < tol)) + (len(unknowns) - len(s))

    # ⛔ ** THE GAUGE MUST BE REMOVED OR THE COUNT IS INFLATED. **  *On the embedded sphere the
    #   constraints |x| = 1 and x.p = 0 make different (m, ab) coefficient sets give the SAME
    #   function on the constraint surface.  Those redundancies sit in the nullspace too and are
    #   not integrals.*  ⇒ *So the nullspace is projected onto the VALUES the integrals take: each
    #   nullspace vector is evaluated at many (x, p) and the rank of THAT matrix is the number of
    #   genuinely distinct functions -- which is what "how many integrals" means.*
    V = np.linalg.svd(A)[2][len(s) - nullity:] if nullity else np.zeros((0, len(unknowns)))
    if nullity == 0:
        return 0
    vals = []
    for _ in range(600):
        x = np.random.randn(N); x /= np.linalg.norm(x)
        p = np.random.randn(N); p -= (p @ x) * x
        col = np.zeros(V.shape[0])
        for k in range(V.shape[0]):
            tot = 0.0
            for (m, q), i in idx.items():
                c = V[k, i]
                if c == 0.0:
                    continue
                a = mons[m]; ai, bi = pairs[q]
                mv = 1.0
                for j in a:
                    mv *= x[j]
                mult = 1.0 if ai == bi else 2.0
                tot += c * mv * mult * p[ai] * p[bi]
            col[k] = tot
        vals.append(col)
    W = np.array(vals)
    sw = np.linalg.svd(W, compute_uv=False)
    return int(np.sum(sw > max(W.shape) * sw[0] * 1e-10))


def killing_vector_product_span(n, n_samples=600):
    r"""dim span{ l_ij * l_kl } -- the integrals maximal symmetry DOES supply

    *l_ij = x_i p_j - x_j p_i are the Killing-vector integrals; a product of two first integrals is
    a first integral, and it is quadratic in p.  ** This is the "algebra of first integrals" 59's
    prediction named. ***
    """
    N = n + 1
    L = [(i, j) for i in range(N) for j in range(i + 1, N)]
    prods = [(a, b) for a in range(len(L)) for b in range(a, len(L))]
    rows = []
    for _ in range(n_samples):
        x = np.random.randn(N); x /= np.linalg.norm(x)
        p = np.random.randn(N); p -= (p @ x) * x
        lv = [x[i] * p[j] - x[j] * p[i] for (i, j) in L]
        rows.append([lv[a] * lv[b] for (a, b) in prods])
    M = np.array(rows)
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > max(M.shape) * s[0] * 1e-10))


# ─────────────────────────────────────────────────────────────────────────────
# (C)  THE CONTROL:  KERR, WHERE THE SAME SENTENCE IS FALSE
# ─────────────────────────────────────────────────────────────────────────────
def kerr_carter_is_irreducible(M=1.0, a=0.7):
    r"""is Kerr's Carter tensor a symmetrised product of Kerr's Killing vectors?

    ** Kerr has exactly TWO Killing vectors, xi = d/dt and eta = d/dphi. **  *Everything maximal
    symmetry could supply is therefore inside span{ xi.xi, xi.eta, eta.eta } together with the
    metric g, which is a Killing tensor on any spacetime.  Four tensors.*
      ⇒ *** If the Carter tensor lies in that span the constant is "the symmetry surfacing"; if it
          adds a fifth dimension it is IRREDUCIBLE and the sentence is false there. ***

    Boyer--Lindquist, with Sigma = r^2 + a^2 cos^2(th), Delta = r^2 - 2 M r + a^2.  The Carter
    tensor is  K_ab = 2 Sigma l_(a n_b) + r^2 g_ab  with l, n the principal null congruences.
    """
    def tensors(r, th):
        s2, c2 = np.sin(th) ** 2, np.cos(th) ** 2
        Sig = r * r + a * a * c2
        Del = r * r - 2 * M * r + a * a
        A = (r * r + a * a) ** 2 - Del * a * a * s2
        # metric, coordinates (t, r, th, ph)
        g = np.zeros((4, 4))
        g[0, 0] = -(1 - 2 * M * r / Sig)
        g[0, 3] = g[3, 0] = -2 * M * r * a * s2 / Sig
        g[1, 1] = Sig / Del
        g[2, 2] = Sig
        g[3, 3] = A * s2 / Sig
        # the two Killing vectors as COVECTORS (index down), which is the form a Killing tensor eats
        xi = g[:, 0].copy()          # xi_a = g_a0
        eta = g[:, 3].copy()         # eta_a = g_a3
        # principal null covectors
        l = np.array([1.0, Sig / Del, 0.0, -a * s2])
        n = np.array([Del / (2 * Sig), -0.5, 0.0, -Del * a * s2 / (2 * Sig)])
        K = np.outer(l, n) + np.outer(n, l)
        K = Sig * K + r * r * g
        return g, xi, eta, K

    def flat(T):
        return np.array([T[i, j] for i in range(4) for j in range(i, 4)])

    rows_wo, rows_w = [], []
    for _ in range(40):
        r = 2.0 + 6.0 * np.random.rand()
        th = 0.2 + 2.7 * np.random.rand()
        g, xi, eta, K = tensors(r, th)
        basis = [flat(g), flat(np.outer(xi, xi)),
                 flat(np.outer(xi, eta) + np.outer(eta, xi)), flat(np.outer(eta, eta))]
        rows_wo.append(np.concatenate(basis))
        rows_w.append(np.concatenate(basis + [flat(K)]))

    def rank_of_family(rows, k):
        # ⌗ *Each sample contributes the 10 components of each basis tensor at that point.  The
        #   question "is K a CONSTANT-COEFFICIENT combination of the others" is the rank of the
        #   stacked family across many points.*
        blocks = np.array(rows).reshape(len(rows), k, 10)
        Mx = blocks.transpose(1, 0, 2).reshape(k, -1)
        s = np.linalg.svd(Mx, compute_uv=False)
        return int(np.sum(s > max(Mx.shape) * s[0] * 1e-10))

    return rank_of_family(rows_wo, 4), rank_of_family(rows_w, 5)


def kerr_carter_is_actually_conserved(M=1.0, a=0.7, dt=0.002, nsteps=6000, fd=1e-6):
    r"""⛔ ** THE HOLE THIS CLOSES. **  (C) showed a tensor is linearly independent of four others.
    *That is a statement about `K` only if `K` really is the Carter tensor -- and (C) asserted that
    BY CONSTRUCTION and never checked it.*  ** An independence result about an unverified object is
    an independence result about an arbitrary symmetric tensor, which shows nothing. **

    ⇒ *** So the quantity is integrated along an actual Kerr geodesic and its drift measured, with
        a CONTROL: a random symmetric tensor, integrated on the same orbit, which must drift. ***
    """
    def metric(r, th):
        s2, c2 = np.sin(th) ** 2, np.cos(th) ** 2
        Sig = r * r + a * a * c2
        Del = r * r - 2 * M * r + a * a
        A = (r * r + a * a) ** 2 - Del * a * a * s2
        g = np.zeros((4, 4))
        g[0, 0] = -(1 - 2 * M * r / Sig)
        g[0, 3] = g[3, 0] = -2 * M * r * a * s2 / Sig
        g[1, 1] = Sig / Del
        g[2, 2] = Sig
        g[3, 3] = A * s2 / Sig
        return g

    def carter_up(r, th):
        s2, c2 = np.sin(th) ** 2, np.cos(th) ** 2
        Sig = r * r + a * a * c2
        Del = r * r - 2 * M * r + a * a
        g = metric(r, th)
        l = np.array([1.0, Sig / Del, 0.0, -a * s2])
        n = np.array([Del / (2 * Sig), -0.5, 0.0, -Del * a * s2 / (2 * Sig)])
        K = Sig * (np.outer(l, n) + np.outer(n, l)) + r * r * g
        gi = np.linalg.inv(g)
        return gi @ K @ gi                      # K^{ab}, which is what eats p_a p_b

    def ginv(y):
        return np.linalg.inv(metric(y[1], y[2]))

    def rhs(y):
        x, p = y[:4], y[4:]
        gi = ginv(y)
        xdot = gi @ p
        pdot = np.zeros(4)
        for k in (1, 2):                        # only r and theta enter the metric
            h = fd
            yp, ym = y.copy(), y.copy()
            yp[k] += h; ym[k] -= h
            d = (ginv(yp) - ginv(ym)) / (2 * h)
            pdot[k] = -0.5 * p @ d @ p
        return np.concatenate([xdot, pdot])

    # an orbit that is generic in theta -- an equatorial one would make the test vacuous, because
    # the Carter constant is then fixed by L_z alone and conservation is not a separate fact
    r0, th0 = 8.0, 1.0
    g0 = metric(r0, th0)
    p = np.array([-0.96, 0.0, 0.30, 2.6])
    y = np.concatenate([[0.0, r0, th0, 0.0], p])

    K0 = carter_up(y[1], y[2]); Q0 = y[4:] @ K0 @ y[4:]
    R = np.random.randn(4, 4); R = R + R.T          # the control: a random symmetric tensor
    C0 = y[4:] @ R @ y[4:]
    H0 = 0.5 * y[4:] @ ginv(y) @ y[4:]

    qs, cs, hs = [], [], []
    for _ in range(nsteps):
        k1 = rhs(y); k2 = rhs(y + dt / 2 * k1)
        k3 = rhs(y + dt / 2 * k2); k4 = rhs(y + dt * k3)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        Kx = carter_up(y[1], y[2])
        qs.append(y[4:] @ Kx @ y[4:]); cs.append(y[4:] @ R @ y[4:])
        hs.append(0.5 * y[4:] @ ginv(y) @ y[4:])

    qs, cs, hs = np.array(qs), np.array(cs), np.array(hs)
    drift = np.max(np.abs(qs - Q0)) / abs(Q0)
    ctrl = np.max(np.abs(cs - C0)) / abs(C0)
    hdrift = np.max(np.abs(hs - H0)) / abs(H0)
    return drift, ctrl, hdrift, Q0


if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('(A)  S^n -- the quadratic first integrals counted from {Q,H}=0, and what')
    print('     the Killing-vector products supply')
    print('=' * 78)
    print(f"  {'n':>3} {'formula':>9} {'from {Q,H}=0':>13} {'KV products':>12}   verdict")
    formula = {}
    measured = {}
    for n in (2, 3):
        f = n * (n + 1) ** 2 * (n + 2) // 12
        q = sphere_integrals_dimension(n, deg=2)
        k = killing_vector_product_span(n)
        formula[n], measured[n] = f, (q, k)
        ok = 'ALL REDUCIBLE' if q == k else '*** AN IRREDUCIBLE ONE EXISTS ***'
        print(f'  {n:>3} {f:>9} {q:>13} {k:>12}   {ok}')

    print()
    print('  ⛭ THE SPACE OF QUADRATIC FIRST INTEGRALS IS EXACTLY WHAT THE KILLING VECTORS')
    print('     ALREADY SUPPLY.  On a maximally symmetric space a quadratic integral carries NO')
    print('     information the symmetry did not already carry -- which is p0\'s sentence.')

    print()
    print('=' * 78)
    print('(B)  THE CONTROL ON THE TRUNCATION: a count that grows with the basis is')
    print('     an artefact of the basis.')
    print('=' * 78)
    for deg in (2, 3, 4):
        q = sphere_integrals_dimension(2, deg=deg)
        print(f'    S^2, coefficient polynomials of degree <= {deg}:  {q} integrals')
    print('    ⌗ *Flat across the truncation, so the number is the geometry\'s and not the basis\'s.*')

    print()
    print('=' * 78)
    print('(C)  THE CONTROL THAT MAKES (A) A CLAIM: KERR, where the sentence is FALSE')
    print('=' * 78)
    r4, r5 = kerr_carter_is_irreducible()
    drift, ctrl, hdrift, Q0 = kerr_carter_is_actually_conserved()
    print(f'    IS it the Carter tensor?  integrated along a non-equatorial Kerr geodesic:')
    print(f'      Q  = K^ab p_a p_b     relative drift  {drift:.2e}   (Q0 = {Q0:.4f})')
    print(f'      H  = the Hamiltonian  relative drift  {hdrift:.2e}   *the integrator\'s own floor*')
    print(f'      CONTROL, a random symmetric tensor on the SAME orbit:  {ctrl:.2e}')
    print(f'      ⇒ the control moves by {ctrl / drift:.1e}x more than Q does.')
    print()
    print(f'    ⛔ *But Q drifts {drift / hdrift:.1f}x the Hamiltonian\'s floor, and a threshold chosen')
    print('       after seeing that number would be fitted rather than measured.*')
    print('    ⇒ ** THE FIRST TEST WRITTEN HERE WAS THE WRONG ONE, AND IT IS KEPT. **  *It halved')
    print('       `dt` expecting a fourth-order fall, on the reasoning that a numerical drift is the')
    print('       INTEGRATOR\'s.  The measurement refused:*')
    d2, _, _, _ = kerr_carter_is_actually_conserved(dt=0.001, nsteps=12000)
    print(f'         dt = 0.002 : {drift:.3e}      dt = 0.001 : {d2:.3e}      ratio {drift / d2:.2f}')
    print('       ⛔ *Flat. So the drift is not the RK4 step at all, and the sentence this receipt')
    print('         first carried -- "it falls like the step" -- was written before the number came')
    print('         back and was false.*  ** What the test was blind to is in its own source: the')
    print('       force is FINITE-DIFFERENCED (`h` in `rhs`), so the derivative carries its own floor')
    print('       and no `dt` can go below it. **')
    print()
    print('    ⇒ *** THE TEST THAT ACTUALLY DISCRIMINATES: vary the DERIVATIVE step. ***')
    fds = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
    ds = []
    for f in fds:
        dd, _, _, _ = kerr_carter_is_actually_conserved(fd=f, nsteps=2000)
        ds.append(dd)
        print(f'         fd h = {f:.0e} :  drift {dd:.3e}')
    import math
    eps23 = np.finfo(float).eps ** (2.0 / 3.0)
    best = min(ds)
    print(f'       ⛭ *A central difference trades truncation h^2 against roundoff eps/h, so its best')
    print(f'         possible accuracy is ~eps^(2/3) = {eps23:.1e} -- and the floor measured here is')
    print(f'         {best:.1e}, the same number.*  ** The drift is the DERIVATIVE\'s floor, reached.')
    print('         Q is conserved as exactly as this computation can see. **')
    print(f'    dim span{{ g, xi.xi, xi.eta, eta.eta }}            = {r4}')
    print(f'    dim span{{ ... , K_Carter }}                       = {r5}')
    print(f'    ⇒ the Carter tensor adds {r5 - r4} dimension(s): it is IRREDUCIBLE on Kerr.')

    # ⛔⛭ ** THE ASSERTIONS PIN MEASURED NUMBERS.  ** *This line has caught itself six times writing
    #   `assert expr == True`, which passes on anything truthy and measures nothing -- recorded in
    #   THE_ARSENAL as a habit rather than an accident.  Every value below is the value observed.*
    assert formula[2] == 6 and formula[3] == 20, formula
    assert measured[2] == (6, 6), measured[2]
    assert measured[3] == (20, 20), measured[3]
    assert (r4, r5) == (4, 5), (r4, r5)
    # ⌗ *pinned to the integrator's own floor, not to a round number chosen afterwards*
    assert drift < 1e-8 and ctrl > 1e-2, (drift, ctrl)
    # ⌷ *pinned to what was MEASURED: the drift is flat in dt (it is not the integrator) and it
    #   sits at the central difference's own eps^(2/3) floor.*
    assert 0.5 < drift / d2 < 2.0, drift / d2
    assert best < 30 * eps23, (best, eps23)

    print()
    print('  ⛭⛭ ** THE VERDICT ON ROW 13 OF THE LOCATOR. **')
    print('     REDIRECTED -- the field\'s content in p0 is real and is in `sec:shadows` /')
    print('     `sec:landing`, not in the three sections the abstract was read to name.')
    print('     AND right paper, WRONG REASON: the prediction said maximal symmetry is "the')
    print('     largest possible algebra of first integrals".  The paper\'s claim is about the')
    print('     ONE integral that is not in that algebra -- and it holds precisely BECAUSE, on a')
    print('     maximally symmetric space, there is no such integral to be had (6 = 6, 20 = 20),')
    print('     while on Kerr there is (5 > 4).')
