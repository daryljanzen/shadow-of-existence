"""C3 — CONFORMAL TIME ON THE LEG: does the map from the limits to the mode's variable close too?
The integrand Psi(x) is elementary in x = k eta / sqrt3 (C1).  The limits are radii (C2).  So the
whole computation closes only if eta(r) closes as well.  Derive it.
ORIGIN: storyboard_receipts/C3_conformal_map.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp, numpy as np
r,M,al,A,k=sp.symbols('r M alpha A k', positive=True)
print("="*80); print("C3 — DOES eta(r) CLOSE?"); print("="*80)
H2=A/r**4+2*M/r**3+1/al**2
print(f"\n  H^2 = {H2}")
print("  conformal time:  d eta = d tau / r  and  dr/d tau = r H, so  d eta = dr/(r^2 H):")
integ=sp.simplify(1/(r**2*sp.sqrt(H2)))
print(f"     d eta/dr = {sp.simplify(sp.powsimp(integ, force=True))}")
print(f"     = 1/sqrt( r^4/alpha^2 + 2 M r + A )")
chk=sp.simplify(integ - 1/sp.sqrt(r**4/al**2+2*M*r+A))
print(f"     check the two forms agree: {chk}")
print("""
  *** A QUARTIC UNDER A SQUARE ROOT: eta(r) IS AN ELLIPTIC INTEGRAL IN GENERAL. ***
  So the closure does NOT extend automatically to the map.  That is the honest general statement,
  and it is worth having because it says exactly where the elementary structure ends.
""")
print("STEP 2 — BUT WHICH TERM DOMINATES WHERE THE DRIVING HAPPENS?  This is the whole question.")
alv=1.0; Mv=1/(3*np.sqrt(3)); rs=1/np.sqrt(3); Av=4*Mv*rs
print(f"   gauge alpha=1, Nariai M={Mv:.6f}, seam r_s={rs:.6f}, A=4 M r_s={Av:.6f}")
print("   the three terms of  r^4/alpha^2 + 2 M r + A  across the leg:")
print(f"   {'r':>10s} {'r^4/a^2 (Lambda)':>18s} {'2 M r (matter)':>16s} {'A (radiation)':>15s}   dominant")
for rr in [0.02,0.05,0.1,0.2,rs,0.8855,1.5]:
    L=rr**4/alv**2; Mm=2*Mv*rr; R=Av
    dom=max([(L,'Lambda'),(Mm,'matter'),(R,'radiation')])[1]
    tag='  <- SEAM' if abs(rr-rs)<1e-9 else ('  <- r*' if abs(rr-0.8855)<1e-3 else '')
    print(f"   {rr:>10.4f} {L:>18.3e} {Mm:>16.3e} {R:>15.3e}   {dom}{tag}")
print("""
  *** RADIATION IS THE LEADING TERM AT EVERY RADIUS ON THE LEG, seam included -- because A is a
      CONSTANT while the other two vanish as r -> 0. ***
  That is not an approximation chosen for convenience; it is what a constant beats.
""")
print("STEP 3 — SO TAKE THE RADIATION TERM AND SEE WHAT THE CORRECTION COSTS.")
print("   Leading:  d eta/dr = 1/sqrt(A)  ->  eta = r/sqrt(A) : LINEAR, the radiation-era a ~ eta.")
print("   Exact/leading ratio, i.e. how far the elementary map is from the elliptic one:")
for rr in [0.05,0.1,0.2,rs,0.8855]:
    ex=1/np.sqrt(rr**4/alv**2+2*Mv*rr+Av); lead=1/np.sqrt(Av)
    print(f"     r={rr:.4f}:  exact/leading = {ex/lead:.6f}   (departure {100*(1-ex/lead):+.2f}%)")
print("""
  *** SO THE ELEMENTARY MAP eta = r/sqrt(A) IS EXACT TO A FEW PERCENT ACROSS THE WHOLE COLLAPSE LEG
      AND DEGRADES ONLY APPROACHING THE SEAM -- where the matter term finally competes. ***
  AND THAT IS THE CORPUS'S OWN DATUM SPEAKING: rho_r/rho_m = 2 AT THE SEAM means matter reaches
  HALF the radiation only there and is negligible everywhere earlier.
""")
print("="*80)
print("RESULT C3: the integrand is elementary (C1); the LIMITS are radii (C2); and the MAP between")
print("  them is elliptic in general BUT radiation-dominated in fact, because A is a constant and the")
print("  other two terms vanish on the leg.  *** SO THE WHOLE DRIVING INTEGRAL IS ELEMENTARY ON THE")
print("  COLLAPSE LEG, WITH A CONTROLLED AND COMPUTABLE DEPARTURE THAT TURNS ON ONLY AT THE SEAM. ***")
print("  The elliptic structure is real and is where the closed form ends -- it is not hidden.")
print("="*80)

print("\n" + "="*80)
print("STEP 4 — CORRECTING STEP 3's GLOSS, AND THEN ASKING THE QUESTION THAT MATTERS.")
print("="*80)
import numpy as np
print("""
  'Exact to a few percent across the whole leg' OVERSTATES it: the departure is 2% at r=0.05, 8% at
  r=0.2, and 24% AT THE SEAM.  Twenty-four percent is not a few.  Withdrawn as stated.
  *** THE RIGHT QUESTION IS NOT 'IS THE MAP GOOD ON THE LEG' BUT 'IS IT GOOD WHERE THE MODES THAT
      ARE ACTUALLY UNCOMPUTED DO THEIR DRIVING' -- and that is a different and answerable question. ***
""")
alv=1.0; Mv=1/(3*np.sqrt(3)); rs=1/np.sqrt(3); Av=4*Mv*rs
def rH(rr): return np.sqrt(Av/rr**2 + 2*Mv/rr + rr**2/alv**2)
print("STEP 5 — WHERE DOES A MODE OF WAVENUMBER k ENTER?")
print("   entry is (rH)^-1 = 1/k, i.e. rH = k.  At small r, rH -> sqrt(A)/r, so r_entry ~ sqrt(A)/k.")
print("   Take k in units of the seam's own horizon wavenumber k_s = (r_s H(r_s)):")
ks=rH(rs)
print(f"     k_s = r_s H(r_s) = {ks:.6f}   (the mode just entering AT the seam)")
print(f"   {'k/k_s':>8s} {'r_entry':>10s} {'r_entry/r_s':>12s} {'map departure at entry':>24s}")
from scipy.optimize import brentq
for kk in [1,2,5,10,30,100,300]:
    ktarget=kk*ks
    try:
        re_=brentq(lambda x: rH(x)-ktarget, 1e-8, rs)
    except Exception:
        re_=np.nan
    ex=1/np.sqrt(re_**4/alv**2+2*Mv*re_+Av); lead=1/np.sqrt(Av)
    print(f"   {kk:>8d} {re_:>10.6f} {re_/rs:>12.5f} {100*(1-ex/lead):>23.2f}%")
print("""
  *** THE HIGHER THE MODE, THE DEEPER IT ENTERS, AND THE BETTER THE ELEMENTARY MAP IS THERE. ***
  A mode entering at the seam sees the full 24% departure; one entering ten times deeper sees under
  a percent; the high-ell modes enter deeper still.
""")
print("  *** AND THAT IS THE PAYOFF, AND IT IS THE EXACT COMPLEMENT OF WHAT IS OPEN: ***")
print("      the corpus's verified range is ell <~ 800 and the UNCOMPUTED part is the HIGH-ell tail.")
print("      Those are the modes with the LARGEST k, hence the DEEPEST entry, hence the SMALLEST")
print("      departure from the elementary map.")
print("  *** THE CLOSED FORM IS WORST EXACTLY WHERE THE CORPUS ALREADY HAS AN ANSWER, AND BEST")
print("      EXACTLY WHERE IT DOES NOT. ***")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  This receipt printed two tables and asserted nothing.  It is one of the
# files whose figures the c54.155 audit corrected in CR_cosmology.tex, so the current paper
# sentence is pinned here as well as the receipt's own numbers -- a divergence between them now
# fails the gate instead of the prose.
#
# CR_cosmology.tex sec:envelope, as it reads NOW: "eta = r/sqrt A to about two per cent at the
# entry radius of the lowest mode in question and better the deeper the mode enters -- sub-percent
# from k >~ 30 k_s".  (It previously read "better than a percent at the entry radii of the modes
# in question"; that was 1.87% at the paper's own 10 k_s threshold and was corrected.)
#
# Gated below: (1) the seam wavenumber k_s; (2) the 24.4% departure AT the seam, which is what
# STEP 4 withdrew "a few percent" in favour of; (3) the monotone improvement with depth, which is
# the receipt's whole payoff; (4) the two threshold figures the paper now quotes.
# ============================================================================================
def _departure_pct(_k_over_ks):
    """map departure 100(1 - exact/leading) at the entry radius of k = _k_over_ks * k_s.
    Uses the receipt's own rH and the same exact/leading forms as the STEP 5 table."""
    _re = brentq(lambda z: rH(z) - _k_over_ks*ks, 1e-8, rs)
    return 100.0*(1.0 - (1/np.sqrt(_re**4/alv**2 + 2*Mv*_re + Av))/(1/np.sqrt(Av)))

assert abs(ks - 1.5275252) < 1.0e-6, f"k_s = r_s H(r_s) = {ks:.7f}, expected 1.5275252"
# (2) AT the seam the elementary map is 24.4% off -- the number STEP 4 uses to withdraw its gloss.
assert abs(_departure_pct(1) - 24.4071) < 1.0e-3, \
    f"departure at the seam is {_departure_pct(1):.4f}%, expected 24.4071%"
# (3) deeper entry -> better map.  The receipt's payoff sentence, made able to fail.
_dep = [_departure_pct(q) for q in (1, 2, 5, 10, 30, 100, 300)]
assert all(_dep[i] > _dep[i+1] for i in range(len(_dep)-1)), \
    f"the map departure is NOT monotonically decreasing with depth: {_dep}"
# (4) the two figures CR_cosmology.tex sec:envelope quotes this receipt for.
assert abs(_departure_pct(10) - 1.8724) < 1.0e-3, \
    f"paper says 'about two per cent' at 10 k_s; receipt gives {_departure_pct(10):.4f}%"
assert abs(_departure_pct(30) - 0.6280) < 1.0e-3, \
    f"paper says 'sub-percent from k >~ 30 k_s'; receipt gives {_departure_pct(30):.4f}%"
assert _departure_pct(30) < 1.0, "sub-percent does NOT begin by 30 k_s"
assert _departure_pct(10) > 1.0, \
    "10 k_s is now sub-percent -- the paper's corrected 'about two per cent' has drifted"
assert abs(100.0*(1 - ex/lead) - 0.0630) < 1.0e-3, \
    f"departure at 300 k_s (last table row) is {100.0*(1-ex/lead):.4f}%, expected 0.0630%"
print(f"GATE C3 (r2376+c54.160): k_s = {ks:.6f}; map departure {_departure_pct(1):.2f}% at the "
      f"seam, {_departure_pct(10):.2f}% at 10 k_s, {_departure_pct(30):.2f}% at 30 k_s -- pinned "
      f"against CR_cosmology.tex sec:envelope.")
