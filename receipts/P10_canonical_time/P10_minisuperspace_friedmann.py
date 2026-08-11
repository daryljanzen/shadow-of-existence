"""
P10_minisuperspace_friedmann.py -- verifies sec:deparam's concrete illustration: in flat FL minisuperspace,
  the deparametrized true Hamiltonian Hphys(a,p_a) = (2pi/3) p_a^2/a - (Lambda/8pi) a^3 generates, via
  Hamilton's equations, the Friedmann equation. On the constraint p_tau + Hphys = 0, Hphys equals the
  conserved comoving dust energy E_d, and eliminating p_a gives (adot/a)^2 = (8pi/3) rho_d/a^3 + Lambda/3.
  So the deparametrized structure is not empty: it reproduces standard cosmology. [P10 canonical_time sec:deparam]
STATUS: ✔✔   RUN: python3 P10_minisuperspace_friedmann.py   RUNTIME: ~2s
COMPUTES: Hamilton's equation adot=dHphys/dp_a=4pi p_a/3a; Hphys autonomous => conserved (=E_d); eliminating
  p_a from Hphys=E_d yields the Friedmann equation with dust (rho_d/a^3) and Lambda/3. CONTROL: a wrong sign
  on the Lambda term flips the cosmological-constant contribution.
ORIGIN: built new r1370 (P10 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
a,p_a,Lam,tau,Ed=sp.symbols('a p_a Lambda tau E_d', positive=True)
adot=sp.Symbol('adot', positive=True)
Hphys=(2*sp.pi/3)*p_a**2/a - (Lam/(8*sp.pi))*a**3
print("="*70); print("P10 minisuperspace deparametrization -> Friedmann equation"); print("="*70)
# (1) Hamilton's equation for adot
adot_eq=sp.simplify(sp.diff(Hphys,p_a))
ok&=check("Hamilton: adot = dHphys/dp_a = 4 pi p_a/(3a)", sp.simplify(adot_eq-4*sp.pi*p_a/(3*a))==0)
# (2) Hphys is autonomous (no explicit tau) => conserved along the flow (= E_d, the comoving dust energy)
#     dHphys/dtau = dH/da * adot + dH/dp_a * p_adot ; with p_adot=-dH/da this is identically 0
padot=-sp.diff(Hphys,a)
dH=sp.simplify(sp.diff(Hphys,a)*sp.diff(Hphys,p_a) + sp.diff(Hphys,p_a)*padot)
ok&=check("Hphys autonomous => conserved on-shell: dHphys/dtau = 0 (equals the comoving dust energy E_d)", sp.simplify(dH)==0)
# (3) eliminate p_a: from adot=4pi p_a/3a -> p_a=3 a adot/(4pi); set Hphys=E_d and derive Friedmann
p_a_of=3*a*adot/(4*sp.pi)
Hphys_on=Hphys.subs(p_a, p_a_of)
fried=sp.simplify(sp.Eq(Hphys_on, Ed))
# solve for (adot/a)^2
lhs=sp.simplify(Hphys_on)            # = (adot/a)^2 * (3 a^3/(8pi)) - (Lam/8pi)a^3   ... check
target=sp.simplify((3*a**3/(8*sp.pi))*(adot/a)**2 - (Lam/(8*sp.pi))*a**3)
ok&=check("Hphys(a, p_a=3a adot/4pi) = (3 a^3/8pi)(adot/a)^2 - (Lam/8pi) a^3", sp.simplify(lhs-target)==0)
# Hphys=E_d  =>  (adot/a)^2 = (8pi/3) E_d/a^3 + Lambda/3
sol=sp.solve(sp.Eq(lhs, Ed), adot)
H2=sp.simplify((sol[0]/a)**2)         # (adot/a)^2
ok&=check("=> (adot/a)^2 = (8pi/3) E_d/a^3 + Lambda/3  (Friedmann; E_d=rho_d comoving dust energy)",
          sp.simplify(H2 - ((8*sp.pi/3)*Ed/a**3 + Lam/3))==0)
# (4) dust scaling: E_d comoving-constant => physical density rho = E_d/a^3 ~ a^-3 (pressureless dust)
rho_phys=Ed/a**3
ok&=check("dust: physical density rho = E_d/a^3 scales as a^-3 (pressureless), Lambda term constant",
          sp.simplify(sp.diff(sp.log(rho_phys),a)*a + 3)==0)
# CONTROL: flipping the Lambda sign in Hphys flips the cosmological term
Hphys_bad=(2*sp.pi/3)*p_a**2/a + (Lam/(8*sp.pi))*a**3
lhs_bad=Hphys_bad.subs(p_a,p_a_of); H2_bad=sp.simplify((sp.solve(sp.Eq(lhs_bad,Ed),adot)[0]/a)**2)
ok&=check("CONTROL: wrong sign on the Lambda term gives (adot/a)^2 = (8pi/3)E_d/a^3 - Lambda/3 (flipped)",
          sp.simplify(H2_bad-((8*sp.pi/3)*Ed/a**3 - Lam/3))==0)
print("="*70)
print("RESULT:", "ALL PASS -- the deparametrized minisuperspace Hamiltonian reproduces the Friedmann equation\n         (adot/a)^2=(8pi/3)rho_d/a^3+Lambda/3 via Hamilton's equations: the true-Hamiltonian structure is real, not empty." if ok else "SOME FAILED")
print("="*70)

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  (a) the PASS/FAIL flag the file previously only PRINTED.
# (b) the two Friedmann coefficients the deparametrized Hphys actually produces, read off
# the solved (adot/a)^2: the dust term carries 8pi/3 and the Lambda term carries 1/3 --
# i.e. (adot/a)^2 = (8pi/3) E_d/a^3 + Lambda/3, the standard-cosmology numbers sec:deparam
# claims.  (A 4pi/3, or a Lambda/8pi, would mean the deparametrization mis-normalises.)
assert ok, "P10 minisuperspace: at least one check FAILED"
assert sp.simplify(H2.coeff(Ed)*a**3 - 8*sp.pi/3) == 0, "dust coefficient is %s, not 8pi/3" % sp.simplify(H2.coeff(Ed)*a**3)
assert sp.simplify(H2.coeff(Lam) - sp.Rational(1, 3)) == 0, "Lambda coefficient is %s, not 1/3" % sp.simplify(H2.coeff(Lam))
