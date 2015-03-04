#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Mar.2015

import logging
import logging.config
import lib.config
from lib.check import *


class SmokeCase:
    case_name = 'Use rhc to control app and snapshot verification - 9'

    step1_cmd = 'rhc app start -a app'
    step2_cmd = 'rhc app stop -a app'
    step3_cmd = 'rhc snapshot save -a app'
    step4_cmd = 'rhc snapshot restore -a app'
    step5_cmd = 'rhc app show -a app --state'
    step6_cmd = 'rhc app force-stop -a app'
    step7_cmd = 'rhc app restart app'
    step8_cmd = 'rhc app reload app'

    step1_check = 'app started'
    step2_check = 'app stopped'
    step3_check = 'done'
    step4_check = 'done'
    step5_check = 'Cartridge php-5.4 is stopped'
    step6_check = 'app force stopped'
    step7_check = 'app restarted'
    step8_check = 'app config reloaded'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    # Test
    def test(self):
        # debug logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        check_no_input(self.step1_cmd, self.step1_check)
        # step 2
        check_no_input(self.step2_cmd, self.step2_check)
        # step 3
        check_no_input(self.step3_cmd, self.step3_check)
        # step 4
        check_no_input(self.step4_cmd, self.step4_check)
        # step 5
        check_no_input(self.step5_cmd, self.step5_check)
        # step 6
        check_no_input(self.step6_cmd, self.step6_check)
        # step 7
        check_no_input(self.step7_cmd, self.step7_check)
        # step 8
        check_no_input(self.step8_cmd, self.step8_check)
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
