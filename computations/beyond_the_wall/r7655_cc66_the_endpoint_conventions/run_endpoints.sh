#!/usr/bin/env bash
# r7655 (cc66), ordered by 69 item 1 -- ** r_D UNDER EVERY DEFENSIBLE ENDPOINT CONVENTION, ON ALL
# THREE ARMS, BECAUSE P15 l.2387-2388 STATES A SECOND CONVENTION THAT NO BANKED LOG CARRIED. **
#
# Every banked log in this corpus reports exactly ONE endpoint -- `r_D at the visibility peak` -- and
# to TWO DECIMALS.  The paragraph's other-convention sentence ("their separation in the governing
# ratio widens tenfold and the difference between them changes sign, at 0.14 degrees") therefore had
# no carrier on any arm.  `ACOUSTIC_two_arm.py` now prints the whole endpoint table beside its
# original line, additively, at six decimals (r7655).
#
# ⛭ ** THESE RUNS ARE CHEAP AND THAT IS A MEASUREMENT, NOT AN ASSUMPTION. **  r_D is a BACKGROUND
#   quantity: it comes out of the opacity and the rate through `kD2inv_of`, which is built before
#   the hierarchy is touched.  So `LMAXL=100 LSTEP=50` -- a spectrum nobody reads -- gives the SAME
#   r_D as the production banks, and each run finishes in about EIGHT SECONDS instead of the
#   production run's hours.  ⇒ ** The check that this is legitimate is in the receipt and is not
#   taken on trust: each log's two-decimal visibility-peak line must equal the production bank's,
#   7.10 / 7.12 / 7.26, or the gate fails. **  Do not "speed up" a receipt figure this way without
#   that check -- it is the whole licence for the shortcut.
set -euo pipefail
# ⌗ OUT is resolved BEFORE the cd: `$0`'s relative dirname stops resolving once the shell has moved.
OUT="$(cd "$(dirname "$0")" && pwd)"
cd "$OUT/.."                                 # computations/beyond_the_wall

run () {  # run <outfile> <switches...>
  local out="$1"; shift
  env "$@" LMAXL=100 LSTEP=50 python3 "$OUT/endpoints.py" > "$OUT/$out" 2>&1
  printf '  %-34s %s\n' "$out" "$(grep -m1 'visibility peak =' "$OUT/$out")"
}

run control_lcdm.log              ARM=lcdm ZSTART=3e7
run namesake_arm_cr.log           ARM=cr CRH0=68.60 CROM=0.2973 HIER=1 LEAFGEOM=1 LEAFSCALES=1 ZSTART=3e7
run arm_of_record_cr_leafrec1.log ARM=cr CRH0=68.570730 CROM=0.291246 HIER=1 LEAFGEOM=1 LEAFREC=1 \
                                  LEAFSCALES=1 NS=1.015066 WBH2=0.021643 ZSTART=3e7
