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
    case_name = 'rhc create app verification - 4'

    step1_cmd = 'rhc app create app php-5.4'
    step2_cmd = 'rhc app create app2 php-5.4 -g medium'
    step3_cmd = 'rhc app create app3 php-5.4 mysql-5.5'
    step4_cmd = 'rhc app create sapp php-5.4 -s'
    step5_cmd = 'rhc app create app4 --from-app app'
    step6_cmd = 'rhc app create app5 php-5.4 mysql-5.1 --from-code https://github.com/openshift/wordpress-example.git -s'
    step7_cmd = 'rhc app create app6 php-5.4 --enable-jenkins'

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
        check_create_app(self.step1_cmd)
        # step 2
        check_create_app(self.step2_cmd)
        # step 3
        check_create_app(self.step3_cmd)
        # step 4
        check_create_app(self.step4_cmd)
        # step 5
        check_create_app(self.step5_cmd)
        # step 6
        check_create_app(self.step6_cmd)
        # step 7
        check_create_app(self.step7_cmd)
        logger.info('end')


# Debug
#cfg = lib.config.setup()
#SmokeCase(cfg).test()
