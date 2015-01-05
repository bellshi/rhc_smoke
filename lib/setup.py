#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /lib
# Author : cshi
# Date : 4.Jan.2015

from option import *

class init:
    
    def __init__(self,config):
        
        self.__config = config

    def print_log_info(self):

        print "|- result: result/rhc_smoke_test.result"
        print "----------------------------"

    def print_config_info(self):

        print "------ RHC SMOKE TEST ------"
        print "|- account : %s" %(self.__config.get('default_rhlogin'))
        print "|- password : %s" %(self.__config.get('default_rhpasswd'))
        print "|- env : %s" %(self.__config.get('libra_server'))

    def setup(self):
        
        self.print_config_info()
        self.print_log_info()

#DEBUG
if __name__ == "__main__" :

    cfg = config().setup()
    si = init(cfg)
    si.setup()
