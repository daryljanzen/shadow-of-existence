#!/bin/bash
# ** HOW MANY INSTRUMENT SOLVERS ARE RUNNING -- read from /proc/*/environ, never from a name test. **
#
#   A bare `pgrep ACOUSTIC_two_arm` or `ps | grep` matches the grep's own command line, an editor
#   holding the file open, and any wrapper shell whose argv carries the name.  ⇒ *That is how a
#   launcher decides nothing is running while four solvers are, or relaunches on top of a live set.*
#   The environment is the authority: a solver process HAS the instrument in its argv-derived
#   environment and nothing else does.
#
# ⌗ ** AND THE STDERR SUPPRESSION HAS TO BE ON `cat`, NOT ON THE REDIRECT. **  Written
#   `tr ... < "$p/environ" 2>/dev/null`, the `2>/dev/null` applies to `tr` -- but the failure is
#   BASH's, opening an unreadable or already-exited /proc entry before `tr` ever starts, so it prints
#   anyway.  *Measured: one line per unreadable entry, about seventy per call, which buries whatever
#   the log was supposed to show.*  Piping from `cat` makes the failure `cat`'s and suppressible.
live () {
  local n=0 p
  for p in /proc/[0-9]*; do
    cat "$p/environ" 2>/dev/null | tr '\0' '\n' | grep -q 'ACOUSTIC_two_arm' && n=$((n + 1))
  done
  echo "$n"
}
# and what each one is writing, which is what tells a resumed launcher where it got to
live_targets () {
  local p
  for p in /proc/[0-9]*; do
    cat "$p/environ" 2>/dev/null | tr '\0' '\n' | grep -q 'ACOUSTIC_two_arm' || continue
    cat "$p/environ" 2>/dev/null | tr '\0' '\n' | grep -m1 '^SAVE='
  done | sort -u
}
if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  echo "solvers live: $(live)"
  live_targets
fi
