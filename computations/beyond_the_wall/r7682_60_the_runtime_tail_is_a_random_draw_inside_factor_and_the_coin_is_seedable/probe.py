"""r7682 (60) -- CATCH THE SLOW PATH IN THE ACT AND NAME THE LINE.

One fresh process per trial, the cores otherwise idle, the suite's own child environment.  Each
trial installs `faulthandler.dump_traceback_later(STALL, repeat=True)`, so a trial that runs longer
than `STALL` seconds prints WHERE IT IS, every `STALL` seconds, and keeps printing.  A fast trial
prints nothing.  ⇒ The first slow trial names its own line.
"""
import faulthandler, os, runpy, sys, time
STALL = int(os.environ.get('STALL', '45'))
faulthandler.dump_traceback_later(STALL, repeat=True, file=sys.stderr)
t0 = time.time()
try:
    runpy.run_path(sys.argv[1], run_name='__main__')
except SystemExit as e:
    print(f"__EXIT__ {e.code}", file=sys.stderr)
print(f"__WALL__ {time.time() - t0:.1f}", file=sys.stderr)
