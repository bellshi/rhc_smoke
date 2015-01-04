#!/bin/sh

BASE_PATH=$(cd `dirname $0` ; pwd)
PYTHON = `which python`

export PATH=$PATH:$BASEPATH/lib:$BASEPATH/config

if [-z $PYTHON];then
    echo 'Please install python.'
    exit 0
fi

