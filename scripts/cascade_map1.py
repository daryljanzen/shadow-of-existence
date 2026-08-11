# First bite, dS6/SM frontier: the cascade group-theory map.
# Compute (not recall) what survives each rung, and where su(3) can sit.
# Conventions: dim so(p,q) = n(n-1)/2 with n=p+q ; dim su(n) = n^2 - 1.

def dim_so(n):    return n*(n-1)//2
def dim_su(n):    return n*n - 1

# --- the cascade chain ---
print("RUNG            manifold     isometry      dim   max-compact   dim")
rows = [
 ("ambient",  "M^7 (6,1)", "SO(6,1)", dim_so(7), "SO(6)", dim_so(6)),
 ("raise",    "dS_6",      "SO(6,1)", dim_so(7), "SO(6)", dim_so(6)),
 ("substrate","dS_5",      "SO(5,1)", dim_so(6), "SO(5)", dim_so(5)),
]
for name,man,iso,d,mc,dmc in rows:
    print(f"{name:10s}  {man:10s}  {iso:8s}  {d:4d}   {mc:6s}  {dmc:4d}")

# --- where can su(3) sit? smallest faithful real rep of su(3) ---
# su(3) fundamental = 3 (complex) -> real dim 6. adjoint = 8 (real). So the
# smallest FAITHFUL real rep has dim 6  => su(3) ⊂ so(6), and 6 > 5 => ⊄ so(5).
print()
print(f"dim su(3) = {dim_su(3)}")
print("smallest faithful real rep of su(3): the 3+3bar = R^6  (complex 3 -> real 6)")
print(f"  su(3) ⊂ so(6)?  need real carrier dim <= 6 : {6 <= 6}  -> dim so(6)={dim_so(6)} >= 8  OK")
print(f"  su(3) ⊂ so(5)?  need real carrier dim <= 5 : {6 <= 5}  -> NO")

# --- the verdict the cascade forces ---
print()
print("WHAT SURVIVES THE CUT:")
print(" dS_6 isometry SO(6,1): max-compact SO(6) ⊃ SU(3)  -> colour CAN sit in the compact part of the RAISE.")
print(" cut dS_6 -> dS_5 (codim-1, totally-geodesic): residual spacetime isometry SO(5,1),")
print("   max-compact SO(5).  SU(3) ⊄ SO(5).  ==> SU(3) is DROPPED by the cut to the real substrate.")
print(" => 'which isometry survives the real-substrate cut' does NOT include colour:")
print("    su(3) ⊄ so(5,1), now seen at the cascade level (same one fact, C2).")
print(" => colour-via-the-raise lives ONLY in the compact SO(6) reachable off the real Lorentzian")
print("    substrate (the Wick/Euclidean face) -- consistent with the closed σ-lift (r295/296).")
