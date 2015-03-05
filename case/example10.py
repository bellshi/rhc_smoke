#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Mar.2015

import logging
import logging.config
import os
import lib.config
from lib.check import *


class SmokeCase:
    case_name = 'rhc deploy process verification - 10'

    step1_cmd = 'rhc app-configure -a app --no-auto-deploy --deployment-type binary'
    step2_cmd = 'rhc git-clone app'
    step3_cmd = 'rhc snapshot save app --deployment'
    step4_cmd = 'rhc deploy -a app --ref app.tar.gz --hot-deploy'
    step5_cmd = 'rhc app-configure -a app --auto-deploy --deployment-type git --keep-deployments 2'
    step7_cmd = 'rhc deployment list -a app'
    step8_cmd = 'rhc deployment activate {0} -a app'
    step10_cmd = 'rhc deployment show {0} -a app'

    step1_check = 'Deployment Type.*binary'
    step2_check = 'Your application Git repository has been cloned to'
    step3_check = 'done'
    step4_check = 'done'
    step5_check = 'Deployment Type.*git'
    step7_check = 'deployment'
    step8_check = 'Success'
    step9_check = '.*deployment.*\(rollback to.*PM\)$'
    step10_check ='Activations'

    def __init__(self, config):
        self.__cfg = config
        self.login = self.__cfg.get('default_rhlogin')
        self.server = self.__cfg.get('libra_server')
        self.password = self.__cfg.get('default_rhpasswd')
        return

    # Test
    def test(self):
        logging.config.fileConfig('../config/log.conf')
        logger = logging.getLogger(self.case_name)
        logger.info('begin')
        # step 1
        check_no_input(self.step1_cmd, self.step1_check)
        # step 2
        os.system("rm -rf app")
        check_no_input(self.step2_cmd, self.step2_check)
        # step 3
        check_no_input(self.step3_cmd, self.step3_check)
        # step 4
        # !!!!!!Problem
        os.system("mv app/ app.bak/")
        os.system("mkdir app | tar xzf app.tar.gz -C app")
        os.system("sed -i 's/Welcome to your PHP application on OpenShift/Modifying/g' app/repo/index.php")
        #os.system("rm app.tar.gz")
        os.system("mv app.tar.gz appb.tar.gz")
        os.system("tar czf app.tar.gz app/* ")
        os.system("rm -rf app")
        #os.system("mv app.bak/ app/")
        check_no_input(self.step4_cmd, self.step4_check)
        # step 5
        check_no_input(self.step5_cmd, self.step5_check)
        # step 6

        # step 7
        check_no_input(self.step7_cmd, self.step7_check)
        # step 8
        commit_id = get_commit_id()
        step8_cmd = self.step8_cmd.format(commit_id)
        check_no_input(step8_cmd, self.step8_check)
        # step 9
        check_no_input(self.step7_cmd, self.step9_check)
        # step 10
        step10_cmd = self.step10_cmd.format(commit_id)
        check_no_input(step10_cmd, self.step10_check)
        logger.info('end')


# Debug
cfg = lib.config.setup()
SmokeCase(cfg).test()
