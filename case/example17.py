#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 5.Mar.2015

import logging
import logging.config
import lib.config
from lib.check import *


class SmokeCase:
    case_name = 'rhc member verification - 17'

    step1_cmd = 'rhc member add {0} -n cshi -r admin'
    step2_cmd = 'rhc member update {0} -n cshi -r edit -l {0}'
    step3_cmd = 'rhc member remove {0} -n cshi'
    step4_cmd = 'rhc member add {0} -n cshi -r edit'
    step5_cmd = 'rhc app create teamapp php-5.4'
    step6_cmd = ''
    step7_cmd = 'rhc member remove {0} -n cshi'
    step8_cmd = 'rhc member add {0} -n cshi -r view'
    step9_cmd = 'rhc app start -a teamapp -l {0}'

    step1_check = 'Adding 1 administrator to domain.*done'
    step2_check = 'Updating 1 editor to domain.*done'
    step3_check = 'Removing 1 member from domain.*done'
    step4_check = 'Adding 1 editor to domain.*done'
    step6_check = ''
    step7_check = 'Removing 1 member from domain.*done'
    step8_check = 'Adding 1 viewer to domain.*done'
    step9_check = 'You are not permitted to perform this action'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        self.teamlogin = self.__cfg.get('team_user_login')
        self.teampasswd = self.__cfg.get('team_user_passwd')
        return

    # Test
    def test(self):
        # logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        step1_cmd = self.step1_cmd.format(self.teamlogin)
        check_no_input(step1_cmd, self.step1_check)
        # step 2
        step2_cmd = self.step2_cmd.format(self.login)
        check_no_input(step2_cmd, self.step2_check)
        # step 3
        step3_cmd = self.step3_cmd.format(self.teamlogin)
        check_no_input(step3_cmd, self.step3_check)
        # step 4
        step4_cmd = self.step4_cmd.format(self.teamlogin)
        check_no_input(step4_cmd, self.step4_check)
        # step 5
        check_create_app(self.step5_cmd)
        # step 6
        # step 7
        step7_cmd = self.step7_cmd.format(self.teamlogin)
        check_no_input(step7_cmd, self.step7_check)
        # step 8
        step8_cmd = self.step8_cmd.format(self.teamlogin)
        check_no_input(step8_cmd, self.step8_check)
        # step 9
        step9_cmd = self.step9_cmd.format(self.teamlogin)
        check_no_input(step9_cmd, self.step9_check)
        logger.info('end')

# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
