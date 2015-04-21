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
    case_name = 'rhc tail/port-forward/threaddump verification - 8'

    step1_cmd = 'rhc tail app'
    step2_cmd = 'rhc port-forward app'
    step3_cmd = 'rhc app create ajboss jbossas-7'
    step4_cmd = 'rhc threaddump ajboss'

    step1_check = 'SELinux policy enabled'
    step2_check = 'Checking available ports.*done'
    step3_check = 'Success'

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
        check_unovercmd_app(self.step1_cmd, self.step1_check)
        # step 2
        check_unovercmd_app(self.step2_cmd, self.step2_check)
        # step 3
        check_create_app(self.step3_cmd)
        check_no_input(self.step4_cmd, self.step3_check)
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
