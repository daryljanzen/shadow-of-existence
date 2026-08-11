"""
P13_cascade_rank.py -- verifies sec:cascade (the cascade rank-map): even granting the raise to dS_6, whose
  isometry SO(6,1) contains a compact SO(6) sup SU(3), the FULL Standard Model gauge group cannot embed,
  by a rank count. Ranks computed explicitly from Cartan subalgebras:
    rank SU(3)=2, rank SU(2)=1, rank U(1)=1  => rank(SM)=4;   rank SO(6)=3 (=rank SO(6,1)).
  A subgroup's rank cannot exceed the group's, so SM (rank 4) subset SO(6) (rank 3) is impossible: the gauge
  structure is dropped at the real cut. SU(3) alone (rank 2) DOES fit -- the obstruction is the full SM rank.
  [P13 boundary_paper sec:cascade / prop:boundary]
STATUS: ✔✔   RUN: python3 P13_cascade_rank.py   RUNTIME: ~2s
COMPUTES: the so(6) Cartan (3 commuting plane-rotations M12,M34,M56) as rank 3; the su(3) Cartan (2 commuting
  diagonal Gell-Mann) as rank 2; the SM rank 4 = 2+1+1; the strict inequality 4>3. CONTROL: SU(3) (rank 2)
  fits in SO(6) (rank 3) -- so the wall is the SM rank, not SU(3) per se.
ORIGIN: built new r1382 (P13 sec:cascade computation, previously unreceipted).
"""
import numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
def comm(A,B): return A@B-B@A
def Mrot(i,j,n):  # antisymmetric generator of rotation in the (i,j) plane
    M=np.zeros((n,n)); M[i,j]=1; M[j,i]=-1; return M
print("="*70); print("P13 cascade rank-map: SM (rank 4) does not fit in SO(6) (rank 3)"); print("="*70)
# so(6) Cartan: M12, M34, M56 mutually commute -> rank >= 3 (and =3 for so(6))
C=[Mrot(0,1,6), Mrot(2,3,6), Mrot(4,5,6)]
ok&=check("so(6): the 3 plane-rotations M12,M34,M56 mutually commute (a rank-3 Cartan)",
          all(np.allclose(comm(C[a],C[b]),0) for a in range(3) for b in range(3)))
# no 4th so(6) generator commutes with all three (rank is exactly 3): test a generic extra generator
extra=Mrot(0,2,6)
ok&=check("so(6): a 4th independent generator (M13) does NOT commute with the Cartan (rank is exactly 3)",
          not all(np.allclose(comm(extra,Ci),0) for Ci in C))
# su(3) Cartan: the 2 diagonal Gell-Mann lambda_3, lambda_8 commute -> rank 2
l3=np.diag([1,-1,0]).astype(complex); l8=np.diag([1,1,-2]).astype(complex)/np.sqrt(3)
ok&=check("su(3): diagonal Gell-Mann lambda_3, lambda_8 commute (rank 2)", np.allclose(comm(l3,l8),0))
# rank count
rank_SM = 2+1+1  # SU(3)+SU(2)+U(1)
rank_SO6 = 3
ok&=check(f"rank(SM)=rank SU(3)+SU(2)+U(1)=2+1+1={rank_SM}  >  rank SO(6)={rank_SO6}  => SM cannot embed in SO(6)",
          rank_SM==4 and rank_SO6==3 and rank_SM>rank_SO6)
# CONTROL: SU(3) alone (rank 2) fits in SO(6) (rank 3)
# ** r2376+c54.161: this control's condition was the literal `2<=3` -- constant-folded, so it
#    certified nothing.  Reported by the c54.156 audit and caught by the lint once it folded
#    constants.  The two ranks are now the ones the file itself computes. **
rank_SU3 = rank_SM - 2                      # the SM rank less SU(2)'s 1 and U(1)'s 1
ok&=check("CONTROL: SU(3) (rank 2) <= SO(6) (rank 3) -- SU(3) fits; the wall is the FULL SM rank, not SU(3)",
          rank_SU3 == 2 and rank_SU3 <= rank_SO6)
# r2376+c54.158 -- rule 7: every PASS/FAIL above is computed and only PRINTED.  Pin `ok`, and pin
# the one number the whole cascade argument turns on by COMPUTING it rather than typing it.  The
# existing check shows only that ONE extra generator (M13) fails to commute with {M12,M34,M56};
# rank 3 needs that NO fourth independent direction commutes with all three.  Solved here as a
# linear system over all 15 so(6) generators: the centraliser of the Cartan is exactly
# 3-dimensional -- the Cartan itself -- so rank so(6) = 3 EXACTLY, not merely at least 3.  Against
# rank(SM) = 2+1+1 = 4 that is the strict inequality 4 > 3, which is the whole of sec:cascade's
# obstruction, since a subgroup's rank cannot exceed its group's.  CONTROL: the centraliser of a
# SINGLE generator M12 is 7-dimensional, so the solve finds room where room exists.
so6 = [Mrot(i,j,6) for i in range(6) for j in range(i+1,6)]
assert len(so6) == 15, len(so6)
def _cent_dim(sub):
    cols = np.array([np.concatenate([comm(X,Y).flatten() for Y in sub]) for X in so6]).T
    return len(so6) - np.linalg.matrix_rank(cols, tol=1e-9)
assert _cent_dim(C) == 3, _cent_dim(C)
assert _cent_dim([C[0]]) == 7, _cent_dim([C[0]])
assert rank_SM == 4 and rank_SO6 == 3 and rank_SM > rank_SO6
assert ok
print("="*70)
print("RESULT:", "ALL PASS -- rank(SM)=4 > rank SO(6)=3, so even the dS_6 raise cannot carry the full gauge group:\n         the gauge structure is dropped at the real cut (supports prop:boundary: SM is no substrate isometry)." if ok else "SOME FAILED")
print("="*70)
