#!/bin/sh

BASEPATH=$(cd `dirname $0` ; pwd)
BASEENV=$(python -V ; awk -F )

export PATH=$PATH:$BASEPATH/lib

if ( $BASEENV)
