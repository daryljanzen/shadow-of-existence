"""
P07_nariai_selection.py -- verifies P7's Nariai selection (the reassignment's central criterion), by
  DERIVING the horizon-cubic discriminant from scratch (not asserting 1/9):
    [eq:SdS-cosmology-condition/Nariai-condition/Nariai-mass, sec:sds-cosmology; F3 sec:central]
    (i)   the SdS horizons are the roots of the cubic  r^3 - alpha^2 r + 2M alpha^2 = 0  (alpha^2=3/Lambda);
    (ii)  its discriminant Delta = 4 alpha^4 (alpha^2 - 27 M^2); Delta=0 (double root) <=> alpha^2=27M^2
          <=>  Lambda M^2 = 1/9 (geometric), i.e.  Lambda G^2 M^2 / c^4 = 1/9  (dimensionful) [Nariai-condition];
    (iii) the merged (double) root sits at  r_star = alpha/sqrt3 = 1/sqrt(Lambda)  and the mass is fixed to
          M = alpha/(3 sqrt3) = 1/(3 sqrt(Lambda))  i.e.  M = c^2/(3 sqrt(Lambda) G)  [Nariai-mass];
    (iv)  the TRICHOTOMY by how the reassigned congruence meets its horizon (r-timelike <=> f<0):
          undercritical (Lambda G^2M^2/c^4 < 1/9) two distinct positive horizons (r spacelike between them);
          Nariai (=1/9) tangent/merged; overcritical (>1/9) no positive horizon (r timelike throughout);
    (v)   surface gravity kappa = f'(r_h)/2: kappa=0 at the Nariai double root (f=f'=0, degenerate),
          kappa=1/alpha at the de Sitter horizon r=alpha (M=0).
  [P7 CR_framework sec:sds-cosmology, eqs SdS-cosmology-condition / Nariai-condition / Nariai-mass]
STATUS: ✔✔   RUN: python3 P07_nariai_selection.py   RUNTIME: ~3s
COMPUTES: the discriminant symbolically from the cubic (sympy), the double-root radius and mass by solving
  Delta=0, the sign of f across r for each regime, and kappa from f'. CONTROL below.
CONTROL: undercritical M<alpha/(3sqrt3) gives TWO distinct positive roots with f>0 between them (a static
  region: r spacelike); overcritical M>alpha/(3sqrt3) gives NO positive root and f<0 for all r>0 (r timelike).
  Break M=alpha/(3sqrt3) either way and the double-root / kappa=0 / 1-9 all move -- the check cannot pass by luck.
BOUND: does NOT re-derive that the vacuum solution is SdS (that is P8 matter_functional); takes f=1-2M/r-Lr^2/3
  and works its horizon structure + the r-timelike causal reading. P3's receipts do the dimensionless ellipse/
  sigma root structure; this is the dimensionful Nariai-selection criterion tied to the r-timelike condition.
ORIGIN: built new (fork r1364d) -- P7's sec:sds-cosmology construction block cited no receipt; the ONLY
  confirmed gap the P7 completeness re-audit found (COMPLETENESS_AUDIT.md, C2).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r, M, Lam, alpha = sp.symbols('r M Lambda alpha', positive=True)
G, c = sp.symbols('G c', positive=True)

print("="*74); print("P07 Nariai selection -- horizon-cubic discriminant, DERIVED"); print("="*74)

# ---- (i) the SdS metric function and its horizon cubic -------------------------------------------
f = 1 - 2*M/r - Lam*r**2/3
# horizons f=0; clear the pole and use alpha^2=3/Lambda: multiply f by (-3 r/Lambda)
cubic = sp.expand((-3*r/Lam)*f).subs(Lam, 3/alpha**2)         # r^3 - alpha^2 r + 2 M alpha^2
cubic = sp.expand(cubic)
ok&=check("SdS horizons are the roots of  r^3 - alpha^2 r + 2 M alpha^2 = 0",
          sp.simplify(cubic - (r**3 - alpha**2*r + 2*M*alpha**2))==0)
# no r^2 term  =>  three roots sum to zero (A_2 configuration) -- a Vieta check
ok&=check("no r^2 term  =>  sum of the three roots = 0", sp.Poly(cubic, r).coeff_monomial(r**2)==0)

# ---- (ii) the discriminant, computed by sympy, and the Nariai condition --------------------------
Delta = sp.discriminant(sp.Poly(cubic, r), r)                # depends on M, alpha
Delta = sp.simplify(Delta)
ok&=check("discriminant Delta = 4 alpha^4 (alpha^2 - 27 M^2)  (sympy, from the cubic)",
          sp.simplify(Delta - 4*alpha**4*(alpha**2 - 27*M**2))==0)
# double root  <=>  Delta = 0  <=>  alpha^2 = 27 M^2
sol_M = sp.solve(sp.Eq(Delta, 0), M)                          # positive root
M_nariai = [s for s in sol_M if s.is_positive][0]
ok&=check("Delta=0 (double root)  <=>  M = alpha/(3 sqrt3)   [Nariai mass, geometric]",
          sp.simplify(M_nariai - alpha/(3*sp.sqrt(3)))==0)
# dimensionful: the geometric mass m = alpha/(3 sqrt3) IS G M_phys/c^2, so the dimensionful group
# Lambda G^2 M^2/c^4 = Lambda m^2; substitute m and alpha^2=3/Lambda
LGM = sp.simplify((Lam*(alpha/(3*sp.sqrt(3)))**2).subs(alpha, sp.sqrt(3/Lam)))
ok&=check("dimensionful Nariai condition:  Lambda G^2 M^2 / c^4 = Lambda m^2 = 1/9",  sp.simplify(LGM - sp.Rational(1,9))==0)
M_dim = sp.simplify((alpha/(3*sp.sqrt(3))).subs(alpha, sp.sqrt(3/Lam)))   # geometric M in terms of Lambda
ok&=check("Nariai mass  M = 1/(3 sqrt(Lambda))  (geometric)  =>  M = c^2/(3 sqrt(Lambda) G)  (dimensionful)",
          sp.simplify(M_dim - 1/(3*sp.sqrt(Lam)))==0)

# ---- (iii) the merged (double) root location ----------------------------------------------------
# double root where cubic and its derivative both vanish
cubic_N = cubic.subs(M, alpha/(3*sp.sqrt(3)))
dcubic  = sp.diff(cubic_N, r)
rstar = [s for s in sp.solve(dcubic, r) if s.is_positive][0]  # 3r^2=alpha^2 -> r=alpha/sqrt3
ok&=check("double root at  r_star = alpha/sqrt3", sp.simplify(rstar - alpha/sp.sqrt(3))==0)
ok&=check("cubic(r_star)=0 there (it is genuinely the merged root)", sp.simplify(cubic_N.subs(r, rstar))==0)
ok&=check("r_star = alpha/sqrt3 = 1/sqrt(Lambda)", sp.simplify((alpha/sp.sqrt(3)).subs(alpha, sp.sqrt(3/Lam)) - 1/sp.sqrt(Lam))==0)

# ---- (iv) the trichotomy: r-timelike <=> f<0 ; count positive horizons per regime ----------------
import numpy as np
# alpha=1 (Lambda=3): cubic r^3 - r + 2M ; count positive real roots numerically
def n_pos_roots(mval):
    rts = np.roots([1.0, 0.0, -1.0, 2.0*mval])
    real = [x.real for x in rts if abs(x.imag) < 1e-9]
    return sorted([x for x in real if x > 1e-9])
M_star = 1.0/(3.0*np.sqrt(3.0))              # alpha=1 Nariai mass ~0.19245
under = n_pos_roots(M_star/2)
over  = n_pos_roots(M_star*2)
# at the exact double root numpy returns a near-degenerate pair (tiny imag); take positive real parts
crit_rts = np.roots([1.0,0.0,-1.0,2.0*M_star])
crit_pos = sorted([x.real for x in crit_rts if x.real > 1e-6 and abs(x.imag) < 1e-3])
ok&=check("undercritical (M<alpha/3sqrt3): TWO distinct positive horizons",
          len(under)==2 and abs(under[0]-under[1])>1e-3)
ok&=check("Nariai (M=alpha/3sqrt3): the two positive horizons have MERGED onto 1/sqrt3~0.577 (gap closed)",
          len(crit_pos)>=1 and (max(crit_pos)-min(crit_pos))<1e-2 and abs(crit_pos[0]-1/np.sqrt(3))<1e-2)
ok&=check("overcritical (M>alpha/3sqrt3): NO positive horizon (r timelike throughout)", len(over)==0)
# r-timelike <=> f<0: undercritical has a static region (f>0 somewhere), overcritical does not
def fval(mval, rval): return 1.0 - 2.0*mval/rval - rval**2      # alpha=1 => Lambda r^2/3 = r^2
ok&=check("undercritical: f>0 between the two horizons (a STATIC region, r spacelike there)",
          fval(M_star/2, 0.5*(under[0]+under[1])) > 0)
ok&=check("overcritical: f<0 for all r>0 (r timelike throughout -- the cosmological reading)",
          all(fval(M_star*2, rv) < 0 for rv in [0.3,0.7,1.0,1.5,3.0]))

# ---- (v) surface gravity kappa = f'(r_h)/2 ------------------------------------------------------
fp = sp.diff(f, r)
kappa_N = sp.simplify((fp/2).subs(M, alpha/(3*sp.sqrt(3))).subs(r, alpha/sp.sqrt(3)).subs(Lam, 3/alpha**2))
ok&=check("kappa = f'(r_star)/2 = 0 at the Nariai double root (DEGENERATE horizon, f=f'=0)", sp.simplify(kappa_N)==0)
f_dS = 1 - Lam*r**2/3                                    # M=0 de Sitter; horizon r=alpha
kappa_dS = sp.simplify((sp.diff(f_dS,r)/2).subs(r, alpha).subs(Lam, 3/alpha**2))
ok&=check("kappa = |f'(alpha)|/2 = 1/alpha at the de Sitter horizon r=alpha (M=0, non-degenerate)",
          sp.simplify(sp.Abs(kappa_dS) - 1/alpha)==0)

print("="*74)
print("RESULT:", "ALL PASS -- the horizon cubic's discriminant Delta=4a^4(a^2-27M^2) vanishes exactly at\n"
      "         Lambda G^2M^2/c^4=1/9 (the double root r_star=alpha/sqrt3=1/sqrt(Lambda), M=c^2/(3 sqrt(Lambda) G));\n"
      "         the r-timelike trichotomy (2 horizons / merged / none) follows; kappa=0 at the degenerate seam."
      if ok else "SOME FAILED")
print("="*74)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  Every check above only PRINTED [PASS]/[FAIL] into `ok`, so the
# run exited 0 whatever it found; `ok` is asserted here.  Added on top of it, and not merely a
# restatement: the discriminant's SIGN on both sides of the Nariai mass (positive below, so
# three real roots; negative above, so one), the numeric values the criterion is quoted by --
# M_N = 0.19245009 alpha and r_star = 0.57735027 alpha -- and the dimensionful group Lambda m^2
# evaluated to 1/9 = 0.11111111 rather than only shown to simplify to it.
assert ok, "P07_nariai_selection: one of the printed checks FAILED"
assert sp.simplify(Delta.subs({M: alpha/(3*sp.sqrt(3))})) == 0
assert sp.simplify(Delta.subs({M: alpha/(6*sp.sqrt(3)), alpha: 1})) > 0      # below: 3 real roots
assert sp.simplify(Delta.subs({M: alpha/sp.sqrt(3), alpha: 1})) < 0         # above: 1 real root
assert abs(float(M_nariai.subs(alpha, 1)) - 0.1924500897) < 1e-9
assert abs(float(rstar.subs(alpha, 1)) - 0.5773502692) < 1e-9
assert abs(float(LGM) - 1.0/9.0) < 1e-15
assert abs(float(sp.Abs(kappa_dS).subs(alpha, 2.5)) - 0.4) < 1e-12          # kappa_dS = 1/alpha
assert len(under) == 2 and abs(under[0] - 0.20051164) < 1e-6 and abs(under[1] - 0.88455193) < 1e-6
assert len(over) == 0 and abs(max(crit_pos) - 1/np.sqrt(3)) < 1e-3
print("  [r2376+c54.161] `ok` asserted; plus Delta > 0 below the Nariai mass and Delta < 0 above,")
print("  M_N = 0.19245009 alpha, r_star = 0.57735027 alpha, Lambda m^2 = 1/9 numerically, and the")
print("  undercritical horizon pair at 0.20051164 / 0.88455193.")
