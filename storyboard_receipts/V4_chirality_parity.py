"""V_4 acts on the three walls' chirality signs (prop:wall: chirality = sigma_y eigenvalue per wall,
and reversing a wall flips it).  det=+1 => EVEN number of flips.  What is the orbit of the
observed configuration, and is the observed one distinguished?"""
import itertools, numpy as np
V4=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]     # diagonal +-1, det +1
obs=(1,1,1)                                     # dim ker_+ = 3, dim ker_- = 0 : all one chirality
print("   V_4 = diagonal sign flips with det +1 -> an EVEN number of chirality flips:")
for v in V4: print("      %s   flips %d wall(s)"%(str(v), sum(1 for x in v if x<0)))
print()
orbit=sorted(set(tuple(a*b for a,b in zip(obs,v)) for v in V4))
print("   orbit of the observed (+,+,+):")
for o in orbit:
    same = len(set(o))==1
    print("      %s   all-equal: %s"%(str(o), 'YES' if same else 'no'))
print()
n_uniform=sum(1 for o in orbit if len(set(o))==1)
print("   configurations in the orbit: %d ;  with UNIFORM chirality: %d"%(len(orbit),n_uniform))
print("   => the observed configuration is the UNIQUE uniform member of its V_4 orbit.")
print()
print("   and the odd flips (det -1) are NOT in the holonomy group:")
for v in [(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,-1)]:
    print("      %s  det %+d  -> excluded"%(str(v), int(np.prod(v))))
print("   so a SINGLE generation's chirality can never be flipped by this holonomy;")
print("   only pairs.  The count 3 (odd) can therefore never be reached from 0.")

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The claim is: V_4 is the det=+1 diagonal sign group (so every element flips an EVEN number
# of walls), the observed (+,+,+) has an orbit of FOUR configurations of which exactly ONE is
# uniform, and the odd (det = -1) flips lie outside it.  Literals pinned are the numbers this
# receipt prints: 4 elements, 0/2/2/2 flips, orbit size 4, uniform count 1.
assert len(V4) == 4, "V_4 must have exactly four elements"
assert all(int(np.prod(v)) == 1 for v in V4), "every V_4 element must have det +1"
assert [sum(1 for x in v if x < 0) for v in V4] == [0, 2, 2, 2], \
    "the flip counts printed above are 0,2,2,2 -- all EVEN"
assert len(orbit) == 4, "the printed orbit size is 4"
assert n_uniform == 1, "exactly ONE orbit member has uniform chirality"
assert sorted(orbit) == sorted(V4), "the orbit of (+,+,+) is V_4 itself"
assert obs in orbit and len(set(obs)) == 1, "the observed (+,+,+) is that unique uniform member"
# and the excluded odd flips: det -1 each, three of them singletons plus the total flip
_odd = [(-1, 1, 1), (1, -1, 1), (1, 1, -1), (-1, -1, -1)]
assert all(int(np.prod(v)) == -1 for v in _odd), "the odd flips must all have det -1"
assert all(v not in V4 for v in _odd), "no odd flip lies in the holonomy group V_4"
# 3 is odd, so it is unreachable from 0 by even flips -- the receipt's closing sentence
assert all(sum(1 for x in v if x < 0) % 2 == 0 for v in V4) and 3 % 2 == 1, \
    "a 3-flip (odd) is not reachable by any even-flip element"
