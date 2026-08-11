#!/usr/bin/env bash
# BOOTSTRAP_THE_REPO.sh -- turn an unpacked bundle into the repo, in one run.
#
# Run it from INSIDE the unpacked tree (the directory holding CORPUS_MAP.md).
# It does nothing destructive: it refuses if a .git already exists, and it does
# not push until it has shown you what it is about to push.
#
#   ./BOOTSTRAP_THE_REPO.sh https://github.com/<you>/<repo>.git
#
set -euo pipefail

REMOTE="${1:-}"
if [[ -z "$REMOTE" ]]; then
  echo "usage: $0 https://github.com/<you>/<repo>.git"; exit 1
fi
if [[ ! -f CORPUS_MAP.md ]]; then
  echo "⛔ not in the tree root -- CORPUS_MAP.md not found here"; exit 1
fi
if [[ -d .git ]]; then
  echo "⛔ a .git already exists here.  Refusing, so nothing is clobbered."; exit 1
fi

REV=$(grep -m1 -oE '^### Revision r[0-9]+' CORPUS_MAP.md | grep -oE 'r[0-9]+')
echo "── bootstrapping the repo at revision ${REV}"
echo

git init -b main
git add -A

# ** THE DRY RUN CAUGHT THIS: on a repo with no commits yet there is no HEAD, so
# `git diff --cached` compares against nothing and reports every file as absent.
# The first run of this script printed MISSING for all six required files while
# 1716 objects sat staged.  ** A check that reports absence because it looked in
# the wrong place is worse than no check: it would have stopped a correct push. **
# `git ls-files` reads the index directly and needs no HEAD.
STAGED=$(git ls-files)

echo
echo "── what will be committed:"
echo "   $(echo "$STAGED" | wc -l) files"
echo
echo "── sanity: these must all be present"
for f in .gitignore .gitattributes .github/workflows/gates.yml THE_HUB.md \
         THE_LIVE_ARC.md corpus/check_id_bands.py; do
  # ** FIXED r2420, AND THE MECHANISM IS WORTH THE COMMENT because it will bite
  # anything else that pipes into `grep -q` under `set -o pipefail`.
  # The first real run of this script printed MISSING for five files that were
  # demonstrably staged (`git ls-files` listed them), and passed only the sixth.
  # CAUSE: `grep -q` exits the instant it matches; `echo` still has output to
  # write and takes SIGPIPE; `pipefail` then reports the PIPELINE as failed, so
  # the `if` takes the else branch.  ** The split was by SORT ORDER: dotfiles and
  # THE_* sort early in `git ls-files` (instant match -> SIGPIPE), while
  # corpus/check_id_bands.py sorts late enough that grep had consumed almost all
  # the input first. **  It did not reproduce on Linux because a 64 KB pipe
  # buffer swallows the whole ~40 KB list; macOS's is 16 KB.
  # A here-string uses a temp file, not a pipe, so there is no SIGPIPE to take.
  # ** A check that reports absence because its own pipeline died is worse than
  #    no check: this one would have stopped a correct push. **
  if grep -qxF "$f" <<< "$STAGED"; then echo "   ok      $f"
  else echo "   MISSING $f"; fi
done
echo
echo "── and these must NOT be (build cruft the .gitignore excludes):"
if grep -qE '\.(aux|log|fls|fdb_latexmk|synctex\.gz)$' <<< "$STAGED"; then
  echo "   ⛔ build artefacts staged -- stop and check .gitignore"; exit 1
else
  echo "   ok      no LaTeX build artefacts staged"
fi

# ** ALSO CAUGHT BY THE DRY RUN: git refuses to commit without an identity, and
# the error arrives AFTER the checks pass -- so a first-time user sees six green
# lines and then a fatal.  Set it locally if it is unset; never touch --global.
if ! git config user.email >/dev/null 2>&1; then
  echo
  echo "── no git identity set; setting one for THIS REPOSITORY only"
  git config user.email "${GIT_EMAIL:-you@example.com}"
  git config user.name  "${GIT_NAME:-Daryl Janzen}"
  echo "   set to: $(git config user.name) <$(git config user.email)>"
  echo "   ** override before running with:  GIT_EMAIL=... GIT_NAME=... $0 ... **"
fi

git commit -q -m "${REV} — the consolidated corpus: 21 gates, the entry-point front worked once through, R-M station C closed"
git remote add origin "$REMOTE"

echo
echo "── committed locally.  Nothing has been pushed yet."
echo "   To push:   git push -u origin main"
echo "   Then:      git branch line/56 && git push -u origin line/56"
