#!/usr/bin/env python

# check utils used pexpect
# by cshi
# 4.Jan.2015

import pexpect

def check_no_input(cmd,check):
    child = pexpect.spawn(cmd)
    while True:
        index = child.expect([check,pexpect.EOF,pexpect.TIMEOUT])
        if(index == 0):
            print 'Pass'
            break
        elif(index == 2):
            pass
        else:
            print 'Fail'
            break
