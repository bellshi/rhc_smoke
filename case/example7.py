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
    case_name = 'rhc env verification - 7'

    step1_cmd = 'rhc env set a= b=123 -a app'
    step2_cmd = 'rhc env list -a app'
    step3_cmd = 'rhc env show -a app -e a'
    step4_cmd = 'rhc env unset -a app -e a -e b'

    step1_check = 'Setting environment variable\(s\).*done'
    step2_check = 'a='
    step3_check = 'b=123'

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
        check_no_input(self.step2_cmd, self.step2_check)
        check_no_input(self.step2_cmd, self.step3_check)
        # step 3
        check_no_input(self.step3_cmd, self.step2_check)
        # step 4
        check_remove_env(self.step4_cmd)
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
