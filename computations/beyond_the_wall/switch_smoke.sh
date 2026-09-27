#!/bin/bash
# ⛭⛭⛭ ** THE STANDING SWITCH GUARD -- r6929+cc66.44. **
#
# *`r6925`'s launcher dropped its extra environment through a positional-argument bug and thirty-six
# slices ran as plain `VISLEAF=0`: they completed, reported nothing wrong, and reproduced the banked
# spectra -- which is exactly the shape that gets banked as an answer.*  66's instruction was that
# the fix should be STANDING rather than per-launcher: any switch whose effect is a bit-difference
# should print a marker and its launcher should fail if the marker is absent.
#
#   usage:  bash switch_smoke.sh NAME=VAL [NAME=VAL ...]
#
# It imports the instrument with exactly that environment -- which is where the switches are read,
# so no solver and no projection is needed -- and asserts that EVERY assignment appears in the
# `__SWITCHES__` line the instrument prints.  Exit 0 = the environment arrived; exit 1 = it did not,
# or the name is not one the instrument reads (a typo fails here instead of running silently).
#
# ⚠ ** WHAT IT DOES NOT PROVE, stated where it is built: that the value reached the PHYSICS. **  That
#   is the knob shadow (`r4558`, `cc66.36`) and it takes a differential, not a print.  A launcher
#   whose switch has a cheap observable signature should grep for THAT too -- see `r6929_directions`.
cd "$(dirname "$0")" || exit 1
[ $# -ge 1 ] || { echo "switch_smoke: no assignments given"; exit 2; }
LINE=$(env "$@" python3 -c 'import ACOUSTIC_two_arm' 2>/dev/null | grep -m1 '^__SWITCHES__ ')
[ -n "$LINE" ] || { echo "switch_smoke: FAIL -- the instrument printed no __SWITCHES__ line"; exit 1; }
rc=0
for a in "$@"; do
  case " $LINE " in
    *" $a "*) echo "  switch_smoke: OK   $a" ;;
    *) echo "  switch_smoke: FAIL $a  -- not in: $LINE"; rc=1 ;;
  esac
done
exit $rc
