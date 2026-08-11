"""What ranks do the substrate's natural bundles have?  Dirac spinor dimension in D dimensions
is 2^floor(D/2) (Lorentzian, complex).  Restriction of a 5D spinor to a 4D slice."""
print("   dimension D    Dirac spinor dim 2^floor(D/2)")
_dims=[]                                # r2376+c54.161: capture only; computes nothing new
for D in (2,3,4,5,6):
    _dims.append(2**(D//2))
    print("      %d              %d"%(D, 2**(D//2)))
print()
print("   substrate dS_5 : D=5  -> spinor rank 4")
print("   slicing leaf   : D=4  -> spinor rank 4")
print("   => the 5D spinor bundle restricts to a 4D slice with THE SAME rank, 4.")
print("      In odd D the Dirac rep is irreducible and its restriction to a codim-1 slice is the 4D Dirac rep.")
print()
print("   other natural bundles of the substrate:")
print("      tangent bundle of dS_5           rank 5")
print("      normal bundle of the wall        rank 1  (codimension one)")
print("      each ruling family               rank 1  (rulings are lines)")
print()
print("   SM needs, per generation: multiplets of dim 6,3,3,2,1 -> 15 Weyl fields.")
print("   NOTE: 15 is a SUM OF REPS, not a natural bundle rank.  The question is not")
print("         'which bundle has rank 15' but 'what supplies the su(3)xsu(2)xu(1) structure'.")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (i) the printed table itself, as the loop above built it: 2^floor(D/2) at D = 2,3,4,5,6.
assert _dims == [2, 2, 4, 4, 8], _dims
# (ii) THE CLAIM of the middle block -- the dS_5 spinor bundle and the 4D leaf spinor bundle
#      have THE SAME rank, and that rank is 4.  Fires if the rank formula or either D moves.
assert _dims[3] == _dims[2] == 4, (_dims[2], _dims[3])
# (iii) THE CLAIM of the closing NOTE: the SM's 15 is a SUM of the multiplet dimensions and is
#      NOT the rank of any Dirac bundle in any dimension -- 2^floor(D/2) is a power of two.
#      This is the sentence that forecloses 'which bundle has rank 15'.
assert 6 + 3 + 3 + 2 + 1 == 15
assert all(2**(D//2) != 15 for D in range(1, 65))
# (iv) the other natural ranks printed, and none of them is 15 either: tangent bundle of dS_5
#      has rank 5, the wall's normal bundle rank 1 (codimension one: 5 - 4), rulings rank 1.
_other = [5, 5 - 4, 1]
assert _other == [5, 1, 1] and 15 not in _other + _dims, _other
