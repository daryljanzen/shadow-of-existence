# r7419+70 ②: RESULT. The formalisation workflows are invisible to READ_INDEX, and "is this Lean file under a GREEN workflow" cannot be answered from the tree. It can be answered exactly with one API read, and made locally answerable with one record ref.

Registration `b94344525` (14:26:32 UTC).

| | predicted | measured | verdict |
|---|---|---|---|
| **G-a** visible to READ_INDEX's nightly artifact | no | **no**: 0 of 1107 entries is a `.lean` path, and 0 traced reads end in `.lean`. The index header holds only `traced_at`. Neither workflow uploads an artifact or writes anything back. | **HOLDS** |
| **G-b** answerable from the tree alone | no | **no**: no committed file records a formalisation run's conclusion (searched every `.py`/`.json`/`.tsv`/`.txt` outside `.lake`) | **HOLDS** |
| **G-c** answerable through the API | yes | **yes, exactly**, with `green_under.py`; offline it prints UNANSWERABLE instead of guessing (`GREEN_UNDER_RUN.txt`) | **HOLDS** |
| EFFORT | `25` min | **≈ 15 min** (14:26 → ~14:41 UTC) | holds |

## The exact form of the question, and why it is not "the run at HEAD"

Both workflows are **path-scoped**:
- `formalisation-mathlib` runs on `computations/formalisation/lean/**`;
- `formalisation-physlib` runs on `lean-physlib/**` plus `lean/check_no_sorry.py`.

That holds on push and on pull request, so most commits have **no run of their own**. Asking for the run at
HEAD answers "no run" almost always, which is the wrong answer.

The exact question is whether there is a completed run at some commit H with
`git diff --quiet H HEAD -- <that workflow's paths:>`. If so, H's conclusion is HEAD's, because the workflow's
verdict is a function of those paths and nothing else.
- **The tree half is local and exact.**
- **Only the conclusion needs the API.**

Measured at HEAD and at `origin/main`, both answer **SUCCESS**:
- mathlib: run `38913994789` at `70c4d0ba9`.
- physlib: run `38329726052` at `dffdcb32f`, from 2026-10-13. Nothing under its paths has changed since.

## What a GATE would need, in each place

| where | can it answer? | what it needs |
|---|---|---|
| a seat's local run, offline | **no** | the verdict is not in the tree |
| a seat with `gh api` | **yes** (`green_under.py`) | nothing more |
| CI's `fast` job | **not as wired**: `permissions: { contents: read }` and no token in the step's env | `actions: read` and `GH_TOKEN: ${{ github.token }}` on that step. `fetch-depth: 0` is already set, so H resolves. |

⌗ **The stated limit.** A `pull_request` run builds the MERGE ref but reports the PR's `head_sha`. If the base
changed the Lean paths after the PR forked, the tree H names is not exactly the tree that was built. A gate that
counts only `push` runs avoids this, at the cost of waiting for the push.

## G-d, the proposal: make it locally answerable the way this repository already records CI state

The nightly and carry jobs push `refs/ci/nightly` and `refs/ci/carry` (PO-65, `contents: write` scoped to that
one step). **A last step in each formalisation workflow could push `refs/ci/lean/<workflow>`**: a one-line
record of `<head_sha> <tree-of-its-paths> <conclusion>`. A gate then answers locally with:
- `git fetch origin 'refs/ci/lean/*'`;
- a tree-hash comparison;
- no API and no token.

That is the same idiom as `check_index_coverage` reading a committed index.

**Not built:** it changes two workflows' permissions, and that is 66's call.

⇒ **For 60's gate:** the GREEN condition is evaluable, so it does not need to be dropped. But until either
the CI permission or the record ref exists, it is evaluable only by a seat with `gh api`, and not by the fast job
or an offline local run. A gate that carries it today must print UNANSWERABLE there, never pass.
