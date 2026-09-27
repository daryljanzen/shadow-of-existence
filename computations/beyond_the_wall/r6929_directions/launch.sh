#!/bin/bash
# ** r6929's order: THE COMB IS NOW THE ARBITER, SO MEASURE WHAT IT CAN ACTUALLY DECIDE. **
#
#   `cc66.43` made the comb the load-bearing reading -- it is the one with an external referent, and
#   it supports the assignment the instrument has.  ⚠ ** But the corpus has never measured how
#   sharply it discriminates, and a reading promoted to arbiter needs its RESOLUTION stated before it
#   decides anything. **  So the assignment is scanned CONTINUOUSLY: `VISLEAF` is a fraction at
#   r6929+cc66.44, f=0 the stacking clock and f=1 the leaf's.
#
#   * the COMB half needs real spectra -- `comb_cr_f*`, the reported path, `LSTEP=8 LMAXL=2000`
#   * the CONTRAST half is read on BOTH the real spectra and the INJECTION (`inj_cr_f*`, a source
#     with no plasma dynamics in it), because the injection is what `r6925`'s table measured and it
#     is also what separates the order's guard: a cos(k r_s) source carries geometry and visibility
#     weighting ONLY, so if its comb moves with f and the real one moves with it, the motion is the
#     visibility's; if the real one moves further, the extra is the plasma's own phase.
#   * the CONTROL is not scanned: `Jac == 1` there by the rate identity, so every f is the same run
#     -- which is a GATE (`noop_lcdm_f050`) and not an assumption.
#   * f=1 is re-run under the NEW code and gated bit-identical against `r6925`'s banked `VISLEAF=1`:
#     the family's endpoint must BE the flag.
#
# ⛭⛭ ** AND THE LAUNCHER'S SWITCH GUARD IS NOW STANDING, not per-launcher (`../switch_smoke.sh`). **
#   *r6925's launcher dropped its extra environment and thirty-six slices ran as plain `VISLEAF=0`,
#   completing and reporting nothing wrong.*  Here: every distinct environment is smoke-tested before
#   the set goes out, AND every slice's own log is checked for the `__SWITCHES__` line carrying the
#   value asked for -- a slice whose environment did not arrive is NOT marked done and re-runs.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6929; mkdir -p $D/comb $D/inj $D/noop
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
FS="0 0.1 0.25 0.5 0.75 1"

# ---- the run function: the extra environment is "$@" AFTER the shift, r6925's lesson ------------
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  # ⛔ the per-slice switch check: the log must carry every assignment on its own __SWITCHES__ line
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the instrument's switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"
  echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
  [ $rc -eq 0 ] || { echo "  ⛔ $tag FAILED"; return 1; }; }
export -f run; export D

echo "=== the smoke test on every distinct environment, BEFORE the set goes out ==="
ok=1
for f in $FS; do
  bash switch_smoke.sh $CR VISLEAF=$f || ok=0
  bash switch_smoke.sh $CR VISLEAF=$f SRCINJ=sweep SRCINJRS=own || ok=0
done
bash switch_smoke.sh $LCDM VISLEAF=0.5 || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

echo "=== the gates: VISLEAF=0 is the unset path, and the CONTROL does not move at all ==="
printf '%s\n' \
 "$D/noop unset_cr      $CR   LSTEP=16 LMAXL=500" \
 "$D/noop zero_cr       $CR   LSTEP=16 LMAXL=500 VISLEAF=0" \
 "$D/noop noop_lcdm_f0  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_lcdm_f050 $LCDM LSTEP=16 LMAXL=500 VISLEAF=0.5" \
 | xargs -P 4 -I{} bash -c 'run {}'

echo "=== the scan: the comb and the injection on the arm, at six values of f ==="
LIST=""
add () { tag=$1; sub=$2; nk=$3; shift 3
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/$sub ${tag}_k${i} $* KSLICE=${i}:${j}"
    i=$j
  done; }
for f in $FS; do
  t=$(echo "$f" | tr -d '.')
  add comb_cr_f$t comb 1452 $CR LSTEP=8 LMAXL=2000 VISLEAF=$f
  add inj_cr_f$t  inj  1452 $CR LSTEP=8 LMAXL=2000 VISLEAF=$f SRCINJ=sweep SRCINJRS=own
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6929 LAUNCH COMPLETE $(date -u) ==="
