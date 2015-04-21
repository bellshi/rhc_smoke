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
    case_name = 'rhc cartridge control verification - 12'

    step1_cmd = 'rhc cartridge {0} -a app -c php-5.4 '
    step2_cmd = 'rhc cartridge add mysql-5.1 -a app'
    step3_cmd = 'rhc cartridge storage -a app -c mysql-5.1'
    step4_cmd = 'rhc cartridge storage --add 1GB -a app -c mysql-5.1'
    step5_cmd = 'rhc cartridge remove mysql-5.1 -a app --confirm'

    step1_check = '{0}ing php-5.4.*done'
    step2_check = 'MySQL 5.1 database added'
    step3_check = 'Additional Gear Storage:'
    step4_check = 'Additional Gear Storage:\s{0}GB'
    step5_check = 'Removing mysql-5.1 from \'app\'.*removed'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    # Test
    def test(self):
        # logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        operate = ['stop', 'start', 'restart', 'reload']
        for op in operate:
            step_cmd = self.step1_cmd.format(op)
            step_check = self.step1_check.format(((op+'p').capitalize()) if op == 'stop' else op.capitalize())
            check_no_input(step_cmd, step_check)
        step1_5_cmd = self.step1_cmd.format('status')
        step1_5_check = 'Application is running'
        check_no_input(step1_5_cmd, step1_5_check)
        # step 2
        check_no_input(self.step2_cmd, self.step2_check)
        # step 3
        check_no_input(self.step3_cmd, self.step3_check)
        # step 4
        storage = get_additional_storage(self.step3_cmd)
        step4_check = self.step4_check.format(storage+1)
        check_no_input(self.step4_cmd, step4_check)
        # step 5
        check_no_input(self.step5_cmd, self.step5_check)
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
