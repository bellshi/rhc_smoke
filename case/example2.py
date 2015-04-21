#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Jan.2015

import logging
import logging.config
import lib.config
from lib.check import *


class SmokeCase:
    case_name = 'rhc server verification - 2'

    step1_cmd = 'rhc servers'
    step2_cmd = 'rhc server add {0}'
    step3_cmd = 'rhc server use --server {0}'
    step4_cmd = 'rhc server list | grep {0}'
    step5_cmd = 'rhc logout'
    step6_cmd = 'rhc server add {0} {1}'
    step7_cmd = 'rhc server add a.com'
    step8_cmd = 'rhc server configure --hostname {0} --nickname {1} --server {2}'
    step9_cmd = 'rhc server show --server {0}'
    step10_cmd = 'rhc server status --server {0}'
    step11_cmd = 'rhc server remove {0}'

    step1_check = 'You have (\w+) (\w+) configured'
    step3_check = 'Now using'
    step4_check = 'Server'
    step5_check = 'All local sessions removed'
    step7_check = 'The OpenShift server is not responding correctly'
    step8_check = 'Saving server configuration to'
    step9_check = 'Server'
    step10_check = 'Using API version'
    step12_check = 'Removing'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    def test(self):
        # debug logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        check_no_input(self.step1_cmd, self.step1_check)
        # step 2
        if 'int' in self.server:
            step2 = self.step2_cmd.format('stg.openshift.redhat.com')
            step3 = self.step3_cmd.format('stg.openshift.redhat.com')
            step4 = self.step4_cmd.format('stg')
            step6 = self.step6_cmd.format('int.openshift.redhat.com', 'int')
            step8 = self.step8_cmd.format('int.openshift.redhat.com', 'intest', 'int.openshift.redhat.com')
            step9 = self.step9_cmd.format('int.openshift.redhat.com')
            step10 = self.step10_cmd.format('stg.openshift.redhat.com')
            step11 = self.step11_cmd.format('stg.openshift.redhat.com')
            step12_e = self.step11_cmd.format('int.openshift.redhat.com')
            step13_e = self.step3_cmd.format('int.openshift.redhat.com')
        else:
            step2 = self.step2_cmd.format('int.openshift.redhat.com')
            step3 = self.step3_cmd.format('int.openshift.redhat.com')
            step4 = self.step4_cmd.format('stg')
            step6 = self.step6_cmd.format('stg.openshift.redhat.com', 'stage')
            step8 = self.step8_cmd.format('stg.openshift.redhat.com', 'stgtest', 'stg.openshift.redhat.com')
            step9 = self.step9_cmd.format('stg.openshift.redhat.com')
            step10 = self.step10_cmd.format('int.openshift.redhat.com')
            step11 = self.step11_cmd.format('int.openshift.redhat.com')
            step12_e = self.step11_cmd.format('stg.openshift.redhat.com')
            step13_e = self.step3_cmd.format('stg.openshift.redhat.com')

        check_add_server(step2, self.login, self.password)
        # step 3
        check_no_input(step3, self.step3_check)
        # step 4
        #check_no_input(step4, self.step4_check)
        # step 5
        check_no_input(self.step5_cmd, self.step5_check)
        # step 6
        check_no_input(step12_e, self.step12_check)
        check_add_server(step6, self.login, self.password)
        # step 7
        check_no_input(self.step7_cmd, self.step7_check)
        # step 8
        check_no_input(step8, self.step8_check)
        # step 9
        check_no_input(step9, self.step9_check)
        # step 10
        check_no_input(step10, self.step10_check)
        # step 11
        check_no_input(step13_e, self.step3_check)
        check_no_input(step11, self.step12_check)

        logger.info('end')

# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
