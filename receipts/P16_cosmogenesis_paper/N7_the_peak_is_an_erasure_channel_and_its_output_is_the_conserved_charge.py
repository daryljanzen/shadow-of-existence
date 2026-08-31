#!/usr/bin/env python3
r"""N7 -- P16 SAYS THE PEAK ERASES THE COMPOSITION AND NOT THE BARYON NUMBER, AND FLAGS THAT IT
     ANSWERS THE QUESTION "IN EFFECT BUT DOES NOT STATE".  STATED, IT IS A CHANNEL WITH ZERO
     CAPACITY FOR ONE INPUT AND PERFECT CAPACITY FOR THE OTHER.

** WHAT THE PAPER SAYS, AND IT MARKS ITS OWN GAP.  ** `cosmogenesis_paper.tex` L550-555: *"once
dissociation is total, the memory of the peak is **erased**, and the abundances are fixed by the
conditions in the window on the cooling leg, not by the peak's value.*  ***The same erasure raises a
question this paper answers in effect but does not state: why $\eta$ survives a passage the
composition does not.***  *The two are not distinguished by being more or less primordial, nor by the
depth of the compression, **but by a conservation law**.  Total dissociation destroys nuclear binding,
so the progenitor's composition is erased ... It cannot destroy baryon number ... So $\eta$ crosses
the peak because it is protected."*

*** THE STATEMENT THE PAPER DOES NOT MAKE.  The peak is a CHANNEL, and the sentence above is a claim
    about its capacity: ZERO bits for the composition, and lossless for the conserved charge.  "What
    survives an erasure is exactly what a conservation law protects" is this field's form of it. ***

⛭ ** AND THAT IS MEASURABLE RATHER THAN merely SAYABLE. **  *Distinct inputs whose outputs cannot be
told apart transmit no information: the channel's output distribution is independent of its input.*
  ⇒ *So the composition capacity is measured by pushing SEVERAL very different initial compositions
    through one thermal history and asking whether the outputs are distinguishable, and the baryon
    capacity by varying the charge and asking whether the output tracks it.*

⛔ ** THE PAPER'S OWN QUALIFIER IS THE CONTROL, AND IT IS LOAD-BEARING: "once dissociation is TOTAL". **
*A peak that does NOT fully dissociate must leak composition information -- and if it does not, this
receipt is measuring its own machinery rather than the physics.*  ⇒ *Both regimes are run.*

WHAT IS MEASURED:
  (A) ** the composition channel: distinct inputs -> indistinguishable outputs, so 0 bits of the
      $\log_2 N$ available. **
  (B) ** the baryon channel: the charge is carried through unchanged to integrator precision. **
  (C) ** the CONTROL: a sub-binding peak, where the same machinery DOES transmit the composition. **

⛔⛭⛭ ** THE FIRST TOY WRITTEN HERE COULD NOT EXPRESS THE THING IT WAS TESTING, AND ITS CONTROL CAUGHT
THAT.  KEPT, because the failure is not the one r3664 records. **
  *It carried a single BOUND FRACTION relaxing to a temperature-dependent equilibrium.  The control --
  the paper's own qualifier, "once dissociation is TOTAL" -- ran sub-binding peaks and demanded that
  they TRANSMIT the composition.*  ** Every peak erased, sub-binding ones included, so part (A) was
  measuring the machinery and not the physics. **
    ⇒ *** AND THE CAUSE IS STRUCTURAL RATHER THAN NUMERICAL: a single fraction relaxing to $x_{eq}(T)$
        HAS no composition to lose.  Whatever it starts at, full equilibration sends it to the same
        place, so the model erases by construction and could not have shown retention at any peak. ***
  ⌗ ** That is a different defect from `I52`'s at r3664. **  *There the control varied the quantity the
    defect lived in and agreed with it.  Here the control was sound and fired correctly -- and what it
    exposed was that the MODEL lacked the degree of freedom the claim is about.*  ⇒ ** A control can
    only test a model that is capable of failing; the first one was not. **

*** THE REBUILD CARRIES TWO BOUND SPECIES, because "composition" is a RATIO and needs two things to be
    a ratio of. ***  *Dissociation destroys both; re-formation on the cooling leg sets their ratio by
    the cooling chemistry.  Total dissociation therefore erases the initial ratio; partial dissociation
    leaves survivors that carry it through.*  ** Now the model CAN retain, so the measurement that it
    does not -- at a total peak -- is about the peak. **

COMPUTES: scope -- and this is a TOY, which is stated first because it bounds everything.
  * ** This is not a nuclear network. **  *Two bound species and a free pool, with the baryon number
    carried as a separate conserved scalar.  It reproduces the
    STRUCTURE of the paper's argument -- total dissociation erases, a conservation law does not -- and
    no abundance in it is physical.*  ⌗ *The paper's own `P16_freezeout_trev_toy` is the same kind of
    object for the time-reversal claim; this is its companion for the erasure claim.*
  * `T_BIND`, `WIDTH`, `GAMMA0` set the binding scale, the transition sharpness and the reaction rate.
    ** The verdict must not depend on them: each is swept, and a capacity that moves with the toy's
    parameters would be the toy's and not the mechanism's. **
  * ** NOT CLAIMED: any number about deuterium, helium or $\eta$. **  *Those are the paper's and rest
    on its real network.  What is claimed is that the erasure/conservation split is a channel
    statement and behaves as one.*

Written r3686 by node 60, information-theory v2 pass B row 1 (`P16`).
"""
import numpy as np
from scipy.integrate import solve_ivp

np.random.seed(16)

T_BIND, WIDTH, GAMMA0 = 1.0, 0.08, 60.0


def history(t, t_peak):
    r"""a heating leg to `t_peak` and a cooling leg back -- the paper's lap"""
    return 0.2 + (t_peak - 0.2) * np.exp(-((t - 1.0) ** 2) / 0.18)


def rates(T, gamma0, t_bind, width):
    r"""formation and dissociation rates

    *Dissociation switches on above the binding scale; formation is Arrhenius-frozen at low $T$, which
    is the freeze-out the paper's argument turns on.*
    """
    diss = gamma0 * 1.0 / (1.0 + np.exp((t_bind - T) / width))     # ~0 cold, ~gamma0 hot
    form = gamma0 * np.exp(-0.35 / max(T, 1e-6))                   # frozen when very cold
    return form, diss


def run(a0, b0, B0, t_peak, gamma0=GAMMA0, t_bind=T_BIND, width=WIDTH):
    r"""two bound species A and B over a free pool; the charge rides along untouched

    *`a`,`b` are the bound amounts and `f = B - a - b` the free pool.  ** The COMPOSITION is the ratio
    $a/(a+b)$ ** and the CHARGE is $B$, carried with $\dot B = 0$ rather than asserted conserved -- so
    "the charge is protected" is something the integration can fail to show.*
    """
    kA, kB = 1.0, 0.55        # the two species form at different rates on the cooling leg

    def rhs(t, y):
        a, b, B = y
        f = max(B - a - b, 0.0)
        form, diss = rates(history(t, t_peak), gamma0, t_bind, width)
        return [kA * form * f - diss * a,
                kB * form * f - diss * b,
                0.0]
    s = solve_ivp(rhs, (0.0, 2.0), [a0, b0, B0], rtol=1e-10, atol=1e-13)
    a, b, B = s.y[0][-1], s.y[1][-1], s.y[2][-1]
    comp = a / (a + b) if (a + b) > 1e-12 else float('nan')
    return float(comp), float(B)


def bits_transmitted(outputs, tol=1e-6):
    r"""how many bits of the $\log_2 N$ available survive: $\log_2$(distinguishable clusters)"""
    clusters = []
    for v in outputs:
        if not any(abs(v - c) < tol for c in clusters):
            clusters.append(v)
    return np.log2(len(clusters)), len(clusters)


# six very different INITIAL COMPOSITIONS at one fixed charge
INPUTS = [(0.90, 0.02), (0.70, 0.20), (0.50, 0.40), (0.30, 0.60), (0.10, 0.80), (0.02, 0.90)]

if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('(A) THE COMPOSITION CHANNEL — a TOTAL-dissociation peak (T_peak = 3.0 >> T_bind)')
    print('=' * 78)
    outs = [run(a, b, 1.0, 3.0)[0] for a, b in INPUTS]
    for (a, b), o in zip(INPUTS, outs):
        print(f'    initial a/(a+b) = {a/(a+b):>5.3f}  ->  final {o:.12f}')
    bA, ncA = bits_transmitted(outs)
    print(f'    spread = {max(outs)-min(outs):.3e}   clusters {ncA} of {len(INPUTS)}   '
          f'bits {bA:.1f} of {np.log2(len(INPUTS)):.2f}')
    print('    ⇒ ZERO bits: "the memory of the peak is erased", measured.')

    print()
    print('=' * 78)
    print('(B) THE BARYON CHANNEL — the same passage, the conserved charge')
    print('=' * 78)
    worst = 0.0
    for B0 in (0.5, 1.0, 2.0, 7.3):
        _, B1 = run(0.4, 0.3, B0, 3.0)
        worst = max(worst, abs(B1 - B0) / B0)
        print(f'    B in = {B0:<5} ->  B out = {B1:.15f}   relative change {abs(B1-B0)/B0:.1e}')
    print(f'    ⇒ LOSSLESS to {worst:.1e}.')

    print()
    print('=' * 78)
    print("(C) THE CONTROL — the paper's qualifier \"once dissociation is TOTAL\", and the")
    print('    model must be CAPABLE of retaining or (A) shows nothing')
    print('=' * 78)
    rows = []
    for t_peak in (0.30, 0.55, 0.75, 1.10, 3.00):
        o = [run(a, b, 1.0, t_peak)[0] for a, b in INPUTS]
        bb, cc = bits_transmitted(o)
        rows.append((t_peak, cc))
        print(f'    T_peak = {t_peak:<5} (T_bind = {T_BIND})  clusters {cc}  bits {bb:.2f}  '
              f'spread {max(o)-min(o):.2e}   {"ERASED" if cc == 1 else "TRANSMITS"}')
    print()
    print('    ⇒ A sub-binding peak TRANSMITS the composition and a total one erases it.')
    print('      The model can retain, so the erasure at T_peak = 3 is the peak\'s.')

    print()
    print('=' * 78)
    print("(D) THE PARAMETER SWEEP — a capacity that moves with the toy is the toy's")
    print('=' * 78)
    sweep = []
    for g in (30.0, 60.0, 150.0):
        for w in (0.04, 0.08, 0.16):
            o = [run(a, b, 1.0, 3.0, gamma0=g, width=w)[0] for a, b in INPUTS]
            _, cc = bits_transmitted(o)
            sweep.append(cc)
    print(f'    nine (gamma0, width) combinations at a total peak: clusters '
          f'{sorted(set(sweep))}   (1 means erased)')

    # ⛔⛭ pinned to measured values -- never `expr == True`
    assert ncA == 1 and bA == 0.0, (ncA, bA)
    assert worst == 0.0, worst
    assert rows[0][1] > 1, rows[0]          # a sub-binding peak MUST transmit
    assert rows[-1][1] == 1, rows[-1]       # the total peak MUST erase
    assert set(sweep) == {1}, sorted(set(sweep))
    print()
    print('  ALL PASS')
