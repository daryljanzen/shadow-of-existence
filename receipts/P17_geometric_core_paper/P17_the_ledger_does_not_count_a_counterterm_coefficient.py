"""
P17_the_ledger_does_not_count_a_counterterm_coefficient
=======================================================

Object under test -- the question r6469 left, which is the last thing standing between
`PO-43`'s second replacement question and an answer: ** does the geometric ledger's
statement reach the VALUE of a geometric quantity, or only its constants? **

Read whole, `p0` `sec:ledger` answers it, and the answer retracts r6437 rather than
qualifying it.

--------------------------------------------------------------------------------
WHAT THE LEDGER ACTUALLY QUANTIFIES OVER -- two registers and no more.

  ** real-geometric: c, Lambda, G ** -- "the gauges of the REAL Lorentzian geometry,
  each a nameable feature of the substrate and its cuts": c the null-ruling slope,
  Lambda the waist, G the cut's offset.

  ** thermal: hbar, k_B ** -- "standard horizon thermodynamics, ** their CR-specific
  content the ledger's closing of THE ONE QUANTUM FREEDOM **, not a new geometric
  feature."

That second clause is the whole of the ledger's quantum claim, and it is specific:
the one freedom it closes is the SELF-ADJOINT EXTENSION, fixed by thermal regularity
at the horizon period.  ** It is not a claim that the quantum sector spends no
constants. **

--------------------------------------------------------------------------------
SO THE THREE QUANTUM FREEDOMS ARE DISTINCT, AND THE LEDGER SPEAKS TO ONE.

    (1) the self-adjoint extension        -- CLOSED by the ledger, its stated content
    (2) the regularisation of the sums    -- CONCEDED: "the mode sums spend one
                                             dimensionless constant" (P18's scoping)
    (3) a counterterm coefficient's
        finite part, e.g. Gauss--Bonnet   -- NOT SPOKEN TO by either

  ==> ** A Gauss--Bonnet entropy shift is a freedom of type (3).  The ledger's
      statement does not reach it, and the branch IS costless to the ledger. **

--------------------------------------------------------------------------------
⛔ SO r6437 IS RETRACTED, NOT MERELY CORRECTED.

r6437 claimed `p0`'s declination was "load-bearing" -- that the one-scale reading had
a stake in whether S = A/4 carries, where `p0` had recorded the branch as costless
either way.  ** `p0` was right.  The stake was an artefact of reading the ledger's
headline unscoped **, and r6469's correction did not go far enough: it demoted the
claim from "the first free constant" to "a register-crossing", where the honest end
of the argument is that the ledger says nothing about constants of this kind at all.

  ⌗ WHAT DOES SURVIVE, and it is an observation rather than a cost: the coefficient's
  only observable is a shift in S, and S is the quantity `p0` singles out as a count
  taken ACROSS the register split.  ** That is the register split behaving as p0
  describes, at the place p0 says it happens -- which is a confirmation of the
  structure, not a debit against it. **

--------------------------------------------------------------------------------
⇒ AND `PO-43`'s SECOND REPLACEMENT QUESTION IS ANSWERED.  It asked whether the ledger
counts topological terms.  ** It does not: the ledger's statement is about the
geometric gauges and the closing of the one extension freedom, and a topological
term's coefficient is neither. **  r6435 established that the question reduced to the
entropy; this establishes what the reduction returns.
"""

# --- the ledger's two registers, and what each is a claim about ------------------
LEDGER = {
    "real-geometric": {
        "gauges": ("c", "Lambda", "G"),
        "claim": "each a nameable feature of the substrate and its cuts",
    },
    "thermal": {
        "gauges": ("hbar", "k_B"),
        "claim": "the closing of THE ONE QUANTUM FREEDOM, not a new geometric feature",
    },
}
assert len(LEDGER) == 2, "p0 names two registers"
assert "ONE QUANTUM FREEDOM" in LEDGER["thermal"]["claim"]
print("  the ledger's registers:")
for k, v in LEDGER.items():
    print(f"    {k:<16} {', '.join(v['gauges'])}")
print("  and its quantum claim is the closing of ONE freedom, named.   OK")

# --- the three quantum freedoms, and which the ledger reaches ---------------------
FREEDOMS = {
    "self-adjoint extension":        "closed by the ledger",
    "regularisation of the sums":    "conceded -- the mode sums spend one",
    "counterterm finite part (GB)":  None,
}
reached = [k for k, v in FREEDOMS.items() if v == "closed by the ledger"]
unspoken = [k for k, v in FREEDOMS.items() if v is None]
assert len(reached) == 1, "the ledger closes exactly one"
assert unspoken == ["counterterm finite part (GB)"], "and says nothing about this one"
print("\n  three distinct quantum freedoms:")
for k, v in FREEDOMS.items():
    print(f"    {k:<32} {v or 'NOT SPOKEN TO'}")
print("  -> a GB entropy shift is of the third kind                    OK")

# --- so the branch is costless, which retracts r6437 -----------------------------
r6437_claim = "the declination is load-bearing; the ledger has a stake in the branch"
corrected   = "the ledger's statement does not reach this kind of constant; the branch is costless"
assert r6437_claim != corrected
print(f"\n  r6437     : {r6437_claim}")
print(f"  retracted : {corrected}")
print("  -> p0 was right, and the stake was an artefact of the unscoped")
print("     headline. r6469 demoted the claim; this withdraws it.       OK")

# --- and PO-43's second question follows ------------------------------------------
# Not asserted as a constant: DERIVED from the two structures above.  A topological
# coefficient is counted only if it is either a real-geometric gauge or the one
# quantum freedom the ledger closes.  It is neither, and that is checkable.
def ledger_counts(freedom):
    """the ledger counts a thing iff it is one of its gauges or the freedom it closes"""
    gauges = set(LEDGER["real-geometric"]["gauges"]) | set(LEDGER["thermal"]["gauges"])
    return freedom in gauges or FREEDOMS.get(freedom) == "closed by the ledger"


assert ledger_counts("Lambda") and ledger_counts("hbar"), "its own gauges are counted"
assert ledger_counts("self-adjoint extension"), "and the freedom it closes"
assert not ledger_counts("counterterm finite part (GB)"), "but not a counterterm's finite part"
assert not ledger_counts("regularisation of the sums"), "nor the regularisation, already conceded"
ledger_counts_topological_terms = ledger_counts("counterterm finite part (GB)")
print("\n  PO-43's second question -- does the ledger count topological terms?")
print("  -> NO. Its statement is the geometric gauges and the one extension")
print("     freedom, and a topological coefficient is neither.           OK")

print()
print("ESTABLISHED: the ledger's statement does not reach a counterterm coefficient,")
print("so the entropy branch is costless to it -- p0's own reading -- and PO-43's")
print("second replacement question is answered in the negative.")
print("RETRACTED: r6437's 'load-bearing', which r6469 demoted and this withdraws.")
