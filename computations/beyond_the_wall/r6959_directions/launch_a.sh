#!/bin/bash
# ** r6959 ⓵ᵃ -- THE SOURCE'S CONFORMAL-TIME DEPENDENCE ACROSS THE WINDOW, ON BOTH ARMS. **
#
#   The profile is a property of the SOURCE and not of the projection, so it is taken at `LSTEP=8`
#   (238 multipoles) while `LMAXL=2000` keeps the k-grid character-identical to `r6941_fine_*`, which
#   is the bank the contrast is measured on.  *Same modes, same source, an eighth of the kernel work.*
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6959; mkdir -p $D/eta
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"

run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SRCETA=$out/$tag.npz SAVE=$out/${tag}_dl.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the instrument's switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
  [ $rc -eq 0 ] || { echo "  ⛔ $tag FAILED"; return 1; }; }
export -f run; export D

echo "=== the standing switch guard, on every distinct environment, before the set goes out ==="
ok=1
bash switch_smoke.sh $LCDM LSTEP=8 LMAXL=2000 SRCETA=/tmp/n66/r6959/x.npz || ok=0
bash switch_smoke.sh $CR   LSTEP=8 LMAXL=2000 SRCETA=/tmp/n66/r6959/x.npz || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

printf '%s\n%s\n' "$D/eta eta_lcdm $LCDM LSTEP=8 LMAXL=2000" \
                  "$D/eta eta_cr   $CR   LSTEP=8 LMAXL=2000" | xargs -P 2 -I{} bash -c 'run {}'
echo "=== r6959 A LAUNCH COMPLETE $(date -u) ==="
grep -h "SRCETA:" $D/eta/*.log
