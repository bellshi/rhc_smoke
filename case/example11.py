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
    case_name = 'rhc cartridge scale verification - 11'

    step1_cmd = 'rhc cartridge scale php-5.4 -a sapp --min 2 --max 4'
    step2_cmd = 'rhc app scale-up -a sapp'
    step3_cmd = 'rhc app scale-down -a sapp'
    step4_cmd = 'rhc cartridge scale php-5.4 -a sapp --min 1'
    step5_cmd = 'rhc app scale-down sapp'

    step1_check = 'Scaling: x2 \(minimum: 2, maximum: 4\) on small gears'
    step2_check_c = 'sapp scaled up'
    step2_check_w = 'Cannot scale up above maximum gear limit of 4'
    step3_check_c = 'sapp scaled down'
    step3_check_w = 'Cannot scale down below gear limit of 24'
    step4_check = 'Scaling: x2 \(minimum: 1, maximum: 4\) on small gears'
    step5_check = 'sapp scaled down'

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
        check_no_input(self.step1_cmd, self.step1_check)
        # step 2
        check_no_input(self.step2_cmd, self.step2_check_c)
        check_no_input(self.step2_cmd, self.step2_check_c)
        check_no_input(self.step2_cmd, self.step2_check_w)
        # step 3
        check_no_input(self.step3_cmd, self.step3_check_c)
        check_no_input(self.step3_cmd, self.step3_check_c)
        check_no_input(self.step3_cmd, self.step3_check_w)
        # step 4
        check_no_input(self.step4_cmd, self.step4_check)
        # step 5
        check_no_input(self.step5_cmd, self.step5_check)
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
