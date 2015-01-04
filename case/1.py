#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /case
# Author : cshi
# Date : 4.Jan.2015

import pexpect
import sys
sys.path.append("../lib")
from check import *
from option import *

# Define

case_name = 'rhc setup verification - 1'
case_id = '447862'

#step1_cmd = 'rhc setup -l {0} --server {1}'.format()
step2_cmd = 'rhc setup'
step3_cmd = 'rhc setup --server a.com'

step1_check = 'Your client tools are now configured'
step2_check = 'Your client tools are now configured'
step3_check = 'The OpenShift server is not responding correctly'

# Test

def Test():

    #step 1
    #step 2
    child = pexpect.spawn(step2_cmd)
    index = child.expect(['Enter the server hostname'])
    if index == 0 :
        index = child.sendline()
        index = child.expect([step1_check])
        if index == 0 :
            print 'pass'
        else :
            print 'fail'
    else : 
        print 'fail'
    #step 3

# Debug
# Test()
print Config().getConfig()
