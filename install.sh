#!/usr/bin/env bash
$BH1
cd $(dirname $0)
bh0 bch lbin4repo $PWD
cd app
uv sync
