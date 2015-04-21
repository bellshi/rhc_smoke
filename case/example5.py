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
    case_name = 'rhc add cartridge verification - 5'

    step1_cmd = 'rhc cartridge add mysql-5.1 -a app'
    step2_cmd = 'rhc cartridge add postgresql-9.2 -a sapp -g medium'

    step1_check = 'MySQL 5.1 database added.'
    step2_check = 'PostgreSQL 9.2 database added'

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
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()

