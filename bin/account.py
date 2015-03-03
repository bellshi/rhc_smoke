#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /bin
# Author : cshi
# Date : 6.Feb.2015

import pexpect
import re

class AccountUtil:

    def __init__(self):
        return

    def delete_all_apps(self):

        child = pexpect.spawn('rhc apps')
        applist_log = file('applist.log','w')
        child.logfile = applist_log
        child.expect(pexpect.EOF)
        applist = open('applist.log').read()
        apps = re.findall(r'(\w+)\s@\shttp',applist)
        if apps:
            for app in apps :
                child = pexpect.spawn('rhc app delete %s --confirm' % app)
                child.expect('Deleting application*deleted')
            print 'All apps deleted.'
        else:
            print 'No apps to be deleted.'
        child.spawn('rm applist.log')

    def init_account(self):
        self.delete_all_apps()
