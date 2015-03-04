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
    case_name = 'rhc apps and cartridges verification - 6'

    step1_cmd = 'rhc apps'
    step2_cmd = 'rhc apps --summary'
    step3_cmd = 'rhc apps --mine'
    step4_cmd = 'rhc cartridges'

    step1_check = 'You have.* {0} application'
    step4_check = 'Note: Web cartridges can only be added to new applications.'

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
        count = compute_app_count()
        if count == 0:
            step1_check = 'No applications.'
        else:
            step1_check = self.step1_check.format(count)
        check_no_input(self.step1_cmd, step1_check)
        # step 2
        check_no_input(self.step2_cmd, step1_check)
        # step 3
        check_no_input(self.step3_cmd, step1_check)
        # step 4
        check_rhc_caritridge(self.step4_cmd, self.step4_check)
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()

