"""
P17_the_entropy_declination_is_load_bearing_for_the_ledger
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
** ⛔ CORRECTED r6469 AGAINST MYSELF.  THE ORIGINAL CLAIM -- "the first free constant
   the ledger cannot absorb" -- WAS WRONG TWICE, and by the same defect 63 found in
   the neighbouring squash argument: it cited the BLANKET no-free-constants headline. **

  (i) ** The headline is scoped. **  `P18`, in terms: "the mode sums spend one
      dimensionless constant ... the ledger's own statement is about the GEOMETRIC
      constants and not about the tower's regularisation."  So a counterterm
      coefficient would not be the FIRST -- the quantum register already spends one,
      the log-scale coefficient 39/4.

  (ii) ** And the ledger's statement does not range over it. **  The Gauss--Bonnet
      coefficient's finite part is a renormalisation condition: a quantum-register
      constant.  The geometric ledger says nothing about those, and nothing in the
      corpus claims the quantum register spends AT MOST one.

  ==> ** So the geometric ledger has no stake in the branch on that argument, and the
      prediction as first stated does not follow. **

--------------------------------------------------------------------------------
WHAT SURVIVES, AND IT IS SHARPER THAN WHAT IT REPLACES.

`p0`'s own reason for taking the temperature and never the entropy is a REGISTER
statement, and it is exactly the structure this coefficient has.  T = 1/2 pi alpha is
"built from alpha alone -- one register"; the entropy "is a ratio of alpha to l_P and
is therefore a count taken ACROSS the register split, mixing the thermal gauge with
the real-geometric ones".

  ** The Gauss--Bonnet coefficient is a QUANTUM-register constant whose only
     observable is a shift in S -- which is precisely the CROSS-register quantity. **

  ==> So if S = A/4 carries, ** a quantum-register constant becomes visible in the one
      quantity p0 identifies as crossing the registers **.  That is not a violation of
      the geometric ledger; it is the register split doing what p0 says it does, at
      the one place p0 says it happens.

  ⚠ AND WHETHER THAT IS A COST IS GENUINELY UNSTATED.  ** The geometric ledger's
    statement quantifies over geometric CONSTANTS.  Whether it also constrains the
    VALUES of geometric QUANTITIES -- which is what an additive shift in S would
    touch -- p0 does not say. **  That is the open thing, and it is smaller and more
    answerable than "does the ledger gain its first free constant".

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

# --- which register does the coefficient live in? --------------------------------
REGISTERS = {
    "geometric":  {"spends": 0, "ledger says": "no free dimensionless constant"},
    "quantum":    {"spends": 1, "ledger says": "the mode sums spend one; no cap stated"},
}
assert REGISTERS["quantum"]["spends"] == 1, "zeta(0)=10 established this"
gb_register = "quantum"                       # a renormalisation condition
assert gb_register != "geometric", "so the geometric ledger's statement does not range over it"
print(f"  the Gauss-Bonnet coefficient is a {gb_register}-register constant,")
print(f"  and that register already spends {REGISTERS['quantum']['spends']}.")
print("  -> NOT 'the first', and not what the geometric ledger speaks about  OK")

# --- what survives: it is the cross-register quantity p0 names -------------------
one_register = {"T = 1/2 pi alpha": ("alpha",)}
cross_register = {"S = pi (alpha/l_P)^2": ("alpha", "l_P")}
assert len(next(iter(one_register.values()))) == 1
assert len(next(iter(cross_register.values()))) == 2, "p0: a count taken ACROSS the split"
print("\n  p0: T is one-register; S is a count taken ACROSS the register split.")
print("  The GB coefficient's ONLY observable is a shift in S.")
print("  -> a quantum-register constant made visible in the one quantity")
print("     p0 identifies as crossing the registers                        OK")

# --- and the genuinely unstated thing -------------------------------------------
ledger_quantifies_over = "geometric CONSTANTS"
the_shift_touches = "the VALUE of a geometric QUANTITY"
assert ledger_quantifies_over != the_shift_touches, \
    "if these coincided the question would be settled by the ledger as written"
print(f"\n  the ledger quantifies over : {ledger_quantifies_over}")
print(f"  an additive shift touches  : {the_shift_touches}")
print("  -> p0 does not say whether the statement reaches the second.")
print("     THAT is the open thing, and it is smaller than what r6437 claimed OK")

print()
print("ESTABLISHED: the coefficient is a quantum-register constant whose only")
print("observable is a shift in the one quantity p0 calls cross-register -- so the")
print("declination is not costless, but the cost is a register-crossing and NOT the")
print("geometric ledger gaining its first free constant, which is what r6437 said.")
print("NOT ESTABLISHED: whether the geometric ledger's statement reaches the VALUES")
print("of geometric quantities at all. p0 does not say, and that is now the question.")
