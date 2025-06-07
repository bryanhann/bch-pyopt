#!/usr/bin/env bash

for pth in $(ls $(dirname ${BASH_SOURCE[0]})/[0-9]*); do
    bch:000:debug . ${pth}
    source ${pth}
done

