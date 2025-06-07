#!/usr/bin/env python3
1

import os
import sys

import bch_pyopt.quick.docparse as DP
from bch_pyopt.quick.docparse import parse, main

VERSION = 'zero'

def cmd_foo(*args):
    """foo [OPTIONS] ARGS
       -n int
       -f True
       -colors list
       This is a good function.
    """
    opts, args = DP.parse(cmd_foo, args)

def _usage(*args):
    NAME = __file__.split('/')[-1]
    print( f"{NAME} (version {VERSION})\n\nUSAGE:" )
    for fn  in globals().values():
        if not type(fn) == type(_usage): continue
        if not fn.__name__.startswith('cmd_'): continue
        if fn.__doc__ is None: continue
        print(f"\n{NAME} {fn.__doc__}")

def _null(*args):
    print( 'null', args )

if __name__ == "__main__":
    DP.main(sys.argv[1:], globals())
