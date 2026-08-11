#!/usr/bin/env python3
"""
`L-150`.  ** THE MACHINE BUILT AT c54.137 HAS A SECTOR IN WHICH IT RUNS WITH NO IDEALISATION AT ALL —
THE TENSORS — AND IT WAS NOT ASKED.  IT RETURNS $\\mathcal{P}_T\\simeq5\\times10^{-111}$: ONE HUNDRED ORDERS
BELOW THE OBSERVATIONAL BOUND, AND NO LONGER RESTING ON THE SUBSTRATE'S FLOOR. **

c54.137 computed the scalar transfer on one stated idealisation, $z\\propto a$ with $c_s=1$.  ** For
tensors that is not an idealisation: $z_T=aM_{\\rm Pl}/2$ EXACTLY, for any content whatever, so
$z_T''/z_T=a''/a$ identically and the whole passage applies verbatim. **  And the same background
answers front #3 — is the leading-order interior good enough — in both its halves.

  PART 1  ** THE TENSOR SECTOR CARRIES NO HYPOTHESIS: $z_T\\propto a$ is exact, and the potential is
          the same $2/(x(x+2\\rho))$ the scalars needed an assumption to get. **
  PART 2  ** $\\mathcal{P}_T=144\\pi(\\ell_P/M)^2\\rho^{-6}$ — and the number. **
  PART 3  ** WHAT $r$ THEN BOUNDS, AND IT IS A STATEMENT ABOUT THE PARENT: the crossing multiplies
          the tensor-to-scalar ratio by a CONSTANT. **
  PART 4  ** FRONT #3, HALF ONE — NONLINEARITY.  $\\delta$ and $h$ peak at equality at $\\sim10^{-6}$. **
  PART 5  ** FRONT #3, HALF TWO — ANISOTROPY, WHICH IS THE STANDARD KILLER OF BOUNCING MODELS AND
          WHICH THIS CONSTRUCTION EXCLUDES BY THE SAME ASSUMPTION THAT MAKES ITS BRANCH POINT A
          NARIAI LOCUS. **
  PART 6  The verdict on front #3, and the residue.

Run: python3 L150g_the_tensor_sector_and_the_interiors_adequacy.py      (numpy, sympy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])

LAM, LP, MPC = 1.1056e-52, 1.616255e-35, 3.0857e22
AS_OBS, R_BOUND = 2.1e-9, 0.032
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))
RHO_HI, RHO_LO = 0.0539, 3.8e-6                 # rho DETERMINED at c54.143; BBN floor below

# =====================================================================
print("=" * 78)
print("PART 1 — THE TENSOR SECTOR CARRIES NO HYPOTHESIS")
print("=" * 78)
a, w, cs, Mpl = sp.symbols('a w c_s M_Pl', positive=True)
zS = a * sp.sqrt(3 * (1 + w)) * Mpl / cs
zT = a * Mpl / 2
print(f"  {'variable':>14} {'z':>34} {'z/a constant?':>22}")
for nm, z, note in [("scalar", "a sqrt(3(1+w)) M_Pl / c_s", "only if w AND c_s are"),
                    ("tensor", "a M_Pl / 2", "** ALWAYS **")]:
    print(f"  {nm:>14} {z:>34} {note:>22}")
assert sp.simplify(zS.subs({w: 0, cs: 1}) - a * sp.sqrt(3) * Mpl) == 0
print()
for s in [
 "⇒⇒ ** THAT IS THE WHOLE POINT AND IT IS ONE LINE.  $z_S/a$ moves across equality — $(1+w)$ runs",
 "   $1\\to4/3$ and $c_s$ runs $0\\to1/\\sqrt3$ — so $z_S''/z_S\\ne a''/a$ in general, and c54.137's",
 "   scalar calculation had to FIX $w$ and $c_s$ to proceed.  $z_T/a$ is a pure number for every",
 "   content, every equation of state, every sound speed. **",
 "",
 "⇒ ** SO c54.137's BACKGROUND, CONNECTION AND MONODROMY APPLY TO THE TENSORS UNCONDITIONALLY:",
 "   same $a(x)=M(\\rho x+x^2/2)$, same potential $2/(x(x+2\\rho))$, same $c_0=(3/2\\rho)D$, same",
 "   $2\\pi/\\rho$.  Only the final division differs. **",
 "   *The one place the machine runs without a stated idealisation is the place nobody asked it.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TENSOR POWER, AND THE NUMBER")
print("=" * 78)
k, rho, M, hbar = sp.symbols('k rho M hbar', positive=True)
D = sp.sqrt(hbar / 2) * k**sp.Rational(-3, 2)          # vacuum, per polarisation
C = (2 * sp.pi / rho) * (sp.Rational(3, 2) / rho) * D  # connection then monodromy
h = C / (M * rho * Mpl / 2)                            # v/z_T at the crunch, z_T = a M_Pl/2
PT = sp.simplify(2 * k**3 / (2 * sp.pi**2) * h**2)     # 2 polarisations
print(f"  h_out = C / z_T'   with   z_T = a M_Pl/2,  a = M rho |sigma|")
print(f"  ** P_T(k) = {PT} **          -- k has cancelled: scale-invariant")
assert sp.simplify(sp.diff(PT, k)) == 0
PT_c = sp.simplify(PT.subs({hbar: 1, Mpl: 1 / sp.sqrt(8 * sp.pi)}))     # G = c = hbar = 1
print(f"  in G = c = hbar = 1 (M_Pl = 1/sqrt(8 pi G)) :  P_T = {PT_c}")
print(f"  ** i.e.  P_T = 144 pi (l_P/M)^2 rho^(-6) **   with l_P^2 = hbar G/c^3")
assert sp.simplify(PT_c - 144 * sp.pi / (M**2 * rho**6)) == 0

# and the scalar, on c54.137's idealisation, for the ratio
zS0 = a * sp.sqrt(3) * Mpl                              # w = 0, c_s = 1
PS = sp.simplify(k**3 / (2 * sp.pi**2) * (C / (M * rho * sp.sqrt(3) * Mpl))**2)
rr = sp.simplify(PT / PS)
print(f"\n  and on c54.137's scalar idealisation the ratio is  ** r = {rr} **"
      f"   ( = 24(1+w)c_s at w = 0, c_s = 1 )")
assert sp.simplify(rr - 24) == 0


def P_T_of(rho_v, M_v=M_nar):
    return 144 * np.pi * (LP / M_v)**2 * rho_v**-6.0


print()
print(f"  {'rho':>14} {'P_T from the vacuum':>24} {'observational bound':>22} {'below by':>12}")
bound = R_BOUND * AS_OBS
for rv in [RHO_HI, 1e-4, RHO_LO]:
    v = P_T_of(rv)
    print(f"  {rv:>14.2e} {v:>24.3e} {bound:>22.2e} {bound/v:>12.1e}")
v_hi = P_T_of(RHO_HI)
print(f"\n  ** AT THE MOST GENEROUS PERMITTED COMPOSITION, P_T = {v_hi:.2e} AGAINST A BOUND OF"
      f" {bound:.1e} **")
print(f"  ** i.e. r = P_T/A_s = {v_hi/AS_OBS:.2e}.  BELOW THE BOUND BY {bound/v_hi:.0e}. **")
assert bound / v_hi > 1e95
print()
for s in [
 "⇒⇒⇒ ** SO THIS COSMOLOGY PREDICTS NO PRIMORDIAL $B$-MODES AT ANY CONCEIVABLE SENSITIVITY, AND THE",
 "   PREDICTION NO LONGER RESTS ON THE SUBSTRATE'S OWN FLOOR. **  *P15 `sec:amplitude` already says",
 "   there are no substrate-sourced $B$-modes, on the ground that the substrate's de Sitter tensor",
 "   vacuum is $\\sim10^{-122}$.  **That argument has the same scope defect c54.137 found in its",
 "   scalar twin: it rules out the substrate's vacuum and says nothing about the progenitor's.***",
 "   *This closes it in the sector where the closing needs no hypothesis at all.*",
 "",
 "⌗ ** AND THE TWO CALCULATIONS ARE NOT INDEPENDENT CHECKS OF EACH OTHER — they are the same",
 "   passage divided by two different $z$'s — so what this adds is not confirmation but SCOPE: the",
 "   scalar statement is conditional and the tensor statement is not. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT r BOUNDS, AND IT IS A STATEMENT ABOUT THE PARENT")
print("=" * 78)
print("  Every k-dependent factor in the passage — the connection 3/2rho, the monodromy 2pi/rho, the")
print("  division by a'(eta_c) = -M rho — is IDENTICAL for the two sectors and free of k.  So")
print()
print("     ** r_observed = 24 x (the parent's own tensor-to-scalar amplitude ratio) **")
print()
print("  and the crossing cannot manufacture or destroy a tensor signal: it multiplies the ratio by")
print("  a constant.")
print()
print(f"  {'reading':>34} {'statement':>44}")
for a_, b_ in [("if the parent's tensors are vacuum", f"r = {v_hi/AS_OBS:.0e} -- unobservable, forever"),
               ("if they share the scalars' enhancement", "r = 24 -- excluded by three orders"),
               ("what the sky actually permits", f"parent's ratio <= {R_BOUND/24:.1e}")]:
    print(f"  {a_:>34} {b_:>44}")
print()
for s in [
 "⇒⇒ ** SO THE OBSERVED ABSENCE OF $B$-MODES IS, IN THIS COSMOLOGY, A MEASUREMENT OF THE PREVIOUS",
 "   GENERATION: the parent's own tensor-to-scalar ratio was below $1.3\\times10^{-3}$. **",
 "   *And that sits beside c54.137's other statement about the parent — that its scalar amplitude",
 "   exceeded its own vacuum by $\\sim10^{47}$ — as the second thing this construction says about a",
 "   universe it does not observe.*",
 "",
 "⌗ *The factor 24 carries c54.137's scalar idealisation and no more: it is $24(1+w)c_s$ on the",
 "   contracting leg, the standard matter-bounce value.  **The absolute $\\mathcal{P}_T$ of PART 2",
 "   carries nothing.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — FRONT #3, HALF ONE: DOES LINEAR THEORY SURVIVE TO THE CRUNCH?")
print("=" * 78)
print("  On the beta = 2 leg zeta grows as |sigma|^{-3}, so the question is real and has never been")
print("  asked.  Normalise by the OUTPUT, which is observed:")
print("     zeta(sigma) / zeta_out = (2/3pi) (rho/|sigma|)^3        [c54.137's own chain, run back]")
print("  and the density contrast in matter domination is delta = (2/3)(k/aH)^2 Phi with aH = 2/|sigma|")
print("  and Phi = (3/5) zeta:")
print("     ** delta(sigma) = (1/10) k^2 sigma^2 zeta(sigma) = 0.0212 k^2 rho^3 zeta_out / |sigma| **")
print()
zeta_out = np.sqrt(AS_OBS)
print(f"  {'rho':>12} {'k (at the break)':>18} {'delta at equality':>20} {'h at equality':>18}")
for rv in [RHO_HI, 1e-4, RHO_LO]:
    kb = 1.0 / rv
    d_eq = (1 / 10) * (2 / (3 * np.pi)) * kb**2 * rv**2 * zeta_out
    h_eq = (2 / (3 * np.pi)) * np.sqrt(R_BOUND * AS_OBS)
    print(f"  {rv:>12.2e} {kb:>18.0f} {d_eq:>20.2e} {h_eq:>18.2e}")
    assert d_eq < 1e-4
print("  ** and the column is CONSTANT, which is not a coincidence: at the break mode k = 1/rho the")
print("     combination k^2 rho^2 is unity, so the peak contrast is a pure number times the observed")
print("     amplitude and does not know the composition at all. **")
print()
print("  Below equality the growth REVERSES: in radiation domination aH = 1/|sigma| and Phi ∝ 1/|sigma|,")
print("  so delta ∝ |sigma| and falls to zero at the crunch.  ** The maximum sits AT equality. **")
print()
for s in [
 "✔✔ ** SO LINEAR THEORY SURVIVES THE WHOLE PASSAGE WITH SIX ORDERS TO SPARE, AND THE MARGIN IS NOT",
 "   AN ASSUMPTION — it is read off the OBSERVED amplitude by running c54.137's own chain",
 "   backwards. **  *The largest contrast the progenitor ever carried, on any mode the sky sees, is",
 "   about one part in a million, and it occurs at its matter--radiation equality.*",
 "",
 "⌗ ** AND THE SAME HOLDS FOR THE TENSORS BY THE SAME ARGUMENT AT THE OBSERVATIONAL CEILING: $h$",
 "   peaks at $\\sim10^{-6}$. **  *So neither sector goes nonlinear, and the leading-order interior",
 "   is adequate for everything c54.121--137 computed on it.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — FRONT #3, HALF TWO: ANISOTROPY")
print("=" * 78)
print("  ** THIS IS THE STANDARD KILLER OF BOUNCING COSMOLOGIES AND THE CORPUS HAS NEVER NAMED IT. **")
print("  A Bianchi shear adds Sigma^2/a^2 to (da/deta)^2 = B + A a - a^2, and it is the term that")
print("  wins at small a.  What that does to the crunch is not a correction:")
x = sp.symbols('x', positive=True)
Sig = sp.symbols('Sigma', positive=True)
a_sh = sp.sqrt(2 * Sig * x)                     # a a' = Sigma  =>  a = sqrt(2 Sigma x)
pot_sh = sp.simplify(sp.diff(a_sh, x, 2) / a_sh)
print(f"     shear-dominated:  a = {a_sh}  ∝ x^(1/2)   and   a''/a = {pot_sh}")
s_ = sp.symbols('s')
roots_sh = sp.solve(sp.Eq(s_ * (s_ - 1), sp.Rational(-1, 4)), s_)
print(f"     indicial roots: {roots_sh}   -- a DOUBLE root at 1/2")
assert roots_sh == [sp.Rational(1, 2)]
print()
print(f"  {'crunch':>28} {'a ∝':>12} {'z''/z':>14} {'exponents':>16} {'monodromy':>16}")
for nm, ap, pp, ex, mo in [("dust only", "sigma^2", "2/sigma^2", "(-1, 2)", "DIAGONAL"),
                           ("with radiation (c54.130)", "sigma", "1/(rho sigma)", "(0, 1)", "2 pi/rho"),
                           ("with ANY shear", "sigma^(1/2)", "-1/(4 sigma^2)", "(1/2, 1/2)", "different again")]:
    print(f"  {nm:>28} {ap:>12} {pp:>14} {ex:>16} {mo:>16}")
print()
for s in [
 "⚠⚠ ** SO A SHEAR-DOMINATED CRUNCH IS NOT A PERTURBATION OF THE ONE c54.130–137 COMPUTED ON — IT",
 "   IS A DIFFERENT SINGULAR POINT, with a degenerate indicial pair and a logarithm at zeroth order",
 "   rather than at the first step. **  *Everything from c54.130 onwards would describe the wrong",
 "   background.*",
]:
    print("  " + s)
print()
print("  ** BUT THE SHEAR IS NOT A FREE DATUM, AND THIS IS WHERE THE ANSWER STOPS BEING A SHRUG. **")
print("  At k = 0 the tensor equation is h'' + 2(a'/a)h' = 0, so h' ∝ 1/a^2 and")
print("     ** Sigma = a^2 h' / 2 = CONSTANT ** ")
print("  -- i.e. the Bianchi shear IS the long-wavelength growing tensor mode, the same object PART 2")
print("  just bounded.  So its size is fixed by the tensor spectrum rather than chosen.")
print()
print("  In the matter era h ∝ |sigma|^{-3}, so |h'| = 3h/|sigma| and a = M sigma^2/2, giving")
print("     ** Sigma = (3/8) M^2 |sigma|^3 h(sigma) ** , evaluated anywhere -- take equality.")
print("  Against the domination threshold Sigma << M^2 rho^3 / 2 (shear beats radiation at a_eq):")
print()
h_ceiling = (2 / (3 * np.pi)) * np.sqrt(R_BOUND * AS_OBS)
h_pred = (2 / (3 * np.pi)) * np.sqrt(P_T_of(RHO_HI))
print(f"  {'tensor amplitude used':>44} {'h at equality':>16} {'Sigma / threshold':>20}")
for nm, hv in [("the OBSERVATIONAL CEILING (r < 0.032)", h_ceiling),
               ("** the PREDICTED P_T (PART 2) **", h_pred)]:
    ratio = (3 / 8) * hv / 0.5
    print(f"  {nm:>44} {hv:>16.2e} {ratio:>20.2e}")
    assert ratio < 1e-5
print()
for s_ in [
 "✔✔✔ ** SO THE ANISOTROPY DANGER IS BOUNDED AND NOT MERELY ASSUMED AWAY: even granting the",
 "   progenitor the largest tensor amplitude the sky permits, the induced shear is SIX ORDERS below",
 "   the value at which it would take over the crunch — and on this construction's own predicted",
 "   tensor amplitude, fifty. **",
 "   *That is the substantive half of the answer, and it did not exist before PART 2: the shear",
 "   could only be bounded once the tensor sector had been.*",
 "",
 "⌗ ** AND THE STRUCTURAL HALF, WHICH COVERS WHAT THE BOUND CANNOT.  A genuinely homogeneous shear",
 "   is not a perturbation of a closed FRW ball at all — the $S^3$ tensor tower starts at $L=2$ and",
 "   has no $k=0$ member — so it would be a change of BACKGROUND CLASS, from FRW to Bianchi IX. **",
 "   *And the construction selects FRW by its matching: the progenitor's exterior is",
 "   Schwarzschild--de Sitter and the branch point IS that exterior's Nariai locus, which is a",
 "   spherically symmetric statement throughout.*  ***One may not drop the symmetry and keep the",
 "   Nariai locus; and within the class the symmetry selects, the residual anisotropy is the $L\\ge2$",
 "   tower, which is what the table above bounds.***",
 "",
 "⚠ *What that leaves is a scope statement rather than an open question: the selection of FRW over",
 "   Bianchi IX is an INPUT of the construction, made by the exterior it matches to, and not a",
 "   result derived within it.*",
]:
    print("  " + s_)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE VERDICT ON FRONT #3")
print("=" * 78)
print(f"  {'threat to the leading-order interior':>46} {'status':>32}")
for a_, b_ in [("nonlinearity of the scalar modes", "** CLOSED: 1e-6 at worst **"),
               ("nonlinearity of the tensor modes", "** CLOSED: 1e-6 at the ceiling **"),
               ("dissipation / imperfect fluid", "not reached; sub-dominant"),
               ("homogeneous (Bianchi) shear", "** not a perturbation at all **"),
               ("shear from the L >= 2 tensor tower", "** CLOSED: 1e-6 of threshold **")]:
    print(f"  {a_:>46} {b_:>32}")
print()
for s in [
 "✔✔✔ ** FRONT #3 CLOSES.  The row asked whether the leading-order interior is good enough, and",
 "   on every threat it names the answer is yes with orders to spare — the perturbations stay",
 "   linear by six, and the anisotropy that kills generic bouncing models is bounded by six on the",
 "   sky's own ceiling and by fifty on this construction's predicted tensor amplitude. **",
 "   *And the bound is the right kind: the shear is not a free datum but the long-wavelength",
 "   growing tensor mode, so bounding the tensor sector bounded it.  **That link did not exist",
 "   before PART 2, which is why the front looked structural and unfalsifiable and is neither.***",
 "",
 "⌗ ** WHAT REMAINS IS A SCOPE STATEMENT AND NOT AN OPEN QUESTION: the construction works in the",
 "   spherically symmetric class, selected by the exterior it matches to, and a genuinely",
 "   homogeneous shear is a change of CLASS rather than a perturbation — the closed $S^3$ tensor",
 "   tower has no $k=0$ member. **  *One may not drop the symmetry and keep the Nariai locus, and",
 "   that is a premise of the construction rather than a gap in it.*",
]:
    print("  " + s)