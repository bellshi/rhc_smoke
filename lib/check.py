#!/usr/bin/env python

# check utils used pexpect
# by cshi
# 4.Jan.2015

import pexpect
import logging
import re


# =================== basic =====================
def check_no_input(cmd, check):
    logger = logging.getLogger('check no input')
    child = pexpect.spawn(cmd, timeout=60)
    index = child.expect([check, pexpect.EOF], timeout=None)
    if index == 0:
        logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')


# =================== server =====================
def check_add_server(cmd, account, password):
    logger = logging.getLogger('check add server')
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
    logger = logging.getLogger('check change server')
    child = pexpect.spawn(cmd, timeout=60)
    index = child.expect('Password')
    if index == 0:
        child.sendline(password)
        index = child.expect('Now using')
        if index == 0:
            logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')


# ================= app ==========================
def check_create_app(cmd):
    logger = logging.getLogger('check create app')
    child = pexpect.spawn(cmd)
    index = child.expect(['Are you sure you want to continue connecting', 'Your application \'(\w+)\' is now available'], timeout=None)
    if index == 0:
        child.sendline('yes')
        index = child.expect('Your application \'(\w+)\' is now available')
        if index == 0:
            logger.info('< ' + cmd + ' > [pass]')
    elif index == 1:
        logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')


def compute_app_count():
    logger = logging.getLogger('compute app count')
    child = pexpect.spawn('rhc apps')
    child.expect(pexpect.EOF)
    apps = re.findall(r'(\w+)\s@\shttp', child.before)
    logger.info('app counts : ' + str(apps.__len__()))
    return apps.__len__()


def check_unovercmd_app(cmd, check):
    logger = logging.getLogger('check unovercmd app')
    child = pexpect.spawn(cmd, timeout=20)
    child.expect(pexpect.TIMEOUT)
    log = re.findall(check, child.before)
    if log.__len__() != 0:
        logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.info('< ' + cmd + ' > [fail]')


def get_commit_id():
    logger = logging.getLogger('get commit id')
    child = pexpect.spawn('rhc deployment list -a app')
    child.expect(pexpect.TIMEOUT)
    commid = re.findall(r'deployment (\S+)$', child.before)
    logger.info('commid id : ' + commid[0])
    return commid[0]


def get_haproxy_time(cmd):
    logger = logging.getLogger('get haproxy time')
    child = pexpect.spawn(cmd)
    child.expect(pexpect.EOF)
    haproxy = re.findall(r'haproxy', child.before)
    logger.info('haproxy : ' + str(haproxy.__len__()))
    return haproxy.__len__()



# ================= cartridge ==========================
def check_rhc_caritridge(cmd, check):
    logger = logging.getLogger('check rhc caritridge')
    child = pexpect.spawn(cmd)
    index = child.expect(pexpect.TIMEOUT, timeout=30)
    if index == 0:
        logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')


def get_additional_storage(cmd):
    logger = logging.getLogger('get additional storage')
    child = pexpect.spawn(cmd)
    child.expect(pexpect.EOF)
    storage = re.findall(r'Additional Gear Storage:\s(\d)GB', child.before)
    logger.info('additional storage : ' + storage[0])
    return int(storage[0])


# ================= env ==============================
def check_remove_env(cmd):
    logger = logging.getLogger('check rhc caritridge')
    child = pexpect.spawn(cmd)
    index = child.expect('Are you sure you wish to remove the environment variable\(s\)', timeout=60)
    if index == 0:
        child.sendline('yes')
        index = child.expect('Removing environment variable\(s\).*done')
        if index == 0:
            logger.info('< ' + cmd + ' > [pass]')
    else:
        logger.error('< ' + cmd + ' > [fail]')