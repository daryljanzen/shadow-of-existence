#!/usr/bin/env python3
"""Every URL the sitemap advertises resolves to a file in the ASSEMBLED site.

** WHY THIS ASKS ITS QUESTION OF `_site` AND NOWHERE ELSE. **  At `r7425` the
formalisation page was generated, linked from the index, linked 68 times from
`receipts.html` and listed in the sitemap, and `pages.yml`'s assemble step --
which carried its own hand-written list of files to copy -- did not copy it.
The public site answered `404` at a URL its own sitemap was advertising to
search engines, for ten hours, and the trunk ran 129 of 130 green throughout.
**Every check in the repository was running in `BOOK_INTRO_cosmiCave/`, which
is the directory that was green all along.**  `r7433` removed the second list,
so that exact failure cannot recur; this gate exists because the question
"does the thing the reader fetches exist" had never been asked of the thing
the reader fetches.

** AND IT ASSERTS THE SITEMAP'S OWN PRESENCE, WHICH IS NOT A FORMALITY. **
`sitemap.xml` is copied into `_site` with `2>/dev/null || true`, so a failed
copy ships a site with no sitemap and a green job.  A gate that reads the
sitemap and finds no sitemap would otherwise pass vacuously -- `r7425`'s
"the negative path passing is no evidence that the positive one exists".

** WHAT IT BUYS, STATED PLAINLY: NOTHING TODAY. **  `cc66` measured it before
it was built -- 25 `<loc>` entries, 25 `PAGES.txt` entries, 0 sitemap paths
outside `PAGES.txt`.  Its value is that the two artifacts are compared as
artifacts.  That they come from one list in the generator is a property of
the generator's code, and a later edit building the sitemap from a second
list would break that premise with nothing to notice.

Usage:  python3 corpus/check_sitemap_resolves.py <site-dir>      (default: _site)
"""
import os
import re
import sys


def main():
    site = sys.argv[1] if len(sys.argv) > 1 else '_site'
    smap = os.path.join(site, 'sitemap.xml')

    if not os.path.isdir(site):
        print(f'  ⛔ {site}/ does not exist -- nothing was assembled.')
        return 1
    # Asserted before it is read: see the header.
    if not os.path.exists(smap) or os.path.getsize(smap) == 0:
        print(f'  ⛔ {smap} is missing or empty.  The sitemap is copied with '
              '`|| true`, so a failed copy ships a site that advertises nothing '
              'and a job that passes.')
        return 1

    text = open(smap, encoding='utf-8').read()
    locs = re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', text)
    if not locs:
        print(f'  ⛔ {smap} carries no <loc> entries.  A sitemap advertising '
              'nothing is not a sitemap that passed.')
        return 1

    bad = []
    for url in locs:
        # Everything after the host; the bare root is served by index.html.
        rel = re.sub(r'^https?://[^/]+/?', '', url)
        rel = rel or 'index.html'
        path = os.path.join(site, rel)
        if not os.path.exists(path):
            bad.append((url, rel, 'no such file in the assembled site'))
        elif os.path.getsize(path) == 0:
            bad.append((url, rel, 'present but empty'))

    print(f'  sitemap: {len(locs)} advertised url(s), read from {smap}')
    if bad:
        print(f'  ⛔ {len(bad)} ADVERTISED URL(S) DO NOT RESOLVE IN {site}/:')
        for url, rel, why in bad:
            print(f'    [FAIL] {url}')
            print(f'           → {rel}: {why}')
        print('     ⌗ A reader following the sitemap gets a 404 at each of these.')
        print('       The page list lives in BOOK_INTRO_cosmiCave/PAGES.txt and the '
              'deploy copies it;')
        print('       a url here that is not there means the two have come apart again.')
        return 1

    print(f'  ✓ all {len(locs)} resolve to a non-empty file in {site}/.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
