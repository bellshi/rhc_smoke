#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 6.Mar.2015

import logging
import logging.config
import lib.config
import os
from lib.check import *


class SmokeCase:
    case_name = 'rhc scp verification - 15'

    step1_cmd = 'rhc scp app upload testfile app-root/data'
    step2_cmd = 'rhc ssh app "ls app-root/data"'

    step1_check = 'uploading testfile: 100% complete'
    step2_check = 'testfile'

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
        os.system('echo case15 > testfile')
        check_no_input(self.step1_cmd, self.step1_check)
        # step 2
        check_no_input(self.step2_cmd, self.step2_check)
        # step 3
        os.system('rm testfile')
        os.system('rhc scp app download ./ app-root/data/testfile')
        check_no_input('ls | grep testfile', 'testfile')
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
