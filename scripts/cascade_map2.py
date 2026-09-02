# Driven step 2: how much of the SM can the raise's compact isometry hold?
# Rigorous core = RANK obstruction (subgroup rank <= group rank). Compute, don't recall.

def rank_so(n): return n//2            # rank of SO(n)
def dim_so(n):  return n*(n-1)//2
def dim_su(n):  return n*n-1

# ranks
rank_SM   = 2 + 1 + 1                   # su(3):2, su(2):1, u(1):1
rank_SU3xU1 = 2 + 1
print(f"rank(SM = SU3xSU2xU1) = {rank_SM}")
print(f"rank SO(6) (compact part of dS6 isometry SO(6,1)) = {rank_so(6)}")
print(f"  SM ⊂ SO(6)?  need rank(SM) <= rank SO(6): {rank_SM} <= {rank_so(6)} -> {rank_SM<=rank_so(6)}")
print(f"  rank(SU3xU1)={rank_SU3xU1} <= {rank_so(6)} -> {rank_SU3xU1<=rank_so(6)} : the raise buys at MOST SU(3)xU(1) (U(3)⊂SO(6))")
print()

# smallest SO(n) whose rank can hold the SM (rank 4):
n = next(n for n in range(3,16) if rank_so(n) >= rank_SM)
print(f"smallest SO(n) with rank >= {rank_SM}: SO({n}) (rank {rank_so(n)})")
print(f"  the standard CHIRAL GUT landmark at rank-4+ is SO(10): SO(10) ⊃ SU(5) ⊃ SM,")
print(f"  one generation = the 16 (chiral spinor). rank SO(10)={rank_so(10)}, dim={dim_so(10)}.")
print(f"  SO(10) is the compact part of SO(10,1) = isometry of dS_10 ⊂ M^11.")
print()

# the cut, again -- the whole internal structure is dropped at the real substrate
print("AT THE REAL-SUBSTRATE CUT dS_5 (isometry SO(5,1), compact SO(5), rank %d):" % rank_so(5))
print(f"  colour needs a 6-dim real carrier; SO(5) acts on R^5 -> su(3) ⊄ so(5,1).")
print(f"  a fortiori the whole SM (rank 4) ⊄ so(5,1).")
print("  => the ENTIRE gauge structure, like colour, is dropped at the cut and would live")
print("     only on the compact/Wick face -- the same place, not a new mechanism.")
print()
print("DRIVEN MAP (bounded, computed):")
print(" * dS6 raise buys at most SU(3)xU(1); the weak SU(2) does NOT fit (rank).")
print(" * full SM needs the raise-tower to continue to ~dS_10 (SO(10)), each rung unforced by real geometry.")
print(" * SM, like colour, is dropped at the real-substrate cut: gauge structure lives on the compact/Wick face.")
print(" * SO(10)-16 'one chiral generation' is the GUT landmark -- a SEDUCTIVE coherence hook; not claimed.")
