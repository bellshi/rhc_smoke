#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Jan.2015

import logging
import logging.config
import lib.config
from lib.check import check_no_input
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
        return

    def test(self):
        # debug logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        step1 = self.step1_cmd.format(self.login, self.server)
        check_no_input(step1, self.step1_check)
        # step 2
        child = pexpect.spawn(self.step2_cmd, timeout=60)
        index = child.expect('Enter the server hostname')
        if index == 0:
            child.sendline()
            index = child.expect(self.step2_check)
            if index == 0:
                logger.info('<' + self.step2_cmd + '> [pass]')
        else:
            logger.error(self.step2_cmd + ' Time out [fail]')
        # step 3
        step3 = self.step3_cmd.format(self.server)
        check_no_input(step3, self.step3_check)
        logger.info('end')

        #log.info('begin')
        #step1 = self.step1_cmd.format(self.login, self.server)
        #child = pexpect.spawn(step1, timeout=None)
        #index = child.expect(self.step1_check)
        #print child.before
        #if index == 0:
        #   log.info(step1 + ' [pass]')
        #else:
        #   log.error(step1 + ' [fail]')
        #child = pexpect.spawn(self.step2_cmd, timeout=None)
        #index = child.expect(self.step2_check)
        #if index == 0:
        #   log.info(self.step2_cmd + ' [pass]')
        #else:
        #   log.error(self.step2_cmd + ' [fail]')
        #step3 = self.step3_cmd.format(self.server)
        #child = pexpect.spawn(step3, timeout=None)
        #index = child.expect(self.step3_check)
        #if index == 0:
        #   log.info(step3 + ' [pass]')
        #else:
        #   log.error(step3 + ' [fail]')
        #step 1
        #step 2
        # child = pexpect.spawn(step2_cmd)
        # index = child.expect(['Enter the server hostname'])
        # if index == 0 :
        #     index = child.sendline()
        #     index = child.expect([step1_check])
        #     if index == 0 :
        #         print 'pass'
        #     else :
        #         print 'fail'
        # else :
        #     print 'fail'
        #step 3

# DEBUG
cfg = lib.config.setup()
SmokeCase(cfg).test()

