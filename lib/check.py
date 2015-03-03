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
        logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')


def check_add_server(cmd, account, password):
    logger = logging.getLogger('check_add_server')
    child = pexpect.spawn(cmd, timeout=60)
    index = child.expect('Login to')
    if index == 0:
        child.sendline(account)
        index = child.expect('Password')
        if index == 0:
            child.sendline(password)
            index = child.expect('Generate a token')
            if index == 0:
                child.sendline('yes')
                index = child.expect('Saving server configuration to')
                if index == 0:
                    logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + '> [fail]')


def check_change_server(cmd, password):
    logger = logging.getLogger('check_change_server')
    child = pexpect.spawn(cmd, timeout=60)
    index = child.expect('Password')
    if index == 0:
        child.sendline(password)
        index = child.expect('Now using')
        if index == 0:
            logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')