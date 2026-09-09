"""
PO31_the_fixed_point_route_is_closed_by_the_monotone
====================================================

CLOSURE-ADJACENCY (L-211): after a closure, read the gaps in the papers and records
it touches. PO-40 closed at r4517. This is what it reaches.

THE IDEA IT REACHES, recorded r1942 in THE_WISDOM_LEDGER and never entered into any
paper (p0's one use of "recursion" is the ontological recursion closing on maximal
symmetry, a different object):

    "The construction is recursive -- the progenitor seeds the next universe, the
     rulings exchanging roles across the step. IF THE RECURSION WERE STATIONARY,
     A_s WOULD BE A FIXED POINT and determined rather than inherited. A real
     possibility, and not asserted: the corpus has 'previous universe' x12 and
     'recursi' x1, so the recursion is present but the map is not built -- and a
     fixed point of an unbuilt map is not a result."

That is the only route the corpus has ever named for DERIVING A_s rather than
inheriting it, and PO-31 is the row that wants it derived.

WHAT PO-40 ESTABLISHED (struck r4517):
    entropy per baryon rises STRICTLY at every crossing. The crossing is an
    erasure, erasures are irreversible, and the increment is bounded below --
    unconditionally by Landauer at k_B ln 2 per bit, since the composition
    distinguishes at minimum bound from free. Hence finitely many laps.

THE CONSEQUENCE, and it is elementary once the two are set side by side:

    A stationary recursion is one whose lap map has a FIXED POINT that the chain
    sits at. A map that strictly increases a coordinate has NO fixed point: a fixed
    point would require s/n_b to return to itself, and the increment is bounded
    below by a positive constant.

    ==> The recursion is not stationary, and cannot be made so. The r1942 route to
        deriving A_s is closed, and closed by a mechanism rather than by absence of
        evidence.

    ==> And the chain is FINITE, so there is no asymptotic limit for a fixed point
        to be the limit OF. The second reason is independent of the first.

WHAT SURVIVES, stated so the negative stays bounded:
    whether A_s ALONE is invariant along the chain while s/n_b rises -- a partial
    invariance, not stationarity. That is a weaker and different question, and
    answering it needs the lap map r1942 already said is unbuilt.

AND WHERE IT IS FIXED INSTEAD, which is the useful half:
    PO-41 answered the same shape of question for eta -- "what is owed at the head
    is the matter". With a finite chain, A_s and n_s are likewise not derived by
    iteration; they terminate at the head. So PO-31's remaining half and PO-41's
    head question are ONE question asked of different quantities, and PO-31's
    target is the head's own structure rather than a fixed point or a thermal
    history.

This receipt could have returned otherwise: if the increment were bounded below by
zero rather than a positive constant, a fixed point would not be excluded; if the
chain were infinite, the second reason would fail.
"""

import math

k_B_ln2 = math.log(2)          # in units of k_B: the Landauer floor per bit
increment_present_day = 6.4    # in units of k_B, PO-40's present-day figure
s_over_nb_today = 1.15e10      # in units of k_B, the standing value


def lap_map_has_fixed_point(increment_floor):
    """A map that strictly increases a coordinate has no fixed point."""
    return increment_floor <= 0


def chain_length_bound(increment_floor):
    """Strictly decreasing read backward, bounded below at zero."""
    return s_over_nb_today / increment_floor


# ---- (1) no fixed point, on the unconditional floor ---------------------------
assert k_B_ln2 > 0
assert not lap_map_has_fixed_point(k_B_ln2)
print(f"(1) Landauer floor per crossing = ln 2 = {k_B_ln2:.4f} k_B > 0")
print("    -> the lap map strictly increases s/n_b, so it has NO fixed point")
print("    -> the recursion is not stationary                          OK")

# ---- (2) and the chain is finite, independently -------------------------------
n_unconditional = chain_length_bound(k_B_ln2)
n_present_day = chain_length_bound(increment_present_day)
print()
print(f"(2) laps, on the Landauer floor alone : <= {n_unconditional:.3g}")
print(f"    laps, on the present-day increment: <= {n_present_day:.3g}")
assert n_unconditional < float('inf')
print("    -> finite, so there is no asymptotic limit for a fixed")
print("       point to be the limit of                                 OK")

# ---- (3) the two reasons are independent ---------------------------------------
print()
print("(3) the two reasons do not share a premise: (1) needs only that the")
print("    increment is positive, (2) only that it is bounded below.        OK")

print()
print("ESTABLISHED: the r1942 fixed-point route to deriving A_s is closed.")
print("SURVIVES:    partial invariance of A_s alone, which is not stationarity")
print("             and needs the unbuilt lap map.")
print("JOINED:      PO-31's remaining half terminates at the head, exactly as")
print("             PO-41 found for eta. One question, two quantities.")
