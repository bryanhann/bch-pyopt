#!/usr/bin/env bash

. bch.pyopt.activate.sh > /dev/null 2> /dev/null

fn_py_exit() { python3 -c "exit()"; }
fn_version() { bch.pyopt --version; }
fn_true () { true; }


for n in $(seq 50); do
    it=$(( $n * 5 ))
    ii=${it}
    t0=$(python3 -c "import time;print(time.time())")
    while [ ! $ii = 0 ]; do
        ii=$(( $ii - 1 ))
        $* >&2
    done
    t1=$(python3 -c "import time;print(time.time())")
    ms=$(python -c "print(int(1000*($t1-$t0)/$it))" )
    echo "$it: $ms ms"
done
