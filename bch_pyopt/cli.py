#!/usr/bin/env python3

import sys
sys.argv.append('')
while sys.argv[1].startswith('_'):
    opt = sys.argv.pop(1)[1:]
    if opt == 'docparse':
        import bch_pyopt.quick.docparse
    if opt == 'cli':
        def cli(): pass
try:
    cli
except NameError:
    from bch_pyopt.original.cli import cli

sys.argv.pop(-1)
cli()
