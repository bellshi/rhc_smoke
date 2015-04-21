#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Jan.2015

import logging
import logging.config
import lib.config
from lib.check import *
import pexpect


class SmokeCase:
    case_name = 'rhc setup verification - 1'
    case_id = '447862'

    step1_cmd = 'rhc setup -l {0} --server {1}'
    step2_cmd = 'rhc setup'
    step3_cmd = 'rhc setup --server {0}'

    step1_check = 'Your client tools are now configured'
    step2_check = 'Your client tools are now configured'
    step3_check = 'Your client tools are now configured'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    def test(self):
        #logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        step1 = self.step1_cmd.format(self.login, self.server)
        check_init_server(step1, self.step1_check, self.password)
        # step 2
        child = pexpect.spawn(self.step2_cmd)
        index = child.expect(['Enter the server hostname', pexpect.EOF])
        if index == 0:
            child.sendline()
            index = child.expect([self.step2_check, pexpect.TIMEOUT])
            if index == 0:
                logger.info('<' + self.step2_cmd + '> [pass]')
        else:
            logger.error(self.step2_cmd + ' Time out [fail]')
        # step 3
        step3 = self.step3_cmd.format(self.server)
        check_no_input(step3, self.step3_check)
        logger.info('end')

# DEBUG
#cfg = lib.config.setup()
#SmokeCase(cfg).test()

