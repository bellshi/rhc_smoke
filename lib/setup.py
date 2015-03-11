#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /lib
# Author : cshi
# Date : 4.Jan.2015
import config


def print_log_info():
    print "|- result: result/rhc_smoke_test.result"
    print "----------------------------"


def print_config_info(smokeconfig):
    print "------ RHC SMOKE TEST ------"
    print "|- account : %s" % (smokeconfig.get('default_rhlogin'))
    print "|- password : %s" % (smokeconfig.get('default_rhpasswd'))
    print "|- env : %s" % (smokeconfig.get('libra_server'))


def setup(smokeconfig):
    print_config_info(smokeconfig)
    print_log_info()



# DEBUG
if __name__ == "__main__":
    cfg = config.setup()
    setup(cfg)
