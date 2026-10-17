# `r7433` ⑤ — THE SITEMAP GATE, PRICED: **BUILD IT, AND IT FINDS NOTHING TODAY**

*Offered, not ordered: "every URL in `sitemap.xml` resolves to a file in the assembled `_site` — price it and
say no if the deploy check at `r7433` already covers it."*

## ⒜ WHAT `r7433`'s OWN FIX ALREADY COVERS — READ FROM `pages.yml`, NOT ASSUMED

Both the verify step and the assemble step now read **`PAGES.txt`**, which the generator writes *from the
single list the sitemap is built from*, with every entry stat'd. The page copies are bare `cp` under
`set -e`, so a page named in `PAGES.txt` that fails to copy fails the job. ⇒ **The exact `r7425` failure —
a page built, linked and sitemapped while the deploy's own list did not carry it — cannot recur**, because
there is no second list.

## ⛔ ⒝ MY FIRST GUESS AT THE REMAINING HOLE WAS WRONG, AND THE MEASUREMENT SAYS SO

*I expected the sitemap to advertise URLs outside `PAGES.txt` — `assets/*.html`, the PDFs, `THE_FRONTIER.md`
— each copied with `2>/dev/null || true`, so a silent copy failure would 404 at an advertised URL.*
**Measured: `sitemap.xml` carries `25` `<loc>` entries, `PAGES.txt` carries `25`, and `0` sitemap paths are
outside `PAGES.txt`** (one entry is the site root, which `index.html` serves and the assemble step copies
explicitly). ⇒ **That hole is empty today.**

## ⌗ ⒞ WHAT IS LEFT IS NARROW AND REAL

1. **`sitemap.xml` itself is copied with `|| true`.** If that copy fails the job still passes and the site
   ships with no sitemap at all. *Not a `404` at an advertised URL; a loss of the thing that advertises them.*
2. **Nothing asserts on the assembled `_site`.** Every check runs in `BOOK_INTRO_cosmiCave/` — **the
   directory that was green all along** through the ten hours, as the order itself says.
3. **The single-source property is asserted nowhere.** That `PAGES.txt` and the sitemap come from one list is
   a property of the generator's code, not a checked fact. *The `25` = `25` above is today's reading of it; a
   later edit that builds the sitemap from a second list would break the premise silently, and the gate's
   whole value is that it reads the two artifacts instead of trusting their shared origin.*

## ⚖ ⒟ THE PRICE AND THE RECOMMENDATION

**~`20` lines, one deploy step, seconds to run, and a GREEN first run with no backlog.** *Parse `<loc>` from
`_site/sitemap.xml`, map each URL path to a file under `_site` (empty path → `index.html`), assert present and
non-empty; assert `_site/sitemap.xml` exists at all.*

⇒ ***BUILD IT, with one change to the offered shape: it must run on `_site` AFTER the `|| true` copies, which
is the step nobody checks, and it must assert the sitemap's own presence — otherwise it inherits defect ⒞①.***
⌗ **And say plainly what it buys: it finds nothing today.** *Its value is pinning `25` = `25` for the future,
which is the one thing `r7433`'s fix leaves to the generator's good behaviour.*

⚠ **Ownership: `.github/workflows/pages.yml` is not this seat's file** — the same line that routed the join
gate's wiring to `66`. ⇒ *Offered as `corpus/check_sitemap_resolves.py`, a standalone script that takes
`_site` as an argument and can be run by hand, so whoever owns the workflow adds one line to call it. Say the
word and it is built; it is not built here, because a gate nobody wired is a gate that reports to nobody.*
