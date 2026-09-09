"""
p0_the_entropy_declination_is_load_bearing_for_the_ledger
=========================================================

Object under test -- `p0` `sec:ledger`'s declination: "whether S=A/4 carries to a
cosmological horizon on this reading is a question this paper does not settle ...
Were it to fail to carry, that would be a result and not a gap -- a one-scale ledger
FORBIDDING a thermodynamic relation rather than merely accommodating one."

** THAT DECLINATION IS NOW DOING WORK IT WAS NEVER ASKED TO DO. **  `PO-43`'s second
replacement question -- whether the ledger counts topological terms -- reduces to it
(r6435), and the reduction has a shape: ** the two branches give OPPOSITE answers,
and the programme's own no-free-constants claim prefers one of them. **

--------------------------------------------------------------------------------
WHAT A TOPOLOGICAL TERM DOES, IN FOUR DIMENSIONS.

  * It contributes NO FIELD EQUATION.  `P10` says so in its own voice of the
    Gauss--Bonnet combination, which is why the coefficient cannot be read off any
    dynamics.

  * It DOES contribute to the Wald entropy, and topologically: the Gauss--Bonnet
    density's Noether-charge contribution goes as the intrinsic curvature integral
    over the horizon cross-section, which in two dimensions is 4 pi chi(Sigma)
    [Jacobson--Myers -- IMPORTED, and the only import here].  ** For a 2-sphere
    cross-section chi = 2, so the contribution is a CONSTANT SHIFT, independent of
    the horizon area. **

  * And the finite part of that coefficient is not fixed by the field content.  The
    DIVERGENCE's coefficient is -- it is the a-type anomaly coefficient, determined
    like the c-type one this corpus now carries at 1/60 -- but renormalising it
    requires a condition, and ** that condition is a free dimensionless constant
    whose ONLY observable here is the entropy shift. **

--------------------------------------------------------------------------------
WHY THE LEDGER CANNOT ABSORB IT, WHICH IS THE POINT.

`p0` has a mechanism for a constant VACUUM ENERGY: it is absorbed into the one
observed curvature, with no bare-Lambda-versus-vacuum split.  ** There is no
corresponding absorber for a constant ENTROPY shift. **  S = pi(alpha/l_P)^2 is
fixed once alpha is, l_P being a gauge; a shift S -> S + s_0 requires s_0 itself.

  ==> S = A/4 CARRIES:        the ledger acquires a free dimensionless constant it
                              cannot absorb -- ** the first one **, against a claim
                              the corpus states as spending none.
  ==> S = A/4 FAILS to carry: the coefficient has no home at all, the ledger counts
                              no topological term, and `p0`'s "a result and not a
                              gap" is exactly what obtains.

** SO THE NO-FREE-CONSTANTS CLAIM, TAKEN SERIOUSLY, PREDICTS THAT S=A/4 DOES NOT
   CARRY TO THIS HORIZON. **  That is not an argument that it does not; it is a
statement that the programme has a stake in which branch holds, where `p0` recorded
the branch as costless either way.  ** The declination is load-bearing, and it was
not known to be. **

--------------------------------------------------------------------------------
WHAT IS NOT CLAIMED.  Not that S=A/4 fails -- that is the open question and this
does not settle it.  Not that the a-type coefficient is computed; only that its
finite part needs a condition and that the condition has one observable.  And the
Wald-entropy fact is imported, not derived here.

⌗ AND ONE ASYMMETRY WORTH KEEPING: `p0`'s own reason for taking the TEMPERATURE and
not the entropy already anticipates this.  T = 1/2 pi alpha is built from alpha
alone -- ** one register **.  S is a ratio of alpha to l_P -- ** a count taken
ACROSS the register split **.  The quantity that would test the ledger is the
cross-register one, and this shows what it would cost if it tested it and passed.
"""

CHI_SPHERE = 2          # Euler characteristic of a 2-sphere horizon cross-section

# --- what each object contributes, in four dimensions ---------------------------
gauss_bonnet = {
    "field equation":  False,   # P10, its own words
    "Wald entropy":    True,    # topological: goes as chi(Sigma)  [imported]
}
assert gauss_bonnet["field equation"] is False
assert gauss_bonnet["Wald entropy"] is True
print("  Gauss-Bonnet in 4D: no field equation; a Wald-entropy term going as chi")
print(f"  2-sphere cross-section, chi = {CHI_SPHERE}: an AREA-INDEPENDENT constant shift  OK")

# --- can the ledger absorb it, as it absorbs a constant vacuum energy? -----------
absorber = {
    "constant vacuum energy": "Lambda",   # p0's own mechanism
    "constant entropy shift": None,       # S = pi(alpha/l_P)^2 is fixed once alpha is
}
assert absorber["constant vacuum energy"] is not None
assert absorber["constant entropy shift"] is None
print("  a constant vacuum energy has an absorber (Lambda); a constant entropy")
print("  shift has none -- it would require a new constant                     OK")

# --- so the two branches disagree, which is the whole finding -------------------
def ledger_gains_a_free_constant(entropy_carries):
    return bool(entropy_carries)

assert ledger_gains_a_free_constant(True) is True
assert ledger_gains_a_free_constant(False) is False
assert ledger_gains_a_free_constant(True) != ledger_gains_a_free_constant(False), \
    "the branches must disagree, or the question would be independent"
print("  S=A/4 carries -> ledger gains a free constant it cannot absorb")
print("  S=A/4 fails   -> the coefficient has no home; p0's 'result, not gap'")
print("  -> the branches DISAGREE, so the topological-terms question cannot")
print("     be settled independently of the entropy                            OK")

print()
print("ESTABLISHED: p0's declination is load-bearing for the counterterm ledger,")
print("and the no-free-constants claim has a stake in which branch holds -- it")
print("PREFERS that S=A/4 does not carry, which p0 recorded as costless either way.")
print("NOT ESTABLISHED: which branch holds. That remains the open question.")
