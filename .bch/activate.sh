#!/usr/bin/env bash

r=$(dirname $(dirname ${BASH_SOURCE[0]}))

export BCH_PYOPT__root=${r}
export BCH_PYOPT__init=${r}/.bch/activate.sh
export BCH_PYOPT__lbin=${r}/.bch/lbin
export BCH_PYOPT__bin=${r}/.bch/bin
export BCH_PYOPT__lib=${r}/.bch/lib

bch:000:linkall ${r}/.bch/lbin

source ${r}/.bch/init/init.sh

unset r
