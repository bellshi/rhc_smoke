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
    case_name = 'rhc enable-ha verification - 13'

    step1_cmd = 'rhc app enable-ha sapp'
    step2_cmd = 'rhc app show sapp --gears'

    step1_check = 'sapp is now highly available'
    step2_check = ''

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        # debug self.server = 'dsadfxe'
        self.password = self.__cfg.get('default_rhpasswd')
        return

    # Test
    def test(self):
        # debug logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        if 'int' not in self.server and 'stg' not in self.server:
            # step 1
            check_no_input(self.step1_cmd, self.step1_check)
            # step 2
            haproxy = get_haproxy_time(self.step2_cmd)
            if haproxy == 2:
                logger.info('< check gears for haproxy > [pass]')
            else:
                logger.info('< check gears for haproxy > [fail]')

        else:
            logger.info('This case is only for devenv [pass]')
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
