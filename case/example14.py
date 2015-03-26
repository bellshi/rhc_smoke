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
    case_name = 'rhc alias verification - 14'

    step1_cmd = 'rhc alias add app.com -a app'
    step2_cmd = 'rhc alias list -a app'
    step3_cmd = 'rhc update-cert-alias app app.com --certificate ../config/server.crt --private-key ../config/server.key'
    step4_cmd = 'rhc alias delete-cert app app.com --confirm'
    step5_cmd = 'rhc alias remove app.com -a app'

    step1_check = 'Alias \'app.com\' has been added'
    step2_check = 'app.com'
    step3_check = 'SSL certificate successfully added'
    step4_check = 'SSL certificate successfully deleted'
    step5_check = 'Alias \'app.com\' has been removed'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    # Test
    def test(self):
        #logging.config.fileConfig('../config/log.conf')
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
        logger.info('end')


# Debug
# cfg = lib.config.setup()
# SmokeCase(cfg).test()
