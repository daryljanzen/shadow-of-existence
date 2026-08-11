"""
P15_the_two_data_are_one.py -- what the "single inherited datum" rho_r/rho_m ~ 2 actually is, and
what the naturalness argument offered for it actually describes.

** (1) IT IS NOT A DATUM DISTINCT FROM $\eta$.  On any thermal history
        $\rho_r/\rho_m(T) = [1+\nu]\,(\pi^4/30\zeta_3)\,T \;/\; [\,\eta\,(\omega_m/\omega_b)\,m_N\,]$,
   which returns 1.99 at $T=1.6\,$eV -- the quoted value to one per cent, from standard
   thermodynamics and no feature of this construction.  Given $\eta$ and the measured
   matter-to-baryon ratio, both inherited for the composition regardless, the ratio at onset IS the
   onset.  ** So the handover supplies ONE composition datum and the cosmology fits ONE parameter.

** (2) AND THE NATURALNESS ARGUMENT DESCRIBES AN EPOCH NINE ORDERS AWAY FROM THE HANDOVER. **
   $\rho_r=\rho_m$ occurs at $T\simeq0.8\,$eV.  The handover sits four orders ABOVE the deuterium
   bottleneck ($0.07\,$MeV), which is what the nucleosynthesis computed on it requires -- so the
   ratio there is $\sim9\times10^{8}$, and "a handover carrying radiation of order the matter
   density" would be a handover with $\eta\simeq0.5$: no light elements, no acoustic peaks.
   ** The naturalness question therefore runs the other way -- what must be explained is a BILLION
   photons per baryon, which is the baryogenesis-analogue question already named as open. **

WHAT THIS DOES AND DOES NOT TOUCH.  It does not touch the rate, the fit, the baryon-acoustic
confrontation or the abundances.  It corrects an accounting (two data to one datum plus one fitted
parameter) and withdraws an argument (the binding-energy scale offers no head start).

STATUS: ✔✔ (the identity asserted against the quoted datum to better than 5%; the equality
  temperature and the handover-epoch ratios computed; the eta that O(1) would require at each epoch
  computed and contrasted with the measured value; P7's superseded sentence asserted absent)
RUN: python3 P15_the_two_data_are_one.py   RUNTIME: <1s (stdlib only)
ORIGIN: computations/frontier_audit/L150w_the_two_data_are_one.py, built r2376 (c54.105).
ORIGIN-DIVERGENCE: deliberate.  The origin is a LEAD DISPOSAL: it opens on what `F-1` was asking
  for and closes on what the row becomes, which belongs in the ledger and not in a paper receipt.
  This receipt keeps the thermodynamics verbatim and replaces the register talk with a check that
  the papers now carry the corrected accounting.
"""
import math
import os

print(__doc__.split("STATUS:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


# --- standard thermodynamics, nothing framework-specific ---
ZETA3 = 1.2020569031595943
RHO_PER_N = math.pi**4/(30*ZETA3)          # rho_gamma / n_gamma = 2.7012 T
NU = 3*(7/8)*(4/11)**(4/3)                 # three decoupled massless species
G_R = 1.0 + NU                             # rho_r / rho_gamma after e+e- annihilation
M_N = 939.0e6                              # eV, mass per baryon
ETA = 6.10e-10                             # baryon-to-photon ratio, measured
WM, WB = 0.1430, 0.02237                   # physical densities; matter-to-baryon = WM/WB
F = WM/WB
T_ONSET = 1.6                              # eV, the corpus's onset temperature
T_BOTTLENECK = 0.07e6                      # eV, the deuterium bottleneck


def ratio(T, eta=ETA):
    """rho_r/rho_m at photon temperature T, from eta and the matter-to-baryon ratio alone."""
    return G_R*RHO_PER_N*T/(eta*F*M_N)


# =====================================================================
print("=" * 78)
print("PART 1 — THE IDENTITY, AND IT REPRODUCES THE DATUM")
print("=" * 78)
print("  rho_r/rho_m (T)  =  [1 + 3(7/8)(4/11)^{4/3}] * (pi^4/30 zeta3) * T  /  [ eta * (w_m/w_b) * m_N ]")
print(f"     rho_gamma/n_gamma      = {RHO_PER_N:.4f} T")
print(f"     rho_r/rho_gamma        = {G_R:.4f}   (photons + three decoupled neutrino species)")
print(f"     matter per baryon      = (w_m/w_b) m_N = {F:.3f} x {M_N/1e6:.0f} MeV "
      f"= {F*M_N/1e9:.2f} GeV")
print(f"     eta                    = {ETA:.2e}")
print()
r_on = ratio(T_ONSET)
print(f"  ** at the corpus's onset temperature T = {T_ONSET} eV:  rho_r/rho_m = {r_on:.3f} **")
print(f"  ** the corpus's quoted datum:                          rho_r/rho_m ~ 2 **")
assert abs(r_on - 2.0) < 0.10
print()
for s in [
 "⇒⇒ ** THE 'INHERITED DATUM' IS REPRODUCED TO TWO PER CENT FROM $\\eta$, THE MATTER-TO-BARYON RATIO",
 "   AND THE ONSET TEMPERATURE -- NOTHING ELSE ENTERS. **  *No collapse physics, no branch point, no",
 "   feature of this construction at all: it is the standard relation between a photon temperature",
 "   and a baryon-to-photon ratio.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — SO THE TWO DATA ARE ONE DATUM AND ONE FITTED PARAMETER")
print("=" * 78)
print(f"  {'quantity':>34} {'what it is here':>34}")
for a, b in [
    ("eta", "INHERITED -- the composition datum"),
    ("w_m/w_b (matter per baryon)", "INHERITED -- measured content"),
    ("T_onset (equivalently z_onset)", "** FITTED -- the one free number **"),
    ("rho_r/rho_m at onset", "** NOT INDEPENDENT -- the three above **"),
]:
    print(f"  {a:>34} {b:>34}")
print()
p7 = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'), encoding='utf-8',
          errors='replace').read()
gone = 'These are\ndistinct data of the same handover'
here = 'These are not, on inspection, distinct data'
print(f"  P7's superseded sentence ('distinct data of the same handover') is GONE: ** {gone not in p7} **")
print(f"  P7 now carries the corrected accounting:                              ** {here in p7} **")
assert gone not in p7 and here in p7
print()
for s in [
 "⚠⚠ ** THEY ARE NOT DISTINCT.  Fix $\\eta$ and the matter content -- which this cosmology inherits",
 "   for the abundances regardless -- and $\\rho_r/\\rho_m$ at onset IS $T_{\\mathrm{onset}}$. **",
 "",
 "⌗ ** AND THE CORRECTION RUNS IN THE CORPUS'S FAVOUR, which is why it is worth making carefully. **",
 "   *The frontier is ONE inherited datum -- the same $\\eta$ flat $\\Lambda$CDM carries from outside",
 "   its own model -- plus ONE fitted parameter, the onset.  That is a smaller bill than the papers",
 "   currently present, and it is the bill `E·4` already found on the other side: the ratio is the",
 "   onset in imported units.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHERE 'RADIATION OF ORDER THE MATTER DENSITY' ACTUALLY LIVES")
print("=" * 78)
T_eq = T_ONSET/r_on
print(f"  rho_r = rho_m  requires  T = {T_eq:.3f} eV     (the ratio runs linearly in T)")
print()
print(f"  {'epoch':>40} {'T':>16} {'rho_r/rho_m':>14}")
for name, T in [("rho_r = rho_m (equality)", T_eq),
                ("the corpus's onset", T_ONSET),
                ("the deuterium bottleneck", T_BOTTLENECK),
                ("** P7's own handover: 4 orders above **", 1e4*T_BOTTLENECK),
                ("the rest mass per nucleon", M_N)]:
    tt = f"{T:.3f} eV" if T < 1e3 else f"{T/1e6:.3g} MeV"
    print(f"  {name:>40} {tt:>16} {ratio(T):>14.4g}")
print()
floor = ratio(T_BOTTLENECK)
print(f"  ** the corpus's own nucleosynthesis requires the handover ABOVE the bottleneck, so at the")
print(f"     handover rho_r/rho_m >= {floor:.3g} -- at least {floor/2:.0e} times the value at onset. **")
assert floor > 1e4
print()
for s in [
 "⇒⇒ ** SO *'A HANDOVER CARRYING RADIATION OF ORDER THE MATTER DENSITY'* DESCRIBES $T\\simeq0.8\\,$eV,",
 "   WHICH IS NOT THE HANDOVER -- IT IS THE ONSET, AND THE ONSET IS THE FITTED QUANTITY. **",
 "",
 "⚠ ** THE ARGUMENT'S PREMISE AND ITS CONCLUSION THEREFORE LIVE AT DIFFERENT EPOCHS, separated on",
 "   P7's own account by NINE orders of magnitude in temperature, across which the ratio the",
 "   argument is about runs LINEARLY. **  *The premise -- complete collapse liberates binding energy",
 "   of order the rest mass -- is a statement about the deep collapse; the conclusion is a statement",
 "   about $T=1.6\\,$eV.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE COLLAPSE MUST ACTUALLY DELIVER")
print("=" * 78)
print("  Invert the identity: at temperature T, rho_r/rho_m = 1 requires")
print("     eta = [1+nu] (pi^4/30 zeta3) T / [ (w_m/w_b) m_N ]")
print()
print(f"  {'if the handover sits at':>34} {'then O(1) there would mean eta =':>34}")
for name, T in [("the onset, 1.6 eV", T_ONSET),
                ("the deuterium bottleneck", T_BOTTLENECK),
                ("** P7's own handover (4 orders up) **", 1e4*T_BOTTLENECK),
                ("the rest mass per nucleon", M_N)]:
    eta_needed = G_R*RHO_PER_N*T/(F*M_N)
    print(f"  {name:>34} {eta_needed:>34.3g}")
print(f"  {'the measured value':>34} {ETA:>34.3g}")
print()
for s in [
 "⇒⇒ ** A HANDOVER WITH 'RADIATION OF ORDER THE MATTER DENSITY' AT A NUCLEOSYNTHESIS TEMPERATURE",
 "   WOULD MEAN $\\eta\\sim10^{-4}$ OR LARGER, AND AT P7's OWN HANDOVER TEMPERATURE $\\eta\\sim0.5$. **  *Either would",
 "   destroy the very things the corpus computes on it: the light-element abundances and the acoustic",
 "   peak heights both turn on $\\eta\\simeq6\\times10^{-10}$.*",
 "",
 "⇒ ** SO THE HONEST FORM OF THE NATURALNESS QUESTION IS THE OPPOSITE OF THE ONE THE PAPERS ASK:",
 "   not *why is the ratio of order unity* but *why does the handover deliver a plasma with a",
 "   BILLION photons per baryon* -- which is the baryogenesis-analogue question the corpus already",
 "   names as open. **",
 "",
 "⌗⌗ ** AND THAT MEANS `F·1` AND THE $\\eta$-DERIVATION ARE ONE PROBLEM, not two items on a list. **",
 "   *`F·1`'s own text says the consistency target is the measured primordial abundances -- which",
 "   are set by $\\eta$.  It was already asking the $\\eta$ question and calling it by the other name.*",
]:
    print("  " + s)



# =====================================================================
print()
print("=" * 78)
print("THE PAPERS NOW CARRY IT")
print("=" * 78)
p15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8',
           errors='replace').read()
CHECKS = [
    ("P15 withdraws the naturalness argument by name",
     'should be withdrawn rather than carried', p15),
    ("P15 states the handover ratio at ~9e8", r'{\sim}9\times10^{8}', p15),
    ("P15 states the eta ~ 0.5 consequence", r'\eta\simeq0.5', p15),
    ("P15 states the ratio is the fitted onset restated",
     'it is the fitted onset restated', p15),
    ("P7 carries the corrected accounting",
     'what the cosmology fits is one\nparameter', p7),
]
for what, needle, txt in CHECKS:
    hit = needle.replace('\\', '\\') in txt
    print(f"  {what:>52}  ** {'yes' if hit else 'NO':>3} **")
    assert hit, what
print()
print("  ** the correction is in the papers, not only in this receipt. **")
print("=" * 78)
