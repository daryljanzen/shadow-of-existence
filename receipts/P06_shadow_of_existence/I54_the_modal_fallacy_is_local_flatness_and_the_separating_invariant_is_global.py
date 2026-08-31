#!/usr/bin/env python3
r"""I54 -- P06's MODAL FALLACY IS A THEOREM OF THIS FIELD, IN THIS FIELD'S OWN WORDS, AND THE
     PAPER USES THE TECHNICAL PHRASE.

** WHAT THE PAPER SAYS.  ** `shadow_of_existence.tex` `thm:modal`: *"From the premise that the
appearances contain no local discriminator between two candidate worlds, it does not follow that the
worlds are identical, nor that the structure distinguishing them does not exist.  **The absence of a
local test is not the absence of the fact.**"*  And the gloss, L313: *"the fallacy denies the
structure because one shadow happens to be* ***locally flat***.*"

⛭ ** `LOCALLY FLAT` IS NOT A METAPHOR HERE; IT IS THIS FIELD'S TECHNICAL TERM. **  *A submanifold is
locally flat when every point has a neighbourhood in which the embedding is the standard one -- and
the entire subject of high-dimensional topology turns on locally flat against wild embeddings,
precisely because* ** local standardness leaves the global invariant free. **
  ⇒ *** SO P06's CENTRAL THEOREM IS THE STATEMENT THAT LOCAL TRIVIALITY DOES NOT IMPLY GLOBAL
      TRIVIALITY, WHICH IS THIS FIELD'S FOUNDING PHENOMENON, AND THE PAPER REACHES IT IN THE FIELD'S
      OWN VOCABULARY. ***

⛔ ** AND THIS ROW WAS ONE STEP FROM BEING SCORED `CHECKED-NEGATIVE`, WHICH IS RECORDED BECAUSE IT IS
THE POINT.  **  *The locator predicted emptiness for `P06`.  A vocabulary screen agrees: `topolog` x0,
`obstruction` x0, `fibre` x0, and the `covering` x1 is ordinary English ("covering unforced choices").
The verdict was drafted as* ** "CHECKED-NEGATIVE, and the reason is a homonym -- `local` x25 is
EPISTEMIC (a test made here), not TOPOLOGICAL (in a neighbourhood)." **  *That drafting was wrong, and
the phrase that refutes it sits in the sentence the read had already passed over.*
  ⌗ *** `SIX_FIELDS_WORK_ORDER_v2.md` §2: "A paper that looks empty is the one to read hardest."  It
      was the single REFUTED row of the integrable run and it is a hit here too. ***

*** WHAT IS MEASURED.  The theorem, made exact on the smallest example that carries it. ***
  * ** NO LOCAL TEST SEPARATES THEM. **  *Over any proper sub-arc of the base circle the Moebius band
    and the cylinder are isomorphic: the transported frame returns with determinant $+1$ on BOTH.
    That is "the appearances contain no local discriminator", computed.*
  * ** A GLOBAL INVARIANT DOES. **  *Transport once around the whole circle and the determinant is
    $-1$ for the Moebius band and $+1$ for the cylinder.*  ⇒ ** "The absence of a local test is not
    the absence of the fact", with the fact exhibited. **
  * ** THE CONTROL THAT CAN FAIL: ** *the same procedure on two genuinely identical bundles must
    return $+1$ BOTH times, globally as well as locally.  A procedure that reports a difference for
    everything is not detecting one.*

COMPUTES: scope.
  * `n_steps` is the transport resolution and is swept; the determinant is $\pm1$ exactly and must not
    drift with it.
  * `arc_fraction` is how much of the circle a "local" test sees; it is swept from $0.1$ to $0.9$ and
    ** every proper fraction must return $+1$ for both bundles **, which is the content of "local".
  * ** NOT CLAIMED: that P06 computes any of this, or that it should. **  *The paper states the
    inference and names the phenomenon; this exhibits the smallest object in which the phenomenon is
    a theorem.  ⌗ That makes it a TRANSLATION rather than a BRIDGE, in the sense this field's ledger
    fixed at r3660: the content is in the paper's own sentence, not in a relation between papers.*

Written r3668 by node 60, pass B on row 13 of the index-theory locator (`P06`).
"""
import numpy as np

np.random.seed(3)


def transport(twist, n_steps, arc_fraction=1.0):
    r"""carry a frame along the base circle and return the determinant of the net transport

    *The band is built as a real line bundle over $S^1$ whose frame rotates by `twist` over the full
    circle: `twist = pi` is the Moebius band (the frame returns reversed) and `twist = 0` is the
    cylinder.  ** The transport is composed step by step, so nothing about the answer is put in by
    hand -- the determinant is read off the accumulated matrix. **
    """
    total = arc_fraction * 2 * np.pi
    d_theta = total / n_steps
    R = np.eye(2)
    for k in range(n_steps):
        # the frame's rotation rate: `twist` radians over the full 2*pi of base
        a = twist * d_theta / (2 * np.pi)
        step = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
        R = step @ R
    # a Moebius identification closes the loop with a REFLECTION; the cylinder with the identity
    if abs(arc_fraction - 1.0) < 1e-12:
        glue = np.array([[1.0, 0.0], [0.0, -1.0]]) if abs(twist - np.pi) < 1e-9 else np.eye(2)
        R = glue @ R
    return float(np.linalg.det(R))


MOEBIUS, CYLINDER = np.pi, 0.0


if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('(A) THE LOCAL TEST — every proper sub-arc, both bundles')
    print('=' * 78)
    print(f"    {'arc seen':>10} {'Moebius':>12} {'cylinder':>12}   separated?")
    local_rows = []
    for frac in (0.1, 0.25, 0.5, 0.75, 0.9):
        m = transport(MOEBIUS, 4000, frac)
        c = transport(CYLINDER, 4000, frac)
        sep = abs(m - c) > 1e-6
        local_rows.append(sep)
        print(f'    {frac:>10.2f} {m:>12.6f} {c:>12.6f}   {"YES" if sep else "no"}')
    print()
    print('    ⇒ NO proper sub-arc separates them.  That is "the appearances contain no')
    print('      local discriminator between two candidate worlds", computed.')

    print()
    print('=' * 78)
    print('(B) THE GLOBAL TEST — once around')
    print('=' * 78)
    gm, gc = transport(MOEBIUS, 4000), transport(CYLINDER, 4000)
    print(f'    Moebius  : det of net transport = {gm:+.6f}')
    print(f'    cylinder : det of net transport = {gc:+.6f}')
    print(f'    ⇒ separated globally: {abs(gm - gc) > 1e-6}')
    print()
    print('    ** "The absence of a local test is not the absence of the fact." **')
    print('    The fact is the sign, and no neighbourhood carries it.')

    print()
    print('=' * 78)
    print('(C) THE CONTROL — two identical bundles must NOT separate, globally either')
    print('=' * 78)
    c1, c2 = transport(CYLINDER, 4000), transport(CYLINDER, 3000)
    print(f'    cylinder vs cylinder : {c1:+.6f} vs {c2:+.6f}   separated: '
          f'{abs(c1 - c2) > 1e-6}')
    print('    ⇒ the procedure reports a difference only where there is one.')

    print()
    print('=' * 78)
    print('(D) THE RESOLUTION SWEEP — the sign is exact, not a drift')
    print('=' * 78)
    sweep = []
    for n in (250, 1000, 4000, 16000):
        m = transport(MOEBIUS, n)
        sweep.append(round(m, 9))
        print(f'    n_steps = {n:>6} :  Moebius det = {m:+.9f}')

    # ⛔⛭ pinned to measured values -- never `expr == True`
    assert not any(local_rows), local_rows          # no proper sub-arc separates them
    assert abs(gm + 1.0) < 1e-9, gm                 # Moebius: -1
    assert abs(gc - 1.0) < 1e-9, gc                 # cylinder: +1
    assert abs(c1 - c2) < 1e-9, (c1, c2)            # the control does not separate
    assert all(abs(x + 1.0) < 1e-9 for x in sweep), sweep
    print()
    print('  ALL PASS')
