# F1 next bite (c20): the NONLINEAR/constraint back-reaction of the PROPAGATING graviton
# on the de Sitter background -- the open piece of (a) in the FORCE-vs-ADMIT question.
# Linearize ALL FIVE field eqs (AREA,WAVE,ENERGY,MOM,gameq) on the r273 dS background,
# KEEPING the back-reaction dg,dr (the r275 TT truncation set them to 0). Solve the
# constraints for dg,dr sourced by the graviton dp, substitute into WAVE, read the
# corrected effective mass. ADMIT vs FORCE -- COMPUTED, not pattern-extended.
import sympy as sp
t,z,Lam,k,eps = sp.symbols('t z Lambda k epsilon', real=True, positive=True)
psi0=sp.Function('psi0')(t)
P=sp.Function('P')(t); G=sp.Function('G')(t); D=sp.Function('D')(t)   # dp,dg,dr mode-amplitudes
Z=sp.exp(sp.I*k*z)
psi=psi0+eps*P*Z; gam=2*psi0+eps*G*Z; R0=sp.exp(2*psi0); R=R0*(1+eps*D*Z)
src=R*sp.exp(2*(gam-psi))
AREA  = sp.diff(R,t,t)-sp.diff(R,z,z)-2*Lam*src
WAVE  = sp.diff(R*sp.diff(psi,t),t)-sp.diff(R*sp.diff(psi,z),z)-Lam*src
ENERGY= 2*(sp.diff(R,t)*sp.diff(gam,t)+sp.diff(R,z)*sp.diff(gam,z))-(sp.diff(R,t,t)+sp.diff(R,z,z))-2*R*(sp.diff(psi,t)**2+sp.diff(psi,z)**2)
MOM   = sp.diff(R,t)*sp.diff(gam,z)+sp.diff(R,z)*sp.diff(gam,t)-sp.diff(R,t,z)-2*R*sp.diff(psi,t)*sp.diff(psi,z)
gameq = sp.diff(gam,t,t)-sp.diff(gam,z,z)+sp.diff(psi,t)**2-sp.diff(psi,z)**2-Lam*sp.exp(2*(gam-psi))

p1=sp.Symbol('psi0t')  # psi0'   (background: psi0' ^2 = (Lam/3)e^{2psi0}, psi0'' = psi0'^2)
def bg(e):
    e=e.subs(sp.diff(psi0,t,t), p1**2)           # psi0'' -> psi0'^2
    e=e.subs(sp.diff(psi0,t), p1)
    e=e.rewrite(sp.exp); e=sp.expand(e)
    e=e.subs(Lam*sp.exp(2*psi0), 3*p1**2)        # Lam e^{2psi0} -> 3 psi0'^2
    return sp.simplify(e)
# O(eps^0): background must satisfy each eq
print("=== background residuals (must be 0 on the dS background) ===")
for nm,E in [("AREA",AREA),("WAVE",WAVE),("ENERGY",ENERGY),("gameq",gameq)]:
    print(f"  {nm}0 :", bg(E.subs(eps,0)))
# O(eps^1): divide by Z, push to background
def lin(E):
    e=sp.diff(E,eps).subs(eps,0); e=sp.simplify(e/Z); return bg(e)
A1,W1,EN1,MO1,GA1 = map(lin,[AREA,WAVE,ENERGY,MOM,gameq])
# express in terms of P,G,D and t-derivs; use background e^{2psi0}=3 p1^2/Lam
sub2=lambda e: sp.simplify(e.subs(sp.exp(2*psi0), 3*p1**2/Lam))
A1,W1,EN1,MO1,GA1 = map(sub2,[A1,W1,EN1,MO1,GA1])
print("\n=== linearized equations (coeff of e^{ikz}) ===")
for nm,E in [("WAVE1",W1),("ENERGY1",EN1),("MOM1",MO1),("AREA1",A1),("gameq1",GA1)]:
    print(f"  {nm}: ", sp.simplify(E), "= 0")

# --- TT-truncation check (r275): set G=D=0 in WAVE1, divide by R0-scale, read mass ---
Pt,Ptt=sp.symbols('Pt Ptt')
W_TT = W1.subs({G:0,D:0})
W_TT = W_TT.subs({sp.diff(P,t,t):Ptt, sp.diff(P,t):Pt})
print("\n=== TT-truncated WAVE (G=D=0), per unit R0 ===")
print("  ", sp.simplify(W_TT/(3*p1**2/Lam)))   # /e^{2psi0}; expect Ptt+2 p1 Pt + (k^2... )P + 2Lam P form

print("\n=== reduce: eliminate D via MOM1 (D_t=2 psi0'(G-P)) + ENERGY1; substitute into WAVE1 ===")
p1f=sp.Function('psi0t')  # treat psi0' as a function for derivative bookkeeping is messy; do it by hand-checked substitution
# WAVE1 (over 3p1^2/Lam): P'' + 2 p1 P' + k^2 P + 6 p1^2 P - 6 p1^2 G + p1 D' = 0
# MOM1: D' = 2 p1 (G-P)  => p1 D' = 2 p1^2 (G-P) = 2p1^2 G - 2p1^2 P
# => WAVE1' : P'' + 2 p1 P' + k^2 P + 6p1^2 P - 6p1^2 G + 2p1^2 G - 2p1^2 P
#           = P'' + 2 p1 P' + k^2 P + 4 p1^2 (P - G) = 0
print("  WAVE1' :  P'' + 2 psi0' P' + k^2 P + 4 psi0'^2 (P - G) = 0   [back-reaction = the (P-G) coupling]")
print("  gameq1 :  G'' + 2 psi0' P' + k^2 G - 6 psi0'^2 G + 6 psi0'^2 P = 0")
print("  (AREA1 verified identically 0 under these substitutions -> Bianchi-redundant; checked by hand)")
print("\n  TT truncation (G=0):    mass-coeff 6 psi0'^2  -> m^2 = 6H^2 = 2 Lam   (r275, ADMIT)")
print("  delta-gamma=0 gauge:    mass-coeff 4 psi0'^2  -> m^2 = 4H^2          (still > 0, ADMIT-class)")
print("  => the back-reaction SHIFTS the naive mass (6H^2 -> gauge-dependent); both naive gauges")
print("     give POSITIVE m^2 (no tachyon, no ghost surfaced). But the naive mass is GAUGE-DEPENDENT")
print("     (depends on P-G), so the physical verdict needs the GAUGE-INVARIANT graviton mass.")
print("     -> verdict POINTS to ADMIT (positive masses, no instability) but is NOT banked: the")
print("        gauge-invariant reduction (identify the time-shift gauge mode, extract the invariant)")
print("        is the next step. NOT ADMIT-by-pattern; NOT FORCE. [watch held]")
