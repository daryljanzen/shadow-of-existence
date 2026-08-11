import sympy as sp

print("="*78)
print("REPRESENTATIONAL READING: the graviton H_phys in the Nariai OBSERVER frame")
print("(dS-null bundle), where the M!=0 matter bend enters. Same ontological tower,")
print("projected from the background geometry into what a real observer sees.")
print("="*78)

tau, al, M, k, A = sp.symbols('tau alpha M k A', positive=True)
# Representational (observer) scale factor = the areal radius r(tau) = flat-LCDM:
a = (2*M*al**2)**sp.Rational(1,3) * sp.sinh(3*tau/(2*al))**sp.Rational(2,3)
print("\n[0] Observer-frame scale factor (the areal radius, fundamental/reassigned-ruling):")
print("    a(tau) = (2M alpha^2)^{1/3} sinh^{2/3}(3 tau / 2 alpha)   (flat-LCDM)")

# --- [1] the matter bend appears in the Friedmann background ---
H = sp.simplify(sp.diff(a,tau)/a)
H2 = sp.simplify(H**2)
print("\n[1] Friedmann readout (the BEND): H^2 = (adot/a)^2 =")
print("    H^2 =", H2)
bend = sp.simplify(H2 - (2*M/a**3 + 1/al**2))
print("    H^2 - (2M/a^3 + 1/alpha^2) =", bend, "  (0 => H^2 = 2M/a^3 + 1/alpha^2)")
print("    => MATTER bend 2M/a^3 (dust, ~a^-3) + dark energy 1/alpha^2 (Lambda/3).")
print("    Contrast BACKGROUND geometry a_bg=alpha cosh(T/a): H_bg^2 = tanh^2/alpha^2 -> 1/alpha^2")
print("    (PURE Lambda, NO matter). The matter bend is the REPRESENTATIONAL difference.")

# --- [2] the graviton H_phys in the observer frame: same deparametrized structure ---
phi = sp.Function('phi')(tau); pi = sp.Function('pi')(tau)
print("\n[2] Graviton mode in the observer frame (flat slices -> continuous k):")
L = sp.Rational(1,2)*a**3*(sp.diff(phi,tau)**2 - (k**2/a**2)*phi**2)
EL = sp.simplify(sp.expand(( sp.diff(sp.diff(L,sp.diff(phi,tau)),tau) - sp.diff(L,phi) )/a**3))
target = sp.diff(phi,tau,2) + 3*H*sp.diff(phi,tau) + (k**2/a**2)*phi
print("    mode eqn residual vs  phidd + 3H phidot + (k^2/a^2) phi =", sp.simplify(EL-target))
print("    H_phys = pi^2/(2a^3) + (a k^2/2) phi^2 ;  i d/dtau Psi = H_phys^hat Psi (unitary).")
print("    SAME deparametrized structure as the background (r248); the bend is now IN a(tau).")

# --- [3] the graviton frequency carries the bend ---
print("\n[3] Graviton frequency omega_k^2(tau) = k^2/a(tau)^2 evolves THROUGH the bend:")
print("    early (a~tau^{2/3}, matter-dominated): omega_k^2 ~ k^2 tau^{-4/3} (the dust bend);")
print("    late  (a~e^{tau/alpha}, Lambda-dominated): omega_k^2 ~ k^2 e^{-2tau/alpha} (frozen).")
print("    The observer's graviton spectrum is the flat-LCDM primordial GW spectrum.")

print("\n" + "="*78)
print("VERDICT: the representational reading CLOSES the arc.")
print(" - The same ontological graviton tower, projected into the Nariai observer frame,")
print("   is the graviton on flat-LCDM a(tau)=sinh^{2/3} -- deparametrized, unitary (as r248).")
print(" - The M!=0 MATTER BEND enters exactly as P7 says it must: as the bend of the")
print("   slicing (2M/a^3 in H^2), the representational difference from the pure-Lambda")
print("   background (cosh). Matter is a feature of the projection, not the ontology.")
print(" - Mode content: DISCRETE S^3 tower (background, global/compact, the ontological")
print("   spectrum) reads as CONTINUOUS k (observer, local non-compact horosphere patch) --")
print("   the two slicings of r246's one congruence; consistent, not in tension.")
print("Open (unchanged): explicit S^3 spectrum mu_n^2 & the discrete->continuous restriction")
print("map; TT action from EH (used, not re-derived); self-adjointness/ordering.")
