#!/usr/bin/env python3
"""
L-150w — `F·1`, "DERIVE $\\rho_r/\\rho_m\\approx2$ FROM THE PROGENITOR COLLAPSE".  THE TARGET IS NOT WHAT
THE ROW SAYS IT IS, AND THE NATURALNESS ARGUMENT THE PAPERS OFFER FOR IT DESCRIBES A DIFFERENT EPOCH.

Two findings, and the second is the sharp one.

  ** (1) $\\rho_r/\\rho_m$ AT ONSET IS NOT A DATUM DISTINCT FROM $\\eta$.  On any thermal history it is
  $\\eta$, the matter-to-baryon ratio, and the TEMPERATURE, combined -- and this cosmology inherits the
  first two anyway.  So P7's *"the frontier is two data and not one"* OVER-COUNTS: what the handover
  supplies is ONE composition datum, and $\\rho_r/\\rho_m\\approx2$ is the FITTED onset restated. **

  ** (2) AND THE NATURALNESS ARGUMENT POINTS AT THE WRONG EPOCH BY NINE ORDERS OF MAGNITUDE.  The
  papers argue that complete collapse liberates binding energy of order the rest mass, so *"a
  handover carrying radiation of order the matter density is the natural scale"*.  But
  $\\rho_r=\\rho_m$ happens at $T\\simeq0.8\\,$eV, and P7 puts the handover four orders ABOVE the
  deuterium bottleneck -- about $700\\,$MeV -- which is nine orders hotter still. **  *At the handover
  the ratio is $\\sim9\\times10^{8}$, and a collapse delivering "radiation of order the matter density"
  there would mean $\\eta\\simeq0.5$: no light elements and no acoustic peaks.*

  PART 1  ** THE IDENTITY: $\\rho_r/\\rho_m$ is $\\eta$ and $T$, computed and checked against the datum. **
  PART 2  ** SO THE TWO DATA ARE ONE DATUM AND ONE FITTED PARAMETER. **
  PART 3  ** WHERE "RADIATION OF ORDER THE MATTER DENSITY" ACTUALLY LIVES. **
  PART 4  ** WHAT THE COLLAPSE MUST ACTUALLY DELIVER, AND WHY IT IS THE $\\eta$ QUESTION. **
  PART 5  What `L-150` becomes.

Run: python3 L150w_the_two_data_are_one.py
"""
import math
import os

print(__doc__.split("Run:")[0])
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
claim = 'The frontier is two data and not one'
print(f"  P7 currently states: '{claim}' -- present in the paper: ** {claim in p7} **")
print("  and glosses them as *the radiation amplitude* (the acoustic spacing) and *eta* (the")
print("  abundances and the peak heights), calling them 'distinct data of the same handover'.")
assert claim in p7
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
print("PART 5 — WHAT `L-150` BECOMES")
print("=" * 78)
for s in [
 "⇒ ** `L-150` DOES NOT STRIKE: the derivation it asks for is genuinely open. **  *What changes is",
 "   what it is asking for, and it changes twice over.*",
 "",
 "① ** ITS TARGET IS $T_{\\mathrm{onset}}$ (equivalently $z_{\\mathrm{onset}}$), NOT THE RATIO. **",
 "   *Given the inherited $\\eta$ and matter content, the ratio at onset IS the onset.  `E·4` reached",
 "   the same place from the $H_0$ side; this reaches it from the thermodynamic side.*",
 "② ** ITS SECOND HALF IS THE $\\eta$ QUESTION, AND THE PAPERS' NATURALNESS ARGUMENT FOR IT IS",
 "   MISDIRECTED. **  *'Order unity, not the small tuned value $\\eta$ takes' contrasts a quantity",
 "   with itself read at another temperature.  What the collapse must explain is the small value.*",
 "",
 "✔ ** AND ONE THING GETS SMALLER RATHER THAN LARGER: P7's *'the frontier is two data and not one'*",
 "   is corrected to ONE inherited datum plus ONE fitted parameter. **  *A corpus that counts its",
 "   own debts should not over-count them either.*",
]:
    print("  " + s)
