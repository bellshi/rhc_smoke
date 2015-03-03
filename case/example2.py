#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Jan.2015

import logging
import pexpect
import lib.config
from lib.check import check_no_input



class SmokeCase:
    case_name = 'rhc server verification - 2'

    step1_cmd = 'rhc servers'
    step2_cmd = 'rhc setup'
    step3_cmd = 'rhc setup --server a.com'

    step1_check = 'Your client tools are now configured'
    step2_check = 'Your client tools are now configured'
    step3_check = 'The OpenShift server is not responding correctly'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        return

    def test(self):
        #step 1
        #step 2
        # child = pexpect.spawn(step2_cmd)
        # index = child.expect(['Enter the server hostname'])
        # if index == 0 :
        #     index = child.sendline()
        #     index = child.expect([step1_check])
        #     if index == 0 :
        #         print 'pass'
        #     else :
        #         print 'fail'
        # else : 
        #     print 'fail'
        #step 3

# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
