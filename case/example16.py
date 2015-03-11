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
    case_name = 'rhc team verification - 16'

    step1_cmd = 'rhc team create smoke'
    step2_cmd = 'rhc team list'
    step3_cmd = 'rhc team show smoke'
    step4_cmd = 'rhc member add {0} -t smoke'
    step5_cmd = 'rhc member add smoke -n cshi --type team -r admin'
    step6_cmd = 'rhc member list -n cshi'
    step7_cmd = 'rhc member list -n cshi --all'
    step8_cmd = 'rhc member remove smoke -n cshi --type team'
    step9_cmd = 'rhc team leave -t smoke'
    step10_cmd = 'rhc team leave -t smoke -l {0}'

    step1_check = 'Creating team \'smoke\'.*done'
    step2_check = 'Team smoke'
    step3_check = 'Team smoke'
    step4_check = 'Adding 1 viewer to team.*done'
    step5_check = 'Adding 1 administrator to domain.*done'
    step6_check = 'team'
    step8_check = 'Removing 1 member from domain.*done'
    step9_check = 'You are the owner of this team and cannot leave'

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
        check_no_input(self.step1_cmd, self.step1_check)
        # step 2
        check_no_input(self.step2_cmd, self.step2_check)
        # step 3
        check_no_input(self.step3_cmd, self.step3_check)
        # step 4
        step4_cmd = self.step4_cmd.format(self.teamlogin)
        check_no_input(step4_cmd, self.step4_check)
        # step 5
        check_no_input(self.step5_cmd, self.step5_check)
        # step 6
        check_no_input(self.step6_cmd, self.step6_check)
        # step 7
        check_no_input(self.step7_cmd, self.teamlogin)
        # step 8
        check_no_input(self.step8_cmd, self.step8_check)
        # step 9
        check_no_input(self.step9_cmd, self.step9_check)
        # step 10
        step10_cmd = self.step10_cmd.format(self.teamlogin)
        check_leave_team(step10_cmd, self.password, self.teampasswd)
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
