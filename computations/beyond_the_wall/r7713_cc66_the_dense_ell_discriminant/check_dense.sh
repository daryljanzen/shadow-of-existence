#!/bin/bash
# ⛭ r7713 / r7715 — the dense-`l` discriminant's STATUS READER.
#
# ⛔ IT NO LONGER RELAUNCHES ANYTHING, AND THAT IS r7715's RULING, NOT AN OMISSION.  The three
#    remaining combinations run as a CI matrix (`.github/workflows/dense-ell.yml`), one per runner,
#    and 69's instruction was explicit: stop the in-container relaunching once the job is running,
#    because the check-in cycle is not where this belongs.  A relaunch here would now compute the
#    SAME combinations a second time on a DIFFERENT machine, and then two sources would exist for
#    one object -- which is the exact fault class this revision spent the evening catching.
#
# ⚠ THREE UNSOUND PROCESS TESTS ARE RECORDED, each of which answered a different question from the
#   one asked, and none is to be used again:
#   ① a bare `pgrep dense.py` NAME test (r7711+cc66.3) -- answers "does something matching exist".
#   ② a /proc scan that joined each argv into one string and substring-matched it -- THE SCANNING
#     SHELL'S OWN COMMAND LINE CONTAINS THE PATTERN, so it matched itself and reported a runner when
#     there was none.  Only the machine's uptime, read independently, contradicted it.
#   ③ a /proc scan requiring the BARE name as an exact argv element -- which silently missed the
#     wrapper, because the wrapper is launched by FULL PATH, so `run_dense.sh` never appears as an
#     element and three rounds of kills reported success while it respawned the job each time.
#   ⇒ What is sound, below: exclude this PID, and match each argv element against the script's PATH
#     SUFFIX (`(^|/)name$`) so neither a full path nor a mere mention is confused with the real thing.
set -u
cd "$(dirname "$0")"
D="$(pwd)"
echo "uptime=$(cut -d. -f1 /proc/uptime)s"
BSZ=$(sed -n 's/^BLOCK = \([0-9]*\).*/\1/p' "$D/dense.py" | head -1)
PER=$(( (693 + BSZ - 1) / BSZ ))
echo "local scratch blocks=$(ls "$D"/pseudo/block__*.npy 2>/dev/null | wc -l) (${PER} per combination at BLOCK=${BSZ}; the CI jobs keep their own)"
echo "banked spectra=$(ls "$D"/pseudo/pseudo__*.npz 2>/dev/null | wc -l)/4:"
for f in "$D"/pseudo/pseudo__*.npz; do [ -e "$f" ] && echo "    $(basename "$f")"; done
self=$$
n=0
for p in /proc/[0-9]*/cmdline; do
  pid=${p%/cmdline}; pid=${pid#/proc/}
  [ "$pid" = "$self" ] && continue
  c=$(tr '\0' '\n' < "$p" 2>/dev/null) || continue
  case "$c" in *turn_gates*) continue;; esac
  if printf '%s' "$c" | grep -qE '(^|/)dense\.py$' || printf '%s' "$c" | grep -qE '(^|/)run_dense\.sh$'; then
    n=$((n+1)); echo "    ⚠ STILL RUNNING IN-CONTAINER: pid=${pid} -- r7715 says this should be stopped"
  fi
done
echo "in-container runners=${n}   (0 is correct now)"
echo "--- the CI refs, which is where the three remaining combinations arrive:"
git fetch origin '+refs/ci/dense_ell/*:refs/remotes/ci/dense_ell/*' -q 2>/dev/null || echo "    (fetch failed; network or no such ref yet)"
got=0
for tag in lcdm_cr cr_lcdm cr_cr; do
  if sha=$(git rev-parse --verify -q "refs/remotes/ci/dense_ell/${tag}"); then
    got=$((got+1))
    echo "    ${tag}: ${sha:0:9}  $(git log -1 --format=%s "$sha" | cut -c1-80)"
  else
    echo "    ${tag}: not yet"
  fi
done
echo "CI combinations available=${got}/3"
echo "⇒ to bank one:  git show refs/remotes/ci/dense_ell/<tag>:pseudo__S_<src>__K_<ker>.npz > pseudo/pseudo__S_<src>__K_<ker>.npz"
echo "⇒ all four banked ⇒ run analyse.py.  Fewer ⇒ it refuses, by design."
