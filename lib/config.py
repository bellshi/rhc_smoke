#!/usr/bin/env python

# Project :  rhc_smoke 
# Loc : /lib
# Author : cshi
# Date : 30.Dec.2014

cfg = {}
config_path = '../config/express.conf'

def readconfig():
    cfile = open(config_path, 'r')
    for line in cfile:
        line = line.strip('\n')
        if not line.startswith("#") and not line.count('\n') == len(line):
            cfg[line.split('=')[0]] = line.split('=')[1]


def get(self, key):
    if key in self.cfg:
        return self.cfg.get(key)
    else:
        return ""


def getconfig():
    return cfg


def setup():
    readconfig()
    return getconfig()

# DEBUG
if __name__ == "__main__":
    print setup()

