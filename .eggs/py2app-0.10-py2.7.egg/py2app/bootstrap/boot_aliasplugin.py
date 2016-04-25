import re, sys
cookie_re = re.compile(b"coding[:=]\s*([-\w.]+)")
if sys.version_info[0] == 2:
    default_encoding = 'ascii'
else:
    default_encoding = 'utf-8'

def guess_encoding(fp):
    for i in range(2):
        ln = fp.readline()

        m = cookie_re.search(ln)
        if m is not None:
            return m.group(1).decode('ascii')

    return default_encoding

def _run():
    global __file__
    import os, site
    sys.frozen = 'macosx_plugin'
    base = os.environ['RESOURCEPATH']

    if 'ARGVZERO' in os.environ:
        argv0 = os.path.basename(os.environ['ARGVZERO'])
    else:
        argv0 = None
    script = SCRIPT_MAP.get(argv0, DEFAULT_SCRIPT)

    sys.argv[0] = __file__ = path = os.path.join(base, script)
    if sys.version_info[0] == 2:
        with open(path, 'rU') as fp:
            source = fp.read() + "\n"
    else:
        with open(path, 'rb') as fp:
            encoding = guess_encoding(fp)

        with open(path, 'r', encoding=encoding) as fp:
            source = fp.read() + '\n'

    exec(compile(source, script, 'exec'), globals(), globals())
