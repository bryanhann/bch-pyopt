#!/usr/bin/env python3

def isflag4tokens(tokens):
    return tokens and tokens[0].startswith('-')

def isarg4tokens(tokens):
    return tokens and not tokens[0].startswith('-')

class Option:
    def __init__(self, line):
        parts = line.strip().split()
        self._flag = parts.pop(0)
        self._name = self._flag.split('-')[-1]
        self._tipe = eval(parts.pop(0))
        if self._tipe in (True, False): self._value = self._tipe
        elif self._tipe == list:        self._value = []
        else:                           self._value = None

    def __repr__(s):
        return f"<{s._flag} : {s._name} : {s._tipe} : {s._value}>"

    def consume(s,tokens):
        if s._tipe == list:
            while isarg4tokens(tokens):
                s._value.append(tokens.pop(0))
        elif s._tipe in [ True, False ]:
            s._value = not s._value
        else:
            try:
                s._value = s._tipe(tokens.pop(0))
            except IndexError:
                raise ValueError( f'flag {s._flag} requires an argument' )
            except ValueError:
                raise ValueError( f'flag {s._flag} expected type {s._tipe}.' )

def parse(fn, args):
    class Namespace:
        def __repr__(self):
            return str(self.__dict__)
    tokens = list(args)
    if fn.__doc__ is None:
        flags = ()
    else:
        lines = fn.__doc__.split('\n')
        lines = [ o.strip() for o in lines if o.strip().startswith('-') ]
        options = [ Option(line) for line in lines ]
        flags = dict( (o._flag, o) for o in options )

    while isflag4tokens(tokens):
        flag = tokens.pop(0)
        if flag == '--':
            break
        elif flag in flags:
            flags[flag].consume(tokens)
        else:
            raise ValueError( f"bad flag: {flag}" )
    opts = Namespace()
    for flag in flags.values():
        setattr(opts, flag._name, flag._value )
    return opts, tokens

def main(args, glob):
    try:               fn = glob[f"cmd_{args.pop(0)}"]
    except IndexError: fn = glob['_null']
    except KeyError:   fn = glob['_usage']
    fn(*args)

