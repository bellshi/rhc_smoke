#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /bin
# Author : cshi
# Date : 6.Feb.2015

import pexpect
import re


def delete_all_apps():
    child = pexpect.spawn('rhc apps')
    child.expect([pexpect.EOF, pexpect.TIMEOUT])
    apps = re.findall(r'.+?(?=\s@)', child.before)
    if apps:
        for app in apps:
            child = pexpect.spawn('rhc app delete %s --confirm' % app)
            child.expect(['Deleting application.*deleted', pexpect.TIMEOUT])
        print 'All apps deleted.'
    else:
        print 'No apps to be deleted.'


# Main
delete_all_apps()