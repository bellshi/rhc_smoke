#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 11.Mar.2015

import logging
import logging.config
import lib.config
from lib.check import *


class SmokeCase:
    case_name = 'rhc authorization verification - 18'

    step1_cmd = 'rhc authorization add --scopes session --note abcd --expire 3600'
    step2_cmd = 'rhc app create qphp php-5.3 --token {0}'
    step3_cmd = 'rhc authorization add --scopes read --note abcd --expire 3600'
    step4_cmd = 'rhc app create qphp2 php-5.3 --token {0}'
    step5_cmd = 'rhc app show qphp --token {0}'
    step6_cmd = 'rhc authorization add --scopes userinfo --note abcd --expire 3600'
    step7_cmd = 'rhc app show qphp --token {0}'
    step8_cmd = 'rhc account --token {0}'
    step9_cmd = 'rhc authorization list'
    step10_cmd = 'rhc authorization delete --auth-token {0}'
    step11_cmd = 'rhc authorization delete-all'

    step1_check = 'Adding authorization.*done'
    step2_check = ''
    step3_check = 'Adding authorization.*done'
    step4_check = 'This action is not allowed with your current authorization'
    step5_check = 'php-5.3 \(PHP 5.3\)'
    step6_check = 'Adding authorization.*done'
    step7_check = 'This action is not allowed with your current authorization'
    step8_check = 'Login {0} on {1}'
    step9_check = ''
    step10_check = 'Deleting authorization.*done'
    step11_check = 'Deleting all authorizations.*done'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    # Test
    def test(self):
        logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        token1 = check_rhc_authorization(self.step1_cmd)
        if token1 == '':
            logger.error('token is null [fail]')
            return
        # step 2
        print token1
        step2_cmd = self.step2_cmd.format(token1)
        check_create_app(step2_cmd)
        # step 3
        token2 = check_rhc_authorization(self.step3_cmd)
        if token2 == '':
            logger.error('token is null [fail]')
            return
        # step 4
        print token2
        step4_cmd = self.step4_cmd.format(token2)
        check_no_input(step4_cmd, self.step4_check)
        # step 5
        step5_cmd = self.step5_cmd.format(token2)
        check_no_input(step5_cmd, self.step5_check)
        # step 6
        token3 = check_rhc_authorization(self.step6_cmd)
        if token3 == '':
            logger.error('token is null [fail]')
            return
        # step 7
        print token3
        step7_cmd = self.step7_cmd.format(token3)
        check_no_input(step7_cmd, self.step7_check)
        # step 8
        step8_cmd = self.step8_cmd.format(token3)
        step8_check = self.step8_check.format(self.login, self.server)
        check_no_input(step8_cmd, step8_check)
        # step 9
        check_authorization_list(self.step9_cmd)
        # step 10
        # step10_cmd = self.step10_cmd.format(token3)
        # check_no_input(step10_cmd, self.step10_check)
        # step 11
        # check_no_input(self.step11_cmd, self.step11_check)
        # step 12
        check_authorization_list_after_delete_all(self.password)
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
__author__ = 'cfshi'
