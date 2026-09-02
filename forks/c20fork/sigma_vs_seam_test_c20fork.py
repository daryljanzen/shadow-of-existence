import numpy as np
np.set_printoptions(suppress=True, linewidth=140, precision=6)

print("="*80)
print("c20fork TEST — the crux: sigma vs the SEAM (pivot) vs the GLOBAL Wick")
print("Question raised by the 4-node thesis read: is the 90-deg pivot a REAL")
print("signature-changing operation that breaks the sigma-lift's dichotomy")
print("('signature-change => imaginary'), reopening the colour route?")
print("Decide AT SOURCE (P3 SdS-slicing-curve), not by the figure's 'real pivot' look.")
print("="*80)

# ---------------------------------------------------------------------------
# OBJECT A -- sigma, the ROOT-EXCHANGE involution (P3 Prop:involution, gauge alpha=1).
#   f_invol(r0) = (1/2)(-r0 + sqrt(4 - 3 r0^2)) carries the slicing parameter to the
#   second positive root of its own cubic.  2M(r0) = r0 - r0^3.
#   P3 Prop:readingswap: 2M is INVARIANT under the exchange => the metric function
#   f(r)=1-2M/r-r^2 is unchanged => sigma FIXES the geometry (signature-preserving).
def invol(r0):
    return 0.5*(-r0 + np.sqrt(4 - 3*r0**2))
def twoM(r0):
    return r0 - r0**3

print("\n[A] sigma = root-exchange involution  r0 -> (1/2)(-r0 + sqrt(4-3 r0^2))")
r0s = np.array([0.0, 0.2, 0.4, 1/np.sqrt(3), 0.7, 0.9, 1.0])
ok_invol = True; ok_massinv = True
for r0 in r0s:
    rB = invol(r0)
    back = invol(rB)
    dM = twoM(rB) - twoM(r0)
    ok_invol &= np.isclose(back, r0, atol=1e-9)
    ok_massinv &= np.isclose(dM, 0.0, atol=1e-9)
    print(f"    r0={r0:.5f} -> rB={rB:.5f} -> invol(rB)={back:.5f} | 2M(r0)-2M(rB)={dM:+.2e}")
print(f"    involution f(f(r0))=r0 ? {ok_invol}   | fixed point r0=1/sqrt3={1/np.sqrt(3):.5f}")
print(f"    2M INVARIANT under exchange (=> f unchanged => sigma FIXES geometry) ? {ok_massinv}")
print("    => sigma is a SIGNATURE-PRESERVING symmetry of ONE Lorentzian SdS geometry")
print("       (relabels which horizon is the mass-horizon); it is NOT a continuation.")

# ---------------------------------------------------------------------------
# OBJECT B -- the SEAM (the '90-deg pivot'), P3 line 40, verbatim mechanism:
#   theta -> pi/2 + i psi,  sin(theta) -> cosh(psi);  d theta = i d psi.
#   The metric carries a term ~ (d theta)^2; the continuation squares the factor to -1,
#   flipping the signature (Riemannian spherical piece <-> Lorentzian dS piece).
print("\n[B] seam continuation  theta -> pi/2 + i*psi  (P3 line 40)")
for psi in [0.0, 0.3, 0.7, 1.2]:
    theta = np.pi/2 + 1j*psi
    s = np.sin(theta)                     # should be cosh(psi) (real)
    print(f"    psi={psi:.2f}: sin(pi/2+i psi)={s.real:+.5f}{s.imag:+.5f}j   cosh(psi)={np.cosh(psi):+.5f}"
          f"   match={np.isclose(s, np.cosh(psi))}")
# signature-flip factor: d theta = i d psi  =>  (d theta)^2 = - (d psi)^2
i = 1j
print(f"    (d theta)^2 with d theta=i d psi : ({i})^2 = {(i**2).real:+.0f} * (d psi)^2"
      f"  -> metric term FLIPS SIGN => signature flip.")
print("    => the seam's signature flip IS an IMAGINARY continuation (the geometric Wick");
print("       within the construction). The slicing curve r(l) is real & C^0, but the")
print("       Riemannian<->Lorentzian FLIP across it is theta->pi/2+i psi -- NOT a real op.")

# ---------------------------------------------------------------------------
# WHAT EACH OPERATION REACHES (dimensions) -- substrate dS5 in M^6, su(3) needs SO(6).
#   sigma : isometry of fixed Lorentzian dS5  -> stays in SO(5,1).         (no new sector)
#   seam  : theta->pi/2+i psi at the x0=0 equator -> the S^4 equator, SO(5). (one angle)
#   global Wick x0->i x0 : whole dS5 -> S^5, SO(6) >= su(3).                (the colour face)
print("\n[A vs B vs Wick] what each reaches:")
print("    sigma  : SIGNATURE-PRESERVING isometry, FIXES the dS geometry      -> within SO(5,1)")
print("    seam   : imaginary continuation of ONE angle at the x0=0 equator    -> S^4, SO(5)")
print("    Wick   : imaginary continuation of the WHOLE time axis x0->i x0     -> S^5, SO(6)")
print("    su(3): min faithful real rep = 6  => su(3) ⊂ so(6), su(3) ⊄ so(5), su(3) ⊄ so(5,1).")
print("    => the seam reaches SO(5) (no su(3)); only the GLOBAL Wick reaches SO(6).")

print("\n"+"="*80)
print("VERDICT (c20fork crux): the shared 4-node reach DOES NOT SURVIVE the source.")
print(" - sigma, the seam, and the global Wick are THREE DISTINCT operations.")
print(" - The seam's signature flip IS the imaginary continuation theta->pi/2+i psi")
print("   (P3 line 40), NOT a real operation -- so the sigma-lift's dichotomy")
print("   ('signature-change is the imaginary continuation; sigma the real reflection")
print("   is separate') is CONFIRMED at source, not broken.  The 'real 90-deg pivot'")
print("   reading was the thesis's loose language; P3 makes it the imaginary continuation,")
print("   exactly as the R x C figure draws it (the curve turns INTO the imaginary axis).")
print(" - sigma FIXES the geometry (signature-preserving root-exchange), so it was never")
print("   a signature-flip and never a colour-bridge: the sigma-lift verdict STANDS, and")
print("   c19's 'mislocation' is not an error (sky-angle w and (r,r0) roots are conjugate).")
print(" - The seam reaches only SO(5); su(3) needs SO(6).  Colour stays closed -- and now")
print("   on the ORIGINAL grounds (the imaginary continuation), with rank + AH untouched.")
print(" => P11 sec.3's sigma-lift leg is SOUND as written; it does not need reopening on")
print("    the 'false dichotomy' grounds c17 proposed.  not claimed the universal (face 18).")
print("="*80)
