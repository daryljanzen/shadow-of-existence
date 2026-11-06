# `r7695` (cc66) — **EVERY `k` SITE IN `_project`, SPLIT INTO SOURCE AND KERNEL**

*The construction needs the source side at `ρk` and the kernel side at `k`. **A site put on the wrong
side makes the object a hybrid, and the byte-identical guard cannot see it**: unset is identical either
way, so the guard protects against regression and NOT against my getting this split wrong. ⇒ So the
split is enumerated here, from the function, before it is written — and a physics gate that CAN see a
wrong split is designed below.*

## SOURCE SIDE — must be evaluated at `ρk`

| site | the term |
|---|---|
| `Ps = Ph - 6*Hcv**2*(Onv*sgn + Ogv*sgg) / kb**2` | the Newtonian potential |
| `D = np.exp(-(kb**2) * kD2inv_of(np.minimum(ee, e_sw)))` | **the damping envelope — where the stretch confound lives** |
| `+ _DPSRC * np.gradient(g_*tb, ee, axis=0) / kb**2` | the Doppler term |
| `+ _PI*0.75*np.gradient(np.gradient(g_*Pi, ee, axis=0), ee, axis=0) / kb**2` | the polarisation term |
| `Y` itself | the solved fields — from `evolve(ρk)` and `evolve_hier(ρk)` |
| the `_SRCS/_SRCD/_SRCE` split block's `_dp` and `_pl` | **mirrors of two of the above** |

⚠ *The last row is the one most easily missed: it is a **diagnostic** re-derivation of the same four
terms, and the receipt gates that they sum to `S`. **Leave it at `k` and that gate fails on a set
switch** — which is the one piece of luck in this patch, since it means the mirror cannot be silently
forgotten.*

## KERNEL AND MEASURE — must stay at `k`

| site | the term |
|---|---|
| `dk = np.gradient(kb)` | the k-measure |
| `P = kb**(NS-1) / kb * dk` | the primordial weight × measure |
| `_J = spherical_jn(int(_l), kb[None,:] * (_SRCXS*x0)[:,None])` | **the projection kernel** |
| `_qk = kb * R_S / np.pi` | a reported diagnostic in `q` |

⌗ *The `_SRCI` analytic-injection branch (`_ph = kb*_rf(ee)` or `kb*R_S`, and `kb**(0.5*(1-NS))`) is a
**separate path** that replaces `S` entirely. It is not on either side of this split: with `SRCINJ` set
there is no plasma to give the control's period to, so the two switches are **mutually exclusive** and
that must be a refusal rather than a precedence rule.*

## ⛭ THE GATE THAT CAN SEE A WRONG SPLIT, WHICH THE BYTE-IDENTICAL ONE CANNOT

1. **`ρ` unset → byte-identical.** *By construction (the second array defaults to the first), and
   measured anyway.*
2. **`ρ` set to exactly `1.0` → byte-identical.** ⇒ *This is the wiring gate: it fails if the switch is
   plumbed to nothing, and it fails if a site is read from the wrong array in a way that survives the
   default. **Neither of gates 1 and 2 alone catches both.***
3. ⛭ **`ρ` set to the real ratio → THE COMB PERIOD IN `q` MUST COME OUT AT THE CONTROL'S.** *This is the
   decisive one: the whole construction's claim is "the CR plasma with the control's acoustic period",
   so **the period is a measurable property of the output and not a hope about the patch.** If a
   source-side site is left at `k`, the comb lands between the two periods and this gate reads it.*
   ⇒ **Nothing is read off the seven bands until gate 3 passes.**

⌗ *** This is the lesson of `r7693` turned into machinery: there, nothing I built could have caught that
the bank was the wrong object, because every check I wrote compared my read against the order's row.
Gate 3 compares the OUTPUT against the property the construction is named for. ***

## STATUS — **NOT IMPLEMENTED, AND SAYING SO RATHER THAN SHOWING PROGRESS**

The inventory is complete and the gates are designed; **no line of the switch is written and no rebuild
is launched.** ⌗ *Six source-side sites in the function that produces every reported spectrum, plus a
mutual-exclusion refusal against `SRCINJ`, is not a patch to half-land and leave in a tree — and
launching a `1–1.5 h` rebuild of a hybrid would cost the night and produce a number that looks like an
answer.* ⇒ *The next step is mechanical because the hard part — **which sites, on which side, checked by
what** — is on paper.*
