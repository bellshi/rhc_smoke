#!/usr/bin/env python

# check utils used pexpect
# by cshi
# 4.Jan.2015

import pexpect
import logging


def check_no_input(cmd, check):
    logger = logging.getLogger('check_no_input')
    child = pexpect.spawn(cmd, timeout=60)
    index = child.expect([check, pexpect.EOF])
    if index == 0:
        logger.info('<' + cmd + '> [pass]')
    else:
        logger.error('<' + cmd + '> Time out [fail]')
