"""
P03_winding_vs_triality_closure
===============================
WHAT IT ASKS.  The corpus carries TWO Z_3 admission rules, in two papers, and reads
them as one:

  (W)  P3 sec:winding   -- a composite is admitted iff its TOTAL WINDING is integral,
                           sum_i n_i = 0 (mod 3), n_i the signed count of graze points
                           the constituent's equatorial route crosses.  A statement
                           about the COVERING of r: to close is to return to the same
                           branch, and r -> omega r once per wall crossing.

  (T)  P14 sec:chirality -- a configuration exists only if its TOTAL RESIDUE vanishes,
                           sum_i t_i = 0 (mod 3), t_i = -lambda_i mod 3 the triality
                           read off the ANGULAR problem (L-78: psi ~ r^-lambda, so
                           psi -> omega^-lambda psi per crossing).

These coincide iff  n_i = t_i (mod 3)  for every constituent -- which is exactly the
step both papers mark as an assumption ("the identification of the triality class with
the charge's fractional part remains the assumption it was").

WHAT THIS COMPUTES.
  1. Both rules on the eleven channels the corpus tests, with the standard assignment.
  2. Whether that test set CAN distinguish them  -- the rigged-discriminator check.
  3. The smallest configuration on which they DISAGREE, if one exists.
  4. Whether (W) and (T) are independent as conditions, or one implies the other.

WHAT WOULD FALSIFY THE HEADLINE.  If the two rules disagreed on any tested channel,
the 11/11 result would belong to one rule and not the other.  If no configuration
separated them, the identification would be free rather than assumed.
"""
from itertools import product

print("=" * 78)
print("PART 1 — THE ELEVEN CHANNELS, BOTH RULES")
print("=" * 78)

# standard assignment: quark (n,t) = (+1,+1), antiquark (-1,-1)
q, qb = (+1, +1), (-1, -1)
channels = [
    ("meson        q qbar",        [q, qb],                     True),
    ("baryon       q q q",         [q, q, q],                   True),
    ("antibaryon   qb qb qb",      [qb, qb, qb],                True),
    ("tetraquark   q q qb qb",     [q, q, qb, qb],              True),
    ("pentaquark   q q q q qb",    [q, q, q, q, qb],            True),
    ("dibaryon     6q",            [q]*6,                       True),
    ("free quark   q",             [q],                         False),
    ("diquark      q q",           [q, q],                      False),
    ("q qbar q",                   [q, qb, q],                  False),
    ("q q q q",                    [q]*4,                       False),
    ("q q q qbar",                 [q, q, q, qb],               False),
]

def W(cfg): return sum(n for n, _ in cfg) % 3 == 0
def T(cfg): return sum(t for _, t in cfg) % 3 == 0

agree = 0
for name, cfg, observed in channels:
    w, t = W(cfg), T(cfg)
    ok_w = (w == observed)
    ok_t = (t == observed)
    agree += (w == t)
    print(f"  {name:24s} observed={str(observed):5s}  (W)={str(w):5s}[{'ok' if ok_w else 'MISS'}]"
          f"  (T)={str(t):5s}[{'ok' if ok_t else 'MISS'}]")
print()
print(f"  (W) agrees with observation on {sum(W(c)==o for _,c,o in channels)}/11")
print(f"  (T) agrees with observation on {sum(T(c)==o for _,c,o in channels)}/11")
print(f"  (W) and (T) agree with EACH OTHER on {agree}/11")

print()
print("=" * 78)
print("PART 2 — CAN THE TEST SET DISTINGUISH THE TWO RULES?  (rigged-discriminator)")
print("=" * 78)
print("  Every constituent in the set above carries n = t by construction:")
print("    quark (n,t)=(+1,+1),  antiquark (n,t)=(-1,-1).")
print("  On any configuration built ONLY from such constituents, sum n = sum t")
print("  identically, so the two rules return the same verdict on every member of")
print("  the set, whatever the physics.")
same = all((sum(n for n,_ in c) % 3) == (sum(t for _,t in c) % 3) for _,c,_ in channels)
print(f"  Checked: sum n == sum t (mod 3) on all eleven -> {same}")
print()
print("  ** SO THE 11/11 RESULT CANNOT DISCRIMINATE (W) FROM (T). **  It tests the")
print("  admission rule, and confirms it; it does NOT test the identification n = t,")
print("  because the test set assumes it.  A discriminator needs a constituent with")
print("  n != t (mod 3).")

print()
print("=" * 78)
print("PART 3 — THE SMALLEST CONFIGURATION ON WHICH THEY DISAGREE")
print("=" * 78)
found = None
for size in range(1, 5):
    for cfg in product([(n, t) for n in (-1, 1, 2) for t in (0, 1, 2)], repeat=size):
        if W(cfg) != T(cfg):
            if any(n % 3 != t % 3 for n, t in cfg):
                found = cfg
                break
    if found:
        break
print(f"  smallest separating configuration: {found}")
print(f"    sum n = {sum(n for n,_ in found)} = {sum(n for n,_ in found)%3} (mod 3)  -> (W) admits: {W(found)}")
print(f"    sum t = {sum(t for _,t in found)} = {sum(t for _,t in found)%3} (mod 3)  -> (T) admits: {T(found)}")
print()
print("  ** So the two rules are genuinely independent conditions. **  A constituent")
print("  whose ROUTE class differs from its INTERNAL class separates them, and the")
print("  question the corpus leaves open is whether the geometry admits one.")

print()
print("=" * 78)
print("PART 4 — DOES EITHER RULE IMPLY THE OTHER?")
print("=" * 78)
alln = [(n, t) for n in (0, 1, 2) for t in (0, 1, 2)]
w_not_t = t_not_w = 0
for size in (2, 3):
    for cfg in product(alln, repeat=size):
        if W(cfg) and not T(cfg): w_not_t += 1
        if T(cfg) and not W(cfg): t_not_w += 1
print(f"  configurations (size 2-3) admitted by (W) and refused by (T): {w_not_t}")
print(f"  configurations (size 2-3) admitted by (T) and refused by (W): {t_not_w}")
print("  Neither implies the other; they are independent Z_3 conditions on")
print("  independent data -- a ROUTE label and an ANGULAR label.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  (W) and (T) are two admission rules on two different labels.  Both return")
print("  11/11 on the corpus's channel set, and that set CANNOT tell them apart,")
print("  because every constituent in it is assigned n = t at the outset.")
print("  The identification 'triality class = fractional part of the charge' is")
print("  exactly the condition  n = t (mod 3)  per constituent, and it is not tested")
print("  by the eleven.  What would test it is a constituent whose route class and")
print("  angular class differ -- and whether the geometry admits one is open.")
print()
print("  NOT CLAIMED: that the geometry does or does not admit such a constituent.")
print("  NOT CLAIMED: that the 11/11 result is weakened.  It stands, for the rule it")
print("  tests.  What is shown is WHICH rule it tests, and what it leaves untested.")
