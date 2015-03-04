#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Jan.2015

import logging
import logging.config
import lib.config
from lib.check import check_no_input


class SmokeCase:
    case_name = 'rhc account verification - 3'

    step1_cmd = 'rhc account --server {0}'
    step2_cmd = 'rhc account'

    step1_check = 'Login {0} on {1}'

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
        # step1
        step1 = self.step1_cmd.format(self.server)
        step1_check = self.step1_check.format(self.login, self.server)
        check_no_input(step1, step1_check)
        # step2
        check_no_input(self.step2_cmd, step1_check)
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
